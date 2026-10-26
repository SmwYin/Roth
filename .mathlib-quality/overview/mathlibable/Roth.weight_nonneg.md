---
decl: Roth.weight_nonneg
file: Roth/Box.lean
line: 75
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent is NO-mathlib-has-it), mathlib has no Finsupp.weight_nonneg, but it is the one-call composition Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _ (zero_le when canonically ordered); the project form is itself one call (Fintype.sum_nonneg + positivity).
action: Keep as a project-local API lemma for its 3 call sites (Index.lean:94, Theta.lean:395, Lattice.lean:145); if Roth.weight is refactored onto Finsupp.weight, reprove it as Finsupp.sum_nonneg fun j _ ↦ nsmul_nonneg (by positivity) _; no mathlib PR.
---

# Roth.weight_nonneg

## Inventory entry

### `theorem Roth.weight_nonneg`
- **Type**: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ Roth.weight r d`
- **What**: The weight `∑ j, d j / r j` of any multi-index is nonnegative.
- **How**: Term proof `Fintype.sum_nonneg fun _ ↦ by positivity` (each summand `(d j : ℝ) / r j` is a quotient of natural-number casts).
- **Hypotheses**: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:94 (`index_nonneg`, via `Real.sInf_nonneg`); Roth/Theta.lean:395 (`(weight_nonneg _ _).trans h2`); Roth/Lattice.lean:145 (`linarith [weight_nonneg r d]` in private `filter_weight_le_eq_empty`).
- **Visibility**: public
- **Lines**: 73–76, proof length 1 line
- **Notes**: Source docstring cites clean.tex §4 l.565 ("Every weight ... is nonnegative").

## Junk check (Step 8)
- Used anywhere? Yes, 3 call sites in 3 files (Index, Theta, Lattice).
- Wrapper of 1–2 mathlib calls? Yes: `Fintype.sum_nonneg` + `positivity`.
- Does mathlib have it? Not for `Roth.weight`; for the re-aimed `Finsupp.weight` there is no `Finsupp.weight_nonneg` (grep of Mathlib/Data/Finsupp/Weight.lean and loogle `0 ≤ Finsupp.weight _ _`: no hit), but it is one call to `Finsupp.sum_nonneg`.
- Too specific (inline)? Inlining at 3 sites would replace a named fact with `Fintype.sum_nonneg fun _ ↦ by positivity` (and `linarith [...]` / `.trans` uses read better with the name); keeping it is cheaper than inlining.
- Well-chosen? Yes; standard `_nonneg` API companion of the project def.
- Conclusion: `KEEP` — action: keep as project API in Roth/Box.lean; if `Roth.weight` is redefined via `Finsupp.weight` (per Roth.weight report), reprove by `Finsupp.sum_nonneg fun j _ ↦ nsmul_nonneg (by positivity) _`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_nonneg` not in mathlib (no `namespace Roth` in Mathlib). Not a glue lemma (`Fintype.sum_nonneg` + `positivity`, not rfl/unfolding). Parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`, so per the re-aim rule this run is re-aimed at `Finsupp.weight`: the target statement is `Finsupp.weight_nonneg : (∀ i, 0 ≤ w i) → 0 ≤ Finsupp.weight w f`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight_nonneg`: resolved at Roth/Box.lean:75
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_nonneg` is a theorem stating the following: for a finite index set `σ`, parameters `r ∈ ℕ^σ` and a multi-index `d ∈ ℕ^σ`, the weight `w_r(d) = ∑_j d_j / r_j` is a nonnegative real number. Re-aimed: for any weight vector `w : σ → M` with values in an ordered additive monoid, all `w_i ≥ 0`, the weighted degree `⟨w, d⟩ = ∑_i d_i w_i` of a multi-index `d ∈ ℕ^(σ)` is `≥ 0`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (needed because `Roth.weight` sums over `univ`).
- `r : σ → ℕ` — parameters (nonnegativity of `1/r_j` is automatic for natural `r_j`, including `r_j = 0` by `x/0 = 0`).
- `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- none.

Conclusion (math): `0 ≤ ∑_j d_j / r_j`.

Conclusion (Lean): `0 ≤ Roth.weight r d`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line positivity fact about a bookkeeping def; not a structure, not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of polynomial nonnegative weight sum i_j/r_j | yes | index defined as min of `∑ i_j/r_j`; nonnegativity used implicitly | arXiv math/0307203 (Roth–Ridout), arXiv 1305.0926 (GIT and Roth), Evertse Bonn notes (weights `1/d_i`) |
| 2 | WebSearch (general form) | weighted degree nonnegative weights monomial weighted degree nonnegative | partial | weighted degree `∑ w_i α_i`, weights usually positive integers | arXiv 1301.5612, 1412.7547, Magma docs, mathlib WeightedHomogeneous docs; nonnegativity is immediate and never stated as a named result |
| 3 | WebSearch (named-after / aliases) | "weighted degree" "positive weights" grading polynomial ring nonnegative grading | partial | positive / nonnegative gradings; weights in ordered groups (arXiv 1305.0093) | nonnegativity of degrees for a nonnegative grading is folklore, used without statement |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `nonneg` | yes | l.565: "Every weight `∑_j i_j/r_j` is nonnegative" (proof of `index ≥ 0` lemma) | project paper §4; stated as an unproved one-line remark |
| 6 | nLab | graded ring / nonnegatively graded | partial | ℕ-graded (nonnegatively graded) rings | the degree map of a nonnegative grading lands in a nonnegative monoid; no lemma-level content |
| 7 | nCatLab | — | n/a | — | not a categorical concept (elementary inequality) |
| 8 | Stacks Project | graded rings (weighted polynomial rings) | partial | ℕ-gradings by positive weights | degrees nonnegative by construction; nothing to cite |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | an immediate fact; no discussion found |
| 10 | recent arXiv (last 5 years) | (results of #2, #3; arXiv 2604.26950 on weighted linearisation) | partial | strictly positive weights, weighted-degree filtration | uses nonnegativity implicitly |

### Literature summary (Phase 3)

Concept identified as: nonnegativity of the weighted degree `⟨w, d⟩ = ∑ w_i d_i` for a nonnegative weight vector `w` and a multi-index `d ∈ ℕ^(σ)`.
Sources agree on the standard form: yes (always immediate, never a named result).
Most general standard form: for `w : σ → M` with `M` an ordered additive commutative monoid and all `w_i ≥ 0`, `0 ≤ ∑ d_i • w_i`; in a canonically ordered `M` it is automatic.
Generality dimensions where the literature varies:
  - weight values: positive integers (gradings) vs reals `1/r_j` (Roth) vs elements of an ordered monoid/group; the most general is an ordered additive monoid.
  - finiteness of `σ`: not needed (finite support suffices).
Disagreement with the literature: none; the project form is the special weight vector `(1/r_j)` with `r_j ∈ ℕ`.

### Generality analysis — `Roth.weight_nonneg`

Literature-standard form (from Phase 3): `0 ≤ Finsupp.weight w f` for `w : σ → M`, `∀ i, 0 ≤ w i`, `[IsOrderedAddMonoid M]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector | `1/r j`, `r : σ → ℕ` | any `w` with `0 ≤ w i` | yes | realised by evidence `finsupp_weight_nonneg` (compiles) |
| 2 | codomain `ℝ` | ℝ | any ordered additive comm. monoid | yes | same evidence; for canonically ordered `M` it is `zero_le` (compiles) |
| 3 | `[Fintype σ]` | required | not needed | yes for the re-aimed form; no for the project form | `Roth.weight` itself needs `[Fintype σ]`; the `Finsupp.weight` form does not |
| 4 | `d : σ →₀ ℕ` | ℕ exponents | ℕ exponents (nonnegative coefficients) | no | with general semiring coefficients nonnegativity needs ordered coefficients; ℕ is the case of interest |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is a one-call mathlib composition (`Finsupp.sum_nonneg` + `nsmul_nonneg`), verified in the evidence file; routed to NO-composable-from-mathlib, not generalise-first.
Number of weakening opportunities found: 3 (rows 1–3), all verified for the re-aimed `Finsupp.weight` statement.
Proposed restatement (re-aimed, optional): `theorem Finsupp.weight_nonneg (hw : ∀ i, 0 ≤ w i) (f : σ →₀ ℕ) : 0 ≤ weight w f := Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _`.
Cost of restatement: CHEAP (one-liner; verified).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite sum inequality |
| 3 | construction vs universal property? | no | — | inequality, not a construction |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | ordered additive monoid codomain (re-aimed form) | matches `Finsupp.le_weight_of_ne_zero`'s typeclass context |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `ℝ` and `1/r j` to arbitrary nonnegative `w : σ → M` | as #5 |
| 8 | concrete-via-abstract? | no | proof uses only termwise nonnegativity; already abstract after unfolding, but there is nothing to extract beyond the re-aimed form | — |
| 9 | false-generalisation guard | no false generalisation | re-aimed form specialises back to the project lemma (evidence example (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `0 ≤ Finsupp.weight w f` under `∀ i, 0 ≤ w i` (one call to `Finsupp.sum_nonneg`).
  - Cost: CHEAP
  - Mathlib downstream this enables: companion to `Finsupp.le_weight_of_ne_zero` (whose proof already inlines exactly this `Finset.sum_nonneg`/`nsmul_nonneg` argument at Weight.lean:159).
  - Real mathematical improvement: marginal; it names a fact that is a single composition.

### Proof strategy — `Roth.weight_nonneg`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `Finsupp.sum_nonneg`, `Fintype.sum_nonneg`, `nsmul_nonneg` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(After the optional `Roth.weight` → `Finsupp.weight` refactor, the proof becomes `Finsupp.sum_nonneg fun j _ ↦ nsmul_nonneg (by positivity) _`; equally short.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_nonneg`

[A] Lean-Finder       "Finsupp.weight w f is nonnegative if every w i is nonnegative"   hits: `Finsupp.le_weight_of_ne_zero`, `Finsupp.sum_nonneg'`, `Finsupp.le_weight`, `Finsupp.sum_nonneg`, `Finsupp.le_weight_of_ne_zero'` — no nonneg lemma for `weight`
[B] Loogle            `0 ≤ Finsupp.weight _ _`   no hits
[C] LeanSearch        "weight of a finsupp is nonnegative when all weights are nonnegative"   hits: `Finsupp.sum_nonneg'`, `Finsupp.single_nonneg`, `Finsupp.sum_pos`, `Finsupp.mapDomain_nonneg`, `Finsupp.sum_pos'` (building blocks only)
[D] Grep mathlib src  `weight_nonneg`, `0 ≤ weight`, `nonneg` in Mathlib/Data/Finsupp/Weight.lean   only `Quiver.Path.weight_nonneg` (unrelated namespace, Combinatorics/Quiver/Path/Weight.lean:108); Weight.lean has no nonneg lemma, only the inline argument in `le_weight_of_ne_zero` (:159)
[E] Name pattern      `Finsupp.weight_nonneg`, `Finsupp.sum_nonneg`, `nsmul_nonneg`   `Finsupp.weight_nonneg` absent; building blocks present (used in compiled evidence)

Searched for both the user's form (`0 ≤ ∑ d j / r j`) and the literature-standard re-aimed form (`0 ≤ Finsupp.weight w f`).

Concluded: found building blocks (`Finsupp.sum_nonneg`, `nsmul_nonneg`, `zero_le`, `Fintype.sum_nonneg`); composition would yield our form.

### Normal-form check — `Roth.weight_nonneg`

Equivalent formalisms: `0 ≤ weight r d`; `0 ≤ Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d`; `0 ≤ ∑ j, (d j : ℝ) / r j`.
Does mathlib already have a canonical form for this idea? The canonical object is `Finsupp.weight`; no nonneg lemma exists.
Is our statement stated against the canonical form? It is stated against the project def `Roth.weight`, which is the parent's refactor target; the lemma itself is an `0 ≤ _` inequality, the standard `_nonneg` shape.
RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.weight_nonneg`

Alternative restatements attempted:
- `0 ≤ Finsupp.weight w f` with `hw : ∀ i, 0 ≤ w i` (compiles; evidence)
- implicit `r`, `d` (call sites pass them explicitly or as `_ _`; `linarith [weight_nonneg r d]` needs them explicit)
Chosen restatement: as stated (explicit `r d`).
Justification: Lattice.lean:145 feeds it to `linarith` with explicit arguments; explicit is easiest there.

### Superfluous-argument audit — `Roth.weight_nonneg`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed for `Roth.weight` to typecheck |
| 2 | `r` | yes | — |
| 3 | `d` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_nonneg`

Internal use count: 3 (outside Roth/Box.lean)
External-to-file callers: 3 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:94 | `Real.sInf_nonneg (Set.forall_mem_image.mpr fun d _ ↦ weight_nonneg r d)` (`index_nonneg`) |
| Roth/Theta.lean:395 | `max_le (add_nonneg (index_nonneg _ _ _) ((weight_nonneg _ _).trans h2)) ...` |
| Roth/Lattice.lean:145 | `Finset.filter_eq_empty_iff.2 fun d _ h ↦ by linarith [weight_nonneg r d]` |

Inline-derivation grep:
  - (none) — no other `sum_nonneg`/`positivity` re-derivation of weight nonnegativity in Roth/.
  - Mathlib itself inlines the re-aimed fact at Mathlib/Data/Finsupp/Weight.lean:159 (inside `le_weight_of_ne_zero`).

### Composition check (Phase 6)

Can `Roth.weight_nonneg` be derived from mathlib in ≤3 chained calls?

Attempt 1 (project form): `Fintype.sum_nonneg fun _ ↦ by positivity`
  - Mathlib decls used: `Fintype.sum_nonneg`, `positivity`
  - Result: succeeds (this is the current proof; evidence example (4))

Attempt 2 (re-aimed form): `Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _`
  - Mathlib decls used: `Finsupp.sum_nonneg`, `nsmul_nonneg` (and `Finsupp.weight_apply` by defeq)
  - Result: succeeds (evidence `finsupp_weight_nonneg`); canonically ordered case is `zero_le` (evidence (2)); project lemma recovered via the parent bridge (evidence (3))

Conclusion: COMPOSABLE

## Verdict: `Roth.weight_nonneg`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): nonnegativity of a weighted degree with nonnegative weights is immediate and never a named result (clean.tex l.565 states it in one line).
- Generality analysis (Phase 4): STRICTLY NARROWER, but the general re-aimed form is a one-call composition (verified).
- Mathlib search (Phase 5): no `Finsupp.weight_nonneg`; building blocks `Finsupp.sum_nonneg`, `nsmul_nonneg`, `Fintype.sum_nonneg`.
- Composition check (Phase 6): COMPOSABLE (one call in both the project and re-aimed forms).

**Rationale:**

Re-aimed at `Finsupp.weight` (the parent `Roth.weight` is `NO-mathlib-has-it` as `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`), the analogue `0 ≤ Finsupp.weight w f` for nonnegative `w` is not in mathlib, but it is `Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _`, a single application, and in the canonically ordered case it is `zero_le`. A `Finsupp.weight_nonneg` would be a reasonable but tiny API completion beside `Finsupp.le_weight_of_ne_zero` (which inlines the same argument); it does not clear the bar for a standalone contribution and could at most ride along in an unrelated `Finsupp/Weight.lean` PR. The project lemma is likewise one call (`Fintype.sum_nonneg` + `positivity`).

WHY not: mathlib has the building blocks and the statement is a one-call composition. Belongs-elsewhere check: keep it project-local in Roth/Box.lean as the `_nonneg` companion of `Roth.weight`; with 3 call sites (one in `linarith`), the named lemma is cheaper than inlining.

Mathlib building blocks:      `Finsupp.sum_nonneg` (Mathlib/Data/Finsupp/Order.lean:56), `nsmul_nonneg`, `Fintype.sum_nonneg`, `zero_le`
Composition sketch (≤3 lines):
```lean
example (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ Roth.weight r d :=
  Fintype.sum_nonneg fun _ ↦ by positivity
-- re-aimed: 0 ≤ Finsupp.weight w f
example (hw : ∀ i, 0 ≤ w i) (f : σ →₀ ℕ) : 0 ≤ Finsupp.weight w f :=
  Finsupp.sum_nonneg fun i _ ↦ nsmul_nonneg (hw i) _
```
Call sites in our project (from Phase 6.0):  3 (Index.lean:94, Theta.lean:395, Lattice.lean:145)
Refactor plan: no inlining recommended (Step 8 KEEP): the 3 sites use the name as a term (`weight_nonneg r d`, `.trans`, `linarith [...]`); inlining would replace it with `Fintype.sum_nonneg fun _ ↦ by positivity` at each, a readability loss. If `Roth.weight` is redefined via `Finsupp.weight` (parent report), reprove this lemma by `Finsupp.sum_nonneg fun j _ ↦ nsmul_nonneg (by positivity) _`; the 3 call sites are unchanged.
Next action: keep `Roth.weight_nonneg` locally; no mathlib PR (optionally mention `Finsupp.weight_nonneg` as a ride-along in any future `Mathlib/Data/Finsupp/Weight.lean` PR).

---

## Next step

No mathlib action. Keep the lemma; reprove via `Finsupp.sum_nonneg` only if the parent `Roth.weight` refactor onto `Finsupp.weight` is carried out.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_nonneg/weight_nonneg_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics after fixing `zero_le` arity): (1) `finsupp_weight_nonneg` — re-aimed general form via `Finsupp.sum_nonneg` + `nsmul_nonneg`; (2) canonically ordered case `zero_le`; (3) project lemma recovered from (1) through the parent bridge; (4) current proof `Fintype.sum_nonneg` + `positivity`.
- Loogle `0 ≤ Finsupp.weight _ _` (no hits); LeanSearch and Lean-Finder queries as in the search-status block (building blocks only).
- Mathlib greps: `weight_nonneg`, `0 ≤ weight`, `nonneg` in Mathlib/Data/Finsupp/Weight.lean.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.565).
- Project grep `grep -rn weight_nonneg Roth/` for the call-sites table.
