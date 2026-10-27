---
decl: Roth.kronHasse
file: Roth/GenWronskian.lean
line: 145
kind: def
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-line abbreviation P ↦ kronecker k (hasseDeriv d P) naming the generators of the K[X]-span kronSpan used in the proof of Lemma 1; mathlib has neither ingredient (no Kronecker substitution, no multivariate Hasse derivative), so nothing to replace it with.
action: Keep as private helper for kronSpan (Roth/GenWronskian.lean:151), derivative_kronHasse_aux (l.153-159), hasseDeriv_kronecker_mem (l.196) and exists_hasseDeriv_kronecker_eq_sum (l.221); if Lemma 1 is upstreamed, carry it along with kronSpan, re-based on the generalised weighted substitution recommended for Roth.kronecker.
---

# Roth.kronHasse

## Inventory entry

### `def Roth.kronHasse`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) : MvPolynomial σ K → Polynomial K`
- **What**: The operator P ↦ (Δ_d P)(t, t^k, t^(k^2), ...), i.e. the Kronecker substitution of the d-th multivariate Hasse derivative of P, viewed as an element of the K[t]-module of functions MvPolynomial σ K → K[t].
- **How**: Direct definition `fun P ↦ kronecker k (hasseDeriv d P)` (composition of the project AlgHom `Roth.kronecker k` with the project linear map `MvPolynomial.hasseDeriv d`); no proof.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` from the section variables (`[Fintype σ]` needed by `kronecker`, which uses `Fintype.equivFin σ`; `Field` is more than the definition needs, `CommSemiring` would do for the composition itself, but the section and parent `kronecker` fix it).
- **Uses from project**: `Roth.kronecker` (Roth/GenWronskian.lean:53), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57).
- **Used by**: Roth/GenWronskian.lean only (`grep -rn kronHasse Roth/`): `kronSpan` l.151 (generators of the span, as `kronHasse k '' {d | d.degree ≤ μ}`), `derivative_kronHasse_aux` l.154,156 (statement) and l.159 (simp unfold), `derivative_mem_kronSpan` indirectly via `derivative_kronHasse_aux` at l.169, `hasseDeriv_kronecker_mem` l.196 (simp unfold), `exists_hasseDeriv_kronecker_eq_sum` l.221 (simp unfold). Transitively feeds `exists_genWronskian_ne_zero` (Lemma 1).
- **Visibility**: private
- **Lines**: 144–146 (docstring l.144, declaration l.145–146), body 1 line
- **Notes**: `private noncomputable def`. Exists only so the K[t]-span `kronSpan` has a named generating family; the public statement `exists_hasseDeriv_kronecker_eq_sum` unfolds it away, so it does not leak into the public API.

## Junk check (Step 8)
- Used anywhere? Yes: it is the generating family of `kronSpan` and appears in the statement of `derivative_kronHasse_aux`; unfolded by `simp` at l.159, l.196, l.221. Four declarations depend on it.
- Wrapper of 1–2 mathlib calls? It is a composition of two *project* maps (`Roth.kronecker`, `MvPolynomial.hasseDeriv`), not of mathlib maps. Equivalent spelling `⇑((kronecker k).toLinearMap ∘ₗ hasseDeriv d)` exists, but the coercion-to-function form is what the K[t]-module `MvPolynomial σ K → Polynomial K` needs (the span is over K[t], acting pointwise, which a K-linear-map spelling would not give directly), so the lambda is the right shape.
- Does mathlib have it? No. Mathlib has no multivariate Hasse derivative (`def hasseDeriv` only in Mathlib/Algebra/Polynomial/HasseDeriv.lean and Mathlib/RingTheory/LaurentSeries.lean) and no named Kronecker substitution (grep for "Kronecker substitution"/`kroneckerSubst` over Mathlib: no hits; see the Roth.kronecker report). Hence it cannot have the composite.
- Too specific / inline? Inlining is possible (replace `kronHasse k` by `fun d P ↦ kronecker k (hasseDeriv d P)` in `kronSpan` and in `derivative_kronHasse_aux`), but that lengthens the statement of `derivative_kronHasse_aux` (two occurrences, one at `d + single j 1`) and the image set in `kronSpan`, and the `simp [kronHasse]` unfold steps would become beta-reductions anyway; the name buys readability at no cost, and it is private.
- Well-chosen? Yes: the docstring states precisely the role (an element of the K[X]-module of functions), the argument order `k d` matches `kronecker k` / `hasseDeriv d`, and the definition is the minimal one.
- Conclusion: `KEEP`. Action: none; keep as private helper of the Lemma 1 proof.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private noncomputable def` at Roth/GenWronskian.lean:145).

Note for an eventual upstreaming of Lemma 1 (`exists_genWronskian_ne_zero`) / `exists_hasseDeriv_kronecker_eq_sum`: both parents `Roth.kronecker` and `MvPolynomial.hasseDeriv` were assessed YES-but-generalise-first; this helper would travel with `kronSpan` and be restated against the weighted substitution `aeval (fun j ↦ X ^ w j)` recommended in the Roth.kronecker report.

## Evidence
- `grep -rn kronHasse Roth/`: definition l.145; uses l.148 (docstring), 151, 153–154, 156, 159, 169 (via the aux lemma), 196, 221; all in Roth/GenWronskian.lean.
- `grep -rln "def hasseDeriv" .lake/packages/mathlib/Mathlib/`: only Algebra/Polynomial/HasseDeriv.lean and RingTheory/LaurentSeries.lean (univariate / Laurent).
- `grep -rn "Kronecker substitution\|kroneckerSubst" .lake/packages/mathlib/Mathlib/`: no hits.
- Parent verdicts read from .mathlib-quality/overview/mathlibable/Roth.kronecker.md and MvPolynomial.hasseDeriv.md (both YES-but-generalise-first, junk KEEP).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the definition compiles as stated.
