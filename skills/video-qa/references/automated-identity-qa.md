# Automated Identity QA with Embeddings

Manual frame review doesn't scale past a handful of clips. The automated
pattern, validated by capy-video-gen-skill across 300 experiments: extract
frames per clip, embed each one, measure cosine distance against a reference
embedding, and let the numbers do the triage. Humans review the failures
plus a random sample of the passes.

## The pattern

1. **Extract** N frames evenly across each clip (ffmpeg).
2. **Embed** each frame. Faces → face-recognition embeddings (DeepFace /
   VGG-Face, ArcFace); everything else — cartoon characters, products,
   creatures → general vision embeddings (CLIP).
3. **Score** cosine distance of each frame vs. the reference (character
   sheet / product photo) embedding. The clip's score is its *worst* frame:
   one drifted frame fails the clip.
4. **Threshold** pass/fail per clip; log every distance to JSONL.
5. **Human-review** all FAILs + a random sample of passes.

`scripts/identity_score.py` implements this. Calibrate first, score second:

```bash
pip install torch open_clip_torch Pillow
python3 scripts/identity_score.py --ref assets/mara-front.png \
  --calibrate-good good1.jpg good2.jpg --calibrate-bad bad1.jpg bad2.jpg
python3 scripts/identity_score.py --ref assets/mara-front.png \
  --clips shot-*.mp4 --frames 12 --threshold 0.32 --out qa.jsonl
```

## Choosing the embedding

- **Human faces:** face-specific models (VGG-Face, ArcFace via DeepFace or
  similar). Capy's validated numbers: 70% face-distance reduction, pass at
  cosine distance < 0.40 — but that's *their* model and data. Recalibrate
  for yours.
- **Non-faces:** CLIP (ViT-B-32 is a fine default). No universal threshold
  exists — the calibration step is mandatory, not optional.

## Honest limits

- Embeddings measure overall visual similarity, not story correctness. A
  clip can pass the numbers and still have the wrong action.
- Subtle part-level defects (a slightly reshaped ear, a shifted logo)
  sometimes slip under the threshold. The manual gates
  (`qa-checklist.md`, `failure-taxonomy.md`) still own fine detail.
- Needs Python + torch: heavy for a quick job. For fewer than ~5 clips,
  manual contact sheets are faster than setting up the stack.
- Worst-frame scoring is deliberately strict. If your project has
  legitimately varied framings (extreme close-up vs. wide), calibrate with
  examples of each or the close-ups will false-fail.
