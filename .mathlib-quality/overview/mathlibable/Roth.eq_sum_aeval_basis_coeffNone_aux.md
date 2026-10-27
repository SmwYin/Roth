---
decl: Roth.eq_sum_aeval_basis_coeffNone_aux
file: Roth/Separation.lean
line: 265
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-use helper of exists_separated_representation that regroups P = sum_nu x_none^nu coeffNone P nu, after expanding each coeffNone P nu in a basis of their span, as sum_rho phi_rho(x_none) psi_rho(x_tau); a bookkeeping rearrangement specific to Lemma 2 with no mathlib counterpart.
action: Keep as private helper for its single call site Roth/Separation.lean:342 (exists_separated_representation); no change needed.
---

# Roth.eq_sum_aeval_basis_coeffNone_aux

## Inventory entry

### `theorem Roth.eq_sum_aeval_basis_coeffNone_aux`
- **Type**: `∀ {τ : Type*} {R : Type*} [CommSemiring R] {P : MvPolynomial (Option τ) R} {n l : ℕ}, (P = ∑ ν : Fin (n + 1), X none ^ (ν : ℕ) * rename some (coeffNone P ν)) → ∀ (b : Module.Basis (Fin l) R (Submodule.span R (Set.range (fun ν : Fin (n + 1) ↦ coeffNone P ν)))), P = ∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) R) (∑ ν : Fin (n + 1), Polynomial.C (b.repr ⟨coeffNone P ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ) * Polynomial.X ^ (ν : ℕ)) * rename some (b ρ : MvPolynomial τ R)` (declared `private lemma`; section variables `[Fintype τ] [DecidableEq τ]` omitted, the section's field `K` unused, its own `R` introduced locally).
- **What**: Suppose `P = ∑_{ν ≤ n} x_none^ν · c_ν(x_τ)` where `c_ν = coeffNone P ν`, and let `b_1, …, b_l` be a basis of the `R`-span of `c_0, …, c_n`, with `c_ν = ∑_ρ a_{νρ} b_ρ`. Then `P = ∑_ρ φ_ρ(x_none) · b_ρ(x_τ)` where `φ_ρ(X) = ∑_ν a_{νρ} X^ν`. This is the identity part of the separated decomposition in §2, proof of Lemma 2 (swap the order of summation after expanding each coefficient polynomial in the basis).
- **How**: Names `a ν ρ` for the coordinates; proves `hexp : coeffNone P ν = ∑ ρ, a ν ρ • b ρ` from `Module.Basis.sum_repr` pushed through `Subtype.val` (`Submodule.coe_sum`, `Submodule.coe_smul`). Rewrites the LHS with `hP`, then `simp_rw [hexp, map_sum, Finset.mul_sum]`, `Finset.sum_comm`, `Finset.sum_mul`, and termwise `map_smul`, `smul_eq_C_mul`, `map_mul`, `Polynomial.aeval_C`, `algebraMap_eq`, `map_pow`, `Polynomial.aeval_X`, closing with `ac_rfl`.
- **Hypotheses**: `[CommSemiring R]` only (more general than the caller's field `K`); `hP` the expansion of `P` in powers of `x_none` up to degree `n` (supplied by the caller from `eq_sum_X_none_pow_mul_coeffNone`); `b` any finite basis of the span. No redundant hypotheses: `hP` is essential (it encodes `degreeOf none P ≤ n`).
- **Uses from project**: `Roth.coeffNone` (Roth/Separation.lean:80). Everything else is mathlib.
- **Used by**: Roth/Separation.lean:342 `Roth.exists_separated_representation` only (supplies the final identity `P = ∑ ν, aeval (X none) (φ ν) * rename some (ψ ν)`); `grep -rn eq_sum_aeval_basis_coeffNone_aux Roth/` returns only the definition (l.265) and this use.
- **Visibility**: private
- **Lines**: 264–288 (including the `omit` line), proof length 16 lines
- **Notes**: Name ends in `_aux`, no docstring (usual for private helpers). The subtype term `⟨coeffNone P ν, Submodule.subset_span ⟨ν, rfl⟩⟩` and the `φ_ρ` expression match the caller and `linearIndependent_coordinate_polynomials_aux` syntactically, so the three pieces plug together in one `refine`. The `change` step merely unfolds the local `a`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Separation.lean:342 inside the public `exists_separated_representation`.
- Wrapper of 1–2 mathlib calls? No. It is a 16-line sum rearrangement (basis expansion via `Module.Basis.sum_repr`, `Finset.sum_comm`, evaluation lemmas for `Polynomial.aeval`).
- Does mathlib have it? No. `lean_leansearch` for the regrouping statement returned only generic ingredients (`Module.Basis.sum_repr`, `Module.Basis.repr_sum_self`, `Polynomial.eval_sum`, `Module.Basis.sum_repr_mul_repr`), which the proof already uses or does not need. The statement is tied to the project def `coeffNone` and the specific `φ_ρ` shape, so no mathlib lemma could match it.
- Too specific / inline? Very specific to Lemma 2, but inlining it into the long `refine` of `exists_separated_representation` would make that proof harder to read; the current split (one helper per conjunct: linear independence, basis existence, identity) is clean. Already private.
- Well-chosen? Yes. Stated over a general commutative semiring, exactly in the shape the caller consumes.
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Separation.lean:265; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent: if `exists_separated_representation` is ever upstreamed, this helper travels with it (and would need `coeffNone` or its mathlib replacement via `MvPolynomial.optionEquivLeft` coefficients).

## Evidence
- `grep -rn eq_sum_aeval_basis_coeffNone_aux Roth/`: definition l.265, single use l.342.
- `grep -n` of `def`/`theorem` mentioning `coeffNone` in Roth/: confirms `Roth.coeffNone` (l.80) is the only project identifier in the body.
- `lean_leansearch` (one query, 6 results, described above): no match.
- No Lean runs and no evidence Lean files. A private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
