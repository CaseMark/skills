const assert = require('node:assert/strict')
const test = require('node:test')
const { PGlite } = require('@electric-sql/pglite')
const { parseSlugs, compareBundle, repairBundle } = require('./repair-bundles')

const bundle = { slug: 'example', name: 'Example', summary: 'Summary', content: '# Example',
  tags: ['analysis'], license: 'Apache-2.0', language: 'en',
  files: [{ path: 'SKILL.md', content: 'raw root', sizeBytes: 8, encoding: 'utf8', contentType: 'text/markdown' },
    { path: 'references/rules.md', content: '# Rules', sizeBytes: 7, encoding: 'utf8', contentType: 'text/markdown' }] }
const root = { ...bundle, version: 5, visibility: 'public', embedding: '[0.1]' }
const source = bundle.files.map(f => ({ ...f, language: 'markdown', size_bytes: f.sizeBytes }))
const companion = { slug: 'example--file--references/rules.md', content: '# Rules', visibility: 'public',
  tags: ['__bundle_file', '__content_type:text/markdown'] }

test('repair requires an explicit, bounded set of safe unique slugs', () => {
  assert.deepEqual(parseSlugs('example, second\nexample'), ['example', 'second'])
  assert.deepEqual(parseSlugs(''), [])
  for (const value of ['../example', 'legal/example', 'example; echo secret', 'Example'])
    assert.throws(() => parseSlugs(value), /Invalid/)
  assert.throws(() => parseSlugs(Array.from({ length: 21 }, (_, i) => `skill-${i}`).join(',')), /20/)
})

test('inventory compares exact source bytes and MCP companion rows, not aggregate timestamps', () => {
  assert.deepEqual(compareBundle(bundle, root, source, [companion]), [])
  assert.deepEqual(compareBundle(bundle, root, [], []), [
    'source:SKILL.md', 'source:references/rules.md', 'mcp:references/rules.md'])
  assert.deepEqual(compareBundle(bundle, root, source, [{ ...companion, content: 'stale' }]), ['mcp:references/rules.md'])
  assert.deepEqual(compareBundle(bundle, root, [...source, { path: 'obsolete.md' }], [companion]), ['removed-source:obsolete.md'])
  assert.ok(compareBundle(bundle, root, source, [companion, { ...companion, slug: 'example--file--obsolete.md' }])
    .includes('removed-mcp:obsolete.md'))
})

test('repair refuses missing, archived, or edited roots and preserves attribution fields', async () => {
  const sql = { query: (text, values) => ({ text, values }), transaction: async queries => queries }
  for (const current of [null, { ...root, visibility: 'archived' }, { ...root, content: 'newer edit' },
    { ...root, tags: ['different'] }, { ...root, license: 'Proprietary' }])
    await assert.rejects(repairBundle(sql, bundle, current, 'legal'), /root/)
  const queries = await repairBundle(sql, bundle, root, 'legal')
  assert.match(queries[0].text, /FOR UPDATE/)
  assert.ok(queries[0].values.includes(5))
  assert.ok(queries.every(q => !/SET\s+author_name|skill_aliases|skill_attribution/.test(q.text)))
})

test('real transactions recover old roots and atomically add, edit, remove, or roll back files', async () => {
  const db = new PGlite()
  const sql = { query: (text, values) => ({ text, values }), transaction: queries => db.transaction(async tx => {
    for (const query of queries) await tx.query(query.text, query.values)
  }) }
  try {
    await db.exec(`CREATE DOMAIN vector AS text; CREATE SCHEMA content;
      CREATE TABLE content.skills (id uuid PRIMARY KEY DEFAULT gen_random_uuid(),slug text,name text,summary text,
        content text,embedding vector,tags text[],license text,language text,domain text,visibility text,
        version integer,author_name text,created_at timestamptz,updated_at timestamptz,UNIQUE(slug,domain));
      CREATE TABLE content.skill_source_files (skill_id uuid REFERENCES content.skills(id),path text,content text,
        language text,size_bytes integer,UNIQUE(skill_id,path));`)
    // Older record has current instructions but no published bundle files.
    await db.query(`INSERT INTO content.skills (slug,name,summary,content,embedding,tags,license,language,domain,
      visibility,version,author_name) VALUES ($1,$2,$3,$4,$5,$6,$7,$8,'legal','public',5,'Original Author')`,
      [bundle.slug, bundle.name, bundle.summary, bundle.content, '[0.1]', bundle.tags, bundle.license, bundle.language])
    const current = async () => (await db.query("SELECT * FROM content.skills WHERE slug='example' AND domain='legal'")).rows[0]
    const check = async expected => {
      const sourceRows = (await db.query('SELECT * FROM content.skill_source_files')).rows
      const companions = (await db.query("SELECT * FROM content.skills WHERE slug LIKE 'example--file--%'")).rows
      assert.deepEqual(compareBundle(expected, await current(), sourceRows, companions), [])
      assert.equal((await current()).author_name, 'Original Author')
    }
    await repairBundle(sql, bundle, await current(), 'legal')
    await check(bundle)
    const edited = { ...bundle, files: [bundle.files[0], { ...bundle.files[1], content: '# Edited', sizeBytes: 8 },
      { ...bundle.files[1], path: 'references/added.md' }] }
    await repairBundle(sql, edited, await current(), 'legal')
    await check(edited)
    const removed = { ...bundle, files: [bundle.files[0]] }
    await repairBundle(sql, removed, await current(), 'legal')
    await check(removed)
    const before = await current()
    await assert.rejects(repairBundle(sql, bundle, { ...before, version: before.version - 1 }, 'legal'), /division by zero/)
    assert.equal((await current()).version, before.version)
    await db.exec("ALTER TABLE content.skill_source_files ADD CHECK (path NOT LIKE '%rules.md')")
    await assert.rejects(repairBundle(sql, bundle, before, 'legal'))
    await check(removed)
    assert.equal((await current()).version, before.version)
  } finally { await db.close() }
})
