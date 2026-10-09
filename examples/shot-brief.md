# Example: Shot Brief

A complete shot-brief for one 8-second clip, using the grammar from
`video-prompt-craft`. This is what a finished brief looks like before it
goes to a model adapter.

---

8s, 16:9. MARA (34, sharp jaw, copper bob, olive bomber jacket — asset
`mara-01`) crosses a night market in the rain.

Camera: tracking shot at waist height, keeping pace on her left, 35mm,
shallow depth of field. Locked horizon, no shake.

Beats:
- 0–3s: she weaves between stalls, neon signs sliding past behind her
- 3–6s: she slows at a dumpling cart, steam washing over her face
- 6–8s: she looks up into the lens and smiles, barely

Audio: sizzle and chatter, rain on canvas awnings, a vendor shouting in
Cantonese. No dialogue.

Style: 1970s paranoia thriller — 35mm, natural light, muted warm grade,
subtle grain, blue-hour neon.

Preserve: Mara's face, copper bob, and olive bomber jacket identical
throughout; three stalls on her right, no more; rain visible in the neon.

Avoid: morphing faces, extra limbs, readable text on signs, slow motion,
camera shake, oversaturated colors.

---

Notes on this brief:

- Every slot of the grammar is filled. Nothing is left for the model to
  invent except the details inside the decisions.
- The asset ID (`mara-01`) points at the registry (`asset-registry.json`);
  the description is pasted verbatim, not paraphrased.
- "Locked horizon, no shake" — stillness stated as a choice.
- The style line is concrete tokens (35mm, natural light, muted warm
  grade), not adjectives.
- Beats are timed and each is one clear action.
