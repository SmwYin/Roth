# Dedicated fresh audit: `Roth.theta_prefix_lt_aux`

This is one introduced-helper obligation inside original35's unpublished Θ_lt cleanup.
No original-count credit: published count remains215/264; original35 is not published by
this audit. Nine retained and two introduced/deleted helper obligations remain in the
batch inventory; this audit introduces/deletes no production helper.

Artifacts below are under `/private/tmp/theta35-prefix-lt-fresh/` unless absolute.
User-authorized scope: the ENTIRE private target, necessary routine proof-call changes,
and this report. No Git, shared logs, other declarations or pins were mutated.

## Result and baseline

The private `hanti` premise is weakened from `Antitone r` to
`∀ j, r (Fin.last (n + 1)) ≤ r j`. These are precisely the last-is-minimum comparisons
used to prove positivity of every weight and the prefix's last-weight lower bound.
The sole direct consumer passes `fun j ↦ hanti (Fin.le_last j)`.
A positive compiled example `![5,6,3]` satisfies the localized premise and is not antitone,
so this is a substantive hypothesis weakening. The exact FIRST Antitone contract is
recovered by an explicit adapter. All18 retained binder names/order/BinderInfo/universe
arity, every other dependent type, and the conclusion are checked against FIRST.

Single-use inner positivity/ratio h certificates are inlined; the positivity expression
needs an explicit real type ascription (the untyped candidate failed and is preserved).
Unsqueezed terminal `simpa [mul_assoc]` compiled, but actual f23 profiling measured
508.747ms there and1409.941ms for the target. The original terminal `simpa only`
is retained as the measured performance exception explicitly permitted by profiling.md.
The restricted numerator certificate `nlinarith only [Nat.cast_nonneg (α := ℝ) n]`
remains unchanged. No broad-context gcongr/linarith regression was restored.
The proof shrinks30→28 lines; its longest branch is8. The signature gains one necessary
packing line. No new helper, public signature, definition, import or narrative comment.

Baseline is explicitly inherited from the identical36f9 source: complete unfiltered
native Theta/MainLemma diagnostics from the preceding prefix-log audit (0errors;8/3
warnings), and its accepted actual-profile pair877.212/918.895ms for this target,
682.808/521.668ms for phi,357.826/302.810ms for publicΘ.
The unrelated historical1539.851ms broad-context failure remains at
`/private/tmp/theta35-prefix-log-fresh/actual-profile-first.*`; it is not discarded.
Cache download/linter executable/full-project baseline are coordinator gates, not
repeated by this scoped worker. Fresh affected-module builds, diagnostics, semantics
and real profiles are recorded below. Whole-project build/LeanEval remain owner gates.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, cleanup-gates.md, the cleanup worker workflow, both skills,
and relevant style/naming/profiling references. The actual Lean4.34 profiling invocation
follows the dispatch correction, not the obsolete reference command.

## All24 audit items

| # | Item | Concrete disposition |
|---|---|---|
| 1 | Lint | Inherited same-SHA baseline is complete and unfiltered: eight Theta/three MainLemma warnings, none on this helper. Fresh final complete diagnostics below. |
| 2 | Have scan | hr0 is a three-line positivity certificate used under Θ_mono. Inline its single-use inner h certificate directly into lt_of_lt_of_le. hCeq names the cast/Fin normalization needed by rw; h2 bridges the last-minimum comparison to the scaled lower bound; both have explicit by proofs. Inline the by-free single-use ratio h := hratio (Fin.castSucc i) into mul_le_mul_of_nonneg_left. Final production has only hr0/hCeq/h2, each with proof content. |
| 3 | Options | No production per-declaration option, raised limit, attribute or diagnostic scaffolding. Only scratch whole-goal automation lowers maxHeartbeats to 10000. |
| 4 | Simp | hCeq ends with unsqueezed simp [Nat.cast_mul]. Actual unsqueezed terminal simpa [mul_assoc] compiled but caused a508.747ms hotspot and1409.941ms full target regression on f23. Restore terminal simpa only [mul_assoc, Fin.castSucc_zero] as the measured performance exception explicitly permitted by profiling.md; raw/source/trace preserved. |
| 5 | Naming | theta_prefix_lt_aux describes the strict Theta bound on a prefix, uses snake_case/private _aux, and matches no numbered auxiliary/scheme/forbidden-abbreviation pattern. No rename. |
| 6 | Packing | Every one of fourteen current signature lines measured in packing.json; all complete-next-item sums exceed100. The extra signature line separates the longer localized hanti from hrlast. No proof line exceeds100. |
| 7 | By | All := by occur on the preceding statement line; inline by certificates are likewise attached. No standalone by. |
| 8 | Format | Two-space proof indentation, no empty proof lines or tactic semicolon chains. Existing finite-index lambdas retain ↦. |
| 9 | Comments | No target narrative comments existed; none removed. Sole necessary caller's one-variable/prefix/combine comments and every unrelated comment preserved byte-for-byte. |
| 10 | Docstring | Private helper correctly has no docstring; public and module documentation untouched. |
| 11 | Visibility | Private auxiliary, sole direct production consumer theta_phi_lt_aux. No external API surface added. |
| 12 | Structure | Twenty-eight proof lines, ratio branch eight, remaining branches/subproofs at most five. No statement conjunction or trivial existential. No new helper needed. Public Θ_lt remains within15. |
| 13 | Mathlib | All five actual search methods retained, plus corrected clean exact-CURRENT-prefix anonymous generic-route trials below. An independent exit0 environment check proves the audited helper/later Root Θ_lt absent. The earlier import Roth.Theta batch is superseded/contaminated and excluded from search evidence. Generic scalar components remain used directly; this substantive Θ induction transport is retained. |
| 14 | Junk def | n/a: theorem, no data definition or custom predicate. |
| 15 | Exists | n/a: no existential conclusion or witness wrapper. |
| 16 | Show/change | n/a: neither tactic appears. |
| 17 | Negation | n/a: no push_neg/by_contra; no negation normalization required. |
| 18 | Generalise | All eighteen effective binders independently drop-tested in original and current forms; strict/weak numerical and point-local candidates compiled. Antitone hanti is safely weakened to the last-is-minimum comparisons actually needed, with exact immutable-FIRST adapter and current-type assertion. Details below. |
| 19 | Inequality | Sixteen signature inequality occurrences use < or ≤. No reversed ≥/>; name contains no _ge_/_gt_. Per-occurrence artifact below. |
| 20 | Normal form | Finite prefix/scaled exponent transport uses the established Θ convention and ordinary smaller-side-left inequalities. No alternate custom canonical predicate. |
| 21 | Syntactic generality | Localized last-minimum premise is directly supplied by fun j ↦ hanti (Fin.le_last j) at the sole consumer; all other arguments and IH convention stay identical. |
| 22 | Import fanout | n/a: imports unchanged. |
| 23 | Casts | The removed inner have carried (3 : ℝ) ≤ r j; its annotation moves onto the inline positivity expression and is load-bearing (untyped inline candidate fails with unresolved cast result type). No new cross-type coercion is introduced. Existing Nat-to-Real crossings and α:=ℝ in the restricted numerator certificate remain necessary; zero redundant casts recommended. |
| 24 | Instances | No universe, typeclass or decidability binder and no new instance. Both original/current effective telescopes contain precisely eighteen ordinary/implicit binders. |

## Five actual search methods and compiled generic routes

Raw complete native responses are `search.json`; source outputs are
`mathlib-full-name-search.log` and `mathlib-source-search.log`.

| Method | Actual query | Observed result |
|---|---|---|
| A Lean-Finder | Roth index theta induction prefix restricting Fin and multiplying exponents geometric ratio bound | Returned unrelated additive-combinatorial Roth-number/Behrend results; no full target match. |
| B Loogle | Antitone ?r, _ (Fin.last _) ≤ _; corrected Antitone, Fin.last | First query rejected placeholder-as-function; corrected clean query returned zero items. Failure is recorded, not treated as an absence proof. |
| C LeanSearch | antitone finite sequence restriction last minimum multiplication positive scale | Found Antitone.const_mul, AntitoneOn.monotone and other scalar/order components. |
| D source rg | full theta_prefix_lt_aux; Antitone.const_mul/div_le_div₀/le_mul_of_one_le_left/mul_le_mul_of_nonneg_left | Untruncated full-name output empty; generic division/multiplication components found with exact source positions. |
| E local names | Antitone (limit12) | Returned Antitone.mul/const_mul and variants; index unavailable, so no indexed-absence inference. |

Auxiliary variants include Antitone.const_mul/const_mul', AntitoneOn.mul_const',
mul_le_mul_of_nonneg_left/right, and simultaneous quotient comparison div_le_div₀.
Discrete/finiteness/separation/bornology common-equivalent buckets do not describe this
higher-order induction transfer. `Positive.lean` #checks the generic names.
Remote tool indexes may lag the pinned local Mathlib; current source/component #checks
are authoritative for this checkout. No full Mathlib absence claim is made. The relevant scalar components are present and
used directly; Θ and its induction hypothesis are project-specific. This is not a thin
one-to-three-Mathlib-call wrapper: it establishes positivity and transports the last,
ratio, logarithmic, scale and lower-degree hypotheses together. Retain the helper.

Search-hygiene correction: the original `AutomationNegative.lean` imported
`Roth.Theta`, which put the current matching private target in the environment despite
its separate namespace and anonymous examples. It also tested the FIRST Antitone
signature. That entire attempt is SUPERSEDED/CONTAMINATED and excluded from generic-route
or absence evidence. Its exact source/log/status and the pre-correction report/freeze
are archived with hashes in `automation-correction-provenance.json`.

`AutomationCorrected.lean` starts with the exact CURRENT production bytes[0:44312]
through line767, ending BEFORE the target declaration, SHA256
`a2b37ea2168abcee735ca33ff08a7459f02afd7677b7e58ffaf1041d9958e520`.
The original imports and every preceding source byte are preserved, then both scopes
close explicitly with `end Lemma7` and `end Roth`. No `Roth.Theta` import is introduced.
`CorrectedPrefixAbsence.lean` independently compiles this identical clean context with
exit0/58.101s and an ACTUAL environment assertion that both the audited private target
and later public Root.Θ_lt are absent. Its positive evidence is separate from the
expected-failure automation batch.

All eleven trials are anonymous `example`s with the literal CURRENT localized
last-is-minimum18-binder header. Each has a distinct BEGIN/END marker and recorded source
range. The corrected batch exits1 normally in71.403s, with every strategy reached and a
compiler failure in each range; default maxErrors was not raised and no trial was hidden
by an error cap. The scratch10000-heartbeat bound only lowers the automation budget.
No named failed target can contaminate later exact?/apply? lookup. Details/raw messages
are in `automation-correction-results.json` and `automation-corrected.log`.

| Corrected current-goal strategy | Actual source error lines | Observed compiler result |
|---|---|---|
| grind | 799 | : `grind` failed |
| aesop | 817 | : Tactic `simp` failed with a nested error: |
| exact? | 835 | : `exact?` could not close the goal. Try `apply?` to see partial suggestions. |
| apply? | 853 | : (deterministic) timeout at `whnf`, maximum number of heartbeats (10000) has been reached |
| simp_all | 871 | : Tactic `simp` failed with a nested error: |
| gcongr | 889 | : `gcongr` did not make progress. |
| positivity | 907 | : not a positivity goal |
| norm_num | 924 | : unsolved goals |
| lia | 943 | : `grind` failed |
| decide | 961 | : Expected type must not contain free variables |
| field_simp/ring | 978 | : unsolved goals |

These are bounded unsuccessful routes, not general Mathlib theorem-absence proofs or
axiom evidence. No unbounded native multi_attempt was repeated. The corrected independent
positive prefix/environment gate has exit0; expected-exit1 trials never certify axioms
or positive proof soundness. Production source remains6bd, so prior semantic/native/
profile evidence is preserved unchanged; none of those gates were rerun for this
report/scratch-only correction. No optimization or production source edit was authorized.

## Every effective binder; mechanical/mathematical generality

`BinderNegative.lean` independently drops every FIRST binder; `BinderCurrentNegative.lean`
repeats every drop with the localized current hanti. `BinderFinalNegative.lean` repeats
all20 individual drop/strict-weak trials with the FINAL selected28-line proof, with
exact final source/error ranges in binder-final-ranges.json/binder-final-results.json. autoImplicit=false prevents hidden
reintroduction. `binder-ranges.json` and `binder-results.json` map each trial to actual
error lines. Proof failures establish that these mechanical proof substitutions did not
work; they do not prove logical indispensability of the hypotheses.

| Binder | Class | Use | Compiled candidates | Disposition |
|---|---|---|---|---|
| n | implicit ℕ | Finite dimensions and numerical exponent | individual drop | Unknown n in dependent types; retain Nat dimension. |
| δ | implicit ℝ | ratio and denominator | individual drop | Unknown δ; no generic field widening with project Θ/Real.log/rpow fixed. |
| ε | implicit ℝ | IH ratio/rpow and bound | individual drop | Unknown ε; same Real-valued construction restriction. |
| M | implicit ℝ | Θ argument and scale comparison | individual drop | Unknown M in dependent statement. |
| hδ0 | explicit proposition | strict lower denominator in div_le_div₀ | drop;0<δ→0≤δ | Both fail; retained strict positivity. |
| hδε | explicit proposition | quotient order and scaled ratio | drop | Unknown hδε in both certificates; already weak ≤. |
| r | implicit Fin(n+2)→ℕ | all weights and prefix | individual drop | Unknown r; finite natural multiplicities are part of Θ. |
| q | implicit Fin(n+2)→ℕ | logarithmic denominators and prefix | individual drop | Unknown q; established Θ denominator domain preserved. |
| hanti | explicit proposition | last-weight minimum at two uses | drop; point-localize to ∀j,rlast≤rj | Drop fails; point-local complete candidate compiles; APPLY localization. |
| hrlast | explicit proposition | positivity and IH last lower bound | drop;3≤last→1≤last | Both mechanical proofs fail; retain numerical threshold3. |
| hratio | explicit proposition | prefix successor-ratio certificate | drop | Unknown hratio; already point-local finite-index family/weak inequality. |
| hq1 | explicit proposition | log bound after quotient comparison | drop | Unknown hq1; already weak ≤. |
| hqr | explicit proposition | weighted-log ordering for every prefix index | drop | Unknown hqr; every prefix point is used, no single-point replacement supplies entire family. |
| l | implicit ℕ | scaled natural multiplicities | individual drop | Unknown l in statement; replacing ℕ by ℝ changes Θ domain. |
| hl | explicit proposition | Nat.mul_pos and one≤cast-l | drop;1≤l→0≤l | Both fail; retain positive integer scale. |
| hM1 | explicit proposition | Θ_mono lower-scale hypothesis | drop;1≤M→0≤M | Both fail; Θ_mono requires1≤M. |
| hM | explicit proposition | Θ_mono upper-scale bound | drop | Unknown hM; already weak ≤. |
| ih | explicit higher-order proposition | lower-dimensional Θ bound | drop | Unknown ih; all inner Fin/weight/log premises transport substantively. |

All18 original/current effective parameters are covered; there are no hidden section,
class, decidability or universe binders. `PointLocal.lean` compiles the entire weaker
proof independently; `Positive.lean` proves the last-minimum condition is strictly
weaker than antitonicity. Scalar/weight variables cannot be mechanically generalized to
an arbitrary field/type while preserving the existing Real.log/rpow/Θ and natural
multiplicity constructions. No bundled conjunction, universe-polymorphism, class-parent
or decidability weakening applies.

Literature search: n/a, private auxiliary explicitly exempt under cleanup§2.6d. This
exemption does not skip mechanical or mathematical generality. Inversion: Θ appears in
Θ_mono and the IH and is never unfolded; the proof continues to use its established
monotonicity and lower-dimensional bound. Real.log/Fin.castSucc identify the actual
prefix hypotheses rather than a concrete witness later forgotten after unfolding.
Abstracting Θ would add its exact monotonicity/IH premises without a reusable new
mathematical object; no supported further inversion/generalisation is recommended.
No unresolved public API or mathematical preference requires user input.

## All42 golfing rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | rw hCeq precedes an induction application with multiple certificates, not a closing exact; no rwa pair. |
| 1.4 | Final cast/product transfer already uses simpa using; preserve composition. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | n/a: no constructor chain. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction branch. |
| 1.9 | Finite-index lambdas precompose q/r and multiply by l; they are not eta wrappers. hr0 lambda proves positivity and cannot eta-reduce. |
| 1.10 | APPLIED: inline the single-use inner positivity h and the by-free typed ratio h. Final hr0/hCeq/h2 retain substantive proof content; no forwarding have remains. |
| 1.11 | n/a: no apply followed by intro. |
| 1.12 | n/a: no redundant show. |
| 1.13 | n/a: no conjunction projection have. |
| 1.14 | n/a: only one rw hCeq, separated from cast normalization. |
| 1.15 | TRIED/REJECTED by actual measurement: unsqueezed terminal simpa [mul_assoc]508.747ms; target1409.941ms. Retain original simpa only [mul_assoc, Fin.castSucc_zero] as a documented measured performance exception. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Already uses .trans/.trans_lt composition; keep. |
| 1.18 | Remaining parentheses delimit arguments before additional arguments or .trans; no avoidable trailing-parenthesis block. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no trivial existential helper. |
| 2.1 | Actual anonymous whole-proof grind fails under conservative scratch cap. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.2 | n/a: no selected grind block with preceding tactics. |
| 2.3 | Final normalized weighted-log transfer remains one simpa using application. Unsqueezed complete candidate compiles but regresses actual performance; selected version uses the measured squeezed exception. |
| 2.4 | n/a: no analytic regularity/property goal. |
| 2.5 | Existing scalar numerator/product nonnegativity uses positivity. Whole-proof positivity correctly reports not a positivity goal. |
| 2.6 | Whole-proof gcongr makes no progress. Preserve restricted numerator certificate, rather than the previously measured broad-context gcongr failure. No repeated broad strategy experiment. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.7 | Whole-proof lia fails: real rpow/Theta/IH transfer, not a linear Nat/Int goal. Concrete 0<3 remains norm_num. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.8 | Actual anonymous whole-proof aesop fails; no production broad search. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.9 | Whole-proof norm_num leaves the induction goal; existing exact_mod_cast/norm_num certificates retained. Positive strict-weakness example uses finite cases/norm_num. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.10 | Whole-proof decide rejects free variables/noncomputable real proposition; no native_decide. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.11 | Actual field_simp/ring whole-proof trial leaves Theta inequality. The sole equality is multiplicative permutation without denominators. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 2.12 | Complete CandidateLinear replaces the ratio identity ring by linear_combination and compiles. Both close a hypothesis-free polynomial permutation; retaining ring expresses that intent directly, no clarity/length advantage from alternative. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | Three-row mixed ≤/= /≤ calc needs an explicit multiplicative permutation. Collapsing to a long transported term hides the scale/ratio argument; current .trans composition already removes two-step bound chains elsewhere. |
| 2.15 | Final induction side-goals have distinct lower-bound/ratio/log-invariant proofs; uniform automation does not apply. No duplicated goal closers to distribute. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy continuity/measurability tactic. |
| 3.3 | n/a: no omega; actual lia whole-goal trial fails as recorded in2.7. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No automation attribute: private higher-order induction transport with large parameter telescope has one explicit caller. |
| 3.6 | Actual anonymous simp_all whole-goal trial fails under conservative cap; no selected squeezed simp_all. Corrected actual trial uses the exact CURRENT pre-target prefix with the target absent; the earlier imported-target attempt is superseded. |
| 3.7 | Zero production limits added/raised; no profiling scaffolding or suppression. |

Step-back reflection: the substantive operation is applying Θ_mono then the inductive
hypothesis to the castSucc prefix scaled by l. Localizing the exact last-minimum
information removes unnecessary global order structure. The generic quotient comparison
already replaces the deleted scalar wrapper. Whole-goal automation does not synthesize
all invariant transports. Keep the small explicit certificate blocks, the restricted
arithmetic context, and no additional helper.

## Measured signature packing and inequality orientation

`format.width100` actual type printing is in the semantic logs. Unicode codepoint widths
and complete next binder/implication constituents are in `packing.json`.

| Sig line | Width | Next complete item width | Arithmetic | Action |
|---|---|---|---|---|
| 1 | 81 | 23 | 81+1+23=105>100 | ok |
| 2 | 69 | 41 | 69+1+41=111>100 | ok |
| 3 | 45 | 63 | 45+1+63=109>100 | ok |
| 4 | 67 | 76 | 67+1+76=144>100 | ok |
| 5 | 80 | 62 | 80+1+62=143>100 | ok |
| 6 | 87 | 13 | 87+1+13=101>100 | ok |
| 7 | 56 | 310 | 56+1+310=367>100 | ok |
| 8 | 63 | 50 | 63+1+50=114>100 | ok |
| 9 | 56 | 62 | 56+1+62=119>100 | ok |
| 10 | 68 | 58 | 68+1+58=127>100 | ok |
| 11 | 64 | 77 | 64+1+77=142>100 | ok |
| 12 | 83 | 112 | 83+1+112=196>100 | ok |
| 13 | 73 | 47 | 73+1+47=121>100 | ok |
| 14 | 54 | — | last line | ok |

| Occurrence | Signature line:column | Relation | Action |
|---|---|---|---|
| 1 | 1:78 | ≤ | already smaller-side-left; unchanged |
| 2 | 1:64 | < | already smaller-side-left; unchanged |
| 3 | 2:64 | ≤ | already smaller-side-left; unchanged |
| 4 | 3:17 | ≤ | already smaller-side-left; unchanged |
| 5 | 4:49 | ≤ | already smaller-side-left; unchanged |
| 6 | 5:64 | ≤ | already smaller-side-left; unchanged |
| 7 | 6:44 | ≤ | already smaller-side-left; unchanged |
| 8 | 6:84 | ≤ | already smaller-side-left; unchanged |
| 9 | 7:14 | ≤ | already smaller-side-left; unchanged |
| 10 | 7:27 | ≤ | already smaller-side-left; unchanged |
| 11 | 8:40 | ≤ | already smaller-side-left; unchanged |
| 12 | 9:36 | ≤ | already smaller-side-left; unchanged |
| 13 | 10:51 | ≤ | already smaller-side-left; unchanged |
| 14 | 11:40 | ≤ | already smaller-side-left; unchanged |
| 15 | 12:37 | < | already smaller-side-left; unchanged |
| 16 | 13:73 | < | already smaller-side-left; unchanged |

Zero ≥/> in signature, no _ge_/_gt_ name, no reversed inequality introduced in proof.
Source byte reconstruction verifies exactly the target replacement plus the sole phi
argument change; every other production byte is unchanged. `owned-proof.diff` records
the complete scoped diff. No definitions, public headers, narrative comments, imports,
pins, limits, attributes or scaffolding changed. The target has28 proof lines and the
ratio branch8. MainLemma and Main byte hashes are unchanged.

## Immutable FIRST and actual built semantic gates

`FirstIndependent.lean` starts with the ENTIRE exact original batch2 bytes (SHA8a7cb0f…):
its original import, namespace, declarations preceding this target, including the now
deleted original prefix-log helper, and all later batch declarations. No sections,
classes or universes were inserted into that FIRST context. The independent original
proof is re-elaborated; it does not call the current target/adapter/expected proof.
`FIRSTComplete.lean` is an unchanged archival copy. All three immutable FIRST batches
and the original success log/status hashes are checked before/after.

The explicit old adapter retains the exact FIRST full18 telescope and passes
`fun j ↦ hanti (Fin.le_last j)` to actualPrefixLt. A separate complete independent current
proof fixes the literal new last-minimum type. Meta compares original↔adapter and
expected-current↔actual-current, including name/BinderInfo/order/type/conclusion/universe
arity; a direct FIRST↔current pass checks every retained binder and every other type,
with one explicit hanti localization row. This also supersedes the inherited final
prefix-log audit's old raw FIRST/current consumer equality, rather than silently dropping
that gate. The exact scaffold delta is `semantic-scaffold-adjustment.diff` with prefix
provenance JSON.

The inherited scaffold's seven-binder deleted-prefix replacement adapter and all actual
constant/reference absence checks remain intact. Both deleted production wrappers stay
absent. The scaled13/FIRST15 adapter, delta3, publicΘ9 and all26 current MainLemma binders
(including protected unused premises) remain checked. The original Index72cf/Theta355a,
ENTIRE original2b MainLemma proof and ENTIRE current independent MainLemma proof blocks
are byte-identical at the four recorded ranges/hashes in `immutable-complete-blocks.json`.
Actual updated RootΘ/main_lemma value!true/inferred type/standard axes and positive Θ
dependency are checked; the independent MainLemma blocks reject imported Root.main_lemma
and private Root MainLemma self-use. Both affected modules were rebuilt before the actual
Root queries. No opaque value uses default value!; no PANIC/sorryAx/error is accepted.

Fresh final full semantic/FIRST compiles have exit0; timings and commands are in
actual-semantics-final.json and first-independent-final.json. Earlier f23 compiles
(180 clean PASS markers,81.970s; FIRST35.816s) are preserved as intermediate evidence.
The final marker count is verified in semantic-marker-summary-final.json.
The successful earlier f23 probe source snapshots are preserved separately alongside
their original logs; final probes use the same complete FIRST context and final proof. Allowed axioms only propext, Classical.choice, Quot.sound.
`semantic-marker-summary-final.json` contains every final marker. These gates establish semantic
compatibility independently of native diagnostics and source-text equality.

## Fresh verification and actual source performance

| Gate | Result | Actual artifact/command |
|---|---|---|
| lake_build_file Theta | PASS | build-theta-final.json: lake build Roth.Theta, exit0 |
| lake_build_file MainLemma | PASS | build-mainlemma-final.json: lake build Roth.MainLemma, exit0 |
| definition_protected | PASS | No def/abbrev bytes changed; exact reconstruction. |
| theorem_statement_protected | PASS with explicit private weakening | Only supported hanti localization; exact immutable-FIRST adapter, all public statements fixed. |
| structure_gate | PASS | 28 lines; ratio branch8; every branch/subproof≤10; publicΘ≤15 preserved. |
| naming_gate | PASS | Descriptive prefix strict-bound/private _aux; no forbidden patterns. |
| line_packing_gate | PASS | Every14 signature line measured above; each next complete constituent would overflow100. |
| inequality_orientation_gate | PASS | Every16 occurrence measured; zero reversed relations. |
| cumulative scoped callers | PASS | Theta/MainLemma builds; complete old/current Θ/Main semantic proofs; fresh full native responses below. |
| whole project and separate LeanEval | OWNER PENDING | Not run or claimed by this worker. |
| whole-file performance | NOT CLAIMED | Unrelated mandatory repair queue remains; MainLemma finite runtime still unmeasured. |

Complete unfiltered fresh native diagnostics:

| Module | Success | Partial | Timeout | Errors | Warnings |
|---|---|---|---|---|---|
| theta | True | False | False | 0 | 8 |
| mainlemma | True | False | False | 0 | 3 |

Every unchanged warning (full text also retained in raw JSON):

| Module | Line | Severity | Message |
|---|---|---|---|
| theta | 1 | warning | * `-/`: Copyright too short! |
| theta | 93 | warning | Variable name `hr` is not explicitly referenced. |
| theta | 101 | warning | Variable name `hB` is not explicitly referenced. |
| theta | 101 | warning | Variable name `hr` is not explicitly referenced. |
| theta | 109 | warning | Variable name `hB` is not explicitly referenced. |
| theta | 129 | warning | Variable name `hr` is not explicitly referenced. |
| theta | 252 | warning | Variable name `hr` is not explicitly referenced. |
| theta | 547 | warning | Variable name `hq` is not explicitly referenced. |
| mainlemma | 1 | warning | * `-/`: Copyright too short! |
| mainlemma | 149 | warning | Variable name `hδ0` is not explicitly referenced. |
| mainlemma | 149 | warning | Variable name `hr₁` is not explicitly referenced. |

A complete279.912s intermediate f23 capture (actual-profile-first.*) is preserved with
its exact source and parsed table. The final HAVE cross-check required additional
single-use certificate inlining, so this source/capture was
explicitly superseded before the final pair. An attempted own-process cancellation was
denied by sandbox EPERM; the bounded runner finished/drained normally before any edit.
Its measured1409.941ms target FAIL is preserved; terminal simpa508.747ms was the
identified hotspot, motivating the restored squeezed performance exception. The first
untyped positivity inlining candidate failed with unresolved cast result type; the
explicit typed candidate compiles. No failed experiment is counted as positive evidence.
It is not selected as a final timing. All mandatory static decisions were then closed
before the single final build/semantic/native/profile cycle.

Normal/native requests drained before each real profile; explicit process-group liveness
checks and pending[] are in the drain artifacts. The actual production command is
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Theta.lean`.
The external420s capture window is not a Lean option/limit change. Both fresh whole-source
raw captures, statuses, SHA-bound tables and strict UTF8 declaration slices are preserved.
Only disjoint outer command plus associated async proof/addDecl/linter rows are summed;
nested macro/kernel duplication is excluded. All51 actual declaration anchors map once.
No diagnostic candidate timing is represented as production timing, and no third
same-source sample is selected.

| Fresh run | Declaration | Conservative ms | Actual proof anchors |
|---|---|---|---|
| final-first | theta_prefix_lt_aux | 866.724 | 1 |
| final-first | theta_phi_lt_aux | 516.827 | 1 |
| final-first | Θ_lt | 314.428 | 1 |
| final-repeat | theta_prefix_lt_aux | 774.687 | 1 |
| final-repeat | theta_phi_lt_aux | 598.56 | 1 |
| final-repeat | Θ_lt | 276.513 | 1 |

The inherited unrelated actual whole-source failures in sum_max_sub_le_index_det,
index_separated_mul_le_aux,index_det_le,index_numeric_bound_aux,index_le_lem6,
lem7_Φ_bound,lem7_numeric and the earlier positive-quadratic helper remain a mandatory
later final-repair queue outside this scope. The previous phi988.865/1013.946 pair remains
historical failed evidence, superseded only by its fresh audit disposition and current
measurements, not erased. MainLemma actual caller timing remains unmeasured after its
old180s capture stopped before main_lemma; successful semantic/build/native checks do not
invent a finite timing. Do not infer whole-file performance PASS from this helper pass.

## Simplify, refactoring, buzz, and all11 workflow steps

Simplify: direct holistic pass completed; no separate built-in simplify callable is
available in this session. The supported hypothesis localization and single-use certificate
inlining are the resulting improvements; terminal squeezing is retained after its
measured regression. No additional duplication/helper extraction
is recommended. Phase5a: scoped localization applied and exact old adapter checked;
no further refactoring. Phase5b: empty rename requirement; no shared queue writes.
Buzz: scoped target/direct-consumer/public-result timings pass the fresh pair above.
No limit raise, no fallback native_decide, no shipped profiling scaffolding.
Whole-file buzz and full-project/LeanEval gates remain coordinator-owned and pending.

| Step | Result |
|---|---|
| 1 | ✓ — Reference documents read. |
| 2 | ✓ — All24 concrete audit dispositions. |
| 2.5 | ✓ — Five actual methods; corrected exact-current-prefix anonymous routes and separate exit0 actual-environment target-absence check. |
| 2.6 | ✓ — All18 FIRST/current drop probes; scalar/strict/point-local candidates; private literature exemption and inversion. |
| 2.7 | ✓ — Every signature line measured and justified. |
| 2.8 | ✓ — Every inequality occurrence scanned. |
| 3 | ✓ — All42 golfing rules considered with concrete outcomes. |
| 4 | ✓ — Step-back and holistic reflection completed. |
| 5a | ✓ — Fresh complete unfiltered native diagnostics have0errors. |
| 5b | ✓ — Scoped diff/module/semantic/performance gates recorded. |
| 6a | ✓ — No rename needed; no shared queue mutation. |

## Freeze and handoff

Exact frozen hashes:

| Source | SHA256 |
|---|---|
| Roth/Theta.lean | 6bd95f9978e7d5c6f853eec3435d4921763aa1f4d192bf381c269ad6de6294ed |
| Roth/MainLemma.lean | ca9099ad6ef1cb7b26e5079f28560c37caa98813e5c213dc98df00711b5c18a4 |
| Roth/Main.lean | f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069 |

FIRST hashes unchanged. Exact baseline→final target proof delta30→28 lines; total
file line delta is recorded in line-counts.json (one extra signature line, two fewer
proof lines). No newly introduced external lemma identifier; all reused scalar names
are #checked in Positive.lean. New production helpers: none; deleted by this audit: none.
Inherited introduced/deleted obligations remain eleven, including deleted
fin-option and prefix-log; no original-count increment. Retained inventory remains51.
Source edit authority remains explicitly revoked. Corrected-search scratch/report authority
and the temporary compiler window are also released. All own compiler/native requests drained;
pending[]. Final artifact hashes and release state are `final-freeze.json` and
`final-process-drain.json`. The owner still must complete remaining dedicated audits,
cumulative29/all-actual/final profiles/full build and separate frozen LeanEval before
publishing original35. This report claims this scoped helper checkpoint only.
