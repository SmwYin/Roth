from pathlib import Path
import json,re,hashlib,subprocess
D=Path(__file__).resolve().parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.exists_approximants'
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def rd(n):return json.loads((D/n).read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(n,args):
 r=subprocess.run(args,cwd=R,text=True,capture_output=True);put(n,dict(request=args,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));return r
for m in ['Main','LeanEval']:(D/('source-'+m+'.lean.txt')).write_bytes((R/('Roth/'+m+'.lean')).read_bytes())
run('source-search.json',['rg','--no-ignore','-n','exists_approximants','Roth','Roth.lean'])
run('tracked-source-search.json',['git','grep','-n','exists_approximants','--','Roth/*.lean','Roth.lean'])
run('inline-search.json',['rg','--no-ignore','-n','Nat.rec|lt_log_of_rpow_lt|Real.exp L|2 / δ \\* Real.log','Roth','Roth.lean'])
forms={'current':r'exists_approximants|exists_reduced_approx|infinite_rat_abs_sub_lt_one_div_den_sq',
 'standard':r'exists_strictMono_subsequence|extraction_forall_of_frequently|seq_of_forall_finite_exists',
 'abstract':r'sequenceOfCofinals|not_bddAbove_iff|exists_seq_of_forall_finset_exists|dependent.*choice'}
for f,p in forms.items():run('formal-'+f+'-rg.json',['rg','-n',p,'.lake/packages/mathlib/Mathlib'])
run('name-search.json',['rg','-n',r'Roth\.exists_approximants|theorem exists_approximants|lemma exists_approximants','.lake/packages/mathlib/Mathlib'])
run('literature-local.json',['rg','-n',r'reduced solutions|pick a reduced|choose solutions|roth:eq50','.mathlib-quality/references/clean.tex'])
loc=R/'.mathlib-quality/references/clean.tex';put('literature-source.json',dict(path=str(loc.relative_to(R)),sha256=sha(loc),bytes=loc.stat().st_size));(D/'local-excerpt.tex.txt').write_text('\n'.join(loc.read_text().splitlines()[1570:1614])+'\n')
paths=['Mathlib/Data/Set/Finite/Basic.lean','Mathlib/Order/Monotone/Basic.lean','Mathlib/Order/Filter/AtTopBot/Basic.lean','Mathlib/Order/Ideal.lean','Mathlib/NumberTheory/DiophantineApproximation/Basic.lean','Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean']
xs=[]
for i,p in enumerate(paths):
 q=R/'.lake/packages/mathlib'/p;a='mathlib-source-'+str(i)+'.lean.txt';(D/a).write_bytes(q.read_bytes());xs.append(dict(path=str(q.relative_to(R)),archive=a,sha256=sha(q),bytes=q.stat().st_size))
put('mathlib-inputs.json',xs)
put('formal-search-matrix.json',dict(cells=[dict(form=f,method=m,receipt='formal-'+f+'-'+m+'.json',assessment='Actual local index error; no absence inference.'if m=='local'else'Executed actual query; partial generic selection/Dirichlet candidates inspected, no exact old signature established.')for f in forms for m in ['leanfinder','loogle','leansearch','rg','local']],conclusion='Selection primitives and Dirichlet exist; current fixed-constant reduced chain not verified as an existing theorem or ≤3-call composition.'))
channels=[]
info={
'web-specific':('An elementary approach to Roth’s theorem','https://aleksa-milojevic.github.io/expository/roth.pdf','§2, page3 and §6','Author exposition explicitly chooses a finite list with rapidly increasing denominators; not a named general finite-chain theorem.'),
'web-general':('Axiom of Choice, Eric Schechter','https://math.vanderbilt.edu/schectex/ccc/choice.html','Choice variants','Recursive witness selection is a dependent-choice pattern. Exact arithmetic approximation is additional input.'),
'web-alias':('Geometric Number Theory','https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf','§4.5, Lemma4.5.3','Gap principles constrain all sufficiently good reduced approximants; our theorem instead selects a sparse finite subsequence. Do not identify these statements.'),
'nlab':('dependent choice in nLab','https://ncatlab.org/nlab/show/dependent%20choice','search result; direct fetch unsupported XHTML','Serial relations admit recursively linked countable choices. Direct opening returned unsupported application/xhtml+xml; search evidence alone retained.'),
'ncatlab':('No exact /ncatlab namespace result',None,'actual site:ncatlab.org/ncatlab query','Returned /nlab and other out-of-namespace results. No exact namespace hit; no categorical generalization claimed.'),
'stacks':('Lemma10.86.3 (0597)','https://stacks.math.columbia.edu/tag/0597','proof, cofinal sequence and choice','A countable directed inverse-system proof constructs a cofinal sequence by induction. Useful structural analogy, not a Diophantine chain statement.'),
'mathoverflow':('Estimate number of solutions in the Roth’s theorem','https://mathoverflow.net/questions/249176/estimate-number-of-solutions-in-the-roths-theorem/249191','discussion of quantitative Roth','Search finds quantitative finiteness/gap questions, not exact arbitrary-cofinal-height finite selection API.'),
'arxiv':('Transcendence of continued fractions over function fields and a quantitative version of Uchiyama’s theorem','https://arxiv.org/abs/2608.15119','2026 search result','Function-field transcendence analogue appeared in the dated query. Other hits were additive Roth/irrelevant approximation papers; no exact finite-selection result found. Refined dated Diophantine gap query returned empty.')}
for n,(title,url,locator,summary) in info.items():
 q=rd(n+'.json')['request']['search_query'][0]['q'];channels.append(dict(channel=n,query=q,title=title,url=url,locator=locator,summary=summary,receipt=n+'.json'))
put('literature.json',dict(general_queries=[dict(q=rd(n+'.json')['request']['search_query'][0]['q'],receipt=n+'.json')for n in ['web-specific','web-general','web-alias']],channels=channels,optional_channel=dict(channel='ask_chatgpt_math',status='n/a',reason='Tool unavailable; full other channels executed.'),local_channel=dict(channel='local',status='checked',receipt='literature-local.json',locator='clean.tex1572–1613, §7 eq50',summary='Source selects first denominator past a bound then successive reduced denominators; uses positive δ elsewhere, while actual Lean theorem permits every real δ.'),third_party_bodies_persisted=False,primary_receipt='primary.json',summary='Sparse finite choice from unbounded reduced denominators is standard proof organization; generic cofinal-height recursion is the reusable mechanism. Fixed-constant approximation membership remains substantive, distinct from existential-C LiouvilleWith.'))
body=rd('target-metadata.json')['source'].split(':= by\n',1)[1]
order=rd('canonical-snapshot.json');deps=[x['name']for x in order if re.search(r'(?<![\w.])'+re.escape(x['name'].split('.')[-1])+r'\b',body)]
assert deps==['Roth.approxSet','Roth.exists_reduced_approx']
put('concrete-diagnostic.json',dict(identifiers={x:dict(lines=sum(x in l for l in body.splitlines()),occurrences=body.count(x))for x in ['α','κ','Irrational','approxSet','exists_reduced_approx','Real.log']},diagnostic='α and κ appear only in the initial selector and membership type; recursion uses only an unbounded admissible-height selector. Generic real-height sequence plus exact full recovery compiled. Coprimality is carried in s, not inferred abstractly.'))
put('callers.json',dict(explicit_caller_count=1,external_to_file_count=0,callers=[dict(name='Roth.exists_roth_approximants_aux',file='Roth/Main.lean',declaration_line=429,declaration_end_line=450,call_line=438)],reading=['Entire Roth/Main.lean1–588','Entire Roth/LeanEval.lean1–73'],verification_scope='Complete actual private caller with literal target proof inlined, and complete actual caller with generic recovered target replacement; original signature retained in both, only visibility/name changed. No transitive terminal proof replay claimed.'))
print('Fresh source/local/search/literature artifacts collected')
