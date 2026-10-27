# Full assessment — `MvPolynomial.taylor_neg_taylor`

Canonical declaration **70/293**; source `Roth/Taylor.lean:182–184`. Verdict **BORDERLINE-needs-human**, independently assessed rather than inherited from the parent translation definition. The assessment is complete; numbered questions concern future upstream API design and do not block this read-only survey. Production Lean and version pins are unchanged.

## Phase 0 — Baseline and resolution

Baseline `99f19fda4b3cbee38fc0d31af76075834f5cc265`: successful full `lake build`, 2467 jobs. All 17 production source/pin hashes were freshly compared and match. [Build](../evidence/MvPolynomial.taylor_neg_taylor/baseline-build.txt), [inputs](../evidence/MvPolynomial.taylor_neg_taylor/inputs.json), [comparison](../evidence/MvPolynomial.taylor_neg_taylor/input-hash-check.json). Unique public theorem resolves at the source above, no `sorry`; no simp attribute. Taylor's module develops translation, Hasse coefficient identification and finite Taylor expansion. Full declaring module and Index consumer context were read: [Taylor](../evidence/MvPolynomial.taylor_neg_taylor/Taylor-module.lean.txt), [Index](../evidence/MvPolynomial.taylor_neg_taylor/Index-module.lean.txt).

## Phase 1 — Mathematical content and exact type

For any polynomial over a commutative ring, translating its variables by a vector and then by the negative vector returns the original polynomial. Algebraically the two substitution homomorphisms are inverse. No division, characteristic-zero argument, finite variable set or nonzero polynomial assumption is involved.

```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A]
  (α : σ → A) (P : MvPolynomial σ A),
  MvPolynomial.taylor (fun j ↦ -α j) (MvPolynomial.taylor α P) = P
```

Native full type, proof print, fresh replay, and axiom audit: [source](../evidence/MvPolynomial.taylor_neg_taylor/native-target-executed.lean.txt), [complete receipt](../evidence/MvPolynomial.taylor_neg_taylor/native-target-success.json). Mathematical argument: the composition law adds the shift vectors, pointwise additive inverse cancellation makes their sum zero, and zero translation is the identity. Direct project dependencies are taylor, taylor_taylor and implicit simp dependency taylor_zero. The scratch proof-constant audit records the actual constants rather than inferring everything from visible tactic names.

## Phase 2 — Preliminary checks

**SMALL**: an inverse-operation helper, not a module-listed main result, new structure, or eponymous theorem. Exhaustive literature and all formal methods still run. Definition-only one-line exemption test is n/a: this is a theorem. Its one-line `simp [taylor_taylor]` is assessed under Phase 6b, not mistaken for a one-line data definition or a three-mathlib-call proof.

## Phase 3 — Exhaustive literature protocol

Every actual query is retained in its batch metadata, together with hash/bytes of the returned response. Full article and search-result bodies are not archived. Only selected unsigned locators and original concise summaries are retained. All rows below correspond to executed requests, including access failures.

| Channel | Actual query or locator | Findings and limits |
|---|---|---|
| General web, specific | `polynomial translation automorphism inverse negative shift multivariate arbitrary commutative ring` | Universal-property and polynomial automorphism material; no separately named arbitrary-ring multivariate inverse theorem established. [batch](../evidence/MvPolynomial.taylor_neg_taylor/web0-metadata.json) |
| General web, general | `multivariate polynomial shift equivalence inverse translation f x alpha` | Shift equivalence and affine transformation context; computational equivalence problems are distinct from this elementary cancellation law. [batch](../evidence/MvPolynomial.taylor_neg_taylor/web0-metadata.json) |
| General web, aliases | `polynomial ring additive group action translations inverse` | Additive-group action and substitution viewpoints; composition corresponds to addition of shifts. General group action terminology supplies context, not a compiled polynomial representation. [batch](../evidence/MvPolynomial.taylor_neg_taylor/web0-metadata.json) |
| Optional ChatGPT math | Standard form, generality, historical evolution | n/a: ask_chatgpt_math unavailable. No consultation claimed. |
| Local reference | `clean.tex` Section 4 Index, lines 500–548 | Real-coordinate finite Taylor expansion uses `(x_j−α_j)` and Pα(X)=P(X+α). Inverse substitution explains returning from shifted expansion; not a separately stated named theorem. [record](../evidence/MvPolynomial.taylor_neg_taylor/local-literature.json), [excerpt](../evidence/MvPolynomial.taylor_neg_taylor/clean-excerpts.tex.txt) |
| nLab | `site:ncatlab.org/nlab polynomial ring automorphism translation` | Polynomial/free commutative algebra and automorphism entries supply universal-property context. Incorrect `polynomial+ring` entry returned 404; corrected `polynomial` open failed due unsupported application/xhtml+xml. Search text was accessible. [search](../evidence/MvPolynomial.taylor_neg_taylor/web4-metadata.json), [initial](../evidence/MvPolynomial.taylor_neg_taylor/webprimary-metadata.json), [corrected access](../evidence/MvPolynomial.taylor_neg_taylor/webfollow-metadata.json) |
| nCatLab | `site:ncatlab.org polynomial algebra universal property automorphism` | Same site's action and automorphism entries describe group actions as maps into automorphisms. Direct action page also unsupported application/xhtml+xml; no successful article fetch claimed. [search](../evidence/MvPolynomial.taylor_neg_taylor/web4-metadata.json), [access](../evidence/MvPolynomial.taylor_neg_taylor/webfollow-metadata.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial ring automorphism translation`; follow-up `site:stacks.math.columbia.edu "polynomial" "automorphism" "X"` | Initial 00F2 is finite presentation context, not target. Follow-up 051P proof uses triangular variable shifts as automorphisms: broader nonconstant triangular substitutions, not the exact arbitrary-index constant-shift identity. [search](../evidence/MvPolynomial.taylor_neg_taylor/web4-metadata.json), [follow-up](../evidence/MvPolynomial.taylor_neg_taylor/webfollow-metadata.json), [inspected lemma](../evidence/MvPolynomial.taylor_neg_taylor/weblocator-metadata.json) |
| MathOverflow | `site:mathoverflow.net polynomial ring translation automorphism`; follow-up `site:mathoverflow.net "translation" "polynomial" "automorphism" inverse` | MO53527 second answer explicitly discusses translations as a subgroup of affine-space automorphisms, over an algebraic closure of a field. Context only; no claim it proves this Lean ring-level statement. [initial](../evidence/MvPolynomial.taylor_neg_taylor/web4-metadata.json), [follow-up](../evidence/MvPolynomial.taylor_neg_taylor/webfollow-metadata.json), [access](../evidence/MvPolynomial.taylor_neg_taylor/weblocator-metadata.json) |
| Recent arXiv | `site:arxiv.org polynomial shift equivalence 2022 2023 2024 2025 2026 automorphism` | Montagard–Pan–Rittatore, 2412.09519, submitted 12 Dec 2024 and revised 21 Aug 2025, lies within 2021-10-27–2026-10-27. Abstract discusses normal subgroups of translations in derivation centralizers over algebraically closed characteristic-zero fields. This is contextual contemporary use, not the target proof. Broad query also returned unrelated topics and old identifiers; they are not counted as exact/recent support. [search and date](../evidence/MvPolynomial.taylor_neg_taylor/webprimary-metadata.json) |

Primary mathematical anchor: [Bergman, *An Invitation to General Algebra and Universal Constructions*, §4.12](https://math.berkeley.edu/~gbergman/245/3.4.pdf), free commutative algebra on arbitrary generators. The shift inverse follows by computing the two maps on generators and using uniqueness; this implication is our mathematical inference. Supplementary [polynomial universal-property notes, Proposition 1, p.2](https://fenix.tecnico.ulisboa.pt/downloadFile/563568428826591/ring_algebras.pdf) give the univariate mapping property. [Stacks 051P](https://stacks.math.columbia.edu/tag/051P) is a primary example of polynomial variable-shift automorphisms in use. [Recent paper abstract/date](https://arxiv.org/abs/2412.09519) verifies only the narrower research context described above.

Literature summary: inverse translation, shift automorphism and additive action are standard descriptions. Coordinate, free-algebra and group-action presentations agree on cancellation but differ in packaging and scope. The elementary ring-level result is broader than finite real-coordinate language. No precise historical attribution is justified by these searches. More general polynomial automorphisms or noncommutative skew rings have additional structure and are not interchangeable with this exact statement.

## Phase 4a–4b — All parameters and generality

| Parameter or hypothesis | Current versus literature and weakening conclusion |
|---|---|
| σ : Type u | Arbitrary variable type, independent universe; empty and infinite types included. No Fintype, DecidableEq or nonemptiness to drop. |
| A : Type v | Arbitrary coefficient type, not fixed ℝ/field. Independent universe. |
| CommRing A | CommSemiring is required by the fixed parent; ring negation and additive cancellation are needed for this unchanged negative-vector statement. Guarded native application with only CommSemiring fails as expected. No Field, domain, nontriviality or characteristic hypothesis exists. |
| α : σ → A | Every shift vector, including zero; supplies the operation to be inverted. It cannot be removed while preserving the theorem's content. |
| P : MvPolynomial σ A | Every polynomial, including zero; no degree restrictions. |
| negative α | Essential cancelling shift, not arbitrary unrelated β. Replacing it by arbitrary β without a cancellation condition would be false. |

**MAXIMALLY GENERAL within unchanged parent/interface; zero verified hypothesis drops.** A genuinely broader, separately compiled reformulation works over CommSemiring for α,β with `h : ∀ j, β j + α j = 0`, concluding shiftβ(shiftαP)=P. This replaces negation by an explicit inverse-pair condition; it is not simply removing CommRing from the unchanged theorem. The generator proof explicitly uses h. This covers additive-invertible shift elements in a semiring even when not every coefficient has an additive inverse. A family in AddUnits A could package this premise, but that encoding has not been compiled and is not claimed as verified evidence. Thus maximality is relative to the unchanged signature, not all representations. Arbitrary semiring translations are not asserted invertible/injective. [Raw conditional and ring specialization](../evidence/MvPolynomial.taylor_neg_taylor/native-raw-executed.lean.txt), [receipt](../evidence/MvPolynomial.taylor_neg_taylor/native-raw-success.json).

## Phase 4c — All nine modern-idiom rows

| # | Diagnostic | Assessment and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | Already CommRing, not an ad-hoc ring-axiom predicate. No replacement instance needed. |
| 2 | Sequences/metrics versus filters | No topology or convergence; n/a. |
| 3 | Construction versus universal property | Polynomial substitutions already use aeval/free-algebra uniqueness. The inverse calculation can be checked on generators; existing composition API supports that route. |
| 4 | Bundled structures | A new translation AlgEquiv is a useful alternative to the present AlgHom plus inverse law. Actually constructed with fresh left/right inverse proofs; generic symm_apply_apply then applies. It gives injectivity, surjectivity and inverse transport automatically. It is a new construction with obligations, not a currently existing mathlib replacement. |
| 5 | Field versus weaker hierarchy | Already CommRing, including positive characteristic and zero divisors. Conditional inverse pairs permit a separately restated semiring law, not a mechanical unchanged-statement weakening. |
| 6 | Higher-category presentation | No additional coherence or higher-category statement needed. Ordinary algebra equivalence is sufficient. |
| 7 | Concrete index | σ arbitrary; nothing numerical to generalize. |
| 8 | Concrete-via-abstract | Yes: proof body has zero literal taylor occurrences and uses the project composition law, plus implicit zero translation/cancellation. Abstract algebra equivalence yields inverse laws only after an equivalence is constructed; no shortcut that assumes its inverse fields. [diagnostic](../evidence/MvPolynomial.taylor_neg_taylor/proof-body-diagnostic.json) |
| 9 | False-generalisation guard | Preserve constant shifts, polynomial substitution and coefficient ring. Arbitrary semiring α with an invented negation, arbitrary unrelated β, and treating polynomial functions as formal polynomials are rejected. The conditional inverse-pair form includes an explicit cancellation premise; no unsupported semiring injectivity claim made. |

Modern packaging is available as a verified new bundle. It has concrete consequences for the immediate injectivity/zero-iff chain, but choosing the primary surface is an API judgment. No YES-generalise-first claim is made from packaging alone. [Bundle and full expansion caller](../evidence/MvPolynomial.taylor_neg_taylor/native-extra-executed.lean.txt), [receipt](../evidence/MvPolynomial.taylor_neg_taylor/native-extra-success.json).

## Phase 4.5 — All six infrastructure risks

Theorem-only n/a for each row: (1) typeclass diamonds, (2) reducibility/defeq abuse, (3) noncanonical data choices, (4) instance priority/search, (5) universe restrictions from new structure fields, (6) coercion diamonds. It creates no data or instance and has no simp attribute. The optional scratch AlgEquiv is an experiment, not installed production infrastructure; its future design is not silently accepted.

## Phase 4.6 — All five proof-strategy checks

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | No analysis; n/a. |
| 2 | Elements versus subobject inclusions | No ideal/submodule lattice argument; direct identity of substitutions is appropriate. |
| 3 | Sequences versus nets | No convergence; n/a. |
| 4 | Construction versus universal property | aeval composition and identity evaluation implement the free-algebra route. Fresh raw proof computes generators rather than doing coefficient induction. |
| 5 | Missing helper API | Generic equivalence cancellation already exists. Potential missing object is a multivariate shift AlgEquiv; its construction requires the inverse calculation under review. |

Strategy **MATHLIB-IDIOMATIC**. Existing short simplification is appropriate local code. Native raw normalization makes the mathematical obligations explicit without suggesting a verbose rewrite of production.

## Phase 5 — Five actual methods × three forms

[Raw exact formal requests/responses](../evidence/MvPolynomial.taylor_neg_taylor/formal-search.json). External indexes can differ from the pinned mathlib; native checks and pinned sources control positive claims.

| Method | Current inverse translation | Literature substitution inverse | Abstract algebra equivalence |
|---|---|---|---|
| Finder | Polynomial.taylorEquiv_symm, algEquivAevalXAddC_symm; univariate only. | Same plus affine one-variable substitutions. | algEquivOfCompEqX family; univariate, requires inverse composition premises. |
| LeanSearch | Polynomial.taylorEquiv, algEquivAevalXAddC and function-translation analogues. | One-variable shift equivalence, not multivariate target. | Polynomial.aeval_algEquiv, renameEquiv, coefficient-map equivalences: distinct operations. |
| Loogle | `MvPolynomial.aeval, "neg"` returns empty, not absence proof. | `Polynomial.taylorEquiv` returns exact univariate bundle and symmetry. | Initial `AlgEquiv, _ (_ _) = _` rejected because placeholder cannot be used as function; preserved, retry `AlgEquiv.symm_apply_apply` hit the 3/30s rate limit; final `"symm_apply_apply"` query succeeds and finds generic Equiv/EquivLike inverse cancellation. Native and pinned source establish the AlgEquiv specialization. |
| pinned rg | [current](../evidence/MvPolynomial.taylor_neg_taylor/rg-current.json) | [literature](../evidence/MvPolynomial.taylor_neg_taylor/rg-literature.json) | [abstract](../evidence/MvPolynomial.taylor_neg_taylor/rg-abstract.json) |
| local search | taylor_neg finds own project theorem. | taylorEquiv finds Polynomial bundle and symmetry. | symm_apply_apply finds generic AlgEquiv law. All local results index=unavailable; no indexed absence inferred. |

Untruncated namespace-aware [full-name search](../evidence/MvPolynomial.taylor_neg_taylor/rg-full-name.json) has no exact target in pinned mathlib. Pinned positive sources: [MvPolynomial Eval](../evidence/MvPolynomial.taylor_neg_taylor/MvPolynomial-Eval-module.lean.txt), [Basic](../evidence/MvPolynomial.taylor_neg_taylor/MvPolynomial-Basic-module.lean.txt), [Polynomial Taylor](../evidence/MvPolynomial.taylor_neg_taylor/Polynomial-Taylor-module.lean.txt), [Polynomial AlgebraMap](../evidence/MvPolynomial.taylor_neg_taylor/Polynomial-AlgebraMap-module.lean.txt), [AlgEquiv](../evidence/MvPolynomial.taylor_neg_taylor/AlgEquiv-module.lean.txt).

`Polynomial.taylorEquiv` at Taylor191 has invFun=taylorAlgHom(-r), with left/right inverse proofs. At Taylor201 its symmetry is taylorEquiv(-r). The native exact term `(Polynomial.taylorEquiv a).symm_apply_apply P` proves `Polynomial.taylor (-a) (Polynomial.taylor a P)=P` definitionally; this is a genuine one-call univariate result, **not** a direct replacement for arbitrary σ. `Polynomial.algEquivAevalXAddC` is another same-type univariate bundle. `MvPolynomial.renameEquiv` only renames variables and cannot shift generators by constants. Generic `AlgEquiv.symm_apply_apply` presupposes a bundle; constructing the new multivariate bundle is tested separately. Mode-B NO-parent re-aim rule does not apply: taylor's parent verdict was BORDERLINE, and this theorem is not rfl glue.

## Phase 5.5 — All three shape checks

Normal form: successive opposite translations reduce to P, the expected inverse-cancellation orientation. Equivalent LeftInverse and RightInverse forms are verified, with the latter obtained by negating α and normalizing double negation. Bundled `equivalence α` exposes the same mathematics; both inverse fields are proved independently, not assumed. Conditional αβ cancellation is a distinct hypothesis-based extension, not a defeq bridge. Superfluous-argument audit: σ,A,CommRing,α,P all serve the statement or fixed parent interface; none unused. **SHIP-AS-STATED mathematically**; future name/simp/bundle policy remains open.

## Phase 6.0 — Complete explicit caller and inline audit

There are **two explicit callers**, both in the declaring file, zero external-to-file callers; no simp attribute and no independent inline rederivation found. [Token search](../evidence/MvPolynomial.taylor_neg_taylor/rg-callers.json), [inline audit](../evidence/MvPolynomial.taylor_neg_taylor/rg-inline.json), [table](../evidence/MvPolynomial.taylor_neg_taylor/callers.json).

| Caller | Use, migration and actual verification |
|---|---|
| MvPolynomial.taylor_injective, Taylor188 | Passes taylor_neg_taylor α as a LeftInverse to Function.LeftInverse.injective. Replace by fresh inverse replay α, inline the composition/zero derivation, or use injectivity of a future independently verified translation AlgEquiv. Full caller and ensuing zero-iff proof compile against the fresh replay. |
| MvPolynomial.eq_sum_box_hasseDeriv, Taylor208 | Uses the inverse equality symmetrically to recover P from its translated monomial expansion. Replace `(taylor_neg_taylor α P).symm` by fresh replay's symmetry or future bundled inverse cancellation. Full actual coefficient/box/monomial expansion proof compiles with precisely that replacement. |

taylor_eq_zero_iff is a transitive consumer, and its Index consumers use that nonvanishing interface; they are not additional explicit inverse-law callers. Source search is not an exhaustive opaque kernel/simp dependency closure. Direct replay constant audit contains project composition/zero laws and arithmetic, but no call to the original inverse theorem. [Target and injective chain](../evidence/MvPolynomial.taylor_neg_taylor/native-target-executed.lean.txt), [success](../evidence/MvPolynomial.taylor_neg_taylor/native-target-success.json), [full expansion caller](../evidence/MvPolynomial.taylor_neg_taylor/native-extra-executed.lean.txt), [success](../evidence/MvPolynomial.taylor_neg_taylor/native-extra-success.json).

## Phase 6 — Actual composition experiments

1. Fresh original-shaped replay `by simp [taylor_taylor]` succeeds, with no use of the target theorem. This is short **project** composition: project taylor_taylor and project taylor_zero are not existing mathlib facts. Counting them as two mathlib calls would be invalid.
2. The raw **directInverse** proof actually closes using only mathlib: `by simp [shift, comp_aeval_apply, add_assoc, aeval_X_left_apply]`. This independently establishes the Phase-6b closing-simp signal; it does not rely on the previously assessed project composition law. Its short tactic syntax does not count as a ≤3 mathematical-fact exact composition.
3. Mathlib-only raw substitute defines shift=aeval(X+Cα), guards the missing project target, proves a conditional inverse over CommSemiring, then specializes β=−α over CommRing. Generator cancellation uses add_assoc, map_add, h, map_zero, add_zero; substitution transport uses comp_aeval_apply, map_add, aeval_X, algHom_C, and final aeval_X_left_apply. This is more than three mathematical facts, plus congrArg/funext/trans structural plumbing. The source does not hide a three-call term or claim the normalization is definitional.
4. Exact existing univariate inverse compiles via taylorEquiv.symm_apply_apply. It cannot directly apply to MvPolynomial σ A for arbitrary σ; no type-changing univariate equivalence makes it a one-call arbitrary-variable replacement.
5. New multivariate AlgEquiv compiles using fresh LeftInverse/RightInverse proofs. Its generic inverse application closes in one call **after those obligations**; circularly bundling the desired theorem does not demonstrate an existing mathlib composition.
6. Both explicit actual callers compile with fresh inverse proof, and the immediate zero-iff chain remains valid. Fixed-interface CommSemiring-only guard fails as expected.

All three accepted native runs are complete, success=true, partial=false, no errors/warnings, standard axioms only. No rejected native attempts, no sorry/admit/new axioms/unsafe/native_decide or raised limits. [Raw exact source](../evidence/MvPolynomial.taylor_neg_taylor/native-raw-executed.lean.txt), [raw receipt](../evidence/MvPolynomial.taylor_neg_taylor/native-raw-success.json), [verification inventory](../evidence/MvPolynomial.taylor_neg_taylor/verification.json).

Conclusion: **BORDERLINE-trivial-simp under Phase 6b**, not NO-composable: the demonstrated explicit generator proof exceeds three existing mathematical facts, while the independent mathlib-only directInverse closes by simp [defs] and triggers Phase 6b. Not automatically YES-generalise-first: the conditional inverse-pair formulation is a genuine verified broader mathematical statement; it does not mechanically drop a hypothesis from the unchanged negative-vector signature. More decisively, the current short closing-simp law still raises the Phase-6b API judgment whether a separate pointwise theorem, conditional variant, or bundled inverse interface merits upstream exposure. This broader form is retained as positive evidence rather than dismissed on cost or inconvenience. Not automatic YES from useful callers: elementary opposite-shift cancellation may belong as a corollary of a bundled API. This judgment is independent of the parent verdict and not based on cost.

## Phase 7 — Actionable verdict and gate

**BORDERLINE-needs-human.** Real API use and univariate precedent support keeping an inverse interface; the generic substitution derivation and closing-simp proof make its separate upstream status a presentation question. Future upstream choices, each answerable briefly:

1. Should the named multivariate translation API expose this inverse law, matching the univariate taylorEquiv interface?
2. Should the primary ring-level API be a new translation AlgEquiv, with the pointwise inverse theorem as a corollary?
3. Should inverse cancellation be a simp lemma, and should name/orientation follow taylorEquiv.symm_apply_apply?

Recommended concrete next action: retain the theorem locally in Roth/Taylor.lean during this survey. If a named multivariate Taylor API is proposed upstream, implement the verified bundle and settle these three API choices as one coherent translation proposal; migrate the two callers only with dependent validation/full build. If named convenience laws are declined, inline the tested composition/zero derivation at Taylor188 and Taylor208. Generic mathlib equivalence laws already exist; no new generic inverse theorem is needed. Archive/ or another satellite library adds no value for this local elementary interface. No PR, source edit or external communication is performed.

Gate: full literature table, all parameter/modern/proof/shape rows, actual 5-method search on three forms, two complete caller rows, raw composition evidence and three numbered API questions are present. Future design questions are not unfinished verification: unresolved=[]; no user response needed to publish this completed read-only assessment.

## Phase 8 — Evidence and handoff

[Assessment](../evidence/MvPolynomial.taylor_neg_taylor/assessment.json), [full overview entry](../evidence/MvPolynomial.taylor_neg_taylor/overview-entry.json), [current manifest](../evidence/MvPolynomial.taylor_neg_taylor/copy-manifest.json), [portable read-only validator](../evidence/MvPolynomial.taylor_neg_taylor/validate.py), and exact native/formal/literature evidence preserve the completed assessment. Root acceptance remains pending until independent review. All supporting files are intended for Git tracking only after that acceptance; no partial checkpoint is requested.
