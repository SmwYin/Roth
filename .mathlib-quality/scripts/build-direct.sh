#!/bin/zsh
# Build the project's modules in dependency order with `lean` directly (no lake), writing
# .olean/.ilean files where lake would put them, so that later modules can import earlier ones.
# usage: .mathlib-quality/scripts/build-direct.sh [Module ...]   (default: all modules of Roth.lean)
set -e
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
OUT="$ROOT/.lake/build/lib/lean"
if [ $# -gt 0 ]; then MODS=("$@"); else
  MODS=($(grep -o 'import Roth\.[A-Za-z0-9_.]*' Roth.lean | sed 's/import //'))
fi
rc=0
for m in "${MODS[@]}"; do
  f="${m//.//}.lean"; o="$OUT/${m//.//}.olean"; i="$OUT/${m//.//}.ilean"
  mkdir -p "$(dirname "$o")"
  echo "== $m"
  if "$ROOT/.mathlib-quality/scripts/lean-direct.sh" -R "$ROOT" -o "$o" -i "$i" "$f"; then :; else rc=1; fi
done
exit $rc
