"""Render source/import and exact direct native graph data, never assessment completion."""
from pathlib import Path
import json,hashlib
B=Path('/private/tmp/roth-overview');R=Path('/Users/ramin/LEAN/Roth')
read=lambda p:json.loads(p.read_text())
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
I=read(B/'final-completed-inventory-preparation.json');S=read(B/'final-source-statistics-and-imports-preparation.json');G=read(B/'final-cross-file-graph-summary.json')
base=read(R/'.mathlib-quality/overview/evidence/shared/input-manifest.json')['sources_and_pins']
for n,x in base.items():assert H(R/n)==x['sha256']
assert len(base)==17 and S['total_files']==len(S['rows'])==14
for x in S['rows']:assert H(R/x['file'])==x['sha256']
assert sum(x['physical_lines']for x in S['rows'])==S['physical_lines']==4874
order=read(R/'.mathlib-quality/overview/declaration-order.json');files={x['file']for x in S['rows']};assert len(order)==S['canonical_written_declarations']==293
L=['# Cross-file rendering preparation','',f"Scratch only. {I['completed_count']}/293 assessments accepted; source/import and native direct graph data cover all293 declarations. Graph coverage is not unfinished-assessment acceptance.",'',f"Production:14 Lean files,4874 physical lines,293 canonical written declarations. All17 sources/version pins match the read-only review baseline.",'','## Direct project imports','','Arrows run from imported module to importer. This is source import structure, not semantic dependence.','','```mermaid',(B/'final-direct-imports.mmd').read_text().rstrip(),'```','','## Direct cross-file expression references','','The exact canonical native graph counts references in values and types separately, with original opaque theorem values inspected directly. It does not expand imported auxiliary proofs or compute simp/generated/opaque/transitive closure. A zero count is not external deadness.','', '| Caller file | Referenced file | Direct body edges | Direct type edges |','|---|---|---:|---:|']
counts={}
for kind in ['body','type']:
 for x in G['module_edges'][kind]:
  a,b=x['caller_file'],x['callee_file'];assert a in files and b in files
  if a==b:continue
  counts.setdefault((a,b),{'body':0,'type':0})[kind]=x['direct_edges']
assert sum(x['body']for x in counts.values())==G['cross_file_body_edges']==279
assert sum(x['type']for x in counts.values())==G['cross_file_type_edges']==110
for (a,b),x in sorted(counts.items()):L.append(f"| `{a}` | `{b}` | {x['body']} | {x['type']} |")
L += ['','The main chain is Hasse/Taylor and coefficient estimates → Wronskian/separation and index/lattice estimates → Theta bound → auxiliary polynomial main lemma → Roth contradiction → LeanEval formulation. Source-import and canonical direct-expression graphs describe different layers.','', 'The default Roth library target does not import Roth.LeanEval. Final validation must run both `lake build` and `lake build Roth.LeanEval`; this preview records no final build or whole-review acceptance.','']
(B/'FINAL_CROSS_FILE_PREVIEW.md').write_text('\n'.join(L))
print(f"PASS scratch cross-file preview:{len(counts)} module pairs,279 body/110 type references,17 fresh hashes; no tracked changes.")
