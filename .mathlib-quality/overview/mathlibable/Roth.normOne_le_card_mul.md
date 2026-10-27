# Roth.normOne_le_card_mul — NO-mathlib-has-it

Canonical declaration **87/293**, `Roth/CoeffNorm.lean:113–115`.

## Phase 0 — Baseline

Freshly hashed all 17 source/pin inputs against the shared manifest: all match.
The successful 2467-job baseline is reusable; production and pins remain unchanged.
[Input receipt](../evidence/Roth.normOne_le_card_mul/inputs.json); [baseline](../evidence/Roth.normOne_le_card_mul/baseline-build.txt).

## Phase 1 — Statement and proof

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ}, (∀ (d : σ →₀ ℕ), |((P.coeff d : ℤ) : ℝ)| ≤ B) → Roth.normOne P ≤ (P.support.card : ℝ) * B
```

The native full type and proof are in the [original receipt](../evidence/Roth.normOne_le_card_mul/native-original-success.json).
The sum of absolute coefficients has at most `P.support.card` summands, each at most B.
`normOne` unfolds definitionally to that exact finite sum. The only nondefinitional
transport is `nsmul_eq_mul`; the mathematical proof is a single existing theorem.
Full [declaring module](../evidence/Roth.normOne_le_card_mul/source-module.lean.txt) and its one explicit caller were read.

## Phase 2 — Size and one-liner test

**SMALL**: one proof line, elementary finite-sum comparison. Not a private/pre-filter skip.
Definition-only one-liner exemption n/a: this is a theorem. A short proof here signals an
existing generic specialization, independently checked rather than inherited.

## Phase 3 — Exhaustive literature

| Channel | Actual request / locator | Result |
|---|---|---|
| Specific web | polynomial coefficient l1 norm support cardinality maximum coefficient bound | Polynomial length/height terminology; sparse norm connection |
| General web | finite sum bounded by number of summands times maximum inequality | Standard finite-sum bound |
| Alias web | l1 l infinity norm inequality sparse support cardinality | Same sparse ℓ¹ ≤ cardinality × ℓ∞ estimate |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Optional channel unavailable |
| Local clean.tex | §3 proof Lemma 3, lines 437–497 | Padding monomials and norm estimate; no extra algebraic requirement |
| nLab | finite sum norm bound cardinality Hölder | Norm/p-norm context; direct Hölder page fetch failed HTTP400 unsupported XHTML |
| nCatLab | site:ncatlab.org/ncatlab norm finite sum inequality | No exact categorical law located; scalar ordered finite sum needs no categorical reformulation |
| Stacks | polynomial coefficients norm bound sum; tag 00H2 opened | Integral polynomial definition unrelated to the bound |
| MathOverflow | polynomial length height sum coefficients norm; question 199752 opened | Height is maximum absolute coefficient, related context; no strengthening |
| Recent arXiv | date-bounded coefficient length height norm, 2021-10-27 through 2026-10-27 | 2310.09704, 2404.06446, 2512.16220 concern heights; no exact stronger law established |

Exact requests, response hashes/byte counts, URLs, access status and concise original summaries
are retained without full response bodies in web-0 through web-6.
[General searches](../evidence/Roth.normOne_le_card_mul/web-0.json); [domains](../evidence/Roth.normOne_le_card_mul/web-1.json);
[Stacks](../evidence/Roth.normOne_le_card_mul/web-2.json); [MO](../evidence/Roth.normOne_le_card_mul/web-3.json); [recent initial](../evidence/Roth.normOne_le_card_mul/web-4.json);
[primary opens](../evidence/Roth.normOne_le_card_mul/web-5.json); [domain/date refinement](../evidence/Roth.normOne_le_card_mul/web-6.json);
[local source](../evidence/Roth.normOne_le_card_mul/local-literature.txt).

Primary positive locator: Mert Pilanci, *Fast Randomized Algorithms for Convex Optimization
and Statistical Estimation* (2016), §6.6, printed p.189, explicitly relates ℓ¹,
support cardinality and maximum coordinate ([Berkeley dissertation](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-147.pdf)).
Concept: finite sum bounded by number of terms times an upper bound; polynomial length/height
is one specialization. The general finite-family formulation removes polynomial arithmetic;
no disagreement in mathematical meaning. Search limitations above do not prove absence.

## Phase 4a — Every parameter

| Parameter | Assessment |
|---|---|
| σ : Type* | Already arbitrary; no finiteness or decidable equality hypothesis |
| P : MvPolynomial σ ℤ | Fixed normOne interface; polynomial operations unused by proof |
| B : ℝ | Arbitrary; positivity is unnecessary |
| hB global | Can weaken to ∀ d ∈ P.support, absolute coefficient ≤ B |

## Phase 4b — Verified generality

**STRICTLY NARROWER THAN STANDARD**: support-only hypothesis and arbitrary ordered additive
commutative monoid forms both compile. These are existing generalizations, so the verdict is
NO-mathlib-has-it, not a request to upstream another general theorem.
[Raw mathlib-only source](../evidence/Roth.normOne_le_card_mul/native-raw-executed.lean.txt) imports 13 stable mathlib modules,
guards the project name with #check_failure, and verifies `polynomialSupport` / `abstractBound`.
[Raw receipt](../evidence/Roth.normOne_le_card_mul/native-raw-success.json). Fixed-parent exact spelling is also verified
by `supportWeakening` in the [caller source](../evidence/Roth.normOne_le_card_mul/native-consumers-executed.lean.txt).
The empty support allows arbitrary negative B under the weaker hypothesis, correctly yielding
0 ≤ 0. No positivity premise should be introduced. The original global hB implies 0 ≤ B,
but that implication is not needed by the estimate. No weakening beyond actual compiled forms
is claimed; no cost-based verdict reasoning.

## Phase 4c — Modern idioms

| # | Question | Finding |
|---|---|---|
| 1 | Typeclasses | yes: abstract codomain AddCommMonoid/Preorder/AddLeftMono, native verified; no custom condition class needed |
| 2 | Filters/nets | no: finite sum, no limits |
| 3 | Universal properties | no: inequality, no constructed object |
| 4 | Bundled substructures | no: arbitrary finset is appropriate |
| 5 | Hierarchy weakening | yes: no field/ring/norm laws needed for bound; abstract native theorem |
| 6 | Higher categories | no: no categorical content |
| 7 | Concrete indices | already arbitrary σ; exponents may be any finite index set in existing generic law |
| 8 | Concrete-via-abstract | yes: single proof line has no polynomial multiplication; after normOne unfolding only support finset and summand function remain. Zero subsequent normOne occurrences. Existing generic law supplies entire result |
| 9 | False-generalization guard | PASS: instantiate s=P.support, f=absolute real cast coefficient; no object meaning changes. Do not confuse sum of norms with norm of polynomial or norm of sum |

Modern idiom available: yes, already mathlib's abstract finite-family ordered sum theorem.
It handles signed summands and arbitrary indices without polynomial or norm structure and
composes directly with support/finite-family arguments. No additional upstream modernization
is identified. Q8 fires after definition unfolding; Q9 preserves the original coefficient sum.

## Phase 4.5 — Infrastructure risks

Theorem n/a for each of diamonds, definitional equality, instance search, coercions,
reducibility and universe inference: no new definition or instance is proposed.

## Phase 4.6 — Proof strategy

| Question | Finding |
|---|---|
| Topology filters | n/a: no topology |
| Algebra inclusions | n/a: no ideals/submodules |
| Analysis nets | n/a: finite summation only |
| Universal property | n/a: no object construction |
| Missing helper API | no: existing Finset.sum_le_card_nsmul is sufficient |

Current strategy **MATHLIB-IDIOMATIC**: finite-sum bound directly. Inline in caller to avoid
public wrapper; no new helper lemma is required.
[Generality/idiom evidence](../evidence/Roth.normOne_le_card_mul/generality.json).

## Phase 5 — Five actual mathlib methods

| Method | Current / standard / abstract results |
|---|---|
| Finder | Current search broad polynomial hits; standard and abstract return Finset.sum_le_card_nsmul |
| Loogle | Name query finds generated Finset/Multiset/List laws; multiplication-shaped standard search broader; abstract sum/nsmul hits exact Finset theorem |
| LeanSearch | Current coefficient API context; standard and abstract hit Finset.sum_le_card_nsmul |
| rg | Current-name mathlib search empty; standard norm files and abstract finite-sum source inspected; exact generated name found via to_additive |
| local | Actual three requests; project target found, but all report index unavailable; empty standard/abstract results are inconclusive |

[12 raw formal receipts](../evidence/Roth.normOne_le_card_mul/formal-search.json); [current rg](../evidence/Roth.normOne_le_card_mul/rg-current.json);
[standard rg](../evidence/Roth.normOne_le_card_mul/rg-literature.json); [abstract rg](../evidence/Roth.normOne_le_card_mul/rg-abstract.json);
[untruncated full-name rg](../evidence/Roth.normOne_le_card_mul/rg-full-name.json). Finder/LeanSearch external signatures
use PartialOrder; pinned native signature is weaker Preorder and authoritative:

```lean
Finset.sum_le_card_nsmul {ι N : Type*} [AddCommMonoid N] [Preorder N] [AddLeftMono N]
  (s : Finset ι) (f : ι → N) (B : N) (h : ∀ x ∈ s, f x ≤ B) :
  s.sum f ≤ s.card • B
```

Pinned source: `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:285–290`,
generated additively from `prod_le_pow_card`; [source](../evidence/Roth.normOne_le_card_mul/mathlib-source-0.lean.txt).
This is a positive presence conclusion, not absence inferred from searches.

## Phase 5.5 — Statement shape

1. Normal form: ≤ already oriented correctly; `card • B` is generic shape and `card * B`
is real specialization, with explicit nsmul_eq_mul transport verified.
2. Syntactic generality: global bound becomes support-local; retains existing support index
and parent normOne meaning. Arbitrary-family abstract version independently compiles.
3. Superfluous arguments: none among σ,P,B; global quantification stronger than necessary.
No hidden finite σ assumption. Overall generic API already has the correct shape.

## Phase 6.0 — Callers and inline audit

| Caller | Location | Refactor and native replay |
|---|---|---|
| Roth.abs_coeff_det_hasseDeriv_le | Roth/CoeffNorm.lean:270 | Introduce typed hsize by the exact Finset specialization below; replace target call by hsize; entire determinant proof replay succeeds |

Internal use count 1; external-file use count 0; declaration occurrence excluded.
Inline derivation audit: `abs_coeff_diag_le` also applies sum_le_card_nsmul after triangle
inequality; it does not call target. `abs_eval_le` uses pointwise sum comparisons. Full module
read and fresh repository searches provide explicit source-call coverage.
[Caller search](../evidence/Roth.normOne_le_card_mul/rg-callers.json); [inline search](../evidence/Roth.normOne_le_card_mul/rg-inline.json);
[caller metadata](../evidence/Roth.normOne_le_card_mul/callers.json).
Fresh runtime audit checks all 293 canonical declarations, 293 unique names, present=293,
values=293 and sole direct proof consumer Roth.abs_coeff_det_hasseDeriv_le. Array was generated
directly from tracked declaration-order.json, including private names via mkPrivateNameCore;
portable validator checks exact order, not only count. Kernel proof-constant audit is separate
from source explicit refs and is not a transitive simp dependency closure.

## Phase 6 — Direct specialization and composition

```lean
have hsize : normOne P ≤ P.support.card * B := by
  simpa only [Roth.normOne, nsmul_eq_mul] using
    P.support.sum_le_card_nsmul
      (fun d ↦ |((P.coeff d : ℤ) : ℝ)|) B (fun d _ ↦ hB d)
```

**FOUND EXISTING GENERAL THEOREM**: one existing mathematical call. This is not a closing
`simp [defs...]` composition whose substantive normalization premise is newly proved: normOne
unfolds directly to precisely `s.sum f`; nsmul_eq_mul only rewrites repeated addition as scalar
multiplication. Native target #print confirms the same single Finset application and that
transport. The support-only and abstract proofs require no project theorem, new helper,
coefficient transport, or newly established norm identity. No Mode B parent re-aim override:
normOne's prior NO-composable assessment is not inherited. Direct generic theorem hit is
independently established for this law, unlike earlier binary coefficient norm bridges.
[Complete caller replay and audit receipt](../evidence/Roth.normOne_le_card_mul/native-consumers-success.json).
All accepted probes use standard axioms only; no sorry, axiom additions, unsafe, native_decide,
raised limits, partial response or rejected attempt.

## Phase 7 — Verdict and action

**NO-mathlib-has-it**. Existing Finset.sum_le_card_nsmul is strictly more general and proves
this target by direct specialization with representation/notation normalization only.
At the sole caller `Roth.abs_coeff_det_hasseDeriv_le`, add typed local hsize above and replace
`normOne_le_card_mul P hB` by hsize, leaving the surrounding trans and degree/cardinality bound.
The entire caller was compile-checked with this exact edit. Then delete the public wrapper.
Alternative destination if preserving exposition: source-paper explanation or module docstring
in project-local `Roth/CoeffNorm.lean`; no separate Archive theorem or new upstream API needed.
No future upstream question is required for this independently positive generic match.
This read-only assessment makes no production edit. YES PR grouping/reviewer selection n/a.

## Phase 8 — Verification and handoff

All mandatory phases PASS or theorem n/a; unresolved []. Three clean native sets preserve exact
executed sources and complete raw receipts: original target/type, isolated raw generalization,
full caller/audit. [Verification](../evidence/Roth.normOne_le_card_mul/verification.json);
[current manifest](../evidence/Roth.normOne_le_card_mul/copy-manifest.json); [portable validator](../evidence/Roth.normOne_le_card_mul/validate.py).
Root acceptance pending; root owns acceptance and integration.
