from pathlib import Path
import json,hashlib
D=Path(__file__).parent;N='Roth.exists_ne_modByMonic_eq';R=Path('/Users/ramin/LEAN/Roth')
def rd(n):return json.loads((D/n).read_text())
def put(n,x):(D/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n'if not isinstance(x,str)else x)
def link(n):return f'[{n}](../evidence/{N}/{n})'
questions=['Should a bounded integer-polynomial observation collision lemma be public independently of Roth, or should the Hasse/diagonal specialization remain project-local?', 'If public, should the helper take a finite coefficient alphabet with its cardinality rather than the symmetric integer interval and uniform C?', 'Should the polynomial observation helper be grouped with a reusable bounded-polynomial counting API, while generic finite-map collision continues to use existing Fintype pigeonhole API?']
a=dict(declaration=N,canonical_index=249,verdict='BORDERLINE-needs-human',completed=True,allphases='PASS',phases={k:'PASS'for k in ['0','1','2','3','4a','4b','4c','4.5','4.6','5','5.5','6.0','6','7','8']},phase_na={'one_line':'Theorem, not a definition.','4.5':'All six infrastructure risks justified n/a: theorem introduces no definition/instance/coercion.','ask_chatgpt_math':'Unavailable optional server; all remaining named channels executed.'},questions=questions,unresolved=[],root_acceptance='pending');put('assessment.json',a)
t=rd('native-type.json')['type'];deps=rd('dependencies.json')
over=dict(type=t,kind='theorem',what='Two distinct integer box polynomials share every selected diagonal Hasse derivative remainder when a strict coefficient-array budget is smaller than the box family.',how='Encode each polynomial by the J × Fin natDegree remainder coefficients in a finite integer interval; use Fintype.exists_ne_map_eq_of_card_lt, ncard_boxFamily, and Polynomial.sum_modByMonic_coeff to recover full remainders.',hypotheses='Arbitrary variable type; finite support of natural degree bounds; natural B,C; monic integer divisor; finite selected multiindices; low coefficient absolute bounds; strict real counting budget.',project_dependencies=deps['canonical_body'],caller_summary='One explicit proof caller, private Roth.exists_mem_RSet_le_index_aux at MainLemma:550, call557. No external-to-file proof callers or direct type consumers. Full caller inlining preserves its signature.',mathlib_api_audit='Existing finite-map collision and low-degree monic remainder reconstruction verified; finite-ring polynomial collision is related but does not apply to integer interval alphabets. Complete original is not <=3 existing mathlib calls.',moral_duplications='Generic collision duplicates Fintype pigeonhole only after a substantive polynomial encoding and project box cardinality bridge; pigeonhole_count supplies the budget and ncard_boxFamily supplies source size, neither is the same theorem.',generalization='Verified finiteObservations over arbitrary finite α,ι and dependent finite codomains; verified polynomialObservations for arbitrary finite source α and finite observation indices ι, followed by exact original recovery. The first is existing pigeonhole API with Pi cardinal normalization; the second is a newly proved helper, not an existing mathlib replacement.',missing_api='Potential bounded polynomial observation collision helper / finite coefficient alphabet counting bridge; acceptance and exact packaging remain concrete upstream design questions.',junk='Used once in the central auxiliary-polynomial construction. Inlining verified but expands the caller by the complete encoding proof; no dead-code or <=3-call wrapper finding.',action='Retain project-local Hasse specialization pending the three upstream API design questions; use existing Fintype collision directly in any abstract-only version. No production edits in this assessment.');put('overview-entry.json',over)
for p in D.glob('web-*.json'):
 x=rd(p.name)
 for l in x['locators']:l['title']=' '.join(l['title'].split())
 put(p.name,x)
callers=rd('callers.json');callers['callers'][0].update(line=550,call_line=557);put('callers.json',callers)
web='\n'.join(f'| {i+1} | {label} | `{rd("web-"+label+".json")["request"]}` | {rd("web-"+label+".json")["summary"]} | {link("web-"+label+".json")} |'for i,label in enumerate(['general1','general2','general3','nlab','ncatlab','stacks','mathoverflow','arxiv','arxiv-refined','primary','primary-detail']))
formal='\n'.join('| '+f+' | '+' | '.join(link('search-'+f+'-'+m+'.json')for m in ['leanfinder','loogle','leansearch','rg','local_search'])+' |'for f in ['current','standard','abstract'])
generic=(D/'isolated-executed.lean.txt').read_text().split('namespace Collision249Generic',1)[1].split('example (C N',1)[0]
report=f'''# `{N}` — canonical249

Verdict: **BORDERLINE-needs-human**. The complete selected-Hasse-remainder theorem needs a polynomial encoding proof. The abstract finite-map collision already exists; calling that outer theorem once does not make the original theorem a one-call replacement. This completed read-only assessment leaves only future upstream design questions, with verification unresolved[] and root acceptance pending.

## Phase0 — Baseline and source

Fresh hashes of all17 sources/pins match the tracked shared manifest; the reusable baseline succeeds with2467 jobs. See {link('inputs.json')}, {link('input-manifest.json')} and {link('baseline-build.txt')}. Canonical tracked order resolves the public theorem at `Roth/MainLemma.lean:359` (prompt's358 was approximate). Full MainLemma and its sole actual caller were read; complete module evidence is {link('source-MainLemma.lean.txt')}. No production, pin, Git, overview or progress edits. No file-end build required at249; last accepted file-end build is Theta228, next MainLemma266.

Original full module replay succeeds, preserving the full target signature: {link('original-executed.lean.txt')} and {link('original-final-receipt.json')}. A first cold request was partial and is retained as warming only. Full #print type/body is unelided; independent `Lean.getConstInfo` with `pp.funBinderTypes` gives the full statement below. Original and replay use only propext, Classical.choice, Quot.sound.

## Phase1 — Mathematical statement and proof

For integer multivariate polynomials whose coordinate degrees are bounded by a finitely supported natural function r and whose coefficients lie in [0,B], consider any finite list J of Hasse derivatives. Substitute the same variable in every coordinate and reduce each resulting univariate polynomial modulo a fixed monic integer polynomial f. If every remainder coefficient below degree f has absolute value at most C and `(2C+1)^(degree f × |J|)` is smaller than the number `(B+1)^(finprod (r+1))` of inputs, two distinct inputs have identical complete remainder tuples.

Each parameter has a separate role: σ is arbitrary (not required finite); r controls the finite monomial box and its finite-support instance ensures counting; B bounds source coefficients; f is the common integer divisor and hf makes the first natDegree coefficients determine its remainder; J selects observations; C bounds the target alphabet; hC provides membership in that finite alphabet; hcount is the strict pigeonhole budget.

```lean
{t}
```

Proof: give the box family a finite type using `boxFamily_finite`; encode W by coefficients indexed by `J × Fin f.natDegree` in `Set.Icc (-C) C`. Compute the codomain cardinality using function/product/Fin/interval cardinalities and the source cardinality using `ncard_boxFamily`, transfer the real inequality back to naturals, and apply `Fintype.exists_ne_map_eq_of_card_lt`. Sum coefficient monomials and use `Polynomial.sum_modByMonic_coeff` to recover the full remainder equalities. Distinct subtypes give distinct polynomials.

Direct canonical **type dependencies**: {', '.join(deps['canonical_type'])}. Direct canonical **body dependencies**: {', '.join(deps['canonical_body'])}. Complete used-constant lists, including the generated internal arithmetic proof helper, are in {link('dependencies.json')}; lexical/body/type/kernel scopes are kept separate. The theorem has no simp attribute; the audit does not claim transitive or simp closure.

## Phase2 — Preliminary checks

**BIG**: the module's main-results list explicitly names this pigeonhole step. This is a substantive finite encoding theorem despite its short final collision call. One-line definition test: **n/a**, theorem. No inherited verdict from246 or248 and no verdict based on proof cost.

## Phase3 — Exhaustive literature

| # | Channel | Exact request | Outcome / own summary | Evidence |
|---|---|---|---|---|
{web}
| 12 | Local clean.tex | `rg` pigeonhole / remainder counts | §6 proof of Lemma9, equations43–45 and padded nD coefficient arrays | {link('literature-local.json')}, {link('literature-local-excerpt.txt')} |
| 13 | ask_chatgpt_math | n/a | Optional tool unavailable; not substituted by invented channel | this row |

The ordinary finite-map principle is standard in arbitrary finite sets. The specific application is classical Roth auxiliary-polynomial construction, also reorganized through Siegel-type linear systems. The Princeton authors' [seminar notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf), PDF pages158–159, equations18.15–18.20, directly count selected remainder coefficient arrays. [Milojevic's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf), Section4, instead constructs a bounded kernel vector by subtracting two equal-image inputs. These formulations agree on the collision mechanism and differ in packaging. Neither source requires that observations themselves be Hasse derivatives once the degree/remainder coefficient bounds have been supplied. The local source already separates the quantitative budget into248 and source counting into246.

nLab supplies FinSet/finite sets, not this specialized wrapper. Distinct nCatLab namespace was actually queried and returned out-of-namespace material, not a claimed exact hit. Stacks' returned commutative-algebra locators concern monic division/integral algebras, not this counting application. MathOverflow is supplementary corroboration, not proof authority. The recent arXiv query used **after:2021-10-29 before:2026-10-30**; additive-combinatorial Roth and Hasse-principle results are not this theorem; refined Diophantine query was empty. Search failure is not absence evidence. Only exact requests, response SHA/bytes/status, clean titles/URLs/locators and concise own summaries are persisted; no web article/search bodies.

## Phase4a–b — Generality

| Parameter/hypothesis | Assessment and verified alternative |
|---|---|
| σ / finite support r | Already allows infinite variable types; replace entire box domain by arbitrary finite α in the verified polynomial helper. Finite support is used to construct/count this particular domain, not intrinsically by collision. |
| r and boxFamily | Source cardinality is the only property used after encoding. Zero bounds are allowed; tested Unit all-zero bounds have B+1 constant polynomials. General source-family α removes all degree constraints. |
| B : ℕ | A convenient source alphabet parameter, not a collision invariant. Generic α removes B, retaining only its cardinality. B=0 makes source count1, so strict budget cannot hold since target count≥1. Tested cardinality and arithmetic. |
| f : Polynomial ℤ | Low-degree remainder reconstruction is ring-general (verified over `[Ring R]`), but counting a bounded symmetric interval uses ℤ and its locally finite order. Replacing ℤ by arbitrary ring without a finite coefficient alphabet loses the finite target bound. |
| hf : f.Monic | Essential for unchanged low-degree observation recovery. Full-family counterexample f=C2, r=0 on Unit, B1, J={{0}}, C0 compiles: bounds vacuous and count1<2, but no distinct pair has equal full remainders. |
| J : Finset (σ→₀ℕ) | Verified replacement by arbitrary finite observation type ι, independent of σ and derivative shape. Empty J is allowed; a concrete collision with f=1 and B1 compiles. |
| C : ℕ | Includes0. A general finite coefficient alphabet / coordinate-dependent codomains is natural; verified abstract finiteObservations takes dependent finite β i. Uniform integer bounds are retained in the substantive polynomial helper, not claimed to be generic ring norms. |
| hC | Needed to land in the finite target. Only coefficients i<natDegree are used; no unnecessary global coefficient bound. |
| hcount | Equivalent natural strict cardinal inequality verified in original recovery. Non-strict inequality cannot guarantee a collision: Fin1 has no distinct pair. |

A **verified wider representation** exists: arbitrary finite α and ι with observations Q : α→ι→Polynomial ℤ and a source-cardinality budget; exact original recovery compiles. The concrete fixed-interface premises are not dead arguments. The generic finite-map core already exists in mathlib; the polynomial helper below is an **own new proof**, not a found existing replacement. This is an API design alternative rather than a claim that deleting hf or finite support from the unchanged statement works.

```lean
{generic.strip()}
```

Sources and receipts: {link('isolated-executed.lean.txt')}, {link('isolated-final-receipt.json')}, {link('recovery-executed.lean.txt')}, {link('recovery-receipt.json')}. Independent mathlib-only18 has `#check_failure Roth.exists_ne_modByMonic_eq`, no Roth import, no project-only taylor/diag/Hasse definitions. Actual-context recovery supplies the project observation map and existing project cardinality theorem explicitly. No new isolated import was needed; disk9/shared18 stayed stable.

## Phase4c — All nine modern-idiom rows

| # | Question | Answer / reformulation / downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already uses Finite support and local Fintype. Generalized α,ι use Fintype and dependent codomain instances, composing with card_pi. No need for a custom collision class. |
| 2 | Filters/topology | No: finite combinatorics, no convergence. |
| 3 | Universal property | No new universal-property object is needed; a finite observation function and its collision suffice. |
| 4 | Bundled substructure | boxFamily is not closed under addition and does not become a submodule. Finite subtype is the right domain. |
| 5 | Hierarchy | Recovery ring-general; finite integer alphabet counting is separate. Arbitrary rings need supplied finite alphabets, not an unjustified ordered-ring weakening. |
| 6 | Higher categories | No higher-categorical content. |
| 7 | Concrete indices | Yes: replace derivative multiindices by arbitrary finite ι and observations Q; verified. Enables coefficient/remainder constraints unrelated to derivatives. |
| 8 | Concrete-via-abstract | Explicit body diagnostic: boxFamily appears twice in executable lines, diag/hasseDeriv in one encoding line, and neither is used by the final coefficient reconstruction. After setting F, only finite cardinalities, bounded coefficients and monic recovery matter. Verified abstraction separates this structure rather than only renaming it. |
| 9 | False-generalization guard | Preserved by recovering the exact original type. Generic finite maps alone forget polynomial reconstruction, so are not advertised as the entire substantive theorem. Nonmonic C2 counterexample rejects dropping monicity without replacing the observations. |

Modern idiom available: **yes, separation of finite observations and polynomial recovery**. It removes derivative-specific coupling and composes with Fintype Pi cardinality. Existing mathlib already has the generic map theorem; deciding whether the polynomial observation bridge deserves a named API remains the concrete upstream issue.

## Phase4.5 — Infrastructure risks

| Exact risk label | Assessment |
|---|---|
| Typeclass diamond | n/a: theorem adds no instance path. |
| Reducibility leak | n/a: theorem proves Prop, not a new reducible data object. |
| Non-canonical unfolding | n/a: no new definition or simp rewrite. |
| Instance priority collision | n/a: no instance declaration. |
| Universe-polymorphism issues | n/a for definitional infrastructure; original signature and polymorphic replay verified. A rejected locally polymorphic inline attempt was corrected by using the caller's existing σ. |
| Coercion ambiguity | n/a: theorem registers no coercion; subtype coefficient coercions are explicit proof data. |

Overall risk: **n/a — theorem**. Definitions-only `#synth`/reducibility probes do not apply.

## Phase4.6 — Proof strategy

| # | Check | Answer |
|---|---|---|
| 1 | ε–δ vs filters | No topology. |
| 2 | Elements vs substructures | Finite observation encoding is appropriate; forcing an ideal/submodule loses bounded input coefficients. Equality of remainders can be expressed by divisibility, but does not perform the finite counting. |
| 3 | Sequences vs nets | No analytic limits. |
| 4 | Construction vs universal property | No categorical construction; finite Pi target already canonical. |
| 5 | Missing helper API | Potential polynomial-observation collision / finite coefficient alphabet helper. Low-degree reconstruction is already sum_modByMonic_coeff; do not re-propose it as missing. |

Verdict: **MATHLIB-IDIOMATIC** finite pigeonhole strategy; optional helper extraction can cleanly separate the reusable layer. This is mathematical packaging, not a cost-based downgrade.

## Phase5 — Fifteen actual formal searches

| Form | Finder | Loogle | LeanSearch | rg pinned source | Local names |
|---|---|---|---|---|---|
{formal}

{link('formal-search-matrix.json')} records all15 cells. Exact name search was untruncated: {link('full-name-search.json')}. All three local searches returned useful source matches with **index:error**; they are not complete index consultations and prove no absence. External indices can differ from the pin. Positive candidate signatures and uses were checked natively in isolated18.

Pinned building blocks: `Fintype.exists_ne_map_eq_of_card_lt` (`Mathlib/Data/Fintype/Pigeonhole.lean:44`), `Polynomial.sum_modByMonic_coeff` (`Mathlib/Algebra/Polynomial/Div.lean:442`), `Fintype.card_fun`, `Fintype.card_pi`, product/Fin/interval cardinalities, and `Int.card_Icc`. Related `Polynomial.exists_eq_polynomial` in `NumberTheory/ClassNumber/AdmissibleCardPowDegree.lean:36` works over a **finite semiring coefficient type** and one finite-indexed polynomial family. ℤ is infinite, and Set.Icc(-C,C) is not a semiring closed under the needed polynomial operations. Thus it does not replace this theorem by setting Fq to an integer interval. `NumberTheory/SiegelsLemma` concerns a bounded linear kernel vector and needs a separate linearization bridge. Source snapshots and pin hashes: {link('mathlib-inputs.json')}.

No exact entire application was located. That is a bounded search conclusion, not a universal absence claim. The compiled direct-pigeonhole attempt in recovery is rejected by `fail_if_success`: the whole polynomial codomain has no finite instance/cardinality budget supplied. Encoding and reconstruction must be supplied. No broad timed-out exact? search is counted as success or absence.

## Phase5.5 — Statement shape

**Normal form:** collision `∃ x y, x≠y ∧ F x=F y` is canonical Fintype API; pointwise equality of selected remainders is appropriate for the caller. Equivalent divisibility `f∣diag(Δj(W'−W''))` is useful after subtraction but packages additional additive work. There is no noncanonical iff orientation here; RHS normal-form convention n/a.

**Syntactic generality:** attempted natural budget, arbitrary finite α/ι polynomial observations, dependent finite β i, and full original recovery all compile. Natural card inequality avoids real casts for standalone counting; the original real inequality is convenient for248's analytic budget. Do not change that caller-facing type just for surface brevity.

**Superfluous arguments:** all nine rows in Phase4a cover σ,r/support,B,f/hf,J,C,hC,hcount. None is unused in the unchanged mathematical interface. B>0, natDegree>0, J nonempty and positive coordinate bounds are deliberately absent; the budget or degenerate observations handle those cases. The explicit full-family C2 guard proves hf cannot be discarded. Overall: **RESTATE-BEFORE-SHIP** for an upstream generic polynomial helper; **SHIP-AS-STATED locally** is reasonable pending API choice.

## Phase6.0 — Complete callers and inlining

| Caller | Use | Refactor experiment |
|---|---|---|
| private `Roth.exists_mem_RSet_le_index_aux`, MainLemma550, call557 | Select a common pair, subtract into RSet, derive root vanishing, then lower-bound index | Full original module replay removes the named theorem, inserts its entire proof as local collision (using existing caller σ), and leaves caller signature unchanged. |

Proof uses within declaring file:1. External-to-file uses/internal-use count excluding declaring file:0. One docstring reference is not a proof caller. Fresh no-ignore rg and tracked git grep agree; {link('source-search.json')}, {link('tracked-source-search.json')}, {link('callers.json')}. Inline-derivation audit found no separate equivalent proof bypassing this theorem: {link('inline-search.json')}. Canonical kernel-value direct consumer count1; type consumers0. Canonical array derives directly from tracked order, preserving correct private modules, with293 requested/unique/present/values and exact ordered source pre-gate: {link('canonical-consumers.json')}, {link('canonical-snapshot.json')}.

Actual full caller inlining, original signature equality and absence of the original target constant in the new caller value compile cleanly: {link('inline-executed.lean.txt')}, {link('inline-receipt.json')}. All downstream MainLemma bodies are replayed through main_lemma with standard axioms. This is a readability/API signal, not evidence of <=3 mathlib-call composition. The first inline attempt's fresh local universe was rejected and preserved separately; accepted proof specializes the local helper to the caller's variable type.

## Phase6 — Actual composition experiments

1. Direct existing `Fintype.exists_ne_map_eq_of_card_lt` on the full remainder tuple: compile-guarded failure, because the complete polynomial range is not the bounded finite target and hcount counts coefficient arrays, not all polynomials.
2. Encode bounded coefficients and reconstruct: succeeds in standalone mathlib-only polynomialObservations; this requires constructing a subtype function, normalizing cardinalities, obtaining a collision and reconstructing remainders. This is a new helper proof, not <=3 existing mathlib calls.
3. Specialize that own generic helper with `boxFamily_finite`/`ncard_boxFamily`: exact original recovery succeeds, but both the helper and the source-size bridge are not existing mathlib replacements. Low-degree reconstruction itself already exists.
4. Full original caller inlining succeeds, with the full encoding argument retained.

Conclusion: **NOT-COMPOSABLE** under the <=3 existing-mathlib-call criterion for the **entire original theorem**. Abstract finite-map collision is already mathlib; one must not transfer that NO verdict to the polynomial recovery application without accounting for the bridge.

Edge verification is {link('guards-executed.lean.txt')}, {link('guards-receipt.json')}, and the isolated/recovery snippets. Empty J and f=1 genuinely admit a collision with zero degree bounds/B1; B0 yields a singleton and impossible strict budget; zero bounds leave B+1 constants. f=C2 has degree0, so its low-coefficient tests are vacuous, yet nonmonic modByMonic leaves inputs unchanged and full-family collision fails. The guard proves all admissible W are constants, not merely that one chosen pair fails. These are accepted kernel proofs, not informal counterexamples.

## Phase7 — Verdict and actionable future decisions

**BORDERLINE-needs-human**, fully assessed. The specialized theorem is used in a central proof, and its polynomial encoding is genuine work. The generic collision theorem is already in mathlib, while the candidate polynomial observation bridge has a reusable formulation. Evidence supports retaining the Hasse application locally and considering a separate bounded-polynomial observation API; it does not resolve whether a new public helper is the right mathlib API grain. This judgment concerns mathematical interface/audience, not implementation cost or a verification blocker.

'''+ '\n'.join(f'{i+1}. {q}'for i,q in enumerate(questions))+f'''

Next action: retain `Roth.exists_ne_modByMonic_eq` in MainLemma while designing any standalone polynomial observation helper; keep the existing Fintype pigeonhole theorem as the abstract core. If a generic helper is adopted, derive this specialization using the verified recovery and keep `exists_mem_RSet_le_index_aux`'s real-budget interface. No deletion is justified merely by one use. A provisional upstream home would be `Mathlib/Algebra/Polynomial/Div.lean` only if its import layering can support finite counting; a separate `Mathlib/Algebra/Polynomial/Card.lean` may be cleaner. No YES PR/reviewer/grouping recommendation is asserted before that choice. This is independent of earlier246/248 BORDERLINE verdicts.

## Phase8 — Verification and handoff

Accepted original, isolated, recovery, inline and guards are all complete, clean and use standard axioms only. Partial warm-up and three rejected proofs are retained separately; rejected recovery sorryAx is not accepted evidence. No limit raises/new axioms/sorry/unsafe/native_decide. Full exact executed sources are `.lean.txt` with original requests/raw receipts/timings. Fresh17 and exact293 order/unique/present/value checks, current copy-manifest, report links, all15 formal cells, all named literature requests, secret guard and actual scratch plus simulated integrated validation are required by {link('validate.py')} and {link('test_layouts.py')}. See {link('verification.json')}, {link('validation-result.json')}, {link('secret-guard.json')}. Root independently reviews before any production-document integration/publication; acceptance remains pending.
'''
put('report.md',report)
print('PASS report/overview/assessment written; all required keys')
