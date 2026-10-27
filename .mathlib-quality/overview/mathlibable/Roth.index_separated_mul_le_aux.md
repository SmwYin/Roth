---
decl: Roth.index_separated_mul_le_aux
file: Roth/Theta.lean
line: 414
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private Step-3 helper of index_det_le bounding the index of U(x_1..x_{p-1}) V(x_p) by l Phi via index_mul, index_rename, index_mul_left_weights and index_le_Θ; built on project-only notions (Roth index, RSet, Θ, lem6Φ) absent from mathlib.
action: Keep as private helper for its single call site Roth/Theta.lean:491 (index_det_le); no change needed.
---

# Roth.index_separated_mul_le_aux

## Inventory entry

### `theorem Roth.index_separated_mul_le_aux`
- **Type**: `∀ {τ : Type*} [Fintype τ] {r : Option τ → ℕ}, (∀ j, 0 < r j) → ∀ {q : Option τ → ℕ} {h : Option τ → ℤ}, (∀ j, IsCoprime (h j) (q j : ℤ)) → ∀ {M : ℝ} {l : ℕ}, 0 < l → ∀ {U : MvPolynomial τ ℤ}, U ∈ RSet M (fun j ↦ l * r (some j)) → ∀ {V : Polynomial ℤ}, V ≠ 0 → V.natDegree ≤ l * r none → (∀ b, |(V.coeff b : ℝ)| ≤ M) → index (map (Int.castRingHom ℝ) (rename some U * Polynomial.aeval (X none : MvPolynomial (Option τ) ℤ) V)) (fun j ↦ (h j : ℝ) / q j) r ≤ l * lem6Φ q r M l`
- **What**: For a product F = U(x_1, …, x_{p-1}) · V(x_p) of an integer polynomial U ∈ ℛ_{p-1}(M; l r_1, …, l r_{p-1}) and a nonzero one-variable integer polynomial V of degree ≤ l r_p with coefficients bounded by M, the index of F at the point (h_j/q_j) with weights r is at most l Φ, where Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}). This is the source's Lemma 4-2 (additivity of the index for separated variables) combined with the definition of Θ as a supremum, Step 3 of eq. (17) in the proof of Lemma 6.
- **How**: Transport V to `V' : MvPolynomial Unit ℤ` via `(uniqueAlgEquiv ℤ Unit).symm` and show `V' ∈ RSet M (fun _ ↦ l * r none)` using `degreeOf_uniqueAlgEquiv_symm` and `MvPolynomial.coeff_uniqueAlgEquiv_symm`; rewrite `aeval (X none) V` as a `rename` with `aeval_X_eq_rename`, push `map` through with `_root_.map_mul`, `map_rename`; split the index with `index_mul` (nonzeroness via `map_injective`, `rename_injective`), drop the renamings with `index_rename` (injective `some` and the constant map `Unit → none`); bound each factor by `index_le_Θ` after rescaling weights with `index_mul_left_weights`, and finish with `div_le_iff₀'`, unfolding `lem6Φ` and `add_le_add`.
- **Hypotheses**: `hr0` (positive weights, needed by `index_mul`); `hh` (coprimality, needed by `index_le_Θ`); `hl : 0 < l` (to clear the `/ l` from `index_mul_left_weights`); `hU` membership in RSet; `hV`, `hVd`, `hVc` are the unpacked RSet conditions for V (stated for a `Polynomial ℤ` rather than an `MvPolynomial Unit ℤ`). All hypotheses are used. Section variable `[DecidableEq τ]` is omitted (`omit ... in`); `classical` is used inside.
- **Uses from project**: `Roth.RSet`, `Roth.index`, `Roth.lem6Φ`, `Roth.Θ` (via lem6Φ), `Roth.index_le_Θ`, `Roth.index_mul`, `Roth.index_rename`, `Roth.index_mul_left_weights`, `aeval_X_eq_rename` (Roth/Separation.lean:137), `degreeOf_uniqueAlgEquiv_symm` (Roth/Separation.lean:174), `MvPolynomial.coeff_uniqueAlgEquiv_symm` (Roth/Separation.lean:169)
- **Used by**: Roth/Theta.lean: `index_det_le` (l.468; `exact index_separated_mul_le_aux hr0 hh hl ⟨hU, hUd, hUc⟩ hV hVd hVc` at l.491). `grep -rn index_separated_mul_le_aux Roth/` returns only the definition (l.414) and this use. Transitively: `index_le_lem6` (l.556, via l.578) and `Θ_option_le` (Lemma 6, l.593), used at l.920 for Lemma 7.
- **Visibility**: private
- **Lines**: 414–451 (with `omit` line 413), proof length 31 lines
- **Notes**: Declared `private lemma` (recorded as theorem). No docstring (acceptable for a private helper). Name ends in `_aux`. Hypotheses on V mirror the RSet conditions; packaging V as an RSet member of `MvPolynomial Unit ℤ` is done inside the proof so the caller can work with `Polynomial ℤ`.

## Junk check (Step 8)
- Used anywhere? Yes, once: `index_det_le` (Roth/Theta.lean:491), on the main path to Lemma 6 (`Θ_option_le`).
- Wrapper of 1–2 mathlib calls? No. A 31-line proof combining four project index lemmas, the RSet/Θ supremum bound and a `Polynomial`→`MvPolynomial Unit` transport.
- Does mathlib have it? No. Mathlib has no notion of Roth's index, of the sets ℛ_m(B; r) or of Θ. `lean_leansearch` ("index of product of polynomials in disjoint sets of variables at a rational point bounded by sum of suprema") returned only `AddMonoidAlgebra.supDegree_prod_le`, `MvPolynomial.vars_mul`, `schwartz_zippel_sup_sum`, `support_mul`, `degreeOf_mul_le` — none relevant. `grep -rn "Roth's index\|Roth index"` in mathlib: no hits.
- Too specific / inline? It is specific to the proof of Lemma 6, but inlining it into `index_det_le` would make that proof ~30 lines longer and mix the coefficient-bound steps (1–2) with the index computation (step 3). The split mirrors the source's structure (eq. (17)) and is sensible.
- Well-chosen? Yes. Taking `hU` as RSet membership and V's conditions unpacked matches what the caller has. Minor possible tidy: state V's hypotheses as a single RSet-like membership, but the caller builds them separately, so no gain.
- Conclusion: `KEEP` — action: keep as private helper for `index_det_le`; no change.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:414). The Step 9a pre-filter also fires on the name suffix `_aux`. In any case it is built on project-only definitions (`index`, `RSet`, `Θ`, `lem6Φ`) with no mathlib counterpart.

## Evidence
- `grep -rn index_separated_mul_le_aux Roth/`: definition l.414, single use l.491 (in `index_det_le`, l.468); `index_det_le` used at l.578 (`index_le_lem6`), which feeds `Θ_option_le` (l.593, used l.920).
- Project identifier lookups by grep over `Roth/`: `RSet` (Theta.lean:56), `Θ` (Theta.lean:68), `index_le_Θ` (Theta.lean:99), `lem6Φ` (Theta.lean:275), `index` (Index.lean:58), `index_mul` (Index.lean:162), `index_mul_left_weights` (Index.lean:200), `index_rename` (Index.lean:212), `aeval_X_eq_rename` (Separation.lean:137), `coeff_uniqueAlgEquiv_symm` (Separation.lean:169), `degreeOf_uniqueAlgEquiv_symm` (Separation.lean:174).
- `lean_leansearch` (query above, 5 results): nothing relevant.
- No Lean runs and no evidence Lean files (no weakening or proof experiments needed for a private SKIP; the project builds clean so the lemma compiles as stated).
