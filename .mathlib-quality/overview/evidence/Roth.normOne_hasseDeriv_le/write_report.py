from pathlib import Path
import json
D=Path(__file__).parent;N='Roth.normOne_hasseDeriv_le'
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
modern=[
['Typeclasses','yes','CommRing R and bundled AddGroupSeminorm R; no custom size axioms'],
['Filters','no','Finite algebraic sum; no topology or limits'],
['Universal property','no','Theorem estimates an existing linear operator; no new construction'],
['Bundled substructure','no','No closure predicate; seminorm already bundled'],
['Weaken algebra','yes','Replace integer coefficients by arbitrary CommRing with additive seminorm'],
['Higher categories','no','No categorical content'],
['Concrete indices','no','σ already arbitrary; ℕ exponents encode polynomials; ℝ is seminorm codomain'],
['Concrete-via-abstract','yes','After expansion integer casts/absolute values use only subadditivity and natural scalar bound; actual generic proof compiled'],
['False-generalization guard','PASS','Exact integer specialization has identical RHS factor and normOne, compiled; not Gauss sup norm, Mahler measure or analytic L1 norm']]
strategy=[['Topology','n/a','No topology'],['Algebra subobjects','no','Support coefficient comparison is natural; no ideal inclusion'],['Analysis filters','n/a','Finite sum only'],['Category universal property','n/a','No category'],['Missing helpers','yes','Multivariate Hasse API and coefficient seminorm finite-sum estimate; new size_add is evidence helper, not existing mathlib fact']]
infra=[[x,'n/a: theorem; adds no structure, instance, coercion or definitional equality'] for x in ['Typeclass diamond','Reducibility leak','Noncanonical unfolding','Instance priority','Universes','Coercion ambiguity']]
out('generality.json',dict(declaration=N,reason='MODERN-IDIOM',parameters=[['σ','arbitrary Type; retain'],['Fintype σ','needed for global sum of all coordinate r; retain'],['d','arbitrary multi-index; retain'],['P : MvPolynomial σ ℤ','replace ℤ with CommRing R, additive seminorm p; verified'],['r','arbitrary ℕ-valued coordinate bounds; retain'],['hP','used to bound every supported exponent; retain'],['ℝ codomain','retain seminorm codomain']],expanded_forms=[dict(name='CommRing and AddGroupSeminorm coefficient sum',status='PASS',verified=True,source='native-generic-executed.lean.txt'),dict(name='exact integer recovery',status='PASS',verified=True,source='native-generic-executed.lean.txt')],modern_rows=modern,strategy_rows=strategy,infrastructure_rows=infra))
phases={x:'PASS' for x in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; six risk rows justified'
out('assessment.json',dict(declaration=N,canonical_index=90,verdict='YES-but-generalise-first',reason='MODERN-IDIOM',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True))
t=json.loads((D/'native-type.json').read_text())['type']
out('overview-entry.json',dict(declaration=N,kind='theorem',type=t,what='Hasse derivative has coefficient ℓ¹ size at most 2 to sum of coordinate degree bounds times original size.',how='Expand derivative into monomials, apply finite triangle inequality, bound each binomial product and sum.',hypotheses='Fintype σ; arbitrary derivative multi-index; integer polynomial with degreeOf j P ≤ r j.',project_dependencies=['MvPolynomial.hasseDeriv_apply','Roth.normOne_sum_le','Roth.normOne_monomial','MvPolynomial.hasseCoeff_le_two_pow','Roth.normOne'],caller_summary='One source proof caller, Roth.abs_coeff_det_hasseDeriv_le:269; same sole direct consumer in exact ordered293 native audit; full generic-specialization replay passed.',mathlib_api_audit='Five actual methods across current/standard/abstract forms. Existing finite sum/natural binomial facts are building blocks; actual multivariate Hasse operator absent in guarded mathlib-only native environment.',moral_duplications='Univariate Hasse coefficient formula is an analogue; Gauss sup norm, Mahler measure, and coefficient sup bound are distinct estimates.',generalization='Native-verified arbitrary CommRing R and AddGroupSeminorm R coefficient sum; exact int recovery. MODERN-IDIOM.',missing_api='Multivariate Hasse derivative foundation and coefficient seminorm finite-support sum bound. State explicit coefficient sums, avoiding a new coefficient norm foundation.',junk='Keep estimate; integer-specific spelling becomes local specialization. Test-only size helper is not recommended public upstream API.',action='YES-but-generalise-first: propose Mathlib/Analysis/Polynomial/MvHasseDeriv.lean after foundational algebra PR, group coefficient sup and coefficient sum bounds; generalise/cleanup before submission.'))
summaries=['Specific form: ring Hasse expansion and polynomial coefficient length; exact degree estimate in local Lemma3.','General form: coefficient norms differ from analytic circle Lp norms; no exact generic seminorm Hasse bound found.','Aliases: polynomial length/height literature and Roth notes; same binomial mechanism.','nLab search finds Hasse-Schmidt derivative and related derivations; no length estimate.','nCatLab search finds Hasse-Schmidt derivation; no coefficient norm estimate.','Stacks divided power polynomial algebras are distinct objects; no estimate found.','MathOverflow yields Hasse derivative questions and unrelated Hasse-Weil bounds; no exact norm bound.','Recent arXiv initial search yields Ganapathy2024 categorified Hasse derivative plus false Hesse/Hasse-principle matches; no exact estimate.','Primary nLab fetch failed: unsupported application/xhtml+xml; search snippets only.','Stacks07H4 uses divided power multiplication and universal properties; not this ordinary polynomial size theorem.','Primary Bhargava-Ghosh-Guo-Kumar-Umans §3.2 defines ring-valued Hasse derivatives by Taylor coefficients; supports algebraic generality, not seminorm estimate.','Refined arXiv multipoint2022 query returned empty.','Ganapathy2024 revised2025 uses categorifications of Hasse derivatives, not coefficient size bound.']
for i in range(23):
 p=D/f'web-{i}.json';w=json.loads(p.read_text());w['urls']=[u.rstrip('),.;') for u in w['urls']];w['summary']=summaries[i] if i<13 else w['summary'];p.write_text(json.dumps(w,indent=2,ensure_ascii=False)+'\n')
P='../evidence/'+N+'/'
report=f'''# `{N}` — YES-but-generalise-first

Reason: **MODERN-IDIOM**. The estimate belongs with multivariate Hasse derivative analysis,
stated for the sum of an arbitrary additive coefficient seminorm on a commutative ring.
This generalization and exact integer recovery compile. The full determinant consumer also
compiles after replacement. No production file or pin was changed. Canonical declaration90/293.

## Phase 0 — baseline

Fresh hashes of all17 source/pin inputs match the shared successful2467-job baseline.
The target resolves in `Roth/CoeffNorm.lean:148–158`, with no sorry.
See [hashes]({P}inputs.json), [baseline]({P}baseline-build.txt),
[original native check]({P}native-original-success.json).
The declaring module and complete Hasse derivative module were read fresh; the only source
caller is in the declaring module, which was read in full.

## Phase 1 — statement and proof

For an integer multivariate polynomial P whose degree in X_j is at most r_j, any Hasse
multi-derivative has coefficient ℓ¹ norm at most 2^(Σr_j) times that of P. The derivative order
is unrestricted; vanishing derivatives cause no exception. There are no positivity or
nonzero hypotheses on P.

Full elaborated type (native):
```lean
{t}
```

Parameters are arbitrary variable type σ, a Fintype instance to express Σr_j, arbitrary
multi-index d, polynomial P, arbitrary natural degree bounds r, and hP bounding every degree.
The proof expands into derivative monomials, applies the finite coefficient-sum triangle
inequality, bounds the binomial multiplier by 2^(Σr_j), and sums input coefficient sizes.
Dependencies are `hasseDeriv_apply`, `normOne_sum_le`, `normOne_monomial`, and
`hasseCoeff_le_two_pow`, plus the definition `normOne`.

## Phase 2 — preliminaries

**BIG**: explicitly listed in the module's Main results. This is not inferred from a sibling.
The definition-only one-line exemption test is n/a: theorem. The proof has ten substantive
lines, and project helpers do not count as existing mathlib calls.

## Phase 3 — exhaustive literature

All exact requests, returned response SHA256/byte counts, sanitized locators and original
summaries are archived as web0–22 metadata; returned article/search bodies are not persisted.
The table identifies every executed request rather than treating synthesis as a ninth channel.

| Channel | Executed evidence | Finding |
|---|---|---|
| General web, specific | [web0]({P}web-0.json) | multivariate Hasse expansion; length terminology |
| General web, general | [web1]({P}web-1.json) | distinguish coefficient norm from analytic Lp norm |
| General web, aliases | [web2]({P}web-2.json) | length, height and Roth estimates |
| ChatGPT math MCP | n/a | ask_chatgpt_math unavailable; no call fabricated |
| Local clean.tex | [source excerpt]({P}local-literature.txt) | Lemma3 lines445–460: coefficient ℓ¹ sum, triangle, binomial factor |
| nLab | [3]({P}web-3.json), [13]({P}web-13.json), [14]({P}web-14.json), [primary8]({P}web-8.json) | Hasse-Schmidt derivations; primary fetch unsupported XHTML |
| nCatLab | [4]({P}web-4.json), [15]({P}web-15.json), [16]({P}web-16.json) | no categorical coefficient-size theorem; categorical abstraction unnecessary |
| Stacks | [5]({P}web-5.json), [17]({P}web-17.json), [18]({P}web-18.json), [primary9]({P}web-9.json) | divided power algebra uses different multiplication; excluded |
| MathOverflow | [6]({P}web-6.json), [19]({P}web-19.json), [20]({P}web-20.json) | Hasse derivative questions, no exact length estimate |
| Recent arXiv | [7]({P}web-7.json), [11]({P}web-11.json), [21]({P}web-21.json), [22]({P}web-22.json), [primary12]({P}web-12.json) | explicit2021-10-27 to2026-10-28 search; recent Hasse uses, no norm bound |

Primary external algebraic standard: Bhargava et al., *Fast Multivariate Multipoint
Evaluation Over All Finite Fields*, §3.2, [primary access]({P}web-10.json),
[author PDF](https://mrinalkr.bitbucket.io/papers/MME2.pdf). The Hasse operator is Taylor
coefficient extraction over a ring. The exact ℓ¹ estimate is grounded in local clean.tex
Lemma3, not claimed from finite-field algorithm papers. Additive-seminorm generality is an
explicit modern abstraction of the verified triangle argument, not a quoted literature theorem.
Ganapathy's [2024 paper revised2025](https://arxiv.org/abs/2407.13604) concerns categorification;
[Stacks07H4](https://stacks.math.columbia.edu/tag/07H4) concerns divided powers. Neither is an
exact replacement. No contradiction in the mathematical definition was found.

## Phase 4a — parameter analysis

| Parameter | Decision and evidence |
|---|---|
| σ | already arbitrary universe-polymorphic type |
| Fintype σ | retain for the sum over coordinate degree bounds; no dropping claimed |
| d | already any finitely supported natural multi-index |
| P over ℤ | replace coefficients by arbitrary CommRing R and p : AddGroupSeminorm R |
| r | retain arbitrary natural coordinate bounds |
| hP | retain; bounds every supported exponent via monomial_le_degreeOf |
| ℝ codomain | retain the standard AddGroupSeminorm codomain |

## Phase 4b — mechanically verified generality

The expanded representation is strictly more general. The fixed parent `Roth.normOne` remains
integer-specific; no weakening of its definition in place is claimed. The proposed theorem
can state explicit coefficient sums:
```lean
(p : AddGroupSeminorm R) (d : σ →₀ ℕ) (P : MvPolynomial σ R)
(hP : ∀ j, degreeOf j P ≤ r j) :
(hasseDeriv d P).coeff.sum (fun _ a ↦ p a) ≤
  2 ^ (∑ j, r j) * P.coeff.sum (fun _ a ↦ p a)
```
Here `[CommRing R] [Fintype σ]`; the code uses a test-only `size` helper definition for these
expressions, not a proposed public upstream definition. The accepted native proof establishes
subadditivity over coefficient support unions, finite triangle inequality, monomial evaluation,
and the Hasse bound. Taking p(z)=|(z:ℝ)| recovers the original result exactly in one call.
See [actual generic snippet]({P}accepted-generic-snippet.lean.txt),
[complete execution]({P}native-generic-executed.lean.txt), [receipt]({P}native-generic-success.json).
Commutative rings with zero divisors and positive characteristic are allowed. Multiplicativity,
normalization p(1)=1 and torsion freeness are unnecessary. No further weakening is claimed.

## Phase 4c — modern idiom

| # | Diagnostic | Result |
|---|---|---|
'''
for i,(a,b,c) in enumerate(modern,1):report+=f'| {i} | {a}: {b} | {c} |\n'
report+='''
Q8 was run on the actual proof: after `hasseDeriv_apply`, the integer-specific work is
cast/absolute-value normalization; the size reasoning is triangle inequality and natural scalar
control. Some `normOne` helper names remain, so occurrence counting alone does not prove
abstraction. The adversarial diagnostic is confirmed by the compiled replacement proof, which
has no integer operations until the specialization. This materially admits other coefficient
seminorms without a multiplicative assumption. Cost MODERATE; no parent API redesign required.

## Phase 4.5 — infrastructure risk

Theorem n/a: all six rows (typeclass diamonds, reducibility leaks, noncanonical unfolding,
instance priorities, universe issues, coercion ambiguity) introduce nothing through this theorem.
No new global instance is proposed. The evidence helper `size` merely names an explicit sum;
it need not become upstream API. Detailed six-row table is in generality.json.

## Phase 4.6 — proof strategy

| Row | Assessment |
|---|---|
| Topology/filter | n/a finite algebra |
| Algebra/subobjects | support comparison and monomial expansion are appropriate; no ideal/submodule substitute |
| Analysis/nets | n/a finite sum |
| Category/universal property | n/a estimate on an existing operator |
| Missing helper API | multivariate Hasse foundation and coefficient seminorm sum support/triangle API |

REFACTOR-RECOMMENDED: retain the monomial expansion but use the additive coefficient seminorm
sum. The new helper proofs are not advertised as existing mathlib replacements. Missing generic
finite-support subadditivity can be a separate contribution; the target can still state explicit
sums. No inference from earlier BORDERLINE normOne infrastructure verdicts was made.

## Phase 5 — five actual mathlib search methods

All current/standard/abstract requests and full formal responses are in formal-search.json.
External indices may differ from the pinned revision; positive candidates were inspected in
pinned sources and the useful signatures were checked in the native raw experiment.

| Method | Current | Literature-standard | Abstract |
|---|---|---|---|
| Lean-Finder | Chevalley complexity false matches; univariate Hasse definitions | univariate Hasse coefficient/apply; Mahler bounds | Gauss/Mahler/projective seminorm near matches |
| Loogle | hasseDeriv,norm: empty | hasseDeriv,sum: empty | AddGroupSeminorm,sum: empty |
| LeanSearch | pderiv/univariate/Laurent Hasse | ordinary derivative degree laws | norm_sum_le_of_le and univariate/Laurent analogues |
| rg | no target/norm-Hasse theorem in mathlib | univariate Hasse API | Finset finite triangle, Finsupp support sums, choose bound |
| Local name | project target and archived project evidence | project+univariate Hasse names | Finsupp.sum_le_sum and index variants |

Local search reports index unavailable and includes archived evidence: these hits prove neither
pinned presence nor absence. [Formal receipts](LINKformal-search.json),
[rg current](LINKrg-current.json), [standard](LINKrg-literature.json),
[abstract](LINKrg-abstract.json), [full-name grep](LINKrg-full-name.json).
The raw mathlib-only execution verifies that the actual multivariate operator and project
target are absent with `#check_failure`. It proves the corresponding finite-monomial expansion
bound from mathlib building blocks, requiring fresh support-sum/triangle and natural scalar
arguments. This is a compiled generic-route test, not an inference from unsuccessful search.
No slow exact? search was repeated. See [raw source](LINKnative-raw-executed.lean.txt)
and [clean receipt](LINKnative-raw-success.json).

## Phase 5.5 — statement shape

1. Normal form: coefficient sum is ℓ¹ length. Gauss sup norm, Mahler measure and analytic
   circle L1 norm do not state this. A coefficient-sup bound followed by a cardinality bound
   loses the input ℓ¹ factor and is not a replacement.
2. Syntactic generality: keep arbitrary d,r and use hP explicitly. State coefficient sums
   directly with p; a global normOne redesign is unnecessary.
3. Superfluous hypotheses: no extra B/positivity, characteristic or NoZeroDivisors assumption.
   General coefficient ring/seminorm recovery is compiled; retain finite-variable global sum.

## Phase 6.0 — caller and inline audit

[Source audit](LINKrg-callers.json) finds one documentation mention, the declaration and
one proof call, inside `Roth.abs_coeff_det_hasseDeriv_le` at269. Its entire proof was read
fresh and replayed with `MvPolynomial.NormHasseGeneric.specialization`; no target reuse occurs
inside the replacement. [Full consumer execution](LINKnative-consumers-executed.lean.txt),
[receipt](LINKnative-consumers-success.json), [structured audit](LINKcallers.json).
The runtime environment audit scans exactly293 ordered names, all293 unique, all293 present
with values, including private names constructed by Lean.mkPrivateNameCore. Its sole direct
proof consumer is Roth.abs_coeff_det_hasseDeriv_le. The portable validator compares the array
against the tracked order exactly. This is direct proof constants, not opaque transitive/simp
closure. Inline audit found related coefficient estimates, not a duplicate ℓ¹ Hasse law.

## Phase 6 — composition experiments

The original ten-line proof composes project normOne and Hasse helpers, which do not count
as mathlib building blocks. The raw successful expansion estimate requires new support-union
subadditivity, finite triangle, scalar and binomial reasoning; no ≤3 existing-call replacement
was found. Native generic proof and exact recovery succeed, and the entire sole caller succeeds.
These four executed sets use standard propext/Classical.choice/Quot.sound only, no sorry,
unsafe, native_decide or raised limits. No rejected native attempt was used: root corrected
Finsupp representation normalization before the first execution, and all four checks were clean.
The parent normOne assessment did not identify a more general parent carrying this Hasse law,
so the parent re-aim NO gate does not apply. New helpers are not existing mathlib theorems.

## Phase 7 — verdict and upstream action

**YES-but-generalise-first / MODERN-IDIOM.** The exact useful estimate is standard coefficient
length arithmetic with an independently verified additive-seminorm formulation. No cost-based
downgrade, sibling verdict inheritance, or missing-search-as-proof shortcut is used.
Proposed home: `Mathlib/Analysis/Polynomial/MvHasseDeriv.lean` (new analysis-facing module)
after `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` establishes the foundational operator.
Proposed PR title: `feat(Analysis/Polynomial): coefficient seminorm bounds for multivariate Hasse derivatives`.
Group the ℓ¹ sum bound with the already accepted YES coefficient bound
`Roth.abs_coeff_hasseDeriv_le`; foundational accepted YES `MvPolynomial.hasseDeriv` and
`MvPolynomial.coeff_hasseDeriv` must precede this. The exact accepted-YES snapshot is in
[accepted grouping](LINKaccepted-yes-grouping.json); usefulness alone is not a prior verdict.

Before submission:

- `/generalise Roth.normOne_hasseDeriv_le`: implement the explicit coefficient-seminorm sum
  theorem already mechanically verified; leave integer specialization local as needed.
- `/cleanup Roth/CoeffNorm.lean Roth.normOne_hasseDeriv_le`: full cleanup/naming/import review.
- Separate the generic Finsupp size triangle helper if reviewers prefer it; do not claim it exists.
- Preserve the original determinant behavior using the full caller replay as validation.
- Ask Moritz Firsching (2026-08-19 HasseDeriv-map commit334438dace) and/or Yaël Dillies
  (2026-06-27 Lp direct sums and2026-07-04 MonoidAlgebra refactor), as shown by fresh
  read-only [relevant history](LINKreviewer-git.json), to review operator and seminorm API shape.

## Phase 8 — completeness and provenance

[Assessment](LINKassessment.json), [verification](LINKverification.json),
[generality tables](LINKgenerality.json), [overview entry](LINKoverview-entry.json),
[current copy manifest](LINKcopy-manifest.json), [portable validator](LINKvalidate.py).
All phases PASS or explicitly theorem-n/a; unresolved[]; root acceptance pending independent
review. The validator checks current artifact hashes, exact canonical order, all17 current input
hashes, full native success/no partial/errors, standard axioms, required literature/formal-search
coverage, report links and credential guard. Historical worker manifests never override current
manifest validation. Production Lean files and pins remain unchanged.
'''.replace('LINK',P)
(D/'report.md').write_text(report)
print('Report and phase/overview artifacts written')
