# Installing the Skills

The skills follow the open Agent Skills format (`SKILL.md` with frontmatter),
which is now read natively by 24+ tools. Pick your agent below. If your
client isn't listed, copy the `skills/` folders into whatever directory your
client scans for skills — the format is the same everywhere.

## The one-liner (skills.sh)

Any public GitHub repo with `SKILL.md` files is auto-listed on skills.sh:

```bash
npx skills add svenkatreddy/universal-video-skills
```

## npm

```bash
npm install universal-video-skills
# then copy the skills you want:
cp -r node_modules/universal-video-skills/skills/video-prompt-craft ~/.claude/skills/
```

## Per-agent paths

**Claude Code:** copy each skill folder into `~/.claude/skills/` (personal)
or `<project>/.claude/skills/` (project). E.g.
`~/.claude/skills/video-prompt-craft/SKILL.md`.

**Muse:** skills live under `~/workspace/skills/<name>/`. Copy the skill
folders there.

**Gemini CLI:** `~/.muse/skills/` — same layout, skill folder per skill.

**Cursor / Windsurf / Cline / OpenCode:** these read `SKILL.md` from their
configured skills/rules directories — check your client's docs for the exact
path and drop the folders in.

**Grok:** xAI's Grok Skills import instruction blocks as `.zip`, `.skill`,
or `.md` files. Zip the `skills/` directory (or a single skill folder) and
import it through Grok's skills interface.

**Codex CLI:** supports the Agent Skills standard — place skill folders in
its skills directory per the Codex docs.

## Which skills to install

Install all eight for the full pipeline, or take what you need:

| I want to... | Install |
|---|---|
| Write better video prompts | `video-prompt-craft` |
| Direct camera, light, style | `cinematic-direction` |
| Plan multi-shot videos | `story-and-shots` |
| Keep faces/products consistent | `character-consistency` |
| Handle dialogue, subtitles, mixing | `dialogue-and-audio` |
| Stitch clips and export | `assembly-and-delivery` |
| Target a specific generator | `model-adapters` |
| Review clips before shipping | `video-qa` |

Each skill is self-contained: its `SKILL.md` routes to its own references,
and cross-skill links are relative, so installing a subset never breaks.
