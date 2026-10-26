---
decl: MvPolynomial.hasseCoeff_mul_succ
file: Roth/HasseDeriv.lean
line: 191
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private multi-index absorption identity binom(n,d)(e_j+1) = (d_j+1) binom(n,d+e_j) with n = e+e_j+d, a one-line specialisation of hasseCoeff_mul_hasseCoeff used only by pderiv_hasseDeriv; mathlib has only the scalar Nat.choose_succ_right_eq.
action: Keep as private helper for its single call site Roth/HasseDeriv.lean:205 (pderiv_hasseDeriv); if hasseCoeff is upstreamed as Finsupp.choose, restate it there as a multi-index analogue of Nat.choose_succ_right_eq.
---

# MvPolynomial.hasseCoeff_mul_succ

## Inventory entry

### `theorem MvPolynomial.hasseCoeff_mul_succ`
- **Type**: `∀ {σ : Type*} (j : σ) (d e : σ →₀ ℕ), hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) = (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d)`
- **What**: Multi-index absorption identity for the binomial coefficient binom(k, d) = ∏_i binom(k_i, d_i): with n = e + e_j + d (e_j the j-th unit multi-index), binom(n, d) · (e_j + 1) = (d_j + 1) · binom(n, d + e_j). Only the j-th factor changes; it is the scalar identity C(N, a)·(N - a) = (a+1)·C(N, a+1). It is the coefficient identity behind ∂_j Δ_d = (d_j + 1) Δ_{d + e_j}.
- **How**: One-line `simpa [hasseCoeff, add_comm, add_left_comm, add_assoc, mul_comm] using hasseCoeff_mul_hasseCoeff e (Finsupp.single j 1) d`, i.e. instantiates the private multi-index `Nat.choose_mul` identity with (f, d, e) := (e, single j 1, d) and lets `simp` evaluate `hasseCoeff (single j 1) _` to `e j + 1` and `hasseCoeff (single j 1) (single j 1 + d)` to `d j + 1` (via `Finsupp.prod_single_index`, `Nat.choose_one_right`) and normalise the additions.
- **Hypotheses**: none beyond the types (σ arbitrary; R does not occur).
- **Uses from project**: `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_mul_hasseCoeff` (private)
- **Used by**: Roth/HasseDeriv.lean: `pderiv_hasseDeriv` (l.200, `rw` at l.205) only (grep over `Roth/` and `Roth.lean`). Transitively: `factorial_smul_hasseDeriv_single` (Roth/HasseDeriv.lean:286, uses `pderiv_hasseDeriv` at l.291) and `derivative_kronHasse_aux` (Roth/GenWronskian.lean:153, uses `pderiv_hasseDeriv` at l.159).
- **Visibility**: private
- **Lines**: 191–195, proof length 2 lines
- **Notes**: Declared with `lemma` (kind recorded as theorem). The statement shape (`e + single j 1 + d`, factor on the right of LHS / left of RHS) is tailored to the `rw` chain in `pderiv_hasseDeriv` after `← add_assoc e d, add_right_comm e d, mul_right_comm, ← Nat.cast_add_one, ← Nat.cast_mul`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `pderiv_hasseDeriv` (Roth/HasseDeriv.lean:205), which is itself used in `factorial_smul_hasseDeriv_single` and `GenWronskian.derivative_kronHasse_aux`.
- Wrapper of 1–2 mathlib calls? It is a one-line specialisation of a project lemma (`hasseCoeff_mul_hasseCoeff`) plus simp normalisation, not of a mathlib lemma.
- Does mathlib have it? No multi-index version: `grep -rn "hasseCoeff\|Finsupp.choose"` over `.lake/packages/mathlib/Mathlib` is empty. The scalar analogue exists: `Nat.choose_succ_right_eq : choose n (k + 1) * (k + 1) = choose n k * (n - k)` (Mathlib/Data/Nat/Choose/Basic.lean:210); also `Nat.choose_mul_succ_eq` (l.220).
- Too specific / inline? Inlining into `pderiv_hasseDeriv` is feasible (replace the `rw [..., hasseCoeff_mul_succ, ...]` step by a `have` with the same `simpa`), saving one declaration but making the already long `rw` chain harder to read; the separate private helper is the cleaner factoring with a single call site of 2 lines either way. No net benefit to inlining.
- Well-chosen? Yes as a local private helper. As public API it would be stated in the `Nat.choose_succ_right_eq` shape on a multi-index `Finsupp.choose` (with tsub), not in this call-site-tailored shape.
- Conclusion: `KEEP` — action: keep as private helper for `pderiv_hasseDeriv`; revisit its shape only in a `Finsupp.choose` upstreaming PR (parent `MvPolynomial.hasseCoeff`).

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/HasseDeriv.lean:191).

Note for the parent upstreaming (`MvPolynomial.hasseCoeff`, verdict YES-but-generalise-first): porting `pderiv_hasseDeriv` would want a public multi-index analogue of `Nat.choose_succ_right_eq`; this lemma (via `hasseCoeff_mul_hasseCoeff`) is its proof template.

## Evidence
- `grep -rn hasseCoeff_mul_succ Roth/`: definition l.191, single use l.205 (`pderiv_hasseDeriv`).
- `grep -rn pderiv_hasseDeriv Roth/`: uses at Roth/HasseDeriv.lean:291 (`factorial_smul_hasseDeriv_single`) and Roth/GenWronskian.lean:159 (`derivative_kronHasse_aux`).
- `grep` in Mathlib/Data/Nat/Choose/Basic.lean: `Nat.choose_succ_right_eq` (l.210), `Nat.choose_mul_succ_eq` (l.220) — scalar only.
- `grep -rn "hasseCoeff\|Finsupp.choose"` over mathlib: no hits.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
