| File:line | Caller | Actual code excerpt |
|---|---|---|
| `Roth/CoeffNorm.lean:136` | `Roth.abs_coeff_hasseDeriv_le` | `\|(((hasseDeriv d P).coeff e : ℤ) : ℝ)\| ≤ 2 ^ (∑ j, r j) * B := by` |
| `Roth/CoeffNorm.lean:149` | `Roth.normOne_hasseDeriv_le` | `(hP : ∀ j, degreeOf j P ≤ r j) : normOne (hasseDeriv d P) ≤ 2 ^ (∑ j, r j) * normOne P := by` |
| `Roth/CoeffNorm.lean:247` | `Roth.degreeOf_det_hasseDeriv_le` | `degreeOf j (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤ l * r j := by` |
| `Roth/CoeffNorm.lean:261` | `Roth.abs_coeff_det_hasseDeriv_le` | `\|(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)\| ≤` |
| `Roth/CoeffNorm.lean:265` | `Roth.abs_coeff_det_hasseDeriv_le` | `calc _ ≤ normOne (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det :=` |
| `Roth/GenWronskian.lean:34` | `Roth.genWronskian` | `(Matrix.of fun μ ν ↦ hasseDeriv (D μ) (φ ν)).det` |
| `Roth/GenWronskian.lean:49` | `Roth.genWronskian_eq_zero_of_not_linearIndependent` | `congrArg (hasseDeriv (D μ)) hg` |
| `Roth/GenWronskian.lean:146` | `Roth.kronHasse` | `fun P ↦ kronecker k (hasseDeriv d P)` |
| `Roth/GenWronskian.lean:216` | `Roth.exists_hasseDeriv_kronecker_eq_sum` | `Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P) := by` |
| `Roth/GenWronskian.lean:241` | `Roth.wronskian_kronecker_eq_sum_aux` | `∑ d ∈ s μ, c μ d * kronecker k (hasseDeriv d (φ ν))) : wronskian (fun ν ↦ kronecker k (φ ν)) =` |
| `Roth/GenWronskian.lean:245` | `Roth.wronskian_kronecker_eq_sum_aux` | `det_sum_rows s c (fun μ d ν ↦ kronecker k (hasseDeriv d (φ ν)))` |
| `Roth/HasseDeriv.lean:67` | `MvPolynomial.hasseDeriv_monomial` | `hasseDeriv d (monomial k a) = monomial (k - d) ((hasseCoeff d k : R) * a) := by` |
| `Roth/HasseDeriv.lean:68` | `MvPolynomial.hasseDeriv_monomial` | `simp [hasseDeriv]` |
| `Roth/HasseDeriv.lean:74` | `MvPolynomial.hasseDeriv_apply` | `hasseDeriv d P = ∑ k ∈ P.support, monomial (k - d) ((hasseCoeff d k : R) * P.coeff k) := by` |
| `Roth/HasseDeriv.lean:75` | `MvPolynomial.hasseDeriv_apply` | `simp [hasseDeriv, sum_def]` |
| `Roth/HasseDeriv.lean:90` | `MvPolynomial.coeff_hasseDeriv` | `(hasseDeriv d P).coeff e = (hasseCoeff d (e + d) : R) * P.coeff (e + d) := by` |
| `Roth/HasseDeriv.lean:112` | `MvPolynomial.hasseDeriv_zero_apply` | `theorem hasseDeriv_zero_apply (P : MvPolynomial σ R) : hasseDeriv 0 P = P := by` |
| `Roth/HasseDeriv.lean:120` | `MvPolynomial.hasseDeriv_zero` | `theorem hasseDeriv_zero : hasseDeriv (0 : σ →₀ ℕ) = (LinearMap.id : MvPolynomial σ R →ₗ[R] _) :=` |
| `Roth/HasseDeriv.lean:126` | `MvPolynomial.hasseDeriv_C` | `theorem hasseDeriv_C {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) : hasseDeriv d (C a) = 0 := by` |
| `Roth/HasseDeriv.lean:135` | `MvPolynomial.hasseDeriv_map` | `(P : MvPolynomial σ R) : hasseDeriv d (map f P) = map f (hasseDeriv d P) := by` |
| `Roth/HasseDeriv.lean:145` | `MvPolynomial.hasseDeriv_rename` | `hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P) := by` |
| `Roth/HasseDeriv.lean:176` | `MvPolynomial.hasseDeriv_hasseDeriv` | `hasseDeriv d (hasseDeriv e P) = (hasseCoeff d (d + e) : R) • hasseDeriv (d + e) P := by` |
| `Roth/HasseDeriv.lean:186` | `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` | `(P : MvPolynomial σ R) : hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := by` |
| `Roth/HasseDeriv.lean:201` | `MvPolynomial.pderiv_hasseDeriv` | `pderiv j (hasseDeriv d P) = ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P := by` |
| `Roth/HasseDeriv.lean:211` | `MvPolynomial.degreeOf_hasseDeriv_le` | `degreeOf j (hasseDeriv d P) ≤ degreeOf j P := by` |
| `Roth/HasseDeriv.lean:220` | `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt` | `(h : degreeOf j P < d j) : hasseDeriv d P = 0 := by` |
| `Roth/HasseDeriv.lean:226` | `MvPolynomial.hasseDeriv_monomial_mul` | `(g : MvPolynomial σ R) : hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g := by` |
| `Roth/HasseDeriv.lean:244` | `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` | `(hf : ∀ j ∈ d.support, degreeOf j f = 0) : hasseDeriv d (f * g) = f * hasseDeriv d g := by` |
| `Roth/HasseDeriv.lean:254` | `MvPolynomial.hasseDeriv_single_aeval_X` | `hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) =` |
| `Roth/HasseDeriv.lean:267` | `MvPolynomial.uniqueAlgEquiv_hasseDeriv` | `uniqueAlgEquiv R σ (hasseDeriv (R := R) (Finsupp.single (default : σ) n) P) =` |
| `Roth/HasseDeriv.lean:287` | `MvPolynomial.factorial_smul_hasseDeriv_single` | `(n.factorial : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv (R := R) j))^[n] P := by` |
| `Roth/Index.lean:63` | `Roth.mem_support_taylor_iff` | `d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0 := by` |
| `Roth/Index.lean:70` | `Roth.index_le_weight` | `(h : eval α (hasseDeriv d P) ≠ 0) : index P α r ≤ weight r d :=` |
| `Roth/Index.lean:77` | `Roth.exists_weight_eq_index` | `∃ d, eval α (hasseDeriv d P) ≠ 0 ∧ weight r d = index P α r := by` |
| `Roth/Index.lean:86` | `Roth.le_index_iff` | `c ≤ index P α r ↔ ∀ d, eval α (hasseDeriv d P) ≠ 0 → c ≤ weight r d := by` |
| `Roth/Index.lean:110` | `Roth.index_sub_weight_le_index_hasseDeriv` | `(hk : hasseDeriv k P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :` |
| `Roth/Index.lean:111` | `Roth.index_sub_weight_le_index_hasseDeriv` | `index P α r - weight r k ≤ index (hasseDeriv k P) α r := by` |
| `Roth/Index.lean:238` | `Roth.index_unique` | `have key (d : σ →₀ ℕ) : eval α (hasseDeriv d P) = q.coeff (d default) := by` |
| `Roth/Index.lean:240` | `Roth.index_unique` | `exact (eval₂_uniqueAlgEquiv (f := hasseDeriv d P) (φ := RingHom.id ℝ) (a := α)).symm` |
| `Roth/Main.lean:385` | `Roth.abs_eval_lt_of_le_index` | `(hC : ∀ i : Fin m →₀ ℕ, \|eval (fun _ ↦ α) (hasseDeriv i Q)\| < C) :` |
| `Roth/Main.lean:392` | `Roth.abs_eval_lt_of_le_index` | `have hterm : ∀ d ∈ box r, \|eval (fun _ ↦ α) (hasseDeriv d Q) *` |
| `Roth/Main.lean:395` | `Roth.abs_eval_lt_of_le_index` | `by_cases h0 : eval (fun _ ↦ α) (hasseDeriv d Q) = 0` |
| `Roth/MainLemma.lean:362` | `Roth.exists_ne_modByMonic_eq` | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ C)` |
| `Roth/MainLemma.lean:365` | `Roth.exists_ne_modByMonic_eq` | `∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f := by` |
| `Roth/MainLemma.lean:369` | `Roth.exists_ne_modByMonic_eq` | `⟨(diag (hasseDeriv p.1.1 W.1) %ₘ f).coeff p.2, abs_le.1 (hC W.1 W.2 p.1.1 p.1.2 p.2.1 p.2.2)⟩` |
| `Roth/MainLemma.lean:404` | `Roth.eval_hasseDeriv_sub_eq_zero` | `(h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f) :` |
| `Roth/MainLemma.lean:405` | `Roth.eval_hasseDeriv_sub_eq_zero` | `eval (fun _ ↦ α) (hasseDeriv j (map (Int.castRingHom S) (W' - W''))) = 0 := by` |
| `Roth/MainLemma.lean:406` | `Roth.eval_hasseDeriv_sub_eq_zero` | `have hdvd : f ∣ diag (hasseDeriv j (W' - W'')) := by` |
| `Roth/MainLemma.lean:421` | `Roth.le_index_of_forall_eval_eq_zero` | `(hvan : ∀ d, (∀ j, d j ≤ r j) → weight r d < c → eval α (hasseDeriv d P) = 0) :` |
| `Roth/MainLemma.lean:456` | `Roth.exists_hasseDeriv_eval_ne_zero` | `weight r k < c ∧ eval α (hasseDeriv k P) ≠ 0 :=` |
| `Roth/MainLemma.lean:462` | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | `: \|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\| <` |
| `Roth/MainLemma.lean:464` | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | `have hdQ : ∀ j, degreeOf j (hasseDeriv k P) ≤ r j := fun j ↦` |
| `Roth/MainLemma.lean:466` | `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | `have heval := abs_eval_le (hasseDeriv i (hasseDeriv k P))` |
| `Roth/MainLemma.lean:480` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `\|eval α (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\| < C)` |
| `Roth/MainLemma.lean:485` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `\|eval α (hasseDeriv i (map (Int.castRingHom ℝ) Q))\| < C := by` |
| `Roth/MainLemma.lean:488` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `have hQev : eval z (map (Int.castRingHom ℝ) (hasseDeriv k P)) ≠ 0 := by` |
| `Roth/MainLemma.lean:490` | `Roth.exists_hasseDeriv_index_eval_bound_aux` | `refine ⟨hasseDeriv k P, fun h0 ↦ hQev (by rw [h0, map_zero, map_zero]),` |
| `Roth/MainLemma.lean:500` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `\|((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)\| ≤ (1 + A) ^ ((∑ k, r k) + 1 - f.natDegree) *` |
| `Roth/MainLemma.lean:503` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `have hdP : ∀ k, degreeOf k (hasseDeriv j P) ≤ r k := fun k ↦` |
| `Roth/MainLemma.lean:505` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `have hsupp : ((hasseDeriv j P).support.card : ℝ) ≤ ((∏ k, (r k + 1) : ℕ) : ℝ) := by` |
| `Roth/MainLemma.lean:507` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `have hcD : ∀ k, \|((diag (hasseDeriv j P)).coeff k : ℝ)\| ≤` |
| `Roth/MainLemma.lean:519` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | `(j : σ →₀ ℕ) (i : ℕ) : \|(diag (hasseDeriv j P) %ₘ f).coeff i\| ≤ (⌊B * β ^ 3⌋₊ : ℤ) := by` |
| `Roth/MainLemma.lean:532` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | `\|((diag (hasseDeriv j P) %ₘ g).coeff i : ℝ)\| ≤ B * β ^ 3 := by` |
| `Roth/MainLemma.lean:538` | `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` | `have hreal : \|((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)\| ≤ B * β ^ 3 := by` |
| `Roth/MainLemma.lean:553` | `Roth.exists_mem_RSet_le_index_aux` | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ (C : ℤ))` |
| `Roth/MainLemma.lean:602` | `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ (Cn : ℤ) := by` |
| `Roth/MainLemma.lean:649` | `Roth.exists_auxiliary_polynomial_of_log_bound_aux` | `\|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k P)))\| <` |
| `Roth/MainLemma.lean:701` | `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | `\|eval (fun _ ↦ α) (map (Int.castRingHom ℝ) (hasseDeriv i (hasseDeriv k W)))\| <` |
| `Roth/MainLemma.lean:745` | `Roth.main_lemma` | `∀ i : Fin m →₀ ℕ, \|eval (fun _ ↦ α) (hasseDeriv i (map (Int.castRingHom ℝ) Q))\| <` |
| `Roth/Separation.lean:147` | `Roth.hasseDeriv_rename_mul_aeval` | `hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval` |
| `Roth/Separation.lean:148` | `Roth.hasseDeriv_rename_mul_aeval` | `(X none : MvPolynomial (Option τ) R) V) = rename some (hasseDeriv d U) * Polynomial.aeval` |
| `Roth/Separation.lean:353` | `Roth.det_hasseDeriv_separated` | `(Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ))` |
| `Roth/Separation.lean:514` | `Roth.exists_rat_factors_det_hasseDeriv_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *` |
| `Roth/Separation.lean:526` | `Roth.exists_rat_factors_det_hasseDeriv_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det with hFdef` |
| `Roth/Separation.lean:547` | `Roth.exists_det_eq_mul` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *` |
| `Roth/Taylor.lean:103` | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | `(ih : ∀ d, (taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a)))` |
| `Roth/Taylor.lean:105` | `MvPolynomial.coeff_taylor_monomial_single_add_aux` | `eval α (hasseDeriv d (monomial (Finsupp.single i n + k) a)) := by` |
| `Roth/Taylor.lean:121` | `MvPolynomial.coeff_taylor_monomial_aux` | `(taylor α (monomial k a)).coeff d = eval α (hasseDeriv d (monomial k a)) := by` |
| `Roth/Taylor.lean:135` | `MvPolynomial.coeff_taylor` | `(taylor α P).coeff d = eval α (hasseDeriv d P) := by` |
| `Roth/Taylor.lean:199` | `MvPolynomial.eq_sum_box_hasseDeriv` | `P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by` |
| `Roth/Taylor.lean:200` | `MvPolynomial.eq_sum_box_hasseDeriv` | `have h1 : taylor α P = ∑ d ∈ Roth.box r, monomial d (eval α (hasseDeriv d P)) := by` |
| `Roth/Taylor.lean:219` | `MvPolynomial.eval_eq_sum_box` | `eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by` |
| `Roth/Theta.lean:378` | `Roth.sum_max_sub_le_index_det` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det ≠ 0) (α : Option τ → ℝ)` |
| `Roth/Theta.lean:383` | `Roth.sum_max_sub_le_index_det` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det α r := by` |
| `Roth/Theta.lean:386` | `Roth.sum_max_sub_le_index_det` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R` |
| `Roth/Theta.lean:463` | `Roth.index_det_le` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` |
| `Roth/Theta.lean:466` | `Roth.index_det_le` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det)` |
| `Roth/Theta.lean:470` | `Roth.index_det_le` | `have hFcoef (d) : \|(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv` |
| `Roth/Theta.lean:514` | `Roth.mapped_det_ne_zero_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` |
| `Roth/Theta.lean:516` | `Roth.mapped_det_ne_zero_aux` | `(Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +` |
| `Roth/Theta.lean:519` | `Roth.mapped_det_ne_zero_aux` | `hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) R).det =` |
| `Roth/Theta.lean:520` | `Roth.mapped_det_ne_zero_aux` | `(Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some +` |
