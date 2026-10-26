section Map

variable (f : R →+* S₁)

/-- `map f p` maps a polynomial `p` across a ring hom `f` -/
def map : MvPolynomial σ R →+* MvPolynomial σ S₁ := AddMonoidAlgebra.mapRingHom _ f

@[simp]
theorem map_monomial (s : σ →₀ ℕ) (a : R) : map f (monomial s a) = monomial s (f a) :=
  AddMonoidAlgebra.map_single ..

@[simp]
theorem map_C : ∀ a : R, map f (C a : MvPolynomial σ R) = C (f a) :=
  map_monomial _ _

@[simp] protected theorem map_ofNat (n : Nat) [n.AtLeastTwo] :
    (ofNat(n) : MvPolynomial σ R).map f = ofNat(n) :=
  _root_.map_ofNat _ _

@[simp]
theorem map_X (n : σ) : map f (X n : MvPolynomial σ R) = X n := by simp [X]

theorem map_id : ∀ p : MvPolynomial σ R, map (RingHom.id R) p = p := AddMonoidAlgebra.map_id

theorem map_map [CommSemiring S₂] (g : S₁ →+* S₂) (p : MvPolynomial σ R) :
    map g (map f p) = map (g.comp f) p := AddMonoidAlgebra.map_map ..

theorem eval₂_eq_eval_map (g : σ → S₁) (p : MvPolynomial σ R) : p.eval₂ f g = eval g (map f p) := by
  simp [eval₂, eval]; simp [map, MvPolynomial, Finsupp.sum_mapRange_index, mapRingHom]

theorem eval₂_comp_right {S₂} [CommSemiring S₂] (k : S₁ →+* S₂) (f : R →+* S₁) (g : σ → S₁) (p) :
    k (eval₂ f g p) = eval₂ k (k ∘ g) (map f p) := by
  apply MvPolynomial.induction_on p
  · intro r
    rw [eval₂_C, map_C, eval₂_C]
  · intro p q hp hq
    rw [eval₂_add, k.map_add, (map f).map_add, eval₂_add, hp, hq]
  · intro p s hp
    rw [eval₂_mul, k.map_mul, (map f).map_mul, eval₂_mul, map_X, hp, eval₂_X, eval₂_X, comp_apply]

theorem map_eval₂ (f : R →+* S₁) (g : S₂ → MvPolynomial S₃ R) (p : MvPolynomial S₂ R) :
    map f (eval₂ C g p) = eval₂ C (map f ∘ g) (map f p) := by
  apply MvPolynomial.induction_on p
  · intro r
    rw [eval₂_C, map_C, map_C, eval₂_C]
  · intro p q hp hq
    rw [eval₂_add, (map f).map_add, hp, hq, (map f).map_add, eval₂_add]
  · intro p s hp
    rw [eval₂_mul, (map f).map_mul, hp, (map f).map_mul, map_X, eval₂_mul, eval₂_X, eval₂_X,
      comp_apply]

lemma eval₂_map_comp_C {ι : Type*} (f : R →+* S₁) (h : ι → MvPolynomial σ S₁)
    (p : MvPolynomial ι R) : eval₂ ((map f).comp C) h p = eval₂ C h (map f p) := by
  induction p using MvPolynomial.induction_on <;> simp_all

lemma map_eval {S₂ : Type*} [CommSemiring S₂] (q : S₁ →+* S₂) (g : σ → S₁) (p : MvPolynomial σ S₁) :
    q (eval g p) = eval (q ∘ g) (map q p) := by
  rw [← eval₂_eq_eval_map, ← eval₂_id, eval₂_comp_right, map_id]

theorem coeff_map (p : MvPolynomial σ R) : ∀ m : σ →₀ ℕ, (map f p).coeff m = f (p.coeff m) := by
  classical
  apply MvPolynomial.induction_on p <;> clear p
  · intro r m
    simp_rw [map_C, coeff_C, apply_ite f, f.map_zero]
  · intro p q hp hq m
    simp only [hp, hq, (map f).map_add, coeff_add, Finsupp.add_apply, f.map_add]
