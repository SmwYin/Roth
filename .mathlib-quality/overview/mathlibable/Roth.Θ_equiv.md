# Roth.Θ_equiv — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The supremum-congruence law already exists, but this theorem also asserts that renaming variables preserves the entire bounded arithmetic family. That preservation is proved from the input variable equivalence, rather than supplied as a premise. A fresh complete bridge verifies it. The remaining upstream question is whether to expose a reusable bounded-polynomial transport API or keep the specialized Θ law in the Roth development.

## Phase 0 — Doctor

Canonical193 is the public theorem at `Roth/Theta.lean:159`. The full985-line [declaring module](../evidence/Roth.Θ_equiv/source-Theta.lean.txt), [Index module](../evidence/Roth.Θ_equiv/source-Index.lean.txt), supporting Taylor/Box/CoeffNorm representations and complete sole caller `theta_lt_succ_aux` were read. The module defines bounded integer polynomial families and proves the three Θ bounds feeding the main lemma.

The successful2467-job [baseline](../evidence/Roth.Θ_equiv/baseline-build.txt) is reusable because all17 production/pin hashes freshly match: [fresh hashes](../evidence/Roth.Θ_equiv/source-hashes.json), [baseline inputs](../evidence/Roth.Θ_equiv/input-manifest.json). Native original type, complete printed body, axioms and canonical kernel audit are in [original executed source](../evidence/Roth.Θ_equiv/theta-equiv193-original-executed.lean.txt) and [raw receipt](../evidence/Roth.Θ_equiv/theta-equiv193-original-receipt.json). There is no sorry or printer elision. No production source, pin, Git or overview record was edited.

## Phase 1 — Comprehend

For a bijection between two finite variable types, Θ is unchanged if the denominator vector and degree/weight vector are pulled back along that bijection. Both sides range over all nonzero integer polynomials of the corresponding multidegrees and bounded coefficients, and all numerator vectors coprime coordinatewise to the denominators. Renaming the polynomial and transporting the numerator vector produces the same index, in both directions.

Full native elaborated type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {τ : Type u_2} [inst_1 : Fintype τ]
  (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ),
  Roth.Θ B (q ∘ ⇑e) (r ∘ ⇑e) = Roth.Θ B q r
```

σ,τ may have different universes. Each Fintype comes from the fixed Θ/indexSet/index interface. DecidableEq is absent, despite the surrounding section variable. e supplies a variable equivalence, not an equivalence of admissible polynomial pairs. B bounds absolute values of all integer coefficients; q gives denominators and coprimality constraints; r gives both individual degree caps and reciprocal index weights. There are no positivity, nonempty-family or boundedness hypotheses. All real totalization conventions, including empty families and zero q/r coordinates, are preserved.

The source first applies `congrArg sSup`, then uses the private family-inclusion lemma forwards and backwards. The helper renames the polynomial, proves nonzero preservation, transports every degree bound and coefficient bound, transports coprimality, and invokes project `index_rename` after coefficient-map compatibility. Its inverse is essential for equality.

## Phase 2 — Preliminary checks

BIG: Θ_equiv is explicitly listed among the module's main results. Its role is structural rather than a new deep bound, but that does not change the literal size criterion. Definition-only one-line test: n/a, theorem. Three source proof lines do not establish composition from existing mathlib alone: the private helper contains substantive family transport.

## Phase 3 — Exhaustive literature

Exact requests, returned-response SHA256/bytes, titles/URLs and concise original summaries are archived in [web searches](../evidence/Roth.Θ_equiv/web-search.json) and [direct access/recent query](../evidence/Roth.Θ_equiv/web-primary.json). External bodies are not persisted. The [local search](../evidence/Roth.Θ_equiv/local-literature.json), [source hash](../evidence/Roth.Θ_equiv/local-literature-input.json) and [§4–5 excerpt](../evidence/Roth.Θ_equiv/clean-excerpt.tex.txt) retain the precise local evidence.

| Channel | Actual query / locator | Outcome |
|---|---|---|
| General, specific | `Roth theorem polynomial index supremum Theta variable renaming` | [Princeton lecture17, Definition17.1.1](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf) gives the weighted first nonzero derivative index. Indexed excerpt read; direct PDF timed out400. |
| General, broad | `supremum invariance bijective change of variables polynomial index height` | [Roth, ICM1958, p206](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) describes weighted derivative index and arithmetic coefficient bounds; indexed text read. Exact Θ-family renaming theorem not attributed to this source. |
| General, aliases | `Roth lemma index polynomial permutation variables weighted multiplicity` | [Min Ru, Roth's Theorem, p3](https://www.math.uh.edu/~minru/fields/roth.pdf) uses normalized derivatives and coefficient height. Permutation-polynomial and additive-combinatorial Roth hits rejected as different topics. |
| ChatGPT mathematical MCP | Standard form, generality and historical formulation | n/a: ask_chatgpt_math unavailable; no answer fabricated. |
| Local manuscript | clean.tex lines628–670 | Requests variable-renaming invariance for the point index and defines Θ over all integral, nonzero, degree/coefficient bounded polynomials and coprime numerators. This supplies the exact family semantics. |
| nLab | `site:ncatlab.org/nlab supremum reindexing bijection` | [join](https://ncatlab.org/nlab/show/join) and equivalence-of-types material give abstract order/transport context. Direct join open failed400 unsupported XHTML; indexed material only. |
| nCatLab | `site:ncatlab.org/ncatlab supremum polynomial reindexing` | Returned nLab material outside the requested namespace. No exact nCatLab theorem found; no absence inference. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring variables renaming automorphism` | Commutative-algebra polynomial presentations are adjacent. Supplementary [Tag00EP](https://stacks.math.columbia.edu/tag/00EP) directly read, but it concerns localization gluing, not this renaming law; excluded as support. |
| MathOverflow | `site:mathoverflow.net Roth theorem polynomial index weights` | Questions64709/332190 concern Diophantine approximation; question401350 concerns maximum weights of homogeneous filtrations. Adjacent context only, no exact family transport claim. |
| Recent arXiv, last5years | `site:arxiv.org Roth theorem index polynomials 2022 2023 2024 2025 2026`; corrected date-filter query `site:arxiv.org Roth theorem Diophantine polynomial index after:2021-10-27 before:2026-10-28` | [Hindes2209.09182](https://arxiv.org/abs/2209.09182), submitted2022-09-19, concerns positive characteristic and explicitly distinguishes failure of classical Roth. Other hits concern additive-combinatorial Roth and are rejected. No exact modern Θ reindexing citation claimed. |

Concept identified: invariance of a bounded arithmetic extremal index under relabeling coordinates; abstract component: supremum invariance under family equivalence. Source hypotheses usually take positive dimension, B≥1 and positive integer q,r. Lean already handles all finite types and total zero parameter cases. Historically Roth's index is a weighted order of vanishing; the indexed source excerpts and local manuscript agree on that content. There is no evidence that arbitrary changes of coordinates preserve coefficient height or individual degree caps. A bijective renaming is the relevant restricted coordinate change.

## Phase 4a — Every parameter and hypothesis

| Parameter | Role and generality check |
|---|---|
| σ,τ : Type* | Arbitrary finite coordinate sets, independent universes; already broader than ordered lists of m positive coordinates. |
| Fintype σ, Fintype τ | Fixed Θ/index signatures need finite global weight sums. An equivalence can transfer finiteness, but deleting either class from the unchanged statement does not supply the missing parent instance. No unverified deletion claimed. |
| e : σ ≃ τ | Injectivity preserves nonzero/coefficient information; surjectivity transports every target degree/monomial and supports inverse inclusion. A mere injection could introduce extra admissible variables and is not the same equality law. |
| B : ℝ | Arbitrary coefficient cap. No B≥1 premise to drop; both sides may be empty for small B. Removing this data loses the height family. |
| q : τ→ℕ | Denominators and coordinatewise integral coprimality remain exactly the same after pullback. Neither positivity nor reduced-fraction uniqueness is required here. |
| r : τ→ℕ | Degree caps and index weights both pull back. No r>0 premise exists. Separating the caps from weights is an API extension rather than removing an unused argument. |
| Integer coefficients and numerators | Integral coefficient bounds and coprimality are application-specific data. A coefficient-predicate transport theorem could be more reusable, but changing these fixed parents is not a mechanical weakening of this theorem. |
| Real output | Equality transport only requires SupSet, while the concrete arithmetic index still uses ℝ. Existing SupSet congruence is verified independently; it does not construct the new admissible family equivalence. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL within the unchanged Θ/indexSet signatures: no mechanical hypothesis deletion established. No YES-but-generalise-first claim is made. The verified abstract schema is

```lean
example {α : Type*} [SupSet α] {s t : Set α} (h : s = t) : sSup s = sSup t :=
  congrArg sSup h
```

It is already existing equality congruence. Its h is not an assumption of Θ_equiv. Likewise `Equiv.iSup_congr` requires equivalence of the family indices plus equality of evaluated values. The actual input e only equates the variable types. Generalizing bounded-degree/coefficient transport to arbitrary coefficient predicates or a chosen height structure would require settling the parent RSet interface, which remains BORDERLINE in the accepted progress snapshot. That is a genuine API choice, independent of implementation cost.

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No new class warranted; Fintype already captures finiteness. A height-preserving map class is not needed for one rename proof. |
| 2 | Sequences to filters | No sequence, topology or convergence. |
| 3 | Construction to universal property | SupSet congruence works without IsLUB or boundedness premises. An IsLUB formulation adds irrelevant prerequisites to an equality of total functions. |
| 4 | Predicate to bundled substructure | RSet excludes0 and bounds coefficients, so is not closed under addition/scalar multiplication and is not a submodule. Degree-only restriction and coefficient-bound restriction should not be confused. |
| 5 | Weaken algebraic hierarchy | A separate coefficient-predicate renaming theorem could use CommSemiring coefficients, existing renameEquiv and degree/coefficient transport; this requires restating the family parent. No claimed compiled weakening of Θ_equiv. |
| 6 | Higher categorical form | None; packaging rename as functorial naturality gives no necessary consumer benefit here. |
| 7 | Concrete index/ordered structure | Outer equality generalizes to SupSet, already covered by congrArg/Equiv.iSup_congr. Arbitrary real-valued family maps still need transported admissibility. |
| 8 | Concrete-via-abstract diagnostic | Θ occurs0times in the3-line proof body after `apply congrArg sSup`; indexSet_comp_subset occurs2times. This fires the diagnostic but reveals a hidden dependency: the entire arithmetic family bridge remains inside that helper. The complete fresh inclusion193 proof exposes it; supplying its conclusion as h would remove mathematical content. |
| 9 | False-generalization guard | Reject arbitrary coordinate substitutions (may merge coefficients/increase degrees), a generic equal-set premise as an equivalent statement of the full theorem, and unqualified complete-lattice image formulas on ℝ. SupSet-only `sSup_image'` is valid; nested bounded `sSup_image` needs CompleteLattice. Preserve empty and zero-parameter cases. |

Modern idiom available for organization: expose equality/transport of admissible polynomial families, then apply existing supremum congruence. It enables reuse by set membership and other extrema independently of Θ. Whether that family deserves a general bounded-polynomial API is unresolved design, not a missing generic supremum law. The present proof is already idiomatic locally.

## Phase 4.5 — Infrastructure risk

n/a — theorem. It introduces no definitional equality, class, instance, coercion or new universe constraint. The six definition-only rows are therefore inapplicable, rather than assumed risk-free by untested synthesis.

## Phase 4.6 — Five proof-strategy checks

| # | Check | Outcome |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Element algebra versus inclusions | Set equality by two inclusions is appropriate. Bundling an equivalence of admissible pairs would reuse renameEquiv, but still requires the same membership transport. |
| 3 | Sequences versus nets | n/a, no limits. |
| 4 | Explicit construction versus universal property | Existing equality congruence is sufficient after family identification; no new supremum construction. |
| 5 | Helpers mathlib should have | Individual rename/nonzero/degree/coeff lemmas exist. A reusable preservation theorem for simultaneous degree caps and coefficient predicates is a candidate, not established missing API. It must be assessed with the parent bounded-family design. |

MATHLIB-IDIOMATIC locally. Optional organizational refactor: prove public family equality, then make Θ invariance its congruence corollary. This can support other extrema, but no cost or proof-length criterion determines the verdict.

## Phase 5 — Fifteen actual mathlib search cells

All12 initial API requests and complete raw responses are in [formal search](../evidence/Roth.Θ_equiv/formal-search.json). [Additional bounded-family Finder/LeanSearch](../evidence/Roth.Θ_equiv/transport-search.json) investigates the substantive bridge rather than just sSup. The pinned source searches are [current](../evidence/Roth.Θ_equiv/rg-current.json), [literature](../evidence/Roth.Θ_equiv/rg-literature.json), [abstract](../evidence/Roth.Θ_equiv/rg-abstract.json), and [transport](../evidence/Roth.Θ_equiv/rg-transport.json). Full source copies and hashes are listed in [mathlib inputs](../evidence/Roth.Θ_equiv/mathlib-inputs.json).

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current arithmetic family rename | degreeOf_rename_of_injective and totalDegree_renameEquiv, partial | `MvPolynomial.rename, MvPolynomial.degreeOf`, degree transport | symmetric polynomial rename laws, different family | no exact project family law | Θ_equiv empty, index unavailable |
| Literature family reindex | Equiv.iSup_congr/comp | `sSup, Equiv` errored; corrected `Equiv.iSup_congr` finds generic law | Equiv.iSup_congr, BijOn laws | renameEquiv and per-degree/coeff/support transport | sSup_image family, index unavailable |
| Abstract equal set suprema | iSup_congr, Finset analogues | `sSup ?s = sSup ?t`, conditional supremum comparisons | indexed congruence and sSup_eq_iSup' | exact existing iSup_congr/Equiv.iSup_congr/image2 laws | congrArg source hit, index unavailable |

Additional Finder finds `renameEquiv`, `supported_eq_range_rename`, finite-variable representation, not a checked equivalence of simultaneous degree/coefficient constrained nonzero families. LeanSearch finds coefficient transport, not the full bounded family law. Source `supported` restricts which variables occur; it does not encode separate degree caps and coefficient height. Search failures/empty results are not absence proofs; external indexed revisions may differ from the pin.

Pinned positive APIs: `MvPolynomial.renameEquiv`, `rename_eq_zero_iff_of_injective`, `coeff_rename_mapDomain`, `map_rename` in `Mathlib/Algebra/MvPolynomial/Rename.lean`; `degreeOf_rename_of_injective` in `Mathlib/Algebra/MvPolynomial/Degrees.lean`; `Finsupp.mapDomain_surjective`; `congrArg`; `Equiv.iSup_congr` at `Mathlib/Order/CompleteLattice/Basic.lean:195`; `sSup_image'` there at219. The source-verified individual polynomial APIs are actually elaborated in the fresh fullBridge proof. The initial standard Loogle query errored and is retained honestly; its [successful corrected query](../evidence/Roth.Θ_equiv/loogle-standard-retry.json) finds Equiv.iSup_congr. The isolated receipt independently checks full generic signatures and proofs. Concluded: exact outer congruence exists; substantive bounded arithmetic family transport has partial matches and new verified glue, not an exact replacement established by these searches.

## Phase 5.5 — Statement shape

Normal forms compared: Θ equality, equality of indexSet, image2 equality for the two independent choices, and indexed supremum over admissible pairs. Θ equality is the most convenient local rewrite for the caller; indexSet equality is the stronger family-level fact. Existing image2 is canonical for the family constructor. Reversing the equality is useful at the actual caller, so no global simp orientation is proposed. An equality to a selected abstract normal form may put that form on the RHS.

Syntactic alternatives actually attempted: familyEq (two helper inclusions), replay (one congrArg application to that newly proved equality), and fullBridge (same conclusion with a separately reconstructed inclusion instead of the private helper). All compile. The sole caller needs the Θ equality in reverse; subtype equivalences would add coercions without making that rewrite easier.

Superfluous-argument audit: σ,τ/Fintype are used by fixed parent signatures; e's inverse provides surjectivity and converse transport; B,q,r all occur in essential bounds/points/weights. DecidableEq and positivity are already absent. NONE to drop. Overall SHIP-AS-STATED locally; a generic upstream proposal needs a family-level restatement after the API questions below, not a duplicate sSup-congruence lemma.

## Phase 6.0 — Complete callers and inline audit

[Scoped rg](../evidence/Roth.Θ_equiv/callers-rg.json), [tracked git grep](../evidence/Roth.Θ_equiv/callers-git.json) and [source inventory](../evidence/Roth.Θ_equiv/source-inventory.json) agree: docstring at34, declaration159, sole application919. There is1 explicit application in1 same-file consumer,0 external-to-file callers, and0 outside-declaring-file internal uses under the command's K convention. [Structured caller plan](../evidence/Roth.Θ_equiv/callers.json) preserves that distinction.

| Caller | Usage and actionable treatment |
|---|---|
| private Roth.theta_lt_succ_aux, Theta:919 | `rw [← Θ_equiv e.symm ((q 0 : ℝ) ^ (δ * r 0)) q r]`, with `e = finSuccEquivLast`. It changes Fin(n+2) coordinates to Option(Fin(n+1)) before applying Θ_option_le. Retain the local rewrite law until the bounded-family API is settled. If splitting it, prove family equality with forward/inverse rename transport and apply congrArg sSup, then use exactly the same reverse rewrite. The complete caller was freshly replayed with the new replay theorem. |

Canonical native audit independently checks exact293 ordered unique/present/valued declarations and finds1 direct kernel-value consumer, `_private.Roth.Theta.0.Roth.theta_lt_succ_aux`, and0 direct type consumers. Source occurrences, direct kernel consumers and transitive/simp dependency closure are distinct. The theorem is live. [Inline audit](../evidence/Roth.Θ_equiv/inline-audit.json) finds the point-index rename law and separated-variable embeddings, but no independent Θ-family invariant rederived elsewhere.

## Phase 6 — Actual composition experiments and parent re-aim

Four complete clean native evidence sets are accepted: original, [project bridge source](../evidence/Roth.Θ_equiv/theta-equiv193-project-executed.lean.txt)/[receipt](../evidence/Roth.Θ_equiv/theta-equiv193-project-receipt.json), [full caller source](../evidence/Roth.Θ_equiv/theta-equiv193-callers-executed.lean.txt)/[receipt](../evidence/Roth.Θ_equiv/theta-equiv193-callers-receipt.json), and [isolated source](../evidence/Roth.Θ_equiv/theta-equiv193-isolated-executed.lean.txt)/[receipt](../evidence/Roth.Θ_equiv/theta-equiv193-isolated-receipt.json). New proof regions are344,383 and16 respectively. Accepted diagnostics have no errors, warnings, partial results or nonstandard axioms. The isolated law is axiom-free; generic reindexing uses only propext and Quot.sound.

Attempt1: `congrArg sSup h` succeeds for supplied family equality h using one existing call. Attempt2: `e.iSup_congr h` succeeds under SupSet for a supplied equivalence of family indices and pointwise compatibility. Both are legitimate existing analogous structural laws; neither derives admissibility from a variable equivalence.

Attempt3, actual old form: `familyEq` proves equality by forward/backward project helper applications, and `replay` applies congrArg. This is not a mathlib-only composition: the helper is project-local. Attempt4, fullBridge, eliminates that helper, redoing all arithmetic transport from existing polynomial facts and project `index_rename`. It explicitly keeps nonzero, every degree cap, every coefficient cap and numerator coprimality. The inverse inclusion normalizes `e (e.symm j)`. No use of the target theorem occurs in that new proof. The complete actual caller replay checks that this replacement has exactly the required orientation and arguments.

The parent re-aim gate is independently applied: Θ181 is NO via sSup and indexSet180 is NO via image2. Their generic congruence/reindexing laws are positive hits. However, the input renames the polynomial carrier and its simultaneous degree/coefficient admissibility set; parent RSet179 remains BORDERLINE. Changing to image2 does not itself establish that renamed bounded polynomial family equals the target family. The verified bridge is new mathematical proof, not mere notation normalization or a given congruence premise. Thus this assessment does not reject the parent re-aim rule because normalization is long or costly: it distinguishes an established outer analogous law from an unprovided inner preservation assertion. If a general bounded-family preservation theorem is accepted upstream, this specialized supremum corollary should be reassessed as a direct re-aim hit.

Composition status: NOT-COMPOSABLE under the evidence criterion. No ≤3-existing-mathlib-call proof of the full old statement was verified. The outer layer alone is composable/existing. No absolute library-absence claim is made and no simp-only success is treated as a decisive NO. The initial rejected native attempt is archived separately; its recovered failures are not accepted proof evidence.

## Phase 7 — Verdict and actionable questions

**BORDERLINE-needs-human.** The specialized family identity is useful and exact, but its appropriate upstream home depends on the bounded-polynomial/height interface. Existing general supremum invariance is not a gap. The fresh full bridge identifies the potential reusable content: compatibility of nonzero, individual degree bounds, coefficient predicates and a transported numerical invariant under renameEquiv. This preserves the arithmetic content instead of replacing it with a supplied family equality. A single source caller is an API signal, not proof of redundancy or dead code. No implementation-cost criterion enters this verdict.

1. Should a reusable polynomial-family transport theorem combine arbitrary coefficient predicates with separate coordinate degree caps, rather than expose the Roth-specific RSet family?
2. Should renaming compatibility live first at the admissible-polynomial family level, with numerator coprimality and the supremum invariance retained as Roth-local corollaries?
3. If a coefficient-height API is selected for RSet, should its renameEquiv invariance be the public primitive used by this theorem?

These are concrete future upstream design choices; they do not block this completed read-only assessment. Current local destination: `Roth/Theta.lean`, adjacent to the exact family and its indexSet transport. Keep Θ_equiv and its one reverse rewrite in theta_lt_succ_aux until that decision is made. If exposing indexSet equality locally, reuse the freshly verified familyEq shape and preserve the same caller rewrite. Do not submit a new generic congrArg/sSup wrapper. No upstream PR or new dependency is proposed by this verdict.

## Phase 8 — Complete handoff

[Assessment](../evidence/Roth.Θ_equiv/assessment.json), [verification](../evidence/Roth.Θ_equiv/verification.json), [overview entry](../evidence/Roth.Θ_equiv/overview-entry.json), [current copy manifest](../evidence/Roth.Θ_equiv/copy-manifest.json), [portable validator](../evidence/Roth.Θ_equiv/validate.py). All accepted exact executed sources and complete native receipts are preserved. The initial project attempt failed on a local polymorphic universe declaration and overly restricted simp normalizations; the corrected top-level inclusion compiles. Preparation-only drafts are labelled by filename and never counted as native proof evidence. No limits were raised. Root acceptance remains pending.
