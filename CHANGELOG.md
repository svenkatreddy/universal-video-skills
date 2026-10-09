# Changelog

## 0.1.0 — 2026-10-08

First release. Eight skills, written from scratch:

- `video-prompt-craft` — shot-brief grammar, JSON prompting, negative
  prompts, failure modes
- `cinematic-direction` — camera language, lighting and color, style lenses
- `story-and-shots` — beats, shot lists, storyboards, quality gates
- `character-consistency` — asset registry, reference sheets
- `dialogue-and-audio` — voiceover, subtitles, mixing
- `assembly-and-delivery` — ffmpeg concat script, transitions, platform exports
- `model-adapters` — Muse, Gemini/Veo, Sora, Kling, Runway, Pika, Luma,
  Hailuo (all dated 2026-10-08)
- `video-qa` — checklists, frame-evidence contact-sheet script, continuity

Plus worked examples, per-agent install docs, and an honest-limits page.

### Added post-review (still 0.1.0, pre-publish)

- `video-prompt-craft/references/i2v-prompting.md` — the I2V prompt
  subtraction principle: describe only motion, never redescribe the anchor
  image (after hermes-media-skill-pack, MIT)
- `video-qa/references/failure-taxonomy.md` — defect → fix table with
  layered gates, cheapest checks first (after openmontage indie-qa;
  AGPLv3, concepts only)
- `video-qa/references/automated-identity-qa.md` +
  `video-qa/scripts/identity_score.py` — CLIP-embedding frame scoring vs.
  a reference image, with mandatory per-project calibration
  (after capy-video-gen-skill, MIT)

### Honest-review fixes (still 0.1.0, pre-publish)

- `concat.py`: audio streams now gated like video (docstring claimed it;
  code didn't), single-quote escaping in the concat list, refuse
  output==input, `+genpts` for safer joins
- `identity_score.py`: warns about the ~350MB first-run CLIP download
- `contact_sheet.py`: clean errors for `--n 0` / bad `--times`
- New `scripts/smoke-test.sh`: 7 checks, all passing
