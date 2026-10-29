# Roth.abs_eval_lt_of_le_index — canonical281

Verdict: **BORDERLINE-needs-human**. The quantitative estimate is substantive and classically justified. Its current arithmetic/index spelling serves one Roth proof. Fresh generic proofs demonstrate reusable finite-expansion mathematics, but the public upstream interface (expansion versus weighted polynomial support/order) is a concrete design choice. This verdict is independent of adjacent declarations and does not depend on implementation cost.

## 0. Baseline and scope

The clean2467-job baseline is reused only after fresh equality of all17 tracked source/pin hashes. Root exclusively executed every native source and project local search. No production Lean, pins, imports or Git were changed by this worker. Main was read in full588 lines and LeanEval in full66 lines; both exact sources are archived. No new file-end build is scheduled at281 (next289).

[baseline-build.txt](../evidence/Roth.abs_eval_lt_of_le_index/baseline-build.txt); [inputs.json](../evidence/Roth.abs_eval_lt_of_le_index/inputs.json); [source-Main.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/source-Main.lean.txt); [source-LeanEval.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/source-LeanEval.lean.txt).

Original re-elaboration scope is the exact target and its exact private monomial-decay helper, in Taylor281Original with open Roth; only target name becomes replay. Original/replay types agree natively via Subsingleton.elim. Original loaded kernel type/value dependencies and axioms were inspected. Kernel body printer explicitly elides89054 characters: this is not a full body dump. The complete written source is preserved. The canonical array is generated directly from tracked declaration-order.json, exact293 ordered/private names; requested/unique/present/values all293, one direct body consumer and no direct type consumer.

[original-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/original-executed.lean.txt); [original-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/original-receipt.json); [canonical-consumers.json](../evidence/Roth.abs_eval_lt_of_le_index/canonical-consumers.json).

## 1. Statement and proof

For a polynomial of coordinate degree at most r, suppose its index at the diagonal center is at least c and every Hasse coefficient there has absolute value strictly below C. Approximation errors and denominator growth bound every surviving Taylor monomial by q₀^(−r₀cκ). The absolute evaluation is strictly less than the number of box monomials times C times that common decay.

The coefficients whose weight is below c vanish: a nonzero Hasse coefficient forces index≤weight. Taylor expansion gives a finite sum over box r. Each zero coefficient term is strictly bounded because hC at0 forces C>0 and the decay is positive. Each nonzero term uses strict coefficient inequality and a weak monomial bound; hence strictness does not require strictly better approximants. The box contains0 even when all degrees are0, so summing strict bounds is valid. Cardinality is ∏(rj+1).

There is no Q≠0 premise and none is needed. Degree values may vanish, including mixed zero coordinates; real division is totalized. hq yields q₀≥1, positivity for rpow, and hκ gives the required antitone-base exponent comparison. c and α are unrestricted reals. C is not separately assumed positive. The all-index coefficient premise can be restricted to the box.

Full native Lean type:

```lean
∀ {m : ℕ} [inst : NeZero m] {Q : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ},
  (∀ (j : Fin m), degreeOf j Q ≤ r j) →
    ∀ {α c : ℝ},
      c ≤ Roth.index Q (fun (x : Fin m) ↦ α) r →
        ∀ {h : Fin m → ℤ} {q : Fin m → ℕ},
          (∀ (j : Fin m), 0 < q j) →
            ∀ {κ : ℝ},
              0 ≤ κ →
                (∀ (j : Fin m), |α - ↑(h j) / ↑(q j)| ≤ 1 / ↑(q j) ^ κ) →
                  (∀ (j : Fin m), ↑(q 0) ^ (↑(r 0) / ↑(r j)) ≤ ↑(q j)) →
                    ∀ {C : ℝ},
                      (∀ (i : Fin m →₀ ℕ), |(eval fun (x : Fin m) ↦ α) ((hasseDeriv i) Q)| < C) →
                        |(eval fun (j : Fin m) ↦ ↑(h j) / ↑(q j)) Q| <
                          (∏ j : Fin m, (↑(r j) + 1)) * C * ↑(q 0) ^ (-↑(r 0) * c * κ)
```

## 2. Preliminary checks

SMALL under the skill classification: a supporting quantitative bound, not a person-named result or one of Main’s final named results. This is a narrative classification, not a claim of triviality. Definition-only one-line test: n/a theorem. Six infrastructure risk rows: n/a theorem, separately recorded; no instance, reducibility or coercion change is introduced.

[phase-checks.json](../evidence/Roth.abs_eval_lt_of_le_index/phase-checks.json).

## 3. Exhaustive literature

| Channel | Actual query / source | Outcome |
|---|---|---|
| web-specific | Roth theorem Taylor expansion index polynomial upper bound Hasse derivatives | Roth original reprint has exact mechanism; modern exposition gives vanishing/index context. |
| web-general | multivariate polynomial weighted vanishing order coefficient estimate polydisc Taylor | Nearby approximation/norm literature; no uniform named exact theorem identified. |
| web-alias | Roth auxiliary polynomial Taylor expansion inequality product degrees | Auxiliary polynomial terminology leads to same finite Taylor proof. |
| nlab | site:ncatlab.org/nlab Taylor polynomial vanishing order | Taylor theorem page covers arbitrary centers and multivariate Taylor, not this arithmetic weighted bound; direct XHTML open fails400 content type in batch3. |
| ncatlab | site:ncatlab.org/ncatlab polynomial Taylor weighted order | Actual distinct namespace queried; returned nLab/out-of-namespace material, no exact scoped hit. Followup batch4 also out-of-namespace. |
| stacks | site:stacks.math.columbia.edu Hasse derivatives Taylor polynomial | No supporting exact scoped hit in returned batch; followup Taylor derivatives in batch4 likewise no scoped match. No absence conclusion. |
| mathoverflow | site:mathoverflow.net Roth theorem Taylor index polynomial bound | Optimal Roth-type result discusses separate need for Roth lemma/nonvanishing; other posts concern broader approximation and analytic bounds rather than this estimate. |
| arxiv | site:arxiv.org Roth theorem Taylor polynomial index after:2021-10-29 before:2026-10-30 | Returned2607.05124 is additive-combinatorial Roth, not Diophantine Roth; rejected as a subject-name collision. More specific Diophantine/Roth/polynomial followup batch4 found no scoped supporting hit. |
| Local | clean.tex §7 lines1650–1699, §4 lines501ff | Exact proof mechanism and strictness note; owned source excerpt archived. |
| Optional ask_chatgpt_math | unavailable tool | Justified optional omission; all named channels still attempted. |

At least three distinct general queries actually ran. The distinct nCatLab namespace was queried as site:ncatlab.org/ncatlab. Recent arXiv query uses after:2021-10-29 before:2026-10-30; additive-combinatorial Roth was rejected as a name collision, not used as Diophantine evidence. Returned nLab results do not count as nCatLab namespace matches. Stacks gave no supporting scoped result; no theorem absence is inferred. Direct nLab open failed on unsupported XHTML; search extraction supplied only context. Exact requests, returned-response SHA256/UTF8 bytes/status and clean returned URLs are archived, never full third-party bodies.

[literature.json](../evidence/Roth.abs_eval_lt_of_le_index/literature.json); [primary-detail.json](../evidence/Roth.abs_eval_lt_of_le_index/primary-detail.json); [literature-local.json](../evidence/Roth.abs_eval_lt_of_le_index/literature-local.json); [local-excerpt.tex.txt](../evidence/Roth.abs_eval_lt_of_le_index/local-excerpt.tex.txt); [web-batch0.json](../evidence/Roth.abs_eval_lt_of_le_index/web-batch0.json), [web-batch1.json](../evidence/Roth.abs_eval_lt_of_le_index/web-batch1.json), [web-batch2.json](../evidence/Roth.abs_eval_lt_of_le_index/web-batch2.json), [web-batch3.json](../evidence/Roth.abs_eval_lt_of_le_index/web-batch3.json), [web-batch4.json](../evidence/Roth.abs_eval_lt_of_le_index/web-batch4.json).

[K. F. Roth, Rational approximations to algebraic numbers (reprint)](https://www.maths.ed.ac.uk/~jmf/MaOv/fieldsmedals.pdf) — Roth reprint pp60–61, Taylor expansion properties A/B and inequality(4). Small Taylor coefficients and vanishing of low-weight monomials yield the evaluation upper bound. Distinct nonvanishing condition is needed only when comparing the integer lower bound.

[Aleksa Milojević, An elementary approach to Roth’s theorem](https://aleksa-milojevic.github.io/expository/roth.pdf) — §2 pp2–3 proof sketch; §3 definition of index; §6 p12 (PDF page11), Taylor upper bound. Weighted vanishing order compensates for unbalanced multidegrees; closeness of approximants gives an upper bound to combine with a nonzero rational evaluation lower bound.

[Min Ru, Roth’s Theorem](https://www.math.uh.edu/~minru/fields/roth.pdf) — Step2 pp5ff, expansion around diagonal point. Taylor expansion relates high index at the algebraic point to small values at rational tuples; this is contextual evidence, not a mathlib API replacement.

[nLab, Taylor’s theorem](https://ncatlab.org/nlab/show/Taylor%27s%2Btheorem) — Preliminary definitions and Statements; search extraction available, direct XHTML open fails. Taylor polynomials use an arbitrary center and can be multivariate. Analytic remainder estimates impose differentiability/regularity rather than exact polynomial support vanishing.

[Optimal Roth-type result in diophantine approximation](https://mathoverflow.net/questions/332190/optimal-roth-type-result-in-diophantine-approximation) — comments on Roth lemma in polynomial method. Separates construction of high-order vanishing at one point from nonvanishing at another; no claimed new generality of the upper estimate.

[A Roth theorem in R² and a related ergodic theorem](https://arxiv.org/abs/2607.05124) — abstract,2026-07-06. Additive-combinatorial polynomial pattern result; rejected as unrelated to algebraic-number rational approximation.

Literature summary: finite weighted Taylor estimates are classical; arbitrary centers and multivariate Taylor are standard, and coefficient/radius inequalities extend beyond number-theoretic rational tuples. The literature does not select one unique mathlib API packaging. The local theorem’s strict coefficient bound is sufficient even with weak coordinate errors.

## 4. Generality, modern idiom and strategy

| Parameter / premise | Assessment | Verified evidence |
|---|---|---|
| m, NeZero m, Fin m | generalize | Finite σ possibly empty in own generic/cost_bound; NeZero required only by original distinguished coordinate0. |
| Q real coefficients | generalize | NormedField and NormedCommRing + NormOneClass shifted polynomial expansion tested; project Hasse/index remains real-specific, not falsely claimed ported. |
| r natural coordinate degrees, hd | retain box, abstract expansion also possible | Natural exponents/degree upper bounds give finite box and cardinal product. Arbitrary s.Nonempty works for expansion form; no positive degree condition. |
| α common center | generalize | Arbitrary a:σ→ℝ or K in generic proof. |
| c, hidx | semantic cost lower bound | Nonzero expansion coefficients imply c≤Σ μj*dj; original recovery rescales c to r0*c*κ and uses index_le_weight. No Q≠0. |
| h integral numerator | remove representation | Arbitrary x:σ→ℝ/K; exact h/q evaluation recovered. |
| q positive natural, hq | abstract to b≥1 and radii | b≥1 supplies positive base and exponent monotonicity; coordinate radius b^(-μj) need only satisfy actual error bound. |
| κ nonnegative, happ, hqr | replace by semantic cost/radius bounds | Original bridge proven using Real.rpow_le_rpow_of_nonpos; μ arbitrary real in generic, no positivity assumption needed beyond actual error bound. |
| C and all-index hC | localize | Only d∈box r needed; box nonempty by0; C>0 derived rather than hypothesized. |

Verified generality verdict: STRICTLY NARROWER. Own generic expansion has arbitrary finite σ (empty allowed), center a, evaluation x, real costs μ and b≥1. Each positive radius b^(−μj) controls the coordinate error. Surviving coefficients satisfy c≤Σμj*dj. μ need not be nonnegative: the proof requires only the actual radius bound and cost threshold. Coefficients need only be bounded on a nonempty finite expansion. Arbitrary s may not be empty for a strict cardinality bound; the zero polynomial is allowed because a box still contains0.

Mathlib-only real generic signature:

```lean
lemma expansion_bound {σ : Type*} [Fintype σ] {s : Finset (σ →₀ ℕ)} (hs : s.Nonempty)
    {a x μ : σ → ℝ} {A : (σ →₀ ℕ) → ℝ} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ s, |A d| < C) (hx : ∀ j, |x j - a j| ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ s, A d ≠ 0 → c ≤ ∑ j, μ j * d j) :
    |eval x (∑ d ∈ s, MvPolynomial.C (A d) * ∏ j, (X j - MvPolynomial.C (a j)) ^ d j)|
      < (s.card : ℝ) * C * b ^ (-c)
```

Full project polynomial/Hasse version (new proof using the imported project Taylor theorem):

```lean
lemma cost_bound {σ : Type*} [Fintype σ] [DecidableEq σ]
    {Q : MvPolynomial σ ℝ} {r : σ → ℕ} (hd : ∀ j, degreeOf j Q ≤ r j)
    {a x μ : σ → ℝ} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ box r, |eval a (hasseDeriv d Q)| < C)
    (hx : ∀ j, |x j - a j| ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ box r, eval a (hasseDeriv d Q) ≠ 0 → c ≤ ∑ j, μ j * d j) :
    |eval x Q| < (∏ j, ((r j : ℝ) + 1)) * C * b ^ (-c)
```

The exact original is recovered by b=q₀, μj=r₀κ/rj and threshold r₀cκ. The radius bridge uses hqr and nonpositive exponent −κ. Multiplying hidx≤weight by nonnegative r₀κ and distributing across the finite sum gives the semantic cost premise. Ring normalization preserves totalized zero division; no cancellation by rj occurs. The full coefficient hypothesis is restricted by fun d _ ↦ hC d. Thus this is a real mathematical weakening, not replacing integers by differently named constants.

[generic-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/generic-executed.lean.txt); [generic01-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/generic01-receipt.json); [project2-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/project2-executed.lean.txt); [project02-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/project02-receipt.json).

A separate mathlib-only normed-field expansion and a normed-commutative-ring plus NormOneClass version test coefficient generality. The ring proof uses norm_prod_le, norm_pow_le and norm_mul_le, rather than multiplicativity of the norm; NormOneClass handles empty products and zeroth powers. Neither version claims that the project’s real Hasse/index API has already been ported. No coefficient completeness, division or order is necessary for the finite expansion bound.

Normed-ring proposed signature:

```lean
lemma expansion_bound {σ K : Type*} [Fintype σ] [NormedCommRing K] [NormOneClass K]
    {s : Finset (σ →₀ ℕ)} (hs : s.Nonempty)
    {a x : σ → K} {μ : σ → ℝ} {A : (σ →₀ ℕ) → K} {b c C : ℝ} (hb : 1 ≤ b)
    (hC : ∀ d ∈ s, ‖A d‖ < C) (hx : ∀ j, ‖x j - a j‖ ≤ b ^ (-μ j))
    (hvanish : ∀ d ∈ s, A d ≠ 0 → c ≤ ∑ j, μ j * d j) :
    ‖eval x (∑ d ∈ s, MvPolynomial.C (A d) * ∏ j, (X j - MvPolynomial.C (a j)) ^ d j)‖
      < (s.card : ℝ) * C * b ^ (-c)
```

[normed2-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/normed2-executed.lean.txt); [normed02-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/normed02-receipt.json); [normedring-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/normedring-executed.lean.txt); [normedring01-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/normedring01-receipt.json).

Modern-idiom checklist:

| Row | Answer | Concrete consequence |
|---|---|---|
| 1 typeclass preambles | no | Original is real-valued; finite indexing already uses Fintype. No new class warranted for a one-off vanishing predicate. |
| 2 filters/nets | no | Exact finite polynomial estimate, no convergence or topology used. |
| 3 universal property | no | Existing MvPolynomial evaluation/aeval already supply universal properties; the missing step is quantitative. |
| 4 bundled substructure | no | A finite support restriction could be a submodule but adds no useful algebraic operation to this numeric bound. |
| 5 hierarchy | yes | Own normed field and normed commutative ring plus NormOneClass expansion proofs; no coefficient division, completeness or ordered coefficients needed. Real b,c,C,μ control the scalar estimates. |
| 6 higher categories | no | No categorical construction or categorical coherence law here. |
| 7 concrete indices | yes | Arbitrary finite variable type including empty, arbitrary real center/evaluation vectors; integer numerator and natural denominator become a downstream radius bridge. |
| 8 concrete-via-abstract | yes | After eval_eq_sum_box original index occurs once via hidx.trans(index_le_weight h0); arithmetic error only supplies a monomial bound. Tested finite shifted expansion and coordinate costs abstract these properties, with actual exact original recovery. |
| 9 false-generalization guard | no false generalization | Original recovery retains exact original statement, zero polynomial and mixed zero degrees; no ENat zero-polynomial convention substitution or unsupported equivalence of index definitions. Nonempty expansion and strict hC preserved. |

Concrete-via-abstract diagnostic: after eval_eq_sum_box the index is used on one line only, through index_le_weight for nonzero coefficient. The repeated h/q syntax supplies only radius inequalities; the rest is finite sum/product arithmetic. Own generic proof and exact recovery compile. No claim is made that this own newly proved helper already exists in mathlib. [concrete-diagnostic.json](../evidence/Roth.abs_eval_lt_of_le_index/concrete-diagnostic.json).

Proof-strategy checklist:

| Row | Assessment |
|---|---|
| 1 epsilon-delta vs filters | n/a finite algebraic inequality |
| 2 elementwise vs substructure | elementwise finite sum/product is appropriate; support lower bound could later be packaged as a submodule but is not needed |
| 3 sequences vs nets | n/a no limits |
| 4 construction vs universal property | existing eval and polynomial sums retained; no new object construction |
| 5 missing helpers | yes: own shifted-expansion strict decay and monomial radius/cost estimate; project multivariate Taylor/Hasse/index ingredients are not mathlib primitives |

Strategy verdict: REFACTOR-RECOMMENDED for upstream review: finite expansion norm estimate, monomial cost decay, then Taylor/index/rational-growth corollaries. This changes mathematical organization and supports arbitrary points/coefficient rings; it is not a cosmetic restatement. Local proof is mathematically sound. Cost does not select the verdict.

Infrastructure risk table:

| Risk | Assessment |
|---|---|
| typeclass diamond | n/a — theorem introduces no such infrastructure. |
| reducibility leak | n/a — theorem introduces no such infrastructure. |
| noncanonical unfolding | n/a — theorem introduces no such infrastructure. |
| instance priority collision | n/a — theorem introduces no such infrastructure. |
| universe polymorphism | n/a — theorem introduces no such infrastructure. |
| coercion ambiguity | n/a — theorem introduces no such infrastructure. |

## 5. Formal search, statement shape and composition

All15 original cells (three forms × Finder, Loogle, LeanSearch, pinned rg and root-executed local search) were actually attempted. A supplemental five-method normed-ring form was also executed (Finder/Search/Loogle, pinned rg, root local); Loogle’s initial unqualified norm name failed and a quoted-name retry returned no items. Finder/Search returned only univariate Gauss/Mahler or analytic-series bounds, not this exact weighted multivariate estimate. Local normed index also errored with10 hits, not a healthy exhaustive result. Current form queries use the exact target/evaluation/index, standard form queries multivariate Taylor/weighted vanishing, abstract form queries finite strict sums/cost/rpow. Current Loogle initially rejected a syntax pattern; a corrected MvPolynomial.eval, LT.lt query returned unrelated finite-field evaluation theorems and is separately preserved. Standard Loogle Real.rpow,_≤_ returned no item; abstract finite sum query returned only general operators. Local index remained error/warming after fresh retries; those hits are leads only, not exhaustive absence evidence. Remote revisions can differ from the pin.

[formal-search-matrix.json](../evidence/Roth.abs_eval_lt_of_le_index/formal-search-matrix.json).

Pinned positive candidates: Finset.abs_sum_le_sum_abs, Finset.sum_lt_sum_of_nonempty, Real.rpow_mul, Real.rpow_sum_of_pos, Real.rpow_le_rpow_of_nonpos; Polynomial.taylor_coeff is univariate, and MvPowerSeries.weightedOrder_le is natural-weight ENat order without a numeric evaluation bound. Native #checks preserve signatures. Existing MvPolynomial algebra evaluation APIs normalize an explicit expansion but do not supply Hasse coefficients, vanishing/order transport or the cost estimate. A supplemental normed source search first hit a nonexistent path and was retried on actual directories; both receipts retained. Polynomial.supNorm is a univariate coefficient norm, not an exact replacement.

[formal-normed-rg-failed.json](../evidence/Roth.abs_eval_lt_of_le_index/formal-normed-rg-failed.json); [formal-normed-rg.json](../evidence/Roth.abs_eval_lt_of_le_index/formal-normed-rg.json); [mathlib-source-0.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/mathlib-source-0.lean.txt); [mathlib-source-1.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/mathlib-source-1.lean.txt); [mathlib-source-2.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/mathlib-source-2.lean.txt).

| Statement-shape check | Verdict | Detail |
|---|---|---|
| normal form | RESTATE | Compare absolute-value real corollary, norm of a shifted finite expansion, and coefficient/support cost formulation. Use norm for general coefficients and low-cost vanishing predicate, keep original index corollary downstream. No known existing canonical exact weighted upper estimate; not an iff theorem so RHS convention irrelevant. |
| syntactic generality | RESTATE | Verified boxed coefficient premise ∀d∈box r instead of all multiindices, arbitrary center/evaluation/cost, finite σ. Actual sole caller supplies box restriction by fun d _ ↦ hC d; original type preserved. |
| superfluous arguments | localize | NeZero m needed only to write q0/r0; Fin m and rational/integer presentations removed in generic. hd needed for box expansion; hidx used for surviving weights; hq for positive denominators/base at least1; hκ for exponent sign; hκ for exponent monotonicity; happ/hqr for radius bridge; hC strict on nonempty box ensures C>0. No nonzero Q/positive r required. |

Shape verdict: RESTATE-BEFORE-SHIP for a generic upstream interface. Original remains valid unchanged. No unused premise is silently deleted: hidx becomes surviving-cost restriction, and hC localizes to the box. Strictness and the nonempty expansion cannot simply be dropped: the empty sum would demand0<0, and a coefficient attaining its weak bound can attain the final bound. Native edge examples and zero-polynomial specialization are preserved.

[shape2-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/shape2-executed.lean.txt); [shape02-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/shape02-receipt.json).

Composition attempt1: triangle inequality followed by Finset.sum_lt_sum_of_nonempty. This still requires a nonempty box and every strict term estimate, including handling zero coefficients, positivity of C and decay, index→weight and monomial decay. Attempt2: use Polynomial.taylor_coeff or weightedOrder_le. These do not give the required multivariate finite expansion and quantitative coefficient/radius bound. Attempt3: native simp-only closure fails as expected; own generic and project recovery close only after new proofs. There is no verified ≤3 existing-mathlib-call composition. NOT-COMPOSABLE on tested candidates; a failed search or negative simp probe is not a global proof of absence. The generic proof’s simplification of an already written expansion is only normalization, not a claimed replacement theorem.

## 6. Full actual callers and inlining

| Actual caller | Use | Verification |
|---|---|---|
| Roth/Main.lean453–478, private one_lt_roth_eval_bound_aux | One invocation at477, multiply Taylor upper estimate by positive denominator product and combine with integer lower bound | Complete original signature and body tested with target proof locally inlined and with new generic recovery. Both target-free in direct kernel value audit; exact original private type agreement. |

Internal use count excluding declaring file per skill:0; same-file actual proof count:1. Documentary reference is Main39; declaration is380. Both rg --no-ignore and git grep cover tracked production inventory. No external-to-file source call or duplicate full inline estimate was found. This is not dead code: private caller feeds roth_of_isIntegral, then roth, roth_rat and LeanEval thueSiegelRoth. Transitive usefulness does not by itself establish a public generic API. Target is not simp-tagged; source lexical/body/type and exact canonical direct kernel scopes are distinct from arbitrary simp/transitive closure.

[source-search.json](../evidence/Roth.abs_eval_lt_of_le_index/source-search.json); [tracked-source-search.json](../evidence/Roth.abs_eval_lt_of_le_index/tracked-source-search.json); [inline-search.json](../evidence/Roth.abs_eval_lt_of_le_index/inline-search.json); [callers.json](../evidence/Roth.abs_eval_lt_of_le_index/callers.json); [callers2-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/callers2-executed.lean.txt); [callers02-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/callers02-receipt.json).

Additionally full Main replay removes only the target declaration and its now orphaned docstring, changes outer namespace to Taylor281Full/open Roth, and replaces the sole invocation with a locally stated exact target proof. All other declarations and full caller bodies remain. The exact private monomial helper is part of that source. Full roth_rat re-elaborates with standard axioms. This is stronger than a chopped caller prefix; no desired conclusion is supplied as a premise.

[fullmain2-executed.lean.txt](../evidence/Roth.abs_eval_lt_of_le_index/fullmain2-executed.lean.txt); [fullmain02-receipt.json](../evidence/Roth.abs_eval_lt_of_le_index/fullmain02-receipt.json).

## 7. Verdict and actionable future design

BORDERLINE-needs-human is an upstream packaging judgment, with all assessment phases and verification finished. It is not a permission request or unfinished proof. The local theorem is a proper quantitative upper estimate, distinct from basic coefficient triangle bounds and the integer denominator lower estimate. The searches identify only ingredients. The verified generic normed-ring theorem demonstrates reusability but leaves a meaningful choice between an explicit finite expansion API and a weighted polynomial support/order API. The latter would also organize multivariate translation/Hasse theory; that is not an already existing replacement. Original arithmetic corollary can remain project-local while generic design is settled.

1. Should a strict finite shifted-expansion estimate with coordinate cost decay be named in mathlib, or remain a local lemma of a future Roth proof?
2. If upstreamed, should the public interface use a finite expansion with a nonzero-coefficient cost predicate, or a weighted support/order API with an explicit translation bridge?
3. Should the multivariate Taylor/index corollary and the rational denominator growth bridge remain in the Roth development while only the normed-ring expansion core enters general polynomial analysis?

Alternative local destination: Roth/Main.lean or future Roth/TaylorBounds.lean. A possible future generic home is a new Mathlib/Analysis/MvPolynomial/Bounds.lean; import layering is provisional, since foundational MvPolynomial/Eval should not acquire all analytic real-power dependencies. No upstream PR/title/group/reviewer commitment is being made for a BORDERLINE verdict. Relevant pinned file-history leads (Yaël Dillies and Aaron Liu for MvPolynomial/Eval) are archived without inferring reviewer availability. No adjacent verdict or parent theorem usefulness was inherited.

[reviewer-commits.json](../evidence/Roth.abs_eval_lt_of_le_index/reviewer-commits.json); [progress-snapshot.json](../evidence/Roth.abs_eval_lt_of_le_index/progress-snapshot.json).

## 8. Evidence and limits

Accepted native proofs use default limits, no sorry/admit/new axiom/unsafe/native_decide and only propext, Classical.choice, Quot.sound. All actual failures/warnings and preparation-only attempts are separately accounted. Sources executed with warning diagnostics remain immutable and are not accepted gates. Root executed every native and saved complete raw request/result/timing receipts. The only kernel printer truncation is disclosed above; complete written proofs and native full type remain. All18 isolated and9 disk imports stay fixed and SHA-bound in the validator; mathlib-only sources guard missing project target. Current copy manifest, input hashes, exact canonical array, both portable layouts and secret scan are checked by the read-only validator.

[verification.json](../evidence/Roth.abs_eval_lt_of_le_index/verification.json); [prefix-controls.json](../evidence/Roth.abs_eval_lt_of_le_index/prefix-controls.json); [validate.py](../evidence/Roth.abs_eval_lt_of_le_index/validate.py); [copy-manifest.json](../evidence/Roth.abs_eval_lt_of_le_index/copy-manifest.json); [secret-scan.json](../evidence/Roth.abs_eval_lt_of_le_index/secret-scan.json).
