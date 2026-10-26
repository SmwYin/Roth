---
decl: Roth.box
file: Roth/Box.lean
line: 47
kind: def
visibility: public
verdict: NO-mathlib-has-it
cost: MODERATE
junk: REPLACE
rationale: box r is exactly mathlib's interval Finset.Iic (Finsupp.equivFunOnFinite.symm r) (equivalently Finset.Icc 0 _) in the locally finite order on σ →₀ ℕ, with membership by Finset.mem_Iic and cardinality by Finsupp.card_Iic plus Nat.card_Iic (all verified in evidence).
action: Redefine Roth.box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r) (or inline that at the call sites in Roth/Lattice.lean, Roth/MainLemma.lean, Roth/Main.lean, Roth/Taylor.lean, Roth/CoeffNorm.lean), reproving mem_box/card_box from Finset.mem_Iic and Finsupp.card_Iic and adding a piFinset bridge for Roth/CoeffNorm.lean:216; do not upstream.
---

# Roth.box

## Inventory entry

### `def Roth.box`
- **Type**: `{σ : Type*} → [Fintype σ] → [DecidableEq σ] → (r : σ → ℕ) → Finset (σ →₀ ℕ)`
- **What**: The finite set of multi-indices `d : σ →₀ ℕ` with `d j ≤ r j` for every `j` (the box `∏ j [0, r j]` of exponent vectors).
- **How**: Image of `Fintype.piFinset fun j ↦ Finset.range (r j + 1)` under the embedding `Finsupp.equivFunOnFinite.symm.toEmbedding` (`Finset.map`).
- **Hypotheses**: `[Fintype σ]` (finite variable set), `[DecidableEq σ]` (needed by `Fintype.piFinset`).
- **Uses from project**: `[]`
- **Used by**: Roth/Box.lean: `mem_box` (l.51), `card_box` (l.57), `card_le_card_box` (l.66-68, via `mem_box`/`card_box`), docstring of `weight_le_card` (l.100); Roth/Taylor.lean: l.199, 200, 206, 219 (Taylor expansion over the box); Roth/CoeffNorm.lean: l.215, 216 (unfolds `box` to use `Finset.prod_univ_sum`), 234, 236; Roth/Main.lean: l.392, 404, 405; Roth/MainLemma.lean: l.570, 608, 616; Roth/Lattice.lean: l.102, 104, 109, 117, 124, 132-133, 138, 144, 148, 151, 159, 162-163, 168, 170, 177, 203 (Lemma 8 lattice count).
- **Visibility**: public
- **Lines**: 45–48, proof length 1 line (definition body)
- **Notes**: Roth/MainLemma.lean:282 and :295 (private `boxFamily_eq_image_finsupp_aux`) already use `Finset.Iic (Finsupp.ofSupportFinite r _)` as an inline box, so the project itself contains the mathlib form.

## Junk check (Step 8)
- Used anywhere? Yes, heavily (about 30 occurrences across 6 files).
- Wrapper of 1–2 mathlib calls? Yes: `Finset.map` of `Fintype.piFinset`; and it is extensionally `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (evidence).
- Does mathlib have it? Yes: `Finset.Iic` in the `LocallyFiniteOrder (σ →₀ ℕ)` instance (`Finsupp.instLocallyFiniteOrder`, Mathlib/Data/Finsupp/Interval.lean:85) with `Finsupp.card_Iic` (l.125); also `Pi.card_Iic` for `σ → ℕ`.
- Too specific / inline? The named concept "box" is mathematically just the lower interval `Iic r`; the dedicated `piFinset` body is only convenient for `Finset.prod_univ_sum` at Roth/CoeffNorm.lean:216.
- Well-chosen definition? Duplicates mathlib's interval API with a different implementation, so `Finset.mem_Iic`, `Finset.Iic` monotonicity, `Finsupp.card_Iic` etc. do not apply to it directly; the project re-derives `mem_box` and `card_box`.
- Conclusion: `REPLACE` — action: set `box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (keeping the name as a thin local abbreviation if the `r : σ → ℕ` interface is convenient) or inline it; reprove `mem_box` via `Finset.mem_Iic`/`Finsupp.le_def` and `card_box` via `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset`; add a one-line bridge to the `piFinset` form for Roth/CoeffNorm.lean:216; this also unifies with the inline `Finset.Iic` in Roth/MainLemma.lean:282.

## Mathlibable assessment (Step 9)

Pre-filter: not private, no `_aux`, docstring not internal/auxiliary, Step 8 said REPLACE (not REMOVE), qualified name `Roth.box` not in mathlib (grep for `namespace Roth` in Mathlib: no hits). Full workflow follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` compiles)
- decl `Roth.box`:           resolved at Roth/Box.lean:47
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.box` is a definition of the following: for a finite index set `σ` and a vector of bounds `r ∈ ℕ^σ`, the finite set
`B(r) = { d ∈ ℕ^σ : 0 ≤ d_j ≤ r_j for all j } = ∏_j [0, r_j]`
of exponent vectors (multi-indices), viewed as finitely supported functions. It indexes the monomials of a polynomial of multidegree at most `r`, and has `∏_j (r_j + 1)` elements.

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]` — finite set of variables.
- `[DecidableEq σ]` — needed by `Fintype.piFinset`.
- `r : σ → ℕ` — coordinatewise upper bounds.

Hypotheses (Lean side):
- none.

Conclusion (math): the finite set `{d : d ≤ r}` (lower interval of `r` in the product order).

Conclusion (Lean): n/a — definition (`Finset (σ →₀ ℕ)`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: bookkeeping finset for a project helper; not a new structure or main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | weak     | Roth/CoeffNorm.lean:216 unfolds `box` (`simpa [..., box, Finset.prod_univ_sum]`) to reach the `piFinset` form; this is a convenience, not a barrier, and a bridge lemma would replace it |
| Avoid typeclass diamonds         | no       | no instances involved; the `Finset.Iic` form uses the canonical `Finsupp.instLocallyFiniteOrder` |
| Mark semantic intent / API name  | yes (project-local) | Lattice.lean Lemma 8 and MainLemma.lean statements are phrased with `box r`; the stable name is useful locally, but the mathlib name for the concept is `Finset.Iic` |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; no exemption justifies a mathlib addition since mathlib has the concept under `Finset.Iic`)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index set {alpha : alpha_j <= r_j} box lattice points count prod (r_j+1) | partial | integer points of a box `∏[0,r_j]`, count `∏(r_j+1)` | arXiv 2312.03168 (lattice aggregations of boxes); count is elementary |
| 2 | WebSearch (general form) | order ideal lower set of a multi-index product of chains divisor lattice interval [0, r] in N^n | yes | principal order ideal / interval `[0,r]` in `ℕ^n` under the componentwise order; product of chains `[r_1+1]×…×[r_n+1]` | arXiv 1608.08004 (order ideals in `N^n`), 2307.08520 (products of chains as divisor posets) |
| 3 | WebSearch (named-after / aliases) | Roth's theorem proof index of polynomial monomials i_j <= r_j number of exponents (r_1+1)...(r_m+1) | yes | monomials with `deg_{x_j} ≤ r_j`, count `∏(r_j+1)` in Roth-lemma proofs | arXiv 2502.00731 (subspace theorem notes); Wikipedia "Roth's theorem" |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `r_1 + 1`, `j_1 \le r_1` | yes | l.1420 `r = (r_1+1)⋯(r_m+1)`; l.1058-1092 Lemma 8 count over `0 ≤ j_i ≤ r_i`; l.441, 724 | project source paper §6 |
| 6 | nLab | interval / lower set in a poset (surfaced by #2) | partial | principal down-set `↓r` of a poset | no box-specific entry; the abstract notion is the down-set/interval |
| 7 | nCatLab | — | n/a | — | not a categorical concept; covered by the order-theoretic notion in #6 |
| 8 | Stacks Project | — | n/a | — | finite combinatorics of exponent vectors, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #2: order ideals in products of chains) | partial | interval `[0,r]` in `ℕ^n` = product of chains | no dedicated thread; the identification is folklore |
| 10 | recent arXiv (last 5 years) | (results of #1-#3) | yes | arXiv 2502.00731 (2025), 2312.03168 (2023), 2307.08520 (2023) | same componentwise-interval form |

### Literature summary (Phase 3)

Concept identified as: the lower interval (principal order ideal) `[0, r] = ↓r` of `r` in `ℕ^σ` with the componentwise order; equivalently the product of chains `∏_j {0,…,r_j}`; in Roth-type proofs, "the exponents of monomials of multidegree ≤ r".
Sources agree on the standard form: yes.
Most general standard form: for a locally finite order with bottom, the finite lower interval `Iic r = {d : d ≤ r}`; for `ℕ^σ` it is `∏_j [0, r_j]` with `#Iic r = ∏_j (r_j + 1)`.
Generality dimensions where the literature varies:
  - ambient poset: `ℕ^n` (most sources) up to any product of locally finite orders / finitely supported functions (mathlib).
  - index set: finite `{1..n}`; with finitely supported vectors, any index type.
Disagreement with the literature: none; the project's form is a particular implementation of `Iic r`.

### Generality analysis — `Roth.box`

Literature-standard form (from Phase 3): `Iic r` in the locally finite order on `σ →₀ ℕ` (or `σ → ℕ`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | finite variable set | any index set, `r` finitely supported | yes | `Finset.Iic (r : σ →₀ ℕ)` needs no `Fintype` (evidence, last example); but then `r` must be a finsupp |
| 2 | `[DecidableEq σ]` | required | required by mathlib's finsupp interval instance too | no | `Fintype.piFinset` and `Finsupp.instLocallyFiniteOrder` both need it (dropping it from `box` fails to synthesize `DecidableEq σ`, observed in the first evidence run) |
| 3 | `r : σ → ℕ` | function | `r : σ →₀ ℕ` / any `r` in a locally finite order | yes | mathlib's form is stated for any `[LocallyFiniteOrder α] [OrderBot α]` codomain |
| 4 | codomain `ℕ` | ℕ | any canonically ordered locally finite `α` | yes | `Finsupp.card_Iic` holds for `[AddCommMonoid α] [PartialOrder α] [IsBotZeroClass α] [OrderBot α] [LocallyFiniteOrder α]` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the standard form is already in mathlib (`Finset.Iic` on `σ →₀ α`, Mathlib/Data/Finsupp/Interval.lean), so this is false-positive class 4 ("general form already in mathlib"), routed to NO-mathlib-has-it.
Number of weakening opportunities found: 3 (rows 1, 3, 4), all realised by the existing mathlib `Finset.Iic`.
Proposed restatement: `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`; verified equal to `box r` by `ext d; simp [Roth.mem_box, Finsupp.le_def]` in the evidence file.
Cost of restatement: MODERATE — the equality is one line; replacing the def needs `mem_box`/`card_box` reproofs and a `piFinset` bridge for Roth/CoeffNorm.lean:216.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite combinatorial set |
| 3 | construction vs universal property? | yes | `box` constructs via `piFinset`+`map`; mathlib characterises the same set as the interval `Iic r` (`Finset.mem_Iic : d ∈ Iic r ↔ d ≤ r`) | the whole `Finset.Iic` API: `Iic_subset_Iic`, `card_Iic`, `Finset.sum_Iic_*`, interval `induction` |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `Finset.Iic (r : σ →₀ α)` for locally finite canonically ordered `α` | `Finsupp.card_Iic`, `DFinsupp.card_Iic`, `Pi.card_Iic` |
| 8 | concrete-via-abstract? | yes | `mem_box` and `card_box` only use that `box r` is the down-set of `r` | as #3 |
| 9 | false-generalisation guard | no false generalisation | `box r = Iic (equivFunOnFinite.symm r)` proved in evidence: same set | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (already in mathlib; nothing to add).
  - Cost: MODERATE (local refactor only)
  - Mathlib downstream this enables: `Finset.mem_Iic`, `Finsupp.card_Iic`, `Finset.Iic_subset_Iic`, and agreement with the project's own inline `Finset.Iic (Finsupp.ofSupportFinite r _)` in Roth/MainLemma.lean:282.
  - Real mathematical improvement: removes a second implementation of the interval `Iic r` and the two re-derived API lemmas.

### Proof strategy — `Roth.box`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | define as `Finset.Iic` (the characterised interval) rather than a `piFinset` image | MODERATE |
| 5 | missing mathlib helpers | partial | a lemma `Finsupp.card_Iic_eq_prod_univ [Fintype ι] : #(Iic f) = ∏ i, #(Iic (f i))` (our evidence needs `Finset.prod_subset` to pass from `f.support` to `univ`); small, optional | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: define/inline as `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`; derive `mem_box` from `Finset.mem_Iic` and `card_box` from `Finsupp.card_Iic` + `Nat.card_Iic` + `Finset.prod_subset`.
  - Cost: MODERATE
  - Missing mathlib API (if any): optional `univ`-product form of `Finsupp.card_Iic` for `Fintype ι`.
  - Would refactoring make the proof strictly shorter / cleaner? yes (no bespoke construction; standard API applies).

### Diamond / defeq risk — `Roth.box`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; the `Iic` replacement uses the canonical `Finsupp.instLocallyFiniteOrder` and `LocallyFiniteOrder.toLocallyFiniteOrderBot` with `Finsupp.orderBot` |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def` |
| 3 | Non-canonical unfolding | low | unfolding gives a `Finset.map` of `piFinset`, not the `Iic` form, so mathlib interval lemmas do not fire by `simp`; this is the cost of the duplicate implementation |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`, no constraint forced |
| 6 | Coercion ambiguity | none | no coercions; the name `box` collides with unrelated mathlib `Finset.box` (Mathlib/Order/Interval/Finset/Box.lean:39), `Behrend.box` and `BoxIntegral.unitPartition.box`, harmless inside `Roth` but a reason not to upstream under this name |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.box`

[A] Lean-Finder       "the set of multi-indices d with d j ≤ r j for all j as a Finset of σ →₀ ℕ"   hits: `DFinsupp.rangeIcc`, `Behrend.box` (Fin n → ℕ, bounds `< d`), `Finset.finsuppAntidiag` — related, the interval form found via [B]
[B] Loogle            `Finset.card (Finset.Iic _) = ∏ _ ∈ _, _`   hits: `Finsupp.card_Iic`, `DFinsupp.card_Iic`, `Multiset.card_Iic`, `Pi.card_Iic`
[C] LeanSearch        "finset of finitely supported functions bounded pointwise by r, cardinality product"   hits: `DFinsupp.card_Iic`, `Finset.card_finsupp`, `Finsupp.card_pi`
[D] Grep mathlib src  `def box`, `namespace Roth`, `instLocallyFiniteOrder`, `card_Iic` in Mathlib/Data/Finsupp/Interval.lean, `toLocallyFiniteOrderTop` (to_dual Bot) in Mathlib/Order/Interval/Finset/Defs.lean:403   hits: `Finsupp.instLocallyFiniteOrder` (l.85), `Finsupp.card_Iic` (l.125); unrelated `Finset.box`, `Behrend.box`, `BoxIntegral...box`; no `Roth` namespace
[E] Name pattern      `Finsupp.card_Iic`, `Finset.mem_Iic`, `Nat.card_Iic` (verified by use in the compiled evidence file)   hits

Searched for both the user's form (`piFinset` image of ranges) and the literature-standard form (interval `Iic r`).

Concluded: found in mathlib as `Finset.Iic` (on `σ →₀ ℕ` via `Finsupp.instLocallyFiniteOrder`); identical set (`box r = Finset.Iic (Finsupp.equivFunOnFinite.symm r)`), with mathlib's form more general (any index type with finsupp bound, any locally finite canonically ordered codomain).

### Normal-form check — `Roth.box`

Equivalent formalisms: `Finset.Iic r` (finsupp); `Finset.Icc 0 r`; `piFinset (fun j ↦ range (r j + 1))` mapped by `equivFunOnFinite.symm`; `Finset.Iic (r : σ → ℕ)` in `σ → ℕ` (`Pi`) transported.
Does mathlib already have a canonical form for this idea? yes: `Finset.Iic` with `Finset.mem_Iic`.
Is our statement stated against the canonical form? no: it is a parallel construction; refactor to `Iic` with the `piFinset` description as a bridge lemma (canonical form on the RHS of rewriting lemmas).
RHS convention respected? n/a for the def; the proposed bridge `Finset.Iic (equivFunOnFinite.symm r) = (piFinset …).map …` would be used only at Roth/CoeffNorm.lean:216.

### Syntactic generality — `Roth.box`

Alternative restatements attempted:
- `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (compiles, equal to `box r`)
- `Finset.Icc 0 (Finsupp.equivFunOnFinite.symm r)` (compiles, equal to `box r`; needs no `OrderBot` import)
- `Finset.Iic (r : σ →₀ ℕ)` with no `Fintype σ` (membership compiles)
Chosen restatement: `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`.
Justification: call sites have `r : σ → ℕ` and `σ` finite; `Iic` gives `mem_Iic`/`card_Iic` directly and matches Roth/MainLemma.lean:282.

### Superfluous-argument audit — `Roth.box`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes for `r : σ → ℕ` | needed to turn `r` into a finsupp; not needed for the finsupp-bound `Iic` form |
| 2 | `[DecidableEq σ]` | yes | `piFinset` / finsupp interval instance |
| 3 | `r : σ → ℕ` | yes | the bound |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (target `Finset.Iic`)
Syntactic generality: RESTATE (`Finset.Iic (Finsupp.equivFunOnFinite.symm r)`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (locally; nothing ships to mathlib)

### Call sites — `Roth.box`

Internal use count: 30+ occurrences outside the declaring file (counting `box`, `mem_box`, `card_box`)
External-to-file callers: 5 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:199 | `P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j` |
| Roth/Taylor.lean:200 | `taylor α P = ∑ d ∈ Roth.box r, monomial d (...)` |
| Roth/Taylor.lean:206 | `simpa [Roth.mem_box] using he` |
| Roth/Taylor.lean:219 | `eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ...` |
| Roth/CoeffNorm.lean:215 | `∑ k ∈ box r, B * ∏ j, abs (x j) ^ k j ≤ B * ∏ j, (1 + abs (x j)) ^ r j` |
| Roth/CoeffNorm.lean:216 | `simpa [← Finset.mul_sum, box, Finset.prod_univ_sum] using` (unfolds to `piFinset`) |
| Roth/CoeffNorm.lean:234 | `_ ≤ ∑ k ∈ box r, B * ∏ j, abs (x j) ^ k j :=` |
| Roth/CoeffNorm.lean:236 | `(fun k hk ↦ mem_box.2 fun j ↦ ...)` |
| Roth/Main.lean:392 | `have hterm : ∀ d ∈ box r, ...` |
| Roth/Main.lean:404 | `Finset.sum_lt_sum_of_nonempty ⟨0, mem_box.2 fun j ↦ Nat.zero_le _⟩ hterm` |
| Roth/Main.lean:405 | `rw [Finset.sum_const, card_box, nsmul_eq_mul]` |
| Roth/MainLemma.lean:570 | `a * (((box r).filter fun d ↦ weight r d ≤ ...).card : ℝ)` |
| Roth/MainLemma.lean:608 | `let J := (box r).filter fun d ↦` |
| Roth/MainLemma.lean:616 | `Finset.mem_filter.2 ⟨mem_box.2 hd, hw.le⟩` |
| Roth/Lattice.lean:102-124 | fibre lemma: `(box (r ∘ Fin.castSucc)).filter ...`, `simp [mem_box, ...]` |
| Roth/Lattice.lean:132-151 | `((box r).filter p).card = ∑ i ∈ range (r (Fin.last m) + 1), ...` |
| Roth/Lattice.lean:159-177 | `Finset.card_filter_le (box r) _`, `simp [card_box]`, induction steps |
| Roth/Lattice.lean:203 | Lemma 8 statement `(((box r).filter fun d ↦ weight r d ≤ ...).card : ℝ) ≤ ...` |

Inline-derivation grep:
  - Roth/MainLemma.lean:282 and :295 — `Finset.Iic (Finsupp.ofSupportFinite r (Set.toFinite _))`, the same box written with mathlib's `Finset.Iic` (private `boxFamily_eq_image_finsupp_aux`).

### Composition check (Phase 6)

Can `Roth.box` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`
  - Mathlib decls used: `Finset.Iic`, `Finsupp.equivFunOnFinite`, `Finsupp.instLocallyFiniteOrder`
  - Result: succeeds — `Roth.box r = Iic (Finsupp.equivFunOnFinite.symm r)` by `ext d; simp [Roth.mem_box, Finsupp.le_def]` (evidence)
  - Notes: `mem_box` becomes `Finset.mem_Iic` + `Finsupp.le_def`; `card_box` becomes `Finsupp.card_Iic`, `Nat.card_Iic`, `Finset.prod_subset` (3 calls, evidence).

Conclusion: COMPOSABLE (indeed a single mathlib construction).

## Verdict: `Roth.box`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): the box is the lower interval `[0, r]` in `ℕ^σ` (product of chains), count `∏(r_j+1)`; project paper §6, l.1058-1092, 1420.
- Generality analysis (Phase 4): narrower than standard, but the standard form is mathlib's `Finset.Iic` (false-positive class 4).
- Mathlib search (Phase 5): found as `Finset.Iic` on `σ →₀ ℕ` (`Finsupp.instLocallyFiniteOrder`, Mathlib/Data/Finsupp/Interval.lean:85) with `Finsupp.card_Iic` (l.125).
- Composition check (Phase 6): COMPOSABLE; `box r = Finset.Iic (Finsupp.equivFunOnFinite.symm r)` compiles.

**Rationale:**

`Roth.box r` is the finite set `{d : σ →₀ ℕ | d ≤ r}`, which mathlib already provides as `Finset.Iic` in the locally finite order on finitely supported functions (and as `Finset.Icc 0 _`). The evidence file proves `Roth.box r = Finset.Iic (Finsupp.equivFunOnFinite.symm r)` in one line, recovers `mem_box` from `Finset.mem_Iic`/`Finsupp.le_def`, and recovers `card_box` from `Finsupp.card_Iic` and `Nat.card_Iic` after passing from `r.support` to `univ` with `Finset.prod_subset`. The mathlib form is strictly more general (no `Fintype σ` needed, arbitrary locally finite canonically ordered codomain). The project itself already uses the mathlib form inline at Roth/MainLemma.lean:282.

WHY not: mathlib has the concept as `Finset.Iic`; `Roth.box` is a second implementation (via `Fintype.piFinset` and `Finset.map`) whose only advantage is that unfolding it gives the `piFinset` description used once with `Finset.prod_univ_sum` (Roth/CoeffNorm.lean:216). Belongs-elsewhere check: keep it project-local at most, as a thin abbreviation `box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r)` for readability of the Lemma 8 statements; the name `box` also collides with mathlib's unrelated `Finset.box`, `Behrend.box` and `BoxIntegral` boxes, so it should not be upstreamed.

Existing mathlib decl:        `Finset.Iic` (instance `Finsupp.instLocallyFiniteOrder`; lemmas `Finset.mem_Iic`, `Finsupp.card_Iic`)
Located at:                   `Mathlib/Data/Finsupp/Interval.lean:85` (instance), `:125` (`card_Iic`)
Our form follows in ≤1 line:
```lean
example (r : σ → ℕ) : Roth.box r = Finset.Iic (Finsupp.equivFunOnFinite.symm r) := by
  ext d; simp [Roth.mem_box, Finsupp.le_def]
```
Call sites in our project (from Phase 6.0):  30+ (Roth/Taylor.lean, Roth/CoeffNorm.lean, Roth/Main.lean, Roth/MainLemma.lean, Roth/Lattice.lean) plus `mem_box`, `card_box`, `card_le_card_box` in Roth/Box.lean.
Refactor plan: change the body of `Roth.box` to `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (keeping the name, so the 30+ call sites are unchanged); reprove `mem_box` by `simp [box, Finsupp.le_def]` and `card_box` by `Finsupp.card_Iic` + `Nat.card_Iic` + `Finset.prod_subset`; add `box_eq_map_piFinset` for Roth/CoeffNorm.lean:216 (or rewrite that proof via `Finset.prod_univ_sum` after the bridge); optionally replace the inline `Finset.Iic (Finsupp.ofSupportFinite r _)` in Roth/MainLemma.lean:282/295 by `box r` where `σ` is finite. Full inlining (deleting `box`) is also possible but would make the Lemma 8 statements in Roth/Lattice.lean noisier.
Next action: do not upstream; locally redefine `Roth.box` via `Finset.Iic` as above (or keep as-is if the refactor is not worth the churn — no mathlib action either way).

---

## Next step

Redefine `Roth.box r := Finset.Iic (Finsupp.equivFunOnFinite.symm r)`, reprove `mem_box`/`card_box` from `Finset.mem_Iic`/`Finsupp.card_Iic`, and add a `piFinset` bridge for Roth/CoeffNorm.lean:216; no mathlib PR.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.box/box_eq_Iic.lean` (compiles cleanly with `lake env lean`, importing `Roth.MainLemma` for the `Finsupp.orderBot` instance): proves `Roth.box r = Finset.Iic (Finsupp.equivFunOnFinite.symm r)`, `Roth.box r = Finset.Icc 0 (...)`, membership via `Finset.mem_Iic`, `#(Iic r) = ∏ j, (r j + 1)` via `Finsupp.card_Iic`/`Nat.card_Iic`/`Finset.prod_subset`, and `mem_Iic` without `Fintype` (with `DecidableEq`).
- Earlier runs of the same file (overwritten): with only `import Roth.Box` the `Iic` form fails (`LocallyFiniteOrderBot (σ →₀ ℕ)` not synthesised: `Finsupp.orderBot` lives in Mathlib/Data/Finsupp/Order.lean, not imported by Roth/Box.lean's imports); a probe dropping `[DecidableEq σ]` from the `box` body failed (`Fintype.piFinset` needs it); `Iic` on `τ →₀ ℕ` without `DecidableEq τ` fails.
- Mathlib greps: `def box` (only unrelated `Finset.box`, `BoxIntegral.unitPartition.box`, `Behrend.box`), `namespace Roth` (none), `Finsupp/Interval.lean` (instance l.85, `card_Iic` l.125).
- Loogle (1 query): `Finsupp.card_Iic`, `DFinsupp.card_Iic`, `Pi.card_Iic`, `Multiset.card_Iic`. LeanSearch (1): `DFinsupp.card_Iic`, `Finset.card_finsupp`. Lean-Finder (1): `DFinsupp.rangeIcc`, `Behrend.box`.
- WebSearch: 3 queries (recorded in the literature table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rnw "box\|mem_box\|card_box" Roth/` for the call-sites table.
