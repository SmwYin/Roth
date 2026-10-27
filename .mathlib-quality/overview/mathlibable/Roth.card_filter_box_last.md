---
decl: Roth.card_filter_box_last
file: Roth/Lattice.lean
line: 131
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: MODERATE
junk: KEEP
rationale: Fibrewise (Fubini/double-counting) count of a filtered box over the last coordinate; the Roth form is tied to the project-local box (itself slated for REPLACE by Finset.Iic) and a hand-rolled Finsupp snoc, while the clean general form over Fintype.piFinset with Fin.snoc is absent from mathlib (only init-predicate versions exist) and compiles in 20 lines, so upstreaming is a judgment call.
action: Keep in Roth/Lattice.lean (sole caller Roth.card_filter_weight_le_succ_aux, l.175); if the user wants an upstream PR, propose the piFinset form compiled in evidence/Roth.card_filter_box_last/general_piFinset.lean to Mathlib/Data/Fin/Tuple/Finset.lean next to Finset.card_snocEquiv_filter_piFinset.
---

# Roth.card_filter_box_last

## Inventory entry

### `theorem Roth.card_filter_box_last`
- **Type**: `∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop) [DecidablePred p], ((box r).filter p).card = ∑ i ∈ range (r (Fin.last m) + 1), ((box (r ∘ Fin.castSucc)).filter fun d ↦ p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card`
- **What**: For a box `∏_{j ≤ m} [0, r_j]` of multi-indices and any decidable predicate `p`, the number of points of the box satisfying `p` equals the sum over `i ∈ [0, r_last]` of the number of points `d` of the lower-dimensional box `∏_{j < m} [0, r_j]` whose extension `(d, i)` satisfies `p`. This is the discrete Fubini / double-counting identity for the last-coordinate projection.
- **How**: `Finset.card_eq_sum_card_fiberwise` with `f := fun d ↦ d (Fin.last m)` and `t := range (r (Fin.last m) + 1)` (maps-to via `mem_box`, `Nat.lt_succ_iff`), then `Finset.sum_congr` with the private fibre bijection `Roth.card_filter_box_fiber_aux`.
- **Hypotheses**: `[DecidablePred p]` (needed for `Finset.filter`); no other hypotheses.
- **Uses from project**: `Roth.box`, `Roth.mem_box` (Roth/Box.lean:47, 51), `Roth.card_filter_box_fiber_aux` (Roth/Lattice.lean:100).
- **Used by**: Roth/Lattice.lean:175 (`rw [card_filter_box_last, ...]` in private `Roth.card_filter_weight_le_succ_aux`, the induction step of Lemma 8). `grep -rn card_filter_box_last Roth/` gives only l.131 and l.175.
- **Visibility**: public
- **Lines**: 131–142, proof length 8 lines (135–142)
- **Notes**: The extension `d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i` is a hand-rolled `Finsupp.snoc`; mathlib's `Mathlib/Data/Finsupp/Fin.lean` has only `Finsupp.cons`/`Finsupp.tail`.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Lattice.lean:175), at the heart of the Lemma 8 induction.
- Wrapper of 1–2 mathlib calls? Not quite: it is `Finset.card_eq_sum_card_fiberwise` plus a 20-line project bijection (`card_filter_box_fiber_aux`).
- Does mathlib have it? No. Closest: `Finset.card_snocEquiv_filter_piFinset` / `Finset.filter_piFinset_eq_map_snocEquiv` (Mathlib/Data/Fin/Tuple/Finset.lean:77, 92) handle only predicates of `Fin.init r`; `Fintype.card_filter_piFinset_eq` (Mathlib/Data/Fintype/BigOperators.lean:184) counts a fibre with no predicate. No general-predicate fibrewise sum.
- Too specific / inline? Inlining would put the fibre bijection into the 40-line `card_filter_weight_le_succ_aux`; a separate counting lemma keeps the combinatorics apart from the analysis, as the source's Lean note asks.
- Well-chosen? Yes, the statement is exactly the induction-step identity; it is phrased against the project-local `box` (which the `Roth.box` report recommends replacing by `Finset.Iic`).
- Conclusion: `KEEP`. Action: none locally; if `box` is replaced by `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`, restate accordingly.

## Mathlibable assessment (Step 9)

Pre-filter: public; no `_aux` suffix; docstring does not start with internal/auxiliary; Step 8 said KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `card_filter_box_last` finds nothing. Not a glue lemma (8-line proof with a bijection). Full workflow follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief)
- decl `Roth.card_filter_box_last`: ✓ resolved at Roth/Lattice.lean:131
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the lattice count estimate (Lemma 8): few multi-indices `j ≤ r` with `∑ j_i/r_i ≤ (m-λ)/2`.

### Statement (Phase 1)

`Roth.card_filter_box_last` is a theorem stating the following. Let `B = ∏_{j=0}^{m} [0, r_j] ⊂ ℕ^{m+1}` and `B' = ∏_{j=0}^{m-1} [0, r_j]`. For any predicate `p` on `ℕ^{m+1}`,
`#{d ∈ B : p(d)} = ∑_{i=0}^{r_m} #{d' ∈ B' : p(d', i)}`,
i.e. a subset of a product is counted by summing the sizes of its sections over the last factor.

Variables / typeclasses involved (Lean side):
- `m : ℕ`: dimension minus one
- `r : Fin (m + 1) → ℕ`: box bounds
- `p`: arbitrary predicate on multi-indices, `[DecidablePred p]` for filtering

Hypotheses (Lean side):
- none

Conclusion (math): the cardinality of the filtered box is the sum over the last coordinate of the cardinalities of the filtered sections.

Conclusion (Lean): `((box r).filter p).card = ∑ i ∈ range (r (Fin.last m) + 1), ((box (r ∘ Fin.castSucc)).filter fun d ↦ p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a counting helper for the induction step of Lemma 8; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 8
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | `counting lattice points in a box by fibres over last coordinate induction on dimension Roth lemma` | no | none | hits on lattice-point counting in fibres of definable families (Barroero–Widmer), Skriganov counting, Chazelle on Roth discrepancy; none states this identity |
| 2 | WebSearch (general form) | `"double counting" cardinality of subset of product set equals sum of fibre sizes over projection` | partial | `#S = ∑_z #(S ∩ π⁻¹ z)` used inline (arXiv 2609.05384 §5), never named | folklore double counting; Cornell CS2800 notes on disjointness |
| 3 | WebSearch (named-after / aliases) | `Fubini principle for finite sets counting abs A = sum over x of abs A_x sections of product` | yes | Fubini/Tonelli with counting measure: `#A = ∑_x #A_x` for `A ⊆ X × Y` | standard; stated as the counting-measure case of Fubini (x-sections `E_x`) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among the available or deferred tools) |
| 5 | Local references | `grep -n -i "fibre\|fiber" .mathlib-quality/references/clean.tex` | yes | clean.tex l.1132–1137 (§6 Lean note): "induction counts the fibres of the last-coordinate projection" | the paper itself does not state the identity; it is an implementation device |
| 6 | nLab | "double counting" / "Fubini" | n/a | none | nLab treats Fubini only in measure/categorical (end/coend) settings; no finite-set statement to compare against |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept beyond the trivial `A ≅ Σ_x A_x` in Set |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | covered by #2/#3 (general web search spans these sites) | no | none | identity is too elementary for a dedicated thread |
| 10 | recent arXiv (last 5 years) | covered by #1/#2 | partial | used inline (arXiv 2609.05384 Prop. 5.5 proof) | never isolated |

### Literature summary (Phase 3)

Concept identified as: double counting / discrete Fubini (sum of section sizes) for the projection of a finite product onto its last factor.
Sources agree on the standard form: yes — `#A = ∑_{x ∈ X} #{y : (x, y) ∈ A}` for finite `A ⊆ X × Y`.
Most general standard form: for any map `f : s → t`, `#s = ∑_{b ∈ t} #f⁻¹(b)` (mathlib's `Finset.card_eq_sum_card_fiberwise`); specialised to a product (`piFinset S` over `Fin (n+1)`), each fibre over `a ∈ S_last` is identified with `{r ∈ piFinset (init S) : P (snoc r a)}`.
Generality dimensions where the literature varies:
  - coordinate sets: intervals `[0, r_j]` (here) to arbitrary finite sets `S_j` (general)
  - ambient type: `ℕ^σ` as finsupps (here) to plain functions / dependent tuples (general)
Disagreement with the literature: none; the project form is the box specialisation.

### Generality analysis — `Roth.card_filter_box_last`

Literature-standard form (from Phase 3): `#{r ∈ ∏ S_j : P r} = ∑_{a ∈ S_last} #{r' ∈ ∏_{j<n} S_j : P (snoc r' a)}`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coordinate sets | intervals `range (r j + 1)` via `box r` | arbitrary `S j : Finset α` | yes | verified: the piFinset form compiles (evidence file) |
| 2 | ambient type | `Fin (m+1) →₀ ℕ` with hand-rolled snoc | `Fin (n+1) → α` with `Fin.snoc` | yes, but a different type | transporting needs `Finsupp.equivFunOnFinite`; restating Roth's form requires changing `box` (multi-file) |
| 3 | `[DecidablePred p]` | required | required | NO | needed by `filter` |
| 4 | last coordinate | `Fin.last` | any pivot `p` via `insertNth` | yes (in principle) | mathlib has the `insertNth` analogues for init-predicates; not compiled here, not needed by the project |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (as a statement), but the weakening is not a single mechanical edit of this lemma: it changes the ambient type from `σ →₀ ℕ`/`box` to `piFinset`.
Number of weakening opportunities found: 1 verified (general `piFinset` form, compiled clean in `.mathlib-quality/overview/evidence/Roth.card_filter_box_last/general_piFinset.lean`).
Proposed restatement (general form, verified):

```lean
theorem Finset.card_filter_piFinset_eq_sum_snoc {n : ℕ} {α : Type*} [DecidableEq α]
    (S : Fin (n + 1) → Finset α) (P : (Fin (n + 1) → α) → Prop) [DecidablePred P] :
    #{r ∈ piFinset S | P r} =
      ∑ a ∈ S (Fin.last n), #{r ∈ piFinset (Fin.init S) | P (Fin.snoc r a)}
```

Cost of restatement: MODERATE (the general lemma is done; deriving the Roth form from it needs a transport along `Finsupp.equivFunOnFinite` or the `box` → `Finset.Iic` refactor).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | typeclasses instead of bundled hypotheses | no | no hypotheses to bundle | n/a |
| 2 | filters instead of sequences | no | finite combinatorics | n/a |
| 3 | universal property | no | no construction | n/a |
| 4 | bundled substructure | no | `Finset` is already the bundled form | n/a |
| 5 | weaken field-specific typeclasses | no | none present | n/a |
| 6 | higher-categorical | no | n/a | n/a |
| 7 | concrete index generalised | yes | intervals `[0, r_j]` → arbitrary `S j`; `Fin.last` → any pivot | sits beside `Finset.card_snocEquiv_filter_piFinset`, `filter_piFinset_eq_map_snocEquiv` |
| 8 | concrete-via-abstract | yes | `box` is used only through `mem_box` (coordinatewise membership); the proof is the general piFinset argument | general lemma serves any product finset |
| 9 | false-generalisation guard | no | the piFinset form specialises to the box form via `box r = map equivFunOnFinite.symm (piFinset (range (r j + 1)))` — same mathematical content | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finset.card_filter_piFinset_eq_sum_snoc` above (plain tuples, `Fin.snoc`).
  - Cost: MODERATE (for the Roth side; the general lemma already compiles).
  - Mathlib downstream this enables: general-predicate companion to `Finset.card_snocEquiv_filter_piFinset` (which only allows predicates of `init r`); fibrewise induction on dimension over `piFinset`.
  - Real mathematical improvement: removes the dependence on the interval shape and on the finsupp encoding, which play no role in the argument.

### Proof strategy — `Roth.card_filter_box_last`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | n/a | n/a |
| 2 | elements vs ideals | no | n/a | n/a |
| 3 | sequences vs nets | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing mathlib helpers | yes | `Finsupp.snoc`/`Finsupp.init` (analogues of `Finsupp.cons`/`tail` in Mathlib/Data/Finsupp/Fin.lean) would replace the `mapDomain castSucc + single last i` encoding and the private `extend_apply_*` lemmas; alternatively the general piFinset lemma | MODERATE |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC for the top level (`card_eq_sum_card_fiberwise` + `sum_congr`); the fibre bijection would shorten given a `Finsupp.snoc` API or the general piFinset lemma.
  - Missing mathlib API: `Finsupp.snoc`/`Finsupp.init`; general-predicate `card_filter_piFinset_eq_sum_snoc`.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.card_filter_box_last`

[A] Lean-Finder       "number of tuples satisfying P equals sum over values a of the last coordinate of number of init tuples r with P (snoc r a)"   no exact hit; returns `Finset.card_snocEquiv_filter_piFinset`, `card_consEquiv_filter_piFinset`, `card_insertNthEquiv_filter_piFinset` (init/tail-predicate only), `Fintype.card_filter_piFinset_eq` (fibre size, no predicate)
[B] Loogle            `Finset.card (Finset.filter _ (Fintype.piFinset _)) = Finset.sum _ _`   no hits
[C] LeanSearch        "cardinality of filtered piFinset equals sum over last coordinate of cardinality of filter with snoc"   same partial hits as [A]
[D] Grep mathlib src  `piFinset_succ`, `piFinset_snoc`, `card_filter_piFinset`, `Finsupp.snoc`, `def snoc` in Data/Finsupp: only `card_filter_piFinset_eq(_of_mem)`, `card_filter_piFinset_const` (Mathlib/Data/Fintype/BigOperators.lean:169–190) and `snoc_mem_piFinset_snoc`; no Finsupp snoc; `Finset.card_eq_sum_card_fiberwise` (Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:993) is the generic building block
[E] Name pattern      `card_filter_box_last` / `card_filter_piFinset_eq_sum` in mathlib: none

Searched for both the user's form and the general piFinset form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks: `Finset.card_eq_sum_card_fiberwise`, `Finset.card_bij'`, `Fin.snoc_init_self`, `Fin.init_snoc`, `Fin.snoc_castSucc`.

### Normal-form check — `Roth.card_filter_box_last`

Equivalent formalisms this statement could take: (a) the current sum over `range (r_last + 1)` of filtered lower boxes; (b) a sum over `Finset.Iic` fibres; (c) `filter p (box r)` as a `Finset.sigma`/`biUnion` over `i`.
Does mathlib already have a canonical form for this idea? Partially: `card_eq_sum_card_fiberwise` (generic) and the `card_snocEquiv_filter_piFinset` family (product form).
Our statement is in the "card = sum of cards" shape used by mathlib's fiberwise lemmas: OK.
RHS convention respected? n/a (not a simp lemma)

### Syntactic generality — `Roth.card_filter_box_last`

Alternative restatements attempted:
- general piFinset form with `Fin.snoc` (compiled)
- statement with fibres `((box r).filter p).filter (· (Fin.last m) = i)` on the right (this is just `card_eq_sum_card_fiberwise`; less useful to the caller)

Chosen restatement: the current form for the project.
Justification: the caller (l.175) needs the sections expressed in the lower box so the induction hypothesis applies after `card_filter_fiber_eq`.

### Superfluous-argument audit — `Roth.card_filter_box_last`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[DecidablePred p]` | yes | needed for `filter` |
| 2 | `r` | yes | defines the box |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK for the project; RESTATE (piFinset form) if upstreamed
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project); RESTATE-BEFORE-SHIP (mathlib)

### Call sites — `Roth.card_filter_box_last`

Internal use count: 1 (in the declaring file; 0 in other files)
External-to-file callers: 0

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Lattice.lean:175 | `rw [card_filter_box_last, Nat.cast_sum, Finset.sum_congr rfl fun i _ ↦ card_filter_fiber_eq r lam i]` in `Roth.card_filter_weight_le_succ_aux` |

Inline-derivation grep: `grep -rn "card_eq_sum_card_fiberwise" Roth/` shows only this lemma; no re-derivation elsewhere.

### Composition check (Phase 6)

Can `Roth.card_filter_box_last` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.card_eq_sum_card_fiberwise` then `Finset.sum_congr` with fibre cards.
  - Mathlib decls used: `Finset.card_eq_sum_card_fiberwise`, `Finset.sum_congr`
  - Result: partial — the fibre identification is a 20-line bijection (`card_filter_box_fiber_aux`).
Attempt 2: transport to `piFinset` and use `Finset.filter_piFinset_eq_map_snocEquiv`.
  - Result: fails — that lemma requires the predicate to depend only on `init r`; `p` here is arbitrary.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.card_filter_box_last`

Verdict: BORDERLINE-needs-human

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): discrete Fubini / double counting; standard but folklore, never a named lemma; the source (clean.tex l.1132–1137) mentions it only as an implementation note.
- Generality analysis (Phase 4): STRICTLY NARROWER as a statement; the general piFinset form compiles (evidence), but moving the Roth statement to it changes the ambient type (false-positive class 5: not a single mechanical edit).
- Mathlib search (Phase 5): not in mathlib; only init-predicate analogues (`Finset.card_snocEquiv_filter_piFinset`) and the generic `Finset.card_eq_sum_card_fiberwise`.
- Composition check (Phase 6): NOT-COMPOSABLE (needs a real bijection).

**Rationale:** The Roth statement itself is not a mathlib candidate: it is phrased against the project-local `box` (whose own report says REPLACE by `Finset.Iic`) and a hand-rolled finsupp snoc. Its mathematical content, however, is a clean general identity — `#{r ∈ piFinset S | P r} = ∑_{a ∈ S last} #{r ∈ piFinset (init S) | P (snoc r a)}` — which mathlib lacks: Mathlib/Data/Fin/Tuple/Finset.lean only covers predicates factoring through `init`. That general lemma compiles in about 20 lines from `card_eq_sum_card_fiberwise` and `card_bij'`. Whether such a folklore double-counting lemma is worth a mathlib PR (versus reviewers asking for the `card_eq_sum_card_fiberwise` + bijection to be done inline), and whether the project should restate its box API on `piFinset`/`Iic` to use it, are taste and policy calls.

Numbered questions:
1. Should the general form `Finset.card_filter_piFinset_eq_sum_snoc` (compiled in evidence) be proposed to Mathlib/Data/Fin/Tuple/Finset.lean beside `Finset.card_snocEquiv_filter_piFinset`? (Recommended: optional, low priority.)
2. Should `Roth.card_filter_box_last` stay project-local in its current finsupp/box form? (Recommended: yes.)
3. If `Roth.box` is refactored to `Finset.Iic` (per the `Roth.box` report), should this lemma be reproved from the general piFinset lemma rather than `card_filter_box_fiber_aux`? (Recommended: only if question 1 is yes.)
4. Should a `Finsupp.snoc`/`Finsupp.init` API (mirroring `Finsupp.cons`/`tail`) be added upstream to replace the `mapDomain castSucc + single last i` encoding? (Recommended: no, unless other uses appear.)

Next action: user answers the questions. With the recommended answers the lemma stays as is in Roth/Lattice.lean, used once at l.175.

---

### Next step

Keep `Roth.card_filter_box_last` in Roth/Lattice.lean (single caller `Roth.card_filter_weight_le_succ_aux`, l.175). Optionally upstream the general piFinset form from `.mathlib-quality/overview/evidence/Roth.card_filter_box_last/general_piFinset.lean` to Mathlib/Data/Fin/Tuple/Finset.lean.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.card_filter_box_last/general_piFinset.lean` (imports only `Mathlib.Data.Fin.Tuple.Finset` and `Mathlib.Algebra.BigOperators.Group.Finset.Basic`), compiled with `lake env lean`: clean, no errors or warnings. It proves the general form `card_filter_piFinset_eq_sum_snoc` via `card_eq_sum_card_fiberwise` + `card_bij'` (`Fin.snoc`/`Fin.init`). Two earlier runs failed (bijection direction swapped; `simpa` normalising `Fin.init S j`) and were fixed.
- Searches: WebSearch ×3, Lean-Finder ×1, LeanSearch ×1, Loogle ×1, mathlib grep (Data/Fin/Tuple/Finset.lean, Data/Fintype/BigOperators.lean, Data/Finsupp/Fin.lean, Algebra/BigOperators/Group/Finset/Basic.lean), local grep of clean.tex. ChatGPT MCP: n/a (not configured).
- `grep -rn card_filter_box_last Roth/`: l.131 (definition), l.175 (sole use).
- Read reports `Roth.box.md` (REPLACE by `Finset.Iic`) and `Roth.card_filter_box_fiber_aux.md` (private SKIP, deferring the upstream question to this lemma).
