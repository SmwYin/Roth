---
decl: Roth.sum_max_sub_le_index_det
file: Roth/Theta.lean
line: 376
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The Lemma 6 step ind(F) ≥ ∑_{ν<l} max(0, ind R - ν/r_p) - lδ for the generalised-Wronskian determinant F of Roth's proof; it is a 30-line combination of four project index lemmas (le_index_sum, index_prod, index_C_mul, index_sub_weight_le_index_hasseDeriv) about the project-only Roth.index, has no standalone counterpart in the literature or mathlib, and is not a ≤3-call composition, so no YES or NO bucket fits cleanly; recommended resolution is to keep it in the project.
action: Keep in Roth/Theta.lean (single caller Roth.index_le_lem6 at Roth/Theta.lean:576); optionally replace hD and hδ by the single hypothesis ∀ μ, weight (r ∘ some) (D μ) ≤ δ (same proof, original recovered in one line, compiled in evidence/Roth.sum_max_sub_le_index_det/restate.lean); do not upstream.
---

# Roth.sum_max_sub_le_index_det

## Inventory entry

### `theorem Roth.sum_max_sub_le_index_det`
- **Type**: `{τ : Type*} [Fintype τ] {R : MvPolynomial (Option τ) ℝ} {l : ℕ} (D : Fin l → (τ →₀ ℕ)) (hD : ∀ μ, (D μ).degree ≤ μ) (hdet : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) R).det ≠ 0) (α : Option τ → ℝ) {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ} (hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ) : ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤ index (Matrix.of fun μ ν ↦ hasseDeriv (...) R).det α r`
- **What**: For a real polynomial `R` in variables `Option τ` (`none` playing the role of `x_p`), the determinant `F = det(Δ_{D_μ} ∂_{x_p}^{(ν)} R)_{μ,ν<l}` (Hasse derivatives) has Roth index at least `∑_{ν<l} max(0, ind R - ν/r_p) - lδ`, provided `F ≠ 0`, `D_μ` has total degree `≤ μ`, and `δ` bounds the weights of all multi-indices of degree `≤ l - 1`. This is the displayed conclusion "We have proved ind(F) ≥ …" of clean.tex §5, proof of Lemma 6 (l.814–840).
- **How**: (i) Entrywise bound `hterm`: for each nonzero entry, `index_sub_weight_le_index_hasseDeriv` gives `ind R - weight ≤ ind(entry)`; `weight_add`, `weight_mapDomain`, `weight_single` split the weight into `weight(D μ) + ν/r_p`, bounded via `hδ`/`hD`; `index_nonneg` and `weight_nonneg` give the `max 0` form. (ii) Expand `det` with `Matrix.det_apply'`; `le_index_sum` reduces to each nonzero permutation term; `index_C_mul` removes the sign; `index_prod` splits the product; `Fin.sum_univ_eq_sum_range`, `Fin.sum_const`, `Finset.sum_sub_distrib`, `Finset.sum_le_sum` finish.
- **Hypotheses**: `hD` and `hδ` (only used through `weight (r ∘ some) (D μ) ≤ δ`, see evidence); `hdet` (needed: Lean has `index 0 = 0`); `hr` (needed by `index_prod`).
- **Uses from project**: `Roth.index`, `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.weight`, `Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_single`, `Roth.index_nonneg`, `Roth.weight_nonneg`, `Roth.le_index_sum`, `Roth.index_C_mul`, `Roth.index_prod`.
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:576, `have hlower := sum_max_sub_le_index_det D hD (mapped_det_ne_zero_aux hU hV hF) α hr0 ...`). No other occurrence in `Roth/` or `Roth.lean`.
- **Visibility**: public
- **Lines**: 372–411 (docstring 373–375, statement 376–383, proof 384–411), proof length 28 lines
- **Notes**: `omit [DecidableEq τ] in` precedes it. Public but single-use and Lemma-6-specific; could be private without loss.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.index_le_lem6` (Theta.lean:576).
- Wrapper of 1–2 mathlib calls? No; it chains four project index lemmas and a weight computation over 28 lines.
- Does mathlib have it? No: `Roth.index` and `MvPolynomial.hasseDeriv` are project definitions; mathlib has no valuation-of-determinant lemma (searches in Phase 5; closest generic tool is `AddValuation.map_le_sum`).
- Too specific (inline?)? It is specific to Lemma 6, but it is a displayed, named step of the source, and inlining would bloat `index_le_lem6` (already long). Keep as a named lemma.
- Well-chosen? Mostly; `hD` + `hδ` can be compressed to one weight hypothesis (evidence (1)), which is a cosmetic improvement.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `sum_max_sub_le_index_det` and `namespace Roth`: no hit. Not a glue lemma (28-line proof), so the full workflow follows. Parent defs `Roth.index` (BORDERLINE) and `MvPolynomial.hasseDeriv` are not NO-mathlib-has-it, so no re-aim.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` elaborates with no diagnostics)
- decl `Roth.sum_max_sub_le_index_det`: resolved at Roth/Theta.lean:376
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index across sets of polynomials `Θ_m(B; q; r)` and Lemmas 5, 6, 7 of the source

### Statement (Phase 1)

`Roth.sum_max_sub_le_index_det` is a theorem stating the following:

Let `R ∈ ℝ[x_1, …, x_{p-1}, x_p]`, let `r_j > 0` be integer weights, `α` a point, and `θ = ind_{α,r}(R)`. For multi-indices `D_0, …, D_{l-1}` in the first `p-1` variables with `|D_μ| ≤ μ`, form the generalised Wronskian `F = det(Δ_{D_μ} (1/ν!) ∂^ν_{x_p} R)_{0≤μ,ν<l}`. If `F ≠ 0` and `δ ≥ ∑_{j<p} d_j / r_j` for every `d` with `|d| ≤ l - 1`, then `ind(F) ≥ ∑_{ν<l} max(0, θ - ν/r_p) - lδ`.

Variables / typeclasses involved (Lean side):
- `τ` with `[Fintype τ]`: the first `p-1` variables; `Option τ`: all `p` variables, `none = x_p`.
- `R`: the polynomial; `l`, `D`: size and row derivative orders; `α`: the point; `r`: weights; `δ`: weight bound.

Hypotheses (Lean side):
- `hD : ∀ μ, (D μ).degree ≤ μ`: row orders have degree `≤ μ ≤ l - 1`.
- `hdet`: `F ≠ 0` (source: index of `0` is `+∞`; Lean: `0`).
- `hr : ∀ j, 0 < r j`: weight positivity.
- `hδ`: `δ` bounds the weight of every multi-index of degree `≤ l - 1`.

Conclusion (math): `ind(F) ≥ ∑_{ν<l} max(0, θ - ν/r_p) - lδ`.

Conclusion (Lean): `∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤ index (Matrix.of …).det α r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an intermediate step inside the proof of Lemma 6, not a main result or a new structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 28 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma index of Wronskian determinant lower bound sum max(0, theta - nu/r) - l delta | partial | Roth's lemma index bounds; Wronskian-index links | arXiv 2502.00731 (Lemma 3.9 Roth's lemma), arXiv 1305.0926 (Prop. 6.21 index of a Wronskian); no source states this exact inequality standalone |
| 2 | WebSearch (general form) | index of generalized Wronskian lower bound index of entries determinant valuation of determinant at least minimum over permutations | partial | valuation of a determinant ≥ min over permutations of sum of entry valuations (ultrametric + Leibniz) | arXiv 2006.10790 (generalised Wronskians and an index); arXiv 1206.4224 (valuation of a Wronskian ≥ sum - C(k,2), same shape) |
| 3 | WebSearch (aliases) | Roth's theorem proof Lemma 6 generalized Wronskian index estimate Hardy Wright Cassels Diophantine approximation | partial | Roth's generalised Wronskian lemma (Roth 1955, Mathematika); textbook Roth lemma (Hindry–Silverman D.6, Bombieri–Gubler ch. 6) | the estimate appears only inside the induction step of Roth's lemma |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for `ind(F)` and `lδ` | yes | clean.tex 814–840: entrywise bound `max(0, θ - ν/r_p) - δ`, Leibniz expansion, Lemma 4-1, conclusion `ind(F) ≥ ∑_{ν<l} max(0, θ - ν/r_p) - lδ` | the Lean statement matches the source display at l.840 exactly |
| 6 | nLab | valuation; Wronskian | no | abstract valuations; Wronskian of functions | nothing on index of determinants |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | valuations | no | ultrametric inequality for valuations | no determinant/index statement; not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 2–3) | no | n/a | no thread on this estimate; it is a routine step in Roth's lemma |
| 10 | recent arXiv | 2502.00731, 1305.0926, 2006.10790 | partial | as #1–#2 | the step is always proved inline within the Roth-lemma induction |

### Literature summary (Phase 3)

Concept identified as: the index lower bound for the generalised Wronskian in the induction step of Roth's lemma (Lemma 6 of the source).
Sources agree on the standard form: yes, but only as an inline step: `ind(F) ≥ min_σ ∑_ν ind(entry) ≥ ∑_ν max(0, θ - ν/r_p) - lδ`.
Most general standard form: for any (weighted) valuation `v` and any square matrix `A`, `v(det A) ≥ min_σ ∑_i v(A_{σ(i),i})`; the Roth-specific content is the entrywise bound via "differentiating by Δ lowers the index by at most its weight".
Generality dimensions where the literature varies:
  - valuation: Roth index (rational weights `1/r_j`) vs general monomial valuation vs abstract `AddValuation`.
  - zero convention: `+∞` vs the project's `0` (forces `hdet`).
Disagreement with the literature: none.

### Generality analysis — `Roth.sum_max_sub_le_index_det`

Literature-standard form: the source display (clean.tex l.840); the generic kernel is `v(det A) ≥ min_σ ∑ v(A_{σ i, i})`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hD` + `hδ` | degree bound on `D μ` and weight bound on all `d` of degree `≤ l-1` | `w/r_{p-1} ≤ (l-1)/r_{p-1} < δ` (source combines both) | yes (restatement) | only `∀ μ, weight (r ∘ some) (D μ) ≤ δ` is used; evidence (1) compiles the one-hypothesis form and recovers the original in one line |
| 2 | `hdet` | `F ≠ 0` | none (`ind 0 = +∞`) | no | Lean's `index 0 = 0` makes the bound false for `F = 0` with positive LHS |
| 3 | `hr` | `0 < r j` | positive weights | no (mechanically) | required by `index_prod` |
| 4 | ring `ℝ`, Roth index | fixed | any valuation | not for this statement | `Roth.index` is defined only over `ℝ`; abstracting means redesigning the parent def |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (up to the cosmetic hypothesis compression in row 1, which is a restatement, not a weakening of content: the original is recovered in one line)
Number of weakening opportunities found: 1 (verified: evidence (1), `lean_diagnostic_messages` clean)
Proposed restatement: replace `hD`, `hδ` by `hw : ∀ μ, weight (r ∘ some) (D μ) ≤ δ` (and `[DecidableEq τ]` is not needed).
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | data-level bounds | — |
| 2 | Sequences vs filters? | no | finite algebraic inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | in principle | an ℕ∞-valued weighted order at a point over any domain | parent-def question (Roth.index BORDERLINE) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | partial | generic `v(det A) ≥ min_σ ∑ v(A_{σ i,i})` for an `AddValuation` | a generic `AddValuation.le_map_det` would be a separate, project-independent lemma |
| 8 | Concrete-via-abstract? | partially | after `Matrix.det_apply'` the proof uses only the ultrametric sum bound, product additivity and sign invariance, i.e. valuation axioms; the Roth-specific part is the entrywise `hterm` | the abstract kernel is the generic determinant bound of row 7 |
| 9 | False-generalisation guard | no false generalisation | the generic kernel specialises back exactly | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the abstract kernel (valuation of a determinant ≥ min over permutations) is a separate generic lemma; the Roth-specific entrywise bound and the specific matrix make this declaration irreducibly project-specific.

### Proof strategy — `Roth.sum_max_sub_le_index_det`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | mild | a generic `AddValuation`-style `v(det A) ≥ min_σ ∑ v(A_{σ i, i})` would split the proof into "generic det bound + entrywise bound"; mathlib lacks it, but `Roth.index` is not an `AddValuation`, so the project could not use it directly | MODERATE |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (Leibniz expansion + ultrametric sum bound + product additivity is the textbook route and mirrors the source)
  - Missing mathlib API: none usable here.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.sum_max_sub_le_index_det`

[A] Lean-Finder       "lower bound for the order (valuation) of a determinant from lower bounds on the orders of its entries"   hits: `Matrix.det_le`, `Matrix.det_sum_smul_le`, `Matrix.det_sum_le` (absolute-value upper bounds), Gershgorin `det_ne_zero_of_sum_*_lt_diag`; no valuation lower bound
[B] Loogle            `Matrix.det, MvPowerSeries.weightedOrder`   no hits
[C] LeanSearch        "valuation of determinant is at least the minimum over permutations of the sum of valuations of entries"   hits: `AddValuation.map_le_sum`, `Matrix.det_apply`, `Matrix.det_apply'`, `Matrix.det_le`, `Matrix.det_permute'` (building blocks only)
[D] Grep mathlib src  `sum_max_sub_le_index_det`, `index_det`, `det.*weightedOrder`, `Valuation.*det`, `Wronskian`   no relevant hits (`Mathlib/RingTheory/Polynomial/Wronskian.lean` is the one-variable two-polynomial Wronskian, unrelated)
[E] Name pattern      `Roth.sum_max_sub_le_index_det`   no mathlib decl in a matching namespace

Searched for both:
  - the user's current form (index of the Roth Wronskian)
  - the literature-standard kernel (valuation of a determinant ≥ min over permutations)

Concluded: found building blocks (`Matrix.det_apply'`, `AddValuation.map_le_sum`, `MvPowerSeries.weightedOrder_prod`); the generic determinant-valuation bound is not in mathlib; the Roth-specific statement is not in mathlib.

### Normal-form check — `Roth.sum_max_sub_le_index_det`

Equivalent formalisms: (a) this `ℝ`-valued inequality with `- l * δ` on the left; (b) `∑ … ≤ index F + l * δ`; (c) the min-over-permutations intermediate form.
Does mathlib already have a canonical form? no.
Proposed canonical form: current (lower bound `… ≤ index F`, matching `le_index_sum` and the source display).
RHS convention respected? yes (index on the RHS of `≤`, as in the project's `le_index_*` lemmas)

### Syntactic generality — `Roth.sum_max_sub_le_index_det`

Alternative restatements attempted:
- current (`hD` + `hδ`)
- `hw : ∀ μ, weight (r ∘ some) (D μ) ≤ δ` (evidence (1), compiles, original is a one-line corollary)
- matrix stated as an arbitrary `Matrix (Fin l) (Fin l)` with entrywise index bounds (generic form): moves the Roth content into the hypothesis; rejected as it would just be the generic kernel

Chosen restatement: current is acceptable; `hw` is marginally easier to apply in general, but the sole caller supplies `hδ` in the `d.degree ≤ l - 1` shape (`weight_le_delta_aux`), so the current form fits the call site.
Justification: the call site at Theta.lean:576 provides exactly `hD` and a degree-bounded `hδ`.

### Superfluous-argument audit — `Roth.sum_max_sub_le_index_det`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype τ]` | yes | needed by `Roth.index` / `Roth.weight` |
| 2 | `[DecidableEq τ]` | no | already omitted (`omit … in`) |
| 3 | `hD`, `hδ` | only through `weight (r ∘ some) (D μ) ≤ δ` | evidence (1) |
| 4 | `hdet` | yes | `index 0 = 0` |
| 5 | `hr` | yes for the proof | used by `index_prod` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (optional RESTATE to `hw`)
Superfluous arguments: NONE essential (hD and hδ can be merged)

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.sum_max_sub_le_index_det`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:576 | `have hlower := sum_max_sub_le_index_det D hD (mapped_det_ne_zero_aux hU hV hF) α hr0 (fun d hd ↦ weight_le_delta_aux …)` in `Roth.index_le_lem6` |

Inline-derivation grep:
  - (none) — no other site re-derives an index bound for a determinant.

### Composition check (Phase 6)

Can `Roth.sum_max_sub_le_index_det` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_apply'` + `Roth.le_index_sum` + `Roth.index_prod`.
  - Decls used: `Matrix.det_apply'` (mathlib), `Roth.le_index_sum`, `Roth.index_C_mul`, `Roth.index_prod`, `Roth.index_sub_weight_le_index_hasseDeriv` (project).
  - Result: partial. The skeleton is three calls, but it needs the entrywise bound `hterm` (weight arithmetic + `max 0`) and the sign/sum bookkeeping; the actual proof is 28 lines, which is a proof, not a composition.

Attempt 2: through a generic `AddValuation` determinant bound.
  - Result: fails; mathlib has no such lemma and `Roth.index` is not an `AddValuation`.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.sum_max_sub_le_index_det`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the estimate is the displayed conclusion of the source's Lemma 6 computation (clean.tex l.840) and the standard inline step of Roth's lemma; no source states it as a standalone result.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; one cosmetic restatement (merge `hD`, `hδ`) verified in evidence (1).
- Mathlib search (Phase 5): not in mathlib; only building blocks (`Matrix.det_apply'`, `AddValuation.map_le_sum`).
- Composition check (Phase 6): NOT-COMPOSABLE (28-line proof combining four project lemmas).

**Rationale:**

The statement is about the project's own `Roth.index` and `MvPolynomial.hasseDeriv` and a specific generalised-Wronskian matrix; it is a single step inside Lemma 6 with one caller. It is not a mathlib-shaped result (YES buckets fail: no literature standing as a standalone lemma, no mathlib gap it fills), and it is not a ≤3-call composition of mathlib (NO-composable fails), nor does mathlib have it (NO-mathlib-has-it fails). Like the sibling `Roth.min_le_sum_max`, it is therefore BORDERLINE, with the clear recommendation to keep it project-local.

The only mathlib-relevant fragment is the generic kernel `v(det A) ≥ min_σ ∑_i v(A_{σ i, i})` for an additive valuation, which mathlib lacks (it follows from `Matrix.det_apply'`, `AddValuation.map_le_sum` and `AddValuation.map_mul`). That would be an independent, project-unrelated contribution, and it would not shorten this proof unless `Roth.index` were redesigned as a valuation (parent-def question).

Numbered questions:
1. Keep `Roth.sum_max_sub_le_index_det` project-local in Roth/Theta.lean (recommended: yes)?
2. Make it `private` (single caller, Lemma-6-internal)? Yes or no.
3. Replace `hD` and `hδ` by `hw : ∀ μ, weight (r ∘ some) (D μ) ≤ δ` (evidence (1)), moving the degree argument to the caller at Theta.lean:576? Yes or no.
4. Is a generic `AddValuation` lemma `v(det A) ≥ min_σ ∑ v(A_{σ i,i})` worth proposing to mathlib independently (Mathlib/RingTheory/Valuation/Basic.lean or LinearAlgebra/Matrix/Determinant)? Yes or no.

Next action: user answers the questions; default is to keep the lemma as is in Roth/Theta.lean.

### Next step

Keep `Roth.sum_max_sub_le_index_det` in Roth/Theta.lean (caller `Roth.index_le_lem6`, Theta.lean:576). Do not upstream. Optionally adopt the one-hypothesis restatement from evidence (1).

## Evidence
- `.mathlib-quality/overview/evidence/Roth.sum_max_sub_le_index_det/restate.lean` (imports `Roth.Theta`; `lean_diagnostic_messages`: no diagnostics):
  - (1) `Roth.sum_max_sub_le_index_det'`: the same theorem with `hD`, `hδ` replaced by `hw : ∀ μ, weight (r ∘ some) (D μ) ≤ δ`, same proof, without `[DecidableEq τ]`; plus an `example` recovering the original statement in one line from it.
- WebSearch ×3 (queries in the table); local grep of `.mathlib-quality/references/clean.tex` (l.814–840); Lean-Finder, Loogle, LeanSearch and a mathlib grep as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
- Sources: https://arxiv.org/pdf/2502.00731, https://arxiv.org/pdf/1305.0926, https://arxiv.org/pdf/2006.10790, https://arxiv.org/pdf/1206.4224, Roth 1955 (Mathematika, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational-approximations-to-algebraic-numbers.pdf).
