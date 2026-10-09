# JSON Prompting

Prose prompts are easy to write and easy to silently break. Change one word in
a paragraph and nothing tells you what moved. JSON prompts fix that: every
decision has a named field, every revision is a diff, and pipelines can
generate or validate them mechanically.

This became the dominant serious-practitioner format in early 2026 for exactly
those reasons. Several models (notably Veo-class) also parse structured input
unusually well.

## The schema

```json
{
  "duration_sec": 8,
  "aspect_ratio": "16:9",
  "subject": {
    "description": "MARA, 34, sharp jaw, copper bob, olive bomber jacket",
    "reference_id": "mara-01"
  },
  "setting": "night market in the rain, neon signs, canvas awnings",
  "camera": {
    "framing": "medium tracking shot, waist height",
    "movement": "dolly keeping pace on subject's left, no shake"
  },
  "beats": [
    { "t": "0-3s", "action": "she weaves between stalls, neon signs sliding past" },
    { "t": "3-6s", "action": "she slows at a dumpling cart, steam washing over her face" },
    { "t": "6-8s", "action": "she looks up into the lens and smiles, barely" }
  ],
  "audio": {
    "dialogue": [{ "speaker": "vendor", "line": "...", "language": "Cantonese" }],
    "foley": ["sizzle", "rain on canvas"],
    "ambience": "night market chatter, distant traffic"
  },
  "preserve": ["Mara's face and jacket identical throughout", "three stalls on her right"],
  "avoid": ["morphing faces", "extra limbs", "readable text on signs", "slow motion"]
}
```

## When JSON earns its keep

- **Multi-shot projects.** Generate the JSON per shot from one script and the
  structure stays consistent where prose would drift.
- **Revision tracking.** `diff shot03-v2.json shot03-v3.json` shows exactly what
  you changed. Try that with two paragraphs.
- **Pipelines.** Scripts can assemble, validate (required fields present?
  beats sum to duration?), and translate these into per-model call formats.
- **Team handoff.** A JSON brief is unambiguous in a way prose never is.

## When prose is fine

Single exploratory shots. If you're just feeling out a look, write the
shot-brief in prose and move on. Convert to JSON once the shot is worth
keeping.

## Practical notes

- Keep field names stable across your project. The schema above is a starting
  point — adapt it, then freeze it.
- `reference_id` points at your asset registry
  (`../../character-consistency/references/asset-registry.md`). The ID is the
  contract; the description is the fallback.
- Validate beats against duration: the timed chunks should add up. A 30-second
  script check catches more errors than a careful re-read.
- Some models accept JSON natively; others want it flattened to prose. The
  model adapters (`../../model-adapters/`) note which is which. Either way,
  author in JSON and render to prose when needed — never the reverse.
