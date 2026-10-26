import Roth.Taylor

/-! Evidence for `MvPolynomial.taylor_eq_zero_iff` (overview run). -/

namespace MvPolynomial

-- (1) project statement and proof (CommRing)
example {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A) :
    taylor α P = 0 ↔ P = 0 :=
  (taylor_injective α).eq_iff' (map_zero _)

-- (2) generalisation to `CommSemiring`: the top-total-degree coefficients survive translation,
-- mirroring the leading-coefficient proof of mathlib's `Polynomial.taylor_eq_zero` (semiring).
theorem coeff_taylor_of_totalDegree_le {σ R : Type*} [CommSemiring R] (α : σ → R)
    (P : MvPolynomial σ R) {d : σ →₀ ℕ} (hd : P.totalDegree ≤ d.degree) :
    (taylor α P).coeff d = P.coeff d := by
  classical
  have key : hasseDeriv d P = C (P.coeff d) := by
    ext e
    rw [coeff_hasseDeriv, coeff_C]
    split_ifs with he
    · subst he
      simp [hasseCoeff, Finsupp.prod]
    · rw [coeff_eq_zero_of_totalDegree_lt, mul_zero]
      change P.totalDegree < (e + d).degree
      rw [map_add]
      have : 0 < e.degree := by
        rw [Nat.pos_iff_ne_zero]
        exact fun h ↦ he ((Finsupp.degree_eq_zero_iff e).1 h).symm
      omega
  rw [coeff_taylor, key, eval_C]

@[simp]
theorem taylor_eq_zero_iff' {σ R : Type*} [CommSemiring R] (α : σ → R) (P : MvPolynomial σ R) :
    taylor α P = 0 ↔ P = 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ by rw [h, map_zero]⟩
  by_contra hP
  obtain ⟨d, hd, hdeg⟩ := Finset.exists_mem_eq_sup P.support (support_nonempty.2 hP)
    fun s ↦ s.sum fun _ e ↦ e
  have h1 := congrArg (fun Q ↦ Q.coeff d) h
  rw [coeff_taylor_of_totalDegree_le α P (le_of_eq hdeg)] at h1
  exact mem_support_iff.1 hd (by simpa using h1)

-- (3) the generalised lemma still specialises to the project use (CommRing)
example {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A) :
    taylor α P = 0 ↔ P = 0 := taylor_eq_zero_iff' α P

-- (4) sanity: over the semiring ℕ∞ injectivity fails (see taylor_injective evidence) but the
-- zero-detection statement still holds
example (P : MvPolynomial Unit ℕ∞) : taylor (fun _ ↦ (⊤ : ℕ∞)) P = 0 ↔ P = 0 :=
  taylor_eq_zero_iff' _ P

end MvPolynomial
