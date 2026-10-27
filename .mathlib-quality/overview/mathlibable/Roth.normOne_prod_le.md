# Roth.normOne_prod_le — full mathlibable assessment

Canonical **86/293**, `Roth/CoeffNorm.lean:105–108`. **BORDERLINE-needs-human**. All assessment phases and four accepted native sets are complete; one rejected raw attempt is retained. The future questions concern upstream API design; there are no unresolved verification items.

## Phase 0 — baseline

The shared build succeeded (2467 jobs). All 17 current source/pin hashes freshly match its manifest. The public theorem resolves without sorry. The entire coefficient-norm module and complete sole consumer were read. Its L1 estimates feed determinant bounds, Hasse derivatives, diagonal substitution and evaluation. No production files or pins changed.

Evidence: [baseline-build.txt](../evidence/Roth.normOne_prod_le/baseline-build.txt), [inputs.json](../evidence/Roth.normOne_prod_le/inputs.json), [input-hash-check.json](../evidence/Roth.normOne_prod_le/input-hash-check.json), [source-module.lean.txt](../evidence/Roth.normOne_prod_le/source-module.lean.txt), [canonical-order.json](../evidence/Roth.normOne_prod_le/canonical-order.json).

## Phase 1 — mathematics and full native type

For any finite family of integer multivariate polynomials, the sum of absolute values of coefficients in their product is at most the product of the corresponding coefficient sums. For an empty family the polynomial product is one and both sizes are one. For insertion, binary submultiplicativity and nonnegativity propagate the inductive bound.

```lean
∀ {σ : Type u_1} {ι : Type u_2} (s : Finset ι) (f : ι → MvPolynomial σ ℤ), Roth.normOne (∏ i ∈ s, f i) ≤ ∏ i ∈ s, Roth.normOne (f i)
```

σ indexes variables and ι the family. s is an arbitrary Finset and f any family; no Fintype, DecidableEq or nonempty hypothesis appears. Integer coefficients and real sizes belong to the fixed parent normOne. The original proof delegates all induction to `Finset.le_prod_of_submultiplicative_of_nonneg`, with project witnesses `normOne_nonneg`, `normOne_monomial` at exponent0/coefficient1, and `normOne_mul_le`.

Evidence: [native-original-executed.lean.txt](../evidence/Roth.normOne_prod_le/native-original-executed.lean.txt), [native-original-success.json](../evidence/Roth.normOne_prod_le/native-original-success.json).

## Phase 2 — preliminary checks

**SMALL**: auxiliary finite-product extension, not named after a person, no new structure, and not itself named under module Main results (binary multiplication and determinant estimates are listed there). Definition-only one-line/exemption test: **n/a: theorem**. Exhaustive literature remains mandatory and was performed.

## Phase 3 — exhaustive literature

All actual requests are archived exactly with returned-response SHA256, UTF8 bytes, status and concise original summaries/locators. Full returned web bodies are not archived. Returned URL queries are removed; no credentials persisted. Queries with irrelevant hits are not treated as proof of absence.

| Channel | Exact query or locator | Result |
|---|---|---|
| General concrete | `polynomial length sum absolute coefficients finite product submultiplicative norm` | Coefficient-length context; unrelated finite-group word length rejected. [web-0.json](../evidence/Roth.normOne_prod_le/web-0.json) |
| General broad | `nonnegative submultiplicative function monoid finite product inequality` | Generic monoid finite-product viewpoint. [web-0.json](../evidence/Roth.normOne_prod_le/web-0.json) |
| General aliases | `Young inequality l1 convolution Banach algebra repeated product` | L1 convolution algebra inequality. [web-0.json](../evidence/Roth.normOne_prod_le/web-0.json) |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Optional external channel unavailable. |
| Local references | clean.tex Lemma3 proof lines437–497 | Coefficient sum, monomial product and determinant products. [local-literature.txt](../evidence/Roth.normOne_prod_le/local-literature.txt), [local-literature-source.json](../evidence/Roth.normOne_prod_le/local-literature-source.json), [rg-local-literature.json](../evidence/Roth.normOne_prod_le/rg-local-literature.json) |
| nLab | `site:ncatlab.org/nlab Banach algebra submultiplicative norm convolution` | Banach algebra norm inequality, unit bound and finite cyclic l1 convolution example. [web-1.json](../evidence/Roth.normOne_prod_le/web-1.json) |
| nCatLab | `site:ncatlab.org/ncatlab "submultiplicative" "norm"` | Returned nLab pages/matrix norm notes; no distinct nCatLab theorem identified. [web-2.json](../evidence/Roth.normOne_prod_le/web-2.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial coefficients norm product` | Trace/norm determinant construction, a different norm. [web-3.json](../evidence/Roth.normOne_prod_le/web-3.json) |
| MathOverflow | `site:mathoverflow.net polynomial coefficient l1 norm product` | Coefficient l1 versus value/sup norm discussion; context only. [web-4.json](../evidence/Roth.normOne_prod_le/web-4.json) |
| Recent arXiv | `site:arxiv.org l1 convolution Banach algebra after:2021-10-27 before:2026-10-28` | 2026 convolution-algebra model theory;2022 vector-valued Banach algebras. [web-5.json](../evidence/Roth.normOne_prod_le/web-5.json) |
| Supplementary direct primary opens | Lerner PDF,2022 arXiv abstract; nLab attempted | Primary PDF and arXiv opened; nLab direct fetch failed400 unsupported XHTML. [web-6.json](../evidence/Roth.normOne_prod_le/web-6.json) |

Primary mathematical source: [Lerner, Elements of Graduate Analysis, §2.1 Proposition2.1.1, p37](https://webusers.imj-prg.fr/~nicolas.lerner/m2intro.pdf), which gives L1 submultiplicativity for convolution. Its actual document date is2014; search crawl dates do not establish publication dates. Recent context: [Aghakoochaki–Rejali2022, abstract](https://arxiv.org/abs/2212.09106), [Berenstein–Gannon–Song2026, abstract](https://arxiv.org/abs/2608.04308). Supplementary standard definitions: [nLab Banach algebra](https://ncatlab.org/nlab/show/Banach%2Balgebra). Norm distinctions: [MathOverflow426978](https://mathoverflow.net/questions/426978/comparing-the-truncated-ell1-norm-of-polynomial-coefficients-with-the-supr); unrelated algebraic norm: [Stacks0BIE](https://stacks.math.columbia.edu/tag/0BIE).

Concept: finite iteration of coefficient L1 submultiplicativity / discrete Young inequality. The standard abstract formulation is a nonnegative submultiplicative function on a monoid, with its unit at most one, bounding finite products. Completeness, finite-dimensionality and a field are unnecessary. Finset products use a commutative source; ordered list products could weaken commutativity but are a different interface, not a compiled claim here. The passage from continuous convolution literature to finite monoid algebra is an inference checked by the raw experiment below.

## Phase 4a — parameter audit

| Item | Current role | Audit |
|---|---|---|
| σ | arbitrary variable type | Already arbitrary, including empty/infinite. |
| ι | arbitrary index type | Already arbitrary; only s is finite. |
| s | any Finset ι | Empty allowed and requires unit bound. |
| f | arbitrary family | No coefficient, support or degree restrictions; essential operand. |
| ℤ / ℝ | parent normOne representation | Not hypotheses of this theorem. Expanded scalar form checked separately. |
| Explicit hypotheses | none | No theorem assumption can be dropped. |

## Phase 4b — verified generality

**MAXIMALLY GENERAL within the fixed parent interface**. No parameter weakening is available there. The fresh Roth-free raw source proves an expanded coefficient-size form with `[CommSemiring R]`, size:R→ℝ, size0=0, subadditivity, submultiplicativity, nonnegative size and size1≤1. This is a real representation expansion, not a silent weakening of normOne. `NormProdRaw.genericProd` and integer `directProd` compile.

The binary convolution proof needs no nonnegativity premise because it only sums inequalities. Finite multiplication of inequalities uses nonnegative intermediate sizes, so the tested genericProd retains it; a weaker size-specific condition is not claimed impossible. The raw triangle, finite triangle, monomial and binary convolution bridges are **newly proved** helpers and do not count as existing mathlib replacements. The rejected first attempt referred to nonexistent `MvPolynomial.monomial_zero_one` and recovered sorryAx. The clean accepted unit bound uses monomialSize at exponent0/coefficient1 and transitivity with size1≤1.

The separate `abstractProd` is verified for arbitrary `[CommMonoid M]` and a nonnegative submultiplicative p:M→ℝ with p1≤1. Its entire proof is the existing Finset theorem. Thus no new generic finite-product API is missing.

Evidence: [native-raw-executed.lean.txt](../evidence/Roth.normOne_prod_le/native-raw-executed.lean.txt), [native-raw-success.json](../evidence/Roth.normOne_prod_le/native-raw-success.json), [native-infrastructure-executed.lean.txt](../evidence/Roth.normOne_prod_le/native-infrastructure-executed.lean.txt), [native-infrastructure-success.json](../evidence/Roth.normOne_prod_le/native-infrastructure-success.json), [rejected-raw-executed.lean.txt](../evidence/Roth.normOne_prod_le/rejected-raw-executed.lean.txt), [rejected-raw-receipt.json](../evidence/Roth.normOne_prod_le/rejected-raw-receipt.json), [generality.json](../evidence/Roth.normOne_prod_le/generality.json).

## Phase 4c — modern idiom, nine rows

| # | Applies? | Finding / enabled use |
|---|---|---|
| 1 | Yes | A bundled nonnegative submultiplicative seminorm would expose the same finite induction; representation bridge remains substantive. |
| 2 | No | Finite products have no convergence or topology. |
| 3 | No | No constructed universal object. |
| 4 | No | No closure predicate or substructure set. |
| 5 | Yes | Compiled expanded coefficient-size form uses CommSemiring; abstract finite induction needs only CommMonoid source. |
| 6 | No | No categorical structure to enrich. |
| 7 | Yes | σ and ι already arbitrary; finite induction uses arbitrary CommMonoid and real nonnegative size, verified abstractProd. |
| 8 | Yes | Proof is solely generic Finset induction with normOne supplied as a witness; abstractProd is an existing one-call mathlib specialization. |
| 9 | Pass | False-generalization guard: preserve coefficient L1 under convolution. A pointwise product, Gauss/sup norm, field norm or integral of polynomial values is different. Nonnegative size and unit bound retained for the tested finite induction. |

Q8 diagnostic explicitly inspects the proof body: zero `MvPolynomial` mentions in its two lines; normOne occurs only as the map and in the three witness names. No initial unfolding is even needed: generic finite induction is already explicit. `abstractProd` verifies this abstraction. It is already mathlib API, so Q8 does not justify a new upstream finite-product lemma. A compatible coefficient L1 structure would let generic norm/product API serve determinants and other monoid algebras. No cost-based downgrade is used.

## Phase 4.5 — infrastructure risk

n/a: theorem. All six rows (typeclass diamonds, reducibility, noncanonical unfolding, instance priority, universe constraints, coercion ambiguity) have individual rationales in [generality.json](../evidence/Roth.normOne_prod_le/generality.json). A future norm instance needs a separate risk assessment; none is introduced here.

## Phase 4.6 — five proof-strategy rows

| # | Applies? | Finding |
|---|---|---|
| 1 | No | No epsilon-delta argument. |
| 2 | No | No ideal/submodule inclusion expresses this estimate. |
| 3 | No | No sequences or limits. |
| 4 | No | No universal object construction. |
| 5 | Yes upstream bridge only | Finite induction already exists. A coefficient-size convolution or compatible norm structure would discharge its substantive binary witness; no new finite-product induction API is needed. |

Current finite-product strategy is **MATHLIB-IDIOMATIC**: reuse existing generic induction. Future shared coefficient-size infrastructure would remove project-specific witnesses, but should retain the same Finset induction rather than reprove it.

## Phase 5 — five actual mathlib methods, three forms

Twelve actual formal calls are retained in [formal-search.json](../evidence/Roth.normOne_prod_le/formal-search.json) and individual method/form receipts. Index-unavailable local results are honest source-name hits, not absence evidence; project target/scratch hits are excluded as replacements. External search revisions may differ from pinned mathlib; positive candidates are checked natively at the pin.

| Method | Current coefficient-product form | Literature norm-product form | Abstract submultiplicative-map form |
|---|---|---|---|
| Lean-Finder | Degree-product inequalities; not coefficient L1 | Finset.norm_prod_le and variants | Finset.le_prod_of_submultiplicative_of_nonneg |
| Loogle | MvPolynomial degree/product API | Generic norm-product API | Finset.le_prod_of_submultiplicative family |
| LeanSearch | Coefficient/leading-coefficient product API | Finset.norm_prod_le, prime and nnnorm variants | Exact nonnegative submultiplicative finite induction |
| rg source | [rg-current.json](../evidence/Roth.normOne_prod_le/rg-current.json), [rg-full-name.json](../evidence/Roth.normOne_prod_le/rg-full-name.json) | [rg-literature.json](../evidence/Roth.normOne_prod_le/rg-literature.json) | [rg-abstract.json](../evidence/Roth.normOne_prod_le/rg-abstract.json) |
| Local name search | normOne_prod_le project/scratch hits excluded | Finset.norm_prod_le family | Finset/Multiset.le_prod_of_submultiplicative_of_nonneg |

Pinned sources: [mathlib-inputs.json](../evidence/Roth.normOne_prod_le/mathlib-inputs.json), [mathlib-finset-ring.lean.txt](../evidence/Roth.normOne_prod_le/mathlib-finset-ring.lean.txt), [mathlib-finset-order.lean.txt](../evidence/Roth.normOne_prod_le/mathlib-finset-order.lean.txt), [mathlib-multiset-ring.lean.txt](../evidence/Roth.normOne_prod_le/mathlib-multiset-ring.lean.txt), [mathlib-norm-ring.lean.txt](../evidence/Roth.normOne_prod_le/mathlib-norm-ring.lean.txt). The exact Finset theorem has CommSemiring target, PartialOrder and IsOrderedRing, arbitrary CommMonoid source, and nonnegative/unit/binary witnesses. Both original and raw replays verify it.

`Finset.norm_prod_le` requires NormedCommRing and NormOneClass. Its prime variant instead assumes nonempty s, so using only that variant would restrict this theorem, which permits the empty family. The unit bound or NormOneClass cannot be silently dropped. Fresh guarded failures confirm no raw Norm or NormedCommRing instance for MvPolynomial σ ℤ in the persistent imported environment. The Lp Finsupp source supplies Lp metrics on WithLp, not a tested compatible raw convolution norm: [mathlib-lp-finsupp.lean.txt](../evidence/Roth.normOne_prod_le/mathlib-lp-finsupp.lean.txt). This does not assert global impossibility of a norm construction. The substantive binary bridge has been proved afresh in the raw probe, rather than assumed from the similarly named norm law.

## Phase 5.5 — three statement-shape checks

Normal form: **OK locally, SHIP-AS-STATED** within normOne API; coefficient support sum is the intended quantity, and no iff/RHS normalization issue occurs. Norm notation becomes appropriate only after a compatible representation bridge. Syntactic generality: explicit s,f match `Finset.univ` and matrix-entry family in the determinant consumer; a curried or coefficient-expanded statement would not ease that use. Superfluous arguments: σ,ι determine types, s determines product, f determines factors. No unused class or hypothesis exists. Empty s remains supported; replacing the unrestricted result with only Finset.norm_prod_le' would lose that case.

## Phase 6.0 — complete callers and inline audit

One named direct caller, one occurrence: `Roth.normOne_det_le`, CoeffNorm127. No explicit external-to-module reference. Fresh untruncated [rg-callers.json](../evidence/Roth.normOne_prod_le/rg-callers.json) and [rg-inline.json](../evidence/Roth.normOne_prod_le/rg-inline.json) plus the entire module read find no separate finite-product rederivation. Declaration lines are not callers.

The whole determinant proof was replayed after replacing the product call with `Finset.le_prod_of_submultiplicative_of_nonneg normOne normOne_nonneg (unit proof) normOne_mul_le ...`. It compiles while still using project witnesses; this is an actual local inline experiment, not a mathlib-only certificate.

A fresh native direct proof-value audit examines **293 entries,293 unique Lean names**, all present with values, and finds only `Roth.normOne_det_le`. Name array is generated directly from tracked declaration-order.json, preserving private names using Lean.mkPrivateNameCore. The portable validator checks full exact order equality, not counts alone. This is direct proof-value use, not transitive kernel/simp dependency closure.

Evidence: [callers.json](../evidence/Roth.normOne_prod_le/callers.json), [canonical-audit-array.lean.txt](../evidence/Roth.normOne_prod_le/canonical-audit-array.lean.txt), [native-consumers-executed.lean.txt](../evidence/Roth.normOne_prod_le/native-consumers-executed.lean.txt), [native-consumers-success.json](../evidence/Roth.normOne_prod_le/native-consumers-success.json).

## Phase 6 — actual composition experiments

1. Original and independent replay: existing Finset induction plus three project witnesses, one being the substantive binary coefficient-size law.
2. Roth-free raw probe: missing-project-target guard; full new coefficient-size bridges and genericProd/directProd. Existing finite induction closes genericProd only after those newly proved bridges.
3. Complete determinant caller replay: existing induction inlined with project witnesses; every explicit caller has a concrete refactor.
4. Generic abstractProd: one existing-call proof over arbitrary CommMonoid, verifying that finite induction is fully present. Generic norm signatures and missing raw instances checked independently.

Relative to the fixed normOne representation the evidence does **not** supply a ≤3 existing-mathlib-call full replacement: project normOne_mul_le is not an existing mathlib theorem. The elementary induction component is already composable, but the whole coefficient-size theorem is **NOT-COMPOSABLE under the strict existing-mathlib-only gate on available evidence**. No closing simp with unfolded definitions is mislabelled as a NO certificate. Search is not a proof of global absence.

There is **no Mode B parent re-aim override**: parent normOne was NO-composable, not NO-mathlib-has-it; binary multiplication was BORDERLINE. Those earlier verdicts are context, not inherited evidence.

## Phase 7 — verdict and action

**BORDERLINE-needs-human**. Do not upstream another finite-product induction theorem: mathlib already has it. Retain the local integer-polynomial wrapper while the shared coefficient L1/convolution representation is settled. The abstract induction existing in mathlib does not erase the binary coefficient-size bridge needed for the exact fixed-parent result; asserting NO-mathlib-has-it would omit that witness. A new integer-specific wrapper would also hard-code the unresolved coefficient representation. This is an API boundary judgment, not cost or a failed search.

1. Should coefficient L1 receive a shared Finsupp/monoid-algebra convolution-size API, with finite products obtained directly from existing Finset induction?
2. Should that shared API expose a RingSeminorm or compatible norm structure so Finset.norm_prod_le applies, rather than retain a named integer-polynomial product wrapper?

If removing locally, inline the accepted Finset induction term in the sole determinant caller and keep the binary witness available; the full replay is concrete validation. Alternative local destination is the existing Roth/CoeffNorm.lean coefficient-size API. No standalone PR or accepted-YES grouping is proposed for BORDERLINE. A future shared convolution package should coordinate with the triangle and binary size API, reuse existing Finset induction and revisit this wrapper then. No user interruption is needed to complete the read-only overview.

## Phase 8 — handoff and verification

[verification.json](../evidence/Roth.normOne_prod_le/verification.json) links four accepted exact sources/raw receipts and one rejected attempt separately. All accepted diagnostics are clean, success=true, partial=false, with standard axioms only (propext, Classical.choice, Quot.sound); no recovered sorryAx or raised limits accepted. [validate.py](../evidence/Roth.normOne_prod_le/validate.py) verifies all phases, all17 source/pins, complete formal/literature channels, exact ordered293 unique canonical names, native success/axioms, current manifest hashes/bytes and portable links. [copy-manifest.json](../evidence/Roth.normOne_prod_le/copy-manifest.json) is authoritative; historical worker manifests never replace current validation. Root acceptance remains pending independent review.
