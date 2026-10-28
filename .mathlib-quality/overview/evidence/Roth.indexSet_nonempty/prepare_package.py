from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');T=Path('/private/tmp/roth-overview');N='Roth.indexSet_nonempty'
def put(n,v):(D/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p in T.glob('nonempty185-*'):
 if p.is_file():shutil.copy(p,D/('git-callers.json'if p.name=='nonempty185-git-callers.json'else p.name))
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
put('assessment.json',{'declaration':N,'canonical_index':185,'source':'Roth/Theta.lean:80','verdict':'NO-mathlib-has-it','completed':True,'allphases':'PASS','phases':dict.fromkeys(ph,'PASS'),'unresolved':[],'root_acceptance':'pending'})
orig=json.loads((D/'nonempty185-original-receipt.json').read_text())['result']['structuredContent']['result']
ty=next(x['message'].split('NONEMPTY185_FULL_TYPE: ')[1]for x in orig['items']if x['message'].startswith('NONEMPTY185_FULL_TYPE: ')).replace('\n',' ')
put('native-type.json',{'type':ty,'body_elision':False,'standard_axioms':['propext','Classical.choice','Quot.sound']})
put('overview-entry.json',{'declaration':N,'kind':'theorem','type':ty,'what':'For B≥1 the bounded integer polynomial index family is nonempty.','how':'Use polynomial1, whose degrees vanish and coefficients are bounded, and numerators constantly1, coprime to arbitrary q.','hypotheses':['σ arbitrary universe; Fintype required by unchanged index parent','B:ℝ;1≤B','q r:σ→ℕ arbitrary including zeros; no DecidableEq'],'project_dependencies':['Roth.indexSet','Roth.RSet','Roth.index','Roth.one_mem_RSet'],'caller_summary':'2 explicit calls, both Theta:127/136;0 outside-file; canonical293 finds2 value/0 type consumers. Both complete caller replacements native clean.','mathlib_api_audit':'All15 method×form cells: Set.Nonempty.image2 and Set.image2_nonempty_iff independently native verified; local index unavailable disclosed.','moral_duplications':'Binary-image nonemptiness after accepted180 parent re-aim. Arithmetic complete-family witness is separately project mathematics, not a mathlib building block.','generalization':'Abstract law accepts arbitrary types/sets/total binary maps without Fintype, arithmetic, order or topology. Original hB is sharp: actual indexSet.Nonempty↔1≤B checked via nonzero integer coefficient.','missing_api':'No missing binary-image nonempty law. Accepted184 bounded-family API judgment remains separate.','junk':'Useful locally to2 supremum callers; delete wrapper with parent re-aim and use existing image2 law; local paper-navigation compatibility is the only retention rationale.','action':'NO-mathlib-has-it: re-aim indexSet at image2; replace nonempty premises at Θ_le_of_forall_index_le and Θ_mono by image2_nonempty_iff plus full unit and coprime witnesses; no upstream addition.'})
accepted=[]
for label,fmt,region,req in [
 ('original','disk',15,['NONEMPTY185_FULL_TYPE:','NONEMPTY185_AUDIT: requested=293; unique=293','NONEMPTY185_AUDIT_PRESENT: present=293; values=293']),
 ('project','disk',int((D/'nonempty185-project-region.txt').read_text()),["'Nonempty185.bridge' depends on axioms:","'Nonempty185.replacement' depends on axioms:","'Nonempty185.replacement_expanded' depends on axioms:","'Nonempty185.caller_bound' depends on axioms:","'Nonempty185.caller_mono' depends on axioms:","'Nonempty185.family_nonempty_iff' depends on axioms:","'Nonempty185.nonempty_iff' depends on axioms:","'Nonempty185.zero_bound_empty' depends on axioms:"]),
 ('isolated','raw',16,["'Nonempty185Isolated.generic' does not depend on any axioms","'Nonempty185Isolated.generic_iff' does not depend on any axioms",'@Set.Nonempty.image2','@Set.image2_nonempty_iff'])]:
 src='nonempty185-'+label+'-executed.lean.txt';accepted.append({'label':label,'format':fmt,'source':src,'source_sha256':sha(D/src),'receipt':'nonempty185-'+label+'-receipt.json','native_region_start_line':region,'required_info':req})
put('verification.json',{'declaration':N,'unresolved':[],'standard_axioms':['propext','Classical.choice','Quot.sound'],'accepted':accepted,'rejected':[{'source':'nonempty185-project-rejected1-executed.lean.txt','receipt':'nonempty185-project-rejected1-receipt.json','reason':'Direct image2 source-set inference exhausted default200k heartbeats despite explicit f; not accepted. Final iff rewrite avoids that route without raised limits.'}],'audit':{'source':'nonempty185-audit-executed.lean.txt','receipt':'nonempty185-original-receipt.json','marker':'NONEMPTY185'},'canonical_direct_consumers':['Roth.Θ_le_of_forall_index_le','Roth.Θ_mono'],'canonical_direct_type_consumers':[],'composition':{'parent_reaim':'accepted180 indexSet exact image2; analogous law independently verified here','bridge_definitional':True,'complete_family_checked':True,'strict_three_existing_call_term_verified':False,'parent_project_def_counted_as_mathlib_block':False,'no_global_absence_claim':True,'accepted_old_form_route':'rw [bridge, Set.image2_nonempty_iff]; exact paired complete source witnesses','generic_route':'hs.image2 ht isolated clean'}})
p=D/'report.md';s=p.read_text().replace('coprrimality','coprimality').replace('The explicit f instantiation resolves all map arguments.','A direct image2 application still exhausted default200k heartbeats despite explicit f; the accepted current-form proof rewrites by the bridge and `Set.image2_nonempty_iff` first, then supplies the pair. No limits were raised.').replace('Its unit-membership premise calls','The bridge itself is definitionally true (`rfl` checked), although the old-form proof still needs an explicit rewrite to guide elaboration. The rejected direct image2 attempt is retained separately and is not accepted evidence. Its unit-membership premise calls')
s=s.replace('One-line generic replacement is', '''The actual checked old-form proof is:

```lean
rw [bridge, Set.image2_nonempty_iff]
exact ⟨⟨1, Roth.one_mem_RSet hB r⟩,
  ⟨fun _ ↦ 1, fun _ ↦ isCoprime_one_left⟩⟩
```

Here `bridge` is the checked exact equality from `indexSet` to the full image2 expression, proved by `rfl`. It is a project-representation proof, not an additional mathlib building block. This expanded snippet preserves honest accounting of the arithmetic premise.

One-line generic replacement is''')
p.write_text(s)
