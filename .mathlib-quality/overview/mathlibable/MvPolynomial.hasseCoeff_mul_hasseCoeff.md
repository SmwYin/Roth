---
decl: MvPolynomial.hasseCoeff_mul_hasseCoeff
file: Roth/HasseDeriv.lean
line: 153
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private multi-index form of Nat.choose_mul (binom(f+d,d) binom(f+d+e,e) = binom(d+e,d) binom(f+d+e,d+e)), the combinatorial core of hasseDeriv_hasseDeriv and hasseCoeff_mul_succ; mathlib has only the scalar Nat.choose_mul and no multi-index binomial.
action: Keep as private helper (call sites Roth/HasseDeriv.lean:179 hasseDeriv_hasseDeriv and :195 hasseCoeff_mul_succ); when upstreaming hasseCoeff as Finsupp.choose, publish it there as Finsupp.choose_mul in the Nat.choose_mul shape.
---

# MvPolynomial.hasseCoeff_mul_hasseCoeff

## Inventory entry

### `theorem MvPolynomial.hasseCoeff_mul_hasseCoeff`
- **Type**: `∀ {σ : Type*} (f d e : σ →₀ ℕ), hasseCoeff d (f + d) * hasseCoeff e (f + d + e) = hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e))`
- **What**: Multi-index "subset-of-a-subset" binomial identity: for multi-indices f, d, e, binom(f+d, d) · binom(f+d+e, e) = binom(d+e, d) · binom(f+d+e, d+e), with binom(k, d) = ∏_j binom(k_j, d_j). It is the coefficient identity behind the Hasse-derivative composition rule Δ_d Δ_e = binom(d+e, d) Δ_{d+e}.
- **How**: Unfolds `hasseCoeff` to `Finsupp.prod`, rewrites all four support-indexed products as products over the common finset `d.support ∪ e.support` via `Finsupp.prod_of_support_subset` (side condition `Nat.choose_zero_right`, support inclusions `Finset.subset_union_left/right`, `Finsupp.support_add`), merges them with `Finset.prod_mul_distrib`, and closes each factor by `Finset.prod_congr` with the scalar identity `Nat.choose_mul` (n := f i + d i + e i, k := d i + e i, s := e i) plus `Nat.choose_symm_add` and `mul_comm`/`add_assoc` reshuffling.
- **Hypotheses**: none beyond the types (`σ` arbitrary; section `[CommSemiring R]` is not included since R does not occur).
- **Uses from project**: `MvPolynomial.hasseCoeff`
- **Used by**: Roth/HasseDeriv.lean: `hasseDeriv_hasseDeriv` (l.179, `rw`), `hasseCoeff_mul_succ` (l.195, private, `simpa using hasseCoeff_mul_hasseCoeff e (Finsupp.single j 1) d`). No other use in `Roth/` (grep over `Roth/` and `Roth.lean`).
- **Visibility**: private
- **Lines**: 153–168, proof length 13 lines
- **Notes**: Declared with `lemma` (kind recorded as theorem). The statement shape is tuned to the `rw` chain in `hasseDeriv_hasseDeriv` (f + d, f + d + e, then `add_assoc`), not to the literature/mathlib `Nat.choose_mul` shape `choose n k * choose k s = choose n s * choose (n - s) (k - s)`.

## Junk check (Step 8)
- Used anywhere? Yes, twice: `hasseDeriv_hasseDeriv` (Roth/HasseDeriv.lean:179) and `hasseCoeff_mul_succ` (Roth/HasseDeriv.lean:195), the latter feeding `pderiv_hasseDeriv`.
- Wrapper of 1–2 mathlib calls? No: it needs the support-alignment of four `Finsupp.prod`s onto a common finset plus a pointwise `Nat.choose_mul` with `Nat.choose_symm_add` reshuffling (13-line proof).
- Does mathlib have it? No. Mathlib has only the scalar `Nat.choose_mul` (Mathlib/Data/Nat/Choose/Basic.lean:159) and no multi-index binomial (`grep` for `Finsupp.choose`/`hasseCoeff` in `.lake/packages/mathlib/Mathlib` is empty; loogle `Nat.choose, Finsupp.prod, HMul.hMul` returns no results). Consistent with the parent report `MvPolynomial.hasseCoeff.md`.
- Too specific / inline? Inlining into `hasseDeriv_hasseDeriv` is possible but would duplicate it, since `hasseCoeff_mul_succ` also instantiates it (with d := single j 1); a shared helper is the right factoring. Private visibility is appropriate for its current tailored shape.
- Well-chosen? Yes as a local helper. As public API (when `hasseCoeff` is upstreamed as `Finsupp.choose`), it should be restated in the mathlib `Nat.choose_mul` shape (`d ≤ k → choose n k * choose k d = choose n d * choose (n - d) (k - d)` with Finsupp tsub) and this form derived from it.
- Conclusion: `KEEP` — action: keep as a private helper; revisit its shape only in the Finsupp.choose upstreaming PR.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/HasseDeriv.lean:153).

Note for the parent upstreaming (`MvPolynomial.hasseCoeff`, verdict YES-but-generalise-first): a multi-index `Finsupp.choose_mul` would be needed to port `hasseDeriv_hasseDeriv`; this private lemma is its proof template.

## Evidence
- `grep -rn hasseCoeff_mul_hasseCoeff Roth/ Roth.lean`: definition l.153, uses l.179 and l.195 only.
- `grep -rn "theorem choose_mul "` over mathlib: `Nat.choose_mul` at Mathlib/Data/Nat/Choose/Basic.lean:159 (scalar only).
- `grep -rn "hasseCoeff|Finsupp.choose"` over mathlib: no hits.
- loogle `Nat.choose, Finsupp.prod, HMul.hMul`: no results.
- `lean_local_search` unavailable (ripgrep not installed); replaced by the grep searches above.
- No evidence Lean files written (no weakening or proof experiments needed for a private SKIP).
