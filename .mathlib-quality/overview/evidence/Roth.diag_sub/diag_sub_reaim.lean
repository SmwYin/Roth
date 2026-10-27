import Roth.MainLemma

namespace Roth
open MvPolynomial

-- (1) Re-aimed general form: diag = aeval (fun _ ↦ X) is an AlgHom, so subtraction is `map_sub`
-- over any CommRing (no project lemma needed).
example {σ R : Type*} [CommRing R] (P Q : MvPolynomial σ R) :
    aeval (fun _ ↦ (Polynomial.X : Polynomial R)) (P - Q) =
      aeval (fun _ ↦ Polynomial.X) P - aeval (fun _ ↦ Polynomial.X) Q :=
  map_sub _ _ _

-- (2) The exact project statement is `map_sub` (its current proof).
example {σ : Type*} (P Q : MvPolynomial σ ℤ) : diag (P - Q) = diag P - diag Q :=
  map_sub _ _ _

-- (3) The unique call site (Roth/MainLemma.lean:408) without `diag_sub`: unfold `diag`.
example {σ : Type*} {S : Type*} [CommRing S] {f : Polynomial ℤ} {α : S}
    (hfα : Polynomial.aeval α f = 0) {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ}
    (h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f) :
    eval (fun _ ↦ α) (hasseDeriv j (map (Int.castRingHom S) (W' - W''))) = 0 := by
  have hdvd : f ∣ diag (hasseDeriv j (W' - W'')) := by
    apply Polynomial.dvd_modByMonic_iff_dvd.mp
    simp only [diag] at h ⊢
    simp [map_sub, Polynomial.sub_modByMonic, h]
  simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def, diag,
    MvPolynomial.comp_aeval_apply, Polynomial.aeval_X] using
    Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero hdvd hfα

end Roth
