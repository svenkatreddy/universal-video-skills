# The Shot-Brief Grammar

One shot, one brief. Eight slots. Write them in this order; it matches how a
director actually thinks through a shot.

```
[DURATION + ASPECT]. [SUBJECT] performs [VISIBLE ACTION] in [SETTING].
Camera: [FRAMING + MOVEMENT].
Beats: [TIMED ACTION BREAKDOWN].
Audio: [DIALOGUE + FOLEY + AMBIENCE].
Preserve: [IDENTITY / GEOMETRY / LAYOUT TO HOLD].
Avoid: [FAILURE MODES].
```

## What goes in each slot

**Duration + aspect.** `8s, 16:9.` Models have hard caps (see the adapters).
State both so nobody assumes. If your story needs 30 seconds, that's four
briefs, not one.

**Subject.** Who or what the shot is about, described once, physically. Age,
build, clothing, distinguishing marks. This exact text gets reused verbatim in
every shot the subject appears in.

**Visible action.** Only what the camera can see. "He looks nervous" is not
visible. "He taps his thumb against the mug, twice, without drinking" is.
Inner states have to be translated into bodies and objects.

**Setting.** Place, time of day, weather, key props. Enough that a location
scout could find it. "A laundromat at 2 a.m., fluorescents buzzing, one dryer
still tumbling" beats "a laundromat."

**Camera.** Framing plus movement, in that order. "Medium close-up, slow push
in." If the camera doesn't move, say "locked off" — static is a choice, and
models drift when you don't choose. (Full vocabulary:
`../../cinematic-direction/references/camera-language.md`.)

**Beats.** The duration split into timed chunks: `0–3s: she enters frame left;
3–6s: she stops at the counter; 6–8s: she looks up, directly into lens.`
Keep chunks under ~5 seconds. Anything longer in one chunk will smear.

**Audio.** Dialogue as quoted lines with the speaker named, then foley, then
ambience. `MARA (quiet): "You came." Foley: bell dings. Ambience: rain on
glass, distant traffic.` If the model doesn't do audio, this slot still helps:
it forces you to decide what the scene *sounds* like, which sharpens what it
looks like.

**Preserve.** What must not change within or across shots: face identity,
product geometry, the count of people, screen direction. This is where you
fight drift before it happens.

**Avoid.** The failure modes you're pre-empting: `no morphing faces, no extra
fingers, no text on signs, no camera shake.` See `negative-prompts.md` and
`failure-modes.md`.

## A worked example

> 8s, 16:9. MARA (34, sharp jaw, copper bob, olive bomber jacket) crosses a
> night market in the rain. Camera: tracking shot at waist height, keeping
> pace on her left. Beats: 0–3s: she weaves between stalls, neon signs sliding
> past; 3–6s: she slows at a dumpling cart, steam washing over her face; 6–8s:
> she looks up into the lens and smiles, barely. Audio: sizzle and chatter,
> rain on canvas awnings, a vendor shouting in Cantonese. Preserve: Mara's
> face and jacket identical throughout; three stalls on her right, no more.
> Avoid: morphing faces, extra limbs, readable text on signs, slow motion.

Notice what's missing: "cinematic," "beautiful," "8k," "masterpiece." Those
words do nothing. The brief above is longer than a one-liner and shorter than
a paragraph of adjectives — and it gives the model decisions instead of
homework.

## Iteration discipline

Change one slot per regeneration. Keep every version. When something finally
works, the version history *is* the documentation — it shows which slot fixed
which problem.
