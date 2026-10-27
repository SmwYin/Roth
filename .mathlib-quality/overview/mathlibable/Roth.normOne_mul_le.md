# Roth.normOne_mul_le — full mathlibable assessment

Canonical declaration **85/293**, `Roth/CoeffNorm.lean:96–102`. Verdict: **BORDERLINE-needs-human**. The read-only assessment is complete, with four accepted native receipts and one rejected attempt retained separately. The two future upstream questions below concern API design; verification has no unresolved items.

## Phase 0 — baseline

The shared `lake build` completed successfully (2467 jobs). All 17 source/pin hashes were freshly matched to its input manifest; production files remain unchanged. The public theorem contains no sorry. The complete declaring module and sole direct consumer were read: integer coefficient L1 estimates feed products, determinants, Hasse derivatives, diagonal specialization and evaluation.

Evidence: [baseline-build.txt](../evidence/Roth.normOne_mul_le/baseline-build.txt), [inputs.json](../evidence/Roth.normOne_mul_le/inputs.json), [input-hash-check.json](../evidence/Roth.normOne_mul_le/input-hash-check.json), [source-module.lean.txt](../evidence/Roth.normOne_mul_le/source-module.lean.txt), [canonical-order.json](../evidence/Roth.normOne_mul_le/canonical-order.json).

## Phase 1 — statement and proof

For integer multivariate polynomials P,Q, the sum of absolute values of all product coefficients is at most the product of their coefficient L1 sizes. In the convolution expansion each pair of input monomials produces a monomial with coefficient equal to the input coefficient product. The triangle inequality bounds cancellation when pairs land at the same exponent, and the resulting double sum factors.

Full native type (from theorem print):

```lean
∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ), Roth.normOne (P * Q) ≤ Roth.normOne P * Roth.normOne Q
```

σ indexes variables; P,Q are arbitrary polynomials; there are no additional hypotheses or typeclasses. The coefficient ring ℤ and target ℝ come from the fixed parent `Roth.normOne`. The print confirms use of project `normOne_sum_le` twice and `normOne_monomial`, plus existing `MvPolynomial.mul_def`, `Finset.sum_mul_sum`, `Finset.sum_le_sum`, scalar casts and `abs_mul`.

Evidence: [native-original-executed.lean.txt](../evidence/Roth.normOne_mul_le/native-original-executed.lean.txt), [native-original-success.json](../evidence/Roth.normOne_mul_le/native-original-success.json).

## Phase 2 — preliminary checks

**BIG** by the exact protocol: the module explicitly lists `Roth.normOne_mul_le` under Main results. Its elementary seven-line proof does not override that criterion. All literature channels were executed. Phase2b definition-only one-line/exemption test is **n/a: theorem**.

## Phase 3 — exhaustive literature

Every web request is exact, with response SHA256/UTF8 byte count, returned titles/URLs and concise original summary. No full returned bodies are archived. Returned URL query parameters are stripped; exact requests retained. Searches are evidence of what was found, not proof of absence.

| Channel | Actual query/locator | Result |
|---|---|---|
| General web concrete | `multivariate polynomial coefficient l1 norm submultiplicative product length` | Coefficient length context and convolution estimates. [web-0.json](../evidence/Roth.normOne_mul_le/web-0.json) |
| General web broad | `Young convolution inequality discrete l1 norm semigroup algebra` | Discrete Young inequality / convolution Banach algebra. [web-0.json](../evidence/Roth.normOne_mul_le/web-0.json) |
| General web aliases | `polynomial length sum absolute coefficients submultiplicative norm` | Same finite coefficient-size concept. [web-0.json](../evidence/Roth.normOne_mul_le/web-0.json) |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Optional tool absent; no channel substitution. |
| Local source | `clean.tex` Lemma3 proof, lines437–497 | Coefficient L1, triangle and monomial product rule. [local-literature.txt](../evidence/Roth.normOne_mul_le/local-literature.txt), [local-literature-source.json](../evidence/Roth.normOne_mul_le/local-literature-source.json), [rg-local-literature.json](../evidence/Roth.normOne_mul_le/rg-local-literature.json) |
| nLab | `site:ncatlab.org/nlab Banach algebra convolution l1` | Banach algebra page states product norm inequality and discrete convolution examples. [web-1.json](../evidence/Roth.normOne_mul_le/web-1.json) |
| nCatLab | `site:ncatlab.org/ncatlab convolution algebra norm`, then `site:ncatlab.org/ncatlab "convolution" "Banach"` | Search returns nLab resources, no distinct nCatLab coefficient-size theorem identified. This is a checked channel, not an absence claim. [web-2.json](../evidence/Roth.normOne_mul_le/web-2.json), [web-6.json](../evidence/Roth.normOne_mul_le/web-6.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial norm coefficients absolute value` | Field norm/trace via determinant, a different mathematical object; rejected as replacement. [web-3.json](../evidence/Roth.normOne_mul_le/web-3.json) |
| MathOverflow | `site:mathoverflow.net polynomial l1 coefficient norm multiplication` | Question426978 distinguishes coefficient L1 and supremum norm; context for false-generalization guard. [web-4.json](../evidence/Roth.normOne_mul_le/web-4.json) |
| Recent arXiv | `site:arxiv.org convolution Banach algebra l1 semigroup after:2021-10-27 before:2026-10-28` |2026 convolution-algebra model theory and2022 vector-valued Banach algebra articles; no novelty claim for elementary finite inequality. [web-5.json](../evidence/Roth.normOne_mul_le/web-5.json) |
| Supplementary primary teaching source | Hunter PDE notes Theorem1.23, Example1.25 | Young inequality with p=q=r=1, Fubini proof; continuous analogue, not alone proof of arbitrary monoid finite version. [web-6.json](../evidence/Roth.normOne_mul_le/web-6.json) |

Primary sources and locators: [Hunter, PDE Chapter1 §1.7](https://www.math.ucdavis.edu/~hunter/pdes/ch1.pdf), [González-Camus et al.2021, Theorem2.6](https://d-nb.info/1226684297/34), [Aghakoochaki–Rejali2022 abstract](https://arxiv.org/abs/2212.09106), [Berenstein–Gannon–Song2026 abstract](https://arxiv.org/abs/2608.04308). Supplementary concept sources: [nLab Banach algebra](https://ncatlab.org/nlab/show/Banach%2Balgebra), [nLab convolution algebra](https://ncatlab.org/nlab/show/convolution%2Balgebra), [MathOverflow426978](https://mathoverflow.net/questions/426978/comparing-the-truncated-ell1-norm-of-polynomial-coefficients-with-the-supr). The requests in web6 include page opens; the returned combined content exposes search results, so separate direct page-open success is not claimed.

Concept: coefficient L1 submultiplicativity, the finite discrete Young convolution bound. The broader standard viewpoint is convolution on monoid/group algebras with scalar absolute value or seminorm. Completeness, countability, finite variable count and a field are unnecessary for finite polynomial supports. This generalization is inferred from convolution mathematics and checked below in the expanded scalar representation.

## Phase 4a — every parameter/hypothesis

| Item | Current | Audit |
|---|---|---|
| σ | arbitrary Type* | Already arbitrary, including infinite/empty; no Fintype or DecidableEq hypothesis to drop. |
| P,Q | arbitrary MvPolynomial σ ℤ | No degree/support/coefficient bounds; both operands essential. |
| Coefficients | ℤ fixed by parent normOne | Expanded coefficient size can use CommSemiring; not a theorem-parameter weakening. |
| Target | ℝ fixed by parent normOne | Real size retained in compiled expansion; arbitrary ordered-target variant not claimed verified. |
| Explicit hypotheses | none | Nothing to drop inside the existing parent interface. |

## Phase 4b — verified generality

**MAXIMALLY GENERAL within the fixed parent interface**. A fresh Roth-free native experiment verifies an expanded representation with `[CommSemiring R]`, coefficient `size : R → ℝ`, `size 0 = 0`, subadditivity and **submultiplicativity** `size (a*b) ≤ size a * size b`. Equality/multiplicative absolute value is not required. No nonnegativity premise is used: the proof only sums inequalities, without multiplying inequalities. No negation or field structure is used. This is not asserted maximal among all monoid/ordered-target formulations.

```lean
variable {σ R : Type*} [CommSemiring R]
-- sizeSum size P := P.coeff.sum fun _ r ↦ size r
(size : R → ℝ) (hzero : size 0 = 0)
(hadd : ∀ a b, size (a + b) ≤ size a + size b)
(hmul : ∀ a b, size (a * b) ≤ size a * size b)
(P Q : MvPolynomial σ R) :
sizeSum size (P * Q) ≤ sizeSum size P * sizeSum size Q
```

`NormMulRaw.genericMul` and its integer `direct` specialization both compile. The support-union triangle, finite triangle and monomial bridge are **newly proved** helpers in this experiment; they do not become existing mathlib building blocks. The first raw attempt's unfold did not align `(P+Q).coeff` with Finsupp addition and was rejected, including recovered sorryAx. The accepted clean source uses an explicit `change`, not extra axioms or limit raises.

Evidence: [native-raw-executed.lean.txt](../evidence/Roth.normOne_mul_le/native-raw-executed.lean.txt), [native-raw-success.json](../evidence/Roth.normOne_mul_le/native-raw-success.json), [rejected-raw-executed.lean.txt](../evidence/Roth.normOne_mul_le/rejected-raw-executed.lean.txt), [rejected-raw-receipt.json](../evidence/Roth.normOne_mul_le/rejected-raw-receipt.json), [generality.json](../evidence/Roth.normOne_mul_le/generality.json).

## Phase 4c — nine modern-idiom rows

| # | Applies? | Finding |
|---|---|---|
| 1 | Yes | Coefficient size can be supplied through standard seminorm/absolute-value classes instead of ad hoc scalar assumptions; packaging remains design work. |
| 2 | No | Finite algebraic sums; filters and topology are unnecessary. |
| 3 | No | No constructed universal object in this inequality. |
| 4 | No | No set-with-closure predicate to bundle. |
| 5 | Yes | The fresh compiled expanded coefficient form uses CommSemiring, not integers or fields; only zero, subadditivity and submultiplicativity of size are needed. |
| 6 | No | No higher categorical content. |
| 7 | Yes | Exponent σ→₀ℕ is already arbitrary in σ. Additive monoid convolution is a broader standard candidate; its size inequality is not claimed compiled here. |
| 8 | Yes | After mul_def, proof is a double finite triangle bound and scalar product size. P,Q occur only through coefficients/support. GenericMul verifies scalar abstraction. |
| 9 | Pass | False-generalization guard: preserve coefficient L1 sum and convolution product. Pointwise multiplication, supremum/Gauss norms, field norm and integrated polynomial L1 are distinct quantities. |

Q8 concrete-via-abstract diagnostic: after the initial mul_def rewrite there are zero further literal `MvPolynomial` occurrences in the proof body; normOne remains on the rewrite line and through its helper names, reflecting coefficient-size aggregation. This signals real scalar/convolution abstraction, not a mysterious polynomial-specific bound. The fresh genericMul proves the scalar expansion; arbitrary AddMonoidAlgebra and a bundled RingSeminorm are proposed design endpoints, not tested weakenings. Modern idiom available; it would serve monoid algebras, scalar absolute values/seminorms, products and determinant estimates. Cost is not a verdict factor.

## Phase 4.5 — infrastructure risk

All six required rows are n/a for this theorem: typeclass diamonds, reducibility leak, noncanonical unfolding, instance priority collision, universe constraints, coercion ambiguity. Each rationale is recorded in [generality.json](../evidence/Roth.normOne_mul_le/generality.json). A future norm instance must undergo a separate risk assessment; this theorem adds no such instance.

## Phase 4.6 — all five proof-strategy rows

| # | Applies? | Finding |
|---|---|---|
| 1 | No | No epsilon-delta reasoning. |
| 2 | No | Element coefficients are appropriate; ideal inclusions do not express the estimate. |
| 3 | No | No sequences or limits. |
| 4 | No | Universal properties do not remove the norm estimate. |
| 5 | Yes | A generic coefficient-size convolution bound would replace the double support expansion; triangle/finite-size helpers in this experiment are newly proved, not existing mathlib. |

Strategy: **REFACTOR-RECOMMENDED for a future upstream package**: prove a shared coefficient-size convolution estimate once; this local theorem is its integer specialization. The present finite monomial expansion is mathematically sound and direct. A packaged norm law would shorten callers only after its representation bridge exists; importing generic norm_mul_le alone does not establish that bridge.

## Phase 5 — five actual formal methods, all three forms

The complete twelve raw formal calls are in [formal-search.json](../evidence/Roth.normOne_mul_le/formal-search.json), with each individual receipt beside it. No unavailable local index was assumed: current local search found the project target and previous scratch theorem; both are excluded as replacements.

| Method | Current form | Literature-standard | Abstract form |
|---|---|---|---|
| Lean-Finder | coefficient L1 multivariate product query: related Mahler/Gauss bounds | polynomial length/product query: related scalar coefficient estimates | finitely supported convolution query: MonoidAlgebra.mul_def/apply, no L1 law |
| Loogle | `MvPolynomial, _ * _ ≤ _ * _`: no hit | `‖_ * _‖ ≤ ‖_‖ * ‖_‖`: norm_mul_le and ring classes | `Finsupp.sum, _ ≤ _ * _`: AbsoluteValue.eval_mvPolynomial_le, an evaluation bound with different hypotheses |
| LeanSearch | coeff_mul/mul_def, norm-product hits | standard norm-product API | AddMonoidAlgebra.mul_apply and ring structures, not a compatible L1 norm |
| rg | [rg-current.json](../evidence/Roth.normOne_mul_le/rg-current.json), [rg-full-name.json](../evidence/Roth.normOne_mul_le/rg-full-name.json) | [rg-literature.json](../evidence/Roth.normOne_mul_le/rg-literature.json) | [rg-abstract.json](../evidence/Roth.normOne_mul_le/rg-abstract.json) |
| Local search | normOne_mul_le: project/scratch hits, excluded | norm_mul_le: generic norm law and unrelated FreeGroup | sum_mul: distributivity building blocks |

Positive pinned candidates are checked in exact native receipts: MvPolynomial.mul_def, Finset.sum_mul_sum, Finsupp.sum_single_index (raw); norm_mul_le and AddMonoidAlgebra.mul_def (infrastructure). Source archives and hashes: [mathlib-inputs.json](../evidence/Roth.normOne_mul_le/mathlib-inputs.json), [mathlib-monoid-algebra.lean.txt](../evidence/Roth.normOne_mul_le/mathlib-monoid-algebra.lean.txt), [mathlib-mvpolynomial.lean.txt](../evidence/Roth.normOne_mul_le/mathlib-mvpolynomial.lean.txt), [mathlib-norm-ring.lean.txt](../evidence/Roth.normOne_mul_le/mathlib-norm-ring.lean.txt). The source matches the abstract convolution mechanism but does not itself give the desired coefficient-size norm estimate.

The pinned Lp Finsupp module [mathlib-lp-finsupp.lean.txt](../evidence/Roth.normOne_mul_le/mathlib-lp-finsupp.lean.txt) equips WithLp finitely supported functions with Lp metrics. It does not furnish the tested raw MvPolynomial Norm/SeminormedRing instance or a compatible convolution law. In the persistent imported environment both `inferInstance : Norm (MvPolynomial σ ℤ)` and `inferInstance : SeminormedRing (MvPolynomial σ ℤ)` are guarded failures. This is evidence about this concrete environment, not global nonexistence of every possible L1 construction. `norm_mul_le` requires NonUnitalSeminormedRing; using it without proving that structure would be circular. Evidence: [native-infrastructure-executed.lean.txt](../evidence/Roth.normOne_mul_le/native-infrastructure-executed.lean.txt), [native-infrastructure-success.json](../evidence/Roth.normOne_mul_le/native-infrastructure-success.json).

## Phase 5.5 — three statement-shape checks

Normal form: **OK locally**, SHIP-AS-STATED for this fixed parent API. Coefficient support sum and Finsupp.sum are the same finite aggregation; norm notation should wait for a compatible structure, not a web hit with a similar name. Inequality has no equivalence-RHS simp orientation to choose.

Syntactic generality: P,Q explicit supports passing the theorem as a binary multiplicative bound in normOne_prod_le. Curried function / explicit coefficients would not ease that caller. Coefficient-semiring expansion is genuine mathematical generality, not a cosmetic restatement. Superfluous argument audit: σ determines exponent type; P,Q determine both factors; all are needed and no removable typeclasses/hypotheses occur.

## Phase 6.0 — callers and inline audit

**One named direct consumer, one occurrence**: `Roth.normOne_prod_le`, CoeffNorm108. No external-to-module explicit reference. Module docstring reference and theorem declaration are not counted as callers. The entire consumer proof was replayed with the full multiplication proof substituted for the binary-bound argument. It still uses project triangle/monomial witnesses, so this is local inlining, not a mathlib-only replacement certificate.

Fresh [rg-callers.json](../evidence/Roth.normOne_mul_le/rg-callers.json) and [rg-inline.json](../evidence/Roth.normOne_mul_le/rg-inline.json) audit all Roth source uses/rederivations. A native direct proof-value audit covers exact tracked canonical order, preserving private names via Lean.mkPrivateNameCore. It checks runtime **293 entries and 293 unique names**, and reports 293 present/values, with sole direct proof consumer Roth.normOne_prod_le. Validator independently compares full ordered name array against declaration-order.json, not just count. This is not transitive kernel/simp dependency closure.

Evidence: [callers.json](../evidence/Roth.normOne_mul_le/callers.json), [canonical-audit-array.lean.txt](../evidence/Roth.normOne_mul_le/canonical-audit-array.lean.txt), [native-consumers-executed.lean.txt](../evidence/Roth.normOne_mul_le/native-consumers-executed.lean.txt), [native-consumers-success.json](../evidence/Roth.normOne_mul_le/native-consumers-success.json).

## Phase 6 — actual composition experiments

1. Exact original/replay compiles using existing convolution expansion and scalar identities **plus project** normOne_sum_le and normOne_monomial. Their proofs are not counted as existing mathlib API.
2. Roth-free raw experiment with missing-target guard proves triangle, finite triangle and monomial bridge afresh, then genericMul. This is an actual full composition attempt with new mathematical helpers, not a <=3 existing-call term.
3. Sole complete caller replay verifies inlining is possible, but repeats the substantive binary estimate and retains other project witnesses.
4. Native generic norm route checks norm_mul_le signature and both missing raw norm/ring instances. An existing normed-ring theorem without the required structure is not an exact hit.

The exact fixed-parent result is **NOT-COMPOSABLE under the strict ≤3 existing mathlib-call gate on the evidence available**. This does not claim global absence from search. No closing simp with unfolded definitions is promoted to a NO certificate. There is **no Mode B parent re-aim override**: normOne's assessment was NO-composable, not NO-mathlib-has-it, and the triangle/finite bound were BORDERLINE. These parent outcomes are context only; this declaration's probes are independent.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human.** The result is standard and useful, with verified scalar-semiring generality. Its right shared home depends on whether coefficient L1 is exposed as a convolution Finsupp sum API or as a bundled seminorm/WithLp structure. A direct integer-polynomial submission would hard-code the project's unsettled norm representation; claiming norm_mul_le already replaces it omits the substantive bridge. This is a representation/API decision, not a cost-based downgrade or mathematical uncertainty.

1. Should the shared upstream API prove coefficient-size submultiplicativity for AddMonoidAlgebra over an arbitrary additive monoid, with MvPolynomial as a specialization?
2. Should coefficient L1 be packaged as a RingSeminorm/WithLp-compatible structure, or exposed as explicit Finsupp.sum bounds before introducing norm instances?

Retain the local theorem in `Roth/CoeffNorm.lean` while deciding the common API. If removed locally, use the full inlined multiplication proof in normOne_prod_le, as the accepted full replay verifies; that repetition is a reason to retain the helper. No standalone PR or accepted-YES grouping is proposed for a BORDERLINE declaration. Future convolution API should coordinate with the coefficient representation and additive triangle assessments, and should reuse existing algebraic convolution expansion and finite induction rather than duplicate them. These future questions require no interruption to complete the overview.

## Phase 8 — verification and handoff

[verification.json](../evidence/Roth.normOne_mul_le/verification.json) lists four accepted exact snippets/raw results and the rejected initial attempt separately. All accepted proof axiom prints use only propext, Classical.choice and Quot.sound; no errors, warnings, sorryAx, partial outputs or raised limits. [validate.py](../evidence/Roth.normOne_mul_le/validate.py) is portable and read-only and validates current manifest, source/pin hashes, all phases, all 5 methods/current-standard-abstract forms, exhaustive literature, source links and exact ordered canonical293 audit. [copy-manifest.json](../evidence/Roth.normOne_mul_le/copy-manifest.json) is authoritative; root acceptance is pending independent review. Production files and pins are unchanged.
