from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='LeanEval.NumberTheory.ThueSiegelRothProblem.isDiophantine_iff'
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def link(f):return '../evidence/'+N+'/'+f
channels=[
('web-specific','irrationality exponent equivalent for every epsilon positive constant lower bound rational approximation','Irrationality exponent has equivalent eventual lower-bound presentations; Tao optimization page explicitly gives the sup/inf comparison.'),
('web-general','Diophantine approximation uniform lower bound finite exceptions arbitrary exponent irrationality measure','Constants and finite exceptional sets recur throughout approximation theory; distinguish uniform-in-p,q lower constants from uniform approximation exponents.'),
('web-alias','Roth theorem irrationality measure epsilon constant formulation equivalence','Aliases irrationality exponent and measure; Roth statements commonly use finiteness for every positive epsilon.'),
('nlab','site:ncatlab.org/nlab irrationality exponent Diophantine approximation','Related irrational-number page discusses nonzero rational differences and constructive distinctions; no exact equivalence found.'),
('ncatlab','site:ncatlab.org/ncatlab irrationality exponent Diophantine approximation','Actual distinct namespace query returned only nLab or unrelated pages, no in-namespace theorem; no categorical reformulation established.'),
('stacks','site:stacks.math.columbia.edu irrationality measure rational approximation','No matching Stacks result returned; this is real Diophantine analysis rather than an algebraic geometry API.'),
('mathoverflow','site:mathoverflow.net irrationality exponent lower bound constant epsilon Roth','Finite-solutions discussion and historical discussion corroborate epsilon quantifier; not evidence of a mathlib replacement.'),
('arxiv','site:arxiv.org irrationality exponent Diophantine lower bounds after:2021-10-29 before:2026-10-30','Recent Aaronson–Nakada paper treats arbitrary irrationality exponent and Diophantine/Liouville classes, confirming nonalgebraic downstream settings.')]
sources=[dict(title='Martine Queffelec, Diophantine approximation and expansions of real numbers',url='https://www.kurims.kyoto-u.ac.jp/~kenkyubu/bessatsu/open/B46/pdf/B46_010.pdf',locator='§2 p215 and Definition3.1 p217; web lines17–24,72–83',summary='Uses nonexact rational approximants and defines the irrationality exponent for irrational reals as a supremum over approximation orders. This supports varying the cutoff and retaining exact-error conventions carefully.'),dict(title='Jon Aaronson and Hitoshi Nakada, Extravagance, irrationality and Diophantine approximation',url='https://arxiv.org/abs/2409.19393',locator='v1 submitted2024-09-28; v5 2025-09-04; abstract and §1',summary='Studies Diophantine and Liouville behavior for invariant measures and examples with arbitrary irrationality exponent. Generic cutoff statements therefore serve more than the algebraic Roth application.'),dict(title='Extravagance, irrationality and Diophantine approximation, HTML',url='https://arxiv.org/html/2409.19393v5',locator='§1 Introduction, abstract',summary='Recent primary paper supplies a modern dynamical context; it does not identify an existing formal equivalence.'),dict(title='The irrationality measure of pi',url='https://teorth.github.io/optimizationproblems/constants/7a.html',locator='Description of constant lines3–11',summary='Explicitly compares a supremum of infinitely-often exponents with an infimum of eventual lower-bound exponents. Used for formulation only, not numerical bounds.'),dict(title='irrational number in nLab',url='https://ncatlab.org/nlab/show/irrational%2Bnumber',locator='Definitions',summary='Discusses positivity versus nonequality with rational numbers and their classical equivalence; no exponent-bound bridge identified.'),dict(title='Estimate number of solutions in Roth theorem',url='https://mathoverflow.net/questions/249176/estimate-number-of-solutions-in-the-roths-theorem',locator='Question and answers',summary='Frames Roth in terms of finitely many solutions for each epsilon and discusses quantitative refinements.'),dict(title='History question: Roth theorem before Roth',url='https://mathoverflow.net/questions/149600/history-question-roths-theorem-on-approximating-algebraic-numbers-before-rot/149653',locator='Question and answer',summary='Highlights the separate universal quantifiers over algebraic irrational numbers and positive epsilon; does not justify dropping epsilon.')]
dump('literature.json',dict(general_queries=[x[1]for x in channels[:3]],channels=[dict(channel=c,query=q,outcome=o)for c,q,o in channels],sources=sources,local=dict(receipt='literature-local.json',source='local-source-section6.tex.txt',summary='clean.tex §6 states pair-exponent Roth and absorption of constants into an exponent gap; no exact LeanEval iff printed there'),optional_channel=dict(status='unavailable: ask_chatgpt_math tool absent',reason='Optional channel unavailable; all named mandatory channels still executed'),third_party_bodies_persisted=False,malformed_queries=False))
modern=[
['typeclasses','no','The hypothesis concerns one real number; a Prop typeclass would create implicit search rather than improve inference.'],
['filters','yes','LiouvilleWith uses frequently atTop denominators; exponent_iff and pair_liouville_iff_all_real connect it to pairs.'],
['universal property','no','No constructed object or universal mapping property.'],
['bundled substructure','no','Approximation pairs are a subset, not closed algebraic data; a subtype is not a replacement for Infinite.'],
['hierarchy','no','Real rpow and rational discreteness are used; arbitrary ordered fields lack the stated analytical API.'],
['higher categories','no','No categorical content; distinct nCatLab query supplied none.'],
['indices','yes','The exponent cutoff2 is a semantic parameter t, unlike the indispensable integer/natural rational indexing. No positivity on t is needed.'],
['concrete via abstract','yes','Counted literal2 in original body: it enters gap arithmetic only; generic proof replaces it uniformly by t. The proof has no special arithmetic property of2.'],
['false-generalization guard','PASS','All-real pair iff is valid because rational exact multiples make both sides false. Liouville cutoff alone is true at rationals with cutoff2; retain Irrational conjunct. Do not identify pair sets with reduced rational sets.']]
strategy=[['topology','yes','Use existing atTop exponent-gap limits; LiouvilleWith frequently_lt_rpow_neg handles absorbing a constant.'],['algebra','no','No ideal/submodule inclusion or point-free algebraic law.'],['analysis','yes','Filters already drive gap; pair-denominator cofinality bridge still needs a proof.'],['categories','no','No universal-property construction.'],['missing helpers','yes','Finite exceptional approximations to positive strict uniform constant; generic exponent-cutoff equivalence; rational-pair irrationality derivation. These are authored proof content.']]
shape=[['normal form','REFACTOR','Prefer uniform lower bounds ↔ Irrational x ∧ all LiouvilleWith exponents bounded, with existing predicate family on RHS. Pair bridge remains useful at project boundary.'],['syntactic generality','RESTATE','Drop hx for full all-real pair equivalence, parameterize cutoff t in generic API; fixed2 project statement recovered definitionally.'],['superfluous arguments','DROP1','hx occurs in private helper but is derivable from either side of full iff. x and real rational indexing remain essential.']]
risk=[[r,'n/a theorem: no new typeclass or definitional equality']for r in ['typeclass diamond','reducibility leak','noncanonical unfolding','instance priority','universe polymorphism','coercion ambiguity']]
dump('phase-checks.json',dict(size='SMALL: equivalence helper, not named theorem or new structure',one_line='n/a theorem',modern9=modern,proofstrategy5=strategy,statement_shape3=shape,infrastructure_risks=risk,generality=[['x : Real','retain','real powers/absolute values and rational approximation'],['hx : Irrational x','drop verified','allreal theorem and original caller recovery'],['2 cutoff','parameterize verified','all t : Real, no positivity hypothesis'],['p q : Int positive q','representation bridge','generic pairSet uses natural positive denominator, integer lower bound retained'],['strict errors/lower bounds','explicit normalization','epsilon half-gap and C/2 strictification; endpoint badly approximable claim not made']]))
# Native type extracted from the complete tagged type diagnostic, not from splitting the printed body.
r=json.loads((D/'original01-receipt.json').read_text())['result'];z=r.get('structuredContent')or json.loads(r['content'][0]['text']);z=z.get('result',z)
messages=[x['message']for x in z['items']];ft=next(m.split('D292_FULL_TYPE: ',1)[1]for m in messages if m.startswith('D292_FULL_TYPE:'))
dump('native-type.json',dict(full_type=ft,source='original01-receipt.json',full_kernel_printer_body=False,elision='139691characters elided in pp.all printer; exact original written proof archived, kernel value read with allowOpaque=true, type and standard axioms complete'))
questions=[
'Should upstream expose a named UniformBound t x predicate, or keep the lower-bound quantifiers inside equivalences to Irrational x ∧ ∀p, LiouvilleWith p x → p ≤ t?',
'Should the canonical public bridge use denominator-frequency LiouvilleWith directly, keeping unreduced pairSet and its equivalence in a secondary interface module?',
'Should the generic finite-exception strictification and rational-pair irrationality lemmas ship together with the cutoff equivalence, with fixed2 LeanEval wrappers remaining project-local?']
dump('overview-entry.json',dict(kind='theorem',type=ft,what='For an irrational real number, uniform positive lower bounds at every exponent2+epsilon are equivalent to an upper bound2 on all exponents having infinitely many unreduced approximation pairs.',how='Uses Roth.eventually_div_rpow_lt to absorb a positive constant into an epsilon half-gap, removes finitely many bounded-denominator pairs with Roth.approxSet_den_le_finite, and uses the private finite-positive-minimum helper for the reverse implication.',hypotheses='The original has Irrational x; fresh all-real proof derives it from either side and removes that binder. Real powers and positive denominators remain.',project_dependencies=json.loads((D/'project-dependencies.json').read_text()),caller_summary='One explicit same-file caller thueSiegelRoth at LeanEval:63; zero external-to-file. Complete original inlining and new all-real recovery preserve its exact signature and eliminate target reference.',mathlib_api_audit='LiouvilleWith and its frequently_lt_rpow_neg/affine API are relevant building blocks; no direct uniform-bound/cutoff equivalence hit was verified. The generic bridge is authored proof, not an existing mathlib call.',moral_duplications='Shares exponent-gap and finite-denominator tools with Main.reduction; these serve different statements. Private positive-minimum helper supplies one direction; no duplicate full equivalence found.',generalization=dict(verified=True,drop='hx',all_real_type='∀ {x : ℝ}, IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2',generic_type='∀ {t x : ℝ}, UniformBound t x ↔ ∀ {κ : ℝ}, (pairSet x κ).Infinite → κ ≤ t',modern_type='∀ {t x : ℝ}, UniformBound t x ↔ Irrational x ∧ ∀ {p : ℝ}, LiouvilleWith p x → p ≤ t',conditions='No positivity condition on t; Liouville bridge retains irrationality; fixed2 recovered without assumption'),missing_api='Generic finite-exception/uniform-bound and exponent-cutoff bridges; decide normal form before exporting new definitions.',junk='Not dead: actual final caller. One caller alone does not turn its nontrivial proof into a mathlib composition.',action=dict(verdict='BORDERLINE-needs-human',retain_local=True,immediate='The mathematically justified local cleanup is to remove hx from the pair equivalence and use all_real.mpr at the existing caller; no production edit made.',questions=questions,upstream_home_provisional='Mathlib/NumberTheory/Transcendental/Liouville/Diophantine.lean (new module importing LiouvilleWith)',cost_based=False)))
phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7']};phases['8']='pending'
dump('assessment.json',dict(declaration=N,canonical_index=292,kind='theorem',verdict='BORDERLINE-needs-human',completed=False,allphases='pending phase8',phases=phases,unresolved=[],root_acceptance='pending',parent_verdict_inherited=False,cost_based_verdict=False,future_upstream_questions=questions,classification='SMALL',one_line='n/a theorem',infrastructure_risk='n/a theorem',native_release='pending full package gates'))
report=f'''# `{N}`

Verdict: **BORDERLINE-needs-human**. The equivalence contains reusable mathematical content beyond a short composition. A fresh proof establishes the stronger all-real statement, and a generic real cutoff works without any positivity assumption on that cutoff. Upstream design remains a choice of canonical interface, rather than a question about whether the proof can be generalized. This assessment is independent of the verdict on `IsDiophantine` and does not assess the later named Roth declaration.

## Phase0: baseline and scope

The unchanged17 source/pin hashes freshly match the shared successful2467-job baseline. The complete66-line LeanEval module and the full actual caller were read. Target resolves at Roth/LeanEval.lean:42, public theorem, no sorry. The module proves the LeanEval interface from `Roth.roth`. Root exclusively executed native checks; workers used only remote formal search and file reads. Stable18 isolated imports and disk9 remained unchanged; root freshly authorized the19th LiouvilleWith import after pinned-header review.

[Fresh input hashes]({link('inputs.json')}); [baseline]({link('baseline-build.txt')}); [module]({link('source-LeanEval.lean.txt')}); [prefix controls]({link('prefix-controls.json')}).

## Phase1: statement and proof

For each positive epsilon a real number has a strictly positive constant bounding every positive-denominator rational approximation error below by C/q^(2+epsilon), precisely when infinitely many unreduced approximation pairs can occur only at exponents at most2. The original supplies irrationality as a hypothesis. There is no algebraicity assumption in this equivalence.

The forward direction assumes kappa>2 and uses epsilon=(kappa-2)/2. `Roth.eventually_div_rpow_lt` absorbs1/C into the positive exponent gap. Removing the finite set of bounded-denominator pairs using `Roth.approxSet_den_le_finite` gives an approximation violating the uniform lower bound. Conversely, the exponent hypothesis makes the pair set at2+epsilon finite. The private helper inserts(0,1), takes a minimum of positive weighted errors, and halves it and1 to produce a strict positive constant valid both inside and outside the exceptional set.

Full native type (tagged kernel type, with binder types):

```lean
{ft}
```

Project dependencies are `IsDiophantine`, `Roth.approxSet`, `Roth.eventually_div_rpow_lt`, `Roth.approxSet_den_le_finite`, and the private `exists_pos_div_rpow_lt_aux` in Roth.LeanEval. The canonical project name is used here; the loaded private kernel name is recorded only in raw audit evidence.

[Exact original proof and helper replay]({link('original-executed.lean.txt')}); [full native receipt]({link('original01-receipt.json')}); [native type]({link('native-type.json')}); [dependencies]({link('project-dependencies.json')}). Original replay copies exactly the target and private helper lines20–39 into a fresh namespace. Proof equality via Subsingleton.elim confirms exact type agreement, not identity of proof construction. The pp.all kernel body is explicitly elided by139691characters; this is not claimed to be a full pretty-printed proof. The exact source proof, complete tagged type, actual kernel value access, used constants and standard-axiom audit are retained.

## Phase2: preliminary classification

SMALL: a characterization lemma rather than a named main theorem or new mathematical structure. Its two directions nevertheless require real reasoning. One-line definition check: n/a, theorem. No prefilter or inherited parent verdict applies.

## Phase3: exhaustive literature

| Channel | Actual query | Outcome |
|---|---|---|
'''
for c,q,o in channels:report+=f'| {c} | `{q}` | {o} |\n'
report+='''| Optional mathematical second opinion | ask_chatgpt_math | Unavailable tool, justified n/a; all other channels completed. |
| Local references | rg Roth/\\kappa/irrational/approximation in clean.tex | §6 gives the pair formulation and exponent-gap constant absorption; no exact LeanEval iff printed. |

'''
for x in sources:report+=f"- [{x['title']}]({x['url']}), {x['locator']}: {x['summary']}\n"
report+=f'''
The primary survey identifies the irrationality exponent as a supremum for irrational real numbers, with generic exponent cutoffs beyond algebraic reals. The exact-minimum argument upgrades eventual lower bounds to all positive denominators. The literature often excludes exact equality or counts reduced rational values: the unreduced pair convention must be kept distinct. No claim about the badly approximable epsilon0 endpoint follows. The nCatLab query was genuinely separate from nLab; its out-of-namespace returns are recorded honestly. No Stacks result or higher categorical formulation was established. Exact requests, returned response SHA256/byte counts/status, clean URLs/locators and original short summaries are archived; no article or search-result bodies are persisted.

[Literature accounting]({link('literature.json')}); [web0]({link('web-batch0.json')}); [web1]({link('web-batch1.json')}); [web2]({link('web-batch2.json')}); [web3]({link('web-batch3.json')}); [local query]({link('literature-local.json')}).

## Phase4a–b: every parameter and verified generality

| Parameter or convention | Decision | Mathematical reason |
|---|---|---|
| x:Real | Retain | Real absolute values, rational discreteness and real exponent asymptotics are used. No arbitrary-field weakening claimed. |
| hx:Irrational x | Remove, verified | Uniform bounds fail at the exact rational numerator/denominator. The exponent bound also fails at rational x, since exact multiples give infinitely many pairs at every kappa. |
| Fixed2 | Generic real t, verified | Only gap arithmetic uses2. The proof applies to any t, including nonpositive t; no positivity hypothesis is needed. |
| Integer/natural denominators | Preserve positive denominator semantics | Lift positive integer q to natural for pair membership; normalize casts explicitly. Replacing integer numerators by arbitrary field elements destroys discreteness. |
| Strict upper approximation error | Preserve in pair convention | The finite-exception complement gives a weak lower inequality; halve constants to recover strict lower bounds. |
| Positive epsilon | Retain | A smaller exponent inside the gap is essential. No epsilon0 or badly approximable equivalence asserted. |

Verified all-real project statement:

```lean
theorem all_real {{x : ℝ}} :
    LeanEval.NumberTheory.ThueSiegelRothProblem.IsDiophantine x ↔
      ∀ {{κ : ℝ}}, (Roth.approxSet x κ).Infinite → κ ≤ 2
```

Verified mathlib-only generic statement, with `UniformBound t x` the complete displayed lower-bound formula and `pairSet` the complete pair formula reconstructed from mathlib operations:

```lean
lemma uniform_pair_iff_all_real {{t x : ℝ}} :
    UniformBound t x ↔ ∀ {{κ : ℝ}}, (pairSet x κ).Infinite → κ ≤ t
lemma pair_liouville_iff_all_real {{t x : ℝ}} :
    (∀ {{κ : ℝ}}, (pairSet x κ).Infinite → κ ≤ t) ↔
      Irrational x ∧ ∀ {{p : ℝ}}, LiouvilleWith p x → p ≤ t
```

The mathlib-only source reconstructs finite bounded-denominator sets, finite positive minima, exponent-gap absorption and pair/frequency transport. It replays accepted290modern3 proofs under a new namespace and extends them here; these are credited as authored proofs, never as existing mathlib theorems. It also proves cutoff monotonicity, rational addition and nonzero rational scaling invariance, rational and Liouville countercases, and C/2 equivalence of strict/weak lower bounds. Fixed2 recovery is definitional. The full project recovery retains the original caller signature and uses `all_real.mpr` with the unchanged Roth proof.

[Generic and semantic proof]({link('modern-executed.lean.txt')}); [generic raw receipt]({link('modern01-receipt.json')}); [project all-real recovery and full actual caller]({link('recovery-executed.lean.txt')}); [recovery receipt]({link('recovery01-receipt.json')}). Current form is strictly narrower in the verified hx binder and semantic cutoff; the upstream representation question is separate from correctness or cost.

## Phase4c: modern idiom, all9 rows

| Row | Applies | Reformulation or reason |
|---|---|---|
'''
for row in modern:report+='| '+' | '.join(row)+' |\n'
report+='''
Concrete-via-abstract diagnostic: the original uses literal2 only in epsilon/gap arithmetic; it does not invoke a special property of2. The generic t proof verifies that observation. The pair-set identifier remains in the finite/cofinal transport, so no claim that arbitrary sets of pairs satisfy the theorem is made. Modern LiouvilleWith form directly enables the existing `add_rat_iff`, `mul_rat_iff`, `mono`, and `frequently_lt_rpow_neg` API. The fresh affine and cutoff consequences demonstrate this downstream improvement.

False-generalization guard: exact unreduced multiples force rational pair sets infinite at every exponent, whereas LiouvilleWith excludes equality. The bare all-Liouville-exponent bound at2 is true at rationals. Dropping Irrational from that bridge would be false; dropping the original hx from the pair equivalence is valid. Positive constants and epsilon quantifiers remain.

## Phase4.5: infrastructure risk

All six rows—typeclass diamond, reducibility leak, noncanonical unfolding, instance priority, universe polymorphism and coercion ambiguity—are n/a for this theorem. It introduces no definition, instance or coercion. Any future predicate packaging needs its own definition review.

## Phase4.6: proof strategy, all5 rows

| Kind | Applies | Idiom or gap |
|---|---|---|
'''
for row in strategy:report+='| '+' | '.join(row)+' |\n'
report+='''
REFACTOR-RECOMMENDED: keep the existing filter asymptotics and finite positive-minimum reasoning, extract the reusable equivalence and make the current project theorem a fixed2 specialization. The finite-exception and pair/frequency conversion helpers are substantive missing bridges rather than a three-call wrapper. This recommendation is mathematical organization, not a cost rationale.

## Phase5: all15 formal search cells

| Form | Finder | Loogle | LeanSearch | rg pinned source | local LSP via root |
|---|---|---|---|---|---|
| Current fixed2 uniform/pairs | LiouvilleWith and constant absorption | Irrational equivalences, not target | LiouvilleWith plus metric-a.e. result | No target; Diophantine-equation hits unrelated | index error; target hit only, no absence inference |
| Standard generic exponent bound | LiouvilleWith, forall_liouvilleWith_iff | LiouvilleWith affine equivalences | Bounded-denominator separation and Dirichlet results | No named full bridge identified | index error with empty items; no absence inference |
| Abstract predicate/frequency | LiouvilleWith.irrational, mono | mono, irrational, affine lemmas | exists_pos and frequently_lt_rpow_neg | Relevant source and measure API | index warming with50 related entries; no absence inference |

'''
report+=f'''[All exact requests and raw results]({link('formal-search-matrix.json')}); [untruncated full-name search]({link('full-name-search.json')}); [pinned module hashes]({link('mathlib-inputs.json')}); [candidate signatures]({link('candidates01-receipt.json')}). Remote indexes can differ from this pin; candidate signatures were checked on the pinned environment through root.

`LiouvilleWith.frequently_lt_rpow_neg` handles absorbing a constant at a smaller exponent, but does not itself prove a uniform positive lower constant from finite exceptional pairs. `Irrational.eventually_forall_le_dist_cast_div_of_denom_le` separates an irrational real from bounded denominators; this is a relevant tool, not the full weighted-exponent equivalence. `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational` is a Dirichlet endpoint statement counting reduced rational values, not the requested upper-exponent equivalence. `forall_liouvilleWith_iff` concerns all exponents and Liouville numbers, not a bounded cutoff. No exact or more-general existing theorem was verified as a replacement.

## Phase5.5: all3 statement-shape checks

| Check | Outcome | Action |
|---|---|---|
'''
for row in shape:report+='| '+' | '.join(row)+' |\n'
report+='''
Candidate canonical RHS: Irrational x together with an upper bound on all LiouvilleWith exponents. This avoids inventing a scalar irrationality measure with extended-real endpoint conventions and gives O(n) bridges to one family. A pair-based theorem is still useful at the current project boundary. Its minimal exact cleanup is the all-real statement, whose correctness and caller were checked.

## Phase6: callers, inlining and actual composition

| Actual caller | Source use | Verification |
|---|---|---|
| LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth, Roth/LeanEval.lean:63 | `(isDiophantine_iff _h_irr).mpr (Roth.roth ...)` | Full original body re-elaborated with the entire iff proof inlined; full generalized replacement re-elaborated with exact original signature. |

Internal use count1; external-to-file0. Canonical metadata and `rg --no-ignore` production inventory agree. No independent inline rederivation found in production. The exact293 loaded canonical audit finds one direct body consumer, no direct type consumer; it is not a claim about the entire transitive dependency graph. Target has no simp attribute, so source, body, type, simp and transitive scopes are kept distinct.

'''
report+=f'''[Caller accounting]({link('callers.json')}); [fresh lexical search]({link('source-search.json')}); [complete inline source]({link('inline-executed.lean.txt')}); [inline raw receipt]({link('inline01-receipt.json')}); [generic actual caller]({link('recovery-executed.lean.txt')}).

Attempt1 uses existing `LiouvilleWith.frequently_lt_rpow_neg` and denominator separation. It is partial: it still requires pair cofinality, an intermediate exponent and finite positive strictification. Attempt2 uses `Set.exists_min_image`, `Set.Infinite.sdiff` and exponent asymptotics: these are building blocks but the inequalities and exceptional-set assembly are real proof steps. The isolated `exact?` probes for current and generic forms and `simp only [UniformBound,pairSet]` do not close the iff. Probes precede authored bridge theorems, so cannot rediscover them accidentally. NOT-COMPOSABLE from existing mathlib in<=3 calls. No production inlining is recommended merely because a full inline proof can be made to compile.

[Exact composition probes]({link('composition-executed.lean.txt')}); [raw composition receipt]({link('composition01-receipt.json')}).

Pairwise moral-duplication check:

| A | B | Same statement | Same proof | Decision |
|---|---|---|---|---|
| isDiophantine_iff | private positive-minimum helper | No; helper is one direction at a fixed exponent | Shared reverse direction | Keep helper or general finite-exception API |
| isDiophantine_iff | Roth.eventually_div_rpow_lt | No; latter is pure asymptotics | Forward direction uses gap | Reuse asymptotic ingredient |
| isDiophantine_iff | Roth.reduction | No; reduction changes algebraic real to integral | Both absorb constants | Share gap theorem; no duplicate iff |
| isDiophantine_iff | forall_liouvilleWith_iff | No; unbounded-all-exponents vs bounded cutoff | Different quantifier conversion | Existing theorem is not a replacement |

## Phase7: independent verdict and actionable alternatives

**BORDERLINE-needs-human**, on canonical upstream API design. This is mathematically reusable across arbitrary real irrationality-exponent bounds and genuinely needs proof beyond current building blocks. Verified irrationality removal and parameterized cutoff establish the available stronger statements. The issue is whether to export both pair and uniform predicates or orient their bridges toward existing LiouvilleWith. A bare fixed2 theorem against two project definitions would prematurely settle that choice. Neither the definition's earlier verdict, the usefulness of the final named Roth theorem, nor implementation cost determines this verdict.

Concrete future upstream questions (assessment complete, no user blocker):

'''
for i,q in enumerate(questions,1):report+=f'{i}. {q}\n'
report+=f'''
Retain locally now; a subsequent authorized cleanup can remove hx and change the sole caller to `all_real.mpr`, using the verified source. For upstream, use the provisional new module `Mathlib/NumberTheory/Transcendental/Liouville/Diophantine.lean` importing LiouvilleWith, with the generic cutoff bridge and finite-exception helpers as one designed API. This is a proposed home, not a claimed accepted YES grouping. No existing mathlib-call deletion plan is supported. No PR is opened, and no production source is changed.

## Phase8: evidence and acceptance

[Verification ledger]({link('verification.json')}); [phase tables]({link('phase-checks.json')}); [canonical snapshot]({link('canonical-snapshot.json')}); [portable validator]({link('validate.py')}); [copy manifest]({link('copy-manifest.json')}). Native verification uses standard axioms only and default resources, complete nonpartial diagnostics, zero errors/warnings and no PANIC in any accepted message. Sources/requests are immutable; no sorry, new axiom, unsafe, native_decide or limit raise is accepted. Root acceptance is pending independent review. Final fileend293 dual builds belong to the root's final boundary gate.
'''
(D/'report.md').write_text('\n'.join(l.rstrip()for l in report.splitlines()).rstrip()+'\n')
print('Wrote complete draft report, all phase tables and assessment phase8 pending')
