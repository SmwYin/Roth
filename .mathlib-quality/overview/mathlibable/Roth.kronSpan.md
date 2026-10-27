---
decl: Roth.kronSpan
file: Roth/GenWronskian.lean
line: 149
kind: def
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private K[X]-submodule spanned by the operators kronHasse k d with deg d at most mu; it is the induction invariant that turns the existential of exists_hasseDeriv_kronecker_eq_sum into closure lemmas (derivative_mem_kronSpan, hasseDeriv_kronecker_mem), and mathlib has no multivariate Hasse derivative or Kronecker substitution to build it from.
action: Keep as private helper used by derivative_mem_kronSpan (Roth/GenWronskian.lean:162-188) and hasseDeriv_kronecker_mem (l.190-205); if Lemma 1 is upstreamed, carry it along with kronHasse, re-based on the weighted substitution aeval (fun j => X ^ w j) recommended in the Roth.kronecker report.
---

# Roth.kronSpan

## Inventory entry

### `def Roth.kronSpan`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k μ : ℕ) : Submodule (Polynomial K) (MvPolynomial σ K → Polynomial K)`
- **What**: The K[t]-submodule of the (pointwise) K[t]-module of functions MvPolynomial σ K → K[t] spanned by the operators P ↦ (Δ_d P)(t, t^k, t^(k^2), ...) for multi-indices d with total degree |d| ≤ μ. Membership of an operator F says F(P) = Σ_d c_d(t) · kronecker k (Δ_d P) uniformly in P, with all |d| ≤ μ.
- **How**: Direct definition `Submodule.span (Polynomial K) (kronHasse k '' {d | d.degree ≤ μ})` (mathlib `Submodule.span`, `Set.image`, `Finsupp.degree`); no proof.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` from the section variables (`[Fintype σ]` inherited from `kronHasse`/`kronecker`, which use `Fintype.equivFin σ`; the span itself only needs `CommSemiring K`, but the section and parents fix `Field`).
- **Uses from project**: `Roth.kronHasse` (Roth/GenWronskian.lean:145).
- **Used by**: Roth/GenWronskian.lean only (`grep -rn kronSpan Roth/`): `derivative_mem_kronSpan` l.162–164 (hypothesis and conclusion; `Submodule.span_induction` on membership, `zero_mem` at l.175, `add_mem` at l.183, `span_mono` for the μ ≤ μ+1 monotonicity), `hasseDeriv_kronecker_mem` l.191 (statement), l.198 (`restrictScalars K` + `smul_mem_iff` to cancel the factor μ+1), l.201 (`change`), l.202 (calls `derivative_mem_kronSpan`). Transitively feeds `exists_hasseDeriv_kronecker_eq_sum` (l.219, via `Finsupp.mem_span_image_iff_linearCombination`, which unfolds the span into a finite combination) and hence `exists_genWronskian_ne_zero` (Lemma 1).
- **Visibility**: private
- **Lines**: 148–151 (docstring l.148, declaration l.149–151), body 1 line
- **Notes**: `private noncomputable def`. It does not appear in any public statement: the public `exists_hasseDeriv_kronecker_eq_sum` states the conclusion explicitly as a finite sum, extracting it from span membership.

## Junk check (Step 8)
- Used anywhere? Yes: two private lemmas state their results in terms of it (`derivative_mem_kronSpan`, `hasseDeriv_kronecker_mem`), and the public `exists_hasseDeriv_kronecker_eq_sum` consumes membership via `Finsupp.mem_span_image_iff_linearCombination`.
- Wrapper of 1–2 mathlib calls? It is a single `Submodule.span` of an image set, so formally a one-call wrapper; but the name is what makes the statements of the two closure lemmas readable and lets `span_induction`, `zero_mem`, `add_mem`, `smul_mem`, `restrictScalars` be applied to a named object (several `convert ... (kronSpan k (μ+1)).zero_mem` steps rely on it being a term with explicit implicit-argument control `(K := K) (σ := σ)`). Inlining would repeat `Submodule.span (Polynomial K) (kronHasse k '' {d | d.degree ≤ μ + 1})` at about six places.
- Does mathlib have it? No. Its generators require a multivariate Hasse derivative and a Kronecker substitution, neither of which exists in mathlib (see the Roth.kronHasse and Roth.kronecker reports: `def hasseDeriv` only in Mathlib/Algebra/Polynomial/HasseDeriv.lean and Mathlib/RingTheory/LaurentSeries.lean; no `Kronecker substitution`). The ambient construction (span of an image in a function module over a ring acting pointwise) is plain `Submodule.span`, which is already what is used.
- Too specific / inline? Specific to the proof of Lemma 1, but it is the right abstraction: the paper's claim "d^μ/dt^μ h_ν is a K[t]-combination of (Δ φ_ν)(γ(t)) with order ≤ μ, uniformly in ν" is exactly membership in this span, and phrasing it as a submodule reduces the induction to closure properties (derivative maps kronSpan μ into kronSpan (μ+1)). A direct existential-based induction would need to carry and re-index finite sums by hand. Not worth inlining.
- Well-chosen? Yes: span over K[t] (not K) is essential, as the coefficients c_d(t) are polynomials; the bound `d.degree ≤ μ` (set-builder) matches the target statement `∀ d ∈ s, d.degree ≤ μ` and is monotone in μ, which `derivative_mem_kronSpan`'s `smul` case uses via `span_mono`. Minor note: the docstring says "|d| ≤ μ" while the code uses `Finsupp.degree`, which is the total degree, consistent.
- Conclusion: `KEEP`. Action: none; keep as private helper of the Lemma 1 proof.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private noncomputable def` at Roth/GenWronskian.lean:149).

Note for an eventual upstreaming of Lemma 1 (`exists_genWronskian_ne_zero`) / `exists_hasseDeriv_kronecker_eq_sum`: generator `Roth.kronHasse` is private SKIP (junk KEEP); its parents `Roth.kronecker` and `MvPolynomial.hasseDeriv` were assessed YES-but-generalise-first. This span would travel with `kronHasse` as a proof-internal device, restated against the weighted substitution recommended in the Roth.kronecker report.

## Evidence
- `grep -rn kronSpan Roth/`: definition l.149; uses l.162, 163, 164, 175, 183, 191, 198, 201, 202; all in Roth/GenWronskian.lean.
- `grep -rn hasseDeriv_kronecker_mem Roth/`: l.190 (def), l.219 (use in `exists_hasseDeriv_kronecker_eq_sum`).
- Sibling/parent reports read: .mathlib-quality/overview/mathlibable/Roth.kronHasse.md (SKIP, KEEP), Roth.kronecker.md (YES-but-generalise-first).
- Mathlib absence of generators relies on the greps recorded in Roth.kronHasse.md (no multivariate `hasseDeriv`, no Kronecker substitution in .lake/packages/mathlib/Mathlib/).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the definition compiles as stated.
