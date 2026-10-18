# Cleanup: `Roth.Θ_unique_le` (original 20)

Dedicated original declaration audit. Release: `4fd80e70d4da2022f1fd97875322e95f99549aa3`,
Theta SHA256 `f72be18abfb0dc5a92007ff55716548b9dd3dae4da799406e1902a49856521a7`.
Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`.
Evidence directory: `/private/tmp/roth-theta-unique/`.

This records the initial original20 leaf phase. The separate fresh helper audit subsequently
shortened the helper and adapted the headline; the final batch and owner gates appended below
supersede this phase’s source hash, line counts, diagnostics and timing for publication.

## Result and scope

The headline proof becomes a two-line term: bound every individual index, then take the supremum.
The substantial individual bound is extracted as the new private `index_unique_le_log_div`,
with a 26-line proof. It does not need the RSet degree bound or `1 ≤ B`; it takes nonvanishing,
coefficient bounds, coprimality and positive weight/denominator conditions directly. Its final
logarithm step uses positive division and log monotonicity instead of broad `nlinarith` over
polynomial context. The intermediate coefficient bound is localized to the leading coefficient.
The original public name, conclusion, domains, argument names/order/BinderInfo and all other
hypotheses are retained; the explicitly approved public `[DecidableEq σ]` binder is removed.

ONE new production helper requires a SEPARATE fresh dedicated audit before the owner's original20
checkpoint: `index_unique_le_log_div`, source lines 218–248 (keyword through final proof line).
This report does not substitute for that audit and does not count the helper as another original.
The owner requested its mathematical name `index_unique_le_log_div` before final gates.
No imports, definitions, global attributes, axioms, limits, shared logs, queues or Git mutations.

## Preparation and inherited baseline doctor

Read both complete Lean/mathlib-quality skills, the complete cleanup command, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and profiling references,
and relevant style/naming sections. Preparation was read-only until explicit RELEASE; no scratch
writes or Lean requests preceded release. Read the current target and immutable original proof.

Owner's matching released full `lake build` exited0 in 77.364s, then separate `Roth.LeanEval`
exited0 in 24.504s, all 17 hashes stable. Complete matching baseline LSP inherited from
`/private/tmp/roth-rootmult-bound/final-lsp.json`: success=true, partial=false, timed_out=false,
failed_dependencies=[], 0 errors/18 warnings. The target's unused DecidableEq warning is addressed.
Baseline performance is explicitly INHERITED, not fresh: 820.803/829.009ms including linter,
raw `/private/tmp/roth-rootmult-bound/final-profile.log` and `final-profile-repeat.log`; the
≥750ms measurement was already repeated uncontended on the exact release source.

## Full 24-item audit

| # | Item | Finding/action |
|---|---|---|
| 1 | Lint | Baseline target DecEq is unused; approved removal. Other module warnings remain outside this declaration. |
| 2 | Have scan | Old hq0: by arithmetic, replace direct Nat.zero_lt_of_lt. hlogq: single-use named lemma, retained inside helper as positivity evidence used by le_div_iff₀. hrpos: cast proof, retained. hR10: old by rewriting, simplified to injectivity term and used for pow bound. hcoef: old uniform bound, replace direct leading-coefficient proof. hpow: single-use no-by alias, inline into log monotonicity. hmapeq/hmult: genuine conversion proofs, retained. hlog: old by log-power rewrite, now direct monotonicity proof and one rw; final explicit division uses it. Headline has no have. |
| 3 | Options | No production options/raised limits. Exploration uses a lower 20k heartbeat budget only. |
| 4 | Simp | Original hmult terminal simp retained; direct coefficient conversion uses terminal simpa only with exact named conversion lemmas; later helper audit may unsqueeze if desired. Final simpa closes divisor rearrangement. No bare nonterminal simp. |
| 5 | Naming | Θ_unique_le describes the one-variable bound, no forbidden numeric/abbreviation pattern. New private helper describes index≤log/divisor. No existing declaration renamed; shared rename queue untouched. |
| 6 | Packing | All headline signature lines measured below; complete table, no pending repack. |
| 7 | By | Headline term proof needs no by; helper by at end of signature/have lines. |
| 8 | Format | Two-space proof indentation, no blank proof lines, semicolon chains, haveI or letI. Lambdas use ↦. |
| 9 | Comments | No original inline proof comments. All three original docstring/source lines preserved byte-for-byte. |
| 10 | Docstring | Existing public source-aware Lemma5 documentation retained without rewriting. Private helper has no docstring. |
| 11 | Visibility | Public headline remains public as required; implementation helper private. Classic dialect. |
| 12 | Structure | Headline 29→2 proof lines; helper26, no independent branch>10 or conjunction conclusion. Supremum's lambda body is one application. |
| 13 | Mathlib | Five actual methods, auxiliary variants and clean prefix exact?/apply? probes below. No direct complete replacement found. |
| 14 | Junk def | n/a: theorem, no new definition. |
| 15 | Exists | n/a: no trivial existential witness lemma. |
| 16 | Show/change | No show or change introduced. |
| 17 | Push-neg | None. |
| 18 | Generality | Every effective binder accounted for with compiled drop/weakening probes; approved DecEq removed, remaining public hypotheses retained. |
| 19 | Inequalities | hB/hq/hr/conclusion all smaller-side-left; table below. |
| 20 | Normal form | Retain established Θ supremum and rational-root multiplicity formulation; no new equivalence/simp normal form. |
| 21 | Syntax generality | Public API still immediately usable by Θ_lt callers. Individual index helper expresses the stronger bound without unused degree hypothesis. |
| 22 | Imports | No new imports; no added import fanout. |
| 23 | Casts | Removed redundant inner ℤ annotation from coefficient expressions. Remaining ℤ→ℝ, ℤ→ℚ, ℕ→ℝ/ℚ/ℤ casts are real domain bridges. ℝ ascriptions fix positivity targets; Polynomial ℤ fixes the unique equivalence result. Headline has no casts. |
| 24 | Instance names | No instance declarations or explicit synthetic instance names introduced. Anonymous instance renumbering accepted only for anonymous instImplicit names in metadata check. |

## Five actual mathlib searches

Raw native responses: `search-finder.json`, `search-loogle.json`, `search-leansearch.json`,
`search-local.json`. All returned isError=false.

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | Multiplicity of rational root of integer polynomial bounded by logarithm of leading coefficient denominator; map uniqueAlgEquiv polynomial | le_rootMultiplicity_map, rational-root/denominator-clearing building blocks; no direct Θ bound. |
| B Loogle | MvPolynomial.uniqueAlgEquiv, MvPolynomial.map | empty response; no claim of exhaustive absence. |
| C LeanSearch | rootMultiplicity rational root integer polynomial logarithm denominator bound | rootMultiplicity definition, pow_rootMultiplicity_dvd, rootMultiplicity_mul_X_sub_C_pow and X_sub_C_pow. |
| D full source rg | uniqueAlgEquiv/map combinations; log/pow/le combinations; full index_unique_le_log_aux, Θ_unique_le, rootMultiplicity/log patterns | No exact match; logb power comparison is a possible alternative but would add an import/conversion for no benefit. Read current Roots.eq_rootMultiplicity_map and Index.index_unique. |
| E native local names | uniqueAlgEquiv, div_le_div_of_nonneg_right, le_div_iff₀, Nat.zero_lt_of_lt | Real source matches. Index=unavailable; not an indexed absence certificate. le_div_iff₀ name is checked by actual compilation despite search normalization to le_div_iff. |

Auxiliary variants checked: multiplicity map/powers/linear factors, coeff_uniqueAlgEquiv, coefficient
map, rational-root denominator clearing, logarithm base/power/division. No common-equivalents bucket
applies. The existing project index_unique and pow_rootMultiplicity_le supply mathematical pieces;
no one-to-three-call mathlib wrapper replaces the target or the substantial conversion argument.
Keep the bound, use existing library lemmas directly, and extract the mathematical individual bound.

Clean anonymous automation examples use an exact released source prefix ending BEFORE the target,
so they cannot cite the target or previously failed named declarations. `automation.lean/.log`:
grind fails, aesop makes no progress, exact? cannot close; apply? produces unrelated partial order
suggestions and reaches the conservative 20k heartbeat bound. No successful suggestion was ignored.
The known consecutive full-Theta multi_attempt stalls in prior leaves were not repeated; bounded
ordinary compiler exploration is the authorized fallback. Failed search batches certify no axioms.

## Effective binder generalisation and inversion

`binders.lean/.log` runs named, independent deletion/weakening variants against the exact source
prefix and selected proof, with autoImplicit=false. Positive selected statement is checked separately
in `actual-original.lean`. Drop tests establish proof/statement dependence, not mathematical
impossibility of a different proof.

| Effective binder | Role | Compiled candidate/result | Decision |
|---|---|---|---|
| {σ : Type*} | variable type in q/r, Θ | drop in isolated `drop-sigma.lean`: unknown σ | retain universe-polymorphic type; no narrower universe restriction. |
| [Fintype σ] | Θ/indexSet's effective finite enumeration | omit: cannot omit referenced section variable | retain chosen public Fintype API. Finite would require selecting enumeration in statement and change its object presentation. |
| [DecidableEq σ] | not needed mathematically | drop: selected proof/module and actual type compile | approved removal applied. |
| [Unique σ] | one variable and default | drop: Inhabited/Unique synthesis failures | retain; Subsingleton alone lacks default, Inhabited alone lacks uniqueness. |
| {B : ℝ} | log bound and RSet coefficients | drop: unknown B/hB | retain real domain; logarithm makes plain ordered-field weakening unavailable. |
| hB : 1≤B | nonempty supremum | drop: unknown hB; 0≤B: argument mismatch at Θ_le_of_forall_index_le | retain. Nonnegative B<1 does not guarantee a nonzero integer polynomial; no unsupported weakening. |
| {q : σ→ℕ} | denominators, coprimality, log | drop: unknown q/hq | retain arbitrary natural denominator function. |
| hq : 1<q default | positive logarithm | drop: unknown hq; 1≤q: mismatch at individual bound | retain; q=1 makes logarithm zero and loses the multiplicity control. |
| {r : σ→ℕ} | positive normalization weight | drop: unknown r/hr | retain arbitrary natural weights. |
| hr : 0<r default | positive normalization | drop: unknown hr; 0≤r: mismatch at individual bound | retain as dispatched. Subsequent fresh helper audit verifies zero weight via Nat.cast_nonneg without a case split; the public positive-weight API is intentionally retained. No mathematical-necessity claim. |

Named-object inversion does fire at Θ: after applying Θ_le_of_forall_index_le, all substantive
work concerns an arbitrary individual integer polynomial and rational point. The extracted helper
captures exactly that stronger local statement, omitting RSet degree control and hB. The headline
is now the supremum corollary. No concrete distinguished polynomial/witness remains to abstract.

Public literature search: “Formalizing Roth Lemma5”, “Roth theorem index polynomial denominator
root multiplicity q log B”, Takloo-Bighash/Yin attribution and arXiv formalization variants.
The local primary source clean.tex 671–692 gives precisely the existing theorem: rational-root
multiplicity divided by r, primitive factorization, leading-coefficient bound, logarithms, supremum.
It supports the extraction and explicit division argument. Primary public [Roth lecture notes]
(https://www.math.uh.edu/~minru/fields/roth.pdf), pp2–4, give the same weighted-index and bounded
integer coefficient framework but do not provide a directly applicable stronger one-variable API.
Search returned unrelated additive-combinatorics Roth formalizations, which were not used.
AMS excerpt open failed; it is not evidence. Math second-opinion MCP is unavailable, not consulted.
No additional public API changes recommended.

## Signature packing and inequality orientation

Unicode codepoint widths include indentation. Actual #check at format.width100 is in the definitive
actual-constant log. Signature text remains unchanged apart from approved surrounding omit.

| Signature line | Before | Final | Addition arithmetic | Action |
|---|---:|---:|---|---|
| theorem through q/hq/r | 96 | 96 | 96+1+20 (next hr binder)=117>100 | ok |
| hr, conclusion, := | 90 with by | 87 | no next signature token | ok |

| Occurrence | Inequality | Action |
|---|---|---|
| hB | 1≤B | already correct |
| hq | 1<q default | already correct |
| hr | 0<r default | already correct |
| conclusion | Θ B q r≤log B/(r log q) | already correct |
| reversed ≥/> in code | 0 | no rewrite/rename |

## All 42 golfing rules

| Rule | Finding/action |
|---|---|
| 1.1 by exact | headline converted to composed term, no wrapper. |
| 1.2 by rfl | n/a: mathematical inequality. |
| 1.3 rw+exact | no remaining adjacent pair; hR10 now direct injectivity term. |
| 1.4 simp+exact | coefficient proof consolidated into simpa. |
| 1.5 trailing rfl | none. |
| 1.6 constructor | none; no conjunction conclusion. |
| 1.7 apply+exact | headline composed directly. |
| 1.8 contradiction | none. |
| 1.9 eta | bound lambda has multiple independent bound inputs, no eta-redex. |
| 1.10 single-use have | hpow inlined; hq0 replaced Nat.zero_lt_of_lt; explicit positivity/equality intermediates retained where they clarify types. |
| 1.11 apply+intro | supremum directly receives a lambda. |
| 1.12 show | none. |
| 1.13 projections | old obtain unpacking replaced direct hR.1/hR.2.2 at one short call. |
| 1.14 merge rw | retained conversion rw lists already combined; no separated consecutive rw. |
| 1.15 terminal simp | hmult terminal simp unsqueezed; coefficient simpa only deliberately focused on representation conversion. |
| 1.16 nonterminal simp | none bare. |
| 1.17 dot | .2 for standard iff adapters and hrpos.le retained. |
| 1.18 trailing parens | no cosmetic parentheses savings worth churn; small grouped positive-division expression. |
| 1.19 push Not | none. |
| 1.20 trivial exists | n/a: no existential helper. |
| 2.1 grind | actual clean-prefix anonymous trial fails. |
| 2.2 delete before grind | no selected grind. |
| 2.3 simpa | applied to coefficient transfer and final division rearrangement. |
| 2.4 fun_prop | n/a: no continuity/measurability goals. |
| 2.5 positivity | closes positive q-power prerequisite of log monotonicity. |
| 2.6 gcongr | explicit ordered division theorem is more focused; no monotone calc chain. |
| 2.7 lia/omega | remove omega and use Nat.zero_lt_of_lt directly; no integer search needed. |
| 2.8 aesop | actual anonymous whole-proof trial fails. |
| 2.9 norm_num/cast | exact_mod_cast handles q/r real positivity; no concrete numeric computation. |
| 2.10 decide | n/a: arbitrary real/log/poly inequality, not finite closed computation. |
| 2.11 field_simp/ring | algebraic denominator rearrangement closes by simp [div_div,mul_comm]; no polynomial ring goal. |
| 2.12 linear_combination | n/a: no ring/ring_nf endpoint or certificate needed. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 calc collapse | selected inequality is composed directly; no calc. |
| 2.15 repeated goals | no independent repeated goals to close with <;>. |
| 3.1 erw | none. |
| 3.2 continuity | none. |
| 3.3 omega→lia | stronger direct Nat lemma removes old omega entirely. |
| 3.4 rcases rfl | none. |
| 3.5 attributes | no broad simp/grind attribute warranted for explicit coefficient/coprimality premises. |
| 3.6 simp_all | none. |
| 3.7 limits | no production limits; none raised. |

## Step back and simplify

The mathematical argument is unchanged: integer rational-root factorization bounds the multiplicity
power by the coefficient height; logarithms divide by log q; normalize by r; take the supremum.
The extracted helper makes the mathematical separation explicit. Existing mathlib map/multiplicity
lemmas handle field transport directly. Generic automation fails to discover this entire chain;
retaining explicit transport and inequalities is clearer and faster than broad arithmetic search.
Built-in /simplify is unavailable; performed its scoped holistic review directly. Outcome:
ISSUES-FOUND-AND-FIXED (extraction, direct leading-coefficient bound and positive-division argument).
No unrelated refactoring, imports or cosmetic public renames. Shared rename queue untouched.

Final gates, actual old-contract/axiom evidence, profile totals and frozen hash are appended below
once their sequential tool requests finish. Owner full project build, separate LeanEval and the
new helper's distinct fresh audit remain pending at this leaf's handoff.


## Definitive verification gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Theta`, exit0, all2423 jobs, `module-final.log`; after final helper name. |
| Complete live LSP | pass | Fresh native lean_diagnostic_messages on entire live Theta, unfiltered; `final-lsp.json`: success=true, partial=false, timed_out=false, failed_dependencies=[], zero errors/16 existing warnings; no target/helper warnings. |
| Definitions/imports protected | pass | `change.diff`: no def/abbrev/import/global attribute changes. |
| Public theorem statement | pass, approved DecEq drop | Actual built constant has exact manually stated approved new AST (universe names normalized, only anonymous instImplicit names exempted); all retained original named metadata/order/BinderInfo checked. |
| Full old contract | pass | `actual-original.lean/.log`, exit0: independently recompiles original Index+Theta through Θ_unique_le, exact full old DecEq lambda adapter type and proof-irrelevance equality. Original10-binder telescope minus only binder2 (checked DecidableEq) definitionally equals actual9-binder telescope. |
| Independent old proof | pass | Both original Θ_unique_le and old uniform-coefficient pow_rootMultiplicity_le blocks byte-identical to immutable2b64544 (`immutable-check.json`). Old proof value checked not to cite current target. |
| Standard axioms | pass | Actual built public target, private helper, complete independent old target and adapter each use only [propext,Classical.choice,Quot.sound] in definitive successful log. |
| Structure | pass | Headline2 body lines≤15, private helper26≤30, no independent>10-line branch/conjunction output. |
| Naming | pass | Descriptive theorem/helper names; no existing public rename. |
| Packing | pass | Complete two-row measured headline table above. |
| Inequality orientation | pass | Complete occurrence table; zero reversed code inequalities. |
| Documentation/comments | pass | Original documentation byte-for-byte; zero inline narrative removed. |
| Caller coverage | pass | Full repository rg: only two Θ_lt proof calls, both inside Theta; module and complete LSP cover them. |
| Limits/scaffolding | pass | Focused diff has no sorry/axiom/native_decide/limits/profiling scaffolding/haveI/letI/TODO/FIXME/legacy lambda. |
| Owner full build + separate LeanEval | pending owner | Not run by this worker; previous checkpoint builds do not certify edited state. |
| New helper fresh dedicated audit | pending owner | ONE helper, index_unique_le_log_div at218–248, omit217; fresh distinct audit required before original20 checkpoint. |

The oldDecEq adapter is a full typed lambda/theorem with old `{σ}[Fintype][DecEq][Unique]` context,
not a visible-header comparison. The exact original source namespace includes its own uniform
pow bound, not the new localized root API. It does not prove the old theorem by invoking itself.
Helper's actual private constant was discovered programmatically:
`_private.Roth.Theta.0.Roth.index_unique_le_log_div`.

Scratch corrections (not accepted evidence): initial helper scratch attempted `rw [R1]` on a local
let and was corrected to `dsimp only [R1]` before coefficient extensionality. Initial metadata
verifier used Array.eraseIdx requiring an index proof; replaced with List.eraseIdx then toArray.
The next metadata run exposed differently named universe parameters; definitive checks normalize
both level-param lists before comparison. Only final exit0 `actual-original.log` certifies types
and axioms. Failed runs were not counted as successful gates.

New identifier verification: `Nat.zero_lt_of_lt` and `div_le_div_of_nonneg_right` found by actual
native name search; `le_div_iff₀` is search-normalized to le_div_iff, and its actual exact name
is elaborated successfully by helper scratch, final module build and the actual-constant probe.
`Polynomial.leadingCoeff` and all map/rootMultiplicity/log lemmas already occur in the released
proof or preceding declarations. No unresolved guessed identifier.

## Required phase checklist

- [✓] Step1: full required references read.
- [✓] Step2: full substantive24-item audit.
- [✓] Step2.5: five actual search methods, auxiliary variants and clean compiled search probes.
- [✓] Step2.6: every effective binder deletion/appropriate weakening probed; public literature/inversion recorded.
- [✓] Step2.7: complete measured signature packing table.
- [✓] Step2.8: complete inequality occurrence table.
- [✓] Step3: all42 golfing rules recorded.
- [✓] Step4: strategy reflection and scoped holistic simplify review.
- [✓] Step5a: fresh complete unfiltered final LSP.
- [✓] Step5b: module, actual original/new types, axioms, protection and content gates.
- [✓] Step6a: no existing rename needed; shared sidecars untouched.

## Buzz: final exact-prefix timing

Outcome: FAST-BOARD. Fresh final accepted run after all module, isolated compiler and native LSP
requests drained. No concurrent compiler/LSP request. Command exited0:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-unique/final-prefix.lean`

The prefix preserves the exact final source/imports/section context through Θ_unique_le and adds
only closing section/namespace commands. This is prefix-only performance evidence; it does not
certify the whole-module profile, which the owner must eventually sweep after slow later proofs.
Raw UTF8 log `final-profile.log`; parser `parse_profile.py`; machine totals `timings.json`.
Sum outermost command plus associated asynchronous proof/kernel-addDecl/linter roots, excluding
all nested duplicate command/tactic timings. Because `omit … in` wraps commands, use its OUTER
root (not the nested theorem or lemma root). No compiler root is emitted for these propositions.

| Declaration/run | Outer ms | Proof ms | Kernel async ms | Linter ms | Total ms | Raw anchor lines |
|---|---:|---:|---:|---:|---:|---|
| baseline inherited Θ_unique_le | 29.535 | 738.667 | 26.926 | 25.675 | 820.803 | prior final-profile.log304857/306310/467204/467206 |
| baseline inherited repeat Θ_unique_le | 29.598 | 725.683 | 31.489 | 42.239 | 829.009 | prior final-profile-repeat.log304923/306376/467241/467243 |
| final index_unique_le_log_div | 66.297 | 353.251 | 17.236 | 17.229 | 454.013 | final-profile.log308686/308766/417074/417076 |
| final Θ_unique_le | 18.867 | 17.906 | 0.878 | 5.442 | 43.093 | final-profile.log418624/418637/419430/419432 |

Fresh final declarations are below750ms, so no final repeat threshold triggers. The inherited
≥750ms baseline was repeated uncontended. Combined helper+headline cost is497.106ms; this
comparison is indicative, with ordinary wall-clock variance, and every individual declaration
is below1000ms. No over-budget deferral, no limit changes or remaining profiling scaffolding.

## Freeze and terminal handoff

Source edits revoked; no compiler/native/profile requests remain running. Final Theta SHA256:
`56a5db29f3c368733fc4adb065ceb265586d0b2ecb80b6d7116bde24c771ce58`.
Source974→981 lines (+7); headline proof29→2 (−27), one new helper proof26.
Only scoped Theta source, this dedicated report and scratch evidence were written.
Owner must now dispatch ONE separate fresh dedicated audit for `index_unique_le_log_div`
(declaration218–248; omit217), then perform the frozen full `lake build`, separate
`lake build Roth.LeanEval`, exact compatibility/axiom/cumulative gates and publication.
This leaf is not an additional original declaration and original20 checkpoint is not yet counted.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (39.883 s),
then separate `lake build Roth.LeanEval` (15.025 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa`.
Raw logs: `/private/tmp/roth-theta-d20-full.log`, `/private/tmp/roth-theta-d20-leaneval.log`; machine record
`/private/tmp/roth-theta-d20-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 20/35, overall 201/264 original
declarations, 9/14 completed files. One new private helper independently audited and retained; helper audits do not increase original counts.


## Final original20 publication batch after fresh helper audit

The separate [fresh helper audit](Theta-index_unique_le_log_div-helper.md) is complete.
It removed the PRIVATE positive-weight premise, localized the helper premise to the equivalent
univariate leading coefficient and inlined two aliases. Final helper body23, headline body3,
source979lines. Public hB/hr/Fintype and all other original public parameters remain; only the
approved DecidableEq σ binder is removed. Public hr is intentionally unused under this audit’s
preserved public-API scope; no separate zero-weight case is needed mathematically.

Final source SHA256 `b9cd75fb1bf852d76868e8c6abc53ad4898664e13b1ec6701c1b40a144f538fa` supersedes the initial leaf
SHA56a5db29 for publication. The helper worker reran the actual module, exact INITIAL-helper
independent proof/full initial adapter/actual selected type metadata/axioms, and the complete
immutable-original public20 proof/full old-DecEq adapter/exact selected public AST/retained
metadata/actual standard axioms after all private changes. All exit0. Final complete native
unfiltered LSP:0errors17warnings, success=true,partial=false,timed_out=false,faileddeps[].
Only new warning is the intentionally retained public hr. Final same-source shared prefix
profiles after all normal requests drained: helper481.521ms/public73.124ms, combined554.645ms;
both below750/1000, no repeat trigger. Raw artifacts and precise anchors are in the helper audit.
No whole-Theta performance pass is claimed. This final batch evidence supersedes the initial
phase’s line counts, diagnostics, timing and hash. Owner cumulative gates above use this same
final SHA. ONE fresh new-helper audit is complete; no original-count inflation.
