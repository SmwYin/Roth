import Roth.HasseDeriv

/-! Evidence for `MvPolynomial.hasseDeriv_map` (overview / mathlibable). -/

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) The project statement, re-proved by the same two-line proof. -/
example {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (map f P) = map f (hasseDeriv d P) := by
  ext e
  simp [coeff_hasseDeriv, coeff_map]

/-- (2) Plain `simp` (current simp set, without the lemma) does not close it: the `ext`
step plus `coeff_hasseDeriv` is needed, so the lemma is not derivable by `simp` alone. -/
example {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (map f P) = map f (hasseDeriv d P) := by
  fail_if_success simp
  exact hasseDeriv_map f d P

/-- (3) Linear-map-free "induction" proof via `induction_on'`, mirroring `pderiv_map`. -/
example {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (map f P) = map f (hasseDeriv d P) := by
  induction P using MvPolynomial.induction_on' with
  | monomial k a => simp [map_monomial]
  | add p q hp hq => simp [hp, hq]

-- (4) Tagging it `@[simp]` (as mathlib tags the univariate `Polynomial.hasseDeriv_map`)
-- is safe: `simp` then closes the composite `map`/`map` case without looping.
attribute [local simp] hasseDeriv_map in
example {S T : Type*} [CommSemiring S] [CommSemiring T] (f : R →+* S) (g : S →+* T)
    (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    hasseDeriv d (map g (map f P)) = map (g.comp f) (hasseDeriv d P) := by
  simp [map_map]

-- (5) The typical call-site shape (evaluation of a coefficient-changed Hasse derivative,
-- cf. Roth/MainLemma.lean:489), closed by `simp` once the lemma is a simp lemma.
attribute [local simp] hasseDeriv_map in
example {S : Type*} [CommRing S] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) (z : σ → S) :
    eval z (hasseDeriv d (map (Int.castRingHom S) P)) =
      eval₂ (Int.castRingHom S) z (hasseDeriv d P) := by
  simp [eval_map]

end MvPolynomial
