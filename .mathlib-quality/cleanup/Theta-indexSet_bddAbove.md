# Dedicated original8 cleanup — `Roth.indexSet_bddAbove`

Scope: this public declaration only in `Roth/Theta.lean`, lines77–83. Its degree-map
simplification now uses `degreeOf` directly and places the short `by simpa` together,
reducing the live-start body from6 to5lines. The initial baseline original body had4lines
using wrappers that earlier dedicated leaves deleted; final is5, not a claimed original reduction. All effective public binders, names, visibility,
definitions, documentation, imports and callers are retained. No helper added.

## Preparation and baseline

Read the full leaf dispatch, lean4/mathlib-quality skills, cleanup workflow, golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and profiling;
consulted relevant style/naming sections. Read-only hold respected until explicit RELEASE.
Owner original7 published a4d22a3d162e1e93cd4a735c0eb66d16fb8e87b4 following full56.405s
then separate LeanEval13.129s, both exit0. Starting source SHA256 was exactly
c2f8c7c4cca1a062bdab7a85a97927ea0b77f55090985752a05ca7d22014f555.
Expressly reused prior complete `/private/tmp/roth-index-nonempty-final-lsp.json` as baseline:
success=true, partial=false, timed_out=false,0errors/27warnings. Existing target warnings
are unused-in-type DecidableEq and unused hr. Their public removal has not been approved.

## Full substantive24audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Existing unused-in-type DecidableEq/hr warnings retained; direct degreeOf adds one unusedSectionVars DecidableEq warning. All protected binders retained; no suppression.|
|2|HAVE SCAN|No have in original or selected proof.|
|3|SET_OPTION|No target option; no source limit raise. Bounded scratch automation lowers budget to2000.|
|4|SIMP SQUEEZE|One terminal simpa using hRd; unsqueezed maintained. Replace degreeOf_def with direct degreeOf unfolding.|
|5|NAMING|indexSet_bddAbove follows custom object's lowerCamelCase plus established BddAbove predicate; descriptive, no forbidden abbreviation/number pattern. No rename.|
|6|LINE PACKING|All2signature lines measured below, justified break.|
|7|BY PLACEMENT|Both outer by and inner by simpa end/start on their surrounding expression line.|
|8|FORMAT|Two-space tactic indentation; no internal empty line; inner simp continuation indented beyond its opener. No haveI/letI.|
|9|COMMENTS|No proof comment; existing source-bearing docstring preserved byte-for-byte.|
|10|DOCSTRING|Existing public explanation/reference protected, including original positivity wording.|
|11|VISIBILITY|Public API retained as instructed; changing visibility would need approval.|
|12|STRUCTURE|5body lines; no conjunction in conclusion; no >10line branch. Correlated R/h witness destructured together. No helper justified.|
|13|MATHLIB|Five actual methods below; generic boundedness API partial match; custom index bound uses project index_le_card directly.|
|14|JUNK DEF|n/a, theorem.|
|15|EXISTS LEMMA|n/a, public multi-use theorem, not private single-use witness wrapper.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective binder actually probed; successful DecEq/hr removals retained as unapplied public candidates.|
|19|INEQUALITY|Only0<rj in signature, already canonical; no reversed relation.|
|20|NORMAL FORM|BddAbove is canonical interface consumed by le_csSup and csSup_le_csSup.|
|21|SYNTAX GENERALITY|Current B/q/hr calling convention directly serves both callers; no approval to alter it.|
|22|IMPORT FANOUT|n/a, no import added.|
|23|CASTS|No explicit coercion/ascription introduced; Fintype.card coerces to ℝ by expected bound type. Existing Int.castRingHom ℝ fixes coefficient map's codomain.|
|24|INSTANCE-NAME|n/a, no instance declaration.|

## Signature packing and inequalities

Actual compiled width100 `#check @Roth.indexSet_bddAbove` is retained in original log.

|Sig line|Codepoints|Next signature token|Arithmetic|Action|
|---|---:|---|---|---|
|77|79|`BddAbove (indexSet B q r) := by` (31chars)|79+1+31=111>100|ok|
|78|35|none, proof body next|n/a|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hr|`0 < r j`|none, canonical|none|
|2|whole signature|zero ≥/> relations; arrows are not relations|n/a|none|

## Five actual mathlib search methods

Raw native results `/private/tmp/roth-index-bdd-search.json`.

|Method|Actual query/result|
|---|---|
|A Lean-Finder|`bounded above set of polynomial indices by number of variables degree bound`: Chevalley degBound/numBound and MvPolynomial.exists_degree_lt; no exact custom-index result returned.|
|B Loogle|`BddAbove, Set.range`: BddAbove.range_comp_right and bbdAbove_range_* sup lemmas; generic partial API.|
|C LeanSearch|`set bounded above if every element is at most a fixed bound`: BddAbove, bddAbove_def, upperBounds, csSup_le_iff', bddAbove_iff_subset_Iic.|
|D source rg|Untruncated scoped indexSet_bddAbove/bddAbove_def/bddAbove_iff_subset_Iic/degrees_map_of_injective searches; Bounds/Basic.lean42 and Degrees.lean196 inspected. DegreeOf_eq_sup/support_map route also inspected.|
|E local name pattern|`bddAbove_def`, limit8: actual source hit Bounds/Basic.lean, index=unavailable; no false absence conclusion.|

Auxiliary variants: range_comp_right, bbdAbove_range_sup, bddAbove_iff_subset_Iic,
upperBounds, degreeOf_eq_sup, degrees_map_of_injective, map_ne_zero_iff, map_injective.
Common-equivalents table: generic boundedness is relevant, but no direct custom Roth index
result. Conclusion: partial match; keep domain-specific packaging with direct Mathlib
map facts and project index_le_card. Earlier private map wrappers stay deleted.
No new helper or claim of exhaustive mathematical absence.

Actual no-Theta-import prefix automation probes try grind[indexSet,RSet,index_le_card],
aesop, exact?, apply?. Grind fails after reasoning about membership; aesop makes no progress;
exact?/apply? exhaust lowered2000heartbeats and remain inconclusive. Known repeated native
full-Theta multi_attempt stalls on preceding leaves were respected: no such request launched.
Initial expected-failure automation batch accidentally lacked section instances; corrected
and rerun before interpreting its results. No failed probe certifies axioms or absence.

## Every effective binder: compiled generalisation probes

Positive `/private/tmp/roth-index-bdd-positive.lean` exit0; negatives/automation
`/private/tmp/roth-index-bdd-negative.lean` expected exit1, raw logs alongside.

|Binder|Class/use|Actual drop/weakening evidence|Decision|
|---|---|---|---|
|σ:Type*|Type variable for polynomials/q/r|Literal drop with autoImplicit=false fails unknownσ; positives compile universe-polymorphically.|Already polymorphic, preserve.|
|Fintypeσ|Instance needed by indexSet/index and cardinal bound|Literal drop fails synthInstance Fintypeσ; Finiteσ plus explicit Fintype.ofFinite in conclusion/proof compiles.|Same conclusion needs a Fintype; reconstructed form changes interpretation/signature, preserve.|
|DecidableEqσ|Section instance unnecessary to selected proof|Independent dropDecEq with local classical compiles and standard axioms.|Candidate UNAPPLIED; no menu approval.|
|B:ℝ|Coefficient bound in indexSet|Literal drop fails unknownB; positive arbitraryB including negative/zero compiles.|Dependent value, preserve. Abstract coefficient ring would change RSet/indexSet definitions.|
|q:σ→ℕ|Denominator data in indexSet|Literal drop fails unknownq; positives arbitraryq, no positivity assumption.|Dependent value, preserve.|
|r:σ→ℕ|Degree and index weights|Literal drop fails unknownr; positives arbitraryr including zero.|Dependent value, preserve.|
|hr:∀j,0<rj|Proposition unused by cardinal bound|Positive dropDecEq simultaneously omits hr; weakHr with∀j,0≤rj also compiles.|Candidate drop/weakening UNAPPLIED; retain exact effective public contract.|

Selected candidate proof and the no-DecEq/no-hr proof were actually independently compiled.
Initial attempt omitted the explicit coefficient-map codomain in degrees_map_of_injective;
Lean could not infer it. Corrected explicit `(f := Int.castRingHom ℝ)` and reran exit0;
only corrected successful artifact is axiom evidence. No typeclass-parent, point-local or
strict→weak catalogue candidate beyond those listed applies to the dependent value binders.

Inversion diagnostic fires: after unpacking indexSet/RSet, B and numerator coprimality
are unused; all points α and all nonzero degree-bounded real polynomials satisfy the
existing `Roth.index_le_card`. That is already the abstract theorem. Generic `abstractSet`
compiled with arbitrary s/M and its upper-bound proof is exactly the existing BddAbove
constructor/definition; extracting another wrapper would duplicate API. No restatement applied.

## Public literature

Read local clean.tex644–666: bounded degrees and nonzero polynomial give a nonzero Taylor
coefficient with exponents≤rj, hence weight≤m. Surrounding source assumes positive r/q and
B≥1, while this boundedness proof compiles without those extra conditions under the project's
zero-denominator convention. Existing theorem already places no conditions on B/q.
Actual web queries: `Roth theorem index polynomial at most number variables Taylor theorem
generalization` and `Formalizing Roth theorem Takloo Bighash Yin index across sets polynomials`.
Primary exposition hits include [Soundararajan's notes](https://math.stanford.edu/~ksound/TransNotes.pdf),
[Min Ru's notes](https://www.math.uh.edu/~minru/fields/roth.pdf), and
[Roth's ICM account](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf).
Results discuss degree/index bounds and Taylor expansion; no stronger same-interface bound
is inferred from broader Roth generalizations. Exact binder claims rest on local source and
compiled probes. ChatGPT math MCP unavailable: no exposed matching capability.
Public menu DecidableEq/hr candidates remain unapplied optional proposals, not blockers.

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|n/a, no wrapper.|
|1.2 by-rfl|n/a, no wrapper.|
|1.3 rw/exact|n/a, no rw chain.|
|1.4 simp/exact|Already terminal simpa using hRd; retained and compacted.|
|1.5 trailing rfl|n/a, none.|
|1.6 constructors|Already anonymous bound constructor.|
|1.7 apply/exact|Already direct index_le_card application.|
|1.8 by_contra|n/a, none.|
|1.9 eta|n/a, no eta-redex.|
|1.10 have|n/a, none.|
|1.11 apply/intro|n/a, no apply+intro chain; bound witness followed by membership destructuring.|
|1.12 show|n/a, none.|
|1.13 projections|n/a, already nested witness destructuring.|
|1.14 rw merge|n/a, none.|
|1.15 terminal simp|Terminal simpa stays unsqueezed.|
|1.16 nonterminal simp|n/a, none.|
|1.17 dot notation|Existing map_ne_zero_iff .2 retained; direct theorem application clearer than forced dot notation.|
|1.18 parens/<||Parenthesized proof is followed by point argument `_`; removing parentheses invalidates application grouping.|
|1.19 push_neg|n/a, none.|
|1.20 exists inline|Public multi-use boundedness theorem, no private existential wrapper.|
|2.1 grind|Actual bounded isolated whole-proof trial fails.|
|2.2 grind predecessors|n/a, no retained grind.|
|2.3 simpa|Retained selected degree-map simpa, now one fewer line.|
|2.4 fun_prop|n/a, no function regularity goal.|
|2.5 positivity|n/a, boundedness existential needs explicit upper bound.|
|2.6 gcongr|n/a, bound follows index_le_card with exact hypotheses; no monotonicity algebra.|
|2.7 lia/omega|n/a, no arithmetic subgoal beyond supplied degree bounds.|
|2.8 aesop|Actual isolated whole-proof trial fails no progress.|
|2.9 norm_num/cast|n/a, symbolic cardinal/degree bounds, no numeric/cast subgoal.|
|2.10 decide|n/a, arbitrary real boundedness, no finite decision goal.|
|2.11 field_simp/ring|n/a, no algebraic identity.|
|2.12 linear_combination|n/a, no ring terminator.|
|2.13 wlog|n/a, no symmetric branches.|
|2.14 calc|n/a, no calc.|
|2.15 <;>|n/a, two semantically different theorem arguments, no parallel identical goal solver.|
|3.1 erw|n/a, none.|
|3.2 continuity|n/a, none.|
|3.3 omega/lia|n/a, none.|
|3.4 rcases/rfl|Already rintro pattern substitutes index equality with rfl.|
|3.5 attributes|No new global automation attribute; requires public normal-form judgment.|
|3.6 simp_all|n/a, targeted terminal simpa needs only hRd.|
|3.7 options|No target limit present or added.|

Step-back: generic boundedness constructor plus pointwise index_le_card is the mathematical
proof. One-tactic attempts fail/inconclusive within explicit budget. A term-only proof would
embed the same long nested membership pattern in a lambda; no clarity/performance gain
established. No unnecessary have or helper. Simplify manual equivalent review (no callable
built-in simplify tool): ISSUES-FOUND-AND-FIXED, direct degreeOf simp and compact by placement.
No other edit made. File phases5a/5b have no applied refactoring/rename; no new helper audit due.

## Verification, profile and freeze

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0, log
`/private/tmp/roth-index-bdd-module.log` (Build completed successfully,2423jobs).
Two compact-layout attempts failed before the final continuation indentation was fixed;
they are not counted as passing gates. Initial original-proof invocation ran while the
module had no .olean after the failed build and failed import; successful rerun followed
the final fresh module build. No failure is laundered into a pass.

Independent `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-index-bdd-original.lean`
exited0; raw original log alongside. Copies original RSet/indexSet definitions and original
proof/wrappers from2b64544bf9f77a8ff957bf1bcaf693ac72217ff6 into Original8. No current target
invocation is used to prove original8. Def/value rfl checks plus direct Lean.getConstInfo
.type comparison after universe-parameter alignment confirm the actual exact original public
contract, including section Fintype/DecidableEq instances. Actual built Roth.indexSet_bddAbove
and independent Original8.indexSet_bddAbove each use exactly propext, Classical.choice,
Quot.sound. No new axiom/native_decide/sorry/source limit raise.

Fresh COMPLETE unfiltered native lean_diagnostic_messages on Roth/Theta.lean succeeded:
partial=false, timed_out=false, failed_dependencies=[],0errors/28warnings. Raw
`/private/tmp/roth-index-bdd-final-lsp.json`. Compared every severity/category/message
against baseline via multiset comparison, allowing the one-line source displacement:
27→28 warnings, exactly one added target unusedSectionVars DecidableEq warning and zero
removed. This exposes that direct degreeOf no longer consumes the protected section
instance. Existing unused-in-type DecidableEq and hr warnings persist. No warning suppressed;
public removal needs approval. Detailed comparison
`/private/tmp/roth-index-bdd-diagnostic-comparison.json`. Two routine callers index_le_Θ and
Θ_mono compile in actual module/live diagnostics; no caller edit or new identifier introduced.
Focused exact before→after diff `/private/tmp/roth-index-bdd-focused.diff` confirms only the
selected target proof changed. Full project and separate LeanEval remain owner checkpoint gates.

### Buzz — FAST-BOARD (exact-prefix only)

Both immutable prefixes preserve every exact preceding source/import/context, terminating
immediately after the target and appending end Roth. Actual sequential commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-index-bdd-{before,after}-prefix.lean`.
Both exit0, wall40.337s/41.951s. No other compiler/LSP/build overlapped either profile.

|Target|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|4.842ms|134.306ms|3.097ms|6.271ms|148.516ms|
|after|5.281ms|146.073ms|3.036ms|6.231ms|160.621ms|

Raw UTF8 `/private/tmp/roth-index-bdd-{before,after}-profile.log`, target outer command
anchor35494 in both logs; structured `/private/tmp/roth-index-bdd-profile-summary.json`.
Outer command plus associated outer async proof/addDecl/linters counted; nested Meta/tactic/
kernel nodes not double-counted. The initial parser expected docstring text on the command
line and found no anchor; corrected by locating theorem text then its preceding outer command.
No false timing reported from the failed parser. Difference is within ordinary profiling
variance; no speedup claimed. Both safely below750ms, no borderline repeat needed;
budget1000ms. Exact final-prefix/source identity verified. Whole-file performance remains
owner final requirement after known late index_le_lem6 default-heartbeat failure is cleaned.
This prefix pass does not claim whole-module profiling success. No source scaffolding;
limit raises removed0/added0; no target performance deferral.

### Eleven leaf gates

|Gate|Actual result/evidence|
|---|---|
|lake_build_file|PASS, actual lake build Roth.Theta exit0,2423jobs, module log.|
|definition_protected|PASS, no def/abbrev or external declaration edited.|
|theorem_statement_protected|PASS, exact signature/name/visibility/docstring retained; actual getConstInfo.type compared directly including instances.|
|structure_gate|PASS, live-start6→5body lines; original baseline4, final5 after previous wrapper deletions. No >10line branch/conjunction conclusion.|
|naming_gate|PASS, descriptive indexSet_bddAbove, no forbidden pattern.|
|line_packing_gate|PASS, complete2line codepoint table,79+1+31=111>100.|
|inequality_orientation_gate|PASS,0<rj canonical, zero reversed relation.|
|cumulative_no_unintended_breakage|PASS at leaf scope, both unchanged callers compile in module/live diagnostics; owner full/LeanEval pending.|
|independent_original_contract|PASS, copied nonself original proof and actual type/def/value checks exit0.|
|standard_axioms|PASS, actual built/original only propext/Classical.choice/Quot.sound.|
|buzz/no_scaffolding|PASS,160.621ms exact-prefix aggregate; no source limits/options; all leaf requests drained.|

Leaf gates pass with documented27→28warnings: one restored unused-section DecidableEq
warning, protected instance retained pending explicit public approval. No claim of warning-free
source. No new helper, rename, shared log, rename queue or Git mutation. Report is the only
repository sidecar written. Full project then separate LeanEval are owner-only checkpoint gates.

Source edits FROZEN and REVOKED. Final Roth/Theta.lean SHA256:
`b24e5eabe809940a7b4a510a6a1cc3e1f707851d87d0bf7cb352cb56a85348f1`.
No further source edits authorized to this leaf. All sessions/compiler/LSP/profile requests
completed; no orphan requests.

## Eleven-step phase checklist

1. ✓ Full required reference preparation; read-only hold honored.
2. ✓ Full substantive24audit.
3. ✓ Five actual searches, unavailable index and bounded failure limitations recorded.
4. ✓ Every effective binder compiled/probed; public literature and inversion checked.
5. ✓ Complete measured signature packing table.
6. ✓ Per-occurrence inequality table.
7. ✓ All42golf rules have concrete statuses.
8. ✓ Step-back and manual simplify equivalent review.
9. ✓ Fresh complete unfiltered final LSP0errors/28warnings, full baseline message comparison.
10. ✓ Eleven leaf gates, actual module/original/axioms/profile; owner full/LeanEval remain pending.
11. ✓ No rename; comments/doc preserved; no helper; freeze/revoke and drain.


## Owner frozen checkpoint gates

Leaf source authority revoked and all requests drained before owner gates. Source SHA256
`b24e5eabe809940a7b4a510a6a1cc3e1f707851d87d0bf7cb352cb56a85348f1` stayed unchanged through
sequential `lake build` (exit0,53.204s) THEN separate `lake build Roth.LeanEval` (exit0,18.410s).
Raw `/private/tmp/roth-theta-d08-{full,leaneval}.log`; structured hashes/outcomes/timing
`/private/tmp/roth-theta-d08-builds.json`. Exact-path staging, commit and successful cleanup-branch
push complete this checkpoint before the next original declaration edit. After publication:
Theta8/35 originals;overall189/264;9/14files complete. No new helper or public amendment;
whole-module final profiling remains pending.
