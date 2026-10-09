# Universal Video Skills

A skill pack for AI agents that make video. Eight skills covering the whole
job — writing prompts, directing the camera, planning multi-shot stories,
keeping faces consistent, handling dialogue and audio, stitching the final
cut, and checking the result before it ships.

The one thing it refuses to do: lock you into a single video model. Write
the prompt once, then translate it for whichever generator you're using —
Muse, Gemini/Veo, Sora, Kling, Runway, Pika, Luma, or Hailuo — with a
per-model adapter sheet. It works in any agent that reads the open
[Agent Skills](https://agentskills.io) format: Claude Code, Muse, Gemini
CLI, Grok, Cursor, Codex, and the rest.

## Why this exists

Every video skill I found was welded to one tool: one assumed Muse's
built-in generator, another assumed an unreleased Meta model, a third
assumed a Chinese API toolchain, a fourth was motion-graphics code with no
AI generation at all. The craft inside them was often excellent — prompt
grammars, continuity systems, QA gates — but you couldn't take any of it to
a different model without rewriting it yourself.

So I took the craft and left the lock-in. The prompting grammar, the
continuity discipline, the review gates, the assembly scripts — rewritten
from scratch, in plain English, with the model-specific bits isolated in
adapter sheets that are dated and honest about going stale.

## The eight skills

| Skill | What it does |
|---|---|
| `video-prompt-craft` | The core: shot-brief grammar, JSON prompting, negative prompts, failure-mode hardening |
| `cinematic-direction` | Camera language, lighting and color, style lenses — directing vocabulary |
| `story-and-shots` | Beats, shot lists, storyboards, review gates, fast-track for simple jobs |
| `character-consistency` | Asset registry, reference sheets, verbatim descriptions — no face drift |
| `dialogue-and-audio` | Voiceover writing and casting, subtitles, mixing |
| `assembly-and-delivery` | ffmpeg stitching, transitions, titles, watermarks, platform exports (16:9/9:16/1:1) |
| `model-adapters` | Per-model translation sheets: Muse, Veo, Sora, Kling, Runway, Pika, Luma, Hailuo |
| `video-qa` | Per-shot checklists, frame evidence, continuity across joins, written verdicts |

Each skill is a thin `SKILL.md` that routes into deep reference files.
Install all eight or just the ones you need — they're self-contained and
cross-link with relative paths.

## Quick start

```bash
npx skills add svenkatreddy/universal-video-skills
```

Or via npm:

```bash
npm install universal-video-skills
```

Per-agent install paths (Claude Code, Muse, Gemini CLI, Grok, Cursor…)
are in [docs/install.md](docs/install.md).

Then look at the [examples](examples/) — a finished shot-brief, its JSON
version, a storyboard, and an asset registry from a small sample project.
They're the fastest way to see how the pieces fit.

## The workflow, in one paragraph

Plan the story in beats, shot-list every beat, lock your characters and
style before generating anything, write each shot as a timed brief with a
negative block, translate the brief through the target model's adapter,
generate, review every clip against its brief with frame evidence, stitch
with the concat script, mix the audio, subtitle everything, export per
platform. The skills walk you through each step; the gates tell you when
to move on.

## Honest limits

This pack doesn't generate video — it teaches agents to direct it. It can't
make a model do what the model can't do (readable text, perfect lip sync,
and complex physics are still hard everywhere). Model specs go stale, so
every adapter is dated: verify before you plan around a number. The full
list is in [docs/honest-limits.md](docs/honest-limits.md) — read it before
you decide this is for you.

## Acknowledgments

The craft here stands on work others published first. The prompt grammar
and stitch discipline owe a debt to Mason Mosen's muse-video-prompt-skill;
the thin-router architecture, phase gates, and asset-registry ideas to
Jiang Yong Luo's muse-video-skill; the shot-brief structure and case
standards to ImagineVid's awesome list; the motion grammar and evidence
gates to Pluviobyte's video-production-skills; and the vendor-neutral,
multi-agent positioning to the wider community (visual-skills, DirectorSKILL,
the cinematic-video-prompt-skill, and others). Everything here is rewritten
in my own words — borrow the ideas, credit the people.

## Contributing

New adapters, durable craft references, and real shipped examples are
welcome. Vendors' proprietary features, copied prose, and AI-sounding filler
are not. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).
