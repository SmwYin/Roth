# Roth.abs_eval_le — full overview and mathlibable assessment

Full assessment complete; the strongest ordered-semiring generalization, exact original specialization, entire private caller and ordered293 audit are native-verified. Root integration acceptance is pending. Canonical declaration 98/293; `Roth/CoeffNorm.lean:223–239`.

## Phase 0 — baseline and scope

The shared baseline completed `lake build` successfully (2467 jobs, exit 0). A fresh comparison of every one of the 17 source/pin hashes against the shared input manifest passes. See [baseline](../evidence/Roth.abs_eval_le/baseline-build.txt), [inputs](../evidence/Roth.abs_eval_le/input-manifest.json), [read provenance](../evidence/Roth.abs_eval_le/read-inputs.json). The [final mathlib-only proof and candidate signature probe](../evidence/Roth.abs_eval_le/native-ordered-raw-executed.lean.txt) has a [clean complete receipt](../evidence/Roth.abs_eval_le/native-ordered-raw-receipt.json); the [final original specialization, full caller and canonical audit](../evidence/Roth.abs_eval_le/native-ordered-consumers-executed.lean.txt) has its own [clean complete receipt](../evidence/Roth.abs_eval_le/native-ordered-consumers-receipt.json). Root alone performed native Lean checks; the assessment changes no production Lean, pins, Git or progress files.

The declaration is public, not a prefilter. No sorry, axiom addition, unsafe proof, native_decide or raised limits occur. The complete declaring module and complete explicit-caller module were read; exact source copies are [CoeffNorm](../evidence/Roth.abs_eval_le/source-module.lean.txt) and [MainLemma](../evidence/Roth.abs_eval_le/source-callers.lean.txt).

## Phase 1 — statement and proof

An integer multivariate polynomial whose coefficients have absolute value at most B and whose degree in coordinate j is at most rⱼ satisfies |P(x)| ≤ B ∏ⱼ(1+|xⱼ|)^rⱼ. There is no positivity premise on B: evaluating the coefficient-bound hypothesis at exponent zero already implies B ≥ 0. Empty variable types, zero polynomials and zero coordinate bounds are included.

The full native type is:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    ∀ {B : ℝ}, (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
      ∀ (x : σ → ℝ),
        |(MvPolynomial.eval x) ((MvPolynomial.map (Int.castRingHom ℝ)) P)| ≤
          B * ∏ j, (1 + |x j|) ^ r j
```

Here σ is an arbitrary universe-polymorphic finite variable type; P is the polynomial; r supplies natural coordinate degree bounds; hP proves them; B bounds the real absolute values of every integer coefficient; hB proves that bound; x is any real point. The proof expands evaluation, applies the triangle inequality termwise, extends the support sum to the rectangular exponent box, factors that finite sum, and uses the geometric-sum estimate. Project body dependencies are `Roth.box`, `Roth.mem_box`, and private `Roth.sum_box_prod_pow_le_aux`; the conclusion has no project-defined object.

See [original type/proof/axioms source](../evidence/Roth.abs_eval_le/native-original-executed.lean.txt) and [complete native receipt](../evidence/Roth.abs_eval_le/native-original-receipt.json). Its axioms are exactly `propext`, `Classical.choice`, and `Quot.sound`.

## Phase 2 — preliminary classification

BIG: the module lists this theorem under Main results. The one-line definition test is n/a because this is a theorem (15 substantive proof lines), not a definition. This classification does not narrow any search phase.

## Phase 3 — exhaustive literature

All exact web requests and response SHA256/byte fingerprints, safe returned URLs and access limitations are in [batch 1](../evidence/Roth.abs_eval_le/web-1.json), [batch 2](../evidence/Roth.abs_eval_le/web-2.json), [batch 3](../evidence/Roth.abs_eval_le/web-3.json), [batch 4](../evidence/Roth.abs_eval_le/web-4.json), [batch 5](../evidence/Roth.abs_eval_le/web-5.json). Full article/search response bodies were not retained. Batched search returns a merged result set, so no unsupported per-query zero-result assertion is made.

| Channel | Actual query/access | Result and relevance |
|---|---|---|
| General web, specific | `multivariate polynomial evaluation coefficient bound product (1+ absolute value) degree` | Related coefficient/height estimates and existing mathlib homogeneous bounds. |
| General web, general | `polynomial height evaluation bound length multidegree absolute value` | Polynomial height/length and archimedean/nonarchimedean variants; no claimed exact externally named theorem. |
| General web, Roth alias/application | `Roth theorem auxiliary polynomial evaluation geometric sum coefficients bound` | Soundararajan–Petrow lecture notes, §16 Roth's Theorem II; auxiliary integer polynomials with independent degree bounds. |
| ChatGPT mathematical MCP | Standard form, generality and historical evolution query unavailable | n/a: `ask_chatgpt_math` is not installed; no fabricated second-opinion response. |
| Local reference | `clean.tex` §6 proof of Lemma 9, lines 1545–1570 | Exact local argument: coefficient bound times coordinate geometric sums, then absorb sums in `(1+|α|)^r`. [Excerpt](../evidence/Roth.abs_eval_le/local-reference-excerpt.tex.txt). |
| nLab | `site:ncatlab.org/nlab polynomial norm seminorm evaluation`; `site:ncatlab.org/nlab multivariate polynomial absolute value bound`; direct normed-ring/polynomial pages | `normed ring`, Definition: triangle and submultiplicative inequalities; supports the abstract seminorm proof. Direct open fails HTTP400 unsupported XHTML, while indexed definitions were returned; no full-page access claimed. |
| nCatLab categorical check | `site:ncatlab.org/nlab "polynomial functor" "norm"` plus polynomial page's explicit algebra-vs-functor distinction | Categorical polynomial/norm search returned Tambara functors (multiplicative transfers). These are different mathematical norm maps, not real-valued size; no categorical restatement applicable. |
| Stacks | `site:stacks.math.columbia.edu polynomial seminorm evaluation bound`; `site:stacks.math.columbia.edu "seminorm" "polynomial"`; `site:stacks.math.columbia.edu "seminorm"` | No relevant quantitative evaluation result identified; first merged batch included algebraic evaluation exercises. This is an elementary ordered estimate, not a scheme construction. |
| MathOverflow | `site:mathoverflow.net multivariate polynomial evaluation absolute value bound coefficient height` | Q151556 relates coefficient height, length, archimedean and p-adic absolute values; Q281115 treats the inverse bounded-values-to-coefficients problem. Neither states our exact estimate. |
| Recent arXiv, five years | `site:arxiv.org "polynomial" "evaluation" "height" after:2021-10-27 before:2026-10-28`; `site:arxiv.org "multivariate" "seminorm" polynomial after:2021-10-27 before:2026-10-28`; further dated Roth queries | Opened arXiv:2205.00342 (submitted 2022-04-30), finite-field multipoint evaluation algorithms; related 2111.07572, and 2024 nonlinear Roth pattern papers are distinct from this size estimate. Recent search does not change standard form. |

Primary locators: [Soundararajan–Petrow notes, §16](https://math.stanford.edu/~ksound/TransNotes.pdf); [nLab normed ring, Definition](https://ncatlab.org/nlab/show/normed%2Bring); [nLab polynomial, algebra vs polynomial-functor distinction](https://ncatlab.org/nlab/show/polynomial); [arXiv:2205.00342, abstract and submission date](https://arxiv.org/abs/2205.00342). MathOverflow is a supplementary discussion source: [coefficient factor bounds](https://mathoverflow.net/questions/151556/bounds-on-coefficients-of-factors-of-a-multivariate-polynomial), [inverse estimate](https://mathoverflow.net/questions/281115/a-bounded-polynomial-having-bounded-coefficients-several-variables).

Synthesis: this is a rectangular coefficient-to-value majorant, an elementary polynomial size estimate used in transcendence theory. Source formulations vary between height/length, individual vs total degrees, arbitrary vs equal coordinates, and archimedean vs nonarchimedean absolute values. The local paper supplies the exact geometric-sum argument. The seminorm extension is an inference from the proof and standard submultiplicative seminorm axioms, not a claim that an external source printed this exact Lean signature.

## Phase 4 — generality

| Parameter or hypothesis | Current | Assessment |
|---|---|---|
| σ universe | arbitrary `Type*` | Keep universe polymorphism. |
| Finiteness | `[Fintype σ]`, full finite product | Required by the written product interface; arbitrary finite variable types already supported. A finite-support/infinite-variable formulation is a separate API, not a claimed verified weakening. |
| Coefficients | ℤ | Replace by arbitrary commutative semiring R, with coefficient homomorphism f into the evaluation semiring. No integral, characteristic-zero, injectivity or domain property is used. |
| Evaluation codomain | ℝ | Replace by a commutative semiring S and an existing size-hom interface into an ordered commutative semiring T; verified, no subtraction needed. |
| Size function | real absolute value | Zero-preserving, nonnegative, subadditive, submultiplicative into T suffices; all four existing hom classes are used. Neither separation nor multiplicativity equality is used. |
| r | natural vector | Exponents remain natural; allowing zero is essential and already supported. |
| hP | coordinate degree bounds | Retain; supplies support containment. A support-containment spelling is equivalent via `degreeOf_le_iff`, with no mathematical strengthening; the degree formulation is retained. |
| B | real scalar | Generalizes to T in the same compiled proof; no separate B≥0 premise. |
| hB | every coefficient bounded | Retain; includes zero polynomial and forces B≥0. A support-only bound without a nonnegativity premise would fail on the zero polynomial with B<0. |
| x | arbitrary real point | Arbitrary S-valued point; no diagonal or unit-ball restriction. |

The original is STRICTLY NARROWER than the verified abstract content. The final primary form has `[CommSemiring R]`, `[CommSemiring S]`, `[CommSemiring T]`, `[PartialOrder T]`, `[IsOrderedRing T]`, and the existing Zero/Nonneg/Subadditive/Submultiplicative hom classes. No real-completeness, total-order, strict-order, negation, multiplicative equality, or normalized unit premise is needed. The exact same proof was compiled in an isolated mathlib-only environment guarded against `Roth.abs_eval_le` and `Roth.box` being loaded; generic geometric summation was reproved in that source, not imported through Roth. The exact `RingSeminorm` generalization and stronger CommSemiring/HomClass generalization compile with standard axioms, without a unit-bound premise. See [accepted RingSeminorm proof](../evidence/Roth.abs_eval_le/native-generic-clean-executed.lean.txt), [native receipt](../evidence/Roth.abs_eval_le/native-generic-clean-receipt.json), [HomClass theorem, original specialization, entire caller and audit](../evidence/Roth.abs_eval_le/native-homclass-consumers-clean-executed.lean.txt), and [complete native receipt](../evidence/Roth.abs_eval_le/native-homclass-consumers-clean-receipt.json). It uses the existing seminorm interface, not a new parent definition threaded through project files. Two coefficient-anchored inductive helpers bound `p(a*b^n)` and `p(a*∏ x_j^k_j)`; their base case simplifies `a*1=a`, avoiding the false extra assumption `p(1)≤1`. These helpers are NEW proof evidence and do not count as existing mathlib replacements.

Concrete-via-abstract diagnostic: after `rw [eval_map, eval₂_eq']`, `Int.castRingHom` occurs zero times, integer-specific theorems occur zero times, and the sole explicit ℝ annotation identifies the sum's ordered value codomain. The proof uses only finite-sum triangle, monomial submultiplicativity, support containment and the geometric bound. This diagnostic is confirmed by the actual compiled abstract theorem and original specialization; it is not an unsupported syntactic guess. See [phase notes](../evidence/Roth.abs_eval_le/phase-notes.json).

### Phase 4c — all nine modern-idiom rows

| # | Check | Answer, consequence |
|---|---|---|
| 1 | Typeclass preambles | Yes: use existing Zero/Nonneg/Subadditive/Submultiplicative hom classes or RingSeminorm interface, no custom predicate or new class. |
| 2 | Sequences/metric to filters | No: a finite algebraic inequality, no limits. |
| 3 | Construction to universal property | No: evaluation already uses `eval₂`/RingHom; no newly constructed object. |
| 4 | Closure predicate to bundled substructure | No: degree and coefficient inequalities do not define a missing algebraic substructure here. |
| 5 | Field-specific to semiring hierarchy | Yes: coefficient and evaluation CommSemirings, ordered output CommSemiring with PartialOrder and IsOrderedRing, existing hom classes; the exact proof verifies all of these weakenings. |
| 6 | Higher categorical | No: categorical norm maps found in search have different meaning. |
| 7 | Concrete indices/scalars | Variable index already arbitrary finite σ; integer coefficients/real evaluation points abstract as above. Natural exponents remain polynomial exponents. |
| 8 | Concrete-via-abstract | Yes, explicit occurrence diagnostic above and exact compiled ordered-semiring generalization/specialization. Enables real-valued RingSeminorms, complex norms, zero seminorms, and arbitrary coefficient homomorphisms through one bound. |
| 9 | False-generalization guard | Pass: same finite polynomial evaluation and same degree majorant; specializing R=ℤ, S=ℝ and p=real norm recovers the original. No unital seminorm normalization, hom injectivity, positivity of degree bounds or homogeneous polynomial premise is introduced. |

Modern-idiom verdict: available, real organizational improvement. Existing `SeminormedRing.toRingSeminorm`, `RingSeminormClass`, Zero/Nonneg/Subadditive/Submultiplicative hom classes, and `MvPolynomial.eval₂` become direct clients; a complex-valued polynomial bound no longer requires duplicating the integer-real proof. Cost is moderate proof adaptation and has no effect on the verdict.

### Phase 4.5 — infrastructure risk

n/a for all six risks (typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe polymorphism, coercion ambiguity): this declaration and proposed result are theorems, not definitions/classes/instances, and introduce none of those infrastructure paths.

### Phase 4.6 — all five proof-strategy rows

| # | Check | Answer |
|---|---|---|
| 1 | Topological ε–δ | No topology. |
| 2 | Element algebra vs substructure inclusions | No ideal/submodule inclusion is hidden; coefficient support is the relevant finite combinatorial datum. |
| 3 | Sequences vs nets | No limits. |
| 4 | Categorical construction vs universal property | Evaluation already canonical. |
| 5 | Helpers mathlib should have | Yes: rectangular evaluation majorant; generic geometric sum from accepted declaration96; optional reusable coefficient-anchored submultiplicative product estimates. |

REFACTOR-RECOMMENDED: ship a size-hom/`eval₂` theorem, factor the generic finite-sum majorant proof, and keep the original as a specialization if needed downstream. Avoid importing analysis into Algebra/MvPolynomial core. The original mathematical strategy is appropriate; shortening follows from the missing majorant API, not replacing the estimate by a different norm.

## Phase 5 — actual mathlib search

Three complete formal batches cover current rectangular form, literature absolute-value/height form, and abstract seminorm/Gauss-norm/MonoidAlgebra form. Exact requests and complete raw formal receipts: [batch1](../evidence/Roth.abs_eval_le/formal-search-1.json), [batch2](../evidence/Roth.abs_eval_le/formal-search-2.json), [batch3](../evidence/Roth.abs_eval_le/formal-search-3.json); [exact CLI searches](../evidence/Roth.abs_eval_le/source-search.json).

| Method | Actual outcome |
|---|---|
| Finder | Current form returned Chevalley degree bounds; abstract form returned Polynomial.gaussNorm and coefficient bounds; absolute-value form returned Mahler measure and Cauchy root bounds. None has the rectangular value estimate. |
| Loogle | `MvPolynomial.eval, _ ≤ _` found actual homogeneous absolute-value evaluation bounds and Height bounds; `MvPolynomial.eval₂, _ ≤ _` returned homogenization equality; absolute-value search returned finite-sum triangle and related basics. |
| LeanSearch | Found homogeneous/natDegree bounds, `le_gaussNorm`, `eval_eq`, seminorm submultiplicativity, and univariate evaluation sum expansions. |
| rg | Full-name current and guessed norm/abs evaluation names; broad polynomial evaluation/norm paths, GaussNorm, monoid algebra lift, and all callers. No proof of global absence is inferred from no hits. |
| Local | `eval_mvPolynomial_le`, `gaussNorm`, `norm_eval` returned source-backed candidates. Every result reports `index: unavailable`; this does not establish absence. |

Pinned positive candidate distinctions:

* `AbsoluteValue.eval_mvPolynomial_le`, `Mathlib/NumberTheory/Height/MvPolynomial.lean:189`: assumes a field K, finite ι and `p.IsHomogeneous N`; RHS is coefficient ℓ¹ sum times `(supᵢ v(xᵢ))^N`. Original P need not be homogeneous, and coefficient-cardinality/total-degree replacement loses the sharp product bound. It is an analogous law, not a more general version of this law.
* `IsNonarchimedean.eval_mvPolynomial_le`, same file:202: requires the nonarchimedean triangle inequality and homogeneity; real absolute value is archimedean. Not a replacement.
* `Polynomial.le_gaussNorm`, `Mathlib/RingTheory/Polynomial/GaussNorm.lean`: bounds one weighted coefficient by a weighted coefficient supremum. It is univariate and does not bound arbitrary archimedean evaluation. The p-adic Gauss result does not apply to the real absolute value.
* `MvPowerSeries.gaussNorm`: weighted coefficient supremum/ultrametric multiplication infrastructure, no rectangular archimedean evaluation majorant supplied.
* `AddMonoidAlgebra.liftNC`/`liftNCRingHom`: canonical evaluation algebra construction, without quantitative sum bound. `WithLp` Finsupp file supplies metrics, not this evaluation theorem.
* `MvPolynomial.eval₂_eq'`, `monomial_le_degreeOf`, `Finset.le_sum_of_subadditive`, `Finset.sum_le_sum_of_subset_of_nonneg`, `Finset.prod_univ_sum`: verified proof building blocks, but require monomial majorization and rectangular sum reasoning.

No `GeneralRingSeminorm` declaration exists by that spelling in the pin; the supported abstraction uses existing hom classes or `RingSeminorm`. The conclusion is a concrete missing API identified relative to the existing homogeneous bound: nonhomogeneous coordinate-degree evaluation with common coefficient bound and no box-cardinality loss. Search failure is not a mathematical absence theorem. No speculative `exact?` negative probe was run under the worker contract; actual generic-route proof and specialization are positive experiments.

## Phase 5.5 — statement shape

Normal form: original `eval (map ...)` and `eval₂` are equivalent by `eval_map`; prefer `p (eval₂ f x P)` with explicit coefficient hom f. The ordered-semiring output removes a further real-specific restriction. RingHom composition then behaves uniformly and callers can retain the original mapped spelling by a single normalization. RHS remains the rectangular majorant; no orthogonal equivalence lemma is proposed.

Syntactic generality: actually compiled `eval₂` abstract theorem, mapped integer-real specialization, and complete sole caller. Degree-bound and support-bound spellings were compared via `degreeOf_le_iff`; choose degree bounds because callers already supply them. Keep x explicit and r/B implicit. Do not replace all-coefficient hB by support-only hB unless also supplying B≥0.

Superfluous-argument audit: σ,Fintype,P,r,hP,B,hB,x each participates as explained in Phase4. Integer arithmetic and real points are unnecessary restrictions, not unused term arguments. The first generic helper proof had an auto-included unused Fintypeσ binder; root removed it, placing Fintype only on the evaluation theorem. The first HomClass/consumer batch then required a cast-normalization fix and parenthesized audit logInfo concatenation. Both rejected raw batches are preserved in [rejected attempts](../evidence/Roth.abs_eval_le/native-rejected-attempts.json). Only clean batches are accepted; the final ordered versions succeeded on their first native runs. Overall RESTATE-BEFORE-SHIP as `eval₂` and abstract size function; no invented hom-injectivity or norm-one hypothesis.

## Phase 6 — callers and composition experiments

Internal use count: **1**, one external-to-file module. Source and canonical audit preserve the actual private Lean name.

| Caller | Use and concrete migration |
|---|---|
| `_private.Roth.MainLemma.0.Roth.abs_eval_iterated_hasseDeriv_lt_aux`, declaration459, call466 | Replace `abs_eval_le` on the iterated Hasse derivative by specialization of the abstract `eval₂` theorem with Int.castRingHomℝ and real norm. Keep both degree monotonicity and nested coefficient bounds; collapse the constant-coordinate product as before. Complete caller proof is replayed with this exact replacement. |

Inline audit: no independent rectangular estimate elsewhere. `Main.abs_eval_lt_of_le_index:380` expands a Taylor polynomial, bounds derivative values and small displacements with weights; it is mathematically different and does not bypass this API. The theorem feeds `main_lemma` through the private iteration bound; not dead code. Explicit source references are distinguished from kernel/simp closure.

Attempt1 (existing homogeneous theorem): cannot supply IsHomogeneous for arbitrary P; homogenization plus degree conversion and coefficient accounting is new reasoning, and the old sup^N bound is not the requested coordinate product. NOT-COMPOSABLE in ≤3 existing calls.

Attempt2 (support expansion → triangle → box factorization): actual compiled generic proof performs coefficient-anchored product/power induction, support containment and geometric majorization. These NEW helpers plus declaration96's NEW generic bound are not existing mathlib blocks. The original specialization becomes short only after adding the new theorem. Its closing `simpa only` is representation transport, not evidence that current mathlib already closes the full target.

Attempt3 (private97 replay): root's previously compiled exact target-body replay confirms source proof soundness, but relies on the project private helper and was not treated as an existing mathlib composition. Overall **NOT-COMPOSABLE** from identified existing mathlib API within the ≤3-call criterion.

## Overview cross-file audit — duplication, missing API, junk

| Target vs candidate | Same statement? | Same proof? | Disposition |
|---|---|---|---|
| `Roth.abs_coeff_diag_le` | No: a coefficient after diagonal substitution, with support-cardinality factor | Both use triangle on monomial sums, but diagonal collisions differ from weighted evaluation | Keep distinct; one cannot replace the other. |
| private `Roth.sum_box_prod_pow_le_aux` | No: already-expanded box majorant only | Last stage of target proof | Keep proof helper private; generic geometric dependency can be upstream prerequisite. |
| `Roth.normOne_le_card_mul` | No: coefficient ℓ¹ sum versus common coefficient bound | Unweighted finite-sum estimate | Can support a coarser estimate, not the sharp rectangular value bound. |
| `Roth.abs_eval_iterated_hasseDeriv_lt_aux` | No: two Hasse derivatives and strict β estimate | Applies target, then numeric comparison | Genuine sole caller; does not duplicate target proof. |
| `Roth.abs_eval_lt_of_le_index` | No: Taylor small-displacement bound using index | Shares sum triangle, but different weight/vanishing premises | No unification of conclusions. |
| `AbsoluteValue.eval_mvPolynomial_le` | No: homogeneous/coefficient ℓ¹/sup bound | Expansion and triangle agree; support majorization differs | Share a future support-sum majorant helper, preserve distinct final bounds. |

Mathlib API audit: `eval₂` and existing size-hom classes are the richer common interface. Degree/support arithmetic already uses `monomial_le_degreeOf`; box representation can use existing Finset/Finsupp transport and need not be a new global definition. Missing API: a general weighted-support evaluation triangle lemma and its rectangular common-coefficient corollary; abstract coefficient-anchored multiplication/power estimates prevent accidental seminorm-unit assumptions. Junk verdict: **not junk**; source and kernel audit identify a live main-lemma dependency, and the theorem contains genuine rectangular summation reasoning rather than ≤3 existing calls. No new instances or simp tags are required for an inequality API.

## Phase 7 — verdict and actionable upstream plan

**YES-but-generalise-first — MODERN-IDIOM.** Replace ℤ-only coefficients/ℝ-only points and real abs by the verified `eval₂`/size-hom form over commutative semirings R,S and ordered commutative semiring T. The new mathematical API is the rectangular coefficient-to-value estimate for arbitrary nonhomogeneous multivariate polynomials. Existing homogeneous height estimates cannot absorb the same coordinate geometry without new work; the local source shows the utility of the sharper bound avoiding an extra cardinality factor.

Proposed primary theorem signature (verified strongest form):

```lean
theorem MvPolynomial.map_eval₂_le
    {σ R S T F : Type*} [Fintype σ] [CommSemiring R] [CommSemiring S]
    [CommSemiring T] [PartialOrder T] [IsOrderedRing T] [FunLike F S T]
    [ZeroHomClass F S T] [NonnegHomClass F S T]
    [SubadditiveHomClass F S T] [SubmultiplicativeHomClass F S T]
    (p : F) (f : R →+* S) (P : MvPolynomial σ R)
    {r : σ → ℕ} (hP : ∀ j, MvPolynomial.degreeOf j P ≤ r j) {B : T}
    (hB : ∀ d, p (f (P.coeff d)) ≤ B) (x : σ → S) :
    p (MvPolynomial.eval₂ f x P) ≤ B * ∏ j, (1 + p (x j)) ^ r j
```

The exact proof is in accepted execution evidence; this report contains no proof placeholder. Suggested upstream path: **`Mathlib/Analysis/Polynomial/MvPolynomial.lean`** (new file); this is an organizational proposal beside existing polynomial size/norm API, keeping its RingSeminorm/norm corollaries out of Algebra/MvPolynomial core. The most abstract HomClass proof could instead be placed in an ordered polynomial file at reviewer preference; no such placement decision is treated as a proof limitation. Proposed title **“feat(Analysis/Polynomial): bound multivariate evaluation by coefficients and coordinate degrees”**. Ship the generic geometric-sum estimate (accepted YES-but-generalise declaration96) in its ordered-semiring home as a prerequisite. Related accepted YES results `Roth.abs_coeff_hasseDeriv_le` and `Roth.normOne_hasseDeriv_le` may form a subsequent Hasse-coefficient estimate PR, not an excuse to couple this generic evaluation API to Roth/Hasse imports. Grouping is checked against the current progress ledger, not inferred from theorem names.

Pre-PR checklist:

- `/generalise Roth.abs_eval_le`: retain the verified semiring/hom-class floor; reconsider only genuinely needed structural assumptions and separate the support-sum lemma if useful.
- `/cleanup Roth/CoeffNorm.lean Roth.abs_eval_le`: apply full cleanup to proposed upstream theorem/helpers, settle names and placement, preserve comments, and run import/lint gates.
- Select Thomas Browning (RingSeminorm API commit `f932a30b0e`, 2026-08-26) and Yaël Dillies (MvPolynomial refactor `631b214f7c`, 2026-09-02; ordered big operators `a78f66ab84`, 2026-09-04) as relevant review candidates; [root Git receipt](../evidence/Roth.abs_eval_le/reviewer-git.json) records the scoped recent history. This identifies candidates, not an assigned or contacted reviewer.

The existing project destination remains `Roth/CoeffNorm.lean` until the upstream abstract theorem exists. At its sole explicit caller migrate mechanically as in Phase6; do not delete the estimate on the strength of a failed search or the new scratch theorem.

## Phase 8 — evidence status

The final package includes accepted exact Lean sources and complete native receipts, all17 source/pin checks, the canonical ordered293 audit, and a [portable read-only validator](../evidence/Roth.abs_eval_le/validate.py). Its [verification index](../evidence/Roth.abs_eval_le/verification.json) uses the exact executed ordered-source signature and actual clean receipts. [Current copy manifest](../evidence/Roth.abs_eval_le/copy-manifest.json) hashes and sizes every artifact. Root acceptance remains pending; the worker assessment is complete, with no unresolved verification item.
