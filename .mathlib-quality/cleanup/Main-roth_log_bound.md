# `Roth.roth_log_bound_aux` — independent necessary-helper cleanup

Status: local helper audit complete; parent audit/publication/count credit is pending the owner's separate acceptance and same-author continuation. Scope is this private helper and this report only. The other four accepted helpers, their ordinary comments and reports, the parent proof/callers, imports and all bytes outside this target were left unchanged. No Git operation or shared-progress write was performed.

The helper expresses the numerical logarithmic stage: balanced degree-log estimates, the coefficient power bound, the product-factor bound and a product greater than one imply `G * κ < m * (1 + 4 * δ)`. It does not package polynomial/integral assumptions or forward a tuple/wrapper.

The genuine first draft was saved before any helper Lean/golf work at `/private/tmp/roth-main-integral-roth/helper-log-FIRSTUNGOLFED.lean`, SHA256 `31d4042a514da96d93db50fa8b00c46a8744920ecc0c8b2a38b9db2e96f3fb84`; 46 declaration / 38 body lines. The entry Main SHA256 was `523cc92f9aa5fee12acefe388b3bb71d786b90b511d7aaea6354f9ff9d00abf2`. The first-draft profile was captured from its immutable exact prefix before accepting any changed final timing; production was never reverted for timing.

Final Main SHA256: `c13cf8d82642ec67d64d87eb27cb3cca90f2965c99f6cd94607775a0b84f2746`. Final target SHA256: `ed03f76f9d2782431d729ba11a296ba440cdb11a8c6749f4a77b2c30a42e01ad`. Final target spans lines 500–535: 36 declaration / 30 ordinary substantive body lines; maximum width 99. There are no explicit case branches; no branch exceeds the 10-line limit. No extra helper, weaker conclusion, new axiom, `sorry`, trust escape or resource override was introduced.

The proof now expands logarithms, bounds the finite sum directly with `trans_eq`, and cancels the positive common degree-log factor. Single-use positivity/logarithm aliases are inlined; supplied-fact arithmetic uses `linarith only`. Trace-backed normalization retains a separate degree-cardinality cast and direct order/division sign derivation. The ordinary helper comment and exact `-- take logarithms` signpost are preserved; a private helper needs no docstring. Naming and visibility remain appropriate.

Two redundant hypotheses were actually removed: `0 < r 0` and `0 ≤ δ` follow from the strict balance estimate at index zero and `1 < q 0`. The supported paired weakening compiled. The parent's future call order is `roth_log_bound_aux hm2 hδ1 hq1 h53 hBpos hBX hN hone`; the parent has not yet consumed this helper and was not edited here.

## Full audit and search evidence

The installed lean4 and mathlib-quality skills, full cleanup/cleanup-all commands and required references were read. The initial 24-item audit and all 42 rule dispositions below were rechecked against the final source before its gates. Initial scan decisions are historical where the final correction explicitly supersedes them.

| Item | Concrete finding/action |
|---|---|
|1 LINT|Final FULL, Eval, native checks and complete unfiltered diagnostics passed; details below.|
|2 HAVE|Full scan below; inline single-use positivity facts and compose finite-sum order directly.|
|3 SET_OPTION|None; preserve default 200000/20000/512.|
|4 SIMP|Original nonterminal `simp only [Real.log_pow]` deterministic; replace together with log-product rewrite by `simp_rw`. Original terminal sum normalization remains bare `simp`.|
|5 NAMING|`roth_log_bound_aux` states subject/operation, snake_case, private `_aux`, no forbidden abbreviation/pattern; no rename.|
|6 PACKING|All six final signature lines measured below, including `:= by`; no fitting next unit remains.|
|7 BY|All `by` attached; preserve.|
|8 FORMAT|Two-space body, no blank lines or tactic semicolons; replace mathematical lambdas by ↦.|
|9 COMMENTS|Preserve and re-anchor the exact `-- take logarithms` signpost.|
|10 DOCSTRING|Private numerical helper: no docstring; retain immediate ordinary mathematical comment.|
|11 VISIBILITY|Private file-local numerical stage; retain.|
|12 STRUCTURE|38 body lines requires substantive shortening to ≤30, branches ≤10, no extra helper justified.|
|13 MATHLIB|Five searches found partial general APIs; use log_prod/log_rpow, finite sum strict order and positive-factor cancellation directly. Exact? failed on actual whole goal.|
|14 JUNK DEF|n/a: theorem, no data definition.|
|15 EXISTS|n/a: numerical strict inequality, not existential.|
|16 SHOW|Real numeric/coefficient ascriptions fix intended arithmetic types; no redundant tactic-mode show/change.|
|17 PUSH_NEG|None.|
|18 GENERALISE|Bounded actual scratch proof removed both hr0 and hδ0 by deriving them from h53 at zero and hq1; retain real logarithm setting, index size and all remaining numerical hypotheses pending drop tests.|
|19 INEQUALITY|Signature contains no ≥ or >; all inequalities use ≤/<.|
|20 NORMAL-FORM|Real log/product/order APIs and strict numerical conclusion already canonical.|
|21 SYNTAX-GEN|Separate balanced-degree and coefficient hypotheses match parent stage outputs; weaker signature removes two redundant arguments.|
|22 IMPORT-FANOUT|No import changes.|
|23 CASTS|Nat→Real coercions are genuine cross-type bridges; `(0 : ℝ)`/`(2 : ℝ)` fix arithmetic target, not redundant value casts.|
|24 INSTANCE-NAME|n/a: no instance declaration; anonymous NeZero binder checked by actual hygiene metadata.|

Initial HAVE scan (all occurrences):

| Have | Shape/use | Action |
|---|---|---|
|hmR|by exact_mod_cast; arithmetic proof|inline at only supplied-fact use|
|hqR|fun/by, reused log/powers|keep|
|hℓ|fun term, only hK0|inline|
|hr0R|by cast, only hK0|inline in hK0|
|hP0|term, only log_mul|inline|
|hN'0|by positivity, used log_mul/log bound|keep without N' alias|
|hT0|term, only log_mul|inline|
|hBc0|term, used positivity/log_mul|inline explicitly, removing slow alias-based positivity|
|hlog|term, rw and arithmetic|keep|
|hlogP|by, sum comparison|direct trans_eq; retain proof block|
|hlogN|by log monotonicity|compose with log_rpow; re-audit any single-use term|
|hlogB|by log monotonicity|compose with log_rpow; re-audit any single-use term|
|hK0|term, cancellation|derive once and reuse in δ0 derivation/cancellation|
|hkey|by arithmetic|replace with direct positive-factor cancellation|
|h1|term, only arithmetic|inline after explicit supplied-fact arithmetic|
|hpos|term, final arithmetic|keep proof content after direct cancellation|
|h2|term, only final arithmetic|inline at final supplied-fact use|

Five-method search: Lean-Finder query “real logarithm of finite product powers finite sum strict bound cancellation positive factor” returned general logb/posLog product APIs, not this numerical stage; Loogle `Real.log (∏ x ∈ _, _) = _` returned Real.log_prod; LeanSearch “strict bound on finite sum by constant times cardinality” returned cardinality/sum inequalities; source search found Real.log_prod, Real.log_rpow and generated sum_lt_sum_of_nonempty; name search sum_lt_sum_of_nonempty returned ENat/ENNReal source matches with index unavailable (not absence evidence). Auxiliary variants log_mul/log_pow/log_le_log/log_lt_log, sum strict nonempty and positive-factor cancellation are used directly. No custom predicates/common-equivalents bucket applies. Compiled actual-goal exact? failed; grind failed; aesop exhausted. No claim that a source-only search proves absence.

# All 42 golfing rules

| Rule | Disposition |
|---|---|
|1.1 by exact|No sole wrapper; inline facts at uses.|
|1.2 by rfl|n/a: none.|
|1.3 rw+exact|Replaced logarithm monotonicity rewrite/exact blocks by direct trans_eq.|
|1.4 simp+exact|Sum comparison directly trans_eq; no remaining matching pair.|
|1.5 simp+rfl|n/a: none.|
|1.6 constructor|n/a: strict inequality, no conjunction goal.|
|1.7 apply+exact|Direct composed cancellation/order terms.|
|1.8 by_contra+push|n/a: no contradiction/push pair.|
|1.9 eta|No redundant lambda; pointwise hypotheses genuinely use the index.|
|1.10 have inline|Inline hℓ, hr0R, hP0, hT0, hBc0, hlogN, hlogB, h1, h2; final have scan separately.|
|1.11 apply+intro|n/a: none.|
|1.12 show|Only term-mode numeric target ascription retained; no redundant tactic show.|
|1.13 projections|n/a: no have+projection pattern.|
|1.14 merge rw|Log expansions in one rewrite list; log_prod/log_pow in one simp_rw.|
|1.15 terminal simp|Retain bare terminal sum-normalization simp.|
|1.16 nonterminal simp|Deterministic simp_rw with exact two APIs; no bare nonterminal simp.|
|1.17 dot|Use .trans_eq, .mp and .ne' directly.|
|1.18 <\||Positive-factor cancellation feeds its proof block with <\|.|
|1.19 push_neg|n/a: absent.|
|1.20 exists inline|n/a: no existential helper.|
|2.1 grind|Actual-goal LSP attempt failed; retained logarithmic proof.|
|2.2 before grind|n/a: no retained grind.|
|2.3 simpa|Derive hr0 by terminal simpa [h] using h53 0.|
|2.4 fun_prop|n/a: no function regularity goal.|
|2.5 positivity|Product factor positivity; trace-heavy rpow/product positivity replaced by explicit APIs.|
|2.6 gcongr|Direct one-step mul_le_mul_of_nonneg_left/right is shorter and supplies exactly arithmetic facts; no monotonicity chain remains.|
|2.7 lia/omega|No standalone integer-arithmetic chain: cast hm2 directly; no omega introduced.|
|2.8 aesop|Actual-goal LSP exhaustive search failed; retained proof.|
|2.9 norm_num/cast|exact_mod_cast on genuine Nat/Real positivity and m bound; no numeric-computation goal.|
|2.10 decide|n/a: real logarithmic universal inequality, no finite computation.|
|2.11 field_simp/ring|n/a: no rational identity subgoal.|
|2.12 linear_combination|n/a: no proof ending ring/ring_nf with hypotheses.|
|2.13 wlog|n/a: no symmetric case split.|
|2.14 calc term|Finite-sum calc replaced by trans_eq.|
|2.15 <;>|n/a: no multiple similar subgoals.|
|3.1 erw|n/a: absent.|
|3.2 fun_prop|n/a: no legacy regularity tactic.|
|3.3 omega→lia|n/a: omega absent in final target; cast instead.|
|3.4 rcases rfl|n/a: no rcases.|
|3.5 attributes|Private one-use numerical stage; no global automation attribute justified.|
|3.6 simp_all|n/a: no closing simp_all only.|
|3.7 resources|No override present or added; default budgets checked on every semantic/profile row.|

Step back: exact?, grind, aesop failed on the actual goal. The proof needs the logarithm identity, strict finite sum estimate and positive-factor cancellation. The trace-backed change removes expensive aliased-rpow positivity and restricts arithmetic premises; a new helper or a one-tactic replacement is not justified.

Simplify is unavailable in installed capabilities; no invocation is claimed. Manual substantive holistic review checked necessity, single-use HAVE facts, direct finite-sum composition, logarithm positivity, cancellation, duplicate stages and cast load. No cross-declaration change is authorized here; the owner performs fresh whole-file review later.

# Per-binder generalisation

Actual scratch tests: `weakening-tests-result.json` records fifteen serial-compiler test cases; `weakening-terminal.json` separately verifies the supported paired removal. Failed drop tests establish proof dependency, not mathematical impossibility. No stronger absence claim is made.

| Binder | Kind/use | Candidate/result |
|---|---|---|
|m : ℕ|Index cardinality and Fin m|Cannot drop from dependent statement; abstract index restatement changes API and is unnecessary for numerical stage.|
|[NeZero m]|Instance for Fin numeral zero/nonempty|Actual remove-instance probe failed; retain.|
|hm2 : 2 ≤ m|Final coefficient comparison|Actual drop and 1 ≤ m weakening failed (required cast 2 ≤ m); retain.|
|δ : ℝ|Real exponent and coefficient|Dependent statement value; cannot drop; logarithm APIs require real setting.|
|G : ℝ|Conclusion and exponent product|Dependent statement value; cannot drop; replacing G*κ by a parameter changes argument shape, not an assumption weakening.|
|κ : ℝ|Conclusion and exponent product|Dependent statement value; cannot drop; same reason as G.|
|B : ℝ|Coefficient scale/logarithm|Dependent statement value; cannot drop.|
|hδ0 : 0 ≤ δ|Original sign assumption|Actual independent scratch proof derives it by nlinarith only [h53 0,hK0]; dropped and retained.|
|hδ1 : δ ≤ 1|Coefficient comparison|Actual drop failed at final arithmetic; already weak inequality, no strict→weak candidate.|
|q : Fin m → ℕ|Denominators|Dependent value; cannot drop; no function regularity/typeclass weakening applies.|
|r : Fin m → ℕ|Degrees|Dependent value; cannot drop; no function regularity/typeclass weakening applies.|
|hq1 : ∀ j, 1 < q j|Positive real logs and nonzero powers|Actual drop and ∀j,0<qj weakening failed (log_pos requires 1<q0); retain. Point-localization would change statement/caller shape and does not cover log_prod nonzeros.|
|hr0 : 0 < r 0|Original positive degree assumption|Actual independent scratch proof derives from strict h53 0 by ruling out r0=0; dropped and retained.|
|h53 : ∀j, rj*log(qj) < (1+δ/10)*(r0*log(q0))|Strict sum and sign derivation|Actual drop and ≤ weakening failed (hr0 derivation and strict sum); retain. Global finite-sum bound uses every j, no point-localization.|
|hBpos : 0 < B|Real logarithm monotonicity/rpow|Actual drop and 0≤B weakening failed at log/rpow APIs; retain.|
|hBX : B ≤ q0^(δ*r0)|Upper coefficient bound|Actual drop failed at log_le_log; already nonstrict.|
|hN : product(rj+1) < B^δ|Strict degree-factor estimate|Actual drop and ≤ weakening failed at log_lt_log; retain.|
|hone : 1 < denominatorProduct*coefficientProduct|Positive total logarithm|Actual drop and 1≤... weakening failed at log_pos; retain.|

No type variable/universe binder exists in the explicit numerical statement. Actual generated family universes are enumerated before semantics guards; no empty-universe assumption is made. No algebra/analysis structure parameter admits a catalogue parent-class weakening. Literature search is n/a for this private helper. Inversion check: the statement already abstracts all polynomial/integral data to meaningful numerical bounds; no concrete named witness survives to abstract further. No additional helper or large generalisation is justified.


## Final HAVE, packing and correction review

The authoritative final HAVE scan is: `hr0`, `hδ0`, `hlogP`, `hpos` and `hmR` contain real proof content; `hK0`, `hqR` and `hN0` are reused; `hlog` is rewritten and then supplied to arithmetic. No single-use no-`by` have remains. The initial plan to inline `hmR` was reversed only after the actual nested-cast/coefficient trace cost justified isolating that cast. Initial alias-based positivity and later terminal sum `simpa` were replaced by explicit positive factors and the direct finite-sum `trans_eq`. No late format-only cycle was applied to the final c13 source.

| Signature line | Width | Next complete unit width | Width with space and next unit | Result |
|---|---:|---:|---:|---|
|500|93|17|111|ok|
|501|42|79|122|ok|
|502|99|33|133|ok|
|503|75|80|156|ok|
|504|84|34|119|ok|
|505|72|none|n/a|ok|

The table includes the final conclusion and `:= by`. Maximum width is 99; the inequality scan found no `≥` or `>` in the target. Final pre-gate review covered all 24 items/42 rules, every binder, casts, documentation, naming, imports, all HAVEs and every signature line. Simplify is unavailable in the installed capabilities, so no invocation is claimed; a substantive manual holistic review checked stage necessity, duplicate work, direct APIs, arithmetic premises, casts and possible one-tactic/extra-helper replacements. Fresh whole-file review remains the owner's later work.

## Validation, strict semantics and independent proof

All compiler, native, LSP and semantic jobs ran serially, with each prior job actually terminal before the next. The final fully packed c13 source was frozen before these gates:

| Gate | Actual result |
|---|---|
|`lake build`|PASS, 59.917 s|
|separate `lake build Roth.LeanEval`|PASS, 33.475 s|
|native Main / LeanEval / root|PASS, 35.965 / 33.594 / 35.466 s|
|complete unfiltered LSP Main / LeanEval / root|success, partial=false, zero errors; Main only the pre-existing line-1 short-copyright warning, Eval/root empty|
|new production TYPE/VALUE semantics|PASS, 117.297 s|
|actual final profile/current TYPE-only binding|PASS, 54.682 s; no VALUE re-inference|

Actual complete families and universe lists were enumerated before guards, rather than inferred from suffix counts or assumed empty. The observed families are production `_private.Roth.Main.0.Roth.roth_log_bound_aux`, independent `Roth.independentLogBound`, recovery `Roth.recoverLogBound`, each a singleton with observed universe list `[]`. Final re-enumeration and complete raw TYPE bytes/strict recursive fields matched accepted current metadata for all three.

The independent proof imports only Roth.MainLemma and proves the weakened numerical contract using the original logarithm/sum strategy, separate from the production direct-cancellation proof. It compiled in 30.468 s. The recovery theorem states the exact original contract and calls that independent theorem; it compiled in 30.422 s. Its two intentional scratch-only unused old assumptions do not occur in production. Recovery proves that the old statement follows from the new contract; it does not assert proof-value identity. Unchanged independent/recovery sources, oleans, valid TYPE and VALUE rows were bound by exact hashes and reused without replay/re-inference on later production-only edits.

The first semantic batch successfully inferred and checked every actual opaque VALUE in memory, closed and under the standard axiom set, then failed its aggregate raw TYPE guard on actual anonymous NeZero binder hygiene. Those valid rows were preserved, and only the outstanding TYPE guard was supplemented. Full recursive Name/Level/Expr/BinderInfo/metadata/source-information/literal/projection comparison uses no ExprBEq shortcut. The two actual old/recovery and current/independent second-binder Name pairs have matching instImplicit/path, both Names.hasMacroScopes, and equal eraseMacroScopes. Raw originals remain unequal; after those exact finite literal name substitutions, all remaining complete raw TYPE bytes and recursive fields agree. No suffix-wide or other broad normalization is allowed. All pasted actual `«_@»` Name components were quoted before compiler use, and private declarations use actual Name expressions.

Final production VALUE was freshly inferred/closed/checked in memory: bytes 26,121,574, Lean hash `4955440742363225857`, axioms exactly `propext`, `Classical.choice`, `Quot.sound`, defaults maxHeartbeats/synthInstance/maxRecDepth `200000/20000/512`, no local edges. Independent has no local edge; recovery has only its independent edge. The local graph is acyclic, with actual external module indices strictly upstream of Main; no accepted helper was cloned/reproved/re-inferred and no entire imported DAG was replayed. These receipts record hashes/lengths, not full raw VALUE dumps or cross-proof VALUE identity.

Both regular final profile captures observe the actual family `_private._stdin.0.Roth.roth_log_bound_aux`, observed universes `[]`, its opaque VALUE under defaults, and the complete raw TYPE. Their TYPE/name/universe metadata agree exactly. The actual production/profile raw TYPE mismatch was then bound by a TYPE-only check: solely the observed second-binder instImplicit Name pair, both actual Names.hasMacroScopes/equal eraseMacroScopes; complete remaining raw bytes and every strict recursive field agree. No production, independent or recovery VALUE was re-inferred for this supplemental check. Prefix VALUE hashes/lengths are separate observations, not production identity claims.

Evidence: `/private/tmp/roth-main-roth-log-bound/revision3-semantics-receipt.json`, `revision3-actual-families-before-guards.json`, `revision3-production-valid-rows.json`, `finite-hygiene-actual.json`, `profile-current-actual-type-pair.json`, and exact LSP/driver/terminal artifacts in the same directory.

## Exact scoped performance

Each phase began only after the owner's HOLD ACK before any preparation. The owner stayed idle through capture, frozen-source/tool/maps checks, actual default checks and full parent/Lake environment byte equality in memory. Only hashes/lengths and the approved PATH/Lean/toolchain allowlist were persisted; process argument observations were limited to task-owned processes and requested escalation first. Every actual driver and all five childgroups were terminal 0 and absent before a RAW UNPARSED notice; parsing started only after the explicit OWNER RELEASE.

Each exact prefix keeps the production imports, preceding commands and full target bytes, then closes the namespace and adds actual family/TYPE/VALUE/default and width-100 observation. Command: `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Prefix.lean`. Full canonical target matching, actual family enumeration and disjoint outer command + actual async proof + kernel/compiler parents + lint roots avoid nested double counts. The actual Mathlib expandLemma macro and Lean recursive elabCommand/addTraceAsMessages source explain inner trace flushing before the canonical outer command; indentation alone was not used to guess command identity. Compiler and lazy-prior-DATA root sets were actually empty for this target.

| Proof context / exact capture | Milliseconds | Result |
|---|---:|---|
|genuine first draft / firstdraft-profile|1178.250|VALID FAIL|
|genuine same-freeze required repeat / firstdraft-repeat|1130.170|VALID FAIL|
|first cleaned state / final-profile|929.880|PASS|
|same first-cleaned state required repeat / final-repeat|1011.605|VALID FAIL; state rejected|
|direct positivity state / optimized-profile|1080.183|VALID FAIL|
|same state required repeat / optimized-repeat|1120.377|VALID FAIL|
|final c13 residual normalization / residual-profile|962.731|PASS|
|same immutable c13 prefix/command required repeat / residual-repeat|852.705|PASS|

Every ≥750 sample received its one mandatory same-freeze repeat after a fresh HOLD ACK; no unchanged third sample was taken. Every valid failure remains retained against its own actual source context. No timing ratio, cherry-picking, noise dismissal or causal waiver is claimed. The earlier failures drove substantive proof corrections: explicit positivity/cancellation, then direct sum trans_eq, direct δ-sign APIs and isolated cast/coefficient comparison.

Final first sample is 83.900 outer + 826.467 proof + 22.897 kernel parent + 29.467 lint = 962.731 ms; final repeat is 77.040 + 726.743 + 21.103 + 27.819 = 852.705 ms. Both are below 1000 ms. The original kernel child is contained in its parent and not counted twice. The same immutable residual-profile/Prefix.lean path, options, default settings, family and frozen source were used for the required repeat.

## Qualifications and phase close

Failed bounded scratch probes are evidence of failure for those candidate proofs, not mathematical impossibility: eight retained-hypothesis drop probes, six proposed relaxations and one instance removal all failed; the supported paired removal passed. The one actual-goal exact?/grind/aesop batch failed/exhausted, so no repeated broad automation was attempted. Other retained scratch corrections were a missing type on inlined coefficient arithmetic, a cancellation orientation/metavariable issue, and the wrong implicit multiplier parameter `c` corrected to source-verified `a`. These failures are not final production diagnostics.

One earlier signature-only packing correction moved a single factor before final proof revision: pre `35a0473f3452f38981c964555b49ec4249e0d7a1ffb191971e2f308fa330288a`, post `2e91ac6d79d518345a73cf829b68cb76145470f12454506f3203cd9177161661`. Exact proof-body bytes and declaration token stream were identical, outside-target bytes exact; the owner allowed completed FULL/Eval/native evidence reuse for that narrow whitespace change (one already-running extra Main native finished and drained). Its packed-source diagnostics/semantics/profile were current, and its profile failures were retained. The final c13 proof change then reran all affected FULL/Eval/native/LSP/new-production semantics gates; current final gate results above do not rely on that packing exception.

Phase checklist: genuine pre-work save; initial 24-item audit; five-method search; one bounded actual-goal automation batch; substantive shortening; per-binder implemented weakening/drop tests; all 42 rules; final HAVE/cast/inequality/comment/packing/holistic review; serial FULL; separate Eval; fresh natives; complete unfiltered diagnostics; actual family/universe enumeration; strict TYPE plus opaque VALUE/default/closure/std checks; independent old-contract recovery; exact final profile and mandatory same-freeze repeat; actual profile/current TYPE binding; scoped report; final actual process drain and all-lease release. The owner must still locally accept this helper, resume the same author's parent proof, run parent/whole-file gates, and jointly publish; no standalone publication or parent audit/count credit is claimed.
