# Negative Prompts: Say What Must Not Happen

The positive prompt describes the shot. The negative prompt describes the
ways models typically ruin it. Writing restrictions feels pessimistic; it is
also the cheapest quality improvement in AI video. A line of "avoid" costs
nothing and prevents the reshoot.

## How to write them

Be specific about the failure, not the vibe. "Bad quality" is useless: the
model doesn't know what you mean. "Extra fingers, morphing face, warping
background" names three concrete things to suppress.

Group them by category so you stop forgetting whole classes:

**Anatomy.** `extra fingers, extra limbs, missing limbs, distorted hands,
morphing face, asymmetrical eyes, melting features`

**Physics and motion.** `warping background, sliding feet, flickering objects,
impossible motion, jitter, strobing`

**Text and logos.** `gibberish text, distorted logos, watermark, subtitles
burned in`. Models still cannot render text reliably; if you need a readable
sign, plan to composite it in post.

**Camera.** `camera shake, sudden zoom, dutch angle drift`: only if you asked
for them.
for them.

**Look.** `oversaturated, plastic skin, airbrushed, video-game render`: use
only if you're chasing realism; drop these when stylization is the point.

**Continuity.** `changing clothes, changing hairstyle, face swap`: for
multi-shot work, restate per shot.

## Model differences

Not every model takes a separate negative prompt field. The adapters note
per-model support. When there's no negative field, fold the restrictions into
the main prompt as an `Avoid:` line. It still helps, just less.

## Two habits

1. **Keep a project-wide block.** Most of your negatives repeat shot to shot.
   Write them once, paste everywhere, and only add shot-specific ones.
2. **Grow the list from failures.** Every time a generation goes wrong in a new
   way, add that failure to the block. After a dozen shots you own a custom
   anti-failure list tuned to your subject matter. That's a real asset.
