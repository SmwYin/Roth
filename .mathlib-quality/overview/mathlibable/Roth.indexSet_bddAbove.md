---
decl: Roth.indexSet_bddAbove
file: Roth/Theta.lean
line: 87
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: BddAbove of the project-local indexSet, proved as BddAbove.intro with bound card σ and one call of the project lemma index_le_card; a csSup side condition about a proof-internal set with no mathlib home, and its body is duplicated verbatim in Θ_le_card.
action: Do not upstream; keep in Roth/Theta.lean (callers index_le_Θ at Theta.lean:102 and Θ_mono at Theta.lean:136); optionally factor the shared body into card_mem_upperBounds_indexSet so indexSet_bddAbove and Θ_le_card (Theta.lean:113) become one-liners (evidence/Roth.indexSet_bddAbove/refactor.lean), and fix the docstring's spurious "if every r j is positive".
---

# Roth.indexSet_bddAbove

## Inventory entry

### `theorem Roth.indexSet_bddAbove`
- **Type**: `∀ {σ : Type*} [Fintype σ] (B : ℝ) (q : σ → ℕ) {r : σ → ℕ}, BddAbove (Roth.indexSet B q r)`
- **What**: The set of indices `ind(R; h/q; r)`, taken over `R ∈ ℛ_m(B; r)` and `h` coprime to `q`, is bounded above by the number of variables `m = card σ`. This is the boundedness half of "the supremum `Θ_m` is well-defined".
- **How**: It gives the explicit bound `Fintype.card σ`. For each member `R` it applies `Roth.index_le_card`, which needs two facts. Nonvanishing over ℝ comes from mathlib's `map_ne_zero_iff` and `MvPolynomial.map_injective` with `Int.cast_injective`. The per-variable degree bound comes from `simpa [degreeOf, MvPolynomial.degrees_map_of_injective]`.
- **Hypotheses**: none. `B` and `q` are arbitrary and `r` is implicit with no positivity. The section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.indexSet`, `Roth.RSet` (destructured membership), `Roth.index_le_card`, and `Roth.index` through `indexSet`.
- **Used by**: `Roth.index_le_Θ` (Roth/Theta.lean:102, `le_csSup (indexSet_bddAbove B q) ...`) and `Roth.Θ_mono` (Roth/Theta.lean:136, `csSup_le_csSup (indexSet_bddAbove B' q) ...`). Nothing else uses it (`grep -rn indexSet_bddAbove Roth/`).
- **Visibility**: public
- **Lines**: 83–92 (docstring 83–86, statement 87, proof 88–92), proof length 5 lines
- **Notes**:
  - The docstring opens "If every `r j` is positive", but the statement has no such hypothesis. The lemma holds for every `r` (evidence (4)), so the docstring is stale and should drop that clause.
  - The argument order is also unusual: `B` and `q` are explicit while `r` is implicit.
  - The proof body (lines 89–92) is a near-verbatim copy of the body of `Θ_le_card` (Theta.lean:113–118).
  - Source: clean.tex:665–667.

## Junk check (Step 8)
- **Used anywhere?** Yes, twice, as the `BddAbove` side condition of `le_csSup` and `csSup_le_csSup`.
- **Wrapper of 1–2 mathlib calls?** No. It is `BddAbove.intro` plus one project lemma (`index_le_card`) plus coercion bookkeeping.
- **Does mathlib have it?** No. `indexSet` is project-local, and mathlib has no `namespace Roth`.
- **Too specific (inline?)?** It should not be inlined: it is the standard named companion of `indexSet_nonempty` for the `csSup` API. However, its content is duplicated in `Θ_le_card`. The fix is to factor that content into `card_mem_upperBounds_indexSet : (card σ : ℝ) ∈ upperBounds (indexSet B q r)`. Then this lemma becomes `⟨_, card_mem_upperBounds_indexSet B q r⟩` and `Θ_le_card` becomes `Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)`. Both compile (evidence (1)–(3)).
- **Well-chosen?** Yes, apart from the stale docstring clause.
- **Conclusion:** `KEEP`. Optionally factor out the shared upper-bound lemma and fix the docstring.

## Mathlibable assessment (Step 9)

Pre-filter:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`).

No SKIP. This is not a glue lemma: the proof uses the real bound `index_le_card`. A full run follows. The parent `Roth.indexSet` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no diagnostics)
- decl `Roth.indexSet_bddAbove`: resolved at Roth/Theta.lean:87
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.indexSet_bddAbove` is a theorem stating the following.

For any `B ∈ ℝ`, denominators `q ∈ ℕ^σ` and weights `r ∈ ℕ^σ`, consider the set `I = { ind(R; (h_j/q_j)_j; r) : R ∈ ℛ_m(B; r), gcd(h_j, q_j) = 1 }` of real numbers. This set is bounded above; indeed every element is at most `m = |σ|`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables.
- `B`: the coefficient bound.
- `q`: the denominators.
- `r`: the degree bounds / weights.

Hypotheses (Lean side): none.

Conclusion (math): `sup I < ∞`, and more precisely `I ⊆ (-∞, m]`.

Conclusion (Lean): `BddAbove (indexSet B q r)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a well-definedness side lemma for a supremum in the proof of Roth's theorem. It is neither a main result nor a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof Θ_m supremum of index over polynomials bounded coefficients "0 ≤ Θ" at most m | partial | arXiv math/0307203 defines `Θ_m` as the supremum of `θ(R)` over `ℛ_m(B; r)` | finiteness is taken for granted, with no separate lemma |
| 2 | WebSearch (general form) | set of real numbers bounded above supremum well-defined index of polynomial at rational points Ridout Roth | no | general Roth/Ridout background (Wikipedia, Waldschmidt, Bugeaud) | boundedness is never isolated as a statement |
| 3 | WebSearch (aliases: Cassels) | Cassels Diophantine approximation Roth lemma Theta_m(B; q; r) supremum index well-defined bounded | partial | math/0307203 Lemma 2.1 gives the deep bound `Θ_m < 10^m δ^{(1/2)^m}`. Cassels' book is the textbook source | the trivial bound `Θ_m ≤ m` is implicit |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "Theta", "well-defined" | yes | clean.tex:665–667: "This supremum is well-defined and satisfies `0 ≤ Θ_m ≤ m`" via Taylor's theorem. clean.tex:700 also records "nonemptiness and boundedness of the defining family" | this lemma is exactly that boundedness step |
| 6 | nLab | supremum / bounded set | no | general order-theoretic supremum only | nothing specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (a bound on a set of reals) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry. After a brief check, "index" in Stacks refers to unrelated notions |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary for a thread |
| 10 | recent arXiv | arXiv 2502.00731 (2025, Roth/subspace exposition) from searches 1–3 | partial | defines the index and Roth's lemma | the trivial upper bound is not stated separately |

### Literature summary (Phase 3)

Concept identified as: well-definedness (boundedness above) of the supremum `Θ_m(B; q; r)` in the Roth/Ridout/Cassels proof.
Sources agree on the standard form: yes. It is tacit everywhere, and the project source states it explicitly at clean.tex:665–667.
Most general standard form: the index of any nonzero polynomial with `deg_{x_j} ≤ r_j` is at most `m`, so the family is bounded by `m`.
Generality dimensions where the literature varies: none relevant. `B` and `q` play no role in the bound.
Disagreement with the literature: none. The Lean docstring's "if every `r j` is positive" is a leftover; the source assumes positive `r_j`, but Lean needs no such hypothesis.

### Generality analysis — `Roth.indexSet_bddAbove`

Literature-standard form: every element of the index family is `≤ m`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `B` | arbitrary real | `B ≥ 1` | already general | no hypothesis |
| 2 | `q` | arbitrary | positive integers | already general | no hypothesis |
| 3 | `r` positivity | none (docstring claims one) | positive | already general | evidence (4) instantiates `r = 0` |
| 4 | conclusion `BddAbove` | existential bound | explicit bound `m` | stronger sibling | `card_mem_upperBounds_indexSet` (evidence (1)) exposes the explicit bound and also serves `Θ_le_card` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. It has no hypotheses at all.
Number of weakening opportunities found: 0. There is one optional strengthening/refactor: expose the explicit upper bound `card σ` (verified in evidence (1)–(3)).
Proposed restatement: none required. Optionally add `card_mem_upperBounds_indexSet` and derive this lemma from it.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | no hypotheses | — |
| 2 | Sequences vs filters? | no | an order-theoretic bound on a set | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | `indexSet` is a plain carrier set, as its own report says | — |
| 5 | Field-specific vs typeclass-weakened? | no | fixed by the parent defs (ℝ-valued `index`) | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | — | — |
| 8 | Concrete-via-abstract? | partially | after `rintro` the proof never mentions `indexSet` again. Its content is "every value of `index` under the box condition is `≤ card σ`", which is `index_le_card`. The abstract piece is already factored as `index_le_card` | none |
| 9 | False-generalisation guard | no false generalisation | the refactor keeps the meaning | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: this is a `BddAbove` side condition on a project-local set. Its abstract content already lives in `Roth.index_le_card`.

### Proof strategy — `Roth.indexSet_bddAbove`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing helpers? | yes (project-local) | `card_mem_upperBounds_indexSet` removes the duplicated body shared with `Θ_le_card`. Separately, if `index_le_card` dropped its superfluous `hP` (see Roth.index_le_card.md), the `map_ne_zero_iff` argument and `hR0` would disappear here too | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (local, cosmetic)
  - Proposed strategy: factor out `card_mem_upperBounds_indexSet`. Then this lemma is `⟨_, card_mem_upperBounds_indexSet B q r⟩` and `Θ_le_card` is `Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)`.
  - Cost: CHEAP (compiled, evidence (1)–(3)).
  - Missing mathlib API: none.
  - Would refactoring make the proof strictly shorter / cleaner? Yes: it removes about 5 duplicated lines.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.indexSet_bddAbove`

[A] Lean-Finder       "set of values of a function bounded above when each value is at most a constant; constant belongs to upperBounds of image"   hits: `IsMaxOn.bddAbove`, `BddAbove.range_mono`, `le_ciSup_set`. These are generic order lemmas, with nothing about indices
[B] Loogle            `BddAbove (Set.image _ _), ∀ _, _ ≤ _`   no hits
[C] LeanSearch        "image of a set under a function bounded by c is BddAbove"   hits: `Cardinal.bddAbove_image`, `BddAbove.image2`, `IsMaxOn.bddAbove`. All generic
[D] Grep mathlib src  `namespace Roth` (no hits); `mem_upperBounds` (Mathlib/Order/Bounds/Basic.lean:35). These are generic building blocks
[E] Name pattern      `indexSet_bddAbove` / `Roth.` in mathlib by grep: no hits

Searched for both:
  - the user's current form (BddAbove of the Roth index family)
  - the literature-standard form (index ≤ m for box-bounded polynomials; covered by Roth.index_le_card.md, which found no mathlib analogue)

Concluded: found building blocks (`BddAbove` / `upperBounds` API, `MvPolynomial.map_injective`, `map_ne_zero_iff`, `MvPolynomial.degrees_map_of_injective`, plus the project's `index_le_card`); composition gives our form.

### Normal-form check — `Roth.indexSet_bddAbove`

Equivalent formalisms:
- `BddAbove (indexSet B q r)` (this lemma)
- `(card σ : ℝ) ∈ upperBounds (indexSet B q r)` (explicit)
- `∀ x ∈ indexSet B q r, x ≤ card σ`

Does mathlib already have a canonical form? `BddAbove` is the canonical side-condition form for `le_csSup` and `csSup_le_csSup`. It is fine as stated.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.indexSet_bddAbove`

Alternative restatements attempted:
- the current `BddAbove` form
- `card_mem_upperBounds_indexSet` (evidence (1))

Chosen restatement: keep `BddAbove`, which is what both callers consume. Add the explicit `upperBounds` form as the primitive it is derived from.
Justification: `le_csSup` and `csSup_le_csSup` take `BddAbove` directly, while `Θ_le_card` wants the explicit bound.

### Superfluous-argument audit — `Roth.indexSet_bddAbove`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `B` explicit | only to name the set | the explicit/implicit mix (`B`, `q` explicit; `r` implicit) is inherited by callers. It is harmless |
| 2 | `q` explicit | only to name the set | same |
| 3 | `[Fintype σ]` | yes | needed for `card σ` and `index` |
| 4 | `[DecidableEq σ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (an optional explicit-bound sibling is proposed)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (local docstring fix recommended)

### Call sites — `Roth.indexSet_bddAbove`

Internal use count: 0 outside the declaring file. There are 2 uses inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:102 | `le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩` (in `index_le_Θ`) |
| Roth/Theta.lean:136 | `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) ?_` (in `Θ_mono`) |

Inline-derivation grep:
  - Roth/Theta.lean:115–118 (`Θ_le_card`): this re-derives the same upper bound inline, with the identical `rintro` and `index_le_card ((map_ne_zero_iff ...).2 hR0) (by simpa [...] using hRd) _` body, instead of sharing it.

### Composition check (Phase 6)

Can `Roth.indexSet_bddAbove` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⟨Fintype.card σ, by rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩; exact index_le_card (...) (...) _⟩`
  - Decls used: mathlib `BddAbove` (anonymous constructor), `map_ne_zero_iff`, `MvPolynomial.map_injective`, `Int.cast_injective`, `MvPolynomial.degrees_map_of_injective`; project `Roth.index_le_card`.
  - Result: succeeds (this is the current proof).
  - Notes: the mathematical content is a single application of `index_le_card`. Everything else is coercion bookkeeping from ℤ to ℝ.

Attempt 2: `⟨_, card_mem_upperBounds_indexSet B q r⟩`, once the shared helper is factored out.
  - Result: succeeds (evidence (2)).

Conclusion: COMPOSABLE

## Verdict: `Roth.indexSet_bddAbove`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** clean.tex:665–667 is the only explicit statement ("This supremum is well-defined and satisfies `0 ≤ Θ_m ≤ m`"). Elsewhere the fact is tacit (math/0307203, 2502.00731).
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. There are no hypotheses, and the docstring's positivity clause is spurious (evidence (4)).
- **Mathlib search (Phase 5):** only generic `BddAbove` / `upperBounds` building blocks; there is no `Roth` namespace in mathlib.
- **Composition check (Phase 6):** COMPOSABLE. It is `BddAbove.intro` plus one call of `index_le_card`.

**Rationale:**

The lemma is the `BddAbove` side condition for `csSup` on the project-local carrier set `Roth.indexSet`, whose own verdict is NO-composable-from-mathlib. Mathematically, it is "every member is an index of a box-bounded nonzero polynomial, hence `≤ m`", which is one application of `Roth.index_le_card` (also NO-composable) wrapped in mathlib's `BddAbove` constructor with ℤ→ℝ coercion bookkeeping. Nothing here is general enough for mathlib: `indexSet` and `Θ` are proof-internal objects of the Roth argument.

WHY not: it is a one-step composition of existing project API (`index_le_card`) and mathlib's order and coercion lemmas, about a set that will never be in mathlib.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean, next to `indexSet_nonempty`, as the paper's "supremum is well-defined" step.

Mathlib building blocks:
- `BddAbove` / `mem_upperBounds` (Mathlib/Order/Bounds/Basic.lean:35)
- `map_ne_zero_iff`
- `MvPolynomial.map_injective`
- `MvPolynomial.degrees_map_of_injective`
- `Int.cast_injective`
- project `Roth.index_le_card` (Roth/Index.lean:224)

Composition sketch (≤3 lines):
```lean
  refine ⟨Fintype.card σ, ?_⟩
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0) (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ) Int.cast_injective] using hRd) _
```

Call sites in our project (from Phase 6.0): 2 (Roth/Theta.lean:102, Roth/Theta.lean:136).

Refactor plan:
- Do not inline at the 2 call sites. Inlining would duplicate the bound twice more, and the named `BddAbove` companion is idiomatic for the `csSup` API.
- Instead, remove the existing duplication: add `card_mem_upperBounds_indexSet` (the body above, stated as `(card σ : ℝ) ∈ upperBounds (indexSet B q r)`). Then:
  - change `indexSet_bddAbove` to `⟨_, card_mem_upperBounds_indexSet B q r⟩`;
  - change `Θ_le_card` (Theta.lean:113) to `Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)`.
- Delete "If every `r j` is positive," from the docstring.
- If `index_le_card` later drops `hP`, also drop the `map_ne_zero_iff` argument and `hR0` here.

Next action: keep locally, do not upstream, and optionally apply the dedup and docstring fix above.

## Next step

Keep `Roth.indexSet_bddAbove` in Roth/Theta.lean and do not upstream it. Optionally factor out `card_mem_upperBounds_indexSet` (proof in `.mathlib-quality/overview/evidence/Roth.indexSet_bddAbove/refactor.lean`) so that it and `Θ_le_card` become one-liners. Also fix the stale "If every `r j` is positive" clause in the docstring.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.indexSet_bddAbove/refactor.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports no diagnostics. It contains:
  - (1) `card_mem_upperBounds_indexSet`, the shared upper-bound fact.
  - (2) `indexSet_bddAbove` as `⟨_, card_mem_upperBounds_indexSet B q r⟩`.
  - (3) `Θ_le_card` as `Real.sSup_le (card_mem_upperBounds_indexSet B q r) (Nat.cast_nonneg _)`.
  - (4) `indexSet_bddAbove` applied with `r = fun _ ↦ 0`, showing there is no positivity hypothesis on `r`.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, Evertse's Luminy slides, Wikipedia "Roth's theorem", Waldschmidt's HRI 2011 notes.
- Local grep of `.mathlib-quality/references/clean.tex` (lines 655–668 and 700).
- Lean-Finder, LeanSearch and Loogle queries, plus a grep of `.lake/packages/mathlib/Mathlib/`, as recorded in Phase 5.
- `grep -rn indexSet_bddAbove Roth/` found the declaration plus Theta.lean:102 and 136.
- The parent reports Roth.indexSet.md, Roth.Θ.md, Roth.index_le_card.md and Roth.indexSet_nonempty.md were reused.
- The ChatGPT channel is n/a: the `ask_chatgpt_math` MCP is not configured in this session.
