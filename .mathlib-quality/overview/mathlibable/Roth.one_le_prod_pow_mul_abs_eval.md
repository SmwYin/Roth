---
decl: Roth.one_le_prod_pow_mul_abs_eval
file: Roth/Main.lean
line: 324
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multivariate Liouville clearing-denominators bound (product of q_j^(r_j) times the absolute value of Q(h/q) is at least 1); mathlib has only the univariate one_le_pow_mul_abs_eval_div in Mathlib/Algebra/Polynomial/DenomsClearable.lean, and the project proof compiles verbatim over any Fintype sigma, any linearly ordered field K and integer denominators.
action: Ship MvPolynomial.one_le_prod_pow_mul_abs_eval_div over [Fintype σ] [Field K] [LinearOrder K] [IsStrictOrderedRing K] with q : σ → ℤ (compiled in evidence/Roth.one_le_prod_pow_mul_abs_eval/general.lean) as the multivariate sibling of one_le_pow_mul_abs_eval_div, optionally with the integrality statement split out; keep the Fin m / ℝ form for the single caller Roth/Main.lean:476 or derive it from the general lemma.
---

# Roth.one_le_prod_pow_mul_abs_eval

## Inventory entry

### `theorem Roth.one_le_prod_pow_mul_abs_eval`
- **Type**: `{m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ} (hQ : ∀ j, degreeOf j Q ≤ r j) (h : Fin m → ℤ) {q : Fin m → ℕ} (hq : ∀ j, 0 < q j) (hne : eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) : 1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)|`
- **What**: If an integer polynomial `Q` in `m` variables has degree at most `r_j` in `x_j` and does not vanish at the rational point `(h_1/q_1, …, h_m/q_m)`, then `(∏_j q_j^{r_j}) |Q(h/q)| ≥ 1`.
- **How**: Defines the explicit integer `N = ∑_{d ∈ supp Q} a_d ∏_j h_j^{d_j} q_j^{r_j - d_j}`; proves `(N : ℝ) = (∏ q_j^{r_j}) Q(h/q)` via `MvPolynomial.eval_eq'`, `support_map_of_injective`, `Finset.mul_sum`, `Finset.prod_mul_distrib`, `pow_sub_mul_pow` with `monomial_le_degreeOf`, `div_pow`, `mul_div_cancel₀`; then `Int.one_le_abs` on the nonzero integer `N`, `abs_mul`, `abs_of_pos`.
- **Hypotheses**: `hQ` (partial degree bounds), `hq` (positive denominators), `hne` (non-vanishing at the rational point).
- **Uses from project**: `[]` (only mathlib: `MvPolynomial.eval_eq'`, `MvPolynomial.support_map_of_injective`, `MvPolynomial.coeff_map`, `MvPolynomial.monomial_le_degreeOf`, `pow_sub_mul_pow`, `Int.one_le_abs`, `Finset.prod_pos`)
- **Used by**: Roth/Main.lean:476 (inside the Lemma 9 / eq. (54) contradiction step of the main argument: `(one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne).trans_lt ...`); also mentioned in the Main.lean module docstring (line 38).
- **Visibility**: public
- **Lines**: 319–347 (docstring 319–323, statement 324–327), proof length 20 lines
- **Notes**: Source: clean.tex §7 l.1646–1653, eq. (54). Direct multivariate analogue of mathlib's `one_le_pow_mul_abs_eval_div`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Main.lean:476.
- Wrapper of 1–2 mathlib calls? No: a 20-line proof constructing the cleared integer and identifying it with the scaled evaluation.
- Does mathlib have it? Only the univariate version `one_le_pow_mul_abs_eval_div` (Mathlib/Algebra/Polynomial/DenomsClearable.lean:86, single denominator `b`, `natDegree`). No `MvPolynomial` analogue (grep, Loogle, LeanSearch, Lean-Finder).
- Too specific / inline? It is the named step (54) of the paper and a standard Liouville-type fact; inlining would bury a 20-line proof in the main argument.
- Well-chosen? Yes, modulo `Fin m` / `ℝ` / `ℕ`-denominator specialisations (see Phase 4).
- Conclusion: `KEEP`. Action: keep; restate as (or derive from) the general multivariate lemma.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.one_le_prod_pow_mul_abs_eval` absent from mathlib (grep `one_le_prod_pow`, `prod_pow_mul_abs_eval` over `.lake/packages/mathlib/Mathlib/`: no hits). Not a glue lemma. Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file compiles with no errors)
- decl `Roth.one_le_prod_pow_mul_abs_eval`:  resolved at Roth/Main.lean:324
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Proof of Roth's theorem from the main lemma (Lemma 9): choice of approximations, degrees, and the final contradiction.

### Statement (Phase 1)

`Roth.one_le_prod_pow_mul_abs_eval` is a theorem stating the following: let `Q ∈ ℤ[x_1, …, x_m]` have degree at most `r_j` in `x_j`, and let `h_j/q_j` be rationals with `q_j > 0`. If `Q(h_1/q_1, …, h_m/q_m) ≠ 0`, then `(∏_j q_j^{r_j}) Q(h/q)` is a nonzero integer, hence `|Q(h/q)| ≥ ∏_j q_j^{-r_j}`.

Variables / typeclasses involved (Lean side):
- `m : ℕ`, variables indexed by `Fin m`.
- `Q : MvPolynomial (Fin m) ℤ`, evaluated after `map (Int.castRingHom ℝ)`.
- `r : Fin m → ℕ` — partial degree bounds; `h : Fin m → ℤ` numerators; `q : Fin m → ℕ` denominators.

Hypotheses (Lean side):
- `hQ : ∀ j, degreeOf j Q ≤ r j`.
- `hq : ∀ j, 0 < q j`.
- `hne : Q(h/q) ≠ 0` (in `ℝ`).

Conclusion (math): `1 ≤ (∏_j q_j^{r_j}) |Q(h/q)|`.

Conclusion (Lean): `1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)|`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-step Liouville-type helper used once; not a main result and not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 20 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate polynomial integer coefficients evaluated at rational point clearing denominators product q_j^{r_j} nonzero integer at least 1 Roth's theorem | partial | Roth-proof expositions (arXiv 2502.00731, math/9708214) use `(∏ q_j^{r_j}) Q(h/q) ∈ ℤ∖{0}` silently | routine step, never a named lemma |
| 2 | WebSearch (general form) | Liouville inequality polynomial value at rational number denominator power b^n f(a/b) ≥ 1 several variables | yes | univariate `b^d |f(a/b)| ≥ 1`; multivariate Liouville inequality `|P(γ)| ≥ …` in terms of partial degrees and heights (Waldschmidt, Ottawa summer school notes ch. 3) | the rational-point case is the trivial denominator-clearing instance |
| 3 | WebSearch (named-after / aliases) | "Liouville's inequality" height polynomial nonzero algebraic number lower bound product formula multivariate | yes | Liouville inequality for multivariate polynomials at algebraic points (Waldschmidt; Bombieri–Gubler); multivariate Liouville (alg-geom/9608010) | general algebraic-point form needs heights / product formula |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` l.1646–1653, eq. (54) | yes | "`(∏_j q_j^{r_j}) Q(h/q)` is a nonzero integer ... absolute value at least 1" | exactly the project statement |
| 6 | nLab | Liouville number / polynomial evaluation | no | — | no Diophantine-inequality content |
| 7 | nCatLab | — | n/a | — | not a categorical statement (elementary integrality estimate) |
| 8 | Stacks Project | — | n/a | — | no archimedean estimates in Stacks |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | partial | folklore "nonzero integer has absolute value ≥ 1" applied after clearing denominators | stated in passing |
| 10 | recent arXiv (last 5 years) | (results of #1) | partial | arXiv 2502.00731 (2025) follows Bombieri–Gubler Ch. 6 | used silently |

### Literature summary (Phase 3)

Concept identified as: Liouville's inequality at a rational point (the "a nonzero integer has absolute value at least 1" step after clearing denominators), multivariate version with per-variable denominators.
Sources agree on the standard form: yes: if `deg_{x_j} Q ≤ r_j` and `Q(h/q) ≠ 0` then `|Q(h/q)| ≥ ∏_j q_j^{-r_j}`.
Most general standard form: `Q ∈ ℤ[x_σ]` for a finite variable set, integer (or nonzero-integer with absolute values) denominators, value taken in any ordered field (the integer `N` lives in `ℤ`; only the embedding `ℤ → K` and `|·|` are needed). The algebraic-point generalisation (Liouville inequality with heights) is a genuinely different theorem.
Generality dimensions where the literature varies:
  - variable index: `m` variables (here `Fin m`) to any finite set.
  - target field: `ℝ` here to any linearly ordered field (mathlib's univariate version already uses arbitrary `K`).
  - denominators: positive naturals here to positive integers (mathlib univariate: `0 < b` in `ℤ`).
  - point: rational (here) vs algebraic (needs heights; separate theorem).
Disagreement with the literature: none.

### Generality analysis — `Roth.one_le_prod_pow_mul_abs_eval`

Literature-standard form (from Phase 3): for `[Fintype σ]`, `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, `Q : MvPolynomial σ ℤ`, `h q : σ → ℤ`, `0 < q j`: `1 ≤ (∏ j, (q j : K) ^ r j) * |Q(h/q)|`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | variable index `Fin m` | `Fin m` | any `[Fintype σ]` | yes | proof uses only finiteness of the product; verified (evidence (1)) |
| 2 | target `ℝ` | `ℝ` | `[Field K] [LinearOrder K] [IsStrictOrderedRing K]` | yes | proof uses only `Int.cast`, division, `abs`, positivity; verified (evidence (1)); matches mathlib's univariate `K` |
| 3 | denominators `q : Fin m → ℕ` | `ℕ`, `0 < q j` | `ℤ`, `0 < q j` | yes | integer denominators match mathlib's `one_le_pow_mul_abs_eval_div`; verified (evidence (1)); the `ℕ` form recovered (evidence (2)) |
| 4 | `hQ` partial degrees | `degreeOf j Q ≤ r j` | same | no | essential: needed for `r j - d j` to be a genuine exponent |
| 5 | `hq` positivity | `0 < q j` | `q j ≠ 0` with `|q j|` in the product | marginal | with `q j ≠ 0` one needs `∏ |q j|^{r j}`; positivity is the mathlib univariate convention, kept |
| 6 | `hne` | nonvanishing | same | no | essential (the integer must be nonzero) |
| 7 | coefficients `ℤ` | `ℤ` | `ℤ` (or a subring of integers with `1 ≤ |n|` for `n ≠ 0`) | no (standard) | the bound `1 ≤ |N|` is specific to `ℤ`; a general "discrete subring" form is not standard |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (rows 1–3), all compiled together in one evidence file (`lake env lean`: no errors; only the `#check` info line).
Proposed restatement:

```lean
theorem MvPolynomial.one_le_prod_pow_mul_abs_eval_div {σ K : Type*} [Fintype σ] [Field K]
    [LinearOrder K] [IsStrictOrderedRing K] (Q : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h q : σ → ℤ) (hq : ∀ j, 0 < q j)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : K) ^ r j) * |eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)|
```

Cost of restatement: CHEAP — the project proof compiles verbatim after replacing `ℝ` by `K` and `(q j : ℤ)` casts (evidence (1)).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | hypotheses are genuine data conditions |
| 2 | sequences to filters? | no | — | finite inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `ℝ` to any linearly ordered field `K` | matches `one_le_pow_mul_abs_eval_div`'s generality; usable over `ℚ` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `Fin m` to `[Fintype σ]`; `ℕ` denominators to `ℤ` | composes with `MvPolynomial σ` API without reindexing |
| 8 | concrete-via-abstract? | no | no named concrete object; the proof is already about an arbitrary polynomial | — |
| 9 | false-generalisation guard | no false generalisation | the original statement is recovered from (1) with `σ = Fin m`, `K = ℝ`, `q := (q · : ℤ)` (compiled, evidence (2)) | — |

Optional companion (not compiled): split out the integrality statement `∃ N : ℤ, (N : K) = (∏ j, (q j : K) ^ r j) * eval (h/q) (map _ Q)`, the multivariate analogue of `denomsClearable_of_natDegree_le`, which also serves algebraic-point / non-archimedean uses.

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the 4b signature (same as the literature form).
  - Cost: CHEAP
  - Mathlib downstream this enables: multivariate sibling of `one_le_pow_mul_abs_eval_div` (Liouville file); lower bounds for auxiliary polynomials in Thue–Siegel–Roth-type arguments; works over `ℚ` and `ℝ` alike.
  - Real mathematical improvement: removes the `Fin m`/`ℝ`/`ℕ` specialisations so the lemma is the exact multivariate analogue of the existing mathlib univariate lemma.

### Proof strategy — `Roth.one_le_prod_pow_mul_abs_eval`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partly | a multivariate `DenomsClearable`-style integrality lemma would make the proof two lines (integer exists, then `Int.one_le_abs`) | CHEAP (the `hNeq` block is that lemma) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (explicit cleared integer via `eval_eq'`, then `Int.one_le_abs`); more direct than the univariate mathlib proof, which goes through the `DenomsClearable` induction.
  - Missing mathlib API (if any): optional multivariate integrality lemma (the `hNeq` step), see Phase 4c companion.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.one_le_prod_pow_mul_abs_eval`

[A] Lean-Finder       "clearing denominators: product of q_j^r_j times Q(h_1/q_1,...,h_m/q_m) is an integer for MvPolynomial with degreeOf j Q ≤ r j"   hits: `DenomsClearable`, `denomsClearable_of_natDegree_le`, `denomsClearable_natDegree`, `denomsClearable_C_mul_X_pow` (all univariate `Polynomial`)
[B] Loogle            `MvPolynomial.eval, MvPolynomial.degreeOf, |_|`   no hits
[C] LeanSearch        "multivariate polynomial with integer coefficients evaluated at rational point times product of denominators powers is at least one in absolute value"   hits: `one_le_pow_mul_abs_eval_div` (univariate), `Polynomial.one_le_mahlerMeasure_of_ne_zero` (unrelated)
[D] Grep mathlib src  `one_le_prod_pow`, `prod_pow_mul_abs_eval`, `DenomsClearable`, `Int.one_le_abs`, `MvPolynomial` under NumberTheory   hits: `one_le_pow_mul_abs_eval_div` (Mathlib/Algebra/Polynomial/DenomsClearable.lean:86), used in Mathlib/NumberTheory/Transcendental/Liouville/Basic.lean; `Int.one_le_abs` used ad hoc in SiegelsLemma, ModularForms; no MvPolynomial analogue
[E] Name pattern      `MvPolynomial.eval_eq'`, `MvPolynomial.monomial_le_degreeOf`, `MvPolynomial.support_map_of_injective`, `pow_sub_mul_pow`, `Int.one_le_abs`   hits (building blocks, used in the evidence)

Searched for both the user's form (`Fin m`, `ℝ`) and the literature-standard form (`Fintype σ`, ordered field `K`).

Concluded: found a partial match (`one_le_pow_mul_abs_eval_div`); it covers only the univariate single-denominator case; otherwise building blocks only.

### Normal-form check — `Roth.one_le_prod_pow_mul_abs_eval`

Equivalent formalisms: (a) `1 ≤ (∏ q_j^{r_j}) |Q(h/q)|` (project, and mathlib univariate shape); (b) `(∏ q_j^{r_j})⁻¹ ≤ |Q(h/q)|`; (c) integrality `∃ N : ℤ, N ≠ 0 ∧ (N : K) = (∏ q_j^{r_j}) Q(h/q)`.
Does mathlib already have a canonical form for this idea? Yes for one variable: form (a) in `one_le_pow_mul_abs_eval_div`.
Is our statement stated against the canonical form? Yes, form (a).
RHS convention respected? yes (inequality, scaled quantity on the RHS).

### Syntactic generality — `Roth.one_le_prod_pow_mul_abs_eval`

Alternative restatements attempted:
- general form over `Fintype σ`, ordered field `K`, `q : σ → ℤ` (compiles; evidence (1))
- project form recovered from it (compiles; evidence (2))
Chosen restatement: general form (a).
Justification: matches the existing mathlib univariate lemma's shape and generality, so users of both see one API; the caller needs only `simpa` to pass from `ℕ` to `ℤ` denominators.

### Superfluous-argument audit — `Roth.one_le_prod_pow_mul_abs_eval`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `Fin m` index | no | any finite type (evidence (1)) |
| 2 | `ℝ` target | no | any linearly ordered field (evidence (1)) |
| 3 | `ℕ`-valued `q` | no | `ℤ` with positivity (evidence (1)) |
| 4 | `hQ` | yes | exponents `r j - d j` |
| 5 | `hq` | yes | nonzero denominators and positivity of the product |
| 6 | `hne` | yes | nonzero integer |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (general form in 4b)
Superfluous arguments: 3 specialisations to drop (`Fin m`, `ℝ`, `ℕ` denominators)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.one_le_prod_pow_mul_abs_eval`

Internal use count: 0 outside the declaring file (1 in the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:476 (main contradiction, Lemma 9 / eq. (54)) | `exact (one_le_prod_pow_mul_abs_eval Q hQd h hq0 hne).trans_lt (mul_lt_mul_of_pos_left (abs_eval_lt_of_le_index ...) ...)` |

Inline-derivation grep (`Int.one_le_abs`, `eval_eq'` over `Roth/`):
  - (none) — no other site re-derives the cleared-integer bound.

### Composition check (Phase 6)

Can the statement be derived from mathlib in ≤3 chained calls?

Attempt 1: `one_le_pow_mul_abs_eval_div`
  - Mathlib decls used: `one_le_pow_mul_abs_eval_div`
  - Result: fails — univariate only; reducing a multivariate polynomial with different denominators per variable to one variable (e.g. substitution `x_j = h_j t / q_j`) is not a composition and loses the per-variable degree bookkeeping.
Attempt 2: `MvPolynomial.eval_eq'` + termwise cancellation + `Int.one_le_abs`
  - Mathlib decls used: `MvPolynomial.eval_eq'`, `MvPolynomial.support_map_of_injective`, `MvPolynomial.coeff_map`, `MvPolynomial.monomial_le_degreeOf`, `pow_sub_mul_pow`, `div_pow`, `mul_div_cancel₀`, `Int.one_le_abs`
  - Result: succeeds only as the 20-line proof (explicit integer, sum/product manipulation, then the integer bound).
Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.one_le_prod_pow_mul_abs_eval`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the multivariate Liouville bound at a rational point is standard (clean.tex eq. (54); Roth-proof expositions; special case of the multivariate Liouville inequality); natural generality is any finite variable set and any ordered field.
- Generality analysis (Phase 4): STRICTLY NARROWER; three specialisations dropped, compiled clean.
- Mathlib search (Phase 5): only the univariate `one_le_pow_mul_abs_eval_div`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The specific gap: Mathlib/Algebra/Polynomial/DenomsClearable.lean provides the univariate Liouville clearing step `one_le_pow_mul_abs_eval_div` (`1 ≤ b ^ natDegree f * |f(a/b)|`), used for Liouville's theorem, but there is no `MvPolynomial` analogue with per-variable denominators and partial degrees. That multivariate form is exactly what Thue–Siegel–Roth-type arguments (and the multivariate Liouville inequality) need, and it is not a composition of the univariate lemma. The lemma composes with mathlib's `degreeOf` API (`degreeOf_mul_le`, `degreeOf_sum_le`) and with `MvPolynomial.eval_eq'`.

The project form specialises three inessential parameters (`Fin m`, `ℝ`, `ℕ` denominators); the identical proof compiles over `[Fintype σ]`, any linearly ordered field `K` and `q : σ → ℤ`, mirroring the univariate lemma's generality, and the project statement is recovered by `simpa`. The single-caller status (K = 1) is not an argument against: the lemma fills an evident gap beside an existing mathlib lemma.

Reason for the generalisation: LITERATURE-WEAKENING (index type, target field, denominator type) plus MODERN-IDIOM (match the existing univariate mathlib API).
Proposed restatement:
```lean
theorem MvPolynomial.one_le_prod_pow_mul_abs_eval_div {σ K : Type*} [Fintype σ] [Field K]
    [LinearOrder K] [IsStrictOrderedRing K] (Q : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h q : σ → ℤ) (hq : ∀ j, 0 < q j)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : K) ^ r j) * |eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)|
```
Estimated cost of regeneralisation: CHEAP (compiled in evidence).
Mathlib downstream this enables: multivariate Liouville-type lower bounds next to `one_le_pow_mul_abs_eval_div`; the auxiliary-polynomial non-vanishing step of Roth / Thue–Siegel / Schmidt subspace proofs; an optional integrality companion (multivariate `DenomsClearable`).
Proposed mathlib location: a new section in Mathlib/Algebra/Polynomial/DenomsClearable.lean would need an `MvPolynomial` import; more natural is an MvPolynomial file (e.g. Mathlib/Algebra/MvPolynomial/DenomsClearable.lean or next to Mathlib/NumberTheory/Transcendental/Liouville/Basic.lean).
PR grouping: alone or with the integrality companion; independent of other Roth PRs.
Local refactor: keep `Roth.one_le_prod_pow_mul_abs_eval` for Roth/Main.lean:476 as the `σ = Fin m`, `K = ℝ` instance (one-line `simpa` from the general lemma, evidence (2)).
Next action: run `/generalise Roth.one_le_prod_pow_mul_abs_eval` targeting the 4b signature (decide on the integrality companion), then `/cleanup` and `/pre-submit`.

---

## Next step

Ship `MvPolynomial.one_le_prod_pow_mul_abs_eval_div` over `[Fintype σ]`, a linearly ordered field `K` and integer denominators as the multivariate sibling of `one_le_pow_mul_abs_eval_div`; derive the project form for Roth/Main.lean:476 from it.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.one_le_prod_pow_mul_abs_eval/general.lean` (`import Mathlib`). Final `lake env lean`: no errors (only the `#check` info output). Two earlier runs failed only in the comparison block (3): a universe-level inference error on `have := @one_le_pow_mul_abs_eval_div`, then a docstring placed before `#check`; both fixed. Contents: (1) the general lemma over `[Fintype σ]`, ordered field `K`, `q : σ → ℤ` (project proof verbatim); (2) the project statement recovered from (1); (3) `#check` of mathlib's univariate `one_le_pow_mul_abs_eval_div`.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries and mathlib greps as recorded in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.1646–1653.
- Project greps: `grep -rn one_le_prod_pow_mul_abs_eval Roth/` (call site Main.lean:476, docstring Main.lean:38).
