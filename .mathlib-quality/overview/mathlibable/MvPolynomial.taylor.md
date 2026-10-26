---
decl: MvPolynomial.taylor
file: Roth/Taylor.lean
line: 42
kind: def
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Multivariate translation P to P(X + α) is standard (multivariate Taylor expansion with Hasse-derivative coefficients) and mathlib has only the univariate Polynomial.taylor / taylorAlgHom / algEquivAevalXAddC; the one-line def is justified as the named API anchor (coeff_taylor, taylor_taylor, eval_taylor, Index.lean) exactly as Polynomial.taylor is in mathlib, and is already maximally general.
action: Upstream with the MvPolynomial.hasseDeriv PR as Mathlib/Algebra/MvPolynomial/Taylor.lean (taylor, taylor_X, taylor_C, taylor_monomial, coeff_taylor, eval_taylor, taylor_taylor, taylor_zero, taylor_map, taylor_rename, degreeOf_taylor_le, taylor_injective) plus the compiled bridge uniqueAlgEquiv_taylor to Polynomial.taylor; locally keep as is (used in Roth/Index.lean).
---

# MvPolynomial.taylor

## Inventory entry

### `def MvPolynomial.taylor`
- **Type**: `{σ R : Type*} → [CommSemiring R] → (α : σ → R) → MvPolynomial σ R →ₐ[R] MvPolynomial σ R`
- **What**: The translation (multivariate Taylor shift) `P ↦ P(X + α)`, the `R`-algebra endomorphism sending each variable `X j` to `X j + α j`.
- **How**: `aeval fun j ↦ X j + C (α j)` (one line, mathlib's `MvPolynomial.aeval`).
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `[]`
- **Used by**: Roth/Taylor.lean (taylor_apply, taylor_X, taylor_C, taylor_monomial, private coeff_taylor_monomial_single_add_aux / coeff_taylor_monomial_aux, coeff_taylor, eval_taylor, taylor_taylor, taylor_zero, taylor_map, taylor_rename, degreeOf_taylor_le, taylor_neg_taylor, taylor_injective, taylor_eq_zero_iff, eq_sum_box_hasseDeriv); Roth/Index.lean (definition of `index` l.59, mem_support_taylor_iff l.63, l.71, l.79-80, weightedOrder form l.145-169, l.202-203). Roth/Index.lean:237 uses mathlib's univariate `Polynomial.taylor`, not this one.
- **Visibility**: public
- **Lines**: 42–43, proof length 1 line (definition body)
- **Notes**: `noncomputable`. Bundled directly as an `AlgHom` (mathlib's univariate `Polynomial.taylor` is a `LinearMap` over `Semiring R` with a separate `taylorAlgHom` over `CommSemiring R`; for `MvPolynomial` `CommSemiring R` is forced, so the AlgHom bundling loses nothing).

## Junk check (Step 8)
- Used anywhere? Yes: 16 project lemmas in Roth/Taylor.lean and the definition of the index (Roth/Index.lean, about 10 occurrences).
- Wrapper of 1–2 mathlib calls? Yes, literally `aeval (fun j ↦ X j + C (α j))` (equivalently `bind₁`, rfl, evidence file). But it is the named anchor for a whole API (`coeff_taylor` is Taylor's theorem), exactly as mathlib names `Polynomial.taylor := f.comp (X + C r)`.
- Does mathlib have it? No multivariate version (Phase 5); only univariate `Polynomial.taylor`, `Polynomial.taylorAlgHom`, `Polynomial.taylorEquiv`, `Polynomial.algEquivAevalXAddC`.
- Too specific / inline? No; inlining would make `coeff_taylor`, `index`, and the support lemmas state `aeval (fun j ↦ X j + C (α j)) P` everywhere.
- Well-chosen definition? Yes; matches the paper ("`P_α(X) = P(X+α)`") and mathlib's univariate naming.
- Conclusion: `KEEP` — action: keep; upstream (see verdict).

## Mathlibable assessment (Step 9)

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` compiles)
- decl `MvPolynomial.taylor`: resolved at Roth/Taylor.lean:42
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: `taylor α P = P(X + α)`, whose coefficient at `d` is `(Δ_d P)(α)`.

### Statement (Phase 1)

`MvPolynomial.taylor` is a definition of the following: for a commutative semiring `R`, a set of variables `σ` and a point `α ∈ R^σ`, the translation by `α` is the `R`-algebra endomorphism `τ_α : R[X_σ] → R[X_σ]`, `τ_α(P)(X) = P(X + α)`, i.e. the unique `R`-algebra map with `X_j ↦ X_j + α_j`. Its main property (proved in the file as `coeff_taylor`) is the multivariate Taylor formula `P(X + α) = Σ_d (Δ_d P)(α) X^d` with `Δ_d` the multivariate Hasse derivative.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables (arbitrary).
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `α : σ → R` — the translation vector.

Hypotheses (Lean side):
- none.

Conclusion (math): the translation endomorphism `τ_α`.

Conclusion (Lean): n/a — definition (`MvPolynomial σ R →ₐ[R] MvPolynomial σ R`).

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main definitions` of Roth/Taylor.lean; it is the named operator underlying multivariate Taylor's theorem and the definition of the index (a named concept, though a light-weight one).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | the def is semireducible and proofs unfold it freely (`simp [taylor, ...]` in eval_taylor, taylor_taylor, taylor_map, taylor_rename); no barrier role |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes      | consumers: `coeff_taylor` (Taylor's theorem), `index` and `mem_support_taylor_iff` in Roth/Index.lean, `eq_sum_box_hasseDeriv`; direct mathlib precedent: the univariate `Polynomial.taylor` is also a one-line wrapper (`f.comp (X + C r)`) kept for exactly this API role, with ~30 lemmas |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Taylor expansion multivariate polynomial P(x+a) coefficients Hasse derivatives translation | yes | `F(X+Z) = Σ_i (D^i F)(X) Z^i`, multi-index; coefficient of `Z^i` in `P(a+Z)` is `(D^i P)(a)` | arXiv 1402.0643, 1509.00279, 1310.6482 (Tao, polynomial method), 1812.07020; exactly our `coeff_taylor` |
| 2 | WebSearch (general form) | translation automorphism polynomial ring several variables x_i mapsto x_i + a_i commutative ring | partial | translations `(x_1 + b_1, ..., x_n + b_n)` as the translation subgroup of affine automorphisms of `R[x_1..x_n]` | arXiv 1709.04510, 0707.3151 (over commutative rings); most general form is substitution `X ↦ X + a` over any commutative ring; no further generality dimension |
| 3 | WebSearch (named-after / aliases) | "shift operator" OR "Taylor shift" multivariate polynomial algorithm | yes | "Taylor shift" `p(x+a)`, multivariate via affine change of variables / shifted power products `(x_i - b_i)` | arXiv cs/0403022, Bell Labs sparse shifts, Maple arXiv 2106.15519; alias "Taylor shift" matches mathlib's univariate name `taylor` |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for taylor / P(X+α) / translat | yes | l.547-549 Lean note: "Let `P_α(X)=P(X+α)`, whose coefficient at `d` is `(Δ_d P)(α)`"; §4 Theorem (Taylor's expansion in several variables); l.600-629 translated polynomials | project source paper |
| 6 | nLab | nLab Hasse-Schmidt derivative (Taylor / several indeterminates) | partial | Hasse derivatives as coefficients of `P(x + y)` | translation itself has no separate nLab entry; it is the substitution underlying the Hasse–Schmidt derivative (same pages cited in the hasseDeriv report) |
| 7 | nCatLab | — | n/a | — | not a categorical concept (a concrete substitution endomorphism of a polynomial ring) |
| 8 | Stacks Project | — | n/a | — | translation of affine space is elementary; Stacks has no standalone tag for `P(X+a)` on polynomial rings |
| 9 | MathOverflow / Math.SE | (via #1 and #3: multiplicity-method and Taylor-shift literature) | partial | same `P(x+a) = Σ (Δ_i P)(a) x^i` | no dedicated thread surfaced; usage consistent |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2603.03841 (2026, list decoding), 2608.14726 (2026, Casas-Alvero), 2106.15519 (2021) | all use the substitution `X ↦ X + a` with Hasse-derivative coefficients |

### Literature summary (Phase 3)

Concept identified as: translation / Taylor shift of a multivariate polynomial, `P(X) ↦ P(X + α)`, with Taylor's formula `P(X + α) = Σ_d (Δ_d P)(α) X^d`.
Sources agree on the standard form: yes.
Most general standard form: over any commutative (semi)ring `R` and any finite (here arbitrary) set of variables, the `R`-algebra map `X_j ↦ X_j + α_j`; over a ring it is an automorphism with inverse translation by `-α`.
Generality dimensions where the literature varies:
  - coefficient ring: field (coding theory, affine automorphism groups) to commutative ring; ours is commutative semiring, the most general available for `MvPolynomial`.
  - shift: constant vector `α ∈ R^σ` (all sources) vs a general affine / polynomial substitution (that is `aeval` / `bind₁`, a different, already-present concept).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.taylor`

Literature-standard form (from Phase 3): the `R`-algebra endomorphism `X_j ↦ X_j + α_j` of `R[X_σ]`, `R` a commutative semiring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative (semi)ring | no | `MvPolynomial σ R` itself requires `CommSemiring R` (verified failure for `[Semiring R]` in the hasseDeriv evidence `weaken_semiring_fails.lean`, same type constructor) |
| 2 | `σ : Type*` | arbitrary | finite set of variables | no (already more general) | — |
| 3 | `α : σ → R` | arbitrary function | point of `R^n` | no | finitely supported `σ →₀ R` would be strictly less general; functions match `MvPolynomial.eval` |
| 4 | bundling `→ₐ[R]` | AlgHom | algebra endomorphism | n/a | strongest natural bundling; an `AlgEquiv` companion exists only over `CommRing` (project has `taylor_neg_taylor`, `taylor_injective`) — a companion, not a weakening |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Cost of restatement: n/a (none needed)

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | purely algebraic |
| 3 | construction vs universal property? | no | it is already defined by the universal property of `MvPolynomial` (`aeval`) | — |
| 4 | set-with-predicate to bundled substructure? | no | already bundled `AlgHom` | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | concrete endomorphism | — |
| 7 | concrete index to general? | no | `α : σ → R` already over arbitrary `σ` | — |
| 8 | concrete-via-abstract? | no | body has no proof; the def is the abstract substitution itself | — |
| 9 | false-generalisation guard | no false generalisation | no generalisation proposed; companion `taylorEquiv` over `CommRing` and bridge `uniqueAlgEquiv_taylor` keep the same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: the definition is already the universal-property substitution (`aeval`) at full generality; the only mathlib-alignment items are additive companions (`taylorEquiv : MvPolynomial σ A ≃ₐ[A] MvPolynomial σ A` over `CommRing`, mirroring `Polynomial.taylorEquiv`, and the compiled bridge `uniqueAlgEquiv_taylor` to `Polynomial.taylor`), not restatements.

### Proof strategy — `MvPolynomial.taylor`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no (already `aeval`) | — | — |
| 5 | missing mathlib helpers | yes (for the API, not the def) | `MvPolynomial.hasseDeriv` (needed for `coeff_taylor`; parent report YES-but-generalise-first) | ship in the same PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (same shape as `Polynomial.taylorAlgHom` / `Polynomial.algEquivAevalXAddC := aeval (X + C t)`).
  - Missing mathlib API: multivariate Hasse derivative, for `coeff_taylor` (row 5).

### Diamond / defeq risk — `MvPolynomial.taylor`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines an `AlgHom`, no instances; only `R`-algebra structure on `MvPolynomial σ R` |
| 2 | Reducibility leak | none | plain semireducible def; `taylor α = aeval ...` and `= bind₁ ...` hold by `rfl` (evidence file) so unfolding is predictable; consumers use `taylor_apply` / `taylor_X` / `coeff_taylor` |
| 3 | Non-canonical unfolding | low | `simp [taylor]` exposes `aeval`, which is the canonical normal form for substitutions in mathlib; harmless |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | elaborates with `σ : Type 3`, `R = ℤ` (evidence file); `σ R : Type*` independent |
| 6 | Coercion ambiguity | none | standard `AlgHom` `FunLike`; name `MvPolynomial.taylor` does not clash (mathlib has `Polynomial.taylor`, a `LinearMap`, in another namespace). Minor naming-consistency point: univariate `taylor` is a `LinearMap` and `taylorAlgHom` the `AlgHom`; for `MvPolynomial` only the `AlgHom` makes sense (CommSemiring forced), so a single `taylor` is defensible, but a reviewer may ask for the `taylorAlgHom` spelling |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a (document the LinearMap-vs-AlgHom naming choice in the PR description)

### Mathlib search-status: `MvPolynomial.taylor`

[A] Lean-Finder       "algebra endomorphism of MvPolynomial sending X i to X i + C (a i), shift of variables"   no multivariate hit (`bind₁`, `rename`, univariate `algEquivAevalXAddC`, `taylorAlgHom`)
[B] Loogle            `(_ → _) → MvPolynomial _ _ →ₐ[_] MvPolynomial _ _`   only `rename`, `killCompl`, `bind₁` (general substitutions)
[C] LeanSearch        "translate multivariate polynomial by a point, P(X + a), Taylor expansion several variables"   only univariate `Polynomial.taylor*`, `algEquivAevalXAddC`, `taylorLinearEquiv`
[D] Grep mathlib src  `def taylor` (only Mathlib/Algebra/Polynomial/Taylor.lean, Analysis/Calculus/Taylor.lean, ContDiff/FaaDiBruno.lean, RingTheory/Polynomial/DegreeLT.lean); `X i + C` / `X j + C` in MvPolynomial files (only MonomialOrder.lean degree lemmas, Lie/CartanExists.lean ad hoc aeval); `taylor`/`subst`/`translat` defs in Algebra/MvPolynomial and RingTheory/MvPowerSeries (only `MvPowerSeries.subst`, general)   no multivariate translation
[E] Name pattern      `MvPolynomial.taylor`, `MvPolynomial.taylorAlgHom`, `MvPowerSeries.taylor`   no hits

Searched for both the user's form and the literature-standard form (translation automorphism / Taylor shift).

Concluded: found building blocks (`MvPolynomial.aeval`, `MvPolynomial.bind₁`, univariate `Polynomial.taylor`); the named multivariate translation with its Taylor-coefficient API is not in mathlib.

### Normal-form check — `MvPolynomial.taylor`

Equivalent formalisms: `aeval (fun j ↦ X j + C (α j))`; `bind₁ (fun j ↦ X j + C (α j))`; `eval₂Hom C (fun j ↦ X j + C (α j))`; in one variable, `Polynomial.taylor` transported along `uniqueAlgEquiv`.
Does mathlib already have a canonical form? For one variable yes (`Polynomial.taylor`, with `taylor_coeff : (taylor r f).coeff n = (hasseDeriv n f).eval r`). Ours is the multivariate analogue with the analogous `coeff_taylor`, and the bridge `uniqueAlgEquiv_taylor` (compiled) connects the two.
RHS convention respected? yes (`taylor_apply : taylor α P = aeval ... P`, `coeff_taylor : ... = eval α (hasseDeriv d P)`, mirroring mathlib).

### Syntactic generality — `MvPolynomial.taylor`

Alternative restatements attempted:
- `aeval (fun j ↦ X j + C (α j))` (current)
- `bind₁ (fun j ↦ X j + C (α j))` (rfl-equal, evidence file)
- `LinearMap` bundling as in univariate `Polynomial.taylor` (rejected: `CommSemiring` is forced anyway; AlgHom gives `map_mul`, `map_pow` for free, used in `coeff_taylor_monomial_single_add_aux`)
Chosen restatement: current.
Justification: the `AlgHom` bundling is the strongest available and every call site uses multiplicativity or `map_sum`.

### Superfluous-argument audit — `MvPolynomial.taylor`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial` |
| 2 | `σ` | yes | variables |
| 3 | `α : σ → R` | yes | translation vector |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `MvPolynomial.taylor`

Internal use count: 10 occurrences outside the declaring file (all in Roth/Index.lean); 16 lemmas inside Roth/Taylor.lean
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:59 | `sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))` (definition of `index`) |
| Roth/Index.lean:63 | `d ∈ (taylor α P).support ↔ eval α (hasseDeriv d P) ≠ 0` |
| Roth/Index.lean:71 | `csInf_le ((taylor α P).support.finite_toSet.image (weight r)).bddBelow` |
| Roth/Index.lean:79 | `(show (weight r '' ((taylor α P).support ...)).Nonempty by` |
| Roth/Index.lean:80 | `simpa using hP).csInf_mem ((taylor α P).support.finite_toSet.image (weight r))` |
| Roth/Index.lean:145 | `(((taylor α P : MvPowerSeries σ ℝ).weightedOrder fun j ↦ ...).toNat : ℝ) /` |
| Roth/Index.lean:148 | `set F : MvPowerSeries σ ℝ := ↑(taylor α P)` |
| Roth/Index.lean:169 | `((taylor α R : MvPowerSeries σ ℝ).weightedOrder ...) ≠ ⊤ := by simp` |
| Roth/Index.lean:202 | `weight (fun j ↦ l * r j) '' ((taylor α P).support : Set (σ →₀ ℕ)) =` |
| Roth/Index.lean:203 | `(l : ℝ)⁻¹ • (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))` |

Inline-derivation grep: Roth/Index.lean:237 (`index_unique`) uses univariate `Polynomial.taylor (α default) (uniqueAlgEquiv ℝ σ P)` and re-derives the coefficient identity through `uniqueAlgEquiv_hasseDeriv`; the compiled bridge `uniqueAlgEquiv_taylor` (evidence) would let it go through `MvPolynomial.taylor` instead. No re-derivation of `aeval (X + C α)` elsewhere.

### Composition check (Phase 6)

Can `MvPolynomial.taylor` be derived from mathlib in ≤3 chained calls?

Attempt 1: `aeval (fun j ↦ X j + C (α j))` (or `bind₁ ...`)
  - Mathlib decls used: `MvPolynomial.aeval` / `MvPolynomial.bind₁`, `X`, `C`
  - Result: succeeds as a term (the def is literally this, rfl).
  - Notes: composable as a value, but this is the one-liner itself; the API (`coeff_taylor` = Taylor's theorem, `taylor_taylor`, `eval_taylor`, `degreeOf_taylor_le`, injectivity) is not composable — `coeff_taylor` is a genuine induction over monomials using the univariate binomial expansion.
Attempt 2: reduce to `Polynomial.taylor` variable by variable via `finSuccEquiv` / `optionEquivLeft`
  - Result: fails as a ≤3-call composition (needs induction on the variable set; new proof).

Conclusion: COMPOSABLE as a term (one-liner), NOT-COMPOSABLE as an API; with the Phase-2b API-name exemption and the `Polynomial.taylor` precedent, the decision rests on the API, so treated as NOT-COMPOSABLE for verdict purposes.

## Verdict: `MvPolynomial.taylor`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): translation `P(X + α)` with Taylor formula `Σ_d (Δ_d P)(α) X^d` is standard (arXiv 1402.0643, 1509.00279, 1310.6482; project paper §4 and l.547).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (`CommSemiring` forced by `MvPolynomial`, arbitrary `σ`, arbitrary `α : σ → R`); Phase 4c: no modern-idiom restatement (already `aeval`).
- Risk (Phase 4.5): LOW.
- Mathlib search (Phase 5): not in mathlib; only univariate `Polynomial.taylor`, `taylorAlgHom`, `taylorEquiv`, `algEquivAevalXAddC`, and general substitutions `aeval` / `bind₁`.
- Composition check (Phase 6): one-liner term, but the API is NOT-COMPOSABLE; Phase 2b ONE-LINER WITH-EXEMPTION (API name).

**Rationale:**

Mathlib's `Mathlib/Algebra/Polynomial/Taylor.lean` provides the univariate Taylor shift `Polynomial.taylor r f = f.comp (X + C r)` with `taylor_coeff : (taylor r f).coeff n = (hasseDeriv n f).eval r`, injectivity, `taylor_taylor`, `taylor_eval`, and an `AlgEquiv` version, but there is no multivariate counterpart: Taylor's theorem in several variables, "vanishing to order `M` at a point" for multivariate polynomials, and index arguments (Roth, Thue–Siegel–Dyson, the polynomial method with multiplicities) all have to work with `aeval (fun j ↦ X j + C (α j)) P` by hand. The project's `MvPolynomial.taylor` fills exactly this gap, with the full API mirroring the univariate file: `taylor_X`, `taylor_C`, `taylor_monomial`, `coeff_taylor` (coefficient at `d` is `(Δ_d P)(α)`), `eval_taylor`, `taylor_taylor`, `taylor_zero`, `taylor_map`, `taylor_rename`, `degreeOf_taylor_le`, and over a ring `taylor_injective`, `taylor_eq_zero_iff`, plus `eq_sum_box_hasseDeriv`. With it, mathlib's `MvPowerSeries.weightedOrder`, `MvPolynomial.support`, `rename` and `map` lemmas apply to translated polynomials directly (as Roth/Index.lean shows).

The body is a one-liner (`aeval`), but it is justified under the API-name exemption on the same grounds mathlib keeps `Polynomial.taylor`: the name carries a substantive lemma API whose central result (`coeff_taylor`) is a genuine theorem, not a composition. The definition is already maximally general and LOW-risk. The only dependency is `MvPolynomial.hasseDeriv` (YES-but-generalise-first, coefficient spelled via `Finsupp.choose`), so this should ship in the same PR or immediately after it; the `AlgHom` bundling (rather than univariate's `LinearMap` + `taylorAlgHom`) should be noted in the PR since `CommSemiring R` is forced for `MvPolynomial`.

WHY add it: names the multivariate Taylor shift whose absence forces every user of multivariate Hasse derivatives to re-state `aeval (X + C ∘ α)`; enables a multivariate `taylor_coeff`, multiplicity at a point, and a characteristic-free multivariate Taylor theorem (`eq_sum_box_hasseDeriv`), and connects to univariate `Polynomial.taylor` via the compiled bridge `uniqueAlgEquiv_taylor`.
Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/Taylor.lean (importing the new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean)
Proposed PR title:            "feat(Algebra/MvPolynomial): multivariate Taylor shift"
PR grouping:                  ship after/with `MvPolynomial.hasseDeriv` (and `Finsupp.choose` from the hasseCoeff report); include taylor_apply, taylor_X, taylor_C, taylor_monomial, coeff_taylor, eval_taylor, taylor_taylor, taylor_zero, taylor_map, taylor_rename, degreeOf_taylor_le, taylor_neg_taylor, taylor_injective, taylor_eq_zero_iff, uniqueAlgEquiv_taylor, and optionally a `taylorEquiv` over `CommRing` mirroring `Polynomial.taylorEquiv`.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.taylor` — confirm no easy further weakening
  - [ ] `/cleanup Roth/Taylor.lean MvPolynomial.taylor` — full audit + diff gates
  - [ ] Pick a mathlib reviewer based on `Mathlib/Algebra/Polynomial/Taylor.lean` and `Mathlib/Algebra/MvPolynomial/` recent commits

---

## Next step

Upstream `MvPolynomial.taylor` with its Roth/Taylor.lean API as Mathlib/Algebra/MvPolynomial/Taylor.lean, in or right after the `MvPolynomial.hasseDeriv` PR, adding the bridge `uniqueAlgEquiv_taylor` (and optionally `taylorEquiv`); locally keep as is.

## Evidence
- `.mathlib-quality/overview/evidence/MvPolynomial.taylor/probes.lean` (compiles with `lake env lean`, no errors or warnings): (1) `taylor α = bind₁ (fun j ↦ X j + C (α j))` and `= aeval ...` by `rfl`; (2) proves the bridge `uniqueAlgEquiv_taylor : uniqueAlgEquiv R σ (taylor α P) = Polynomial.taylor (α default) (uniqueAlgEquiv R σ P)` for `[Unique σ]`; (3) universe probe at `σ = PUnit.{3}`.
- `[Semiring R]` failure for `MvPolynomial` reused from `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`.
- Mathlib greps: `def taylor` (univariate / calculus only), `X i + C` / `X j + C` in MvPolynomial files, taylor/subst/translat defs in Algebra/MvPolynomial and RingTheory/MvPowerSeries; read Mathlib/Algebra/Polynomial/Taylor.lean (`taylor` is a `LinearMap` over `Semiring`, `taylorAlgHom` over `CommSemiring`).
- LeanSearch, Lean-Finder, Loogle (one query each): univariate or general substitution only.
- WebSearch: 3 queries (table rows 1-3). ChatGPT MCP: n/a (not configured).
- Project greps `grep -rnw taylor Roth/` for Used-by and call sites; reference grep of `.mathlib-quality/references/clean.tex`.
