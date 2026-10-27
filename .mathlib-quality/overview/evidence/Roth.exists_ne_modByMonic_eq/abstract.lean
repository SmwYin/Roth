import Roth.MainLemma

open Polynomial

/-- Abstract form: the Hasse/diag/boxFamily content is incidental; only a finite pigeon set and
a family of integer polynomials with bounded low remainder coefficients are used. -/
theorem exists_ne_forall_modByMonic_eq {α ι : Type*} {s : Set α} (hs : s.Finite)
    {f : ℤ[X]} (hf : f.Monic) (J : Finset ι) (g : ι → α → ℤ[X]) (C : ℕ)
    (hC : ∀ a ∈ s, ∀ j ∈ J, ∀ i < f.natDegree, |(g j a %ₘ f).coeff i| ≤ C)
    (hcount : (2 * C + 1) ^ (f.natDegree * J.card) < s.ncard) :
    ∃ a ∈ s, ∃ b ∈ s, a ≠ b ∧ ∀ j ∈ J, g j a %ₘ f = g j b %ₘ f := by
  classical
  let : Fintype s := hs.fintype
  let F (a : s) (p : J × Fin f.natDegree) : Set.Icc (-(C : ℤ)) C :=
    ⟨(g p.1.1 a.1 %ₘ f).coeff p.2, abs_le.1 (hC a.1 a.2 p.1.1 p.1.2 p.2.1 p.2.2)⟩
  obtain ⟨a, b, hne, h⟩ := Fintype.exists_ne_map_eq_of_card_lt F <| by
    simpa only [Fintype.card_fun, Fintype.card_ofFinset, Int.card_Icc, sub_neg_eq_add,
      Fintype.card_prod, Fintype.card_coe, Fintype.card_fin, mul_comm, Set.fintypeCard_eq_ncard,
      show ((C : ℤ) + 1 + C).toNat = 2 * C + 1 by lia] using hcount
  refine ⟨a, a.2, b, b.2, Subtype.coe_ne_coe.2 hne, fun j hj ↦ ?_⟩
  simpa [F, Polynomial.sum_modByMonic_coeff hf Polynomial.degree_le_natDegree] using
    congrArg (fun g ↦ ∑ i : Fin f.natDegree, Polynomial.monomial (i : ℕ)
      (g (⟨j, hj⟩, i) : ℤ)) h

/-- The project lemma is a corollary of the abstract form. -/
example {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ)
    {f : Polynomial ℤ} (hf : f.Monic) (J : Finset (σ →₀ ℕ)) (C : ℕ)
    (hC : ∀ W ∈ Roth.boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree,
      |(Roth.diag (MvPolynomial.hasseDeriv j W) %ₘ f).coeff i| ≤ C)
    (hcount : ((2 * C + 1 : ℕ) : ℝ) ^ (f.natDegree * J.card) < ((B : ℝ) + 1) ^ ∏ᶠ j, (r j + 1)) :
    ∃ W' ∈ Roth.boxFamily r B, ∃ W'' ∈ Roth.boxFamily r B, W' ≠ W'' ∧
      ∀ j ∈ J, Roth.diag (MvPolynomial.hasseDeriv j W') %ₘ f =
        Roth.diag (MvPolynomial.hasseDeriv j W'') %ₘ f :=
  exists_ne_forall_modByMonic_eq (Roth.boxFamily_finite r B) hf J
    (fun j W ↦ Roth.diag (MvPolynomial.hasseDeriv j W)) C hC <| by
      rw [Roth.ncard_boxFamily]; exact_mod_cast hcount
