---
decl: Roth.mem_support_taylor_iff
file: Roth/Index.lean
line: 62
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-line bridge d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 (MvPolynomial.mem_support_iff then coeff_taylor), used at four call sites in Roth/Index.lean to translate between the support-based definition of index and the derivative-based statements.
action: Keep as private helper in Roth/Index.lean (uses at l.72, 81, 90, 228); optional low-priority generalisation from ℝ to any CommSemiring R if it is ever made public next to coeff_taylor in Roth/Taylor.lean.
---

# Roth.mem_support_taylor_iff

## Inventory entry

### `theorem Roth.mem_support_taylor_iff`
- **Type**: `∀ {σ : Type*} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ}, d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0`
- **What**: A multi-index d lies in the support of the Taylor shift P(X + α) iff the d-th Hasse derivative of P does not vanish at α; i.e. the support of the shifted polynomial is exactly the set of tuples entering the minimum that defines the index.
- **How**: `rw [mem_support_iff, coeff_taylor]` — mathlib's `MvPolynomial.mem_support_iff` turns membership into `coeff d (taylor α P) ≠ 0`, and the project's Taylor theorem `MvPolynomial.coeff_taylor` (Roth/Taylor.lean:134) rewrites the coefficient as `eval α (hasseDeriv d P)`.
- **Hypotheses**: none beyond the implicit data; `omit [Fintype σ] in` drops the section's `Fintype σ`. Stated over ℝ only because the surrounding file is; the proof works verbatim over any `CommSemiring R` (both rewritten lemmas are stated at that generality).
- **Uses from project**: `MvPolynomial.taylor` (Roth/Taylor.lean:42), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `MvPolynomial.coeff_taylor` (Roth/Taylor.lean:134)
- **Used by**: Roth/Index.lean only (`grep -rn mem_support_taylor_iff Roth/`): `index_le_weight` (l.72, `.2`), `exists_weight_eq_index` (l.81, `.1`), `le_index_iff` (l.90, `.1`), `index_le_card` (l.228, `.2`). Transitively everything built on these index API lemmas.
- **Visibility**: private
- **Lines**: 61–64 (incl. `omit` line), proof length 1 line
- **Notes**: Declared `private lemma` (kind recorded as theorem). The same rewrite pair is inlined once elsewhere, in `degreeOf_taylor_le` (Roth/Taylor.lean:173, `simp [mem_support_iff, coeff_taylor, ...]`), which is in a different file and cannot see this private lemma.

## Junk check (Step 8)
- Used anywhere? Yes, four times in Roth/Index.lean (l.72, 81, 90, 228), in both directions.
- Wrapper of 1–2 mathlib calls? Yes: a composition of `MvPolynomial.mem_support_iff` (mathlib, Mathlib/Algebra/MvPolynomial/Basic.lean:513) and the project's `coeff_taylor`. But it is used in term mode (`mem_support_taylor_iff.2 h`, `.1 hd`) inside `csInf_le`/`csInf_mem`/`monomial_le_degreeOf` arguments; inlining would need `(mem_support_iff.2 ((coeff_taylor α d P).symm ▸ h))`-style terms or extra `rw` steps at four sites, a net loss of readability.
- Does mathlib have it? No: `taylor` and `hasseDeriv` for MvPolynomial are project definitions, so the statement cannot exist in mathlib; `grep -rn mem_support_taylor .lake/packages/mathlib/Mathlib/` returns nothing.
- Too specific? It is exactly the bridge between the definition of `index` (an `sInf` over `(taylor α P).support`) and the paper's formulation (minimum over tuples with Δ_d P(α) ≠ 0), so it is the right granularity for this file.
- Well-chosen? Yes. Minor: could be stated for general `CommSemiring R` and made public in Roth/Taylor.lean (also usable at Taylor.lean:173), but that is cosmetic.
- Conclusion: `KEEP` — action: keep as private helper in Roth/Index.lean; no change required.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Index.lean:62).

Note: if `MvPolynomial.taylor` / `coeff_taylor` are upstreamed, a public, ring-general `MvPolynomial.mem_support_taylor_iff` would be a natural companion simp-style lemma next to `coeff_taylor`; that would be a new declaration, not this private one.

## Evidence
- `grep -rn mem_support_taylor_iff Roth/`: definition l.62, uses l.72, 81, 90, 228 (all Roth/Index.lean).
- `grep -rn "theorem mem_support_iff" .lake/packages/mathlib/Mathlib/Algebra/MvPolynomial/Basic.lean`: l.513.
- `grep -rn mem_support_taylor .lake/packages/mathlib/Mathlib/`: no results.
- `grep -rn support Roth/Taylor.lean Roth/HasseDeriv.lean`: only the inlined analogue at Taylor.lean:173; no public project lemma subsumes it.
- No Lean runs and no evidence Lean files (no weakening claimed; the project builds clean so the lemma compiles as stated).
