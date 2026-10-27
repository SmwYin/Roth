# MvPolynomial.hasseDeriv_single_aeval_X

Assessment of `Roth/HasseDeriv.lean:253`, canonical declaration 22. Read-only assessment; no production or pin changes.

## Phase 0: baseline

The shared successful `lake build` completed 2467 jobs with exit code 0. All 17 source/pin hashes were freshly recomputed and match the shared input manifest. The declaration resolves and the native kernel replay has no errors, warnings, partial elaboration, or nonstandard axioms. Evidence: [fresh input check](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/input-check.json), [baseline](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/baseline-build.txt), [full source](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/target-source.lean.txt), [native receipt](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/disk-success.json).

## Phase 1: comprehension

For a commutative semiring R and any variable j, embedding a univariate polynomial f into R[σ] by sending its variable to X_j intertwines its nth Hasse derivative with the multivariate derivative of multi-index n e_j. On a monomial aT^m, both sides are the monomial a binom(m,n) X_j^(m-n). Linearity extends this calculation to every polynomial, including orders above the degree, zero order, and coefficients of positive characteristic.

The full elaborated type is universe-polymorphic in σ and R, with `[CommSemiring R]`, `(j : σ)`, `(n : ℕ)`, `(f : Polynomial R)`, and the conclusion

```lean
hasseDeriv (Finsupp.single j n) (Polynomial.aeval (X j : MvPolynomial σ R) f) =
  Polynomial.aeval (X j : MvPolynomial σ R) (Polynomial.hasseDeriv n f)
```

There is no finiteness, decidable equality, characteristic, domain, field, or nonzero-order hypothesis. The proof is polynomial additive/monomial induction followed by evaluation, the monomial Hasse formula, singleton subtraction, and binomial-factor normalization. [Exact executed source](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/disk-executed.lean.txt).

## Phase 2: preliminary checks

BIG: explicitly listed in the module's Main results as the compatibility with univariate Hasse derivatives. This classification does not narrow literature search. One-line definition check: n/a, this is a theorem, not a definition or instance. It is not a definitional-equality glue lemma.

## Phase 3: exhaustive literature

Exact requests, returned-response SHA256 and byte counts are retained in [web receipts](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/web-receipts.json); article/search bodies are not retained. The following summaries are original and concise.

| Channel | Actual query / locator | Result and significance |
|---|---|---|
| Web specific | `"Hasse derivative" multivariate univariate variable` | [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025), Def. 3.4 and Prop. 3.5: translation coefficient definition and binomial monomial expression; coordinate restriction follows by choosing one variable. |
| Web general | `"Hasse Schmidt" polynomial rings arbitrary base ring Taylor coefficients` | Generalized Hasse–Schmidt operator literature exists; this is broader machinery rather than a requirement to replace a coordinate compatibility lemma. |
| Web aliases | `"divided derivatives" polynomial coordinate restriction binomial` | The same binomial normalization is described as divided or Hasse–Schmidt differentiation. Factorial division is unsuitable over arbitrary characteristic. |
| ChatGPT math | Standard form, generality, historical evolution | n/a: `ask_chatgpt_math` is unavailable in the tool inventory; no fabricated second opinion. |
| Local references | `clean.tex`, lines 122–155; grep Hasse/univariate/Polynomial.hasseDeriv | Defines the multivariate monomial operator and explicitly identifies compatibility with mathlib's univariate derivative. The source is mathematical context, not evidence of an existing mathlib bridge. |
| nLab | `site:ncatlab.org/nlab "Hasse" derivative` | [Hasse-Schmidt derivative](https://ncatlab.org/nlab/show/Hasse-Schmidt+derivative), sections for one/several indeterminates, uses commutative rigs and linear extension. A separate direct open of the derivation page failed with unsupported XHTML; indexed derivative text was returned. |
| nCatLab | `site:ncatlab.org "Hasse-Schmidt"` | A dedicated `site:ncatlab.org/ncatlab "Hasse-Schmidt" polynomial` query and `/ncatlab/show/Hasse-Schmidt+derivative` URL attempt were also made. The direct namespace URL was inaccessible via the tool; no independent nCatLab replacement was located. The nLab result is not independent corroboration. |
| Stacks | `site:stacks.math.columbia.edu "divided" "differential operators"`; [09CH](https://stacks.math.columbia.edu/tag/09CH) | Section 10.133 defines finite order differential operators and principal parts. This places Hasse operators in a broader theory, but does not state this polynomial coordinate normalization. |
| MathOverflow | `site:mathoverflow.net "Hasse" derivatives` | [Formal multidimensional Taylor series expansion over commutative rings](https://mathoverflow.net/questions/288218/formal-multidimensional-taylor-series-expansion-over-commutative-rings) discusses the need for Hasse rather than factorial division. Context only, not proof authority. |
| Recent arXiv | `site:arxiv.org "Hasse-Schmidt" "2023" OR "2024" OR "2025" OR "2026"` | [Burton, arXiv:2501.19379](https://arxiv.org/abs/2501.19379), submitted Jan. 31, 2025, revised Feb. 14, 2025, studies commuting generalized operators. Within five years of Oct. 26, 2026; abstract does not supersede the bridge. |

The standard object is the coefficient of an increment monomial in a polynomial translation. Over commutative semirings the binomial formula makes sense without coefficient subtraction or factorial inverses. Infinite variable types are handled through finite support. The current lemma expresses the one-coordinate restriction of precisely that object. The semiring form is already stronger than field-only presentations; broader Hasse–Schmidt or principal-parts objects do not invalidate a concrete polynomial API theorem.

## Phase 4a–b: every parameter and hypothesis

| Parameter | Audit and weakening result |
|---|---|
| `σ : Type*` | Arbitrary variable type and universe; no finite-type assumptions to remove. A supplied j already witnesses nonemptiness, so no separate `Nonempty σ` is needed. |
| `R : Type*` | Arbitrary coefficient type and universe, not fixed to a field or characteristic. |
| `[CommSemiring R]` | Fixed canonical parent interface: MvPolynomial and algebra evaluation require it. Native `#check_failure MvPolynomial σ S` under only `[Semiring S]` confirms failure. An expanded monoid-algebra representation would change the parent development, not mechanically weaken this theorem. |
| `j : σ` | Chooses the same coordinate on both sides. Removing it leaves an unspecified embedding/derivative. |
| `n : ℕ` | Arbitrary order, including zero. Natural-number indices are integral to the Hasse/binomial object; replacing them with arbitrary additive monoids is not this object. |
| `f : Polynomial R` | Arbitrary polynomial, no bound, support restriction, monicity, or nonzero hypothesis. Bundling into a linear-map equation removes pointwise syntax without weakening mathematics. |

MAXIMALLY GENERAL within its canonical parent interface. Zero verified hypothesis-weakening opportunities. The full source induction compiled at this generality in both the target environment and an isolated mathlib-only reconstruction. No claim is made that all imaginable representations have the same assumptions.

## Phase 4c: modern-idiom audit

| # | Question | Answer, concrete consequence |
|---|---|---|
| 1 | Typeclasses | Already uses canonical `CommSemiring`; adding a bespoke class would duplicate polynomial data. |
| 2 | Filters/nets | No: finite polynomial identity, no topology or limits. |
| 3 | Universal property | Polynomial evaluation is already the canonical algebra homomorphism. Its universal property alone does not compare the linear Hasse operators; the minimal native probe supplies normalization by definition simp after basis extensionality. |
| 4 | Bundled substructure | No set/closure predicates. A bundled linear-map commuting square is useful and was compiled; it is equivalent to the pointwise statement. |
| 5 | Hierarchy | Already commutative semirings. Fixed parent weakening to Semiring fails; no field/characteristic assumptions. |
| 6 | Higher category | No categorical coherence content requiring categorification. |
| 7 | Abstract index | No: order n is the natural Hasse order. Replacing ℕ changes binomial arithmetic. |
| 8 | Concrete-via-abstract | Diagnostic fires syntactically: the monomial branch has one `X` substring line through `X_pow_eq_monomial`, zero literal `X j` occurrences. The real abstraction is equality of linear maps on monomials; it needs the single-coordinate monomial premise, which the minimal experiment actually discharges by definition simp. This is a short basis-ext proof, not an existing named Hasse compatibility theorem. |
| 9 | False-generalization guard | Reject arbitrary evaluation points: n=1, f=T, evaluation at 0 gives derivative of 0 on the left and 1 on the right over ℕ. A coordinate must be retained, or substantial compatibility hypotheses supplied. |

[Q8 evidence](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/q8-diagnostic.json). Modern idiom available as equivalent packaging, not a required semantic generalization. The native bundled square composes linear maps; the existing pointwise orientation directly rewrites the actual caller. A generic theorem asserting two linear maps agree given agreement on all monomials is already `Polynomial.lhom_ext'`; restating our result as that conditional theorem would discard its substantive coordinate calculation.

## Phase 4.5: infrastructure risks

All six rows are n/a because a theorem introduces no new computational definition, instance, or coercion: typeclass diamond; reducibility leak; noncanonical unfolding; instance priority collision; universe-polymorphism construction; coercion ambiguity. The theorem retains the existing parent definitions and separate universes.

## Phase 4.6: proof strategy

| # | Strategy question | Finding |
|---|---|---|
| 1 | Topology ε–δ versus filters | n/a, no topology. |
| 2 | Element algebra versus substructure inclusion | The goal is equality of linear operators; additive/monomial induction is its natural basis proof. Bundled equality is equivalent and compiled. |
| 3 | Sequences versus nets | n/a, no limits. |
| 4 | Construction versus universal property | Evaluation is already canonical. Algebra-hom extensionality cannot directly compare Hasse derivatives of positive order, which are not algebra homomorphisms. |
| 5 | Missing helpers | Multivariate Hasse monomial normalization belongs with the parent operator. The pinned univariate monomial theorem exists; a bridge to the multivariate embedding is the target gap. |

MATHLIB-IDIOMATIC. A linear-map monomial-ext proof may shorten syntax; the minimal experiment verifies that definition simp discharges the normalized premise. Neither syntax change constitutes a strictly weaker theorem.

## Phase 5: all five methods on three forms

[Raw formal-search receipts](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/formal-search.json) preserve all exact requests and complete responses. [Source rg receipts](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/source-search.json) provide the fifth method. External indexes may differ from the pinned revision; local results include archived evidence copies, which were excluded as candidates. All three local queries report `index: unavailable`; source hits still inform the audit but no empty index result proves absence.

| Form | Finder | LeanSearch | Loogle | rg | Local |
|---|---|---|---|---|---|
| Current single-index/aeval-X | Ordinary pderiv evaluation and univariate Hasse monomial formula | Same, plus LaurentSeries | `MvPolynomial.hasseDeriv`: unknown identifier; actual failure, not absence proof | Project bridge and one caller; no mathlib multivariate Hasse declaration | `Polynomial.hasseDeriv` source found, index unavailable |
| Literature coordinate restriction | `hasseDeriv_one`, univariate Hasse | Hasse, LaurentSeries, pderiv | `Polynomial.hasseDeriv, Polynomial.aeval`: empty | Hasse/Schmidt search in MvPolynomial returns no Hasse operator | `hasseDeriv` shows project declaration and univariate source; index unavailable |
| Abstract intertwining square | Derivations and Kähler first-order identities | `Polynomial.toMvPolynomial` | `Polynomial.hasseDeriv, Polynomial.monomial`: apply and monomial formulas | `lhom_ext'`, `aeval_monomial`, `toMvPolynomial` read in pinned source | `aeval` canonical evaluations; index unavailable |

Pinned positive candidates: `Polynomial.hasseDeriv_monomial` and `Polynomial.hasseDeriv_apply` in `Mathlib/Algebra/Polynomial/HasseDeriv.lean:104,62`; `Polynomial.aeval_monomial` in `Mathlib/Algebra/Polynomial/AlgebraMap.lean:298`; `Polynomial.lhom_ext'` in `Mathlib/Algebra/Polynomial/Basic.lean:734`; `Polynomial.toMvPolynomial` in `Mathlib/Algebra/MvPolynomial/Equiv.lean:880` is definitionally `aeval (X j)`. Ordinary derivations concern first order and cannot recover all Hasse orders in positive characteristic. LaurentSeries and Kähler results have different source/target operators. The isolated probe guards absence of the project operator and target and reconstructs the raw operator without importing Roth. [Pinned univariate source](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/polynomial-hasse-source.lean.txt), [raw execution](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/raw-executed.lean.txt), [raw native receipt](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/raw-success.json).

## Phase 5.5: statement shape

Normal form: keep derivative-of-embedding on the left and embedding-of-univariate-derivative on the right, matching the caller's simplification. `Polynomial.toMvPolynomial j` is the same embedding with another name, not a separate mathematical contribution.

Syntactic generality: the compiled bundled form is

```lean
(hasseDeriv (Finsupp.single j n)).comp (Polynomial.aeval (X j)).toLinearMap =
  (Polynomial.aeval (X j)).toLinearMap.comp (Polynomial.hasseDeriv n)
```

It follows by explicit `LinearMap.ext`, introducing f, and the independently replayed pointwise proof. It enables rewriting compositions, but the pointwise lemma remains best for the actual `rw` site. No RESTATE-BEFORE-SHIP requirement follows from equivalent bundling. Superfluous-argument audit: every parameter selects the operators or polynomial in the conclusion; the only instance supports the parent interface. No unused proof hypothesis exists.

## Phase 6.0: full explicit caller and inline audit

| Source | Role and audit |
|---|---|
| `Roth/Separation.lean:160`, theorem `Roth.hasseDeriv_rename_mul_aeval` (146–164) | One explicit proof reference, with j=none, n=ν, f=V. It rewrites the derivative of the univariate factor after splitting disjoint derivative indices and pulling out a factor independent of none. The Option.none instance was compiled using the independently replayed proof. |

Internal explicit use count: 1. The defining theorem and module-docstring mention are excluded. Whole `Roth/Separation.lean` and whole declaring module were read. The inline grep examines both orders of hasseDeriv/aeval: `GenWronskian.lean:159` is ordinary derivative chain rule, `MainLemma.lean:409` coefficient-map/evaluation transport, and `Separation.lean:365` calls the separated-product theorem. None rederives this bridge inline. No claim is made about opaque kernel/simp dependency closure. [Full caller source](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/caller-source.lean.txt).

If a future decision removes the public theorem, replace the one `rw` occurrence at Separation:160 by a local `have hbridge :=` proved by the exact polynomial induction (or the fully verified monomial-ext proof), then rewrite with `hbridge none ν V`. This duplicates a real normalization proof and uses project parent API; it is not a mechanical replacement by an existing mathlib lemma.

## Phase 6: actual composition experiments

The original polynomial induction was replayed without calling the target theorem. An isolated mathlib-only raw `Finsupp.lsum` operator proves the same identity via its explicitly proved monomial formula. New reconstructed helpers are not counted as existing mathlib building blocks. Native target, linear-square and actual caller fragments succeed with standard axioms only. The decisive third experiment uses only the raw operator definition, `Polynomial.lhom_ext'`, `LinearMap.ext`, and a closing definition-expanding simp. It has no coefficient helper, monomial helper, polynomial induction, or invocation of a previously proved bridge. The basis normalization premise is actually discharged by this simp, not merely assumed. Thus this is Phase 6b's closing-definition-simp case, rather than a demonstrated ≤3 existing-call term or a substantial independently missing proof. [Minimal exact source](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/minimal-executed.lean.txt), [complete native receipt](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/minimal-success.json).

## Phase 7–8: verdict and action

**BORDERLINE-needs-human**: complete read-only assessment with no unresolved verification. The bridge is standard and the parent multivariate Hasse API is absent from pinned mathlib, but its full proof reduces to existing basis extensionality and definition-expanding simplification. Phase 6b explicitly routes a closing `simp [defs...]` composition to review; it does not justify automatic NO, and the successful minimal experiment prevents presenting the proof as a substantive missing coefficient calculation. Cost is not a verdict factor.

Concrete future upstream API questions:

1. Should the multivariate Hasse PR expose this coordinate compatibility as a public rewrite lemma, given its sole explicit consumer and the closing-simp basis proof?
2. Should the primary public statement use `Polynomial.aeval (X j)` or the definitionally equal `Polynomial.toMvPolynomial j`, with the other spelling provided only by definitional reduction?
3. Should the PR include the equivalent bundled linear-map commuting square alongside the pointwise rewrite lemma, or retain only the pointwise form used at Separation:160?

Retain locally in `Roth/HasseDeriv.lean` pending that API decision. If retained upstream, place it in proposed `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` beside the new operator and monomial formula. Proposed PR title: `feat(Algebra/MvPolynomial): add multivariate Hasse derivatives and univariate compatibility`. If omitted from the public API, keep a private/local bridge at the one Separation caller using the verified basis-ext and definition-simp proof; rewrite the occurrence at line 160 with that local bridge. No existing named pinned theorem is asserted to replace it.

Grouping candidates are taken from the actual completed progress records, not inferred from names: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, and `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero` are accepted YES entries. In particular, monomial/apply/zero wrappers are not silently counted as YES.

Before any upstream PR run `/generalise MvPolynomial.hasseDeriv_single_aeval_X`, `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_single_aeval_X`, and `/pre-submit`; settle the three API questions during upstream preparation. Reviewer candidates from recent relevant pinned commits: Moritz Firsching (`334438dace`, Hasse derivative map), Yaël Dillies (`631b214f7c`, MvPolynomial coefficient API), and Nathanael Thompson (`026dd116f1`, monomial API). [Commit evidence](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/reviewer-commits.json).

The production source and pins remain unchanged. [Verification manifest](../evidence/MvPolynomial.hasseDeriv_single_aeval_X/verification.json) distinguishes accepted complete proofs from a rejected guard attempt. Native success proves the target replay, equivalent bundled statement, literal Option.none caller instance, raw construction/induction, minimal composition and arbitrary-image counterexample; it does not claim a fresh rebuild of all downstream files. The shared full build is reused only under the fresh 17-input match.
