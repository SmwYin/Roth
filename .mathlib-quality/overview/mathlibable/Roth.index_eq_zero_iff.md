# Roth.index_eq_zero_iff — full mathlibable assessment

**Verdict: NO-mathlib-has-it.** After re-aiming at `AddMonoidAlgebra.infDegree`, the mathematical law is the existing `Finset.inf_eq_bot_iff`: a finite minimum is bottom iff some supported degree is bottom. Strictly positive weights identify that supported exponent with zero. The actual real index requires both its nondefinitional parent bridge and a checked nonnegative-degree recoding; neither is silently counted as an existing mathlib call.

## Phase 0 — Baseline and scope

Canonical declaration139 is the public theorem at `Roth/Index.lean:98`. The entire declaring module, the sole explicit consuming declaration `index_prod`, and parent reports133 and135–138 were read. Parent verdicts are context; the analogous law and representation connection are checked independently here. [Source](../evidence/Roth.index_eq_zero_iff/Index.lean.txt), [canonical entry](../evidence/Roth.index_eq_zero_iff/canonical-entry.json), [caller inventory](../evidence/Roth.index_eq_zero_iff/callers.json).

The [baseline build](../evidence/Roth.index_eq_zero_iff/baseline-build.txt) succeeded, exit0,2467 jobs, no reported errors/warnings. Its reuse is justified by fresh equality of all17 source/pin hashes with the shared manifest: [inputs](../evidence/Roth.index_eq_zero_iff/inputs.json), [fresh check](../evidence/Roth.index_eq_zero_iff/input-hash-check.json). No production source, pin or Git mutation was made by this worker.

Fresh [original commands](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-original-executed.lean.txt), [canonical audit](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-audit-executed.lean.txt) and [raw receipt](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-original-audit-receipt.json) establish successful nonpartial elaboration, standard axioms only, and the full short kernel body without printer elision. Audit checks all293 names in exact canonical order, including private names:293 unique/present/value-bearing. Original info starts4232, audit4235; historical info is not substituted. Exactly one direct kernel-value consumer is `Roth.index_prod`.

## Phase 1 — Statement and mathematics

For a nonzero real multivariate polynomial and strictly positive natural denominator parameters, index at α equals zero iff evaluation at α is nonzero. Taylor expansion converts evaluation into its exponent-zero coefficient. The support minimum is attained. All weights are nonnegative and, by strict positivity of denominators, only exponent0 has weight0. Conversely a nonzero exponent-zero coefficient supplies weight0 and nonnegativity gives equality.

Full native type:

```lean
Roth.index_eq_zero_iff.{u_1} {σ : Type u_1} [Fintype σ]
    {P : MvPolynomial σ ℝ} (hP : P ≠ 0) {r : σ → ℕ}
    (hr : ∀ j, 0 < r j) (α : σ → ℝ) :
    Roth.index P α r = 0 ↔ (MvPolynomial.eval α) P ≠ 0
```

σ indexes variables, Fintype supports the parent global weight sum, P is the polynomial, r supplies denominators, α is the center. hP rules out empty Taylor support and its default0; hr prevents nonzero exponents from having zero weight. The proof uses project `exists_weight_eq_index`, `weight_eq_zero_iff`, `hasseDeriv_zero_apply`, `index_nonneg` and `index_le_weight`, with index/weight/translation in their types. These project declarations do not count as existing mathlib building blocks.

## Phase 2 — Preliminary checks

**SMALL**: an elementary minimum/constant-coefficient criterion; its source statement is standard, but it introduces no major structure or theorem. Exhaustive search still applies. One-line-definition test and its exemptions are **n/a: theorem**, not a definition. The original proof has two substantive directions and minimum-attainment content.

## Phase 3 — Exhaustive literature

[General searches](../evidence/Roth.index_eq_zero_iff/web-a-metadata.json), [nLab/nCatLab/Stacks](../evidence/Roth.index_eq_zero_iff/web-b-metadata.json), [MO/recent arXiv](../evidence/Roth.index_eq_zero_iff/web-c-metadata.json), [refinements/direct access](../evidence/Roth.index_eq_zero_iff/web-d-metadata.json) retain exact requests, UTF-8 response hashes/bytes/status and sanitized locators, without bodies. [Local search](../evidence/Roth.index_eq_zero_iff/local-literature-search.json), [exact source excerpt](../evidence/Roth.index_eq_zero_iff/clean-excerpt.tex.txt), [synthesis](../evidence/Roth.index_eq_zero_iff/literature-summary.json).

| Channel | Actual query / primary locator | Finding |
|---|---|---|
| General specific | `Roth theorem polynomial index zero if only if polynomial does not vanish positive weights` | [Roth ICM1958](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), p206: weighted minimum of nonvanishing derivative orders. Indexed excerpt inspected; direct PDF open failed because74,705,952 bytes exceeds fetch limit. |
| General standard | `weighted order vanishing zero constant coefficient positive weights monomial valuation` | Weighted-support language and importance of zero-weight variables. Inference: positive weights force weight0 precisely at constant exponent; arbitrary nonnegative weights do not. |
| General aliases | `Dyson lemma index polynomial nonvanishing at point index zero` | [Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf), Definition1, pp2–3/extracted lines130–181, defines the same positive-integral-weight derivative minimum. Direct six-page PDF access succeeded. |
| ChatGPT math | Standard form/generality/history | n/a: ask_chatgpt_math unavailable; no simulated answer. |
| Local clean.tex | index/nonzero/vanish search; §4 lines530–570 | Exact criterion and proof. Positive REAL denominators; value+∞ at the zero polynomial, so source criterion also holds at zero. The project uses real fallback0 and needs hP. |
| nLab | `site:ncatlab.org/nlab valuation order vanishing constant term zero positive weights` | [Valuation](https://ncatlab.org/nlab/show/valuation), Definition/Rational functions: additive valuation convention∞ at0 and smallest nonzero degree as an example. Adjacent abstraction, not an exact Roth-index theorem. Direct open failed unsupported XHTML; search text inspected. |
| nCatLab | `site:ncatlab.org/ncatlab weighted order vanishing polynomial valuation constant coefficient` | Actual distinct namespace query returned off-path nLab material, including an Euler-characteristic paper whose vanishing-constant-term discussion is unrelated. No exact in-namespace hit located; not an absence proof. |
| Stacks | `site:stacks.math.columbia.edu order vanishing zero unit local ring` | [Tag02MB](https://stacks.math.columbia.edu/tag/02MB), Definition10.121.2, direct access succeeded: local-ring order via length. Unit/nonvanishing context is adjacent; not arbitrary multivariate weighted support. |
| MathOverflow | `site:mathoverflow.net weighted valuation strictly positive weights order zero constant coefficient`; refinement `site:mathoverflow.net "monomial valuations" weights` | Returned weighted graphs, polynomial positivity and lattice-point valuations. These are rejected as exact weighted-order-zero references. No proof or absence conclusion is inferred from those mismatches. |
| Recent arXiv | `site:arxiv.org/abs/ "monomial valuation" "positive" after:2021-10-27`; Roth/index/polynomial query; Taylor refinement | Five-year window2021-10-27–2026-10-27. [Dutta–Ghosh2609.03451](https://arxiv.org/abs/2609.03451), submitted2026-09-03: monomial valuations through Taylor expansions in positive characteristic; abstract inspected, adjacent rather than this criterion. 2609.11107 and2604.18465 concern quasi-monomial valuation geometry. Additive-combinatorial Roth papers are rejected. |

Standard names: weighted index, weighted order of vanishing, constant term criterion. Source and classical presentations agree on a positive weighted derivative minimum; coefficient-support language handles Hasse derivatives without characteristic-zero factorial division. The abstract order law is a finite-minimum criterion. A valuation carries additional algebraic laws; arbitrary degree maps in the checked generic statement are not automatically valuations. Literature supports more general coefficient/weight settings; existing library API already supplies the underlying order law.

## Phase 4a–4b — Parameter and generality audit

| Parameter / hypothesis | Fixed parent interface | Expanded representation and actual necessity |
|---|---|---|
| σ:Type u, Fintype | Arbitrary universe; Fintype used by Roth.weight global sum | AbstractLaw uses arbitrary A:Type u with no Fintype; finite coefficient support suffices. No claim of mechanically dropping Fintype while keeping the parent signature. |
| ℝ coefficients | Fixed in index, translation and evaluation | Arbitrary Semiring R:Type v in abstractLaw and real-degree bridges. No domain, nontrivial coefficient ring, characteristic-zero or field assumption for the finite-support order criterion. Translation is separate algebra data. |
| P and α | Nonzero polynomial translated at arbitrary α | Arbitrary AddMonoidAlgebra R A; distinguished exponent a₀:A replaces zero. Point data disappears once the Taylor input is supplied. |
| r:σ→ℕ | Positive reciprocal denominator weights | Arbitrary D:A→T with `D a = ⊥ ↔ a = a₀` in bounded linear target. Real version needs nonnegative D and `D a=0↔a=a₀`; positivity away from a₀ is genuine, not optional. No additivity or injectivity beyond the zero fiber is required. |
| hP:P≠0 | Essential for the old default0 theorem | P=0 gives index0=0 and eval0=0, an actual checked polynomial guard. Nonempty support is used by the real-to-unprojected zero bridge. Unprojected bounded nontrivial target law covers zero because inf empty=top≠bottom. Right-to-left eval≠0 already implies P≠0. |
| hr:∀j,0<rj | Sufficient and necessary for a uniform statement over all P | Actual Unit X with r0 and Bool X false with mixed r(false)=0,r(true)=1 have index0 and evaluation0. For a particular P, parameters of variables absent from Taylor support need not be positive; support-local zero-fiber control suffices mathematically. No such untested weakening is advertised as mechanically compiled. |
| Ordered result | ℝ, which has no bottom | Generic law needs LinearOrder+BoundedOrder+Nontrivial T. Recode nonnegative real degrees into WithTop NNReal, whose bottom0 exists, and prove its relationship to the old projection. Do not instantiate bottom with0 in WithTop ℝ: that type lacks bottom. |
| Other assumptions | None | Empty σ is allowed; hr is then vacuous and polynomials are constants. No Nonempty σ, DecidableEq σ or NoZeroDivisors is introduced. |

The independent [mathlib-only laws](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-mathlib-clean-executed.lean.txt), [raw receipt](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-mathlib-clean-receipt.json) compile over independent universes and arbitrary Semiring. abstractLaw is one existing finite-infimum criterion plus zero-fiber/support normalization. projectedLaw is a separate newly proved generic real criterion; it does not literally instantiate abstractLaw. The checked nonnegative recoding and actual bounded replacement supply that missing connection in Phase6.

Generality: **STRICTLY NARROWER THAN STANDARD in expanded representation**, with no asserted unchanged-parent mechanical weakening. Existing mathlib already has the wider finite-infimum law, so this is no YES-generalise-first opportunity. Nontrivial T cannot be omitted unconditionally at empty support; a subsingleton target has top=bottom while coefficient support may be empty. Linear order is not casually replaced by a semilattice: meets of two nonbottom incomparable values can equal bottom.

## Phase 4c — All nine modern-idiom rows

| # | Question | Finding / consequence |
|---|---|---|
|1| Typeclasses | Semiring and bounded linear order express the actual generic law; no new Index typeclass needed. |
|2| Filters/metric limits | No topology or convergence; finite support is the relevant structure. |
|3| Universal property | No new object is constructed. Finite minimum equality follows from the existing fold criterion, beyond mere greatest-lower-bound introduction. |
|4| Bundled substructure | Support is already a Finset; no closure predicate, ideal or submodule is hidden. |
|5| Field/vector space to semiring | Yes: arbitrary Semiring coefficient carrier compiles. Translation remains independently specialized; no unsupported field weakening is claimed. |
|6| Higher categories | No categorical data whose higher analogue improves this scalar criterion. |
|7| Concrete index/order | Yes: arbitrary bounded linear order and arbitrary distinguished exponent/zero fiber. This covers nonintegral and nonadditive degree maps when the fiber condition holds. |
|8| Concrete-via-abstract diagnostic | Fires. The old proof never unfolds index; it uses minimum attainment, nonnegative weights and zero-weight uniqueness. Hasse exponent0/evaluation is the final representation conversion. The actual abstract content is finite minimum equals bottom iff supported bottom degree. |
|9| False-generalization guard | Reject arbitrary D without positivity/zero-fiber premises, arbitrary signed minima identified with bottom0, dropping hP under fallback0, and allowing zero denominators in this uniform iff. Actual polynomial guards and nonnegative target recoding preserve original meaning. No infinite-series attained-minimum claim or automatic valuation structure. |

Modern idiom available **yes, already in mathlib**. Use the existing degree-support representation and order criterion; keep Taylor/evaluation and denominator conversion explicit.

## Phase 4.5 — Infrastructure risk

All six rows are **n/a: theorem**: typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priorities, universe infrastructure and coercion ambiguity. This proof of Prop introduces no data, coercion or instance. Parent risks are separate; the NNReal coercions in evidence are actually checked, not new production infrastructure.

## Phase 4.6 — All five strategy rows

| Question | Assessment |
|---|---|
| ε–δ versus filters | n/a: no topology. |
| Elements versus algebraic inclusions | No ideal/submodule inclusion; a supported distinguished exponent is the natural conclusion. |
| Sequences versus nets | n/a: no limits. |
| Construction versus universal property | No new construction. Finite-inf criterion already captures existence of a bottom-supported degree. |
| Helpers mathlib should have | No missing abstract criterion. Real projection and NNReal recoding are actual normalization proofs, not preexisting replacement calls or a missing derivative theorem. |

**REFACTOR-RECOMMENDED** after parent migration: share its projection and nonnegative-degree bridges, then use Finset.inf_eq_bot_iff. The present minimum-attainment proof is idiomatic for the existing real-sInf interface. No cost-based verdict is used.

## Phase 5 — Five actual methods × three forms

[Complete formal requests/raw receipts](../evidence/Roth.index_eq_zero_iff/formal-search.json) preserve12 actual requests: Finder, Loogle, LeanSearch and local search on each current point-index, literature weighted-order and abstract finite-infimum form. [Current rg](../evidence/Roth.index_eq_zero_iff/rg-current.json), [standard rg](../evidence/Roth.index_eq_zero_iff/rg-literature.json), [abstract rg](../evidence/Roth.index_eq_zero_iff/rg-abstract.json) provide the fifth actual method on pinned source.

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Finder | Nullstellensatz and unrelated polynomial nonvanishing | weightedOrder_eq_nat/monomial and finite-order laws | **Finset.inf_eq_bot_iff**, Nonempty variant, infDegree |
| Loogle | Quoted hasseDeriv/eval/zero pattern empty | weightedOrder/constantCoeff pattern empty | **Finset.inf_eq_bot_iff**, exact signature |
| LeanSearch | coeff_zero_eq_eval_zero, roots, unrelated Roth names | weightedOrder_eq_nat and coefficient bounds | **Finset.inf_eq_bot_iff**, Nonempty variant and sInf neighbors |
| rg | Old criterion and project zero-weight theorem | weightedOrder_eq_nat and constant coefficients | Generated dual finite-inf criterion, infDegree definition |
| local | Target and scratch/history occurrences; unrelated subgroup index | Empty | Filter.inf_eq_bot_iff, different object |

All12 formal requests returned isError=false. Local index was unavailable, so empty/mismatched local output is a limitation, not evidence of absence. Remote snapshots may differ from the pin; native proofs verify the decisive positive hit.

`AddMonoidAlgebra.infDegree` is `Mathlib/Algebra/MonoidAlgebra/Degree.lean:624`, abbreviation `P.coeff.support.inf D`. `Finset.inf_eq_bot_iff` is generated by to_dual from `Finset.sup_eq_top_iff` at `Mathlib/Data/Finset/Lattice/Fold.lean:465`; its signature requires LinearOrder, BoundedOrder and Nontrivial. `Finset.Nonempty.inf_eq_bot_iff` at the following source theorem trades Nontrivial for nonempty support. `Finset.inf'_le_iff`, generated at Fold:748, supports the separate real projected proof, while `Finset.coe_inf'` and `Finset.apply_inf'_eq_inf'_comp` support the representation bridges. `MvPowerSeries.weightedOrder_eq_nat` is adjacent natural/ENat coefficient-order API; no denominator-clearing theorem is required for the deciding hit.

## Phase 5.5 — All three statement-shape checks

Normal forms: original real index/evaluation iff; translated coefficient0 criterion; infDegree-bottom criterion with degree fiber distinguished at a₀; and nonempty real projection criterion. The generic iff places coefficient/support existence on the RHS and supports both directions. For the existing caller only .2 is used. No web of pairwise equivalences is proposed.

Syntactic generality is actually tested in abstractLaw and projectedLaw: arbitrary coefficient semiring, support carrier, degree map, ordered codomain and distinguished exponent. Support membership/nonzero coefficient normalization is explicit. The NNReal bridge checks that changing ordered codomain preserves the real index rather than merely sharing a zero symbol.

Superfluous arguments: all σ/Fintype/P/r/α parameters are fixed by the current parent interfaces. hP and hr are not uniformly droppable; checked counterexamples establish why. No nonempty-variable or positive-characteristic obstruction is added to the finite-support law. Normal form **REFACTOR**, syntactic generality **RESTATE** to existing support-infimum criterion, fixed-interface hypotheses **NONE superfluous uniformly**. Overall **RESTATE-BEFORE-SHIP**, which would duplicate existing API.

## Phase 6.0 — Complete caller and inline audit

[Canonical source inventory plus fresh rg and tracked git-grep](../evidence/Roth.index_eq_zero_iff/complete-caller-search.json), [full caller fragment/plan](../evidence/Roth.index_eq_zero_iff/callers.json), [kernel consumers](../evidence/Roth.index_eq_zero_iff/direct-consumers.json). Searches use --no-ignore across Roth/ and Roth.lean and independent tracked git-grep; both return3 lines: docstring, declaration and one application. There is **one application in one caller**, `Roth.index_prod` at Index:182. Internal count excluding the declaring file **K=0**; it is still used inside its declaring module. Direct kernel consumers separately equal one. Neither inventory is a transitive/opaque/simp closure claim. The target is not simp and is not dead code.

The empty-product base case uses `(index_eq_zero_iff one_ne_zero hr α).2 (by simp)` to show index1=0. After shared parent and nonnegative recoding bridges, use the finite support criterion with degree0 at exponent0, and keep simp evaluation1. The nonempty induction branch remains unchanged. One use makes a project wrapper removable, but the positive generic API hit decides the upstream verdict.

[Inline audit](../evidence/Roth.index_eq_zero_iff/rg-inline.json) examines index-zero/evaluation patterns across every production module. No additional independent re-derivation of this exact iff was found. Mere evaluation nonvanishing or other index bounds are not counted as equivalent bypasses.

## Phase 6 — Composition, exact re-aim and bridges

The [isolated law source](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-mathlib-clean-executed.lean.txt) and [raw clean success](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-mathlib-clean-receipt.json) verify:

```lean
-- [Semiring R] [LinearOrder T] [BoundedOrder T] [Nontrivial T]
-- hD : ∀ a, D a = ⊥ ↔ a = a₀
AddMonoidAlgebra.infDegree D P = ⊥ ↔ P.coeff a₀ ≠ 0
-- one existing criterion call, then zero-fiber/coefficient-support normalization:
Finset.inf_eq_bot_iff
```

This is the exact analogous finite-support law, not a neighboring degree inequality. The displayed abstractLaw uses one substantive existing order-law call, with infDegree unfolding and hD/exists_eq_right/Finsupp.mem_support_iff simplification. Counting these named library normalization rules too gives3 existing rules, not one complete old-form proof. It is not claimed that the entire old index statement is one mathlib call. The initial isolated projected proof failed because le_antisymm_iff rewrote equality too early; the clean proof removes that rewrite. The recoding preparation also exposed scoped NNReal notation and implicit-lift issues; clean evidence uses explicit NNReal/WithTop constructors. A180-second virtual transport timeout returned no native diagnostics and remains UNVERIFIED, not evidence of compilation failure or success. Rejected/partial/transport receipts and exact attempted sources are archived separately.

The actual [parent bridge](../evidence/Roth.index_eq_zero_iff/index-consumers-executed.lean.txt), [receipt](../evidence/Roth.index_eq_zero_iff/index-consumers-receipt.json), [expanded bridge](../evidence/Roth.index_eq_zero_iff/index-expanded-bridge-executed.lean.txt), [receipt](../evidence/Roth.index_eq_zero_iff/index-expanded-bridge-receipt.json), and [isolated expanded construction](../evidence/Roth.index_eq_zero_iff/index-expanded-mathlib-executed.lean.txt), [receipt](../evidence/Roth.index_eq_zero_iff/index-expanded-mathlib-receipt.json) were independently inspected. Empty support maps top to default0; nonempty support uses coe_inf' and inf'_eq_csInf_image. The reciprocal Finsupp-weight and aeval translation bridges handle every P and r, including mixed zero denominators. These are newly proved nondefinitional bridges.

An additional nonnegative-degree bridge is required because WithTop ℝ has no bottom. Fresh [mathlib-only recoding source](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-nonnegative-clean-executed.lean.txt), [raw clean success](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-nonnegative-clean-receipt.json), [actual-context recoding source](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-nonnegative-disk-clean-executed.lean.txt) and [nonpartial success](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-nonnegative-disk-clean-receipt.json) prove equality between the real projected support-infimum and the real coercion of the projected support-infimum of `⟨D a,hD a⟩:NNReal`, for every P. For nonempty support it proves zero of the real projection iff bottom of unprojected `infDegree` into WithTop NNReal. The accepted [boundedReplacement source](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-bounded-target-executed.lean.txt) and [nonpartial clean receipt](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-bounded-target-receipt.json) then use this exact bridge, instantiates abstractLaw at WithTop NNReal, uses weight_eq_zero_iff hr for its bottom fiber, and converts Taylor coefficient0 through coeff_taylor/hasseDeriv_zero_apply to evaluation. The independently compiled projectedLaw/originalReplacement provides a separate real proof route, not the sole justification for the bounded-target re-aim.

Fresh actual guards check P=0; Unit X at0 with all-r0; and Bool X false at0 with mixed zero/positive r. Each former case has real index0 and evaluation0; both X cases are nonzero. Thus hP and strict positivity cannot be discarded from the original uniform statement. The target proof never calls Roth.index_eq_zero_iff or downstream index laws.

The [whole Index replay](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-callers-executed.lean.txt) and [complete clean native success](../evidence/Roth.index_eq_zero_iff/index-eq-zero-iff-callers-receipt.json) remove the original target declaration, provides a replacement from the accepted boundedReplacement, and replaces the sole index_prod application. It verifies the actual argument instantiation and .2 direction with standard axioms. The original target identifier is absent from this replay.

Old-form composition is **NOT claimed ≤3 mathlib calls**: parent sInf normalization, projection, nonnegative recoding, finite-inf criterion, weight positivity/zero-fiber law and Taylor/evaluation conversion are real steps, including project API. No closing simp[defs] alone decides the verdict. ModeB explicitly requires NO-mathlib-has-it after an existing parent has the analogous law and its actual bridge is independently verified; that is the gate used here. No cost-based downgrade or blanket inheritance.

## Phase 7 — Actionable verdict

**NO-mathlib-has-it** via `Finset.inf_eq_bot_iff` on `AddMonoidAlgebra.infDegree`, with explicit nonnegative bounded-target recoding. Do not submit another specialized Roth-index-zero theorem upstream. First migrate/share the parent projection and NNReal recoding bridge. At `Roth.index_prod`, Index:182, replace the iff .2 with the existing finite-infimum bottom criterion plus the zero-degree fiber/evaluation1 normalization. Delete this wrapper after that single caller is migrated if eliminating local wrappers. The complete caller replay verifies this plan.

Alternative local destination: retain the manuscript convenience criterion in **Roth/Index.lean** if the compact point-index API is useful. No Archive/satellite library is needed for this elementary specialization. No upstream PR is proposed; YES-only path/title/grouping/reviewer requirements are n/a. Neighboring index laws still require independent assessments.

## Phase 8 — Handoff

All required phases complete after native success; unresolved=[] and root acceptance pending. [Assessment](../evidence/Roth.index_eq_zero_iff/assessment.json), [verification](../evidence/Roth.index_eq_zero_iff/verification.json), [overview entry](../evidence/Roth.index_eq_zero_iff/overview-entry.json), [current manifest](../evidence/Roth.index_eq_zero_iff/copy-manifest.json), [portable read-only validator](../evidence/Roth.index_eq_zero_iff/validate.py). The validator checks full phase coverage, successful nonpartial native evidence and standard axioms, exact canonical293 order/private names, fresh17 source/pin hashes, current manifest hashes/bytes, all search channels, sole caller and portable links/credential guard. Historical worker manifest and root-added acceptance are not substitutes for current artifact validation.
