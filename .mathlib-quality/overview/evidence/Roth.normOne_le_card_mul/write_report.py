from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.normOne_le_card_mul'
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
modern=[('Typeclasses','yes: abstract codomain AddCommMonoid/Preorder/AddLeftMono, native verified; no custom condition class needed'),('Filters/nets','no: finite sum, no limits'),('Universal properties','no: inequality, no constructed object'),('Bundled substructures','no: arbitrary finset is appropriate'),('Hierarchy weakening','yes: no field/ring/norm laws needed for bound; abstract native theorem'),('Higher categories','no: no categorical content'),('Concrete indices','already arbitrary σ; exponents may be any finite index set in existing generic law'),('Concrete-via-abstract','yes: single proof line has no polynomial multiplication; after normOne unfolding only support finset and summand function remain. Zero subsequent normOne occurrences. Existing generic law supplies entire result'),('False-generalization guard','PASS: instantiate s=P.support, f=absolute real cast coefficient; no object meaning changes. Do not confuse sum of norms with norm of polynomial or norm of sum')]
strategy=[('Topology filters','n/a: no topology'),('Algebra inclusions','n/a: no ideals/submodules'),('Analysis nets','n/a: finite summation only'),('Universal property','n/a: no object construction'),('Missing helper API','no: existing Finset.sum_le_card_nsmul is sufficient')]
out('generality.json',dict(parameters=[dict(parameter='σ',status='arbitrary Type universe; no Fintype/DecidableEq assumption'),dict(parameter='P : MvPolynomial σ ℤ',status='fixed parent normOne interface; raw theorem generalises to arbitrary finite family in ordered additive commutative monoid'),dict(parameter='B : ℝ',status='no positivity needed; retained'),dict(parameter='hB : ∀ d, abs(coeff d) ≤ B',status='STRICTLY NARROWER: support-local bound sufficient; verified native supportWeakening')],modern_rows=modern,strategy_rows=strategy,infrastructure_rows=[dict(risk=k,status='n/a: theorem introduces no definition or instance') for k in ['Diamonds','Definitional equality','Instance search','Coercions','Reducibility','Universe inference']],expanded_forms=[dict(name='support-local hB',status='PASS',verified=True,native='MvPolynomial.NormCardConsumers.supportWeakening'),dict(name='abstract finite-family bound',status='PASS',verified=True,native='NormCardRaw.abstractBound')],future_questions=[]))
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem introduces no infrastructure'
out('assessment.json',dict(declaration=N,canonical_index=87,verdict='NO-mathlib-has-it',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True))
type='∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ}, (∀ (d : σ →₀ ℕ), |((P.coeff d : ℤ) : ℝ)| ≤ B) → Roth.normOne P ≤ (P.support.card : ℝ) * B'
out('overview-entry.json',dict(declaration=N,kind='theorem',type=type,what='Coefficient ℓ¹ sum bounded by support size times uniform coefficient bound.',how='Direct specialization of Finset.sum_le_card_nsmul; unfold normOne and rewrite nsmul_eq_mul.',hypotheses='Arbitrary variable type; integer coefficients and real bound fixed by normOne interface; global coefficient bound can weaken to support-only.',project_dependencies=['Roth.normOne'],caller_summary='One explicit caller Roth.abs_coeff_det_hasseDeriv_le at CoeffNorm.lean:270; full caller replay succeeds with inline Finset bound; canonical293 unique audit confirms sole direct proof consumer.',mathlib_api_audit='Finset.sum_le_card_nsmul at Algebra/Order/BigOperators/Group/Finset.lean:285 generated from prod_le_pow_card. Current native signature uses Preorder.',moral_duplications='Same scalar finite-family inequality independently used by abs_coeff_diag_le; exact target already duplicates existing generic Finset theorem.',generalization='Support-only hB and arbitrary AddCommMonoid/Preorder/AddLeftMono codomain compile; existing mathlib law covers both.',missing_api='No missing API required for this bound; broader coefficient norm representation issues do not obstruct this theorem.',junk='Thin wrapper with one caller; useful estimate, redundant public declaration.',action='NO-mathlib-has-it: inline Finset.sum_le_card_nsmul via local hsize in determinant caller and delete wrapper in separately authorized implementation. Keep source explanation in Roth/CoeffNorm.lean.'))
link=lambda f:'../evidence/'+N+'/'+f
r=f'''# Roth.normOne_le_card_mul — NO-mathlib-has-it

Canonical declaration **87/293**, `Roth/CoeffNorm.lean:113–115`.

## Phase 0 — Baseline

Freshly hashed all 17 source/pin inputs against the shared manifest: all match.
The successful 2467-job baseline is reusable; production and pins remain unchanged.
[Input receipt]({link('inputs.json')}); [baseline]({link('baseline-build.txt')}).

## Phase 1 — Statement and proof

```lean
{type}
```

The native full type and proof are in the [original receipt]({link('native-original-success.json')}).
The sum of absolute coefficients has at most `P.support.card` summands, each at most B.
`normOne` unfolds definitionally to that exact finite sum. The only nondefinitional
transport is `nsmul_eq_mul`; the mathematical proof is a single existing theorem.
Full [declaring module]({link('source-module.lean.txt')}) and its one explicit caller were read.

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
[General searches]({link('web-0.json')}); [domains]({link('web-1.json')});
[Stacks]({link('web-2.json')}); [MO]({link('web-3.json')}); [recent initial]({link('web-4.json')});
[primary opens]({link('web-5.json')}); [domain/date refinement]({link('web-6.json')});
[local source]({link('local-literature.txt')}).

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
[Raw mathlib-only source]({link('native-raw-executed.lean.txt')}) imports 13 stable mathlib modules,
guards the project name with #check_failure, and verifies `polynomialSupport` / `abstractBound`.
[Raw receipt]({link('native-raw-success.json')}). Fixed-parent exact spelling is also verified
by `supportWeakening` in the [caller source]({link('native-consumers-executed.lean.txt')}).
The empty support allows arbitrary negative B under the weaker hypothesis, correctly yielding
0 ≤ 0. No positivity premise should be introduced. The original global hB implies 0 ≤ B,
but that implication is not needed by the estimate. No weakening beyond actual compiled forms
is claimed; no cost-based verdict reasoning.

## Phase 4c — Modern idioms

| # | Question | Finding |
'''
for i,(a,b) in enumerate(modern,1):r+=f'| {i} | {a} | {b} |\n'
r+=f'''
Modern idiom available: yes, already mathlib's abstract finite-family ordered sum theorem.
It handles signed summands and arbitrary indices without polynomial or norm structure and
composes directly with support/finite-family arguments. No additional upstream modernization
is identified. Q8 fires after definition unfolding; Q9 preserves the original coefficient sum.

## Phase 4.5 — Infrastructure risks

Theorem n/a for each of diamonds, definitional equality, instance search, coercions,
reducibility and universe inference: no new definition or instance is proposed.

## Phase 4.6 — Proof strategy

| Question | Finding |
'''
for a,b in strategy:r+=f'| {a} | {b} |\n'
r+=f'''
Current strategy **MATHLIB-IDIOMATIC**: finite-sum bound directly. Inline in caller to avoid
public wrapper; no new helper lemma is required.
[Generality/idiom evidence]({link('generality.json')}).

## Phase 5 — Five actual mathlib methods

| Method | Current / standard / abstract results |
|---|---|
| Finder | Current search broad polynomial hits; standard and abstract return Finset.sum_le_card_nsmul |
| Loogle | Name query finds generated Finset/Multiset/List laws; multiplication-shaped standard search broader; abstract sum/nsmul hits exact Finset theorem |
| LeanSearch | Current coefficient API context; standard and abstract hit Finset.sum_le_card_nsmul |
| rg | Current-name mathlib search empty; standard norm files and abstract finite-sum source inspected; exact generated name found via to_additive |
| local | Actual three requests; project target found, but all report index unavailable; empty standard/abstract results are inconclusive |

[12 raw formal receipts]({link('formal-search.json')}); [current rg]({link('rg-current.json')});
[standard rg]({link('rg-literature.json')}); [abstract rg]({link('rg-abstract.json')});
[untruncated full-name rg]({link('rg-full-name.json')}). Finder/LeanSearch external signatures
use PartialOrder; pinned native signature is weaker Preorder and authoritative:

```lean
Finset.sum_le_card_nsmul {{ι N : Type*}} [AddCommMonoid N] [Preorder N] [AddLeftMono N]
  (s : Finset ι) (f : ι → N) (B : N) (h : ∀ x ∈ s, f x ≤ B) :
  s.sum f ≤ s.card • B
```

Pinned source: `Mathlib/Algebra/Order/BigOperators/Group/Finset.lean:285–290`,
generated additively from `prod_le_pow_card`; [source]({link('mathlib-source-0.lean.txt')}).
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
[Caller search]({link('rg-callers.json')}); [inline search]({link('rg-inline.json')});
[caller metadata]({link('callers.json')}).
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
[Complete caller replay and audit receipt]({link('native-consumers-success.json')}).
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
full caller/audit. [Verification]({link('verification.json')});
[current manifest]({link('copy-manifest.json')}); [portable validator]({link('validate.py')}).
Root acceptance pending; root owns implementation and integration.
'''
(D/'report.md').write_text(r)
