---
decl: Roth.card_le_card_box
file: Roth/Box.lean
line: 65
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Re-aimed at Finset.Iic the statement is Finset.card_le_card of s ⊆ Iic r followed by the card_Iic count (Pi.card_Iic or Finsupp.card_Iic plus Nat.card_Iic), and for the current def it is card_le_card plus mem_box plus card_box; all compiled in evidence, nothing new for mathlib.
action: Keep locally as the convenience bound used at Roth/MainLemma.lean:506 and Roth/CoeffNorm.lean:264 (it spares both sites the box detour); if Roth.box is redefined as Finset.Iic, keep the proof as card_le_card plus mem_Iic plus card_box; do not upstream.
---

# Roth.card_le_card_box

## Inventory entry

### `theorem Roth.card_le_card_box`
- **Type**: `{σ : Type*} [Fintype σ] {r : σ → ℕ} {s : Finset (σ →₀ ℕ)} (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) : s.card ≤ ∏ j, (r j + 1)`
- **What**: A finset of multi-indices that are coordinatewise bounded by `r` has at most `∏ j (r j + 1)` elements (it sits inside the box `box r`).
- **How**: `classical`, then `(Finset.card_le_card fun d hd ↦ mem_box.2 (hs d hd)).trans_eq (card_box r)`: the inclusion `s ⊆ box r` via `Roth.mem_box`, `Finset.card_le_card`, then rewrite the box cardinality with `Roth.card_box`.
- **Hypotheses**: `hs` — every element of `s` is bounded by `r` coordinatewise. Section variable `[Fintype σ]` (the `[DecidableEq σ]` is omitted and recovered by `classical`).
- **Uses from project**: `Roth.mem_box`, `Roth.card_box` (and through them `Roth.box`)
- **Used by**: Roth/MainLemma.lean:506 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, bound on `#(hasseDeriv j P).support`); Roth/CoeffNorm.lean:264 (`abs_coeff_det_hasseDeriv_le`, Lemma 3, bound on `#P.support`).
- **Visibility**: public
- **Lines**: 62–68, proof length 2 lines
- **Notes**: Not a `:= rfl`/`Iff.rfl` glue lemma. Parent `Roth.box` is NO-mathlib-has-it (mathlib's `Finset.Iic`), so per the re-aim rule this was assessed against `s ⊆ Finset.Iic r → #s ≤ #(Iic r)`, not inherited. Both callers apply it to the support of an `MvPolynomial` bounded via `MvPolynomial.monomial_le_degreeOf`.

## Junk check (Step 8)
- Used anywhere? Yes: 2 call sites in 2 files (MainLemma.lean:506, CoeffNorm.lean:264).
- Wrapper of 1–2 mathlib calls? Yes: `Finset.card_le_card` + `.trans_eq` with the project's `card_box` (re-aimed: `card_le_card` + `Pi.card_Iic`/`Finsupp.card_Iic` + `Nat.card_Iic`).
- Does mathlib have it? Not verbatim; the general form `s ⊆ t → #s ≤ #t` is `Finset.card_le_card` and the count is `Pi.card_Iic`/`Finsupp.card_Iic` (evidence).
- Too specific (inline?)? Borderline: inlining at the 2 sites costs one line each, but the lemma hides the `box`/`Iic` detour behind a pointwise-hypothesis interface that matches both call sites exactly (`fun d hd j ↦ (monomial_le_degreeOf j hd).trans _`). Keeping it is reasonable.
- Well-chosen? Yes; the pointwise hypothesis is easier to supply than `s ⊆ box r`.
- Conclusion: `KEEP` — action: keep as the local bound; if `box` is redefined as `Finset.Iic`, the proof becomes `card_le_card` + `mem_Iic` + `card_box` (evidence example 2) with the same name and statement.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.card_le_card_box` not in mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`). Not glue. Parent `Roth.box` is NO-mathlib-has-it because mathlib has `Finset.Iic`, so the **re-aim rule** applies: full run aimed at `s ⊆ Iic r → #s ≤ ∏ (r j + 1)`. Re-aim result: hit in composition form (`Finset.card_le_card` + `Pi.card_Iic`/`Finsupp.card_Iic` + `Nat.card_Iic`), no verbatim mathlib lemma.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` has no diagnostics)
- decl `Roth.card_le_card_box`: resolved at Roth/Box.lean:65
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.card_le_card_box` is a theorem stating the following: let `σ` be a finite set and `r ∈ ℕ^σ`. If `S` is a finite set of multi-indices `d ∈ ℕ^(σ)` with `d_j ≤ r_j` for all `j`, then `#S ≤ ∏_j (r_j + 1)`. Equivalently: any subset of the lower interval `↓r` of `ℕ^σ` has at most `#↓r = ∏_j (r_j + 1)` elements. In Roth's proof it bounds the number of monomials of a polynomial of multidegree ≤ r.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (needed for the `univ` product).
- `r : σ → ℕ` — bounds.
- `s : Finset (σ →₀ ℕ)` — the finite set of multi-indices.

Hypotheses (Lean side):
- `hs : ∀ d ∈ s, ∀ j, d j ≤ r j` — `s ⊆ ↓r`.

Conclusion (math): `#S ≤ (r_1 + 1) ⋯ (r_m + 1)`.

Conclusion (Lean): `s.card ≤ ∏ j, (r j + 1)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: corollary of `card_box` by monotonicity of cardinality; helper lemma.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: n/a (theorem)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | number of monomials with degree at most r_j in each variable at most (r_1+1)...(r_m+1) coefficients bound | partial | exponent choices independent, count `∏(r_j+1)`; a polynomial of multidegree ≤ r has at most that many terms | Wikipedia "Monomial"; arXiv 2410.20162 (per-variable degree bound counts) |
| 2 | WebSearch (general form) | subset of a finite set has cardinality at most that of the set; lower set of product order cardinality bound | partial | monotonicity of cardinality is elementary; lower sets in `ℕ^d` studied for counting | arXiv 2208.02113, 1909.06719 (lower sets in `ℕ^m`); no lemma-level statement beyond `S ⊆ T ⇒ #S ≤ #T` |
| 3 | WebSearch (named-after / aliases) | Roth theorem proof support of polynomial multidegree bounded number of terms (r_1+1)(r_2+1) Siegel lemma unknowns | yes | `N = ∏(d_i+1)` is the number of terms/unknowns of a polynomial of degree ≤ d_i in X_i | arXiv 1806.10737; arXiv 2502.00731 (Evertse); Evertse Luminy slides |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `Pad the monomial`, `r_1 + 1` | yes | l.454: "Set `N=∏_j(r_j+1)`. Pad the monomial expansion ..." (the source cited in the docstring); l.441, 724, 736 | project paper §3, Lemma 3 |
| 6 | nLab | finite set / cardinality monotone under inclusion | partial | cardinality is monotone under injections | generic; no box-specific entry |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | elementary finite combinatorics, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1–#3: monomial count of bounded multidegree) | partial | folklore `#{monomials of multidegree ≤ r} = ∏(r_j+1)` | no dedicated thread needed |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | yes | arXiv 2502.00731 (2025), 2410.20162 (2024), 2208.02113 (2022) | same product formula / lower-set framing |

### Literature summary (Phase 3)

Concept identified as: monotonicity of cardinality applied to the lower interval `[0, r]` of `ℕ^σ`; equivalently "a polynomial of multidegree ≤ r has at most ∏(r_j+1) monomials".
Sources agree on the standard form: yes.
Most general standard form: if `S ⊆ Iic b` in a locally finite order with bottom then `#S ≤ #Iic b`; for a product of chains `#Iic b = ∏_i #Iic (b_i)`.
Generality dimensions where the literature varies:
  - codomain: `ℕ` vs any locally finite order with bottom.
  - ambient type: functions on a finite set vs finitely supported functions.
Disagreement with the literature: none.

### Generality analysis — `Roth.card_le_card_box`

Literature-standard form (from Phase 3): `S ⊆ Iic b → #S ≤ ∏ i, #(Iic (b i))`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | required | needed for `univ` product | no (for this RHS) | the `univ` product needs it; a support-product form would need a bound on the support of `r`, i.e. `r : σ →₀ ℕ` |
| 2 | `hs` pointwise bound | `∀ d ∈ s, ∀ j, d j ≤ r j` | `s ⊆ Iic r` | equivalent | same content; pointwise form is more convenient at both call sites |
| 3 | codomain `ℕ` | ℕ | any locally finite order with bottom | yes | realised by `card_le_card` + `Pi.card_Iic` (evidence example 4); no new lemma needed |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is the composition `Finset.card_le_card` + `Pi.card_Iic` (compiled, evidence example 4), i.e. false-positive class 4 ("general form already in mathlib").
Number of weakening opportunities found: 1 (row 3), realised by existing mathlib lemmas; verified in `card_le_card_box_reaim.lean`.
Proposed restatement: none to add to mathlib.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | only a membership hypothesis |
| 2 | sequences to filters? | no | — | finite combinatorics |
| 3 | construction vs universal property? | yes | phrase via `s ⊆ Iic r` instead of the `piFinset` box | `Finset.mem_Iic`, `Finset.card_le_card`, `card_Iic` API |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `#s ≤ ∏ i, #(Iic (b i))` for locally finite codomains | already composable (`Pi.card_Iic`) |
| 8 | concrete-via-abstract? | yes | the proof only uses `s ⊆ ↓r` and `#↓r`; `box` appears only through `mem_box`/`card_box` | as #3 |
| 9 | false-generalisation guard | no false generalisation | evidence proves the same bound for `box`, `Iic` on `σ →₀ ℕ`, `Iic` on `σ → ℕ` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `card_le_card (hs : s ⊆ Iic r)` composed with `Finsupp.card_Iic`/`Pi.card_Iic` and `Nat.card_Iic` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: interval API once `box` is `Iic`.
  - Real mathematical improvement: none beyond the parent refactor.

### Proof strategy — `Roth.card_le_card_box`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after parent refactor: `card_le_card` + `mem_Iic` + `card_box` | CHEAP |
| 5 | missing mathlib helpers | partial | an `MvPolynomial` lemma `#p.support ≤ ∏ j, (degreeOf j p + 1)` does not exist in mathlib (LeanSearch); both call sites are instances of it (evidence example 5); too thin to propose on its own | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`card_le_card` of an inclusion, then the exact count).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.card_le_card_box`

[A] Lean-Finder       "a set of multi-indices each coordinatewise bounded by r has at most prod (r_j + 1) elements"   hits: `Behrend.box`/`Behrend.card_box` (unrelated `< d` box), `Pi.card_Iic`, `BoxIntegral...card_filter_mem_Icc_le` (unrelated); no bound lemma
[B] Loogle            `Finset.card _ ≤ Finset.card (Finset.Iic _)`   no hits
[C] LeanSearch        "finset of finitely supported functions bounded pointwise by r has card at most product of (r j + 1)"; "MvPolynomial support card bounded by product of degreeOf plus one"   hits: `DFinsupp.card_Iic`, `Finset.card_finsupp`, `Finsupp.card_pi`; `MvPolynomial.monomial_le_degreeOf` (building block); no bound lemma
[D] Grep mathlib src  `theorem card_le_card` (Mathlib/Data/Finset/Card.lean:66), `card_Iic` (Mathlib/Data/Finsupp/Interval.lean:125, Mathlib/Data/Pi/Interval.lean), `namespace Roth`   hits: building blocks only; no `Roth` namespace
[E] Name pattern      `Finset.card_le_card`, `Finset.mem_Iic`, `Pi.card_Iic`, `Finsupp.card_Iic`, `Nat.card_Iic`, `MvPolynomial.monomial_le_degreeOf` (all used in compiled evidence)   hits

Searched for both the user's form (pointwise bound → `∏ (r j + 1)`) and the re-aimed form (`s ⊆ Iic r → #s ≤ ...`).

Concluded: found building blocks (`Finset.card_le_card`, `Finset.mem_Iic`, `Pi.card_Iic`/`Finsupp.card_Iic`, `Nat.card_Iic`); composition yields our form.

### Normal-form check — `Roth.card_le_card_box`

Equivalent formalisms: `s ⊆ box r → #s ≤ ∏ (r j + 1)`; `s ⊆ Iic r → #s ≤ #(Iic r)`; pointwise-hypothesis form (current).
Does mathlib already have a canonical form for this idea? yes: `Finset.card_le_card` (monotonicity) plus `card_Iic`.
Is our statement stated against the canonical form? yes for a local convenience lemma (closed product RHS).
RHS convention respected? yes

### Syntactic generality — `Roth.card_le_card_box`

Alternative restatements attempted:
- `(hs : s ⊆ box r) : #s ≤ ∏ j, (r j + 1)` (one `mem_box` step more at each call site)
- `(hs : s ⊆ Iic r) : #s ≤ ∏ j, (r j + 1)` for `σ → ℕ` (compiles, evidence 3)
- current pointwise form
Chosen restatement: current.
Justification: both call sites supply `fun d hd j ↦ (monomial_le_degreeOf j hd).trans _` directly.

### Superfluous-argument audit — `Roth.card_le_card_box`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | `univ` product and `box` |
| 2 | `[DecidableEq σ]` | already omitted | recovered by `classical` |
| 3 | `hs` | yes | the inclusion |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; nothing ships to mathlib)

### Call sites — `Roth.card_le_card_box`

Internal use count: 2 (outside the declaring file)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:506 | `exact_mod_cast card_le_card_box fun d he k ↦ (monomial_le_degreeOf k he).trans (hdP k)` |
| Roth/CoeffNorm.lean:264 | `exact_mod_cast card_le_card_box fun d hd j ↦ (monomial_le_degreeOf j hd).trans (hP j)` |

Inline-derivation grep (`grep -rn "card_le_card.*mem_box\|card_le_card.*Iic" Roth/`):
  - only Roth/Box.lean:68 (the declaration's own proof); no inline re-derivation elsewhere.

### Composition check (Phase 6)

Can `Roth.card_le_card_box` be derived from mathlib in ≤3 chained calls?

Attempt 1 (current def): `(Finset.card_le_card fun d hd ↦ mem_box.2 (hs d hd)).trans_eq (card_box r)`
  - Mathlib decls used: `Finset.card_le_card`, `LE.le.trans_eq` (+ project `mem_box`, `card_box`)
  - Result: succeeds (evidence example 1)

Attempt 2 (re-aimed, finsupp `Iic`): `card_le_card` + `mem_Iic`, then `Finsupp.card_Iic`, `Nat.card_Iic`, `prod_subset`
  - Result: succeeds (evidence example 2); the count part is exactly the re-aimed `card_box`

Attempt 3 (re-aimed, pi `Iic`): `simpa only [Pi.card_Iic, Nat.card_Iic] using card_le_card hs`
  - Result: succeeds (evidence example 3); general codomain also succeeds (example 4)

Conclusion: COMPOSABLE

## Verdict: `Roth.card_le_card_box`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): monotonicity of cardinality applied to the box `[0, r]`; source paper l.454 ("Set `N=∏_j(r_j+1)`. Pad the monomial expansion ...").
- Generality analysis (Phase 4): narrower than standard, but the general form is the mathlib composition `card_le_card` + `Pi.card_Iic` (compiled).
- Mathlib search (Phase 5): building blocks found; no verbatim lemma.
- Composition check (Phase 6): COMPOSABLE (≤3 calls for the current def and both re-aimed forms).

**Rationale:**

Re-aimed at the parent's mathlib form, the statement is `Finset.card_le_card (s ⊆ Iic r)` followed by the count `#(Iic r) = ∏ (r j + 1)`, which is `Pi.card_Iic` + `Nat.card_Iic` on `σ → ℕ` or `Finsupp.card_Iic` + `Nat.card_Iic` + `prod_subset` on `σ →₀ ℕ`. For the current `piFinset` definition it is `card_le_card` + `mem_box` + `card_box`. All forms, and the general locally-finite-codomain version, compile in the evidence file. The only mathematically meaningful packaging absent from mathlib is the `MvPolynomial` bound `#p.support ≤ ∏ j, (degreeOf j p + 1)` (both call sites are instances of it), but that is itself a two-call composition with `MvPolynomial.monomial_le_degreeOf` and too thin to propose from this project.

WHY not: composable from existing mathlib in ≤3 calls; it is a local convenience corollary of `card_box`. Belongs-elsewhere check: keep it in Roth/Box.lean beside `box`/`card_box`; inlining is possible but would add the `box` detour to both callers, so the lemma is kept rather than deleted (deviation from the bucket's default "delete and inline", justified by the cleaner call sites).

Mathlib building blocks:      `Finset.card_le_card` (Mathlib/Data/Finset/Card.lean:66), `Finset.mem_Iic`, `Pi.card_Iic` (Mathlib/Data/Pi/Interval.lean), `Finsupp.card_Iic` (Mathlib/Data/Finsupp/Interval.lean:125), `Nat.card_Iic` (Mathlib/Order/Interval/Finset/Nat.lean)
Composition sketch (≤3 lines):
```lean
example [DecidableEq σ] {r : σ → ℕ} {s : Finset (σ → ℕ)} (hs : s ⊆ Iic r) :
    #s ≤ ∏ j, (r j + 1) := by
  simpa only [Pi.card_Iic, Nat.card_Iic] using card_le_card hs
```
Call sites in our project (from Phase 6.0):  2 (Roth/MainLemma.lean:506, Roth/CoeffNorm.lean:264)
Refactor plan: optional. If inlining, at each of the 2 sites replace `card_le_card_box fun d hd j ↦ H` with `(Finset.card_le_card fun d hd ↦ mem_box.2 fun j ↦ H).trans_eq (card_box r)` (needs `classical` for `box`). Recommended: keep the lemma; if `Roth.box` becomes `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`, reprove it with `mem_Iic` in place of `mem_box` (evidence example 2) and leave the call sites unchanged.
Next action: do not upstream; keep `Roth.card_le_card_box` locally.

---

## Next step

No mathlib action. Keep `Roth.card_le_card_box` as the local bound for the two support-cardinality call sites; reprove via `Finset.mem_Iic` when the parent `Roth.box` is redefined as `Finset.Iic`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.card_le_card_box/card_le_card_box_reaim.lean` (imports `Roth.MainLemma` for the finsupp `OrderBot`/interval instance, `Mathlib.Data.Pi.Interval` for `Pi.card_Iic`; `lean_diagnostic_messages`: no diagnostics on first run): (1) current statement via `card_le_card`/`mem_box`/`card_box`; (2) re-aimed finsupp `Iic` form via `card_le_card`/`mem_Iic`/`Finsupp.card_Iic`/`Nat.card_Iic`/`prod_subset`; (3) re-aimed `σ → ℕ` form in one `simpa` with `Pi.card_Iic`/`Nat.card_Iic`; (4) general locally-finite codomain `#s ≤ ∏ i, #(Iic (b i))`; (5) call-site shape `#P.support ≤ ∏ (r j + 1)` from `degreeOf` bounds.
- Mathlib greps: `theorem card_le_card` (Finset/Card.lean:66), `card_Iic` (Finsupp/Interval.lean:125); no `namespace Roth`.
- Loogle (1, no hits), LeanSearch (2), Lean-Finder (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex.
- Project grep `grep -rn card_le_card_box Roth/` for the call-sites table; inline-derivation grep found nothing.
