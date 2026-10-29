from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.exists_approximants'
def rd(n):return json.loads((D/n).read_text())
def link(n,label=None):return '['+(label or n)+'](../evidence/'+N+'/'+n+')'
a=rd('assessment.json');o=rd('overview-entry.json');p=rd('phase-checks.json');v=rd('verification.json');lit=rd('literature.json')
s='''# Roth.exists_approximants — canonical277

**Verdict: BORDERLINE-needs-human.** Keep the arithmetic packaging local while deciding whether
cofinal-height recursive selection deserves a public API. This is a completed mathematical
assessment once the final package gates pass; the three upstream design questions are not a user
blocker. No verdict is inherited from the reduced-approximation selector or another declaration.
Cost is not a verdict factor.

## Phase0 — baseline and provenance

The unchanged production statement resolves at Roth/Main.lean256. Kind: theorem; no sorry in
original source. Main proves Roth's theorem by reduction, parameter and approximant selection,
polynomial construction, and a logarithmic contradiction. The shared baseline succeeded with2467
jobs; all17 current production-source/pin hashes freshly match its tracked manifest. The accepted
Theta228 file-boundary build remains applicable; the next requested literal build is289.
No build was required at277. Root exclusively executed native/project-LSP operations; this worker
prepared immutable source/request archives and inspected the complete raw returned diagnostics.

'''+link('baseline-build.txt')+', '+link('inputs.json')+', '+link('fresh-final-inputs.json')+'''.
Original re-elaboration scope is exactly the target theorem, renamed `replay` in a fresh namespace
with public project ingredients imported. There is no private helper closure to copy. Native
proof-irrelevance equality verifies the exact original/replay type; it does not identify proof
construction. The293-name audit derives directly from tracked declaration order, preserving
private modules, and verifies exact order/uniqueness/presence/values. Native full type and axioms
were captured via `Lean.getConstInfo` and tagged `pp.funBinderTypes`. Both original and scope executions request the original `pp.all #print`; each
contains the same79277-character printer elision; a full kernel-body dump is not claimed.

'''+link('original-executed.lean.txt')+', '+link('original-receipt.json')+', '+link('native-type.json')+'''.

## Phase1 — mathematical content

From infinitely many fixed-constant approximating pairs for an irrational real number, select any
nonzero finite number of reduced pairs. Every denominator exceeds1, the first logarithm strictly
exceeds an arbitrary real L, and each adjacent logarithm strictly exceeds2/δ times its predecessor.
The actual δ parameter is arbitrary real. For δ≤0 the inequality does not assert an increasing
sequence: at δ=0 totalized division makes its left factor0. No hidden positivity assumption is
added.

The proof calls `Roth.exists_reduced_approx` for an unbounded-denominator selector, recursively
chooses above natural ceilings of exp(L) and powered previous denominators, and applies
`Real.lt_log_of_rpow_lt`. Coprimality and q>1 are carried at every recursive step.

Full native type:

```lean
'''+o['type']+'''
```

Parameters/hypotheses and every generality finding appear in Phase4. Written project dependencies
in tracked canonical order are exactly `Roth.approxSet`, `Roth.exists_reduced_approx`.
Generated kernel constants, lexical occurrences, direct type/value consumers, and transitive
consumers are distinct scopes.

## Phase2 — size and definition-only checks

SMALL: auxiliary selection theorem, neither a new structure nor a named main result.
One-line definition test: n/a, theorem. All six infrastructure risks are n/a for a theorem:
no instance diamond, reducibility leak, noncanonical data unfolding, priority registration,
universe-constrained data instance, or new coercion. Detailed reasons: '''+link('phase-checks.json')+'''.

## Phase3 — exhaustive literature

Every named channel was attempted, including the distinct /ncatlab namespace and a dated recent
arXiv query. General queries differ in specific, abstract, and alias formulations. Only exact
requests, response SHA/byte/status, titles/URLs/locators, and original concise summaries are
persisted; no third-party article or search-response bodies are archived.

| Channel | Actual query | Finding and source locator |
|---|---|---|
'''
for x in lit['channels']:
 title='['+x['title']+']('+x['url']+')'if x['url']else x['title']
 s+='| '+x['channel']+' | '+x['query']+' | '+x['summary']+' '+title+'; '+x['locator']+'. '+link(x['receipt'],'request/fingerprint')+' |\n'
s+='''| Local | reduced solutions / choose solutions / eq50 | clean.tex1572–1613, §7: unbounded reduced denominators and successive strict log ratios. '''+link('literature-local.json')+', '+link('local-excerpt.tex.txt')+''' |
| Optional ChatGPT math | n/a | ask_chatgpt_math unavailable; all other channels still executed. |

The author's [elementary Roth exposition](https://aleksa-milojevic.github.io/expository/roth.pdf)
explicitly chooses rapidly increasing denominators in §2 page3; it dates itself January2022.
The literature distinguishes this freedom to choose a sparse subsequence from the gap principle,
which constrains all sufficiently good approximants. The [Stacks proof0597](https://stacks.math.columbia.edu/tag/0597)
constructs a cofinal sequence inductively in a different setting; it is an analogy, not the same
arithmetic theorem. nLab direct opening failed on unsupported XHTML; the distinct /ncatlab query
returned only out-of-namespace hits. The refined dated arXiv Diophantine gap query returned empty;
the first dated query also returned additive-Roth and irrelevant approximation papers, retained
honestly as search noise. '''+link('primary.json')+', '+link('literature.json')+'''.

Standard mechanism: recursively select from a cofinal set, with arbitrary starting bound and
prescribed growth. The factor2/δ is downstream parameter bookkeeping. Reducedness and fixed1
approximation membership remain substantive arithmetic input; a generic recursion does not
prove them.

## Phase4a–4b — parameter-by-parameter generality

| Parameter/hypothesis | Finding |
|---|---|
'''
for x in p['full_generality']:s+='| '+x['parameter']+' | '+x['finding']+' |\n'
s+='''
**Verified weakening:** κ positivity is unnecessary for the complete original conclusion.
For κ>0 the finite-fiber reduction proof supplies unbounded reduced approximants. For κ≤0,
Dirichlet's existing exponent2 rational approximation theorem supplies infinitely many reduced
rationals; bounded-denominator finiteness and monotonicity in the exponent provide the needed
selector. More generally κ≤2 needs no supplied infinitude. These selector proofs are newly
written scratch mathematics, credited to prior274 as proof templates and independently rechecked
here. They are not existing mathlib theorems and are not inherited assessment evidence.

'''+link('signed-executed.lean.txt')+', '+link('signed01-receipt.json')+'''.
Full original positive-κ signature is recovered specifically through the unrestricted theorem;
δ=0 and δ=−1 full-output specializations also compile. '''+link('edges2-executed.lean.txt')+', '+link('edges02-receipt.json')+'''.

Irrationality is protected by a checked counterexample: α=0, κ=3 has infinitely many exact
unreduced pairs, yet no coprime approximating pair with q>1 and hence no m=1 output chain.
This is a full-family obstruction, not merely failure of one proposed witness.
'''+link('counterexample2-executed.lean.txt')+', '+link('counterexample02-receipt.json')+'''.

Generality status: strictly narrower in κ, and abstractable in witness/height/growth semantics.
The finite-chain proof tested for arbitrary real c and arbitrary objects A has a stronger
infinite-sequence version with arbitrary time-dependent threshold F. Empty-chain restatement
requires omitting the nonexistent first entry; its separate no-start form is compiled.
No weakening of the real analytic approximation theory to arbitrary fields is claimed.

## Phase4c — nine modern-idiom checks

| Question | Answer and downstream consequence |
|---|---|
'''
for a,b in p['modern9']:s+='| '+a+' | '+b+' |\n'
s+='''
Concrete-via-abstract diagnostic: α and κ enter only through the initial selector and the
membership assertion. The remaining recursion constructs height-separated witnesses.
'''+link('concrete-diagnostic.json')+'''. Genuine organizational improvement: isolate selection from
integer/rational representation, permit arbitrary real growth factors, and use unbounded-image
API. The exact recovery still proves cofinal logarithmic height using exp/ceiling and preserves
all original output fields. It does not replace the theorem by a hypothesis supplying its conclusion.

Verified generic signature (new scratch proof):

```lean
'''+o['generalization']['proposed_type']+'''
```

'''+link('generic-executed.lean.txt')+', '+link('generic01-receipt.json')+'''.
The full old statement follows from the generic finite chain with A=ℤ×ℕ,
s={admissible coprime pairs with q>1}, height=log denominator, and c=2/δ. Exact original/recovered
type equality also compiles in the real project context.
'''+link('recovery-executed.lean.txt')+', '+link('recovery01-receipt.json')+'''.

## Phase4.6 — five proof-strategy checks

| Question | Answer |
|---|---|
'''
for a,b in p['proofstrategy5']:s+='| '+a+' | '+b+' |\n'
s+='''
Strategy verdict: REFACTOR-RECOMMENDED if a general selection API is adopted; arithmetic
cofinality feeds generic recursive selection. Existing direct recursion is mathematically sound.
Neither cost nor brevity establishes the upstream verdict.

## Phase5 — fifteen actual formal-search cells

| Form | Lean-Finder | Loogle | LeanSearch | Source rg | Root local LSP |
|---|---|---|---|---|---|
'''
for f in ['current','standard','abstract']:
 s+='| '+f+' | '+' | '.join(link('formal-'+f+'-'+m+'.json',m)for m in ['leanfinder','loogle','leansearch','rg','local'])+' |\n'
s+='''
Current form finds Dirichlet and Liouville-family candidates, not the old output chain.
Standard form finds `Nat.exists_strictMono_subsequence` and
`Filter.extraction_forall_of_frequently`; abstract form finds
`Set.seq_of_forall_finite_exists` and cofinal constructions. All three local requests returned
`index:error` with1/2/3 hits respectively; this is degraded indexing, never absence evidence.
Remote indexes may differ from the pin. The finite-history, strict-monotone, frequent-extraction, unbounded-image and log
candidate signatures were checked natively; cofinal bundles and LiouvilleWith were inspected in
pinned source. Current pinned modules are archived with hashes. '''+link('formal-search-matrix.json')+', '+link('mathlib-inputs.json')+'''.

`Set.seq_of_forall_finite_exists` relates the next element to its finite predecessor image;
applying it here requires proving a finite upper-bound selection premise and transporting its
outputs. Strictly increasing natural subsequences alone do not provide arbitrary adaptive
real-logarithmic growth. `Order.sequenceOfCofinals` supplies monotonicity and membership in fixed
countably indexed cofinal sets; the pinned source does not supply this exact recursive gap law.

The pinned `LiouvilleWith p x` has an existential approximation constantC, frequent natural
denominators, and excludes exact equality. Its `exists_pos` adds positive C and positive
denominators, `mono` weakens exponent, and `frequently_lt_rpow_neg` absorbs C only with a strict
exponent loss. It is not the fixed1 `approxSet α κ`, nor a reduced-pair set, nor the
uniform-for-every-ε lower-bound `IsDiophantine` API. For p≤1 it can hold for rational x. Its
pinned source is inspected, not claimed as a native exact equivalence or ≤3-call replacement.

## Phase5.5 — three statement-shape checks

| Check | Finding |
|---|---|
'''
for a,b in p['statement_shape3']:s+='| '+a+' | '+b+' |\n'
s+='''
Normal form: OK for the local arithmetic caller; upstream recursive selection would use
cofinal-height semantics. Syntactic generality: RESTATE for public generic API. Superfluous
arguments: hκ positivity verified removable; hinf removable only in verified κ≤2 branch.
No reversed simp-normal-form equivalence or new global instances are proposed.

## Phase6.0 — complete callers, inline audit, dependency scopes

Fresh scoped `rg --no-ignore` and tracked `git grep` agree: one actual source caller,
`Roth.exists_roth_approximants_aux` at Main438, inside its full declaration Main429–450.
There are zero external-to-file source callers. Main's docstring occurrence is not a caller.
The entire Main file and LeanEval wrapper were read. No separate inline rederivation was found.
'''+link('source-search.json')+', '+link('tracked-source-search.json')+', '+link('inline-search.json')+', '+link('callers.json')+'''.

Both tests retain the actual caller's complete original signature and body: first literal
selection proof inlined at the actual application, then substitution by the generic recovered
theorem. They return all balanced degrees and subsequent bound obligations, not merely an
isolated prefix or a supplied desired conclusion. Only declaration visibility/name change.
'''+link('callers2-executed.lean.txt')+', '+link('callers02-receipt.json')+'''.

Native293 audit finds zero direct type consumers, one direct kernel-value consumer, and five
canonical transitive consumers: the private approximant/degree helper, roth_of_isIntegral,
roth, roth_rat, and LeanEval.thueSiegelRoth. This theorem has no simp attribute; lexical,
body/type, and canonical graph scopes are separately recorded.
'''+link('scope-executed.lean.txt')+', '+link('scope01-receipt.json')+', '+link('canonical-consumers.json')+'''.

Pairwise moral-duplication audit:

| A | B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| exists_approximants | exists_reduced_approx | No: unbounded one-witness selector versus finite recursive chain | Selector is initial arithmetic input | Keep scopes separate; do not count parent as mathlib |
| exists_approximants | exists_degrees | No: rational selection versus degree rounding/balancing | No | No unification |
| exists_approximants | Set.seq_of_forall_finite_exists | No: exact arithmetic/log outputs versus finite-history predicate | Shared choice/recursion mechanism | Investigate public generic selection API |

## Phase6 — actual composition experiments

Attempt1: strict-monotone subsequence/extraction primitives. Native signatures confirm their
shapes, but arbitrary recursive growth and reduced fixed-constant approximation membership are
missing; no1–3-call old-form proof was obtained.

Attempt2: finite-history sequence selection plus finite bounds. This is a possible proof
strategy, but the finite-bound premise and logarithmic/reduced-pair bridge require new proof;
it is not a1–3-call replacement. The new generic recursion proves the exact desired growth.

The accepted native probe places `fail_if_success solve | simp` and
`fail_if_success solve | exact?` inside the first own generic declaration, before any own
selection theorem is available. Neither closes. This is evidence about those routes, not an
absolute absence theorem. The cofinal-image normal-form equivalence does close by simp; that
small equivalence is not the full chain theorem. No ≤3-call mathlib-only old-signature
composition, and no full simp composition, has been demonstrated.
'''+link('composition2-executed.lean.txt')+', '+link('composition02-receipt.json')+'''.

## Phase7 — actionable verdict

**BORDERLINE-needs-human.** A useful local witness-construction theorem is established, but
whether its generic recursion packaging should become public API remains an audience/granularity
choice. The exact2/δ logarithmic formulation serves one Roth caller. A reusable cofinal-height
sequence exposes more mathematics and composes with unbounded-image predicates, but the
selection mechanism overlaps existing finite-history sequence primitives. This does not justify
calling the old theorem redundant, nor establish that its exact arithmetic spelling should ship.

Keep the current project theorem. A concrete local improvement is dropping κ positivity using
the verified signed selector, and supplying only the reduced cofinal-height premise to the
finite-chain theorem. The only actual caller can retain every output obligation with the tested
generic replacement. If public selection API is pursued, decide these future upstream questions:

'''
for i,q in enumerate(rd('assessment.json')['questions'],1):s+=str(i)+'. '+q+'\n'
s+='''
These are future upstream decisions, not missing mathematical proof or user blockers. No
production theorem, pin, Git state, overview, or progress entry was changed by this worker.

## Phase8 — native attempt ledger and final gates

| Accepted exact source | Raw root receipt | Elapsed ms |
|---|---|---|
'''
for e in v['accepted']:s+='| '+link(e['source'],e['label'])+' | '+link(e['receipt'])+' | '+str(e['elapsed_ms'])+' |\n'
s+='''
All accepted proofs have clean complete diagnostics and only propext/Classical.choice/Quot.sound.
Disk results explicitly report partial=false; raw run_code format reports success/diagnostics
without a partial field. Nine accepted native executions; three other native executions are
separately retained: callers01 errors/recovered sorryAx rejected; counterexample01 clean but
missing target-isolation guard, superseded by guarded02; edges01 clean proof with two whitespace
warnings, superseded by warning-free02. Composition01 was never executed: the circular own-theorem
negative-probe mistake was caught in preparation and corrected in02. Exact executed sources and
hashes are immutable. No raised limits, new axioms, sorry/admit/unsafe/native_decide accepted.

Stable18 isolated prefix and disk9 prefix remain unchanged. Signed and edge probes alone use the
fresh root-approved19th import, DiophantineApproximation.Basic. '''+link('native-prefix-authorization.json')+'''.
Portable validator checks current manifest hashes/bytes,17 fresh source/pin hashes, exact293 array,
all native receipts and imported prefixes, standard axioms, literal replay/complete caller
scope,15 formal cells, named literature requests, required overview keys and report links in
both scratch and integrated layouts. '''+link('verification.json')+', '+link('validate.py')+'''.
'''
(D/'report.md').write_text(s)
print('Report written with full phase tables, exact native ledger, and future upstream questions')
