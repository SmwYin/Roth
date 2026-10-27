---
decl: Roth.exists_coeffNone_basis_aux
file: Roth/Separation.lean
line: 291
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-use helper of exists_separated_representation producing a finite basis of the span of the x_none-coefficients of a nonzero P with 1 <= l <= n+1 and per-variable degree bounds; Lemma 2 bookkeeping with no mathlib counterpart.
action: Keep as private helper for its single call site Roth/Separation.lean:336 (exists_separated_representation); no change needed.
---

# Roth.exists_coeffNone_basis_aux

## Inventory entry

### `theorem Roth.exists_coeffNone_basis_aux`
- **Type**: `∀ {τ : Type*} {K : Type*} [Field K] {P : MvPolynomial (Option τ) K}, P ≠ 0 → ∀ {n : ℕ}, (P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (coeffNone P ν)) → ∃ l, ∃ b : Module.Basis (Fin l) K (Submodule.span K (Set.range (fun ν : Fin (n + 1) ↦ coeffNone P ν))), 1 ≤ l ∧ l ≤ n + 1 ∧ ∀ ρ j, degreeOf j (b ρ : MvPolynomial τ K) ≤ degreeOf (some j) P` (declared `private lemma`; section variables `[Fintype τ] [DecidableEq τ]` omitted).
- **What**: For a nonzero `P = ∑_{ν ≤ n} x_none^ν c_ν(x_τ)` over a field (with `c_ν = coeffNone P ν`), the span `V` of `c_0, …, c_n` has a basis `b_1, …, b_l` with `1 ≤ l ≤ n + 1`, and every basis vector has degree in `x_j` at most `degreeOf (some j) P`. This is the basis-choice step of the separated decomposition in §2, proof of Lemma 2.
- **How**: `V` is finite-dimensional by `FiniteDimensional.span_of_finite`; take `b := Module.finBasis K V`, so `l = finrank K V`. `1 ≤ l`: some `c_ν ≠ 0` (else `hP'` with `simp` forces `P = 0`), then `Module.finrank_pos_iff_exists_ne_zero`. `l ≤ n + 1`: `finrank_range_le_card` and `Fintype.card_fin`. Degree bound: `V ≤ restrictSupport K {d | ∀ j, d j ≤ degreeOf (some j) P}` by `Submodule.span_le` + `Set.range_subset_iff`, each generator handled with `mem_support_coeff_optionEquivLeft` and `monomial_le_degreeOf`; then `degreeOf_le_iff` applied to `(b ρ).2`.
- **Hypotheses**: `[Field K]` (needed for finite-dimensionality/`finBasis` and `finrank_pos`; a free-module version over a PID would also work but is not needed); `hP : P ≠ 0` (essential for `1 ≤ l`); `hP'` the expansion of `P` in powers of `x_none` up to `n` (used only to derive some `c_ν ≠ 0`; it encodes `degreeOf none P ≤ n`). The degree bound and `l ≤ n + 1` do not need `hP'`. No redundant hypotheses for the statement as consumed.
- **Uses from project**: `Roth.coeffNone` (Roth/Separation.lean:80, defined as `(optionEquivLeft R τ P).coeff ν`, which is why the mathlib lemma `MvPolynomial.mem_support_coeff_optionEquivLeft` applies after unfolding). All other identifiers (`restrictSupport`, `monomial_le_degreeOf`, `degreeOf_le_iff`, `finrank_range_le_card`, `Module.finBasis`, `Module.finrank_pos_iff_exists_ne_zero`, `FiniteDimensional.span_of_finite`) are mathlib (checked by grep in `.lake/packages/mathlib/Mathlib/`).
- **Used by**: Roth/Separation.lean:336 `Roth.exists_separated_representation` only (`obtain ⟨l, b, hl1, hl2, hdegree⟩ := exists_coeffNone_basis_aux hP hP'`); `grep -rn exists_coeffNone_basis_aux Roth/` returns only the definition (l.291) and this use.
- **Visibility**: private
- **Lines**: 290–316 (including the `omit` line), proof length 21 lines
- **Notes**: Name ends in `_aux`, no docstring (usual for private helpers). Part of a clean three-helper split of `exists_separated_representation` (basis existence here, linear independence in `linearIndependent_coordinate_polynomials_aux`, identity in `eq_sum_aeval_basis_coeffNone_aux`). The basis type is stated on the exact submodule the other two helpers expect, so they plug together in one `refine`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Separation.lean:336 inside the public `exists_separated_representation`.
- Wrapper of 1–2 mathlib calls? No. It combines `Module.finBasis`, a positivity-of-finrank argument, `finrank_range_le_card`, and a support-restriction argument through `restrictSupport` (21 lines).
- Does mathlib have it? No. `lean_leansearch` for a basis of a span of polynomials respecting a support bound returned `MvPolynomial.basisRestrictSupport`, `MvPolynomial.restrictSupport`, `Module.Basis.ofSpan_subset`, `Module.Basis.mem_span_image` and similar generic ingredients; none states this. The statement is phrased via the project def `coeffNone` and the specific `degreeOf (some j) P` bound, so no mathlib lemma could match it verbatim. The generic content (a basis of a submodule contained in `restrictSupport s` consists of elements of `restrictSupport s`) is a one-liner from `Submodule.span_le` and membership, already what the proof does.
- Too specific / inline? Very specific to Lemma 2, but inlining it into `exists_separated_representation` would lengthen an already long `refine`; the current split is readable. Already private.
- Well-chosen? Yes. Minor possible simplification (not required): the existence of a nonzero `c_ν` could be derived from `P ≠ 0` without `hP'`, but `hP'` is already available at the call site, so passing it is cheaper.
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:291; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent: if `exists_separated_representation` is ever upstreamed, this helper travels with it (with `coeffNone` replaced by `(optionEquivLeft K τ P).coeff ν`).

## Evidence
- `grep -rn exists_coeffNone_basis_aux Roth/`: definition l.291, single use l.336.
- `grep` in `.lake/packages/mathlib/Mathlib/` confirmed `restrictSupport` (RingTheory/MvPolynomial/Basic.lean:93), `mem_support_coeff_optionEquivLeft` (Algebra/MvPolynomial/Equiv.lean:549), `monomial_le_degreeOf` (Algebra/MvPolynomial/Degrees.lean:268), `degreeOf_le_iff` (same file:235), `finrank_range_le_card` (LinearAlgebra/Dimension/Constructions.lean:451), `Module.finBasis` (LinearAlgebra/Dimension/Free.lean:334), `FiniteDimensional.span_of_finite` (LinearAlgebra/FiniteDimensional/Defs.lean:199) are mathlib; `Roth.coeffNone` (Roth/Separation.lean:80) is the only project identifier in the body.
- `lean_leansearch` (one query, 6 results, described above): no match.
- No Lean runs and no evidence Lean files. A private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
