from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.exists_m'
def rd(n):return json.loads((D/n).read_text())
def link(n,label=None):return f'[{label or n}](../evidence/{N}/{n})'
p=rd('phase-checks.json');v=rd('verification.json');lit=rd('literature.json');gen=rd('generality.json')
s='''# Roth.exists_m — full assessment

**BORDERLINE-needs-human.** The numerical existence theorem is valid and useful in Roth's proof. A stronger theorem with arbitrary real size coefficient and numerator coefficient has been proved from mathlib in isolation, with exact old recovery and the complete actual caller checked. The remaining question is whether this precise combination deserves public upstream API. This is a completed assessment, not a user blocker; no production change is proposed here.

## 0. Baseline and scope

Canonical275, public theorem at `Roth/Main.lean:196–218`. All of Main (588 lines) and LeanEval (66 lines), including the full actual caller, were read. The original replay scope is exactly the target, renamed `Dimension275Original.replay` in a fresh namespace; no helper closure is needed. Existing public project imports remain available. The equality check with `Subsingleton.elim` certifies exact original/replay proposition agreement, not proof-construction identity.

The reusable baseline completed2467jobs cleanly. All17source/pin hashes were freshly matched against the tracked shared manifest and checked again before freeze. No file-boundary build is due at275; the next is289. Root exclusively executed every native and local-LSP request; the worker prepared sources, inspected returned evidence, and ran portable checks. No production/pin/Git/overview/progress change or native limit raise was made.

Evidence: '''+ ', '.join(link(x)for x in ['baseline-build.txt','inputs.json','input-manifest.json','source-Main.lean.txt','source-LeanEval.lean.txt','original-executed.lean.txt','original-receipt.json'])+'''.

## 1. Statement and proof

For every natural n, including0, and every real κ>2, there exists a natural m strictly exceeding16n². It simultaneously satisfies4n√m<m and2m/(m−4n√m)<κ. Thus m is positive and the quotient denominator is positive. The theorem makes no assumption that n is a polynomial degree or n≥2.

Full loaded kernel type (captured with Lean.getConstInfo and pp.funBinderTypes, not by splitting a printer output at an internal let):

```lean
'''+rd('native-type.json')['type']+'''
```

The original chooses s=ceil_nat(4κn/(κ−2))+4n+1 and m=s². The additive slack gives s>4n and s>0; ceiling control gives4κn<s(κ−2). Multiplication by s then proves all three bounds after √(s²)=s and positive-denominator division. The source proof has no project-declaration dependency. Kernel lists include generated `Roth.exists_m._proof_*` constants, which are internal proof fragments, not separate canonical project declarations.

The full written source and full kernel type, constant lists, value availability and standard axioms were inspected. The `pp.all` body explicitly elides80194characters; it is **not** a full kernel-body dump. Both the loaded original and focused replay depend only on propext, Classical.choice and Quot.sound.

## 2. Preliminary checks

SMALL: a numerical parameter-selection helper, not a new mathematical structure, named theorem, or main result listed in the module's main-results list. The one-line definition test is n/a because this is a theorem. Proof length does not determine the contribution verdict.

## 3. Exhaustive literature

All named channels were actually attempted. Optional ask_chatgpt_math is unavailable. Search receipts preserve exact requests, returned-response SHA256/byte count/status, clean titles/URLs and concise original summaries; no full third-party article/search body is stored. Some batched results are out of the requested namespace; this is recorded rather than treated as absence.

| Channel | Actual query / locator | Finding |
|---|---|---|
'''
for x in lit['general_queries']:s+=f"| General web | `{x['q']}` | Roth proof/background and Archimedean bound selection; no named combined selector. {link('web1-receipt.json')} |\n"
for x in lit['channels']:s+=f"| {x['channel']} | {link(x['receipt']) if 'receipt'in x else x['status']} | {x.get('summary',x.get('reason'))} |\n"
s+='''
The closest exact source is the local reference, §7 eq(47), lines1588–1594: choose a positive integer m with m>4n√m and quotient<κ, using κ>2. The formal theorem additionally exposes16n²<m. This is a standard step in the proof of Roth, not an independently named theorem found by the search. The publisher page confirms Roth's1955 article (June1955, pp1–20; online2010 is distinct), but the visible extract does not display internal eq(47). The IMU1958 search extract discusses many variables; root's direct PDF open failed400 for74705952bytes, so no claim of a full read is made. Root independently checked the actual local formula and publisher metadata.

Sources: [Roth1955 publisher page](https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F), [IMU1958 outline](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf), [nLab Archimedean property](https://ncatlab.org/nlab/show/Archimedean%2Bproperty). Recent-arXiv query used after:2021-10-29 before:2026-10-30; [Hindes2209.09182](https://arxiv.org/abs/2209.09182) treats characteristic p and different approximation methods, not this scalar selection lemma. Additive Roth search hits are unrelated.

Evidence: '''+', '.join(link(x)for x in ['literature.json','literature-source.json','literature-local.json','root-primary-crosscheck.json','web4-receipt.json','web6-receipt.json'])+'''.

## 4. Generality

| Parameter | Current | Verified analysis |
|---|---|---|
| n | arbitrary ℕ | No n>0 required. Replace4n by arbitrary real a, even signed, and16n² by a². |
| κ | real | Retain reals for Real.sqrt; full arbitrary-field sqrt transport is not claimed. |
| hκ | 2<κ | Cannot weaken uniformly to2≤κ: n=0,κ=2 admits no witness, compiled counterexample. |
| coefficient4 | fixed multiplier of n | Independent real c and real size t are allowed via a=c*t; positive c/nonnegative t included. |
| numerator2 | fixed | Arbitrary signed b with sufficient b<κ works; not asserted necessary for every fixed signed a,b. |
| m | natural witness | Kept natural to supply finite variable counts; replacing it by a real would not recover the project interface. |

First a≥0 was verified. The stronger signed variant chooses natural s>max(|a|,κa/(κ−b)) and m=s². Since s>|a| and s>0, a²<m and a√m<m. The cross-multiplied quotient follows from κa<s(κ−b). All arithmetic positivity obligations are proved, and n=0 is tested explicitly. No argument supplies the desired conclusion as a premise.

Verified stronger signature:

```lean
'''+gen['proposed_type']+'''
```

This is **our new generic proof**, not a theorem already in mathlib. Exact old recovery specializes a=4n,b=2 and transports the first inequality back to ℕ using arithmetic and exact_mod_cast. The full original caller also compiles using this recovery with its original signature intact. A meaningful scalar parameter has replaced project constants; nevertheless, searches did not establish that this exact conjunction is the customary standalone upstream API. Generality is mathematically established; upstream interface choice remains a Phase7 question. Cost is not part of the verdict.

A full Tendsto-to-b alternative was considered and searched. Pinned Real.tendsto_sqrt_atTop and tendsto_bdd_div_atTop_nhds_zero are verified building blocks. No full normalized quotient limit, eventual denominator bound, or simultaneous eventual witness theorem has been claimed or counted as an existing replacement. The explicit generic proof already certifies the required quantitative existence.

Evidence: '''+', '.join(link(x)for x in ['generic-executed.lean.txt','generic-receipt.json','signed-executed.lean.txt','signed-receipt.json','generality.json','replacement-caller-executed.lean.txt','replacement-caller-receipt.json'])+'''.

### Modern idiom — all nine rows

| # | Question | Verdict | Concrete analysis |
|---|---|---|---|
'''
for x in p['modern9']:s+=f"| {x['row']} | {x['question']} | {x['verdict']} | {x['reason']} |\n"
s+='''
The signed-size version lets unrelated real error coefficients and arbitrary leading ratio coefficients use the same proof without manufacturing natural dimensions in advance. No categorical, finite-dimensional-algebra or abstract-square-root theorem is substituted for the scalar statement. The natural witness remains compatible with the actual finite-variable caller.

### 4.5. Infrastructure risk

All six rows are n/a for a theorem: typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism data, and coercion ambiguity. No definition/instance/coercion is introduced. The explicit six-row record is in '''+link('phase-checks.json')+'''.

### 4.6. Proof strategy — all five rows

| # | Question | Verdict | Analysis |
|---|---|---|---|
'''
for x in p['proofstrategy5']:s+=f"| {x['row']} | {x['question']} | {x['verdict']} | {x['reason']} |\n"
s+='''
MATHLIB-IDIOMATIC: direct Archimedean square witness avoids proving only a limiting slogan. A proposed upstream generic API would be the scratch theorem itself, not a pre-existing helper silently assumed available.

## 5. Five methods × three forms

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
'''
for f in ['current','standard','abstract']:
 s+='| '+f+' | '+' | '.join(link(f'formal-{f}-{m}'+('-retry'if m=='loogle'else'')+'.json',m)for m in ['finder','loogle','search','rg','local'])+' |\n'
s+='''
Current-form semantic hits concerned additive Roth numbers, integer square roots and unrelated bounds; they do not prove the statement. Standard-form queries found square-root/filter growth building blocks. Abstract queries found the existing exists_nat_gt and Archimedean API. Positive candidate signatures were pinned natively and source files archived with hashes. External indexes can describe different revisions: the pin locates exists_nat_gt at Algebra/Order/Archimedean/Defs.lean:76 and Real.sqrt_sq at Analysis/Real/Sqrt.lean:181.

All three local requests returned `index=error`, despite positive candidate lists. These do not provide negative presence evidence. Initial Loogle attempts were rate-limited; successful later retries are separate receipts. An initial remote batch could not serialize its receipts; all nine queries were repeated with complete subsequent raw archives. The untruncated current-name rg returned exit1; it is not by itself an absence proof. Compiled `fail_if_success exact?` on the full current goal and full signed-generic goal also did not close. These checks support “no replacement identified”, not a logical theorem of library absence.

Evidence: '''+', '.join(link(x)for x in ['formal-search-matrix.json','mathlib-inputs.json','shape-receipt.json','composition2-receipt.json'])+'''.

## 5.5. Statement shape

| Check | Verdict | Analysis |
|---|---|---|
'''
for x in p['statement_shape3']:s+=f"| {x['question']} | {x['verdict']} | {x['reason']} |\n"
s+='''
The existential conjunction is directly convenient for the caller. The middle inequality follows from16n²<m, verified independently with Real.lt_sqrt and multiplication by positive√m. Thus an upstream minimal interface could separate this bridge, while exact original recovery must retain all three requirements. The alternative abstract simultaneous-bound lemma is checked over an Archimedean ordered semiring; it does not pretend Real.sqrt generalizes through that hierarchy. RHS normalization conventions are not relevant to an existential theorem with no equivalence rewrite.

Evidence: '''+link('shape-executed.lean.txt')+', '+link('shape-receipt.json')+'''.

## 6.0. Complete callers and inlining

| Caller | Site / calls | Full original use | Experiments |
|---|---|---|---|
| Roth.exists_roth_parameters_aux (private) | Main:419 /1 | n=f.natDegree; consumes hm and quotient bound in exists_delta, discards middle bound, uses degree≥2 to derive m≥2 | Full original caller signature/body checked with literal target proof in local helper, and separately with signed-generic recovery. |

Fresh `rg --no-ignore` and `git grep` across all tracked production modules agree: one explicit proof caller, no cross-file explicit caller. Two documentation mentions occur at29 and220; target declaration at196 is not a caller. Native exact293 audit finds that same one direct kernel-value consumer and zero direct type consumers. Five canonical type/value transitive consumers are the private parameter selector, Roth.roth_of_isIntegral, Roth.roth, Roth.roth_rat, and LeanEval.NumberTheory.ThueSiegelRothProblem.thueSiegelRoth. Target's canonical dependency closure is only itself. This is an explicit canonical-project graph, not a traversal of every imported mathlib/generated constant. No simp attribute exists on the target; lexical references and opaque kernel/transitive dependencies are distinct scopes.

Every actual affected direct caller is fully checked. All transitive consumers' full modules were read; they do not contain another target call to inline. Raw canonical names preserve correct private modules and exact293order, generated directly from tracked declaration-order; Python preflight and native requested/unique/present/value counts all pass.

Evidence: '''+', '.join(link(x)for x in ['source-search.json','git-source-search.json','inline-search.json','callers.json','caller-excerpt.lean.txt','callers-executed.lean.txt','callers-receipt.json','canonical-consumers.json','consumer-scope2-executed.lean.txt','consumers2-receipt.json'])+'''.

## 6. Composition

NOT-COMPOSABLE by the identified existing API in≤3calls. exists_nat_gt or Nat.le_ceil selects a large scalar; it does not establish all square, sqrt and quotient bounds. Real.sqrt_sq and division order lemmas normalize once a suitable witness and positivity inequalities have been supplied. The actual original proof and new generic proof both contain substantive arithmetic bridging. The full current goal resisted exact?, simp and aesop in an accepted isolated test before the original proof closed it. This is evidence about those concrete routes, not an exhaustive impossibility theorem. The new generic theorem makes recovery short only after a new proof; it cannot count as an existing mathlib building block.

The literal full proof can be inlined at the one caller and passes, but that is a refactoring experiment, not a≤3-call composition. No NO-composable/delete recommendation follows merely from having one caller.

## 7. Verdict, overview findings and next action

**BORDERLINE-needs-human**, independently assessed; no parent verdict is inherited. The statement is a genuine useful numerical lemma, with a stronger verified form and no exact existing match identified. It is also an ad hoc conjunction associated with one stage of Roth's proof; the literature does not establish a named general public interface, and no second independent consumer was identified. The upstream API/publicness question remains after the proof work, not because generalization would cost time.

'''
for i,q in enumerate(rd('assessment.json')['questions']):s+=f'{i+1}. {q}\n'
s+='''
These are future upstream design questions, not unresolved verification or a request blocking the project overview. Keep the current theorem in Roth/Main.lean pending that decision. If proposed upstream, use the signed generic result and decide whether to split the redundant middle inequality; tentative homes are a real square-root inequality module or a dedicated Roth proof module. No YES PR title/reviewer/grouping claim is made for this BORDERLINE package.

Moral duplication: exists_delta/exists_delta_bound choose real small parameters near0, while this theorem chooses a natural dimension at infinity; their conclusions and interfaces differ. No duplicate or junk classification follows from their common parameter-choice role. Missing API is at most a reusable generic quantitative selector, whose scratch proof is now available. The existing theorem is used, substantive, and safe to retain. There are no project proof dependencies to replace.

## 8. Verification and evidence

'''
for x in v['accepted']:s+=f"- Accepted {x['label']}: {link(x['source'])}, {link(x['receipt'])}; root elapsed{x['elapsed_ms']}ms.\n"
s+='''
Eight accepted native executions are clean, complete, and use standard axioms only. Two earlier executions are preserved and rejected: composition01 had erroneous indentation and recovered sorryAx; consumers01 used unavailable Array.union. Corrected immutable attempts passed. Rejected output is never counted as proof. All exact requests, executed sources, receipt hashes, full raw native/formal results, input hashes, current recursive manifest and read-only portable validator are included. Printer body elision and local index-error limitations are explicit. The checker validates both scratch and integrated layouts, every current-manifest artifact, canonical dependency membership/normalization, exact293array order/private modules, accepted-source identity, roots/prefixes, links, and final inputs.

Evidence: '''+', '.join(link(x)for x in ['assessment.json','overview-entry.json','verification.json','preparation-notes.json','composition-receipt.json','consumers-receipt.json','validate.py','copy-manifest.json','validation-scratch.json','validation-integrated.json','secret-scan.json'])+'''.
'''
(D/'report.md').write_text(s)
print('report written',len(s.splitlines()),'lines')
