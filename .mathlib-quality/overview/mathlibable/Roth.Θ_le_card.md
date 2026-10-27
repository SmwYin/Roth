---
decl: Roth.Θ_le_card
file: Roth/Theta.lean
line: 114
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The upper bound Θ ≤ card σ for the project-local supremum Θ, proved as one call of mathlib's Real.sSup_le fed by the project's index_le_card (compiled); about a Roth-proof-specific quantity so nothing to upstream, but it is the paper-facing Θ_m ≤ m API lemma used at Theta.lean:939.
action: Do not upstream; keep in Roth/Theta.lean next to Θ_nonneg (caller theta_lt_of_large_delta_aux at Theta.lean:939); optionally remove the body duplicated with indexSet_bddAbove (Theta.lean:87) by factoring card_mem_upperBounds_indexSet as in evidence/Roth.indexSet_bddAbove/refactor.lean, making Θ_le_card the one-liner Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _).
---

# Roth.Θ_le_card

## Inventory entry

### `theorem Roth.Θ_le_card`
- **Type**: `∀ {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, Θ B q r ≤ ↑(Fintype.card σ)`
- **What**: For every coefficient bound `B`, denominators `q` and weights `r`, the quantity `Θ_m(B; q; r)` is at most the number `m = card σ` of variables. This is the upper half of the paper's `0 ≤ Θ_m ≤ m`.
- **How**: `refine Real.sSup_le ?_ (Nat.cast_nonneg _)`, then destructure membership in `indexSet` (`rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩`) and close with the project's `index_le_card`, transporting `R ≠ 0` along the injective cast `ℤ → ℝ` (`map_ne_zero_iff`, `map_injective`, `Int.cast_injective`) and the degree bound with `degrees_map_of_injective`. Mathlib's `Real.sSup_le` needs only a member-wise bound and `0 ≤ card σ` (because `sSup ∅ = 0` in `ℝ`), so no `1 ≤ B` and no nonemptiness lemma is required.
- **Hypotheses**: none (beyond `[Fintype σ]`). No `1 ≤ B`, no positivity of `r`; the section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet` (membership pattern), `Roth.index`, `Roth.index_le_card`
- **Used by**: Roth/Theta.lean:939 (`simpa using Θ_le_card (r := r) q`, inside private `theta_lt_of_large_delta_aux`, the large-δ case of Lemma 7); also named in the module docstring at Roth/Theta.lean:33. Found with `grep -rn Θ_le_card Roth/`; no other file uses it.
- **Visibility**: public
- **Lines**: 112–118 (docstring 113, statement 114, proof 115–118), proof length 4 lines
- **Notes**: Source: clean.tex §5 l.665–667 ("`0 ≤ Θ_m ≤ m` ... Taylor's theorem gives a nonzero derivative ... of weight at most `m`"). The proof body (lines 116–118) is a verbatim duplicate of `indexSet_bddAbove`'s body (Theta.lean:89–93), as already recorded in Roth.indexSet_bddAbove.md; factoring the shared fact `card σ ∈ upperBounds (indexSet B q r)` would make both one-liners (compiled in evidence/Roth.indexSet_bddAbove/refactor.lean). `q` explicit while `B`, `r` implicit, matching `Θ_nonneg`; cosmetic.

## Junk check (Step 8)
- **Used anywhere?** Yes, at Roth/Theta.lean:939.
- **Wrapper of 1–2 mathlib calls?** It is `Real.sSup_le` plus the project lemma `index_le_card` and a cast-transport step. Inlining would expose `indexSet`'s existential shape and the `ℤ → ℝ` transport at the caller.
- **Does mathlib have it?** No; it concerns the project's `Θ`. The generic content is `Real.sSup_le`.
- **Too specific (inline?)?** No. It is the paper-facing `Θ_m ≤ m`, paired with `Θ_nonneg`.
- **Well-chosen?** Yes, hypothesis-free; the only wart is the body duplicated with `indexSet_bddAbove`.
- **Conclusion:** `KEEP`. Optional: deduplicate the body with `indexSet_bddAbove` via a shared `card_mem_upperBounds_indexSet`.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib: `grep -rn "namespace Roth" .lake/packages/mathlib/Mathlib/` has no hits.

This is not a glue lemma: the body applies `Real.sSup_le` and `index_le_card` with a cast transport (a real, if short, proof), not `rfl`/`Iff.rfl`/unfolding. A full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors)
- decl `Roth.Θ_le_card`:     resolved at Roth/Theta.lean:114
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.Θ_le_card` is a theorem stating the following.

Let `Θ_m(B; q; r)` be the supremum of the indices `ind(R; (h_j/q_j)_j; r)` over nonzero `R ∈ ℤ[X_j : j ∈ σ]` with `deg_{X_j} R ≤ r_j` and coefficients of absolute value at most `B`, and over `h ∈ ℤ^σ` with `gcd(h_j, q_j) = 1`. Then `Θ_m(B; q; r) ≤ m`, where `m = |σ|`. (In Lean the supremum of an empty family is `0`, so the statement holds for all `B`, `q`, `r`.)

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables; `m = Fintype.card σ`.
- `B`: the coefficient bound (implicit).
- `q`: the denominators (explicit).
- `r`: the degree bounds and index weights (implicit).

Hypotheses (Lean side):
- none.

Conclusion (math): `Θ_m(B; q; r) ≤ m`.

Conclusion (Lean): `Θ B q r ≤ ↑(Fintype.card σ)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic bound on a project-local supremum; an API lemma, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem); the proof is `Real.sSup_le` plus membership destructuring and `index_le_card` (evidence (1)).

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma Theta_m supremum index polynomial "Θ_m ≤ m" Ridout Cassels index at most m | partial | Yamada (arXiv math/0307203) defines `Θ_m` as this supremum and bounds it above via Roth's lemma; `Θ_m ≤ m` is not stated as a separate result | tacit in the literature |
| 2 | WebSearch (general form) | supremum least upper bound property sSup le of upper bound real numbers Real.sSup_le | yes | an upper bound of every member bounds the supremum; mathlib doc mirrors show `Real.sSup_nonpos`, `Real.isLUB_sSup`, `Real.sSup_def` (`sSup` = 0 off nonempty bounded sets) | the entire supremum-level content |
| 3 | WebSearch (named-after / aliases) | index of a polynomial at a point Roth theorem index at most number of variables Taylor expansion nonzero derivative | partial | index = min of `Σ j_i/r_i` over nonzero Taylor coefficients (math/0307203; arXiv 2502.00731 Lemma 3.9 gives the sharp `≤ 2mη`); the trivial `≤ m` follows since `j_i ≤ r_i` | supplies the member-wise fact (`index_le_card`) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "0\leq\Theta_m\leq m" | yes | clean.tex l.665–667: "satisfies `0 ≤ Θ_m ≤ m`", the upper bound via Taylor's theorem giving a nonzero derivative of weight at most `m` | this lemma is the `≤ m` half |
| 6 | nLab | supremum | partial | generic least upper bound; sup below any upper bound | nothing Roth-specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an inequality of reals) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; no index-of-a-polynomial-at-a-point notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary for a thread |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), from searches 1 and 3 | partial | pointwise Roth's lemma `Ind ≤ 2mη` | no supremum `Θ_m`, so no analogue of this lemma |

### Literature summary (Phase 3)

Concept identified as: the trivial upper bound `Θ_m ≤ m` for the supremum `Θ_m(B; q; r)` in the Ridout/Cassels presentation of Roth's lemma.
Sources agree on the standard form: yes. It is tacit, immediate from each index being at most `m` (each `j_i/r_i ≤ 1`).
Most general standard form: a supremum of reals each `≤ a` (with `a ≥ 0` under the `sSup ∅ = 0` convention) is `≤ a` (`Real.sSup_le`).
Generality dimensions where the literature varies: whether nonemptiness (`B ≥ 1`) is assumed; the Lean form does not need it.
Disagreement with the literature: none; the Lean form is slightly stronger (no `B ≥ 1`, no `r_j ≥ 1`).

### Generality analysis — `Roth.Θ_le_card`

Literature-standard form: `(∀ x ∈ s, x ≤ a) → 0 ≤ a → sSup s ≤ a` with `a = m`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `1 ≤ B` | not taken | paper has `B ≥ 1` implicitly | already weaker | `Real.sSup_le` needs no nonemptiness; evidence (2) instantiates `B = -1` |
| 2 | positivity of `r` | not taken | paper has `r_j ≥ 1` | already weaker | `index_le_card` holds for all `r`; evidence (2) instantiates `r = 0` |
| 3 | `[DecidableEq σ]` | omitted | n/a | already absent | evidence (3) signature check |
| 4 | `[Fintype σ]` | required | finite `m` | NO | needed for `index`, `Θ` and `card σ` |
| 5 | bound `card σ` | `m` | `m` | NO | sharper bounds are Lemmas 5–7 (`Θ_unique_le`, `Θ_option_le`, `Θ_lt`), separate results |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. It has no hypotheses at all.
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | no hypotheses | — |
| 2 | Sequences vs filters? | no | an order inequality | — |
| 3 | Construction vs universal property? | no | already uses the least-upper-bound property via `Real.sSup_le` | — |
| 4 | Bundled substructure? | no | `indexSet` is a plain set of reals | — |
| 5 | Field-specific vs typeclass-weakened? | no | ℝ-valued by definition of `index`; the `sSup ∅ = 0` convention is ℝ-specific | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | arbitrary finite `σ` already | — |
| 8 | Concrete-via-abstract? | yes, trivially | after destructuring, the proof is `Real.sSup_le` + `index_le_card`; the abstract form already exists in mathlib | none (the abstraction is `Real.sSup_le`) |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the abstract content is exactly mathlib's `Real.sSup_le`; nothing remains to modernise.

### Proof strategy — `Roth.Θ_le_card`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | no (project-side only) | the shared fact `card σ ∈ upperBounds (indexSet B q r)` would remove the body duplicated with `indexSet_bddAbove` | CHEAP (project-local refactor) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`Real.sSup_le` + `index_le_card`). A project-local deduplication with `indexSet_bddAbove` is recommended but is not a mathlib API gap.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_le_card`

[A] Lean-Finder       "supremum of a set of reals bounded above by a nonnegative number is at most that number"   hits: `Real.sSup_le`, `Real.iSup_le`, `Real.sSup_nonpos`, `Real.iSup_nonpos`, `Real.sSup_nonneg'` (building blocks)
[B] Loogle            `(∀ x ∈ ?s, x ≤ ?a) → 0 ≤ ?a → sSup ?s ≤ ?a`   hits: `Real.sSup_le` (Mathlib.Algebra.Order.Archimedean.Real.Basic)
[C] LeanSearch        "supremum of indices of integer polynomials at rational points is at most number of variables"   hits: `iSup`, `MvPolynomial.totalDegree_le_degrees_card`, `MvPolynomial.schwartz_zippel_sup_sum` (unrelated)
[D] Grep mathlib src  `namespace Roth` (no hits); `sSup_le` in Mathlib/Algebra/Order/Archimedean/Real/Basic.lean (definition at l.222)
[E] Name pattern      `Real.sSup_le` (mathlib); `Θ_le_card`, `index_le_card` (project only)

Searched for both:
  - the user's form (`Θ B q r ≤ card σ`)
  - the literature-standard form (sup below a nonnegative upper bound): this is `Real.sSup_le`

Concluded: found building blocks (`Real.sSup_le`, plus the project's `index_le_card`); composition gives our form.

### Normal-form check — `Roth.Θ_le_card`

Equivalent formalisms:
- `Θ B q r ≤ card σ` (current)
- `card σ ∈ upperBounds (indexSet B q r)` combined with `Real.sSup_le` at the call site

Does mathlib already have a canonical form? Yes: `_ ≤ _` bound lemmas; our statement is in that form.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.Θ_le_card`

Alternative restatements attempted:
- hypothesis-free (current, evidence (1)–(2))
- via `csSup_le` with `1 ≤ B` (strictly weaker; not compiled as it is dominated)

Chosen restatement: hypothesis-free (current).
Justification: the caller at Theta.lean:939 supplies only `q` and `r`, no side conditions.

### Superfluous-argument audit — `Roth.Θ_le_card`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `index`, `Θ`, `card σ` |
| 2 | `[DecidableEq σ]` | no | already omitted |
| 3 | `q` explicit | n/a | could be implicit like `B`, `r`; cosmetic, consistent with `Θ_nonneg` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.Θ_le_card`

Internal use count: 0 outside the declaring file; 1 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:939 | `simpa using Θ_le_card (r := r) q` (first step of the `calc` in `theta_lt_of_large_delta_aux`, Lemma 7 large-δ case) |
| Roth/Theta.lean:33 | module docstring mention only |

Inline-derivation grep:
  - Roth/Theta.lean:87–93 (`indexSet_bddAbove`): re-derives the same member-wise bound `index ≤ card σ` over `indexSet` with a verbatim copy of lines 116–118 (to produce `BddAbove` rather than the `sSup` bound). Found with `grep -rn index_le_card Roth/` (hits at Theta.lean:91 and :117 only).

### Composition check (Phase 6)

Can `Roth.Θ_le_card` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.sSup_le (fun _ ⟨R, ⟨hR0, hRd, _⟩, _, _, hx⟩ ↦ hx ▸ index_le_card (cast-transport hR0) (cast-transport hRd) _) (Nat.cast_nonneg _)`
  - Decls used: mathlib `Real.sSup_le`, `Nat.cast_nonneg`, `map_ne_zero_iff`, `MvPolynomial.map_injective`, `Int.cast_injective`, `MvPolynomial.degrees_map_of_injective`; project `Roth.index_le_card`.
  - Result: succeeds (evidence (1)).
  - Notes: one mathlib supremum call; the rest is transporting hypotheses along `ℤ → ℝ`.

Attempt 2 (with the sibling refactor): `Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)`
  - Result: succeeds (evidence/Roth.indexSet_bddAbove/refactor.lean, item (3)).

Conclusion: COMPOSABLE

## Verdict: `Roth.Θ_le_card`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** the fact is tacit (clean.tex l.665–667; Yamada math/0307203 defines `Θ_m` but does not state `Θ_m ≤ m` separately). The general content is "a sup is below any nonnegative upper bound of its members".
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. No hypotheses; stronger than the paper (evidence (2)).
- **Mathlib search (Phase 5):** building block `Real.sSup_le` (Loogle, Lean-Finder). No `Roth` namespace in mathlib.
- **Composition check (Phase 6):** COMPOSABLE as one `Real.sSup_le` call with `index_le_card` (evidence (1)).

**Rationale:**

`Roth.Θ_le_card` is mathlib's `Real.sSup_le` applied to the project-local carrier `Roth.indexSet`, whose members are bounded by `card σ` by the project's `Roth.index_le_card` (the actual mathematical content: Taylor expansion has a nonzero coefficient with `i_j ≤ r_j`, hence weight `≤ m`). `Roth.Θ` and `Roth.indexSet` are bookkeeping objects of the Ridout/Cassels proof of Roth's lemma, and `Θ` itself is NO-composable-from-mathlib; whatever reusable content exists lives in `Roth.index`/`index_le_card`, assessed separately.

WHY not: a single mathlib call (`Real.sSup_le`) about a Roth-proof-specific supremum that will never be in mathlib.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean as the paper-facing `Θ_m ≤ m`, paired with `Θ_nonneg`. The bucket's usual "inline at call sites" step is not recommended: inlining at Theta.lean:939 would expose `indexSet`'s internals and the cast transport in the middle of a `calc`, and the named lemma documents the paper's claim.

Mathlib building blocks:
- `Real.sSup_le` (Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:222)
- `MvPolynomial.map_injective`, `map_ne_zero_iff`, `Int.cast_injective`, `MvPolynomial.degrees_map_of_injective` (cast transport)
- project `Roth.index_le_card` (Roth/Index.lean:224)

Composition sketch (≤3 lines, given the sibling helper from evidence/Roth.indexSet_bddAbove/refactor.lean):
```lean
example {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} : Θ B q r ≤ Fintype.card σ :=
  Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)
```

Call sites in our project (from Phase 6.0): 1, at Roth/Theta.lean:939.

Refactor plan: keep the lemma; leave Theta.lean:939 unchanged. Optional deduplication: add `card_mem_upperBounds_indexSet` (body = current lines 116–118 plus `classical`), then set `indexSet_bddAbove := ⟨_, card_mem_upperBounds_indexSet B q r⟩` and `Θ_le_card := Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)`.

Next action: no upstreaming; keep as basic `Θ` API, optionally deduplicating with `indexSet_bddAbove`.

## Next step

No upstreaming. Keep `Roth.Θ_le_card` in Roth/Theta.lean as the `Θ_m ≤ m` API lemma; optionally factor the body shared with `indexSet_bddAbove` into `card_mem_upperBounds_indexSet`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ_le_card/composition.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports success with no errors or warnings, only the `#check` info. It contains:
  - (1) the statement proved by `Real.sSup_le` + `index_le_card` with no hypotheses;
  - (2) `Θ_le_card` instantiated at `B = -1`, `r = 0` (empty index set, zero weights), confirming no hidden hypotheses;
  - (3) `#check @Θ_le_card`, confirming the signature uses only `[Fintype σ]`.
- Sibling evidence reused: `.mathlib-quality/overview/evidence/Roth.indexSet_bddAbove/refactor.lean` item (3) compiles `Θ_le_card` as a one-liner from `card_mem_upperBounds_indexSet`.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, mathlib doc mirrors (`Real.sSup_nonpos`, `Real.isLUB_sSup`, `Real.sSup_def`).
- Lean-Finder, Loogle and LeanSearch queries as recorded in Phase 5. Grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth`; `Real.sSup_le` at Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:222.
- Local refs: clean.tex l.660–670.
- `grep -rn "Θ_le_card\|index_le_card" Roth/` for the call-sites and inline-derivation tables.
- Parent/sibling reports Roth.Θ.md, Roth.indexSet_bddAbove.md, Roth.Θ_nonneg.md were reused.
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
