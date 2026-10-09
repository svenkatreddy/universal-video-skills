#!/bin/bash
# Smoke test for the video-qa and assembly helper scripts.
# Generates synthetic clips with ffmpeg, then exercises concat.py,
# contact_sheet.py, and the graceful-degradation path of identity_score.py.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CONCAT="$ROOT/skills/assembly-and-delivery/scripts/concat.py"
SHEET="$ROOT/skills/video-qa/scripts/contact_sheet.py"
SCORE="$ROOT/skills/video-qa/scripts/identity_score.py"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

pass() { echo "PASS: $1"; }
fail() { echo "FAIL: $1"; exit 1; }

echo "== 1. generate test clips =="
ffmpeg -y -v error -f lavfi -i "testsrc=duration=2:size=640x480:rate=30" \
  -pix_fmt yuv420p "$TMP/a.mp4"
ffmpeg -y -v error -f lavfi -i "testsrc=duration=2:size=640x480:rate=30" \
  -pix_fmt yuv420p "$TMP/b.mp4"
ffmpeg -y -v error -f lavfi -i "testsrc=duration=1:size=640x480:rate=30" \
  -f lavfi -i "sine=frequency=440:duration=1" -pix_fmt yuv420p \
  -shortest "$TMP/with-audio.mp4"

echo "== 2. concat.py happy path =="
python3 "$CONCAT" "$TMP/a.mp4" "$TMP/b.mp4" -o "$TMP/master.mp4" \
  | grep -q "^Done:" || fail "concat happy path"
pass "concat happy path"

echo "== 3. concat.py audio-mismatch gate =="
# NB: concat exits non-zero on mismatch by design; capture output first
# so `set -o pipefail` doesn't trip the check.
out=$(python3 "$CONCAT" "$TMP/a.mp4" "$TMP/with-audio.mp4" \
  -o "$TMP/nope.mp4" 2>&1 || true)
if echo "$out" | grep -q "MISMATCH"; then
  pass "audio-mismatch gate"
else
  fail "audio-mismatch gate (silent+audio clips must not concat)"
fi

echo "== 4. concat.py refuses output==input =="
out=$(python3 "$CONCAT" "$TMP/a.mp4" -o "$TMP/a.mp4" 2>&1 || true)
if echo "$out" | grep -q "refusing"; then
  pass "output==input guard"
else
  fail "output==input guard"
fi

echo "== 5. contact_sheet.py =="
python3 "$SHEET" "$TMP/master.mp4" -o "$TMP/sheet.jpg" --n 4 \
  | grep -q "^Wrote" || fail "contact sheet"
test -s "$TMP/sheet.jpg" || fail "contact sheet file empty"
pass "contact_sheet"

echo "== 6. contact_sheet.py rejects bad args =="
out=$(python3 "$SHEET" "$TMP/master.mp4" -o "$TMP/x.jpg" --n 0 2>&1 || true)
echo "$out" | grep -q "must be >= 1" || fail "--n 0 validation"
out=$(python3 "$SHEET" "$TMP/master.mp4" -o "$TMP/x.jpg" \
  --times "abc" 2>&1 || true)
echo "$out" | grep -q "comma-separated numbers" \
  || fail "--times validation"
pass "arg validation"

echo "== 7. identity_score.py graceful without torch =="
if python3 -c "import torch" 2>/dev/null; then
  echo "SKIP: torch present (graceful path not testable here)"
else
  out=$(python3 "$SCORE" --ref x --clips y --threshold 0.3 2>&1 || true)
  echo "$out" | grep -q "pip install" || fail "graceful dep message"
  pass "graceful dep message"
fi

echo ""
echo "ALL SMOKE TESTS PASSED"
