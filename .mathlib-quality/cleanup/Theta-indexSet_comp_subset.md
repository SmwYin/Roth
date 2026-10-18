# Cleanup — `Roth.indexSet_comp_subset` (original14)

Private target only, scoped omit at `Roth/Theta.lean:127`, declaration at128. Original baseline
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`; immediate checkpoint13 parent
`1ca2873855c5200fb62f203694821159b7f5bf2e`.

The witness transport now uses `rename_eq_zero_iff_of_injective`,
`Finsupp.mapDomain_surjective`, and terminal simplification of `index_rename`.
Both private decidable-equality instances were removed: explicit τ binder deleted and
section σ instance omitted locally. Compiled caller-contract3 shows the unchanged public
`Θ_equiv` independently retains both original instances with identical type and BinderInfo.
No caller proof, public declaration, comment, import, definition, or visibility changed.
No new helper was added. Declaration:18 →14 lines plus one local omit command; body:16 →12 lines; file:977 →974.

## Baseline and scope

- Read both skills, full cleanup command, all five mandatory references, relevant style/naming
  sections, full profiling reference, and buzz command.
- Prepared read-only until the owner's explicit RELEASE after checkpoint13 push; no Lean,
  scratch/report write, or source mutation preceded RELEASE.
- Reused owner baseline complete same-hash LSP at
  `/private/tmp/roth-theta-mono/final-lsp.json`, source
  `8d6d5dda0246f2b78ed60a6a06017c5ad8de774aec4693dfb710ef8a94288045`.
  Success, complete, no timeout/dependency failures, 0 errors/33 warnings.
- Owner supplied preceding frozen full build 58.864s and separate LeanEval 21.222s, both exit0.
- Private original target exactly matches baseline source; original independent proof retained
  separately and compiled. Work directory: `/private/tmp/roth-theta-index-comp/`.
- File-wide phases/rename queue/shared reports and final full/LeanEval gates belong to owner.

## Full 24-item audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | Lint | Original unused section σ-DecEq and unused decidability-in-type warnings; both private DecEq instances removed after direct public contract recovery; no suppression. Final diagnostic results below. |
| 2 | Have scan | Only original `hd : ... := by`, one use, proof-bearing; replace whole inverse roundtrip with mathlib surjectivity. Final no `have`. |
| 3 | Set option | None in target; no production options added. |
| 4 | Simp squeeze | Original terminal `simp`/`simpa` only. Final all four `simpa` calls and final `simp` close branches; unsqueezed. |
| 5 | Naming | Descriptive `indexSet_comp_subset` uses existing lowerCamelCase object name plus snake_case predicates; no forbidden number pattern/abbreviation. No rename required. |
| 6 | Line packing | Both signature lines measured below; first packed from 78 to94 codepoints. |
| 7 | By placement | End of conclusion line. |
| 8 | Format | Two-space proof indentation, focused branches, one tactic per line, no empty proof lines, no `haveI`/`letI`; old lambdas eliminated. |
| 9 | Comments | No target comments; all surrounding original narratives byte-preserved. |
| 10 | Docstring | Private target has none; public caller docstring unchanged. |
| 11 | Visibility | Remains private; single public caller `Θ_equiv`, two applications. |
| 12 | Structure | Final12 body lines; maximum branch3 lines; no top-level conjunction; no extraction needed. |
| 13 | Mathlib | Five actual methods below; partial APIs found and used; no direct replacement established. |
| 14 | Junk def | n/a: lemma, no data definition. |
| 15 | Exists lemma | n/a: set inclusion with substantial witness transport, not trivial existential wrapper. |
| 16 | Show/change | Neither occurs. |
| 17 | Push neg | None. |
| 18 | Generalise | All10 effective original binders audited/probed below; both private DecEq instances removed, all public instances retained. |
| 19 | Inequality | No reversed inequalities; table below. |
| 20 | Normal form | Set inclusion is canonical one-direction transport; caller combines inverse direction via subset antisymmetry. |
| 21 | Syntax generality | Bundled equivalence provides inverse, injectivity and surjectivity directly; no easier caller form found. |
| 22 | Import fanout | n/a: no import change. |
| 23 | Casts | No explicit casts/ascriptions introduced; 0 dropped/0 kept in diff. Original cross-type coefficient casts are hidden by destructuring and unchanged definitions. |
| 24 | Instance name | n/a: no instance declaration. |

## Mathlib search-status (actual attempts)

| Method | Query/evidence | Result |
|---|---|---|
| A LeanFinder | “Multivariate polynomial renaming variables by an equivalence preserves coefficient bounds degree and polynomial index”,3results | Degree/total-degree rename and finSuccEquiv components; no full target. |
| B Loogle | `MvPolynomial.rename, MvPolynomial.coeff` then corrected `MvPolynomial.rename, "coeff"` | First query unknown identifier; corrected query returned `coeff_rename_mapDomain`, `coeff_rename_embDomain`, `constantCoeff_rename`, zero/nonzero coefficient facts. |
| C LeanSearch | “coefficient of multivariate polynomial rename under equivalence”,4results | Four coefficient rename facts, including exact coefficient component used. |
| D Source rg | Untruncated `coeff_rename`, `degreeOf_rename`, `rename_eq_zero_iff_of_injective`, `mapDomain_surjective`, `renameEquiv` in mathlib; target name in project/mathlib | Existing rename zero/degree/coefficient APIs and Finsupp surjectivity; local domain-specific inclusion only in Theta. One attempted MapDomain filename did not exist; corrected to Data/Finsupp/Basic. |
| E Native local search | `coeff_rename`, `rename_eq_zero_iff_of_injective`, `mapDomain_surjective` | Found names in source; returned index=`unavailable`, so no indexed-absence claim. |

Auxiliary variants checked: rename equivalence, rename zero iff, coefficient mapDomain/embDomain,
coefficient zero/nonzero, degree rename, mapDomain composition/surjectivity.
Common-equivalents lookup: no discrete/compact/finiteness bucket applies.
Use partial matches directly within the domain-specific witness transport; it requires more than
three independent mathlib calls and is used twice. No new wrapper/helper introduced.

Generic-route experiments: `negative.lean` tried whole-proof grind, aesop and simp; all failed.
Its later exact?/apply? suggestions referred to an earlier failed theorem (containing sorry),
so those suggestions were discarded and never used. Corrected independent files have no prior
target theorem: `absence-exact.lean` reports exact? cannot close; `absence-apply.lean` reaches
the deliberately lowered20k heartbeat bound after irrelevant partial order suggestions.
The latter is inconclusive; no exhaustive absence theorem is claimed. This is bounded search
evidence, not evidence that a mathematical generalization is impossible. The known session
multi_attempt stalls were not repeated; ordinary isolated compiler probes were used.

## Generalisation — every effective original binder

All named negative probes use `autoImplicit false`; compiler failures are expected and kept
separate from successful proof/axiom checks. See `negative.log`, `extra-negative.log`.

| # | Binder | Role/use | Compiled drop/weakening | Result |
|---|---|---|---|---|
| 1 | `{σ : Type*}` | Domain of polynomial/index | `drop_sigma` in extra-negative | Unknown σ; retain independent universe-polymorphic carrier. |
| 2 | `[Fintype σ]` | Required by `indexSet`/index | `drop_fintype_sigma`; `finite_sigma` | Both fail Fintype synthesis in statement; retain. No type-level chosen Fintype restatement applied. |
| 3 | `[DecidableEq σ]` | Automatically included section instance | `candidate2.lean` omits it and compiles exit0 | Dropped with scoped omit after caller-contract3 exit0 proves ordinary public caller still has exact original type and all10 BinderInfo entries. No public amendment. |
| 4 | `{τ : Type*}` | Codomain carrier | `drop_tau` in extra-negative | Unknown τ; retain independent universe. |
| 5 | `[Fintype τ]` | Required by target indexSet | `drop_fintype_tau`; `finite_tau` | Both fail Fintype synthesis in statement; retain. |
| 6 | `[DecidableEq τ]` | Explicit unused private instance | `candidate2.lean`, caller-contract2 and live module build | Dropped; weaker private theorem compiles; public caller retains its explicit instance. |
| 7 | `(e : σ ≃ τ)` | Rename, inverse numerators, surjectivity | `drop_e`; function-only selected-proof attempt; `injective_e` exact? | Drop ill-typed; function proof lacks inverse/surjectivity, injective-route search fails. Retain; no claim injective restatement is false. |
| 8 | `(B : ℝ)` | Shared coefficient bound | `drop_B` | Unknown B; no strict/weak proposition to weaken. Abstract coefficient-ring change would restate the project definitions, outside private cleanup. |
| 9 | `(q : τ → ℕ)` | Denominators/coprimality | `drop_q` | Unknown q; no additional sign/nonzero hypothesis to drop. |
| 10 | `(r : τ → ℕ)` | Coordinate degree/weight | `drop_r` | Unknown r; no positivity assumption present. |

Private literature search: n/a, private declaration; public caller untouched.
Inversion check: indexSet unfolds to a shared polynomial/numerator witness; proof keeps using
specific polynomial rename, degree, coefficient, coprimality and index structures. The generic
renaming pieces already exist and are used. No remaining standalone abstract-only tail warrants
a new production API. Full injective/Finite/type-level restatements are optional unapproved
API changes, not applied or blockers. No public A–F menu item was applied.

## Signature packing

`#check` of the selected compiled theorem and of the original appears in candidate/positive logs
at `format.width 100`. Final effective private type includes σ/Fintypeσ/τ/Fintypeτ/e/B/q/r, with no DecidableEq.

| Signature line | Width | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 128 | 94 | conclusion `indexSet B (q ∘ e) (r ∘ e) ⊆ indexSet B q r := by` (49 unindented chars) | 94+1+49=144>100 | packed |
| 129 | 53 | no next signature line | n/a | packed |

| # | Location | Reversed inequality | Rewrite/rename |
|---|---|---|---|
| 1 | Full target signature and hypotheses | none (`⊆` is set inclusion; function arrows are not `>`) | n/a |

## All42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | Old degree/coefficient rw+exact consolidated using terminal simpa. |
| 1.4 | Applied simpa using to degree/coefficient invariance. |
| 1.5 | n/a: no trailing rfl after simp. |
| 1.6 | Existing anonymous witness constructors retained; logical branches flattened. |
| 1.7 | n/a: no apply+exact. |
| 1.8 | n/a: no contradiction/push_neg. |
| 1.9 | Removed old witness lambdas with holes/branch binders; no remaining eta expansion. |
| 1.10 | Original single-use hd was proof-bearing; eliminated whole roundtrip via mapDomain_surjective. |
| 1.11 | n/a: no apply+intro sequence. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no have-projection pair; original nested witness destructuring retained. |
| 1.14 | n/a: no consecutive rw after replacement. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: every simp/simpa terminal. |
| 1.17 | Existing e.injective/e.surjective/e.symm notation retained. |
| 1.18 | n/a: no avoidable final parenthesized compound expression. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: inclusion, not trivial single-use existential lemma. |
| 2.1 | Actual whole-proof grind failed in named batch. |
| 2.2 | n/a: no grind retained. |
| 2.3 | Final index rw/congr/funext/simp replaced by one terminal simp; degree/coefficient simpa consolidation. |
| 2.4 | n/a: no function-property predicate. |
| 2.5 | n/a: no positivity branch; coefficient bounds transported by equality. |
| 2.6 | n/a: no monotonicity estimate, only equality transport. |
| 2.7 | n/a: no arithmetic subgoal; no lia/omega needed. |
| 2.8 | Actual whole-proof aesop failed, made no progress. |
| 2.9 | n/a: no concrete arithmetic or cast-normalization branch. |
| 2.10 | n/a: unbounded existential witness construction, no finite decidable computation. |
| 2.11 | n/a: quotient functions coincide under equivalence, no field identity needed. |
| 2.12 | n/a: no ring/ring_nf endpoint. |
| 2.13 | n/a: no symmetric case split; inverse-direction caller already reuses this lemma. |
| 2.14 | n/a: no calc chain. |
| 2.15 | Branches prove different witness properties; common all-goal automation offers no consolidation. Whole-proof grind/aesop/simp failed. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega. |
| 3.4 | Existing surjective obtain substitutes rfl; new mapDomain surjective obtain does likewise. |
| 3.5 | No simp/grind attribute: private one-direction transport should not become a global rewrite. |
| 3.6 | n/a: no simp_all only; whole-proof simp failed without constructing witnesses. |
| 3.7 | n/a: no production limit overrides; isolated negative probes only lower to20k. |

## Reflection, simplify, trust, and final gates

Step-back check tested one-tactic routes and generic exact?/apply? routes. A term proof would
hide the five distinct witness obligations. The selected proof exposes those obligations and
uses existing APIs for each. No new private helper or public API extraction is needed.

Simplify pass: native `/simplify`/Skill invocation is unavailable in this host; performed the
scoped holistic review manually. Outcome ISSUES-FOUND-AND-FIXED by the selected proof: removed
manual inverse-mapDomain equality and manual index function congruence. No further changes.

New identifiers verified by native local search, source definitions, then actual compilation:
`MvPolynomial.rename_eq_zero_iff_of_injective` (Rename.lean107),
`Finsupp.mapDomain_surjective` (Basic.lean441). All other identifiers already existed in target.

Successful independent evidence: `positive.lean/.log` reproves the exact original target using
the baseline original proof, without invoking the current target; exit0, only propext,
Classical.choice, Quot.sound. `caller-contract2.lean/.log` and the decisive σ-omission
`caller-contract3.lean/.log` compiled a namespace copy of the new prefix and unchanged caller: exact equality to imported original Θ_equiv via rfl,
same ten BinderInfo entries and standard axioms. This is stronger than header-text equality.

Verification details and profiles are completed below before final handoff.

## Final verification

Final targeted build `/Users/ramin/.elan/bin/lake build Roth.Theta` exited0; module built43s,
2423jobs (`module-build-final.log`). The earlier pre-omit worker build also passed40s.
Final fresh complete unfiltered native diagnostics in `final-lsp-omit.json`:
success=true, partial=false, timed_out=false, failed_dependencies=[],0errors/32warnings.
No target diagnostics; public/header warnings retained under scope protection. The pre-omit
`final-lsp.json` remains separate stage evidence (33warnings).

`actual-built-final.lean/.log` exited0 after the fresh module build. It locates exactly one
private constant programmatically by suffix:
`_private.Roth.Theta.0.Roth.indexSet_comp_subset`. Its actual built type has exactly8 binders
(σ/Fintypeσ/τ/Fintypeτ/e/B/q/r), no DecidableEq, and standard axioms only:
propext, Classical.choice, Quot.sound. An explicit old10-binder adapter accepts both old
DecidableEq instances and applies the new private constant. It equals the independently
reproved original theorem via rfl, with identical BinderInfo. The same successful file checks
actual built Θ_equiv against the original explicit telescope after universe alignment using
Meta.isDefEq plus all10 BinderInfo entries, and checks its standard axioms. Thus no public
binder/type change is hidden by an unchanged visible header.

Scratch corrections were completed before certification: an import placed after a doc-comment
command was moved to the import header; a metaprogram local named reserved `at` was renamed
`actualType`; an initial shorthand coprimality lambda was expanded to intro j. No failed file
is used to certify proof soundness. Successful proof checks and expected-failure search files
are distinct. Native multi_attempt was not repeated after its documented prior stalls.

## Buzz pass — exact-prefix scope only

Outcome: FAST-BOARD,1000ms budget. All normal/LSP/build processes were drained first;
profiles ran sequentially in the exclusive worker window, both exit0. No repeat is required:
both results are below the750ms repeat threshold.

Real Lean4.34 command (each exact source prefix, no production scaffolding):
`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE`.

| Version | Outer command | Async proof | Kernel | Linter | Total | Prefix wall |
|---|---:|---:|---:|---:|---:|---:|
| Before |12.338ms|147.223ms|10.325ms|8.845ms|178.731ms|44.841s|
| Final |14.817ms|151.863ms|7.659ms|7.062ms|181.401ms|42.066s|

Raw UTF8 `before-profile.log` anchors:122980 outer lemma,123008 target async proof,
142523 kernel,142525 linter. Inner theorem macro command at122174 is excluded.
Raw `final-profile.log` anchors:123047 outer omit command,123063 target async proof,
139735 kernel,139737 linter. Nested omit/theorem/lemma command expansions are excluded:
122189/122263/123031. No nested timing is double-counted. Target source anchors are before127,
final scope127/declaration128. `profile-summary.json` and `profile-runs.json` retain the numbers,
commands, statuses, scope and repeat decision. This is a clarity/generality cleanup; the small
+2.670ms target difference is not claimed as a speed improvement. Both are comfortably fast.
No slow-declaration diagnosis/fix/propagation queue; no performance deferral or limit raise.

The files preserve all exact preceding source/imports/context, with only namespace closure
appended. Prefix correspondence and final source hash were checked programmatically. These
profiles do not certify a whole-file sweep. Known late full-Theta default-heartbeat failure
at index_le_lem6 remains a separate owner final-sweep obligation; no limits were raised.
No heartbeat counter/profiler scaffolding was inserted in production.

## Worker gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | PASS | Actual final `/Users/ramin/.elan/bin/lake build Roth.Theta`, session74380 exit0; module43s/2423jobs, module-build-final.log. |
| definition_protected | PASS | No def/abbrev change; outside-target byte equality. |
| theorem_statement_protected | PASS | Authorized private DecEq weakening only; all public source untouched; actual built Θ_equiv type/universe/BinderInfo exact. |
| original private contract | PASS | Independent original proof plus explicit old10-binder adapter to actual new private constant; equality and BinderInfo recovered. |
| structure_gate | PASS | Body12≤30, max branch3≤10; public caller unchanged. |
| naming_gate | PASS | Descriptive clean name; no rename queue entry needed. |
| line_packing_gate | PASS | Both lines measured94/53 codepoints; justified break arithmetic above. |
| inequality_orientation_gate | PASS | Explicit scan table; no reversed inequality. |
| native complete diagnostics | PASS | final-lsp-omit.json complete, success/no timeout/no dependency failure,0errors32warnings. |
| actual built standard axioms | PASS | Programmatic private suffix and public Θ_equiv/adapter/original checks, successful actual-built-final.log. |
| no limits/scaffolding/trust weakening | PASS | Target diff has none; no sorry/new axiom/native_decide or profiling option. |
| local caller compatibility | PASS | Compiled module and direct actual Θ_equiv contract/BinderInfo; public source byte unchanged. |
| full project + separate LeanEval | OWNER PENDING | Not run/claimed by worker. |
| whole-file final profile sweep | OWNER PENDING | Prefix-only evidence explicitly scoped above. |

Worker gates pass; owner cumulative/full/LeanEval gates are pending.

## Required11-step checklist

- [✓] Step1 — mandatory references and relevant style/naming/profiling read.
- [✓] Step2 — all24 audit items recorded with actions or concrete n/a.
- [✓] Step2.5 — five actual mathlib search methods and bounded generic-route evidence recorded.
- [✓] Step2.6 — all10 original effective binders classified and compiled drop/weakening probes recorded.
- [✓] Step2.7 — measured two-line signature packing table.
- [✓] Step2.8 — explicit inequality occurrence table.
- [✓] Step3 — all42 golfing rules have status.
- [✓] Step4 — one-tactic, generic-route, term-mode and structural reflection completed.
- [✓] Step5a — fresh COMPLETE unfiltered final native LSP succeeded.
- [✓] Step5b — diff gates, actual module build, original/private/public contract/axiom recovery and scoped buzz pass completed.
- [✓] Step6a — no rename needed; parent-owned sidecar/shared files untouched.

No outstanding worker fix, new private helper audit, orphan request, or worker compiler process.


Final source frozen SHA256:
`f7c692b5eac9b0fb46be5031ae57440a49e27f3f34dfeb6bf2fb38962e388c9a`.
Outside-target source byte-equality verified against checkpoint13 snapshot. The owner reopened
source authority once for the tested private σ omission; source refrozen afterward. No source
edit authority remains after final freeze; no Git mutation performed. Owner full then separate
LeanEval gates remain pending and are not claimed by this worker.


## Owner cumulative publication gates

After final leaf freeze/revocation and all requests drained, owner ran `lake build` followed by
separate `lake build Roth.LeanEval`: both exited 0, in 60.885 s and 22.704 s. Source SHA256
`f7c692b5eac9b0fb46be5031ae57440a49e27f3f34dfeb6bf2fb38962e388c9a` was identical before
and after both commands. Raw logs: `/private/tmp/roth-theta-d14-full.log` and
`/private/tmp/roth-theta-d14-leaneval.log`; machine record `/private/tmp/roth-theta-d14-builds.json`.
These completed owner gates supersede the worker's earlier pending cumulative entries. Exact-path
staging, commit and successful push publish this checkpoint before the next original source edit.
Published counts: Theta 14/35, overall 195/264, 9/14 files. Public menus A–F remain unapplied.
