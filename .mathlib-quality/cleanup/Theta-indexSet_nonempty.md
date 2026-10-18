# Dedicated original7 cleanup — `Roth.indexSet_nonempty`

Scope: only this public theorem in `Roth/Theta.lean`, lines71–72. The change replaces
both ordinary lambda arrows with `↦`; the one-line shared existential witness is preserved.
No public signature, hypothesis, definition, name, visibility, documentation, import, caller,
helper, header metadata, rename queue or shared log changed. Proof body1→1lines; line delta0.

## Preparation and baseline

Full `/private/tmp/roth_theta_leaf_instructions.md`, lean4/mathlib-quality skills, full cleanup
workflow, full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns,
cleanup-gates and profiling were read; relevant style/naming sections consulted. Read-only
preparation honored until owner's explicit RELEASE following published original6 checkpoint
`a4600633fbc0c15c131ec6e0d85fbe644a15303b`. Owner baseline full build60.236s THEN separate
LeanEval16.524s both exit0. Baseline source SHA256
`555407fefac3d3c452906b586e4b98953d4a54593beb2e538f212dd805b0b45b` matched exactly.
Reused complete unfiltered native `/private/tmp/roth-one-mem-final-lsp.json` as expressly
allowed: success=true, partial=false, timed_out=false,27warnings/0errors. Target has an
unused-in-type DecidableEq warning; this is a public-contract candidate, not authorization.
No redundant baseline compiler/LSP request; no linter suppression added.

## Full substantive24audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Existing DecidableEq instance warning retained pending public approval. Complete baseline and final diagnostics retained.|
|2|HAVE SCAN|No have in either one-line proof.|
|3|SET_OPTION|No target option; none added. Isolated automation uses lowered2000 budget, never a source limit raise.|
|4|SIMP SQUEEZE|No simp in proof; no squeezing applicable.|
|5|NAMING|indexSet_nonempty describes nonemptiness of the established indexSet definition; no forbidden number pattern or abbreviation; no rename.|
|6|LINE PACKING|Single91-codepoint signature line measured below; no next signature token.|
|7|BY PLACEMENT|Term-mode body; no by wrapper needed.|
|8|FORMAT|Two-space body indentation, no empty internal line; two fun lambdas corrected to ↦; no haveI/letI output.|
|9|COMMENTS|No inline proof comment; original source-bearing docstring preserved byte-for-byte.|
|10|DOCSTRING|Existing public docstring states nonemptiness and source; protected.|
|11|VISIBILITY|Public contract retained; useful for csSup proofs; no approval to privatize.|
|12|STRUCTURE|One-line existential witness; outputs share the same R and h, hence no independent conjunct to split or pointless helper. No >10line branch.|
|13|MATHLIB|Five actual methods below; generic image_nonempty is partial conceptual building block; original direct witness is simpler. No absence claim from unavailable index.|
|14|JUNK DEF|n/a: theorem, no definition touched.|
|15|EXISTS LEMMA|Public multi-use nonempty theorem, not private single-use existential wrapper; correlated witness remains shared.|
|16|SHOW/CHANGE|None.|
|17|PUSH_NEG|None.|
|18|GENERALISE|Every effective binder tested or dependent-drop compiled below; public candidates all unapplied.|
|19|INEQUALITY|Only1≤B, canonical orientation; no reversed relation.|
|20|NORMAL FORM|Set.Nonempty on indexSet is canonical for csSup API; no alternate equivalence family needed.|
|21|SYNTAX GENERALITY|Current hB/q/r ordering is immediately usable by all three callers; generic RSet.Nonempty hypothesis is a candidate, not necessary API churn.|
|22|IMPORT FANOUT|n/a: no new import.|
|23|CASTS|Zero introduced casts/ascriptions. Retained witness1 is inferred as integer polynomial, h as integer-valued function.|
|24|INSTANCE-NAME|n/a: no instance declaration.|

## Line packing and inequality scan

Actual compiled `#check @Roth.indexSet_nonempty` with format.width100:

```
@indexSet_nonempty : ∀ {σ : Type u_1} [inst : Fintype σ] [DecidableEq σ] {B : ℝ},
  1 ≤ B → ∀ (q r : σ → ℕ), (indexSet B q r).Nonempty
```

|Sig line|Codepoints|Next signature token|Arithmetic|Action|
|---|---:|---|---|---|
|71|91|none; proof body next|n/a, entire signature on one line|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none, canonical|none|
|2|whole signature|zero ≥/> relations (function arrows are not relations)|n/a|none|

## Five actual mathlib search methods

Raw results: `/private/tmp/roth-index-nonempty-search-results.json`. The successful Loogle
retry was separately returned by the native tool. No remote result is treated as a current
local compile guarantee until source/probe verification.

|Method|Queries and actual results|
|---|---|
|A Lean-Finder|`nonempty set of indices of bounded integer multivariate polynomials constant one witness`: unrelated Chevalley complexity degree-bound results; no exact match returned.|
|B Loogle|`Set.Nonempty {x | ∃ a, _ a = x}` rejected malformed function placeholder. Actual retry `"image_nonempty"` returned Set.image_nonempty and Finset.image_nonempty.|
|C LeanSearch|`image of nonempty set is nonempty`: Set.instNonemptyElemImage, MapsTo.nonempty, range_nonempty and image_nonempty.|
|D source rg|Untruncated scoped indexSet_nonempty/Nonempty.image/nonempty_image_iff/isCoprime_one_left search in Set/Coprime sources and Theta; actual standard files checked: Set/Image.lean389–398 and Coprime/Basic.lean94. No duplicate custom-indexSet result claimed.|
|E local name pattern|`Nonempty.image`, limit8: empty items with index=unavailable; explicit limitation, not absence evidence.|

Auxiliary variants inspected: Nonempty.image, Nonempty.of_image, image_nonempty,
range_nonempty, MapsTo.nonempty, isCoprime_one_left. Common-equivalents table has no relevant
discrete/finiteness/separation bucket. Conclusion: partial generic Set API exists, while
indexSet's admissible polynomial and coprime numerator still require witnesses. No private
wrapper was added. This theorem packages a custom domain-specific witness, not a duplicate
of Set.image_nonempty with the same type.

Compiled no-Theta-import prefix probes ran grind, aesop, exact?, apply?. The first two fail;
exact?/apply? exhaust deliberately lowered2000 scratch heartbeats and remain inconclusive.
No self declaration exists in these artifacts. Five-method search therefore does not assert
mathematical absence. All identifiers already existed in the old proof; no new identifier
requires a hallucination exemption. Actual selected witness compiled independently.

## Generalisation: every effective binder

Positive artifact `/private/tmp/roth-index-nonempty-positive.lean`; negative artifact
`/private/tmp/roth-index-nonempty-negative.lean`; status/raw logs alongside. Every listed
negative was actually sent to Lean, not inferred from a textual unused-variable scan.

|Binder|Class/use|Compiled drop/weakening probes|Decision|
|---|---|---|---|
|σ:Type*|Type variable, polynomial variable and q/r domains|Literal σ drop with autoImplicit=false fails unknown σ; arbitrary universe-polymorphic σ compiles in positive probes.|Already polymorphic; preserve.|
|Fintype σ|Instance required by Roth.index/indexSet type|Literal drop fails synthInstance Fintypeσ. Finiteσ plus explicit chosen Fintype.ofFinite in conclusion/proof compiles.|Finite form changes how indexSet is interpreted; no same-type drop available; preserve.|
|DecidableEq σ|Decidability inherited by old proof's one_mem_RSet call|dropDecEq with local classical compiles, actual axioms printed.|Public weakening candidate UNAPPLIED; owner/root has not approved any menu.|
|B:ℝ|Value in coefficient bound|Literal drop fails unknown B; arbitrary real B in positives. Abstract coefficient-bound domain would require changing RSet definition.|Dependent value retained.|
|hB:1≤B|Proposition admitting constant1|Literal drop fails unknown hB; weakening to0≤B rejects one_mem_RSet application. Positive compiled counterexample ¬(indexSet0qr).Nonempty for Unit.|Cannot drop or weaken to nonnegative B. No strict hypothesis to weaken.|
|q:σ→ℕ|Denominator value used by indexSet|Literal drop fails unknown q; all positive witnesses arbitrary q including zeros.|No positivity hypothesis exists to remove; dependent value retained.|
|r:σ→ℕ|Degree/index value|Literal drop fails unknown r; positives arbitrary r including zero.|No positivity hypothesis exists to remove; dependent value retained.|

The counterexample proves zero coefficient bound forces every coefficient to zero and hence
R=0, contradicting RSet's nonzero condition. It certifies more than failure of the old witness.
No global/pointwise, strict-to-weak or bundled-class catalogue entry otherwise applies.
Initial generic scratch probe had an untyped zero-function domain; corrected to arbitrary
explicit q/r and rerun successfully. Failed scratch did not enter source.

Inversion check: after unfolding indexSet, no index-specific theorem is used; any R∈RSet
and the universal coprime numerator1 supplies an index value. Compiled generic candidate
`fromNonemptyRSet (q r) (hR : (RSet B r).Nonempty)` establishes this abstraction. Thus the
inversion diagnostic fires conceptually, but extracting a one-line helper adds no useful
proof structure; existing Set nonempty/image API already covers the abstract principle.
The public candidate and potential hR-hypothesis restatement remain assessed/unapplied.

## Public literature

Read clean.tex §Index across sets of polynomials, lines644–666. Source explicitly admits
constant1 with every numerator1; positive r/q and finite positive m are assumptions of the
surrounding estimates, while this witness works without q/r positivity and on empty variable
sets too (existing arbitrary σ already covers this).

Actual WebSearch queries: `Roth theorem polynomial height index constant polynomial one
supremum nonempty generalization`; `Formalizing Roth theorem Takloo Bighash Yin index across
sets of polynomials`. Returned leading hits included Wikipedia's Roth overview, McKinnon–Roth
[arXiv1306.2976](https://arxiv.org/abs/1306.2976), and Bombieri–Gubler material; other relevant
primary expositions: [Min Ru's Roth notes](https://www.math.uh.edu/~minru/fields/roth.pdf),
[AMS chapter4](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf),
[Milojević's exposition](https://aleksa-milojevic.github.io/expository/roth.pdf).
Broader geometric Roth generalizations do not alter this elementary set-witness argument;
no stronger local contract inferred from them. Local source and compiled binder probes are
the evidence for the exact formulation. ChatGPT math MCP unavailable (no exposed matching
capability), explicitly recorded. Public DecidableEq removal and RSet.Nonempty restatement
remain optional unapproved candidates, not blockers or applied changes.

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|n/a, already direct term.|
|1.2 by-rfl|n/a, no wrapper.|
|1.3 rw/exact|n/a, no tactic chain.|
|1.4 simp/exact|n/a, no simp.|
|1.5 trailing rfl|Final rfl is an essential existential equality field, not a tactic after simp; retain.|
|1.6 constructors|Already one anonymous constructor term.|
|1.7 apply/exact|n/a, no tactic chain.|
|1.8 by_contra|n/a, no contradiction proof.|
|1.9 eta|Two lambdas are constant functions, not eta-redexes; ↦ style correction applied.|
|1.10 have|n/a, none.|
|1.11 apply/intro|n/a, none.|
|1.12 show|n/a, none.|
|1.13 projections|n/a, none.|
|1.14 rw merge|n/a, none.|
|1.15 terminal simp|n/a, none.|
|1.16 nonterminal simp|n/a, none.|
|1.17 dot notation|n/a, no lemma application improved by dot notation.|
|1.18 parens/<||n/a, no needless trailing parentheses.|
|1.19 push_neg|n/a, none.|
|1.20 exists inline|Public theorem has three callers; keep shared witness instead of private helper.|
|2.1 grind|Actual isolated grind[indexSet,one_mem_RSet] fails witness synthesis.|
|2.2 grind predecessors|n/a, no retained grind.|
|2.3 simpa|n/a, no simp/closing chain. Direct term already minimal.|
|2.4 fun_prop|n/a, no analytic function property.|
|2.5 positivity|n/a, target is existential set nonemptiness.|
|2.6 gcongr|n/a, no inequality construction.|
|2.7 lia/omega|n/a, no Nat/Int linear arithmetic subgoal; coprimality uses exact standard theorem.|
|2.8 aesop|Actual isolated aesop fails with no progress.|
|2.9 norm_num/cast|n/a, no numeric calculation or cast goal in retained proof.|
|2.10 decide|n/a, arbitrary real B and polynomial existence, no finite computation theorem.|
|2.11 field_simp/ring|n/a, no algebraic identity.|
|2.12 linear_combination|n/a, no ring terminator/hypothesis identity.|
|2.13 wlog|n/a, no symmetric cases.|
|2.14 calc|n/a, no calc chain.|
|2.15 <;>|n/a, direct term has no open tactics/subgoals.|
|3.1 erw|n/a, absent.|
|3.2 continuity|n/a, absent.|
|3.3 omega/lia|n/a, absent.|
|3.4 rcases/rfl|n/a, absent; final term rfl retained.|
|3.5 attributes|No new global attribute: public normal form changes require approval.|
|3.6 simp_all|n/a, no local-context simplification.|
|3.7 options|No source heartbeat/recursion option present or added.|

Step-back reflection: the existing one-line term directly expresses the mathematical witness
and is already shorter/more deterministic than automation. No helper extraction serves an
independent fact. Generic image restatement adds proof plumbing. Exact?/apply? were actually
tried independently and inconclusive within lowered budget; no claim of absence follows.
Known repeated native multi_attempt stalls on preceding leaves were honored by using bounded
isolated ordinary compiler exploration; no stalled request was launched or left orphaned.

## Simplify pass

Manual equivalent review, since no callable built-in simplify tool exists: PASS-THROUGH.
No duplicate skeleton, single-use have, unnecessary wrapper, cast or helper identified.
No additional source edit. File-level phases5a/5b: no refactoring/rename applied; optional
public candidates above require fresh owner/root decision. No helper needing a fresh audit.

## Verification, performance, freeze

Actual completed leaf results follow. Full project then separate LeanEval
are owner-only checkpoint gates; this leaf does not assert they passed on the new source.

Actual module gate `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0,41.172s;
raw `/private/tmp/roth-index-nonempty-module.log`, structured gate status
`/private/tmp/roth-index-nonempty-gate-status.json`. Corrected positive probes exit0,25.694s.
Selected no-Theta-import prefix witness `/private/tmp/roth-index-nonempty-proofs.lean` exit0.
Negative/automation probes complete with expected exit1; none timed out at process level.
Their deterministic2000-heartbeat search failures are explicitly inconclusive.

Independent original gate `/Users/ramin/.elan/bin/lake env lean
/private/tmp/roth-index-nonempty-original.lean` exit0,24.008s. Original RSet/indexSet definitions,
original membership proof and original7 witness proof copied into Original7 namespace; neither
original theorem is proved by invoking the current theorem. Definition and proof-value rfl
checks corroborate compatibility. Most strongly `Lean.getConstInfo` retrieves actual original
and built constant `.type` fields; universe parameters alpha-aligned and Meta.isDefEq compares
them directly. It prints exact original7 contract PASS, including implicit section instances.
Actual built Roth.indexSet_nonempty and independent Original7.indexSet_nonempty each depend
on exactly `[propext, Classical.choice, Quot.sound]`. Raw original log alongside artifact.
No new axiom, sorry, native_decide or raised source limit.

Fresh COMPLETE unfiltered native `lean_diagnostic_messages(file_path="Roth/Theta.lean")`:
success=true, partial=false, timed_out=false, failed_dependencies=[],0errors/27warnings.
Raw `/private/tmp/roth-index-nonempty-final-lsp.json`. Exact line/message multisets equal
baseline; no added or suppressed warning. The one target DecidableEq warning remains because
its public removal is unapproved. Three routine callers compile in actual module and live
LSP; none edited. Exact snapshot comparison confirms the entire source differs only by the
two target lambda arrows (`/private/tmp/roth-index-nonempty-focused.diff`).

### Buzz — FAST-BOARD (exact-prefix only)

Both prefix files preserve every exact preceding import/source/context, terminate immediately
after original7 and append `end Roth`. Actual sequential commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-index-nonempty-{before,after}-prefix.lean`.
Both exit0, wall32.973s/30.780s. No ordinary compiler/LSP/probe request overlapped these profiles.

|Target|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|1.450ms|7.164ms|1.617ms|4.007ms|14.238ms|
|after|1.413ms|6.287ms|1.742ms|3.861ms|13.303ms|

Raw UTF8 `/private/tmp/roth-index-nonempty-before-profile.log` anchor33773 and
`/private/tmp/roth-index-nonempty-after-profile.log` anchor33775; structured summary
`/private/tmp/roth-index-nonempty-profile-summary.json`. Outer command plus associated outer
async proof/addDecl/linters counted; nested tactic/Meta/kernel children not double-counted.
No performance improvement is asserted for the syntax-only edit; both measurements are safely
below750ms, so no borderline repeat required; budget1000ms. No profiler scaffolding entered
source. maxHeartbeats raises removed0, added0. No target deferral or big change.
Whole-module profiling remains an owner final requirement after known late index_le_lem6
cleanup; this exact-prefix measurement makes no whole-module performance claim.

### Eleven leaf gates

|Gate|Actual result/evidence|
|---|---|
|lake_build_file|PASS, actual lake build Roth.Theta exit0,41.172s, module log.|
|definition_protected|PASS, exact before→after transform changes only target proof arrows; no def/abbrev edits.|
|theorem_statement_protected|PASS, unchanged signature/docstring/visibility/name and direct actual elaborated-type comparison including instances.|
|structure_gate|PASS,1body line; correlated witness preserved; no >10line branch.|
|naming_gate|PASS, descriptive indexSet_nonempty, no forbidden pattern/abbreviation.|
|line_packing_gate|PASS,91-codepoint single signature row with complete table.|
|inequality_orientation_gate|PASS, canonical1≤B; zero reversed inequalities.|
|cumulative_no_unintended_breakage|PASS at leaf scope: all3existing callers compile in module/live LSP; no caller edit. Owner downstream full/LeanEval pending.|
|independent_original_contract|PASS, nonself copied original proof and direct getConstInfo.type comparison exit0.|
|standard_axioms|PASS, actual built and independent original only propext/Classical.choice/Quot.sound.|
|buzz/no_scaffolding|PASS,13.303ms exact-prefix aggregate, all profile/probe/compiler/LSP requests complete, no source option raise.|

Leaf gates pass with the existing unapproved public DecidableEq warning explicitly retained.
Source edits are now FROZEN and REVOKED. Final Roth/Theta.lean SHA256:
`c2f8c7c4cca1a062bdab7a85a97927ea0b77f55090985752a05ca7d22014f555`.
No further source edit authorized to this leaf. All leaf requests/processes drained.
Only repository sidecar written: this report. No Git mutations/shared-log/rename-queue edits.

## Eleven-step phase checklist

1. ✓ Required full reference reads and scoped preparation.
2. ✓ Substantive24audit.
3. ✓ Five actual searches, failed/unavailable paths recorded honestly.
4. ✓ Every effective binder compiled/probed; public literature and inversion checked.
5. ✓ Measured complete per-signature-line packing table.
6. ✓ Per-occurrence inequality scan table.
7. ✓ All42golf rules concrete statuses.
8. ✓ Step-back/alternative proof review and simplify equivalent pass.
9. ✓ Complete unfiltered fresh native final diagnostics,0errors, unchanged27warnings.
10. ✓ Eleven leaf gates including actual module/original/axiom/profile evidence; owner full then separate LeanEval remain pending.
11. ✓ No rename needed; original documentation/comments preserved; no new helper; freeze/revoke.

## Owner frozen checkpoint gates

All leaf compiler/LSP/profile sessions drained and source authority revoked before owner gates.
Source SHA256 `c2f8c7c4cca1a062bdab7a85a97927ea0b77f55090985752a05ca7d22014f555` stayed
unchanged through sequential `lake build` (exit0,56.405s) THEN separate `lake build Roth.LeanEval`
(exit0,13.129s). Raw `/private/tmp/roth-theta-d07-{full,leaneval}.log`; structured timing/outcomes
and hashes `/private/tmp/roth-theta-d07-builds.json`. Exact-path stage/commit and successful
cleanup-branch push precede the next original declaration edit. After successful publication:
Theta7/35 originals; overall188/264;9/14files complete. No new helper or public amendment;
whole-module final profiling remains pending.
