---
decl: Roth.diag
file: Roth/CoeffNorm.lean
line: 161
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: diag P is literally the single mathlib term MvPolynomial.aeval (fun _ ↦ Polynomial.X) P (equivalently uniqueAlgEquiv R Unit composed with rename (fun _ ↦ ())), valid over any CommSemiring; mathlib has the map but no name for it, and a one-line abbreviation is not mathlib material; keep it as a project-local name.
action: Do not upstream; optionally generalise locally to CommSemiring R and bundle as aeval (fun _ ↦ X) : MvPolynomial σ R →ₐ[R] R[X]; re-aim downstream lemmas (natDegree_diag_le via MvPolynomial.aeval_natDegree_le, eval_diag via MvPolynomial.comp_aeval, diag_sub is map_sub); call sites Roth/MainLemma.lean:362-409, 497-538, 553, 602-606 unchanged.
---

# Roth.diag

## Inventory entry

### `def Roth.diag`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) : Polynomial ℤ`
- **What**: The diagonal substitution `P(x, …, x)`: replaces every variable `X_j` by the single variable `x`.
- **How**: `aeval (fun _ ↦ Polynomial.X) P` (one mathlib call, `MvPolynomial.aeval`).
- **Hypotheses**: none.
- **Uses from project**: `[]`
- **Used by**: Roth/CoeffNorm.lean: `diag_eq_sum` (164), `abs_coeff_diag_le` (174), `natDegree_diag_le` (183), `eval_diag` (193), `diag_sub` (199); Roth/MainLemma.lean: 362, 365, 369, 404, 406, 408 (`diag_sub`), 409 (`simpa [..., diag, ...]` unfolds it), 497, 500, 507, 509, 513, 519, 532, 538, 553, 602 (13 lines outside the declaring file).
- **Visibility**: public
- **Lines**: 159–161, body 1 line
- **Notes**: Listed under "Main definitions" of the CoeffNorm.lean module docstring. Stated over `ℤ` only, though nothing about `ℤ` is used.

## Junk check (Step 8)
- Used anywhere? Yes: 5 API lemmas in CoeffNorm.lean and 13 lines in MainLemma.lean (Lemma 9 statements about `diag (hasseDeriv j W) %ₘ f`).
- Wrapper of 1–2 mathlib calls? Yes: exactly one, `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`.
- Does mathlib have it? The map yes (as `aeval (fun _ ↦ X)`, also `uniqueAlgEquiv R Unit ∘ rename (fun _ ↦ ())`); no named declaration.
- Too specific (inline)? Inlining `aeval (fun _ ↦ Polynomial.X)` at 13 sites would hurt readability of the Lemma 9 statements; the name matches the paper's "diagonal substitution".
- Well-chosen? Mostly; could be over any `CommSemiring R` and bundled as an `AlgHom` so `diag_sub` (and any `map_*`) come for free.
- Conclusion: `KEEP` — action: keep as project-local name; optionally restate as `noncomputable abbrev diag : MvPolynomial σ R →ₐ[R] R[X] := aeval fun _ ↦ Polynomial.X`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.diag` not in mathlib (no `namespace Roth`). Not a glue lemma (it is a def). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no diagnostics)
- decl `Roth.diag`:          resolved at Roth/CoeffNorm.lean:161
- kind:                      def
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.diag` is a definition of the following: for a polynomial `P(x_1, …, x_m) = ∑_k a_k x^k` in variables indexed by `σ`, the one-variable polynomial `P(x, …, x) = ∑_k a_k x^{|k|}`, i.e. the image of `P` under the unique `ℤ`-algebra homomorphism `ℤ[x_j : j ∈ σ] → ℤ[x]` sending every `x_j` to `x`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variable index set (no finiteness needed).
- `P : MvPolynomial σ ℤ` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `diag P = P(x, …, x) ∈ ℤ[x]`.

Conclusion (Lean): n/a — definition (`noncomputable def diag (P : MvPolynomial σ ℤ) : Polynomial ℤ := aeval (fun _ ↦ Polynomial.X) P`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line specialisation of the evaluation homomorphism; not a new structure or main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | MainLemma.lean:409 deliberately unfolds `diag` in `simpa [..., ← aeval_def, diag, ...]`; nothing relies on it staying sealed |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes (project-local) | 13 MainLemma lines state Lemma 9 in terms of `diag (hasseDeriv j W) %ₘ f`; the name mirrors the paper. In mathlib, `aeval (fun _ ↦ X)` is already the idiomatic spelling |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; does not justify a mathlib addition)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate polynomial diagonal substitution P(x,...,x) coefficient sum over monomials of total degree n | partial | `P(x,…,x) = ∑ a_α x^{|α|}`; coefficient of `x^n` is the sum of the degree-`n` homogeneous component's coefficients | no named concept; only total-degree references |
| 2 | WebSearch (general form) | algebra homomorphism k[x_1,...,x_n] to k[x] sending each x_i to x specialization evaluation homomorphism | yes | universal property of the polynomial ring: the evaluation homomorphism `x_i ↦ b_i` (here `b_i = x`) | Encyclopedia of Math "Polynomial ring"/"Ring of polynomials" |
| 3 | WebSearch (named-after / aliases) | "diagonal" restriction of multivariate polynomial x_1 = ⋯ = x_m Roth lemma index proof | partial | Roth/Schmidt auxiliary polynomial vanishing at the diagonal point `(α,…,α)` | arXiv 2502.00731, math/0307203, math.uh.edu Roth notes; restriction to the diagonal is an ad hoc step, not a named construction |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "same variable", "diag" | yes | l.1449 "replace x_1, …, x_m by the same variable x"; l.1476, 1505, 1562-1564 (diagonal substitution may merge monomials) | project paper §6, Lemma 9 |
| 6 | nLab | polynomial ring / free commutative algebra | partial | free commutative algebra universal property | the map is the induced hom from the constant family |
| 7 | nCatLab | — | n/a | — | not a categorical concept beyond the free-algebra adjunction (covered in #6) |
| 8 | Stacks Project | polynomial algebra universal property (Tag 00EE area) | partial | `R[x_i] → S` determined by images of `x_i` | no diagonal-specific notion; geometrically restriction to the diagonal line in affine space |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore: kernel generated by `x_i − x_j` | no standard name |
| 10 | recent arXiv (last 5 years) | (results of #3) | partial | arXiv 2502.00731 (2025) uses the diagonal point in the Roth construction | same ad hoc usage |

### Literature summary (Phase 3)

Concept identified as: the evaluation (substitution) homomorphism `R[x_j : j ∈ σ] → R[x]`, `x_j ↦ x`; geometrically pull-back along the diagonal `𝔸¹ → 𝔸^σ`.
Sources agree on the standard form: yes.
Most general standard form: for any commutative semiring `R`, an `R`-algebra `S` and a family `(b_j)` in `S`, the evaluation hom `R[x_j] → S`; diag is the case `S = R[x]`, `b_j = x`.
Generality dimensions where the literature varies:
  - coefficient ring: `ℤ` (Roth) vs any commutative (semi)ring.
  - target point: the constant family `x` vs arbitrary families.
Disagreement with the literature: none; no source gives the diagonal substitution its own name.

### Generality analysis — `Roth.diag`

Literature-standard form (from Phase 3): `MvPolynomial.aeval b : MvPolynomial σ R →ₐ[R] S`, here `b = fun _ ↦ X`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficients `ℤ` | `MvPolynomial σ ℤ` | any `CommSemiring R` | yes | `aeval` needs only `CommSemiring`; verified (`diagHom` in evidence) |
| 2 | unbundled function | `MvPolynomial σ ℤ → ℤ[X]` | `R`-algebra hom | yes | `aeval _` is already an `AlgHom`; the def forgets this |
| 3 | `σ` | arbitrary | arbitrary | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is the existing mathlib term `MvPolynomial.aeval (fun _ ↦ Polynomial.X)` (false-positive class 4), so this does not route to generalise-first.
Number of weakening opportunities found: 2 (rows 1–2), verified in the evidence file (`diagHom : MvPolynomial σ R →ₐ[R] Polynomial R` over `[CommSemiring R]`, with `Roth.diag P = diagHom P := rfl`).
Proposed restatement (project-local): `noncomputable abbrev diag : MvPolynomial σ R →ₐ[R] Polynomial R := aeval fun _ ↦ Polynomial.X`.
Cost of restatement: CHEAP (call sites apply `diag` to a polynomial and keep parsing via the `AlgHom` coercion; `diag_sub` becomes `map_sub`; `diag_eq_sum` proof unchanged, verified over general `R`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | pure algebra |
| 3 | construction vs universal property? | yes | it is the hom given by the universal property (`aeval`) | `comp_aeval`, `aeval_rename`, `algHom_ext`, `map_sub`/`map_sum`/`map_prod` |
| 4 | bundled substructure? | yes | bundled `AlgHom` | `map_*` lemmas for free |
| 5 | field-specific to semiring? | yes | `ℤ` to `CommSemiring R` | evidence (1)-(5) all over general `R` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | as row 5 (coefficient ring) | — |
| 8 | concrete-via-abstract? | no | def has no proof body | — |
| 9 | false-generalisation guard | no false generalisation | `Roth.diag P = (aeval fun _ ↦ X : MvPolynomial σ ℤ →ₐ[ℤ] ℤ[X]) P` by `rfl` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `aeval (fun _ ↦ Polynomial.X)` itself (already mathlib); nothing to add.
  - Cost: CHEAP
  - Mathlib downstream this enables: `MvPolynomial.comp_aeval` (gives `eval_diag` in one line), `MvPolynomial.aeval_natDegree_le` (gives a `natDegree` bound), `map_sub` (`diag_sub`), `uniqueAlgEquiv`/`rename` bridge.
  - Real mathematical improvement: diag is an algebra hom; exposing that removes `diag_sub` and shortens `eval_diag`.

### Proof strategy — `Roth.diag`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already defined via the universal property (`aeval`) | — |
| 5 | missing mathlib helpers | yes (minor) | mathlib has no coefficient formula for `aeval (fun _ ↦ X)` (loogle `Polynomial.coeff (MvPolynomial.aeval _ _) _`: no hits); `diag_eq_sum` fills it | follow-up, see Verdict |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (the body is the mathlib idiom; only the bundling/coefficient-ring choice is suboptimal, see 4b)
  - Missing mathlib API (if any): coefficient formula `coeff n (aeval (fun _ ↦ X) P) = ∑ k ∈ P.support with degree k = n, coeff k P` (or the `∑ monomial k.degree (coeff k P)` form, `diag_eq_sum`).

### Diamond / defeq risk — `Roth.diag`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | no instances; `Algebra ℤ ℤ[X]` is the canonical one used by `aeval` (evidence `rfl`) |
| 2 | Reducibility leak | none | semireducible `noncomputable def` |
| 3 | Non-canonical unfolding | low | MainLemma.lean:409 unfolds `diag` together with `← aeval_def`; after unfolding, mathlib `aeval` lemmas fire, so the unfolding is benign |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`; evidence uses `Unit` and a general `σ` without constraints |
| 6 | Coercion ambiguity | low | bundled `AlgHom` version is applied through `DFunLike`; `diag (hasseDeriv j W) %ₘ f` still parses (as in `Roth.weight`-style refactors) |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.diag`

[A] Lean-Finder       "diagonal specialization of a multivariate polynomial: set all variables equal to a single variable x"   hits: `MvPolynomial.join₂`, `join₁`, `eval₂_eta` (unrelated); no named diagonal map
[B] Loogle            `Polynomial.natDegree (MvPolynomial.aeval _ _)` hit `MvPolynomial.aeval_natDegree_le`; `Polynomial.coeff (MvPolynomial.aeval _ _) _` no hits
[C] LeanSearch        "substitute the same variable X for every variable of a multivariate polynomial to get a univariate polynomial"   hits: `Polynomial.toMvPolynomial` (the opposite direction, `X ↦ X i`), `MvPolynomial.pUnitAlgEquiv`, `MvPolynomial.bind₁`
[D] Grep mathlib src  `fun _ (=>|↦) (Polynomial.)?X`, `aeval (fun _`, `rename (fun _`, `pUnitAlgEquiv`, `uniqueAlgEquiv`, `natDegree_aeval`, `totalDegree_rename_le`   hits: `MvPolynomial.uniqueAlgEquiv` (Mathlib/Algebra/MvPolynomial/Equiv.lean:67, `toFun := eval₂ Polynomial.C fun _ => Polynomial.X` for `[Unique σ]`), `pUnitAlgEquiv` (deprecated alias, :119), `coeff_uniqueAlgEquiv` (:103), `rename (fun _ ↦ i)` patterns (AffineSpace.lean:487, Equiv.lean:893, Nullstellensatz.lean:175), `aeval (fun _ ↦ 1)` (UniversallyClosed.lean:128); no general-`σ` diagonal def
[E] Name pattern      `MvPolynomial.aeval`, `MvPolynomial.comp_aeval`, `MvPolynomial.eval₂_rename`, `MvPolynomial.uniqueAlgEquiv_apply`, `MvPolynomial.le_totalDegree` (all used in the compiled evidence)   hits

Searched for both the user's form (diagonal substitution `P(x,…,x)`) and the literature-standard form (evaluation hom `aeval b`).

Concluded: found building blocks (`MvPolynomial.aeval`, equivalently `MvPolynomial.uniqueAlgEquiv R Unit ∘ MvPolynomial.rename (fun _ ↦ ())`); composition (one call) yields our form. `MvPolynomial.uniqueAlgEquiv` is literally `diag` for `[Unique σ]`.

### Normal-form check — `Roth.diag`

Equivalent formalisms: `aeval (fun _ ↦ X) P`; `eval₂ C (fun _ ↦ X) P`; `uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P)` (evidence (2)); `∑ k ∈ P.support, monomial k.degree (coeff k P)` (`diag_eq_sum`).
Does mathlib already have a canonical form for this idea? yes: `aeval` (mathlib's simp normal form rewrites `eval₂ (algebraMap _ _)` to `aeval`).
Is our statement stated against the canonical form? yes (body is `aeval`).
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.diag`

Alternative restatements attempted:
- bundled `aeval fun _ ↦ Polynomial.X : MvPolynomial σ R →ₐ[R] R[X]` over `[CommSemiring R]` (compiles; evidence (1))
- `uniqueAlgEquiv R Unit ∘ rename (fun _ ↦ ())` (equal; evidence (2)); worse to apply, two maps
Chosen restatement: the bundled `aeval` form.
Justification: one map, `AlgHom` API for free, `comp_aeval` handles evaluation.

### Superfluous-argument audit — `Roth.diag`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficient ring `ℤ` | no | any `CommSemiring R` works (evidence) |
| 2 | `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (bundle as `AlgHom`, general `R`) — local only
Superfluous arguments: 1 (`ℤ` specialisation)

Overall: RESTATE-BEFORE-SHIP (locally optional; nothing ships to mathlib)

### Call sites — `Roth.diag`

Internal use count: 13 lines outside the declaring file (plus 5 API lemmas in CoeffNorm.lean)
External-to-file callers: 1 distinct file (Roth/MainLemma.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:362 | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ C)` |
| Roth/MainLemma.lean:365 | `∀ j ∈ J, diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f` |
| Roth/MainLemma.lean:369 | `⟨(diag (hasseDeriv p.1.1 W.1) %ₘ f).coeff p.2, ...⟩` |
| Roth/MainLemma.lean:404 | `(h : diag (hasseDeriv j W') %ₘ f = diag (hasseDeriv j W'') %ₘ f)` |
| Roth/MainLemma.lean:406 | `have hdvd : f ∣ diag (hasseDeriv j (W' - W''))` |
| Roth/MainLemma.lean:408 | `simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]` |
| Roth/MainLemma.lean:409 | `simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def, diag, ...]` (unfolds) |
| Roth/MainLemma.lean:497, 500 | `private lemma abs_coeff_diag_hasseDeriv_modByMonic_le_aux ... \|((diag (hasseDeriv j P) %ₘ f).coeff i : ℝ)\|` |
| Roth/MainLemma.lean:507, 509 | `have hcD : ∀ k, \|((diag (hasseDeriv j P)).coeff k : ℝ)\| ≤ ...`; `abs_coeff_diag_le _ (abs_coeff_hasseDeriv_le j P hd hc) k` |
| Roth/MainLemma.lean:513 | `natDegree_diag_le _ hdP` |
| Roth/MainLemma.lean:519, 532, 538 | `\|(diag (hasseDeriv j P) %ₘ f).coeff i\| ≤ (⌊B * β ^ 3⌋₊ : ℤ)` and real-cast variants |
| Roth/MainLemma.lean:553, 602 | `\|(diag (hasseDeriv j W) %ₘ f).coeff i\| ≤ (C : ℤ)` / `(Cn : ℤ)` |

Inline-derivation grep (`aeval (fun _ ↦ Polynomial.X)` / `aeval fun _ ↦ X` over `Roth/`):
  - (none) — only the definition itself.

### Composition check (Phase 6)

Can `Roth.diag` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Roth.diag P = MvPolynomial.aeval (fun _ ↦ Polynomial.X) P` — `rfl` (it is the definition).
  - Mathlib decls used: `MvPolynomial.aeval`
  - Result: succeeds

Attempt 2: `= MvPolynomial.uniqueAlgEquiv R Unit (MvPolynomial.rename (fun _ ↦ ()) P)` by `simp [uniqueAlgEquiv_apply, eval₂_rename, aeval_def, Function.comp_def, Polynomial.algebraMap_eq]`
  - Mathlib decls used: `MvPolynomial.uniqueAlgEquiv`, `MvPolynomial.rename`, `MvPolynomial.eval₂_rename`
  - Result: succeeds (evidence (2))

Downstream re-aim (lemmas about `diag`, stated against `aeval (fun _ ↦ X)`):
  - `diag_sub` = `map_sub` (already its proof) — NO-composable.
  - `eval_diag`: general form `Polynomial.aeval x (aeval (fun _ ↦ X) P) = aeval (fun _ ↦ x) P` is `by rw [← AlgHom.comp_apply, comp_aeval]; simp` (evidence (5)) — NO-composable from `MvPolynomial.comp_aeval`.
  - `natDegree_diag_le`: `MvPolynomial.aeval_natDegree_le` (Mathlib/RingTheory/Polynomial/Basic.lean) with `n = 1` gives `natDegree ≤ totalDegree`; evidence (4) proves `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P` directly; the project form then needs `totalDegree P ≤ ∑ r_j` from `degreeOf` bounds — composable, re-aim the statement through `totalDegree`.
  - `diag_eq_sum`: holds verbatim over any `CommSemiring R` (evidence (3)); mathlib has no coefficient formula for `aeval (fun _ ↦ X)` (loogle empty), so a general-`R` coefficient lemma is the only plausible small mathlib contribution from this cluster (assess under `Roth.diag_eq_sum`).
  - `abs_coeff_diag_le`: genuinely `ℤ`/norm-specific; unaffected.

Conclusion: COMPOSABLE (one mathlib call)

## Verdict: `Roth.diag`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the diagonal substitution is the evaluation homomorphism `x_j ↦ x` from the universal property of polynomial rings; no source names it (paper l.1449; Encyclopedia of Math "Polynomial ring"; Roth literature uses it ad hoc).
- Generality analysis (Phase 4): STRICTLY NARROWER (`ℤ`, unbundled), but the general form is the existing mathlib term `aeval (fun _ ↦ X)` (class 4).
- Mathlib search (Phase 5): building blocks `MvPolynomial.aeval`, `MvPolynomial.uniqueAlgEquiv` + `MvPolynomial.rename`; no named diagonal def.
- Composition check (Phase 6): COMPOSABLE in one call.

**Rationale:**

`Roth.diag` is by definition `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`, a single application of mathlib's evaluation homomorphism; the evidence also shows it equals `uniqueAlgEquiv R Unit ∘ rename (fun _ ↦ ())`, and mathlib's `uniqueAlgEquiv` is exactly the `[Unique σ]` case (`toFun := eval₂ C fun _ => X`). A named one-line abbreviation of a mathlib term at a specific argument does not meet mathlib's bar (Phase 2b: only a project-local naming exemption applies; no defeq or diamond reason). Mathlib's idiom is to write `aeval (fun _ ↦ X)` directly, and the downstream facts are mathlib one-liners: `map_sub`, `comp_aeval`, `aeval_natDegree_le`.

WHY not: the def is a 1-call composition. Belongs-elsewhere check: keep it as a project-local name in Roth/CoeffNorm.lean, since the Lemma 9 statements in MainLemma.lean read better with `diag`. The only gap found is a coefficient formula for `aeval (fun _ ↦ X)` (`diag_eq_sum` over general `R`), which belongs to the `diag_eq_sum` assessment, not to this def.

Mathlib building blocks:      `MvPolynomial.aeval` (Mathlib/Algebra/MvPolynomial/Eval.lean), `MvPolynomial.uniqueAlgEquiv` (Mathlib/Algebra/MvPolynomial/Equiv.lean:67), `MvPolynomial.rename`, `MvPolynomial.comp_aeval`, `MvPolynomial.aeval_natDegree_le` (Mathlib/RingTheory/Polynomial/Basic.lean)
Composition sketch (≤3 lines):
```lean
example (P : MvPolynomial σ ℤ) : Roth.diag P = MvPolynomial.aeval (fun _ ↦ Polynomial.X) P := rfl
```
Call sites in our project (from Phase 6.0):  13 lines in Roth/MainLemma.lean (362, 365, 369, 404, 406, 408, 409, 497/500, 507, 509, 513, 519, 532, 538, 553, 602) plus 5 lemmas in CoeffNorm.lean
Refactor plan: no inlining recommended (readability). Optional CHEAP local improvement: change to `noncomputable abbrev diag : MvPolynomial σ R →ₐ[R] Polynomial R := aeval fun _ ↦ Polynomial.X` over `[CommSemiring R]`; then `diag_sub` becomes `map_sub` (delete it, and drop it from the simp list at MainLemma.lean:408), `eval_diag` reproved via `MvPolynomial.comp_aeval`, `natDegree_diag_le` routed through `MvPolynomial.aeval_natDegree_le` (`n = 1`) plus a `totalDegree ≤ ∑ r_j` bound, `diag_eq_sum` unchanged over general `R`; MainLemma.lean:409 unfolding still works (`diag` unfolds to `aeval`). All other call sites apply `diag` to a polynomial and are unaffected.
Next action: do not upstream `Roth.diag`; keep the name; optionally apply the local bundling above.

---

## Next step

No mathlib action for `Roth.diag`. Optionally generalise/bundle it as `aeval (fun _ ↦ X)` over `CommSemiring R`, and re-aim the downstream lemma assessments (`diag_sub`, `eval_diag`, `natDegree_diag_le`) at mathlib's `map_sub`, `comp_aeval`, `aeval_natDegree_le`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.diag/diag_mathlib_forms.lean` (imports `Roth.CoeffNorm`; `lake env lean` produced no errors; `lean_diagnostic_messages`: no diagnostics after adding a module docstring): (1) `Roth.diag P = (aeval fun _ ↦ X : MvPolynomial σ ℤ →ₐ[ℤ] ℤ[X]) P` by `rfl`, with `diagHom` over `[CommSemiring R]`; (2) `diagHom P = uniqueAlgEquiv R Unit (rename (fun _ ↦ ()) P)`; (3) `diag_eq_sum` over general `R`; (4) `natDegree (diagHom P) ≤ totalDegree P`; (5) `Polynomial.aeval x (diagHom P) = aeval (fun _ ↦ x) P` via `comp_aeval`; (6) `diag_sub` is `map_sub`.
- Mathlib greps listed in search-status [D].
- Loogle (2), LeanSearch (1), Lean-Finder (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.1449, 1476, 1505, 1562-1564).
- Project grep `grep -rn diag Roth/` for the call-sites table and inline-derivation grep.
