# Fresh private helper cleanup: `weight_le_delta_aux`

Scope: only this helper and its necessary routine caller proof in `Roth/Theta.lean`; **0 original declarations counted**. No Git, shared report, rename queue, new helper, definition, import, public signature, metadata or documentation changes.

The redundant global positivity hypothesis `hr : ∀ j, 0 < r j` is removed completely. If `r none = 0`, the degree bound forces `d = 0`, and the result is `hδ`. Otherwise `r none > 0`; the ratio hypothesis and `hδ` force every denominator positive. The existing sum comparison then proves the bound. This is stronger than the preliminary point-localization idea, with a two-line zero branch inside the existing helper and no wrapper cycle. The single caller stops forwarding `hr0`; its public hypothesis remains intact. The final cancellation uses a direct order certificate.

## Required reading and baseline

Read both dispatched instruction files; `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, full cleanup workflow, golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and relevant style/naming sections. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Instructions overriding older permission/public API language are honored.

Inherited exact-SHA baseline: source `c1aa9de515850c72246fb7e8ef531937ceaa5616dcbd155f808d00dd2a468691`, 936 lines, public29 body22, weight body11. Complete baseline native LSP `/private/tmp/roth-numeric-helper/final-lsp.json`: success, partial=false, timed_out=false, failed_dependencies=[],0 errors/10 warnings. Accepted final/repeat real profiles at that SHA: weight228.983/191.727ms, mapped637.956/643.007ms, numeric787.045/810.470ms, public29 843.584/839.167ms. These are inherited, not fresh. No duplicate identical baseline request. Prior actual module and compatibility exits0 are recorded in direct-final-gate-status.json. Owner project build and separate LeanEval are separate final owner gates.

First introduction: `/private/tmp/roth-theta-lem6/first-manifest.json`; exact `weight_le_delta_aux-FIRST-with-context.lean` SHA42fd0fa1a1cc283888bc2ab2302cbd2e3d447305add544f8a2118446a7c44340, including original omit. Baseline assigned declaration equals that exact saved first declaration. FIRST-compiled-weight-mapped-full.lean had later numerical errors and is not represented as a clean full compile. This audit independently recompiled the exact FIRST body in a minimal Roth.Index namespace with identical section variable context, independently proves the new form, and reconstructs the full original telescope. Raw first-contract.log exit0 and all pass markers/standard axioms certify that separate proof. The final actual compatibility tail independently rechecks its selected proof after the one-use-have inline. Independent universe names are alpha-bound: actual/fresh types use different generated labels. The final checker enforces equal arity and positional instantiation at the same common level parameters (one universe here), preserving all universe relationships; it does not permit permutations. No production universe changed. Early experiments corrected `(Finsupp.degree_eq_zero_iff d).1` (lemma takes explicit d), and a metaprogram error-message interpolation lacking ToMessageData BinderInfo; neither failed log certifies anything.

## Full24-item audit

| # | Item | Substantive result |
|---|---|---|
|1|Lint|No assigned-helper warning in inherited diagnostics. Ten preexisting public unused-hypothesis warnings remain outside this leaf; no suppressions. Fresh final diagnostics below.|
|2|Have scan|Original hrp has proof content and multiple uses: retain. New single-use hd0 was inlined as a direct zero-case rewrite under rule1.10.|
|3|Set options|None in production, no limit raise. Scratch search uses conservative20k only.|
|4|Simp squeeze|New zero case terminal `simpa [weight] using hδ`, unsqueezed; no nonterminal simp.|
|5|Naming|Descriptive snake_case weight_le_delta_aux, `_aux` private suffix, no banned abbreviation, numeric suffix, source-number pattern or rename.|
|6|Line packing|All3 final signature lines measured below.|
|7|By placement|Every production by remains at preceding line end.|
|8|Format|2-space proof,4-space signatures, no empty body line, semicolon chain, haveI/letI, trailing whitespace or line>100.|
|9|Comments|No original helper proof comments present; all caller comments preserved unchanged.|
|10|Docstring|Private helper has none; public docs untouched.|
|11|Visibility|Private retained, only single in-file caller. No new exported API.|
|12|Structure|11→12 body lines, zero branch2 and positive remainder8;≤30 ordinary cap, all branches≤10, no ∧/∃ packing issue.|
|13|Mathlib|Five actual methods plus clean generic probes below. Uses existing arithmetic/sum lemmas directly; helper contains the complete finite weighted-degree argument, not a 1–3-call wrapper.|
|14|Junk def|n/a: theorem, no definition.|
|15|Exists lemma|n/a: no existential result/witness.|
|16|Show/change|n/a: neither present.|
|17|Push_neg|n/a: absent.|
|18|Generalise|Global hr removed; all effective original/final parameters covered below.|
|19|Inequality|All inequalities already small-side-left; complete signature scan below.|
|20|Normal form|Project's canonical weight and Finsupp.degree; no new equivalence API, custom predicate or definition.|
|21|Syntactic generality|No-hr interface eases application and handles zero radii. Retain independent r/δ ratio rather than reorder d before a support-only hypothesis; no caller benefit warrants that churn.|
|22|Import fanout|n/a: no new import.|
|23|Casts|No redundant new casts: hrp forces ℝ for denominator comparison; all d/r casts bridge ℕ→ℝ; exact_mod_cast handles genuine bridges.|
|24|Instance names|No instance declared/named; DecEq omitted originally and finally; Fintype remains effective.|

Have scan resolution: new single-use hd0 inlined as a direct rewrite by the degree-zero inference; only hrp remains and has proof content and multiple uses in sum/cancellation and ratio positivity. No unnecessary new helper extracted.

## Five actual Mathlib search methods

All remote search calls are recorded in search-results.json, with structured actual responses. Search candidates were never accepted just because a name appeared.

| Method | Actual query / results |
|---|---|
|A Lean-Finder|“sum d_i / r_i bounded by delta when total degree bounded and r_none <= delta * r_i”; returns Schwartz–Zippel root-count estimates, not this statement.|
|B Loogle|`Finset.sum, _ / _ ≤ _`; returns Cauchy–Schwarz, mean inequalities, Schwartz–Zippel, etc., no replacement.|
|C LeanSearch|“finite sum quotients bounded using total sum bound and denominator lower bound”; returns `Finset.sum_div` building block and unrelated infinite sums.|
|D Source grep|Full-name untruncated `weight_le_delta_aux` in mathlib: no hit. Read Finsupp.Weight and arithmetic order files; degree_eq_zero_iff, degree_eq_sum, pos_of_mul_pos_right are useful building blocks. grep-search.log/full-name-search.log.|
|E Name pattern|Actual lean_local_search weight_le found project weight_le_card/weight_le_degree_div plus own target; index reported unavailable, so no absence inference from index. Read weight_le_degree_div in Box: requires a common NAT denominator lower bound; cannot directly express scaled ratio with arbitrary real δ. Own target hit is ignored.|

Auxiliary variants: weight/degree/weight_le/degree_eq_zero and div order/pos_of_mul_pos_left/right. Common-equivalents lookup: no discrete/compact/etc. bucket. No exact Mathlib replacement found; this is a bounded search result, not a global absence theorem. Compiled generic routes: anonymous `exact?` fails to close; `apply?` returns only incomplete generic order transformations then bounded delaboration timeout. `grind`, `aesop`, `simp [weight]` also fail. They run against the exact entire source prefix BEFORE the assigned helper, without current Theta import, later public29, current helper, or named failed trials. automation.log exit1 is deliberately negative evidence, never axiom evidence. All five methods actually ran. Native multi_attempt was not retried because dispatched session evidence shows repeated stalls; ordinary bounded compiler exploration used instead.

## Every effective binder / generalisation

Negative probes were batched in binder-negative.lean against clean exact pre-weight prefix with autoImplicit=false. Exit1 is expected; source ranges/log identify each failed declaration. final-binder-negative.log recompiles every final-form drop after the zero-case inline (expected exit1). Positive first-contract.lean exit0 independently establishes the no-hr strengthening and old adapter. Distinguish unchanged-proof failure from mathematical necessity.

| Parameter | Role | Compiled probe/candidate | Result |
|---|---|---|---|
|τ : Type u|Dependent index type|Replace omitted type by unknown missingType, autoImplicit=false|Fails unknown type; structurally needed in Finsupp/r. Universe polymorphism retained; actual/type/level verification below.|
|[Fintype τ]|Effective finite sum structure|omit Fintype alongside DecEq in same body|Fails cannot omit referenced section instance. Finite alone would require choosing/replacing a Fintype and is a different weight API. Retain.|
|{δ : ℝ}|Real bound/ratio scale|Drop binder|Fails unknown δ in statement/body. General field restatement would replace project's ℝ-valued weight; no scoped API benefit.|
|hδ : 0≤δ|Nonnegative scalar|Drop binder from selected proof|Fails unknown hδ in zero/scalar steps. Counterexamples.lean independently certifies δ=-1, Empty-index d=0 has weight0 not≤δ, so unrestricted deletion is false. Already weak≤.|
|{r : Option τ→ℕ}|Denominators and degree bound|Drop binder|Fails unknown r; dependent data needed.|
|hr : ∀j,0<rj (FIRST)|Global positivity|Original unchanged proof with hr weakened to0≤; point-localized0<rnone; then full deletion with redesigned zero branch|Unchanged-proof variants fail cast/application, not necessity. Full removal COMPILES (candidate2 and selected independent proof); applies, handles rnone0. No wrapper/new helper.|
|hratio : ∀j, ↑rnone≤δ*↑r(some j)|Ratio comparison|Drop binder (both original/selected probes)|Fails unknown hratio; Unit d1, rnone=rsome=1,δ0 shows no unrestricted bound without ratio. Already≤; no strictness to weaken.|
|{d : τ→₀ℕ}|Multi-index|Drop binder|Fails unknown d/degree in statement and proof.|
|hd : d.degree≤rnone|Total degree cap|Drop binder|Fails unknown hd in zero and final comparison. Unit d2, all r1,δ1 shows failure without cap. Already≤.|
|[DecidableEq τ]|Not effective in FIRST/final|Exact omit context and compiled full types|Already omitted, classical local choice only; no production class change.|

Positive counterexamples.lean supplies concrete false conclusions for hδ/ratio/degree deletions separately from deliberately failing proof probes, and #checks every new arithmetic lemma. Support-only hratio would require moving dependent d and complicate the caller's natural global ratio; considered but not recommended/applied. No conclusion weakening, result still weight≤δ, no new hypothesis or universe restriction.

Private literature exemption: n/a, private declaration; public literature search not required. No external-source absence claim is made. Inversion check: the only named construction is the project's generic weight, unfolded into a finite sum; no named special witness. Abstracting to an arbitrary sum/ordered field would duplicate this argument plus conversions, have no additional consumer, and would introduce a one-use wrapper; no extraction recommended. The helper remains parametric over arbitrary finite τ and arbitrary r,d,δ.

## Signature line packing and inequalities

`#check @generalWeight` at format.width100 is printed in first-contract.log and the actual full type appears in final compatibility. All3 final codepoint widths:

| Sig line | Chars | Next complete binder/conclusion | Arithmetic | Result |
|---|---:|---|---|---|
|481|73|`(hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j))` (45)|73+1+45=119>100|ok|
|482|89|`weight (r ∘ some) d ≤ δ := by` (29)|89+1+29=119>100|ok|
|483|33|none, proof follows|n/a|ok|

Every final signature inequality occurrence:

| # | Location | Inequality | Action |
|---|---|---|---|
|1|hδ|0≤δ|already correct|
|2|hratio|↑rnone≤δ*↑r(some j)|already correct|
|3|hd|d.degree≤rnone|already correct|
|4|conclusion|weight(r∘some)d≤δ|already correct|
|5|reversed-orientation scan|zero ≥ or > in signature/body|no rewrite/rename|

Original hr strict 0<rj is removed with the whole redundant binder. New body hrp uses0<↑rnone; all comparisons remain canonical. Names contain no _ge_/_gt_.

## All42 golfing rules

| Rule | Status |
|---|---|
|1.1 by exact|n/a: no wrapper|
|1.2 by rfl|n/a: rfl is a calc equality certificate|
|1.3 rw+exact→rwa|Original final rewrite+exact replaced by direct `(div_le_iff₀ hrp).2` certificate|
|1.4 simp+exact|Applied terminal simpa using hδ in zero case|
|1.5 trailing rfl|n/a: no simp/rfl chain|
|1.6 constructors|n/a: no conjunction|
|1.7 apply+exact|Direct order/mul certificates already used|
|1.8 by_contra!|n/a: no contradiction proof|
|1.9 eta reduction|n/a: sum lambda contains actual reasoning|
|1.10 have inline|Applied to hd0: direct rewrite, no new one-use have; hrp is multiply used proof content|
|1.11 refine+fun|n/a: no apply/intro chain|
|1.12 redundant show|n/a: none|
|1.13 obtain|n/a: no projected conjunction/existential|
|1.14 merge rw|Each rw already has a single merged list|
|1.15 terminal simp|Zero case unsqueezed terminal simpa; no squeezed terminal simp|
|1.16 nonterminal simp|n/a: none|
|1.17 dot notation|`hrp.trans_le`, `(div_le_iff₀ hrp).2` used|
|1.18 <\| syntax|n/a: no disposable final parentheses in production application|
|1.19 push Not|n/a: no push_neg|
|1.20 ∃ inline|n/a: no existential helper|
|2.1 grind|Actual clean-prefix whole-goal attempt fails; retained deterministic sum proof|
|2.2 grind subsumption|n/a: no grind in selected proof|
|2.3 simpa consolidation|Applied zero branch terminal simpa|
|2.4 fun_prop|n/a: no analytic regularity proposition|
|2.5 positivity|Actual local-automation.lean fail_if_success positivity confirms it does not infer denominator positivity from hratio; use direct pos_of_mul_pos_right certificate. hrp cast direct from Nat.pos_of_ne_zero.|
|2.6 gcongr|Actual local scalar gcongr probe succeeds. Keep equally short direct mul_le_mul_of_nonneg_left certificate; avoids automation for a one-lemma step|
|2.7 lia/omega|Actual local Nat degree-zero lia probe succeeds. Keep direct Nat.eq_zero_of_le_zero certificate; caller existing lia unchanged|
|2.8 aesop|Actual clean-prefix whole-goal attempt fails|
|2.9 norm_num/cast|exact_mod_cast retains genuine Nat/Real bridges; no concrete numerical normalization needed|
|2.10 decide|n/a: symbolic arbitrary-real inequality, no finite computation|
|2.11 field_simp/ring|n/a: inequality, positivity required; direct division-order equivalence|
|2.12 linear_combination|n/a: no ring/ring_nf ending|
|2.13 wlog|n/a: asymmetric zero versus positive radius, not symmetric cases|
|2.14 calc collapse|Four distinct sum comparison/identity/cancellation stages; preserve mathematical outline|
|2.15 <;> duplicate goals|n/a: no repeated goal branches|
|3.1 erw|n/a: none|
|3.2 fun_prop legacy|n/a: no continuity/measurability tactic|
|3.3 omega→lia|n/a: no omega introduced or present in helper|
|3.4 rcases rfl|n/a: no such pattern|
|3.5 attributes|No global automation attribute justified on a private weighted bound|
|3.6 simp_all|n/a: no simp_all only|
|3.7 limits|Production has no maxHeartbeats/maxRecDepth/profiling option; zero raises|

## Holistic simplify / independent proof and actual contracts

The whole-proof automation attempts show no one-tactic replacement; the chosen proof states the zero case, then sums termwise scaled denominator bounds and cancels the positive distinguished radius. No repeated skeleton, circular helper, shared witness split, new constant or API extraction signal remains. The original one-use weight helper itself contains the substantial weighted-degree estimate needed by public29; retaining it keeps the caller short. Simplify API is unavailable; this direct holistic pass follows the workflow and found the no-hr generalisation implemented above.

Compatibility source copies `/private/tmp/roth-numeric-helper/actual-compatibility-final.lean` as an immutable byte prefix, including BOTH original independent public29/public30 proof blocks and their full telescope/value/BinderInfo/names/standard-axiom checks. Accepted source name corrected by coordinator (dispatch had accidentally inferred a nonexistent direct-*.lean from a log prefix). compatibility-provenance.json records prefix SHA/bytes. The appended tail independently repeats the exact FIRST weight proof, proves selected no-hr form, builds an explicit full FIRST λ adapter dropping only hr, compares actual built private suffix/type/BinderInfo/user names/universes and proves actualRecovery by proof irrelevance. All values use `value! true` and axioms restricted to propext/Classical.choice/Quot.sound. Existing immutable prefix also verifies ALL retained new helpers and deleted coeff_det_le_lem6M_aux absence. Anonymous synthetic instance names may differ as authorized; user argument names/order/BinderInfo/types retained.


## Fresh final performance / buzz

REAL Lean4.34 command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`. The final/repeat source is the exact entire production prefix through public29, retaining every preceding import/declaration/context, closing **end Lemma6 then end Roth**. No current-Theta import shortcut, profiling scaffold, limit raise, masking or inner-node doublecount. All normal compiler/build/LSP requests were terminal before the first trace; traces ran sequentially. These are prefix-only performance certificates, not claims about the later file declarations or owner whole-module sweep.

Totals sum the actual declaration's outer Elab.command plus associated disjoint top-level Elab.async proof/kernel/addDecl/linter work. Nested timings are excluded; exact raw node anchors are preserved in the timings JSON and logs.

| Declaration | Inherited baseline ms (first/repeat) | Fresh final ms | Required repeat ms | Final outer/proof log lines | Repeat outer/proof lines |
|---|---:|---:|---:|---|---|
| weight_le_delta_aux | 228.983 /191.727 | **336.843** | **356.888** | 1088012 / 1088042 | 1088920 / 1088950 |
| mapped_det_ne_zero_aux | 637.956 /643.007 | **661.006** | **664.630** | 1135469 / 1135572 | 1136348 / 1136451 |
| index_numeric_bound_aux | 787.045 /810.470 | **941.689** | **875.463** | 1237845 / 1237890 | 1238673 / 1238718 |
| index_le_lem6 | 843.584 /839.167 | **951.482** | **856.651** | 1346072 / 1346154 | 1345698 / 1345780 |

final-profile.log: exit0, 172.254117459s wall, 154207756 rawUTF8 bytes; prefix SHA `e24542061e94411a02ff2cc51fde913874a89c792bb4b4f069b1b0e09e418b7a`; live/full source SHA `aad8c2999fcfb469c9d3cf75ed3913884d3797923abf8d6653c2b9c67e0d82fc`.

repeat-profile.log: exit0, 173.398017750s wall, 154185466 rawUTF8 bytes; prefix SHA `e24542061e94411a02ff2cc51fde913874a89c792bb4b4f069b1b0e09e418b7a`; live/full source SHA `aad8c2999fcfb469c9d3cf75ed3913884d3797923abf8d6653c2b9c67e0d82fc`.

The first CURRENT-final-SHA timings were inspected before the second invocation; at least one≥750ms requires the same-SHA repeat. The sequential repeat driver would skip if all four were below750. All4 pass1000ms in both current runs. No performance improvement is claimed from removing a hypothesis; the mathematical strengthening is the benefit and its cost remains below budget. Buzz outcome **FAST-BOARD** for this leaf/all4 measured targets. Added/removed maxHeartbeats raises0, no timing deferral or new helper.

## Final gate status

| Gate | Result | Concrete evidence |
|---|---|---|
|final-module-build|PASS|Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,35.605022208s on current SHA; final-module-build.log|
|actual-compatibility-final|PASS|Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-weight-helper/actual-compatibility-final.lean` exit0,66.371782833s on current SHA; actual-compatibility-final.log|
|Independent FIRST/old full adapter|PASS|Exact old proof independently recompiled; final actual tail repeats it. Full telescope/BinderInfo/ordinary names/conclusion and one positional universe checked, explicit λ drops only hr.|
|Actual values/standard axioms|PASS|All actual new helpers plus FIRST/general/oldAdapter/actualRecovery checked using value!true; only propext/Classical.choice/Quot.sound. Deleted coeff_det_le_lem6M_aux absence verified.|
|Definitions/public statements|PASS|No def/abbrev/import/public header/visibility/doc change. Exact raw public headers invariant, plus actual original29/ENTIREoriginal30 type/value/independent proof checks; hq retained.|
|Structure|PASS|Weight body12≤30; zero branch2/positive remainder8≤10; caller body22≤30; no new helper.|
|Naming|PASS|Descriptive private `_aux`, no forbidden pattern/abbreviation; no rename.|
|Line packing|PASS|All3 codepoint-width rows and complete-next-group arithmetic above; max bodyline95.|
|Inequality|PASS|All4 final signature inequalities scanned; zero≥/> in code.|
|Scope/caller effects|PASS|Only assigned helper and one necessary caller argument changed; current module compiles; actual old public telescopes and ENTIREold30 independently compile.|
|Fresh final native LSP|PASS|Complete unfiltered success,partial=false,timed_out=false,deps=[],0errors/10 inheritedwarnings; final-lsp.json.|
|Fresh real all4 profiles|PASS|Both exact global prefixes exit0 same current SHA; required≥750 repeat honored, each target<1000ms.|
|Owner full build / separate LeanEval|PENDING OWNER|Not run or claimed by this private audit; after all fresh private audits, owner performs full build then separate LeanEval.|
|Queued public29 boundary revisit|PENDING OWNER, NOT THIS LEAF BLOCKER|Live public29 still strict δ/rp10δ and approved weak hratio/DecEq drop; hq retained. Separate dedicated approved boundary revisit follows current29 batch/push.|

Ten native warnings retained: header metadata at1 (user preserved), unused public hr/hB at93/101/109/129/252, retained hq at547, old30 DecEq warnings at576/579. No assigned helper warning, new suppression or warning hidden. The parent controls the retained public hypotheses and later original30 audit.

## Eleven-step checklist

- [✓] Step1: required skills/workflow/reference reading.
- [✓] Step2: all24 substantive audit items, have/simp/comment scans.
- [✓] Step2.5: all5 ACTUAL Mathlib search methods and clean generic compiler probes; bounded limitations documented.
- [✓] Step2.6: every effective FIRST/final binder compiled drop/weakening coverage; positive no-hr strengthening, counterexamples; private literature exemption and inversion check.
- [✓] Step2.7: every signature line's codepoint packing arithmetic.
- [✓] Step2.8: every inequality occurrence and reversed orientation scan.
- [✓] Step3: all42 golfing rules and actual relevant automation trials.
- [✓] Step4: whole-proof/term/helper alternatives, holistic simplify and direct order proof assessed.
- [✓] Step5a: fresh COMPLETE unfiltered final native diagnostics.
- [✓] Step5b: actual build, unchanged-public/protected definitions, FIRST/full-old/ENTIREold30 values, standard axioms, structure/name/packing/inequality and real performance gates.
- [✓] Step6a: no rename needed; no queue/sidecar/Git mutation.

Overall **PRIVATE HELPER PASS**, contribution **0 original declarations**. Source936→937 lines (+1); body11→12, mathematically stronger; no new helpers, all original caller comments/docstrings preserved. No public API edit. All source edits are now **frozen/revoked**, and all compiler/LSP/profile requests are **terminal/drained**.

Final source SHA256: **`aad8c2999fcfb469c9d3cf75ed3913884d3797923abf8d6653c2b9c67e0d82fc`**. Detailed raw evidence and manifests: `/private/tmp/roth-weight-helper/`. Owner full build/separate LeanEval and remaining fresh helper audit remain owner work.


Owner handoff note: the leaf saved this complete report and freeze-manifest.json, including
exit0 repeat results and explicit source revocation/request drainage, before its final chat
response failed because the selected model was at capacity. The owner read the full report,
checked the completed raw repeat/manifest and accepted the finished audit; the model-service
error is not represented as a missing compiler gate or a successful final chat response.
