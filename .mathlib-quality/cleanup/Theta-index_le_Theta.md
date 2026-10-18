# Dedicated original9 cleanup — `Roth.index_le_Θ`

Scope: only this public declaration, current lines88–91. Change: ordinary lambda `=>` becomes
`↦`; mathematical statement, effective public binders, proof, name, visibility, documentation,
definitions and imports preserved. Declaration remains4lines, body1line, delta0. No helper or
caller edit. No Git, shared report, learning log or rename queue mutation.

## Preparation and baseline

Read full leaf instructions, lean4 and mathlib-quality skills, complete cleanup command,
full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/cleanup-gates/profiling,
and relevant style/naming sections. Read-only preparation respected until owner RELEASE.
Owner reports original8 full build53.204s THEN separate LeanEval18.410s, both0, published
692d63c0fcc4d064239cd7ebc3043e83841c7621. Start source SHA256
b24e5eabe809940a7b4a510a6a1cc3e1f707851d87d0bf7cb352cb56a85348f1.
Same-source baseline reused from `/private/tmp/roth-index-bdd-final-lsp.json`: complete,
success=true, partial=false, timed_out=false,0errors28warnings. Target existing warning:
unused-in-type DecidableEq. All public binders protected, including hr/Fintype/DecidableEq;
no suppression added. Header metadata remains protected. Full project and separate LeanEval
are owner checkpoint gates, not claimed here.

## Full substantive24audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Target unusedDecidableInType warning retained as protected API artifact. Complete final diagnostics match baseline exactly.|
|2|HAVE SCAN|No have in one-line proof; no single-use intermediates.|
|3|SET_OPTION|No target option; no source heartbeat/recursion raise. Automation scratch conservatively lowers to2000.|
|4|SIMP SQUEEZE|No simp in selected proof; isolated simp trial leaves supremum inequality unsolved.|
|5|NAMING|index_le_Θ names the actual ordered operands, with the custom Θ notation. No forbidden number pattern or abbreviation. No rename required.|
|6|LINE PACKING|All3signature lines measured in table below. Adjacent complete syntactic arguments cannot fit.|
|7|BY PLACEMENT|Term proof, no by wrapper.|
|8|FORMAT|Two-space body, four-space signature continuation; no internal empty line; replaced ordinary lambda => with ↦; no haveI/letI.|
|9|COMMENTS|No proof comment; all three original source-bearing docstring lines preserved verbatim.|
|10|DOCSTRING|Public mathematical explanation and §5/source note preserved.|
|11|VISIBILITY|Public domain API used in Theta and MainLemma, retained. Deletion requires fresh approval.|
|12|STRUCTURE|One body line; no conjunction conclusion or branch. Correlated R/h witnesses remain one membership constructor.|
|13|MATHLIB|All5actual search methods find le_csSup already used directly; keep domain convenience API as instructed.|
|14|JUNK DEF|n/a, theorem.|
|15|EXISTS LEMMA|n/a, public multi-use inequality; not private trivial witness lemma.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective binder compiled drop/weakening probes below. No public alteration applied.|
|19|INEQUALITY|hr0<rj and conclusion index≤Θ already smaller-side-left; no reversed relation.|
|20|NORMAL FORM|index≤Θ is natural application-facing bound; underlying le_csSup canonical. No normal-form attribute added.|
|21|SYNTAX GENERALITY|Current hr/hR/hh parameters let callers use polynomial data directly without constructing indexSet membership.|
|22|IMPORT FANOUT|n/a, no import added.|
|23|CASTS|No cast changes. Int.castRingHom ℝ fixes coefficient codomain; `(h j : ℝ)` genuinely crosses ℤ→ℝ and qj coerces ℕ→ℝ.|
|24|INSTANCE-NAME|n/a, no instance declaration.|

Issues fixed: ordinary lambda notation only. Refactoring needed: none applied; existing
optional DecidableEq-removal menu remains unapproved. The successful no-hr discovery is
protected and does not broaden that menu. No new helper audit due.

## Measured signature packing and inequalities

Actual compiled width100 `#check @Roth.index_le_Θ` in original log includes
`{σ : Type u_1} [Fintype σ] [DecidableEq σ] {B : ℝ} {q r : σ → ℕ}` followed by
hr, R, hR, h, hh and exactly the original conclusion. Lean's printer uses implication
nesting; source packs complete binder/application syntax rather than splitting an identifier
from its application solely to occupy a column.

|Sig line|Codepoints|Next complete signature token|Arithmetic|Action|
|---|---:|---|---|---|
|88|83|`(hR : R ∈ RSet B r)`19chars|83+1+19=103>100|ok|
|89|75|`index (map (Int.castRingHom ℝ) R)`33chars|75+1+33=109>100|ok|
|90|78|none; proof body next|n/a|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hr|`0 < r j`|none, canonical|none|
|2|conclusion|`index … ≤ Θ B q r`|none, canonical|none|
|3|whole signature|zero ≥/> relations; function arrows are not relations|n/a|none|

## Five actual mathlib searches

Raw native results `/private/tmp/roth-index-theta-search.json`.

|Method|Actual query and result|
|---|---|
|A Lean-Finder|element of bounded above set is at most its supremum: le_csSup, ConditionallyCompleteLattice.le_csSup, le_csSup_of_le, le_ciSup.|
|B Loogle|`BddAbove ?s → ?a ∈ ?s → ?a ≤ sSup ?s`: DirectedOn.le_csSup and le_csSup.|
|C LeanSearch|element of bounded above set is less than or equal to supremum: le_csSup, le_ciSup_iff', le_csSup_iff', le_sSup, le_csSup_of_le.|
|D source rg|Untruncated `theorem le_csSup / lemma le_csSup / le_csSup_of_le / le_csSup_iff` over Mathlib/Order; Basic.lean197 read in context.|
|E local name pattern|`le_csSup`, limit10:8source matches, including direct theorem and DirectedOn/Monotone/iff variants; index unavailable honestly recorded.|

Auxiliary variants inspected: le_csSup_of_le, le_csSup_iff, le_csSup_iff', le_ciSup,
DirectedOn.le_csSup, csSup_le. Common-equivalents lookup: generic upper-bound/supremum
bucket, no disguised custom predicate. Inversion fires: the mathematical proof abstracts to
arbitrary α/s/a with ConditionallyCompleteLattice, BddAbove s and a∈s; this is exactly
existing le_csSup, compiled as a generic example in positive scratch. No missing API extracted.
Direct application already used. Retain the meaningful public domain convenience theorem per
scope instruction; public deletion needs fresh approval. No claim of mathematical absence.
Known repeated full-Theta multi_attempt stalls on preceding leaves: did not repeat; bounded
isolated no-Theta-import prefix automation is used instead. Grind[Θ,indexSet], aesop, simp
all fail; exact?/apply? exhaust lowered2000heartbeats and are inconclusive. The prefix omits
the target, so searches cannot close by invoking the target itself.

## Every effective binder: compiled probes

Positive `/private/tmp/roth-index-theta-positive.lean` exit0; negative
`/private/tmp/roth-index-theta-negative.lean` expected exit1. Raw logs alongside.

|Binder|Class/use|Actual drop/weakening evidence|Decision|
|---|---|---|---|
|σ:Type*|Type variable for indices, polynomial and point|Literal drop with autoImplicit=false reports unknownσ; full proof compiles at arbitrary universe.|Already polymorphic, retain.|
|Fintypeσ|Instance required by index/Θ|Drop reports failed synthInstance Fintypeσ; Finiteσ candidate with Fintype.ofFinite explicitly reconstructed in conclusion/proof compiles.|Reconstruction changes signature, not applied.|
|DecidableEqσ|Effective section instance passed to boundedness|Drop with local classical compiles, standard axioms.|Existing optional menu candidate UNAPPLIED.|
|B:ℝ|Coefficient bound in RSet/Θ|Drop reports unknownB; arbitrary realB selected proof compiles.|Dependent data, preserve; real→abstract would change underlying project definitions.|
|q:σ→ℕ|Denominators in point and Θ|Drop reports unknownq (then secondary whnf timeout). Arbitraryq selected proof compiles.|Dependent data, preserve; no positivity strengthening.|
|r:σ→ℕ|Weights, degree constraints and Θ|Drop reports unknownr; selected arbitraryr with hr compiles.|Dependent data, preserve.|
|hr:∀j,0<rj|Proposition supplied to boundedness|Literal proof drop reports unknownhr; replacing by0≤ fails expected strict type. Independently proved boundedness without hr permits drop_hr and weak_hr, exit0 standard axioms.|Protected discovery; neither edit nor menu expansion.|
|R:MvPolynomialσℤ|Polynomial data|Drop reports unknownR; selected proof compiles arbitraryR satisfying membership.|Dependent value, preserve.|
|hR:R∈RSetBr|Membership with nonzero/degree/coeff facts|Drop reports unknownhR. Weakening to nonzero∧degree bounds fails membership constructor expected R∈RSetBr.|Coefficient restriction matters to membership; no unsupported minimality claim.|
|h:σ→ℤ|Numerator data|Drop reports unknownh (then secondary whnf timeout); arbitraryh selected proof compiles.|Dependent value, preserve.|
|hh:∀j,IsCoprime…|Proposition supplies permitted numerator|Drop reports unknownhh; existential-point variant fails expected universal coprimality type.|Pointwise membership definition requires each coordinate; preserve.|

No algebraic/analytic parent-class weakening or strict→weak candidate applies beyond those
listed: other binders are dependent values, non-strict membership bounds or coprimality.
The first positive scratch copied a no-hr helper without σ/Fintype binders under
autoImplicit=false; corrected. Its first corrected rerun overlapped module rebuild and
failed missing Theta.olean; rerun after completed module build exits0. Only final exit0
is proof/axiom evidence; negative batch/failed experiments certify neither absence nor axioms.

## Public literature

Local clean.tex644–669 defines Θ as supremum over precisely the permitted polynomials and
coprime numerators; membership immediately gives the bound. Source assumes positive r/q and
B≥1 in its surrounding definition; current API already permits arbitraryB/q where membership
and project index conventions make sense. Web queries actually run: `supremum least upper
bound every element bounded above set generalization` and `Roth theorem index polynomial
supremum Theta index sets polynomials`. First three results for supremum are ScienceDirect,
ProofWiki and Axiom Academy; author exposition also found [Gressman, Advanced Analysis](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html)
defining supremum by its upper-bound/leastness properties. First Roth results include
[Princeton diophantine approximation notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf),
[Min Ru's Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf), and Uppsala's
Thue–Siegel–Roth thesis. No extra specialized hypothesis removal inferred from search snippets.
The generic order-theory form is already le_csSup. ChatGPT math MCP unavailable: no exposed
matching tool. Exact binder findings are compiled above, not guessed from literature.

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|Already term proof, no wrapper.|
|1.2 by-rfl|None.|
|1.3 rw/exact|No rw.|
|1.4 simp/exact|No simp/exact chain.|
|1.5 trailing rfl|No trailing tactic rfl; membership's rfl is essential equality witness.|
|1.6 constructors|Already anonymous correlated membership constructor.|
|1.7 apply/exact|Already direct le_csSup application.|
|1.8 contradiction|None.|
|1.9 eta|Point lambda performs casts/division, no eta-redex; notation corrected to↦.|
|1.10 have|None.|
|1.11 apply/intro|None.|
|1.12 show|None.|
|1.13 projections|None.|
|1.14 rw merge|None.|
|1.15 terminal simp|None in selected proof.|
|1.16 nonterminal simp|None in selected proof.|
|1.17 dot notation|le_csSup takes separate boundedness and membership hypotheses; explicit application names the mathematical operation clearly.|
|1.18 parens/<||Boundedness application parentheses necessary before membership argument.|
|1.19 push_neg|None.|
|1.20 exists inline|Public multi-use inequality; no private existential wrapper.|
|2.1 grind|Actual bounded prefix trial fails.|
|2.2 grind predecessors|No retained grind.|
|2.3 simpa|Actual whole simp[Θ,indexSet] fails; no shorter consolidation.|
|2.4 fun_prop|n/a, no regularity property.|
|2.5 positivity|n/a, arbitrary symbolic index≤supremum, not positivity.|
|2.6 gcongr|n/a, no monotone arithmetic structure; needed supremum membership.|
|2.7 lia/omega|n/a, real supremum goal, no Nat/Int arithmetic subgoal.|
|2.8 aesop|Actual bounded prefix trial fails no progress.|
|2.9 norm_num/cast|n/a, no numeric computation/cast comparison.|
|2.10 decide|n/a, arbitrary real order bound, no finite decision procedure.|
|2.11 field_simp/ring|n/a, no equality; denominator not manipulated.|
|2.12 linear_combination|n/a, no ring terminator.|
|2.13 wlog|n/a, no symmetric branches.|
|2.14 calc|Already shortest direct term; no calc.|
|2.15 <;>|No parallel goals, supplied both arguments directly.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega/lia|None.|
|3.4 rcases/rfl|No destructuring; rfl equality constructs membership.|
|3.5 attributes|No public automation attribute justified or approved.|
|3.6 simp_all|No retained simp_all; targeted le_csSup term already direct.|
|3.7 options|No target option present/added.|

Step-back: already a one-line direct application of the canonical general theorem; automation
would obscure or lengthen membership/boundedness construction. exact?/apply? bounded failures
are inconclusive, not absence proofs. No helper or changed proof strategy improves clarity.
Simplify manual equivalent review (no callable built-in simplify skill): PASS-THROUGH except
ordinary lambda syntax correction; no additional change. Phase5a/5b: none applied, no renames.

## Verification and gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exits0,
`/private/tmp/roth-index-theta-module.log`,2423jobs. Selected exact-source-prefix proof exits0,
`/private/tmp/roth-index-theta-selected.{lean,log}`. Independent original proof
`/private/tmp/roth-index-theta-original.{lean,log}` exits0: isolated Original9 definitions,
original boundedness proof and its original map wrappers, then the original target proof;
no invocation of current target to prove original. rfl value/definition contracts pass.
Direct actual Lean.getConstInfo.type comparison modulo aligned universe parameters PASS,
including Fintype/DecidableEq implicit section binders. Both actual built Roth.index_le_Θ
and independent Original9.index_le_Θ axioms exactly propext, Classical.choice, Quot.sound.
No source sorry/new axiom/native_decide/limit raise or profiling scaffold.

Fresh complete unfiltered native lean_diagnostic_messages succeeds partial=false,
timed_out=false, failed_dependencies=[],0errors28warnings. Raw final
`/private/tmp/roth-index-theta-final-lsp.json`; exact diagnostic multiset equality to same-source
baseline, including line/column/category/message; comparison JSON alongside. All existing
protected warnings remain, including original8's deliberate unusedSectionVars DecidableEq.
No suppression. No new identifier introduced; le_csSup verified by native search, source and
successful selected proof. Focused worker diff `/private/tmp/roth-index-theta-focused.diff`
contains only lambda arrow. Routine Theta callers3 and external MainLemma caller1 unchanged;
exact actual type identity preserves their contract. Owner full project checkpoint is pending.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Actual lake build Roth.Theta exit0, module log.|
|definition_protected|pass|No definition edit; original definition value checks rfl.|
|theorem_statement_protected|pass|Only lambda notation; actual getConstInfo.type matches original modulo universes.|
|structure_gate|pass|Body1line, no conjunction conclusion or long branch.|
|naming_gate|pass|Descriptive index_le_Θ, no forbidden pattern/abbreviation.|
|line_packing_gate|pass|Measured all3signature lines above.|
|inequality_orientation_gate|pass|All relations0<rj and index≤Θ, no reverse.|
|diagnostics|pass|Fresh complete native final0errors28warnings, baseline identical.|
|trust_basis|pass|Actual built and independent original standard trio only.|
|comments_and_scope|pass|Docstring unchanged, zero proof comments removed, exclusive target notation edit.|
|performance|pass, prefix-only|24.066ms before/26.208ms after; actual trace appendix below.|

## Eleven-step phase checklist

- [✓] Step1 required reference docs read.
- [✓] Step2 full24audit printed above.
- [✓] Step2.5 five actual methods and auxiliary variants recorded.
- [✓] Step2.6 every effective binder compiled drop/weakening table plus public literature/inversion.
- [✓] Step2.7 every signature line measured with arithmetic.
- [✓] Step2.8 per-occurrence inequalities scanned.
- [✓] Step3 every one of42golfing rules has concrete status.
- [✓] Step4 independent step-back/simplify review.
- [✓] Step5a fresh complete native diagnostics verified.
- [✓] Step5b diff/type/module/trust gates printed; performance appendix follows.
- [✓] Step6a no rename required or queued; shared queue untouched per ownership instruction.

## Buzz — FAST-BOARD (exact-prefix only), final freeze

Both immutable source prefixes preserve every exact preceding import/context/declaration,
terminate after index_le_Θ, and append end Roth. Sequential uncontended actual commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-index-theta-{before,after}-prefix.lean`.
Both exit0, wall35.809s/36.318s. All other compiler/module/native LSP requests completed
before profiles launched; no request overlapped either profile.

|Target|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|10.225ms|7.544ms|1.780ms|4.517ms|24.066ms|
|after|9.579ms|9.250ms|2.225ms|5.154ms|26.208ms|

Raw UTF8 `/private/tmp/roth-index-theta-{before,after}-profile.log`, outer command anchors
73021/73054; structured summary `/private/tmp/roth-index-theta-profile-summary.json`,
execution status `/private/tmp/roth-index-theta-profile-status.json`. Count outer command
and associated top-level async proof/addDecl/linters; nested Meta/tactic/kernel nodes not
counted twice. Difference is ordinary noise, no speedup claimed. Both below750ms,
no borderline repeat;1000ms budget. No heartbeat/recursion raise, no source scaffolding.
WholeTheta profile remains owner requirement after known late index_le_lem6 default-heartbeat
failure cleanup; these prefix checks do not claim whole-module profiling success.

Final source SHA256 a66d8859819b240cb588a5b33b0e064bc0b25226a6b63ee19cba2946dde1adb0.
Final prefix verified identical to exact final source through target. Source edits frozen
and revoked; all requests drained. Owner full-project then separate LeanEval checks pending.

## Owner frozen checkpoint gates

Leaf source authority revoked and all requests drained before owner checks. Source SHA256
`a66d8859819b240cb588a5b33b0e064bc0b25226a6b63ee19cba2946dde1adb0` stayed unchanged through
sequential `lake build` (exit0,6.508s) THEN separate `lake build Roth.LeanEval` (exit0,3.153s).
Raw `/private/tmp/roth-theta-d09-{full,leaneval}.log`; structured hashes/outcomes/timing
`/private/tmp/roth-theta-d09-builds.json`. Exact-path staging, commit and successful cleanup-branch
push complete the checkpoint before the next original declaration edit. After publication:
Theta9/35 originals;overall190/264;9/14files complete. No new helper or public amendment;
whole-module final profiling remains pending.
