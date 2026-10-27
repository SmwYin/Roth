---
decl: Roth.exists_hasseDeriv_eval_ne_zero
file: Roth/MainLemma.lean
line: 454
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Strict-cutoff form of index attainment, one Exists.imp on exists_weight_eq_index or the contrapositive of le_index_iff (both compiled); its weighted-order analogue is the one-line contrapositive of MvPowerSeries.le_weightedOrder (compiled); hP necessary (compiled); nothing new for mathlib.
action: Keep project-local (sole caller exists_hasseDeriv_index_eval_bound_aux at Roth/MainLemma.lean:486), optionally move beside exists_weight_eq_index in Roth/Index.lean; no mathlib PR.
---

# Roth.exists_hasseDeriv_eval_ne_zero

## Inventory entry

### `theorem Roth.exists_hasseDeriv_eval_ne_zero`
- **Type**: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) {c : ℝ} (hc : index P α r < c) : ∃ k : σ →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0`
- **What**: If a nonzero real polynomial `P` has index `< c` at `α` relative to `r`, then some Hasse derivative `Δ_k P` with weight `∑ k_j/r_j < c` does not vanish at `α`.
- **How**: `Exists.imp` on `Roth.exists_weight_eq_index hP α r` (a multi-index attaining the index has nonzero derivative value and weight `= index < c`, rewritten with `hw ▸ hc`).
- **Hypotheses**: `hP : P ≠ 0` (necessary: junk value `index 0 = 0`, evidence (3)); `hc : index P α r < c` strict cutoff. No positivity on `r`, any finite `σ`.
- **Uses from project**: `Roth.index`, `Roth.weight`, `Roth.exists_weight_eq_index`, `MvPolynomial.hasseDeriv`
- **Used by**: `Roth.exists_hasseDeriv_index_eval_bound_aux` (private, Roth/MainLemma.lean:486). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 446–457 (docstring 446–453, statement 454–456), proof length 1 line
- **Notes**: Paper step: §6, proof of Lemma 9 (clean.tex l.1526, "the index of W^* ... is less than η ... Hence W^* has some derivative").

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:486 inside the private `exists_hasseDeriv_index_eval_bound_aux`.
- Wrapper of 1–2 mathlib calls? Wrapper of one project lemma (`exists_weight_eq_index`) plus `Exists.imp`; no mathlib content.
- Does mathlib have it? No (project-local `index`, `hasseDeriv`); the weighted-order analogue is the contrapositive of `MvPowerSeries.le_weightedOrder` (not stated as a separate mathlib lemma; loogle `MvPowerSeries.weightedOrder _ _ < _ → ∃ d, _` 0 hits).
- Too specific (inline)? Single caller and a 1-line proof, so inlining is possible, but the strict-cutoff shape is the form the consumer needs (`obtain ⟨k, hkw, hkev⟩`), it names one paper sentence, and it is the natural companion of `exists_weight_eq_index` / `le_index_iff` in the index API; same treatment as siblings `le_index_of_forall_eval_eq_zero`, `sub_mem_RSet` (KEEP).
- Well-chosen? Yes: strict inequality matches Lemma 7's output `index < η`.
- Conclusion: `KEEP`. Optional: relocate to Roth/Index.lean beside `exists_weight_eq_index` (it only needs `Roth.Index`; evidence file imports only `Roth.Index`).

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `exists_hasseDeriv_eval_ne_zero`, `namespace Roth` in `.lake/packages/mathlib/Mathlib/`: 0 hits). Not a glue lemma (`Exists.imp` with a rewrite, not `rfl`/unfolding), so INHERITED does not apply; full run. Parent `Roth.index` is BORDERLINE-needs-human and `Roth.exists_weight_eq_index` is NO-composable-from-mathlib (neither is NO-mathlib-has-it), so no re-aim; the canonical analogue is nevertheless checked (Phase 4c row 7, Phase 6 attempt 3).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` elaborates clean)
- decl `Roth.exists_hasseDeriv_eval_ne_zero`: ✓ resolved at Roth/MainLemma.lean:454
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's Lemma 9 (the main lemma): existence of an auxiliary integer polynomial with large index at (α, …, α) and controlled coefficients.

### Statement (Phase 1)

`Roth.exists_hasseDeriv_eval_ne_zero` is a theorem stating the following:

Let `P ∈ ℝ[x_j : j ∈ σ]` be nonzero, `α ∈ ℝ^σ`, `r ∈ ℕ^σ`, `c ∈ ℝ`. If `ind_{α,r}(P) < c`, then there is a multi-index `k` with `∑_j k_j/r_j < c` and `(Δ_k P)(α) ≠ 0`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite variable set (needed by `weight`, `index`)
- `P`: the polynomial; `α`: the point; `r`: weights; `c`: the cutoff

Hypotheses (Lean side):
- `hP : P ≠ 0`: nonzero polynomial
- `hc : index P α r < c`: index below the cutoff

Conclusion (math): some Hasse derivative of weight below `c` is nonzero at `α`.

Conclusion (Lean): `∃ k : σ →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: one sentence inside the proof of Lemma 9; not a main result, not named.

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | Roth's theorem proof index less than eta polynomial has derivative with sum k_j/r_j less than eta nonvanishing at point | yes | arXiv math/0307203 (quantitative Roth–Ridout): index of W below η gives a derivative W_k with `∑ k_j/r_j < η`; Evertse Leiden slides | the same inline step as in our source; never a separate lemma |
|  2 | WebSearch (general form) | weighted order of vanishing of multivariate polynomial at a point minimum over nonzero Taylor coefficients existence of nonvanishing derivative | yes | order of vanishing = min weight of a nonzero Taylor coefficient (arXiv 1707.01354 weighted multiplicity; Lebl notes; 2511.13537) | existence below any cutoff above the minimum is definitional |
|  3 | WebSearch (named / aliases) | "index" of a polynomial Roth lemma Hasse derivative multiplicity weighted Siegel Bombieri Gubler heights | partial | weighted index in Roth's lemma (JTNB 2001, Bombieri–Gubler ch. 6, Maculan notes) | index always defined as a minimum; the step is not stated separately |
|  4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "W^*", "some derivative" | yes | l.1526: index of W^* less than η, hence some derivative with weight `< η` nonvanishing | exactly the sentence formalised |
|  6 | nLab | Hasse derivative multiplicity of polynomial at point (WebSearch restricted to ncatlab.org) | no | none (search returned only arXiv hits on Hasse-derivative multiplicity: 1509.00279, 1909.03180, 1402.3018) | no nLab page on weighted order / index |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept (finite minimum of a weight function) |
|  8 | Stacks Project | n/a | n/a | n/a | weighted point-index of a real polynomial is not treated in Stacks; the statement is the definition of an order of vanishing read contrapositively |
|  9 | MathOverflow / Math.SE | covered by #2/#3 results | no | none | folklore; no thread states it |
| 10 | recent arXiv (last 5 years) | #2/#6 hits arXiv 2511.13537 (2025), 2403.19824 (2024), 2502.00731 (2025, from #1 family) | yes | same definitions | step is inline |

### Literature summary (Phase 3)

Concept identified as: the "minimum is below c" reading of the definition of the (weighted) index / order of vanishing at a point: if `ord_w(f) < c` then some nonzero Taylor coefficient has weight `< c`.
Sources agree on the standard form: yes; definitional and always inline.
Most general standard form: for any (semi)ring and weights, `ord_w(f) < n → ∃ d, w(d) < n ∧ coeff_d f ≠ 0` (contrapositive of mathlib's `MvPowerSeries.le_weightedOrder`).
Generality dimensions where the literature varies:
  - weights: ℕ (mathlib) vs real `1/r_j` (Roth)
  - coefficients: ℝ vs any (semi)ring
Disagreement with the literature: none.

### Generality analysis — `Roth.exists_hasseDeriv_eval_ne_zero`

Literature-standard form: `ord_w f < n → ∃ d, w(d) < n ∧ coeff_d f ≠ 0`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | nonzero | not needed when `ord 0 = ∞` | no (for this def) | with junk `index 0 = 0`, `P = 0`, `c = index 0 α r + 1` the conclusion fails (evidence (3), compiled) |
| 2 | `hc` strict | `index < c` | strict | no | with `c = index` no `k` has `weight < c`, by `index_le_weight` |
| 3 | coefficients `ℝ`, `[Fintype σ]` | fixed by `Roth.index` | any semiring | inherited | determined by the parent def |
| 4 | positivity of `r` | not assumed | — | already maximal | holds for all `r` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (relative to the parent `Roth.index`)
Number of weakening opportunities found: 0 (`hP` verified necessary in evidence (3))
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | single-use hypotheses | — |
| 2 | sequences to filters? | no | finite algebraic statement | — |
| 3 | construction vs universal property? | no | it is the glb property of the defining minimum | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | only via parent def | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `weightedOrder w (taylor α P) < n → ∃ d, weight w d < n ∧ coeff d (taylor α P) ≠ 0` | contrapositive of `MvPowerSeries.le_weightedOrder` (evidence (4)) |
| 8 | concrete-via-abstract? | yes, trivially | proof uses only that `index` is an attained minimum | abstraction already exists (`exists_weight_eq_index`, `le_index_iff`; mathlib `le_weightedOrder`) |
| 9 | false-generalisation guard | no false generalisation | the `weightedOrder` analogue is canonical but not a drop-in for the ℝ-valued index (as for the parent) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
One-line reason: the canonical analogue is a one-line contrapositive of mathlib's `MvPowerSeries.le_weightedOrder`; no new organisational idea.

### Proof strategy — `Roth.exists_hasseDeriv_eval_ne_zero`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already via the attainment lemma | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (1 line; an alternative via `le_index_iff` contrapositive also compiles, evidence (2), but is longer).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "order of vanishing of a polynomial at a point is less than c implies some derivative of weighted order less than c does not vanish at the point"   hits: `Polynomial.lt_rootMultiplicity_iff_isRoot_iterate_derivative_of_mem_nonZeroDivisors(')` (one-variable unweighted analogue), `Polynomial.derivRootWeight` (unrelated)
[B] Loogle            `MvPowerSeries.weightedOrder _ _ < _ → ∃ d, _`   no hits
[C] LeanSearch        "if weighted order of power series is less than n then some coefficient of weight less than n is nonzero"   hits: `MvPowerSeries.le_weightedOrder` (contrapositive is our form), `exists_coeff_ne_zero_and_weightedOrder`, `coeff_eq_zero_of_lt_weightedOrder`, `weightedHomogeneousComponent_of_weightedOrder`
[D] Grep mathlib src  `exists_hasseDeriv_eval_ne_zero`, `hasseDeriv_eval_ne_zero`, `namespace Roth`: 0 hits; `le_weightedOrder` at Mathlib/RingTheory/MvPowerSeries/Order.lean:197
[E] Name pattern      grep [D] used in place of `lean_local_search` (no MvPolynomial Hasse derivative or point index exists in mathlib; see `MvPolynomial.hasseDeriv`, `Roth.index` reports)

Searched for both: the project form (strict-cutoff nonvanishing derivative) and the literature-standard form (weighted order below n gives a nonzero coefficient of weight below n).

Concluded: found building blocks; project form is `exists_weight_eq_index` + `Exists.imp`; canonical analogue is the contrapositive of `MvPowerSeries.le_weightedOrder`.

### Statement-shape verdict (Phase 5.5)

Normal-form check: equivalent formalisms are `index P α r < c → ∃ k, …` (this), `exists_weight_eq_index` (attainment, the canonical form for this def), and `¬ c ≤ index` via `le_index_iff`. This lemma is the strict-cutoff consumer form of the canonical attainment lemma; RHS convention: n/a (not an iff).
Syntactic generality: alternatives tried: attainment form (caller would need `hw ▸ hc`), `le_index_iff` contrapositive. Chosen: current form; the caller destructures `⟨k, hkw, hkev⟩` directly.
Superfluous-argument audit:

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP` | yes | evidence (3) |
| 2 | `hc` | yes | gives `weight < c` |
| 3 | `[Fintype σ]` | yes | via `weight`/`index` |

Normal form: OK. Syntactic generality: OK. Superfluous arguments: NONE.
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 1 (declaring file only); external-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern |
|---|---|
| Roth/MainLemma.lean:486 | `obtain ⟨k, hkw, hkev⟩ := exists_hasseDeriv_eval_ne_zero ((map_ne_zero_iff _ …).2 hP) z r hz` in `exists_hasseDeriv_index_eval_bound_aux` |

Inline-derivation grep: none; the other users of `exists_weight_eq_index` (Roth/Index.lean:101, 112, 226) need the equality `weight = index`, not a strict cutoff.

### Composition check (Phase 6)

Attempt 1: `(exists_weight_eq_index hP α r).imp fun _ ⟨hd, hw⟩ ↦ ⟨hw ▸ hc, hd⟩`
  - Decls used: project `Roth.exists_weight_eq_index`, core `Exists.imp`
  - Result: succeeds (evidence (1))
Attempt 2: `by_contra! h; exact hc.not_ge ((le_index_iff hP).2 fun d hd ↦ le_of_not_gt fun hw ↦ hd (h d hw))`
  - Decls used: project `Roth.le_index_iff`
  - Result: succeeds (evidence (2))
Attempt 3 (canonical analogue): `by_contra! h; exact hn.not_ge (MvPowerSeries.le_weightedOrder w h)`
  - Result: succeeds for the mathlib weighted order over any semiring (evidence (4))

Conclusion: COMPOSABLE (one project API call; analogue is one mathlib call).

## Verdict: `Roth.exists_hasseDeriv_eval_ne_zero`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the index / order of vanishing is a minimum; "below the cutoff gives a nonvanishing derivative" is the definition read contrapositively, always inline (clean.tex l.1526, arXiv math/0307203).
- Generality analysis (Phase 4): MAXIMALLY GENERAL; `hP` necessary (evidence (3)).
- Mathlib search (Phase 5): canonical analogue is the contrapositive of `MvPowerSeries.le_weightedOrder`; no point index in mathlib.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

The statement is the strict-cutoff restatement of the attainment lemma `Roth.exists_weight_eq_index` (itself NO-composable-from-mathlib), obtained by one `Exists.imp`, or equivalently the contrapositive of `Roth.le_index_iff`. For mathlib's canonical weighted order the same statement is the one-line contrapositive of `MvPowerSeries.le_weightedOrder`. Nothing here is new mathematics for mathlib; its upstream fate is tied to the parent `Roth.index` (BORDERLINE) and to `MvPolynomial.hasseDeriv`.

WHY not: a 1-call composition of project API whose mathlib analogue is a 1-call composition of `le_weightedOrder`. Belongs-elsewhere: keep project-local, in Roth/MainLemma.lean or beside `exists_weight_eq_index` in Roth/Index.lean.
Building blocks: project `Roth.exists_weight_eq_index` (Roth/Index.lean:76), project `Roth.le_index_iff` (Roth/Index.lean:85); mathlib analogue `MvPowerSeries.le_weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean:197).
Composition sketch:
```lean
example (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) (hc : index P α r < c) :
    ∃ k : σ →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 :=
  (exists_weight_eq_index hP α r).imp fun _ ⟨hd, hw⟩ ↦ ⟨hw ▸ hc, hd⟩
```
Call sites in our project: 1 (Roth/MainLemma.lean:486).
Refactor plan: none required. Inlining at Roth/MainLemma.lean:486 (`obtain ⟨k, hkev, hkw⟩ := exists_weight_eq_index …` then `hkw ▸ hz`) is mechanical but not recommended: the lemma names the paper step and keeps the caller's coercion-heavy proof readable. Optional: move the lemma to Roth/Index.lean.
Next action: no upstreaming; keep as is.

---

## Next step

Do not upstream; keep `Roth.exists_hasseDeriv_eval_ne_zero` (sole caller Roth/MainLemma.lean:486), optionally relocating it to Roth/Index.lean beside `exists_weight_eq_index`. No mathlib PR.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_hasseDeriv_eval_ne_zero/experiments.lean` (imports `Roth.Index`), checked with `lean_diagnostic_messages`: no errors, no sorry (only the module-docstring header style warning). Contains:
  - (1) the current one-line proof via `exists_weight_eq_index`;
  - (2) alternative proof via the contrapositive of `le_index_iff`;
  - (3) `hP` necessary: for `P = 0` and `c = index 0 α r + 1` no derivative is nonzero (closed by `simp`);
  - (4) mathlib analogue: `f.weightedOrder w < n → ∃ d, weight w d < n ∧ coeff d f ≠ 0` over any semiring, via `MvPowerSeries.le_weightedOrder`.
- WebSearch ×4 (three generality levels + nLab-restricted), queries in the literature table.
- Loogle `MvPowerSeries.weightedOrder _ _ < _ → ∃ d, _` (0 hits); LeanSearch and Lean-Finder queries as recorded.
- Greps: mathlib for `exists_hasseDeriv_eval_ne_zero`, `hasseDeriv_eval_ne_zero`, `namespace Roth` (0 hits); project for call sites and `exists_weight_eq_index` users; clean.tex for `W^*` (l.1526).
- `ask_chatgpt_math` MCP not configured in this session.
