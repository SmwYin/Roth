from pathlib import Path
import re,json
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.main_lemma');prefix=(D/'disk-prefix.lean.txt').read_text();raw=(R/'Roth/MainLemma.lean').read_text();module=raw[raw.index('namespace Roth'):];original=module.replace('namespace Roth','namespace Main266Original\nopen Roth',1).replace('end Roth','end Main266Original');original=re.sub(r'\bmain_lemma\b','replay',original);assert(D/'original-executed.lean.txt').read_text().startswith(prefix+original+'\n')
# Reconstruct complete actual caller module independently from source and the exact target proof.
main=(R/'Roth/Main.lean').read_text();main=main[main.index('namespace Roth'):].replace('namespace Roth','namespace Main266Inline\nopen Roth',1).replace('end Roth','end Main266Inline')
decl=raw[raw.index('theorem main_lemma'):raw.rindex('\nend Roth')];sig,proof=decl.split(' := by\n',1);concl='∃ Q'+sig.split(' : ∃ Q',1)[1];proof=proof.rstrip('\n').replace('exists_auxiliary_polynomial_with_index_gap_aux','auxgap266').replace('exists_hasseDeriv_index_eval_bound_aux','selectInline266').replace('hW hh','hW hcop');inline='show '+concl+' from by\n'+'\n'.join('    '+s for s in proof.splitlines());call='main_lemma hf hfα hA hδ0 hδm hrlast h31b h32 h33 hcop';assert main.count(call)==1;main=main.replace(call,inline)
setup='''
open Lean Elab Term in
elab "auxgap266" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.exists_auxiliary_polynomial_with_index_gap_aux)
open Lean Elab Term in
elab "selectInline266" : term =>
  Lean.Meta.mkConstWithFreshMVarLevels
    (Lean.mkPrivateNameCore `Roth.MainLemma `Roth.exists_hasseDeriv_index_eval_bound_aux)
''';main=main.replace('open Roth\n','open Roth\n'+setup,1);assert(D/'inline-executed.lean.txt').read_text().startswith(prefix+main+'\n')
# Exact independent reconstruction preserves all mathematical target and caller proof bodies.
v=json.loads((D/'verification.json').read_text())
for e in v['accepted']:
 q=json.loads((D/e['receipt']).read_text());z=q['result']['structuredContent'];z=z.get('result',z);ds=z.get('items',z.get('diagnostics'));assert z['success']and not z.get('partial',False);assert not[x for x in ds if x['severity']in['error','warning']]
 print(e['label'],q['elapsed_ms'],'ms',len(ds),'messages',sum('depends on axioms'in x['message']for x in ds),'axiom prints','elision:',sum('LEAN_MCP_MAX_OUTPUT_CHARS'in x['message']or'characters elided'in x['message']for x in ds))
print('PASS root independent complete original and actual-caller module reconstruction; five clean raw receipts inspected; original pp.all elision disclosed')
