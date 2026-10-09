# Frame Evidence

Watching a clip tells you if it feels right. Stills tell you if it *is*
right. Pull frames at the moments that matter and look at them frozen —
drift, morphing, and count errors hide in motion and show in stills.

## The contact sheet

`scripts/contact_sheet.py` extracts frames across a clip into a grid:

```bash
python3 scripts/contact_sheet.py clip3.mp4 -o clip3-sheet.jpg
```

Defaults: 12 frames evenly spaced, labeled with timestamps. Options: `--n`
for count, `--times 0.5,3.0,7.5` for exact moments.

What to look at:

- **First vs. last frame.** Same face? Same wardrobe? Same stall count?
  The first-last comparison catches more drift than anything else.
- **Boundary frames.** ±1 second around every join, from both clips. The
  join is where continuity lives or dies.
- **Beat frames.** One frame per timed beat — did each beat's action
  actually happen?

## Claim discipline

Say what the evidence shows, not what you hope:

- "Frames show the same jacket in shots 2–4" — a claim.
- "Looks consistent" — not a claim.
- "Unverified" — the honest label for anything you didn't check.

Different checks are different claims. A contact sheet proves visual
continuity; it doesn't prove the audio syncs. Don't let one piece of
evidence certify the whole clip.

## When frames aren't enough

- **Motion problems** (sliding feet, warping) need the moving clip, slowed
  down. Stills won't show them.
- **Audio** needs ears, not eyes.
- **Pacing** needs the full cut watched straight through, no pausing.

Frames are one instrument. Use all of them.
