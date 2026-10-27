# MvPolynomial.pderiv_hasseDeriv — full mathlibable assessment

**Verdict: YES-add-as-is.** The ordinary partial derivative of the canonical multivariate Hasse derivative is the next Hasse derivative multiplied by the relevant successor coordinate. This is reusable polynomial API in arbitrary characteristic, with a concrete gap between pinned univariate Hasse composition and multivariate partial derivation.

This is canonical declaration 17 of the repository overview. Production sources, toolchain and dependencies remain unchanged. All experimental proofs are scratch evidence. No upstream contribution has been submitted.

## Phase 0 — baseline and identity

The shared baseline is a successful full lake build at commit 99f19fda4b3cbee38fc0d31af76075834f5cc265: 2467 jobs, exit 0, no reported warnings/errors. This assessment freshly checks all 17 production-source and pin hashes against that baseline; all match. Reusing that build is justified by unchanged inputs; it is not described as a fresh full rebuild.

The public theorem resolves at Roth/HasseDeriv.lean:200. The whole 294-line module was read, together with both executable caller contexts. Its module develops multivariate binomial-weighted Hasse derivatives, including coefficient, composition, substitution and factorial-scaling interfaces. The target has no sorry.

The actual elaborated type and target axioms were requested in the accepted native disk bundle:

~~~lean
∀ {σ R : Type*} [CommSemiring R] (j : σ) (d : σ →₀ ℕ)
  (P : MvPolynomial σ R),
  pderiv j (hasseDeriv d P) =
    ((d j + 1 : ℕ) : R) • hasseDeriv (d + Finsupp.single j 1) P
~~~

Only standard foundational axioms propext, Classical.choice and Quot.sound occur. Independent replay, statement-shape experiments, caller fragments and the isolated raw construction also pass with standard axioms and no errors/warnings. See verification.json for exact accepted source/receipt pairs.

## Phase 1 — mathematical content

Let R be a commutative semiring and let P be a polynomial in an arbitrary family of variables. For a finitely supported multi-index d, applying ordinary differentiation in variable j after the Hasse operator Δ_d gives (d_j + 1) times Δ_(d+e_j). The scalar is a natural-number cast, so the theorem does not divide by a factorial and remains meaningful in positive characteristic.

Parameters: σ is the variable type, R the coefficient semiring, j a distinguished variable, d the derivative order, and P the input polynomial. There are no proposition hypotheses, no finiteness requirement on σ and no characteristic restriction.

The proof compares coefficients. The pinned ordinary-derivative coefficient formula contributes e_j+1; the Hasse coefficient formula contributes a product of binomial coefficients. A finite-product binomial successor identity moves their product to (d_j+1) times the shifted Hasse coefficient, and associativity closes the equality. The private scalar lemma is a substantive prerequisite, not an existing multivariate mathlib theorem.

## Phase 2 — preliminary checks

**BIG:** the theorem is explicitly listed under the module's Main results and supplies the recurrence used in the generalized Wronskian construction. Its proof is short, but the skill's classification uses its mathematical/API role. Literature width was exhaustive regardless.

One-line definition check: **n/a, theorem**. This is neither an alias nor a definitional equality; it receives a fresh full assessment. Short proof length does not itself establish a 1–3 existing-mathlib-call replacement.

## Phase 3 — exhaustive literature assessment

Exact web requests, response hashes/byte counts and access limitations are in web-receipts.json; concise original source summaries are in web-sources.json. No full article or search-result bodies are archived.

| Channel | Actual query/access | Result and relevance |
|---|---|---|
| Specific web | "Hasse derivative" "partial" "composition" | Primary literature on iterativity and explicit multivariate Hasse formulas surfaced. |
| General web | "Hasse Schmidt" "iterative" "derivative" first | Hoffmann–Kowalski distinguishes the higher Leibniz law from additive iterativity; the first ordinary derivative is a coordinate of the latter. |
| Alias web | "divided derivatives" "multivariate" formula | Divided-derivative and multivariate formulations checked; ordinary iterates and Hasse operations must not be conflated in positive characteristic. |
| Optional mathematical second opinion | ask_chatgpt_math | Unavailable; skipped under the user's explicit exception. Other channels were not reduced. |
| Local references | clean.tex search for derivatives, Δ, partial and FACT; lines 120–150 and 283–317 read | Lines 305–306 explicitly give ∂_j Δ_d=(d_j+1)Δ_(d+e_j) on monomials. The recurrence enters the simultaneous higher derivative expansion. |
| nLab | Hasse-Schmidt derivative; Hasse-Schmidt derivation | Search response supplies the canonical binomial-weighted definition over commutative rigs, including several variables. Direct opens failed with unsupported XHTML400. Search-accessible content is distinguished from a successful direct fetch. |
| nCatLab / categorical view | Same host's derivation and derivative pages, graded bimonoid context | Related abstraction was actually checked; no separate ready-made categorical replacement of this polynomial recurrence was obtained. Direct page fetches share the XHTML limitation. |
| Stacks Project | site:stacks.math.columbia.edu "Hasse" "derivation"; "higher derivation"; "Hasse-Schmidt" | Actual domain searches returned no useful exact target statement. This is a limited search outcome, not a proof the Stacks Project lacks related material. |
| MathOverflow | site:mathoverflow.net "Hasse" "iterative"; "Hasse-Schmidt" "iterative" | The jets listings identify the 2023 question on higher derivations versus differential operators; this is context, not a proved successor identity. |
| Recent arXiv | Hasse derivatives 2024/2025; Hasse Schmidt 2024; abs/2409.19093 opened | Bravo–Tirado Hernández, submitted September 2024, studies integrability of derivations. Only its abstract was inspected; no claim it proves the exact polynomial identity. |

Additional primary sources examined:
- [Hoffmann–Kowalski, Integrating Hasse-Schmidt derivations](https://arxiv.org/html/1212.5788), Definitions 2.1–2.2 and Remark 2.7. Additive iterativity is extra structure; arbitrary higher Leibniz systems need not satisfy it. Characteristic-zero factorial descriptions do not license division over arbitrary semirings.
- [Non-Archimedean meromorphic maps](https://www.impan.pl/shop/publication/transaction/download/product/92270), search-accessible §2.3, p.169: explicit multi-index binomial definition and equality of order-one Hasse and ordinary partial derivatives. A direct PDF fetch failed with cache miss; no successful full PDF reading is claimed.
- [Finiteness of Leaps in the sense of Hasse-Schmidt of reduced rings](https://arxiv.org/abs/2409.19093), abstract: current higher-derivation work supports the importance of retaining arbitrary-characteristic formulations, without supplying this exact Lean statement.

**Summary:** this is the coordinate-successor case of additive Hasse iterativity, also called a divided-derivative recurrence. The local source states it explicitly; external primary formulas agree with its coefficient interpretation. Literature varies from fields and characteristic-zero normalization to commutative rigs and iterative higher-derivation systems. The canonical polynomial theorem already uses arbitrary variable types and commutative semirings. Replacing its operators by arbitrary HS operators without an iterativity premise would change its content.

## Phase 4a–4b — generality and all arguments

| Argument | Role / essential use | Weaker form considered and result |
|---|---|---|
| σ : Type* | Arbitrary variable set, independent universe | Already arbitrary; Finsupp orders ensure finite support even for infinite σ. No Fintype/Finite/Unique/DecidableEq assumption to remove. |
| R : Type* | Arbitrary coefficients | Already arbitrary and universe polymorphic. |
| CommSemiring R | Pinned MvPolynomial, R-linear Hasse operator and bundled pderiv interface | A literal Semiring-only MvPolynomial expression is rejected by #check_failure in the successful isolated probe. This is an interface obstruction, not a proof no alternative noncommutative representation is possible. |
| j : σ | Chooses the partial derivative and successor coordinate | Needed in both operator and scalar/order; cannot erase it. |
| d : σ →₀ ℕ | Arbitrary finite derivative multi-order | No positivity, degree bound or disjointness premise. Nat exponents are structural polynomial data; a group-indexed family would need a different definition. |
| P : MvPolynomial σ R | Arbitrary input | Needed pointwise; equivalent bundled equality tested instead of falsely calling P unused. |

The successor coefficient in positive characteristic may vanish; no cancellation of d_j+1 is used. The theorem needs neither an integral domain nor a field, characteristic zero, nonzero polynomial, or invertible factorials.

**Generality verdict: MAXIMALLY GENERAL for the current canonical polynomial/pderiv interface.** The first-order factor cannot simply be removed: the accepted Unit/Nat/X² counterexample distinguishes LHS 2 from RHS 1. The isolated construction verifies the full proof independently of project theorem premises.

## Phase 4c — all nine modern-idiom rows

| # | Question | Assessment and downstream implication |
|---|---|---|
| 1 | Typeclass preambles | No new instance: semiring assumptions are already typeclasses; no bundled hypothesis to replace. |
| 2 | Filters/nets | No: finite algebraic identity, no topology or limit. |
| 3 | Universal property | A freely generated polynomial algebra admits generic operator descriptions, but the coefficient model gives a direct finite proof; no established universal-property replacement was found. |
| 4 | Bundled substructures | Linear operators are already bundled. An equivalent composition equality was compiled and is useful for operator rewriting, but does not replace the pointwise form used by callers. |
| 5 | Hierarchy weakening | Already CommSemiring, below ring/domain/field. The exact parent-interface attempt fails as recorded above. |
| 6 | Higher categories | No: no categorical coherence statement or verified downstream improvement. |
| 7 | General index | σ already arbitrary. Replacing natural exponents by arbitrary monoids changes binomial coefficients and subtraction, so no mechanical index weakening is claimed. |
| 8 | Concrete-via-abstract diagnostic | YES, literally fires. The first rw line contains two coeff_hasseDeriv occurrences; subsequent proof lines contain zero hasseDeriv/pderiv identifiers. The accepted generic weighted recurrence below transfers the coefficient argument. |
| 9 | False-generalization guard | The generic coefficient premises must include the weight successor identity. Removing that condition, forgetting additive iterativity, or dropping d_j+1 is unjustified; the last fails on X² over Nat. |

The actual compiled Q8 proposal PDerivWeightedAssessment.weighted replaces Δ by an arbitrary family L of R-linear polynomial operators with coefficient formula
coeff(L_d P,e)=w(d,e+d) coeff(P,e+d), and assumes
w(d,e+e_j+d)(e_j+1)=(d_j+1)w(d+e_j,e+e_j+d).
It then proves ∂_j(L_d P)=(d_j+1)•L_(d+e_j)P by coefficient comparison. The complete Lean statement and proof are in disk-executed.lean.txt.

This is a genuine successful abstract proof experiment, not an existing mathlib replacement or an assumption-free weakening. Its premise requires the scalar recurrence whose verification is the content here. It could organize multiple weighted-shift constructions, but no additional pinned consumer or improved existing API application was established. Consequently **no material public modern-idiom replacement is selected**: retain the standard polynomial law, and keep the generic criterion as documented supporting evidence. This conclusion is based on concrete downstream utility, not the cost of abstraction.

## Phase 4.5 — infrastructure risk

**n/a: theorem.** The six checks are individually inapplicable: no new typeclass instance/diamond; no reducibility attribute; no new definition to unfold; no instance priority; no data construction forcing new universe equalities; no coercion instance. Existing operator coercions are exercised by pointwise, bundled and iterative caller probes. The theorem does not install a new instance or definitional equality.

## Phase 4.6 — proof strategy

| # | Question | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topological proof. |
| 2 | Elements versus subobject inclusions | No ideal/submodule inclusion is the content. LinearMap.ext gives the bundled equivalent; coefficient ext is appropriate for this operator identity. |
| 3 | Sequences versus nets | n/a, finite polynomial algebra. |
| 4 | Explicit categorical construction versus universal property | No categorical object is being constructed. |
| 5 | Missing helpers that should exist | YES: canonical multivariate Hasse coefficient and composition API. They belong with the parent construction; the private Nat product successor helper can stay internal. |

**MATHLIB-IDIOMATIC** for the coefficient-based development. A future alternative is first prove Δ_(e_j)=∂_j, then specialize multivariate iterativity. The order-zero identity and bundled equality were actually checked; this alternative depends on new multivariate API, not a short pinned-mathlib replacement. The current proof avoids adding that auxiliary result merely to shorten this theorem. No proof refactor is required by the evidence before the upstream cleanup pass.

## Phase 5 — actual five-method searches

All three query forms were executed for Finder, LeanSearch, Loogle and local name search. CLI receipts cover current full name, literature analogues and abstract divided-power/derivation vocabulary.

| Method | Current form | Literature-standard form | Abstract form / interpretation |
|---|---|---|---|
| Lean-Finder | Ordinary partial after multivariate Hasse | Iterative HS first derivative recurrence | Weighted/divided operator coefficient identity; returns univariate and LaurentSeries analogues plus unrelated divided powers |
| Loogle | MvPolynomial.pderiv | Polynomial.hasseDeriv, Polynomial.derivative | DividedPowers.mul_dpow |
| LeanSearch | Partial of multivariate Hasse | Iterative HS coordinate law | Coefficient/derivation/divided-power interface; returns pderiv, coeff-like basics, derivation laws, not the raw multivariate result |
| rg pinned source | Untruncated full-name pderiv_hasseDeriv search: exit 1, empty output | coeff_pderiv and Polynomial.hasseDeriv_one/comp/factorial_smul | DividedPowers and Derivation files inspected; unrelated ideal divided powers are not Hasse polynomial endomorphisms |
| lean_local_search | pderiv_hasseDeriv finds project source | hasseDeriv_comp finds univariate and LaurentSeries | mul_dpow gives source fallback; index unavailable in all three calls |

A local index marked unavailable is not absence evidence. External services use their own snapshots (Finder default v4.28.0); pinned source plus successful Lean checks control positive claims.

Pinned candidates were read and actually #checked:
- MvPolynomial.coeff_pderiv, Mathlib/Algebra/MvPolynomial/PDeriv.lean:121: coefficient of ordinary partial differentiation.
- Polynomial.hasseDeriv_one', Mathlib/Algebra/Polynomial/HasseDeriv.lean:95: first univariate Hasse derivative is ordinary derivative.
- Polynomial.hasseDeriv_comp, same file:154: composition with the binomial scalar.
- Polynomial.factorial_smul_hasseDeriv, same file:133: factorial-scaled Hasse derivative equals the ordinary iterate.

The accepted isolated snippet actually derives derivative(hasseDeriv n p)=(n+1)•hasseDeriv(n+1)p from the univariate composition theorem, first-order theorem and choose-one simplification. That is a verified analogue. An arbitrary σ-variable polynomial is not a univariate polynomial over R; transporting it as a polynomial over other-variable coefficients requires additional equivalences and Hasse transport proofs. Neither a same-name match nor this analogue is an immediate replacement of the multi-index law.

The successful mathlib-only snippet guards failure of the project parent operator, coefficient theorem, composition theorem and target name, then constructs a raw delta via Finsupp.lsum, proves its coefficient formula, finite-product choose cocycle, successor factor and partial-derivative identity. These are fresh substantive proofs. There was no negative exact? absence proof; the only exact? is a positive tactic control. Search results and name-failure guards are not represented as a universal semantic absence theorem.

## Phase 5.5 — statement shape

1. **Normal form:** the RHS is a single derivative with incremented multi-order and the necessary scalar. Equivalent forms include a bundled linear-map composition equality, an all-input function equality, or an equality with ∂_j replaced by Δ_(e_j). The bundled form and order-zero identification were actually compiled. The pointwise direction is the natural rewrite form for both real callers; it agrees with the normalization convention of pinned univariate Hasse composition.
2. **Syntactic generality:** tried bundled .toLinearMap.comp and d=0 specialization. Keep explicit j,d,P for rw/simp usage; bundled form is an optional companion, not an independently stronger theorem.
3. **Superfluous arguments:** all six rows of Phase 4 account for every type/instance/data argument; none can be dropped within the stated interface. No explicit proposition assumptions exist.

**SHIP-AS-STATED.** No new simp attribute is recommended automatically: the operator-changing rule is used explicitly at source consumers.

## Phase 6 — callers, inline audit and composition

There are **two executable invocations in two files**, excluding the target itself and module documentation. Of these, one invocation is outside the declaring file:

| Caller | Use | Actual validation scope |
|---|---|---|
| Roth/HasseDeriv.lean:291, factorial_smul_hasseDeriv_single | Succ induction changes ∂_j Δ_(n e_j) into (n+1)•Δ_((n+1)e_j) | Complete factorial theorem induction replay accepted, replacing the target by scratch replay. |
| Roth/GenWronskian.lean:159, private derivative_kronHasse_aux | simp after polynomial chain rule extracts scalar into the univariate coefficient polynomial | Scoped aeval scalar-extraction fragment accepted over general CommSemiring; not a claimed full reconstruction of the chain-rule sum/private caller. |

No separate inline re-derivation of the same target was found in the production source search. The downstream derivative_mem_kronSpan invocation of derivative_kronHasse_aux is indirect, not counted as an additional direct invocation. Source-level searches do not measure opaque kernel or implicit simp dependency closure.

Composition attempts:
1. **Pinned univariate first-order plus comp:** succeeds for Polynomial R, as actually compiled. Does not directly specialize to arbitrary multivariate σ; missing transport/coefficient Hasse API remains.
2. **coeff_pderiv + generic coefficient ext:** reduces the task to new binomial-weight coefficients and their successor identity. Actual isolated proof succeeds only after proving those new facts; this is not ≤3 existing-mathlib calls.
3. **Generic weighted criterion or new multivariate composition:** useful organization, but the premises/new parent lemmas carry the missing multivariate mathematical content. They cannot be counted as existing pinned-mathlib building blocks.

**NOT-COMPOSABLE in the skill's existing-mathlib ≤3-call sense.** No closing bare simp-from-existing-definitions proof was established. A multi-step raw construction/induction/product-cocycle proof supports the assessment, without claiming exhaustive impossibility of every imaginable shorter proof.

## Phase 7 — verdict and actionable upstream plan

**YES-add-as-is.**

The precise API gap is compatibility of canonical multi-index Hasse endomorphisms with ordinary partial derivation over commutative semirings. Pinned mathlib supplies the ordinary pderiv coefficient formula and a univariate Hasse composition theorem, but not the operator construction/transport needed to use their univariate analogue for arbitrary multivariate polynomials. The raw proof verifies that gap independently of project premises.

This law supplies two concrete kinds of existing API composition: Derivation.map_smul and Function.iterate_succ_apply' give the factorial iteration theorem, while AlgHom.map_smul and Polynomial.smul_eq_C_mul carry derivative coefficients through substitution into K[X]. These consumers justify a named polynomial interface despite the short coefficient proof and just one external-to-file invocation. The weight criterion is useful diagnostic evidence but does not eliminate the standard canonical API.

- Proposed location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean.
- Proposed PR title: feat(Algebra/MvPolynomial/HasseDeriv): relate partial and Hasse derivatives.
- Group with already accepted YES declarations MvPolynomial.hasseDeriv, MvPolynomial.coeff_hasseDeriv, MvPolynomial.hasseDeriv_map, MvPolynomial.hasseDeriv_rename, and MvPolynomial.hasseDeriv_hasseDeriv. The same module should provide construction, coefficient computation, naturality, iteration and ordinary-derivative compatibility together.
- Retain the scalar product successor lemma privately unless independent consumers justify a public combinatorial API.
- Alternative destination if upstream packaging is deferred: the existing Roth/HasseDeriv.lean reusable local operator layer, rather than Archive/ or a Roth-only theorem namespace.

Pre-PR checklist:

- [ ] /generalise MvPolynomial.pderiv_hasseDeriv — confirm the pinned semiring interface floor and no additional verified weakening.
- [ ] /cleanup Roth/HasseDeriv.lean MvPolynomial.pderiv_hasseDeriv — full style/proof/import checks in the proposed upstream module.
- [ ] Select a reviewer from relevant recent commits: reviewer-commits.json records Yaël Dillies (MvPolynomial coefficient refactor #41427), Moritz Firsching (univariate Hasse map #42428) and other actual recent contributors. Dillies and Firsching are evidence-based candidates, not promises of review.
- [ ] Run the eventual upstream module and downstream build/lint checks against its target mathlib revision; this read-only assessment did not create or submit that PR.

No user input or unresolved proof obligation is required to complete this assessment.

## Phase 8 — evidence and limits

verification.json enumerates accepted exact Lean sources and complete native receipts. input-manifest.json plus source-hashes.json retain the fresh 17-input baseline comparison; source-module.lean.txt and caller excerpts preserve the read source; five-method receipts and web-receipts.json/web-sources.json make searches auditable. Q8's count is recorded in q8-diagnostic.json. Portable validate.py checks current artifact hashes, phases, successful nonpartial diagnostics, standard axioms and source/pin identity.

The historical rejected univariate simp attempt is preserved separately; it is not accepted proof evidence. No proof uses sorry, new axioms, unsafe/native_decide or raised heartbeat limits. Executed source archives use .lean.txt; actual native execution paths remain in receipts.

Limitations: optional ask_chatgpt_math absent; local symbol index unavailable; direct nLab/nCatLab XHTML fetches and the alternate primary PDF fetch failed; recent arXiv evidence is abstract-only; GenWronskian validation is the scoped substitution fragment, not a fresh complete private caller build; no downstream repository or GitHub PR was searched as an implicit consumer. These are explicit scope limits, not unfinished mandatory assessments.
