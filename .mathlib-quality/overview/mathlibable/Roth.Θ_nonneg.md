---
decl: Roth.Θ_nonneg
file: Roth/Theta.lean
line: 107
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The nonnegativity of the project-local supremum Θ, proved as one call of mathlib's Real.sSup_nonneg fed by the project's index_nonneg (compiled); it is about a Roth-proof-specific quantity, so there is nothing to upstream, but it is the paper-facing Θ API lemma (clean.tex 0 ≤ Θ_m) used at Theta.lean:583.
action: Do not upstream; keep in Roth/Theta.lean next to Θ_le_card as the basic Θ API (caller index_numeric_bound application at Theta.lean:583, used twice there); no call-site changes.
---

# Roth.Θ_nonneg

## Inventory entry

### `theorem Roth.Θ_nonneg`
- **Type**: `∀ {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ}, 0 ≤ Θ B q r`
- **What**: For every coefficient bound `B`, denominators `q` and weights `r`, the quantity `Θ_m(B; q; r)` (the supremum of the indices `ind(R; h/q; r)` over admissible `R` and coprime numerators `h`) is nonnegative. This is the lower half of the paper's `0 ≤ Θ_m ≤ m`.
- **How**: `apply Real.sSup_nonneg`, then destructure membership in `indexSet` (`rintro _ ⟨R, _, h, _, rfl⟩`) and close with the project's `index_nonneg`. Mathlib's `Real.sSup_nonneg` needs only that every member is nonnegative, because `sSup ∅ = 0` and `sSup` of an unbounded set is `0` in `ℝ`; hence no `1 ≤ B` hypothesis and no nonemptiness or boundedness lemma is required.
- **Hypotheses**: none (beyond `[Fintype σ]`). No `1 ≤ B`, no positivity of `r`; the section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.Θ`, `Roth.indexSet`, `Roth.index`, `Roth.index_nonneg` (and `Roth.RSet` implicitly through the `indexSet` membership pattern)
- **Used by**: Roth/Theta.lean:583 (`add_nonneg (Θ_nonneg _) (Θ_nonneg _)`, the nonnegativity argument fed to `index_numeric_bound_aux` inside the Lemma 6 proof); also cited in the module docstring at Roth/Theta.lean:33. Found with `grep -rn Θ_nonneg Roth/`; no other file uses it.
- **Visibility**: public
- **Lines**: 104–110 (docstring 105–106, statement 107, proof 108–110), proof length 3 lines
- **Notes**: Source: clean.tex §5 l.665 ("satisfies `0 ≤ Θ_m ≤ m`"). The paper argues via the member `R = 1` (nonemptiness); the Lean proof avoids that by using the `sSup ∅ = 0` convention, so it holds for every `B`, including `B < 1` where `indexSet` is empty. Minor shape nit: `q` is explicit while `B`, `r` are implicit (all three are determined by the conclusion); harmless, and matches `Θ_le_card`.

## Junk check (Step 8)
- **Used anywhere?** Yes, at Roth/Theta.lean:583 (twice on one line, for two different instances of `Θ`).
- **Wrapper of 1–2 mathlib calls?** Yes: `Real.sSup_nonneg` plus the project's `index_nonneg`. Inlining it would make the caller write `Real.sSup_nonneg fun _ ⟨_, _, _, _, hx⟩ ↦ hx ▸ index_nonneg _ _ _` twice and expose `indexSet`'s existential shape at the call site.
- **Does mathlib have it?** No; it concerns the project's `Θ`. The generic content is `Real.sSup_nonneg`.
- **Too specific (inline?)?** No. It is the paper-facing statement `0 ≤ Θ_m`, paired with `Θ_le_card`, and keeps callers independent of how `Θ` is defined.
- **Well-chosen?** Yes; hypothesis-free, which is the strongest form.
- **Conclusion:** `KEEP`. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib: there is no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`.

This is not a glue lemma in the brief's sense: the body applies `Real.sSup_nonneg` and `index_nonneg` (a real, if short, proof), not `rfl`/`Iff.rfl`/pure unfolding. A full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors)
- decl `Roth.Θ_nonneg`:      resolved at Roth/Theta.lean:107
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.Θ_nonneg` is a theorem stating the following.

Let `Θ_m(B; q; r)` be the supremum of the indices `ind(R; (h_j/q_j)_j; r)` over nonzero `R ∈ ℤ[X_j : j ∈ σ]` with `deg_{X_j} R ≤ r_j` and coefficients of absolute value at most `B`, and over `h ∈ ℤ^σ` with `gcd(h_j, q_j) = 1`. Then `Θ_m(B; q; r) ≥ 0`. (In Lean the supremum of an empty or unbounded family is `0` by convention, so the statement holds for all `B`, `q`, `r`.)

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables.
- `B`: the coefficient bound (implicit).
- `q`: the denominators (explicit).
- `r`: the degree bounds and index weights (implicit).

Hypotheses (Lean side):
- none.

Conclusion (math): `0 ≤ Θ_m(B; q; r)`.

Conclusion (Lean): `0 ≤ Θ B q r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic sign property of a project-local supremum; an API lemma, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem); recorded that the proof is `Real.sSup_nonneg` plus a membership destructuring and `index_nonneg`, expressible as a single term (evidence (1)).

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma Theta_m supremum index polynomial bounded coefficients "0 ≤ Θ" Ridout Cassels | partial | Yamada (arXiv math/0307203 §2, Lemma 2.1) bounds `Θ_m` above (Ridout's version of Roth's Lemma 7); nonnegativity is not stated separately | tacit in the literature |
| 2 | WebSearch (general form) | supremum of a set of nonnegative real numbers is nonnegative, empty set sSup convention, Real.sSup_nonneg | yes | every member `≥ 0` gives `sup ≥ 0`; mathlib `Real.sSup_nonneg` (with the `sSup ∅ = 0` convention) | the entire mathematical content |
| 3 | WebSearch (named-after / aliases) | index of a polynomial at a point Roth theorem nonnegative weighted order of vanishing Cassels | yes | the index is a minimum of nonnegative weighted sums `Σ i_j/r_j` (math/0307203; arXiv 2502.00731), so it is `≥ 0` | supplies the member-wise fact (`index_nonneg`) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "0\leq\Theta_m" | yes | clean.tex l.665: the supremum "is well-defined and satisfies `0 ≤ Θ_m ≤ m`", argued via the member `R = 1` | this lemma is the `0 ≤` half |
| 6 | nLab | supremum | partial | generic least upper bound; monotonicity of sup under pointwise bounds | nothing Roth-specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (a sign of a real number) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; no index-of-a-polynomial-at-a-point notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary for a thread |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), 2601.11376 (2026), from searches 1 and 3 | partial | pointwise Roth's lemma / effective Ridout constants | no supremum `Θ_m`, so no analogue of this lemma |

### Literature summary (Phase 3)

Concept identified as: the nonnegativity of the supremum `Θ_m(B; q; r)` from the Ridout/Cassels presentation of Roth's lemma.
Sources agree on the standard form: yes. It is tacit, immediate from the index being nonnegative.
Most general standard form: a supremum of nonnegative reals is nonnegative (`Real.sSup_nonneg`).
Generality dimensions where the literature varies: whether nonemptiness (`B ≥ 1`) is assumed; the paper uses it, the Lean form does not need it.
Disagreement with the literature: none in substance; the Lean form is slightly stronger (no `B ≥ 1`).

### Generality analysis — `Roth.Θ_nonneg`

Literature-standard form: `(∀ x ∈ s, 0 ≤ x) → 0 ≤ sSup s`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `1 ≤ B` | not taken | paper assumes `B ≥ 1` (member `R = 1`) | already weaker | `Real.sSup_nonneg` needs no nonemptiness (evidence (1)); the `B ≥ 1` route is evidence (2) and is strictly weaker |
| 2 | positivity of `r` | not taken | paper has `r_j ≥ 1` | already weaker | `index_nonneg` holds for all `r` |
| 3 | `[DecidableEq σ]` | omitted | n/a | already absent | evidence (3) |
| 4 | `[Fintype σ]` | required | finite `m` | NO | needed for `index`/`Θ` to be defined |

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
| 3 | Construction vs universal property? | no | follows from the upper-bound/least-ness of `sSup` already | — |
| 4 | Bundled substructure? | no | `indexSet` is a plain set of reals | — |
| 5 | Field-specific vs typeclass-weakened? | no | ℝ-valued by definition of `index`; the `sSup ∅ = 0` convention is ℝ-specific | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | arbitrary finite `σ` already | — |
| 8 | Concrete-via-abstract? | yes, trivially | after destructuring membership, the proof is `Real.sSup_nonneg` + `index_nonneg`; the abstract form already exists in mathlib | none (the abstraction is `Real.sSup_nonneg`) |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the abstract content is exactly mathlib's `Real.sSup_nonneg`; nothing remains to modernise.

### Proof strategy — `Roth.Θ_nonneg`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | no | `Real.sSup_nonneg` covers it | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`Real.sSup_nonneg` + `index_nonneg`; mirrors `index_nonneg`'s own `Real.sInf_nonneg` proof).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_nonneg`

[A] Lean-Finder       "supremum of a set of nonnegative real numbers is nonnegative"   hits: `Real.sSup_nonneg`, `Real.iSup_nonneg`, `Real.sSup_nonneg'`, `Real.iSup_nonneg'`, `NNReal.coe_iSup` (building blocks)
[B] Loogle            `(∀ x ∈ ?s, 0 ≤ x) → 0 ≤ sSup ?s`   hits: `Real.sSup_nonneg` (Mathlib.Algebra.Order.Archimedean.Real.Basic)
[C] LeanSearch        "supremum of indices of integer polynomials with bounded coefficients at rational points is nonnegative"   hits: `Real.iSup_nonneg'`, `Real.iSup_nonneg`, `one_le_pow_mul_abs_eval_div`, `Int.csSup_of_not_bddAbove` (building blocks / unrelated)
[D] Grep mathlib src  `namespace Roth` (no hits); `def Θ` (no hits); `sSup_nonneg` (definition at Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:288, plus uses)
[E] Name pattern      `Real.sSup_nonneg` (mathlib); `Θ_nonneg` (project only)

Searched for both:
  - the user's form (`0 ≤ Θ B q r`)
  - the literature-standard form (sup of nonnegatives is nonnegative): this is `Real.sSup_nonneg`

Concluded: found building blocks (`Real.sSup_nonneg`, plus the project's `index_nonneg`); composition gives our form.

### Normal-form check — `Roth.Θ_nonneg`

Equivalent formalisms:
- `0 ≤ Θ B q r` (current)
- `∀ x ∈ indexSet B q r, 0 ≤ x` combined with `Real.sSup_nonneg` at the call site

Does mathlib already have a canonical form? Yes: `0 ≤ _` nonnegativity lemmas named `*_nonneg`; our statement is in that form.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.Θ_nonneg`

Alternative restatements attempted:
- hypothesis-free (current, evidence (1))
- with `1 ≤ B` via `le_csSup` at a member (evidence (2), strictly weaker)

Chosen restatement: hypothesis-free (current).
Justification: the caller at Theta.lean:583 supplies nothing but `_` for `q`; no side conditions to discharge.

### Superfluous-argument audit — `Roth.Θ_nonneg`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `index` and `Θ` |
| 2 | `[DecidableEq σ]` | no | already omitted |
| 3 | `q` explicit | n/a | could be implicit like `B`, `r` (all determined by the conclusion); cosmetic only, consistent with `Θ_le_card` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.Θ_nonneg`

Internal use count: 0 outside the declaring file; 1 line (2 uses) inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:583 | `(add_nonneg (Θ_nonneg _) (Θ_nonneg _)) hδ1 hrp` (argument to `index_numeric_bound_aux` in the Lemma 6 proof) |
| Roth/Theta.lean:33 | module docstring mention only (`Roth.Θ_nonneg`, `Roth.Θ_le_card`: `0 ≤ Θ_m ≤ m`) |

Inline-derivation grep:
  - (none). `grep -rn sSup_nonneg Roth/` finds only this lemma's own proof (Theta.lean:108).

### Composition check (Phase 6)

Can `Roth.Θ_nonneg` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.sSup_nonneg fun _ ⟨_, _, _, _, hx⟩ ↦ hx ▸ index_nonneg _ _ _`
  - Decls used: mathlib `Real.sSup_nonneg`; project `Roth.index_nonneg`; anonymous-pattern destructuring of `indexSet` membership.
  - Result: succeeds (evidence (1)).
  - Notes: one mathlib call.

Attempt 2 (paper's route, for comparison): `indexSet_nonempty hB` + `le_csSup` + `index_nonneg` under `1 ≤ B`.
  - Result: succeeds (evidence (2)) but needs an extra hypothesis; not preferred.

Conclusion: COMPOSABLE

## Verdict: `Roth.Θ_nonneg`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** the fact is tacit (clean.tex l.665 "`0 ≤ Θ_m ≤ m`"; Yamada math/0307203 §2 only bounds `Θ_m` above). The general content is "sup of nonnegatives is nonnegative".
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. No hypotheses; stronger than the paper (no `B ≥ 1`) (evidence (1)).
- **Mathlib search (Phase 5):** building block `Real.sSup_nonneg` (Loogle, Lean-Finder hits). There is no `Roth` namespace in mathlib.
- **Composition check (Phase 6):** COMPOSABLE as one `Real.sSup_nonneg` call with `index_nonneg` (evidence (1)).

**Rationale:**

`Roth.Θ_nonneg` is mathlib's `Real.sSup_nonneg` applied to the project-local carrier `Roth.indexSet`, whose members are nonnegative by the project's `Roth.index_nonneg`. `Roth.Θ`, `Roth.indexSet` and `Roth.index_nonneg`'s subject (`Roth.index`) are bookkeeping objects of the Ridout/Cassels proof of Roth's lemma, and `Θ` itself is NO-composable-from-mathlib. The only general mathematics here is "a supremum of nonnegative reals is nonnegative", which mathlib already has.

WHY not: a single mathlib call (`Real.sSup_nonneg`) about a Roth-proof-specific supremum that will never be in mathlib.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean. It is the paper-facing `0 ≤ Θ_m` (clean.tex l.665), paired with `Θ_le_card`. The bucket's usual "inline at call sites" step is not recommended: the only caller (Theta.lean:583) uses it twice, inlining would duplicate a destructuring lambda over `indexSet`'s internal shape, and the named lemma documents the paper's claim.

Mathlib building blocks:
- `Real.sSup_nonneg` (Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:288)
- project `Roth.index_nonneg` (Roth/Index.lean:93)

Composition sketch (≤3 lines):
```lean
example {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} : 0 ≤ Θ B q r :=
  Real.sSup_nonneg fun _ ⟨_, _, _, _, hx⟩ ↦ hx ▸ index_nonneg _ _ _
```

Call sites in our project (from Phase 6.0): 1 line (2 uses), at Roth/Theta.lean:583.

Refactor plan: none. Keep the lemma; leave Theta.lean:583 unchanged. (If ever inlined, each `Θ_nonneg _` at 583 would become the term above; not recommended.) Optional golf: the 3-line tactic proof could be replaced by the one-line term from evidence (1).

Next action: no upstreaming; keep the lemma as part of the basic `Θ` API.

## Next step

No upstreaming. Keep `Roth.Θ_nonneg` in Roth/Theta.lean as the `0 ≤ Θ_m` API lemma. Any reusable content (a weighted order of vanishing at a point) is tracked under `Roth.index`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ_nonneg/composition.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports no errors, only a header-linter warning about a missing module docstring and the `#check` info. It contains:
  - (1) the statement proved by one `Real.sSup_nonneg` term with `index_nonneg` (no hypotheses);
  - (2) the paper's route under `1 ≤ B` via `indexSet_nonempty`, `le_csSup`, `index_nonneg` (strictly weaker);
  - (3) `#check @Θ_nonneg`, confirming the signature uses only `[Fintype σ]`.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, arXiv 2601.11376, mathlib doc mirrors for `Real.sSup_nonneg`.
- Lean-Finder, Loogle and LeanSearch queries as recorded in Phase 5. Grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth`; `Real.sSup_nonneg` at Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:288.
- Local refs: clean.tex l.655–670.
- `grep -rn Θ_nonneg Roth/` and `grep -rn sSup_nonneg Roth/` for the call-sites table.
- Parent/sibling reports Roth.Θ.md, Roth.index_le_Θ.md, Roth.index_nonneg.md were reused.
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
