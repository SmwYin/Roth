# Roth.weight_mul_left — NO-mathlib-has-it

Canonical declaration 37, public theorem at Roth/Box.lean:110. The analogous generator-weight scaling law already exists as the scalar-preservation law of `Finsupp.bilinearCombination`. The parent `Roth.weight` is a reciprocal-real specialisation of `Finsupp.weight`; the representation bridge and complete scaling identity were independently checked. Mode B's re-aim rule therefore applies.

This is **not** a claim that the old theorem is definitionally identical to a mathlib theorem, nor a three-fact composition claim. Its old spelling needs four distinct algebraic facts, including `Nat.cast_mul` and `mul_comm`. All zero cases are retained.

## Phase 0 — baseline and provenance

The shared successful `lake build` is reusable: all 17 source/pin hashes freshly match the shared manifest. [Baseline](../evidence/Roth.weight_mul_left/baseline-build.txt), [fresh input check](../evidence/Roth.weight_mul_left/input-check.json), [source hashes](../evidence/Roth.weight_mul_left/source-hashes.json).

[Canonical metadata](../evidence/Roth.weight_mul_left/canonical-metadata.json) independently matches tracked declaration order, corrected manifest, and source head 110. Entire [Box module](../evidence/Roth.weight_mul_left/Box-source.lean.txt) and entire [Index caller module](../evidence/Roth.weight_mul_left/Index-source.lean.txt) were read. No production changes were made. The theorem has no sorry, unsafe, extra axioms, heartbeat changes, or proof placeholders.

## Phase 1 — exact content

For a natural multi-index d over a finite variable type, multiply every denominator parameter r(j) by the same natural l. The sum of the quotients d(j)/(l r(j)) equals the original sum divided by l. Division is real, including totalised division by zero; l=0 and any r(j)=0 are allowed.

Elaborated signature (native receipt):

```lean
Roth.weight_mul_left.{u_2} {σ : Type u_2} [Fintype σ] {l : ℕ}
    (r : σ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight (fun j ↦ l * r j) d = Roth.weight r d / ↑l
```

Parameters: σ an arbitrary universe-polymorphic variable type; `Fintype σ` provides the ambient enumeration; l a natural scalar, implicit; r natural denominator parameters; d a finitely supported natural multi-index. No DecidableEq or positivity hypothesis survives elaboration. Only project dependency: `Roth.weight`.

Proof: cast the product into ℝ, move common division through the finite sum, reassociate successive division as product denominator, and commute l with each r(j). A denominator zero contributes zero; l=0 makes both sides zero.

## Phase 2 — preliminary checks

**SMALL.** This is a helper identity, neither a named mathematical theorem nor listed in Box's Main results; no matching primary-plan target was found. It introduces no structure. The one-line-definition test is **n/a: theorem**; the one-line simp proof is not itself a verdict.

## Phase 3 — exhaustive literature protocol

Every named channel was actually attempted. There are three distinct general queries; the command's informal nine-channel label does not replace any named row.

| Channel | Exact query / locator | Result and mathematical relevance |
|---|---|---|
| General, current | Roth polynomial index scaling weights ind P alpha l r 1/l | Schmidt/Schlickewei Roth index sources located; reciprocal-weight context. |
| General, linear | linear combination scaling all vectors scalar linearity weighted sum | Boyd–Vandenberghe, Introduction to Applied Linear Algebra, §1.3; finite weighted linear combinations. Primary PDF open timed out; search locator retained, no PDF-content verification claimed. |
| General, aliases | weighted degree reciprocal weights rescaling multiindex Roth index | Mostly irrelevant index-weight results; no separate stronger theorem inferred. |
| ChatGPT mathematical MCP | Standard form, generality, historical evolution | n/a: ask_chatgpt_math unavailable in this session. |
| Local clean.tex | §4 lines 530–554 and 635–641 | Positive real denominator parameters, index as least nonzero Taylor weight; index scaling explicitly for l>0. |
| nLab | site:ncatlab.org/nlab linear combination module free module | Module/free-module universal-property discussion found. Primary free-module open rejected unsupported XHTML; search-level access only. |
| nCatLab | site:ncatlab.org/nlab weighted degree scalar multiplication | Graded-bundle discussion found; no independent categorical strengthening of this scalar sum identity. nCatLab and nLab share a host but were queried separately. |
| Stacks | site:stacks.math.columbia.edu graded algebra weights degree | Tag 00JL, §10.56, graded rings and weighted monomial degree sum; no reciprocal scaling law asserted there. |
| MathOverflow | site:mathoverflow.net Roth index weights polynomial | Weighted filtrations / Roth discussions found; no exact scalar-denominator law needed beyond linearity. |
| Recent arXiv, 2021-10-26 onward | site:arxiv.org Roth theorem weighted index polynomial 2022 2023 2024 2025 2026 | Salami, arXiv:2610.17589v1 (2026-10-13), §8, genuinely relevant; older/out-of-area hits rejected. |

Exact requests, returned response hashes/bytes, sanitised returned URLs and access limitations are in [web0](../evidence/Roth.weight_mul_left/web0-metadata.json), [web1](../evidence/Roth.weight_mul_left/web1-metadata.json), [web2](../evidence/Roth.weight_mul_left/web2-metadata.json), [web3](../evidence/Roth.weight_mul_left/web3-metadata.json), [web4](../evidence/Roth.weight_mul_left/web4-metadata.json), [web5](../evidence/Roth.weight_mul_left/web5-metadata.json), [web6](../evidence/Roth.weight_mul_left/web6-metadata.json), [web7](../evidence/Roth.weight_mul_left/web7-metadata.json), [primary opens](../evidence/Roth.weight_mul_left/web8-metadata.json), [arXiv §8 inspection](../evidence/Roth.weight_mul_left/web9-metadata.json). [Local excerpts](../evidence/Roth.weight_mul_left/caller-literature-excerpts.json).

Primary source locators: [Stacks 00JL](https://stacks.math.columbia.edu/tag/00JL); [Salami §8](https://arxiv.org/html/2610.17589v1#S8); [nLab module](https://ncatlab.org/nlab/show/module); [Boyd–Vandenberghe textbook](https://vmls-book.stanford.edu/vmls.pdf).

**Synthesis.** The classical object is the Roth index based on reciprocal parameter weights; the local paper uses positive real parameters. Its elementary monomial-weight scaling is finite linearity. The useful abstract version is linearity of the generator family in a finitely supported linear combination. The present totalised field identity is algebraic and does not require the positivity that the literature uses for order/index interpretations.

**Adversarial recent-paper check.** Salami's §8 counterexample concerns rescaling degree boxes using floor(d(j)/q(j)), with the resulting failure of an auxiliary-polynomial dimension argument when divisibility fails. It does not contradict uniform denominator scaling. Section 8 itself expresses the weighted index as a scalar multiple of ordinary vanishing index. We do not generalise this theorem to a degree-box existence assertion.

## Phases 4a–4b — generality

| Parameter/hypothesis | Current form | Literature / useful general form | Finding |
|---|---|---|---|
| σ | Type u | Arbitrary generator index set | Universe-polymorphic already; Finsupp abstract operation needs no finite ambient type. |
| Fintype σ | Full ambient sum | Finite support suffices | Fixed parent interface requires Fintype; dropping it from unchanged Roth.weight statement is ill-typed. Abstract representation extension verified separately. |
| DecidableEq σ | Absent | Not required | Section omission was verified by native type. |
| l | ℕ, may be zero | Arbitrary field scalar, and abstract module action | Field finite-set extension checked; no positivity introduced. |
| r | σ → ℕ, possibly zero | Arbitrary field denominators / reciprocal generator weights | Representation extension, not merely a class weakening of the unchanged definition. |
| d | σ →₀ ℕ | Semiring-valued finitely supported coefficients | General generator-family law supports semiring/module abstraction. |
| ℝ | Concrete real field | Field identity, or arbitrary additive module with commuting scalar actions | Algebraic proof uses no order/completeness. |
| Positivity | None | Classical index interpretation often requires positivity | Do not add it; l=0 and zero coordinates are valid. |

Within the unchanged parent interface, the theorem is maximally general in its hypotheses: nothing remains to drop. The broader representations were mechanically checked and are existing mathlib infrastructure, so this is not an unsupported YES-but-generalise-first claim.

## Phase 4c — nine modern-idiom checks

| # | Diagnostic | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses for bundled assumptions | Yes in abstract form: Semiring, AddCommMonoid, Module, SMulCommClass express linearity; no new instance is needed. |
| 2 | Filters/nets | No: finite algebraic sum, no topology. |
| 3 | Universal property | Yes: Finsupp linearCombination is the free-module extension; bilinearCombination bundles linearity in the generator family. It supplies map_smul directly. |
| 4 | Bundled substructures | Yes in the sense of bundled maps: use the existing LinearMap rather than a bespoke unbundled weight family law; map_smul API applies. No submodule lattice issue occurs. |
| 5 | Field to module hierarchy | Yes: generator scaling only needs commuting module structures; field inverses are confined to the reciprocal bridge. |
| 6 | Higher categories | No: no categorical coherence/limit content is present. |
| 7 | Concrete indices/scalars | Yes: arbitrary generator index and semiring coefficients eliminate ambient Fintype and natural-only restrictions. |
| 8 | Concrete-via-abstract | Fires: after unfolding weight once, its name disappears and only cast/sum/division facts remain. Abstract content is generator-family linearity, already bundled by bilinearCombination. |
| 9 | False-generalisation guard | Passed: reciprocal generator vector w(j)=r(j)⁻¹ yields exactly the same numerical weight. Coefficient scaling d↦c•d is a different law and is not used as the hit. Natural subtraction, order and degree-box existence are not asserted. |

The modern idiom enables `LinearMap.map_smul` without any Fintype, uses `Finsupp.weight`'s existing additive-map interface, and keeps natural reciprocals local to the number-theoretic application. This eliminates a duplicate API rather than creating an abstract synonym.

## Phase 4.5 — infrastructure risks

n/a: theorem; it defines no instance, coercion, or mathematical structure. All six risk dimensions checked:

| Risk | Result |
|---|---|
| Typeclass diamond | None: the theorem introduces no instance; existing module structures are explicit in the generic probe. |
| Reducibility leak | None: no new reducible definition; reciprocal bridge is proved, not treated as defeq. |
| Noncanonical unfolding | None introduced; old weight unfolds only explicitly in the bridge/inline proof. |
| Instance priority collision | None: no priority or instance declaration. |
| Universe polymorphism | None introduced; native type and generic probes retain arbitrary σ universe. |
| Coercion ambiguity | None introduced; natural casts and LinearMap evaluation are checked explicitly. |

## Phase 4.6 — five proof-strategy rows

| # | Question | Finding |
|---|---|---|
| 1 | Topology ε–δ versus filters | No topology. |
| 2 | Elements versus algebraic maps | Existing bilinearCombination.map_smul proves the re-aimed law; preferable after migration to canonical weight. |
| 3 | Sequences versus nets | No limiting argument. |
| 4 | Construction versus universal property | The free-module linear extension already exists; no new categorical machinery is needed. |
| 5 | Missing helper that mathlib should have | No mathematical gap established. A convenience spelling Finsupp.weight_smul would wrap an existing bundled law. |

Current short elementary proof is idiomatic locally. Refactor the mathematical interface toward existing bundled linearity when migrating the parent. No cost consideration influences the verdict.

## Phase 5 — all five actual mathlib searches

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Finder | denominator scaling query; misleading Int/Nat.sum_div near hits rejected | Finset.sum_div and Multiset.sum_map_div | Finsupp.weight, weight_apply, linearCombination; no exact-name discovery assumed |
| Loogle | Finset.sum_div | Finset.sum_div plus division-product pattern: no hit | Finsupp.bilinearCombination and bilinearCombination_apply exact signatures |
| LeanSearch | denominator scaling query; unrelated localization/Int/Nat hits rejected | Finset.sum_div | linearCombination and lmapDomain_linearCombination; not coefficient-scaling evidence |
| rg, pinned tree | weight_mul_left / weight_mul / weight_smul | sum_div and div_div in source | weight definition plus bilinearCombination and map/comp laws inspected |
| local search | weight | sum_div | bilinearCombination |

Complete receipts: [current Finder](../evidence/Roth.weight_mul_left/search-current-0.json), [current LeanSearch](../evidence/Roth.weight_mul_left/search-current-1.json), [current Loogle](../evidence/Roth.weight_mul_left/search-current-2.json), [current local](../evidence/Roth.weight_mul_left/search-current-3.json), [literature form](../evidence/Roth.weight_mul_left/search-literature.json), [abstract form](../evidence/Roth.weight_mul_left/search-abstract.json), [untruncated source searches](../evidence/Roth.weight_mul_left/source-search.json). The local tool reports index unavailable despite returning source-backed hits; it does not prove absence. External indices can differ from the pin; positive candidates were checked against local sources and native Lean.

**Positive candidate.** In Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:285, `Finsupp.bilinearCombination R S` is a linear map in the generator family. Its map_smul law says linearCombination R (c • w) = c • linearCombination R w. Since Finsupp.weight w is the additive hom underlying linearCombination R w, evaluating this equality at d is the exact analogous generator-weight law. The weight relationship is definitional here; the Roth-to-reciprocal-weight bridge is not.

```lean
exact congrArg (fun f : (σ →₀ ℕ) →ₗ[ℕ] ℝ => f d)
  ((Finsupp.bilinearCombination ℕ ℝ).map_smul c w)
```

This proof of the re-aimed weight scalar law is a single existing mathlib-law application with evaluation; no newly proved mathematical helper is being counted as an existing replacement. `linearCombination_smul` at line 221 is a product-index tensor formula and was explicitly rejected as the simple scalar-law candidate. Lower-bound `le_weight` and coefficient map_smul are also different results.

## Phase 5.5 — all three statement-shape checks

1. **Normal form.** Old denominator spelling, reciprocal Finsupp.weight spelling, and bilinearCombination.map_smul are equivalent here. Canonical upstream form is existing bundled generator-family linearity; old weight spelling requires a proved bridge. RHS is naturally the scalar action on the original value. No pairwise family of conversion lemmas is proposed.
2. **Syntactic generality.** Division by l and multiplication by l⁻¹ are equivalent; the actual consumer wants inverse-scalar multiplication inside a set image. A native Set.image scalar-equality fragment verifies that form. Multiplying the equation by l would lose information at l=0; do not replace the theorem by that non-equivalent cancellation form.
3. **Superfluous parameters.** Native signature has no DecidableEq. Fintype is used only by the old parent; no unverified deletion is claimed. Every remaining variable occurs in the statement; no positivity is needed.

## Phase 6.0 — callers and inline audit

| Explicit caller | Use | Refactor |
|---|---|---|
| Roth.index_mul_left_weights, Index.lean:200 (reference 206) | Pointwise weight equality under Set.image_congr, then real sInf scalar compatibility | After migrating weight to reciprocal Finsupp.weight, rewrite reciprocal generator family and evaluate bilinearCombination.map_smul. Preserve the existing nonnegative scalar/sInf step. If retaining the old interface temporarily, inline the exact sum/division normalization at that one point. |

K=1 explicit source caller. No other inline rediscovery found by untruncated source search. These are source-level references, not exhaustive opaque kernel or simp dependency closure. The theorem is not tagged simp; no dead-code claim is made. The whole Index module was read to verify the consumer's purpose.

## Phase 6 — actual composition experiments

**Old syntax**, after unfolding only the parent definition:

```lean
simp only [Nat.cast_mul, Finset.sum_div, div_div, mul_comm]
```

Four distinct nondefinitional facts: (1) Nat.cast_mul, (2) Finset.sum_div, (3) div_div, (4) mul_comm. Finsupp is not unfolded into a new invented helper. Full simp syntax in the original source hides Nat.cast_mul, so counting only its written list would be wrong. This is **not** a ≤3-fact NO-composable certificate. Under Phase 6b, the closing simp would otherwise leave a convenience-API judgment.

**Re-aimed syntax**, however, is exactly an existing scalar-preservation law. The native experiment proves: old sum = Finsupp.weight reciprocal; reciprocal family at l*r equals l⁻¹ • old reciprocal family; generator_scale follows from bilinearCombination.map_smul; together these recover the old theorem. Generic semiring/module and field finite-set experiments check wider representations. These checked normalizations do not alter the re-aim verdict gate.

**Zero cases.** Nothing is cancelled and all inverse/division laws are totalised. l=0 and any/all r(j)=0 remain allowed throughout. An empty variable type is also covered. Negative real scalars in the field extension are allowed because no ordering is used.

[Native verification inventory](../evidence/Roth.weight_mul_left/verification.json) links exact executed sources, terminal successful receipts and standard-axiom checks. Rejected import-incomplete attempts are retained separately and are not accepted proof evidence. Native caller experiment is a complete Set.image equality fragment matching the actual consumer; it is not a rewritten production Index module.

## Phases 7–8 — actionable verdict

**NO-mathlib-has-it**, via independently verified parent re-aim. The parent was already assessed NO-mathlib-has-it because Finsupp.weight is more general; the dependent generator-scaling law is supplied by the existing `Finsupp.bilinearCombination.map_smul` operation. The reciprocal bridge requires real algebra, but that does not change the analogous-law result.

Action: do not propose this old Roth-specific theorem upstream. During the parent migration, replace its sole Index call with the existing generator-family scalar law plus reciprocal normalization, then remove the redundant local theorem. If the old denominator interface is retained, Roth/Box.lean remains the appropriate local destination for the convenience theorem; its one actual consumer explains its local readability. No upstream PR grouping/reviewer selection is applicable to a NO verdict.

No mathematical verification issue remains. No judgment question is needed to complete this read-only assessment. Production migration and an upstream convenience-wrapper taste decision are separate from the completed assessment.
