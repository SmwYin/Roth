# Roth.index_sub_weight_le_index_hasseDeriv — full assessment

**Verdict: YES-but-generalise-first (MODERN-IDIOM).** Contribute the derivative estimate against existing `AddMonoidAlgebra.infDegree`, with arbitrary variable type, commutative-ring coefficients and a shift-compatible real degree map. The independently verified new theorem needs no production parent migration. The parent's NO verdict does not settle this law: existing minimum sum/product laws do not supply the derivative's exponent-shift premise.

## Phase 0 — Doctor

Canonical140 is the public theorem at Roth/Index.lean:109. The entire [declaring module](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/Index.lean.txt), Hasse/Taylor parent interfaces and both complete caller declarations were read. [Source links](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/source-links.json) preserve exact copies. The [successful baseline](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/baseline-build.txt) is reusable because a fresh [17-input check](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/inputs.json) matches every production source/pin in the shared manifest. No production edit or additional worker build is claimed.

## Phase 1 — Statement and proof

Full native type:

```lean
Roth.index_sub_weight_le_index_hasseDeriv.{u_1} {σ : Type u_1} [Fintype σ]
    {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ}
    (hk : (MvPolynomial.hasseDeriv k) P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) :
    Roth.index P α r - Roth.weight r k ≤
      Roth.index ((MvPolynomial.hasseDeriv k) P) α r
```

Differentiating by a multi-index k decreases weighted vanishing order by at most its weight. Choose a derivative i attaining the minimum for Δ_kP. The composition formula expresses Δ_iΔ_kP as a scalar times Δ_(i+k)P. Nonzero evaluation of that product forces nonzero evaluation of its second factor. Therefore index(P)≤weight(i+k)=index(Δ_kP)+weight(k). Rearranging gives the conclusion. Cancellation of the binomial scalar, characteristic zero and division of coefficients are unnecessary; the proof only needs the implication from a nonzero product to a nonzero factor.

σ indexes variables; P and α specify the polynomial and center; k specifies differentiation; r supplies natural denominators. No positivity of r is assumed. The hypothesis hk guarantees a nonempty translated derivative support. `Fintype σ` and ℝ are fixed-parent interface constraints, not the floor of the mathematical estimate. All three project parents index, weight and multivariate Hasse derivative remain distinct from existing mathlib facts. Direct project references in the statement/body are index, weight, hasseDeriv, exists_weight_eq_index, weight_add, index_le_weight and hasseDeriv_hasseDeriv; the printed elaborated composition factor also contains hasseCoeff.

[Fresh original source](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-original-executed.lean.txt), [canonical audit](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-audit-executed.lean.txt), and [complete receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-original-audit-receipt.json) show the full body without printer elision and only propext/Classical.choice/Quot.sound. Audit: 293 requested, unique, present and value-bearing declarations; exactly two direct kernel-value consumers. Required assertions are scoped to the fresh native region577; historical disk info is not new evidence.

## Phase 2 — Preliminary checks

SMALL: a standard four-line mathematical estimate, foundational for determinant and auxiliary-polynomial arguments rather than Roth's main theorem. Both actual uses establish substantive downstream index bounds. Definition-only one-line/exemption checks are n/a: this declaration is a theorem, and its proof uses attainment, Hasse composition, support comparison, weight additivity and ordered-group rearrangement.

## Phase 3 — Exhaustive literature

Exact requests, response hashes/byte counts/status and concise locator summaries are retained in [web A](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/web-a-metadata.json), [B](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/web-b-metadata.json), [C](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/web-c-metadata.json) and [D](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/web-d-metadata.json). Search bodies are not archived. [Local search](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/local-literature-search.json), [source excerpt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/clean-excerpt.tex.txt) and [synthesis](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/literature-summary.json) complete the protocol.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General web: exact form | Roth theorem polynomial index derivative index minus weight Hasse derivative | Milojevic, Claim3.1, p4 gives this inequality and Taylor-support proof. |
| General web: broad form | Hasse derivatives weighted order vanishing arbitrary characteristic inequality | Coefficient/Taylor formulation works in arbitrary characteristic; finite-field multiplicity sources support the broader algebraic setting. |
| General web: alternative language | monomial valuation derivative weighted order differential operator decrease | Monomial valuations and filtered operators are adjacent; arbitrary valuation derivative bounds need their own compatibility hypotheses. |
| ChatGPT math | unavailable | n/a: ask_chatgpt_math unavailable; no second-opinion response invented. |
| Local clean.tex | index-of-derivative, lines574–591 | Exact statement/proof, positive real denominators and nonzero derivative. Manuscript sets index0=∞; project sets it0. |
| nLab | explicit site:ncatlab.org/nlab Hasse Schmidt derivative weighted order vanishing | Hasse-Schmidt derivative page defines operators over commutative rigs and explains positive characteristic. Direct open failed400 unsupported XHTML; returned search content was accessible. |
| nCatLab | explicit site:ncatlab.org/ncatlab Hasse derivative order vanishing polynomial | Returned nLab material is outside the requested namespace; no exact in-namespace hit, not proof of absence. |
| Stacks | divided power differential operators order vanishing; tag09CH §10.133 | Differential operators over ring maps/modules; related organizational generality, no exact reciprocal-weighted estimate claimed. |
| MathOverflow | Hasse derivatives multiplicity weighted vanishing order; question71423 | Positive-characteristic replacement for derivations, with Hasse/jet references. Not the exact weighted estimate. |
| arXiv recent | Hasse derivatives with multiplicity and2023/2024 queries | 2402.18717, Feb2024, uses Hasse-Schmidt derivatives over arbitrary characteristic; adjacent, not the exact theorem.2103.07239 predates2021-10-27 and is excluded from the five-year evidence. |

The exact classical bound appears in [Milojevic's exposition, Claim3.1](https://aleksa-milojevic.github.io/expository/roth.pdf). [Roth's ICM1958 contribution, p206](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf) supplies the historical weighted derivative-minimum viewpoint. Hasse operators avoid factorial division in positive characteristic, as discussed in [nLab](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative), [MO71423](https://mathoverflow.net/questions/71423/replacement-for-derivations-in-characteristic-p) and the recent [Casas-Alvero paper](https://arxiv.org/abs/2402.18717). [Stacks09CH](https://stacks.math.columbia.edu/tag/09CH) is a broader differential-operator reference, not an asserted replacement proof.

Standard form: a weighted support minimum drops by at most the degree shift of a Hasse derivative; a point is introduced by translation. The numerator/operator order is integral, but additive real weights need not be rational, positive or reciprocals. Infinite-support power-series extensions would require separate boundedness/attainment or complete-order arguments.

## Phase 4a–4b — Generality

| Parameter / hypothesis | Current role | Checked generality / limit |
|---|---|---|
| σ and Fintype | Global sum defining Roth.weight and parent index | Generic support theorem and point theorem use arbitrary σ, since polynomial supports are finite. This is an expanded representation, not a successful deletion of Fintype from the fixed parent's type. |
| ℝ coefficients | Current index parent | supportShift compiles over CommSemiring; pointShift over CommRing, including positive characteristic and zero divisors. No NoZeroDivisors, field, linear order on coefficients or CharZero needed. |
| ℝ target | Finite minimum and subtraction | Verified target remains ℝ; proposed ordered-group/WithTop widening is an upstream design target, not claimed compiled here. |
| hk | Nonempty derivative support | Essential for the projected default-zero original. Compiled Bool counterexample below. Nonzero P alone is insufficient. |
| α | Point of vanishing | Arbitrary point remains genuine input; translation converts to origin support. CommRing supplies the existing taylor_eq_zero_iff used by pointShift. A CommSemiring point theorem would need an independently established nonzero-translation premise/law. |
| r : σ→ℕ | Reciprocal weights, zeros permitted | Replacement checks all r; no positivity added. Generic D replaces reciprocal denominators when D(i+k)=D(i)+D(k). Positive real denominators are a specialization. |
| k : σ→₀ℕ | Hasse multi-order | Arbitrary finite support; no nonzero k or degree bound needed. k=0 is harmless. |
| Additivity / shift law | Roth.weight_add | Essential compatibility. An arbitrary function D has no derivative estimate. For D(n)=n² and P=X², first derivative2X, the alleged bound4−1≤1 fails. Signed additive weights are compatible; nonnegativity is not used in the finite-support proof. |

Verified expanded signature (new theorem, not a preexisting mathlib hit):

```lean
{σ R : Type*} → [CommRing R] →
(D : (σ →₀ ℕ) → ℝ) → (P : MvPolynomial σ R) → (α : σ → R) →
(k : σ →₀ ℕ) → hasseDeriv k P ≠ 0 →
(∀ i, D (i+k) = D i + D k) →
minimum D (taylor α P) - D k ≤ minimum D (taylor α (hasseDeriv k P))
```

The [accepted target source](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-target-clean-executed.lean.txt) and [receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-target-clean-receipt.json) prove this and recover the exact original type through replacement. The commutative-semiring point draft was corrected before execution after reading Taylor's CommRing injectivity section; it is preparation-only. The accepted support theorem is independently CommSemiring.

Verdict: **STRICTLY NARROWER THAN STANDARD in expanded representation; no mechanical fixed-parent weakening claimed.** The standalone re-aimed theorem already compiles over CommRing coefficients, arbitrary σ and compatible D; it does not require modifying the index definition or its consumers. This supports MODERN-IDIOM generalise-first rather than an unverified claim of deleting Fintype or changing the coefficient of the existing parent in place.

## Phase 4c — All nine modern-idiom questions

| # | Diagnostic | Answer and concrete consequence |
|---|---|---|
| 1 | Preambles to typeclasses | Coefficient assumptions belong in CommRing/CommSemiring; hD can remain a fixed-k compatibility premise or be supplied by an AddHom. No new instance is needed. |
| 2 | Metric / filters | No topology or convergence in this finite-support algebraic proof. |
| 3 | Universal property | Translation already uses aeval; no additional universal-property bundle improves the degree estimate. |
| 4 | Bundled substructure | A weighted coefficient-vanishing filtration is possible, but submodule closure would require laws beyond this single estimate; no filtration equivalence claimed. |
| 5 | Field to (semi)ring | Yes: nonzero product implies nonzero second factor without a domain. Verified pointShift CommRing and supportShift CommSemiring enable finite-characteristic and zero-divisor coefficients. |
| 6 | Higher categories | No categorical data or higher coherence problem. |
| 7 | Concrete numerical index | Yes: arbitrary finite-support additive degree D removes reciprocal-natural restrictions. An infinity-preserving infDegree target would also express zero derivatives without projecting∞to0. Only the projected real form is checked here. |
| 8 | Concrete-via-abstract | Fires. After selecting the attaining index, the body uses only a support shift, an additive weight and an ordered additive inequality; it never uses any analytic property of ℝ coefficients. The checked generic supportShift isolates exactly those premises. |
| 9 | False-generalization guard | Reject arbitrary D without shift compatibility; reject dropping hk after projecting∞to0; reject silently using positive-integral denominator clearing with mixed zeros; reject calling CommSemiring point-translation injectivity an existing theorem. Polynomial finite support and Hasse coefficient semantics are preserved. |

Modern-idiom verdict: **RESTATE-BEFORE-SHIP**, toward existing infDegree and a new compatible support-shift/Hasse law. This independently re-aims the lemma at the parent's more-general representation. It does not inherit NO from the definition's verdict or from sum/product laws.

## Phase 4.5 — Infrastructure risks

All six rows are n/a for a theorem: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe-construction issues and coercion-instance ambiguity. The theorem creates no data definition, typeclass instance or coercion. Arbitrary-universe σ/R parameters in accepted proof signatures provide positive evidence of the proposed generality; this is not a claim that a future valuation bundle has been audited.

## Phase 4.6 — All five proof-strategy questions

| Question | Assessment |
|---|---|
| ε–δ versus filters | n/a: no topology. |
| Elements versus substructures | Coefficient support is the right local proof. A new filtration package would be a separate API proposal. |
| Sequences versus nets | n/a: finite minimum, no limit process. |
| Construction versus universal property | Existing aeval already provides substitution. No alternative categorical proof simplifies the estimate. |
| Missing helpers | A degree lower-bound law under a compatible coefficient-support shift would serve Hasse and other filtered operators. Existing sum/product inequalities do not discharge hs or hD. The actual proof here is a new helper. |

Strategy verdict: **REFACTOR-RECOMMENDED** for upstream support/order organization; current four-line point proof is mathematically direct and appropriate as a downstream wrapper.

## Phase 5 — Five actual mathlib methods

[Complete raw formal searches](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/formal-search.json) preserve twelve requests/results; every service returned isError=false. Pinned [current](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/rg-current.json), [standard](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/rg-literature.json) and [abstract](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/rg-abstract.json) source searches supply the fifth method.

| Method | Current form | Literature form | Abstract support-degree form |
|---|---|---|---|
| Finder | Polynomial.natDegree_hasseDeriv_le, irrelevant maximum degree bound | weightedOrder_le / le_weightedOrder | infDegree sum/product/power laws; ordinary univariate derivative-support lemma |
| Loogle | MvPolynomial subtraction inequality pattern: no items | Polynomial.hasseDeriv inequality: natDegree_hasseDeriv_le | infDegree inequality with addition: no items |
| LeanSearch | LaurentSeries.hasseDeriv, univariate degree bounds | analytic order and weightedOrder families | infDegree and generic product support inequalities |
| rg | Own theorem and actual callers | weightedOrder and univariate Hasse degree bound | infDegree implementation and sum/multiplication API, no derivative shift law |
| local | Own target | Hasse family, including project/evidence copies | infDegree and WithTop comparison |

Local index reports unavailable; its negative or generated evidence hits are not absence proofs. Remote revisions may differ from the pinned source; candidate signatures are independently checked in the native mathlib-only run. `natDegree_hasseDeriv_le` is about a maximum, in one variable, and has the wrong mathematical direction for weighted vanishing minima. `MvPowerSeries.weightedOrder_le` supplies a coefficient bound, not the coefficient shift or translated derivative. `AddMonoidAlgebra.le_infDegree_add` and `le_infDegree_mul` concern addition/multiplication of polynomials. They are not analogous derivative laws.

Conclusion: **no existing exact or more-general derivative estimate identified**. Positive reusable minimum/order building blocks are present and checked; this conclusion is bounded by actual searches and is not a proof of universal absence. [Pinned candidate hashes](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/mathlib-inputs.json) fix the inspected sources.

## Phase 5.5 — All three statement-shape checks

Normal forms: the current subtraction inequality is convenient for its two real-valued consumers; equivalently index(P)≤index(Δ_kP)+weight(k). An infinity-preserving generic law should prefer addition, avoiding subtraction from top. Projected infDegree agrees through an explicit finite-order bridge, not definitional equality.

Syntactic generality: the fixed-k premise D(i+k)=D(i)+D(k) suffices and is weaker than globally packaging D as additive. An AddHom offers a standard producer of this premise; an arbitrary D does not. Splitting the pure support theorem from the Hasse-specific support transport gives two meaningful statement shapes whose primary public home remains a design question.

Superfluous arguments: hk is essential under the project convention; P, k, α and r all carry mathematical data. Fintype and real coefficients cannot be deleted from the current fixed-parent statement. The verified expanded statement removes those interface restrictions using actual new proof and normalization. No positivity premise exists to remove. Overall **RESTATE-BEFORE-SHIP** if this becomes upstream API.

## Phase 6.0 — Every caller and inline audit

Fresh ignore-independent rg and tracked git grep agree: excluding docstrings/declaration, **two source callers, one application each**, both in proof bodies and neither in theorem statements. [Complete searches](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/complete-caller-search.json) cross-check the canonical inventory. [Caller fragments/plans](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/callers.json) preserve exact source/hash data.

| Caller | Source | Role / refactor |
|---|---|---|
| Roth.sum_max_sub_le_index_det | Theta.lean:390 | Bounds each nonzero determinant entry's index. Replace the sole call with the checked replacement, preserving Option-coordinate weight rewrites and nonzero premise. |
| private Roth.exists_hasseDeriv_index_eval_bound_aux | MainLemma.lean:494 | Preserves a large α-index after selecting a derivative nonvanishing at z. Replace the sole call with replacement at the same hk/α/r; map/Hasse compatibility remains explicit. |

Both entire caller proofs were replayed with only this substitution. The private caller's actual kernel name is separately audited using canonical private-name construction, not an invalid pasted `_private...0...` identifier. The [inline search](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/rg-inline.json) found no additional independent derivative-index rederivation beyond this theorem and its uses. Kernel direct-consumer count2 agrees here with source count2, but is not a simp/transitive dependency closure. This is a used API, not dead code.

## Phase 6 — Actual composition and re-aim experiments

The [mathlib-only clean source](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-mathlib-clean-executed.lean.txt) and [raw clean receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-mathlib-clean-receipt.json) prove supportShift over arbitrary σ/CommSemiring coefficients with the exact hs coefficient implication and hD shift law. Guards show both the project target and multivariate Hasse operator are absent from its imports. The proof uses an attained finite-support minimum, a support image membership proof, csInf comparison and additive rearrangement. It is new reasoning, not ≤3 existing calls.

The first isolated attempt failed only because broad add_comm simplification changed i+k before hD fired; its [source](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-mathlib-initial-executed.lean.txt) and [receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-mathlib-initial-receipt.json) are rejected evidence. The clean proof rewrites hD i and the attaining equality explicitly. Limits were not raised.

The actual-context pointShift obtains hs from coeff_taylor and hasseDeriv_hasseDeriv, using only right_ne_zero_of_mul. This is precisely the normalization/support transport that would be missing from a purported infDegree-only existing-call replacement. The independently checked replacement specializes D to Roth.weight and uses weight_add. A single call to this *new* helper is not a mathlib composition.

The parent [mathlib-only finite bridge](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-mathlib-infdegree-final-executed.lean.txt), [receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-mathlib-infdegree-final-receipt.json), and [actual-context bridge](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-consumers-executed.lean.txt) with [receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-consumers-receipt.json) are supporting representation evidence, not inherited law evidence. The retained warm prefix is documented in [trim evidence](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/warm-session-trim-after-index139.json) with [exact executed prefix](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/warm-session-index139-trimmed-executed.lean.txt) and [clean receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/warm-session-index139-trim-native-receipt.json). Their historical region numbers remain historical.

[Fresh projectedInfDegreeShift](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-reaim-executed.lean.txt) explicitly transfers both minima through this bridge and applies the newly proved pointShift. The [combined complete clean receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-reaim-guards-callers-receipt.json) verifies this theorem, [both guards](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-guards-executed.lean.txt) and [both complete caller replays](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-callers-executed.lean.txt), scoped to fresh regions939/959/981. The final [expanded aeval statement receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-expanded-reaim-receipt.json) is separately clean at region1049. An initial combined run failed in the guard because degreeOf_X needed an explicit simp lemma; its [rejected guard source](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-guards-initial-executed.lean.txt) and [rejected receipt](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-reaim-guards-callers-initial-rejected-receipt.json) are not accepted verification. The re-aim/caller regions were unchanged in the successful rerun. Thus the representation bridge and the re-aimed law are actual checks, while the derivative law remains new. The parent re-aim gate therefore supplies **no NO-mathlib-has-it conclusion**: there is no independently identified existing analogous law. The generic definition's arbitrary D is not magically shift-compatible.

The Bool guard has P=X_false, center0, weights r_false=1/r_true=2 and derivative order e_true. The derivative is0, index(P)=1 and weight(k)=1/2, so dropping hk would assert1/2≤0. The all-zero-denominator specialization still checks with hk. This separates the essential nonzero premise from unnecessary positivity of denominators.

Composition verdict: **NOT-COMPOSABLE** from ≤3 existing mathlib calls in the original spelling or checked re-aim. The existing proof's project attainment/composition/index lemmas are not mathlib building blocks. No closing simp[definitions] experiment is used as a NO verdict, and no unsupported absence or complexity argument is used as a YES/BORDERLINE reason.

## Phase 7 — Verdict and action

**YES-but-generalise-first**, reason **MODERN-IDIOM / re-aim**. There is a concrete mathematical gap: a compatible coefficient-support shift must imply a lower bound for support infimum degree, with the Hasse derivative specialization. The missing premise is not provided by current infDegree sum/product API. The independently verified standalone projectedInfDegreeShift provides the broader theorem without changing any production parent or caller. It is not an existing mathlib replacement and is not justified merely by search absence. Its proof supplies precisely the missing coefficient/support transport and real finite-minimum inequality. The two replayed consumers demonstrate practical use.

Ship the checked theorem over arbitrary σ, CommRing R and D satisfying the fixed-k additive shift premise. Its explicit statement is in [re-aim execution](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-reaim-executed.lean.txt); its [expanded aeval spelling](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/index-sub-weight-expanded-reaim-executed.lean.txt) avoids requiring a second named Taylor definition. Its target is projected infDegree with hk, as verified; the infinity-preserving variant and broader ordered target are possible later extensions, not claimed accepted proof evidence. An arbitrary D without compatibility is rejected. This is an actual compiled modern restatement, not a suggestion that a substantial production-wide migration has already happened or is a prerequisite.

Proposed upstream file: **Mathlib/Algebra/MvPolynomial/TaylorDegree.lean**, an extension importing proposed **Mathlib/Algebra/MvPolynomial/Taylor.lean** and existing **Mathlib/Algebra/MonoidAlgebra/Degree.lean**, plus the finite real-order/WithTop support needed by the checked statement. Taylor imports the proposed **Mathlib/Algebra/MvPolynomial/HasseDeriv.lean** foundation already accepted for contribution. This layering keeps real order and infDegree out of the foundational Hasse operator and keeps Taylor coefficient transport available. A generic target-order support lemma can be separately placed in MonoidAlgebra/Degree once stated without importing real analysis there; this does not block the checked standalone Hasse result. Existing aeval may spell translation if the optional Taylor name is declined.

Proposed PR title: **feat(Algebra/MvPolynomial): weighted degree bounds for Hasse derivatives**. Group with the actually accepted YES declarations **MvPolynomial.coeff_taylor**, **MvPolynomial.hasseDeriv**, **MvPolynomial.coeff_hasseDeriv**, **MvPolynomial.hasseDeriv_hasseDeriv** and **MvPolynomial.taylor_eq_zero_iff**, staging foundational/operator and degree-bound PRs as needed. [Fresh grouping inventory](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/accepted-grouping.json) records their real verdicts; no YES is inferred from a useful name or from the parent index.

Next actions:

1. Run `/generalise Roth.index_sub_weight_le_index_hasseDeriv` toward the exact checked projectedInfDegreeShift/expandedProjectedShift signature; preserve hk and hD. The semantic improvement is arbitrary coefficients/variables/weights and reuse of existing minimum-degree API, not merely fewer lines.
2. Add the standalone theorem in TaylorDegree.lean with the explicit support/finite-order proof, plus any normalization bridge it needs. Keep Roth.index as a downstream convention wrapper; recover its current theorem and both caller applications through the verified specialization. No foundational project-wide migration is required for the contribution.
3. Run `/cleanup Mathlib/Algebra/MvPolynomial/TaylorDegree.lean MvPolynomial.projectedInfDegreeShift`, the full import/downstream/style checks and `/pre-submit`. The displayed name is provisional and should follow final upstream naming; this survey has not run a future PR build.
4. Select **Yaël Dillies** (MvPolynomial coefficient refactor631b214f7c) or **Moritz Firsching** (Polynomial Hasse derivative map334438dace) from the [fresh relevant Git history](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/reviewer-history.json); recheck then-current duplication before proposing the PR. No reviewer is contacted and no PR is created here.

A project-local wrapper can remain in Roth/Index.lean for its zero convention and both point-index uses. There is no deletion recommendation based on the parent's NO verdict. The contribution is a law about the existing generic degree representation, not another definition of weighted order. Ordinary naming/packaging preferences do not require a BORDERLINE pause after the standalone general theorem has been verified.

## Phase 8 — Evidence handoff

[Assessment](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/assessment.json), [verification](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/verification.json), [overview entry](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/overview-entry.json), [manifest](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/copy-manifest.json) and [portable validator](../evidence/Roth.index_sub_weight_le_index_hasseDeriv/validate.py) record phase completion and native evidence. Verification unresolved=[] means the stated checks completed; unverified future extensions are explicitly distinguished from the checked proposal. Root acceptance is pending. Production, pins, Git state and overview/progress files were not changed by this worker.
