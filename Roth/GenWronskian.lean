/-
Copyright (c) 2026 Ramin Takloo-Bighash, Samuel Yin. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Ramin Takloo-Bighash, Samuel Yin
-/

import Mathlib.Algebra.CharP.Algebra
import Mathlib.Data.List.Indexes
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.RingTheory.Localization.Module

import Roth.HasseDeriv
import Roth.Wronskian

/-!
# Generalized Wronskians

For `φ : Fin l → MvPolynomial σ K` and Hasse operators `Δ_{D μ}` of orders `≤ μ`, the generalized
Wronskian is `det (Δ_{D μ} (φ ν))_{μ ν}`.  The main result (Lemma 1 of the source) is that a
linearly independent family has at least one nonvanishing generalized Wronskian.  The proof uses
the Kronecker substitution `x_j ↦ t^{k^j}`, which reduces to the univariate Wronskian criterion.

Source: Takloo-Bighash–Yin, *Formalizing Roth's theorem*, §2 "Wronskians", second lemma and
Lemma 1 (`roth:lem1`) (`.mathlib-quality/references/clean.tex`).
-/

namespace Matrix

/-- Expanding the determinant of a matrix whose rows are linear combinations, by multilinearity
in the rows.

Source: §2, proof of Lemma 1 ("multilinearity of the determinant in each row gives
`det (∑_i f^μ_i ⋯) = ∑_{i ∈ 𝒮} f_i(t) det (⋯)`"). -/
theorem det_sum_rows {R ι n : Type*} [CommRing R] [Fintype n] [DecidableEq n] (s : n → Finset ι)
    (c : n → ι → R) (N : n → ι → n → R) :
    (of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (of fun μ ν ↦ N μ (f μ) ν).det := by
  have h := (detRowAlternating (R := R) (n := n)).toMultilinearMap.map_sum_finset
    (fun μ i ↦ c μ i • N μ i) s
  simp_rw [MultilinearMap.map_smul_univ, smul_eq_mul] at h
  simp only [det, Finset.sum_fn, Pi.smul_def, smul_eq_mul] at h ⊢
  exact h

end Matrix

namespace Roth

open MvPolynomial

variable {σ : Type*} {l : ℕ}

/-- The generalized Wronskian `det (Δ_{D μ} φ_ν)_{μ, ν}`. Source: §2, definition of
`W(φ_0, …, φ_{l-1}; Δ_0, …, Δ_{l-1})`. -/
noncomputable def genWronskian {R : Type*} [CommRing R] (D : Fin l → σ →₀ ℕ)
    (φ : Fin l → MvPolynomial σ R) : MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det

/-- `genWronskian` commutes with change of coefficients along a ring hom. -/
theorem map_genWronskian {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R) :
    map f (genWronskian D φ) = genWronskian D fun ν ↦ map f (φ ν) := by
  simp [genWronskian, RingHom.map_det, Matrix.map]

/-- `genWronskian` commutes with renaming variables along an injective map, provided the
multi-indices are transported along the same map. -/
theorem rename_genWronskian {R τ : Type*} [CommRing R] {f : σ → τ} (hf : Function.Injective f)
    (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R) :
    rename f (genWronskian D φ) =
      genWronskian (fun μ ↦ (D μ).mapDomain f) fun ν ↦ rename f (φ ν) := by
  simp [genWronskian, AlgHom.map_det, Matrix.map, hasseDeriv_rename hf]

section Kronecker

variable [Fintype σ]

section CommSemiring

variable {R : Type*} [CommSemiring R]

/-- Kronecker substitution `x_j ↦ t^{k^{e j}}` where `e : σ ≃ Fin (card σ)` is the chosen
enumeration. Source: §2, proof of Lemma 1 (`h_ν(t) = φ_ν(t, t^k, …, t^{k^{p-1}})`). -/
noncomputable def kroneckerSubst (k : ℕ) : MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)

/-- The exponent `∑ j, d j * k^{e j}` of the image of the monomial `X^d`: the `Finsupp.weight`
with weights `k ^ e j`. -/
noncomputable abbrev kroneckerExp (k : ℕ) : (σ →₀ ℕ) →+ ℕ :=
  Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)

theorem kroneckerExp_apply (k : ℕ) (d : σ →₀ ℕ) :
    kroneckerExp k d = ∑ j, d j * k ^ (Fintype.equivFin σ j : ℕ) := by
  simp [Finsupp.weight_apply, Finsupp.sum_fintype]

/-- The Kronecker substitution sends the monomial `a X^d` to `a t^{kroneckerExp k d}`. -/
@[simp]
theorem kroneckerSubst_monomial (k : ℕ) (d : σ →₀ ℕ) (a : R) :
    kroneckerSubst k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d := by
  simp [kroneckerSubst, kroneckerExp_apply, aeval_monomial, Finsupp.prod_fintype, ← pow_mul,
    mul_comm, ← Finset.prod_pow_eq_pow_sum]

/-- The Kronecker exponent map is injective on exponent vectors whose entries are all `< k`.

Source: §2, proof of Lemma 1, FACT ("Since each `s_i` is strictly smaller than `k`, the
representation of any natural number in the form `s_1 + k s_2 + ⋯ + k^{p-1} s_p` is unique"). -/
theorem kroneckerExp_injOn {k : ℕ} :
    Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by
  intro d hd d' hd' h
  rcases le_or_gt k 1 with hk | hk
  · grind
  set e := Fintype.equivFin σ
  have hsum (d : σ →₀ ℕ) : Nat.ofDigits k (List.ofFn fun i ↦ d (e.symm i)) = kroneckerExp k d := by
    simp only [Nat.ofDigits_eq_sum_mapIdx, List.mapIdx_eq_ofFn, Fin.sum_ofFn, kroneckerExp_apply,
      ← e.symm.sum_comp, e, List.get_eq_getElem, List.getElem_ofFn, List.length_ofFn,
      Equiv.apply_symm_apply, Fin.val_cast, Fin.eta]
  apply DFunLike.coe_injective
  apply e.symm.surjective.injective_comp_right
  refine List.ofFn_injective (Nat.ofDigits_inj_of_len_eq hk (by simp)
    (List.forall_mem_ofFn_iff.2 fun i ↦ hd (e.symm i))
    (List.forall_mem_ofFn_iff.2 fun i ↦ hd' (e.symm i)) ?_)
  simpa [Function.comp_def, hsum] using h

/-- If all partial degrees of `P` are `< k`, the Kronecker substitution preserves the coefficient
of `X^d` for every `d` with entries `< k`.

Source: §2, proof of Lemma 1 ("Comparing the coefficient of `t^{s_1 + k s_2 + ⋯}` gives ..."). -/
theorem coeff_kroneckerSubst {k : ℕ} {P : MvPolynomial σ R} (hP : ∀ j, degreeOf j P < k)
    {d : σ →₀ ℕ} (hd : ∀ j, d j < k) :
    (kroneckerSubst k P).coeff (kroneckerExp k d) = P.coeff d := by
  conv_lhs => rw [P.as_sum]
  rw [map_sum, Polynomial.finsetSum_coeff]
  simp_rw [kroneckerSubst_monomial, Polynomial.coeff_C_mul_X_pow]
  rw [Finset.sum_eq_single d]
  · simp
  · intro e he hed
    exact ite_eq_right fun h ↦ hed (kroneckerExp_injOn
      (fun j ↦ (monomial_le_degreeOf j he).trans_lt (hP j)) hd h.symm)
  · intro hdP
    simp [notMem_support_iff.1 hdP]

/-- A polynomial with all partial degrees `< k` vanishes iff its Kronecker substitution does.

Source: §2, Lean implementation note ("prove injectivity only on the subspace where every
individual exponent is less than `k`"). -/
theorem kroneckerSubst_eq_zero_iff {k : ℕ} {P : MvPolynomial σ R}
    (hP : ∀ j, degreeOf j P < k) : kroneckerSubst k P = 0 ↔ P = 0 := by
  refine ⟨fun h ↦ support_eq_empty.1 <| Finset.eq_empty_iff_forall_notMem.2 fun d hd ↦ ?_,
    fun h ↦ by rw [h, map_zero]⟩
  apply mem_support_iff.1 hd
  simpa [h] using (coeff_kroneckerSubst hP fun j ↦ (monomial_le_degreeOf j hd).trans_lt (hP j)).symm

/-- The algebraic chain rule for substituting univariate polynomials into a multivariate one.

Source: §2, proof of Lemma 1, FACT
(`d/dt h_ν(t) = ∑_j γ_j'(t) (∂φ_ν/∂x_j)(γ(t))`). -/
theorem _root_.MvPolynomial.derivative_aeval (γ : σ → Polynomial R) (P : MvPolynomial σ R) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) := by
  classical
  induction P using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq, Finset.sum_add_distrib, mul_add]
  | mul_X p j hp =>
    simp [hp, Finset.sum_add_distrib, ← Finset.mul_sum, add_mul, mul_assoc, mul_comm,
      Pi.single_apply, apply_ite (aeval γ)]

end CommSemiring

section CommRing

variable {R : Type*} [CommRing R]

/-- The Kronecker substitution preserves linear independence of polynomials whose partial degrees
are all `< k`.

Source: §2, proof of Lemma 1 ("We claim that these polynomials are linearly independent"). -/
theorem linearIndependent_kroneckerSubst {k : ℕ} {φ : Fin l → MvPolynomial σ R}
    (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent R φ) :
    LinearIndependent R fun ν ↦ kroneckerSubst k (φ ν) := by
  rw [Fintype.linearIndependent_iff] at h ⊢
  intro g hg ν
  refine h g ((kroneckerSubst_eq_zero_iff (k := k) fun j ↦ ?_).mp ?_) ν
  · refine (degreeOf_sum_le _ _ _).trans_lt <|
      (Finset.sup_lt_iff (Nat.zero_lt_of_lt (hφ ν j))).2 fun i _ ↦ ?_
    simpa [smul_eq_C_mul] using (degreeOf_C_mul_le (φ i) j (g i)).trans_lt (hφ i j)
  · simpa [map_sum, map_smul] using hg

end CommRing

end Kronecker

section Field

variable {K : Type*} [Field K]

section Fintype

variable [Fintype σ]

/-- The operator `P ↦ kroneckerSubst k (Δ_d P)`, as an element of the `K[X]`-module of functions. -/
private noncomputable def kronHasse (k : ℕ) (d : σ →₀ ℕ) : MvPolynomial σ K → Polynomial K :=
  fun P ↦ kroneckerSubst k (hasseDeriv d P)

/-- The `K[X]`-span of the operators `kronHasse k d` with `|d| ≤ μ`. -/
private noncomputable def kronSpan (k μ : ℕ) : Submodule (Polynomial K)
    (MvPolynomial σ K → Polynomial K) :=
  Submodule.span (Polynomial K) (kronHasse (K := K) k '' {d | d.degree ≤ μ})

private lemma derivative_kronHasse_aux (k : ℕ) (d : σ →₀ ℕ) :
    (fun P ↦ Polynomial.derivative (kronHasse (K := K) k d P)) =
      ∑ j, (Polynomial.derivative (Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)) *
        Polynomial.C ((d j + 1 : ℕ) : K)) • kronHasse k (d + Finsupp.single j 1) := by
  funext P
  simp [kronHasse, kroneckerSubst, derivative_aeval, pderiv_hasseDeriv, map_smul,
    Polynomial.smul_eq_C_mul, mul_assoc, mul_comm, mul_left_comm]

private lemma derivative_mem_kronSpan_aux (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K}
    (hF : F ∈ kronSpan k μ) :
    (fun P ↦ Polynomial.derivative (F P)) ∈ kronSpan (K := K) (σ := σ) k (μ + 1) := by
  induction hF using Submodule.span_induction with
  | mem F hF =>
    obtain ⟨d, hd, rfl⟩ := hF
    rw [derivative_kronHasse_aux]
    refine Submodule.sum_mem _ fun j _ ↦ Submodule.smul_mem _ _ (Submodule.subset_span ?_)
    refine ⟨d + Finsupp.single j 1, ?_, rfl⟩
    simpa using Nat.add_le_add_right hd 1
  | zero => exact zero_mem _
  | add F G _ _ hF hG =>
    convert Submodule.add_mem _ hF hG using 1
    funext P
    simp [Polynomial.derivative_add]
  | smul a F hF' hF =>
    convert Submodule.add_mem (kronSpan (K := K) (σ := σ) k (μ + 1))
      (Submodule.smul_mem _ (Polynomial.derivative a)
        (Submodule.span_mono (Set.image_mono fun _ hd ↦ le_trans hd (Nat.le_succ μ)) hF'))
      (Submodule.smul_mem _ a hF) using 1
    funext P
    simp [Polynomial.derivative_mul, add_comm]

private lemma hasseDeriv_kroneckerSubst_mem_aux [CharZero K] (k μ : ℕ) :
    (fun P ↦ Polynomial.hasseDeriv μ (kroneckerSubst k P)) ∈ kronSpan (K := K) (σ := σ) k μ := by
  induction μ with
  | zero =>
    refine Submodule.subset_span ⟨0, by simp, ?_⟩
    funext P
    simp [kronHasse]
  | succ μ ih =>
    -- `(μ + 1) • Δ^{μ+1} = d/dt ∘ Δ^μ` (`Polynomial.hasseDeriv_comp 1 μ`), and the span is
    -- closed under the scalar `μ + 1`, which is invertible in characteristic zero.
    apply (((kronSpan (K := K) (σ := σ) k (μ + 1)).restrictScalars K).smul_mem_iff
      (s := ((μ + 1 : ℕ) : K)) (Nat.cast_ne_zero.2 μ.succ_ne_zero)).mp
    change (((μ + 1 : ℕ) : K) • fun P ↦ Polynomial.hasseDeriv (μ + 1) (kroneckerSubst k P)) ∈
      kronSpan (K := K) (σ := σ) k (μ + 1)
    convert derivative_mem_kronSpan_aux k μ ih using 1
    funext P
    simpa [← Nat.cast_smul_eq_nsmul K, add_comm] using
      (congrArg (fun L ↦ L (kroneckerSubst k P)) (Polynomial.hasseDeriv_comp (R := K) 1 μ)).symm

variable (σ K) in
/-- The `μ`-th Hasse derivative of a Kronecker substitution is a `K[t]`-linear combination of
Kronecker substitutions of Hasse derivatives `Δ_d` of order `|d| ≤ μ`, uniformly in `P`.

Source: §2, proof of Lemma 1 ("for each `μ`, there is a natural number `r(μ)` ..., polynomials
`f^μ_i(t)` with rational coefficients, and differential operators `Δ^{(i)}_μ` of order `≤ μ` such
that for all `ν`, `d^μ/dt^μ h_ν = ∑_i f^μ_i(t) (Δ^{(i)}_μ φ_ν)(γ(t))`"; here stated with Hasse
derivatives on both sides, which over `ℚ` differ from iterated derivatives by factorials). -/
theorem exists_hasseDeriv_kroneckerSubst_eq_sum [CharZero K] (k μ : ℕ) : ∃ (s : Finset (σ →₀ ℕ))
    (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K,
      Polynomial.hasseDeriv μ (kroneckerSubst k P) =
        ∑ d ∈ s, c d * kroneckerSubst k (hasseDeriv d P) := by
  obtain ⟨c, hc, hsum⟩ := (Finsupp.mem_span_image_iff_linearCombination _).1
    (hasseDeriv_kroneckerSubst_mem_aux (K := K) (σ := σ) k μ)
  refine ⟨c.support, c, hc, fun P ↦ ?_⟩
  simpa [Finsupp.linearCombination_apply, Finsupp.sum, kronHasse] using congrFun hsum.symm P

private lemma wronskian_kroneckerSubst_eq_sum_aux (k : ℕ) (φ : Fin l → MvPolynomial σ K)
    (s : Fin l → Finset (σ →₀ ℕ)) (c : Fin l → (σ →₀ ℕ) → Polynomial K)
    (hc : ∀ μ ν : Fin l, Polynomial.hasseDeriv μ (kroneckerSubst k (φ ν)) =
      ∑ d ∈ s μ, c μ d * kroneckerSubst k (hasseDeriv d (φ ν))) :
    wronskian (fun ν ↦ kroneckerSubst k (φ ν)) =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * kroneckerSubst k (genWronskian f φ) := by
  simpa [wronskian, hc, genWronskian, AlgHom.map_det, Matrix.map] using
    Matrix.det_sum_rows s c (fun μ d ν ↦ kroneckerSubst k (hasseDeriv d (φ ν)))

end Fintype

private lemma exists_genWronskian_ne_zero_of_finite_aux [Finite σ] [CharZero K]
    {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by
  let := Fintype.ofFinite σ
  -- a Kronecker base `k` exceeding every partial degree of every `φ ν`
  let k := ∑ ν, (φ ν).totalDegree + 1
  choose s c hs hc using fun μ : Fin l ↦ exists_hasseDeriv_kroneckerSubst_eq_sum σ K k μ
  by_contra! hcon
  -- the univariate Wronskian of the substituted family is nonzero ...
  apply wronskian_ne_zero_of_linearIndependent
    (linearIndependent_kroneckerSubst (fun ν j ↦ Nat.lt_succ_of_le
      ((degreeOf_le_totalDegree _ _).trans
        (Finset.single_le_sum (f := fun ν ↦ (φ ν).totalDegree) (by simp) (Finset.mem_univ ν)))) h)
  -- ... but expands as a combination of the generalized Wronskians, all of which vanish
  rw [wronskian_kroneckerSubst_eq_sum_aux k φ s c (fun μ ν ↦ hc μ (φ ν))]
  refine Finset.sum_eq_zero fun f hf ↦ ?_
  rw [hcon f fun μ ↦ hs μ _ (Fintype.mem_piFinset.1 hf μ), map_zero, mul_zero]

private lemma exists_genWronskian_ne_zero_of_field_aux [CharZero K] {φ : Fin l → MvPolynomial σ K}
    (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by
  classical
  -- restrict to the finitely many variables actually occurring in the family
  let s : Finset σ := Finset.univ.biUnion fun ν ↦ (φ ν).vars
  choose ψ hψ using fun ν ↦ exists_rename_eq_of_vars_subset_range (φ ν) (Subtype.val : s → σ)
    Subtype.val_injective fun x hx ↦ ⟨⟨x, Finset.mem_biUnion.2 ⟨ν, Finset.mem_univ _, hx⟩⟩, rfl⟩
  have hli : LinearIndependent K ψ := by
    refine LinearIndependent.of_comp (rename (R := K) Subtype.val).toLinearMap ?_
    convert h using 1
    exact funext hψ
  obtain ⟨D, hD, hne⟩ := exists_genWronskian_ne_zero_of_finite_aux hli
  refine ⟨fun μ ↦ (D μ).mapDomain Subtype.val, fun μ ↦ by simpa using hD μ, fun h0 ↦ hne ?_⟩
  apply rename_injective (R := K) _ (Subtype.val_injective (p := (· ∈ s)))
  rw [rename_genWronskian Subtype.val_injective, map_zero, ← h0]
  simp [hψ]

end Field

/-- **Lemma 1**: a linearly independent family of polynomials has a generalized Wronskian (with
Hasse operators of orders `|D μ| ≤ μ`) that is not identically zero.

Source: §2, Lemma `roth:lem1` ("If `φ_0, …, φ_{l-1}` are `l` linearly independent
polynomials in `p` variables with rational coefficients, then at least one of their generalized
Wronskians is not identically zero"). -/
theorem exists_genWronskian_ne_zero {R : Type*} [CommRing R] [IsDomain R] [CharZero R]
    {φ : Fin l → MvPolynomial σ R} (h : LinearIndependent R φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by
  -- pass to the fraction field, where linear independence is preserved
  have hli : LinearIndependent (FractionRing R)
      (fun ν ↦ map (algebraMap R (FractionRing R)) (φ ν)) := by
    rw [← LinearIndependent.iff_fractionRing R (FractionRing R)]
    exact h.map' (mapAlgHom (Algebra.ofId R (FractionRing R))).toLinearMap
      (LinearMap.ker_eq_bot.2 (map_injective _ (IsFractionRing.injective R (FractionRing R))))
  obtain ⟨D, hD, hne⟩ := exists_genWronskian_ne_zero_of_field_aux hli
  exact ⟨D, hD, fun h0 ↦ hne (by rw [← map_genWronskian, h0, map_zero])⟩

end Roth
