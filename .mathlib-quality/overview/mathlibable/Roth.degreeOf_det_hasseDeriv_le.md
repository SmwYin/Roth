# Roth.degreeOf_det_hasseDeriv_le — YES-but-generalise-first

## Phase 0 — Baseline

Resolved public theorem at `Roth/CoeffNorm.lean:245`, canonical index 99. Reusable baseline `lake build` succeeded with 2467 jobs at `99f19fda4b3cbee38fc0d31af76075834f5cc265`. All 17 source/pin hashes freshly match that baseline. No production changes. The module develops coefficient norms, determinant estimates, diagonal substitution and evaluation bounds. Entire declaring module, Hasse module and sole calling module were read. [Baseline](../evidence/Roth.degreeOf_det_hasseDeriv_le/baseline-build.txt), [fresh hashes](../evidence/Roth.degreeOf_det_hasseDeriv_le/inputs.json), [module](../evidence/Roth.degreeOf_det_hasseDeriv_le/source-module.lean.txt), [caller module](../evidence/Roth.degreeOf_det_hasseDeriv_le/source-callers.lean.txt).

## Phase 1 — Statement and proof

For any polynomial P with integer coefficients and coordinate degrees bounded by r, form an l by l matrix whose entries are arbitrary Hasse derivatives of P. Its determinant has degree at most l times r(j) in each variable j. No nonvanishing assumption, finite variable set, positive matrix size or bound on derivative orders is needed.

Full native type:

```lean
∀ {σ : Type u_1} {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ)
  (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ (j : σ), MvPolynomial.degreeOf j
      (Matrix.of fun μ ν ↦ (MvPolynomial.hasseDeriv (E μ ν)) P).det ≤ l * r j
```

σ is the arbitrary variable type, l the matrix size, E its matrix of multi-indices, P the input polynomial, r the coordinate bounds, hP their proof and j the selected coordinate. The proof expands the determinant by permutations, bounds degree of a sum by the supremum, removes the constant sign factor, bounds degree of a product by a sum, and applies Hasse degree monotonicity to each entry. The sum of l copies of r(j) is l r(j). This is a substantive finite algebra argument. Original proof and axioms are printed in the exact native evidence; axioms are only `propext`, `Classical.choice`, `Quot.sound`. [Executed original](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-original-executed.lean.txt), [complete receipt](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-original-success.json).

Project dependencies: `MvPolynomial.hasseDeriv` and `MvPolynomial.degreeOf_hasseDeriv_le`; both live in `Roth/HasseDeriv.lean`. Their accepted upstream assessments do not make them current mathlib facts.

## Phase 2 — Preliminary checks

SMALL: a degree-estimate helper, not a named main result or new structure. The exhaustive search is unchanged by this classification. One-line definition test: n/a, theorem. Its six substantive proof lines include several independent inequalities and finite-sum normalization.

## Phase 3 — Exhaustive literature

Every listed channel was executed, including the three distinct general-web forms. Web evidence stores exact requests, returned response SHA256/bytes/status, locators and original summaries, with no full result/article bodies. Returned URL query parameters were stripped; no credential values are stored.

| Channel | Actual request / result | Evidence |
|---|---|---|
| General specific | `Roth theorem determinant Hasse derivatives degree bound l r_j`; Stanford notes §17 build the relevant generalized Wronskian determinant | [web0](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-0.json) |
| General standard | `polynomial matrix determinant degree bound sum column degrees`; Storjohann polynomial matrix inversion p12 gives sharper maximum over permutation sums of entry degrees | [web1](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-1.json) |
| General aliases | `Leibniz formula determinant polynomial ring degree bound`; determinant expansion and polynomial-ring context | [web2](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-2.json) |
| ChatGPT math MCP | n/a: `ask_chatgpt_math` unavailable; optional channel, no fabricated second opinion | tool inventory checked |
| Local references | `clean.tex:435`, end proof Lemma2, states the exact l r(j) consequence of entry degrees; Lemma3 is a separate coefficient bound | [excerpt](../evidence/Roth.degreeOf_det_hasseDeriv_le/local-literature-excerpt.txt), [hash](../evidence/Roth.degreeOf_det_hasseDeriv_le/local-literature-source.json) |
| nLab | `site:ncatlab.org/nlab determinant commutative ring polynomial`; determinant and polynomial pages located | [web3](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-3.json) |
| nCatLab | `site:ncatlab.org/ncatlab determinant polynomial degree`; checked, no dedicated determinant degree law; categorical enhancement unnecessary | [web3](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-3.json) |
| Stacks | `site:stacks.math.columbia.edu determinant polynomial ring`; tag0B2V discusses generic determinant polynomial, a related coordinate-degree context, not this Hasse result | [web4](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-4.json) |
| MathOverflow | `site:mathoverflow.net polynomial matrix determinant degree bound`; related determinant representations and algebra, no exact Hasse degree hit | [web4](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-4.json) |
| Recent arXiv | `site:arxiv.org polynomial matrix determinant column degree after:2021-10-27 before:2026-10-28`; 2306.06104 and 2311.08408 polynomial matrix completion; related, no exact Hasse law | [web5](../evidence/Roth.degreeOf_det_hasseDeriv_le/web-5.json) |

Standard concept: degree upper bounds for polynomial determinants. The uniform l r bound is a specialization of a column-degree sum bound, itself bounded by a maximum of permutation entry-degree sums. [Primary polynomial matrix inversion source, p12](https://cs.uwaterloo.ca/~astorjoh/polyinv.pdf) explicitly records the permutation bound. [Stanford Roth notes §17](https://math.stanford.edu/~ksound/TransNotes.pdf) explain the Hasse/Wronskian application. The literature often works over fields for matrix algorithms; the degree upper-bound proof itself needs only a commutative ring, as formally verified here. No historical change of this elementary bound was established by these searches. No search failure is treated as proof of absence.

## Phase 4a — Parameter generality

| Parameter | Current form | Verified broader form / limit |
|---|---|---|
| σ | arbitrary Type* | Already general; no finiteness or decidable equality needed |
| coefficients | ℤ | Any `[CommRing R]`, including zero divisors and positive characteristic |
| matrix size | `Fin l` | Any finite square index ι, `[Fintype ι] [DecidableEq ι]` |
| E | arbitrary multi-index matrix | Retained, no order restriction |
| P | any polynomial | Retained, including zero |
| r | all-coordinate bound function | One scalar b at the chosen coordinate suffices |
| hP | `∀ j, degreeOf j P ≤ r j` | `degreeOf j P ≤ b`; other coordinates unused |
| j | chosen variable | Essential coordinate retained |

CommSemiring is not claimed: the existing `Matrix.det` interface requires CommRing, even though the Hasse degree inequality alone is semiring-general. No claim of noncommutative determinant generalization is made.

## Phase 4b — Verified restatement

STRICTLY NARROWER THAN STANDARD. Cheap, mechanical coefficient/index/hypothesis weakening passed native Lean; it does not require modifying the parent Hasse definition or any production file:

```lean
theorem hasse_generic {σ R ι : Type*} [CommRing R] [Fintype ι] [DecidableEq ι]
    (E : ι → ι → (σ →₀ ℕ)) (P : MvPolynomial σ R) (j : σ)
    {b : ℕ} (hP : degreeOf j P ≤ b) :
    degreeOf j (Matrix.of fun μ ν ↦ hasseDeriv (E μ ν) P).det ≤ Fintype.card ι * b
```

The exact proof is the original proof with generalized types and localized hP. Original specialization and the entire current caller with both replacements also passed. [Executed consumers](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-consumers-executed.lean.txt), [receipt](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-consumers-success.json).

## Phase 4c — All nine modern idiom checks

| # | Check | Result and concrete consequence |
|---|---|---|
| 1 | Typeclasses | Yes: CommRing R abstracts integer coefficients; no domain/nontriviality required |
| 2 | Filters/nets | n/a: finite algebra, no limiting process |
| 3 | Universal property | No new characterization needed; existing MvPolynomial and determinant suffice |
| 4 | Bundled substructures | n/a: no closure predicate or ad hoc subset |
| 5 | Hierarchy | Yes: integer ring generalized to CommRing; determinant interface fixes the lower boundary |
| 6 | Higher category | n/a: scalar inequality, no category construction |
| 7 | Concrete indices | Yes: arbitrary finite square index composes directly with Matrix API |
| 8 | Concrete via abstract | Yes: Hasse-specific content appears only in final entry-degree inequality; a generic determinant degree helper serves all polynomial matrices |
| 9 | False-generalization guard | Passed: same determinant and coordinate degree; original specialization verified. Reject replacing determinant by permanent or upper bound by equality |

Modern-idiom verdict: generalize coefficients/index/local hypothesis, and factor generic polynomial determinant degree estimates. The mathlib-only `entry_bound` and column-specific `row_bound` (historical scratch name; b depends on column ν) were proved and verified independently, but they are NEW helpers, not evidence of an existing mathlib replacement. [Raw exact source](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-raw-executed.lean.txt), [receipt](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-raw-success.json).

## Phase 4.5 — Infrastructure risks

| Risk | Status |
|---|---|
| Typeclass diamond | n/a: theorem introduces no instances |
| Reducibility leak | n/a: no data definition or reducibility annotation |
| Non-canonical unfolding | n/a: theorem is a propositional upper bound |
| Instance priority | n/a: no instance |
| Universes | n/a as infrastructure risk; generic independent Type* parameters compiled |
| Coercion ambiguity | n/a: no new coercion |

## Phase 4.6 — Proof strategy

| # | Strategy check | Finding |
|---|---|---|
| 1 | Topological ε–δ vs filters | n/a |
| 2 | Elements vs ideals/submodules | Current finite Leibniz proof is natural; no substructure improvement |
| 3 | Sequences vs nets | n/a |
| 4 | Construction vs categorical universal property | n/a |
| 5 | Missing helpful mathlib lemmas | Generic coordinate-degree bound for arbitrary polynomial determinants; raw proofs isolate the gap |

Verdict: current proof idiomatic, but generic determinant-degree API should precede specialized Hasse corollaries. No performance or implementation cost is used to downgrade the verdict.

## Phase 5 — Five-method mathlib search

All methods were run on current, literature-standard and abstract forms; [full exact requests and responses](../evidence/Roth.degreeOf_det_hasseDeriv_le/formal-search.json).

| Method | Current | Standard | Abstract |
|---|---|---|---|
| LeanFinder | Hasse determinant degree; unrelated Chevalley degree results | polynomial matrix determinant sum column bounds; affine degree1 hit | CommRing multivariate determinant; same affine hit |
| Loogle | `MvPolynomial.degreeOf, Matrix.det`: no items | `Polynomial.natDegree, Matrix.det`: affine determinant and monic coefficient matrix results | `MvPolynomial.degreeOf, _ ≤ _`: sum/product degree building blocks |
| LeanSearch | Hasse derivative degree gives univariate Hasse bound and powers | column degree sum gives finite product inequalities | generic coordinate determinant gives det definition, absolute-value bounds, degree product |
| rg | Full untruncated degreeOf/det scan | matrix natDegree/det and column degree scan | determinant expansion, constant/product/sum inequalities |
| local search | `degreeOf_det`: project target | `natDegree_det`: affine determinant | `degreeOf`: pinned/project candidates; index unavailable reported honestly |

Pinned positive candidate `Polynomial.natDegree_det_X_add_C_le`, `Mathlib/LinearAlgebra/Matrix/Polynomial.lean`, has A,B matrices over a CommRing and bounds `natDegree (det (X • A.map C + B.map C))` by matrix cardinality. Native exact signature and axioms passed in a mathlib-only environment. It only handles affine univariate entries; arbitrary Hasse derivatives have arbitrary polynomial degree. `Matrix.det_le` bounds an absolute value by factorial times a power; coordinate degree is not such an absolute value (product degree is only subadditive generally). Neither is an existing replacement. [Candidate source](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-candidates-executed.lean.txt), [receipt](../evidence/Roth.degreeOf_det_hasseDeriv_le/native-candidates-success.json).

Existing blocks, pinned and native-checked: `Matrix.det_apply'`; `MvPolynomial.degreeOf_sum_le` (Degrees.lean:303), `degreeOf_prod_le` (:311), `degreeOf_C_mul_le` (:407); finite supremum and sum inequalities. Full-name and all scoped source searches are archived, not truncated. External indices may differ from the pin and local index unavailability proves no absence. No speculative exact? timeout was run or represented as a negative proof. The actual generic proof probes demonstrate how the existing blocks apply and which new helper is needed.

## Phase 5.5 — Statement shape

Normal form: use selected j, scalar b, and `degreeOf j M.det` with an arbitrary polynomial matrix; avoid a global r unless preserving downstream convenience. Syntactic generality: arbitrary finite square ι and CommRing coefficients compiled, as did the sharper per-column bound. Superfluous audit: σ, E, P, l and j describe the object; r and hP outside j are unnecessary in a single-coordinate statement. No unneeded typeclass is introduced: Fintype/DecidableEq belong to determinant's interface. Verdict: RESTATE-BEFORE-SHIP, explicitly included in next actions.

## Phase 6.0 — Callers and inline audit

| Caller | Location | Role | Verified plan |
|---|---|---|---|
| `Roth.exists_det_eq_mul` | Separation.lean:555 | Bound U degree at `some j` | Replace by generic Hasse bound at `some j` using `hr (some j)` |
| same declaration | Separation.lean:558 | Bound V degree at `none` | Replace by generic bound at `none` using `hr none` |

K=1 distinct caller, 2 explicit occurrences, both external to declaring file. The entire caller replay passed with both calls replaced, using its actual private rational-factor helper through a scratch term elaborator. That elaborator resolves an existing private constant, adds no axiom and is not a proposed production API. Canonical audit constructed all 293 names directly from tracked order, preserving private names, checked 293 unique, 293 present and 293 values; the sole direct proof consumer is `Roth.exists_det_eq_mul`. This covers direct constant references only, not transitive or simp dependency closure. [Callers](../evidence/Roth.degreeOf_det_hasseDeriv_le/callers.json), [source search](../evidence/Roth.degreeOf_det_hasseDeriv_le/rg-callers.json), [inline search](../evidence/Roth.degreeOf_det_hasseDeriv_le/rg-inline.json).

Inline search also finds GenWronskian.lean:124's finite-sum degree argument for linear independence, and Wronskian.lean:124's binomial coefficient determinant; neither re-derives this determinant degree bound. No dead-code inference is made.

## Phase 6 — Actual composition experiments

Attempt 1: specialize existing affine `natDegree_det_X_add_C_le`. Rejected structurally: it constrains entries to affine univariate polynomials, while these Hasse entries have arbitrary coordinate degree. Exact native candidate signature confirms that restriction.

Attempt 2: existing degree sum/product/constant rules plus determinant expansion. The actual mathlib-only generic entry and column proofs pass, but require determinant rewriting, a finite supremum argument, constant factor inequality, product-degree inequality, finite sum comparison and normalization. More than three mathlib calls and real reasoning; NOT-COMPOSABLE under Phase6b. Adding project `degreeOf_hasseDeriv_le` is an additional non-mathlib dependency. A new `entry_bound` cannot be counted as an existing building block. No closing `simp [defs]` or ≤3 existing-call proof was found or claimed.

Attempt 3: actual generalized Hasse proof and original/caller specializations pass. A one-line corollary from the newly proposed generic Hasse theorem is useful API organization, not proof that mathlib already has the result. Accepted proofs use only standard axioms. One rejected first consumer batch is preserved: direct textual private name parsing and inferred counter types failed, corrected by private-constant elaboration and explicit Nat counters. No failed attempt is accepted proof evidence. [Rejected exact source](../evidence/Roth.degreeOf_det_hasseDeriv_le/rejected-consumers-executed.lean.txt), [complete rejection receipt](../evidence/Roth.degreeOf_det_hasseDeriv_le/rejected-consumers-receipt.json).

## Phase 7 — Actionable verdict

**YES-but-generalise-first**, reason GENERALITY plus concrete-via-abstract. The gap is a coordinate-degree upper-bound API for determinants of arbitrary multivariate polynomial matrices. The current integer/Fin/global-bound version is narrower than its mechanically verified CommRing/arbitrary-finite/local-bound version. None of the existing candidate laws handles arbitrary entries at this generality. The finite determinant argument is substantive, and the project uses it twice.

Proposed upstream files: generic determinant degree estimates in `Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean` (import `Mathlib.Algebra.MvPolynomial.Degrees`); Hasse corollary in proposed `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` after the already accepted multivariate Hasse API. PR title: **feat(LinearAlgebra/Matrix): degree bounds for polynomial determinants**. Add the generic column and uniform-entry bounds first; add the generalized Hasse corollary with the parent API. Rename scratch `row_bound` to an accurate column-bound name; naming is not frozen by this assessment.

Grouping is based on accepted progress records, not inferred from lemma names: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_map` and `MvPolynomial.hasseDeriv_rename` are accepted YES-add-as-is and provide the Hasse foundation. `Roth.normOne_det_le` is separately accepted YES-but-generalise-first; its absolute-value bound is related organizationally but not a replacement or mandatory dependency. [Accepted grouping snapshot](../evidence/Roth.degreeOf_det_hasseDeriv_le/accepted-yes-grouping.json).

Checklist: run `/generalise Roth.degreeOf_det_hasseDeriv_le` with the compiled signature; factor generic determinant degree helpers and restate before ship; run `/cleanup Roth/CoeffNorm.lean Roth.degreeOf_det_hasseDeriv_le` and cleanup each new upstream declaration; retain or replace the two local convenience calls using the verified replay; run relevant tests and `/pre-submit`. Reviewer candidates from actual relevant recent history: Yaël Dillies (`631b214f7c`, 2026-09-02, MvPolynomial coefficient refactor) and Rao Xiaojia (`3b3cdbb692`, 2026-07-30, Matrix echelon API). These are suggestions only, no contact was made. [History receipt](../evidence/Roth.degreeOf_det_hasseDeriv_le/reviewer-git.json).

## Phase 8 — Completion and evidence

All mandatory phases PASS or justified theorem n/a. Four accepted native sets (original, mathlib-only raw determinant proofs, generalized Hasse/full caller/canonical audit, pinned candidate) and one rejected set are preserved exactly with full receipts. Verification unresolved list is empty; root acceptance remains pending independent review. No production, pin, Git or progress mutation was made by this worker. [Verification](../evidence/Roth.degreeOf_det_hasseDeriv_le/verification.json), [assessment](../evidence/Roth.degreeOf_det_hasseDeriv_le/assessment.json), [generality matrix](../evidence/Roth.degreeOf_det_hasseDeriv_le/generality.json), [portable validator](../evidence/Roth.degreeOf_det_hasseDeriv_le/validate.py).
