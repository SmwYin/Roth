---
decl: Roth.derivative_kronHasse_aux
file: Roth/GenWronskian.lean
line: 153
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private chain-rule identity d/dt (kronHasse k d) = sum over j of (X^(k^j))' * (d j + 1) • kronHasse k (d + single j 1), the generator case of derivative_mem_kronSpan; combines the project lemmas derivative_aeval and pderiv_hasseDeriv, neither of which mathlib has.
action: Keep as private helper of derivative_mem_kronSpan (Roth/GenWronskian.lean:169); if Lemma 1 is upstreamed, carry it with kronHasse/kronSpan, restated for the weighted substitution aeval (fun j ↦ X ^ w j) and derived from the generalised derivative_aeval and pderiv_hasseDeriv.
---

# Roth.derivative_kronHasse_aux

## Inventory entry

### `theorem Roth.derivative_kronHasse_aux`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) : (fun P ↦ Polynomial.derivative (kronHasse k d P)) = ∑ j, (Polynomial.derivative (Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)) * Polynomial.C ((d j + 1 : ℕ) : K)) • kronHasse k (d + Finsupp.single j 1)`
- **What**: As an identity in the K[t]-module of functions MvPolynomial σ K → K[t]: differentiating (in t) the operator P ↦ (Δ_d P)(t, t^k, t^(k^2), ...) gives the K[t]-linear combination over j of (t^(k^(e j)))' · (d_j + 1) times the operator for the Hasse multi-index d + e_j. I.e. the derivative of a generator of `kronSpan k μ` lies in `kronSpan k (μ + 1)`, with explicit coefficients.
- **How**: `funext P` then a single `simp` that unfolds `kronHasse` and `kronecker` (to `aeval`), applies the project chain rule `Roth.derivative_aeval` (d/dt aeval γ P = ∑ j, (γ j)' * aeval γ (pderiv j P)), rewrites `pderiv j (hasseDeriv d P)` by the project lemma `MvPolynomial.pderiv_hasseDeriv` (= (d j + 1) • hasseDeriv (d + single j 1) P), and normalises with `map_smul`, `Polynomial.smul_eq_C_mul`, `mul_assoc`, `mul_comm`, `mul_left_comm`.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` from section variables; `classical` for the Finsupp/sum decidability. No hypothesis on `k` or `d`.
- **Uses from project**: `Roth.kronHasse` (Roth/GenWronskian.lean:145), `Roth.kronecker` (l.53), `Roth.derivative_aeval` (l.133), `MvPolynomial.pderiv_hasseDeriv` (Roth/HasseDeriv.lean:200); implicitly `MvPolynomial.hasseDeriv` (through `kronHasse`).
- **Used by**: `grep -rn derivative_kronHasse_aux Roth/`: only `Roth.derivative_mem_kronSpan` (Roth/GenWronskian.lean:169, `rw` in the `mem` case of `Submodule.span_induction`). Transitively feeds `hasseDeriv_kronecker_mem`, `exists_hasseDeriv_kronecker_eq_sum` and Lemma 1 `exists_genWronskian_ne_zero`.
- **Visibility**: private
- **Lines**: 153–159, proof length 4 lines (l.156–159: `classical`, `funext P`, two-line `simp`)
- **Notes**: Name ends in `_aux`. Stated at the level of functions (not pointwise) so it can be used with `rw` on the generator `kronHasse k d` inside the K[t]-span. The coefficient `C ((d j + 1 : ℕ) : K)` is put inside the K[t]-scalar so the result is visibly a K[t]-combination of generators.

## Junk check (Step 8)
- Used anywhere? Yes, once: `derivative_mem_kronSpan` l.169, which needs exactly this generator-level identity to close the `mem` case of span induction.
- Wrapper of 1–2 mathlib calls? No. The proof is one `simp`, but the substantive ingredients are two *project* lemmas (`Roth.derivative_aeval`, `MvPolynomial.pderiv_hasseDeriv`), not mathlib lemmas.
- Does mathlib have it? No. Mathlib has no multivariate Hasse derivative (`def hasseDeriv` only in Mathlib/Algebra/Polynomial/HasseDeriv.lean and Mathlib/RingTheory/LaurentSeries.lean), no Kronecker substitution, and no chain rule for `Polynomial.derivative (MvPolynomial.aeval γ P)` (grep for `derivative_aeval` / `derivative (aeval` over Mathlib: no hits; only univariate `Polynomial.derivative_comp`).
- Too specific / inline? It could be inlined as a `have` in `derivative_mem_kronSpan` (single use), but the statement is long (a ∑ of K[t]-smuls) and stating it separately keeps the span-induction proof readable; it is private, so it costs nothing in the API. Inlining would not shorten the code.
- Well-chosen? Yes: function-level equality is the right shape for `rw` inside `Submodule.span_induction`; the coefficient placement makes the `Submodule.smul_mem` / `subset_span` step immediate.
- Conclusion: `KEEP`. Action: none; keep as the private generator lemma of `derivative_mem_kronSpan`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/GenWronskian.lean:153; the name also ends in `_aux`, so the Step 9a pre-filter would fire independently).

Note for an eventual upstreaming of Lemma 1: its ingredients `Roth.derivative_aeval` and `MvPolynomial.pderiv_hasseDeriv` were both assessed YES-but-generalise-first, and the parents `Roth.kronHasse` / `Roth.kronSpan` are private SKIP/KEEP. This identity would travel with them, restated against the weighted substitution `aeval (fun j ↦ X ^ w j)` recommended in the Roth.kronecker report (where the coefficient becomes `derivative (X ^ w j)`).

## Evidence
- `grep -rn derivative_kronHasse_aux Roth/`: definition l.153, single use l.169 (Roth/GenWronskian.lean).
- `grep -rn "derivative_aeval\|derivative.*aeval.*pderiv" .lake/packages/mathlib/Mathlib/`: no hits. `grep -rn "derivative (aeval\|derivative_comp\b"`: only `Polynomial.derivative_comp` (univariate composition).
- `grep -rln "def hasseDeriv" .lake/packages/mathlib/Mathlib/`: only Algebra/Polynomial/HasseDeriv.lean and RingTheory/LaurentSeries.lean.
- Read `MvPolynomial.pderiv_hasseDeriv` statement (Roth/HasseDeriv.lean:200–201) and the sibling reports Roth.kronHasse.md, Roth.kronSpan.md, Roth.derivative_aeval.md, MvPolynomial.pderiv_hasseDeriv.md.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated.
