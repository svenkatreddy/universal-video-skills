# Changelog

## Unreleased

- `stitching.md`: the transcode fix-up now covers silent clips. The old
  single command could not fix a silent odd clip (ffmpeg will not invent
  an audio stream for `-c:a`), so the concat gate kept failing after
  following the doc. Added the `-an` variant for silent projects and the
  silent-track (`anullsrc`) variant for silent clips joining a project
  with audio.
- `stitching.md`: the `xfade` example mapped video only, silently dropping
  audio and tripping the concat gate downstream. Documented the `offset`
  math and added the `acrossfade` variant that preserves audio.
- `contact_sheet.py`: `--cols` and `--thumb` now validate like `--n`
  (previously `--cols 0` crashed with `ZeroDivisionError`).
- `identity_score.py`: `--frames` now validates as a positive int
  (previously `--frames 0` died in `max()` on an empty frame list).
- `smoke-test.sh`: the arg-validation checks now cover the new cases.
- `package.json`: fixed the `author` field (URL sat in the email slot);
  `scripts/` is now in the published tarball so the documented smoke
  test runs from an npm install. Invoked via `bash scripts/smoke-test.sh`
  (CONTRIBUTING.md updated) because the exec bit does not survive npm
  tarballs or GitHub API pushes.

## 0.1.0 (2026-10-08)

First release. Eight skills, written from scratch:

- `video-prompt-craft`: shot-brief grammar, JSON prompting, negative
  prompts, failure modes
- `cinematic-direction`: camera language, lighting and color, style lenses
- `story-and-shots`: beats, shot lists, storyboards, quality gates
- `character-consistency`: asset registry, reference sheets
- `dialogue-and-audio`: voiceover, subtitles, mixing
- `assembly-and-delivery`: ffmpeg concat script, transitions, platform exports
- `model-adapters`: Muse, Gemini/Veo, Sora, Kling, Runway, Pika, Luma,
  Hailuo (all dated 2026-10-08)
- `video-qa`: checklists, frame-evidence contact-sheet script, continuity

Plus worked examples, per-agent install docs, and an honest-limits page.

### Added post-review (still 0.1.0, pre-publish)

- `video-prompt-craft/references/i2v-prompting.md`: the I2V prompt
  subtraction principle: describe only motion, never redescribe the anchor
  image (after hermes-media-skill-pack, MIT)
- `video-qa/references/failure-taxonomy.md`: defect → fix table with
  layered gates, cheapest checks first (after openmontage indie-qa;
  AGPLv3, concepts only)
- `video-qa/references/automated-identity-qa.md` +
  `video-qa/scripts/identity_score.py`: CLIP-embedding frame scoring vs.
  a reference image, with mandatory per-project calibration
  (after capy-video-gen-skill, MIT)
- New skill `muse-google-veo-web`: end-to-end Veo production through
  Google Flow on the web (AI Pro subscription): project setup and credit
  budgeting, five-part Veo prompting, browser ops, full-duration QA,
  stitching. Written from a real production workflow, generalized for any
  use case.

### Honest-review fixes (still 0.1.0, pre-publish)

- `concat.py`: audio streams now gated like video (docstring claimed it;
  code didn't), single-quote escaping in the concat list, refuse
  output==input, `+genpts` for safer joins
- `identity_score.py`: warns about the ~350MB first-run CLIP download
- `contact_sheet.py`: clean errors for `--n 0` / bad `--times`
- New `scripts/smoke-test.sh`: 7 checks, all passing
