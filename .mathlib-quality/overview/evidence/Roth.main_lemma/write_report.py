from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.main_lemma'
def rd(n):return json.loads((D/n).read_text())
def link(n):return '['+n+'](../evidence/'+N+'/'+n+')'
type_=rd('native-type.json')['type']
text='''# canonical266 — Roth.main_lemma

**Verdict: YES-add-as-is**, for the complete named quantitative Roth auxiliary-polynomial lemma. This is an independent assessment of its mathematical result, not a verdict inherited from its private helpers, its short orchestration body, or the usefulness of the eventual Roth theorem. The mathematical statement should be retained; a descriptive upstream name and ordinary proof/API cleanup precede submission.

## Phase0 — baseline and controls

The target resolves at `Roth/MainLemma.lean:735`, is a public theorem, and has no unproved placeholder. The entire762-line declaring module and588-line actual caller module were read, including all local construction helpers. All17 production source/pin hashes freshly match the shared baseline; the final hash check after native work/build matches too. The reusable baseline build was clean2467 jobs. The required actual file-end command `lake build` also completed successfully2467 jobs, exit0, in6275.167291ms; the complete42-byte actual log has SHA256 `b7f96a04d807f93a54c01314b6f59b969256b6222dffa7ae4b62832d3a174e65`.

Evidence: @INPUTS@, @FINALINPUTS@, @BUILD@, @BUILDLOG@. No production/pin/tracked overview/Git state was edited. Exclusive native ownership began on root dispatch and lasts through the explicit freeze/release record. The original disk nine imports remain byte-identical. Shared mathlib-only18 imports remain unchanged. Root explicitly authorized a declaration266-only19th import, `Mathlib.NumberTheory.SiegelsLemma`, for positive candidate verification; that exact19-import prefix is retained throughout isolated runs. @AUTH@ records the scope.

## Phase1 — full statement and mathematical construction

Let α be a real root of any monic integer polynomial f, with coefficient absolute values bounded by A. For nonzero dimension m, a small nonnegative δ, positive degrees decreasing sufficiently rapidly, and rational denominators satisfying the displayed square-log and degree/logarithm balancing inequalities, there exists a nonzero integer polynomial Q whose coordinate degrees are at most r. At the diagonal algebraic point its index is strictly greater than γ−η; it is nonzero at the prescribed coordinatewise reduced rational point; and every Hasse derivative at the diagonal point is smaller in absolute value than B₁^(1+3δ).

The complete native kernel type, obtained through `Lean.getConstInfo` and tagged printing with `pp.funBinderTypes`, is:

```lean
@TYPE@
```

Here λ=4(1+3δ)deg(f)√m, γ=(m−λ)/2, η=10^m δ^(2^−m), B₁=⌊q₀^(δr₀)⌋₊. Dimension `[NeZero m]` makes the first and last `Fin m` coordinates meaningful. Neither irrationality, irreducibility, minimal-polynomial status, nor deg(f)≥2 is assumed. The coefficient hypothesis implies A≥0 (in fact monicity supplies A≥1). Current weak numerical hypotheses imply δ>0 and all r_j>0, as the exact recovery proof verifies.

**Comparison with the source:** local `clean.tex` §6 Lemma `roth:lem9` assumes stronger original strict conditions and includes γ−η>0 in its conclusion. Current Lean deliberately weakens numerical hypotheses, proves strict index>γ−η, and does **not** itself assert γ−η>0. The final §7 application separately chooses parameters making the gap positive. Do not attach the source lemma's positive-gap assertion to the weaker Lean assumptions.

The full construction, not just the last theorem body, proceeds as follows.

1. The coefficient box consists of integer polynomials supported on the multidegree box, with coefficients in[0,B₁]. Its cardinality is(B₁+1)^∏(r_j+1). Filtered multi-indices of low weight have the lattice-count bound needed for a strict observation-count inequality.
2. Each observation is the low-degree coefficient tuple of the diagonal Hasse derivative reduced modulo monic f. Hasse differentiation has no coefficient collisions; diagonal substitution can merge coefficients and incurs the box-cardinality factor. Monic division bounds remainder coefficients by repeated leading-term elimination, each lowering the degree and multiplying the coefficient bound by at most1+A. Monicity also gives the degree/reconstruction fact making the finite tuple sufficient.
3. Pigeonhole gives two distinct coefficient arrays with identical selected remainders. Their difference is nonzero and has absolute coefficient bound **B₁**, not2B₁, because both arrays lie in[0,B₁]. Evaluation at a root of f kills the appropriate diagonal derivative remainders. Outside the degree box the derivative is identically zero. Thus this difference W has algebraic index≥γ.
4. Separate evaluation estimates control all iterated Hasse derivatives. The geometric sums at α are absorbed by(1+|α|)^Σr; no extra box-cardinality factor is inserted here. The three small-factor inequalities combine these bounds into B₁^(1+3δ).
5. The uniform project Θ theorem supplies a strict upper bound at the coprime rational tuple. The original proof chooses an intermediate cutoff between Θ and the available algebraic index gap, then selects a Hasse derivative of W below that cutoff. The derivative is nonzero at the rational point, remains within the degree bounds, loses at most its weight in algebraic index, and inherits the iterated derivative bound. This proves all five conjuncts simultaneously.

@ORIGINAL@ is a fresh complete written module replay in `Main266Original`, renaming only the target to `replay`. @ORIGINALRECEIPT@ is clean/nonpartial and all printed axioms are standard. Its `pp.all` kernel-body print explicitly contains `LEAN_MCP_MAX_OUTPUT_CHARS` elision: it is **not** a full kernel-body dump. Complete written source/body, full tagged kernel type, axioms, actual kernel-value presence and dependency audits are separate complete evidence.

## Phase2 — BIG and one-line check

BIG: this is the explicitly named Roth Lemma9, a main result listed in the module docstring and the construction theorem central to §7. Its size is the mathematics of the whole construction chain. The one-line definition test and its three exemptions are n/a: the declaration is a theorem. The short final orchestration does not qualify it as a definition wrapper or as a mathlib-call composition.

## Phase3 — exhaustive literature

All named channels were actually queried. Exact requests, returned-string UTF-8 SHA256/bytes, honest returned status, clean titles/URLs/locators and original concise summaries are archived; full search/article bodies are not stored. Batched requests record the actual full batch, so unsuccessful per-query targeting is not misrepresented as a distinct successful result.

| Channel | Actual query or source | Finding and limitation | Receipt |
|---|---|---|---|
| General specific | Roth main lemma auxiliary polynomial index Lemma9 bounded derivatives | Named auxiliary construction and height/index/nonvanishing exposition | @WEBGENERAL@ |
| General broader | Siegel lemma auxiliary polynomial prescribed vanishing nonvanishing rational point Roth theorem | Siegel-type construction is relevant but does not alone give prescribed-point nonvanishing | @WEBGENERAL@ |
| General aliases | Roth lemma9 index auxiliary polynomial construction Dyson lemma | Roth and Dyson approaches share purpose, not an identical numerical statement | @WEBGENERAL@ |
| Local reference | `.mathlib-quality/references/clean.tex`, §6 Lemma9 and proof, §7 application | Exact named statement and all construction/estimate stages read; input hash and excerpt retained | @LOCAL@ |
| nLab | `site:ncatlab.org/nlab Roth theorem auxiliary polynomial` | Returned operator-index/broad material, no exact quantitative result; not a proof of absence | @WEBCHANNELS@ |
| Distinct nCatLab | `site:ncatlab.org/ncatlab Roth auxiliary polynomial index`; quoted Roth/polynomial retry and Diophantine retry | Returned mostly/numerous out-of-namespace nLab pages; no exact /ncatlab hit claimed | @WEBCHANNELS@, @WEBRECENT@, @WEBMORE@ |
| Stacks | Siegel lemma polynomial vanishing; quoted Siegel/lemma retry; vanishing/polynomial/order retry | No exact Roth construction identified; algebraic vanishing alone does not supply its arithmetic/analytic estimates | @WEBCHANNELS@, @WEBRECENT@, @WEBMORE@ |
| MathOverflow | Roth auxiliary polynomial Siegel lemma prescribed order | Question491110 and answer point to number-field multivariable Siegel literature; this is a pointer, not a checked replacement proof | @WEBCHANNELS@ |
| Recent arXiv | Roth theorem auxiliary polynomial, plus quoted auxiliary-polynomial retry and standalone Roth theorem, all `after:2021-10-29 before:2026-10-30` | Recent p-adic/Ridout extension2603.10561; additive-combinatorial Roth homonyms explicitly excluded; no exact replacement theorem found | @WEBRECENT@, @WEBMORE@, @WEBPRIMARY@ |
| Optional mathematical second opinion | tool inventory checked | justified n/a: `ask_chatgpt_math` unavailable | @OPTIONAL@ |
| Primary supplementary | Roth1955 publisher page; Roth1958 ICM lecture search/open; author exposition by Maculan and Milojević | Publisher confirms original citation but full article HTML unavailable; ICM open failed400 oversized74705952 bytes, so only search snippet used. Local full proof is the exact source comparator | @WEBPRIMARY@, @WEBGENERAL@ |

Primary bibliographic record: [Roth1955](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F), Mathematika2,1–20. An author presentation explains the high algebraic vanishing/low rational-index strategy in its introduction: [Maculan](https://webusers.imj-prg.fr/~marco.maculan/files/papers/roth_book). [Milojević](https://aleksa-milojevic.github.io/expository/roth.pdf) gives an alternative auxiliary construction and rational index lemma with different numerical constants. [Davenport–Roth1955](https://www.cambridge.org/core/journals/mathematika/article/abs/rational-approximations-to-algebraic-numbers/0C0168456333A102C843522D7AADA535) notes on page162 that the original argument can also treat complex α; that is evidence for a broader mathematical direction, not a verified mechanical weakening of this real-index API.

The stable standard content is a controlled-height/high-index auxiliary polynomial combined with low index at rational approximants, followed by derivative selection. Numerical constants and whether the construction and nonvanishing step are packaged together vary by exposition. Number-field, complex and p-adic formulations exist in the literature but change analytic/index/height infrastructure. No single wider typeclass signature was verified here as a direct weakening of this complete numeric statement.

## Phase4a–4b — all parameters and generality

| Parameter/hypothesis | Role, comparison and actual weakening assessment |
|---|---|
| α:ℝ | Real evaluation, absolute value, log/rpow bounds. Complex/normed-field variants are mathematically meaningful, but require transporting the whole index/evaluation/height API; no unchecked field weakening is claimed. |
| f:ℤ[X] | Any monic equation, not necessarily minimal/irreducible. A rational root is allowed. Integers supply the coefficient lattice and discreteness. |
| hf:f.Monic | Required by low-degree remainder reconstruction and integral coefficient control in this construction. The evaluation-at-root helper alone not needing hf does not remove it from the full theorem. Unit-leading normalization would also require tracking the bound/degree and root equation. |
| hfα:aeval α f=0 | Turns equal diagonal remainders into derivative vanishing at α; cannot be discarded from that construction. |
| A and hA | Coefficient bound, supplies A≥0/≥1, controls monic elimination and logarithmic growth. No separate positivity assumption to drop. |
| m,[NeZero m] | Arbitrary nonzero dimension, includes m=1; required for chosen first/last coordinates. Removing the instance makes q0/Fin.rev0 ill-formed rather than a theorem weakening. |
| δ,hδ0 | Already0≤δ. The square-log bound forcesδ>0; an unused explicit positivity check does not establish a new weakening. Recovery derivesδ>0 directly. |
| hδm:δ≤1/m | Already weak boundary. Converts the square-log hypothesis to the weak threshold used by Θ; do not substitute the unused strict arithmetic lemma253. |
| r,hrlast≥3 | Together withδ≤1 and ratios yields antitonicity and all positive coordinates. The theorem does not admit zero-degree coordinates merely because some earlier structural index helpers do. |
| h31b consecutive ratios | Already non-strict; supplies degree separation for Θ and monotonicity forΣr≤mr₀. Arbitrary positive bounds without separation do not give the same quantitative Θ estimate. |
| q:Fin m→ℕ | Denominator arithmetic and logarithmic size, no extra positivity premise is assumed. Coprimality and Θ bound are used exactly in their existing interfaces. |
| h32 square-log bound | Already non-strict; gives the three analytic factor estimates, positiveδ and sufficient denominator size. Removing one term requires supplying the missing analytic estimate, not simply dropping it. |
| h33 balanced logs | Controls denominators at every coordinate for the uniform rational-index bound. Consecutive versus all-coordinate spelling is a possible equivalent interface, not a demonstrated weakening. |
| h:Fin m→ℤ,hh | Prescribed rational tuple and coordinatewise coprimality; used by index_le_Θ. No irrationality/irreducibility assumptions were inserted. |

The named full result is at the tested generality for this quantitative real formulation: no additional hypothesis deletion has been verified. This does not assert logical optimality of each numerical constant.

**Actual numerical-envelope experiment.** @PROJECT@ proves `Main266Project.numerical_envelope`, with independent positive integer B, analytic factor β, exponent c, outer coefficient budget X≥B, and strict index cutoff E. Its admissibility hypotheses are

```text
Σr≤s; 2^s<β; (1+A)^s≤β; (1+|α|)^s≤β;
Bβ³≤B^c; B≤X; Θ(X;q,r)<E.
```

It constructs a nonzero Q, coordinate degree≤r, index>((m−4c deg(f)√m)/2)−E, nonzero prescribed rational value, and all derivative evaluations<β(βB)β. It still performs the pigeonhole/high-index construction through the actual project helper; it does not assume existence of Q. The new proof uses private project construction, iterated derivative control and selection helpers, never `Roth.main_lemma`.

`old_recovery` then derives all these admissibility conditions from **every original hypothesis**, with B=B₁, β=B₁^δ, c=1+3δ, X=q₀^(δr₀), E=η. It derivesδ>0, antitonicity/positive degrees,Σr≤mr₀, the three analytic factors, floor positivity, B≤X and the exact power identity. The result has the complete original signature and all original conclusions; nothing has been weakened or dropped. The final `rfl` equality of theorem proofs checks type compatibility using proof irrelevance; it does **not** claim the proof constructions are identical. @PROJECTRECEIPT@ is clean with standard axioms.

These are **semantic**, not merely renamed arithmetic, parameters: β controls analytic growth, c controls construction counting/index, X determines the uniform arithmetic family, E controls derivative weight. The inequalities are necessary data for this interface. This experiment supplies a useful private budget layer; it does not replace the named lemma's substantive derivation ofΘ<η from concrete numerical inputs. Keeping the full end-to-end named theorem alongside that layer is justified. It is not a generalise-first claim based on an unverified drop or on development cost.

An arbitrary finite ordered variable type could be presented with an explicit order isomorphism toFin(card σ); first/last/consecutive conditions and the polynomial/index/Θ transports would need to be supplied. That changes representation rather than the arithmetic content. No full arbitrary-σ recovery was executed, so no such generalized theorem is claimed. The verified numerical experiment above is the positive exact-recovery evidence.

## Phase4c — modern idiom, all nine rows

| # | Diagnostic | Answer and concrete consequence |
|---|---|---|
|1| Typeclass rather than bundled hypotheses | No new class: monicity, root equation and quantitative inequalities depend on this input tuple. `[NeZero m]` already handles dimension. Packaging them as instances would hide numerical data from applications. |
|2| Filters/nets for sequences | n/a: finite polynomial construction, no limiting argument in this theorem. |
|3| Universal property instead of construction | No: prescribed quantitative integer witness is the content. A kernel/universal-property description by itself loses the coefficient/index/nonvanishing bounds. |
|4| Bundled substructure | The coefficient box is not a submodule: adding two members can leave[0,B]. A submodule kernel may organize vanishing conditions but cannot replace the bounded integer-box count. |
|5| Typeclass hierarchy | Semiring generalization fails the subtraction/sharp difference and integer lattice semantics; arbitrary ordered fields do not automatically supply the same log/floor/index infrastructure. Complex/number-field variants need a different height layer. |
|6| Higher categorical form | n/a: no categorical construction with a relevant higher analogue improving this arithmetic statement. |
|7| Abstract ordered variable index | Explicit enumeration/order equivalence can transportFin m; no infinite-index or arbitrary-degree generalization is inferred. It does not remove separation assumptions. |
|8| Concrete-via-abstract body diagnostic | Wrapper alone works with an index-gap witness, but the complete chain still uses box counts, monic remainder growth and quantitative Θ. New independent-budget layer is verified above. It is reusable for optimizing constants/cutoffs and separates construction from logarithmic admissibility; it is project proof, not mathlib replacement. |
|9| False-generalization guard | Reject arbitrary constants without inequalities, arbitrary coefficient rings, dropping monicity based only on evaluation, zero dimensions/degrees under unchanged first/last interfaces, or merely assuming an already constructed Q. Exact old recovery preserves all five conclusions and numerical premises. |

Modern organization: retain the full named end-to-end lemma, optionally organize the verified semantic budget result as a private constructor. It enables alternate bounds to reuse coefficient/derivative/index work without erasing the numerical Roth theorem. No newly verified single hypothesis/typeclass weakening forces a different public mathematical statement.

## Phase4.5 — six infrastructure rows

The theorem adds no definition/class/instance; this phase is justified n/a. Individually: typeclass diamond—n/a, no instance path; reducibility leak—n/a, proof constant inProp; noncanonical unfolding—n/a, no new data implementation; priority collision—n/a, no instance; universe issue—n/a, fixed arithmetic types/Fin indexing rather than new polymorphic data; coercion ambiguity—n/a, no Coe/CoeFun/CoeSort. Overall NONE for adding the theorem; dependency API import layering remains an ordinary prerequisite concern.

## Phase4.6 — proof strategy, all five rows

| # | Check | Finding |
|---|---|---|
|1| Topology ε–δ versus filters | n/a; no topological argument in this theorem. |
|2| Element versus submodule algebra | A matrix kernel could organize homogeneous constraints, and pinned Siegel supplies a small kernel vector. The exact bounded remainder map/pigeonhole count remains mathematically substantive; a kernel-only proof does not obtain the prescribed rational nonvanishing. |
|3| Sequence versus filter analysis | n/a; finite powers/logarithmic inequalities and finite evaluation sums. |
|4| Universal-property construction | n/a; witness existence with explicit quantitative controls cannot be replaced by an abstract universal property alone. |
|5| Missing supporting API | Hasse/index transport, coefficient norm under monic remainder, derivative coefficient/evaluation height, and the uniform arithmetic index theorem are the substantial reusable inputs. Stage them separately where their accepted assessments require generalization; keep specialized admissibility helpers private. |

Strategy verdict: **MATHLIB-IDIOMATIC** at the level of integer-box pigeonhole followed by derivative selection; **REFACTOR-RECOMMENDED** for organizing the already verified semantic budget layer and upstream prerequisite APIs. The mathematical result does not become redundant when this organization is improved. Cost is not part of the verdict.

## Phase5 — fifteen formal search cells and pinned candidates

@MATRIX@ records all3forms×5methods with exact raw receipts; these are current full statement, literature-standard auxiliary-polynomial/Siegel formulation, and abstract bounded-kernel/vanishing formulation. All Finder/Loogle/LeanSearch/source-rg/local-search attempts ran. The abstract Finder timeout is preserved; its successful retry found the actual Siegel theorem. Local search reported `index:error`, so empty local results are explicitly not evidence of absence. The source full-name search was untruncated. Index revisions may differ from the pin; native signatures and archived pinned files decide positive hits.

@SEARCHTABLE@

Pinned positive candidates:

* `Fintype.exists_ne_map_eq_of_card_lt` gives a collision in a map between finite types after supplying strict cardinalities. It neither defines the polynomial/remainder observations nor proves their sharp bounds/index conditions.
* `Int.Matrix.exists_ne_zero_int_vec_norm_le` (`Mathlib/NumberTheory/SiegelsLemma.lean:155`) gives a nonzero integer kernel vector with norm≤(N max(1,‖M‖))^(D/(N−D)), assumingD<N andD>0. The primed theorem177 additionally needsM≠0 and replacesmax by‖M‖. The **zero-row** case is not covered by thatD>0 signature and needs a separate witness, even though the full construction can handle an empty constraint family. The unprimed theorem can handle a zero matrix when the row type is positive. These hypotheses and constants are not interchangeable with the Roth observation-count formula.
* `Polynomial.sum_modByMonic_coeff` reconstructs the low-degree monic remainder from its coefficient tuple. `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero` evaluates a divisible polynomial at a known root. They support two steps, not the whole theorem.
* Nullstellensatz and Schwartz–Zippel hits choose a nonzero evaluation on a sufficiently large grid. They do not force nonvanishing at this **specified** rational tuple while preserving high algebraic index and derivative bounds. Number-field House/Siegel hits use a different height/kernel interface. Liouville and denominator-clearing hits bound values, not this auxiliary-polynomial existence statement.

@ISOLATED@ contains genuine19-import mathlib-only positive collision/kernel proofs and exact candidate checks, guarded by `#check_failure Roth.main_lemma` and `#check_failure MvPolynomial.taylor`. Its full comparison goal reconstructs translation using existing `MvPolynomial.aeval`, weighted support infimum using `sInf`, and derivative evaluations as coefficients of the translated polynomial. It does not call a project-only Taylor definition.

The theorem named `candidate_mismatch` is a **diagnostic witness pass-through**: it receives the goal as a `witness`, tests candidate terms, clears that witness inside a rolled-back `fail_if_success exact?` probe, and finally returns the witness. It is not an independent proof of the existence goal, not a theorem of mathematical absence, and not a formal noncomposability proof. It records observed candidate/tactic failure with unchanged standard limits. Noncomposability below rests on the full semantic gap and the actual searches/construction, not on treating that tautology as a new theorem.

@REPRESENTATION@ separately verifies the reconstructed translation/index and the **entire conclusion equivalence** through the genuine project `coeff_taylor` theorem. Translation and index bridges are definitional; the full derivative-conclusion bridge is a proved equivalence, not a claim that all original spelling is kernel-definitional. @REPRESENTATIONRECEIPT@ is clean. This bridge is project evidence and is never counted as an existing-mathlib proof.

## Phase5.5 — statement shape, all three checks

Normal form: the existential Q with all bounds is the usable named construction output. Equivalent presentations include translated coefficients rather than evaluated Hasse derivatives (verified), or a bundled quantitative witness record. There is no existing pinned canonical full Roth construction declaration to which it is an orthogonal equivalence. The index/derivative bridge should point toward the established Hasse/index API; no quadratic web of pairwise equivalences is proposed.

Syntactic generality: the caller immediately destructures Q, degree, index, nonvanishing and derivative controls. Its existing hypothesis order follows the paper's inputs and works unchanged. The independent numerical-envelope interface was actually proved and exactly specialized back; it can be an internal constructor. A new bundled record would add transport/projection API without reducing what this sole caller must supply. Use the full current existential statement for the named theorem, with a descriptive upstream name.

Superfluous-argument audit: every parameter and hypothesis is covered inPhase4a. No hidden irrationality, irreducibility, minimal-polynomial or deg≥2 hypothesis is needed. δ>0, A≥0 and positive degrees are derived, not extra arguments to remove. `[NeZero m]` supports actual first/last indexing. Monicity is used before root evaluation, and weakδm≤1 supports the boundary. No verified argument to drop. Overall **SHIP-AS-STATED** mathematically; ordinary naming/private-helper cleanup remains.

## Phase6.0 — complete callers and inlining

@CALLERS@ preserves the full canonical metadata/body for the one actual use. Fresh `rg --no-ignore` scoped to all production sources and independent tracked`git grep` agree. The declaring module has two docstring mentions plus the declaration; Main has one docstring mention and one executable use. Internal body-use count=1; external-to-declaring-file uses=1; distinct external caller files=1; source statement uses=0. The original canonical293 audit finds exactly one direct kernel value consumer, `_private.Roth.Main.0.Roth.one_lt_roth_eval_bound_aux`, and no direct type consumer. Generated/transitive dependency closure is a different scope; this theorem is not a simp rule.

| Actual caller | What it consumes |
|---|---|
| `Roth/Main.lean:466`, private `one_lt_roth_eval_bound_aux` (full body453–478) | Obtains Q; discards explicit Q≠0 because rational nonvanishing implies it; uses degree bounds for mapped-degree and denominator clearing, strict index via`.le` at477 for Taylor estimate, nonzero rational value for the integral lower bound, and uniform derivative bound for the upper bound. |

The final theorem then uses this estimate in`roth_of_isIntegral`; that is a transitive use, not another direct main_lemma caller. Full §7 bodies and paper application were read. Fresh inline-derivation enumeration found no independent rederivation of the whole construction elsewhere; the private helpers are proof stages, not bypasses of a trivial wrapper.

@INLINE@ replays the entire Main module under a fresh namespace and **physically replaces the actual call expression** with the target's full orchestration proof, using term elaborators only to reference actual pre-existing private construction/selection constants. It checks the actual private caller type against its original kernel type and the original`roth_of_isIntegral` signature. @INLINERECEIPT@ passes cleanly with standard axioms and verifies no direct target reference in the inlined caller value. Successful inlining proves local refactoring is possible; it does not convert the substantial project constructors into mathlib primitives.

@DEPS@ separates direct kernel body/type constants from the recorded traversal through private/generated project dependencies. Full source lexical occurrences, kernel direct consumers, simp status and transitive edges are not conflated.

Canonical body/type dependency fields map private kernel module/name pairs through the exact tracked293 declaration inventory to canonical names. Separately labeled `raw_kernel_body`/`raw_kernel_type` fields and the original constant-list messages preserve native spellings; raw receipts and executed sources are unchanged.

The unfiltered native body-constant message separately elides128 characters among tactic constants. Its ten tracked project-body dependencies are cross-checked using the nonelided target `MAIN266_PROJECT_BODY_EDGE` row for the nine Roth/private constants and the explicit `MvPolynomial.hasseDeriv` entry. Neither this message nor the `pp.all` print is described as a complete unfiltered constant/body dump.

## Phase6 — actual composition attempts

Attempt1: specialize the genuine Siegel small-kernel theorem. Positive pinned call compiles. Failure to obtain the full result is substantive: construct and bound the integer constraint matrix/remainder map; prove the low-weight constraint count; transport a kernel vector to polynomial degree/coefficient bounds; prove high algebraic index; obtain low index at the **specified** rational tuple; select a derivative; propagate all derivative/evaluation bounds. The matrix theorem does not contain those assertions or their exact numerical envelope. ItsD>0 restriction also needs an empty-row branch.

Attempt2: finite pigeonhole + monic remainder reconstruction + root evaluation. These three existing calls are real ingredients and compile independently. But before they can be applied one must define/count the box and observation codomain and prove the sharp remainder coefficient estimates and count inequality; after them one still needs Θ and index-loss/derivative estimates. Filling those with project results is not a composition **from existing mathlib**.

Attempt3: new numerical-envelope theorem plus supplied admissibility. Actual project proof and full exact old recovery pass; they use private project construction and selector and several analytic/numeric derivations. This is an additional proved layer, not an existing theorem and not a≤3-call old-statement replacement. The exact intermediate-cutoff proof also inlines successfully at the caller but retains that same substantive construction.

Conclusion: **NOT-COMPOSABLE** in≤3existing-mathlib calls. No closing`simpa` over only existing mathlib declarations produces the full statement, and no parent verdict is inherited. A local closing`simp` for the representation equivalence is only a bridge proof, not an existence proof; the Phase6b trivial-simp borderline rule is therefore not being used to mislabel this construction.

## Phase7 — actionable verdict and contribution plan

**YES-add-as-is**, preserving the complete named mathematical statement. The missing contribution is the quantitative Roth auxiliary-polynomial construction that simultaneously gives high algebraic weighted index, prescribed rational-point nonvanishing and uniform Hasse-derivative control. Existing finite pigeonhole/Siegel and polynomial remainder/root APIs are the right foundations, but they omit exactly this conjunction of arithmetic and analytic guarantees. The independent full source/caller replay, semantic budget experiment and isolated candidate audit support that conclusion; neither proof length nor cost decides it.

The full theorem should remain public as the stable classical endpoint. A lower-level budget constructor may remain private and support alternate numerical estimates without asking downstream users to proveΘ<η themselves. Current numeric assumptions are already weaker than the source and conclusions retain strict index; no additional mechanical hypothesis deletion was verified. Broader complex/number-field or enumeration-based interfaces are genuine mathematical projects, but do not erase the standard real lemma's content or justify an unsupported generalise-first verdict.

* Exact proposed home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean` (new module above the prerequisite index/height API).
* Descriptive public name: `Roth.exists_auxiliary_polynomial`, or the local namespace convention chosen for the new module; preserve the entire mathematical type. The generic name`main_lemma` is project-local nomenclature, not the proposed upstream theorem name.
* Proposed PR title: **feat(NumberTheory/DiophantineApproximation): Roth auxiliary polynomial lemma**.
* Grouping: @GROUPING@ is checked against the actual accepted progress snapshot. First stage accepted foundational Hasse results`MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_map`, `degreeOf_hasseDeriv_le`; stage the already accepted generalise-first index/height candidates`Roth.index_sub_weight_le_index_hasseDeriv`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.abs_eval_le` at their generalized homes. Then contribute the full named Roth lemma with its specialized construction/admissibility chain private. Do not list255–265 as public accepted YES declarations, and do not label the not-yet-assessed final Roth theorem as an accepted grouping candidate.
* Reviewer evidence: pinned relevant recent commit`f9314f86ef3bdc9c59ce1ab0e5c014f69a834429` (2026-08-27), Fabrizio Barroero, simplifies/golfs `NumberTheory/SiegelsLemma`; this is the most direct reviewer candidate for the construction. `a78f66ab84d18caad4f74f242218038874bfd5ad` (2026-09-04), Yaël Dillies, follows the ordered big-operator naming convention across the relevant files and is a secondary API reviewer candidate. These are activity evidence, not claims that anyone has agreed to review. @REVIEWERS@ records the actual read-only log request and output.
* Pre-PR checklist: `/generalise Roth.main_lemma` to recheck mechanically supported weakenings; `/cleanup Roth/MainLemma.lean Roth.main_lemma` for naming/proof/import cleanup; complete the prerequisite generalized APIs; preserve the named lemma's full quantitative content and explicitly document the weak-premise/strict-index distinction; choose reviewer from the actual relevant commit evidence. No PR, production edit, commit or message to a reviewer was made in this assessment.

Moral-duplication comparison:

| Pair | Same statement? | Same proof? | Action |
|---|---|---|---|
| main_lemma vs private high-index constructor | No: constructor has W and bound data before rational derivative selection | Construction is shared proof stage | Keep stage private and public named endpoint |
| main_lemma vs private derivative selector | No: selector assumes all polynomial/index estimates | Only last selection stage shared | Reuse selector; not a mathlib replacement |
| main_lemma vs new numerical_envelope | Related with exact specialization; envelope assumes semantic bounds that old theorem derives | New project assembly + substantial old recovery | Optional private API layer, retain full named theorem |
| main_lemma vs pinned Siegel theorem | No: bounded matrix kernel vector lacks polynomial/index/prescribed-point controls | Both use pigeonhole in construction | Use genuine generic building block where suitable; full Roth feature remains |

Junk decision: keep the named full theorem. Inlining at one caller is possible but does not remove its mathematical content or establish an existing-mathlib replacement. No public verdict was inherited from the short wrapper or any private helper.

## Phase8 — verification, limitations and handoff

@VERIFICATION@ lists exact accepted sources, full raw requests/results, original execution paths, hashes, timings and required native regions. The accepted sources are full original module replay; semantic numerical envelope with exact original recovery; complete actual caller inlining; genuine19-import isolated candidates and observed mismatch/generic-route diagnostic; and the exact reconstructed-statement representation bridge. All pass without warning/error, timeout, partial result, new axiom, unsafe/native_decide, resource raise or recovered sorryAx. Only`propext`, `Classical.choice`, `Quot.sound` occur.

Rejected source/receipt pairs are explicitly separate: one projectFin successor inference error with recovered sorryAx; one project unused-simp warning; one caller inlining missing-expected-type failure with recovered sorryAx; one isolated unknown coefficient identifier/missing theorem signature failure with recovered sorryAx; one isolated proposition-valued-def warning. None is accepted proof evidence. The original warming receipt is partial and also not accepted. Two failed width-preparation checks were corrected before any query of the new project source; no stale-source query followed preparation failure. Fresh accepted sources were inspected and width-checked before execution. @PREP@ records those controls.

@CANONICAL@ confirms exact293 order and unique names (including private modules), all293 present with values, and exact direct consumers. The portable validator checks current copy-manifest hashes/bytes, source/pin hashes, native regions/diagnostics/axioms, exact293 source/runtime audits, all15formal cells, web metadata/URLs, imports/authorizations, full caller verification, actual full-build log, report links and required overview fields in scratch and simulated integrated layouts. Historical worker manifest never replaces current manifest validation. The targeted shared secret guard must pass before freeze; @FINALVALIDATION@ records the actual final checks. Root acceptance remains pending until independent review. This assessment has no unresolved work item or user blocker; upstream preparation actions above are the completed assessment's recommendations.
'''
replace={'TYPE':type_,'INPUTS':link('inputs.json'),'FINALINPUTS':link('fresh-final-inputs.json'),'BUILD':link('file-end-build.json'),'BUILDLOG':link('file-end-build.log'),'AUTH':link('root-prefix-scope-authorization.json'),'ORIGINAL':link('original-executed.lean.txt'),'ORIGINALRECEIPT':link('original-receipt.json'),'WEBGENERAL':link('web-general.json'),'LOCAL':link('local-excerpt.tex.txt'),'WEBCHANNELS':link('web-channels.json'),'WEBRECENT':link('web-recent.json'),'WEBMORE':link('web-more.json'),'WEBPRIMARY':link('web-primary.json'),'OPTIONAL':link('optional-math-opinion.json'),'PROJECT':link('project-executed.lean.txt'),'PROJECTRECEIPT':link('project-receipt.json'),'MATRIX':link('formal-search-matrix.json'),'ISOLATED':link('isolated-executed.lean.txt'),'REPRESENTATION':link('representation-executed.lean.txt'),'REPRESENTATIONRECEIPT':link('representation-receipt.json'),'CALLERS':link('callers.json'),'INLINE':link('inline-executed.lean.txt'),'INLINERECEIPT':link('inline-receipt.json'),'DEPS':link('dependencies.json'),'GROUPING':link('accepted-grouping.json'),'REVIEWERS':link('reviewer-commits.json'),'VERIFICATION':link('verification.json'),'PREP':link('preparation-checks.json'),'CANONICAL':link('canonical-consumers.json'),'FINALVALIDATION':link('final-validation.json')}
table='| Form | Method | Actual evidence | Result |\n|---|---|---|---|\n'+'\n'.join('| '+r['form']+' | '+r['method']+' | '+link(r['receipt'])+' | '+r['summary']+' |'for r in rd('formal-search-matrix.json'))+'\n\nAbstract Finder retry: '+link('search-abstract-leanfinder-retry.json')+'.'
replace['SEARCHTABLE']=table
for k,v in replace.items():text=text.replace('@'+k+'@',v)
assert not __import__('re').search('@[A-Z]+@',text)
(D/'report.md').write_text(text)
print('Wrote',len(text.splitlines()),'report lines')
