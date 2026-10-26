---
decl: Roth.linearIndependent_update_sub_smul
file: Roth/Wronskian.lean
line: 170
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Pure linear algebra (transvection preserves linear independence) that mathlib has only in the Pi-add spelling linearIndependent_add_smul_iff; the Function.update iff over [Ring R] for any module (verified, 4-line proof) is the missing companion of Submodule.span_range_update_add_smul, and the project lemma is a one-line corollary.
action: Add linearIndependent_update_sub_smul_iff (and the add_smul variant) over [Ring R] [AddCommGroup M] to Mathlib/LinearAlgebra/LinearIndependent/Defs.lean next to linearIndependent_add_smul_iff; then reduce the project lemma (call sites Roth/Wronskian.lean:190 and :214) to a one-line corollary or inline it.
---

# Roth.linearIndependent_update_sub_smul

## Inventory entry

### `theorem Roth.linearIndependent_update_sub_smul`
- **Type**: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) (hφ : LinearIndependent K φ) : LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν))`
- **What**: Replacing `φ ν'` by `φ ν' - c φ ν` (constant `c`, `ν ≠ ν'`) in a linearly independent family of polynomials keeps it linearly independent.
- **How**: Rewrites linear independence as `card = finrank (span)` (`linearIndependent_iff_card_eq_finrank_span`, `Set.finrank`), turns `C c *` into `c •` (`smul_eq_C_mul`), and uses mathlib's `Submodule.span_range_update_sub_smul` to see the span is unchanged.
- **Hypotheses**: `[Field K]` (section variable); `h : ν ≠ ν'`; `c : K`; `hφ : LinearIndependent K φ`.
- **Uses from project**: `[]` (only mathlib lemmas; `wronskian` not involved)
- **Used by**: Roth/Wronskian.lean:190 (`sum_natDegree_update_lt`, nonvanishing of the updated member), Roth/Wronskian.lean:214 (`wronskian_ne_zero_of_linearIndependent`, induction step). No other project use.
- **Visibility**: public
- **Lines**: 170–175, proof length 3 lines
- **Notes**: Nothing polynomial-specific: the statement is about a family of vectors in any module. The `finrank` proof needs a division ring (finite-dimensional span), but the statement itself holds over any ring (evidence (1)).

## Junk check (Step 8)
- Used anywhere? Yes, twice, both in Roth/Wronskian.lean (l.190, l.214).
- Wrapper of 1–2 mathlib calls? Nearly: `linearIndependent_iff_card_eq_finrank_span` + `Submodule.span_range_update_sub_smul`; alternatively `linearIndependent_add_smul_iff` with `c = Pi.single ν' (-c)` plus a function-extensionality step (evidence (1)).
- Does mathlib have it? In content yes (`linearIndependent_add_smul_iff`, Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:751, Pi-add spelling `v + (c · • v i)` with `c i = 0`); not in the `Function.update` spelling, although the span analogue `Submodule.span_range_update_sub_smul` is in that spelling.
- Too specific? Stated for `K[X]` over a field, which is needlessly specific; the general version belongs in mathlib's linear-independence API.
- Well-chosen? The mathematical content is right; the generality is too narrow.
- Conclusion: `KEEP` — action: keep locally until the general `Function.update` iff is upstreamed, then make it a one-line corollary (or inline at the two call sites).

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring does not start internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `update_sub_smul` over `.lake/packages/mathlib/Mathlib/` only hits `Submodule.span_range_update_sub_smul`, Span/Defs.lean:652, and its use in Algebra/Polynomial/CoeffMem.lean:117). Not a glue lemma (no parent def; a real 3-line proof), so the full workflow is run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.linearIndependent_update_sub_smul`: resolved at Roth/Wronskian.lean:170
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.linearIndependent_update_sub_smul` is a theorem stating: let `φ_0, …, φ_{l-1} ∈ K[t]` be linearly independent over a field `K`, let `ν ≠ ν'` and `c ∈ K`. Then the family obtained by replacing `φ_{ν'}` with `φ_{ν'} - c φ_ν` (all other members unchanged) is again linearly independent. That is, an elementary column operation (a transvection) preserves linear independence.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]` — scalar field.
- `l : ℕ` — size of the family.
- `φ : Fin l → K[X]` — the family (vectors in the `K`-module `K[X]`).
- `ν ν' : Fin l` — source and target index.
- `c : K` — multiplier.

Hypotheses (Lean side):
- `h : ν ≠ ν'` — the multiple is of a different member.
- `hφ : LinearIndependent K φ` — the original family is independent.

Conclusion (math): `(φ_0, …, φ_{ν'} - c φ_ν, …, φ_{l-1})` is linearly independent.

Conclusion (Lean): `LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν))`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper for the induction proving `wronskian_ne_zero_of_linearIndependent`; no new structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | elementary column operation preserves linear independence adding multiple of one vector to another | yes | adding a scalar multiple of one vector to another preserves the span and linear independence (reversible operation) | UAlberta "Discover Linear Algebra" 21.5, Sowiso, NKU MAT225 notes; textbook folklore |
| 2 | WebSearch (general form) | linear independence invariant under invertible change of basis matrix module over ring | yes | for invertible `P`, `v` independent iff `v P` independent; holds over any ring (automorphism of the free module `R^n`) | arXiv 2508.13165 (rings and modules notes), Reed/CUHK notes; no division needed |
| 3 | WebSearch (named-after / aliases) | transvection elementary operation family of vectors linearly independent iff lemma | partial | transvections are `I + v w*` with `w*(v)=0`; elementary operations preserve span hence independence | no named lemma; Axler-style exercise; Mathlib docs surfaced (LinearIndependent/Lemmas) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §2 first lemma, l.174–180 | yes | "By invertible column operations over Q, replace them by a basis ... of their span" | the source uses only that invertible column operations preserve the span/independence; no special statement |
| 6 | nLab | linear independence | partial | linear independence of a family in a module; no lemma on elementary operations | general definition only |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | elementary linear algebra, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by #1/#3) | partial | standard exercise answers: row/column operations preserve independence of columns | folklore |
| 10 | recent arXiv (last 5 years) | results of #1/#2 | partial | arXiv 2207.02728 (formalising Fisher's inequality, linear-algebra techniques in Isabelle) uses the folklore fact | confirms folklore; no new formulation |

### Literature summary (Phase 3)

Concept identified as: invariance of linear independence under elementary (transvection) operations, a special case of invariance under right multiplication by an invertible matrix.
Sources agree on the standard form: yes — for a family `v : ι → M` in a module over a ring `R`, `i ≠ j`, `r ∈ R`: `(…, v_j + r v_i, …)` is independent iff `v` is.
Most general standard form: an iff, over any ring `R` and any `R`-module `M`, any index type, for a single transvection (and more generally for any invertible change of family).
Generality dimensions where the literature varies:
  - scalars: field to any ring (the operation is invertible over any ring).
  - ambient space: `K^n`/function spaces to any module.
  - direction: one implication to iff (the inverse operation is again a transvection).
Disagreement with the literature: none; the Lean form is a specialisation (field, polynomial ring, one direction).

### Generality analysis — `Roth.linearIndependent_update_sub_smul`

Literature-standard form (from Phase 3): `LinearIndependent R (Function.update v j (v j - r • v i)) ↔ LinearIndependent R v` for `[Ring R] [AddCommGroup M] [Module R M]`, `v : ι → M`, `i ≠ j`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | ring | yes | verified via `linearIndependent_add_smul_iff` (`[Ring R]`) in evidence (1); the current `finrank` proof does not survive, a different 4-line proof does |
| 2 | `K[X]` (ambient) | polynomial ring | any module `M` | yes | nothing polynomial-specific is used; verified for `[AddCommGroup M] [Module R M]` (evidence (1)) |
| 3 | `Fin l` (index) | finite index | any type `ι` with `[DecidableEq ι]` | yes | verified (evidence (1)); the `finrank` proof needed finiteness, the new one does not |
| 4 | `C c * φ ν` | polynomial multiplication | `c • φ ν` | yes (spelling) | `smul_eq_C_mul`; the module spelling is the general one |
| 5 | implication | `hφ → …` | iff | yes | the inverse is a transvection with `-r`; verified as iff (evidence (1)) |
| 6 | `[Ring R]` to `[Semiring R]` | — | — | NO | statement uses subtraction; `linearIndependent_add_smul_iff` is stated for `Ring`, and over semirings the operation is not invertible |
| 7 | `h : ν ≠ ν'` | distinct indices | distinct indices | NO | necessary: `ν = ν'`, `c = 1` sends `![X]` to `![0]`, not independent (evidence (3), verified) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 5 (field to ring, `K[X]` to any module, `Fin l` to any index type, `C c *` to `•`, implication to iff), all in one verified statement: `linearIndependent_update_sub_smul_iff` in `.mathlib-quality/overview/evidence/Roth.linearIndependent_update_sub_smul/compose.lean`, `lean_diagnostic_messages` clean (no errors, no warnings).
Proposed restatement:

```lean
theorem linearIndependent_update_sub_smul_iff {ι R M : Type*} [DecidableEq ι] [Ring R]
    [AddCommGroup M] [Module R M] {v : ι → M} {i j : ι} (hij : i ≠ j) (r : R) :
    LinearIndependent R (Function.update v j (v j - r • v i)) ↔ LinearIndependent R v
```
(plus the `v j + r • v i` variant, mirroring `Submodule.span_range_update_add_smul` / `span_range_update_sub_smul`).

Cost of restatement: CHEAP — verified; proof is `convert linearIndependent_add_smul_iff (c := Pi.single j (-r)) …` + `ext`/`by_cases`/`simp` (4 lines).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled preamble |
| 2 | sequences to filters? | no | — | finite algebra, no topology |
| 3 | construction vs universal property? | no | — | a property, not a construction |
| 4 | set-with-predicate to bundled substructure? | no | — | already uses `LinearIndependent` on a family |
| 5 | field-specific to (semi)ring? | yes | `[Ring R]` module statement (Phase 4a rows 1–2) | full module API; applies to `ℤ`-families, polynomial rings over rings |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `ι` with `[DecidableEq ι]` instead of `Fin l` (row 3) | infinite families, `Finsupp`-indexed bases |
| 8 | concrete-via-abstract? | yes | the proof body never uses that the vectors are polynomials (`K[X]` appears only through `C c * = c •`); abstract restatement over any module, project lemma as one-line corollary (evidence (2)) | reuse for any family of vectors |
| 9 | false-generalisation guard | no false generalisation | the general statement is the same property (`LinearIndependent`) of the same family viewed in the module `K[X]`; evidence (2) recovers the project lemma in one line | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `linearIndependent_update_sub_smul_iff` / `linearIndependent_update_add_smul_iff` over `[Ring R] [AddCommGroup M] [Module R M]` (above).
  - Cost: CHEAP
  - Mathlib downstream this enables: a `Function.update`-spelled companion to `Submodule.span_range_update_add_smul` / `span_range_update_sub_smul` (Span/Defs.lean:640/652), so elementary-operation arguments on bases (span unchanged and independence unchanged) can be run in one spelling; `Basis` construction via elementary operations; it would also give the proof of `Roth.sum_natDegree_update_lt` and the reduction in `Roth.wronskian_ne_zero_of_linearIndependent` directly.
  - Real mathematical improvement: removes the needless field/finite-dimensionality dependence of the proof (the `finrank` argument) and states the fact at the level where it is true.

### Proof strategy — `Roth.linearIndependent_update_sub_smul`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals/submodules | partial | current proof is already point-free (span equality + finrank); but going through `finrank` forces a division ring and finiteness | CHEAP |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the `Function.update` iff above (the update/Pi-add bridge is what is missing; `linearIndependent_add_smul_iff` has the content) | CHEAP (file with the upstreaming PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: derive from `linearIndependent_add_smul_iff` with `c = Pi.single j (-r)` (works over any ring) instead of the dimension count.
  - Cost: CHEAP
  - Missing mathlib API (if any): `linearIndependent_update_add_smul_iff` / `linearIndependent_update_sub_smul_iff`.
  - Would refactoring make the proof strictly shorter / cleaner? yes for the general statement (the `finrank` route is unavailable over rings); with the mathlib lemma in place, the project lemma is one line.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.linearIndependent_update_sub_smul`

[A] Lean-Finder       "linear independence preserved when replacing one vector by itself minus a scalar multiple of another vector"   hits: `linearIndependent_add_smul_iff` (Pi-add spelling, `[Ring R]`), `LinearIndependent.pair_add_smul_left_iff/right_iff`, `pair_add_left_iff/right_iff` (two-element families only)
[B] Loogle            `LinearIndependent, Function.update`   one hit: `LinearIndependent.update` (`[CommRing R]`, replacement `m` with `r • m` a combination with non-zero-divisor coefficients; one direction; applicable but much heavier to instantiate)
[C] LeanSearch        "LinearIndependent of update add smul of a different index iff"   `linearIndependent_add_smul_iff`, `pair_add_smul_*_iff`, `linearIndependent_iff_eq_zero_of_smul_mem_span`; no update-spelled iff
[D] Grep mathlib src  `update_sub_smul`, `update_add_smul` (only `Submodule.span_range_update_add_smul/sub_smul`, Span/Defs.lean:640/652); `linearIndependent.*update` (only `LinearIndependent.update`, LinearIndependent/Lemmas.lean:544)   no update-spelled transvection lemma for independence
[E] Name pattern      `linearIndependent_update_sub_smul`, `linearIndependent_update_add_smul`, `LinearIndependent.update_add_smul`   absent

Searched for both the user's form (field, polynomials, implication) and the literature-standard form (ring, module, iff, update spelling).

Concluded: found building blocks (`linearIndependent_add_smul_iff`, `LinearIndependent.update`, `Submodule.span_range_update_sub_smul` with `linearIndependent_iff_card_eq_finrank_span`); the content is in mathlib in the Pi-add spelling, the `Function.update` spelling is not.

### Normal-form check — `Roth.linearIndependent_update_sub_smul`

Equivalent formalisms: `Function.update v j (v j - r • v i)`; `v + (Pi.single j (-r) · • v i)` (mathlib's `linearIndependent_add_smul_iff`); `v ∘ₗ transvection`-style matrix action.
Does mathlib already have a canonical form? For this fact, `linearIndependent_add_smul_iff` (Pi-add, general `c` with `c i = 0`); for the companion span fact, the `Function.update` spelling (`Submodule.span_range_update_add_smul`).
Proposed canonical form: an iff `LinearIndependent R (update v j (v j + r • v i)) ↔ LinearIndependent R v` with the simpler side on the RHS, proved from `linearIndependent_add_smul_iff`; sub variant as a corollary, exactly as `span_range_update_sub_smul` is derived from `span_range_update_add_smul`.
RHS convention respected? the current form is an implication, not an equation/iff; the restatement puts `LinearIndependent R v` on the RHS.

### Syntactic generality — `Roth.linearIndependent_update_sub_smul`

Alternative restatements attempted:
- current: field, `K[X]`, `C c * φ ν`, implication.
- `Function.update` iff over `[Ring R]`, any module, any index (verified, evidence (1)).
- direct use of `linearIndependent_add_smul_iff` at call sites (needs a `Pi.single` + funext bridge each time).
Chosen restatement: the `Function.update` iff (add and sub variants).
Justification: call sites (as in the project) naturally produce `Function.update`; the Pi-add spelling needs a function-extensionality bridge at each use, which is the gap.

### Superfluous-argument audit — `Roth.linearIndependent_update_sub_smul`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[Ring R]` suffices (verified) |
| 2 | `K[X]` ambient | no | any module (verified) |
| 3 | `Fin l` finiteness | no | any `ι` with `[DecidableEq ι]` (verified) |
| 4 | `h : ν ≠ ν'` | yes | counterexample with `ν = ν'` (verified) |
| 5 | `hφ` | yes | becomes the RHS of the iff |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (iff in `Function.update` spelling with `LinearIndependent R v` on the RHS)
Syntactic generality: RESTATE (module statement over a ring, any index type)
Superfluous arguments: 3 to drop (`[Field K]` to `[Ring R]`, `K[X]` to any module, `Fin l` to any `ι`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.linearIndependent_update_sub_smul`

Internal use count: 0 outside the declaring file; 2 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:190 | `simpa using (linearIndependent_update_sub_smul h a hφ).ne_zero ν'` (in `sum_natDegree_update_lt`) |
| Roth/Wronskian.lean:214 | `(linearIndependent_update_sub_smul hne _ h) rfl` (in `wronskian_ne_zero_of_linearIndependent`) |

Inline-derivation grep: `grep -rn "span_range_update\|linearIndependent_add_smul_iff\|LinearIndependent.update" Roth/` finds only the declaration's own proof (l.174). (none)

### Composition check (Phase 6)

Can `Roth.linearIndependent_update_sub_smul` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(linearIndependent_add_smul_iff (c := Pi.single ν' (-c)) (i := ν) (by simp [h])).2 hφ`
  - Mathlib decls used: `linearIndependent_add_smul_iff`
  - Result: partial — the family it produces is `φ + (Pi.single ν' (-c) · • φ ν)`, which must be identified with `Function.update φ ν' (φ ν' - C c * φ ν)` by `ext k; by_cases k = ν'; simp [...]` (evidence (1)): a small real proof, not a call chain.

Attempt 2: current proof: `linearIndependent_iff_card_eq_finrank_span` + `Set.finrank` + `smul_eq_C_mul` + `Submodule.span_range_update_sub_smul` (a `rw` chain of 4 rewrites plus `exact`).
  - Result: works, but only over a division ring with a finite family; a 4-step rewrite chain is at the edge of the ≤3-call heuristic.

Attempt 3: `LinearIndependent.update` (`[CommRing R]`), with `r = 1`, `l = single ν' 1 - single ν c`.
  - Result: partial — needs building the `Finsupp` and two `nonZeroDivisors` side goals; a proof, not a composition.

Conclusion: NOT-COMPOSABLE (the content is in `linearIndependent_add_smul_iff`, but the `Function.update` bridge is a genuine, if short, proof; this bridge is exactly the proposed mathlib lemma)

## Verdict: `Roth.linearIndependent_update_sub_smul`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard folklore over any ring: elementary (transvection) operations preserve linear independence, as an iff (UAlberta DLA 21.5, Axler-style exercises, module notes arXiv 2508.13165); the source §2 (clean.tex l.174–180) uses it implicitly.
- Generality analysis (Phase 4): STRICTLY NARROWER — field to ring, `K[X]` to any module, `Fin l` to any index, implication to iff; all verified in one compiled statement (evidence (1)); `ν ≠ ν'` necessary (evidence (3)).
- Mathlib search (Phase 5): content present as `linearIndependent_add_smul_iff` (Pi-add spelling); no `Function.update`-spelled lemma, although the span companion `Submodule.span_range_update_sub_smul` exists in that spelling.
- Composition check (Phase 6): NOT-COMPOSABLE (needs a funext bridge).

**Rationale:**

The project lemma is pure linear algebra stated in a needlessly special setting: polynomials over a field. Its proof also goes through `finrank`, which only works for finite families over a division ring. The literature fact is an iff over any ring and module. Mathlib has the content only in the spelling `LinearIndependent R (v + (c · • v i)) ↔ LinearIndependent R v` with `c i = 0` (`linearIndependent_add_smul_iff`, Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:751). The span half of the same elementary-operation argument is already in mathlib in the `Function.update` spelling (`Submodule.span_range_update_add_smul` / `span_range_update_sub_smul`, Mathlib/LinearAlgebra/Span/Defs.lean:640/652), but the independence half is not. That missing `update` companion is the gap. Without it, every user (here two call sites) either repeats the `Pi.single` + funext bridge or, as the project does, falls back on a dimension count that only works for finite families over a division ring.

The general iff compiles over `[Ring R] [AddCommGroup M] [Module R M]` with any `[DecidableEq ι]` index, with a 4-line proof from `linearIndependent_add_smul_iff`, and the project statement is a one-line corollary (evidence (1), (2)). This lemma is not tied to the n-ary Wronskian PR of its siblings. It is an independent, small linear-algebra PR. The borderline aspect is size: mathlib maintainers may consider an `update` wrapper of `linearIndependent_add_smul_iff` too thin. The precedent of `span_range_update_*` argues for it.

Reason for the generalisation: LITERATURE-WEAKENING (field to ring, polynomials to any module, finite to arbitrary index, implication to iff) and MODERN-IDIOM (`Function.update` spelling mirroring `Submodule.span_range_update_add_smul`, proof via `linearIndependent_add_smul_iff` rather than `finrank`).
Proposed restatement:
```lean
theorem linearIndependent_update_add_smul_iff {ι R M : Type*} [DecidableEq ι] [Ring R]
    [AddCommGroup M] [Module R M] {v : ι → M} {i j : ι} (hij : i ≠ j) (r : R) :
    LinearIndependent R (Function.update v j (v j + r • v i)) ↔ LinearIndependent R v := by
  sorry -- as evidence (1) with `Pi.single j r`
theorem linearIndependent_update_sub_smul_iff {ι R M : Type*} [DecidableEq ι] [Ring R]
    [AddCommGroup M] [Module R M] {v : ι → M} {i j : ι} (hij : i ≠ j) (r : R) :
    LinearIndependent R (Function.update v j (v j - r • v i)) ↔ LinearIndependent R v := by
  sorry -- verified in evidence (1)
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- elementary-operation arguments on families/bases in one spelling: `span_range_update_*_smul` (span unchanged) together with the new lemma (independence unchanged) give "an elementary operation sends a basis to a basis" directly;
- removes the division-ring/finite-dimensionality dependence of such arguments (works for `ℤ`-lattices, polynomial rings over rings);
- in the project, `Roth.sum_natDegree_update_lt` and `Roth.wronskian_ne_zero_of_linearIndependent` would use it directly.
PR grouping: standalone small PR to `Mathlib/LinearAlgebra/LinearIndependent/Defs.lean` (next to `linearIndependent_add_smul_iff`), not tied to the n-ary Wronskian PR (`Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.wronskian_update_sub_smul`); the Wronskian criterion PR would then consume it.
Next action: run `/generalise Roth.linearIndependent_update_sub_smul` (target the module iff above); then update the call sites Roth/Wronskian.lean:190 and :214 to the corollary.

---

## Next step

Run `/generalise Roth.linearIndependent_update_sub_smul`, targeting `linearIndependent_update_sub_smul_iff` (and the `add_smul` variant) over `[Ring R] [AddCommGroup M] [Module R M]`. Then upstream it to `Mathlib/LinearAlgebra/LinearIndependent/Defs.lean` and keep the project lemma as a one-line corollary used at Roth/Wronskian.lean:190 and :214.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.linearIndependent_update_sub_smul/compose.lean` (imports `Roth.Wronskian`), checked with `lean_diagnostic_messages`. The first check had no errors, only style warnings (missing module docstring placement, unused simp args); these were cleaned up and the re-check is clean (no diagnostics). It verifies: (1) `linearIndependent_update_sub_smul_iff` over `[Ring R] [AddCommGroup M] [Module R M]`, any `ι` with `[DecidableEq ι]`, proved from `linearIndependent_add_smul_iff` with `c = Pi.single j (-r)`; (2) the project statement as a one-line `simpa [smul_eq_C_mul]` corollary of (1); (3) `ν ≠ ν'` is necessary (`ν = ν' = 0`, `c = 1`, `φ = ![X]` over `ℚ` gives a non-independent family).
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Lean-Finder, Loogle and LeanSearch queries, plus the mathlib greps, are recorded in Phase 5.
- Project greps: `grep -rn linearIndependent_update_sub_smul Roth/` found the declaration plus call sites l.190 and l.214. `grep -rn "span_range_update\|linearIndependent_add_smul_iff\|LinearIndependent.update" Roth/` found only l.174.
