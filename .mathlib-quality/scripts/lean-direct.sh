#!/bin/zsh
# Run `lean` directly with the project's dependency path (workaround: the v4.34.0-rc2 `lake`
# binary crashes with SIGTRAP on this machine; see .mathlib-quality/plan.md § Toolchain note).
# usage: .mathlib-quality/scripts/lean-direct.sh <args to lean>
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
P="$ROOT/.lake/packages"
export LEAN_PATH="$P/mathlib/.lake/build/lib/lean:$P/batteries/.lake/build/lib/lean:$P/aesop/.lake/build/lib/lean:$P/Qq/.lake/build/lib/lean:$P/proofwidgets/.lake/build/lib/lean:$P/importGraph/.lake/build/lib/lean:$P/LeanSearchClient/.lake/build/lib/lean:$P/plausible/.lake/build/lib/lean:$P/Cli/.lake/build/lib/lean:$ROOT/.lake/build/lib/lean"
exec lean "$@"
