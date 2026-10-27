# Roth.kronecker_monomial — full mathlibable assessment

Verdict: **NO-mathlib-has-it**, by independently verified parent re-aim to
`MvPolynomial.aeval_monomial` (`Mathlib/Algebra/MvPolynomial/Eval.lean:681`).
The geometric exponent is a specialization, not extra mathematical content.
The old spelling needs a genuine finite-product/finite-sum normalization; it is
not definitionally equal to the existing law. No production changes are proposed
as already applied. 

## Phase 0 — baseline and prefilter

All17 source/pin hashes were freshly compared with the shared baseline manifest;
all match. The reusable build exited0 with2467 jobs and no errors/warnings.
[Fresh inputs](../evidence/Roth.kronecker_monomial/inputs.json),
[build](../evidence/Roth.kronecker_monomial/baseline-build.txt).
The public qualified name has no mathlib exact-name hit. It is not private, an
example, an auxiliary declaration or a definitional glue lemma. Full assessment
therefore applies, including the independent parent re-aim test.

## Phase 1 — comprehension

Declared at `Roth/GenWronskian.lean:60`.
Full native elaborated type:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ]
  (k : ℕ) (d : σ →₀ ℕ) (a : K),
  (Roth.kronecker k) ((MvPolynomial.monomial d) a) =
    Polynomial.C a * Polynomial.X ^ Roth.kroneckerExp k d
```

`kronecker k` evaluates variable j at `X^(k^(equivFin σ j))` and `kroneckerExp`
is the sum of d j times that exponent. The theorem computes the image of one
coefficient-bearing monomial. Evaluation preserves multiplication and powers;
`(X^w)^n=X^(w*n)` and multiplying powers adds exponents. Summing over the full
finite variable type adds zero terms outside d.support. Neither k>1 nor bounded
digits nor characteristic zero is needed; these enter later injectivity theorems.
There is no l parameter. The entire272-line declaring module and the complete
sole caller were read. The target directly uses project definitions kronecker
and kroneckerExp, and mathlib monomial evaluation and elementary power/product
laws. It introduces no new operator or structure.

[Whole module](../evidence/Roth.kronecker_monomial/source-0.lean.txt),
[exact native original](../evidence/Roth.kronecker_monomial/kronecker-monomial-original-executed.lean.txt),
[full type/proof/axiom receipt](../evidence/Roth.kronecker_monomial/kronecker-monomial-original-receipt.json).

## Phase 2 — size and definition test

**SMALL:** a monomial evaluation specialization supporting coefficient extraction;
the name Kronecker describes the chosen substitution, not a new standalone named
major theorem. The theorem is not the module's nonvanishing Wronskian theorem.
One-line definition-only test: **n/a, theorem**, not def/class/instance. Its short
simp proof is not a definition-only exemption or evidence of upstream novelty.
Literature search remains exhaustive.

## Phase 3 — exhaustive literature

All named channels were actually attempted. The protocol informally says nine
channels but lists three web forms plus the named specialized sources; no invented
extra channel is counted. Web artifacts retain exact requests, returned response
SHA256/bytes/status, title/URL locators and original summaries only. No full web
bodies are stored. There are no credential-bearing URL queries.

| Channel | Actual evidence and finding |
|---|---|
| General web1 | `Kronecker substitution monomial exponent weighted sum polynomial`: monomial encodings, weighted degree, algorithm references. |
| General web2 | `multivariate polynomial evaluation monomial product powers algebra homomorphism`: ordinary substitution/evaluation background. |
| General web3 | `Kronecker substitution arbitrary commutative ring polynomial encoding`: sources distinguish arbitrary-characteristic substitution from stronger injectivity uses. |
| Optional ask_chatgpt_math | Unavailable tool; explicitly not treated as a negative mathematical result. |
| Local clean.tex | §2, proof of Lemma `roth:lem1`, lines227–271: expands φ into monomials and replaces their exponents by s1+k s2+…; bounded digits are used for uniqueness, not for this evaluation identity. |
| nLab | Domain query returned [polynomial](https://ncatlab.org/nlab/show/polynomial), Definitions and meanings: free commutative R-algebra on arbitrary variables. Initial polynomial+algebra URL404; direct correct-page retry unsupported XHTML. Search-returned content supports the universal-property formulation, not a newly claimed theorem. |
| nCatLab | Proper `site:ncatlab.org/ncatlab` query attempted; no pertinent separate categorical source found. Direct HomePage inaccessible. nLab hits are not mislabeled nCatLab results. |
| Stacks | Domain queries returned [04EB](https://stacks.math.columbia.edu/tag/04EB), proof constructs polynomial-algebra map from chosen generators; [07H5](https://stacks.math.columbia.edu/tag/07H5) concerns divided-power algebras and is not the same multiplication. Initial00RM open is differentials, a documented mis-target, not evidence for the evaluation law. No exact monomial-law locator claimed. |
| MathOverflow | `site:mathoverflow.net Kronecker substitution monomial` returned mainly Kronecker coefficients/products and other Kronecker theorems. [53065](https://mathoverflow.net/questions/53065/a-question-about-how-polynomials-simplify-under-substitution) is polynomial-substitution discussion; no stronger evaluation hypotheses or exact replacement inferred. |
| Recent arXiv, five years | Explicit after2021-10-27/before2026-10-28 search and supplementary2024 query. [2403.12716](https://arxiv.org/abs/2403.12716), Wang–Su–Wang–Zhang2024, abstract: iterative Kronecker substitution and smaller substitution exponents. [2404.00332](https://arxiv.org/abs/2404.00332), Shunia2024: quotient-ring encodings. [2311.10276](https://arxiv.org/abs/2311.10276) inspected and excluded: Schur/Kronecker products, unrelated. |

Primary supplementary source: Beecken–Mittmann–Saxena,
[Algebraic Independence and Blackbox Identity Testing](https://www.cse.iitk.ac.in/users/nitin/papers/alg-indep.pdf),
ICALP2011, §3.1, “A Kronecker-Inspired Map (Arbitrary Characteristic)”: variables
are sent to powers t^(D^i). This identifies the same substitution family, while
its additional faithful-homomorphism results are not conflated with this identity.

Literature-standard content: for any commutative coefficient ring and substitution
values, a monomial evaluates to its coefficient image times the product of values
raised to exponents. For monomial values t^w_j, this yields the weight sum.
Finite variable enumeration and a geometric progression are a special case.

[General requests](../evidence/Roth.kronecker_monomial/web-0.json),
[specialized queries](../evidence/Roth.kronecker_monomial/web-1.json),
[MO/recent arXiv](../evidence/Roth.kronecker_monomial/web-2.json),
[direct accesses](../evidence/Roth.kronecker_monomial/web-direct.json),
[corrected/supplementary queries](../evidence/Roth.kronecker_monomial/web-supplement.json),
[local excerpt](../evidence/Roth.kronecker_monomial/local-literature.txt).

## Phase 4a–4b — parameters and generality

| Parameter / assumption | Actual use, weakening and result |
|---|---|
| K, Field K | Original spelling constrained by parent kronecker's interface. Expanded weighted theorem compiled over arbitrary CommSemiring R, including zero divisors and positive characteristic; no division, subtraction, nontriviality or char assumption. This is a representation/parent-interface refactor, not dropping Field while still invoking the unchanged parent. |
| σ, Fintype σ | Needed by chosen equivFin enumeration and full sum. Arbitrary σ compiled in the weighted form using finite d.support. No finite universe assumption in abstract aeval_monomial. |
| k : ℕ | Any natural allowed, including0/1. Replace geometric weights by arbitrary w : σ → ℕ in compiled weighted theorem. Positivity is not required. |
| d : σ →₀ ℕ | Natural exponents encode the same ordinary polynomial object; finite support is essential, whole σ need not be finite. |
| a : K | Any coefficient, including0; no unit/nonzero assumption. Coefficient image may be general algebraMap into any commutative algebra in existing aeval_monomial. |
| codomain Polynomial K | Generalized to any commutative R-algebra A in compiled abstract theorem with arbitrary variable values g. |
| universes and implicit parameters | Native type has independent u_1,u_2 and no l/CharZero parameter; raw theorems use Type*. No universe restriction to weaken. |

**STRICTLY NARROWER THAN STANDARD** after expanding the two project interfaces;
the useful general version is already present in mathlib. This is not a new
YES-generalise-first proposal. Actual raw proofs and independent bridges compiled:

```lean
-- Existing abstract law: a single existing-call term.
MvPolynomial.aeval_monomial g d a
-- The more general monomial-value specialization actually verified:
aeval (fun j ↦ (Polynomial.X : Polynomial R) ^ w j) (monomial d a) =
  Polynomial.C a * Polynomial.X ^ Finsupp.weight w d
```

The exact executable source is linked below.
[Raw exact source](../evidence/Roth.kronecker_monomial/kronecker-monomial-raw-executed.lean.txt),
[raw success](../evidence/Roth.kronecker_monomial/kronecker-monomial-raw-receipt.json),
[independent bridge](../evidence/Roth.kronecker_monomial/kronecker-monomial-bridge-executed.lean.txt),
[bridge success](../evidence/Roth.kronecker_monomial/kronecker-monomial-bridge-receipt.json).

## Phase 4c — modern idiom, nine rows

| # | Question | Result / actual downstream consequence |
|---|---|---|
|1| Typeclasses | Already uses Field/Fintype typeclasses; do not add ad hoc hypotheses. |
|2| Filters/nets | No: finite algebraic identity. |
|3| Universal property | Yes: aeval is the free commutative-algebra evaluation hom. Existing aeval_monomial computes it in any target algebra, including MvPolynomial and Polynomial. |
|4| Bundled substructure | No closure predicates; substitution already bundled AlgHom. |
|5| Field to semiring/module | Yes: compiled CommSemiring weighted/abstract forms; allows e.g. natural coefficients without field instances. Pure Module would discard needed multiplicative evaluation. |
|6| Higher categories | No mathematical role or concrete downstream benefit identified. |
|7| Index generality | Arbitrary variable type and weights compiled. Ordinary polynomial exponent ℕ remains correct; replacing by signed exponents would change to Laurent/group algebra and is rejected. |
|8| Concrete-via-abstract diagnostic | Yes. kronecker and kroneckerExp occur only in the single unfolding simp list, then the proof uses aeval_monomial and generic power laws. No property of geometric weights or chosen enumeration remains. Verified abstract g-form is an exact existing call; weighted form uses support and weight. Composes directly with aeval and avoids changing enumeration for other substitutions. |
|9| False-generalization guard | No false generalization for nonnegative arbitrary weights/CommSemiring: geometric special case is recovered by compiled exp_eq and map_eq. Different notions such as divided-power multiplication, negative exponents or global injectivity without digit bounds are explicitly rejected. |

Modern form available **already in mathlib**; no missing abstraction inferred.

## Phase 4.5 — infrastructure risk

The declaration is a theorem, so each required definition-risk row is **n/a**:
(1) typeclass diamond; (2) reducibility leak; (3) noncanonical unfolding;
(4) instance-priority collision; (5) universe-polymorphism issues;
(6) coercion ambiguity.
It adds no definition, instance or coercion. Parent replacement bridges are
explicitly propositional normalization rather than a hidden defeq claim.

## Phase 4.6 — proof strategy, five rows

| # | Diagnostic | Applies / alternative |
|---|---|---|
|1| ε–δ vs filters | No topology. |
|2| Elements vs substructure inclusions | No closure theorem; evaluation of a specified monomial is the appropriate element statement. |
|3| Sequences vs nets | No analysis. |
|4| Construction vs universal property | Existing aeval already packages universal-property substitution; use aeval_monomial instead of re-proving by induction. |
|5| Missing helpers that should exist | None established: evaluation, finite-support product, power multiplication and product-power sum laws all exist. The generic weighted helper is a newly proved probe and is not counted as an existing replacement. |

**MATHLIB-IDIOMATIC** strategy for the local spelling; **REFACTOR-RECOMMENDED**
for export/API organization: use existing generic evaluation law, with local
normalization where the coefficient-extraction proof needs the old exponent
spelling. Cost does not determine this verdict.

## Phase 5 — all five actual mathlib methods

Twelve actual formal search requests cover current, literature-standard and
abstract forms. All returned responses; local current form also includes scratch
assessment names, which are excluded from mathlib evidence. External index hits
may reflect different revisions, so pinned source/native checks are decisive.

| Method | Current | Standard | Abstract |
|---|---|---|---|
| Finder | Kronecker/monomial query: expand_monomial and substitution relatives | Evaluation monomial query: eval₂_monomial | Algebra hom monomial query: generators/aeval relatives |
| Loogle | `MvPolynomial.aeval, MvPolynomial.monomial`: aeval_monomial | `MvPolynomial.eval₂, MvPolynomial.monomial`: eval₂_monomial | `MvPolynomial.aeval, _ = _ * _`: aeval_monomial |
| LeanSearch | Kronecker evaluation query: eval_monomial | Product/powers query: eval₂_mul_monomial and relatives | Arbitrary commutative algebra: aeval_monomial |
| rg | Qualified name/current-form search archived, no mathlib exact target | Full untruncated aeval/eval₂/eval₂Hom monomial declarations | weight/product normalization source search |
| Local name search | kronecker: project/scratch hits only | aeval_monomial: pinned mathlib theorem | eval₂_monomial: eval/evaluation API relatives |

[Exact formal requests and raw receipts](../evidence/Roth.kronecker_monomial/formal-search.json),
[rg current](../evidence/Roth.kronecker_monomial/rg-current.json),
[rg standard](../evidence/Roth.kronecker_monomial/rg-standard.json),
[rg abstract](../evidence/Roth.kronecker_monomial/rg-abstract.json).

Pinned positive hit (independently source-read and native checked):

```lean
MvPolynomial.aeval_monomial (g : σ → A) (d : σ →₀ ℕ) (a : R) :
  aeval g (monomial d a) = algebraMap R A a * d.prod (fun i n ↦ g i ^ n)
```

`eval₂_monomial` at Eval.lean92 and `eval₂Hom_monomial` are the underlying ring-map
versions. `Finsupp.weight_eq_sum` at Weight.lean100 relates the finite-sum exponent
to arbitrary weights. `Polynomial.algebraMap_eq`, `Finsupp.prod_fintype`,
`pow_mul`, `mul_comm`, and `Finset.prod_pow_eq_pow_sum` provide old-form
normalization. [Pinned Eval source](../evidence/Roth.kronecker_monomial/source-1.lean.txt),
[pinned Weight source](../evidence/Roth.kronecker_monomial/source-2.lean.txt).
No absence claim is used to decide this assessment; a costly exact? absence
probe would add no evidence to this positive replacement hit.

## Phase 5.5 — three statement-shape checks

1. **Normal form:** aeval_monomial's algebraMap/product RHS is canonical for
arbitrary substitution. For the specific coefficient calculation, C a * X^n is
a useful local normal form because coeff_C_mul_X_pow consumes it directly.
2. **Syntactic generality:** replace fixed geometric values by arbitrary g for
the existing exact theorem; replace the finite full sum by weight for monomial
values. Both representations were actually compiled. No need for O(n²) wrapper
conversion API.
3. **Superfluous arguments:** k,d,a all occur essentially in the fixed form;
Field/Fintype are parent-interface requirements, not mathematical requirements
of expanded evaluation. No l/CharZero appears. No positivity hypotheses to drop.

**RESTATE-BEFORE-SHIP** as an independent export; existing aeval_monomial already
provides that restatement. Preserve the local coefficient-oriented normal form
only within its caller if convenient.

## Phase 6.0 — source/canonical caller audit

| Explicit caller | Source location | Use | Concrete refactor |
|---|---|---|---|
| Roth.coeff_kronecker | GenWronskian.lean93 | `simp_rw [kronecker_monomial, Polynomial.coeff_C_mul_X_pow]` after expanding P into monomials | Introduce local hmon e a proved from aeval_monomial plus the exact normalization list, and replace only the simp_rw entry by hmon. Alternatively re-aim parent representations and normalize once at coefficient extraction. |

Internal named use count **1**, external-module explicit references **0**;
occurrences excluding the declaration **1**. Inline-derivation grep found no
independent duplicate Kronecker monomial computation elsewhere in production;
Roth/HasseDeriv, CoeffNorm and MainLemma use generic prod_pow_eq_pow_sum for other
purposes. The target has no simp attribute. This count is source-level, not a
claim about opaque kernel dependency closure or downstream mathematical use.

Native canonical audit independently visits **293 names,293 unique,293 present,
293 values in exact tracked order**, including real private-name encodings.
Its sole immediate value consumer is Roth.coeff_kronecker. This reinforces the
source audit; it does not replace it or claim a transitive dependency count.
[Source refs](../evidence/Roth.kronecker_monomial/rg-callers.json),
[inline grep](../evidence/Roth.kronecker_monomial/rg-inline.json),
[caller summary](../evidence/Roth.kronecker_monomial/callers.json),
[exact canonical execution](../evidence/Roth.kronecker_monomial/kronecker-monomial-audit-executed.lean.txt),
[audit raw receipt](../evidence/Roth.kronecker_monomial/kronecker-monomial-audit-receipt.json).

## Phase 6 — actual composition and replacement experiments

Re-aimed abstract form is **COMPOSABLE in one existing call**:

```lean
example {R A σ : Type*} [CommSemiring R] [CommSemiring A] [Algebra R A]
    (g : σ → A) (d : σ →₀ ℕ) (a : R) :
    MvPolynomial.aeval g (MvPolynomial.monomial d a) =
      algebraMap R A a * d.prod (fun i n ↦ g i ^ n) :=
  MvPolynomial.aeval_monomial g d a
```

Honest old-form count: unfolding2 project definitions plus aeval_monomial and
at least5 generic normalization ingredients (prod_fintype, pow_mul, mul_comm,
prod_pow_eq_pow_sum, automatically discharged zero exponent conditions/coefficient
algebra map). It is not a ≤3-call old-form term. The actual closing simp is
Phase6b's **BORDERLINE composition signal considered in isolation**, not automatic
NO-composable. The mandatory ModeB parent re-aim rule resolves the final bucket:
kronecker is already re-aimed to aeval, aeval already has the analogous monomial
law, and the representation bridge was independently verified. Therefore final
NO-mathlib-has-it, with no claim that normalization is definitional.

The isolated mathlib-only raw theorem `weighted_monomial` proves the arbitrary
weight/no-Fintype specialization; it is a new helper proof, not a claimed existing
mathlib lemma. `#check_failure Roth.kronecker_monomial` confirms isolation. The
project-form target proof compiles without invoking the target or its generated
simp helpers. First simp-only attempt left a finite-product zero-side-condition;
its rejected source/receipt are preserved separately, not accepted as success.
The corrected ordinary simp proof matches the original normalization pattern.

Full caller replay compiled with only the target invocation replaced by local
hmon. All coefficient sum/injectivity steps remain, so this checks actual argument
flow rather than merely asserting an inlining plan. The executed caller source
contains no kronecker_monomial identifier.
[Exact corrected old-form proof](../evidence/Roth.kronecker_monomial/kronecker-monomial-probes-executed.lean.txt),
[success receipt](../evidence/Roth.kronecker_monomial/kronecker-monomial-probes-receipt.json),
[exact caller replay](../evidence/Roth.kronecker_monomial/kronecker-monomial-consumer-executed.lean.txt),
[caller success](../evidence/Roth.kronecker_monomial/kronecker-monomial-consumer-receipt.json).

## Phase 7 — actionable verdict and gate

**NO-mathlib-has-it.** The independently verified analogous law is
`MvPolynomial.aeval_monomial`, in `Mathlib/Algebra/MvPolynomial/Eval.lean:681`.
The exact abstract one-call specialization and original-form normalization both
compile; independent `map_eq` rfl and `exp_eq` via weight_eq_sum verify the bridge.
This follows the explicit parent re-aim gate, not inherited taste, cost, failed
search, an unproved generalization, or a falsely counted ≤3-call old-form proof.
All required phases and caller rows are present; rejected evidence is separated.

Next action: delete this standalone theorem when carrying out the parent/API
refactor. At the sole explicit caller Roth.coeff_kronecker line93, inline the
verified local hmon computation, then retain coeff_C_mul_X_pow; exact replay
shows this compiles. Retaining the old presentation temporarily belongs in
`Roth/GenWronskian.lean` as a private/local helper for its coefficient argument,
not Archive or a new mathlib export. Existing building blocks are all named in
Phase5; no new upstream PR or reviewer selection is appropriate to a NO verdict.
No production/Git/progress mutation was performed by this worker.

## Phase 8 — completed package

All native runs are complete, successful and free of errors/warnings in their
accepted receipts; disk runs have partial=false. Raw run_code uses its documented
diagnostics format without a partial field. All printed axioms are within
propext/Classical.choice/Quot.sound. Native checks are scoped to fresh target
regions while full-file errors/warnings/axioms are checked. Exact sources retain
original execution paths in receipts. The validator checks the current copy
manifest, source/pin hashes, exact canonical order, all search channels, accepted
sources/receipts, links and secret guard. Root owns integration and independent
acceptance.

[Machine assessment](../evidence/Roth.kronecker_monomial/assessment.json),
[verification index](../evidence/Roth.kronecker_monomial/verification.json),
[portable validator](../evidence/Roth.kronecker_monomial/validate.py).
