"""Assemble scratch overview from accepted evidence; never edits tracked reports.
--require-complete enforces all293 before producing the final candidate document.
"""
from pathlib import Path
import json,hashlib,re,collections,sys
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth');load=lambda n:json.loads((B/n).read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
I=load('final-completed-inventory-preparation.json');rows=I['rows'];n=len(rows);assert n==I['completed_count'];complete='--require-complete'in sys.argv
if complete:assert n==293
for x in rows:assert H(Path(x.get('report_source',str(R/x['report']))))==x['report_sha256']
P=json.loads((B/'final-pairwise-partitions/index.json').read_text());A=load('final-completed-action-synthesis-coverage-preparation.json');assert P['accepted_declaration_count']==A['completed_count']==n and not A['unreconciled_completed']
assert P['pair_count']==n*(n-1)//2 and P['markdown_artifacts']
if complete:assert P['complete_project_pair_coverage']and n==293
old=(R/'PROJECT_OVERVIEW.md').read_text();parts={}
for k in range(3,8):
 pattern=r'^## Part '+str(k)+r':.*?(?=^## Part '+str(k+1)+r':)';m=re.search(pattern,old,re.M|re.S);assert m;parts[k]=m[0].rstrip()
if complete:
 stale='For the completed declaration, no second independent implementation of the same support\nproduct was found in project code. The all-coordinate finite product is a bridge, not a\nbetter replacement for arbitrary variable types. Other declaration findings remain unpublished.'
 assert stale in parts[4]
 parts[4]=parts[4].replace(stale,'All293 declarations have completed assessments. The support-product coefficient has no second independent implementation; its all-coordinate product bridge is not a better replacement for arbitrary variable types. The complete pair evidence below distinguishes shared ingredients, equivalent endpoint interfaces and substantive independent statements across the whole project.')
 stale='A named coefficient may belong with a coherent multivariate Hasse derivative package.\nThe derivative assessment supports a coherent upstream operator API; its supporting\nidentities still await their own assessments. This is not\na reason for a separate PR consisting only of this two-operation alias.'
 assert stale in parts[6]
 parts[6]=parts[6].replace(stale,'The Hasse coefficient and derivative belong with a coherent multivariate differential API; all supporting identities now have completed assessments. The per-declaration findings below identify existing evaluation/support primitives, substantive missing operator laws and optional upstream interface choices. A scalar construction alias alone does not replace this package. The Roth endpoints likewise form one theorem contribution with derived interfaces, rather than separate novel proofs.')
inv=(B/'FINAL_INVENTORY_PREVIEW.md').read_text();assert f'{n}/293'in inv;inv=inv[inv.index('## Roth'):]
inv=re.sub(r'^## (Roth[^\n]*)$',r'### \1',inv,flags=re.M)
inv=re.sub(r'^### ((?:theorem|lemma|def) )',r'#### \1',inv,flags=re.M)
inv=inv.replace('### File structural summary','#### File structural summary')
cross=(B/'FINAL_CROSS_FILE_PREVIEW.md').read_text();assert cross;cross=cross[cross.index('|'):].replace('; this preview records no final build or whole-review acceptance.', '.')
counts=collections.Counter(x['verdict']for x in rows);group=load('final-completed-yes-mathematical-groups-preparation.json');assert group['completed_count']==n and not group['unassigned_later_yes']
G='.mathlib-quality/overview/evidence/final'
L=['# Project overview: Roth','',('**COMPLETE — 'if complete else'**SCRATCH PREVIEW — ')+f'{n}/293 declaration assessments complete.**','', '## Executive summary','',
'Roth formalizes Roth’s theorem through characteristic-free Hasse derivatives, Wronskians, coefficient bounds, weighted indices, lattice counting, auxiliary polynomials and the final rational-approximation contradiction. This review assesses correctness of the retained interfaces and mathlib contribution potential; production Lean sources and pinned versions are unchanged.', '',
'Keep coherent differential and determinant APIs separate from scalar storage/construction aliases. The strongest upstream candidates are the multivariate Hasse operator and substantive laws, multivariate Taylor identities, coefficient estimates, determinant bounds, coefficient decomposition and arithmetic descent. A NO contribution verdict identifies existing API or a short composition; it does not by itself recommend deleting useful local notation.', '',
'Generality and representation changes require their exact verified bridges: characteristic-zero converse results retain their hypotheses; coefficient l1 size is distinct from a coefficient maximum; real-valued index and supremum definitions retain zero/default and mixed-zero-weight conventions. Generic construction primitives do not automatically replace a complete project theorem.', '',
'All applicable per-declaration reports, exact executed scratch sources, successful and rejected native receipts, searches, root acceptance and evidence manifests are retained. Private declarations use the explicit B1 prefilter with native/source/caller verification; their full public contribution searches are not claimed. Optional ask_chatgpt_math was unavailable, and local search-index failures are not absence evidence.', '',
'## Statistics','',f'- Production Lean source files:14; physical Lean lines:4874; canonical written declarations:293 (28 definitions,191 theorems,74 lemmas).',f'- Visibility:215 public,78 private. Completed assessments:{n}; unfinished:{293-n}.', '- Completed verdicts: '+', '.join(f'{v}:{c}'for v,c in sorted(counts.items()))+'.',f'- Source/pin preservation:17 hashes unchanged. Native whole293 direct graph:740 body and291 type references to canonical project declarations; cross-file279 body and110 type references across31 module pairs.',f'- Semantic comparisons among completed declarations:{P["pair_count"]}; all unique expected pairs present. '+('All42,778 project pairs covered.'if complete else'Unfinished declarations remain outside these judgments.'),'',
'## Part 1: Declaration inventory','',
'Full native types and source-faithful mathematical fields follow. Lexical references, native direct references and explanatory dependencies are separate scopes. Fourteen older kind-only type fields and fifteen mathematical-argument descriptions have separately preserved repair provenance; historical accepted packages remain immutable. Usage counts do not establish external or implicit simp/generated/transitive deadness.','',inv,'',
'## Part 2: Cross-file dependencies','',cross,'',
'## Cross-file interpretation','',
'Hasse/Taylor and coefficient-size API support determinant and index estimates. Wronskian independence feeds separation/Theta; lattice counting bounds the derivative constraints. MainLemma constructs bounded integer candidates, finds remainder collisions, subtracts a nonzero bounded difference, proves root vanishing and selects a nonvanishing derivative at a rational point. Main compares the resulting Taylor upper estimate to an integer-value lower estimate. LeanEval converts finite approximation exceptions into uniform positive constants. These are distinct mathematical stages, not duplicated versions of one theorem.','',parts[3],'',parts[4],'',
'### Complete semantic comparison evidence','',f'The [module-pair table index]({G}/pairwise/README.md) links every full comparison table and its adjacent source/report-hash evidence. All{P["pair_count"]} comparisons retain their full mathematical relationship and action. These are reviewed mathematical judgments, not machine proofs of inequivalence.','',parts[5],'',parts[6],'',parts[7],'',
'## Part 8: Mathlibable assessment','',
'Each non-prefiltered public declaration received the full applicable literature, generality, modern-idiom, infrastructure, five-method/form search, statement-shape, caller, composition and native verification workflow. The detailed report governs its exact evidence and caveats. BORDERLINE questions concern optional upstream API design, not incomplete verification.','',
'| # | Declaration | Verdict | Detailed report |','|---:|---|---|---|']
for x in rows:L.append(f'| {x["canonical_index"]} | `{x["declaration"]}` | {x["verdict"]} | [report]({x["report"]}) |')
L+=['','### Coherent contribution groups','']
for g in group['groups']:
 L+=['- **'+g['mathematical_group']+'**: '+', '.join('`'+x['declaration']+'`'for x in g['assessments'])+'.']
L+=['','## Recommended action plan','',
'1. Preserve current production behavior. For existing-API migrations, follow the report-specific caller and normalization plans rather than delete an entire NO bucket. Revalidate every downstream use before implementation.',
'2. Extract coherent Hasse/Taylor/coefficient/determinant/descent contributions in dependency order. Use each YES report’s exact target home, statement, grouping and reviewer evidence; do not infer approval for neighboring BORDERLINE wrappers.',
'3. Apply verified generalizations in a later implementation task with the exact original-specialization proofs retained. In particular, the selected-remainder collision theorem does not need finite support of the degree bounds; two proofs verify this. Its nonFinite finprod is a sufficient budget, not the cardinality of the infinite family. Monicity remains necessary for low-coefficient remainder reconstruction.',
'4. Retain the sharp B bound for subtraction of [0,B] coefficient families. Decide scalar/observation versus Hasse-specific API grain before upstreaming the local difference and root-vanishing helpers. Their broader scratch theorems are newly proved, not already existing mathlib APIs.',
'5. Preserve local proof boundaries and meaningful endpoint theorems even when direct internal consumer counts are zero. Private B1 status and absent direct consumers are not public novelty or external deadness judgments.','',
'## Verification scope','',
'The source/pin snapshot, exact293 native direct dependency graph, binder-type repairs, detailed accepted reports, all pairwise JSON/Markdown evidence and portable validation scripts are required supporting artifacts. Final completion additionally requires actual successful literal `lake build` and `lake build Roth.LeanEval` receipts; the default root does not import LeanEval. This renderer does not itself assert that those commands have run. The final readiness record and tracked final build evidence govern that gate.','',
'### Completed: `'+rows[-1]['declaration']+'`','',f'Latest completed assessment:{n}; [detailed report]('+rows[-1]['report']+'). All required per-declaration verification is independently accepted before publication.']
if complete:
 build=load('final-build-verification.json')
 assert build['command']==['lake','build']and build['exit_code']==0
 assert H(Path(build['log']))==build['log_sha256']
 other=build['lean_eval'];assert other['command']==['lake','build','Roth.LeanEval']and other['exit_code']==0
 assert H(Path(other['log']))==other['log_sha256']
 L+=['','Final literal build validation: **PASS** for `lake build` and **PASS** for `lake build Roth.LeanEval`. Exact command/exit/log hashes are retained in [final build verification]('+G+'/final-build-verification.json).']
else:L+=['','This is an untracked rendering preview. It does not accept unfinished declarations or final global readiness.']
out=B/('FINAL_PROJECT_OVERVIEW_CANDIDATE.md'if complete else'WHOLE_OVERVIEW_RENDERING_PREVIEW.md');out.write_text('\n'.join(L)+'\n');print('PASS scratch whole-overview rendering:',n,'assessments;',out.stat().st_size,'bytes; no tracked edits; final readiness separately gated')
