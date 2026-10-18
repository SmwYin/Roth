# Approved revisit of original9 — `Roth.index_le_Θ`

Applied exactly approved A.DecidableEqσ removal through `omit [DecidableEq σ] in` before the
unchanged docstring. Fintypeσ, every ordinary argument (including now-unused `hr`), their names,
order, BinderInfo, domains, conclusion, public name and visibility remain. No caller or helper
edit. Declaration4lines/body1line unchanged; source gains1 omit line. No original-count increase:
Theta15/35 and overall196/264 remain owner counts. No Git/shared-report/rename-queue write.

## Preparation and baseline

Read `/private/tmp/roth_theta_leaf_instructions.md`, both lean4/mathlib-quality SKILL.md files,
full cleanup workflow, full golfing-rules/proof-patterns/mathlib-search/generalisation-patterns/
cleanup-gates/profiling, relevant style rules and full naming guide; prior dedicated original9
report and exact Theta-contract-proposal decision. Read current Theta source and immutable
baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Read-only freeze honored until explicit RELEASE.
RELEASE checkpoint c12193f2322542c9415892ee26354bf46532c74f was pushed; parent reports sequential
full build80.493s then separate LeanEval22.939s, both0, all requests drained. Start source hash
71d8a5a8821bfc9c787d0ae6db8b4a086c580370f0ddd13ca10a5353c0f3c460 matches baseline doctor
`/private/tmp/roth-bdd-api/final-lsp.json`: complete success, partial=false,timed_out=false,
failed_dependencies=[],0errors28warnings. Identical-source baseline LSP reused per instructions.
No optional cache fetch or separate runLinter needed; native LSP supplies all linter diagnostics.
Header metadata preserved. All new artifacts below use `/private/tmp/roth-index-theta-api/`.

Candidate exact prefix compiled exit0 before mutation (`candidate.lean/log`), retaining hr and
Fintype, using only standard axioms. Production patch is only the omit line (`focused.diff`).
Current proof uses r08's `indexSet_bddAbove B q`; no obsolete hr argument was reintroduced.

## Fresh substantive24audit

|#|Item|Finding/action|
|---|---|---|
|1|LINT|Remove approved DecEqσ instance. Retain unused hr by exact selected scope; no suppression/underscore rename. Complete final0errors27warnings, delta below.|
|2|HAVE SCAN|No have in target; no single-use intermediary.|
|3|SET_OPTION|No target option/limit raise; scratch automation lowers budget to2000.|
|4|SIMP SQUEEZE|No selected simp; actual clean-prefix simp trial leaves supremum inequality.|
|5|NAMING|index_le_Θ describes index≤Θ in operand order; no forbidden abbreviations/numeric pattern; no rename.|
|6|LINE PACKING|All3signature lines measured below; no complete next argument fits.|
|7|BY PLACEMENT|Already direct term, no by wrapper.|
|8|FORMAT|2-space body/4-space continuation, no empty internal line, ordinary lambda ↦, no production haveI/letI.|
|9|COMMENTS|No proof comments; all3docstring lines byte-preserved and omit placed before them.|
|10|DOCSTRING|Public mathematical statement and §5/Lean-note attribution retained unchanged.|
|11|VISIBILITY|Public API used by MainLemma and Theta; retained per user preference.|
|12|STRUCTURE|Body1line; no conjunction conclusion/branch. Correlated membership witnesses stay shared.|
|13|MATHLIB|Five fresh actual searches reconfirm le_csSup already used directly; no new private wrapper. Public domain API retained under scope preference.|
|14|JUNK DEF|n/a theorem, no data definition edited.|
|15|EXISTS LEMMA|n/a public inequality with actual multiple uses, not private witness wrapper.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every original effective binder probed; apply only selected DecEq removal. hr/Fintype stay per current scope.|
|19|INEQUALITY|0<rj and index≤Θ canonical, no reversed relation.|
|20|NORMAL FORM|Application-facing index≤supremum; le_csSup is canonical generic form. No normal-form attribute.|
|21|SYNTAX-GEN|hR/hh let caller supply polynomial/numerator facts directly; no extra membership API proposed.|
|22|IMPORT-FANOUT|n/a no import change.|
|23|CASTS|No cast diff; h j:ℝ and qj coercions genuinely bridge integers/naturals to real evaluation. Int.castRingHom ℝ fixes codomain.|
|24|INSTANCE-NAME|n/a no instance declaration. Synthetic anonymous instance renumbering exempt from name equality; exact types/order/BinderInfo checked.|

Issues fixed: only approved DecEqσ removal. No recommended broader weight API change in this
scoped revisit, no helper/extraction due. Standing autonomy does not reopen preserved choices.

## Signature packing and inequality inventory

Successful `original-adapter-fixed.log` renders actual `#check @Roth.index_le_Θ` at width100:
σ/Fintype/B/q/r, then hr/R/hR/h/hh and the original index≤Θ conclusion; no DecEq binder.

|Signature line|Codepoints|Next complete token|Arithmetic|Action|
|---|---:|---|---|---|
|93|83|`(hR : R ∈ RSet B r)`19|83+1+19=103>100|ok|
|94|75|`index (map (Int.castRingHom ℝ) R)`33|75+1+33=109>100|ok|
|95|78|none, proof body next|n/a|ok|

|#|Location|Relation|Action|
|---|---|---|---|
|1|hr|`0 < r j`|canonical, retain|
|2|conclusion|`index … ≤ Θ B q r`|canonical, retain|
|3|whole signature|zero ≥/> comparisons|no rewrite or rename|

## Fresh five-method search, auxiliary routes and inversion

Raw native results `search.json`. All search results inspected; local index says unavailable,
so source hits establish presence and no empty-index absence inference is made.

|Method|Actual query|Result|
|---|---|---|
|A Lean-Finder|Every element of a bounded above set is at most its supremum|le_csSup, ConditionallyCompleteLattice.le_csSup, le_csSup_of_le, le_sSup, le_ciSup|
|B Loogle|`BddAbove ?s → ?a ∈ ?s → ?a ≤ sSup ?s`|le_csSup; DirectedOn.le_csSup|
|C LeanSearch|An element of a bounded above set is less than or equal to its supremum|le_csSup, le_csSup_of_le, le_sSup, le_csSup_iff', le_sSup_iff|
|D source rg|Untruncated theorem/lemma le_csSup and le_csSup_of_le/le_csSup_iff over Mathlib/Order|Basic.lean197/205/213 and partial-order variants; Basic190–225 read in context|
|E local name|le_csSup, limit15|8source hits incl direct/DirectedOn/Monotone/iff variants; index unavailable|

Auxiliary routes examined: le_csSup_of_le, le_csSup_iff, le_csSup_iff', le_ciSup,
DirectedOn.le_csSup, csSup_le. Common-equivalents bucket: generic supremum/order upper bound;
no disguised custom predicate. Inversion fires: after treating the index as an element of a
bounded set, all content is generic order theory. Generic `ConditionallyCompleteLattice`
example compiles in `positive.lean` using le_csSup directly. No missing API extraction needed.
Domain-facing public theorem retained per explicit prior preference/current scope; no deletion
or wrapper churn. No mathematical absence claim. Known full-Theta multi_attempt stalls were
not repeated; actual bounded clean-prefix anonymous automation trials used instead.
`automation.lean` ends BEFORE target and imports no Roth.Theta, so exact?/apply? cannot cite it
or failed named trials. grind[Θ,indexSet], aesop, simp fail; exact?/apply? reach conservative
2000heartbeats and are inconclusive. Expected exit1 is exploration evidence, never axiom evidence.

## Fresh binder drop/weakening probes

`positive.lean/log` exit0. `negative.lean/log` expected exit1 with named source ranges. All
proofs construct le_csSup membership directly, without invoking current audited theorem.

|Original effective binder|Class/use|Actual evidence|Decision|
|---|---|---|---|
|σ:Type*|type variable for all dependent data|Drop under autoImplicit=false: unknownσ. Positive proof remains universe-polymorphic.|retain polymorphism|
|Fintypeσ|index/Θ require finite enumeration|Drop: failed synth Fintypeσ. Finiteσ with Fintype.ofFinite explicitly reconstructed in conclusion/proof compiles.|retain exact original Fintype per selected scope|
|DecidableEqσ|section decidability|Drop compiles, even selected term prefix without classical; standard axioms.|approved removal applied|
|B:ℝ|RSet/Θ bound|Drop: unknownB. Positive proof handles arbitrary real bound.|dependent value retained; abstract codomain would change definitions|
|q:σ→ℕ|point denominators/Θ|Drop: unknownq (plus secondary timeout). Arbitrary q positive proof compiles.|retain no q-positivity requirement|
|r:σ→ℕ|weights/degrees/Θ|Drop: unknownr. Positive proof arbitrary natural weights with retained hr.|retain exact domain|
|hr:∀j,0<rj|now unused after r08|drop_hr and weak_hr compile, standard axioms; no claimed necessity.|retained EXACTLY; not selected, no broader API churn|
|R:MvPolynomialσℤ|polynomial data|Drop: unknownR; arbitrary satisfying membership compiles.|retain dependent value|
|hR:R∈RSetBr|membership witness|Drop: unknownhR. Weaken to nonzero∧degree bound: membership constructor mismatch.|retain; failed current-proof probe is not mathematical minimality|
|h:σ→ℤ|numerators|Drop: unknownh (plus secondary timeout); arbitrary h positive proof compiles.|retain dependent value|
|hh:∀j,IsCoprime…|coordinate condition|Drop: unknownhh. Existential coordinate condition: expected universal mismatch.|retain; definition needs each coordinate|

No parent algebraic/analytic class candidate exists here: types are project-fixed integers/reals,
remaining hypotheses are dependent data, membership or coprimality. Finiteness reconstruction
is explicitly measured but not recommended/applied under this revisit's fixed scope.

## Public literature and mathematical formulation

Read clean.tex644–669: Θ is the supremum over precisely these nonzero bounded polynomials and
coprime numerators; membership gives the individual bound. Surrounding source assumes positive
r/q and B≥1; this Lean API already accepts arbitrary B/q with membership and its index conventions.
Fresh web queries: `supremum upper bound every member bounded above set definition generalization`
and `Roth theorem "index" "supremum" polynomials Theta` (also broader initial Roth query).
First generic hits: [Gressman's Advanced Analysis](https://www2.math.upenn.edu/~gressman/analysis/01-completeness.html),
[MathWorld](https://mathworld.wolfram.com/Supremum.html),
[MathCS definition](https://mathcs.org/analysis/reals/infinity/defs/lub_sup.html).
Gressman's exposition defines supremum as least upper bound, supporting the generic order
form already supplied by le_csSup. First specialized hits: [Princeton Roth lecture](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf),
[A quantitative Roth–Ridout version](https://citeseerx.ist.psu.edu/document?doi=97e1f64a69bd280d0abc586cb61277fbd390e499&repid=rep1&type=pdf),
and [Diophantine Approximations notes](https://simonrs.com/eulercircle/irpw2022/leo-diopapprox-paper.pdf).
Specialized snippets are discovery context, not evidence for further hypothesis removal.
ChatGPT math MCP: unavailable, no matching exposed tool. No literature-driven API amendment.

## All42golfing rules

|Rule|Concrete fresh status|
|---|---|
|1.1 by-exact|Already direct term; no wrapper.|
|1.2 by-rfl|None.|
|1.3 rw/exact|No rw.|
|1.4 simp/exact|No selected simp chain.|
|1.5 trailing rfl|Membership rfl essential equality witness, not trailing tactic.|
|1.6 constructors|Already anonymous correlated membership constructor.|
|1.7 apply/exact|Already direct le_csSup application.|
|1.8 contradiction|None.|
|1.9 eta|Cast/division lambda is not eta-redex; ↦ already correct.|
|1.10 have|None.|
|1.11 apply/intro|None.|
|1.12 show|None.|
|1.13 projections|None.|
|1.14 rw merge|No rw.|
|1.15 terminal simp|No selected simp.|
|1.16 nonterminal simp|No selected simp.|
|1.17 dot notation|le_csSup separate boundedness/membership arguments already clear.|
|1.18 parens/<||Boundedness application's parentheses required before membership argument.|
|1.19 push_neg|None.|
|1.20 exists inline|Public inequality, no private witness helper.|
|2.1 grind|Actual clean-prefix grind[Θ,indexSet] trial fails.|
|2.2 grind predecessors|No retained grind/predecessors.|
|2.3 simpa|Actual simp[Θ,indexSet] trial leaves inequality; no consolidation.|
|2.4 fun_prop|n/a no function regularity.|
|2.5 positivity|n/a arbitrary index≤supremum, not positivity goal.|
|2.6 gcongr|n/a supremum membership, no congruent arithmetic structure.|
|2.7 lia/omega|n/a no integer arithmetic subgoal.|
|2.8 aesop|Actual clean-prefix trial fails, no progress.|
|2.9 norm_num/cast|n/a no concrete computation or cast equality.|
|2.10 decide|n/a arbitrary real order, no finite decision problem.|
|2.11 field_simp/ring|n/a inequality with unaltered denominator.|
|2.12 linear_combination|n/a no ring terminator/hypothesis combination.|
|2.13 wlog|n/a no symmetric cases.|
|2.14 calc|Already direct term, no calc.|
|2.15 <;>|No multiple similar goals, both evidence arguments supplied.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega/lia|None.|
|3.4 rcases/rfl|No destructuring; constructor rfl retained.|
|3.5 attributes|No automation attribute justified in selected scope.|
|3.6 simp_all|No selected simp_all.|
|3.7 options|No production option/limit raise.|

Step-back: canonical direct proof is already1line; automation adds search without simplifying
membership construction. exact?/apply? bounded failures are inconclusive. No callable built-in
simplify skill exists; manual holistic equivalent PASS-THROUGH. No duplicate proof skeleton/new
helper, no Phase5a/5b action or rename queued. Only approved omitted instance changed.

## Verification, original contract, callers and trust

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0, `module.log`,2423jobs. Fresh complete
unfiltered native final LSP `final-lsp.json`: success=true, partial=false,timed_out=false,
failed_dependencies=[],0errors27warnings. Baseline28→27: both target DecEq warnings removed;
index_det_le gains unusedSectionVars DecEq warning because its proof now calls an instance-free
target. Its original effective public instance remains, verified below. Existing target hr
warning remains, no suppressions/rename. All other diagnostic message/category/severity entries
unchanged (line numbers after insertion shift); `diagnostic-delta.json` records full delta.

`original-adapter.lean` independently copies immutable original RSet/indexSet/Θ values,
map wrappers, original boundedness algorithm and original target proof; immutable target text
verified verbatim in that copy. It never invokes current target for the independent original
proof. Definition-value checks rfl pass. Explicit `Adapter9.recover` accepts the ENTIRE old
σ/Fintype/DecEq/B/q/r/hr/R/hR/h/hh telescope and calls actual built Roth.index_le_Θ with exactly
the retained arguments. Its explicit full-old λ is kernel-checked; it kernel-equals independent
original proof by rfl. Direct getConstInfo types compare old adapter to immutable original,
and actual new type to original minus ONLY DecEq. Actual telescope10 vs original11; retained
ordinary names/order/BinderInfo and Fintype verified, actual AST has no DecEq. Standard axioms
exactly propext,Classical.choice,Quot.sound for independent original, actual built theorem and
adapter. Definitive successful log `original-adapter-fixed.log` exit0. First verifier failed
only scratch Array.eraseIdx bound elaboration; corrected to extract/concatenation, final clean
exit0 is certification. Earlier failed log is retained separately, never accepted as pass.

Repository inventory: Theta has two actual uses inside index_det_le (now505/506); external
MainLemma.lean672 has `index_le_Θ hr0 hWX hh`. hr stays visible and no denominator change.
No caller edit. `caller.lean/log` proves a theorem using immutablebaseline index_det_le HEADER
and actual imported caller proof, then compares actual complete public type including implicit
DecEqτ and checks standard axioms: exit0/PASS. Owner prepared independent immutable MainLemma
header probe is UNCOMPILED here and belongs after owner's frozen full→LeanEval rebuild; not
claimed passed. Whole-project and separate LeanEval gates remain parent-owned/pending.

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Actual lake build Roth.Theta exit0; module.log|
|definition_protected|pass|No definition diff, old defining values rfl|
|theorem_statement_protected|pass, approved exception|Only selected A.DecEqσ removal; full old adapter/exact new AST/type metadata verified|
|structure_gate|pass|Body1line, no conjunction conclusion/branch|
|naming_gate|pass|Descriptive name with no forbidden pattern|
|line_packing_gate|pass|All3signature lines measured above|
|inequality_orientation_gate|pass|Complete scan has no reversed comparison|
|diagnostics|pass|Fresh complete unfiltered native0errors27warnings, scoped delta explained|
|trust_basis|pass|Actual built/independent original/adapter standard trio only|
|comments_and_scope|pass|Only omit inserted; unchanged docstring/body; no caller or helper edit|
|performance|pass, prefix-only|25.452ms before/26.385ms after; appendix below|

## Eleven-step phase checklist

- [✓] Step1 references fully read as scoped above.
- [✓] Step2 full24audit.
- [✓] Step2.5 five actual searches, auxiliary variants, no unsupported absence claim.
- [✓] Step2.6 every effective binder compiled probe plus public literature/inversion.
- [✓] Step2.7 complete measured signature table.
- [✓] Step2.8 full inequality scan.
- [✓] Step3 all42golfing rules concrete status.
- [✓] Step4 holistic step-back/manual simplify.
- [✓] Step5a fresh complete native final diagnostics.
- [✓] Step5b module/diff/type/trust gates, performance appendix below.
- [✓] Step6a no rename needed; sidecar untouched under ownership instruction.


## Buzz — FAST-BOARD, exact-prefix only; final freeze

All ordinary compiler sessions and COMPLETE native LSP request finished and were drained before
profiling. Sequential actual commands, each exit0:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-index-theta-api/{before,after}-prefix.lean`.
No overlapping compiler/LSP/build request during either sample. Prefixes preserve exact source
imports/context and all preceding declarations, ending immediately after target with end Roth.
Final prefix equality to current source through target verified. No production profiling scaffold.

|Phase|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|10.848ms|7.127ms|1.763ms|5.714ms|25.452ms|
|after|11.498ms|7.109ms|2.032ms|5.746ms|26.385ms|

UTF8 raw `before-profile.log` outer anchor77005; `after-profile.log` outer omit anchor79418.
After's nested declaration command10.948ms is INCLUDED in enclosing omit11.498ms and not counted
twice. Associated top-level async proof/addDecl/linter included; nested Meta/kernel/tactic nodes
not double-counted. Structured `profile-summary.json`, gate statuses `status.json`. Both totals
well below750ms repeat threshold/1000ms budget, ordinary noise, no speedup claim. Limit raises0,
performance deferrals0. These are prefix-only checks; known late index_le_lem6 default-heartbeat
issue means owner whole-module final performance sweep remains pending, not passed here.

New identifier check: no new mathematical identifier; existing DecidableEq and omit syntax
verified by candidate/module/actual-type checks. Source docstring/body are unchanged.

Final source SHA256 `4d5ff0a2c7715084f7c0dfeffd93d22467e2bce175501e7e60c81d427d693607`.
All requests/terminal sessions drained. No additional source/report/scratch mutation or Lean
requests after final handoff; source authority frozen/revoked. Owner frozen full build THEN
separate LeanEval rebuild and prepared MainLemma original-contract probe remain PENDING here.


## Owner external caller contract gate

After the successful frozen full build and separate LeanEval rebuild, owner compiled
`/private/tmp/ThetaIndexLeMainLemmaOriginalContract.lean` with `lake env lean`: final exit 0,
raw `/private/tmp/roth-theta-r09-mainlemma-original-contract-final.log`. The expected proposition
is extracted from immutable baseline MainLemma.lean's main_lemma header (SHA256
902262cdce5c02b3a6a34022ea7063e2bb0290e7889c826b6b15e2f04e641373), not copied from the
current constant type. Actual fresh-built Roth.main_lemma has exactly that original type and
retained user-written names/order/BinderInfo, and only the three standard axioms. This checks
the external caller's contract; it is not a claim to independently reprove its entire long proof.
The visible call `index_le_Θ hr0 hWX hh` is unchanged, including positivity and denominator data.
The first scratch metaprogram had ambiguous `.instImplicit` notation; explicit
`BinderInfo.instImplicit` fixed it. That failed log is preserved separately and is not pass evidence.
No production source changed; all owner compiler sessions are drained before publication.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 57.757 s and 12.932 s.
Theta SHA256 `4d5ff0a2c7715084f7c0dfeffd93d22467e2bce175501e7e60c81d427d693607` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r09-full.log` and `/private/tmp/roth-theta-r09-leaneval.log`; machine record
`/private/tmp/roth-theta-r09-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 9; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
