from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.exists_hasseDeriv_eval_ne_zero'
def link(n,t=None):return '['+(t or n)+'](../evidence/'+N+'/'+n+')'
t=json.loads((D/'native-type.json').read_text())['type']
text='''# Roth.exists_hasseDeriv_eval_ne_zero — canonical254

Verdict: **NO-mathlib-has-it**, independently verified by re-aiming at `AddMonoidAlgebra.infDegree`. Its strict-cutoff witness law is exactly `Finset.inf_lt_iff`. This is an upstream redundancy judgment; keeping a project-local Hasse/index convenience theorem is a separate choice. No production sources, pins, tracked overview files, or Git were changed.

## Phase0 — baseline and scope

The shared baseline is a successful `lake build` (2467 jobs). All17 production-source/pin SHA256 values were freshly compared and match. No file-end build is due for254; the accepted full Theta228 build is prior evidence, not a new build here. The target resolves at `Roth/MainLemma.lean:454`, public theorem. The full762-line declaring module and actual private caller/main continuation were read and replayed. There are no sorries in accepted evidence.

EVIDENCE_BASELINE

## Phase1 — statement and proof

For a nonzero polynomial P, its index at α is the least weight of a nonzero coefficient of P(X+α), equivalently of a nonvanishing Hasse derivative at α. If that least weight is strictly below c, then one such derivative has weight strictly below c. The theorem selects a minimum-attaining derivative and transfers the inequality along its weight equality; it does not prove minimum attainment again.

Full elaborated kernel type, obtained via `Lean.getConstInfo` with `pp.funBinderTypes`:

```lean
FULL_TYPE
```

Parameters: universe-polymorphic variable type σ; `[Fintype σ]` for current weight/index signatures; P over ℝ; hP nonzero; arbitrary point α; natural vector r allowing zero entries; real cutoff c and strict index bound hc. The witness k is a finitely supported natural multi-index. Both zero weights and empty σ are allowed.

The original source body is `(exists_weight_eq_index hP α r).imp ...`. The native full type and complete small kernel body were captured without printer elision. Kernel body dependencies include `Roth.index`, `MvPolynomial.hasseDeriv`, `Roth.weight`, `Roth.exists_weight_eq_index`, plus a generated match helper. The only explicit source proof call is `exists_weight_eq_index`. This distinguishes type/body dependencies from lexical calls.

EVIDENCE_ORIGINAL

## Phase2 — preliminary checks

**SMALL:** one existential corollary, not a named main theorem or new structure. The substantive body is one expression over two source lines. The one-line *definition* test and its defeq/diamond/API exemptions are n/a: this is a theorem. A short proof using a project lemma is not evidence of a mathlib composition.

## Phase3 — exhaustive literature

All named channels were actually attempted; three distinct general queries cover the exact Roth form, Hasse/Taylor multiplicity generality, and the abstract finite minimum law. Exact requests and response SHA256/byte/status metadata are retained; no full article or search-result bodies are archived. Returned URLs are clean locator URLs; query parameters were omitted. Optional `ask_chatgpt_math` is unavailable, documented n/a, with no reduction to other channels.

| Channel | Actual request / finding | Receipt |
|---|---|---|
| General specific | Roth theorem polynomial index nonvanishing derivative weighted order strict cutoff. Roth1958 ICM p206 search snippet defines index via minimal nonvanishing derivative order. | WEB_general1 |
| General generality | Hasse derivatives order vanishing multivariate polynomial Taylor expansion arbitrary characteristic. Algebraic Taylor coefficient interpretation is characteristic-independent. | WEB_general2 |
| General alias/order | finite infimum minimum strict inequality exists element below bound. General infimum/minimum references, not a distinct named Roth result. | WEB_general3 |
| Local | clean.tex530–553 gives weighted minimum, finite attainment and source index0=∞;1526–1537 explicitly selects the low-weight derivative. | LOCAL |
| nLab | `site:ncatlab.org/nlab order of vanishing valuation polynomial`; valuation context, no exact target hit. | WEB_nlab |
| nCatLab distinct | `site:ncatlab.org/ncatlab Hasse derivative order of vanishing`; returned /nlab pages are out of requested namespace, not an exact nCatLab hit. | WEB_ncatlab |
| Stacks | `site:stacks.math.columbia.edu order vanishing Taylor polynomial derivative`;02MB defines local order using module length, a related but different construction. | WEB_stacks |
| MathOverflow | `site:mathoverflow.net Hasse derivative multiplicity multivariate polynomial`; multiplicity/derivative discussions, not exact cutoff law. | WEB_mathoverflow |
| Recent arXiv | `site:arxiv.org Hasse derivatives multiplicity polynomial after:2021-10-29 before:2026-10-30`; He–Pham–Xu2201.06156 and Ghosh2402.18717 concern Hasse multiplicity; unrelated Hasse-principle results rejected. | WEB_arxiv |
| Primary follow-up | Roth ICM PDF fetch failed size limit74,705,952bytes; nLab fetch failed XHTML content type. Stacks02MB and2022 arXiv abstract accessed successfully. | WEB_primary |
| Optional mathematical second opinion | n/a: `ask_chatgpt_math` unavailable. | protocol |

Literature summary: **weighted order of vanishing / polynomial index**, with a strict-cutoff consequence of finite minimum. The standard arithmetic exposition uses positive real denominators, while current natural r admits zero denominators under totalized division. Hasse/Taylor coefficients support arbitrary commutative rings, and the underlying finite support order law supports arbitrary linearly ordered top-valued weights. Source convention index0=∞ differs from project index0=0. This assessment keeps the latter exactly in recovery. No source was taken as authority for the false claim that positive-denominator power-series weightedOrder replaces the all-r interface.

## Phase4a–4b — generality

| Parameter/hypothesis | Assessment and compiled evidence |
|---|---|
| σ universe | Already `Type*`; abstract cutoff has independent I/A/L universes. |
| Fintype σ | Required to write existing `weight` and `index`; not mathematically needed for a polynomial's finite support. `Witness254Project.generalized` compiles for arbitrary σ with a real cost D on finitely supported exponents. This is a representation restatement, not silently deleting a needed binder. |
| Real coefficients | Not used by finite minimum reasoning. Generalized Taylor/Hasse form compiles over arbitrary `[CommRing A]`; abstract infDegree form over `[Semiring A]`. No unnecessary domain, characteristic-zero, or Nontrivial assumption. |
| hP nonzero | Essential in the old real zero-default index: P=0, c=1 satisfies hc and has no nonzero derivative. Native counterexample. In top-valued infDegree, a strict bound itself rules out empty support, so no hP is needed. |
| α | Arbitrary point, already point-local; no analytic regularity. |
| r : σ→ℕ | No positivity needed. All-r recovery proven through WithTop ℝ infDegree and `untopD 0`, without a denominator product. Abstract D may be any cost on exponents, even nonadditive. Arithmetic positivity matters only for separate index_nonneg control. |
| c : ℝ | Re-aim supports arbitrary `[LinearOrder L] [OrderTop L]`. Real-valued projection separately proved. |
| hc strict | Cannot replace < by ≤ while keeping < in the witness. P=1,c=0 is the compiled counterexample. A weak witness law has its own existing `Finset.inf'_le_iff`. |
| Empty σ / allzero r | Nonzero constants have order0 witness for any c>0; native controls cover both. Mixedzero r is included in the quantified all-r recovery. |
| c≤0 | Impossible under hc since current index is nonnegative; compiled using `index_nonneg`. |

Generality verdict: **STRICTLY NARROWER as a representation than the verified existing abstract standard law**; the old project interface retains Fintype/ℝ by its definitions. The proof `Witness254Project.generalized` establishes the actual arbitrary-variable polynomial version, not merely a prose localization claim. The abstract re-aim is already in mathlib, so this does not justify YES-but-generalise-first. New projected/translation helpers used in experiments are explicitly new proofs, not alleged mathlib declarations.

Compiled abstract re-aim (complete body, one existing mathlib call):

```lean
theorem abstract_cutoff {I A L : Type*} [Semiring A] [LinearOrder L] [OrderTop L]
    (D : I → L) (P : AddMonoidAlgebra A I) (c : L) :
    AddMonoidAlgebra.infDegree D P < c ↔ ∃ i ∈ P.coeff.support, D i < c :=
  Finset.inf_lt_iff
```

The coefficient-nonzero version uses `Finsupp.mem_support_iff`. Project index recovery first normalizes the support minimum to `(infDegree (fun d ↦ (weight r d : WithTop ℝ)) (taylor α P)).untopD 0`, then uses finite nonempty projection and `coeff_taylor`. The bridge also handles P=0 as an equality of values, but nonempty support is needed to recover a witness from the defaulted real value. `Witness254Project.recovery` has exactly the original full type; `contraposition` separately derives it from project `le_index_iff`. Neither proof invokes the target.

EVIDENCE_PROJECT

## Phase4c — all nine modern idiom checks

| # | Question | Answer / consequence |
|---|---|---|
|1| Typeclass/instance preambles | Already Fintype; abstract Semiring/LinearOrder/OrderTop classes are genuine available generality. No global new instance needed. |
|2| Filters/nets | No: finite support/order assertion, no convergence. |
|3| Universal property | No new construction to characterize; finite infimum uses existing order universal property. |
|4| Bundled substructure | Yes at representation layer: use existing AddMonoidAlgebra coefficients/support and Finset.inf instead of a separately named real sInf index. No new subring/submodule is warranted. |
|5| Hierarchy weakening | Yes: polynomial ℝ→CommRing A and finite-support Semiring A versions actually compile; Hasse avoids factorial inversion. |
|6| Higher categories | No: no categorical content. |
|7| Concrete order/cost | Yes: arbitrary top-valued linear order and arbitrary exponent cost in abstract_cutoff, existing Finset API. |
|8| Concrete-via-abstract diagnostic | Fires: after `exists_weight_eq_index` the one-expression body mentions only witness components, equality transport and hc. `index`, `weight`, and `hasseDeriv` each have zero literal proof-body occurrences. The exact original proof's project parent encapsulates the support normalization; this observation alone does not count as an existing-mathlib composition. Generic proof independently verifies the abstraction. |
|9| False-generalization guard | Reject dropping hP from old index, or weakening hc while retaining strict witness, or replacing all-r weights with positive-denominator-only weightedOrder. Preserved semantics in compiled projection/generalized proofs; native counterexamples cover rejected proposals. |

Modern-idiom verdict: re-aim at existing **infDegree / finite support infimum**. It enables `Finset.inf_lt_iff` and `inf'_lt_iff` directly, arbitrary costs and variables, and the empty support top convention. It supplies real downstream reuse, not cosmetic repackaging. The separate defaulted real projection is documented. No new strict-cutoff theorem is needed upstream.

## Phase4.5 — infrastructure risk6

Theorem, so all six infrastructure rows are justified n/a: (1) no instance paths/diamond; (2) no new reducible definition; (3) no computational unfolding choice; (4) no instance priority; (5) no data universes/coercion forced by a construction; (6) no CoeFun/CoeSort. Existing polymorphic types are validated by the generalized native proofs. Overall n/a, not a claim about the risk of redesigning index itself.

## Phase4.6 — proof strategy5

| # | Check | Answer |
|---|---|---|
|1| Topology ε–δ vs filters | No topology. |
|2| Elementwise algebra vs substructure | No ideal/submodule argument; support membership is the existing finite infimum form. |
|3| Analysis sequences vs nets | No limits. |
|4| Construction vs universal property | Existing finite infimum universal property gives the witness law; no object construction gap. |
|5| Missing helpers mathlib should have | No missing order witness API. Project Taylor/Hasse coefficient bridge and zero-default projection remain separate normalization work; scratch helpers are not existing API. |

Strategy verdict: **MATHLIB-IDIOMATIC** within current project API (attained minimum then strict transfer); for re-aimed upstream statements use existing infimum law. The tested contraposition route is valid but uses a project theorem, not evidence for a mathlib-only NO-composition.

## Phase5 — all15 formal search cells

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current Hasse/index witness | SEARCH_current_leanfinder | SEARCH_current_loogle | SEARCH_current_leansearch | SEARCH_current_rg | SEARCH_current_local_search |
| Standard finite minimum strict cutoff | SEARCH_standard_leanfinder | SEARCH_standard_loogle | SEARCH_standard_leansearch | SEARCH_standard_rg | SEARCH_standard_local_search |
| Abstract infDegree/support cutoff | SEARCH_abstract_leanfinder | SEARCH_abstract_loogle | SEARCH_abstract_leansearch | SEARCH_abstract_rg | SEARCH_abstract_local_search |

Finder standard initial request timed out; successful retry finds `Finset.inf'_lt_iff` and `Finset.inf_lt_iff`. Current local index was warming and returned project/evidence names; these are not mathlib declarations and no absence claim uses that result. External indexes may differ from the pin. All raw search receipts retained, and positive signatures verified natively against the pin. The full-name rg has no truncation; failure to find a named multivariate project spelling is not used as proof of absence.

Pinned hits: `AddMonoidAlgebra.infDegree` at Degree.lean:624 (abbrev to coefficient-support infimum); `Finset.inf_lt_iff` generated by to_dual at Fold.lean:477; `Finset.inf'_lt_iff` generated at Fold.lean:753; `Finset.inf'_eq_csInf_image` in ConditionallyCompleteLattice/Finset.lean; `Finsupp.mem_support_iff`; `Finset.coe_inf'` and `WithTop.untopD_coe`. The isolated source imports exactly the stable18 mathlib prefix, guards both target and project taylor as missing, and reconstructs translation from genuine `MvPolynomial.aeval`, X and C. Its scratch `translate`, projection and bridge theorems are new, clearly labeled.

Search conclusion: **found in mathlib as `Finset.inf_lt_iff`, the more general analogous law on `AddMonoidAlgebra.infDegree`**. This is not a claim that mathlib already has the project's Hasse/Taylor spelling. EVIDENCE_ISOLATED

## Phase5.5 — statement shape3

1. Normal form: finite-support infDegree / Finset.inf is the existing canonical order form. Real sInf and derivative evaluation are equivalent project-facing forms through an explicit bridge. The theorem is existential, so RHS normal-form convention for iff is n/a; the abstract equivalence puts the witness on RHS exactly as existing Finset API.
2. Syntactic alternatives actually tried: attained-minimum transfer (original), `le_index_iff` contraposition (exact type), Finset.inf'_lt_iff support witness (full caller inline), and projected infDegree witness (exact recovery). The full caller consumes weight-first/nonzero-second, so that conjunction order is convenient locally. The canonical iff already exists; no separate upstream implication needed.
3. Superfluous arguments: hP essential in old spelling; hc strict essential; α/r are semantic data; σ universe already general; Fintype and ℝ fixed by old index interface but absent/weakened in compiled generic form. There is no extra hr>0 or positive c premise to drop. Overall **RESTATE-BEFORE-SHIP** toward existing infDegree; upstream action is reuse, not a new theorem.

## Phase6.0 — complete caller and inline audit

Internal use count excluding declaring file: **0**. External-to-file callers: **0**. Total actual proof uses excluding declaration: **1**.

| Caller | Use and verified refactor |
|---|---|
| MainLemma.lean:486, private `exists_hasseDeriv_index_eval_bound_aux` declared477 | Cast nonzero P over ℤ to ℝ; choose k; set Q=Δ_kP over ℤ; preserve degree bound, nonzero evaluation, strict index gap and all Hasse bounds. Full original module replay replaces the call with nonempty translated support, `Finset.inf'_eq_csInf_image`, `Finset.inf'_lt_iff`, then `coeff_taylor`. |
| MainLemma.lean:752, `main_lemma` declared735 (indirect continuation) | Calls the private result at midpoint cutoff c; continuation replayed whole, with original main type definitionally equal. This is not counted as a second direct use. |

Fresh `rg --no-ignore` and tracked `git grep` agree. Inline-equivalent search found stronger attained-minimum and lower-bound characterization APIs in Index.lean; no second source rederivation of this exact strict-cutoff statement. Native audit covers exactly293 canonical names in tracked order, unique/present/value293, with one direct value and zero direct type consumers. It is not a global simp or transitive dependency count. Target has no simp attribute; no simp-closure claim. Main is a known transitive continuation; no exhaustive environment-transitive-closure claim is made.

The full caller and main signatures were checked by kernel definitional equality against original constants (private original accessed by `Lean.mkPrivateNameCore`). The new module contains no target reference in mathematical declaration bodies and neither new caller/main body directly references target. Importing the project makes its old declarations available; this is actual-context evidence, not mathlib-only replacement evidence.

EVIDENCE_INLINE

## Phase6 — composition experiments

- **Original spelling:** **NOT-COMPOSABLE in ≤3 existing-MATHLIB calls as written**. The two-line original uses project `exists_weight_eq_index`; contraposition uses project `le_index_iff`. Neither is a mathlib building block. The full inlining requires support nonempty, finite sInf normalization, cutoff witness, and Taylor/Hasse membership normalization. Compiled projected infDegree recovery likewise contains new explicit bridges.
- **Re-aimed infDegree statement:** one exact existing call, `Finset.inf_lt_iff`; no new order proof. This is a **hit on the analogous law**, not a cost-based judgment or merely closing `simp [defs]`.
- **Real projected version:** nonempty support + `Finset.coe_inf'`, `WithTop.untopD_coe`, `Finset.inf'_lt_iff`, and membership conversion. The new scratch projection helper is not counted as mathlib. P=0 exposes why projection needs care.

This differs from canonical252 `le_index_of_forall_eval_eq_zero`: that theorem restricts the supplied vanishing checks to a degree box and needs a separate support/degree confinement argument. This254 witness is unrestricted in k, so the infDegree analogue is already precisely the existing strict infimum witness law. Both judgments were independently checked; the parent's verdict was not inherited.

## Phase7 — rationale and actionable verdict

**NO-mathlib-has-it under the explicit ModeB re-aim rule.** The parent index was assessed against existing infDegree. Re-aiming this dependent strict witness law gives `infDegree D P < c ↔ ∃ i∈support, D i<c`, whose proof is literally the existing `Finset.inf_lt_iff`. This hit is native-verified over arbitrary semiring coefficients, index types and linear top-valued orders. The exact old theorem is recovered with all-r real projection and actual Taylor coefficient bridge, with original signature checked. It is not a new generic theorem or a three-call claim about the old spelling.

WHY not add: a separate strict finite-infimum witness lemma would duplicate already available Finset API. The project wrapper packages semantic normalization around that law. Its one existing local use makes a local convenience reasonable, but does not create new upstream order content. There is no unresolved design question or cost-based downgrade.

**Refactor plan for the sole direct caller MainLemma:486:** while keeping the current index interface, inline the original project attained-minimum `.imp` expression, or use the fully verified finite-support inline block in inline-executed.lean.txt. For coordinated parent infDegree migration, express the cutoff as support infDegree, apply `Finset.inf_lt_iff` (or real `inf'_lt_iff` after projection), and convert nonzero coefficient to Hasse evaluation via the retained Taylor/Hasse bridge. Keep all subsequent Q construction, degree, evaluation and index estimates unchanged. `main_lemma` at752 keeps its current signature and midpoint argument. After updating that one direct use, delete the wrapper if minimizing local API is desired.

**Belongs elsewhere / local retention:** `Roth/Index.lean` beside `exists_weight_eq_index` is a sensible local home if the convenience theorem is retained; it is used, not dead code. The assessment does not authorize source changes. No YES PR title, grouping or reviewer selection is applicable.

## Phase8 — verification and completion

Four accepted exact sources: original full module replay/canonical audit; isolated mathlib-only re-aim and projection; actual project recovery/generalization/boundary controls; full module caller inline/main continuation. All clean/nonpartial, no warnings/errors, only propext/Classical.choice/Quot.sound. Complete original type/body and standard axioms captured without elision. Rejected attempts remain separately archived: isolated missing nonempty/projection syntax, inline audit syntax/opaque-value-access failure, and a disclosed accidental stale diagnostic query after a failed width preparation. None contributes accepted evidence; the rejected panic output contains printer elision and is not represented as a full dump. Subsequent successful preparation preceded the clean accepted execution.

Fresh17 inputs, pinned mathlib excerpts, exact canonical293 source/order/runtime counts, all15formal cells, all named literature channels, report links, secret guard and current copy-manifest are validated in scratch and a simulated integrated layout. The portable validator uses the current copy-manifest; a historical worker manifest cannot substitute. Root acceptance is pending independent review. Native ownership is released only with the final frozen-package handoff.

EVIDENCE_FINAL
'''
text=text.replace('FULL_TYPE',t)
text=text.replace('EVIDENCE_BASELINE','Evidence: '+', '.join(link(n)for n in ['inputs.json','baseline-build.txt','source-MainLemma.lean.txt'])+'.')
text=text.replace('EVIDENCE_ORIGINAL','Evidence: '+', '.join(link(n)for n in ['original-executed.lean.txt','original-receipt.json','native-type.json','dependencies.json'])+'.')
text=text.replace('EVIDENCE_PROJECT','Evidence: '+', '.join(link(n)for n in ['project-executed.lean.txt','project-receipt.json'])+'.')
text=text.replace('EVIDENCE_ISOLATED',link('isolated-executed.lean.txt')+'; '+link('isolated-receipt.json')+'.')
text=text.replace('EVIDENCE_INLINE','Evidence: '+', '.join(link(n)for n in ['inline-executed.lean.txt','inline-receipt.json','canonical-consumers.json','callers.json','scope-audit.json'])+'.')
text=text.replace('EVIDENCE_FINAL','Evidence: '+', '.join(link(n)for n in ['verification.json','assessment.json','validate.py','validation-receipts.json','secret-guard.json','copy-manifest.json'])+'.')
for x in ['general1','general2','general3','nlab','ncatlab','stacks','mathoverflow','arxiv','primary']:text=text.replace('WEB_'+x,link('web-'+x+'.json'))
text=text.replace('LOCAL',link('local-excerpt.tex.txt')+' / '+link('literature-local.json'))
for f in ['current','standard','abstract']:
 for m in ['leanfinder','loogle','leansearch','rg','local_search']:text=text.replace('SEARCH_'+f+'_'+m,link('search-'+f+'-'+m+'.json',m))
text+='\nStandard Finder retry: '+link('search-standard-leanfinder-retry.json')+'.\n'
(D/'report.md').write_text(text)
print('PASS report written',len(text),'characters')
