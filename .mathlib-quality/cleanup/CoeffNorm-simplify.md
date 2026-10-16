# CoeffNorm holistic simplify review

Verdict: **two minor, compiled simplifications**. No mathematical, public-signature,
reuse, or structural defect found. Source was reviewed read-only; the file owner
should apply the following patch and rerun its gates.

Reviewed `Roth/CoeffNorm.lean`, SHA-256
`6bd90da3a6a467e166523e006f4911384e2d3ffd7c277b40d8a660c39d9aa738`,
including the cumulative diff against `e63b156` and
`/private/tmp/roth-coeffnorm-original.lean`. Read the `mathlib-quality` and `lean4`
skills, cleanup gate reference, proof-simplification reference, and golfing rules.
Read the exact Phase 6.5 instructions (lines 1556–1632) in the installed cleanup
command at `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`.
The built-in `/simplify` entry point is unavailable. This is the requested independent
fallback review, not an assertion that the built-in command ran. The earlier report
incorrectly claimed that no installed cleanup command was found; that claim is corrected
here. The review covers all three requested dimensions: reuse (shared norm and box
proofs), quality (whole-file structure and preserved contracts), and efficiency
(unnecessary import and redundant classical setup).

## Exact compiled patch

```diff
--- a/Roth/CoeffNorm.lean
+++ b/Roth/CoeffNorm.lean
@@
-import Mathlib.Algebra.MvPolynomial.Polynomial
 import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
@@
 private theorem sum_box_prod_pow_le_aux [Fintype σ] (r : σ → ℕ) {B : ℝ} (hB : 0 ≤ B) (x : σ → ℝ) :
     ∑ k ∈ box r, B * ∏ j, |x j| ^ k j ≤ B * ∏ j, (1 + |x j|) ^ r j := by
-  classical
   simpa [← Finset.mul_sum, box, Finset.prod_univ_sum] using
```

1. The multivariate/univariate polynomial bridge import is unused. The whole file
   compiles without it. Its two extra bridge results are not used by these proofs;
   the existing induction proof of `eval_diag` requires neither. Benefit: remove an
   unnecessary direct import. No build-time improvement is claimed.
2. The helper's surrounding `open scoped Classical in` already supplies classical
   decidability throughout the declaration. Its `classical` tactic is redundant.
   Benefit: remove one repeated setup line, with the helper statement unchanged.

## Compiler evidence

Each command ran from `/Users/ramin/LEAN/Roth`, using the existing toolchain and
built dependency artifacts. These were **full copies of the source**, not isolated
replacement lemmas:

| Scratch file | Change | Command/result |
|---|---|---|
| `/private/tmp/coeffnorm_no_mvpoly.lean` | Remove first import only | `/Users/ramin/.elan/bin/lake env lean /private/tmp/coeffnorm_no_mvpoly.lean` — exit 0 |
| `/private/tmp/coeffnorm_helper_scope.lean` | Remove helper `classical` only | `/Users/ramin/.elan/bin/lake env lean /private/tmp/coeffnorm_helper_scope.lean` — exit 0 |
| `/private/tmp/coeffnorm_simplify_combined.lean` | Both changes | `/Users/ramin/.elan/bin/lake env lean /private/tmp/coeffnorm_simplify_combined.lean` — exit 0 |
| `/private/tmp/coeffnorm_no_det.lean` | Remove determinant import only | `/Users/ramin/.elan/bin/lake env lean /private/tmp/coeffnorm_no_det.lean` — exit 1; `Matrix`, `Matrix.of`, and `Matrix.det_apply'` unavailable |

The successful checks retain the existing unused `hC` warning. This is the already
pending API proposal, not a new finding; neither removal nor warning suppression is
proposed here. No full-project build or performance profile was run.

## Other concrete review checks

- All 26 original comment/docstring blocks compare exactly equal to the original
  snapshot. The missing copyright header remains unchanged as instructed.
- The two definitions and all 23 public theorem declarations remain present. The
  existing public-API preservation boundary rules out wrapper deletion or public
  restatement as simplifications.
- Reviewed the whole norm/derivative/determinant chain for duplicated expansion
  proofs. `normOne_sum_le`, `normOne_prod_le`, and the private box bound already
  consolidate the recurring inequalities; further helper extraction would add
  indirection to short proofs.
- Reviewed diagonal substitution as a possible cross-declaration simplification.
  Native LSP `lean_multi_attempt` at the actual `eval_diag` proof line 191 rejects
  `rfl`, `simp [diag]`, and `simp [diag, aeval_def, eval₂_map]` with unsolved goals.
  The existing one-line induction proof remains concise and justified. An earlier
  attempt targeted line 158 (outside that proof) and produced parser errors; it was
  discarded rather than treated as mathematical evidence.
- The final determinant estimate composes the established coefficient, norm,
  derivative, and support bounds directly. The small support-card intermediate is
  useful to the inequality chain; no repeated abstraction or dead helper remains.
- Every scratch compiler process completed. No `.lean` source, Git state, or
  workflow-progress file was modified by this review.

## Simplify pass — `Roth/CoeffNorm.lean`

Outcome: **ISSUES-FOUND-NOT-FIXED** by this read-only reviewer.

Issues identified by the independent fallback review:
- Unused `Mathlib.Algebra.MvPolynomial.Polynomial` import.
- Redundant helper `classical` under `open scoped Classical in`.

Fixes applied by this reviewer: none; the exact combined patch above compiles. The
file owner is applying these fixes and is responsible for Phase 6.5c's renewed
diagnostics, module build, statement/definition preservation, and downstream gates.

Files modified by this reviewer:
- `.mathlib-quality/cleanup/CoeffNorm-simplify.md` only.

This status describes the reviewer's handoff, not the file owner's eventual
ISSUES-FOUND-AND-FIXED outcome after application and revalidation.
