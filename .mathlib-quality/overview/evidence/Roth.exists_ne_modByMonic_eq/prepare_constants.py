from pathlib import Path
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth')
t=(D/'target-excerpt.lean.txt').read_text().rstrip()
sig=t.split(':= by',1)[0].replace('theorem exists_ne_modByMonic_eq','theorem noFiniteConstants').replace(' [Finite (Function.support r)]','')
finite=t.replace('theorem exists_ne_modByMonic_eq {σ : Type*}','have finiteCase',1)
s=(D/'disk-prefix.lean.txt').read_text()+'namespace Collision249Constants\nopen Roth MvPolynomial\n'+sig+''' := by
  classical
'''+''.join('  '+line+'\n'for line in finite.splitlines())+'''
  by_cases hfin : Finite (Function.support r)
  · let : Finite (Function.support r) := hfin
    exact finiteCase r B hf J C hC hcount
  · have hinf : (Function.support r).Infinite := fun h ↦ hfin (Set.finite_coe_iff.mpr h)
    have hp : ∏ᶠ j, (r j + 1) = 1 := finprod_of_infinite_mulSupport (by
      simpa [Function.mulSupport, Function.support] using hinf)
    have liftMem {W : MvPolynomial σ ℤ} (hW : W ∈ boxFamily (fun _ ↦ 0) B) :
        W ∈ boxFamily r B :=
      ⟨fun j ↦ (hW.1 j).trans (Nat.zero_le _), hW.2⟩
    obtain ⟨W', hW', W'', hW'', hne, he⟩ := finiteCase (fun _ ↦ 0) B hf J C
      (fun W hW ↦ hC W (liftMem hW)) (by simpa [hp] using hcount)
    exact ⟨W', liftMem hW', W'', liftMem hW'', hne, he⟩
end Collision249Constants
#print axioms Collision249Constants.noFiniteConstants
'''
# Avoid blank lines within the local finiteCase and outer proof.
s=s.replace('        (g (⟨j, hj⟩, i) : ℤ)) h\n\n  by_cases','        (g (⟨j, hj⟩, i) : ℤ)) h\n  by_cases')
assert max(map(len,s.splitlines()))<=100
(D/'constants-executed.lean.txt').write_text(s);(R/'.lake/roth-overview-session/GenWronskianChecks.lean').write_text(s)
print(s)
