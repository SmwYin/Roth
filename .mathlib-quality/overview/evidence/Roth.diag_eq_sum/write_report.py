from pathlib import Path
import json,shutil,hashlib
D=Path(__file__).parent;R=Path('/Users/ramin/LEAN/Roth');N='Roth.diag_eq_sum'
def load(n):return json.loads((D/n).read_text())
def out(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def link(n,label=None):return f'[{label or n}](../evidence/{N}/{n})'
modern=[('Typeclasses','No new class; use existing CommSemiring R.'),('Filters/topology','n/a: finite algebraic identity.'),('Universal property','Already aeval; arbitrary valuation expansion is eval₂_eq. No new universal-property class.'),('Bundled substructures','n/a: no closure predicates; aeval is already an AlgHom.'),('Hierarchy weakening','Yes: integers expand to arbitrary CommSemiring coefficients; native generic compiled.'),('Higher categories','n/a: ordinary polynomial substitution has no higher coherence requirement.'),('Concrete index','σ is already arbitrary Type u; natural exponents define ordinary polynomials. General additive exponents change representation.'),('Concrete-via-abstract','Fires: after unfolding diag there is no integer-specific reasoning; generic CommSemiring proof compiled. Arbitrary valuation formula already exists as eval₂_eq.'),('False-generalization guard','CommSemiring preserves original substitution on specialization. Reject confusing substitution P(X,…,X) with power-series diagonal coefficient extraction or arbitrary images while retaining total-degree RHS.')]
strategy=[('Topology','n/a: no topology.'),('Algebra inclusions','No ideals/submodules appear; rewriting support expansion is appropriate.'),('Sequences','n/a: no limits.'),('Universal property','aeval already uses polynomial universal property; rebuilding it would duplicate infrastructure.'),('Missing helpers','No required mathematical helper missing: eval₂_eq plus product-power and monomial identities suffice. Optional named diagonal expansion remains API-design question.')]
infra=[(x,'n/a: theorem; introduces no data, instances or coercions.') for x in ['Typeclass diamond','Reducibility leak','Noncanonical unfolding','Instance priority','Universes','Coercion ambiguity']]
out('generality.json',dict(parameter_rows=[dict(parameter='σ : Type u',status='already arbitrary; no finiteness/nonempty/decidable instance assumed'),dict(parameter='P : MvPolynomial σ ℤ',status='P essential; coefficients can be CommSemiring R in expanded representation'),dict(parameter='diag : integer-polynomial interface',status='fixed parent interface; generic result stated with aeval, not a claimed local edit dropping a class')],expanded_forms=[dict(name='CommSemiring coefficient expansion',verified=True,status='PASS',source='native-raw-executed.lean.txt',receipt='native-raw-success.json')],modern_rows=[dict(question=q,analysis=a) for q,a in modern],strategy_rows=[dict(question=q,analysis=a) for q,a in strategy],infrastructure_rows=[dict(risk=q,analysis=a) for q,a in infra],verdict='STRICTLY NARROWER in coefficient representation; mechanical expanded statement verified; BORDERLINE trivial-simp API packaging'))
phases={k:'PASS' for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']};phases['4.5']='n/a: theorem; all six infrastructure rows documented'
out('assessment.json',dict(declaration=N,canonical_index=91,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=phases,unresolved=[],root_acceptance='pending',production_unchanged=True,reason='Phase6b trivial-simp composition; generic diagonal expansion API packaging needs upstream taste decision'))
t=load('native-type.json')['type']
questions=['Should mathlib expose the constant-X specialization of eval₂_eq as a named CommSemiring theorem with a monomial-sum RHS?', 'Should the canonical API use aeval directly, or a bundled map induced by total degree, with the diagonal expansion as its apply lemma?', 'For the two local callers, should this shared expansion remain a private/local helper if no upstream API is added?']
out('overview-entry.json',dict(declaration=N,kind='theorem',type=t,what='Diagonal substitution sends each coefficient monomial to a univariate monomial at total degree.',how='Unfold diag/aeval, use eval₂_eq, collapse product of powers, identify total exponent and polynomial monomial.',hypotheses='Arbitrary variable type σ and integer polynomial P; no finiteness, degree, or nonzero hypotheses.',project_dependencies=['Roth.diag'],caller_summary='Two explicit same-file callers: abs_coeff_diag_le at176 and natDegree_diag_le at185; zero external-to-file. Canonical293 direct proof audit agrees.',mathlib_api_audit='eval₂_eq plus aeval_def, prod_pow_eq_pow_sum, degree_apply, algebraMap_eq, C_mul_X_pow_eq_monomial compile generically. No exact diagonal theorem established; local index unavailable.',moral_duplications='Elementary specialization and normalization of existing evaluation expansion; genuine product-power/monomial bridge prevents claiming definitional exact duplicate.',generalization='Verified CommSemiring R coefficient expansion with aeval; no need finite σ. Current diag remains fixed at ℤ.',missing_api='Optional named constant-X evaluation expansion, contingent on upstream API design; no mathematical proof infrastructure gap.',junk='Not dead: two direct callers use the common expansion.',action='BORDERLINE: retain production unchanged; resolve the three concrete upstream API questions before proposing a lemma or inlining.'))
# Exact pinned sources for each normalization fact, including degree definition.
f=R/'.lake/packages/mathlib/Mathlib/Data/Finsupp/Weight.lean';shutil.copyfile(f,D/'mathlib-source-weight.lean.txt');m=load('mathlib-inputs.json');m.append(dict(path=str(f.relative_to(R)),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),bytes=f.stat().st_size,archive='mathlib-source-weight.lean.txt'));out('mathlib-inputs.json',m)
rows=[]
for i in range(19):
 w=load(f'web-{i}.json');qs=w['request'].get('search_query',[])
 for q in qs:rows.append(f'| {i} | `{q["q"]}` | {w["summary"]} {link(f"web-{i}.json","receipt")} |')
formal=[]
for method in ['lean_leanfinder','lean_loogle','lean_leansearch','lean_local_search']:
 fs=[]
 for form in ['current','standard','abstract']:
  x=load(method+'-'+form+'.json');r=x['response'].get('structuredContent',{});its=r.get('items',[]);names=[z.get('name',z.get('formal_name','')) for z in its]
  fs.append(form+': '+(', '.join(names[:4]) or ('index unavailable' if r.get('index')=='unavailable' else 'no items'))+' '+link(method+'-'+form+'.json','raw'))
 formal.append('| '+method+' | '+'; '.join(fs)+' |')
report=f'''# `{N}` — declaration 91/293

**BORDERLINE-needs-human.** The expansion is a verified trivial-simp specialization of evaluation. Its reusable API value, after generalizing coefficients, needs an upstream packaging decision. This is a completed read-only assessment; verification unresolved list is empty. Production, pins, Git and progress are unchanged; root acceptance is pending.

## Phase 0 — baseline

Freshly matched all17 source/pin hashes against the shared successful `lake build` baseline (2467 jobs, exit0). Target resolves at `Roth/CoeffNorm.lean:164`; theorem without placeholders. Full declaring module and both callers were read. {link('input-hash-check.json')} {link('inputs.json')} {link('baseline-build.txt')} {link('source-module.lean.txt')}

## Phase 1 — comprehend

For a polynomial P in any variable set with integer coefficients, identifying all variables with X sends the term aₖXᵏ to aₖX^|k|. Summing these terms gives the univariate polynomial; distinct exponents with equal total degree may merge. No assumption that coefficients avoid cancellation is made.

Full native type (pretty-printer resolves `monomial` in `Polynomial`):

```lean
{t}
```

Parameters are σ (arbitrary universe-polymorphic variable type) and P (essential input). There are no instance hypotheses on σ and no degree, nonzero or finiteness hypotheses. Proof unfolds `diag`, then `aeval`, invokes support expansion `eval₂_eq`, and normalizes the constant-X product into the monomial of total degree. The only project dependency is `Roth.diag`. {link('native-type.json')} {link('native-original-executed.lean.txt')} {link('native-original-success.json')}

## Phase 2 — preliminary classification

SMALL: helper expansion, no new structure, named classical theorem or project main result. One-line definition test n/a: theorem. Its shared name has actual API value for two same-file callers, but theorem length itself is not a verdict factor.

## Phase 3 — exhaustive literature

Three distinct general queries and every named channel ran. ChatGPT math channel is n/a: `ask_chatgpt_math` unavailable. Local clean.tex lines1444–1461 explicitly discuss replacing all xᵢ by x and bounding merged coefficients; that is the downstream mathematical purpose. {link('local-literature.txt')} {link('local-literature-source.json')}

| Receipt | Exact query | Result / interpretation |
|---|---|---|
'''+ '\n'.join(rows)+f'''

Primary context: [nLab polynomial](https://ncatlab.org/nlab/show/polynomial) search identifies the free-algebra viewpoint (direct open failed due to unsupported XHTML); [Thiel's commutative-algebra notes](https://ulthiel.com/math/files/Commutative-Algebra.pdf) were returned for the polynomial universal property (direct fetch timed out). [Jiang, arXiv2609.10609](https://arxiv.org/abs/2609.10609), submitted2026-09-08, uses diagonal specialization in a recent application; its abstract confirms terminology rather than proving our formula. Stacks00EX was accessible but concerns spectra examples, so is not claimed as the universal-property proof. Exact multi-page open request/failures: {link('web-18.json')}.

The standard mathematical content is ordinary polynomial evaluation and its monomial expansion, with diagonal specialization as the constant valuation. Coefficient bases range from integers in the Roth application to commutative rings/semirings in universal-property formulations. The universal-property abstraction is already `aeval`/`eval₂`; recent applications do not require a new definition. Power-series coefficient-extraction “diagonal” and quadratic diagonal forms are different concepts and excluded. Search results do not prove absence of an upstream theorem. Web records store hashes/bytes, exact requests, titles/locators and original summaries only; all URL queries and oversized returned headings are omitted.

## Phase 4a — parameters and hypotheses

| Parameter | Generality / audit |
|---|---|
| σ : Type u | Already arbitrary, including empty/infinite types; finite supports suffice. No Fintype/DecidableEq parameter to drop. |
| P : MvPolynomial σ ℤ | Essential polynomial argument; ℤ coefficients can expand to arbitrary CommSemiring R. |
| diag | Existing parent signature fixes ℤ; generic claim is stated against aeval, not falsely described as dropping a target hypothesis. |
| Natural exponents / degree | Define ordinary polynomials and total degree; arbitrary additive exponents would change representation and need a separate monoid-algebra API. |

## Phase 4b — verified generality

STRICTLY NARROWER in coefficient representation: both `generic` and `existingExpansion` compiled in isolated mathlib-only code under `[CommSemiring R]`, with arbitrary σ. Generalized signature:

```lean
{{σ R : Type*}} [CommSemiring R] (P : MvPolynomial σ R) :
  MvPolynomial.aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P =
    ∑ k ∈ P.support, Polynomial.monomial k.degree (P.coeff k)
```

This is a mechanical expanded representation (CHEAP sequencing observation, never a verdict reason). No ring subtraction, field, characteristic, order, nontriviality or finite variable assumption is used. Generalized proof and specialization route: {link('native-raw-executed.lean.txt')} {link('native-raw-success.json')}. Arbitrary coefficient homomorphisms/valuations are already covered by `eval₂_eq` (verified native signature); retaining the monomial-degree RHS requires the constant-X valuation.

## Phase 4c — all nine modern-idiom rows

| Question | Assessment / concrete downstream consequences |
|---|---|
'''+ '\n'.join('| '+q+' | '+a+' |' for q,a in modern)+f'''

Concrete downstream benefit of CommSemiring coefficients: the same monomial expansion applies to ℕ, finite-characteristic coefficients and arbitrary commutative semirings, while both existing integer coefficient/degree estimates remain rewrites by specialization. A bundled total-degree map is a possible alternative representation, not a new verified existing replacement. No higher-level packaging is required to prove the formula. {link('generality.json')}

## Phase 4.5 — all six infrastructure risks

'''+ '\n'.join('- '+q+': '+a for q,a in infra)+'''

## Phase 4.6 — all five proof-strategy rows

| Question | Assessment |
|---|---|
'''+ '\n'.join('| '+q+' | '+a+' |' for q,a in strategy)+f'''

Verdict: current finite-support normalization is idiomatic. Avoid induction over P or rebuilding a polynomial homomorphism. Optional naming is the issue, not unavailable proof infrastructure.

## Phase 5 — five actual mathlib methods on three forms

| Method | Actual results |
|---|---|
'''+ '\n'.join(formal)+f'''
| rg source | Current diagonal/monomial form, standard eval/product-power form, and abstract mapDomain/lift form: {link('rg-current.json')}, {link('rg-literature.json')}, {link('rg-abstract.json')}. Full-name search: {link('rg-full-name.json')}. |

External indices may differ from pinned revision; local unavailable index is not absence evidence. Positive pinned evidence is `MvPolynomial.eval₂_eq` and the normalization facts, all signatures checked natively and used in the isolated proof. Conclusion: found evaluation building blocks, not an established exact diagonal expansion theorem. This report makes no exhaustive-absence claim.

| Existing fact | Pinned path / role |
|---|---|
| MvPolynomial.eval₂_eq | Mathlib/Algebra/MvPolynomial/Eval.lean:72; rfl support expansion. |
| MvPolynomial.aeval_def | Same module; converts aeval to eval₂; needed explicitly by successful simpa. |
| Finset.prod_pow_eq_pow_sum | Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:656; genuine power-product identity. |
| Finsupp.degree_apply | Mathlib/Data/Finsupp/Weight.lean:221; rfl exponent-sum notation. |
| Polynomial.algebraMap_eq | Mathlib/Algebra/Polynomial/AlgebraMap.lean:90; rfl canonical C map. |
| Polynomial.C_mul_X_pow_eq_monomial | Mathlib/Algebra/Polynomial/Basic.lean:658; genuine monomial identification. |

Pinned source archives/hashes: {link('mathlib-inputs.json')}; exact native signatures and proof: {link('native-raw-success.json')}. New assessment helpers are not counted as pre-existing mathlib calls.

## Phase 5.5 — statement shape

Normal forms: support sum of `Polynomial.monomial k.degree`, or support sum of `C a * X^(sum exponents)`. Existing eval₂_eq supplies the latter with a product before normalization. Monomial RHS is directly usable for coefficient and degree APIs; orientation RHS-expanded is appropriate. Syntactic alternatives actually attempted: raw aeval expansion and specialization of existing eval₂_eq via explicit `simpa only`; both now compile. P explicit is convenient for rewrites. No superfluous variables/typeclasses; σ is inferred from P and supports arbitrary universes. Overall RESTATE-BEFORE-SHIP if upstream: CommSemiring coefficients and aeval-based signature. Local fixed-parent statement is usable as written.

## Phase 6.0 — complete callers and inline audit

Internal use count excluding declaring file:0; external-to-file callers:0. Explicit same-file calls:2 (not conflated with the first count).

| Caller | Usage | Concrete refactor experiment |
|---|---|---|
| Roth.abs_coeff_diag_le, CoeffNorm.lean:176 | `rw [diag_eq_sum, Polynomial.finsetSum_coeff, …]` | Replace first rewrite by generic existingExpansion specialized to ℤ; full theorem replay compiled. |
| Roth.natDegree_diag_le, CoeffNorm.lean:185 | `rw [diag_eq_sum]` | Same specialized expansion, retain degree-of-sum proof; full theorem replay compiled. |

No equivalent diagonal expansion is re-derived inline elsewhere. Other eval₂ expansions and product-power rewrites concern other evaluations; no extra target caller inferred. {link('rg-callers.json')} {link('rg-inline.json')} {link('callers.json')}.

Fresh audit of the canonical array generated directly from tracked JSON preserves private names and exact order: requested293, unique293, present293, values293; direct proof consumers exactly the two rows above. This is not a transitive kernel/simp dependency closure. {link('canonical-audit-array.lean.txt')} {link('canonical-order.json')} {link('native-consumers-executed.lean.txt')} {link('native-consumers-success.json')}.

## Phase 6 — actual compositions and gate semantics

Attempt1: specialize `eval₂_eq` and normalize via product-power, degree, canonical coefficient map and monomial identity. The first attempted `simpa only` omitted aeval_def and failed (preserved rejected receipt); corrected proof succeeded. Attempt2: source-style `rw [aeval_def, eval₂_eq]; simp_rw […]` under CommSemiring succeeds independently. Both exact snippets are in raw accepted evidence.

There are six named existing facts in the explicit proof, not one existing diagonal lemma. Three (`eval₂_eq`, `aeval_def`, `degree_apply`) plus canonical coefficient-map normalization are definitional bridges; `prod_pow_eq_pow_sum` and `C_mul_X_pow_eq_monomial` are genuine identities. Even viewing those three core mathematical ingredients as a count of3 does not turn their nested sum-congruence normalization into a simple chained-call term. No compiled <=3 existing-call term was established. The named helper used by caller replays is newly proved evidence, not an existing replacement.

Composition classification: **trivial simp composition; Phase6b BORDERLINE**. The explicit command says a closing `simp [facts]` is borderline and the API value must be judged; `simpa only` over eval₂_eq has precisely that normalization character. NO-has-it would overstate exact specialization without the genuine product/monomial bridge. YES solely from syntactic normalization length would overstate the mathematical gap. Parent diag is NO-composable; the special ModeB re-aim gate for a NO-has-it parent therefore does not apply automatically. This assessment is independent of parent and sibling verdicts.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, grounded in the explicit trivial-simp gate, not proof cost or unverified absence. A shared generic support-expansion theorem may be useful, but all mathematical infrastructure exists and the two consumers are local. Concrete upstream API questions:

'''+ '\n'.join(f'{i+1}. {q}' for i,q in enumerate(questions))+f'''

If a named API is selected, propose the CommSemiring/aeval statement near Mathlib/Algebra/MvPolynomial/Eval.lean after coefficient-polynomial imports are reviewed; do not upstream the integer-only Roth spelling. If omitted upstream, keep a private shared helper in Roth/CoeffNorm.lean or inline the exact verified normalization at both listed callers. Neither change is authorized by this read-only assessment. Existing accepted YES groupings were freshly read, but no PR grouping/reviewer selection is applicable to this BORDERLINE verdict. {link('accepted-yes-grouping.json')}

## Phase 8 — verification and handoff

Three accepted exact native source/receipt sets: original target/type/axioms, isolated generic composition, full caller replays/canonical audit. All success=true, no errors/warnings; disk responses explicitly partial=false, completed virtual response has no partial flag; axioms only propext, Classical.choice, Quot.sound. Two rejected attempts are separately archived: first missing aeval_def type mismatch, second corrected proof with longLine warning. Neither is counted as success. {link('verification.json')}

Portable read-only validation checks current copy-manifest hashes/bytes (historical worker manifest never substitutes), sources/pins, native receipts and exact archived sources, all mandatory phases and searches, canonical293 exact name order/private handling, links and credential guard. {link('validate.py')}. Root independently reviews before integrating. No user question or production edit is required to complete this assessment.
'''
(D/'report.md').write_text(report)
