const fs = require('node:fs')
const path = require('node:path')
const { execFileSync } = require('node:child_process')
const { TextDecoder } = require('node:util')
const yaml = require('yaml')

const FILE_SEPARATOR = '--file--'
function readSkillBundle(filePath, repoRoot = process.cwd()) {
  const fullPath = path.resolve(repoRoot, filePath)
  const raw = fs.readFileSync(fullPath, 'utf8')
  const match = raw.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/)
  if (!match) throw new Error(`Invalid frontmatter in ${filePath}`)
  const meta = yaml.parse(match[1])
  const content = match[2].trim()
  const slug = meta.name
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug) || slug !== path.basename(path.dirname(fullPath))) {
    throw new Error(`Invalid or mismatched skill slug in ${filePath}`)
  }
  const files = execFileSync('git', ['ls-files', '-z', '--', path.dirname(filePath)], { cwd: repoRoot, encoding: 'utf8' })
    .split('\0').filter(Boolean).sort().map((trackedPath) => {
      const absolute = path.resolve(repoRoot, trackedPath)
      if (fs.lstatSync(absolute).isSymbolicLink()) throw new Error(`Symlink in skill bundle: ${trackedPath}`)
      const relative = path.relative(path.dirname(fullPath), absolute).split(path.sep).join('/')
      const bytes = fs.readFileSync(absolute)
      let encoding = 'utf8', text
      try {
        new TextDecoder('utf-8', { fatal: true }).decode(bytes)
        text = bytes.toString('utf8')
        if (text.includes('\0')) throw new Error('Binary source file')
      }
      catch { encoding = 'base64'; text = bytes.toString('base64') }
      const contentType = relative.endsWith('.md') ? 'text/markdown' : relative.endsWith('.pdf') ? 'application/pdf' : 'text/plain'
      return { path: relative, content: text, sizeBytes: bytes.length, encoding, contentType }
    })
  const title = content.match(/^#\s+(.+)$/m) || content.match(/^\*\*([^*]+)\*\*/m)
  return { slug, name: title ? title[1].trim() : slug, summary: meta.description,
    content, tags: meta.tags || [], license: meta.license || 'Apache-2.0', language: meta.language || 'en', files }
}

function publicationQueries(sql, skill, domain, embedding) {
  const queries = [sql.query(`
    INSERT INTO content.skills (slug, name, summary, content, embedding, tags, license, language, domain, visibility, version, created_at, updated_at)
    VALUES ($1,$2,$3,$4,$5::vector,$6,$7,$8,$9,'public',1,NOW(),NOW())
    ON CONFLICT (slug,domain) DO UPDATE SET name=EXCLUDED.name, summary=EXCLUDED.summary,
      content=EXCLUDED.content, embedding=EXCLUDED.embedding, tags=EXCLUDED.tags,
      license=EXCLUDED.license, language=EXCLUDED.language, version=content.skills.version+1,
      visibility='public', updated_at=NOW()
  `, [skill.slug, skill.name, skill.summary, skill.content, JSON.stringify(embedding), skill.tags, skill.license, skill.language, domain])]
  queries.push(sql.query(`DELETE FROM content.skill_source_files WHERE skill_id IN
    (SELECT id FROM content.skills WHERE slug=$1 AND domain=$2)`, [skill.slug, domain]))
  const companions = skill.files.filter((file) => file.path !== 'SKILL.md')
  const companionSlugs = companions.map((file) => `${skill.slug}${FILE_SEPARATOR}${file.path}`)
  // Archive removed files; existing companion versions only change on an upsert.
  queries.push(sql.query(`UPDATE content.skills SET visibility='archived', updated_at=NOW()
    WHERE domain=$1 AND starts_with(slug,$2) AND NOT (slug = ANY($3::text[]))`,
    [domain, `${skill.slug}${FILE_SEPARATOR}`, companionSlugs]))
  for (const file of skill.files) {
    const language = file.encoding === 'base64' ? `base64:${file.contentType}` : file.path.endsWith('.md') ? 'markdown' : 'text'
    queries.push(sql.query(`INSERT INTO content.skill_source_files (skill_id,path,content,language,size_bytes)
      SELECT id,$3,$4,$5,$6 FROM content.skills WHERE slug=$1 AND domain=$2`,
      [skill.slug, domain, file.path, file.content, language, file.sizeBytes]))
    if (file.path === 'SKILL.md') continue
    const tags = ['__bundle_file', `__content_type:${file.contentType}`]
    if (file.encoding === 'base64') tags.push('__bundle_base64')
    queries.push(sql.query(`INSERT INTO content.skills
      (slug,name,summary,content,tags,license,language,domain,visibility,version,created_at,updated_at)
      VALUES ($1,$2,$3,$4,$5,$6,$7,$8,'public',1,NOW(),NOW())
      ON CONFLICT (slug,domain) DO UPDATE SET name=EXCLUDED.name,summary=EXCLUDED.summary,
        content=EXCLUDED.content,tags=EXCLUDED.tags,license=EXCLUDED.license,language=EXCLUDED.language,
        visibility='public',version=content.skills.version+1,updated_at=NOW()`,
      [`${skill.slug}${FILE_SEPARATOR}${file.path}`, file.path, `Companion file for ${skill.slug}: ${file.path}`,
        file.content, tags, skill.license, skill.language, domain]))
  }
  return queries
}

async function publishSkill(sql, skill, domain, embedding) {
  // The root, source manifest and MCP companion rows become visible together.
  await sql.transaction(publicationQueries(sql, skill, domain, embedding))
}

async function main() {
  const { neon } = require('@neondatabase/serverless')
  const { OpenAI } = require('openai')
  const sql = neon(process.env.SKILLS_DB_URL)
  const domain = process.env.SKILL_DOMAIN
  const reserved = JSON.parse(fs.readFileSync('spec/reserved-slugs.json', 'utf8'))[domain] || {}
  const openai = new OpenAI({ apiKey: process.env.AI_GATEWAY_API_KEY, baseURL: 'https://ai-gateway.vercel.sh/v1' })
  for (const filePath of (process.env.ADDED_SKILL_PATHS || '').split('\n').filter(Boolean)) {
    const skill = readSkillBundle(filePath)
    if (Object.hasOwn(reserved, skill.slug)) throw new Error(`Retired alias cannot be republished: ${skill.slug}`)
    const result = await openai.embeddings.create({ model: 'text-embedding-3-small', dimensions: 1536,
      input: `${skill.name}: ${skill.summary}\n\n${skill.content}` })
    await publishSkill(sql, skill, domain, result.data[0].embedding)
    console.log(`Published ${domain}/${skill.slug} (${skill.files.length} files)`)
  }
  // A failed publish aborts before any retired root is archived.
  for (const filePath of (process.env.DELETED_SKILL_PATHS || '').split('\n').filter(Boolean)) {
    const slug = path.basename(path.dirname(filePath))
    await sql.query(`UPDATE content.skills SET visibility='archived',updated_at=NOW()
      WHERE domain=$1 AND (slug=$2 OR starts_with(slug,$3))`, [domain, slug, `${slug}${FILE_SEPARATOR}`])
    console.log(`Archived ${domain}/${slug}`)
  }
}
if (require.main === module) main().catch((error) => { console.error(error); process.exitCode = 1 })
module.exports = { readSkillBundle, publishSkill, publicationQueries }
