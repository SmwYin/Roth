# `Roth.one_le_prod_pow_mul_abs_eval` — original 13

Status: scoped FINAL/END. All required current gates and both final timing samples pass. Owner publication and independent whole-file review remain outside this worker scope.

## Scope, preservation, references and baseline

Sole target source/report scope, no Git/shared progress/rename changes, no helper, no new import.
Saved genuine original and entry before any Lean experiment in
`/private/tmp/roth-main-integer-bound/{genuine-original,entry}.lean`.
Both are exactly identical: SHA256 `6f030676a4489bf9d4c3775df0e63d21aa0f7c69bd0293ac441a496af0d98c94`,
1548 bytes, 29 declaration lines / 25 proof lines. The inherited >30 inventory estimate was
incorrect; no forced decomposition applies. Entry Main SHA256
`8327e6baee2bf25b8f8b372edfbacab0e1b5f30f7a92a379ac02d934ff3b9853`.
Final candidate: 21 declaration lines / 17 proof lines, eight lines saved. Main 573→565 lines.
The theorem still clears every monomial denominator into one integer and applies the unit
gap for nonzero integers. Its exact real inequality, domains, explicitness and order survive.

Read installed Lean/mathlib-quality skills; cleanup and cleanup-all workflows; golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates; relevant style/naming;
review stages, profiling and buzz references. No invocation of unavailable simplify skill is
claimed. A substantive manual holistic review precedes final gates; independent whole-file
review remains the owner's later phase.
Baseline reuse is explicitly authorized: unchanged source FULL 35.968s / separate Eval 5.063s,
native Main/Eval/root 31.346/28.394/26.237s, complete unfiltered Main diagnostics zero errors
and three existing warnings (header, unused hQ/hc), Eval/root clean, from
`/private/tmp/roth-main-degrees` and owner degrees receipt. No redundant baseline run.
Cache optional/skipped; runLinter executable absent, Lean native lint and LSP used.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Accepted baseline has no target warning; complete current diagnostics required below. |
| 2 | HAVE | Full initial/final scan below: inline hdj/nonzero fact, eliminate hN0 case split. |
| 3 | SET_OPTION | None; defaults 200000/20000/512 preserved. |
| 4 | SIMP | No standalone simp call. push_cast normalizes the sum once; field_simp closes the monomial identity with explicit denominator nonzero evidence. |
| 5 | NAMING | Descriptive snake_case conclusion name; no forbidden abbreviation, numbered auxiliary or scheme prefix; no rename. |
| 6 | PACKING | All four signature lines measured below; no underpacked row. |
| 7 | BY | Every by sits on its preceding declaration line. |
| 8 | FORMAT | Two-space proof indentation; no internal blank line or chained tactics; all target lambdas now ↦. |
| 9 | COMMENTS | No initial proof-body comment; none deleted. |
| 10 | DOCSTRING | Existing public statement and §7 eq.(54) citation preserved byte-for-byte; source explains integrality context. |
| 11 | VISIBILITY | Documented mathematical API; actual downstream theorem consumer. Preserve public visibility. |
| 12 | STRUCTURE | 25→17 proof lines; no conjunction conclusion; no branch >10 lines. The remaining local equality proof is nine lines. No helper necessary. |
| 13 | MATHLIB | Five-method search finds exact integer gap/cast APIs, but only a univariate denominators theorem; keep multivariate result. |
| 14 | JUNK DEF | n/a: theorem, no def/abbrev introduced. |
| 15 | EXISTS | n/a: inequality theorem, no private trivial existential helper. |
| 16 | SHOW/CHANGE | n/a: neither present. |
| 17 | PUSH_NEG | n/a: no push_neg or negation preprocessing. |
| 18 | GENERALISE | Every binder assessed below; all remain necessary for the exact integer denominator statement. |
| 19 | INEQUALITY | All Lean inequalities use ≤ or <; reversed scan below. |
| 20 | NORMAL-FORM | Product times absolute real eval and degreeOf bounds match the consumer; standard map(Int.castRingHom) and eval forms retained. |
| 21 | SYNTAX-GEN | Same explicit Q,h,hQ,hq,hne and inferred m,r,q; no caller adaptation or optional ambient restatement. |
| 22 | IMPORT-FANOUT | n/a: no import change. |
| 23 | CASTS | All explicit target ascriptions bridge ℕ/ℤ→ℝ or fix the integer witness/real order. New Int.cast_ne_zero bridges actual N to real nonvanishing; none redundant. |
| 24 | INSTANCE-NAME | n/a: no instance binder or declaration introduced. |

### HAVE scan and final holistic review

| Initial have | Shape/use | Decision |
|---|---|---|
| hqR | lambda with proof; reused in positivity and denominator cancellation | keep |
| hP | term; used in nonvanishing and abs_of_pos | keep |
| hNeq | proof block; reused in nonvanishing and final equality | keep |
| hdj | term, one use | inline (monomial_le_degreeOf j hd).trans(hQ j) into pow_sub_mul_pow |
| anonymous (hqR j).ne' | term, single field_simp consumer | pass directly in field_simp list |
| hN0 | six-line contradiction/case split | replace with Int.cast_ne_zero.mp and mul_ne_zero inline in integer gap |
| h1 | proof block, final rewrite | keep: it stages the integer/real cast boundary clearly |

Final has exactly hqR,hP,hNeq,h1; no single-use term alias remains. N/hN remains a local
integer witness used in equality, casts and inequality. Review considered reusing surrounding
lemmas, witness duplication, casts, proof organization and efficiency: no duplicated proof
skeleton worth extracting, no unnecessary new API, all bounded suggestions implemented.

## Search and generality

| Method | Actual query | Result |
|---|---|---|
| Lean-Finder | integer polynomial rational evaluation, clearing denominators, nonzero gap | one_le_pow_mul_abs_eval_div, DenomsClearable and variants: univariate only |
| Loogle | Int.one_le_abs | exact integer gap API already underlying proof |
| LeanSearch | nonzero integer absolute value at least one | Int.one_le_abs; Int.abs_lt_one_iff alternative used independently |
| Source | eval/denom/rat in MvPolynomial; DenomsClearable source; cast_ne_zero | no direct multivariate product-denominator replacement; exact Int.cast_ne_zero verified |
| Local name | cast_ne_zero | Int.cast_ne_zero and Nat/Rat alternatives; index unavailable, no indexed absence claim |

Auxiliary variants inspected: DenomsClearable.add, denomsClearable_of_natDegree_le,
denomsClearable_natDegree; Int.abs_lt_one_iff; cast/nonzero/product routes.
Common-equivalents table: no discrete/finite/bounded predicate match.
Bounded compiled generic route: original live LSP grind fails; exact? cannot close; apply?
provides generic order transformations and ends in the default 200000 isDefEq timeout.
No repeated broad probe; no claim of exhaustive mathematical absence from search alone.
Conclusion: partial matches only; build on existing cast/product/gap APIs and retain the
actual multivariate denominator calculation. It is not a 1–3-call wrapper.

| Binder | Class/use | Drop/weakening review | Result |
|---|---|---|---|
| m:ℕ | structural index | needed by Fin m; no NeZero constraint | retain, m=0 allowed |
| Q:MvPolynomial(Fin m)ℤ | structure value | coefficient/support and eval content | retain |
| r:Fin m→ℕ | degree vector | powers and denominator bound | retain, zero degrees allowed |
| hQ:∀j,degreeOf j Q≤r j | proposition | needed monomial_le_degreeOf transitivity; point-local bound covers each support monomial | retain weak bound already |
| h:Fin m→ℤ | structure value | integer numerator makes cleared value integral | retain; no positivity/coprimality imposed |
| q:Fin m→ℕ | structure value | natural denominators and product | retain; optional arbitrary field/index abstraction outside bounded scope |
| hq:∀j,0<q j | proposition | supplies nonzero casts and positive product; merely 0≤q j admits zero denominators and false conclusion when Q=1,r>0 | retain; q≠0 equivalent for naturals, no gain |
| hne:eval...≠0 | proposition | necessary integer unit gap; drop admits Q=0 | retain |

No typeclass-parent/universe weakening applies: all domains are concrete and there is no
ambient universe/typeclass binder. Drop-tests for structural parameters would make the
statement unbound; hQ/hq/hne are substantively used. No needless failed statement edits.
Inversion check: no fixed concrete named polynomial/object disappears after unfolding;
Q,h,q,r are arbitrary throughout. No optional generalization/helper/caller edit proposed.

Literature search performed: "Roth theorem polynomial integer nonzero value rational
denominators lower bound multidegree" and "Liouville inequality multivariate integer polynomial
rational points clearing denominators". Related lower-bound literature does not eliminate
integrality, degree control or nonvanishing. Main source is the project's clean.tex §7,
lines1648–1649, the precise nonzero-integer assertion. Broader geometry results, e.g.
[Liouville inequalities on projective varieties](https://arxiv.org/abs/1609.04262), are optional
ambient restatements and introduce no necessary local API change. ChatGPT math MCP unavailable.

## Packing and inequalities

Widths count codepoints. Final #check at format.width100 is captured with final profile.

| Signature line | Width | Next complete token/unit | Arithmetic | Action |
|---|---:|---|---|---|
| 320 | 89 | (hQ : ∀ j, degreeOf j Q ≤ r j), 30 | 89+1+30=120>100 | ok |
| 321 | 86 | complete hne hypothesis, 70 | 86+1+70=157>100 | ok |
| 322 | 76 | conclusion expression and :=by, 90 | 76+1+90=167>100 | ok |
| 323 | 94 | proof body next | n/a | ok |

| # | Location | Reversed ≥/> occurrence | Action |
|---|---|---|---|
| 1 | full signature, hypotheses and proof | none (arrows excluded) | retain ≤/<; no rename |

## All 42 golfing rule slots

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: exact_mod_cast is substantive, no exact wrapper |
| 1.2 by rfl | n/a: none |
| 1.3 rw+exact | existing final rwa retained; cast step needs exact_mod_cast |
| 1.4 simp+exact | n/a: none |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructor | n/a: no conjunction/constructor |
| 1.7 apply+exact | n/a: no such pair |
| 1.8 by_contra | n/a: none in production |
| 1.9 eta | lambdas do arithmetic or use argument twice; no eta reduction |
| 1.10 have | hdj and anonymous denominator fact inlined; hN0 scaffolding removed |
| 1.11 apply+intro | n/a: refinements already use lambdas |
| 1.12 show | n/a: none |
| 1.13 obtain | n/a: no tuple projection binding |
| 1.14 rw merge | current consecutive rewrites already merged; push_cast separates the two meaningful rewrites |
| 1.15 terminal simp only | n/a: no simp only |
| 1.16 nonterminal simp | n/a: no bare simp |
| 1.17 dot notation | .trans/.ne'/.symm retained; .mp is direct cast API |
| 1.18 <\| | nested term parentheses fix Int.one_le_abs argument; no awkward terminal by/fun parentheses |
| 1.19 push_neg | n/a: none |
| 1.20 exists helper | n/a: none |
| 2.1 grind | actual original live probe failed; direct arithmetic construction retained |
| 2.2 before grind | n/a: no grind remains |
| 2.3 simpa | n/a: no simp-then-close block; casts handled directly |
| 2.4 fun_prop | n/a: no function regularity goal |
| 2.5 positivity | explicit prod_pos(pow_pos hqR) already short, targeted and reused; no multi-line positivity chain |
| 2.6 gcongr | n/a: no monotonicity chain |
| 2.7 lia/omega | degree order proof supplied directly by transitivity; no arithmetic automation needed |
| 2.8 aesop | logical N≠0 branch replaced by exact APIs; no remaining logic search goal |
| 2.9 norm_num/norm_cast | exact_mod_cast used once per cast boundary; no concrete computation |
| 2.10 decide | n/a: parameterized polynomial/real theorem, no closed finite decision |
| 2.11 field_simp;ring | field_simp alone closes actual monomial identity; trailing ring unnecessary |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or linear hypothesis combination |
| 2.13 wlog | n/a: no symmetric cases |
| 2.14 calc | n/a: no calc |
| 2.15 <;> | n/a: no similar multiple goal family |
| 3.1 erw | n/a: rw suffices |
| 3.2 regularity | n/a: no continuity/measurability |
| 3.3 omega | n/a: no omega; direct degree transitivity |
| 3.4 rcases rfl | obsolete disjunction eliminated entirely |
| 3.5 attributes | no new broad simp/grind rule justified for the specialized inequality |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 limits | no limit/scaffolding introduced |

Step-back reflection: whole-proof automation cannot construct integrality; explicit finite
sum plus one local equality is the useful mathematical strategy. Direct nonzero APIs are
clearer than disjunction scaffolding. No helper/decomposition, API/normal-form restatement,
definition/rename or cross-file refactoring necessary. Phase5a/5b: none; shared queue untouched.

## Semantic and verification evidence

Fresh final FULL build0 58.874s; separate `lake build Roth.LeanEval`0 29.234s. The root excludes
Eval, hence the separate gate. Actual invocations and exit/stream hashes are in
`final-full-build-{launch,terminal}.json` and `final-Eval-build-{launch,terminal}.json` under
`/private/tmp/roth-main-integer-bound`. Independent proof uses the cleared integer and
`Int.abs_lt_one_iff` by contradiction; no call to target, target-generated wrappers or later
Main result. Independent compile0 27.541s. Complete family inventory0 57.060s precedes every
row guard. Actual families: target+seven generated simp proofs and independent+seven;
actual roots have []; generated `_simp_1_{1,2,3}` have u_2, `{4,5,7}` u_1, `{6}` u_3.
No suffix/universe count was assumed; `actual-family-types.json` records full actual Types.

Fresh semantics0 61.329s, all16 actual rows: opaque VALUE checked in memory, inferred type,
closed terms/universes, no admits and only propext/Classical.choice/Quot.sound; actual default
resources200000/20000/512 per command. Actual VALUE hash/length receipts, not full VALUE dump,
are in `final-semantics.json`; root lengths3267801/3460925 bytes (production/independent).
Complete raw TYPEs and strict recursive comparison (Name,Level,BinderInfo,metadata,literals,
projections included, no ExprBEq shortcut) give old=current=independent. No hygiene exception.
Old target TYPE recovered with an indexed capped read; the exact cap is recorded in
`old-type-receipt.json` (2×32046+2000=66092 bytes); only TYPE string decoded, hash verified,
no giant old VALUE read/decoded/exported. Actual universes preserved.
Fresh local dependency graph acyclic; all external constants have actual strictly upstream
ModuleIdx; no target-generated/circular/later-Main path in independent proof. No full imported
DAG replay or clone of unchanged earlier helpers. Signature unchanged, so no old-contract
recovery wrapper/caller adaptation necessary. Actual sole code consumer is
Roth.roth_of_isIntegral (entry510, final502); Eval has no direct target call. Both downstream
module and Eval covered by current builds/native/complete diagnostics.

## Final gates, simplify review and buzz

Fresh final native Main/Eval/root: exit0 in30.898/30.543/27.590s, respective
`final-native-{Main,Eval,root}-{launch,terminal}.json` receipts. Then, with every compiler and
native driver terminal, complete fresh unfiltered LSP Main/Eval/root responses were saved in
`final-diagnostics.json`: Main zero errors and exactly the three existing warnings at1/349/350;
Eval/root no diagnostics. No failed dependencies, partial response, still-elaborating range or
timeout. No warning in target320–340. No source edit during verification/capture.

| Gate | Result/evidence |
|---|---|
| lake_build_file + lake_build | PASS: actual final-full-build lake build0, 58.874s, Main/root jobs built |
| separate Eval | PASS: actual final-Eval-build lake build Roth.LeanEval0,29.234s |
| definition_protected | PASS: no def/abbrev/import or other declaration edited |
| theorem_statement_protected | PASS: same complete TYPE/raw bytes, independently verified; only lambda token spelling changes in textual signature |
| structure | PASS:17 proof lines, no conjunction/long case branch; no forced helper |
| naming | PASS: descriptive snake_case; no forbidden pattern; no rename queue entry |
| line_packing | PASS: all four measured rows above |
| inequality_orientation | PASS: no reversed Lean inequality |
| casts/instances | PASS: genuine integer/natural-to-real bridges; no instance additions |
| cumulative_no_unintended_breakage | PASS: sole caller module/root, separate Eval, native and complete diagnostics |
| semantics/trust | PASS: all16 actual current/independent VALUE rows, exact original/current/independent TYPE and fresh local acyclic upstream graph |
| no limits/admit/scaffolding | PASS: no sorry/new axiom/native_decide/count_heartbeats/resource raise/debug option in source diff |

Simplify status: manual scoped holistic review completed because actual simplify skill/tool is
unavailable; no actual invocation claimed. Reuse, clarity, duplication, witness construction,
casts, HAVE aliases and efficiency were reviewed before final gates. Concrete issues fixed:
single-use degree and denominator aliases, avoidable nonvanishing disjunction, lambda style.
No outstanding scoped suggestion; owner later independent whole-file reviewer remains required.

Buzz budget1000ms. The historical whole-source capture from
`/private/tmp/roth-main-approxset/profile-all17-rows.json` gives1066.582ms, a valid FAIL, rooted
in its actual Main689 context after MainLemma caller repairs (not automatically the genuine
Main684 source context). Its complete canonical payload matches the original target, and
outer42.114/proof972.223/kernelparents20.397/lint31.848ms sum1066.582ms. That historical failure
is preserved, not discarded as noise. The current exact source-prefix context is separate;
no cross-context speedup ratio or unsupported causal timing claim is made.

Current diagnosis from indexed target-only trace bytes58890200–73710049: proof807.635ms,
local cleared-evaluation equality633.894ms, field_simp407.810ms (includes optional failed
numerator-nonzero discharge241.462ms, not a theorem failure), push_cast118.363ms. This is
algebraic cast/denominator automation work (taxonomy4/6), not import or kernel dominance.
Direct existing APIs simplify nonvanishing and make denominator evidence explicit; fresh
actual timing closes the budget. No extra optional optimization/capture is required.

| Sample | Outer command | Proof | Eight kernel parents | Lint | Total | Budget |
|---|---:|---:|---:|---:|---:|---|
| Final exact prefix |57.322|807.635|41.314|17.506|923.777|PASS <1000ms |
| Required same-freeze repeat |44.882|812.833|41.923|17.373|917.011|PASS <1000ms |

Totals use disjoint outer/async/kernel-parent/lint roots; nested Kernel timing is not added
again. No compiler or lazy prior DATA root in either target command. Canonical full
doc/signature/body binding, actual fresh eight-member family, strict full TYPEs against
production and in-memory inferred/closed/opaque/standard-axiom VALUE checks all pass.
Actual universes are checked individually, not blanket-empty. Resources remain200000/20000/512.
Both samples are reported; the >=750ms required repeat was run exactly once, same source,
exact byte-identical prefix/maps and unchanged model/tool/import/options. No third capture.

Each capture used its own explicit owner HOLD before preparation and explicit owner RELEASE
only after actual RAW UNPARSED drain: five launches0, all task groups absent, capture driver
terminal, input freeze/defaults/parent and Lake full environment byte-equality verified.
Full environment comparison occurred only in memory; persisted environment evidence is
hash/length plus approved PATH/LEAN/toolchain allowlist. Process observation persisted only
task-owned identities/arguments; safe elevated observer succeeded first try. Raw outputs
and independently indexed roots/acceptance receipts are in final-profile and repeat-profile.
No parse before the explicit releases. No additional production source edit after gates.

New identifier verification:

| Identifier introduced at use site | Verification | Result |
|---|---|---|
| Int.cast_ne_zero | actual local search; Data/Int/Cast/Lemmas.lean:71; final compiled proof | PASS |
| mul_ne_zero | standard product API resolved in actual final compiled proof and in-memory VALUE inference | PASS |

## Phase checklist and disposition

- [x] Step1: mandatory references read, genuine/entry preserved before Lean/golf.
- [x] Step2: full24-item audit, complete initial/final HAVE scan.
- [x] Step2.5: five actual search methods, variants and compiled generic probe.
- [x] Step2.6: every binder/generalization/normal-form/inversion/literature review.
- [x] Step2.7: measured per-signature-line packing.
- [x] Step2.8: inequality scan.
- [x] Step3: all42 rule slots.
- [x] Step4: step-back/manual scoped holistic review.
- [x] Step5a: complete fresh unfiltered diagnostics.
- [x] Step5b: actual build/native/semantic/trust/diff gates and both budget samples PASS.
- [x] Step6a: no rename required; shared queue untouched.
- [x] Step6/7: scoped report complete; no deferred scoped refactor/helper work.

Final source Main565lines/32523bytes, SHA256
`f514a82586b0df1ad6d45d65471512f2524755d7be931291ff4c5b4482e6d02c`;
target21declaration/17body lines, eight saved. Final target SHA256
`982fe35a173e27d6a58d32a9af7d33893386c88d8b55bc62db0b716036569436`.
This is scoped FINAL/END; owner publication and later independent whole-file gates remain
outside this worker. No Git action performed. All compiler/native/semantic/LSP/profile leases
released after actual final drain, with all19 task launchgroups absent and all query/driver
calls terminal; exact current receipt in `/private/tmp/roth-main-integer-bound/FINAL.json`.
