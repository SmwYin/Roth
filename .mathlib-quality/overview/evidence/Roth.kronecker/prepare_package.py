from pathlib import Path
import json,hashlib,shutil
D=Path(__file__).resolve().parent; N='Roth.kronecker';T=D.parent.parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']}
dump('assessment.json',dict(declaration=N,canonical_index=102,verdict='NO-mathlib-has-it',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,reason='Exact existing MvPolynomial.aeval specialization rfl; CommSemiring arbitrary weights verified; complete inline caller proof migration. Semantic exemption acknowledged without assuming novelty.'))
dump('overview-entry.json',dict(declaration=N,kind='def',type='∀ {K : Type u_1} [Field K] {σ : Type u_2} [Fintype σ], ℕ → MvPolynomial σ K →ₐ[K] Polynomial K',what='Chosen-enumeration Kronecker power substitution from multivariate to univariate polynomials.',how='Existing MvPolynomial.aeval with generator j mapped to Polynomial.X ^ k ^ rank(j).',hypotheses=['Field K, definition weakens to CommSemiring','Fintype σ supplies chosen enumeration; explicit weights require no finite variable type','k arbitrary natural; no degree/injectivity/characteristic hypotheses'],project_dependencies=[],caller_summary='9 explicit same-module callers;17 identifier occurrences on15 lines; zero external-to-file callers. Full declaring-module proof replay inlines existing aeval and removes the definition. Canonical293 ordered audit independently records constant consumers.',mathlib_api_audit='Exact positive existing MvPolynomial.aeval; aeval_monomial and eval₂Hom native checked; unrelated Matrix.kronecker, expand, bind₁ and finSuccEquiv not mistaken for target.',moral_duplications='Literal one-call specialization of existing universal evaluation, with legitimate local semantic naming exemption.',generalization='CommSemiring coefficients and arbitrary explicit ranks/weights verified; existing aeval is already more general. Hidden enumeration is noncanonical and changes the substitution.',missing_api='No missing API for the definition itself; bounded encoding/injectivity and derivative results assessed separately.',junk='Useful local semantic API, not dead code. No new typeclass/coercion instance.',action='NO-mathlib-has-it. Inline existing aeval at all9 named callers per tested migration, or retain a documented local/private helper in Roth/GenWronskian.lean; do not propose this wrapper alone upstream.'))
# verification.json is finalized against the actual accepted native receipt list.
files=[]
for p in sorted(D.iterdir()):
 if not p.is_file() or p.name in ['copy-manifest.json','worker-copy-manifest.json','root-acceptance.json']:continue
 dest=f'.mathlib-quality/overview/mathlibable/{N}.md' if p.name=='report.md' else f'.mathlib-quality/overview/evidence/{N}/{p.name}'
 files.append(dict(source=str(p),destination=dest,sha256=sha(p),bytes=p.stat().st_size))
dump('copy-manifest.json',dict(declaration=N,files=files))
