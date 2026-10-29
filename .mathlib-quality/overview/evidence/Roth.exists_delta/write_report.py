from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.exists_delta';r=lambda n:json.loads((D/n).read_text());L=lambda n:'../evidence/'+N+'/'+n
p=r('phase-checks.json');typ=r('native-type.json')['type'];lit=r('literature.json');a=r('assessment.json')
s='''# Roth.exists_delta — canonical276

Verdict: **BORDERLINE-needs-human**. Keep this parameter choice project-local while the upstream public API granularity is decided. The mathematical and mechanical assessment is complete when the portable gates below pass; the three future questions are not a request to pause this overview. This verdict is independent of exists_delta_bound/exists_m and is not based on proof cost.

## Phase0: baseline and scope

The clean2467-job baseline is reusable: fresh checks match all17 tracked production-source/pin hashes. No production Lean/pin/Git/overview/progress changes were made. No new full literal build is due at276; next required file boundary is289. Root exclusively executed every native check and all local searches through its persistent session. Sources and raw request/results retain exact code, hashes and elapsed times.

The target is the public theorem at Main227. The declaring file and the sole actual caller were read in full, together with Main's full continuation and the LeanEval terminal module. Original proof re-elaboration is deliberately **target-only**, in a fresh namespace, with no private-helper closure needed: public project ingredients remain imported. A native theorem equality checks exact original/replay proposition type; proof irrelevance does not assert identical proof construction.

## Phase1: statement and proof

For natural degree n and fixed dimension m>16n², suppose the limiting quotient 2m/(m−4n√m) is strictly below real κ. There is a positive δ below1/m such that both η(δ,m)+2(1+3δ)n√m<m/2 and m(1+4δ)/(γ(δ,n,m)−η(δ,m))<κ. Here η=10^m δ^((1/2)^m), γ=(m−4(1+3δ)n√m)/2. **n may be zero**; **κ>2 is not an input binder**.

Full native type:

```lean
'''+typ+'''
```

The proof first uses exists_delta_bound for the cap and first strict envelope on an interval that includes0. That interval's estimate at0 gives a positive gamma-minus-eta denominator. Continuity of the real-power quotient at0 preserves the second strict inequality; a positive point below the original interval and a metric continuity radius meets both bounds. This is a small-perturbation argument with a genuine limiting gap, not just an arbitrary witness choice.

## Phase2 and4.5: preliminary/risk checks

SMALL: a parameter-selection helper, not a main named result or new structure. One-line definition check is n/a because this is a theorem. Each of the six infrastructure risks (diamond, reducibility, unfolding, priority, universes, coercion) is n/a: the declaration introduces a proof, no instance or data representation. All six are recorded separately in the phase evidence.

## Phase3: exhaustive literature

'''
s+='| Channel | Actual query / outcome |\n|---|---|\n'
for x in lit['channels']:
 q=x['request']['search_query'][0]['q'];s+='| '+x['channel']+' | `'+q+'` — '+x['summary']+' |\n'
s+='| local | clean.tex, §6 lemma m-delta and §7 equations47–49; full exact query receipt and bounded source excerpt retained. |\n| ask_chatgpt_math | n/a: tool unavailable; no reduction of other channels. Historical comparison uses primary2003 notes. |\n'
s+='''
The specific-form, general-form and alias queries are three actual distinct requests. nCatLab was queried distinctly with site:ncatlab.org/ncatlab; search returned nLab pages, not a claimed nCatLab exact match. Direct nLab fetch failed for unsupported XHTML; that limitation is retained. Recent arXiv used after:2021-10-29 before:2026-10-30, with irrelevant or old returned results excluded as mathematical evidence. No failed or empty search is a proof of absence.

The primary [Princeton seminar notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), §17.3 pp.151–152 equations17.17–17.20, choose m and then successively decrease δ to preserve a positive denominator and the strict quotient inequality. Their text after17.19 prints k<2 despite the section beginning k>2; this is a typo, and the native theorem uses the explicit strict h47 input. The local modern source has the corrected positive exponent and retains the simultaneous envelopes. [NIST DLMF §1.4(ii)](https://dlmf.nist.gov/1.4) supplies the classical continuity vocabulary; the abstract standard form is persistence of strict inequalities in neighborhoods, with finite intersections. No standalone traditional theorem name for this entire Roth-specific parameter package was established.

Only exact requests, returned-response SHA256/bytes/status, selected clean titles/URLs/locators and original summaries are persisted for web evidence. No article/search body is archived; truncated URLs were omitted. Search-only sources are background, not a substitute for primary mathematical evidence.

## Phases4a–4b: parameter/generality analysis

| Parameter/hypothesis | Concrete assessment |
|---|---|
| n:ℕ | Zero is allowed; native recovery explicitly verifies n=0,m=1. No n>0 premise may be introduced. |
| m:ℕ | hm implies m>0; this is needed for1/m to be a positive cap. Real division by0 is0, so deleting hm admits an impossible positive δ<0 at m=0. |
| hm:16n²<m | Supplies4n<√m, hence strict positive limiting gamma-minus-eta gap. The proof does not merely use m≠0. |
| κ:ℝ | Arbitrary real bound at the interface. No separate κ>2 binder; h47 supplies all needed limiting slack. |
| h47 | Essential strict quotient slack. A native no-zero-upper-bound test proves that positive numerator/positive gap cannot meet a zero strict threshold. This is a counterexample to naive deletion, not a claimed classification of every possible weakening. |
| Fixed constants and named functions | Generic quantitative cap/envelope selection is compiled; actual arithmetic recovery proves continuity, zero values and square-root gap, without calling the target. The concrete arithmetic spelling alone is not evidence for a NO verdict. |

There is no verified removable **original** hypothesis. Modern abstraction is available as a different reusable interface; it is not a mechanical removal of n,m or κ. Strictly positive exponent makes η(0)=0; the native zero-rpow and division conventions are checked before weakening assumptions. Adding all-real generic envelopes is a new proof rather than an existing-mathlib replacement.

## Phase4c: modern idiom, all nine rows

| Question | Answer / downstream consequence |
|---|---|
'''
for q,v in p['modern9']:s+='| '+q+' | '+v+' |\n'
s+='''
The mathlib-only generic theorem takes continuous real f,p,q, a positive cap U, bounds f(0)<B and p(0)/q(0)<K, and q(0)≠0. It returns δ>0,δ<U,f(δ)<B,p(δ)/q(δ)<K simultaneously. Its implementation composes eventual inequalities and exists_gt; a separate example verifies that **point selection alone already exists**. The old-recovery proof uses f=η+2(1+3δ)n√m, p=m(1+4δ), q=γ−η. It rebuilds each analytic/quantitative premise, so the abstraction has not discarded the actual Roth content. This replaces explicit metric-radius bookkeeping with filter composition and enables other continuous perturbations to reuse the selection step.

## Phase4.6: proof strategy, all five rows

| Question | Assessment |
|---|---|
'''
for q,v in p['proofstrategy5']:s+='| '+q+' | '+v+' |\n'
s+='''
REFACTOR-RECOMMENDED: use existing filter tools for the selection stage. Whether to expose a named simultaneous helper is a public API question; no cost-based downgrade is made.

## Phase5: all15 formal search cells

| Form | Finder | Loogle | LeanSearch | source rg | local search |
|---|---|---|---|---|---|
'''
for f in ['current','standard','abstract']:
 s+='| '+f+' | '+' | '.join('['+m+']('+L('formal-'+f+'-'+m+'.json')+')'for m in ['leanfinder','loogle','leansearch','rg','local'])+' |\n'
s+='''
Current-form searches are polluted by the unrelated additive-combinatorics Roth theorem; those are rejected as matches. Standard and abstract forms identify ContinuousAt.eventually_lt, Filter.Eventually.and/exists_gt/exists and ContinuousAt.div. Positive candidate signatures are natively checked. All three local calls returned index:error; neither their hits nor empty lists certify complete local index coverage. Remote indices can differ from the pinned mathlib; pinned source excerpts and native compilation verify the candidates actually used.

The strongest confirmed hits cover component steps, not the full eta/gamma envelope theorem in a one-line specialization. The exact isolated code is guarded by #check_failure Roth.exists_delta, and imports no project module. New generic proofs are labelled as new proofs, never cited as pre-existing building blocks.

## Phase5.5: statement shape

| Check | Assessment |
|---|---|
'''
for q,v in p['statement_shape3']:s+='| '+q+' | '+v+' |\n'
s+='''
The expanded denominator form is the literature's2m(1+4δ)/(m−4(1+3δ)n√m−2η). The native shape proof validates it, while the project gamma-minus-eta form aligns with downstream eta_lt_gam_iff. There is no proposed new simp-normal-form cycle or unnecessary instance constraint.

## Phases6.0–6: callers, dependencies, composition

Lexical enumeration was cross-checked with git grep over tracked production sources. There is one actual source call, Main420 inside private exists_roth_parameters_aux; the module docstring and declaration line are not callers. Canonical293 loaded-kernel audit finds the same one direct value consumer and no direct type consumer. Five canonical transitive consumers are that helper, roth_of_isIntegral, roth, roth_rat and LeanEval's thueSiegelRoth. These are canonical graph edges from native type/value constants, distinct from lexical use and unrestricted generated-constant closure. Target has no simp attribute and no later source attribute registration was found.

Canonical written proof dependencies, in tracked declaration order: Roth.lam, Roth.gam, Roth.eta, Roth.exists_delta_bound, Roth.eta_lt_gam_iff. The overview contains only these public/canonical names. Generated kernel constants such as lam._proof_1 are preserved in native raw evidence, not promoted into the overview dependency list.

The complete actual private caller was re-elaborated with a local exact-signature helper containing the target's literal proof. This retains all original hypotheses and polynomial/coefficient/dimension conclusions. The replacement experiment separately replays the **entire Main410–588 continuation**, including every required private helper with private visibility removed in the scratch namespace, then roth_of_isIntegral/roth/roth_rat, replacing the actual target call with the recovered generic theorem. It retains original signatures. The LeanEval module was read and its transitive edge audited; **no new LeanEval terminal replay is claimed**.

Composition tests are scoped honestly. The isolated generic selection is several existing calls (three eventual inequalities, two conjunctions, quotient continuity and exists_gt); the complete old-form recovery additionally needs the arithmetic square-root gap, rpow continuity and zero-value normalization. This is not a verified≤3-existing-call replacement. Independent native `solve | simp` and `solve | aesop` do not close the full original goal; the literal proof then closes it. These bounded failures do not prove library absence. Inline success proves feasibility, not redundancy. No separate source-level inline derivation bypassing the theorem was found.

## Phase7: verdict and future upstream questions

BORDERLINE-needs-human, with these concrete future API questions:

'''
for i,q in enumerate(a['questions'],1):s+=str(i)+'. '+q+'\n'
s+='''
Keeping the current project-local theorem is a concrete next action. It is used and not established junk. Its full arithmetic content is too narrow to recommend as-is solely from Roth's theorem being important; its reusable selection pattern already has a rich filter API, but the whole original result is not verified as a tiny existing-call composition. No public mathlib PR/home/reviewer/grouping is proposed under this BORDERLINE verdict; those YES-only artifacts are n/a rather than invented.

## Phase8: native/evidence gates and limitations

Accepted root-executed proofs use only propext, Classical.choice and Quot.sound, with default resource limits, no sorry/new axioms/unsafe/native_decide. Full raw receipts and exact executed sources include failed attempts separately. Original and scope kernel printers each elide a large body segment; **neither is a full kernel-body dump**. Complete written proof, full native type/standard axioms and the ordered293/unique293/present293/value293 kernel audit remain available.

Rejected attempts remain raw: recovery01/callers01 left the zero-dimension contradiction unfinished; composition01 used fail_if_success on a progress-only simp; shape01 elaborated but produced an unnecessary-sequence-focus warning. Subsequent immutable02 sources fix each issue. The initial inline width guard occurred before a native call and is documented separately; no earlier executed source was overwritten.

Evidence: [verification]('''+L('verification.json')+'''), [phase checklist]('''+L('phase-checks.json')+'''), [literature requests/summaries]('''+L('literature.json')+'''), [canonical consumers]('''+L('canonical-consumers.json')+'''), [portable validator]('''+L('validate.py')+'''), [current manifest]('''+L('copy-manifest.json')+'''). Validation supports scratch and integrated layouts, checks current manifest hashes/bytes, exact293 order/private names, normalized written dependencies, fresh17 hashes, native outcomes/axioms/requests and all report links. Root acceptance remains pending independent review.
'''
(D/'report.md').write_text(s);print('Draft report generated',len(s.split()),'words')
