---
decl: Roth.genWronskian_eq_zero_of_not_linearIndependent
file: Roth/GenWronskian.lean
line: 41
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The easy direction of the generalized-Wronskian criterion (dependent multivariate polynomials have all generalized Wronskians zero; Roth 1955, Bostan-Dumas, source paper section 2) is absent from mathlib; [Field K] weakens to [CommRing R] [IsDomain R] with the proof verbatim (verified, IsDomain necessary by a ZMod 4 counterexample), and the proof is an instance of an abstract det-of-linear-maps lemma (verified) that also yields Roth.wronskian_eq_zero_of_not_linearIndependent.
action: Upstream with MvPolynomial.genWronskian (placeholder) over [CommRing R] [IsDomain R] in a new Mathlib/RingTheory/MvPolynomial/Wronskian.lean, preferably as a one-line corollary of the abstract lemma det_linearMap_eq_zero_of_not_linearIndependent (Mathlib/LinearAlgebra/Matrix/ToLinearEquiv.lean, next to Matrix.exists_mulVec_eq_zero_iff); locally keep (no project call sites; it is the source paper's second lemma of section 2).
---

# Roth.genWronskian_eq_zero_of_not_linearIndependent

## Inventory entry

### `theorem Roth.genWronskian_eq_zero_of_not_linearIndependent`
- **Type**: `{K : Type*} [Field K] {σ : Type*} {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ K} (h : ¬ LinearIndependent K φ) : genWronskian D φ = 0`
- **What**: If multivariate polynomials `φ_0, …, φ_{l-1}` over a field are `K`-linearly dependent, then every generalized Wronskian `det (Δ_{D μ} φ_ν)` vanishes, for any choice of Hasse multi-indices `D` (no order constraint).
- **How**: `Fintype.not_linearIndependent_iff` gives a nontrivial relation `∑ g ν • φ ν = 0`; the constant vector `C ∘ g` is a nonzero kernel vector of the matrix (apply the linear map `hasseDeriv (D μ)` to the relation, `map_smul`, `smul_eq_C_mul`), so `Matrix.exists_mulVec_eq_zero_iff` gives `det = 0`.
- **Hypotheses**: `[Field K]` (section variable); `[Fintype σ]` is omitted (`omit [Fintype σ] in`); `h : ¬ LinearIndependent K φ`.
- **Uses from project**: `Roth.genWronskian`, `MvPolynomial.hasseDeriv`
- **Used by**: unused in project (`grep -rn genWronskian_eq_zero_of_not_linearIndependent Roth/` returns only the declaration).
- **Visibility**: public
- **Lines**: 37–48, proof length 7 lines
- **Notes**: Same 6-line proof as `Roth.wronskian_eq_zero_of_not_linearIndependent` (Roth/Wronskian.lean:65); both are instances of one abstract lemma (compiled in evidence). It is the formalisation of the source's second lemma of §2 (clean.tex l.213) and the converse companion of `exists_genWronskian_ne_zero`.

## Junk check (Step 8)
- Used anywhere? No project call site. The main development only needs the hard direction `exists_genWronskian_ne_zero`.
- Wrapper of 1–2 mathlib calls? No: a 7-line proof combining `Fintype.not_linearIndependent_iff`, `Matrix.exists_mulVec_eq_zero_iff`, linearity of `hasseDeriv` and a `simpa` computation.
- Does mathlib have it? No. Mathlib has no generalized (or n-ary) Wronskian; the nearest results are `Matrix.det_eq_zero_of_not_linearIndependent_cols` (dependence over the matrix ring, not over constants) and `Algebra.discr_zero_of_not_linearIndependent` (a different determinant).
- Too specific (inline?)? No: it is a named statement of the source paper (§2, second lemma) and the char-free half of the generalized-Wronskian criterion.
- Well-chosen? Yes. Only `[Field K]` is stronger than needed.
- Conclusion: `KEEP`. Action: keep it as the source-faithful lemma and the natural API companion of `genWronskian`. Generalise to `[CommRing R] [IsDomain R]` when upstreaming. Optionally prove it and the univariate sibling from one abstract lemma.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring does not start internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `genWronskian` over `.lake/packages/mathlib/Mathlib/`: no hit). It is not a glue lemma (it has a real 7-line proof), so the full workflow is run. The parent def `Roth.genWronskian` is YES-but-generalise-first, and its evidence is reused.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.GenWronskian` elaborates clean in the LSP)
- decl `Roth.genWronskian_eq_zero_of_not_linearIndependent`: resolved at Roth/GenWronskian.lean:41
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians `det (Δ_{D μ} φ_ν)` of multivariate polynomials and Lemma 1 (an independent family has a nonvanishing generalized Wronskian), via Kronecker substitution.

### Statement (Phase 1)

`Roth.genWronskian_eq_zero_of_not_linearIndependent` is a theorem stating the following. Suppose polynomials `φ_0, …, φ_{l-1} ∈ K[x_j : j ∈ σ]` over a field `K` satisfy a nontrivial relation `c_0 φ_0 + ⋯ + c_{l-1} φ_{l-1} = 0` with constants `c_ν ∈ K`. Then for every choice of multi-indices `D_0, …, D_{l-1}`, the generalized Wronskian `det (Δ_{D_μ} φ_ν)_{μ,ν}` is the zero polynomial. Here `Δ_d` is the multivariate Hasse derivative. No characteristic assumption is needed, and the orders `|D_μ|` are unconstrained.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]`: the coefficient field.
- `σ`: the variable index type (no finiteness assumed).
- `l : ℕ`: the size of the family.
- `D : Fin l → σ →₀ ℕ`: the Hasse multi-indices, one per row.
- `φ : Fin l → MvPolynomial σ K`: the family.

Hypotheses (Lean side):
- `h : ¬ LinearIndependent K φ`: linear dependence over the constants.

Conclusion (math): `W(φ_0, …, φ_{l-1}; Δ_{D_0}, …, Δ_{D_{l-1}}) = 0`.

Conclusion (Lean): `Roth.genWronskian D φ = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is the easy companion of the file's main result `exists_genWronskian_ne_zero` (Lemma 1), not itself a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7 substantive lines
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | generalized Wronskian linearly dependent polynomials several variables vanishes identically Roth lemma | yes | if the functions are linearly dependent, all generalized Wronskians vanish; Roth: multivariate polynomials are dependent iff all generalized Wronskians vanish | Wikipedia "Wronskian"; Walker (LinDep, Penn State); Bostan–Dumas arXiv 1301.6598; Ball–Parks–Pong arXiv 1611.00248; Roth, Mathematika 1955 |
| 2 | WebSearch (general form) | determinant of linear operators applied to linearly dependent functions vanishes generalized Wronskian differential operators | yes | the dependent-implies-zero direction holds because each row operator is linear, so a constant relation among the functions is a relation among the columns; it holds for any linear operators | Wikipedia; arXiv 1310.4683 §2.4; arXiv 1609.06793 |
| 3 | WebSearch (named-after / aliases) | "generalized Wronskians" Ostrowski linear independence multivariate functions Hasse derivatives | yes | Ostrowski introduced generalized Wronskians, which Dyson and Roth then used; dependent families give all generalized Wronskians zero; the converse holds in char 0 for power series | Bostan–Dumas 1301.6598; arXiv 2502.00731 (subspace theorem survey); arXiv 2108.02993 (terminology caveat: "geometric" generalized Wronskians differ) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` l.210–216 | yes | "If φ_0, …, φ_{l-1} are polynomials over a characteristic-zero field and are linearly dependent over that field, then all of their generalized Wronskians are identically zero" | exact source statement; the source states it over a char-0 field, but its proof (a constant column relation) is char-free |
| 6 | nLab | Wronskian / generalized Wronskian | no | — | no nLab page (also checked for the parent `Roth.genWronskian`) |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not a scheme-theoretic statement; Wronskians there occur only for curves (Weierstrass points), not generalized multivariate Wronskians |
| 9 | MathOverflow / Math.SE | (covered by #1–#3) | partial | no dedicated thread; the statement is treated as folklore (one line in every source) | — |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2502.00731 (2025) recalls generalized Wronskians in the subspace-theorem context; arXiv 2511.03848 (Jacobi identities for multidimensional Wronskians) | confirms the easy direction is standard and char-free |

### Literature summary (Phase 3)

Concept identified as: the easy direction of the generalized (Ostrowski–Roth) Wronskian criterion for linear independence ("dependent families have all generalized Wronskians zero").
Sources agree on the standard form: yes. It is stated for multivariate polynomials, formal power series and analytic functions, always with dependence over the constants, and it never needs a characteristic hypothesis. The source paper adds "characteristic zero" only because its section works over ℚ.
Most general standard form: let `L_1, …, L_n` be maps from a module to a commutative domain `A` that are linear over the constant ring `R`, with `R` acting faithfully on `A`. If `f_1, …, f_n` satisfy a nontrivial `R`-linear relation, then `det (L_μ f_ν) = 0`.
Generality dimensions where the literature varies:
  - coefficients: from a field (or ℚ in the source) to an integral domain. A domain is needed so that a nonzero constant vector is a nonzero kernel vector.
  - operators: from constant-coefficient differential operators of bounded order, through Hasse derivatives, to arbitrary linear operators. Only linearity is used for this direction.
  - ambient object: polynomials, power series, analytic functions.
Disagreement with the literature: none. The user's form is char-free and constraint-free on `D`, which is already more general than the source statement.

### Generality analysis — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

Literature-standard form (from Phase 3): for `φ : Fin l → MvPolynomial σ R` over an integral domain `R` and any `D`, `¬ LinearIndependent R φ → genWronskian D φ = 0`; abstractly, `det (L μ (φ ν)) = 0` for `R`-linear `L μ` into a faithful `R`-algebra domain.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | integral domain | yes | proof uses only `Matrix.exists_mulVec_eq_zero_iff` (needs `MvPolynomial σ R` a domain) and injectivity of `C`; verified: the proof compiles verbatim over `[CommRing R] [IsDomain R]` (evidence item 1) |
| 2 | `[IsDomain R]` to plain `[CommRing R]` | — | — | NO | false: over `ZMod 4`, `![C 2]` is dependent but `genWronskian ![0] ![C 2] = C 2 ≠ 0` (verified, evidence item 2) |
| 3 | `[Fintype σ]` | already omitted | arbitrary variables | n/a | already maximal |
| 4 | `D` (orders) | arbitrary | arbitrary | n/a | no `|D μ| ≤ μ` constraint; already maximal |
| 5 | `hasseDeriv` (specific operators) | Hasse derivatives | any `R`-linear maps | yes (abstract form) | proof only uses `R`-linearity of `hasseDeriv (D μ)`; verified abstract lemma (evidence item 3), from which this theorem is a one-line corollary |
| 6 | `h` | dependence over constants | dependence over constants | no | the hypothesis itself |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 mechanical (`[Field K]` to `[CommRing R] [IsDomain R]`, verified clean via `lean_diagnostic_messages`; `IsDomain` shown necessary), plus 1 abstraction (Phase 4c row 8, verified).
Proposed restatement:

```lean
theorem MvPolynomial.genWronskian_eq_zero_of_not_linearIndependent {R σ : Type*} [CommRing R]
    [IsDomain R] {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ R}
    (h : ¬ LinearIndependent R φ) : genWronskian D φ = 0
```

Cost of restatement: CHEAP (the proof is unchanged).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled preamble |
| 2 | sequences to filters? | no | — | algebraic and finite |
| 3 | construction vs universal property? | no | — | a vanishing statement |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R] [IsDomain R]` (row 1 above) | generalized Wronskians over `ℤ` (the source works with integral polynomials); consistent with the `[CommRing R]` parent def |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | `Fin l` is inherited from the parent def (a square matrix) | — |
| 8 | concrete-via-abstract? | yes | the diagnostic fires: after `obtain`, the proof never mentions `genWronskian` or anything Hasse-specific except that `hasseDeriv (D μ)` is a linear map. Abstract lemma `det_linearMap_eq_zero_of_not_linearIndependent` (for `L : Fin l → M →ₗ[R] A`, `[IsDomain A] [Algebra R A] [FaithfulSMul R A]`) compiles, and both this theorem and `Roth.wronskian_eq_zero_of_not_linearIndependent` follow from it in one line (evidence item 3) | deduplicates the two project proofs; applies to any determinant of operators applied to a dependent family (ordinary derivations, `pderiv`, Casoratians with shift operators, generalized Wronskians of power series) |
| 9 | false-generalisation guard | no false generalisation | the `IsDomain` version is the same statement about the same object (the project theorem is a direct specialisation, verified); the abstract lemma specialises definitionally (verified) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the abstract lemma
    ```lean
    theorem Matrix.det_linearMap_eq_zero_of_not_linearIndependent {R M A : Type*} [CommRing R]
        [AddCommGroup M] [Module R M] [CommRing A] [IsDomain A] [Algebra R A] [FaithfulSMul R A]
        {l : ℕ} (L : Fin l → M →ₗ[R] A) {φ : Fin l → M} (h : ¬ LinearIndependent R φ) :
        (Matrix.of fun μ ν ↦ L μ (φ ν)).det = 0
    ```
    (placeholder name). The generalized-Wronskian statement over `[CommRing R] [IsDomain R]` then becomes its one-line corollary.
  - Cost: CHEAP (compiled, 6 lines).
  - Mathlib downstream this enables: the one-variable n-ary Wronskian vanishing (`Roth.wronskian_eq_zero_of_not_linearIndependent`), Wronskians for `Derivation`s and Casoratians all become one-liners, and a contrapositive `linearIndependent_of_det_linearMap_ne_zero` works for any operator family.
  - Real mathematical improvement: it isolates the actual content (constant relations become column relations under linear operators), replacing two copies of the same proof.

### Proof strategy — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the abstract det-of-linear-maps lemma (4c row 8) is the helper mathlib should have; with it, this proof is one line | CHEAP (file with the abstract lemma) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (mildly)
  - Proposed strategy: derive it from the abstract lemma `det_linearMap_eq_zero_of_not_linearIndependent`.
  - Cost: CHEAP
  - Missing mathlib API: that abstract lemma (natural home next to `Matrix.exists_mulVec_eq_zero_iff`).
  - Would refactoring make the proof strictly shorter / cleaner? yes (one line; deduplicates with Roth/Wronskian.lean:65)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.genWronskian_eq_zero_of_not_linearIndependent`

[A] Lean-Finder       "generalized Wronskian of linearly dependent multivariate polynomials vanishes"   only 2-ary `Polynomial.wronskian` API (`wronskian_self_eq_zero`, `isAlt_wronskianBilin`, `IsCoprime.wronskian_eq_zero_iff`, …); no multivariate or n-ary hit
[B] Loogle            `Matrix.det, LinearIndependent, MvPolynomial`   no hits
[C] LeanSearch        "determinant of matrix of linear maps applied to linearly dependent family is zero"   building blocks only: `Matrix.det_eq_zero_of_not_linearIndependent_cols` / `_rows` (dependence over the matrix ring), `Matrix.linearIndependent_cols_of_det_ne_zero`, `Algebra.discr_zero_of_not_linearIndependent` (trace-form determinant, different statement)
[D] Grep mathlib src  `genWronskian`, `generali[sz]ed ?wronskian`, `wronskian.*linearIndependent`, `linearIndependent.*wronsk` (case-insensitive): no hits; `exists_mulVec_eq_zero_iff` at Mathlib/LinearAlgebra/Matrix/ToLinearEquiv.lean:163; `det_eq_zero_of_not_linearIndependent_rows/cols` at Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:483/496
[E] Name pattern      `genWronskian_eq_zero_of_not_linearIndependent`, `MvPolynomial.genWronskian`, `det_linearMap_eq_zero_of_not_linearIndependent` (grep)   absent

Searched for both the user's form (field, Hasse derivatives) and the literature-standard and abstract forms (domain, arbitrary linear maps).

Concluded: found building blocks (`Fintype.not_linearIndependent_iff`, `Matrix.exists_mulVec_eq_zero_iff`, `Matrix.det_eq_zero_of_not_linearIndependent_cols`, `FaithfulSMul.algebraMap_injective`). Neither the statement nor its abstract form is in mathlib.

### Normal-form check — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

Equivalent formalisms: `¬ LinearIndependent R φ → genWronskian D φ = 0`; contrapositive `genWronskian D φ ≠ 0 → LinearIndependent R φ`; relation form `∑ g ν • φ ν = 0 → g ≠ 0 → genWronskian D φ = 0`.
Does mathlib already have a canonical form? For matrices, mathlib states the pair `det_eq_zero_of_not_linearIndependent_cols` / `linearIndependent_cols_of_det_ne_zero`, and we follow that pattern.
Proposed canonical form: keep the implication, and add the contrapositive `linearIndependent_of_genWronskian_ne_zero`.
RHS convention respected? yes (not an iff)

### Syntactic generality — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

Alternative restatements attempted:
- current: `¬ LinearIndependent R φ → genWronskian D φ = 0`
- contrapositive: `genWronskian D φ ≠ 0 → LinearIndependent R φ`
- abstract: `(Matrix.of fun μ ν ↦ L μ (φ ν)).det = 0` for linear maps `L`
Chosen restatement: the current form over a domain, derived from the abstract form, plus the contrapositive companion.
Justification: the current form matches the source and the univariate sibling; the contrapositive is how independence is proved in practice.

### Superfluous-argument audit — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R] [IsDomain R]` suffices (verified) |
| 2 | `[IsDomain R]` (after weakening) | yes | `ZMod 4` counterexample without it (verified) |
| 3 | `D` explicit | yes | appears in the conclusion; explicit is right (not inferable from `h`) |
| 4 | `h` | yes | the hypothesis |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (add the contrapositive companion when upstreaming)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[CommRing R] [IsDomain R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.genWronskian_eq_zero_of_not_linearIndependent`

Internal use count: 0 (outside the declaring file), and 0 inside it.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none) | `grep -rn genWronskian_eq_zero_of_not_linearIndependent Roth/` returns only the declaration at Roth/GenWronskian.lean:41 |

Inline-derivation grep: Roth/Wronskian.lean:65–71 (`wronskian_eq_zero_of_not_linearIndependent`) runs the identical argument for the univariate Wronskian (`Fintype.not_linearIndependent_iff` + `Matrix.exists_mulVec_eq_zero_iff` + linearity). It does not re-derive this statement, but it is the same proof, so there is an opportunity to deduplicate via the abstract lemma.

Signal: K = 0 with no re-derivation of this exact statement. This is not junk: it is a stated lemma of the source paper (§2, second lemma), kept for source-fidelity and as the converse half of the criterion whose hard half (`exists_genWronskian_ne_zero`) is used downstream.

### Composition check (Phase 6)

Can the statement be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_eq_zero_of_not_linearIndependent_cols (A := Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)) ?_`.
  - Mathlib decls used: `Matrix.det_eq_zero_of_not_linearIndependent_cols`
  - Result: partial. The remaining goal (the columns are `MvPolynomial σ R`-dependent) needs the relation to be transferred via `Fintype.not_linearIndependent_iff`, linearity and `smul_eq_C_mul`, which is a real proof of several lines.

Attempt 2: the current proof (`Fintype.not_linearIndependent_iff`, then `Matrix.exists_mulVec_eq_zero_iff`, then a `simpa` computation).
  - Result: works, but it is a proof with a nontrivial `simpa` step, not a call chain.

Conclusion: NOT-COMPOSABLE. (With the proposed abstract lemma in mathlib, it would be a 1-call corollary, and that is the recommended shape.)

## Verdict: `Roth.genWronskian_eq_zero_of_not_linearIndependent`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the easy direction of the Ostrowski–Roth generalized-Wronskian criterion is standard and char-free (Roth 1955; Walker; Bostan–Dumas arXiv 1301.6598; Ball–Parks–Pong arXiv 1611.00248; Wikipedia; source clean.tex l.213).
- Generality analysis (Phase 4): STRICTLY NARROWER. `[Field K]` weakens to `[CommRing R] [IsDomain R]` (verified), and `IsDomain` is necessary (verified). An abstract det-of-linear-maps form is also verified.
- Mathlib search (Phase 5): building blocks only. Mathlib has no generalized or n-ary Wronskian, and no abstract det-of-linear-maps vanishing lemma.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's Wronskian file (`Mathlib/RingTheory/Polynomial/Wronskian.lean`) has only the 2-ary Wronskian, with an n-ary TODO. It has nothing multivariate. The parent def `Roth.genWronskian` was assessed YES-but-generalise-first for upstreaming as `MvPolynomial.genWronskian`, and this lemma is the first basic fact one proves about it. It is the half of Roth's criterion that holds in every characteristic, and its contrapositive (a nonzero generalized Wronskian implies independence) is the usable form. Mathlib's `Matrix.det_eq_zero_of_not_linearIndependent_cols` does not give it, because it needs dependence over the polynomial ring rather than over the constants. Bridging the two is exactly the content of this lemma.

The proof never divides. The evidence file compiles the identical proof over `[CommRing R] [IsDomain R]`. It also shows the domain hypothesis is necessary: over `ZMod 4`, `![C 2]` is dependent, but its generalized Wronskian with `D = ![0]` is `C 2 ≠ 0`. Moreover, the Q8 diagnostic fires. The proof uses nothing about Hasse derivatives beyond linearity. The abstract lemma "det of `R`-linear maps applied to an `R`-dependent family into a faithful `R`-algebra domain is zero" compiles in 6 lines, and both this theorem and `Roth.wronskian_eq_zero_of_not_linearIndependent` follow from it in one line (verified).

Reason for the generalisation: LITERATURE-WEAKENING (field to integral domain) and MODERN-IDIOM (concrete-via-abstract: factor out the det-of-linear-maps lemma).
Proposed restatement:
```lean
theorem Matrix.det_linearMap_eq_zero_of_not_linearIndependent {R M A : Type*} [CommRing R]
    [AddCommGroup M] [Module R M] [CommRing A] [IsDomain A] [Algebra R A] [FaithfulSMul R A]
    {l : ℕ} (L : Fin l → M →ₗ[R] A) {φ : Fin l → M} (h : ¬ LinearIndependent R φ) :
    (Matrix.of fun μ ν ↦ L μ (φ ν)).det = 0 := by
  sorry -- 6-line proof verified in evidence
theorem MvPolynomial.genWronskian_eq_zero_of_not_linearIndependent {R σ : Type*} [CommRing R]
    [IsDomain R] {l : ℕ} (D : Fin l → σ →₀ ℕ) {φ : Fin l → MvPolynomial σ R}
    (h : ¬ LinearIndependent R φ) : genWronskian D φ = 0 :=
  Matrix.det_linearMap_eq_zero_of_not_linearIndependent (fun μ ↦ hasseDeriv (D μ)) h
theorem MvPolynomial.linearIndependent_of_genWronskian_ne_zero {R σ : Type*} [CommRing R]
    [IsDomain R] {l : ℕ} {D : Fin l → σ →₀ ℕ} {φ : Fin l → MvPolynomial σ R}
    (h : genWronskian D φ ≠ 0) : LinearIndependent R φ := by
  sorry -- contrapositive
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- a one-line vanishing for any determinant of operators applied to a dependent family: the n-ary univariate Wronskian (`Roth.wronskian_eq_zero_of_not_linearIndependent`), Wronskians for `Derivation`s, and Casoratians;
- proving linear independence over `ℤ` or any domain from one nonzero generalized Wronskian;
- the easy half of Roth's Lemma 1 iff (with `exists_genWronskian_ne_zero` as a follow-up PR).
PR grouping: the abstract lemma goes as its own small PR to `Mathlib/LinearAlgebra/Matrix/ToLinearEquiv.lean`, next to `Matrix.exists_mulVec_eq_zero_iff`. This lemma then ships with `MvPolynomial.hasseDeriv`, `Roth.genWronskian` and the univariate sibling `Roth.wronskian_eq_zero_of_not_linearIndependent`.
Next action: run `/generalise Roth.genWronskian_eq_zero_of_not_linearIndependent` (target `[CommRing R] [IsDomain R]`, via the abstract lemma). Then upstream it with the generalized-Wronskian PR, adding the contrapositive companion.

---

## Next step

Run `/generalise Roth.genWronskian_eq_zero_of_not_linearIndependent`, targeting `[CommRing R] [IsDomain R]` and deriving it from the abstract `det_linearMap_eq_zero_of_not_linearIndependent`. Then upstream it in the generalized-Wronskian PR (new `Mathlib/RingTheory/MvPolynomial/Wronskian.lean`), adding a `linearIndependent_of_genWronskian_ne_zero` companion.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.genWronskian_eq_zero_of_not_linearIndependent/weaken_and_abstract.lean`, checked with `lean_diagnostic_messages`: clean, no errors or warnings. The first check failed on two corollary `example`s, which needed the target ring `(A := …)` given explicitly; after that fix it was clean. It verifies:
  - (1) the theorem over `[CommRing R] [IsDomain R]`, with the project proof verbatim;
  - (2) the project theorem is a specialisation of it;
  - (3) over `ZMod 4`, `![C 2]` is not linearly independent, and `genWronskian ![0] ![C 2] ≠ 0`, so `IsDomain` is necessary;
  - (4) the abstract lemma `det_linearMap_eq_zero_of_not_linearIndependent` holds, and both the domain version of this theorem and `Roth.wronskian_eq_zero_of_not_linearIndependent` are one-line corollaries of it.
- WebSearch: 3 queries, summarised in the literature table. ChatGPT MCP: n/a (not configured in this session).
- LeanSearch, Lean-Finder and Loogle queries and the mathlib greps are recorded in Phase 5.
- Project greps: `grep -rn genWronskian_eq_zero_of_not_linearIndependent Roth/` found the declaration only. `grep -rn "not_linearIndependent_iff\|exists_mulVec_eq_zero_iff" Roth/` found the parallel proof at Roth/Wronskian.lean:67–68.
- Local references: `.mathlib-quality/references/clean.tex` l.210–216.
