from pathlib import Path
import json,hashlib,re,subprocess
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.eta_lt_gam_iff'
def rd(n):return json.loads((D/n).read_text())
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def native(n):
 z=rd(n)['result']['structuredContent'];return z.get('result',z)
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
questions=[
 'When a Roth parameter API is proposed upstream, should this named equivalence stay beside eta/gam as a stable semantic bridge to the source equation (38)?',
 'Should an upstream parameter API expose gamma as m/2 minus the error term, making this law a direct lt_sub_iff_add_lt specialization?',
 'Does the general scalar law a + b < c/d ↔ a < (c-d*b)/d merit a separate upstream name despite its verified three-existing-lemma term?']
put('assessment.json',dict(declaration=N,canonical_index=235,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=dict.fromkeys(ph,'PASS'),justified_na={'2b':'theorem, not a definition','4.5':'all six infrastructure risks n/a for a theorem','ask_chatgpt_math':'unavailable'},unresolved=[],root_acceptance='pending',questions=questions))
typ=rd('native-type.json')['type'];accepted=[]
for label,fmt,required in [('original','disk',['GAP235_FULL_TYPE:','GAP235_AUDIT: requested=293; unique=293','GAP235_AUDIT_PRESENT: present=293; values=293']),('isolated','raw',["'Gap235Isolated.three_term' depends on axioms:","'Gap235Isolated.generic' depends on axioms:","'Gap235Isolated.expanded' depends on axioms:","'Gap235Isolated.false_coefficient' depends on axioms:"]),('inline','disk',['GAP235_INLINE: two actual caller proofs; original signatures retained']),('project','disk',['GAP235_PROJECT: arbitrary eta, normalization bridge, explicit existing law verified','GAP235_PROJECT_BODY_EDGE: Roth.eta_lt_gam_iff -> [Roth.eta_lt_gam_iff._proof_1_3]'])]:
 source=label+'-executed.lean.txt';receipt=label+'-receipt.json'
 accepted.append(dict(label=label,format=fmt,source=source,source_sha256=sha(D/source),receipt=receipt,original_execution_request=rd(receipt)['request'],native_region_start_line=19 if fmt=='raw'else 15,required_info=required))
ds=native('original-receipt.json')['items'];cons=[d['message'].split(': ',1)[1]for d in ds if d['message'].startswith('GAP235_DIRECT_CONSUMER: ')];types=[d['message'].split(': ',1)[1]for d in ds if d['message'].startswith('GAP235_DIRECT_TYPE_CONSUMER: ')]
put('verification.json',dict(declaration=N,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=[dict(source='isolated-rejected-executed.lean.txt',receipt='isolated-rejected-receipt.json',reason='Initial equality-substitution motive and rewrite orientation were wrong; numeric counterexample had unintended Nat divisions. Recovered sorryAx is rejected.'),dict(source='isolated-rejected2-executed.lean.txt',receipt='isolated-rejected2-receipt.json',reason='Successful compilation had two tactic-linter warnings; replaced by clean generic proof, not accepted.')],warming=[dict(source='original-executed.lean.txt',receipt='original-warming-receipt.json')],audit=dict(source='original-executed.lean.txt',receipt='original-receipt.json',requested=293,unique=293,present=293,values=293),canonical_direct_consumers=cons,canonical_direct_type_consumers=types,composition=dict(strict_three_existing_call_term_normalized_verified=True,strict_three_existing_call_term_original_verified=False,new_generic_is_existing_mathlib=False,exact_expanded_original_verified=True,normalization_bridge_new_proof=True,actual_caller_replays=2,original_signatures_retained_by_defeq=True,imported_transitive_target_freedom_claimed=False)))
put('overview-entry.json',dict(type=typ,kind='theorem',what='The numerical small-delta inequality (30) is equivalent to eta being smaller than gamma.',how='Unfold gamma and lambda, distribute division over subtraction, and collect the scalar factor: half of the lambda term is the error term in (30).',hypotheses='No sign, nonzero-dimension, or degree assumptions: delta is any real and n,m are arbitrary naturals.',project_dependencies=['Roth.gam','Roth.lam'],caller_summary='Unused in MainLemma; two body occurrences in Main.exists_delta (241) and Main.roth_of_isIntegral (560); both full proofs replayed with inline arithmetic and original signatures.',mathlib_api_audit='lt_sub_iff_add_lt is the canonical additive order law. sub_div/div_sub_div_same and mul_div_cancel_left₀ give the normalized scalar version; the exact old spelling also needs coefficient and association normalization.',moral_duplications='The exact eta formula has no role in the equivalence. Morally a translated strict inequality; exists_delta_bound supplies a substantive numerical bound rather than this equivalence.',generalization='Verified arbitrary e:ℝ in place of eta and arbitrary a,b,c in a Field K with LinearOrder K and IsStrictOrderedRing K: a + 2*b < c/2 ↔ a < (c-4*b)/2. This is a new generic proof, not an existing mathlib declaration; the underlying additive law already holds for AddGroup G, LT G, AddRightStrictMono G.',missing_api='No established mathematical gap; upstream naming of the normalized scalar identity or a future Roth parameter API remains a design question.',junk='Not dead: two critical proof consumers. Full caller inlining works, but removing the stable named bridge is a local API decision.',action='BORDERLINE-needs-human: retain locally in Roth/MainLemma.lean pending future parameter-API design; use the three concrete upstream questions in the report. No production edits proposed or performed by this assessment.'))
put('concrete-diagnostic.json',dict(source_body='grind [gam, lam]',named_identifier_counts={'eta':0,'gam':1,'lam':1},fires=True,verification=['Gap235Project.arbitrary_eta','Gap235Isolated.generic','Gap235Isolated.expanded'],false_generalization_guard='Abstract the scalar values while retaining the coefficient relation; do not treat Dedekind eta, Euler gamma or additive-combinatorial Roth numbers as these parameters. false_coefficient gives a certified counterexample to dropping the coefficient relation.'))
put('scope-audit.json',dict(source_body=['Roth.gam','Roth.lam'],source_type=['Roth.eta','Roth.gam'],kernel_direct_body=['Roth.eta_lt_gam_iff._proof_1_3'],kernel_canonical_direct_body_consumers=cons,kernel_canonical_direct_type_consumers=types,project_outgoing_body_closure='project-receipt.json',simp='No simp attribute on target; no claim about arbitrary tactic search or unenumerated generated constants.',transitive='Canonical audit checks direct edges only. Original project imports remain loaded; caller replay removes lexical and direct body uses, without claiming no transitive imported dependency.'))
commands=[]
for args in [['python3','/private/tmp/roth-overview/check_audit_source.py',str(D/'original-executed.lean.txt')]]:
 z=subprocess.run(args,text=True,capture_output=True);assert z.returncode==0;commands.append(dict(command=args,exit_code=z.returncode,stdout=z.stdout,stderr=z.stderr,scope='Read-only recheck; identical gate passed before first original native execution.'))
put('preparation-checks.json',dict(commands=commands,observed_pre_execution=[dict(script=p,exit_code=0,exact_source=s,width_guard='PASS <=100',source_read_before_native=True)for p,s in [('prepare.py','original-executed.lean.txt'),('prepare_probes.py','isolated-executed.lean.txt'),('prepare_inline.py','inline-executed.lean.txt'),('prepare_project.py','project-executed.lean.txt')]],rejected_preparations='Every failed native attempt is separately archived; no failed preparation was followed by querying a stale file.'))
L=lambda n:'../evidence/'+N+'/'+n
report=f'''# `{N}` — canonical235

**BORDERLINE-needs-human.** The exact named bridge has two real consumers and records the paper's equation (38). Its mathematical core is existing additive-order API; the precise 2/4 coefficient spelling also needs arithmetic normalization. All assessment phases and native verification are complete; the three future upstream-design questions below do not block this read-only assessment. Production Lean, pins, nine disk imports, shared18 and Git were not changed.

## Phase 0 — baseline

The fresh [17-input comparison]({L('inputs.json')}) matches the tracked [baseline manifest]({L('input-manifest.json')}) exactly. The reusable [baseline build]({L('baseline-build.txt')}) completed all 2467 jobs without warnings/errors. Target resolves at MainLemma:100–102, theorem, no sorry. The whole MainLemma develops Roth's Lemma 9 via a polynomial pigeonhole construction and derivative extraction; this target only translates its parameter condition. The original complete module was replayed under `Gap235Original`, target alone renamed `replay`.

[Exact original execution]({L('original-executed.lean.txt')}), [complete native receipt]({L('original-receipt.json')}), [canonical order]({L('canonical-snapshot.json')}), [preparation checks]({L('preparation-checks.json')}). No file-end build is due at235 (last accepted boundary228, next266).

## Phase 1 — comprehend

For any real δ and naturals n,m, let λ=4(1+3δ)n√m, γ=(m−λ)/2 and η=10^m δ^((1/2)^m). Then η+2(1+3δ)n√m<m/2 exactly when η<γ. Dividing λ by two gives the error term; translation of a strict inequality supplies the equivalence. No property of the real-power expression defining η is used.

Full native kernel type (obtained with `Lean.getConstInfo` and `pp.funBinderTypes`, not by splitting a printer message at `:=`):

```lean
{typ}
```

Parameters: δ is a scalar perturbation; n a polynomial-degree parameter; m a dimension. No hypotheses besides their types. Source proof uses `gam` and `lam`; `eta` is in the statement. Direct kernel body uses the generated `Roth.eta_lt_gam_iff._proof_1_3`; this differs from source lexical dependencies. The [full target printer]({L('original-receipt.json')}) has no printer-elision marker and prints that wrapper, not expanded generated `grind` internals. The separate [project body-edge traversal]({L('project-receipt.json')}) follows Roth-prefixed body edges and shows eta/gam/lam and their generated helpers. It is not a traversal of all imported mathlib constants.

## Phase 2 — preliminary checks

SMALL: a parameter-conversion helper, neither a named theorem nor a module main result nor a new structure. Phase2b definition-only one-line test: n/a, theorem. A one-line tactic proof is not itself a NO criterion. Semantic naming is nevertheless concretely useful: exists_delta uses the bridge to prove a denominator nonzero for continuity, and roth_of_isIntegral uses it to clear the positive denominator in the final contradiction. This supports a project-local API name, not by itself a general upstream API.

## Phase 3 — exhaustive literature

Every named channel was actually checked; exact requests, response SHA256/byte counts/status, clean titles and URLs, and original summaries are preserved. Full web bodies are not archived. The original local paper is the exact source; supplementary web sources only establish context/abstraction.

| Channel | Exact query / locator | Finding |
|---|---|---|
| General specific | `Roth theorem "Inequality" "eta" "gamma" main lemma parameters` | Broad Roth and unrelated eta/gamma results; no exact equivalence. |
| General abstract | `ordered field addition subtraction division strict inequality equivalence` | Ordered-field arithmetic; primary university course notes give translation and positive scaling. |
| General alias/source | `Roth lemma 9 lambda gamma eta parameter inequality 30 38` | No exact named independent scalar theorem. |
| Local reference | clean.tex §6, eqs.(30),(34)–(36),(38), lines1334–1359 | Exact parameter definitions and equivalence; [local excerpt]({L('local-excerpt.tex.txt')}). |
| ChatGPT math | unavailable | Optional `ask_chatgpt_math` tool absent. |
| nLab | `site:ncatlab.org/nlab ordered field addition inequality` | [Ordered field](https://ncatlab.org/nlab/show/ordered%2Bfield), Definition; compatible strict order is the abstract setting. |
| nCatLab distinct | `site:ncatlab.org/ncatlab ordered field order translation` | Returned /nlab pages, no in-namespace result; no categorical upgrade established. |
| Stacks | `site:stacks.math.columbia.edu ordered field inequality` | Field/valuation material, e.g. [Examples of fields,09FF](https://stacks.math.columbia.edu/tag/09FF); no Roth scalar bridge. |
| MathOverflow | `site:mathoverflow.net Roth theorem parameters main lemma` | [Optimal Roth-type result](https://mathoverflow.net/questions/332190/optimal-roth-type-result-in-diophantine-approximation), effectiveness discussion; no competing scalar law. |
| Recent arXiv | `site:arxiv.org Roth theorem formalizing after:2021-10-28 before:2026-10-29` | [2207.07499](https://arxiv.org/abs/2207.07499) concerns the different arithmetic-progression Roth theorem. |
| Refined recent arXiv and primary access | `site:arxiv.org "Roth" "Diophantine" "formalization" after:2021-10-28 before:2026-10-29` | No results; opening [Penn notes](https://www2.math.upenn.edu/~gressman/analysis/01-orderedfields.html) returned403; only initial indexed excerpts available. |

Receipts: [general]({L('web-general.json')}), [nLab]({L('nlab.json')}), [nCatLab]({L('ncatlab.json')}), [Stacks]({L('stacks.json')}), [MO]({L('mathoverflow.json')}), [arXiv]({L('arxiv.json')}), [refinement/access failure]({L('primary.json')}), [local search]({L('local-literature.json')}). No malformed site query was used. Query noise and access failure do not establish absence. The exact local formulation is a paper-specific parameter bridge; the standard general mathematics is translation invariance of strict order in an additive group and distributivity of division over subtraction. No historical evolution of this elementary law was established by the search.

## Phase 4a — generality dimensions

| Parameter / feature | Current | Verified broader form / constraint |
|---|---|---|
| δ | arbitrary ℝ, no sign condition | η can be independent e; no δ-positivity needed. |
| n | ℕ degree parameter | Abstract scalar error b in the field law. Dropping n from the unchanged concrete signature is meaningless: it occurs in γ/error. |
| m | ℕ dimension | Arbitrary scalar c in the field law; no m>0 required for original equivalence. |
| eta formula | fixed real power, constants10 and1/2 | `arbitrary_eta` replaces it by any e:ℝ; its constants play no role. |
| sqrt and natural coercions | fixed concrete representation | Treat `(1+3δ)n√m` as b; no analytic theorem or completeness needed. |
| constants2,4 | linked by division by2 | Cannot vary independently; certified `false_coefficient` counterexample. |
| ℝ | concrete scalar field | `Field K`, `LinearOrder K`, `IsStrictOrderedRing K` generic proof compiles. |
| order hypotheses | none explicit | Underlying translation requires only `AddGroup G`, `LT G`, `AddRightStrictMono G`. |
| strict conclusion | both sides strict | Weak analogue independently verified, but replacing only one side loses equivalence; keep strict original semantics. |
| universes / unused binders | concrete types | Abstract G/K universe-polymorphic; no unused explicit arguments/classes in original. |

## Phase 4b — verified generality

The scalar mathematical relation is STRICTLY NARROWER than its abstract form. This is not a claim that `gam` or real `sqrt` can be kept unchanged over an arbitrary field: those concrete definitions fix the original interface. The genuinely verified generic statement is:

```lean
theorem generic {{K : Type*}} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (a b c : K) : a + 2 * b < c / 2 ↔ a < (c - 4 * b) / 2
```

[Exact isolated source]({L('isolated-executed.lean.txt')}) and [clean receipt]({L('isolated-receipt.json')}) verify it, the fully expanded original, the weak analogue and a coefficient counterexample with no project imports. `#check_failure` guards eta/gam/lam/target. [Project probes]({L('project-executed.lean.txt')}) verify arbitrary eta and the concrete normalization bridge. These are **new proofs**, not existing mathlib building blocks and not new axioms. Restating at this level is mechanically verified; cost is not a verdict reason. Existing additive API already provides the broader mathematical law after normalization.

## Phase 4c — modern idiom

| # | Check | Applies / concrete consequence |
|---|---|---|
| 1 | Typeclasses | Yes for abstract scalar law; field/order hierarchy removes concrete ℝ dependence and permits ℚ or any ordered field. Original parameter definitions stay real. |
| 2 | Filters/nets | No; no limit statement in this equivalence. Caller's continuity argument does not turn this algebra law into a filter theorem. |
| 3 | Universal property | No construction or universal object. |
| 4 | Bundled substructure | No closed-set predicate or subobject. |
| 5 | Weaker hierarchy | Yes; translated inequality is already `lt_sub_iff_add_lt` at AddGroup/LT/right-strict-monotone level. Division law uses existing division-ring API. |
| 6 | Higher category | No categorical content. |
| 7 | Concrete indices | Yes as scalar abstraction: n/m/sqrt's values can become arbitrary b/c; not a claim about arbitrary dimensions' square roots. |
| 8 | Concrete-via-abstract | Fires: source body `grind [gam, lam]` mentions eta zero times, gam/lam once each. Arbitrary e and general-field probes certify abstraction; [diagnostic]({L('concrete-diagnostic.json')}). |
| 9 | False-generalization guard | Preserve linked coefficients and ordinary subtraction. Do not replace Roth eta/gamma by modular/Dirichlet functions or Diophantine Roth by arithmetic-progression Roth. Counterexample rejects independent coefficients. |

Modern organization is available: use existing additive order API after scalar normalization. It enables direct composition with `sub_pos` and ordered-field arithmetic without real analysis. It does not establish a missing mathlib theorem warranting a new general wrapper.

## Phase 4.5 — infrastructure risk

All six rows are justified n/a for this theorem; it introduces no data definition or instance.

| Risk | Assessment |
|---|---|
| Typeclass diamond | n/a: no instance or structure is introduced. |
| Reducibility | n/a: theorem equality is proof-irrelevant; no data reduction contract. |
| Noncanonical unfolding | n/a for theorem; normalization of its parent definitions is separately tested. |
| Instance priority | n/a: no priority declaration. |
| Universe | n/a infrastructure risk: original concrete ℝ/ℕ, abstract probes use Type*. |
| Coercion | n/a: no coercion is installed; Nat→Real casts already existing. |

## Phase 4.6 — proof strategy

| # | Check | Result |
|---|---|---|
| 1 | Topology / epsilon-delta | No topology in target. |
| 2 | Algebra / subobjects | Scalar arithmetic, no ideal/submodule abstraction to gain. |
| 3 | Analysis / sequence vs filter | No analytic argument after treating eta/error as scalar values. |
| 4 | Category / universal characterization | No constructed categorical object. |
| 5 | Missing helper mathlib should have | None established: existing translation and field API suffice after normalization. New generic arithmetic proof is a possible wrapper, not evidence of absent substantive mathematics. |

MATHLIB-IDIOMATIC locally: unfold two parameter definitions and normalize scalar arithmetic. An explicit alternative is the verified `bridge` equality followed by `lt_sub_iff_add_lt.symm`; the bridge is a new `ring` proof, so that route cannot be labelled a strict existing-call replacement for the original. The current named form exposes source semantics to its callers.

## Phase 5 — all fifteen formal search cells

Each cell has the complete original tool request/result and elapsed_ms, or exact rg command/stdout/stderr/exit. External indexes are not assumed to match the pin. All local-search indexes reported warming: positive results are useful, empty results would not show absence.

| Form | Method | Result / receipt |
|---|---|---|
'''
for form in ['current','standard','abstract']:
 for method in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=rd('search-'+form+'-'+method+'.json')
  if method=='rg':desc='Pinned source enumeration; exact command and returned lines archived.'
  else:
   z=x['result']['structuredContent'];items=z.get('items',[]);names=[i.get('formal_name',i.get('name',''))for i in items];desc=', '.join('`'+n+'`'for n in names[:4])if names else'No results, not proof of absence.'
  report+=f"| {form} | {method} | {desc} [receipt]({L('search-'+form+'-'+method+'.json')}) |\n"
report+=f'''
Current-form searches returned unrelated Roth-number and Dedekind-eta declarations; those are rejected conceptually. Standard/abstract searches find the real building blocks. Pinned native #checks verify `lt_sub_iff_add_lt`, `sub_div`, `div_sub_div_same`, `mul_div_cancel_left₀`, `lt_div_iff₀`. Pinned homes: `Mathlib/Algebra/Order/Group/Unbundled/Basic.lean` (lt_sub_iff_add_lt via to_additive near619), `Mathlib/Algebra/Field/Basic.lean:97,112` (division/subtraction), `Mathlib/Algebra/GroupWithZero/Defs.lean:204` (cancellation). [Pinned files and hashes]({L('mathlib-inputs.json')}). No exact named old-form API is established; absence is not inferred solely from searches.

## Phase 5.5 — statement shape

1. **Normal form:** compare η+error<m/2, η<m/2−error, η<γ, and 0<γ−η. The canonical additive translation is already `lt_sub_iff_add_lt`; local RHS η<γ is the paper's semantic normal form and both callers then use `sub_pos`. It is not tagged simp, so no new global normalization policy is introduced.
2. **Syntactic generality:** verified `arbitrary_eta`, general-field `generic`, explicit subtraction `explicit_existing_translation`, and `original_normalized`. The named form is easiest for source-aligned local consumers; abstract upstream arithmetic should use the existing additive form. Both `.mp` and `.mpr` exist; actual callers only use `.mp`.
3. **Superfluous parameters/classes:** no explicit hypotheses or typeclasses to drop; δ/n/m occur in the concrete type. Eta's defining formula is superfluous to the arithmetic proof and can become e in a broader statement. This does not permit deleting these parameters from the unchanged `gam` signature.

Statement-shape verdict: acceptable locally; RESTATE-BEFORE-SHIP for any upstream scalar law, at the existing canonical abstract API. No public signature changed.

## Phase 6.0 — full caller and inline audit

Fresh no-ignore rg agrees with git grep over tracked production; inventory includes all canonical source files. [Lexical search]({L('source-search.json')}), [tracked crosscheck]({L('tracked-source-search.json')}), [inventory]({L('source-inventory.json')}), [full callers]({L('callers.json')}), [related expression audit]({L('inline-audit.json')}).

| Caller | Occurrences / use | Verified inline action |
|---|---|---|
| Roth.exists_delta, Main:227–249 (use241) | 1 body; no signature occurrence | In denominator nonzero proof, retain h=(hδ₀' 0 le_rfl hδ₀.le).2, unfold gam/lam, derive eta0<gam0 arithmetically. |
| Roth.roth_of_isIntegral, Main:547–563 (use560) | 1 body; no signature occurrence | Retain h30, unfold gam/lam and derive eta<gam before `sub_pos` and `div_lt_iff₀'`. |

External-to-file: one file, two declarations/two occurrences. None in declaring file. Both whole actual proofs replayed inside the complete original Main module under `Gap235Inline`, with only target calls replaced by explicit arithmetic derivations; both original signatures validated by `rfl` equality. [Exact full replay]({L('inline-executed.lean.txt')}), [clean result]({L('inline-receipt.json')}). This is more than a toy caller. No exact equivalent re-derivation elsewhere was established; related gamma−eta bounds are substantive estimates, not duplicates of the iff.

The canonical293 kernel audit independently finds exactly these two direct body consumers, zero direct type consumers, all293 names unique/present/with values and exact tracked order/private modules. Source lexical refs, source type refs, direct kernel body/type edges, generated-helper closure, simp and transitive import closure are distinct scopes: [scope audit]({L('scope-audit.json')}). No unmeasured transitive target-freedom claim is made for the replay.

## Phase 6 — composition experiments

A strict **three-existing-theorem term** compiles for normalized arbitrary scalars:

```lean
theorem three_term (a b c d : ℝ) (hd : d ≠ 0) :
    a + b < c / d ↔ a < (c - d * b) / d :=
  Eq.ndrec (motive := fun z ↦ a + b < c / d ↔ a < z)
    (Eq.ndrec (motive := fun z ↦ a + b < c / d ↔ a < c / d - z)
      (show a + b < c / d ↔ a < c / d - b from lt_sub_iff_add_lt.symm)
      (mul_div_cancel_left₀ b hd).symm) (div_sub_div_same c (d * b) d)
```

This uses exactly three mathematical lemmas plus equality transport and Iff symmetry; the equivalent three-rewrite proof is also verified. Only d≠0 is required, not d>0; negative_d verifies that detail. It is **not** an existing named mathlib theorem and not a strict three-call proof of the exact original spelling. Directly supplying it at d=2 to the expanded original fails (certified `fail_if_success`) because d*b is not definitionally the left-associated 4(1+3δ)n√m expression. Direct `lt_sub_iff_add_lt.symm` also fails until the gamma normalization bridge is supplied.

The fully expanded original closes by arithmetic automation; generic and arbitrary-eta forms likewise compile. The concrete bridge γ=m/2−error needs new ring normalization. Therefore **NOT-COMPOSABLE under the strict original-form ≤3-existing-call test as verified here**; this is not a universal impossibility theorem about all possible terms. The normalized form is COMPOSABLE. New generic proofs/project eta/gam/lam must not be counted as existing mathlib calls. Short `grind`/`ring` or a closing `simp [defs]` proof does not meet that strict composition criterion; this semantic-versus-normalization choice is precisely why the verdict remains BORDERLINE rather than an unsupported NO.

## Phase 7 — verdict and actionable alternatives

**BORDERLINE-needs-human**, independently assessed. The scalar content is already represented by mathlib's additive order and field identities, while the local name tells both actual callers that the paper's inequality gives a positive γ−η gap. Searches establish no substantive missing theorem; verified abstraction removes eta's formula, sqrt and natural indices entirely. The exact old spelling still needs arithmetic normalization, and the clean inline replay does not erase the value of a source-aligned local name. Neither the short original proof nor a parent parameter's verdict determines this result; no cost-based downgrade is used.

Future upstream design questions (not blockers for completion):
'''
for i,q in enumerate(questions,1):report+=f'{i}. {q}\n'
report+=f'''
Concrete local action: retain this lemma in `Roth/MainLemma.lean` while the named parameter API is local. If that API is removed or normalized, inline the two exact replacements already validated in `inline-executed.lean.txt`; no caller signatures need change. If a standalone upstream scalar wrapper is proposed, first decide question3 against the already verified three-call composition. No PR home/title/reviewer/grouping is promised for a BORDERLINE declaration. Prior accepted YES declarations were not inferred from names or reused as a verdict rationale.

Pairwise duplication audit:

| A | B | Same statement? | Same argument? | Action |
|---|---|---|---|---|
| eta_lt_gam_iff | lt_sub_iff_add_lt | After non-definitional gamma normalization | Yes, translated strict inequality | Use canonical additive API for abstract arithmetic; retain local semantic bridge if desired. |
| eta_lt_gam_iff | div_sub_div_same / mul_div_cancel_left₀ composition | Normalized scalar form only | Same arithmetic core | Verified strict-three term; coefficient/association bridge is separate. |
| eta_lt_gam_iff | exists_delta_bound | No: existence of small δ with the inequality versus equivalence | No: continuity/gap versus arithmetic | Do not unify; latter supplies the substantive hypothesis. |
| eta_lt_gam_iff | the two actual caller denominator arguments | Same local conversion substep | Yes | Full inlining possible; no other exact redeclaration located. |

## Phase 8 — evidence and completion

Four accepted clean native sets: original full-module replay/type/body/axioms/exact293 audit; exact18 isolated mathlib-only arithmetic; full Main caller inline replay; project generic/normalization and outgoing Roth body-edge probes. All are successful, nonpartial/non-timeout where the tool exposes those fields, error/warning/sorry-free, standard axioms only. Initial original warming response is not accepted success. The first isolated rejected attempt has recovered sorryAx; the second has tactic-linter warnings. Both exact sources and raw receipts are preserved separately and excluded from accepted verification. No limits raised, unsafe code, native_decide or new axiom. `#check_failure` unknown-identifier messages are intended info diagnostics, not errors.

[Verification index]({L('verification.json')}), [assessment]({L('assessment.json')}), [portable validator]({L('validate.py')}), [current manifest]({L('copy-manifest.json')}), [final validation]({L('final-validation.json')}). Supporting Lean sources are exact `.lean.txt` evidence, not new project modules. Root independent acceptance is pending. Freeze/native release only after manifest, portable validator and credential guard PASS.
'''
(D/'report.md').write_text(report)
print('Wrote report, assessment, verification, overview, scope/diagnostic/preparation artifacts.')
