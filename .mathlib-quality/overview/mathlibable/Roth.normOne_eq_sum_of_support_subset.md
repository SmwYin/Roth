# Mathlibable assessment — `Roth.normOne_eq_sum_of_support_subset`

Canonical declaration **78/293**, public theorem at `Roth/CoeffNorm.lean:54–56`.
Verdict: **NO-mathlib-has-it**. The existing theorem
`Finsupp.sum_of_support_subset` is the same finite-support padding law at greater
generality. Its exact old-interface specialization compiled. The cast-zero and
absolute-value-zero obligations are explicit mathematical facts, not definitional equality.

## Phase 0 — Baseline and resolution

The saved `lake build` succeeded with2467 jobs at baseline commit
`99f19fda4b3cbee38fc0d31af76075834f5cc265`. All17 source/toolchain/dependency-pin
hashes were freshly compared and matched. The full declaring module and both entire
caller proofs were read. The module develops integer-polynomial coefficient ℓ¹ estimates,
diagonal substitution and evaluation bounds for Roth's determinant/main lemma.
No production Lean, pins, Git, overview or progress files were modified.
[Baseline](../evidence/Roth.normOne_eq_sum_of_support_subset/baseline-build.txt),
[inputs](../evidence/Roth.normOne_eq_sum_of_support_subset/inputs.json),
[hash comparison](../evidence/Roth.normOne_eq_sum_of_support_subset/input-hash-check.json),
[canonical metadata](../evidence/Roth.normOne_eq_sum_of_support_subset/canonical-entry.json),
[canonical order](../evidence/Roth.normOne_eq_sum_of_support_subset/canonical-order.json),
[module](../evidence/Roth.normOne_eq_sum_of_support_subset/source-module.lean.txt).

## Phase 1 — Statement and mathematical proof

Full native type (universe label normalized, integer-to-real casts explicit):

```lean
∀ {σ : Type u_1} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)},
  P.support ⊆ s → Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)|
```

For an integer multivariate polynomial, its coefficient ℓ¹ norm can be computed by
summing absolute coefficient values over any finite exponent set containing all
nonzero coefficients. Every extra exponent has zero coefficient, whose real absolute
value is zero. Thus enlarging the summation set leaves the result unchanged.
The variable type `σ` is arbitrary and universe-polymorphic; `P` and `s` are implicit,
and the only hypothesis `hs` asserts support containment. There is no finite-variable,
degree, nonzero, positivity or decidable-equality assumption. The only project
dependency in the statement is `Roth.normOne`; the proof body has no project calls.
The original proof is `Finset.sum_subset` with vanishing coefficients supplied by
`MvPolynomial.notMem_support_iff`, followed by cast/absolute-value zero normalization.
[Native type, original proof, replay and axioms](../evidence/Roth.normOne_eq_sum_of_support_subset/native-target-success.json).

## Phase 2 — Size and one-line test

**SMALL**: an elementary support-padding identity, neither a main named theorem nor
a new mathematical object. The exhaustive search width is unaffected.
The definition-only one-line/exemption test is **n/a: theorem**.
Its one-line source proof is assessed through actual search and specialization,
not rejected merely for being short.

## Phase 3 — Exhaustive literature protocol

Each named channel was actually checked; three distinct general-web queries used
the specific form, abstract form and length alias. Optional `ask_chatgpt_math`
is unavailable; no external mathematical second opinion is claimed.
Only exact requests, original response hashes/byte counts, safe URL locators and
original concise summaries are retained. Full web/article bodies are not archived;
all returned URL query parameters were removed before archival.

| Channel | Actual query / locator | Finding and limitation |
|---|---|---|
| General web, specific | `polynomial coefficient l1 norm padding zero coefficients support finite sum` | Coefficient-vector padding context; primary coding-theory text located. |
| General web, abstract | `finitely supported function sum finite superset support zero terms` | Harrison's primary formal-summation paper and finite-support sum law context. |
| General web, aliases | `polynomial length sum absolute coefficients adding zero coefficients` | Length/coefficient ℓ¹ terminology; do not confuse polynomial degree, module length or root norms. |
| Optional ChatGPT math | n/a: `ask_chatgpt_math` unavailable | Remaining channels still executed fully. |
| Local primary source | `clean.tex:437–497`, §3 Lemma3 | Defines coefficient ℓ¹ sum and explicitly pads monomial expansion by zero terms. |
| nLab | `site:ncatlab.org/nlab finite sum support zero` | Indexed “support of a function”: pointed coefficient set and nonzero locus. Direct page access failed400 unsupported XHTML; indexed definition only. |
| nCatLab | `site:ncatlab.org/ncatlab finitely supported functions sum` | Returned nLab direct-sum/zero material, no separate categorical padding theorem. A proposition about finite scalar sums needs no categorical universal property. |
| Stacks | `site:stacks.math.columbia.edu polynomial finite support coefficients sum` | Algebra PDF returned; literal `finite support` find had no match, polynomial-ring find matched unrelated UFD/formal-smoothness material. No exact norm-padding result established; not evidence of absence. |
| MathOverflow | `site:mathoverflow.net polynomial coefficient l1 norm zero padding`; follow-up `site:mathoverflow.net "polynomial" "l1" "coefficients"` | First query no positive exact hit;465899 defines integer coefficient-vector ℓ¹ norm, supplementary terminology only. Circle-integral L¹ norms are different objects. |
| Recent arXiv | `site:arxiv.org polynomial "length" "coefficients" "norm" after:2021-10-27 before:2026-10-28`; exact2207.08915 follow-up | Broad result set alone is inconclusive. Direct Houben–Streng2022 source confirms complex coefficient ℓ¹ sum within the required five-year window. |

[Three web forms](../evidence/Roth.normOne_eq_sum_of_support_subset/web-0.json),
[domain channels](../evidence/Roth.normOne_eq_sum_of_support_subset/web-1.json),
[recent/source search](../evidence/Roth.normOne_eq_sum_of_support_subset/web-2.json),
[direct access](../evidence/Roth.normOne_eq_sum_of_support_subset/web-3.json),
[primary locators](../evidence/Roth.normOne_eq_sum_of_support_subset/web-4.json),
[exact follow-ups](../evidence/Roth.normOne_eq_sum_of_support_subset/web-5.json),
[refined locators](../evidence/Roth.normOne_eq_sum_of_support_subset/web-6.json),
[local reference excerpt](../evidence/Roth.normOne_eq_sum_of_support_subset/local-literature.txt),
[local reference hash](../evidence/Roth.normOne_eq_sum_of_support_subset/local-literature-source.json).

Primary mathematical anchors:
[Harrison, Formalizing WZ](https://www.cl.cam.ac.uk/~jrh13/papers/wz.pdf),
§2.2 printedp226/PDFp4 lines180–185, treats sums of functions vanishing outside finite sets;
the finite support makes unrestricted summation meaningful.
[Guruswami–Rudra–Sudan, Essential Coding Theory,2023](https://cse.buffalo.edu/faculty/atri/courses/coding-theory/book/prev-ver/web-coding-book-Oct3-2023.pdf),
Appendix polynomial addition, printedp509/PDFp524 lines30873–30888, pads coefficient
vectors by zeros before adding.
[Houben–Streng, Generalized class polynomials,2022](https://arxiv.org/pdf/2207.08915),
§3.2 PDFp5 lines251–253, defines the coefficient ℓ¹ sum for complex polynomials.
The first two sources justify the padding/summation interpretation; the third fixes
which polynomial norm is intended. None is asserted to state this exact Lean lemma.

**Literature synthesis:** this is zero-padding invariance of coefficient length/ℓ¹
aggregation. The generic mathematical reason is the additive identity, not polynomial
multiplication, positivity, completeness or convergence. Integer and complex coefficient
formulations agree after choosing the appropriate absolute value. Abstractly, any
zero-preserving indexed size into an additive commutative monoid admits the same law.
This abstract formulation is directly verified rather than attributed verbatim to a
source that only discusses real/complex sums. No historical-evolution claim is inferred
from publication dates or the missing optional channel.

## Phase 4a — All parameters and hypotheses

| Parameter / structure | Current form | Generality assessment |
|---|---|---|
| Universe and variables | `σ : Type*` | Already arbitrary; no Fintype/Finite hypothesis to remove. |
| Polynomial `P` | `MvPolynomial σ ℤ` | Fixed parent interface. Expanded formula works on arbitrary `ι →₀ R` with `Zero R`; polynomial algebra is unused. |
| Coefficients | Integers cast to real | Required by the fixed parent; expanded coefficient-norm statement compiles for `SeminormedCommRing R` (sufficient, not claimed minimal). |
| Exponent set `s` | Finite set of monomial exponents | Essential finite summation representation; arbitrary Finsupp index also works. No finite ambient variable universe required. |
| Inclusion `hs` | `P.support ⊆ s` | Needed for this unrestricted claim: omitting it loses nonzero terms. Native counterexample verified. |
| Target values | Real absolute values | Generic target needs only `AddCommMonoid S`; no order or norm axiom is used in padding. |
| Size behavior at zero | Implicit cast/abs zero laws | Generic indexed size requires zero preservation on `s`; can be weakened further to added positions only. Cannot drop all zero behavior. |
| Other assumptions | None | No unused instance or explicit binder to delete. |

## Phase 4b — Verified generality

**MAXIMALLY GENERAL relative to the fixed `Roth.normOne` interface**: its sole
support hypothesis is needed and there are no instance assumptions to weaken.
The expanded formula is **STRICTLY NARROWER THAN the standard abstract padding law**,
but that law already exists in mathlib. This is not a new theorem-only weakening ticket.

The existing generic law, independently compiled with the support-local zero premise:

```lean
theorem supportLocal {ι R S : Type*} [Zero R] [AddCommMonoid S]
    (f : ι →₀ R) (s : Finset ι) (hs : f.support ⊆ s) (size : ι → R → S)
    (hsize : ∀ i ∈ s, size i 0 = 0) : f.sum size = ∑ i ∈ s, size i (f i) :=
  Finsupp.sum_of_support_subset f hs size hsize
```

An exploratory stronger generalization `addedOnly` needs zero preservation only on
`s ∖ f.support`; it also compiled using `Finset.sum_subset`.
This helper is a new proof, not an existing named replacement. The sufficient
support-local hypothesis above is not claimed minimal. The native coefficient-norm
version over `SeminormedCommRing R` also compiled. Cost: **CHEAP** for the expanded
formula; replacing the parent representation throughout its API is separate work.
No cost-based verdict downgrade is used.
[Exact raw generalizations and two counterexamples](../evidence/Roth.normOne_eq_sum_of_support_subset/native-raw-executed.lean.txt),
[raw receipt](../evidence/Roth.normOne_eq_sum_of_support_subset/native-raw-success.json),
[norm-coefficient source](../evidence/Roth.normOne_eq_sum_of_support_subset/native-extra-executed.lean.txt),
[norm receipt](../evidence/Roth.normOne_eq_sum_of_support_subset/native-extra-success.json),
[generality summary](../evidence/Roth.normOne_eq_sum_of_support_subset/generality.json).

## Phase 4c — All nine modern-idiom checks

| # | Question | Assessment / reformulation / downstream consequence |
|---|---|---|
| 1 | Bundled hypotheses to classes | No custom bundled structure. The abstract statement already uses Zero and AddCommMonoid instances; containment remains a proposition. |
| 2 | Sequences/metrics to filters | No topology, limit or sequence argument. |
| 3 | Construction to universal property | A sum equality, not an object construction. |
| 4 | Closure sets to bundled substructures | No closure predicate or ideal/submodule to bundle. |
| 5 | Field/vector hierarchy weakening | Yes for expanded formula: arbitrary Zero coefficients and additive target. Normed-ring multiplication is unnecessary for the generic law. Enables arbitrary finite coefficient statistics preserving zero. |
| 6 | Higher-category formulation | No categorical coherence data in this finite equality. |
| 7 | Concrete indices/values | Exponent index becomes arbitrary `ι`, real target arbitrary additive commutative monoid. Supports non-polynomial Finsupp aggregations without new wrappers. |
| 8 | Concrete-via-abstract diagnostic | Fires: proof-body occurrences of `normOne`, `MvPolynomial`, `P` are each zero; support vanishing and finite-sum extension do all the work. Existing Finsupp law is the abstract restatement. |
| 9 | False-generalization guard | Preserve zero behavior and support containment; native `zeroSizeNecessary` and `containmentNecessary` refute removing them. Arbitrary size is an aggregation, not automatically a norm; topological support/pointwise polynomial L¹ are different objects. |

Modern idiom is available **already in mathlib**. It improves organization by using
Finsupp's support-padding API. It does not require a new global norm instance or
categorification. The `addedOnly` diagnostic preserves content but supplies no reason
to propose an upstream API addition for this target.

## Phase 4.5 — Infrastructure risk

All six risk rows (typeclass diamond, reducibility leak, noncanonical unfolding,
instance priority, universe-polymorphism of new data, coercion ambiguity) are
**n/a: theorem**. A proof in Prop introduces no definition, instance or coercion path.
No new norm structure on multivariate polynomials is installed or assumed.

## Phase 4.6 — All five proof-strategy checks

| # | Check | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a: finite algebraic equality. |
| 2 | Elements versus subobjects | No ideal/submodule relation. Apply existing support-padding law directly. |
| 3 | Sequences versus nets | n/a: no convergence or infinite summation needed. |
| 4 | Construction versus universal property | n/a: no categorical object is constructed. |
| 5 | Helpers mathlib should have | None missing for this theorem: generic padding and zero normalization already exist. |

Current mathematical strategy **MATHLIB-IDIOMATIC**: discard only zero added terms.
The proof can use the existing Finsupp specialization directly, avoiding a project
wrapper upstream. This is a CHEAP API simplification, not a different mathematical proof.

## Phase 5 — All five search methods, all three forms

| Method | Current coefficient sum | Literature coefficient length / zero padding | Abstract finite support |
|---|---|---|---|
| Lean-Finder | `MvPolynomial.sum_def`, univariate `Polynomial.sum_eq_of_subset`, monomial sum candidates. | Hamming norm and module length are near misses, not coefficient ℓ¹. | Exact `Finsupp.sum_of_support_subset` positive hit. |
| Loogle | `Finset.sum, abs, Finset.Subset` rejected unknown identifier; actual retry `Finset.sum, abs` gives inequalities, not padding. | `Finsupp.sum, Finset.sum` includes exact generic padding. | `"sum_of_support_subset"` returns Finsupp and related dependent/finite-sum laws. |
| LeanSearch | Univariate polynomial padding and multivariate sum definition. | Exact Finsupp padding and finite-type/finite-sum variants. | Exact Finsupp support-padding signature. |
| Source rg | No separate mathlib spelling `normOne_eq_sum_of_support_subset`. | Univariate sum padding/normalization checked in standard polynomial files. | Generated additive theorem at Finsupp Basic56–61 and Finset Basic202–206. |
| Local name search | Project theorem found. | `sum_of_support_subset` empty. | `Finset.sum_subset` empty. All three report index **unavailable**; empty results establish no absence. |

[Complete raw formal requests/receipts](../evidence/Roth.normOne_eq_sum_of_support_subset/formal-search.json),
[current source search](../evidence/Roth.normOne_eq_sum_of_support_subset/rg-current.json),
[literature source search](../evidence/Roth.normOne_eq_sum_of_support_subset/rg-literature.json),
[abstract source search](../evidence/Roth.normOne_eq_sum_of_support_subset/rg-abstract.json),
[untruncated full-name search](../evidence/Roth.normOne_eq_sum_of_support_subset/rg-full-name.json),
[pinned Finsupp source](../evidence/Roth.normOne_eq_sum_of_support_subset/mathlib-finsupp-basic.lean.txt),
[pinned MvPolynomial source](../evidence/Roth.normOne_eq_sum_of_support_subset/mathlib-mvpolynomial-basic.lean.txt),
[pinned Finset source](../evidence/Roth.normOne_eq_sum_of_support_subset/mathlib-finset-basic.lean.txt),
[pinned polynomial source](../evidence/Roth.normOne_eq_sum_of_support_subset/mathlib-polynomial-basic.lean.txt),
[source hashes](../evidence/Roth.normOne_eq_sum_of_support_subset/mathlib-inputs.json).

The additive Finsupp and Finset declarations are generated by `to_additive` from
multiplicative source, so literal theorem-name search alone would miss them.
Pinned native signature, not external-index wording/version, establishes compatibility:

```lean
@Finsupp.sum_of_support_subset :
  ∀ {α : Type u} {M : Type v} {N : Type w} [Zero M] [AddCommMonoid N]
    (f : α →₀ M) {s : Finset α}, f.support ⊆ s →
    ∀ (g : α → M → N), (∀ i ∈ s, g i 0 = 0) →
      f.sum g = ∑ x ∈ s, g x (f x)
```

Conclusion: **found in mathlib in more general form**. `Polynomial.sum_eq_of_subset`
is only an analogous univariate law. `MvPolynomial.sum_def` identifies the support
formula; the exact old target accepts the Finsupp theorem directly via the coefficient
Finsupp representation, without a proved bridge lemma.

## Phase 5.5 — All three statement-shape checks

1. **Normal form:** `normOne P = ∑ d ∈ s, …` is a useful rewriting orientation,
   putting the chosen finite-sum expression on the RHS. Equivalent forms are the
   coefficient Finsupp sum and direct support Finset sum; the canonical general law
   is `Finsupp.sum_of_support_subset`. This is no orthogonal equivalence network.
2. **Syntactic generality:** implicit `P,s` inferred from containment makes both
   monomial and union-support rewrites convenient. The generic indexed-size form
   was actually attempted and compiled; its explicit size function avoids an
   inference failure through `normOne`. No benefit established from bundling a
   norm object or changing the local equality to an inequality.
3. **Superfluous arguments:** none. `σ,P,s` occur in the conclusion;
   `hs` excludes missing nonzero terms. No explicit instance binder can be dropped.
   Native counterexamples certify that zero preservation in expanded forms and
   support containment cannot both be ignored.

Shape verdict: **SHIP-AS-STATED locally**, with the existing generic Finsupp law as
upstream canonical form. Expanded restatements are not new upstream candidates.

## Phase 6.0 — Every explicit caller and inline audit

| Caller | Exact applications | Complete replacement plan |
|---|---|---|
| `Roth.normOne_monomial`, CoeffNorm59–62 | One rewrite at61 with `support_monomial_subset` | Instantiate Finsupp padding at `(monomial e c).coeff`, explicit absolute-value size, and the same containment proof; keep final simp. |
| `Roth.normOne_add_le`, CoeffNorm77–83 | Three rewrites79–81 for sum, left/right union inclusions | Instantiate Finsupp padding at `(P+Q).coeff`, `P.coeff`, `Q.coeff`; use `support_add`, `Finset.subset_union_left/right`; keep sum distribution and coefficientwise `abs_add_le`. |

Two distinct named consumers, four source applications, zero consumers outside the
declaring file. These are explicit source references, not opaque kernel or simp
dependency closure. Both **entire proof bodies** were freshly compiled using the
fresh `viaFinsupp` replacement for all four rewrites; the new proof bodies do not
call the assessed project target. The scratch helper is solely an experiment,
not a proposed new upstream wrapper.

The repository-wide inline audit found no independent full normOne-padding identity
bypassing the lemma. Other coefficient-vanishing uses in HasseDeriv, Separation,
Taylor, GenWronskian and MainLemma handle derivative/binomial coefficients,
denominator clearing, coefficient extraction or bounded-family membership;
they do not sum this coefficient absolute-value functional over a support superset.
This is useful project-local API, not dead code. No source deletion was performed.
[Callers metadata](../evidence/Roth.normOne_eq_sum_of_support_subset/callers.json),
[caller search](../evidence/Roth.normOne_eq_sum_of_support_subset/rg-callers.json),
[inline audit search](../evidence/Roth.normOne_eq_sum_of_support_subset/rg-inline.json),
[entire consumer proofs](../evidence/Roth.normOne_eq_sum_of_support_subset/native-consumers-executed.lean.txt),
[consumer receipt](../evidence/Roth.normOne_eq_sum_of_support_subset/native-consumers-success.json).

## Phase 6 — Exact specialization and composition

The exact old-interface one-line specialization compiled in the target session:

```lean
Finsupp.sum_of_support_subset P.coeff hs (fun _ z ↦ |(z : ℝ)|) (by simp)
```

Here the support/sum representation is definitionally compatible, but zero
normalization is **not** definitional. The isolated mathlib-only proof makes every
mathematical fact explicit:

```lean
Finsupp.sum_of_support_subset P.coeff hs (fun _ z ↦ |(z : ℝ)|)
  (fun _ _ ↦ (congrArg abs (Int.cast_zero : ((0 : ℤ) : ℝ) = 0)).trans abs_zero)
```

Three named mathematical facts: `Finsupp.sum_of_support_subset`, `Int.cast_zero`,
`abs_zero`. Equality transport/congruence are structural operations.
The raw statement uses `P.coeff.sum` because Roth is deliberately absent; the native
old-interface check separately proves that this term has exactly the required type.
The raw `#check_failure Roth.normOne_eq_sum_of_support_subset` succeeds, so the proof
cannot be circular through its own imported theorem. No broad terminal simp proof is
being used as unexamined composition evidence.
[Exact target source](../evidence/Roth.normOne_eq_sum_of_support_subset/native-target-executed.lean.txt),
[exact isolated source](../evidence/Roth.normOne_eq_sum_of_support_subset/native-raw-executed.lean.txt),
[isolated receipt](../evidence/Roth.normOne_eq_sum_of_support_subset/native-raw-success.json).

## Phase 7 — Verdict and action

**NO-mathlib-has-it**. This classification uses the command's explicit allowance for
an existing *more general result* with a one-line specialization. Finsupp's existing
theorem is already the same support-padding law; specializing its coefficient size to
real absolute value supplies the original result. Its zero premise is discharged by
the two named normalization facts above. This is not a claim that the exact project
spelling exists, or that the entire old expression is definitionally equal without
normalization.

Composition conclusion: **COMPOSABLE**, using the three named mathematical facts
shown in Phase6. The existing-result
bucket is more precise here because the principal existing theorem is the whole
abstract support-padding law, rather than separate unrelated properties that happen
to assemble the conclusion. The parent `Roth.normOne` was assessed NO-composable;
**no Mode B parent re-aim override or inherited verdict is used**.
No new padding API, reviewer-selection task, PR title or upstream file addition is needed.

Exact old-interface specialization (the native `viaFinsupp` theorem uses this body):

```lean
example {σ : Type*} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)}
    (hs : P.support ⊆ s) : Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)| :=
  Finsupp.sum_of_support_subset P.coeff hs (fun _ z ↦ |(z : ℝ)|) (by simp)
```

Existing declaration location: `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:56–61`
(the additive theorem is generated from `prod_of_support_subset`).

Recommended cleanup: replace all four applications and then delete the project wrapper.
Use `Finsupp.sum_of_support_subset` with the explicit size function and
zero normalization at each of the four listed applications during a separately
authorized source refactor. Alternatively retain this convenience in
`Roth/CoeffNorm.lean` as the local destination while the parent norm interface remains.
A read-only upstream assessment does not itself require removing useful local API.

## Phase 8 — Verification and package

Four accepted native sets: original target/type/proof/specialization, both complete
consumers, isolated exact/generic padding and counterexamples, and coefficient-norm
extension. Each completed successfully with no errors, warnings, timeout, failed
dependencies or partial result; axioms are confined to `propext`,
`Classical.choice`, `Quot.sound`. The persistent receipts retain the original full
diagnostics/context and execution path, while the exact appended snippets are archived.
The isolated receipt's expected unknown-identifier diagnostic is informational under
`#check_failure`.

Two preparation attempts are retained separately: target size-placeholder inference
failed, fixed by an explicit size function; raw norm notation was unavailable under
stable imports, fixed by moving that extra theorem to the loaded persistent session.
Neither rejected attempt is accepted evidence. No sorry, new axiom, unsafe tactic,
native_decide or raised limit appears in accepted proof snippets.
[Verification](../evidence/Roth.normOne_eq_sum_of_support_subset/verification.json),
[assessment](../evidence/Roth.normOne_eq_sum_of_support_subset/assessment.json),
[overview entry](../evidence/Roth.normOne_eq_sum_of_support_subset/overview-entry.json),
[portable read-only validator](../evidence/Roth.normOne_eq_sum_of_support_subset/validate.py),
[copy manifest](../evidence/Roth.normOne_eq_sum_of_support_subset/copy-manifest.json).

All phases complete; unresolved checks: none. Root acceptance remains pending for
independent review before integration/publication.

