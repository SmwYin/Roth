# Dedicated audit — `Roth.Θ_option_le` (original 30)

Scope: original 30, its necessary routine `Θ_lt` call, and this report only. No Git mutations, shared logs/queues, import/header/definition changes, or helper changes. Explicit user preference retains `hq`; `hB` remains a real input to `Θ_le_of_forall_index_le`. Standing authority permits the supported recommended boundary changes after concrete compilation and full original compatibility evidence. The owner still runs the full build, then the separate LeanEval build and publication gates.

## Baseline and mathematics

Initial live source SHA256 `59fc1479999b47953aff7aee6bf8be17a325e9523ca94375d8b48b273618e427`, published checkpoint `81aa9b2d1db6ee3f43c100f5b1cbe934742db542`. Same-SHA inherited complete native baseline diagnostics `/private/tmp/roth-public29-K/final-lsp.json`: 0 errors/11 warnings. This is explicitly inherited doctor evidence. No inherited original-29 trace is presented as target-30 evidence.

Fresh, drained, **real exact entire prefix through 30**, closed by `end Lemma6` and `end Roth`, ran before any live edit. Command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-public30-option/baseline-prefix.lean`, exit 0, 178.280s. Baseline total disjoint outer-command plus associated async rows: target 30 **217.512ms**, public29 1117.975ms, weight491.763ms, mapped885.559ms, numeric1078.657ms. These diagnostic baseline overages are recorded honestly; they are not accepted final timings. Raw log, declaration anchors, and manifest: `/private/tmp/roth-public30-option/baseline-profile.log`, `baseline-timings.json`, `baseline-profile-manifest.json`. No options/limits raised or trace nodes masked.

The mathematics is the supremum step of Lemma 6: for every allowed polynomial and rational point, `index_le_lem6` supplies one shared natural `l` and its two bounds. Its index estimate is dominated by the finite maximum at that same `l`. Multiplication by 2 preserves the inequality, and taking the supremum over allowed indices proves the conclusion. The already-published index theorem works on the closed δ interval, with `3 ≤ r none` and weak coordinate ratio. Passing precisely those premises through removes the now-unused external positivity assumption on `r`. No new helper is necessary.

References read: Lean and mathlib-quality SKILL.md; complete cleanup workflow; full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates; relevant style, naming and profiling sections. Skill profiler command examples are superseded by the dispatched correct Lean4.34 `--profile`/`trace.profiler` command above.

## Full 24-item audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | Initial target has unused hr0 and automatically included DecEq. Both selected omissions are tested; no warning suppression/artificial use. hq stays even when a stronger independent experiment omits it. |
| 2 | HAVE | No `have` in target. `obtain ⟨l,hl,hl',hle⟩` preserves the correlated witness/bounds. The caller's hr'0 remains used later for Φ nonnegativity. |
| 3 | SET_OPTION | None in production target; no added limits, masks or profiling scaffolding. |
| 4 | SIMP | No simp in target, so squeezing/unsqueezing is inapplicable. |
| 5 | NAMING | Θ_option_le describes the Option-indexed upper bound, uses no forbidden abbreviation/numeric scheme/_aux-number. Public source terminology and name retained. No rename. |
| 6 | LINE PACKING | All six signature lines measured below; existing output formula retained, hypothesis groups packed. |
| 7 | BY | `:= by` ends final signature line. |
| 8 | FORMAT | Two-space tactic indentation; four-space signature continuation; no blank proof lines or haveI/letI. Lambda arrows corrected in target. |
| 9 | COMMENTS | No inline comments in target; original docstring and all caller signposts preserved. No narrative removed. |
| 10 | DOCSTRING | Original public Lemma6 description and precise source reference retained byte-for-byte. |
| 11 | VISIBILITY | Main-results public wrapper retained per user preference. No private wrapper/helper introduced. |
| 12 | STRUCTURE | Eight proof lines become five, below headline cap15; no branches or conjunction conclusion. Shared l not split. |
| 13 | MATHLIB | Five actual methods and uncontaminated prefix-before-target automation below. `Finset.le_sup'` supplies the finite-maximum step directly; no duplicate custom order helper. |
| 14 | JUNK DEF | n/a: theorem, no def/abbrev added or edited. |
| 15 | EXISTS | n/a: public supremum bound, not a trivial private witness lemma. Its internal existential witness remains correlated. |
| 16 | SHOW | No show/change in target. |
| 17 | PUSH_NEG | None in target; no deprecated tactic introduced. |
| 18 | GENERALISE | All effective parameters and compiled candidates accounted for below; hq explicitly retained. Exactly DecEq/hr0 omitted, δ boundaries closed, rp premise weakened to≥3, coordinate ratio weakened to≤. |
| 19 | INEQUALITY | Zero reversed ≥/> tokens in signature; every occurrence audited below. |
| 20 | NORMAL FORM | RSet/index/Θ/lem6Φ and the finite nonempty Icc supremum remain the canonical existing project forms. No conclusion restatement. |
| 21 | SYNTAX GENERALITY | Existing argument names/order/BinderInfo retained apart from exact selected omissions. Ordinary callers specialize strict hypotheses with .le. No bundled premise helps this caller. |
| 22 | IMPORT FANOUT | n/a: no new production import. |
| 23 | CASTS | `r none : ℝ` is a genuine Nat→Real bridge in new rp premise and existing ratio. No redundant explicit cast introduced. No algebraic domain generalization of Θ/rational indices proposed. |
| 24 | INSTANCE NAME | No instance declaration. Synthetic anonymous instance renumbering permitted; actual retained class/type/order/BinderInfo and all ordinary binder names checked. |

## Generalisation: every effective binder

Data/type drop failures below establish signature/current-proof necessity, not mathematical impossibility. Expected-failure files never certify axioms. Positive files are separate exit0 evidence.

| Binder | Classification/use | Compiled candidate and decision |
|---|---|---|
| τ : Type* | type variable, polynomial/index domain | Already universe polymorphic. Drop/domain-placeholder probe fails signature formation; keep. No different domain requested. |
| Fintype τ | class, cardinal and finite Θ | Omission probe fails Fintype synthesis in the statement. A bare Finite cannot supply the statement's chosen Fintype.card; keep. |
| DecidableEq τ | decidability | Omit in original strict theorem and new theorem; selected drop. No classical global instance. |
| δ : ℝ | value, square root/coefficient ratio | AutoImplicit-false drop fails formation; keep. Abstract field cannot support the existing real Θ and square root without restatement. |
| hδ0 | proposition | Drop fails direct index-theorem premise; strict→weak 0≤δ compiles in complete candidate; keep weakened. |
| hδ1 | proposition | Drop fails direct index-theorem premise; strict→weak δ≤1 compiles; keep weakened. |
| r | structure value, degrees/weights | Drop fails formation; keep. |
| hr0 | proposition | Fresh strict theorem omission compiles, independently of boundary weakening; selected drop. Published index theorem derives all necessary positivity. |
| hrp | proposition | Replace reciprocal strict bound by 3≤(r none:ℝ), matching numerical requirement; complete candidate compiles. Further 0<r none probe fails premise type; no unsupported widening. |
| hratio | proposition | Weak coordinate inequality suffices; full candidate and old strict adapter check it. Drop fails required bound. All coordinates are used by the arbitrary derivative estimate; no single-coordinate localization. |
| r₁ | value, coefficient-bound parameter | Drop fails formation; keep. |
| hr₁ | proposition | Drop fails index-theorem premise; keep the all-coordinate degree upper bound. |
| q | structure value, rational denominators | Drop fails formation; keep. |
| hq | proposition, preserved public contract | Separate positive experiment clones the full frozen K proof without its unused hq, then proves the hq-free target. This is assessment only: explicit user preference retains hq. No artificial uses/linter masks. |
| B | value, coefficient bound | Drop fails formation; keep. |
| hB | proposition | Drop fails Θ_le_of_forall_index_le premise; keep. This audit does not speculate about changing that public wrapper or empty-family behavior. |

Exact adapter permits only the named selected omission/weakening set. For old strict hrp, its real≥3 proof is `(3≤10).trans ((le_div_self ... hδ0 hδ1.le).trans hrp.le)`. Strict hδ0/hδ1/ratios specialize by `.le`. All old retained ordinary names/types/BinderInfo, positional universe parameters, and result are verified. `Θ_lt` keeps its **entire** old public type and proof, with only the actual call adapted; its proof value is checked to contain the new target constant. Its own larger cleanup is outside this leaf.

## Literature, inversion and search

Local primary project source: `.mathlib-quality/references/clean.tex`, lines704–733, Lemma `roth:lem6`. It states strict 0<δ<1, positive degrees/denominators and the stronger reciprocal separation. The proof first bounds each index and then takes a maximum/supremum. The relaxed boundary result comes from the compiled already-published K theorem, not from claiming the source printed weaker hypotheses.

Fresh web queries: `"Formalizing Roth" "Lemma 6"`; `"Roth" "index" "polynomials" "Lemma 6" generalization`; `Roth theorem Dyson lemma index polynomial theta bound`. Results include primary [Diophantine Geometry lecture notes](https://ziyangjeremygao.github.io/LectureNotes/DiophantineGeometry.pdf), primary [Dyson's theorem for curves](https://preprints.ihes.fr/storage/dyson3.pdf), and search hits about broader Roth/Dyson index methods. None provides an exact replacement for this project's finite Φ formula or justifies an extra live API change. ChatGPT math MCP is not available among exposed capabilities; no second-opinion request claimed.

Inversion check: the proof's only concrete mathematical use is `index_le_lem6`; after `Θ_le_of_forall_index_le`, the remaining finite-supremum domination is abstract order reasoning already supplied by `Finset.le_sup'` and multiplication monotonicity. Extracting another generic wrapper would duplicate that API and provide no new content. The public source wrapper is explicitly retained. No speculative abstract theorem or new helper added.


### Five actual methods

Raw native MCP responses: `/private/tmp/roth-public30-option/search-results.json`.

| Method | Fresh actual query/result |
|---|---|
| A Lean-Finder | Roth lemma6 supremum of weighted polynomial indices at rational points / maximum square root Φ → unrelated additive Roth-number estimates and Chevalley complexity; no target replacement found. |
| B Loogle | `Finset.sup', _ ≤ _` → `Finset.le_sup'`, sup'_le, sup'_mono, sup'_le_iff and sup'_mono_fun. The exact finite-maximum step uses `Finset.le_sup'` directly. |
| C LeanSearch | Roth polynomial index supremum determinant square root → Matrix.det_le and unrelated additive Roth-number bounds. Determinant absolute-value result is upstream, not this theorem's conclusion. |
| D source rg | Untruncated full names Θ_option_le/index_le_lem6/lem6Φ across Mathlib: no hits. Standard `Data/Finset/Lattice/Fold.lean` and conditionally complete lattice source inspected for le_sup'/sup'_le/csSup_le. Logs `mathlib-target-grep.log`, `mathlib-order-api.log`. |
| E native local names | Θ_option_le → empty with index **unavailable**, not absence evidence. Finset.le_sup' → actual source hits for le_sup', le_sup'_iff, le_sup'_of_le. |

Auxiliary variants: sup'_le, sup'_mono, sup'_mono_fun, le_sup'_of_le and le_sup'_iff; generic csSup_le and multiplication monotonicity. No common-equivalent discrete/compact/coset/boundedness bucket applies. No complete replacement found within the bounded searches; no mathematical absence claim. The user-selected public wrapper stays; no convenience wrapper introduced.

Fresh compiled anonymous searches use the **entire exact source prefix before 30**, with no imported Theta module, matching target, or prior failed named theorem available. Seven examples: exact?, apply?, grind, aesop, simp_all, decide and gcongr. The batch exits1 as expected; none closes the target. Conservative scratch maxHeartbeats10000 is a decrease, not a production limit change. Previous stalled native multi_attempt behavior is recorded in dispatch; that unbounded experiment is not repeated. Positive numerical positivity/gcongr and Icc lia tests are separate from expected-failure files.

Exploration failures are retained honestly: a maximally compressed Finset.le_sup' call left its function unresolved; adding only the real codomain still did not infer the function. The selected proof keeps the explicit finite-maximum function, as the original did. The first full caller clone also required the original private log helper in its scratch namespace and properly indented multiline exact application. These failed files/logs (first/second candidate attempts and candidate-only) do **not** certify axioms. The corrected complete candidate exits0, checks all requested old contracts and entire caller values, and contains no error/PANIC/sorryAx.

## Measured signature packing and inequalities

The initial candidate's first signature line had74 codepoints; adding the next complete24-character hrp binder gives99, so it was repacked. Moving hr₁ and q into the next line then gives99. Final codepoint table below covers **every** signature line; mathematical expression continuations use the next complete expression group, never a partial identifier or unmatched binder. Width100 #check is in the positive and final actual logs.

| Signature line | Width | Next complete binder/expression | Arithmetic | Action |
|---|---:|---|---|---|
| 1 | 99 | hratio binder45 | 99+1+45=145>100 | ok |
| 2 | 99 | hq binder19 | 99+1+19=119>100 | ok |
| 3 | 46 | Entire Θ conclusion201 | 46+1+201=248>100 | ok |
| 4 | 83 | Entire lambda function121 | 83+1+121=205>100 | ok |
| 5 | 64 | sqrt/add/closing continuation62 | 64+1+62=127>100 | ok |
| 6 | 70 | Proof body follows | n/a | ok |

No short standalone conclusion is left dangling: the conclusion is a201-character expression, and the remaining signature lines split its finite supremum/function at natural expression boundaries.

| Occurrence | Final code | Orientation/rewrite |
|---|---|---|
| hδ0 | 0≤δ | smaller side left; selected strict→weak |
| hδ1 | δ≤1 | smaller side left; selected strict→weak |
| hrp | 3≤(r none:ℝ) | smaller side left; selected reciprocal-bound weakening |
| hratio | (r none:ℝ)≤δ*r(some j) | smaller side left; selected strict→weak |
| hr₁ | r j≤r₁ | unchanged |
| hq | 0<q j | unchanged, explicitly retained |
| hB | 1≤B | unchanged and used |
| conclusion | Θ B q r≤2*sup'… | unchanged |
| Reversed tokens/name | zero ≥/> and no _ge_/_gt_ | no orientation rename |

## Every golfing rule (42/42)

| Rule | Concrete status |
|---|---|
| 1.1 by exact | No by-exact wrapper; target has substantive witness/supremum steps. |
| 1.2 by rfl | No reflexivity goal. |
| 1.3 rw+exact | No target rewrites. |
| 1.4 simp+exact | No target simp. |
| 1.5 trailing rfl | None. |
| 1.6 constructor | No conjunction/pair goal; correlated witness is obtained from K. |
| 1.7 apply+exact | None. |
| 1.8 by_contra | No contradiction branch. |
| 1.9 eta reduction | Function l↦Φ(l)+√Φ(l)+√δ is not eta-reducible. |
| 1.10 single-use have | No haves; obtain carries the used l/bounds/index proof. |
| 1.11 apply+intro | Already refine Θ_le_of_forall_index_le with lambda. |
| 1.12 redundant show | None. |
| 1.13 obtain | Already obtains the shared l,hl,hl',hle. |
| 1.14 merge rw | No target rewrites. |
| 1.15 terminal simp | None. |
| 1.16 nonterminal simp | None. |
| 1.17 dot notation | hle.trans and strict-to-weak .le specializations. |
| 1.18 trailing parens | No useful lambda/parens simplification; explicit function required by elaboration. |
| 1.19 push Not | No pushed negation. |
| 1.20 trivial exists helper | No private existential helper; no new helper. |
| 2.1 grind | Fresh anonymous whole-target failure in automation.log. |
| 2.2 delete before grind | No retained grind. |
| 2.3 simpa consolidation | No simp/closing chain. |
| 2.4 fun_prop | No continuity/differentiability/measurability predicate. |
| 2.5 positivity | Separate positive scalar0≤2 test succeeds; existing tiny norm_num scalar certificate retained. |
| 2.6 gcongr | Whole-target attempt does not solve; separate real scalar monotonicity test succeeds. Direct mul_le_mul_of_nonneg_left is already explicit and cheap. |
| 2.7 lia/omega | lia proves nonempty Icc arithmetic; selected replacement for omega in target's statement proof. |
| 2.8 aesop | Fresh whole-target attempt does not close within conservative budget. |
| 2.9 norm_num/cast | Tiny constant2 positivity stays norm_num; no target cast normalization goal. |
| 2.10 decide | Whole-target decidability attempt fails; no native_decide. |
| 2.11 field_simp/ring | No algebraic equality/denominator identity in target proof. |
| 2.12 linear_combination | No ring/ring_nf step or algebraic identity. |
| 2.13 wlog | No symmetric branches. |
| 2.14 calc composition | hle.trans composes index estimate and scaled finite maximum; no redundant calc. |
| 2.15 <;> | No collection of similar subgoals; refinement leaves one maximum bound. |
| 3.1 erw | None. |
| 3.2 fun_prop | No continuity/measurability tactic. |
| 3.3 omega→lia | Applied in Icc nonemptiness proof; compiled exact old adapter makes proof-irrelevant result term compatibility explicit. |
| 3.4 rcases rfl | No such pattern. |
| 3.5 automation attributes | No new attribute: this specialized source bound is not a simp normal-form identity. |
| 3.6 simp_all | Whole-target trial does not close; none retained. |
| 3.7 maxHeartbeats | No production option before/after; no limits raised. |

Step-back/simplify reflection: generic order APIs already express all remaining proof steps. Eliminating the explicit finite-maximum function caused real elaboration failure, so the selected five-line proof keeps it. No duplicated substantive mathematical block, new helper, unused alias, artificial hypothesis use or alternate proof strategy remains justified. A built-in `/simplify` invocation is not exposed in this runtime; this is the explicit local simplify review, not a claimed tool invocation. Buzz is the real drained prefix workflow below.


## Successful proof/build/native gates on the final source

Pre-edit `candidate-compatibility.lean` exited0 after the recorded failed exploration attempts; no error/PANIC/sorryAx in accepted output. It checks the concrete new30 declaration, exact full old30 adapter, **entire**204-line old `Θ_lt` declaration/proof and its208-line adapted counterpart, all ordinary retained binders/names/BinderInfo, common positional universes, opaque proof-value types, standard axioms, and explicit dependency of the new full caller on new30. No header-only comparison or invocation of the current theorem as an independent original proof.

Successful isolated omission/proof gates:

| Gate | Actual command suffix / exit | Result |
|---|---|---|
| Original strict DecEq/hr0 omission | `lake env lean /private/tmp/roth-public30-option/drop-positive.lean`,0,25.487s | Standard axioms only. |
| Protected hq omission experiment | `lake env lean /private/tmp/roth-public30-option/binder-positive.lean`,0,26.820s | Full frozen K proof cloned without hq, then whole target proved; standard axioms. Assessment only, hq retained. |
| Every negative binder/weakening | `lake env lean /private/tmp/roth-public30-option/binder-negative.lean`,1,25.908s | All16 named ranges reached and have errors; no maxErrors truncation. `binder-results.json` maps exact ranges/errors. No false impossibility claim. |
| Seven anonymous automation examples | `lake env lean /private/tmp/roth-public30-option/automation.lean`,1,30.976s | exact? fails; apply? hits conservative budget; grind fails; aesop/simp_all leave goals; decide rejects free variables; gcongr makes no progress. No selfproof suggestions accepted. |
| Final packed candidate + local automation | `lake env lean /private/tmp/roth-public30-option/local-positive.lean`,0 | Standard axioms; actual #check; positivity/gcongr/lia local tests and identifiers verified. |

Final source SHA256: `c488d3189154ae0da29fd6d798c3b1d016e44fa588ab4ab32a5ea7c93c3837fd`.

`/Users/ramin/.elan/bin/lake build Roth.Theta` exited0, "Build completed successfully (2423 jobs)"; raw `final-module-build.log`. Then, sequentially, `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-public30-option/actual-compatibility-final.lean` exited0; no error/PANIC/sorryAx and all expected markers. It preserves the whole original Index+Theta proof namespace byte-for-byte and all inherited K29/old30/private-FIRST/value/axiom/deleted-helper absence checks. It now also verifies **actual built Θ_lt's complete old type and opaque value**, with no permitted binder drops, and direct new30 proof dependency. New30 exact old adapter permits precisely DecEq/hr0 drops plus named hδ0/hδ1/hrp/hratio weakenings. Both actual theorem values and original/recovery values use only propext, Classical.choice and Quot.sound.

Original immutable Index block hash remains `72cfbff9abab811d59c4037bc09f00e3e5f326d8435ff6dd03f0e73301eb7b2f`; Theta block remains `355a53300f7f991dbf4ee28c034a5a88bedadad5935a5ddc08363a5e887f52da`. `scope-verification.json` confirms exact owned substitutions only and all three live helpers byte-identical. This narrower successful source does **not** claim the owner's future all29 final-state generator has compiled.

Fresh native `lean_goal` at actual line595 confirmed the new effective hypotheses, including retained hq, and the scaled finite-supremum subgoal. Then **complete unfiltered** native `lean_diagnostic_messages(file_path="Roth/Theta.lean")` with no declaration/line/severity filtering returned success=true, partial=false, timed_out=false, no failed dependencies, zero errors and eight warnings. Raw complete responses `final-live-goal.json`, `final-lsp.json`. All three old target warnings disappeared (unused section DecEq, unused hr0, and unused-DecEq-in-type). Remaining warnings: header line1, hr93, hB/hr101, hB109, hr129, hr252, protected hq547; none is suppressed or in this target. Earlier explicit public-hypothesis/header preferences remain respected.

| Diff gate | Result and evidence |
|---|---|
| lake_build_file | PASS, actual `lake build Roth.Theta` exit0 cited above. |
| definition_protected | PASS, exact scoped comparison: no definition/import/header change. |
| theorem_statement_protected | PASS for exact selected changes, full immutable-original adapter/name/type/BinderInfo/universe/axiom checks; Θ_lt entire old public type unchanged. |
| structure_gate | PASS, target5 proof lines≤15; no branch/conjunction/shared-witness split. The routine caller Θ_lt has its own original35 audit later; next original31 is the private log helper. |
| naming_gate | PASS, no forbidden pattern/abbreviation; no renames. |
| line_packing_gate | PASS, full six-row measured table above; max99 codepoints. |
| inequality_orientation_gate | PASS, all8 occurrence rows above; zero reversed tokens. |
| new identifiers | Finset.le_sup' verified by native local source lookup, source rg and compiled #check; le_div_self, le_of_lt, trans, lia and norm_num verified by accepted candidate/module/actual compile. No new unverified lemma name. |
| comments/public wrappers | PASS, docstring and every caller narrative preserved; public domains/wrappers/conclusion retained. |
| cumulative external build | Owner gate pending; sole routine call in Θ_lt already builds and its complete old-type/value/dependency checks pass. |

At UTC2026-10-18T23:19:45, all ordinary compiler/search/native-LSP requests were drained, pending_requests=[], source editing authority revoked and the above SHA frozen. `normal-requests-drained.json` and `source-freeze.json` record this before the performance phase. Only report writes and sequential real profile subprocesses follow; source stays immutable.


### Result and 11-step verification checklist

Immediate pre-audit target proof: 8→5 lines (−3); the immutable initial inventory has6 proof lines, so initial→final is6→5. The temporary8-line baseline includes the earlier K caller forwarding. Whole file: 946→948 lines (+2, including the necessary four-line caller expansion and one omit line). Target/public result names, domains, output formula and original documentation retained. No renames queued, no new helper, no shared-file/Git mutations.

- [✓] Step1: required references read.
- [✓] Step2: all24 audit items have concrete statuses.
- [✓] Step2.5: all five search methods actually run, raw responses retained.
- [✓] Step2.6: all effective binders classified, compiled drop/weakening/positive-protected probes, literature and inversion checked.
- [✓] Step2.7: every signature line measured/repacked, final table emitted.
- [✓] Step2.8: all inequality occurrences scanned; no reversed tokens.
- [✓] Step3: all42 golf rules recorded; failed and accepted trials distinguished.
- [✓] Step4: explicit whole-proof/simplify reflection, no unnecessary helper.
- [✓] Step5a: complete unfiltered native LSP, zero errors/zero target warnings.
- [✓] Step5b: actual module, immutable originals, exact old adapters, entire actual caller values/dependency and standard axioms; diff gates above. Performance gate is separately reported below.
- [✓] Step6a: no rename required; no queue mutation permitted or made.

Owner publication counts after successful owner gates:211/264 originals,Theta30/35,nine project files. This leaf does not stage/commit/push or claim those owner gates have run.

## Buzz — frozen actual all-five exact prefix through 30

First final real trace completed exit0 in178.234s, raw157442529 bytes. Correct command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-public30-option/final-prefix.lean`. No other compiler/LSP/search request active; source remained frozen. Raw `final-profile.log`, `final-profile-manifest.json`, `final-timings.json` preserve exact declaration anchors and disjoint top-level outer/async rows, including proof/kernel/compiler costs without nested double-counting.

First final totals: target30=158.615ms, public29=901.577ms, numeric903.545ms, mapped693.423ms, weight401.279ms. All five<1000ms. Source/full-live hash is c488d318…3837fd; exact prefix hash is `9033a46506ec0ca783c627ceb4dc5c2c73a53708920834928edad9ea44d34d1e`. Because public29 and numeric≥750ms, all five were repeated on this **same final SHA and identical prefix**, after inspection of the completed first trace. The original pre-edit baseline overages remain recorded above; they are not hidden or substituted for final evidence.


### Required repeat accepted and final frozen handoff

The required same-source all-five repeat completed exit0; its exact runtime/log-byte manifest is `repeat-profile-manifest.json`. Raw `repeat-profile.log`, `repeat-timings.json` retain all anchors and disjoint costs. Same full/live/prefix SHA as the first trace, sole uncontended compiler, no source edit or ordinary request between traces.

| Target | First ms | Repeat ms | Repeat outer/proof line anchors | Result |
|---|---:|---:|---|---|
|weight_le_delta_aux|401.279|399.404|1087672/1087702|both<1000ms|
|mapped_det_ne_zero_aux|693.423|723.578|1135159/1135262|both<1000ms|
|index_numeric_bound_aux|903.545|922.672|1237522/1237567|both<1000ms|
|index_le_lem6|901.577|925.763|1346701/1346790|both<1000ms|
|Θ_option_le|158.615|144.368|1468836/1468942|both<1000ms|

Overall leaf gates: PASS; owner cumulative/build/publication gates remain pending.

Buzz outcome: FAST-BOARD on both accepted real **prefix-through-30** traces. Target30 reduced217.512→158.615ms on the first final trace. This is not a whole-Theta timing claim: later Lemma7 declarations lie outside the prefix; the owner's eventual whole-module sweep remains required. No deferred over-budget target among these five. Zero production limit raises/masks, profiling scaffolding, sorry, native_decide, new axiom, new helper, or changed helper.

Final source SHA256 `c488d3189154ae0da29fd6d798c3b1d016e44fa588ab4ab32a5ea7c93c3837fd`. Source editing authority remains revoked. All requests fully drained, pending_requests=[]; compiler/native-LSP window returned to owner. Only this report was written after source freeze. No Git mutation.

Owner next compiles its updated cumulative29-public compatibility generator, then full `lake build`, then separate `lake build Roth.LeanEval`, updates central records, exactly stages/commits/pushes the checkpoint, and only then starts original31. These owner gates are **pending**, not claimed completed by this leaf. Latest actually compiled compatibility source: `/private/tmp/roth-public30-option/actual-compatibility-final.lean`. Expected post-publication counts211/264,Theta30/35,nine files.


## Owner cumulative original-public recovery

After leaf revocation/drain, owner compiled the first cumulative29-public compatibility probe
exit0 in53.314s, with29 explicit entire old-telescope adapters and only standard actual axioms.
Its byte-exact source is archived at `/private/tmp/ThetaApprovedOriginalFinalProbe-d30-first.lean`
(SHA256 `86cba9d1e262161d9b139e43beb5bd90d5a69ceebae1c39e1b14873d2d321cdf`); raw log and
record `/private/tmp/roth-theta-d30-cumulative29.{log,json}`. This verifies all currently applied
selected A/B/C changes and supported G–L changes, rather than presenting a future-state file
as already compiled. All five original definition values and all original public conclusions
are recovered; changed hypotheses are forwarded by exact checked old-contract adapters.

Owner then completed the frozen full build and separate LeanEval, and enhanced the same verifier
with explicit `value! true` body-type checks for EVERY original/current/recovery constant.
The enhanced standalone command `lake env lean /private/tmp/ThetaApprovedOriginalFinalProbe.lean`
exited0 in48.324s on the identical final source. Actual log markers:29 entire original adapters,
87 opaque body-type passes,87 actual axiom-set checks,29 complete public passes. No error/PANIC/
sorryAx. The exact enhanced source is archived at
`/private/tmp/ThetaApprovedOriginalFinalProbe-d30-values.lean`, SHA256
`a50b3671f6e0579e44d759b1c05fe6435d3bba4a0cb3b581c6b1dff9f983192a`; raw log/record
`/private/tmp/roth-theta-d30-values-cumulative29.{log,json}`. The independent entire Index and
Theta original proof blocks remain byte-identical, respective hashes72cfbff9…eb7b2f and
355a5330…7f52da (full hashes in record). Both module/public-value recovery and all actual
standard axiom sets are checked, not inferred from successful project compilation alone.

All17 project/source/pin hashes still match the frozen owner build snapshot after this enhanced
probe. No Lean source changed, so the passed real profiles and sequential owner builds remain
valid. These are CURRENT cumulative contract certificates; no later whole-file performance or
original31–35 audit is claimed. The remaining final file-wide phases are mandatory.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (113.288 s),
then separate `lake build Roth.LeanEval` (37.676 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `c488d3189154ae0da29fd6d798c3b1d016e44fa588ab4ab32a5ea7c93c3837fd`.
Raw logs: `/private/tmp/roth-theta-d30-full.log`, `/private/tmp/roth-theta-d30-leaneval.log`; machine record
`/private/tmp/roth-theta-d30-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 30/35, overall 211/264 original
declarations, 9/14 completed files. No new private helper; all three previously audited helpers unchanged. Original counts exclude revisits and helper audits.
