import Mathlib.Data.List.Indexes
import Mathlib.Data.Nat.Digits.Defs
import Mathlib.LinearAlgebra.Multilinear.Basic

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

namespace Roth

open MvPolynomial

variable {K : Type*} [Field K] {σ : Type*} [Fintype σ] {l : ℕ}

/-- The generalized Wronskian `det (Δ_{D μ} φ_ν)_{μ, ν}`. Source: §2, definition of
`W(φ_0, …, φ_{l-1}; Δ_0, …, Δ_{l-1})`. -/
noncomputable def genWronskian (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ K) :
    MvPolynomial σ K :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det

/-- Linearly dependent polynomials have identically vanishing generalized Wronskians.

Source: §2, second lemma ("If `φ_0, …, φ_{l-1}` ... are linearly dependent ..., then all of
their generalized Wronskians are identically zero"). -/
theorem genWronskian_eq_zero_of_not_linearIndependent (D : Fin l → (σ →₀ ℕ))
    {φ : Fin l → MvPolynomial σ K} (h : ¬ LinearIndependent K φ) : genWronskian D φ = 0 := by
  classical
  obtain ⟨g, hg, ν₀, hν₀⟩ := Fintype.not_linearIndependent_iff.1 h
  refine Matrix.exists_mulVec_eq_zero_iff.1 ⟨fun ν ↦ C (g ν), fun h0 ↦ hν₀ ?_, ?_⟩
  · simpa using congrFun h0 ν₀
  · ext1 μ
    simpa [Matrix.mulVec, dotProduct, map_smul, ← smul_eq_C_mul, mul_comm] using
      congrArg (hasseDeriv (D μ)) hg

/-- Kronecker substitution `x_j ↦ t^{k^{e j}}` where `e : σ ≃ Fin (card σ)` is the chosen
enumeration. Source: §2, proof of Lemma 1 (`h_ν(t) = φ_ν(t, t^k, …, t^{k^{p-1}})`). -/
noncomputable def kronecker (k : ℕ) : MvPolynomial σ K →ₐ[K] Polynomial K :=
  aeval fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)

/-- The exponent `∑ j, d j * k^{e j}` of the image of the monomial `X^d`. -/
noncomputable def kroneckerExp (k : ℕ) (d : σ →₀ ℕ) : ℕ := ∑ j, d j * k ^ (Fintype.equivFin σ j : ℕ)

/-- The Kronecker substitution sends the monomial `a X^d` to `a t^{kroneckerExp k d}`. -/
theorem kronecker_monomial (k : ℕ) (d : σ →₀ ℕ) (a : K) :
    kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d := by
  simp [kronecker, kroneckerExp, aeval_monomial, Finsupp.prod_fintype, ← pow_mul, mul_comm,
    ← Finset.prod_pow_eq_pow_sum]

/-- The Kronecker exponent map is injective on exponent vectors whose entries are all `< k`.

Source: §2, proof of Lemma 1, FACT ("Since each `s_i` is strictly smaller than `k`, the
representation of any natural number in the form `s_1 + k s_2 + ⋯ + k^{p-1} s_p` is unique"). -/
theorem kroneckerExp_injOn {k : ℕ} (hk : 1 < k) :
    Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by
  intro d hd d' hd' h
  set e := Fintype.equivFin σ
  have hsum (d : σ →₀ ℕ) : Nat.ofDigits k (List.ofFn fun i ↦ d (e.symm i)) = kroneckerExp k d := by
    simp [Nat.ofDigits_eq_sum_mapIdx, List.mapIdx_eq_ofFn, Fin.sum_ofFn, kroneckerExp,
      ← e.symm.sum_comp, e]
  refine DFunLike.coe_injective <| e.symm.surjective.injective_comp_right ?_
  refine List.ofFn_injective (Nat.ofDigits_inj_of_len_eq hk (by simp)
    (by simpa using fun i ↦ hd (e.symm i)) (by simpa using fun i ↦ hd' (e.symm i)) ?_)
  simpa [Function.comp_def, hsum] using h

/-- If all partial degrees of `P` are `< k`, the Kronecker substitution preserves the coefficient
of `X^d` for every `d` with entries `< k`.

Source: §2, proof of Lemma 1 ("Comparing the coefficient of `t^{s_1 + k s_2 + ⋯}` gives ..."). -/
theorem coeff_kronecker {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K} (hP : ∀ j, degreeOf j P < k)
    {d : σ →₀ ℕ} (hd : ∀ j, d j < k) : (kronecker k P).coeff (kroneckerExp k d) = P.coeff d := by
  classical
  conv_lhs => rw [P.as_sum]
  rw [map_sum, Polynomial.finsetSum_coeff]
  simp_rw [kronecker_monomial, Polynomial.coeff_C_mul_X_pow]
  rw [Finset.sum_eq_single d]
  · simp
  · intro e he hed
    exact ite_eq_right fun h ↦ hed (kroneckerExp_injOn hk
      (fun j ↦ (monomial_le_degreeOf j he).trans_lt (hP j)) hd h.symm)
  · intro hdP
    simp [notMem_support_iff.1 hdP]

/-- A polynomial with all partial degrees `< k` vanishes iff its Kronecker substitution does.

Source: §2, Lean implementation note ("prove injectivity only on the subspace where every
individual exponent is less than `k`"). -/
theorem kronecker_eq_zero_iff {k : ℕ} (hk : 1 < k) {P : MvPolynomial σ K}
    (hP : ∀ j, degreeOf j P < k) : kronecker k P = 0 ↔ P = 0 := by
  refine ⟨fun h ↦ support_eq_empty.1 <| Finset.eq_empty_iff_forall_notMem.2 fun d hd ↦ ?_,
    fun h ↦ by rw [h, map_zero]⟩
  apply mem_support_iff.1 hd
  simpa [h] using (coeff_kronecker hk hP fun j ↦ (monomial_le_degreeOf j hd).trans_lt (hP j)).symm

/-- The Kronecker substitution preserves linear independence of polynomials whose partial degrees
are all `< k`.

Source: §2, proof of Lemma 1 ("We claim that these polynomials are linearly independent"). -/
theorem linearIndependent_kronecker {k : ℕ} (hk : 1 < k) {φ : Fin l → MvPolynomial σ K}
    (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent K φ) :
    LinearIndependent K fun ν ↦ kronecker k (φ ν) := by
  rw [Fintype.linearIndependent_iff] at h ⊢
  intro g hg
  apply h g
  refine (kronecker_eq_zero_iff hk fun j ↦ ?_).mp ?_
  · refine (degreeOf_sum_le _ _ _).trans_lt <|
      (Finset.sup_lt_iff (Nat.zero_lt_of_lt hk)).2 fun i _ ↦ ?_
    simpa [smul_eq_C_mul] using (degreeOf_C_mul_le (φ i) j (g i)).trans_lt (hφ i j)
  · simpa [map_sum, map_smul] using hg

/-- The algebraic chain rule for substituting univariate polynomials into a multivariate one.

Source: §2, proof of Lemma 1, FACT
(`d/dt h_ν(t) = ∑_j γ_j'(t) (∂φ_ν/∂x_j)(γ(t))`). -/
theorem derivative_aeval (γ : σ → Polynomial K) (P : MvPolynomial σ K) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P) := by
  classical
  induction P using MvPolynomial.induction_on with
  | C a => simp
  | add p q hp hq => simp [hp, hq, Finset.sum_add_distrib, mul_add]
  | mul_X p j hp =>
    simp [hp, Finset.sum_add_distrib, ← Finset.mul_sum, add_mul, mul_assoc, mul_comm,
      Pi.single_apply, apply_ite (aeval γ)]

/-- The operator `P ↦ kronecker k (Δ_d P)`, as an element of the `K[X]`-module of functions. -/
private noncomputable def kronHasse (k : ℕ) (d : σ →₀ ℕ) : MvPolynomial σ K → Polynomial K :=
  fun P ↦ kronecker k (hasseDeriv d P)

/-- The `K[X]`-span of the operators `kronHasse k d` with `|d| ≤ μ`. -/
private noncomputable def kronSpan (k μ : ℕ) : Submodule (Polynomial K)
    (MvPolynomial σ K → Polynomial K) :=
  Submodule.span (Polynomial K) (kronHasse (K := K) k '' {d | d.degree ≤ μ})

private lemma derivative_kronHasse_aux (k : ℕ) (d : σ →₀ ℕ) :
    (fun P ↦ Polynomial.derivative (kronHasse (K := K) k d P)) =
      ∑ j, (Polynomial.derivative (Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)) *
        Polynomial.C ((d j + 1 : ℕ) : K)) • kronHasse k (d + Finsupp.single j 1) := by
  classical
  funext P
  simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, map_smul,
    Polynomial.smul_eq_C_mul, mul_assoc, mul_comm, mul_left_comm]

private lemma derivative_mem_kronSpan (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K}
    (hF : F ∈ kronSpan k μ) :
    (fun P ↦ Polynomial.derivative (F P)) ∈ kronSpan (K := K) (σ := σ) k (μ + 1) := by
  classical
  induction hF using Submodule.span_induction with
  | mem F hF =>
    obtain ⟨d, hd, rfl⟩ := hF
    rw [derivative_kronHasse_aux]
    refine Submodule.sum_mem _ fun j _ ↦ Submodule.smul_mem _ _ (Submodule.subset_span ?_)
    refine ⟨d + Finsupp.single j 1, ?_, rfl⟩
    simp only [Set.mem_ofPred_eq, map_add, Finsupp.degree_single] at hd ⊢
    exact Nat.add_le_add_right hd 1
  | zero =>
    convert (kronSpan (K := K) (σ := σ) k (μ + 1)).zero_mem using 1
    funext P
    simp
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

private lemma hasseDeriv_kronecker_mem [CharZero K] (k μ : ℕ) :
    (fun P ↦ Polynomial.hasseDeriv μ (kronecker k P)) ∈ kronSpan (K := K) (σ := σ) k μ := by
  induction μ with
  | zero =>
    refine Submodule.subset_span ⟨0, by simp, ?_⟩
    funext P
    simp [kronHasse]
  | succ μ ih =>
    apply (((kronSpan (K := K) (σ := σ) k (μ + 1)).restrictScalars K).smul_mem_iff
      (s := ((μ + 1 : ℕ) : K)) (Nat.cast_ne_zero.2 μ.succ_ne_zero)).mp
    change (((μ + 1 : ℕ) : K) • fun P ↦ Polynomial.hasseDeriv (μ + 1) (kronecker k P)) ∈
      kronSpan (K := K) (σ := σ) k (μ + 1)
    convert derivative_mem_kronSpan k μ ih using 1
    funext P
    simpa [← Nat.cast_smul_eq_nsmul K, add_comm] using
      (congrArg (fun L ↦ L (kronecker k P)) (Polynomial.hasseDeriv_comp (R := K) 1 μ)).symm

/-- The `μ`-th Hasse derivative of a Kronecker substitution is a `K[t]`-linear combination of
Kronecker substitutions of Hasse derivatives `Δ_d` of order `|d| ≤ μ`, uniformly in `P`.

Source: §2, proof of Lemma 1 ("for each `μ`, there is a natural number `r(μ)` ..., polynomials
`f^μ_i(t)` with rational coefficients, and differential operators `Δ^{(i)}_μ` of order `≤ μ` such
that for all `ν`, `d^μ/dt^μ h_ν = ∑_i f^μ_i(t) (Δ^{(i)}_μ φ_ν)(γ(t))`"; here stated with Hasse
derivatives on both sides, which over `ℚ` differ from iterated derivatives by factorials). -/
theorem exists_hasseDeriv_kronecker_eq_sum [CharZero K] (k μ : ℕ) :
    ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧
      ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (kronecker k P) =
        ∑ d ∈ s, c d * kronecker k (hasseDeriv d P) := by
  classical
  obtain ⟨c, hc, hsum⟩ := (Finsupp.mem_span_image_iff_linearCombination _).1
    (hasseDeriv_kronecker_mem (K := K) (σ := σ) k μ)
  refine ⟨c.support, c, fun d hd => hc hd, fun P => ?_⟩
  rw [← congrFun hsum P, Finsupp.linearCombination_apply, Finsupp.sum, Finset.sum_apply]
  rfl

/-- Expanding the determinant of a matrix whose rows are linear combinations, by multilinearity
in the rows.

Source: §2, proof of Lemma 1 ("multilinearity of the determinant in each row gives
`det (∑_i f^μ_i ⋯) = ∑_{i ∈ 𝒮} f_i(t) det (⋯)`"). -/
theorem det_sum_rows {A : Type*} [CommRing A] {ι : Type*} [DecidableEq ι] (s : Fin l → Finset ι)
    (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) :
    (Matrix.of fun μ ν => ∑ i ∈ s μ, c μ i * N μ i ν).det =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν => N μ (f μ) ν).det := by
  have hM : (Matrix.of fun μ ν => ∑ i ∈ s μ, c μ i * N μ i ν) =
      fun μ => ∑ i ∈ s μ, c μ i • N μ i := by
    ext μ ν
    simp [Finset.sum_apply]
  rw [Matrix.det, hM, ← AlternatingMap.coe_multilinearMap, MultilinearMap.map_sum_finset]
  refine Finset.sum_congr rfl fun f _ => ?_
  rw [MultilinearMap.map_smul_univ, smul_eq_mul]
  rfl

/-- **Lemma 1**: a linearly independent family of polynomials has a generalized Wronskian (with
Hasse operators of orders `|D μ| ≤ μ`) that is not identically zero.

Source: §2, Lemma `roth:lem1` ("If `φ_0, …, φ_{l-1}` are `l` linearly independent
polynomials in `p` variables with rational coefficients, then at least one of their generalized
Wronskians is not identically zero"). -/
theorem exists_genWronskian_ne_zero [CharZero K] {φ : Fin l → MvPolynomial σ K}
    (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by
  classical
  set k := 2 + ∑ ν, ∑ j, degreeOf j (φ ν)
  have hk : 1 < k := by omega
  have hdeg : ∀ ν j, degreeOf j (φ ν) < k := fun ν j => by
    have h1 := Finset.single_le_sum (f := fun j => degreeOf j (φ ν)) (by simp) (Finset.mem_univ j)
    have h2 := Finset.single_le_sum (f := fun ν => ∑ j, degreeOf j (φ ν)) (by simp)
      (Finset.mem_univ ν)
    omega
  have hW := wronskian_ne_zero_of_linearIndependent (linearIndependent_kronecker hk hdeg h)
  choose s c hs hc using fun μ : Fin l => exists_hasseDeriv_kronecker_eq_sum (K := K) (σ := σ) k μ
  have hexp : wronskian (fun ν => kronecker k (φ ν)) = ∑ f ∈ Fintype.piFinset s,
      (∏ μ, c μ (f μ)) * kronecker k (genWronskian f φ) := by
    have hM : wronskianMatrix (fun ν => kronecker k (φ ν)) =
        Matrix.of fun μ ν => ∑ d ∈ s μ, c μ d * kronecker k (hasseDeriv d (φ ν)) := by
      ext1 μ ν
      exact hc μ (φ ν)
    rw [wronskian, hM, det_sum_rows]
    refine Finset.sum_congr rfl fun f _ => ?_
    rw [genWronskian, ← AlgHom.coe_toRingHom, RingHom.map_det]
    rfl
  by_contra! hcon
  refine hW (hexp ▸ Finset.sum_eq_zero fun f hf => ?_)
  rw [hcon f fun μ => hs μ _ (Fintype.mem_piFinset.1 hf μ), map_zero, mul_zero]

end Roth
