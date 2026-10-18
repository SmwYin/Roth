# Dedicated original12 cleanup — `Roth.Θ_le_of_forall_index_le`

Scope: this public domain theorem only. Preserve its three-line mathematical proof,
all nine actual original binders, source-bearing docstring, name and visibility.
Change the mathematical lambda arrow to `↦` and pack the conclusion onto its preceding
signature line. No caller, helper, import, definition, header, Git or shared-log changes.
Body3→3 lines; physical declaration7→6 lines.

## Preparation and baseline

Read the full leaf instructions, lean4/mathlib-quality skills and cleanup workflow;
full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns and cleanup-gates;
relevant style, naming and profiling sections. Remained read-only until owner RELEASE.
Original11 checkpoint: owner full build69.923s THEN separate LeanEval21.839s, both exit0;
committed/pushed81ceeab76d55cf73710d93ceee4b69294624f7bf. Starting Theta SHA256
`1db9c6a343176b8aa3c95568a5ffeeb51d7cc992c7191a0d4a7900061af6d6de`.
Same-source baseline doctor evidence reused from `/private/tmp/roth-theta-card-final-lsp.json`:
success=true,partial=false,timed_out=false,0errors33warnings. Owner final cumulative
full project THEN separate LeanEval builds remain pending and are not claimed here.

## Full substantive24audit

|#|Item|Finding/action|
|---|---|---|
|1|LINT|Original DecEq-in-type warning retained pending public decision; no suppression. Final complete diagnostics recorded below.|
|2|HAVE SCAN|No have in original/live-start/final target.|
|3|SET_OPTION|None in target; no source limit raised. Scratch automation uses lowered2000heartbeats.|
|4|SIMP SQUEEZE|No simp in selected proof.|
|5|NAMING|Θ_le_of_forall_index_le describes a supremum upper bound from all defining indices; no forbidden abbreviation or numeric scheme.|
|6|LINE PACKING|Measured every signature line; final conclusion merged, width92. Table below.|
|7|BY PLACEMENT|by remains at end of signature.|
|8|FORMAT|2-space tactics,4-space signature continuation, no internal blank line or haveI/letI; mathematical lambda uses ↦.|
|9|COMMENTS|Zero inline comments; source-bearing two-line docstring preserved byte-for-byte.|
|10|DOCSTRING|Existing public statement/source documentation retained, no rewrite.|
|11|VISIBILITY|Public domain API used by Θ_unique_le and Θ_option_le, retained.|
|12|STRUCTURE|Body3lines≤30; no conjunction conclusion or >10line branch; correlated R/h witnesses stay together.|
|13|MATHLIB|All5actual searches below identify csSup_le infrastructure. Public domain statement retained; no helper added.|
|14|JUNK DEF|n/a, theorem.|
|15|EXISTS LEMMA|n/a, public inequality, not private trivial existential.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All9effective original binders covered below; no public amendment applied. hB drop/nonnegative weakening disproved by compiled certificate.|
|19|INEQUALITY|hB1≤B, callback index≤c and conclusion Θ≤c canonical; scan below.|
|20|NORMAL FORM|Supremum bound is canonical csSup_le shape, callback exposes domain witnesses conveniently.|
|21|SYNTAX GENERALITY|Nonempty-set precondition compiles, but merely exposes csSup_le's existing precondition; retain domain hB API.|
|22|IMPORT FANOUT|n/a, no new imports.|
|23|CASTS|All original ℤ→ℝ and ℕ→ℝ coercions needed for rational evaluation. Int.castRingHom ℝ fixes mapped coefficient codomain; none introduced or removed.|
|24|INSTANCE-NAME|n/a, no instance declarations.|

## Packing and inequality tables

`#check @Roth.Θ_le_of_forall_index_le` at format.width100 and direct type/BinderInfo
inspection in `/private/tmp/roth-theta-forall-original.log`.

|Sig line|Codepoints|Next complete token/block|Arithmetic|Action|
|---|---:|---|---|---|
|112|74|hc binder first line69chars|74+1+69=144>100|ok|
|113|73|index callback expression ending c)66chars|73+1+66=140>100|ok|
|114|92|none, proof next|n/a|ok|

Original separate conclusion fit with its preceding line; final merged line92≤100.
Table counts Unicode codepoints, not UTF8 bytes; nested callback remains unbroken.

|#|Location|Occurrence|Action|Rename|
|---|---|---|---|---|
|1|hB|1≤B|already canonical|none|
|2|hc callback|index…≤c|already canonical|none|
|3|conclusion|ΘBqr≤c|already canonical|none|
|4|whole signature|zero ≥ or > relations; function →/lambda ↦ excluded|none|none|

## Five actual mathlib searches

Native raw search results: `/private/tmp/roth-theta-forall-search.json`.

|Method|Actual query and result|
|---|---|
|A Lean-Finder|“The supremum of a nonempty set is at most any upper bound”→exact csSup_le, ConditionallyCompleteLattice.csSup_le and csSup_le'.|
|B Loogle|`Set.Nonempty ?s → (∀ b ∈ ?s, b ≤ ?a) → sSup ?s ≤ ?a`→csSup_le and DirectedOn.csSup_le.|
|C LeanSearch|“supremum nonempty set less than upper bound”→ConditionallyCompleteLattice.csSup_le, Real.isLUB_sSup, csSup_le'.|
|D source rg|Untruncated csSup_le/csSup_le_iff searches, inspected Basic.lean195–235; Real.sSup_empty inspected in real-order source.|
|E local name|csSup_le limit8→csSup_le, csSup_le_iff, csSup_le', directed variants; index unavailable, valid source hits, no absence inference.|

Auxiliary variants: csSup_le_iff, csSup_le', csSup_le_csSup, Real.sSup_le, Real.sSup_empty.
Common equivalent: conditionally complete order supremum upper bound. Presence established;
no absence claim. Generic csSup_le handles the supremum; local callback destructs the
concrete indexSet witnesses. The protected public domain convenience theorem already
exists and remains; no private wrapper is created or retained.

## Every effective binder — compiled probes

Positive successful actual-import files are separate from expected-failure files.
`/private/tmp/roth-theta-forall-positive.lean` exits0 and its printed axioms are standard.
`/private/tmp/roth-theta-forall-negative.lean` uses autoImplicit=false for meaningful literal
drops, rather than silently restoring omitted data. Expected failures do not certify absence.

|Binder|Class/use|Mechanical compiled evidence|Decision|
|---|---|---|---|
|σ:Type*|Index type in RSet/index/Θ/functions|Literal drop errors unknownσ; positive independent proof works universe-polymorphically.|Already arbitrary-universe; retain.|
|Fintypeσ|Required by index and Θ definitions|Drop/Finite replacement fail Fintype synthesis in statement.|Retain; reconstructing Fintype in expressions is a restatement.|
|DecidableEqσ|Actual original section instance used by public indexSet_nonempty signature|dropDecEq compiles with local classical; first direct trial without classical failed synthesis.|Existing menu unapproved; retain actual instance.|
|B:ℝ|Coefficient bound|Literal drop unknownB; independent proof works arbitraryB satisfying hB.|Dependent data retained.|
|hB:1≤B|Supplies indexSet_nonempty|Literal drop fails original proof; 0≤B cannot imply 1≤B. Stronger evidence: zero_empty/negative_counterexample compile, refuting unrestricted/nonnegative versions.|Retain; cannot remove outright.|
|q:σ→ℕ|Evaluation denominators|Literal drop unknownq; independent proof arbitraryq without positivity/coprimality assumptions beyond callback.|Dependent data retained.|
|r:σ→ℕ|Degree/weight data|Literal drop unknownr; independent proof arbitraryr, no hr introduced.|Dependent data retained.|
|c:ℝ|Proposed upper bound|Literal drop unknownc; arbitraryc, including negativec, in independent proof.|Dependent bound retained; nonnegativity restriction would weaken theorem.|
|hc|Universal defining-index bound|Literal drop leaves no upper-bound proof; isolated drop_hc le_rfl leaves stuck Preorder metavariable (inconclusive alone); separate hc_needed certificate refutes a bound for every arbitraryc. The unchanged domain callback is used to construct a set-membership bound.|Retain domain callback; no unused claim.|

The hB certificate establishes `indexSet 0 q r = ∅` by showing every coefficient of
an alleged member is zero. Therefore all defining indices are ≤−1 vacuously, while
`Θ 0 q r = sSup ∅ = 0`, so the conclusion Θ≤−1 fails. It applies even when0≤B.
This is a mathematical certificate, not an inference from syntactic proof usage.

Compiled but UNAPPLIED: remove DecEq with local classical (existing menu); replace hB by
indexSet.Nonempty (scratch optional alternative only). The latter is the generic precondition
already provided by csSup_le, with no new useful domain case identified; retention recommended.
No new public companion or menu expansion requested. Every public actual binder remains.

## Literature and inversion

WebSearch actual queries: “least upper bound supremum nonempty set upper bound theorem
conditionally complete lattice”; “Takloo Bighash Yin Formalizing Roth theorem index supremum”.
Primary mathematical formulation: [Penn analysis notes](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html)
define a least upper bound as an upper bound below every other upper bound; the
nonempty bounded-above real set has such a supremum. Mathlib's own source confirms the
fully abstract conditional-completeness form in csSup_le. The search response returned
multiple sources; no exact Roth paper match was assumed. Local authoritative source
`.mathlib-quality/references/clean.tex`650–703 defines this same index supremum and states
“Taking the supremum proves the claim” at692, with the constant1 witnessing nonemptiness.
No ChatGPT math MCP was exposed in available tool metadata, recorded unavailable.

Inversion FIRES: Θ/indexSet disappear after selecting csSup_le and unpacking witnesses;
the abstract content is precisely existing csSup_le. No new abstract theorem is needed.
The public domain callback supports the two actual callers without rebuilding membership
proofs. No public restructuring or generic helper introduced.

## All42golf rules

|Rule|Concrete status|
|---|---|
|1.1 by exact|n/a, refine/rintro/exact proof rather than no-op wrapper.|
|1.2 by rfl|n/a, supremum inequality not reflexivity.|
|1.3 rwa|n/a, no rw.|
|1.4 simpa using|n/a, no simp-plus-exact chain.|
|1.5 trailing rfl|n/a, no simp/rfl tail.|
|1.6 anonymous constructor|n/a, no constructor chain.|
|1.7 apply/exact|n/a, refine establishes callback goal, not final apply/exact pair.|
|1.8 by_contra!|n/a, direct argument.|
|1.9 eta reduce|Lambda evaluates h/q; not an eta-redex. Canonical ↦ notation applied.|
|1.10 inline have|n/a, no have.|
|1.11 refine/fun|Already refine; rintro must destruct shared existential witnesses.|
|1.12 redundant show|n/a, no show.|
|1.13 obtain|n/a, no have/projection.|
|1.14 merge rw|n/a, no rw.|
|1.15 terminal simp|n/a, no simp.|
|1.16 nonterminal simp|n/a, no simp.|
|1.17 dot notation|csSup_le is an unbundled supremum theorem; no natural receiver.|
|1.18 <||Current applications have no removable trailing-parenthesis wrapper.|
|1.19 push Not|n/a, no push_neg.|
|1.20 existential inline|n/a, target not private existential helper.|
|2.1 grind|Actual bounded target-free native trial; result below.|
|2.2 delete before grind|n/a, selected proof has no grind.|
|2.3 simpa consolidation|No simplification stage; actual simp alternative trial below.|
|2.4 fun_prop|n/a, no function-property predicate.|
|2.5 positivity|n/a, general bound c may be negative; not positivity.|
|2.6 gcongr|Actual bounded trial below; supremum membership requires explicit bound.|
|2.7 lia/omega|n/a, no Nat/Int arithmetic goal.|
|2.8 aesop|Actual bounded target-free native trial below.|
|2.9 norm_num/cast|n/a, no closed arithmetic/cast goal in selected proof.|
|2.10 decide|n/a, arbitrary real supremum universal statement.|
|2.11 field_simp/ring|n/a, no equality/denominator algebra proof.|
|2.12 linear_combination|n/a, no ring-ending branch.|
|2.13 wlog|n/a, no symmetric cases.|
|2.14 term calc|n/a, no calc; reflected on direct term csSup_le callback.|
|2.15 <;>|n/a, one remaining callback goal.|
|3.1 erw→rw|n/a, no erw.|
|3.2 fun_prop legacy|n/a, no continuity/measurability.|
|3.3 omega→lia|n/a, no omega.|
|3.4 rfl substitution|Already rintro…rfl removes the correlated equality directly.|
|3.5 attributes|No canonical rewrite direction or automation need demonstrated; no global attribute.|
|3.6 simp_all|n/a, no simp_all only.|
|3.7 limits|No source limit present or raised.|

## Step-back and simplify review

Selected three-line proof says precisely: use nonemptiness, unpack a defining index,
apply hc to the same polynomial/point witnesses. A term proof would merely hide the
necessary pattern match in a lambda. Keeping this clear proof avoids automation search
and preserves correlated witnesses. Only notation/packing changes justified by style.
Built-in simplify invocation is unavailable in this host; direct scoped holistic review:
PASS-THROUGH, no duplicated local skeleton needing extraction, no new helpers or identifiers.

## Verification and performance

Actual bounded target-free automation: `/private/tmp/roth-theta-forall-trials.lean`
contains exact preceding source/imports/context, omits target and every later declaration,
and tests distinct named grind[Θ,indexSet], simp[Θ,indexSet], aesop, gcongr, exact?, apply?
declarations. Native `/private/tmp/roth-theta-forall-trials.json` completed with
timed_out=false: first four fail; exact?/apply? reach lowered2000heartbeats, inconclusive.
This is exploration evidence, not axiom certification or proof of absence. Known prior
full-Theta multi_attempt stalls were not retried. Native helper returned a complete result
and terminated before later compiler/profile runs; its shutdown event-loop warning did not
change the completed result. No source option or profiling scaffolding was introduced.

Successful post-module actual-import gate:
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-theta-forall-original.lean`
exited0, raw `/private/tmp/roth-theta-forall-original.log`. It reconstructs the baseline
commit2b64544bf9f77a8ff957bf1bcaf693ac72217ff6 target proof under independent name,
without invoking the target. It also independently proves selected proof, compares
getConstInfo.type directly by isDefEq and compares all outer BinderInfo, including both
implicit section instances. Exactly9actual binders in original order: implicitσ,
instanceFintypeσ,instanceDecEqσ,implicitB,explicithB,implicitq,implicitr,implicitc,explicithc.
Printed actual/independent/selected/hc_needed axioms are exactly
[propext,Classical.choice,Quot.sound]. Initial scratch pp.width option was corrected to
format.width before the successful rerun. Positive no-DecEq scratch initially needed local
classical for the protected indexSet_nonempty API; fixed before exit0 certification.
Negative scope for hB probes repaired before final expected-exit1 batch; final hB diagnostics
are Unknown hB and 0≤B versus1≤B mismatch, with positive counterexample stronger evidence.

Fresh native final COMPLETE UNFILTERED Theta diagnostics:
`lean_diagnostic_messages(file_path=/Users/ramin/LEAN/Roth/Roth/Theta.lean,timeout_s=60)`;
raw `/private/tmp/roth-theta-forall-final-lsp.json`:
success=true,partial=false,timed_out=false,0errors33warnings,failed_dependencies=[].
Warning count unchanged from baseline; existing public DecEq/header/other-declaration
warnings remain under owner scope. No warning suppressed.

Exact-before/final diff `/private/tmp/roth-theta-forall.diff` and machine assertions
`/private/tmp/roth-theta-forall-diff-check.json` prove that precisely the lambda/line packing
change occurred, every other source byte is untouched, zero comments removed and zero new
identifiers introduced. No additional hallucinated identifier check needed beyond no new
identifiers; csSup_le was independently found via search/source and compiled.
Both unchanged callers Θ_unique_le and Θ_option_le compile in the module gate.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|`/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,2423jobs; raw `/private/tmp/roth-theta-forall-module.log`.|
|definition_protected|pass|No definition edits; exact expected-diff assertion.|
|theorem_statement_protected|pass|Notation/packing only; actual original type/BinderInfo identity compiled after module build.|
|structure_gate|pass|Body3lines; zero long branch/conjunction conclusion.|
|naming_gate|pass|Descriptive public bound name; no forbidden patterns.|
|line_packing_gate|pass|Complete measured table above, final max92codepoints.|
|inequality_orientation_gate|pass|Zero reversed inequality relations.|
|axioms|pass|Actual built constant and independent proofs standard3axioms only.|
|live_LSP|pass|Fresh complete unfiltered0errors33warnings.|
|callers|pass|No caller edit; both target callers covered by module build.|
|owner cumulative full + separateLeanEval|deferred to owner|Must run sequentially after leaf source freeze; not claimed complete.|

Per-leaf gates pass with owner cumulative build gates explicitly pending.

### Buzz pass

FAST-BOARD. All compiler/LSP requests were drained before these two sequential exact
source-prefix commands (Lean4.34 syntax):
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-forall-before-prefix.lean`
and the identical command on `/private/tmp/roth-theta-forall-final-prefix.lean`.
Both exit0; walls41.165s/38.521s. Raw UTF8 logs:
`/private/tmp/roth-theta-forall-before-profile.log`,
`/private/tmp/roth-theta-forall-final-profile.log`.
Timing parser/raw component summary `/private/tmp/roth-theta-forall-profile-summary.json`.

|Target anchored at original112|Outercommand|Async proof|Async addDecl/kernel|Async linter|Total|
|---|---:|---:|---:|---:|---:|
|Before|12.423ms|7.117ms|1.930ms|4.963ms|26.433ms|
|Final|12.264ms|7.733ms|2.752ms|5.244ms|27.993ms|

The outercommand begins at the source docstring and explicitly prints the target theorem;
subsequent top-level async entries are associated proof, addDecl/kernel and linter before
next command. No nested kernel/tactic timings counted twice. Both totals are far below
750ms repeat threshold and1000ms budget; no performance change claimed for notation-only
edit. maxHeartbeats raises removed0,added0; no deferral. These are PREFIX-ONLY profiles:
they preserve all exact preceding source/imports/context, end after target and add namespace
closure. No whole-file profile pass is claimed; owner final whole-module sweep remains
mandatory after later slow-declaration cleanup. Ordinary whole-module build already passed.


## 11-step checklist

- [✓] Step1: full required references and relevant style/naming/profile read.
- [✓] Step2: substantive24item audit above.
- [✓] Step2.5: five actual search methods and auxiliary variants above.
- [✓] Step2.6: all9effective original binders, compiled probes, literature/inversion above.
- [✓] Step2.7: measured every signature line and packed conclusion.
- [✓] Step2.8: inequality occurrence table above.
- [✓] Step3: every42golf rule has explicit concrete status.
- [✓] Step4: step-back/simplify review above.
- [✓] Step5a: fresh complete unfiltered final LSP evidence below.
- [✓] Step5b: diff/type/BinderInfo/axiom/module/performance gates below.
- [✓] Step6a: no rename needed; no queue/shared-log mutation.

Source frozen; no further source edits authorized by this leaf. All tracked native,
compiler and profile requests completed before handoff. Report-only work now complete.
Final Theta SHA256 `7f8ddcf44c78dd1b8f505206609b350b66cc70e17aaca919d70c704bcc0584e7`.
Only repo changes: target notation/packing plus this dedicated report. No Git mutations,
new helpers, rename queue writes or shared logs. Owner final full→separateLeanEval pending.


## Owner frozen checkpoint gates

All leaf requests drained and source authority revoked before owner checks. Source SHA256
`7f8ddcf44c78dd1b8f505206609b350b66cc70e17aaca919d70c704bcc0584e7` stayed unchanged through
sequential `lake build` (exit0,89.886s) THEN separate `lake build Roth.LeanEval` (exit0,28.529s).
Raw `/private/tmp/roth-theta-d12-{full,leaneval}.log`; structured hashes/outcomes/timing
`/private/tmp/roth-theta-d12-builds.json`. Exact-path stage/commit and successful cleanup-branch
push precede next original declaration edit. After publication:Theta12/35 originals,
overall193/264,9/14files complete. No new warranted API proposal/helper; every pending menu
remains unapplied. Whole-module final profiling and late default-heartbeat repair remain pending.
