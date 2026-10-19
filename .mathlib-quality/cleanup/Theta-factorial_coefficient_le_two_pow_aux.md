# Fresh private-helper audit: `factorial_coefficient_le_two_pow_aux`

Scope: only this newly introduced private helper and its single necessary proof application in `lem6M_lt`. No Git, shared-log, header, import, public-statement, or other-helper edits. This is a fresh helper audit within the pending original32 batch; it does not increase the original declaration count. Evidence directory: `/private/tmp/roth-coefficient-audit/`.

## Baseline and mathematics

Inherited exact-source baseline SHA256 `52868a517597da434ede705309f6563030ce587eaafbffb28d991e782c9f7a9d`, 949 lines. Baseline complete unfiltered native LSP `/private/tmp/roth-d32-log/final-lsp.json`: success, partial=false, timed_out=false, zero errors/eight warnings. Baseline real prefix profile `/private/tmp/roth-d32-log/final-profile.log`: coefficient helper263.134ms, exponential helper590.813ms, public32 627.089ms. These are explicitly inherited, not fresh measurements. Baseline module and compatibility exits0 are inherited from the immediately preceding frozen handoff. Owner full-project/LeanEval gates remain owner work.

Read lean4 and mathlib-quality skills, full cleanup workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, profiling, and relevant style/naming sections. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Classic dialect.

The estimate replaces `(r₁+1)^(p*l)` by `(2^r₁)^(p*l)` and `l!` by `l^l ≤ (2^r₁)^l`, then combines the three powers of2 by a polynomial exponent identity. This is a substantive coefficient estimate with factorial monotonicity and exponent arithmetic, not a convenience wrapper around1–3 calls or an existential witness wrapper.

Recommended and applied private generalisation: `hl : l ≤ r₁` becomes `hl : l ≤ 2 ^ r₁`. The proof uses precisely the latter bound. This admits, for example, r₁=1,l=2. The public32 signature still requires `l ≤ r₁`, preserving its separate positive-product argument. Its one helper application supplies `hl'.trans Nat.lt_two_pow_self.le`. Owner confirmed this supported private change under the user's standing authority. The one-use, non-by `hfactorial` is inlined at its precise gcongr subgoal. Helper proof body10→9 lines; module949→948 lines. No new helper is introduced.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
|1|Lint|No warning in helper range; complete final native diagnostic list recorded below. Eight pre-existing warnings outside scope remain; their distinct preservation scopes are listed below.|
|2|Have scan|Exactly one original `hfactorial`, no by, one implicit use by gcongr: inline the composed factorial bound into the corresponding subgoal. Final helper has no have.|
|3|Set option|None in helper; no production limit raise, trace, linter mask or profiling scaffolding. Lower10000 budgets occur only in negative scratch.|
|4|Simp squeeze|No simp in original/final helper; bare simp whole-proof trial made no progress.|
|5|Naming|Snake-case mathematical coefficient/power comparison with permitted unnumbered `_aux`; no forbidden abbreviation, numbered pattern, single-letter public name, `_ge_` or `_gt_`. No rename required.|
|6|Line packing|Confirmed historical concrete100-column packing opportunity. Supported binder generalisation changes its arithmetic; independently measured final two-row table below.|
|7|By placement|`:= by` at end of conclusion line and both calc justifications; no standalone by.|
|8|Format|2-space proof indentation, ordinary calc formatting, two focused monotonicity goals, no empty proof lines, trailing whitespace, semicolon, haveI/letI or lambda.|
|9|Comments|No original helper comments. Public32's signpost is preserved verbatim. No comments/docstrings removed.|
|10|Docstring|Private auxiliary has none; no public docstring changed.|
|11|Visibility|Retain private, single-file technical estimate.|
|12|Structure|9 proof lines, no conjunction, no branch/subproof over10 lines; gcongr block3 lines and exponent-normalisation block2. No extraction needed.|
|13|Mathlib|Five actual methods plus clean anonymous compiled exact?/apply? probes below. Partial matches supply existing factorial/power building blocks; no direct whole-result replacement located. No absolute absence claim from unavailable local index.|
|14|Junk def|n/a: lemma, no definition changed.|
|15|Exists lemma|n/a: no existential conclusion or witness.|
|16|Show/change|Neither appears.|
|17|Push negation|No push_neg or negation tactics.|
|18|Generalise|Every effective binder has a compiled probe below. Weakened hl applied; no hidden σ/τ typeclass parameters in actual built type.|
|19|Inequality|All signature and body inequalities are ≤; table below. No reversed operator/name.|
|20|Normal form|Natural factorial and powers are canonical for this coefficient estimate; exponent equality is polynomial normalization. No custom predicate or new equivalence API.|
|21|Syntax generality|The weaker direct bound is easier to supply from power estimates while the old caller has an explicit one-term adapter. No extra quantified witness or conclusion restatement.|
|22|Import fanout|n/a: no production import change.|
|23|Casts|Zero explicit coercions/type ascriptions in helper diff. Public caller retains its one genuine Nat→Real exact_mod_cast bridge.|
|24|Instance name|n/a: no instance declaration or effective instance binder.|

## Measured signature packing

Widths are Unicode codepoints, including indentation and `:= by`. `#check @FreshCoefficient.finalCandidate` at format.width100 is in `final-candidate.log`; actual built type is in `actual-compatibility.log`.

Historical baseline table (before supported generalisation):

| Sig line | Chars | Next logical expression group | Arithmetic | Action |
|---|---:|---|---|---|
|603|79|`(r₁ + 1) ^ (p * l) *`,20|79+1+20=100|Concrete repack finding confirmed|
|604|90|none|n/a|ok|

Final table after changing the mathematical hypothesis:

| Sig line | Chars | Next logical expression group | Arithmetic | Action |
|---|---:|---|---|---|
|603|83|`(r₁ + 1) ^ (p * l) *`,20|83+1+20=104|ok; full first factor overflows|
|604|90|none; proof follows|n/a|ok|

The final break is at the whole power-factor boundary, not an artificial80-column target. No signature line is over100. The public signature and other helper signature are unchanged.

## Inequality scan

| # | Location | Occurrence | Rewrite / rename |
|---|---|---|---|
|1|Initial hl|`l ≤ r₁`|Weakened to `l ≤ 2 ^ r₁`; orientation unchanged|
|2|Final hl|`l ≤ 2 ^ r₁`|none; correct ≤|
|3|Conclusion|coefficient `≤ 2 ^ ...`|none; correct ≤|
|4|Body calc|coefficient `≤` product of powers|none; correct ≤|
|5|Entire signature/body|zero ≥/>|no rewrite or rename|

## Five actual Mathlib searches

Raw native results: `native-searches.json`; unfiltered source search: `mathlib-rg.log` (52 rows). Standard file `Mathlib/Data/Nat/Factorial/Basic.lean` inspected.

| Method | Actual query | Result |
|---|---|---|
|A Lean-Finder|natural factorial coefficient `(r+1)^(p*l)*l!*2^(p*l*r)` at most `2^((2*p+1)*r*l)`|Five hits; Nat.factorial_le_pow is partial match. factorial_two_mul_le and factorial_mul_pow_le_factorial do not state the coefficient estimate.|
|B Loogle|`Nat.factorial _ ≤ _ ^ _`|Nat.factorial_le_pow.|
|C LeanSearch|factorial bounded by power and natural number less than two to its power|Ten hits including factorial_le_pow, descending/ascending factorial variants; no full coefficient estimate returned.|
|D Source rg|full helper name, factorial_le_pow, lt_two_pow_self, factorial/power and factorial_le/lt/mul_pow variants over entire Mathlib tree|Full helper name has no source hit; natural factorial and exponential building blocks found. Untruncated results saved.|
|E Local name search|`factorial_le`|Nat.factorial_le and Nat.factorial_le_pow returned; index=unavailable, so empty-result completeness is not claimed.|

Auxiliary variants searched include factorial_mul_pow_le_factorial, factorial_mul_pow_sub_le_factorial, descFactorial_le_pow, ascFactorial_le_pow_add, and two_pow factorial comparisons. Common-equivalents table has no matching topology/finiteness/bornology bucket. The available partial match is used directly as `Nat.factorial_le_pow`; no direct replacement was located. Keep the substantive local coefficient estimate.

`negative-automation.lean/.log` uses the exact production prefix ending BEFORE the target, anonymous examples, and lower10000 heartbeat budgets. Neither the current helper nor failed named target declarations are in its imported context. `exact?` failed; `apply?` generated generic partial arithmetic suggestions and reached the deliberately lower budget; no full proof or direct replacement emerged. This is bounded negative search evidence, not proof of global mathematical absence. Native multi_attempt is not retried after the documented repeated stalled requests in prior leaves; ordinary isolated compilation is the instructed fallback.

## Every-effective-binder probes and inversion

`negative-binders.lean/.log` exits1 as expected; it has autoImplicit=false and separate named negative trials, never used for proof search or axiom certificates. `positive.lean/.log` exits0 and independently proves both the initial contract and wider candidate. `no-have.lean/.log` exits0 verifies inlining before production. `final-candidate.lean/.log` exits0 proves the exact final helper independently, checks standard axioms, and verifies the exponent polynomial with linear_combination. Final actual compatibility also certifies opaque proof values.

| Binder | Kind / use | Actual compiled probe | Result |
|---|---|---|---|
|p:ℕ|Value; natural exponent count|Drop p with autoImplicit=false|Unknown p; needed in expression. No abstract-type weakening: exponent is naturally Nat.|
|r₁:ℕ|Value; degree bound and exponents|Drop r₁ with autoImplicit=false|Unknown r₁; needed in expression. Nat power/exponent roles intrinsic.|
|l:ℕ|Value; factorial index and exponents|Drop l with autoImplicit=false|Unknown l/l.factorial. Nat factorial API intrinsically natural.|
|hl:l≤r₁|Proposition; original factorial bound|Drop hl; weaken to l≤r₁+1 in the old selected proof; replace by l≤2^r₁ in full independent positive proof|Drop fails unknown hl; +1 old proof fails power bound (a proof-dependence failure, not a false-theorem claim). Power-bound weakening compiles and is applied.|
|Final hl:l≤2^r₁|Proposition; direct factorial monotonicity|Same final no-have proof compiles; successful actual proof certifies a counterexample to dropping the bound at p=0,r₁=0,l=2|Without hl,2!≤1 is false, independently certified by decide. No further drop recommended.|

No type variables, universes or implicit section instances appear in the actual helper type. There are no strict hypotheses to weaken, global hypotheses to point-localise, bundled maps to unbundle, or typeclass-parent candidates. The final premise is already a direct natural power bound.

Literature status: n/a: private declaration, external literature search not required by the workflow. Inversion check performed: factorial appears substantively in the estimate via Nat.factorial_le_pow, rather than disappearing after unfolding an unrelated named object. Base2 is the specific coefficient normalization consumed by the next exponential helper; replacing factorial by a variable with an assumed identical bound would create an arbitrary wrapper, not a useful independent abstraction. The supported broader range of l is already applied.

## All 42 golfing rules

| Rule | Status |
|---|---|
|1.1 by exact wrapper|n/a: final proof has substantive calc.|
|1.2 by rfl|n/a: none.|
|1.3 rw+exact→rwa|n/a: exponent rewrite followed by normalization.|
|1.4 simp+exact|n/a: no simp.|
|1.5 trailing rfl|n/a: none.|
|1.6 constructors|n/a: no conjunction.|
|1.7 apply+exact|n/a: no apply.|
|1.8 by_contra!|n/a: no contradiction.|
|1.9 eta reduction|n/a: no lambda.|
|1.10 inline one-use have|Applied hfactorial at its exact monotonicity subgoal.|
|1.11 refine+fun|n/a: no intro/apply chain.|
|1.12 redundant show|n/a: none.|
|1.13 obtain projections|n/a: no products/existentials.|
|1.14 merge rw|Already one four-rewrite call.|
|1.15 terminal simp unsqueeze|n/a: none.|
|1.16 nonterminal squeeze|n/a: none.|
|1.17 dot notation|Existing `.trans` retained in the inlined bound.|
|1.18 avoid parens|Parentheses preserve the factorial bound's `.trans` receiver; no removable function-lambda wrapping.|
|1.19 push Not|n/a: no push_neg.|
|1.20 existential inline|n/a: no existential.|
|2.1 whole grind|Actually tried clean anonymous target; fails.|
|2.2 delete before grind|n/a: no production grind.|
|2.3 simpa consolidation|No simp/exact chain; whole simp trial made no progress.|
|2.4 fun_prop|n/a: purely natural inequality.|
|2.5 positivity|Whole target trial reports not a positivity goal; no side positivity goals.|
|2.6 gcongr|Retained and used to expose exactly the two factor bounds.|
|2.7 lia/omega|Both actually tried on full estimate; fail on nonlinear power/factorial content.|
|2.8 aesop|Actually tried; no progress.|
|2.9 norm_num/norm_cast|Whole norm_num trial leaves symbolic estimate; no helper casts.|
|2.10 decide|n/a for universally symbolic target; kernel decide used only for closed witnesses/counterexample in positive certificate.|
|2.11 field_simp;ring|n/a: no division.|
|2.12 linear_combination|Actual positive exponent identity succeeds; integrating it requires an extra congr step, so retain one ring_nf.|
|2.13 wlog|n/a: no symmetric cases.|
|2.14 collapse calc|Estimate then nontrivial exponent equality; term chain would duplicate large products and not remove reasoning.|
|2.15 <;>|Two distinct gcongr goals need different exact bounds; no common closing tactic.|
|3.1 erw→rw|Already rw.|
|3.2 fun_prop migration|n/a: no continuity/measurability.|
|3.3 omega→lia|Neither retained; full lia and omega both failed as2.7.|
|3.4 rfl substitution|n/a: no rcases.|
|3.5 attributes|Private one-use coefficient estimate; global automation registration adds no supported value.|
|3.6 simp_all|n/a: no simp_all.|
|3.7 limit removal|No production limit option present or added.|

Step-back reflection: one-tactic and generic Mathlib routes were actually tested. The remaining mathematical steps are the factorial bound, first-factor exponential bound, and exponent arithmetic. Inlining removes the hidden gcongr premise while retaining the short calc. A term expression would obscure the two monotone factors; no further abstraction or new helper is warranted.

## Compatibility, diagnostics, and gates

`lake build Roth.Theta` → exit0, raw `module-build.log`,2423 jobs. `actual-compatibility.lean/.log` → exit0. This file preserves BOTH independent original proof blocks byte-for-byte: Index SHA256 `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`, Theta SHA256 `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`. Owner independently compared both complete blocks with the archived successful verifier; `/private/tmp/roth-coefficient-audit/owner-both-immutable-blocks.json`. The exact immutable first helper block comes from `/private/tmp/roth-d32-log/helpers-first-context.lean`, entire context SHA256 `807e99748225d46c5acaeaa802f15ae3743c5357f2c10e81a339613c0e03f6cb`; its independent proof remains present unchanged as D32First. The actual updated built private constant is located programmatically; an explicit exact-initial-contract adapter applies that actual constant, not a self-proof or only a guessed current type. Its type is checked against the exact first type. The separately proved finalCandidate type is checked against the actual built final type.

The same successful verification checks exact original32 telescope adaptation, full original/current Θ_lt types and opaque proof values, actual public32 and both actual helper proof values, and only standard propext/Classical.choice/Quot.sound axioms. Opaque values use `value! true`; clean output has no PANIC, error or sorryAx. Entire caller is semantic evidence; no bounded-prefix-only claim substitutes for its type/value check. Other exponential helper source is byte-identical to baseline, and its original type remains checked.

Fresh COMPLETE unfiltered live `lean_diagnostic_messages` → success=true,partial=false,timed_out=false,failed_dependencies=[],zero errors/eight warnings; raw `final-lsp.json`. Native goal after ring_nf has goals_after=[] (`final-goal.json`). All warnings shown, without filtering:

| Line:column | Warning |
|---|---|
|1:2|Copyright too short; header preserved under explicit scope.|
|93:43|hr not explicitly referenced; retained earlier scoped audit choice, not an explicit user veto.|
|101:27|hB not explicitly referenced; protected existing public hypothesis.|
|101:64|hr not explicitly referenced; protected existing public hypothesis.|
|109:28|hB not explicitly referenced; protected existing public hypothesis.|
|129:81|hr not explicitly referenced; protected existing public hypothesis.|
|252:6|hr not explicitly referenced; existing out-of-scope declaration.|
|547:47|hq not explicitly referenced; explicitly retained earlier public hypothesis.|

| Gate | Result | Evidence |
|---|---|---|
|lake_build_file|pass|Actual `/Users/ramin/.elan/bin/lake build Roth.Theta`,exit0.|
|definition_protected|pass|No def/abbrev edits.|
|theorem_statement_protected|pass under authorised private generalisation|Only helper hl weakens; exact immutable-first adapter and actual built final type checked. Public32 and entire Θ_lt signatures unchanged.|
|structure_gate|pass|9-line body; all branches/subproofs≤10; no conjunction.|
|naming_gate|pass|Descriptive snake-case + permitted unnumbered aux.|
|line_packing_gate|pass|Two measured final rows83/90; next whole power factor would give104.|
|inequality_orientation_gate|pass|No reversed inequalities/names.|
|cumulative_no_unintended_breakage|pass for owned scope|Module build, actual private adapter, unchanged other helper, full public32/entire Θ_lt semantic check.|
|owner full build / LeanEval|pending owner|Not run by this leaf.|

Phase3 file-level fixes: n/a, single-private-helper scope. Phase5a: supported private weakening and single minimal public proof-call adaptation applied; no wrapper replacement found. Phase5b: no rename needed, no queue/shared-log write. No new Mathlib identifier is introduced; the relocated factorial/power identifiers were already present, searched and compiled. Exact final source diff is `source.diff`.

Simplify pass: manual equivalent, PASS-THROUGH after the inline-bound fix. No callable built-in simplify skill exists in this host, so no tool invocation is claimed. Holistic review found no duplicated skeleton, thin wrapper or extra abstraction to introduce. No further edit followed verification.

## Buzz pass and freeze

Outcome: FAST-BOARD for the three scoped declarations, budget1000ms. Actual command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-coefficient-audit/final-prefix.lean` → exit0. All normal compiler/native requests were drained before launch; no competing request ran during profiling. Raw UTF-8 log `final-profile.log`; exact disjoint anchor rows, log intervals and excluded nested macro rows are in `final-profile-summary.json` and `profile-manifest.json`.

| Scoped declaration | Inherited baseline ms | Fresh final ms | Final log anchor interval |
|---|---:|---:|---|
|factorial_coefficient_le_two_pow_aux|263.134|216.980|1475600–1492261|
|two_pow_lt_rpow_aux|590.813|513.609|1495431–1535805|
|lem6M_lt|627.089|614.335|1535806–1584722|

All are below750ms, so no borderline repeat is required. Counted outer lemma/theorem command plus associated proof/kernel/linter async rows; nested macro theorem commands are excluded, preventing double counting. No performance repair or causal speedup claim is made from routine wall-clock variation. No raises removed or added; production scaffolding clean. A premature parse while the log was still being written encountered an incomplete trailing UTF-8 codepoint; it supplied no accepted timing. The final summary was regenerated only after process exit0 from the complete valid UTF-8 log.

This is an exact-source prefix measurement through public32, with `end Lemma7` then `end Roth`, not a successful whole-file performance sweep. The known earlier numeric/index29 repeat1068.193/1115.157ms and whole Θ_lt/original35 performance stall remain mandatory file-final owner queue items; no earlier proof is edited here and no whole-file FAST claim is made. The other new helper still requires its separate fresh dedicated audit before owner frozen full build then separate LeanEval and original32 publication.

## Eleven phase checks

- [✓] Step1: mandatory references read.
- [✓] Step2: all24 audit items concrete.
- [✓] Step2.5: all five actual search methods and clean anonymous generic routes.
- [✓] Step2.6: every effective binder probed; private literature exemption and inversion recorded.
- [✓] Step2.7: measured before/final signature tables.
- [✓] Step2.8: inequality occurrence table.
- [✓] Step3: all42 golfing statuses.
- [✓] Step4: independent step-back reflection and proof alternatives.
- [✓] Step5a: complete unfiltered fresh native diagnostics, zero errors.
- [✓] Step5b: actual module/contract/opaque-value/axiom gates and scoped performance evidence.
- [✓] Step6a: no rename needed; no queue write.

Frozen source SHA256 `88184680e2461359c26db220177f45648e6c1827467f401a9a2c74340785b4c4`,948 lines. Source edits revoked; report-only handoff. Requests/normal compilers/native requests/profilers all drained `[]`. Final successful supplemental `independent-first-values.lean/.log` directly re-proves BOTH exact INITIAL helper blocks from the immutable first context and checks both opaque values/types/standard axioms; exit0. It ran after the uncontended profile, with no source change. No PANIC/error/sorryAx. File-final owner work is explicitly pending above. Final handoff and evidence hashes: `handoff.json`.


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
