# Ticket Board — Roth's theorem

## Summary
- Total: 118 tickets (84 proof/definition tickets, 34 cleanup tickets)
- Open: 118 | In Progress: 0 | Done: 0
- Parallel capacity: up to 8 workers at the start (the first tickets of `HasseDeriv`, `Box`,
  `Wronskian`, and the `CoeffNorm`/`Lattice`/`MainLemma`-numeric tickets have no dependencies);
  typically 3–5 workers mid-project.
- Milestone: [T084] `Roth.roth` (preceded by [CLEANUP-ALL-1]).
- Toolchain: `leanprover/lean4:v4.34.0` with mathlib `v4.34.0` (bumped 2026-10-12; `lake build`
  works). A ticket is done only when `lake build` passes with no `sorry` in the ticket's declarations
  and no new axioms.
- Mathlib migration note: this mathlib deleted `MvPolynomial.coeff`; write `p.coeff m`
  (`AddMonoidAlgebra.coeff`, a `Finsupp`) for the source's `[X^m] p`; the generic `coeff_add`,
  `coeff_zero`, `coeff_smul` replace the deprecated `MvPolynomial.coeff_add`/`coeff_zero`;
  `MvPolynomial.coeff_monomial` now takes `[DecidableEq σ]`. Lemma names in the sketches were
  verified against `v4.34.0-rc2`; expect a few deprecation redirects.
- Every proof ticket's **Statement** is the canonical declaration from the skeleton (copied verbatim
  at board-generation time); do not change statements — if a statement is wrong, stop with a B2
  report and re-run `/develop --continue`.
- Cleanup cadence: per file, a `CLEANUP-n` ticket after every 3rd proof ticket and after the last
  one; `CLEANUP-ALL-1` before the milestone; `CLEANUP-FINAL` last. Later proof tickets on a file
  depend on that file's latest cleanup ticket.
- Files: Roth/Box.lean, Roth/CoeffNorm.lean, Roth/GenWronskian.lean, Roth/HasseDeriv.lean, Roth/Index.lean, Roth/Lattice.lean, Roth/Main.lean, Roth/MainLemma.lean, Roth/Separation.lean, Roth/Taylor.lean, Roth/Theta.lean, Roth/Wronskian.lean.

## Tickets

### [T001] Multivariate Hasse derivative: definition and monomial formula
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R0.1, R0.2

#### Statement
```lean
def hasseCoeff (d k : σ →₀ ℕ) : ℕ := d.prod fun j n => (k j).choose n

noncomputable def hasseDeriv (d : σ →₀ ℕ) : MvPolynomial σ R →ₗ[R] MvPolynomial σ R :=
  Finsupp.lsum R (fun k : σ →₀ ℕ =>
      (monomial (k - d)).comp (LinearMap.lsmul R R (hasseCoeff d k : R))) ∘ₗ
    (AddMonoidAlgebra.coeffLinearEquiv R).toLinearMap

theorem hasseDeriv_apply (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by sorry

@[simp]
theorem hasseDeriv_monomial (d k : σ →₀ ℕ) (a : R) :
    hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by sorry
```

#### Proof sketch
1. `hasseDeriv_monomial`: unfold `hasseDeriv`; `AddMonoidAlgebra.coeffLinearEquiv R (monomial k a) = Finsupp.single k a` (`MvPolynomial.single_eq_monomial`, `rfl`-level), then `Finsupp.lsum_apply`/`Finsupp.sum_single_index` (the summand at `0` is `monomial _ (c * 0) = 0`: `mul_zero`, `map_zero`); `LinearMap.lsmul_apply`, `smul_eq_mul`. Mirror `MvPolynomial.mkDerivationₗ_monomial`.
2. `hasseDeriv_apply`: write `P = ∑ k ∈ P.support, monomial k (coeff k P)` (`MvPolynomial.as_sum`), apply `map_sum`, rewrite each term with `hasseDeriv_monomial`.
3. Tag `hasseDeriv_monomial` `@[simp]` (already in skeleton).

#### Mathlib lemmas needed
- `MvPolynomial.as_sum`
- `Finsupp.lsum_apply`, `Finsupp.sum_single_index`
- `LinearMap.lsmul_apply`, `LinearMap.comp_apply`
- `MvPolynomial.single_eq_monomial`, `AddMonoidAlgebra.coeffLinearEquiv` (`Mathlib/Algebra/MonoidAlgebra/Module.lean:75`)
- `MvPolynomial.mkDerivationₗ_monomial` (as a model, `Mathlib/Algebra/MvPolynomial/Derivation.lean:44`)

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §1 definition of Δ_i, clean.tex:122-132
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.1, R0.2).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated.

**Progress**:
- 2026-10-12T18:34: DONE — proved; file compiles


### [T002] Coefficient identity for Hasse derivatives
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T001
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.3, R0.4, R0.5

#### Statement
```lean
theorem hasseCoeff_eq_zero_iff (d k : σ →₀ ℕ) : hasseCoeff d k = 0 ↔ ¬ d ≤ k := by sorry

theorem coeff_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by sorry

theorem hasseCoeff_eq_prod [Fintype σ] (d k : σ →₀ ℕ) :
    hasseCoeff d k = ∏ j, (k j).choose (d j) := by sorry
```

#### Proof sketch
1. `hasseCoeff_eq_zero_iff`: unfold `hasseCoeff`, `Finsupp.prod`; `Finset.prod_eq_zero_iff`; `Nat.choose_eq_zero_iff` (`n.choose k = 0 ↔ n < k`); `Finsupp.le_iff` (`d ≤ k ↔ ∀ j ∈ d.support, d j ≤ k j`); `not_forall`, `not_le`.
2. `coeff_hasseDeriv`: by linearity in `P` (`MvPolynomial.induction_on'`: monomial case + additivity; the RHS is additive in `P` by `coeff_add`, `mul_add`). Monomial `monomial k a`: LHS `= coeff e (monomial (k - d) (c k * a)) = if k - d = e then c k * a else 0` (`hasseDeriv_monomial`, `coeff_monomial`); RHS `= c (e+d) * (if k = e + d then a else 0)`. Case `k = e + d`: both `c (e+d) * a` (`add_tsub_cancel_right`). Case `k ≠ e + d`: RHS `0`; LHS: if `c k = 0` done (`zero_mul`), else `d ≤ k` by `hasseCoeff_eq_zero_iff`, so `k - d = e → k = e + d` (`tsub_eq_iff_eq_add_of_le`), contradiction.
3. `hasseCoeff_eq_prod`: `Finsupp.prod_fintype _ _ (fun j => Nat.choose_zero_right _)`.

#### Mathlib lemmas needed
- `Finset.prod_eq_zero_iff`, `Nat.choose_eq_zero_iff`, `Finsupp.le_iff`
- `MvPolynomial.induction_on'`, `MvPolynomial.coeff_monomial`, `MvPolynomial.coeff_add`
- `tsub_eq_iff_eq_add_of_le`, `add_tsub_cancel_right`
- `Finsupp.prod_fintype`, `Nat.choose_zero_right`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §1 Lean note (coefficient identity), clean.tex:147-152
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.3, R0.4, R0.5).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated.

**Progress**:
- 2026-10-12T18:34: DONE — proved; file compiles


### [T003] Hasse derivative of order 0, of constants, and compatibility with coefficient maps
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T002
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.6, R0.7, R0.8

#### Statement
```lean
@[simp]
theorem hasseDeriv_zero : hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] _) := by
  sorry

theorem hasseDeriv_zero_apply (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by sorry

theorem hasseDeriv_C {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by sorry

theorem hasseDeriv_map {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) : hasseDeriv d (map f P) = map f (hasseDeriv d P) := by sorry
```

#### Proof sketch
1. `hasseDeriv_zero_apply`: `MvPolynomial.ext`, `coeff_hasseDeriv`, `hasseCoeff 0 _ = 1` (`Finsupp.prod_zero_index`), `add_zero`, `one_mul`. `hasseDeriv_zero`: `LinearMap.ext hasseDeriv_zero_apply`.
2. `hasseDeriv_C`: `C a = monomial 0 a` (`MvPolynomial.C_apply`), `hasseDeriv_monomial`, `hasseCoeff d 0 = 0` by `hasseCoeff_eq_zero_iff` (`¬ d ≤ 0` since `d ≠ 0`: `Finsupp.le_zero_iff`?/`nonpos_iff_eq_zero`), `zero_mul`, `monomial_zero`.
3. `hasseDeriv_map`: `MvPolynomial.ext`, `coeff_hasseDeriv` both sides, `MvPolynomial.coeff_map`, `map_mul`, `map_natCast`.

#### Mathlib lemmas needed
- `MvPolynomial.ext`, `MvPolynomial.coeff_map`, `MvPolynomial.C_apply`
- `Finsupp.prod_zero_index`, `nonpos_iff_eq_zero`
- `map_natCast`, `map_mul`
- `LinearMap.ext`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §1 clean.tex:126-132 and Lean note clean.tex:151-152; §4 clean.tex:565-567 (Δ_0 P = P)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.6, R0.7, R0.8).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated.

**Progress**:
- 2026-10-12T18:34: DONE — proved; file compiles


### [CLEANUP-1] Run /cleanup on Roth/HasseDeriv.lean
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T003
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/HasseDeriv.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T18:34: light inline cleanup (deprecations fixed); full /cleanup deferred to CLEANUP-3 (final per-file)


### [T004] Hasse derivatives commute with injective renaming of variables
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T003, CLEANUP-1
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.9

#### Statement
```lean
theorem hasseDeriv_rename {τ : Type*} {f : σ → τ} (hf : Function.Injective f) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) :
    hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) := by sorry
```

#### Proof sketch
1. Linearity in `P` (`MvPolynomial.induction_on'`); monomial case: `rename_monomial`, `hasseDeriv_monomial`.
2. Show `hasseCoeff (d.mapDomain f) (k.mapDomain f) = hasseCoeff d k`: unfold `Finsupp.prod`; `Finsupp.support_mapDomain`/`Finsupp.mapDomain_support_of_injective hf`, `Finset.prod_map`, `Finsupp.mapDomain_apply hf`.
3. Show `k.mapDomain f - d.mapDomain f = (k - d).mapDomain f`: `Finsupp.ext`; for `i ∈ range f` use `mapDomain_apply hf`; for `i ∉ range f` both sides are `0` (`Finsupp.mapDomain_notin_range`, `tsub_zero`).
4. Conclude with `rename_monomial` on the right.

#### Mathlib lemmas needed
- `MvPolynomial.rename_monomial`, `MvPolynomial.induction_on'`
- `Finsupp.mapDomain_apply`, `Finsupp.mapDomain_notin_range`, `Finsupp.mapDomain_support_of_injective`
- `Finset.prod_map`, `Finsupp.ext`, `tsub_zero`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lean note clean.tex:638-641 (variable renaming)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.9).

#### Generality decision
- injective `f : σ → τ`; `R` any `CommSemiring`. Injectivity is sharp (decomposition R0.9 attack [3]).

**Progress**:
- 2026-10-12T18:35: DONE — proved via prod_mapDomain_index_inj


### [T005] Composition of Hasse derivatives
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T002, CLEANUP-1
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.10, R0.11

#### Statement
```lean
theorem hasseDeriv_hasseDeriv (d e : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by sorry

theorem hasseDeriv_hasseDeriv_of_disjoint {d e : σ →₀ ℕ} (h : Disjoint d.support e.support)
    (P : MvPolynomial σ R) : hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := by sorry
```

#### Proof sketch
1. `hasseDeriv_hasseDeriv`: `MvPolynomial.ext e`; `coeff_hasseDeriv` twice on the left (`coeff e (Δ_d (Δ_e' P)) = c_d(e+d) * c_{e'}(e+d+e') * coeff (e+d+e') P`), `coeff_smul`/`coeff_hasseDeriv` on the right (`c_d(d+e') * c_{d+e'}(e+(d+e')) * coeff …`), `add_assoc`/`add_comm` to align exponents.
2. Reduce to the scalar identity `hasseCoeff d (e+d) * hasseCoeff e' (e+d+e') = hasseCoeff d (d+e') * hasseCoeff (d+e') (e+d+e')` in `ℕ` (then `Nat.cast_mul`): unfold as products over `d.support ∪ e'.support` (`Finsupp.prod_add_index'` or rewrite each `Finsupp.prod` as a product over the union via `Finsupp.prod_of_support_subset`), and prove the coordinatewise identity `binom(f+d, d) * binom(f+d+e, e) = binom(d+e, d) * binom(f+d+e, d+e)` by multiplying both sides by `f! d! e!` and using `Nat.add_choose_mul_factorial_mul_factorial` three times (`Nat.factorial_ne_zero`, `mul_left_cancel₀`).
3. `hasseDeriv_hasseDeriv_of_disjoint`: from the previous with `hasseCoeff d (d+e) = 1`: each factor `binom(d_j + e_j, d_j)` with `j ∈ d.support` has `e_j = 0` (`Finset.disjoint_left`), so it is `Nat.choose_self`; `Finset.prod_eq_one`, `one_smul`.

#### Mathlib lemmas needed
- `Nat.add_choose_mul_factorial_mul_factorial`, `Nat.factorial_ne_zero`, `mul_left_cancel₀`
- `Finsupp.prod_of_support_subset`, `Finset.prod_eq_one`, `Nat.choose_self`
- `Finset.disjoint_left`, `MvPolynomial.coeff_smul`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 proof of Lemma index-of-derivative, clean.tex:578-582 (composition identity)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.10, R0.11).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated.

**Progress**:
- 2026-10-12T18:36: DONE — composition identity via Nat.choose_mul


### [T006] Partial derivative of a Hasse derivative; factorial identity
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T002, CLEANUP-1
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.12, R0.19

#### Statement
```lean
theorem pderiv_hasseDeriv (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P := by
  sorry

theorem factorial_smul_hasseDeriv_single (j : σ) (n : ℕ) (P : MvPolynomial σ R) :
    (n.factorial : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv (R := R) j))^[n] P := by sorry
```

#### Proof sketch
1. `pderiv_hasseDeriv`: `MvPolynomial.ext e`; `MvPolynomial.coeff_pderiv` (`coeff e (pderiv j Q) = coeff (e + single j 1) Q * (e j + 1)`), `coeff_hasseDeriv` on both sides, `coeff_smul`; align exponents `e + single j 1 + d = e + (d + single j 1)` (`add_right_comm`).
2. Scalar identity in `ℕ`: `hasseCoeff d (e + single j 1 + d) * (e j + 1) = (d j + 1) * hasseCoeff (d + single j 1) (e + (d + single j 1))`: products over supports; all coordinates `i ≠ j` agree (`Finsupp.single_eq_of_ne`); at `j`: `binom(e_j + 1 + d_j, d_j) * (e_j+1) = (d_j+1) * binom(e_j + d_j + 1, d_j + 1)` by `Nat.choose_succ_right_eq` (`n.choose (k+1) * (k+1) = n.choose k * (n - k)` with `n = e_j+d_j+1`, `k = d_j`). Handle `j ∉ d.support` by `Finsupp.prod_add_index'`/`Finsupp.support_add_eq`-style case split (`Finsupp.prod_single_index`).
3. `factorial_smul_hasseDeriv_single`: induction on `n`; `n = 0`: `Nat.factorial_zero`, `one_smul`, `Finsupp.single_zero`, `hasseDeriv_zero_apply`, `Function.iterate_zero`. Step: `Function.iterate_succ_apply'`, IH, `pderiv_hasseDeriv` with `d = single j n` (`single_add` for `single j n + single j 1 = single j (n+1)`), `Nat.factorial_succ`, `mul_smul`, `Nat.cast_mul`.

#### Mathlib lemmas needed
- `MvPolynomial.coeff_pderiv`
- `Nat.choose_succ_right_eq`
- `Finsupp.single_eq_of_ne`, `Finsupp.single_add`, `Finsupp.prod_single_index`
- `Function.iterate_succ_apply'`, `Nat.factorial_succ`, `mul_smul`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 1, clean.tex:303-305 (∂_jΔ_d=(d_j+1)Δ_{d+e_j}); §1 clean.tex:134-139
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.12, R0.19).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated. The factorial identity holds over any commutative semiring (as mathlib's `Polynomial.factorial_smul_hasseDeriv`).

**Progress**:
- 2026-10-12T18:37: DONE — coordinate identity via Nat.choose_succ_right_eq


### [CLEANUP-2] Run /cleanup on Roth/HasseDeriv.lean
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T006
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/HasseDeriv.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T18:37: light inline cleanup; full /cleanup at CLEANUP-3


### [T007] Degree bounds for Hasse derivatives and the binomial bound
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T002, CLEANUP-2
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.13, R0.14, R0.18

#### Statement
```lean
theorem degreeOf_hasseDeriv_le (j : σ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    degreeOf j (hasseDeriv d P) ≤ degreeOf j P := by sorry

theorem hasseDeriv_eq_zero_of_degreeOf_lt {j : σ} {d : σ →₀ ℕ} {P : MvPolynomial σ R}
    (h : degreeOf j P < d j) : hasseDeriv d P = 0 := by sorry

theorem hasseCoeff_le_two_pow [Fintype σ] {d k : σ →₀ ℕ} {r : σ → ℕ} (hk : ∀ j, k j ≤ r j) :
    hasseCoeff d k ≤ 2 ^ (∑ j, r j) := by sorry
```

#### Proof sketch
1. `degreeOf_hasseDeriv_le`: `MvPolynomial.degreeOf_le_iff.2`; for `e ∈ support (Δ_d P)`, `coeff e (Δ_d P) ≠ 0` gives `coeff (e+d) P ≠ 0` (`coeff_hasseDeriv`, `mul_ne_zero_iff`), so `(e+d) j ≤ degreeOf j P` (`degreeOf_le_iff.1 le_rfl`) and `e j ≤ (e+d) j` (`Finsupp.add_apply`, `Nat.le_add_right`).
2. `hasseDeriv_eq_zero_of_degreeOf_lt`: `MvPolynomial.ext e`; `coeff_hasseDeriv`; `coeff (e+d) P = 0` because `(e+d) j ≥ d j > degreeOf j P` (`MvPolynomial.degreeOf_lt_iff` or `degreeOf_le_iff` contrapositive), `mul_zero`.
3. `hasseCoeff_le_two_pow`: `hasseCoeff_eq_prod`; `Finset.prod_le_prod'` with `Nat.choose_le_two_pow (k j) (d j) : (k j).choose (d j) ≤ 2 ^ k j`, then `Finset.prod_pow_eq_pow_sum` and `pow_le_pow_right` with `∑ k j ≤ ∑ r j` (`Finset.sum_le_sum`).

#### Mathlib lemmas needed
- `MvPolynomial.degreeOf_le_iff`, `MvPolynomial.degreeOf_lt_iff`
- `Nat.choose_le_two_pow`, `Finset.prod_le_prod'`, `Finset.prod_pow_eq_pow_sum`, `pow_le_pow_right`
- `mul_ne_zero_iff`, `Finsupp.add_apply`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 clean.tex:435-437; §6 clean.tex:1510-1511; §3 clean.tex:457-461
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.13, R0.14, R0.18).

#### Generality decision
- `degreeOf` lemmas over any `CommSemiring`; the `2^S` bound needs `[Fintype σ]` for the sum.

**Progress**:
- 2026-10-12T18:38: DONE


### [T008] A Hasse operator passes through a factor not involving its variables
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T001, T002, CLEANUP-2
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.15

#### Statement
```lean
theorem hasseDeriv_mul_of_degreeOf_eq_zero {d : σ →₀ ℕ} {f g : MvPolynomial σ R}
    (hf : ∀ j ∈ d.support, degreeOf j f = 0) : hasseDeriv d (f * g) = f * hasseDeriv d g := by
  sorry
```

#### Proof sketch
1. Bilinearity: `MvPolynomial.induction_on'` on `g` (both sides additive in `g`: `mul_add`, `map_add`), then on `f` (`add_mul`, `map_add`, and the hypothesis passes to summands: `degreeOf_add_le`… — better: induct on `f` via `MvPolynomial.as_sum` with each monomial `monomial a c`, `a ∈ f.support`, so `a j = 0` for `j ∈ d.support` by `degreeOf_le_iff.1 (hf j hj) a ha`).
2. Monomial case `f = monomial a c`, `g = monomial b c'`: `monomial_mul`, `hasseDeriv_monomial`; show `hasseCoeff d (a + b) = hasseCoeff d b` (products over `d.support`; at each `j ∈ d.support`, `a j = 0` so `(a+b) j = b j`) and `a + b - d = a + (b - d)` (`Finsupp.ext`; coordinatewise: `j ∈ d.support` ⇒ `a j = 0`; else `d j = 0`, `tsub_zero`).
3. Reassemble with `monomial_mul` and `mul_comm`/`mul_assoc` on the scalars.

#### Mathlib lemmas needed
- `MvPolynomial.induction_on'`, `MvPolynomial.as_sum`, `MvPolynomial.monomial_mul`
- `MvPolynomial.degreeOf_le_iff`, `Finsupp.mem_support_iff`
- `Finsupp.ext`, `Finsupp.add_apply`, `Finsupp.tsub_apply`, `tsub_zero`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:407-420 (the entries of A Bᵀ)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.15).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated. Hypothesis only on `d.support` (sharp, see R0.15).

**Progress**:
- 2026-10-12T18:38: DONE


### [T009] One-variable Hasse operators are the univariate Hasse derivative
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T001, CLEANUP-2
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R0.16, R0.17

#### Statement
```lean
theorem hasseDeriv_single_aeval_X (j : σ) (n : ℕ) (f : Polynomial R) :
    hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) =
      Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv n f) := by sorry

theorem uniqueAlgEquiv_hasseDeriv [Unique σ] (n : ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv (R := R) (Finsupp.single (default : σ) n) P) =
      Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P) := by sorry
```

#### Proof sketch
1. `hasseDeriv_single_aeval_X`: `Polynomial.induction_on'` (additivity: `map_add`) reducing to `f = monomial m a`: `Polynomial.aeval_monomial` (`= algebraMap a * X j ^ m`), `MvPolynomial.X_pow_eq_monomial`, `C_mul_monomial`-style (`algebraMap_eq`, `C_mul_monomial`), `hasseDeriv_monomial` with `hasseCoeff (single j n) (single j m) = m.choose n` (`Finsupp.prod_single_index`, `Finsupp.single_eq_same`), `single j m - single j n = single j (m - n)` (`Finsupp.single_tsub`?/`Finsupp.ext`); right side: `Polynomial.hasseDeriv_monomial`, `Polynomial.aeval_monomial`.
2. `uniqueAlgEquiv_hasseDeriv`: set `P = (uniqueAlgEquiv R σ).symm f` (`AlgEquiv.symm_apply_apply`); `(uniqueAlgEquiv R σ).symm f = Polynomial.aeval (X default) f` (`MvPolynomial.uniqueAlgEquiv` is `pUnitAlgEquiv` transported; unfold with `MvPolynomial.uniqueAlgEquiv_symm_apply`/`algHom_ext`), apply the first lemma, then `AlgEquiv.apply_symm_apply`.

#### Mathlib lemmas needed
- `Polynomial.induction_on'`, `Polynomial.aeval_monomial`, `Polynomial.hasseDeriv_monomial`
- `MvPolynomial.X_pow_eq_monomial`, `MvPolynomial.C_mul_monomial`, `MvPolynomial.algebraMap_eq`
- `Finsupp.prod_single_index`, `Finsupp.single_eq_same`
- `MvPolynomial.uniqueAlgEquiv` (`Mathlib/Algebra/MvPolynomial/Equiv.lean`), `AlgEquiv.apply_symm_apply`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §1 Lean note clean.tex:147-150 (univariate hasseDeriv as a model)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R0.16, R0.17).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: ℤ, ℚ, ℝ, 'any commutative semiring'); no `Fintype` unless a sum over all variables is stated. `[Unique σ]` for the second lemma (mathlib's current `uniqueAlgEquiv`).

**Progress**:
- 2026-10-12T18:38: DONE


### [CLEANUP-3] Run /cleanup on Roth/HasseDeriv.lean
- **Status**: done
- **File**: Roth/HasseDeriv.lean
- **Depends on**: T009
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/HasseDeriv.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T18:38: dispatched /cleanup to background agent
- 2026-10-12T18:45: agent cleanup: golfed proofs, docstrings; no statement changes; build clean


### [T010] The box of multi-indices and its cardinality
- **Status**: done
- **File**: Roth/Box.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R1.1, R1.2

#### Statement
```lean
noncomputable def box (r : σ → ℕ) : Finset (σ →₀ ℕ) :=
  (Fintype.piFinset fun j => Finset.range (r j + 1)).map
    Finsupp.equivFunOnFinite.symm.toEmbedding

theorem mem_box {r : σ → ℕ} {d : σ →₀ ℕ} : d ∈ box r ↔ ∀ j, d j ≤ r j := by sorry

theorem card_box (r : σ → ℕ) : (box r).card = ∏ j, (r j + 1) := by sorry

theorem card_le_card_box {r : σ → ℕ} {s : Finset (σ →₀ ℕ)} (hs : ∀ d ∈ s, ∀ j, d j ≤ r j) :
    s.card ≤ ∏ j, (r j + 1) := by sorry
```

#### Proof sketch
1. `mem_box`: unfold `box`; `Finset.mem_map`, `Function.Embedding.coeFn_mk`/`Equiv.toEmbedding_apply`, `Fintype.mem_piFinset`, `Finset.mem_range`, `Nat.lt_succ_iff`; the witness is `Finsupp.equivFunOnFinite d` with `Finsupp.equivFunOnFinite_symm_apply_toFun`.
2. `card_box`: `Finset.card_map`, `Fintype.card_piFinset`, `Finset.card_range`.
3. `card_le_card_box`: `Finset.card_le_card (fun d hd => mem_box.2 (hs d hd))` then `card_box`.

#### Mathlib lemmas needed
- `Finset.mem_map`, `Fintype.mem_piFinset`, `Finset.mem_range`
- `Finset.card_map`, `Fintype.card_piFinset`, `Finset.card_range`
- `Finsupp.equivFunOnFinite`, `Finset.card_le_card`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 Lemma 8 clean.tex:1053-1056; Lemma 9 eq. (43) clean.tex:1413-1418
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R1.1, R1.2).

#### Generality decision
- `[Fintype σ] [DecidableEq σ]`; `r : σ → ℕ` arbitrary.

**Progress**:
- 2026-10-12T18:39: DONE


### [T011] Weights of multi-indices: basic API
- **Status**: done
- **File**: Roth/Box.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R1.3, R1.4, R1.5

#### Statement
```lean
noncomputable def weight (r : σ → ℕ) (d : σ →₀ ℕ) : ℝ := ∑ j, (d j : ℝ) / r j

theorem weight_nonneg (r : σ → ℕ) (d : σ →₀ ℕ) : 0 ≤ weight r d := by sorry

@[simp]
theorem weight_zero (r : σ → ℕ) : weight r 0 = 0 := by sorry

theorem weight_add (r : σ → ℕ) (d e : σ →₀ ℕ) : weight r (d + e) = weight r d + weight r e := by
  sorry

theorem weight_eq_zero_iff {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} :
    weight r d = 0 ↔ d = 0 := by sorry

theorem weight_single (r : σ → ℕ) (j : σ) (n : ℕ) :
    weight r (Finsupp.single j n) = n / r j := by sorry

theorem weight_le_card {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} (hd : ∀ j, d j ≤ r j) :
    weight r d ≤ Fintype.card σ := by sorry
```

#### Proof sketch
1. `weight_nonneg`: `Finset.sum_nonneg`, `div_nonneg`, `Nat.cast_nonneg`. `weight_zero`: `simp [weight]`.
2. `weight_add`: `Finsupp.add_apply`, `Nat.cast_add`, `add_div`, `Finset.sum_add_distrib`.
3. `weight_eq_zero_iff`: `Finset.sum_eq_zero_iff_of_nonneg` + `div_eq_zero_iff` + `Nat.cast_eq_zero` + `(hr j).ne'` + `Finsupp.ext_iff`.
4. `weight_single`: `Finsupp.single_apply`, `Finset.sum_ite_eq'`, `Nat.cast_ite`, `zero_div`.
5. `weight_le_card`: `Finset.sum_le_card_nsmul _ _ 1 (fun j _ => div_le_one_of_le (by exact_mod_cast hd j) (Nat.cast_nonneg _))`, `Finset.card_univ`, `nsmul_eq_mul`, `mul_one`.

#### Mathlib lemmas needed
- `Finset.sum_nonneg`, `div_nonneg`, `Finset.sum_add_distrib`, `add_div`
- `Finset.sum_eq_zero_iff_of_nonneg`, `div_eq_zero_iff`, `Nat.cast_eq_zero`
- `Finsupp.single_apply`, `Finset.sum_ite_eq'`
- `Finset.sum_le_card_nsmul`, `div_le_one_of_le`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 definition of the index clean.tex:535-541, clean.tex:565-566; §5 clean.tex:665-668
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R1.3, R1.4, R1.5).

#### Generality decision
- `[Fintype σ]`; `r : σ → ℕ` (positivity only where stated; Lean's `x/0 = 0` keeps the other lemmas true).

**Progress**:
- 2026-10-12T18:39: DONE


### [T012] Weights under scaling, degree bounds, and embeddings
- **Status**: done
- **File**: Roth/Box.lean
- **Depends on**: T011
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R1.6, R1.7, R1.8

#### Statement
```lean
theorem weight_mul_left {l : ℕ} (hl : 0 < l) (r : σ → ℕ) (d : σ →₀ ℕ) :
    weight (fun j => l * r j) d = weight r d / l := by sorry

theorem weight_le_degree_div {r : σ → ℕ} {m : ℕ} (hm : 0 < m) (hr : ∀ j, m ≤ r j)
    (d : σ →₀ ℕ) : weight r d ≤ d.degree / m := by sorry

theorem weight_mapDomain {τ : Type*} [Fintype τ] [DecidableEq τ] {f : σ → τ}
    (hf : Function.Injective f) (r : τ → ℕ) (d : σ →₀ ℕ) :
    weight r (d.mapDomain f) = weight (r ∘ f) d := by sorry
```

#### Proof sketch
1. `weight_mul_left`: unfold; `Finset.sum_div`; termwise `Nat.cast_mul`, `div_mul_eq_div_div` (true also when `r j = 0`), `mul_comm`.
2. `weight_le_degree_div`: `Finsupp.degree` as `∑ j, d j` (`Finsupp.degree_eq_weight_one` + `Finsupp.weight_apply` + `Finsupp.sum_fintype`, or `Finsupp.degree` unfolds to `∑ j ∈ d.support, d j` and `Finset.sum_subset`), `Nat.cast_sum`, `Finset.sum_div`, `Finset.sum_le_sum` with `div_le_div_of_nonneg_left` (`(d j : ℝ)/r j ≤ d j / m` from `m ≤ r j`, `0 < m`).
3. `weight_mapDomain`: write `∑ i : τ, (d.mapDomain f) i / r i` as a sum over `Finset.univ.map ⟨f, hf⟩` plus zero terms off the range (`Finset.sum_subset`, `Finsupp.mapDomain_notin_range`, `zero_div`), then `Finset.sum_map` and `Finsupp.mapDomain_apply hf`.

#### Mathlib lemmas needed
- `Finset.sum_div`, `div_mul_eq_div_div`
- `Finsupp.degree_eq_weight_one`, `Finsupp.weight_apply`, `Finsupp.sum_fintype`, `div_le_div_of_nonneg_left`
- `Finset.sum_subset`, `Finset.sum_map`, `Finsupp.mapDomain_apply`, `Finsupp.mapDomain_notin_range`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 clean.tex:646-650; §5 clean.tex:800-806; §4 Lemma 4-2 clean.tex:621-624
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R1.6, R1.7, R1.8).

#### Generality decision
- `[Fintype σ]`; injective `f` for `weight_mapDomain` (sharp).

**Progress**:
- 2026-10-12T18:39: DONE


### [CLEANUP-4] Run /cleanup on Roth/Box.lean
- **Status**: done
- **File**: Roth/Box.lean
- **Depends on**: T012
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Box.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T18:45: agent dispatched
- 2026-10-12T18:53: agent cleanup; build clean


### [T013] Wronskian of a linearly dependent family vanishes
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R4.1, R4.2

#### Statement
```lean
noncomputable def wronskianMatrix (φ : Fin l → K[X]) : Matrix (Fin l) (Fin l) K[X] :=
  Matrix.of fun μ ν => hasseDeriv (μ : ℕ) (φ ν)

noncomputable def wronskian (φ : Fin l → K[X]) : K[X] := (wronskianMatrix φ).det

theorem wronskian_eq_zero_of_not_linearIndependent {φ : Fin l → K[X]}
    (h : ¬ LinearIndependent K φ) : wronskian φ = 0 := by sorry
```

#### Proof sketch
1. From `¬ LinearIndependent K φ` get `g : Fin l → K`, `∑ ν, g ν • φ ν = 0`, `g ν₀ ≠ 0` (`Fintype.not_linearIndependent_iff`).
2. Put `v : Fin l → K[X] := fun ν => C (g ν)`; `v ≠ 0` (`Polynomial.C_ne_zero`, `Function.ne_iff`). Show `(wronskianMatrix φ) *ᵥ v = 0`: entry `μ` is `∑ ν, hasseDeriv μ (φ ν) * C (g ν) = hasseDeriv μ (∑ ν, g ν • φ ν) = 0` (`Matrix.mulVec`, `Matrix.of_apply`, `map_sum`, `map_smul`, `Polynomial.smul_eq_C_mul`, `mul_comm`).
3. `Matrix.exists_mulVec_eq_zero_iff.1 ⟨v, hv, h⟩ : det = 0` (`K[X]` is a domain).

#### Mathlib lemmas needed
- `Fintype.not_linearIndependent_iff`
- `Matrix.exists_mulVec_eq_zero_iff` (`[CommRing A] [IsDomain A]`)
- `Matrix.mulVec`, `Matrix.of_apply`, `Polynomial.smul_eq_C_mul`, `Polynomial.C_ne_zero`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 first lemma, clean.tex:166-173
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R4.1, R4.2).

#### Generality decision
- any field `K` (no characteristic assumption needed for this direction).

**Progress**:
- 2026-10-12T18:40: DONE


### [T014] The binomial determinant is a scaled Vandermonde determinant
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R4.3

#### Statement
```lean
theorem det_choose_eq [CharZero K] (d : Fin l → ℕ) :
    (Matrix.of fun μ ν : Fin l => ((d ν).choose μ : K)).det =
      (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) * ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i) := by
  sorry
```

#### Proof sketch
1. Rewrite each entry: `((d ν).choose μ : K) = ((μ : ℕ)! : K)⁻¹ * (descPochhammer K μ).eval (d ν : K)` from `descPochhammer_eval_eq_descFactorial` and `Nat.descFactorial_eq_factorial_mul_choose` (cast with `Nat.cast_mul`, `Nat.cast_choose`-free: `eq_inv_mul_iff_mul_eq₀`, `Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _)` — `CharZero K`).
2. Pull the row factors out: `Matrix.det_mul_row (fun μ => (μ !)⁻¹)` gives `det = (∏ μ, (μ !)⁻¹) * det (of fun μ ν => (descPochhammer K μ).eval (d ν))`.
3. Transpose: `Matrix.det_transpose`; the transposed matrix is `of fun i j => (p j).eval (v i)` with `v = (fun ν => (d ν : K))`, `p = descPochhammer K`; apply `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde v p (fun i => descPochhammer_natDegree _) (fun i => monic_descPochhammer _)` (direction: it states `det (vandermonde v) = det (of …)`), then `Matrix.det_vandermonde`.

#### Mathlib lemmas needed
- `descPochhammer_eval_eq_descFactorial`, `Nat.descFactorial_eq_factorial_mul_choose`
- `monic_descPochhammer`, `descPochhammer_natDegree`
- `Matrix.det_mul_row`, `Matrix.det_transpose`
- `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`, `Matrix.det_vandermonde`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 first lemma, clean.tex:184-194
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R4.3).

#### Generality decision
- field `K` with `CharZero K` (sharp: inverses of factorials).

**Progress**:
- 2026-10-12T18:41: DONE


### [T015] The top coefficient of a Wronskian with distinct degrees
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R4.4, R4.5

#### Statement
```lean
theorem sum_range_le_sum_of_injective (d : Fin l → ℕ) (hd : Function.Injective d) :
    ∑ ν : Fin l, (ν : ℕ) ≤ ∑ ν, d ν := by sorry

theorem coeff_wronskian_of_natDegree_injective {φ : Fin l → K[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν => (φ ν).natDegree) :
    (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      (∏ ν, (φ ν).leadingCoeff) *
        (Matrix.of fun μ ν : Fin l => (((φ ν).natDegree.choose μ : ℕ) : K)).det := by sorry
```

#### Proof sketch
1. `sum_range_le_sum_of_injective`: induction on `l`; for `Fin (l+1)` pick `ν₀` maximising `d` (`Finset.exists_max_image`), then `d ν₀ ≥ l` (it exceeds the `l` other distinct values below it: the image of the others is a set of `l` naturals all `< d ν₀`, so `d ν₀ ≥ l` by `Finset.card_le_card` into `range (d ν₀)`), remove `ν₀` (`Fin.sum_univ_succAbove`, `Fin.sum_univ_castSucc` for the range side) and apply the IH to `d ∘ ν₀.succAbove` (injective: `Fin.succAbove_right_injective`).
2. `coeff_wronskian_of_natDegree_injective`: set `D := ∑ natDegree − ∑ ν` (ℕ, well-defined by step 1); unfold `wronskian`, `Matrix.det_apply'`, `Polynomial.finset_sum_coeff`, `Polynomial.coeff_mul`-free: `Int.cast`-sign `ε σ` is `±1` so `coeff (ε σ * p) D = ε σ * coeff p D` (`Polynomial.coeff_intCast_mul`?/`Int.units_eq_one_or` cases, `one_mul`, `neg_one_mul`, `coeff_neg`).
3. For each `σ`: if `∃ ν, d ν < σ ν` then the factor `hasseDeriv (σ ν) (φ ν) = 0` (`Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`), the product is `0` (`Finset.prod_eq_zero`), and the corresponding term of `(∏ lc) * det(binom)` is `0` because `(d ν).choose (σ ν) = 0` (`Nat.choose_eq_zero_of_lt`). Otherwise `∀ ν, σ ν ≤ d ν`: with `n ν := d ν − σ ν` we have `∑ n ν = D` (`Finset.sum_tsub_distrib` with the pointwise bound, `Fin.sum_univ_eq_sum_range`, `Equiv.sum_comp σ`), `natDegree (hasseDeriv (σ ν) (φ ν)) ≤ n ν` (`Polynomial.natDegree_hasseDeriv_le`), so `Polynomial.coeff_prod_of_natDegree_le` gives `coeff D (∏) = ∏ coeff (n ν) (hasseDeriv (σ ν) (φ ν)) = ∏ ((d ν).choose (σ ν) * lc (φ ν))` (`Polynomial.hasseDeriv_coeff`, `Nat.sub_add_cancel`, `Polynomial.coeff_natDegree`).
4. Collect: `Finset.prod_mul_distrib`, `Finset.mul_sum`, and recognise `Matrix.det_apply'` of `of fun μ ν => ((d ν).choose μ : K)` (its term for `σ` is `ε σ * ∏ ν, (d ν).choose (σ ν)` — `Matrix.of_apply`).

#### Mathlib lemmas needed
- `Finset.exists_max_image`, `Fin.sum_univ_succAbove`, `Fin.succAbove_right_injective`
- `Matrix.det_apply'`, `Polynomial.finset_sum_coeff`, `Int.units_eq_one_or`
- `Polynomial.coeff_prod_of_natDegree_le`, `Polynomial.natDegree_hasseDeriv_le`, `Polynomial.hasseDeriv_coeff`, `Polynomial.hasseDeriv_eq_zero_of_lt_natDegree`
- `Nat.choose_eq_zero_of_lt`, `Finset.prod_eq_zero`, `Finset.sum_tsub_distrib`, `Equiv.sum_comp`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 first lemma, clean.tex:181-196
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R4.4, R4.5).

#### Generality decision
- any field `K`; `φ ν ≠ 0` and injective degrees.

**Progress**:
- 2026-10-12T18:43: DONE


### [CLEANUP-5] Run /cleanup on Roth/Wronskian.lean
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: T015
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Wronskian.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T18:43: deferred to final per-file cleanup (CLEANUP-6) run by agent


### [T016] Nonvanishing of the Wronskian for distinct degrees
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: T014, T015, CLEANUP-5
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R4.6

#### Statement
```lean
theorem wronskian_ne_zero_of_natDegree_injective [CharZero K] {φ : Fin l → K[X]}
    (hφ : ∀ ν, φ ν ≠ 0) (hd : Function.Injective fun ν => (φ ν).natDegree) :
    wronskian φ ≠ 0 := by sorry
```

#### Proof sketch
1. `Polynomial.ne_zero_of_coeff_ne_zero` at `D`; rewrite the coefficient with `coeff_wronskian_of_natDegree_injective` and the determinant with `det_choose_eq`.
2. All three factors are nonzero: `Finset.prod_ne_zero_iff` with `Polynomial.leadingCoeff_ne_zero.2 (hφ ν)`; `inv_ne_zero (Nat.cast_ne_zero.2 (Nat.factorial_ne_zero _))`; the Vandermonde product: `Finset.prod_ne_zero_iff` + `sub_ne_zero.2` + `Nat.cast_injective.ne (hd.ne hij)` (or `Matrix.det_vandermonde_ne_zero_iff.2` with `Nat.cast_injective.comp hd`).

#### Mathlib lemmas needed
- `Polynomial.ne_zero_of_coeff_ne_zero`, `Polynomial.leadingCoeff_ne_zero`
- `Finset.prod_ne_zero_iff`, `Nat.factorial_ne_zero`, `Nat.cast_injective`
- `Matrix.det_vandermonde_ne_zero_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 first lemma, clean.tex:194-196
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R4.6).

#### Generality decision
- field `K` with `CharZero K`.

**Progress**:
- 2026-10-12T18:43: DONE


### [T017] Column operations on Wronskians
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: CLEANUP-5
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R4.7, R4.8

#### Statement
```lean
theorem wronskian_update_sub_smul {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K) :
    wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = wronskian φ := by sorry

theorem linearIndependent_update_sub_smul {φ : Fin l → K[X]} {ν ν' : Fin l} (h : ν ≠ ν') (c : K)
    (hφ : LinearIndependent K φ) :
    LinearIndependent K (Function.update φ ν' (φ ν' - C c * φ ν)) := by sorry

theorem sum_natDegree_update_lt {φ : Fin l → K[X]} (hφ : LinearIndependent K φ) {ν ν' : Fin l}
    (h : ν ≠ ν') (hdeg : (φ ν).natDegree = (φ ν').natDegree) :
    ∑ ρ, (Function.update φ ν' (φ ν' - C ((φ ν').leadingCoeff / (φ ν).leadingCoeff) * φ ν) ρ).natDegree
      < ∑ ρ, (φ ρ).natDegree := by sorry
```

#### Proof sketch
1. `wronskian_update_sub_smul`: show `wronskianMatrix (update φ ν' (φ ν' − C c * φ ν)) = (wronskianMatrix φ).updateCol ν' (fun μ => (wronskianMatrix φ) μ ν' + (−c) • (wronskianMatrix φ) μ ν)` (`Matrix.ext`, `Matrix.updateCol_apply`, `Function.update_apply`, `map_sub`, `Polynomial.C_mul'`/`map_smul`, `Polynomial.smul_eq_C_mul`), then `Matrix.det_updateCol_add_smul_self _ h.symm`.
2. `linearIndependent_update_sub_smul`: `linearIndependent_iff_card_eq_finrank_span` in both directions; the spans agree: `Submodule.span_le.2` each way (`φ ν' = (update …) ν' + C c * (update …) ν`, memberships via `Submodule.sub_mem`, `Submodule.add_mem`, `Submodule.smul_mem`, `Submodule.subset_span`, `Function.update_noteq`/`update_same`).
3. `sum_natDegree_update_lt`: let `c := lc(φ ν')/lc(φ ν)`; `q := C c * φ ν` has `degree q = degree (φ ν')` and `leadingCoeff q = leadingCoeff (φ ν')` (`Polynomial.degree_C_mul`, `leadingCoeff_C_mul`? (`Polynomial.leadingCoeff_mul`, `leadingCoeff_C`), `div_mul_cancel₀`, `hφ.ne_zero`); the difference is nonzero (else `φ ν' = C c * φ ν`, contradicting independence of the pair: `LinearIndependent.pair_iff` via `hφ.comp ![ν, ν'] (injective)` or `linearIndependent_iff'` with the coefficient vector `single ν' 1 − single ν c`); so `Polynomial.degree_sub_lt` gives `degree (φ ν' − q) < degree (φ ν')`, hence `natDegree (φ ν' − q) < natDegree (φ ν')` (`Polynomial.natDegree_lt_natDegree`); conclude with `Finset.sum_lt_sum_of_nonempty`/`Finset.sum_update_of_mem` (all other summands equal, `Function.update_noteq`).

#### Mathlib lemmas needed
- `Matrix.det_updateCol_add_smul_self`, `Matrix.updateCol_apply`, `Function.update_apply`
- `linearIndependent_iff_card_eq_finrank_span`, `Submodule.span_le`, `Submodule.subset_span`
- `Polynomial.degree_sub_lt`, `Polynomial.natDegree_lt_natDegree`, `Polynomial.degree_C_mul`, `Polynomial.leadingCoeff_mul`
- `LinearIndependent.pair_iff`, `Finset.sum_update_of_mem`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 first lemma, clean.tex:174-180
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R4.7, R4.8).

#### Generality decision
- any field `K` (`sum_natDegree_update_lt` needs `LinearIndependent K φ`, see R4.8).

**Progress**:
- 2026-10-12T18:45: DONE


### [T018] Wronskian criterion for linear independence
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: T013, T016, T017, CLEANUP-5
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R4.9

#### Statement
```lean
theorem wronskian_ne_zero_of_linearIndependent [CharZero K] {φ : Fin l → K[X]}
    (h : LinearIndependent K φ) : wronskian φ ≠ 0 := by sorry

theorem wronskian_eq_zero_iff [CharZero K] {φ : Fin l → K[X]} :
    wronskian φ = 0 ↔ ¬ LinearIndependent K φ := by sorry
```

#### Proof sketch
1. Strong induction on `N := ∑ ρ, (φ ρ).natDegree` generalising `φ` (`Nat.strong_induction_on` / `induction N using Nat.strong_induction_on generalizing φ`).
2. Case the degree map `fun ν => (φ ν).natDegree` is injective: `wronskian_ne_zero_of_natDegree_injective` (with `hφ.ne_zero` for nonvanishing).
3. Otherwise obtain `ν ≠ ν'` with equal degrees (`Function.Injective`, `not_forall`, `Classical`); set `φ' := update φ ν' (φ ν' − C c * φ ν)`; `wronskian φ' = wronskian φ` (`wronskian_update_sub_smul`), `LinearIndependent K φ'` (`linearIndependent_update_sub_smul`), `∑ natDegree φ' < N` (`sum_natDegree_update_lt`); apply the IH.
4. `wronskian_eq_zero_iff`: `⟨fun h hli => wronskian_ne_zero_of_linearIndependent hli h, wronskian_eq_zero_of_not_linearIndependent⟩`.

#### Mathlib lemmas needed
- `Nat.strong_induction_on`
- `Function.Injective` (negation: `not_forall`)
- (project) `wronskian_ne_zero_of_natDegree_injective`, `wronskian_update_sub_smul`, `linearIndependent_update_sub_smul`, `sum_natDegree_update_lt`, `wronskian_eq_zero_of_not_linearIndependent`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 first lemma, clean.tex:164-196
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R4.9).

#### Generality decision
- field `K` with `CharZero K`; any `l` (including `l = 0`).

**Progress**:
- 2026-10-12T18:45: DONE


### [CLEANUP-6] Run /cleanup on Roth/Wronskian.lean
- **Status**: done
- **File**: Roth/Wronskian.lean
- **Depends on**: T018
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Wronskian.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T18:45: agent dispatched
- 2026-10-12T18:53: agent cleanup; build clean


### [T019] Translation of multivariate polynomials: definition and basic API
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R2.1, R2.2, R2.4, R2.5

#### Statement
```lean
noncomputable def taylor (α : σ → R) : MvPolynomial σ R →ₐ[R] MvPolynomial σ R :=
  aeval fun j => X j + C (α j)

theorem taylor_apply (α : σ → R) (P : MvPolynomial σ R) :
    taylor α P = aeval (fun j => X j + C (α j)) P := rfl

@[simp]
theorem taylor_X (α : σ → R) (j : σ) : taylor α (X j) = X j + C (α j) := by sorry

@[simp]
theorem taylor_X (α : σ → R) (j : σ) : taylor α (X j) = X j + C (α j) := by sorry

@[simp]
theorem taylor_C (α : σ → R) (a : R) : taylor α (C a) = C a := by sorry

theorem taylor_monomial (α : σ → R) (k : σ →₀ ℕ) (a : R) :
    taylor α (monomial k a) = C a * k.prod fun j n => (X j + C (α j)) ^ n := by sorry

theorem eval_taylor (α x : σ → R) (P : MvPolynomial σ R) :
    eval x (taylor α P) = eval (fun j => x j + α j) P := by sorry

theorem taylor_taylor (α β : σ → R) (P : MvPolynomial σ R) :
    taylor α (taylor β P) = taylor (fun j => α j + β j) P := by sorry

@[simp]
theorem taylor_zero (P : MvPolynomial σ R) : taylor (fun _ => (0 : R)) P = P := by sorry
```

#### Proof sketch
1. `taylor_X`/`taylor_C`: `simp [taylor, aeval_X, aeval_C, algebraMap_eq]`.
2. `taylor_monomial`: `MvPolynomial.aeval_monomial` + `algebraMap_eq`.
3. `eval_taylor`: `MvPolynomial.eval_aeval`? If absent: `taylor_apply`, `MvPolynomial.aeval_eq_eval₂Hom`, `MvPolynomial.eval₂_comp_left`/`eval_eval₂`, then `simp [eval_X, eval_C]`.
4. `taylor_taylor`: `MvPolynomial.algHom_ext` (compare on `X j`): `taylor_X`, `map_add`, `taylor_C`, `C_add`, `add_assoc`. `taylor_zero`: `algHom_ext`, `taylor_X`, `C_0`, `add_zero`, or `MvPolynomial.aeval_X_left`.

#### Mathlib lemmas needed
- `MvPolynomial.aeval_X`, `MvPolynomial.aeval_C`, `MvPolynomial.algebraMap_eq`, `MvPolynomial.aeval_monomial`
- `MvPolynomial.algHom_ext`, `MvPolynomial.aeval_X_left`
- `MvPolynomial.aeval_eq_eval₂Hom`, `MvPolynomial.eval₂_comp_left` (or `MvPolynomial.eval_aeval`)

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lean note clean.tex:546-547; proof of Taylor's theorem clean.tex:521-526
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R2.1, R2.2, R2.4, R2.5).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring`.

**Progress**:
- 2026-10-12T18:48: DONE


### [T020] Coefficients of the translate are the Hasse derivatives (Taylor, coefficient form)
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: T019, T002
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R2.3

#### Statement
```lean
theorem coeff_taylor (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (taylor α P).coeff d = eval α (hasseDeriv d P) := by sorry
```

#### Proof sketch
1. Both sides are additive in `P` (`map_add`, `coeff_add`, `eval_add`) and vanish at `0`; reduce to `P = monomial k a` by `MvPolynomial.induction_on'`.
2. Left side: `taylor_monomial`, expand each factor `(X j + C (α j)) ^ (k j)` by `add_pow` (sum over `range (k j + 1)` of `X j ^ i * C (α j) ^ (k j − i) * (k j).choose i`); `Finsupp.prod` over `k.support` of sums → sum over `Fintype.piFinset`-style functions (`Finset.prod_sum` for a `Finset`-indexed product: `Finset.prod_sum` gives a sum over `pi`), each product being `C (coefficient) * monomial …`; then `coeff_sum`, `coeff_C_mul`, `coeff_monomial`, `Finset.sum_eq_single d`.
3. Right side: `hasseDeriv_monomial`, `eval_monomial`/`eval_C_mul`, `Finsupp.prod` of `α j ^ (k − d) j`, `hasseCoeff` as `Finsupp.prod` of `choose`; match factor by factor over `k.support` (`Finsupp.prod_mul`), using `Nat.choose` vanishing when `d ≰ k` on both sides (`hasseCoeff_eq_zero_iff`, `Nat.choose_eq_zero_of_lt`).
4. Alternative route (same leaf): prove `taylor α (monomial k a) = ∑ d ∈ Finset.Iic k, monomial d (a * hasseCoeff d k * ∏ j, α j ^ (k − d) j)` by induction on `k` via `Finsupp.induction` (`k = single j n + k'`, `taylor` of a product, `Polynomial.add_pow`-type expansion in one variable, `Finset.sum_mul_sum`, `Finsupp.Iic` product structure), then read off coefficients.

#### Mathlib lemmas needed
- `MvPolynomial.induction_on'`, `add_pow`, `Finset.prod_sum`
- `MvPolynomial.coeff_sum`, `MvPolynomial.coeff_C_mul`, `MvPolynomial.coeff_monomial`, `Finset.sum_eq_single`
- `MvPolynomial.eval_monomial`, `Finsupp.prod_mul`, `Finsupp.induction`
- (project) `hasseDeriv_monomial`, `hasseCoeff_eq_zero_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Theorem (Taylor's expansion) and proof, clean.tex:502-526; Lean note clean.tex:546-548
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R2.3).

#### Generality decision
- `σ` arbitrary, `R` any `CommSemiring` (the source: real coefficients).

**Progress**:
- 2026-10-12T18:48: DONE


### [T021] Translation commutes with coefficient maps and renaming; degree bound
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: T020, T003
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R2.6, R2.7, R2.8

#### Statement
```lean
theorem taylor_map {S : Type*} [CommSemiring S] (f : R →+* S) (α : σ → R) (P : MvPolynomial σ R) :
    taylor (fun j => f (α j)) (map f P) = map f (taylor α P) := by sorry

theorem taylor_rename {τ : Type*} (f : σ → τ) (α : τ → R) (P : MvPolynomial σ R) :
    taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by sorry

theorem degreeOf_taylor_le (α : σ → R) (j : σ) (P : MvPolynomial σ R) :
    degreeOf j (taylor α P) ≤ degreeOf j P := by sorry
```

#### Proof sketch
1. `taylor_map`: `MvPolynomial.ext d`; `coeff_taylor` on both sides, `MvPolynomial.coeff_map`, `hasseDeriv_map`, `MvPolynomial.eval_map`/`eval₂_map` (`eval (f ∘ α) (map f Q) = f (eval α Q)`: `MvPolynomial.eval_map`).
2. `taylor_rename`: `taylor_apply`, `MvPolynomial.aeval_rename` (`aeval g (rename k p) = aeval (g ∘ k) p`), and `rename f = aeval (X ∘ f)` (`MvPolynomial.rename` definition / `MvPolynomial.aeval_X_left`-style: `MvPolynomial.rename_eq`? else `MvPolynomial.algHom_ext` comparing on `X i`: `aeval_X`, `rename_X`, `taylor_X`).
3. `degreeOf_taylor_le`: `MvPolynomial.as_sum P`, `map_sum`, `taylor_monomial`; `degreeOf_sum_le`, `degreeOf_C_mul_le`, `Finsupp.prod` → `degreeOf_prod_le`/`degreeOf_pow_le`, `degreeOf_add_le`, `degreeOf_X`, `degreeOf_C`; sum of the bounds is `≤ degreeOf j P` because each `k ∈ support` has `k j ≤ degreeOf j P` (`degreeOf_le_iff`) and the only contribution to variable `j` comes from the factor `(X j + C (α j)) ^ (k j)`.

#### Mathlib lemmas needed
- `MvPolynomial.coeff_map`, `MvPolynomial.eval_map`
- `MvPolynomial.aeval_rename`, `MvPolynomial.rename_X`, `MvPolynomial.algHom_ext`
- `MvPolynomial.degreeOf_sum_le`, `degreeOf_C_mul_le`, `degreeOf_prod_le`, `degreeOf_pow_le`, `degreeOf_add_le`, `degreeOf_X`, `degreeOf_C`, `degreeOf_le_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §1 Lean note clean.tex:151-152; §4 Lemma 4-2 clean.tex:621-624; §5 clean.tex:665-668
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R2.6, R2.7, R2.8).

#### Generality decision
- `R` any `CommSemiring`; `taylor_rename` for any `f` (no injectivity needed).

**Progress**:
- 2026-10-12T18:48: DONE


### [CLEANUP-7] Run /cleanup on Roth/Taylor.lean
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: T021
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Taylor.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:00: agent cleanup of Taylor/CoeffNorm; build clean


### [T022] Translation is invertible
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: T019, CLEANUP-7
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R2.9

#### Statement
```lean
theorem taylor_neg_taylor (α : σ → A) (P : MvPolynomial σ A) :
    taylor (fun j => -α j) (taylor α P) = P := by sorry

theorem taylor_injective (α : σ → A) : Function.Injective (taylor α : MvPolynomial σ A → _) := by
  sorry

@[simp]
theorem taylor_eq_zero_iff (α : σ → A) (P : MvPolynomial σ A) : taylor α P = 0 ↔ P = 0 := by sorry
```

#### Proof sketch
1. `taylor_neg_taylor`: `taylor_taylor`, `neg_add_cancel`, `taylor_zero` (over a `CommRing A`).
2. `taylor_injective`: `Function.LeftInverse.injective (taylor_neg_taylor α)`.
3. `taylor_eq_zero_iff`: `(taylor_injective α).eq_iff' (map_zero _)`.

#### Mathlib lemmas needed
- `Function.LeftInverse.injective`, `Function.Injective.eq_iff'`, `map_zero`
- (project) `taylor_taylor`, `taylor_zero`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 clean.tex:546 (translation by −α inverts translation by α)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R2.9).

#### Generality decision
- `A` any `CommRing` (needs negation).

**Progress**:
- 2026-10-12T18:48: DONE


### [T023] Taylor's theorem for multivariate polynomials (polynomial and evaluation form)
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: T020, T021, T022, T010, CLEANUP-7
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R2.10

#### Statement
```lean
theorem eq_sum_box_hasseDeriv [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by sorry

theorem eval_eq_sum_box [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by sorry
```

#### Proof sketch
1. `eq_sum_box_hasseDeriv`: `P = taylor (fun j => −α j) (taylor α P)` (`taylor_neg_taylor`); write `taylor α P = ∑ d ∈ (taylor α P).support, monomial d (coeff d (taylor α P))` (`as_sum`), extend the sum to `box r` (`Finset.sum_subset`: support ⊆ box by `degreeOf_taylor_le` + `degreeOf_le_iff` + `mem_box`; terms off the support vanish by `MvPolynomial.notMem_support_iff`), apply `map_sum`, `taylor_monomial` (with `X j + C (−α j) = X j − C (α j)`: `C_neg`, `sub_eq_add_neg`), `coeff_taylor`, and `Finsupp.prod` over `d.support` = `∏ j` (`Finsupp.prod_fintype`, `pow_zero`).
2. `eval_eq_sum_box`: apply `eval x` to the previous identity: `map_sum`, `eval_mul`, `eval_C`, `eval_prod`, `eval_pow`, `eval_sub`, `eval_X`.

#### Mathlib lemmas needed
- `MvPolynomial.as_sum`, `Finset.sum_subset`, `MvPolynomial.notMem_support_iff`
- `Finsupp.prod_fintype`, `MvPolynomial.C_neg`
- `MvPolynomial.eval_prod`, `eval_pow`, `eval_sub`, `eval_mul`, `eval_C`, `eval_X`
- (project) `taylor_neg_taylor`, `taylor_monomial`, `coeff_taylor`, `degreeOf_taylor_le`, `mem_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Theorem (Taylor's expansion), clean.tex:502-508; §7 clean.tex:1655-1658
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R2.10).

#### Generality decision
- `A` any `CommRing`, `[Fintype σ] [DecidableEq σ]`; summation over the box `r` with `degreeOf j P ≤ r j` (the source's `d_i ≥ r_i` is the same up to zero terms).

**Progress**:
- 2026-10-12T18:48: DONE


### [CLEANUP-8] Run /cleanup on Roth/Taylor.lean
- **Status**: done
- **File**: Roth/Taylor.lean
- **Depends on**: T023
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Taylor.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:00: agent cleanup of Taylor/CoeffNorm; build clean


### [T024] ℓ¹ coefficient norm: definition, triangle inequality, sup bound
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R3.1, R3.2, R3.4

#### Statement
```lean
noncomputable def normOne (P : MvPolynomial σ ℤ) : ℝ := ∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|

theorem normOne_nonneg (P : MvPolynomial σ ℤ) : 0 ≤ normOne P := by sorry

@[simp]
theorem normOne_zero : normOne (0 : MvPolynomial σ ℤ) = 0 := by sorry

theorem abs_coeff_le_normOne (P : MvPolynomial σ ℤ) (d : σ →₀ ℕ) :
    |((P.coeff d : ℤ) : ℝ)| ≤ normOne P := by sorry

theorem normOne_add_le (P Q : MvPolynomial σ ℤ) : normOne (P + Q) ≤ normOne P + normOne Q := by
  sorry

theorem normOne_neg (P : MvPolynomial σ ℤ) : normOne (-P) = normOne P := by sorry

theorem normOne_sum_le {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, normOne (f i) := by sorry

theorem normOne_le_card_mul (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) :
    normOne P ≤ P.support.card * B := by sorry
```

#### Proof sketch
1. `normOne_nonneg`: `Finset.sum_nonneg (fun _ _ => abs_nonneg _)`. `normOne_zero`: `simp [normOne]`.
2. `abs_coeff_le_normOne`: if `d ∈ P.support` then `Finset.single_le_sum` (nonneg terms); else `coeff d P = 0` (`MvPolynomial.notMem_support_iff`), `abs_zero`, `normOne_nonneg`.
3. `normOne_add_le`: rewrite both norms as sums over `P.support ∪ Q.support` (`Finset.sum_subset`, zero terms off the support), `coeff_add`, `Int.cast_add`, `abs_add`, `Finset.sum_le_sum`, `Finset.sum_add_distrib`; `support_add` (`MvPolynomial.support_add` ⊆ union).
4. `normOne_neg`: `MvPolynomial.support_neg`, `coeff_neg`, `Int.cast_neg`, `abs_neg`. `normOne_sum_le`: `Finset.induction_on` with `normOne_add_le`, `normOne_zero`.
5. `normOne_le_card_mul`: `Finset.sum_le_card_nsmul _ _ B (fun d _ => hB d)`, `nsmul_eq_mul`.

#### Mathlib lemmas needed
- `Finset.sum_nonneg`, `Finset.single_le_sum`, `MvPolynomial.notMem_support_iff`
- `Finset.sum_subset`, `MvPolynomial.support_add`, `abs_add`, `Finset.sum_add_distrib`
- `MvPolynomial.support_neg`, `MvPolynomial.coeff_neg`, `abs_neg`
- `Finset.sum_le_card_nsmul`, `nsmul_eq_mul`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §3 proof of Lemma 3, clean.tex:446-456 and Lean note clean.tex:482-488
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.1, R3.2, R3.4).

#### Generality decision
- `σ` arbitrary; integer polynomials, real-valued norm (the only coefficient ring used by the source for norms).

**Progress**:
- 2026-10-12T18:52: DONE


### [T025] Submultiplicativity of the ℓ¹ norm
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R3.3

#### Statement
```lean
theorem normOne_mul_le [DecidableEq σ] (P Q : MvPolynomial σ ℤ) :
    normOne (P * Q) ≤ normOne P * normOne Q := by sorry

theorem normOne_prod_le [DecidableEq σ] {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) :
    normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, normOne (f i) := by sorry
```

#### Proof sketch
1. `normOne_mul_le`: `normOne (P*Q) = ∑_{d ∈ supp(PQ)} |∑_{(a,b) ∈ antidiagonal d} p_a q_b|` (`MvPolynomial.coeff_mul`) `≤ ∑_{d ∈ supp(PQ)} ∑_{(a,b) ∈ antidiagonal d} |p_a||q_b|` (`Finset.abs_sum_le_sum_abs`, `abs_mul`, `Int.cast_mul`).
2. Bound the double sum by `∑_{a ∈ supp P} ∑_{b ∈ supp Q} |p_a||q_b|`: terms with `a ∉ supp P` or `b ∉ supp Q` vanish; use `Finset.sum_le_sum_of_subset_of_nonneg` after rewriting the sum over `(d, (a,b))` with `a + b = d` as a sum over `supp P ×ˢ supp Q` via `Finset.sum_sigma'`/`Finset.sum_bij`/`Finset.sum_comm'` (map `(a,b) ↦ (a+b, (a,b))`, injective) — or avoid antidiagonals: `P * Q = ∑_{a ∈ supp P} ∑_{b ∈ supp Q} monomial (a+b) (p_a q_b)` (`as_sum`, `Finset.sum_mul_sum`, `monomial_mul`), then `normOne_sum_le` twice and `normOne (monomial _ c) = |c|` (`MvPolynomial.support_monomial`, `coeff_monomial`).
3. Finish with `Finset.sum_mul_sum` (`(∑ |p_a|)(∑ |q_b|) = ∑∑ |p_a||q_b|`). `normOne_prod_le`: `Finset.induction_on`, `normOne_mul_le`, `normOne` of `1` is `1` (`support_one`/`coeff_one`), `mul_le_mul` with nonnegativity.

#### Mathlib lemmas needed
- `MvPolynomial.as_sum`, `Finset.sum_mul_sum`, `MvPolynomial.monomial_mul`, `MvPolynomial.support_monomial`
- `Finset.abs_sum_le_sum_abs`, `abs_mul`, `Finset.sum_le_sum_of_subset_of_nonneg`
- `Finset.prod_induction`/`Finset.induction_on`, `mul_le_mul`
- (project) `normOne_sum_le`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §3 Lean note clean.tex:484-485; clean.tex:451-452
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.3).

#### Generality decision
- `[DecidableEq σ]` only for `coeff_mul`; integer polynomials.

**Progress**:
- 2026-10-12T18:52: DONE


### [T026] ℓ¹ norm of a determinant
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T024, T025
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R3.5

#### Statement
```lean
theorem normOne_det_le [DecidableEq σ] {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ))
    {C : ℝ} (hC : 0 ≤ C) (hM : ∀ μ ν, normOne (M μ ν) ≤ C) :
    normOne M.det ≤ l.factorial * C ^ l := by sorry
```

#### Proof sketch
1. `Matrix.det_apply'`: `det M = ∑ σ, ε σ * ∏ i, M (σ i) i`; `normOne_sum_le`.
2. For each `σ`: `ε σ = ±1` (`Int.units_eq_one_or (Equiv.Perm.sign σ)`), so `normOne (ε σ * p) = normOne p` (`one_mul`; `Int.cast_neg`, `neg_one_mul`, `normOne_neg`); `normOne_prod_le`, `Finset.prod_le_prod (fun _ _ => normOne_nonneg _) (fun i _ => hM _ _)`, `Finset.prod_const`, `Finset.card_fin`.
3. Sum of `l!` equal bounds: `Finset.sum_le_card_nsmul`, `Finset.card_univ`, `Fintype.card_perm`, `Fintype.card_fin`, `nsmul_eq_mul`.

#### Mathlib lemmas needed
- `Matrix.det_apply'`, `Int.units_eq_one_or`, `Equiv.Perm.sign`
- `Finset.prod_le_prod`, `Finset.prod_const`, `Finset.sum_le_card_nsmul`, `Fintype.card_perm`
- (project) `normOne_sum_le`, `normOne_prod_le`, `normOne_neg`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §3 proof of Lemma 3, clean.tex:467-479
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.5).

#### Generality decision
- any `l`; entries in `MvPolynomial σ ℤ`; `0 ≤ C`.

**Progress**:
- 2026-10-12T18:52: DONE


### [CLEANUP-9] Run /cleanup on Roth/CoeffNorm.lean
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T026
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/CoeffNorm.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:00: agent cleanup of Taylor/CoeffNorm; build clean


### [T027] Coefficient bounds for Hasse derivatives
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T002, T007, CLEANUP-9
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R3.6, R3.7

#### Statement
```lean
theorem abs_coeff_hasseDeriv_le [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ e, |((P.coeff e : ℤ) : ℝ)| ≤ B) (e : σ →₀ ℕ) :
    |(((hasseDeriv d P).coeff e : ℤ) : ℝ)| ≤ 2 ^ (∑ j, r j) * B := by sorry

theorem normOne_hasseDeriv_le [Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P := by
  sorry
```

#### Proof sketch
1. `abs_coeff_hasseDeriv_le`: `coeff_hasseDeriv`, `Int.cast_mul`, `abs_mul`, `Nat.abs_cast`; if `coeff (e+d) P = 0` the LHS is `0 ≤ 2^S B` (`0 ≤ B` from `hB e` and `abs_nonneg`); else `(e+d) ∈ support` so `(e+d) j ≤ r j` (`degreeOf_le_iff`) and `hasseCoeff_le_two_pow`; `mul_le_mul` with `hB`.
2. `normOne_hasseDeriv_le`: `normOne (Δ_d P) = ∑_{e ∈ supp(Δ_d P)} |c_d(e+d)| |coeff (e+d) P|`; the map `e ↦ e + d` is injective (`add_left_injective d`) and sends `supp (Δ_d P)` into `supp P` (`coeff_hasseDeriv`, `mul_ne_zero_iff`); so `≤ ∑_{e ∈ supp(Δ_d P)} 2^S |coeff (e+d) P| = 2^S ∑_{k ∈ (supp Δ_d P).image (·+d)} |coeff k P| ≤ 2^S ∑_{k ∈ supp P} |coeff k P|` (`Finset.sum_image`, `Finset.sum_le_sum_of_subset_of_nonneg`, `Finset.mul_sum`).

#### Mathlib lemmas needed
- `Int.cast_mul`, `abs_mul`, `Nat.abs_cast`, `mul_le_mul`
- `Finset.sum_image`, `add_left_injective`, `Finset.sum_le_sum_of_subset_of_nonneg`, `Finset.mul_sum`
- (project) `coeff_hasseDeriv`, `hasseCoeff_le_two_pow`, `degreeOf_le_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §3 clean.tex:457-461; §6 clean.tex:1443-1446; Lean note clean.tex:486-488
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.6, R3.7).

#### Generality decision
- `[Fintype σ]`, integer polynomials, real bounds.

**Progress**:
- 2026-10-12T18:52: DONE


### [T028] Diagonal substitution: additivity, evaluation, coefficient and degree bounds
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T024, CLEANUP-9
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R3.10, R3.11, R3.12

#### Statement
```lean
noncomputable def diag (P : MvPolynomial σ ℤ) : Polynomial ℤ := aeval (fun _ => Polynomial.X) P

theorem diag_sub (P Q : MvPolynomial σ ℤ) : diag (P - Q) = diag P - diag Q := by sorry

theorem eval_diag (P : MvPolynomial σ ℤ) (x : ℝ) :
    Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (diag P)) =
      eval (fun _ => x) (map (Int.castRingHom ℝ) P) := by sorry

theorem abs_coeff_diag_le (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B)
    (n : ℕ) : |(((diag P).coeff n : ℤ) : ℝ)| ≤ P.support.card * B := by sorry

theorem natDegree_diag_le [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) : (diag P).natDegree ≤ ∑ j, r j := by sorry
```

#### Proof sketch
1. `diag_sub`: `map_sub`. `eval_diag`: `diag P = aeval (fun _ => X) P`; `Polynomial.eval_map`+`Polynomial.eval₂_at_apply`-style: `Polynomial.eval x (map (Int.castRingHom ℝ) (aeval (fun _ => X) P)) = eval (fun _ => x) (map _ P)`: use `MvPolynomial.aeval_eq_eval₂Hom`, `MvPolynomial.eval₂_comp_left`/`MvPolynomial.map_aeval`, `Polynomial.eval_map`, `Polynomial.eval₂_X`, `MvPolynomial.eval_map`; or `MvPolynomial.induction_on P` (cases `C`, `+`, `* X j`) with `simp`.
2. `abs_coeff_diag_le`: `MvPolynomial.as_sum P`, `map_sum`, `MvPolynomial.aeval_monomial` (`= C a * X ^ (∑ k j)` via `Finsupp.prod` of `X ^ k j` = `X ^ (k.sum fun _ n => n)`: `Finsupp.prod_pow`? / `pow_finset_sum`), `Polynomial.finset_sum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.abs_sum_le_sum_abs`, each term `≤ B` (`abs_ite`/`ite_le`), `Finset.sum_le_card_nsmul`.
3. `natDegree_diag_le`: same expansion; `Polynomial.natDegree_sum_le`, `Polynomial.natDegree_C_mul_X_pow_le`, `Finset.sup_le`, `k.sum ≤ ∑ j, r j` (`degreeOf_le_iff`, `Finsupp.sum_fintype`, `Finset.sum_le_sum`).

#### Mathlib lemmas needed
- `MvPolynomial.as_sum`, `MvPolynomial.aeval_monomial`, `pow_finset_sum`
- `Polynomial.finset_sum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.abs_sum_le_sum_abs`, `Finset.sum_le_card_nsmul`
- `Polynomial.natDegree_sum_le`, `Polynomial.natDegree_C_mul_X_pow_le`
- `Polynomial.eval_map`, `MvPolynomial.eval_map`, `MvPolynomial.aeval_eq_eval₂Hom`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1441-1449, 1463-1464, 1505-1510
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.10, R3.11, R3.12).

#### Generality decision
- `σ` arbitrary (Fintype for the degree bound); integer polynomials.

**Progress**:
- 2026-10-12T18:52: DONE


### [T029] Geometric-sum bound and evaluation bound
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T010, CLEANUP-9
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R3.13, R3.14

#### Statement
```lean
theorem geom_sum_le_one_add_pow {t : ℝ} (ht : 0 ≤ t) (r : ℕ) :
    ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r := by sorry

theorem abs_eval_le [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j)
    {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (x : σ → ℝ) :
    |eval x (map (Int.castRingHom ℝ) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j := by sorry
```

#### Proof sketch
1. `geom_sum_le_one_add_pow`: `add_comm 1 t`, `add_pow` (`(t + 1)^r = ∑ s ∈ range (r+1), t^s * 1^(r-s) * r.choose s`), `one_pow`, `mul_one`, `Finset.sum_le_sum` with `le_mul_of_one_le_right (pow_nonneg ht s) (by exact_mod_cast Nat.one_le_iff_ne_zero.2 (Nat.choose_pos (Finset.mem_range_succ_iff.1 hs)).ne')`.
2. `abs_eval_le`: `MvPolynomial.eval_eq`/`as_sum` + `map_sum` + `eval_monomial`: `eval x (map P) = ∑_{k ∈ supp} (coeff k P) * ∏ j, x j ^ k j`; `Finset.abs_sum_le_sum_abs`, `abs_mul`, `abs_prod`, `abs_pow`, `hB`, `Finset.sum_le_sum`, then extend to `box r` (`Finset.sum_le_sum_of_subset_of_nonneg`, support ⊆ box by `degreeOf_le_iff`), factor `∑_{d ∈ box r} ∏ j |x j|^{d j} = ∏ j ∑_{s ≤ r j} |x j|^s` (`box` as a mapped `piFinset`: `Finset.sum_map`, `Finset.prod_univ_sum`, `Finsupp.equivFunOnFinite_symm_apply_toFun`), bound each factor by `geom_sum_le_one_add_pow` (`Finset.prod_le_prod` with nonnegativity), `Finset.mul_sum`.

#### Mathlib lemmas needed
- `add_pow`, `Nat.choose_pos`, `le_mul_of_one_le_right`
- `MvPolynomial.eval_monomial`, `Finset.abs_sum_le_sum_abs`, `abs_prod`, `abs_pow`
- `Finset.sum_map`, `Finset.prod_univ_sum`, `Finset.prod_le_prod`, `Finset.sum_le_sum_of_subset_of_nonneg`
- (project) `mem_box`, `card_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1545-1552
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.13, R3.14).

#### Generality decision
- `[Fintype σ] [DecidableEq σ]`; any real point `x`.

**Progress**:
- 2026-10-12T18:52: DONE


### [CLEANUP-10] Run /cleanup on Roth/CoeffNorm.lean
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T029
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/CoeffNorm.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:00: agent cleanup of Taylor/CoeffNorm; build clean


### [T030] Lemma 3: degree and coefficient bounds for the determinant of Hasse derivatives
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T026, T027, T010, T007, CLEANUP-10
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R3.8, R3.9

#### Statement
```lean
theorem degreeOf_det_hasseDeriv_le {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ)
    {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) (j : σ) :
    degreeOf j (Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P).det ≤ l * r j := by sorry

theorem abs_coeff_det_hasseDeriv_le [Fintype σ] [DecidableEq σ] {l : ℕ}
    (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB0 : 0 ≤ B) (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B)
    (d : σ →₀ ℕ) :
    |(((Matrix.of fun μ ν : Fin l => hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤
      (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l) := by sorry
```

#### Proof sketch
1. `degreeOf_det_hasseDeriv_le`: `Matrix.det_apply'`, `MvPolynomial.degreeOf_sum_le`, `Finset.sup_le`; each term `ε σ * ∏ …`: `degreeOf_C_mul_le`-type bound for the integer sign (`Int.cast` of `±1`: `Int.units_eq_one_or`, `degreeOf_neg`, `one_mul`), `degreeOf_prod_le`, `degreeOf_hasseDeriv_le`, `Finset.sum_le_sum`, `Finset.sum_const`, `Finset.card_fin`, `smul_eq_mul`.
2. `abs_coeff_det_hasseDeriv_le`: `abs_coeff_le_normOne`; `normOne_det_le` with `C := 2 ^ (∑ r_j) * (∏ (r_j+1)) * B` (nonneg), each entry bounded by `normOne_hasseDeriv_le` and `normOne_le_card_mul` + `card_le_card_box` (support ⊆ box: `degreeOf_le_iff`); then rearrange `l! * (2^S N B)^l = N^l * l! * B^l * 2^(S l)` (`mul_pow`, `pow_mul`, `Nat.cast_pow`, `ring`).

#### Mathlib lemmas needed
- `Matrix.det_apply'`, `MvPolynomial.degreeOf_sum_le`, `degreeOf_prod_le`, `degreeOf_neg`
- `mul_pow`, `pow_mul`, `Nat.cast_prod`
- (project) `degreeOf_hasseDeriv_le`, `abs_coeff_le_normOne`, `normOne_det_le`, `normOne_hasseDeriv_le`, `normOne_le_card_mul`, `card_le_card_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §3 Lemma 3, clean.tex:438-479; §2 clean.tex:435-437
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R3.8, R3.9).

#### Generality decision
- arbitrary multi-indices `E μ ν` (more general than the source's `Δ_μ Δ^{(p)}_ν`); `0 ≤ B`.

**Progress**:
- 2026-10-12T18:52: DONE


### [CLEANUP-11] Run /cleanup on Roth/CoeffNorm.lean
- **Status**: done
- **File**: Roth/CoeffNorm.lean
- **Depends on**: T030
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/CoeffNorm.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:00: agent cleanup of Taylor/CoeffNorm; build clean


### [T031] Generalized Wronskian of a dependent family vanishes
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + lemma
- **Decomposition entries**: R5.1, R5.2

#### Statement
```lean
noncomputable def genWronskian (D : Fin l → (σ →₀ ℕ)) (φ : Fin l → MvPolynomial σ K) :
    MvPolynomial σ K :=
  (Matrix.of fun μ ν => hasseDeriv (D μ) (φ ν)).det

theorem genWronskian_eq_zero_of_not_linearIndependent (D : Fin l → (σ →₀ ℕ))
    {φ : Fin l → MvPolynomial σ K} (h : ¬ LinearIndependent K φ) : genWronskian D φ = 0 := by
  sorry
```

#### Proof sketch
1. As T013 with `K[X]` replaced by the domain `MvPolynomial σ K` (`MvPolynomial.instIsDomain`): `Fintype.not_linearIndependent_iff`, `v ν := C (g ν)`, `Matrix.mulVec` entry `= hasseDeriv (D μ) (∑ g ν • φ ν) = 0` (`map_sum`, `map_smul`, `MvPolynomial.smul_eq_C_mul`), `Matrix.exists_mulVec_eq_zero_iff`.

#### Mathlib lemmas needed
- `Fintype.not_linearIndependent_iff`, `Matrix.exists_mulVec_eq_zero_iff`
- `MvPolynomial.smul_eq_C_mul`, `MvPolynomial.C_ne_zero`, `MvPolynomial.instIsDomain`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 second lemma, clean.tex:212-222
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.1, R5.2).

#### Generality decision
- any field `K` (the source's characteristic-zero hypothesis is not needed).

**Progress**:
- 2026-10-12T18:53: DONE


### [T032] Kronecker substitution: monomials, injectivity of exponents, coefficients
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R5.3, R5.4, R5.5

#### Statement
```lean
noncomputable def kronecker (k : ℕ) : MvPolynomial σ K →ₐ[K] Polynomial K :=
  aeval fun j => Polynomial.X ^ (k ^ (Fintype.equivFin σ j : ℕ))

noncomputable def kroneckerExp (k : ℕ) (d : σ →₀ ℕ) : ℕ := ∑ j, d j * k ^ (Fintype.equivFin σ j : ℕ)

theorem kronecker_monomial (k : ℕ) (d : σ →₀ ℕ) (a : K) :
    kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d := by sorry

theorem kroneckerExp_injOn {k : ℕ} (hk : 1 < k) :
    Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by sorry

theorem coeff_kronecker {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k)
    {d : σ →₀ ℕ} (hd : ∀ j, d j < k) : (kronecker k P).coeff (kroneckerExp k d) = P.coeff d := by
  sorry

theorem kronecker_eq_zero_iff {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K}
    (hP : ∀ j, degreeOf j P < k) : kronecker k P = 0 ↔ P = 0 := by sorry
```

#### Proof sketch
1. `kronecker_monomial`: `MvPolynomial.aeval_monomial`, `Polynomial.algebraMap_eq`/`Polynomial.C_eq_algebraMap`, `Finsupp.prod_fintype` (zero exponents give `1`), `pow_mul`, `Finset.prod_pow_eq_pow_sum`.
2. `kroneckerExp_injOn`: for `d, d'` with all entries `< k`, the lists `List.ofFn (fun i : Fin (card σ) => d (e.symm i))` have `Nat.ofDigits k L = kroneckerExp k d` (`Nat.ofDigits_eq_sum_mapIdx`/induction on the list with `Nat.ofDigits_cons`, `Fin.sum_univ_eq_sum_range` after reindexing by `e`), so `Nat.ofDigits_inj_of_len_eq hk (by simp) (digits < k) (digits < k) h` gives `L = L'`, hence `d = d'` (`List.ofFn_inj`, `Finsupp.ext`, `e.symm.surjective`).
3. `coeff_kronecker`: `MvPolynomial.as_sum P`, `map_sum`, `kronecker_monomial`, `Polynomial.finset_sum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single d` (other `d' ∈ supp` have `d' ≠ d`, hence `kroneckerExp k d' ≠ kroneckerExp k d` by `kroneckerExp_injOn` since `d' j ≤ degreeOf j P < k`), `Finset.sum_ite_eq`; if `d ∉ supp` both sides are `0`.
4. `kronecker_eq_zero_iff`: `⟨fun h => MvPolynomial.ext fun d => ?_, fun h => h ▸ map_zero _⟩`; for `d`: if some `d j ≥ k` then `coeff d P = 0` (`degreeOf_lt_iff`), else `coeff_kronecker` and `Polynomial.coeff_zero`.

#### Mathlib lemmas needed
- `MvPolynomial.aeval_monomial`, `Finsupp.prod_fintype`, `Finset.prod_pow_eq_pow_sum`, `pow_mul`
- `Nat.ofDigits_inj_of_len_eq`, `Nat.ofDigits_cons`, `List.ofFn_inj`, `Fin.sum_univ_eq_sum_range`
- `Polynomial.finset_sum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Finset.sum_eq_single`, `MvPolynomial.degreeOf_lt_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 1, clean.tex:226-264 and Lean note clean.tex:265-270
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.3, R5.4, R5.5).

#### Generality decision
- `[Fintype σ]` with the enumeration `Fintype.equivFin σ`; any field `K`; `1 < k`.

**Progress**:
- 2026-10-12T18:53: DONE


### [T033] Kronecker substitution preserves linear independence of bounded-degree families
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: T032
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R5.6

#### Statement
```lean
theorem linearIndependent_kronecker {k : ℕ} (hk : 1 < k) {φ : Fin l → MvPolynomial σ K}
    (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent K φ) :
    LinearIndependent K fun ν => kronecker k (φ ν) := by sorry
```

#### Proof sketch
1. `LinearIndependent.map h (f := (kronecker k).toLinearMap)`; the required `Disjoint (span K (range φ)) (LinearMap.ker _)`: `Submodule.disjoint_def.2`: an element `P` of the span lies in `MvPolynomial.restrictDegree σ K (k−1)` (`Submodule.span_le.2` with `mem_restrictDegree_iff_sup` and `hφ`: `degreeOf j (φ ν) ≤ k − 1`), so `kronecker k P = 0 → P = 0` by `kronecker_eq_zero_iff` (`degreeOf j P < k` from `≤ k−1`, `Nat.lt_of_le_pred`).

#### Mathlib lemmas needed
- `LinearIndependent.map`, `Submodule.disjoint_def`, `Submodule.span_le`
- `MvPolynomial.restrictDegree`, `MvPolynomial.mem_restrictDegree_iff_sup`
- (project) `kronecker_eq_zero_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 1, clean.tex:233-264
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.6).

#### Generality decision
- any field `K`, `1 < k`, degrees `< k`.

**Progress**:
- 2026-10-12T18:53: DONE


### [CLEANUP-12] Run /cleanup on Roth/GenWronskian.lean
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: T033
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/GenWronskian.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:01: agent dispatched (GenWronskian/Lattice)
- 2026-10-12T19:01: agent dispatched
- 2026-10-12T19:13: agent cleanup; build clean


### [T034] Algebraic chain rule for substitution into one variable
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: CLEANUP-12
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R5.7

#### Statement
```lean
theorem derivative_aeval (γ : σ → Polynomial K) (P : MvPolynomial σ K) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) := by sorry
```

#### Proof sketch
1. `MvPolynomial.induction_on P`: case `C a`: `aeval_C`, `Polynomial.derivative_C`/`derivative_algebraMap`, `pderiv_C`, `map_zero`, `Finset.sum_const_zero`. Case `P + Q`: `map_add`, `Polynomial.derivative_add`, `pderiv` additive, `Finset.sum_add_distrib`, `mul_add`.
2. Case `P * X j`: `map_mul`, `aeval_X`, `Polynomial.derivative_mul`, IH; on the right `MvPolynomial.pderiv_mul`, `pderiv_X` (`Pi.single`), `map_add`, `map_mul`, `Finset.sum_add_distrib`, `Finset.mul_sum`; the second sum collapses by `Finset.sum_ite_eq`/`Pi.single_apply` to `derivative (γ j) * aeval γ P`; `ring`.

#### Mathlib lemmas needed
- `MvPolynomial.induction_on`, `MvPolynomial.aeval_X`, `MvPolynomial.aeval_C`
- `Polynomial.derivative_mul`, `Polynomial.derivative_add`, `Polynomial.derivative_C`
- `MvPolynomial.pderiv_mul`, `MvPolynomial.pderiv_X`, `MvPolynomial.pderiv_C`, `Finset.sum_ite_eq`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 1, FACT clean.tex:281-290; Lean note clean.tex:306-309
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.7).

#### Generality decision
- `[Fintype σ]`; any field `K` (works over any `CommRing`); arbitrary `γ : σ → K[X]`.

**Progress**:
- 2026-10-12T18:57: DONE


### [T035] Uniform expansion of Hasse derivatives of a Kronecker substitute
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: T034, T006, CLEANUP-12
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R5.8

#### Statement
```lean
theorem exists_hasseDeriv_kronecker_eq_sum [CharZero K] (k μ : ℕ) :
    ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧
      ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (kronecker k P) =
        ∑ d ∈ s, c d * kronecker k (hasseDeriv d P) := by sorry
```

#### Proof sketch
1. Induction on `μ`. Base: `s = {0}`, `c 0 = 1`: `Polynomial.hasseDeriv_zero'`, `hasseDeriv_zero_apply`, `Finset.sum_singleton`, `one_mul`.
2. Step: from `(s, c)` for `μ`, use `(μ+1 : K) • hasseDeriv (μ+1) f = derivative (hasseDeriv μ f)` (from `Polynomial.hasseDeriv_comp 1 μ`, `hasseDeriv_one'`, `Nat.choose_one_right`, `LinearMap.comp_apply`), divide by `(μ+1 : K) ≠ 0` (`Nat.cast_add_one_ne_zero`, `smul_right_injective`/`inv_smul_smul₀`).
3. `derivative (∑ d ∈ s, c d * kronecker k (Δ_d P)) = ∑ d ∈ s, (derivative (c d) * kronecker k (Δ_d P) + c d * ∑ j, derivative (γ j) * kronecker k (pderiv j (Δ_d P)))` (`Polynomial.derivative_sum`, `derivative_mul`, `derivative_aeval` with `γ j = X ^ (k ^ e j)`), and `pderiv j (Δ_d P) = (d j + 1) • Δ_{d + single j 1} P` (`pderiv_hasseDeriv`, `map_smul`/`map_natCast_smul`).
4. Define `s' := s ∪ s.biUnion (fun d => Finset.univ.image fun j => d + Finsupp.single j 1)` and `c' d' := (μ+1 : K)⁻¹ • (derivative (c d') + ∑ j, ∑ d ∈ s.filter (fun d => d + single j 1 = d'), c d * derivative (γ j) * (d j + 1))` (with `c d' := 0`-convention outside `s`); prove the identity by `Finset.sum_comm`, `Finset.sum_fiberwise`/`Finset.sum_filter`, `Finset.sum_biUnion`-free reindexing (`Finset.sum_image` is not injective — use `Finset.sum_fiberwise_of_maps_to` on the map `(d, j) ↦ d + single j 1` from `s ×ˢ univ` into `s'`). Degrees: `Finsupp.degree_add`, `Finsupp.degree_single`, `Nat.succ_le_succ`.

#### Mathlib lemmas needed
- `Polynomial.hasseDeriv_comp`, `Polynomial.hasseDeriv_one'`, `Polynomial.hasseDeriv_zero'`, `Nat.choose_one_right`
- `Polynomial.derivative_sum`, `Polynomial.derivative_mul`, `Nat.cast_add_one_ne_zero`
- `Finset.sum_comm`, `Finset.sum_fiberwise_of_maps_to`, `Finset.sum_filter`, `Finsupp.degree_add`, `Finsupp.degree_single`
- (project) `derivative_aeval`, `pderiv_hasseDeriv`, `hasseDeriv_zero_apply`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 1, clean.tex:292-314
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.8).

#### Generality decision
- field `K` with `CharZero K` (division by `μ+1`); any `k`; `[Fintype σ]`.

**Progress**:
- 2026-10-12T18:57: DONE


### [T036] Multilinear expansion of a determinant whose rows are sums
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: CLEANUP-12
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R5.9

#### Statement
```lean
theorem det_sum_rows {A : Type*} [CommRing A] {ι : Type*} [DecidableEq ι] (s : Fin l → Finset ι)
    (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) :
    (Matrix.of fun μ ν => ∑ i ∈ s μ, c μ i * N μ i ν).det =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν => N μ (f μ) ν).det := by
  sorry
```

#### Proof sketch
1. `Matrix.det M = Matrix.detRowAlternating M` (unfold `Matrix.det`); the matrix `of fun μ ν => ∑ i ∈ s μ, c μ i * N μ i ν` is `fun μ => ∑ i ∈ s μ, c μ i • N μ i` as a family of rows (`funext`, `Finset.sum_apply`, `Pi.smul_apply`, `smul_eq_mul`).
2. `MultilinearMap.map_sum_finset (detRowAlternating).toMultilinearMap` gives the sum over `Fintype.piFinset s`; then `MultilinearMap.map_smul_univ` pulls out `∏ μ, c μ (f μ)` (`smul_eq_mul`); conclude with `Matrix.det` of `of fun μ ν => N μ (f μ) ν` (`Matrix.of_apply`, `rfl`).

#### Mathlib lemmas needed
- `Matrix.det`, `Matrix.detRowAlternating`
- `MultilinearMap.map_sum_finset`, `MultilinearMap.map_smul_univ`, `AlternatingMap.coe_multilinearMap`
- `Finset.sum_apply`, `Pi.smul_apply`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 1, clean.tex:331-343
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.9).

#### Generality decision
- any `CommRing A`, any index type `ι` with `DecidableEq`, any `l`.

**Progress**:
- 2026-10-12T18:57: DONE


### [CLEANUP-13] Run /cleanup on Roth/GenWronskian.lean
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: T036
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/GenWronskian.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:01: agent dispatched (GenWronskian/Lattice)
- 2026-10-12T19:01: agent dispatched
- 2026-10-12T19:13: agent cleanup; build clean


### [T037] Lemma 1: a linearly independent family has a nonvanishing generalized Wronskian
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: T031, T033, T035, T036, T018, CLEANUP-13
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R5.10

#### Statement
```lean
theorem exists_genWronskian_ne_zero [CharZero K] {φ : Fin l → MvPolynomial σ K}
    (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by sorry
```

#### Proof sketch
1. Choose `k := 2 + Finset.univ.sup (fun ν => Finset.univ.sup fun j => degreeOf j (φ ν))` (so `1 < k` and `degreeOf j (φ ν) < k`: `Finset.le_sup`, `Nat.lt_succ_of_le`).
2. `linearIndependent_kronecker` ⇒ `LinearIndependent K (kronecker k ∘ φ)`; `wronskian_ne_zero_of_linearIndependent` ⇒ `wronskian (fun ν => kronecker k (φ ν)) ≠ 0`.
3. For each `μ : Fin l`, `exists_hasseDeriv_kronecker_eq_sum k μ` gives `(s μ, c μ)` (use `Classical.choose`/`choose` tactic over `Fin l`).
4. Rewrite `wronskianMatrix (kronecker k ∘ φ) = of fun μ ν => ∑ d ∈ s μ, c μ d * kronecker k (hasseDeriv d (φ ν))` and apply `det_sum_rows`; each inner determinant is `kronecker k (genWronskian f φ)` by `RingHom.map_det (kronecker k).toRingHom` (`RingHom.mapMatrix_apply`, `Matrix.map_apply`).
5. If every `genWronskian f φ = 0` (`f ∈ piFinset s`) the sum vanishes (`Finset.sum_eq_zero`, `map_zero`, `mul_zero`), contradiction; so some `f` has `genWronskian f φ ≠ 0`, and `(f μ).degree ≤ μ` from `Fintype.mem_piFinset` and the degree condition of step 3.

#### Mathlib lemmas needed
- `Finset.le_sup`, `Fintype.mem_piFinset`, `Finset.sum_eq_zero`
- `RingHom.map_det`, `RingHom.mapMatrix_apply`, `Matrix.map_apply`
- (project) `linearIndependent_kronecker`, `wronskian_ne_zero_of_linearIndependent`, `exists_hasseDeriv_kronecker_eq_sum`, `det_sum_rows`, `genWronskian`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 Lemma 1 (roth:lem1), clean.tex:224-345
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R5.10).

#### Generality decision
- `[Fintype σ]`, field `K` with `CharZero K` (the source: rational coefficients); any `l`.

**Progress**:
- 2026-10-12T18:57: DONE — Lemma 1 proved


### [CLEANUP-14] Run /cleanup on Roth/GenWronskian.lean
- **Status**: done
- **File**: Roth/GenWronskian.lean
- **Depends on**: T037
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/GenWronskian.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:01: agent dispatched (GenWronskian/Lattice)
- 2026-10-12T19:01: agent dispatched
- 2026-10-12T19:13: agent cleanup; build clean


### [T038] Reciprocal-sum estimate for Lemma 8
- **Status**: done
- **File**: Roth/Lattice.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R11.1, R11.2

#### Statement
```lean
theorem sqrt_one_sub_inv_lt {m : ℕ} (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2 := by sorry

theorem sum_inv_lt {r m : ℕ} (hr : 1 ≤ r) (hm : 2 ≤ m) {lam : ℝ} (hlam : 2 * √(m : ℝ) < lam) :
    ∑ j ∈ range (r + 1), (lam - 1 + 2 * (j : ℝ) / r)⁻¹ <
      lam⁻¹ * (√((m : ℝ) - 1))⁻¹ * √(m : ℝ) * (r + 1) := by sorry
```

#### Proof sketch
1. `sqrt_one_sub_inv_lt`: `Real.sqrt_lt' (by positivity : 0 < 1 − lam⁻¹^2)` (positivity needs `lam > 1`: `lam > 2√m ≥ 2√2 > 1`); then `1 − 1/m < (1 − lam⁻¹²)²`: from `lam² > 4m` (`Real.sq_sqrt`, `mul_self_lt_mul_self`) get `lam⁻¹² < 1/(4m)`, and `(1 − 1/(4m))² − (1 − 1/m) = 1/(2m) + 1/(16m²) > 0`; `nlinarith`/`field_simp`.
2. `sum_inv_lt`: let `S := ∑ j ∈ range (r+1), (lam − 1 + 2j/r)⁻¹`; reflect: `S = ∑ j, (lam − 1 + 2(r−j)/r)⁻¹` (`Finset.sum_range_reflect`); so `2S = ∑ j, [(lam−1+2j/r)⁻¹ + (lam+1−2j/r)⁻¹] = ∑ j, 2lam/(lam² − (1−2j/r)²)` (`inv_add_inv`, `field_simp`, `ring`) `≤ (r+1) · 2lam/(lam²−1)` (`Finset.sum_le_card_nsmul`, `div_le_div_of_nonneg_left`, `(1−2j/r)² ≤ 1` from `0 ≤ j ≤ r`, denominators positive by `lam² > 4m ≥ 8 > 1`).
3. Hence `S ≤ (r+1) lam⁻¹ (1−lam⁻¹²)⁻¹ < (r+1) lam⁻¹ (√(1−1/m))⁻¹` by `sqrt_one_sub_inv_lt` and `one_div_lt_one_div_of_lt`; finally `(√(1−1/m))⁻¹ = (√(m−1))⁻¹ √m` (`Real.sqrt_div`, `Real.sqrt_div_self'`, `div_eq_mul_inv`, `Real.sqrt_mul_self`), `Nat.cast_sub`.

#### Mathlib lemmas needed
- `Real.sqrt_lt'`, `Real.sq_sqrt`, `Real.sqrt_pos`
- `Finset.sum_range_reflect`, `inv_add_inv`, `Finset.sum_le_card_nsmul`, `div_le_div_of_nonneg_left`
- `one_div_lt_one_div_of_lt`, `Real.sqrt_div`, `Nat.cast_sub`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 8, clean.tex:1100-1133
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R11.1, R11.2).

#### Generality decision
- `1 ≤ r`, `2 ≤ m`, `2√m < λ` (as in the source).

**Progress**:
- 2026-10-12T18:59: DONE


### [T039] Counting a filtered box by the fibres of the last coordinate
- **Status**: done
- **File**: Roth/Lattice.lean
- **Depends on**: T010
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R11.3

#### Statement
```lean
theorem card_filter_box_last {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
    [DecidablePred p] :
    ((box r).filter p).card = ∑ i ∈ range (r (Fin.last m) + 1),
      ((box (r ∘ Fin.castSucc)).filter fun d =>
        p (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)).card := by sorry
```

#### Proof sketch
1. `Finset.card_eq_sum_card_fiberwise (f := fun d => d (Fin.last m)) (t := range (r (Fin.last m) + 1))` (maps-to from `mem_box`).
2. For each `i`, a bijection between `(box r).filter (fun d => p d ∧ d last = i)` and `(box (r ∘ castSucc)).filter (fun d' => p (d'.mapDomain castSucc + single last i))`: `Finset.card_bij'` with `d ↦ Finsupp.comapDomain Fin.castSucc d (castSucc_injective.injOn)` and inverse `d' ↦ d'.mapDomain castSucc + single last i`; membership via `mem_box`, `Fin.lastCases`/`Fin.exists_castSucc_eq`, `Finsupp.mapDomain_apply (Fin.castSucc_injective _)`, `Finsupp.mapDomain_notin_range` (`Fin.last ∉ range castSucc`: `Fin.castSucc_lt_last`), `Finsupp.comapDomain_apply`, `Finsupp.single_eq_same`, `Finsupp.ext`.

#### Mathlib lemmas needed
- `Finset.card_eq_sum_card_fiberwise`, `Finset.card_bij'`
- `Finsupp.comapDomain`, `Finsupp.comapDomain_apply`, `Finsupp.mapDomain_apply`, `Finsupp.mapDomain_notin_range`
- `Fin.lastCases`, `Fin.exists_castSucc_eq`, `Fin.castSucc_lt_last`, `Fin.castSucc_injective`
- (project) `mem_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 Lean note clean.tex:1134-1136; clean.tex:1070-1076
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R11.3).

#### Generality decision
- any `m`, any predicate `p` with decidable instances.

**Progress**:
- 2026-10-12T19:00: DONE


### [T040] Lemma 8: the lattice count estimate
- **Status**: done
- **File**: Roth/Lattice.lean
- **Depends on**: T038, T039, T011, T012
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R11.4

#### Statement
```lean
theorem card_filter_weight_le (m : ℕ) (r : Fin m → ℕ) (hr : ∀ j, 0 < r j) {lam : ℝ}
    (hlam : 0 < lam) :
    (((box r).filter fun d => weight r d ≤ ((m : ℝ) - lam) / 2).card : ℝ) ≤
      2 * √(m : ℝ) / lam * ∏ j, ((r j : ℝ) + 1) := by sorry
```

#### Proof sketch
1. Induction on `m` (`Nat.le_induction` from `m = 1`, with `m = 0` separately: the filter is empty since `0 ≤ (0 − λ)/2` fails; `Finset.card_eq_zero`, `Finset.filter_eq_empty_iff`; RHS `= 0` by `Real.sqrt_zero`).
2. `m = 1`: by cases `1 < λ`: then `j/r ≥ 0 > (1−λ)/2`, filter empty, `0 ≤ RHS`; else `card ≤ card (box r) = r_0 + 1` (`Finset.card_filter_le`, `card_box`, `Fin.prod_univ_one`) and `r_0 + 1 ≤ 2/λ · (r_0+1)` (`le_mul_of_one_le_left`, `one_le_div`).
3. Step `m+1 ≥ 2`: if `λ ≤ 2√(m+1)`: `card ≤ card (box r) = ∏ (r_j + 1)` and `1 ≤ 2√(m+1)/λ` (`one_le_div`). Else `card_filter_box_last`; for each `i ≤ r_last`, the fibre predicate is `weight (r∘castSucc) d + i/r_last ≤ (m+1−λ)/2` (`weight_add`, `weight_single`, `weight_mapDomain`, `Nat.cast_add`), i.e. `weight ≤ (m − λ')/2` with `λ' := λ − 1 + 2i/r_last > 0` (`2√(m+1) − 1 > 0`); apply the IH; sum: `Finset.sum_le_sum`, then `∑_{i ≤ r_last} 2√m/λ' · ∏_{j<m}(r_j+1) = 2√m ∏ · ∑ (λ−1+2i/r_last)⁻¹ < 2√m ∏ · λ⁻¹ (√m)⁻¹ √(m+1) (r_last+1)` by `sum_inv_lt` (with `r := r_last ≥ 1`, `m := m+1`, `√((m+1)−1) = √m`), `= 2√(m+1)/λ · ∏_{j ≤ m}(r_j+1)` (`Fin.prod_univ_castSucc`, `mul_inv_cancel₀`, `Real.sqrt_pos`).

#### Mathlib lemmas needed
- `Nat.le_induction`, `Finset.card_filter_le`, `Finset.filter_eq_empty_iff`, `one_le_div`, `le_mul_of_one_le_left`
- `Fin.prod_univ_castSucc`, `Fin.prod_univ_one`, `Finset.sum_le_sum`, `Finset.mul_sum`, `mul_inv_cancel₀`
- (project) `card_filter_box_last`, `sum_inv_lt`, `weight_add`, `weight_single`, `weight_mapDomain`, `card_box`, `mem_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 Lemma 8 (roth:lem8), clean.tex:1050-1138
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R11.4).

#### Generality decision
- all `m` (including `0`), positive `r`, `λ > 0` (as in the source).

**Progress**:
- 2026-10-12T19:01: DONE — Lemma 8 proved


### [CLEANUP-15] Run /cleanup on Roth/Lattice.lean
- **Status**: done
- **File**: Roth/Lattice.lean
- **Depends on**: T040
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Lattice.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:01: agent dispatched (GenWronskian/Lattice)
- 2026-10-12T19:01: agent dispatched
- 2026-10-12T19:13: agent cleanup; build clean


### [T041] The index: definition and the attained-minimum characterisation
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T020, T022
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R7.1–R7.5

#### Statement
```lean
noncomputable def index (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : ℝ :=
  sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))

theorem index_le_weight {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ}
    (h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d := by sorry

theorem exists_weight_eq_index {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    ∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by sorry

theorem le_index_iff {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {α : σ → ℝ} {r : σ → ℕ} {c : ℝ} :
    c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by sorry

theorem index_nonneg (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r := by
  sorry
```

#### Proof sketch
1. `index_le_weight`: `d ∈ (taylor α P).support` by `MvPolynomial.mem_support_iff` + `coeff_taylor`; `csInf_le (Set.Finite.bddBelow ((Finset.finite_toSet _).image _)) (Set.mem_image_of_mem _ hd)`.
2. `exists_weight_eq_index`: the image set is finite and nonempty (`taylor α P ≠ 0` by `taylor_eq_zero_iff`, `MvPolynomial.support_nonempty`/`Finsupp.support_nonempty_iff`), so `Set.Nonempty.csInf_mem hne hfin : sInf _ ∈ _`; unpack the image membership to get `d` with `coeff_taylor` ≠ 0 and `weight r d = index`.
3. `le_index_iff`: `⟨fun h d hd => h.trans (index_le_weight hd), fun h => le_csInf hne (by rintro _ ⟨d, hd, rfl⟩; exact h d (by simpa [coeff_taylor] using hd))⟩`.
4. `index_nonneg`: `Real.sInf_nonneg` with `weight_nonneg` (covers the empty set: `Real.sInf_empty`).

#### Mathlib lemmas needed
- `csInf_le`, `le_csInf`, `Set.Finite.bddBelow`, `Set.Finite.image`, `Finset.finite_toSet`
- `Set.Nonempty.csInf_mem`, `Real.sInf_nonneg`, `Real.sInf_empty`
- `MvPolynomial.mem_support_iff`, `MvPolynomial.support_nonempty`
- (project) `coeff_taylor`, `taylor_eq_zero_iff`, `weight_nonneg`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 definition of the index, clean.tex:528-548; clean.tex:558-567
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.1–R7.5).

#### Generality decision
- real polynomials, `[Fintype σ] [DecidableEq σ]`, weights `r : σ → ℕ` (positivity only where stated); the zero polynomial is excluded by explicit hypotheses instead of the source's `ind 0 = +∞` (plan.md decision 3).

**Progress**:
- 2026-10-12T19:02: DONE


### [T042] Index zero iff nonvanishing; index of a derivative
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T041, T005, T011
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R7.6, R7.7

#### Statement
```lean
theorem index_eq_zero_iff {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j)
    (α : σ → ℝ) : index P α r = 0 ↔ eval α P ≠ 0 := by sorry

theorem index_hasseDeriv_ge {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : hasseDeriv k P ≠ 0)
    (α : σ → ℝ) (r : σ → ℕ) : index P α r - weight r k ≤ index (hasseDeriv k P) α r := by sorry
```

#### Proof sketch
1. `index_eq_zero_iff` (⇐): `eval α P = eval α (hasseDeriv 0 P)` (`hasseDeriv_zero_apply`), so `index ≤ weight r 0 = 0` (`index_le_weight`, `weight_zero`) and `0 ≤ index` (`index_nonneg`). (⇒): `exists_weight_eq_index hP` gives `d` with `weight r d = 0`, so `d = 0` (`weight_eq_zero_iff hr`), hence `eval α (hasseDeriv 0 P) ≠ 0`, i.e. `eval α P ≠ 0`.
2. `index_hasseDeriv_ge`: `exists_weight_eq_index hk` gives `i` with `eval α (hasseDeriv i (hasseDeriv k P)) ≠ 0`; `hasseDeriv_hasseDeriv` turns it into `(hasseCoeff i (i+k) : ℝ) * eval α (hasseDeriv (i+k) P) ≠ 0` (`MvPolynomial.smul_eval`/`eval_smul`, `smul_eq_mul`), so `eval α (hasseDeriv (i+k) P) ≠ 0` (`mul_ne_zero_iff`); `index_le_weight` at `i + k`, `weight_add`, `sub_le_iff_le_add`, `linarith`.

#### Mathlib lemmas needed
- `mul_ne_zero_iff`, `MvPolynomial.eval_smul`/`smul_eval`, `sub_le_iff_le_add`
- (project) `index_le_weight`, `exists_weight_eq_index`, `index_nonneg`, `weight_zero`, `weight_eq_zero_iff`, `weight_add`, `hasseDeriv_zero_apply`, `hasseDeriv_hasseDeriv`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 lemmas on the index, clean.tex:558-587
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.6, R7.7).

#### Generality decision
- real polynomials, `[Fintype σ] [DecidableEq σ]`, weights `r : σ → ℕ` (positivity only where stated); the zero polynomial is excluded by explicit hypotheses instead of the source's `ind 0 = +∞` (plan.md decision 3).

**Progress**:
- 2026-10-12T19:02: DONE


### [T043] Index of sums, negatives and scalar multiples
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T041
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R7.8, R7.11

#### Statement
```lean
theorem le_index_sum {ι : Type*} {s : Finset ι} {f : ι → MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ}
    (hs : ∑ i ∈ s, f i ≠ 0) {c : ℝ} (hf : ∀ i ∈ s, f i ≠ 0 → c ≤ index (f i) α r) :
    c ≤ index (∑ i ∈ s, f i) α r := by sorry

theorem index_neg (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index (-P) α r = index P α r := by sorry

theorem index_C_mul {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index (C c * P) α r = index P α r := by sorry
```

#### Proof sketch
1. `le_index_sum`: `(le_index_iff hs).2`; for `d` with `eval α (hasseDeriv d (∑ f)) ≠ 0`, rewrite `map_sum`, `MvPolynomial.eval_sum`, get `i ∈ s` with `eval α (hasseDeriv d (f i)) ≠ 0` (`Finset.exists_ne_zero_of_sum_ne_zero`); then `f i ≠ 0` (else the derivative is `0`) and `(le_index_iff _).1 (hf i hi _) d` gives `c ≤ weight r d`.
2. `index_neg`: `index` depends only on `(taylor α P).support`; `map_neg`, `MvPolynomial.support_neg`. `index_C_mul`: `map_mul`, `taylor_C`, `MvPolynomial.support_C_mul`? (over a field: `C c * Q = c • Q`, `MvPolynomial.smul_eq_C_mul`, `MvPolynomial.support_smul_eq` with `c ≠ 0`); `congrArg`.

#### Mathlib lemmas needed
- `Finset.exists_ne_zero_of_sum_ne_zero`, `MvPolynomial.eval_sum`, `map_sum`
- `MvPolynomial.support_neg`, `MvPolynomial.support_smul_eq`, `MvPolynomial.smul_eq_C_mul`
- (project) `le_index_iff`, `taylor_C`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lemma 4-1 (sum), clean.tex:589-604; clean.tex:646-648; §5 clean.tex:823-826
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.8, R7.11).

#### Generality decision
- real polynomials, `[Fintype σ] [DecidableEq σ]`, weights `r : σ → ℕ` (positivity only where stated); the zero polynomial is excluded by explicit hypotheses instead of the source's `ind 0 = +∞` (plan.md decision 3).

**Progress**:
- 2026-10-12T19:02: DONE


### [CLEANUP-16] Run /cleanup on Roth/Index.lean
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T043
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Index.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T044] Bridge between the index and the weighted order of power series
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T041, T011, CLEANUP-16
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R7.15

#### Statement
```lean
theorem weight_eq_finsuppWeight_div {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) :
    weight r d = (Finsupp.weight (fun j => (∏ i, r i) / r j) d : ℝ) / ∏ i, r i := by sorry

theorem index_eq_weightedOrder_div {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (α : σ → ℝ) :
    index P α r =
      (((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j => (∏ i, r i) / r j).toNat : ℝ) /
        ∏ i, r i := by sorry
```

#### Proof sketch
1. `weight_eq_finsuppWeight_div`: `Finsupp.weight_apply` (`= d.sum fun j n => n • w j`), `Finsupp.sum_fintype`, `Nat.cast_sum`, `Finset.sum_div`, termwise `((∏ i, r i) / r j : ℕ)` divides exactly (`Finset.dvd_prod_of_mem`, `Nat.cast_div`, `Nat.div_mul_cancel`), so `(d j * (D / r j)) / D = d j / r j` (`field_simp`, `(hr j).ne'`, `Finset.prod_pos`).
2. `index_eq_weightedOrder_div`: let `F := (taylor α P : MvPowerSeries σ ℝ)`, `w j := D / r j`. `F ≠ 0` (`MvPolynomial.coe_eq_zero`/`coe_inj`, `taylor_eq_zero_iff`), so the order is finite (`MvPowerSeries.weightedOrder_eq_top_iff`, `ENat.coe_toNat`). Show `index = (order.toNat : ℝ) / D` by `le_antisymm`: (≤) `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder` gives `d` with `coeff d F ≠ 0` (`MvPolynomial.coeff_coe`) and `Finsupp.weight w d = order`; `index_le_weight` + `weight_eq_finsuppWeight_div`. (≥) `exists_weight_eq_index hP` gives `d` with nonzero coefficient; `MvPowerSeries.weightedOrder_le` gives `order ≤ weight w d`, cast with `Nat.cast_le`, `div_le_div_of_nonneg_right`.

#### Mathlib lemmas needed
- `Finsupp.weight_apply`, `Finsupp.sum_fintype`, `Nat.cast_div`, `Finset.dvd_prod_of_mem`, `Finset.prod_pos`
- `MvPowerSeries.weightedOrder_le`, `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_eq_top_iff`, `ENat.coe_toNat`
- `MvPolynomial.coeff_coe`, `MvPolynomial.coe_inj`
- (project) `index_le_weight`, `exists_weight_eq_index`, `taylor_eq_zero_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lean note clean.tex:549-556
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.15).

#### Generality decision
- real polynomials, `[Fintype σ] [DecidableEq σ]`, weights `r : σ → ℕ` (positivity only where stated); the zero polynomial is excluded by explicit hypotheses instead of the source's `ind 0 = +∞` (plan.md decision 3). Positive integer weights (needed for `D / r j`).

**Progress**:
- 2026-10-12T19:03: DONE


### [T045] Lemma 4-1 (product): the index is additive on products
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T044, CLEANUP-16
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R7.9, R7.10

#### Statement
```lean
theorem index_mul {P Q : MvPolynomial σ ℝ} (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) : index (P * Q) α r = index P α r + index Q α r := by sorry

theorem index_prod {ι : Type*} (s : Finset ι) {f : ι → MvPolynomial σ ℝ} (hf : ∀ i ∈ s, f i ≠ 0)
    (α : σ → ℝ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r := by sorry
```

#### Proof sketch
1. `index_mul`: rewrite all three indices with `index_eq_weightedOrder_div` (`P*Q ≠ 0`: `mul_ne_zero`); `taylor α (P*Q) = taylor α P * taylor α Q` (`map_mul`), `MvPolynomial.coe_mul`, `MvPowerSeries.weightedOrder_mul` (`ℝ` has `NoZeroDivisors`); both orders finite ⇒ `ENat.toNat_add` (`WithTop`/`ENat` finiteness from `weightedOrder_eq_top_iff`), `Nat.cast_add`, `add_div`.
2. `index_prod`: `Finset.induction_on s`; empty: `Finset.prod_empty`, `index 1 = 0` (`index_eq_zero_iff` with `eval α 1 = 1 ≠ 0`, `one_ne_zero`); step: `Finset.prod_insert`, `index_mul` (`∏ ≠ 0` by `Finset.prod_ne_zero_iff`), `Finset.sum_insert`.

#### Mathlib lemmas needed
- `MvPowerSeries.weightedOrder_mul`, `MvPolynomial.coe_mul`, `ENat.toNat_add`
- `Finset.prod_ne_zero_iff`, `Finset.prod_insert`, `Finset.sum_insert`, `mul_ne_zero`
- (project) `index_eq_weightedOrder_div`, `index_eq_zero_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lemma 4-1 (product), clean.tex:589-612; Lean note clean.tex:628-632
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.9, R7.10).

#### Generality decision
- real polynomials, `[Fintype σ] [DecidableEq σ]`, weights `r : σ → ℕ` (positivity only where stated); the zero polynomial is excluded by explicit hypotheses instead of the source's `ind 0 = +∞` (plan.md decision 3).

**Progress**:
- 2026-10-12T19:03: DONE


### [T046] Scaling of weights, renaming of variables, and the bound by the number of variables
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T041, T012, T021, T010, CLEANUP-16
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R7.12, R7.13, R7.14

#### Statement
```lean
theorem index_mul_left_weights {l : ℕ} (hl : 0 < l) (P : MvPolynomial σ ℝ) (α : σ → ℝ)
    (r : σ → ℕ) : index P α (fun j => l * r j) = index P α r / l := by sorry

theorem index_rename {τ : Type*} [Fintype τ] [DecidableEq τ] {f : σ → τ}
    (hf : Function.Injective f) (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) :
    index (rename f P) α r = index P (α ∘ f) (r ∘ f) := by sorry

theorem index_le_card {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ} (hr : ∀ j, 0 < r j)
    (hd : ∀ j, degreeOf j P ≤ r j) (α : σ → ℝ) : index P α r ≤ Fintype.card σ := by sorry
```

#### Proof sketch
1. `index_mul_left_weights`: `weight_mul_left` pointwise gives `weight (l•r) '' S = (l⁻¹ : ℝ) • (weight r '' S)` (`Set.image_image`, `Set.image_congr`, `Set.smul_set_image`-free: `Set.ext`/`Set.image_smul`), then `Real.sInf_smul_of_nonneg (inv_nonneg.2 (Nat.cast_nonneg l))`, `smul_eq_mul`, `div_eq_inv_mul`.
2. `index_rename`: `taylor_rename` (`taylor α (rename f P) = rename f (taylor (α ∘ f) P)`), `MvPolynomial.support_rename_of_injective hf` (`= support.map (mapDomain f)`), `Finset.coe_map`, `Set.image_image`, `weight_mapDomain hf` pointwise; the two `sInf`s are of the same set.
3. `index_le_card`: `exists_weight_eq_index hP` gives `d` with `coeff d (taylor α P) ≠ 0` (via `coeff_taylor`), so `d j ≤ degreeOf j (taylor α P) ≤ degreeOf j P ≤ r j` (`degreeOf_le_iff`, `degreeOf_taylor_le`), then `weight_le_card hr`.

#### Mathlib lemmas needed
- `Real.sInf_smul_of_nonneg`, `Set.image_image`, `Set.image_congr`
- `MvPolynomial.support_rename_of_injective`, `Finset.coe_map`
- (project) `weight_mul_left`, `taylor_rename`, `weight_mapDomain`, `exists_weight_eq_index`, `degreeOf_taylor_le`, `weight_le_card`, `mem_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 clean.tex:646-650; Lemma 4-2 and note clean.tex:614-641; §5 clean.tex:665-668
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.12, R7.13, R7.14).

#### Generality decision
- real polynomials, `[Fintype σ] [DecidableEq σ]`, weights `r : σ → ℕ` (positivity only where stated); the zero polynomial is excluded by explicit hypotheses instead of the source's `ind 0 = +∞` (plan.md decision 3). `index_rename` for injective `f` (sharp).

**Progress**:
- 2026-10-12T19:04: DONE


### [CLEANUP-17] Run /cleanup on Roth/Index.lean
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T046
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Index.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T047] The one-variable index is the root multiplicity over the weight
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T041, T009, CLEANUP-17
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R7.16

#### Statement
```lean
theorem index_unique [Unique σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    index P α r =
      (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default := by sorry
```

#### Proof sketch
1. Let `e := uniqueAlgEquiv ℝ σ`, `P' := e P ≠ 0`, `a := α default`. Show `e (taylor α P) = Polynomial.taylor a P'` (`MvPolynomial.algHom_ext`-style on `X`: both are algebra maps `MvPolynomial σ ℝ → ℝ[X]` sending `X default ↦ X + C a`; `Polynomial.taylor_apply`, `taylor_X`, `uniqueAlgEquiv` on `X`).
2. Every multi-index is `single default n` (`Finsupp.unique_single`), and `coeff (single default n) (taylor α P) = (Polynomial.taylor a P').coeff n` (via `coeff_uniqueAlgEquiv_symm`-type lemma: `MvPolynomial.coeff` through `e`; `Finsupp.unique_single_eq_iff`).
3. So `weight r '' support = (fun n => n / r default) '' (Polynomial.taylor a P').support` (`weight_single`); its `sInf` is `(min support)/r` with `min support = natTrailingDegree (Polynomial.taylor a P')` (`Polynomial.natTrailingDegree_le_of_ne_zero`, `Polynomial.coeff_eq_zero_of_lt_natTrailingDegree`, `Polynomial.trailingCoeff_nonzero_iff_nonzero`, `csInf_le`/`le_csInf`, `div_le_div_of_nonneg_right`), and `Polynomial.rootMultiplicity_eq_natTrailingDegree : rootMultiplicity a P' = (Polynomial.taylor a P').natTrailingDegree`.

#### Mathlib lemmas needed
- `Polynomial.rootMultiplicity_eq_natTrailingDegree`, `Polynomial.taylor_apply`, `Polynomial.taylor_X`
- `Polynomial.natTrailingDegree_le_of_ne_zero`, `Polynomial.coeff_eq_zero_of_lt_natTrailingDegree`, `Polynomial.trailingCoeff_nonzero_iff_nonzero`
- `Finsupp.unique_single`, `Finsupp.unique_single_eq_iff`, `MvPolynomial.uniqueAlgEquiv`
- (project) `weight_single`, `index` characterisation (`index_le_weight`, `exists_weight_eq_index`)

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 5, clean.tex:677-679; Lean note clean.tex:692-693
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R7.16).

#### Generality decision
- `[Unique σ]`; real polynomials.

**Progress**:
- 2026-10-12T19:04: DONE


### [CLEANUP-18] Run /cleanup on Roth/Index.lean
- **Status**: done
- **File**: Roth/Index.lean
- **Depends on**: T047
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Index.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T048] Coefficient polynomials with respect to the distinguished variable
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R6.1, R6.2

#### Statement
```lean
theorem eq_mapDomain_some_add_single (d : Option τ →₀ ℕ) :
    d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none) := by sorry

noncomputable def coeffNone (P : MvPolynomial (Option τ) R) (ν : ℕ) : MvPolynomial τ R :=
  (optionEquivLeft R τ P).coeff ν

theorem coeff_coeffNone (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν) := by sorry

theorem eq_sum_X_none_pow_mul_coeffNone (P : MvPolynomial (Option τ) R) {n : ℕ}
    (hn : degreeOf none P ≤ n) :
    P = ∑ ν ∈ Finset.range (n + 1), X none ^ ν * rename some (coeffNone P ν) := by sorry

theorem degreeOf_coeffNone_le (P : MvPolynomial (Option τ) R) (ν : ℕ) (j : τ) :
    degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P := by sorry
```

#### Proof sketch
1. `eq_mapDomain_some_add_single`: `Finsupp.ext`, `rintro (_|j)`; `none`: `Finsupp.mapDomain_notin_range` (`none ∉ range some`), `Finsupp.single_eq_same`; `some j`: `Finsupp.mapDomain_apply (Option.some_injective _)`, `Finsupp.some_apply`, `Finsupp.single_eq_of_ne`.
2. `coeff_coeffNone`: reduce to monomials (`MvPolynomial.induction_on'`, additivity of both sides: `map_add`, `Polynomial.coeff_add`, `coeff_add`); for `monomial k a`: `optionEquivLeft` is `aeval (fun o => o.elim X (fun s => C (X s)))` (unfold `MvPolynomial.optionEquivLeft`; `optionEquivLeft_X_some`, `optionEquivLeft_X_none`, `optionEquivLeft_C`), `aeval_monomial`, `Finsupp.prod` split by `eq_mapDomain_some_add_single k` into the `none`-factor `X ^ (k none)` and the `some`-factors; `Polynomial.coeff_C_mul_X_pow`, `MvPolynomial.coeff_monomial`, and injectivity of `d ↦ d.mapDomain some + single none ν` (`Finsupp.mapDomain_injective`, `Finsupp.some_mapDomain`?/apply at `none`).
3. `eq_sum_X_none_pow_mul_coeffNone`: `MvPolynomial.ext d`; `coeff_sum`, `coeff_X_pow_mul'`?/`MvPolynomial.coeff_mul_X_pow'`, `coeff_rename_mapDomain`, `coeff_coeffNone`, `eq_mapDomain_some_add_single d`, `Finset.sum_eq_single (d none)` (`d none ≤ degreeOf none P` by `degreeOf_le_iff` when `coeff d P ≠ 0`).
4. `degreeOf_coeffNone_le`: `degreeOf_le_iff.2`; `coeff_coeffNone` nonzero ⇒ the big coefficient is nonzero ⇒ `(d.mapDomain some + single none ν) (some j) = d j ≤ degreeOf (some j) P`.

#### Mathlib lemmas needed
- `Finsupp.mapDomain_apply`, `Finsupp.mapDomain_notin_range`, `Finsupp.some_apply`, `Finsupp.single_eq_of_ne`
- `MvPolynomial.optionEquivLeft_X_some`, `optionEquivLeft_X_none`, `optionEquivLeft_C`, `MvPolynomial.aeval_monomial`
- `Polynomial.coeff_C_mul_X_pow`, `MvPolynomial.coeff_rename_mapDomain`, `MvPolynomial.coeff_mul_X_pow'`, `Finset.sum_eq_single`, `MvPolynomial.degreeOf_le_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:372-376 (collecting powers of x_p)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.1, R6.2).

#### Generality decision
- `[Fintype τ] [DecidableEq τ]`, `R` any `CommSemiring`.

**Progress**:
- 2026-10-12T19:07: DONE


### [T049] Separated products: coefficients and Hasse derivatives
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T048, T004, T005, T008, T009
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R6.3, R6.4

#### Statement
```lean
theorem coeff_rename_mul_aeval (U : MvPolynomial τ R) (V : Polynomial R) (a : τ →₀ ℕ) (b : ℕ) :
    (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V).coeff
        (a.mapDomain some + Finsupp.single none b) = U.coeff a * V.coeff b := by sorry

theorem hasseDeriv_rename_mul_aeval (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R) (V : Polynomial R) :
    hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) =
      rename some (hasseDeriv d U) * Polynomial.aeval (X none : MvPolynomial (Option τ) R) (Polynomial.hasseDeriv ν V) := by
  sorry
```

#### Proof sketch
1. `coeff_rename_mul_aeval`: write `rename some U = ∑_{a' ∈ supp U} monomial (a'.mapDomain some) (coeff a' U)` (`as_sum`, `map_sum`, `rename_monomial`) and `aeval (X none) V = ∑_{b' ∈ supp V} monomial (single none b') (V.coeff b')` (`Polynomial.as_sum_support`/`Polynomial.sum_def`, `aeval_monomial`, `X_pow_eq_monomial`); `Finset.sum_mul_sum`, `monomial_mul`, `coeff_sum`, `coeff_monomial`, `Finset.sum_eq_single (a, b)` — the equation `a'.mapDomain some + single none b' = a.mapDomain some + single none b` forces `a' = a` (evaluate at `some j`) and `b' = b` (evaluate at `none`); use `Finsupp.ext_iff` and `eq_mapDomain_some_add_single`.
2. `hasseDeriv_rename_mul_aeval`: `hasseDeriv_hasseDeriv_of_disjoint` (supports: `Finsupp.support_mapDomain` ⊆ image of `some`, `Finsupp.support_single_subset`; `Finset.disjoint_left`), then `hasseDeriv (single none ν) (rename some U * aeval (X none) V) = rename some U * hasseDeriv (single none ν) (aeval (X none) V)` by `hasseDeriv_mul_of_degreeOf_eq_zero` (`degreeOf none (rename some U) = 0`: `degreeOf_rename_of_injective`? — `none ∉ vars`, use `MvPolynomial.degreeOf_eq_zero_iff`-free route: `degreeOf_le_iff` with `coeff_rename_mapDomain`/`coeff_rename_eq_zero`), `hasseDeriv_single_aeval_X`; then `hasseDeriv (d.mapDomain some) (rename some U * Q) = hasseDeriv (d.mapDomain some) (Q * rename some U)` with `Q := aeval (X none) (hasseDeriv ν V)` having `degreeOf (some j) Q = 0` (`mul_comm`, `hasseDeriv_mul_of_degreeOf_eq_zero`), and `hasseDeriv_rename (Option.some_injective _)`.

#### Mathlib lemmas needed
- `MvPolynomial.as_sum`, `rename_monomial`, `Polynomial.as_sum_support`, `MvPolynomial.monomial_mul`, `Finset.sum_mul_sum`, `Finset.sum_eq_single`
- `Finsupp.support_mapDomain`, `Finsupp.support_single_subset`, `Finset.disjoint_left`, `MvPolynomial.coeff_rename_eq_zero`
- (project) `eq_mapDomain_some_add_single`, `hasseDeriv_hasseDeriv_of_disjoint`, `hasseDeriv_mul_of_degreeOf_eq_zero`, `hasseDeriv_rename`, `hasseDeriv_single_aeval_X`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:407-425
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.3, R6.4).

#### Generality decision
- `R` any `CommSemiring`.

**Progress**:
- 2026-10-12T19:07: DONE


### [T050] Univariate polynomials as one-variable multivariate polynomials
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R9.6 (transport), R7.16

#### Statement
```lean
theorem aeval_X_eq_rename {σ : Type*} (i : σ) (f : Polynomial R) :
    Polynomial.aeval (X i : MvPolynomial σ R) f =
      rename (fun _ : Unit => i) ((uniqueAlgEquiv R Unit).symm f) := by sorry

theorem coeff_uniqueAlgEquiv_symm {σ : Type*} [Unique σ] (f : Polynomial R) (n : ℕ) :
    ((uniqueAlgEquiv R σ).symm f).coeff (Finsupp.single default n) = f.coeff n := by sorry

theorem degreeOf_uniqueAlgEquiv_symm {σ : Type*} [Unique σ] (f : Polynomial R) :
    degreeOf default ((uniqueAlgEquiv R σ).symm f) = f.natDegree := by sorry
```

#### Proof sketch
1. `aeval_X_eq_rename`: both sides are `R`-algebra maps `R[X] → MvPolynomial σ R` applied to `f`; `Polynomial.algHom_ext` comparing on `X`: left `aeval_X`; right `rename (fun _ => i) ((uniqueAlgEquiv R Unit).symm X) = rename _ (X default) = X i` (`MvPolynomial.uniqueAlgEquiv_symm_X`? — unfold `uniqueAlgEquiv`; `rename_X`).
2. `coeff_uniqueAlgEquiv_symm`: `Polynomial.induction_on'` (additivity) + monomial: `(uniqueAlgEquiv R σ).symm (monomial n a) = monomial (single default n) a` (`Polynomial.aeval_monomial`, `X_pow_eq_monomial`, `C_mul_monomial`), `coeff_monomial`, `Finsupp.unique_single_eq_iff`.
3. `degreeOf_uniqueAlgEquiv_symm`: `le_antisymm`: `degreeOf_le_iff` with `coeff_uniqueAlgEquiv_symm` and `Polynomial.le_natDegree_of_ne_zero`; conversely the coefficient at `single default (natDegree f)` is `leadingCoeff f ≠ 0` (if `f ≠ 0`; `f = 0` trivial), `MvPolynomial.degreeOf_le_iff`/`Finset.le_sup` via `degreeOf_eq_sup`.

#### Mathlib lemmas needed
- `Polynomial.algHom_ext`, `Polynomial.aeval_X`, `MvPolynomial.rename_X`
- `Polynomial.induction_on'`, `Polynomial.aeval_monomial`, `MvPolynomial.coeff_monomial`, `Finsupp.unique_single_eq_iff`
- `Polynomial.le_natDegree_of_ne_zero`, `Polynomial.leadingCoeff_ne_zero`, `MvPolynomial.degreeOf_eq_sup`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lemma 4-2 clean.tex:621-624; §5 clean.tex:757-764 (V ∈ ℛ_1)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R9.6 (transport), R7.16).

#### Generality decision
- `R` any `CommSemiring`; `[Unique σ]`.

**Progress**:
- 2026-10-12T19:07: DONE


### [CLEANUP-19] Run /cleanup on Roth/Separation.lean
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T050
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Separation.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T051] Degrees of separated products
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: CLEANUP-19
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R6.5

#### Statement
```lean
theorem degreeOf_rename_mul_aeval (U : MvPolynomial τ R) {V : Polynomial R} (hV : V ≠ 0) (j : τ) :
    degreeOf (some j) (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) = degreeOf j U := by sorry

theorem degreeOf_none_rename_mul_aeval {U : MvPolynomial τ R} (hU : U ≠ 0) (V : Polynomial R) :
    degreeOf none (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) R) V) = V.natDegree := by sorry
```

#### Proof sketch
1. `degreeOf_rename_mul_aeval`: by cases `U = 0` (both sides `0`: `map_zero`, `zero_mul`, `degreeOf_zero`); else `MvPolynomial.degreeOf_mul_eq (rename_ne_zero) (aeval_ne_zero)` (both factors nonzero: `MvPolynomial.rename_injective`, and `aeval (X none) V ≠ 0` by `aeval_X_eq_rename` + `rename_injective` + `AlgEquiv` injectivity), `degreeOf_rename_of_injective (Option.some_injective _)`, and `degreeOf (some j) (aeval (X none) V) = 0` (`aeval_X_eq_rename`, `degreeOf_le_iff` + `coeff_rename_eq_zero`/`vars_rename` ⊆ `{none}`), `add_zero`.
2. `degreeOf_none_rename_mul_aeval`: symmetric: `degreeOf none (rename some U) = 0` (`vars_rename`, `degreeOf` of a variable not in `vars`: `MvPolynomial.degreeOf_eq_zero_of_not_mem_vars`?/`degreeOf_le_iff`), and `degreeOf none (aeval (X none) V) = V.natDegree` (`aeval_X_eq_rename`, `degreeOf_rename_of_injective`, `degreeOf_uniqueAlgEquiv_symm`); `zero_add`.

#### Mathlib lemmas needed
- `MvPolynomial.degreeOf_mul_eq` (NoZeroDivisors), `MvPolynomial.degreeOf_rename_of_injective`, `MvPolynomial.rename_injective`
- `MvPolynomial.vars_rename`, `MvPolynomial.degreeOf_le_iff`, `MvPolynomial.coeff_rename_eq_zero`
- (project) `aeval_X_eq_rename`, `degreeOf_uniqueAlgEquiv_symm`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 end of proof of Lemma 2, clean.tex:435-437
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.5).

#### Generality decision
- `R` a domain (`[CommRing R] [IsDomain R]`), as needed for `degreeOf_mul_eq`.

**Progress**:
- 2026-10-12T19:08: DONE


### [T052] Separated representation with linearly independent factors
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T048, CLEANUP-19
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R6.6

#### Statement
```lean
theorem exists_separated_representation {P : MvPolynomial (Option τ) K} (hP : P ≠ 0) {n : ℕ}
    (hn : degreeOf none P ≤ n) :
    ∃ l, 1 ≤ l ∧ l ≤ n + 1 ∧ ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
      LinearIndependent K φ ∧ LinearIndependent K ψ ∧ (∀ ν, (φ ν).natDegree ≤ n) ∧
      (∀ ν j, degreeOf j (ψ ν) ≤ degreeOf (some j) P) ∧
      P = ∑ ν, Polynomial.aeval (X none : MvPolynomial (Option τ) K) (φ ν) * rename some (ψ ν) := by sorry
```

#### Proof sketch
1. Set `ψ' ν := coeffNone P ν` for `ν ∈ range (n+1)` and `V := Submodule.span K (Set.range (fun ν : Fin (n+1) => ψ' ν))`; `FiniteDimensional K V` (`FiniteDimensional.span_of_finite`, `Set.finite_range`); `l := Module.finrank K V`; `b := Module.finBasis K V : Basis (Fin l) K V`.
2. `1 ≤ l`: `V ≠ ⊥` because `P ≠ 0` gives some `ψ' ν ≠ 0` (`eq_sum_X_none_pow_mul_coeffNone`, `Finset.sum_eq_zero`), `Submodule.finrank_pos_iff`/`Module.finrank_pos_iff_exists_ne_zero`. `l ≤ n+1`: `finrank_span_le_card` + `Fintype.card_fin`.
3. `ψ ρ := (b ρ : MvPolynomial τ K)`; independence: `b.linearIndependent.map' (Submodule.subtype V) (ker_subtype)`. Degree bounds: every element of `V` satisfies `degreeOf j ≤ degreeOf (some j) P` — the set of such polynomials is a submodule (`degreeOf_add_le`, `degreeOf_C_mul_le`/`degreeOf_smul_le`, `degreeOf_zero`), containing the generators by `degreeOf_coeffNone_le`, so `Submodule.span_le`.
4. Coordinates `a ν ρ := b.repr ⟨ψ' ν, Submodule.subset_span ⟨ν, rfl⟩⟩ ρ`; `φ ρ := ∑ ν, Polynomial.C (a ν ρ) * X ^ (ν : ℕ)`; `natDegree (φ ρ) ≤ n` (`Polynomial.natDegree_sum_le_of_forall_le`, `natDegree_C_mul_X_pow_le`). Identity: `P = ∑_ν X none ^ ν * rename some (ψ' ν)` and `ψ' ν = ∑_ρ a ν ρ • ψ ρ` (`b.sum_repr`, `Submodule.coe_sum`), so `P = ∑_ρ (∑_ν X none^ν * C (a ν ρ)) * rename some (ψ ρ)` by `Finset.sum_comm`, `Finset.mul_sum`, `map_sum`, `rename` of `smul` (`map_smul`, `MvPolynomial.smul_eq_C_mul`), and `aeval (X none) (φ ρ) = ∑_ν C (a ν ρ) * X none ^ ν` (`map_sum`, `aeval_C`, `aeval_X_pow`); `ring`-level rearrangement.
5. Independence of `φ`: `Fintype.linearIndependent_iff.2`: from `∑ ρ, g ρ • φ ρ = 0` compare `Polynomial.coeff` at `ν` (`Polynomial.finset_sum_coeff`, `coeff_C_mul_X_pow`): `∑ ρ, g ρ * a ν ρ = 0` for all `ν ≤ n`; define `f : V →ₗ[K] K := ∑ ρ, g ρ • b.coord ρ`; `f` vanishes on each generator `ψ' ν` (`Module.Basis.coord_apply`, `Finset.sum_apply`) hence on `V` (`Submodule.span_induction`/`LinearMap.eqOn_span'`), so `f (b ρ) = g ρ = 0` (`Module.Basis.coord_apply`, `Module.Basis.repr_self`, `Finsupp.single_apply`).

#### Mathlib lemmas needed
- `FiniteDimensional.span_of_finite`, `Module.finBasis`, `finrank_span_le_card`, `Submodule.finrank_pos_iff`
- `Module.Basis.sum_repr`, `Module.Basis.coord_apply`, `Module.Basis.repr_self`, `Module.Basis.linearIndependent`, `LinearIndependent.map'`
- `Submodule.span_le`, `Submodule.span_induction`, `Submodule.subset_span`, `MvPolynomial.degreeOf_add_le`, `MvPolynomial.degreeOf_C_mul_le`
- `Fintype.linearIndependent_iff`, `Polynomial.finset_sum_coeff`, `Polynomial.coeff_C_mul_X_pow`, `Polynomial.natDegree_sum_le_of_forall_le`
- (project) `eq_sum_X_none_pow_mul_coeffNone`, `degreeOf_coeffNone_le`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:349-394 and Lean note clean.tex:428-433
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.6).

#### Generality decision
- any field `K` (the source: ℚ); `n ≥ degreeOf none P`.

**Progress**:
- 2026-10-12T19:14: DONE


### [T053] The determinant of a separated sum factors as (generalized Wronskian)·(Wronskian)
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T049, T031, T013, CLEANUP-19
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R6.7

#### Statement
```lean
theorem det_hasseDeriv_separated {l : ℕ} (D : Fin l → (τ →₀ ℕ)) (φ : Fin l → Polynomial K)
    (ψ : Fin l → MvPolynomial τ K) :
    (Matrix.of fun μ ν : Fin l => hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ))
        (∑ ρ, Polynomial.aeval (X none : MvPolynomial (Option τ) K) (φ ρ) * rename some (ψ ρ))).det =
      rename some (genWronskian D ψ) * Polynomial.aeval (X none : MvPolynomial (Option τ) K) (wronskian φ) := by sorry
```

#### Proof sketch
1. Entry `(μ, ν)`: `map_sum` then `hasseDeriv_rename_mul_aeval` termwise: `∑ ρ, rename some (hasseDeriv (D μ) (ψ ρ)) * aeval (X none) (Polynomial.hasseDeriv ν (φ ρ))`; this is `(A * Bᵀ) μ ν` with `A := (rename some).mapMatrix (of fun μ ρ => hasseDeriv (D μ) (ψ ρ))` and `B := (aeval (X none)).mapMatrix (wronskianMatrix φ)` (`Matrix.mul_apply`, `Matrix.transpose_apply`, `RingHom.mapMatrix_apply`, `Matrix.map_apply`, `Matrix.of_apply`).
2. `Matrix.det_mul`, `Matrix.det_transpose`, then `RingHom.map_det` twice to get `rename some (genWronskian D ψ) * aeval (X none) (wronskian φ)` (unfold `genWronskian`, `wronskian`).

#### Mathlib lemmas needed
- `Matrix.det_mul`, `Matrix.det_transpose`, `RingHom.map_det`, `RingHom.mapMatrix_apply`
- `Matrix.mul_apply`, `Matrix.transpose_apply`, `Matrix.map_apply`, `Matrix.of_apply`, `map_sum`
- (project) `hasseDeriv_rename_mul_aeval`, `genWronskian`, `wronskian`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:407-420
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.7).

#### Generality decision
- any field `K`; any `D`, `φ`, `ψ` (no independence needed for the identity).

**Progress**:
- 2026-10-12T19:09: DONE


### [CLEANUP-20] Run /cleanup on Roth/Separation.lean
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T053
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Separation.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T054] Bézout for finite families of integers
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: CLEANUP-20
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R6.8, R6.10

#### Statement
```lean
theorem exists_sum_mul_eq_gcd {ι : Type*} (s : Finset ι) (u : ι → ℤ) :
    ∃ z : ι → ℤ, ∑ i ∈ s, z i * u i = s.gcd u := by sorry

theorem exists_int_eq_of_gcd_eq_one {ι : Type*} {s : Finset ι} {u : ι → ℤ} (hu : s.gcd u = 1)
    {v : ℚ} (hv : ∀ a ∈ s, ∃ z : ℤ, (u a : ℚ) * v = z) : ∃ z : ℤ, v = z := by sorry
```

#### Proof sketch
1. `exists_sum_mul_eq_gcd`: `Finset.induction_on s`; empty: `z := 0`, `Finset.gcd_empty`, `Finset.sum_empty`. Insert `i`: `Finset.gcd_insert`: `gcd (insert i s) u = GCDMonoid.gcd (u i) (s.gcd u)`; in `ℤ`, `GCDMonoid.gcd a b = (Int.gcd a b : ℤ)` (`Int.coe_gcd`), and `Int.gcd_eq_gcd_ab a b : (Int.gcd a b : ℤ) = a * gcdA a b + b * gcdB a b`; with the IH `s.gcd u = ∑ z i * u i`, set `z' := update (fun j => gcdB * z j) i (gcdA)` and expand (`Finset.sum_insert`, `Finset.mul_sum`, `Finset.sum_congr` with `Function.update_noteq`).
2. `exists_int_eq_of_gcd_eq_one`: from step 1 get `z` with `∑ z a * u a = 1` (`hu ▸`); choose `w a` with `(u a : ℚ) * v = w a` (`hv`, `choose`); then `v = (∑ z a * u a : ℤ) * v = ∑ z a * (u a * v) = ∑ z a * w a` (`Int.cast_sum`, `Int.cast_mul`, `Finset.sum_mul`, `mul_assoc`), an integer.

#### Mathlib lemmas needed
- `Finset.gcd_insert`, `Finset.gcd_empty`, `Int.coe_gcd`, `Int.gcd_eq_gcd_ab`
- `Finset.sum_insert`, `Finset.mul_sum`, `Function.update_noteq`, `Function.update_same`
- `Int.cast_sum`, `Int.cast_mul`, `Finset.sum_mul`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2 and Lean note, clean.tex:421-433
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.8, R6.10).

#### Generality decision
- any finite index type; integers (the source's Bézout relation).

**Progress**:
- 2026-10-12T19:10: DONE


### [T055] Clearing denominators and primitivity for rational polynomials
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: CLEANUP-20
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R6.9

#### Statement
```lean
theorem exists_nat_smul_eq_map {σ : Type*} (G : MvPolynomial σ ℚ) :
    ∃ (N : ℕ) (U : MvPolynomial σ ℤ), 0 < N ∧ map (Int.castRingHom ℚ) U = (N : ℚ) • G := by sorry

theorem exists_primitive_smul_eq {σ : Type*} {G : MvPolynomial σ ℚ} (hG : G ≠ 0) :
    ∃ (g : ℚ) (U : MvPolynomial σ ℤ), g ≠ 0 ∧ map (Int.castRingHom ℚ) U = g • G ∧
      U.support.gcd (fun d => U.coeff d) = 1 := by sorry
```

#### Proof sketch
1. `exists_nat_smul_eq_map`: `N := ∏ d ∈ G.support, (coeff d G).den` (`0 < N`: `Finset.prod_pos`, `Rat.den_pos`); for `d ∈ support`, `(coeff d G).den ∣ N` (`Finset.dvd_prod_of_mem`), so `(N : ℚ) * coeff d G` is an integer: `Rat.mul_den_eq_num`-style: write `N = (coeff d G).den * k`, then `N * q = k * (q.den * q) = k * q.num` (`Rat.mul_den_eq_num`, `Nat.cast_mul`); define `U := ∑ d ∈ G.support, monomial d (((N : ℚ) * coeff d G).num)` and check coefficients with `MvPolynomial.coeff_map`, `coeff_sum`, `coeff_monomial`, `Rat.num_div_den`/`Rat.coe_int_num_of_den_eq_one`, `smul_eq_mul`, `MvPolynomial.coeff_smul`.
2. `exists_primitive_smul_eq`: from step 1, `U₀ ≠ 0` (`G ≠ 0`, `N ≠ 0`, `map` injective: `MvPolynomial.map_injective`, `Int.cast_injective`); `g₀ := U₀.support.gcd (coeff · U₀) ≠ 0` (`Finset.gcd_eq_zero_iff`, nonzero coefficient on the support); `Finset.extract_gcd (fun d => coeff d U₀) (support nonempty)` gives `g'` with `coeff d U₀ = g₀ * g' d` on the support and `support.gcd g' = 1`; `U := ∑ d ∈ U₀.support, monomial d (g' d)`; then `map U = (g₀⁻¹ : ℚ) • map U₀ = (N / g₀) • G` (`MvPolynomial.ext`, `coeff_map`, `coeff_sum`, `coeff_monomial`, `Int.cast_mul`, `inv_mul_cancel_left₀`), `g := N / g₀ ≠ 0`; the gcd of `U`'s coefficients on its support equals `support.gcd g'` (support of `U` = `U₀.support` since `g' d ≠ 0` there: `Finset.gcd_congr`/`Finset.gcd_eq_gcd_image`).

#### Mathlib lemmas needed
- `Finset.prod_pos`, `Rat.den_pos`, `Finset.dvd_prod_of_mem`, `Rat.mul_den_eq_num`, `Rat.coe_int_num_of_den_eq_one`
- `Finset.extract_gcd`, `Finset.gcd_eq_zero_iff`, `Finset.gcd_congr`
- `MvPolynomial.coeff_map`, `MvPolynomial.coeff_sum`, `MvPolynomial.coeff_monomial`, `MvPolynomial.coeff_smul`, `MvPolynomial.map_injective`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:421-423
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.9).

#### Generality decision
- any index type `σ`; `ℚ`/`ℤ` coefficients as in the source.

**Progress**:
- 2026-10-12T19:11: DONE


### [T056] Integral factors from a rational factorisation
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T049, T051, T054, T055, CLEANUP-20
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R6.11

#### Statement
```lean
theorem exists_int_factors {U' : MvPolynomial τ ℚ} {V' : Polynomial ℚ} (hU : U' ≠ 0) (hV : V' ≠ 0)
    {F : MvPolynomial (Option τ) ℤ}
    (hF : map (Int.castRingHom ℚ) F = rename some U' * Polynomial.aeval (X none : MvPolynomial (Option τ) ℚ) V') :
    ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
      F = rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V ∧
      (∀ j, degreeOf j U = degreeOf j U') ∧ V.natDegree = V'.natDegree := by sorry
```

#### Proof sketch
1. `exists_primitive_smul_eq hU` gives `g ≠ 0`, `U` integral with `map U = g • U'` and gcd of coefficients `1`. Put `V'' := g⁻¹ • V'`; then `map F = rename some (map U) * aeval (X none) V''` (`smul` pulled through `rename` and `aeval`: `map_smul`, `smul_mul_smul`/`mul_smul_comm`, `inv_mul_cancel₀`).
2. Every coefficient `V''.coeff b` is an integer: for `a ∈ U.support`, `(coeff a U : ℚ) * V''.coeff b = coeff (a.mapDomain some + single none b) (map F)` (`coeff_rename_mul_aeval`, `MvPolynomial.coeff_map` twice) `= ((coeff _ F : ℤ) : ℚ)`; apply `exists_int_eq_of_gcd_eq_one` with the gcd `1`.
3. Define `V := ∑ b ∈ V''.support, Polynomial.monomial b (chosen integer)`; `Polynomial.map (Int.castRingHom ℚ) V = V''` (`Polynomial.ext`, `coeff_map`, `finset_sum_coeff`, `coeff_monomial`); `F = rename some U * aeval (X none) V` by injectivity of `MvPolynomial.map (Int.castRingHom ℚ)` (`map_mul`, `map_rename`, `MvPolynomial.map_aeval`/`Polynomial.aeval_map`-compatibility: `MvPolynomial.map_aeval`?, `Polynomial.map_aeval_eq_aeval_map`).
4. Nonvanishing: `U ≠ 0` (`map U = g • U' ≠ 0`), `V ≠ 0` (`V'' = g⁻¹ • V' ≠ 0`). Degrees: `degreeOf j U = degreeOf j (map U)` (injective map preserves `degreeOf`: `MvPolynomial.degreeOf_map_of_injective`? else via `degreeOf_eq_sup` + `support_map_of_injective`) `= degreeOf j (g • U') = degreeOf j U'` (`degreeOf_C_mul` with `g ∈ ℚ⁰`, `smul_eq_C_mul`); `natDegree V = natDegree V'' = natDegree V'` (`Polynomial.natDegree_map_eq_of_injective`, `Polynomial.natDegree_smul_of_smul_regular`/`natDegree_C_mul`).

#### Mathlib lemmas needed
- `MvPolynomial.map_injective`, `MvPolynomial.map_rename`, `MvPolynomial.coeff_map`, `Polynomial.coeff_map`, `Polynomial.natDegree_map_eq_of_injective`
- `MvPolynomial.support_map_of_injective`, `MvPolynomial.degreeOf_C_mul`, `Polynomial.natDegree_C_mul`, `MvPolynomial.smul_eq_C_mul`
- (project) `exists_primitive_smul_eq`, `coeff_rename_mul_aeval`, `exists_int_eq_of_gcd_eq_one`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 proof of Lemma 2, clean.tex:421-437
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.11).

#### Generality decision
- `ℤ`/`ℚ` as in the source; `[Fintype τ] [DecidableEq τ]`.

**Progress**:
- 2026-10-12T19:13: DONE


### [CLEANUP-21] Run /cleanup on Roth/Separation.lean
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T056
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Separation.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T057] Lemma 2: the determinant of Hasse derivatives separates as U(x_τ)·V(x_none)
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T018, T030, T037, T051, T052, T053, T056, CLEANUP-21
- **Parallel**: no
- **Type**: theorem
- **Decomposition entries**: R6.12

#### Statement
```lean
theorem exists_det_eq_mul {P : MvPolynomial (Option τ) ℤ} (hP : P ≠ 0) {r : Option τ → ℕ}
    (hr : ∀ j, degreeOf j P ≤ r j) :
    ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧
      ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧
        (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧
        (Matrix.of fun μ ν : Fin l =>
            hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =
          rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V := by sorry
```

#### Proof sketch
1. `P_ℚ := map (Int.castRingHom ℚ) P ≠ 0` (`MvPolynomial.map_injective`, `Int.cast_injective`); `degreeOf none P_ℚ ≤ r none` (degree preserved by the injective map).
2. `exists_separated_representation` with `n := r none` gives `l, φ, ψ` (and `1 ≤ l ≤ r none + 1`).
3. `wronskian_ne_zero_of_linearIndependent hφ : wronskian φ ≠ 0`; `exists_genWronskian_ne_zero hψ` gives `D` with `(D μ).degree ≤ μ` and `genWronskian D ψ ≠ 0`.
4. `det_hasseDeriv_separated D φ ψ` rewritten with `P_ℚ = ∑ …` gives `map P_ℚ-det = rename some G * aeval (X none) W` where the left side is `map (Int.castRingHom ℚ)` of the integer determinant (`RingHom.map_det`, `RingHom.mapMatrix_apply`, `hasseDeriv_map`).
5. `exists_int_factors hG hW this` gives `U, V ≠ 0`, the integer factorisation, and `degreeOf j U = degreeOf j G`, `natDegree V = natDegree W`.
6. Degree bounds: `degreeOf (some j) F ≤ l * r (some j)` (`degreeOf_det_hasseDeriv_le`) and `degreeOf (some j) F = degreeOf j U` (`degreeOf_rename_mul_aeval` applied to the integer factorisation, `hV`); likewise `natDegree V = degreeOf none F ≤ l * r none` (`degreeOf_none_rename_mul_aeval`, `hU`). Assemble the `∃`.

#### Mathlib lemmas needed
- `MvPolynomial.map_injective`, `Int.cast_injective`, `RingHom.map_det`, `RingHom.mapMatrix_apply`
- (project) `exists_separated_representation`, `wronskian_ne_zero_of_linearIndependent`, `exists_genWronskian_ne_zero`, `det_hasseDeriv_separated`, `exists_int_factors`, `degreeOf_det_hasseDeriv_le`, `degreeOf_rename_mul_aeval`, `degreeOf_none_rename_mul_aeval`, `hasseDeriv_map`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §2 Lemma 2 (roth:lem2), clean.tex:347-437
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R6.12).

#### Generality decision
- `σ = Option τ` with `[Fintype τ] [DecidableEq τ]` (any `τ`, including empty); integer coefficients.

**Progress**:
- 2026-10-12T19:14: DONE — Lemma 2 proved


### [CLEANUP-22] Run /cleanup on Roth/Separation.lean
- **Status**: done
- **File**: Roth/Separation.lean
- **Depends on**: T057
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Separation.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:14: agent dispatched (Index/Separation)
- 2026-10-12T19:27: agent cleanup of Index/Separation; signatures unchanged


### [T058] ℛ_m, Θ_m: definitions and supremum API
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T041, T046
- **Parallel**: yes
- **Type**: def + API
- **Decomposition entries**: R8.1

#### Statement
```lean
def RSet (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ) :=
  {R | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧ ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}

def indexSet (B : ℝ) (q r : σ → ℕ) : Set ℝ :=
  {x | ∃ R ∈ RSet B r, ∃ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) ∧
    index (map (Int.castRingHom ℝ) R) (fun j => (h j : ℝ) / q j) r = x}

noncomputable def Θ (B : ℝ) (q r : σ → ℕ) : ℝ := sSup (indexSet B q r)

theorem one_mem_RSet {B : ℝ} (hB : 1 ≤ B) (r : σ → ℕ) : (1 : MvPolynomial σ ℤ) ∈ RSet B r := by
  sorry

theorem indexSet_nonempty {B : ℝ} (hB : 1 ≤ B) (q r : σ → ℕ) : (indexSet B q r).Nonempty := by
  sorry

theorem indexSet_bddAbove (B : ℝ) (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    BddAbove (indexSet B q r) := by sorry

theorem index_le_Θ {B : ℝ} {q r : σ → ℕ} (hr : ∀ j, 0 < r j) {R : MvPolynomial σ ℤ}
    (hR : R ∈ RSet B r) {h : σ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j => (h j : ℝ) / q j) r ≤ Θ B q r := by sorry

theorem Θ_nonneg {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    0 ≤ Θ B q r := by sorry

theorem Θ_le_card {B : ℝ} (hB : 1 ≤ B) (q : σ → ℕ) {r : σ → ℕ} (hr : ∀ j, 0 < r j) :
    Θ B q r ≤ Fintype.card σ := by sorry

theorem Θ_le_of_forall_index_le {B : ℝ} (hB : 1 ≤ B) {q r : σ → ℕ} {c : ℝ}
    (hc : ∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
      index (map (Int.castRingHom ℝ) R) (fun j => (h j : ℝ) / q j) r ≤ c) :
    Θ B q r ≤ c := by sorry

theorem Θ_mono {B B' : ℝ} (hB : 1 ≤ B) (hBB' : B ≤ B') (q : σ → ℕ) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) : Θ B q r ≤ Θ B' q r := by sorry
```

#### Proof sketch
1. `one_mem_RSet`: `one_ne_zero`, `degreeOf_one`, `Nat.zero_le`; coefficients: `MvPolynomial.coeff_one` (`if 0 = d then 1 else 0`), `abs_one`/`abs_zero`, `hB`, `zero_le_one.trans hB`.
2. `indexSet_nonempty`: `⟨_, 1, one_mem_RSet hB r, fun _ => 1, fun j => isCoprime_one_left, rfl⟩`.
3. `indexSet_bddAbove`: `⟨Fintype.card σ, _⟩`: `rintro _ ⟨R, ⟨hR0, hRd, _⟩, h, _, rfl⟩`; `index_le_card (map_ne_zero: MvPolynomial.map_injective _ Int.cast_injective …) hr (degreeOf (map R) ≤ degreeOf R ≤ r)` (`MvPolynomial.degreeOf_map_le`?/injective equality).
4. `index_le_Θ`: `le_csSup (indexSet_bddAbove _ _ hr) ⟨R, hR, h, hh, rfl⟩`. `Θ_nonneg`: `(index_nonneg _ _ _).trans (index_le_Θ hr (one_mem_RSet hB r) (fun _ => isCoprime_one_left))` or `le_csSup_of_le`. `Θ_le_card`: `csSup_le (indexSet_nonempty hB q r) (fun x ⟨…⟩ => index_le_card …)`. `Θ_le_of_forall_index_le`: `csSup_le (indexSet_nonempty hB q r)` + `rintro`. `Θ_mono`: `csSup_le_csSup (indexSet_bddAbove _ _ hr) (indexSet_nonempty hB q r)` with `indexSet B q r ⊆ indexSet B' q r` (`RSet` monotone in `B`: `le_trans`).

#### Mathlib lemmas needed
- `le_csSup`, `csSup_le`, `csSup_le_csSup`, `le_csSup_of_le`
- `MvPolynomial.coeff_one`, `MvPolynomial.degreeOf_one`, `isCoprime_one_left`, `MvPolynomial.map_injective`
- (project) `index_le_card`, `index_nonneg`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 definitions of ℛ_m and Θ_m, clean.tex:652-669; Lean note clean.tex:696-699
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R8.1).

#### Generality decision
- `[Fintype σ] [DecidableEq σ]`; `B : ℝ` with `1 ≤ B` where nonemptiness is needed.

**Progress**:
- 2026-10-12T19:15: DONE


### [T059] Θ is invariant under renaming the variables
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T058, T046
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R8.2

#### Statement
```lean
theorem Θ_equiv {τ : Type*} [Fintype τ] [DecidableEq τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ) :
    Θ B (q ∘ e) (r ∘ e) = Θ B q r := by sorry
```

#### Proof sketch
1. `congrArg sSup`; `Set.ext x`; (→) given `R ∈ RSet B (r ∘ e)` and `h`, take `R' := rename e R ∈ RSet B r` (`rename` injective ⇒ `R' ≠ 0`; `degreeOf_rename_of_injective e.injective` gives `degreeOf (e j) R' = degreeOf j R ≤ r (e j)`, and every `i : τ` is `e (e.symm i)`; coefficients: `coeff_rename_mapDomain e.injective` and `MvPolynomial.coeff_rename_eq_zero` for indices not in the image), `h' := h ∘ e.symm`, `IsCoprime` transported (`e.apply_symm_apply`), and `index (map R') (fun i => h' i / q i) r = index (map R) ((…) ∘ e) (r ∘ e)` by `index_rename e.injective` + `MvPolynomial.map_rename` and function extensionality (`e.symm_apply_apply`); (←) symmetric with `e.symm` (`rename_rename`, `e.symm_comp_self`).

#### Mathlib lemmas needed
- `MvPolynomial.rename_injective`, `MvPolynomial.map_rename`, `MvPolynomial.degreeOf_rename_of_injective`, `MvPolynomial.coeff_rename_mapDomain`, `MvPolynomial.coeff_rename_eq_zero`
- `Equiv.apply_symm_apply`, `Equiv.symm_apply_apply`, `Equiv.injective`
- (project) `index_rename`, `RSet`, `indexSet`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §4 Lean note clean.tex:638-640 (variable renaming), used in Lemma 7's induction
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R8.2).

#### Generality decision
- any `e : σ ≃ τ` between finite types.

**Progress**:
- 2026-10-12T19:16: DONE


### [T060] Gauss's lemma step and the leading-coefficient bound for Lemma 5
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R8.3, R8.4

#### Statement
```lean
theorem exists_eq_pow_mul_of_rootMultiplicity {R : Polynomial ℤ} (hR : R ≠ 0) {h : ℤ} {q : ℕ}
    (hq : 0 < q) (hcop : IsCoprime h (q : ℤ)) :
    ∃ Q : Polynomial ℤ, R = (Polynomial.C (q : ℤ) * Polynomial.X - Polynomial.C h) ^
      Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) * Q := by sorry

theorem pow_rootMultiplicity_le {R : Polynomial ℤ} (hR : R ≠ 0) {h : ℤ} {q : ℕ} (hq : 0 < q)
    (hcop : IsCoprime h (q : ℤ)) {B : ℝ} (hB : ∀ n, |((R.coeff n : ℤ) : ℝ)| ≤ B) :
    (q : ℝ) ^ Polynomial.rootMultiplicity ((h : ℚ) / q) (R.map (Int.castRingHom ℚ)) ≤ B := by
  sorry
```

#### Proof sketch
1. `exists_eq_pow_mul_of_rootMultiplicity`: `t := rootMultiplicity (h/q) R_ℚ`; `Polynomial.pow_rootMultiplicity_dvd R_ℚ (h/q) : (X − C (h/q))^t ∣ R_ℚ`; `C (q:ℚ) * X − C (h:ℚ) = C q * (X − C (h/q))` (`mul_sub`, `C_mul`, `mul_div_cancel₀`, `q ≠ 0`), so `(C q X − C h)^t = C (q^t) * (X − C(h/q))^t` divides `R_ℚ` (`mul_pow`, `C_pow`, `IsUnit.mul_dvd`/`Dvd.dvd.mul_left`); `p := C (q:ℤ) * X − C h` is primitive: `Polynomial.isPrimitive_iff_isUnit_of_C_dvd.2`: if `C c ∣ p` then `c ∣ q` and `c ∣ h` (compare coefficients `1` and `0`: `Polynomial.C_dvd_iff_dvd_coeff`), hence `c` is a unit by `IsCoprime.isUnit_of_dvd' hcop`; `IsPrimitive.pow`/`IsPrimitive.mul` iterated; `(IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast (p^t) R hp).2` (with `Polynomial.map_pow`, `map_sub`, `map_mul`, `map_C`, `map_X`) gives `p^t ∣ R`, i.e. `∃ Q, R = p^t * Q`.
2. `pow_rootMultiplicity_le`: from the factorisation, `Q ≠ 0` (`R ≠ 0`); `leadingCoeff R = leadingCoeff (p^t) * leadingCoeff Q` (`Polynomial.leadingCoeff_mul`), `leadingCoeff (p^t) = q^t` (`leadingCoeff_pow`, `leadingCoeff` of `C q * X − C h` is `q`: `Polynomial.leadingCoeff_linear`? — prove via `natDegree_sub_eq_left_of_natDegree_lt` and `leadingCoeff_C_mul_X`); `|leadingCoeff R| = q^t |leadingCoeff Q| ≥ q^t` (`Int.one_le_abs`, `abs_mul`); and `|(leadingCoeff R : ℝ)| ≤ B` by `hB` at `natDegree R` (`Polynomial.leadingCoeff`); cast (`Int.cast_abs`, `Nat.cast_pow`).

#### Mathlib lemmas needed
- `Polynomial.pow_rootMultiplicity_dvd`, `Polynomial.isPrimitive_iff_isUnit_of_C_dvd`, `Polynomial.C_dvd_iff_dvd_coeff`, `IsCoprime.isUnit_of_dvd'`, `Polynomial.IsPrimitive.mul`
- `Polynomial.IsPrimitive.Int.dvd_iff_map_cast_dvd_map_cast`, `Polynomial.map_pow`, `Polynomial.map_sub`
- `Polynomial.leadingCoeff_mul`, `Polynomial.leadingCoeff_pow`, `Polynomial.leadingCoeff_C_mul_X`, `Int.one_le_abs`, `Int.cast_abs`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 5, clean.tex:679-688; Lean note clean.tex:693-695
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R8.3, R8.4).

#### Generality decision
- integer polynomials, `0 < q`, `IsCoprime h q` (sharp).

**Progress**:
- 2026-10-12T19:20: proved, Theta.lean diagnostics clean


### [CLEANUP-23] Run /cleanup on Roth/Theta.lean
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T060
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Theta.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:20: folded into CLEANUP-26 (Theta.lean under active edit)


### [T061] Lemma 5: the one-variable bound Θ_1(B; q; r) ≤ log B / (r log q)
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T047, T050, T058, T060, CLEANUP-23
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R8.5

#### Statement
```lean
theorem Θ_unique_le [Unique σ] {B : ℝ} (hB : 1 ≤ B) {q : σ → ℕ} (hq : 1 < q default) {r : σ → ℕ}
    (hr : 0 < r default) : Θ B q r ≤ Real.log B / (r default * Real.log (q default)) := by sorry
```

#### Proof sketch
1. `Θ_le_of_forall_index_le hB`; fix `R ∈ RSet B r` and coprime `h`; `R' := uniqueAlgEquiv ℤ σ R : ℤ[X]` (`R' ≠ 0`), with `|R'.coeff n| ≤ B` (`coeff_uniqueAlgEquiv_symm` on `R = e.symm R'`).
2. `index_unique (map_ne_zero) : index = (rootMultiplicity (h/q : ℝ) (uniqueAlgEquiv ℝ σ (map R)) : ℝ) / r default`; identify `uniqueAlgEquiv ℝ σ (map R) = Polynomial.map (Int.castRingHom ℝ) R'` (`algHom_ext` on `X`) and `rootMultiplicity (↑(h/q : ℚ)) (map ℚ→ℝ R'_ℚ) = rootMultiplicity (h/q) R'_ℚ` (`Polynomial.eq_rootMultiplicity_map (Rat.cast_injective)`, `Polynomial.map_map`, `Rat.cast_div`).
3. `pow_rootMultiplicity_le` gives `q^t ≤ B`; `Real.log_le_log (by positivity) this`, `Real.log_pow`, so `t * log q ≤ log B`, then `t / r ≤ log B / (r * log q)` (`div_le_div_iff`, `Real.log_pos (by exact_mod_cast hq)`, `Nat.cast_pos.2 hr`).

#### Mathlib lemmas needed
- `Polynomial.eq_rootMultiplicity_map`, `Polynomial.map_map`, `Rat.cast_injective`
- `Real.log_le_log`, `Real.log_pow`, `Real.log_pos`, `div_le_div_iff`
- (project) `Θ_le_of_forall_index_le`, `index_unique`, `coeff_uniqueAlgEquiv_symm`, `pow_rootMultiplicity_le`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 Lemma 5 (roth:lem5), clean.tex:671-690
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R8.5).

#### Generality decision
- `[Unique σ]`; `1 ≤ B`, `1 < q`, `0 < r`.

**Progress**:
- 2026-10-12T19:20: proved, Theta.lean diagnostics clean


### [T062] Numerical lemmas for Lemma 6 (the two FACTs and the min bound)
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: CLEANUP-23
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R9.2, R9.3, R9.4

#### Statement
```lean
theorem floor_sq_div_two_le_sum {a : ℝ} (ha : 0 ≤ a) :
    (⌊a⌋₊ : ℝ) ^ 2 / 2 ≤ ∑ ν ∈ Finset.range (⌊a⌋₊ + 1), (a - ν) := by sorry

theorem sq_div_three_lt_floor_sq_div_two {a : ℝ} (ha : 10 < a) :
    a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2 := by sorry

theorem min_le_sum_max {θ : ℝ} {rp : ℕ} (hrp : 0 < rp) (hθ : 10 < θ * rp) (l : ℕ) :
    min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ν / rp) := by sorry
```

#### Proof sketch
1. `floor_sq_div_two_le_sum`: `Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_range`, `Finset.sum_range_id_mul_two` (cast to `ℝ`: `Nat.cast_sum`), `n := ⌊a⌋₊`, `Nat.floor_le ha : n ≤ a`; `nlinarith`.
2. `sq_div_three_lt_floor_sq_div_two`: `n := ⌊a⌋₊`, `Nat.lt_floor_add_one a : a < n + 1`, `Nat.le_floor (by norm_num : (10:ℝ) ≤ a)`-type `10 ≤ n`; `nlinarith`.
3. `min_le_sum_max`: by cases `(l : ℝ) ≤ θ * rp`: `min_le_left`; each term is `θ − ν/rp` (`max_eq_right`, `ν ≤ l−1 < θ rp`), `Finset.sum_sub_distrib`, `Finset.sum_range_id_mul_two`, `nlinarith` with `l/rp ≤ θ`. Else (`θ rp < l`): `min_le_right`; `n := ⌊θ rp⌋₊ < l` (`Nat.floor_lt`), `Finset.sum_le_sum_of_subset_of_nonneg (Finset.range_subset.2 …) (fun _ _ _ => le_max_left _ _)` to restrict to `range (n+1)`, where `max 0 (θ − ν/rp) = θ − ν/rp` (`ν ≤ n ≤ θ rp`); `= (1/rp) ∑ (θ rp − ν)` (`Finset.sum_div`, `field_simp`) `≥ n²/(2 rp)` (`floor_sq_div_two_le_sum`) `> rp θ²/3` (`sq_div_three_lt_floor_sq_div_two` with `a := θ rp > 10`, `div_lt_div_of_pos_right`).

#### Mathlib lemmas needed
- `Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.sum_range_id_mul_two`, `Nat.cast_sum`
- `Nat.floor_le`, `Nat.lt_floor_add_one`, `Nat.le_floor`, `Nat.floor_lt`
- `Finset.sum_le_sum_of_subset_of_nonneg`, `Finset.range_subset`, `le_max_left`, `max_eq_right`, `div_lt_div_of_pos_right`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 6, clean.tex:855-921 and Lean note clean.tex:915-921
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R9.2, R9.3, R9.4).

#### Generality decision
- pure real-number statements with explicit positivity hypotheses.

**Progress**:
- 2026-10-12T19:20: proved, Theta.lean diagnostics clean


### [T063] Lower bound for the index of the determinant
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T042, T043, T045, T011, T012, CLEANUP-23
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R9.5

#### Statement
```lean
theorem sum_max_sub_le_index_det {R : MvPolynomial (Option τ) ℝ} (hR : R ≠ 0) {l : ℕ}
    (D : Fin l → (τ →₀ ℕ)) (hD : ∀ μ, (D μ).degree ≤ μ)
    (hdet : (Matrix.of fun μ ν : Fin l =>
      hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0)
    (α : Option τ → ℝ) {r : Option τ → ℕ} (hr : ∀ j, 0 < r j) {δ : ℝ}
    (hδ : ∀ d : τ →₀ ℕ, d.degree ≤ l - 1 → weight (r ∘ some) d ≤ δ) :
    ∑ ν ∈ Finset.range l, max 0 (index R α r - ν / r none) - l * δ ≤
      index (Matrix.of fun μ ν : Fin l =>
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by sorry
```

#### Proof sketch
1. `Matrix.det_apply'`; `le_index_sum hdet` (after rewriting the determinant as the sum): for each `σ` with nonzero term, `index (ε σ * ∏ …) = index (∏ …)` (`Int.units_eq_one_or`, `Int.cast_one`, `one_mul`, `Int.cast_neg`, `neg_one_mul`, `index_neg`).
2. `index_prod` for the nonzero product (all factors nonzero: `Finset.prod_ne_zero_iff`); for factor `ν` with `E := hasseDeriv ((D (σ ν)).mapDomain some + single none ν) R ≠ 0`: `index_hasseDeriv_ge hE : index R − weight r (…) ≤ index E`, `weight_add`, `weight_mapDomain (Option.some_injective _)`, `weight_single`, `hδ (D (σ ν)) ((hD _).trans …)` (`σ ν ≤ l − 1`: `Fin.is_le`), so `index E ≥ index R − ν/r none − δ`, and `index E ≥ 0` (`index_nonneg`), hence `≥ max 0 (index R − ν / r none) − δ` (`le_max_iff`, `linarith`).
3. Sum over `ν`: `Finset.sum_le_sum`, `Finset.sum_sub_distrib`, `Finset.sum_const`, `Finset.card_fin`/`Fin.sum_univ_eq_sum_range`, `nsmul_eq_mul`; the composition with `σ` reindexes nothing on the `ν` side (the product is over `ν` with rows `σ ν`).

#### Mathlib lemmas needed
- `Matrix.det_apply'`, `Int.units_eq_one_or`, `Finset.prod_ne_zero_iff`, `Fin.sum_univ_eq_sum_range`, `Fin.is_le`
- (project) `le_index_sum`, `index_neg`, `index_prod`, `index_hasseDeriv_ge`, `index_nonneg`, `weight_add`, `weight_mapDomain`, `weight_single`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 6, clean.tex:786-854
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R9.5).

#### Generality decision
- real polynomials in `Option τ` variables; `δ` any bound for the weights of degree-`≤ l−1` multi-indices in the `τ`-variables.

**Progress**:
- 2026-10-12T19:20: proved, Theta.lean diagnostics clean


### [CLEANUP-24] Run /cleanup on Roth/Theta.lean
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T063
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Theta.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:20: folded into CLEANUP-26 (Theta.lean under active edit)


### [T064] Upper bound (17): the index of F is at most l·Φ
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T030, T045, T046, T049, T050, T057, T058, CLEANUP-24
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R9.1, R9.6

#### Statement
```lean
noncomputable def lem6M (p r₁ : ℕ) (B : ℝ) (l : ℕ) : ℝ :=
  ((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r₁)

noncomputable def lem6Φ (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ :=
  Θ M (fun _ : Unit => q none) (fun _ => l * r none) + Θ M (q ∘ some) fun j => l * r (some j)

theorem index_det_le {δ : ℝ} {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ} (hB : 1 ≤ B) {R : MvPolynomial (Option τ) ℤ}
    (hR : R ∈ RSet B r) {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ}
    (hl : 1 ≤ l) (hl' : l ≤ r none + 1) {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ}
    {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0) (hUd : ∀ j, degreeOf j U ≤ l * r (some j))
    (hVd : V.natDegree ≤ l * r none)
    (hF : (Matrix.of fun μ ν : Fin l =>
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =
      rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V) (hδ : 0 < δ) :
    index (map (Int.castRingHom ℝ) (Matrix.of fun μ ν : Fin l =>
        hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)
      (fun j => (h j : ℝ) / q j) r ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l := by
  sorry
```

#### Proof sketch
1. Coefficient bound for `F`: `abs_coeff_det_hasseDeriv_le` with `E μ ν := (D μ).mapDomain some + single none ν`, then `∏ (r_j+1) ≤ (r₁+1)^p` (`Finset.prod_le_pow_card`, `Fintype.card_option`) and `∑ r_j ≤ p r₁` (`Finset.sum_le_card_nsmul`), monotonicity of powers (`pow_le_pow_left`, `pow_le_pow_right`), so `|coeff d F| ≤ lem6M (card τ + 1) r₁ B l =: M`; also `1 ≤ M` (`one_le_pow_of_one_le`, `Nat.one_le_cast.2 (Nat.factorial_pos _)`, `hB`).
2. Coefficients of `U` and `V`: from `hF`, `coeff_rename_mul_aeval`: `coeff a U * V.coeff b = coeff (…) F`; pick `b` with `V.coeff b ≠ 0` (`Polynomial.exists_coeff_ne_zero`? / `leadingCoeff_ne_zero`), `|coeff a U| ≤ |coeff a U| * |V.coeff b| ≤ M` (`Int.one_le_abs`, `le_mul_of_one_le_right`); symmetric for `V`. Hence `U ∈ RSet M (fun j => l * r (some j))` and `V' := (uniqueAlgEquiv ℤ Unit).symm V ∈ RSet M (fun _ => l * r none)` (`coeff_uniqueAlgEquiv_symm`, `degreeOf_uniqueAlgEquiv_symm`, `Finsupp.unique_single`).
3. Lemma 4-2 in Lean: `map F = rename some (map U) * rename (fun _ => none) (map V')` (`MvPolynomial.map_mul`, `map_rename`, `aeval_X_eq_rename`, `map` through `uniqueAlgEquiv`); `index_mul` (both nonzero), `index_rename` twice: `index (map F) a r = index (map U) (a ∘ some) (r ∘ some) + index (map V') (a ∘ const) (r ∘ const)`.
4. Scaling: `index (map U) _ (r ∘ some) = l * index (map U) _ (fun j => l * r (some j))` (`index_mul_left_weights` with `0 < l`, `div_eq_iff`), and `≤ l * Θ M (q ∘ some) (…)` by `index_le_Θ` (positivity of `l * r`), coprimality `hh (some j)`; same for `V'` with `Θ M (fun _ : Unit => q none) (fun _ => l * r none)`. Conclude `≤ l * lem6Φ …` (`mul_add`).

#### Mathlib lemmas needed
- `Finset.prod_le_pow_card`, `Finset.sum_le_card_nsmul`, `Fintype.card_option`, `pow_le_pow_left`, `pow_le_pow_right`, `Nat.factorial_pos`
- `Int.one_le_abs`, `le_mul_of_one_le_right`, `Polynomial.leadingCoeff_ne_zero`, `Finsupp.unique_single`
- `MvPolynomial.map_mul`, `MvPolynomial.map_rename`, `div_eq_iff`
- (project) `abs_coeff_det_hasseDeriv_le`, `coeff_rename_mul_aeval`, `coeff_uniqueAlgEquiv_symm`, `degreeOf_uniqueAlgEquiv_symm`, `aeval_X_eq_rename`, `index_mul`, `index_rename`, `index_mul_left_weights`, `index_le_Θ`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 6, clean.tex:729-784 (eq. (17) and its Lean note)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R9.1, R9.6).

#### Generality decision
- `Option τ` variables; hypotheses `r j ≤ r₁` (the source's `r_1 > ⋯ > r_p` is only used for this).

**Progress**:
- 2026-10-12T19:24: proved


### [T065] Lemma 6: Θ_p bounded by Θ_{p−1} and Θ_1
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T057, T062, T063, T064, CLEANUP-24
- **Parallel**: no
- **Type**: theorem
- **Decomposition entries**: R9.7, R9.8

#### Statement
```lean
theorem index_le_lem6 {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j)
    (hrp : 10 / δ < r none) (hratio : ∀ j, (r none : ℝ) < δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B)
    {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧
      index (map (Int.castRingHom ℝ) R) (fun j => (h j : ℝ) / q j) r ≤
        2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
          √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by sorry

theorem Θ_option_le {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j)
    (hrp : 10 / δ < r none) (hratio : ∀ j, (r none : ℝ) < δ * r (some j)) {r₁ : ℕ}
    (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B) :
    Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' (Finset.nonempty_Icc.2 (by omega))
      (fun l => lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l +
        √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ) := by sorry
```

#### Proof sketch
1. `index_le_lem6`: `exists_det_eq_mul hR.1 hR.2.1` gives `l, D, U, V`; `F ≠ 0` (`mul_ne_zero`, `rename_injective`, `aeval_X_eq_rename` + `rename_injective` + `AlgEquiv.injective`); `θ := index (map R) (h/q) r`; `Φ := lem6Φ …`, `0 ≤ Φ` (`Θ_nonneg` twice, `1 ≤ M`).
2. Case `θ * r none ≤ 10`: `θ ≤ 10 / r none < δ` (`div_lt_iff`, `hrp`), `δ < √δ` (`Real.lt_sqrt`, `δ < 1`, `δ² < δ`), `√δ ≤ 2(Φ + √Φ + √δ)` (`Real.sqrt_nonneg`), done.
3. Case `10 < θ * r none`: `index_det_le … : index (map F) (h/q) r ≤ l Φ`; `sum_max_sub_le_index_det (map R ≠ 0) D hD hFne (h/q) hr0 hδ' : ∑_{ν<l} max 0 (θ − ν/r none) − lδ ≤ index (map F) …` where `hδ'` : for `d` with `d.degree ≤ l−1 ≤ r none`, `weight (r ∘ some) d ≤ d.degree / m ≤ r none · δ / r none = δ` (`weight_le_degree_div` with `m := ⌈r none/δ⌉`-free: use `m := r none + 1`? — better: `hratio j : r none < δ r (some j)` gives `d.degree / r (some j) ≤ d.degree δ / r none` termwise: prove `weight (r∘some) d ≤ δ` directly: `weight = ∑ d j / r (some j) ≤ ∑ d j δ / r none = δ d.degree / r none ≤ δ` using `d.degree ≤ l − 1 ≤ r none`), then `min_le_sum_max hr0 h10 l`, so `min (lθ/2) (r none θ²/3) ≤ l (Φ + δ)` (`linarith`).
4. Subcase `lθ/2 ≤ l(Φ+δ)`: `θ ≤ 2(Φ+δ) ≤ 2(Φ + √Φ + √δ)` (`δ ≤ √δ` from `δ < 1`: `Real.le_sqrt`, `Real.sqrt_nonneg`). Subcase `r none θ²/3 ≤ l(Φ+δ) ≤ (r none + 1)(Φ+δ) < (4/3) r none (Φ+δ)` (`hl'`, `r none > 3` from `hrp` and `δ < 1`): `θ² < 4(Φ+δ)` so `θ < 2√(Φ+δ)` (`Real.lt_sqrt`, `abs_lt_of_sq_lt`-style: `θ ≥ 0` by `index_nonneg`, `Real.sqrt_lt_sqrt`/`Real.lt_sqrt`), and `√(Φ+δ) ≤ √Φ + √δ` (`Real.sqrt_le_sqrt`-free: square both sides, `Real.sq_sqrt`, `Real.sqrt_nonneg`, `nlinarith`).
5. `Θ_option_le`: `Θ_le_of_forall_index_le hB`; for `R, h` get `l` from `index_le_lem6`; `Finset.le_sup' _ (Finset.mem_Icc.2 ⟨hl, hl'⟩)` and `mul_le_mul_left two_pos`.

#### Mathlib lemmas needed
- `div_lt_iff`, `Real.lt_sqrt`, `Real.le_sqrt`, `Real.sqrt_nonneg`, `Real.sq_sqrt`, `Real.sqrt_lt_sqrt`
- `Finset.le_sup'`, `Finset.mem_Icc`, `mul_le_mul_left`
- (project) `exists_det_eq_mul`, `index_det_le`, `sum_max_sub_le_index_det`, `min_le_sum_max`, `Θ_nonneg`, `Θ_le_of_forall_index_le`, `index_nonneg`, `weight_le_degree_div`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 Lemma 6 (roth:lem6), clean.tex:704-933
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R9.7, R9.8).

#### Generality decision
- `Option τ` variables; hypotheses are the ones the source's proof uses (`r_p > 10/δ`, `r_p < δ r_j`, `r_j ≤ r₁`).

**Progress**:
- 2026-10-12T19:24: proved index_le_lem6 + Θ_option_le


### [T066] The constant M is below q_1^{δ_1 l r_1}
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T064, CLEANUP-24
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R10.1

#### Statement
```lean
theorem lem6M_lt {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ : ℕ} (hr₁ : 0 < r₁) {q₁ : ℕ}
    (hq₁ : (p : ℝ) * (2 * p + 1) / δ < Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) :
    lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁)) := by sorry
```

#### Proof sketch
1. Unfold `lem6M` with `B = q₁^{δ r₁}`: `M = (r₁+1)^{pl} · l! · (q₁^{δ r₁})^l · 2^{p l r₁}`.
2. Bounds in `ℝ`: `l! ≤ l^l` (`Nat.factorial_le_pow`, cast), `l ≤ r₁ < r₁ + 1 ≤ 2^{r₁}` (`Nat.lt_two_pow_self`), `(r₁+1)^{pl} ≤ (2^{r₁})^{pl}`, so `M ≤ (2^{(2p+1) r₁})^l (q₁^{δ r₁})^l` (`pow_le_pow_left`, `pow_mul`, `mul_pow`); `2 < exp 1` (`Real.add_one_lt_exp one_ne_zero` gives `1 + 1 < exp 1`), so `2^{(2p+1)r₁} < exp ((2p+1) r₁)` (`Real.exp_one_rpow`-free: `Real.rpow_natCast`, `pow_lt_pow_left`), and `(2p+1) r₁ < (δ/p) log q₁ · r₁` from `hq₁` (`div_lt_iff`), hence `exp ((2p+1) r₁) < q₁^{(δ/p) r₁}` (`Real.rpow_def_of_pos`, `Real.exp_lt_exp`).
3. Combine: `M < (q₁^{δ r₁ / p} · q₁^{δ r₁})^l = q₁^{δ(1+1/p) l r₁}` (`Real.rpow_add`, `Real.rpow_natCast`, `Real.rpow_mul`, `mul_comm`); strictness from positivity (`Real.rpow_pos_of_pos`, `mul_lt_mul_of_pos_right`, `pow_lt_pow_left`).

#### Mathlib lemmas needed
- `Nat.factorial_le_pow`, `Nat.lt_two_pow_self`, `pow_le_pow_left`, `pow_lt_pow_left`
- `Real.add_one_lt_exp`, `Real.exp_lt_exp`, `Real.rpow_def_of_pos`, `Real.rpow_add`, `Real.rpow_mul`, `Real.rpow_natCast`, `Real.rpow_pos_of_pos`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 7, clean.tex:950-964
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R10.1).

#### Generality decision
- `p ≥ 2`, `0 < δ`, `0 < r₁`, `1 ≤ l ≤ r₁`, `(p(2p+1))/δ < log q₁`.

**Progress**:
- 2026-10-12T19:32: proved; Theta.lean sorry-free, diagnostics clean


### [CLEANUP-25] Run /cleanup on Roth/Theta.lean
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T066
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Theta.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:24: folded into CLEANUP-26 (Theta.lean under active edit)


### [T067] Numerical estimates for the induction step of Lemma 7
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: CLEANUP-25
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R10.2, R10.3

#### Statement
```lean
theorem lem7_Φ_bound {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) :
    δ * (1 + 1 / p) + 10 ^ (p - 1) * (δ * (1 + 1 / p)) ^ ((1 / 2 : ℝ) ^ (p - 1)) <
      3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1)) := by sorry

theorem lem7_numeric {p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {Φ : ℝ}
    (hΦ0 : 0 ≤ Φ) (hΦ : Φ < 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))) :
    2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ ((1 / 2 : ℝ) ^ p) := by sorry
```

#### Proof sketch
1. `lem7_Φ_bound`: `e := (1/2)^{p−1} ∈ (0, 1]`; `δ ≤ δ^e` (`Real.rpow_le_rpow_of_exponent_ge hδ0 hδ1.le`, `e ≤ 1`), `(δ(1+1/p))^e = δ^e (1+1/p)^e` (`Real.mul_rpow`), `(1+1/p)^e ≤ 1 + 1/p ≤ 3/2` (`Real.rpow_le_rpow_of_exponent_le` with base `≥ 1`, `e ≤ 1`, `Real.rpow_one`), `δ(1+1/p) ≤ (3/2)δ < 2δ^e`; `2 ≤ 10^{p−1}` (`Nat.one_le_two_pow`-style, `pow_le_pow_right`); `nlinarith [Real.rpow_pos_of_pos hδ0 e]`.
2. `lem7_numeric`: `a := δ^{(1/2)^p}`, `0 < a ≤ 1` (`Real.rpow_pos_of_pos`, `Real.rpow_le_one`), `a^2 = δ^{(1/2)^{p−1}}` (`Real.rpow_natCast_mul`/`← Real.rpow_mul`, `pow_succ`, `mul_comm`), `√δ ≤ a` (`Real.sqrt_eq_rpow`, `Real.rpow_le_rpow_of_exponent_ge`, `(1/2)^p ≤ 1/2`), `√Φ < √(3·10^{p−1}) · a` (`Real.sqrt_lt_sqrt`, `Real.sqrt_mul`, `Real.sqrt_sq`), `√(3·10^{p−1}) ≤ √3 · 10^{p−1}` (`Real.sqrt_le_sqrt`, `Real.sqrt_mul_self`); then `2(Φ + √Φ + √δ) < 2(3·10^{p−1} a² + √3 10^{p−1} a + a) ≤ 2a(3·10^{p−1} + √3·10^{p−1} + 1) < 10^p a` because `6 + 2√3 + 2/10^{p−1} < 10` (`Real.sqrt_lt' `: `√3 < 1.75`, `10^{p−1} ≥ 10`); `nlinarith`.

#### Mathlib lemmas needed
- `Real.rpow_le_rpow_of_exponent_ge`, `Real.mul_rpow`, `Real.rpow_le_rpow_of_exponent_le`, `Real.rpow_le_one`, `Real.rpow_pos_of_pos`
- `Real.rpow_mul`, `Real.rpow_natCast`, `Real.sqrt_eq_rpow`, `Real.sqrt_lt_sqrt`, `Real.sqrt_lt'`, `Real.sqrt_mul_self`
- `pow_le_pow_right`, `nlinarith`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 proof of Lemma 7, clean.tex:1008-1041 and Lean note clean.tex:1042-1045
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R10.2, R10.3).

#### Generality decision
- pure real-number statements; `p ≥ 2`, `0 < δ < 1`.

**Progress**:
- 2026-10-12T19:32: proved; Theta.lean sorry-free, diagnostics clean


### [T068] Lemma 7: Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T058, T059, T061, T065, T066, T067, CLEANUP-25
- **Parallel**: no
- **Type**: theorem
- **Decomposition entries**: R10.4

#### Statement
```lean
theorem Θ_lt (n : ℕ) {δ : ℝ} (hδ0 : 0 < δ) (hδ : δ < 1 / ((n : ℝ) + 1)) {r q : Fin (n + 1) → ℕ}
    (hr0 : ∀ j, 0 < r j) (hrlast : 10 / δ < r (Fin.last n))
    (hratio : ∀ i : Fin n, (r i.succ : ℝ) / δ < r i.castSucc) (hq0 : ∀ j, 0 < q j)
    (hq1 : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ < Real.log (q 0))
    (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) :
    Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1)) := by sorry
```

#### Proof sketch
1. Induction on `n`. Base `n = 0`: `Fin 1` is `Unique` (`default = 0`); `B := q 0 ^ (δ r 0) ≥ 1` (`Real.one_le_rpow`), `1 < q 0` (`log q 0 > 3/δ > 0`: `Real.log_pos_iff`), `Θ_unique_le hB hq hr0 : Θ ≤ log B / (r 0 log q 0) = δ` (`Real.log_rpow`, `mul_div_assoc`, `div_self`); `δ < 10 √δ` (`Real.lt_sqrt`-type: `δ < √δ` since `δ² < δ`; `(1/2)^1 = 1/2`, `Real.sqrt_eq_rpow`).
2. Step (`Fin (n+2)`, `p := n+2`): `Θ_equiv finSuccEquivLast` transports to `Option (Fin (n+1))` (`finSuccEquivLast_last`, `finSuccEquivLast_castSucc`); derive antitonicity of `r` from `hratio` and `δ < 1` (`Fin.induction`/`Fin.le_iff_val_le_val`), hence `hr₁ : r j ≤ r 0`, `hratio' : r last < δ r j` (`r_n > r_last/δ`), `r_last + 1 ≤ r 0` (`l ≤ r 0` for every `l ≤ r_last + 1`).
3. Apply `Θ_option_le` with `B := q 0^{δ r 0}`, `r₁ := r 0`; for each `l ∈ Icc 1 (r_last+1)`: `lem6M_lt` gives `M < q 0 ^ (δ₁ (l r 0))`, `δ₁ := δ(1+1/p)`; `Θ_mono` (needs `1 ≤ M`) + `Θ_unique_le` give `Θ_1(M; q last; l r last) ≤ δ₁` (`log(q 0^{δ₁ l r 0}) / (l r_last log q_last) ≤ δ₁` from `hqr last`); `Θ_mono` + induction hypothesis (for `n+1` with `δ₁`, `q ∘ castSucc`, `l • r ∘ castSucc`; hypotheses: `δ₁ < 1/(n+1)` via `(p−1)(p+1) < p²`, `hrlast'`, `hratio'` (cancel `l`), `hq1'` via `(p−1)(2p−1) p < p(2p+1)(p+1)`-type `nlinarith`, `hqr'` (`mul_assoc`, `mul_le_mul_left`)) give `Θ_{p−1}(…) < 10^{n+1} δ₁^{(1/2)^{n+1}}`; `lem7_Φ_bound` ⇒ `Φ_l < 3·10^{n+1} δ^{(1/2)^{n+1}}`; `lem7_numeric` ⇒ `2(Φ_l + √Φ_l + √δ) < 10^{n+2} δ^{(1/2)^{n+2}}`.
4. `Finset.sup'_lt_iff` turns the per-`l` strict bounds into a strict bound on the `sup'`, and `Θ ≤ 2 sup' < …` concludes (`lt_of_le_of_lt`).

#### Mathlib lemmas needed
- `finSuccEquivLast`, `finSuccEquivLast_last`, `finSuccEquivLast_castSucc`, `Finset.sup'_lt_iff`
- `Real.one_le_rpow`, `Real.log_rpow`, `Real.log_pos_iff`, `Real.lt_sqrt`, `Real.sqrt_eq_rpow`
- (project) `Θ_equiv`, `Θ_option_le`, `Θ_unique_le`, `Θ_mono`, `lem6M_lt`, `lem7_Φ_bound`, `lem7_numeric`, `Θ_nonneg`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §5 Lemma 7 (roth:lem7), clean.tex:935-1045
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R10.4).

#### Generality decision
- `Fin (n+1)` variables in the source's order (`0 ↔ x_1`, `Fin.last ↔ x_m`); hypotheses (19)–(22) verbatim.

**Progress**:
- 2026-10-12T19:32: proved; Theta.lean sorry-free, diagnostics clean


### [CLEANUP-26] Run /cleanup on Roth/Theta.lean
- **Status**: done
- **File**: Roth/Theta.lean
- **Depends on**: T068
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Theta.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:32: background agent (also covers folded CLEANUP-23/24/25)
- 2026-10-12T19:44: agent cleanup of Theta.lean; signatures unchanged


### [T069] Lemma m–δ (fixed-m form) and η < γ
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + lemma
- **Decomposition entries**: R12.1, R12.2, R12.3

#### Statement
```lean
noncomputable def lam (δ : ℝ) (n m : ℕ) : ℝ := 4 * (1 + 3 * δ) * n * √(m : ℝ)

noncomputable def gam (δ : ℝ) (n m : ℕ) : ℝ := ((m : ℝ) - lam δ n m) / 2

noncomputable def eta (δ : ℝ) (m : ℕ) : ℝ := 10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)

noncomputable def B₁ (δ : ℝ) (q₁ r₁ : ℕ) : ℕ := ⌊(q₁ : ℝ) ^ (δ * r₁)⌋₊

theorem exists_delta_bound {n m : ℕ} (hn : 0 < n) (hm : 16 * n ^ 2 < m) :
    ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 < δ → δ < δ₀ →
      δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 := by sorry

theorem eta_lt_gam_iff (δ : ℝ) (n m : ℕ) :
    eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ eta δ m < gam δ n m := by sorry
```

#### Proof sketch
1. `exists_delta_bound`: `E := m/2 − 2n√m > 0` (from `16n² < m`: `4n < √m` by `Real.lt_sqrt`, `nlinarith`); `δ₀ := min (1/m) (min (E/(12 n √m)) ((E/(2·10^m))^(2^m : ℕ)))`, all positive (`div_pos`, `pow_pos`, `Real.sqrt_pos`, `Nat.cast_pos.2 hn`); for `δ < δ₀`: `δ < 1/m` (`lt_min_iff`); `eta δ m = 10^m δ^{(1/2)^m} < E/2` because `δ < (E/(2·10^m))^{2^m}` ⇒ `δ^{(1/2)^m} < E/(2·10^m)` (`Real.rpow_lt_rpow hδ0.le h (by positivity)` then `Real.rpow_natCast`, `← Real.rpow_mul`, `(2^m : ℝ) * (1/2)^m = 1` by `mul_pow`-style `one_div_pow`, `Real.rpow_one`); `6 δ n √m < E/2` from `δ < E/(12n√m)` (`lt_div_iff`); conclude `linarith`.
2. `eta_lt_gam_iff`: unfold `gam`, `lam`; `constructor <;> intro h <;> linarith`.

#### Mathlib lemmas needed
- `Real.lt_sqrt`, `Real.sqrt_pos`, `lt_min_iff`, `div_pos`, `lt_div_iff`
- `Real.rpow_lt_rpow`, `Real.rpow_natCast`, `Real.rpow_mul`, `one_div_pow`, `Real.rpow_one`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 Lemma m-delta, clean.tex:1211-1263 and Lean note clean.tex:1303-1309; eq. (38) clean.tex:1357-1360
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.1, R12.2, R12.3).

#### Generality decision
- `0 < n` (needed by the explicit threshold), `16n² < m`.

**Progress**:
- 2026-10-12T19:35: proved


### [T070] B₁ is large: the floor estimate and the three small factors
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R12.4–R12.7

#### Statement
```lean
theorem sqrt_lt_floor {X : ℝ} (hX : 4 < X) : √X < ⌊X⌋₊ ∧ (⌊X⌋₊ : ℝ) ≤ X := by sorry

theorem four_lt_rpow {δ : ℝ} (hδ0 : 0 < δ) {m : ℕ} (hm : 1 ≤ m) (hδm : δ < 1 / m) {q₁ r₁ : ℕ}
    (hr₁ : 0 < r₁) (hq₁ : (2 * m + 1 : ℝ) < δ ^ 2 * Real.log q₁) : 4 < (q₁ : ℝ) ^ (δ * r₁) := by
  sorry

theorem log_B₁_gt {δ : ℝ} (hδ0 : 0 < δ) {q₁ r₁ : ℕ} (hq₁ : 1 < q₁) (hr₁ : 0 < r₁)
    (hX : 4 < (q₁ : ℝ) ^ (δ * r₁)) :
    δ * r₁ * Real.log q₁ / 2 < Real.log (B₁ δ q₁ r₁) := by sorry

theorem three_small_factors {δ : ℝ} (hδ0 : 0 < δ) {m : ℕ} (hm : 1 ≤ m) (hδm : δ < 1 / m)
    {q₁ r₁ : ℕ} (hq₁ : 1 < q₁) (hr₁ : 0 < r₁) {A α : ℝ} (hA : 1 ≤ A)
    (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) <
      δ ^ 2 * Real.log q₁) :
    (2 : ℝ) ^ (m * r₁) < (B₁ δ q₁ r₁ : ℝ) ^ δ ∧ (1 + A) ^ (m * r₁) < (B₁ δ q₁ r₁ : ℝ) ^ δ ∧
      (1 + |α|) ^ (m * r₁) < (B₁ δ q₁ r₁ : ℝ) ^ δ := by sorry
```

#### Proof sketch
1. `sqrt_lt_floor`: `⌊X⌋₊ ≤ X` is `Nat.floor_le (by positivity)`; `√X < ⌊X⌋₊`: `X − 1 < ⌊X⌋₊` (`Nat.sub_one_lt_floor`) and `√X < X − 1` (`√X > 2` from `4 < X` via `Real.lt_sqrt`; then `X − 1 − √X = √X(√X − 1) − 1 > 2·1 − 1 > 0`: `nlinarith [Real.sq_sqrt (le_of_lt (by linarith : (0:ℝ) < X))]`).
2. `four_lt_rpow`: `Real.rpow_def_of_pos (Nat.cast_pos.2 (by omega))`: `q₁^{δ r₁} = exp (δ r₁ log q₁)`; `log q₁ > (2m+1)/δ² > 0`; `δ r₁ log q₁ ≥ δ log q₁ > (2m+1)/δ > m(2m+1) ≥ 3` (`δ < 1/m`, `div_lt_iff`); `exp 3 > 4` (`Real.add_one_lt_exp`: `exp 1 > 2`, `exp 3 = (exp 1)^3 > 8`; `Real.exp_nat_mul`/`Real.exp_one_pow`), `Real.exp_lt_exp`.
3. `log_B₁_gt`: `B₁ = ⌊X⌋₊ > √X` (`sqrt_lt_floor hX`), `Real.log_lt_log (Real.sqrt_pos.2 …)`, `Real.log_sqrt`, `Real.log_rpow (Nat.cast_pos …)`.
4. `three_small_factors`: each is `A^{m r₁} < B₁^δ ↔ m r₁ log A < δ log B₁` (`Real.log_lt_log_iff`, `Real.log_pow`, `Real.log_rpow`, `B₁ > 0`); with `log_B₁_gt`: `δ log B₁ > δ² r₁ log q₁ / 2`; from `h32`: `δ² log q₁ > 2m log 2` (`Real.log_two_lt_d9`, `log 2 < 1`), `> 2m log(1+A)`, `> 2m log(1+|α|)` (the omitted terms are `≥ 0`: `Real.log_nonneg`, `mul_nonneg`); multiply by `r₁/2`; `nlinarith`/`linarith` with `Real.log_nonneg`.

#### Mathlib lemmas needed
- `Nat.floor_le`, `Nat.sub_one_lt_floor`, `Real.lt_sqrt`, `Real.sq_sqrt`
- `Real.rpow_def_of_pos`, `Real.exp_lt_exp`, `Real.add_one_lt_exp`, `Real.exp_one_pow`
- `Real.log_lt_log`, `Real.log_sqrt`, `Real.log_rpow`, `Real.log_lt_log_iff`, `Real.log_pow`, `Real.log_two_lt_d9`, `Real.log_nonneg`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 clean.tex:1362-1388 (B_1 large, three-small-factors and its Lean note)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.4–R12.7).

#### Generality decision
- explicit positivity hypotheses; `1 ≤ m`, `0 < δ`, `δ < 1/m`, `1 < q₁`, `0 < r₁`, `1 ≤ A`.

**Progress**:
- 2026-10-12T19:35: proved


### [T071] Coefficient bound for remainders modulo a monic polynomial
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R12.8

#### Statement
```lean
theorem abs_coeff_modByMonic_le {f : Polynomial ℤ} (hf : f.Monic) {A : ℝ} (hA : 0 ≤ A)
    (hfA : ∀ i, |((f.coeff i : ℤ) : ℝ)| ≤ A) (P : Polynomial ℤ) {C : ℝ} (hC : 0 ≤ C)
    (hP : ∀ i, |((P.coeff i : ℤ) : ℝ)| ≤ C) {s : ℕ} (hs : P.natDegree ≤ s) (i : ℕ) :
    |(((P %ₘ f).coeff i : ℤ) : ℝ)| ≤ (1 + A) ^ (s + 1 - f.natDegree) * C := by sorry
```

#### Proof sketch
1. Strong induction on `s` generalising `P` and `C`. If `P.degree < f.degree` (in particular if `natDegree P < natDegree f`): `(Polynomial.modByMonic_eq_self_iff hf).2 this`, and the bound `(1+A)^k C ≥ C` (`le_mul_of_one_le_left`, `one_le_pow_of_one_le`).
2. Else `n := natDegree f ≤ natDegree P =: s' ≤ s`; `P' := P − C P.leadingCoeff * X^(s' − n) * f`; `degree P' < degree P` (`Polynomial.degree_sub_lt`: equal degrees `natDegree_C_mul_X_pow_mul`-style via `natDegree_mul`, `hf.natDegree_mul`, leading coefficients equal: `leadingCoeff_mul`, `hf.leadingCoeff`, `leadingCoeff_C_mul_X_pow`), so `natDegree P' ≤ s' − 1 ≤ s − 1`; coefficients of `P'`: `coeff_sub`, `coeff_C_mul`, `coeff_X_pow_mul'`/`Polynomial.coeff_mul_X_pow'`, `|coeff i P'| ≤ C + C·A = (1+A) C` (`abs_sub`, `abs_mul`, `hfA`, `hP`).
3. `P %ₘ f = P' %ₘ f` (`Polynomial.modByMonic_eq_of_dvd_sub hf ⟨_, by ring⟩`); apply the IH at `s − 1` with `C' := (1+A) C` and `(1+A)^{(s−1)+1−n} (1+A) C = (1+A)^{s+1−n} C` (`pow_succ`, `Nat.sub_add_cancel`-arithmetic with `n ≤ s`; `omega`).

#### Mathlib lemmas needed
- `Polynomial.modByMonic_eq_self_iff`, `Polynomial.modByMonic_eq_of_dvd_sub`, `Polynomial.degree_sub_lt`
- `Polynomial.natDegree_mul`, `Polynomial.Monic.natDegree_mul`, `Polynomial.leadingCoeff_mul`, `Polynomial.leadingCoeff_C_mul_X_pow`, `Polynomial.coeff_mul_X_pow'`, `Polynomial.coeff_C_mul`
- `abs_sub`, `abs_mul`, `le_mul_of_one_le_left`, `one_le_pow_of_one_le`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1453-1474
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.8).

#### Generality decision
- integer polynomials, real bounds `0 ≤ A`, `0 ≤ C`; any monic `f`.

**Progress**:
- 2026-10-12T19:45: proved; MainLemma.lean sorry-free, axioms standard


### [CLEANUP-27] Run /cleanup on Roth/MainLemma.lean
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T071
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/MainLemma.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:45: background agent (covers 27/28/29)
- 2026-10-12T19:49: agent cleanup of MainLemma.lean; signatures unchanged


### [T072] The family 𝒲 of box polynomials: finiteness and cardinality
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T010, CLEANUP-27
- **Parallel**: yes
- **Type**: def + lemma
- **Decomposition entries**: R12.9

#### Statement
```lean
def boxFamily {m : ℕ} (r : Fin m → ℕ) (B : ℕ) : Set (MvPolynomial (Fin m) ℤ) :=
  {W | (∀ j, degreeOf j W ≤ r j) ∧ ∀ d, 0 ≤ W.coeff d ∧ W.coeff d ≤ B}

theorem ncard_boxFamily {m : ℕ} (r : Fin m → ℕ) (B : ℕ) :
    (boxFamily r B).ncard = (B + 1) ^ ∏ j, (r j + 1) := by sorry

theorem boxFamily_finite {m : ℕ} (r : Fin m → ℕ) (B : ℕ) : (boxFamily r B).Finite := by sorry
```

#### Proof sketch
1. Build `e : boxFamily r B ≃ (box r → Finset.Icc (0:ℤ) B)` (or `→ Fin (B+1)`): forward `W ↦ fun d => ⟨coeff d W, …⟩`; inverse `c ↦ ∑ d ∈ box r, monomial d (c d)` (degree bounds from `mem_box` + `degreeOf_sum_le`/`degreeOf_monomial_le`; coefficient bounds from `coeff_sum`, `coeff_monomial`, `Finset.sum_ite_eq'`); left/right inverse by `MvPolynomial.ext` + `coeff_sum` + `coeff_monomial` + `Finset.sum_ite_eq'` and the fact that coefficients outside the box vanish (`degreeOf_le_iff`, `mem_box`).
2. `boxFamily_finite`: `Set.finite_coe_iff.1 (Finite.of_equiv _ e.symm)` (`Finite` instance on functions from a `Fintype` to a `Fintype`). `ncard_boxFamily`: `Set.ncard_eq_toFinset_card'`/`Nat.card_eq_fintype_card` + `Nat.card_congr e` + `Fintype.card_fun` + `card_box` + `Int.card_Icc`/`Fintype.card_fin`.

#### Mathlib lemmas needed
- `Set.ncard`, `Nat.card_congr`, `Nat.card_eq_fintype_card`, `Fintype.card_fun`, `Int.card_Icc`, `Finite.of_equiv`
- `MvPolynomial.coeff_sum`, `MvPolynomial.coeff_monomial`, `Finset.sum_ite_eq'`, `MvPolynomial.degreeOf_sum_le`
- (project) `mem_box`, `card_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1399-1418
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.9).

#### Generality decision
- `Fin m` variables; `B : ℕ`.

**Progress**:
- 2026-10-12T19:45: proved; MainLemma.lean sorry-free, axioms standard


### [T073] The pigeonhole counting inequality
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: CLEANUP-27
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R12.10

#### Statement
```lean
theorem pigeonhole_count {B : ℕ} (hB : 1 < B) {c : ℝ} (hc : 1 < c) {n D N : ℕ} (hN : 0 < N)
    (hD : c * n * D ≤ N / 2) :
    ((2 * ⌊(B : ℝ) ^ c⌋₊ + 1 : ℕ) : ℝ) ^ (n * D) < ((B : ℝ) + 1) ^ N := by sorry
```

#### Proof sketch
1. `(2⌊B^c⌋₊ + 1 : ℝ) ≤ 1 + 2 B^c` (`Nat.floor_le`, `Nat.cast_add`, `Nat.cast_mul`); `1 + 2B^c < (2(1+B))^c`: `(2(1+B))^c = 2^c (1+B)^c` (`Real.mul_rpow`), `2 ≤ 2^c` (`Real.self_le_rpow_of_one_le`? / `Real.rpow_le_rpow_of_exponent_le one_le_two hc.le` with `Real.rpow_one`), `1 + B^c ≤ (1+B)^c` (`Real.add_rpow_le_rpow_add zero_le_one (by positivity) hc.le` with `Real.one_rpow`; fallback described in decomposition R12.10), so `(2(1+B))^c ≥ 2(1 + B^c) > 1 + 2B^c`.
2. `(1+2B^c)^{nD} < (2(1+B))^{c nD}` when `nD ≥ 1` (`pow_lt_pow_left`, `Real.rpow_natCast`, `Real.rpow_mul`); if `nD = 0` both sides... handle by `≤` then strictness from the last step: `(2(1+B))^{cnD} ≤ (2(1+B))^{N/2}` (`Real.rpow_le_rpow_of_exponent_le`, base `≥ 1`, `hD`), and `(2(1+B))^{N/2} < (1+B)^N` since `((2(1+B))^{N/2})^2 = (2(1+B))^N < ((1+B)^2)^N = ((1+B)^N)^2` (`Real.rpow_natCast`, `Real.rpow_mul`, `pow_lt_pow_left` with `2(1+B) < (1+B)^2 ⟺ 1 < B` and `N ≥ 1`), then `pow_lt_pow_left`-converse/`abs_lt_abs`/`Real.sqrt_lt_sqrt` (`lt_of_pow_lt_pow_left`).

#### Mathlib lemmas needed
- `Nat.floor_le`, `Real.mul_rpow`, `Real.rpow_le_rpow_of_exponent_le`, `Real.add_rpow_le_rpow_add`, `Real.one_rpow`
- `Real.rpow_natCast`, `Real.rpow_mul`, `pow_lt_pow_left`, `lt_of_pow_lt_pow_left`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1479-1500
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.10).

#### Generality decision
- `1 < B`, `1 < c`, `0 < N` (added; the source's `D ≥ 1` is not needed), `c n D ≤ N/2`.

**Progress**:
- 2026-10-12T19:45: proved; MainLemma.lean sorry-free, axioms standard


### [T074] Pigeonhole: two distinct box polynomials with equal remainder tuples
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T028, T072, CLEANUP-27
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R12.11

#### Statement
```lean
theorem exists_ne_modByMonic_eq {m : ℕ} (r : Fin m → ℕ) (B : ℕ) {f : Polynomial ℤ} (hf : f.Monic)
    (J : Finset (Fin m →₀ ℕ)) (C : ℕ)
    (hC : ∀ W ∈ boxFamily r B, ∀ j ∈ J, ∀ i, |(diag (hasseDeriv j W) %ₘ f).coeff i| ≤ C)
    (hcount : ((2 * C + 1 : ℕ) : ℝ) ^ (f.natDegree * J.card) < ((B : ℝ) + 1) ^ ∏ j, (r j + 1)) :
    ∃ W' ∈ boxFamily r B, ∃ W'' ∈ boxFamily r B, W' ≠ W'' ∧
      ∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f := by sorry
```

#### Proof sketch
1. `s := (boxFamily_finite r B).toFinset`, `#s = (B+1)^N` (`Set.ncard_eq_toFinset_card'`, `ncard_boxFamily`). Codomain `t := Fintype.piFinset (fun _ : J × Fin f.natDegree => Finset.Icc (−(C:ℤ)) C)`, `#t = (2C+1)^(|J| · n)` (`Fintype.card_piFinset`, `Int.card_Icc`, `Finset.card_univ`, `Fintype.card_prod`, `Fintype.card_fin`, `Finset.prod_const`).
2. Map `F W := fun ⟨j, i⟩ => (diag (hasseDeriv j W) %ₘ f).coeff i`; maps-to by `hC` (`Finset.mem_Icc`, `abs_le`).
3. `#t < #s` from `hcount` (cast: `Nat.cast_lt`, `Nat.cast_pow`, `Nat.cast_add`, `mul_comm`); `Finset.exists_ne_map_eq_of_card_lt_of_maps_to` gives `W' ≠ W''` in `s` with `F W' = F W''`.
4. Equal remainders: `Polynomial.ext fun i => ?_`; for `i < natDegree f` read off `congrFun h ⟨j, ⟨i, _⟩⟩`; for `i ≥ natDegree f` both coefficients vanish (`Polynomial.degree_modByMonic_lt _ hf`, `Polynomial.coeff_eq_zero_of_degree_lt`, `Polynomial.natDegree_lt_iff_degree_lt`); `f ≠ 1`? — `degree_modByMonic_lt` needs `[Nontrivial ℤ]` only.

#### Mathlib lemmas needed
- `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`, `Set.Finite.toFinset`, `Set.ncard_eq_toFinset_card'`
- `Fintype.card_piFinset`, `Int.card_Icc`, `Fintype.card_prod`, `Finset.mem_Icc`, `abs_le`
- `Polynomial.degree_modByMonic_lt`, `Polynomial.coeff_eq_zero_of_degree_lt`
- (project) `ncard_boxFamily`, `boxFamily_finite`, `diag`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1479-1505 and Lean note clean.tex:1515-1521
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.11).

#### Generality decision
- any `J`, `C`, monic `f`; the count hypothesis as a real inequality.

**Progress**:
- 2026-10-12T19:45: proved; MainLemma.lean sorry-free, axioms standard


### [CLEANUP-28] Run /cleanup on Roth/MainLemma.lean
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T074
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/MainLemma.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:49: agent cleanup of MainLemma.lean; signatures unchanged


### [T075] Properties of W* = W' − W'' and the derivative witness
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T007, T010, T028, T041, T042, CLEANUP-28
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R12.12–R12.16

#### Statement
```lean
theorem sub_mem_RSet {m : ℕ} {r : Fin m → ℕ} {B : ℕ} {W' W'' : MvPolynomial (Fin m) ℤ}
    (h' : W' ∈ boxFamily r B) (h'' : W'' ∈ boxFamily r B) (hne : W' ≠ W'') :
    W' - W'' ∈ RSet (B : ℝ) r := by sorry

theorem eval_hasseDeriv_sub_eq_zero {m : ℕ} {f : Polynomial ℤ} {α : ℝ}
    (hfα : Polynomial.aeval α f = 0) {W' W'' : MvPolynomial (Fin m) ℤ} {j : Fin m →₀ ℕ}
    (h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f) :
    eval (fun _ => α) (hasseDeriv j (map (Int.castRingHom ℝ) (W' - W''))) = 0 := by sorry

theorem le_index_of_forall_eval_eq_zero {m : ℕ} {P : MvPolynomial (Fin m) ℝ} (hP : P ≠ 0)
    {r : Fin m → ℕ} (hd : ∀ j, degreeOf j P ≤ r j) (α : Fin m → ℝ) {c : ℝ}
    (hvan : ∀ d ∈ box r, weight r d ≤ c → eval α (hasseDeriv d P) = 0) : c ≤ index P α r := by
  sorry

theorem lem7_hyp_of_h32 {δ : ℝ} (hδ0 : 0 < δ) {m : ℕ} (hδm : δ < 1 / m) {q₁ : ℕ} {A α : ℝ}
    (hA : 1 ≤ A) (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) <
      δ ^ 2 * Real.log q₁) :
    (m : ℝ) * (2 * m + 1) / δ < Real.log q₁ := by sorry

theorem exists_hasseDeriv_eval_ne_zero {m : ℕ} {P : MvPolynomial (Fin m) ℝ} (hP : P ≠ 0)
    (α : Fin m → ℝ) (r : Fin m → ℕ) {c : ℝ} (hc : index P α r < c) :
    ∃ k : Fin m →₀ ℕ, weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 := by sorry
```

#### Proof sketch
1. `sub_mem_RSet`: `sub_ne_zero.2 hne`; `(degreeOf_sub_le _ _ _).trans (max_le (h'.1 j) (h''.1 j))`; `coeff_sub`, `Int.cast_sub`, `abs_sub_le_iff` with `0 ≤ c ≤ B` bounds (`Int.cast_le`, `Int.cast_nonneg`).
2. `eval_hasseDeriv_sub_eq_zero`: `map_sub`, `diag_sub`, `Polynomial.sub_modByMonic`, `sub_eq_zero.2 h`, `Polynomial.modByMonic_eq_zero_iff_dvd hf` ⇒ `f ∣ diag (hasseDeriv j (W' − W''))`; `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero this hfα`; rewrite `eval (fun _ => α) (hasseDeriv j (map (W'−W'')))` as `Polynomial.eval α (map (diag …))` (`hasseDeriv_map`, `eval_diag`, `Polynomial.aeval_def`, `Polynomial.eval_map`).
3. `le_index_of_forall_eval_eq_zero`: `(le_index_iff hP).2 fun d hd => ?_`; by cases `d ∈ box r`: `by_contra`/`not_le` + `hvan d hd' (le_of_lt …)` contradicts `hd`; else `∃ j, r j < d j` (`mem_box`, `not_forall`), so `hasseDeriv d P = 0` (`hasseDeriv_eq_zero_of_degreeOf_lt ((hd j).trans_lt …)`), contradiction with `hd` (`map_zero`, `eval_zero`).
4. `lem7_hyp_of_h32`: `log q₁ > (2m+1)/δ²` (drop the nonneg terms: `Real.log_nonneg`, `mul_nonneg`; `div_lt_iff`), and `(2m+1)/δ² ≥ m(2m+1)/δ` since `δ m < 1`... (`div_le_div_iff`, `nlinarith`).
5. `exists_hasseDeriv_eval_ne_zero`: `obtain ⟨d, hd, hw⟩ := exists_weight_eq_index hP α r; exact ⟨d, hw ▸ hc, hd⟩`.

#### Mathlib lemmas needed
- `MvPolynomial.degreeOf_sub_le`, `MvPolynomial.coeff_sub`, `abs_sub_le_iff`
- `Polynomial.sub_modByMonic`, `Polynomial.modByMonic_eq_zero_iff_dvd`, `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero`, `Polynomial.eval_map`, `Polynomial.aeval_def`
- `Real.log_nonneg`, `div_lt_iff`, `div_le_div_iff`
- (project) `diag_sub`, `eval_diag`, `hasseDeriv_map`, `le_index_iff`, `mem_box`, `hasseDeriv_eq_zero_of_degreeOf_lt`, `exists_weight_eq_index`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 proof of Lemma 9, clean.tex:1501-1536; Lemma lem7-satisfied clean.tex:1330-1336
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.12–R12.16).

#### Generality decision
- `Fin m` variables as in Lemma 9; real evaluation point `α`.

**Progress**:
- 2026-10-12T19:37: proved


### [T076] Lemma 9: Roth's main lemma
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T027, T029, T040, T058, T068, T069, T070, T071, T073, T074, T075, CLEANUP-28
- **Parallel**: no
- **Type**: theorem
- **Decomposition entries**: R12.17

#### Statement
```lean
theorem main_lemma {α : ℝ} {f : Polynomial ℤ} (hf : f.Monic) (hfα : Polynomial.aeval α f = 0)
    (hdeg : 2 ≤ f.natDegree) {A : ℝ} (hA1 : 1 ≤ A) (hA : ∀ i, |((f.coeff i : ℤ) : ℝ)| ≤ A) {m : ℕ}
    [NeZero m] (hm : 16 * f.natDegree ^ 2 < m) {δ : ℝ} (hδ0 : 0 < δ) (hδm : δ < 1 / m)
    (h30 : eta δ m + 2 * (1 + 3 * δ) * f.natDegree * √(m : ℝ) < m / 2) {r : Fin m → ℕ}
    (hr0 : ∀ j, 0 < r j) (h31a : ∀ j, 10 / δ < r j)
    (h31b : ∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) {q : Fin m → ℕ}
    (hq0 : ∀ j, 0 < q j) (hq1 : 1 < q 0)
    (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) <
      δ ^ 2 * Real.log (q 0))
    (h33 : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) {h : Fin m → ℤ}
    (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    ∃ Q : MvPolynomial (Fin m) ℤ, Q ≠ 0 ∧ (∀ j, degreeOf j Q ≤ r j) ∧
      gam δ f.natDegree m - eta δ m ≤ index (map (Int.castRingHom ℝ) Q) (fun _ => α) r ∧
      eval (fun j => (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0 ∧
      ∀ i : Fin m →₀ ℕ, |eval (fun _ => α) (hasseDeriv i (map (Int.castRingHom ℝ) Q))| <
        (B₁ δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ) := by sorry
```

#### Proof sketch
1. Constants: `n := f.natDegree`, `N := ∏ (r j + 1)`, `X := q 0 ^ (δ r 0)`, `B := B₁ δ (q 0) (r 0)`; `η < γ` (`eta_lt_gam_iff`); `4 < X` (`four_lt_rpow` with the first term of `h32`); `√X < B ≤ X` (`sqrt_lt_floor`), `1 < B`; `three_small_factors` ⇒ `2^{m r 0}, (1+A)^{m r 0}, (1+|α|)^{m r 0} < B^δ`. Antitonicity of `r` from `h31b`/`δ < 1` ⇒ `∀ j, r j ≤ r 0` ⇒ `∑ r j ≤ m r 0` and `N ≤ 2^{∑ r j}` (`Nat.lt_two_pow_self`, `Finset.prod_le_prod'`, `Finset.prod_pow_eq_pow_sum`).
2. `J := (box r).filter (fun d => weight r d ≤ γ)`; `|J| ≤ 2√m/λ · N` (`card_filter_weight_le` with `λ > 0`, `γ = (m − λ)/2`); `D := |J|`.
3. Remainder bound: for `W ∈ boxFamily r B`, `j ∈ J`: `|coeff (hasseDeriv j W)| ≤ 2^{∑ r} B ≤ 2^{m r 0} B < B^{1+δ}` (`abs_coeff_hasseDeriv_le`, `Real.rpow_add`, `Real.rpow_one`); `|coeff (diag …)| ≤ N 2^{m r 0} B < B^{1+2δ}` (`abs_coeff_diag_le`, `card_le_card_box`); `natDegree (diag …) ≤ ∑ r ≤ m r 0` (`natDegree_diag_le`); `|coeff ((diag …) %ₘ f)| ≤ (1+A)^{m r 0 + 1 − n} B^{1+2δ} ≤ (1+A)^{m r 0} B^{1+2δ} < B^{1+3δ}` (`abs_coeff_modByMonic_le`, `pow_le_pow_right`); set `C := ⌊B^{1+3δ}⌋₊`, so integer coefficients satisfy `|c| ≤ C` (`Nat.le_floor`, `Int.natAbs`/`Int.cast_abs`).
4. Count: `c := 1 + 3δ > 1`; `c n D ≤ N/2` from `D ≤ 2√m N/λ` and `λ = 4(1+3δ) n √m` (`div_le_iff`, `field_simp`, `nlinarith`/`ring`); `pigeonhole_count hB hc (N > 0) this`; `exists_ne_modByMonic_eq` ⇒ `W', W''`.
5. `W* := W' − W''`; `W* ∈ RSet B r` (`sub_mem_RSet`), hence `∈ RSet X r` (`B ≤ X`); `γ ≤ index (map W*) (fun _ => α) r` (`le_index_of_forall_eval_eq_zero` with `eval_hasseDeriv_sub_eq_zero` for `j ∈ J`, `map_ne_zero`).
6. Lemma 7: `obtain ⟨n', rfl⟩ : ∃ n', m = n' + 1` (`Nat.exists_eq_succ_of_ne_zero (NeZero.ne m)`); `Θ_lt n' hδ0 (by …) hr0 (h31a _) (fun i => h31b _ _ (by simp)) hq0 (lem7_hyp_of_h32 …) h33 : Θ X q r < η`; `index_le_Θ hr0 hW* hh : index (map W*) (h/q) r ≤ Θ`; `exists_hasseDeriv_eval_ne_zero` ⇒ `k` with `weight r k < η`, `eval (h/q) (hasseDeriv k (map W*)) ≠ 0`.
7. `Q := hasseDeriv k W*`; `map Q = hasseDeriv k (map W*)` (`hasseDeriv_map`); `Q ≠ 0` (evaluation nonzero), `degreeOf j Q ≤ r j` (`degreeOf_hasseDeriv_le`), (1): `index_hasseDeriv_ge` + `weight r k < η` + `linarith`, (2) ✓, (3): `|coeff Q| ≤ 2^{m r 0} B < B^{1+δ}` (`abs_coeff_hasseDeriv_le`), `|coeff (hasseDeriv i Q)| ≤ 2^{m r 0} 2^{m r 0} B < B^{1+2δ}`, then `abs_eval_le` and `∏ (1+|α|)^{r j} = (1+|α|)^{∑ r} ≤ (1+|α|)^{m r 0} < B^δ` (`Finset.prod_pow_eq_pow_sum`, `pow_le_pow_right`), product of the strict bounds (`mul_lt_mul''`, positivity), `Real.rpow_add`.

#### Mathlib lemmas needed
- `Nat.exists_eq_succ_of_ne_zero`, `NeZero.ne`, `Nat.lt_two_pow_self`, `Finset.prod_le_prod'`, `Finset.prod_pow_eq_pow_sum`, `pow_le_pow_right`
- `Real.rpow_add`, `Real.rpow_one`, `Nat.le_floor`, `mul_lt_mul''`, `div_le_iff`
- (project) `eta_lt_gam_iff`, `four_lt_rpow`, `sqrt_lt_floor`, `three_small_factors`, `card_filter_weight_le`, `abs_coeff_hasseDeriv_le`, `abs_coeff_diag_le`, `natDegree_diag_le`, `abs_coeff_modByMonic_le`, `pigeonhole_count`, `exists_ne_modByMonic_eq`, `sub_mem_RSet`, `le_index_of_forall_eval_eq_zero`, `eval_hasseDeriv_sub_eq_zero`, `Θ_lt`, `index_le_Θ`, `lem7_hyp_of_h32`, `exists_hasseDeriv_eval_ne_zero`, `index_hasseDeriv_ge`, `degreeOf_hasseDeriv_le`, `abs_eval_le`, `hasseDeriv_map`, `card_le_card_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 Lemma 9 (roth:lem9), clean.tex:1393-1562
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R12.17).

#### Generality decision
- `Fin m` with `[NeZero m]`; hypotheses (29)–(33) verbatim with the chain (31) in consecutive-index form; `A` any real `≥ 1` bounding the coefficients of `f`.

**Progress**:
- 2026-10-12T19:45: proved; MainLemma.lean sorry-free, axioms standard


### [CLEANUP-29] Run /cleanup on Roth/MainLemma.lean
- **Status**: done
- **File**: Roth/MainLemma.lean
- **Depends on**: T076
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/MainLemma.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:49: agent cleanup of MainLemma.lean; signatures unchanged


### [T077] Algebraic integers from algebraic numbers; finiteness and tail estimates
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: none
- **Parallel**: yes
- **Type**: def + lemma
- **Decomposition entries**: R13.1–R13.4

#### Statement
```lean
def approxSet (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}

theorem exists_nat_mul_isIntegral {α : ℝ} (hα : IsAlgebraic ℚ α) :
    ∃ M : ℕ, 0 < M ∧ IsIntegral ℤ ((M : ℝ) * α) := by sorry

theorem approxSet_den_le_finite (α κ : ℝ) (Q₀ : ℕ) :
    {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite := by sorry

theorem eventually_div_rpow_lt {M : ℝ} (hM : 0 < M) {κ κ' : ℝ} (hκ : κ' < κ) :
    ∃ Q₀ : ℕ, ∀ q : ℕ, Q₀ < q → M / (q : ℝ) ^ κ < 1 / (q : ℝ) ^ κ' := by sorry
```

#### Proof sketch
1. `exists_nat_mul_isIntegral`: `(IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).2 hα : IsAlgebraic ℤ α`; `.exists_integral_multiple` gives `y ≠ 0`, `IsIntegral ℤ (y • α)`; `M := y.natAbs`, `0 < M` (`Int.natAbs_pos`); `(M : ℝ) * α = ± (y • α)` (`Int.natAbs_eq`/`Int.cast_natAbs`, `zsmul_eq_mul`, `Int.cast_abs`, `abs_eq`), `IsIntegral.neg` in the negative case.
2. `approxSet_den_le_finite`: contained in `(Finset.Icc (−K) K ×ˢ Finset.Icc 1 Q₀ : Finset (ℤ × ℕ))` with `K := ⌈Q₀ * (|α| + max 1 ((Q₀:ℝ) ^ (−κ)))⌉`: for `(h, q)` in the set, `|h/q| ≤ |α| + 1/q^κ` (`abs_sub_abs_le_abs_sub`), and `1/q^κ = q^{−κ} ≤ max 1 Q₀^{−κ}` (cases `κ ≥ 0`: `Real.rpow_le_one`/`≤ 1`; `κ < 0`: `Real.rpow_le_rpow_of_exponent_nonpos`-type monotonicity in the base for `q ≤ Q₀`), so `|h| ≤ q(…) ≤ K` (`Int.cast_abs`, `Int.le_ceil`); `Set.Finite.subset (Finset.finite_toSet _)`.
3. `eventually_div_rpow_lt`: `Q₀ := ⌈M ^ (1/(κ − κ'))⌉₊`; for `q > Q₀` (so `q ≥ 1` and `(q:ℝ) > M^{1/(κ−κ')}`): `M < q^{κ−κ'}` (`Real.rpow_lt_rpow` + `Real.rpow_natCast`-free `← Real.rpow_mul`, `div_mul_cancel₀`, `Real.rpow_one`; `Nat.le_ceil`), then `M/q^κ < 1/q^{κ'} ⟺ M q^{κ'} < q^κ = q^{κ'} q^{κ−κ'}` (`Real.rpow_add`, `div_lt_div_iff`, `Real.rpow_pos_of_pos`).

#### Mathlib lemmas needed
- `IsFractionRing.isAlgebraic_iff`, `IsAlgebraic.exists_integral_multiple`, `IsIntegral.neg`, `Int.natAbs_pos`, `zsmul_eq_mul`
- `Set.Finite.subset`, `Finset.finite_toSet`, `Finset.mem_product`, `Finset.mem_Icc`, `Int.le_ceil`, `abs_sub_abs_le_abs_sub`
- `Real.rpow_lt_rpow`, `Real.rpow_mul`, `Real.rpow_add`, `Real.rpow_pos_of_pos`, `Nat.le_ceil`, `div_lt_div_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 clean.tex:1139-1177
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.1–R13.4).

#### Generality decision
- `κ` arbitrary real in `approxSet_den_le_finite`; `0 < M`, `κ' < κ` in the tail estimate.

**Progress**:
- 2026-10-12T19:48: proved


### [T078] Reduction to algebraic integers; a monic equation of degree ≥ 2
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T077
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R13.5, R13.6

#### Statement
```lean
theorem reduction {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ} (hκ : 2 < κ)
    (hinf : (approxSet α κ).Infinite) :
    ∃ (α' κ' : ℝ), Irrational α' ∧ IsIntegral ℤ α' ∧ 2 < κ' ∧ (approxSet α' κ').Infinite := by
  sorry

theorem exists_monic_aeval_eq_zero {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) :
    ∃ f : Polynomial ℤ, f.Monic ∧ Polynomial.aeval α f = 0 ∧ 2 ≤ f.natDegree := by sorry
```

#### Proof sketch
1. `reduction`: `M` from `exists_nat_mul_isIntegral`; `κ' := (κ + 2)/2` (`2 < κ'`, `κ' < κ`); `Q₀` from `eventually_div_rpow_lt (M > 0)`; `S := approxSet α κ \ {hq | hq.2 ≤ Q₀}` is infinite (`Set.Infinite.diff hinf (approxSet_den_le_finite …)`); `g : ℤ × ℕ → ℤ × ℕ := fun hq => (M * hq.1, hq.2)` is injective (`Prod.ext_iff`, `mul_right_injective₀`), and `g '' S ⊆ approxSet (M α) κ'`: `|Mα − (M h)/q| = M |α − h/q| < M/q^κ < 1/q^{κ'}` (`Nat.cast_mul`, `mul_div_assoc`, `abs_mul`, `Nat.abs_cast`, `mul_lt_mul_of_pos_left`); `Set.Infinite.image`/`Set.Infinite.mono`; `Irrational (M * α)` from `hα.natCast_mul`? (`Irrational.natCast_mul`/`irrational_natCast_mul_iff`, `M ≠ 0`); `IsIntegral` from step 1.
2. `exists_monic_aeval_eq_zero`: `obtain ⟨f, hf, hf0⟩ := hint` (`IsIntegral` unfolds to `∃ p, Monic p ∧ eval₂ _ α p = 0`; `Polynomial.aeval_def`); `2 ≤ natDegree f`: not `0` (`Polynomial.Monic.natDegree_eq_zero_iff_eq_one` ⇒ `f = 1` ⇒ `aeval = 1 ≠ 0`), not `1` (`Polynomial.Monic.natDegree_eq_one_iff`?/`Polynomial.eq_X_add_C_of_natDegree_le_one` + monic ⇒ `f = X + C a` ⇒ `α = −a` (`aeval_add`, `aeval_X`, `aeval_C`, `eq_neg_of_add_eq_zero_left`) ⇒ `hα (−a : ℤ)` contradiction via `Irrational.ne_int`/`irrational_iff_ne_rational`).

#### Mathlib lemmas needed
- `Set.Infinite.diff`, `Set.Infinite.image`, `Set.Infinite.mono`, `Prod.ext_iff`, `mul_right_injective₀`
- `Irrational.natCast_mul` (or `irrational_natCast_mul_iff`), `Irrational.ne_int`
- `Polynomial.Monic.natDegree_eq_zero_iff_eq_one`, `Polynomial.eq_X_add_C_of_natDegree_le_one`, `Polynomial.aeval_def`
- (project) `exists_nat_mul_isIntegral`, `eventually_div_rpow_lt`, `approxSet_den_le_finite`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 clean.tex:1145-1199
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.5, R13.6).

#### Generality decision
- real irrational algebraic `α`, `κ > 2`.

**Progress**:
- 2026-10-12T19:48: proved


### [T079] Reduced approximations with arbitrarily large denominators
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T077
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R13.7

#### Statement
```lean
theorem exists_reduced_approx {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) :
    ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ) := by sorry
```

#### Proof sketch
1. Define the reduction map `ρ : ℤ × ℕ → ℤ × ℕ`, `ρ (h, q) := ((h : ℚ)/q).num, ((h : ℚ)/q).den)` and show `ρ '' approxSet α κ ⊆ approxSet α κ ∩ {reduced}`: `b := den > 0` (`Rat.den_pos`), `b ∣ q` hence `b ≤ q` (`Rat.den_dvd`, `Nat.le_of_dvd`), `(num : ℝ)/den = h/q` (`Rat.num_div_den`, `Rat.cast_div`, `Rat.cast_intCast`, `Rat.cast_natCast`), `1/q^κ ≤ 1/b^κ` (`Real.rpow_le_rpow` with `κ ≥ 0`, `one_div_le_one_div_of_le`); coprimality: `Rat.reduced` (`num.natAbs.Coprime den`) ⇒ `IsCoprime num (den : ℤ)` (`Int.isCoprime_iff_gcd_eq_one`, `Int.gcd_eq_natAbs`, `Nat.Coprime`).
2. The image is infinite: fibres of `ρ` on `approxSet α κ` are finite — for a fixed reduced value `x = a/b`, `ε := |α − x| > 0` (irrationality: `Irrational.ne_rat`-type `sub_ne_zero`), and `(h,q)` in the fibre has `ε < 1/q^κ`, i.e. `q^κ < 1/ε`, bounding `q` (`Real.rpow_lt_rpow_left_iff`-converse: `q < (1/ε)^{1/κ}`), then `h` determined by `q` (`h = x * q`); `Set.Finite.subset` of a finite box. If `ρ '' S` were finite, `S ⊆ ⋃_{y ∈ ρ '' S} fibre y` would be finite (`Set.Finite.biUnion`), contradiction (`Set.Infinite`).
3. Remove bounded denominators: `approxSet_den_le_finite α κ Q₀`; `(ρ '' S).Infinite.diff this` is nonempty (`Set.Infinite.nonempty`), giving the required pair.

#### Mathlib lemmas needed
- `Rat.num_div_den`, `Rat.den_pos`, `Rat.den_dvd`, `Rat.reduced`, `Rat.cast_div`, `Int.isCoprime_iff_gcd_eq_one`, `Int.gcd_eq_natAbs`
- `Real.rpow_le_rpow`, `one_div_le_one_div_of_le`, `Real.rpow_lt_rpow_left_iff`
- `Set.Finite.biUnion`, `Set.Infinite.diff`, `Set.Infinite.nonempty`, `Set.Finite.subset`
- (project) `approxSet_den_le_finite`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §7 first paragraph, clean.tex:1578-1590
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.7).

#### Generality decision
- `Irrational α`, `0 < κ` (needed for `b ≤ q ⇒ q^{−κ} ≤ b^{−κ}`).

**Progress**:
- 2026-10-12T19:48: proved


### [CLEANUP-30] Run /cleanup on Roth/Main.lean
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T079
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Main.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T19:54: background agent (covers 30/31/32)
- 2026-10-12T20:04: agent cleanup of Main.lean; signatures unchanged


### [T080] Choice of m and δ
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T069, CLEANUP-30
- **Parallel**: yes
- **Type**: lemma
- **Decomposition entries**: R13.8, R13.9

#### Statement
```lean
theorem exists_m {n : ℕ} (hn : 0 < n) {κ : ℝ} (hκ : 2 < κ) :
    ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧ 2 * m / (m - 4 * n * √(m : ℝ)) < κ := by
  sorry

theorem exists_delta {n m : ℕ} (hn : 0 < n) (hm : 16 * n ^ 2 < m) {κ : ℝ}
    (h47 : 4 * n * √(m : ℝ) < m)
    (h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) :
    ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧
      (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ := by sorry
```

#### Proof sketch
1. `exists_m`: `s := ⌈4 κ n / (κ − 2)⌉₊ + 4 n + 1`, `m := s^2`; `√m = s` (`Real.sqrt_sq`, `Nat.cast_pow`); `16 n² < s²` and `4 n s < s²` from `s > 4n`; `2 s²/(s² − 4 n s) = 2s/(s − 4n) < κ ⟺ 2s < κ(s − 4n) ⟺ s(κ − 2) > 4κn` (`div_lt_iff`, `Nat.le_ceil`, `nlinarith`).
2. `exists_delta`: `E := κ (m − 4n√m)/2 − m > 0` (⟺ `h47'` via `div_lt_iff`); `δ₀` from `exists_delta_bound hn hm`; `δ := (1/2) * min δ₀ (min (E/(12 m)) (min (E/(18 κ n √m)) ((E/(3 κ 10^m))^(2^m : ℕ))))`, positive; `0 < δ < δ₀` gives (29),(30); for (49): `γ − η > 0` (`eta_lt_gam_iff`), and `m(1+4δ) < κ(γ − η) ⟺ 4mδ + 6κnδ√m + κη < E` (unfold `gam`, `lam`; `field_simp`/`ring_nf`), each term `< E/3` (`eta`: `Real.rpow_lt_rpow` as in `exists_delta_bound`; the other two by `lt_div_iff`); `lt_div_iff`.

#### Mathlib lemmas needed
- `Real.sqrt_sq`, `Nat.le_ceil`, `div_lt_iff`, `lt_div_iff`, `lt_min_iff`
- `Real.rpow_lt_rpow`, `Real.rpow_natCast`, `Real.rpow_mul`
- (project) `exists_delta_bound`, `eta_lt_gam_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §7 clean.tex:1592-1607 (eqs. (47)–(49))
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.8, R13.9).

#### Generality decision
- `0 < n`, `2 < κ`; explicit thresholds replace the source's limit argument (same device as the source's Lemma m-δ).

**Progress**:
- 2026-10-12T19:50: proved


### [T081] Choice of the approximants q_1, …, q_m and of the degrees r_1, …, r_m
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T079, CLEANUP-30
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R13.10, R13.11

#### Statement
```lean
theorem exists_approximants {α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ)
    (hinf : (approxSet α κ).Infinite) (m : ℕ) [NeZero m] {δ : ℝ} (hδ : 0 < δ) (L : ℝ) :
    ∃ (h : Fin m → ℤ) (q : Fin m → ℕ), (∀ j, (h j, q j) ∈ approxSet α κ) ∧
      (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ (∀ j, 1 < q j) ∧ L < Real.log (q 0) ∧
      ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j) := by sorry

theorem exists_degrees {m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ < 1) {q : Fin m → ℕ}
    (hq : ∀ j, 1 < q j)
    (h50 : ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) < Real.log (q j)) :
    ∃ r : Fin m → ℕ, (∀ j, 0 < r j) ∧ (∀ j, 10 / δ < r j) ∧
      (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) ∧
      (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧
      ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0)) := by sorry
```

#### Proof sketch
1. `exists_approximants`: define `s : ℕ → ℤ × ℕ` by recursion: `s 0 :=` the pair from `exists_reduced_approx hα hκ hinf (max ⌈exp L⌉₊ 1)` (so `q > exp L ≥ 1`, i.e. `L < log q`: `Real.lt_log_iff_exp_lt`, and `q > 1`); `s (i+1) :=` the pair from `exists_reduced_approx … ⌈(q_i : ℝ) ^ (2/δ)⌉₊` (so `q_{i+1} > q_i^{2/δ}`, hence `log q_{i+1} > (2/δ) log q_i`: `Real.log_lt_log`, `Real.log_rpow`, `Nat.le_ceil`); restrict to `Fin m` (`h j := (s j).1`, `q j := (s j).2`); the consecutive-index chain follows from the recursion (`i.val + 1 = j.val`).
2. `exists_degrees`: `r 0 := ⌈10 log q_last / (δ log q 0)⌉₊ + 1` (`q_last` the maximum, i.e. index `⟨m−1, _⟩`; or any `j` — use `Finset.univ.sup' (fun j => log (q j))`), `r j := ⌈r 0 log q 0 / log q j⌉₊` for `j ≠ 0` (`Function.update`/`if j = 0`). Positivity: `Nat.ceil_pos`/`Nat.le_ceil` with positive arguments (`Real.log_pos`). (33): `Nat.le_ceil` ⇒ `r 0 log q 0 / log q j ≤ r j` ⇒ `r 0 log q 0 ≤ r j log q j` (`div_le_iff`). (53): `r j < r 0 log q 0 / log q j + 1` (`Nat.ceil_lt_add_one`) ⇒ `r j log q j < r 0 log q 0 + log q j ≤ r 0 log q 0 + log q_max < (1 + δ/10) r 0 log q 0` (from (51): `10 log q_max/(δ log q 0) < r 0`). (31a): `r j ≥ r 0 log q 0/log q j ≥ r 0 log q 0 / log q_max > 10/δ`. (31b): for consecutive `i, j`: `r i ≥ r 0 log q 0 / log q i` and `r j < (1 + δ/10) r 0 log q 0 / log q j`, so `r i / r j > log q j / ((1+δ/10) log q i) > (2/δ)/(1+δ/10) > 1/δ` (`h50`, `2 > 1 + δ/10`); rearrange to `r j / δ < r i` (`div_lt_iff`, `nlinarith`).

#### Mathlib lemmas needed
- `Real.lt_log_iff_exp_lt`, `Real.log_lt_log`, `Real.log_rpow`, `Real.log_pos`, `Nat.le_ceil`, `Nat.ceil_lt_add_one`
- `div_le_iff`, `div_lt_iff`, `lt_div_iff`, `Finset.univ.sup'`/`Finset.le_sup'`
- (project) `exists_reduced_approx`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §7 clean.tex:1608-1642 (eqs. (50)–(53), (31), (33) and the Lean note)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.10, R13.11).

#### Generality decision
- `[NeZero m]`; `0 < δ < 1`; `q j > 1`.

**Progress**:
- 2026-10-12T19:50: proved


### [T082] Denominator clearing (54) and the Taylor upper bound
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T023, T041, CLEANUP-30
- **Parallel**: yes
- **Type**: theorem
- **Decomposition entries**: R13.12, R13.13

#### Statement
```lean
theorem one_le_prod_pow_mul_abs_eval {m : ℕ} (Q : MvPolynomial (Fin m) ℤ) {r : Fin m → ℕ}
    (hQ : ∀ j, degreeOf j Q ≤ r j) (h : Fin m → ℤ) {q : Fin m → ℕ} (hq : ∀ j, 0 < q j)
    (hne : eval (fun j => (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : ℝ) ^ r j) * |eval (fun j => (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| := by
  sorry

theorem abs_eval_lt_of_le_index {m : ℕ} [NeZero m] {Q : MvPolynomial (Fin m) ℝ} (hQ : Q ≠ 0)
    {r : Fin m → ℕ} (hr : ∀ j, 0 < r j) (hd : ∀ j, degreeOf j Q ≤ r j) {α : ℝ} {c : ℝ} (hc : 0 < c)
    (hidx : c ≤ index Q (fun _ => α) r) {h : Fin m → ℤ} {q : Fin m → ℕ} (hq : ∀ j, 0 < q j)
    {κ : ℝ} (hκ : 0 < κ) (happ : ∀ j, |α - (h j : ℝ) / q j| < 1 / (q j : ℝ) ^ κ)
    (hqr : ∀ j, (q 0 : ℝ) ^ ((r 0 : ℝ) / r j) ≤ q j) {C : ℝ}
    (hC : ∀ i : Fin m →₀ ℕ, |eval (fun _ => α) (hasseDeriv i Q)| < C) :
    |eval (fun j => (h j : ℝ) / q j) Q| <
      (∏ j, ((r j : ℝ) + 1)) * C * (q 0 : ℝ) ^ (-(r 0 : ℝ) * c * κ) := by sorry
```

#### Proof sketch
1. `one_le_prod_pow_mul_abs_eval`: show `(∏ q_j^{r_j}) * eval (h/q) (map Q) = ((z : ℤ) : ℝ)` with `z := ∑_{d ∈ supp} coeff d Q * ∏ j, h_j^{d_j} * q_j^{r_j − d_j}`: `MvPolynomial.eval_eq`/`as_sum`, `map_sum`, `eval_monomial`, `Finset.mul_sum`, per term `∏ q_j^{r_j} * ∏ (h_j/q_j)^{d_j} = ∏ h_j^{d_j} q_j^{r_j − d_j}` (`Finset.prod_mul_distrib`, `div_pow`, `pow_sub₀`-free: `q_j^{r_j} = q_j^{d_j} q_j^{r_j−d_j}` by `pow_add`/`Nat.add_sub_cancel'` with `d_j ≤ r_j` from `degreeOf_le_iff`, `mul_div_cancel_left₀`), `Int.cast_sum`, `Int.cast_mul`, `Int.cast_pow`, `Int.cast_natCast`; `z ≠ 0` (its cast is nonzero), `Int.one_le_abs`, `abs_mul`, `abs_of_pos` (`∏ q^r > 0`).
2. `abs_eval_lt_of_le_index`: `eval_eq_sum_box α' x r Q hd` with `α' := fun _ => α`, `x := h/q`; `Finset.abs_sum_le_sum_abs`; for `d ∈ box r`: if `weight r d < c` then `eval α' (hasseDeriv d Q) = 0` (contrapositive of `index_le_weight` with `hidx`), term `= 0`; else `|∏ (h_j/q_j − α)^{d_j}| = ∏ |h_j/q_j − α|^{d_j} ≤ ∏ (q_j^{−κ})^{d_j}` (`abs_prod`, `abs_pow`, `pow_le_pow_left`, `happ`, `one_div`, `Real.rpow_neg`) `≤ ∏ (q_0^{r_0/r_j})^{−κ d_j}` (`Real.rpow_le_rpow_left_iff`-monotone in the base for negative exponent: `Real.rpow_le_rpow_of_nonpos`? / use `Real.inv_rpow` and `Real.rpow_le_rpow` with `hqr`) `= q_0^{−κ r_0 ∑ d_j/r_j} = q_0^{−κ r_0 weight r d} ≤ q_0^{−κ r_0 c}` (`Real.rpow_natCast`, `← Real.rpow_mul`, `Finset.prod` of `rpow` = `rpow` of sum (`Real.rpow_sum_of_pos`), `Real.rpow_le_rpow_of_exponent_le` with `1 ≤ q 0`, `weight r d ≥ c`, `κ > 0`); so `|term| ≤ |eval α' (hasseDeriv d Q)| · q_0^{−r_0 c κ} < C q_0^{…}` when the derivative value is nonzero (`mul_lt_mul_of_pos_right (hC d)`), and `= 0 < C q_0^{…}` otherwise; `Finset.sum_lt_sum_of_nonempty` (box nonempty: `0 ∈ box`) or `Finset.sum_lt_sum` with one strict term, `Finset.sum_const`, `card_box`.

#### Mathlib lemmas needed
- `MvPolynomial.eval_monomial`, `Finset.prod_mul_distrib`, `div_pow`, `pow_add`, `mul_div_cancel_left₀`, `Int.cast_sum`, `Int.one_le_abs`
- `Finset.abs_sum_le_sum_abs`, `abs_prod`, `abs_pow`, `pow_le_pow_left`, `Real.rpow_neg`, `Real.rpow_natCast`, `Real.rpow_mul`, `Real.rpow_sum_of_pos`, `Real.rpow_le_rpow_of_exponent_le`, `Finset.sum_lt_sum`
- (project) `eval_eq_sum_box`, `index_le_weight`, `card_box`, `mem_box`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §7 clean.tex:1647-1675 (eq. (54) and the Taylor estimate)
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.12, R13.13).

#### Generality decision
- `[NeZero m]`; general real polynomial `Q` with a lower bound `c > 0` on its index and a bound `C` on its derivatives (the roles of `γ − η` and `B₁^{1+3δ}`).

**Progress**:
- 2026-10-12T19:51: proved


### [CLEANUP-31] Run /cleanup on Roth/Main.lean
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T082
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: cadence cleanup (3 proof tickets done on this file). Run `/cleanup` on `Roth/Main.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T20:04: agent cleanup of Main.lean; signatures unchanged


### [T083] Roth's theorem for real irrational algebraic integers
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T076, T078, T079, T080, T081, T082, T070, CLEANUP-31
- **Parallel**: no
- **Type**: theorem
- **Decomposition entries**: R13.14

#### Statement
```lean
theorem roth_of_isIntegral {α : ℝ} (hα : Irrational α) (hint : IsIntegral ℤ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by sorry
```

#### Proof sketch
1. `by_contra hκ; push_neg at hκ` (`2 < κ`). `exists_monic_aeval_eq_zero hα hint` ⇒ `f, n := natDegree f ≥ 2`; `A := max 1 (f.support.sup fun i => |f.coeff i|)` cast to `ℝ` (`1 ≤ A`, `|f.coeff i| ≤ A` by `Finset.le_sup`).
2. `exists_m (by omega : 0 < n) hκ` ⇒ `m` with `16 n² < m`, `4n√m < m`, (47); `haveI : NeZero m`; `exists_delta` ⇒ `δ` with (29), (30), (49).
3. `L := (2m + 1 + 2m log(1+A) + 2m log(1+|α|)) / δ²`; `exists_approximants hα (by linarith) hinf m hδ0 L` ⇒ `h, q` with membership in `approxSet`, coprimality, `q j > 1`, `L < log (q 0)` (hence (32): `lt_div_iff`), (50).
4. `exists_degrees hδ0 hδ1 hq h50` ⇒ `r` with (31a), (31b), (33), (53).
5. `main_lemma hf hfα hn hA1 hA hm hδ0 hδm h30 hr0 h31a h31b hq0 hq1 h32 h33 hh` ⇒ `Q` with (1)–(3).
6. Lower bound: `one_le_prod_pow_mul_abs_eval Q hQd h hq0 hQne`; and `∏ q_j^{r_j} < q_0^{m r_0 (1+δ)}` (take logs: `Real.log_prod`, `Real.log_pow`, `∑ r_j log q_j < m (1 + δ/10) r_0 log q_0 ≤ m(1+δ) r_0 log q_0` from (53) and `Finset.sum_lt_sum_of_nonempty`; `Real.exp_lt_exp`, `Real.rpow_def_of_pos`), hence `q_0^{−m r_0 (1+δ)} < |Q(h/q)|` (`Real.rpow_neg`, `div_lt_iff`).
7. Upper bound: `abs_eval_lt_of_le_index (map Q ≠ 0) hr0 hQd' (γ−η > 0) hidx hq0 (by linarith) happ hqr hC` with `hqr j : q_0^{r_0/r_j} ≤ q_j` from (33) (`Real.rpow_le_iff_le_log`/`Real.log_rpow`, `div_mul_eq_mul_div`, `div_le_iff`) and `hC := (3)`; then `∏(r_j+1) ≤ 2^{∑ r_j} ≤ 2^{m r_0} < B₁^δ` (`three_small_factors`; antitone `r`) and `B₁ ≤ q_0^{δ r_0}` (`sqrt_lt_floor`), so `|Q(h/q)| < B₁^{δ} B₁^{1+3δ} q_0^{−r_0(γ−η)κ} ≤ q_0^{δ r_0 (1+4δ)} q_0^{−r_0(γ−η)κ}` (`Real.rpow_add`, `Real.rpow_le_rpow`, `Real.rpow_mul`).
8. Compare exponents with `Real.rpow_lt_rpow_left_iff (1 < q 0)`: `−m r_0 (1+δ) < δ r_0 (1+4δ) − r_0 (γ−η) κ`; divide by `r_0 > 0`; `(γ−η)κ < m(1+δ) + δ(1+4δ) < m(1+4δ)` (`1 + 4δ < 3m`: `m > 64`, `δ < 1`; `nlinarith`); so `κ < m(1+4δ)/(γ−η)` (`lt_div_iff`), contradicting (49).

#### Mathlib lemmas needed
- `Finset.le_sup`, `lt_div_iff`, `div_le_iff`, `Real.log_prod`, `Real.log_pow`, `Real.exp_lt_exp`, `Real.rpow_def_of_pos`, `Real.rpow_neg`, `Real.rpow_add`, `Real.rpow_mul`, `Real.rpow_le_rpow`, `Real.rpow_lt_rpow_left_iff`, `Real.rpow_le_iff_le_log`, `Finset.sum_lt_sum_of_nonempty`
- (project) `exists_monic_aeval_eq_zero`, `exists_m`, `exists_delta`, `exists_approximants`, `exists_degrees`, `main_lemma`, `one_le_prod_pow_mul_abs_eval`, `abs_eval_lt_of_le_index`, `three_small_factors`, `sqrt_lt_floor`, `eta_lt_gam_iff`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §7 clean.tex:1565-1690
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.14).

#### Generality decision
- real irrational algebraic integers, any real `κ`.

**Progress**:
- 2026-10-12T19:53: proved; #print axioms Roth.roth = propext, Classical.choice, Quot.sound


### [CLEANUP-ALL-1] Run /cleanup-all on the project so far
- **Status**: done
- **File**: (all)
- **Depends on**: every proof ticket before the milestone (T001 … T083)
- **Parallel**: no
- **Type**: cleanup
- **Description**: project-wide `/cleanup-all` before the milestone theorem `Roth.roth`.

**Progress**:
- 2026-10-12T20:04: all files cleaned per file; lake build clean; remaining warnings are copyright headers and unused hypotheses/instances in protected statements


### [T084] Roth's theorem
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T078, T083, CLEANUP-31, CLEANUP-ALL-1
- **Parallel**: no
- **Type**: theorem
- **Decomposition entries**: R13.15
- **Milestone**: yes (project goal)

#### Statement
```lean
theorem roth {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : (approxSet α κ).Infinite) : κ ≤ 2 := by sorry

theorem roth_rat {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2 := by sorry
```

#### Proof sketch
1. `roth`: `by_contra hκ; push_neg at hκ`; `obtain ⟨α', κ', hα', hint', hκ', hinf'⟩ := reduction hα halg hκ hinf`; `exact absurd (roth_of_isIntegral hα' hint' hinf') (not_le.2 hκ')`.
2. `roth_rat`: apply `roth hα halg` to the image of the set under `x ↦ (x.num, x.den)`: injective (`Rat.ext`), and `(x.num, x.den) ∈ approxSet α κ` since `x.den > 0` (`Rat.den_pos`) and `(x.num : ℝ)/x.den = x` (`Rat.num_div_den`, `Rat.cast_def`); `Set.Infinite.image (injOn)`/`Set.infinite_of_injective_forall_mem`, `Set.Infinite.mono`.

#### Mathlib lemmas needed
- `not_le`, `absurd`, `Set.Infinite.image`, `Set.Infinite.mono`, `Set.infinite_of_injective_forall_mem`
- `Rat.ext`, `Rat.num_div_den`, `Rat.cast_def`, `Rat.den_pos`
- (project) `reduction`, `roth_of_isIntegral`

#### Sources
- [TY] Takloo-Bighash–Yin, *Formalizing Roth's theorem*, `.mathlib-quality/references/clean.tex`: §6 Theorem (Roth), clean.tex:1139-1146
  (verbatim quotes and the Lean ↔ source match are in `decomposition.md`, entries R13.15).

#### Generality decision
- `Irrational α`, `IsAlgebraic ℚ α`, any real `κ`; `roth_rat` is the mathlib-idiomatic form with `x.den`.

**Progress**:
- 2026-10-12T19:53: proved; #print axioms Roth.roth = propext, Classical.choice, Quot.sound


### [CLEANUP-32] Run /cleanup on Roth/Main.lean
- **Status**: done
- **File**: Roth/Main.lean
- **Depends on**: T084
- **Parallel**: no (blocks all later proof tickets on this file)
- **Type**: cleanup
- **Description**: final per-file cleanup. Run `/cleanup` on `Roth/Main.lean` to bring it to mathlib quality (naming,
  golfing, docstrings, `@[simp]` audit) before further work builds on it. Algorithmically inserted
  per the cadence rule of `/develop` §1g.

**Progress**:
- 2026-10-12T20:04: agent cleanup of Main.lean; signatures unchanged


### [CLEANUP-FINAL] Run /cleanup-all on the whole project
- **Status**: done
- **File**: (all)
- **Depends on**: every other ticket
- **Parallel**: no
- **Type**: cleanup
- **Description**: final `/cleanup-all`; then `/pre-submit` (`#print axioms Roth.roth` must show only
  `propext`, `Classical.choice`, `Quot.sound`).

**Progress**:
- 2026-10-12T20:04: lake build passes, no sorry, #print axioms Roth.roth = propext, Classical.choice, Quot.sound

