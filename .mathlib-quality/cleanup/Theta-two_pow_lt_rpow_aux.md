# Fresh private-helper audit: `two_pow_lt_rpow_aux`

Scope: this new private helper and the single necessary application inside public original32 `lem6M_lt`. No original-count increment. No Git, shared-log, header, import, public-statement, other-helper or unrelated proof changes. Evidence directory: `/private/tmp/roth-exponential-audit/`.

## Baseline, instructions and mathematics

Exact inherited source SHA256 `88184680e2461359c26db220177f45648e6c1827467f401a9a2c74340785b4c4`,948 lines. Baseline complete native diagnostics and real trace are inherited from `/private/tmp/roth-coefficient-audit/`: zero errors/eight warnings; exponential513.609ms, coefficient216.980ms, public32614.335ms. These are inherited measurements, not fresh. The module/compatibility exits0 in the preceding frozen handoff establish baseline compilation. Full-project and separate LeanEval gates belong to the owner.

Read the lean4 and mathlib-quality skills, cleanup worker workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, relevant style and naming sections. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Classic file dialect. The dispatch/common instructions take precedence over generic whole-file workflow and original-statement permission language. The parent approved applying a supported private q-nonnegativity weakening under the user's standing authority.

Mathematics: `log 2 < 1` and positivity of `2p+1` turn the assumed logarithmic lower bound into a strict comparison. Multiplication by the positive product `l*r₁` preserves strictness; cast normalization and exponentiation recover the stated natural-power/real-power comparison. This is a substantive estimate with division/sign control and exponent normalization, beyond a1–3-call wrapper.

Applied private weakening: `hq : 0 < q` becomes `hq : 0 ≤ q`. The remaining positive lower bound on `log q` yields `1 < q`, hence positivity internally. The original contract has the exact adapter `actualExponential hp hδ hq.le hlog hlr`. The public32 application changes only `hq1pos` to `hq1pos.le`. Its public statement is unchanged. Two one-use facts h4/hlr0 are inlined; the local log2 bound uses the existing analytic lemma and numeric endpoint equality rather than linarith. The independently compiled candidate is `candidate.lean/.log` exit0; the first failed simpa attempt is described in the audit below, not used as evidence. Helper body20→21 lines and module948→949 lines, accommodating the weaker premise without a new helper.

## Full 24-item audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|Lint|No helper-range warning in module output. Final complete unfiltered diagnostics and all retained warnings are recorded below.|
|2|Have scan|Initial hp0: by/exact_mod_cast, keep; hlog2: by analytic bound, keep its proof content; inner unnamed log bound: no-by/one-use, compose directly; h3: by division normalization/linarith, keep; h4: no-by/one-use, inline; hlr0: by exact_mod_cast, safely inline its one use. New replace hq derives positivity from the weaker premise.|
|3|Set option|No production option, limit raise, trace, linter mask, or profiling scaffold.10000 heartbeat caps exist only in negative scratch.|
|4|Simp squeeze|No production simp. A terminal simpa numeric-endpoint trial failed because `2-1` was not reduced; corrected by explicit numeric equality. Whole simp made no progress.|
|5|Naming|`two_pow_lt_rpow_aux` describes the compared expressions, snake_case, permitted unnumbered `_aux`, no forbidden abbreviation/pattern or reversed inequality suffix. No rename.|
|6|Line packing|All three signature lines measured by Unicode codepoint; table below.|
|7|By placement|`by` remains on preceding signature/have/calc line.|
|8|Format|2-space proof indentation, no empty proof lines, trailing whitespace, semicolons, haveI/letI or lambda.|
|9|Comments|No original helper comments. Public32 signpost and all docstrings preserved verbatim.|
|10|Docstring|Private helper has none; no new public documentation required.|
|11|Visibility|Retain private with one local technical consumer.|
|12|Structure|21 body lines≤30; no conjunction or case branch; h3 is3 lines, cast/ring subproof2 lines. No extraction.|
|13|Mathlib|Five actual responsive methods, complete local source search, clean anonymous exact?/apply? fallback. Partial analytic building blocks found, no whole-result replacement located; no absolute absence claim.|
|14|Junk definition|n/a: lemma, no def/abbrev changed.|
|15|Existential lemma|n/a: no existential witness/result.|
|16|Show/change|Neither appears.|
|17|Push negation|No push_neg or negation tactics.|
|18|Generalise|Every effective binder has a compiled drop probe; strict weakening tests and successful nonnegative-q proof below. No hidden section instances in actual helper type.|
|19|Inequality|All signature/body inequalities use < or ≤; full occurrence table below.|
|20|Normal form|Real log/rpow and natural exponents are native Mathlib expressions. No custom predicate, quotient representation or equivalence API.|
|21|Syntactic generality|Nonnegative q is enough at the application boundary; exact initial adapter and minimal caller proof provide recovery. No reordered arguments or changed conclusion.|
|22|Import fanout|No new production import. Decimal log2 bound tested but unavailable under existing imports; no extra import introduced.|
|23|Casts|Nat→Real casts identify the genuinely mixed exponent domains. Real numeric ascriptions fix the intended analytic field. No redundant same-type coercion introduced.|
|24|Instance names|n/a: no instance declarations/effective class binders.|

## Signature packing and inequality orientation

Actual #check at format.width100 is in final compatibility/positive logs. Widths include indentation and `:= by`.

|Signature line|Codepoints|Next logical group|Arithmetic|Action|
|---|---:|---|---|---|
|615|95|`(hlog : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q)`,47|95+1+47=143|ok|
|616|72|`(2 : ℝ) ^ ((2 * p + 1) * r₁ * l)`,32|72+1+32=105|ok|
|617|67|none, proof follows|n/a|ok|

|Occurrence|Location|Expression/orientation|Action|
|---|---|---|---|
|1|hp|0 < p|none|
|2|hδ|0 < δ|none|
|3|initial/final hq|0 < q → 0 ≤ q|supported weakening; orientation preserved|
|4|hlog|p*(2p+1)/δ ≤ log q|none|
|5|hlr|0 < l*r₁|none|
|6|conclusion|natural power < real power|none|
|7|body hp0/hq/hlog2/h3/calc|0<p;0<q;log2<1;2p+1≤logq*(δ/p);scaled strict comparison|none|
|8|entire signature/body|zero ≥/>|no rewrite or rename|

## Five actual searches

Raw native results `native-searches.json`; source search `mathlib-rg.log` is unfiltered. `Pow/Real.lean` analytic comparison section inspected directly. The full helper name search has no Mathlib source hit.

|Method|Actual query|Result|
|---|---|---|
|A Lean-Finder|natural power of two less than real power from a lower bound on logarithm|Five hits including Real.pow_lt_of_lt_log; a building block rather than the coefficient/log lower-bound estimate.|
|B Loogle|`Real.log, _ < 1`|Eight hits including logarithm and log series inequalities; no exact full estimate.|
|C LeanSearch|The natural logarithm of two is less than one|Real.log_two_lt_d9 and Real.log_lt_sub_one_of_pos among five hits.|
|D Source rg|log_two_lt, log_lt_one, rpow_lt_rpow_iff, logarithm/rpow bounds, exact helper name in analytic source files|Real.rpow_lt_rpow_iff, log/rpow comparison iff variants, and base-log facts located.|
|E Local name|log_two_lt|Real.log_two_lt_d9 returned; index=unavailable, so no index-completeness claim.|

Auxiliary variants include Real.rpow_lt_iff_lt_log, Real.pow_lt_iff_lt_log, Real.lt_rpow_iff_log_lt, Real.pow_lt_of_lt_log, Real.rpow_def_of_pos and Real.log_lt_sub_one_of_pos. The common-equivalents topology/finiteness/bornology table has no match. The mixed-natural exponent transformation and strict scaled logarithmic bound still require the substantive local calculation; no1–3-call full-result replacement found.

`analytic-trials.lean/.log` confirms that Real.log_two_lt_d9 is unknown under the unchanged imports. The existing generic log bound is available and suffices. No source/import/name is invented to obtain a decimal inequality. This expected-failure file does not certify proof values; corrected positive analytic trials are included in the independent-first-values exit0 gate.

`negative-automation.lean/.log` uses the exact source prefix ending BEFORE this helper, anonymous examples, and conservative10000 heartbeat caps. It contains neither this already-proved target nor named failed target declarations. grind, simp, aesop, exact?, positivity, gcongr, lia, norm_num do not close the full result. apply? offers generic partial inequalities and reaches the deliberate lower cap. No direct replacement emerged. This is bounded search evidence, not a proof of global absence. Per the recorded repeated native multi_attempt stalls, that unbounded live-file experiment was not repeated; ordinary isolated compilation is the instructed fallback.

## Every-effective-binder generalisation and inversion

`negative-binders.lean/.log` exit1 is a separate expected-failure file with autoImplicit=false. It is never imported for proof search, compatibility or axioms. Removing value binders correctly gives unknown-identifier errors rather than silently reintroducing them. Removing hypotheses breaks the selected proof; these failures alone do not establish mathematical necessity.

|Binder|Kind/use|Actual compiled candidate|Result|
|---|---|---|---|
|p:ℕ|value; natural exponent and divisor|drop with autoImplicit=false|unknown p; retained. Nat exponent role intrinsic, not arbitrarily widened.|
|r₁:ℕ|value; natural exponent/product|drop with autoImplicit=false|unknown r₁; retained.|
|l:ℕ|value; natural exponent/product|drop with autoImplicit=false|unknown l; retained.|
|δ:ℝ|value; real division/exponent|drop with autoImplicit=false|unknown δ; retained. Logarithm/rpow are Real APIs, no ordered-field-only restatement.|
|q:ℝ|value; logarithm/rpow base|drop with autoImplicit=false|unknown q; retained. Already Real, not fixed to caller's Nat domain.|
|hp:0<p|proposition; positive denominator|drop; weaken to0≤p|drop loses hp; weak version fails strict cast hp0. p=0 is a genuine obstruction because δ/p=0; retain.|
|hδ:0<δ|proposition; positive division|drop; weaken to0≤δ|drop loses hδ; weak version cannot apply div_le_iff₀. δ=0 is a genuine obstruction because hlog divides by0; retain.|
|hq:0<q|proposition; rpow definition|drop; weaken to0≤q with positive-log derivation|drop loses hq; nonnegative candidate compiles independently and in module; applied. Positive logarithm plus nonnegativity implies q>1.|
|hlog:lower bound≤log q|proposition; quantitative comparison|drop|unknown hlog; retained. Already weak ≤; no global-to-pointwise/bundled-map alternative.|
|hlr:0<l*r₁|proposition; strict scaling|drop; weaken to0≤l*r₁|drop loses hlr; weak form fails strict product cast. Zero product makes both powers1 and strict comparison false.|

No type variables, universe binders, typeclasses, decidability parameters, bundled function properties or global hypotheses appear in the actual effective type. No corresponding parent-class/point-localisation/universe weakening applies. Exact initial proof is independently reproduced, not proved by invoking the live helper. Both first helper values and standard axioms are checked independently as required.

Literature status: n/a: private declaration; external literature search is exempt under the workflow. Inversion check: no project-specific named construction disappears after an unfolding. Real.log and Real.rpow are used throughout. Replacing base2 or `2p+1` by arbitrary values and taking the desired strict scaled log inequality as a hypothesis would largely restate the existing generic analytic comparison; no additional arbitrary-domain widening is proposed. The meaningful mechanical weakening of q is applied.

## All 42 golfing rules

|Rule|Status|
|---|---|
|1.1 by exact wrapper|No whole-proof wrapper. Local log2 bound composes the existing analytic lemma with an explicitly proved numeric equality; no separate one-use unnamed bound remains.|
|1.2 by rfl|n/a: none.|
|1.3 rw+exact→rwa|n/a: normalization rewrites feed linarith/calc rather than exact.|
|1.4 simp+exact→simpa|Attempted terminal numeric simpa did not normalize2-1; explicit endpoint equality selected.|
|1.5 simp;rfl|n/a: none.|
|1.6 constructors|n/a: no conjunction.|
|1.7 apply;exact|n/a: no such chain.|
|1.8 by_contra!|n/a: no contradiction chain.|
|1.9 eta reduction|n/a: no lambda.|
|1.10 inline single-use have|Applied to unnamed logarithm bound and h4; also inlined hlr0's cast proof. h3/hp0 retain proof content.|
|1.11 refine+fun|n/a: no introductions.|
|1.12 redundant show|n/a: none.|
|1.13 obtain projections|n/a: no conjunction/existential products.|
|1.14 merge rw|h3 rewrites target then hypothesis: distinct locations require two commands. Main exponential rewrites already merged.|
|1.15 unsqueeze terminal simp|n/a: none.|
|1.16 squeeze nonterminal simp|n/a: no production simp.|
|1.17 dot notation|Uses .trans_le and .trans_eq for the analytic/numeric chain.|
|1.18 <\||Used in q positivity derivation; remaining parentheses delimit method receivers/arguments.|
|1.19 push Not|n/a: no push_neg.|
|1.20 existential inlining|n/a: no witness.|
|2.1 whole grind|Actually tried; fails symbolic logarithm/exponential comparison.|
|2.2 delete before grind|n/a: no production grind.|
|2.3 simpa consolidation|Numeric endpoint trial failed; explicit equality is clearer and verified.|
|2.4 fun_prop|n/a: no function regularity goal.|
|2.5 positivity|Retained for strict logarithmic lower bound and positive scaling coefficient; whole target is not a positivity goal.|
|2.6 gcongr|Actually tried on full target; no progress. Explicit multiplication theorem records strictness correctly.|
|2.7 lia/omega|lia actually tried; cannot solve analytic inequality. Only real arithmetic remains in production; no Nat omega replacement opportunity.|
|2.8 aesop|Actually tried; exhaustive search leaves target.|
|2.9 norm_num/norm_cast|Numeric endpoint normalized; genuine Nat→Real casts use exact_mod_cast/push_cast. Whole norm_num does not prove symbolic estimate.|
|2.10 decide/+kernel|n/a: symbolic real logarithm inequality, not a finite decidable computation. No native_decide.|
|2.11 field_simp;ring|n/a: division inequality requires sign-sensitive iff, not denominator-clearing an equality. Final ring treats δ/p as a shared factor without cancellation.|
|2.12 linear_combination|Both polynomial identities tried in corrected positive trials; ring remains the direct polynomial identity tactic of equal length.|
|2.13 wlog|n/a: no symmetric cases.|
|2.14 collapse calc|Three links include two nontrivial polynomial identities and a strict bound; composing would obscure the cast bridge and duplicate expressions.|
|2.15 <;>|n/a: side goals have different numeric/cast/ring roles.|
|3.1 erw→rw|Already rw.|
|3.2 fun_prop migration|n/a: no continuity/measurability.|
|3.3 omega→lia|No omega retained; full lia trial recorded in2.7.|
|3.4 rcases rfl|n/a: no cases.|
|3.5 automation attributes|One-use private technical estimate; no supported global automation registration.|
|3.6 simp_all|n/a: none.|
|3.7 remove limits|No production limit present/added.|

Step-back reflection: whole-result automation and generic Mathlib routes were actually tried in a clean context. The useful structure is strict analytic comparison, positive scaling and exponent normalization. The private weakening improves the input contract without moving mathematical work into another helper. No additional API extraction or unrelated reformulation is justified.

## Compatibility, final diagnostics and scoped profile

All normal scoped gates below are complete; the final performance artifact is recorded after its process finishes. No pending owner build is claimed complete here.

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0,2423 jobs (`module-build.log`). Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-exponential-audit/actual-compatibility.lean` exited0. It preserves BOTH full immutable original namespaces byte-identically: Index13711 bytes SHA256 `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`; Theta52169 bytes SHA256 `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`. Fresh comparison and hashes are in `immutable-blocks.json`; the inherited owner block check is an additional provenance source, not substituted for this fresh comparison.

The D32First block independently reproduces both initial helpers from immutable context `/private/tmp/roth-d32-log/helpers-first-context.lean`, SHA256 `807e99748225d46c5acaeaa802f15ae3743c5357f2c10e81a339613c0e03f6cb`. The actual final private helper is located programmatically. Its type equals the separately proved final candidate's effective type; the initial adapter equals the exact independent first type. Every actual/final/first/adapter opaque proof value is checked with `info.value! true` and inferred against its type. Axioms are restricted to propext,Classical.choice,Quot.sound. No positive output contains PANIC,error or sorryAx. No self-proof is used to establish either independent initial proof.

The same exit0 verifier checks the exact original32 telescope adapter, ENTIRE independent original/current Θ_lt effective type equality, opaque values, current proof's actual lem6M_lt dependency, and standard axioms. The completed coefficient helper remains source-identical, with its earlier supported private contract and exact first adapter verified. The supplemental `independent-first-values.lean/.log` freshly compiles BOTH exact initial helper proofs and checks both opaque values/types/standard axioms; it also verifies the corrected generic log bound and both linear_combination identities. Exit0. These normal compiler requests were complete before final profiling.

Fresh complete unfiltered native `lean_diagnostic_messages` on live `Roth/Theta.lean` returned success=true,partial=false,timed_out=false,no failed dependencies,zero errors,eight warnings. Raw complete output `final-lsp.json`. Nothing was filtered by declaration, line, severity or message. No target warning. Retained warning provenance is deliberately distinguished:

|Location|Retained warning and reason|
|---|---|
|1:2|Copyright too short; header metadata explicitly out of scope.|
|93:43|hr not explicitly referenced; existing out-of-scope declaration.|
|101:27|hB not explicitly referenced; explicitly retained Θ_nonneg hypothesis.|
|101:64|hr not explicitly referenced; explicitly retained Θ_nonneg hypothesis.|
|109:28|hB not explicitly referenced; explicitly retained Θ_le_card hypothesis.|
|129:81|hr not explicitly referenced; protected existing Θ_mono hypothesis.|
|252:6|hr not explicitly referenced; existing out-of-scope declaration.|
|547:47|hq not explicitly referenced; explicitly retained earlier public hypothesis.|

|Newly used identifier/form|Verification|Result|
|---|---|---|
|Real.log_pos_iff|Returned in actual LeanSearch results; already used by caller; module/independent candidate compile|pass|
|LT.lt.trans_eq|Exact alias in Mathlib/Order/Basic.lean:89; `new-identifiers-rg.log`; actual proof compiles|pass|
|lt_of_lt_of_le,zero_lt_one.trans|Already present in public32's existing positivity derivation; actual helper compiles|pass|
|Real.log_lt_sub_one_of_pos|Actual search plus #check and corrected independent analytic proof|pass|

Only the allowed helper and single caller application changed relative to the inherited snapshot (`source.diff`); the entire file prefix before this helper is equal and its suffix is equal after the exact one-token `.le` adaptation. Comments/docstrings are unchanged, and no def/abbrev, import, header or public signature changed. Production source has no new limit/trace/scaffolding option. Signature-width rows are identical before/final because `<`→`≤` preserves codepoint width.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Actual `/Users/ramin/.elan/bin/lake build Roth.Theta`,exit0.|
|definition_protected|pass|No def/abbrev edits.|
|theorem_statement_protected|pass under authorised private weakening|Only helper hq weakens; exact initial adapter and actual final type checked; all public declarations unchanged.|
|structure_gate|pass|21 lines≤30, every subproof≤10,no conjunction.|
|naming_gate|pass|Descriptive snake_case and permitted unnumbered aux.|
|line_packing_gate|pass|Measured three rows95/72/67; next groups give143/105.|
|inequality_orientation_gate|pass|No reversed inequality/name.|
|cumulative_no_unintended_breakage|pass for owned scope|Module, exact helper recovery, untouched coefficient, full public32/entire Θ_lt semantic gates.|
|owner full build / LeanEval|pending owner|Not run by this leaf.|

Phase3 file-level fixes: n/a for this single private-helper scope. Phase5a: supported private weakening and one caller proof adaptation implemented, no new helper. Phase5b: no rename needed, no queue/shared-log write. Simplify pass: manual equivalent, PASS-THROUGH after the local bound inlining. No callable built-in simplify skill exists in this host, so no invocation is claimed. Holistic review found no duplicated skeleton, accidental wrapper or useful further abstraction.

## Buzz pass and frozen handoff

Outcome: FAST-BOARD for the three scoped declarations,1000ms budget. Actual command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-exponential-audit/final-prefix.lean` → exit0.

All normal compiler/native requests were complete before launch; no competing request ran during profiling. Raw complete UTF-8 trace `final-profile.log` retained. The exact production source prefix ends after public32 and closes `end Lemma7` then `end Roth`; no production profiling scaffold is present. `profile-manifest.json` records all disjoint outer-command/async-proof/addDecl/kernel/linter anchor rows. Nested macro theorem commands are not counted again. The parser was independently checked against the inherited raw trace and reproduced all three inherited totals exactly.

|Scoped declaration|Inherited baseline ms|Fresh final ms|Final raw log interval|
|---|---:|---:|---|
|factorial_coefficient_le_two_pow_aux|216.980|290.063|1477302–1494606|
|two_pow_lt_rpow_aux|513.609|597.526|1497752–1536426|
|lem6M_lt|614.335|675.914|1536427–1585424|

All fresh totals are below750ms, so no borderline repeat is required. This is an accepted final-source performance check, not a speedup claim; wall-clock noise and the positivity derivation can change timing. No heartbeat raises were removed or added. The profile is PREFIX-ONLY, not an all-file performance pass. Known earlier numerical/index29 repeats1068.193/1115.157ms and actual whole Θ_lt/original35 stall remain mandatory owner file-final queue items. This leaf does not edit those proofs or claim their performance passed.

The full-name untruncated `rg -n 'two_pow_lt_rpow_aux' .lake/packages/mathlib/Mathlib` returned exit1/no hits, raw `full-name-rg.log`; that is combined with the clean anonymous generic-route experiments, never taken alone as a universal absence proof. `static-verification.json` records width/structure/scoping checks, exact unchanged coefficient source and public statements, and forbidden-token scan.

## Eleven phase checks

- [✓] Step1: mandatory reference documents read.
- [✓] Step2: all24 audit items concrete.
- [✓] Step2.5: five actual searches plus clean anonymous generic routes.
- [✓] Step2.6: every effective binder/drop/weakening, private literature exemption and inversion.
- [✓] Step2.7: all signature-line widths measured; initial/final widths identical.
- [✓] Step2.8: per-occurrence inequality table.
- [✓] Step3: all42 golfing statuses.
- [✓] Step4: step-back reflection, independent candidate and analytic alternatives.
- [✓] Step5a: fresh complete unfiltered live diagnostics,zero errors.
- [✓] Step5b: actual module,exact-first adapter,opaque values/standard axioms,entire caller semantics,final scoped profile.
- [✓] Step6a: no rename needed/no queue write.

Frozen source SHA256 `edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`,949 lines. Source edits revoked before final profiling; no subsequent source edit. Only this report/evidence metadata was completed afterward. All requests/normal compilers/native requests/profiler sessions drained `[]`. Evidence manifest and hashes: `handoff.json`. The leaf audit is complete; original32 publication and owner frozen full build THEN separate Roth.LeanEval/cumulative public checks remain owner work. The private-helper audit adds no original declaration to completion counts.


## Owner final32 batch gates

Both separate fresh helper audits are complete. Final source SHA256
`edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`;949lines.
Final scoped profile: coefficient290.063ms, exponential597.526ms, public32675.914ms.
The newest full actual verifier checks both INITIAL independent helper contracts and current
actual opaque values/standard axioms plus the ENTIRE old/current Θ_lt proof/type/value. Complete
unfiltered final native diagnostics pass0errors8samewarnings. Prior per-leaf frozen-source
profiles above remain historical evidence; the final batch profile is from the second fresh audit.

Owner cumulative all29 original-public adapters, all5 definition values,87opaque body-type checks
and87actual standard-axiom sets pass47.118s; exact source/log record is in the original32 audit.
After every leaf request drained/source edits revoked, owner ran full lake build91.810s THEN
separate lake build Roth.LeanEval31.678s; both exit0, all17 project/source/pin hashes stable.
Raw logs `/private/tmp/roth-theta-d32-full.log`, `roth-theta-d32-leaneval.log`; record
`/private/tmp/roth-theta-d32-builds.json`. These gates supersede pending owner/helper entries
above; exact staging/commit/push publishes the original32 batch. No count from helper audits.
Known earlier numerical/index29 failed repeats and whole Θ_lt profiling stall remain mandatory
file-final obligations. This is not a whole-file performance pass.
