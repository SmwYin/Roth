---
decl: MvPolynomial.hasseDeriv_rename
file: Roth/HasseDeriv.lean
line: 143
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Delta_d commutes with injective renaming of variables when the multi-index is transported by mapDomain; it is the Hasse analogue of mathlib's MvPolynomial.pderiv_rename, absent from mathlib (no MvPolynomial Hasse derivative), and maximally general (injectivity is necessary, counterexample compiled).
action: Upstream with MvPolynomial.hasseDeriv to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, stated exactly as now (mirrors pderiv_rename); locally keep (call site Roth/Separation.lean:165 in hasseDeriv_rename_mul_aeval).
---

# MvPolynomial.hasseDeriv_rename

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_rename`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {τ : Type*} {f : σ → τ}, Function.Injective f → ∀ (d : σ →₀ ℕ) (P : MvPolynomial σ R), (hasseDeriv (Finsupp.mapDomain f d)) ((rename f) P) = (rename f) ((hasseDeriv d) P)`
- **What**: For an injective relabelling `f : σ → τ` of variables, the Hasse derivative of order `f_* d` of the renamed polynomial is the renaming of `Δ_d P`: `Δ_{f_* d} ∘ rename f = rename f ∘ Δ_d`. In particular an operator in a subset of the variables acts on a polynomial that only involves those variables as it did before the embedding.
- **How**: `induction P using MvPolynomial.induction_on'`; the monomial case is `simp` with `rename_monomial`, `hasseCoeff`, `Finsupp.prod_mapDomain_index_inj hf` (the binomial product is unchanged under injective reindexing), `Finsupp.mapDomain_apply_of_injective hf` and `← Finsupp.mapDomain_tsub hf` (`f_*(k - d) = f_* k - f_* d`); the additive case is `simp [hp, hq]`.
- **Hypotheses**: `hf : Function.Injective f` (necessary; see evidence item 3); `[CommSemiring R]`.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseCoeff`, `MvPolynomial.hasseDeriv_monomial` (via `simp`)
- **Used by**: Roth/Separation.lean:165 (`hasseDeriv_rename_mul_aeval`, with `f = some : τ → Option τ`), which in turn is used at Roth/Separation.lean:365.
- **Visibility**: public
- **Lines**: 143–152 (docstring 139–142), proof length 7 lines
- **Notes**: Docstring cites "§4, Lean implementation note after Lemma 4-2"; the paper's corresponding remark is that the operators `Δ_μ` use only the variables `x_1, …, x_{p-1}` (clean.tex l.408, 463). Statement shape is identical to mathlib's `MvPolynomial.pderiv_rename` (same `hf` argument, same orientation).

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Separation.lean:165 (one direct use, inside the separated-product lemma that feeds the Lemma-2 determinant factorisation).
- Wrapper of 1–2 mathlib calls? No: it is about the project operator; mathlib's `pderiv_rename` is about first-order partial derivatives and does not give Hasse derivatives in positive characteristic.
- Does mathlib have it? No (Loogle `"hasseDeriv", MvPolynomial.rename` returns nothing; only `MvPolynomial.pderiv_rename`).
- Too specific / inline? No: the standard naturality-in-variables lemma that mathlib supplies for `pderiv`; inlining would repeat the 7-line `induction_on'` proof.
- Well-chosen? Yes; `mapDomain` + `Injective` matches mathlib's `coeff_rename_mapDomain` / `pderiv_rename` conventions.
- Conclusion: `KEEP` — action: keep; upstream with the parent definition.

## Mathlibable assessment (Step 9)

Not a glue lemma (needs induction and three `Finsupp` reindexing lemmas), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` has no diagnostics)
- decl `MvPolynomial.hasseDeriv_rename`: resolved at Roth/HasseDeriv.lean:143
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_rename` is a theorem stating the following:

Let `f : σ → τ` be an injective map of variable sets and `f_* : R[X_σ] → R[X_τ]` the induced renaming `X_i ↦ X_{f(i)}`. For every multi-index `d ∈ ℕ^(σ)`, with push-forward `f_* d ∈ ℕ^(τ)` (`(f_* d)(f i) = d i`, zero off the image), and every polynomial `P`, `Δ_{f_* d}(f_* P) = f_*(Δ_d P)`. That is, Hasse derivatives are natural with respect to injective changes of variable names.

Variables / typeclasses involved (Lean side):
- `σ τ : Type*` — source and target variable index sets.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `f : σ → τ` — the renaming.
- `d : σ →₀ ℕ` — order of the derivative.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- `hf : Function.Injective f` — renaming does not merge variables.

Conclusion (math): `Δ_{f_* d} ∘ f_* = f_* ∘ Δ_d`.

Conclusion (Lean): `hasseDeriv (d.mapDomain f) (rename f P) = rename f (hasseDeriv d P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: naturality API lemma of the BIG parent definition `MvPolynomial.hasseDeriv`; not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative multivariate polynomial change of variables renaming variables, subset of variables | partial | partial Hasse derivatives in a subset of variables computed by viewing `F` as a polynomial over the ring of the other variables (arXiv 1812.07020); multi-index definition via `F(X+Z)` (arXiv 1707.01354, 1412.5012) | the `F(X+Z)` definition makes naturality under injective renaming immediate; no source states it as a lemma (folklore) |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation functoriality, polynomial ring inclusion k[x_1..x_n] into k[x_1..x_m] | yes | functoriality of the HS algebra in algebra maps (arXiv 2305.04537); explicit polynomial-ring description `HS^m_{B/A} = B[d_j x_i]` (Vojta, arXiv math/0407113) | the inclusion of polynomial rings is an algebra map, so HS derivations along it are compatible; our lemma is the explicit coefficient version |
| 3 | WebSearch (named-after / aliases) | "divided power" derivative OR "Hasse derivative" multi-index rename/relabel variables injective map | partial | multi-index Hasse derivative with componentwise binomials (arXiv 1412.5012); Narváez Macarro, Hasse–Schmidt derivations, divided powers and differential smoothness (Ann. Inst. Fourier, arXiv 0903.0246), polynomial-ring case via Taylor expansion | no explicit relabelling lemma; componentwise binomial definition shows renaming just permutes multi-indices |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for variable subsets / operators in fewer variables | yes | "differential operators `Δ_0, …, Δ_{l-1}` on the variables `x_1, …, x_{p-1}`" applied to polynomials in `x_1, …, x_p` (l.352, 408); "`Δ_μ` uses only the first `p-1` variables" (l.463) | this is exactly the use: `f = some : τ → Option τ` embeds the first `p-1` variables |
| 6 | nLab | Hasse-Schmidt derivative | partial | HS derivations as ring maps `A → A[[t]]`, functorial in `A` | no polynomial-ring relabelling lemma |
| 7 | nCatLab | — | n/a | — | not a categorical concept beyond naturality of the operator |
| 8 | Stacks Project | differential operators, base change | n/a | — | Stacks treats differential operators abstractly; no Hasse-derivative-specific renaming lemma |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; treated as immediate from the definition |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2305.04537 (2023), 2111.07572 (2021), 2205.00342 (2022) use multi-index Hasse derivatives with componentwise binomials | all implicitly use naturality in variable names |

### Literature summary (Phase 3)

Concept identified as: naturality of multivariate Hasse derivatives under injective relabelling of variables (equivalently, Hasse derivatives in a subset of the variables extend along the inclusion of polynomial rings); abstractly, functoriality of HS derivations along the algebra map `R[X_σ] → R[X_τ]`.
Sources agree on the standard form: yes (folklore; immediate from `Δ_d X^k = binom(k, d) X^{k-d}` with componentwise binomials).
Most general standard form: for an injective `f : σ → τ`, `Δ_{f_* d} ∘ f_* = f_* ∘ Δ_d`.
Generality dimensions where the literature varies:
  - map of variables: injective maps (relabelling / inclusion) — for non-injective maps the formula is false (multinomial merging; evidence item 3).
  - object: polynomials / power series (operator choice belongs to the parent report).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_rename`

Literature-standard form (from Phase 3): `Δ_{f_* d} ∘ f_* = f_* ∘ Δ_d` for injective `f`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hf : Function.Injective f` | injective | injective | NO | compiled counterexample (evidence item 3): `f : Fin 2 → Unit`, `P = X 0 * X 1`, `d = e_0` gives `2 X_* ≠ X_*`; injectivity only on `vars P ∪ d.support` would suffice but is not a standard or mathlib-idiomatic hypothesis (`pderiv_rename`, `coeff_rename_mapDomain` use `Injective`) |
| 2 | `[CommSemiring R]` | commutative semiring | any ring | no | forced by `MvPolynomial σ R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 3 | `d`, `P` | arbitrary | arbitrary | n/a | no constraint |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only hypothesis is necessary, evidence item 3).
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single injectivity hypothesis, same as `pderiv_rename` |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | `f : σ ↪ τ` with `Finsupp.embDomain` is an alternative spelling | rejected: mathlib's rename API (`pderiv_rename`, `coeff_rename_mapDomain`, `killCompl`) uses `mapDomain` + `Injective` |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | operator form `(hasseDeriv (d.mapDomain f)).comp (rename f).toLinearMap = (rename f).toLinearMap.comp (hasseDeriv d)` possible | pointwise form is what call sites rewrite with; mathlib's `pderiv_rename` is pointwise |
| 7 | concrete index to general? | no | index types already general | — |
| 8 | concrete-via-abstract? | no | proof uses only `Finsupp` reindexing facts; no named object | — |
| 9 | false-generalisation guard | no false generalisation | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is exactly the shape of mathlib's `MvPolynomial.pderiv_rename`, the canonical template.

### Proof strategy — `MvPolynomial.hasseDeriv_rename`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | uses existing `Finsupp.prod_mapDomain_index_inj`, `Finsupp.mapDomain_apply_of_injective`, `Finsupp.mapDomain_tsub` (Mathlib/Data/Finsupp/Order.lean:295); with the parent's proposed `Finsupp.choose` coefficient a `Finsupp.choose_mapDomain` lemma would be the natural helper, filed with the parent | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (induction on monomials, as `pderiv_rename` uses `induction_on`)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_rename`

[A] Lean-Finder       "multivariate Hasse derivative commutes with renaming variables by an injective function"   `MvPolynomial.pderiv_rename`, `rename_comp_expand`, `coeff_rename_mapDomain`, `killCompl_rename_app`; no Hasse
[B] Loogle            `"hasseDeriv", MvPolynomial.rename` (no results); `MvPolynomial.pderiv, MvPolynomial.rename` (only `MvPolynomial.pderiv_rename`)
[C] LeanSearch        "derivative of multivariate polynomial commutes with rename along injective map of variables"   `pderiv_rename`, `pderiv_map`, `map_comp_rename`, `bind₁_rename`; no Hasse
[D] Grep mathlib src  `hasseDeriv_rename`, `rename_hasseDeriv`, `pderiv_rename`, `mapDomain_tsub` over `.lake/packages/mathlib/Mathlib`: only `Algebra/MvPolynomial/PDeriv.lean:143` (`pderiv_rename`) and `Data/Finsupp/Order.lean:295` (`mapDomain_tsub`); `Polynomial/HasseDeriv.lean` has no rename lemma (univariate)
[E] Name pattern      `MvPolynomial.hasseDeriv_rename` (grep; the namespace has no `hasseDeriv` in mathlib)   no hits

Searched for both the user's form and the literature-standard general form (HS-derivation functoriality; first-order analogue).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); `MvPolynomial.pderiv_rename` is the template, and the parent operator itself is absent.

### Normal-form check — `MvPolynomial.hasseDeriv_rename`

Equivalent formalisms this statement could take: pointwise `Δ_{f_* d}(rename f P) = rename f (Δ_d P)`; operator composition form; `embDomain` with `f : σ ↪ τ`; coefficient form via `coeff_rename_mapDomain`.
Does mathlib already have a canonical form for this idea? yes: `MvPolynomial.pderiv_rename` states `pderiv (f x) (rename f p) = rename f (pderiv x p)` with `hf : Injective f`.
Our statement is stated against the canonical form? yes (same orientation, same hypothesis, `d.mapDomain f` playing the role of `f x`; evidence item 2 recovers the single-variable shape `Δ_{n e_{f i}}` in one `rw`).
RHS convention respected? yes (pushes `rename` outward).

### Syntactic generality — `MvPolynomial.hasseDeriv_rename`

Alternative restatements attempted:
- current (`d.mapDomain f`, `hf : Injective f`)
- `f : σ ↪ τ` with `d.embDomain f`
- single-variable `Finsupp.single (f i) n` version (evidence item 2: a corollary)
Chosen restatement: current.
Justification: `mapDomain` + `Injective` matches `pderiv_rename` and the rename API, and the call site (`Option.some_injective`) supplies exactly that.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_rename`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hf : Function.Injective f` | yes | counterexample without it (evidence item 3) |
| 2 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 3 | `d`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `MvPolynomial.hasseDeriv_rename`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:165 | `rw [..., hasseDeriv_rename (Option.some_injective τ), mul_comm]` (`hasseDeriv_rename_mul_aeval`) |

Inline-derivation grep: (none) — `grep -rn rename Roth/*.lean | grep -i hasse` finds no other proof re-deriving the commutation.

K = 1 would lean toward inlining, but the lemma is the standard naturality API (template `pderiv_rename` in mathlib) and its proof is a 7-line induction, not a mathlib composition; see Phase 6.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_rename` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib; `pderiv_rename` handles first-order derivatives only and cannot produce Hasse derivatives in positive characteristic (no division by factorials).
  - Result: fails

Attempt 2: from the parent's API plus `Finsupp` reindexing.
  - Decls used: `rename_monomial`, `hasseDeriv_monomial`, `Finsupp.prod_mapDomain_index_inj`, `Finsupp.mapDomain_apply_of_injective`, `Finsupp.mapDomain_tsub`, under `induction_on'`.
  - Result: succeeds, but this is the lemma's own proof (induction + simp with five lemmas), i.e. a real proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.hasseDeriv_rename`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): folklore naturality of multi-index Hasse derivatives (componentwise binomial definition, arXiv 1412.5012, 1707.01354; functoriality of HS derivations, arXiv 2305.04537, math/0407113); the source paper uses operators in `x_1, …, x_{p-1}` acting on polynomials in `x_1, …, x_p` (clean.tex l.352, 408, 463).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (injectivity necessary, compiled counterexample); Phase 4c: no modern-idiom move.
- Mathlib search (Phase 5): not in mathlib; template `MvPolynomial.pderiv_rename`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` was assessed YES-but-generalise-first (multivariate Hasse derivative absent from mathlib; ship with `Finsupp.choose` coefficients). Mathlib equips its partial derivative with exactly this naturality lemma (`MvPolynomial.pderiv_rename`, same hypothesis and orientation), and the multivariate Hasse derivative needs the same: it is how an operator in a subset of the variables is applied to a polynomial in more variables (the project uses `f = some : τ → Option τ` to separate `x_1, …, x_{p-1}` from `x_p` in Roth's Lemma 2). The statement is maximally general: dropping injectivity fails (evidence item 3), and the typeclass is forced by `MvPolynomial`.

Only one internal call site exists, but the lemma is not a composition of mathlib calls (Phase 6) and is the canonical API partner of the parent; it belongs in the parent's PR rather than being inlined.

WHY add it: `Mathlib/Algebra/MvPolynomial/PDeriv.lean` provides `pderiv_rename` but mathlib has no multivariate Hasse derivative, so there is no lemma moving `rename` through `Δ_d`. Hasse derivatives are the characteristic-free replacement for `(1/d!) ∂^d`, so `pderiv_rename` cannot be used to obtain this lemma over rings without division. With it, the rename API (`rename_rename`, `coeff_rename_mapDomain`, `killCompl_rename_app`, `optionEquivLeft`/`sumAlgEquiv` decompositions) composes with Hasse derivatives, which is what separating variables needs (DKSS-style multiplicity arguments, Roth/Dyson lemmas, tensor-product splittings `R[X_σ ⊕ X_τ]`).
Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
Proposed PR title:            "feat(Algebra/MvPolynomial): multivariate Hasse derivatives"
PR grouping (if applicable):  ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`, `coeff_hasseDeriv`, `hasseDeriv_zero(_apply)`, `hasseDeriv_C`, `hasseDeriv_map`, in one PR.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.hasseDeriv_rename` — confirm no easy further weakening (expected none)
  - [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_rename` — full audit + diff gates (re-check the proof after the parent's `Finsupp.choose` rename)
  - [ ] Pick a mathlib reviewer based on `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/HasseDeriv.lean` recent commits

---

## Next step

Ship unchanged as `MvPolynomial.hasseDeriv_rename` in the parent's PR to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, next to the `hasseDeriv_map` naturality lemma; locally keep it (call site Roth/Separation.lean:165).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_rename/variants.lean` (checked with `lean_diagnostic_messages`: no errors or warnings): (1) the statement re-proved standalone; (2) the single-variable corollary `Δ_{n e_{f i}} (rename f P) = rename f (Δ_{n e_i} P)` in one `rw` (the shape of `pderiv_rename`); (3) a compiled counterexample showing injectivity cannot be dropped (`f : Fin 2 → Unit`, `P = X 0 * X 1`, `d = e_0`, evaluated at `1`: `2 ≠ 1`).
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `"hasseDeriv", MvPolynomial.rename`: no results; `MvPolynomial.pderiv, MvPolynomial.rename`: `pderiv_rename` only. LeanSearch / Lean-Finder: `pderiv_rename` and rename API only. Mathlib grep as recorded in [D].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseDeriv_rename Roth/` (Used-by, call sites) and `grep -rn rename Roth/*.lean | grep -i hasse` (inline derivations: none); grep of `.mathlib-quality/references/clean.tex` for operators in a subset of the variables (l.352, 408, 463).
