
namespace LaurentSeries

section

/-- `R⸨X⸩` is notation for `LaurentSeries R`. -/
scoped notation:9000 R "⸨X⸩" => LaurentSeries R

end

section HasseDeriv

/-- The Hasse derivative of Laurent series, as a linear map. -/
def hasseDeriv (R : Type*) {V : Type*} [AddCommGroup V] [Semiring R] [Module R V] (k : ℕ) :
    V⸨X⸩ →ₗ[R] V⸨X⸩ where
  toFun f := HahnSeries.ofSuppBddBelow (fun n ↦ Ring.choose (n + k) k • f.coeff (n + k)) <| by
    refine ⟨f.order - k, fun x h ↦ ?_⟩
    contrapose! h
    rw [Function.notMem_support, coeff_eq_zero_of_lt_order <| lt_sub_iff_add_lt.mp h, smul_zero]
  map_add' f g := by
    ext
    simp only [ofSuppBddBelow, coeff_add', Pi.add_apply, smul_add]
  map_smul' r f := by
    ext
    simp only [ofSuppBddBelow, HahnSeries.coeff_smul, RingHom.id_apply, smul_comm r]
