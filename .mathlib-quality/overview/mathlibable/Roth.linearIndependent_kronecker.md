---
decl: Roth.linearIndependent_kronecker
file: Roth/GenWronskian.lean
line: 117
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Once the injectivity lemma for weightedSubst on restrictSupport ships (sibling kronecker_eq_zero_iff), this is one call to mathlib's LinearIndependent.map_injOn plus Submodule.span_le (verified over any CommSemiring and index type, without hk); no separate mathlib lemma is warranted.
action: Do not upstream; ship injOn_weightedSubst_restrictSupport with the weightedSubst PR, then reprove l.117 as h.map_injOn (kronecker k).toLinearMap (injOn.mono (span_le.2 ...)) (drop hk, update the caller at Roth/GenWronskian.lean:263) or inline it there.
---

# Roth.linearIndependent_kronecker

## Inventory entry

### `theorem Roth.linearIndependent_kronecker`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] {l : ℕ} {k : ℕ} (hk : 1 < k) {φ : Fin l → MvPolynomial σ K} (hφ : ∀ ν j, degreeOf j (φ ν) < k) (h : LinearIndependent K φ) : LinearIndependent K fun ν ↦ kronecker k (φ ν)`
- **What**: The Kronecker substitution `x_j ↦ t^{k^{e j}}` sends a linearly independent family of multivariate polynomials, all of whose partial degrees are `< k`, to a linearly independent family of univariate polynomials.
- **How**: Unfolds both sides with `Fintype.linearIndependent_iff`; given `∑ g ν • kronecker (φ ν) = 0`, it applies `Roth.kronecker_eq_zero_iff` to `∑ g ν • φ ν`, bounding its partial degrees by `MvPolynomial.degreeOf_sum_le`, `Finset.sup_lt_iff` and `MvPolynomial.degreeOf_C_mul_le`, and pushes `kronecker` through the sum with `map_sum`/`map_smul`.
- **Hypotheses**: `hk : 1 < k` (passed to `kronecker_eq_zero_iff`, whose `hk` is superfluous, and used as `0 < k` for `Finset.sup_lt_iff`; superfluous overall, verified); `hφ` (essential: supports in the digit box); `h` (essential); `[Field K]` (only semiring structure needed); `[Fintype σ]` (only for the weight `k ^ equivFin j`); `Fin l` index (any index type works).
- **Uses from project**: `Roth.kronecker`, `Roth.kronecker_eq_zero_iff`
- **Used by**: `Roth.exists_genWronskian_ne_zero` (Lemma 1) at Roth/GenWronskian.lean:263. No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 113-127, proof length 8 lines (120-127)
- **Notes**: The proof re-derives by hand (via `Fintype.linearIndependent_iff`) what mathlib's `LinearIndependent.map_injOn` gives in one call from an injectivity-on-span statement.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/GenWronskian.lean:263, Lemma 1), on the critical path.
- Wrapper of 1-2 mathlib calls? Not as currently written (8-line coefficient argument), but in substance yes: it is `LinearIndependent.map_injOn` applied to the injectivity of the Kronecker substitution on the degree box (verified in the evidence file).
- Does mathlib have it? Not the Kronecker statement; it has the general transport lemmas `LinearIndependent.map_injOn`, `LinearMap.linearIndependent_iff_of_injOn`, `LinearIndependent.map`.
- Too specific? It is the exact step the source names ("We claim that these polynomials are linearly independent"), so keeping it as a named project lemma is reasonable; it could also be inlined at its single call site.
- Well-chosen? The statement is fine; `hk`, `Field`, `Fin l` are needlessly narrow.
- Conclusion: `KEEP`. Action: reprove as a `map_injOn` one-liner once the sibling InjOn lemma exists, dropping `hk`.

## Mathlibable assessment (Step 9)

Pre-filter: not private, not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `linearIndependent_kronecker` / `weightedSubst` finds nothing. Not a glue lemma (8-line proof). Parent `Roth.kronecker` is `YES-but-generalise-first` (re-aimed at `MvPolynomial.weightedSubst w := aeval (fun j ↦ X ^ w j)`); sibling `Roth.kronecker_eq_zero_iff` is `YES-but-generalise-first` (`weightedSubst_eq_zero_iff`, `injOn_weightedSubst_restrictSupport`). Full run, aimed at the `weightedSubst` form.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing Roth.GenWronskian compiles clean)
- decl `Roth.linearIndependent_kronecker`:  ✓ resolved at Roth/GenWronskian.lean:117
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians and Lemma 1 (a linearly independent family has a nonvanishing generalized Wronskian), proved via Kronecker substitution reducing to the univariate Wronskian criterion.

### Statement (Phase 1)

`Roth.linearIndependent_kronecker` is a theorem stating the following:

Let `φ_0, …, φ_{l-1} ∈ K[x_j : j ∈ σ]` be linearly independent over `K`, each of degree `< k` in every variable, and let `κ_k : K[x] → K[t]` be the Kronecker substitution `x_j ↦ t^{k^{e(j)}}` for an enumeration `e : σ ≃ Fin p`. Then `κ_k(φ_0), …, κ_k(φ_{l-1})` are linearly independent in `K[t]`. The reason: `κ_k` is a linear map injective on the space of polynomials with all partial degrees `< k`, which contains the span of the `φ_ν`.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]`: coefficients (semiring structure suffices).
- `σ` with `[Fintype σ]`: variables, enumerated by `Fintype.equivFin`.
- `l : ℕ`, family indexed by `Fin l`.
- `k : ℕ`: the base.

Hypotheses (Lean side):
- `hk : 1 < k`: base ≥ 2 (superfluous).
- `hφ : ∀ ν j, degreeOf j (φ ν) < k`: all supports in the box `[0,k)^σ`.
- `h : LinearIndependent K φ`.

Conclusion (math): the `κ_k(φ_ν)` are linearly independent.

Conclusion (Lean): `LinearIndependent K fun ν ↦ kronecker k (φ ν)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an intermediate step inside the proof of Lemma 1, transporting linear independence along an injective-on-a-subspace linear map.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 8 substantive lines
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel                          | Query | Hit? | Standard form found | Notes |
|----|----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)        | Kronecker substitution preserves linear independence of multivariate polynomials degree less than k | partial | Kronecker substitution is a one-to-one correspondence between polynomials of individual degree `< D` and univariate polynomials of degree `< D^n` | Roche arXiv:1807.08289, Arnold–Roche arXiv:1401.6694; linear independence not stated separately, it is the immediate consequence of injectivity |
|  2 | WebSearch (general form)         | linear map injective on span preserves linear independence | yes | a linear map injective on the span of an independent family (equivalently with kernel meeting the span trivially) maps it to an independent family | standard linear algebra (Sharipov arXiv:math/0405323 and course notes); mathlib's `LinearIndependent.map_injOn` |
|  3 | WebSearch (named-after / aliases)| Roth's theorem generalized Wronskian proof Kronecker substitution linearly independent polynomials one variable reduction | partial | Roth's Lemma 1 picks `k` exceeding all partial degrees; reduction to one variable | Roth 1955 (Mathematika), arXiv:2502.00731; the independence of the substituted polynomials is an inline step, not a named result |
|  4 | ChatGPT MCP                      | (standard form / generality of "Kronecker substitution preserves linear independence") | n/a | — | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references                 | `.mathlib-quality/references/clean.tex` l.255-271 | yes | proof of Lemma 1 compares coefficients of `t^{s_1 + k s_2 + …}`; Lean note: "Uniqueness of base-`k` expansions gives the restricted coefficient comparison, which then transports the required linear independence" | the source itself frames this as transport of independence along the restricted injectivity |
|  6 | nLab                             | linear independence / injective linear map | no | — | nLab has general linear-algebra pages only; nothing about this substitution |
|  7 | nCatLab (if categorical)         | n/a | n/a | — | not a categorical concept (concrete linear-algebra transport) |
|  8 | Stacks Project (if alg geom)     | n/a | n/a | — | not an algebraic-geometry concept |
|  9 | MathOverflow / Math.StackExchange| injective linear map preserves linear independence (covered by #2) | yes | same as #2 | textbook exercise; no specialised Kronecker version |
| 10 | recent arXiv (last 5 years)      | Kronecker substitution sparse interpolation / PIT (arXiv:2403.12716, 2411.17330) | partial | injectivity of weighted substitutions on supports | independence-transport is never isolated as a separate statement |

### Literature summary (Phase 3)

Concept identified as: transport of linear independence along a linear map injective on the span (here: the Kronecker / weighted monomial substitution restricted to polynomials with support in a set where the weight is injective).
Sources agree on the standard form: yes. The literature states the injectivity of Kronecker substitution on the individual-degree box and treats linear independence as its immediate consequence.
Most general standard form: if `f` is linear and injective on `span (range v)`, then `v` independent implies `f ∘ v` independent; for the substitution `x_j ↦ t^{w_j}`, injectivity holds on `restrictSupport R S` whenever `w·` is injective on `S`.
Generality dimensions where the literature varies:
  - weights: base-`k` digits (classical) versus any weight injective on the support set.
  - coefficients: fields in the source; any commutative semiring works.
  - index set: finite families in the source; any index type works.
Disagreement with the literature: none in content; the Lean form is narrower (`1 < k`, `Field`, `Fin l`, box, `equivFin`) and re-proves the transport by hand.

### Generality analysis — `Roth.linearIndependent_kronecker`

Literature-standard form (from Phase 3): `LinearIndependent R φ → (∀ i, ↑(φ i).support ⊆ S) → Set.InjOn (Finsupp.weight w) S → LinearIndependent R (weightedSubst w ∘ φ)`, which is `LinearIndependent.map_injOn` composed with the InjOn lemma.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hk : 1 < k` | base ≥ 2 | none | yes | `Evidence.linearIndependent_kronecker'` compiles without it |
| 2 | `[Field K]` | field | commutative semiring | yes | `Evidence.linearIndependent_weightedSubst` compiles over `[CommSemiring R]` (InjOn proved by coefficient comparison, no subtraction) |
| 3 | `Fin l` index | finite family | any index type `ι` | yes | both evidence lemmas are stated for arbitrary `ι` |
| 4 | `[Fintype σ]` + base-`k` weight | `k ^ equivFin j` | arbitrary `w : σ → ℕ` injective on `S` | yes | only used to build the weight |
| 5 | `hφ` (box) | partial degrees `< k` | supports in `S` with `InjOn (weight w) S` | yes | box is one instance of `S` (`weight_injOn_box`, via `Behrend.map_injOn`) |
| 6 | `h` | independence | independence | no | essential |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 5 (all verified in `evidence/Roth.linearIndependent_kronecker/generalise.lean`, `lake env lean` clean: no errors, no warnings)
Proposed restatement (as a corollary, not a new mathlib lemma):

```lean
theorem linearIndependent_weightedSubst {R σ ι : Type*} [CommSemiring R] {w : σ → ℕ}
    {S : Set (σ →₀ ℕ)} (hw : Set.InjOn (Finsupp.weight w) S) {φ : ι → MvPolynomial σ R}
    (hφ : ∀ i, ↑(φ i).support ⊆ S) (h : LinearIndependent R φ) :
    LinearIndependent R (weightedSubst w ∘ φ)
```

Cost of restatement: CHEAP (the proof is the one-call composition below; the project lemma becomes a term-mode specialisation).

The generality finding does not push toward a YES bucket: the general form is a one-call composition of an existing mathlib lemma with the sibling's InjOn lemma (Phase 6), so it is not a separate mathlib contribution.

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|---|---|---|---|
|  1 | preambles → typeclasses? | no | no bundled structure hypotheses | — |
|  2 | sequences → filters? | no | no topology | — |
|  3 | construction → universal property? | no | statement about a fixed map | — |
|  4 | set-with-predicate → bundled substructure? | yes | the box becomes membership of the span in `restrictSupport R S`; independence is transported by `LinearIndependent.map_injOn` | reuses the general transport API instead of a hand proof |
|  5 | field-specific → (semi)ring? | yes | `[CommSemiring R]` | — (follows from the sibling) |
|  6 | 1-categorical → higher? | no | not categorical | — |
|  7 | concrete index → general? | yes | arbitrary index type `ι` and arbitrary weight `w` | — |
|  8 | concrete-via-abstract? | yes | the proof uses `kronecker` only through `kronecker_eq_zero_iff`, i.e. only that the map is linear and injective on a subspace containing the `φ ν`; abstract form is `LinearIndependent.map_injOn` | already in mathlib, so the abstraction removes the need for the lemma |
|  9 | false-generalisation guard | no false generalisation | `weightedSubst (k ^ equivFin ·)` is `rfl`-equal to `Roth.kronecker`; evidence item 2 recovers the project statement (minus `hk`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: none as a new lemma; the idiomatic form is `h.map_injOn (weightedSubst w).toLinearMap (injOn.mono (Submodule.span_le.2 …))`.
  - Cost: CHEAP
  - Mathlib downstream this enables: `LinearIndependent.map_injOn` / `LinearMap.linearIndependent_iff_of_injOn` / `LinearIndepOn.map_injOn` apply directly once `injOn_weightedSubst_restrictSupport` exists.
  - Real mathematical improvement: the independence statement reduces to "injective on a subspace containing the family", so it needs no lemma of its own.

### Proof strategy — `Roth.linearIndependent_kronecker`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals/submodules | yes | argue with `span (range φ) ≤ restrictSupport R S` and InjOn on the submodule, instead of unfolding to coefficient vectors with `Fintype.linearIndependent_iff` and bounding `degreeOf` of a linear combination | CHEAP (verified) |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `MvPolynomial.weightedSubst`, `coeff_weightedSubst_weight`, `injOn_weightedSubst_restrictSupport` (sibling PR) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: `LinearIndependent.map_injOn` with InjOn on `restrictSupport` restricted to the span via `Submodule.span_le`.
  - Cost: CHEAP
  - Missing mathlib API (if any): `injOn_weightedSubst_restrictSupport` (sibling `Roth.kronecker_eq_zero_iff` assessment)
  - Would refactoring make the proof strictly shorter / cleaner? yes (8 lines with `degreeOf_sum_le`/`sup_lt_iff` bookkeeping become a 3-line term).

### Phase 4.5
n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.linearIndependent_kronecker`

[A] Lean-Finder       "a linear map injective on the span of a linearly independent family maps it to a linearly independent family"   hits: `LinearIndependent.map_injOn`, `LinearIndepOn.map_injOn`, `LinearIndepOn.id_imageₛ`, `LinearMap.linearIndependent_iff_of_injOn` (building blocks)
[B] Loogle            `LinearIndependent, MvPolynomial.aeval`   only `Algebra.SubmersivePresentation` Jacobian lemmas (unrelated)
[C] LeanSearch        "substituting powers of a single variable into linearly independent multivariate polynomials preserves linear independence"   no match (`MvPolynomial.linearIndependent_X`, `Polynomial.linearIndependent_powers_iff_aeval`, `linearIndependent_pow`: unrelated)
[D] Grep mathlib src  `linearIndependent_kronecker`, `weightedSubst`, `theorem LinearIndependent.map_injOn`, `linearIndependent_iff_of_injOn`   no Kronecker hits; building blocks at Mathlib/LinearAlgebra/LinearIndependent/Basic.lean:136 (`map_injOn`), :346 (`map`) and Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:330 (`linearIndependent_iff_of_injOn`)
[E] Name pattern      `lean_local_search linearIndependent_kronecker`: n/a (ripgrep not on PATH); substituted by the namespace-aware grep in [D]: no hits

Searched for both:
  - the user's current form (box, base `k`, `Fin l`, field)
  - the literature-standard form (transport along a map injective on the span; weighted substitution)

Concluded: found building blocks (`LinearIndependent.map_injOn`, `Submodule.span_le`, `MvPolynomial.mem_restrictSupport_iff`, plus the sibling-proposed `injOn_weightedSubst_restrictSupport`); composition yields our form.

### Normal-form check — `Roth.linearIndependent_kronecker`

Equivalent formalisms this statement could take: (a) `LinearIndependent R (f ∘ φ)` from `LinearIndependent R φ`; (b) `LinearIndependent R (f ∘ φ) ↔ LinearIndependent R φ` under the support hypothesis; (c) `LinearIndepOn` on a set.
Does mathlib already have a canonical form for this idea? yes: `LinearMap.linearIndependent_iff_of_injOn` (iff form) and `LinearIndependent.map_injOn` (implication form) for any linear map injective on the span.
Our statement is a specialisation of the canonical form to one map; no separate lemma needed.
RHS convention respected? n/a (implication, not an iff)

### Syntactic generality — `Roth.linearIndependent_kronecker`

Alternative restatements attempted (list):
- current: `Fin l`, degree bounds, `kronecker`
- `linearIndependent_weightedSubst` (any `ι`, `CommSemiring`, support ⊆ `S`)
- iff form via `linearIndependent_iff_of_injOn`
Chosen restatement: the implication form, as a local corollary only.
Justification: the one call site has `h : LinearIndependent K φ` and degree bounds in hand and needs only the forward direction.

### Superfluous-argument audit — `Roth.linearIndependent_kronecker`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hk : 1 < k` | no | verified: `Evidence.linearIndependent_kronecker'` compiles without it |
| 2 | `[Field K]` | no | CommSemiring suffices (verified) |
| 3 | `Fin l` | no | any index type (verified) |
| 4 | `[Fintype σ]` | only for the weight | absent from the general form |
| 5 | `hφ`, `h` | yes | essential |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (derive from `LinearIndependent.map_injOn`)
Syntactic generality: RESTATE (any `ι`, no `hk`)
Superfluous arguments: 2 to drop locally (`hk`, `Fin l` → `ι`); `Field` irrelevant locally

Overall: RESTATE-BEFORE-SHIP (locally; not shipped to mathlib)

### Call sites — `Roth.linearIndependent_kronecker`

Internal use count: 0 outside the declaring file (1 inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:263 (`exists_genWronskian_ne_zero`, same file) | `(linearIndependent_kronecker (Nat.lt_add_right _ (by decide)) (fun ν j ↦ …) h)` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.linearIndependent_kronecker`?):
  - (none)

### Composition check (Phase 6)

Can `Roth.linearIndependent_kronecker` be derived from mathlib in ≤3 chained calls?

Attempt 1: `h.map_injOn (weightedSubst w).toLinearMap ((injOn_weightedSubst_restrictSupport hw).mono (Submodule.span_le.2 (Set.range_subset_iff.2 fun i ↦ (mem_restrictSupport_iff R).2 (hφ i))))`
  - Mathlib decls used: `LinearIndependent.map_injOn` (equivalently `LinearMap.linearIndependent_iff_of_injOn`), `Set.InjOn.mono`, `Submodule.span_le`, `Set.range_subset_iff`, `MvPolynomial.mem_restrictSupport_iff`; plus `injOn_weightedSubst_restrictSupport` from the sibling PR.
  - Result: succeeds (compiled as `Evidence.linearIndependent_weightedSubst`, using the `iff_of_injOn.2` spelling, which is the body of `map_injOn`).
  - Notes: the only non-mathlib ingredient is the InjOn lemma, already recommended for upstreaming under `Roth.kronecker_eq_zero_iff`; with current mathlib alone the project's 8-line coefficient proof (or the evidence InjOn proof) is needed.

Conclusion: COMPOSABLE (relative to the sibling InjOn lemma that is being upstreamed)

## Verdict: `Roth.linearIndependent_kronecker`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the literature states injectivity of Kronecker substitution on the individual-degree box (arXiv:1807.08289, 1401.6694; clean.tex l.255-271) and treats linear independence as its immediate linear-algebra consequence; no source isolates it as a result.
- Generality analysis (Phase 4): STRICTLY NARROWER (`hk`, `Field`, `Fin l`, box all removable, verified), but the general form is a corollary, not a new statement.
- Mathlib search (Phase 5): building blocks `LinearIndependent.map_injOn`, `LinearMap.linearIndependent_iff_of_injOn`, `Submodule.span_le`, `MvPolynomial.mem_restrictSupport_iff`; no Kronecker/weighted-substitution lemma.
- Composition check (Phase 6): COMPOSABLE in one `map_injOn` call plus a span-inclusion argument, given the sibling InjOn lemma.

**Rationale:**

The content here is all in the injectivity of the substitution on the degree box, which the sibling assessment (`Roth.kronecker_eq_zero_iff`, YES-but-generalise-first) already routes to mathlib as `MvPolynomial.weightedSubst_eq_zero_iff` and `injOn_weightedSubst_restrictSupport`. Given that InjOn lemma, linear independence follows from mathlib's `LinearIndependent.map_injOn` (Mathlib/LinearAlgebra/LinearIndependent/Basic.lean:136): the span of the family sits inside `restrictSupport R S` by `Submodule.span_le`, and the map is injective there. The evidence file proves this over any commutative semiring, for any index type and any weight injective on `S`, and gets the project statement without `hk` as a one-line specialisation. A separate mathlib lemma `linearIndependent_weightedSubst` would only package `map_injOn` with one hypothesis, which mathlib does not do for individual maps (compare `Polynomial.expand_injective`, which has no independence corollary).

WHY not (refactor-actionable): mathlib has the transport lemma `LinearIndependent.map_injOn`; the Kronecker-specific input is the InjOn lemma being upstreamed with the `weightedSubst` package. Once that exists, this lemma is the composition below.

Belongs-elsewhere check: keep it as a project-local lemma in Roth/GenWronskian.lean (it is the named step "We claim that these polynomials are linearly independent" in the source), reproved by the composition; or inline it at its single call site.

Mathlib building blocks:
- `LinearIndependent.map_injOn` (Mathlib/LinearAlgebra/LinearIndependent/Basic.lean:136)
- `LinearMap.linearIndependent_iff_of_injOn` (Mathlib/LinearAlgebra/LinearIndependent/Defs.lean:330)
- `Submodule.span_le`, `Set.range_subset_iff`, `Set.InjOn.mono`
- `MvPolynomial.mem_restrictSupport_iff` (Mathlib/RingTheory/MvPolynomial/Basic.lean)
- to be upstreamed: `MvPolynomial.injOn_weightedSubst_restrictSupport` (sibling `Roth.kronecker_eq_zero_iff`)

Composition sketch (≤3 lines):
```lean
example : LinearIndependent R (weightedSubst w ∘ φ) :=
  h.map_injOn (weightedSubst w).toLinearMap <| (injOn_weightedSubst_restrictSupport hw).mono <|
    Submodule.span_le.2 <| Set.range_subset_iff.2 fun i ↦ (mem_restrictSupport_iff R).2 (hφ i)
```

Call sites in our project (from Phase 6.0): 1 (Roth/GenWronskian.lean:263).

Refactor plan: after the `weightedSubst` lemmas land (or are added locally), replace the body of `linearIndependent_kronecker` (l.117) by the composition above with `w := fun j ↦ k ^ equivFin σ j` and `S := {d | ∀ j, d j < k}` (InjOn from `kroneckerExp_injOn` / `Behrend.map_injOn`), drop `hk` and generalise `Fin l` to any `ι`, and change the call at l.263 from `linearIndependent_kronecker (Nat.lt_add_right _ (by decide)) (fun ν j ↦ …) h` to `linearIndependent_kronecker (fun ν j ↦ …) h`. Alternatively inline the composition at l.263 and delete the lemma.

Next action: do not upstream; reprove locally via `LinearIndependent.map_injOn` once `injOn_weightedSubst_restrictSupport` exists, dropping `hk` and updating the caller at l.263.

## Next step

Do not upstream `Roth.linearIndependent_kronecker`. Ship `MvPolynomial.injOn_weightedSubst_restrictSupport` with the `weightedSubst` PR (sibling verdict), then reprove l.117 as `h.map_injOn (kronecker k).toLinearMap (…InjOn.mono (Submodule.span_le.2 …))` without `hk`, and update the call at Roth/GenWronskian.lean:263.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.linearIndependent_kronecker/generalise.lean` (imports `Roth.GenWronskian`, `Mathlib.Combinatorics.Additive.AP.Three.Behrend`, `Mathlib.RingTheory.MvPolynomial.Basic`). `lake env lean`: clean (no errors, no warnings) after two fixes to the explicit-argument form of `mem_restrictSupport_iff`. Contents:
  1. `Evidence.injOn_weightedSubst_restrictSupport`: InjOn on `restrictSupport R S` over a `CommSemiring` (coefficient comparison, no subtraction; strengthens the CommRing version in the sibling evidence).
  2. `Evidence.linearIndependent_weightedSubst`: general form over `CommSemiring`, any `ι`, any weight injective on `S`; proof is one call to `LinearMap.linearIndependent_iff_of_injOn` + `Submodule.span_le`.
  3. `Evidence.linearIndependent_kronecker'`: the project statement without `hk`, for any index type, as a specialisation of 2 via `weight_injOn_box` (from `Behrend.map_injOn`).
  4. `example`: the project lemma `Roth.linearIndependent_kronecker` typechecks against the same statement (agreement check).
- Searches: WebSearch ×3 (literature table); Loogle `LinearIndependent, MvPolynomial.aeval`; LeanSearch (no match); Lean-Finder (found `LinearIndependent.map_injOn` and relatives); grep of mathlib for `linearIndependent_kronecker`, `weightedSubst` (no hits) and the transport lemmas; grep of `Roth/` for call sites; `clean.tex` l.255-271.
- Unavailable channels: ChatGPT channel n/a (`ask_chatgpt_math` MCP not configured in this session); `lean_local_search` n/a (ripgrep not on PATH), replaced by grep.
