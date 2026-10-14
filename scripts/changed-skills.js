const fs = require('node:fs')
const path = require('node:path')
const { execFileSync } = require('node:child_process')

function changedSkills({ vertical, base, head = 'HEAD', fullSync = false, repoRoot = process.cwd() }) {
  if (!['legal', 'med', 'capital', 'finance'].includes(vertical)) throw new Error('Unsupported vertical')
  const prefix = `skills/${vertical}/`
  const args = fullSync ? ['ls-files', '-z', '--', prefix] : ['diff', '--name-only', '-z', base, head, '--', prefix]
  const files = execFileSync('git', args, { cwd: repoRoot, encoding: 'utf8' }).split('\0').filter(Boolean)
  const roots = [...new Set(files.map((file) => file.split('/').slice(0, 3).join('/')))].sort()
  const added = [], deleted = []
  for (const root of roots) {
    if (!/^[a-z0-9-]+$/.test(path.basename(root))) throw new Error(`Invalid skill directory: ${root}`)
    const skillPath = `${root}/SKILL.md`
    if (fs.existsSync(path.join(repoRoot, skillPath))) added.push(skillPath)
    else if (!fullSync) deleted.push(skillPath)
  }
  return { added, deleted }
}

if (require.main === module) {
  const before = process.env.BEFORE_SHA
  const result = changedSkills({ vertical: process.env.SKILL_VERTICAL,
    base: before && !/^0+$/.test(before) ? before : 'HEAD~1',
    head: process.env.HEAD_SHA || 'HEAD', fullSync: process.env.FULL_SYNC === 'true' })
  const output = `added<<EOF\n${result.added.join('\n')}\nEOF\ndeleted<<EOF\n${result.deleted.join('\n')}\nEOF\nhas_changes=${result.added.length + result.deleted.length > 0}\n`
  fs.appendFileSync(process.env.GITHUB_OUTPUT, output)
}
module.exports = { changedSkills }
