---
decl: Roth.hasseDeriv_kronecker_mem
file: Roth/GenWronskian.lean
line: 190
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private induction on mu showing the operator P mapsto hasseDeriv mu (kronecker k P) lies in the K[t]-span kronSpan k mu; membership form of exists_hasseDeriv_kronecker_eq_sum, specific to the private kronHasse/kronSpan machinery of Lemma 1, no mathlib analogue.
action: Keep as private helper of exists_hasseDeriv_kronecker_eq_sum (Roth/GenWronskian.lean:219); if Lemma 1 is upstreamed, carry it with kronHasse/kronSpan/derivative_mem_kronSpan restated for the weighted substitution.
---

# Roth.hasseDeriv_kronecker_mem

## Inventory entry

### `theorem Roth.hasseDeriv_kronecker_mem`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] [CharZero K] (k μ : ℕ) : (fun P ↦ Polynomial.hasseDeriv μ (kronecker k P)) ∈ kronSpan k μ`
- **What**: The operator MvPolynomial σ K → K[t], P ↦ D^{(μ)}_t (P(t, t^k, …, t^{k^{p-1}})) (μ-th univariate Hasse derivative of the Kronecker substitution) lies in the K[t]-submodule of functions spanned by the operators P ↦ kronecker k (Δ_d P) with |d| ≤ μ (Δ_d the multivariate Hasse derivative). This is the "for each μ there are f^μ_i(t) and Δ^{(i)}_μ of order ≤ μ" statement of §2, proof of Lemma 1, in submodule-membership form.
- **How**: Induction on `μ`. Base: `Submodule.subset_span` at generator `d = 0` (`kronHasse k 0 = kronecker k`, by `simp [kronHasse]`, using `hasseDeriv` at 0 being the identity). Step: cancel the nonzero scalar `((μ+1 : ℕ) : K)` (needs `CharZero K`, `Nat.cast_ne_zero`) via `Submodule.smul_mem_iff` on `(kronSpan k (μ+1)).restrictScalars K`; then `convert` to the project lemma `derivative_mem_kronSpan k μ ih` and identify `(μ+1) • D^{(μ+1)} = D ∘ D^{(μ)}` pointwise from mathlib's `Polynomial.hasseDeriv_comp` (with `k = 1`, `l = μ`), `Nat.cast_smul_eq_nsmul`, `add_comm`.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` (section variables), `[CharZero K]` (used to divide by μ+1). No condition on `k`.
- **Uses from project**: `Roth.kronecker` (Roth/GenWronskian.lean:53), `Roth.kronSpan` (l.149), `Roth.kronHasse` (l.145, in the base case), `Roth.derivative_mem_kronSpan` (l.162); implicitly `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57) through `kronHasse`.
- **Used by**: `grep -rn hasseDeriv_kronecker_mem Roth/`: only `Roth.exists_hasseDeriv_kronecker_eq_sum` (Roth/GenWronskian.lean:219, unpacked by `Finsupp.mem_span_image_iff_linearCombination`). Transitively feeds Lemma 1 `exists_genWronskian_ne_zero` (l.254).
- **Visibility**: private
- **Lines**: 190–205, proof length 14 lines (l.192–205)
- **Notes**: `CharZero K` is an artefact of the proof (dividing D∘D^{(μ)} by μ+1); mathematically the statement holds in any characteristic (Taylor-expand P(γ(t+h)) = Σ_d Δ_d P(γ(t)) (γ(t+h) − γ(t))^d and read off the h^μ coefficient; only |d| ≤ μ contribute since γ(t+h) − γ(t) is divisible by h). Not compiled; irrelevant for Roth (K = ℚ) and recorded only as a pointer for an eventual upstreaming.

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_hasseDeriv_kronecker_eq_sum` l.219, which is the public statement of the same fact.
- Wrapper of 1–2 mathlib calls? No: an induction on μ combining the project span-step lemma `derivative_mem_kronSpan` with a scalar cancellation and `Polynomial.hasseDeriv_comp`.
- Does mathlib have it? No. mathlib has univariate `Polynomial.hasseDeriv` but no multivariate Hasse derivative and no Kronecker substitution (`grep -rln kronecker` over `Mathlib/Algebra/MvPolynomial` and `Mathlib/RingTheory/MvPolynomial`: no hits); `kronSpan`/`kronHasse` are project-private.
- Too specific / inline? It could be inlined into `exists_hasseDeriv_kronecker_eq_sum` (single use), but the membership form is exactly what the induction needs (the IH must range over the span), while the public theorem gives the user-facing ∃-sum form; splitting them is the right structure.
- Well-chosen? Yes.
- Conclusion: `KEEP`. Action: none; keep as private helper of `exists_hasseDeriv_kronecker_eq_sum`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/GenWronskian.lean:190).

Note for an eventual upstreaming of Lemma 1: this lemma would travel with the private `Roth.kronHasse`, `Roth.kronSpan`, `Roth.derivative_kronHasse_aux`, `Roth.derivative_mem_kronSpan` (all SKIP/KEEP), restated for the weighted substitution `aeval (fun j ↦ X ^ w j)` recommended in the Roth.kronecker report, and ideally with the `CharZero` hypothesis removed via a Taylor-expansion proof (see Notes).

## Evidence
- `grep -rn hasseDeriv_kronecker_mem Roth/`: definition l.190, single use l.219 (Roth/GenWronskian.lean).
- `grep -rn "theorem hasseDeriv_comp" .lake/packages/mathlib/Mathlib/`: `Polynomial.hasseDeriv_comp` at Mathlib/Algebra/Polynomial/HasseDeriv.lean:154 (the lemma used in the step case).
- `grep -rln kronecker` over mathlib `Algebra/MvPolynomial` and `RingTheory/MvPolynomial`: no hits.
- Read sibling report Roth.derivative_mem_kronSpan.md.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated. The CharZero remark in Notes is a mathematical observation, not a compiled claim.
