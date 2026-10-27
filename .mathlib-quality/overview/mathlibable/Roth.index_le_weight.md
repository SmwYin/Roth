---
decl: Roth.index_le_weight
file: Roth/Index.lean
line: 69
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The defining upper bound of the sInf-defined index (index at most the weight of any d with Hasse derivative nonvanishing at α) is csInf_le of a finite image plus the project coeff_taylor (compiled); its mathlib-canonical counterpart is MvPowerSeries.weightedOrder_le (one call, compiled), so nothing new for mathlib.
action: Keep locally as the basic API lemma of Roth.index (used at Roth/Index.lean:87, 105, 114, 153, 245 and Roth/Main.lean:401); do not upstream; if index is ever rebased on weightedOrder of taylor (parent question 3), reprove via MvPowerSeries.weightedOrder_le.
---

# Roth.index_le_weight

## Inventory entry

### `theorem Roth.index_le_weight`
- **Type**: `{P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ} (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d` (with `[Fintype σ]`)
- **What**: The index of `P` at `α` with weights `r` is at most the weight `∑ d_j / r_j` of any multi-index `d` whose Hasse derivative `Δ_d P` does not vanish at `α`.
- **How**: `csInf_le` applied to the image `weight r '' (taylor α P).support`, which is bounded below because it is finite (`Finset.finite_toSet`, `Set.Finite.image`, `Set.Finite.bddBelow`); membership via `Set.mem_image_of_mem` and the private `mem_support_taylor_iff` (`mem_support_iff` + `coeff_taylor`).
- **Hypotheses**: `h`: the `d`-th Hasse derivative of `P` is nonzero at `α`, i.e. `d` lies in the support of `P(X + α)`.
- **Uses from project**: `Roth.index`, `Roth.weight`, `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, `Roth.mem_support_taylor_iff` (private; via `MvPolynomial.coeff_taylor`)
- **Used by**: Roth/Index.lean:87 (`le_index_iff`), :105 (`index_eq_zero_iff`), :114 (`index_sub_weight_le_index_hasseDeriv`), :153 (`index_eq_weightedOrder_div`), :245 (`index_unique`); Roth/Main.lean:401
- **Visibility**: public
- **Lines**: 66–72, proof length 2 lines
- **Notes**: no positivity of `r` needed (the `sInf` def is total in `r`); no `P ≠ 0` needed (vacuous then).

## Junk check (Step 8)
- Used anywhere? Yes, 6 sites in 2 files (5 in Index.lean, 1 in Main.lean).
- Wrapper of 1–2 mathlib calls? Essentially yes (`csInf_le` + `Set.Finite.bddBelow`), but it is the characterising API lemma of the project definition `Roth.index`, and it hides the `sInf`/image/support unfolding from every caller.
- Does mathlib have it? Not for `Roth.index` (a project def). For mathlib's canonical weighted order it is `MvPowerSeries.weightedOrder_le`.
- Too specific (inline?)? No: inlining would expose the `sInf` definition at 6 sites.
- Well-chosen? Yes; standard shape (`foo_le` from membership), stated via Hasse derivatives as in the source.
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, qualified name `Roth.index_le_weight` absent from mathlib (grep). Not a glue lemma (`csInf_le` proof, not `rfl`), so full run.

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.index_le_weight`: ✓ resolved at Roth/Index.lean:69
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights (Roth §4)

### Statement (Phase 1)

`Roth.index_le_weight` is a theorem stating the following: let `P ∈ ℝ[x_j : j ∈ σ]`, `α ∈ ℝ^σ`, `r ∈ ℕ^σ`. If `d` is a multi-index with `(Δ_d P)(α) ≠ 0` (equivalently the coefficient of `x^d` in `P(x + α)` is nonzero), then `ind_{α,r}(P) ≤ ∑_j d_j / r_j`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the finite set of variables (needed by `Roth.weight`'s sum)
- `P`, `α`, `r`, `d`: polynomial, point, weights, multi-index

Hypotheses (Lean side):
- `h : eval α (hasseDeriv d P) ≠ 0`: `d` is in the support of the Taylor expansion

Conclusion (math): the index is at most the weight of any support element (the minimum is a lower bound of the set it minimises over).

Conclusion (Lean): `index P α r ≤ weight r d`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the project def `Roth.index`; not a main result, not named.

### One-line check (Phase 2b)

Body line count: 2 (proof term)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | index of a polynomial at a point Roth's theorem "index" minimum weighted derivative nonvanishing | yes | index = min of `∑ i_j/r_j` over `i` with `Δ_i P(α) ≠ 0` (arXiv math/0307203, 2502.00731, 1806.10737, Evertse notes) | the bound "index ≤ weight of a nonvanishing derivative" is immediate from the definition as a minimum; never stated as a separate lemma |
| 2 | WebSearch (general form) | weighted order of vanishing multivariate polynomial at most weighted degree of any nonzero monomial coefficient | partial | weighted multiplicity `m_w(F, a)` (arXiv 1707.01354) | the bound is treated as immediate from "minimum over support" |
| 3 | WebSearch (aliases) | monomial valuation definition minimum over support weighted degree | yes | monomial valuation `v_w(P) = min_{d ∈ supp P} ⟨w, d⟩` (arXiv 1607.04860, 1802.00481, Toulouse notes) | same: `v_w(P) ≤ ⟨w, d⟩` for `d ∈ supp P` is definitional |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` "minimum" | yes | clean.tex l.530–556: index defined as "the minimum of all numbers of the form ∑ i_j/r_j" over tuples with `Δ_i P(α) ≠ 0`; "attained minimum" | the lemma is the "minimum ≤ each element" half of the definition |
| 6 | nLab | order of vanishing / valuation | partial | valuation, order of vanishing at a point | no weighted multivariate version; nothing at this granularity |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing | partial | `ord` along a divisor | no weighted point-order; the inequality would be definitional there too |
| 9 | MathOverflow / Math.SE | (covered by #2, #3 results) | no | — | folklore; no stand-alone statement |
| 10 | recent arXiv (last 5 years) | (#1 results: 2502.00731 (2025)) | yes | same definition | inequality implicit |

### Literature summary (Phase 3)

Concept identified as: the trivial bound "weighted order ≤ weighted degree of any monomial in the support" for the index / weighted order of vanishing at a point / monomial valuation.
Sources agree on the standard form: yes; every source defines the index as a minimum, so the bound is definitional and never stated separately.
Most general standard form: for any (semi)ring `R`, weight vector `w`, and `f` with `coeff_d f ≠ 0`, `ord_w(f) ≤ ⟨w, d⟩`; at a point, apply to `f = P(X + α)`.
Generality dimensions where the literature varies:
  - weights: ℕ (mathlib, algebraic geometry) vs real `1/r_j` (Roth)
  - coefficients: ℝ (Roth) vs any ring
Disagreement with the literature: none (the junk value at `P = 0` is irrelevant here since `h` forces `P ≠ 0`).

### Generality analysis — `Roth.index_le_weight`

Literature-standard form: `ord_w(f) ≤ ⟨w, d⟩` whenever `coeff_d f ≠ 0`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `h : eval α (hasseDeriv d P) ≠ 0` | nonvanishing Hasse derivative | `coeff_d P(X+α) ≠ 0` | no (equivalent) | same condition via `coeff_taylor`; needed (e.g. `P = X`, `α = 0`, `r = 1`, `d = 0` gives index 1 > 0) |
| 2 | coefficients `ℝ` | fixed by `Roth.index` | any semiring | inherited | determined by the parent def (parent row 1) |
| 3 | `[Fintype σ]` | required | not needed | inherited | only through `Roth.weight` (parent row 4) |
| 4 | positivity of `r` | not assumed | — | already maximal | the lemma holds for all `r` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent definition `Roth.index`; any further generality (ring, `Fintype`) lives in the parent def, not in this lemma.
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
| 7 | concrete index to general? | yes (re-aim) | `(↑(taylor α P)).weightedOrder w ≤ Finsupp.weight w d` | exactly `MvPowerSeries.weightedOrder_le` (evidence (2)) |
| 8 | concrete-via-abstract? | yes, trivially | the proof only uses "sInf of a finite set ≤ each member" | that abstract fact is mathlib's `csInf_le` + `Set.Finite.bddBelow` |
| 9 | false-generalisation guard | no false generalisation in the re-aim itself | the `weightedOrder` statement is the canonical analogue; as with the parent, it is not a drop-in replacement for the real-valued `index` (needs `0 < r` and `toNat`/scaling) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but already in mathlib: the re-aimed statement is `MvPowerSeries.weightedOrder_le`, so there is nothing to contribute.

### Proof strategy — `Roth.index_le_weight`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`csInf_le` on a finite, hence bounded-below, image; evidence (1) is an equivalent 2-line variant with an anonymous-constructor membership).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_le_weight`

[A] Lean-Finder       "infimum of a finite image set is at most the value at any element"   hits: `Finset.inf'_le`, `Finset.inf_le`, `Finite.ciInf_le` (building blocks)
[B] Loogle            `MvPowerSeries.weightedOrder _ _ ≤ _`   hits: `MvPowerSeries.weightedOrder_le`, `le_weightedOrder_map`, `le_weightedOrder_smul`, `le_weightedOrder_subst_of_forall_ne_zero`
[C] LeanSearch        "weighted order of a power series is at most the weight of any index with nonzero coefficient"   hits: `MvPowerSeries.weightedOrder_le`, `MvPowerSeries.order_le`, `PowerSeries.order_le`
[D] Grep mathlib src  `theorem weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean:171); `index_le_weight`, `weightedOrderAt` (no hits); `coeff_taylor` for MvPolynomial (none; project Roth/Taylor.lean:134)
[E] Name pattern      `lean_local_search` unavailable (ripgrep not on PATH); replaced by grep [D] and by compiling the names used in evidence (`MvPowerSeries.weightedOrder_le`, `MvPolynomial.coeff_coe`, `csInf_le`, `Set.Finite.bddBelow`)

Searched for both the user's form (real-valued `sInf` index) and the literature-standard form (weighted order bounded by weight of a support element).

Concluded: found building blocks (`csInf_le`, `Set.Finite.bddBelow`, `Set.Finite.image`) giving the Roth form, and found the canonical analogue `MvPowerSeries.weightedOrder_le` (identical content for mathlib's weighted order, ℕ weights). `Roth.index` itself is not in mathlib (parent BORDERLINE).

### Normal-form check — `Roth.index_le_weight`

Equivalent formalisms: (a) hypothesis via Hasse derivative `eval α (hasseDeriv d P) ≠ 0` (current); (b) via `coeff d (taylor α P) ≠ 0`; (c) `d ∈ (taylor α P).support`.
Mathlib canonical form: `weightedOrder_le` uses `coeff d f ≠ 0` (form (b)).
Our statement uses (a), matching the source's definition and every call site (all supply Hasse-derivative nonvanishing). OK; the private `mem_support_taylor_iff` is the bridge.
RHS convention respected? n/a (inequality, not iff).

### Syntactic generality — `Roth.index_le_weight`

Alternative restatements attempted:
- hypothesis `coeff d (taylor α P) ≠ 0` (form (b))
- `index P α r ≤ c` from `weight r d ≤ c` (an `_of_le` variant)
Chosen restatement: current (a).
Justification: all 6 call sites have a Hasse-derivative nonvanishing fact in hand; the `_of_le` variant is just `.trans`.

### Superfluous-argument audit — `Roth.index_le_weight`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `h` | yes | without it the bound fails (`P = X`, `α = 0`, `r = 1`, `d = 0`) |
| 2 | `[Fintype σ]` | via `Roth.weight` only | parent-level, not removable here |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as project API)

### Call sites — `Roth.index_le_weight`

Internal use count: 1 outside the declaring file (5 more inside Roth/Index.lean)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:87 | `refine ⟨fun h d hd ↦ h.trans (index_le_weight hd), ...⟩` (`le_index_iff`) |
| Roth/Index.lean:105 | `simpa using index_le_weight (r := r) (d := 0) ...` (`index_eq_zero_iff`) |
| Roth/Index.lean:114 | `... using index_le_weight (r := r) hi.2` (`index_sub_weight_le_index_hasseDeriv`) |
| Roth/Index.lean:153 | `exact index_le_weight (by simpa [F, MvPolynomial.coeff_coe, coeff_taylor] using hd)` (`index_eq_weightedOrder_div`) |
| Roth/Index.lean:245 | `simpa [weight, hqdef] using index_le_weight (P := P) (α := α) (r := r) ...` (`index_unique`) |
| Roth/Main.lean:401 | `... hqr d (hidx.trans (index_le_weight h0))` |

Inline-derivation grep: (none); no other site applies `csInf_le` to the index set directly.

### Composition check (Phase 6)

Can `Roth.index_le_weight` be derived from mathlib in ≤3 chained calls?

Attempt 1: `csInf_le ((taylor α P).support.finite_toSet.image _).bddBelow ⟨d, by simpa [mem_support_iff, coeff_taylor] using h, rfl⟩`
  - Mathlib decls used: `csInf_le`, `Set.Finite.bddBelow`, `Set.Finite.image`, `Finset.finite_toSet`, `MvPolynomial.mem_support_iff`; plus project `MvPolynomial.coeff_taylor`
  - Result: succeeds (evidence (1), compiled)

Attempt 2 (re-aim at the canonical object): `MvPowerSeries.weightedOrder_le w (by simpa [MvPolynomial.coeff_coe, coeff_taylor] using h)` proves `(↑(taylor α P)).weightedOrder w ≤ Finsupp.weight w d`
  - Result: succeeds (evidence (2), compiled); one mathlib call.

Conclusion: COMPOSABLE (one `csInf_le` application on a finite set, modulo the project's `coeff_taylor`; the canonical analogue is a single mathlib lemma).

## Verdict: `Roth.index_le_weight`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): every source defines the index / weighted order / monomial valuation as a minimum over the support, so this bound is definitional and never a stand-alone result.
- Generality analysis (Phase 4): MAXIMALLY GENERAL at the lemma level; remaining generality belongs to the parent def.
- Mathlib search (Phase 5): building blocks `csInf_le` + `Set.Finite.bddBelow`; canonical analogue `MvPowerSeries.weightedOrder_le`.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

The lemma is the "minimum ≤ each member" half of the definition of `Roth.index`: `csInf_le` applied to the finite (hence bounded-below) set `weight r '' supp(P(X+α))`, with the support condition translated into Hasse-derivative language by the project's `coeff_taylor`. Mathematically there is nothing to add to mathlib: for mathlib's canonical weighted order the identical statement is already `MvPowerSeries.weightedOrder_le`, and evidence (2) shows the Taylor-expansion version is one call to it. Its upstream fate is tied to the parent (`Roth.index`, BORDERLINE): if a weighted order at a point is ever upstreamed, this lemma is subsumed by `weightedOrder_le`, not shipped separately.

Unlike a typical NO-composable wrapper, it should not be inlined: it is the characterising API lemma of a project definition, with 6 call sites, and inlining would expose the `sInf`/image/support unfolding at each one. Junk verdict KEEP.

Belongs-elsewhere check: keep in the project file Roth/Index.lean as the basic API of `Roth.index`.
Mathlib building blocks: `csInf_le` (Mathlib/Order/ConditionallyCompleteLattice/Defs.lean area, class lemma of `ConditionallyCompleteLattice`), `Set.Finite.bddBelow`, `Set.Finite.image`, `Finset.finite_toSet`, `MvPolynomial.mem_support_iff`; canonical analogue `MvPowerSeries.weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean:171).
Composition sketch:
```lean
example (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d :=
  csInf_le ((taylor α P).support.finite_toSet.image _).bddBelow
    ⟨d, by simpa [mem_support_iff, coeff_taylor] using h, rfl⟩
```
Call sites in our project: 6 (Roth/Index.lean:87, 105, 114, 153, 245; Roth/Main.lean:401).
Refactor plan: none. The 6 sites keep calling `index_le_weight`. Inlining is not recommended because the lemma is the def's interface. If `Roth.index` is rebased on `weightedOrder (taylor α P)` (parent question 3), reprove it as `MvPowerSeries.weightedOrder_le` plus the scaling bridge, and the call sites stay unchanged.
Next action: no upstreaming; keep as is.

---

## Next step

No upstreaming; keep `Roth.index_le_weight` as the local API lemma of `Roth.index`. Revisit only if the parent's question 3 (rebase on `MvPowerSeries.weightedOrder`) is answered yes, in which case reprove via `MvPowerSeries.weightedOrder_le`.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_le_weight/compose_and_reaim.lean` (imports `Roth.Index`), compiled clean with `lake env lean` (no output, rc 0): (1) the composition via `csInf_le` + `Set.Finite.bddBelow` + `coeff_taylor`; (2) the re-aimed statement for `(↑(taylor α P)).weightedOrder w` as one call to `MvPowerSeries.weightedOrder_le`; (3) the `d = 0` specialisation used at Index.lean:105.
- WebSearch ×3 (queries in the literature table); Loogle `MvPowerSeries.weightedOrder _ _ ≤ _`; LeanSearch and Lean-Finder queries as recorded; grep of mathlib for `weightedOrder_le`, `index_le_weight`, `weightedOrderAt`, `coeff_taylor`; grep of clean.tex for "minimum".
- `lean_local_search` unavailable (ripgrep not installed); `ask_chatgpt_math` MCP not configured in this session.
