---
decl: MvPolynomial.taylor_eq_zero_iff
file: Roth/Taylor.lean
line: 192
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multivariate analogue of mathlib's simp lemma Polynomial.taylor_eq_zero (stated over a Semiring), absent for MvPolynomial; the project proves it over CommRing via injectivity, but a compiled top-total-degree-coefficient proof shows it holds over any CommSemiring, where injectivity itself fails.
action: Upstream in the MvPolynomial.taylor PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) restated over CommSemiring, named taylor_eq_zero to mirror Polynomial.taylor_eq_zero, with helper coeff_taylor_of_totalDegree_le (evidence variants.lean); locally keep (implicit simp uses at Roth/Index.lean:80 and :169).
---

# MvPolynomial.taylor_eq_zero_iff

## Inventory entry

### `theorem MvPolynomial.taylor_eq_zero_iff`
- **Type**: `∀ {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A), taylor α P = 0 ↔ P = 0`
- **What**: A multivariate polynomial vanishes iff its translate `P(X + α)` vanishes. Tagged `@[simp]`.
- **How**: one term, `(taylor_injective α).eq_iff' (map_zero _)`: injectivity of translation (project lemma `taylor_injective`) applied against `taylor α 0 = 0`.
- **Hypotheses**: `[CommRing A]` (section variable; not needed, see Phase 4); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.taylor_injective`
- **Used by**: never referenced by name (`grep -rn taylor_eq_zero_iff Roth/` gives only its declaration). As a `@[simp]` lemma it is the natural closer for the `simp`/`simpa` calls on translated polynomials in Roth/Index.lean:80 (`exists_weight_eq_index`, support of `taylor α P` nonempty from `hP : P ≠ 0`) and Roth/Index.lean:169 (`hfin`, `weightedOrder` of `↑(taylor α R)` is not `⊤` for `R ≠ 0`); these implicit uses were not individually traced with `simp?` (to save Lean runs), so they are recorded as probable.
- **Visibility**: public
- **Lines**: 190–193 (docstring 190, attribute 191, statement 192, proof 193), proof length 1 line
- **Notes**: Mathlib's univariate counterpart is `Polynomial.taylor_eq_zero` (name without `_iff`), and there the dependency runs the other way: `Polynomial.taylor_injective := (injective_iff_map_eq_zero' _).2 (taylor_eq_zero r)`.

## Junk check (Step 8)
- Used anywhere? Not by name; probably used by `simp` at Roth/Index.lean:80 and :169 (it is `@[simp]`).
- Wrapper of 1–2 mathlib calls? It is one mathlib call (`Function.Injective.eq_iff'`) on the project lemma `taylor_injective`; the operator is not in mathlib, so no mathlib replacement exists.
- Does mathlib have it? Not for `MvPolynomial`. Univariate: `Polynomial.taylor_eq_zero` (Mathlib/Algebra/Polynomial/Taylor.lean:104, `[Semiring R]`, simp) and `Polynomial.comp_X_add_C_eq_zero_iff` (Mathlib/Algebra/Polynomial/AlgebraMap.lean:518).
- Too specific / inline? No: it is the simp normal form for "translate is zero", which mathlib has univariately.
- Well-chosen? Yes, but the typeclass is too strong (Phase 4) and the name differs from mathlib's univariate `taylor_eq_zero`.
- Conclusion: `KEEP`. Action: keep locally; upstream in the generalised form.

## Mathlibable assessment (Step 9)

Not private, not `_aux`, docstring not internal/auxiliary, Step 8 said KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds no `MvPolynomial.taylor_eq_zero_iff` (`theorem taylor_eq_zero` occurs only in namespace `Polynomial`). Not a glue lemma (it is not `rfl`/`Iff.rfl`/unfolding, and, as Phase 4 shows, its content is strictly more than the injectivity of the parent), so the full workflow is run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` elaborates with no diagnostics in lean-lsp)
- decl `MvPolynomial.taylor_eq_zero_iff`: resolved at Roth/Taylor.lean:192
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)`, its coefficients as Hasse derivatives, and Taylor's expansion.

### Statement (Phase 1)

`MvPolynomial.taylor_eq_zero_iff` is a theorem stating the following:

Let `A` be a commutative ring, `σ` a set of variables and `α ∈ A^σ`. For `P ∈ A[X_σ]`, the translate `P(X + α)` is the zero polynomial if and only if `P` is the zero polynomial. Equivalently the translation map has trivial kernel.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `A : Type*`, `[CommRing A]` — coefficient ring.
- `α : σ → A` — translation vector.
- `P : MvPolynomial σ A` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `P(X + α) = 0 ⇔ P = 0`.

Conclusion (Lean): `taylor α P = 0 ↔ P = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API corollary of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | polynomial p(x+a) = 0 implies p = 0 Taylor shift leading coefficient preserved semiring | partial | Taylor shift `p(x) ↦ p(x + a)` keeps the leading coefficient (`q_n = a_n`, Shaw–Traub) | planetcalc 7726, codeforces blog 99646; the leading-coefficient fact is exactly mathlib's univariate proof, and it needs no negation |
| 2 | WebSearch (general form) | translation automorphism multivariate polynomial highest degree homogeneous component preserved f(x+a) | partial | top homogeneous component `h̄` (arXiv 2401.12523); translations as automorphisms over finite fields (arXiv 1709.04566) | top-degree component of `f(x+a)` equals that of `f`, which gives the statement with no ring hypothesis beyond a commutative semiring |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" multivariate polynomial nonzero kernel trivial Hasse derivative Taylor expansion | partial | multivariate Taylor expansion `P(Y) = Σ_i (Δ_i P)(a)(Y − a)^i` via Hasse derivatives (arXiv 1812.07020, Wikipedia "Hasse derivative") | coefficient formula `coeff_d P(X+α) = (Δ_d P)(α)` is the project's `coeff_taylor`; no explicit kernel statement in sources (regarded as immediate) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for injective / eq_zero / `X+\alpha` | partial | l.547 "Let `P_α(X)=P(X+α)`, whose coefficient at `d` is `(Δ_d P)(α)`"; l.544 "Taylor's theorem shows that at least one derivative at the chosen point is nonzero" | the paper uses exactly this fact (nonzero `P` has nonzero translate) to make the index an attained minimum; real-coefficient setting |
| 6 | nLab | affine space / automorphism / translation | partial | translations of affine space act by algebra automorphisms on coordinate rings | no polynomial-specific lemma; the automorphism form presupposes a ring |
| 7 | nCatLab | — | n/a | — | not a categorical statement beyond the action remark in row 6 |
| 8 | Stacks Project | — | n/a | — | translation is the `G_a^n` action on `A^n`; Stacks has no elementary polynomial-ring lemma of this kind (checked: no tag on translates of polynomials) |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | no dedicated thread; regarded as immediate |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | partial | arXiv 2401.12523 (2024) highest-degree homogeneous components; 2311.08873 (2023) shift-operator polynomial method | no new form |

### Literature summary (Phase 3)

Concept identified as: trivial kernel of the translation (Taylor shift) `P ↦ P(X + α)`; equivalently, translation preserves the top-degree homogeneous component (hence the total degree).
Sources agree on the standard form: yes.
Most general standard form: over any commutative semiring `A`, `P(X + α)` and `P` have the same top-degree homogeneous component, so `P(X + α) = 0 ⇔ P = 0`. Over rings it also follows from invertibility of translation.
Generality dimensions where the literature varies:
  - coefficient ring: field to commutative ring in most sources; the degree argument (mathlib's univariate `Polynomial.taylor_eq_zero`, `[Semiring R]`) needs only a (commutative) semiring. Ours is CommRing, which is narrower.
  - proof route: invertibility (needs `-α`) vs. degree/leading term (no negation).
Disagreement with the literature: the project derives the result from injectivity, which forces `CommRing`; the literature's degree argument does not.

### Generality analysis — `MvPolynomial.taylor_eq_zero_iff`

Literature-standard form (from Phase 3): `taylor α P = 0 ↔ P = 0` over a commutative semiring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing A]` | commutative ring | commutative semiring | YES (verified) | compiled in evidence item 2: the coefficient of `taylor α P` at any `d` with `totalDegree P ≤ d.degree` equals `coeff d P` (`hasseDeriv d P = C (coeff d P)` by `coeff_hasseDeriv` and `coeff_eq_zero_of_totalDegree_lt`), and taking `d` of maximal degree in the support gives `P = 0`. Works over `ℕ∞`, where injectivity fails (evidence item 4 vs. the `taylor_injective` counterexample) |
| 2 | `α : σ → A` | arbitrary | vector in `A^σ` | no | already general |
| 3 | `σ : Type*` | arbitrary | finite in most sources | no (already more general) | — |
| 4 | commutativity | forced | — | no | `MvPolynomial σ R` requires `CommSemiring R` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`CommRing` to `CommSemiring`, verified: evidence file compiles with no diagnostics).
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem coeff_taylor_of_totalDegree_le {σ R : Type*} [CommSemiring R] (α : σ → R)
    (P : MvPolynomial σ R) {d : σ →₀ ℕ} (hd : P.totalDegree ≤ d.degree) :
    (taylor α P).coeff d = P.coeff d

@[simp]
theorem taylor_eq_zero {σ R : Type*} [CommSemiring R] (α : σ → R) (P : MvPolynomial σ R) :
    taylor α P = 0 ↔ P = 0
```

Cost of restatement: CHEAP — mechanical; the full proof (about 20 lines including the helper) is in the evidence file. The project's CommRing call sites are unaffected (evidence item 3).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | `RingHom.ker (taylor α) = ⊥` is an equivalent spelling but the iff is the simp form |
| 5 | field-specific to semiring? | yes | `CommRing` to `CommSemiring` (Phase 4, verified) | matches the univariate `Polynomial.taylor_eq_zero` which is `[Semiring R]` |
| 6 | higher-categorical / bundled? | no | — | — |
| 7 | concrete index to general? | no | already general | — |
| 8 | concrete-via-abstract? | no | proof uses only `taylor_injective`; statement is about the project operator itself | — |
| 9 | false-generalisation guard | no false generalisation | the CommSemiring statement is the same mathematical object (same operator, same predicate) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only improvement is the literature/univariate-precedent typeclass weakening already recorded in Phase 4b (reason LITERATURE-WEAKENING); the statement shape is already mathlib's.

### Proof strategy — `MvPolynomial.taylor_eq_zero_iff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `coeff_taylor_of_totalDegree_le` (multivariate analogue of `Polynomial.coeff_taylor_natDegree` / `leadingCoeff_taylor`), naturally followed by `totalDegree_taylor` | CHEAP (helper compiles in evidence item 2) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove via preservation of top-total-degree coefficients (as mathlib's univariate `taylor_eq_zero` goes via `leadingCoeff_taylor`), and then derive `taylor_injective` from it as mathlib does (`(injective_iff_map_eq_zero' _).2 (taylor_eq_zero α)`), or keep the left-inverse proof of injectivity.
  - Cost: CHEAP
  - Missing mathlib API (if any): `MvPolynomial.coeff_taylor_of_totalDegree_le` (new, ships in the same PR).
  - Would refactoring make the proof strictly shorter / cleaner? No (longer), but it is strictly more general, which is the point.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.taylor_eq_zero_iff`

[A] Lean-Finder       "multivariate polynomial composed with translation X_i + a_i is zero iff polynomial is zero"   `Polynomial.comp_X_add_C_eq_zero_iff`, `Polynomial.comp_X_add_C_ne_zero_iff`, `MvPolynomial.expand_eq_zero`, `Polynomial.expand_eq_zero`, `Polynomial.taylor_eq_zero` (all univariate or unrelated); no multivariate translation
[B] Loogle            `MvPolynomial.aeval _ _ = 0 ↔ _ = 0`   `MvPolynomial.aeval_algebraMap_eq_zero_iff`, `..._of_injective` (scalar-tower statements, unrelated)
[C] LeanSearch        "MvPolynomial aeval (fun i => X i + C (a i)) p = 0 iff p = 0"   `MvPolynomial.aeval_eq_zero`, `algebraicIndependent_iff`, `MvPolynomial.monomial_eq_zero`, `MvPolynomial.coe_eq_zero_iff`; no hit
[D] Grep mathlib src  `taylor_eq_zero`, `taylor` under Mathlib/Algebra/MvPolynomial and Mathlib/RingTheory/MvPolynomial, `comp_X_add_C_eq_zero_iff`   `taylor_eq_zero` only in Mathlib/Algebra/Polynomial/Taylor.lean:104 (univariate, `[Semiring R]`); no `taylor` at all in the MvPolynomial directories; `Polynomial.comp_X_add_C_eq_zero_iff` at AlgebraMap.lean:518
[E] Name pattern      `MvPolynomial.taylor_eq_zero_iff`, `MvPolynomial.taylor_eq_zero` (namespace-aware grep)   no hits

Searched for both the user's form (CommRing, via injectivity) and the literature-standard form (CommSemiring, via top-degree component).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); univariate template `Polynomial.taylor_eq_zero` (`[Semiring R]`, simp).

### Normal-form check — `MvPolynomial.taylor_eq_zero_iff`

Equivalent formalisms this statement could take: `taylor α P = 0 ↔ P = 0` (current); `taylor α P ≠ 0 ↔ P ≠ 0`; `RingHom.ker (taylor α) = ⊥`; `(taylor α P).support.Nonempty ↔ P.support.Nonempty`.
Does mathlib already have a canonical form for this idea? yes (univariate): `@[simp] Polynomial.taylor_eq_zero : taylor r f = 0 ↔ f = 0`.
Our statement is stated against the canonical form? yes (identical shape; `P = 0` on the RHS).
RHS convention respected? yes.

### Syntactic generality — `MvPolynomial.taylor_eq_zero_iff`

Alternative restatements attempted:
- `taylor α P = 0 ↔ P = 0` over CommRing (current; evidence item 1)
- same over CommSemiring (evidence item 2)
- `≠` version (derivable by `.not`, as univariate `comp_X_add_C_ne_zero_iff`)
Chosen restatement: the CommSemiring `=` iff, named `taylor_eq_zero` to match `Polynomial.taylor_eq_zero`.
Justification: the `= 0 ↔ = 0` form is the simp normal form; dropping to CommSemiring makes simp fire for semiring coefficients too.

### Superfluous-argument audit — `MvPolynomial.taylor_eq_zero_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing A]` | no | `CommSemiring` suffices (evidence item 2); the ring structure is only used through the route via `taylor_injective` |
| 2 | `α`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (`CommRing` to `CommSemiring`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.taylor_eq_zero_iff`

Internal use count: 0 by name (outside the declaring file and inside it); probable implicit `simp` uses below
External-to-file callers: 1 distinct file (implicit simp, Roth/Index.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:80 | `simpa using hP` (support of `taylor α P` nonempty; simp needs `taylor α P = 0 ↔ P = 0`) — probable implicit use |
| Roth/Index.lean:169 | `... (taylor α R : MvPowerSeries σ ℝ).weightedOrder ... ≠ ⊤ := by simp` — probable implicit use |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.taylor_eq_zero_iff`?):
  - Roth/Index.lean:242 uses the univariate `Polynomial.taylor_eq_zero` (a different operator), not a re-derivation of this lemma. Otherwise (none): `grep -rn "taylor_injective\|eq_iff'" Roth/` shows only Roth/Taylor.lean:187, 193.

### Composition check (Phase 6)

Can `MvPolynomial.taylor_eq_zero_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(taylor_injective α).eq_iff' (map_zero _)` (current proof).
  - Mathlib decls used: `Function.Injective.eq_iff'`, `map_zero`; but `taylor` and `taylor_injective` are project declarations absent from mathlib.
  - Result: succeeds only given the parent operator; CommRing only.
  - Notes: the statement cannot be written without the new operator.

Attempt 2 (CommSemiring): via `coeff_taylor`, `coeff_hasseDeriv`, `coeff_eq_zero_of_totalDegree_lt`, `Finset.exists_mem_eq_sup`.
  - Result: succeeds (evidence item 2) but is a genuine roughly 20-line proof with a helper lemma, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.taylor_eq_zero_iff`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): translation preserves the top-degree homogeneous component (rows 1–2) and hence has trivial kernel over any commutative semiring; mathlib's univariate version is stated over `[Semiring R]`.
- Generality analysis (Phase 4): STRICTLY NARROWER; `CommRing` to `CommSemiring` verified by a compiled proof (evidence item 2), including over `ℕ∞` (item 4), where injectivity fails.
- Mathlib search (Phase 5): not in mathlib; univariate template `Polynomial.taylor_eq_zero` (Mathlib/Algebra/Polynomial/Taylor.lean:104).
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent from mathlib).

**Rationale:**

This is the multivariate version of mathlib's `@[simp] Polynomial.taylor_eq_zero`, which is basic API for translation. The parent `MvPolynomial.taylor` is YES-add-as-is, so the lemma belongs in the same PR. The project's statement is too narrow, though. It is derived from `taylor_injective`, which forces `CommRing`, and the `taylor_injective` report includes a compiled counterexample showing that injectivity really fails over semirings. Zero-detection does not need injectivity. Translation leaves every coefficient of maximal total degree unchanged, because `Δ_d P = C (coeff d P)` when `|d| ≥ totalDegree P`. Taking a support element of maximal degree then gives `P = 0`. So the lemma holds over every commutative semiring, which matches the univariate mathlib lemma (`[Semiring R]`, proved through `leadingCoeff_taylor`). With this restatement the lemma is strictly stronger than "injective implies trivial kernel" and is no longer a corollary of `taylor_injective`. Mathlib's univariate file derives `taylor_injective` from `taylor_eq_zero`, and the same order works here.

Reason for the generalisation: LITERATURE-WEAKENING (Phase 4b: `CommRing` is superfluous; the literature's top-degree argument and the univariate mathlib precedent use only a semiring).

Proposed restatement:
```lean
theorem coeff_taylor_of_totalDegree_le {σ R : Type*} [CommSemiring R] (α : σ → R)
    (P : MvPolynomial σ R) {d : σ →₀ ℕ} (hd : P.totalDegree ≤ d.degree) :
    (taylor α P).coeff d = P.coeff d := by
  sorry  -- proved in evidence/MvPolynomial.taylor_eq_zero_iff/variants.lean

@[simp]
theorem taylor_eq_zero {σ R : Type*} [CommSemiring R] (α : σ → R) (P : MvPolynomial σ R) :
    taylor α P = 0 ↔ P = 0 := by
  sorry  -- proved in evidence/MvPolynomial.taylor_eq_zero_iff/variants.lean
```
Estimated cost of regeneralisation: CHEAP (both proofs already compile in the evidence file).

Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`)
PR grouping:                  ship inside "feat(Algebra/MvPolynomial): add MvPolynomial.taylor" with `taylor_zero`, `taylor_taylor`, `taylor_neg_taylor` / `taylorEquiv`, `taylor_injective` (optionally proved as `(injective_iff_map_eq_zero' _).2 (taylor_eq_zero α)`, mirroring the univariate file), `taylor_inj`, and the new helper `coeff_taylor_of_totalDegree_le` (natural follow-up: `totalDegree_taylor`, analogue of `Polynomial.natDegree_taylor`).

Next action: run `/generalise MvPolynomial.taylor_eq_zero_iff` (target: CommSemiring, name `taylor_eq_zero`) before opening the PR; locally the project can move the lemma to the `CommSemiring` section with the evidence proof, which leaves its CommRing uses unchanged.

---

## Next step

Restate over `CommSemiring` as `MvPolynomial.taylor_eq_zero` (simp), with the helper `coeff_taylor_of_totalDegree_le`, using the compiled proofs in `.mathlib-quality/overview/evidence/MvPolynomial.taylor_eq_zero_iff/variants.lean`; ship in the `MvPolynomial.taylor` upstream PR. Locally there are no by-name call sites; the probable implicit simp uses (Roth/Index.lean:80, :169) are over `ℝ` and unaffected.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_eq_zero_iff/variants.lean` (checked with `lean_diagnostic_messages`: no diagnostics): (1) project statement with project proof; (2) `coeff_taylor_of_totalDegree_le` and `taylor_eq_zero_iff'` over `CommSemiring` (proof: `hasseDeriv d P = C (coeff d P)` by `coeff_hasseDeriv`, `hasseCoeff d d = 1`, `coeff_eq_zero_of_totalDegree_lt`, `Finsupp.degree_eq_zero_iff`; then `Finset.exists_mem_eq_sup` picks a maximal-degree support element); (3) the generalised lemma specialises to the CommRing statement; (4) it applies over the semiring `ℕ∞` with `α = ⊤`, where `taylor_injective` fails (counterexample in `.mathlib-quality/overview/evidence/MvPolynomial.taylor_injective/variants.lean`, item 5).
- Searches: WebSearch ×3 (table rows 1–3); Lean-Finder, LeanSearch, Loogle (Phase 5 block); mathlib greps for `taylor_eq_zero`, `taylor` in MvPolynomial directories, `comp_X_add_C_eq_zero_iff`. ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn taylor_eq_zero_iff Roth/` (declaration only); `grep -rn taylor Roth/` outside Taylor.lean (Roth/Index.lean simp sites 80, 169; univariate use at 242); `.mathlib-quality/references/clean.tex` l.544–550.
