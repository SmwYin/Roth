# Roth.index_det_le — full assessment (209/293)

**BORDERLINE-needs-human.** This is a substantive arithmetic upper bound in Roth's determinant argument, but its public endpoint packages the project's extremal-index conventions and coefficient envelope. The generic coefficient estimate and factorization results deserve their separately accepted upstream work; they do not automatically justify a standalone upstream `lem6Φ` assembly theorem. All assessment and verification phases are complete. The questions below concern future upstream API design, not missing verification or a user blocker. Production is unchanged.

## Phase 0 — Baseline and scope

All 17 production-source/pin hashes freshly match the shared successful 2467-job build. The theorem resolves at `Roth/Theta.lean:457`; it has no sorry or nonstandard axiom. Entire Theta, Index, CoeffNorm and Separation modules and the complete sole actual caller were read. Theta develops the extremal index and Lemmas5–7; this theorem is the upper half of the determinant comparison in Lemma6. [Baseline](../evidence/Roth.index_det_le/baseline-build.txt), [fresh inputs](../evidence/Roth.index_det_le/inputs.json), [manifest](../evidence/Roth.index_det_le/input-manifest.json), [declaring module](../evidence/Roth.index_det_le/source-module.lean.txt), [metadata](../evidence/Roth.index_det_le/target-metadata.json).

## Phase 1 — Mathematical statement and proof

Let R be a nonzero integer polynomial with coordinate degrees bounded by positive r and coefficients of absolute value at most B. Form an l by l determinant F of the indicated mixed Hasse derivatives, with l positive. Suppose F factors as U in the complementary variables times V in the distinguished variable, both nonzero integer polynomials with degrees bounded by l times r. Then its real weighted index at a coordinatewise reduced rational point h/q is at most l times the sum of the two extremal indices at coefficient envelope M, using the scaled weights lr.

`abs_coeff_det_hasseDeriv_le` bounds every coefficient of F by `lem6M`, using the uniform ceiling r₁. The identity `coeff_rename_mul_aeval` identifies each coefficient of the separated product as exactly one product of factor coefficients. `Polynomial.leadingCoeff_ne_zero` and `Int.one_le_abs` give a coefficient of V of size at least1; `MvPolynomial.ne_zero_iff` and `Int.one_le_abs` do the same for U. Thus each factor inherits the coefficient bound. Finally `index_separated_mul_le_aux` represents V in Unit variables, uses `index_mul` and `index_rename`, applies `index_le_Θ` to both factors, and uses `index_mul_left_weights` to obtain lΦ. These are three mathematical stages, not three existing mathlib calls. [Exact source](../evidence/Roth.index_det_le/target-excerpt.lean.txt).

The exact complete elaborated type is retained in [native-type.json](../evidence/Roth.index_det_le/native-type.json) and printed in the original receipt. It has arbitrary universe τ and `[Fintype τ]`; no DecidableEq instance survives. Parameters are r, r₁, q, B, R, h, l, D, U, V, with hypotheses hr0, hr₁, hR, hh, hl, hU, hV, hUd, hVd and hF. The statement has no positivity hypothesis on q, B≥1, bound on D, or inequality l≤r none+1. These are supplied elsewhere when constructing witnesses, not hidden requirements here.

```lean
∀ {τ : Type u_2} [inst : Fintype τ] {r : Option τ → ℕ},
  (∀ (j : Option τ), 0 < r j) →
    ∀ {r₁ : ℕ},
      (∀ (j : Option τ), r j ≤ r₁) →
        ∀ {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ},
          R ∈ Roth.RSet B r →
            ∀ {h : Option τ → ℤ},
              (∀ (j : Option τ), IsCoprime (h j) ↑(q j)) →
                ∀ {l : ℕ},
                  1 ≤ l →
                    ∀ {D : Fin l → τ →₀ ℕ} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ},
                      U ≠ 0 →
                        V ≠ 0 →
                          (∀ (j : τ), degreeOf j U ≤ l * r (some j)) →
                            V.natDegree ≤ l * r none →
                              (Matrix.of fun μ ν ↦
                                      (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det =
                                  (rename some) U * (Polynomial.aeval (X none)) V →
                                Roth.index
                                    ((map (Int.castRingHom ℝ))
                                      (Matrix.of fun μ ν ↦
                                          (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det)
                                    (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                                  ↑l * Roth.lem6Φ q r (Roth.lem6M (Fintype.card τ + 1) r₁ B l) l
```

## Phase 2 — Preliminary checks

SMALL: a technical upper-bound helper rather than a listed main result or named theorem. The exhaustive literature protocol still applies. One-line definition-only check: n/a, theorem. Its proof is not definitional glue, so neither prefilter nor inherited verdict applies.

## Phase 3 — Exhaustive literature

Every named channel was actually checked, with three distinct general-web queries. Exact requests, returned-response SHA256/byte counts/status, locators and original short summaries are archived; full returned web bodies are not stored.

| Channel | Actual request and finding |
|---|---|
| Specific web | `Roth theorem index determinant separated polynomials coefficient bound l Phi`: Roth1958 ICM and Soundararajan–Petrow notes locate the classical argument. [Receipt](../evidence/Roth.index_det_le/web-specific.json). |
| General web | `polynomial disjoint variables product coefficient height index multiplicity weighted order`: weighted order and Hasse derivative definitions; weighted degree is a different extremum. [Receipt](../evidence/Roth.index_det_le/web-general.json). |
| Alias web | `Dyson lemma auxiliary polynomial Wronskian index height Roth`: Roth/Dyson index estimates; no exact standalone endpoint API. [Receipt](../evidence/Roth.index_det_le/web-aliases.json). |
| ChatGPT math | n/a: ask_chatgpt_math unavailable in the actual tool inventory. No reply invented. |
| Local references | clean.tex §5 Lemma6, equations15–17, exact coefficient bound, separated integral factor heights, index scaling and lΦ conclusion. [Excerpt](../evidence/Roth.index_det_le/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab Hasse derivative polynomial valuation`: Hasse-Schmidt derivative over a commutative rig; not an arithmetic height theorem. [Receipt](../evidence/Roth.index_det_le/nlab.json). |
| nCatLab | `site:ncatlab.org/ncatlab polynomial weighted order Hasse derivative`: no exact in-namespace hit; out-of-namespace results are not counted as one. [Receipt](../evidence/Roth.index_det_le/ncatlab.json). |
| Stacks | `site:stacks.math.columbia.edu polynomial order vanishing product`: tag02MB explains vanishing-order additivity via length, without this height envelope/supremum. [Receipt](../evidence/Roth.index_det_le/stacks.json). |
| MathOverflow | `site:mathoverflow.net Roth lemma polynomial index height Wronskian`: Dyson lemma question431381 asks about the role of height bounds; no replacement theorem. [Receipt](../evidence/Roth.index_det_le/mathoverflow.json). |
| Recent arXiv | `site:arxiv.org Roth polynomial index Hasse Wronskian after:2021-10-28 before:2026-10-29`: paper2607.26039 (July28, revised August17 2026) concerns iterated Wronskian degree growth, not this arithmetic estimate. The date window and topic mismatch are explicit. [Receipt](../evidence/Roth.index_det_le/arxiv.json). |

Primary follow-ups opened [Soundararajan–Petrow notes](https://math.stanford.edu/~ksound/TransNotes.pdf), [Stacks02MB](https://stacks.math.columbia.edu/tag/02MB) and [arXiv2607.26039](https://arxiv.org/abs/2607.26039). The ICM PDF fetch failed400 because its74MB content exceeded the tool limit; nLab direct fetch failed400 unsupported XHTML. Both honest access failures and successful requests are in [primary receipt](../evidence/Roth.index_det_le/primary.json). Search excerpts are not represented as successful direct retrievals.

Standard form: an integral separated product transfers coefficient height bounds to each factor because nonzero integer coefficients have absolute value at least1; weighted vanishing order splits across products and scaled weights. The explicit lΦ endpoint is a classical proof-stage packaging. Abstract valuation laws do not supply its arithmetic coefficient bound. This is a mathematical synthesis of the sources, not an assertion that every source states the exact Lean endpoint.

## Phase 4a–b — Every parameter and hypothesis

| Item | Checked scope and outcome |
|---|---|
| τ and `[Fintype τ]` | Arbitrary universe already. Current `index`, `Θ`, cardinality M and weights require a finite-variable interface. Finite-support and infinity-valued alternatives require representation bridges; no claim that Fintype is mathematically minimal. |
| `[DecidableEq τ]` | Already omitted in source and absent from native type; no removal to propose. |
| r and hr0 | Natural index weights, strictly positive in the existing multiplication/scaling interface. Retained in verified generalization; a zero-weight version would require another bridge, not evidence of impossibility. |
| r₁ and hr₁ | r₁ controls the input degree estimate. Verified replacement is directly `∀ j, degreeOf j R ≤ r₁`, decoupling input degree ceiling from index weights; the old hR and hr₁ supply it. |
| R, hR | ℤ is meaningful for the factor-height argument. Verified unbundling replaces RSet by input degree and coefficient bounds, removing its unused nonzero component. No domain/field-wide endpoint generalization is claimed. |
| B | Arbitrary real coefficient ceiling; B≥0 follows from the zero-exponent coefficient bound. No B≥1 premise is needed. The scalar target ℝ is fixed by extremal-index definitions. |
| q, h, hh | Rational point and coordinatewise coprimality witness membership in the extremal family. Positive q is not required by this existing statement. Removing coprimality while leaving the same family is not a mechanical weakening. |
| l, hl | Verified removal of hl: at l=0 the determinant is1, its index is0 and RHS is0; positive l uses the existing bridge. |
| D | Source rows have no order bound. Verified arbitrary E:Fin l→Fin l→multiindex replaces the special mixed-derivative pattern. Its determinant factorization is still an explicit premise. |
| U, V, hU, hV | Verified removal at the endpoint by zero-factor cases, using real `index 0=0` and nonnegative Φ. Nonzero factor coefficients remain essential inside the factor-height stage. |
| hUd, hVd | Kept in the decoupled generalization. Independently verified derivation from original hR degree bounds, hF, hU/hV using `degreeOf_rename_mul_aeval`, `degreeOf_none_rename_mul_aeval`, `degreeOf_det_hasseDeriv_le`; thus removable in the old coupled interface. These are different verified interfaces, not a claimed simultaneous removal of all data. |
| hF | Exact separated factorization connects determinant to the disjoint product. Retained. Merely existence of unrelated factors or overlapping variables does not give the coefficient identity. |

Generality verdict: strictly narrower than the verified expanded forms, while retaining fixed project index/height interfaces. The strongest decoupled checked theorem is `DetUpper209.arbitraryFactors`: positive r, degreeR≤r₁, coefficientR≤B, coprime point, arbitrary E and l, both factor-degree bounds, and hF imply the original-shaped upper estimate, without RSet, hr₁, hl, hU or hV. Its exact signature/proof and the independent old-interface degree elimination are in [final executed source](../evidence/Roth.index_det_le/final-executed.lean.txt), [final receipt](../evidence/Roth.index_det_le/final-receipt.json). The original is recovered by a compiled specialization; the complete sole caller also compiles using the generalized core.

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer and downstream consequence |
|---|---|---|
|1| Typeclasses instead of preambles | No new instance: coefficient/degree/factorization inequalities are pointwise data. A generic norm/lower-bound interface is better explicit than an artificial global class. |
|2| Filters/topology | No: finite algebra and support orders, no limit or metric argument. |
|3| Universal properties | No new object is constructed here. Existing polynomial equivalences are appropriate for the coordinate bridge. |
|4| Bundled substructure | The degree box can use restrictSupport, but bounded coefficient height and nonzero membership are not closed under addition. Turning the whole RSet into a submodule changes meaning. |
|5| Hierarchy weakening | Integer coefficient discreteness is used essentially in factor heights; raw ℚ extension is false. The isolated real-size abstraction retains explicit nonnegative sizes and witnesses of size≥1. It does not generalize the full Θ interface. |
|6| Higher categories | No categorical mathematical content or useful downstream categorical consequence. |
|7| Concrete indices | Arbitrary E and l=0 verified. Arbitrary finite matrix index requires cardinality transport; not claimed checked. Polynomial exponents remain ℕ. |
|8| Concrete-via-abstract | Fires at the three-stage boundary: after hFcoef the actual Hasse pattern is irrelevant; proof uses a separated product with coefficient bounds. The proof contains no use of hR.1. The checked arbitrary E, unbundled degree/coefficient and abstract size versions make this diagnostic concrete. |
|9| False-generalization guard | Pass for checked versions and original specialization. Reject naive ℚ factor-height extension:100·(1/100)=1 but100 has height>1, compiled. Reject overlapping variables (coefficients become convolutions). Endpoint zero-factor extension uses zero-default real index and would fail for conventional zero→∞ order without a separate case/convention. |

Modern improvement available: separate the coefficient determinant estimate, separated-product factor heights and extremal-index endpoint, with direct degree hypotheses and arbitrary derivative matrix. This enables reuse of the coefficient stage independently of Θ, and avoids forcing RSet nonzero data. It does not establish that the entire endpoint deserves an upstream name. [Isolated proof and guards](../evidence/Roth.index_det_le/isolated-executed.lean.txt), [raw receipt](../evidence/Roth.index_det_le/isolated-receipt.json).

## Phase 4.5 — Six infrastructure rows

Theorem n/a for new definitional infrastructure. Explicitly: typeclass diamonds n/a (no new instance); reducibility leaks n/a (proof of Prop); noncanonical unfolding n/a (no new definition); priority collisions n/a (no instance); universe-polymorphism construction risk n/a (arbitrary τ proposition); coercion ambiguity n/a (no coercion registered). Existing parent representation conventions are audited separately and are not silently redefined here.

## Phase 4.6 — Five proof-strategy rows

| # | Strategy diagnostic | Result |
|---|---|---|
|1| Topology/epsilon versus filters | n/a: finite algebra. |
|2| Element proofs versus ideals/submodules | Factor coefficient products are the correct element-level fact; ideal membership alone loses real size. Separate factor-height helper would shorten assembly. |
|3| Sequences versus nets | n/a: no convergence. |
|4| Construction versus universal property | n/a: no new universal object; use existing coordinate equivalence. |
|5| Missing reusable helpers | Candidate separated coefficient-height transfer, plus already accepted generalized determinant coefficient API; Θ assembly remains a separate scope choice. |

REFACTOR-RECOMMENDED: expose or locally isolate the independent coefficient-height stage, decouple input degree ceilings, and apply the existing index machinery last. No cost-based verdict is used.

## Phase 5 — Actual five-method search on three forms

All fifteen cells executed; four-method raw requests/results and exact rg commands/full outputs are retained. Additional five parent re-aim cells also executed. External search snapshots may differ from the pin. Local index statuses warming/error are explicitly not evidence of absence, and local results include the imported project theorem and fresh scratch namespace.

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
| Current determinant/index upper bound | Chevalley/ClassGroup numerical bounds: wrong statements | determinant coefficients of characteristic polynomials: wrong statements | univariate/Laurent Hasse derivative API: ingredients only | no current full-name pattern hit | imported Roth/scratch results and unrelated subgroup index |
| Literature separated factor height | Chevalley degree bounds: wrong statements | `Int.one_le_abs`: correct discrete-size ingredient | integrality of factor coefficients: integrality, not size | integer abs and coefficient/height fragments | coeff_mul convolution APIs |
| Abstract weighted order/size | weightedOrder_mul/prod | weightedOrder_mul | weightedOrder_mul/prod, order_mul | weightedOrder and coefficient APIs | weightedOrder family, warming |

The corresponding artifacts are `search-{current,standard,abstract}-{leanfinder,loogle,leansearch,rg,local_search}.json`; [current Finder](../evidence/Roth.index_det_le/search-current-leanfinder.json), [standard Loogle](../evidence/Roth.index_det_le/search-standard-loogle.json), [abstract LeanSearch](../evidence/Roth.index_det_le/search-abstract-leansearch.json), [complete abstract rg](../evidence/Roth.index_det_le/search-abstract-rg.json), [local status](../evidence/Roth.index_det_le/search-current-local_search.json). No result was accepted merely by its name. Correct positive candidates were checked with full pinned signatures and isolated proofs.

Parent re-aim gate: `Roth.index` was NO because `AddMonoidAlgebra.infDegree` is more general; Θ is sSup of the extremal family. Independently re-aiming this entire upper estimate finds `le_infDegree_mul`, a lower product-order inequality, and weightedOrder_mul, equality of product orders. Neither contains the integer coefficient envelope, separated factor bounds, admissibility or the two extremal suprema. Existing `le_csSup` handles membership once it is proved; it does not prove that arithmetic membership. Thus the analogous complete law is not a hit, and NO-mathlib-has-it is not inherited. [Re-aim Finder](../evidence/Roth.index_det_le/reaim-leanfinder.json), [Loogle](../evidence/Roth.index_det_le/reaim-loogle.json), [LeanSearch](../evidence/Roth.index_det_le/reaim-leansearch.json), [rg](../evidence/Roth.index_det_le/reaim-rg.json), [local error status](../evidence/Roth.index_det_le/reaim-local_search.json). Pinned #checks are in the final receipt. The earlier index representation bridge is a substantive normalization proof, not defeq or a new generic degree definition.

## Phase 5.5 — Three statement-shape checks

1. Normal form: source real index and expanded infDegree/weightedOrder are alternative representations. The generic support minimum exists, but replacing the endpoint entails the known zero projection and coordinate/scale bridges. No orthogonal pairwise equivalence theorem is proposed; inequalities retain the smaller side on the left.
2. Syntactic generality: arbitrary E, direct input degree/coeff bounds, l=0 and zero-factor cases were compiled. The exact original specialization and complete caller validate argument flow. This is an endpoint improvement independent of upstream audience selection.
3. Superfluous arguments: native type already omits DecidableEq; hR.1 and hl are unnecessary in expanded interface; hU/hV can be handled by cases; old factor-degree premises derive independently. All remaining parameters have explicit mathematical roles. No global minimality claim is made.

RESTATE-BEFORE-SHIP for any future upstream leaf; no production change made.

## Phase 6 — Complete callers, inline audit and composition

| Source caller | Occurrences | Validation |
|---|---|---|
| Roth.index_le_lem6, Theta.lean:556 (application578) |1| Whole original module replay under fresh target name; complete caller with generalized core; full local inlining of original target proof, all compiled. |

The exhaustive canonical source inventory, fresh `rg --no-ignore` and tracked-source `git grep` agree. No other explicit source caller or bypass re-derivation of the whole estimate was found. Private208 contains the separate product-index stage; the coefficient identity/height extraction is not a duplicate of determinant factor construction. [Callers](../evidence/Roth.index_det_le/callers.json), [fresh lexical search](../evidence/Roth.index_det_le/source-search.json), [tracked cross-check](../evidence/Roth.index_det_le/tracked-source-search.json), [inline audit](../evidence/Roth.index_det_le/inline-audit.json).

Canonical audit independently validates exact tracked293 order including private modules;293 unique names are present with values. The sole direct kernel-value consumer is `Roth.index_le_lem6`. This is direct expression reference evidence, not opaque transitive/simp closure. [Canonical snapshot](../evidence/Roth.index_det_le/canonical-snapshot.json), [direct consumers](../evidence/Roth.index_det_le/canonical-consumers.json), [original source/audit](../evidence/Roth.index_det_le/original-executed.lean.txt), [complete original receipt](../evidence/Roth.index_det_le/original-receipt.json).

No strict at-most-three-existing-mathlib-call term was verified. Existing `Int.one_le_abs`, coefficient convolution and weightedOrder_mul are genuine ingredients; they do not supply the full endpoint. `abs_coeff_det_hasseDeriv_le`, `coeff_rename_mul_aeval` and private208 are project results. The isolated factor-size/real-size proofs and generalized core are new evidence, never counted as existing mathlib. The attempted direct simp gate does not close the generic endpoint; that bounded failure is not a theorem of absence. A complete inline derivation succeeds, but it retains the arithmetic proof and project APIs. [Inline source](../evidence/Roth.index_det_le/inline-executed.lean.txt), [inline success](../evidence/Roth.index_det_le/inline-receipt.json).

## Phase 7 — Actionable verdict

BORDERLINE on upstream scope and abstraction, with a positive verified generalization and substantive proof. Keep the theorem in `Roth/Theta.lean`; it is used and not junk. The following future design questions do not block completion:

1. Should a general Diophantine extremal-index API expose this separated determinant upper-bound leaf, or keep its lΦ packaging local to the proof of Roth's lemma?
2. Should the reusable separated factor coefficient-height transfer be contributed independently, with explicit coefficient-size lower-bound witnesses, before considering the extremal endpoint?
3. For a future public endpoint, should the primary statement use the verified arbitrary derivative matrix/direct degree interface, with a separate zero-default convention wrapper?

Prior accepted YES declarations were read from current progress, not inferred from names: `Roth.abs_coeff_det_hasseDeriv_le` (100) has verified seminorm/arbitrary finite matrix extensions, and `Roth.exists_det_eq_mul` (178) has verified characteristic-zero normalized GCD-domain extensions. Their reports and full208 source were read before grouping. Those accepted ingredients are prerequisites, not existing mathlib replacements, and their broader coefficient claims do not transfer the nonzero-integer-size property. [Accepted grouping snapshot](../evidence/Roth.index_det_le/accepted-grouping.json). No YES PR or reviewer recommendation is asserted for this BORDERLINE leaf. No user answer is required to complete this read-only assessment.

## Phase 8 — Complete verification and handoff

Accepted exact sources/whole requests and raw complete receipts are linked in [verification.json](../evidence/Roth.index_det_le/verification.json). Disk receipts are success=true, partial=false, without warnings/errors or failed dependencies; raw isolated receipt uses its documented diagnostics format and no partial field. All accepted axiom lists are subsets of propext, Classical.choice and Quot.sound. The original #print kernel body contains the tool's explicit1687-character elision; this is disclosed, not a claimed complete kernel-body dump. Complete written proof, full native type and canonical value-reference audit are available.

Rejected missing-`open Roth` attempt (recovered sorryAx) and warning-only attempt are separately archived and excluded from accepted evidence. A width-guard preparation failure occurred before any source write/native execution; no stale source was executed. No resource limits were raised, and no new axiom/sorry/unsafe/native_decide was introduced.

[Assessment](../evidence/Roth.index_det_le/assessment.json), [overview entry](../evidence/Roth.index_det_le/overview-entry.json), [portable read-only validator](../evidence/Roth.index_det_le/validate.py), [current manifest](../evidence/Roth.index_det_le/copy-manifest.json). All required work is complete, unresolved=[], root acceptance pending. Root independently reviews, accepts and publishes the frozen candidate once.
