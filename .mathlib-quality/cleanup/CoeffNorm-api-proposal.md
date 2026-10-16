# Concrete CoeffNorm unused-hypothesis proposal — awaiting user decision

No proposed public signature change has been applied to project source.

Compiler evidence: `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-coeffnorm-api-proposal.lean`, session46719 exit0. The entire original320-line module was compiled under `Roth.CoeffNormProposal` with exactly the following changes, so proofs and internal callers work together. All four proposed theorem axiom sets contain only propext,Classical.choice,Quot.sound. Both old and proposed fully elaborated signatures are printed in `/private/tmp/roth-coeffnorm-api-proposal.log`.

Proposed public changes:

1. Remove `[DecidableEq σ]` from `Roth.normOne_mul_le`, `Roth.normOne_prod_le`, `Roth.normOne_det_le`, and `Roth.abs_coeff_det_hasseDeriv_le`.
2. Remove explicit `(hC : 0 ≤ C)` from `Roth.normOne_det_le`; preserve its name, all other arguments, and conclusion.

Minimal proof/caller adjustments:

- Add `classical` inside normOne_mul_le and normOne_det_le (normOne_prod_le already has it).
- Sole explicit hC caller is the local `abs_coeff_det_hasseDeriv_le`: `normOne_det_le _ hC0 hentry` becomes `normOne_det_le _ hentry`.
- Delete now-unused local positivity witnesses hC0 and hN0 there.
- Source search across all Roth Lean files finds only internal normOne_mul/prod/det callers; the sole external caller of abs_coeff_det_hasseDeriv_le is Theta.lean:440 and uses ordinary application (no explicit instance argument), so no source change there is expected. Full downstream builds remain mandatory after approved application.

Why valid: DecidableEq is proof-only and classical synthesis supplies it; the nonnegative norm bounds hM suffice for the determinant estimate. For l=0 the determinant estimate is1≤1 independently of C; for positive l the entry bounds already force C nonnegative. The existing proof never uses hC, as baseline LSP reports.

These removals strengthen applicability and preserve mathematical conclusions, but alter public elaborated signatures. Earlier Box/Wronskian approval was scoped and is not treated as approval here. Dedicated declaration audits still run individually; this proposal does not count any declaration complete. Retaining the original APIs is also viable and leaves the existing warnings explicit, unsuppressed.
