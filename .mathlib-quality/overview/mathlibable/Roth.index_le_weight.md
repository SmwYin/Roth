# Roth.index_le_weight — full mathlibable assessment

**NO-mathlib-has-it**, after re-aiming at the existing `AddMonoidAlgebra.infDegree` representation of the parent index. The analogous upper bound is existing `Finset.inf_le`, applicable definitionally to infDegree. The project spelling additionally needs its verified finite-minimum bridge, the zero-default projection and the Taylor coefficient identity. Those are identified explicitly; the old spelling is not claimed definitionally equal to infDegree.

## Phase 0 — Baseline and scope

Canonical declaration 135, theorem `Roth.index_le_weight`, `Roth/Index.lean:69`. The entire declaring module and all six caller fragments were read. [Exact Index source](../evidence/Roth.index_le_weight/Index-source.lean.txt), [Main source](../evidence/Roth.index_le_weight/Main-source.lean.txt). The baseline full build succeeded with 2467 jobs, exit 0, no reported warnings/errors. Its reuse is justified by a new [17-input hash check](../evidence/Roth.index_le_weight/inputs.json), all matching the shared manifest. [Build receipt](../evidence/Roth.index_le_weight/baseline-build.txt). Production sources, pins, Git and progress were not changed.

The fresh [original/canonical native receipt](../evidence/Roth.index_le_weight/index-le-weight-original-audit-receipt.json) is successful/nonpartial, with standard axioms only. The [exact original commands](../evidence/Roth.index_le_weight/index-le-weight-original-executed.lean.txt) print the complete short kernel body without printer elision. The [fresh audit](../evidence/Roth.index_le_weight/index-le-weight-audit-executed.lean.txt) checks all 293 canonical names in their exact tracked order, including private names: 293 unique, 293 present, 293 values. Target information is scoped from line 993; audit information from line 996. Historical info messages in the disk receipt are not substituted for these assertions.

## Phase 1 — Mathematical content and full type

For every multi-index d whose Hasse derivative of P does not vanish at α, the weighted index of P at α is at most the weight of d. This is the elementary fact that a minimum of a finite nonempty set is at most any of its members. The nonvanishing premise already ensures that d belongs to the Taylor support, so no separate P≠0 assumption is needed. No positive-weight assumption is present: the definition and inequality include zero denominators under Lean's division convention.

Full native elaborated statement:

```lean
Roth.index_le_weight.{u_1} {σ : Type u_1} [Fintype σ]
    {P : MvPolynomial σ ℝ} {α : σ → ℝ} {r : σ → ℕ} {d : σ →₀ ℕ}
    (h : (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0) :
    Roth.index P α r ≤ Roth.weight r d
```

σ indexes variables, Fintype supplies the current finite global sum in weight, P is the real polynomial, α its center, r the natural denominator parameters and d the selected exponent. The only propositional assumption is h. The proof applies `csInf_le`: the image of finite Taylor support is bounded below; h yields membership through the private support lemma and `coeff_taylor`. Direct project dependencies are index, weight, taylor, hasseDeriv, and the private membership equivalence. The coefficient identity is project API and is not counted as existing mathlib.

## Phase 2 — Preliminary checks

**SMALL**: a basic minimum/support bound, neither a new structure nor a named main theorem. The exhaustive search still runs. One-line-definition check: **n/a**, declaration kind is theorem; no definition exemption is needed. The original proof has two substantive expression lines.

## Phase 3 — Exhaustive literature

[Web metadata 0](../evidence/Roth.index_le_weight/web0-metadata.json), [metadata 1](../evidence/Roth.index_le_weight/web1-metadata.json), [metadata 2](../evidence/Roth.index_le_weight/web2-metadata.json), [primary opens](../evidence/Roth.index_le_weight/web3-metadata.json) preserve exact requests, response byte counts/SHA256 and locators, without article/search-result bodies. No credential-bearing query was found or retained.

| Channel | Exact query or action | Result and interpretation |
|---|---|---|
| General specific | Roth polynomial index minimum weighted nonzero partial derivative index inequality | Roth-index presentations describe the same minimum; primary local manuscript below supplies the exact formulation. |
| General standard | Hasse derivatives weighted order vanishing polynomial nonzero Taylor coefficient | Hasse derivatives as translation coefficients and order from the first nonzero coefficient. |
| General abstract | monoid algebra minimum support degree infimum coefficient valuation | Generic support inf-degree and valuation references; distinguishes a minimum from weighted total degree, which is a maximum. |
| ChatGPT math | Unavailable | n/a: ask_chatgpt_math is unavailable; no simulated consultation or inferred opinion. |
| Local references | rg index/minimum/attained in clean.tex | §4, lines 530–556: index is a finite support minimum with positive real denominator parameters, and zero polynomial has infinity. [Search receipt](../evidence/Roth.index_le_weight/local-literature-search.json), [exact excerpt](../evidence/Roth.index_le_weight/clean-excerpt.tex.txt). |
| nLab | site:ncatlab.org/nlab weighted valuation polynomial order vanishing | Valuation and Hasse–Schmidt derivative references. The direct Hasse–Schmidt page open failed with 400, unsupported application/xhtml+xml; search snippets are distinguished from full access. |
| nCatLab | site:ncatlab.org/ncatlab polynomial valuation order vanishing | An actual mathematical query targets the distinct namespace. Returned locators are /nlab pages/files; no in-namespace exact hit. This is a search limitation, not proof of absence. |
| Stacks | site:stacks.math.columbia.edu order vanishing polynomial derivatives multiplicity | Curve-order material; direct Tag 00PD checks the related local-ring valuation formulation, rather than supplying this weighted multivariate comparison. |
| MathOverflow | site:mathoverflow.net weighted order vanishing polynomial Hasse derivative | Related order-of-vanishing and Hasse-derivative discussions, including question 209846. They support terminology, not a pinned library replacement. |
| Recent arXiv | site:arxiv.org after:2021-10-27 Hasse derivative multiplicity polynomial weighted order | 2610.00259, submitted 24 September 2026, studies derivative/multiplicity loci in positive characteristic; adjacent, not the weighted support bound. The returned 2103.07239 is outside the five-year interval and is not counted as recent. |

The primary survey [Tao, *Algebraic combinatorial geometry*](https://ems.press/content/serial-article-files/36979?nt=1), §2, p. 10, treats Hasse–Taylor expansion and vanishing order over fields of arbitrary characteristic. This supports the coefficient-support formulation and explains why ordinary higher derivatives would be inadequate in positive characteristic. [Stacks Tag 00PD](https://stacks.math.columbia.edu/tag/00PD) concerns valuations on one-dimensional regular local rings, a different abstraction from this arbitrary finite weighted support minimum. [Recent arXiv abstract](https://arxiv.org/abs/2610.00259) concerns characteristic-sensitive derivative loci; it does not strengthen or replace the present elementary inequality.

Standard names are weighted order of vanishing, weighted index, and minimum support degree. The local source uses positive **real** r and infinity at zero; the project uses natural r and returns zero for the zero polynomial. For this upper bound h rules out the empty-support case. Finite-support coefficient comparison is the common core; positivity, a field and characteristic zero are not needed there. No alleged literature novelty is inferred from failed access or search results.

## Phase 4a–4b — Generality

| Parameter/hypothesis | Current form | Verified or necessary general form |
|---|---|---|
| σ/universe | arbitrary Type u with Fintype | arbitrary Type u without Fintype in expandedLaw; finite polynomial support suffices. |
| Coefficients | ℝ | CommSemiring R for translated MvPolynomial; Semiring R for the monoid-algebra law. |
| α | σ→ℝ | σ→R for translation; disappears entirely once the translated polynomial is supplied. |
| r | σ→ℕ | arbitrary degree map D on exponents, including arbitrary real weights and positive real reciprocal denominators. |
| Target order | ℝ with default-zero convention | any SemilatticeInf T with OrderTop T for the unprojected law; ℝ default projection checked separately. |
| P | unrestricted polynomial | arbitrary additive monoid-algebra element, no nonzero assumption added. |
| d and h | nonzero evaluated Hasse derivative | nonzero translated coefficient, equivalently membership in its support. h cannot simply be removed: X at center 0 with weight 1 and d=0 would demand 1≤0. |
| Positivity/additivity | none | none: no positivity, linearity, injectivity or additive law for D is used by the comparison. |

The unchanged project interface has no mechanically removable propositional assumption; Fintype and ℝ occur in its parent interfaces. The expanded representation is **STRICTLY NARROWER THAN STANDARD in the original**: the wider support law has actually compiled, not merely been proposed. [Exact isolated source](../evidence/Roth.index_le_weight/index-le-weight-mathlib-executed.lean.txt), [raw native success](../evidence/Roth.index_le_weight/index-le-weight-mathlib-receipt.json) prove abstractLaw, projectedLaw and expandedLaw. These are probes of existing general lemmas, not new missing API.

```lean
-- The abstract conclusion, for arbitrary D, T and monoid-algebra P:
AddMonoidAlgebra.infDegree D P ≤ D d
-- Existing library proof term when h : P.coeff d ≠ 0:
Finset.inf_le (Finsupp.mem_support_iff.mpr h)
```

The mathlib-only probe has no Roth imports, guards `#check_failure Roth.index_le_weight`, uses the same preflighted seven-module prefix as the earlier parent check, and has no obsolete forwarding import, new axiom, sorry, unsafe, native_decide or raised limit. Universe u/v/w independence is explicit. This generality lands on existing library machinery, so it is not a YES-generalise-first gap.

## Phase 4c — All nine modern-idiom checks

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | Existing Semiring/SemilatticeInf/OrderTop already express the general law. No new class is needed; the same Finset theorem specializes to all such targets. |
| 2 | Filters/topology | No: a finite support/order statement, no topology or convergence. |
| 3 | Universal property | No new object is constructed by the theorem. Translation is already aeval substitution. |
| 4 | Bundled substructure | No closure predicate is present. Finset support is the actual finite input to the existing inf operation. |
| 5 | Field to semiring/module | Yes: abstractLaw works over Semiring; translated expandedLaw over CommSemiring, so positive-characteristic rings are included without factorial division. |
| 6 | Higher categories | No categorical or higher-categorical data. |
| 7 | Concrete index/order | Yes: any degree map into a semilattice with top. This allows nonintegral, nonadditive and negative weights for this inequality, and preserves infinity before projection. |
| 8 | Concrete-via-abstract diagnostic | Fires: index appears zero times in the original proof body; only finite support, image membership and csInf_le remain. Taylor occurs as the support input once. The generic existing comparison is Finset.inf_le on infDegree. |
| 9 | False-generalization guard | The compiled finite bridge and original/expanded replacement prove preservation of all original cases. Reject ordinary derivatives in positive characteristic; reject changing formal polynomials to polynomial functions over finite fields; reject treating arbitrary-real-weight infinite power-series supports as finite attained minima. Reject extending the h-free inequality to arbitrary d. |

Modern idiom available: **yes, already in mathlib**. Using infDegree and its reducible Finset.inf representation makes the theorem a standard lattice bound. The improvement is concrete reuse of generic semilattice support bounds, without another order theory tied to Roth's reciprocal weights. No gratuitous valuation class is introduced: a general degree map need not give multiplicativity.

## Phase 4.5 — Definition infrastructure

All six rows are **n/a because this is a theorem**: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism infrastructure, and coercion infrastructure. It introduces a proof of Prop and no instance, coercion or data definition. The parent definition's risks are assessed separately; they are not silently inherited as this theorem's risks.

## Phase 4.6 — Proof strategy

| Question | Assessment |
|---|---|
| ε–δ versus filters | n/a: no topology. |
| Elements versus algebraic inclusions | A single support member is the natural input; Finset.inf_le already supplies the abstract comparison. |
| Sequences versus nets | n/a: no analytic limit. |
| Construction versus universal property | No construction in the comparison. Input translation uses the existing aeval universal substitution. |
| Missing helpers mathlib should have | No missing abstract upper-bound law. The bridge from finite sInf to projected infDegree is actual normalization glue; coefficient-Taylor is project API and must remain separately justified. |

Strategy: **REFACTOR-RECOMMENDED** if migrating the parent to infDegree; call the generic comparison and projection after normalizing the support premise. The original csInf_le proof is already idiomatic for its current real-sInf parent. Strategy choice is not based on proof cost or performance.

## Phase 5 — Five actual mathlib methods on three forms

[Complete formal requests/receipts](../evidence/Roth.index_le_weight/formal-search.json) contain 12 actual calls: Finder, Loogle, LeanSearch and local on each of current, standard weighted-order, and abstract support-degree forms. [Current rg](../evidence/Roth.index_le_weight/rg-current.json), [standard rg](../evidence/Roth.index_le_weight/rg-literature.json), [abstract rg](../evidence/Roth.index_le_weight/rg-abstract.json) supply the fifth method on pinned source.

| Method | Current point-index form | Standard weighted-order form | Abstract support-infimum form |
|---|---|---|---|
| Finder | Adjacent polynomial bounds, no exact point-index law | weightedOrder_le and related coefficient bounds | infDegree plus support-degree algebra laws |
| Loogle | Polynomial support bounds | weightedOrder_le family | **Finset.inf_le**, with exact semilattice/top signature |
| LeanSearch | weightedOrder_le, homogeneous-support material | weightedOrder_le | infDegree and degree/support candidates |
| rg | Six project applications, own csInf proof | Pinned weightedOrder_le | Reducible infDegree and generated inf_le/untopD_le source annotations |
| local | Project theorem and scratch replay | weightedOrder_le family | Name matches; index unavailable, so these are not exhaustive absence evidence |

All actual formal requests returned isError=false; remote snapshots can differ from the pin. Local index unavailable is explicitly a limitation. The pinned native check verifies the positive decisive declarations:

- `AddMonoidAlgebra.infDegree`: `Mathlib/Algebra/MonoidAlgebra/Degree.lean:624`, abbreviation `f.coeff.support.inf D`.
- `Finset.inf_le`: generated by `@[to_dual inf_le]` on `Finset.le_sup`, `Mathlib/Data/Finset/Lattice/Fold.lean:121`; the theorem checks and directly elaborates for infDegree.
- `WithTop.untopD_le`: generated by the corresponding dual of `le_unbotD`, `Mathlib/Order/WithBot.lean:653`; projects a bound by a finite value with arbitrary default.
- `Finsupp.mem_support_iff`: converts a nonzero coefficient to support membership. This ordinary coefficient premise, rather than project Hasse API, is enough for the fully abstract law.

Conclusion: **found in mathlib as Finset.inf_le; more general form on the existing infDegree representation**, independently verified. MvPowerSeries.weightedOrder_le is a useful standard analogue for natural additive weights, but a denominator-clearing bridge would impose unnecessary positivity and is not the deciding replacement. No negative search result is used as proof of absence.

## Phase 5.5 — Statement shape

Normal forms tested are (i) real sInf of the weighted Taylor support, (ii) infDegree of the translated polynomial into WithTop ℝ, then default-zero projection, and (iii) completely arbitrary semilattice support infimum. A power-series weightedOrder presentation is a complementary natural-weight form. The canonical generic order form is (iii), already supplied by Finset.inf_le. This is an inequality, so the equivalence-normal-form RHS convention is not directly applicable; parent normalization places infDegree on the RHS of an equality.

Syntactic generality attempts actually compile as abstractLaw, projectedLaw, expandedLaw, originalReplacement and expandedReplacement. The h form is convenient for all six existing callers; the coefficient form is natural for generic algebra consumers, and the membership form is directly Finset.inf_le. Superfluous-argument audit covers σ/Fintype, P, α, r, d, h in Phase 4: no h can be dropped, no P≠0 or positive-r assumption should be added. Fintype/ℝ can be removed only in the expanded representation, not by leaving fixed project parents unchanged. Normal form: REFACTOR toward existing infDegree if proposing upstream. Syntactic generality: RESTATE to the generic existing comparison. Fixed-interface superfluous hypotheses: NONE. Overall **RESTATE-BEFORE-SHIP** for a hypothetical upstream addition, which would then be redundant.

## Phase 6.0 — All callers and inline audit

[Caller inventory](../evidence/Roth.index_le_weight/callers.json) records complete source fragments, file hashes, exact reference lines and a plan per caller. Six distinct explicit callers/six applications: five in Index, one in Main. Internal count excluding declaring module **K=1**, in one external-to-file module. The fresh scoped kernel audit finds exactly the same six direct consumers. This source-level inventory is not an opaque/transitive kernel/simp dependency-closure claim. The theorem is not marked simp and is not dead code.

| Caller | Explicit reference | Concrete refactor continuation |
|---|---|---|
| Roth.le_index_iff | Index:87 | Use generic bound after bridge inside h.trans. |
| Roth.index_eq_zero_iff | Index:105 | Specialize d=0, retaining existing hasseDeriv_zero_apply simplification. |
| Roth.index_sub_weight_le_index_hasseDeriv | Index:114 | Apply bound to hi.2, retaining weight_add and sub_le_iff_le_add. |
| Roth.index_eq_weightedOrder_div | Index:153 | Convert hd to the Taylor/Hasse premise as before; use projected bound. |
| Roth.index_unique | Index:245 | Preserve chosen single exponent and key coefficient identity; use projected bound. |
| Roth.abs_eval_lt_of_le_index | Main:401 | Apply bound to h0 inside hidx.trans; retain subsequent product/rpow estimate. |

[Inline audit](../evidence/Roth.index_le_weight/rg-inline.json) finds the theorem's own csInf_le derivation and the later standard weightedOrder_le comparison in the parent/power-series bridge. The latter is not an independent bypass implementation of this same point-index upper bound. No additional equivalent inline point-index upper bound was identified. Useful multiple-consumer API is a local retention signal; it does not outweigh a verified more general existing law upstream.

## Phase 6 — Actual composition and bridge experiments

The [mathlib-only proof](../evidence/Roth.index_le_weight/index-le-weight-mathlib-executed.lean.txt) derives the abstract law with `Finset.inf_le (Finsupp.mem_support_iff.mpr h)`, and the real projected law with:

```lean
WithTop.untopD_le (Finset.inf_le (Finsupp.mem_support_iff.mpr h))
```

That is three existing mathlib declaration applications (support conversion, finite-infimum bound, finite upper-bound projection); the abstract membership-premise law is literally one Finset.inf_le call. infDegree is reducible to Finset.inf, so its analogous law requires no new algebra proof. The expandedLaw also directly instantiates this expression for an aeval-translated polynomial over any CommSemiring, arbitrary σ and arbitrary real degree map.

The [accepted parent mathlib-only bridge source](../evidence/Roth.index_le_weight/index-expanded-mathlib-executed.lean.txt), [complete raw success](../evidence/Roth.index_le_weight/index-expanded-mathlib-receipt.json), are preserved and independently inspected here. The finite bridge splits empty/nonempty support, uses Finset.coe_inf' and Finset.inf'_eq_csInf_image in the nonempty branch, and handles default-zero on empty support separately. Thus old sInf and projected infDegree are not defeq. Its denominatorIndex also expands weight to Finsupp.weight of reciprocal parameters and Taylor to aeval. These helpers are proved normalization glue, explicitly not preexisting library laws.

The [fresh actual-target source](../evidence/Roth.index_le_weight/index-le-weight-target-clean-executed.lean.txt), [native success](../evidence/Roth.index_le_weight/index-le-weight-target-clean-receipt.json), prove the original and fully expanded old-spelling results. They rewrite the independently proved parent bridge, apply WithTop.untopD_le and Finset.inf_le, explicitly change the support spelling and rewrite only membership/coeff_taylor. They never use Roth.index_le_weight or its downstream index lemmas to prove the replacement. Initial failure to reconcile coeff.support with polynomial support is [archived as rejected](../evidence/Roth.index_le_weight/index-le-weight-target-initial-receipt.json); it does not count as verification.

The [fresh whole-module/caller experiment](../evidence/Roth.index_le_weight/index-le-weight-callers-executed.lean.txt), [native success](../evidence/Roth.index_le_weight/index-le-weight-callers-receipt.json), replays the entire Index module with its bound proved by that composition, so all five Index consumers typecheck. It additionally replays Main's complete sixth caller with its private product estimate, replacing its application by the fresh bound. No original index_le_weight reference occurs in this accepted caller source. All six caller proofs and the replacement print standard axioms. This proves usable refactoring at the actual caller shapes, while leaving production unchanged.

Composition conclusion: **COMPOSABLE on the re-aimed infDegree representation**; the original spelling requires a genuine normalization/representation proof plus the project coeff_taylor identity. No false ≤3-call claim is made for the complete old-spelling proof. A closing simp [defs] would by itself invoke Phase 6b's BORDERLINE caution; that is not the decisive evidence here. Mode B explicitly directs NO-mathlib-has-it when the existing parent D′ already has its analogous law. The verified re-aim hit, rather than old spelling glue or cost, controls the verdict.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it** by the explicit parent re-aim rule, independently checked. Existing `Finset.inf_le` is the analogous support-degree upper-bound law for `AddMonoidAlgebra.infDegree`. The parent wrapper's accepted NO verdict suggested this route; it did not establish the law until the fresh mathlib-only probe above compiled. The one-line generic proof is exactly the displayed Finset.inf_le term, or the displayed three-call projected term when using real default-zero output. The fresh original/fully expanded bridges expose every extra normalization needed by Roth's spelling; no newly proved helper is advertised as existing mathlib.

If refactoring, implement the local parent via the projected infDegree expression, use the coefficient-support conversion at each of the six listed call sites, and delete index_le_weight after replacing those applications. With the current sInf parent kept intact, inline the accepted target replacement at each site, retaining a single documented local parent bridge; do not replicate six finite-minimum proofs. The row-by-row continuation plan above identifies the required specializations and arithmetic. The complete caller replay confirms this plan's type compatibility. Retaining the short theorem as a **project-local convenience API in Roth/Index.lean** is also reasonable for the manuscript vocabulary; it has six consumers. Neither this convenience spelling nor its zero convention identifies a missing upstream order law. Archive or an unrelated satellite is not an appropriate alternative destination.

No upstream PR is proposed for this theorem. Separately assessed Hasse/Taylor infrastructure is not rejected by this decision, and no claim is made that every later index law is already provided by infDegree. No cost-based downgrade, absence claim, blanket inherited verdict or automatic BORDERLINE from old notation is used.

## Phase 8 — Handoff

All required phases are complete; verification unresolved=[]; root acceptance is pending. [Assessment](../evidence/Roth.index_le_weight/assessment.json), [verification](../evidence/Roth.index_le_weight/verification.json), [overview entry](../evidence/Roth.index_le_weight/overview-entry.json), [current manifest](../evidence/Roth.index_le_weight/copy-manifest.json), [portable read-only validator](../evidence/Roth.index_le_weight/validate.py). The validator checks current artifact hashes/bytes, 17 fresh source/pin hashes, candidate/source hashes, exact canonical order and native counters, complete native success and standard axioms, six caller fragments/plans, formal and web channels, links, and the tracked evidence-secret guard. Scratch and integrated layouts are supported, with historical worker manifests never replacing the current manifest.
