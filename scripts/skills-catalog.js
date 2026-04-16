#!/usr/bin/env node

const fs = require('fs')
const path = require('path')

const CATALOG_VERSION = 1

function normalizeSlashPath(filePath) {
  return filePath.split(path.sep).join('/')
}

function unquote(value) {
  const trimmed = value.trim()
  if (!trimmed) return ''
  if (
    (trimmed.startsWith('"') && trimmed.endsWith('"')) ||
    (trimmed.startsWith("'") && trimmed.endsWith("'"))
  ) {
    return trimmed.slice(1, -1)
  }
  return trimmed
}

function parseInlineArray(value) {
  const trimmed = value.trim()
  if (!trimmed.startsWith('[') || !trimmed.endsWith(']')) return []
  return trimmed
    .slice(1, -1)
    .split(',')
    .map((item) => unquote(item))
    .filter(Boolean)
}

function parseFrontmatterBlock(block) {
  const lines = block.split(/\r?\n/)
  const frontmatter = {}

  for (let index = 0; index < lines.length; ) {
    const line = lines[index]
    if (!line.trim()) {
      index += 1
      continue
    }

    const keyMatch = line.match(/^([A-Za-z0-9_-]+):(?:\s*(.*))?$/)
    if (!keyMatch) {
      index += 1
      continue
    }

    const key = keyMatch[1]
    const rawValue = keyMatch[2] ?? ''

    if (rawValue) {
      frontmatter[key] = key === 'tags' ? parseInlineArray(rawValue) : unquote(rawValue)
      index += 1
      continue
    }

    if (key === 'tags') {
      const tags = []
      let cursor = index + 1
      while (cursor < lines.length) {
        const candidate = lines[cursor]
        const tagMatch = candidate.match(/^\s*-\s+(.+)$/)
        if (tagMatch) {
          tags.push(unquote(tagMatch[1]))
          cursor += 1
          continue
        }
        if (!candidate.trim()) {
          cursor += 1
          continue
        }
        if (/^\s+/.test(candidate)) {
          cursor += 1
          continue
        }
        break
      }
      frontmatter.tags = tags
      index = cursor
      continue
    }

    let cursor = index + 1
    while (cursor < lines.length) {
      const candidate = lines[cursor]
      if (!candidate.trim()) {
        cursor += 1
        continue
      }
      if (/^\s+/.test(candidate)) {
        cursor += 1
        continue
      }
      break
    }
    frontmatter[key] = ''
    index = cursor
  }

  return frontmatter
}

function parseSkillDocument(content, filePath) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)([\s\S]*)$/)
  if (!match) {
    throw new Error(`Invalid frontmatter in ${filePath}`)
  }

  return {
    frontmatter: parseFrontmatterBlock(match[1]),
    body: match[2].trim(),
  }
}

function getDisplayName(body, fallbackName) {
  const headingMatch = body.match(/^#\s+(.+)$/m) || body.match(/^\*\*([^*]+)\*\*/m)
  return (headingMatch?.[1] || fallbackName || '').trim()
}

function collectSkillFiles(rootDir) {
  const skillFiles = []

  function visit(currentDir) {
    const entries = fs.readdirSync(currentDir, { withFileTypes: true })
    for (const entry of entries) {
      const entryPath = path.join(currentDir, entry.name)
      if (entry.isDirectory()) {
        visit(entryPath)
        continue
      }
      if (entry.isFile() && entry.name === 'SKILL.md') {
        skillFiles.push(entryPath)
      }
    }
  }

  visit(rootDir)
  return skillFiles.sort((a, b) => a.localeCompare(b))
}

function parseSkillFile(filePath, repoRoot) {
  const content = fs.readFileSync(filePath, 'utf8')
  const { frontmatter, body } = parseSkillDocument(content, filePath)

  const skillsRoot = path.join(repoRoot, 'skills')
  const relativePath = normalizeSlashPath(path.relative(skillsRoot, filePath))
  const [category] = relativePath.split('/')
  const slug = String(frontmatter.name || path.basename(path.dirname(filePath))).trim()
  const description = String(frontmatter.description || '').trim()
  const name = getDisplayName(body, slug)
  const tags = Array.isArray(frontmatter.tags)
    ? frontmatter.tags.map((tag) => String(tag).trim()).filter(Boolean)
    : []

  if (!category) {
    throw new Error(`Could not infer category from ${filePath}`)
  }
  if (!slug) {
    throw new Error(`Missing skill name in ${filePath}`)
  }
  if (!description) {
    throw new Error(`Missing skill description in ${filePath}`)
  }

  return {
    id: `${category}/${slug}`,
    slug,
    name,
    description,
    tags,
    category,
    path: relativePath,
  }
}

function buildSkillsCatalog(options = {}) {
  const repoRoot = path.resolve(options.repoRoot || path.join(__dirname, '..'))
  const skillsRoot = path.join(repoRoot, 'skills')
  const files = collectSkillFiles(skillsRoot)
  const skills = files.map((filePath) => parseSkillFile(filePath, repoRoot))

  skills.sort(
    (left, right) =>
      left.category.localeCompare(right.category) ||
      left.name.localeCompare(right.name) ||
      left.slug.localeCompare(right.slug)
  )

  const countsByCategory = {}
  for (const skill of skills) {
    countsByCategory[skill.category] = (countsByCategory[skill.category] || 0) + 1
  }

  return {
    version: CATALOG_VERSION,
    generatedAt: new Date().toISOString(),
    generatedFromSha: process.env.GITHUB_SHA || null,
    skillCount: skills.length,
    countsByCategory,
    skills,
  }
}

function parseArgs(argv) {
  const args = {
    repoRoot: path.join(__dirname, '..'),
    out: '',
  }

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index]
    if (arg === '--repo-root') {
      args.repoRoot = argv[index + 1]
      index += 1
      continue
    }
    if (arg === '--out') {
      args.out = argv[index + 1]
      index += 1
      continue
    }
  }

  return args
}

function main() {
  const args = parseArgs(process.argv.slice(2))
  const catalog = buildSkillsCatalog({ repoRoot: args.repoRoot })

  if (args.out) {
    const outputPath = path.resolve(args.out)
    fs.mkdirSync(path.dirname(outputPath), { recursive: true })
    fs.writeFileSync(outputPath, `${JSON.stringify(catalog, null, 2)}\n`, 'utf8')
    console.log(`Wrote skill catalog to ${outputPath}`)
    return
  }

  process.stdout.write(`${JSON.stringify(catalog, null, 2)}\n`)
}

module.exports = {
  buildSkillsCatalog,
  parseFrontmatterBlock,
  parseSkillDocument,
  parseSkillFile,
}

if (require.main === module) {
  try {
    main()
  } catch (error) {
    console.error(error)
    process.exit(1)
  }
}
