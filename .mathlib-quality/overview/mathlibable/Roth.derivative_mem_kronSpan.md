---
decl: Roth.derivative_mem_kronSpan
file: Roth/GenWronskian.lean
line: 162
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private span-induction step showing the K[t]-span kronSpan k mu is mapped into kronSpan k (mu+1) by pointwise d/dt; specific to the private kronHasse/kronSpan machinery of Lemma 1, no mathlib analogue.
action: Keep as private helper of hasseDeriv_kronecker_mem (Roth/GenWronskian.lean:202); if Lemma 1 is upstreamed, carry it with kronHasse/kronSpan/derivative_kronHasse_aux restated for the weighted substitution.
---

# Roth.derivative_mem_kronSpan

## Inventory entry

### `theorem Roth.derivative_mem_kronSpan`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K} (hF : F ∈ kronSpan k μ) : (fun P ↦ Polynomial.derivative (F P)) ∈ kronSpan k (μ + 1)`
- **What**: In the K[t]-module of functions MvPolynomial σ K → K[t], if F lies in the K[t]-span of the operators P ↦ kronecker k (Δ_d P) with |d| ≤ μ, then its pointwise t-derivative P ↦ (F P)' lies in the span of those with |d| ≤ μ + 1. This is the inductive step behind "d^μ/dt^μ h_ν is a K[t]-combination of Δ^{(i)}_μ φ_ν (γ(t)) with order ≤ μ" in §2, proof of Lemma 1.
- **How**: `Submodule.span_induction` on `hF`. Generator case: write the generator as `kronHasse k d` with `d.degree ≤ μ`, rewrite with the project lemma `derivative_kronHasse_aux`, close with `Submodule.sum_mem`, `Submodule.smul_mem`, `Submodule.subset_span` at index `d + Finsupp.single j 1` (degree bound by `map_add`, `Finsupp.degree_single`, `Nat.add_le_add_right`). Zero case: `zero_mem` after `funext`/`simp`. Add case: `Submodule.add_mem` plus `Polynomial.derivative_add`. Smul case (a • F): Leibniz `Polynomial.derivative_mul` splits into `a' • F + a • F'`; the first term lies in the span via `Submodule.span_mono` with `Set.image_mono` and `Nat.le_succ` (kronSpan k μ ≤ kronSpan k (μ+1)), the second by the induction hypothesis and `Submodule.smul_mem`.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` from section variables; `classical` for the Finsupp decidability. No condition on `k`, `μ`.
- **Uses from project**: `Roth.kronSpan` (Roth/GenWronskian.lean:149), `Roth.kronHasse` (l.145, via the generator image set), `Roth.derivative_kronHasse_aux` (l.153); implicitly `Roth.kronecker` and `MvPolynomial.hasseDeriv` through `kronHasse`.
- **Used by**: `grep -rn derivative_mem_kronSpan Roth/`: only `Roth.hasseDeriv_kronecker_mem` (Roth/GenWronskian.lean:202, `convert ... using 1` in the `succ` case). Transitively feeds `exists_hasseDeriv_kronecker_eq_sum` and Lemma 1 `exists_genWronskian_ne_zero`.
- **Visibility**: private
- **Lines**: 162–187, proof length 23 lines (l.165–187)
- **Notes**: The smul case re-derives the monotonicity kronSpan k μ ≤ kronSpan k (μ+1) inline via `Submodule.span_mono`; no separate monotonicity lemma exists in the project (it is used only here).

## Junk check (Step 8)
- Used anywhere? Yes, once: `hasseDeriv_kronecker_mem` l.202, the induction step of the Hasse-derivative-of-Kronecker statement.
- Wrapper of 1–2 mathlib calls? No: a four-case span induction combining the project lemma `derivative_kronHasse_aux` with Leibniz and span monotonicity.
- Does mathlib have it? No. `kronSpan`/`kronHasse` are project-private; mathlib has no Kronecker substitution or multivariate Hasse derivative. There is no generic mathlib lemma of the form "a derivation-like map sending generators into a submodule N, and with D(a • x) = D a • x + a • D x, sends span S into N" (grep of Mathlib/RingTheory/Derivation for span lemmas: no hits), so the argument cannot be replaced by a single library call.
- Too specific / inline? It could be inlined into the `succ` case of `hasseDeriv_kronecker_mem` (single use), but that would bury a 23-line span induction inside another induction; as a private lemma it costs nothing in the API.
- Well-chosen? Yes: stating membership for an arbitrary F in the span (rather than for the specific Hasse-derivative operator) is exactly what makes the outer induction on μ go through.
- Conclusion: `KEEP`. Action: none; keep as private helper of `hasseDeriv_kronecker_mem`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/GenWronskian.lean:162).

Note for an eventual upstreaming of Lemma 1: the parents `Roth.kronHasse` / `Roth.kronSpan` and the generator lemma `Roth.derivative_kronHasse_aux` are all private SKIP/KEEP; this lemma would travel with them, restated against the weighted substitution `aeval (fun j ↦ X ^ w j)` recommended in the Roth.kronecker report.

## Evidence
- `grep -rn derivative_mem_kronSpan Roth/`: definition l.162, single use l.202 (Roth/GenWronskian.lean).
- `grep -rln "kronSpan\|kronHasse" Roth/`: only Roth/GenWronskian.lean.
- `grep -rn "span_induction"` and `grep -rn "theorem.*span\|lemma.*span"` over `.lake/packages/mathlib/Mathlib/RingTheory/Derivation/`: no hits (no generic derivation-preserves-span lemma).
- Read sibling report Roth.derivative_kronHasse_aux.md.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
