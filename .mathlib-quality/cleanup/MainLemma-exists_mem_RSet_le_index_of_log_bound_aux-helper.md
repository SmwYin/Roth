# Fresh full Mode B audit — logarithmic auxiliary polynomial existence

Scope: private `Roth.exists_mem_RSet_le_index_of_log_bound_aux` in `Roth/MainLemma.lean`. Final source `d893d39e1ac727b2ff0f490a2951ccd421de8264c2190217bb7cfb3ea0d64e60`, 768 lines; original entry `d8445fdd82d7c4bbe5d42bc2f73e014d57906b0ed047aab38811eac0e389a84a`, 779 lines. This helper is not an original-264 declaration and receives no publication/count credit.

The helper proof is 26 → 16 nonblank tactic lines; its full declaration is 34 → 23 physical lines including the separator. Its name, binder order, BinderInfo, dependent types, universes, hypotheses, and single common-witness conclusion are preserved by actual Lean constructor comparisons. The caller remains 44 proof lines, still FAIL against its separate headline-15 obligation. No new helper, wrapper, import, API weakening, or caller repair is introduced.

Status: final retained guards and matched AFTER profiling pass; closure/owner independent THIRD pending.

## Phase 0 — Doctor

Fresh FULL `lake build`, then separate `lake build Roth.LeanEval`, passed before loaded-origin credit. Baseline receipts: `baseline-full-v2.json` (exit0, 33.210s, drained) and `baseline-eval-v1.json` (exit0, 13.990s, drained). The first runner CLI assertion failed before spawning because options followed the REMAINDER label; it is preserved in `baseline-cli-v1-preexecution-failure.json`, with no V1 build credit. Optional cache fetch was skipped for the existing warm pinned cache. A separate project `runLinter` executable was not invoked; normal mathlib linters ran during compilation and complete natives.

Early native MainLemma request was file_path-only, complete/unfiltered, errors0/failed_dependencies[]/partial=false/timed_out=false, with the inherited header warning. Full raw result, immediate-return timestamp, source17 pre/save/post hashes and bytes are retained. Unknown copyright year/authors/license remain unknown; no metadata was invented.

## Phase 1 — Preparation and primary mathematics

The full 53,991-byte dispatch, full installed lean4 and mathlib-quality skills, cleanup/cleanup-all/buzz commands, and mandatory style/naming/golf/search/generalisation/gates/profiling/review references were read freshly. Full source and primary clean.tex §6 were read. No applicable AGENTS.md exists at ancestors or recursively in the repository. `instruction-reference-read-bindings-v1.json` binds actual paths/SHA/bytes; later relevant Lean search/golf/metaprogramming and PR examples were also consulted. No Git calls or children were used.

Dialect: classic imports, not module-system syntax. Scope ownership protects all thirteen earlier helper declarations and reports, all public main written TYPE/doc/paper quotes, all nine literal proof comments, Main689, and original27 report678. Fresh inventories were derived from actual local/module-origin constants, using hasValue(true) and value! true, including DATA/generated declarations and LeanEval. No namespace-only or guessed-suffix inventory was used.

The mathematical argument turns the coefficient-only weak logarithmic budget into a positive natural floor B1 and `(1+A)^(m*r1) < B1^δ`; the exact nonnegative-base identity supplies `B1*(B1^δ)^3 = B1^(1+3δ)`. The accepted power-budget existence theorem then supplies ONE P with both RSet membership and gamma index bound. This isolates the quantitative construction before the rational/Theta stage. It is neither an unrelated conjunction nor a hidden whole-main proof.

The primary reference says the three small factors follow from logarithmic terms and the floor logarithm; it then bounds diagonal Hasse remainders, counts tuples, and takes the difference of two box polynomials. This helper uses the alpha=0 specialization because the construction needs the coefficient factor, not the later alpha-evaluation factor. The current theorem already omits alpha-magnitude logarithms, ratio/degree-chain assumptions, upper bounds on δ, rational coordinates, and coprimality. The scale r1 is arbitrary and its positivity is derived, not assumed.

## Phases 2 and 3 — File and declaration audit

File audit: A.1 inherited unknown copyright header retained; A.2 existing module doc retained verbatim; A.3 imports already grouped/alphabetized and unchanged; A.4 no contentless section headers; A.5 final768<1000; A.6 no file limit/debug options; A.7 no lambda/$/push_neg replacement required in this helper. No foreign/file-level fix is authorized or needed. All source warnings are inherited (native counts1/4/0).

| # | Audit item | Concrete result |
|---|---|---|
| 1 | LINT | Early unfiltered native: zero errors, only inherited header warning at line1; no helper-specific warnings. |
| 2 | HAVE SCAN | Original hlogA, hX and hBpos single-use terms eliminated; hsumpos/hz contradiction removed. hA1/hr1 reused; hq/hmR/hpow contain proof content. Detailed use table recorded at final source. |
| 3 | SET_OPTION | No source options or limit raises; profiling scaffold isolated in scratch and exactly invertible. |
| 4 | SIMP SQUEEZE | Original terminal simp only in power identity replaced by terminal simp [mul_comm]; nonterminal rewrites explicit; final simpa only[gam,lam] is targeted transport. |
| 5 | NAMING | Descriptive exists_mem_RSet_le_index_of_log_bound_aux; RSet is the named mathematical object; private _aux suffix; no forbidden numeric/scheme/abbreviation pattern. |
| 6 | LINE PACKING | Original signature had repackable first and degree-budget lines. Candidate packs 99/97/86/71/59/81 codepoints with binder-order unchanged; full arithmetic table required in report. |
| 7 | BY PLACEMENT | Every by remains on its preceding declaration/have line. |
| 8 | FORMAT | Two-space tactic indentation, no blank proof lines, no naked semicolons, no haveI/letI. |
| 9 | COMMENTS | Target has no narrative comments; entire prefix/caller and all nine literal comments are protected byte-for-byte. |
| 10 | DOCSTRING | Private helper appropriately has no docstring; public main doc and paper quotes unchanged. |
| 11 | VISIBILITY | Private helper used by one same-file caller; no exported API change. |
| 12 | STRUCTURE | 26→16 proof lines; maximal nested proof branch3. Existential conjunction is essential: one common P satisfies RSet membership and index bound; splitting would lose correlation. No new helper. |
| 13 | MATHLIB | Five fresh methods saved. Semantic hits unrelated Chevalley/Liouville/root-multiplicity results, no direct logarithmic existence replacement. Existing rpow/floor/natural-product APIs used directly; clean isolated exact?/apply? guards decide proof credit. |
| 14 | JUNK DEF | Not a definition; no definitions added or changed. |
| 15 | EXISTS LEMMA | Substantive coefficient/index existence, not a witness-rfl wrapper. Accepted counting helper retained; no convenience wrapper added. |
| 16 | SHOW vs CHANGE | No show/change in candidate proof. |
| 17 | PUSH_NEG | No push_neg/push Not or by_contra in candidate. |
| 18 | GENERALISE | All sixteen binders examined; no classes/universe variables. Already arbitrary scale, coefficient-only weak log bound, no alpha-magnitude/rational/upper-delta/degree-chain restrictions. Formal boundaries and selected-proof drop tests separately qualified. |
| 19 | INEQUALITY | All code inequalities ≤/<; no reversed symbols or _ge_/_gt_ name. Per-occurrence no-violation row required. |
| 20 | NORMAL-FORM | Canonical RSet and index witness; B1 retained explicitly via named argument after inlining positivity. No alternate predicate or equivalence API. |
| 21 | SYNTAX-GEN | Current weak coefficient-only premise is directly supplied by main; no root-height/rational data duplicated. No beneficial restatement identified. |
| 22 | IMPORT-FANOUT | No new imports; caller/import graph unchanged. |
| 23 | CASTS | Three explicit cross-type casts retained (integer coefficients and two natural B1 power bases); three real numeral ascriptions are load-bearing. Named B argument prevents unfolded-bound inference drift. |
| 24 | INSTANCE-NAME | No instance declarations or local class introductions. |

### Every-have scan

| Binding | Original use / action | Final result |
|---|---|---|
| hA1 | Leading coefficient gives A≥1; used for logarithm and factor estimate | Keep, reused |
| hlogA | Term with one use in hq | Inline into bounded arithmetic |
| hmR | Cast proof used in hq | Keep inside hq; genuine proof content |
| hr1 | Scale proof used in floor and small-factor estimates | Replace contradiction with direct product positivity; keep reused result |
| hsumpos, hz | Local one-use sum/case intermediates inside contradiction | Entire branch removed |
| hq | Quantitative real inequality, one use but genuine proof content | Keep named bound |
| hX | One-use real power bound | Inline at floor positivity |
| hBpos | One-use floor positivity proof | Inline; explicit `(B := B1 ...)` prevents implicit bound unfolding |
| hpow | Genuine rpow identity | Keep named identity |

### Actual final width-100 signature

```text
@Roth.exists_mem_RSet_le_index_of_log_bound_aux : ∀ {f : Polynomial ℤ} {α A : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
        ∀ {m q₁ r₁ : ℕ},
          0 < m →
            ∀ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) →
                ∑ j, r j ≤ m * r₁ →
                  ∀ {δ : ℝ},
                    0 ≤ δ →
                      2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) ≤ δ ^ 2 * Real.log ↑q₁ →
                        ∃ P ∈ Roth.RSet (↑(Roth.B₁ δ q₁ r₁)) r,
                          Roth.gam δ f.natDegree m ≤
                            Roth.index ((MvPolynomial.map (Int.castRingHom ℝ)) P) (fun x => α) r
```

### Signature packing, measured in codepoints

Fresh width-100 `#check @Roth.exists_mem_RSet_le_index_of_log_bound_aux` is retained in the final local batch raw output. Every complete next binder/conclusion unit would overflow; conclusion and `:= by` are included. Original first-line84 + next hf14 +1=99 and degree-line66 + next hs24 +1=91 were repacked.

| Source line | Chars | Next complete unit chars | Sum | Action |
|---|---:|---:|---:|---|
| 678 | 99 | 32 | 132 | ok |
| 679 | 97 | 15 | 113 | ok |
| 680 | 86 | 65 | 152 | ok |
| 681 | 71 | 55 | 127 | ok |
| 682 | 59 | 75 | 135 | ok |
| 683 | 81 | none | n/a | ok |

Inequality per-occurrence scan: entire signature and every hypothesis contain zero `≥` or `>` occurrences; no rewrite or rename required. Proof code also uses ≤/<. The `.ge` projection on an equality is proof use, not a reversed theorem name.

Casts: 3 explicit cross-type casts retained (integer coefficients and two natural B1 power bases); 3 real numeral ascriptions retained as load-bearing. No gratuitous cast was added.

## Phase 4 — Full fresh golf pass

| Rule | Attempt/result |
|---|---|
| 1.1 | No by-exact wrapper on target; direct term scale proof retained. |
| 1.2 | No by-rfl proof. |
| 1.3 | No rw+exact pair. |
| 1.4 | No simp+exact pair; existing simpa uses actual coefficient and gamma transports. |
| 1.5 | No trailing rfl after simp. |
| 1.6 | Common existential witness supplied by substantive accepted existence theorem; no constructor-exact chain. |
| 1.7 | No apply-exact pair after golf. |
| 1.8 | Scale contradiction removed by direct natural product positivity. |
| 1.9 | No eta-reducible lambda; lambda in finite sum and diagonal evaluation is mathematical. |
| 1.10 | Inline hlogA, hX and hBpos; retain hA1/hr1 used twice and proof-content hq/hpow. |
| 1.11 | No apply-intro chain. |
| 1.12 | Original show1≤m annotation replaced by direct exact_mod_cast hm. |
| 1.13 | Existing obtain extracts only coefficient-power bound from three_small_factors; no redundant conjunction variable. |
| 1.14 | Power identity uses one rw list. |
| 1.15 | Terminal simp only[Nat.cast_ofNat,mul_comm] unsqueezed to simp[mul_comm], compiled V4. |
| 1.16 | No nonterminal bare simp. |
| 1.17 | Existing .trans/.trans_le/.le/.ge used directly. |
| 1.18 | Direct <| for natural product positivity and inline floor bound. |
| 1.19 | No push_neg. |
| 1.20 | Target is not a trivial existential wrapper. |
| 2.1 | Clean isolated original whole-proof grind probe retained; actual compiler exit1 and guarded rejection; no whole-proof replacement. |
| 2.2 | No grind remains to absorb preceding tactics. |
| 2.3 | hA1 and specialized alpha0 budget use simpa; no extra closing tactic. |
| 2.4 | No continuity/differentiability/measurability goal. |
| 2.5 | positivity closes nonnegative real factors/base conditions in compiled candidate. |
| 2.6 | No monotonicity-congruence chain in candidate; hq is arithmetic and hpow equality is rpow API. |
| 2.7 | Natural scale contradiction/omega replaced by direct Nat.pos_of_mul_pos_left and single_le_sum. |
| 2.8 | Clean isolated aesop probe retained; actual compiler exit1 and guarded rejection; no whole-proof replacement. |
| 2.9 | norm_num discharges 1≤4; exact_mod_cast hm bridges Nat→Real. |
| 2.10 | Infinite polynomial existence is not a finite decidable computation; no native_decide. |
| 2.11 | No rational denominator identity to field_simp/ring; rpow identity handled by exact APIs. |
| 2.12 | No ring/ring_nf terminal goal requiring linear_combination. |
| 2.13 | No symmetric case split. |
| 2.14 | Original hq calc replaced by bounded nlinarith only with exact two sign/budget facts. |
| 2.15 | No duplicated literally identical subgoals. |
| 3.1 | No erw. |
| 3.2 | No legacy continuity/measurability. |
| 3.3 | All omega eliminated with direct scale positivity; no natural arithmetic tactic remains. |
| 3.4 | No rcases-with-rfl chain. |
| 3.5 | Private specialized existential theorem has no useful simp/grind attribute role; none added. |
| 3.6 | No simp_all only in accepted proof; clean isolated simp_all probe retained. |
| 3.7 | No maxHeartbeats override exists or is added. |

### Five-method fresh search status

| Method | Actual query and observed result |
|---|---|
| A Lean-Finder | Nonzero bounded integer multivariate polynomial of large index at an algebraic diagonal root: five Chevalley-complexity hits, no direct replacement. Remote indexv4.28 qualified; pinned local APIs verified by source+compiler. |
| B Loogle | `Real.rpow, _ * (_ ^ _) ≤ _ ^ _`: no hits; searches the quantitative bridge, with clean compiled generic-route probes below. |
| C LeanSearch | Integer polynomial height / high-order algebraic-root vanishing / pigeonhole: Cauchy bound, Liouville, root-multiplicity and Mahler-count hits; none states this correlated RSet/index result. |
| D source grep | Full target name over all mathlib sources: exit1/no text match; NumberTheory RSet/le_index/log_bound/height-index variants and exact rpow/natural APIs searched with full raw results saved. |
| E local name pattern | `exists_mem_RSet`: three project helper hits. Symbol index returned error, so no index-absence inference; actual source hits and compiled probes are the fallback. |

Auxiliary variants: exists_mem, le_index, of_log_bound, of_rpow_bound, rpow_add_of_nonneg/rpow_mul_natCast and floor/product positivity APIs. Common-equivalents lookup: no relevant discrete/topology/finite/bornology bucket. Conclusion: no direct mathlib replacement located; retain substantive project construction and use existing scalar APIs directly. Fresh raw searches `search-*-v1.json/log` are preserved; no search-only proof of absolute absence.


Five isolated original whole-proof automation probes (`grind`, `aesop`, `simp_all`, `exact?`, `apply?`) each compiled in a clean target-absent context and failed actual proof guards/default compilation. Eight selected-proof drop tests likewise failed; this is evidence about this proof, not mathematical necessity. Every raw failure is retained in `automation-drop-acceptance-v1.json` and its linked logs. No suggestion, exit0 partial goal, sorryAx, or admitted residual goal is credited.

Step-back review found that inlining the accepted algebraic construction would duplicate genuine remainder/counting mathematics. No new subhelper is warranted. The 16-line conversion is the correct mathematical boundary, and the public main keeps its separate evaluation-stage factors because those control derivatives at alpha.

## Item 18 and 2.6a–e — Generality, universes, and boundaries

| Binder | Classification | Role | Candidate assessment |
|---|---|---|---|
| f | polynomial datum | conclusion natDegree and monicity/root/height; fixed integer coefficients carry arithmetic content | No purely mechanical alternative with same mathematical object. |
| α | real datum | diagonal evaluation and root hypothesis | Abstract field replacement changes RSet/index real framework. |
| A | real datum | coefficient height and log budget | Concrete logarithm and power estimates. |
| hf | proposition | height at leading coefficient and accepted algebraic existence theorem | Drop selected-proof probe retained in actual failed guard probes; no semantic necessity claim. |
| hfα | proposition | root vanishing in accepted algebraic existence theorem | Drop selected-proof probe retained in actual failed guard probes; no semantic necessity claim. |
| hA | proposition | height of every coefficient and resulting nonnegativity | Drop/point restriction selected-proof probe retained in actual failed guard probes; no safe restriction identified. |
| m | natural datum | Fin m, gamma, sum budget and log bound | Dependent finite-dimensional statement; no universe weakening. |
| q₁ | natural datum | B1 and logarithmic budget | Already arbitrary natural; positivity follows from budget. |
| r₁ | natural datum | arbitrary degree-budget scale and B1 | Already arbitrary natural; positivity is derived. |
| hm | proposition | nonempty dimension and counting theorem | Empty m=0 case may be true but no current caller benefit; retain without false counterexample. |
| r | function datum | degree box, RSet and index weights | Arbitrary natural function on Fin m; no monotonicity assumption. |
| hr | proposition | coordinate positivity in counting and scale derivation | Zero-coordinate semantics need a different counting boundary; no necessity claim from selected proof. |
| hs | proposition | total-degree bound in scale derivation and accepted existence theorem | Already weak ≤ including equality; not tied to first coordinate. |
| δ | real datum | B1 exponent, gamma and log bound | Concrete real data; no typeclass binder. |
| hδ0 | proposition | power estimates in nonnegative exponent regime | Formally proved δ=0 inconsistency is separate. Negative δ has only a qualitative floor-vanishing obstruction here; no certified negative counterexample and no necessity from failed drop probes. |
| hL | proposition | quantitative logarithmic budget | Already weak ≤; retains coefficient-only terms and no alpha magnitude term. |

2.6b: eight actual selected-proof drop attempts are saved, all failed; no drop is justified by them and no necessity is inferred. Data binders remain in dependent hypotheses/conclusion, so deleting them is not an assumption weakening. No typeclass/universe binder exists on this concrete theorem; parent-class and Type→Type* changes are n/a. Real logarithm/index and finite-dimension counting make arbitrary-field/index restatements substantial API redesigns rather than mechanical removals.

2.6c: no beneficial big change identified. Inversion check: the proof still uses the named B1 construction and coefficient-log estimates; the abstract algebraic budget theorem already exists as accepted helper13. A second abstract wrapper would duplicate that API. 2.6d: private declaration; literature search not required, primary §6 was checked. 2.6e: no signature change; all recommended beneficial proof/packing changes are implemented.

Formal boundary probes (five actual closed/inferred/default/std3 proofs, `boundary-acceptance-v2.json`): positive scale from hm/hr/hs; monic root forbids degree zero; δ=0 contradicts the coefficient logarithmic budget; q≤1 contradicts that budget; and in dimension0 the constant1 satisfies RSet1 and gamma0≤index. The latter is an honest boundary witness, not a claim that m=0 is false or a proof of the entire dropped-hm contract. No current caller benefits from adding the empty-domain case. Weak hL/hs include equality. Negative δ is not assumed harmless: q^(δ*r1) may lie below1, so positivity of the floor cannot be inferred merely from its squared log budget. No formal negative-delta counterexample to a stronger theorem is claimed.

## Independent proof, original contract and caller recovery

Fresh actual independent theorem has a VALUE different from BOTH genuine original and current target. It is guarded against the exact original full TYPE/BinderInfo/written binder names/order/universes, closedness, inferred type, standard3 axioms and defaults. Its recursive dependency walk expands TYPE and allowOpaque VALUE across 20875 actual constants, denying actual local and imported target Name-prefix families, scratch aliases and sorryAx. It uses the accepted unrelated algebraic helpers and a separate strict-positive-base rpow argument; the target is absent from its source/import closure.

Candidate-bounded-v4 contains the entire literal original caller doc/TYPE/body unchanged and validates actual target+main opaque VALUEs against their original TYPEs. Source inverse replaces only the new helper with its immutable first draft, restoring d844 exactly; all13-helper prefix, public main written contract/doc/body, all9 comments, Main SHA6668 and original report SHA18e3 are exact. There is no weakening of conclusion or recovery by an imported target alias. Only BOTH genuinely generated binder macro scopes may compare after exact erased-name agreement; raw originals are always retained. No constant/written-name/BinderInfo/mdata/general Name map is normalized.

## Phases 5a and 5b — Refactoring/rename result

No non-rename API refactor, new helper, convenience wrapper, definition change or caller repair. Local rename queue is empty; target naming passes. The owner retains the five project-end rename queue and other files. No central/shared logs were modified here.

## Phase 6 — Verification and seven diff gates

| Gate | Evidence/result |
|---|---|
| lake_build_file | Final FULL build actually rebuilt MainLemma and exited0; complete file_path-only native errors0 |
| definition_protected | No def/abbrev line or body changed; exact source inverse |
| theorem_statement_protected | Exact actual original/current full TYPE guards; only whitespace packing of original written signature |
| structure_gate | 16 lines≤30, maxbranch3≤10; common existential conjunction must be retained |
| naming_gate | Descriptive private _aux, no forbidden pattern, no rename |
| line_packing_gate | Six-row arithmetic table above; every action ok |
| inequality_orientation_gate | Per-occurrence zero-violation scan above |

Final actual FULL build then separate Eval build passed, both terminal/drained, source immutable, defaults unchanged. `final-full-build-v1.json` and `final-eval-build-v1.json` are actual command/exit receipts; no LSP-only build assertion. Final ML/Main/Eval natives are complete unfiltered file_path-only requests with errors0/faileddeps[]/partial=false/timed_out=false, warning counts1/4/0. Each has actual source17 SHA+bytes pre→request→IMMEDIATE return→full raw save/hash/bytes/save observation→post. All9 prep/save/post execs actually returned0/no sessions, chronology in `final-native-chronology-v1.json`.

Eleven verification items: (1) full/isolated proof guards; (2) full project build; (3) separate Eval build; (4) no source sorry/admit/new axioms/native_decide; (5) actual standard3 axioms; (6) default200000/20000/512 entry/exit; (7) all nine comments preserved; (8) every introduced library identifier source-verified and compiled (`Nat.pos_of_mul_pos_left`, finite single_le_sum, rpow/floor APIs); (9) all retained local/imported DATA/generated values checked; (10) defining-module source-presence/origin checked; (11) downstream Main/Eval and exact source/pin/static contracts checked. Items9–10 are PASS with final evidence below.

### Fresh all-retained raw proof gate

All 544 actual raw TYPEs are byte-exact against their original rows. Only the target helper VALUE changes in the local and imported inventories. The complete main theorem TYPE and VALUE remain byte-exact in both inventories. Exactly one generated helper-family declaration disappears (two local/imported rows), checked with independent actual local/loaded Name.isPrefixOf families. The final direct target VALUE equals the compiled candidate V4 and differs from the separate independent proof.

Actual final inventory: 74 local and 470 imported project declarations across13 actual defining modules, including Eval. Every record has actual raw TYPE, allowOpaque VALUE, closed/inferred/std3/default/origin guards. Per-declaration commands avoid aggregate heartbeat raises. Retained supported original TYPE constructors are compiled and compared; unsupported optional typeCode rows are qualified separately while raw guards still pass.

Final rows and actual generated-family change details: `final-pairs-acceptance-v2.json`. Four optional serializer rows / three distinct names are metadata-node limitations, not proof failures or dropped raw guards. Raw TYPES and VALUES remain retained for every row. Exact original/current loaded helper and main contract results are recorded from actual final loaded data; raw byte equality is claimed only where observed, not by normalization.

## Phase 6.5 — Fresh holistic simplify adaptation

No built-in Claude Skill(simplify) is available. The required fresh independent whole-helper holistic review was performed directly and saved in `holistic-review-candidate-v4.txt`; no nonexistent tool invocation is claimed. Reuse, mathematical boundary, generality, proof quality, duplication, inference and efficiency were reviewed independently of the rule table. Result: ISSUES-FOUND-AND-FIXED (direct scale proof, inline single-use bounds, load-bearing explicit B argument, terminal simplification and signature packing). No local recommendation remains. Later NEW independent whole-FILE review is still the owner obligation.

## Phase 6.6 — Matched performance

Prospective owner HOLD was ACKed before ANY phase preparation. Original helper15+full attached main44 doc/TYPE/body were captured with exact CLI `/Users/ramin/.elan/bin/lake env lean -j1 --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`, external420s bound, unchanged default limits. Both captures and all env/pre/post observers/postfreeze/drain completed before owner release and parsing. Full canonical command payload matches strictly after whitespace/standalone-comment removal only; no transferable parenthesis waiver. Dynamic actual Name.isPrefixOf families validate kernel/compiler roots. Only disjoint COLUMN0 command+proof+kernel+compiler+lint roots are summed; Meta/nested/trailing end are excluded, with no subtraction/double count.

| Full canonical command | BEFORE A ms | BEFORE B ms | AFTER A ms | AFTER B ms |
|---|---:|---:|---:|---:|
| helper15 | 357.203 | 364.630 | 278.616 | 281.993 |
| complete attached main44 | 659.052 | 649.965 | 650.738 | 649.658 |

BEFORE and AFTER each have internally exact actual source17/cache104/root8/setup14/package12202/core12592/binaries4/PATH/frozen parent and actual Lake environment tuples. Across stages, only MainLemma source, seven cache derivative tuples, one Roth root trace and the same MainLemma.olean package-catalog tuple change; all old tuples have byte-verified immutable saved snapshots. Setups/core/binaries, other source/availability tuples, actual Lake environment and frozen parent are exact across stages (`profile-before-after-input-binding-v1.json`). These catalogs are availability supersets, never an exact loaded closure. Each raw/source/scaffold/default binding is retained. AFTER is internally exact and all samples<750; no third/replacement/cherry-pick/noise discount needed.

No helper15 prior timing was reused, and P9 main46/foreign-caller timings were not substituted. The earlier valid Roth.roth_of_isIntegral3072.070/3040.443ms failure remains a separate Main obligation; main44 still fails length15, and GLOBAL exists_delta_bound12408.373/11188.775 and pigeonhole_count1018.335/1000.235ms remain pending final-file queues. Scoped helper speed never certifies the whole file/project. No heartbeat macro was used because installed count_heartbeats sets limits0.

## Preserved failures and corrections

All preexecution/assertion, failed mathematical probes and framework failures are retained with unique receipts. V1 runner argument order failed before Lean. Boundary V1 failed because Nat.cast_nonneg needed an explicit Real type; V2 full rerun passed. Candidate V3 inlining inferred the unfolded floor coefficient bound; V4 supplies explicit B and passes. Independent V3 strict-rpow rewrite needed the explicit base/cast bridge; V4 full proof and closure pass. Initial source patch format was rejected before writing; corrected bare-@@ patch applied exact context. Final metadata V1 raw guards were present but whole constructor comparison failed because non-atomic Name applications needed grouping and pp.width was unknown; V2 uses grouped Name and installed format.width, and the complete final series is PASS.

AFTER preparation first failed an exact inverse assertion before any file write because the replacement included separator newlines already present in the scaffold; the subsequent missing-driver invocation exited2 before spawning. The corrected replacement preserves the original separator and its full scaffold inverse is exact. No failed preparation received capture credit. Both actual AFTER samples are retained. Final-family bookkeeping initially used the local family for a loaded name; a separate actual four-group Name.isPrefixOf probe repaired the bookkeeping before acceptance, without dropping any raw guard.

No failure is erased, waived by native/cache assumptions, or treated as proof from exit0 suggestions. No production source changed during an active driver series. No limit raise, invented metadata, general normalization or weaker conclusion was introduced.

## Phase 7 and lifecycle boundary

The authorized local changes are fully implemented. ALL final acceptance remains conditional on matched AFTER captures, complete report binding, two genuinely fresh complete closure streams (their eventual actual receipts are `manifest.json` and `second-rehash.json` in the immutable private evidence root), fresh escalated full PS/current-group/source17 drain, immutable owner-evidence snapshots, and owner independent THIRD semantic/native/profile/report/live-drain review. Source/evidence become immutable after actual ALL8END. Owner holds all Git/publication/central writes; original27 author may resume only after owner acceptance/regrant. Published242/264 ML26/27 10/14 counts are unchanged by this helper audit.

Historical provenance: available predecessor/current rows, archive692 logical/645 stored+decoded blobs, generic8542 source universe, exact binary catalog tuples and old-live saved aliases must be freshly bound. Missing unselected pre-reboot data is not reconstructed. Distinct lost P8ADMIN raw bytes/time remain unknown under the 9eee5f erratum. Q12 prior returned observation1792712982.471543 and replacement1792714051.5226429 are known; old receipt bytes/SHA/exact file mtime are unknown. Do not claim full current old P8/R3 rehash. Only small immutable owner snapshots enter final closure, never mutable live owner paths.
