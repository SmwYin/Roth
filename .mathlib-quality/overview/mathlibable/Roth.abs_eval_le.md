---
decl: Roth.abs_eval_le
file: Roth/CoeffNorm.lean
line: 223
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The local value bound for a polynomial with sup-coefficient bound B and partial degrees at most r_j, namely the norm of P(x) is at most B times the product of (1 + norm x_j)^(r_j), is absent from mathlib (its nearest sibling AbsoluteValue.eval_mvPolynomial_le needs homogeneity, an l1 coefficient sum and a sup of the x_j) and not a short composition; the project proof compiles verbatim over any NormedCommRing with NormOneClass, recovering the Z-to-R statement.
action: Ship MvPolynomial.norm_eval_le_mul_prod_one_add_pow over [NormedCommRing R] [NormOneClass R] (compiled in evidence/Roth.abs_eval_le/abs_eval_le_general.lean) next to AbsoluteValue.eval_mvPolynomial_le in Mathlib/NumberTheory/Height/MvPolynomial.lean or an Analysis/Polynomial companion, together with the geom_sum_le_one_add_pow PR and with box replaced by Finset.Iic; keep the Z form for the single caller Roth/MainLemma.lean:466.
---

# Roth.abs_eval_le

## Inventory entry

### `theorem Roth.abs_eval_le`
- **Type**: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (x : σ → ℝ) : |eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j`
- **What**: If every coefficient of the integer polynomial `P` is at most `B` in absolute value and `P` has degree at most `r_j` in `x_j`, then `|P(x)| ≤ B ∏_j (1 + |x_j|)^{r_j}` for every real point `x`.
- **How**: `eval_map` and `eval₂_eq'` expand `P(x)` as `∑_{k ∈ supp P} a_k ∏_j x_j^{k_j}`; `Finset.abs_sum_le_sum_abs` plus `abs_mul`/`Finset.abs_prod`/`abs_pow` and `hB` bound it by `∑_{k ∈ supp P} B ∏_j |x_j|^{k_j}`; `Finset.sum_le_sum_of_subset_of_nonneg` with `monomial_le_degreeOf` and `mem_box` enlarges the index set to `box r`; the private helper `sum_box_prod_pow_le_aux` (via `Finset.prod_univ_sum` and `geom_sum_le_one_add_pow`) finishes.
- **Hypotheses**: `[Fintype σ]`; `hP` (partial degree bounds); `hB` (uniform coefficient bound). Nonnegativity of `B` is derived from `hB 0`.
- **Uses from project**: `Roth.box`, `Roth.mem_box`, `Roth.sum_box_prod_pow_le_aux` (which uses `Roth.geom_sum_le_one_add_pow`)
- **Used by**: Roth/MainLemma.lean:466 (`abs_eval_iterated_hasseDeriv_lt_aux`, private, applied to `hasseDeriv i (hasseDeriv k P)` at the diagonal point `fun _ ↦ α`); also listed in the CoeffNorm.lean module docstring (line 32).
- **Visibility**: public
- **Lines**: 219–240 (docstring 219–222, statement 223–225), proof length 15 lines
- **Notes**: Source: §6, proof of Lemma 9 (clean.tex l.1546–1568). The paper's Lean note explicitly prefers this route ("absorbs the monomial sum without an additional box-cardinality factor").

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:466 (Lemma 9 evaluation estimate).
- Wrapper of 1–2 mathlib calls? No: a three-step calc (triangle inequality, support-into-box enlargement, box-sum factorisation plus geometric bound).
- Does mathlib have it? No. Loogle `‖MvPolynomial.eval _ _‖ ≤ _` empty; leansearch/leanfinder return only `MvPolynomial.eval_eq`, Mahler-measure and Gauss-norm results. Nearest relative: `AbsoluteValue.eval_mvPolynomial_le` (Mathlib/NumberTheory/Height/MvPolynomial.lean:189), which needs `p.IsHomogeneous N`, uses the l1 coefficient sum and `(⨆ i, v (x i))^N`; it does not give the partial-degree form.
- Too specific / inline? Single use, but it is the named evaluation step of the paper and a standard local height estimate; inlining would move a 15-line calc into an already long private lemma.
- Well-chosen? Yes, modulo the `ℤ`-mapped-to-`ℝ` presentation (a norm statement over a normed ring is cleaner).
- Conclusion: `KEEP`. Action: keep; optionally restate as the `R = ℝ` instance of the general norm lemma.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.abs_eval_le` absent from mathlib (grep `abs_eval_le` over `.lake/packages/mathlib/Mathlib/`: only the unrelated `Polynomial.finite_abs_eval_le_of_degree_lt`). Not a glue lemma (15-line proof). Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` compiles with no output)
- decl `Roth.abs_eval_le`:  resolved at Roth/CoeffNorm.lean:223
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.abs_eval_le` is a theorem stating the following: let `P = ∑_k a_k x^k` be a polynomial in finitely many variables `x_j` (`j ∈ σ`) with integer coefficients, of degree at most `r_j` in `x_j`, and with `|a_k| ≤ B` for all `k`. Then for every real point `x`, `|P(x)| ≤ B ∏_j (1 + |x_j|)^{r_j}`. (Indeed `|P(x)| ≤ B ∏_j ∑_{s ≤ r_j} |x_j|^s ≤ B ∏_j (1 + |x_j|)^{r_j}`.)

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable index set.
- `P : MvPolynomial σ ℤ` — the polynomial (evaluated after `map (Int.castRingHom ℝ)`).
- `r : σ → ℕ` — partial degree bounds; `B : ℝ` — coefficient bound; `x : σ → ℝ` — the point.

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — partial degree bounds.
- `hB : ∀ d, |(P.coeff d : ℝ)| ≤ B` — uniform coefficient bound (height `H(P) ≤ B`).

Conclusion (math): `|P(x)| ≤ B ∏_j (1 + |x_j|)^{r_j}`.

Conclusion (Lean): `|eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper estimate (triangle inequality plus a geometric-sum bound) used once in Lemma 9; not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 15 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | bound P(x) at most H(P) prod (1+x_j)^(r_j) multivariate polynomial height partial degrees value estimate | partial | evaluation height bounds `h(P(y)) ≤ h(P) + m log(d+1) + d h(y)` (arXiv 2001.04138, generalising Bombieri–Gubler Prop. B.7.1); `h(F(x)) ≤ d h(x) + h(F) + log(d+1)` (arXiv 2105.07670) | log-height versions of the same local estimate; exact partial-degree form not stated |
| 2 | WebSearch (general form) | polynomial value bounded by length times max(1,x)^degree inequality height L(P) | partial | `|P(α)| ≤ L(P) max(1,|α|)^d` with `L(P)` the length (folklore triangle inequality) | length/height/Mahler measure definitions (Schinzel; Dubickas 2021) |
| 3 | WebSearch (named-after / aliases) | Roth's theorem proof auxiliary polynomial estimate P(alpha,...,alpha) at most B (1+alpha)^(r_1+...+r_m) | partial | Roth-proof expositions (Evertse Luminy notes, arXiv 2502.00731 following Bombieri–Gubler Ch. 6) use the estimate silently | routine step, never a named lemma |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` l.1546–1568 | yes | `|(Δ_i Q)(α,…,α)| ≤ abc(Δ_i Q) ∏_j ∑_{s≤r_j} |α|^s` with `∑_{s≤r} t^s ≤ (1+t)^r` | exactly the project statement (at the diagonal point) |
| 6 | nLab | polynomial / evaluation map | no | — | no norm/height content |
| 7 | nCatLab | — | n/a | — | not a categorical statement (archimedean estimate) |
| 8 | Stacks Project | — | n/a | — | algebraic geometry without absolute values; no height estimates |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore triangle-inequality bound `|P(x)| ≤ L(P) ∏ max(1,|x_j|)^{deg_j P}` | stated in passing only |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | partial | arXiv 2001.04138 (2020), 2105.07670 (2021), 2502.00731 (2025) | log-height versions |

### Literature summary (Phase 3)

Concept identified as: the local (archimedean) value bound for a polynomial in terms of its height and partial degrees, the local ingredient of `h(P(x)) ≤ h(P) + ∑ deg_j h(x_j) + log(#monomials)` (Bombieri–Gubler, Prop. B.7.1 / Ch. 1).
Sources agree on the standard form: yes, up to presentation: `|P(x)| ≤ H(P) ∏_j ∑_{s≤r_j} |x_j|^s ≤ H(P) ∏_j (1+|x_j|)^{r_j}`, or with the length `L(P)` and `max(1,|x_j|)`.
Most general standard form: over any (semi)normed commutative ring or any absolute value `v`: `v(P(x)) ≤ B ∏_j (1 + v(x_j))^{r_j}` when `v(a_k) ≤ B` and `deg_{x_j} P ≤ r_j`.
Generality dimensions where the literature varies:
  - coefficient/point ring: `ℤ → ℝ` (Roth) to any normed ring / absolute value on a field.
  - coefficient size: sup-height `H(P)` (here) vs length `L(P)` (then `max(1,|x_j|)` replaces `1+|x_j|`).
  - degree data: partial degrees (here) vs total degree / homogeneous degree (mathlib's `AbsoluteValue.eval_mvPolynomial_le`).
Disagreement with the literature: none.

### Generality analysis — `Roth.abs_eval_le`

Literature-standard form (from Phase 3): for `[NormedCommRing R] [NormOneClass R]`, `P : MvPolynomial σ R`, `x : σ → R`, `‖P(x)‖ ≤ B ∏_j (1 + ‖x_j‖)^{r_j}`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficients `ℤ` mapped to `ℝ`, `|·|` | `eval x (map (Int.castRingHom ℝ) P)` | `eval x P` over `[NormedCommRing R] [NormOneClass R]`, `‖·‖` | yes | proof uses only `norm_sum_le`, `norm_mul_le`, `Finset.norm_prod_le`, `norm_pow_le`; verified (evidence (1)) |
| 2 | `[NormOneClass R]` | (implicit, `ℝ`) | needed | no | used for `‖∏‖ ≤ ∏‖·‖` over possibly empty products and `‖x^0‖ ≤ 1`; could be avoided only by a seminormed restatement with extra care, not standard |
| 3 | `[NormedCommRing R]` vs `SeminormedCommRing` | (`ℝ`) | `NormedCommRing` | no (in mathlib today) | `Finset.norm_prod_le` is stated for `NormedCommRing` (Mathlib/Analysis/Normed/Ring/Basic.lean:383); first attempt over `SeminormedCommRing` failed to elaborate for this reason |
| 4 | `[Fintype σ]` | finite | finite (or `Finite`) | no | product over all variables on the RHS needs finiteness |
| 5 | `hP` partial degrees | `degreeOf j P ≤ r j` | same | no | essential; total degree would give a different (weaker in general) bound |
| 6 | `hB` | `∀ d` | `∀ d` (or on support) | no | standard shape; off-support coefficients are 0 |
| 7 | box spelling | `Roth.box r` (internal to the proof) | `Finset.Iic` | n/a | proof-internal; `Roth.box` report says replace by `Finset.Iic` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (row 1), compiled clean in the evidence file (`lake env lean`: no output).
Proposed restatement:

```lean
theorem MvPolynomial.norm_eval_le_mul_prod_one_add_pow {σ R : Type*} [Fintype σ]
    [NormedCommRing R] [NormOneClass R] (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (x : σ → R) :
    ‖eval x P‖ ≤ B * ∏ j, (1 + ‖x j‖) ^ r j
```

Cost of restatement: CHEAP — the project proof with `abs_*` replaced by the norm lemmas (compiled).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | hypotheses are genuine data bounds |
| 2 | sequences to filters? | no | — | finite estimate |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `ℤ`-mapped-to-`ℝ` with `|·|` to `[NormedCommRing R] [NormOneClass R]` with `‖·‖` | applies over `ℝ`, `ℂ`, `ℚ_[p]`, `ℤ_[p]` and composes with `Polynomial`/`MvPolynomial` norm API; `ℤ` recovered via `eval_map` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `σ` already arbitrary finite |
| 8 | concrete-via-abstract? | no | after `rw [eval_map]` the proof uses only norm properties of `ℝ`, which row 5 already captures; no named concrete object beyond the ring | — |
| 9 | false-generalisation guard | no false generalisation | the original statement is recovered from (1) with `R = ℝ` applied to `map (Int.castRingHom ℝ) P` (compiled, evidence (2)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the norm lemma in 4b (an `AbsoluteValue` variant `v (eval x P) ≤ B * ∏ j, (1 + v (x j)) ^ r j` is the same proof with `AbsoluteValue.sum_le`/`map_mul`/`map_prod`/`map_pow`, matching the style of `AbsoluteValue.eval_mvPolynomial_le`; not compiled, optional companion).
  - Cost: CHEAP
  - Mathlib downstream this enables: partial-degree local height bounds alongside the homogeneous ones in Mathlib/NumberTheory/Height/MvPolynomial.lean; value estimates for auxiliary polynomials in Diophantine approximation (Roth, Thue–Siegel, Schmidt) over any completion.
  - Real mathematical improvement: removes the `ℤ`/cast detour and states the estimate for every normed ring at once.

### Proof strategy — `Roth.abs_eval_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `geom_sum_le_one_add_pow` (assessed YES-but-generalise-first) and the box-sum factorisation over `Finset.Iic` (proof-internal; `Finset.prod_univ_sum` already in mathlib) | ship with the geom-sum PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (triangle inequality, enlarge to the box, factorise `∑_{k ∈ box} ∏_j = ∏_j ∑_{s ≤ r_j}`, geometric bound) — the strategy the paper's Lean note itself recommends.
  - Missing mathlib API (if any): `geom_sum_le_one_add_pow` (separate YES report).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.abs_eval_le`

[A] Lean-Finder       "absolute value of P(x) at most max coefficient times product over variables of (1+|x_j|)^(degree in x_j)"   hits: Mahler-measure bounds, Schwartz–Zippel — none relevant
[B] Loogle            `‖MvPolynomial.eval _ _‖ ≤ _`   no hits
[C] LeanSearch        "norm of evaluation of multivariate polynomial bounded by coefficient bound times product of (1 + norm x_i) to the degree"   hits: `MvPolynomial.eval_eq`, `Polynomial.le_gaussNorm`, `Polynomial.mahlerMeasure_le_sum_norm_coeff` — building blocks / unrelated
[D] Grep mathlib src  `abs_eval_le`, `norm_eval_le`, `eval_mvPolynomial_le`, `degreeOf_map`   hits: `AbsoluteValue.eval_mvPolynomial_le`, `IsNonarchimedean.eval_mvPolynomial_le` (NumberTheory/Height/MvPolynomial.lean:189, :202; homogeneous, l1 / sup-coefficient times `(⨆ v(x_i))^N`); `Polynomial.finite_abs_eval_le_of_degree_lt` (unrelated)
[E] Name pattern      `MvPolynomial.eval_eq'`, `norm_sum_le`, `Finset.norm_prod_le`, `norm_pow_le`, `Finset.prod_univ_sum`, `MvPolynomial.monomial_le_degreeOf`, `MvPolynomial.degrees_map_of_injective` (all used in the compiled evidence)   hits (building blocks)

Searched for both the user's form (`|eval x (map _ P)| ≤ …`) and the literature-standard form (norm over normed ring, absolute-value form).

Concluded: found a partial match (`AbsoluteValue.eval_mvPolynomial_le`); it covers the homogeneous/total-degree, l1-coefficient variant only, not the partial-degree sup-coefficient form; otherwise building blocks only.

### Normal-form check — `Roth.abs_eval_le`

Equivalent formalisms: (a) `|eval x (map (Int.castRingHom ℝ) P)| ≤ …` (project); (b) `‖eval x P‖ ≤ B * ∏ j, (1 + ‖x j‖) ^ r j` over a normed ring; (c) `v (eval x P) ≤ …` for an `AbsoluteValue v`; (d) the sharper `B * ∏ j, ∑ s ∈ range (r j + 1), ‖x j‖ ^ s`.
Does mathlib already have a canonical form for this idea? Partly: `AbsoluteValue.eval_mvPolynomial_le` uses form (c) for the homogeneous case.
Is our statement stated against the canonical form? After restatement (b) (or (c) to match the Height file), yes.
RHS convention respected? yes (inequality; bound on RHS).

### Syntactic generality — `Roth.abs_eval_le`

Alternative restatements attempted:
- (b) norm form over `[NormedCommRing R] [NormOneClass R]` (compiles; evidence (1))
- (b) over `SeminormedCommRing` (fails: `Finset.norm_prod_le` needs `NormedCommRing`)
- (a) recovered from (b) (compiles; evidence (2))
Chosen restatement: (b), with (c) as an optional companion in the Height file.
Justification: (b) applies directly to any normed ring and is what consumers in analysis use; the `ℤ` caller needs only `eval_map` plus `Real.norm_eq_abs`.

### Superfluous-argument audit — `Roth.abs_eval_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficient ring `ℤ` and the map to `ℝ` | no | any normed commutative ring (evidence (1)) |
| 2 | `[Fintype σ]` | yes | RHS is a product over all variables |
| 3 | `hP` | yes | without it the RHS exponent is unrelated to `P` |
| 4 | `hB` | yes | the bound; also gives `0 ≤ B` |
| 5 | `x` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (after restatement to `‖eval x P‖` over a normed ring)
Syntactic generality: RESTATE (normed-ring form (b))
Superfluous arguments: 1 to drop (the `ℤ`/cast specialisation)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.abs_eval_le`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:466 (`abs_eval_iterated_hasseDeriv_lt_aux`) | `have heval := abs_eval_le (hasseDeriv i (hasseDeriv k P)) (fun j ↦ …) (abs_coeff_hasseDeriv_le i _ hdQ …) (fun _ ↦ α)` |

Inline-derivation grep (`abs_sum_le_sum_abs`, `eval_eq'` over `Roth/`):
  - (none) — CoeffNorm.lean:177 is `abs_coeff_diag_le`; Main.lean:333 and :403 bound a Taylor-expansion sum against `card_box`, a different estimate.

### Composition check (Phase 6)

Can `‖eval x P‖ ≤ B * ∏ j, (1 + ‖x j‖) ^ r j` be derived from mathlib in ≤3 chained calls?

Attempt 1: `AbsoluteValue.eval_mvPolynomial_le`
  - Mathlib decls used: `AbsoluteValue.eval_mvPolynomial_le`
  - Result: fails — needs `p.IsHomogeneous N` and a field `K`, gives `L(P) (⨆ v(x_i))^N`; homogenising `P` and comparing constants is a new proof, not a composition.
Attempt 2: `eval_eq'` then `norm_sum_le`, termwise `norm_mul_le`/`Finset.norm_prod_le`/`norm_pow_le`, `Finset.sum_le_sum_of_subset_of_nonneg` into `Finset.Iic`, `Finset.prod_univ_sum`, geometric bound
  - Mathlib decls used: `MvPolynomial.eval_eq'`, `norm_sum_le`, `norm_mul_le`, `Finset.norm_prod_le`, `norm_pow_le`, `MvPolynomial.monomial_le_degreeOf`, `Finset.sum_le_sum_of_subset_of_nonneg`, `Finset.prod_univ_sum`, `Finset.prod_le_prod₀` (+ `geom_sum_le_one_add_pow`, not in mathlib)
  - Result: succeeds only as a 15-line calc proof (three substantive steps) depending on a lemma mathlib does not have.
Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.abs_eval_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the local height/value bound `|P(x)| ≤ H(P) ∏_j (1+|x_j|)^{r_j}` is folklore in Diophantine geometry (local ingredient of Bombieri–Gubler B.7.1-type evaluation bounds); paper clean.tex l.1546–1568 states it verbatim; natural over any normed ring / absolute value.
- Generality analysis (Phase 4): STRICTLY NARROWER (`ℤ` mapped to `ℝ`); the normed-ring weakening compiled clean.
- Mathlib search (Phase 5): not in mathlib; only the homogeneous l1 variant `AbsoluteValue.eval_mvPolynomial_le` exists.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The specific gap: mathlib's height file Mathlib/NumberTheory/Height/MvPolynomial.lean proves the local value bound only for homogeneous polynomials, in total degree, with the l1 coefficient sum (`AbsoluteValue.eval_mvPolynomial_le`, `IsNonarchimedean.eval_mvPolynomial_le`). Arguments of Thue–Siegel–Roth type work with multihomogeneous / partial-degree data and a sup coefficient bound, and need `‖P(x)‖ ≤ B ∏_j (1 + ‖x_j‖)^{r_j}` (or the sharper `B ∏_j ∑_{s≤r_j} ‖x_j‖^s`). Nothing in mathlib states a value bound in terms of `degreeOf`. The lemma composes with mathlib's `degreeOf` API (`degreeOf_mul_le`, `degreeOf_sum_le`, the project's Hasse-derivative degree bounds) and with any coefficient estimate of the form `‖coeff d P‖ ≤ B`.

The project's Lean form is a specialisation: the `ℤ`-to-`ℝ` map is inessential. The identical proof compiles over `[NormedCommRing R] [NormOneClass R]` (NormOneClass is used for empty products and `x^0`; `SeminormedCommRing` fails only because `Finset.norm_prod_le` is stated for `NormedCommRing`), and the original statement is recovered by `eval_map` and `Real.norm_eq_abs`. It is small and belongs in a PR with its helpers, not standalone.

Reason for the generalisation: LITERATURE-WEAKENING (`ℤ → ℝ` to any normed commutative ring) plus MODERN-IDIOM (norm statement, optionally the `AbsoluteValue` form to match the Height file).
Proposed restatement:
```lean
theorem MvPolynomial.norm_eval_le_mul_prod_one_add_pow {σ R : Type*} [Fintype σ]
    [NormedCommRing R] [NormOneClass R] (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ d, ‖P.coeff d‖ ≤ B) (x : σ → R) :
    ‖eval x P‖ ≤ B * ∏ j, (1 + ‖x j‖) ^ r j
```
Estimated cost of regeneralisation: CHEAP (compiled in evidence).
Mathlib downstream this enables: partial-degree value bounds next to `AbsoluteValue.eval_mvPolynomial_le`; height-of-value estimates for non-homogeneous auxiliary polynomials; over `ℂ`, `ℚ_[p]` alike.
Proposed mathlib location: Mathlib/NumberTheory/Height/MvPolynomial.lean (as an `AbsoluteValue` companion) or an Analysis file such as Mathlib/Analysis/Normed/Ring/ (norm form); the norm form needs only normed-ring imports.
PR grouping: with `geom_sum_le_one_add_pow` (Mathlib/Algebra/Order/Ring/GeomSum.lean), with the box sum stated over `Finset.Iic` (per the `Roth.box` report).
Local refactor: keep `Roth.abs_eval_le` for Roth/MainLemma.lean:466 as the `R = ℝ` instance via `eval_map`.
Next action: run `/generalise Roth.abs_eval_le` targeting the normed-ring form (and decide on the `AbsoluteValue` companion), then `/cleanup` and `/pre-submit` together with the geom-sum PR.

---

## Next step

Ship `MvPolynomial.norm_eval_le_mul_prod_one_add_pow` over `[NormedCommRing R] [NormOneClass R]` together with `geom_sum_le_one_add_pow`. Locally, `Roth.abs_eval_le` becomes the `ℝ` instance and the call site Roth/MainLemma.lean:466 stays as it is.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.abs_eval_le/abs_eval_le_general.lean` (imports `Mathlib.Analysis.Normed.Ring.Lemmas`, `Mathlib.Analysis.Normed.Group.Int`, `Mathlib.Analysis.Normed.Field.Basic`, `Roth.CoeffNorm`). `lake env lean` gives no output (clean) after four fix iterations: a `prod_le_prod` signature mismatch, the missing `NormOneClass ℝ` import, no `degreeOf_map_le` in mathlib (used `degrees_map_of_injective`), and `Finset.norm_prod_le` needing `NormedCommRing` rather than `SeminormedCommRing`. Contents: (1) `norm_eval_le` over `[NormedCommRing R] [NormOneClass R]`; (2) the project statement recovered from (1); (3) a sanity check that `Roth.abs_eval_le` elaborates.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries and mathlib greps as recorded in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.1546–1568.
- Project greps: `grep -rn abs_eval_le Roth/` (call site); inline-derivation grep for `abs_sum_le_sum_abs` and `eval_eq'`.
