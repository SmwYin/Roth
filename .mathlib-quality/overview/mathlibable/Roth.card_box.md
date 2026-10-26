---
decl: Roth.card_box
file: Roth/Box.lean
line: 57
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Re-aimed at the parent's mathlib form Finset.Iic, the count is Pi.card_Iic plus Nat.card_Iic (or Finsupp.card_Iic plus Nat.card_Iic plus Finset.prod_subset), and for the current def it is card_map plus card_piFinset plus card_range; all verified in evidence, nothing new for mathlib.
action: Keep as the local cardinality lemma of Roth.box (used at Roth/Box.lean:68, Roth/Main.lean:405, Roth/Lattice.lean:163); if box is redefined via Finset.Iic, reprove via Finsupp.card_Iic, Nat.card_Iic and Finset.prod_subset; do not upstream.
---

# Roth.card_box

## Inventory entry

### `theorem Roth.card_box`
- **Type**: `{σ : Type*} [Fintype σ] [DecidableEq σ] (r : σ → ℕ) : (Roth.box r).card = ∏ j, (r j + 1)`
- **What**: The box of multi-indices `{d : σ →₀ ℕ : ∀ j, d j ≤ r j}` has `∏ j (r j + 1)` elements.
- **How**: `simp [box]` — unfolds `box` to `Finset.map` of `Fintype.piFinset (fun j ↦ range (r j + 1))`; simp closes with `Finset.card_map`, `Fintype.card_piFinset`, `Finset.card_range`.
- **Hypotheses**: none beyond the section variables `[Fintype σ] [DecidableEq σ]` (required by `box`).
- **Uses from project**: `Roth.box`
- **Used by**: Roth/Box.lean:68 (`card_le_card_box`, which is in turn used at Roth/MainLemma.lean:506 and Roth/CoeffNorm.lean:264); Roth/Main.lean:405 (`rw [Finset.sum_const, card_box, nsmul_eq_mul]`); Roth/Lattice.lean:163 (`simp [card_box]`).
- **Visibility**: public
- **Lines**: 54–58, proof length 1 line
- **Notes**: Not a `:= rfl`/`Iff.rfl` glue lemma. The parent `Roth.box` is NO-mathlib-has-it because mathlib has the more general `Finset.Iic`, so per the re-aim rule this lemma was assessed against `#(Finset.Iic _)` rather than inherited. Listed under "Main results" in the Box.lean module docstring.

## Junk check (Step 8)
- Used anywhere? Yes: 3 direct uses (Box.lean:68, Main.lean:405, Lattice.lean:163), plus indirect via `card_le_card_box`.
- Wrapper of 1–2 mathlib calls? Yes: for the current definition it is `card_map` + `Fintype.card_piFinset` + `card_range` (one `simp`); in the re-aimed `σ → ℕ` interval form it is `Pi.card_Iic` + `Nat.card_Iic`.
- Does mathlib have it? Not verbatim (mathlib states `Finsupp.card_Iic` as a product over `f.support`, and `Pi.card_Iic` for `σ → α`); composable in at most 3 calls (evidence).
- Too specific (inline)? No: the box is a named project def with three consumers; the `card_` lemma is the standard companion API and insulates call sites from the implementation of `box`.
- Well-chosen? Yes, usual `card_` shape with explicit product RHS consumed directly at Main.lean:405 and Lattice.lean:163.
- Conclusion: `KEEP` — action: keep as the cardinality lemma of `Roth.box`; if `box` is redefined as `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (parent's recommendation), reprove by `rw [Finsupp.card_Iic]; simp only [Nat.card_Iic]; rw [prod_subset ...]; simp` (evidence).

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.card_box` not in mathlib (no `namespace Roth` in Mathlib; the mathlib `Behrend.card_box` and `Finset.card_box` are unrelated boxes). Not a pure glue lemma, and the parent `Roth.box` is NO-mathlib-has-it via the more general `Finset.Iic`, so the **re-aim rule** applies: full run re-aimed at `#(Finset.Iic r)`. The re-aim is a near-hit: mathlib has `Pi.card_Iic` (univ product, `σ → α`) and `Finsupp.card_Iic` (support product, `σ →₀ α`), but not the finsupp univ-product form verbatim; composition succeeds in ≤3 calls.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` and `Mathlib.Data.Pi.Interval` has no diagnostics)
- decl `Roth.card_box`:      resolved at Roth/Box.lean:57
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.card_box` is a theorem stating the following: for a finite index set `σ` and bounds `r ∈ ℕ^σ`, the box `B(r) = {d ∈ ℕ^σ : d_j ≤ r_j for all j} = ∏_j [0, r_j]` has exactly `∏_j (r_j + 1)` elements. In order-theoretic terms: the lower interval `↓r` of the product order on `ℕ^σ` has cardinality `∏_j #[0, r_j]`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]`, `[DecidableEq σ]` — finite variable set (to form `box r`).
- `r : σ → ℕ` — bounds.

Hypotheses (Lean side):
- none.

Conclusion (math): `#B(r) = (r_1 + 1) ⋯ (r_m + 1)`.

Conclusion (Lean): `(Roth.box r).card = ∏ j, (r j + 1)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: cardinality API lemma of a project helper def; elementary counting.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: n/a (theorem)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | number of lattice points in box 0 ≤ j_i ≤ r_i equals (r_1+1)(r_2+1)...(r_m+1) | yes | integer points of `∏[0, x_i+y_i]` number `∏(x_i+y_i+1)` | arXiv 2312.03168 (lattice aggregations of boxes); count is the multiplication principle |
| 2 | WebSearch (general form) | cardinality of interval [0,r] in product of chains N^n number of divisors formula product (a_i+1) | yes | `d(n) = ∏(ν_i+1)`: divisors of `n` correspond to the interval `[0, ν]` in a product of chains | arXiv 1405.4784; Encyclopedia of Math "Number of divisors" |
| 3 | WebSearch (named-after / aliases) | Roth's theorem auxiliary polynomial number of monomials degree at most r_j in each variable (r_1+1)...(r_m+1) Siegel lemma | yes | monomials with `deg_{X_h} ≤ r_h`, count `∏(r_h+1)` as number of unknowns in Siegel's lemma | arXiv 2502.00731 (Evertse, subspace theorem notes); arXiv 1806.10737 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `r_1 + 1` | yes | l.441, 724, 736: `(r_1+1)⋯(r_p+1)` as the number of coefficients; parent report also cites l.1058-1092, 1420 | project paper §3, §6 |
| 6 | nLab | interval / product of posets (from #2) | partial | cardinality of a product of finite posets is the product of cardinalities | no box-specific entry |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | elementary finite combinatorics, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #2: divisor-count formula) | partial | `τ(n) = ∏(a_i+1)` as the count of exponent vectors below `a` | folklore |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2502.00731 (2025), 2312.03168 (2023) | same product formula |

### Literature summary (Phase 3)

Concept identified as: cardinality of the lower interval `[0, r]` in `ℕ^σ` (product of chains), i.e. the multiplication principle `#∏_j [0, r_j] = ∏_j (r_j + 1)`; in Roth-type proofs it is the number of coefficients of a polynomial of multidegree ≤ r.
Sources agree on the standard form: yes.
Most general standard form: for a finite product of locally finite orders with bottom, `#Iic b = ∏_i #Iic (b_i)`; for finitely supported functions the product runs over the support (all other factors are 1).
Generality dimensions where the literature varies:
  - codomain: `ℕ` (most sources) vs any locally finite order with bottom.
  - ambient type: functions on a finite set vs finitely supported functions.
Disagreement with the literature: none.

### Generality analysis — `Roth.card_box`

Literature-standard form (from Phase 3): `#(Iic b) = ∏ i, #(Iic (b i))`, with `#(Iic n) = n + 1` in `ℕ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | required | needed for a `univ` product; mathlib's `Finsupp.card_Iic` avoids it by taking the product over `f.support` | partial | the RHS `∏ j, (r j + 1)` over `univ` is meaningless without `Fintype`; the support-product form is already `Finsupp.card_Iic` |
| 2 | `[DecidableEq σ]` | required | required by `Pi.card_Iic` / `Finsupp.card_Iic` too | no | interval instances need it |
| 3 | codomain `ℕ` | ℕ | any locally finite order with bottom (`Pi.card_Iic`), any `IsBotZeroClass` locally finite codomain (`Finsupp.card_Iic`) | yes | realised by the mathlib lemmas; the specific RHS `r j + 1` is `Nat.card_Iic` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — the general forms (`Pi.card_Iic`, `Finsupp.card_Iic`) are already in mathlib, so false-positive class 4. The one form not verbatim in mathlib is the `univ`-product version of `Finsupp.card_Iic` for `Fintype ι`; the evidence file proves it in 3 lines for any `IsBotZeroClass` locally finite codomain (optional, very small helper; not enough on its own to justify a PR from this project).
Number of weakening opportunities found: 1 (row 3), realised by existing mathlib lemmas; verified in `card_box_reaim.lean`.
Proposed restatement: none to add; locally `#(Iic (Finsupp.equivFunOnFinite.symm r)) = ∏ j, (r j + 1)` via `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset`.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite combinatorics |
| 3 | construction vs universal property? | yes | cardinality of the interval `Iic` rather than of a `piFinset` image | `Pi.card_Iic`, `Finsupp.card_Iic` |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `#(Iic b) = ∏ i, #(Iic (b i))` for locally finite codomains | already in mathlib (`Pi.card_Iic`) |
| 8 | concrete-via-abstract? | yes | proof only uses that `box r` is the down-set of `r` and `#[0,n] = n+1` | as #3 |
| 9 | false-generalisation guard | no false generalisation | evidence proves the same count for `box r`, for `Iic (equivFunOnFinite.symm r)` and for `Iic r` in `σ → ℕ` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: composition of `Finsupp.card_Iic` (or `Pi.card_Iic`) with `Nat.card_Iic` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: interval cardinality API once `box` is `Iic`.
  - Real mathematical improvement: none beyond the parent refactor.

### Proof strategy — `Roth.card_box`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after parent refactor: `Finsupp.card_Iic` + `Nat.card_Iic` + `Finset.prod_subset` | CHEAP |
| 5 | missing mathlib helpers | partial | `Finsupp.card_Iic` in `univ`-product form for `Fintype ι` would make the re-aimed proof 2 calls; proved in evidence | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the current definition; a one-line `simp` over `card_map`, `card_piFinset`, `card_range`)
  - If the parent is refactored: proof becomes `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset` (4 lines, CHEAP).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.card_box`

[A] Lean-Finder       "number of multi-indices d with d j ≤ r j for all j equals product of (r j + 1)"   hits: `Behrend.card_box` (`#box n d = d ^ n`, unrelated bounds `< d`), `Pi.card_Iic`, `DFinsupp.card_Iic`, `Pi.card_Iio`
[B] Loogle            `Finset.card (Finset.Iic _) = ∏ _, _`   hit: `Pi.card_Iic` (Mathlib.Data.Pi.Interval)
[C] LeanSearch        "cardinality of Finset.Iic of finitely supported function equals product over all indices of card Iic"   hits: `Finsupp.card_Iic` (product over support), `DFinsupp.card_Iic`, `Pi.card_Iic`, `Finsupp.card_Icc`
[D] Grep mathlib src  `card_Iic`, `card_Icc`, `card_piFinset` in Mathlib/Data/Finsupp/Interval.lean, Mathlib/Data/Pi/Interval.lean, Mathlib/Order/Interval/Finset/Nat.lean, Mathlib/Data/Fintype/BigOperators.lean; `namespace Roth`   hits: `Finsupp.card_Iic` (Interval.lean:125, support product), `Pi.card_Iic` (Pi/Interval.lean:62), `Nat.card_Iic` (Nat.lean:93), `Fintype.card_piFinset` (BigOperators.lean:124); no `Roth` namespace; no `univ`-product finsupp form
[E] Name pattern      `Finsupp.card_Iic`, `Pi.card_Iic`, `Nat.card_Iic`, `Fintype.card_piFinset` (all used in compiled evidence)   hits

Searched for both the user's form (`piFinset` box) and the re-aimed form (`#(Finset.Iic _)`).

Concluded: not found verbatim (mathlib's finsupp version takes the product over the support); composable in ≤3 mathlib calls for every form.

### Normal-form check — `Roth.card_box`

Equivalent formalisms: `#(box r)`; `#(Iic (equivFunOnFinite.symm r))`; `#(Iic r)` in `σ → ℕ`; `#(piFinset fun j ↦ range (r j + 1))`.
Does mathlib already have a canonical form for this idea? yes: `#(Iic b) = ∏ i, #(Iic (b i))` (`Pi.card_Iic`) with `Nat.card_Iic`.
Is our statement stated against the canonical form? yes for a local def: `card_` lemma with explicit closed product on the RHS.
RHS convention respected? yes

### Syntactic generality — `Roth.card_box`

Alternative restatements attempted:
- `#(Iic (equivFunOnFinite.symm r)) = ∏ j, (r j + 1)` (compiles)
- `#(Iic r) = ∏ j, (r j + 1)` for `r : σ → ℕ` (compiles, 2 calls)
- `#(Iic f) = ∏ i, #(Iic (f i))` for `f : ι →₀ α`, `Fintype ι` (compiles; candidate helper)
Chosen restatement: current.
Justification: call sites (Main.lean:405, Lattice.lean:163) consume the explicit `∏ j, (r j + 1)`.

### Superfluous-argument audit — `Roth.card_box`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | `box` and the `univ` product |
| 2 | `[DecidableEq σ]` | yes | `box` |
| 3 | `r` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; nothing ships to mathlib)

### Call sites — `Roth.card_box`

Internal use count: 2 outside the declaring file, plus 1 in Roth/Box.lean:68
External-to-file callers: 2 distinct files (plus indirect via `card_le_card_box` in Roth/MainLemma.lean:506 and Roth/CoeffNorm.lean:264)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Box.lean:68 | `(Finset.card_le_card fun d hd ↦ mem_box.2 (hs d hd)).trans_eq (card_box r)` |
| Roth/Main.lean:405 | `rw [Finset.sum_const, card_box, nsmul_eq_mul]` |
| Roth/Lattice.lean:163 | `_ = ∏ j, ((r j : ℝ) + 1) := by simp [card_box]` |

Inline-derivation grep:
  - Roth/MainLemma.lean:311 `ncard_boxFamily` counts a different (integer-coefficient) family; no inline re-derivation of `∏ (r j + 1)` found.

### Composition check (Phase 6)

Can `Roth.card_box` be derived from mathlib in ≤3 chained calls?

Attempt 1 (current definition): `rw [Roth.box, card_map, Fintype.card_piFinset]; simp only [card_range]`
  - Mathlib decls used: `Finset.card_map`, `Fintype.card_piFinset`, `Finset.card_range`
  - Result: succeeds (evidence example 1)

Attempt 2 (re-aimed, finsupp interval): `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset`
  - Result: succeeds (evidence examples 2 and 5)

Attempt 3 (re-aimed, pi interval): `simp only [Pi.card_Iic, Nat.card_Iic]`
  - Result: succeeds (evidence example 3)

Conclusion: COMPOSABLE

## Verdict: `Roth.card_box`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the multiplication-principle count `∏(r_j + 1)` of the interval `[0, r]` in `ℕ^σ` (paper l.441, 724, 736; divisor-count formula; Siegel-lemma unknowns in Roth's proof).
- Generality analysis (Phase 4): narrower than standard; general forms `Pi.card_Iic`, `Finsupp.card_Iic` exist in mathlib.
- Mathlib search (Phase 5): not verbatim (finsupp form uses a support product), but all ingredients present.
- Composition check (Phase 6): COMPOSABLE in ≤3 calls for the current def and both re-aimed forms.

**Rationale:**

Re-aimed at the parent's mathlib form, `#(Iic (Finsupp.equivFunOnFinite.symm r)) = ∏ j, (r j + 1)` follows from `Finsupp.card_Iic`, `Nat.card_Iic` and `Finset.prod_subset`; in the `σ → ℕ` interval it is literally `Pi.card_Iic` plus `Nat.card_Iic`; and for the current `piFinset` definition it is `card_map`, `Fintype.card_piFinset`, `card_range`. All three compile in the evidence file. The only form absent from mathlib verbatim is the `univ`-product version of `Finsupp.card_Iic` for a finite index type, a 3-line consequence of `Finsupp.card_Iic` that is too thin to be a contribution from this project.

WHY not: composable from existing mathlib in ≤3 calls; the lemma is the API lemma of a project-local def. Belongs-elsewhere check: keep it in Roth/Box.lean next to `box` and `mem_box`.

Existing mathlib decls:       `Pi.card_Iic`, `Finsupp.card_Iic`, `Nat.card_Iic`, `Fintype.card_piFinset`
Located at:                   `Mathlib/Data/Pi/Interval.lean:62`, `Mathlib/Data/Finsupp/Interval.lean:125`, `Mathlib/Order/Interval/Finset/Nat.lean:93`, `Mathlib/Data/Fintype/BigOperators.lean:124`
Our form follows in ≤3 calls:
```lean
example (r : σ → ℕ) : #(Iic r) = ∏ j, (r j + 1) := by
  simp only [Pi.card_Iic, Nat.card_Iic]
```
Call sites in our project (from Phase 6.0):  3 (Roth/Box.lean:68, Roth/Main.lean:405, Roth/Lattice.lean:163)
Refactor plan: none needed now. If the parent refactor (`box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r)`) is done, reprove `card_box` by `rw [Finsupp.card_Iic]; simp only [Nat.card_Iic]; rw [prod_subset (subset_univ _) fun j _ hj ↦ by simp_all]; simp`, keeping the name so the 3 call sites are unchanged.
Next action: do not upstream; keep `Roth.card_box` locally.

---

## Next step

No mathlib action. Keep `Roth.card_box` as the local API lemma; when `Roth.box` is redefined via `Finset.Iic`, reprove it from `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.card_box/card_box_reaim.lean` (imports `Roth.MainLemma` for `Finsupp.orderBot` and `Mathlib.Data.Pi.Interval` for `Pi.card_Iic`; `lean_diagnostic_messages`: no diagnostics): (1) `card_box` via `card_map`/`card_piFinset`/`card_range`; (2) `#(Iic (equivFunOnFinite.symm r)) = ∏ (r j + 1)` via `Finsupp.card_Iic`/`Nat.card_Iic`/`prod_subset`; (3) `#(Iic r) = ∏ (r j + 1)` in `σ → ℕ` via `Pi.card_Iic`/`Nat.card_Iic`; (4) candidate helper `#(Iic f) = ∏ i, #(Iic (f i))` for `f : ι →₀ α`, `Fintype ι`, any `IsBotZeroClass` locally finite codomain; (5) `card_box` from the parent's `box = Iic` bridge.
- First diagnostic run of the same file (overwritten) failed: unknown simp-lemma name `Finsupp.equivFunOnFinite_symm_apply_toFun`; `Pi.card_Iic` missing without `import Mathlib.Data.Pi.Interval`; `CanonicallyOrderedAdd` hypotheses insufficient for the finsupp `LocallyFiniteOrderBot` instance (mathlib v4.34 uses `IsBotZeroClass`). All fixed.
- Mathlib greps: `card_Iic`/`card_Icc`/`card_piFinset` in the files listed in [D]; no `namespace Roth`.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex.
- Project grep `grep -rn card_box Roth/` for the call-sites table.
