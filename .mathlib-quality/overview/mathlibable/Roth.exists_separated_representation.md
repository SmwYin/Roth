---
decl: Roth.exists_separated_representation
file: Roth/Separation.lean
line: 325
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: MODERATE
junk: KEEP
rationale: The real content is the standard linear-algebra fact that over a field every tensor x in M ⊗ N is a sum of l pure tensors with both factor families linearly independent (tensor/Schmidt rank decomposition). Mathlib has TensorProduct.exists_sum_tmul_eq without independence, so that abstract lemma is a genuine gap. But the project form is specialised to MvPolynomial (Option τ) K, adds degree bounds its only caller discards, and moving to the tensor form is a restatement plus a new proof, not a mechanical edit.
action: Ask the user whether to upstream the abstract lemma TensorProduct.exists_sum_tmul_eq_of_linearIndependent (field K, x in M ⊗[K] N) to Mathlib/LinearAlgebra/TensorProduct/Finiteness.lean next to exists_sum_tmul_eq. Keep this theorem locally either way. Optionally drop the two degree-bound conclusions, which the only caller exists_rat_factors_det_hasseDeriv_aux (Separation.lean:521) discards.
---

# Roth.exists_separated_representation

## Inventory entry

### `theorem Roth.exists_separated_representation`
- **Type**: `{τ : Type*} {K : Type*} [Field K] {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ} (hn : degreeOf none P ≤ n) : ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K), LinearIndependent K φ ∧ LinearIndependent K ψ ∧ (∀ ν, (φ ν).natDegree ≤ n) ∧ (∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P) ∧ P = ∑ ν, Polynomial.aeval (X none) (φ ν) * rename some (ψ ν)` (`[Fintype τ] [DecidableEq τ]` are omitted via `omit ... in`).
- **What**: Over a field, a nonzero polynomial `P(x_τ, x_none)` of degree at most `n` in `x_none` can be written as `∑_{ν<l} φ_ν(x_none) ψ_ν(x_τ)`. Here `1 ≤ l ≤ n+1`, both families are linearly independent, `deg φ_ν ≤ n`, and `deg_{x_j} ψ_ν ≤ deg_{x_j} P`.
- **How**: Expand `P = ∑_{ν ≤ n} x_none^ν · coeffNone P ν` (`eq_sum_X_none_pow_mul_coeffNone`). Take a basis `b` of the span of the coefficient polynomials (`exists_coeffNone_basis_aux`, via `Module.finBasis`, `finrank_range_le_card`, `restrictSupport`). Set `ψ_ρ = b ρ`, which is independent by `Module.Basis.linearIndependent.map'` with `Submodule.ker_subtype`. Set `φ_ρ = ∑_ν (b.repr (coeffNone P ν) ρ) X^ν`, which is independent by `linearIndependent_coordinate_polynomials_aux`. The identity comes from `eq_sum_aeval_basis_coeffNone_aux`, and the degree bound from `Polynomial.natDegree_sum_le_of_forall_le` and `Polynomial.natDegree_C_mul_X_pow_le`.
- **Hypotheses**: `[Field K]` (basis of a subspace), `hP : P ≠ 0` (only for `1 ≤ l`), `hn` (degree bound in `x_none`).
- **Uses from project**: `Roth.coeffNone`, `Roth.eq_sum_X_none_pow_mul_coeffNone`, private `Roth.exists_coeffNone_basis_aux`, private `Roth.linearIndependent_coordinate_polynomials_aux`, private `Roth.eq_sum_aeval_basis_coeffNone_aux`.
- **Used by**: `Roth.exists_rat_factors_det_hasseDeriv_aux` (private, Roth/Separation.lean:521–523). It uses `l, hl1, hl2, φ, ψ, hφ, hψ, hPQ` and discards both degree-bound conclusions (`-, -`). Also mentioned in the module docstring (line 31). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 318–345 (statement 325–330), proof 15 lines (331–345)
- **Notes**: The source (clean.tex §2, proof of Lemma 2) gets independence from a minimal-`l` argument. The Lean proof follows the source's Lean implementation note instead (clean.tex:428, "basis of the span of the coefficient polynomials").

## Junk check (Step 8)
- Used anywhere? Yes. One caller, `exists_rat_factors_det_hasseDeriv_aux` (Separation.lean:521), on the path to Lemma 2 (`exists_det_eq_mul`).
- Wrapper of 1–2 mathlib calls? No. It assembles three project helpers plus basis machinery.
- Does mathlib have it? No. Mathlib has `TensorProduct.exists_sum_tmul_eq` (Mathlib/LinearAlgebra/TensorProduct/Finiteness.lean:182), which gives `x = ∑ m j ⊗ₜ n j` with no linear independence. There is no polynomial-specific form.
- Too specific (inline)? No. Inlining 15 lines plus three helpers into the Lemma 2 proof would hurt readability. It is a named source step.
- Well-chosen? Mostly. Two conclusions (`natDegree φ ν ≤ n` and the `degreeOf` bound on `ψ`) are unused, because `exists_det_eq_mul` gets its degree bounds from `degreeOf_det_hasseDeriv_le` instead. They mirror the source statement, so keeping them is defensible.
- Conclusion: `KEEP`. Optionally drop the two unused degree conclusions.

## Mathlibable assessment (Step 9)

Pre-filter: not private. The name does not end in `_aux`. The docstring does not start with internal/auxiliary. Step 8 = KEEP. A namespace-aware grep finds no `Roth.exists_separated_representation` and no `exists_separated_representation` in `.lake/packages/mathlib/Mathlib/`. It is not a glue lemma (15-line proof), so INHERITED does not apply even though the parent def `coeffNone` was assessed (NO-composable-from-mathlib). The full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (per brief; the project builds)
- decl `Roth.exists_separated_representation`: resolved at Roth/Separation.lean:325
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) for polynomials over `Option τ`, culminating in Lemma 2 of the source (`det(Δ Δ^{(none)} R) = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.exists_separated_representation` is a theorem stating the following.

Let `K` be a field and `P ∈ K[x_τ, y]` a nonzero polynomial with `deg_y P ≤ n`. Then there are `1 ≤ l ≤ n+1` and families `φ_0, …, φ_{l-1} ∈ K[y]` and `ψ_0, …, ψ_{l-1} ∈ K[x_τ]` with the following properties. Both families are `K`-linearly independent, `deg φ_ν ≤ n`, `deg_{x_j} ψ_ν ≤ deg_{x_j} P`, and `P = ∑_ν φ_ν(y) ψ_ν(x_τ)`. Equivalently, under `K[x_τ, y] ≅ K[y] ⊗_K K[x_τ]`, the element `P` has a rank decomposition with linearly independent factors on both sides, and that rank is at most `n+1`.

Variables / typeclasses involved (Lean side):
- `τ : Type*`: the remaining variables `x_j`. `none : Option τ` is the separated variable `y = x_p`.
- `K : Type*`, `[Field K]`: coefficients.
- `P : MvPolynomial (Option τ) K`, `n : ℕ`.

Hypotheses (Lean side):
- `hP : P ≠ 0`: needed only for `1 ≤ l`.
- `hn : degreeOf none P ≤ n`: bounds the number of `y`-coefficients, which gives `l ≤ n+1` and `deg φ_ν ≤ n`.

Conclusion (math): `P` is a sum of `l ∈ [1, n+1]` separated products with both factor families linearly independent and with the stated degree control.

Conclusion (Lean): `∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ φ ψ, LinearIndependent K φ ∧ LinearIndependent K ψ ∧ (∀ ν, (φ ν).natDegree ≤ n) ∧ (∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P) ∧ P = ∑ ν, Polynomial.aeval (X none) (φ ν) * rename some (ψ ν)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: An intermediate step inside the proof of Lemma 2 (Roth's separation step). It is listed under the module's Main results, but it is a specialisation of a textbook linear-algebra fact, not a project goal or a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 15
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel                          | Query | Hit? | Standard form found | Notes |
|----|----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)        | polynomial in two sets of variables written as sum phi_i(x) psi_i(y) with linearly independent phi and psi minimal rank | partial | `K(x,y) = ⟨φ(x), ψ(y)⟩` with feature dimension = rank (arXiv:2106.02755) | Polynomial-kernel factorisation at minimal rank. Related "direct sum" decompositions (arXiv:1307.3314). |
|  2 | WebSearch (general form)         | "separation rank" tensor product element minimal number of pure tensors factors linearly independent | yes | tensor rank: fewest rank-one summands; for 2 factors = matrix rank / Schmidt rank (arXiv:1912.06854, cs/0703059) | General form: element of `V ⊗ W`. Two-factor rank is the matrix rank. |
|  3 | WebSearch (named-after / aliases)| Roth's theorem proof lemma polynomial R = sum phi_nu(x_p) psi_nu(x_1..x_{p-1}) minimal l Wronskian factorization | yes | minimal-length `∑ φ_i ψ_i`, minimality forces independence of both families (survey arXiv:2502.00731; Roth 1955, Mathematika) | Exactly the Roth step. Every source uses the minimal-length argument. |
|  4 | WebSearch (tensor statement, MO/MSE/nLab) | every tensor in V ⊗ W can be written as sum v_i ⊗ w_i with v_i linearly independent and w_i linearly independent | yes | "Any tensor admits an independent representation", and such a representation has the minimal number of summands (Whitney algebras, arXiv:1010.2964) | Confirms the abstract standard form (both sides independent; length = rank). |
|  5 | ChatGPT MCP                      | n/a | n/a | n/a | n/a: the `ask_chatgpt_math` MCP is not configured in this session (no such tool in the deferred-tool list). |
|  6 | Local references                 | grep `.mathlib-quality/references/clean.tex` for "linearly independent" / "separat" | yes | clean.tex:369–394 (proof of Lemma 2): minimal-`l` representation `R = ∑ φ_ν(x_p) ψ_ν(x_1..x_{p-1})`, both families independent. clean.tex:428 Lean note: build it from a basis of the span of the coefficient polynomials. | The Lean proof follows the implementation note, not the minimality argument. |
|  7 | nLab                             | tensor product of vector spaces / rank of a tensor | no specific hit | nLab covers tensor products but has no page stating the independent-representation lemma (search #4 found no nLab hit) | The concept is elementary linear algebra. |
|  8 | nCatLab                          | n/a | n/a | n/a | Not a categorical statement. The content is finite-dimensional linear algebra. |
|  9 | Stacks Project                   | n/a | n/a | n/a | Not algebraic geometry. The polynomial ring is used only as a vector space. |
| 10 | MathOverflow / Math.StackExchange| (folded into query #4, which included MO/MSE) | no direct thread | n/a | No thread surfaced. Lecture-note and arXiv sources cover it (rank factorisation of matrices). |
| 11 | recent arXiv (last 5 years)      | (folded into #1–#4) | yes | arXiv:2502.00731 (2025 survey; same minimal-length Roth step), arXiv:2106.02755 (2021), arXiv:2105.08394 (slice rank, 2021) | Same standard form. |

### Literature summary (Phase 3)

Concept identified as: the rank (Schmidt rank / tensor rank of an order-2 tensor) decomposition of an element of `V ⊗_K W`, specialised to `K[y] ⊗_K K[x_τ] ≅ K[x_τ, y]`. In the Roth literature it is the "minimal separated representation" step.
Sources agree on the standard form: yes. Over a field, every `x ∈ V ⊗ W` is `∑_{i<r} v_i ⊗ w_i` with `(v_i)` and `(w_i)` linearly independent, and then `r` is the rank (minimal length).
Most general standard form: for a field `K` and arbitrary `K`-vector spaces `V, W`, every `x ∈ V ⊗_K W` has a representation `∑_{i<r} v_i ⊗ w_i` with both families independent. If `x` lies in `V ⊗ W₀` with `W₀` finite-dimensional (here `W₀ = K[y]_{≤ n}`), then `r ≤ dim W₀`, and the `v_i, w_i` can be chosen in the "spans of the slices" (which gives the degree bounds).
Generality dimensions where the literature varies:
  - Ambient spaces: polynomial rings (Roth) up to arbitrary vector spaces (tensor literature). The most general is arbitrary `V ⊗_K W`.
  - Coefficients: `ℚ` (Roth) up to any field (tensor literature). Over a non-field ring the statement fails in general.
Disagreement with the literature: none on content. The project form is the polynomial specialisation, with extra degree-control conclusions that come from choosing the factors inside the coefficient spans.

### Generality analysis — `Roth.exists_separated_representation`

Literature-standard form (from Phase 3): over a field `K`, every `x ∈ M ⊗[K] N` equals `∑_{i<l} m_i ⊗ₜ n_i` with both families linearly independent, with `l ≤ dim` of any finite-dimensional subspace containing one side.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|------------------------|-------------------|--------------------------|---------------------|---------------------------------|
| 1 | `[Field K]` | field | field (division ring for one-sided vector-space statements) | NO (not mechanically) | The proof needs a basis of the span of the coefficient polynomials (`Module.finBasis`, `FiniteDimensional.span_of_finite`), which is field-specific API. Mathematically the statement also holds over a PID (a submodule of a free module is free), but that would need a different basis API (`Submodule.basisOfPid`) and a different `finrank` bound. This was not attempted and is not claimed as a weakening. The project only needs `ℚ`. |
| 2 | ambient `MvPolynomial (Option τ) K` | polynomial ring in one extra variable | `M ⊗[K] N`, arbitrary vector spaces | yes, as a restatement | The proof uses only the coefficient decomposition `P = ∑ y^ν c_ν` and a basis of `span{c_ν}`. That is the tensor argument applied to `K[y] ⊗ K[x_τ]`. Not a mechanical edit: it needs a new statement and a new proof against `TensorProduct`. |
| 3 | `hP : P ≠ 0` | nonzero | `x ≠ 0` gives `1 ≤ l` | NO | It is used only for `1 ≤ l`, and that conclusion is false for `P = 0`. The hypothesis matches the conclusion. |
| 4 | `hn : degreeOf none P ≤ n` | degree bound | `x ∈ M ⊗ N₀`, `N₀` finite-dimensional | NO (for this form) | It is needed to bound `l ≤ n+1` and `deg φ ≤ n`. Without it, `n := degreeOf none P` always works, so the hypothesis is a convenience parameter, not a restriction. |
| 5 | degree-bound conclusions | `natDegree φ ν ≤ n`, `degreeOf j (ψ ν) ≤ degreeOf (some j) P` | not part of the standard statement | n/a (conclusions) | Extra information, unused by the only caller. Dropping them strengthens nothing and weakens the conclusion. |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (within its polynomial shape; no hypothesis or typeclass can be mechanically dropped)
Number of weakening opportunities found: 0 mechanical. 1 restatement-level (row 2: the abstract tensor form), which is not a single mechanical edit.
Proposed restatement (as a restatement, not a weakening; see 4c):

```lean
theorem TensorProduct.exists_sum_tmul_eq_of_linearIndependent {K M N : Type*} [Field K]
    [AddCommGroup M] [Module K M] [AddCommGroup N] [Module K N] (x : M ⊗[K] N) :
    ∃ (l : ℕ) (m : Fin l → M) (n : Fin l → N),
      LinearIndependent K m ∧ LinearIndependent K n ∧ x = ∑ i, m i ⊗ₜ n i
```

Cost of restatement: MODERATE. A new 30–60 line proof is needed, either by the minimal-length argument or by a basis of the span of the right factors followed by a basis of the left coefficients. Reconnecting the project statement then needs the iso `K[x_τ, y] ≅ K[y] ⊗ K[x_τ]` (`polyEquivTensor`, `scalarRTensorAlgEquiv`/`algebraTensorAlgEquiv`, `optionEquivLeft`) plus the degree bounds, which is extra transport work.

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|----------|----------|------------------------|---------------------------------|
|  1 | Preambles as typeclasses? | no | Nothing is bundled. Hypotheses are a nonzero condition and a degree bound. | n/a |
|  2 | Sequences/metric vs filters? | no | Pure algebra, no topology. | n/a |
|  3 | Construction vs universal property? | no | An existence statement. Nothing to characterise. | n/a |
|  4 | Set-with-predicate vs bundled substructure? | no | The proof already uses bundled `Submodule.span`. | n/a |
|  5 | Field-specific vs weaker typeclasses? | no | A field is genuinely needed (row 1 above). | n/a |
|  6 | Higher-categorical generalisation? | no | Not categorical. | n/a |
|  7 | Concrete index generalisable? | no | The `Fin l` indexing is natural. `ℕ`-degrees are intrinsic to polynomials. | n/a |
|  8 | Concrete-via-abstract (proof uses only abstract properties)? | yes | Diagnostic: after the first step (`eq_sum_X_none_pow_mul_coeffNone`), the proof never uses polynomial multiplication or evaluation except to re-express `∑ y^ν c_ν` (in the helper `eq_sum_aeval_basis_coeffNone_aux`). The core (`exists_coeffNone_basis_aux`, `linearIndependent_coordinate_polynomials_aux`) is "basis of span of the right factors, then coordinates on the left". That is the abstract tensor statement above, with the polynomial result a corollary via `K[x_τ, y] ≅ K[y] ⊗ K[x_τ]`. | Complements `TensorProduct.exists_sum_tmul_eq` (Finiteness.lean:182), `LinearIndependent.tmul_of_flat_left` / `LinearIndepOn.tmul_of_isDomain` (the converse direction), and tensor-rank / `Module.rank` of slices. |
|  9 | False-generalisation guard | no false generalisation | Under `K[x_τ, y] ≅ K[y] ⊗_K K[x_τ]` the tensor statement says exactly the same thing (`φ_ν ⊗ ψ_ν ↦ φ_ν(y)ψ_ν(x_τ)`). The degree bounds are an extra layer on top. | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `TensorProduct.exists_sum_tmul_eq_of_linearIndependent` (signature above), optionally with a refinement `x ∈ range (N₀.subtype.lTensor M)` with `N₀` finite-dimensional gives `l ≤ finrank K N₀`.
  - Cost: MODERATE
  - Mathlib downstream this enables: it sits next to `TensorProduct.exists_sum_tmul_eq` (which has no independence and whose docstring discourages its use), as the field-specific strengthening. It is the existence half of tensor rank, whose converse half already exists as `LinearIndependent.tmul_of_flat_left`. Any "separation of variables" argument for `MvPolynomial (σ ⊕ τ) K` or `A ⊗ B` (Roth, Wronskian-type, Schmidt decomposition) could use it.
  - Real mathematical improvement: the polynomial lemma is a disguised special case of a basic structure theorem for `V ⊗ W` over a field, which mathlib lacks.

### Proof strategy — `Roth.exists_separated_representation`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|-----------------------|----------------|
| 1 | ε-δ vs filters? | no | n/a | n/a |
| 2 | Elements vs submodule inclusions? | partially | The proof is already point-free where it matters (`Submodule.span_le`, `restrictSupport`, `LinearMap.ext_on`). | n/a |
| 3 | Sequences vs nets? | no | n/a | n/a |
| 4 | Construction vs universal property? | no | n/a | n/a |
| 5 | Helper lemmas mathlib should have? | yes | (a) `TensorProduct.exists_sum_tmul_eq_of_linearIndependent` (the abstract lemma). (b) `degreeOf_coeff_optionEquivLeft` (already flagged in the `Roth.coeffNone` report as the `optionEquivLeft` twin of `degreeOf_coeff_finSuccEquiv`). With (a) and the iso, the private helpers `linearIndependent_coordinate_polynomials_aux` and `eq_sum_aeval_basis_coeffNone_aux` would become transport. | MODERATE (file follow-up PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the polynomial-specific form; basis-of-span is the standard constructive route)
  - The note on row 5 stands: the shortest path modulo what mathlib should have goes through the abstract tensor lemma. That is the BORDERLINE question below, not a required refactor of this proof.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_separated_representation`

[A] Lean-Finder       "every element of a tensor product of vector spaces is a finite sum of pure tensors x_i ⊗ y_i with both families linearly independent" → `TensorProduct.exists_finset`, `exists_finsupp_left/right`, `exists_multiset`, `exists_eq_tmul_of_forall`, `sum_tmul_basis_left/right_eq_zero`, `LinearIndepOn.tmul_of_isDomain`. None has independence of both factor families in an existence statement.
[B] Loogle            `TensorProduct.tmul, LinearIndependent, Finset.sum, ∃` → query syntax error (`∃` not accepted as a constant). Replaced by grep [D] over the TensorProduct directories for `LinearIndependent` together with `exists`/`∃`: no hits.
[C] LeanSearch        "tensor product element as sum of tmul with linearly independent left and right factors (tensor rank decomposition)" → `exists_multiset`, `exists_finset`, `exists_finsupp_left/right`, `LinearIndepOn.tmul_of_flat_left`, `LinearIndependent.tmul_of_flat_left` (converse direction), `sum_tmul_basis_right_eq_zero`. No existence-with-independence lemma.
[D] Grep mathlib src  `exists_separated_representation` (0 hits). `tensorRank`/`TensorRank`/`Schmidt` (only Gram–Schmidt hits). `exists.*linearIndependent.*tmul` (0 hits). The `LinearAlgebra/TensorProduct/Finiteness.lean` lemma list confirms `exists_sum_tmul_eq` (line 182) as the closest, with no independence. Isos: `MvPolynomial.optionEquivLeft` (Algebra/MvPolynomial/Equiv.lean:467), `MvPolynomial.sumAlgEquiv` (Equiv.lean:397), `polyEquivTensor` (RingTheory/PolynomialAlgebra.lean:168), `MvPolynomial.scalarRTensorAlgEquiv` / `algebraTensorAlgEquiv` (RingTheory/TensorProduct/MvPolynomial.lean:89/97).
[E] Name pattern      `exists_separated`, `exists_sum_tmul_eq`, `exists_finset` (TensorProduct): only the independence-free variants exist.

Searched for both:
  - the user's current form (polynomial separated representation): not present.
  - the literature-standard form (tensor decomposition with independent factors over a field): not present. Only `TensorProduct.exists_sum_tmul_eq` without independence.

Concluded: found building blocks (`TensorProduct.exists_sum_tmul_eq`, `Module.finBasis`, `MvPolynomial.optionEquivLeft`, `polyEquivTensor`, `scalarRTensorAlgEquiv`), but the composition is a real proof. Not in mathlib in either form (all 5 methods exhausted).

### Normal-form check — `Roth.exists_separated_representation`

Equivalent formalisms this statement could take: (i) the current polynomial form with `Polynomial.aeval (X none)` and `rename some`. (ii) The `optionEquivLeft` form, `optionEquivLeft P = ∑ ν, Polynomial.map C (φ ν) * Polynomial.C (ψ ν)`. (iii) The tensor form `x = ∑ m i ⊗ₜ n i` in `K[X] ⊗[K] MvPolynomial τ K`.
Does mathlib already have a canonical form for this idea? Partially. `TensorProduct.exists_sum_tmul_eq` uses the `∃ k (m : Fin k → M) (n : Fin k → N), x = ∑ j, m j ⊗ₜ n j` shape, so the canonical shape for a mathlib lemma is (iii) in that format.
Our statement is a polynomial specialisation in the same `Fin l`-indexed shape, so it is consistent with the canonical shape. An `↔` normal-form question does not arise (existence statement).
RHS convention respected? n/a (not an equation/iff lemma meant for rewriting).

### Syntactic generality — `Roth.exists_separated_representation`

Alternative restatements attempted (list):
- Drop `n`/`hn` and use `degreeOf none P` directly. This loses the caller's flexibility (the caller passes `r none`), so it was rejected.
- Drop the two degree-bound conclusions. The only caller discards them, which makes the statement and destructuring simpler, but it departs from the source's Lemma 2 setup.
- Tensor form (iii). More general, but the caller would then need transport through three isos.

Chosen restatement: current form (for the project).
Justification: The caller (`exists_rat_factors_det_hasseDeriv_aux`) consumes exactly the `aeval (X none) φ * rename some ψ` shape that `det_hasseDeriv_separated` pattern-matches on, so this shape is easiest to supply at the call site.

### Superfluous-argument audit — `Roth.exists_separated_representation`

| # | Argument / typeclass | Essentially used? | Notes |
|---|----------------------|-------------------|-------|
| 1 | `[Field K]` | yes | Basis of a subspace (`Module.finBasis`). |
| 2 | `hP : P ≠ 0` | yes | Only for the conclusion `1 ≤ l` (via `Module.finrank_pos_iff_exists_ne_zero`). |
| 3 | `hn : degreeOf none P ≤ n` | yes | Used for the expansion over `Fin (n+1)`, `l ≤ n+1` and `natDegree φ ≤ n`. |
| 4 | `[Fintype τ] [DecidableEq τ]` | no (already omitted) | Removed by `omit ... in`. |
| 5 | conclusion `∀ ν, (φ ν).natDegree ≤ n` | unused by the caller | Superfluous for the project, but source-faithful. |
| 6 | conclusion `∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P` | unused by the caller | Superfluous for the project. This is the only reason `exists_coeffNone_basis_aux` needs `restrictSupport`. |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (for the project). A mathlib version would be the tensor form.
Superfluous arguments: NONE among the hypotheses. 2 conclusions are unused by the only caller (optional to drop).

Overall: SHIP-AS-STATED (as a project lemma). A mathlib contribution would be the restated tensor lemma, not this statement.

### Call sites — `Roth.exists_separated_representation`

Internal use count: 0 outside the declaring file (1 in the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|------------------|----------------------------------|
| Roth/Separation.lean:521–523 (`exists_rat_factors_det_hasseDeriv_aux`, private) | `obtain ⟨l, hl1, hl2, φ, ψ, hφ, hψ, -, -, hPQ⟩ := exists_separated_representation (fun h ↦ hP (...)) hdeg` |
| Roth/Separation.lean:31 | module docstring mention only |

Inline-derivation grep (was the equivalent re-derived elsewhere without using it?):
  - (none). `grep -rn` over `Roth/` for `coeffNone`/`finBasis`/`LinearIndependent K φ` patterns finds no second construction of a separated representation.

### Composition check (Phase 6)

Can `Roth.exists_separated_representation` be derived from mathlib in ≤3 chained calls?

Attempt 1: `TensorProduct.exists_sum_tmul_eq` transported along `polyEquivTensor` / `scalarRTensorAlgEquiv` / `optionEquivLeft`.
  - Mathlib decls used: `TensorProduct.exists_sum_tmul_eq`, `polyEquivTensor`, `MvPolynomial.scalarRTensorAlgEquiv`, `MvPolynomial.optionEquivLeft`.
  - Result: fails.
  - Notes: `exists_sum_tmul_eq` gives no linear independence, which is the whole content. The transport alone is more than 3 calls.

Attempt 2: `Module.finBasis` of `span (range (coeffNone P))` plus `Module.Basis.sum_repr`.
  - Mathlib decls used: `Module.finBasis`, `Module.Basis.sum_repr`, `Module.Basis.linearIndependent`, `finrank_range_le_card`.
  - Result: partial.
  - Notes: This gives `ψ` and the identity, but the independence of the coordinate polynomials `φ` is a genuine argument (the private helper's 25-line proof via `LinearMap.ext_on`). Multiple `have`s with real reasoning count as a proof, not a composition.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_separated_representation`

Verdict: BORDERLINE-needs-human

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): standard. "Every tensor admits an independent representation" (arXiv:1010.2964), tensor/Schmidt rank, and in Roth the minimal-length separated representation (clean.tex:369–394, arXiv:2502.00731, Roth 1955).
- Generality analysis (Phase 4): MAXIMALLY GENERAL within its polynomial shape (no mechanical weakening; `[Field K]` is essential). Phase 4c Q8 fires: the real content is the abstract tensor lemma.
- Mathlib search (Phase 5): not in mathlib in either form. Closest is `TensorProduct.exists_sum_tmul_eq` (Mathlib/LinearAlgebra/TensorProduct/Finiteness.lean:182), which has no independence.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**
The polynomial statement is the separation step from Roth's Lemma 2. It is a disguised special case of a basic fact mathlib does not have: over a field, every `x ∈ M ⊗[K] N` is `∑_{i<l} m_i ⊗ₜ n_i` with both families linearly independent. The specific gap is the field-specific strengthening of `TensorProduct.exists_sum_tmul_eq`, whose docstring tells users to avoid it in favour of induction. Its converse (`LinearIndependent.tmul_of_flat_left`, `LinearIndepOn.tmul_of_isDomain`) is already in mathlib. Adding the polynomial-specific form as stated would be wrong for mathlib. Its `Option τ` / `aeval (X none)` / `rename some` shape, and the degree conclusions its own caller discards, are tailored to Roth's argument. So `YES-add-as-is` does not fit.

`YES-but-generalise-first` would point at the tensor lemma. That is false-positive class 5 of the verdict gate: the abstract lemma is a new statement with a new (MODERATE, 30–60 line) proof, not a single mechanical weakening, and no weakening of the current statement compiles to it. Whether to invest in that upstream contribution, and whether to then re-derive this project lemma from it, is a project-policy and taste call, so the verdict is BORDERLINE. The cost is recorded but is not the reason for the bucket: the bucket follows from "restatement, not mechanical weakening".

Numbered questions:
1. Do you want to upstream the abstract lemma `TensorProduct.exists_sum_tmul_eq_of_linearIndependent` (over a field `K`, for any `x : M ⊗[K] N`) to Mathlib/LinearAlgebra/TensorProduct/Finiteness.lean next to `exists_sum_tmul_eq`? If yes, the follow-up is `/develop` for that lemma (proof by basis of the span of the right factors, then coordinates, mirroring `exists_coeffNone_basis_aux` + `linearIndependent_coordinate_polynomials_aux`).
2. Should the upstream version also include the bound refinement (`x ∈ M ⊗ N₀` with `N₀` finite-dimensional gives `l ≤ finrank K N₀`, with the `n_i ∈ N₀`)? That bound is what gives `l ≤ n+1` and the degree control here.
3. If question 1 is answered yes, should `Roth.exists_separated_representation` then be re-proved from it via `polyEquivTensor` + `scalarRTensorAlgEquiv` + `optionEquivLeft`? Or kept as is, given that the transport plus the degree bounds may not be shorter than the current 15 lines plus three private helpers?
4. Should the two degree-bound conclusions (`natDegree φ ν ≤ n`, `degreeOf j (ψ ν) ≤ degreeOf (some j) P`) be dropped? They are unused by the only caller, `exists_rat_factors_det_hasseDeriv_aux` (Separation.lean:521). Dropping the second also removes the `restrictSupport` part of `exists_coeffNone_basis_aux`. Or should they be kept for fidelity to the source's Lemma 2 setup?

Next action: the user answers the questions. Either way, keep `Roth.exists_separated_representation` in Roth/Separation.lean (its single call site at line 521 is unaffected unless question 4 is answered yes, in which case update the `obtain` pattern there by removing the two `-` placeholders).

---

### Next step

Decide question 1, whether to upstream `TensorProduct.exists_sum_tmul_eq_of_linearIndependent` (Mathlib/LinearAlgebra/TensorProduct/Finiteness.lean). No mathlib PR for the polynomial-specific form. Keep it locally, optionally dropping its two unused degree conclusions (call site Separation.lean:521).

## Evidence
- Source read: Roth/Separation.lean:230–345 (the theorem and its three private helpers) and 505–560 (caller `exists_rat_factors_det_hasseDeriv_aux` and `exists_det_eq_mul`). Source notes: `.mathlib-quality/references/clean.tex` lines 365–400 and 428.
- Project grep: `grep -rn exists_separated_representation Roth/ Roth.lean` gives the definition (325), the docstring (31) and one use (522).
- Mathlib grep: no `exists_separated_representation`, no tensor-rank/`Schmidt` lemma, no `exists ... linearIndependent ... tmul`. Read `TensorProduct.exists_sum_tmul_eq` (Finiteness.lean:182) and located the isos `optionEquivLeft` (Equiv.lean:467), `sumAlgEquiv` (Equiv.lean:397), `polyEquivTensor` (PolynomialAlgebra.lean:168), `scalarRTensorAlgEquiv`/`algebraTensorAlgEquiv` (RingTheory/TensorProduct/MvPolynomial.lean:89/97).
- Lean-Finder and LeanSearch: 1 query each (results in Phase 5). Loogle: 1 query, which failed on syntax and was replaced by grep.
- WebSearch: 4 queries (Phase 3 rows 1–4).
- ChatGPT MCP: n/a (not configured in this session).
- No Lean evidence file. No weakening or composition is claimed, so nothing needed compiling. The `[Field K]` necessity argument is mathematical (basis existence, plus `MvPolynomial` needs commutativity).
