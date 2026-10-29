from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.le_index_of_forall_eval_eq_zero'
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
type_=json.loads((D/'native-type.json').read_text())['type'];dep=json.loads((D/'dependencies.json').read_text())
questions=[
'After migrating the parent to existing infDegree, should the bounded derivative-check wrapper remain project-local, with callers using the shared support/degree bridge?',
'If a public multivariate Hasse/Taylor package is contributed, should it expose this bounded-box lower-index criterion in addition to an unrestricted coefficient-vanishing criterion?',
'Should a future public criterion use arbitrary real-weight support minima with a separate zero-default projection, or use top-valued infDegree as its primary interface?']
phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']}
put('assessment.json',dict(declaration=N,canonical_index=252,kind='theorem',verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,justified_na={'2b':'Theorem, not a definition: substantive one-line definition test and its three exemptions n/a.','4.5':'Theorem introduces neither definitional computation nor instances; all six infrastructure risk categories n/a.','ask_chatgpt_math':'Unavailable optional tool.'},unresolved=[],root_acceptance='pending',questions=questions,cost_based_verdict=False,parent_verdict_inherited=False,composition='NOT-COMPOSABLE as exact original from ≤3 existing mathlib calls; existing infDegree support-order core is COMPOSABLE after supplying substantive support normalization.'))
put('overview-entry.json',dict(type=type_,kind='theorem',what='For a nonzero real multivariate polynomial within coordinate degree bounds, vanishing of the in-box Hasse derivatives strictly below a real weight cutoff forces the index to be at least that cutoff.',how='A nonzero evaluated Hasse derivative cannot exceed a coordinate degree. Apply the project le_index_iff characterization and contrapose the strict cutoff condition; excessive orders vanish by hasseDeriv_eq_zero_of_degreeOf_lt.',hypotheses=['P is nonzero; index of zero is defined as 0.','Every coordinate degree is bounded by r.','Only derivative orders in the box and of weight strictly less than c must vanish.','The existing index/weight interface requires Fintype σ; α and c are arbitrary and r may contain zeros.'],project_dependencies=dep['canonical_body'],caller_summary='One source proof call and one canonical kernel-value consumer: private exists_mem_RSet_le_index_aux at MainLemma:562; no external-to-file source calls or direct type consumers. Full caller inlining and entire module continuation through main_lemma compile with the original caller signature.',mathlib_api_audit='Existing le_of_not_gt is only scalar contraposition. Finset.le_inf_iff/le_inf and AddMonoidAlgebra.infDegree already supply the abstract support lower bound; a three-call bounded-support check compiles once support⊆test-set is given. MvPowerSeries.nat_le_weightedOrder/le_weightedOrder are natural-weight/top-valued alternatives. Project Hasse/Taylor support normalization is still needed for the exact bounded derivative theorem.',moral_duplications=['le_index_iff supplies unrestricted nonzero-derivative bounds, not bounded checking.','eq_sum_box_hasseDeriv and degreeOf_taylor_le share out-of-box annihilation but conclude reconstruction/support confinement.','exists_hasseDeriv_eval_ne_zero is the complementary strict upper-cutoff witness theorem.'],generalization='Verified cutoff-local outside-box degree condition, or outside-box evaluated annihilation, weakens the global degree premise. New finite-support observation proofs work over arbitrary Zero coefficients and conditionally complete linear ordered weights; arbitrary-variable/CommRing polynomial indexAny recovers the exact original via finite-support weights. Fintype cannot simply be deleted from the unchanged parent signatures.',missing_api='Potential discoverability for bounded Hasse/Taylor support checking, not a missing finite-infimum order law. Upstream choice between a public boxed convenience theorem and local use of shared support bridges remains a taste/API question.',junk='Not dead code: the sole caller converts pigeonhole remainder equalities into the key index bound. Full inlining works but duplicates the degree-box proof; one use alone does not establish ≤3-mathlib-call composability.',action='BORDERLINE-needs-human; retain production unchanged. Decide the three concrete future upstream API questions after considering the verified generic support formulation and parent infDegree migration. No question blocks completion of this assessment.'))
report=r'''# Roth.le_index_of_forall_eval_eq_zero — full assessment

**BORDERLINE-needs-human.** The order-theoretic core already belongs to mathlib's finite-support infimum API. This theorem additionally turns bounded Hasse derivative tests into the correct weighted-order conclusion by proving that all relevant nonzero derivatives lie in the degree box. The open upstream choice is whether that boxed polynomial convenience interface deserves a public lemma alongside the general support API. This is an independently completed assessment, not a cost verdict or an inherited verdict from `index`/`le_index_iff`.

## Phase 0 — Doctor and controls

Canonical252 is the public theorem at `Roth/MainLemma.lean:419`. The entire declaring module, original index/weight definitions, Hasse degree annihilation, sole actual caller and its continuation to `main_lemma` were read. [Full module](../evidence/NAME/source-MainLemma.lean.txt), [Index](../evidence/NAME/source-Index.lean.txt), [Box](../evidence/NAME/source-Box.lean.txt), [Taylor](../evidence/NAME/source-Taylor.lean.txt), [Hasse derivatives](../evidence/NAME/source-HasseDeriv.lean.txt).

The shared baseline is exit0, clean2467jobs; all17 source/pin hashes freshly match. [Baseline](../evidence/NAME/baseline-build.txt), [fresh inputs](../evidence/NAME/inputs.json). The accepted file-end build throughTheta228 remains applicable; no new file-end build is required at252. No production, pin, tracked overview or Git edits were made. Stable18 mathlib-only imports and nine persistent disk imports were preserved.

## Phase 1 — Content and full kernel statement

Let P be nonzero and have coordinate degrees at most r. If each Hasse derivative whose order lies in the degree box and whose reciprocal-weight sum is strictly below c vanishes at α, then the weighted index of P at α is at least c. Outside-box orders need no supplied vanishing proof: some order exceeds a coordinate degree, so that derivative is identically zero. No positivity of r or c, nonempty variable type, or diagonal restriction on α is assumed.

```lean
FULLTYPE
```

σ is universe-polymorphic; Fintype supplies the present global weight sum; P has real coefficients; r supplies natural denominator weights (division by0 contributes0); α is an arbitrary point; c is any real cutoff. hP guards the project's real zero-default index; hd bounds every coordinate degree; hvan is the in-box strict-cutoff predicate.

The source proof applies project `le_index_iff`, contraposes scalar order with existing `le_of_not_gt`, and obtains the in-box condition from project `hasseDeriv_eq_zero_of_degreeOf_lt`. Complete source, kernel body/type, standard axioms and exact293 ordered canonical audit are in [original source](../evidence/NAME/original-executed.lean.txt) and [raw native receipt](../evidence/NAME/original-receipt.json). No printer elision occurred. One initial cold partial timeout is preserved separately and is not accepted verification. Native type is read with `Lean.getConstInfo.type` and `pp.funBinderTypes`, not split from a printed body.

[Dependencies](../evidence/NAME/dependencies.json) distinguish lexical spelling from complete kernel constant lists. Canonical body constants are `Roth.weight`, `MvPolynomial.hasseDeriv`, `Roth.index`, `Roth.le_index_iff`, and `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`; type constants among canonical declarations are weight, Hasse derivative and index. This list includes constants introduced through elaboration of binders, not just the two named proof lemmas.

## Phase 2 — Preliminary checks

SMALL: a helper extracting the index conclusion from the pigeonhole step, not a named theorem or a new structure. The module's main named result is `main_lemma`. Full literature/search phases still run. One-line definition test and its defeq/diamond/stable-name exemptions: n/a, theorem kind; a short theorem proof is not the one-line-definition prefilter.

## Phase 3 — Exhaustive literature

Exact requests, responseSHA256/bytes/status, sanitized locators and original summaries are retained; full search/article bodies are not archived. [Protocol](../evidence/NAME/literature-protocol.json).

| Channel | Actual query or locator | Finding |
|---|---|---|
| General specific | `polynomial Roth index vanishing derivatives weighted index coordinate degrees` | [Roth, ICM1958 p.206](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) describes the least weighted nonvanishing derivative order. Full PDF open failed because its74,705,952bytes exceed fetch limits; search excerpt only. [Receipt](../evidence/NAME/web-general1.json). |
| General general | `weighted order vanishing Taylor coefficients below threshold multivariate polynomial arbitrary field Hasse derivatives` | [Tang, Multijoints and Factorisation](https://link.springer.com/article/10.1007/s12220-023-01469-6), §3.1, works over arbitrary fields and defines Hasse derivatives by translated coefficients. This supports coefficient generality without using ordinary derivative division. [Receipt](../evidence/NAME/web-general2.json). |
| General aliases | `multiplicity polynomial Hasse derivatives lower set support weighted valuation` | Multiplicity-code/polynomial-method sources frame multiplicity as vanishing of lower-order Hasse derivatives. These are related formulations, not an exact zero-denominator real-index API. [Receipt](../evidence/NAME/web-general3.json). |
| Optional ChatGPT math | standard form/generality/history | n/a: ask_chatgpt_math unavailable. No answer invented. |
| Local manuscript | clean.tex §4 lines530–556, §6 line1511 | Finite nonzero derivative support gives the minimum; §6 explicitly combines the tested derivatives and identically zero outside-box derivatives to infer the index bound. Source uses positive real r and zero value+∞; current Lean uses natural r with zeros allowed and real zero value0. [Search](../evidence/NAME/literature-local.json), [excerpt](../evidence/NAME/local-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab order of vanishing Hasse derivative` | Hasse–Schmidt derivative/derivation pages give Taylor context. Direct XHTML open is unsupported; no exact bounded criterion claimed. [Receipt](../evidence/NAME/web-nlab.json). |
| Distinct nCatLab namespace | `site:ncatlab.org/ncatlab weighted order vanishing polynomial` | Executed exact namespace query; returned /nlab pages/files are outside requested namespace. No exact /ncatlab hit; no absence inference. [Receipt](../evidence/NAME/web-ncatlab.json). |
| Stacks | `site:stacks.math.columbia.edu order vanishing polynomial Taylor coefficient` | [Tag02MB](https://stacks.math.columbia.edu/tag/02MB), Definition10.121.2, uses one-dimensional local-ring lengths. Adjacent valuation framework, not the weighted multi-index box criterion. Direct page read. [Receipt](../evidence/NAME/web-stacks.json). |
| MathOverflow | `site:mathoverflow.net Hasse derivatives multiplicity polynomial weighted` | Positive-characteristic multiplicity and Hasse-derivative discussions show why ordinary derivatives are unsuitable without characteristic conditions; no exact target located. [Receipt](../evidence/NAME/web-mathoverflow.json). |
| Recent arXiv | `site:arxiv.org Hasse derivatives weighted multiplicity polynomial after:2021-10-29 before:2026-10-30` | Returned [2201.06156](https://arxiv.org/abs/2201.06156) and [2610.00259](https://arxiv.org/abs/2610.00259) discuss Hasse derivatives/multiplicity, alongside irrelevant Hasse-principle material. Date window is explicit; no full-paper equivalence claimed. [Receipt](../evidence/NAME/web-arxiv.json). |

[Direct primary access](../evidence/NAME/web-primary.json) and [targeted §3.1 inspection](../evidence/NAME/web-primary-detail.json) separate successful page reads from failed PDF/XHTML access. Synthesis: weighted order as the least nonzero translated coefficient weight is standard; the box is a finite checking device justified by polynomial degrees. The literature supports arbitrary coefficient fields and weight systems. It does not settle whether this exact convenience theorem should be public independently of its parent representation. Historical “normalized derivatives” over characteristic0 translate to Hasse coefficient operators in arbitrary characteristic; this is a mathematical interpretation, not a claim that all ordinary derivative formulas are equivalent in positive characteristic.

## Phase 4a–4b — Every parameter and actual generalizations

| Parameter/hypothesis | Essential role and tested result |
|---|---|
| σ : Type u | Already arbitrary universe. Natural multi-index exponents belong to the polynomial object; changing to group exponents would change to Laurent objects. |
| Fintype σ | Both original weight and index kernel types contain this instance. It cannot simply be omitted while retaining those parents. `weightAny` uses existing finite-support Finsupp.weight and `indexAny` its finite support minimum; native `generic_cutoff` has no Fintype. |
| ℝ coefficients | Fixed by existing index interface. Verified arbitrary-variable `CommRing A` polynomial criterion uses translated coefficients and recovers original. Arbitrary `Zero A` suffices for the isolated finite-support observation theorem; that theorem does not itself construct or invert polynomial translation. |
| P | Polynomial finite support supplies finite observations. No claim about arbitrary infinite series with real weights attaining a minimum or being bounded below. |
| hP : P≠0 | Necessary for unchanged real index when c>0. Verified zero-polynomial observations all vanish, degree bounds hold, but index0=0<c. For c≤0 the conclusion follows without hP or derivative premises from index_nonneg. |
| r : σ→ℕ | Existing representation uses reciprocal natural parameters, including zeros. New observation theorem permits arbitrary weights into a conditionally complete linear order. No positivity was added to any old-form comparison. |
| hd | Cannot be dropped outright: verified X:Unit, α0,r0,c1 satisfies all in-box tests but has index0. Can be localized as below. |
| α | Arbitrary, no diagonal or algebraic-root condition needed. General coefficient-ring proof preserves arbitrary centers. |
| c : ℝ | Arbitrary. Strict-less-than testing is intentional: X at0,r1,c1 has all smaller-weight derivatives zero and the equality-weight derivative nonzero. |
| hvan | Needed on the relevant box. Equivalent bounded iff and unrestricted iff were both proved; unrestricted tests remove degree premises by demanding more observations, not by dropping hypotheses without replacement. |

The verified cutoff-local degree condition is

```lean
∀ d, weight r d < c → (¬ ∀ j, d j ≤ r j) → ∃ j, degreeOf j P < d j
```

Global hd implies it. It is strictly weaker: c0,X,r0 makes this local condition vacuous while the global degree bound fails. A nontrivial positive-cutoff witness also compiles: P=X² on Unit, α0,r1,c1 satisfies the localized condition and every in-box below-cutoff test, fails degree≤1, and obtains1≤index from the localized theorem. [Exact positive witness](../evidence/NAME/positive-executed.lean.txt), [clean native receipt](../evidence/NAME/positive-receipt.json). An even more semantic replacement is evaluated annihilation outside the box below c. This is a **new supplied hypothesis interface**, not an assertion that hd is unnecessary. The in-box hvan predicate remains unchanged.

[Project exact probes](../evidence/NAME/project-executed.lean.txt), [success](../evidence/NAME/project-receipt.json), [controls](../evidence/NAME/controls-executed.lean.txt), [success](../evidence/NAME/controls-receipt.json). The successful generalization uses only standard axioms and recovers the full original signature by native definitional type comparison. Existing parents have representation constraints, while the broader objects are genuinely defined and proved in scratch. No cost-based downgrade or hypothetical unverified weakening.

## Phase 4c — All nine modern-idiom checks

| # | Question | Assessment and consequence |
|---|---|---|
| 1 | Typeclasses/instances | Algebra/order classes already capture coefficients and weights. No new Index or Vanishing instance is justified. |
| 2 | Filters/nets | No convergence or topology. |
| 3 | Universal property | Translation can use existing aeval/eval₂Hom free-algebra substitution; no newly constructed object calls for a universal-property class. |
| 4 | Bundled substructures | Simultaneous vanishing is an intersection of linear-map kernels, potentially useful for the preceding pigeonhole/parameter-counting problem. This theorem's conclusion is a scalar bound, and its actual caller supplies pointwise zeros. No replacement by a new bundled object demonstrated. |
| 5 | Algebra hierarchy | Verified CommRing polynomial form; isolated observation form needs only Zero coefficients. CommSemiring with translation injectivity/nonzero translated support supplied is conceptually possible, but no stronger unconditional semiring claim is made. |
| 6 | Higher categories | No categorical data or useful higher-categorical downstream consequence. |
| 7 | Concrete index/order | Existing infDegree handles arbitrary semilattice-top weight targets; own finite-support sInf criterion handles conditionally complete linear orders. Infinite variable types are admissible after replacing the global finite sum with Finsupp.weight. |
| 8 | Concrete-via-abstract | Diagnostic fires: index and weight have zero literal proof-body occurrences after the le_index_iff step; the remaining content is observation vanishing, order contraposition, and degree-induced confinement. New generic observation proofs and exact original recovery compile. [Diagnostic](../evidence/NAME/concrete-diagnostic.json). This does not turn the normalization premises into existing mathlib lemmas. |
| 9 | False-generalization guard | Preserve index0=0, zero denominators, strict cutoff and the degree-box justification. Reject replacing Hasse by ordinary derivatives in arbitrary characteristic, positive-denominator-only comparisons, and arbitrary infinite-support real infima as finite attained minima. |

Modern organization: separate existing finite-meet order laws, derivative/Taylor support confinement, and the user's finite checking interface. This allows arbitrary test sets and finite observations and makes the zero projection explicit. It is not a reason to publish a duplicate generic finite-meet lemma. The large parent representation move is not a mechanical single-hypothesis weakening of the existing theorem; the local degree weakening itself is verified.

## Phase4.5 — Infrastructure risk

Theorem-kind n/a for all six rows: typeclass diamonds (no instance declared); reducibility leak (proof, no computational definition); noncanonical unfolding (no new definitional equality); instance priority (no priority or search rule); universe polymorphism (native type remains arbitrary-u, no new structure); coercion ambiguity (existing polynomial/Finset coercions only). The exploratory scratch definitions are not proposed infrastructure additions. Overall theorem risk n/a, not an untested blanket low rating for a new definition.

## Phase4.6 — All five proof-strategy checks

| Question | Outcome |
|---|---|
| Topology ε–δ versus filters | n/a: no topology. |
| Algebra elements versus substructure inclusions | Degree-box support containment is a useful intermediate predicate; pointwise equality is what the actual caller supplies. Kernel intersections add no demonstrated gain here. |
| Analysis sequences versus nets | n/a: no analysis limit argument. |
| Categories construction versus universal property | n/a: no categorical construction. |
| Missing helpers mathlib should have | The reusable Hasse/Taylor degree and coefficient-support laws are the substantive bridge. Generic finite infimum bounds already exist, so a fresh abstraction should reuse them rather than rebuild an order theory. |

Current small proof is mathematically idiomatic. For an infDegree migration, refactor to the shared support-confinement bridge and existing finite meet bound; native alternative recovery verifies this strategy. A public boxed criterion remains a discoverability/granularity choice, not an order-theoretic gap.

## Phase 5 — Full formal search and pinned positive checks

All15 cells (3forms×5methods) executed. [Matrix](../evidence/NAME/formal-search-matrix.json) links full raw requests/responses. Current form is bounded Hasse/real index; standard form is weighted vanishing/Taylor coefficients; abstract form is finite observation/sInf lower bounds. Supplemental [re-aim five-method matrix](../evidence/NAME/formal-search-reaim.json) searches infDegree/finite support directly.

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Finder | Univariate Hasse high-order-zero and unrelated Chevalley degree bounds | nat_le_weightedOrder, le_weightedOrder, coefficient vanishing | Finsupp weight inequalities and Hahn-series order; supplement finds infDegree |
| Loogle | MvPolynomial/hasse name-pattern result empty | weightedOrder inequality API | Initial unqualified sInf failed; corrected InfSet.sInf query returns generic infima; infDegree supplement finds Finset.le_inf_iff/le_inf |
| LeanSearch | Univariate Hasse, root multiplicity, homogeneous component zeros | Weighted-order lower bounds | le_csInf_iff, finite nonempty csInf membership; supplement finds infDegree |
| rg pinned source | No exact target/project APIs in mathlib | WeightedOrder and univariate Hasse building blocks | Conditional infimum and Hahn-series lower laws; supplemental finite-meet and infDegree source read |
| local name search | Target exists in project only | WeightedOrder source declarations | Conditional-infimum declarations; supplemental infDegree source declarations. Index is warming/error, so no absence claim from it. |

[Untruncated full-name search](../evidence/NAME/full-name-search.json) is evidence only for that lexical scope. External indices can differ from the pinned revision. The corrected Loogle retry and all original failed/error statuses remain archived.

Pinned positive checks are stronger than search hits: [isolated source](../evidence/NAME/isolated-executed.lean.txt)/[raw success](../evidence/NAME/isolated-receipt.json) checks full signatures of le_csInf, le_csInf_iff, le_of_not_gt, nat_le_weightedOrder, le_weightedOrder, coeff_eq_zero_of_lt_weightedOrder and the univariate high-degree Hasse zero theorem. Scalar exact? finds `Std.not_lt.mp`; this is a tool control, not a proof that the polynomial theorem is absent. Reconstructed multivariate translation uses genuine existing eval₂Hom/C/X operations; `#check_failure` confirms the project multivariate taylor/Hasse/target names are not imported. Natural-weight power-series lower bound compiles in one existing call, but it is a different representation from the current real index with reciprocal weights and zero denominators.

[Fresh re-aim isolated source](../evidence/NAME/reaim-executed.lean.txt)/[success](../evidence/NAME/reaim-receipt.json) verifies `AddMonoidAlgebra.infDegree` (`Degree.lean:624`) and `Finset.le_inf_iff` (generated dual at `Fold.lean:99`). The generic lower-bound equivalence is exactly the existing finite-meet law. A bounded-support check is a three-existing-call composition **provided** its support⊆test-set premise is supplied. The full [mathlib input snapshots/hashes](../evidence/NAME/mathlib-inputs.json) retain the pinned sources.

## Phase5.5 — Statement shape

Normal forms considered: (1) present in-box derivative vanishing implication; (2) unrestricted derivative vanishing iff; (3) support lower bound against infDegree; (4) lower bound against sInf of arbitrary finite observation weights. Existing Finset.le_inf_iff is canonical for the support-order core; its pointwise condition is on the RHS. No new quadratic web of equivalent order laws is warranted.

Syntactic attempts actually proved: bounded iff retaining hd; unrestricted iff replacing bounded tests and eliminating hd; cutoff-local degree premise; arbitrary test-set observation form; infDegree projection recovery. The existing caller naturally supplies hd and in-box zeros from J, so forcing it to supply all derivatives merely moves the degree-box proof outward.

Superfluous-argument audit: all original data and premises have roles listed in4a; no silently droppable Fintype or nonzero condition. `c≤0` is a separate simpler branch, not a valid deletion at arbitrary c. SHIP-AS-STATED for local convenience; RESTATE-BEFORE-SHIP for any generic upstream order contribution, using infDegree/explicit support bridges and preserving zero conventions.

## Phase6.0 — Every caller and inline scope

One actual invocation: private `exists_mem_RSet_le_index_aux`, MainLemma:550–567, at562. No external-to-file invocation. Its full proof chooses W′≠W″ by pigeonhole, proves their difference is a nonzero degree-box polynomial, maps it to real coefficients, obtains low-weight derivative zeros from diagonal remainder equality and applies this theorem. The continuation through power/log coefficient bounds, index-gap selection and main_lemma was compiled in full. [Caller inventory](../evidence/NAME/callers.json).

| Caller | Inlining/refactor outcome |
|---|---|
| MainLemma:562 | Full module replay removes the target declaration and replaces this application by direct le_index_iff plus the degree-excess contradiction. Exact original caller signature is checked using private-name construction; kernel body no longer contains target. Downstream main_lemma has standard axioms. [Source](../evidence/NAME/inline-executed.lean.txt), [success](../evidence/NAME/inline-receipt.json). |

[Inline audit](../evidence/NAME/inline-audit.json) and [fresh tracked lexical search](../evidence/NAME/tracked-source-search.json) distinguish related mechanisms from duplicates. `eq_sum_box_hasseDeriv` reconstructs P; `degreeOf_taylor_le` confines translated support; `le_index_iff` gives unrestricted lower bounds; `exists_hasseDeriv_eval_ne_zero` selects a witness from a strict upper bound. None is the identical bounded-check theorem independently rederived elsewhere.

| Pair | Same statement? | Same proof? | Action |
|---|---|---|---|
| target / le_index_iff | no; boxed versus unrestricted | shares order core | Reuse existing support lower law, retain degree restriction bridge. |
| target / eq_sum_box_hasseDeriv | no; bound versus reconstruction | same outside-box zero mechanism | Share Hasse degree annihilation, no duplicate theorem deletion justified. |
| target / degreeOf_taylor_le | no; index versus coordinate support | related degree confinement | Prefer shared support lemma during parent migration. |
| target / exists_hasseDeriv_eval_ne_zero | no; lower bound versus upper-bound witness | complementary minimum observation | Keep semantic roles distinct. |

The exact293 audit reports one direct kernel-value consumer, the same private caller, and zero direct type consumers. These are not claims about global simp closure or a complete transitive kernel graph. Target is not a simp theorem. Full-module replay establishes the specific downstream continuation, not every possible external user. [Scope audit](../evidence/NAME/scope-audit.json).

## Phase 6 — Composition and parent re-aim

1. **Scalar order**: le_of_not_gt supplies only contraposition. It cannot manufacture derivative zeros, the support box, or the semantic weighted minimum.
2. **Natural-weight power series**: nat_le_weightedOrder is an actual existing one-call criterion. Directly applying it to the old real-index theorem fails in a guarded native probe. Positive-denominator clearing changes the interface and does not cover all original zero-r cases without further work.
3. **Finite observations**: new `support_lower_iff`/`support_lower_of_checks` are genuinely proved mathlib-only generic lemmas, not preexisting replacements. The exact original is recovered using actual Taylor coefficients, nonzero translation, outside-box annihilation and finite-support weight bridge.
4. **Parent infDegree re-aim**: independently verified exact existing lower law `Finset.le_inf_iff`; the bounded-support core is `Finset.le_inf_iff.mpr (fun i hi ↦ le_of_not_gt (fun hw ↦ (Finsupp.mem_support_iff.mp hi) (hv i (hs i hi) hw)))`. This is a three-existing-call composition once hs is available. The fresh all-P/all-r real-projection bridge and exact original recovery compile: [re-aim project source](../evidence/NAME/reaim-project-executed.lean.txt), [success](../evidence/NAME/reaim-project-receipt.json). The indispensable hs normalization uses project `degreeOf_taylor_le`/`coeff_taylor`, or the original Hasse degree-excess proof; it is not supplied by the finite-meet law.
5. **Unfold-and-simp**: guarded `simp only [index]` does not close the original goal. Closing simp[defs] would be a Phase6b taste question, not automatic NO. [Guard/control receipt](../evidence/NAME/controls-receipt.json).

The explicit parent re-aim rule was examined, not bypassed: index's minimum representation and its unrestricted bound law are already in mathlib. This does not by itself identify an existing **degree-box Hasse checking law**. Treating the hs bridge as an axiom or assuming all out-of-box derivatives vanish without hd would lose content; the native X/r0 counterexample guards exactly that error. Existing support-order core COMPOSABLE; exact old statement NOT-COMPOSABLE from ≤3 existing mathlib calls established by this assessment. No search failure is called an absence proof, and new generic proofs are never counted as existing building blocks.

## Phase 7 — Actionable verdict

**BORDERLINE-needs-human.** This is useful local semantic API: it turns the finite derivative tests produced by pigeonhole into the index lower bound used by the main lemma. Existing finite-infimum order machinery already captures its abstract order component. The additional mathematical bridge is degree-induced derivative/Taylor support confinement; whether to expose this particular boxed convenience implication publicly, or to keep it local atop shared support API, is an upstream granularity choice.

The verified broader finite-support/general-ring formulation is real and recovers the exact original; it is not a promise of a mechanical single-line replacement of the current parent hierarchy. Nor does the short scalar contraposition justify NO. This classification uses mathematical organization and actual caller needs, not cost, elapsed time, or an inherited parent verdict.

Future upstream questions (assessment completion does not wait for answers):

QUESTIONS

Concrete local action: retain in `Roth/MainLemma.lean` while parent migration/design is considered. If minimizing wrappers locally, the full validated inline proof replaces the only call at562; do not pretend this eliminates the degree argument. If migrating to infDegree, introduce one shared point-translation/support bridge and apply the existing lower law; do not repeat the nondefinitional real projection proof at each site. A generic order-law PR duplicating Finset.le_inf_iff is not proposed. A future public Hasse boxed criterion would need a coherent Hasse/Taylor/index home and an explicit zero convention; no upstream PR, reviewer contact or production change is authorized by this read-only report.

## Phase 8 — Verification and completion

All required phases complete, including all named literature channels, full15formal cells plus five re-aim supplements, nine modern rows, five strategy rows, theorem n/a infrastructure six, three statement-shape checks, actual full caller inlining, fresh17, exact293 and portable current-manifest validation. [Verification](../evidence/NAME/verification.json) links eight accepted exact source/receipt pairs, all clean, nonpartial and standard-axiom-only. One rejected exploratory project attempt is separately labelled (unknown lemma spellings, boundary proof fixes and a metadata monad issue); its recovered sorryAx is never accepted evidence. Cold partial original receipt remains warming only. No raised limits, sorry, new axiom, unsafe or native_decide in accepted source. `unresolved=[]`; root acceptance pending.
'''.replace('FULLTYPE',type_).replace('NAME',N).replace('QUESTIONS','\n'.join(f'{i+1}. {q}'for i,q in enumerate(questions)))
put('report.md',report)
print('PASS report+assessment+overview generated',len(report.split()),'words')
