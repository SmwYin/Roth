from pathlib import Path
D=Path(__file__).resolve().parent;R=Path.cwd()
s=(D/'project-executed.lean.txt').read_text()
extra='''
namespace Box245Composition
open MvPolynomial
open Classical in
theorem existing_image_law {σ : Type*} (s : Finset (σ →₀ ℕ))
    (t : (σ →₀ ℕ) → Finset ℤ) :
    (AddMonoidAlgebra.ofCoeff '' (↑(s.finsupp t) : Set ((σ →₀ ℕ) →₀ ℤ))).Finite :=
  (s.finsupp t).finite_toSet.image _

theorem original_absence_probe {σ : Type*} (r : σ → ℕ)
    [Finite (Function.support r)] (B : ℕ) : (Roth.boxFamily r B).Finite := by
  fail_if_success exact (Finset.finite_toSet _).image _
  fail_if_success solve | simp only [Roth.boxFamily]
  exact Box245Project.finite_original r B

run_cmd do
  let ci ← Lean.getConstInfo `Box245Project.exists_ne_modByMonic_eq
  let some v := ci.value? (allowOpaque := true) | throwError "BOX245_NO_INLINE_BODY"
  if v.getUsedConstants.contains `Roth.boxFamily_finite then
    throwError "BOX245_INLINE_STILL_USES_TARGET"
  let helper := Lean.mkPrivateNameCore `Roth.MainLemma `Roth.boxFamily_eq_image_finsupp_aux
  unless v.getUsedConstants.contains helper do
    throwError "BOX245_INLINE_MISSING_PRIVATE_BRIDGE"
  Lean.logInfo "BOX245_INLINE: direct_target=false; private_representation=true; full_caller=true"

#print axioms existing_image_law
#print axioms original_absence_probe
end Box245Composition
'''
s+=extra
assert max(map(len,s.splitlines()))<=100
(D/'composition-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print(extra)
