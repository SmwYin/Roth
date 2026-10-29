from pathlib import Path
import json,hashlib,re
D=Path(__file__).resolve().parent;R=Path.cwd();N='Roth.boxFamily_finite';P='../evidence/'+N+'/'
def rd(n):return json.loads((D/n).read_text())
def put(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def result(r):
 z=r['result']['structuredContent'];return z.get('result',z)
z=result(rd('dependencies-receipt.json'));nt=rd('native-type.json');nt.update(compact_body_complete=True,compact_body_receipt='dependencies-receipt.json',compact_body=next(x['message'].split(': ',1)[1]for x in z['items']if x['message'].startswith('BOX245_TARGET_COMPACT_BODY:')),source_body_dependencies=['Roth.boxFamily_eq_image_finsupp_aux'],source_type_dependencies=['Roth.boxFamily'],kernel_body_project_constants=['Roth.boxFamily','_private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux'],kernel_type_project_constants=['Roth.boxFamily']);put('native-type.json',nt)
accepted=[]
for label,fmt,start,infos in [
 ('original','disk',16,['BOX245_FULL_TYPE:','BOX245_AUDIT: requested=293; unique=293','BOX245_AUDIT_PRESENT: present=293; values=293',"'Box245Original.replay' depends on axioms:","'Roth.boxFamily_finite' depends on axioms:"]),
 ('availability','raw',19,['@Set.Finite.image','@Set.Finite.pi\'','Unknown constant `Finset.finsupp`']),
 ('isolated','raw',19,["'Box245Generic."+n+"' depends on axioms:"for n in ['finite_coeff_choices','finite_family_of_monomials','zero_bound','infinite_family','abstract_image']]),
 ('project','disk',16,["'Box245Project."+n+"' depends on axioms:"for n in ['finite_generic','finite_original','private_bridge_composition','supplied_signature','zero_coefficient_bound','zero_degree','empty_variables','infinite_variables_finite_support','support_needed','weaker_disjunction','exists_ne_modByMonic_eq','caller_signature']]),
 ('composition','disk',190,['BOX245_INLINE: direct_target=false; private_representation=true; full_caller=true',"'Box245Composition.existing_image_law' depends on axioms:","'Box245Composition.original_absence_probe' depends on axioms:"]),
 ('dependencies','disk',218,['BOX245_TARGET_KERNEL_TYPE: Roth.boxFamily','BOX245_TARGET_KERNEL_BODY: _private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux','BOX245_TARGET_COMPACT_BODY:'])]:
 r=rd(label+'-receipt.json');accepted.append(dict(label=label,format=fmt,source=label+'-executed.lean.txt',receipt=label+'-receipt.json',source_sha256=sha(D/(label+'-executed.lean.txt')),original_execution_request=r['request'],native_region_start_line=start,required_info=infos))
rej=[]
for l,reason in [('isolated-rejected','Subtype binder inferred at ambient monomial type; rejected errors and recovered sorryAx'),('isolated-rejected2','MapsTo target unresolved; rejected errors and recovered sorryAx'),('isolated-rejected3','Explicit subtype binder alone insufficient; MapsTo target unresolved; rejected errors and recovered sorryAx'),('project-rejected','Missing classical DecidableEq for Iic and singleton normal form; rejected errors and recovered sorryAx'),('project-rejected2','Clean mathematical proof but unnecessarySimpa warning; rejected as accepted evidence'),('dependencies-rejected','Array.toArray typo; rejected errors')]:rej.append(dict(source=l+'-executed.lean.txt',receipt=l+'-receipt.json',reason=reason))
v=dict(declaration=N,completed=True,unresolved=[],standard_axioms=['propext','Classical.choice','Quot.sound'],accepted=accepted,rejected=rej,warming=[dict(receipt='original-warming-receipt.json',reason='initial disk cold elaboration partial=true; not accepted')],audit=dict(source='original-executed.lean.txt',receipt='original-receipt.json',requested=293,unique=293,present=293,values=293),canonical_direct_consumers=['Roth.exists_ne_modByMonic_eq'],canonical_direct_type_consumers=[],composition=dict(strict_existing_mathlib_composition_verified=False,abstract_existing_image_law_verified=True,new_generic_is_existing_mathlib=False,generic_semiring_finite_coefficients_verified=True,original_recovery_verified=True,actual_caller_replays=1,full_body_inline_success=True,original_signatures_retained_by_defeq=True,inline_private_bridge_retained=True,direct_target_independence_only=True,absence_probe_scope='explicit finite image call and simp only [Roth.boxFamily] do not close original target; no universal absence claim'),boundaries=dict(production_unchanged=True,nine_disk_imports_retained=True,stable_isolated_imports=18,extra_imports_requested=False,file_end_build='not due at245; prior accepted Theta228 build; next266'),generality=dict(arbitrary_semiring_and_coefficient_sets=True,finite_monomials=True,finiteness_choices_only_on_chosen_monomials=True,convenience_wrapper_choices_all_monomials=True,zero_bound_no_support_needed=True,zero_degree=True,empty_variables=True,infinite_variables_finite_support=True,unqualified_support_drop_refuted=True,support_iff_claimed=False,weaker_disjunction_compiled=True))
put('verification.json',v)
ph=['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']
questions=[
 'Should mathlib expose a semantic finite-support/finite-coefficient polynomial finiteness theorem, or should users retain an explicit Finset.finsupp image?',
 'If a semantic theorem is wanted, should its primary statement use an arbitrary finite monomial set and coefficient sets, with coordinate-degree boxes as corollaries?',
 'Should the integer coordinate-box definition and its finiteness corollary stay local to Roth while only the reusable coefficient-support bridge is proposed upstream?']
put('assessment.json',dict(declaration=N,canonical_index=245,file='Roth/MainLemma.lean',line=301,kind='theorem',verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases=dict.fromkeys(ph,'PASS'),justified_na={'2b':'theorem, not a one-line definition','4.5':'theorem introduces no data/instance; all six infrastructure risks n/a','YES_upstream_title_reviewers_grouping':'not a YES verdict; no proposed accepted PR'},unresolved=[],root_acceptance='pending',questions=questions,reason='Existing image finiteness closes after a project-only representation bridge. A broader semantic polynomial theorem was proved freshly, not found as a one-call existing mathlib replacement. Upstream interface boundary remains a mathematical API choice, not a verification blocker or cost decision.'))
put('overview-entry.json',dict(type=nt['type'],kind='theorem',what='Integer multivariate polynomials whose coordinate degrees have finitely supported bounds and whose coefficients lie in [0,B] form a finite set, even for an infinite ambient variable type.',how='Rewrite by Roth.boxFamily_eq_image_finsupp_aux to the image of a finite coefficient-array box, then use Finset.finite_toSet and Set.Finite.image.',hypotheses='Only finitely many variable degree bounds are nonzero. No finiteness of the ambient variable type or positivity of B is required.',project_dependencies=['Roth.boxFamily','Roth.boxFamily_eq_image_finsupp_aux'],caller_summary='One explicit body call in Roth.exists_ne_modByMonic_eq supplies its local Fintype. No external-file callers; exact293 kernel audit confirms one direct value consumer and no direct type consumer.',mathlib_api_audit='Finset.finsupp, Finset.mem_finsupp_iff, Finset.finite_toSet and Set.Finite.image provide enumeration and image finiteness. Set.Finite.pi\' and Set.Finite.of_injOn support a newly proved semantic theorem. The project representation helper is not existing mathlib.',moral_duplications='Shares the coefficient-array representation with Roth.ncard_boxFamily; finiteness and counting are different statements. It is not a duplicate of finite degree-index sets or nonzero bounded families.',generalization='Compiled: arbitrary CommSemiring R, arbitrary finite monomial support, and finite coefficient sets (only on selected monomials). Original recovered with no signature change. Also B=0 permits removal of the support condition; unqualified support removal fails for ℕ variables, r=1, B=1.',missing_api='A semantic finite-coefficient/finite-support bridge for MvPolynomial is the candidate API boundary; current Finset.finsupp image machinery already supplies the enumerated form.',junk='Used once and successfully inlined in its actual caller with unchanged type, but the inline still uses the project private representation bridge. Do not call it a pure existing-mathlib wrapper or dead code.',action='Retain production unchanged. Consider the three concrete upstream API questions in the full report; if choosing a local cleanup, inline the verified bridge/image proof at Roth.exists_ne_modByMonic_eq.'))
put('preparation-checks.json',dict(all_sources_inspected_before_execution=True,canonical_gate=dict(command=['python3','/private/tmp/roth-overview/check_audit_source.py',str(D/'original-executed.lean.txt')],exit_code=0,stdout='PASS exact293 unique source order: '+str(D/'original-executed.lean.txt')),observed_pre_execution=[dict(source=e['source'],exit_code=0,width_le100=True,source_read_before_native=True)for e in accepted],rejected_attempts_separately_preserved=True,failed_preparation_native_execution=False))

def link(n,label=None):return '['+(label or n)+']('+P+n+')'
search_rows=[]
findings={
 ('current','leanfinder'):'Finsupp.finite_of_degree_le needs Finite σ; unrelated Chevalley bounds do not solve coefficient finiteness.',
 ('current','loogle'):'Empty results for degreeOf plus Set.Finite; not an absence proof.',
 ('current','leansearch'):'External univariate card_eq_of_natDegree_le_of_coeff_le; pin spells related API Polynomial.ncard_boxPoly.',
 ('current','local_search'):'Only project Roth.boxFamily_finite; index:error reported honestly.',
 ('current','rg'):'No target duplicate; degree/coefficient candidates inspected.',
 ('standard','leanfinder'):'Finset.finsupp / Finsupp.pi are genuine generic enumerators; search prose about Finset zero is checked against pin.',
 ('standard','loogle'):'ofSupportFinite support identity; no semantic polynomial finite-family law.',
 ('standard','leansearch'):'Finset.finsupp and onFinset; Finsupp.fintype requires finite ambient types.',
 ('standard','local_search'):'Finset.finsupp candidate; index:error; scratch evidence hits excluded from existing mathlib.',
 ('standard','rg'):'mem_finsupp_iff and locally finite Finsupp intervals supply the actual image construction.',
 ('abstract','leanfinder'):'Set.Finite.image exact positive generic image law.',
 ('abstract','loogle'):'Set.Finite.image / of_finite_image / finite_image_iff; all require a bridge to the target set.',
 ('abstract','leansearch'):'Finite.Set.finite_image instance; same image representation obligation.',
 ('abstract','local_search'):'Set.Finite.image and image2; index:error, positive source/native verification required.',
 ('abstract','rg'):'Finite.image and Finite.of_injOn read in pinned source.'}
for f in ['current','standard','abstract']:
 for m in ['leanfinder','loogle','leansearch','rg','local_search']:
  x=rd('search-'+f+'-'+m+'.json');q=x['command'][2]if m=='rg'else x['request']['query']
  search_rows.append('| '+f+' | '+m+' | `'+q.replace('|','∣')+'` | '+findings[f,m]+' '+link('search-'+f+'-'+m+'.json','receipt')+' |')
rep=f'''# Roth.boxFamily_finite — completed single-declaration assessment

Verdict: **BORDERLINE-needs-human**. Canonical245, `Roth/MainLemma.lean:301–305`.
All required assessment work is complete; the three future upstream questions are design decisions,
not user blockers. Production Lean sources, pins, Git and overview/progress were not modified.

## Phase 0 — baseline and identity

Fresh hashes of all17 production source/pin inputs equal the shared manifest; the accepted baseline
was clean2467jobs. This declaration is not a file-end checkpoint; no new whole-project build was due.
The entire MainLemma module (including its main lemma and actual pigeonhole caller) was read and
replayed in a fresh namespace, renaming only the target outside the canonical array.
The exact tracked canonical293 array passes the independent pre-execution gate and the native
requested/unique/present/value checks, all293. No partial response is accepted.
Evidence: {link('inputs.json')}, {link('input-manifest.json')}, {link('baseline-build.txt')},
{link('source-MainLemma.lean.txt')}, {link('original-executed.lean.txt')}, {link('original-receipt.json')},
{link('preparation-checks.json')}.

## Phase 1 — statement and mathematical argument

Fix a variable type σ, a natural coordinate-degree bound r, and a natural coefficient bound B.
If only finitely many coordinates have nonzero r, only finitely many monomials can occur.
Each such monomial has one of the finitely many integer coefficients 0,…,B, so the entire
polynomial family is finite. The proof identifies it with an image of the finite coefficient-array
product. The representation equality, including the off-box zero coefficients, is substantive;
the final image-finiteness step is generic set theory.

Full native type (`Lean.getConstInfo`, `pp.funBinderTypes`):

```lean
{nt['type']}
```

σ is universe polymorphic; r and B are semantic bounds; `[Finite (Function.support r)]` is
the sole finiteness assumption. The conclusion is `Set.Finite`, not an enumeration.
Source body dependency: `Roth.boxFamily_eq_image_finsupp_aux`; source type dependency:
`Roth.boxFamily`. Kernel body additionally mentions `Roth.boxFamily` in its type transports
and the private name `_private.Roth.MainLemma.0.Roth.boxFamily_eq_image_finsupp_aux`.
These scopes differ. Exact type and body evidence: {link('native-type.json')},
{link('dependencies-executed.lean.txt')}, {link('dependencies-receipt.json')}.
The initial `pp.all` output elides9641characters and is **not a full kernel-body dump**.
A later compact printer emits the complete proof term without elision in the accepted dependencies
receipt. The full written source is separately archived.

## Phase 2 — preliminary checks

SMALL: an auxiliary finiteness theorem, not a named main result or a new structure.
The four proof lines do not determine contribution value. The one-line-definition test is
n/a because this declaration is a theorem. No exemption is being used to avoid the search.

## Phase 3 — exhaustive literature

| Channel | Exact query/access and result | Mathematical relevance |
|---|---|---|
| General specific | Integer multivariate polynomials, bounded degree and bounded coefficients, finite set, Roth auxiliary polynomial; {link('web-general.json')} | Local paper supplies exact box count. General web context is related height finiteness. |
| General abstract | Finite support functions, finite coefficient choices, finite Cartesian products; same receipt | Finite product/image is the right elementary abstraction, without an ambient finite variable type. |
| General alias | Northcott finiteness, bounded height and degree; same receipt | Related bounded-complexity terminology, not a claim this theorem is Northcott. |
| Optional ChatGPT math | Unavailable tool; justified skip | No external answer is invented. |
| Local clean.tex | Lemma9 proof, displayed coefficient box, eq43; {link('local-excerpt.tex.txt')}, {link('local-literature.json')} | Exact original family has finite m and count (B₁+1)^∏(rⱼ+1). Lean already supports infinite ambient σ with finite r support. |
| nLab | `site:ncatlab.org/nlab finite set finite product finite support functions`; {link('web-channels.json')} | Finite-set closure and pointed support context. Direct page fetch later failed unsupported XHTML; search result access is distinguished. |
| nCatLab distinct | `site:ncatlab.org/ncatlab finite products finite sets polynomials`; same receipt | Only out-of-namespace /nlab material returned; no exact in-namespace hit. This elementary theorem needs no categorical reformulation. |
| Stacks | Two actual mathematical queries, preserved in {link('web-channels.json')} and {link('web-recent.json')} | Broad graded-module chapters, no target law. Exploratory tag00E0 proved irrelevant and is labelled as such. |
| MathOverflow | Integer multivariate coefficient bounds and counting polynomials of bounded height; same two receipts | Pigeonhole coefficient boxes are familiar; discussion is not an exact infinite-variable theorem. |
| Recent arXiv | `site:arxiv.org multivariate polynomials bounded coefficients counting after:2021-10-29 before:2026-10-30`; {link('web-recent.json')} | arXiv2509.17563 submitted2025-09-22, revised2026-07-07, studies finite-field bounded-degree polynomial spaces, a related generality rather than this law. |

Primary crosschecks and access failures: {link('web-primary.json')}. Each web artifact contains exact
requests, response SHA256/byte count/status, clean selected titles/URLs/locators and original concise
summaries only; no article or search-result bodies are stored. No malformedsite query was used.
Returned query URLs not needed as evidence were omitted. The local source hash is in
{link('literature-source.json')}.

The common content is finite coefficient choices on a fixed finite monomial set. The manuscript's
integer coordinate box is one instance. Finite-field and height literature uses other coefficient
notions, so interval bounds must not be blindly transplanted to arbitrary rings or fields.
Ingram's June2020 slides, slide18, explicitly use bounded integer degree/coefficient finiteness
in a height-finiteness explanation; the recent finite-field paper supplies a different application.
No exact theorem-specific generality is inferred solely from absent search results.

## Phase 4a — all parameters and hypotheses

| Parameter/condition | Current form | Verified analysis |
|---|---|---|
| σ/universe | Arbitrary `Type u_1` | Already permits infinite σ and empty σ; no Fintype strengthening. |
| r | `σ → ℕ` with finite support | Bundling as Finsupp is a representation change. Native `finite_generic` uses `Finsupp.ofSupportFinite` and finite Iic, with its coercion defeq to r. |
| Support hypothesis | `[Finite ↑(Function.support r)]` | Required for general nonzero coefficient boxes: r=1 on ℕ and B=1 contains injectively all X i and is infinite. No iff or maximality criterion is claimed. |
| B | Any natural including0 | No positivity hypothesis to weaken. B=0 gives singleton zero independently of r support. The weaker disjunction B=0∨finite-support compiles. |
| Coefficient type | ℤ | Fresh theorem works over arbitrary `CommSemiring R` with explicitly finite coefficient sets. Merely replacing ℤ by ℚ and keeping intervals would not preserve finiteness. |
| Coefficient choices | Uniform integer interval | Fresh generic finite-support theorem permits coefficient sets varying by monomial; their finiteness is needed only on the selected monomial set. No zero-in-every-set premise is required for finiteness, since incompatible choices may make the family empty. |
| Monomial shape | Coordinate box | Fresh theorem permits an arbitrary finite monomial set, independent of coordinate or total-degree form. |
| Decidability | None in signature | Classical finite enumeration is local; no new public decidability assumption. |

Evidence: {link('isolated-executed.lean.txt')}, {link('isolated-receipt.json')},
{link('project-executed.lean.txt')}, {link('project-receipt.json')}.

## Phase 4b — verified generality verdict

STRICTLY NARROWER in a semantic restatement: arbitrary finite monomial support and finite coefficient
sets were actually proved. This is a new proof, **not existing mathlib**. Within the fixed boxFamily
interface the support hypothesis cannot simply be dropped; the exceptional B=0 branch is separately
verified. The source signature is retained by the original recovery and a compiled proof equality
(the equality certifies type agreement by proof irrelevance, not identical proof syntax).

The proposed reusable semantic type, compiled under the stable18 mathlib-only imports, is:

```lean
{{σ R : Type*}} → [CommSemiring R] →
  (s : Set (σ →₀ ℕ)) → s.Finite →
  (t : (σ →₀ ℕ) → Set R) → (∀ d ∈ s, (t d).Finite) →
  {{P : MvPolynomial σ R | (↑P.support : Set (σ →₀ ℕ)) ⊆ s ∧
    ∀ d, P.coeff d ∈ t d}}.Finite
```

The project-context convenience wrapper for coordinate bounds asks finite t d for **all** d;
this is stronger than the primary theorem needs and is not called the weakest formulation.
The compiled generic recovery changes the underlying family/coefficient interface, so it does not
by itself settle YES-generalise-first. The upstream decision is between a semantic corollary and
using the existing enumerated image. Cost does not choose the verdict.

## Phase 4c — modern idiom, nine rows

| # | Question | Answer / concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | Already uses Finite support; local Fintype construction only for enumeration. No custom finiteness predicate. |
| 2 | Filters/topology | No: finite combinatorics, no limit or metric premise. |
| 3 | Universal property | No: a coefficient injection and finite product suffice; no new universal-property class is justified. |
| 4 | Bundled substructure | No: bounded coefficient boxes are not generally closed under addition, so submodule/subring would change the object. |
| 5 | Algebraic hierarchy | Yes: arbitrary CommSemiring with finite coefficient sets is compiled; supports finite coefficient rings and non-interval choices. |
| 6 | Higher categories | No: no categorical hypothesis or additional usable consequence. |
| 7 | Concrete indices | σ already arbitrary. Monomials can be an arbitrary finite set; integer coefficient intervals become finite sets rather than an unjustified generic order. |
| 8 | Concrete-via-abstract | Yes: after the image rewrite, boxFamily occurs zero times in the remaining proof line. Abstract finite-image law already exists. The bridge to that form remains project-only, while the fresh semantic proof uses Set.Finite.pi' and of_injOn. |
| 9 | False-generalisation guard | Pass for finite coefficient sets with verified original specialization. Reject replacing infinite σ by Fintype as a generalization, dropping support unconditionally, or treating arbitrary ordered-field intervals as finite. |

Modern idiom available as a reusable semantic view, but its finiteness law is newly proved here;
no new typeclass or redundant enumerator is proposed. It concretely enables Set.Finite.pi',
Set.Finite.of_injOn, image/subset operations, and support shapes beyond coordinate boxes.

## Phase 4.5 — infrastructure risk

The declaration is a theorem, so the canonical six definition-risk rows are all justified n/a:

| Risk | Verdict / reason |
|---|---|
| Typeclass diamond | n/a: introduces no instance or structure. |
| Reducibility leak | n/a: introduces a proof, not a data definition or reducibility setting. |
| Noncanonical unfolding | n/a: introduces no definitional equality for data. |
| Instance priority | n/a: registers no instance. |
| Universe restriction | n/a: introduces no data universe choice; the theorem retains arbitrary σ. |
| Coercion | n/a: registers no coercion. |

It introduces no data definition, instance, coercion or simp attribute. The scratch generic family
is a probe, not an accepted production definition or instance proposal.

## Phase 4.6 — proof strategy, five rows

| # | Question | Verdict / consequence |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Element algebra versus substructures | No refactor into substructures: interval boxes are not closed; support/coeff injection is the meaningful abstraction. |
| 3 | Sequences versus nets | n/a: no analytic limit. |
| 4 | Construction versus universal property | n/a: a finite enumeration is exactly the required object. |
| 5 | Helper mathlib should have | Candidate semantic finite-support/finite-coefficient bridge, tested as a new theorem; Finset.finsupp and Set.Finite.image already cover its enumerated form. |

Current strategy is MATHLIB-IDIOMATIC once the representation is fixed. A semantic API change may
replace the private bridge with the fresh generic theorem, but shortness after a project helper is
not evidence of a strict existing-mathlib composition. No proof-strategy cost drives the verdict.

## Phase 5 — all15 actual formal-search cells

| Form | Method | Exact query/pattern | Result and receipt |
|---|---|---|---|
'''+ '\n'.join(search_rows)+f'''

The external search revision differs from the pin: `Polynomial.card_eq_of_natDegree_le_of_coeff_le`
is returned externally, while the pinned file has `Polynomial.boxPoly`, `Polynomial.ncard_boxPoly`
and `Polynomial.finite_mahlerMeasure_le`. Those are univariate and do not supply the required
arbitrary-variable coefficient/support bridge. Finsupp.finite_of_degree_le requires finite σ and
bounds exponent degree, not polynomial coefficient choices.
All source-based candidates were read in the archived pinned modules:
{link('mathlib-inputs.json')}. Native positive signatures and stable-prefix availability:
{link('availability-executed.lean.txt')}, {link('availability-receipt.json')}.
`Finset.finsupp` and Finsupp locally finite intervals are not imported by stable18; they are available
in the actual project document and their image law is compiled there, with no added imports.
A source-wide untruncated target/coefficient search is {link('full-name-search.json')}.
The local index reports `index:error`; scratch/evidence names it returns never count as mathlib.
Positive candidates are verified against the pin; failed/empty searches do not establish absence.

## Phase 5.5 — statement shape, three checks

1. **Normal form:** Set.Finite is the right output for subsequent `.fintype` use. The finite
   coefficient image and semantic support predicate are not definitionally identical; the private
   bridge proves equality. The native generic recovery verifies the semantic correspondence.
2. **Syntactic generality:** arbitrary finite monomial support avoids committing to coordinate
   degree syntax. Finsupp-bundled r can avoid a separate support instance; original function r is
   retained at the tested caller. The disjunctive B=0 statement is compiled as an optional logical
   weakening, not asserted to be an iff or the preferred main interface.
3. **Superfluous arguments:** σ, r and B describe the family; no argument is redundant. No
   positivity/Nonempty/Fintype σ condition is needed. Removing finite support wholesale is refuted
   by the actual infinite family. Classical decidability is local, not an additional hypothesis.

Statement-shape verdict: RESTATE-BEFORE-SHIP if choosing a semantic upstream theorem; the current
local statement is suitable for its one caller and all boundary cases pass.

## Phase 6.0 — full callers, inline derivations and kernel scopes

| Explicit caller | Source use | Cross-file? | Actual experiment |
|---|---|---|---|
| `Roth.exists_ne_modByMonic_eq`, MainLemma:359–379 | One body occurrence at367; local Fintype for pigeonhole domain | No | Full original statement and body replayed, replacing only the finiteness call by its bridge/image proof; clean success and signature agreement. |

Fresh `rg --no-ignore` and `git grep` agree exactly on the declaration head and the one use:
{link('source-search.json')}, {link('tracked-source-search.json')}. Full source caller body/signature
and hash are {link('callers.json')}; full inventory is {link('source-inventory.json')}. The canonical
kernel audit independently yields one direct value consumer, zero direct type consumers:
{link('canonical-consumers.json')}. These are distinct from lexical declaration occurrences.
The broader inline audit {link('inline-audit.json')} finds the target finiteness proof and
representation/counting code, but no second hidden direct derivation of the same boxFamily
finiteness statement. Other finite-set constructions prove different claims.

No simp attribute is present. Kernel direct-use independence of the inline caller is tested in
{link('composition-receipt.json')}: target constant absent, private representation helper present.
The inline still uses `Roth.ncard_boxFamily`, which may share the private bridge. No independence
from all transitive project dependencies is claimed. Likewise, source caller counts are not a
transitive dependency census and the scoped kernel inventory does not pretend otherwise.

## Phase 6 — composition experiments and pairwise duplication audit

The abstract enumerated family has the existing two-call proof:

```lean
(s.finsupp t).finite_toSet.image AddMonoidAlgebra.ofCoeff
```

It was compiled in {link('composition-executed.lean.txt')}. Recovering the original boxFamily needs
`Roth.boxFamily_eq_image_finsupp_aux`, not an existing mathlib constant. The exact native caller
inline is in {link('project-executed.lean.txt')}; this is locally actionable, but it retains that
private helper and is not counted as a pure mathlib-only ≤3-call replacement.
The original target fails the explicit finite-image call and `simp only [Roth.boxFamily]` closure
probes; a fresh generic theorem then closes it. These bounded negative probes are not a universal
proof of library absence. Outcome: **NOT-COMPOSABLE by the strict existing-mathlib criterion**
without the representation bridge. The newly proved semantic bridge is not silently relabelled
as an existing building block. No new imported project definitions are used in the isolated proof.

The parent boxFamily assessment is BORDERLINE, independently checked against the actual image
representation rather than inherited as a verdict. The explicit parent re-aim gate only forces
NO-mathlib-has-it when the parent was replaced by an existing more-general definition with its
analogous existing law. Here the generic image law exists and compiles, but the semantic bridge
is still new/project-only, so that gate does not force NO. This is an interface decision.

| Decl A | Decl B | Same statement? | Same proof? | Verdict |
|---|---|---|---|---|
| boxFamily_finite | boxFamily_eq_image_finsupp_aux | No: finite versus representation equality | Shares representation | Keep distinction; the equality carries normalization content. |
| boxFamily_finite | ncard_boxFamily | No: finite versus exact count | Shared private representation | Coordinate the API; do not use ncard count alone as automatic finiteness (infinite sets have ncard0). |
| boxFamily_finite | box/card_le_card_box | No: polynomial family versus finite exponent box | Both finite-coordinate combinatorics | Distinct coefficient layer; no duplicate statement. |
| boxFamily_finite | finite_mahlerMeasure_le | No: coordinate degrees and nonnegative coefficients versus univariate degree/Mahler measure | Different encodings | Related bounded complexity, no direct specialization verified. |
| boxFamily_finite | Set.Finite.image | Abstract law after bridge | Exact last step only | Reuse image law; retain honest bridge obligation. |

## Phase 7 — verdict and concrete actions

**BORDERLINE-needs-human.** The finiteness theorem is correct, used, and already general in its
variable index. There is a compiled, meaningful broader semantic theorem. The relevant existing
API already enumerates finite coefficient choices, and its image law is immediate, while the
semantic polynomial/degree bridge is substantive new content. Whether to expose a semantic
polynomial finiteness lemma upstream or use the enumerated interface is a mathematical API
boundary. Neither the four-line source spelling nor the parent's later use nor implementation
cost settles that choice. This is not an unsupported absence-based YES or an automatic NO.

Future upstream questions (assessment complete; no response required to finish this report):

'''+ '\n'.join(str(i+1)+'. '+q for i,q in enumerate(questions))+f'''

Alternative local destination: retain `Roth/MainLemma.lean` near the private coefficient-box
representation. If local cleanup is chosen, the sole caller can inline the verified bridge/image
proof, preserving its exact statement; no other caller needs changing. If proposing upstream,
use the arbitrary finite-monomial/finite-coefficient statement above and assess its home near
MvPolynomial support APIs with the Finset/Finsupp import layering made explicit. No upstream
PR title, reviewer, or grouping with accepted YES declarations is claimed for this BORDERLINE
assessment; those YES-only requirements are n/a. No production edit or PR was made.

## Phase 8 — verification, limits and frozen handoff

All accepted executions have complete clean diagnostics and only propext/Classical.choice/Quot.sound.
Exact executed sources, unchanged full raw native requests/results and elapsed_ms are linked by
{link('verification.json')}. Three rejected isolated attempts, one rejected project elaboration,
one rejected project warning-only attempt and one rejected dependency-audit typo are retained;
none is accepted proof evidence. Initial cold original elaboration was partial and is retained
as warming only. No sorry/new axiom/unsafe/native_decide or resource-limit increase is accepted.
The final proof sets are original, availability, isolated, project, composition and dependencies.

The portable read-only validator checks current manifest hashes/bytes, fresh17 inputs, exact293
source/runtime array, accepted diagnostics/axioms, formal15 searches, caller/source consistency,
report links and secret guard, and supports scratch plus integrated layouts:
{link('validate.py')}. Current supporting artifact inventory is {link('copy-manifest.json')}.
Root acceptance remains pending and is independent of the worker's checks.
'''
(D/'report.md').write_text(rep)
print('Wrote report, assessment, verification, overview entry and preparation metadata')
