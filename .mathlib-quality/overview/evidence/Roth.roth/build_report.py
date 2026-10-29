from pathlib import Path
import json,re
D=Path('/private/tmp/roth-overview/assess/Roth.roth');N='Roth.roth'
def rd(n):return json.loads((D/n).read_text())
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def res(n):
 q=rd(n)['result'];q=q.get('structuredContent')or json.loads(q['content'][0]['text']);return q.get('result',q)
messages=[x['message']for x in res('original-receipt.json')['items']]
full=next(x.split('ROTH288_FULL_TYPE: ')[1]for x in messages if x.startswith('ROTH288_FULL_TYPE:'))
raw=next(x.split('some ([',1)[1].rsplit('])',1)[0]for x in messages if x.startswith('ROTH288_BODY_CONSTANTS:'))
constants=[x.strip()for x in raw.split(',')];order=rd('canonical-snapshot.json');names={x['name']for x in order};deps=[x for x in constants if x in names]
dump('native-type.json',dict(full_type=full,type=full,full_kernel_printer_body=False,elided_characters=[9674],full_kernel_constant_inventory=True,scope='Exact original target only replay, imported public project ingredients; full original type/axioms/value constants audited.'))
dump('canonical-consumers.json',dict(type_consumers=[x for x in messages if x.startswith('ROTH288_DIRECT_TYPE_CONSUMER:')],body_consumers=[x for x in messages if x.startswith('ROTH288_DIRECT_CONSUMER:')],audit=[x for x in messages if x.startswith('ROTH288_AUDIT')]))
dump('project-dependencies.json',dict(kernel_raw_constants=constants,canonical_dependencies=deps,scope='Direct kernel value constants mapped to canonical project names; binder annotations count, arbitrary transitive/simp closure does not.'))
proposed='∀ {α p : ℝ}, IsAlgebraic ℚ α → LiouvilleWith p α → p ≤ 2'
o=dict(type=full,what='Roth’s theorem for irrational real algebraic numbers: infinitely many unreduced positive-denominator pair approximations force exponent at most2.',how='Assume κ>2, clear denominators to obtain a positive integer multiple of α integral over ℤ, absorb that factor by lowering κ to κ′∈(2,κ), then contradict the integral Roth theorem. Its underlying multivariate auxiliary-polynomial argument compares integral lower and Taylor upper bounds.',hypotheses=['Irrational real α','α algebraic over ℚ','Infinite set of integer/natural pairs with q>0 and |α−h/q|<q^(−κ), arbitrary real κ'],project_dependencies=deps,caller_summary='Two actual proof/body consumers: Roth.roth_rat Main583 and LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth LeanEval64; no kernel type consumers. Full caller bodies and full LeanEval replay with target proof inlined, original signatures retained, target-free assertions verified.',mathlib_api_audit='All15 search cells executed; local current/standard errors and abstract warming are limitations. Liouville degree-dependent bound and Dirichlet exponent2 existence do not supply Roth’s sharp upper bound. Pinned LiouvilleWith doc explicitly names the missing p>2 transcendence implication.',moral_duplications='Integral Roth is the proof core, general algebraic endpoint adds substantive scaling/exponent-loss transport; rational-value and uniform lower-bound endpoints are equivalent formulations for irrational α through genuine bridges.',generalization=dict(verified=True,reason='MODERN-IDIOM',proposed_type=proposed,exact_equivalence='For irrational α, the all-exponent pair-bound property iff ∀ {p}, LiouvilleWith p α → p≤2; modern algebraic endpoint derives irrationality only in p>2 case.',native_scope='Fresh conditional bridge adapted from287, compiled independently with algebraicity premises; original proof replay validates the mathematical premise. No independent mathlib Roth proof claimed.'),missing_api=['Sharp exponent2 exclusion for algebraic real LiouvilleWith values','New bounded-denominator/frequently transport and exponent-family equivalence','Staged auxiliary polynomial/Hasse/Taylor/index/Roth-main-lemma prerequisites'],junk='Keep the named BIG endpoint; four-line assembly and two callers do not reduce the theorem to existing mathlib content.',action='Expose the verified algebraic LiouvilleWith exponent bound, retain classical finite/pair corollaries, and stage after accepted integral Roth/main-lemma prerequisites; /generalise and /cleanup before PR.')
dump('overview-entry.json',o)
def link(n,label=None):return '['+(label or n)+'](../evidence/'+N+'/'+n+')'
def table(head,rows):return '| '+' | '.join(head)+' |\n|'+ '|'.join(['---']*len(head))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','/')for x in r)+' |'for r in rows)+'\n'
ph=rd('phase-checks.json');lit=rd('literature.json')
s='''# `Roth.roth` — canonical288

Verdict: **YES-but-generalise-first**, reason **MODERN-IDIOM**. This is the named BIG Roth theorem
for irrational real algebraic numbers. Its short reduction proof does not make the full mathematical
content an existing mathlib composition. No parent verdict is inherited and cost is not a factor.

## Phase0 — baseline and scope

Fresh17 source/pin hashes match the tracked shared manifest; baseline build passed2467jobs.
The accepted file-end228 full build remains reusable; next literal file-end build is289.
Full Main588 and LeanEval66 were read, including algebraic-integral reduction and the entire
multivariate integral proof. Local paper§6 reduction and §7 conclusion were read. Production,
pins, Git, overview and progress remain unchanged. Root exclusively executed native/LSP requests.
Original replay contains exactly this target in a fresh namespace, with no helper closure needed;
public reduction and integral theorem remain imported. Full unrelated Main replay is not claimed.

'''+link('inputs.json')+'; '+link('baseline-build.txt')+'; '+link('source-Main.lean.txt')+'; '+link('source-LeanEval.lean.txt')+'.\n\n'
s+='''## Phase1 — exact statement and mathematics

```lean
'''+full+'''
```

The pairs are unreduced; q is a positive natural denominator, h an integer, κ any real.
Assuming κ>2, choose positive M with Mα integral. Removing finitely many bounded-denominator
solutions preserves infinitude. Multiplication (h,q)↦(Mh,q) is injective. Choose κ′=(κ+2)/2;
eventually M/q^κ<1/q^κ′, so Mα has infinitely many κ′ approximants and remains irrational.
The integral theorem forces κ′≤2, a contradiction.

The integral theorem is the hard Roth mathematics: choose a monic integer equation and parameters
m,δ; select reduced approximants with rapidly growing denominators and balanced r_j log q_j.
The main lemma supplies a multivariate integer Q of high index at α, small Hasse derivatives and
nonzero value at the approximants. Clearing denominators bounds that value below; Taylor expansion
and the index bound estimate it above. Logarithmic comparison contradicts m(1+4δ)/(γ−η)<κ.
Generic order closure supplies only the final contradiction, not this polynomial theorem.

Direct canonical dependencies in the elaborated value: '''+', '.join(deps)+'''.
Full kernel constant inventory and full type/axioms are retained. The pp.all proof-body printer
elides9674characters; no full kernel-body pretty-print is claimed. Exact complete original source
is retained and re-elaborated, with original/replay type agreement by proof irrelevance.

'''+link('original-executed.lean.txt')+'; '+link('original-receipt.json')+'; '+link('local-section6.tex.txt')+'; '+link('local-section7.tex.txt')+'.\n\n'
s+='''## Phase2 — size and one-line check

BIG: named Roth theorem, main project endpoint, classical standard result. The four-line assembly
uses project Roth.reduction and Roth.roth_of_isIntegral, neither an existing mathlib replacement.
Definition-only one-line test: n/a theorem. All six infrastructure rows are n/a theorem; no new
instance, coercion, reducibility or diamond structure is introduced.

## Phase3 — exhaustive literature

'''+table(['Channel','Exact actual query','Finding'],[(x['channel'],x['query'],x['summary'])for x in lit['channels']])+'''
Local clean.tex§6/7 is available and read. Optional ask_chatgpt_math is unavailable, recorded n/a.
Every named channel was queried, including distinct /ncatlab and /nlab namespaces. Searches return
out-of-namespace results honestly; Stacks supplied no usable statement. The nLab Vojta open failed
unsupported XHTML; full ICM PDF open exceeded tool size, so only its returned primary search extract
is used. Web receipts retain exact requests, response hashes/bytes/status and clean locators,
with our concise summaries, and no full third-party article/search bodies. Signed or credential
query URLs are not retained. Initial recent query confused additive-combinatorics Roth; targeted
Diophantine retry found the relevant papers.

Standard name: Thue–Siegel–Roth theorem. Standard equivalent real forms are finite exceptions at
every exponent2+ε, infinite-implies-exponent≤2, and ε-dependent positive uniform error constants.
[Roth1955 original](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F), Mathematika2(1),1–20,
provides publication metadata and the degree-dependent Liouville precursor.
[Roth’s1958 lecture](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), opening§1–2 search extract,
states the exponent bound and integral reduction.
[Goel–Lunia–Ray2026](https://arxiv.org/html/2502.00731v2), §3.2 Theorems3.2–3.3,
gives number-field finite-place versions. These use heights/valuations and are not mechanical
weakenings of this real proof. [Hindes2022](https://arxiv.org/abs/2209.09182), abstract,
warns the characteristic-p analogue fails. We do not claim an arbitrary-field generalization.

'''+link('literature.json')+'; '+', '.join(link(f'web-batch{i}.json',f'web{i}')for i in range(7))+'.\n\n'
s+='## Phase4a–b — complete generality\n\n'+table(['Parameter','Status','Reason'],ph['generality'])+'''
Classical form: MAXIMALLY GENERAL within real rational approximation; no original hypothesis
can simply be dropped. κ>0 is unnecessary and absent. Threshold2 is mathematical and sharp;
finite-for-κ>2 is equivalent, whereas finiteness atκ=2 is false for irrational reals by Dirichlet.
A generic threshold would only abstract an order tautology after assuming Roth content.

Verified modern restatement:
```lean
'''+proposed+'''
```
The isolated source reconstructs the exact pair predicate using mathlib operations and guards
Roth.roth/Roth.approxSet absence. It takes classical Roth as an explicit premise; it does not
pretend this premise is already mathlib. The all-exponent classical property for irrational α
is equivalent to the all-exponent LiouvilleWith upper bound. One direction uses bounded-denominator
finiteness to produce frequent denominators with C=1. Conversely, LiouvilleWith p α supplies
constant1 approximants at the smaller exponent (p+2)/2 through frequently_lt_rpow_neg.
The modern algebraic theorem needs no explicit irrationality binder: split p≤2 first, and when
p>2 use LiouvilleWith.irrational with 1<p. The original theorem is recovered using irrationality.
This is NOT a fixed-exponent equivalence between constant1 pair membership and existential C.
The bridge is new conditional proof, adapted from accepted287 syntax and independently compiled
with algebraicity premises; no prior verdict or unverified proof is inherited.

## Phase4c — modern idioms

'''+table(['Question','Applies','Concrete consequence'],ph['modern9'])+'''
Modern-idiom verdict: verified and a real organizational improvement. Existing mono, exponent-loss,
rational/integer/natural scaling and rational-translation API accepts LiouvilleWith directly.
This meets the pinned module’s explicit missing p>2 transcendence implication. The original pair
corollary stays useful; no whole development need be generalized to heights or arbitrary fields.

## Phase4.5 — six infrastructure risks

'''+table(['Risk','Status','Reason'],[(x['risk'],x['status'],x['reason'])for x in ph['infrastructure_risks']])+'''
## Phase4.6 — proof strategy

'''+table(['Question','Applies','Alternative'],ph['proofstrategy5'])+'''
REFACTOR-RECOMMENDED for public API: preserve integral auxiliary-polynomial proof and reduction,
expose LiouvilleWith exponent exclusion; stage reusable Hasse/Taylor/index/main-lemma prerequisites.
No alternative generic filter/order theorem supplies the Roth arithmetic.

## Phase5 — all fifteen formal cells

'''+table(['Form','Method','Receipt'],[(x['form'],x['method'],link(x['receipt']))for x in rd('formal-search-matrix.json')['cells']])+'''
All methods were actually executed. Finder uses externalv4.28 index; external search versions can
differ from the pin. Actual local current/standard returned index:error and abstract warming;
no absence conclusion is drawn. The untruncated source search additionally checks full name and
statement variants; no truncation hides additive-combinatorics Roth or Lüroth collisions.

Positive candidates read from the pin and checked natively: Liouville.exists_pos_real_of_irrational_root
has polynomial-degree exponent, insufficient for sharp2 in all degrees. LiouvilleWith.irrational
excludes rationals above1, while mono/frequently_lt_rpow_neg/affine invariance transport approximation
information. Dirichlet’s infinite rational exponent2 theorem is a lower-side optimality statement.
The almost-everywhere ae_not_liouvilleWith theorem cannot specialize to every algebraic irrational.
Pinned LiouvilleWith introduction explicitly identifies the unproved Roth implication. Existing
Liouville.transcendental assumes approximations of every natural order, far stronger than one p>2.
Negative exact?/aesop probes compile, recording failure of those generic routes, not a universal
proof of absence. New scratch bridges never count as existing mathlib replacement theorems.

'''+link('mathlib-source-0.lean.txt')+'; '+link('mathlib-source-1.lean.txt')+'; '+link('mathlib-source-2.lean.txt')+'; '+link('modern2-executed.lean.txt')+'.\n\n'
s+='## Phase5.5 — statement shape\n\n'+table(['Check','Verdict','Reason'],ph['statement_shape3'])+'''
Finite-for-κ>2 equivalence and original recovery are native verified. The α=0 infinite unreduced
pair counterexample for every κ confirms irrationality is essential in the original. LiouvilleWith1
holds even for0, so irrationality is inferred only with p>1. The full LeanEval bridge proves the
uniform lower-bound equivalence for irrational α; no equivalence on all reals is asserted.

## Phase6.0 — actual callers, inline audit and duplications

'''+table(['Caller','Location','Uses','Inlining'],[(x['name'],x['file']+':'+str(x['line']),x['uses'],'Full original body, original signature, exact target proof inlined')for x in rd('callers.json')['explicit_proof_callers']])+'''
One same-file and one external-file direct proof call. Documentation is excluded from the count.
Canonical293 audit independently finds exactly these two direct body consumers and no type consumer;
requested/unique/present/values are each293. No simp attribute and no arbitrary simp/transitive
closure claim. Both complete caller bodies, and the whole LeanEval module, were re-elaborated.
Kernel assertions confirm both endpoint proof values contain no direct target reference.

Integral Roth is the proof core; algebraic Roth adds integer scaling and exponent loss. roth_rat
maps rational values injectively to reduced numerator/denominator pairs. LeanEval minimizes the
weighted error on finitely many exceptions and handles the remaining pairs. Their mathematical
content is equivalent under irrationality, but these are actual representation bridges, not
identical proof copies. No independent full Roth theorem is silently rederived inline elsewhere.
Inlining succeeds, but does not make Roth junk or a composition from existing mathlib.

'''+link('callers.json')+'; '+link('source-search.json')+'; '+link('tracked-source-search.json')+'; '+link('inline-search.json')+'; '+link('callers2-executed.lean.txt')+'.\n\n'
s+='''## Phase6 — actual composition experiments

NOT-COMPOSABLE from≤3 existing mathlib calls. Degree-dependent Liouville cannot give2 in arbitrary
degree. Irrationality/affine/mono/exponent-loss lemmas do not exclude LiouvilleWith p above2.
Native exact?/aesop attempts fail to derive the bound. Set/order finiteness equivalences consume
Roth content. The short original invokes project reduction and integral Roth, not mathlib Roth.
No simp-only closure is promoted as new arithmetic. The independently adapted exponent-family
bridge is new conditional mathematics, separate from existing pinned API.

## Phase7 — verdict and concrete upstream plan

**YES-but-generalise-first**, MODERN-IDIOM: expose the verified algebraic LiouvilleWith exponent
bound and recover classical finite/pair corollaries. This fills the explicit p>2 transcendence gap
named in the pinned LiouvilleWith introduction, beyond elementary irrationality, affine invariance
and degree-dependent Liouville. It is a terminal addition to the staged Roth proof, not a request
to mechanically port the entire proof to number-field heights. Irrationality is safely removed
only in the modern theorem, whose approximation premise excludes exact equality.

Exact proposed new home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean`.
Proposed PR title: `feat(NumberTheory/DiophantineApproximation): prove Roth's theorem for algebraic reals`.
Group the endpoint with already accepted YES Roth.roth_of_isIntegral and Roth.main_lemma; ship accepted
Hasse/Taylor/index prerequisites earlier. The progress snapshot actually confirms these assessments;
accepted assessment does not mean the theorem already exists in mathlib. Avoid import cycles:
prove the integral core first, then scaling/algebraic endpoint; do not use Roth.roth to prove its
own upstream integral premise.

Reviewer candidates from actual relevant recent history: Jovan Gerbscheid’s
[filter-negation change2025-11-19](https://github.com/leanprover-community/mathlib4/commit/66b2a6571bcd28f2ab6cd8e15f195d394fc175bd)
touches LiouvilleWith; Marcelo Lynch’s2026-08-11 exact-file cleanup also supplies a recent reviewer
candidate. This is history-based selection, not an endorsement or claim they accepted the proposal.
Pre-PR: `/generalise Roth.roth` against the exact modern signature, then
`/cleanup Roth/Main.lean Roth.roth`; stage prerequisite imports, names and documentation before PR.

'''+link('reviewer-specific-commits.json')+'; '+link('progress-snapshot.json')+'.\n\n'
s+='''## Phase8 — actual verification and portability

Five accepted executions: original exact replay/type/axioms/canonical293; complete caller inlining;
clean finite/recovery/rational guard; caller target-free assertions; isolated modern bridge/recovery.
All actual root receipts and source hashes/timings are retained. Only propext, Classical.choice,
Quot.sound occur in accepted proofs. Failed shape01 and modern01, with recovered sorryAx, remain
separately rejected and never count as verification. Original #print elision is disclosed above;
full unelided constant/type messages and exact written source remain available.

Stable mathlib18 and disk9 hashes remain fixed. Root freshly authorized precisely LiouvilleWith as
isolated19 after pinned-header read; prefixSHA effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc.
No project import in isolated probes; no new axioms, unsafe/native_decide or raised limits.
The portable read-only validator checks current manifest/hash/bytes/links, both layouts, actual
native complete success and all source/pin controls. Completion remainsfalse/phase8pending until
actual draft scratch/integrated-layout/secret gates pass; final completion is settrue only afterward.
Root acceptance stayspending for independent review. Native execution requests are released.
Initial packaging-only draft validation rejected a normalized copy of the disk prefix; exact control
bytes were restored before the successful draft gates. Both rejected packaging receipts remain.
No executed Lean source or raw receipt changed. Copied prefixes retain their exact EOF whitespace;
only authored report/preparation scripts are normalized, and generators do not normalize prefixes.

'''+link('verification.json')+'; '+link('validate.py')+'; '+link('copy-manifest.json')+'.\n'
(D/'report.md').write_text('\n'.join(l.rstrip()for l in s.rstrip().splitlines())+'\n')
print('Fresh report/overview written; completion state unchanged')
