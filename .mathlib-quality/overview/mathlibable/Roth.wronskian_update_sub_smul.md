---
decl: Roth.wronskian_update_sub_smul
file: Roth/Wronskian.lean
line: 158
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Column-operation invariance of the n-ary Wronskian is a basic missing fact once the n-ary Wronskian (mathlib TODO) is upstreamed; [Field K] weakens to [CommRing R] verbatim and the literature-standard form W(phi A) = det A * W(phi) (stated in the project source itself) is verified, with this lemma as the transvection case.
action: Upstream with Roth.wronskian to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R], adding the change-of-basis lemma (wronskian of sum A rho nu smul phi rho = C (det A) * wronskian phi, verified) and this transvection lemma (preferably in the smul/add spelling); locally keep (call site Roth/Wronskian.lean:212).
---

# Roth.wronskian_update_sub_smul

## Inventory entry

### `theorem Roth.wronskian_update_sub_smul`
- **Type**: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) : wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ`
- **What**: Replacing `φ ν'` by `φ ν' - c φ ν` (constant `c`, `ν ≠ ν'`) does not change the Wronskian `det (D^{(μ)} φ_ρ)`.
- **How**: The new Wronskian matrix is `(wronskianMatrix φ).updateCol ν' (col ν' + (-C c) • col ν)` (entrywise by `Matrix.updateCol_apply`, `Function.update_apply`, linearity of `hasseDeriv`, `smul_eq_C_mul`); then `Matrix.det_updateCol_add_smul_self`.
- **Hypotheses**: `[Field K]` (section variable); `h : ν ≠ ν'`; `c : K`.
- **Uses from project**: `Roth.wronskian`, `Roth.wronskianMatrix`
- **Used by**: Roth/Wronskian.lean:212 (`wronskian_ne_zero_of_linearIndependent`, induction step on total degree). No other project use (also mentioned in the module docstring l.38).
- **Visibility**: public
- **Lines**: 158–164, proof length 5 lines
- **Notes**: Companion of `linearIndependent_update_sub_smul` (l.170). The source (§2, clean.tex l.179–180) states the general form `W(g) = W(φ) det A` for a constant change of basis `A`; the project only formalises the transvection case it needs.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Wronskian.lean:212), the reduction step of the hard direction of the Wronskian criterion.
- Wrapper of 1–2 mathlib calls? Close: `Matrix.det_updateCol_add_smul_self` plus an entrywise `simp` identification of the updated matrix. The identification step is the content (it needs `hasseDeriv` linearity and the `Function.update`/`updateCol` bridge), so it is not a bare wrapper.
- Does mathlib have it? No: only the 2-ary `Polynomial.wronskian` with `wronskian_add_left/right`, bilinearity and `isAlt_wronskianBilin` exist; no n-ary Wronskian.
- Too specific (inline?)? Inlining at the single call site is possible, but it is the natural API lemma for the n-ary Wronskian (its 2-ary analogue follows from `isAlt_wronskianBilin` + bilinearity), so keep.
- Well-chosen? Yes; only `[Field K]` is stronger than needed, and the general change-of-basis form would be better API.
- Conclusion: `KEEP` — action: keep; when upstreaming, generalise to `[CommRing R]` and add the `det A` change-of-basis lemma.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring does not start internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `update_sub_smul` over `.lake/packages/mathlib/Mathlib/` only hits `Submodule.span_range_update_sub_smul`, a different decl). Not a glue lemma (5-line proof with a real computation), so the full workflow is run; parent defs `Roth.wronskian` / `Roth.wronskianMatrix` are YES-but-generalise-first and their evidence is reused.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.wronskian_update_sub_smul`: resolved at Roth/Wronskian.lean:158
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskian_update_sub_smul` is a theorem stating: for polynomials `φ_0, …, φ_{l-1} ∈ K[t]`, indices `ν ≠ ν'` and a constant `c ∈ K`, the Wronskian `det (D^{(μ)} φ_ρ)` of the family obtained by replacing `φ_{ν'}` with `φ_{ν'} - c φ_ν` equals the Wronskian of the original family. In other words, an elementary (transvection) column operation with constant coefficients leaves the Wronskian unchanged.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]` — coefficient field.
- `l : ℕ` — number of polynomials.
- `φ : Fin l → K[X]` — the family.
- `ν ν' : Fin l` — source and target column of the operation.
- `c : K` — the constant multiplier.

Hypotheses (Lean side):
- `h : ν ≠ ν'` — the operation adds a multiple of a different column.

Conclusion (math): `W(φ_0, …, φ_{ν'} - c φ_ν, …, φ_{l-1}) = W(φ_0, …, φ_{l-1})`.

Conclusion (Lean): `wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper lemma for the induction in `wronskian_ne_zero_of_linearIndependent`; not a main result, not a new structure, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5 substantive lines
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian invariant under elementary column operations adding constant multiple of one function | partial | adding a constant multiple of one function to another leaves the Wronskian unchanged (derivation is linear; column operation on the determinant) | no source states it as a named result; folklore; MIT 18.03 notes, arXiv 2410.18867 surfaced |
| 2 | WebSearch (general form) | Wronskian of linear transformation of functions W(Af) = det(A) W(f) constant matrix | yes | `W(f A) = det(A) W(f)` for a constant matrix `A`, over a commutative ring | arXiv 2007.04045 ("With Wronskian through the Looking Glass"); UBC / UPenn course notes |
| 3 | WebSearch (named-after / aliases) | Hasse derivative Wronskian change of basis det constant matrix polynomials span | yes | change of basis `T` acts by right multiplication, Wronskian scales by `det T`; Hasse vs ordinary Wronskian differ by a constant | arXiv 1404.4506 (Hasse Wronskians, linear matroids); Berkeley Math H54 solutions; arXiv 2511.12337 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §2 first lemma, l.174–180 | yes | "If `A ∈ GL_l(ℚ)` is this change-of-basis matrix, then `W(g) = W(φ) det A`" | the project's own source states the general change-of-basis form; the Lean lemma is its transvection case |
| 6 | nLab | Wronskian | no | — | no nLab page on Wronskians (checked for the parent `Roth.wronskian`) |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not a scheme-theoretic statement |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | partial | only elementary exercises ("Wronskian of a basis change is a constant multiple") | textbook folklore, no dedicated thread |
| 10 | recent arXiv (last 5 years) | results of #2/#3 | yes | arXiv 2007.04045 (2020), 2410.18867 (2024) use `W(fA) = det A · W(f)` freely | confirms the standard general form |

### Literature summary (Phase 3)

Concept identified as: behaviour of the Wronskian under a constant linear change of the family (column operations).
Sources agree on the standard form: yes — `W(φ A) = det(A) · W(φ)` for a constant matrix `A`; elementary column operations are special cases (transvections preserve `W`, scaling by `c` multiplies by `c`).
Most general standard form: for `φ : Fin l → R[X]` over a commutative ring `R` and `A ∈ M_l(R)`, `W(fun ν ↦ ∑_ρ A ρ ν φ ρ) = det A · W(φ)` (holds for any linear derivation/Hasse–Schmidt system, since the Wronskian matrix transforms by right multiplication by `A`).
Generality dimensions where the literature varies:
  - coefficients: real/complex functions to any commutative ring (no division needed).
  - operation: single transvection to arbitrary constant matrix `A`.
  - derivative: ordinary vs Hasse (only linearity matters).
Disagreement with the literature: none; the Lean lemma is a specialisation (transvection, field coefficients).

### Generality analysis — `Roth.wronskian_update_sub_smul`

Literature-standard form (from Phase 3): `wronskian (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskian φ` over `[CommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative ring | yes | `Matrix.det_updateCol_add_smul_self` needs only `[CommRing]`; verified: project proof compiles verbatim over `[CommRing R]` (evidence (1)) |
| 2 | `[CommRing R]` to `[CommSemiring R]` | — | — | NO | the statement uses subtraction; even the `add` variant needs `det_updateCol_add_smul_self`, stated for `CommRing` (alternating-map argument) |
| 3 | `h : ν ≠ ν'` | distinct indices | distinct indices | NO | necessary: with `ν = ν'`, `c = 1` the family `![1]` becomes `![0]` and the Wronskian drops from `1` to `0` (evidence (4), verified) |
| 4 | single transvection `φ ν' - C c * φ ν` | elementary operation | arbitrary constant matrix `A`, factor `det A` | yes (generalisation of content) | verified: `wronskian_mul_matrix` (evidence (5)) proves the `det A` form over `[CommRing R]` in 6 lines via `Matrix.det_mul` and `RingHom.map_det`; the source itself states this form |
| 5 | `c : K` constant (vs `c : R[X]`) | constant | constant | NO | `hasseDeriv` is only `R`-linear; a polynomial multiplier would not commute with the derivatives |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (`[Field K]` to `[CommRing R]`, verified with the proof verbatim; transvection to general constant matrix `A` with factor `det A`, verified with a new 6-line proof). Both checked clean via `lean_diagnostic_messages` on the evidence file.
Proposed restatement:

```lean
theorem Polynomial.wronskianDet_mul_matrix {R : Type*} [CommRing R] {l : ℕ}
    (φ : Fin l → R[X]) (A : Matrix (Fin l) (Fin l) R) :
    wronskianDet (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskianDet φ

theorem Polynomial.wronskianDet_update_add_smul {R : Type*} [CommRing R] {l : ℕ}
    {φ : Fin l → R[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : R) :
    wronskianDet (Function.update φ ν' (φ ν' + c • φ ν)) = wronskianDet φ
```
(`wronskianDet` = placeholder n-ary name chosen when upstreaming the parent def; the project's `sub`/`C c *` spelling stays available as a corollary or via `sub_eq_add_neg`/`smul_eq_C_mul`.)

Cost of restatement: CHEAP — both verified in the evidence file.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled preamble |
| 2 | sequences to filters? | no | — | finite algebraic identity |
| 3 | construction vs universal property? | no | — | an identity |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R]` (Phase 4a row 1) | integral Wronskians, consistency with the `CommRing` parent def |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | `Fin l` inherited from the square Wronskian matrix | — |
| 8 | concrete-via-abstract? | partial | proof uses only `R`-linearity of each `hasseDeriv μ`; the abstract fact is "for linear maps `L_μ`, `det (L_μ (∑ A ρ ν • φ ρ)) = det A · det (L_μ (φ ν))`", which is `Matrix.det_mul` after one rewrite; the `det A` form (row 4 of 4a) already captures it | `wronskianDet_mul_matrix` would also give `smul` scaling (`A` diagonal), permutation sign (`A` a permutation matrix) and transvections at once |
| 9 | false-generalisation guard | no false generalisation | `[CommRing R]` and the `det A` form are statements about the same Wronskian; the project lemma is a direct specialisation (evidence (3) and the transvection case of (5) via `det` of a transvection being 1) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `wronskianDet_mul_matrix` (the `det A` form) as the main lemma, with `wronskianDet_update_add_smul` as the elementary-operation corollary, both over `[CommRing R]`.
  - Cost: CHEAP
  - Mathlib downstream this enables: n-ary analogues of `Polynomial.wronskian_add_left/right`-style manipulations; invariance of the Wronskian of a basis of a subspace up to a unit (the classical "Wronskian of a linear system" notion); reduction to distinct-degree families in the char-0 independence criterion.
  - Real mathematical improvement: one lemma covers all elementary column operations and arbitrary changes of basis, which is exactly the form the source paper uses.

### Proof strategy — `Roth.wronskian_update_sub_smul`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partial | with `wronskianDet_mul_matrix` in place, the transvection lemma is a corollary (det of a transvection is 1, `Matrix.det_transvection_of_ne`); either route is short | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (identify the updated matrix, apply `Matrix.det_updateCol_add_smul_self`; 5 lines).
  - Optional: derive it from the general `det A` lemma when upstreaming, or keep the direct proof (both are short).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.wronskian_update_sub_smul`

[A] Lean-Finder       "Wronskian unchanged when adding a constant multiple of one polynomial to another"   only 2-ary `Polynomial.wronskian_add_left/right`, `wronskian_eq_of_sum_zero`, `wronskianBilin_apply`, `isAlt_wronskianBilin`
[B] Loogle            `Polynomial.wronskian, Function.update`   no hits
[C] LeanSearch        "determinant unchanged when adding a multiple of one column to another column"   building blocks `Matrix.det_updateCol_add_smul_self`, `det_updateCol_add_self`, `det_updateCol_sum`, `det_eq_of_forall_col_eq_smul_add_pred` (all `[CommRing R]`)
[D] Grep mathlib src  `wronskian` with `add|update|smul|sub` (only 2-ary lemmas in RingTheory/Polynomial/Wronskian.lean l.67–81 and FLT/MasonStothers.lean); `update_sub_smul` (only `Submodule.span_range_update_sub_smul`, Span/Defs.lean:652); `det_updateCol_add_smul_self` (Determinant/Basic.lean:478)   no n-ary Wronskian hit
[E] Name pattern      `Roth.wronskian_update_sub_smul`, `wronskian_update`   absent from mathlib

Searched for both the user's form (transvection over a field) and the literature-standard form (`det A` change of basis over a commutative ring).

Concluded: found building blocks (`Matrix.det_updateCol_add_smul_self`, `Matrix.det_mul`, `RingHom.map_det`); the statement itself is not in mathlib (no n-ary Wronskian exists; `Mathlib/RingTheory/Polynomial/Wronskian.lean` TODO).

### Normal-form check — `Roth.wronskian_update_sub_smul`

Equivalent formalisms: `update φ ν' (φ ν' - C c * φ ν)`; `update φ ν' (φ ν' + c • φ ν)`; general `fun ν ↦ ∑ ρ, A ρ ν • φ ρ` with factor `det A`.
Does mathlib already have a canonical form? For matrices, mathlib's canonical elementary-operation lemma is `Matrix.det_updateCol_add_smul_self` (`A k i + c • A k j`, `smul`, `add`) and the general one is `Matrix.det_mul`.
Proposed canonical form: mirror mathlib: `update φ ν' (φ ν' + c • φ ν)` (add + smul) for the elementary lemma, `det A` form for the general one; the project's `sub`/`C c *` form is a corollary.
RHS convention respected? yes (equation with the simpler side `wronskian φ` on the RHS)

### Syntactic generality — `Roth.wronskian_update_sub_smul`

Alternative restatements attempted:
- current: `φ ν' - C c * φ ν` (verified over `[CommRing R]`)
- `φ ν' + c • φ ν` (verified over `[CommRing R]`, evidence (2))
- `fun ν ↦ ∑ ρ, A ρ ν • φ ρ` with `C A.det` factor (verified, evidence (5))
Chosen restatement: the `det A` form as main lemma plus the `add`/`smul` elementary form.
Justification: matches mathlib's `Matrix.det_updateCol_add_smul_self` spelling so users can transfer intuition; the `det A` form is what the source uses and subsumes all elementary operations.

### Superfluous-argument audit — `Roth.wronskian_update_sub_smul`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R]` suffices (verified) |
| 2 | `h : ν ≠ ν'` | yes | counterexample with `ν = ν'` (verified) |
| 3 | `c` | yes | the multiplier |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (prefer the mathlib-style `φ ν' + c • φ ν` spelling upstream)
Syntactic generality: RESTATE (add the `det A` change-of-basis lemma)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[CommRing R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskian_update_sub_smul`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:212 | `rw [← wronskian_update_sub_smul hne ((φ ν').leadingCoeff / (φ ν).leadingCoeff)]` (in `wronskian_ne_zero_of_linearIndependent`) |

Inline-derivation grep: `grep -rn "det_updateCol\|update_sub_smul\|RingHom.map_det" Roth/` finds no re-derivation of this column-operation argument; `RingHom.map_det`/`Matrix.det_mul` uses in Roth/Separation.lean:359/529 and Roth/Theta.lean:522/579 concern different determinants. (none)

### Composition check (Phase 6)

Can `Roth.wronskian_update_sub_smul` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(congrArg Matrix.det ?_).trans (Matrix.det_updateCol_add_smul_self (wronskianMatrix φ) h.symm (-C c))`.
  - Mathlib decls used: `Matrix.det_updateCol_add_smul_self`
  - Result: partial — the remaining goal (the Wronskian matrix of the updated family is the column-updated matrix) needs an `ext` + `simp` with `hasseDeriv` linearity, `Function.update_apply`, `Matrix.updateCol_apply`, `smul_eq_C_mul`: a real computation.

Attempt 2: via the general `det A` lemma and `Matrix.det_transvection_of_ne`.
  - Result: requires the (new) `det A` lemma, itself a proof with a nontrivial `simp` step; not a mathlib call chain.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.wronskian_update_sub_smul`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard `W(φA) = det A · W(φ)` (arXiv 2007.04045, Berkeley/UBC notes, arXiv 1404.4506 for Hasse Wronskians), stated verbatim in the project source §2 (clean.tex l.179–180).
- Generality analysis (Phase 4): STRICTLY NARROWER — `[Field K]` to `[CommRing R]` verified with the proof verbatim; the `det A` generalisation verified; `ν ≠ ν'` necessary (verified counterexample).
- Mathlib search (Phase 5): building blocks only (`Matrix.det_updateCol_add_smul_self`, `Matrix.det_mul`, `RingHom.map_det`); no n-ary Wronskian in mathlib (TODO at `Mathlib/RingTheory/Polynomial/Wronskian.lean`).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The gap is the n-ary Wronskian itself. `Mathlib/RingTheory/Polynomial/Wronskian.lean` has only `W(a, b)` and lists the n-tuple version as a TODO. The parent def `Roth.wronskian` is assessed YES-but-generalise-first for that file, and a lemma saying how the Wronskian changes under a constant change of the family belongs in its basic API. The 2-ary file has the corresponding facts (`wronskian_add_left/right`, `isAlt_wronskianBilin`, `wronskian_eq_of_sum_zero`). The literature, including the project's own source, uses the general form `W(φA) = det A · W(φ)`, and the Lean lemma is its transvection case. Without the identification of the updated Wronskian matrix (the `simp` step), mathlib's `Matrix.det_updateCol_add_smul_self` does not apply directly.

The current statement is narrower than it needs to be in two verified ways. First, nothing in the proof uses division: it compiles verbatim over `[CommRing R]`. Second, the general change-of-basis lemma `wronskian (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskian φ` has a 6-line proof via `Matrix.det_mul` and `RingHom.map_det` (evidence (5)). The hypothesis `ν ≠ ν'` cannot be dropped (evidence (4)).

Reason for the generalisation: LITERATURE-WEAKENING (field to commutative ring; transvection to arbitrary constant matrix with factor `det A`) and MODERN-IDIOM (spelling `φ ν' + c • φ ν` to mirror `Matrix.det_updateCol_add_smul_self`).
Proposed restatement:
```lean
theorem Polynomial.wronskianDet_mul_matrix {R : Type*} [CommRing R] {l : ℕ}
    (φ : Fin l → R[X]) (A : Matrix (Fin l) (Fin l) R) :
    wronskianDet (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskianDet φ := by
  sorry -- verified in evidence (5)
theorem Polynomial.wronskianDet_update_add_smul {R : Type*} [CommRing R] {l : ℕ}
    {φ : Fin l → R[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : R) :
    wronskianDet (Function.update φ ν' (φ ν' + c • φ ν)) = wronskianDet φ := by
  sorry -- verified in evidence (2)
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- the n-ary analogue of the 2-ary bilinearity/alternation API (`wronskian_add_left/right`, `isAlt_wronskianBilin`): elementary column operations, scaling (`A` diagonal) and permutation sign (`A` a permutation matrix) all come from one lemma;
- the Wronskian of a basis of a finite-dimensional space of polynomials is well defined up to a unit (factor `det A`, `A` invertible);
- the reduction to distinct-degree families in the char-0 independence criterion (`Roth.wronskian_ne_zero_of_linearIndependent`, follow-up PR).
PR grouping: same PR as `Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent` (n-ary Wronskian over `[CommRing R]` in `Mathlib/RingTheory/Polynomial/Wronskian.lean`); `Roth.linearIndependent_update_sub_smul` is its natural companion for the criterion PR.
Next action: run `/generalise Roth.wronskian_update_sub_smul` (target `[CommRing R]`, `add`/`smul` spelling, plus the `det A` lemma), then ship with the parent defs; locally keep the call site Roth/Wronskian.lean:212 unchanged.

---

## Next step

Run `/generalise Roth.wronskian_update_sub_smul`, targeting `[CommRing R]` and adding the change-of-basis lemma `wronskian (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskian φ`. Then upstream both with the n-ary Wronskian PR to `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskian_update_sub_smul/weaken_commring.lean`, checked with `lean_diagnostic_messages`: clean, no errors or warnings, after two fix iterations of the new lemmas (the `simp` sets for (2) and (5) were adjusted; (1) compiled verbatim on the first check). It verifies: (1) the theorem over `[CommRing R]`, with the project proof verbatim; (2) the `φ ν' + c • φ ν` variant over `[CommRing R]`; (3) the project theorem is a specialisation of (1); (4) `ν ≠ ν'` is necessary (`ν = ν' = 0`, `c = 1`, `φ = ![1]` over `ℚ`); (5) the general change-of-basis lemma `wronskian (fun ν ↦ ∑ ρ, A ρ ν • φ ρ) = C A.det * wronskian φ` over `[CommRing R]`.
- WebSearch: 3 queries, summarised in the literature table. ChatGPT MCP: n/a (not configured).
- Lean-Finder, LeanSearch and Loogle queries and the mathlib greps are recorded in Phase 5.
- Project greps: `grep -rn wronskian_update_sub_smul Roth/` found 1 call site (l.212) plus the docstring mention (l.38). `grep -rn "det_updateCol\|update_sub_smul\|RingHom.map_det" Roth/` found no re-derivation of this argument.
