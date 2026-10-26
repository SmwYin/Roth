---
decl: MvPolynomial.hasseDeriv_zero_apply
file: Roth/HasseDeriv.lean
line: 112
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Delta_0 P = P is the basic normalisation lemma of the multivariate Hasse derivative (pointwise analogue of mathlib's Polynomial.hasseDeriv_zero'), absent from mathlib, already maximally general (CommSemiring forced by MvPolynomial), and it is the lemma from which the bundled hasseDeriv_zero is proved; it ships unchanged in the parent's PR.
action: Upstream with MvPolynomial.hasseDeriv (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean) as hasseDeriv_zero_apply beside @[simp] hasseDeriv_zero, proof adjusted to the Finsupp.choose spelling; locally keep (used by hasseDeriv_zero l.121 and Roth/Index.lean:104-105).
---

# MvPolynomial.hasseDeriv_zero_apply

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_zero_apply`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (P : MvPolynomial σ R), (hasseDeriv 0) P = P`
- **What**: The Hasse derivative of order zero fixes every polynomial: `Δ_0 P = P`.
- **How**: `ext e` then `simp [coeff_hasseDeriv, hasseCoeff]`: the coefficient formula gives `[X^e] Δ_0 P = hasseCoeff 0 (e + 0) * [X^(e+0)] P`, and `hasseCoeff 0 k` is the empty `Finsupp.prod` over the support of `0`, i.e. `1`.
- **Hypotheses**: `[CommSemiring R]` (section variable); no other hypotheses.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseCoeff`
- **Used by**: Roth/HasseDeriv.lean: `hasseDeriv_zero` (l.121, `LinearMap.ext hasseDeriv_zero_apply`); Roth/Index.lean: `index_eq_zero_iff` (l.104 and l.105, as a `simpa` argument).
- **Visibility**: public
- **Lines**: 112–114 (docstring 109–111), proof length 2 lines
- **Notes**: Not `@[simp]`, but the bundled `hasseDeriv_zero` is `@[simp]`, so `simp` already proves `hasseDeriv 0 P = P` via `LinearMap.id_apply` (evidence file); the `simpa [hasseDeriv_zero_apply]` arguments in Roth/Index.lean are therefore probably redundant (not checked in Roth/ since the file must not be edited). The mathlib univariate analogue is named `Polynomial.hasseDeriv_zero'`; current mathlib naming prefers the `_apply` suffix for pointwise forms of bundled-map equalities, so `hasseDeriv_zero_apply` is the better name.

## Junk check (Step 8)
- Used anywhere? Yes: proves the bundled `hasseDeriv_zero` (HasseDeriv.lean:121) and is used twice in `index_eq_zero_iff` (Index.lean:104-105).
- Wrapper of 1–2 mathlib calls? No: it is a statement about a project operator, proved from the project coefficient lemma.
- Does mathlib have it? No: only univariate `Polynomial.hasseDeriv_zero'` / `Polynomial.hasseDeriv_zero` and `LaurentSeries.hasseDeriv_zero` (Loogle `"hasseDeriv_zero"`, LeanSearch, Lean-Finder).
- Too specific / inline? No: it is the standard normalisation lemma that every operator family in mathlib carries in both bundled and pointwise forms (`Polynomial.hasseDeriv_zero'`/`hasseDeriv_zero`, `iteratedDeriv_zero`).
- Well-chosen? Yes.
- Conclusion: `KEEP` — action: keep; upstream with the parent definition.

## Mathlibable assessment (Step 9)

Not a glue lemma (`ext` + `simp` with the coefficient formula, not `rfl`), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles with no errors or warnings)
- decl `MvPolynomial.hasseDeriv_zero_apply`: resolved at Roth/HasseDeriv.lean:112
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_zero_apply` is a theorem stating the following:

Let `R` be a commutative semiring and `P ∈ R[X_σ]`. The Hasse derivative of order `0` (the zero multi-index) leaves `P` unchanged: `Δ_0 P = P`. Equivalently, since `binom(k, 0) = ∏_j binom(k_j, 0) = 1` for every multi-index `k`, `Δ_0` fixes every monomial.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `Δ_0 P = P`.

Conclusion (Lean): `hasseDeriv 0 P = P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma (pointwise normalisation) of the BIG parent definition `MvPolynomial.hasseDeriv`; not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative of order zero is the identity multivariate polynomial D^(0) = id | yes | `D^{(0)} = id`; multivariate `D^{(0,...,0)}` fixes every monomial since all `binom(k_j, 0) = 1` | arXiv 1310.6482 (multidimensional Hasse derivatives via Taylor expansion); mathlib univariate docs; the multivariate statement is immediate from the definition, not stated as a separate lemma |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation D_0 identity map definition sequence of maps | yes | a Hasse–Schmidt derivation is a sequence `(D_i)` with `D_0 = id` (an axiom of the abstract notion) | arXiv 1807.10502, 1106.1391, 1905.01704, 2509.00887, 1810.08075; nLab "Hasse-Schmidt derivation" |
| 3 | WebSearch (named-after / aliases) | "Hasse derivative" multi-index "D^{(0)}" OR "zeroth Hasse derivative" polynomial method multiplicity | partial | `P^{(β)}` = coefficient of `y^β` in `P(x + y)`; `β = 0` gives `P(x)` | arXiv 2403.19824, 0901.2529 (DKSS), 1707.01354, 1402.0643; the `β = 0` case is used implicitly (multiplicity ≥ 1 iff `P(a) = 0`) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Δ_0 / hasse | yes | l.567: "and `Δ_0 P = P`, proving the equivalence" (index-zero lemma); l.298 "for `μ=0`, use the identity operator" | project paper uses exactly this fact in the `ind(P) = 0 ⇔ P(α) ≠ 0` lemma, matching the call site in Roth/Index.lean |
| 6 | nLab | Hasse-Schmidt derivation | yes | `D_0 = id` as part of the definition of a HS derivation | general abstract form: the zeroth component is the identity |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators abstractly; no Hasse-derivative normalisation lemma on polynomial rings |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; the fact is treated as trivial from the definition |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | yes | arXiv 2509.00887 (2025), 2403.19824 (2024), 1905.01704 | all take `D_0 = id` as part of the definition or as immediate |

### Literature summary (Phase 3)

Concept identified as: zeroth Hasse (divided-power) derivative is the identity; in the abstract theory of Hasse–Schmidt derivations, the normalisation axiom `D_0 = id`.
Sources agree on the standard form: yes.
Most general standard form: for any (semi)ring `R` and any family of Hasse derivatives (univariate or multivariate, polynomials or power series, or an abstract HS derivation), `D_0 = id`.
Generality dimensions where the literature varies:
  - object: polynomials, power series, Laurent series, abstract HS derivations; the concrete multivariate polynomial operator is the parent's choice (power-series companion is a parent-level option).
  - bundled `D_0 = id` vs pointwise `D_0 f = f`: both standard; mathlib carries both for the univariate operator.
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_zero_apply`

Literature-standard form (from Phase 3): `D_0 f = f` for every `f`, over any (semi)ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | any semiring | no (for `MvPolynomial`) | `MvPolynomial σ R` itself requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `σ : Type*` | arbitrary | finitely many variables | no (already more general) | — |
| 3 | `P : MvPolynomial σ R` | polynomial | polynomial / power series | companion only | the power-series operator would be a separate definition (parent report); not a weakening of this statement |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (no hypotheses; the only typeclass is forced by `MvPolynomial`).
Cost of restatement: n/a (no restatement of the statement; after the parent's `Finsupp.choose` rename only the proof changes, verified in evidence `hasseDeriv_zero_apply_choose`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | normalisation of an operator family |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | already a commutative semiring, the minimum for `MvPolynomial` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | the index is the zero multi-index; nothing to generalise |
| 8 | concrete-via-abstract? | no | the proof uses only `coeff_hasseDeriv` and `hasseCoeff 0 k = 1`; an abstract "HS-derivation" class is not in mathlib and would be a separate project | — |
| 9 | false-generalisation guard | no false generalisation | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is already the canonical pointwise normalisation form used by mathlib for the univariate operator; the bundled form `hasseDeriv_zero` exists next to it.

### Proof strategy — `MvPolynomial.hasseDeriv_zero_apply`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | monomial induction (`induction_on'` + `hasseDeriv_monomial`, evidence `hasseDeriv_zero_apply_alt`) also works; mathlib's univariate proof goes via `hasseDeriv_apply` + `Nat.choose_zero_right` | n/a (keep current `ext` + coefficient formula, 2 lines) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (two-line `ext` + `simp` with the operator's coefficient lemma; with the parent's `Finsupp.choose` spelling a `@[simp] Finsupp.choose_zero_right` makes it equally short, verified in evidence).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_zero_apply`

[A] Lean-Finder       "multivariate Hasse derivative with zero multi-index is the identity"   only univariate/Laurent (`Polynomial.hasseDeriv_zero`, `Polynomial.hasseDeriv_zero'`, `LaurentSeries.hasseDeriv_zero`) and unrelated `LineDeriv.iteratedLineDerivOp_zero`
[B] Loogle            `"hasseDeriv_zero"`   3 hits: `Polynomial.hasseDeriv_zero`, `Polynomial.hasseDeriv_zero'`, `LaurentSeries.hasseDeriv_zero`; no multivariate
[C] LeanSearch        "Hasse derivative of order zero applied to f equals f"   `Polynomial.hasseDeriv_zero'`, `Polynomial.hasseDeriv_zero`, `iteratedDeriv_zero`, ...; no multivariate
[D] Grep mathlib src  `hasseDeriv_zero_apply`, `hasseDeriv_zero'`, `hasseDeriv` across `.lake/packages/mathlib/Mathlib`: only Algebra/Polynomial/HasseDeriv.lean (l.82, 86), Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; nothing in Algebra/MvPolynomial or RingTheory/MvPowerSeries
[E] Name pattern      `MvPolynomial.hasseDeriv_zero_apply`, `MvPolynomial.hasseDeriv_zero` (grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard form (bundled `D_0 = id`, abstract HS-derivation normalisation).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); the univariate `Polynomial.hasseDeriv_zero'` is the template, and the parent operator itself is absent.

### Normal-form check — `MvPolynomial.hasseDeriv_zero_apply`

Equivalent formalisms this statement could take: pointwise `hasseDeriv 0 P = P`; bundled `hasseDeriv 0 = LinearMap.id` (`hasseDeriv_zero`, l.120); coefficientwise `∀ e, (hasseDeriv 0 P).coeff e = P.coeff e`.
Does mathlib already have a canonical form for this idea? yes for the univariate case: both `Polynomial.hasseDeriv_zero` (bundled, `@[simp]` in our project's version) and `Polynomial.hasseDeriv_zero'` (pointwise).
Our statement is stated against the canonical form? yes (pointwise form, simplified side `P` on the RHS).
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.hasseDeriv_zero_apply`

Alternative restatements attempted:
- pointwise `hasseDeriv 0 P = P` (current)
- bundled only (`hasseDeriv_zero`) with call sites using `LinearMap.id_apply` (works: `simp` proves the pointwise form from the `@[simp]` bundled lemma, evidence)
- name `hasseDeriv_zero'` (univariate mathlib convention)
Chosen restatement: current statement and name.
Justification: the pointwise form is what `LinearMap.ext` needs to build the bundled form, and is directly usable in `rw`; `_apply` is the current mathlib naming for pointwise versions of bundled-map equalities (preferred over the primed name for new code).

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_zero_apply`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `MvPolynomial.hasseDeriv_zero_apply`

Internal use count: 2 outside the declaring file (1 caller, Roth/Index.lean), plus 1 in the declaring file
External-to-file callers: 1 distinct file (Roth/Index.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/HasseDeriv.lean:121 | `LinearMap.ext hasseDeriv_zero_apply` (proves `hasseDeriv_zero`) |
| Roth/Index.lean:104 | `simpa [hasseDeriv_zero_apply] using hd` (in `index_eq_zero_iff`) |
| Roth/Index.lean:105 | `index_le_weight (r := r) (d := 0) (by simpa [hasseDeriv_zero_apply] using h)` (in `index_eq_zero_iff`) |

Inline-derivation grep: (none) — `grep -rn "hasseDeriv 0\|hasseDeriv (0" Roth/` finds only the two declarations themselves; no proof re-derives `Δ_0 = id` from the coefficient formula.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_zero_apply` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib.
  - Result: fails
  - Notes: no mathlib operator to specialise.

Attempt 2: `LinearMap.congr_fun hasseDeriv_zero P` (one call to the project's bundled lemma).
  - Mathlib decls used: `LinearMap.congr_fun`, project `hasseDeriv_zero`
  - Result: circular — `hasseDeriv_zero` is proved from this lemma; the non-circular content is `ext` + `coeff_hasseDeriv` + `hasseCoeff 0 k = 1` (or monomial induction), a real (if short) proof.
  - Notes: this is the standard bundled/pointwise pair, as in mathlib's `Polynomial.hasseDeriv_zero'`/`hasseDeriv_zero`.

Conclusion: NOT-COMPOSABLE (from mathlib; the operator is new)

## Verdict: `MvPolynomial.hasseDeriv_zero_apply`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): `D_0 = id` is the normalisation of Hasse(-Schmidt) derivatives (nLab; arXiv 1807.10502, 1106.1391, 2509.00887; multivariate Hasse derivatives in arXiv 1310.6482, 2403.19824); the project paper uses `Δ_0 P = P` explicitly (clean.tex l.567).
- Generality analysis (Phase 4): MAXIMALLY GENERAL; Phase 4c: no modern idiom move.
- Mathlib search (Phase 5): not in mathlib; univariate template `Polynomial.hasseDeriv_zero'`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` was assessed YES-but-generalise-first (multivariate Hasse derivative absent from mathlib; ship with `Finsupp.choose` coefficients). Every operator family in mathlib carries its order-zero normalisation in both a bundled and a pointwise form (`Polynomial.hasseDeriv_zero` / `Polynomial.hasseDeriv_zero'`, `LaurentSeries.hasseDeriv_zero`, `iteratedDeriv_zero`); this lemma is the pointwise one for the multivariate operator, and the bundled `hasseDeriv_zero` is proved from it. The specific gap is that `Mathlib/Algebra/MvPolynomial/` has `pderiv` but no Hasse derivative and hence no normalisation lemma; any upstream `MvPolynomial.hasseDeriv` PR needs exactly this lemma (it is also what the composition rule `Δ_d Δ_e = binom(d+e, d) Δ_{d+e}` reduces to at `e = 0`, and what multiplicity/index arguments use at order zero, as in Roth/Index.lean).

The statement itself needs no change: no hypotheses, `CommSemiring R` forced by `MvPolynomial`, name already follows the modern `_apply` convention. The parent's generalisation (`hasseCoeff` to `Finsupp.choose`) touches only the proof, which stays two lines once `Finsupp.choose_zero_right` is `@[simp]` (verified in evidence). Hence YES-add-as-is, bundled with the parent PR rather than as a standalone contribution.

WHY add it: it supplies the missing order-zero normalisation for the multivariate Hasse derivative, mirroring `Polynomial.hasseDeriv_zero'`; with it, `simp` normalises `Δ_0` away, and the bundled `hasseDeriv_zero : hasseDeriv 0 = LinearMap.id` follows by `LinearMap.ext`, so `LinearMap`-level lemmas (`LinearMap.id_apply`, `LinearMap.id_comp`) apply to `Δ_0`.
Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
Proposed PR title:            "feat(Algebra/MvPolynomial): multivariate Hasse derivatives"
PR grouping (if applicable):  ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`, `coeff_hasseDeriv`, `hasseDeriv_zero` (bundled, `@[simp]`) in one PR.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.hasseDeriv_zero_apply` — confirm no easy further weakening (expected none)
  - [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_zero_apply` — full audit + diff gates
  - [ ] Pick a mathlib reviewer based on `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/HasseDeriv.lean` recent commits

---

## Next step

Ship unchanged as `MvPolynomial.hasseDeriv_zero_apply` (proof adapted to the parent's `Finsupp.choose` spelling) in the parent's PR to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, next to `@[simp] hasseDeriv_zero`; locally keep as is (optionally drop the probably-redundant `simpa` arguments at Roth/Index.lean:104-105, since `@[simp] hasseDeriv_zero` already covers them).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_zero_apply/altproofs_and_compose.lean` (compiles with `lake env lean`, no errors or warnings): `hasseDeriv_zero_apply_alt` (monomial induction, with `-hasseDeriv_zero` to avoid circularity), `hasseDeriv_zero_apply_choose` (proof under the parent's `Finsupp.choose` spelling with a `@[simp] Finsupp.choose_zero_right`), and an `example` showing plain `simp` proves the statement from the project's `@[simp] hasseDeriv_zero`.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `"hasseDeriv_zero"`: 3 univariate/Laurent hits; LeanSearch and Lean-Finder: univariate hits only; grep of mathlib for `hasseDeriv_zero_apply` / `hasseDeriv_zero'` / `hasseDeriv`: univariate only. `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1-3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseDeriv_zero_apply Roth/` and `grep -rn "hasseDeriv 0" Roth/` for Used-by, call sites and inline derivations; `grep -n "Delta_0" .mathlib-quality/references/clean.tex` (l.567).
