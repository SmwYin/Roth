# Roth.le_index_iff — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** On the independently verified parent representation `AddMonoidAlgebra.infDegree`, the analogous lower-bound equivalence is exactly `Finset.le_inf_iff`. This is the explicit parent re-aim rule, with a fresh law check and a checked representation bridge, rather than an inherited verdict.

## Phase 0 — Doctor

Canonical declaration 137 is the public theorem at `Roth/Index.lean:85`. The entire declaring [Index module](../evidence/Roth.le_index_iff/Index.lean.txt) and external [MainLemma module](../evidence/Roth.le_index_iff/MainLemma.lean.txt) were read. Index develops weighted order at a point and its derivative, additive, multiplicative, renaming and univariate laws. The target resolves without sorry and is one of the module's main results. [Canonical entry](../evidence/Roth.le_index_iff/canonical-entry.json).

The [baseline build](../evidence/Roth.le_index_iff/baseline-build.txt) succeeded with exit 0, 2467 jobs and no reported errors/warnings. All 17 current source/pin hashes freshly agree with the baseline manifest: [inputs](../evidence/Roth.le_index_iff/inputs.json), [hash check](../evidence/Roth.le_index_iff/input-hash-check.json). No production or pin modifications were made by this assessment.

## Phase 1 — Comprehend

For a nonzero real polynomial in finitely many variables, a real number c is at most its index at α relative to r exactly when c is at most the weight of every exponent whose Hasse derivative is nonzero at α. The Taylor coefficient identity identifies those exponents with the support of the translate P(X+α). Thus the result is the greatest-lower-bound characterization of a nonempty finite set of real weights.

Full native elaborated type:

```lean
Roth.le_index_iff.{u_1} : ∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℝ},
  P ≠ 0 → ∀ {α : σ → ℝ} {r : σ → ℕ} {c : ℝ},
    c ≤ Roth.index P α r ↔
      ∀ (d : σ →₀ ℕ), (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0 →
        c ≤ Roth.weight r d
```

σ indexes the variables and is universe-polymorphic; Fintype enables the parent weight's global finite sum. P is the polynomial, α the translation center, r the natural denominators, c the candidate lower bound, and d a finitely supported exponent. The only mathematical hypothesis is P≠0; positivity of r is deliberately absent, including mixed zero denominators. The project index of zero is 0, so nonzero support is essential for this real-valued iff: with P=0,c=1 the RHS is vacuous but the LHS fails.

The original forward implication composes the proposed bound with index_le_weight. The reverse applies le_csInf to the nonempty translated support image, converting membership by the private mem_support_taylor_iff. [Original printer source](../evidence/Roth.le_index_iff/le-index-iff-original-executed.lean.txt), [fresh audit source](../evidence/Roth.le_index_iff/le-index-iff-audit-executed.lean.txt), [complete native receipt](../evidence/Roth.le_index_iff/le-index-iff-original-audit-receipt.json) show the full type, proof body without elision, standard axioms and canonical 293 requested/unique/present/value-bearing declarations. Audit information is scoped to the new region 2181/2182; historical scratch info is not substituted for it.

## Phase 2 — Preliminary checks

**BIG**, because `Roth.le_index_iff` is explicitly listed under Main results. This narrative classification does not reduce the exhaustive search. One-line definition check is **n/a — theorem**, not def/abbrev/structure. No glue-lemma inheritance applies: the proof has two genuine implications and uses conditional-infimum API.

## Phase 3 — Exhaustive literature

Exact requests, returned UTF-8 response sizes/digests and sanitized titles/URLs are preserved in [general forms](../evidence/Roth.le_index_iff/web0-metadata.json), [nLab/nCatLab/Stacks](../evidence/Roth.le_index_iff/web1-metadata.json), [MO/arXiv](../evidence/Roth.le_index_iff/web2-metadata.json), [refinements](../evidence/Roth.le_index_iff/web3-metadata.json), and [recent/primary access](../evidence/Roth.le_index_iff/web4-metadata.json). Full returned bodies are not persisted. [Original literature summary](../evidence/Roth.le_index_iff/literature-summary.json), [local search](../evidence/Roth.le_index_iff/local-literature-search.json), [local excerpt](../evidence/Roth.le_index_iff/clean-excerpt.tex.txt).

| Channel | Actual query or source | Result / limitation |
|---|---|---|
| General web, specific | `Roth theorem index polynomial vanishing derivatives weighted minimum lower bound` | Roth ICM1958 p206 defines the index through the least nonvanishing derivative. Min Ru's Roth notes, Definition1 pp2–3, use normalized derivatives and the minimum of exponent/degree sums. |
| General web, standard | `weighted order polynomial monomial valuation coefficient vanishing lower bound` | Weighted-order and monomial-valuation material; the mathlib documentation gives coefficient vanishing below weighted order. This is adjacent support-order language. |
| General web, abstract | `infimum finite set greatest lower bound characterization order theory` | Order-theory sources describe the greatest lower bound; this isolates the exact content from the polynomial application. |
| ChatGPT math | Standard form/generality/history consultation | **n/a: ask_chatgpt_math unavailable**. No fabricated answer or ninth synthetic channel. |
| Local references | clean.tex530–556; subsequent addition proof and1511 | The manuscript defines an attained nonvanishing-Hasse minimum; its proof of the main lemma infers a lower index bound from low-weight vanishing. The manuscript assigns zero +∞; the project chooses0 and explicitly assumes nonzero here. |
| nLab | `site:ncatlab.org/nlab infimum lower bound meet semilattice` | [meet](https://ncatlab.org/nlab/show/meet) characterizes finite meets by common lower bounds and identifies empty meet with top. Search access succeeded; direct open failed unsupported application/xhtml+xml. |
| nCatLab | `site:ncatlab.org/ncatlab infimum semilattice lower bounds`; `site:ncatlab.org/ncatlab "meet"` | Both explicit namespace queries returned nLab pages, with no exact /ncatlab hit. Out-of-namespace results are recorded honestly, not proof of absence. |
| Stacks | `site:stacks.math.columbia.edu polynomial order vanishing coefficients`; refined `"order of vanishing" polynomial` | [02MB §10.121](https://stacks.math.columbia.edu/tag/02MB), especially Definition10.121.2, uses length-defined orders on one-dimensional local Noetherian rings. It is adjacent valuation context, not this finite-support iff. Direct access succeeded. |
| MathOverflow | `site:mathoverflow.net weighted order polynomial monomial valuation derivatives` | [449959, leadable monomials](https://mathoverflow.net/questions/449959/which-monomials-are-leadable) discusses support geometry and weighted lexicographic order, not the lower-bound universal property. Other derivative hits were unrelated. |
| Recent arXiv, last five years | Broad2022–2026 queries; refined `site:arxiv.org after:2021-10-27 "monomial valuations"` and weighted/Hasse query | [Kim2604.18465](https://arxiv.org/abs/2604.18465), abstract, treats quasi-monomial valuations computing α/δ invariants. It is recent related context, not a new form of the elementary finite meet law. Weighted quartic/Hasse-principle hits are unrelated and do not support the iff. |
| Direct primary access, supplementary | ICM1958 PDF; Min Ru notes | ICM PDF open failed because its74705952-byte content exceeded retrieval limits; search passage remains available. [Min Ru PDF](https://www.math.uh.edu/~minru/fields/roth.pdf) opened successfully, Definition1 at extracted lines130–181 and pp2–3. |

The standard names are **weighted index**, **weighted order of vanishing**, and, abstractly, **finite meet/greatest lower bound**. The lower-bound criterion agrees across the polynomial definition and order-theoretic characterization. The inference from a minimum to bounds on all members is mathematical synthesis, not a claim that every source states this exact Lean theorem. Historically Roth's derivative wording and the normalized derivative/Taylor coefficient wording express the same characteristic-zero finite minimum. Modern semilattice organization removes irrelevant real and polynomial restrictions for the order law. Arbitrary degree maps alone are not valuations: no multiplicativity is asserted.

## Phase 4a–4b — Generality

| Parameter / hypothesis | Current form | Checked wider form / necessity |
|---|---|---|
| σ, universe, finiteness | Type u with Fintype | AbstractLaw uses an arbitrary A:Type u; finite support suffices, no Fintype A. |
| Coefficient ring | ℝ | AbstractLaw and projectedLaw compile over arbitrary Semiring R:Type v; no commutativity, field, domain or Nontrivial needed by the support-order law. |
| P | Multivariate polynomial | Any AddMonoidAlgebra R A, without algebraic structure on A for this statement. |
| α | Real-valued translation center | Used only in selecting the translated polynomial. Disappears from the abstract law; the actual target replacement retains its independently checked Taylor bridge. |
| r, degree map | Natural reciprocal denominators | Arbitrary map D:A→T in abstractLaw; arbitrary real D in projectedLaw. Additivity, injectivity and positivity are unnecessary. |
| c, ordered codomain | ℝ | Any c:T with SemilatticeInf T and OrderTop T, universe w independent. Unlike minimum attainment, this iff does **not** require LinearOrder. |
| hP | P≠0 | Retained for the old real zero-default projection; projectedLaw uses support.Nonempty. Entirely absent for unprojected infDegree: inf empty=top makes the iff true even at zero. |
| Other implicit requirements | None | No positive-r, characteristic-zero derivative identity, finite variable nonemptiness, or NoZeroDivisors is introduced into the abstract finite-meet law. |

The fixed parent interfaces need real coefficients/Fintype in the unchanged spelling. No unchanged-parent mechanical drop is claimed. In expanded representation this is **STRICTLY NARROWER THAN STANDARD**, verified by the fresh isolated [exact source](../evidence/Roth.le_index_iff/le-index-iff-mathlib-clean-executed.lean.txt) and [raw native success](../evidence/Roth.le_index_iff/le-index-iff-mathlib-clean-receipt.json). The most general checked analogous law is:

```lean
-- [Semiring R] [SemilatticeInf T] [OrderTop T]
-- D : A → T, P : AddMonoidAlgebra R A, c : T
c ≤ AddMonoidAlgebra.infDegree D P ↔ ∀ d ∈ P.coeff.support, c ≤ D d
-- Existing proof:
Finset.le_inf_iff
```

This is an existing theorem specialization, not new API awaiting a generalise-first contribution. The projected real law is separately checked with nonempty support. The stable seven-import prefix contains no Roth import and has `#check_failure Roth.le_index_iff`. No deprecated forwarding Real import, limit raises, axioms or unsafe proofs are used.

## Phase 4c — All nine modern-idiom checks

| # | Question | Finding and concrete consequence |
|---|---|---|
|1| Typeclass preambles | Yes: Semiring/SemilatticeInf/OrderTop express exactly the existing abstract law, allowing instance-driven specialization to integer, real-lifted and product-ordered targets. |
|2| Sequences/metrics to filters | No: finite coefficient support, no topology or convergence. |
|3| Construction to universal property | Yes: the theorem is the finite meet universal property. Existing Finset.le_inf_iff supplies it directly; no new construction or characterization class is needed. |
|4| Closure predicates to bundles | No closure predicate; coefficient support is already a Finset. No submodule/ideal package improves the lower-bound iff. |
|5| Field to semiring/module | Yes: Semiring suffices for the carrier. Avoids real algebra assumptions in support-order consumers. The translation/derivative bridge is separately identified. |
|6| Higher categories | No: although meets can be seen as limits in a poset, categorical restatement adds no useful downstream consequence here. |
|7| Concrete index to ordered structure | Yes: arbitrary SemilatticeInf+OrderTop, including incomparable degree values. Reuses finite-fold bounds without linearly ordered minimum machinery. |
|8| Concrete-via-abstract diagnostic | Fires. Original proof body has zero occurrences of the identifier index, two lines mentioning index_le_weight/le_csInf, and one final support-to-Hasse conversion. No derivative-specific reasoning occurs: coefficient support conversion exposes pure lower-bound API. |
|9| False-generalization guard | The actual originalReplacement preserves the nonzero old value and all r including zero parameters. Reject dropping hP from the old zero-default theorem (P=0,c=1), replacing an infinite support by Finset without finite support, or equating this arbitrary D-order law with a multiplicative valuation. No linearity is needed for the abstract lower-bound iff; that restriction belongs to attainment, not this law. |

Modern idiom available: **yes, already in mathlib**. The real mathematical organizational improvement is separating the support-degree finite meet law from Hasse coefficient conversion. This enables degree bounds for arbitrary monoid algebras and arbitrary ordered semilattices; it is not a category-theoretic cosmetic change.

## Phase 4.5 — Infrastructure risk

All six rows are **n/a — theorem**: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe infrastructure and coercion ambiguity. The declaration provides only a proof of Prop, with no new instance, data or coercion. Parent-definition infrastructure is assessed separately.

## Phase 4.6 — All five proof-strategy checks

| Question | Assessment |
|---|---|
| ε–δ/neighborhoods versus filters | n/a: no topology. |
| Elements versus algebraic inclusions | Lower bounds on support members are the desired conclusion. No algebraic inclusion is hidden; use the existing fold-iff. |
| Sequences versus nets | n/a: no limits. |
| Construction versus universal property | Finite meet's universal property is exact. No extra class or construction needed. |
| Missing helper API | No missing lower-bound law: Finset.le_inf_iff and le_inf'_iff exist. Parent normalization and coeff_taylor are separately checked bridges. |

**REFACTOR-RECOMMENDED** after parent migration: use the generic fold characterization, with one shared representation bridge rather than repeating a bespoke two-implication proof. This is a moderate representation refactor, not a verdict based on cost. The current le_csInf proof remains idiomatic for the existing real sInf definition.

## Phase 5 — Five actual mathlib methods × three forms

[Exact requests/raw complete receipts](../evidence/Roth.le_index_iff/formal-search.json) preserve12 actual requests: Finder, Loogle, LeanSearch and local search on current Hasse/index, literature weighted-order, and abstract infDegree/finite-inf forms. [Current rg](../evidence/Roth.le_index_iff/rg-current.json), [standard rg](../evidence/Roth.le_index_iff/rg-literature.json), [abstract rg](../evidence/Roth.le_index_iff/rg-abstract.json) supply the fifth method. All requests returned; no search failure is used as evidence of absence.

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | le_weightedOrder, nat_le_weightedOrder, weightedOrder_le | weightedOrder coefficient bounds | infDegree; neighboring degree/support bounds |
| Loogle | Quoted hasseDeriv pattern clean empty | weightedOrder inequalities | **Finset.le_inf_iff**, exact signature; neighboring variants |
| LeanSearch | Weighted-order lower bounds | le_weightedOrder / nat_le_weightedOrder | infDegree and neighboring degree coefficient criteria |
| rg | Target plus consumers | Pinned weighted-order bounds | Generated dual Finset law and infDegree definition |
| local | Target plus scratch/history results, index unavailable | Weighted-order family, index unavailable | Empty, index unavailable |

Local index-unavailable is a limitation, not an absence argument; scratch/history hits are not mathlib replacements. External snapshots may differ from this pin. Fresh native signatures/proofs pin the positive candidates:

- `Finset.le_inf_iff`, generated by `@[to_dual]` from sup_le_iff at `Mathlib/Data/Finset/Lattice/Fold.lean:99`: with SemilatticeInf T/OrderTop T, `c ≤ s.inf D ↔ ∀ d ∈ s, c ≤ D d`.
- `Finset.le_inf'_iff`, generated dual at Fold:557: nonempty finite meet without requiring top in the unlifted codomain. Its nonempty proof and degree-map arguments are **explicit**.
- `AddMonoidAlgebra.infDegree`, `Mathlib/Algebra/MonoidAlgebra/Degree.lean:624`, is an abbrev for coefficient-support inf.
- `Finset.coe_inf'`, Fold:538, identifies the lifted nonempty meet; `WithTop.untopD_coe` projects it. `Finsupp.mem_support_iff` turns coefficient support membership into nonvanishing.
- `le_csInf_iff`, generated dual in `Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:228`, is the conditional-complete-order analogue; it needs boundedness/nonemptiness.
- `MvPowerSeries.le_weightedOrder`, `Mathlib/RingTheory/MvPowerSeries/Order.lean:197`, is the natural/extended-natural weighted-order lower-bound law via coefficient vanishing. It is a standard adjacent API, while infDegree avoids clearing denominators or requiring positive r.

Conclusion: **found in mathlib as Finset.le_inf_iff, the exact analogous law on the more general infDegree parent**. This is positive evidence of presence, with no claimed exhaustive proof of absence.

## Phase 5.5 — All three statement-shape checks

Normal forms: (i) original nonvanishing-Hasse weight iff; (ii) coefficient support lower-bound iff for infDegree; (iii) lower bounds on nonempty inf' after real projection; (iv) vanishing below cutoff for natural-weighted power series. The generic finite support characterization is already canonical. The existing iff places the pointwise support condition on the RHS, as does the old statement, so it is useful for both .1 and .2. No quadratic web of new equivalences is proposed.

Syntactic generality attempts **actually compile**: abstractLaw uses support membership, projectedLaw uses nonzero coefficients and untopD0, originalReplacement returns the original evaluated-Hasse statement. Support membership gives the one-call abstract proof, whereas nonvanishing is convenient for the five actual uses. The real projection legitimately retains nonempty support.

Superfluous-argument audit: σ/P/α/r/c describe the quantity and bound; Fintype/ℝ are fixed by current parent interfaces. hP is necessary for the unchanged zero-default form and not superfluous. No positivity or nonempty-variable premise is needed. Dropping hP is verified only after changing to the unprojected top-valued representation. Normal form **REFACTOR** to existing infDegree; syntactic generality **RESTATE** to existing finite support iff; fixed-parent superfluous arguments **NONE**. Overall **RESTATE-BEFORE-SHIP** for a hypothetical upstream addition, which would duplicate existing API.

## Phase 6.0 — Complete caller and inline audit

[Caller inventory/full fragments](../evidence/Roth.le_index_iff/callers.json), [canonical source inventory plus rg/git-grep receipts](../evidence/Roth.le_index_iff/complete-caller-search.json), [direct consumers](../evidence/Roth.le_index_iff/direct-consumers.json). Fresh enumeration includes every canonical production file and Roth.lean, with --no-ignore and tracked git-grep cross-check. The initial git-grep regex was overescaped and returned exit1; its rejected receipt is retained, and the accepted explicit whole-word retry returned all seven source lines (docstring, declaration and five applications). There are **five applications in four declarations**: four applications in Index, one in MainLemma. Internal use count excluding the declaring file **K=1**, one distinct external module. There are separately **four direct kernel-value consumers** in the canonical audit; no opaque/transitive/simp dependency-closure claim is made. The target is not simp and is useful local API, not dead code.

| Caller | References | Refactor after shared bridge |
|---|---|---|
| Roth.le_index_sum | Index:121,125 | Use generic iff .2 for the translated sum; generic iff .1 for the selected nonzero summand. Retain map_sum, exists_ne_zero_of_sum_ne_zero and hfi. |
| Roth.index_eq_weightedOrder_div | Index:154 | Use generic iff .2; retain denominator identity, div bound and power-series weightedOrder_le. |
| Roth.index_unique | Index:248 | Use generic iff .2; retain univariate coefficient key, trailing-degree lower bound and division inequality. |
| Roth.le_index_of_forall_eval_eq_zero | MainLemma:423 | Use generic iff .2; retain le_of_not_gt, low-weight vanishing, box restriction and degree-bound zero derivative. |

[Inline search](../evidence/Roth.le_index_iff/rg-inline.json) finds the target's own le_csInf introduction, the stated callers and the low-weight-vanishing corollary. It finds no additional independent re-derivation of this exact iff outside the target. Weighted-order bounds in Index are analogous ingredients in a separate representation, not hidden explicit uses. Multiple uses justify a manuscript-facing convenience lemma locally; they do not establish an upstream gap.

## Phase 6 — Actual composition and representation bridge

The fresh isolated [law source](../evidence/Roth.le_index_iff/le-index-iff-mathlib-clean-executed.lean.txt) and [raw success](../evidence/Roth.le_index_iff/le-index-iff-mathlib-clean-receipt.json) prove the analogous infDegree statement with exactly **one existing mathlib call**, `Finset.le_inf_iff`, by reducibility of infDegree. projectedLaw then normalizes through coe_inf', untopD_coe and support membership, invoking le_inf'_iff with explicit hP D. The [rejected initial source](../evidence/Roth.le_index_iff/le-index-iff-mathlib-initial-executed.lean.txt) and [receipt](../evidence/Roth.le_index_iff/le-index-iff-mathlib-initial-receipt.json) are retained because omitting those explicit arguments did not elaborate; they are not accepted proof evidence.

I independently inspected the parent's accepted [isolated bridge source](../evidence/Roth.le_index_iff/index-expanded-mathlib-executed.lean.txt) and [complete raw success](../evidence/Roth.le_index_iff/index-expanded-mathlib-receipt.json). Its finsetBridge handles empty support by zero-default projection and nonempty support by coe_inf' and inf'_eq_csInf_image. denominatorBridge expands reciprocal Finsupp.weight and translation as aeval. These are real newly proved normalization bridges, not preexisting one-call mathlib replacements. The [actual target bridge](../evidence/Roth.le_index_iff/index-consumers-executed.lean.txt), [receipt](../evidence/Roth.le_index_iff/index-consumers-receipt.json), [fully expanded bridge](../evidence/Roth.le_index_iff/index-expanded-bridge-executed.lean.txt), [receipt](../evidence/Roth.le_index_iff/index-expanded-bridge-receipt.json) match the old parent for **all P and all r**, including zero and mixed zero-r cases. No definitional equality between the old index and projected infDegree is claimed.

The fresh [originalReplacement source](../evidence/Roth.le_index_iff/le-index-iff-target-executed.lean.txt) and [complete native receipt](../evidence/Roth.le_index_iff/le-index-iff-target-receipt.json) obtain nonempty Taylor support from hP, rewrite the actual parent bridge, pass through coe_inf'/untopD, and apply le_inf'_iff with coefficient conversion via coeff_taylor. It invokes neither Roth.le_index_iff nor downstream index laws. This old spelling uses **more than three total normalization/building-block steps**, including project Taylor API. Thus **NOT-COMPOSABLE as a bare ≤3-call old-form term**; project lemmas do not count as mathlib blocks.

The fresh [whole Index/four-consumer experiment](../evidence/Roth.le_index_iff/le-index-iff-callers-executed.lean.txt), [native receipt](../evidence/Roth.le_index_iff/le-index-iff-callers-receipt.json) replay the entire Index with the target renamed replacement and proved from originalReplacement, covering all four Index applications. They separately replay the complete MainLemma le_index_of_forall_eval_eq_zero body with its fifth application replaced. The original target identifier occurs nowhere in this accepted replay, and replacement/all four consumers print standard axioms. A [rejected initial caller source](../evidence/Roth.le_index_iff/le-index-iff-callers-initial-rejected-executed.lean.txt) and [receipt](../evidence/Roth.le_index_iff/le-index-iff-callers-initial-rejected-receipt.json) preserve a long-line style warning; the accepted source only wraps that line and is warning-free.

Composition conclusion: **one existing call on the re-aimed parent**, with honest nondefinitional normalization for the old form. A closing simp[defs] alone would trigger Phase6b's BORDERLINE caution; it is not the deciding evidence. Mode B's explicit re-aim rule instead requires NO-mathlib-has-it when the already-existing parent has this analogous law, after independently verifying the law and bridge. Both gates passed.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it** via `Finset.le_inf_iff`, generated dual at Fold:99, on `AddMonoidAlgebra.infDegree`. The arbitrary semilattice finite-meet iff is already one existing call. Fresh isolated and actual-context checks independently verify the re-aim and its bridge. No bare-name collision, inherited conclusion, search-failure absence claim, cost downgrade or false ≤3-call old-form claim supports the verdict.

To remove the wrapper, first migrate the parent to projected infDegree or retain one shared local bridge. At Index:121 and125 use the finite support iff's .2/.1 respectively; at Index:154 and248 and MainLemma:423 use .2. Normalize projection once using the nonzero Taylor support, convert support membership via coeff_taylor, and retain each caller's subsequent steps listed above. Delete le_index_iff after replacing these **five** applications if eliminating local wrappers. The accepted complete caller replay verifies argument compatibility and both iff directions. Do not duplicate the parent real-sInf bridge at five sites.

Alternative destination: **project-local convenience API in Roth/Index.lean**, matching the manuscript and its four consumers. Archive or a satellite library is unnecessary for this specialized elementary spelling. No upstream PR is proposed, so YES-only PR grouping/reviewer-selection steps are n/a. Other index laws still require independent re-aim assessments.

## Phase 8 — Handoff

All required phases are complete, verification unresolved=[], root acceptance pending. [Assessment](../evidence/Roth.le_index_iff/assessment.json), [verification](../evidence/Roth.le_index_iff/verification.json), [overview entry](../evidence/Roth.le_index_iff/overview-entry.json), [current manifest](../evidence/Roth.le_index_iff/copy-manifest.json), [portable read-only validator](../evidence/Roth.le_index_iff/validate.py). The validator supports scratch/integrated layouts; checks current manifest hashes/bytes,17 fresh source/pin hashes, exact293 canonical names/order, scoped target native audit counters and standard axioms, all four callers/five applications, all search channels, links and the credential guard. Historical worker-copy-manifest does not replace current artifact validation.
