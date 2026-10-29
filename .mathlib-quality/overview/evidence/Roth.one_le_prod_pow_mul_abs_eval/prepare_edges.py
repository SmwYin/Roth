exec(open('/private/tmp/roth-overview/assess/Roth.one_le_prod_pow_mul_abs_eval/prepare_probes.py').read().split('s=(D/')[0])
prefix=(D/'isolated-prefix.lean.txt').read_text()+'\nopen MvPolynomial\n#check_failure Roth.one_le_prod_pow_mul_abs_eval\nnamespace Integer279\n'
g=(D/'generic-body.lean.txt').read_text()
edge='''
-- A zero denominator invalidates the original conclusion even for Q=1.
example : eval (fun _ : Fin 1 ↦ (0 : ℝ) / 0)
    (map (Int.castRingHom ℝ) (1 : MvPolynomial (Fin 1) ℤ)) ≠ 0 ∧
    ¬ (1 ≤ (∏ _j : Fin 1, (0 : ℝ) ^ (1 : ℕ)) *
      |eval (fun _ : Fin 1 ↦ (0 : ℝ) / 0)
        (map (Int.castRingHom ℝ) (1 : MvPolynomial (Fin 1) ℤ))|) := by
  norm_num
-- Nonvanishing cannot be dropped.
example : ¬ (1 ≤ (∏ _j : Fin 1, (1 : ℝ) ^ (1 : ℕ)) *
    |eval (fun _ : Fin 1 ↦ (0 : ℝ))
      (map (Int.castRingHom ℝ) (0 : MvPolynomial (Fin 1) ℤ))|) := by
  norm_num
-- Degree bounds cannot be dropped: X squared evaluated at 1/2 with r=1.
example : eval (fun _ : Fin 1 ↦ (1 : ℝ) / 2)
    (map (Int.castRingHom ℝ) ((X 0)^2 : MvPolynomial (Fin 1) ℤ)) ≠ 0 ∧
    ¬ (1 ≤ (∏ _j : Fin 1, (2 : ℝ) ^ (1 : ℕ)) *
      |eval (fun _ : Fin 1 ↦ (1 : ℝ) / 2)
        (map (Int.castRingHom ℝ) ((X 0)^2 : MvPolynomial (Fin 1) ℤ))|) := by
  norm_num
-- Empty-variable recovery needs no nonemptiness assumption.
example (Q : MvPolynomial (Fin 0) ℤ) {r : Fin 0 → ℕ}
    (h : Fin 0 → ℤ) {q : Fin 0 → ℕ}
    (hne : eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0) :
    1 ≤ (∏ j, (q j : ℝ) ^ r j) *
      |eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q)| :=
  generic Q (fun j ↦ Fin.elim0 j) h (fun j ↦ Fin.elim0 j) hne
-- Rational coefficients invalidate the separated integer image bound.
example : ¬ ((1 : ℝ) ≤ |((1 / 2 : ℚ) : ℝ)|) := by norm_num
'''
write('edges-executed.lean.txt',prefix+g+edge+'\nend Integer279\n');req('edges01','edges-executed.lean.txt')
gs=(D/'signed-body.lean.txt').read_text()
clearing=gs[:gs.index(':= by')]+':= by'+gs[gs.index(':= by')+len(':= by'):gs.index('  have h1')]+ '  exact ⟨N, hNeq⟩\n'
start=clearing.index('    (hne :');end=clearing.index(':= by')
clearing=clearing[:start]+'''    : ∃ N : ℤ, (N : K) = (∏ j, (q j : K) ^ r j) *
      eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) '''+clearing[end:]
clearing=clearing.replace('theorem signed','theorem clearing').replace('[LinearOrder K]\n    [IsStrictOrderedRing K]','[CharZero K]')
# remove product nonzero declaration, since only equality is at issue.
a=clearing.index('  have hP');b=clearing.index('  set N',a);clearing=clearing[:a]+clearing[b:]
write('clearing-body.lean.txt',clearing)
norm='''
theorem separatedNorm {ι K : Type*} [Fintype ι] [NormedField K] [CharZero K]
    (Q : MvPolynomial ι ℤ) {r : ι → ℕ} (hQ : ∀ j, degreeOf j Q ≤ r j)
    (h : ι → ℤ) {q : ι → ℤ} (hq : ∀ j, q j ≠ 0)
    (hsep : ∀ z : ℤ, z ≠ 0 → 1 ≤ ‖(z : K)‖)
    (hne : eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q) ≠ 0) :
    1 ≤ ‖∏ j, (q j : K) ^ r j‖ *
      ‖eval (fun j ↦ (h j : K) / q j) (map (Int.castRingHom K) Q)‖ := by
  obtain ⟨N, hN⟩ := clearing Q hQ h hq
  have hP : (∏ j, (q j : K) ^ r j) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun j _ ↦ pow_ne_zero _ (Int.cast_ne_zero.mpr (hq j))
  have hNz : N ≠ 0 := Int.cast_ne_zero.mp (hN.symm ▸ mul_ne_zero hP hne)
  simpa only [hN, norm_mul] using hsep N hNz
#print axioms clearing
#print axioms separatedNorm
'''
write('clearing-executed.lean.txt',prefix+clearing+norm+'\nend Integer279\n');req('clearing01','clearing-executed.lean.txt')
print('Prepared edge guards and separate algebraic clearing/separated norm diagnostics')
