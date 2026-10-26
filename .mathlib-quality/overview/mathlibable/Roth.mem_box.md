---
decl: Roth.mem_box
file: Roth/Box.lean
line: 51
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: CHEAP
junk: KEEP
rationale: Re-aimed at the parent's mathlib form Finset.Iic (Finsupp.equivFunOnFinite.symm r), the statement is exactly Finset.mem_Iic.trans Finsupp.le_def (verified in evidence), so mathlib already has it.
action: Keep as a local simp-style API lemma for Roth.box (9 call sites in Taylor, CoeffNorm, Main, MainLemma, Lattice, Box); if box is redefined via Finset.Iic, reprove it as Finset.mem_Iic.trans Finsupp.le_def; do not upstream.
---

# Roth.mem_box

## Inventory entry

### `theorem Roth.mem_box`
- **Type**: `{σ : Type*} [Fintype σ] [DecidableEq σ] {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ Roth.box r ↔ ∀ j, d j ≤ r j`
- **What**: A multi-index `d` lies in the box `box r` iff it is bounded coordinatewise by `r`.
- **How**: `simp [box, Nat.lt_succ_iff]` — unfolds `box` to the `Finset.map` of `Fintype.piFinset (fun j ↦ range (r j + 1))`; simp uses `Finset.mem_map`, `Fintype.mem_piFinset`, `Finset.mem_range` and `Nat.lt_succ_iff`.
- **Hypotheses**: none beyond `[Fintype σ] [DecidableEq σ]` (section variables required by `box`).
- **Uses from project**: `Roth.box`
- **Used by**: Roth/Box.lean:68 (`card_le_card_box`); Roth/Taylor.lean:206; Roth/CoeffNorm.lean:236; Roth/Main.lean:404; Roth/MainLemma.lean:616; Roth/Lattice.lean:109, 117, 124, 138.
- **Visibility**: public
- **Lines**: 50–52, proof length 1 line
- **Notes**: Not a `:= rfl`/`Iff.rfl` glue lemma (needs simp through `map`/`piFinset`/`range`), and the parent `Roth.box` is `NO-mathlib-has-it` because of the more general mathlib def `Finset.Iic`, so per the re-aim rule this was assessed against `Finset.Iic` rather than inherited.

## Junk check (Step 8)
- Used anywhere? Yes, 9 uses in 6 files.
- Wrapper of 1–2 mathlib calls? Morally yes: for the mathlib form of the box it is `Finset.mem_Iic.trans Finsupp.le_def`; for the current `piFinset` definition it is a one-line `simp`.
- Does mathlib have it? Yes in re-aimed form: `Finset.mem_Iic` (Mathlib/Order/Interval/Finset/Defs.lean) composed with `Finsupp.le_def` (Mathlib/Order/Preorder/Finsupp.lean:32, `.rfl`).
- Too specific (inline)? No: as long as `Roth.box` exists as a named def, the characteristic membership lemma is the right API (used by `simp` at Lattice.lean and by `.2` at several sites).
- Well-chosen? Yes, standard `mem_` lemma shape for a project-local def.
- Conclusion: `KEEP` — action: keep as the API lemma of `Roth.box`; if `box` is redefined as `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (parent's recommendation), change the proof to `Finset.mem_Iic.trans Finsupp.le_def`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.mem_box` not in mathlib (no `namespace Roth`; the mathlib `Finset.mem_box` in Mathlib/Order/Interval/Finset/Box.lean:102 is unrelated: the `ℤ × ℤ` sup-norm shell). Not a pure glue lemma, and the parent `Roth.box` is NO-mathlib-has-it via the more general `Finset.Iic`, so the **re-aim rule** applies: full run re-aimed at `Finset.Iic`. The re-aim was a hit (mathlib has the analogous lemma `Finset.mem_Iic` + `Finsupp.le_def`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` has no diagnostics)
- decl `Roth.mem_box`:       resolved at Roth/Box.lean:51
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.mem_box` is a theorem stating the following: for a finite index set `σ`, bounds `r ∈ ℕ^σ` and a multi-index `d ∈ ℕ^σ`, `d` belongs to the box `B(r) = ∏_j [0, r_j]` if and only if `d_j ≤ r_j` for every `j`. In order-theoretic terms: `d ∈ ↓r ⇔ d ≤ r` in the product order, and the product order is coordinatewise.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]`, `[DecidableEq σ]` — finite variable set (needed to form `box r`).
- `r : σ → ℕ` — bounds; `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- none.

Conclusion (math): `d ∈ B(r) ⇔ ∀ j, d_j ≤ r_j`.

Conclusion (Lean): `d ∈ Roth.box r ↔ ∀ j, d j ≤ r j`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: characteristic membership lemma of a project helper def.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: n/a (theorem)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index d ≤ r componentwise "d_j ≤ r_j for all j" lower interval membership | yes | `h ≤ k` componentwise; block set `{h : h ≤ k}` is the lower interval `[0,k]` | arXiv 1908.01178, 2406.10145 (lower sets of multi-indices) |
| 2 | WebSearch (general form) | product order componentwise partial order on N^n interval [0,r] membership x ≤ y iff x_i ≤ y_i | yes | product (coordinatewise) order: `a ≤ b ⇔ ∀ i, a_i ≤ b_i`; `x ∈ [0,r] ⇔ 0 ≤ x ≤ r` | Wikipedia "Product order" |
| 3 | WebSearch (named-after / aliases) | mathlib Finsupp.le_def Finset.mem_Iic finitely supported functions pointwise order | yes | `Finsupp.le_def : f ≤ g ↔ ∀ i, f i ≤ g i` (pointwise order on finsupps) | mathlib docs Mathlib/Order/Preorder/Finsupp, Data/Finsupp/Order |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `0 \leq j_1 \leq r_1` | yes | l.1053, 1074: "`0 ≤ j_1 ≤ r_1, …, 0 ≤ j_m ≤ r_m`" (the box as a coordinatewise system of inequalities) | project paper §6 Lemma 8 |
| 6 | nLab | product order / down-set (from #2) | partial | principal down-set `↓r`; product order of posets | abstract notion only; membership is the definition of `↓r` |
| 7 | nCatLab | — | n/a | — | not a categorical concept; order-theoretic notion covered by #2/#6 |
| 8 | Stacks Project | — | n/a | — | elementary order theory of exponent vectors, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #2) | partial | coordinatewise order on `ℕ^n` (Dickson's lemma context) | folklore; no dedicated thread needed |
| 10 | recent arXiv (last 5 years) | (results of #1) | yes | arXiv 2406.10145 (2024): lower sets / blocks `{h : h ≤ k}` | same coordinatewise form |

### Literature summary (Phase 3)

Concept identified as: membership in the principal down-set `↓r = [0, r]` of the product (coordinatewise) order on `ℕ^σ`.
Sources agree on the standard form: yes.
Most general standard form: in any poset, `x ∈ ↓a ⇔ x ≤ a`; in a product / finsupp order, `f ≤ g ⇔ ∀ i, f i ≤ g i`.
Generality dimensions where the literature varies:
  - ambient poset: `ℕ^n` up to any locally finite order with bottom (`Finset.Iic`).
  - index set: finite, or arbitrary with finitely supported vectors.
Disagreement with the literature: none.

### Generality analysis — `Roth.mem_box`

Literature-standard form (from Phase 3): `x ∈ Iic a ↔ x ≤ a`, plus `f ≤ g ↔ ∀ i, f i ≤ g i` for finsupps.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | required | not needed for `Iic (r : σ →₀ ℕ)` | yes | evidence example 1 compiles with only `[DecidableEq τ]` and `r : τ →₀ ℕ` |
| 2 | `[DecidableEq σ]` | required | required by `Finsupp.instLocallyFiniteOrder` | no | needed for the finsupp interval instance (parent evidence) |
| 3 | codomain `ℕ` | ℕ | any `Preorder` with `LocallyFiniteOrderBot` (for `mem_Iic`); `Finsupp.le_def` for any `[Zero M] [LE M]` | yes | realised by the mathlib lemmas themselves |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is already in mathlib (`Finset.mem_Iic`, `Finsupp.le_def`): false-positive class 4, routed to NO-mathlib-has-it.
Number of weakening opportunities found: 2 (rows 1, 3), both realised by existing mathlib lemmas; verified in `mem_box_reaim.lean` (no diagnostics).
Proposed restatement: none to add; locally `d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r) ↔ ∀ j, d j ≤ r j := Finset.mem_Iic.trans Finsupp.le_def`.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite combinatorics |
| 3 | construction vs universal property? | yes | membership in the interval `Iic` instead of in a `piFinset` image | `Finset.mem_Iic` and the interval API |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `Finset.mem_Iic` for any `LocallyFiniteOrderBot` | already in mathlib |
| 8 | concrete-via-abstract? | yes | proof only uses that `box r` is the down-set of `r` | as #3 |
| 9 | false-generalisation guard | no false generalisation | evidence proves the same iff for `Iic (equivFunOnFinite.symm r)` and for `box r` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finset.mem_Iic.trans Finsupp.le_def` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: `Finset.mem_Iic` / `Finsupp.le_def` simp lemmas fire directly once `box` is `Iic`.
  - Real mathematical improvement: none beyond the parent refactor; this lemma becomes a one-term corollary.

### Proof strategy — `Roth.mem_box`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after parent refactor: `Finset.mem_Iic.trans Finsupp.le_def` | CHEAP |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the current definition; a one-line `simp`)
  - If the parent is refactored: proof becomes `Finset.mem_Iic.trans Finsupp.le_def` (CHEAP), strictly shorter in dependencies.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.mem_box`

[A] Lean-Finder       "d ∈ Finset.Iic r ↔ ∀ i, d i ≤ r i for finitely supported functions σ →₀ ℕ"   hits: `Finsupp.mem_rangeIcc_apply_iff`, `DFinsupp.instLocallyFiniteOrder`, `DFinsupp.le_iff'` (related)
[B] Loogle            `Finsupp.le_def`   hit: `Finsupp.le_def : f ≤ g ↔ ∀ i, f i ≤ g i` (Mathlib.Order.Preorder.Finsupp)
[C] LeanSearch        "membership in Finset.Iic of finsupp iff pointwise le"   hits: `Finsupp.le_def`, `Finset.mem_Iic`, `DFinsupp.le_iff`
[D] Grep mathlib src  `mem_box`, `le_def` in Mathlib/Order/Preorder/Finsupp.lean, `mem_Iic` in Mathlib/Order/Interval/Finset/Defs.lean   hits: `Finsupp.le_def` (l.32, `.rfl`); unrelated `Finset.mem_box` (Box.lean:102, ℤ×ℤ shells), `BoxIntegral.unitPartition.mem_box_iff`
[E] Name pattern      `Finset.mem_Iic`, `Finsupp.le_def` (used in compiled evidence)   hits

Searched for both the user's form (`piFinset` box membership) and the re-aimed form (`Finset.Iic` membership).

Concluded: found in mathlib as `Finset.mem_Iic` composed with `Finsupp.le_def`; more general form (we are a specialisation).

### Normal-form check — `Roth.mem_box`

Equivalent formalisms: `d ∈ box r`; `d ∈ Iic r'`; `d ≤ r'`; `∀ j, d j ≤ r j`.
Does mathlib already have a canonical form for this idea? yes: `d ≤ r'` (via `Finset.mem_Iic`), unfolded by `Finsupp.le_def`.
Is our statement stated against the canonical form? yes for a local def: `mem_box` has the usual `x ∈ S ↔ predicate` shape with the elementary predicate on the RHS.
RHS convention respected? yes

### Syntactic generality — `Roth.mem_box`

Alternative restatements attempted:
- `d ∈ box r ↔ d ≤ Finsupp.equivFunOnFinite.symm r` (needs extra unfolding at call sites)
- `d ∈ box r ↔ ∀ j, d j ≤ r j` (current)
Chosen restatement: current.
Justification: every call site supplies or consumes the coordinatewise bound directly (`mem_box.2 fun j ↦ ...`).

### Superfluous-argument audit — `Roth.mem_box`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed to form `box r` from `r : σ → ℕ` |
| 2 | `[DecidableEq σ]` | yes | needed by `box` |
| 3 | `r`, `d` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; nothing ships to mathlib)

### Call sites — `Roth.mem_box`

Internal use count: 8 (outside the declaring file), plus 1 in Roth/Box.lean:68
External-to-file callers: 5 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Box.lean:68 | `(Finset.card_le_card fun d hd ↦ mem_box.2 (hs d hd)).trans_eq (card_box r)` |
| Roth/Taylor.lean:206 | `simpa [Roth.mem_box] using he` |
| Roth/CoeffNorm.lean:236 | `(fun k hk ↦ mem_box.2 fun j ↦ (monomial_le_degreeOf j hk).trans (hP j))` |
| Roth/Main.lean:404 | `Finset.sum_lt_sum_of_nonempty ⟨0, mem_box.2 fun j ↦ Nat.zero_le _⟩ hterm` |
| Roth/MainLemma.lean:616 | `Finset.mem_filter.2 ⟨mem_box.2 hd, hw.le⟩` |
| Roth/Lattice.lean:109 | `simp only [Finset.mem_filter, mem_box, Function.comp_apply] at hd ⊢` |
| Roth/Lattice.lean:117 | `obtain ⟨⟨hdr, hdp⟩, hdi⟩ := (by simpa [mem_box] using hd)` |
| Roth/Lattice.lean:124 | `simp [mem_box, hext, hdp, hdr]` |
| Roth/Lattice.lean:138 | `simp only [Finset.coe_filter, Set.mem_ofPred_eq, mem_box] at hd` |

Inline-derivation grep:
  - Roth/MainLemma.lean:282/295 (private `boxFamily_eq_image_finsupp_aux`) works with `Finset.Iic (Finsupp.ofSupportFinite r _)` and so uses `Finset.mem_Iic` directly rather than `mem_box` (noted in the parent report).

### Composition check (Phase 6)

Can `Roth.mem_box` be derived from mathlib in ≤3 chained calls?

Attempt 1 (re-aimed, `box r := Iic (equivFunOnFinite.symm r)`): `Finset.mem_Iic.trans Finsupp.le_def`
  - Mathlib decls used: `Finset.mem_Iic`, `Finsupp.le_def`
  - Result: succeeds (evidence examples 1–2)
  - Notes: one `.trans` chain.

Attempt 2 (current definition): rewrite `box r` to `Iic` via the parent's bridge, then Attempt 1 (evidence example 3) — or the existing one-line `simp [box, Nat.lt_succ_iff]`.
  - Result: succeeds.

Conclusion: COMPOSABLE

## Verdict: `Roth.mem_box`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): membership in the down-set `[0, r]` of the coordinatewise order, standard (paper l.1053, 1074; product order).
- Generality analysis (Phase 4): narrower than standard, but the standard form is in mathlib (false-positive class 4).
- Mathlib search (Phase 5): found as `Finset.mem_Iic` + `Finsupp.le_def`.
- Composition check (Phase 6): COMPOSABLE, `Finset.mem_Iic.trans Finsupp.le_def`.

**Rationale:**

The parent `Roth.box` was judged NO-mathlib-has-it because `box r` is mathlib's `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`. Re-aimed at that interval, `mem_box` is the conjunction of two existing mathlib lemmas: `Finset.mem_Iic : x ∈ Iic a ↔ x ≤ a` (any `LocallyFiniteOrderBot`) and `Finsupp.le_def : f ≤ g ↔ ∀ i, f i ≤ g i` (any `[Zero M] [LE M]`). The evidence file compiles `Finset.mem_Iic.trans Finsupp.le_def` for both the `σ →₀ ℕ` bound (no `Fintype`) and the `equivFunOnFinite.symm r` bound. Nothing new would be contributed to mathlib.

WHY not: mathlib has the more general statement; the project lemma is only the API lemma of a project-local def. Belongs-elsewhere check: keep it project-local in Roth/Box.lean as the membership lemma of `Roth.box` (it is used by `simp` and `.2` at 9 sites, and keeping it insulates those sites from the definition of `box`).

Existing mathlib decl:        `Finset.mem_Iic` and `Finsupp.le_def`
Located at:                   `Mathlib/Order/Interval/Finset/Defs.lean` (`mem_Iic`), `Mathlib/Order/Preorder/Finsupp.lean:32` (`le_def`)
Our form follows in ≤1 line:
```lean
example {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r) ↔ ∀ j, d j ≤ r j :=
  Finset.mem_Iic.trans Finsupp.le_def
```
Call sites in our project (from Phase 6.0):  9 (Roth/Box.lean:68, Roth/Taylor.lean:206, Roth/CoeffNorm.lean:236, Roth/Main.lean:404, Roth/MainLemma.lean:616, Roth/Lattice.lean:109, 117, 124, 138)
Refactor plan: no call-site change needed. If the parent refactor (`box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r)`) is done, replace the proof of `mem_box` by `Finset.mem_Iic.trans Finsupp.le_def` and keep the name so all 9 call sites stay unchanged. If instead `box` is fully inlined, replace `mem_box.2 h` by `Finset.mem_Iic.2 (Finsupp.le_def.2 h)` and `simp [mem_box]` by `simp [Finsupp.le_def]` at the 9 sites.
Next action: do not upstream; keep `Roth.mem_box` locally (reprove as above if the parent is refactored).

---

## Next step

No mathlib action. Keep `Roth.mem_box` as the local API lemma; when `Roth.box` is redefined via `Finset.Iic`, reprove it as `Finset.mem_Iic.trans Finsupp.le_def`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.mem_box/mem_box_reaim.lean` (imports `Roth.MainLemma` for the `Finsupp.orderBot` instance; `lean_diagnostic_messages`: no diagnostics): (1) `d ∈ Iic r ↔ ∀ j, d j ≤ r j` for `r : τ →₀ ℕ` without `Fintype`, by `mem_Iic.trans Finsupp.le_def`; (2) the same for `Iic (Finsupp.equivFunOnFinite.symm r)`; (3) `mem_box` recovered from the parent's `box = Iic` bridge.
- Parent evidence `.mathlib-quality/overview/evidence/Roth.box/box_eq_Iic.lean` (box equals `Finset.Iic`).
- Mathlib greps: `Finsupp.le_def` at Mathlib/Order/Preorder/Finsupp.lean:32; `mem_box` only unrelated (`Finset.mem_box` for ℤ×ℤ, BoxIntegral `mem_box_iff`).
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex.
- Project grep `grep -rn mem_box Roth/` for the call-sites table.
