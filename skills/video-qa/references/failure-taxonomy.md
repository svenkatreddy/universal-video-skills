# Failure Taxonomy and the Repair Loop

Not all defects are equal, and not all fixes are "try again." This taxonomy
maps each defect type to its most likely cause and its highest-percentage
fix. When a clip fails QA, find the row, apply the fix, regenerate once.
That's the repair loop: **defect → mapped fix → regenerate → re-verify.**

## The taxonomy

| Defect | What you see | Likely cause | Fix |
|---|---|---|---|
| `identity_drift` | Face/body changes across shots | Paraphrased descriptions; no reference image | Freeze verbatim description; add reference image; cite asset ID |
| `part_loss` | A distinctive part (ear, horn, antenna, logo detail) vanishes or reshapes mid-shot | Model dropped a complex appendage in motion | Regenerate with the part named in Preserve ("the dragon's left horn, fully visible, same curve throughout"); shorten the clip |
| `lineup_invention` | Extra people/objects appear | Unpinned counts | Identity-lock: exact counts in Subject + Preserve; reseed |
| `count_drift` | Three stalls become two, then four | Counts stated once, weakly | State exact counts in brief *and* Preserve; check boundary frames |
| `wardrobe_change` | Clothes/hair differ between shots | No asset lock | Register the asset; cite ID; never paraphrase |
| `face_morph` | Features slide during the clip | Long clip + complex motion | Shorten beats (≤5s); locked camera; `morphing face` in negatives |
| `text_gibberish` | Scrambled signage | Models can't render text | Remove text from frame or composite in post. Don't re-prompt |
| `physics_break` | Objects intersect; liquid wrong | Overcomplex interaction | Simplify to one object, one action |
| `screen_flip` | Direction reverses across a cut | Unmarked screen direction | Mark L→R/R→L in the shot list; regenerate or bridge with a cutaway |
| `light_break` | Noon cuts to midnight | Unplanned time change | Note time of day per shot; regenerate the weaker side |
| `audio_mismatch` | Line lands on the wrong beat | Untimed dialogue | Put dialogue in timed beats; verify sync support; plan post voiceover |
| `tail_decay` | Last 2 seconds fall apart | Temporal degradation | Trim the tail; regenerate shorter; use the good portion |

Two rules about the table:

1. **Some rows say "don't re-prompt."** Text gibberish and physics breaks
   are model limits, not prompt problems. Re-rolling wastes generations.
   Route around instead.
2. **Grow it.** Every new failure your project hits gets a row: defect,
   cause, the fix that worked. After a production, this table is the most
   valuable page you own.

## Layered gates (cheap checks first)

Don't spend expensive review on clips that fail cheap tests. Order the QA
so the cheap gates kill bad clips early:

1. **Probe** (seconds): ffprobe. Right codec, resolution, duration? A
   2-second clip that should be 8 is dead on arrival.
2. **Contact sheet** (a minute): first vs. last frame. Identity and
   counts hold? Most drift dies here.
3. **Boundary frames** (minutes): ±1s around joins. Continuity holds?
4. **Full watch** (the expensive one): only clips that survived 1–3 get
   watched end to end, with sound.

A clip that fails gate 1 never reaches gate 4. That's the whole idea.

## The repair loop, written out

1. QA finds a defect → name it from the taxonomy.
2. Apply the row's fix: exactly one change (one variable per
   regeneration, always).
3. Regenerate, re-run the gates from the top.
4. If it fails twice with mapped fixes, stop: the shot needs replanning
   (simplify, shorten, switch to I2V, or cut), not a third prompt tweak.

Log every loop: clip ID, defect, fix applied, result. The log *is* the
taxonomy growing.
