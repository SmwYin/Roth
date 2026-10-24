# Local necessary helper audit — weighted product bound

Status: FINAL — locally accepted helper lifecycle complete; no original/project completion credit or separate publication.

# Necessary weighted-product helper: initial audit

Binding: entry-binding.json verifies exact saved 29-line declaration, 24 body lines, before any helper Lean/golf. First native original compile exit 0; complete LSP diagnostics show no helper warning and only pre-existing header/hQ/hc warnings. OldWeighted is the exact unchanged source prefix through the helper, namespace closed. Its first successful build is old-build-v2 (initial missing -R invocation failed before elaboration); actual original family enumeration is old-enumeration-v2, before row guards: one opaque theorem `_private.OldWeighted.0.Roth.abs_prod_pow_le_rpow_weight_aux`, actual universes `[]`.

All binding cleanup.md/cleanup-all.md, installed Lean/mathlib skills and mandatory golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, style-rules, naming-conventions, mathlib-review-stages, profiling, buzz references read. This is the dedicated independent helper worker; no subagents. Built-in simplify unavailable; manual holistic review required, no invocation claimed.

1. LINT: none in helper; expected out-of-scope header/parent warnings retained.
2. HAVE: hqR has explicit proof content inside its lambda, used 4 times; keep. hq1 has proof content, used once; keep (can inline safely but no necessary benefit).
3. SET_OPTION: none, actual defaults remain required.
4. SIMP: one explicit simp_rw for rpow multiplication; no bare nonterminal simp or terminal squeezed simp.
5. NAMING: propose `abs_prod_pow_le_rpow_of_le_weight`, describes conclusion and actual lower-weight hypothesis; private visibility retained. Dedicated scoped name edit authorized by binding task, shared rename queue forbidden.
6. PACKING: current signature widths 82,60,41,77,85. Second line can absorb hx (60+1+37=98); then hqr/d/c and hw must repack. Final complete table will be measured before gates.
7. BY: attached to final signature line.
8. FORMAT: no empty lines or haveI/letI. Sum_congr four-line block can become `exact congrArg _ (Finset.sum_congr rfl fun j _ ↦ by ring)`; preserve math and readability.
9. COMMENTS: zero original inline comments. Add only ordinary explanation of denominator-growth estimate, no private docstring.
10. DOCSTRING: private helper, none appropriate.
11. VISIBILITY: private retained; helper not separately published.
12. STRUCTURE: 24 body lines, four calc branches of 5/4/6/4 lines; no conjunction. Compression gives 21 body lines, all branches <=10.
13. MATHLIB: A LeanFinder weighted monomial product/exponent query gives power-mean bounds, no replacement. B Loogle `Real.rpow, Finset.prod` gives no hits. C LeanSearch product-of-powers/negative monotonicity gives Real.rpow_mul and antitoneOn_rpow_Ioi_of_exponent_nonpos. D direct full-name/variant source search in Pow/Real and ordered Finset APIs finds rpow_sum_of_pos, rpow_sum_of_nonneg, rpow_le_rpow_of_nonpos and generic product monotonicity; these are the building blocks already used. E name search rpow_sum finds the existing power/sum API; initial index unavailable then warming, so no false absence claim from index. Actual goal exact? fails; apply? offers partial logarithm/order reductions, not an exact replacement. Whole grind fails; simp/aesop leave the power estimate. Earlier misplaced attempts on signature line 345 are invalid, excluded. No matching common-equivalents bucket. Keep necessary nontrivial estimate built from generic library facts.
14. JUNK DEF: n/a, theorem.
15. EXISTS: n/a, no existential conclusion.
16. SHOW: none.
17. PUSH_NEG: none.
18. GENERALISE: all binders reviewed below; already enough for caller. No optional ambient loops.
19. INEQUALITY: signature has no ≥ or >; all coordinate/growth/weight/result comparisons oriented ≤ or <. No _ge_/_gt_ name.
20. NORMAL FORM: absolute product and real-power decay with weight are natural multiplicative estimate; no competing equivalence/API normal form.
21. SYNTAX: x is an arbitrary real tuple, weak magnitude bound and weak weight/growth bounds make application direct; no polynomial-specific input.
22. IMPORT: no imports added; fanout n/a.
23. CASTS: all q/r natural-to-real casts genuine; 0:ℝ pins real inequalities, κ/d multiplication uses expected real exponent. No redundant same-type cast identified.
24. INSTANCE NAME: no new instance declaration; NeZero m is necessary to form distinguished Fin index 0.

Per-binder review: m (natural size) used by Fin/products, cannot drop; [NeZero m] used by Fin 0, removing makes statement ill-typed; r,q used in bound/weight and growth, cannot drop; hq provides positive q and q0>=1, nonnegative replacement is false (m=1,q0=0,r0=1,κ=1,d=0,c=-1,x=0 gives 1<=0); κ used in estimate, cannot drop; hκ weak nonnegative already minimal (m=2,r=(1,1),q=(2,4),κ=-1,x=(2,4),d=(1,1),c=2 would give 8<=4 without it); x used in result; hx needed for coordinate bound (arbitrarily large x refutes dropping); hqr needed (q=(4,1),r=(1,1),κ=1,x=(0,1),d=(0,1),c=1 gives 1<=1/4 without it); d used in product/weight, zero exponents allowed; c used in conclusion; hw needed (m=1,q0=2,r0=1,κ=1,d=0,c=1 gives 1<=1/2 without it). hq/hx/hqr all quantified only over actual finite product, no global-to-local weakening. No abstract type/universe parameter to widen; ℝ needed for rpow, Fin indexing necessary for project weight and distinguished base; changing either is optional restatement excluded by scope. Inversion check: polynomial context already removed, weight appears once to expose its finite sum, exactly the mathematical estimate needed. Literature n/a: private declaration.

42-rule pass: 1.1 n/a no by-exact wrapper; 1.2 n/a no by-rfl; 1.3 n/a rewrites followed by mathematical inequality; 1.4 n/a no simp+exact; 1.5 n/a no trailing rfl; 1.6 n/a no constructor; 1.7 sum apply+intro compressed to sum_congr expression; 1.8 n/a no contradiction; 1.9 lambdas bind used j, not eta wrappers; 1.10 hqR reused, hq1 proof content retained; 1.11 sum intro replaced by lambda; 1.12 n/a no show; 1.13 n/a no projections; 1.14 consecutive rw absent; 1.15 no terminal simp only; 1.16 no bare nonterminal simp; 1.17 hqR.le/hκ preserved natural projections; 1.18 proof-valued one-off by exact_mod_cast already compact, no redundant wrapping; 1.19 no push_neg; 1.20 no existential wrapper. 2.1 actual whole grind failed; 2.2 no grind in production; 2.3 no simp chain; 2.4 no function-property goal; 2.5 existing positivity solves product-base positivity, kept; 2.6 ordered rpow exponent negative requires explicit antitone API, gcongr cannot replace essential sign data; 2.7 no pure integer arithmetic goal; 2.8 whole aesop leaves essential estimate; 2.9 exact_mod_cast legitimately crosses Nat/Real positivity; 2.10 no computable closed proposition; 2.11 ring identity has denominators as atoms, no nonzero r required, field_simp inappropriate; 2.12 tested linear_combination at sum level fails (requires sum congruence), pointwise ring uses no relevant equalities; 2.13 no symmetric cases; 2.14 four distinct stages, no two-step collapse; 2.15 final convert already closes both exponent algebra goals with ring. 3.1 no erw; 3.2 no continuity/measurability; 3.3 no omega; 3.4 no rcases; 3.5 private one-off estimate not an automation normal form; 3.6 no simp_all; 3.7 no limits.

Step-back/manual holistic review: product magnitude, negative exponent comparison, sum identity, then weight monotonicity are the necessary four mathematical stages. No wrapper around 1–3 library calls, new companion, or ambient API warranted. Keep explicit sign handling and ring normalization, allowing zero degrees.


Final audit/freeze completed before final gates. Source binding proves ONLY helper declaration + immediate ordinary comment changed; parent target and actual caller byte-identical. All 24 items, 42 golf slots, per-binder review and manual holistic review in initial-audit.md rechecked against final-helper.lean. Scope-authorized private name is now `Roth.abs_prod_pow_le_rpow_of_le_weight`; no queue/shared/Git writes. Actual final signature table is final-source-binding.json: four lines 84/98/99/64 codepoints, next-binder/result groups would give104/147/159, final n/a. All justified, no overwidth. Signature has no ≥/>. Proof21 lines, branches5/4/3/4, no conjunction. HAVE hqR proof-lambda reused4 times, hq1 proof content once; both justified. No private docstring, ordinary mathematical comment added; no existing comments removed. All natural-to-real casts genuine, no unused local assumption or arbitrary limit. Sum identity now an explicit congrArg/sum_congr/ring term. Defaults unchanged. No optional new API/companion/ambient generalization. Full independent reviewer remains owner later, this local review does not replace it. Native/LSP/type/value/performance gates pending, no success claimed yet.


# Final gates and local result

Final name: private `Roth.abs_prod_pow_le_rpow_of_le_weight`.
Only this declaration and its immediate ordinary comment changed. Exact inverse substitution reproduces the entire 595-line entry file byte for byte, so the parent theorem and its existing caller are untouched. Final Main:592 lines/34278 bytes, SHA256 `08790a2873090e46cc1b30af0c4fca7f35a400fe789ed1d2e48e81bf23538a90`. Helper:29→25 declaration lines,24→21 body lines; source595→592 because one ordinary explanatory comment was added. Helper SHA256 `8e17d0654af3467e8e015d5c7375be50fd8f74c0bf589a4c89c607b87d6056ac`. No definition/public contract or import changed, no source change after the final audit/freeze.

## Literal final packing and inequality table

| Signature line | Actual codepoints | Next whole binder/result group | Sum | Action |
|---|---:|---:|---:|---|
| 1 |84|19|104|ok|
| 2 |98|48|147|ok|
| 3 |99|59|159|ok|
| 4 |63|none|n/a|ok|

The earlier metadata width64 for the last signature line counted a duplicated separator while reconstructing `:= by`; direct literal-source measurement gives63. This is an evidence-only correction, with unchanged source/proof. All lines <=100. Inequality scan: no ≥/> occurrence in signature/hypotheses; all inequalities oriented ≤/<. Branches <=10, body21<=30, no conjunction. Final HAVE review: hqR is a reused proof-lambda; hq1 has proof content. Cast status:0 dropped /12 retained genuine natural→real /2 retained load-bearing literal ascriptions. No helper warnings. No private docstring; zero original comments deleted. No rename queue/shared/Git writes.

## Baseline and build/diagnostic gates

All commands below actually ran in this helper worker. Full stream/launch/terminal evidence is in `/private/tmp/roth-main-weighted-product`.

| Gate | Actual invocation/evidence | Result |
|---|---|---|
| First ungolfed helper compile |`lake env lean Roth/Main.lean`, direct session34752, first-baseline.stdout/stderr |exit0 before any helper golf|
| Genuine old actual artifact |old-build-v2: `lake env lean -R … -o …/OldWeighted.olean …/OldWeighted.lean` |exit0; exact saved prefix|
| Complete old family then guards |old-enumeration-v2 then old-guards-v2 |exit0 each; actual opaque VALUE checked before source edits|
| Full project build |final-full-build: `lake build` |exit0;2467 jobs|
| Separate Eval build |final-eval-build: `lake build Roth.LeanEval` |exit0|
| Fresh unfiltered native Main |`lake env lean Roth/Main.lean`, native-Main terminal |exit0|
| Fresh unfiltered native Eval |`lake env lean Roth/LeanEval.lean`, native-Eval terminal |exit0|
| Fresh unfiltered native root |`lake env lean Roth.lean`, native-root terminal |exit0; native driver terminal0|
| Complete fresh Main LSP |final-Main-LSP.json |success=true,partial=false; only existing header/hQ/hc376/377|
| Complete fresh Eval/root LSP |final-Eval-LSP.json/final-root-LSP.json |success=true,partial=false,empty items each|
| Definition/statement protection |exact outside-helper equality; actual TYPE comparison below |pass; same mathematical helper contract, authorized private rename|
| Normalization/necessity/manual simplify |24-item/42-rule/per-binder/holistic audit above |pass; built-in simplify unavailable, manual substantive review; no tool invocation claimed|
| No unintended breakage |full/Eval and fresh all3 native/LSP |pass|

Scratch tooling failures were repaired without source weakening: initial old artifact invocation omitted `-R`; observation lift/name serialization and match-arrow syntax needed repair; independent positivity required its explicit available positive base. All failed launches are retained with actual nonzero terminal records. Final valid rows were preserved, not replayed to hide those attempts. Misplaced LSP snippets on signature line345 are explicitly excluded; actual helper-goal exact? failed and generic search found building blocks only.

## Actual complete families, default opaque VALUES and strict TYPE

Old genuine family discovered before guards: one actual `_private.OldWeighted.0.Roth.abs_prod_pow_le_rpow_weight_aux`, actual universes[]. Final production family discovered before guards: one `_private.Roth.Main.0.Roth.abs_prod_pow_le_rpow_of_le_weight`, actual universes[]. Independently authored coordinate-first proof imports only Roth.MainLemma; its complete actual family has TWO rows: `independentWeighted` and generated `independentWeighted._simp_1_1`, each actual universes[]. No suffix count or empty universe list was assumed. No recovery family is required: the helper contract was not weakened.

Actual final-type-comparison terminal0 checks the whole genuine-old/current/independent/baseline-profile TYPE recursively through Name/Level/BinderInfo/metadata/literal/projection/Expr without ExprBEq. Raw TYPEs are UNEQUAL: only the second forall binder (anonymous NeZero instance, instImplicit) has module-scoped macro names. The finite literal pairs observed are OldWeighted4191390519/Main2773899615/IndependentWeighted1104065393 and the genuine baseline `_stdin4191390519`, each at that exact binder path, each hasMacroScopes=true and eraseMacroScopes=`inst`. `strictAtAnonymousInstance` checks the exact literals, exact path, BinderInfo, scope flags/erased names, outer binder/type and every remaining Expr recursively. A SINGLE exact literal replacement also yields complete remaining raw TYPE byte equality; broad binder erasure is forbidden and was not used. See finite-literal-name-pairs.json, actual-binder-observation.json and TypeCompare.lean.

Final actual row guards terminal0: all3 actual opaque VALUES were loaded IN MEMORY, inferred to their actual types, closed (no metavariables/free/loose bound/level metavariables), and checked for only propext/Classical.choice/Quot.sound with actual defaults200000/20000/512. Every row has its own default-budget command. Complete values were not persisted or claimed identical; only sizes/hashes are recorded. final-actual-rows.json and final-guards.stdout retain every passed row. Actual acyclic local dependency graph plus607 external references each with actual strictly upstream ModuleIdx deny production/generated/Main/later/circular origins to the independent proof, without replaying the imported DAG. See final-dependencies.json.

## Genuine first-draft and final profile — separate accepted measurements

Both phases obeyed HOLD request→owner ACK BEFORE ANY prep, exact frozen prefix/canonical/source maps, safe parent/Lake full environment byte equality IN MEMORY ONLY, allowed fields/hash/length persisted, default200000/20000/512, five actual launches0, groups absent and actual driver terminal0, RAW UNPARSED drain notice→explicit owner RELEASE BEFORE parsing. Safe task-owned observer used escalation on first try. No full environment or unrelated command arguments persisted. Production was never reverted. Both captures retain full canonical payloads and fresh complete families/universes before VALUE guards.

| Phase | Canonical target | Disjoint outer/proof/kernel-parent/lint roots ms | Total ms | Result |
|---|---|---|---:|---|
| Genuine first draft |exact saved29-line helper + exact595-entry imports/preceding commands |39.562+444.063+8.329+18.343|510.297|<750; no repeat|
| Final freeze |exact25-line final helper + unchanged current imports/preceding commands |44.305+462.754+8.394+16.756|532.209|<750; no repeat|

Nested kernel8.271/8.333ms is inside its respective parent, not added again; compiler roots absent. Full canonical matched once per phase. No controlled ratio or speedup claim across these contexts. Actual fresh profile stems are `_private._stdin.0.Roth.abs_prod_pow_le_rpow_weight_aux` and `_private._stdin.0.Roth.abs_prod_pow_le_rpow_of_le_weight`; each family has exactly its enumerated opaque row and actual universes[]. Both actual profile VALUES checked closed/inferred/std/default in memory. Approved exact-prefix scope only; the mandatory later whole-file all-row profile remains the owner's file-final responsibility.

Final regular capture discovered its ACTUAL fresh anonymous binder `_stdin2773899615`, NOT the old baseline419 scope, with actual instImplicit/hasMacroScopes/erase inst. Outstanding-only final-profile-type terminal0 checks that exact fresh literal pair against Main2773899615 at the same second-forall path, plus complete remaining strict Expr/defaults. Raw final profile/current TYPEs remain UNEQUAL; one literal replacement gives full remaining raw byte equality. No passed old/current/independent VALUE or native/build row was replayed. See final-profile/actual-binder-observation.json, actual-current-type-binding.json and FinalProfileType.lean.

Buzz outcome: FAST-BOARD, final532.209<1000ms. No limit raises, no remaining profiling scaffold, no performance deferral or optional API expansion. Profile receipts: baseline-profile/target-profile-acceptance.json and final-profile/target-profile-acceptance.json.

## Lifecycle

This is LOCAL helper acceptance only. Original14 parent and its caller remain unchanged, original completion counts unchanged; earlier13 declarations not reopened. Owner must minimally accept this helper then have the SAME parked parent author resume, with joint parent+helper publication only. No standalone helper publication. Final source/report bindings and actual drained/released state are in final-END.json/final-drain.json; all task compiler/native/semantic/LSP/profile leases released at handback.

Historical freeze qualification: the owner later rehashed all43 final inputs successfully. The baseline currently rehashes42/43; only Main.olean changed legitimately during the later final full build. The genuine baseline prefix imports MainLemma, not Main. Its own pre/post phase freeze passed historically; no claim that the old Main.olean still matches now, and no controlled same-context speed ratio is asserted.
