# The Asset Registry

A small file (JSON or a table) that lists every recurring asset in the
project and points at its canonical description and reference images. Every
prompt cites the registry; nothing re-describes from memory.

## Format

```json
{
  "project": "night-market",
  "assets": [
    {
      "id": "mara-01",
      "type": "character",
      "description_ref": "reference-sheets.md#mara-01",
      "reference_images": ["assets/mara-front.png", "assets/mara-profile.png"],
      "notes": "copper bob must read at night; bomber jacket olive, not brown"
    },
    {
      "id": "umbrella-red-01",
      "type": "prop",
      "description_ref": "reference-sheets.md#umbrella-red-01",
      "reference_images": ["assets/umbrella.png"],
      "notes": "story-critical color pop; exact red matters"
    }
  ]
}
```

Keep it in the project folder, next to the shot list. It takes five minutes
to start and saves hours of "wait, which jacket did we use in shot 2."

## What gets registered

- **Characters** who appear in more than one shot.
- **Products:** the thing being sold gets an ID even in a single-shot ad,
  because the client will ask for a second cut.
- **Story-critical props:** the red umbrella, the letter, the key. If the
  plot notices it, register it.
- **Locations** (for multi-scene work): the market, the alley. Same stall
  layout, same neon signs.

## Registry discipline

- **Cite by ID in every brief.** `Subject: mara-01: [paste frozen
  description]`. The ID tells humans which asset; the pasted text tells the
  model what it looks like.
- **Version on change.** If Mara's jacket changes mid-story, that's
  `mara-02`, not a quiet edit. Old shots keep citing `mara-01`.
- **Images beat words.** A front and profile reference image does more for
  identity than a paragraph. Generate or shoot the references before the
  project starts, and reuse the same files everywhere the model accepts image
  input.
- **Review the registry at Gate 3.** (See `../../story-and-shots/`.) No
  generation starts until every recurring asset has an ID, a frozen
  description, and (where possible) a reference image.
