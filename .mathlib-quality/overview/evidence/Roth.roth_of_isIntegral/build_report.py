from pathlib import Path
import json,hashlib,re
D=Path('/private/tmp/roth-overview/assess/Roth.roth_of_isIntegral');R=Path('/Users/ramin/LEAN/Roth');N='Roth.roth_of_isIntegral'
def rd(n):return json.loads((D/n).read_text())
def dump(n,x):(D/n).write_text(json.dumps(x,indent=2)+'\n')
def res(n):
 q=rd(n)['result'];q=q.get('structuredContent')or json.loads(q['content'][0]['text']);return q.get('result',q)
def items(n):
 q=res(n);return q.get('items',q.get('diagnostics',[]))
messages=[x['message']for x in items('original-receipt.json')]
full=next(x.split('INT287_FULL_TYPE: ')[1]for x in messages if x.startswith('INT287_FULL_TYPE:'))
nt=dict(type=full,full_type=full,full_kernel_printer_body=False,elided_characters=[101777,462],body_inventory='constants01-receipt.json',scope='Exact original target and five private helpers replayed; type agreement; original loaded kernel type/value audited. Printer body elided; exact complete target source retained.')
dump('native-type.json',nt)
dump('canonical-consumers.json',dict(type_consumers=[x for x in messages if x.startswith('INT287_DIRECT_TYPE_CONSUMER:')],body_consumers=[x for x in messages if x.startswith('INT287_DIRECT_CONSUMER:')],audit=[x for x in messages if x.startswith('INT287_AUDIT')]))
order=rd('canonical-snapshot.json');mapping={('_private.'+x['file'][:-5].replace('/','.')+'.0.'+x['name']if x['visibility']=='private'else x['name']):x['name']for x in order}
raw=[x['message'].split(': ',1)[1]for x in items('constants01-receipt.json')if x['message'].startswith('INT287_BODY_CONSTANT:')]
deps=[mapping[x]for x in raw if x in mapping];dump('project-dependencies.json',dict(kernel_raw_constants=raw,canonical_dependencies=deps,scope='Direct value constants that occur in canonical293; includes elaborated binder/type annotation constants, excludes generated proof implementation names.'))
proposed='∀ {α p : ℝ}, IsIntegral ℤ α → LiouvilleWith p α → p ≤ 2'
o=dict(type=full,what='Roth’s theorem for irrational real algebraic integers: infinitely many integer/natural pair approximations force exponent at most2.',how='Choose monic equation, m and δ via exists_roth_parameters_aux; choose reduced approximants and balanced degrees; combine main_lemma, cleared-denominator integer lower bound and Taylor upper bound; roth_log_bound_aux contradicts the exponent gap.',hypotheses=['Real α irrational','α integral over ℤ','Approximation set of positive-denominator integer/natural pairs infinite at real exponent κ'],project_dependencies=deps,caller_summary='One direct source/kernel-value caller Roth.roth at Main577; no direct type consumer or external-to-file proof call. Full caller inlining plus complete roth_rat and LeanEval bodies verified.',mathlib_api_audit='Pinned LiouvilleWith is the useful existing predicate; current mathlib Liouville bound depends on polynomial degree and Dirichlet proves exponent2 existence, neither proves Roth exponent≤2. All15 actual search cells executed; local index:error honestly limited.',moral_duplications='Roth.roth is reduction-based algebraic extension; Roth.roth_rat and LeanEval endpoint are equivalent public formulations with genuine representation bridges, not independent copies of the proof.',generalization=dict(verified=True,reason='MODERN-IDIOM',proposed_type=proposed,exact_equivalence='For irrational α, classical all-exponent pair bound iff ∀ {p}, LiouvilleWith p α → p≤2; modern integral theorem derives irrationality only in p>2 branch.',native_scope='Mathlib-only new conditional bridge plus original exact proof/type agreement; no independent mathlib Roth proof claimed.'),missing_api=['New exponent-family LiouvilleWith bridge and bounded-denominator/frequently transport','Actual Roth exponent2 exclusion for algebraic integers; pinned LiouvilleWith doc names this missing theorem','Staged Hasse/Taylor/index and main-lemma dependencies'],junk='Keep the mathematical result; one direct caller and short orchestration do not erase a named main theorem. No deletion based on generic order closure.',action='Upstream LiouvilleWith integral exponent theorem with classical finite/pair corollaries; /generalise and /cleanup before PR, stage after accepted main_lemma and prerequisite API.')
dump('overview-entry.json',o)
ph=rd('phase-checks.json');lit=rd('literature.json')
def table(head,rows):return '| '+' | '.join(head)+' |\n|'+ '|'.join(['---']*len(head))+'|\n'+'\n'.join('| '+' | '.join(str(x).replace('|','/')for x in r)+' |'for r in rows)+'\n'
def link(n,label=None):return '['+(label or n)+'](../evidence/'+N+'/'+n+')'
s='''# `Roth.roth_of_isIntegral` — canonical287

Verdict: **YES-but-generalise-first**, reason **MODERN-IDIOM**. This is the named BIG integral
Roth theorem. Its short assembly proof is not a composition from existing mathlib Roth content.

## Phase0 — baseline and scope

Fresh17 production/pin hashes match the tracked shared input manifest; baseline `lake build`
completed successfully with2467jobs. File-end228 successful build is reusable;287 is not a file-end
build gate (next289). No production source, pin, Git, progress, or overview mutation was performed.

Read full Main588 and LeanEval66; read the complete parameter/approximant/degree/Taylor/integer
lower-bound/log contradiction chain and local paper§7, equations46–54. Original replay copies the
exact target plus its five necessary private helper bodies in a fresh namespace and imports
existing public ingredients. Full unrelated Main replay is not claimed or required by the minimal
replay addendum. All native/LSP execution was performed by root; workers prepared immutable sources.

'''+link('inputs.json','Fresh inputs')+'; '+link('baseline-build.txt','baseline')+'; '+link('source-Main.lean.txt','full Main')+'; '+link('source-LeanEval.lean.txt','full LeanEval')+'; '+link('original-executed.lean.txt','exact original replay')+'.\n\n'
s+='''## Phase1 — statement and mathematical proof

For an irrational real algebraic integer α, if infinitely many pairs (h,q) in ℤ×ℕ, q>0,
satisfy |α−h/q|<q^(−κ), then κ≤2. Approximants need not be reduced in this set. The exponent
is an arbitrary real; the proof assumes κ>2 for contradiction and derives its positivity.

```lean
'''+full+'''
```

Choose a monic integer equation for α, a coefficient bound A, a large dimension m and small δ
with m(1+4δ)/(γ−η)<κ. Irrationality turns infinitely many unreduced pairs into reduced fractions
with unbounded denominators, so one selects rapidly growing q_j and balances r_j log q_j.
Roth.main_lemma supplies an integer Q with high index at α, bounded derivatives and nonzero value
at the rational approximants. Clearing denominators gives 1≤∏q_j^r_j |Q(h/q)|. Taylor expansion
and the index lower bound give a strict upper estimate. The coefficient/degree products are
absorbed into q_0 powers. Taking logarithms yields (γ−η)κ<m(1+4δ), contradicting the chosen gap.
These are the actual arithmetic ingredients, not generic order lemmas furnishing Roth’s theorem.

'''+link('local-section7.tex.txt','Paper§7')+'; '+link('constants01-receipt.json','complete unelided constant inventory')+'.\n\n'
s+='''## Phase2 — size and definition check

BIG: named after Roth and explicitly listed as a project main result. Definition-only one-line
check: n/a, theorem. The17-line target orchestration invokes the substantive multivariate proof.
A single direct caller is an API-granularity observation, not evidence the named result is junk.

## Phase3 — exhaustive literature

'''+table(['Channel','Actual query','Finding'],[(x['channel'],x['query'],x['summary'])for x in lit['channels']])+'''
Optional ask_chatgpt_math was unavailable; its standard-form/generality/history query was not run.
Local clean.tex§7 was read completely. General web queries were three distinct specific/general/
alias forms. Additional independent channel retries and primary opens are retained. Search output
hashes/byte counts/status and clean titles/URLs are stored; full third-party bodies are not stored.
Returned signed URL queries were discarded, never used as source evidence. Namespace misses and
nLab fetch failure are limitations, not proofs of mathematical absence.

Standard concept: Thue–Siegel–Roth theorem. The real rational result has equivalent finite-exception,
exponent-bound and ε-dependent positive lower-bound forms. Algebraic-integral reduction is
classical. Number-field/place/product-formula and subspace theorems are broader results requiring
new machinery here; they are not a verified mechanical generalization of this implementation.
Positive-characteristic analogues are not valid without additional hypotheses.

Primary locators: [Roth1955, Mathematika2,1–20](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F);
[Roth’s1958 lecture, opening§1–2](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf);
[Goel–Lunia–Ray2026,§3.2 Theorems3.2–3.3](https://arxiv.org/html/2502.00731v2);
[Hindes2022, abstract](https://arxiv.org/abs/2209.09182).

'''+link('literature.json','Literature records')+'; '+', '.join(link(f'web-batch{i}.json',f'web{i}')for i in range(9))+'.\n\n'
s+='## Phase4a–b — generality\n\n'+table(['Parameter','Assessment','Reason'],ph['generality'])+'''
The classical pair statement has no safely droppable hypothesis. Integral→algebraic is implemented
by the following project theorem Roth.roth using reduction; it is not an existing mathlib theorem
and is not the basis of this verdict. The verified modern restatement is:

```lean
∀ {α p : ℝ}, IsIntegral ℤ α → LiouvilleWith p α → p ≤ 2
```

This accepts the existing existential-constant predicate and derives irrationality when p>2;
for p≤2 the conclusion is immediate. The bridge is an equivalence of the **all-exponent bounds**
for irrational α, not equivalence of fixed-C=1 pair membership with LiouvilleWith at one exponent.
Forward transport chooses q=(p+2)/2 and uses frequently_lt_rpow_neg; the reverse constructs
constant1 LiouvilleWith from unbounded positive denominators. The exact original pair predicate
is reconstructed from mathlib operations, and target absence is guarded with #check_failure.
The isolated proof takes the classical Roth theorem as an explicit premise. Together with the
separately replayed original theorem and identical pair predicate, this verifies the proposed
restatement and recovery modularly; it does not independently prove Roth in mathlib.

## Phase4c — all nine modern idioms

'''+table(['Question','Applies','Concrete consequence'],ph['modern9'])+'''
Modern-idiom verdict: available and verified. Use LiouvilleWith so mono, rational affine invariance
and exponent-loss API apply directly. The new bridge proofs are original scratch work. No cost
or inherited verdict enters the decision.

## Phase4.5 — infrastructure

Theorem: all six definition risks are n/a (diamond, reducibility leak, noncanonical unfolding,
instance priority, universe polymorphism and coercion ambiguity). No new instance or definition
is proposed by the original declaration. Scratch pairSet is a test representation only.

## Phase4.6 — proof strategy

'''+table(['Question','Applies','Alternative'],ph['proofstrategy5'])+'''
REFACTOR-RECOMMENDED for public API organization: preserve the finite multivariate arithmetic
proof, expose exponent exclusion through LiouvilleWith, and stage the missing Hasse/Taylor/index/
main-lemma API. Generic filter transport alone does not replace the proof.

## Phase5 — fifteen formal search cells

'''+table(['Form','Method','Receipt'],[(x['form'],x['method'],link(x['receipt']))for x in rd('formal-search-matrix.json')['cells']])+'''
All methods actually executed. Finder’s external defaultv4.28.0 index and current web docs may
differ from the pin. Root local search returned index:error for all three queries; names returned
were retained and source-checked, but no local absence conclusion is made. Untruncated whole-tree
full-name search additionally excludes confusing this theorem with additive-combinatorics Roth
or Lüroth. Negative exact?/aesop probes are compile-checked search outcomes, not an absolute proof
that no possible mathlib derivation exists.

Closest pinned candidates: Liouville.exists_pos_real_of_irrational_root supplies a bound depending
on polynomial degree, insufficient for universal threshold2. LiouvilleWith.irrational only excludes
rationals above exponent1; mono/exponent-loss/affine invariance transport existing approximation
information. Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational is the opposite-direction
Dirichlet optimality statement. ae_not_liouvilleWith is almost-everywhere, not pointwise on every
algebraic irrational. None is a full Roth replacement. Pinned LiouvilleWith module introduction
explicitly names the missing p>2 algebraic-transcendence implication.

'''+link('full-name-search.json','Whole-tree search')+'; '+link('mathlib-source-0.lean.txt','LiouvilleWith')+'; '+link('mathlib-source-1.lean.txt','Liouville bound')+'; '+link('mathlib-source-2.lean.txt','Dirichlet API')+'.\n\n'
s+='## Phase5.5 — statement shape\n\n'+table(['Check','Verdict','Reason'],ph['statement_shape3'])+'''
The finite-for-κ>2 formulation and exact classical recovery were compiled. Uniform IsDiophantine
is a project predicate with a complete bridge in LeanEval, not an existing mathlib replacement.
The full LeanEval module was re-elaborated in the caller test rather than assuming those two
predicates coincide. The α=0 native counterexample confirms why the old irrationality hypothesis
cannot simply be removed from the pair theorem. The p=1 rational LiouvilleWith guard prevents
inferring irrationality without its actual p>1 hypothesis.

## Phase6.0 — complete callers, inlining and duplications

One direct proof call: Roth.roth, Main577. No external-to-file direct proof calls; documentary
Main21 and declaration Main547 excluded. Canonical293 kernel-value audit independently finds
only Roth.roth, and no direct kernel-type consumer. Transitive users include roth_rat and the
LeanEval endpoint. Arbitrary simp closure is not inferred from source or direct kernel counts.

The exact original five-helper closure and full Roth.roth proof were replayed with the target
body inserted as a local integral_inline; original signature agreement holds. Full roth_rat and
all LeanEval declarations were then replayed through that caller. Additional kernel assertions
show all three endpoint replay values contain no direct reference to the original target.
Inlining preserves correctness; it does not make the hard proof an existing mathlib composition.

'''+table(['A','B','Same statement?','Same proof?','Action'],[
('Integral Roth','Roth.roth','Special case','No; algebraic reduction invokes integral result','Keep integral proof core; algebraic extension is downstream'),
('Integral Roth','Roth.roth_rat','Different domain/premise','No; num/den injection transports existing result','Retain representation corollary as needed'),
('Exponent bound','LeanEval IsDiophantine','Equivalent for irrational α','No; exponent-gap/minimum argument','Choose public API and bridge once'),
('Integral Roth','Generic order contradiction','No','Only final closure resembles it','Do not classify full named result as generic order wrapper')])+link('callers.json','Caller inventory')+'; '+link('tracked-source-search.json','Tracked search')+'; '+link('inline-search.json','Inline search')+'; '+link('callers2-executed.lean.txt','Actual full inline/downstream source')+'.\n\n'
s+='''## Phase6 — actual composition attempts

1. Degree-dependent Liouville bound cannot replace degree by2 for arbitrary integral equations.
2. LiouvilleWith.irrational/mono/affine invariance and frequently_lt_rpow_neg transport hypotheses;
   they do not provide exponent2 exclusion. The isolated negative exact?/aesop probes confirm
   those generic routes did not close the supplied Roth goal in this context.
3. The finite-set equivalence is generic order/set logic, but consumes the full exponent theorem.
   It is not a proof of that theorem. The modern equivalence also takes Roth content explicitly.
4. Imported project main_lemma and five private helpers do assemble the result, but these are
   project arithmetic theorems, not existing mathlib building blocks.

NOT-COMPOSABLE from current mathlib in≤3 existing calls. No simp-only closure is being sold as
new Roth content. The independently written bridge is not counted as an existing building block.

## Phase7 — upstream action

**YES-but-generalise-first**, MODERN-IDIOM. Add the actual algebraic-integer exponent2 exclusion
using the existing LiouvilleWith predicate. This fills the concrete theorem identified by that
module’s p>2 documentation, beyond its present elementary/affine API and beyond Liouville’s
degree-dependent bound. Keep the proven classical pair/finite formulations as recovery corollaries.
The modern theorem drops the explicit irrationality argument safely, handles the existential
constant and composes directly with LiouvilleWith.mono, rational affine invariance and
frequently_lt_rpow_neg. It preserves the named theorem’s full mathematical content.

Proposed new home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean`.
Proposed PR title: `feat(NumberTheory/DiophantineApproximation): prove Roth's theorem for algebraic integers`.
Stage after prerequisites; group the terminal arithmetic theorem with **already accepted YES**
Roth.main_lemma (progress snapshot checked), while shipping foundational accepted Hasse derivative/
Taylor/index API in prior PRs. Roth.exists_degrees and Roth.one_le_prod_pow_mul_abs_eval are also
accepted YES-but-generalise-first dependencies, not assumed already present in mathlib. No future
unassessed algebraic extension is described as already accepted.

Reviewer candidates based on actual relevant recent file history: Jovan Gerbscheid, whose
[2025-11-19 filter-negation API commit](https://github.com/leanprover-community/mathlib4/commit/66b2a6571bcd28f2ab6cd8e15f195d394fc175bd)
touches LiouvilleWith; Marcelo Lynch’s2026-08-11 cleanup also touches that exact file. These are
reviewer candidates, not claims of acceptance or subject-specialist endorsement.

Pre-PR checklist: `/generalise Roth.roth_of_isIntegral` against the exact modern signature above;
`/cleanup Roth/Main.lean Roth.roth_of_isIntegral` and prerequisite import/naming staging;
request reviewer feedback on the new DiophantineApproximation home and LiouvilleWith API.
Cost is not a verdict factor. Number-field/place extensions are separate mathematics, not an
excuse to downgrade or a claimed mechanically verified generalization.

'''+link('reviewer-specific-commits.json','Reviewer commit receipt')+'; '+link('progress-snapshot.json','Accepted grouping snapshot')+'.\n\n'
s+='''## Phase8 — verification and portability

Accepted exact original replay/type agreement/canonical293, full caller inlining, finite/recovery/
rational guard, unelided constant inventory, and isolated modern equivalence/recovery are archived
with complete root requests/raw receipts and elapsed milliseconds. Standard axioms only:
propext, Classical.choice, Quot.sound. Failed shape01 and modern01 attempts (including recovered
sorryAx diagnostics) are rejected evidence, preserved separately, never counted as verification.
Original pp.all body printer elides101777characters; initial aggregate constant printer elides462.
The exact complete written proof and separate306-info constant inventory remain available;
a full unelided kernel-body pretty-print is not claimed.

Stable mathlib-only18 and disk9 prefixes are checked against fixed portable SHA constants.
Root freshly authorized only LiouvilleWith as the19th isolated import after pinned-header read;
that exact prefix SHA is effedd80b74beb9109429be8d2df4cc70926d98f957a0867a7a2f9fc10dcd4cc.
No project import appears in isolated proofs. No limit raises or new axioms were used.

Portable validator checks current manifest hashes/bytes, links, exact canonical/private order293,
all17 pins, actual native receipt success/nonpartial format, approved prefixes, widths and source
bytes. Draft completion remainsfalse until actual scratch/integrated-layout/secret gates pass;
then final completion istrue. Root mathematical acceptance remainspending until independent review.

'''+link('verification.json','Verification ledger')+'; '+link('validate.py','Portable validator')+'; '+link('copy-manifest.json','Current manifest')+'.\n'
(D/'report.md').write_text('\n'.join(l.rstrip()for l in s.rstrip().splitlines())+'\n')
print('Report/overview/type/dependencies prepared; assessment not frozen')
