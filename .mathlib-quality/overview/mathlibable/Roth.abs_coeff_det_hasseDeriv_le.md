# /mathlibable report — `Roth.abs_coeff_det_hasseDeriv_le`

**Verdict: YES-but-generalise-first.** Reason: verified redundant `hB0` removal, coefficient `RingSeminorm` generalization and arbitrary finite matrix index. This is a genuine polynomial coefficient estimate; the strongest checked form and complete caller compile. This is canonical declaration 100 of 293, source `Roth/CoeffNorm.lean:258`.

## Phase 0 — Doctor

The shared baseline succeeded with 2467 jobs; all 17 current source/pin hashes freshly match. See [baseline-build.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/baseline-build.txt) and [inputs.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/inputs.json). The theorem resolves, has no sorry, and its native type and axioms are checked. The entire declaring module and full caller module `Roth/Theta.lean` were read, together with HasseDeriv and Box. The file collects coefficient size, derivative, diagonal and evaluation estimates for Roth's proof.

At this file-completion milestone, root ran a new full `lake build`: exit 0,2467 jobs, no errors or warnings; [file-completion-build.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/file-completion-build.json) and [file-completion-build.log](../evidence/Roth.abs_coeff_det_hasseDeriv_le/file-completion-build.log). Production files and pins remain unchanged.

## Phase 1 — Comprehend

Let P be an integer polynomial in finitely many variables, of coordinate degrees at most rj and coefficients of absolute value at most B. Form an l×l matrix by taking arbitrary Hasse derivatives of this same P. Each coefficient of its determinant has absolute value at most N^l l! B^l 2^(S l), where N=∏j(rj+1) and S=∑j rj. There is no nonzero-P, positive-size, derivative-order or positive-degree assumption.

The proof bounds a coefficient by coefficient length, bounds each derivative length by 2^S times the original length, bounds the latter by NB using the support box, and sums l! products in the Leibniz determinant expansion. The final scalar identity is ring normalization. The explicit B≥0 assumption is derivable from the coefficient ceiling.

Full native elaborated type ([native-full-type.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-full-type.json)):

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ)
  (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      0 ≤ B →
        (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
          ∀ (d : σ →₀ ℕ),
            |↑((Matrix.of fun μ ν ↦ (MvPolynomial.hasseDeriv (E μ ν)) P).det.coeff d)| ≤
              (∏ j, (↑(r j) + 1)) ^ l * ↑l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)
```

The source proof is preserved in [source-module.lean.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/source-module.lean.txt); original native source/returned receipt are [native-original-executed.lean.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-original-executed.lean.txt) and [native-original-receipt.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-original-receipt.json). `#print` of the kernel proof was tool-elided by 26659 characters; this is not claimed to be a complete printed kernel proof. The full source proof, full elaborated type and standard axiom result are preserved. Axioms are exactly propext, Classical.choice and Quot.sound.

## Phase 2 — Preliminary checks

BIG: explicitly named in the module's Main results and identified as source Lemma 3. The full exhaustive literature protocol applies independently of size. One-line definition-only test: n/a, theorem. The proof is a real coefficient/length/determinant argument, not definitional glue; no inherited verdict or one-liner exemption is used.

## Phase 3 — Exhaustive literature

Each web artifact contains exact requests, returned-response SHA256/bytes/status, locators and original concise summaries. Full bodies are not archived; credential-bearing URL query parameters are excluded.

| Channel | Actual query/locator | Evidence | Finding |
| --- | --- | --- | --- |
| General web specific | Hasse derivative determinant polynomial coefficient bound Roth lemma3 | [web-0.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-0.json) | Standard coefficient/Taylor definitions over rings and fields; no exact size theorem found. |
| General web standard | polynomial coefficient l1 norm determinant height bound seminorm factorial | [web-1.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-1.json) | Coefficient length versus sup height; polynomial norm literature and mathlib TODO. |
| General web aliases | divided derivatives polynomial height Leibniz determinant bound | [web-2.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-2.json) | Divided-derivative terminology; no complete matching determinant estimate. |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Tool inventory checked | Optional channel unavailable; no invented response. |
| Local reference | clean.tex §3 Lemma 3 lines 438–500 | [local-literature-excerpt.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/local-literature-excerpt.txt) | Exact formula N^l l! (B2^S)^l, proof via coefficient length. |
| nLab | site:ncatlab.org/nlab Hasse derivative seminorm polynomial | [web-3.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-3.json); [web-8.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-8.json) | Hasse-Schmidt derivation/derivative pages located; direct XHTML fetch unsupported 400, recorded honestly. |
| nCatLab | site:ncatlab.org and explicit site:ncatlab.org/ncatlab | [web-4.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-4.json); [web-9.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-9.json) | No separate categorical norm estimate; related Hasse-Schmidt algebra. |
| Stacks | site:stacks.math.columbia.edu divided power Hasse derivative | [web-5.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-5.json); [web-8.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-8.json) | Opened tag07GL Definition 23.2.1; ring/ideal divided powers, not coefficient sizes. |
| MathOverflow | site:mathoverflow.net Hasse derivatives polynomial height determinant | [web-6.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-6.json) | Coefficient-height and polynomial determinant-root questions; no replacement estimate. |
| Recent arXiv | site:arxiv.org Hasse derivatives polynomial height after:2021-10-27 before:2026-10-28 | [web-7.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-7.json); [web-9.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/web-9.json) | Barajas 2023 (2305.04537) abstract opened; derivation modules, not norm bounds. March 2021 skew-polynomial hit is outside window and not counted. |

Literature summary: the concept is a coefficient-height bound for a determinant of divided/Hasse derivatives, proved using coefficient length. The local paper supplies the exact integer formula; primary general Hasse sources work over rings, while divided-power structures address a distinct abstraction. There is no claim that a recent paper states the exact RingSeminorm estimate. That extension is an independently verified mathematical inference from the proof's abstract size laws. Size targets vary (sup height, coefficient length, nonarchimedean Gauss norm); those must not be conflated. Original polynomial content and general seminorm form agree under actual specialization.

Primary locators: [Stacks divided powers](https://stacks.math.columbia.edu/tag/07GL), [Barajas 2023 abstract](https://arxiv.org/abs/2305.04537), [mathlib Polynomial Norm TODO](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/Norm.html). The pinned source archive, rather than external moving docs, grounds mathlib API claims.

## Phase 4a — All parameters and hypotheses

| Parameter | Role | Weakening/retention |
| --- | --- | --- |
| σ : Type* | Arbitrary variable universe | Keep; no finite-cardinality coding in variable names. |
| [Fintype σ] | Finite variables | Global product and sum on RHS need a finite type. Finite-support variant changes interface and is not claimed verified. |
| l : ℕ, Fin l | Matrix size | Generalize to arbitrary finite index ι with cardι in formula; specialization recovers Fin l. |
| E : Fin l → Fin l → σ →₀ ℕ | Arbitrary multiindices | Already arbitrary; no triangularity, disjointness or derivative-order bounds needed. |
| P : MvPolynomial σ ℤ | Integer coefficients | Generalize ℤ/real absolute value to CommRing R with RingSeminorm p and p1≤1; the coefficient length proof uses only additive and submultiplicative bounds. |
| r : σ → ℕ | Degree ceiling vector | Keep natural exponents; hP supplies support box bound. No positive r assumption is necessary. |
| hP : ∀ j, degreeOf j P ≤ r j | Degree bound | Used in both support count and binomial estimate; retain. |
| B : ℝ | Coefficient-size ceiling | Keep real scalar bound to match bundled RingSeminorm codomain; arbitrary ordered target is not claimed verified. |
| hB0 : 0 ≤ B | Nonnegative ceiling | Drop: inferred from hB at exponent0 and nonnegative size. Verified omitted-hypothesis specialization and full caller replay. |
| hB : ∀ d, |coeff d P| ≤ B | Coefficient ceiling | Retain; p(coeff d P) in generalized form. Local-to-support hypotheses would need separate nonnegativity for zero polynomial. |
| d : σ →₀ ℕ | Output coefficient | Already arbitrary; retain. |

## Phase 4b — Verified generality

STRICTLY NARROWER THAN STANDARD in the precise verified sense: `hB0` is dropped mechanically; integer coefficient absolute size is generalized to a normalized RingSeminorm on any commutative ring, and `Fin l` is replaced by any finite matrix index. CommRing remains the fixed determinant interface; CommSemiring cannot provide its signs. Arbitrary infinite variable types with a finite support-set RHS or arbitrary ordered size codomain would require restatement and are not claimed verified.

[native-generic-clean-executed.lean.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-generic-clean-executed.lean.txt) and [native-index-accepted-executed.lean.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-index-accepted-executed.lean.txt) contain the actual checked statements and proofs; their matching native receipts confirm success/partial=false and standard axioms. The strongest target statement is:

```lean
theorem bound [Fintype σ] (p : RingSeminorm R) (hp : p 1 ≤ 1)
    {ι : Type*} [Fintype ι] [DecidableEq ι]
    (E : ι → ι → (σ →₀ ℕ)) (P : MvPolynomial σ R) {r : σ → ℕ}
    (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB : ∀ d, p (P.coeff d) ≤ B)
    (d : σ →₀ ℕ) :
    p ((Matrix.of fun μ ν : ι ↦ hasseDeriv (E μ ν) P).det.coeff d) ≤
      (∏ j, ((r j : ℝ) + 1)) ^ Fintype.card ι * (Fintype.card ι).factorial * B ^ Fintype.card ι *
        2 ^ ((∑ j, r j) * Fintype.card ι)
```

Its `intSize` specialization recovers the original conclusion without `hB0`. The entire sole caller compiles through this strongest specialization. This is a checked transfer with helper lemmas, not an unverified claim that the old proof accepts a text substitution. Named hypothesis drop is cheap; coefficient-size API extraction is moderate, no cost-based downgrade is used.

## Phase 4c — Modern-idiom diagnostic

| Q | Applies | Restatement/reason | Concrete downstream consequence |
| --- | --- | --- | --- |
| 1 | yes | RingSeminorm p bundles additive/nonnegative/negative/submultiplicative laws; retain explicit p1≤1. | map_add_le_add, map_mul_le_mul, map_neg_eq_map compose directly. |
| 2 | no | Finite algebraic inequality has no convergence, metric or topology. | No filters needed. |
| 3 | no | No object with universal-property construction is being chosen. | No new universal-property layer. |
| 4 | no | No ad hoc closed subset predicate; RingSeminorm is an existing bundled function. | No substructure lattice needed. |
| 5 | yes | ℤ coefficients → arbitrary commutative ring carrying RingSeminorm; retain CommRing for determinant signs and commutativity. | Works over real, complex or other seminormed coefficient rings without separate integer casts. |
| 6 | no | No category or higher categorical structure occurs. | Higher categories do not improve coefficient bounds. |
| 7 | yes | Fin l matrix indices → arbitrary finite ι and cardι. Natural exponent monoid remains σ→₀ℕ. | Use Matrix.det on existing finite-index matrices without transporting to Fin. |
| 8 | yes | Proof body contains no ℤ-specific cast/absolute operations after statement: 0 ℤ, 0 Int.cast, 0 abs tokens in source proof; normOne calls expose abstract coefficient length laws. | Same Hasse bound feeds RingSeminorm coefficient estimate for other rings; new helper proofs establish transfer. |
| 9 | no false generalization | Generalized theorem has original as actual intSize specialization. RingSeminorm is not replaced with AbsoluteValue, since coefficient length is not multiplicative. | No wrong equality of distinct norms. Normalization p1≤1 retained, including empty determinant. |

The Q8 concrete-via-abstract diagnostic fires: after its statement, the original proof contains 0 ℤ, 0 Int.cast and0 abs tokens; it invokes coefficient length laws and a support count. `RingSeminorm` makes these laws reusable over real/complex or other seminormed coefficient rings. False-generalization guard passes by actual specialization; retaining p1≤1 handles the empty determinant: its value is1 and the scalar bound is1. An arbitrary RingSeminorm need not be normalized; the original real absolute value supplies p1=1, so this introduces no extra premise in the integer specialization. Do not use multiplicative `AbsoluteValue` to model coefficient length.

## Phase 4.5 — Infrastructure risk

Declaration kind theorem: n/a. All six risks are explicitly accounted for:

| Risk | Reason |
| --- | --- |
| Typeclass diamond | n/a: theorem introduces no data, instances or coercion paths |
| Reducibility leak | n/a: theorem introduces no data, instances or coercion paths |
| Non-canonical unfolding | n/a: theorem introduces no data, instances or coercion paths |
| Instance priority collision | n/a: theorem introduces no data, instances or coercion paths |
| Universe polymorphism | n/a: theorem introduces no data, instances or coercion paths |
| Coercion ambiguity | n/a: theorem introduces no data, instances or coercion paths |

Auxiliary bundled functions in experiments are local witness constructions, not proposed global instances. No new typeclass path is introduced by the target theorem.

## Phase 4.6 — Proof strategy

| Q | Applies | Alternative/reason |
| --- | --- | --- |
| 1 | no | No topology/epsilon-delta argument. |
| 2 | no | Finite coefficient sums are natural; ideal/submodule inclusions cannot express numerical upper bound. |
| 3 | no | No sequence convergence. |
| 4 | no | No categorical construction. |
| 5 | yes | Coefficient l1 size, size_mul, normalized RingSeminorm determinant and Hasse-size bounds form reusable API; use these then support-card bound and ring normalization. |

REFACTOR-RECOMMENDED: expose coefficient l1 size and normalized RingSeminorm determinant estimates, then compose derivative-length and support bounds. This is cleaner and serves other coefficient rings. It needs genuinely new API, not a more powerful tactic on a hidden existing theorem. Parent Hasse and seminorm-helper experiments are new proofs and never counted as current mathlib facts.

## Phase 5 — All five actual mathlib methods

| Method | Current form | Literature-standard form | Abstract form |
| --- | --- | --- | --- |
| lean_leanfinder | [lean_leanfinder-current.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_leanfinder-current.json) | [lean_leanfinder-standard.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_leanfinder-standard.json) | [lean_leanfinder-abstract.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_leanfinder-abstract.json) |
| lean_loogle | [lean_loogle-current.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_loogle-current.json) | [lean_loogle-standard.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_loogle-standard.json) | [lean_loogle-abstract.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_loogle-abstract.json) |
| lean_leansearch | [lean_leansearch-current.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_leansearch-current.json) | [lean_leansearch-standard.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_leansearch-standard.json) | [lean_leansearch-abstract.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_leansearch-abstract.json) |
| lean_local_search | [lean_local_search-current.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_local_search-current.json) | [lean_local_search-standard.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_local_search-standard.json) | [lean_local_search-abstract.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_local_search-abstract.json) |
| Source rg | [rg-current.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/rg-current.json) | [rg-literature.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/rg-literature.json) | [rg-abstract.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/rg-abstract.json) |

All 12 initial external/local tool requests and one Loogle correction were executed. The original current-form Loogle query rejected MvPolynomial.coeff as unknown; its exact failure is preserved, then the quoted name-pattern retry succeeded ([retry](../evidence/Roth.abs_coeff_det_hasseDeriv_le/lean_loogle-current-retry.json)). These returned affine univariate determinant coefficient identities, not a norm estimate; source searches are separately preserved. Finder returned Polynomial.hasseDeriv_coeff/apply and unrelated polynomial determinant statements. Loogle found Matrix.det_le, det_sum_le and det_sum_smul_le; these are positive partial candidates. Local symbol index was unavailable, so its source matches do not establish absence. External indices can differ from the pinned revision.

Pinned positive signatures and actual isolated coefficient-size helper proofs appear in [native-raw-executed.lean.txt](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-raw-executed.lean.txt) / [native-raw-receipt.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-raw-receipt.json). `Matrix.det_le` uses `AbsoluteValue`, whose exact multiplicativity fails for coefficient length: for example length((1+X)(1−X))=2 whereas the product of lengths is4. `Polynomial.hasseDeriv_coeff` concerns a univariate derivative only. Polynomial.le_gaussNorm/gaussNorm_mul_le concerns a supremum with additional nonarchimedean conditions, not the archimedean coefficient sum. These are not equivalent replacements.

The untruncated full-name search is [rg-full-name.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/rg-full-name.json). No absence conclusion rests solely on failed searches. The isolated mathlib-only run guards missing project target and constructs size_mul/coeff_le_size/size_le_card independently. The complete generic Hasse/determinant proof runs in disk context because the multivariate Hasse interface itself is project API. No speculative exact?/absence rerun or raised limits was used.

Concrete gap: pinned `Mathlib/Analysis/Polynomial/Norm.lean` has an explicit TODO for other lp norms, including coefficient length. An arbitrary commutative-ring coefficient length requires only submultiplicativity; current `Matrix.det_le` takes a stricter multiplicative absolute value. These are the exact missing organizing interfaces behind this bound.

## Phase 5.5 — Statement shape

Normal form: `p (coeff d determinant) ≤ scalar bound`, rather than integer casts or a new ad hoc coefficient maximum. Related alternatives are a bound on coefficient length and a sup-height bound; the length bound is stronger and supplies the coefficient form by coeff_le_size. Proposed primary statement uses existing RingSeminorm with real scalar target; no orthogonal equivalence or RHS simp normalization issue arises.

Syntactic generality: verified arbitrary finite matrix index avoids unnecessary reindexing to Fin; retain pointwise degree and coefficient ceilings because callers already have them. Superfluous-argument audit is the full Phase4a table: only hB0 drops. r may be0, P may be0 and matrix may be empty. Overall: RESTATE-BEFORE-SHIP.

## Phase 6.0 — Complete callers and inline audit

Internal use count1; external-to-file count1. Sole caller is `Roth.index_det_le`, `Roth/Theta.lean:475`; it applies a constant degree ceiling r₁ and simplifies the scalar bound to lem6M. No independent inline rederivation of the full estimate was found. Nearby determinant-degree and determinant-length laws are distinct supporting estimates. Full source searches: [rg-callers.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/rg-callers.json) and [rg-inline.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/rg-inline.json).

The entire caller, including factor coefficient estimates and private separated-index helper, compiles with the strongest generalized specialization. Private helper access uses `Lean.mkPrivateNameCore` through a term elaborator, not a textual numeric private identifier and not an axiom. The exact ordered canonical 293 proof audit reports requested=293, unique=293, present=293, values=293 and sole direct consumer Roth.index_det_le. This is a source-level direct-proof constant audit, not a claim about transitive kernel/simp closure. See [native-consumers-receipt.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-consumers-receipt.json) and [native-index-accepted-receipt.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/native-index-accepted-receipt.json).

## Phase 6 — Actual composition experiments

Attempt1: apply Matrix.det_le to the polynomial coefficient length. Partial: candidate requires multiplicative AbsoluteValue; length is merely submultiplicative. Isolated positive helper execution constructs the correct laws. This does not yield the Hasse/support factors in ≤3 existing calls.

Attempt2: coefficient≤length, determinant seminorm estimate, derivative-length estimate and support-card bound. The checked proof succeeds using NEW genericDet, NEW NormHasseGeneric.bound, NEW size_mul and project box/Hasse API, plus scalar normalization. That is a genuine proof with support/binomial reasoning; those new helpers do not become existing mathlib building blocks because they were accepted in prior assessments. The archived exact proof exhibits what must be added.

Attempt3: feed the strongest new generic form into the full existing caller. Succeeds by actual native replay, dropping hB0; demonstrates a useful abstraction and a mechanical future caller change. It is not a current-mathlib composition.

Conclusion: NOT-COMPOSABLE in ≤3 existing mathlib calls. No closing simp-[defs] proof was found or asserted. The single-use signal raises an API-grain question but does not erase the concrete norm/Hasse gap or justify a NO verdict.

## Phase 7 — Actionable verdict

YES-but-generalise-first, with MODERN-IDIOM and verified hypothesis weakening. Add the RingSeminorm-based coefficient bound at arbitrary finite matrix index, omit redundant hB0 and expose the underlying coefficient-length machinery. The contribution is the support/binomial/determinant length estimate in a reusable coefficient-ring interface, not the integer wrapper alone.

Proposed upstream path: `Mathlib/Analysis/Polynomial/MvHasseDeriv.lean`, after multivariate Hasse API and coefficient-size infrastructure; determinant seminorm helper belongs in `Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean` or a focused seminorm sibling. Proposed PR title: `feat(Analysis/MvPolynomial): bound coefficients of Hasse derivative determinants`.

Group with already accepted YES declarations `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.normOne_hasseDeriv_le` and `Roth.normOne_det_le`, sequencing basic Hasse API before norm bounds. Their actual accepted verdicts were read from progress at 99 completed declarations; [accepted-yes-grouping.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/accepted-yes-grouping.json). Do not infer verdicts from names. The specialized integer spelling can remain local to `Roth/CoeffNorm.lean` until generic API lands; its sole caller should use intSize specialization and omit hB0.

Pre-PR checklist: `/generalise Roth.abs_coeff_det_hasseDeriv_le`; `/cleanup Roth/CoeffNorm.lean Roth.abs_coeff_det_hasseDeriv_le`; settle coefficient-length naming and normalized determinant seminorm helper; select reviewers from relevant recent Hasse/seminorm commits. The recorded actual recent commits identify Moritz Firsching (Hasse map API,334438dace) and Moritz Doll (seminorm organization, c404bb7edd) as relevant reviewer candidates, with Yaël Dillies for coefficient representation conventions; [reviewer-git.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/reviewer-git.json). These are grounded reviewer suggestions, not inferred approval or guaranteed availability.

## Phase 8 — Evidence and handoff

All phases completed. Five accepted native sets include original type/axioms, generic coefficient-ring form, complete caller plus 293 audit, strongest index form plus specialization/full caller, and isolated mathlib-only size helper/candidate checks. Five actual failed native attempts are preserved separately; none is accepted proof evidence. Preparation-only probes are labelled as such. Full-file errors and axioms are checked, while positive info assertions are restricted to fresh target regions. New helper proofs use only standard axioms, no sorry/admit/unsafe/native_decide/new axioms/raised limits.

Verification ledger: [verification.json](../evidence/Roth.abs_coeff_det_hasseDeriv_le/verification.json). Read-only portable validator: [validate.py](../evidence/Roth.abs_coeff_det_hasseDeriv_le/validate.py). Current copy manifest validates scratch and integrated layouts. Root acceptance remains pending until independent review; no Git, production, progress or deployment writes were made by this worker.
