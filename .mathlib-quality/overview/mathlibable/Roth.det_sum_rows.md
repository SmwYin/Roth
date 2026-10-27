---
decl: Roth.det_sum_rows
file: Roth/GenWronskian.lean
line: 228
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Row-multilinear expansion of det is MultilinearMap.map_sum_finset applied to Matrix.detRowAlternating plus MultilinearMap.map_smul_univ and unfolding Matrix.det (the current 4-line proof); no det-specific mathlib lemma exists but the composition is mechanical and has one caller.
action: Keep locally next to its single caller wronskian_kronecker_eq_sum_aux (Roth/GenWronskian.lean:245); optionally restate over an arbitrary [Fintype n] [DecidableEq n] index (verified in evidence); do not upstream.
---

# Roth.det_sum_rows

## Inventory entry

### `theorem Roth.det_sum_rows`
- **Type**: `{l : ℕ} {A : Type*} [CommRing A] {ι : Type*} (s : Fin l → Finset ι) (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) : (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det = ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det`
- **What**: If row `μ` of a square matrix is the linear combination `∑_{i ∈ s μ} c μ i • N μ i`, the determinant is the sum, over choice functions `f` with `f μ ∈ s μ`, of `∏_μ c μ (f μ)` times the determinant of the matrix with rows `N μ (f μ)`.
- **How**: `MultilinearMap.map_sum_finset` for `(Matrix.detRowAlternating).toMultilinearMap` applied to the rows `fun μ i ↦ c μ i • N μ i`, then `MultilinearMap.map_smul_univ` and `smul_eq_mul` to pull out `∏ c`, then `simp only [Matrix.det, Finset.sum_fn, Pi.smul_def, smul_eq_mul]` to match `Matrix.of`.
- **Hypotheses**: none (only `[CommRing A]`, needed for `Matrix.det`).
- **Uses from project**: `[]`
- **Used by**: Roth/GenWronskian.lean:245 (`wronskian_kronecker_eq_sum_aux`, private). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 228–236, proof length 5 lines
- **Notes**: Row/column type is `Fin l` (section variable `l`); the proof works verbatim for any `[Fintype n] [DecidableEq n]` (evidence).

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/GenWronskian.lean:245), inside a `simpa ... using det_sum_rows ...`.
- Wrapper of 1–2 mathlib calls? Essentially yes: `MultilinearMap.map_sum_finset` + `MultilinearMap.map_smul_univ` + unfolding `Matrix.det`.
- Does mathlib have it? Not in this determinant form (searched: `Matrix.det_updateRow_sum`, `Matrix.det_updateRow_add`, `Matrix.det_mul`, `Matrix.det_sum_le`, `Matrix.det_sum_smul_le`, no `Matrix.det_sum`); the abstract version `MultilinearMap.map_sum_finset` is in mathlib.
- Too specific (inline)? Single caller, but inlining the 4 tactic lines into the `simpa` of the private aux would make that proof harder to read; the separate statement mirrors the paper's sentence.
- Well-chosen? Yes; clean statement. Could be stated over a general `Fintype` index.
- Conclusion: `KEEP` — action: keep as a local helper; optionally generalise `Fin l` to `[Fintype n] [DecidableEq n]`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name does not end `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.det_sum_rows` not in mathlib (no `namespace Roth` in Mathlib; no `det_sum_rows` anywhere). Not a glue lemma (no parent def). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.GenWronskian` compiles with no output)
- decl `Roth.det_sum_rows`:  resolved at Roth/GenWronskian.lean:228
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  generalized Wronskians and Lemma 1 (a linearly independent family has a nonvanishing generalized Wronskian), via Kronecker substitution.

### Statement (Phase 1)

`Roth.det_sum_rows` is a theorem stating the following: let `A` be a commutative ring and `M` an `l × l` matrix over `A` whose `μ`-th row is a finite linear combination `M_μ = ∑_{i ∈ S_μ} c_{μ,i} N_{μ,i}` of row vectors `N_{μ,i} ∈ A^l`. Then, by multilinearity of the determinant in the rows,
`det M = ∑_{f ∈ ∏_μ S_μ} (∏_μ c_{μ,f(μ)}) · det (N_{μ,f(μ)})_{μ,ν}`.

Variables / typeclasses involved (Lean side):
- `A`, `[CommRing A]` — coefficient ring of the determinant.
- `ι` — index type of the terms in each row expansion.
- `s : Fin l → Finset ι` — the finite index set `S_μ` for row `μ`.
- `c : Fin l → ι → A` — coefficients.
- `N : Fin l → ι → Fin l → A` — the row vectors `N_{μ,i}`.

Hypotheses (Lean side):
- none.

Conclusion (math): the determinant expands as a sum over choice functions of products of coefficients times determinants.

Conclusion (Lean): `(Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det = ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: helper identity (row-multilinearity of det), a specialisation of the generic multilinear-map expansion.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: n/a (theorem)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | determinant multilinear in rows expand sum of rows "sum over all functions" determinant formula | yes | multilinear function of the rows expands as a sum over all functions `[n] → [n]`, alternation kills non-injective terms | UW Math 136 notes (4-20.pdf); TCD MA1111 handout |
| 2 | WebSearch (general form) | multilinear map applied to sums equals sum over choice functions product of coefficients alternating map determinant expansion | yes | `f(a) = ∑_{φ:[k]→[n]} a_{1φ(1)}⋯a_{kφ(k)} f(ε_{φ(1)},…,ε_{φ(k)})` for any multilinear `f` | LSU M7210 lecture notes eq. (1); Wikipedia "Leibniz formula", "Multilinear map"; arXiv 1803.09554 |
| 3 | WebSearch (named-after / aliases) | Wronskian of Kronecker substitution generalized Wronskian multilinearity determinant Roth lemma | yes | the same multilinear expansion used in the Kronecker-substitution proof of the generalized Wronskian criterion | arXiv 2502.00731 (Evertse); Roth 1955 Mathematika; arXiv 1310.4683 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `multilinearity` | yes | l.331: "multilinearity of the determinant in each row gives" the expansion | project paper §2, proof of Lemma 1 |
| 6 | nLab | multilinear map / determinant | partial | determinant as the top exterior power of an endomorphism; multilinear expansion is the definition of the tensor/exterior product | no specific entry for the choice-function expansion |
| 7 | nCatLab | — | n/a | — | not a categorical concept (elementary linear algebra identity) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; elementary multilinear algebra |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore "expand each row and use multilinearity" | textbook exercise level |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | yes | arXiv 2502.00731 (2025), arXiv 2509.06294 (2025, slice rank of det) | same expansion used as a tool |

### Literature summary (Phase 3)

Concept identified as: multilinear expansion of a multilinear (here alternating) map evaluated on sums, specialised to the determinant as a function of its rows.
Sources agree on the standard form: yes.
Most general standard form: for any multilinear map `f : ∏_i M_i → N` over a semiring and finite sums `x_i = ∑_{j ∈ S_i} g_{ij}`, `f(x) = ∑_{r ∈ ∏ S_i} f(g_{i,r(i)})`; with scalars, `f(∑ c_{ij} • v_{ij}) = ∑_r (∏ c_{i,r(i)}) f(v_{i,r(i)})`.
Generality dimensions where the literature varies:
  - map: determinant vs any multilinear map (the latter is standard).
  - row index: `{0,…,l-1}` vs any finite set.
Disagreement with the literature: none.

### Generality analysis — `Roth.det_sum_rows`

Literature-standard form (from Phase 3): `MultilinearMap.map_sum_finset` (+ `map_smul_univ`) for any multilinear map; for det, any finite row type.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | row/column type `Fin l` | `Fin l` | any finite type with decidable equality | yes | proof only needs `[Fintype n] [DecidableEq n]` for `Matrix.det`; verified in evidence (`det_sum_rows_gen`) |
| 2 | `[CommRing A]` | commutative ring | commutative ring (mathlib's `Matrix.det` requires `CommRing`) | no | `Matrix.det` / `detRowAlternating` are defined over `CommRing` |
| 3 | the map `det` | determinant | any multilinear map | yes, but already in mathlib | `MultilinearMap.map_sum_finset` is exactly the general form |
| 4 | `ι` single index type for all rows | uniform `ι` | dependent `α μ` per row | yes, trivially | mathlib's `map_sum_finset` already allows dependent index types; no need here |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — the general form (row 3) is already in mathlib as `MultilinearMap.map_sum_finset` (false-positive class 4); the only local weakening (row 1, `Fin l` to `[Fintype n] [DecidableEq n]`) compiles verbatim (evidence `det_sum_rows_gen`), but is a cosmetic local improvement, not a mathlib contribution.
Number of weakening opportunities found: 2 (rows 1, 3); row 1 verified in `det_sum_rows_exp.lean`; row 3 is mathlib's `MultilinearMap.map_sum_finset`.
Proposed restatement: optional local restatement over `{n : Type*} [Fintype n] [DecidableEq n]`, same body.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic identity |
| 3 | construction vs universal property? | yes | state for `detRowAlternating` as a multilinear map, i.e. use `MultilinearMap.map_sum_finset` directly | already in mathlib |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already over a `CommRing` (minimal for `Matrix.det`) | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `Fin l` to `[Fintype n] [DecidableEq n]` | uniformity with `Matrix.det` API (verified) |
| 8 | concrete-via-abstract? | yes | proof never uses determinant-specific facts, only multilinearity of `detRowAlternating`: it is `MultilinearMap.map_sum_finset` + `map_smul_univ` | already in mathlib |
| 9 | false-generalisation guard | no false generalisation | both generalisations keep the same determinant/same identity | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: none to add; use `(Matrix.detRowAlternating).toMultilinearMap.map_sum_finset` with `MultilinearMap.map_smul_univ` (already in mathlib).
  - Cost: CHEAP
  - Mathlib downstream this enables: nothing new.
  - Real mathematical improvement: none beyond `Fin l` to a general finite index.

### Proof strategy — `Roth.det_sum_rows`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already uses the multilinear-map structure of `det` rather than the Leibniz formula | — |
| 5 | missing mathlib helpers | partial | a `Matrix.det` wrapper of `map_sum_finset` does not exist; the `Matrix.of`/`Matrix.det` unfolding step is the only friction (a one-shot `simpa` fails on the `Matrix.of` wrapper, see Evidence) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (multilinear-map expansion via `MultilinearMap.map_sum_finset` and `MultilinearMap.map_smul_univ`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.det_sum_rows`

[A] Lean-Finder       "det of matrix with rows ∑ i ∈ s μ, c μ i • N μ i expands as ∑ over piFinset s of (∏ c) * det"   hits: `Matrix.sum_cramer`, `Matrix.det_eq_of_forall_row_eq_smul_add_const_aux`, `Matrix.sum_cramer_apply`, `Matrix.det_updateRow_sum_aux`, `Matrix.det_updateRow_sum` — none is the expansion
[B] Loogle            `Matrix.det, Fintype.piFinset`   no hits
[C] LeanSearch        "determinant of a matrix whose rows are finite sums equals sum over choice functions of determinants (multilinearity in rows)"   hits: `MultilinearMap.map_sum_finset`, `MultilinearMap.map_sum`, `MultilinearMap.map_sum_finset_aux`, `Matrix.det_updateRow_sum`, `Matrix.sum_cramer` — general form found
[D] Grep mathlib src  `map_sum_finset`, `map_smul_univ`, `piFinset` in Mathlib/LinearAlgebra/; `det_sum`, `det_of_sum`, `det_sum_rows`, `det_updateRow_sum`, `det_add_mul`; `namespace Roth`   hits: `MultilinearMap.map_sum_finset` (Multilinear/Basic.lean:620), `MultilinearMap.map_smul_univ` (Multilinear/Basic.lean:1161), `AlternatingMap.map_smul_univ` (Alternating/Basic.lean:633), `Matrix.det_updateRow_sum` (Determinant/Basic.lean:428), `Matrix.det_sum_le` (AbsoluteValue.lean:52, an inequality), `Matrix.det_add_mul` (SchurComplement.lean:437, unrelated); no det-specific choice-function expansion; no `Roth` namespace
[E] Name pattern      `MultilinearMap.map_sum_finset`, `MultilinearMap.map_smul_univ`, `Matrix.detRowAlternating`, `Matrix.det` (all used in compiled evidence)   hits

Searched for both the user's form (det of row sums) and the literature-standard form (multilinear map on sums).

Concluded: found building blocks (`MultilinearMap.map_sum_finset`, `MultilinearMap.map_smul_univ`, `Matrix.detRowAlternating`); composition yields our form. The more general multilinear form is in mathlib; the det-with-scalars specialisation is not stated verbatim.

### Normal-form check — `Roth.det_sum_rows`

Equivalent formalisms: (a) current `Matrix.of`-with-scalars form; (b) `det (of fun μ ↦ ∑ i ∈ s μ, g μ i) = ∑ f ∈ piFinset s, det (of fun μ ↦ g μ (f μ))` (no scalars, literally `map_sum_finset`, evidence example 3); (c) `detRowAlternating (fun μ ↦ ∑ c • N) = ...`.
Does mathlib already have a canonical form for this idea? yes: `MultilinearMap.map_sum_finset` (form b/c).
Is our statement stated against the canonical form? yes for a local helper (LHS is the matrix as it arises at the call site, RHS the expanded sum).
RHS convention respected? yes

### Syntactic generality — `Roth.det_sum_rows`

Alternative restatements attempted:
- over `[Fintype n] [DecidableEq n]` (compiles; `det_sum_rows_gen`)
- without scalars, `g μ i` rows (compiles; one-call `map_sum_finset`)
Chosen restatement: current (with scalars), optionally over a general `n`.
Justification: the single call site has rows `c μ d * kronecker k (hasseDeriv d (φ ν))` and wants `∏ c` pulled out; the scalar form is what the `simpa` consumes.

### Superfluous-argument audit — `Roth.det_sum_rows`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing A]` | yes | required by `Matrix.det` |
| 2 | `Fin l` (implicit `l`) | no (as a specific type) | any `[Fintype n] [DecidableEq n]` works (evidence) |
| 3 | `s`, `c`, `N` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (optional `Fin l` to general `n`)
Superfluous arguments: NONE (the `Fin l` specialisation is cosmetic, not a hypothesis)

Overall: SHIP-AS-STATED (locally; nothing ships to mathlib)

### Call sites — `Roth.det_sum_rows`

Internal use count: 0 outside the declaring file; 1 inside Roth/GenWronskian.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:245 | `simpa [wronskian, wronskianMatrix, hc, genWronskian, AlgHom.map_det, Matrix.map] using det_sum_rows s c (fun μ d ν ↦ kronecker k (hasseDeriv d (φ ν)))` |

Inline-derivation grep (`grep -rn "map_sum_finset\|map_smul_univ\|detRowAlternating" Roth/`):
  - (none besides the proof of `det_sum_rows` itself)

### Composition check (Phase 6)

Can `Roth.det_sum_rows` be derived from mathlib in ≤3 chained calls?

Attempt 1 (current proof): `MultilinearMap.map_sum_finset` on `(Matrix.detRowAlternating).toMultilinearMap` with rows `c μ i • N μ i`, then `MultilinearMap.map_smul_univ`, then unfold `Matrix.det`/`Matrix.of` by `simp only`.
  - Mathlib decls used: `MultilinearMap.map_sum_finset`, `MultilinearMap.map_smul_univ`, `Matrix.detRowAlternating`
  - Result: succeeds (evidence example 1, for a general `Fintype n`)

Attempt 2 (scalar-free variant): `(Matrix.detRowAlternating).toMultilinearMap.map_sum_finset g s`, a single term.
  - Result: succeeds (evidence example 3)

Attempt 3 (one-shot `simpa [map_smul_univ, Matrix.det, Finset.sum_fn] using this`, and `simp only ... at this; exact this`):
  - Result: fails on the `Matrix.of` wrapper (the goal keeps `Matrix.of`, the hypothesis does not); needs the `simp only [Matrix.det, ...] at h ⊢` step of attempt 1. Discarded from the evidence file.

Conclusion: COMPOSABLE (3 mathlib steps; borderline "trivial simp composition" in the sense of 6b)

## Verdict: `Roth.det_sum_rows`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the standard multilinear expansion over choice functions (LSU / UW notes, Leibniz-formula derivation); paper clean.tex l.331 invokes exactly "multilinearity of the determinant in each row".
- Generality analysis (Phase 4): narrower than standard; the general form is `MultilinearMap.map_sum_finset` (in mathlib); `Fin l` to `Fintype n` verified.
- Mathlib search (Phase 5): building blocks found (`MultilinearMap.map_sum_finset`, `MultilinearMap.map_smul_univ`, `Matrix.detRowAlternating`); no det-specific lemma (checked `Matrix.det_updateRow_sum`, `Matrix.det_updateRow_add`, `Matrix.det_mul`, `Matrix.det_sum_le`, `Matrix.det_sum_smul_le`).
- Composition check (Phase 6): COMPOSABLE.

**Rationale:**

The statement is the determinant instance of the generic expansion of a multilinear map on sums, which mathlib has as `MultilinearMap.map_sum_finset`; with scalars pulled out by `MultilinearMap.map_smul_univ` and `Matrix.det` unfolded to `detRowAlternating`, the identity is the project's current 4-line proof, which compiles verbatim for an arbitrary finite row type. None of mathlib's determinant row lemmas (`det_updateRow_sum`, `det_updateRow_add`, `det_mul`) states the choice-function expansion, so a `Matrix.det_of_sum_rows` wrapper would be new, but it adds no content beyond the multilinear-map lemma, and the project has a single (private) consumer.

WHY not: composable from mathlib's multilinear-map API in three steps; no new mathematics. Belongs-elsewhere check: keep in Roth/GenWronskian.lean next to its single consumer `wronskian_kronecker_eq_sum_aux`; it records the paper's "multilinearity in each row" step.

Mathlib building blocks:      `MultilinearMap.map_sum_finset` (Mathlib/LinearAlgebra/Multilinear/Basic.lean:620), `MultilinearMap.map_smul_univ` (Mathlib/LinearAlgebra/Multilinear/Basic.lean:1161), `Matrix.detRowAlternating` (Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean)
Composition sketch (≤3 lines):
```lean
  have h := (Matrix.detRowAlternating (R := A) (n := n)).toMultilinearMap.map_sum_finset
    (fun μ i ↦ c μ i • N μ i) s
  simp_rw [MultilinearMap.map_smul_univ, smul_eq_mul] at h
  simp only [Matrix.det, Finset.sum_fn, Pi.smul_def, smul_eq_mul] at h ⊢; exact h
```
Call sites in our project (from Phase 6.0):  1 (Roth/GenWronskian.lean:245)
Refactor plan: none required. Inlining at Roth/GenWronskian.lean:245 is possible (replace `using det_sum_rows s c (...)` by the 3-step composition followed by the existing `simpa`), but keeping the named helper is clearer; optionally generalise `Fin l` to `{n : Type*} [Fintype n] [DecidableEq n]` (same proof).
Next action: do not upstream; keep `Roth.det_sum_rows` locally.

---

## Next step

No mathlib action. Keep `Roth.det_sum_rows` as a local helper (optionally over a general `Fintype` index); its content is `MultilinearMap.map_sum_finset` + `MultilinearMap.map_smul_univ` for `Matrix.detRowAlternating`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.det_sum_rows/det_sum_rows_exp.lean` (imports `Roth.GenWronskian`; `lake env lean` exit 0, no output): (1) `det_sum_rows_gen` over `[Fintype n] [DecidableEq n]` with the original proof verbatim; (2) the original `Fin l` statement as `det_sum_rows_gen s c N`; (3) scalar-free form as a single `MultilinearMap.map_sum_finset` term.
- Earlier runs of the same file (overwritten) contained a 4th example, a one-shot `simpa [MultilinearMap.map_smul_univ, Matrix.det, Finset.sum_fn] using this` and a `simp only ... at this; exact this` variant; both failed with type mismatches on the `Matrix.of` wrapper, so the example was removed.
- Mathlib greps listed in [D]; Loogle (1), LeanSearch (1), Lean-Finder (1) as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.331).
- Project grep `grep -rn det_sum_rows Roth/` and `grep -rn "map_sum_finset\|map_smul_univ\|detRowAlternating" Roth/` for the call-sites table.
