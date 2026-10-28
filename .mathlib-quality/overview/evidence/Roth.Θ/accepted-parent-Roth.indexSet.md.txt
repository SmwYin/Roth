# Roth.indexSet — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** The set construction is exactly the existing binary image `Set.image2`, with the bounded polynomial family and coprime numerator family as its two arguments. This conclusion concerns the image constructor; it does not claim that mathlib already exports the project-specific `RSet` or a named Roth index-family definition. Retaining the documented local alias is useful.

## Phase 0 — Doctor

Canonical180 is the public definition at `Roth/Theta.lean:62`. The entire985-line declaring module was read, together with the relevant definitions of index and weight and all explicit callers. [Theta](../evidence/Roth.indexSet/source-Theta.lean.txt), [Index](../evidence/Roth.indexSet/source-Index.lean.txt), [Box](../evidence/Roth.indexSet/source-Box.lean.txt). The module defines the polynomial/index families and their supremum, proves Lemmas5–7, and transports indices through determinant separation. [Canonical snapshot](../evidence/Roth.indexSet/canonical-snapshot.json) identifies the exact public/private inventory.

The successful2467-job [baseline](../evidence/Roth.indexSet/baseline-build.txt) is reused only after fresh equality of all17 source/pin hashes: [fresh check](../evidence/Roth.indexSet/source-hashes.json), [manifest](../evidence/Roth.indexSet/input-manifest.json), [fresh-build receipt](../evidence/Roth.indexSet/separation-file-completion-2026-10-27.json). The declaration contains no sorry. Native type, exact definition, standard axioms and canonical293 kernel-value/type-consumer audit are retained in [original execution](../evidence/Roth.indexSet/indexset180-original-executed.lean.txt) and [receipt](../evidence/Roth.indexSet/indexset180-original-receipt.json). The full printer is not elided.

## Phase 1 — Comprehend

For a finite variable type σ, choose any nonzero integer polynomial with each individual degree bounded by r and every real-cast coefficient absolute value bounded by B. Independently choose an integer numerator in each coordinate, coprime to its prescribed natural denominator q. The definition collects all real indices at the corresponding coordinatewise quotients; Θ is their real supremum.

Full native type:

```lean
@Roth.indexSet : {σ : Type u_1} → [Fintype σ] →
  ℝ → (σ → ℕ) → (σ → ℕ) → Set ℝ
```

σ is universe-polymorphic; Fintype is inherited from the present index implementation. B bounds coefficients; q fixes denominator data; r bounds degrees and also specifies index weights. No DecidableEq is captured. No condition B≥1, qj>0 or rj>0 is a definition hypothesis. Even qj=0 is allowed: division is total and the coprimality predicate remains present. The entire `RSet` conjunction—nonzero, every degree bound, every coefficient bound—is essential input, not replaced by a weaker degree-only carrier.

## Phase 2 — Preliminary checks

BIG: introduces the named family underlying the main Θ estimates. The body occupies two substantive source lines (nested existential followed by the index expression), so literally MULTI-LINE; the definition-only one-expression test also records its single mathematical construction as one binary-image application. The one-line-exemption diagnostic is still explicit:

| Exemption | Applies? | Evidence |
|---|---|---|
| Defeq barrier | no | Exact image2 equality is rfl; explicit ordinary-unfold probe succeeds. No opaque barrier is required by a caller. |
| Diamond avoidance | no | A Set-valued definition registers no class, instance or alternate arithmetic action. |
| Semantic intent / stable name | yes | Θ, indexSet_nonempty, indexSet_bddAbove and private indexSet_comp_subset use the family name. It separates the arithmetic choices from the supremum API. |

The literal classification is MULTI-LINE; under the compressed one-expression interpretation it is ONE-LINER WITH-EXEMPTION. Neither classification itself settles upstream inclusion. The stable alias can remain local even though its generic constructor exists.

## Phase 3 — Exhaustive literature

Requests, response digests/byte counts, returned titles/URLs and original concise summaries are preserved in [general queries](../evidence/Roth.indexSet/web-0.json), [nLab/nCatLab/Stacks](../evidence/Roth.indexSet/web-1.json), [MO/recent search](../evidence/Roth.indexSet/web-2.json), [direct primary access](../evidence/Roth.indexSet/web-primary.json), [date-window refinement](../evidence/Roth.indexSet/web-recent.json), [local query](../evidence/Roth.indexSet/local-literature.json), and [local §5 excerpt](../evidence/Roth.indexSet/clean-theta-excerpt.tex.txt). Full web bodies are not retained.

| Channel | Actual query or locator | Finding |
|---|---|---|
| Web specific | `Roth theorem theta index polynomial bounded coefficients rational denominators` | The polynomial family and its Θ supremum appear in the local manuscript and indexed textbook Definition6.4.14. The indexed third-party textbook copy is discovery evidence; local §5 is the exact source used here. |
| Web general | `Roth lemma index across sets of polynomials theta supremum` | The weighted derivative index and bounded auxiliary polynomials occur in primary lecture notes; no independently standardized standalone name for indexSet was established. |
| Web aliases | `polynomial index weighted multiplicity Diophantine approximation auxiliary polynomial` | Weighted multiplicity/order is the standard underlying concept. [Princeton chapter17 Definition17.1.1](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf) was available through its indexed excerpt; direct PDF access timed out. |
| ChatGPT mathematics MCP | Standard form/generality/history channel | n/a: ask_chatgpt_math unavailable. No simulated response. |
| Local source | clean.tex §5 lines643–702 | Defines the nonzero integral bounded-degree/bounded-coefficient family and takes the supremum over all coprime numerators. It assumes m≥1, B≥1, positive r and q; the Lean construction admits the totalized boundary inputs. |
| nLab | `site:ncatlab.org/nlab polynomial multiplicity index` | [Polynomial](https://ncatlab.org/nlab/show/polynomial), degree and valuation pages returned; generic context only. Direct polynomial-page open failed with unsupported XHTML. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial index weighted multiplicity` | Actual distinct namespace request returned off-namespace nLab material, including weighted categories/limits. These are rejected as an identification of the arithmetic family. No categorical reformulation inferred. |
| Stacks | `site:stacks.math.columbia.edu polynomial multiplicity order vanishing` | [Tag02MB, Definition10.121.2](https://stacks.math.columbia.edu/tag/02MB) directly read: order along dimension-one local Noetherian domains uses lengths. Adjacent order-of-vanishing theory, not an equal replacement for this set image. |
| MathOverflow | `site:mathoverflow.net Roth theorem polynomial index` | [Dyson's lemma and small index](https://mathoverflow.net/questions/431381/dysons-lemma-implies-index-is-small-in-proving-roths-theorem) is relevant context. Other returned Roth questions discuss effectiveness or additive combinatorics; no formal identity is taken from them. |
| Recent arXiv | `site:arxiv.org 2022 2023 2024 2025 2026 Roth theorem polynomial index`; refined `site:arxiv.org "Diophantine approximation" "subspace theorem" after:2021-10-27 before:2026-10-28` | The first query returned unrelated additive-combinatorial Roth papers and some older noise, explicitly rejected. [Goel–Lunia–Ray2502.00731](https://arxiv.org/abs/2502.00731), submitted2025-02-02, is a primary recent exposition of the classical proof and subspace theorem. Abstract inspected; no claim of a full-paper exact indexSet identity. |

Standard form: values of the weighted polynomial index as polynomial and reduced rational-point data vary independently, followed by a supremum. Literature varies the coefficient field, geometric setting, weight conventions and heights; those are expanded developments, not automatically equal objects. The exact standalone helper set is an implementation boundary, while Θ and weighted index have established mathematical meaning. This supports reusing image infrastructure without treating negative literature searches as absence proofs.

## Phase 4a — Every parameter

| Parameter | Use | Comparison / possible expansion |
|---|---|---|
| σ : Type u | common coordinate type for polynomial/numerator/denominator/degree data | Already arbitrary finite type and universe, including empty type; source uses m≥1. Binary image itself has independent arbitrary universes. |
| Fintype σ | present index uses a global finite sum in weight | Cannot remove while retaining its parent signature. The expanded infDegree/Finsupp.weight representation makes sense without Fintype, but comparing to the unchanged parent still assumes it. |
| B : ℝ | absolute-value bound on all coefficients | No B≥1 premise captured; negative bounds may yield the empty family. Replacing by projective height changes the object. |
| q : σ→ℕ | fixed denominators and integer coprimality inputs | No positivity captured. Allowing arbitrary real rational centers would lose the prescribed-denominator/reduced-numerator family. |
| r : σ→ℕ | individual degree upper bounds and reciprocal index weights | Zero coordinates are valid totalized inputs. Separate bound and weight vectors would expand the interface, not remove a dead argument. |
| ℤ coefficients/numerators | arithmetic family and IsCoprime predicate | Replacing by arbitrary rings requires specifying a new coefficient size/cast/denominator model; no unsupported mechanical weakening claimed. |
| ℝ target | current index convention and real supremum | Extended-real or WithTop order retains infinity internally, then untopD0 must preserve existing zero convention when comparing. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL relative to the fixed parent interfaces; no mechanically droppable captured hypothesis. Parent index already has a verified broader support-degree representation. A fresh all-P/all-r bridge and exact image2 transport independently recheck it here. The expanded arbitrary_variable_image is separately compiled with full native type {σ : Type u} → ℝ → (σ → ℕ) → (σ → ℕ) → Set ℝ, without Fintype; its finite specialization is checked. No positivity is added. The generic outer construction is existing Set.image2 over arbitrary source/target types; replacing the map input by arbitrary f is a genuine constructor specialization, not an assertion that any arbitrary map retains Roth-specific index bounds.

## Phase 4c — All nine modern-idiom questions

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses / instances | No new class needed. Fintype is already the captured parent constraint; new arithmetic predicates should remain explicit sets. |
| 2 | Filters / nets | No topology/convergence in this family construction. |
| 3 | Universal property | No new universal construction; image2 is the existing set image operation. |
| 4 | Bundled substructure | No: the nonzero bounded arithmetic family and its real image are not submodules. Bundling would invent closure laws. |
| 5 | Weaker algebra hierarchy | The outer constructor needs no algebra at all. Coefficient-semiring generalization concerns the index map/input family, not a removable class in this definition. |
| 6 | Higher category | No categorical data/laws; categorical search did not expose an applicable replacement. |
| 7 | Concrete indices | σ already arbitrary finite; abstract image2 has independent universe-polymorphic domains and codomain. InfDegree/Finsupp.weight removes finite-coordinate dependence in the expanded index map. |
| 8 | Concrete-via-abstract diagnostic | Definition body contains no recursive indexSet; RSet and index each occur once, supplying only the source set and mapping function. After naming those inputs, only two bounded existential quantifiers remain: exactly Set.image2. `Set.Nonempty.image2`, `Set.image2_subset`, `Set.forall_mem_image2` and `Set.image2_congr'` then apply directly. |
| 9 | False-generalization guard | Accepted abstraction preserves the *whole* RSet and coprime numerator predicates. Reject omitting nonzero, coefficient bounds or coprimality; replacing individual by total degree; assuming q>0 in an all-input equality; changing untopD0 to infinity; or replacing the nonzero family by a submodule containing0. Generic arbitrary-f image laws are structural, not inherited arithmetic bounds. |

Modern idiom available: yes, already in mathlib. It gives actual nonempty, membership, monotonicity and bound-quantifier API access. Exact ordinary image2 equality is rfl; the expanded infDegree equality uses a genuine finite-order normalization proof and is separately labelled. There is no proposal to add a redundant generic constructor.

## Phase 4.5 — All six infrastructure risks

| Risk | Verdict | Evidence |
|---|---|---|
| Typeclass diamond | none observed | The target is Set ℝ, not a class. Native Membership synthesis and direct predicate application exercise the standard Set interface; the definition installs none. |
| Reducibility leak | low | The exact existential/image2 body equality is rfl, using an ordinary semireducible def without reducible attribute. Expansion exposes arithmetic inputs but no computation-heavy instance search. |
| Noncanonical unfolding | low | Explicit no_automatic_unfold probes simp only, then rfl. Callers intentionally exploit existential membership; no automatic upstream rewrite registered. |
| Instance priority collision | none | No instance or priority is introduced. Existing Fintype σ is a parameter and the set membership/function instances are standard. |
| Universe issues | none observed | Native generic Type u, actual universe1 ULift Unit target, and independent-universe isolated image2 probes elaborate. No universe0 restriction. |
| Coercion ambiguity | none observed | Actual indexSet-to-predicate application and standard Set Membership synthesis tested. Integer-to-real/natural casts have explicitly fixed targets in the map. No new coercion installed. |

Overall LOW; no HIGH rows or special infrastructure mitigation required.

## Phase 4.6 — All five proof-strategy rows

| Question | Assessment |
|---|---|
| ε–δ vs filters | No topology. |
| Element algebra vs point-free structure | image2 expresses the independent choices directly; its nonempty/monotone APIs avoid rebuilding existential logic. Polynomial index bounds still need their substantive arithmetic proofs. |
| Sequences vs nets | No limiting sequence. |
| Construction vs universal property | Existing image2 is the appropriate set constructor; no new universal-property class needed. |
| Missing helpers that should exist | Generic image2 membership/nonempty/monotonicity/pointwise bounds already exist. Finite sInf/infDegree projection normalization is a real bridge proof, not an invented preexisting theorem. No new helper needed to identify the outer image family. |

Strategy: REFACTOR-RECOMMENDED for an upstream proposal—use the existing set image API. Local existential presentation is clear, and its stable alias is worth retaining. No cost-based verdict criterion used.

## Phase 5 — Fifteen actual search cells

Each cell has its raw request/response in `search-{current,standard,abstract}-{finder,loogle,leansearch,local}.json`; the three source search receipts are [current](../evidence/Roth.indexSet/rg-current.json), [standard](../evidence/Roth.indexSet/rg-standard.json), [abstract](../evidence/Roth.indexSet/rg-abstract.json). [Pinned inputs](../evidence/Roth.indexSet/mathlib-inputs.json) preserve positive definitions.

| Method | Current family | Literature-standard family/Θ | Abstract binary image |
|---|---|---|---|
| Finder | Chevalley polynomial bounds; partial/irrelevant | additive-combinatorial RothNumber hits; rejected | Set.mem_image2 and generic image2 laws |
| Loogle | IsCoprime/ideal hits; not the image family | Initial sSup identifier rejected; actual corrected SupSet.sSup retry returned generic supremum-image API | Set.mem_image2, Set.mem_image2_of_mem and image2 projections |
| LeanSearch | support, Schwartz–Zippel and Diophantine polynomial API; not equal | additive-combinatorial Roth hits; rejected | Set.image2, Set.mem_image2, Set.exists_mem_image2 |
| rg | No exact Roth.indexSet definition in pin | infDegree support minimum infrastructure; no exact specialized family identified | Exact Set.image2 and its membership/nonempty/monotonicity source |
| local | Project target/helpers; index unavailable | Project family/helpers; index unavailable | Existing image2 family, bounds and finite/countable/nonempty image API |

The corrected standard Loogle attempt is [retained](../evidence/Roth.indexSet/search-standard-loogle-retry.json); the initial error remains labelled, not counted as successful search evidence. Online results may differ from the pin. Positive native checks verify exact pinned signatures. Local index unavailability and negative searches establish no global absence claim.

Concluded: found in mathlib as **Set.image2**, a strictly more general constructor whose specialization is exactly the original family. Pinned location `Mathlib/Data/Set/Operations.lean` defines image2 immediately before mem_image2 at341; `Mathlib/Data/Set/NAry.lean` supplies Nonempty.image2 at114, image2_subset at37, forall_mem_image2 at54. Parent index is separately re-aimed to AddMonoidAlgebra.infDegree with a fresh all-input bridge; no blanket inheritance of RSet's BORDERLINE verdict.

## Phase 5.5 — Statement shape

Normal forms tested: nested bounded existentials; Set.image2 of the independent choices; image of an uncurried function over the Cartesian product (existing image_uncurry_prod). image2 is canonical for this two-input pattern. A comparison places it on the RHS; the ordinary bridge is rfl. The product-image route is unnecessary normalization and is not used to establish the verdict.

Syntactic generality: preserve the short local `indexSet B q r` name at arithmetic callers, while using image2 laws or the exact explicit term when expressing generic structure. Two separately bundled subtypes would also describe the choices, but add coercions without improving current membership/destructuring. Actual caller proofs test the chosen image2 signature.

Superfluous arguments: σ/Fintype are required by the current index signature; B, q and r all determine the family. DecidableEq is absent rather than a removable native assumption. Positivity hypotheses do not occur. Overall RESTATE-BEFORE-SHIP if proposing anything upstream: use existing image2 rather than introduce a specialized parallel constructor. Local SHIP-AS-STATED is reasonable as a semantic alias.

## Phase 6.0 — Every explicit caller and inline audit

Fresh scoped `rg --no-ignore` and tracked git grep agree: [rg](../evidence/Roth.indexSet/callers.json), [git](../evidence/Roth.indexSet/git-callers.json), [exact caller structure/plans](../evidence/Roth.indexSet/callers-structured.json). Excluding docstrings/definition and requiring a standalone identifier gives **4 callers,5 occurrences, all in Theta**. K outside the declaring file is0, with0 external files. References to names such as indexSet_nonempty are not textual indexSet calls.

| Caller | Location | Exact occurrences and refactor |
|---|---|---|
| Roth.Θ | Theta:68 |1; sSup(indexSet B q r) becomes sSup of exact image2. Tested theta_inline by rfl. |
| Roth.indexSet_nonempty | Theta:80 |1 in statement; use Set.image2_nonempty_iff with1 polynomial and all1 numerator, retaining one_mem_RSet proof. Tested the exact target through the image2 bridge; direct Nonempty.image2 is separately tested in isolation. |
| Roth.indexSet_bddAbove | Theta:87 |1 in statement; replace by exact image2, retain source bound proof and project index_le_card. Complete source proof replay tested. |
| private Roth.indexSet_comp_subset | Theta:142 |2 in subset statement; replace both source/target sets with corresponding image2, preserve variable-equivalence transport. Complete source proof replay tested. |

Canonical kernel audit independently reports10 direct value consumers and3 direct type consumers across exactly293 source declarations; several proof consumers depend on definitional unfolding without spelling the target in source. This is not a full transitive/simp closure. The target is live. [Inline audit](../evidence/Roth.indexSet/inline-audit.json) finds the original family definition and many unrelated index/supremum manipulations; it does not identify an independent duplicate arithmetic index-family implementation. K=0 outside the file alone is not evidence of dead code.

## Phase 6 — Composition experiments and boundaries

The exact replacement term is one existing set-constructor application:

```lean
Set.image2 (fun R h ↦
  index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r)
  (RSet B r) {h : σ → ℤ | ∀ j, IsCoprime (h j) (q j : ℤ)}
```

Native `image2_bridge` is rfl; this is the project's checked identification of its own definition with an **existing mathlib constructor**, not an existing mathlib theorem named image2_bridge. The function and two sets are input data. They preserve the entire nonzero/degree/coefficient conjunction and coprimality constraint; no assertion that RSet or index are already mathlib construction calls is smuggled into a ≤3-call count.

The parent index re-aim is independently verified using a finite support empty/nonempty split, Finset.coe_inf' and Finset.inf'_eq_csInf_image, then Finsupp.weight_eq_sum and the aeval Taylor definition. It yields Set.image2 with an infDegree/Finsupp.weight/aeval map and untopD0 projection, retaining RSet and the coprime-numerator family exactly. The normalization is new proved glue, not a definitional equality or preexisting mathlib point-index theorem. The expanded expression has multiple input-construction operations; no claim that the whole expanded arithmetic expression is a ≤3-call proof. The decisive more-general object for this target is image2, independent of how its map is represented.

Actual target checks include q≡0 with the same coprimality condition and total division; arbitrary q,r in the general bridge already cover mixed zero coordinates. Isolated mathlib-only checks guard the project target as missing and verify the generic binary-image definition and its nonempty/monotone/pointwise-bound API. Complete actual source caller replays cover boundedness and renaming, while Θ and nonempty use direct existing operations. Project index laws used in caller proofs are labelled project dependencies and do not count as replacement building blocks.

Composition conclusion: **exact specialization of existing Set.image2**; generic outer construction is composable in1 call. The project-specific arithmetic inputs are not a new generic set construction. This is NO-mathlib-has-it by positive constructor identification, not NO-composable justified merely by `simp [defs]`. No closing-simp-only experiment is used to decide the verdict; Phase6b's trivial-simp caution is respected.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it.** `Set.image2` already represents exactly the independent polynomial/numerator image family. The native equality is rfl for all B,q,r, including zero denominators. It leaves every RSet and coprimality restriction untouched. Mathlib's generic image laws already provide the structural API. The positive hit is the existing image constructor, not an assertion of absolute library absence of a Roth-family name, and not inherited from RSet or from the previous index assessment.

The semantic-name exemption is real: the local alias documents the family feeding Θ. Keep it in `Roth/Theta.lean`, optionally implementing its body with the displayed Set.image2 term. There is no proposed upstream definition PR. If eliminating the name locally, replace each of the5 explicit occurrences at the4 table rows with the displayed exact term; the native replays confirm each signature and proof interface. At Θ preserve sSup; at nonempty use image2_nonempty_iff; at boundedness preserve the actual degree/index bound; at renaming preserve transport of polynomial coefficients, degrees and numerator coprimality. Update the module/docstring references and retain helper theorem names unless separately reassessed. The10 kernel direct consumers describe additional proof dependency scope, not5 further explicit edits.

An alternative local destination is the existing Theta module because the definition combines proof-specific arithmetic bounds and prescribed-denominator data. Archive or a generic Set module would obscure that purpose. Separately useful generic support-degree or arithmetic-height laws can be assessed independently; no missing generic image API is asserted. No implementation-cost criterion enters this verdict.

## Phase 8 — Complete handoff

[Assessment](../evidence/Roth.indexSet/assessment.json), [verification](../evidence/Roth.indexSet/verification.json), [overview entry](../evidence/Roth.indexSet/overview-entry.json), [copy manifest](../evidence/Roth.indexSet/copy-manifest.json), [portable validator](../evidence/Roth.indexSet/validate.py). Accepted exact native sources/receipts and rejected attempts are distinguished in verification. The initial direct target nonempty term exceeded default200k heartbeats and the first zero-denominator rfl failed on cast normalization; the accepted version uses explicit image2_nonempty_iff and Nat.cast_zero. Two expanded attempts failed before the explicit infDegree/support normalization was complete; one also guessed a nonexistent CoeFun(Set) instance, corrected because Set is already a predicate function. These3 rejected receipts are preserved, never counted as accepted evidence; no limits were raised. The validator checks phase completion, complete native success/standard axioms, current hashes/bytes, fresh17 inputs, canonical293 exact order/private names and direct consumers, mandatory search channels and report links. Root acceptance remains pending; no production, pin, Git or overview record is edited by the worker.
