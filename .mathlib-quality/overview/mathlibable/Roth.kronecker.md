---
decl: Roth.kronecker
file: Roth/GenWronskian.lean
line: 53
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: MODERATE
junk: KEEP
rationale: Mathlib has no Kronecker-substitution def (only the term aeval (X ^ w ·) and a private reproof of the base-k injectivity inside RingTheory/NoetherNormalization); the named substitution plus its injectivity/coefficient API is a standard tool, but it should ship as a weighted substitution aeval (fun j ↦ X ^ w j) over [CommSemiring R] with no Fintype, with exponents via Finsupp.weight (all verified rfl/clean), not with the noncanonical Fintype.equivFin.
action: Upstream (placeholder) MvPolynomial.weightedSubst w := aeval (fun j ↦ Polynomial.X ^ w j) in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean) with monomial lemma via Finsupp.weight, base-k injectivity (deduplicating NoetherNormalization.sum_r_mul_ne), coeff and eq_zero_iff on the degree box; locally replace kroneckerExp by Finsupp.weight and restate kronecker_monomial/coeff_kronecker/kronecker_eq_zero_iff against it (call sites all in Roth/GenWronskian.lean:60-268).
---

# Roth.kronecker

## Inventory entry

### `def Roth.kronecker`
- **Type**: `{K : Type*} → [Field K] → {σ : Type*} → [Fintype σ] → (k : ℕ) → MvPolynomial σ K →ₐ[K] Polynomial K`
- **What**: The Kronecker substitution `x_j ↦ t^{k^{e j}}`, where `e = Fintype.equivFin σ` is the (noncanonical) chosen enumeration of the variables, bundled as a `K`-algebra map `K[x_j : j ∈ σ] → K[t]`.
- **How**: One-line definition `aeval fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)`, i.e. mathlib's `MvPolynomial.aeval` at a specific point.
- **Hypotheses**: `[Field K]`, `[Fintype σ]` (section variables; `Fintype` is needed only for `Fintype.equivFin`).
- **Uses from project**: `[]`
- **Used by**: Roth/GenWronskian.lean only: `kronecker_monomial` (l.60–62, unfolds it), `coeff_kronecker` (l.88–93), `kronecker_eq_zero_iff` (l.106–111), `linearIndependent_kronecker` (l.117–123), private `kronHasse` (l.146), private `derivative_kronHasse_aux` (l.159, unfolds it), private `hasseDeriv_kronecker_mem` (l.190–205), `exists_hasseDeriv_kronecker_eq_sum` (l.214–219), private `wronskian_kronecker_eq_sum_aux` (l.238–245), `exists_genWronskian_ne_zero` (l.260–268, via the lemmas). No uses in other files.
- **Visibility**: public
- **Lines**: 51–54, proof length 1 line (definition body)
- **Notes**: The exponent depends on `Fintype.equivFin σ`, which is a noncomputable, noncanonical choice; downstream statements only need "some injective `e : σ → ℕ` into `[0, card σ)`". The companion `kroneckerExp k d` is exactly `Finsupp.weight (fun j ↦ k ^ e j) d` (verified).

## Junk check (Step 8)
- Used anywhere? Yes: 10 declarations in Roth/GenWronskian.lean (4 public lemmas, 1 public existence lemma, private helpers), feeding Lemma 1 (`exists_genWronskian_ne_zero`).
- Wrapper of 1–2 mathlib calls? Yes syntactically: one `MvPolynomial.aeval` at the point `j ↦ X ^ k ^ e j`.
- Does mathlib have it? No named def. Grep of `.lake/packages/mathlib/Mathlib/` for `kronecker` finds only Kronecker products of matrices; the only Kronecker-substitution trick is inside `Mathlib/RingTheory/NoetherNormalization.lean` (`T1`, an `aeval` into `MvPolynomial`, and the private `sum_r_mul_ne`, the base-`up` uniqueness argument).
- Too specific (inline?)? No: it names the source's `h_ν(t) = φ_ν(t, t^k, …)` and is the subject of a small API (monomial, coefficient, vanishing, linear-independence transport).
- Well-chosen definition? Mostly. Bundling as `→ₐ[K]` is right. The `Fintype.equivFin` enumeration and the `Field` assumption are narrower than needed (see Phase 4).
- Conclusion: `KEEP`. Action: keep the name locally; optionally generalise it as the weighted substitution in Phase 4 and replace `kroneckerExp` by `Finsupp.weight`.

## Mathlibable assessment (Step 9)

Pre-filter: not private, no `_aux`, docstring not internal/auxiliary, Step 8 KEEP, and no `MvPolynomial.kronecker`/`Roth.kronecker`/Kronecker-substitution def in mathlib (namespace-aware grep). Not a glue lemma. Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; the evidence file importing `Roth.GenWronskian` is diagnostic-clean)
- decl `Roth.kronecker`:     ✓ resolved at Roth/GenWronskian.lean:53
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  Generalized Wronskians of multivariate polynomials and Lemma 1 (linearly independent family has a nonzero generalized Wronskian), proved via Kronecker substitution `x_j ↦ t^{k^j}`.

### Statement (Phase 1)

`Roth.kronecker` is a definition of the following. Fix an enumeration `e : σ ≃ {0, …, p-1}` of the variables and an integer `k`. The Kronecker substitution is the `K`-algebra homomorphism `K[x_j : j ∈ σ] → K[t]` determined by `x_j ↦ t^{k^{e(j)}}`; it sends a monomial `a x^d` to `a t^{∑_j d_j k^{e(j)}}`. When all partial degrees are `< k`, uniqueness of base-`k` expansions makes it injective on that subspace (proved downstream, not part of the def).

Variables / typeclasses involved (Lean side):
- `K : Type*`, `[Field K]`: coefficient ring.
- `σ : Type*`, `[Fintype σ]`: the finite set of variables (finiteness used only to get `Fintype.equivFin σ`).
- `k : ℕ`: the base.

Hypotheses (Lean side):
- none.

Conclusion (math): the algebra map `P ↦ P(t^{k^{e(j)}})_j`.

Conclusion (Lean): n/a — definition (value `MvPolynomial σ K →ₐ[K] Polynomial K`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a named classical technique (Kronecker substitution) used as a tool inside the proof of Roth's Lemma 1. It is not a new structure and not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | yes (weak) | Sealed def. It is unfolded only deliberately (`simp [kronecker, …]` in `kronecker_monomial` l.62 and `derivative_kronHasse_aux` l.159); elsewhere `map_sum`, `map_smul` act on the bundled `AlgHom` without exposing `aeval` |
| Avoid typeclass diamonds         | no       | no instances involved |
| Mark semantic intent / API name  | yes      | `kronecker_monomial`, `coeff_kronecker`, `kronecker_eq_zero_iff`, `linearIndependent_kronecker`, `exists_hasseDeriv_kronecker_eq_sum` are stated about it. "Kronecker substitution" is a classical named technique (Kronecker 1882; standard in computer algebra). Mathlib names the analogous one-line `aeval`/`bind₁` specialisation `MvPolynomial.expand` |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Kronecker substitution multivariate polynomial x_i -> t^{d^i} injective partial degree less than d | yes | `x_i ↦ x^{D^{i-1}}`; a bijection between n-variate polynomials with every partial degree `< D` and univariate polynomials of degree `< D^n`; inverse via base-`D` expansion of exponents | arXiv 1807.08289 (sparse polynomials survey), 1401.6694 (Arnold–Roche randomized Kronecker substitution), 2403.12716 (iterative KS), 2304.01191 (inverse Kronecker map) |
| 2 | WebSearch (general form / history) | Kronecker's substitution ... history Kronecker 1882 reduction multivariate univariate | yes | reduction of multivariate problems to univariate ones by substituting powers of one variable (Kronecker 1882, Crelle 92); Schönhage's integer variant `Z[x] → Z` | Wikipedia "Kronecker substitution"; Harvey arXiv 0712.4046; numdam RHM 2001 (factorisation history) |
| 3 | WebSearch (aliases / forums) | "Kronecker substitution" mathoverflow OR nlab OR stackexchange polynomial | yes (arXiv only) | same form; also used for combinatorial identities (arXiv 2404.00332) | no forum hits; general form with arbitrary weight vectors (randomized KS) appears in Arnold–Roche |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for kronecker / `t^{k` | yes | §2 proof of Lemma 1, l.231 `h_ν(t) = φ_ν(t, t^k, …, t^{k^{p-1}})`; l.266 Lean note: define as the algebra hom `x_j ↦ t^{k^{j-1}}`, prove injectivity only on exponents `< k` (since `x_2 - x_1^k ↦ 0`) | exact source of the def |
| 6 | nLab | Kronecker substitution (covered by query #3 site terms) | no | — | no nLab page; computational-algebra technique |
| 7 | nCatLab | — | n/a | — | not a categorical concept (nLab #6 found nothing) |
| 8 | Stacks Project | — | n/a | — | the same trick appears in the Noether normalisation proof (Stacks 00OW cited by mathlib's NoetherNormalization), but as a substitution `x_i ↦ x_i + x_0^{r^i}`, not as a named map to `K[t]` |
| 9 | MathOverflow / Math.SE | query #3 | no | no thread surfaced | — |
| 10 | recent arXiv (last 5 years) | results of #1, #3 | yes | 2403.12716 (2024), 2404.00332 (2024), 2304.01191 (2023) | same form, often with a general weight vector instead of `D^i` |

### Literature summary (Phase 3)

Concept identified as: Kronecker substitution (Kronecker 1882), also used inside Nagata's proof of Noether normalisation.
Sources agree on the standard form: yes. The map is `x_i ↦ t^{D^{i}}` (index shift varies); injectivity holds on polynomials with all partial degrees `< D`, by uniqueness of base-`D` expansions.
Most general standard form: the monomial (weighted) substitution `x_i ↦ t^{w_i}` for a weight vector `w`, over any commutative (semi)ring; Kronecker's choice `w_i = D^i` is the special weight that makes it injective on the box `{d : d_i < D}`. Randomized KS (Arnold–Roche) uses other weights.
Generality dimensions where the literature varies:
  - weights: `D^i` (classical) up to arbitrary `w : σ → ℕ`; the general weight is the natural def, with `D^i` needed only for the injectivity lemma.
  - coefficient ring: integers and fields in computer algebra; nothing beyond a commutative semiring is used.
  - variable indexing: `{1, …, n}` with an explicit order; the order is part of the data.
Disagreement with the literature: none in substance. The Lean def hides the order in `Fintype.equivFin σ` (a noncanonical choice) and fixes the weight to `k^{e j}`.

### Generality analysis — `Roth.kronecker`

Literature-standard form (from Phase 3): `aeval (fun j ↦ X ^ w j) : MvPolynomial σ R →ₐ[R] R[X]` for `w : σ → ℕ`, `R` a commutative semiring; Kronecker's case is `w j = k ^ e j` for an injective `e : σ → ℕ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative semiring | yes | `aeval` needs only `[CommSemiring R]`. Verified: `Evidence.weightedSubst` over `[CommSemiring R]` compiles and elaborates at `R = ℤ` |
| 2 | `[Fintype σ]` | finite variables | any `σ` | yes | needed only for `Fintype.equivFin`. Verified: `weightedSubst` needs no finiteness and runs at `σ = ℕ` |
| 3 | exponent `k ^ equivFin σ j` | fixed weight from a noncanonical enumeration | arbitrary weight `w : σ → ℕ` | yes | Verified: `Roth.kronecker k = weightedSubst (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))` holds by `rfl` |
| 4 | `kroneckerExp k d` (companion) | `∑ j, d j * k ^ e j` | `Finsupp.weight w d` | yes (mathlib has it) | Verified: `kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ e j) d` by `simp [Finsupp.weight_apply, Finsupp.sum_fintype]` |
| 5 | monomial lemma | `kronecker_monomial` (Field, Fintype) | `aeval (X ^ w ·) (monomial d a) = C a * X ^ Finsupp.weight w d` | yes | Verified: `Evidence.weightedSubst_monomial` over `[CommSemiring R]`, any `σ` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (Field to CommSemiring; drop Fintype; arbitrary weight), all verified clean via `lean_diagnostic_messages` on `.mathlib-quality/overview/evidence/Roth.kronecker/generalise.lean`.
Proposed restatement:

```lean
namespace MvPolynomial
variable {R σ : Type*} [CommSemiring R]
/-- The weighted substitution `X j ↦ t ^ w j`; for `w j = k ^ e j` this is Kronecker's
substitution. -/
noncomputable def weightedSubst (w : σ → ℕ) : MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ w j

theorem weightedSubst_monomial (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d
-- injectivity / coeff lemmas for w = (k ^ e ·), e injective with values < card, or σ = Fin n
end MvPolynomial
```

Cost of restatement: MODERATE. The def and monomial lemma are mechanical (verified). The downstream `kroneckerExp_injOn`, `coeff_kronecker` and `kronecker_eq_zero_iff` must be restated with `Finsupp.weight` and an injective index map `e` (or `σ = Fin n`) in place of `Fintype.equivFin`. Their proofs carry over, but this was not compiled here.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic, finite |
| 3 | construction vs universal property? | no | already an `aeval`, i.e. defined by its universal property | — |
| 4 | set-with-predicate to bundled substructure? | no (weak) | the injectivity domain `{P : ∀ j, degreeOf j P < k}` could be phrased via mathlib's `MvPolynomial.restrictDegree`-style submodules | `LinearMap.injOn`-style statements |
| 5 | field to (semi)ring? | yes | `[CommSemiring R]` | usable over `ℤ` (Roth's integer polynomials), `ℕ` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | the weight `k ^ equivFin σ j` becomes an arbitrary `w : σ → ℕ`; the exponent becomes `Finsupp.weight w` | ties into `Finsupp.weight`, `weightedDegree`, `IsWeightedHomogeneous` (a weighted-homogeneous `P` of weight `n` maps to `C · t^n`) |
| 8 | concrete-via-abstract? | yes | the monomial lemma's proof never uses the special weight; only the injectivity lemma uses base-`k` digits | general monomial lemma, with the Kronecker case as a specialisation |
| 9 | false-generalisation guard | no false generalisation | `weightedSubst (k ^ e ·)` is definitionally the same map (rfl) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `weightedSubst w := aeval (fun j ↦ X ^ w j)` with exponent `Finsupp.weight w`, Kronecker as `w = (k ^ e ·)`.
  - Cost: CHEAP for the def and monomial lemma; MODERATE for the injectivity lemmas.
  - Mathlib downstream this enables: `Finsupp.weight` API (`map_add`, `weight_single`, `le_weight`), the weighted-homogeneous API in `Mathlib/RingTheory/MvPolynomial/WeightedHomogeneous.lean`, and a public base-`k` injectivity lemma that `NoetherNormalization` could reuse instead of its private `sum_r_mul_ne`.
  - Real mathematical improvement: it removes the noncanonical `Fintype.equivFin` from the definition and separates the general substitution from the digit-uniqueness fact.

### Proof strategy — `Roth.kronecker`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ? | no | — | — |
| 2 | Algebra elementwise vs point-free? | no | def is a point-free `aeval` | — |
| 3 | Analysis sequences? | no | — | — |
| 4 | Construction vs universal property? | no | `aeval` is the universal property | — |
| 5 | Missing mathlib helpers? | yes | (a) the monomial-to-`Finsupp.weight` lemma for `aeval (X ^ w ·)`; (b) a public base-`k` injectivity of `d ↦ ∑ d j * k ^ e j` on `{d : ∀ j, d j < k}` (mathlib has `Nat.ofDigits_inj_of_len_eq` and the private `NoetherNormalization.sum_r_mul_ne`) | file follow-up PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the def itself). The companion `kroneckerExp` should be replaced by `Finsupp.weight`. The injectivity helper (b) is a missing public mathlib lemma.

### Diamond / defeq risk — `Roth.kronecker`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | no instances; it is an `AlgHom` value |
| 2 | Reducibility leak | none | plain (semireducible) `def`, not `@[reducible]`; the rfl to `weightedSubst` holds but does not leak into instance search |
| 3 | Non-canonical unfolding | low | the current def depends on `Fintype.equivFin σ`, so two `Fintype σ` instances give propositionally different maps. `exists_genWronskian_ne_zero` creates one with `Fintype.ofFinite`. The weighted restatement removes this (the weight is explicit data) |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `weightedSubst` elaborates at `σ = ℕ`, `R = ℤ` with `Type*` |
| 6 | Coercion ambiguity | none | uses the standard `AlgHom` `FunLike` coercion |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none HIGH. The low risk (row 3, noncanonical enumeration) disappears under the proposed weighted restatement.

### Mathlib search-status: `Roth.kronecker`

[A] Lean-Finder       "algebra hom from multivariate to univariate polynomials sending X_i to a power of X, injective on bounded partial degree"  no hits (returned `MvPolynomial.expand_injective`, `Polynomial.toMvPolynomial`, `killCompl`, `finSuccEquiv_eq`, all different maps)
[B] Loogle            `MvPolynomial.aeval, Polynomial.X, HPow.hPow, Polynomial.coeff`; `Finsupp.weight, Polynomial.X`; `Finsupp.weight`  no hits for the first two; the third lists the `Finsupp.weight` API (`weight_apply`, `weight_single`, `le_weight`, …), confirming the exponent map exists but no polynomial-substitution lemma uses it
[C] LeanSearch        "Kronecker substitution multivariate polynomial to univariate X_i maps to X^(k^i) injective on bounded degree"; "aeval fun i => X ^ w i of monomial equals C a * X ^ weight w d"  no hits (only `aeval_monomial`, `toMvPolynomial_injective`, `MvPolynomial.expand`, `bind₁`)
[D] Grep mathlib src  `kronecker` (case-insensitive, excluding matrix Kronecker products), `ofDigits` in RingTheory/Algebra  only hit is `Mathlib/RingTheory/NoetherNormalization.lean`: `T1` (`aeval fun i ↦ if i = 0 then X 0 else X i + c • X 0 ^ r i`, `r i = up ^ i`, into `MvPolynomial`) and the private `sum_r_mul_ne` (l.83–97), the same base-`up` digit uniqueness as `Roth.kroneckerExp_injOn`
[E] Name pattern      lean_local_search-style checks for `kronecker`, `kroneckerSubst`, `weightedSubst`, `MvPolynomial.expand`  no Kronecker-substitution decl; `MvPolynomial.expand p = bind₁ (X i ^ p)` is the closest named analogue (stays multivariate, uniform exponent)

Searched for both:
  - the user's current form (`x_j ↦ t^{k^{e j}}`)
  - the literature-standard form (weighted substitution `x_j ↦ t^{w j}` with exponent `Finsupp.weight w`)

Concluded: found building blocks (`MvPolynomial.aeval`, `MvPolynomial.aeval_monomial`, `Finsupp.weight`, `Nat.ofDigits_inj_of_len_eq`); the def is the single term `aeval (fun j ↦ X ^ w j)`; no named def and no public API (monomial, injectivity, coefficient) for it. The only mathlib use of the trick is private inside NoetherNormalization.

### Normal-form check — `Roth.kronecker`

Equivalent formalisms this statement could take: `aeval (fun j ↦ X ^ w j)`; `eval₂Hom C (fun j ↦ X ^ w j)`; `(Polynomial.aeval …) ∘ rename …` composites; `Finsupp.mapDomain`-based `AddMonoidAlgebra.mapDomain (Finsupp.weight w)` on the underlying monoid algebra.
Does mathlib already have a canonical form for this idea? Partly: `aeval` is canonical for substitution maps, and `Finsupp.weight` is canonical for the exponent.
If yes: our def is stated as `aeval` (canonical); the exponent companion should be `Finsupp.weight` rather than a custom `kroneckerExp`.
RHS convention respected? yes (`kronecker_monomial` rewrites to `C a * X ^ _`, the standard normal form)

### Syntactic generality — `Roth.kronecker`

Alternative restatements attempted (list):
- `aeval (fun j ↦ X ^ k ^ Fintype.equivFin σ j)` (current)
- `weightedSubst (w : σ → ℕ)` (verified)
- `kroneckerSubst (k : ℕ) (e : σ → ℕ) := weightedSubst (fun j ↦ k ^ e j)` (Kronecker case with an explicit index)
- `AddMonoidAlgebra.mapDomain`-based formulation (an `AddMonoidHom` on exponents); rejected because it is harder to use with `MvPolynomial` API

Chosen restatement: `weightedSubst w`, with the Kronecker lemmas stated for `w = (k ^ e ·)` and `e` injective with `e j < card σ` (or `σ = Fin n`, `e = Fin.val`).
Justification: callers supply an explicit weight, so no `Fintype` instance choice is involved, and `map_*` plus `Finsupp.weight` lemmas apply directly.

### Superfluous-argument audit — `Roth.kronecker`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommSemiring R]` suffices (verified) |
| 2 | `[Fintype σ]` | no for the substitution | only to choose `equivFin`; an explicit weight removes it (verified) |
| 3 | `k : ℕ` | yes | the base; generalises to a weight `w` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (exponent as `Finsupp.weight w d`, not a custom `kroneckerExp`)
Syntactic generality: RESTATE (`weightedSubst w` with an explicit weight)
Superfluous arguments: 2 to drop (`[Field K]` to `[CommSemiring R]`, `[Fintype σ]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.kronecker`

Internal use count: 0 outside the declaring file (all uses are in Roth/GenWronskian.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:61–62 | `kronecker k (monomial d a) = C a * X ^ kroneckerExp k d` by `simp [kronecker, kroneckerExp, aeval_monomial, …]` |
| Roth/GenWronskian.lean:89 | `(kronecker k P).coeff (kroneckerExp k d) = P.coeff d` |
| Roth/GenWronskian.lean:107 | `kronecker k P = 0 ↔ P = 0` |
| Roth/GenWronskian.lean:119 | `LinearIndependent K fun ν ↦ kronecker k (φ ν)` |
| Roth/GenWronskian.lean:146 | `fun P ↦ kronecker k (hasseDeriv d P)` (private `kronHasse`) |
| Roth/GenWronskian.lean:155–159 | `simp [kronHasse, kronecker, derivative_aeval, …]`, with the weight spelled out at l.155 |
| Roth/GenWronskian.lean:191–205 | `Polynomial.hasseDeriv μ (kronecker k P)` (private `hasseDeriv_kronecker_mem`) |
| Roth/GenWronskian.lean:216–219 | `Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P)` |
| Roth/GenWronskian.lean:240–245 | `wronskian (fun ν ↦ kronecker k (φ ν)) = ∑ … kronecker k (genWronskian f φ)` |
| Roth/GenWronskian.lean:260–268 | `exists_genWronskian_ne_zero` via `linearIndependent_kronecker`, `wronskian_kronecker_eq_sum_aux` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.kronecker`?):
  - Roth/GenWronskian.lean:155 spells out `Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)` (the substituted point) for the chain rule; it uses `derivative_aeval`, which is stated for an arbitrary `γ`.
  - mathlib `NoetherNormalization.sum_r_mul_ne` re-derives the injectivity argument privately (outside the project).

### Composition check (Phase 6)

Can `Roth.kronecker` be derived from mathlib in ≤3 chained calls?

Attempt 1: `MvPolynomial.aeval fun j ↦ Polynomial.X ^ k ^ (Fintype.equivFin σ j : ℕ)`
  - Mathlib decls used: `MvPolynomial.aeval`, `Fintype.equivFin`
  - Result: succeeds (it is the definition)
  - Notes: the def itself is composable. Its API is not: `kroneckerExp_injOn`, `coeff_kronecker` and `kronecker_eq_zero_iff` are 10–15-line proofs (base-`k` digits through `Nat.ofDigits_inj_of_len_eq`, a support-sum argument) with no mathlib counterpart.

Attempt 2: `kronecker_monomial` from `aeval_monomial` + `Finsupp.weight_apply`
  - Result: succeeds as a one-`simp` composition (evidence `weightedSubst_monomial`)

Conclusion: COMPOSABLE for the bare def, NOT-COMPOSABLE for the injectivity/coefficient API that justifies naming it. Since the def is wanted for its API, Phase 7 treats the package as NOT-COMPOSABLE (as with `MvPolynomial.expand`, a named one-line `bind₁` that has its own API).

## Verdict: `Roth.kronecker`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): Kronecker substitution is a standard named technique (Kronecker 1882; Arnold–Roche; the arXiv KS literature; Nagata's Noether normalisation). The general form is the weighted substitution `x_j ↦ t^{w_j}`, and injectivity on `{d_j < k}` holds for `w_j = k^{e j}`.
- Generality analysis (Phase 4): STRICTLY NARROWER (`Field`, `Fintype`, fixed weight), with 3 weakenings verified clean in the evidence file.
- Mathlib search (Phase 5): no def and no public API. Building blocks are `aeval`, `aeval_monomial`, `Finsupp.weight` and `Nat.ofDigits_inj_of_len_eq`; the injectivity argument appears only privately in `NoetherNormalization.sum_r_mul_ne`.
- Composition check (Phase 6): the def composes; the API does not.

**Rationale:**

The def is one `aeval` term, so on its own it would be `NO-composable` like `Roth.diag`. The difference is that "Kronecker substitution" is a classical named map, and it carries a non-trivial API: base-`k` injectivity, preservation of coefficients and of vanishing on the degree box, and transport of linear independence. Mathlib re-proves the core of this privately in `Mathlib/RingTheory/NoetherNormalization.lean` (`sum_r_mul_ne`). There is precedent for naming a one-line substitution together with its API (`MvPolynomial.expand`). The one-liner exemption that applies is "semantic intent / API name": five project lemmas and the Noether normalisation proof would consume it.

The project's form is not the right one to upstream. It hard-codes the weight `k ^ Fintype.equivFin σ j`, which makes the map depend on a noncanonical `Fintype` instance. It also assumes a field, which the substitution does not need, and it defines a custom `kroneckerExp` that is exactly `Finsupp.weight`. The verified restatement is `weightedSubst w := aeval (fun j ↦ X ^ w j)` over `[CommSemiring R]` with no finiteness assumption, whose monomial lemma lands on `Finsupp.weight w d`. The Kronecker-specific results should then be stated for `w = (k ^ e ·)` with `e` injective. A bare def with no API would not be accepted, so it must ship with that API.

Reason for the generalisation: LITERATURE-WEAKENING (general weight, commutative semiring) and MODERN-IDIOM (`Finsupp.weight` as the exponent map; no noncanonical enumeration).

Proposed restatement:
```lean
noncomputable def MvPolynomial.weightedSubst {R σ : Type*} [CommSemiring R] (w : σ → ℕ) :
    MvPolynomial σ R →ₐ[R] Polynomial R :=
  aeval fun j ↦ Polynomial.X ^ w j

theorem MvPolynomial.weightedSubst_monomial (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]   -- verified

theorem Finsupp.weight_pow_injOn {σ : Type*} {k : ℕ} (hk : 1 < k) {e : σ → ℕ}
    (he : Function.Injective e) :
    Set.InjOn (Finsupp.weight fun j ↦ k ^ e j) {d : σ →₀ ℕ | ∀ j, d j < k} := by
  sorry  -- port of Roth.kroneckerExp_injOn / NoetherNormalization.sum_r_mul_ne

theorem MvPolynomial.coeff_weightedSubst_pow ... -- port of Roth.coeff_kronecker
theorem MvPolynomial.weightedSubst_pow_eq_zero_iff ... -- port of Roth.kronecker_eq_zero_iff
```
Estimated cost of regeneralisation: MODERATE.

Mathlib downstream this enables:
- `NoetherNormalization` can replace its private `sum_r_mul_ne` (and the degree computation `degreeOf_zero_t`) with the public injectivity lemma.
- `Finsupp.weight` and weighted-homogeneous API: a weighted-homogeneous `P` of `w`-weight `n` maps to `C c * t^n` directly.
- Over `ℤ` (the setting of Roth's integer polynomials), without passing through `ℚ`.

Re-aim consequences for downstream lemmas (for the orchestrator):
- `Roth.kroneckerExp`: NO-mathlib-has-it. It equals `Finsupp.weight (fun j ↦ k ^ e j)` (verified); replace it (used at l.61, 69–74, 89, 97).
- `Roth.kronecker_monomial`: re-aim at `weightedSubst_monomial` (verified over CommSemiring, any σ); not in mathlib; ships with the def.
- `Roth.kroneckerExp_injOn`: re-aim as base-`k` injectivity of `Finsupp.weight (k ^ e ·)`; mathlib has only the private `NoetherNormalization.sum_r_mul_ne` (Fin (n+1), `ofDigits`); YES candidate that deduplicates mathlib.
- `Roth.coeff_kronecker`, `Roth.kronecker_eq_zero_iff`, `Roth.linearIndependent_kronecker`: re-aim against `weightedSubst (k ^ e ·)`; likely weakenable from `Field` (eq_zero_iff and coeff need only CommSemiring; linear independence needs the base ring), not compiled here.

Next action: run `/generalise Roth.kronecker` aiming at `MvPolynomial.weightedSubst` + `Finsupp.weight`; locally replace `kroneckerExp` by `Finsupp.weight` and restate the GenWronskian.lean lemmas (l.57–123, 155) against the explicit weight; then PR the def plus monomial, injectivity, coeff and eq_zero_iff lemmas to `Mathlib/Algebra/MvPolynomial/` (next to `Expand.lean`), proposing to reuse the injectivity lemma in `Mathlib/RingTheory/NoetherNormalization.lean`.

---

## Next step

Run `/generalise Roth.kronecker` with target `MvPolynomial.weightedSubst w := aeval (fun j ↦ X ^ w j)` over `[CommSemiring R]`, exponent `Finsupp.weight w`; ship it with its injectivity/coefficient API (not as a bare def) in `Mathlib/Algebra/MvPolynomial/`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.kronecker/generalise.lean` (imports `Roth.GenWronskian`); `lean_diagnostic_messages`: clean, no errors or warnings. It verifies: (1) `Roth.kronecker k = weightedSubst (fun j ↦ k ^ equivFin σ j)` by `rfl`; (2) `Roth.kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ equivFin σ j) d`; (3) `weightedSubst_monomial` over `[CommSemiring R]` with no `Fintype`; (4) elaboration at `R = ℤ`, `σ = ℕ`.
- Grep of mathlib: `kronecker` (only matrix Kronecker products); `ofDigits` gives `Mathlib/RingTheory/NoetherNormalization.lean:94–96` (private `sum_r_mul_ne`).
- Loogle (3 queries), LeanSearch (2), Lean-Finder (1): results as recorded in the Phase 5 block.
- WebSearch (3 queries): results as recorded in the Phase 3 table. ChatGPT MCP: n/a, not configured.
