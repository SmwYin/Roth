# Roth.index_mul

**Verdict: BORDERLINE-needs-human.** The natural-weight power-series multiplication law already exists and was verified independently. The parent index was re-aimed at projected `AddMonoidAlgebra.infDegree`, whose arbitrary-real-weight multiplication equality was not established by that hit: its available generic multiplication theorem gives only an inequality. The upstream choice is between a broader polynomial initial-form/order API and keeping reciprocal-index multiplication as local transport of the existing series law. This is an interface/scope question, not a judgment based on proof cost. Independently, positivity of the natural denominators is unnecessary for the exact project statement; its deletion and both complete callers were verified.

## Phase 0 — baseline and evidence

The shared successful build (2467 jobs, exit0, no reported errors/warnings) is reusable because all17 production/pin hashes freshly match its input manifest: [inputs](../evidence/Roth.index_mul/inputs.json), [manifest](../evidence/Roth.index_mul/input-manifest.json), [build](../evidence/Roth.index_mul/baseline-build.txt). Canonical144 resolves publicly at Roth/Index.lean162. The entire declaring module and both full caller declarations were read. No production source, Git or progress record was changed.

[Original native receipt](../evidence/Roth.index_mul/index-mul-original-audit-receipt.json) verifies the elaborated type and standard axioms. The large `#print` body has an explicit509-character MCP printer elision; no complete kernel-body dump is claimed. The exact original source is separately retained. The fresh target-specific canonical audit checks exactly293 names in tracked order, including private names, with293 unique/present/values and precisely two direct kernel consumers. [Audit source](../evidence/Roth.index_mul/index-mul-audit-executed.lean.txt). Root's pre-execution canonical source gate and this package's independent equality check protect against count-only mistakes.

## Phase 1 — statement and proof

For nonzero real multivariate polynomials P and Q, the minimum reciprocal-weighted Taylor exponent occurring in PQ at α is the sum of the two minima. The source proof clears denominators to natural weights, applies multiplicativity of multivariate power-series weighted order, and converts the two finite extended-natural orders to natural numbers before dividing by the common denominator.

Full native type:
```lean
Roth.index_mul.{u_1} {σ : Type u_1} [Fintype σ] {P Q : MvPolynomial σ ℝ}
    (hP : P ≠ 0) (hQ : Q ≠ 0) (α : σ → ℝ) {r : σ → ℕ}
    (hr : ∀ (j : σ), 0 < r j) :
    Roth.index (P * Q) α r = Roth.index P α r + Roth.index Q α r
```

σ/Fintype supplies the parent finite variable interface and product of denominators; P/Q are the factors; α is the translation center; r specifies reciprocal weights. hP/hQ ensure finite orders before projection; hr makes the original denominator product positive. The real index uses default0 at the zero polynomial, whereas the manuscript uses infinity.

## Phase 2 — preliminary classification

BIG: `index_mul` is listed among the module's main results. Definition-only one-line test and its three exemptions are n/a for a theorem. Its normalization, finiteness and casting steps are genuine proof content, even though its natural-order core is a single existing theorem.

## Phase 3 — exhaustive literature

All named channels were actually queried; at least three distinct general-web forms were used. Web artifacts retain exact requests, returned-response SHA256/bytes/status, titles/URLs/locators and concise original summaries, not full returned bodies. URL queries were removed from locator metadata; no signed credentials are retained. [Summary](../evidence/Roth.index_mul/literature-summary.json).

| Channel | Actual query/source and result |
|---|---|
| Specific web | “Roth polynomial index product sum indices weighted derivatives”; Roth ICM1958 p206 gives weighted derivative minimum; [metadata](../evidence/Roth.index_mul/web-specific.json). |
| General web | “weighted order product formal power series monomial valuation no zero divisors”; series weighted-order API and related valuation sources; [metadata](../evidence/Roth.index_mul/web-general.json). |
| Alias web | “minimum weight support polynomial multiplication initial forms additive valuation”; real-weight initial forms and their max/min conventions; [metadata](../evidence/Roth.index_mul/web-alias.json). |
| ChatGPT math | n/a: ask_chatgpt_math unavailable; no substitute invocation claimed. |
| Local references | clean.tex530–558 defines arbitrary positive real denominators and infinity at zero; Lemma4-1 proves product additivity via lowest homogeneous pieces. [Exact excerpt](../evidence/Roth.index_mul/clean-excerpt.tex.txt), [actual search](../evidence/Roth.index_mul/local-literature-search.json). |
| nLab | `site:ncatlab.org/nlab valuation multiplicative order formal power series`; valuation/valuation-ring pages give multiplicativity and ordered value groups, adjacent support; [metadata](../evidence/Roth.index_mul/web-nlab.json). |
| nCatLab | `site:ncatlab.org/ncatlab monomial valuation multiplicativity weighted order`; returned nLab/out-of-namespace pages, no exact namespace hit; [metadata](../evidence/Roth.index_mul/web-ncatlab.json). |
| Stacks | `site:stacks.math.columbia.edu power series order product valuation`; nearby restricted-series pages. Opened tag00I8 Section10.50 for general valuation-ring context, not an exact weighted-product theorem; [metadata](../evidence/Roth.index_mul/web-stacks.json). |
| MathOverflow | `site:mathoverflow.net monomial valuation weighted order multiplicative`; Q476147 discusses real weights and monomial-order refinements, showing the relevance of tied weights; [metadata](../evidence/Roth.index_mul/web-mathoverflow.json). |
| Recent arXiv | `site:arxiv.org "monomial valuations" after:2021-10-27`; Bengus-Lasnier–Shkolnikov, *Fibers of phase tropicalizations*, Jan2026/revisedApr2026, associated graded rings of monomial valuations; [metadata](../evidence/Roth.index_mul/web-arxiv.json). |

Primary [Markwig–Ren Definition1/2](https://link.springer.com/article/10.1007/s10208-019-09430-2) treats real weight vectors and initial homogeneous forms; maximum becomes minimum upon reversing weights. This supports the broader real-weight formulation, not a claimed compiled Lean theorem. The [recent paper](https://arxiv.org/abs/2601.18519) supplies contemporary valuation/graded-ring context. [Primary opens](../evidence/Roth.index_mul/web-primary-open.json) and [definition locator](../evidence/Roth.index_mul/web-primary-definition.json) record successful article/arXiv/Stacks access and the failed nLab XHTML fetch honestly.

Standard form: the minimum additive weight over a polynomial's finite coefficient support is additive on products over a coefficient domain. Lowest-weight homogeneous pieces are nonzero and have nonzero product. The natural-weight series formulation is standard too, but arbitrary real polynomial weights do not uniformly reduce to natural weights by one denominator. Infinity at zero yields an unconditional law; projecting it to default0 requires nonvanishing factors in general.

## Phase 4a — every parameter and hypothesis

| Parameter | Status |
|---|---|
| σ : Type* | Already universe polymorphic; arbitrary σ allowed in the verified expanded series/polynomial law. |
| Fintype σ | Fixed Roth.weight/index and denominator-product interface. It disappears in the expanded natural series law; not claimed removable while leaving the parent syntax unchanged. |
| P,Q : MvPolynomial σ ℝ | ℝ is fixed by Roth.index. The verified natural polynomial law works over CommSemiring R with NoZeroDivisors; the series law needs only Semiring and NoZeroDivisors. No characteristic-zero requirement in those laws. |
| hP : P≠0 | Necessary uniformly under default0; P=0,Q=X at center0 with r=1 gives0≠1. Actual guard compiled. |
| hQ : Q≠0 | Symmetric actual guard compiled. Neither is needed before infinity-valued natural order projection. |
| α : σ→ℝ | Changes translated support. Expanded law works for any polynomial/series; choose translated P/Q via multiplicativity of Taylor. |
| r : σ→ℕ | Reciprocal natural denominators are a strict subcase of the source's positive-real denominators. Existing natural-weight order does not by itself implement the whole real-weight parent. |
| hr : ∀j,0<rj | Removable in the exact conclusion. Use D=∏max1(rᵢ)>0 and wⱼ=D/rⱼ. When rⱼ=0, both reciprocal weight and natural D/0 are0. Verified independently. |
| ℝ-valued index | Explicit finite/default projection; replacing with infinity changes zero behavior and must be stated as a representation change. |

## Phase 4b — compiled weakening and separated proposal

STRICTLY NARROWER in one verified exact-interface hypothesis: delete hr. [Exact executed target proof](../evidence/Roth.index_mul/index-mul-target-clean-executed.lean.txt), [complete nonpartial success](../evidence/Roth.index_mul/index-mul-target-clean-receipt.json). `clearedWeight` proves the revised denominator identity for all natural r; `comparison` transports the index through projected infDegree and the independently established scaled weighted-order comparison; `replacement` proves the hr-free product identity. The original proof was not merely reused after deleting hr: its D=∏rᵢ normalization fails at mixed zero weights. Both zero-factor guards compiled after explicitly fixing the zero polynomial's variable type.

Verified expanded existing law:
```lean
∀ {σ : Type u} {R : Type v} [Semiring R] [NoZeroDivisors R]
  (w : σ → ℕ) (f g : MvPowerSeries σ R),
  (f * g).weightedOrder w = f.weightedOrder w + g.weightedOrder w
```
It is exactly `MvPowerSeries.weightedOrder_mul`. The isolated [mathlib source](../evidence/Roth.index_mul/index-mul-mathlib-executed.lean.txt) and [receipt](../evidence/Roth.index_mul/index-mul-mathlib-receipt.json) also verify the polynomial coercion specialization and real `toNat/D` product law for nonzero polynomials, arbitrary real D (including0 and negative D). Equality distributes over division regardless of its sign; unlike minimum identification, this final arithmetic equality needs no positivity.

Distinct broader upstream proposal, **not a compiled weakening or verified existing theorem**:
```lean
-- Proposed interface only; no implementation claimed.
-- σ arbitrary; R a commutative semiring with NoZeroDivisors; w : σ → ℝ.
AddMonoidAlgebra.infDegree (fun d ↦ (Finsupp.weight w d : WithTop ℝ)) (P * Q) =
  AddMonoidAlgebra.infDegree (fun d ↦ (Finsupp.weight w d : WithTop ℝ)) P +
    AddMonoidAlgebra.infDegree (fun d ↦ (Finsupp.weight w d : WithTop ℝ)) Q
```
The manuscript's homogeneous-piece proof motivates this form. Its general noninjective real-weight equality is not supplied by `le_infDegree_mul` or by `supDegree_mul` with its injectivity hypothesis. Existing arbitrary-weight homogeneous components and graded decompositions are relevant infrastructure, not a replacement proof. This distinction prevents a narrower natural-series hit from improperly settling the parent re-aim. Assessment completion does not claim completion of this future API development.

## Phase 4c — all nine modern-idiom checks

| # | Check | Finding and consequence |
|---|---|---|
| 1 | Typeclass preambles | Existing Semiring/NoZeroDivisors capture the natural core; no new class needed for multiplication. |
| 2 | Filters/nets | n/a, no convergence/topology. |
| 3 | Universal properties | Taylor and polynomial inclusion are existing multiplicative maps; no reconstruction of a universal object needed. |
| 4 | Bundled substructures | Weighted homogeneous submodules/graded algebra already exist and can organize initial pieces. Support alone is already bundled as a Finset. |
| 5 | Field/module hierarchy | Natural series law needs only Semiring/NoZeroDivisors, verified. Coercing polynomials uses CommSemiring. Broader coefficient changes to the real index require parent restatement. |
| 6 | Higher categories | No higher-categorical content. |
| 7 | Concrete numerical target | Retain infinity-valued orders internally, project only deliberately. Parent infDegree supports arbitrary real weights; natural series order only natural w. |
| 8 | Concrete-via-abstract | Fires. After the first index comparison rewrite, no index-specific mathematics remains; the rest uses existing weightedOrder_mul, finiteness and casts. Abstract natural core is already present. Parent's broader finite-support real-weight law is a separate candidate. |
| 9 | False-generalization guard | hP/hQ deletions rejected by compiled guards. hr deletion preserves exact default-zero reciprocal semantics. Replacing minimum by weightedTotalDegree maximum without dualization, assuming weight injectivity, or treating all real weights as one natural normalization is rejected. Arbitrary torsion exponent monoids are not silently substituted for free polynomial exponents. |

Modern idiom available: use canonical polynomial finite-support order or natural power-series order with an explicit comparison, rather than a second index construction. Concrete benefit: the natural core immediately covers arbitrary variable types and semiring domains, and the proposed broader polynomial order would cover irrational/negative real weights and initial forms without pretending to be the natural series API. The latter benefit is a design motivation, not a verified implementation claim.

## Phase 4.5 — six infrastructure risks

n/a for all six rows: theorem introduces no typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe construction, or coercion instance. The proposed broader theorem likewise need not introduce a new definition/instance. Import layering for a future component/order API remains part of upstream interface selection.

## Phase 4.6 — all proof-strategy checks

| Row | Audit |
|---|---|
| Topological εδ/filter | n/a, algebraic finite minima. |
| Element vs substructure | Existing homogeneous submodules/decompositions provide a useful generic initial-piece organization. No ideal inclusion alone proves noncancellation of lowest terms. |
| Sequence vs net | n/a, no limiting process. |
| Construction vs universal property | Existing Taylor/coercion maps are reused; no new universal-property proof required. |
| Missing helper API | Natural multiplication law exists. New generic coe/projection comparisons from143 are genuine normalization proofs. Potential broader extremal homogeneous-component multiplication/real-weight infDegree law is a distinct API candidate. |

REFACTOR-RECOMMENDED: keep the already existing natural multiplication law as the core; remove hr locally using the verified normalization. For a broader upstream contribution, decide whether an extremal-component multiplication theorem or a direct polynomial infDegree theorem is primary. That decision concerns reusable normal forms and import boundaries, independent of proof cost.

## Phase 5 — actual five-method search on three forms

[Formal receipts](../evidence/Roth.index_mul/formal-search.json) preserve all12 actual Finder/Loogle/LeanSearch/local requests and responses; the fifth method is full pinned source search for [current](../evidence/Roth.index_mul/rg-current.json), [literature](../evidence/Roth.index_mul/rg-literature.json), and [abstract](../evidence/Roth.index_mul/rg-abstract.json) forms. The first literature Finder and abstract LeanSearch requests timed out, honestly retained; [Finder retry](../evidence/Roth.index_mul/search-literature-finder-retry.json) succeeds with the exact natural multiplication law; a [fresh successful retry](../evidence/Roth.index_mul/search-abstract-leansearch-retry.json) returns weightedOrder_mul, inf-support inequality, support_mul and homogeneous multiplication. Local index reports unavailable, with project/scratch hits for index_mul; this is not absence evidence.

| Method | Current point index | Standard weighted order | Abstract finite-support/graded order |
|---|---|---|---|
| Finder | DegreeOf/totalDegree products (different maximum APIs) | Initial timeout; successful retry weightedOrder_mul | infDegree and generic inf-support inequalities |
| Loogle | weightedOrder multiplication family | weightedOrder_mul exact hit | le_infDegree_mul only |
| LeanSearch | Natural series weightedOrder law | Existing natural order multiplication | Initial timeout; retry gives natural law, inf-support inequality, homogeneous multiplication |
| rg | No Roth spelling replacement | weightedOrder_mul exact pinned source146 | infDegree inequality637; injective supDegree equality515; arbitrary-M homogeneous infrastructure381/519/677/702 |
| Local | Project target, scratch theorem, unrelated subgroup names | weightedOrder_mul | infDegree_mul empty, index unavailable |

Pinned [NoZeroDivisors](../evidence/Roth.index_mul/NoZeroDivisors.lean.txt) supplies the verified natural multiplication law; [Degree](../evidence/Roth.index_mul/Degree.lean.txt) supplies only generic infDegree inequality and injective supDegree equality. The [weighted homogeneous source](../evidence/Roth.index_mul/WeightedHomogeneous.lean.txt) supplies arbitrary AddCommMonoid weight components, coefficient/support formulas, homogeneous product and graded decompositions. [DirectSum/graded search](../evidence/Roth.index_mul/rg-graded.json) found no corresponding extremal-degree product equality. Search failures or missing names are not proof of universal absence. [Isolated component signatures](../evidence/Roth.index_mul/index-mul-generic-api-clean-receipt.json), [decomposition/product signatures](../evidence/Roth.index_mul/index-mul-broader-api-receipt.json) and three `#check_failure` probes substantiate the API distinctions without such an absence claim.

Parent re-aim outcome: **partial hit**. Natural weighted-order multiplication exists exactly, but the canonical parent's arbitrary-real infDegree equality is not established by that result alone. New bridge proofs are not counted as preexisting library primitives. This is why the report does not blanket-inherit NO from parent133 or YES from comparison143.

## Phase 5.5 — all statement-shape checks

1. Normal form: preserve the two distinct canonical objects—polynomial infDegree and natural series weightedOrder—with a coefficient-preserving comparison. Do not add pairwise reciprocal aliases or a second natural multiplication theorem. A general polynomial infDegree or initial-component result is the potential new normal-form law.
2. Syntactic generality: the exact hr-free equality rewrites at both callers with explicit r and no positivity proof. The broader proposed infinity-valued law would remove nonzero hypotheses; its projection would reintroduce them. The full natural series law already has the useful unconditional shape.
3. Superfluous arguments: hr is actually removed; hP/hQ cannot be removed uniformly under current zero convention. σ/Fintype/ℝ remain fixed parent-interface constraints. α and r change the index; dropping them is an expanded representation, not an unused-argument claim.

RESTATE-BEFORE-SHIP: no Roth-specific multiplication theorem should be submitted unchanged. Local deletion of hr is verified. Broader upstream interface/scope remains a concrete design decision.

## Phase 6.0 — complete callers and inline audit

[Canonical-inventory enumeration](../evidence/Roth.index_mul/lexical-enumeration.json), [ignore-safe rg and tracked git grep](../evidence/Roth.index_mul/complete-caller-search.json), [full fragments/plans](../evidence/Roth.index_mul/callers.json). Two proof-body applications in two declarations; zero statement applications. One application is external to the declaring module. Documentation mention/declaration are excluded. The independent293-value audit agrees, with the Theta consumer's actual private kernel name retained.

| Caller | Concrete refactor and actual experiment |
|---|---|
| Roth.index_prod, Index185 | Replace index_mul with IndexMul144.replacement, pass the same nonzero factor certificates and α, then explicit r, omit hr. The entire original finite-product statement/proof compiled. |
| Private Roth.index_separated_mul_le_aux, Theta438 | Replace the single rewrite application with IndexMul144.replacement and explicit r, retaining the two injective-rename nonzero proofs. The original full statement and proof compiled. hr0 was used solely by the old multiplication call; root renamed its binding _hr0 to avoid a warning while preserving the hypothesis type and position. |

[Clean complete caller replay](../evidence/Roth.index_mul/index-mul-callers-clean-executed.lean.txt), [native receipt](../evidence/Roth.index_mul/index-mul-callers-clean-receipt.json). Source-level callers and direct kernel consumers remain separate audits. [Inline search](../evidence/Roth.index_mul/rg-inline.json) finds no independent production derivation bypassing this theorem; the original proof itself is the only production natural-order multiplication use. Current callers justify retaining convenient local API while upstream design is settled.

## Phase 6 — actual compositions and semantic guards

The re-aimed natural law has a one-call proof, exactly `MvPowerSeries.weightedOrder_mul w f g`, independently compiled without Roth imports and guarded by `#check_failure Roth.index_mul`. Polynomial specialization needs coe_mul; finite real scaling additionally needs finite-order proofs, ENat.toNat_add, Nat.cast_add and add_div. The unchanged old index spelling is **NOT-COMPOSABLE** in ≤3 existing mathlib calls: Taylor, denominator clearing, coe comparison, finite/default projection and arithmetic are real normalization work. The project comparison theorem and new133/143 bridges cannot be counted as mathlib calls.

[The final exact diagnostic](../evidence/Roth.index_mul/index-mul-composition-final-executed.lean.txt) and [native success](../evidence/Roth.index_mul/index-mul-composition-final-receipt.json) attempt the existing theorem directly on the old goal and a bounded `simp only [index, map_mul]` unfolding of index; both fail to close, then the independently proved hr-free replacement completes the statement. This tests the displayed candidate routes only; it is not a proof of absence. No closing simp composition was found, so Phase6b's automatic BORDERLINE-for-simp case is not invoked. The verdict instead concerns the broader normal-form API scope.

Guard evidence: for P=0,Q=X() and the symmetric case at center0,r=1, real default0 makes the two sides unequal. For arbitrary r including zero coordinates the new positive D=∏max1(rᵢ) preserves reciprocal weights and proves additivity. All-zero weights therefore produce0 consistently; empty σ gives denominator1 and only constant exponents. Natural w=0 is permitted by weightedOrder_mul. The expanded coefficient condition NoZeroDivisors prevents cancellation through zero divisors; it is present in the existing exact law. No widening to arbitrary exponent monoids or arbitrary real-weight infinite series is claimed.

## Phase 7 — verdict and actionable design questions

**BORDERLINE-needs-human.** The scope is genuinely ambiguous: the natural-series algebraic law is already in mathlib, and its local reciprocal-index transport can be made hr-free; nevertheless, the parent133 abstraction is broader, and the manuscript's initial-piece argument points at a real-weight polynomial API not established by the exact natural hit. Declaring automatic NO would ignore the parent re-aim; declaring YES-but-generalise-first for a broader real-weight theorem would present an unverified interface development as a compiled weakening. The verified hr deletion alone does not identify a missing upstream natural multiplication law.

1. For polynomial finite-support orders, should the primary upstream law be stated directly for `AddMonoidAlgebra.infDegree` with real additive variable weights, rather than through natural `MvPowerSeries.weightedOrder`?
2. Should that broader law first expose extremal `weightedHomogeneousComponent` multiplication for ordered additive weight targets, with polynomial infDegree multiplication as a corollary?
3. Should the reciprocal-weight real index remain project-local using the checked natural normalization and existing `weightedOrder_mul`, while the broader infDegree/initial-form API is developed separately?

These are future upstream interface questions, not an approval request or a blocker to this completed read-only assessment. Alternative local destination: Roth/Index.lean is appropriate for the default0 reciprocal convention and its two callers. Immediate concrete action is the verified hr-free replacement at both callers; the natural law itself should be reused directly behind the comparison layer. If a broader contribution is chosen, its proof, coefficient/order generality, import home and reviewer selection must be completed under /generalise and /cleanup before a PR. No production edits were authorized by this assessment contract.

## Phase 8 — completeness and verification limits

[Assessment metadata](../evidence/Roth.index_mul/assessment.json), [verification index](../evidence/Roth.index_mul/verification.json), [portable validator](../evidence/Roth.index_mul/validate.py), [overview entry](../evidence/Roth.index_mul/overview-entry.json). All required phases, actual search methods and named literature channels are complete; unresolved assessment checks are empty. Accepted evidence uses only standard axioms, no recovered sorry, no raised limits, and complete native successes. Rejected initial guards, caller warning, importless signature attempt, two offside exact-attempt failures (including recovered sorryAx), and a nonaccepted simp-warning attempt are preserved separately. None is used as accepted proof evidence. Earlier comparison/finite-projection proof sources and receipts are explicitly prerequisite evidence, not new existing mathlib primitives. The prospective arbitrary-real infDegree theorem is deliberately not listed as an accepted proof.
