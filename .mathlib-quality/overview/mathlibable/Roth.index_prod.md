# Roth.index_prod

**Verdict: BORDERLINE-needs-human.** Mathlib already has the natural-weight power-series finite-product law, independently verified here. The parent polynomial index was re-aimed at projected `AddMonoidAlgebra.infDegree`, and the analogous arbitrary-real, noninjective-weight polynomial product equality was not established by that hit. The upstream choice is a broader polynomial initial-form/order API or local transport of the existing natural-series law. This is a mathematical interface question, not a proof-cost judgment. Independently, positivity of the denominators is unnecessary: the exact hr-free result, its empty-product base and the full determinant caller were verified.

## Phase 0 — baseline

All17 source/pin hashes freshly match the shared successful2467-job build, exit0 with no reported errors/warnings: [fresh inputs](../evidence/Roth.index_prod/inputs.json), [manifest](../evidence/Roth.index_prod/input-manifest.json), [baseline](../evidence/Roth.index_prod/baseline-build.txt). Canonical145 resolves at Roth/Index.lean:175. The complete Index module and Theta caller context were read. No production/Git/progress changes were made.

[Original native receipt](../evidence/Roth.index_prod/index-prod-original-audit-receipt.json) contains the type, complete target kernel print and standard axioms. Unlike the historical144 message retained in the persistent document, the145 target print has no elision. [Fresh canonical audit](../evidence/Roth.index_prod/index-prod-audit-executed.lean.txt) checks exact tracked order of293 names, including private names,293 unique/present/values, and one direct kernel consumer. Required messages are scoped to the fresh145 region; full-file error/warning checks still apply.

## Phase 1 — comprehend

For a finite family of nonzero real multivariate polynomials, the minimum reciprocal-weighted exponent in the Taylor expansion of their product at a common point equals the sum of the individual minima. The proof inducts on the finite set: the empty product is1 with index0; the insertion step applies binary additivity to a nonzero factor and a nonzero remaining product.

Full native type:
```lean
Roth.index_prod.{u_1, u_2} {σ : Type u_1} [Fintype σ] {ι : Type u_2}
    (s : Finset ι) {f : ι → MvPolynomial σ ℝ}
    (hf : ∀ i ∈ s, f i ≠ 0) (α : σ → ℝ) {r : σ → ℕ}
    (hr : ∀ (j : σ), 0 < r j) :
    Roth.index (∏ i ∈ s, f i) α r = ∑ i ∈ s, Roth.index (f i) α r
```

σ/Fintype determines the finite variable interface; ι indexes an arbitrary finite family s; f supplies factors; hf excludes the default-zero obstruction; α is the common Taylor center; r supplies reciprocal natural denominators; hr is used by the original binary law and original index-one base. Direct project proof dependencies are `Roth.index`, `Roth.index_mul`, `Roth.index_eq_zero_iff`; no hidden project inference is counted as a mathlib primitive.

## Phase 2 — preliminary checks

BIG because index_prod is explicitly listed among the Index module's main results. The definition-only one-line test and its three exemptions are n/a: this is a theorem. Its proof is a finite induction, and its natural-order core already exists.

## Phase 3 — exhaustive literature

All named channels were actually queried, including three distinct general-web forms. Metadata records exact requests, returned-response SHA256/bytes/status and titles/URLs/locators, plus concise original summaries; no full returned web bodies are persisted. Returned locator query strings were removed. One tool response contained an unpaired surrogate; its recorded UTF8-surrogatepass hash preserves that fact. [Literature summary](../evidence/Roth.index_prod/literature-summary.json).

| Channel | Actual query and finding |
|---|---|
| Specific web | “Roth polynomial index finite product sum indices weighted derivatives”; Roth ICM1958 p206 defines the weighted derivative minimum. [Receipt](../evidence/Roth.index_prod/web-specific.json). |
| General web | “weighted order product polynomials initial forms arbitrary real weights integral domain”; initial forms and real weight vectors, including Sturmfels's primary monograph. [Receipt](../evidence/Roth.index_prod/web-general.json). |
| Alias web | “monomial valuation product initial form weighted degree polynomial”; weighted degree and initial forms are related but largest-degree orientation differs. [Receipt](../evidence/Roth.index_prod/web-alias.json). |
| ChatGPT math | n/a: ask_chatgpt_math unavailable; no substitute invocation claimed. |
| Local manuscript | Actual clean.tex search; lines530–558 define positive-real denominator index with infinity at zero; Lemma4-1 lines589–616 proves binary product equality via lowest homogeneous pieces. Its finite iteration is used in the determinant argument. [Exact excerpt](../evidence/Roth.index_prod/clean-excerpt.tex.txt), [search](../evidence/Roth.index_prod/local-literature-search.json). |
| nLab | `site:ncatlab.org/nlab valuation multiplicative polynomial order`; valuation-ring/group context. Direct XHTML open unsupported, search locator available. [Receipt](../evidence/Roth.index_prod/web-nlab.json). |
| nCatLab | `site:ncatlab.org/ncatlab weighted polynomial valuation`; actual namespace-targeted query returned nLab/out-of-namespace pages, not an exact in-namespace hit. [Receipt](../evidence/Roth.index_prod/web-ncatlab.json). |
| Stacks | `site:stacks.math.columbia.edu valuation order product polynomial`; nearby valuation-ring and power-series material. Opened tag00I8 Section10.50 for context, not an exact weighted-product law. [Receipt](../evidence/Roth.index_prod/web-stacks.json). |
| MathOverflow | `site:mathoverflow.net weighted order polynomial product valuation`; Q476147 discusses real weights, tied weights and refinements to monomial orders. [Receipt](../evidence/Roth.index_prod/web-mathoverflow.json). |
| Recent arXiv | Initial broad year query returned mostly unrelated data-valuation work. Refined `site:arxiv.org "initial forms" "weights" "2023" polynomial` found Bossinger et al., arXiv2309.10761, submitted19Sep2023, within five years. Opened abstract gives valuation/initial-degeneration context, not this exact normalized formula. [Initial](../evidence/Roth.index_prod/web-arxiv.json), [retry](../evidence/Roth.index_prod/web-arxiv-retry.json). |

Primary sources: [Roth's ICM1958 proceedings p206](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [Sturmfels, Gröbner Bases and Convex Polytopes](https://math.berkeley.edu/~bernd/GBCP.pdf), [Bossinger et al. abstract](https://arxiv.org/abs/2309.10761). [Actual primary opens](../evidence/Roth.index_prod/web-primary-open.json) preserve locators and honest nLab access failure. Standard form is minimum additive monomial weight on polynomial support over a domain, with infinity at zero; lowest homogeneous pieces multiply nontrivially. Real weight vectors permit ties. Reversing weights exchanges maximum/minimum conventions. Natural-weight power-series order is another standard form, but does not uniformly encode arbitrary real polynomial weights by one common denominator.

## Phase 4a — parameters and generality

| Parameter/hypothesis | Assessment |
|---|---|
| σ : Type* | Universe polymorphic already. Expanded natural law allows arbitrary σ. |
| Fintype σ | Fixed parent weight/index and denominator-product interface. Removing it while preserving unchanged parent syntax is not claimed. |
| ι : Type* | Arbitrary, no Fintype/DecidableEq requirement; only s is finite. Already appropriate. |
| s : Finset ι | Finite product is the intended law; no ordering/duplicate factors needed. Empty set is supported. Infinite products require different convergence/definition assumptions. |
| f : ι → MvPolynomial σ ℝ | No unnecessary support/degree restriction. ℝ fixed by parent; expanded polynomial law works over CommSemiring, NoZeroDivisors, Nontrivial. |
| hf | Necessary uniformly for real default0. The compiled Bool family {0,X} at center0 and r=1 gives product index0 and sum1. Not needed in infinity-valued series form. |
| α | Arbitrary common center. Existing law applies to all translated series, but Taylor compatibility must be transported. |
| r : σ → ℕ | Reciprocal natural denominators are a special case of manuscript positive real denominators. Expanded natural series weights are direct additive weights. |
| hr | Removable in exact conclusion. Compiled induction uses144's proved all-r multiplication and direct index-one simplification. |
| ℝ-valued index | Projection/default-zero differs from infinity-valued order; retain hf for this representation. |

## Phase 4b — mechanically verified weakening

The exact conclusion compiles after deleting hr. [Target source](../evidence/Roth.index_prod/index-prod-target-clean-executed.lean.txt), [native success](../evidence/Roth.index_prod/index-prod-target-clean-receipt.json). Base `IndexProd145.one` proves index1=0 for every r by `simp [index, weight]`, including zero weights; induction uses `IndexMul144.replacement`. `nonzeroGuard` verifies the hf obstruction. Initial target run was rejected for an unused `taylor_X` simp argument; final accepted source removes it.

The earlier all-r binary law is an explicitly cited proved prerequisite, not an existing mathlib replacement. It clears denominators with D=∏max1(rᵢ)>0 and wⱼ=D/rⱼ, using D/0=0. [Accepted144 proof](../evidence/Roth.index_prod/index-mul-target-clean-executed.lean.txt), [receipt](../evidence/Roth.index_prod/index-mul-target-clean-receipt.json). Its earlier133 projected-infDegree bridge and143 scaled-order proofs are preserved as dependency evidence. None is falsely counted as a fresh145 proof or a preexisting library call.

Expanded natural-weight laws compile over arbitrary σ and coefficient CommSemiring/NoZeroDivisors/Nontrivial, including zero factors. [Isolated mathlib source](../evidence/Roth.index_prod/index-prod-mathlib-final-executed.lean.txt), [receipt](../evidence/Roth.index_prod/index-prod-mathlib-final-receipt.json). The arbitrary-real polynomial infDegree product equality is **not a compiled weakening**: it is a separate proposed upstream interface, involving a parent representation change. No generalise-first verdict is inferred merely from that proposal.

## Phase 4c — all nine modern-idiom rows

| # | Diagnostic | Result and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled predicates | Use CommSemiring/NoZeroDivisors/Nontrivial in expanded law; hf remains meaningful for default-zero index. No custom domain predicate needed. |
| 2 | Filters instead of metric/sequences | n/a, finite algebraic identity. |
| 3 | Universal-property replacement | n/a, no constructed object; existing coercion ring hom transports products. |
| 4 | Bundled substructures | No set-with-closure predicate here. A valuation-like bundle for real additive order would organize finite products, but requires an actual parent API. |
| 5 | Weaken field hierarchy | Yes in expanded natural law: verified CommSemiring/NoZeroDivisors/Nontrivial; no subtraction or characteristic-zero argument required. ℝ remains fixed in original index. |
| 6 | Higher categories | n/a, no categorical content. |
| 7 | General additive ordered target | Polynomial finite support supports broader real/additive weights; generic infDegree handles minima. Product equality at this generality not established. Natural ENat series law is existing, distinct scope. |
| 8 | Concrete-via-abstract | Adversarial check: finite induction only needs index1=0, nonzero-product closure and binary additivity. Real analytic properties are absent from this induction. Its algebraic core has an existing natural-series abstract theorem; reciprocal normalization and finite projection remain genuine separate proofs. |
| 9 | False-generalization guard | Do not equate default0 with infinity, min with max, polynomial finite support with unrestricted real-weight series, or arbitrary real weights with natural weights. No injectivity assumption on weight is valid: equal-weight terms can tie. |

Conclusion: genuine broader polynomial API design question, not expense-based downgrading. Arbitrary-real finite-product equality should accompany the analogous binary law if that scope is chosen.

## Phase 4.5 — six infrastructure risks

All six rows are justified n/a for a theorem: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism construction issue, coercion ambiguity. No new instance/def/coercion is introduced. The expanded proof uses the existing polynomial-to-series ring hom explicitly. Parent default-zero conventions are a mathematical-interface issue, not a new defeq risk.

## Phase 4.6 — all proof-strategy rows

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ vs filters | n/a, algebraic finite identity. |
| 2 | Element arguments vs ideal/submodule inclusions | No ideal/submodule structure would clarify this finite multiplicative law. A bundled additive valuation could derive finite products from map_prod once the correct parent exists. |
| 3 | Sequences vs nets | n/a, no convergence. |
| 4 | Construction vs universal property | n/a, no object construction. |
| 5 | Missing reusable helpers | Index-one all-r base compiled; existing series finite-product theorem eliminates induction there. Broader polynomial infDegree/initial-piece product law remains a possible upstream helper, not an absence theorem. |

Current finite induction is idiomatic; replacing it with the series theorem entails parent normalization. No helper-cost rationale drives the verdict.

## Phase 5 — all five actual search methods

[Full formal search requests/results](../evidence/Roth.index_prod/formal-search.json) records Finder, Loogle, LeanSearch and local-name searches on current, literature and abstract forms; source rg supplies the fifth method. All12 calls returned successfully. Local reports index unavailable even when fallback hits exist: an empty result is not a proof of absence. Remote index revisions may differ; positive conclusions rely on pinned source and native checks.

| Form | Finder | Loogle | LeanSearch | local | rg |
|---|---|---|---|---|---|
| Current finite index product | degreeOf_prod_eq and weightedOrder_prod | weightedOrder with Finset.prod finds lower/equal laws | weightedOrder_prod | weightedOrder_prod | [current](../evidence/Roth.index_prod/rg-current.json) |
| Literature lowest-weight product | weightedOrder_prod and homogeneous products | IsWeightedHomogeneous.prod | component application/degree APIs | infDegree_prod empty, index unavailable | [literature](../evidence/Roth.index_prod/rg-literature.json) |
| Abstract infDegree finite product | le_infDegree_mul only inequality | infDegree/prod empty | infDegree and adjacent algebra | infDegree fallback names | [abstract](../evidence/Roth.index_prod/rg-abstract.json) |

Pinned positive exact law: `MvPowerSeries.weightedOrder_prod`, Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean:176. Expanded theorem proof is exactly `MvPowerSeries.weightedOrder_prod w f s`; polynomial transport uses `coeToMvPowerSeries.ringHom`, `map_prod`, that law and final definitional `rfl`. It is not an exact old-form one-call proof. `weightedOrder_one` needs Nontrivial: the empty product prevents dropping this in arbitrary semirings. `order_prod` is its unweighted specialization. [Pinned source](../evidence/Roth.index_prod/NoZeroDivisors.lean.txt).

`MvPolynomial.IsWeightedHomogeneous.prod` gives homogeneous closure, not that a selected extremal component of a product equals the product of extrema. [Pinned homogeneous file](../evidence/Roth.index_prod/WeightedHomogeneous.lean.txt). Its fresh145 isolated signature confirms arbitrary AddCommMonoid weight target M and CommSemiring coefficients: [signature source](../evidence/Roth.index_prod/index-prod-generic-api-executed.lean.txt), [clean receipt](../evidence/Roth.index_prod/index-prod-generic-api-receipt.json). Earlier144 isolated component/decomposition signature evidence is preserved with honest prerequisite status; no fresh arbitrary-real extremal product proof is claimed. `AddMonoidAlgebra.le_infDegree_mul` is a lower bound; `supDegree_mul` has an injective-degree hypothesis that arbitrary weights need not satisfy, and concerns the opposite extremum. [Degree source](../evidence/Roth.index_prod/Degree.lean.txt).

The initial isolated attempt was rejected: `MvPolynomial.coe_prod` does not exist, causing recovered sorryAx; next ringHom rewrite attempt left a definitional equality and was rejected. Final explicit `rfl` closes it cleanly. `ENat.toNat_sum` exists in pinned Data/ENat/BigOperators.lean:75 but is not loaded by the stable seven imports; `#check_failure` only records that import boundary, not global absence. [Pinned source](../evidence/Roth.index_prod/BigOperators.lean.txt).

## Phase 5.5 — three statement-shape checks

Normal form: product mapped to sum is the right rewrite orientation; binder `∏ i ∈ s` matches the library's finite-product API. Syntactic generality: arbitrary ι and Finset already handle arbitrary finite families; no DecidableEq needs adding to the signature. Superfluous arguments: hr is verified removable; hf is essential uniformly; σ/Fintype and ℝ belong to the parent contract; s/f/α/r determine the result. The original implicit r is fine. The full caller keeps its hr argument position/type as `_hr`; actual removal of that caller hypothesis is outside this read-only assessment.

## Phase 6.0 — all callers and inline audit

Fresh `rg --no-ignore` and tracked `git grep` both find exactly three occurrences: module main-result docstring, declaration, and Theta proof application. Canonical source-inventory lexical enumeration agrees. [Complete search](../evidence/Roth.index_prod/complete-caller-search.json), [lexical inventory](../evidence/Roth.index_prod/lexical-enumeration.json), [complete caller](../evidence/Roth.index_prod/callers.json).

| Caller | Use and verified plan |
|---|---|
| Roth.sum_max_sub_le_index_det, Theta:407 | Rewrites the index of each nonzero determinant permutation product to a sum. Keep hentry nonvanishing witnesses; replace invocation with `IndexProd145.replacement _ (fun i _ ↦ hentry i) α r`. Entire declaration replay compiled. |

[Full caller and composition source](../evidence/Roth.index_prod/index-prod-callers-composition-executed.lean.txt), [clean native receipt](../evidence/Roth.index_prod/index-prod-callers-composition-receipt.json). Kernel audit independently finds exactly this direct consumer. Source proof applications and direct kernel consumers are separate enumerations; neither claims complete opaque/simp dependency closure. K=1 suggests checking abstraction, but does not prove inline composability. [Inline search](../evidence/Roth.index_prod/rg-inline.json) finds no independent production re-derivation of the finite law; binary multiplication and natural-order normalization are related API, not duplicate finite-product callers.

## Phase 6 — actual composition experiments

`IndexProdComposition145.exactAttempt` uses `fail_if_success` to test the exact natural-series theorem against the old real-index goal; it fails, as types differ. A bounded `simp only [index, map_prod]` closing attempt also fails. The theorem then closes using the independently verified hr-free local replacement. These are scoped negative probes, not universal absence proofs. No default-heartbeat exact? repetition, raised limits, sorry, axiom or unsafe proof was accepted.

Expanded natural law is one existing call; old form needs a substantive representation bridge, finite-order projection, casting and denominator scaling. Original finite induction uses project index_mul and index_eq_zero_iff, so it is not a1–3 mathlib-call composition. New133/143/144 bridge proofs are explicitly not existing mathlib calls. Phase6b says even a closing `simp [defs...]` composition would be BORDERLINE, not automatic NO. No such closing old-form composition was found here.

Parent re-aim gate was checked independently: canonical projected infDegree has no analogous arbitrary-real finite-product equality established by this search; therefore the positive natural-series hit does not force NO-mathlib-has-it for that broader parent property. This report does not blanket-inherit144's verdict.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, completed read-only assessment, verification unresolved[]. No user interruption required; the following are future upstream design questions:

1. Should the upstream finite-product law target polynomial `AddMonoidAlgebra.infDegree` for arbitrary real additive weights alongside binary multiplication?
2. Should this be organized through an extremal weighted-homogeneous component product API over ordered additive weights?
3. Should reciprocal-weight default-zero index_prod remain local while natural-weight applications directly use existing weightedOrder_prod?

Possible local refactor is concrete and verified: drop hr from index_prod, retain hf, use the direct index-one base and proved all-r binary law, then adapt the sole determinant caller. No production edit was authorized for this worker. Do not submit a duplicate natural-series wrapper. If the broader design proceeds, provisional home is Mathlib/Algebra/MonoidAlgebra/Degree.lean for the generic order law, with polynomial initial-piece infrastructure in Mathlib/RingTheory/MvPolynomial/WeightedHomogeneous.lean; import layering must be reviewed. PR title/grouping/reviewer checklist for YES is n/a because this is not a YES verdict. No NO deletion plan is substituted for unresolved API scope. Broader design work is optional follow-up, not unfinished verification.

## Phase 8 — portable handoff

[Assessment](../evidence/Roth.index_prod/assessment.json), [verification](../evidence/Roth.index_prod/verification.json), [overview entry](../evidence/Roth.index_prod/overview-entry.json), [current copy manifest](../evidence/Roth.index_prod/copy-manifest.json), [portable validator](../evidence/Roth.index_prod/validate.py). Validator checks mandatory phases and schema, current artifact hashes/bytes, fresh17 input hashes, native clean nonpartial success, standard axioms, exact293 order/uniqueness and target-specific direct consumer, accepted/rejected separation, target/caller experiment shapes, actual search methods, literature metadata and credential scan. Historical worker manifests never replace the current manifest. Root acceptance remains pending.
