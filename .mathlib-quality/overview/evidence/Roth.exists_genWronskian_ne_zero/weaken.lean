import Roth.GenWronskian
import Mathlib.RingTheory.Localization.Module
import Mathlib.RingTheory.Localization.FractionRing
import Mathlib.Algebra.CharP.Algebra

/-! Evidence for `Roth.exists_genWronskian_ne_zero`. -/

open MvPolynomial

namespace Evidence

-- CommRing generalized Wronskian (copied from the `Roth.genWronskian` evidence file).
noncomputable def genWronskian {R σ : Type*} [CommRing R] {l : ℕ} (D : Fin l → σ →₀ ℕ)
    (φ : Fin l → MvPolynomial σ R) : MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det

theorem map_genWronskian {R S σ : Type*} [CommRing R] [CommRing S] (f : R →+* S) {l : ℕ}
    (D : Fin l → σ →₀ ℕ) (φ : Fin l → MvPolynomial σ R) :
    map f (genWronskian D φ) = genWronskian D fun ν ↦ map f (φ ν) := by
  rw [genWronskian, genWronskian, RingHom.map_det]
  congr 1
  ext μ ν
  simp [MvPolynomial.hasseDeriv_map]

-- (1) Drop `[Finite σ]`: every finite family lives in finitely many variables; rename into the
-- finite set of variables used, apply the project lemma there, and push forward along `rename`.
theorem exists_genWronskian_ne_zero_of_infinite {K σ : Type*} [Field K] [CharZero K] {l : ℕ}
    {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ Roth.genWronskian D φ ≠ 0 := by
  classical
  let s : Finset σ := Finset.univ.biUnion fun ν ↦ (φ ν).vars
  have hψ : ∀ ν, ∃ q : MvPolynomial s K, rename Subtype.val q = φ ν := fun ν ↦
    exists_rename_eq_of_vars_subset_range _ _ Subtype.val_injective fun x hx ↦
      ⟨⟨x, Finset.mem_biUnion.2 ⟨ν, Finset.mem_univ _, hx⟩⟩, rfl⟩
  choose ψ hψ using hψ
  have hinj := rename_injective (R := K) _ (Subtype.val_injective (p := (· ∈ s)))
  have hli : LinearIndependent K ψ := by
    refine LinearIndependent.of_comp (rename (R := K) Subtype.val).toLinearMap ?_
    convert h using 1
    funext ν
    exact hψ ν
  obtain ⟨D, hD, hne⟩ := Roth.exists_genWronskian_ne_zero hli
  refine ⟨fun μ ↦ (D μ).mapDomain Subtype.val, fun μ ↦ by simpa using hD μ, ?_⟩
  have : Roth.genWronskian (fun μ ↦ (D μ).mapDomain Subtype.val) φ =
      rename Subtype.val (Roth.genWronskian D ψ) := by
    rw [Roth.genWronskian, Roth.genWronskian, AlgHom.map_det]
    refine congrArg Matrix.det (Matrix.ext fun μ ν ↦ ?_)
    simp [← hψ, hasseDeriv_rename Subtype.val_injective]
  rw [this]
  exact fun h0 ↦ hne (hinj (by rw [h0, map_zero]))

-- (2) Weaken `[Field K]` to `[CommRing R] [IsDomain R] [CharZero R]` (fraction-field transfer),
-- also without `[Finite σ]` (uses (1)).
theorem exists_genWronskian_ne_zero {R σ : Type*} [CommRing R] [IsDomain R] [CharZero R] {l : ℕ}
    {φ : Fin l → MvPolynomial σ R} (h : LinearIndependent R φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by
  have hinj : Function.Injective (algebraMap R (FractionRing R)) :=
    IsFractionRing.injective R (FractionRing R)
  have : CharZero (FractionRing R) := charZero_of_injective_algebraMap hinj
  have hli : LinearIndependent (FractionRing R)
      (fun ν ↦ map (algebraMap R (FractionRing R)) (φ ν)) := by
    rw [← LinearIndependent.iff_fractionRing R (FractionRing R)]
    exact h.map' (mapAlgHom (Algebra.ofId R (FractionRing R))).toLinearMap
      (LinearMap.ker_eq_bot.2 (map_injective _ hinj))
  obtain ⟨D, hD, hne⟩ := exists_genWronskian_ne_zero_of_infinite hli
  refine ⟨D, hD, fun h0 ↦ hne ?_⟩
  have := congrArg (map (algebraMap R (FractionRing R))) h0
  rwa [map_genWronskian, map_zero] at this

-- (2') applies over `ℤ` with infinitely many variables
example {l : ℕ} {φ : Fin l → MvPolynomial ℕ ℤ} (h : LinearIndependent ℤ φ) :
    ∃ D : Fin l → (ℕ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 :=
  exists_genWronskian_ne_zero h

-- (3) the project statement is the specialisation
example {K σ : Type*} [Field K] [CharZero K] [Finite σ] {l : ℕ} {φ : Fin l → MvPolynomial σ K}
    (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ Roth.genWronskian D φ ≠ 0 :=
  exists_genWronskian_ne_zero h

end Evidence
