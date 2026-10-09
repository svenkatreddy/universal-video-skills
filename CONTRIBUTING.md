# Contributing

## What belongs here

- New **model adapters** (copy `skills/model-adapters/references/adapter-template.md`).
- New **references** that teach durable craft — things that will still be
  true in two years.
- **Examples** from real projects: shot-briefs, storyboards, registries that
  actually shipped.
- Fixes to stale specs (adapters are dated — if you verify a newer number,
  update the date too).

## What doesn't belong

- **Vendor lock-in.** Nothing that only works with one tool's proprietary
  feature. If it's model-specific, it goes in that model's adapter, clearly
  labeled.
- **Copied content.** Rewrite ideas in your own words. Some repos in this
  space have no license — their text is not ours to take. Concepts are
  fine; prose is not.
- **AI slop.** Write like a person. Short sentences, concrete nouns, no
  "delve," no "leverage," no "in today's fast-paced world." If it sounds
  like a model wrote it, rewrite it.
- **Non-English core content.** The pack is English-first. Translations are
  welcome as separate community contributions, not mixed into the core.

## How

1. Keep skills thin: `SKILL.md` routes, `references/` teaches, `scripts/`
   are deterministic and dependency-light.
2. Cross-link with relative paths so skills work installed individually.
3. Update the adapter's "Last verified" date when you touch specs.
4. One idea per file. If a reference tries to do two jobs, split it.

## Tests

`scripts/smoke-test.sh` exercises the helper scripts against
ffmpeg-generated synthetic clips: concat happy path, the audio-mismatch
gate, the output==input guard, contact-sheet generation, arg validation,
and identity-QA's graceful degradation without torch. Run it before
pushing any change to a script:

```bash
./scripts/smoke-test.sh
```

It needs ffmpeg on PATH. All 7 checks must pass.

## License

Contributions are under the MIT license, same as the repo.
