---
decl: Roth.index_eq_zero_iff
file: Roth/Index.lean
line: 98
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The index vanishes iff P(alpha) is nonzero is the attained-minimum property plus weight_eq_zero_iff (weight zero forces d = 0 for positive r) plus coeff_taylor at d = 0 (compiled without sibling lemmas); the canonical analogue is the unweighted MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero and the weighted form composes from le_weightedOrder and weightedOrder_le (compiled); hP and hr both necessary (compiled).
action: Keep locally as the source lemma of section 4 (used at Roth/Index.lean:182 in index_prod); do not upstream; optional tiny generic mathlib follow-up MvPowerSeries.weightedOrder_eq_zero_iff for positive weights (Mathlib/RingTheory/MvPowerSeries/Order.lean, next to order_ne_zero_iff_constCoeff_eq_zero).
---

# Roth.index_eq_zero_iff

## Inventory entry

### `theorem Roth.index_eq_zero_iff`
- **Type**: `{P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j) (α : σ → ℝ) : index P α r = 0 ↔ eval α P ≠ 0` (with `[Fintype σ]`)
- **What**: For a nonzero real polynomial and positive weights, the index of `P` at `α` is zero iff `P(α) ≠ 0`.
- **How**: (→) take the attaining multi-index from `exists_weight_eq_index`; its weight is `0`, so `weight_eq_zero_iff hr` gives `d = 0`, and `hasseDeriv_zero_apply` turns `(Δ_0 P)(α) ≠ 0` into `P(α) ≠ 0`. (←) antisymmetry of `index_nonneg` with `index_le_weight` at `d = 0` (weight `0`).
- **Hypotheses**: `hP : P ≠ 0` (otherwise the junk value `index 0 = 0` breaks (→); necessary, evidence (3a)); `hr : ∀ j, 0 < r j` (otherwise `d_j / 0 = 0` gives weight-zero nonzero multi-indices; necessary, evidence (3b)).
- **Uses from project**: `Roth.index`, `Roth.exists_weight_eq_index`, `Roth.index_nonneg`, `Roth.index_le_weight`, `Roth.weight_eq_zero_iff` (Roth/Box.lean:91), `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply` (Roth/HasseDeriv.lean:112)
- **Used by**: Roth/Index.lean:182 (`index_prod`, empty case: `index 1 α r = 0`)
- **Visibility**: public
- **Lines**: 96–106, proof length 7 lines
- **Notes**: listed under Main results in the module docstring; it is the second half of the source's first index lemma (clean.tex l.558–566).

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Index.lean:182, `index_prod`).
- Wrapper of 1–2 mathlib calls? No; it chains three project lemmas (`exists_weight_eq_index`, `weight_eq_zero_iff`, `index_le_weight`) plus `hasseDeriv_zero_apply`.
- Does mathlib have it? Not for `Roth.index`. Mathlib has the unweighted power-series analogue `MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` and the one-variable `Polynomial.rootMultiplicity_eq_zero_iff`; no weighted-order version.
- Too specific (inline?)? Only one call site, but it states a lemma of the source paper verbatim and is listed as a main result; inlining it into `index_prod` would hide that statement. Keep.
- Well-chosen? Yes; it matches the source statement exactly.
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal or auxiliary, Step 8 KEEP. The qualified name is not in mathlib (no `namespace Roth` under `Mathlib/`; grep `index_eq_zero_iff` hits only `Subgroup`/`GroupTheory/Index.lean`, an unrelated namespace). It is not a glue lemma (the proof is a 7-line argument, not `rfl`), so this is a full run. The parent `Roth.index` is BORDERLINE-needs-human (not NO-mathlib-has-it), so the re-aim rule does not force a re-aim, but the canonical analogue is checked anyway (Phase 4c row 7, Phase 6 attempt 2).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.index_eq_zero_iff`: ✓ resolved at Roth/Index.lean:98
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights (Roth §4)

### Statement (Phase 1)

`Roth.index_eq_zero_iff` is a theorem stating the following. Let `P ∈ ℝ[x_j : j ∈ σ]` be nonzero, `r ∈ ℕ^σ` with every `r_j > 0`, and `α ∈ ℝ^σ`. Then `ind_{α,r}(P) = 0` iff `P(α) ≠ 0`. Equivalently: the minimum of `∑ d_j / r_j` over the support of `P(x+α)` is zero exactly when the constant Taylor coefficient `P(α)` is nonzero.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite set of variables (needed by `Roth.weight`)
- `P`, `α`, `r`: polynomial, point, weights

Hypotheses (Lean side):
- `hP : P ≠ 0`: excludes the junk value `index 0 = 0`
- `hr : ∀ j, 0 < r j`: ensures only `d = 0` has weight zero

Conclusion (math): the index vanishes iff `P` does not vanish at `α`.

Conclusion (Lean): `index P α r = 0 ↔ eval α P ≠ 0`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under Main results, but it is a basic property of the project def `Roth.index` (the source's first, trivial lemma on the index), not a theorem of independent weight.

### One-line check (Phase 2b)

Body line count: 7 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | Roth's theorem index of polynomial "index" zero if and only if P does not vanish at the point | yes | index as min of `∑ i_j/d_j` over nonvanishing derivatives (arXiv math/0307203, 2502.00731, uh.edu Roth notes) | the iff is not stated separately; immediate since `i = 0` has weight 0 |
| 2 | WebSearch (general form) | weighted order of vanishing at a point equals zero iff polynomial nonzero at point | partial | unweighted: `ord_p P > 0` iff `P(p) = 0`, `ord 0 = ∞` (arXiv 1310.6482) | no weighted statement found; needs `P ≠ 0` with junk/∞ conventions |
| 3 | WebSearch (aliases) | power series order zero iff constant coefficient nonzero monomial valuation v(f)=0 unit | yes | `ord f = 0` iff `f(0) ≠ 0` (mathlib `PowerSeries.order` docs) | the standard fact in power-series language |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "if and only if", "ind(P) = 0" | yes | clean.tex l.558–566: lemma "`ind(P) ≥ 0` and `ind(P) = 0` iff `P(α) ≠ 0`", proof uses `r_j > 0` | the Lean statement is exactly the second half |
| 6 | nLab | order of vanishing / valuation | partial | valuation, order of a zero | no weighted multivariate point-order; the fact is folklore there |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing / multiplicity at a point | partial | `ord` along a divisor; a function is a unit at a point iff its order is 0 | same fact, unweighted |
| 9 | MathOverflow / Math.SE | (covered by #2, #3) | no | — | folklore; no stand-alone statement |
| 10 | recent arXiv (last 5 years) | (#1 hit 2502.00731 (2025)) | yes | same index definition | iff implicit |

### Literature summary (Phase 3)

Concept identified as: "order of vanishing zero iff nonvanishing at the point" for the weighted order (index) at `α`; equivalently, a (weighted) power series has order `0` iff its constant coefficient is nonzero.
Sources agree on the standard form: yes. All sources treat it as immediate from "minimum over the support" since only `d = 0` has weight `0` when weights are positive.
Most general standard form: for any semiring `R`, weights `w` with all `w_j ≠ 0`, and `f`, `ord_w(f) = 0 ↔ f(0) ≠ 0` (with `ord_w 0 = ∞`, no nonvanishing hypothesis needed).
Generality dimensions where the literature varies:
  - weights: ℕ (mathlib, unweighted `order` has `w = 1`) vs `1/r_j` reals (Roth); positivity always required
  - coefficients: ℝ (Roth) vs any semiring
  - value at `0`: `+∞` (source, mathlib) vs project junk `0`, which forces `hP`
Disagreement with the literature: none. `hP` stems only from the parent's junk-value convention (recorded in the parent report).

### Generality analysis — `Roth.index_eq_zero_iff`

Literature-standard form: `ord_w(f) = 0 ↔ f(0) ≠ 0` for positive weights.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | nonzero | not needed when `ord 0 = ∞` | no (for this def) | iff fails for `P = 0` (evidence (3a), compiled); removable only by changing the parent def |
| 2 | `hr : ∀ j, 0 < r j` | positive weights | positive weights | no | iff fails for `r = 0`, `P = X`, `α = 0` (evidence (3b), compiled) |
| 3 | coefficients `ℝ` | fixed by `Roth.index` | any semiring | inherited | parent def |
| 4 | `[Fintype σ]` | required | not needed | inherited | via `Roth.weight` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent definition `Roth.index`. Both hypotheses verified necessary (evidence (3a), (3b)).
Number of weakening opportunities found: 0 at the lemma level.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | `hr` is a pointwise positivity hypothesis, no class fits |
| 2 | sequences to filters? | no | — | finite algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | only via the parent def | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `(↑(taylor α P)).weightedOrder w = 0 ↔ eval α P ≠ 0` for positive `w`, i.e. generic `weightedOrder w f = 0 ↔ constantCoeff f ≠ 0` | composes from `MvPowerSeries.le_weightedOrder` + `weightedOrder_le` + `Finsupp.le_weight` (evidence (2)); mathlib has only the unweighted `order_ne_zero_iff_constCoeff_eq_zero` |
| 8 | concrete-via-abstract? | yes, trivially | proof only uses "finite min attained" + "only 0 has weight 0" | no new abstraction worth a lemma |
| 9 | false-generalisation guard | no false generalisation | the `weightedOrder` form is the canonical analogue but not a drop-in for the real-valued index (same caveat as parent) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no project-specific contribution. The re-aimed statement is a short composition of existing mathlib API. A generic `MvPowerSeries.weightedOrder_eq_zero_iff` (positive weights) would be a small convenience lemma beside `order_ne_zero_iff_constCoeff_eq_zero`, not this project's statement.

### Proof strategy — `Roth.index_eq_zero_iff`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | proof uses sibling API; a direct `csInf_mem`/`csInf_le` proof also compiles (evidence (1)) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (reuses the project's attained-minimum API rather than re-unfolding `sInf`).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "order of vanishing of a polynomial at a point is zero iff the polynomial does not vanish there"   hits: `Polynomial.rootMultiplicity_eq_zero_iff`, `rootMultiplicity_pos'` (one-variable analogues)
[B] Loogle            `MvPowerSeries.weightedOrder _ _ = 0`   only `MvPowerSeries.weightedOrder_one`; no iff
[C] LeanSearch        "weighted order of a multivariate power series is zero iff constant coefficient is nonzero"   hits: `MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` (unweighted), `FormalMultilinearSeries.order_eq_zero_iff`; no weighted version
[D] Grep mathlib src  `index_eq_zero_iff` (only GroupTheory/Index.lean, unrelated `Subgroup`); `weightedOrder` with `constantCoeff`/`= 0 ↔` (no hits); `one_le_order_iff_constCoeff_eq_zero`, `order_ne_zero_iff_constCoeff_eq_zero` (MvPowerSeries/Order.lean:480, 491); `Finsupp.le_weight`, `weight_eq_zero_iff_eq_zero` (Data/Finsupp/Weight.lean:134, 173)
[E] Name pattern      `lean_local_search` not run (grep [D] used instead, as in sibling reports)

Searched for both: the project form (index of a polynomial at a point is zero) and the literature-standard form (weighted order of a power series is zero iff constant coefficient nonzero).

Concluded: found building blocks (`Set.Nonempty.csInf_mem`, `csInf_le`, `Set.Finite.image`, `MvPolynomial.mem_support_iff`, `Finsupp.le_weight`); canonical analogue `MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` (unweighted) — the weighted analogue is absent but composes from `le_weightedOrder` / `weightedOrder_le`.

### Normal-form check

Equivalent formalisms: `index P α r = 0 ↔ eval α P ≠ 0`; `0 < index P α r ↔ eval α P = 0`; `index P α r ≠ 0 ↔ eval α P = 0` (mathlib's `order_ne_zero_iff_constCoeff_eq_zero` shape). Mathlib canonical form for orders: `order ≠ 0 ↔ constantCoeff = 0`. Our form is the negation of both sides; it matches the source sentence and the single call site (`.2 (by simp)` on `eval α 1 ≠ 0`). RHS convention respected: yes (the computable condition is on the RHS).

### Syntactic generality

Alternatives: the `≠ 0 ↔ = 0` form; a `0 < index ↔ eval = 0` form. Chosen: existing form, since the only consumer needs `index = 0` from `eval ≠ 0`.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP : P ≠ 0` | yes | evidence (3a) |
| 2 | `hr : ∀ j, 0 < r j` | yes | evidence (3b) |
| 3 | `[Fintype σ]` | yes (via `Roth.weight`) | inherited |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 1 (in the declaring file; 0 outside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern |
|---|---|
| Roth/Index.lean:182 | `exact (index_eq_zero_iff one_ne_zero hr α).2 (by simp)` (`index_prod`, empty product) |

Inline-derivation grep: none found (no other site proves `index … = 0` from `index_nonneg` + `index_le_weight` at `d = 0`).

### Composition check (Phase 6)

Can `Roth.index_eq_zero_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1 (direct, no sibling lemmas): `Set.Nonempty.csInf_mem` on the finite nonempty image + project `weight_eq_zero_iff` (→); `csInf_le` at `0` + `index_nonneg` (←); membership of `0` in the support via `mem_support_iff`, `coeff_taylor`, `hasseDeriv_zero_apply`.
  - Result: succeeds (evidence (1), compiled). It is a short glue proof on project API rather than a literal 3-call chain.

Attempt 2 (re-aim at the canonical object): `(↑(taylor α P)).weightedOrder w = 0 ↔ eval α P ≠ 0` for positive `w`, from `MvPowerSeries.le_weightedOrder` (with `Finsupp.le_weight` to see only `d = 0` has weight `< 1`) and `MvPowerSeries.weightedOrder_le` at `d = 0`.
  - Result: succeeds (evidence (2), compiled).

Conclusion: COMPOSABLE. It combines the attained-minimum property of a finite set with "weight zero only at `d = 0`" and `coeff_taylor` at `0`; the canonical analogue composes from existing mathlib weighted-order API.

## Verdict: `Roth.index_eq_zero_iff`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): standard and immediate from the definition (clean.tex l.558–566; the unweighted analogue "order 0 iff constant coefficient nonzero" is textbook).
- Generality analysis (Phase 4): MAXIMALLY GENERAL at the lemma level; `hP`, `hr` verified necessary (evidence (3a), (3b)).
- Mathlib search (Phase 5): building blocks `Set.Nonempty.csInf_mem`, `csInf_le`, `Finsupp.le_weight`; canonical analogue `MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` (unweighted).
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

Mathematically the lemma says that a finite minimum of nonnegative weights is zero exactly when the weight-zero point `d = 0` lies in the support, and that `d = 0` lies in the support of `P(X+α)` iff `P(α) ≠ 0`. With positive `r_j`, only `d = 0` has weight zero (`weight_eq_zero_iff`). Nothing here is new for mathlib. For mathlib's canonical object, `weightedOrder` of the Taylor expansion, the same statement composes from `le_weightedOrder`, `weightedOrder_le` and `Finsupp.le_weight` (evidence (2)). Mathlib lacks only a packaged weighted version of `order_ne_zero_iff_constCoeff_eq_zero`, which would be a generic convenience lemma, not this statement. The upstream fate of the lemma is tied to the parent `Roth.index` (BORDERLINE).

Locally it should stay: it is a verbatim lemma of the source paper and listed as a main result of the file. It has 1 call site (`index_prod`).

Belongs-elsewhere check: keep in Roth/Index.lean as basic API of `Roth.index`.
Mathlib building blocks: `Set.Nonempty.csInf_mem`, `csInf_le` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean), `Set.Finite.image`, `Set.Finite.bddBelow`, `MvPolynomial.mem_support_iff`; canonical analogue `MvPowerSeries.order_ne_zero_iff_constCoeff_eq_zero` (Mathlib/RingTheory/MvPowerSeries/Order.lean:491), `MvPowerSeries.le_weightedOrder`, `MvPowerSeries.weightedOrder_le`, `Finsupp.le_weight` (Mathlib/Data/Finsupp/Weight.lean:134).
Composition sketch (term-mode paraphrase of the compiled proof at Roth/Index.lean:100–106; the compiled direct composition is evidence (1)):
```lean
example (hP : P ≠ 0) (hr : ∀ j, 0 < r j) : index P α r = 0 ↔ eval α P ≠ 0 :=
  ⟨fun h ↦ by obtain ⟨d, hd, hdw⟩ := exists_weight_eq_index hP α r
              rw [h, weight_eq_zero_iff hr] at hdw; simpa [hdw, hasseDeriv_zero_apply] using hd,
   fun h ↦ (index_nonneg P α r).antisymm'
     (by simpa using index_le_weight (r := r) (d := 0) (by simpa [hasseDeriv_zero_apply] using h))⟩
```
Call sites in our project: 1 (Roth/Index.lean:182).
Refactor plan: none required. The single site `index_prod` keeps calling `index_eq_zero_iff`. If `Roth.index` is rebased on `weightedOrder (taylor α P)` (parent question 3), reprove it via the weighted analogue in evidence (2) plus the scaling bridge `index_eq_weightedOrder_div`; the call site is unchanged.
Next action: no upstreaming; keep as is. Optional generic follow-up: add `MvPowerSeries.weightedOrder_eq_zero_iff` (positive weights) next to `order_ne_zero_iff_constCoeff_eq_zero`.

---

## Next step

No upstreaming; keep `Roth.index_eq_zero_iff` as the local source lemma. Optionally propose a generic `MvPowerSeries.weightedOrder_eq_zero_iff` (with `∀ i, w i ≠ 0`) in Mathlib/RingTheory/MvPowerSeries/Order.lean; evidence (2) gives the proof idea.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_eq_zero_iff/compose_reaim_necessity.lean` (imports `Roth.Index`) compiled clean with `lake env lean` (no output, about 28 s per run; two runs, the first fixing elaboration details). It contains:
  - (1) direct composition via `Set.Nonempty.csInf_mem`, `csInf_le`, `weight_eq_zero_iff`, `coeff_taylor`, `hasseDeriv_zero_apply` (no sibling attained-minimum lemmas used except `index_nonneg`);
  - (2) re-aim: `(↑(taylor α P)).weightedOrder w = 0 ↔ eval α P ≠ 0` for positive `w` via `MvPowerSeries.le_weightedOrder`, `MvPowerSeries.weightedOrder_le`, `Finsupp.le_weight`;
  - (3a) `hP` necessary: the iff fails for `P = 0`;
  - (3b) `hr` necessary: for `σ = Unit`, `r = 0`, `P = X ()`, `α = 0` the index is `0` but `P(0) = 0`.
- WebSearch ×3 (queries in the literature table).
- Loogle `MvPowerSeries.weightedOrder _ _ = 0` (only `weightedOrder_one`); LeanSearch and Lean-Finder queries as recorded.
- Greps: project for call sites; mathlib for `index_eq_zero_iff`, weighted-order/constant-coefficient iffs, `Finsupp.le_weight`; clean.tex for "if and only if".
- `ask_chatgpt_math` MCP not configured in this session.
