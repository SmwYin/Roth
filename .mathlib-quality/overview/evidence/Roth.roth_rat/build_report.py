from pathlib import Path
import json
D=Path(__file__).resolve().parent;N='Roth.roth_rat'
def rd(n):return json.loads((D/n).read_text())
def link(n):return f'[{n}](../evidence/{N}/{n})'
def table(headers,rows):return '| '+' | '.join(headers)+' |\n|'+'|'.join('---'for _ in headers)+'|\n'+'\n'.join('| '+' | '.join(str(c).replace('|','∣').replace('\n',' ')for c in r)+' |'for r in rows)
p=rd('phase-checks.json');lit=rd('literature.json');native=rd('native-type.json');ver=rd('verification.json')
r='''# Roth.roth_rat — canonical289

**Verdict: YES-but-generalise-first — LITERATURE-WEAKENING.** Keep the named rational-value endpoint with the Roth theorem contribution package, and remove its unnecessary `Irrational α` binder. This is an independently assessed mathematical endpoint, although its current proof is a short representation transfer. No production source or pin changed.

## Phase0 — Baseline and scope

The public theorem resolves at `Roth/Main.lean:581–586`. All588lines of Main and all66lines of LeanEval were read. There are no actual proof/type callers of this endpoint. The focused original replay copies the exact target only, renaming it into `Roth289Original.replay`, opening the original namespaces; no private helpers are needed. Unrelated Main declarations are imported, not redundantly re-elaborated.

Fresh17 source/pin hashes agree with the shared clean2467-job baseline. At this Main file boundary root additionally executed literal `lake build`: exit0,6833.895ms,0warnings,2026-10-29 21:14:57–21:15:04UTC. Its log hash is `b7f96a04d807f93a54c01314b6f59b969256b6222dffa7ae4b62832d3a174e65`. Final293 dualbuild gates belong to root separately.

Evidence: LINKS_BASE.

## Phase1 — Comprehension

For a fixed irrational algebraic real α, if infinitely many distinct rational numbers x satisfy |α−x|<den(x)^(−κ), then κ≤2. The exponent is an arbitrary real, and `x.den` is the positive denominator of the canonical reduced fraction. Distinct rational values, rather than arbitrary integer/natural representations, are being counted.

The map x↦(x.num,x.den) is injective by `Rat.ext`. Its image of the infinite good rational set is therefore infinite. `Rat.den_pos` and `Rat.cast_def` put every image pair in `Roth.approxSet`; the actual `Roth.roth` then bounds κ. Those set/cast operations supply representation transport; they do not supply the algebraic exponent-two theorem.

Full fresh kernel type, obtained through `Lean.getConstInfo` and tagged `pp.funBinderTypes`:

```lean
TYPE
```

The loaded kernel body directly mentions `Roth.roth` and `Roth.approxSet`; only `Roth.roth` is lexically explicit in the written target. No project constant occurs in the type. Transitive parent proof dependencies are not conflated with direct references. The original kernel printer elides18826characters; this is **not** a complete body dump. The exact complete written proof, full kernel type, complete used-constant lists, standard axioms and complete canonical value audit remain available. The proof equality check confirms exact original/replay type agreement by proof irrelevance, not construction identity.

Evidence: LINKS_ORIGINAL.

## Phase2 — Preliminary checks

**BIG:** a named Roth theorem and explicitly listed Main result. Its five proof lines do not make the endpoint mathematically small. One-line definition test: n/a, this is a theorem. Definition barrier/diamond/API exemptions: n/a. No prefilter or parent verdict was inherited.

## Phase3 — Exhaustive literature

All named channels were actually checked, including three distinct general queries and a separate nCatLab namespace query. Optional `ask_chatgpt_math` is unavailable. Local `clean.tex` §6 states the unreduced-pair theorem with irrationality; §7 proves it. The all-algebraic rational-value formulation appears directly in Fukshansky, *Geometric Number Theory*, Theorem4.5.1, printed p67 / physical PDF page71 (zero-based70), lines5063–5095: only finitely many reduced rationals at exponent2+δ. This is the relevant standard generality.

LIT_TABLE

The nLab open failed with400 unsupported XHTML; the dedicated Stacks/nCatLab queries returned empty. These are access/search outcomes, not proof of absence. The publisher request for Roth1955 redirected from PDF to HTML; no complete original-paper proof was accessed there. The primary lecture theorem and local manuscript supply the statement evidence. Recent arXiv results were inspected at their dated abstracts: Hindes(19Sep2022) explicitly cautions that characteristic-p Roth fails; Salami(13Oct2026) studies weighted heights and distinguishes a proved pullback exponent from a conjectural coprime refinement. Neither licenses blindly changing this real/rational theorem's field or denominator.

Primary citations: [Fukshansky, Theorem4.5.1](https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2019/m195/GNT_lecture-notes.pdf), [Roth1955 publisher record](https://www.cambridge.org/core/journals/mathematika/article/abs/rational-approximations-to-algebraic-numbers/9B22B10EFDE4FFC405FCAAFB12C67D3C), [Hindes2022 abstract](https://arxiv.org/abs/2209.09182), [Salami2026 abstract](https://arxiv.org/abs/2610.17589).

Evidence: LINKS_LIT. Exact web requests, returned SHA256/byte lengths/status and clean title/URL metadata are archived; no third-party article/search-result bodies are persisted. Out-of-scope/truncated returned URLs were omitted, query strings stripped. Search-engine crawl dates were not treated as publication dates.

## Phase4a–b — Generality

GEN_TABLE

**STRICTLY NARROWER THAN STANDARD: one verified hypothesis drop.** The proposed endpoint is:

```lean
theorem roth_rat {α : ℝ} (halg : IsAlgebraic ℚ α) {κ : ℝ}
    (hinf : {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite) : κ ≤ 2
```

For κ>2, denominator≥1 and real-exponent monotonicity enlarge the good set into the exponent2 good set. The pinned `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational` then infers irrationality of α, permitting the exact original Roth endpoint to finish. This uses existing rational-center finiteness through that iff; it does not re-prove integer separation. At κ≤2 the conclusion is immediate. Rational algebraic targets are thus admitted without changing approximation semantics.

The mathlib-only `generalize` proof is explicitly conditional on `hR`, whose type is exactly the original all-target endpoint schema. The actual original hR is re-elaborated and type-agreed separately in the project context. This is a compiled implication from the verified original theorem, not a claim that isolated mathlib already proves Roth. `recover` restores the original signature. The rational-center edge additionally proves finiteness for every κ≥2. No proposed field/typeclass widening or C>1 strengthening is claimed verified.

Evidence: LINKS_GENERAL.

## Phase4c — Modern mathlib idiom

MODERN_TABLE

The finite bad-set endpoint is the natural arithmetic statement. Its exact cofinite reformulation supplies a non-strict lower bound outside finitely many **rational values**. The compiled `cofinite_consequence` combines two such exponent bounds by `Filter.Eventually.and`; recovery produces the original exponent implication. These are useful equivalent interfaces, not a stronger asymptotic result. The two-line `simp only [eventually_cofinite, not_le]` proves only the logical bridge, and would be a trivial simp composition if assessed on its own.

The current `LiouvilleWith` source was also read and searched: its existential constant, frequently-atTop denominators, exclusion of equality, exponent monotonicity, positive-witness normalization, exponent-gap and rational affine invariance are relevant to a larger coherent package. No new LiouvilleWith import was authorized or executed here, and no rational-value/LiouvilleWith equivalence is claimed. The existing Liouville polynomial-degree lower bound is weaker than Roth's universal exponent2 bound. LeanEval's strict uniform positive-C lower bound additionally requires irrationality and is not the cofinite statement.

Evidence: LINKS_MODERN.

## Phase4.5 — Infrastructure risks

RISK_TABLE

Overall n/a: theorem, no definition/class/instance. No new coercion or instance was proposed.

## Phase4.6 — Proof strategy

STRATEGY_TABLE

**REFACTOR-RECOMMENDED for the public statement:** retain the canonical rational injection, infer irrationality only in the κ>2 branch, and offer finite/cofinite interfaces. No new abstraction should hide the actual Roth theorem behind a supplied desired conclusion. The original proof is mathematically sound; the issue is its unnecessary binder, not its shortness.

## Phase5 — Fifteen formal search cells

Current = original rational Infinite implication; standard = finite rational values for all algebraic targets; abstract = cofinite rational lower bound. All five methods were executed on each form. Remote snapshots can differ from the pin; every positive candidate used in proofs was checked against pinned source and natively checked.

FORMAL_TABLE

The current and standard local queries returned one result each with `index=error`; cofinite returned seven with `index=error`. The earlier Liouville local query returned forty with `index=warming` and is retained as supplementary evidence. None supports a negative index inference. Finder/Search found Dirichlet, rational-center finite bounds, Liouville APIs and metric results, not a verified algebraic Roth bound. Loogle current and supplementary Liouville patterns were empty; standard found the rational-center theorem, abstract found cofinite generic bridges. Full-name source search was untruncated across all Mathlib; thematic rg covered NumberTheory plus the filter form.

Pinned relevant candidates:

- `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, DiophantineApproximation/Basic:253: rational target, exponent2, inequality in ℚ. It is not Roth for algebraic irrational reals.
- `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational`, same:277: real-target characterization, used to infer irrationality above exponent2 by set inclusion.
- `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, same:197: Dirichlet sharpness at exponent2, opposite direction to finiteness above2.
- `Filter.eventually_cofinite`, Order/Filter/Cofinite:49: finite-exception transport, no arithmetic lower bound.
- `Liouville.exists_pos_real_of_irrational_root`, Transcendental/Liouville/Basic: polynomial-degree lower bound, not exponent2 independent of degree.

Evidence: LINKS_SEARCH.

## Phase5.5 — Statement shape

SHAPE_TABLE

The main arithmetic assertion must still be supplied; generic finite/infinite/cofinite equivalences are not replacements for it. The finite/cofinite RHS convention agrees with the existing filter API. Original type agreement and original-signature recovery are executed, not inferred from textual similarity.

## Phase6.0 — All callers and inline audit

| Scope | Count | Evidence and disposition |
|---|---|---|
| Explicit proof callers, same/other files |0| Fresh no-ignore rg plus tracked git grep; only declaration and module-doc mention occur. |
| Explicit type callers |0| Full source inventory/canonical metadata cross-check. |
| Direct canonical kernel value/type consumers |0/0| Fresh exact ordered293 names,293unique,293present,293values; no consumer marker emitted. |
| Inline re-derivations bypassing this endpoint |0| Main pair/integral theorems and LeanEval bound have distinct domains/statements; full Main/LeanEval read. |

No actual caller exists to inline; caller-body verification is therefore justified n/a. A separate fresh `inline_endpoint` reconstructs the original endpoint from the exact canonical-map proof and actual `Roth.roth`, retains the original full signature and passes type equality; its loaded opaque value is target-free. This is a construction audit, not an invented downstream caller. There is no claim about arbitrary external consumers, simp closure or full transitive dependency traversal.

Zero internal uses do **not** establish deadness: `roth_rat` is expressly documented as a user-facing Main result, giving downstream users native rational values and canonical reduced denominators. Keep that endpoint in the coherent contribution package.

Evidence: LINKS_CALLERS.

## Phase6 — Composition and duplication

Attempt1 uses `Set.Infinite.image`, injectivity from `Rat.ext`, `Set.Infinite.mono`, positivity and `Rat.cast_def`. This transports the premise to pairs, but cannot prove κ≤2 without `Roth.roth`. The latter is a project theorem, not an existing mathlib building block. Thus the five-line source proof is not a ≤3-existing-mathlib-call proof of the endpoint.

Attempt2 uses the pinned rational-center finite theorem/real iff: it infers irrationality, but still cannot bound algebraic irrational approximation exponents. Attempt3 uses existing Liouville lower-bound API: its degree-dependent exponent cannot specialize to universal2. In the isolated accepted general02 source, both `exact?` and `aesop` were required to fail on the actual original arithmetic goal; no resource limits were raised. These unsuccessful routes do not prove universal library absence, but prevent treating the located generic candidates as a verified replacement.

**NOT-COMPOSABLE from current mathlib.** The cofinite logical bridge itself composes by simp; that fact does not downgrade the missing Roth endpoint.

| Decl A | Decl B | Same statement? | Same proof? | Action |
|---|---|---|---|---|
| roth_rat | Roth.roth |No: rational values vs unreduced pairs|Canonical injection plus actual parent theorem|Group as theorem and rational-value corollary; pair hα remains.|
| roth_rat | Roth.roth_of_isIntegral |No: algebraic target vs integral/pairs|Additional reduction plus representation transport|Keep related endpoint corollaries in one staged package.|
| roth_rat | LeanEval.thueSiegelRoth |No: exponent implication vs strict uniform positive-C lower bound|Finite minimum/exponent-gap bridge needed|Do not conflate cofinite rational bound with uniform pair bound.|
| rational-center finite | Rat finite exponent2 |Yes up to casts/exponent monotonicity|Existing mathlib supplies it|Reuse pinned iff; no independent new separation theorem needed.|

## Phase7 — Actionable verdict

**YES-but-generalise-first**, reason **LITERATURE-WEAKENING**: drop `Irrational α`, retaining an original-signature corollary. This is a real compiled binder weakening, not a wholesale foundation change or cost-based choice. Modern finite/cofinite spellings improve application but are not the justification for claiming new arithmetic content.

**Why add this endpoint:** mathlib's DiophantineApproximation/Basic already exposes good rational approximation sets and Dirichlet exponent2 infinitude; its rational-center finite theorem closes the easy branch. Its LiouvilleWith module explicitly describes exponent>2 algebraic exclusion as the Thue–Siegel–Roth theorem. The concrete missing bridge is the algebraic irrational exponent-two bound, proved by this project's parent theorem. Users working with `ℚ` should be able to obtain finiteness at exponent>2 without manually constructing integer pairs or unnecessarily proving irrationality. The named rational endpoint belongs with that mathematical contribution, not in an isolated PR selling its cast conversion as new mathematics.

Proposed exact home: `Mathlib/NumberTheory/DiophantineApproximation/Roth.lean`, as a new leaf above the existing Basic and staged Roth proof modules. Proposed PR title: **feat(NumberTheory/DiophantineApproximation): Roth bounds for algebraic real rational approximations**. Namespace/naming can follow the surrounding `Real` endpoint conventions.

Grouping was checked against the current accepted progress snapshot: `Roth.roth` and `Roth.roth_of_isIntegral` are accepted YES-but-generalise-first, and `Roth.main_lemma` accepted YES-add-as-is. Their underlying proof/API work should be staged coherently; this endpoint is a corollary in the culminating theorem PR. `Roth.reduction` is accepted BORDERLINE, so it is not falsely advertised as an independently accepted YES companion. No earlier verdict was inherited here.

Pre-PR actions: `/generalise Roth.roth_rat` to remove hα using the verified branch; `/cleanup Roth/Main.lean Roth.roth_rat` before migration; preserve original recovery and finite/cofinite interfaces. For recent relevant reviewer evidence, pinned git history records Yaël Dillies' rational coercion change483ba09b(16Jun2026), Andrew Hendel's DiophantineApproximation reference correction834e5169(12May2026), and Marcelo Lynch's direct-file cleanupf01aa345(11Aug2026). Ask a number-theory reviewer such as original DiophantineApproximation author Michael Stoll for mathematical placement, with Yaël Dillies suitable for the rational-cast/API review; authorship and recent commit evidence are distinguished, not treated as proof of availability.

No production deletion/refactor was performed. The endpoint stays locally in Main until its parent theorem contribution is migrated. No user checkpoint or future upstream taste question is needed to complete this read-only assessment.

## Phase8 — Evidence integrity and completion gate

Root owns every native/LSP/build execution; the worker prepared immutable source/hash/request files and inspected raw returned receipts. Disk9 and fixed18 prefixes are byte-preserved; the only authorized extra isolated import is genuine pinned DiophantineApproximation.Basic, giving19imports and hash`9b1bd511ef007f620a7163c38b76aaf650486373cce45b2a4b108b5c1d83583e`.

NATIVE_TABLE

General01 is rejected for a set-membership elaboration error and recovered sorryAx. Shape01 is rejected despite success=true: an informational PANIC from `ConstantInfo.value!` invalidated its target-free audit. Shape02 explicitly uses `value? (allowOpaque := true)` with a missing-value failure and succeeds without PANIC. Rejected exact source/raw receipts remain immutable. Standard axioms only: propext, Classical.choice, Quot.sound. No sorry, new axiom, unsafe/native_decide, partial accepted result or raised resource limit.

Syntax credit: accepted287 shape2's finite/infinite duality proof and zero-pair construction were adapted with fresh rational-domain mathematics and fresh execution; rejected old archives were not templates. General02 supplies the genuinely new compiled hypothesis-drop implication; existing pinned rational-center/Dirichlet/filter APIs remain separately identified.

Current copy-manifest validates every artifact hash/byte size in scratch and simulated integrated layouts, including report links and exact293 source order/private modules. The completion gate holds completed=false/phase8pending until actual draft validators and secret guard PASS; completion is then set true and final current-manifest/layout checks run again. Historical worker manifests never replace the current manifest. Root acceptance stays pending until independent review. Exact executed sources, raw receipts, copied prefixes and copied source excerpts are preserved; only authored preparation/report text is normalized.

Evidence: LINKS_FINAL.
'''
r=r.replace('TYPE',native['full_type'])
r=r.replace('LIT_TABLE',table(['Channel','Actual query','Finding'],[[x['channel'],x['query'],x['finding']]for x in lit['channels']]+[['Local references','clean.tex §6/§7','Read original manuscript reduction and proof, archived excerpts.'],['Optional ChatGPT','standard form/generality/history query unavailable','ask_chatgpt_math tool absent; documented skip.']]))
for marker,key,headers in [('GEN_TABLE','generality',['Parameter','Disposition','Evidence']),('MODERN_TABLE','modern9',['Question','Applies','Concrete result']),('STRATEGY_TABLE','proofstrategy5',['Question','Applies','Alternative']),('SHAPE_TABLE','statement_shape3',['Check','Verdict','Evidence'])]:r=r.replace(marker,table(headers,p[key]))
r=r.replace('RISK_TABLE',table(['Risk','Status','Reason'],[[x['risk'],x['status'],x['reason']]for x in p['infrastructure_risks']]))
r=r.replace('FORMAL_TABLE',table(['Form','Finder','Loogle','LeanSearch','rg','local'],[[f,*[link(f'formal-{f}-{m}.json')for m in ['leanfinder','loogle','leansearch','rg','local']]]for f in ['current','standard','abstract']]))
r=r.replace('NATIVE_TABLE',table(['Accepted source','Raw receipt','ms','Scope'],[[link(x['source']),link(x['receipt']),x['elapsed_ms'],x['label']]for x in ver['accepted']]))
links={'BASE':['inputs.json','baseline-build.txt','file-end-build.json','file-end-lake-build.log','source-Main.lean.txt','source-LeanEval.lean.txt'],'ORIGINAL':['original-executed.lean.txt','original-receipt.json','native-type.json','project-dependencies.json','canonical-consumers.json'],'LIT':['literature.json','literature-local.json','web-batch0.json','web-batch1.json','web-batch2.json','web-batch3.json','web-batch4.json'],'GENERAL':['general2-executed.lean.txt','general02-receipt.json','edges-executed.lean.txt','edges01-receipt.json'],'MODERN':['modern-executed.lean.txt','modern01-receipt.json','mathlib-source-0.lean.txt'],'SEARCH':['formal-search-matrix.json','full-name-search.json','mathlib-inputs.json'],'CALLERS':['callers.json','source-search.json','tracked-source-search.json','inline-search.json','shape2-executed.lean.txt','shape02-receipt.json'],'FINAL':['verification.json','phase-checks.json','prefix-controls.json','prefix-authorization.json','reviewer-specific-commits.json','progress-snapshot.json','validate.py']}
for k,ns in links.items():r=r.replace('LINKS_'+k,', '.join(link(n)for n in ns))
assert 'LINKS_'not in r
(D/'report.md').write_text('\n'.join(x.rstrip()for x in r.splitlines()).rstrip()+'\n')
print('Detailed report written',len(r.split()),'words')
