const assert = require('node:assert/strict')
const fs = require('node:fs')
const os = require('node:os')
const path = require('node:path')
const { execFileSync } = require('node:child_process')
const test = require('node:test')
const { PGlite } = require('@electric-sql/pglite')
const { readSkillBundle, publishSkill, verifyRetirementSnapshots } = require('./embed-skills')
const { changedSkills } = require('./changed-skills')

test('reserved root retirement requires the original snapshots before publication', async () => {
  const reserved = { 'form-d': 'form-d-exempt-offering-notice', 'form-d-notice': 'form-d-exempt-offering-notice' }
  const deleted = ['skills/legal/form-d/SKILL.md', 'skills/legal/form-d-notice/SKILL.md']
  const snapshots = Object.keys(reserved).map(alias_slug => ({ alias_slug,
    target_slug: reserved[alias_slug], archived_content: 'Original v5 content', archived_version: 5 }))
  const sql = { query: async (_text, [domain, alias, target]) => [{ ready: snapshots.some(s =>
    s.alias_slug === alias && s.target_slug === target && s.archived_content && s.archived_version != null) }] }
  await verifyRetirementSnapshots(sql, 'legal', deleted, reserved)
  snapshots.pop()
  await assert.rejects(verifyRetirementSnapshots(sql, 'legal', deleted, reserved), /Missing original snapshot/)
  snapshots.push({ alias_slug: 'form-d-notice', target_slug: 'wrong-target', archived_content: 'Original', archived_version: 5 })
  await assert.rejects(verifyRetirementSnapshots(sql, 'legal', deleted, reserved), /Missing original snapshot/)
  let queried = false
  await verifyRetirementSnapshots({query: async () => { queried = true }}, 'legal', ['skills/legal/ordinary/SKILL.md'], reserved)
  assert.equal(queried, false)
})

function fixture() {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'skill-publish-'))
  execFileSync('git', ['init', '-q', root])
  const dir = path.join(root, 'skills/legal/test-skill')
  fs.mkdirSync(path.join(dir, 'references'), { recursive: true })
  fs.writeFileSync(path.join(dir, 'SKILL.md'), '---\nname: test-skill\ndescription: Test skill\n---\n# Test Skill\nRead references/rules.md.\n')
  fs.writeFileSync(path.join(dir, 'references/rules.md'), '# Rules\nCurrent rules.\n')
  fs.writeFileSync(path.join(dir, 'example.pdf'), Buffer.from([0xff, 0xfe, 0x00, 0x01]))
  execFileSync('git', ['add', '.'], { cwd: root })
  execFileSync('git', ['-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'fixture'], { cwd: root })
  return root
}

async function database() {
  const db = new PGlite()
  await db.exec(`CREATE DOMAIN vector AS text;
    CREATE SCHEMA content;
    CREATE TABLE content.skills (id uuid PRIMARY KEY DEFAULT gen_random_uuid(), slug text NOT NULL,
      name text, summary text, content text NOT NULL, embedding vector, tags text[], license text,
      language text, domain text NOT NULL, visibility text, version integer, created_at timestamptz,
      updated_at timestamptz, UNIQUE(slug,domain));
    CREATE TABLE content.skill_source_files (id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
      skill_id uuid REFERENCES content.skills(id), path text, content text, language text,
      size_bytes integer, UNIQUE(skill_id,path));`)
  const sql = {
    query: (text, values) => ({ text, values }),
    transaction: (queries) => db.transaction(async (tx) => {
      for (const query of queries) await tx.query(query.text, query.values)
    }),
  }
  return { db, sql }
}

test('publishes source and MCP files atomically; removes stale companions on an update', async () => {
  const root = fixture()
  const { db, sql } = await database()
  try {
    const bundle = readSkillBundle('skills/legal/test-skill/SKILL.md', root)
    await publishSkill(sql, bundle, 'legal', [0.1])
    assert.equal((await db.query('SELECT * FROM content.skill_source_files')).rows.length, 3)
    const rows = (await db.query("SELECT * FROM content.skills WHERE visibility='public'")).rows
    assert.equal(rows.length, 3)
    const reference = rows.find((row) => row.slug.endsWith('--file--references/rules.md'))
    assert.match(reference.content, /Current rules/)
    assert.ok(reference.tags.includes('__bundle_file'))
    const binary = rows.find((row) => row.slug.endsWith('--file--example.pdf'))
    assert.ok(binary.tags.includes('__bundle_base64'))
    assert.deepEqual(Buffer.from(binary.content, 'base64'), Buffer.from([0xff, 0xfe, 0x00, 0x01]))

    await publishSkill(sql, { ...bundle, files: bundle.files.filter((file) => file.path === 'SKILL.md') }, 'legal', [0.2])
    assert.equal((await db.query('SELECT * FROM content.skill_source_files')).rows.length, 1)
    assert.equal((await db.query("SELECT * FROM content.skills WHERE visibility='public'")).rows.length, 1)
  } finally { await db.close(); fs.rmSync(root, { recursive: true, force: true }) }
})

test('a failed companion insert rolls back the root and its source manifest', async () => {
  const root = fixture()
  const { db, sql } = await database()
  try {
    await db.exec("ALTER TABLE content.skills ADD CHECK (slug NOT LIKE '%--file--%')")
    await assert.rejects(publishSkill(sql, readSkillBundle('skills/legal/test-skill/SKILL.md', root), 'legal', [0.1]))
    assert.equal((await db.query('SELECT * FROM content.skills')).rows.length, 0)
    assert.equal((await db.query('SELECT * FROM content.skill_source_files')).rows.length, 0)
  } finally { await db.close(); fs.rmSync(root, { recursive: true, force: true }) }
})

test('reference-only edits and removals trigger the root publication', () => {
  const root = fixture()
  try {
    const base = execFileSync('git', ['rev-parse', 'HEAD'], { cwd: root, encoding: 'utf8' }).trim()
    fs.rmSync(path.join(root, 'skills/legal/test-skill/references/rules.md'))
    execFileSync('git', ['add', '.'], { cwd: root })
    execFileSync('git', ['-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'remove reference'], { cwd: root })
    assert.deepEqual(changedSkills({ vertical: 'legal', base, repoRoot: root }), { added: ['skills/legal/test-skill/SKILL.md'], deleted: [] })
    fs.rmSync(path.join(root, 'skills/legal/test-skill'), { recursive: true })
    execFileSync('git', ['add', '.'], { cwd: root })
    execFileSync('git', ['-c', 'user.name=Test', '-c', 'user.email=test@example.invalid', 'commit', '-qm', 'remove skill'], { cwd: root })
    assert.deepEqual(changedSkills({ vertical: 'legal', base, repoRoot: root }), { added: [], deleted: ['skills/legal/test-skill/SKILL.md'] })
  } finally { fs.rmSync(root, { recursive: true, force: true }) }
})

test('the Form D bundle includes all eight references and its regression tests', () => {
  const bundle = readSkillBundle('skills/legal/form-d-exempt-offering-notice/SKILL.md', path.join(__dirname, '..'))
  assert.equal(bundle.files.filter((file) => file.path.startsWith('references/')).length, 8)
  assert.ok(bundle.files.some((file) => file.path === 'SKILL.md'))
  const others = bundle.files.filter((file) => file.path !== 'SKILL.md' && !file.path.startsWith('references/'))
  assert.ok(others.length > 0, 'the evals/ suite is bundled as companion files')
  assert.ok(others.every((file) => file.path.startsWith('evals/')), `unexpected companions: ${others.map((f) => f.path).join(', ')}`)
})
