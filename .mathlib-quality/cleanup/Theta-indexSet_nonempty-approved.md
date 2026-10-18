# Approved API revisit of original7 — `Roth.indexSet_nonempty`

The exact approved A row removes ONLY `DecidableEq σ`, by adding `omit [DecidableEq σ] in`
BEFORE the preserved docstring. Fintype σ, σ/B/hB/q/r, ordinary names, binder order and
implicitness, conclusion, public name/visibility, and the existing direct witness proof remain.
No caller, helper, import, definition, header metadata, other declaration or shared log changed.
Proof body1→1lines; source adds1line. This revisit does not increase counts:196/264overall,
Theta15/35. Other approved targets and declined hq/D/E/F extras are outside this leaf.

## Preparation and baseline

Read the leaf instructions, lean4 and mathlib-quality SKILL.md, full cleanup command,
full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates and
profiling, relevant style/naming sections, prior original7 report, exact contract decision,
and immutable baseline `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6` source.
No writes/compiler/LSP/Lean-search request occurred before RELEASE; only reads/rg preparation. Previous checkpoint
`a646c9b4393690e0c6501e9521f86cadf4b900d5` was published first.
Owner baseline full build45.375s THEN separate LeanEval15.075s both exit0, drained.
Actual before snapshot hash equals released source:
`5d7f681b2e03c3c1845e8751bb87783aab68dc21c2633bb5c9d03b95b1a46592`.
Reused exact samehash complete native baseline `/private/tmp/roth-one-api/final-lsp.json`:
success=true, partial=false, timed_out=false, failed_dependencies=[],0errors28warnings.
The target has two decidability warnings (unused section variable and unusedDecidableInType);
removing its approved binder resolves both. Cache fetch/optional standalone linter not rerun;
the module compiler and complete native diagnostics run the actual linters. File-wide phases
are owner scope; this leaf only handles the approved declaration.

## Full substantive24audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Resolve the target's two DecEq warnings through the approved omit; no suppression. Other declaration warnings remain owner scope.|
|2|HAVE SCAN|No have in the one-line witness; nothing to inline.|
|3|SET_OPTION|No source option; no raised limit or scaffolding introduced.|
|4|SIMP SQUEEZE|No simp in the target; no squeezing applicable.|
|5|NAMING|indexSet_nonempty names the nonemptiness of established indexSet; no forbidden numeric pattern or abbreviation. No rename.|
|6|LINE PACKING|The91-codepoint signature is already one line; measured table below.|
|7|BY PLACEMENT|Term body has no by wrapper.|
|8|FORMAT|Two-space body indent, no internal blank, existing ↦ lambdas remain. No haveI/letI added.|
|9|COMMENTS|No inline proof narrative; existing source-bearing docstring byte-preserved.|
|10|DOCSTRING|Protected public documentation stays anchored directly to theorem; omit precedes it.|
|11|VISIBILITY|Public status retained under exact approval. It supports two actual supremum proofs.|
|12|STRUCTURE|One anonymous constructor shares R and h across correlated outputs; no independent conjunct or >10line branch. No helper.|
|13|MATHLIB|Five actual fresh searches and clean compiled generic/automation probes below. Set image API is partial, with admissibility/coprimality still to supply.|
|14|JUNK DEF|n/a: theorem; no definition touched.|
|15|EXISTS LEMMA|Public multi-use domain theorem, not a private single-use existential wrapper. Shared witness stays shared.|
|16|SHOW/CHANGE|Neither occurs.|
|17|PUSH_NEG|Absent.|
|18|GENERALISE|Fresh compiled probes for all seven old effective binders below; only approved DecEq removal applied.|
|19|INEQUALITY|1≤B is canonical; no ≥/> relation.|
|20|NORMAL FORM|Set.Nonempty is the standard input to csSup APIs; no alternate equivalence family needed.|
|21|SYNTAX GENERALITY|Existing hB/q/r explicit ordering directly fits both callers. RSet.Nonempty abstraction assessed but not applied.|
|22|IMPORT FANOUT|n/a: zero import changes.|
|23|CASTS|Zero added/dropped cast; polynomial1 and integer numerator1 inferred in unchanged proof.|
|24|INSTANCE-NAME|n/a: no instance declaration; generated retained instance name may renumber after approved removal.|

## Measured packing and inequalities

Actual compiled width100 reference:

```
@indexSet_nonempty : ∀ {σ : Type u_1} [inst : Fintype σ] {B : ℝ},
  1 ≤ B → ∀ (q r : σ → ℕ), (indexSet B q r).Nonempty
```

|Sig line|Codepoints|Next signature token|Arithmetic|Action|
|---|---:|---|---|---|
|74|91|none; proof body next|n/a, entire signature fits one line|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none, canonical|none|
|2|whole signature|zero ≥/> relations; arrows are function syntax|n/a|none|

## Five actual fresh mathlib methods

Raw `/private/tmp/roth-index-api/searches.json`; independent successful ordinary compiler
`positive.lean` verifies the relevant returned lemma names/types. No missing index is an
absence proof, and no search result alone is a local compile guarantee.

|Method|Actual query/result|
|---|---|
|A Lean-Finder|nonempty set of indices of bounded integer multivariate polynomials using constant one and coprime numerator one → ChevalleyThm degree/numBound results, no exact match returned.|
|B Loogle|Set.Nonempty, Set.image → Set.Nonempty.image/of_image, Set.image_nonempty, image_const, image_inter_nonempty_iff.|
|C LeanSearch|the image of a nonempty set is nonempty → instNonemptyElemImage, range_nonempty, MapsTo.nonempty, Nonempty.map and category image instance.|
|D source rg|Untruncated indexSet_nonempty/Nonempty.image/nonempty_image_iff/image_nonempty in Roth and Set/Image; coprime source isCoprime_one_left. Set/Image389–398 and Coprime/Basic94 provide generic building blocks.|
|E local pattern|Nonempty.image,limit8 → empty items,index=unavailable. Explicit limitation, not absence evidence.|

Auxiliary variants searched/read: Nonempty.image/of_image, image_nonempty, image_const,
range_nonempty, MapsTo.nonempty, isCoprime_one_left. Common-equivalents table has no relevant
custom discrete/finiteness/separation predicate. Partial generic image theorem does not
supply RSet admission or coprime numerators. The existing single constructor is direct and
shorter than repackaging those witnesses through image syntax. No exact replacement is claimed
absent: bounded clean exact?/apply? failures are inconclusive. No private wrapper introduced.
No new proof identifier; omit/DecidableEq already exist in immediately preceding source.

Clean no-Theta-import prefix ends BEFORE the audited target; four anonymous examples try
grind[indexSet,one_mem_RSet], aesop, exact?, apply? with lowered2000 scratch heartbeats.
They cannot cite the target or matching failed named trials. Known repeated native multi_attempt
stalls on earlier leaves were respected: no unbounded request relaunched. Actual ordinary
compiler exploration is used; failure evidence is kept separate from successful axioms checks.

## Every effective binder: fresh compiled generalisation probes

`positive.lean` and `negative.lean` in `/private/tmp/roth-index-api` were freshly compiled.
All old effective binders are represented, including section instances. Expected failures
are separate from successful positive/original/actual-axiom probes.

|Binder|Role|Compiled drop/weakening trial|Decision|
|---|---|---|---|
|σ:Type*|Variable and q/r domains|Literal drop with autoImplicit=false rejects unknown σ; arbitrary universe-polymorphic σ succeeds in positive/retained proof.|Already general; retain.|
|Fintypeσ|Required by indexSet/index type|Drop rejects synthInstance Fintypeσ; Finiteσ plus chosen Fintype.ofFinite in conclusion/proof succeeds.|Finite restates the instance-indexed conclusion; user explicitly retains Fintype.|
|DecidableEqσ|Old inherited decidability|Direct witness now compiles without DecEq and without local classical, after approved one_mem_RSet generalization.|Approved ONLY removal applied. Actual AST absence/type/metadata checked.|
|B:ℝ|Coefficient bound in conclusion|Literal drop rejects unknown B; arbitrary real bound in positives.|Dependent value retained; abstract bound domain requires changing definitions.|
|hB:1≤B|Admits polynomial1|Drop rejects unknown hB in witness; weaken to0≤B rejects one_mem_RSet application. Positive certified counterexample shows indexSet0qr empty for Unit.|Cannot generally drop/weaken to nonnegative B; retain exact hB.|
|q:σ→ℕ|Denominator function|Literal drop rejects unknown q; arbitrary q, including zeros, succeeds in witness.|Dependent value retained; no positivity assumption exists to weaken.|
|r:σ→ℕ|Degree/index weights|Literal drop rejects unknown r; arbitrary r including zeros succeeds.|Dependent value retained; no strict hypothesis exists.|

The successful zero-bound counterexample forces every coefficient to zero from |coeff|≤0,
contradicting RSet's nonzero condition; it proves failure of nonemptiness, beyond witness failure.
No applicable algebraic parent, point-localization or strict-to-weak catalogue entry remains.
All public restatements beyond the exact A.DecEq removal stay unapplied.

Inversion: unfolding indexSet exposes only an admissible polynomial plus coprime numerators;
its specific index value is existentially inferred. Fresh compiled fromNonemptyRSet proves
nonemptiness from `(RSet B r).Nonempty` with the same numerator1. Diagnostic fires, but a
one-line helper adds plumbing and Set image API already gives the abstract principle. No
helper or public hR restatement is authorized/applied.

## Public literature

Read local clean.tex644–671: source explicitly permits polynomial1 with every numerator1.
The surrounding paper assumes positive r/q and positive finite m for later estimates; this
witness does not need positivity and already covers arbitrary existing finite σ, including empty.
Fresh WebSearch queries: `Roth polynomial index supremum constant polynomial one nonempty
generalization Takloo Bighash Yin`; `Roth theorem index polynomial constant one supremum
nonempty generalization`. Top results of first: polynomial extremal problems, Shalika–
Takloo-Bighash–Tschinkel rational-points paper, Takloo-Bighash bounded-height paper; these
are not evidence for a new local API. Second: generalisation-of-Roth article, Roth overview,
and [Vojta's primary exposition](https://math.berkeley.edu/~vojta/ftp/cime.pdf); also
[AMS chapter4](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) and
[Min Ru notes](https://www.math.uh.edu/~minru/fields/roth.pdf). Primary Roth1958 ICM search
excerpt defines weighted derivative index; opening its full PDF returned Internal Error,
so no claim is based on unseen content. Broad Diophantine generalisations do not themselves
prove an exact local contract extension. Local source plus compiled probes justify this
scoped removal. ChatGPT math MCP unavailable (no exposed matching tool); no invocation claimed.
No literature-driven additional live change.

## All42golfing rules: fresh assessment

|Rule|Concrete status|
|---|---|
|1.1 by-exact|n/a: already direct term.|
|1.2 by-rfl|n/a: no wrapper.|
|1.3 rw/exact|n/a: no tactic chain.|
|1.4 simp/exact|n/a: no simp.|
|1.5 trailing rfl|Essential equality field of existential, not a trailing tactic; keep.|
|1.6 constructors|Already one anonymous constructor.|
|1.7 apply/exact|n/a: no tactic chain.|
|1.8 by_contra|n/a: absent.|
|1.9 eta|Constant functions are not eta-redexes; existing ↦ retained.|
|1.10 have|n/a: absent.|
|1.11 apply/intro|n/a: absent.|
|1.12 show|n/a: absent.|
|1.13 projections|n/a: absent.|
|1.14 rw merge|n/a: absent.|
|1.15 terminal simp|n/a: absent.|
|1.16 nonterminal simp|n/a: absent.|
|1.17 dot notation|No useful dot-notation replacement for one_mem_RSet hB r.|
|1.18 parens/<||No unnecessary application parentheses.|
|1.19 push_neg|n/a: absent.|
|1.20 exists inline|Public two-caller domain theorem; no private single-use wrapper.|
|2.1 grind|Actually compiled clean anonymous whole-proof trial, failed witness synthesis.|
|2.2 grind predecessors|n/a: no grind in retained proof.|
|2.3 simpa|No simp chain; direct term already closes.|
|2.4 fun_prop|n/a: no analytic function property.|
|2.5 positivity|n/a: target is set nonemptiness.|
|2.6 gcongr|n/a: no inequality assembly.|
|2.7 lia/omega|n/a: no Nat/Int arithmetic goal in direct witness.|
|2.8 aesop|Actually compiled clean anonymous trial, failed no progress.|
|2.9 norm_num/cast|n/a: no numeric calculation or cast goal.|
|2.10 decide|n/a: arbitrary real bound and polynomial existence, no finite computation.|
|2.11 field_simp/ring|n/a: no algebraic identity.|
|2.12 linear_combination|n/a: no ring terminator or identity hypotheses.|
|2.13 wlog|n/a: no symmetric cases.|
|2.14 calc|n/a: no calc chain.|
|2.15 <;>|n/a: direct term, no open tactic subgoals.|
|3.1 erw|n/a: absent.|
|3.2 continuity|n/a: absent.|
|3.3 omega/lia|n/a: absent.|
|3.4 rcases/rfl|No rcases; final term rfl essential.|
|3.5 attributes|No global attribute added; changes to normal forms outside exact approval.|
|3.6 simp_all|n/a: absent.|
|3.7 options|No source option present or added.|

Step-back reflection: direct mathematical witness is concise/deterministic; a different image
proof adds plumbing, and automation must still invent the same admissible polynomial/numerator.
Fresh exact?/apply? probes are anonymous and uncontaminated; bounded failure is inconclusive.
One-line proof has no helper extraction benefit. Approved removal needs only scoped omit.

## Simplify pass

Manual equivalent review because no callable built-in simplify tool is exposed: PASS-THROUGH.
No duplicate skeleton, single-use have, wrapper, cast or helper issue. No further source edit.
Phases5a/5b: no refactoring or rename, no queue/shared log written. Optional abstract/Finite
restatements assessed/unapplied; no helper needing fresh dedicated audit.

## Verification and exact original contract

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0; raw
`/private/tmp/roth-index-api/module.log` ends Build completed successfully (2423jobs).
This is the leaf's module gate, not the owner-only final full-build/LeanEval gates.
Fresh probes use `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-index-api/NAME.lean`:

|NAME|Exit|Wall seconds|Accepted evidence|
|---|---:|---:|---|
|actual-compatibility (first draft)|1|32.180|Rejected: ambiguous anonymous Fintype term timed out during elaboration; no limit raised.|
|actual-compatibility (corrected final)|0|not separately timed|Accepted full-old adapter/AST/metadata/actual and independent axioms; raw actual-compatibility-final.log.|
|callers|0|22.876|Both immutable original caller proofs and actual public types/BinderInfo/axioms.|
|positive|0|22.937|No-DecEq witness, Finite restatement, inversion candidate, zero-bound counterexample and lemma #checks.|
|negative|1|29.412|Expected binder drop/weakening failures, not pass/axiom evidence.|
|automation|1|35.592|Expected clean grind/aesop failure and bounded exact?/apply? inconclusive timeouts.|

The corrected final compatibility artifact independently copies baseline RSet/indexSet,
one_mem_RSet and indexSet_nonempty proofs into IndexApiOriginal. The old proof does NOT
invoke the current theorem. Baseline text was extracted directly from immutable
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`, saved in immutable-original-source.lean;
independent namespace uses the original declarations, not weakened currentRoot types.

The explicit kernel-checked old telescope adapter to ACTUAL BUILT new target is:

```
fun {σ : Type _} [f : Fintype σ] [DecidableEq σ] {B : ℝ}
    (hB : 1 ≤ B) (q r : σ → ℕ) ↦ @Roth.indexSet_nonempty σ f B hB q r
```

Its equality with the independent original theorem checks by rfl/proof irrelevance at the
same old proposition. Direct getConstInfo.type comparisons check its exact old seven-binder
type and the actual six-binder retained type, modulo universe alpha-alignment. AST checks
forbid DecidableEq throughout the actual type and require Fintype. All retained ordinary
names/order/BinderInfo agree; anonymous instance names are exempt from name equality only,
as required by Lean's generated-name renumbering, while exact class/type/order/BinderInfo
remain checked. Actual metadata is σ implicit, Fintype instImplicit, B implicit, hB/q/r default.
Direct retained type comparison checks dependent argument types and conclusion as well.
Actual compiled original/actual/adapter/retained axiom sets are exactly
`[propext, Classical.choice, Quot.sound]`; all outside that set are programmatically rejected.
The initial failed scratch sample is not used as pass evidence; only the corrected final
exit0 run certifies the adapter and axioms. No source workaround or limit change occurred.

Repository-wide source inventory finds exactly TWO actual uses of indexSet_nonempty, both
inside Theta: Θ_le_of_forall_index_le and Θ_mono. No external direct caller. Both original
baseline proof bodies are freshly copied and compiled invoking actual revised target; direct
actual public type comparisons and BinderInfo checks include all implicit section instances.
Their actual and copied axiom sets are standard. No caller source edit needed.

Fresh COMPLETE UNFILTERED native `lean_diagnostic_messages(file_path="Roth/Theta.lean")`
returned success=true, partial=false, timed_out=false, failed_dependencies=[],0errors27warnings.
Raw final-lsp.json; diagnostic-delta.json compares message/severity multisets (lines shift+1).
Exactly the two target DecEq warnings disappear. Exactly one newly exposed unused-section
DecEq warning appears in Θ_le_of_forall_index_le, whose old public contract is preserved by
compiled direct metadata/type comparison; its own approved revisit comes later. All other
warnings remain unchanged, including protected header and hypotheses outside this leaf.
No suppression or unrelated public edit was used to hide them.

Exact focused.diff plus a programmatic string-transform assertion proves the entire source
change is just the one approved omit line. Original docstring and proof are byte-preserved.
No new identifier hallucination: the only added identifiers DecidableEq/σ already exist in
local scope and exact preceding omit syntax. No sorry/new axiom/native_decide/profiler source
scaffolding or heartbeat raise; none of the expected scratch failures is counted as a proof.

## Buzz pass — FAST-BOARD (exact-prefix only)

All ordinary module/probe/search/LSP requests had completed before either accepted profile;
no other compiler or LSP request was launched during the sequential before/after profiles.
Both prefix files preserve every exact preceding import/source/context, stop immediately
after target and append `end Roth`. Before snapshot hash is the owner's released hash.
Actual command for each phase:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-index-api/PHASE-prefix.lean`.
Both exited0, before wall35.200s and after wall31.115s. Raw UTF8 logs before-profile.log and
after-profile.log; profile-status.json and profile-summary.json retain measured evidence.

|Phase|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|Raw anchor|
|---|---:|---:|---:|---:|---:|---:|
|before|1.446ms|7.434ms|1.698ms|4.559ms|15.137ms|35167|
|after|1.910ms|6.690ms|1.601ms|4.444ms|14.645ms|35582|

Only top-level target command plus associated top-level async proof/addDecl/linter nodes
are summed; nested kernel/tactic/Meta children are not double-counted. Budget1000ms; neither
sample approaches750ms, so no borderline repeat required. No performance improvement claim
is made for this small API removal. No scaffold/limit raise or deferral; raises removed0,
added0. Whole-Theta profiling is NOT certified by a prefix; final owner whole-module sweep
remains required after known late index_le_lem6 default-heartbeat cleanup.

## Eleven leaf gates

|Gate|Result/evidence|
|---|---|
|lake_build_file|PASS, actual lake build Roth.Theta exit0, module.log.|
|definition_protected|PASS, exact source transform adds only one omit before target; zero def/abbrev changes.|
|theorem_statement_protected|PASS under exact approved A row: actual7→6 binder adapter removes ONLY DecEq; retained type/AST/metadata and original independent proof checked.|
|structure_gate|PASS,1bodyline, shared correlated existential witness; no long branch/helper.|
|naming_gate|PASS, descriptive indexSet_nonempty without forbidden pattern/abbreviation; no rename.|
|line_packing_gate|PASS, measured91-codepoint sole signature line with complete table.|
|inequality_orientation_gate|PASS, canonical1≤B, zero ≥/> relations.|
|cumulative_no_unintended_breakage|PASS at leaf scope: both independent old callers compile against actual revised theorem, original actual public types/BinderInfo/standard axioms verified; module and live LSP pass. Owner full/LeanEval pending.|
|independent_original_contract|PASS, immutable nonself original proof plus explicit full-old telescope λ→actual new target; corrected final exit0.|
|standard_axioms|PASS, actual built/original/adapter/retained and both actual/copied callers only propext/Classical.choice/Quot.sound.|
|buzz/no_scaffolding|PASS,14.645ms exact-prefix aggregate, all requests drained, no scaffold/raise.|

Overall leaf gates PASS with the unrelated/protected and newly exposed future-target warnings
explicitly documented. Owner-only cumulative full build THEN separate LeanEval remain pending;
this report does not claim those new-source gates have run.

## Eleven-step phase checklist

1. ✓ Required skills/full workflow/core references and scoped preparation.
2. ✓ Substantive24audit with concrete statuses.
3. ✓ Five fresh actual mathlib methods; unavailable/failed paths recorded without absence claim.
4. ✓ All seven old effective binders freshly compiled/probed; literature and inversion checked.
5. ✓ Complete per-signature-line measured packing table.
6. ✓ Complete per-occurrence inequality table.
7. ✓ All42golfing rules explicitly assessed; clean automation actually compiled.
8. ✓ Step-back alternative proof review and manual simplify equivalent pass.
9. ✓ Fresh complete unfiltered native final diagnostics:0errors27warnings, exact delta documented.
10. ✓ Eleven gates including actual module, original adapter/metadata, actual standard axioms and uncontended real profiles; owner full/separate LeanEval pending.
11. ✓ No rename/helper/shared-log write; documentation/proof preserved; source frozen/revoked.

Source edits are FROZEN and REVOKED; no further source edit authorized to this leaf.
Final Roth/Theta.lean SHA256:
`6163ff1d8e0d00c5f916828e53f4aed5b4fc28a36f35bdcb1f8fab48db973980`.
All leaf compiler/probe/profile/LSP/search requests have terminal completed results; no orphan
session. Only repository sidecar written is this report; no Git mutation/shared report/
rename queue/learning log edit. Source unchanged through final SHA verification.


## Owner cumulative publication gates

After leaf freeze/revocation and drained requests, owner ran `lake build` followed by separate
`lake build Roth.LeanEval`: both exited 0, in 53.182 s and 12.704 s.
Theta SHA256 `6163ff1d8e0d00c5f916828e53f4aed5b4fc28a36f35bdcb1f8fab48db973980` was identical before and after both commands.
Raw logs: `/private/tmp/roth-theta-r07-full.log` and `/private/tmp/roth-theta-r07-leaneval.log`; machine record
`/private/tmp/roth-theta-r07-builds.json`. These completed owner gates supersede the
leaf's earlier pending cumulative entries. Exact-path staging, commit and successful push publish
this approved revisit before the next source edit. This revisits original 7; original counts
remain Theta 15/35, overall 196/264, 9/14 files. No new original or helper is counted.
