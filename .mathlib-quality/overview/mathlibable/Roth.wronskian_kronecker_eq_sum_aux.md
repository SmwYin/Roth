---
decl: Roth.wronskian_kronecker_eq_sum_aux
file: Roth/GenWronskian.lean
line: 238
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-use helper of exists_genWronskian_ne_zero expanding the univariate Wronskian of Kronecker substitutions into a K[t]-combination of Kronecker images of generalized Wronskians, via det_sum_rows and AlgHom.map_det; mathlib has no Kronecker substitution or generalized Wronskian.
action: Keep as private helper for its single call site Roth/GenWronskian.lean:268 (exists_genWronskian_ne_zero); optional cosmetic inlining there is not recommended; if Lemma 1 is ever upstreamed, carry it along with det_sum_rows.
---

# Roth.wronskian_kronecker_eq_sum_aux

## Inventory entry

### `theorem Roth.wronskian_kronecker_eq_sum_aux`
- **Type**: `∀ {K : Type*} [Field K] {σ : Type*} [Fintype σ] {l : ℕ} (k : ℕ) (φ : Fin l → MvPolynomial σ K) (s : Fin l → Finset (σ →₀ ℕ)) (c : Fin l → (σ →₀ ℕ) → Polynomial K), (∀ μ ν : Fin l, Polynomial.hasseDeriv ↑μ (kronecker k (φ ν)) = ∑ d ∈ s μ, c μ d * kronecker k (hasseDeriv d (φ ν))) → wronskian (fun ν ↦ kronecker k (φ ν)) = ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * kronecker k (genWronskian f φ)` (declared `private lemma`).
- **What**: If, for every row index `μ` and every `ν`, the `μ`-th Hasse derivative of the Kronecker substitution `φ_ν(t, t^k, t^{k^2}, …)` is the `K[t]`-combination `∑_{d ∈ s μ} c μ d · kronecker k (Δ_d φ_ν)`, then the (Hasse) Wronskian of the substituted family equals `∑_f (∏_μ c μ (f μ)) · kronecker k (W(φ; Δ_{f 0}, …, Δ_{f (l-1)}))`, the sum running over choice functions `f` with `f μ ∈ s μ`. This is the "multilinearity of the determinant in each row" step of the source's proof of Lemma 1 (§2).
- **How**: `classical` then a single `simpa [wronskian, wronskianMatrix, hc, genWronskian, AlgHom.map_det, Matrix.map] using det_sum_rows s c (fun μ d ν ↦ kronecker k (hasseDeriv d (φ ν)))`. Unfolding `wronskian`/`wronskianMatrix` and rewriting each entry with `hc` puts the left side in the shape `det (of fun μ ν ↦ ∑_{d ∈ s μ} c μ d * N μ d ν)`, which is the left side of the project lemma `Roth.det_sum_rows`; on the right, `genWronskian` is unfolded and mathlib's `AlgHom.map_det` (with `Matrix.map`) pushes `kronecker k` inside the determinant so it matches `det (of fun μ ν ↦ N μ (f μ) ν)`.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` (both from the file `variable` line; `Fintype σ` is needed because `kronecker` sends `X_j ↦ t^{k^{equivFin j}}`). `hc` is the essential hypothesis (row expansion); it is exactly what `exists_hasseDeriv_kronecker_eq_sum` produces, specialised at `φ ν`. No `CharZero` needed here. No redundant hypotheses: all of `k, φ, s, c, hc` appear in the conclusion or are used.
- **Uses from project**: `Roth.wronskian` (Roth/Wronskian.lean:60), `Roth.wronskianMatrix` (Roth/Wronskian.lean:56), `Roth.kronecker` (Roth/GenWronskian.lean:53), `Roth.hasseDeriv` (Roth/HasseDeriv.lean:57), `Roth.genWronskian` (Roth/GenWronskian.lean:32), `Roth.det_sum_rows` (Roth/GenWronskian.lean:228). Mathlib: `Polynomial.hasseDeriv`, `Fintype.piFinset`, `AlgHom.map_det`, `Matrix.map`.
- **Used by**: Roth/GenWronskian.lean:268 `Roth.exists_genWronskian_ne_zero` (Lemma 1) only; `grep -rn wronskian_kronecker_eq_sum_aux Roth/` returns just the definition (l.238) and this use. Transitively everything downstream of Lemma 1.
- **Visibility**: private
- **Lines**: 238–245, proof length 3 lines
- **Notes**: Name ends in `_aux` (no docstring, as is usual for private helpers). Index-type subtlety: `hc` uses `Polynomial.hasseDeriv ↑μ` with the coercion `Fin l → ℕ`, matching `wronskianMatrix`'s row convention. The caller supplies `hc` as `fun μ ν ↦ hc μ (φ ν)` from `choose s c hs hc using … exists_hasseDeriv_kronecker_eq_sum`.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/GenWronskian.lean:268, inside the public `exists_genWronskian_ne_zero` (Lemma 1), where it rewrites `wronskian (kronecker ∘ φ)` before the final `Finset.sum_eq_zero`.
- Wrapper of 1–2 mathlib calls? No. It is one `simpa` combining the project lemma `det_sum_rows` with mathlib's `AlgHom.map_det` and unfolding of three project defs (`wronskian`, `wronskianMatrix`, `genWronskian`). Short, but it carries the identifiable mathematical step "expand the Wronskian row by row".
- Does mathlib have it? No. Mathlib has only the two-polynomial `Polynomial.wronskian` (Mathlib/RingTheory/Polynomial/Wronskian.lean); `lean_leansearch` ("Wronskian of Kronecker substitution of multivariate polynomials equals sum of generalized Wronskians") returned only `Polynomial.wronskian` and its 2-variable API lemmas. `grep -rli` over `.lake/packages/mathlib/Mathlib/` for "kronecker substitution", "genWronskian", "generalized wronskian" found nothing; "wronskian" occurs only in Polynomial/Wronskian.lean, Polynomial/Radical.lean and FLT/MasonStothers.lean (all 2-term). Since `kronecker`, `genWronskian` and the `l × l` Hasse Wronskian are project defs, the statement cannot exist in mathlib.
- Too specific / inline? Specific to Lemma 1's proof. It could be inlined at l.268 as a `have`/`rw` with the same `simpa`, but keeping it separate isolates the heavy `simpa` unfolding from the already long `exists_genWronskian_ne_zero` proof and gives the source step a name; it is already private. Inlining would be cosmetic, not a quality gain.
- Well-chosen? Yes: the statement is precisely the rewrite used by the caller, with the row expansion abstracted as hypothesis `hc` (so it does not depend on `CharZero` or on how `s, c` were obtained). Hypotheses are minimal.
- Conclusion: `KEEP`. Action: none; keep as private helper of `exists_genWronskian_ne_zero`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/GenWronskian.lean:238; the name also ends in `_aux`, which would trigger the Step 9a pre-filter anyway).

Note for the parent: if `exists_genWronskian_ne_zero` (Lemma 1) is ever upstreamed, this helper must come along together with `det_sum_rows`, `kronecker` and `genWronskian`, or be re-proved inline via `MultilinearMap.map_sum_finset` on `Matrix.detRowAlternating` plus `AlgHom.map_det`.

## Evidence
- `grep -rn wronskian_kronecker_eq_sum_aux Roth/`: definition l.238, single use l.268.
- `grep` for project defs: `genWronskian` Roth/GenWronskian.lean:32, `kronecker` Roth/GenWronskian.lean:53, `det_sum_rows` Roth/GenWronskian.lean:228, `hasseDeriv` Roth/HasseDeriv.lean:57, `wronskianMatrix` Roth/Wronskian.lean:56, `wronskian` Roth/Wronskian.lean:60.
- `lean_leansearch` (query above, 6 results): only `Polynomial.wronskian` (2-term) and its API; no match.
- `grep -rli` in mathlib for "kronecker substitution", "genWronskian", "generalized wronskian": no hits; "wronskian": only 2-term Wronskian files.
- Earlier report consulted: `.mathlib-quality/overview/mathlibable/Roth.det_sum_rows.md` (NO-composable-from-mathlib, single caller is this lemma).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
