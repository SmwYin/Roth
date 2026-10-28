# Roth.lem6Φ — full mathlibable assessment

Canonical183, `Roth/Theta.lean:275`. **NO-composable-from-mathlib** for a standalone upstream definition. Retain this useful arithmetic abbreviation locally in `Roth/Theta.lean`; any future deletion should inline the displayed two summands at every caller. Production files are unchanged. This is an independent assessment, not inheritance from the earlier Θ/indexSet assessments.

## Phase 0 — baseline

The recorded baseline `lake build` succeeded with2467 jobs. All17 source/pin hashes freshly match the shared baseline. Original native resolution, full type/body and standard axioms are clean, with all293 canonical names present in exact order and293 distinct names. Five direct kernel-value and four direct kernel-type consumers were independently enumerated. This is a public noncomputable definition, with no sorry.

Evidence: [baseline](../evidence/Roth.lem6Φ/baseline-build.txt), [fresh hashes](../evidence/Roth.lem6Φ/source-hashes.json), [original native](../evidence/Roth.lem6Φ/lem6phi183-original-receipt.json), [exact audit source](../evidence/Roth.lem6Φ/lem6phi183-audit-executed.lean.txt).

## Phase 1 — comprehend

Φ is the sum of the supremum of permitted indices in the distinguished last variable and the supremum of permitted indices in the remaining variables. Both families use the same integer coefficient bound M and degree weights multiplied by l. Rational evaluation points have prescribed natural denominators and integer numerators individually coprime to those denominators. The definition supplies bookkeeping for bounding the index of a product in separated variables, and subsequently for the numeric maximum in Roth Lemma6.

Full native type:

```lean
{τ : Type u_2} → [Fintype τ] →
  (Option τ → ℕ) → (Option τ → ℕ) → ℝ → ℕ → ℝ
```

Source with its mathematical argument names:

```lean
noncomputable def lem6Φ (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ :=
  Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) +
    Θ M (q ∘ some) (fun j ↦ l * r (some j))
```

τ is the complementary variable type; q contains denominators; r contains weights; M is an arbitrary real coefficient bound; l is an arbitrary natural scaling factor. There are no positivity, nonempty-type, nonzero-weight or denominator hypotheses. The section's `DecidableEq τ` is omitted in the actual elaborated type. Its immediate project dependency is Θ, which itself refers to indexSet/RSet/index. The entire985-line declaring module and every actual source caller were read. The module defines the index supremum and proves Lemmas5–7. The definition has an expression body, not a mathematical proof.

## Phase 2 — preliminary checks

SMALL: a local auxiliary quantity, although listed among the module's main definitions; it introduces no new mathematical structure and is not itself a main theorem. One substantive expression line in the original source, so ONE-LINER WITH-EXEMPTION for semantic/API intent. No defeq-barrier exemption: `rfl` unfolds it, and the caller explicitly rewrites it. No typeclass-diamond exemption: its result is an existing real number. The semantic exemption is concrete: index_det_le, index_le_lem6 and Θ_option_le use the short name in substantial statements, and the separated-product and induction proofs unfold it. The exemption supports local retention, not a new universal arithmetic API.

## Phase 3 — exhaustive literature

Exact requests, response hashes/bytes, returned locators and original concise summaries are preserved; full search/article bodies are not archived. The command's named channels were all executed, with three distinct general-web queries. The optional mathematical ChatGPT tool is unavailable. Searches are evidence of identified concepts, never proofs of absence.

| Channel | Actual query or locator | Result and relevance |
|---|---|---|
| General web: specific | `Roth theorem auxiliary polynomial index Phi Theta lemma 6 sum suprema` | Princeton lecture17 and classical index references; exact Φ is identified in local source eq15. |
| General web: broader | `Diophantine approximation polynomial index supremum separate variables sum` | Weighted vanishing and separated factors, not a distinct canonical named sum. |
| General web: aliases | `Roth lemma index lemma Dyson auxiliary polynomial height` | Roth/Dyson alternatives and original index constructions; same context rather than a standalone Φ concept. |
| ChatGPT math | unavailable | Optional tool not provided; no fabricated answer. |
| Local references | clean.tex §5 Lemma6 eq15, lines719–723 | Exact two-supremum formula, with M specified by eq16. |
| nLab | `site:ncatlab.org/nlab supremum addition` | join/supremum concepts; no exact arithmetic Φ. Direct join page access failed400 unsupported XHTML; only returned search material used. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial index supremum`; retry `site:ncatlab.org/ncatlab "supremum" "addition"` | Results mostly /nlab, outside requested /ncatlab namespace; no exact namespace hit. No categorical reformulation inferred. |
| Stacks | `site:stacks.math.columbia.edu polynomial multiplicity order vanishing`; direct tag00NN | Local-ring graded vanishing context, without these bounded integer polynomial/coprime families. Not a replacement. |
| MathOverflow | `site:mathoverflow.net Roth theorem polynomial index lemma` | Question431381 concerns replacing Roth's lemma by Dyson's lemma; not this auxiliary definition. |
| Recent arXiv | `site:arxiv.org Roth theorem polynomial index after:2021-10-27 before:2026-10-28`; targeted survey title | Many combinatorial Roth results are irrelevant. Goel–Lunia–Ray arXiv2502.00731 is a relevant2025 survey, revised2026-07-21, concerning classical index machinery. |

Primary locators: [Princeton Chapter17](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), [Goel–Lunia–Ray](https://arxiv.org/abs/2502.00731), [Stacks00NN](https://stacks.math.columbia.edu/tag/00NN), [MathOverflow431381](https://mathoverflow.net/questions/431381/dysons-lemma-implies-index-is-small-in-proving-roths-theorem). Direct Princeton PDF fetch timed out; its search excerpt is supplemental, not a claimed full-text reading. The survey abstract was directly accessed; index Definition2.19 and multiplicativity Lemma2.22 were located in the search-returned primary repository excerpt. The exact Φ standard form rests on local clean.tex, not on these broader analogues.

Literature synthesis: this is a proof-local auxiliary sum of two extremal weighted indices. The local source fixes finite integer-polynomial families, positive degree weights and denominators in its theorem; Lean totalizes the definition beyond those theorem hypotheses. No independent universal naming or broader Φ construction was established. The standard mathematical operation underlying the packaging is ordinary addition of two suprema.

Evidence: [local source](../evidence/Roth.lem6Φ/clean-lem6-excerpt.tex.txt), [web0](../evidence/Roth.lem6Φ/web-0.json), [web1](../evidence/Roth.lem6Φ/web-1.json), [web2](../evidence/Roth.lem6Φ/web-2.json), [web3](../evidence/Roth.lem6Φ/web-3.json), [primary access](../evidence/Roth.lem6Φ/web-primary.json).

## Phase 4a — parameters and generality

| Parameter | Role, necessity and verified scope |
|---|---|
| τ : Type u | Arbitrary complementary variable type; universe-polymorphic. Empty and higher-universe examples compile. No Nonempty hypothesis. |
| Fintype τ | Needed by the fixed Θ/index parent interface; not inherent in the outer sum-of-suprema constructor. Independently expanded both families to infDegree and aeval; expanded construction compiles with no Fintype at all. This is representation expansion, not a proposed new upstream definition. |
| DecidableEq τ | Absent from the actual native type; project checks do not add it. |
| q : Option τ → ℕ | Prescribed denominators; none/some genuinely separate one variable from the complement. Zero denominators compile and retain Lean real division conventions. |
| r : Option τ → ℕ | Degree bounds and reciprocal weights; zero values are already allowed. Replacing this natural degree vector by arbitrary real weights changes the coefficient-degree family unless the two roles are separated. |
| M : ℝ | Real bound on all integer coefficients; arbitrary M already allowed, including negative values and empty families. General ordered targets make sense only for the outer constructor, not as automatic replacements for the arithmetic object. |
| l : ℕ | Simultaneous natural degree scaling; zero compiles. Changing l to a real changes the degree bounds. |

No actual mathematical hypotheses can be dropped: there are none. Finite-type removal is verified after expanding the fixed parents, not claimed to be a mechanical edit to this original declaration.

## Phase 4b — generality verdict

MAXIMALLY GENERAL relative to its fixed arithmetic parent interfaces and source's finite-variable setup. The outer constructor is strictly more general as `Add.add (sSup s) (sSup t)` over any `[SupSet A] [Add A]`, which already exists as a three-call expression. The expansion to arbitrary variables was actually verified; it does not warrant YES-but-generalise-first because the generic operation already exists and the full arithmetic interface change is not a new one-edit result. Both complete RSet constraints and both coprime numerator families are preserved in the executed project expansion, not erased as “arbitrary sets”.

Evidence: [independent project execution](../evidence/Roth.lem6Φ/lem6phi183-project-executed.lean.txt), [clean project receipt](../evidence/Roth.lem6Φ/lem6phi183-project-receipt.json), [isolated generic execution](../evidence/Roth.lem6Φ/lem6phi183-isolated-executed.lean.txt).

## Phase 4c — nine modern-idiom checks

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Bundled hypotheses to typeclasses | No bespoke structure hypotheses. Existing Fintype parent interface is explicit. |
| 2 | Sequences/metrics to filters | No convergence or metric reasoning. |
| 3 | Construction to universal property | SupSet already supplies the supremum operation; adding a new class for this sum would add redundant infrastructure. |
| 4 | Closed sets to bundled substructures | RSet is an admissibility set, not a submodule: zero excluded and bounded coefficients not closed under addition. |
| 5 | Field-specific to weaker hierarchy | Yes for the outer expression only: SupSet+Add suffice, verified in isolation. Existing operations already expose this generality. |
| 6 | Higher categories | No categorical mathematical content. |
| 7 | Concrete indices to arbitrary structures | Natural l/r encode integer degree bounds. Arbitrary weights require separating degree and weight data; not the same one-edit object. |
| 8 | Concrete-via-abstract diagnostic | The full expression has two Θ occurrences and one addition, with no intervening proof. After expanding Θ it is precisely the same sum-of-suprema constructor. The abstraction is existing sSup/Add, not a new theorem. Source body and exact expansion were inspected. |
| 9 | False-generalization guard | Preserving both admissibility sets, coprimality and real totalization passes. Replacing reals by ENNReal/EReal, or replacing the two families by one without hypotheses, changes empty/unbounded behavior and is rejected. |

Modern idiom is available and already implemented by generic operations. Use it directly; downstream lattice and addition APIs apply without inventing a Φ class. No cost-based downgrade is used.

## Phase 4.5 — six infrastructure risks

| Risk | Verdict | Evidence |
|---|---|---|
| Typeclass diamond | NONE | A value of ℝ, not an instance; existing SupSet ℝ and Add ℝ synthesis succeeds. |
| Reducibility leak | LOW | Ordinary semireducible def, no reducible annotation; constructor/literal equalities close by rfl. No instance is unfolded through this value. |
| Noncanonical unfolding | LOW | `simp only` does not automatically unfold it; named rewriting is deliberate at449 and927. It exposes the two established parent forms. |
| Instance priority | NONE | No instance declaration or priority introduced. |
| Universe | NONE | Native type is universe-polymorphic; Empty and ULift at higher universe compile. Expanded arbitrary-variable form is verified. |
| Coercion ambiguity | NONE | No CoeFun/CoeSort is declared; a CoeFun ℝ synthesis failure is guarded as expected. |

Overall LOW, with no HIGH rows. Local semantic clarity and stable caller API are the relevant reasons to retain the name.

## Phase 4.6 — five proof-strategy rows

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | Not applicable: expression definition, no topological argument. |
| 2 | Elements versus subobjects | No elementwise algebra proof. RSet's constraints are not a substructure. |
| 3 | Sequences versus nets | Not applicable: no limit. |
| 4 | Explicit categorical construction | Not applicable: no universal categorical object. |
| 5 | Missing helper API | None for the outer Φ construction. The expanded index-to-infDegree bridge is a genuine separately proved representation bridge, not counted as an existing mathlib replacement. |

MATHLIB-IDIOMATIC arithmetic expression. The local abbreviated form remains readable; upstream should reuse existing operations.

## Phase 5 — all15 formal-search cells

| Method | Current arithmetic Φ | Literature sum of two suprema | Abstract addition constructor |
|---|---|---|---|
| Lean-Finder | Roth/auxiliary-index query returns polynomial-degree/index analogues, not exact Φ. | Supremum-addition inequalities over EReal/ENNReal. | Addition implementations; not a new combined definition. |
| Loogle | `"sSup"` returns broad lexical matches. | `SupSet.sSup` finds generic operation; external module locator differs from current pin. | `HAdd.hAdd` initial identifier error retained; retry `"add"` returns Add.add. |
| LeanSearch | Roth Lemma6 query gives polynomial sums. | iSup/add inequalities; partial matches, not replacement of totalized real definition. | Add/two_nsmul etc.; generic additive infrastructure. |
| rg pinned sources | `lem6Φ|lem6Phi|Roth.*[Pp]hi`, no exact name. | sSup addition laws located; laws need their own boundedness/nonempty context and are not used to merge these two sets. | SupSet class, Set.image2 and real exceptional-value laws identified and read. |
| Local name search | Project spelling truncated to `Roth.lem6`; index unavailable. | sSup name matches available but not proof of exact arithmetic replacement. | No matching `HAdd.hAdd`; index unavailable. |

All12 tool cells and three source cells were actually executed. Local index unavailability does not establish absence. External candidates are not trusted by name alone. Native checks verify `SupSet.sSup`, `Add.add`, `Set.image2`, `Real.sSup_empty` and `Real.sSup_of_not_bddAbove` at the pin. SupSet.sSup lives in `Mathlib/Order/SetNotation.lean:44`; Add.add is Lean core. Current real exceptional-value laws live in `Mathlib/Algebra/Order/Archimedean/Real/Basic.lean:168,183`. Set.image2 is in `Mathlib/Data/Set/Operations.lean:337`. ENNReal/EReal and finite-sup addition results are different target types/domains and cannot silently replace this totalized real expression. No absence theorem is asserted: positive generic composition suffices.

Evidence: [all formal responses](../evidence/Roth.lem6Φ/formal-search.json), [rejected external request](../evidence/Roth.lem6Φ/formal-search-rejected.json), [current rg](../evidence/Roth.lem6Φ/rg-current.json), [standard rg](../evidence/Roth.lem6Φ/rg-standard.json), [abstract rg](../evidence/Roth.lem6Φ/rg-abstract.json), [pinned input hashes](../evidence/Roth.lem6Φ/mathlib-inputs.json).

## Phase 5.5 — statement shape

Normal forms: (1) source's Θ sum; (2) sum of real sSup of indexSets; (3) sum of sSup of Set.image2 with full arithmetic families; (4) full infDegree/aeval representation. Forms1–3 are definitionally equal, independently verified. Form4 requires the separately proved index representation bridge. RHS normal-form convention is respected by the bridge equalities. Do not pretend the infDegree conversion or Fin equivalence transport is definitional.

Syntactic generality: tried direct sum, explicit Add.add/sSup, and arbitrary-variable expansion. Locally keep the short arithmetic name, with no new typeclasses. For a future upstream proof, use the two summands or a local let binding at the caller. Argument audit: τ,q,r,M,l have the roles in Phase4a; Fintype is fixed-interface-only; DecidableEq is absent. No superfluous original explicit hypothesis. Overall SHIP-AS-STATED locally, with no proposed upstream standalone declaration.

## Phase 6.0 — all callers and inline audit

Fresh ignored-file-resistant lexical enumeration and tracked git grep agree. There are eleven semantic source lines in five declarations, all in Theta; zero callers outside the declaring file. This is a live local API, not junk. The five direct kernel-value/four type-consumer counts agree with the distinct source caller declarations, but are separately measured, not opaque closure claims.

| Caller | Exact lines | Refactor plan if deleting standalone spelling |
|---|---|---|
| private index_separated_mul_le_aux |420,449| Replace conclusion Φ by two Θ summands. Remove `lem6Φ` from rw list; retain mul_add/add_comm and the two index inequalities. |
| index_det_le |467| Replace conclusion Φ by same sum and call the refactored separated-product helper. |
| index_le_lem6 |562,563,574| Replace both numeric occurrences and local let Φ by the two-summand sum; existing add_nonneg already works on its summands. |
| Θ_option_le |597,598,602,603| Replace both occurrences in each maximum function with the sum; Finset.le_sup' reasoning unchanged. |
| private theta_lt_succ_aux |927| Remove Φ from unfolding list after source substitution; retain composition/equivalence normalization and Fintype.card_fin. |

The module docstring at29 and definition at275 are not callers. `theta_phi_lt_aux` already writes the two transported summands at845–847; this is an inline form of the same numeric bound, not a new construction. Its use by theta_lt_succ_aux is the expected bridge between the Option API and finite-index induction.

Evidence: [fresh lexical search](../evidence/Roth.lem6Φ/callers.json), [tracked cross-check](../evidence/Roth.lem6Φ/git-callers.json), [structured callers](../evidence/Roth.lem6Φ/callers-structured.json), [inline audit](../evidence/Roth.lem6Φ/inline-audit.json).

## Phase 6 — composition experiments and re-aim gate

The current definition's outer constructor is **COMPOSABLE** using exactly three existing calls:

```lean
Add.add (sSup A) (sSup B)
```

Here A and B are precisely the original one-variable and complementary-variable index families. They are input sets, not newly invented assumptions. The executed `constructor` equality substitutes the actual indexSets and closes by rfl, and the separately executed image2_formula identifies both RSet and coprime numerator families, and the full expansion preserves both complete RSet degree/coefficient/nonzero constraints. The isolated polymorphic expression works over `[SupSet A] [Add A]`, with the real specialization independently verified and no project import. No project Θ/indexSet/helper is counted as one of the three existing calls.

Counting the *entire expanded arithmetic argument expression* instead gives more than three calls: Set.image2, map, aeval, infDegree, Finsupp.weight and the casts/degree predicates occur inside the inputs. We do not claim that full expression or the new index representation bridge is a three-call existing proof. The distinction is substantive: Φ itself introduces only the sum of its two already specified supremum inputs; it adds no new constraint, proof or law. This is the same constructor-level analysis as recognizing a supremum applied to a domain-specific set, now with two independent sets and addition. A parent re-aim was performed independently: replacing Θ by its generic SupSet.sSup parent leaves this existing three-call expression. It is NO-composable, rather than claiming mathlib has a distinct named “Roth Phi” definition or inheriting NO automatically.

The full two-family infDegree expansion was executed afresh. It uses a new finset/sInf bridge and index_bridge; that successful proof is representation evidence only. It preserves the same real sSup, including zero for empty or unbounded sets, and the index default value. It does not replace real sSup by an extended-real operator or conflate a sum of suprema with one supremum over a Cartesian product.

Actual caller-expression experiments were compiled, with the exact original operations: separated scalar distribution closes by `mul_add` against Φ by definitional reduction; repeated numeric substitution closes by rfl. The Fin successor transport initially failed rfl and was correctly repaired with `simp only [lem6Φ, Function.comp_def, finSuccEquivLast_symm_none, finSuccEquivLast_symm_some]`. This last *transport proof* is a substantive normalization and is recorded as the Phase6b trivial-simp/borderline pattern on its own; it is not the basis of the three-call constructor verdict. These are experiments on the live caller expressions, not a claimed rebuild of every complete caller proof.

Evidence: [accepted caller source](../evidence/Roth.lem6Φ/lem6phi183-callers-executed.lean.txt), [clean caller receipt](../evidence/Roth.lem6Φ/lem6phi183-callers-receipt.json), [isolated receipt](../evidence/Roth.lem6Φ/lem6phi183-isolated-receipt.json), [full independent expansion receipt](../evidence/Roth.lem6Φ/lem6phi183-project-receipt.json).

## Phase 7 — actionable verdict

**NO-composable-from-mathlib.** Generic sSup and addition already express exactly the construction introduced by this definition. This is positive evidence from a mathlib-only polymorphic expression plus a literal specialization to both actual input families. The conclusion does not rely on fruitless search, local-index unavailability, cost, treating project parent names as mathlib calls, or any nondefinitional normalization.

Existing building blocks are SupSet.sSup twice and Add.add once, with Set.image2 and real sSup conventions verifying the supplied input representation; the expanded weighting/translation operations are separate representation evidence. Locally keep the useful name in `Roth/Theta.lean`: the semantic one-line exemption and five live consumer declarations justify it there. A future contribution of Roth's theorem should put this abbreviation in its proof module or local let bindings rather than propose a generic mathlib Phi API. If deletion is chosen during an upstream rewrite, perform all five caller refactors in Phase6.0 and update the module-docstring entry. No production rewrite is part of this read-only assessment.

## Phase 8 — completion and verification

All mandatory phases and named literature channels complete; unavailable optional ChatGPT channel and external local-index limitations are explicitly recorded. All accepted native receipts are clean, complete and use only standard axioms. Original type/body, exact ordered293-name canonical audit, constructor/expanded-family checks, generic isolated expression, exceptional-value conventions and actual caller-expression checks are archived. Two native failed attempts are retained separately: isolated Add.add zero normalization and Fin transport rfl; neither is accepted evidence. The portable read-only validator checks the current manifest, all17 production/pin hashes, source/input snapshots, canonical exact order, all15 formal cells, native regions/diagnostics/axioms, report links and credential guard. Root acceptance remains pending until independent review.
