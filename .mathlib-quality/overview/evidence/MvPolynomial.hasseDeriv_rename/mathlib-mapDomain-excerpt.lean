theorem prod_mapDomain_index [CommMonoid N] {f : α → β} {s : α →₀ M} {h : β → M → N}
    (h_zero : ∀ b, h b 0 = 1) (h_add : ∀ b m₁ m₂, h b (m₁ + m₂) = h b m₁ * h b m₂) :
    (mapDomain f s).prod h = s.prod fun a m => h (f a) m :=
  (prod_sum_index h_zero h_add).trans <| prod_congr fun _ _ => prod_single_index (h_zero _)

-- Note that in `prod_mapDomain_index`, `M` is still an additive monoid,
-- so there is no analogous version in terms of `MonoidHom`.
/-- A version of `sum_mapDomain_index` that takes a bundled `AddMonoidHom`,
rather than separate linearity hypotheses.
-/
@[simp]
theorem sum_mapDomain_index_addMonoidHom [AddCommMonoid N] {f : α → β} {s : α →₀ M}
    (h : β → M →+ N) : ((mapDomain f s).sum fun b m => h b m) = s.sum fun a m => h (f a) m :=
  sum_mapDomain_index (fun b => (h b).map_zero) (fun b _ _ => (h b).map_add _ _)

theorem embDomain_eq_mapDomain (f : α ↪ β) (v : α →₀ M) : embDomain f v = mapDomain f v := by
  ext a
  by_cases h : a ∈ Set.range f
  · rcases h with ⟨a, rfl⟩
    rw [mapDomain_apply_of_injective f.injective, embDomain_apply_self]
  · rw [mapDomain_of_notMem_range, embDomain_of_notMem_range] <;> assumption

@[to_additive]
theorem prod_mapDomain_index_inj [CommMonoid N] {f : α → β} {s : α →₀ M} {h : β → M → N}
    (hf : Function.Injective f) : (s.mapDomain f).prod h = s.prod fun a b => h (f a) b := by
  rw [← Function.Embedding.coeFn_mk f hf, ← embDomain_eq_mapDomain, prod_embDomain]

theorem mapDomain_injective {f : α → β} (hf : Function.Injective f) :
    Function.Injective (mapDomain f : (α →₀ M) → β →₀ M) := by
  intro v₁ v₂ eq
  ext a
  have : mapDomain f v₁ (f a) = mapDomain f v₂ (f a) := by rw [eq]
  rwa [mapDomain_apply_of_injective hf, mapDomain_apply_of_injective hf] at this

