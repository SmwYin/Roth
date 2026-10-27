# Roth.index_rename

**Verdict: NO-composable-from-mathlib.** Re-aiming the parent index at projected `AddMonoidAlgebra.infDegree` reveals a two-call proof from existing support transport and `Finset.inf_image`. The old centered, reciprocal-weight interface needs a separately verified normalization bridge; it is not definitional. No existing named infDegree renaming theorem was established, so the verdict does not claim NO-mathlib-has-it.

## Phase 0 — Baseline

The [successful baseline build](../evidence/Roth.index_rename/baseline-build.txt) is reusable: All17 source/pin hashes were freshly recomputed and match the shared manifest, as recorded in [inputs](../evidence/Roth.index_rename/inputs.json). Target is public theorem Roth/Index.lean:212, without sorry. The entire declaring module, supporting Taylor/weight definitions, and full Theta caller module were read. The module defines and develops the weighted minimum of Taylor support. Production files, pins and Git remain unchanged.

## Phase 1 — Mathematical content and full native type

Renaming variables along an injection preserves a polynomial's centered weighted index, provided the center and denominator weights on the old variables are pulled back along the same injection. This includes adjoining unused variables and permutations. The polynomial and denominator entries may be zero.

```lean
Roth.index_rename.{u_1, u_2} {σ : Type u_1} [Fintype σ]
    {τ : Type u_2} [Fintype τ] {f : σ → τ} (hf : Function.Injective f)
    (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) :
    Roth.index ((MvPolynomial.rename f) P) α r = Roth.index P (α ∘ f) (r ∘ f)
```

σ,τ index variables; their Fintype instances support the current global-sum weight interface. f transports variable names; hf prevents merging distinct monomials and coefficient cancellation. P is the polynomial, α the new-variable center, r the new-variable natural denominator vector. The proof commutes translation with rename, identifies support as the image under `Finsupp.mapDomain f`, and uses weight compatibility before applying congruence to sInf. Its original kernel dependencies include the direct rewrite API `Roth.index`, `MvPolynomial.taylor_rename`, and `Roth.weight_mapDomain`, together with the construction constants `MvPolynomial.taylor` and `Roth.weight` exposed after unfolding index; the overview dependency list retains both kinds. [Full executed original](../evidence/Roth.index_rename/index-rename-original-executed.lean.txt) and [raw native/audit receipt](../evidence/Roth.index_rename/index-rename-original-audit-receipt.json) retain the exact elaborated type, full kernel print with no elision and standard axioms.

## Phase 2 — Preliminary checks

**SMALL:** a naturality/helper law; it introduces no new structure and is not a named major theorem. Literature search remains exhaustive. One-line-definition check: n/a, the declaration is a theorem. It is not glue (`rfl`): the proof transports support and the numerical weight function explicitly.

## Phase 3 — Exhaustive literature protocol

Exact requests, response SHA256/bytes/status and source locators with concise original summaries are preserved, without full article or search-result bodies. Returned URL query strings were stripped in metadata; no credential values are persisted.

| Channel / actual query | Result and locator |
|---|---|
| Specific general web: `polynomial index weighted order invariance embedding variables Roth theorem` | Classical Roth index identified. Princeton lecture17 Definition17.1.1; Min Ru p3; Roth ICM1958. [Receipt](../evidence/Roth.index_rename/web-general.json). |
| General form web: `weighted order polynomial minimum support pullback injective variable renaming` | Weighted monomial orders and polynomial pullbacks adjacent; no new exact law inferred. Same receipt. |
| Alias web: `Roth lemma index polynomial adjoining dummy variables` | Acta1996 *Multiplicities of recurrence sequences* p217 explicitly regards V in m−1 variables as polynomial in m variables while retaining its Roth index. Search snippet only; direct PDF fetch timed out400. Same receipt and [open metadata](../evidence/Roth.index_rename/web-primary.json). |
| ChatGPT MCP | n/a: ask_chatgpt_math unavailable; no fabricated consultation. |
| Local manuscript clean.tex | [Actual search](../evidence/Roth.index_rename/local-literature-search.json), [§4 excerpt](../evidence/Roth.index_rename/clean-index-excerpt.tex.txt). Lemma4-2 proof says embedded translated monomials have zero exponent in the added variable, so index is unchanged; Lean note requests variable-renaming invariance. |
| nLab: `site:ncatlab.org/nlab weighted polynomial valuation` | Valuation and polynomial pages give minimum-exponent/monoid-algebra context, including infinity at zero. [Receipt](../evidence/Roth.index_rename/web-labs-stacks.json). |
| nCatLab: `site:ncatlab.org/ncatlab weighted polynomial variable renaming` | Distinct namespace actually queried. Returned nLab/logic pages outside namespace; no exact nCatLab hit. Same receipt. |
| Stacks: `site:stacks.math.columbia.edu polynomial ring variables injection` | 0G8R is a Rees-algebra example, not index invariance. Supplementary primary00DM describes polynomial algebras as symmetric algebras on finite free modules; no exact transport theorem. Same search and primary receipts. |
| MathOverflow: `site:mathoverflow.net weighted order polynomial variable embedding valuation` | Questions476147 and87994 discuss weighted monomial orders and extension, not this support-minimum law. [Receipt](../evidence/Roth.index_rename/web-mo-arxiv.json). |
| Recent arXiv within five years: `site:arxiv.org Roth polynomial index weighted order 2022 2023 2024 2025 2026` | Salami2610.17589 (13Oct2026), §8 defines generalized weighted Roth index. 2210.04347 concerns additive-combinatorial Roth and is irrelevant. Same receipt; [actual §8 open](../evidence/Roth.index_rename/web-section8.json). |

Primary current supporting source [Salami2026 §8](https://arxiv.org/html/2610.17589v1#S8) defines the weighted index by the minimum of weighted normalized derivative orders. Its Proposition8.2 disproves a separate existence assertion with floored anisotropic degree bounds; it does not contradict renaming invariance. [Stacks00DM](https://stacks.math.columbia.edu/tag/00DM) supplies abstract polynomial-algebra context, not a claimed proof of this law. The [Acta1996 PDF locator](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6531-11511_2006_Article_BF02551582.pdf) supports an explicit historical embedding use through its returned search excerpt, with direct-fetch failure disclosed. Princeton direct fetch also timed out400.

Concept: naturality of weighted order of vanishing under injective variable changes. Classical sources use positive real/integer denominators and index0=∞; the project extends zero denominators by total division and sets index0=0. Finite support, not finiteness of the variable type, drives the abstract identity. No categorical or literature absence claim follows from unsuccessful channels. [Literature summary](../evidence/Roth.index_rename/literature-summary.json).

## Phase 4a — Every parameter and generality dimension

| Parameter/hypothesis | Current form | Broader verified representation / limitation |
|---|---|---|
| σ,τ | arbitrary universes, finite variable types | Generic transport and combined expanded weighted law use arbitrary types without Fintype. |
| Fintype σ and Fintype τ | needed to form unchanged weight/index expressions | Removing instances from the unchanged signature is not a valid mechanical weakening. Finite coefficient support suffices after parent restatement. |
| P | real multivariate polynomial | Generic core and expanded centered law use CommSemiring R, with no field, domain, characteristic or nonzero requirement. |
| f | arbitrary map between variable types | Preserve same map in exponent transport, center and weights. Surjectivity not needed; arbitrary embeddings supported. |
| hf | globally injective | Essential for the uniform equality: collision guard sends X0−X1 to zero along Fin2→Unit while source index remains nonzero at zero with positive weights. A support-relative injectivity statement might be separately useful, but was not claimed verified. |
| α | arbitrary τ→ℝ | Generic centered law uses τ→R, pulls back α∘f; no sign/positivity condition. Removing or failing to pull back the center changes the object. |
| r | arbitrary τ→ℕ, possibly zero | Expanded form uses arbitrary direct weights w:τ→M; original is reciprocal natural weights. Weight transport alone needs no injection. |
| ℝ output | sInf∅=0 | Generic degree target T is SemilatticeInf + OrderTop; combined weighted form uses WithTop M and untopD0, retaining the project's zero convention. |

## Phase 4b — Generality verdict and actual experiments

**MAXIMALLY GENERAL within the fixed Roth.index parent interface:** there are no positivity/nonvanishing hypotheses to drop. Fintype instances are formation constraints of that parent. Broader coefficient and weight types require a representation change, not a claim of a single mechanical edit. The isolated proof actually compiles for arbitrary universes, CommSemiring coefficients, arbitrary degree maps and infimum semilattices with top. The combined expanded centered-weight law compiles for arbitrary variable types, CommSemiring R and AddCommMonoid M with SemilatticeInf M. Those are tested sufficient assumptions, not an unsupported claim of logical minimality.

The [isolated exact mathlib proof](../evidence/Roth.index_rename/index-rename-mathlib-final-executed.lean.txt) / [receipt](../evidence/Roth.index_rename/index-rename-mathlib-final-receipt.json), [actual bridge](../evidence/Roth.index_rename/index-rename-bridge-executed.lean.txt) / [receipt](../evidence/Roth.index_rename/index-rename-bridge-receipt.json), and further caller/guard evidence certify the statements. No existing own-target theorem is used in the accepted replacement. The collision guard rejects dropping hf in the uniform claim. Zero-polynomial and zero-weight specializations compile without added assumptions.

## Phase 4c — All nine modern-idiom rows

| # | Diagnostic | Applies / consequence |
|---|---|---|
| 1 | Typeclasses for preambles | Already use algebra/order classes in abstract law; no new custom predicate or instance needed. hf is a property of a particular map; keeping it explicit is conventional. |
| 2 | Sequences/metrics to filters | No: finite support identity has no convergence. |
| 3 | Construction to universal property | Center compatibility follows the polynomial aeval universal substitution API (`rename_eq_aeval`, `comp_aeval_apply`); no new universal-property class. |
| 4 | Closure-predicate sets to bundled structures | No closed subobject is constructed. An embedding parameter could bundle f/hf, but support theorem already takes Injective f and matches callers directly. |
| 5 | Field/vector-space hierarchy | Yes in expanded representation: CommSemiring R is enough; arbitrary coefficient semirings share the transport law. |
| 6 | Higher category | No higher-categorical mathematical content or coherence requirement. |
| 7 | Concrete numerical degree | Yes: arbitrary semilattice-inf/top target T; arbitrary additive direct weights M in combined law. Finset.inf_image composes with any degree map. |
| 8 | Concrete-via-abstract | Fires. After the initial `rw [index, index, ...]`, index does not recur in the remaining proof body; the remaining steps are sInf congruence and weight compatibility. Replace centered index with finite coefficient-support infimum. This enables direct Finset lattice API. |
| 9 | False-generalization guard | Preserve injectivity at support transport, pull back both center and weights, and keep WithTop until projecting empty support to0. Colliding variables can cancel; weightedTotalDegree is a maximum, not the same object; replacing index0=0 with∞ is not silent equivalence. |

Modern idiom: **yes**, projected infDegree and additive Finsupp weights. This removes repeated global-set minimum machinery and permits arbitrary variable types. It is a representation adapter around existing mathematical building blocks, not proof of a new named law already present.

## Phase 4.5 — Infrastructure risk

n/a: target is a theorem. All six definition-only rows (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe computation, coercion ambiguity) are n/a because this theorem introduces neither definitions nor instances/coercions. Scratch proof names are evidence only.

## Phase 4.6 — All five proof-strategy rows

| # | Strategy question | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Element algebra versus point-free maps | Prefer support-image equality followed by congrArg finite-inf and Finset.inf_image; weight compatibility is existing linearCombination_mapDomain. |
| 3 | Sequences versus nets | n/a, finite support only. |
| 4 | Explicit objects versus universal properties | aeval/rename substitution composition handles center compatibility directly; no object construction required. |
| 5 | Missing helper API mathlib should supply | No essential missing mathematical helper: support_rename_of_injective, inf_image, linearCombination_mapDomain and aeval substitution suffice. A discoverability-only infDegree_rename wrapper is at most a separate API-design question, not a new theorem contribution justified here. |

Strategy: **MATHLIB-IDIOMATIC locally; REFACTOR-RECOMMENDED with parent migration**. The current source image argument is sound; generic proof eliminates repeated real-sInf normalization. Cost does not determine the verdict.

## Phase 5 — Actual five-method searches on all three forms

[Raw formal requests/responses](../evidence/Roth.index_rename/formal-search.json) record all four remote/name methods separately on current, literature-standard and abstract forms; [current rg](../evidence/Roth.index_rename/rg-current.json), [literature rg](../evidence/Roth.index_rename/rg-literature.json), and [abstract rg](../evidence/Roth.index_rename/rg-abstract.json) supply the fifth method on pinned sources.

| Method | Current form | Literature weighted-order form | Abstract form |
|---|---|---|---|
| Finder | weightedTotalDegree_rename_of_injective and degreeOf_rename_of_injective, adjacent maxima | weightedTotalDegree rename, weightedOrder substitution inequality | exact Finset.inf_image, nonempty inf'_image and complete-lattice variants |
| Loogle | exact support_rename_of_injective signature | exact linearCombination_mapDomain signature | exact Finset.inf_image signature |
| LeanSearch | rename/aeval and univariate Taylor families | weightedOrder, homogeneous and weightedTotalDegree APIs | exact Finset.inf_image/inf_map/inf'_image |
| rg pinned source | support_rename and project-name patterns | weight and weightedOrder/degree rename families | infDegree definition and finite-inf image families |
| Local name search | support_rename_of_injective found | linearCombination_mapDomain found | no inf_image item; index unavailable |

Local unavailable indexing is a limitation, not absence evidence. Remote signatures may differ by revision; accepted pinned-native proof checks the actual usable APIs. Positive candidates: `MvPolynomial.support_rename_of_injective` at Mathlib/Algebra/MvPolynomial/Rename.lean:381; `Finset.inf_image` is generated by to_dual from sup_image in Mathlib/Data/Finset/Lattice/Fold.lean:66; `Finsupp.linearCombination_mapDomain` at Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158. `AddMonoidAlgebra.infDegree` at Degree.lean:624 is an abbreviation of coeff.support.inf. Existing weightedTotalDegree_rename_of_injective concerns a maximum in natural degree, so it is not used as the replacement. No named infDegree_rename theorem is asserted absent absolutely; the demonstrated two-call composition suffices for the verdict.

## Phase 5.5 — All three statement-shape checks

**Normal form:** projected infDegree of the translated polynomial, with its finite support and weight map made explicit. Equivalent forms are real image-sInf, nonempty Finset.inf', and finite inf into WithTop followed by untopD0. For the re-aimed law, RHS is the original polynomial with degree function composed with mapDomain. The local RHS correctly pulls back both α and r.

**Syntactic generality:** attempted unweighted arbitrary degree transport, arbitrary additive direct weights, and actual old-interface replacement. All compiled. The hypothesis Injective f matches both equivalence and Option.some callers without requiring surjectivity. An embedding-bundled spelling adds no mathematical benefit here.

**Superfluous arguments:** σ,τ/universes are generic. Fintype σ/τ belong to unchanged parent formation; they disappear only after expanded restatement. P, α and r genuinely determine the object. f is essential, hf prevents cancellation. There is no nonzero/positive premise to drop. Overall **RESTATE-BEFORE-SHIP toward existing finite-support API**; do not add the Roth-specific statement upstream.

## Phase 6.0 — Complete callers and inline audit

[Ignore-safe rg plus git grep](../evidence/Roth.index_rename/complete-caller-search.json) and [fresh lexical enumeration of the canonical production inventory](../evidence/Roth.index_rename/lexical-enumeration.json) find **three proof applications on two source lines**, two private callers, one external-to-file module, zero statement applications. A module-docstring reference is counted separately. The exact ordered293-name kernel-value audit finds the same two direct consumers; source occurrences and direct kernel dependency closure are distinct measurements.

| Caller | Source / applications | Refactor plan |
|---|---|---|
| private Roth.indexSet_comp_subset | Theta.lean:154 / one | Replace index_rename e.injective in the terminal simp with the verified bridge; preserve coefficient map commutation and function composition simplification. |
| private Roth.index_separated_mul_le_aux | Theta.lean:442 / two | Replace both rw entries with bridge specializations for Option.some and Unit→none. Preserve product-index proof and later scaling/logarithmic estimate. |

Full exact caller replays change only copied declaration names, one necessary line wrap, and the three target applications. [Full executed caller/guard/expanded source](../evidence/Roth.index_rename/index-rename-callers-guards-expanded-clean-executed.lean.txt) and [clean native receipt](../evidence/Roth.index_rename/index-rename-callers-guards-expanded-clean-receipt.json) retain the actual execution. They retain the complete proof and all parameters, including real coefficient-map injectivity. [Caller plans](../evidence/Roth.index_rename/callers.json) and [inline search](../evidence/Roth.index_rename/rg-inline.json) are explicit. The inline audit identifies supporting Taylor/weight naturality and explicit callers, not a separate re-derivation bypassing this target. This is useful API, not junk/dead code; external downstream use is not established by local searches.

## Phase 6 — Actual composition and normalization

The re-aimed law has exactly two existing mathlib mathematical calls, plus equality congruence/transitivity:

```lean
exact (congrArg (fun s : Finset (τ →₀ ℕ) ↦ s.inf D)
  (MvPolynomial.support_rename_of_injective (p := P) hf)).trans
    (Finset.inf_image P.support (Finsupp.mapDomain f) D)
```

This is the accepted isolated `IndexRenameMathlib149.transport`. It works at the actual canonical parent infDegree and does not pretend there is an existing named infDegree renaming law. Weight transport is one existing call `Finsupp.linearCombination_mapDomain ℕ (v' := w) f d`; no injection is needed for that weight-only identity. Center compatibility is an independently checked terminal simp composition through aeval/rename. Under Phase6b, such a closing simp is **BORDERLINE** when considered alone, not automatic evidence of a ≤3-call result.

The old centered reciprocal-weight target is **not demonstrated in ≤3 existing mathlib calls**: it needs the actual parent bridge and center/weight normalization. Those are new adapter proofs, not existing mathlib calls. The verified bridge unfolds to arbitrary direct weights and then applies transport; it uses neither Roth.index_rename nor the project Taylor/weight rename lemmas, so no own-target circular proof is hidden. Generic core is **COMPOSABLE, two calls**, and the canonical parent is already assessed against infDegree. This supports NO-composable rather than inventing a further re-aim to claim a one-call NO-mathlib-has-it verdict.

The collision experiment mechanically guards the essential hf premise: Fin2→Unit merges X0 and X1, so rename(X0−X1)=0; at zero with all denominators1, original nonzero P evaluates to0 and has nonzero index. Zero-polynomial and zero-weight boundary cases separately compile. The expanded theorem certifies arbitrary coefficients/weight targets and infinite variable types via finite support. No recovered sorryAx or raised elaboration limits are accepted.

## Phase 7 — Actionable verdict

**NO-composable-from-mathlib.** Existing building blocks are support_rename_of_injective and Finset.inf_image for the re-aimed infDegree law, linearCombination_mapDomain for weights, and rename_eq_aeval/comp_aeval_apply for centered substitution. The exact two-call term above is the required actionable composition. This result is not selected by cost, weak literature search, or a claim that all old normalization is definitional.

Refactor every explicit caller as listed in Phase6.0. With the current project interface, a local compatibility adapter can remain in Roth/Index.lean until parent migration; it must not be counted as an existing mathlib theorem. After migrating index to projected infDegree and weights to Finsupp.weight, inline the two-call transport at the equivalence and separated-variable sites, retaining actual center/weight conversions where needed. The independently verified bridge and full copied caller replays make that proposal reviewable. Alternative local destination: a private helper next to the Theta consumers if the public compatibility API is later removed.

No upstream PR for Roth.index_rename is proposed; therefore YES-only location/title/reviewer/grouping requirements are n/a. Any future generic infDegree rename convenience theorem would need its own API justification beyond these two existing calls. No user decision is pending, and no verification issue remains unresolved.

## Phase 8 — Evidence and verification

[Verification registry](../evidence/Roth.index_rename/verification.json) lists exact accepted executed sources and raw receipts, rejected attempts separately, source hashes, region starts and required target-specific diagnostics. Canonical audit is293 requested/293 unique/293 present/293 kernel values in tracked declaration order, including private names. Original full kernel print has no elision. Accepted proofs use only propext, Classical.choice and Quot.sound. Independent old-target-free bridge, arbitrary expanded representation, full caller replays and collision/boundary guards are native checked. No production file was modified.

[Assessment metadata](../evidence/Roth.index_rename/assessment.json), [overview entry](../evidence/Roth.index_rename/overview-entry.json), [current copy manifest](../evidence/Roth.index_rename/copy-manifest.json), and [portable read-only validator](../evidence/Roth.index_rename/validate.py) complete the package. The validator checks scratch/integrated links, exact ordered canonical names, source/pin and current manifest hashes/bytes, clean nonpartial native results, standard axioms, required phase rows, full caller replays and credential safety. Historical worker manifests never replace validation of the current manifest.
