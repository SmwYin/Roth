# Dedicated original11 cleanup — `Roth.Θ_le_card`

Scope: this public theorem only. Use `Real.sSup_le` to bound the supremum directly,
including its empty-set case, and use the canonical `degreeOf` unfolding for the mapped
polynomial bound. Preserve every original public hypothesis, instance, binder order,
implicit/explicit status, name, visibility and source-bearing docstring. No caller,
helper, import, definition, header or shared-log mutation. No Git mutations.

Physical proof-body counts, excluding signature lines and declaration-separator blanks:
original baseline4, live-start6, final5. The original4 used two subsequently deleted
private wrappers; their direct mathlib replacements were already in live-start6.
This leaf removes one body line from live-start. Declaration8→7physical lines.

## Preparation and baseline

Read the complete leaf instructions, lean4/mathlib-quality skills and cleanup workflow;
full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns and cleanup-gates;
relevant style, naming and profiling sections. Prepared read-only until owner RELEASE.
Original10 owner checkpoint: full build88.364s THEN separate LeanEval25.958s, both exit0,
committed/pushed3dc739abcf1291966e13b8223bdadc3bdad195ff. Starting Theta SHA256
`b38cacf9d85ab62c485804d7848d92e8d7a4ef2145b05c32dc57f0eab0c4fd34`.
Identical-source baseline native complete diagnostics reused from
`/private/tmp/roth-theta-nonneg-final-lsp.json`: success=true,partial=false,timed_out=false,
0errors31warnings. Final owner full project THEN separate LeanEval gates are pending
and are not claimed here.

## Full substantive24audit

|#|Item|Concrete finding/action|
|---|---|---|
|1|LINT|Original hr/DecEq warnings protected. Canonical proof exposes hB-unused and auto-included DecEq-unused; final0errors33warnings, no suppression or API change.|
|2|HAVE SCAN|No have in original/live-start/final target proofs; no single-use intermediate.|
|3|SET_OPTION|None in target; no source limit raised. Isolated expected-failure automation uses lowered2000heartbeats.|
|4|SIMP SQUEEZE|One terminal simpa membership-degree subgoal; keep explicit unfolding lemmas, no nonterminal bare simp or terminal simp-only list.|
|5|NAMING|Θ_le_card describes a cardinal upper bound for established Θ; no forbidden abbreviation, numeric scheme, single-letter declaration or rename.|
|6|LINE PACKING|Both signature lines measured below; moving complete conclusion to preceding line gives115codepoints.|
|7|BY PLACEMENT|by remains at end of conclusion line.|
|8|FORMAT|2-space tactics/4-space signature continuation, no internal blank line or haveI/letI; direct simp argument now on by line.|
|9|COMMENTS|Target had zero inline proof comments. Original source-bearing one-line docstring preserved byte-for-byte.|
|10|DOCSTRING|Public result/source claim remains accurate, no unauthorized rewrite.|
|11|VISIBILITY|Public headline result named in module main-results, retained; no actual callers does not authorize deleting a public theorem.|
|12|STRUCTURE|Final headline body5lines≤15; no conjunction conclusion or >10line branch. Shared R/h witnesses unpacked together.|
|13|MATHLIB|All5actual searches below; use Real.sSup_le and direct mapped-degree mathlib terms. No new wrapper/helper.|
|14|JUNK DEF|n/a, theorem.|
|15|EXISTS LEMMA|n/a, public inequality rather than private trivial existential helper.|
|16|SHOW/CHANGE|None in selected proof.|
|17|PUSH_NEG|None.|
|18|GENERALISE|All8actual effective binders covered by compiled drop/weakening probes below; no public amendment applied.|
|19|INEQUALITY|hB1≤B, hr0<rj and Θ≤card all canonical; table below.|
|20|NORMAL FORM|Direct upper-bound formulation Θ≤card and Real.sSup_le are canonical. No normal-form attribute changed.|
|21|SYNTAX GENERALITY|Five-binder no-hB/no-hr/no-DecEq candidate compiled with exact actual-old-type adapter; report-only pending fresh root/user decision.|
|22|IMPORT FANOUT|n/a, no import added.|
|23|CASTS|New Nat.cast_nonneg proves genuine ℕ→ℝ bound. Kept Int.castRingHom ℝ ascription fixes map codomain; no redundant same-type cast introduced.|
|24|INSTANCE-NAME|n/a, no instance declaration introduced or renamed.|

## Measured signature packing and inequality scan

Actual width100 `#check @Roth.Θ_le_card` and direct actual type checks are in
`/private/tmp/roth-theta-card-original.log`. The effective original type has exactly
σ/Fintypeσ/DecidableEqσ/B/hB/q/r/hr, in that order.

|Sig line|Codepoints|Next complete signature token|Arithmetic|Action|
|---|---:|---|---|---|
|102|84|`Θ B q r ≤ Fintype.card σ := by`30chars|84+1+30=115>100|ok|
|103|34|none, proof next|n/a|ok|

|#|Location|Occurrence|Rewrite|Rename|
|---|---|---|---|---|
|1|hB|1≤B|none, canonical|none|
|2|hr|0<rj|none, canonical|none|
|3|conclusion|ΘBqr≤cardσ|none, canonical|none|
|4|whole signature|zero ≥ or > relations; → is function syntax|n/a|none|

## Five actual mathlib searches

Raw native results: `/private/tmp/roth-theta-card-search.json`.

|Method|Actual query and result|
|---|---|
|A Lean-Finder|A real supremum is at most a nonnegative upper bound, including empty sets → exact Real.sSup_le, Real.iSup_le, Real.sSup_nonneg'.|
|B Loogle|`sSup ?s ≤ ?a` → generic sSup_le, sSup_le_iff and sSup_le_sSup; complete-lattice assumptions differ from real conditional completeness.|
|C LeanSearch|real supremum is less than or equal to nonnegative bound for all elements → exact Real.sSup_le and Real.iSup_le.|
|D source rg|Untruncated searches sSup_le/csSup_le over real/conditionally-complete sources; local Real.sSup_le inspected in Algebra/Order/Archimedean/Real/Basic.lean218–231. degrees/degreeOf_def/map sources also inspected.|
|E local name|sSup_le limit12 → Real.sSup_le plus generic variants; index unavailable, source hits valid, no absence inference.|

Auxiliary variants: csSup_le, csSup_le_iff, sSup_le_iff, Real.iSup_le,
Real.sSup_empty, Real.sSup_of_not_bddAbove. Common equivalents: supremum/order bucket.
Presence established; no claim of mathematical absence. Real.sSup_le is generic supremum
infrastructure, while the concrete membership callback establishes the domain-specific
index bound. Existing public theorem is protected; no new generic wrapper is introduced.
Previously deleted private mapped-polynomial wrappers remain deleted.

Compiled target-free native automation file `/private/tmp/roth-theta-card-trials.lean`
contains the exact preceding imports/context/definitions, excludes target Θ_le_card and
all later theorems, then gives distinct trial declarations. Native raw result
`/private/tmp/roth-theta-card-trials.json`: grind[Θ,indexSet], simp[Θ], aesop and gcongr
fail; exact?/apply? reach conservative2000heartbeats and are inconclusive. This expected
failure batch is neither axiom certification nor absence proof. Repeated known full-Theta
multi_attempt stalls from prior leaves were not retried. Initial scratch declaration/doc
and scope syntax was repaired; the saved final trial has no syntax errors. A scratch-only
unscoped lowered-limit linter warning is harmless and no limit option exists in live source.

## Every effective binder — compiled probes

Positive actual-import `/private/tmp/roth-theta-card-original.lean` exited0; standard axioms
for actual, independent original, candidate, adapter and callers are checked separately
from expected-failure files. Negative `/private/tmp/roth-theta-card-negative.lean` exited1
as expected; autoImplicit=false prevents silent reintroduction of dropped data binders.

|Binder|Class and use|Compiled mechanical evidence|Decision|
|---|---|---|---|
|σ:Type*|Index type in functions/Θ/card|Literal drop errors unknownσ; positive proofs/candidate and actual-old identity are arbitrary-universe.|Already universe-polymorphic; retain.|
|Fintypeσ|Θ/index definitions and cardinal target|Literal drop fails Fintype synthesis in both Θ/card. Finiteσ version reconstructing Fintype.ofFinite in conclusion/proof compiles.|Reconstruction is a public restatement; unapplied.|
|DecidableEqσ|Original effective section instance, original degreeOf_def route|Candidate without DecEq compiles using degreeOf; AST rejects any remaining DecEq binder. Original-style bare degreeOf_def route cannot rewrite mapped degrees without decidability.|Existing optional menu unapproved; retain original actual binder.|
|B:ℝ|Coefficient bound in Θ|Literal drop errors unknownB. Candidate proves bound for arbitrary realB.|Dependent data retained; abstract codomain would restate underlying definitions.|
|hB:1≤B|Original nonempty-set argument|Original-style drop errors unknownhB; drop_hB/weak_hB0≤B and unrestricted candidate compile.|New genuine stronger candidate, unapplied.|
|q:σ→ℕ|Denominator function in Θ|Literal drop errors unknownq; positive proof works for arbitraryq without q-positive assumptions.|Dependent data retained.|
|r:σ→ℕ|Degree/weight data in Θ|Literal drop errors unknownr; positive proof works for arbitraryr.|Dependent data retained.|
|hr:∀j,0<rj|Already unused in original upper-bound proof|drop_hr/weak_hr0≤rj and simultaneous unrestricted candidate compile.|Existing optional menu unapproved; retain.|

All effective parameters are included. Other catalogue parent-class, strict→weak,
point-localisation and universe changes are inapplicable to dependent data for these fixed
project definitions; hB/hr strict/weak and finiteness/decidability candidates are explicitly
compiled. No statement, visibility, binder-info or hypothesis alteration was applied.

## Public literature and inversion

Local clean.tex644–669 defines Θ with B≥1 and positive r/q, then bounds every polynomial
index by the variable count using a nonzero Taylor derivative of bounded weight. It also
uses polynomial1 for nonemptiness. The current Lean definitions totalize division and real
suprema; the upper bound remains true with arbitrary B and zero r entries.

Actual WebSearch queries: `supremum upper bound nonnegative empty real set Lean mathlib
Real.sSup_le` and `Roth theorem index polynomial number variables upper bound index`.
First query's first three documented hits are mathlib3 real.Sup_def docs, mathlib add-combi
Real.Basic docs, and Lean-Asymptotic-Statistical-Theory Real.Archimedean docs. Roth query
returns Min Ru's Roth notes, Princeton diophantine notes, and Roth's ICM proceedings among
relevant hits, mixed with generic-set/unrelated Roth search noise; no generality claim
was inferred from snippets. Primary
[mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Archimedean/Real/Basic.html),
[Princeton notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf) and
[Min Ru notes](https://www.math.uh.edu/~minru/fields/roth.pdf) were opened. Mathlib's
Real.sSup_le explicitly includes empty sets through sSup∅=0 and a nonnegative bound.
The generalisation is certified against actual Lean definitions, not asserted as a
classical real supremum for empty sets. No exposed ChatGPT math MCP was available.

Inversion fires: after applying Real.sSup_le the proof is a generic upper-bound callback;
Θ disappears. Its abstract content is exactly the existing theorem
∀s:Setℝ,∀a:ℝ,(∀x∈s,x≤a)→0≤a→sSup s≤a. The concrete callback uses index_le_card and
invariance of degree under the injective integer cast. Existing generic API suffices;
no abstract helper/public wrapper needs extraction. This justifies the compiled stronger
proposal without authorizing a live signature edit.

## Concrete stronger candidate — UNAPPLIED

`Stronger11.candidate` imports actual Roth.Theta definitions and has exactly this signature:

```lean
theorem candidate {σ : Type*} [Fintype σ] {B : ℝ} (q : σ → ℕ) {r : σ → ℕ} :
    Θ B q r ≤ Fintype.card σ := by
  refine Real.sSup_le ?_ (Nat.cast_nonneg _)
  rintro _ ⟨R, ⟨hR0, hRd, -⟩, h, -, rfl⟩
  exact index_le_card ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR0)
    (by simpa [degreeOf, degrees_map_of_injective R (f := Int.castRingHom ℝ)
          Int.cast_injective] using hRd) _
```

Definitive `/private/tmp/roth-theta-card-original.lean` exit0 checks candidate AST exactly
σ(implicit)/Fintype(instance)/B(implicit)/q(explicit)/r(implicit), rejecting hB/hr/DecEq.
The explicit lambda `adapter` accepts all8original parameters including DecEq/hB/hr and
invokes candidate q. Kernel rfl identity with actual Roth.Θ_le_card and direct
getConstInfo.type comparison (aligned universe parameters), plus equal BinderInfo/order,
all pass. Actual built target/candidate/adapter/caller_named/caller_inferred/caller_old
have only propext, Classical.choice and Quot.sound.

Full project `rg -n Θ_le_card Roth` inventory: declaration and module-doc mention only;
zero actual routine or external callers. Named/inferred prospective calls to candidate
and a fully typed original-shape call to adapter compile against actual project definitions.
No caller was changed. This expands beyond the pending DecEq/hr-only menu by additionally
removing hB; fresh root/user decision is required. All existing live hypotheses remain.

## All42golfing rules

|Rule|Concrete status|
|---|---|
|1.1 by-exact|No redundant wrapper; selected proof has substantive tactics.|
|1.2 by-rfl|None.|
|1.3 rw/exact|No rw chain.|
|1.4 simp/exact|Single terminal simpa already combines degree normalization and exact hRd.|
|1.5 trailing rfl|None; membership rfl pattern performs needed equality substitution.|
|1.6 constructors|No constructor tactics; correlated witnesses unpacked together.|
|1.7 apply/exact|refine supplies upper-bound callback and nonnegative cardinal bound; direct index_le_card alone does not prove supremum goal.|
|1.8 contra/push|No contradiction.|
|1.9 eta|No eta-redex lambda.|
|1.10 single-use have|None.|
|1.11 apply/intro|No separate apply/intro chain; membership unpacking remains clear rintro.|
|1.12 show|None.|
|1.13 have projections|No have/projection pair.|
|1.14 merge rw|None.|
|1.15 terminal simp|No terminal simp-only; terminal simpa must name domain-specific normalization.|
|1.16 nonterminal simp|None.|
|1.17 dot notation|Existing .2 hR0 injectivity application appropriate. No useful dot rewrite.|
|1.18 trailing parentheses|Remaining mapped-degree proof parentheses are one of several positional arguments; <| would consume remaining argument.|
|1.19 push_neg|None.|
|1.20 exists helper|No private existential helper.|
|2.1 grind|Actual target-free grind[Θ,indexSet] fails.|
|2.2 delete before grind|No retained grind.|
|2.3 simpa|Mapped-degree terminal simpa retained; canonical degreeOf unfolding succeeds in compiled selected/candidate proofs.|
|2.4 fun_prop|n/a, no analytic regularity target.|
|2.5 positivity|Nat.cast_nonneg directly proves auxiliary nonnegativity; overall target is an upper bound, no positivity target to replace.|
|2.6 gcongr|Actual target-free whole-proof gcongr makes no progress.|
|2.7 lia/omega|n/a, no Nat/Int linear arithmetic target.|
|2.8 aesop|Actual target-free aesop fails.|
|2.9 norm_num/cast|No concrete calculation; genuine Nat→ℝ cast handled by direct standard theorem.|
|2.10 decide|n/a, arbitrary real inequality, no finite computation.|
|2.11 field_simp/ring|n/a, no algebraic identity goal.|
|2.12 linear_combination|n/a, no ring-ending proof or polynomial certificate.|
|2.13 wlog|n/a, no symmetric cases.|
|2.14 calc|No two-step calc.|
|2.15 multiple goals|Different semantic obligations: callback and bound nonnegativity, no duplicated goals.|
|3.1 erw|None.|
|3.2 continuity|None.|
|3.3 omega/lia|None, arithmetic rule inapplicable.|
|3.4 rfl substitution|Applied directly in rintro; no redundant subsequent equality rewrite.|
|3.5 attributes|No new simp/grind normal form needed or authorized.|
|3.6 simp_all|None.|
|3.7 limits|No live source limit to remove/raise.|

Step-back reflection: Real.sSup_le eliminates the unrelated nonemptiness argument and its
hB dependency. index_le_card already handles zero weights via the fixed index definition;
no hr is needed. The callback remains a direct project-specific polynomial bound, so a
single generic automation tactic is inferior. Exact?/apply? were inconclusive under the
lowered conservative budget. No missing abstract API, independent long branch or useful
new helper was found.

## Verification and gates

Actual `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0,2423jobs;
raw `/private/tmp/roth-theta-card-module.log`.
Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-theta-card-original.lean`
exited0. Original baseline2b64544bf9f77a8ff957bf1bcaf693ac72217ff6 definitions, prerequisites,
deleted private-wrapper proofs and target proof are copied into namespace Original11;
its target proof never invokes current Roth.Θ_le_card. Original and actual built types are
checked directly through getConstInfo.type with aligned universes and BinderInfo checks;
standard3axioms printed for both. The same successful artifact certifies the actual-import
candidate, full explicit old-type adapter, AST and prospective callers. Early scratch
missing-import/reserved-local-name errors were corrected before this successful run;
no failed run is used as trust evidence.

Fresh COMPLETE unfiltered native live Roth/Theta.lean diagnostics:
success=true,partial=false,timed_out=false,failed_dependencies=[],0errors33warnings.
Raw `/private/tmp/roth-theta-card-final-lsp.json`. Baseline31 plus2new target warnings:
unused hB and automatically included unused DecEq. Existing hr and unusedDecidableInType
warnings persist. All are deliberately protected pending explicit API decision; no
suppression or underscore renaming. Native live lean_goal at104 confirms original8binder
context and transition from Θ≤card to ∀x∈indexSet,x≤card.

Exact immutable start/final comparison proves only this target proof changed; full signature
and all remaining source identical. Focused `/private/tmp/roth-theta-card-focused.diff`.
No target narrative comments existed; source docstring exact. No sorry, new axiom,
native_decide, limit increase or source profiling scaffolding. No new helper audit required.

|New identifier|Verification|Result|
|---|---|---|
|Real.sSup_le|Actual local search/source inspection/native candidate/module/compiled generic example|pass|
|Nat.cast_nonneg|Actual local search source hit (index error), compiled candidate/module/original-adapter artifact|pass|
|degreeOf|Existing declaration in source; native #check and compiled degree-normalization proof|pass|

|Gate|Result|Evidence|
|---|---|---|
|lake_build_file|pass|Actual lake build Roth.Theta exit0, module log.|
|definition_protected|pass|No definition/abbrev/import change, exact focused comparison.|
|theorem_statement_protected|pass|Header text exact and actual old getConstInfo.type/BinderInfo equality, DecEq retained.|
|structure_gate|pass|Headline proof5lines≤15, no conjunction conclusion/long branch.|
|naming_gate|pass|Descriptive Θ_le_card, no forbidden pattern/abbreviation.|
|line_packing_gate|pass|Both signature rows measured,115overflow justifies break.|
|inequality_orientation_gate|pass|All3occurrences smaller-side-left; zero ≥/>.|
|diagnostics|pass|Fresh complete unfiltered native0errors33warnings, protected warnings documented.|
|trust_basis|pass|Actual built and independent original/candidate/adapter/callers standard3axioms only.|
|comments_and_scope|pass|Original docstring exact, zero proof comments removed, exclusive target proof edit.|
|performance|pass,prefix-only|153.288ms before/155.638ms final; exact-prefix sequential trace aggregation below.|

Overall: worker gates pass. Owner full project
THEN separate LeanEval checkpoint pending; not asserted by this leaf.

Simplify pass — PASS-THROUGH. Direct holistic review found no further reuse, readability,
independence or missing-API issue. Built-in Skill/simplify invocation is not exposed here;
review performed directly, not attributed to an unavailable tool. Phase5a: canonical
mathlib API used directly; stronger candidate remains UNAPPLIED. Phase5b: no rename
required/queued, shared sidecar untouched. File-wide phases remain owner responsibilities.

## Eleven-step phase checklist

- [✓] Step1 required references read.
- [✓] Step2 full24audit printed above.
- [✓] Step2.5 all5actual mathlib searches and auxiliary variants recorded.
- [✓] Step2.6 all8effective binders compiled probes plus public literature/inversion.
- [✓] Step2.7 every signature line measured with arithmetic.
- [✓] Step2.8 per-occurrence inequality table.
- [✓] Step3 all42golfing rules have concrete statuses.
- [✓] Step4 independent step-back/direct simplify reflection.
- [✓] Step5a fresh COMPLETE unfiltered native final diagnostics.
- [✓] Step5b focused diff/type/module/trust gates; performance completed below before freeze.
- [✓] Step6a no rename required/queued, shared sidecar untouched.


## Buzz — FAST-BOARD (exact-prefix only)

Immutable before/final exact source prefixes preserve every preceding import/context/source,
end immediately after this target and append end Roth. Sequential uncontended actual commands:
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 /private/tmp/roth-theta-card-{before,final}-prefix.lean`.
Both exit0; all earlier compiler/native/module requests drained before profiling, no overlapping
profile or independent compiler request. The supplied Lean4.34 trace command is used rather
than the obsolete -Dprofiler=true spelling in the reference.

|Target|Outer command|Async proof|Async addDecl/kernel|Async linter|Aggregate|
|---|---:|---:|---:|---:|---:|
|before|4.755ms|138.490ms|5.386ms|4.657ms|153.288ms|
|final|5.368ms|142.513ms|3.116ms|4.641ms|155.638ms|

Raw UTF8 `/private/tmp/roth-theta-card-{before,final}-profile.log`; declaration outer anchors
77796/77782. `/private/tmp/roth-theta-card-profile-summary.json` records every counted
anchor. Aggregate includes outer command and associated top-level async proof/addDecl/linter;
nested tactic/Meta/kernel nodes not double-counted. Both far below750ms/1000msbudget, so no
borderline repeat. Difference is ordinary run noise, no speedup claim. No limit raise or
profiling scaffolding added. These are prefix-only measurements: wholeTheta late
index_le_lem6 profiling failure remains owner's cleanup obligation. No whole-file profile
success is claimed. Buzz workflow executed directly with real compiler traces; no unavailable
Skill-tool invocation claimed.

## Final freeze

Final Theta source SHA256
`1db9c6a343176b8aa3c95568a5ffeeb51d7cc992c7191a0d4a7900061af6d6de`.
Exact source comparison confirms only the target proof changed, original public signature/doc
and all remaining source identical. Final prefix checked equal to exact final source through
target. All native/search/compiler/module/profile requests awaited and drained. Source editing
authority frozen/revoked. No subsequent source edits authorized by this leaf. Owner full
project THEN separate LeanEval checkpoint remains pending. No Git/shared-log/queue mutation;
no new helper. The stronger no-hB/no-hr/no-DecEq candidate remains UNAPPLIED pending a fresh
root/user decision, regardless of its successful independent compilation.

## Owner frozen checkpoint gates

All leaf requests drained and source authority revoked before owner checks. Source SHA256
`1db9c6a343176b8aa3c95568a5ffeeb51d7cc992c7191a0d4a7900061af6d6de` stayed unchanged through
sequential `lake build` (exit0,69.923s) THEN separate `lake build Roth.LeanEval` (exit0,21.839s).
Raw `/private/tmp/roth-theta-d11-{full,leaneval}.log`; structured hashes/outcomes/timing
`/private/tmp/roth-theta-d11-builds.json`. Exact-path staging, commit and successful cleanup-branch
push precede the next original declaration edit. After publication:Theta11/35 originals,
overall192/264,9/14files complete. Verified new proposalE is reviewable in the shared contract
menu, remains UNAPPLIED; no public amendment/caller change/helper. One prior report attribution
was corrected from owner-progress to leaf-progress; its accepted metric/source are unchanged.
Whole-module final profiling and late default-heartbeat repair remain pending.
