  exact_mod_cast abs_sub_le_of_nonneg_of_le (h'.2 d).1 (h'.2 d).2 (h''.2 d).1 (h''.2 d).2

/-- If `Δ_j W'(x, …, x) ≡ Δ_j W''(x, …, x) mod f` and `f(α) = 0`, then `Δ_j (W' - W'')`
vanishes at `(α, …, α)`.
The variables may be arbitrary, and evaluation may take values in any commutative ring.

Source: §6, proof of Lemma 9 ("For all `j` satisfying (44), `Δ_j W^*(x_1, …, x_m)` are zero
when `x_1 = ⋯ = x_m = α`"). -/
theorem eval_hasseDeriv_sub_eq_zero {σ : Type*} {S : Type*} [CommRing S] {f : Polynomial ℤ} {α : S}
    (hfα : Polynomial.aeval α f = 0) {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ}
    (h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f) :
    eval (fun _ ↦ α) (hasseDeriv j (map (Int.castRingHom S) (W' - W''))) = 0 := by
  have hdvd : f ∣ diag (hasseDeriv j (W' - W'')) := by
    apply Polynomial.dvd_modByMonic_iff_dvd.mp
    simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]
  simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def, diag,
    MvPolynomial.comp_aeval_apply, Polynomial.aeval_X] using
    Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero hdvd hfα

/-- Vanishing of box Hasse derivatives of weight `< c` gives the lower bound `c` on the index.
