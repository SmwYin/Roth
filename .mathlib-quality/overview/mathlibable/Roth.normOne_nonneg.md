# Mathlibable assessment — `Roth.normOne_nonneg`

Canonical declaration **77/293**, `Roth/CoeffNorm.lean:50–51`. Verdict:
**NO-composable-from-mathlib**. The exact theorem is an application of two existing facts,
`Finset.sum_nonneg` and `abs_nonneg`. This is independently verified below, rather than
inherited from the earlier assessment of the parent definition.

## Phase 0 — Baseline and resolution

The saved successful baseline is `lake build` (2467 jobs), commit
`99f19fda4b3cbee38fc0d31af76075834f5cc265`. All seventeen production-source/toolchain/dependency
pin hashes freshly match it. [Baseline](../evidence/Roth.normOne_nonneg/baseline-build.txt),
[inputs](../evidence/Roth.normOne_nonneg/inputs.json),
[hash check](../evidence/Roth.normOne_nonneg/input-hash-check.json).
Production files, pins, Git state, progress and overview were not modified by this assessment.
The native target check resolves, prints and audits the original theorem; no editor acceptance
or unexecuted proof is substituted for kernel validation.

## Phase 1 — Mathematical statement and proof

Full native type (universe label normalized):

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ), 0 ≤ Roth.normOne P
```

`normOne P` is the finite sum of the absolute values of the real-cast integer coefficients
on `P.support`. Every term is nonnegative, and a finite sum of nonnegative terms is nonnegative.
Neither polynomial multiplication nor finiteness of the entire variable type is involved.
The parent definition is the only project dependency; the proof body uses two mathlib facts.
The whole declaring module, including the two consumers, was read.
[Module](../evidence/Roth.normOne_nonneg/source-module.lean.txt),
[native original type/proof/axioms](../evidence/Roth.normOne_nonneg/native-target-success.json).

## Phase 2 — Size and one-line test

**SMALL**: elementary positivity of a finite coefficient sum. This is a narrative description,
not the reason for the verdict. Phase 2b's definition-only one-line/definitional-abuse gate is
**n/a: theorem, not an object-producing definition**. It happens to have a one-line term proof;
its two consumers justify a useful local convenience but do not supply new upstream mathematics.
No infrastructure exemption is needed or asserted for the theorem.

## Phase 3 — Exhaustive literature assessment

The search protocol's named channels are all addressed. Requests, original returned-response
SHA256 and byte counts are recorded; full search/article bodies are deliberately not archived.
No signed credential-bearing URLs are retained.

| Channel | Actual query or locator | Result and scope |
|---|---|---|
| General web, specific | `polynomial coefficient l1 norm nonnegative length sum absolute coefficients` | Coefficient-sum norm context; distinguish positivity of the norm from positivity of polynomial values. |
| General web, abstract | `finite sum nonnegative functions ordered additive monoid nonnegativity` | Generic finite-sum order law; direct formal-library sources returned. |
| General web, aliases | `polynomial length norm positivity sum absolute coefficients` | Length/coefficient norm terminology; roots of homogeneous forms called polynomial norms are a different object. |
| Optional mathematical second opinion | n/a: `ask_chatgpt_math` unavailable | No claimed second opinion or historical confirmation. |
| Local primary reference | `clean.tex:437–497`, §3 Lemma 3 coefficient ℓ¹ estimates | Same coefficient absolute sum and use in determinant estimates; nonnegativity is implicit in the definition, not a separate deep theorem. |
| nLab | `site:ncatlab.org/nlab p-norm nonnegative norm`; indexed `p-norm` and `norm` | p=1 finite/sequence sum of absolute values. Direct p-norm page fetch fails HTTP400 unsupported XHTML; indexed text only. |
| nCatLab | `site:ncatlab.org/ncatlab ordered monoid nonnegative sum` | Returned nLab monoid material, not a distinct categorical coefficient-norm theorem. No categorical construction is needed for the finite order law. |
| Stacks | `site:stacks.math.columbia.edu norm nonnegative coefficients polynomial` | No exact coefficient ℓ¹ replacement established; this scalar finite-sum order fact is not specific algebraic geometry. |
| MathOverflow | `site:mathoverflow.net polynomial coefficient l1 norm length` | Supplementary coefficient-vector norm discussions, not an independent primary proof of this theorem. |
| Recent arXiv, five-year window | `site:arxiv.org polynomial "length" "coefficients" "norm" after:2021-10-27 before:2026-10-28` | Broad result set not treated as an exact theorem; exact follow-up2207.08915 and direct primary PDF establish2022 coefficient-norm use. |

[Web requests0](../evidence/Roth.normOne_nonneg/web-0.json),
[domain channels1](../evidence/Roth.normOne_nonneg/web-1.json),
[recent/source searches2](../evidence/Roth.normOne_nonneg/web-2.json),
[direct access3](../evidence/Roth.normOne_nonneg/web-3.json),
[source locators4](../evidence/Roth.normOne_nonneg/web-4.json),
[recent exact definition5](../evidence/Roth.normOne_nonneg/web-5.json),
[local source excerpt](../evidence/Roth.normOne_nonneg/local-literature.txt),
[local source hash](../evidence/Roth.normOne_nonneg/local-literature-source.json).

Two primary sources anchor the mathematical interpretation:
[Evertse–Győry, Effective Results and Methods for Diophantine Equations](https://math.unideb.hu/sites/default/files/upload_documents/version-210614_0.pdf),
printed p67/PDF page86, §4.1 before(4.1.7), defines multivariate integer-polynomial length by
coefficient absolute sum. Nonnegativity follows termwise; the source does not advertise this
exact Lean theorem separately.
[Houben–Streng, Generalized class polynomials (2022)](https://arxiv.org/pdf/2207.08915),
§3.2, PDF page4 lines251–253, uses the sum for complex coefficients and contrasts it with
maximum coefficient size. This is within the requested five-year interval.

**Literature synthesis:** coefficient ℓ¹ norm/length is standard, for integer, real and complex
coefficients. More abstractly finite sums preserve nonnegativity in an ordered additive monoid.
These are compatible formulations, not evidence of a new integer-polynomial positivity API.
No historical-evolution claim is made from search-result dates or missing optional tools.

## Phase 4a — Parameters and generality

| Parameter/structure | Current form | Assessment and verified extension |
|---|---|---|
| Variables | arbitrary `σ : Type*` | Already universe-polymorphic; no finite-variable assumption to drop. |
| Polynomial | `P : MvPolynomial σ ℤ` | Needed to state the fixed parent `normOne`; not an explicit mathematical hypothesis. |
| Coefficients | integer, cast to real | Expanded formula works for arbitrary seminormed commutative rings using coefficient norms; native checked, not claimed minimal. |
| Values | real absolute values | Expanded finite-size formula works in any `S` with `AddCommMonoid`, `Preorder`, `IsOrderedAddMonoid`. |
| Index | exponent Finsupp type | Expanded aggregate works on arbitrary `ι →₀ R`, `Zero R`; no multiplication needed. |
| Sign input | supplied by absolute value | General size function needs only pointwise nonnegativity on actual support, not on every coefficient in the universe. |
| Other hypotheses | none | No Fintype, DecidableEq, nonzero, degree, positivity or cardinality binder can be removed. |

## Phase 4b — Generality verdict

**MAXIMALLY GENERAL relative to the fixed `Roth.normOne` interface**: no removable hypotheses
exist. The mathematical formula is **STRICTLY NARROWER THAN the generic finite-size form**
when its parent interface is expanded. This distinction prevents presenting a replacement of
`normOne` as a silent theorem-only assumption deletion.
The following exact expanded formulation compiled in fresh mathlib-only evidence:

```lean
theorem supportOnly {ι R S : Type*} [Zero R] [AddCommMonoid S] [Preorder S]
    [IsOrderedAddMonoid S] (f : ι →₀ R) (size : ι → R → S)
    (hsize : ∀ i ∈ f.support, 0 ≤ size i (f i)) : 0 ≤ f.sum size :=
  Finsupp.sum_nonneg hsize
```

The integer-coefficient specialization closes with `Finsupp.sum_nonneg` and `abs_nonneg`.
A norm-coefficient form over `[SeminormedCommRing R]` also compiled using
`Finset.sum_nonneg` and `norm_nonneg`; no minimality of this sufficient ring structure is claimed.
Cost: **CHEAP** specialization of existing abstractions. This does not create a YES candidate,
since the generic statement already exists as `Finsupp.sum_nonneg`.
[Fresh raw proof/generalization](../evidence/Roth.normOne_nonneg/native-raw-executed.lean.txt),
[receipt](../evidence/Roth.normOne_nonneg/native-raw-success.json),
[norm specialization](../evidence/Roth.normOne_nonneg/native-target-executed.lean.txt).

## Phase 4c — Modern mathlib idiom, all nine rows

| # | Question | Assessment | Concrete downstream consequence |
|---|---|---|---|
| 1 | Bundled hypotheses to classes | No extra bundled premise exists. Generic order assumptions already use classes. | Existing finite-sum order API applies directly. |
| 2 | Sequences/metrics to filters | No limit, topology or sequence argument. | No filter theorem to unify. |
| 3 | Construction to universal property | A proposition about a finite sum, not a construction. | No universal-property replacement needed. |
| 4 | Sets to bundled substructures | No closure predicate or substructure here. | None. |
| 5 | Field/vector hierarchy weakening | Yes for expanded coefficient formula, not the fixed integer parent signature. | Native coefficient-norm form permits any seminormed commutative ring. |
| 6 | Higher-categorical generality | No categorical content in this finite inequality. | None established. |
| 7 | Concrete indices/values | Exponent index can become arbitrary Finsupp index and real target an ordered additive monoid. | Existing `Finsupp.sum_nonneg` applies to size estimates beyond polynomial norms. |
| 8 | Concrete-via-abstract diagnostic | Fires: `normOne`, `MvPolynomial`, and `P` each occur in zero proof-body lines; body has only two generic facts with inferred arguments. | Abstract finite-sum nonnegativity already supplies the proof; exact raw replay confirms this diagnostic. |
| 9 | False-generalization guard | Arbitrary size functions need nonnegativity; arbitrary `Norm` data does not give norm axioms. | Verified support-local hypothesis preserves the inequality, without claiming every size is a norm or replacing L1 with supremum/pointwise positivity. |

Modern idiom is available and **already in mathlib**, not a new bundling ticket: use the finite
aggregate order API. Supremum/Gauss norm nonnegativity and Mahler measure nonnegativity found by
semantic search concern different objects and do not replace coefficient ℓ¹ nonnegativity.

## Phase 4.5 — Infrastructure risks

All six definition/class/instance risk rows are **n/a**: this declaration is a proof in `Prop`.
It creates no typeclass instance, coercion, universe-constrained data, foundational definition,
notation or competing computational path. The native arbitrary-universe Finsupp form is checked;
no new global norm instance on polynomials is installed or assumed.

## Phase 4.6 — Proof-strategy optimality, all five rows

| # | Question | Answer / cost |
|---|---|---|
| 1 | Topology ε–δ versus filters | n/a: finite algebraic inequality. |
| 2 | Element algebra versus subobject inclusions | n/a: no ideal/submodule relation; generic sum order law is direct. |
| 3 | Sequences versus nets | n/a: no convergence. |
| 4 | Explicit categorical construction versus universal property | n/a: no construction. |
| 5 | Missing helpers that should be in mathlib | No missing helper: `Finset.sum_nonneg`, `Finsupp.sum_nonneg`, `abs_nonneg` already suffice. |

Current strategy **MATHLIB-IDIOMATIC**. The shortest path is the proof already used. Inlining
at two consumer sites would remove an upstream wrapper, not improve the mathematical argument.

## Phase 5 — All five formal methods and all three forms

| Method | Current coefficient sum | Literature length/L1 form | Abstract finite sum |
|---|---|---|---|
| Lean-Finder | Gauss norm, spectral terms and Mahler measure candidates are distinct objects. | Same near misses, including coeffList.length (different length). | `Finset.sum_nonneg`, `Finsupp.sum_nonneg` positive hits. One returned informal Finsupp description incorrectly mentions cosine; formal type/native pinned source, not that description, is used. |
| Loogle | Literal free `p.support` query rejected as unknown identifier; retained, then actually retried with `Finset.sum, abs, (0 ≤ _)`. | `Finset.sum, (0 ≤ _)` returns finite nonneg facts. | Finset/Fintype sum nonneg positive hits. |
| LeanSearch | Absolute-sum and unrelated Gauss norm candidates. | lp norm and unrelated polynomial seminorm candidates. | Finset/Finsupp/finsum nonneg positive hits. |
| Source rg | Full exact names checked without truncation. No separate mathlib `normOne_nonneg` found. | Polynomial norm module confirms length terminology; maximum norm is different. | Pinned `Data/Finsupp/Order.lean:56–58` and generated Finset laws verified. |
| Local symbol/name search | Finds project target. | `sum_nonneg` finds Finsupp order laws. | `norm_nonneg` finds several domain-specific results; generic candidate separately native checked. Index reported **unavailable**, so these source-backed results establish presence only, not absence. |

[All raw formal requests/responses](../evidence/Roth.normOne_nonneg/formal-search.json),
[current rg](../evidence/Roth.normOne_nonneg/rg-current.json),
[literature rg](../evidence/Roth.normOne_nonneg/rg-literature.json),
[abstract rg](../evidence/Roth.normOne_nonneg/rg-abstract.json),
[untruncated full-name rg](../evidence/Roth.normOne_nonneg/rg-full-name.json).
External indexes use different snapshots; fresh Lean checks and pinned sources decide signature
compatibility. In particular pinned `Finsupp.sum_nonneg` has `Preorder`, and its zero-coefficient
size need not vanish. Pinned `Finset.sum_nonneg` is generated by `to_additive` near line151
(and a later ordered variant near746), which is why searching only literal `theorem` names
would miss it. No claim of global absence follows from any search.
[Finsupp source](../evidence/Roth.normOne_nonneg/mathlib-finsupp-order.lean.txt),
[Finset source](../evidence/Roth.normOne_nonneg/mathlib-finset-order.lean.txt),
[native generic signatures](../evidence/Roth.normOne_nonneg/native-consumers-success.json).

## Phase 5.5 — Statement shape

1. **Normal form:** `0 ≤ normOne P` is the canonical order orientation. Expanded coefficient sum
   and `P.coeff.sum` are definitionally the same integer functional; both exact two-call forms
   were checked. A `norm_nonneg P` proof needs an appropriate norm structure, which is not
   assumed for this project polynomial type.
2. **Syntactic generality:** explicit `P` makes the theorem usable as the positivity function
   argument required by `Finset.le_prod_of_submultiplicative_of_nonneg`. No unnecessary equality,
   existential witness, extra bound or coercion hypothesis obscures application.
3. **Unused assumptions:** none. Polynomial `P` occurs in the conclusion; universe-polymorphic
   `σ` is part of its type. The concrete coefficient/value types are parent-interface choices,
   not unused instance binders. The generalized support-local version was actually checked.

Verdict: statement shape is locally appropriate; generic upstream form already exists.

## Phase 6.0 — Callers and inline audit

| Caller | Exact location and use | Complete refactor plan |
|---|---|---|
| `Roth.normOne_prod_le` | CoeffNorm105–108, function argument at107 | Replace positivity argument by `fun P ↦ Finset.sum_nonneg (fun _ _ ↦ abs_nonneg _)`, inferred with target `0 ≤ normOne P`; preserve monomial and multiplication inputs. |
| `Roth.normOne_det_le` | CoeffNorm119–129, witness at128 | Replace norm positivity witness in `Finset.prod_le_prod₀` with the same two-call proof; use updated product theorem for the determinant permutation product. |

Both **entire proof bodies** were freshly replayed, not just caller type transports. The
scratch determinant explicitly uses the freshly replayed product estimate and fresh nonneg
proof. Other project helper estimates are imported dependencies, not falsely claimed replaced.
Two named consumers are in one file, zero outside; this is not a complete opaque-kernel
reference count. The target has no `[simp]` attribute. An inline audit found individual
absolute-value nonnegativity elsewhere, not a second proof of full normOne nonnegativity.
[Caller ledger](../evidence/Roth.normOne_nonneg/callers.json),
[caller grep](../evidence/Roth.normOne_nonneg/rg-callers.json),
[inline grep](../evidence/Roth.normOne_nonneg/rg-inline.json),
[full consumer proofs](../evidence/Roth.normOne_nonneg/native-consumers-executed.lean.txt),
[clean native receipt](../evidence/Roth.normOne_nonneg/native-consumers-success.json).

## Phase 6 — Exact composition

**COMPOSABLE**, no automation-based borderline judgment needed:

```lean
Finset.sum_nonneg fun _ _ ↦ abs_nonneg _
```

Two mathematical calls; lambda binders and implicit specialization are not new facts.
The same expansion in `P.coeff.sum` closes with `Finsupp.sum_nonneg` plus `abs_nonneg`.
These are fresh mathlib-only executions with `#check_failure Roth.normOne_nonneg` and no Roth
import. They neither call the assessed theorem nor rely on a project simp wrapper.
The abstract support-only version is one existing theorem call.
No failed native attempts, limits raised, unsafe proofs, new axioms or unproved placeholders.

## Phase 7 — Verdict and gates

**NO-composable-from-mathlib.** Evidence is the exact two-call proof, fresh isolated native
success, generic pinned theorem, both complete consumer replays, and full source/literature
protocol. Parent `Roth.normOne` was assessed NO-composable, not NO-mathlib-has-it, so Mode B's
special inherited re-aim rule is not being misapplied. One can regard generic Finsupp positivity
as the abstract existing law, but the current absolute-value specialization explicitly supplies
two facts; the composition bucket precisely records that mechanism.

No cost-based downgrade or unsupported absence assertion is used. The concrete-via-abstract
check exposes an **existing** general law, so it does not create a missing generic YES theorem.
All gates pass. No upstream PR title, reviewer selection or future API design question is needed
for this NO verdict. Alternative local destination: retain the existing semantic convenience
in `Roth/CoeffNorm.lean`; if a separate authorized refactor deletes it, use both caller plans.
The current survey keeps all production sources unchanged. This useful local lemma is not junk.

## Phase 8 — Verification and next action

Three fresh accepted native sets: original/replay/generality, both full consumers and pinned
signatures, isolated mathlib-only composition/support generalization. Axioms are restricted to
`propext`, `Classical.choice`, `Quot.sound`. Every native result is complete and clean;
prerequisite75 evidence was not relabeled as new77 verification. Source hashes, artifact hashes,
links, credential guard and completion schema are checked by the portable validator.
[Verification ledger](../evidence/Roth.normOne_nonneg/verification.json),
[assessment](../evidence/Roth.normOne_nonneg/assessment.json),
[portable validator](../evidence/Roth.normOne_nonneg/validate.py).
No unresolved verification or input-dependent decision remains. Root independently reviews and
publishes this completed declaration before advancing the canonical progress record.
