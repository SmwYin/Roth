import Roth.HasseDeriv

open MvPolynomial Nat

namespace MvPolynomial

variable {σ R : Type*} [CommSemiring R]

/-- (1) Operator form, matching the shape of `Polynomial.factorial_smul_hasseDeriv`. -/
example (j : σ) (n : ℕ) :
    ⇑((n ! : R) • hasseDeriv (σ := σ) (R := R) (Finsupp.single j n)) =
      (⇑(pderiv (R := R) j))^[n] := by
  funext P
  exact factorial_smul_hasseDeriv_single j n P

/-- (2) Generalisation to an arbitrary base multi-index `d`:
`∂_j^n Δ_d = n! * C(d_j + n, n) • Δ_{d + n e_j}`; the project lemma is the case `d = 0`. -/
theorem iterate_pderiv_hasseDeriv (j : σ) (n : ℕ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (⇑(pderiv (R := R) j))^[n] (hasseDeriv d P) =
      ((n ! * (d j + n).choose n : ℕ) : R) • hasseDeriv (d + Finsupp.single j n) P := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply', ih, Derivation.map_smul, pderiv_hasseDeriv, smul_smul,
      add_assoc d, ← Finsupp.single_add, Finsupp.add_apply, Finsupp.single_eq_same, ← Nat.cast_mul]
    congr 2
    have h := Nat.add_one_mul_choose_eq (d j + n) n
    rw [Nat.factorial_succ, show d j + (n + 1) = d j + n + 1 by omega]
    calc n ! * (d j + n).choose n * (d j + n + 1) = n ! * ((d j + n + 1) * (d j + n).choose n) := by ring
      _ = (n + 1) * n ! * (d j + n + 1).choose (n + 1) := by rw [h]; ring

/-- (2') The project lemma recovered from (2) at `d = 0`. -/
example (j : σ) (n : ℕ) (P : MvPolynomial σ R) :
    (n ! : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv (R := R) j))^[n] P := by
  have := iterate_pderiv_hasseDeriv (R := R) j n 0 P
  simpa [hasseDeriv_zero_apply] using this.symm

end MvPolynomial
