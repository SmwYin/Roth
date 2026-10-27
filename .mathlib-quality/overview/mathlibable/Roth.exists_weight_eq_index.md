---
decl: Roth.exists_weight_eq_index
file: Roth/Index.lean
line: 76
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Attainment of the sInf-defined index of a nonzero polynomial is Set.Nonempty.csInf_mem on a finite nonempty image plus the project coeff_taylor (compiled); its mathlib-canonical counterpart is MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder (one call, compiled), so nothing new for mathlib; hP is necessary (compiled).
action: Keep locally as the attainment API lemma of Roth.index (used at Roth/Index.lean:101, 112, 226 and Roth/MainLemma.lean:457); do not upstream; if index is ever rebased on weightedOrder of taylor (parent question 3), reprove via MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder.
---

# Roth.exists_weight_eq_index

## Inventory entry

### `theorem Roth.exists_weight_eq_index`
- **Type**: `{P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r` (with `[Fintype σ]`)
- **What**: For a nonzero polynomial the index is an attained minimum: some multi-index `d` with `(Δ_d P)(α) ≠ 0` has weight `∑ d_j / r_j` exactly equal to `index P α r`.
- **How**: `Set.Nonempty.csInf_mem` applied to the image `weight r '' (taylor α P).support`, which is finite (`Finset.finite_toSet`, `Set.Finite.image`) and nonempty (`simpa using hP`, i.e. `taylor α P ≠ 0`); the support membership is translated by the private `mem_support_taylor_iff` (`mem_support_iff` + `coeff_taylor`).
- **Hypotheses**: `hP : P ≠ 0` (makes the support of the Taylor expansion nonempty; necessary, see evidence (3)).
- **Uses from project**: `Roth.index`, `Roth.weight`, `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, `Roth.mem_support_taylor_iff` (private), and the simp lemma(s) giving `taylor α P = 0 ↔ P = 0` used by `simpa using hP`
- **Used by**: Roth/Index.lean:101 (`index_eq_zero_iff`), :112 (`index_sub_weight_le_index_hasseDeriv`), :226 (`index_le_card`); Roth/MainLemma.lean:457 (`exists_hasseDeriv_eval_ne_zero`)
- **Visibility**: public
- **Lines**: 74–81, proof length 5 lines
- **Notes**: Companion of `index_le_weight` (the other half of "index = attained minimum"). No positivity of `r` needed.

## Junk check (Step 8)
- Used anywhere? Yes, 4 sites in 2 files.
- Wrapper of 1–2 mathlib calls? Essentially (`Set.Nonempty.csInf_mem` + finiteness), but it is the characterising "attained minimum" API lemma of the project def `Roth.index` and hides the `sInf`/image/support unfolding.
- Does mathlib have it? Not for `Roth.index` (project def). For mathlib's canonical weighted order the analogue is `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`.
- Too specific (inline?)? No: inlining would expose the `sInf` definition at 4 sites in 2 files.
- Well-chosen? Yes; matches the source's "Thus this is an attained minimum" (clean.tex l.545) and the shape of mathlib's analogue.
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, qualified name `Roth.exists_weight_eq_index` absent from mathlib (grep of `.lake/packages/mathlib/Mathlib`: no hit). Not a glue lemma (proof uses `csInf_mem`, not `rfl`), so full run. Parent `Roth.index` is BORDERLINE-needs-human (not NO-mathlib-has-it), so no re-aim rule applies; the canonical analogue is still checked (Phase 4c row 7, Phase 6 attempt 2).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.exists_weight_eq_index`: ✓ resolved at Roth/Index.lean:76
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights (Roth §4)

### Statement (Phase 1)

`Roth.exists_weight_eq_index` is a theorem stating the following: let `P ∈ ℝ[x_j : j ∈ σ]` be nonzero, `α ∈ ℝ^σ`, `r ∈ ℕ^σ`. Then there is a multi-index `d` with `(Δ_d P)(α) ≠ 0` (equivalently, the coefficient of `x^d` in `P(x + α)` is nonzero) such that `∑_j d_j / r_j = ind_{α,r}(P)`. That is, the minimum defining the index is attained.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite set of variables (needed by `Roth.weight`)
- `P`, `α`, `r`: polynomial, point, weights

Hypotheses (Lean side):
- `hP : P ≠ 0`: the support of `P(X + α)` is nonempty

Conclusion (math): the index of a nonzero polynomial is attained by some multi-index in the support of its Taylor expansion.

Conclusion (Lean): `∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the project def `Roth.index`; not a main result, not named.

### One-line check (Phase 2b)

Body line count: 5 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | Roth's theorem index of a polynomial "attained" minimum derivative nonvanishing weight sum i_j/r_j | yes | index = smallest `∑ j_i/r_i` over tuples with nonzero derivative coefficient (arXiv math/0307203, 2502.00731, Evertse Bonn slides, Natarajan–Thangadurai ch. "Roth's Theorem") | attainment is implicit in "smallest value" over a finite set; never stated separately |
| 2 | WebSearch (general form) | weighted order of power series attained by a nonzero monomial coefficient of minimal weighted degree | yes | mathlib docs: "If the order of a formal power series f is finite, then some coefficient of weight equal to the order of f is nonzero"; η-order of polynomials (arXiv 0811.0414) as a min over nonzero coefficients | the general form is exactly mathlib's `exists_coeff_ne_zero_and_weightedOrder` |
| 3 | WebSearch (aliases) | monomial valuation minimum attained support initial form weighted degree polynomial | yes | monomial valuation / weighted degree as min (or max) over the support (Meunier, Teissier, arXiv 1607.04860); initial form = terms attaining the extremum | attainment is what makes the initial form nonzero; definitional |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` "attained" | yes | clean.tex l.545 "this is an attained minimum"; l.566 "The minimum is attained" | the lemma is exactly this sentence of the source |
| 6 | nLab | order of vanishing / valuation | partial | valuation, order of vanishing | no weighted multivariate version; nothing at this granularity |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing | partial | `ord` along a divisor | no weighted point-order; attainment would be definitional there too |
| 9 | MathOverflow / Math.SE | (covered by #2, #3 results) | no | — | folklore; no stand-alone statement |
| 10 | recent arXiv (last 5 years) | (#1 result 2502.00731 (2025), #3 result 2601.18519) | yes | same definitions | attainment implicit |

### Literature summary (Phase 3)

Concept identified as: attainment of the minimum defining the index / weighted order of vanishing at a point / monomial valuation (the minimum over the finite nonempty support of `P(X+α)`).
Sources agree on the standard form: yes; every source defines the index as a minimum ("smallest value") over a finite set, so attainment is definitional.
Most general standard form: for any (semi)ring `R`, weights `w`, and nonzero `f`, some `d` with `coeff_d f ≠ 0` has `⟨w, d⟩ = ord_w(f)`; at a point apply to `f = P(X + α)`.
Generality dimensions where the literature varies:
  - weights: ℕ (mathlib, algebraic geometry) vs real `1/r_j` (Roth)
  - coefficients: ℝ (Roth) vs any (semi)ring
  - value at `0`: `+∞` (source, mathlib) vs junk `0` (project); the hypothesis `P ≠ 0` is required in every form
Disagreement with the literature: none.

### Generality analysis — `Roth.exists_weight_eq_index`

Literature-standard form: nonzero `f` has some `d ∈ supp f` with `⟨w, d⟩ = ord_w(f)`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | nonzero polynomial | `f ≠ 0` (or finite order) | no | necessary: for `P = 0` the conclusion is false (evidence (3), compiled) |
| 2 | coefficients `ℝ` | fixed by `Roth.index` | any semiring | inherited | determined by the parent def |
| 3 | `[Fintype σ]` | required | not needed | inherited | only via `Roth.weight` (parent row 4) |
| 4 | positivity of `r` | not assumed | — | already maximal | holds for all `r` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent definition `Roth.index`; the only hypothesis `hP` is verified necessary (evidence (3)); further generality lives in the parent def.
Number of weakening opportunities found: 0 at the lemma level.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic minimum |
| 3 | construction vs universal property? | no | (parent: monomial valuation) | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | only via the parent def | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `∃ d, eval α (Δ_d P) ≠ 0 ∧ (weight w d : ℕ∞) = (↑(taylor α P)).weightedOrder w` | exactly `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` (evidence (2)) |
| 8 | concrete-via-abstract? | yes, trivially | proof only uses "sInf of a finite nonempty set is a member" | that abstract fact is mathlib's `Set.Nonempty.csInf_mem` |
| 9 | false-generalisation guard | no false generalisation in the re-aim itself | the `weightedOrder` form is the canonical analogue but, as for the parent, not a drop-in replacement for the real-valued `index` (needs `0 < r`, `toNat`, scaling by `∏ r`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but already in mathlib: the re-aimed statement is `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, so there is nothing to contribute.

### Proof strategy — `Roth.exists_weight_eq_index`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | proof is `Set.Nonempty.csInf_mem` + finiteness | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (direct `csInf_mem` on a finite nonempty image).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "infimum of a finite nonempty set of reals is attained by some element"   hits: `Set.Nonempty.csInf_mem`, `Finset.Nonempty.csInf_mem`, `exists_eq_ciInf_of_finite`, `Finset.exists_mem_eq_inf'` (building blocks)
[B] Loogle            `∃ d, MvPowerSeries.coeff d _ ≠ 0 ∧ _`   hits: `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `exists_coeff_ne_zero_and_order`, `weightedOrder_eq_nat`, `ne_zero_iff_exists_coeff_ne_zero_and_weight` (canonical analogue)
[C] LeanSearch        "nonzero power series has a nonzero coefficient whose weight equals the weighted order"   hits: same as [B], plus `PowerSeries.coeff_order`
[D] Grep mathlib src  `exists_weight_eq_index` (no hit), `exists_coeff_ne_zero_and_weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean:161), `csInf_mem` (Order/ConditionallyCompleteLattice/Basic.lean:462, Finset.lean)
[E] Name pattern      `lean_local_search` not run (grep [D] used instead; previous workers recorded it unavailable, ripgrep missing)

Searched for both: the project form (index of a polynomial at a point, attained) and the literature-standard form (weighted order of a nonzero power series attained by a support element).

Concluded: found building blocks (`Set.Nonempty.csInf_mem`, `Set.Finite.image`, `Finset.finite_toSet`, `MvPolynomial.mem_support_iff`); canonical analogue `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` for the ℕ-weighted order.

### Normal-form check

Equivalent formalisms: `∃ d ∈ (taylor α P).support, weight r d = index P α r`; `index P α r ∈ weight r '' (taylor α P).support`; the Hasse-derivative form used here. The project's convention (Hasse-derivative form, as in the source and `index_le_weight`) is consistent across the file. RHS convention respected: yes (`weight r d = index ...`, matching mathlib's `weight w d = weightedOrder w f`).

### Syntactic generality

Alternatives: set-membership form; `∃ d ∈ support` form. Chosen: the existing `∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r`, since all 4 call sites consume exactly a nonvanishing derivative plus the weight equation via `obtain`.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP : P ≠ 0` | yes | conclusion false for `P = 0` (evidence (3)) |
| 2 | `[Fintype σ]` | yes (via `Roth.weight`) | inherited from parent |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 4 (1 outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern |
|---|---|
| Roth/Index.lean:101 | `obtain ⟨d, hd, hdw⟩ := exists_weight_eq_index hP α r` (`index_eq_zero_iff`) |
| Roth/Index.lean:112 | `obtain ⟨i, hi, hiw⟩ := exists_weight_eq_index hk α r` (`index_sub_weight_le_index_hasseDeriv`) |
| Roth/Index.lean:226 | `obtain ⟨d, hd0, hdw⟩ := exists_weight_eq_index hP α r` (`index_le_card`) |
| Roth/MainLemma.lean:457 | `(exists_weight_eq_index hP α r).imp fun _ ⟨hd, hw⟩ ↦ ⟨hw ▸ hc, hd⟩` (`exists_hasseDeriv_eval_ne_zero`) |

Inline-derivation grep: (none); no other site applies `csInf_mem` to the index set.

### Composition check (Phase 6)

Can `Roth.exists_weight_eq_index` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(nonempty).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))`, then translate support membership by `simpa [mem_support_iff, coeff_taylor]`
  - Mathlib decls used: `Set.Nonempty.csInf_mem`, `Set.Finite.image`, `Finset.finite_toSet`, `MvPolynomial.mem_support_iff`; project `MvPolynomial.coeff_taylor`
  - Result: succeeds (evidence (1), compiled)

Attempt 2 (re-aim at the canonical object): `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder w ((ne_zero_iff_weightedOrder_finite w).1 h0)` with `h0 : (↑(taylor α P) : MvPowerSeries σ ℝ) ≠ 0`
  - Result: succeeds (evidence (2), compiled); one mathlib call plus the nonvanishing bridge.

Conclusion: COMPOSABLE (one `csInf_mem` application on a finite nonempty set, modulo the project's `coeff_taylor`; the canonical analogue is a single mathlib lemma).

## Verdict: `Roth.exists_weight_eq_index`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): every source defines the index / weighted order / monomial valuation as a minimum over a finite support, so attainment is definitional (clean.tex l.545 "attained minimum").
- Generality analysis (Phase 4): MAXIMALLY GENERAL at the lemma level; `hP` verified necessary.
- Mathlib search (Phase 5): building block `Set.Nonempty.csInf_mem`; canonical analogue `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

The lemma is the "minimum is attained" half of the definition of `Roth.index`: `Set.Nonempty.csInf_mem` applied to the finite nonempty set `weight r '' supp(P(X+α))`, with support membership translated into Hasse-derivative language by `coeff_taylor`. Mathematically nothing is new for mathlib: for mathlib's canonical weighted order the identical statement is `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, and evidence (2) shows the Taylor-expansion version is one call to it. Its upstream fate is tied to the parent (`Roth.index`, BORDERLINE): if a weighted order at a point is upstreamed, this lemma is subsumed by `exists_coeff_ne_zero_and_weightedOrder`.

As with its sibling `index_le_weight`, it should not be inlined: it is the characterising API lemma of a project definition with 4 call sites in 2 files, and inlining would expose the `sInf`/image/support unfolding. Junk verdict KEEP.

Belongs-elsewhere check: keep in Roth/Index.lean as the basic API of `Roth.index`.
Mathlib building blocks: `Set.Nonempty.csInf_mem` (Mathlib/Order/ConditionallyCompleteLattice/Finset.lean), `Set.Finite.image`, `Finset.finite_toSet`, `MvPolynomial.mem_support_iff`; canonical analogue `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean:161).
Composition sketch:
```lean
example (hP : P ≠ 0) : ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by
  obtain ⟨d, hd, hdw⟩ := (show (weight r '' ((taylor α P).support : Set _)).Nonempty by
    simpa using hP).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))
  exact ⟨d, by simpa [mem_support_iff, coeff_taylor] using hd, hdw⟩
```
Call sites in our project: 4 (Roth/Index.lean:101, 112, 226; Roth/MainLemma.lean:457).
Refactor plan: none. The 4 sites keep calling `exists_weight_eq_index`; inlining is not recommended because the lemma is the def's interface. If `Roth.index` is rebased on `weightedOrder (taylor α P)` (parent question 3), reprove it via `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` plus the scaling bridge `index_eq_weightedOrder_div`; call sites stay unchanged.
Next action: no upstreaming; keep as is.

---

## Next step

No upstreaming; keep `Roth.exists_weight_eq_index` as the local API lemma of `Roth.index`. Revisit only if the parent's question 3 (rebase on `MvPowerSeries.weightedOrder`) is answered yes, in which case reprove via `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.exists_weight_eq_index/compose_and_reaim.lean` (imports `Roth.Index`), compiled clean with `lake env lean` (no output, rc 0; first run failed only because `w` is an explicit argument of `exists_coeff_ne_zero_and_weightedOrder`, fixed): (1) composition via `Set.Nonempty.csInf_mem` + `coeff_taylor`; (2) re-aimed statement for `(↑(taylor α P)).weightedOrder w` via `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` + `ne_zero_iff_weightedOrder_finite`; (3) `hP` is necessary: the conclusion fails for `P = 0` (closed by `simp`).
- WebSearch ×3 (queries in the literature table); Loogle `∃ d, MvPowerSeries.coeff d _ ≠ 0 ∧ _`; LeanSearch and Lean-Finder queries as recorded; grep of mathlib for `exists_weight_eq_index`, `exists_coeff_ne_zero_and_weightedOrder`, `csInf_mem`; grep of clean.tex for "attained".
- `ask_chatgpt_math` MCP not configured in this session.
