// Read-only by default. Repairs reuse the normal publisher's atomic transaction
// and existing embedding; they do not rewrite skill instructions or aliases.
const fs = require('node:fs')
const path = require('node:path')
const { execFileSync } = require('node:child_process')
const { readSkillBundle, publicationQueries } = require('./embed-skills')

function parseSlugs(value = '') {
  const slugs = [...new Set(value.split(/[\s,]+/).filter(Boolean))]
  if (slugs.some(slug => !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug))) throw new Error('Invalid repair slug')
  if (slugs.length > 20) throw new Error('At most 20 explicit repair slugs per reviewed run')
  return slugs
}

function compareBundle(bundle, root, sources, companions) {
  if (!root || root.visibility !== 'public') return ['root:not-public-or-missing']
  const differences = []
  const expected = new Map(bundle.files.map(file => [file.path, file]))
  const published = new Map(sources.map(file => [file.path, file]))
  for (const file of bundle.files) {
    const stored = published.get(file.path)
    const language = file.encoding === 'base64' ? `base64:${file.contentType}` : file.path.endsWith('.md') ? 'markdown' : 'text'
    if (!stored || stored.content !== file.content || stored.size_bytes !== file.sizeBytes || stored.language !== language)
      differences.push(`source:${file.path}`)
    if (file.path === 'SKILL.md') continue
    const companion = companions.find(row => row.slug === `${bundle.slug}--file--${file.path}`)
    if (!companion || companion.visibility !== 'public' || companion.content !== file.content ||
      !companion.tags?.includes('__bundle_file') || !companion.tags?.includes(`__content_type:${file.contentType}`) ||
      companion.tags.includes('__bundle_base64') !== (file.encoding === 'base64'))
      differences.push(`mcp:${file.path}`)
  }
  for (const stored of sources) if (!expected.has(stored.path)) differences.push(`removed-source:${stored.path}`)
  for (const stored of companions) {
    const relative = stored.slug.slice(`${bundle.slug}--file--`.length)
    if (stored.visibility === 'public' && !expected.has(relative)) differences.push(`removed-mcp:${relative}`)
  }
  return differences
}

function validateRepair(bundle, root) {
  // Never revive an archived root, overwrite a newer instruction edit, or alter
  // public metadata as a side effect of recovering its missing source files.
  const sameTags = root && JSON.stringify([...(root.tags || [])].sort()) === JSON.stringify([...bundle.tags].sort())
  if (!root || root.visibility !== 'public' || root.content !== bundle.content || root.name !== bundle.name ||
    root.summary !== bundle.summary || root.license !== bundle.license || root.language !== bundle.language || !sameTags || !root.embedding)
    throw new Error(`Refusing repair: ${bundle.slug} root must already match the public repository and have an embedding`)
  return typeof root.embedding === 'string' ? JSON.parse(root.embedding) : root.embedding
}

async function repairBundle(sql, bundle, root, domain) {
  const embedding = validateRepair(bundle, root)
  // Lock and recheck the reviewed version in the same transaction as the normal
  // publisher. Concurrent edits/retirement fail closed and roll back every file.
  const guard = sql.query(`WITH locked AS (
    SELECT id FROM content.skills WHERE slug=$1 AND domain=$2
      AND visibility='public' AND version=$3 FOR UPDATE
    ) SELECT 1 / count(*)::int AS version_guard FROM locked`, [bundle.slug, domain, root.version])
  return sql.transaction([guard, ...publicationQueries(sql, bundle, domain, embedding)])
}

async function inventoryBundles(sql, domain, slugs = [], repoRoot = process.cwd()) {
  if (!['legal', 'med', 'finance', 'capital'].includes(domain)) throw new Error('Unsupported domain')
  const paths = execFileSync('git', ['ls-files', '-z', '--', `skills/${domain}/`], { cwd: repoRoot, encoding: 'utf8' })
    .split('\0').filter(file => file.endsWith('/SKILL.md') && file.split('/').length === 4)
  const reserved = JSON.parse(fs.readFileSync(path.join(repoRoot, 'spec/reserved-slugs.json'), 'utf8'))[domain] || {}
  const available = new Set(paths.map(file => file.split('/')[2]))
  if (slugs.some(slug => !available.has(slug) || Object.hasOwn(reserved, slug))) throw new Error('Unknown or retired repair slug')
  const bundles = paths.filter(file => !slugs.length || slugs.includes(file.split('/')[2]))
    .map(file => readSkillBundle(file, repoRoot)).filter(bundle => slugs.length || bundle.files.length > 1)
  const roots = await sql.query(`SELECT slug,name,summary,content,tags,license,language,visibility,version,embedding
    FROM content.skills WHERE domain=$1`, [domain])
  const sources = await sql.query(`SELECT s.slug,f.path,f.content,f.language,f.size_bytes
    FROM content.skill_source_files f JOIN content.skills s ON s.id=f.skill_id WHERE s.domain=$1`, [domain])
  return bundles.map(bundle => {
    const root = roots.find(row => row.slug === bundle.slug)
    const differences = compareBundle(bundle, root, sources.filter(row => row.slug === bundle.slug),
      roots.filter(row => row.slug.startsWith(`${bundle.slug}--file--`)))
    return { bundle, root, differences }
  })
}

async function main() {
  const { neon } = require('@neondatabase/serverless')
  const domain = process.env.SKILL_DOMAIN || 'legal'
  const slugs = parseSlugs(process.env.REPAIR_SLUGS)
  const apply = process.env.APPLY_REPAIR === 'true'
  const sha = execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim()
  if (apply && (!slugs.length || process.env.APPROVED_SHA !== sha))
    throw new Error('Applying a repair requires explicit slugs and the exact approved checkout SHA')
  const sql = neon(process.env.SKILLS_DB_URL)
  const inventory = await inventoryBundles(sql, domain, slugs)
  console.log(JSON.stringify({ sha, domain, mode: apply ? 'repair' : 'dry-run',
    bundles: inventory.map(({ bundle, differences }) => ({ slug: bundle.slug, files: bundle.files.length, differences })) }, null, 2))
  if (!apply) return
  // Validate the entire selected batch before the first write.
  for (const { bundle, root } of inventory) {
    validateRepair(bundle, root)
  }
  for (const { bundle, root, differences } of inventory) {
    if (!differences.length) continue
    await repairBundle(sql, bundle, root, domain)
    console.log(`Repaired ${domain}/${bundle.slug} (${bundle.files.length} files)`)
  }
  const after = await inventoryBundles(sql, domain, slugs)
  if (after.some(item => item.differences.length)) throw new Error('Repair verification failed')
}

if (require.main === module) main().catch(error => { console.error(error.message); process.exitCode = 1 })
module.exports = { parseSlugs, compareBundle, repairBundle, inventoryBundles }
