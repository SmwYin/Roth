---
decl: MvPolynomial.uniqueAlgEquiv_hasseDeriv
file: Roth/HasseDeriv.lean
line: 266
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: One-variable bridge uniqueAlgEquiv (Delta_{n e} P) = D^(n) (uniqueAlgEquiv P) between the multivariate and univariate Hasse derivatives, absent from mathlib (which lacks even the pderiv/derivative analogue for uniqueAlgEquiv); it should be stated for an arbitrary multi-index d with D^(d default), a verified syntactic generalisation that removes the caller's Finsupp.unique_single rewrite.
action: Upstream with the parent to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean in the general-d form (evidence bridge.lean item 1), plus the linear-map form; locally optional: restate with d and drop the Finsupp.unique_single rewrite at Roth/Index.lean:239.
---

# MvPolynomial.uniqueAlgEquiv_hasseDeriv

## Inventory entry

### `theorem MvPolynomial.uniqueAlgEquiv_hasseDeriv`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] [Unique σ] (n : ℕ) (P : MvPolynomial σ R), uniqueAlgEquiv R σ (hasseDeriv (Finsupp.single default n) P) = Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P)`
- **What**: When `σ` has a single element, mathlib's algebra isomorphism `MvPolynomial σ R ≃ₐ[R] R[X]` carries the multivariate Hasse derivative `Δ_{n e}` to the univariate Hasse derivative `D^(n)`.
- **How**: `ext m`; rewrite coefficients on both sides with mathlib's `coeff_uniqueAlgEquiv` and `Polynomial.hasseDeriv_coeff` and the project's `coeff_hasseDeriv`; close with `simp [hasseCoeff, Finsupp.single_add]`.
- **Hypotheses**: `[Unique σ]` (needed for `uniqueAlgEquiv`), section variable `[CommSemiring R]`.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff` (unfolded in simp)
- **Used by**: Roth/Index.lean:239 (in `index_unique`, l.234, `rw [Polynomial.taylor_coeff, ← uniqueAlgEquiv_hasseDeriv, ← Finsupp.unique_single d]`). Mentioned in Roth/HasseDeriv.lean:36 (module docstring). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 266–271, proof length 3 lines
- **Notes**: Companion of `hasseDeriv_single_aeval_X` (l.253); each can be derived from the other (evidence item 3).

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Index.lean:239 (index of a one-variable polynomial = root multiplicity / weight, source §5 Lemma 5).
- Wrapper of 1–2 mathlib calls? No; `hasseDeriv` is a project definition.
- Does mathlib have it? No (Phase 5). Mathlib does not even have the first-order version `uniqueAlgEquiv (pderiv default P) = derivative (uniqueAlgEquiv P)`.
- Too specific / inline? No: it is the canonical transport lemma between the two theories. The only caller would otherwise need the 3-line coefficient computation inline.
- Well-chosen? Yes, but the `Finsupp.single default n` index is narrower than needed: under `[Unique σ]` every `d` equals `single default (d default)`, so stating it for arbitrary `d` removes the caller's `← Finsupp.unique_single d` step.
- Conclusion: `KEEP`. Optional local action: restate with arbitrary `d`.

## Mathlibable assessment (Step 9)

Real content (coefficient computation), not glue; full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; evidence file importing `Roth.HasseDeriv` elaborates with no errors)
- decl `MvPolynomial.uniqueAlgEquiv_hasseDeriv`: resolved at Roth/HasseDeriv.lean:266
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.uniqueAlgEquiv_hasseDeriv` is a theorem stating the following:

Let `R` be a commutative semiring and `σ` a one-element index set, so that `R[x_σ] ≅ R[t]` via the canonical isomorphism `Φ` (`x_default ↦ t`). For every `n ∈ ℕ` and `P ∈ R[x_σ]`, `Φ(Δ_{n e} P) = D^(n)(Φ P)`. In other words, in one variable the multivariate Hasse derivative is the univariate one, transported along `Φ`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Unique σ]`: the single-variable index set.
- `R : Type*`, `[CommSemiring R]`: coefficients.
- `n : ℕ`: order of differentiation.
- `P : MvPolynomial σ R`.

Hypotheses (Lean side):
- none beyond typeclasses.

Conclusion (math): `Φ ∘ Δ_{n e} = D^(n) ∘ Φ`.

Conclusion (Lean): `uniqueAlgEquiv R σ (hasseDeriv (Finsupp.single default n) P) = Polynomial.hasseDeriv n (uniqueAlgEquiv R σ P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: compatibility (transport) lemma for the BIG parent `MvPolynomial.hasseDeriv`; listed in the module docstring as a compatibility result, not a main theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multivariate Hasse derivative one variable reduces to univariate Hasse derivative polynomial ring isomorphism | partial | arXiv 2205.00342, 2111.07572, 1412.5012: multivariate `H(f, e)` = coefficient of `z^e` in `f(x+z)`; univariate `h^(k)` = coefficient of `z^k` in `h(t+z)` | with `m = 1` the two definitions coincide verbatim; no source states it as a separate lemma (folklore) |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation transported along ring isomorphism functoriality divided power derivative | partial | Narváez Macarro arXiv 0903.0246 (HS derivations, divided powers); arXiv 1802.09894 (action of substitution maps on HS derivations) | transport of HS derivations along (iso)morphisms is the general principle; our lemma is the instance for the iso `R[x_σ] ≅ R[t]` |
| 3 | WebSearch (named-after / aliases) | "Hasse derivative" "multi-index" definition coefficient f(x+z) one variable case | yes | arXiv 1509.00279, 1505.07547, 2311.08873, 0807.4332: `H(F,i) = Σ_j f_j binom(j,i) X^{j−i}` with `binom(j,i) = ∏ binom(j_k,i_k)` | for `m = 1` this is exactly the univariate formula; our proof is this coefficientwise comparison |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §1 (l.119–155) | yes | Hasse operator for multi-indices; Lean note at l.152–153 says to use the univariate `Polynomial.hasseDeriv` as a model | the bridge is implicit in the source (§5 Lemma 5 uses one-variable Taylor expansion) |
| 6 | nLab | Hasse-Schmidt derivation (surfaced via query #2) | partial | HS derivation as algebra hom `A → A[[t]]` | no polynomial-ring statement; functoriality is formal |
| 7 | nCatLab | (same nLab page) | n/a | — | not a categorical statement |
| 8 | Stacks Project | — | n/a | — | Stacks has differential operators but no Hasse-derivative transport lemma; not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | queries #1–#3 surfaced no MO/MSE thread | no | — | folklore |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2111.07572 (2021), 2205.00342 (2022), 2311.08873 (2023), 2510.08857 (2025) | all define multivariate Hasse derivatives so that `m = 1` is the univariate one |

### Literature summary (Phase 3)

Concept identified as: in one variable, the multivariate Hasse derivative coincides with the univariate one (`H(F, i)` with `m = 1`).
Sources agree on the standard form: yes. Every source defines `H(F, i)` as the coefficient of `Z^i` in `F(X+Z)`, which is visibly the univariate definition when `m = 1`.
Most general standard form: for one variable, `Δ_d` for any multi-index `d` (necessarily `d = d_0 e`) equals `D^(d_0)`; more generally, Hasse–Schmidt derivations are compatible with ring isomorphisms (functoriality).
Generality dimensions where the literature varies:
  - multi-index: written `n e` (current) vs an arbitrary multi-index `d` (with `d_0 = d default`). Under `Unique σ` these are the same set of operators, but the arbitrary-`d` statement applies to any `d` without first normalising it.
  - transport: iso `MvPolynomial σ R ≃ R[X]` for unique `σ` (current) vs general rename/embedding (covered by the sibling `hasseDeriv_single_aeval_X` and `hasseDeriv_rename`).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

Literature-standard form (from Phase 3): for one variable, `Φ (Δ_d P) = D^(d_0) (Φ P)` for every multi-index `d`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative ring/semiring | no | `MvPolynomial σ R` needs `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `[Unique σ]` | unique index | one variable | no | needed for `uniqueAlgEquiv` to exist; other variable sets are handled by the sibling `hasseDeriv_single_aeval_X` |
| 3 | multi-index `Finsupp.single default n` | `n e` only | arbitrary `d`, order `d default` | yes (syntactic) | `uniqueAlgEquiv_hasseDeriv'` with `d : σ →₀ ℕ` compiles (evidence item 1, and item 1b by the same 3-line proof) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (syntactically: it covers only multi-indices already written as `single default n`. Mathematically every `d` has this shape, but the general form saves callers from rewriting `d` into it).
Number of weakening opportunities found: 1 (arbitrary multi-index `d`; verified, evidence items 1 and 1b).
Proposed restatement:

```lean
theorem uniqueAlgEquiv_hasseDeriv [Unique σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv d P) =
      Polynomial.hasseDeriv (d default) (uniqueAlgEquiv R σ P)
```

Cost of restatement: CHEAP (same 3-line proof plus one `conv_lhs => rw [Finsupp.unique_single d]`; matches mathlib's own `uniqueAlgEquiv_monomial`, which is stated for arbitrary `d` with `d default`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic |
| 3 | construction vs universal property? | partial | operator form `(uniqueAlgEquiv R σ).toLinearMap ∘ₗ hasseDeriv d = Polynomial.hasseDeriv (d default) ∘ₗ (uniqueAlgEquiv R σ).toLinearMap` (item 2) | `LinearMap.comp` API; same content |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary multi-index `d` with `d default` (mirrors mathlib's `uniqueAlgEquiv_monomial`) | applies directly to any `d`; removes `Finsupp.unique_single` rewrites (Roth/Index.lean:239) |
| 8 | concrete-via-abstract? | no | the proof is a coefficient comparison specific to `uniqueAlgEquiv`. The abstract alternative (item 3, via `hasseDeriv_single_aeval_X`) is a different proof of the same statement, not a more abstract one | — |
| 9 | false-generalisation guard | no false generalisation | general `d` is the same operator family (`d = single default (d default)` under `Unique σ`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: arbitrary `d`, order `d default`, following the convention of `MvPolynomial.uniqueAlgEquiv_monomial` / `uniqueAlgEquiv_symm_monomial` in Mathlib/Algebra/MvPolynomial/Equiv.lean.
  - Cost: CHEAP
  - Mathlib downstream this enables: rewrites directly with `coeff_uniqueAlgEquiv`, `uniqueAlgEquiv_monomial` (both stated with `d default`); transfers univariate results (`Polynomial.hasseDeriv_mul`, `Polynomial.factorial_smul_hasseDeriv`, `Polynomial.taylor_coeff`) to `MvPolynomial` over a unique index type.
  - Real mathematical improvement: the lemma applies to every `d` without a normalisation step.

### Proof strategy — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | partial | derive from `hasseDeriv_single_aeval_X` via `uniqueAlgEquiv.symm = aeval (X default)` (item 3) | CHEAP, but longer (5 lines vs 3) |
| 5 | missing mathlib helpers | yes | `(uniqueAlgEquiv R σ).symm = Polynomial.aeval (X default)` (mathlib has `MvPolynomial.uniqueAlgEquiv_symm_apply` via `@[simps]` as `eval₂ C (X default)` but no `aeval` form; item 3 needed `rfl`) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  (A coefficient-wise `ext` using mathlib's `coeff_uniqueAlgEquiv` and `Polynomial.hasseDeriv_coeff` is the shortest proof.)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

[A] Lean-Finder       "Hasse derivative of multivariable polynomial in one variable corresponds to Polynomial.hasseDeriv under uniqueAlgEquiv"   `Polynomial.Bivariate.pderiv_one_equivMvPolynomial`, `pderiv_zero_equivMvPolynomial` (bivariate, first-order), `Polynomial.hasseDeriv_one'`; no uniqueAlgEquiv bridge
[B] Loogle            `MvPolynomial.uniqueAlgEquiv, Polynomial.derivative`; `MvPolynomial.uniqueAlgEquiv, MvPolynomial.pderiv`   no hits (not even the first-order bridge)
[C] LeanSearch        "derivative commutes with the isomorphism between MvPolynomial over a unique type and Polynomial"   only the `Polynomial.Bivariate` pderiv lemmas and `KaehlerDifferential.polynomialEquiv_comp_D`
[D] Grep mathlib src  `hasseDeriv` only in Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; `uniqueAlgEquiv` lemmas in Algebra/MvPolynomial/Equiv.lean (`uniqueAlgEquiv_monomial`, `uniqueAlgEquiv_symm_monomial`, `coeff_uniqueAlgEquiv`, eval2 lemmas), none about derivatives
[E] Name pattern      grep `.lake/packages/mathlib/Mathlib` for `uniqueAlgEquiv_hasseDeriv`, `uniqueAlgEquiv_pderiv`, `pderiv_uniqueAlgEquiv`, `MvPolynomial.hasseDeriv`   no hits

Searched for both the user's form and the general-`d` / operator form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Closest: `Polynomial.Bivariate.pderiv_one_equivMvPolynomial` (first-order, bivariate equivalence).

### Normal-form check — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

Equivalent formalisms: `uniqueAlgEquiv` form (current); `aeval (X default)` / `toMvPolynomial default` form (sibling `hasseDeriv_single_aeval_X`); `pUnitAlgEquiv` for `σ = PUnit`; operator form.
Does mathlib already have a canonical form for this idea? Yes for the iso: `MvPolynomial.uniqueAlgEquiv` (with `pUnitAlgEquiv` as the PUnit specialisation); its lemmas use `d default`.
Our statement is stated against the canonical form? yes (iso applied on both sides, univariate operator on the RHS).
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

Alternative restatements attempted:
- arbitrary `d` with `d default` (item 1/1b, compiles)
- linear-map operator form (item 2, compiles)
- via `hasseDeriv_single_aeval_X` (item 3, compiles)
Chosen restatement: arbitrary `d` with `Polynomial.hasseDeriv (d default)`.
Justification: applies to any `d` (the caller at Roth/Index.lean:239 has a general `d` and must currently insert `← Finsupp.unique_single d`), and matches `uniqueAlgEquiv_monomial`.

### Superfluous-argument audit — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `[Unique σ]` | yes | required by `uniqueAlgEquiv` |
| 3 | `n`, `P` | yes | data of the statement |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (arbitrary `d`, order `d default`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:239 | `rw [Polynomial.taylor_coeff, ← uniqueAlgEquiv_hasseDeriv, ← Finsupp.unique_single d]` in `index_unique` |

Inline-derivation grep: none (`grep -rn uniqueAlgEquiv Roth/` finds only this lemma, the docstring mention and `index_unique`). The sibling `hasseDeriv_single_aeval_X` is the embedding-form bridge, not a re-derivation.

### Composition check (Phase 6)

Can `MvPolynomial.uniqueAlgEquiv_hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1: mathlib only.
  - Mathlib decls used: `coeff_uniqueAlgEquiv`, `Polynomial.hasseDeriv_coeff` are available, but `MvPolynomial.hasseDeriv` is not in mathlib.
  - Result: fails

Attempt 2: from the sibling project lemma `hasseDeriv_single_aeval_X` plus `AlgEquiv.apply_symm_apply` and the defeq `(uniqueAlgEquiv R σ).symm g = aeval (X default) g` (evidence item 3).
  - Result: succeeds in 5 lines (a proof, not a ≤3-call composition) and needs non-mathlib API.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.uniqueAlgEquiv_hasseDeriv`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): every source defines the multivariate Hasse derivative so that the one-variable case is literally the univariate one (arXiv 1509.00279, 1412.5012, 2111.07572, 2205.00342). The project source clean.tex §1 uses `Polynomial.hasseDeriv` as the model.
- Generality analysis (Phase 4): STRICTLY NARROWER (syntactically). The general-`d` form is verified (evidence items 1, 1b).
- Mathlib search (Phase 5): not in mathlib. Mathlib also lacks the first-order `pderiv`/`derivative` bridge for `uniqueAlgEquiv`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is YES-but-generalise-first: mathlib has only the univariate `Polynomial.hasseDeriv`. A new multivariate Hasse derivative file must connect to the univariate theory. This lemma and its sibling `hasseDeriv_single_aeval_X` are that connection. This one transports along mathlib's canonical isomorphism `uniqueAlgEquiv`, so univariate facts such as `Polynomial.taylor_coeff` and root multiplicity become available for `MvPolynomial` over one variable. The Roth project uses it for exactly that (Roth/Index.lean:239, index = root multiplicity / weight).

The upstream statement should take an arbitrary multi-index `d` and use `Polynomial.hasseDeriv (d default)`. This follows mathlib's existing `uniqueAlgEquiv_monomial` convention, applies without first normalising `d` to `single default n`, and compiles with the same 3-line proof (evidence item 1b).

Reason for the generalisation: LITERATURE-WEAKENING (arbitrary multi-index) and MODERN-IDIOM (match the `d default` convention of `Mathlib/Algebra/MvPolynomial/Equiv.lean`).
Proposed restatement:
```lean
theorem uniqueAlgEquiv_hasseDeriv [Unique σ] (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    uniqueAlgEquiv R σ (hasseDeriv d P) =
      Polynomial.hasseDeriv (d default) (uniqueAlgEquiv R σ P) := by
  ext m
  rw [coeff_uniqueAlgEquiv, coeff_hasseDeriv, Polynomial.hasseDeriv_coeff, coeff_uniqueAlgEquiv]
  conv_lhs => rw [Finsupp.unique_single d]
  simp [hasseCoeff, Finsupp.single_add]
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - composes with `coeff_uniqueAlgEquiv`, `uniqueAlgEquiv_monomial`, `eval₂_uniqueAlgEquiv` (all with the `d default` convention) in Mathlib/Algebra/MvPolynomial/Equiv.lean;
  - transfers `Polynomial.hasseDeriv_mul`, `Polynomial.taylor_coeff`, `Polynomial.factorial_smul_hasseDeriv` to one-variable `MvPolynomial`;
  - with `factorial_smul_hasseDeriv_single` and `Polynomial.hasseDeriv_one'`, it gives the first-order `uniqueAlgEquiv (pderiv default P) = derivative (uniqueAlgEquiv P)`, which mathlib lacks (its only analogue is the bivariate `Polynomial.Bivariate.pderiv_one_equivMvPolynomial`).
WHY it belongs in mathlib (gap): mathlib has no multivariate Hasse derivative and no derivative compatibility lemma for `MvPolynomial.uniqueAlgEquiv` / `pUnitAlgEquiv`. Loogle finds nothing for `uniqueAlgEquiv` with either `pderiv` or `derivative`.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new, with the parent).
PR grouping: ship with `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_rename`, `hasseDeriv_single_aeval_X` (as `hasseDeriv_toMvPolynomial`).
Next action: run `/generalise MvPolynomial.uniqueAlgEquiv_hasseDeriv` (target: general-`d` form above) before opening the PR.

---

## Next step

Upstream with the parent in the general-`d` form. Optionally restate locally the same way and drop the `← Finsupp.unique_single d` rewrite at Roth/Index.lean:239 (check the `rw` direction still matches there).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.uniqueAlgEquiv_hasseDeriv/bridge.lean` (imports `Roth.HasseDeriv`), checked with `lean_diagnostic_messages`: success, no diagnostics. Contents:
  - (1) `uniqueAlgEquiv_hasseDeriv'`: general multi-index `d`, from the project lemma via `Finsupp.unique_single`.
  - (1b) The same general form proved directly by the original coefficient proof plus one `conv_lhs` rewrite.
  - (2) Linear-map operator form.
  - (3) Composition from the sibling `hasseDeriv_single_aeval_X`, via `(uniqueAlgEquiv R σ).symm g = aeval (X default) g` (by `rw [Polynomial.aeval_def, algebraMap_eq]; rfl`).
- Iterations: first version of item 3 used `simp [uniqueAlgEquiv, ...]`, which left an unsolved structure-`symm` goal; replaced by `rw ...; rfl`. No cold `lake env lean` run.
- Searches: Lean-Finder, Loogle (2 queries), LeanSearch as in [A]–[C]; mathlib grep [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn uniqueAlgEquiv_hasseDeriv Roth/`; `.mathlib-quality/references/clean.tex` (l.122, 152–153).
