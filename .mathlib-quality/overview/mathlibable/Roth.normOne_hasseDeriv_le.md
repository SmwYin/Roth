---
decl: Roth.normOne_hasseDeriv_le
file: Roth/CoeffNorm.lean
line: 148
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The l1 (length) bound for Hasse derivatives L(Delta_d P) ≤ 2^deg L(P) is the standard Roth-type estimate and absent from mathlib (no l1 norm on polynomials, no MvPolynomial Hasse derivative, no size bound even univariately); the Z/abs box form generalises verbatim to l1Norm over any SeminormedCommRing and to a box-free 2^totalDegree form without Fintype, both compiled with the project statement recovered.
action: Ship MvPolynomial.l1Norm_hasseDeriv_le_two_pow_totalDegree (plus the degreeOf-box corollary) over [SeminormedCommRing R] in the MvPolynomial.l1Norm / hasseDeriv PR (Mathlib/Analysis/Polynomial/Norm.lean companion or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the Z form for the single call site Roth/CoeffNorm.lean:269 (abs_coeff_det_hasseDeriv_le) via Int.norm_eq_abs.
---

# Roth.normOne_hasseDeriv_le

## Inventory entry

### `theorem Roth.normOne_hasseDeriv_le`
- **Type**: `{σ : Type*} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P`
- **What**: If `deg_{X_j} P ≤ r_j` for all `j`, every Hasse derivative `Δ_d P` of the integer polynomial `P` has ℓ¹ coefficient norm at most `2^{r_1+⋯+r_m} ‖P‖₁`.
- **How**: Expand `Δ_d P` with `MvPolynomial.hasseDeriv_apply` as `∑_{k ∈ supp P} monomial (k-d) (hasseCoeff d k · a_k)`, apply `Roth.normOne_sum_le`, unfold `normOne P` and distribute with `Finset.mul_sum`, compare termwise via `Roth.normOne_monomial`, `abs_mul`, `Nat.abs_cast`, and bound the binomial factor by `MvPolynomial.hasseCoeff_le_two_pow` (box hypothesis from `monomial_le_degreeOf` + `hP`).
- **Hypotheses**: `[Fintype σ]` (to form `∑ j, r j`), `hP` (partial degree box).
- **Uses from project**: `Roth.normOne`, `Roth.normOne_sum_le`, `Roth.normOne_monomial`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_apply`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`
- **Used by**: Roth/CoeffNorm.lean:269 (proof of `Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3). No other use (`grep -rn normOne_hasseDeriv_le Roth/`; line 29 is the module docstring).
- **Visibility**: public
- **Lines**: 145–157, proof length 8 lines
- **Notes**: Source clean.tex:450–461 (§3 proof of Lemma 3, "An individual Hasse derivative of such a term is zero or a monomial whose coefficient has absolute value at most B2^S"). ℓ¹ sibling of `Roth.abs_coeff_hasseDeriv_le` (line 134).

## Junk check (Step 8)
- Used anywhere? Yes: once, in Lemma 3 (`abs_coeff_det_hasseDeriv_le`, CoeffNorm.lean:269), a main result.
- Wrapper of 1–2 mathlib calls? No: 8-line proof combining project lemmas (`hasseDeriv_apply`, `normOne_sum_le`, `normOne_monomial`, `hasseCoeff_le_two_pow`).
- Does mathlib have it? No (mathlib has no ℓ¹ norm on (Mv)Polynomial and no Hasse-derivative size bound; Phase 5).
- Too specific (inline)? Single use, but it is the natural named estimate of the ℓ¹ API and keeps the Lemma 3 calc readable; inlining would bury it.
- Well-chosen? Yes for the project; for mathlib the normed, box-free form is better (Phase 4).
- Conclusion: `KEEP` — action: keep; upstream the generalised form with the `l1Norm` / `hasseDeriv` PRs.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_hasseDeriv_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (genuine 8-line proof). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` compiles with no errors or warnings)
- decl `Roth.normOne_hasseDeriv_le`: resolved at Roth/CoeffNorm.lean:148
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_hasseDeriv_le` is a theorem stating the following: let `P = ∑_k a_k X^k ∈ ℤ[X_1,…,X_m]` have degree at most `r_j` in `X_j`, and write `‖P‖₁ = ∑_k |a_k|` (the *length* of `P`). Then for every multi-index `d`, the Hasse derivative `Δ_d P = ∑_k binom(k,d) a_k X^{k-d}` satisfies `‖Δ_d P‖₁ ≤ 2^{r_1+⋯+r_m} ‖P‖₁`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]` — the finite set of variables.
- `d : σ →₀ ℕ` — order of the Hasse derivative.
- `P : MvPolynomial σ ℤ` — the polynomial.
- `r : σ → ℕ` — partial degree bounds.

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — partial degree box.

Conclusion (math): `L(Δ_d P) ≤ 2^{∑ r_j} L(P)`.

Conclusion (Lean): `normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: helper size estimate feeding Lemma 3 (not listed as a main result, not named, no new structure).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 8
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of polynomial L(P) sum of absolute values coefficients derivative bound L(P^(k)/k!) ≤ 2^deg L(P) | partial | `L(P)` = length (Landau–Mignotte literature, arXiv 1911.00480); the derivative bound follows from `[x^j]P^{(k)}/k! = binom(j,k) a_j`, `binom(j,k) ≤ 2^j` | no standalone citation; treated as immediate |
| 2 | WebSearch (named-after / Roth context) | Roth's theorem auxiliary polynomial index derivative 2^{r_1+…} coefficients bound | yes | Roth–Ridout (arXiv math/0307203): derived polynomials have coefficients `≤ 2^{r_1+⋯+r_m} B_1` | sup-norm version; ℓ¹ version is the same termwise argument |
| 3 | WebSearch (general form) | Hasse derivative divided derivative l1 norm polynomial inequality multivariate binomial | partial | multivariate Hasse derivative = coefficient of `Y^β` in `P(X+Y)`, multi-index binomial `∏ binom(α_i,β_i)` (multiplicity-code papers, Wikipedia "Hasse derivative") | no norm estimates stated; algebraic definitions only |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 447–499 | yes | `‖·‖₁` triangle inequality, monomial multiplicativity, and "Hasse derivative of such a term is zero or a monomial whose coefficient has absolute value at most B2^S" | source of the project statement (Lemma 3 proof and its Lean note) |
| 6 | nLab | Hasse derivative / Hasse–Schmidt derivation | partial | algebraic Hasse–Schmidt derivations; no norm estimates | algebraic only |
| 7 | nCatLab | — | n/a | — | not a categorical statement (archimedean coefficient inequality) |
| 8 | Stacks Project | — | n/a | — | differential operators treated algebraically; no coefficient size bounds |
| 9 | MathOverflow / Math.SE | length of derivative of polynomial / height of Hasse derivative | partial | folklore `L(Δ_d P) ≤ 2^{deg P} L(P)` used without proof | no competing form |
| 10 | recent arXiv (last 5 years) | subspace theorem survey (arXiv 2502.00731), effective Roth constants | yes | same `2^{∑ r_j}` factor in auxiliary-polynomial estimates | no generalisation beyond the termwise bound |

### Literature summary (Phase 3)

Concept identified as: length (ℓ¹ coefficient norm) bound for Hasse/divided derivatives, `L(Δ_d P) ≤ 2^{deg P} L(P)`; with partial-degree box `r`, factor `2^{r_1+⋯+r_m}`.
Sources agree on the standard form: yes — all derive it termwise from `[X^{k-d}] Δ_d (a_k X^k) = binom(k,d) a_k` and `binom(k,d) ≤ 2^{|k|}`.
Most general standard form: for `P` over any normed coefficient ring, `‖Δ_d P‖₁ ≤ ∑_k binom(k,d) ‖a_k‖ ≤ 2^{totalDeg P} ‖P‖₁`; the box form is a corollary since `totalDeg P ≤ ∑ r_j`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / number fields / any normed ring — only `‖n • a‖ ≤ n‖a‖` is used.
  - exponent: total degree vs. sum of partial degree bounds `∑ r_j` (the latter is weaker).
  - norm: ℓ¹ (this decl) vs. sup (sibling `abs_coeff_hasseDeriv_le`).
Disagreement with the literature: none in content; the project fixes ℤ and the box shape needed by Lemma 3.

### Generality analysis — `Roth.normOne_hasseDeriv_le`

Literature-standard form (from Phase 3): `l1Norm (hasseDeriv d P) ≤ 2 ^ P.totalDegree * l1Norm P` for `P : MvPolynomial σ R`, `[SeminormedCommRing R]`, any `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ`, `normOne` via `|(· : ℝ)|` | `[SeminormedCommRing R]`, `l1Norm` via `‖·‖` | yes | proof uses only `norm_nsmul_le` and the `l1Norm` triangle/monomial lemmas; verified (`Evidence89.l1Norm_hasseDeriv_le`) |
| 2 | `[Fintype σ]` | required | not needed | yes | only used to form `∑ j, r j`; box-free form uses `P.totalDegree`; verified (`Evidence89.l1Norm_hasseDeriv_le_two_pow_totalDegree`) |
| 3 | `hP` (degree box `r`) | required | not needed | yes | only bounds `|k|` on the support; `le_totalDegree` does it without `r`; box form becomes a corollary |
| 4 | `d` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (ℤ → `[SeminormedCommRing R]`; drop `Fintype σ` and `hP` via `totalDegree`)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_hasseDeriv_le/general_and_composition.lean` — shared core `l1Norm_hasseDeriv_le_of_forall` (binomial factors `≤ C` on the support ⇒ `l1Norm` grows by `≤ C`); (1) box form `l1Norm_hasseDeriv_le` over `[SeminormedCommRing R]`; (2) box-free `l1Norm_hasseDeriv_le_two_pow_totalDegree` (no `Fintype`, no `r`); (3) recovery `example` of the exact project statement via `Int.norm_eq_abs`. `lake env lean`: no errors, no warnings (two earlier runs failed only on the `Finsupp.degree` ↔ `totalDegree` bridge, fixed with `Finsupp.degree_apply`).
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_hasseDeriv_le {σ R : Type*} [SeminormedCommRing R]
    (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    l1Norm (hasseDeriv d P) ≤ 2 ^ P.totalDegree * l1Norm P

theorem MvPolynomial.l1Norm_hasseDeriv_le_of_degreeOf_le {σ R : Type*}
    [SeminormedCommRing R] [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) :
    l1Norm (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * l1Norm P
```

Cost of restatement: CHEAP — 3–6 line proofs, compiled.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | the degree box is a genuine data bound | — |
| 2 | Sequences → filters? | no | finite algebraic inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ/`|·|` → `[SeminormedCommRing R]`/`‖·‖` (with the parent `l1Norm` restatement) | estimates over ℝ, ℂ, ℚ_p, number-field completions |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general? | no | `σ →₀ ℕ` is the exponent monoid; univariate companion via `Polynomial.hasseDeriv_coeff` | — |
| 8 | Concrete-via-abstract? | yes | after `hasseDeriv_apply` the proof uses only the ℓ¹ triangle inequality, `‖n • a‖ ≤ n‖a‖` and the binomial bound; ℤ never matters | covered by row 5 |
| 9 | False-generalisation guard | no | for `R = ℤ`, `l1Norm = Roth.normOne` (`Int.norm_eq_abs`) and the box form is literally the project statement (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_hasseDeriv_le` (box-free, normed) with the `degreeOf`-box corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: ℓ¹ estimates for Hasse derivatives over any seminormed commutative ring; composes with the proposed `MvPolynomial.l1Norm` API (`l1Norm_mul_le`, `l1Norm_sum_le`, determinant bound) and with the pointwise sibling `norm_coeff_hasseDeriv_le`.
  - Real mathematical improvement: one estimate for every coefficient ring, free of the project's auxiliary box parameters.

### Proof strategy — `Roth.normOne_hasseDeriv_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | a coefficient inequality is inherently termwise | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | yes | `MvPolynomial.l1Norm` + `l1Norm_sum_le`/`l1Norm_monomial` (parent PR), `hasseDeriv_apply` (hasseDeriv PR), multi-index `choose_le_two_pow_degree` | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Expand as a sum of monomials + triangle inequality + binomial bound. Factoring through the evidence's `l1Norm_hasseDeriv_le_of_forall` lets both the box and the totalDegree forms be one-liners; `norm_nsmul_le` replaces the `Int.cast`/`abs_mul` bookkeeping.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_hasseDeriv_le`

[A] Lean-Finder       "l1 norm (length) of a polynomial: sum of absolute values of coefficients, bound for derivatives"  no hits (only `cauchyBound`, `mahlerMeasure_le_sum_norm_coeff`, `norm_coeff_le_choose_mul_mahlerMeasure`, `le_gaussNorm`)
[B] Loogle            `Polynomial.hasseDeriv, Norm.norm`  no hits
[C] LeanSearch        "sum of norms of coefficients of Hasse derivative of polynomial bounded by 2^degree times sum of norms"  no hits (`Polynomial.hasseDeriv`, `LaurentSeries.hasseDeriv`, Mahler-measure and Chebyshev bounds — unrelated)
[D] Grep mathlib src  `hasseDeriv` (only Algebra/Polynomial/HasseDeriv.lean, Taylor.lean, RingTheory/LaurentSeries.lean — none with norms); `l1Norm`/`normOne` as polynomial norm (none; only `NormOneClass`); `namespace Roth` (none); Analysis/Polynomial/Norm.lean lists the ℓ¹ norm / length only as a TODO-style remark  no hits
[E] Name pattern      `l1Norm_hasseDeriv`, `normOne_hasseDeriv`, `hasseDeriv_..._le` (grep / lean_local_search)  no hits

Searched for both:
  - the user's current form (ℤ, box, `normOne`)
  - the literature-standard form (normed `l1Norm`, `2^totalDegree`, multivariate and univariate)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks `Nat.choose_le_two_pow`, `norm_nsmul_le`, `Polynomial.hasseDeriv_coeff` (univariate only), `MvPolynomial.le_totalDegree`.

### Normal-form check — `Roth.normOne_hasseDeriv_le`

Equivalent formalisms: `l1Norm (Δ_d P) ≤ 2^{totalDeg P} l1Norm P`; box form `≤ 2^{∑ r_j} l1Norm P`; sharp form `l1Norm (Δ_d P) ≤ ∑_k binom(k,d) ‖a_k‖`.
Does mathlib already have a canonical form? No (no ℓ¹ norm on polynomials). Proposed canonical form: the `totalDegree` statement, shaped like `Polynomial.natDegree_hasseDeriv_le` (operator on the left, bound on the right). RHS convention: n/a (inequality).

### Syntactic generality — `Roth.normOne_hasseDeriv_le`

Alternative restatements attempted:
- box-free `l1Norm (hasseDeriv d P) ≤ 2 ^ P.totalDegree * l1Norm P` (compiled)
- box form with `r` over `[SeminormedCommRing R]` (compiled; the call-site shape)
- general core `(∀ k ∈ P.support, hasseCoeff d k ≤ C) → l1Norm (hasseDeriv d P) ≤ C * l1Norm P` (compiled)
Chosen restatement: the `totalDegree` form as the main lemma plus the box corollary. Justification: the main lemma is hypothesis-free; Lemma 3's call site carries `hP` and multiplies with `2 ^ (∑ j, r j)`, so the box corollary keeps it a one-term application.

### Superfluous-argument audit — `Roth.normOne_hasseDeriv_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | only for `∑ j, r j` | drop in the `totalDegree` form |
| 2 | `hP` | only to bound `|k|` on the support | drop in the `totalDegree` form |
| 3 | ℤ coefficients | no | `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (main lemma = box-free normed bound)
Syntactic generality: RESTATE (`totalDegree` form + box corollary)
Superfluous arguments: 3 to drop in the main lemma (ℤ specialisation, `Fintype σ`, `hP`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_hasseDeriv_le`

Internal use count: 0 (outside the declaring file); 1 inside the declaring file
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:269 | `(normOne_hasseDeriv_le _ P hP).trans (mul_le_mul_of_nonneg_left ...)` inside `normOne_det_le _ fun μ ν ↦ ...` (Lemma 3) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_hasseDeriv_le`?):
  - (none; the sup-norm sibling `Roth.abs_coeff_hasseDeriv_le` re-uses `hasseCoeff_le_two_pow` for the pointwise bound, which is a different statement).

K = 1 leans toward inlining in the Phase 6.0.1 table, but the lemma is the natural ℓ¹ analogue of the sup bound and is part of the coherent `l1Norm` API proposed by the parent `Roth.normOne` report; mathlib consumers of an `l1Norm` API would need it, so the low local count reflects the project's single Lemma-3 use, not a wrong abstraction.

### Composition check (Phase 6)

Can `Roth.normOne_hasseDeriv_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: via a mathlib Hasse-derivative ℓ¹ bound
  - Mathlib decls used: none available
  - Result: fails — mathlib has no `MvPolynomial.hasseDeriv`, no ℓ¹ norm on polynomials, and no size bound even for `Polynomial.hasseDeriv`.
Attempt 2: `hasseDeriv_apply` + `l1Norm_sum_le` + termwise `norm_nsmul_le`/`choose_le_two_pow`
  - Mathlib decls used: `norm_nsmul_le`, `Nat.choose_le_two_pow`, `Finset.mul_sum`, `Finset.sum_le_sum`
  - Result: partial — `hasseDeriv_apply`, `l1Norm` and its triangle/monomial lemmas are project lemmas, and the termwise comparison is a 6-line proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.normOne_hasseDeriv_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard auxiliary-polynomial estimate (clean.tex:450–461; Roth–Ridout arXiv math/0307203 for the sup version; length `L(P)` literature), always derived termwise from `binom(k,d) ≤ 2^{|k|}`.
- Generality analysis (Phase 4): STRICTLY NARROWER; box form over `[SeminormedCommRing R]` and box-free `2^totalDegree` form (no `Fintype`, no `r`) compiled, with the ℤ statement recovered.
- Mathlib search (Phase 5): not in mathlib; no ℓ¹ polynomial norm, no multivariate Hasse derivative, no Hasse-derivative size bound.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's `Mathlib/Analysis/Polynomial/Norm.lean` defines only the sup norm and remarks that the ℓ¹ norm ("length") is missing; the parent `Roth.normOne` report (YES-but-generalise-first) proposes adding `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`, and `MvPolynomial.hasseDeriv` is likewise proposed for upstreaming. The bound `L(Δ_d P) ≤ 2^{deg P} L(P)` is the basic interaction between these two additions and is the estimate consumed by every auxiliary-polynomial argument that controls Wronskian/determinant sizes (Roth's Lemma 3 here); mathlib currently cannot state it at all.

The project form is a specialisation: ℤ with `|·|`, finite `σ`, and a partial-degree box. The evidence file proves the statement over any seminormed commutative ring (only `norm_nsmul_le` is needed, no `NormOneClass`), and a box-free version with `2 ^ P.totalDegree`, which implies the box form because `totalDegree P ≤ ∑ r_j`. Both factor through a two-line core lemma. The box form should ship as a corollary because that is the shape Lemma 3 consumes.

Reason for the generalisation: LITERATURE-WEAKENING (box-free `totalDegree` form, no `Fintype`) and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy, following the parent `l1Norm` restatement).

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_hasseDeriv_le {σ R : Type*} [SeminormedCommRing R]
    (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    l1Norm (hasseDeriv d P) ≤ 2 ^ P.totalDegree * l1Norm P := by
  sorry  -- proof in evidence file

theorem MvPolynomial.l1Norm_hasseDeriv_le_of_degreeOf_le {σ R : Type*}
    [SeminormedCommRing R] [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) :
    l1Norm (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * l1Norm P := by
  sorry  -- proof in evidence file
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- ℓ¹ size estimates for Hasse derivatives over ℝ, ℂ, ℚ_p and number-field completions (Thue–Siegel–Roth, Schmidt, Siegel-lemma arguments);
- composes with `l1Norm_mul_le` / `l1Norm_sum_le` / the determinant bound to give Wronskian-size bounds (Lemma 3 pattern) in general;
- a univariate `Polynomial.l1Norm_hasseDeriv_le` next to `Polynomial.supNorm` using `Polynomial.hasseDeriv_coeff`.

PR grouping: ship in the `MvPolynomial.l1Norm` PR (with `l1Norm_sum_le`, `l1Norm_monomial`, `l1Norm_mul_le`, `l1Norm_det_le`) after `MvPolynomial.hasseDeriv` / `hasseDeriv_apply` and the multi-index `choose_le_two_pow_degree` land; pairs with the pointwise sibling `norm_coeff_hasseDeriv_le` (from `Roth.abs_coeff_hasseDeriv_le`).

Next action: run `/generalise Roth.normOne_hasseDeriv_le`, restate as `MvPolynomial.l1Norm_hasseDeriv_le` (+ box corollary) over `[SeminormedCommRing R]`, and keep the ℤ form at Roth/CoeffNorm.lean:269 via `Int.norm_eq_abs`.

---

## Next step

Upstream `MvPolynomial.l1Norm_hasseDeriv_le` (box-free, `2 ^ totalDegree`) and `l1Norm_hasseDeriv_le_of_degreeOf_le` over `[SeminormedCommRing R]` in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean companion or new Mathlib/Analysis/MvPolynomial/Norm.lean), after the `MvPolynomial.hasseDeriv` PR; locally keep the ℤ statement for Roth/CoeffNorm.lean:269.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_hasseDeriv_le/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): `l1Norm` API over `[SeminormedCommRing R]`; core `l1Norm_hasseDeriv_le_of_forall`; box form `l1Norm_hasseDeriv_le`; `hasseCoeff_le_two_pow_degree`; box-free `l1Norm_hasseDeriv_le_two_pow_totalDegree`; recovery `example` of the exact project statement. `lake env lean`: clean (no errors, no warnings) on the third run; the first two failed only on the `Finsupp.degree`/`totalDegree` bridge.
- Mathlib greps: `hasseDeriv` files (Algebra/Polynomial/HasseDeriv.lean, Taylor.lean, RingTheory/LaurentSeries.lean; no norms), `l1Norm`/`normOne` (none as polynomial norm), `namespace Roth` (none), Analysis/Polynomial/Norm.lean ℓ¹ remark.
- Lean-Finder / LeanSearch / Loogle queries as in Phase 5 (no hit).
- WebSearch ×3 (length of derivative bound; Roth auxiliary-polynomial `2^{r_1+…}` bound; Hasse derivative ℓ¹ multivariate), local reference clean.tex:447–499 and :1445.
- ChatGPT MCP: n/a (not configured in this session).
