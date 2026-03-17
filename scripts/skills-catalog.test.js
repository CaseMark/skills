const assert = require('node:assert/strict')
const fs = require('fs')
const os = require('os')
const path = require('path')
const test = require('node:test')

const {
  buildSkillsCatalog,
  buildMetaKey,
  parseSkillDocument,
  publishSkillsCatalog,
  splitCatalogIntoShards,
} = require('./skills-catalog')

test('parseSkillDocument reads frontmatter fields needed for the catalog', () => {
  const { frontmatter, body } = parseSkillDocument(
    `---
name: deposition-summarization
description: Summarizes deposition transcripts with citations.
tags:
  - litigation
  - summary
metadata:
  author: casemark
---

# Deposition Summarization

Do the work.
`,
    'skills/legal/deposition-summarization/SKILL.md'
  )

  assert.equal(frontmatter.name, 'deposition-summarization')
  assert.equal(frontmatter.description, 'Summarizes deposition transcripts with citations.')
  assert.deepEqual(frontmatter.tags, ['litigation', 'summary'])
  assert.match(body, /Do the work\./)
})

test('buildSkillsCatalog builds a shared catalog across categories', () => {
  const repoRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'skills-catalog-'))
  const legalDir = path.join(repoRoot, 'skills', 'legal', 'deposition-summarization')
  const casedevDir = path.join(repoRoot, 'skills', 'casedev', 'search')

  fs.mkdirSync(legalDir, { recursive: true })
  fs.mkdirSync(casedevDir, { recursive: true })

  fs.writeFileSync(
    path.join(legalDir, 'SKILL.md'),
    `---
name: deposition-summarization
description: Summarizes deposition transcripts with precise citations.
tags:
  - litigation
  - summary
---

# Deposition Summarization

Use when drafting a transcript summary.
`,
    'utf8'
  )

  fs.writeFileSync(
    path.join(casedevDir, 'SKILL.md'),
    `---
name: search
description: Searches case.dev sources and the web.
---

# case.dev Search

Use for platform search tasks.
`,
    'utf8'
  )

  const catalog = buildSkillsCatalog({ repoRoot })

  assert.equal(catalog.version, 1)
  assert.equal(catalog.skillCount, 2)
  assert.equal(catalog.countsByCategory.legal, 1)
  assert.equal(catalog.countsByCategory.casedev, 1)
  assert.deepEqual(
    catalog.skills.map((skill) => skill.id),
    ['casedev/search', 'legal/deposition-summarization']
  )
  assert.deepEqual(catalog.skills[1].tags, ['litigation', 'summary'])
  assert.equal(catalog.skills[0].path, 'casedev/search/SKILL.md')
})

test('publishSkillsCatalog uses the valid default key when none is provided', async () => {
  const previousFetch = global.fetch

  try {
    global.fetch = async () => ({
      ok: true,
      json: async () => ({}),
      text: async () => '',
    })

    const result = await publishSkillsCatalog(
      { skills: [] },
      {
        edgeConfigId: 'ecfg_test',
        vercelToken: 'token',
      }
    )

    assert.equal(result.catalogKey, 'agent-skills-catalog-v1')
    assert.equal(result.metaKey, 'agent-skills-catalog-v1-meta')
  } finally {
    global.fetch = previousFetch
  }
})

test('publishSkillsCatalog rejects invalid catalog keys before calling Vercel', async () => {
  await assert.rejects(
    () =>
      publishSkillsCatalog(
        { skills: [] },
        {
          edgeConfigId: 'ecfg_test',
          vercelToken: 'token',
          catalogKey: 'agent-skills:catalog:v1',
        }
      ),
    /Invalid SKILLS_CATALOG_EDGE_CONFIG_KEY/
  )
})

test('splitCatalogIntoShards splits oversized categories into multiple shards', () => {
  const catalog = {
    version: 1,
    generatedAt: '2026-01-01T00:00:00.000Z',
    generatedFromSha: 'abc123',
    skillCount: 3,
    countsByCategory: { legal: 3 },
    baseKey: 'agent-skills-catalog-v1',
    skills: [
      {
        id: 'legal/a',
        slug: 'a',
        name: 'A',
        description: 'x'.repeat(120),
        tags: ['litigation'],
        category: 'legal',
      },
      {
        id: 'legal/b',
        slug: 'b',
        name: 'B',
        description: 'y'.repeat(120),
        tags: ['litigation'],
        category: 'legal',
      },
      {
        id: 'legal/c',
        slug: 'c',
        name: 'C',
        description: 'z'.repeat(120),
        tags: ['litigation'],
        category: 'legal',
      },
    ],
  }

  const result = splitCatalogIntoShards(catalog, { maxShardBytes: 350 })

  assert.equal(result.metaKey, buildMetaKey('agent-skills-catalog-v1'))
  assert.deepEqual(result.meta.shardsByCategory.legal, [
    'agent-skills-catalog-v1-legal-0',
    'agent-skills-catalog-v1-legal-1',
    'agent-skills-catalog-v1-legal-2',
  ])
  assert.equal(result.items.length, 3)
})
