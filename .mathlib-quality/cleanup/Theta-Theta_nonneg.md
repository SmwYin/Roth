# Dedicated original10 cleanup — `Roth.Θ_nonneg`

Scope: only this public theorem. Replace the bounded-supremum/constant-polynomial argument
with the existing `Real.sSup_nonneg`, directly unpacking an arbitrary index and applying
`index_nonneg`. Every original public binder, hypothesis, instance, name, visibility and
source-bearing docstring is protected. No helper/caller/import/definition change. No Git,
shared log, rename queue or header mutation. Declaration4→5lines (proof2→3lines); the extra
line expresses the canonical order-theoretic argument without boundedness bookkeeping.

## Preparation and baseline

Read full leaf instructions, lean4/mathlib-quality skills and cleanup workflow, full
five mandatory search/golf/generalisation/gates references, relevant style/naming/profiling.
Read-only preparation until owner RELEASE. Original9 owner checkpoint: full build6.508s THEN
separate LeanEval3.153s, both0, committed/pushed132df630f7f677ae8afb08c57645ff7a3071d06b.
Starting Theta SHA256 a66d8859819b240cb588a5b33b0e064bc0b25226a6b63ee19cba2946dde1adb0.
Identical-source baseline full native diagnostics reused from preceding
Theta-index_le_Theta report: success=true,partial=false,timed_out=false,0errors28warnings.
Full project/separateLeanEval gates remain owner responsibilities and are not claimed here.

## Full substantive24audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Original effective DecidableEq is unused in type. Preserve it and all hypotheses; canonical proof exposes hB/hr unused warnings, no suppression. Final complete diagnostics evidence below.|
|2|HAVE SCAN|No have in either original or selected proof; no intermediate to inline.|
|3|SET_OPTION|No target option or source limit increase. Scratch automation only lowers heartbeat budget to2000.|
|4|SIMP SQUEEZE|No simp in selected proof. Isolated simp trial leaves supremum inequality unsolved.|
|5|NAMING|Θ_nonneg describes nonnegativity of the established Θ object. No forbidden abbreviations, numeric scheme or rename.|
|6|LINE PACKING|Every signature line measured below; full conclusion plus by would overflow first line.|
|7|BY PLACEMENT|by ends conclusion line; no standalone by.|
|8|FORMAT|2-space tactic indentation,4-space continuation, no internal blank lines, no haveI/letI.|
|9|COMMENTS|No proof comments originally; original2-line source-bearing docstring preserved verbatim.|
|10|DOCSTRING|Public claim/source remains correct with retained original hB/hr. No unauthorized documentation rewrite.|
|11|VISIBILITY|Public main result in module docstring, retained. Generic API is used directly in proof; deleting public convenience theorem requires fresh decision.|
|12|STRUCTURE|Headline theorem body3lines≤15; no conjunction conclusion or >10line branch. Correlated R/h witnesses unpacked together.|
|13|MATHLIB|All5actual searches find Real.sSup_nonneg. Use directly, no new wrapper/helper.|
|14|JUNK DEF|n/a, theorem.|
|15|EXISTS LEMMA|n/a, public inequality, not private trivial witness declaration.|
|16|SHOW/CHANGE|None in selected proof.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All8effective parameters audited with compiled drop/weakening probes below; no API amendment applied.|
|19|INEQUALITY|hB1≤B, hr0<rj and conclusion0≤Θ already canonical. No reversed relation.|
|20|NORMAL FORM|Nonnegativity as0≤Θ is canonical; Real.sSup_nonneg abstracts the proof. No automation attribute changed.|
|21|SYNTAX GENERALITY|Stronger no-hB/no-hr/no-DecEq candidate and actual-type adapter prepared, unapplied pending fresh decision.|
|22|IMPORT FANOUT|n/a, no new import.|
|23|CASTS|No introduced casts or explicit type ascriptions. All original coercions live inside underlying definitions, untouched.|
|24|INSTANCE-NAME|n/a, no instance declaration.|

## Measured signature packing and inequality scan

Actual width100 #check and actual getConstInfo.type evidence is in original probe log.
It includes exactly σ/Fintypeσ/DecidableEqσ/B/hB/q/r/hr in the original binder order.

|Sig line|Codepoints|Next complete token|Arithmetic|Action|
|---|---:|---|---|---|
|95|83|`0 ≤ Θ B q r := by`17chars|83+1+17=101>100|ok|
|96|21|none, proof next|n/a|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none, canonical|none|
|2|hr|0<rj|none, canonical|none|
|3|conclusion|0≤ΘBqr|none, canonical|none|
|4|whole signature|zero ≥ or > relations; arrows are function syntax|n/a|none|

## Five actual mathlib searches

Raw native results: `/private/tmp/roth-theta-nonneg-search.json`.

|Method|Actual query/result|
|---|---|
|A Lean-Finder|supremum of a set of nonnegative real numbers is nonnegative → Real.sSup_nonneg, Real.iSup_nonneg, primed variants, NNReal.coe_iSup.|
|B Loogle|`(∀ x ∈ ?s, 0 ≤ x) → 0 ≤ sSup ?s` → exact Real.sSup_nonneg.|
|C LeanSearch|supremum nonnegative real set every member nonnegative even empty → Real.sSup_nonneg, Real.sSup_empty, Real.sSup_nonpos.|
|D source rg|Untruncated sSup_nonneg/csSup_nonneg over all Mathlib; inspected Algebra/Order/Archimedean/Real/Basic.lean258–298.|
|E local name|sSup_nonneg limit10 → Real.sSup_nonneg and primed variant; index unavailable, source hits valid, no absence inference.|

Auxiliary variants: sSup_nonneg', iSup_nonneg, iSup_nonneg', sSup_empty,
sSup_of_not_bddAbove, le_csSup_of_le. Common equivalents: supremum/order bucket.
Presence proved, no mathematical absence claim. Existing generic theorem used directly;
public domain theorem retained under explicit API protection. No extracted missing API.
Known repeated full-Theta multi_attempt stalls on prior leaves: no repeat; bounded isolated
original-target-free automation batch used. Grind[Θ,indexSet], simp[Θ], aesop and positivity
fail; exact?/apply? hit lowered2000heartbeats, inconclusive. Failed expected batch is not
axiom/absence evidence. Native final diagnostics still required separately.

## Every effective binder: compiled probes

Positive prefix `/private/tmp/roth-theta-nonneg-positive.lean` exit0 and standard axioms;
definitive actual-import candidate/adapter/type probes in original artifact below.
Negative `/private/tmp/roth-theta-nonneg-negative.lean` expected exit1. No failed file certifies
axioms. Candidate success files include no admitted proof.

|Binder|Class/use|Compiled drop/weakening evidence|Decision|
|---|---|---|---|
|σ:Type*|Index type in functions and Θ|Literal removal with autoImplicit=false errors unknownσ in isolated namespace; selected/candidate proofs work at arbitrary universe.|Already universe-polymorphic; retain.|
|Fintypeσ|Instance underlying index/Θ definitions|Drop fails synthInstanceFintypeσ. Finiteσ candidate reconstructs Fintype.ofFinite in conclusion/proof, exit0.|Reconstruction restates signature; unapplied.|
|DecidableEqσ|Effective original section instance|No-DecEq candidate compiles independently and AST verifies absence. Original-style proof with local classical also compiles.|Existing optional menu unapproved; retain actual binder.|
|B:ℝ|Coefficient bound inside Θ|Literal drop errors unknownB. Canonical candidate accepts arbitraryB, including B<1.|Dependent data, retain; abstract codomain would restate definitions.|
|hB:1≤B|Original constant-polynomial witness|Original proof drop errors unknownhB. Canonical drop_hB/weak_hB0≤B and simultaneous unrestricted candidate compile.|Genuine stronger theorem discovered, unapplied.|
|q:σ→ℕ|Denominator data inside Θ|Literal drop errors unknownq; canonical proof accepts arbitraryq without positive-denominator assumption.|Dependent data, retain.|
|r:σ→ℕ|Degree/weight data inside Θ|Literal drop errors unknownr; canonical proof accepts arbitraryr.|Dependent data, retain.|
|hr:∀j,0<rj|Original boundedness argument|Original drop errors unknownhr. Canonical drop_hr/weak_hr0≤rj and simultaneous unrestricted candidate compile.|Genuine stronger theorem discovered, unapplied.|

No omitted algebraic parent, point-localisation, strict→weak or universe candidate applies:
remaining parameters are dependent data for fixed project definitions. Finiteness weakening
is a restatement; proposition drops/weakening and DecEq elimination are compiled, report-only.

## Public literature and inversion

Local clean.tex644–669 defines Θ for positive r/q and B≥1; its nonnegativity argument admits
the constant1 polynomial. The canonical mathlib theorem instead exploits every index's
nonnegativity and its totalized real supremum (zero for empty/unbounded sets).
Actual WebSearch queries: `supremum set nonnegative real numbers empty unbounded supremum Lean mathlib`
and `Roth theorem index polynomial Theta supremum nonnegative`. First query top3 hits:
mathlib real.Sup_def documentation, mathlib3 source, and mathlib set basic source. Second
query returns Princeton diophantine notes and Min Ru Roth notes among the Roth-specific
results, plus unrelated search noise; no generality inference from snippets.
Primary [mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html)
was opened and confirms totalization. Primary [Princeton notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf)
and [Min Ru notes](https://www.math.uh.edu/~minru/fields/roth.pdf) were opened for index context.
No claim that classical real least-upper-bound theory assigns a supremum to the empty set.
ChatGPT math MCP unavailable: no matching exposed tool.

Inversion fires: Θ disappears immediately through Real.sSup_nonneg; the abstract content is
∀s:Setℝ,(∀x∈s,0≤x)→0≤sSup s, exactly existing Real.sSup_nonneg. Its concrete membership
callback is index_nonneg. No new abstraction/helper is warranted. This does substantiate
the report-only hB/hr/DecEq removals but does not silently expand the approved menu.

## Concrete stronger candidate — UNAPPLIED

Definitive actual-import `/private/tmp/roth-theta-nonneg-original.lean` imports Roth.Theta;
`Stronger10.candidate` is:

```lean
theorem candidate {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} : 0 ≤ Θ B q r := by
  apply Real.sSup_nonneg
  rintro _ ⟨R, _, h, _, rfl⟩
  exact index_nonneg _ _ _
```

Compiled AST verifies exactly5binders σ/Fintype/B/q/r, no hB/hr/DecEq. B/r stay implicit,
q stays explicit; no data binder reorder. `Stronger10.adapter` is a full original-type
explicit lambda accepting σ/Fintype/DecEq/B/hB/q/r/hr and invoking candidate q. Kernel
checks `@adapter = @Roth.Θ_nonneg` by rfl. Direct actual getConstInfo.type alpha-aligns
universe parameters and verifies adapter type plus binderInfo/order against actual old
Roth.Θ_nonneg. Candidate/adapter/caller_named/caller_inferred all print standard3axioms only.
This imports actual definitions; earlier prefix candidate is only additional independent
proof evidence, not substituted for actual-import compatibility.

Inventory `rg -n Θ_nonneg Roth`: four actual calls, two each inside index_le_lem6 and Θ_lt,
plus module-doc mention; zero external uses. No caller edited. Actual lem6Φ prospective
replacement `add_nonneg (candidate (B := M) _) (candidate (B := M) _)` and fully inferred
`add_nonneg (candidate _) (candidate _)` both compile with actual project definitions.
Fresh root/user decision required before removing any protected hypothesis/instance;
this discovery was sent to owner as a concrete candidate, not silently applied/menu-expanded.

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|No wrapper; selected proof has substantive tactics.|
|1.2 by-rfl|No by-rfl.|
|1.3 rw/exact|No rw.|
|1.4 simp/exact|No such chain.|
|1.5 trailing rfl|No trailing tactic; membership rfl pattern substitutes actual equality.|
|1.6 constructors|No constructor tactics; correlated witnesses unpacked together.|
|1.7 apply/exact|Apply creates quantified membership callback, cannot simply exact index_nonneg without unpacking.|
|1.8 contra/push|No contradiction.|
|1.9 eta|Original constant lambdas removed with inferior witness route, not eta-redexes.|
|1.10 single-use have|None.|
|1.11 apply/intro|Tried direct anonymous dependent pattern lambda; failed rfl application mismatch, clear rintro retained.|
|1.12 show|None.|
|1.13 have projections|None.|
|1.14 merge rw|None.|
|1.15 terminal simp|None.|
|1.16 nonterminal simp|None.|
|1.17 dot notation|Original .trans removed by canonical direct supremum argument.|
|1.18 trailing parens|None in selected proof.|
|1.19 push_neg|None.|
|1.20 exists helper|No private helper or trivial witness lemma.|
|2.1 grind|Actual isolated grind[Θ,indexSet] fails.|
|2.2 delete before grind|No retained grind.|
|2.3 simpa|Actual simp[Θ] fails; no consolidation chain.|
|2.4 fun_prop|n/a, no analytic regularity proposition.|
|2.5 positivity|Actual isolated positivity fails on custom supremum.|
|2.6 gcongr|n/a, no compound monotonicity goal.|
|2.7 lia/omega|n/a, no Nat/Int linear arithmetic target.|
|2.8 aesop|Actual isolated aesop fails.|
|2.9 norm_num/cast|n/a, no concrete computation/cast subgoal.|
|2.10 decide|n/a, arbitrary real inequality no finite decidable computation.|
|2.11 field_simp/ring|n/a, no algebraic identity.|
|2.12 linear_combination|n/a, no ring-ending proof/hypothesis certificate.|
|2.13 wlog|n/a, no symmetric cases.|
|2.14 calc|Original trans chain replaced by direct generic API.|
|2.15 multiple goals|No independent similar goals; one membership callback.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega/lia|None, arithmetic rule inapplicable.|
|3.4 rfl subst|Applied in rintro, no redundant subsequent simp.|
|3.5 attributes|No simp/grind normal-form registration authorized or necessary.|
|3.6 simp_all|None.|
|3.7 limits|No source limit to remove/raise.|

Step-back reflection: direct canonical API avoids proving boundedness or choosing polynomial1.
Actual exact?/apply? automation inconclusive at conservative2000heartbeat bound. Direct term
candidate failed dependent-rfl elaboration in `/private/tmp/roth-theta-nonneg-candidate-term.log`;
selected3-line proof is clear. An early unsupported `include [DecidableEq σ] in` syntax trial
was removed completely; automatic section-instance retention and actual-type verification
provide compatibility. No artificial unused proof terms/instance scaffolding retained.

## Verification, simplify, performance and freeze

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0,2423jobs, raw
`/private/tmp/roth-theta-nonneg-module.log`. Independent original probe command
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-theta-nonneg-original.lean` exited0.
It copies original baseline2b64544bf9f77a8ff957bf1bcaf693ac72217ff6 target and prerequisite
proofs into Original10, without invoking current Θ_nonneg to prove the original theorem.
Kernel rfl equality original/actual holds; direct actual getConstInfo.type exact old type
PASS modulo aligned universes. Actual built Θ_nonneg and independent original axioms exactly
propext/Classical.choice/Quot.sound. The same actual-import artifact certifies stronger
candidate/explicit lambda adapter/caller proofs/AST as above, each standard axioms only.

Fresh COMPLETE unfiltered native lean_diagnostic_messages on live Roth/Theta.lean:
success=true,partial=false,timed_out=false,failed_dependencies=[],0errors31warnings.
Raw `/private/tmp/roth-theta-nonneg-final-lsp.json`. Original28warnings remain, with3new
warnings from deliberately protected unused hB/hr and automatically retained DecEq section
instance. No suppression or unauthorized hypothesis removal. Source docstring unchanged;
no proof comment existed. New identifier Real.sSup_nonneg verified through local search,
source read, successful selected proof and generic compiled example. `index_nonneg` already
existed in original proof. Full source comparison against immutable start snapshot confirms
only the exact target proof changed; raw `/private/tmp/roth-theta-nonneg-focused.diff`.
All four routine callers unchanged; actual complete original contract identity preserves them.
No external usage found. No sorry/newaxiom/native_decide/limit raise/scaffolding introduced.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Actual lake build Roth.Theta exit0, module log.|
|definition_protected|pass|No def/abbrev/import edited, exact focused scope comparison.|
|theorem_statement_protected|pass|Original binder text and direct actual getConstInfo.type exact old type; DecEq retained automatically.|
|structure_gate|pass|Headline body3lines≤15, no conjunction conclusion or long branch.|
|naming_gate|pass|Θ_nonneg is descriptive, no forbidden pattern/abbreviation.|
|line_packing_gate|pass|All2signature rows measured above,101overflow justifies break.|
|inequality_orientation_gate|pass|hB/hr/conclusion all smaller-side-left, zero ≥/>.|
|diagnostics|pass|Fresh complete unfiltered native0errors31warnings; protected warnings documented.|
|trust_basis|pass|Actual built and independent original only standard3axioms.|
|comments_and_scope|pass|Original docstring exact, zero comments removed, exclusive target proof edit.|
|performance|pass,prefix-only|14.181ms before/13.669ms after, details below.|

Overall: worker gates pass. Owner full project THEN separate LeanEval checkpoint pending;
these owner results are not asserted here.

Simplify pass — PASS-THROUGH. Direct holistic review of the selected argument found no
further reuse, independence, missing API or readability issue. No new helper. Built-in
Skill/simplify invocation tool is not exposed in this runtime; the required review was
performed directly, not falsely attributed to an unavailable tool. Phase5a: canonical
mathlib proof used directly; stronger proposalD remains UNAPPLIED. Phase5b: no rename
required/queued; shared queue untouched under ownership instructions. File-wide phases
are owner responsibilities; no out-of-scope source modification.

## Eleven-step phase checklist

- [✓] Step1 required references read.
- [✓] Step2 full24audit printed above.
- [✓] Step2.5 all5actual mathlib searches and auxiliary variants recorded.
- [✓] Step2.6 every effective binder compiled probes plus public literature/inversion.
- [✓] Step2.7 all signature lines measured with arithmetic.
- [✓] Step2.8 per-occurrence inequality scan.
- [✓] Step3 all42golfing rules concrete statuses.
- [✓] Step4 independent step-back and direct simplify review.
- [✓] Step5a fresh COMPLETE unfiltered native final diagnostics.
- [✓] Step5b focused diff/type/module/trust/performance gates.
- [✓] Step6a no rename required/queued; shared sidecar untouched.

## Buzz — FAST-BOARD (exact-prefix only)

Immutable before/final source prefixes preserve every exact preceding import/context/source,
end immediately after target and append end Roth. Sequential uncontended actual commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-theta-nonneg-{before,final}-prefix.lean`.
Both exit0. All other compiler/native diagnostics/module requests drained before profiling.

|Target|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|3.096ms|5.181ms|2.094ms|3.810ms|14.181ms|
|final|3.690ms|4.140ms|2.021ms|3.818ms|13.669ms|

Raw UTF8 `/private/tmp/roth-theta-nonneg-{before,final}-profile.log`, declaration outer
anchors76885/76899. Structured `/private/tmp/roth-theta-nonneg-profile-summary.json` lists
all counted anchors. Count outer plus associated top-level async proof/addDecl/linter;
nested tactic/Meta/kernel not double-counted. Earlier leaf progress8.277ms reported only
outer+proof and was incomplete;14.181ms is full corrected baseline. Difference is ordinary
noise; no speedup claim. Both well below750ms, so no borderline repeat;1000msbudget.
No limit raise, profiling scaffold or source option added. WholeTheta late index_le_lem6
profiling failure remains owner cleanup obligation; these prefixes do not claim whole-file
profiling success. Buzz workflow executed directly with actual compiler trace; no separate
unavailable Skill tool invocation claimed.

## Final freeze

Final source SHA256
`b38cacf9d85ab62c485804d7848d92e8d7a4ef2145b05c32dc57f0eab0c4fd34`.
Exact source comparison: only selected target proof changed; original public signature/doc
and all remaining source identical to start snapshot. Final prefix checked equal to exact
final source through target. Source editing authority frozen/revoked. All native/search/
compiler/module/profile requests awaited and drained. Owner full project THEN separate
LeanEval checkpoint pending. No Git/shared log mutation. No new helper audit required.


## Owner frozen checkpoint gates

All leaf compiler/LSP/profile requests drained and source authority revoked before owner gates.
Source SHA256 `b38cacf9d85ab62c485804d7848d92e8d7a4ef2145b05c32dc57f0eab0c4fd34` stayed
unchanged through sequential `lake build` (exit0,88.364s) THEN separate `lake build Roth.LeanEval`
(exit0,25.958s). Raw `/private/tmp/roth-theta-d10-{full,leaneval}.log`; structured outcomes/hashes/
timing `/private/tmp/roth-theta-d10-builds.json`. Exact-path stage/commit and successful cleanup-
branch push precede the next original declaration edit. After publication:Theta10/35 originals,
overall191/264,9/14files complete. New proposalD is reviewable in the shared contract menu,
with definitive actual-import source/log evidence; no public amendment or caller change applied.
No new helper; whole-module final profiling and late default-heartbeat repair remain pending.
