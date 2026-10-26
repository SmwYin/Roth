---
decl: Roth.weight_le_card
file: Roth/Box.lean
line: 103
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent is NO-mathlib-has-it), mathlib has no upper-bound lemma for Finsupp.weight, but the general form weight w d ≤ card σ • c (termwise d i • w i ≤ c) is one call to Finset.sum_le_card_nsmul after Finsupp.weight_eq_sum, and the project form is one call plus div_le_one_of_le₀ (all verified).
action: Keep as project-local API in Roth/Box.lean for its single call site Roth/Index.lean:227 (index_le_card); optionally reprove as Finset.sum_le_card_nsmul + div_le_one_of_le₀; no mathlib PR.
---

# Roth.weight_le_card

## Inventory entry

### `theorem Roth.weight_le_card`
- **Type**: `{σ : Type*} [Fintype σ] {r : σ → ℕ} {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) : Roth.weight r d ≤ Fintype.card σ`
- **What**: A multi-index in the box `d ≤ r` (coordinatewise) has weight `∑ j, d j / r j` at most the number of variables `card σ`.
- **How**: Term proof: `Finset.sum_le_sum` with each summand bounded by `1` via `div_le_one_of_le₀` (cast of `hd j`, `positivity` for `0 ≤ r j`), then `.trans_eq (by simp)` to rewrite `∑ j, 1 = card σ`. Zero parameters `r j = 0` are harmless: `hd` forces `d j = 0`, and `0 / 0 = 0 ≤ 1`.
- **Hypotheses**: `hd : ∀ j, d j ≤ r j` (membership in `box r`, stated unbundled); section variable `[Fintype σ]`.
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:227 (`index_le_card`, `exact hdw ▸ weight_le_card fun j ↦ ...`). Also listed in the Box.lean module docstring (Main results, line 32).
- **Visibility**: public
- **Lines**: 100–106, proof length 2 lines
- **Notes**: Docstring cites clean.tex §5 l.667 ("Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, of weight at most `m`").

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Index.lean:227, `index_le_card`).
- Wrapper of 1–2 mathlib calls? Yes: `Finset.sum_le_sum`/`Finset.sum_le_card_nsmul` + `div_le_one_of_le₀`.
- Does mathlib have it? Not for `Roth.weight`; re-aimed at `Finsupp.weight` there is no upper-bound lemma (loogle `Finsupp.weight _ _ ≤ _` returns only `finite_of_nat_weight_le` and `MvPolynomial.le_weightedTotalDegree`), but the general form is one call to `Finset.sum_le_card_nsmul` (evidence).
- Too specific (inline)? Single call site; inlining would replace `weight_le_card h` with a two-lemma term plus an unfold of `weight` at Index.lean:227. Keeping it is marginally cleaner and matches the paper's "weight at most m" remark and the module docstring's Main results list.
- Well-chosen? Yes; a natural box-companion of `weight` (hypothesis could alternatively be `d ∈ box r`, but the unbundled form is what the caller supplies).
- Conclusion: `KEEP` — action: keep in Roth/Box.lean; no change needed.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_le_card` not in mathlib (no `namespace Roth` in Mathlib). Not a glue lemma (a real inequality). Parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`, so per the re-aim rule this run is re-aimed at `Finsupp.weight`: target statement `Finsupp.weight w d ≤ Fintype.card σ • c` under `∀ i, d i • w i ≤ c`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight_le_card`: resolved at Roth/Box.lean:103
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_le_card` is a theorem stating the following: for a finite set of variables `σ` with `m = |σ|`, parameters `r ∈ ℕ^σ`, and a multi-index `d ∈ ℕ^σ` with `0 ≤ d_j ≤ r_j` for all `j`, the weight `∑_j d_j / r_j` is at most `m`. Re-aimed: for a weight vector `w : σ → M` in an ordered additive monoid and `d` with every term `d_i w_i ≤ c`, the weighted degree `⟨w, d⟩` is at most `|σ| · c`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set; `Fintype.card σ` is `m`.
- `r : σ → ℕ` — parameters `r_j` (with `x / 0 = 0`).
- `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- `hd : ∀ j, d j ≤ r j` — `d` lies in the box `box r`.

Conclusion (math): `∑_j d_j / r_j ≤ m`.

Conclusion (Lean): `Roth.weight r d ≤ ↑(Fintype.card σ)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary termwise bound (each term `≤ 1`, summed over `m` terms); a helper for `index_le_card`, not a main result of the project (though listed in Box.lean's Main results).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of polynomial at most m number of variables degree r_j weight sum i_j/r_j | partial | index = min of `∑ j_i/r_i` over nonzero Taylor coefficients; bound `≤ m` implicit | arXiv math/0307203 (Roth–Ridout), arXiv 1806.10737, Evertse notes; bound used, not stated as a lemma |
| 2 | WebSearch (general form) | weighted degree of monomial bounded by number of variables when exponent at most degree in each variable | no | `∑ w_i e_i ≤ d ∑ w_i` (termwise) | no named source; immediate termwise estimate |
| 3 | WebSearch (named-after / aliases) | "index" polynomial Roth theorem "0 ≤ ind" "≤ m" Schmidt Diophantine approximation lecture notes | partial | Schmidt LNM 785 index argument; Klazar NDMI045 lecture notes | `0 ≤ ind ≤ m` is a one-line remark in all expositions |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "weight at most" | yes | l.667: Taylor's theorem gives a nonzero derivative with `0 ≤ i_j ≤ r_j`, "of weight at most `m`" | project paper §5; one-line remark, no proof |
| 6 | nLab | weighted degree / graded ring | partial | gradings by weights | no lemma-level content on bounds |
| 7 | nCatLab | — | n/a | — | not a categorical concept (elementary finite-sum inequality) |
| 8 | Stacks Project | weighted polynomial rings | n/a | — | not an algebraic-geometry statement; checked graded-ring sections, nothing on box bounds |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | immediate fact; no discussion found |
| 10 | recent arXiv (last 5 years) | (arXiv 2111.12409, 1806.10737 from #1) | partial | index bounds in function-field / generalised Roth | bound `≤ m` used implicitly |

### Literature summary (Phase 3)

Concept identified as: upper bound on the weighted degree (Roth's index weight) of a multi-index in a box.
Sources agree on the standard form: yes (always an immediate one-line remark, never a named result).
Most general standard form: `∑_i d_i w_i ≤ |σ| · c` whenever every term `d_i w_i ≤ c` (equivalently the trivial bound "a sum of `m` terms each `≤ c` is `≤ m c`").
Generality dimensions where the literature varies:
  - weights: `1/r_j` (Roth) vs arbitrary nonnegative weights; the termwise-bounded form needs no sign condition.
  - bound per term: `1` (box `d ≤ r`) vs arbitrary `c`.
Disagreement with the literature: none.

### Generality analysis — `Roth.weight_le_card`

Literature-standard form (from Phase 3): `Finsupp.weight w d ≤ Fintype.card σ • c` under `∀ i, d i • w i ≤ c`, `M` an ordered additive commutative monoid.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector / codomain | `1/r j` in ℝ | any `w : σ → M`, `M` ordered add. monoid | yes (re-aimed) | evidence `finsupp_weight_le_card_nsmul` compiles |
| 2 | `hd : ∀ j, d j ≤ r j` | box membership | termwise `d i • w i ≤ c` | yes (re-aimed) | box membership is exactly `d j / r j ≤ 1`, i.e. `c = 1` |
| 3 | `hd` dropped entirely | — | — | NO | evidence counterexample (3): `σ = Unit`, `r = 1`, `d = single () 2` gives weight `2 > 1` |
| 4 | `[Fintype σ]` | required | required | no | the bound mentions `card σ` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general re-aimed form is a one-call mathlib composition (`Finsupp.weight_eq_sum` + `Finset.sum_le_card_nsmul`), verified in the evidence file; routed to NO-composable-from-mathlib, not generalise-first.
Number of weakening opportunities found: 2 (rows 1–2), verified for the re-aimed statement; the project hypothesis `hd` itself is necessary (row 3, verified).
Proposed restatement (re-aimed, optional): `theorem Finsupp.weight_le_card_nsmul (w : σ → M) (d : σ →₀ ℕ) (c : M) (h : ∀ i, d i • w i ≤ c) : weight w d ≤ Fintype.card σ • c := by rw [weight_eq_sum]; exact Finset.sum_le_card_nsmul _ _ c fun i _ ↦ h i`.
Cost of restatement: CHEAP (verified).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single box hypothesis |
| 2 | sequences to filters? | no | — | finite sum inequality |
| 3 | construction vs universal property? | no | — | inequality |
| 4 | bundled substructure? | marginal | hypothesis as `d ∈ box r` or `d ≤ equivFunOnFinite.symm r` | none material; caller supplies the unbundled form |
| 5 | field-specific to semiring? | yes | ordered additive monoid codomain (re-aimed) | matches `Finsupp/Weight.lean` context |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `ℝ`, `1/r j`, bound `1` to `M`, `w`, `c` | as #5 |
| 8 | concrete-via-abstract? | no | proof uses only termwise bound; nothing beyond the re-aimed form to extract | — |
| 9 | false-generalisation guard | no false generalisation | re-aimed form specialises back (evidence (2) is the `c = 1` instance on the explicit sum) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.weight w d ≤ Fintype.card σ • c` under termwise bound.
  - Cost: CHEAP
  - Mathlib downstream this enables: nothing beyond naming a single `Finset.sum_le_card_nsmul` application.
  - Real mathematical improvement: no; it is a one-call specialisation of `Finset.sum_le_card_nsmul`.

### Proof strategy — `Roth.weight_le_card`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `Finset.sum_le_card_nsmul` + `div_le_one_of_le₀` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(`Finset.sum_le_sum ... |>.trans_eq (by simp)` is equivalent to `Finset.sum_le_card_nsmul`; either is fine.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_le_card`

[A] Lean-Finder       "upper bound for Finsupp.weight of a multi-index bounded coordinatewise"   hits: `Finsupp.le_weight`, `le_weight_of_ne_zero(')`, `finite_of_nat_weight_le`, `MvPolynomial.le_weightedTotalDegree` — only lower bounds / finiteness
[B] Loogle            `Finsupp.weight _ _ ≤ _`   hits: `Finsupp.finite_of_nat_weight_le`, `MvPolynomial.le_weightedTotalDegree` — no termwise upper bound
[C] LeanSearch        "weight of a finsupp bounded by card times bound when each term is bounded"   hits: `Finset.sum_le_card_nsmul`, `Multiset.sum_le_card_nsmul`, `Finsupp.le_degree` (building blocks)
[D] Grep mathlib src  theorem list of Mathlib/Data/Finsupp/Weight.lean; `sum_le_card_nsmul` in Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:285   no `weight_le_*` upper bound; building block present
[E] Name pattern      `Finsupp.weight_le`, `Finsupp.weight_le_card`   absent (lean_local_search unavailable: ripgrep not on PATH; checked by grep of Weight.lean instead)

Searched for both the user's form (`∑ d j / r j ≤ card σ`) and the re-aimed literature-standard form (`Finsupp.weight w d ≤ card σ • c`).

Concluded: found building blocks (`Finsupp.weight_eq_sum`, `Finset.sum_le_card_nsmul`, `div_le_one_of_le₀`); composition would yield our form.

### Normal-form check — `Roth.weight_le_card`

Equivalent formalisms: `weight r d ≤ card σ` under `∀ j, d j ≤ r j`; same under `d ∈ box r`; `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d ≤ card σ`.
Does mathlib already have a canonical form for this idea? The canonical object is `Finsupp.weight`; no upper-bound lemma exists.
Is our statement stated against the canonical form? Against the project def `Roth.weight` (parent refactor target); shape `_ ≤ _` is standard.
RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.weight_le_card`

Alternative restatements attempted:
- hypothesis `d ∈ box r` (caller would need `mem_box.2`)
- re-aimed `Finsupp.weight w d ≤ card σ • c` (compiles; evidence)
Chosen restatement: as stated (unbundled `∀ j, d j ≤ r j`, implicit `r d`).
Justification: the only caller (Index.lean:227) builds exactly `fun j ↦ ...` bounds.

### Superfluous-argument audit — `Roth.weight_le_card`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed for `weight` and `card σ` |
| 2 | `hd` | yes | counterexample in evidence (3) |
| 3 | `[DecidableEq σ]` | not present | omitted by `omit` earlier in the file |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_le_card`

Internal use count: 1 (outside Roth/Box.lean)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:227 | `exact hdw ▸ weight_le_card fun j ↦ (monomial_le_degreeOf j ...).trans ((degreeOf_taylor_le α j P).trans (hd j))` (`index_le_card`) |

Inline-derivation grep:
  - (none) — no other re-derivation of the box weight bound in Roth/ (other `sum_le_card_nsmul` uses at MainLemma.lean:718, CoeffNorm.lean:115/177 bound unrelated sums).

### Composition check (Phase 6)

Can `Roth.weight_le_card` be derived from mathlib in ≤3 chained calls?

Attempt 1 (project form): `by simpa [Roth.weight] using Finset.sum_le_card_nsmul Finset.univ (fun j ↦ (d j : ℝ) / r j) 1 fun j _ ↦ div_le_one_of_le₀ (by exact_mod_cast hd j) (by positivity)`
  - Mathlib decls used: `Finset.sum_le_card_nsmul`, `div_le_one_of_le₀`
  - Result: succeeds (evidence example (2))

Attempt 2 (re-aimed form): `rw [weight_eq_sum]; exact Finset.sum_le_card_nsmul _ _ c fun i _ ↦ h i`
  - Mathlib decls used: `Finsupp.weight_eq_sum`, `Finset.sum_le_card_nsmul`
  - Result: succeeds (evidence `finsupp_weight_le_card_nsmul`)

Conclusion: COMPOSABLE

## Verdict: `Roth.weight_le_card`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the bound "weight at most `m`" on the box is a one-line remark everywhere (clean.tex l.667, Schmidt/Ridout expositions), never a named result.
- Generality analysis (Phase 4): STRICTLY NARROWER, but the general re-aimed form is a one-call composition (verified); `hd` itself is necessary (verified counterexample).
- Mathlib search (Phase 5): no upper-bound lemma for `Finsupp.weight`; building blocks `Finset.sum_le_card_nsmul`, `Finsupp.weight_eq_sum`, `div_le_one_of_le₀`.
- Composition check (Phase 6): COMPOSABLE (one call + one termwise lemma, both forms).

**Rationale:**

Re-aimed at `Finsupp.weight` (parent `Roth.weight` is `NO-mathlib-has-it`), the analogue `Finsupp.weight w d ≤ Fintype.card σ • c` under a termwise bound is not in mathlib, but it is literally `Finset.sum_le_card_nsmul` after `Finsupp.weight_eq_sum` — a restatement of a general big-operators lemma, not new API worth a PR. The project form adds only `div_le_one_of_le₀` for the termwise bound `d j / r j ≤ 1`.

WHY not: the content is "a sum of `m` terms each at most `1` is at most `m`", which mathlib has as `Finset.sum_le_card_nsmul`. Belongs-elsewhere check: keep project-local in Roth/Box.lean; it names the paper's "weight at most `m`" remark and is listed in the module's Main results, and its single caller reads better with the name.

Mathlib building blocks:      `Finset.sum_le_card_nsmul` (Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:285), `div_le_one_of_le₀` (Mathlib/Algebra/Order/GroupWithZero/Basic.lean:1190), `Finsupp.weight_eq_sum` (Mathlib/Data/Finsupp/Weight.lean:100)
Composition sketch (≤3 lines):
```lean
example {r : σ → ℕ} {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) : Roth.weight r d ≤ Fintype.card σ := by
  simpa [Roth.weight] using Finset.sum_le_card_nsmul Finset.univ (fun j ↦ (d j : ℝ) / r j) 1
    fun j _ ↦ div_le_one_of_le₀ (by exact_mod_cast hd j) (by positivity)
```
Call sites in our project (from Phase 6.0):  1 (Roth/Index.lean:227)
Refactor plan: no inlining recommended (Step 8 KEEP): at Index.lean:227 the lemma is used as `hdw ▸ weight_le_card (fun j ↦ ...)`; inlining would require unfolding `weight` there. If `Roth.weight` is redefined via `Finsupp.weight` (parent report), reprove as `by rw [weight_eq_sum ...]; exact Finset.sum_le_card_nsmul _ _ 1 fun j _ ↦ ...` (the caller is unchanged).
Next action: keep `Roth.weight_le_card` locally; no mathlib PR.

---

## Next step

No mathlib action. Keep the lemma in Roth/Box.lean; optionally rewrite its proof via `Finset.sum_le_card_nsmul`; reprove via `Finsupp.weight_eq_sum` only if the parent `Roth.weight` refactor is carried out.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_le_card/weight_le_card_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics after fixing a `Module ℕ M` instance clash, an unfolding `simpa`, and a redundant `norm_num`): (1) `finsupp_weight_le_card_nsmul` — re-aimed general form; (2) project lemma via `Finset.sum_le_card_nsmul` + `div_le_one_of_le₀`; (3) counterexample showing `hd` cannot be dropped; (4) current lemma applies.
- Loogle `Finsupp.weight _ _ ≤ _`; LeanSearch and Lean-Finder queries as in the search-status block; `lean_local_search` unavailable (ripgrep not installed), replaced by grep of Mathlib/Data/Finsupp/Weight.lean.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.667).
- Project grep `grep -rn weight_le_card Roth/` for the call-sites table.
