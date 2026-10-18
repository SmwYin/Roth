# Approved original6 API revisit: `Roth.one_mem_RSet`

Scope is exactly the user's selected A+B row: remove both `[Fintype σ]` and `[DecidableEq σ]`
from this public theorem, retaining σ/B/hB/r, their types, dependency, implicitness, names,
order and conclusion. This is a revisit, not another original: counts stay196/264,Theta15/35.
No other public change, helper, import, definition, caller edit or Git/shared-log write.

## Baseline and preparation

Read leaf instructions, both skills and full cleanup workflow; full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates; relevant
style/naming/profiling references; previous dedicated original6 report; shared contract
proposal including exact decision; immutable original source2b64544bf9f77a8ff957bf1bcaf693ac72217ff6.
Read-only preparation honored until explicit RELEASE after checkpoint15 push69a7271b.
Baseline source SHA ee05dd2413443892400d9d05ca4be8d26afbb0c4f4c33b47339460451abfca4d.
Owner baseline full build45.642s THEN separate LeanEval14.442s, both0 and stableSHA.
Reused same-hash COMPLETE unfiltered native baseline `/private/tmp/roth-theta-equiv/final-lsp.json`:
success=true,partial=false,timed_out=false,failed_dependencies=[],0errors/30warnings.
Cache fetch skipped (built imports ready); no separate project linter executable required.

## Result and mathematics

The polynomial1 is nonzero, has coordinate degree0, and coefficients0 or1. Thus arbitrary
natural degree bounds and1≤B suffice for membership, even for infinitely many variables.
The selected terminal simp stays unchanged; local `classical` supplies coefficient decidability.
`omit [Fintype σ] [DecidableEq σ] in` is placed BEFORE the unchanged docstring.
Body1→2lines; source adds exactly two lines. No claimed golfing saving from this API amendment.

## Full substantive24audit

|#|Item|Finding/action|
|---|---|---|
|1|LINT|Three baseline target instance warnings motivate exactly the approved removals; fresh complete final diagnostics required. Header/unrelated warnings remain owner scope.|
|2|HAVE|No have/let in target; local classical adds no named instance.|
|3|SET_OPTION|No source option or raised limit. Automation uses lowered2000 scratch budget only.|
|4|SIMP|One terminal unsqueezed simp; no nonterminal simp to squeeze.|
|5|NAMING|one_mem_RSet describes membership of1 in the existing RSet; no forbidden abbreviation or number scheme. No rename needed/authorized.|
|6|PACKING|One95-codepoint signature; complete measured table below.|
|7|BY|:=by stays on signature line.|
|8|FORMAT|Two two-space-indented proof lines, no blank body lines, haveI/letI, or semicolon.|
|9|COMMENTS|Original docstring byte-identical; no original inline comment to re-anchor.|
|10|DOCSTRING|Original statement/source citation preserved in place beneath omit.|
|11|VISIBILITY|Existing public theorem retained. No visibility amendment authorized.|
|12|STRUCTURE|Two-line body, no branches>10, explicit public conjunction, or helper.|
|13|MATHLIB|Fresh five methods find degree/coeff building blocks; use directly in existing custom-RSet API. No generic absence claim from unavailable index or bounded automation.|
|14|JUNK DEF|n/a theorem; no definition edit.|
|15|EXISTS|n/a membership theorem, no existential helper.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective original parameter compiled/probed below; only approved two class removals applied.|
|19|INEQUALITY|1≤B canonical; no ≥/>.|
|20|NORMAL FORM|Membership in unchanged project RSet is its existing API; coefficient/degree API already canonical.|
|21|SYNTAX GENERALITY|hB then r preserved for sole caller; no new iff or constant-polynomial API.|
|22|IMPORT FANOUT|n/a no import change.|
|23|CASTS|No cast in diff; existing `(1 : MvPolynomial σ ℤ)` fixes polynomial type and remains load-bearing.|
|24|INSTANCE-NAME|No instance declaration/name. Both public classes removed using scoped omit; classical is proof-local.|

## Fresh five-method search

Raw native search payload `/private/tmp/roth-one-api-search.json`.

|Method|Actual query/result|
|---|---|
|A Lean-Finder|`multivariate polynomial one coefficients zero or one degree zero arbitrary variables`: degrees_one,coeffs_one,coeffs_one_of_nontrivial,isHomogeneous_one,degreeOf_one.|
|B Loogle|`"degreeOf_one"`: MvPolynomial.degreeOf_one.|
|C LeanSearch|`multivariate polynomial coefficient of one degree of one`: coeff_X_pow,coeff_X',coeff_single_X,coeff_single_X_pow,coeff_X; partial auxiliary results.|
|D source rg|Untruncated scoped one_mem_RSet/RSet/degreeOf_one/coeff_one/coeff_one_zero/coeffs_one_of_nontrivial/degreeOf_C scan in Roth and mathlib MvPolynomial files; degreeOf_one and coeff_one found.|
|E local name|coeff_one limit15: exact MvPolynomial.coeff_one textual hit; index unavailable, so no absence inference.|

Auxiliary variants: degrees_one,coeffs_one,coeffs_one_of_nontrivial,degreeOf_C,coeff_C,
coeff_C_of_ne_zero. Common-equivalents table has no matching discrete/finite/separation bucket.
Conclusion: standard partial building blocks exist; retain public custom-RSet theorem under
explicit approved scope. No fresh helper/wrapper. No unverified identifier introduced: omit
is Lean syntax and classical is existing tactic; retained proof identifiers already compiled.

Fresh anonymous automation examples use exact source prefix BEFORE target, without Theta
import or a named failed theorem, preventing self-proof/search contamination. Actual compiler
`lake env lean /private/tmp/roth-one-api/automation.lean` exits1: grind[RSet] fails degree
case; aesop makes no progress; exact?/apply? hit lowered2000 scratch heartbeat budget and
are inconclusive. Selected simp example succeeds in this expected-failure batch; separate
positive exit0 compile supplies proof evidence. No native multi_attempt repeated because
prior consecutive Theta leaves stalled/cancelled; direct bounded compiler exploration used.

## Every effective original parameter

Fresh positive compiler `/private/tmp/roth-one-api/positive.lean` exits0. Fresh corrected
negative compiler `/private/tmp/roth-one-api/negative.lean` exits1 with expected dependency/
unsolved-goal failures, raw `negative-corrected.log`. Original erroneous dropBound scratch
used an invalid classical-semicolon line; corrected before conclusions and preserved earlier
log as non-evidence. Positive inversion probe uses deprecated Set.mem_setOf_eq only in scratch;
warning is documented, no deprecated lemma enters source.

|Parameter|Class/use|Actual candidates|Result|
|---|---|---|---|
|σ:Type*|Variable type in r and MvPolynomial|Universe-polymorphic positive cases; literal drop(autoImplicit=false); Sort*|Type* already general; drop unknownσ, Sort* incompatible with MvPolynomial Type domain.|
|Fintypeσ|Finiteness unused|dropFintype,Finite,dropBoth all compile|Approved full removal applied; all other public Fintype retained.|
|DecidableEqσ|coeff_one requires proof decidability|dropDecEq/dropBoth with local classical compile|Approved full removal applied.|
|B:ℝ|Bound in RSet|Literal drop; arbitrary B; exactThreshold|Drop unknownB; bound domain belongs to unchanged RSet, no abstract-domain rewrite.|
|hB:1≤B|Coefficient1 bound|Drop leaves unsolved conditional; exactThreshold iff; B=0 counterexample|Necessary; cannot weaken to0≤B. Retained exactly. No strict inequality/global bundle applies.|
|r:σ→ℕ|Coordinate bound|Arbitrary r including zero; literal drop|Drop unknownr; no positivity assumption exists; original domain/dependency retained.|

No point-localisation, algebraic parent, bundled/unbundled, strict→weak candidate applies beyond
these entries. Positive probes include constantMem: a≠0 and |a|≤B imply C a∈RSet B r,
with arbitraryσ. Inversion check fires after unfolding RSet: standard degree/coeff properties
suffice for constants; this broader candidate remains assessed/unapplied and is not a new API.
No additional public proposal is made, including the declined hq and D/E/F changes.

## Public literature and source check

Read clean.tex:644–666: integral nonzero polynomials with coordinate degree/coefficient bounds,
explicit allowance of constant1. The original finite positive-weight setting includes this
observation; compiler probes certify arbitraryσ andr for the unchanged Lean definition.
Fresh WebSearch queries: `Roth theorem polynomial height constant polynomial 1 degree coefficient bound`;
`Formalizing Roth theorem Takloo Bighash Yin index across sets polynomials`;
`polynomial ring arbitrary variables constant polynomial degree zero coefficients one generalization`.
Returned background includes [Sharifi's polynomial-ring notes](https://math.ucla.edu/~sharifi/notes/algebra-ch03.html),
[IAS algebra notes](https://www.math.ias.edu/~goresky/pdf/algebraic0.pdf), and
[nLab polynomial](https://ncatlab.org/nlab/show/polynomial). These support the ordinary
constant-polynomial formulation, not an additional local API amendment. Search results were
pooled by the web tool; no claim of exhaustive literature absence. ChatGPT math MCP unavailable
(no matching exposed tool); not evidence of absence. Inversion/general field/domain changes
would alter RSet and remain outside this exact approval.

## Packing and inequality artifacts

Signature line67 is95 codepoints, complete on one line (keyword through :=by).

|Sig line|Chars|Next signature token|Arithmetic|Action|
|---|---:|---|---|---|
|67|95|none(body next)|n/a entire signature on one line|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none smaller side left|none|
|2|entire signature|zero≥/>|n/a|none|

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|n/a absent.|
|1.2 by-rfl|n/a absent.|
|1.3 rw/exact|n/a absent.|
|1.4 simp/exact|n/a single terminal simp, no exact suffix.|
|1.5 trailing rfl|n/a absent.|
|1.6 constructor|n/a no constructor sequence.|
|1.7 apply/exact|n/a absent.|
|1.8 contra/push|n/a absent.|
|1.9 eta|n/a no lambda in retained proof.|
|1.10 single-use have|n/a no have.|
|1.11 apply/intro|n/a absent.|
|1.12 redundant show|n/a absent.|
|1.13 projections|n/a absent.|
|1.14 consecutive rw|n/a absent.|
|1.15 terminal simp|Unsqueezed retained.|
|1.16 nonterminal simp|n/a none.|
|1.17 dot notation|zero_le_one.trans hB retained.|
|1.18 trailing parens|n/a no needless trailing parentheses.|
|1.19 push_neg|n/a absent.|
|1.20 existential helper|n/a none.|
|2.1 grind|Fresh compiled grind[RSet] fails degree case.|
|2.2 pre-grind deletion|n/a no grind retained.|
|2.3 simpa|Single terminal simp already closes; no trailing chain to consolidate.|
|2.4 fun_prop|n/a no function-property proposition.|
|2.5 positivity|No remaining standalone positivity goal; 0≤B supplied directly by trans.|
|2.6 gcongr|n/a no monotonicity/calc.|
|2.7 lia/omega|n/a Nat degree bound solved directly by simp; no arithmetic chain.|
|2.8 aesop|Fresh anonymous compiler probe fails no progress.|
|2.9 norm_num/cast|Numeric casts handled by selected simp; threshold/counterexample separately compile.|
|2.10 decide|n/a arbitrary realB andσ; no finite decidable computation.|
|2.11 field_simp/ring|n/a no denominator identity.|
|2.12 linear_combination|n/a no ring/ring_nf terminator.|
|2.13 wlog|n/a no symmetric case branches.|
|2.14 calc|n/a none.|
|2.15 multiple goals|n/a no repeated goal branches.|
|3.1 erw|n/a absent.|
|3.2 legacy fun tactics|n/a absent.|
|3.3 omega→lia|n/a absent.|
|3.4 rcases-rfl|n/a absent.|
|3.5 attributes|No automation attribute change required or authorized.|
|3.6 simp_all|n/a one bound, no dependent local simplification chain.|
|3.7 options|No source options present/added.|

Step-back: one terminal simp plus local classical is the direct proof of all three defining
conditions. Compressing classical with a semicolon or introducing a helper would reduce
clarity or violate style. Generic searches cannot cite audited target; bounded exact?/apply?
remain inconclusive. No additional theorem is necessary.

## Simplify pass

Manual equivalent review; callable built-in simplify tool unavailable. PASS-THROUGH:
only scoped omit/proof-local classical added; no duplicate skeleton, wrapper, redundant cast,
single-use have, or helper. No additional source change.

## Caller inventory and exact original recovery

Repository-wide Lean-source rg finds exactly one direct call, in indexSet_nonempty; no
external caller. No caller edit was needed. A fresh standalone caller artifact copies the
immutable original indexSet_nonempty proof against actual Roth definitions and the updated
actual one_mem_RSet. It directly compares actual caller getConstInfo.type and BinderInfo
against this independent original caller. This also tests implicit section instances, not
merely header text. Module build and complete live diagnostics cover all later declarations.

Independent original target source is saved verbatim from immutable baseline in
`/private/tmp/roth-one-api/immutable-original-source.lean`. The compatibility artifact copies
the original RSet and original three-line proof into OneApiOriginal; no invocation of current
target occurs in that proof. Its RSet value kernel-equals actual RSet. An explicit adapter
takes the complete old six-binder σ/Fintype/DecEq/B/hB/r telescope and calls the actual built
new four-binder constant. A kernel-checked equality compares this lambda with the independent
old proof. Direct getConstInfo.type checks full old adapter type and actual retained exact
four-binder type. Names/order/BinderInfo match retained old binders; AST rejects both Fintype
and DecidableEq anywhere in actual type. Generated anonymous instance names in the full old
adapter are exempt, with exact class/type/order/BinderInfo retained. The initial verifier
wrongly compared those synthetic names; corrected final exit0 run alone certifies metadata.
Actual built target, independent old proof, adapter and retained-contract witness are each
checked against only propext/Classical.choice/Quot.sound. This is independent proof plus
actual-built-constant checking, not self-invocation as original evidence.

Actual printed four-binder signature at format.width100:

```lean
@one_mem_RSet : ∀ {σ : Type u_1} {B : ℝ}, 1 ≤ B → ∀ (r : σ → ℕ), 1 ∈ RSet B r
```

Actual explicit old-adapter output:

```lean
fun {σ} [Fintype σ] [DecidableEq σ] {B} hB r => one_mem_RSet hB r
```

`lake build Roth.Theta` exit0,43.970s; raw `module.log`, machine `module-status.json`.
`lake env lean actual-compatibility.lean` final exit0,26.605s; raw
`actual-compatibility-final.log`, machine `actual-final-status.json`.
`lake env lean caller.lean` exit0,24.971s; raw `caller-final.log`, same machine status.
All filenames here are under `/private/tmp/roth-one-api/`. Earlier failed verifier log is
explicitly not pass evidence. Original proof's original Fintype linter warning in scratch
is expected; independent proof keeps its original contract.

The unchanged caller now exposes unused-section DecidableEq after its callee stops taking
that instance. Its original type still retains both classes exactly. This warning is a
consequence of this approved target edit, not license to apply the later approved caller
removal during the current declaration checkpoint. No suppression/artificial proof use added.

## Complete live verification

Fresh native `lean_diagnostic_messages(file_path="Roth/Theta.lean",timeout_s=60)` returned
COMPLETE unfiltered success=true,partial=false,timed_out=false,failed_dependencies=[],
28warnings/0errors. Raw full payload `/private/tmp/roth-one-api/final-lsp.json`.
Compared message sets against exact same-hash baseline: precisely three target warnings removed
and the one expected caller unused-section DecidableEq warning added; all other messages
unchanged. No linter suppression. All normal compiler/LSP requests completed before profiler.

## Eleven leaf gates

|Gate|Result/evidence|
|---|---|
|lake_build_file|PASS actual lake build Roth.Theta exit0,43.970s, module.log/status.|
|definition_protected|PASS exact transformation shows no definition/domain/import change.|
|theorem_statement_protected|PASS exactly approved two class removals; ordinary header and conclusion byte-identical, exact retained actual type independently checked.|
|structure_gate|PASS2bodylines, no branch/helper or explicit public conjunction.|
|naming_gate|PASS descriptive membership name, no forbidden pattern, no rename.|
|line_packing_gate|PASS required complete95codepoint table.|
|inequality_orientation_gate|PASS required table,zero reversed relations.|
|cumulative_no_unintended_breakage|PASS leaf module/full live diagnostics and independent original sole-caller proof/type/BinderInfo. No caller edit; owner full/downstream gates pending.|
|independent_original_contract|PASS immutable baseline proof, explicit fullold6→actualnew4 lambda adapter, exact type/names/order/BinderInfo/AST.|
|standard_axioms|PASS actualbuilt/independentold/adapter/retained/caller all subsets of three standard axioms.|
|buzz/no_scaffolding|PASS185.150ms exact-prefix aggregate; no source options/limits/native_decide/sorry/newaxiom.|

Phase5a/5b: no extra refactoring/rename; queue/shared logs untouched. Simplify manual equivalent
PASS-THROUGH. No helper requiring another dedicated audit. Header metadata unchanged as instructed.
Full project lake build THEN separate Roth.LeanEval belong exclusively to owner and remain
pending the frozen revisit; this report does not claim those final owner gates ran.

## Eleven-step phase checklist

1. ✓ Required full references/skills/workflow read.
2. ✓ Full substantive24audit.
3. ✓ Five actual mathlib methods and honest index/automation limits.
4. ✓ Every effective original binder compiled/probed; literature and inversion recorded.
5. ✓ Per-signature-line measured packing table and actual #check.
6. ✓ Per-occurrence inequality table.
7. ✓ All42rules given concrete status.
8. ✓ Step-back review and contamination-free one-tactic/term/search alternatives considered.
9. ✓ Complete unfiltered final live diagnostics; exact warning delta documented.
10. ✓ Eleven leaf gates with raw actual build/type/axiom/performance evidence; owner gates pending.
11. ✓ No rename/helper; comments/docstring preserved; only dedicated report sidecar.

## Buzz: FAST-BOARD, exact source prefixes only

After all ordinary compiler/build/LSP requests drained, ran sequential before/after actual
source prefixes preserving every preceding exact import/declaration/section and ending just
after target with end Roth. Actual commands:

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-one-api/before-prefix.lean
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-one-api/after-prefix.lean
```

Both exit0; wall32.711s/30.982s, structured profile-status.json; raw before-profile.log and
after-profile.log. Corrected pure parser profile-summary.json retains every counted node.
The initial parser detected two target anchors in the omit expansion and stopped rather
than accepting a double count. Corrected parser uses the OUTER omit macro command exclusively;
its inner section/omit/end_local_scope/theorem/end command records are excluded as already
included. No source/compiler change or repeated performance run was needed for parsing.

|Version|Outer command|Async proof|Async kernel/addDecl/realization|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|Before|4.086ms|177.691ms|6.094ms|8.055ms|195.926ms|
|After|5.052ms|161.034ms|7.974ms|11.090ms|185.150ms|

Before anchor rawline5377; after outer omit anchor rawline5989 (inner theorem rawline5466
excluded). Associated top-level async proof/kernel/linter counted; nested tactic, Meta,
macro and kernel child timings not double counted. No separate target compiler node emitted.
Both aggregates below750ms, so no borderline repeat required; budget1000ms. No heartbeat
figure inferred from wall time. No profiling scaffolding or limits added to production.
This is prefix-only evidence; owner actual whole-Theta final sweep remains mandatory after
known late index_le_lem6 cleanup. It certifies no whole-module performance claim.

## Final freeze and handoff

All leaf ordinary compiler, native LSP, and profiler requests/processes have completed; all
sessions drained. Source authority revoked: this leaf will make no further source edits.
Final exact source transformation rechecked: precisely scoped omit and local classical,
rest of file byte-identical to release snapshot. Full target docstring preserved byte-for-byte;
no inline comment removed. Body1→2lines, source+2lines, no helper or caller edit.

Final source SHA256:
`5d7f681b2e03c3c1845e8751bb87783aab68dc21c2633bb5c9d03b95b1a46592`.

Detailed report is the only repository sidecar this leaf writes. No Git mutation, shared-log
write, rename queue write, header change, additional hypothesis removal, or outstanding request.
All11leaf gates pass; owner frozen full lake build THEN separate Roth.LeanEval and publication
remain pending. Original audit counts stay196/264,Theta15/35 after this approved revisit.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 45.375 s and 15.075 s.
Theta SHA256 `5d7f681b2e03c3c1845e8751bb87783aab68dc21c2633bb5c9d03b95b1a46592` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r06-full.log` and `/private/tmp/roth-theta-r06-leaneval.log`; machine record
`/private/tmp/roth-theta-r06-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 6; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
