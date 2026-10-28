# coding: utf-8
from pathlib import Path
p=Path('/private/tmp/roth-overview/assess/Roth.\u0398_equiv')
s=(p/'probe-preparation.lean.txt').read_text().replace('elab "helper193" : term =>\n  Lean.Meta','elab "helper193" : term => do\n  return \u2190 Lean.Meta')
s=s.replace('Function.comp_def, Equiv.symm_apply_apply] using','Function.comp_def, Equiv.apply_symm_apply] using')
a=s.index('lemma fullBridge');b=s.index('  apply congrArg sSup',a)
s=s[:a]+'''lemma inclusion193 {ι κ : Type*} [Fintype ι] [Fintype κ] (e : ι ≃ κ) (B : ℝ)
    (q r : κ → ℕ) : Roth.indexSet B (q ∘ e) (r ∘ e) ⊆ Roth.indexSet B q r := by
  rintro _ ⟨R, ⟨hR0, hRd, hRc⟩, h, hh, rfl⟩
  refine ⟨rename e R, ⟨?_, ?_, ?_⟩, h ∘ e.symm, ?_, ?_⟩
  · simpa [rename_eq_zero_iff_of_injective R e.injective] using hR0
  · intro j
    obtain ⟨i, rfl⟩ := e.surjective j
    simpa only [degreeOf_rename_of_injective e.injective, Function.comp_apply] using hRd i
  · intro d
    obtain ⟨d, rfl⟩ := Finsupp.mapDomain_surjective e.surjective d
    simpa only [coeff_rename_mapDomain _ e.injective] using hRc d
  · intro j
    simpa only [Function.comp_apply, Equiv.apply_symm_apply] using hh (e.symm j)
  · simp only [map_rename, Roth.index_rename e.injective, Function.comp_def,
      Equiv.symm_apply_apply]
lemma fullBridge {σ τ : Type*} [Fintype σ] [Fintype τ] (e : σ ≃ τ) (B : ℝ)
    (q r : τ → ℕ) : Roth.Θ B (q ∘ e) (r ∘ e) = Roth.Θ B q r := by
'''+s[b:]
s=s.replace('(inclusion e q r)','(inclusion193 e B q r)').replace('inclusion e.symm','inclusion193 e.symm B')
(p/'probe-revised-preparation.lean.txt').write_text(s)
c=(p/'caller-preparation.lean.txt').read_text().replace(': term =>\n  Lean.Meta',': term => do\n  return \u2190 Lean.Meta')
(p/'caller-preparation.lean.txt').write_text(c)
