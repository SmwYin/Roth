---
decl: Roth.weight
file: Roth/Box.lean
line: 71
kind: def
visibility: public
verdict: NO-mathlib-has-it
cost: MODERATE
junk: REPLACE
rationale: weight r d = sum_j d j / r j is exactly mathlib's Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d (an AddMonoidHom), verified for all r including r j = 0; weight_zero, weight_add, weight_single become map_zero, map_add, Finsupp.weight_single.
action: Redefine Roth.weight r := Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) (keeping the name) with a bridge lemma weight_eq_sum, reprove the Box.lean API via map_add/map_zero/Finsupp.weight_single, and repoint the unfolding sites Index.lean:133,245,249, Theta.lean:500,502, Main.lean:366 at the bridge; do not upstream.
---

# Roth.weight

## Inventory entry

### `def Roth.weight`
- **Type**: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) : ℝ`
- **What**: The real weight `∑ j, d j / r j` of a multi-index `d` with respect to the parameters `r`; the index of a polynomial (`Roth.index`) is the least weight of a nonvanishing Taylor coefficient.
- **How**: Direct definition `∑ j, (d j : ℝ) / r j` (sum over `Finset.univ`, casts to `ℝ`).
- **Hypotheses**: section variable `[Fintype σ]` (the `[DecidableEq σ]` section variable is not included in the elaborated def).
- **Uses from project**: `[]`
- **Used by**: Roth/Box.lean (API: `weight_nonneg` 75, `weight_zero` 80, `weight_add` 85, `weight_eq_zero_iff` 91, `weight_single` 96, `weight_le_card` 103, `weight_mul_left` 110, `weight_le_degree_div` 118, `weight_mapDomain` 127); Roth/Index.lean:59 (definition of `Roth.index`), 70, 71, 77, 80, 86, 111, 131, 133, 202, 203, 245, 249; Roth/MainLemma.lean:421, 456, 555, 570, 609; Roth/Theta.lean:380, 496, 500, 502; Roth/Main.lean:349, 364, 366; Roth/Lattice.lean:144, 148, 151, 160, 168, 170, 178, 203.
- **Visibility**: public
- **Lines**: 70–71, body 1 line
- **Notes**: Listed under "Main definitions" of the Box.lean module docstring. Roth/Index.lean:131 already proves a bridge to `Finsupp.weight` (with natural weights `∏ r / r j`, divided by `∏ r`), so the project is aware of the mathlib def.

## Junk check (Step 8)
- Used anywhere? Yes, heavily: 9 API lemmas in Box.lean and ~40 references across Index, MainLemma, Theta, Main, Lattice.
- Wrapper of 1–2 mathlib calls? Yes: it is `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)` (evidence, one `simp`).
- Does mathlib have it? Yes, as `Finsupp.weight` (Mathlib/Data/Finsupp/Weight.lean:82), in greater generality (any coefficient semiring, any module of weights), bundled as an `AddMonoidHom`.
- Too specific (inline)? No: the project-specific parametrisation by `r : σ → ℕ` with weights `1 / r j` is used in ~50 places and matches the paper; keep the name.
- Well-chosen? Partly: as an unbundled function it duplicates `Finsupp.weight` and forces ad hoc re-proofs of `map_zero`/`map_add`/`weight_single`.
- Conclusion: `REPLACE` — action: redefine `Roth.weight r := Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` (keeping the name and the `r : σ → ℕ` interface), add a bridge `weight_eq_sum : weight r d = ∑ j, (d j : ℝ) / r j`, reprove `weight_zero`/`weight_add`/`weight_single` from `map_zero`/`map_add`/`Finsupp.weight_single`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said REPLACE (not REMOVE); qualified name `Roth.weight` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (it is a def). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight`:        resolved at Roth/Box.lean:71
- kind:                      def
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight` is a definition of the following: for a finite variable set `σ`, parameters `r = (r_j) ∈ ℕ^σ` and a multi-index `d = (d_j) ∈ ℕ^σ`, the weight of `d` is the real number `w_r(d) = ∑_j d_j / r_j`. This is the weighted degree of the monomial `X^d` for the weight vector `(1/r_j)_j`, and the index of a polynomial `P` at `α` is `min { w_r(d) : (Δ_d P)(α) ≠ 0 }`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (sum over `univ`).
- `r : σ → ℕ` — the parameters `r_j` (Lean convention: `x / 0 = 0`, so a zero parameter contributes `0`).
- `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- none.

Conclusion (math): `w_r(d) = ∑_j d_j / r_j ∈ ℝ`.

Conclusion (Lean): n/a — definition (`noncomputable def weight (r : σ → ℕ) (d : σ →₀ ℕ) : ℝ := ∑ j, (d j : ℝ) / r j`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line bookkeeping def (weighted degree with weights `1/r_j`), not a new structure or main result; it underlies the project's `index`, but the concept itself is the standard weighted degree.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | weak     | sites unfold it to the explicit sum (`rw [weight, ...]` at Index.lean:133, Main.lean:366; `simp [weight]` at Index.lean:245, 249, Theta.lean:500; `rfl` at Theta.lean:502); these want the sum form, not a barrier, and a bridge lemma serves them |
| Avoid typeclass diamonds         | no       | no instances involved; `Finsupp.weight` needs only `Module ℕ ℝ`, which is canonical |
| Mark semantic intent / API name  | yes (project-local) | ~40 project statements are phrased with `weight r d` and the paper's parametrisation by `r`; the stable name is useful locally, but mathlib's name for the concept is `Finsupp.weight` |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; no exemption justifies a mathlib addition since mathlib has the concept as `Finsupp.weight`)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem index of polynomial weight sum i_j / r_j definition | yes | index = min of `∑ j_i / r_i` over exponents with nonzero Taylor coefficient | arXiv math/0307203 (quantitative Roth–Ridout), arXiv 2502.00731 (Evertse, subspace theorem), Natarajan–Thangadurai chapter |
| 2 | WebSearch (general form) | weighted degree of monomial sum w_i a_i weight vector multi-index definition | yes | weighted degree `⟨w, α⟩ = ∑ w_i α_i` of `x^α` for a weight vector `w` | arXiv 2202.05742 (matrix-weighted Gröbner bases), Magma docs, Asir docs; weights may be arbitrary (even non-positive) |
| 3 | WebSearch (named-after / aliases) | "index" of a polynomial at a point with respect to (r_1,...,r_m) Roth lemma Schmidt Diophantine approximation | yes | same index; arXiv math/9708214 phrases it as weighted multiplicity with weights `1/d_j` | Evertse's Roth-lemma papers |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `weight`, `i_j/r_j` | yes | l.549-553: index as min of `∑_j d_j / r_j`; suggests natural weights `w_j = D / r_j` with `MvPowerSeries.weightedOrder`; l.565, 586, 601 (`w(i) = ∑_j i_j / r_j`) | project paper §4 |
| 6 | nLab | weighted degree / graded polynomial ring | partial | grading of a polynomial ring by assigning degrees to variables | general grading notion; no Roth-specific entry |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | weighted polynomial ring (graded rings) | partial | weighted projective space / graded rings with weights on variables | weights are integers there; same linear functional on exponents |
| 9 | MathOverflow / Math.SE | (results of #2: weighted degree) | partial | weighted degree as a linear functional on the exponent lattice | folklore |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | yes | arXiv 2502.00731 (2025), 2202.05742 (2022) | same formula |

### Literature summary (Phase 3)

Concept identified as: weighted degree of a monomial / multi-index, `⟨w, d⟩ = ∑_j w_j d_j`, specialised in Roth's proof to the weight vector `w_j = 1/r_j`.
Sources agree on the standard form: yes.
Most general standard form: a linear (additive) functional on the exponent monoid `ℕ^(σ)` determined by a weight vector `w : σ → M` in any additive commutative monoid / module `M`.
Generality dimensions where the literature varies:
  - weight values: positive integers (graded rings) vs rationals/reals `1/r_j` (Roth) vs arbitrary (term orders).
  - exponents: `ℕ` multi-indices vs elements of a semiring.
Disagreement with the literature: none; the project's form is the special weight vector `(1/r_j)`.

### Generality analysis — `Roth.weight`

Literature-standard form (from Phase 3): `Finsupp.weight w : (σ →₀ R) →+ M`, `d ↦ ∑ d i • w i`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector | `1 / r j` with `r : σ → ℕ` | arbitrary `w : σ → M` | yes | realised by `Finsupp.weight`; the project only needs `w = fun j ↦ (r j : ℝ)⁻¹` |
| 2 | codomain `ℝ` | ℝ | any `AddCommMonoid M` with `Module R M` | yes | realised by `Finsupp.weight` |
| 3 | `[Fintype σ]` | required (sum over `univ`) | not needed (`Finsupp.sum` over support) | yes | `Finsupp.weight` needs no `Fintype`; `Finsupp.weight_eq_sum` recovers the `univ` form under `Fintype` |
| 4 | exponents `σ →₀ ℕ` | ℕ | any semiring `R` | yes | realised by `Finsupp.weight` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is already in mathlib (`Finsupp.weight`), so this is false-positive class 4 and routes to `NO-mathlib-has-it`, not generalise-first.
Number of weakening opportunities found: 4 (rows 1–4), all realised by the existing mathlib def; equality verified in `weight_eq_finsupp_weight.lean`.
Proposed restatement: `Roth.weight r := Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` (project-local).
Cost of restatement: MODERATE (the def change is one line, but ~6 call sites that unfold `weight` to the explicit sum need a bridge lemma, and the `[Fintype σ]`-based Box.lean lemmas need re-proofs).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic sum |
| 3 | construction vs universal property? | yes | bundle as an `AddMonoidHom` (`Finsupp.weight` is `linearCombination` restricted) | `map_add`, `map_zero`, `map_sum`, `map_nsmul` for free; replaces `weight_zero`, `weight_add` |
| 4 | bundled substructure? | yes | bundled hom `(σ →₀ ℕ) →+ ℝ` instead of a bare function | as #3 |
| 5 | field-specific to semiring? | no | weights `1/r_j` need division; general form already avoids it | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary weight vector `w : σ → M` | `MvPolynomial.IsWeightedHomogeneous`, `weightedTotalDegree`, `Finsupp.le_weight_of_ne_zero`, `Finsupp.weight_eq_zero_iff_eq_zero` all stated for `Finsupp.weight` |
| 8 | concrete-via-abstract? | no | the def has no proof body | — |
| 9 | false-generalisation guard | no false generalisation | evidence proves `Roth.weight r d = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d` for every `r` (including `r j = 0`, both sides use `x/0 = x * 0⁻¹ = 0`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` (already in mathlib; nothing to add).
  - Cost: MODERATE
  - Mathlib downstream this enables: `map_add`/`map_zero`/`map_sum`, `Finsupp.weight_single`, `Finsupp.weight_eq_sum`, `Finsupp.le_weight_of_ne_zero`, `MvPolynomial.IsWeightedHomogeneous` API.
  - Real mathematical improvement: the weight is an additive functional, and bundling it removes the ad hoc re-proofs of additivity.

### Proof strategy — `Roth.weight`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | define via `Finsupp.weight` (bundled `AddMonoidHom`) | MODERATE |
| 5 | missing mathlib helpers | no | `Finsupp.weight_eq_sum`, `Finsupp.weight_single` already give the explicit and single forms | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: define `weight r` as `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)`, derive the sum form from `Finsupp.weight_eq_sum`.
  - Cost: MODERATE
  - Missing mathlib API (if any): none.
  - Would refactoring make the proof strictly shorter / cleaner? yes (`weight_zero`, `weight_add` become `map_zero`, `map_add`; `weight_single` becomes `Finsupp.weight_single` + `nsmul_eq_mul`).

### Diamond / defeq risk — `Roth.weight`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; the `Finsupp.weight` form uses `Module ℕ ℝ` from `AddCommMonoid.toNatModule`, the canonical instance (evidence compiles with `simp`/`nsmul_eq_mul`) |
| 2 | Reducibility leak | none | plain semireducible `noncomputable def` |
| 3 | Non-canonical unfolding | low | unfolding gives a `univ` sum of quotients, so mathlib's `Finsupp.weight` lemmas do not fire; this is the cost of the duplicate implementation; Theta.lean:502 relies on `rfl` to the sum form and would need the bridge lemma after the refactor |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`, no constraint forced |
| 6 | Coercion ambiguity | low | the redefined version would be an `AddMonoidHom` applied via `DFunLike` coercion; call sites write `weight r d`, which still parses; `Set.image (weight r)` at Index.lean:59 works with the coercion. The name `weight` collides with mathlib's `Finsupp.weight`, harmless inside `namespace Roth` but a reason not to upstream under this name |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.weight`

[A] Lean-Finder       "weight of a multi-index d : σ →₀ ℕ with respect to weight vector w, sum of d i • w i"   hits: `Finsupp.weight`, `Finsupp.weight_apply`, `Finsupp.le_weight`, `Finsupp.weight_eq_zero_iff_eq_zero`, `MvPolynomial.isWeightedHomogeneous_monomial`
[B] Loogle            `Finsupp.weight`   hits: `Finsupp.weight`, `Finsupp.degree_eq_weight_one`, `Finsupp.finite_of_nat_weight_{eq,le,lt}`, `Finsupp.le_weight`
[C] LeanSearch        "weighted sum of a finitely supported multi-index with real weights sum over i of d i times w i"   hits: `Finsupp.weight_apply`, `Finsupp.weight_single`, `Finsupp.weight`, `MvPolynomial.isWeightedHomogeneous_monomial`
[D] Grep mathlib src  `def weight`, `weight_eq_sum`, `def weightedTotalDegree`, `def weightedOrder`, `namespace Roth`   hits: `Finsupp.weight` (Mathlib/Data/Finsupp/Weight.lean:82), `Finsupp.weight_eq_sum` (:100), `MvPolynomial.weightedTotalDegree` (Mathlib/RingTheory/MvPolynomial/WeightedHomogeneous.lean:96), `MvPowerSeries.weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean:140); no `Roth` namespace
[E] Name pattern      `Finsupp.weight`, `Finsupp.weight_eq_sum`, `Finsupp.weight_single` (all used in the compiled evidence)   hits

Searched for both the user's form (`∑ j, d j / r j`) and the literature-standard form (`∑ d i • w i`).

Concluded: found in mathlib as `Finsupp.weight`; more general form (we are the specialisation `w = fun j ↦ (r j : ℝ)⁻¹`).

### Normal-form check — `Roth.weight`

Equivalent formalisms: `∑ j, (d j : ℝ) / r j`; `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d`; `d.sum fun j n ↦ n / r j`; `(Finsupp.weight (fun j ↦ ∏ r / r j) d : ℝ) / ∏ r` (Index.lean:131, for positive `r`).
Does mathlib already have a canonical form for this idea? yes: `Finsupp.weight w`.
Is our statement stated against the canonical form? no — it is a parallel definition; REFACTOR: define via `Finsupp.weight` and keep the explicit sum as a bridge lemma.
RHS convention respected? n/a (definition); the bridge should be `weight r d = ∑ j, (d j : ℝ) / r j`.

### Syntactic generality — `Roth.weight`

Alternative restatements attempted:
- `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` as an `AddMonoidHom` (compiles; evidence)
- parameters `r : σ → ℝ` instead of `σ → ℕ` (paper remark l.556 allows real `r_j`; not needed by the project)
Chosen restatement: `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` keeping the `r : σ → ℕ` interface.
Justification: call sites are phrased with natural `r` (box bounds `d j ≤ r j`), and the bundled hom gives additivity for free.

### Superfluous-argument audit — `Roth.weight`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | only for the `univ` sum | `Finsupp.weight` does not need it; after the refactor it can be dropped from the def (still needed by `weight_le_card` etc.) |
| 2 | `r` | yes | — |
| 3 | `d` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (define via `Finsupp.weight`)
Syntactic generality: OK
Superfluous arguments: 1 to drop after refactor (`[Fintype σ]` on the def itself)

Overall: RESTATE-BEFORE-SHIP (locally; nothing ships to mathlib)

### Call sites — `Roth.weight`

Internal use count: ~40 references outside the declaring file (plus 9 API lemmas in Roth/Box.lean)
External-to-file callers: 5 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:59 | `sInf (weight r '' ((taylor α P).support : Set (σ →₀ ℕ)))` (definition of `index`) |
| Roth/Index.lean:70-86 | `index P α r ≤ weight r d`, `csInf_le (... .image (weight r)).bddBelow`, `c ≤ weight r d` |
| Roth/Index.lean:111-114 | `index P α r - weight r k ≤ ...`; `simpa [weight_add, hiw]` |
| Roth/Index.lean:131-133 | `weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i`; `rw [weight, Finsupp.weight_eq_sum, ...]` |
| Roth/Index.lean:202-203 | `weight (fun j ↦ l * r j) '' ... = (l : ℝ)⁻¹ • (weight r '' ...)` |
| Roth/Index.lean:245, 249 | `simpa [weight, hqdef] using ...` |
| Roth/MainLemma.lean:421, 456, 555 | `weight r d < c → eval α (hasseDeriv d P) = 0`, `weight r k < c ∧ ...`, `weight r d < γ → d ∈ J` |
| Roth/MainLemma.lean:570, 609 | `(box r).filter fun d ↦ weight r d ≤ ...`, `weight r d ≤ (m - ...) / 2` |
| Roth/Theta.lean:380, 391 | `weight (r ∘ some) d ≤ δ`; `rw [weight_add, weight_mapDomain ..., weight_single] at h1` |
| Roth/Theta.lean:496-502 | `simpa [weight] using hδ`; `calc weight (r ∘ some) d = ∑ j, (d j : ℝ) / r (some j) := rfl` |
| Roth/Main.lean:349, 364, 366 | `c ≤ weight r d`; `rw [← Real.rpow_sum_of_pos (hqR 0), weight, Finset.mul_sum]` |
| Roth/Lattice.lean:144-178, 203 | `(box r).filter (fun d ↦ weight r d ≤ ...)`; line 155 `rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]` |

Inline-derivation grep:
  - Roth/Index.lean:131 (`weight_eq_finsupp_weight`-style bridge with natural weights `∏ r / r j`): the project already connects to `Finsupp.weight`, confirming the mathlib def is the canonical target.
  - No other inline re-derivation of `∑ d j / r j` outside `Roth.weight`.

### Composition check (Phase 6)

Can `Roth.weight` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d` by `simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]`
  - Mathlib decls used: `Finsupp.weight`, `Finsupp.weight_eq_sum`, `div_eq_mul_inv`
  - Result: succeeds (evidence, theorem `weight_eq_finsupp_weight`)

Attempt 2: the project API from the hom: `weight_add` by `map_add`, `weight_zero` by `map_zero`, `weight_single` by `Finsupp.weight_single` + `nsmul_eq_mul` + `div_eq_mul_inv`
  - Result: succeeds (evidence examples)

Conclusion: COMPOSABLE (the def is a specialisation of an existing mathlib def; routed to NO-mathlib-has-it)

## Verdict: `Roth.weight`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): the weight `∑ d_j / r_j` is the weighted degree `⟨w, d⟩` for `w_j = 1/r_j` (paper l.549-553, 601; arXiv 2502.00731, math/0307203; weighted-degree literature).
- Generality analysis (Phase 4): STRICTLY NARROWER, with the general form already in mathlib (class 4).
- Mathlib search (Phase 5): found in mathlib as `Finsupp.weight`; more general form.
- Composition check (Phase 6): COMPOSABLE; equality proved in one `simp`.

**Rationale:**

Mathlib's `Finsupp.weight w : (σ →₀ R) →+ M`, `d ↦ ∑ d i • w i`, is exactly the weighted degree, and `Roth.weight r = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` holds for every `r : σ → ℕ` (including zero parameters, since Lean's `x / 0 = 0 = x * 0⁻¹`); the evidence file proves this and rederives `weight_add`, `weight_zero`, `weight_single` from `map_add`, `map_zero`, `Finsupp.weight_single`. The paper itself (clean.tex l.551-553) points to mathlib's weighted machinery, and Roth/Index.lean:131 already bridges to `Finsupp.weight` with natural weights.

WHY not: mathlib already has the concept in strictly greater generality, bundled as an additive hom. Belongs-elsewhere check: keep a project-local `Roth.weight` name (parametrised by `r` as in the paper) in Roth/Box.lean, but implement it via `Finsupp.weight`.

Existing mathlib decl:        `Finsupp.weight` (with `Finsupp.weight_eq_sum`, `Finsupp.weight_single`)
Located at:                   `Mathlib/Data/Finsupp/Weight.lean:82` (`weight_eq_sum` at :100, `weight_single` at :96)
Our form follows in ≤1 line:
```lean
example (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d := by
  simp [Roth.weight, Finsupp.weight_eq_sum, div_eq_mul_inv]
```
Call sites in our project (from Phase 6.0):  ~40 references in 5 files (Index, MainLemma, Theta, Main, Lattice) plus 9 API lemmas in Box.lean
Refactor plan: change the def to `noncomputable def weight (r : σ → ℕ) : (σ →₀ ℕ) →+ ℝ := Finsupp.weight fun j ↦ ((r j : ℝ))⁻¹`; add `theorem weight_eq_sum [Fintype σ] : weight r d = ∑ j, (d j : ℝ) / r j` (from `Finsupp.weight_eq_sum`, `nsmul_eq_mul`, `div_eq_mul_inv`); reprove `weight_zero`/`weight_add` as `map_zero`/`map_add` (or keep them as thin `simp` aliases so Index.lean:114, Theta.lean:391, Lattice.lean:155 are unchanged) and `weight_single` from `Finsupp.weight_single`; at the unfolding sites Index.lean:133, 245, 249, Theta.lean:500, 502 and Main.lean:366 replace `weight` in `rw`/`simp` lists by `weight_eq_sum`; all other call sites use `weight r d` as a term and are unaffected.
Next action: do not upstream; perform the local REPLACE refactor above (optional; MODERATE), keeping the name `Roth.weight`.

---

## Next step

No mathlib action. Optionally redefine `Roth.weight` via `Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)` with a `weight_eq_sum` bridge, repointing the six unfolding sites.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight/weight_eq_finsupp_weight.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics): (1) `Roth.weight r d = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) d` for all `r`; (2) `weight_add`, `weight_zero`, `weight_single` rederived from `map_add`, `map_zero`, `Finsupp.weight_single`; (3) `Finsupp.weight_eq_sum` for general `R`, `M`.
- Mathlib greps: `def weight`, `def weightedTotalDegree`, `def weightedOrder`, `namespace Roth` over `.lake/packages/mathlib/Mathlib`.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.549-556, 565, 586, 601).
- Project grep `grep -rnw weight Roth/` for the call-sites table.
