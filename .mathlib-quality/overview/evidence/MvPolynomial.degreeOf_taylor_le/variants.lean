import Roth.Taylor

/-! Evidence for `MvPolynomial.degreeOf_taylor_le`. -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

-- (1) plain `simp` does not prove the statement.
example (α : σ → R) (j : σ) (P : MvPolynomial σ R) :
    degreeOf j (taylor α P) ≤ degreeOf j P := by
  fail_if_success (simp; done)
  exact degreeOf_taylor_le α j P

-- (2) Over a commutative ring, the inequality upgrades to an equality (two lines).
theorem degreeOf_taylor_ring {A : Type*} [CommRing A] (α : σ → A) (j : σ)
    (P : MvPolynomial σ A) : degreeOf j (taylor α P) = degreeOf j P := by
  refine le_antisymm (degreeOf_taylor_le α j P) ?_
  simpa [taylor_neg_taylor] using degreeOf_taylor_le (fun i ↦ -α i) j (taylor α P)

-- (3a) hasseCoeff m m = 1.
theorem hasseCoeff_self' (m : σ →₀ ℕ) : hasseCoeff m m = 1 := by
  simp [hasseCoeff, Finsupp.prod, Nat.choose_self]

-- (3b) If `m` is maximal (for the pointwise order) in the support, then the Taylor coefficient at `m` is the coefficient of `P` at `m`.
theorem coeff_taylor_of_maximal (α : σ → R) (P : MvPolynomial σ R) (m : σ →₀ ℕ)
    (hmax : ∀ e ∈ P.support, m ≤ e → e = m) :
    (taylor α P).coeff m = P.coeff m := by
  classical
  have h : hasseDeriv m P = C (P.coeff m) := by
    ext e
    rw [coeff_hasseDeriv, coeff_C]
    split_ifs with he
    · subst he; simp [hasseCoeff_self']
    · have : P.coeff (e + m) = 0 := by
        by_contra hne
        have h1 := hmax (e + m) (mem_support_iff.2 hne) le_add_self
        exact he (by simpa using congrArg (· - m) h1.symm)
      simp [this]
  rw [coeff_taylor, h, eval_C]

-- (3c) Over any commutative semiring, translation preserves `degreeOf` exactly.
theorem degreeOf_taylor (α : σ → R) (j : σ) (P : MvPolynomial σ R) :
    degreeOf j (taylor α P) = degreeOf j P := by
  classical
  refine le_antisymm (degreeOf_taylor_le α j P) ?_
  rcases eq_or_ne P 0 with rfl | hP
  · simp
  obtain ⟨e, he, hej⟩ : ∃ e ∈ P.support, e j = degreeOf j P := by
    obtain ⟨e, he, hmax⟩ := P.support.exists_max_image (fun m ↦ m j)
      (support_nonempty.2 hP)
    exact ⟨e, he, le_antisymm (monomial_le_degreeOf j he)
      (degreeOf_le_iff.2 hmax)⟩
  obtain ⟨m, hem, hm, hmax⟩ :=
    (P.support.filter fun d ↦ d j = degreeOf j P).exists_le_maximal
      (Finset.mem_filter.2 ⟨he, hej⟩)
  rw [Finset.mem_filter] at hm
  have hmax' : ∀ d ∈ P.support, m ≤ d → d = m := by
    intro d hd hmd
    have hdj : d j = degreeOf j P :=
      le_antisymm (monomial_le_degreeOf j hd) (hm.2 ▸ hmd j)
    exact le_antisymm (hmax (Finset.mem_filter.2 ⟨hd, hdj⟩) hmd) hmd
  have hcoeff : (taylor α P).coeff m ≠ 0 := by
    rw [coeff_taylor_of_maximal α P m hmax']
    exact mem_support_iff.1 hm.1
  exact hm.2 ▸ monomial_le_degreeOf j (mem_support_iff.2 hcoeff)

end MvPolynomial
