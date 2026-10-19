# `Roth.lem7_Φ_bound` — original declaration 33

Status: scoped original33 audit complete; owner checkpoint gates remain pending. Sole original declaration scope,
minimal `Θ_lt` caller adaptation, no new helpers, no Git operations. The standing user instruction
“From now on implement all changes that you recommend. Only ask me if you can't decide” authorizes
this supported strengthening. Earlier explicit preservation choices remain.

## Baseline and preparation

Published baseline HEAD `432bd8ef42fc69295d68ec9fa562c7b742253876`, source SHA256
`edd28b8b48e01767e9d4434e08c0190f8a8848a873497bd647fa25e8ecdbc35f`, 949 lines.
Baseline snapshot `/private/tmp/roth-phi33-audit/before.lean`. Inherited owner full build 91.810s,
then separate LeanEval 31.678s, exit 0; inherited complete native diagnostics
`/private/tmp/roth-exponential-audit/final-lsp.json`: success, no errors, eight warnings.
These are inherited evidence, not fresh runs by this leaf. Optional cache/linter executable not run;
no dependency/import changes. Five required core references read fully; full cleanup command,
Lean/mathlib-quality skills, and relevant naming/style/profiling sections consulted.

Fresh real baseline exact production prefix through original33, closed with `end Lemma7`,
`end Roth`, command:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-phi33-audit/baseline-prefix.lean`.
Exit 0, all other compiler/native requests drained. Raw UTF-8
`baseline-profile.log` (same audit directory); extracted target `baseline-target.log`.
Disjoint rows: outer command 41.547ms, async proof 1359.017ms, addDecl 10.290ms and 54.333ms,
linter 23.872ms, total **1489.059ms**. Nested kernel 10.275/20.721ms are inside addDecl,
not added again. Nested macro command rows are not double-counted. Broad h1 nlinarith
342ms and final nlinarith 404ms were actual hotspots. This is prefix evidence only.

## Mathematical decision and pre-edit certificate

For `e = (1/2)^(p-1)`, use `δ ≤ δ^e`, `1 ≤ 1+1/p ≤ 3/2`, and
`(δ(1+1/p))^e ≤ (3/2)δ^e`. Multiplying `10 ≤ 10^(p-1)` by positive `δ^e`
provides strict slack for the sum. Thus the result remains strict for `δ = 1`.
Recommend and implement `hδ1 : δ ≤ 1`; the source's original strict range is preserved in
its unchanged quotation. The endpoint extension is established by Lean, not attributed to the paper.

Before public edits, `/private/tmp/roth-phi33-audit/candidate.lean` compiled exit 0 and
clean `candidate.log` includes exact immutable original33 telescope adapter, independent old33
proof, opaque proof values, standard axioms, ENTIRE immutable old and candidate `Θ_lt`
proof/type/value/axioms and candidate dependency. Its complete immutable original Index/Theta
namespace comes from the supplied clean `actual-compatibility.lean`; no old proof block was edited.
`optimized.lean/.log` then compiled the direct product bounds and restricted arithmetic before
that proof was applied. `polished.lean/.log` covers the final dead-local/one-use polishing.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No inherited target-range warning. All final unfiltered warnings are retained below. |
| 2 | HAVE SCAN | See detailed scan below; remove dead exponent positivity/equality and inline single-use numeric bounds. |
| 3 | SET_OPTION | None in production; no heartbeat/recursion/instance limits raised. |
| 4 | SIMP SQUEEZE | Terminal `simpa using` for rpow comparison and coefficient bound; no nonterminal bare simp. |
| 5 | NAMING | `lem7_Φ_bound` describes the source numerical Φ bound; no forbidden multi-number/mN/multipass/numbered-aux/abbreviation/single-letter pattern. Existing name retained; no rename recommended. |
| 6 | LINE PACKING | All signature lines measured below; conclusion occupies two necessarily separate inequality sides. |
| 7 | BY PLACEMENT | All `by` at preceding line end. |
| 8 | FORMAT | Two-space proof indentation, no blank proof lines; replace semicolon chain with terminal simpa; no haveI/letI. |
| 9 | COMMENTS | No inline narrative comments in target; all source attribution text preserved. Caller narratives unchanged. |
| 10 | DOCSTRING | Public mathematical statement/source retained; only assumption endpoint corrected. |
| 11 | VISIBILITY | Existing public result retained; no new helper. |
| 12 | STRUCTURE | Ordinary result, not in module Main results; final body ≤30, all subproofs ≤10, no conjunction/witness splitting. |
| 13 | MATHLIB | Five actual methods and uncontaminated anonymous automation below. Build on real-power API; no equivalent found in those searches. |
| 14 | JUNK DEF | n/a: theorem, no definition introduced/changed. |
| 15 | EXISTS LEMMA | n/a: no existential output/helper. |
| 16 | SHOW/CHANGE | No production show/change. Scratch numeric type ascriptions only. |
| 17 | PUSH_NEG | No push_neg. |
| 18 | GENERALISE | Every effective binder tested, endpoint accepted with original contract adapter and complete caller proofs. |
| 19 | INEQUALITY | All code inequalities smaller-first; measured scan below. |
| 20 | NORMAL FORM | Already standard `<` expression over Real.rpow and Nat powers, not a custom predicate. |
| 21 | SYNTAX GENERALITY | Keep argument names/order/implicitness; non-strict upper hypothesis naturally accepts `.le` at existing caller. |
| 22 | IMPORT FANOUT | n/a: no imports/header changes. |
| 23 | CASTS | No redundant cross-type coercion introduced. Real literal/ exponent annotations fix rpow and numeric bound elaboration. |
| 24 | INSTANCE NAME | n/a: no instances or typeclass binders in effective target type. |

### Have scan

Original `set e ... with he`: remove unused equality; `he0` proof removed because no selected
step needs this fact. `he1` (non-by) feeds both power comparisons: keep. Real-cast `hp` has
proof content: keep. `hc1` feeds exponent comparison and the direct product bound: keep.
`hc2` has a two-line arithmetic proof: keep; its anonymous reciprocal bound has one use and
is proof content certified with `linarith only [this]`. `hδe` has rpow comparison proof: keep.
`hde0` used repeatedly in signs/scaled bounds: keep. `hmul` has the meaningful five-line rpow
subproof: keep. `hT` non-by, one use: inline the explicitly typed `le_self_pow₀` application.
Original `h1` broad arithmetic proof replaced by direct `mul_le_mul`; original `h2` non-by,
one use: inline. Both direct inequalities feed only the restricted final calculation.

## Five actual search methods and public literature/inversion

All native results archived in `/private/tmp/roth-phi33-audit/searches.json`.

| Method | Actual query/result |
|---|---|
| A Lean-Finder | Full p≥2, δ≤1, iterated-root absorption query; five unrelated numerical-bound matches, no target replacement. |
| B Loogle | `Real.rpow, _ ≤ _ → _ ^ _ ≤ _ ^ _`: successful request, zero results. |
| C LeanSearch | Real powers of bases between 0 and 1 increase as exponents decrease; found `Real.antitone_rpow_of_base_le_one`, `Real.rpow_le_rpow_of_exponent_ge_of_imp`, strict variants. |
| D source grep | `source-search.log`: exact existing rpow comparison/antitone statements in Pow/Real.lean; full untruncated `lem7_Φ_bound` grep over Mathlib empty (`full-name-search.log`). |
| E native local name | `rpow_le_rpow_of_exponent`: nine source hits, including used Real variants; index **unavailable**, so no indexed absence claim. |

Auxiliary variants: `_ge`, `_ge'`, `_ge_of_imp`, `_le`, `_le_or_ge`, antitone/strictAnti.
Common-equivalents table has no matching topology/discrete/finite/meromorphic pattern.
Partial matches are existing real-power comparisons used directly. This numerical absorption
requires coefficient/exponent/strict-slack reasoning beyond a 1–3-call wrapper. No needless helper
or mathematical absence claim from grep alone. `/private/tmp/roth-phi33-audit/automation.lean`
is an exact prefix ending BEFORE target, with anonymous `grind`, `aesop`, `simp`, `exact?`, `apply?`
examples. Exit 1 as expected: four unsuccessful proof searches and bounded apply? delaboration timeout
at 10000 scratch heartbeats. No named failed declarations or imported audited target contaminate it.
A timed-out apply? is inconclusive, not proof of absence. Repeated known-stalled native full-Theta
multi_attempt was not retried; ordinary compiler is the bounded fallback required by dispatch.

Public web searches actually run: “Roth theorem proof lemma 7 delta theta 10 p quantitative
elementary proof”; “Roth lemma 7 delta_1 Phi delta 1/p proof generalization”; exact authors/title;
“Roth δ 10 Lemma 7 Diophantine approximation generalization”. Many results concern additive
Roth and are irrelevant. [Milojevic's primary exposition](https://aleksa-milojevic.github.io/expository/roth.pdf)
was opened; it presents a different elementary proof and supplies no replacement for this precise
absorption. [Roth's ICM survey](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf)
search snippet has a small strict δ condition; full opening failed, so no stronger claim drawn.
The repository's authoritative `clean.tex` §5, lines 1002–1021, explicitly uses `0<δ<1`
only to obtain `δ≤δ^e` in this absorption. No external endpoint theorem was found in these
queries. No ChatGPT-math MCP capability is available.

Mandatory inversion: no named polynomial/Θ object occurs in the signature; target is already
an elementary scalar estimate. Replacing the concrete constants/exponent by independent parameters
would require a separate new numerical API with no established second caller. That does not justify
expanding scope or a one-use helper. Real→abstract field would need a real-power API/restatement;
retain Real and Nat because the current real-power and dimension APIs use them; no broader domain API is recommended.

## Every effective binder

Negative syntactic/proof probes are separate: `negative.lean/.log`, exit 1 intentionally.
Positive mathematical refutations `counterexamples.lean/.log`, corrected exit 0. The first
counterexample attempt had a redundant second sqrt rewrite and failed; it is not a positive
certificate. Corrected file removes that rewrite; final successful provenance is distinct.

| Binder | Actual drop/weakening probe | Result |
|---|---|---|
| `{p : ℕ}` | Remove binder under `autoImplicit false` | Unknown p; structural dimension genuinely appears in powers/reciprocal. Nat domain retained. |
| `hp : 2 ≤ p` | Remove hp in selected original proof | Missing hp and unsolved nonzero exponent obligation; independent p=1,δ=1/2 counterexample certifies hp cannot become 1≤p or disappear. |
| `{δ : ℝ}` | Remove binder under `autoImplicit false` | Unknown δ; scalar parameter occurs throughout. Real rpow demands Real domain here. |
| `hδ0 : 0 < δ` | Drop, and replace with 0≤δ | Missing positivity / strict rpow premise; δ=0,p=2 certified strict conclusion false, so keep positive. |
| `hδ1 : δ < 1` | Drop, and replace with δ≤1 | Drop fails; δ=10000,p=2 certified false. Closed δ≤1 candidate independently proved and accepted; strict conclusion unchanged. |

No effective section types/Fintype/DecidableEq binders: exact original adapter/type verifier checks
actual constant telescopes, not visible headers. No bundled outputs to split, no localization or
universe weakening applies to fixed ℕ/ℝ scalar parameters.

## Full 42-rule golf pass

| Rule | Actual disposition |
|---|---|
| 1.1 by exact | n/a: no wrapper. |
| 1.2 by rfl | n/a: no reflexive proof. |
| 1.3 rw+exact | Replace rpow_one/rw+exact with terminal simpa. |
| 1.4 simp+exact | Terminal simpa retained for exponent comparison. |
| 1.5 trailing rfl | n/a: no such tail. |
| 1.6 constructors | n/a: scalar inequality. |
| 1.7 apply+exact | n/a: no adjacent pair. |
| 1.8 by_contra | n/a: no contradiction split. |
| 1.9 eta | n/a: no lambda. |
| 1.10 single-use have | Inline h2/hT and direct replacement h1; remove dead he/he0. |
| 1.11 apply+intro | n/a: no quantified subgoal. |
| 1.12 show | n/a: none. |
| 1.13 conjunction projections | n/a: none. |
| 1.14 rw merge | n/a: only one rewrite in target. |
| 1.15 terminal simp only | n/a: terminal simpa already unsqueezed. |
| 1.16 nonterminal simp | n/a: none. |
| 1.17 dot notation | Use `.trans`, `.le` at monotonicity and caller; preserved standard forms. |
| 1.18 application parentheses | Explicit positive type annotation kept where inferentially useful; no gratuitous parenthesis change. |
| 1.19 push Not | n/a: no negation pushing. |
| 1.20 trivial exists helper | n/a: none. |
| 2.1 entire grind | Actual anonymous exact-prefix trial failed. |
| 2.2 pre-grind deletion | n/a: selected proof has no grind. |
| 2.3 simpa consolidation | Used for terminal coefficient rpow comparison. |
| 2.4 fun_prop | n/a: no function property goal. |
| 2.5 positivity | Existing sign obligations verified; remove unused e positivity proof. |
| 2.6 gcongr | Separate product monotonicity trial in tactics.lean; direct mul_le_mul retained for deterministic explicit application. |
| 2.7 lia | Selected exponent-nonzero obligation succeeds with lia. |
| 2.8 aesop | Actual anonymous whole-proof trial leaves goals. |
| 2.9 norm_num/cast | Concrete 1≤10 proof norm_num; hp conversion exact_mod_cast; certified concrete counterexamples. |
| 2.10 decide | n/a: arbitrary Real/rpow inequality is not finite decidable computation. |
| 2.11 field_simp/ring | n/a: no algebraic equality or denominator identity goal; reciprocal comparison uses existing one_div API. |
| 2.12 linear_combination | n/a: no ring/ring_nf-ending identity with hypotheses. |
| 2.13 wlog | n/a: asymmetric scalar estimate, no symmetric branches. |
| 2.14 calc collapse | Two steps combine exponent monotonicity with rpow_one simplification; retained as meaningful subproof instead of a longer composed term. |
| 2.15 shared goal closing | n/a: no duplicated branches. |
| 3.1 erw | n/a: no erw. |
| 3.2 legacy fun tactics | n/a: none. |
| 3.3 omega→lia | Applied in target nonzero exponent proof; unrelated caller omega preserved under minimal caller scope. |
| 3.4 rcases/rfl | n/a: no cases or substitution. |
| 3.5 attributes | No broad attribute added for one local numeric absorption; no canonical simplification rule. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 maxHeartbeats | No production options; exploratory scratch uses a lower 10000 budget, no raised limits. |

Step-back reflection: direct entire-proof automation did not find the absorption. The selected
proof exposes rpow monotonicity, multiplicative comparison and strict numeric slack, with no
new helper justified by duplication or length. Term mode for the full proof would obscure those
stages. The actual speed claim must come from final uncontended traces, not line counts.

## Packing and inequality artifacts

Actual signature widths (codepoints; explicit complete next expression, no byte-width counting):

| Line | Width | Next signature expression width | Arithmetic | Action |
|---|---:|---:|---|---|
| 672 | 79 | 78 (left side through `<`) | 79+1+78=158>100 | ok |
| 673 | 82 | 52 (right side through `:= by`) | 82+1+52=135>100 | ok |
| 674 | 58 | none | n/a | ok |

The exact built `#check @Roth.lem7_Φ_bound` with `format.width 100` is retained in final
compatibility output. Binary inequality sides are the natural break boundaries.

| Occurrence | Orientation | Action |
|---|---|---|
| hp | `2 ≤ p` | keep |
| hδ0 | `0 < δ` | keep |
| hδ1 | `δ ≤ 1` | accepted endpoint extension |
| conclusion | left expression `<` right expression | keep |
| reversed `≥`/`>` in code | zero | n/a; prose source `p≥2` preserved |

## Refactoring, simplify and performance scope

Phase 3: no file-level edits authorized or needed. Phase 5a: supported upper-endpoint
strengthening, no definition/mathlib replacement/helper extraction. Phase 5b: no rename entries
or queue writes; no forbidden naming pattern. No import/header/global setting or other declaration change.
Simplify pass: manual holistic review equivalent, because this environment has no callable built-in
`/simplify` skill/tool. Removed dead locals and unnecessary numeric have bindings; no duplicated
skeleton requiring a helper. This is not represented as an actual external simplify invocation.
Buzz pass uses the real Lean4.34 profile command; final frozen target numbers recorded below.

Mandatory inherited file-final repair queue remains: earlier numeric/index29 failure measurements
1068.193/1115.157ms, and stalled whole-`Θ_lt` traces. These are outside scoped33; no whole-file
performance PASS is claimed. Owner must repair/re-sweep at file completion. No new unbounded
wholecaller trace was started merely to rediscover the known stall before original35.

Original32 cumulative evidence remains `/private/tmp/ThetaApprovedOriginalFinalProbe-d32-values-corrected.lean`,
SHA256 `1a673f9914a15a60ce5d80d5e864b7c12e1e3b87e790bb919d1f2bd4e1301b70`, and
`/private/tmp/roth-theta-d32-values-corrected-cumulative29.json`: all29 original public adapters,
87 opaque value/type checks and 87 actual standard-axiom checks. Current helper FIRST/audit
scaffolds supplied by owner remain `/private/tmp/roth-exponential-audit/independent-first-values.lean/.log`
and `actual-compatibility.lean/.log`. This leaf does not misrepresent them as fresh33 evidence.

## Final semantic and diagnostic gates

Final production source is 947 lines (949→947, −2); target body 22→20 lines. No helper
introduced, no independent branch above ten lines. Sole routine caller edit is `hδ1.le`.
The first module build was superseded by dead-local polishing. Final actual invocation
`/Users/ramin/.elan/bin/lake build Roth.Theta` exited 0 (`final-module-build.log`, 2423 jobs).
No owner full build or LeanEval was run by this leaf.

Complete **unfiltered** final native `lean_diagnostic_messages` on the live file returned
`success=true, partial=false, timed_out=false`, no failed dependencies and zero errors.
Raw response: `/private/tmp/roth-phi33-audit/final-lsp.json`. All eight warnings, without filtering:

| Line | Warning | Disposition |
|---|---|---|
| 1 | Copyright too short | User-protected header metadata. |
| 93 | hr not explicitly referenced | Retained earlier scoped-audit choice; no explicit user veto. |
| 101 | hB not explicitly referenced | Protected prior public hypothesis. |
| 101 | hr not explicitly referenced | Protected prior public hypothesis. |
| 109 | hB not explicitly referenced | Protected prior public hypothesis. |
| 129 | hr not explicitly referenced | Protected prior public hypothesis. |
| 252 | hr not explicitly referenced | Retained earlier scoped-audit choice; no explicit user veto. |
| 547 | hq not explicitly referenced | Explicit earlier hq preservation preference. |

No new target/caller diagnostic or linter warning. No warnings suppressed by new options.
The separate positive product `gcongr` scratch compiled exit 0; it has one unused scratch hpos
warning and is not production or standard-axiom evidence.

Immutable original proof blocks in final certificate are byte-identical to supplied evidence:
Index SHA256 `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`,
Theta SHA256 `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`.
Exact actual direct old-contract adapter and all current/old entire-caller semantic checks are
in `/private/tmp/roth-phi33-audit/final-compatibility.lean/.log`; these use `value! true`,
`inferType`, exact `isDefEq` and `Lean.collectAxioms`, whitelist precisely propext,
Classical.choice, Quot.sound. They check actual compiled full Θ_lt proof dependency on
Roth.lem7_Φ_bound, not header equality or a current theorem invoked as independent proof.
The independent selected proof and entire candidate caller remain separately available.

New identifier verification: `mul_le_mul`, `mul_le_mul_of_nonneg_right`, `zero_le_one.trans`,
`le_self_pow₀`, `lia` all elaborated in positive polished candidates and actual module build.
Real.rpow comparison names verified by native local search and source; no invented names.

## Diff gates and eleven steps

| Gate | Status/evidence |
|---|---|
| lake_build_file | PASS actual final `lake build Roth.Theta`, exit 0. |
| definition_protected | PASS no def/abbrev/header/import/global setting change. |
| theorem_statement_protected | PASS under item18 and standing user authority: δ<1→δ≤1 only; exact old-contract adapter and independent complete caller proofs. |
| structure_gate | PASS body20≤30; largest meaningful subproof≤10; no split output. |
| naming_gate | PASS no forbidden pattern; public API/name retained. |
| line_packing_gate | PASS all three measured signature lines, table above. |
| inequality_orientation_gate | PASS zero ≥/> in code, scan above. |
| cumulative caller | PASS module and independent entire Θ_lt proof/type/value/standard-axiom checks; owner broader cumulative gate still due. |
| comments/source preservation | PASS source quote unchanged; only assumption range updated, zero inline comments removed. |
| no proof/trust escapes | PASS production has no sorry/new axiom/native_decide/limit raise/profiling scaffolding. |
| full project/LeanEval | OWNER PENDING after this leaf freezes; never claimed complete here. |

Eleven-step checklist: [✓]1 references; [✓]2 complete24-item audit; [✓]2.5 five actual
searches; [✓]2.6 everybinder/generalisation/literature/inversion; [✓]2.7 packing table;
[✓]2.8 inequality table; [✓]3 all42 rules; [✓]4 reflection; [✓]5a complete unfiltered
live diagnostics; [✓]5b scoped diff/build/semantic gates; [✓]6a no rename needed/queue untouched.
Owner fullbuild/separateLeanEval/cumulativeallpublic/report/stage/commit/push remain sequential
checkpoint duties before original34. Successful owner checkpoint counts become214/264,
Theta33/35,ninefiles; helper/revisit counts0. These counts are prospective until owner publishes.

Additional public formulation searches (archived `literature-extra.json`): exact Roth/delta_1/Theta,
nLab Diophantine Roth, and Stacks Diophantine Roth. Results are unrelated additive Roth,
Vojta's general dictionary, nLab number theory/Pythagorean material and a Rotthaus bibliography
entry. None supplies an alternative formulation of this scalar estimate; no mathematical claim
is inferred from these unrelated matches or index silence. Initial failed counterexample output
is separately preserved in `counterexamples-initial-failure.txt` (explicit transcription of actual
tool output), separate from the corrected clean positive log.

## Final uncontended performance evidence

First final actual exact-prefix command (same real flags as baseline) exited 0 on final source
SHA256 `fc354913a6695d434020810dd37299614daa2bd7ca345b0e8bac489492679337`.
Raw `/private/tmp/roth-phi33-audit/final-profile.log`; extracted `final-profile-target.log`,
disjoint parsed rows `final-profile.json`:

| Disjoint outer row | ms |
|---|---:|
| Elab.command target | 51.508 |
| Elab.async target proof | 779.243 |
| addDecl auxiliary proof | 7.082 |
| addDecl target | 20.433 |
| asynchronous target linter | 17.755 |
| **Total** | **876.021** |

Nested Kernel auxiliary7.068ms and target17.247ms are recorded but not added again.
This repairs original33 below1000ms, from1489.059ms baseline, without helpers or limit raises.
Because the first final total is≥750ms, a same-source uncontended repeat is required and was
launched before completion. Its final result and freeze record follow. No wholefile performance
PASS can be inferred from either prefix measurement.


Required same-source repeat exited0 with no other compiler/native requests active. Raw
`/private/tmp/roth-phi33-audit/final-profile-repeat.log`, extracted
`final-profile-repeat-target.log`, parsed `final-profile-repeat.json`:

| Disjoint outer row | ms |
|---|---:|
| Elab.command target | 36.859 |
| Elab.async target proof | 678.567 |
| addDecl auxiliary proof | 5.155 |
| addDecl target | 19.339 |
| asynchronous target linter | 17.331 |
| **Total** | **757.251** |

Nested Kernel auxiliary5.144ms and target15.723ms are not added again. Both final
measurements876.021/757.251ms pass below1000ms; the≥750ms repeat rule is satisfied.
All raw runs, including baseline1489.059ms, are preserved; no cherry-picked third sweep.
Outcome: **FIXED, scoped original33**; inherited file-final repair queue remains open as above.
No production profiling scaffolding or limits added. Separate `/buzz` tool is unavailable;
this report records the actual executed profiling workflow rather than claiming an invocation.

## Freeze and handoff

Final source SHA256 `fc354913a6695d434020810dd37299614daa2bd7ca345b0e8bac489492679337`.
All source-edit authority for this leaf is revoked after this freeze. Pending compiler/native
requests: `[]`; every session drained, both profile processes exit0. Report-only handoff.
Only source changes: original33 δ≤1/doc assumption/direct arithmetic/local polishing and
sole actual caller `Θ_lt` `.le`; repository-wide `rg` found no other call site. Source947lines,
body20lines; newhelpers0. Report path `.mathlib-quality/cleanup/Theta-lem7_Phi_bound.md`.

Owner next steps: frozen sequential full `lake build`, THEN separate `lake build Roth.LeanEval`,
all-public cumulative actual type/opaque-value/standard-axiom adapters (incorporating this approved
original33 weakening), shared report update, exact-path source/report/progress staging, commit and push, then original34.
No owner gates, Git operations, main/forcepush/pin changes were performed by this leaf.


## Owner current cumulative public-contract gate

On the exact frozen sourcefc354913, owner compiled the regenerated33-aware all-public verifier
exit0 in51.807s:29exact original-public adapters, all5 definition-value equalities,87explicit
opaque body-type checks and87actual standard-axiom sets,29final PASS markers. Exact archived
compiled input `/private/tmp/ThetaApprovedOriginalFinalProbe-d33-values.lean`, SHA256
`6d7fc49401e480f2e681a733ccabf9c5dae1d1f3f764410205738fcc57ffed10`; log/record
`/private/tmp/roth-theta-d33-values-cumulative29.{log,json}`. Both entire immutable original
Index/Theta proof blocks remain byte-identical72cf/355a, independently compared in
`/private/tmp/roth-theta-d33-owner-cumulative-checked.json`. No production change during this gate.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (105.519 s),
then separate `lake build Roth.LeanEval` (38.323 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `fc354913a6695d434020810dd37299614daa2bd7ca345b0e8bac489492679337`.
Raw logs: `/private/tmp/roth-theta-d33-full.log`, `/private/tmp/roth-theta-d33-leaneval.log`; machine record
`/private/tmp/roth-theta-d33-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 33/35, overall 214/264 original
declarations, 9/14 completed files. No new helper; existing separately audited private helpers are unchanged.
