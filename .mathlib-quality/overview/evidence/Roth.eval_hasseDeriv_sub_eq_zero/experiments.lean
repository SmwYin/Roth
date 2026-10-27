import Roth.CoeffNorm
import Mathlib.Algebra.Polynomial.Div

/-! Evidence for `Roth.eval_hasseDeriv_sub_eq_zero` (overview run). -/

open MvPolynomial

namespace Roth.Evidence

/-- (1) Generic core: congruence mod `f` (via `%ₘ`, no monicity) gives equal values at roots of
`f`. Pure 3-lemma composition of mathlib. -/
example {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] {f g h : Polynomial R} {α : S}
    (hfα : Polynomial.aeval α f = 0) (hgh : g %ₘ f = h %ₘ f) :
    Polynomial.aeval α (g - h) = 0 :=
  Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero
    (Polynomial.dvd_modByMonic_iff_dvd.mp (by simp [Polynomial.sub_modByMonic, hgh])) hfα

/-- (2) The declaration re-proved verbatim from the source (baseline). -/
example {σ : Type*} {S : Type*} [CommRing S] {f : Polynomial ℤ} {α : S}
    (hfα : Polynomial.aeval α f = 0) {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ}
    (h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f) :
    eval (fun _ ↦ α) (hasseDeriv j (map (Int.castRingHom S) (W' - W''))) = 0 := by
  have hdvd : f ∣ diag (hasseDeriv j (W' - W'')) := by
    apply Polynomial.dvd_modByMonic_iff_dvd.mp
    simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]
  simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def, diag,
    MvPolynomial.comp_aeval_apply, Polynomial.aeval_X] using
    Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero hdvd hfα

-- (3) Weakening probe: `Int.castRingHom S` needs `NonAssocRing S` and `eval` needs
-- `CommSemiring S`, so `CommRing S` is already minimal.
#check @Int.castRingHom

end Roth.Evidence
