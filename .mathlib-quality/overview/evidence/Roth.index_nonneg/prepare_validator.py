from pathlib import Path
D=Path(__file__).parent;P=Path('/private/tmp/roth-overview/assess/Roth.le_index_iff')
s=(P/'validate.py').read_text().replace("NAME='Roth.le_index_iff'","NAME='Roth.index_nonneg'")
s=s.replace("let target := `Roth.le_index_iff","let target := `Roth.index_nonneg")
a=s.index("cs=read('callers.json')");b=s.index("formal=read('formal-search.json')")
s=s[:a]+'''cs=read('callers.json');assert len(cs)==3 and sum(c['identifier_occurrences'] for c in cs)==3
assert sum(c['file']=='Roth/Index.lean' for c in cs)==1
for c in cs:
 assert sha(ROOT/c['file'])==c['source_sha256'] and c['source_fragment'] in (ROOT/c['file']).read_text() and c['plan']
 for line in c['reference_lines']:assert 'index_nonneg' in (ROOT/c['file']).read_text().splitlines()[line-1]
cons=read('direct-consumers.json');assert cons['count']==3 and set(cons['consumers'])=={c['declaration'] for c in cs}
search=read('complete-caller-search.json');assert len(search['searches'])==2
assert all(e['exit_code']==0 and len(e['stdout'].splitlines())==4 for e in search['searches'])
assert {x['file'] for x in order}<=set(search['canonical_source_inventory'])
orig=next(e for e in v['accepted'] if e['label']=='original-and-audit');ds=native(orig)
new=[x for x in ds if x.get('line',0)>=v['audit']['native_region_start_line']]
actualcons=[x['message'].split(': ',1)[1] for x in new if x['message'].startswith('INDEX_NONNEG138_DIRECT_CONSUMER:')]
assert actualcons==cons['consumers']
s=(D/'index-nonneg-callers-executed.lean.txt').read_text();assert not re.search(r'\\bindex_nonneg\\b',s)
assert s.count('IndexNonneg138.originalReplacement')==3 and 'theorem replacement' in s
assert all(n in s for n in ['IndexReplay138.index_eq_zero_iff','ThetaReplay138.Θ_nonneg','ThetaReplay138.sum_max_sub_le_index_det'])
'''+s[b:]
s=s.replace("assert s=='\\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:556])+'\\n'","assert s=='\\n'.join((ROOT/'.mathlib-quality/references/clean.tex').read_text().splitlines()[529:570])+'\\n'")
s=s.replace("['Fintype','MvPolynomial','hasseDeriv','Roth.index','Roth.weight']","['Fintype','MvPolynomial','0 ≤ Roth.index','σ → ℕ']")
s=s.replace('four callers/five applications','three callers/three applications')
s=s.replace("for e in formal:assert e['result'].get('isError') is False","for e in formal:\n assert e['result'].get('isError') is False and e['request']['query']")
(D/'validate.py').write_text(s)
