---
name: character-consistency
description: Keep faces, products, and props identical across AI-generated shots — asset registry, reference sheets, verbatim descriptions. Use when a character or product appears in more than one shot, or when faces keep drifting between generations.
---

# Character Consistency

The single most visible failure in AI video: the same person looks like three
different people across four shots. Models don't remember your character from
shot to shot. Every generation starts from zero, so continuity has to be
engineered — with words, pictures, and IDs that don't change.

## The workflow

1. **Register everything that repeats.** Every character, product, and key
   prop gets an asset ID before the first generation
   (`references/asset-registry.md`). The registry is the single source of
   truth.
2. **Write the reference sheet.** One canonical description per asset —
   physical, specific, frozen (`references/reference-sheets.md`). This text
   gets pasted verbatim into every prompt. Verbatim. Not "in your own words."
3. **Attach reference images where the model allows.** Image inputs lock
   identity far better than text. The adapters note per-model support.
4. **Cite, don't describe.** In every shot-brief, write the asset ID and paste
   the frozen description. Never paraphrase, never summarize, never
   "improve" it mid-project.
5. **Verify across shots.** Check identity at every join
   (`../video-qa/references/continuity.md`). Drift caught at the join is a
   reshoot; drift caught at delivery is a disaster.

## Rules that don't bend

- **One description, frozen.** The moment two shots describe the same face
  differently, you have two faces. Copy-paste is a feature.
- **IDs are contracts.** `mara-01` means the registry entry, not "a woman
  kind of like Mara." When the description needs to change, change the
  registry and bump the version — don't silently edit prompts.
- **Describe what's stable, not what's momentary.** The reference sheet holds
  face, build, hair, wardrobe staples — not expressions, not poses, not
  lighting. Momentary things live in the shot-brief.
- **Products are characters too.** A bottle, a car, a logo: same discipline.
  Geometry, colors, label placement — frozen and cited.
- **Fewer recurring assets, better continuity.** Every additional recurring
  character multiplies the drift surface. Design casts you can actually hold
  together.
