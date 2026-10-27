# Full mathlibable assessment — `Roth.exists_genWronskian_ne_zero`

**YES-but-generalise-first**. Remove the global `[Finite σ]` assumption using the verified finite-support/renaming bridge. This is the classical generalized Wronskian criterion in its substantive direction. It is the module's main theorem, and its derivative-order restriction is part of the content. The single caller does not make its proof a short composition of existing mathlib laws.

## Phase 0 — baseline and scope

The baseline `lake build` succeeded with 2467 jobs. All 17 source/pin hashes were freshly compared with the shared manifest and match; see [fresh inputs](../evidence/Roth.exists_genWronskian_ne_zero/inputs.json) and [baseline receipt](../evidence/Roth.exists_genWronskian_ne_zero/baseline-build.txt). Production files and pins remain unchanged. The whole 272-line declaring module, the whole 561-line caller module, the parent Hasse definition and the relevant primary local paper were read. Source and caller snapshots/hashes are in [source inputs](../evidence/Roth.exists_genWronskian_ne_zero/source-inputs.json), [declaring module](../evidence/Roth.exists_genWronskian_ne_zero/declaring-module.lean.txt), and [caller module](../evidence/Roth.exists_genWronskian_ne_zero/caller-module.lean.txt). A fresh full build at this completed-file boundary is separately recorded below.

## Phase 1 — statement and proof

Let φ₀,…,φₗ₋₁ be polynomials in finitely many variables over a characteristic-zero field K, linearly independent over K. There are multiindices D₀,…,Dₗ₋₁ with total degree |Dμ|≤μ such that det(ΔDμ φν) is a nonzero polynomial. The derivative Δ is the divided, or Hasse, derivative; in characteristic zero it differs from iterated partial derivatives by an invertible multiindex factorial. The assertion includes l=0 and empty variable types.

The full native elaborated type is in [original type](../evidence/Roth.exists_genWronskian_ne_zero/original-type.txt):

```lean
Roth.exists_genWronskian_ne_zero.{u_1, u_2} {K : Type u_1} [Field K]
    {σ : Type u_2} {l : ℕ} [Finite σ] [CharZero K] {φ : Fin l → MvPolynomial σ K}
    (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ ↑μ) ∧ Roth.genWronskian D φ ≠ 0
```

K is the coefficient field; σ the variable type; l the family size; φ the polynomial family; h its scalar independence. `[Finite σ]` is the actual instance, not a globally required enumeration `[Fintype σ]`. The existential chooses pure multiindex Hasse derivatives, not arbitrary coefficient-dependent differential operators or arbitrary linear maps.

The proof chooses a base k larger than every partial degree, substitutes xⱼ=t^(k^j), and uses the injectivity of bounded base-k exponents to preserve independence. The univariate Wronskian is nonzero. Each Hasse derivative of a substituted polynomial is a uniform K[t]-linear combination of substituted partial Hasse derivatives of order at most the row index. Multilinearity expands its determinant into substituted generalized Wronskians. If all admissible determinants vanished, this nonzero univariate Wronskian would vanish. These steps use project lemmas, not existing mathlib replacements.

## Phase 2 — preliminary checks

**BIG**: the module docstring names this criterion as its main result; it is a named Wronskian theorem and Lemma 1 of the primary source. One-line definition test: **n/a — theorem**. Neither a short caller nor the proof's final contradiction changes this classification.

## Phase 3 — exhaustive literature

[Web receipts](../evidence/Roth.exists_genWronskian_ne_zero/web-receipts.json) preserve exact requests, response hashes/bytes, safe selected URLs and original summaries. Article and search-result bodies are not archived. Query date: 2026-10-27; the five-year window starts 2021-10-27. The protocol's nominal nine-channel wording lists three web forms plus the other named channels; all named rows were actually attempted.

| Channel | Actual query/access | Finding and locator |
|---|---|---|
| General web: specific | `generalized Wronskians linear independence multivariate polynomials order at most i` | Bostan–Dumas, *Wronskians and linear independence*, Theorem 3; pure multiindex derivatives with total order≤s. |
| General web: general | `Bostan Dumas Wronskians linear independence multivariate generalized Wronskian characteristic zero` | Theorem 3 works for multivariate formal power series over arbitrary characteristic-zero fields; polynomials are a specialization. |
| General web: historical aliases | `Roth lemma generalized Wronskian linearly independent polynomials Kronecker substitution` | Roth/Thue–Siegel usage and substitution reduction are standard; Bostan–Dumas §Generalized Wronskians identifies Ostrowski, Dyson and Roth and contrasts substitution/inductive proofs. |
| ChatGPT mathematical MCP | Inventory check | `ask_chatgpt_math` unavailable; no fabricated answer or historical-formulation conversation. |
| Local primary paper | `clean.tex` §Wronskians, `roth:lem1` | Exact polynomial assertion and Kronecker proof; the written source specializes to rational coefficients. [Local excerpt](../evidence/Roth.exists_genWronskian_ne_zero/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab/show Wronskian generalized linear independence`; direct URL | Indexed *Wronskian* gives the ordinary derivative determinant. Direct fetch fails unsupported XHTML; not counted as full direct access. |
| nCatLab | `site:ncatlab.org Wronskian`, targeted retry `site:ncatlab.org/ncatlab "Wronskian"` | Returned nLab pages and hosted expositions, no distinct nCatLab general criterion. |
| Stacks | `site:stacks.math.columbia.edu Wronskian`; retry with quotes; direct search URL | No target result identified. Direct search fetch inaccessible; no assertion that Stacks proves absence. |
| MathOverflow | `site:mathoverflow.net generalized Wronskian multivariate linear independence`; targeted retry | Q487552 (Feb 2025), *Wronskian, linear dependence, and multi-variables*, points to Wolsson 1989. Q436759 (2022), historical multidimensional Wronskian translation, mentions Roth. Direct search URL inaccessible, indexed question text available. |
| Recent arXiv, last five years | `site:arxiv.org generalized Wronskians linear independence multivariate after:2021-10-27`; targeted2022/2023/2024/2025 queries | Actual 2022 Zeitlin2208.08018 G-Wronskians and 2023 Müller–Regensburger2304.05273 fewnomials concern different settings. Etesse2108.02993 is Aug 2021 and explicitly outside the window despite a recent crawl label. No recent result was treated as an exact algebraic replacement. |

Primary external anchor: [Bostan–Dumas Theorem 3](https://arxiv.org/html/1301.6598), §Generalized Wronskians, lines 119–140. Its characteristic-zero field and row-order bound exactly match the mathematical structure here. The stronger formal-series scope is real, but requires a different polynomial/series API, not a single typeclass edit. Its univariate discussion lines 45–47 explicitly explains the positive-characteristic counterexample1, x^p. Supplementary context: [Etesse 2021](https://arxiv.org/abs/2108.02993), [Zeitlin 2022](https://arxiv.org/abs/2208.08018), [Müller–Regensburger 2023](https://arxiv.org/abs/2304.05273), [MO487552](https://mathoverflow.net/questions/487552/wronskian-linear-dependence-and-multi-variables). These sources are not cited as Lean building blocks.

Literature-standard form: arbitrary characteristic-zero field, finitely many series/variables, pure partial differential operators with row-dependent total-order upper bounds; nonvanishing of at least one determinant. Hasse normalization over fields of characteristic zero preserves this meaning. Rational coefficients and positive family size in the local source are already broadened in Lean.

## Phase 4a–b — parameters and generality

| Parameter / hypothesis | Actual use and possible change |
|---|---|
| `K : Type*` | Arbitrary universe-polymorphic coefficient field, already broader than ℚ. |
| `[Field K]` | Needed by current parent `genWronskian` interface and the univariate independence criterion, including elimination/scalar division. A domain/fraction-field route would require new transport API. A failed current-parent elaboration does not refute that mathematical extension. |
| `[CharZero K]` | Essential for this order bound. For1, x^p in characteristic p, row 0 is evaluation and every first derivative in row 1 vanishes (or duplicates row 0); bounded Hasse derivatives do not avoid this obstruction. Allowing unbounded Hasse orders is a different assertion. |
| `σ : Type*`, `[Finite σ]` | Proof chooses an enumeration and a sum of all partial degrees. Each finite polynomial family itself uses finitely many variables, suggesting restriction to the finite union of `vars` and renaming back. Such a bridge is new proof work; direct deletion does not supply an enumeration. The accepted `ExistsGenSupportProbe.arbitrary_variables` establishes this route; the failed direct-deletion probe establishes only the old proof limitation. |
| `l : ℕ`, `Fin l` | No positivity or inhabitedness assumption; order≤μ uses the natural row order. Arbitrary finite column indices can be enumerated, but replacing rows by an unordered finite type loses the bound unless a ranking/bijection is supplied. Parent determinant generality does not by itself generalize the bounded-existence assertion. |
| `φ` | Arbitrary polynomial family; no degree bound in the statement. Finite degrees are used only to choose k. Formal power series would match the strongest standard source but cannot use this same finite-degree Kronecker proof unchanged. |
| `h` | Essential independence premise. Without it, dependence forces zero determinants, as checked separately in the parent law; e.g. a zero member. |
| `D` and bound | Existential pure multiindices and degree≤row are essential output; deleting the bound weakens the theorem and misses what the Separation caller consumes. |

Generality verdict: **STRICTLY NARROWER THAN STANDARD** for the polynomial API after finite-support normalization, with an actual clean theorem proving the identical conclusion for arbitrary σ. The cited power-series theorem explicitly has finitely many variables; it does not itself state the arbitrary-variable result. The broader polynomial formulation is justified by the accepted finite-support proof, rather than attributed verbatim to that source. The direct one-edit proof replay fails at `Fintype.ofFinite`, while the accepted finite-support bridge restricts the family to the finite union of its variables and transports derivatives/determinants back. This is a specific hypothesis deletion with a compiled proof and unchanged parent/result interface, not a conjectural wholesale foundational rewrite. The new bridge is not an existing mathlib replacement. No Field→domain or power-series extension is labeled mechanically compiled. Any future fraction-field or power-series extension is grounded in the displayed mathematical target and explicitly separated from fixed parent interface constraints. Cost does not decide the verdict.

## Phase 4c — modern idiom

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Preambles to typeclasses | Already uses Field, CharZero and Finite. No new ad hoc class is warranted. |
| 2 | Sequences/metrics to filters | No: finite polynomial algebra, no convergence. |
| 3 | Construction to universal property | No new universal construction: D is a finite existential witness with specific derivative bounds. |
| 4 | Closure predicate to bundled substructure | A finite-dimensional subspace/basis formulation is possible, but the caller naturally supplies a `LinearIndependent` family and needs an ordered witness. No demonstrated simplification from bundling. |
| 5 | Field/vector-space to module/ring | A characteristic-zero domain version is a meaningful fraction-field project; current interfaces capture Field. Arbitrary modules and rings with zero divisors do not follow from merely generalizing the parent determinant. |
| 6 | Higher categories | No categorical object or higher-coherence issue. |
| 7 | Concrete index | Fin l is not merely an incidental enumeration: it expresses the rank/order bound≤μ. Arbitrary finite column indexing needs a row ranking; no unconditional unordered-bound replacement proposed. Removing global finiteness of variables via finite supports would improve reuse for infinitely generated polynomial rings. |
| 8 | Concrete-via-abstract diagnostic | No named concrete witness appears in the theorem: φ and K are already arbitrary. Body grep finds0 occurrences of `genWronskian` as an identifier, but it remains inside the private determinant-expansion theorem and the contradictory assumption. This is not evidence that an arbitrary matrix or arbitrary linear-operator theorem has been proved: substitution, Hasse derivative order and polynomial independence are essential. |
| 9 | False-generalization guard | Reject dropping CharZero, replacing pure derivatives with arbitrary maps, forgetting order bounds, or asserting nonzero determinants over arbitrary zero-divisor rings from independence. Domain/finite-support/series proposals preserve the intended criterion only with explicit transport and correct scalar independence; they are not already validated by parent definition generality. |

Modern-idiom verdict: already largely idiomatic finite polynomial/linear-independence statement. A finite-support variable reduction has a concrete benefit for families in arbitrarily generated `MvPolynomial`; a domain version supports integral coefficient rings; a series version serves formal differential algebra. They are distinct extensions with separate proof obligations, not a category-theory rewrite. The YES-but-generalise claim rests on the actually compiled deletion of `[Finite σ]`, not on the speculative domain or power-series benefits.

## Phase 4.5 — infrastructure risk

n/a: theorem. All six definition-specific categories were considered: no new instance diamond, reducibility boundary, noncanonical definition unfolding rule, instance priority, structure universe computation or coercion instance is introduced. Existing Field capture in the parent is an interface dependency, not a new theorem-created diamond.

## Phase 4.6 — proof strategy

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Elements versus subobjects | Uses `LinearIndependent` and the bundled K[t]-submodule of bounded-order derivative operators upstream; already exploits the right linear algebra. A jet-rank formulation would need the same nontrivial derivative spanning argument. |
| 3 | Sequences versus nets | n/a: no limiting process. |
| 4 | Explicit object versus categorical universal property | n/a: no categorical object constructed. |
| 5 | Missing helper API | Finite-family univariate Wronskian criterion; multivariate Hasse API; uniform higher chain-rule expansion; bounded substitution injection; final generalized criterion. Some generic determinant multilinearity is existing mathlib API, but these polynomial bridges are project results. |

Verdict: **MATHLIB-IDIOMATIC** in its reduction strategy. The local proof follows the substitution argument explicitly identified in Bostan–Dumas; the latter also offers a leading-monomial proof for power series. Either is legitimate. No efficiency/cost-based verdict downgrade follows from the number of prerequisites.

## Phase 5 — actual five methods on three forms

[Formal-search receipts](../evidence/Roth.exists_genWronskian_ne_zero/formal-search-raw.json) preserve every Finder, LeanSearch, Loogle and local query/response; [source-search receipts](../evidence/Roth.exists_genWronskian_ne_zero/source-search-raw.json) preserve exact rg commands and complete outputs. Finder's index may differ from the pin. Local search reports `index: unavailable`; its positive source hits prove presence only. Scratch `.lake` hits are excluded from production caller counts and candidate replacements.

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | Finite multivariate polynomial nonzero bounded Hasse Wronskian | Generalized Wronskian independence, admissible multiindex bound | Full-rank jets/partial derivatives of finite-dimensional polynomial space |
| LeanSearch | Same actual current natural-language query | Same actual standard-form query | Same actual jet-rank query |
| Loogle | `"wronskian", LinearIndependent` | `MvPolynomial, LinearIndependent, Exists` | `Matrix.det, LinearIndependent, Exists` |
| rg | `genWronskian`, generalized Wronskian | all pinned `wronskian` occurrences; Hasse derivative declarations | determinant nonvanishing and Jacobian independence declarations |
| Local pattern | `genWronskian` | `wronskian` | `LinearIndependent` |

The most useful pinned gap anchor is **Mathlib/RingTheory/Polynomial/Wronskian.lean:29**, whose TODO explicitly asks for n-tuple Wronskians, beyond the existing pair. The search does not justify claiming an unproved global absence theorem, but locates no existing bounded multiindex existence criterion.

Selected source/native candidate checks:

- `Polynomial.wronskian` and `IsCoprime.wronskian_eq_zero_iff`, `Mathlib/RingTheory/Polynomial/Wronskian.lean`: two univariate polynomials; coprimality plus vanishing derivative criterion. No finite-family multivariate witness with order bounds.
- `Matrix.det_mvPolynomialX_ne_zero`, `Mathlib/LinearAlgebra/Matrix/MvPolynomial.lean:70`: determinant of generic independent matrix-entry variables is nonzero. Specialization can send a nonzero polynomial to zero; it does not ensure admissible derivative-row selection.
- `Algebra.PreSubmersivePresentation.isUnit_jacobian_of_linearIndependent_of_span_eq_top`, `Mathlib/RingTheory/Extension/Presentation/Submersive.lean:167`: assumes the evaluated derivative rows are already independent and span; this is exactly the missing sort of premise and cannot be inferred from scalar independence of φ by a bare call.
- `Algebra.SubmersivePresentation.linearIndependent_aeval_val_pderiv_relation`, same file:651: assumes a submersive presentation; unrelated to arbitrary polynomial-family independence.
- `Polynomial.hasseDeriv`, `Matrix.det`, standard linear-independence transport and multilinear expansion are genuine building blocks. None supplies the bounded-row existence step.

Conclusion: **partial/building-block matches only; no replacement found after all 5×3 methods**. Positive signatures and the actual composition attempt are linked in [verification](../evidence/Roth.exists_genWronskian_ne_zero/verification.json).

## Phase 5.5 — statement shape

Normal forms considered: existence of one nonzero bounded generalized determinant; equivalence between independence and existence; contraposition saying all bounded determinants vanish implies dependence; full rank of an appropriate jet-row family. The direct existential form best supplies the caller's D, bound and nonzero determinant. An iff can package the separately proved easy direction later; it does not delete the substantive existence proof. No existing mathlib canonical finite-family generalized predicate was identified. The nonzero output is the intended normal form; no orthogonal equivalence rewrite violates the RHS convention.

Syntactic attempts: direct `[Finite σ]` deletion; coefficient-domain replay; finite-support restriction/renaming; raw `Matrix.of` determinant in place of `genWronskian`; and exact destructuring of the caller's existential. Their actual native statuses are separately recorded. Arbitrary unordered rows without a rank bound were rejected as a meaning-changing restatement.

Superfluous-argument audit: K/σ/φ/l determine the data; h and CharZero carry essential mathematics; Field and Finite are used by the present proof/interfaces, with possible separate transport generalizations identified above. No global Fintype or DecidableEq parameter survives elaboration; no positivity assumption must be removed. Statement-shape verdict: normal form **OK**; syntactic generality **RESTATE** with arbitrary σ; superfluous arguments **one to drop: `[Finite σ]`**, by the verified support bridge. Overall **RESTATE-BEFORE-SHIP**.

## Phase 6.0 — callers and inline audit

| Caller | Actual use and refactor consequence |
|---|---|
| `Roth/Separation.lean:524`, private `Roth.exists_rat_factors_det_hasseDeriv_aux` | `obtain ⟨D, hD, hG⟩ := exists_genWronskian_ne_zero hψ`; D provides the rows for the separated determinant, hD the≤μ bounds, hG the nonzero multivariate factor. Its full source body and actual replay are preserved; a theorem wrapper alone is not presented as this caller verification. |

Internal use count excluding declaring file: **1**, in **1** external-to-file module; same-file explicit uses: **0**. The target-specific canonical audit checks all 293 declarations in exact tracked order, with 293 unique/present/value entries, retaining the actual private-name constants. Its sole direct consumer agrees with source search. This is direct expression/source evidence, not complete transitive kernel/simp dependency closure. No other production inline rederivation of bounded generalized Wronskian existence was found by the archived patterns. The [accepted full Separation caller replay](../evidence/Roth.exists_genWronskian_ne_zero/exists-gen-wronskian-actual-consumer-executed.lean.txt) uses the stronger theorem with the original existential destructuring and all public helpers unchanged. The single-caller heuristic cannot override the mathematical main-theorem content or fabricate a≤3-call mathlib derivation.

## Phase 6 — composition experiments

The original contradiction proof combines `linearIndependent_kronecker`, `exists_hasseDeriv_kronecker_eq_sum`, the private Wronskian determinant expansion and `wronskian_ne_zero_of_linearIndependent`, with a nontrivial degree bound and finite-sum vanishing proof. These are project lemmas, so even a shorter rearrangement is not a composition from existing mathlib.

Attempt 1: apply generic nonzero determinant of independent variables and specialize. Fails mathematically: a specialization need not preserve nonzero elements; an arbitrary derivative matrix is not generic. Attempt 2: apply a Jacobian invertibility/independence criterion. Its hypotheses demand independence over the polynomial/evaluated algebra and appropriate derivative rows, whereas h only gives coefficient-field independence of the original columns. Establishing the needed row/rank premise is the generalized Wronskian theorem, not normalization. Attempt 3: mathlib-only `exact?` on the exact coefficient-sum realization of Hasse derivatives and determinant, with `#check_failure` guarding the absent project target. The exact native `exact?` attempt failed to close the goal at default limits, without timeout or heartbeat exhaustion. Its raw failure is retained as rejected proof evidence, not treated as an absence theorem or a successful proof.

Conclusion: **NOT-COMPOSABLE** on the actual checked candidates; no≤3 existing-call term or closing simp proof was produced. A failed search is not a proof of absence. Phase6b's special borderline simp heuristic is not invoked without a successful simp composition.

## Phase 7 — verdict and action

**YES-but-generalise-first — MODERN-IDIOM / verified finite-support hypothesis removal**. The concrete missing API is the bounded generalized Hasse-Wronskian nonvanishing criterion for an independent finite polynomial family. The pinned pairwise Wronskian file explicitly TODOs n-tuples; generic determinant and Jacobian laws do not discharge the derivative-row selection/order condition. The verified hypothesis deletion is `[Finite σ]`: each finite polynomial family has finite variable support, so global variable finiteness need not be imposed. This is positive compiled evidence for the generalise gate; neither search absence alone nor the prior parent verdict supplies the verdict. No parent verdict was inherited: parent `genWronskian` was accepted for generalized finite-index/CommRing definition work, not as an existing mathlib criterion; dependence⇒zero was separately borderline. The present direction is substantive and mathematically classical.

Proposed upstream home: **`Mathlib/RingTheory/MvPolynomial/Wronskian.lean`**, matching the accepted parent definition proposal. The finite-family univariate criterion and multivariate Hasse API should precede this leaf; the first-order chain rule remains in its separately assessed algebraic API layer. Keep the bounded theorem indexed by `Fin l`, even if the parent determinant definition accepts arbitrary finite square indices.

Proposed PR title: **`feat(MvPolynomial): nonvanishing generalized Hasse Wronskians`**. Group the theorem with the already accepted YES `Roth.genWronskian` proposal, after the accepted YES multivariate Hasse definitions/rename lemmas; the earlier accepted YES `Roth.derivative_aeval` supports the proof but deserves its own focused chain-rule PR. Accepted verdicts were read from current progress. Do not label the separately borderline dependence⇒zero, higher Kronecker chain expansion or determinant convenience law as accepted YES additions; their mathematical proofs may still be prerequisites to integrate or refactor.

Proposed exact theorem restatement (using the existing parent spelling for clarity):

```lean
theorem exists_genWronskian_ne_zero {K σ : Type*} [Field K] [CharZero K] {l : ℕ}
    {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ Roth.genWronskian D φ ≠ 0
```

The [accepted support snippet](../evidence/Roth.exists_genWronskian_ne_zero/exists-gen-wronskian-support-clean-executed.lean.txt), `ExistsGenSupportProbe.arbitrary_variables`, is the exact executable proof blueprint. It uses the finite-variable theorem on the subtype of `Finset.univ.biUnion (fun ν ↦ (φ ν).vars)`, pulls independence back by `LinearIndependent.of_comp`, maps each D with `Finsupp.mapDomain`, preserves degree using `degree_mapDomain`, and transports the determinant using `hasseDeriv_rename`, `AlgHom.map_det` and injectivity of rename. These are explicit proof obligations, not an asserted definitional bridge.

- [ ] `/generalise Roth.exists_genWronskian_ne_zero`: delete `[Finite σ]` using the verified bridge, retain Field/CharZero and the row-order bound; coordinate the namespace with the parent API.
- [ ] `/cleanup Roth/GenWronskian.lean Roth.exists_genWronskian_ne_zero`: documentation, namespace, import layering and proof preparation; avoid treating project prerequisites as already upstream.
- [ ] Update the sole Separation caller to the stronger theorem using the exact accepted full-body caller replay; arguments and existential destructuring remain the same.
- [ ] Decide separately whether domain/fraction-field or formal-series versions merit further development. No claim that these extensions compiled, and no requirement to redesign them merely to justify the proven variable-support generalization.
- [ ] Reviewer selection: request **Yaël Dillies**, whose scoped recent commit 631b214f7 (2026-09-02) refactors MvPolynomial coefficient infrastructure; **Marcelo Lynch**, August 2026 scoped algebra cleanup commits, is an alternate. This is subject-area selection from actual scoped recent history, not presumed availability. [Scoped reviewer receipt](../evidence/Roth.exists_genWronskian_ne_zero/exists-gen-wronskian-reviewer-git.json).

No production rewrite or upstream publication is performed. If kept local, `Roth/GenWronskian.lean` remains its coherent destination beside its proof prerequisites. This is a positive contribution assessment, not a recommendation to inline the substantial proof into its sole consumer.

## Phase 8 — verification closure

Native acceptance includes exact current original type/axioms, target-specific exact293 audit, successful support proof/caller replay, candidate signatures, and a small characteristic-two derivative obstruction. The last proves only that the first Hasse derivative of X² over ZMod 2 vanishes; the full mathematical counterexample independence claim is supported by the primary source, not falsely presented as a fully formalized countermodel. Two rejected drafts of that small guard are retained separately along with rejected support/interface/search drafts. Standard axioms only: propext, Classical.choice, Quot.sound. Full-file errors/warnings and axiom contamination are checked; fresh info assertions are scoped to each actual `native_region_start_line`. No sorry, unsafe, new axioms, native_decide, or raised limits are accepted. Persistent source archives retain the exact appended snippets and their original execution file/starting line, not full scratch-document snapshots. Run-code raw responses use diagnostics and have no partial field; persistent disk receipts must explicitly report partial=false. [Verification manifest](../evidence/Roth.exists_genWronskian_ne_zero/verification.json) distinguishes these formats and does not accept a historical target marker as a current audit.

The fresh full `lake build` at this completed-file boundary **passed**, exit 0, 2467 jobs, no errors or warnings, 5.60 seconds. [Actual build receipt](../evidence/Roth.exists_genWronskian_ne_zero/gen-wronskian-file-completion-2026-10-27.json), [raw log](../evidence/Roth.exists_genWronskian_ne_zero/gen-wronskian-file-completion-2026-10-27.log). All 17 source/pin hashes and all manifest entries are validated again before freeze. All open upstream API choices are separated from verification status. The portable validator resolves the report's `../evidence/Roth.exists_genWronskian_ne_zero/` links in scratch and integrated layouts; the tracked credential scanner runs before publication.
