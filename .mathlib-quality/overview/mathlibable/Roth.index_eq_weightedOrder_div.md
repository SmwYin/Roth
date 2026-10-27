---
decl: Roth.index_eq_weightedOrder_div
file: Roth/Index.lean
line: 143
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The bridge index = toNat(weightedOrder_w (taylor α P))/∏r with w_j = ∏r/r_j is the project def Roth.index read through MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder and weightedOrder_le after the project rescaling weight_eq_finsuppWeight_div; it is about a project-only def so nothing goes upstream; hP is superfluous (compiled) and hr is necessary (compiled counterexample).
action: Keep locally as the bridge used by index_mul (Roth/Index.lean:164-165); drop the superfluous hP (proof - case split P = 0 with simp [index]) and simplify the three call sites in index_mul accordingly; do not upstream.
---

# Roth.index_eq_weightedOrder_div

## Inventory entry

### `theorem Roth.index_eq_weightedOrder_div`
- **Type**: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r = (((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j ↦ (∏ i, r i) / r j).toNat : ℝ) / ∏ i, r i`
- **What**: For positive integer parameters `r`, the Roth index of `P` at `α` equals the weighted order of the Taylor translate `P(X + α)` (as a power series) with natural weights `w_j = D / r_j`, `D = ∏ r_j`, divided by `D`.
- **How**: Obtains a coefficient `d` attaining the weighted order (`MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, finiteness from `MvPowerSeries.ne_zero_iff_weightedOrder_finite`); `≤` by `index_le_weight` at `d` after rewriting `weight` via `weight_eq_finsuppWeight_div`; `≥` by `le_index_iff`, `div_le_div_of_nonneg_right`, `ENat.toNat_le_toNat` and `MvPowerSeries.weightedOrder_le`; coefficients identified via `MvPolynomial.coeff_coe` and `coeff_taylor`.
- **Hypotheses**: `hP : P ≠ 0` (superfluous, evidence (1)); `hr : ∀ j, 0 < r j` (necessary, evidence (2)).
- **Uses from project**: `Roth.index`, `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`, `Roth.weight_eq_finsuppWeight_div`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight` (via the rewrite).
- **Used by**: Roth/Index.lean:164, 165 (`index_mul`, three rewrites); mentioned in the module docstring Roth/Index.lean:38. No other file.
- **Visibility**: public
- **Lines**: 139–158, proof length 13 lines
- **Notes**: Formalises the paper's Lean implementation note (clean.tex §4, "use the natural weights `w_j = D/r_j` in `MvPowerSeries.weightedOrder`, then divide the finite value by `D`"). The `hP` hypothesis is superfluous as stated by the Roth.index report; verified independently here.

## Junk check (Step 8)
- Used anywhere? Yes, by `index_mul` (the only route to multiplicativity of the index, via `MvPowerSeries.weightedOrder_mul`), which in turn feeds `index_prod` and the Theta/MainLemma development.
- Wrapper of 1–2 mathlib calls? No: a 13-line two-sided argument combining two mathlib lemmas with three project lemmas.
- Does mathlib have it? No: `Roth.index` and `MvPolynomial.taylor` are project defs; mathlib has no weighted order for `MvPolynomial` or at a point.
- Too specific (inline)? No: it is the bridge that makes mathlib's `weightedOrder` API available for the index; inlining would duplicate 13 lines.
- Well-chosen? Yes, except that `hP` is superfluous (evidence (1)).
- Conclusion: `KEEP`. Action: drop `hP` and simplify the call sites in `index_mul`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring not internal/auxiliary; Step 8 KEEP; no `namespace Roth` in mathlib, so the qualified name is absent. Not a glue lemma (13-line proof). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Index` elaborates with no diagnostics)
- decl `Roth.index_eq_weightedOrder_div`: resolved at Roth/Index.lean:143
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_eq_weightedOrder_div` is a theorem stating the following:

Let `P ∈ ℝ[X_j : j ∈ σ]` (σ finite), `α ∈ ℝ^σ`, and `r_j` positive integers. Put `D = ∏ r_j` and `w_j = D / r_j ∈ ℕ`. Then the index `ind_{α,r}(P) = min { ∑ d_j / r_j : (Δ_d P)(α) ≠ 0 }` equals `ord_w(P(X + α)) / D`, where `ord_w` is the `w`-weighted order of a power series (minimum `∑ w_j d_j` over nonzero coefficients).

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables; `P`: the polynomial; `α`: the point; `r`: integer parameters.

Hypotheses (Lean side):
- `hP : P ≠ 0`: excludes the zero polynomial (not needed, see 4b).
- `hr : ∀ j, 0 < r j`: makes `D ≠ 0` and `w_j = D/r_j` exact.

Conclusion (math): `ind(P) = ord_w(P_α)/D`.

Conclusion (Lean): `index P α r = ((weightedOrder w ↑(taylor α P)).toNat : ℝ) / ∏ i, r i`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a bridge lemma between a project definition and a mathlib definition; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 13 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of polynomial at a point weights r_j minimum sum i_j/r_j | yes | index = min of sum i_h/r_h over nonvanishing derivatives / over nonzero Taylor coefficients at the point | arXiv 2502.00731, math/0307203, Ru's notes (uh.edu); always real-valued with weights 1/r_j, never via an integer weighted order |
| 2 | WebSearch (general form) | weighted order of vanishing multivariate polynomial at a point weighted degree lowest term Taylor expansion | yes | weighted order = min weighted exponent sum over monomials (rational weights allowed) | arXiv 2604.16698 (weighted blowups) uses rational weights directly; Hasse-derivative Taylor expansion in arXiv 1310.6482 |
| 3 | WebSearch (aliases / rescaling) | quasi-homogeneous weighted order rational weights rescale integer weights multivariate power series order | yes | rational weights rescaled to integers by multiplying by a common denominator | Wikipedia "Quasi-homogeneous polynomial", Brzostowski–Krasiński; the rescaling is folklore; mathlib doc page for MvPowerSeries.Order surfaced |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for weightedOrder / natural weights | yes | clean.tex §4 Lean note lines 547–556: for positive integral r_j use natural weights w_j = D/r_j in MvPowerSeries.weightedOrder and divide by D | the lemma is exactly this implementation note |
| 6 | nLab | weighted order / index of a polynomial | no | n/a | no nLab page on weighted order of vanishing; elementary commutative algebra |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing / weighted | no | n/a | Stacks treats orders of vanishing of divisors (valuations), not weighted multi-index orders of polynomials |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread on this rescaling identity; it is a routine denominator-clearing step |
| 10 | recent arXiv | weighted blowups order (2604.16698), Roth subspace (2502.00731) | yes | rational weighted orders used directly | confirms literature never needs the integer rescaling |

### Literature summary (Phase 3)

Concept identified as: the Roth index (weighted order of vanishing at a point) and its rescaling to an integer-weighted order.
Sources agree on the standard form: yes — index is a minimum of `∑ d_j/r_j` over nonzero Taylor coefficients.
Most general standard form: weighted order with arbitrary positive real (or rational) weights; for rational weights it equals an integer-weighted order divided by a common denominator.
Generality dimensions where the literature varies:
  - weights: real positive (Roth) vs integer (mathlib `weightedOrder`); the bridge is the denominator-clearing identity.
  - common denominator: any nonzero common multiple of the `r_j` works, `D = ∏ r_j` is one choice (see Roth.weight_eq_finsuppWeight_div report).
Disagreement with the literature: none; the lemma is a formalisation device rather than a literature statement.

### Generality analysis — `Roth.index_eq_weightedOrder_div`

Literature-standard form: `ind_{α,r}(P) = ord_w(P_α)/D` for any nonzero common multiple `D` of the `r_j`, `w_j = D/r_j`, all `P` (with the `ℕ∞ → ℕ` truncation making `P = 0` give `0`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | required | none | yes | evidence (1): `P = 0` gives `sInf ∅ = 0` and `(⊤).toNat = 0`; compiled |
| 2 | `hr : ∀ j, 0 < r j` | required | positive integers | NO | evidence (2): `σ = Bool`, `r = (1, 0)`, `P = X true`, `α = 0` gives LHS `1`, RHS `0`; compiled |
| 3 | `D = ∏ r_j` | fixed | any nonzero common multiple | yes (cosmetic) | would require generalising `weight_eq_finsuppWeight_div` first (that report's `_of_dvd` form); no call site needs it |
| 4 | ring `ℝ` | fixed | any field / comm ring for the ℕ∞ form | not for this statement | `Roth.index` is defined only over `ℝ` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (by one superfluous hypothesis)
Number of weakening opportunities found: 1 verified (`hP`), 1 cosmetic unverified-and-unneeded (general `D`)
Proposed restatement: `theorem index_eq_weightedOrder_div (P : MvPolynomial σ ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r = ... ` — compiled as `Roth.Evidence.index_eq_weightedOrder_div_noHP` (proof: `rcases eq_or_ne P 0 with rfl | hP; · simp [index]; · exact index_eq_weightedOrder_div hP hr α`).
Cost of restatement: CHEAP — mechanical rewrite.

(This is a local cleanup; it does not make the lemma a mathlib candidate, since its subject `Roth.index` is not in mathlib.)

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | positivity of `r` is data-level | — |
| 2 | Sequences vs filters? | no | finite algebraic statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | `index` is ℝ-valued by design over ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `ℕ` weights are what `weightedOrder` takes | — |
| 8 | Concrete-via-abstract? | no | the proof uses `index`-specific API (`index_le_weight`, `le_index_iff`) throughout | — |
| 9 | False-generalisation guard | no false generalisation | dropping `hP` keeps the same statement for `P ≠ 0` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: the lemma is itself the translation of the project's real-valued index into mathlib's modern `MvPowerSeries.weightedOrder` idiom; the idiom-level content (weighted order of a power series) is already in mathlib.

### Proof strategy — `Roth.index_eq_weightedOrder_div`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (minor) | a lemma `MvPolynomial` weighted order = min of `Finsupp.weight` over support (coercion to power series) would shorten both directions; also `MvPowerSeries.weightedOrder_eq_nat` could replace the two-sided argument | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (two-sided bound via attainment + `weightedOrder_le`, the standard shape)
  - Missing mathlib API: no `MvPolynomial`-level weighted order (already noted in Roth.index report as a possible upstream target); not blocking.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_eq_weightedOrder_div`

[A] Lean-Finder       "weightedOrder of a multivariate polynomial as power series is the minimum of the weights of monomials in its support"   hits: `MvPowerSeries.weightedOrder`, `weightedOrder_le`, `weightedOrder_monomial`, `weightedOrder_eq_nat` (building blocks only)
[B] Loogle            `MvPowerSeries.weightedOrder, MvPolynomial.coeToMvPowerSeries`   no hits (no lemma relating the two)
[C] LeanSearch        "weighted order of multivariate polynomial coerced to power series equals minimum weight of support"   hits: `weightedOrder`, `le_weightedOrder`, `weightedOrder_eq_nat`, `weightedOrder_le` (building blocks)
[D] Grep mathlib src  `weightedOrder` (files: MvPowerSeries/Order, NoZeroDivisors, PiTopology, Substitution; PowerSeries/Substitution), `MvPolynomial.*weightedOrder`, `weightedOrder_coe`   no polynomial-level or at-a-point result
[E] Name pattern      `index_eq_weightedOrder`, `Roth` namespace   no hits in mathlib

Searched for both:
  - the user's current form (index as weighted order / D)
  - the literature-standard form (weighted order of a polynomial at a point with rational weights)

Concluded: found building blocks (`MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.ne_zero_iff_weightedOrder_finite`, `MvPowerSeries.weightedOrder_le`, `MvPolynomial.coeff_coe`, `ENat.toNat_le_toNat`); composition with the project lemmas `weight_eq_finsuppWeight_div`, `index_le_weight`, `le_index_iff`, `coeff_taylor` yields our form.

### Normal-form check — `Roth.index_eq_weightedOrder_div`

Equivalent formalisms: (a) index as `sInf` of real weights (project def); (b) `weightedOrder`/D (this lemma); (c) a hypothetical `ℕ∞`-valued `MvPolynomial` weighted order at a point.
Does mathlib already have a canonical form? yes — `MvPowerSeries.weightedOrder` for the order itself.
Our statement is `project_def = expression in the canonical form`, i.e. `X ↔ canonical` shape, with the canonical form on the RHS. OK.
RHS convention respected? yes

### Syntactic generality — `Roth.index_eq_weightedOrder_div`

Alternative restatements attempted:
- current (with `hP`)
- without `hP` (evidence (1))
- multiplied out: `index P α r * ∏ r = toNat(...)` (avoids division; not better for `index_mul`, which uses `← add_div`)

Chosen restatement: without `hP`, division form.
Justification: the division form is what `index_mul` rewrites with (`← add_div`); dropping `hP` removes three side-goals (`hP`, `hQ`, `mul_ne_zero hP hQ`) at the rewrite sites.

### Superfluous-argument audit — `Roth.index_eq_weightedOrder_div`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `Roth.weight` and `∏ i, r i` |
| 2 | `hP : P ≠ 0` | no | evidence (1), compiled |
| 3 | `hr : ∀ j, 0 < r j` | yes | evidence (2), compiled counterexample |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (drop `hP`)
Superfluous arguments: 1 to drop (`hP`)

Overall: RESTATE-BEFORE-SHIP (locally; not a mathlib candidate)

### Call sites — `Roth.index_eq_weightedOrder_div`

Internal use count: 0 outside the declaring file (3 rewrites inside Roth/Index.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:164 | `rw [index_eq_weightedOrder_div hP hr, index_eq_weightedOrder_div hQ hr,` (in `index_mul`) |
| Roth/Index.lean:165 | `index_eq_weightedOrder_div (mul_ne_zero hP hQ) hr, ← add_div, map_mul, ...` (in `index_mul`) |
| Roth/Index.lean:38 | module docstring entry |

Inline-derivation grep:
  - (none) — no other site re-derives the `weightedOrder` form; `index_prod` goes through `index_mul`.

### Composition check (Phase 6)

Can `Roth.index_eq_weightedOrder_div` be derived from mathlib in ≤3 chained calls?

Attempt 1: `le_antisymm` of (`index_le_weight` at the `d` from `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`) and (`le_index_iff` + `MvPowerSeries.weightedOrder_le`), both after `weight_eq_finsuppWeight_div`.
  - Mathlib decls used: `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.ne_zero_iff_weightedOrder_finite`, `MvPowerSeries.weightedOrder_le`, `MvPolynomial.coeff_coe`, `ENat.toNat_le_toNat`, `div_le_div_of_nonneg_right`.
  - Result: succeeds (it is the current proof), as a composition of two mathlib `weightedOrder` lemmas with the project's index API (`index_le_weight`, `le_index_iff`) and rescaling (`weight_eq_finsuppWeight_div`).
  - Notes: the mathematical content beyond mathlib is only the denominator-clearing identity (assessed NO-composable in Roth.weight_eq_finsuppWeight_div.md) and the definition of `Roth.index` (BORDERLINE, project-specific).

Attempt 2: `MvPowerSeries.weightedOrder_eq_nat` with `n` the attaining weight — same building blocks, packaged differently; no shorter.

Conclusion: COMPOSABLE (from mathlib's `weightedOrder` primitives plus the project's own index API; there is no residual statement for mathlib).

## Verdict: `Roth.index_eq_weightedOrder_div`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the identity is a formalisation device (clean.tex §4 Lean note); the literature works directly with rational weights.
- Generality analysis (Phase 4): STRICTLY NARROWER by the superfluous `hP` (compiled); `hr` necessary (compiled).
- Mathlib search (Phase 5): building blocks only (`MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `weightedOrder_le`, `ne_zero_iff_weightedOrder_finite`); no polynomial or at-a-point weighted order.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

The lemma is the translation of the project-specific real-valued `Roth.index` into mathlib's `MvPowerSeries.weightedOrder`. Its content is the attainment lemma `exists_coeff_ne_zero_and_weightedOrder` plus the lower bound `weightedOrder_le`, transported through the denominator-clearing identity `weight_eq_finsuppWeight_div`. Its subject `Roth.index` is not a mathlib notion: the Roth.index report rated it BORDERLINE, with a real-valued, Roth-specific form. So the lemma has no standalone place in mathlib. If a polynomial-level weighted order at a point were ever upstreamed, it would be defined directly in `ℕ∞` and this bridge would not be needed there.

The Roth.index report says `hP` is superfluous, and that is confirmed: at `P = 0` both sides are `0` (`sInf ∅ = 0`, `(⊤ : ℕ∞).toNat = 0`). Evidence (1) compiles this. Positivity of `r` is genuinely needed. Evidence (2) gives a compiled counterexample with one `r_j = 0`, where `D = 0` collapses the right-hand side to `0` while the index is `1`.

WHY not: mathlib has the `weightedOrder` building blocks and the lemma composes from them. Everything else is project API about a project def.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean as the bridge that gives `index_mul` access to `MvPowerSeries.weightedOrder_mul`.
Mathlib building blocks: `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.ne_zero_iff_weightedOrder_finite`, `MvPowerSeries.weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean:148,161,171), `MvPolynomial.coeff_coe`, `ENat.toNat_le_toNat`.
Composition sketch:
```lean
-- d from exists_coeff_ne_zero_and_weightedOrder; then
le_antisymm (index_le_weight hd ▸ weight_eq_finsuppWeight_div hr d)
  ((le_index_iff hP).2 fun e he ↦ by
    rw [weight_eq_finsuppWeight_div hr]; gcongr; exact ENat.toNat_le_toNat (weightedOrder_le w he) (by simp))
```
Call sites in our project (from Phase 6.0): 3 rewrites, all in `index_mul` (Roth/Index.lean:164–165).
Refactor plan: do not inline, because 13 lines repeated three times would be worse. Keep the lemma and drop `hP`, proving `P = 0` by `simp [index]` and otherwise using the current proof. In `index_mul`, change the rewrites to `index_eq_weightedOrder_div P hr α`-style calls with no nonzeroness arguments. `hP` and `hQ` are still needed there for `hfin` and `ENat.toNat_add`.
Next action: keep locally; apply the `hP` drop; do not upstream.

## Next step

Keep `Roth.index_eq_weightedOrder_div` in Roth/Index.lean. Drop its superfluous `hP` hypothesis, using evidence (1) as the proof template, and remove the `hP`/`hQ`/`mul_ne_zero` arguments at the three rewrites in `index_mul` (Roth/Index.lean:164–165). Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_eq_weightedOrder_div/weaken.lean` (imports `Roth.Index`; `lean_diagnostic_messages`: no diagnostics):
  - (1) `Roth.Evidence.index_eq_weightedOrder_div_noHP`: the statement without `hP`, compiled.
  - (2) an `example` showing that the statement fails for `σ = Bool`, `r = fun b ↦ if b then 1 else 0`, `P = X true`, `α = 0` (index `1`, RHS `0`), compiled. So `hr` is necessary.
- WebSearch ×3 (queries in the table); local grep of `.mathlib-quality/references/clean.tex`; Lean-Finder, LeanSearch, Loogle, and a grep of mathlib's `weightedOrder` files as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
