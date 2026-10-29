from pathlib import Path
import json,re
R=Path('/Users/ramin/LEAN/Roth');D=Path('/private/tmp/roth-overview/assess/Roth.approxSet');prefix=(D/'disk-prefix.lean.txt').read_text()
s=(R/'Roth/Main.lean').read_text();base=s[s.index('namespace Roth'):]
original=base.replace('namespace Roth','namespace Approx267Original\nopen Roth',1).replace('end Roth','end Approx267Original');original=re.sub(r'\bapproxSet\b','replay',original)
assert(D/'original-executed.lean.txt').read_text().startswith(prefix+original)
raw='''(fun (α κ : ℝ) ↦
      ({hq : ℤ × ℕ | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ} : Set (ℤ × ℕ)))
      '''
main=base.replace('namespace Roth','namespace Approx267Inline\nopen Roth',1).replace('end Roth','end Approx267Inline');main=re.sub(r'/\-.*?\-/','',main,flags=re.S);main=re.sub(r'def approxSet \(α κ : ℝ\) : Set \(ℤ × ℕ\) :=\n  .*\n','',main);main=re.sub(r'\bapproxSet\b',raw,main)
s=(R/'Roth/LeanEval.lean').read_text();other=s[s.index('namespace LeanEval.NumberTheory.ThueSiegelRothProblem'):];other=other.replace('namespace LeanEval.NumberTheory.ThueSiegelRothProblem','namespace Approx267InlineLeanEval',1).replace('end LeanEval.NumberTheory.ThueSiegelRothProblem','end Approx267InlineLeanEval');other=re.sub(r'/\-.*?\-/','',other,flags=re.S).replace('Roth.approxSet ',raw+' ')
actual=(D/'inline-executed.lean.txt').read_text();expected=prefix+main+'\n'+other+'\n';assert actual.startswith(expected);assert not re.search(r'\bapproxSet\b',actual[len(prefix):])
checks=actual[len(expected):];assert checks.count('Subsingleton.elim _ _')==12
for label in ['original','project','isolated','inline','supplement']:
 q=json.loads((D/(label+'-receipt.json')).read_text());z=q['result']['structuredContent'];z=z.get('result',z);assert z['success']and not z.get('partial',False)and not z.get('timed_out',False)
 ds=z.get('items',z.get('diagnostics'));assert not[x for x in ds if x['severity']in['warning','error']];assert not any('sorryAx'in x['message']for x in ds)
 print(label,q['elapsed_ms'],'ms',len(ds),'messages')
print('PASS root exact original full Main and literal-definition full Main/LeanEval inlining independently reconstructed;12 signature checks; five raw native receipts clean. Not final assessment acceptance.')
