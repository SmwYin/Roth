---
decl: Roth.index_le_card
file: Roth/Index.lean
line: 224
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The bound ind(P; α; r) ≤ card σ when deg_{x_j} P ≤ r_j, about the project-only def Roth.index, is a 3-step chain (project exists_weight_eq_index, mathlib MvPolynomial.monomial_le_degreeOf with project degreeOf_taylor_le, project weight_le_card); hP is superfluous (index 0 = 0, compiled), hd is necessary (compiled counterexample), and nothing goes upstream.
action: Keep in Roth/Index.lean for its callers Roth/Theta.lean:91 and Roth/Theta.lean:117; optionally drop the superfluous hP (proof in evidence/Roth.index_le_card/hyps.lean), which removes the map_ne_zero_iff argument at both Theta call sites; do not upstream.
---

# Roth.index_le_card

## Inventory entry

### `theorem Roth.index_le_card`
- **Type**: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) : Roth.index P α r ≤ Fintype.card σ`
- **What**: If a real polynomial has degree at most `r j` in each variable `x_j`, then its Roth index at any point, with weights `r`, is at most the number of variables.
- **How**: `Roth.exists_weight_eq_index hP α r` gives a multi-index `d` with `(Δ_d P)(α) ≠ 0` whose weight is the index. The private `mem_support_taylor_iff` puts `d` in the support of `taylor α P`. Mathlib's `MvPolynomial.monomial_le_degreeOf` bounds `d j` by `degreeOf j (taylor α P)`. The project's `MvPolynomial.degreeOf_taylor_le` bounds that by `degreeOf j P`, and `hd j` bounds it by `r j`. Finally `Roth.weight_le_card` turns `d ≤ r` into `weight r d ≤ card σ`.
- **Hypotheses**: `hP : P ≠ 0` is superfluous, because `index 0 α r = sInf ∅ = 0` (evidence (1)). `hd` is necessary (evidence (3)). There is no positivity hypothesis on `r`; `r j = 0` forces `d j = 0` and the junk `0/0 = 0` term.
- **Uses from project**: `Roth.index`, `Roth.exists_weight_eq_index` (Roth/Index.lean:76), `Roth.mem_support_taylor_iff` (private, Roth/Index.lean:62), `MvPolynomial.taylor`, `MvPolynomial.degreeOf_taylor_le` (Roth/Taylor.lean:170), `Roth.weight_le_card` (Roth/Box.lean:103), `Roth.weight` (via the `hdw ▸`)
- **Used by**: Roth/Theta.lean:91 (`indexSet_bddAbove`) and Roth/Theta.lean:117 (`Θ_le_card`). Both have the same shape, `index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0) (by simpa [degreeOf, degrees_map_of_injective ...] using hRd) _`. There are no other uses (`grep -rn index_le_card Roth/`).
- **Visibility**: public
- **Lines**: 221-229 (docstring 221-223, statement 224-225, proof 226-229), proof length 4 lines
- **Notes**: Formalises the source's justification of `Θ_m ≤ m` (clean.tex:665-667, "Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, of weight at most `m`"). The source sets `ind(0) = +∞` (clean.tex:545), whereas Lean's junk value is `index 0 = 0`. Because of that junk value the Lean statement holds for `P = 0` as well.

## Junk check (Step 8)
- Used anywhere? Yes, at 2 sites in Roth/Theta.lean (lines 91 and 117).
- Wrapper of 1-2 mathlib calls? No. It chains three project lemmas (`exists_weight_eq_index`, `degreeOf_taylor_le`, `weight_le_card`) with one mathlib lemma (`monomial_le_degreeOf`).
- Does mathlib have it? No, because `Roth.index` is project-only. The nearest mathlib analogue is `MvPowerSeries.weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean:171). Mathlib has no "order is at most the (weighted) degree" lemma for polynomials, and no order at a point.
- Too specific (inline)? No. It is a named fact from the source with two identical call sites, and inlining would duplicate a 3-step chain.
- Well-chosen? Mostly. `hP` is superfluous (evidence (1)). Dropping it would let both Theta callers omit their `map_ne_zero_iff` argument.
- Conclusion: `KEEP`, optionally dropping `hP`.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The declaration is public.
- The name does not end `_aux`.
- The docstring does not start internal/auxiliary.
- Step 8 said KEEP.
- `Roth.index_le_card` is not in mathlib (there is no `namespace Roth` in `.lake/packages/mathlib/Mathlib/`). The only `index_le_card` hit is the unrelated `Subgroup.exists_index_le_card_of_leftCoset_cover`.

This is not a glue lemma, so it gets a full run. The parent `Roth.index` is BORDERLINE-needs-human rather than NO-mathlib-has-it, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief, and the evidence file importing `Roth.Index` elaborates with no diagnostics)
- decl `Roth.index_le_card`: resolved at Roth/Index.lean:224
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_le_card` is a theorem stating the following:

Let `P ∈ ℝ[x_j : j ∈ σ]` be nonzero with `deg_{x_j} P ≤ r_j` for every `j`, and let `α ∈ ℝ^σ`. Then `ind(P; α; r) ≤ |σ|`. The reason is that some Taylor coefficient of `P` at `α`, with multi-index `i`, is nonzero. Every such `i` satisfies `i_j ≤ r_j`, so `∑ i_j / r_j ≤ |σ|`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables, with `m = |σ|`.
- `P`: the polynomial.
- `r`: the weights / degree bounds.
- `α`: the point.

Hypotheses (Lean side):
- `hP : P ≠ 0`: the source hypothesis. It is superfluous in Lean.
- `hd : ∀ j, degreeOf j P ≤ r j`: the box condition.

Conclusion (math): the index is at most the number of variables.

Conclusion (Lean): `index P α r ≤ Fintype.card σ`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary bound on a project definition, used for the bounds `0 ≤ Θ_m ≤ m`. It is not a main result and is not named after anyone.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem index of polynomial at most number of variables degree at most r_j in each variable | partial | the index (min of `∑ j_i/r_i` over nonzero Taylor coefficients) for polynomials with `deg_{x_j} ≤ r_j` (arXiv math/0307203, arXiv 2502.00731, Evertse's Luminy slides) | the bound `ind ≤ m` is used implicitly as an immediate consequence of the definition, with no separate statement |
| 2 | WebSearch (general form) | weighted order of vanishing at a point bounded by weighted degree multivariate polynomial nonzero Taylor coefficient | partial | weighted order ≤ weight of any multi-index with a nonzero coefficient (the Mathlib `MvPowerSeries.weightedOrder_le` docs page, arXiv 2309.09757) | general form: order at a point ≤ weighted degree of the polynomial, where the weighted degree is bounded by `∑ deg_{x_j}/r_j` |
| 3 | WebSearch (aliases: Bombieri–Gubler index, Roth's lemma) | Bombieri Gubler index polynomial "index" bounded by m multidegree (r_1,...,r_m) Roth lemma | partial | Roth's lemma bounds Ind(P) by `2mη` under extra hypotheses (arXiv 2502.00731 Lemma 3.9). The trivial bound `Ind ≤ m` is the starting point | no explicit statement of the trivial bound |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for "Theta", "Taylor's theorem" | yes | clean.tex:665-667: `0 ≤ Θ_m ≤ m` because "Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, of weight at most `m`". clean.tex:543-545: attainment, and `ind(0) = +∞` | the Lean lemma is exactly this argument |
| 6 | nLab | order of vanishing / valuation | no | abstract valuations only | nothing about the weighted bound |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an elementary real-number inequality on finite sums) |
| 8 | Stacks Project | order of vanishing (tag 02MB area) | no | order of vanishing of a function on a curve | not the weighted multi-index form |
| 9 | MathOverflow / Math.SE | covered by searches 1-3 | no | n/a | too elementary for a dedicated thread |
| 10 | recent arXiv | Roth index / Roth's lemma (results of 1 and 3) | partial | arXiv 2502.00731 (2025) restates Roth's lemma with `deg_{x_h} P ≤ r_h` | the trivial bound is not stated separately |

### Literature summary (Phase 3)

Concept identified as: the trivial upper bound for a weighted order of vanishing at a point. For a nonzero polynomial, the order at any point is at most its weighted degree, because the translate has the same partial degrees and some coefficient is nonzero.
Sources agree on the standard form: yes. It is used tacitly; the project source states it once (clean.tex:665-667).
Most general standard form: `ord_{α,1/r}(P) ≤ ∑_j deg_{x_j}(P)/r_j`, which is hypothesis-free in Lean (evidence (2)). The `|σ|` bound follows when `deg_{x_j} P ≤ r_j`.
Generality dimensions where the literature varies:
  - coefficients: ℚ or ℤ in Roth, ℝ in the project, any field in general. Here it is fixed by the parent def `Roth.index`.
  - bound: `m` (Roth), or the sharper `∑ deg_j / r_j`.
Disagreement with the literature: `ind(0)` is `+∞` in the source and `0` in Lean. Hence `hP` is needed in the source but not in Lean.

### Generality analysis — `Roth.index_le_card`

Literature-standard form: `ind(P; α; r) ≤ ∑_j deg_{x_j}(P)/r_j ≤ m`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | required | required in the source (since `ind 0 = ∞`) | YES (Lean) | `index 0 α r = 0` by junk value. Evidence (1), `index_le_card_noHP`, compiles |
| 2 | `hd : ∀ j, degreeOf j P ≤ r j` | required | required for the `m` bound | NO | evidence (3): one variable, `P = x²`, `α = 0`, `r = 1` gives index `2 > 1 = card` (compiled) |
| 3 | `r` positivity | none | positive in the source | already general | `r j = 0` is handled by the junk `/0` |
| 4 | conclusion `≤ card σ` | the `m` bound | `≤ ∑ deg_j/r_j` is sharper | alternative, sharper form | evidence (2), `index_le_sum_degreeOf`, compiles with no hypotheses. It is not needed by any caller |
| 5 | ring `ℝ` | fixed | any ring | not for this statement | it is fixed by the parent def `Roth.index` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN NECESSARY in one hypothesis (`hP`, verified droppable), and otherwise maximally general for the `card σ` conclusion. This is a local cleanup, not a mathlib-generalisation target, because the subject is the project-only def `Roth.index`.
Number of weakening opportunities found: 1 (drop `hP`). There is also an optional sharper sibling, `index_le_sum_degreeOf`.
Proposed restatement: `theorem index_le_card {P : MvPolynomial σ ℝ} {r : σ → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) : index P α r ≤ Fintype.card σ` (evidence (1)).
Cost of restatement: CHEAP. It is a mechanical `rcases eq_or_ne P 0` in the proof, and the two Theta call sites drop one argument.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | `hd` is a plain per-variable bound | — |
| 2 | Sequences vs filters? | no | finite algebraic statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | yes in principle | any `CommSemiring` | this belongs to the parent-def question (`Roth.index` is ℝ-only and BORDERLINE) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | — | — |
| 8 | Concrete-via-abstract? | partially | after `exists_weight_eq_index`, `index` is gone. The content is "a support element of `taylor α P` is bounded by `degreeOf`" plus `weight_le_card`. The abstract analogue would be `weightedOrder w (taylor α P) ≤ weight w (degreeOf · P)` for an `MvPolynomial` weighted order | that needs a new mathlib def (the parent's BORDERLINE question) |
| 9 | False-generalisation guard | no false generalisation | dropping `hP` keeps the meaning in Lean (it only uses the junk value) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the only abstraction would be a weighted-order-of-`MvPolynomial` bound, which first needs an upstream def. That is the parent `Roth.index`'s BORDERLINE question and not this lemma's.

### Proof strategy — `Roth.index_le_card`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | mild | `degreeOf_taylor` (the equality) belongs in mathlib with `MvPolynomial.taylor` (see MvPolynomial.degreeOf_taylor_le.md). The call `degreeOf_taylor_le α j P` would become `(degreeOf_taylor ..).le` | CHEAP, follow-up of the taylor PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (attain the min, bound the minimiser termwise).
  - Missing mathlib API: only the `degreeOf_taylor` equality, already tracked in MvPolynomial.degreeOf_taylor_le.md.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_le_card`

[A] Lean-Finder       "weighted order of a multivariate power series is at most the weighted degree of any nonzero coefficient, bounded by degree in each variable"   hits: `MvPowerSeries.weightedOrder_le`, `nat_le_weightedOrder`, `le_weightedOrder`, `weightedOrder`, `weightedOrder_monomial`. There is no bound by partial degrees
[B] Loogle            `MvPowerSeries.weightedOrder, MvPolynomial.degreeOf`   no hits
[C] LeanSearch        "order of vanishing of nonzero polynomial at a point is at most its degree"   hits: only `analyticOrderAt` API (one-variable analytic). There is no polynomial bound
[D] Grep mathlib src  `weightedOrder_le_weightedTotalDegree`, `order_le_totalDegree`, `index_le_card`, `weightedOrder` files. Hits: `MvPowerSeries.weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean:171), `MvPowerSeries.order_le` (same file:409), `MvPolynomial.monomial_le_degreeOf` (Mathlib/Algebra/MvPolynomial/Degrees.lean:268). There is no order-versus-degree lemma
[E] Name pattern      `Roth.index_le_card`, `index_le_card` (grep, since `lean_local_search` failed because ripgrep is not installed)   no Roth decl. The only hit is the unrelated `Subgroup.exists_index_le_card_of_leftCoset_cover`

Searched for both:
  - the user's current form (Roth index ≤ number of variables under a box condition)
  - the literature-standard form (weighted order at a point ≤ weighted degree)

Concluded: found building blocks (`MvPolynomial.monomial_le_degreeOf`, `MvPowerSeries.weightedOrder_le`, plus the project's `exists_weight_eq_index`, `degreeOf_taylor_le`, `weight_le_card`); composition gives our form.

### Normal-form check — `Roth.index_le_card`

Equivalent formalisms:
- `index P α r ≤ card σ` given `hd` (this lemma)
- `index P α r ≤ ∑ j, degreeOf j P / r j` (the sharper form, evidence (2))
- `BddAbove` of the indices of a family (the caller-side use in Theta.lean)

Does mathlib already have a canonical form? No (`Roth.index` is project-only).
RHS convention respected? yes (an inequality, not an iff)

### Syntactic generality — `Roth.index_le_card`

Alternative restatements attempted:
- the current form
- without `hP` (evidence (1))
- the sharper `index_le_sum_degreeOf` (evidence (2)), with the card bound as a corollary via `weight_le_card`

Chosen restatement: the current form minus `hP`.
Justification: both callers want the `card σ` bound directly, and dropping `hP` removes a non-trivial argument (`map_ne_zero_iff ... map_injective ...`) from each call site.

### Superfluous-argument audit — `Roth.index_le_card`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP : P ≠ 0` | no | `index 0 = 0` (junk value). Evidence (1) |
| 2 | `hd` | yes | evidence (3) counterexample |
| 3 | `α` explicit | yes | the callers pass `_` |
| 4 | `[Fintype σ]` | yes | needed by `index` and `card` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (drop `hP`)
Superfluous arguments: 1 to drop (`hP`)

Overall: RESTATE-BEFORE-SHIP (local cleanup only; this is not a mathlib candidate)

### Call sites — `Roth.index_le_card`

Internal use count: 2 (outside the declaring file)
External-to-file callers: 1 distinct file (Roth/Theta.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:91 | `exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0) (by simpa [degreeOf, degrees_map_of_injective ...] using hRd) _` (in `indexSet_bddAbove`) |
| Roth/Theta.lean:117 | the same expression (in `Θ_le_card`) |

Inline-derivation grep:
  - (none) — `weight_le_card` has only this caller (Roth/Index.lean:227), and no other site re-derives the bound.

### Composition check (Phase 6)

Can `Roth.index_le_card` be derived from mathlib in ≤3 chained calls?

Attempt 1 (the current proof): `exists_weight_eq_index`, then `weight_le_card fun j ↦ (monomial_le_degreeOf j _).trans ((degreeOf_taylor_le α j P).trans (hd j))`.
  - Decls used: mathlib `MvPolynomial.monomial_le_degreeOf` (Mathlib/Algebra/MvPolynomial/Degrees.lean:268); project `Roth.exists_weight_eq_index`, `MvPolynomial.degreeOf_taylor_le`, `Roth.weight_le_card`.
  - Result: succeeds (it is the current 3-line proof).
  - Notes: the project pieces are each themselves NO-composable (exists_weight_eq_index, weight_le_card) or YES-but-generalise (degreeOf_taylor) wrappers of mathlib's `Set.Nonempty.csInf_mem`, `Finset.sum_le_card_nsmul` and coefficient lemmas.

Conclusion: COMPOSABLE (a 3-call chain)

## Verdict: `Roth.index_le_card`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): clean.tex:665-667 states exactly this argument for `Θ_m ≤ m`. In the literature it is the tacit "order at a point ≤ weighted degree" bound.
- Generality analysis (Phase 4): `hP` is droppable (compiled), `hd` is necessary (compiled counterexample). There is a sharper hypothesis-free sibling `index ≤ ∑ deg_j/r_j` (compiled).
- Mathlib search (Phase 5): building blocks only (`monomial_le_degreeOf`, `MvPowerSeries.weightedOrder_le`). There is no order-versus-degree lemma, and no `Roth.index`.
- Composition check (Phase 6): COMPOSABLE (3 chained calls).

**Rationale:**

The statement is about the project-only, ℝ-valued `Roth.index` (its own report is BORDERLINE), so it has no mathlib home as stated. Its content is "the minimiser `d` lies in the support of the translate, so `d ≤ (degreeOf j P)_j ≤ r`, so its weight is at most `card σ`". That is three chained lemmas, one of them mathlib's `monomial_le_degreeOf`. If an upstream `MvPolynomial` weighted order were ever added, the natural lemma would be "weighted order at a point ≤ weighted degree", a different lemma about that def. It would not be this one.

Locally, `hP` is superfluous because of the junk value `index 0 = 0` (evidence (1)). Dropping it simplifies both call sites in Theta.lean. `hd` is genuinely needed (evidence (3)).

WHY not: it is a short chain of existing project and mathlib API about a project definition, and it adds no mathematics mathlib lacks.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean. It is the source's `Θ_m ≤ m` step and is shared by two Theta lemmas.
Mathlib building blocks: `MvPolynomial.monomial_le_degreeOf` (Mathlib/Algebra/MvPolynomial/Degrees.lean:268); analogue `MvPowerSeries.weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean:171); project `Roth.exists_weight_eq_index` (Roth/Index.lean:76), `MvPolynomial.degreeOf_taylor_le` (Roth/Taylor.lean:170), `Roth.weight_le_card` (Roth/Box.lean:103).
Composition sketch (≤3 lines):
```lean
  obtain ⟨d, hd0, hdw⟩ := exists_weight_eq_index hP α r
  exact hdw ▸ weight_le_card fun j ↦ (monomial_le_degreeOf j (mem_support_taylor_iff.2 hd0)).trans
    ((degreeOf_taylor_le α j P).trans (hd j))
```
Call sites in our project (from Phase 6.0): 2 (Roth/Theta.lean:91, Roth/Theta.lean:117).
Refactor plan: do not delete or inline. Inlining would duplicate the chain at both Theta sites and would need the private `mem_support_taylor_iff`. Optional local cleanup: drop `hP`, proving the `P = 0` case with `rcases eq_or_ne P 0 with rfl | hP; · simp [index]`. Then at Theta.lean:91 and :117 delete the first argument `((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)`. If `hR0` then becomes unused, replace it by `-` in the `rintro` patterns.
Next action: keep locally; optionally drop `hP`; do not upstream.

## Next step

Keep `Roth.index_le_card` in Roth/Index.lean and do not upstream it. Optionally drop the superfluous `hP` (proof in `.mathlib-quality/overview/evidence/Roth.index_le_card/hyps.lean`) and remove the corresponding argument at Roth/Theta.lean:91 and Roth/Theta.lean:117.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_le_card/hyps.lean` (imports `Roth.Index`). `lean_diagnostic_messages` reports no diagnostics at all. The file contains:
  - (1) `index_le_card_noHP`: the lemma without `hP`, with the `P = 0` case closed by `simp [index]`.
  - (2) `index_le_sum_degreeOf`: the hypothesis-free sharper bound `index P α r ≤ ∑ j, degreeOf j P / r j`.
  - (3) a counterexample showing `hd` is necessary: `σ = Unit`, `P = monomial (single () 2) 1`, `α = 0`, `r = 1`. Then `index_unique` gives index `2`, which is not `≤ 1 = card Unit`.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, Evertse's Luminy slides, arXiv 2309.09757.
- Local grep of `.mathlib-quality/references/clean.tex` (lines 538-548, 655-667).
- Lean-Finder, Loogle and LeanSearch searches, and a grep of `.lake/packages/mathlib/Mathlib/`, as recorded in Phase 5. `lean_local_search` was unavailable (ripgrep is not installed), so grep was used instead.
- `grep -rn index_le_card Roth/`: the declaration and Theta.lean:91 and 117.
- The ChatGPT channel is n/a: the `ask_chatgpt_math` MCP is not configured in this session.
