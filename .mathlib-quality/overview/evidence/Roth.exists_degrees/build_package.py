from pathlib import Path
import json,re,hashlib,sys
D=Path(__file__).resolve().parent;N='Roth.exists_degrees';draft='--draft'in sys.argv
R=Path('/Users/ramin/LEAN/Roth')
def rd(n):return json.loads((D/n).read_text())
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(n):
 z=rd(n)['result'];z=z.get('structuredContent')or json.loads(z['content'][0]['text']);return z.get('result',z)
def msgs(n):
 z=result(n);return z.get('items',z.get('diagnostics',[]))
def link(n):return '['+n+'](../evidence/'+N+'/'+n+')'
labels={'original':('original-executed.lean.txt','original-receipt.json','disk'),
'generic':('generic5-executed.lean.txt','generic05-receipt.json','isolated'),
'recovery':('recovery5-executed.lean.txt','recovery05-receipt.json','disk'),
'callers':('callers5-executed.lean.txt','callers05-receipt.json','disk'),
'composition':('composition6-executed.lean.txt','composition06-receipt.json','isolated'),
'candidate':('candidate6-executed.lean.txt','candidate06-receipt.json','isolated'),
'edges':('edges-executed.lean.txt','edges01-receipt.json','isolated')}
accepted=[]
for label,(src,receipt,fmt)in labels.items():
 if not(D/receipt).exists():
  assert draft,(label,'missing required native receipt');continue
 z=result(receipt);ds=msgs(receipt)
 assert z['success']and not z.get('partial',False)and not z.get('timed_out',False),(label,z)
 assert not[x for x in ds if x['severity']in['error','warning']or x.get('category')=='sorry'],(label,ds)
 assert all('sorryAx'not in x['message']for x in ds)
 q=rd(receipt)
 accepted.append(dict(label=label,source=src,source_sha256=sha(D/src),receipt=receipt,format=fmt,elapsed_ms=q['elapsed_ms'],original_execution_request=q['request'],native_region_start_line=10 if fmt=='disk'else 19,axiom_print_required=label!='candidate',required_info=['DEG278_AUDIT: requested=293; unique=293','DEG278_AUDIT_PRESENT: present=293; values=293']if label=='original'else[]))
other=[]
for p in sorted(D.glob('*-receipt.json')):
 if p.name in [x['receipt']for x in accepted]:continue
 q=rd(p.name);wr=q['executor']['worker_request']
 if wr['operation']not in['diagnostics','run_code']:continue
 other.append(dict(receipt=p.name,source=wr['source'],source_sha256=sha(D/wr['source']),status='rejected; inspect complete raw diagnostics'))
executed={x['source']for x in accepted+other}
preparation=[p.name for p in D.glob('*executed.lean.txt')if p.name not in executed]
type_=rd('native-type.json')['type'];body=(D/'generic5-body.lean.txt').read_text()
generic='variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [FloorRing K]\n'+body.split('theorem separated',1)[1].split(':= by',1)[0].join(['theorem exists_separated_nat_multiples',''])
# Preserve the complete tested source signature, including inherited field binders explicitly above.
put('verification.json',dict(declaration=N,canonical_index=278,completed=False,unresolved=[],accepted=accepted,other_executions=other,preparation_only=preparation,standard_axioms=['propext','Classical.choice','Quot.sound'],attempt_accounting=dict(native_executions=len(accepted)+len(other),accepted=len(accepted),rejected=len(other)),build_gate='Shared baseline clean2467 jobs with fresh17 matching; next required file-end literalbuild289, not278. No new production source.',prefix_control='prefix-controls.json',native_executor='root exclusively'))
verdict='YES-but-generalise-first'
phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7']};phases['8']='pending'
put('assessment.json',dict(declaration=N,canonical_index=278,verdict=verdict,completed=False,allphases='pending',phases=phases,unresolved=[],root_acceptance='pending',parent_verdict_inherited=False,cost_based_verdict=False,reason=['verified removal of δ≤1','finite ordered-floor-field positive-weight abstraction','independent tolerance/lower threshold/growth margin'],questions=[]))
put('overview-entry.json',dict(type=type_,kind='theorem',what='Choose positive natural degrees, larger than10/δ, with strict adjacent ratio and simultaneous weak-lower/strict-upper balanced logarithmic products.',how='Use exists_nat_gt above a finite supremum, then Nat.le_ceil and Nat.ceil_lt_add_one on ceil(s*log(q0)/log(qj)); positivity transports bounds and the factor2 preserves strict separation.',hypotheses='Nonzero finite dimension, δ>0 with original δ≤1, denominators qj>1 and weak adjacent logarithm growth2/δ.',project_dependencies=[],caller_summary=rd('callers.json'),mathlib_api_audit='Existing Nat.ceil_lt_mul is scalar rounding; tendsto_nat_ceil_mul_div_atTop is asymptotic. Neither is a verified existing full finite package; generic helper is newly proved scratch mathematics.',moral_duplications=rd('phase-checks.json')['pairwise_duplications'],generalization=dict(verified=len(accepted)==7,proposed_type=generic,remove=['δ≤1 from original target'],retain=['δ>0 for positive ε=δ/10 and B=10/δ in original quantitative recovery','q>1/log positivity','strict adjacent ratio and strict upper balanced product; weak lower product'],scope='Generic ordered field with FloorRing; arbitrary Finite ι, base b, positive ℓ, ε,B, c>1, arbitrary relation R, unrestricted generic δ. Original full type recovered exactly.'),missing_api='Finite simultaneous positive-weight natural rounding with an arbitrary relative error, lower degree bound and strict separation margin.',junk='Not dead: one complete actual private caller and terminal dependency chain. No ≤3-existing-call replacement verified; retain local wrapper until upstream generic API exists.',action=dict(verdict=verdict,home='Mathlib/Algebra/Order/Floor/Finite.lean (new leaf)',pr_title='feat(Algebra/Order/Floor): balance natural multiples of finite positive weights',next='Run /generalise Roth.exists_degrees and /cleanup on the generic finite-weight lemmas; replace current caller via the verified all-positive-delta recovery.',grouping='Own small balancing+separation PR. Keep separate from accepted YES Roth.eventually_div_rpow_lt and Roth.exists_reduced_approx (analytic/Diophantine interfaces), and Roth.main_lemma (project theorem); progress snapshot confirms those verdicts.',reviewers='Yaël Dillies (a78f66ab84/e06eff5f95) or Seewoo Lee (caabe1c7b0): recent relevant order/floor commits, not endorsements.')))
p=rd('phase-checks.json');lit=rd('literature.json');fm=rd('formal-search-matrix.json')
tables=lambda rows:'\n'.join('| '+' | '.join(str(y).replace('|','\\|').replace('\n',' ')for y in x)+' |'for x in rows)
text='''# Roth.exists_degrees — canonical278

**Verdict: YES-but-generalise-first.** The reusable contribution is finite positive-weight natural
rounding with independent error, lower threshold and growth margin. The exact Roth wrapper is a
corollary. This assessment proposes changes; production Lean files and pins remain unchanged.

## Phase0 — baseline and scope

Shared baseline: clean2467 jobs; all17 source/pin hashes freshly match the tracked shared manifest.
No file-end build is due at278 (next289). See '''+link('baseline-build.txt')+', '+link('inputs.json')+'''.
The declaration resolves at Roth/Main.lean282–317. Entire Main1–588 and LeanEval1–73 were read.
Original re-elaboration copies only the complete target in a fresh namespace; no private helpers
are needed. Loaded original full type, direct kernel constants, standard axioms, and all293 ordered
canonical declarations are independently audited. Printer output explicitly elides78277 characters;
this is **not** a full kernel-body dump. Complete written original proof is retained.

'''+link('original-executed.lean.txt')+'; '+link('original-receipt.json')+'; '+link('native-type.json')+'''.

## Phase1 — mathematical content

Given positive logarithms growing by at least2/δ at each successor, choose positive integer degrees
rj>10/δ so that adjacent degrees satisfy rj/δ<ri. Their logarithmic products all lie in the
half-open interval from r0 log(q0) to (1+δ/10)r0 log(q0). The source chooses a common large integer
scale using Finset.sup', rounds each inverse logarithmic weight upward, and bounds the rounding
error by one. The final factor estimate uses hδ1; the existence assertion itself does not need it.

Full native original type:
```lean
'''+type_+'''
```
Written project dependencies: `[]`; direct kernel project dependencies: `[]`. Arithmetic and order
lemmas are mathlib. Source occurrences, direct type/body consumers, transitive source closure and
implicit simp/typeclass dependencies are distinct scopes. See '''+link('canonical-consumers.json')+'''.

## Phase2 — preliminary checks

SMALL: quantitative helper, no new structure or main named result. Definition-only one-line check:
n/a, theorem. Its short scale/rounding spelling does not establish a three-call composition.

## Phase3 — exhaustive literature

| Channel | Exact query | Title / locator | Finding |
|---|---|---|---|
'''+tables([(x['channel'],rd(x['receipt'])['request']['search_query'][0]['q'],x['title']+'; '+x['locator'],x['summary'])for x in lit['channels']])+'''

Local source: clean.tex1608–1646, §7 eqs51–53. The author notes explicitly request one rounding
lemma. Optional ask_chatgpt_math is unavailable; all remaining named channels were actually queried.
The precise complete sources and own summaries are in '''+link('literature.json')+'''. External response
hashes/bytes/status and exact requests are archived; full article/search bodies are not persisted.
Primary direct access succeeded for Soundararajan/Petrow p56 and the2025/2026 arXiv survey; nLab
returned unsupported XHTML. General rounding/sum-preserving apportionment and characteristic-p
analogues are distinct results. Neither a standard name nor the most general field statement is
attributed to the recent survey's abstract. The broader field form is our tested new proof.

## Phase4a–b — generality

| Parameter | Finding |
|---|---|
'''+tables([(x['parameter'],x['assessment'])for x in p['generality']])+'''

The exact original upper bound δ≤1 is removable with **all** five quantitative outputs retained.
Take ε=δ/10, B=10/δ and c=2 in the generic theorem. Internally use τ=min(δ/10,1/2)>0;
choose a sufficiently large scale using max(B,1/τ). The strict upper error is at most1+τ≤3/2≤2,
so adjacency cancellation still gives rj/δ<ri. Since τ≤δ/10, the original strict upper product bound
survives. This also covers δ≤10; stopping at10 would leave a verified further weakening.
The complete exact old type is recovered by retaining its unused hδ1 binder.

Original δ>0, q>1/log positivity and successor conditions remain in that recovered interface.
Generic δ>0 was independently found unnecessary and removed, since its error and B are independent
positive parameters; that does not authorize removing original δ>0. Zero error and zero weight
contradict the strict upper bound at the base; c=1 with equal weights contradicts strict separation.
The q=1 counterexample blocks merely weakening q>1 to q≥1. See '''+link('edges-executed.lean.txt')+'''.

Proposed complete generic signature (tested section binders included):
```lean
'''+generic+'''
```

'''+link('generic5-executed.lean.txt')+'; '+link('recovery5-executed.lean.txt')+'''.
Verified strictly weaker hypotheses and broader applicability, with modern abstraction. Proof effort is moderate;
cost does not drive the verdict. Natural witnesses and every strict/weak endpoint are preserved.

## Phase4c — modern idioms

| Question | Applies | Restatement | Downstream consequence |
|---|---|---|---|
'''+tables([(x['question'],x['applies'],x['reformulation'],x['downstream'])for x in p['modern9']])+'''

The concrete-via-abstract diagnostic counted the proof: Real.log occurs only in the initial
positivity step after defining ℓ. All subsequent arguments use positive weights. The same generic
proof works for rational weights and arbitrary finite indices; finite height/degree allocations
can reuse it without natural denominator/logarithm presentation. These are mathematical changes,
not a cosmetic rescaling of10. The recovered full original and actual caller guard against changing
meaning. See '''+link('concrete-diagnostic.json')+'''.

## Phase4.5 — infrastructure risks

| Risk | Verdict | Reason |
|---|---|---|
'''+tables([(x['risk'],x['status'],x['reason'])for x in p['infrastructure_risks']])+'''

## Phase4.6 — proof strategy

| Question | Applies | Alternative | Cost |
|---|---|---|---|
'''+tables([(x['question'],x['applies'],x['alternative'],x['cost'])for x in p['proofstrategy5']])+'''

REFACTOR-RECOMMENDED: extract finite balancing and a margin corollary, then recover logarithmic
weights. Existing Nat.ceil_lt_mul may shorten the one-coordinate upper estimate during cleanup.
A filter proof via tendsto_nat_ceil_mul_div_atTop is possible, but finite intersection, choosing an
integer scale, base equality and strict-margin arithmetic still need proof. No filter rewrite was
falsely claimed as a three-call replacement.

## Phase5 — all15 formal cells

| Form | Method | Receipt | Result |
|---|---|---|---|
'''+tables([(x['form'],x['method'],link(x['receipt']),x['assessment'])for x in fm['cells']])+'''

Current means the full logarithmic quantitative result; standard means finite relative-error
ceiling rounding; abstract means arbitrary finite positive weights over an ordered floor field.
Additional abstract-field remote searches and one local retry are archived. Local states were
error/error/warming, followed by error on retry: returned candidates only, **no absence inference**.
Remote indexes may differ from the pin. Pinned source and native candidate checks establish the
actual signatures: Nat.le_ceil, Nat.ceil_lt_add_one, Nat.ceil_natCast, exists_nat_gt,
Finset.le_sup', Nat.ceil_lt_mul/ceil_le_mul, and tendsto_nat_ceil_mul_div_atTop.
The latter two kinds address scalar bounds or asymptotic convergence, not this synchronized
finite package. Dirichlet approximations and additive Roth numbers are different problems.
The untruncated qualified-name grep and compiled exact?/simp negative closure probe supplement
search; they do not logically prove no conceivable composition exists.

## Phase5.5 — statement shape

| Check | Assessment |
|---|---|
'''+tables([(x['check'],x['assessment'])for x in p['statement_shape3']])+'''

RESTATE-BEFORE-SHIP: generic natural witness/product normal form; base b, independent ε,B and margin
c. Original signature remains the application interface in the tested recovery. No new class or
custom positivity predicate is introduced. Generic Finite replaces unused-in-type Fintype, and
FloorRing.archimedean infers Archimedean rather than retaining a redundant instance.

## Phase6.0 — callers and inline audit

Exactly one explicit proof call: Roth.exists_roth_approximants_aux at Main440, whole declaration
429–450; zero external-to-file calls. Main33 is documentation, not a proof call. Its complete body
was tested twice: literal original target proof inlined into the actual obtain, then the target
call replaced by the all-positive-delta recovery. Native equality checks preserve the exact original
private caller signature. Its δ≤1 remains for antitonicity and degree≥3. The terminal source closure
is roth_of_isIntegral→roth→roth_rat/LeanEval.thueSiegelRoth; no terminal replay is claimed.
'''+link('callers5-executed.lean.txt')+'; '+link('callers.json')+'''.
Fresh rg --no-ignore and tracked git grep agree; inline-pattern search found the source rounding
proof and consumers of its outputs, no independent duplicate degree selector.

## Phase6 — composition and duplication

NOT-COMPOSABLE from at most three existing mathlib calls on the verified evidence. Nat.ceil_lt_mul
needs a supplied one-coordinate lower threshold. Finset.le_sup' and exists_nat_gt choose a common
scale, but proving positivity, base equality, both products and strict relation preservation still
requires nontrivial multiplication/order reasoning. The compiled generic probe rejects simp and
exact? before writing the actual new proof. New balanced/separated helpers are **not** existing
mathlib replacements. The old recovery's one generic call is a call to our new theorem.

| A | B | Same statement | Same proof | Action |
|---|---|---|---|---|
'''+tables([(x['a'],x['b'],x['same_statement'],x['same_proof'],x['verdict'])for x in p['pairwise_duplications']])+'''

## Phase7 — actionable verdict

YES-but-generalise-first, for verified weakening plus modern idiom. The concrete missing API is
finite synchronized natural rounding at a prescribed multiplicative tolerance and degree floor,
with a strict relation-margin corollary. Existing scalar ceiling and limit APIs do not discharge
that complete package. The known Roth degree choice supplies a concrete application; arbitrary
positive rational/real weights, finite index sets and independent tolerances are additional uses.
Retain the project wrapper until a generic upstream theorem is available, then replace its single
actual call using the exact tested recovery. Do not delete its required caller δ≤1 argument.

Proposed home: `Mathlib/Algebra/Order/Floor/Finite.lean`, a **new leaf** importing finite-supremum and
ordered-floor APIs. Floor.Semifield has assert_not_exists Finset, so placing this finite result
there would violate current import layering. Proposed PR title: **feat(Algebra/Order/Floor): balance
natural multiples of finite positive weights**. Group the new balanced theorem and separated
corollary together. Fresh accepted progress confirms YES for Roth.eventually_div_rpow_lt,
Roth.exists_reduced_approx and Roth.main_lemma; those belong to separate analytic/Diophantine or
project-theorem PRs, not this foundational floor API. No earlier verdict is inherited.

Before PR: `/generalise Roth.exists_degrees`; `/cleanup` on the new leaf/balancing lemmas; minimize
imports and split the constructive scale estimate if useful. Reviewer candidates based on actual
recent relevant commits: Yaël Dillies (a78f66ab84/e06eff5f95) or Seewoo Lee (caabe1c7b0). This is a
routing suggestion, not reviewer approval. See '''+link('reviewer-commits.json')+'''.

## Phase8 — evidence and limits

Root exclusively executed all native/project-LSP requests. Stable18 mathlib-only and disk9 controls
are archived and unchanged; only candidate06 adds the freshly authorized Floor.Semifield import; its exact19prefix/hash authorization is archived. No inherited exception is used. All
sources are at most100 columns. Required accepted proofs use only propext, Classical.choice and
Quot.sound. Rejected generic attempts and every preparation-only version remain separately
accounted for, including recovered sorryAx in failed generic01/04 (never accepted proof evidence).
'''+link('verification.json')+'; '+link('prefix-controls.json')+'; '+link('formal-search-matrix.json')+'''.

Completion remains pending until the required exact native receipts, current manifest, both
portable layouts and secret scan pass. Root acceptance is a separate pending review.
'''
(D/'report.md').write_text('\n'.join(line.rstrip() for line in text.splitlines()) + '\n')
print('Draft package prepared: accepted',len(accepted),'required7; completed=false; phase8pending')
