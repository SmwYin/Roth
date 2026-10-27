#!/bin/bash
# Validate one completed declaration report, regenerate aggregates, commit, and push.
# Usage: commit_decl.sh <Decl.Name> "<verdict>"
set -euo pipefail
cd "$(dirname "$0")/../../.."
decl="$1"; verdict="$2"
python3 -I .mathlib-quality/overview/scripts/assemble.py check "$decl"
# production sources must be untouched
if [ -n "$(git -c core.quotePath=false status --porcelain -- Roth Roth.lean lakefile.toml lake-manifest.json lean-toolchain)" ]; then
  echo "production files modified — refusing to commit" >&2; exit 1
fi
stray=$(git -c core.quotePath=false status --porcelain --untracked-files=all | grep -vE '^.. (\.mathlib-quality/overview/|PROJECT_OVERVIEW\.md$)' || true)
if [ -n "$stray" ]; then echo "unexpected changes outside overview:"; echo "$stray"; exit 1; fi
python3 -I .mathlib-quality/overview/scripts/assemble.py build
grep -q "\`$decl\`" .mathlib-quality/overview/PROGRESS.md
git add -A .mathlib-quality/overview PROJECT_OVERVIEW.md
git commit -q -m "overview: assess $decl ($verdict)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
git push -q origin HEAD:ramin-cleanup-2
git log --oneline -1
