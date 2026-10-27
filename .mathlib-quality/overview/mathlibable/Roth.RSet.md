---
decl: Roth.RSet
file: Roth/Theta.lean
line: 56
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: RSet is Yamada/Roth's paper notation R_m(B; r) (nonzero integer polynomials, degree at most r_j in x_j, coefficients at most B), a Roth-proof-specific set; its degree clause is exactly mathlib's MvPolynomial.degreesLE ℤ σ r.toMultiset (compiled) and the rest is R ≠ 0 plus a pointwise coefficient bound, so there is nothing general to upstream.
action: Do not upstream; keep Roth.RSet in Roth/Theta.lean as the paper's named set (about 20 call sites in Theta.lean and MainLemma.lean, e.g. index_le_Θ, Θ_le_of_forall_index_le, index_det_le, index_le_lem6, sub_mem_RSet); optionally note the degreesLE bridge in the docstring; no call-site changes.
---

# Roth.RSet

## Inventory entry

### `def Roth.RSet`
- **Type**: `{σ : Type*} (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ)`
- **What**: The set `ℛ_m(B; r)` of nonzero integer polynomials whose degree in each variable `X j` is at most `r j` and whose coefficients all have absolute value at most `B`.
- **How**: Set-builder `{R | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧ ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}`, using mathlib's `MvPolynomial.degreeOf` and `MvPolynomial.coeff`.
- **Hypotheses**: none. The section variables `[Fintype σ] [DecidableEq σ]` are not included (the evidence file elaborates `RSet` for a bare `σ`, and `sub_mem_RSet` uses it with no `Fintype`).
- **Uses from project**: `[]`
- **Used by**: Roth/Theta.lean: `indexSet` (63), `one_mem_RSet` (73, 75), `indexSet_nonempty` (81), `index_le_Θ` (99), `Θ_le_of_forall_index_le` (125), `indexSet_bddAbove` / `Θ_le_card` / `Θ_mono` / `Θ_equiv` (by destructuring membership), `index_separated_mul_le_aux` (416, 425), `index_det_le` (458), `index_le_lem6` (559); Roth/MainLemma.lean: `sub_mem_RSet` (388–390), `exists_mem_RSet_le_index_aux` (550–560), `exists_mem_RSet_le_index_of_rpow_bound_aux` (581–613), `exists_mem_RSet_le_index_of_log_bound_aux` (618–639), `exists_auxiliary_polynomial_of_log_bound_aux` (647–653), `exists_auxiliary_polynomial_with_index_gap_aux` (698).
- **Visibility**: public
- **Lines**: 56–57, proof length 0 lines (2-line def body)
- **Notes**: Source: clean.tex §5 l.646–655 (items (1)–(3)). The paper takes `B ≥ 1` and positive `r_j`; Lean imposes neither, and the lemmas add `1 ≤ B` where needed (`one_mem_RSet`, `indexSet_nonempty`).

## Junk check (Step 8)
- Used anywhere? Yes, about 20 references across Theta.lean and MainLemma.lean. It is the domain of `indexSet` / `Θ` and the target set of the auxiliary-polynomial construction (Lemma 9).
- Wrapper of 1–2 mathlib calls? It is a conjunction of three predicates. Its degree clause is mathlib's `degreesLE ℤ σ (Finsupp.toMultiset r)` for finitely supported `r` (evidence (2)). The coefficient clause has no mathlib name for `MvPolynomial`.
- Does mathlib have it? No. The closest mathlib notions are `MvPolynomial.degreesLE`, `restrictDegree` (a uniform bound only), `restrictSupport`, `Polynomial.supNorm` (univariate only), and `Height.mulHeight` / `Finsupp.mulHeight` (projective heights over fields with admissible absolute values). None is this set.
- Too specific (inline?)? Inlining the three-way conjunction at about 20 statement sites would hurt readability. The name is the paper's notation `ℛ_m(B; r)`, so keep it.
- Well-chosen definition? Yes for the project. Using `Set` membership with anonymous-constructor destructuring is light. A possible improvement is to phrase the degree clause through `degreesLE`, which buys nothing locally.

Conclusion: KEEP. No action needed. Optionally mention the `degreesLE` characterisation in the docstring.

## Mathlibable assessment (Step 9)

Pre-filter: the def is public, its name does not end in `_aux`, its docstring is not internal or auxiliary, and Step 8 said KEEP. No `namespace Roth` / `Roth.RSet` exists under `.lake/packages/mathlib/Mathlib/`. It is not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` compiles with no output)
- decl `Roth.RSet`:          resolved at Roth/Theta.lean:56
- kind:                      def
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5, 6, 7 bounding it.

### Statement (Phase 1)

`Roth.RSet` is a definition. For a variable set `σ`, a real `B` and degree bounds `r : σ → ℕ`, it is

  `ℛ(B; r) = { R ∈ ℤ[X_j : j ∈ σ] : R ≠ 0, deg_{X_j} R ≤ r_j for all j, |coeff_d R| ≤ B for all d }`,

the set of nonzero integer polynomials in the "box" of multidegree `≤ r` whose naive height (max absolute value of the coefficients) is at most `B`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`: the variables (no finiteness needed).
- `B : ℝ`: the coefficient bound (paper: `B ≥ 1`).
- `r : σ → ℕ`: per-variable degree bounds (paper: positive).

Hypotheses (Lean side):
- none.

Conclusion (math): a subset of `ℤ[X_σ]`.

Conclusion (Lean): n/a — definition (`def RSet (B : ℝ) (r : σ → ℕ) : Set (MvPolynomial σ ℤ) := {R | R ≠ 0 ∧ (∀ j, degreeOf j R ≤ r j) ∧ ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is listed as a main definition of Theta.lean, but it is a notational set combining existing notions (degree box, coefficient bound) for the proof of Roth's theorem. It is neither a new structure nor a named theorem.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | membership is destructured directly (`rintro _ ⟨R, ⟨hR0, hRd, -⟩, ...⟩` in `indexSet_bddAbove`, `Θ_le_card`) and built by anonymous constructor (`sub_mem_RSet`); nothing relies on sealing |
| Avoid typeclass diamonds         | no       | no instances |
| Mark semantic intent / API name  | yes      | it is the paper's `ℛ_m(B; r)`; it appears in the statements of `indexSet`, `index_le_Θ`, `Θ_le_of_forall_index_le`, `index_det_le`, `index_le_lem6` and the Lemma 9 existence lemmas in MainLemma.lean |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; the exemption does not argue for mathlib)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof set of polynomials integer coefficients bounded by B degree at most r_j in x_j index Theta_m(B; q; r) | yes | `ℛ_m(B; r_1,…,r_m)` = nonzero integer polynomials of degree `≤ r_j` in `x_j` with coefficients of absolute value `≤ B` | Yamada / Ridout-style quantitative Roth (arXiv math/0307203) uses exactly this notation together with `Θ_m`; also Evertse arXiv 2502.00731 (Roth's lemma with height conditions) |
| 2 | WebSearch (general form) | height of a multivariate polynomial maximum absolute value of coefficients multidegree bounded set of integer polynomials Siegel's lemma | partial | naive height `H(P) = max |coeff|` (CoCoA `CoeffHeight`; arXiv math/9911094); Siegel's lemma produces integer polynomials of bounded multidegree and height | the set itself is an ad hoc "box × height ball", not a named object |
| 3 | WebSearch (named-after / aliases) | Roth's lemma "polynomials of multidegree" "height at most" index Bombieri Gubler Diophantine approximation | partial | Roth's lemma is stated for polynomials of multidegree `≤ (d_1,…,d_m)` with height bounds (Evertse Luminy notes; Bombieri–Gubler Ch. 6) | phrased as hypotheses, not as a named set |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §5 l.643–666 | yes | `ℛ_m(B; r_1,…,r_m)` with items (1) integral, nonzero; (2) degree `≤ r_j` in `x_j`; (3) coefficients `≤ B`; `B ≥ 1`, `r_j ≥ 1` | matches the Lean def; Lean drops the side conditions `B ≥ 1`, `r_j ≥ 1` |
| 6 | nLab | polynomial height / multidegree | no | — | no entry for bounded-height polynomial sets |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry. Multidegree boxes appear only as graded pieces, with no height condition |
| 9 | MathOverflow / Math.SE | (results of #2) | partial | "polynomials of bounded degree and height" as counting sets (Northcott-type finiteness) | folklore, no canonical definition |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | yes | arXiv 2502.00731 (2025), 2111.12409 (2021) | same hypotheses-style usage |

### Literature summary (Phase 3)

Concept identified as: the set `ℛ_m(B; r)` of Roth / Ridout / Yamada, i.e. nonzero integer polynomials of multidegree at most `r` and naive height at most `B`.
Sources agree on the standard form: yes. It is notation inside the proof of Roth's theorem. Elsewhere the same data appear as hypotheses ("`P ∈ ℤ[x]` of multidegree `≤ d` and height `≤ H`").
Most general standard form: polynomials over a ring with an absolute value, with support in a box (a `degreesLE` submodule) and a height bound. Over number fields the height is the projective `H(P)` built from all places.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ (Roth) vs number-field integers (Ridout, Schmidt) vs fields with absolute values (height theory).
  - height: naive max-coefficient (here) vs ℓ¹ length vs projective/Weil height.
Disagreement with the literature: none on content. Lean omits the side conditions `B ≥ 1`, `r_j ≥ 1`, which only matters for nonemptiness. No source treats the set as a standalone object worth a theory.

### Generality analysis — `Roth.RSet`

Literature-standard form (from Phase 3): `{P ∈ R[X_σ] : P ≠ 0, supp P ⊆ box(r), height(P) ≤ B}`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring `ℤ` | `MvPolynomial σ ℤ` | any ring with an absolute value / seminormed ring | yes, but meaningless here | the project needs `ℤ`: integrality is the point (nonzero integer ⇒ `|·| ≥ 1` in Lemma 5 / Liouville arguments) |
| 2 | degree bound `∀ j, degreeOf j R ≤ r j` | per-variable `degreeOf` | `R ∈ degreesLE ℤ σ (toMultiset r)` | equivalent, not weaker | evidence (2): equal for finitely supported `r` |
| 3 | `[Fintype σ]`, `[DecidableEq σ]` | not taken | not needed | already absent | evidence (1) |
| 4 | `B : ℝ` without `1 ≤ B` | none | paper requires `B ≥ 1` | already weaker than the paper | — |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for what the project needs). No hypotheses to drop: the def has none and no unused instance arguments (evidence (1)). Generalising the coefficient ring would change the object (Q9).
Number of weakening opportunities found: 0
Proposed restatement: none. The equivalent `degreesLE` phrasing (evidence (3)) is a reformulation, not a weakening.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic condition |
| 3 | construction vs universal property? | no | — | a subset, not a construction |
| 4 | bundled substructure? | partial | `(degreesLE ℤ σ r.toMultiset : Set _) ∩ {R | ∀ d, |coeff d R| ≤ B} \ {0}` | `degreesLE_add`, `degreesLE_nsmul` (product bounds), as in `ChevalleyComplexity`'s `coeffsIn ⊓ degreesLE`; the height-ball part is not a submodule, so the whole set cannot be bundled |
| 5 | field-specific to semiring? | no | — | already over `ℤ`, and integrality is essential |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `r : σ → ℕ` with arbitrary `σ` is already general |
| 8 | concrete-via-abstract? | no | — | no proof body |
| 9 | false-generalisation guard | yes (for row 1) | replacing `ℤ` by a general seminormed ring loses the integrality that every use exploits (nonzero ⇒ coefficient of size ≥ 1); the `degreesLE` reformulation (row 4) is the same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only idiomatic rephrasing writes the degree clause as `degreesLE ℤ σ r.toMultiset` (evidence (3)). That needs `r : σ →₀ ℕ` (every call site uses `σ → ℕ` with finite `σ`) and makes no downstream proof shorter. The height clause has no mathlib counterpart for `MvPolynomial`.

### Proof strategy — `Roth.RSet`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | (`degreesLE` submodule for the degree clause) | CHEAP but no gain |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | a coefficient sup-norm / naive height for `MvPolynomial` (mathlib has `Polynomial.supNorm` only for one variable; Analysis/Polynomial/Norm.lean lists other ℓ^p norms as TODO). Compare the project's `Roth.normOne`, judged YES-but-generalise-first | follow-up, independent of RSet |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a definition with no proof; the set-builder is the natural shape)

### Diamond / defeq risk — `Roth.RSet`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; uses only `MvPolynomial σ ℤ` and `ℝ` abs |
| 2 | Reducibility leak | none | plain semireducible def; membership is unfolded by anonymous-constructor patterns, which is the intended use |
| 3 | Non-canonical unfolding | low | the coefficient condition casts through `ℝ` (`|((R.coeff d : ℤ) : ℝ)|`), not `|R.coeff d| ≤ ⌊B⌋`; consistent with `normOne` and the `Θ` lemmas; `simp [RSet]` unfolds as expected (`one_mem_RSet`) |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`; `Θ_equiv` transports across `σ ≃ τ` in different universes |
| 6 | Coercion ambiguity | none | no coercions defined; `RSet` is a poor generic name for mathlib but harmless inside `namespace Roth` |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.RSet`

[A] Lean-Finder       "set of multivariate polynomials with degree in each variable bounded and coefficients bounded in absolute value"   hits: `MvPolynomial.degreesLE`, `restrictDegree`, `restrictTotalDegree`, `MvPolynomial.R` (finite-field exponent bound); none with a coefficient bound
[B] Loogle            `Set (MvPolynomial _ ℤ)`   no hits
[C] LeanSearch        "multivariate polynomials whose degree in each variable is at most n (restrictDegree)"; "height of a multivariate polynomial: maximum absolute value of its coefficients"   hits: `restrictDegree`, `mem_restrictDegree`, `mem_restrictDegree_iff_sup`; `Finsupp.mulHeight`, `Height.mulHeight`, `Polynomial.mahlerMeasure_le_sum_norm_coeff` (no naive-height on `MvPolynomial`)
[D] Grep mathlib src  `def degreesLE` (Algebra/MvPolynomial/Degrees.lean:616), `def restrictSupport` / `def restrictDegree` (RingTheory/MvPolynomial/Basic.lean:93, 171), `supNorm` (Analysis/Polynomial/Norm.lean:53, univariate), `NumberTheory/Height/MvPolynomial.lean` (`mulHeightBound` for homogeneous families over fields), `coeffsIn ⊓ degreesLE` (ChevalleyComplexity.lean:672, 713), `namespace Roth` (none)
[E] Name pattern      `MvPolynomial.mem_degreesLE`, `MvPolynomial.degreeOf_def`, `Finsupp.count_toMultiset`, `Multiset.le_iff_count` (all used in compiled evidence)

Searched for both the user's form (nonzero, per-variable degree ≤ r, coefficients ≤ B over ℤ) and the literature-standard form (box support plus height bound over a valued ring).

Concluded: found building blocks (`MvPolynomial.degreesLE`, `MvPolynomial.coeff`, `Finsupp.toMultiset`). No mathlib set or predicate combines a degree box with a coefficient bound for `MvPolynomial`.

### Normal-form check — `Roth.RSet`

Equivalent formalisms: (a) `∀ j, degreeOf j R ≤ r j` (current); (b) `R.degrees ≤ toMultiset r`, i.e. `R ∈ degreesLE`; (c) `R.support ⊆ box r` (`restrictSupport`); (d) `∀ d ∈ R.support, d ≤ r`.
Does mathlib already have a canonical form for this idea? For the degree clause, `degreesLE` (multiset form) is the bundled canonical one. For the whole set, no.
Is our statement stated against the canonical form? The bridge (evidence (2)) puts `degreesLE` on the RHS. The def itself uses `degreeOf`, which is what every call site supplies (`degreeOf_sub_le`, `degreeOf_mul_le`).
RHS convention respected? yes (in the bridge).

### Syntactic generality — `Roth.RSet`

Alternative restatements attempted:
- `degreesLE` phrasing (evidence (3), needs `r : σ →₀ ℕ`)
- `R ≠ 0 ∧ R ∈ restrictSupport ℤ {d | d ≤ r} ∧ …`
Chosen restatement: current (a). Call sites take `r : σ → ℕ` and prove the per-variable bounds with `degreeOf_*` lemmas.
Justification: easiest to supply and consume at the 20 sites; no `Finsupp` conversion.

### Superfluous-argument audit — `Roth.RSet`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `B` | yes | coefficient bound |
| 2 | `r` | yes | degree bounds |
| 3 | `[Fintype σ]`, `[DecidableEq σ]` | not taken | evidence (1) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project def)

### Call sites — `Roth.RSet`

Internal use count: 14 lines in Roth/MainLemma.lean, plus 10 lines in the declaring file Theta.lean (excluding its docstring mentions)
External-to-file callers: 1 distinct file (MainLemma.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:388–390 | `theorem sub_mem_RSet ... (hne : W' ≠ W'') : W' - W'' ∈ RSet B r` |
| Roth/MainLemma.lean:550–560 | `exists_mem_RSet_le_index_aux ... ∃ P, P ∈ RSet B r ∧ ...`; `have hP := sub_mem_RSet hW' hW'' hne` |
| Roth/MainLemma.lean:581–585, 613 | `exists_mem_RSet_le_index_of_rpow_bound_aux ... P ∈ RSet B r ∧ ...` |
| Roth/MainLemma.lean:618–622, 639 | `exists_mem_RSet_le_index_of_log_bound_aux ... P ∈ RSet (mainCoeffBound δ q₁ r₁) r` |
| Roth/MainLemma.lean:647, 653 | `exists_auxiliary_polynomial_of_log_bound_aux ... P ∈ RSet ((q₁ : ℝ) ^ (δ * r₁)) r` |
| Roth/MainLemma.lean:698 | `exists_auxiliary_polynomial_with_index_gap_aux ... W ∈ RSet ((q 0 : ℝ) ^ (δ * r 0)) r` |
| Roth/Theta.lean:63 | `indexSet`: `∃ R ∈ RSet B r, ∃ h, ...` |
| Roth/Theta.lean:73–81 | `one_mem_RSet`, `indexSet_nonempty` |
| Roth/Theta.lean:99, 125 | `index_le_Θ (hR : R ∈ RSet B r)`, `Θ_le_of_forall_index_le (hc : ∀ R ∈ RSet B r, ...)` |
| Roth/Theta.lean:416, 425 | `index_separated_mul_le_aux (hU : U ∈ RSet M (fun j ↦ l * r (some j)))`, `hVmem : V' ∈ RSet M ...` |
| Roth/Theta.lean:458, 559 | `index_det_le (hR : R ∈ RSet B r)`, `index_le_lem6 (hR : R ∈ RSet B r)` |

Inline-derivation grep:
  - Roth/MainLemma.lean:275 `boxFamily r B := {W | (∀ j, degreeOf j W ≤ r j) ∧ ∀ d, 0 ≤ W.coeff d ∧ W.coeff d ≤ B}` repeats the degree clause with a one-sided coefficient box. This is a different set (the pigeonhole family) and is linked to `RSet` by `sub_mem_RSet`, so it is not a bypass.
  - No site restates the full `R ≠ 0 ∧ degree ∧ coeff` conjunction without `RSet`.

### Composition check (Phase 6)

Can `Roth.RSet` be derived from mathlib in ≤3 chained calls?

Attempt 1: `RSet B r = {R | R ≠ 0 ∧ R ∈ degreesLE ℤ σ (Finsupp.toMultiset r) ∧ ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B}` for `r : σ →₀ ℕ`
  - Mathlib decls used: `MvPolynomial.degreesLE`, `Finsupp.toMultiset`, `MvPolynomial.coeff`
  - Result: succeeds (evidence (3), proved by one `simp only` through the bridge (2))
  - Notes: the third conjunct is a raw pointwise bound because mathlib has no `MvPolynomial` coefficient sup-norm. The set is still a direct set-builder over mathlib primitives.

Conclusion: COMPOSABLE. The set is a set-builder conjunction of mathlib primitives (`≠ 0`, `degreeOf` / `degreesLE`, `coeff`), with no new mathematics.

### Verdict: `Roth.RSet`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): `ℛ_m(B; r)` is proof-internal notation of Roth / Ridout / Yamada (arXiv math/0307203; clean.tex §5). Elsewhere it appears only as hypotheses ("multidegree ≤ d, height ≤ H"). It is not a named object with a theory.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for the project. No hypotheses or instance arguments to drop (evidence (1)). Changing the ring is a false generalisation (Q9).
- Mathlib search (Phase 5): building blocks only (`degreesLE`, `degreeOf`, `coeff`). No `MvPolynomial` height/sup-norm.
- Composition check (Phase 6): COMPOSABLE as a one-line set-builder over mathlib primitives (evidence (3)).

**Rationale:**

`Roth.RSet` names the set of nonzero integer polynomials in a multidegree box with naive height at most `B`, exactly as the source defines `ℛ_m(B; r_1, …, r_m)`. It contributes nothing mathematically new: the degree clause is mathlib's `degreesLE ℤ σ (toMultiset r)` (compiled, evidence (2)–(3)), and the other two clauses are `R ≠ 0` and a pointwise coefficient bound. No source outside Roth-type proofs singles out this set, and mathlib would not want a `Set` of integer polynomials tied to a real bound `B` under the generic name `RSet`. The one piece of genuinely reusable infrastructure hiding here is a coefficient sup-norm (naive height) for `MvPolynomial`. Mathlib has it only for `Polynomial` (`Polynomial.supNorm`), with the other ℓ^p norms listed as TODO. That belongs with the `Roth.normOne` upstreaming (YES-but-generalise-first there), not with this set.

Belongs-elsewhere check: the def is worth keeping project-locally, so it is not junk. It is the paper's notation, it gives about 20 statements in Theta.lean and MainLemma.lean a readable hypothesis `R ∈ RSet B r`, and Phase 2b found the API-name exemption. The "inline at call sites" refactor that normally follows this bucket is not recommended. Inlining the three-way conjunction into `indexSet`, `index_le_Θ`, `Θ_le_of_forall_index_le`, `index_separated_mul_le_aux`, `index_det_le`, `index_le_lem6`, `sub_mem_RSet` and the four Lemma 9 existence lemmas (MainLemma.lean:550–698) would make those statements longer and lose the link to the source. The composition matters only for upstreaming: it is why the def should not go to mathlib.

Mathlib building blocks: `MvPolynomial.degreesLE` (Mathlib/Algebra/MvPolynomial/Degrees.lean:616), `MvPolynomial.degreeOf` / `degreeOf_def`, `MvPolynomial.coeff`, `Finsupp.toMultiset`.
Composition sketch (≤3 lines):
```lean
example {σ : Type*} [DecidableEq σ] (B : ℝ) (r : σ →₀ ℕ) :
    Roth.RSet B r = {R | R ≠ 0 ∧ R ∈ degreesLE ℤ σ (Finsupp.toMultiset r) ∧
      ∀ d, |((R.coeff d : ℤ) : ℝ)| ≤ B} := by
  ext R; simp only [Roth.RSet, Set.mem_ofPred_eq, forall_degreeOf_le_iff_mem_degreesLE]
```
Call sites in our project (from Phase 6.0): about 24 lines (14 in MainLemma.lean, 10 in Theta.lean).
Refactor plan: none required. Keep `Roth.RSet` as project-local notation, and do not upstream it. Optionally add "the degree condition is `R ∈ degreesLE ℤ σ (toMultiset r)`" to the docstring. If a mathlib `MvPolynomial` sup-norm ever lands (see `Roth.normOne`), restate the third clause as `supNorm R ≤ B`; the call sites are unchanged.
Next action: no upstreaming. Leave the def and its call sites as is.

---

### Next step

No upstreaming. Keep `Roth.RSet` in Roth/Theta.lean. Any reusable content (an `MvPolynomial` coefficient norm) is tracked under `Roth.normOne`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.RSet/RSet_vs_mathlib.lean` (imports `Roth.Theta`; `lake env lean` compiles with no output):
  (1) `RSet B r` elaborates for a bare `σ` with no `Fintype` / `DecidableEq`;
  (2) `forall_degreeOf_le_iff_mem_degreesLE`: `(∀ j, degreeOf j R ≤ r j) ↔ R ∈ degreesLE ℤ σ (Finsupp.toMultiset r)` (one `simp`);
  (3) `RSet_eq`: `RSet B r` equals the set-builder over `R ≠ 0`, `degreesLE`, and the coefficient bound.
  A first draft also referenced `Polynomial.supNorm`, which is not imported by `Roth.Theta`, and used the deprecated `Set.mem_setOf_eq`. Both were removed or replaced, and the file now compiles clean.
- Mathlib greps: `def degreesLE`, `def restrictSupport`, `def restrictDegree`, `supNorm`, `NumberTheory/Height/*`, `coeffsIn ⊓ degreesLE` in ChevalleyComplexity, `namespace Roth` (none).
- Lean-Finder (1), LeanSearch (2), Loogle (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex §5 l.643–666.
- Project grep `grep -rn RSet Roth/` for the call-sites table.
