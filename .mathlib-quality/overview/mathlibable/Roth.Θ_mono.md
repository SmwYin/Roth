---
decl: Roth.Θ_mono
file: Roth/Theta.lean
line: 134
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Monotonicity in B of the project-local supremum Θ, which is one csSup_le_csSup call on the inclusion indexSet B ⊆ indexSet B' (compiled); the quantity is specific to the Roth proof, so nothing goes upstream, and the hypothesis 1 ≤ B is superfluous (a weakened version without it compiles).
action: Do not upstream; keep in Roth/Theta.lean, optionally drop hB (proof in evidence Θ_mono') and remove the hM1 argument at the two call sites Theta.lean:758 and Theta.lean:790.
---

# Roth.Θ_mono

## Inventory entry

### `theorem Roth.Θ_mono`
- **Type**: `∀ {σ : Type*} [Fintype σ] {B B' : ℝ}, 1 ≤ B → B ≤ B' → ∀ (q : σ → ℕ) {r : σ → ℕ}, Θ B q r ≤ Θ B' q r`
- **What**: If `1 ≤ B ≤ B'`, then `Θ_m(B; q; r) ≤ Θ_m(B'; q; r)`. Raising the coefficient bound enlarges `ℛ_m(B; r)`, which enlarges the set of indices, so it cannot decrease their supremum.
- **How**: The proof is `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) ?_`. The inclusion `indexSet B q r ⊆ indexSet B' q r` is proved by destructuring a membership witness and weakening the coefficient bound with `(hRc d).trans hBB'`.
- **Hypotheses**: `hB : 1 ≤ B` is used only to make `indexSet B q r` nonempty. It is superfluous for the conclusion; see the evidence. `hBB' : B ≤ B'` carries the content. The section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet`, `Roth.index`, `Roth.indexSet_bddAbove`, `Roth.indexSet_nonempty`
- **Used by**: Roth/Theta.lean:758 (in the private lemma that bounds Θ in one variable during the proof of Lemma 7) and Roth/Theta.lean:790 (`theta_prefix_lt_aux`, Lemma 7). Found with `grep -rn Θ_mono Roth/`. Theta.lean:34 is a docstring mention. There are no uses outside Theta.lean.
- **Visibility**: public
- **Lines**: 131–138 (docstring 132–133, statement 134–135, proof 136–138), proof length 3 lines
- **Notes**: Source: clean.tex l.668 ("Θ_m is nondecreasing in B, since increasing B enlarges the set of allowed polynomials"). The source states it with no hypothesis `B ≥ 1`.

## Junk check (Step 8)
- **Used anywhere?** Yes, twice in Lemma 7's machinery (Theta.lean:758 and Theta.lean:790).
- **Wrapper of 1–2 mathlib calls?** Yes. It is one `csSup_le_csSup` call plus the project's `indexSet_bddAbove` and `indexSet_nonempty`, with a three-line inclusion. Inlining it would expose the existential shape of `indexSet` at both callers. It is the named monotonicity API of `Θ` and is stated in the paper.
- **Does mathlib have it?** No. It concerns the project's `Θ`. The generic content is `csSup_le_csSup`.
- **Too specific (inline?)?** No. It is part of the basic `Θ` API, alongside `Θ_nonneg`, `Θ_le_card` and `Θ_equiv`.
- **Well-chosen?** Mostly. `hB : 1 ≤ B` is superfluous. `Θ_mono'` in the evidence file proves the statement without it, by splitting on whether `indexSet B q r` is empty (if it is, `Θ B q r = 0 ≤ Θ B' q r` by `Θ_nonneg`). Dropping it would match the source and allow a `Monotone` form.
- **Conclusion:** `KEEP`. An optional polish is to drop `hB` and update the two callers (they pass `hM1`).

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib: there is no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`.

This is not a glue lemma. The body applies `csSup_le_csSup` and proves a set inclusion; it is not `rfl` or pure unfolding. A full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors or warnings)
- decl `Roth.Θ_mono`:        resolved at Roth/Theta.lean:134
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.Θ_mono` is a theorem stating the following.

Let `1 ≤ B ≤ B'`. Then `Θ_m(B; q; r) ≤ Θ_m(B'; q; r)`, where `Θ_m(B; q; r)` is the supremum of `ind(R; (h_j/q_j)_j; r)` over nonzero `R ∈ ℤ[X_j : j ∈ σ]` with `deg_{X_j} R ≤ r_j` and coefficients bounded by `B`, and over `h` with `gcd(h_j, q_j) = 1`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables.
- `B`, `B'`: the coefficient bounds.
- `q`: the denominators.
- `r`: the degree bounds and index weights.

Hypotheses (Lean side):
- `hB : 1 ≤ B`: ensures the smaller index set is nonempty.
- `hBB' : B ≤ B'`: the comparison of the bounds.

Conclusion (math): `Θ` is nondecreasing in `B`.

Conclusion (Lean): `Θ B q r ≤ Θ B' q r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a monotonicity API lemma for a project-local supremum, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem); recorded that the proof is `csSup_le_csSup` plus an inclusion.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem Ridout Theta_m(B; q; r) nondecreasing in B supremum index polynomials bounded coefficients | partial | Yamada (arXiv math/0307203) defines Θ_m as a supremum of indices over polynomials with bounded coefficients | monotonicity in B is tacit, not a named lemma |
| 2 | WebSearch (general form) | supremum monotone under set inclusion csSup_le_csSup conditionally complete lattice subset bounded above nonempty | yes | `s ⊆ t`, `s` nonempty and `t` bounded above give `sup s ≤ sup t` | the entire mathematical content (mathlib `csSup_le_csSup`) |
| 3 | WebSearch (named-after / aliases) | Cassels Diophantine approximation Roth lemma index of polynomial rational point Theta monotone in height bound | partial | Yamada math/0307203 (Lemma 2.1, the bound `Θ_m < 10^m δ^{(1/2)^m}`); Evertse arXiv 2502.00731; Cassels 1965 catalogue entry | monotonicity follows from the definition; no stated lemma found |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "nondecreasing in" | yes | clean.tex l.668: "Θ_m is nondecreasing in B, since increasing B enlarges the set of allowed polynomials" | the source has no `B ≥ 1` hypothesis here |
| 6 | nLab | supremum (least upper bound) | partial | generic order theory: the supremum is monotone under inclusion | nothing Roth-specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an inequality between reals) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; Stacks has no index-of-a-polynomial notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary for a thread |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025) and 2601.11376, from searches 1 and 3 | partial | Roth/Ridout set-up and quantitative constants | no Θ-monotonicity lemma |

### Literature summary (Phase 3)

Concept identified as: monotonicity of the supremum `Θ_m(B; q; r)` in the height bound `B`, from the Ridout/Cassels presentation of Roth's lemma.
Sources agree on the standard form: yes. It is tacit, following from the definition.
Most general standard form: if `s ⊆ t`, `t` is bounded above and `s` is nonempty, then `sup s ≤ sup t` (`csSup_le_csSup`). In `ℝ` with `sSup ∅ = 0` and nonnegative elements, the nonemptiness hypothesis is not needed.
Generality dimensions where the literature varies: none. The source states the fact for all `B`.
Disagreement with the literature: the Lean form adds `1 ≤ B`, which the source does not have. It is removable (evidence (2)).

### Generality analysis — `Roth.Θ_mono`

Literature-standard form: `B ≤ B' → Θ B q r ≤ Θ B' q r` with no lower bound on `B`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hB : 1 ≤ B` | required | absent | YES (verified) | If `indexSet B q r = ∅` then `Θ B q r = sSup ∅ = 0 ≤ Θ B' q r` by `Θ_nonneg`. `Θ_mono'` in the evidence file compiles without it. |
| 2 | `hBB' : B ≤ B'` | required | required | NO | this is the content |
| 3 | `[DecidableEq σ]` | omitted | n/a | already absent | `#check` in the evidence file |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (project-locally). `hB` is droppable, and this was verified: `Θ_mono'` compiles. The weakening concerns a project-local lemma about a project-local quantity, so it does not create a mathlib candidate.
Number of weakening opportunities found: 1
Proposed restatement: `theorem Θ_mono {B B' : ℝ} (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Θ B' q r`, or equivalently `Monotone fun B ↦ Θ B q r` (evidence (4)).
Cost of restatement: CHEAP (a 4-line proof, plus deleting the `hM1` argument at the 2 callers)

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | the hypotheses are data-specific | — |
| 2 | Sequences vs filters? | no | an order inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Bundled substructure? | no | `indexSet` is a plain set of reals | — |
| 5 | Field-specific vs typeclass-weakened? | no | ℝ-valued by the definition of `index` | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | arbitrary finite `σ` already | — |
| 8 | Concrete-via-abstract? | yes, trivially | after destructuring, the proof is pure `csSup_le_csSup`; the abstract form already exists in mathlib | none |
| 9 | False-generalisation guard | no false generalisation | dropping `hB` keeps the same object, `Θ` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the abstract content is exactly mathlib's `csSup_le_csSup`. Stating the result as `Monotone (Θ · q r)` is a project-local cosmetic option, not a mathlib contribution.

### Proof strategy — `Roth.Θ_mono`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | no | `csSup_le_csSup` covers it | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`csSup_le_csSup` with an inclusion; it can also be written as a single term, evidence (1)).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_mono`

[A] Lean-Finder       "supremum of a subset of reals is at most supremum of a bounded superset"   hits: `csSup_le_csSup'`, `csSup_le_csSup`, `Real.sSup_le`, `ciSup_mono'` (building blocks)
[B] Loogle            `?s ⊆ ?t → sSup ?s ≤ sSup ?t`   hits: `sSup_le_sSup`, `DirectedOn.csSup_le_csSup`, `csSup_le_csSup`, `csSup_le_csSup'` (the last needs `ConditionallyCompleteLinearOrderBot`, which ℝ is not)
[C] LeanSearch        "supremum of indices of integer polynomials with bounded coefficients is monotone in the coefficient bound"   hits: `partialSups_mono`, `Polynomial.degreeLE_mono` (unrelated)
[D] Grep mathlib src  `namespace Roth` (no hits); `theorem csSup_le_csSup` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:209)
[E] Name pattern      `csSup_le_csSup`, `csSup_le_csSup'` (mathlib); `Θ_mono` (project only)

Searched for both:
  - the user's form (Θ monotone in B)
  - the literature-standard form (the supremum is monotone under inclusion): this is `csSup_le_csSup`

Concluded: found building blocks (`csSup_le_csSup`, plus the project's `indexSet_bddAbove` and `indexSet_nonempty`); composition gives our form.

### Normal-form check — `Roth.Θ_mono`

Equivalent formalisms:
- pointwise `B ≤ B' → Θ B q r ≤ Θ B' q r` (current, with an extra `1 ≤ B`)
- `Monotone fun B ↦ Θ B q r`

Does mathlib already have a canonical form? For monotonicity of a function, mathlib usually states `Monotone f` together with a pointwise `_mono` lemma. Either form fits.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.Θ_mono`

Alternative restatements attempted:
- current pointwise form with `hB`
- pointwise form without `hB` (evidence (2))
- `Monotone` form (evidence (4))

Chosen restatement: the pointwise form without `hB`.
Justification: callers use `(Θ_mono hM1 hM _).trans`. Without `hB` they write `(Θ_mono hM _).trans`, which is strictly easier to supply.

### Superfluous-argument audit — `Roth.Θ_mono`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hB : 1 ≤ B` | no | the conclusion holds without it (evidence (2)) |
| 2 | `hBB'` | yes | content |
| 3 | `[Fintype σ]` | yes | needed by `index`, `Θ` and the bounded-above lemma |
| 4 | `[DecidableEq σ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (drop `hB`)
Superfluous arguments: 1 to drop (`hB`)

Overall: RESTATE-BEFORE-SHIP. This is a project-local polish, since nothing is shipped upstream.

### Call sites — `Roth.Θ_mono`

Internal use count: 0 outside the declaring file, 2 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:758 | `refine (Θ_mono hM1 hM _).trans ((Θ_unique_le ...` (one-variable case in the proof of Lemma 7) |
| Roth/Theta.lean:790 | `refine (Θ_mono hM1 hM _).trans_lt ?_` (`theta_prefix_lt_aux`, Lemma 7) |

Inline-derivation grep:
  - (none). `grep -rn csSup_le_csSup Roth/` finds only Theta.lean:136, the lemma itself.

### Composition check (Phase 6)

Can `Roth.Θ_mono` be derived from mathlib in ≤3 chained calls?

Attempt 1: `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) fun _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, hx⟩ ↦ ⟨R, ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩, h, hh, hx⟩`
  - Decls used: mathlib `csSup_le_csSup`; project `Roth.indexSet_bddAbove` and `Roth.indexSet_nonempty`; anonymous-constructor destructuring.
  - Result: succeeds (evidence (1)).
  - Notes: one mathlib call.

Attempt 2 (without `hB`): split on `Set.eq_empty_or_nonempty`, then use `Real.sSup_empty` with `Θ_nonneg`, or `csSup_le_csSup`.
  - Result: succeeds (evidence (2)).

Conclusion: COMPOSABLE

## Verdict: `Roth.Θ_mono`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** the fact is tacit: "Θ_m is nondecreasing in B, since increasing B enlarges the set of allowed polynomials" (clean.tex l.668). The general content is that the supremum is monotone under inclusion.
- **Generality analysis (Phase 4):** STRICTLY NARROWER project-locally, since `hB` can be dropped (verified, evidence (2)). This creates no mathlib candidate.
- **Mathlib search (Phase 5):** building block `csSup_le_csSup` (Loogle and Lean-Finder hits). There is no `Roth` namespace in mathlib.
- **Composition check (Phase 6):** COMPOSABLE as one `csSup_le_csSup` call (evidence (1)).

**Rationale:**

`Roth.Θ_mono` is mathlib's `csSup_le_csSup` applied to the inclusion `indexSet B q r ⊆ indexSet B' q r`, which holds because a polynomial with coefficients bounded by `B` also has them bounded by `B'`. The quantities `Θ`, `indexSet` and `RSet` are bookkeeping objects of the Ridout/Cassels proof of Roth's lemma, all NO-composable-from-mathlib. The only general mathematics here is that the supremum is monotone under inclusion, which mathlib already has. There is nothing to upstream.

The "generalise" finding (drop `1 ≤ B`) is real but concerns a project-local lemma, so it does not move the verdict into a YES bucket. It is recorded as a local polish.

WHY not: it is a single mathlib call (`csSup_le_csSup`) about a Roth-proof-specific supremum that will never be in mathlib.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean as the monotonicity API of `Θ`, which the paper states explicitly. The bucket's usual "inline at call sites" step is not recommended. Inlining would repeat the inclusion destructuring at both callers and tie them to the shape of `indexSet`.

Mathlib building blocks:
- `csSup_le_csSup` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:209)
- `Real.sSup_empty` (for the `hB`-free variant)
- project `Roth.indexSet_bddAbove`, `Roth.indexSet_nonempty`, `Roth.Θ_nonneg` (Roth/Theta.lean)

Composition sketch (≤3 lines):
```lean
example (hB : 1 ≤ B) (hBB' : B ≤ B') : Θ B q r ≤ Θ B' q r :=
  csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r)
    fun _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, hx⟩ ↦ ⟨R, ⟨hR0, hRd, fun d ↦ (hRc d).trans hBB'⟩, h, hh, hx⟩
```

Call sites in our project (from Phase 6.0): 2, at Roth/Theta.lean:758 and Roth/Theta.lean:790.

Refactor plan: no inlining. Optionally replace the statement with the `hB`-free `Θ_mono'` from the evidence file, and change both call sites from `Θ_mono hM1 hM _` to `Θ_mono hM _`. `hM1` is still used elsewhere at both sites, so no unused-variable fallout is expected; check with `lake build`.

Next action: no upstreaming; optionally drop `hB` locally.

## Next step

No upstreaming. Keep `Roth.Θ_mono` in Roth/Theta.lean. An optional polish is to drop the superfluous `hB : 1 ≤ B` (proof in evidence `Θ_mono'`, which matches the source's unconditional statement in clean.tex l.668) and update Theta.lean:758 and Theta.lean:790.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ_mono/composition.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports success with no errors or warnings, only the `#check` info. It contains:
  - (1) a one-term `csSup_le_csSup` composition of the original statement;
  - (2) `Θ_mono'`, the statement without `hB`, proved by splitting on `Set.eq_empty_or_nonempty` with `Real.sSup_empty`, `Θ_nonneg` and `csSup_le_csSup`;
  - (3) the original statement recovered from `Θ_mono'`;
  - (4) the `Monotone fun B ↦ Θ B q r` form;
  - (5) `#check @Θ_mono`, confirming the signature uses only `[Fintype σ]`.
  The first check flagged a header-linter warning (no module docstring). A docstring was added and the re-check is clean.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, arXiv 2601.11376, Cassels catalogue entry, and mathlib doc mirrors for ConditionallyCompleteLattice.
- Lean-Finder, Loogle and LeanSearch queries as recorded in Phase 5. A grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth` and located `csSup_le_csSup` at Basic.lean:209.
- Local refs: clean.tex l.660–669.
- `grep -rn Θ_mono Roth/` and `grep -rn csSup_le_csSup Roth/` for the call-sites table.
- Sibling reports Roth.Θ_le_of_forall_index_le.md and Roth.Θ.md were reused for format and the parent verdict.
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
