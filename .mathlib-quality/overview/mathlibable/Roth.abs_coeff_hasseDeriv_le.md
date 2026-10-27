---
decl: Roth.abs_coeff_hasseDeriv_le
file: Roth/CoeffNorm.lean
line: 134
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The coefficient bound for (multivariate) Hasse derivatives is standard in Roth-type arguments and absent from mathlib (not even for univariate Polynomial.hasseDeriv); but the Z/abs form with Fintype, box r and uniform bound B is a specialisation of the verified pointwise bound norm of [X^e] Delta_d P at most 2^deg(e+d) times norm of [X^(e+d)] P over any SeminormedCommRing.
action: Ship MvPolynomial.norm_coeff_hasseDeriv_le (pointwise, SeminormedCommRing, via norm_nsmul_le) plus the box corollary in the MvPolynomial.hasseDeriv PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean or an Analysis companion), with a univariate Polynomial.norm_coeff_hasseDeriv_le; keep the Z form for Roth/MainLemma.lean:468 and :509 via Int.norm_eq_abs.
---

# Roth.abs_coeff_hasseDeriv_le

## Inventory entry

### `theorem Roth.abs_coeff_hasseDeriv_le`
- **Type**: `{σ : Type*} [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) (e : σ →₀ ℕ) : |(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B`
- **What**: If `deg_{X_j} P ≤ r_j` for all `j` and all coefficients of the integer polynomial `P` are bounded by `B` in absolute value, then every coefficient of every Hasse derivative `Δ_d P` is bounded by `2^{r_1+⋯+r_m} B`.
- **How**: Rewrite with `MvPolynomial.coeff_hasseDeriv` (`[X^e] Δ_d P = hasseCoeff d (e+d) · [X^(e+d)] P`), push casts and `abs_mul`/`Nat.abs_cast`; case on `e + d ∈ P.support`: if yes, bound the binomial factor by `MvPolynomial.hasseCoeff_le_two_pow` (box hypothesis supplied by `monomial_le_degreeOf` + `hP`) and combine with `hB` via `mul_le_mul`; if not, the coefficient is zero and the RHS is nonneg (`mul_nonneg`, `positivity`).
- **Hypotheses**: `[Fintype σ]` (to form `∑ j, r j`), `hP` (degree box), `hB` (uniform coefficient bound).
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseCoeff_le_two_pow`
- **Used by**: Roth/MainLemma.lean:468 (twice, nested, in private `abs_eval_iterated_hasseDeriv_lt_aux`, feeding `Roth.abs_eval_le`); Roth/MainLemma.lean:509 (in private `abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, feeding `Roth.abs_coeff_diag_le`). Not used elsewhere (`grep -rn abs_coeff_hasseDeriv_le Roth/`).
- **Visibility**: public
- **Lines**: 130–144, proof length 8 lines
- **Notes**: Source clean.tex:1445 ("abc(Δ_j W) ≤ 2^{r_1+⋯+r_m} B_1") and §3 proof of Lemma 3. Sibling `Roth.normOne_hasseDeriv_le` (line 149) is the ℓ¹ analogue.

## Junk check (Step 8)
- Used anywhere? Yes: 3 uses in 2 places of Roth/MainLemma.lean (Lemma 9 size estimates).
- Wrapper of 1–2 mathlib calls? No: combines the project's `coeff_hasseDeriv` and `hasseCoeff_le_two_pow` with a support case split (8 lines).
- Does mathlib have it? No (no norm/abs bound on Hasse-derivative coefficients, multivariate or univariate; see Phase 5).
- Too specific (inline)? No: used 3 times, and it is the natural size estimate for Hasse derivatives.
- Well-chosen? Yes for the project; for mathlib the pointwise normed form is better (Phase 4).
- Conclusion: `KEEP` — action: keep; upstream the generalised pointwise form with the `hasseDeriv` PR.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.abs_coeff_hasseDeriv_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (genuine 8-line proof). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` compiles with no errors or warnings)
- decl `Roth.abs_coeff_hasseDeriv_le`: resolved at Roth/CoeffNorm.lean:134
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.abs_coeff_hasseDeriv_le` is a theorem stating the following: let `P ∈ ℤ[X_1,…,X_m]` have degree at most `r_j` in `X_j` and all coefficients of absolute value at most `B`. Then for every multi-index `d`, every coefficient of the Hasse derivative `Δ_d P = ∑_k binom(k,d) a_k X^{k-d}` has absolute value at most `2^{r_1+⋯+r_m} B`. Equivalently `abc(Δ_d P) ≤ 2^{|r|} abc(P)` for the sup-norm of coefficients.

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]` — the (finite) set of variables.
- `d : σ →₀ ℕ` — order of the Hasse derivative.
- `P : MvPolynomial σ ℤ` — the polynomial.
- `r : σ → ℕ` — partial degree bounds.
- `B : ℝ` — coefficient bound.
- `e : σ →₀ ℕ` — the output exponent.

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — partial degree box.
- `hB : ∀ e, |P_e| ≤ B` — uniform coefficient bound.

Conclusion (math): `|[X^e] Δ_d P| ≤ 2^{∑ r_j} B`.

Conclusion (Lean): `|(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper size estimate (not listed as a main result, not named, no new structure).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 8
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative coefficient bound 2^degree height polynomial Roth lemma | yes | derived polynomials in Roth–Ridout have coefficients bounded by `2^{r_1+⋯+r_m}` times the height (arXiv math/0307203) | exactly the project form, stated inline in a Roth-type proof |
| 2 | WebSearch (general form) | height of derivative of polynomial H(D_i P) ≤ 2^deg H(P) multivariate binomial coefficient bound Siegel lemma | partial | no standalone lemma; product-height bounds `H(R) ≤ N^{deg R} ∏ H(P_k)` (arXiv 2112.13919 etc.) | the derivative bound is treated as immediate from `binom(k,d) ≤ 2^{|k|}` |
| 3 | WebSearch (named-after / aliases) | divided derivative / Hasse derivative height bound Roth's theorem index | yes | Bombieri–Gubler / Hindry–Silverman style "height of derivatives" lemma (arXiv 2502.00731 survey, Lemma 3.7 in Adiceam–Shirandami); Maculan Roth notes | always pointwise: `|∂_d a_k| = binom(k,d)|a_k| ≤ 2^{|k|}|a_k|` |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 1445, 487–495 | yes | "abc(Δ_{j_1,…,j_m} W) ≤ 2^{r_1+⋯+r_m} B_1" | source of the project statement |
| 6 | nLab | Hasse derivative / divided power | partial | Hasse–Schmidt derivations as divided-power operators; no norm estimates | algebraic only |
| 7 | nCatLab | — | n/a | — | not a categorical statement (an archimedean coefficient inequality) |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators algebraically; no coefficient size bounds |
| 9 | MathOverflow / Math.SE | height of Hasse derivative of polynomial | partial | folklore `H(Δ_d P) ≤ 2^{deg P} H(P)` used without proof in transcendence/Diophantine answers | no competing form |
| 10 | recent arXiv (last 5 years) | effective Roth / Ridout constants (arXiv 2601.11376), subspace theorem survey (2502.00731) | yes | same `2^{∑ r_j}` factor | no generalisation beyond the pointwise bound |

### Literature summary (Phase 3)

Concept identified as: height (coefficient sup-norm) bound for Hasse/divided derivatives, `H(Δ_d P) ≤ 2^{deg P} H(P)`; in Roth's proof with partial degrees `r_j`, factor `2^{r_1+⋯+r_m}`.
Sources agree on the standard form: yes — all derive it from the pointwise identity `[X^e] Δ_d P = binom(e+d,d) [X^{e+d}] P` and `binom(k,d) ≤ 2^{|k|}`.
Most general standard form: pointwise, for any normed coefficient ring: `‖[X^e] Δ_d P‖ ≤ binom(e+d,d) ‖[X^{e+d}] P‖ ≤ 2^{|e+d|} ‖[X^{e+d}] P‖`; the box/sup-norm version is a corollary.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / number-field absolute values / any normed ring — only `‖n • a‖ ≤ n ‖a‖` is used.
  - shape: pointwise bound vs. sup-norm (height) bound vs. box-parametrised bound `2^{∑ r_j}`.
  - finiteness of variables: only needed to write `∑_j r_j`; the pointwise form needs none.
Disagreement with the literature: none in content; the project fixes ℤ and the box-sup shape required by its call sites.

### Generality analysis — `Roth.abs_coeff_hasseDeriv_le`

Literature-standard form (from Phase 3): `‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (e + d).degree * ‖P.coeff (e + d)‖` for `P : MvPolynomial σ R`, `[SeminormedCommRing R]`, any `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` with `|(· : ℝ)|` | `[SeminormedCommRing R]`, `‖·‖` | yes | proof needs only `norm_nsmul_le` (no `NormOneClass`); verified (`Evidence88.norm_coeff_hasseDeriv_le_of_degreeOf_le`), ℤ form recovered via `Int.norm_eq_abs` |
| 2 | `[Fintype σ]` | required | not needed | yes | pointwise form uses `(e+d).degree`; verified (`Evidence88.norm_coeff_hasseDeriv_le`) |
| 3 | `hP` (degree box `r`) | required | not needed (pointwise) | yes | only used to bound `(e+d).degree` on the support; pointwise form drops it; box form becomes a corollary |
| 4 | `hB` (uniform bound `B`) | required | not needed (pointwise) | yes | pointwise form compares with the single coefficient `‖P.coeff (e+d)‖` |
| 5 | `d`, `e` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4 (ℤ → `[SeminormedCommRing R]`; drop `Fintype σ`, `hP`, `hB` in the pointwise form)
Verification: `.mathlib-quality/overview/evidence/Roth.abs_coeff_hasseDeriv_le/general_and_composition.lean` — (1) pointwise `norm_coeff_hasseDeriv_le` over `[SeminormedCommRing R]`, no `Fintype`/`r`/`B`; (2) project-shaped `norm_coeff_hasseDeriv_le_of_degreeOf_le` over `[SeminormedCommRing R]`; (3) recovery `example` of the exact project statement from (2) via `Int.norm_eq_abs`. `lake env lean`: no errors, no warnings (first run failed only because `norm_nsmul_le` takes implicit arguments; fixed).
Proposed restatement:

```lean
theorem MvPolynomial.norm_coeff_hasseDeriv_le {σ R : Type*} [SeminormedCommRing R]
    (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    ‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (e + d).degree * ‖P.coeff (e + d)‖

theorem MvPolynomial.norm_coeff_hasseDeriv_le_of_degreeOf_le {σ R : Type*}
    [SeminormedCommRing R] [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, ‖P.coeff e‖ ≤ B) (e : σ →₀ ℕ) :
    ‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (∑ j, r j) * B
```

Cost of restatement: CHEAP — 3–6 line proofs, compiled.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | hypotheses are genuine data bounds | — |
| 2 | Sequences → filters? | no | finite algebraic inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ/`|·|` → `[SeminormedCommRing R]`/`‖·‖` | estimates over ℝ, ℂ, ℚ_p, number-field completions |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general? | no | `σ →₀ ℕ` is the MvPolynomial exponent monoid; univariate companion via `Polynomial.hasseDeriv_coeff` | — |
| 8 | Concrete-via-abstract? | yes | after `coeff_hasseDeriv` the proof uses only `‖n • a‖ ≤ n‖a‖` and the binomial bound; ℤ never matters | covered by row 5 |
| 9 | False-generalisation guard | no | for `R = ℤ` the general box form reduces to the project statement (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.norm_coeff_hasseDeriv_le` (pointwise, normed) with the box form as corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: size estimates for Hasse derivatives over any seminormed ring; composes with `Polynomial.supNorm`/`Polynomial.le_supNorm` (sup-norm form `supNorm (hasseDeriv k p) ≤ 2^{natDegree p} supNorm p` univariately) and with the proposed `MvPolynomial.l1Norm` (sibling `normOne_hasseDeriv_le`).
  - Real mathematical improvement: one estimate for every coefficient ring, and a pointwise statement free of the project's auxiliary box parameters.

### Proof strategy — `Roth.abs_coeff_hasseDeriv_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | coefficient inequality is inherently elementwise | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | yes | `Finsupp.choose_le_two_pow_degree` (multi-index `Nat.choose_le_two_pow`, see hasseCoeff_le_two_pow report) and `coeff_hasseDeriv` (ships with the `hasseDeriv` PR) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Coefficient formula + binomial bound. In the general setting `norm_nsmul_le` replaces the `Int.cast`/`abs_mul` bookkeeping; the pointwise form needs no support case split.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.abs_coeff_hasseDeriv_le`

[A] Lean-Finder       "absolute value of coefficient of Hasse derivative of a polynomial bounded by 2^degree times coefficient bound"  no hits (only `Polynomial.hasseDeriv_coeff`, `natDegree_hasseDeriv_le`, Chebyshev coefficient bounds, `cauchyBound`)
[B] Loogle            `‖Polynomial.coeff (Polynomial.hasseDeriv _ _) _‖ ≤ _`  no hits
[C] LeanSearch        "norm of coefficient of hasseDeriv bounded by binomial times norm of coefficient"  no hits (`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`, `Polynomial.coeff_le_of_roots_le`, `LaurentSeries.hasseDeriv_coeff` — unrelated)
[D] Grep mathlib src  `hasseDeriv` lines with `norm`/`abs`/`_le`; `namespace Roth`; `choose_le_two_pow`  only `Polynomial.natDegree_hasseDeriv_le` (degree, not size); `Nat.choose_le_two_pow` (Data/Nat/Choose/Bounds.lean:96) as building block; no MvPolynomial Hasse derivative at all; no `namespace Roth`
[E] Name pattern      `norm_coeff_hasseDeriv`, `abs_coeff_hasseDeriv`, `hasseDeriv_coeff_le` (grep)  no hits

Searched for both:
  - the user's current form (ℤ, box, uniform bound)
  - the literature-standard form (pointwise normed bound, multivariate and univariate)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks `Nat.choose_le_two_pow`, `norm_nsmul_le`, `Polynomial.hasseDeriv_coeff` (univariate only).

### Normal-form check — `Roth.abs_coeff_hasseDeriv_le`

Equivalent formalisms: pointwise `‖c_e(Δ_d P)‖ ≤ 2^{|e+d|}‖c_{e+d}(P)‖`; box-uniform `… ≤ 2^{∑ r_j} B`; sup-norm `supNorm (Δ_d P) ≤ 2^{…} supNorm P` (no MvPolynomial sup-norm in mathlib).
Does mathlib already have a canonical form? No. Proposed canonical form: the pointwise `norm_coeff_hasseDeriv_le` (shape of `Polynomial.le_supNorm`/`norm_coeff_le_choose_mul_mahlerMeasure`: `‖coeff‖ ≤ …`). RHS convention: n/a (inequality).

### Syntactic generality — `Roth.abs_coeff_hasseDeriv_le`

Alternative restatements attempted:
- pointwise `‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (e + d).degree * ‖P.coeff (e + d)‖` (compiled)
- pointwise sharp `‖…‖ ≤ (e + d).choose d * ‖P.coeff (e + d)‖` (immediate from `coeff_hasseDeriv` + `norm_nsmul_le`)
- box-uniform form with `r`, `B` (compiled, the call-site shape)
Chosen restatement: pointwise `2^degree` form as the main lemma plus the box-uniform corollary. Justification: the pointwise form is hypothesis-free; the corollary is exactly what the 3 call sites consume (nested application at MainLemma.lean:468 needs the uniform-`B` output shape).

### Superfluous-argument audit — `Roth.abs_coeff_hasseDeriv_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | only for `∑ j, r j` | drop in the pointwise form |
| 2 | `hP` | only to bound `(e+d).degree` | drop in the pointwise form |
| 3 | `hB` | yes for the uniform form | pointwise form compares with one coefficient |
| 4 | ℤ coefficients | no | `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (main lemma = pointwise normed bound)
Syntactic generality: RESTATE (pointwise + box corollary)
Superfluous arguments: ℤ specialisation; `Fintype σ`, `hP`, `hB` in the main lemma

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.abs_coeff_hasseDeriv_le`

Internal use count: 3 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:468 | `(abs_coeff_hasseDeriv_le i _ hdQ (abs_coeff_hasseDeriv_le k P hP hc)) (fun _ ↦ α)` (two nested uses) |
| Roth/MainLemma.lean:509 | `(abs_coeff_diag_le _ (abs_coeff_hasseDeriv_le j P hd hc) k).trans` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.abs_coeff_hasseDeriv_le`?):
  - (none; the sibling `Roth.normOne_hasseDeriv_le` at CoeffNorm.lean:149 re-uses `hasseCoeff_le_two_pow` for the ℓ¹ analogue, not this bound).

### Composition check (Phase 6)

Can `Roth.abs_coeff_hasseDeriv_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: via a mathlib Hasse-derivative coefficient bound
  - Result: fails — mathlib has no `MvPolynomial.hasseDeriv` and no size bound even for `Polynomial.hasseDeriv`.
Attempt 2: `coeff_hasseDeriv` + `norm_nsmul_le` + `Nat.choose_le_two_pow` (multi-index)
  - Result: partial — `coeff_hasseDeriv` and the multi-index binomial bound are project lemmas (not mathlib), and the box form still needs the support case split; a 6-line proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.abs_coeff_hasseDeriv_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard Roth-type height bound for Hasse derivatives (clean.tex:1445; Roth–Ridout arXiv math/0307203; Bombieri–Gubler-style surveys), always derived pointwise.
- Generality analysis (Phase 4): STRICTLY NARROWER; pointwise normed form over `[SeminormedCommRing R]` without `Fintype`/`r`/`B` compiled, plus normed box form and ℤ recovery.
- Mathlib search (Phase 5): not in mathlib; no size bound on Hasse-derivative coefficients even univariately.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's Hasse derivative API (`Mathlib/Algebra/Polynomial/HasseDeriv.lean`) is purely algebraic: it has the coefficient formula `Polynomial.hasseDeriv_coeff` and `natDegree_hasseDeriv_le`, but no estimate on the *size* of coefficients, and there is no multivariate Hasse derivative at all (the parent `MvPolynomial.hasseDeriv` is assessed YES-but-generalise-first). The coefficient-size bound `‖[X^e] Δ_d P‖ ≤ 2^{|e+d|} ‖[X^{e+d}] P‖` is the standard estimate in auxiliary-polynomial arguments (Roth, Siegel/Thue, subspace theorem), so it fills a concrete gap next to the planned `MvPolynomial.hasseDeriv` and `Finsupp.choose` additions.

The project form is a specialisation: ℤ with `|·|`, a finite variable set, a degree box `r` and a uniform bound `B`. The evidence file shows the pointwise statement holds over any `[SeminormedCommRing R]` with a three-line proof (`coeff_hasseDeriv`, `nsmul_eq_mul`, `norm_nsmul_le`, multi-index `choose_le_two_pow_degree`), and the box-uniform form also holds over any seminormed commutative ring and recovers the exact project statement via `Int.norm_eq_abs`. The box form should ship as a corollary because it is what iterated estimates consume (MainLemma.lean:468 applies it twice in a nest).

Reason for the generalisation: LITERATURE-WEAKENING (pointwise, no auxiliary hypotheses) and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy).

Proposed restatement:
```lean
theorem MvPolynomial.norm_coeff_hasseDeriv_le {σ R : Type*} [SeminormedCommRing R]
    (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    ‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (e + d).degree * ‖P.coeff (e + d)‖ := by
  sorry  -- proof in evidence file

theorem MvPolynomial.norm_coeff_hasseDeriv_le_of_degreeOf_le {σ R : Type*}
    [SeminormedCommRing R] [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, ‖P.coeff e‖ ≤ B) (e : σ →₀ ℕ) :
    ‖(hasseDeriv d P).coeff e‖ ≤ 2 ^ (∑ j, r j) * B := by
  sorry  -- proof in evidence file
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- size estimates for Hasse derivatives over ℝ, ℂ, ℚ_p and number-field completions (needed by any formalisation of Thue–Siegel–Roth or Schmidt);
- a univariate `Polynomial.norm_coeff_hasseDeriv_le` (from `Polynomial.hasseDeriv_coeff` + `Nat.choose_le_two_pow`) and `supNorm (hasseDeriv k p) ≤ 2 ^ p.natDegree * supNorm p` next to `Polynomial.supNorm`;
- composition with the proposed `MvPolynomial.l1Norm` (sibling `normOne_hasseDeriv_le`).

PR grouping: ship with `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `Finsupp.choose` / `choose_le_two_pow_degree` (from the hasseCoeff_le_two_pow report), and the ℓ¹ sibling `normOne_hasseDeriv_le` if the `l1Norm` PR lands first.

Next action: run `/generalise Roth.abs_coeff_hasseDeriv_le`, restate as `MvPolynomial.norm_coeff_hasseDeriv_le` (+ box corollary) over `[SeminormedCommRing R]`, and keep the ℤ form at Roth/MainLemma.lean:468 and :509 via `Int.norm_eq_abs`.

---

## Next step

Upstream `MvPolynomial.norm_coeff_hasseDeriv_le` (pointwise) and `norm_coeff_hasseDeriv_le_of_degreeOf_le` (box corollary) over `[SeminormedCommRing R]` in the `MvPolynomial.hasseDeriv` PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, or an Analysis-side companion if the algebra file must not import norms), with a univariate `Polynomial` companion; locally keep the ℤ statement for Roth/MainLemma.lean:468 and :509.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.abs_coeff_hasseDeriv_le/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): `hasseCoeff_le_two_pow_degree`; pointwise `norm_coeff_hasseDeriv_le` over `[SeminormedCommRing R]` (no `Fintype`, `r`, `B`); box-form `norm_coeff_hasseDeriv_le_of_degreeOf_le` over `[SeminormedCommRing R]`; recovery `example` of the exact project statement; sanity `example` via `Roth.abs_coeff_hasseDeriv_le`. `lake env lean`: clean (no errors, no warnings). First run failed only because `norm_nsmul_le` has implicit arguments (`(norm_nsmul_le _ _)` → `norm_nsmul_le`).
- Mathlib greps: `hasseDeriv` with `norm`/`abs`/`_le` (only `natDegree_hasseDeriv_le`), `namespace Roth` (none), `choose_le_two_pow` (Data/Nat/Choose/Bounds.lean:96).
- Lean-Finder / LeanSearch / Loogle queries as in Phase 5 (no hit).
- WebSearch ×3 (Hasse derivative coefficient bound in Roth; height of derivative bound; divided/Hasse derivative height bound in Roth's theorem), local reference clean.tex:1445.
- ChatGPT MCP: n/a (not configured in this session).
