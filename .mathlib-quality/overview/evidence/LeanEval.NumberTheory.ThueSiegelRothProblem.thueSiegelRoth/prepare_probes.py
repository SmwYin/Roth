exec((__import__('pathlib').Path(__file__).parent/'prepare.py').read_text().split("order=json.loads")[0])
P=D.parent/'LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff'
# Replay accepted292 generic bridge in a fresh namespace, unchanged written proof otherwise.
a=(P/'modern-executed.lean.txt').read_text()
a=a.replace('Equivalence292Modern','Endpoint293Bridge')
a=a.replace('LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine','LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth')
(D/'modern-executed.lean.txt').write_text(a);req('modern01','modern-executed.lean.txt',op='run_code')
prefix=(D/'disk-prefix.lean.txt').read_text()
code=prefix+'''\nnamespace Endpoint293Generality
open Real
open LeanEval.NumberTheory.ThueSiegelRothProblem
#check @IsFractionRing.isAlgebraic_iff
#check @IsAlgebraic.extendScalars
#check @Liouville.exists_pos_real_of_irrational_root
lemma algebraic_int_iff_rat (x : ℝ) : IsAlgebraic ℤ x ↔ IsAlgebraic ℚ x :=
  (IsFractionRing.isAlgebraic_iff ℤ ℚ ℝ).symm
-- Same mathematical hypothesis in the standard field spelling, not a strict weakening.
theorem endpoint_rat (x : ℝ) (hx : Irrational x) (ha : IsAlgebraic ℚ x) :
    IsDiophantine x := (isDiophantine_iff hx).mpr (Roth.roth hx ha)
theorem endpoint_finite (x : ℝ) (hx : Irrational x) (ha : IsAlgebraic ℚ x)
    (ε : ℝ) (hε : 0 < ε) : (Roth.approxSet x (2 + ε)).Finite := by
  exact Set.not_infinite.mp fun h ↦ (by linarith : ¬ (2 + ε ≤ 2)) (Roth.roth hx ha h)
theorem endpoint_weak (x : ℝ) (hx : Irrational x) (ha : IsAlgebraic ℚ x)
    (ε : ℝ) (hε : 0 < ε) : ∃ C : ℝ, 0 < C ∧ ∀ p q : ℤ, 0 < q →
      C / (q : ℝ) ^ (2 + ε) ≤ |x - (p : ℝ) / q| := by
  obtain ⟨C, hC, hb⟩ := endpoint_rat x hx ha ε hε
  exact ⟨C, hC, fun p q hq ↦ (hb p q hq).le⟩
lemma diophantine_irrational {x : ℝ} (h : IsDiophantine x) : Irrational x := by
  rintro ⟨r, rfl⟩
  obtain ⟨C, hC, hb⟩ := h 1 zero_lt_one
  have hp := hb r.num r.den (by exact_mod_cast r.den_pos)
  have heq : (r.num : ℝ) / r.den = (r : ℝ) := (Rat.cast_def r).symm
  simp only [Int.cast_natCast] at hp
  rw [heq, sub_self, abs_zero] at hp
  exact (div_pos hC (rpow_pos_of_pos (by positivity) _)).not_gt hp
lemma rational_counterexample (r : ℚ) : ¬ IsDiophantine (r : ℝ) := by
  intro h
  exact (diophantine_irrational h).ne_rat r rfl
example : IsAlgebraic ℤ (0 : ℝ) := isAlgebraic_zero
example : ¬ IsDiophantine (0 : ℝ) := by simpa using rational_counterexample 0
-- Exact original-signature recovery from the Q statement.
theorem recovered (x : ℝ) (_h_irr : Irrational x) (_h_alg : IsAlgebraic ℤ x) :
    IsDiophantine x := endpoint_rat x _h_irr ((algebraic_int_iff_rat x).mp _h_alg)
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Endpoint293Generality.recovered := Subsingleton.elim _ _
#print axioms Endpoint293Generality.endpoint_rat
#print axioms Endpoint293Generality.endpoint_finite
#print axioms Endpoint293Generality.endpoint_weak
#print axioms Endpoint293Generality.rational_counterexample
#print axioms Endpoint293Generality.recovered
end Endpoint293Generality
'''
assert max(map(len,code.splitlines()))<=100
(D/'generality-executed.lean.txt').write_text(code);req('generality01','generality-executed.lean.txt')
# Actual project-context modern endpoint: exact disk9 + sole newly authorized module.
start=a.index('namespace Endpoint293Bridge')
bridge=a[start:]
code='\n'.join(prefix.splitlines()[:9])+'\nimport Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith\n\n'+bridge+'''
namespace Endpoint293Modern
open Endpoint293Bridge
open LeanEval.NumberTheory.ThueSiegelRothProblem
lemma algebraic_family (x : ℝ) (hx : Irrational x) (ha : IsAlgebraic ℚ x) :
    Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ 2 := by
  exact ⟨hx, (exponent_iff hx).mp (Roth.roth hx ha)⟩
lemma algebraic_not_liouville {x p : ℝ} (ha : IsAlgebraic ℚ x) (hp : 2 < p) :
    ¬ LiouvilleWith p x := by
  intro h
  exact (not_le.mpr hp) ((algebraic_family x (h.irrational (by linarith)) ha).2 h)
lemma family_recovery (x : ℝ) (_h_irr : Irrational x) (_h_alg : IsAlgebraic ℤ x) :
    IsDiophantine x := by
  exact uniform_iff.mpr (algebraic_family x _h_irr
    (_h_alg.extendScalars (FaithfulSMul.algebraMap_injective ℤ ℚ)))
example : @LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth =
    @Endpoint293Modern.family_recovery := Subsingleton.elim _ _
lemma liouville_counterexample {x : ℝ} (hx : Liouville x) :
    Irrational x ∧ ¬ IsAlgebraic ℤ x ∧ ¬ IsDiophantine x := by
  exact ⟨hx.irrational, hx.transcendental, liouville_not_uniform hx⟩
lemma no_irrational_free_uniform :
    ¬ (∀ x : ℝ, IsAlgebraic ℤ x → IsDiophantine x) := by
  intro h
  exact (uniform_irrational (h 0 isAlgebraic_zero)).ne_rat 0 (by norm_num)
#print axioms Endpoint293Modern.algebraic_family
#print axioms Endpoint293Modern.algebraic_not_liouville
#print axioms Endpoint293Modern.family_recovery
#print axioms Endpoint293Modern.liouville_counterexample
#print axioms Endpoint293Modern.no_irrational_free_uniform
end Endpoint293Modern
'''
assert max(map(len,code.splitlines()))<=100
(D/'project-modern-executed.lean.txt').write_text(code);req('projectmodern01','project-modern-executed.lean.txt',op='run_code')
r=json.loads((D/'root-requests/projectmodern01.json').read_text());r['context']='project_endpoint293';dump('root-requests/projectmodern01.json',r)
# Mathlib-only endpoint absence/composition probes, no authored theorem helpers in scope.
p19='\n'.join(a.splitlines()[:19])+'\n'
code=p19+'''
#check_failure Roth.roth
#check_failure LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth
namespace Endpoint293Composition
open Real
def UniformBound (t x : ℝ) : Prop :=
  ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
    ∀ p q : ℤ, 0 < q → C / (q : ℝ) ^ (t + ε) < |x - (p : ℝ) / q|
def pairSet (α κ : ℝ) : Set (ℤ × ℕ) :=
  {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}
example (x : ℝ) (hx : Irrational x) (ha : IsAlgebraic ℤ x) : True := by
  fail_if_success
    have : UniformBound 2 x := by exact?
  fail_if_success
    have : UniformBound 2 x := by simp only [UniformBound]
  exact (fun (_ : Irrational x) (_ : IsAlgebraic ℤ x) ↦ True.intro) hx ha
example (x : ℝ) (hx : Irrational x) (ha : IsAlgebraic ℚ x) : True := by
  fail_if_success
    have : ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ 2 := by exact?
  fail_if_success
    have : Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ 2 := by exact?
  exact (fun (_ : Irrational x) (_ : IsAlgebraic ℚ x) ↦ True.intro) hx ha
#check @Liouville.exists_pos_real_of_irrational_root
#check @LiouvilleWith.exists_pos
#check @LiouvilleWith.frequently_lt_rpow_neg
#check @LiouvilleWith.irrational
#check @LiouvilleWith.add_rat_iff
#check @LiouvilleWith.mul_rat_iff
#print axioms Liouville.exists_pos_real_of_irrational_root
#print axioms LiouvilleWith.frequently_lt_rpow_neg
end Endpoint293Composition
'''
assert max(map(len,code.splitlines()))<=100
(D/'composition-executed.lean.txt').write_text(code);req('composition01','composition-executed.lean.txt',op='run_code')
print('Prepared modern01, generality01, projectmodern01, composition01')
