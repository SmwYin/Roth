lemma mapDomain_tsub {f : ι → κ} (h : f.Injective) (f1 f2 : ι →₀ α) :
    (f1 - f2).mapDomain f = f1.mapDomain f - f2.mapDomain f := by
  ext y
  by_cases! hy : y ∉ Set.range f
  · simp [mapDomain_of_notMem_range _ _ hy]
  · obtain ⟨x, rfl⟩ := hy
    simp [h]

lemma embDomain_tsub (f : ι ↪ κ) (f1 f2 : ι →₀ α) :
    (f1 - f2).embDomain f = f1.embDomain f - f2.embDomain f := by
  simp_rw [embDomain_eq_mapDomain, mapDomain_tsub f.injective]
