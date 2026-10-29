from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.pigeonhole_count'
def rd(n):return json.loads((D/n).read_text())
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n' if not isinstance(x,str) else x)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
typ=rd('native-type.json')['type'];link=lambda f:'../evidence/'+N+'/'+f
questions=['Should Mathlib.Analysis.SpecialFunctions.Pow.Real expose the verified arbitrary strict-base/exponent-budget lifting theorem, including its zero-exponent branch, rather than leave this composition to callers?', 'Should the independent scalar floor-count bound be public analysis API, or remain a private ingredient of the Diophantine construction?', 'If the scalar bound and budget lifting are accepted, should the exact n*D counting spelling remain project-local, with only the arbitrary a,b,t,k form upstream?']
a=dict(declaration=N,canonical_index=248,source='Roth/MainLemma.lean:334',verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']},justified_na={'2b':'Definition-only one-line test: target is theorem.','4.5':'All six infrastructure labels n/a for theorem, not a definition/instance.'},questions=questions,unresolved=[],root_acceptance='pending',reason='Exact arithmetic count has one private caller; no existing-only <=3-call witness established. A verified arbitrary strict-base/exponent-budget statement offers a concrete API alternative, but literature supports the construction mechanism rather than a uniquely standard public scalar package. Upstream granularity remains a concrete design decision, independent of proof cost.')
put('assessment.json',a)
base='''theorem powerBudget {a b t : ℝ} {k N : ℕ} (ha : 0 ≤ a) (hb : 1 < b)
    (hbase : a < b ^ t) (hN : 0 < N) (hbudget : t * k ≤ N) : a ^ k < b ^ N'''
entries=[]
for lab,src,receipt,fmt,req in [('original','original-executed.lean.txt','original-final-receipt.json','disk',['COUNT248_FULL_TYPE:','COUNT248_SIGNATURE_IDENTICAL','COUNT248_AUDIT: requested=293; unique=293','COUNT248_AUDIT_PRESENT: present=293; values=293','COUNT248_TYPE_CONSTANTS:','COUNT248_BODY_CONSTANTS:']),('isolated','isolated-executed.lean.txt','isolated-final-receipt.json','raw',["'Count248Isolated."+x+"' depends on axioms:"for x in ['floorBound','powerBudget','flattened','original','zeroBGuard','zeroCGuard','zeroNGuard','noBudgetGuard','zeroExponent','boundaryStrict','halfCGuard','weakBaseGuard','weakConclusion','candidateProbe','naturalVersion','localizedBudget']]),('inline','inline-executed.lean.txt','inline-receipt.json','disk',['COUNT248_INLINE_SIGNATURE_IDENTICAL','COUNT248_INLINE_NO_TARGET',"'Count248Inline.main_lemma' depends on axioms:"])]:
 r=rd(receipt);entries.append(dict(label=lab,source=src,source_sha256=sha(D/src),receipt=receipt,format=fmt,original_execution_request=r['request'],native_region_start_line=17 if fmt=='disk'else 20,required_info=req))
v=dict(declaration=N,canonical_index=248,completed=True,accepted=entries,rejected=[dict(source='rejected-isolated-executed.lean.txt',receipt='rejected-isolated-receipt.json',format='raw',reason='Exact18 lacked genuine Real.add_rpow_le_rpow_add import; recovered sorryAx only in rejected evidence.')],warming=[dict(source='original-initial-success-executed.lean.txt',receipt='original-warming-receipt.json',reason='Initial cold fullmodule diagnostic was partial/timed_out; never accepted as success.')],supplementary_successes=[dict(source=x+'-executed.lean.txt',receipt=x+'-receipt.json',format=f)for x,f in [('original-initial-success','disk'),('isolated-initial-success','raw'),('isolated-second-success','raw')]],standard_axioms=['propext','Classical.choice','Quot.sound'],unresolved=[],audit=dict(source='original-executed.lean.txt',receipt='original-final-receipt.json',requested=293,unique=293,present=293,values=293,exact_source_order_gate='preparation-checks.json'),full_actual_callers=dict(source='inline-executed.lean.txt',receipt='inline-receipt.json',complete_modules=['Roth.MainLemma'],original_signatures_verified=1,direct_target_absence_verified=1,endpoint_axiom_checks=1,target_declaration_removed=True,proof_note='Full original target proof inserted as a local have at the actual sole caller; complete declaring module replayed; helper retained and not claimed existing mathlib.'),composition=dict(original_existing_only_three_call_witness=False,new_proofs_count_as_existing_api=False,abstract_budget_proof_verified=True,independent_floor_proof_verified=True,original_bridge_verified=True,natural_cast_verified=True,broad_exact_search='Not run: avoid broad numerical-heartbeat searches; targeted candidate probes do not prove semantic absence.'),controls=dict(stable_disk_import_count=9,shared_isolated_import_count=18,declaration_only_isolated_import_count=19,shared_prefix_unchanged=True,shared_prefix_sha256=sha(D/'isolated-prefix18.lean.txt'),disk_prefix_sha256=sha(D/'disk-prefix.lean.txt'),additional_import='Mathlib.Analysis.MeanInequalitiesPow',authorization='Explicit root approval for required semantic experiment; pinned header is genuine current module.'),root_acceptance='pending',secret_guard='secret-guard.json')
put('verification.json',v)
o=dict(type=typ,kind='theorem',what='A strict upper bound for the number of integer remainder-coefficient arrays: for B>0,c≥1 and c n D≤N/2 with N>0, (2 floor(B^c)+1)^(nD)<(B+1)^N.',how='Uses floor_rpow_count_lt_aux to bound one coefficient count by (B+1)^(2c), then pow_lt_pow_left₀, Real.rpow_mul_natCast and exponent monotonicity; handles nD=0 using one_lt_pow₀.',hypotheses=['B>0 gives positive real-power base and B+1>1.','c≥1 supplies power superadditivity in the floor-count helper.','N>0 retains strictness in the zero-dimensional case.','c n D≤N/2 is the weak exponent budget; n,D may be zero.'],project_dependencies=['Roth.floor_rpow_count_lt_aux'],caller_summary=rd('callers.json'),mathlib_api_audit='Existing rpow/floor/order primitives are appropriate. No exact existing replacement was verified in all15 search cells; the scalar floor helper and budget theorem in scratch are new proofs, not existing mathlib API.',moral_duplications=[dict(other='Roth.floor_rpow_count_lt_aux',same_statement=False,same_proof=False,action='Keep scalar floor bound distinct from exponent-budget lifting.'),dict(other='Roth.exists_ne_modByMonic_eq',same_statement=False,same_proof=False,action='Keep arithmetic size comparison distinct from finite pigeonhole existence.')],generalization=dict(verified=base,semantic='Arbitrary a,b,t separate count generation from exponent lifting; permits other coefficient-count bounds. Flattening nD to k alone is only representation normalization.',hypothesis_localization='N positivity can be localized to k=0 in verified localizedBudget; exact target cannot drop it because nD=0 is allowed.',sharpness='B0,c0,N0/no-budget and positive c=1/2 counterexamples compile. No claim that c>=1 is sharp or that current hypotheses are globally maximal.'),missing_api=['Possible arbitrary strict-base/exponent-budget lifting law with explicit zero-exponent behavior; public value undecided.','Possible scalar floor-count estimate; supplied project helper is not existing mathlib.'],junk='Not dead: one private actual caller and transitive use in main_lemma. An actual inline proof compiles, but no <=3 existing-mathlib-call proof was established; deletion as trivial wrapper is unsupported.',action='Retain locally while considering the three concrete upstream API questions. Assessment complete, no task blocker; production files unchanged.')
put('overview-entry.json',o)
report=f'''# Roth.pigeonhole_count — canonical248

**Verdict: BORDERLINE-needs-human. Completed assessment; root acceptance pending.**

The mathematical issue is upstream API granularity: a strict scalar floor-count bound and an exponent-budget lifting argument have separable roles. Neither usefulness of the final Roth construction nor brevity of arithmetic spelling decides whether this exact combination belongs in mathlib. No proof-cost argument is used.

## Phase0 — baseline and scope

Fresh SHA256/byte checks of all17 production sources/pins match the tracked shared manifest. The accepted baseline is clean2467 jobs, with the accepted full file-end build at canonical228 unchanged. No file-end build is due at248; next is266. [Fresh inputs]({link('inputs.json')}); [baseline]({link('baseline-build.txt')}). Production Lean, pins, Git and tracked reports remain unchanged.

Read the complete MainLemma module, including private helper247 and complete sole caller581. The exact full-module replay elaborates; target and replay signatures are definitionally identical; target/replay/caller endpoint proofs use only propext, Classical.choice, Quot.sound. [Original source]({link('original-executed.lean.txt')}), [complete raw receipt]({link('original-final-receipt.json')}). The #print body explicitly elides26115 characters: it is **not** claimed to be a full kernel-body dump. Complete written source, full kernel type and direct used-constant lists are retained.

## Phase1 — statement and proof

For positive real B, real c≥1 and natural n,D,N, assume N>0 and c n D≤N/2. Each integer coefficient bounded in absolute value by floor(B^c) has 2 floor(B^c)+1 possible values; the theorem bounds the nD-fold count strictly by (B+1)^N. The floor is natural, the count is natural before coercion, its outer exponent is natural, and B^c is real exponentiation. The cast back to a wholly natural count for natural B also compiles.

Full kernel type, obtained by Lean.getConstInfo with pp.funBinderTypes:

```lean
{typ}
```

B is the coefficient-box bound, c the coefficient growth exponent, n the number of coefficients per remainder, D the number of remainders, N the number of source coefficients. The proof splits nD=0: it uses B+1>1 and N>0 to show 1<(B+1)^N. Otherwise the private scalar helper gives count<(B+1)^(2c); strict natural-power monotonicity lifts this, Real.rpow_mul_natCast combines exponents, and Real.rpow_le_rpow_of_exponent_le uses the weak budget. Equality in the budget still yields a strict final result.

Direct project dependency: only private Roth.floor_rpow_count_lt_aux in the body; no project constants in the type. [All exact native type/body constants]({link('dependencies.json')}). The exact293 ordered/unique/present/value audit finds one direct kernel-value consumer and no direct type consumers. The target has no simp attribute. Lexical references, direct kernel dependencies and transitive dependencies are different scopes; this audit does not pretend to enumerate transitive or simp closure.

## Phase2 — preliminary checks

BIG under the command's literal criterion: the module's Main results lists pigeonhole_count as part of the pigeonhole step. Mathematically it is a numerical helper, so BIG is a framing label only. Definition-only one-line/exemption test: n/a, theorem. No definition has been introduced.

## Phase3 — exhaustive literature

All named channels were actually queried. Exact requests, returned UTF8 response SHA256/bytes/status and clean locators are archived; no article or search-result bodies are stored. Search-tool status is distinguished from unreported HTTP status. Returned hits are evidence of access, not proof that each source states the target.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General specific | Roth theorem auxiliary polynomial pigeonhole "1+2" coefficient count | Auxiliary-polynomial references; additive-combinatorial Roth hits excluded from semantic conclusions. [Receipt]({link('web-general1.json')}) |
| General broader | Siegel lemma pigeonhole principle integer box counting powers inequality | Small integer-solution/box-count mechanism. [Receipt]({link('web-general2.json')}) |
| General aliases | Bernoulli inequality (x+y)^r >= x^r+y^r r >= 1 | Power superadditivity is a standard building block; not an exact final count theorem. [Receipt]({link('web-general3.json')}) |
| ChatGPT math | n/a: ask_chatgpt_math unavailable | Optional channel unavailable; no substitute claim. |
| Local manuscript | clean.tex §6, Lemma9 proof, lines1415–1536 | nD coefficient count and cnD≤r/2, with intermediate2(1+B). [Exact local input hash/excerpt]({link('literature-local-input.json')}); [excerpt]({link('literature-local-excerpt.txt')}) |
| nLab | site:ncatlab.org/nlab pigeonhole principle | Abstract finite-count context; no identified exact scalar law. [Receipt]({link('web-nlab.json')}) |
| nCatLab distinct | site:ncatlab.org/ncatlab pigeonhole principle counting inequality | Returned nLab/other namespace hits do not establish nCatLab coverage. No exact categorical statement identified. [Receipt]({link('web-ncatlab.json')}) |
| Stacks | site:stacks.math.columbia.edu pigeonhole principle polynomial counting | Algebra/exercise hits; no identified exact real floor-power estimate. [Receipt]({link('web-stacks.json')}) |
| MathOverflow | site:mathoverflow.net Siegel lemma pigeonhole principle | Context distinguishes Roth Lemma9 and Siegel argument; discussion is contextual, not primary proof. [Receipt]({link('web-mathoverflow.json')}) |
| Recent arXiv | site:arxiv.org Roth theorem auxiliary polynomial Siegel lemma after:2021-10-29 before:2026-10-30 | Mostly additive-combinatorial Roth/unrelated Siegel; not this Diophantine inequality. [Receipt]({link('web-arxiv.json')}) |
| Recent refined arXiv | site:arxiv.org "Roth" "Diophantine" "formalizing" with same date bounds | Actual empty search, no novelty inference. [Receipt]({link('web-arxiv-refined.json')}) |
| Supplementary primary | Gao, An Introduction to Diophantine Geometry, §3.3.1, printed p50, PDF page49, lines3988–4053 | Uses Siegel lemma to construct a high-index integer polynomial; supports full mechanism, not a named scalar inequality. [Access metadata]({link('web-primary-detail.json')}) |

The [Gao notes](https://ziyangjeremygao.github.io/LectureNotes/DiophantineGeometry.pdf) and the local manuscript support coefficient-box counting within auxiliary-polynomial constructions. No uniquely standard public statement of this exact arithmetic package emerged. This is a limit on positive evidence, not a proof of absence.

The manuscript assumes B>1,c>1 and D≥1, bounds a real count expression by [2(1+B)]^c, then uses 2(1+B)<(1+B)^2. The implementation uses the exact natural floor count and directly bounds it by (B+1)^(2c). This is a different sufficient scalar route, allowing B>0,c≥1 and nD=0. It preserves the strict final count; it is not merely a normalization of the manuscript's intermediate inequality, nor a weakening from < to ≤. The manuscript's assumptions must not be silently reintroduced at the caller.

## Phase4a–b — generality, all parameters

| Parameter / assumption | Mathematical role and actual experiment |
|---|---|
| B:ℝ | Positive real input is broader than the manuscript integer B1; real exponentiation remains concrete. Natural-B exact-cast version compiles. B≥0 alone fails at B0,c1,nD1,N2: 1<1 is false. |
| c:ℝ,1≤c | Used in Real.add_rpow_le_rpow_add. Dropping it fails at c0,B1,nD1,N1:3<2 is false; even c>0 fails at c=1/2 with the same B,nD,N. The threshold1 is sufficient, **not asserted sharp**. |
| n,D:ℕ | Only their product enters the proof, count and budget. k=nD restatement compiles; every natural k already arises as n=k,D=1, so this alone is representation improvement, not new mathematical generality. Zero factors are allowed and tested. |
| N:ℕ,0<N | Natural source dimension. At N0,nD0,B1,c1 all remaining assumptions hold but1<1 fails. In arbitrary-base lifting, positivity can be localized to k=0; verified localizedBudget. For nD≠0 the original positive-c budget already forces N>0. |
| hD:c n D≤N/2 | Weak budget is intentional. B1,c1,nD1,N2 realizes equality yet gives3<4. Dropping budget fails with B1,c1,nD1,N1. Rewriting to2c k≤N compiles. |
| Strict conclusion | Supplies finite pigeonhole; weakConclusion compiles by .le but does not replace strictness needed downstream. A weak base bound plus weak budget fails even with b2,t1,k1,N1,a2; weakBaseGuard verifies this. |
| Concrete types | No typeclass/universe hypotheses to drop. Real.rpow has specific analytic content; replacing ℝ by an arbitrary ordered field is not asserted meaningful or verified. Natural dimensions encode finite cardinality. |

No assumption can simply be deleted uniformly in the current interface; no sharp maximality claim is made. As a mechanical weakening of this fixed arithmetic spelling, current form is MAXIMALLY GENERAL in the command's tested sense. A distinct semantic abstraction is verified: replace the generated count and special2c relation by an arbitrary a,b,t and strict base bound. It is a new theorem, not existing mathlib.

```lean
{base}
```

`localizedBudget` further uses `(hzero : k = 0 → 0 < N)` instead of global positivity. `flattened` specializes a to the floor count,b=B+1,t=2c; `original` supplies the original arithmetic budget. This is concrete semantic reuse: other coefficient ranges/count bounds can supply their own a<b^t without reproving the zero/nonzero exponent argument. It does not assert any unverified new scalar bound. [Exact isolated source]({link('isolated-executed.lean.txt')}); [raw receipt]({link('isolated-final-receipt.json')}).

## Phase4c — all nine modern-idiom rows

| # | Question | Decision and downstream consequence |
|---|---|---|
|1|Typeclass preambles|No. Positivity and numerical budgets are value hypotheses, not mathematical structures; making them classes creates no useful instance inference.|
|2|Sequences to filters|No sequences or convergence.|
|3|Universal-property construction|No constructed algebraic/topological object.|
|4|Closure predicates to bundled substructures|No substructure predicate.|
|5|Weaker module/field hierarchy|No algebraic hierarchy parameter; ℝ carries real exponentiation. No speculative ordered-field rpow API.|
|6|Higher categorical form|No categorical data; finite inequality is not a categorification target.|
|7|Concrete indices|n,D may be collapsed to natural k, verified. This simplifies `Real.rpow_mul_natCast` application but is representation only; ℕ remains the cardinal exponent.|
|8|Concrete-via-abstract diagnostic|Yes for the generated scalar expression, rather than a named mathematical object. Lexically floor appears only in the scalar helper call's inferred argument; after that the proof lifts a strict base bound. The verified arbitrary a,b,t form removes dependence on how count is generated and composes with other bound-producing lemmas. No named Roth definition occurs in the statement or tail proof; no fictitious named-object grep claim.|
|9|False-generalisation guard|Pass for verified specialization with a≥0,b>1,a<b^t and budget. Removing strictness/positivity is rejected by guards. Replacing ℝ-rpow with generic field powers, or replacing strict final count with weak count, is not licensed.|

Modern-idiom alternative available as the verified scalar/exponent separation. It offers concrete compositional organization; no filters/categories/typeclasses are introduced. Its public API value is a question of granularity, not proof expense.

## Phase4.5 — six infrastructure labels

The declaration is a theorem; each row is justified n/a. Typeclass diamond: no instance path introduced. Reducibility leak: no new data definition. Non-canonical unfolding: no new computational unfolding rule. Instance priority collision: no instance registered. Universe-polymorphism issues: no data/type constructor added; concrete ℝ/ℕ statement. Coercion ambiguity: no coercion registered, and natural/real casts explicitly tested. Overall theorem infrastructure risk n/a.

## Phase4.6 — five proof-strategy rows

| # | Question | Outcome |
|---|---|---|
|1|ε-δ vs filters|n/a: finite scalar inequality.|
|2|Elements vs subobjects|n/a: no ideal/module inclusion.|
|3|Sequences vs nets|n/a: no limiting process.|
|4|Construction vs universal property|n/a: no categorical construction.|
|5|Missing helper mathlib should have|Potential scalar floor-count bound and arbitrary budget lifting, independently verified; public packaging is not decided by current short syntax.|

Strategy: REFACTOR-RECOMMENDED for an upstream proposal. Separate the scalar floor estimate from generic strict-power lifting, retaining the explicit zero branch; this states what is reusable without adding a new mathematical proof technique. Current direct monotonicity strategy is mathematically sound. Any upstream refactor must decide which small boundary-aware package is useful, not introduce logarithms simply to shorten arithmetic.

## Phase5 — all15 formal search cells

[Matrix]({link('formal-search-matrix.json')}) links all complete requests and raw formal responses; source rg receipts include complete output and exit status. External indexes may differ from the pin. Local index status was error/warming: project matches are not mathlib hits, and these limitations do not establish absence.

| Form | Lean-Finder | Loogle | LeanSearch | rg | Local-name |
|---|---|---|---|---|---|
|Current exact floor/count budget|Behrend and Bertrand near-hits, not exact result|No returned hits|Natural logarithm/count near-hits|Exact-name/count-pattern search retained|Target only, index error|
|Literature standard box/Siegel count|Additive-combinatorial Behrend hits|No returned hits|Siegel integer matrix existence, broader construction, not scalar inequality|Power-superadditivity/Siegel/floor candidates retained|Project floor helper only, index error|
|Abstract strict base/exponent budget|Generic power monotonicity near-hits|No returned hits|pow_lt_pow_left₀ is a real building block|rpow product, monotonicity, zero-exponent primitives|Real.rpow_mul_natCast plus NNReal/ENNReal variants, warming|

Pinned statements/proofs read and archived for Real.add_rpow_le_rpow_add (MeanInequalitiesPow:190), Real.rpow_mul_natCast (Pow/Real:520), Real.rpow_le_rpow_of_exponent_le (Pow/Real:617), natural-power monotonicity and floor bounds. Exact signature checks appear in isolated receipt. Siegel matrix existence and Behrend additive-combinatorial theorems are contextual near-hits: their conclusions do not give the required scalar inequality. [Pinned inputs]({link('mathlib-inputs.json')}). [Untruncated exact-name search]({link('full-name-search.json')}).

Conclusion: verified existing building blocks, no verified existing exact or general replacement. No claim of semantic absence from empty search. New `floorBound`, `powerBudget`, `flattened`, `original` are newly proved scratch declarations, excluded from existing-mathlib call counts.

## Phase5.5 — three statement-shape checks

Normal form: a strict real inequality after natural count coercion matches the actual caller; the natural-B natural-count form also compiles. Alternatives are flattened k, exponent budget2ck≤N, or arbitrary strict base bound plus exponent budget. No competing global normal form was found. This is not an A↔B normalization theorem, so RHS equivalence convention is n/a.

Syntactic generality: the current spelling directly accepts f.natDegree,J.card and the exact counting hD supplied by the sole caller. Flattening removes duplicate product structure; arbitrary a,b,t enables a wider family of count estimates. Both were actually compiled. For an upstream candidate choose the abstract base/budget form, retaining original arithmetic specialization locally.

Superfluous-argument audit: no undeclared typeclass premises; B positivity,N positivity,c bound and budget cannot simply be dropped uniformly (guards above). n,D are a redundant factorization, not dead parameters. N positivity can be point-localized to k0 in the abstract API. Overall: RESTATE-BEFORE-SHIP if an upstream proposal proceeds; no change required to the preserved production interface.

## Phase6.0 — full callers and inline audit

Internal-use count under command's **excluding declaring file** convention:0. Total actual proof uses:1, in the declaring file. External-to-file distinct callers:0. One module-docstring mention is not a proof use.

| Caller | Actual usage and role |
|---|---|
|private Roth.exists_mem_RSet_le_index_of_rpow_bound_aux, MainLemma:581, call:615|`pigeonhole_count (Nat.cast_pos.2 hB) hc (Finset.prod_pos ...) hD`; n=f.natDegree,D=J.card,N=∏(rj+1),C=floor(B^c). Supplies strict count to exists_mem_RSet_le_index_aux.|

[Fresh lexical/tracked searches]({link('source-search.json')}); [tracked cross-check]({link('tracked-source-search.json')}); [inline derivation search]({link('inline-search.json')}); [caller metadata]({link('callers.json')}). No bypassing equivalent derivation found in production sources. The helper is only a scalar bound, not a second proof of the full count. Kernel canonical audit independently confirms this sole direct consumer; transitive downstream use is through the private construction and main_lemma.

The complete original proof was physically inlined as a typed local `have countBound` in this actual caller, with the target declaration removed from a full MainLemma replay. The caller's full original signature is preserved by native defeq check; its body contains no direct target constant. The replayed main_lemma has standard axioms. This demonstrates a concrete local alternative, **not** trivial mathlib composability: the private scalar floor lemma remains a real project ingredient. [Complete source]({link('inline-executed.lean.txt')}); [raw result]({link('inline-receipt.json')}).

## Phase6 — composition experiments

Attempt1: apply pow_lt_pow_left₀ to the scalar floor bound. This yields the wrong final RHS and needs nD≠0; a targeted `fail_if_success` verifies it does not close the original goal. It also uses a newly proved floorBound, so it cannot count as an existing-only replacement.

Attempt2: Real.rpow_le_rpow_of_exponent_le supplies only a weak bound for matching powers; it neither proves the scalar floor count nor supplies final strictness/zero branch. The targeted candidate closure probe fails, then the complete independently reconstructed proof closes. No broad exact? numerical search or resource increase was used; no semantic absence claim is inferred.

Attempt3: the new powerBudget theorem, scalar floorBound, arithmetic normalization and casts do prove the original statement; naturalVersion confirms the exact natural count. All are fully verified, but new helpers are not existing mathlib calls. The floor helper itself uses power superadditivity, positive square slack and a floor bound; this is not a ≤3-call witness for the original target.

Conclusion: NOT-COMPOSABLE under the command's existing-only≤3 criterion on established evidence. This does not constitute proof that no clever alternative exists, and does not by itself force a YES verdict; independent public API value still matters.

## Overview synthesis — API, moral duplication, generalization, junk

| Pair | Same statement? | Same proof mechanism? | Action |
|---|---|---|---|
|pigeonhole_count / private floor_rpow_count_lt_aux|No; powered count vs one coefficient count|No; exponent budget lifting vs scalar square/superadditivity slack|Keep the scalar input bound separate from the lifting law.|
|pigeonhole_count / exists_ne_modByMonic_eq|No; arithmetic inequality vs existence of two polynomial witnesses|No; power inequalities vs finite-function cardinal pigeonhole|Keep the arithmetic bound and existence theorem distinct.|
|pigeonhole_count / ncard_boxFamily|No; strict image-size upper bound vs exact source-family cardinality|No; monotonicity vs coefficient-array enumeration|Combine at use, not an artificial unification.|

API audit: existing Real.rpow, natural powers, natural floor, and order lemmas are the appropriate rich APIs; no custom powers, floors or cardinality structures should be introduced. Missing-API candidate is precisely the arbitrary strict-base/exponent-budget law with zero handling, plus independently assessed scalar floor estimate. Generalization is semantic separation of generated count from budget, rather than merely factor names/constants. Junk: target is live and nontrivial under the established composability criterion; localizing the one-use arithmetic helper is a verified optional project design, not an automatic deletion recommendation. No claim of external adoption was found.

## Phase7–8 — verdict, concrete future upstream questions

**BORDERLINE-needs-human.** The target contributes a boundary-aware arithmetic step, but its exact nD,2c,N/2 spelling is tailored to one private Diophantine caller. The literature supports the full auxiliary-polynomial/Siegel mechanism; it does not identify this precise scalar package as a uniquely standard public theorem. The verified arbitrary-base restatement supplies a concrete alternative, while the scalar helper and finite pigeonhole theorem remain distinct content. This is an API-granularity judgment, not an uncompleted search, unavailable proof, inherited verdict, or cost-based downgrade.

'''+ '\n'.join(str(i+1)+'. '+q for i,q in enumerate(questions))+f'''

These are future upstream design questions, not blockers to completing this read-only assessment. Retain the production interface. If public generic budget API is chosen, start from the exact verified powerBudget/localizedBudget signatures and keep the exact floor/count specialization local unless independently justified. If the scalar bound alone is chosen upstream, replace its helper use only after actual acceptance; do not claim a nonexistent existing replacement today. If neither is chosen, keep this arithmetic step private/local in Roth/MainLemma.lean; the archived actual caller inlining is the concrete alternative.

No YES grouping/title/reviewer is proposed because this verdict does not authorize an upstream package. No production edit, deployment, Git mutation or publication was performed. All required assessment phases are complete; verification unresolved is empty, with root review pending. [Machine assessment]({link('assessment.json')}); [verification]({link('verification.json')}); [portable validator]({link('validate.py')}).
'''
put('report.md',report)
print('PASS report, assessment, verification and exact-key overview entry written')
