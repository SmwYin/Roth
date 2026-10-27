---
decl: Roth.index_unique_le_log_div
file: Roth/Theta.lean
line: 223
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private 22-line single-variable step of Lemma 5 converting q^t ≤ B (pow_rootMultiplicity_le) into ind ≤ log B / (r log q) via index_unique and a Q-to-R rootMultiplicity transfer; about the project-local index, used once.
action: Keep as private helper for its single call site Roth/Theta.lean:259 (Θ_unique_le); nothing upstream.
---

# Roth.index_unique_le_log_div

## Inventory entry

### `theorem Roth.index_unique_le_log_div`
- **Type**: `∀ {σ : Type u_1} [Fintype σ] [Unique σ] {B : ℝ} {q r : σ → ℕ}, 1 < q default → ∀ {R : MvPolynomial σ ℤ}, R ≠ 0 → |((uniqueAlgEquiv ℤ σ R).leadingCoeff : ℝ)| ≤ B → ∀ {h : σ → ℤ}, IsCoprime (h default) (q default : ℤ) → index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Real.log B / (r default * Real.log (q default))`
- **What**: In one variable, if `R ∈ ℤ[X]` is nonzero with `|lc(R)| ≤ B`, and `h/q` is in lowest terms with `q > 1`, then `ind(R; h/q; r) ≤ log B / (r log q)`. This is the per-polynomial bound behind Lemma 5.
- **How**: Let `R1 := uniqueAlgEquiv ℤ σ R`. `hmapeq` shows that mapping to ℝ commutes with `uniqueAlgEquiv`, by `ext` and `coeff_uniqueAlgEquiv`, `Polynomial.coeff_map`, `coeff_map`. `hmult` moves the root multiplicity at `h/q` from ℝ to ℚ via `Polynomial.eq_rootMultiplicity_map` (with `Rat.castHom ℝ`, `Rat.cast_injective`) and `Polynomial.map_map`. The project's `index_unique` (Roth/Index.lean:234) then rewrites the index as `rootMultiplicity / r default`. Applying `Real.log_le_log` to the project's `pow_rootMultiplicity_le` (`q^t ≤ B`) and then `Real.log_pow` gives `t log q ≤ log B`. The bound follows from `le_div_iff₀` with `Real.log_pos` and `div_le_div_of_nonneg_right`, closed by `simpa [div_div, mul_comm]`.
- **Hypotheses**: `hq : 1 < q default` is needed for `log q > 0` and, through `Nat.zero_lt_of_lt`, for `0 < q`. `hR : R ≠ 0` is needed by `index_unique` and `pow_rootMultiplicity_le`. `hRB` bounds only the leading coefficient of the one-variable polynomial, which is weaker than membership in `RSet`. `hh` gives coprimality at the single index only. `h` and `q` are functions on `σ` because `index` takes points `σ → ℝ`; only their values at `default` matter. The section's `[DecidableEq σ]` is omitted. None of the hypotheses is superfluous. If `r default = 0`, both sides are `0` because of division by zero in ℝ, so the statement still holds.
- **Uses from project**: `Roth.index`, `Roth.index_unique`, `Roth.pow_rootMultiplicity_le`, `MvPolynomial.coeff_uniqueAlgEquiv` (mathlib), `MvPolynomial.uniqueAlgEquiv` (mathlib). The project identifiers are `index`, `index_unique` and `pow_rootMultiplicity_le`.
- **Used by**: only Roth/Theta.lean:259, in `Roth.Θ_unique_le` (Lemma 5), through `Θ_le_of_forall_index_le`. `grep -rn index_unique_le_log_div Roth/` returns the definition (l.223) and that one use.
- **Visibility**: private
- **Lines**: 222–250 (`omit` on l.222, statement 223–227, proof 228–250), proof length 22 lines
- **Notes**: Declared `private lemma` (recorded as theorem) in `section Lemma5`. It has no docstring, which is acceptable for a private lemma. It implements the step from `B ≥ q_1^t` to `t/r_1 ≤ log B/(r_1 log q_1)` in §5, proof of Lemma 5.

## Junk check (Step 8)
- **Used anywhere?** Yes, once: `Θ_unique_le` (Roth/Theta.lean:259).
- **Wrapper of 1–2 mathlib calls?** No. It is a 22-line combination of two project lemmas (`index_unique`, `pow_rootMultiplicity_le`), a transfer of the scalar field (ℝ to ℚ) for `rootMultiplicity`, and real log arithmetic.
- **Does mathlib have it?** No. It is about the project-local `Roth.index`. `lean_leansearch` for "q ^ rootMultiplicity ≤ leading coefficient bound, log bound" returns only generic `Polynomial.rootMultiplicity` API (`rootMultiplicity_le_rootMultiplicity_of_dvd`, `rootMultiplicity_X_sub_C_pow`, ...). Nothing there matches.
- **Too specific (inline?)?** Inlining it into the term-mode `Θ_unique_le` would turn that one-liner into a 22-line tactic block. Keeping it as a separate private helper is the cleaner structure.
- **Well-chosen?** Yes. Stating it per polynomial with only a leading-coefficient bound decouples it from `RSet`, and the caller supplies that bound from `hR.2.2` in one line.
- **Conclusion:** `KEEP`. Keep it as the private helper for Roth/Theta.lean:259.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:223). Its content is also specific to the project's `index` and to the Roth Lemma 5 setting, so there is nothing to upstream.

## Evidence
- `grep -rn index_unique_le_log_div Roth/`: definition l.223, single use l.259.
- `lean_hover_info` at Roth/Theta.lean:223: confirmed the elaborated type recorded above.
- `lean_leansearch` (query in the junk check): no mathlib counterpart, only generic rootMultiplicity lemmas.
- I wrote no evidence file and ran no Lean beyond the persistent LSP queries above.
