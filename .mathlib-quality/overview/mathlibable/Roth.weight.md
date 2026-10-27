# Roth.weight — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** The pinned `Finsupp.weight` already defines the more general weighted sum. Specialize its scalar semiring to ℕ, its target to ℝ, and its assigned weights to `fun j ↦ (r j : ℝ)⁻¹`. This decision concerns upstream duplication; it does not claim the heavily used project name is dead code.

## Phase 0 — doctor and canonical position

Canonical declaration 27 is the public noncomputable definition at Roth/Box.lean:71. Previous completed declaration is Roth.box; tracked progress names Roth.weight next. No prefilter applies: there is no qualified Roth.weight in pinned mathlib ([untruncated search](../evidence/Roth.weight/source-search-0.json)). The full declaring module and all 30 explicit caller declarations were read. No sorry, unsafe, native_decide or limit change occurs in the target.

The successful baseline build is reusable: all 17 current source/pin hashes freshly match the shared input manifest. [Baseline](../evidence/Roth.weight/baseline-build.txt), [fresh hash check](../evidence/Roth.weight/baseline-hash-check.json), [canonical metadata](../evidence/Roth.weight/target-manifest.json), [order](../evidence/Roth.weight/canonical-order.json). Assessment writes are scratch evidence only; production files/pins remain unchanged.

Native root checks are complete successes, partial=false, timed_out=false, with no error/warning diagnostics. [Project receipt](../evidence/Roth.weight/native-project.json), [exact executed disk source](../evidence/Roth.weight/project-executed.lean.txt), [disk-source hash agreement](../evidence/Roth.weight/project-source-check.json). The project document contains earlier verification sections; only WeightAssessment and WeightConsumerChecks are relevant here. An initial Finite/Fintype equality attempt was rejected and corrected using Subsingleton.elim; [rejected attempt](../evidence/Roth.weight/rejected-target.json) is not accepted proof evidence.

## Phase 1 — comprehend

For a finite set of variables, a natural parameter vector r and a finitely supported natural multi-index d, this definition sums the real fractions dⱼ/rⱼ. There is no positivity hypothesis. In Lean's totalized real field, zero denominators contribute zero. In the Roth index, these values measure the normalized derivative orders of nonzero Taylor coefficients.

Fresh elaborated type:
```lean
@Roth.weight : {σ : Type u} → [Fintype σ] → (σ → ℕ) → (σ →₀ ℕ) → ℝ
```
The section's DecidableEq binder is absent from this type. r and d are essential data; Fintype is required by the written full sum, not by the weighted-sum mathematical object. There are no project dependencies. Definition formula and rfl were checked natively.

## Phase 2 — preliminary checks

BIG: this introduces a named mathematical concept, listed among the module's main definitions. Literature width remains exhaustive. Body substantive line count: 1; ONE-LINER. Defeq-abuse exemption: no protective sealed interface or delicate unfolding path was found. Diamond-avoidance exemption: no instances are introduced. Semantic/API-stability exemption: applicable locally, because 30 declarations use the name and several proofs unfold its formula. That is a reason to organize a local interface, not a reason to add a duplicate definition upstream.

## Phase 3 — exhaustive literature

Only requests, returned-response hashes/bytes/status, locators and original concise summaries are retained for web evidence. No full web result or article body is persisted.

| Channel | Actual query/access and finding |
|---|---|
| General web, specific | “Roth theorem index polynomial weighted multi index sum i_j r_j definition”: Roth's 1958 ICM account measures derivative order by reciprocal parameter weights; University of Houston Roth notes use the same index formula. |
| General web, standard | “weighted degree monomial real weights linear functional exponent vector”: MIT 18.721 notes §1.8 before Lemma 1.8.8 assign weights to variables and sum exponent times assigned weight. |
| General web, abstract | “Finsupp weight free commutative monoid weighted sum universal property”: weighted-sum/free-object formulations and library source documentation. [Three exact requests and metadata](../evidence/Roth.weight/literature-general.json). |
| ChatGPT mathematics | n/a: ask_chatgpt_math unavailable in tool inventory. No simulated answer. |
| Local references | clean.tex §Index, lines 529–555, explicitly uses arbitrary positive real parameters; its Lean note distinguishes integral common-denominator discretization. [Local excerpt](../evidence/Roth.weight/local-literature.txt). |
| nLab | Separate searches “site:ncatlab.org/nlab weighted degree monomial” and “site:ncatlab.org/nlab free commutative monoid” found finite natural formal combinations and the free-forgetful universal property. [Metadata](../evidence/Roth.weight/literature-nlab.json). Direct page open failed HTTP400, unsupported application/xhtml+xml; indexed text was accessible. |
| nCatLab | Separate site-wide queries for weighted monomial degree and free commutative monoids found Selinger thesis §6.1.3, generalized multicategories and Trimble operads. Adjacent abstraction, no special reciprocal-weight construction. [Metadata](../evidence/Roth.weight/literature-ncatlab.json). |
| Stacks | “site:stacks.math.columbia.edu weighted degree monomial grading”: Tag 0BZ6 §22.38 adds degrees on free graded-algebra words. Relevant structural analogue, not exact Roth index. [Metadata](../evidence/Roth.weight/literature-stacks.json). |
| MathOverflow | Roth-index and real-weighted-degree queries found questions 503992 and 81001, with weighted monomial degrees and dot products of exponent vectors; polynomial maximum degree is a distinct derived notion. [Metadata](../evidence/Roth.weight/literature-mathoverflow.json). |
| Recent arXiv, 2021-10-26–2026-10-26 | Two dated-topic queries; opened arXiv:2610.17589 (submitted 2026-10-13) and 2402.08833 (2024, revised August). The former concerns weighted projective Roth and warns about naive index rescaling; the latter assigns linear monomial weights. Both are adjacent, not a replacement definition. Unrelated statistical weights and finite-field Roth hits excluded. [Search](../evidence/Roth.weight/literature-arxiv.json), [primary opens and failure metadata](../evidence/Roth.weight/literature-primary.json). |

Primary locators: [Roth ICM 1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [MIT §1.8](https://math.mit.edu/classes/18.721/ag-feb20.pdf), [free commutative monoid](https://ncatlab.org/nlab/show/free%2Bcommutative%2Bmonoid), [Stacks 0BZ6](https://stacks.math.columbia.edu/tag/0BZ6), [recent Roth variant](https://arxiv.org/abs/2610.17589), [weighted monomial ideals](https://arxiv.org/abs/2402.08833).

Literature summary: this is a monomial weight/weighted exponent sum, specialized to reciprocal parameters in Roth's normalized index. The general algebraic form assigns an arbitrary target element to each variable and extends additively over finite natural combinations. Positive parameters are customary for order/faithfulness properties, not necessary to define the totalized sum. The current natural-parameter real-valued form is narrower than both local literature and the existing library abstraction. No claim of novelty follows from a failed search.

## Phase 4a–b — generality

| Parameter | Current interface | General form and verification |
|---|---|---|
| σ universe | Type u | Universe-polymorphic; Type 1 project example succeeds. |
| Fintype σ | Full ambient finite enumeration | Finite-only rewritten sum compiles and agrees after instance equality; arbitrary σ works through finite-support Finsupp.weight, with actual infinite ambient ℕ singleton example. |
| DecidableEq σ | Not an elaborated parameter | Already omitted; no weakening to claim. |
| r : σ → ℕ | Natural denominators | Assign arbitrary w : σ → M instead. Native generic AddCommMonoid M examples compile; native real_denominator_agreement also verifies arbitrary real denominator parameters, encompassing clean.tex's positive real case. This changes the parameter representation, rather than merely deleting a binder in the old body. |
| d : σ →₀ ℕ | Finite natural coefficients | Already appropriate monomial exponent representation. Existing Finsupp.weight also supports arbitrary Semiring R coefficients and Module R M; do not change monomial exponent semantics to signed coefficients without explanation. |
| output ℝ | Real sum | Generic AddCommMonoid M target verified using its canonical ℕ-module instance. No field, order, topology, or finiteness required for the generic sum. |
| positivity | None | Preserve it. Adding positivity would restrict the original object. Zero-denominator nonzero-singleton guard compiles. |

STRICTLY NARROWER as an interface to an existing abstraction, with verified Finite-only and arbitrary-index finite-support variants. No missing generalization needs to be upstreamed. [Raw exact source](../evidence/Roth.weight/raw-executed.lean.txt) and [raw successful receipt](../evidence/Roth.weight/native-raw.json) independently verify the generic form using only Mathlib.Data.Finsupp.Weight and Mathlib.Basic.Real.Basic; #check_failure Roth.weight guards isolation. No Roth/downstream theorem closes these raw proofs.

The general replacement is `Finsupp.weight (R := ℕ) w : (σ →₀ ℕ) →+ M`; its existing parent implementation is `(Finsupp.linearCombination ℕ w).toAddMonoidHom`. The exact old interface is its reciprocal-real specialization. A real-coefficient `linearCombination ℝ` would require changing/coercing the coefficient Finsupp; using ℕ as the scalar is the direct route.

## Phase 4c — nine modern-idiom checks

| Q | Applies? | Restatement and concrete consequence |
|---|---|---|
| 1 Typeclasses | Yes | Canonical ℕ-module on AddCommMonoid M, confirmed by #synth; arbitrary module targets use the existing class hierarchy. |
| 2 Filters/topology | No | Finite algebraic sum, no convergence or neighborhoods. |
| 3 Universal property | Yes | Finsupp.linearCombination extends assigned generator values linearly. Existing Finsupp.weight exposes its additive map. This removes separate hand-proved zero/add laws. |
| 4 Bundled substructure | No | No set-with-closure predicate; bundling the operation as AddMonoidHom is relevant instead. |
| 5 Hierarchy weakening | Yes | Real field calculation replaced by generic additive target; raw generic zero/add/single examples succeed. |
| 6 Higher categories | No | No categorical coherence or higher morphisms needed. |
| 7 Concrete index/codomain | Yes | Arbitrary ambient σ and AddCommMonoid M. Native ℕ-index example demonstrates truly infinite ambient support handling. |
| 8 Concrete-via-abstract | Yes | Body contains no special real constant, only real casts and division inside a sum. Identifier audit finds no mathematical object-specific lemma; replacing fractions by nsmul of inverse weights yields the verified existing abstract object. It is a definition, so there is no residual proof body after unfolding to count. |
| 9 False-generalization | No for accepted form | Exact equality verifies preservation even at zero denominators. Reject claiming weight=0 iff d=0 without positive denominators. Also reject identifying this sum with polynomial weightedTotalDegree (a supremum) or weightedOrder (a minimum). Natural common-denominator weights in Index:130 require positivity and differ from the reciprocal-real definition when denominators vanish. |

Modern idiom available: yes, already in mathlib. Map zero, map add and Finsupp.weight_single give actual downstream consequences, verified both generically and against the project's three corresponding consumers. This is reuse of existing organization, not an unsupported modernization contribution.

## Phase 4.5 — six infrastructure risks

| Risk | Level | Evidence |
|---|---|---|
| Typeclass diamond | NONE | Numeric function definition introduces no instance. #synth Module ℕ ℝ chooses AddCommMonoid.toNatModule. |
| Reducibility leak | LOW | Ordinary def, no reducible attribute; native rfl exposes formula as expected. Existing proofs explicitly unfold it. |
| Noncanonical unfolding | LOW | Full ambient sum differs definitionally from support sum; equality requires weight_eq_sum and scalar/division normalization. State this bridge explicitly during migration. |
| Instance priority collision | NONE | Neither target nor proposed specialization installs any instance/priority. |
| Universe polymorphism | NONE | Fresh elaborated Type u and compiled Type 1 specialization; no universe restriction observed. |
| Coercion ambiguity | LOW | Original returns ℝ; Finsupp.weight returns AddMonoidHom coerced to function through the existing canonical DFunLike API. Native applications and map laws succeed without competing coercions. |

Overall LOW; no HIGH mitigation required. Reuse existing map instances and avoid adding a custom module structure.

## Phase 4.6 — five proof-strategy checks

| Question | Applies? | Result |
|---|---|---|
| Topology ε–δ versus filters | No | No topology. |
| Algebra elements versus bundled inclusions | Yes, bundled operation | Replace manual coordinate-addition normalization by map_add of existing AddMonoidHom; compiled consumer. |
| Analysis sequences versus nets | No | No limits. |
| Categorical construction versus universal property | Yes, algebraic free-module analogue | Reuse Finsupp.weight / linearCombination, rather than create another extension operation. |
| Helpers mathlib should have | No missing helper identified for definition | weight_eq_sum, weight_single, map_zero and map_add supply the tested bridge and consumers. Other order/index lemmas require their own later re-aim assessments. |

REFACTOR-RECOMMENDED: use the existing bundled weighted sum. No new helper theorem is being counted as an existing mathlib primitive.

## Phase 5 — actual five-method × three-form search

Every entry below was actually executed; full raw returned receipts retained. External indexes can differ from the pinned revision; pinned source plus native signatures decide candidate validity. Local search reports index=unavailable and returns source fallback matches; this is presence evidence, never proof of absence.

| Method | Current reciprocal finite sum | Literature weighted monomial sum | Abstract module/free sum |
|---|---|---|---|
| Finder | Current prose returned centroid/constant weights, no exact hit | Found isWeightedHomogeneous_monomial and weightedTotalDegree; adjacent consumers | Found weight_apply, weight, weight_single and linearCombination |
| Loogle | `Finsupp.weight, _ = ∑ _, _` → weight_eq_sum | `_ = ∑ i, _ • _` → sum_nsmul, Fintype.linearCombination_apply | `Finsupp.linearCombination` → module extension API |
| LeanSearch | Explicit natural weighted-sum prose → weight, weight_apply, weight_single | Found weight_apply and weight, plus unrelated affine weights | Linear-combination prose → linearCombination and apply |
| rg pinned source | Current reciprocal normalization and weight_eq_sum search | weight_eq_sum, weightedTotalDegree, isWeightedHomogeneous_monomial | linearCombination, apply, mapDomain, single and def weight |
| local names | weight → Finsupp.weight and target, fallback index unavailable | Separate weight query → same relevant fallback plus unrelated namespaces | linearCombination → exact definition and apply/mapDomain APIs, fallback index unavailable |

[Current Finder](../evidence/Roth.weight/search-current-lean_leanfinder.json), [Loogle](../evidence/Roth.weight/search-current-lean_loogle.json), [LeanSearch](../evidence/Roth.weight/search-current-lean_leansearch.json), [local](../evidence/Roth.weight/search-current-lean_local_search.json), [rg](../evidence/Roth.weight/search-current-rg.json).
[Literature Finder](../evidence/Roth.weight/search-literature-lean_leanfinder.json), [Loogle](../evidence/Roth.weight/search-literature-lean_loogle.json), [LeanSearch](../evidence/Roth.weight/search-literature-lean_leansearch.json), [local](../evidence/Roth.weight/search-literature-lean_local_search.json), [rg](../evidence/Roth.weight/search-literature-rg.json).
[Abstract Finder](../evidence/Roth.weight/search-abstract-lean_leanfinder.json), [Loogle](../evidence/Roth.weight/search-abstract-lean_loogle.json), [LeanSearch](../evidence/Roth.weight/search-abstract-lean_leansearch.json), [local](../evidence/Roth.weight/search-abstract-lean_local_search.json), [rg](../evidence/Roth.weight/search-abstract-rg.json).

Concluded: found in mathlib as **Finsupp.weight**, more general form. Pinned source [Weight.lean](../evidence/Roth.weight/Weight.lean.txt), definition line 82, weight_eq_sum line 100; underlying [LinearCombination.lean](../evidence/Roth.weight/LinearCombination.lean.txt). Exact signatures checked in both native environments.

## Phase 5.5 — three statement-shape checks

1. Normal form: full Fintype sum, Finsupp support sum, and bundled weight application are equivalent. Existing canonical concept is Finsupp.weight; proposed equality places it on the RHS. Do not add pairwise equivalences between further wrappers.
2. Syntactic generality: actually tested full old formula, Finite-only formula, and arbitrary-index bundled reciprocal weight. Chosen replacement is `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`, which supplies an ordinary function when needed in Set.image and a homomorphism when needed in map laws.
3. Superfluous arguments: σ, r, d essential; DecidableEq already absent. Fintype essential only to the old full-sum syntax, dispensable in support-based representation. No positivity can be silently added.

RESTATEMENT/REUSE recommended; no new declaration to ship.

## Phase 6 — callers, inline audit and actual experiments

30 explicit source-level caller declarations, including 9 in the declaring file. This count is not a kernel/simp dependency closure. [Complete exact caller excerpts and hashes](../evidence/Roth.weight/caller-excerpts.json), [untruncated references](../evidence/Roth.weight/source-search-1.json), [inline-form search](../evidence/Roth.weight/source-search-2.json). This is an active local API. Inline audit: Theta:502 spells the same sum using rfl while explicitly starting from weight; Main:366 unfolds weight in the rpow product calculation; Index:133 expands both weight notions for common-denominator discretization. No independent bypass motivates a dead-code claim.

Replacement notation below is explanatory only: W(r) means the existing `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`; apply W(r) to d for a number. For every caller, replace all scalar applications `weight r d` with `W(r) d`; bare function occurrences `weight r` become `⇑W(r)`. The per-row additional plan accounts for formula-sensitive proofs.

| Explicit caller | Source | Additional refactor plan |
|---|---|---|
| Roth.weight_nonneg | Roth/Box.lean:75 | Use weight_eq_sum and nonnegative nsmul/inverses, or unfold to original finite fractions. |
| Roth.weight_zero | Roth/Box.lean:80 | Use map_zero; actual compiled consumer. |
| Roth.weight_add | Roth/Box.lean:85 | Use map_add; actual compiled consumer. |
| Roth.weight_eq_zero_iff | Roth/Box.lean:91 | Retain hr; expand weight_eq_sum and normalize nsmul/division before existing sum-zero argument. Do not apply canonically ordered-target lemma directly to ℝ. |
| Roth.weight_single | Roth/Box.lean:96 | Use Finsupp.weight_single and nsmul_eq_mul/div_eq_mul_inv; actual compiled consumer. |
| Roth.weight_le_card | Roth/Box.lean:103 | Expand weight_eq_sum to fractions; retain coordinatewise bound proof. |
| Roth.weight_mul_left | Roth/Box.lean:110 | Expand weight_eq_sum, convert nsmul to multiplication, retain sum_div/div_div proof. |
| Roth.weight_le_degree_div | Roth/Box.lean:118 | Replace rw [weight] with weight_eq_sum plus scalar normalization; retain degree_eq_sum/gcongr. |
| Roth.weight_mapDomain | Roth/Box.lean:127 | Expand to Finsupp.sum via weight_apply; retain existing sum_mapDomain_index_inj and normalize nsmul/division. |
| Roth.index | Roth/Index.lean:58 | Use ⇑W(r) in Set.image; resulting input/output types agree. |
| Roth.index_le_weight | Roth/Index.lean:69 | Use ⇑W(r) in image/bddBelow and W(r) d in conclusion. |
| Roth.exists_weight_eq_index | Roth/Index.lean:76 | Replace both Set.image functions and resulting scalar equality uniformly. |
| Roth.le_index_iff | Roth/Index.lean:85 | Replace scalar expression; csInf argument structure unchanged. |
| Roth.index_sub_weight_le_index_hasseDeriv | Roth/Index.lean:109 | Replace scalar expression and use W(r).map_add at the existing weight_add rewrite. |
| Roth.weight_eq_finsuppWeight_div | Roth/Index.lean:130 | Keep positive common-denominator natural weights on RHS; expand both Finsupp.weight_eq_sum instances and normalize the real nsmul. Preserve hr and Nat.cast_div_charZero divisibility. |
| Roth.index_mul_left_weights | Roth/Index.lean:200 | Replace image functions uniformly; reuse migrated scaling identity or normalize assigned inverse weights. |
| Roth.index_unique | Roth/Index.lean:234 | Replace simp [weight] with weight_eq_sum and scalar normalization; Unique summation still supplies the single coordinate. |
| Roth.filter_weight_le_eq_empty | Roth/Lattice.lean:143 | Replace filter predicate; use migrated/nonnegative expanded weight argument. |
| Roth.card_filter_fiber_eq | Roth/Lattice.lean:147 | Replace both predicates; use existing map_add, weight_single and mapped-domain sum identity before grind. |
| Roth.card_filter_weight_le_of_le_sqrt_aux | Roth/Lattice.lean:158 | Replace predicate only; cardinal filter argument remains applicable. |
| Roth.card_filter_weight_le_succ_aux | Roth/Lattice.lean:166 | Replace all induction/filter predicates consistently; use migrated fiber equality. |
| Roth.card_filter_weight_le | Roth/Lattice.lean:202 | Replace predicate and use consistently migrated auxiliary signatures. |
| Roth.abs_prod_pow_le_rpow_of_le_weight | Roth/Main.lean:347 | Replace hw/conclusion use; at rpow_sum calculation expand weight_eq_sum and normalize scalar division before Finset.mul_sum. |
| Roth.le_index_of_forall_eval_eq_zero | Roth/MainLemma.lean:419 | Replace hvan predicate; index/vanishing argument unchanged after consistent migration. |
| Roth.exists_hasseDeriv_eval_ne_zero | Roth/MainLemma.lean:454 | Replace existential scalar inequality; transport attained-index equality as before. |
| Roth.exists_mem_RSet_le_index_aux | Roth/MainLemma.lean:550 | Replace hJ predicate; use migrated le_index_of_forall_eval_eq_zero. |
| Roth.mul_card_filter_weight_le_aux | Roth/MainLemma.lean:569 | Replace filter predicate and invoke migrated counting statement. |
| Roth.exists_mem_RSet_le_index_of_rpow_bound_aux | Roth/MainLemma.lean:581 | Replace J's filter predicate; propagate to hD and hJ arguments. |
| Roth.sum_max_sub_le_index_det | Roth/Theta.lean:376 | Replace hδ predicate; use map_add/weight_single and mapped-domain identity in hterm. |
| Roth.weight_le_delta_aux | Roth/Theta.lean:494 | Replace zero branch with map_zero; replace rfl at line 502 by weight_eq_sum plus normalization; keep subsequent fraction estimates. |

Actual composition experiments: project WeightConsumerChecks verifies add/zero/single without using the corresponding project theorem; the sole project bridge used is the independently verified representation equality. RawWeightAssessment repeats zero/add/single using only existing mathlib, verifies generic AddCommMonoid targets, arbitrary-real denominator agreement, support-sum agreement, and a genuinely infinite ambient ℕ example. All accepted axioms are standard propext, Classical.choice and Quot.sound; no sorryAx.

The existing-definition witness is:
```lean
example [Fintype σ] (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r d = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d := by
  simpa [Roth.weight, nsmul_eq_mul, div_eq_mul_inv] using
    (Finsupp.weight_eq_sum (fun j ↦ (r j : ℝ)⁻¹) d).symm
```
Replacement term: `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d` — one existing named operation. The displayed proof is a representation bridge, not a claim that an arbitrary simp-normalization theorem is a ≤3-call composition. Phase 6b's BORDERLINE rule for a newly obtained `simp [defs…]` composition does not apply to erase this exact existing named-object match. No new normalization premise or helper API is required to identify the object. Other wrapper/order lemmas receive separate future assessments.

## Phase 7–8 — verdict and actionable handoff

**NO-mathlib-has-it**, via `Finsupp.weight`, Mathlib/Data/Finsupp/Weight.lean:82; finite-form identification via `Finsupp.weight_eq_sum`:100. Its underlying `Finsupp.linearCombination`, Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:52, is already available too. Generic map_zero/map_add and weight_single cover the tested consumers. This is the same mathematical object, including the target's unrestricted zero parameters, in a more general and structurally useful interface.

The source-level refactor plan above covers every explicit caller, including higher-order uses, formula-unfolding proofs and common-denominator discretization. No production refactor is performed by this assessment. Next action: migrate the scalar applications and functions to the existing reciprocal-weight specialization, replace formula-sensitive unfolding with weight_eq_sum/weight_apply normalization, and remove the redundant project definition after downstream compilation. Do not automatically delete dependent lemmas: re-aim each at Finsupp.weight and assess its own mathematical content.

Alternative local destination: Roth/Box.lean is appropriate for a short project notation or documented semantic interface if desired during migration; upstream needs no duplicate reciprocal-parameter definition. The local name has real use, so retaining a documented project API is a project organization choice. No Archive/satellite contribution is needed.

YES-only upstream PR file/title/grouping/reviewer tasks: n/a, because the concept is already upstream and this verdict proposes no PR. No cost-based downgrade was used. No unresolved verification remains. Root acceptance is pending independent review.

