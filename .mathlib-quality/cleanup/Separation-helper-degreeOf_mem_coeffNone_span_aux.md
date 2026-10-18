# Fresh helper audit: `degreeOf_mem_coeffNone_span_aux`

Scope: private helper at source lines 248–262, frozen original helper `/private/tmp/roth-d21-degreeOf_mem_coeffNone_span_aux.lean.txt`; original module `/private/tmp/roth-separation-d21-source-freeze.lean`. Parent owns all public decisions/Git/shared reporting. No edits made before this initial audit. The `lean4` and `mathlib-quality` skills and cleanup Phase 4 apply.

## Initial audit (before source edits)

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | Lint | Native complete module baseline succeeds; no diagnostic on helper lines. Preserve parent-owned warnings. |
| 2 | Have scan | No `have`; `W` is a local submodule value, not a disposable proof witness. |
| 3 | Options | No local/global options in target. |
| 4 | Simp | `zero_mem'` terminal `simp`; generator proof terminal `simpa using`. No nonterminal simp. |
| 5 | Name | Describes degree bound on coefficient span; snake case with conventional `degreeOf`, private `_aux`; no forbidden numbered suffix. |
| 6 | Packing | Measure every signature line below; first full `P` binder does not fit after first line. Conclusion does not fit after `hp`. |
| 7 | By placement | Every `by` ends its introducing line. |
| 8 | Format | Two-space proof indent, no blank proof lines or forbidden instance syntax. |
| 9 | Comments | No inline comments to move/delete; preserve surrounding public documentation. |
| 10 | Docstring | Private helper: no docstring required. |
| 11 | Visibility | Private and used only by the public representation theorem. |
| 12 | Structure | 11 proof lines, no conjunction/case branches; below bound. |
| 13 | Mathlib | Actual A/B/C/E searches completed; A finds bundled `MvPolynomial.degreesLE`. Probe replacing bespoke submodule and span-induction strategy. Source search D and compiled generic-route probe required below. |
| 14 | Junk def | Not a definition. |
| 15 | Exists lemma | Not existential witness boilerplate. |
| 16 | Show/change | No tactic-mode `show`. |
| 17 | Push neg | None. |
| 18 | Generalise | Every effective binder considered below; no variable-index instances. Probe `CommSemiring` → `Semiring`, no coefficient class, arbitrary index set for span. |
| 19 | Inequality | Two explicit `≤` in statement/carrier and one submodule inclusion `≤`; all correct orientation. |
| 20 | Normal form | Degree bounds are canonical `degreeOf ≤`; bundled equivalent `degreesLE` found and will be tested. |
| 21 | Syntax generality | Caller naturally provides span membership; preserve caller interface unless measured deletion is justified. |
| 22 | Import fanout | No new import planned. |
| 23 | Casts | `ν : Fin (n + 1)` fixes index; final `: Submodule.span R _ ≤ W` directs membership elaboration. No cross-type cast. |
| 24 | Instance name | Not an instance. |

Private literature exemption: this internal degree-closure helper is not public mathematical API. No literature assertion or public generalisation is being introduced; online library searches are API searches only.

Initial issues: examine built-in `degreesLE`/span induction rather than duplicating submodule closure. No committed source changes yet. Final detailed golf/generalisation/gate artifacts follow below.

## Actual five-method Mathlib search

| Method | Actual query / evidence | Result |
|---|---|---|
| A Lean-Finder | Native query `MvPolynomial degreeOf bounded submodule span coefficients optionEquivLeft`; `/private/tmp/roth-d21-helper2-finder.json` | Success: `degreesLE`, `restrictDegree`, `degreeOf_le_iff`, coefficient degree facts. |
| B Loogle | Native `MvPolynomial.degreeOf, Submodule.span`; `/private/tmp/roth-d21-helper2-loogle.json` | Successful empty response; not an absence claim. |
| C LeanSearch | Native natural-language query on degree bounds in linear spans of coefficients; `/private/tmp/roth-d21-helper2-search.json` | Success: degree/support lemmas, `restrictTotalDegree_le_restrictDegree`; no one-call replacement returned. |
| D source | Full untruncated relevant MvPolynomial source searches, `/private/tmp/roth-d21-helper2-source-search.log`; full candidate-name search over all Mathlib in `/private/tmp/roth-d21-helper2-full-name-search.log` | Existing `restrictSupport`, `mem_restrictSupport_iff`, `degreesLE`; no full-name match (exit 1). |
| E local names | Native `degreeOf`, limit 30; `/private/tmp/roth-d21-helper2-local.json` | Returned degree APIs but `index: unavailable`; use source/#check as honest fallback, not indexed absence. |

Native `lean_run_code` confirmed `restrictSupport`, `mem_restrictSupport_iff`, `degreesLE`, `Multiset.le_iff_count`, and `span_induction` types. It also rejected a guessed `Multiset.count_filterMap`: no such constant, so that route was abandoned. The actual compiled support proof is `/private/tmp/roth-d21-helper2-support.lean` (exit 0, standard axioms). `degreesLE` encodes a multiset bound; `restrictSupport` directly encodes unequal bounds by variable and avoids extra multiset/Option transport. No new imports.

Generic-route search: native live-goal `exact?` failed, `apply?` produced only partial suggestions; `grind`, `simp`, `aesop` failed at the original goal. Raw `/private/tmp/roth-d21-helper2-attempts.json`. These line-replacement probes also encounter parse errors from the untouched structure tail; they are not successful full-proof tests. The isolated span-induction proof and compiled module-inline candidate provide the successful full-proof evidence, with no self-reference or `sorry`.

Six replacement rules: (1) replace bespoke closure with imported bundled API and inline at sole caller; (2) all five searches plus compiler-directed generic route attempted, no unsupported absence claim; (3) degree/support/coeff variants searched; (4) no custom class predicate needed; (5) delete wrapper completely rather than keep a thinner copy; (6) existing module documentation preserved under parent scope, concrete library usage documented here.

## Generalisation and every effective binder

Fresh compiler probes use `set_option autoImplicit false` in scratch files only. `/private/tmp/roth-d21-helper2-probes.py`, summary `/private/tmp/roth-d21-helper2-probes.log`, individual `/private/tmp/roth-d21-helper2-fresh-<case>.lean` and `.log` files. Body-preserving drop failures establish that the existing elaborated proof/signature uses the binder, not a universal semantic impossibility theorem.

Artifact correction: this host's case-insensitive filesystem makes `drop_P` and `drop_p` collide. The `P` test is re-run under unique name `drop_polynomial`; the member-polynomial test is saved as `drop_member`. Those unambiguous files/logs, not the colliding historical names, are the final evidence for those two rows.

| Binder / hypothesis | Mechanical test | Decision |
|---|---|---|
| `{τ : Type*}` | Drop `τ` | Unknown identifier in variable type; preserve universe-polymorphic index type. |
| `{R : Type*}` | Drop `R` | Unknown coefficient-ring identifier; preserve. |
| `[CommSemiring R]` | Drop class; replace with `[Semiring R]` | MvPolynomial/degree/support APIs require `CommSemiring`; both fail synthesis. No field, ring, subtraction, nontriviality, domain, or zero-divisor assumption remains. |
| `P` | Drop parameter | `P` unresolved in span generator and bound; preserve. |
| `n : ℕ` | Drop parameter | `n` unresolved in finite index. Tested arbitrary index function successfully in `/private/tmp/roth-d21-helper2-general-index.lean`, standard axioms. This confirms finiteness/cutoff is not used in closure. No broader helper is retained: caller uses its own coefficient family directly. |
| `{p}` | Drop binder | Polynomial identifier unresolved in membership/conclusion. Can be implicit already. |
| `hp` | Drop membership | Existing proof refers to missing `hp`; membership is mathematically essential (take `P=0`, `p=X j` over ℕ). No compiler claim that every possible proof fails. |
| `j` | Universal conclusion binder | Pointwise result is already universally quantified over arbitrary variables; a global finite-variable or decidable-variable assumption is unnecessary. |
| section `[Fintype τ]`, `[DecidableEq τ]` | Exact original-type independent proof with neither instance | Compiles; the original helper already has explicit `omit`, so no additional removal is needed. |
| strictness/point locality | No strict inequality or analytic/global-function hypothesis | Not applicable. |

Inversion check: `n` only restricts the coefficient family; arbitrary `ι → ℕ` version compiles. `P` remains used through its coefficient support and coordinate bounds. The final inlined proof obtains precisely that abstract support-closure argument from Mathlib; no duplicate generalised declaration is added. Literature exemption is private-only as stated above; public theorem type/generalisation was not changed.

## Signature width and inequality artifacts

Codepoint lengths measured with Python `len` (not byte `awk`). Original helper signature, now removed:

| Original line | Width | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 248 | 74 | `(P : MvPolynomial (Option τ) R)` (31) | 74+1+31=106 | Packed correctly; removed. |
| 249 | 66 | complete `hp` binder (77) | 66+1+77=144 | Packed correctly; removed. |
| 250 | 83 | conclusion `∀ j, degreeOf j p ≤ degreeOf (some j) P := by` (45) | 83+1+45=129 | Packed correctly; removed. |
| 251 | 49 | proof starts | Final signature line | Removed. |

The public caller's entire signature is byte-identical; no signature packing changes. All introduced proof lines are ≤100 codepoints. No `pp.width`; scratch reference checks use `format.width 100`.

| Inequality occurrence | Orientation / action |
|---|---|
| Original conclusion `degreeOf j p ≤ degreeOf (some j) P` | Correct; copied into independent original-type test. |
| Original `W.carrier` coordinate bound | Correct; removed with bespoke W. |
| Original ascription `Submodule.span R _ ≤ W` | Correct; removed. |
| New caller support predicate `d j ≤ degreeOf (some j) P` | Correct. |
| Final local inclusion `V ≤ restrictSupport K ...` | Correct submodule order. |
| Existing caller signature bounds and `hl1` | Untouched; smaller side left. |

No reversed `≥`/`>` or `_ge_`/`_gt_` names introduced. Cast audit: typed `ν : Fin (n + 1)` fixes the family; `p := restrictSupport K ...` is load-bearing for expected submodule elaboration (unannotated scratch candidate failed). No cross-type casts added.

## All 42 golfing rules

| Rule | Concrete status |
|---|---|
| 1.1 by exact | No whole `by exact` wrapper; direct final proof term inlined. |
| 1.2 by rfl | None. |
| 1.3 rw/exact | Original scalar closure pair eliminated with bespoke submodule. |
| 1.4 simp/exact | Original generator was already `simpa using`; preserved the support certificate. |
| 1.5 trailing rfl | None. |
| 1.6 anonymous constructor | No constructor tactic pair; existing caller witness remains anonymous tuple. |
| 1.7 apply/exact | Direct `span_le.2` / `range_subset_iff.2` terms used. |
| 1.8 contradiction | No contradiction in target; caller's existing `by_contra!` unchanged. |
| 1.9 eta reduction | Lambdas bind actual support/degree parameters; cannot eta-reduce dependent conversions. |
| 1.10 single-use have | Original no have; successful scratch `h` membership folded directly into caller. |
| 1.11 apply/intro | Composed term functions instead of adding tactic introductions. |
| 1.12 redundant show | None. |
| 1.13 have projections | None. |
| 1.14 merge rw | No adjacent rw; scalar rw removed altogether. |
| 1.15 terminal simp | New terminal `simpa using` remains unsqueezed; parent-owned measured narrow lists untouched. |
| 1.16 nonterminal simp | None introduced; no squeeze needed. |
| 1.17 dot notation | `.2` API projections and existing transitive closure terms retained where appropriate. |
| 1.18 trailing parens | Parentheses around applying `span_le.2` are required to apply result to membership; nested proof term typed explicitly. |
| 1.19 push neg | None. |
| 1.20 existential helper | Target is not an existential witness; removed after bundled API find instead. |
| 2.1 grind | Actual native original-goal test failed. |
| 2.2 pre-grind steps | No existing grind chain to shorten. |
| 2.3 simpa consolidation | Already consolidated generator support certificate; kept. |
| 2.4 fun_prop | No analytic function property. |
| 2.5 positivity | Final comparison is not nonnegativity; old zero closure disappears into bundled API. |
| 2.6 gcongr | Needed support/span closure, not monotonicity; old max/trans chain removed. |
| 2.7 lia/omega | No arithmetic fact remains after support conversion; no omega introduced. |
| 2.8 aesop | Actual native test failed to establish original degree bound. |
| 2.9 norm_num/norm_cast | No concrete computation/cast normalization goal. |
| 2.10 decide | Proposition depends on arbitrary polynomial span membership, not finite computation. |
| 2.11 field_simp/ring | No denominator identity. |
| 2.12 linear_combination | No ring/ring_nf target; no polynomial equality proof in scope. |
| 2.13 wlog | No symmetric branches. |
| 2.14 calc collapse | Original closure already used `.trans`; final uses no calc. |
| 2.15 shared goals | No repeated tactic subgoals. |
| 3.1 erw/rw | No erw. |
| 3.2 continuity | No legacy continuity/measurability. |
| 3.3 omega/lia | No omega; arithmetic API untouched. |
| 3.4 rfl substitution | No rcases-rfl/simp redundancy. |
| 3.5 attributes | One internal use; no global simp/grind attribute warranted. |
| 3.6 simp_all | No simp_all only. |
| 3.7 heartbeat limits | None added or needed. |

## Step back / simplify

The mathematical content is linear closure of a support bound. Defining W manually repeats Mathlib's `restrictSupport`. A whole-proof automation route fails and the multiset-oriented `degreesLE` route would add transport overhead. The imported `restrictSupport` plus `span_le` gives a direct proof; folding the single-use scratch membership into the caller removes the helper entirely. This is the substantive step-back improvement. The compiled inline module has a 30-line headline proof, satisfying the explicit parent bound. No new helper was introduced. No public declaration rename/type/docstring change. No comment or header edits.

Performance follow-up: putting the full support proof inside the witness tuple costs 1070.206 ms on the first actual-module sweep (81.906 ms outer command + 988.300 ms outer async proof). The isolated repeat gives 934.305 ms (36.199 + 898.106), still above the 750 ms resweep threshold. Diagnosis: the witness `refine` alone costs 433.241 ms in the first sweep; repeated unification and support conversion occur inside a large dependent tuple. Parent explicitly authorized testing a typed local span inclusion. The final candidate moves the identical support proof into local `have hdegree : V ≤ restrictSupport K ...` before the tuple and uses `hdegree (b ρ).2 hd j` in the witness. This local fact is retained as an expected-type/performance boundary; it introduces no new declaration. Main proof remains exactly 30 physical lines.

Typed-local first sweep completed with exit 0, `/private/tmp/roth-d21-helper2-profile-typed.log`: 125.921 ms outer command + 982.413 ms outer async proof = 1108.334 ms. This is rejected as a final performance gate. Its run overlapped final verification compiler jobs. Those were drained before starting a fully isolated typed-local repeat, `/private/tmp/roth-d21-helper2-profile-typed-repeat.log`. The repeat decides whether to keep inlining or restore the shorter bundled-API helper as a measured performance boundary. No time/heartbeat limits changed.

Baseline supplied in dispatch: actual-module `/private/tmp/roth-d21-final-profile1.log`, original helper 97.518 ms (18.768 + 78.750), actual main 698.714 ms. This worker makes no claim of whole-project performance improvement. Every final sweep uses `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean`, with actual command/proof anchors, not extracted-namespace timing and not aggregate category totals. Nested header/value/typechecking nodes are not added again.

Typed-local candidate have scan: `hdegree` is the one added have, a typed span inclusion used once. Its algebraic/support content is provided by existing Mathlib; its type boundary is intended to reduce large-tuple elaboration cost (final timings below decide acceptance). Existing caller `FiniteDimensional`, `hP'`, `hl1` are unchanged. New terminal `simpa` remains unsqueezed. Fresh complete native LSP for typed-local candidate: `/private/tmp/roth-d21-helper2-typed-lsp.json`, 0 errors, 31 warnings, `partial=false`, `success=true`.

The standalone original-helper proof is `/private/tmp/roth-d21-helper2-fresh-independent.lean`, with final compatibility example spelling out its exact original quantified type. It is independent span induction, not a call to this helper or the public representation theorem. Its final pre-typed-local compile `/private/tmp/roth-d21-helper2-fresh-independent-final.log` exited 0; axioms `[propext, Classical.choice, Quot.sound]`. Original meaning/signature is thus available independently even after helper deletion. Final built-target verification follows below.

## Verification evidence for typed-local candidate

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0: `/private/tmp/roth-d21-helper2-build-final.log`, `Build completed successfully (1876 jobs)`. The complete unfiltered native LSP is `/private/tmp/roth-d21-helper2-typed-lsp.json`: `partial=false`, `timed_out=false`, `success=true`, 0 errors / 31 existing warnings. No warnings suppressed. Public-instance approval decisions remain the parent's separate work.

After that actual build, `/private/tmp/roth-d21-helper2-final-verification.lean` combines the exact ORIGINAL-helper type, its independent non-self span-induction proof, an explicit compatibility example, and checks of the actual built constants. `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-d21-helper2-final-verification.lean` exited 0; full log `/private/tmp/roth-d21-helper2-final-verification.log`. `independentAudit`, actual `Roth.exists_separated_representation`, and actual retained private `linearIndependent_coordinate_polynomials_aux` and `eq_sum_aeval_basis_coeffNone_aux` use only `[propext, Classical.choice, Quot.sound]`. The checker locates private constants by exact suffix and verifies the deleted helper is absent. The main theorem's entire source signature is byte-identical to the dispatch freeze; defs/docs/header/imports untouched.

Arithmetic: dispatch module 587 lines → candidate 575, net −12. Diff against dispatch freeze: 18 removed lines / 6 added lines (`/private/tmp/roth-d21-helper2-diff-final.patch`). The helper block is 15 declaration lines plus its omit/blank delimiter; sole caller substitution adds five lines. Main body 25 → 30 physical lines (not 26 → 31). Maximum introduced proof-line width is 81 codepoints. One retained declaration deleted; no new declaration. The 30-line bound is explicit parent authorization; this worker does not claim the generic 15-line headline target was achieved.

## Final performance decision

The fully isolated typed-local repeat passes the affected actual main budget: `/private/tmp/roth-d21-helper2-profile-typed-repeat.log` outer `[Elab.command] [0.029921]` at line 395339 and outer `[Elab.async] [0.762753] elaborating proof of Roth.exists_separated_representation` at line 404841 give **792.674 ms** total. This is below 1000 ms, and its ≥750 ms repeat requirement is satisfied by the two typed-local sweeps (the first rejected, this fully isolated repeat accepted). The deleted helper has no final elaboration cost. The isolated direct-inline candidate was 934.305 ms; the explicit typed local inclusion reduces that affected-main measurement by 141.631 ms. Compared with the dispatch main baseline 698.714 ms, the accepted main is slower by 93.960 ms; this tradeoff removes the separate helper and duplicated submodule implementation. No claim that summed/whole-project elapsed time improved.

The rejected candidates and raw logs remain available. No broad simp discharger or helper1 change was introduced. The final actual profile process must complete and be drained before the freeze statement below is recorded.

**Borderline performance flag: repeated under budget, owner final repeat pending.** Final main 792.674 ms remains ≥750 ms. Parent explicitly accepted this measured typed-local candidate for this worker freeze and will perform additional fully isolated final batch sweeps after helper3's audit and before publishing original21. Any actual declaration ≥1000 ms there must be fixed and re-gated. This report does not clear that owner-level pending repeat or claim all performance variability eliminated.

## Diff gates and all eleven completion steps

| Gate | Worker result | Evidence / scope |
|---|---|---|
| `definition_protected` | Pass | No def/abbrev/import/header edits. |
| `theorem_statement_protected` | Pass | Public signature byte-identical; private helper deletion and exact caller substitution explicitly authorized by parent after compiled proposal. |
| `lake_build_file` | Pass | Actual final `lake build Roth.Separation`, exit 0, 1876 jobs, final build log above. |
| `structure_gate` | Pass under explicit dispatch bound | Deleted helper; actual main 30 lines, parent bound ≤30. No new declaration or long branch. |
| `naming_gate` | Pass | No added/renamed declaration; deleted private `_aux` name was descriptive. |
| `line_packing_gate` | Pass | Every original helper signature line measured above; removed. Caller signature unchanged, max introduced line 81 codepoints. |
| `inequality_orientation_gate` | Pass | Every original/new bound and inclusion listed above; no reversed inequalities. |
| `cumulative_no_unintended_breakage` | Worker module pass; owner project gate pending | Only caller in same module; full module build/LSP clean. Parent owns sequential full project and separate LeanEval builds. |
| `axioms_and_original_type` | Pass | Combined final verification exit 0; exact-original non-self proof and actual built constants use only standard axioms. |
| `buzz` | Repeated under budget; borderline flag | Final affected main 792.674 ms; parent additional isolated final batch sweeps pending as explicitly recorded. |

Overall worker gates: pass with the explicit parent performance handoff above. No public-instance changes, domain weakening, rename, new helper, or new import proposed/applied. No unresolved worker refactor proposal. Renames queued: none. Comments preserved: none in deleted helper; all caller/surrounding documentation unchanged. Parent project-wide compatibility/Git/push remains outside worker ownership.

- [✓] Step 1: skills and relevant reference docs read; full 42-rule list and proof-patterns considered.
- [✓] Step 2: all 24 initial audit items written before source edits; final have/cast/normal-form follow-up included.
- [✓] Step 2.5: five actual Mathlib searches recorded with honest unavailable local index and source/compiler fallback.
- [✓] Step 2.6: every effective binder considered/tested; private literature exemption explicit; arbitrary-index generalisation compiled and not retained as a new helper.
- [✓] Step 2.7: every original signature line has codepoint arithmetic; caller signature unchanged.
- [✓] Step 2.8: per-occurrence inequality/inclusion scan included.
- [✓] Step 3: all 42 golf-rule statuses supplied, failed native probes distinguished from successful compiled proofs.
- [✓] Step 4: substantive step-back replaced bespoke submodule construction with imported support API; measured local expected-type boundary.
- [✓] Step 5a: complete unfiltered native module diagnostics pass, 0 errors / 31 preserved warnings.
- [✓] Step 5b: diff gates, actual module build, independent original type, actual axioms, and affected actual timing recorded; borderline handoff explicit.
- [✓] Step 6a: no rename to enqueue and no shared sidecar/Git mutation.

## Freeze

Final actual isolated profile process completed with exit 0; no pending partial response. Final source `Roth/Separation.lean`: **575 lines / 25 retained declarations**, SHA256 **`bf21df6efe9383af81820b6d34b9c4be2f65fe201c21446006a96d28573c63df`**. The helper declaration is absent; main proof is exactly 30 lines, original public signature preserved. Original-declaration cleanup counter is unchanged by this fresh helper audit.

Declaration arithmetic includes `noncomputable def coeffNone`: dispatch freeze 26 → final 25. A regex omitting the `noncomputable` prefix counts only 24 and is not the declaration inventory.

**ALL source ownership revoked. ALL Lean/MCP/compiler/profile requests drained.** Worker is now report-only; no further source edits. Only the explicitly parent-owned additional isolated final batch performance sweeps, cumulative original compatibility/project/LeanEval gates, and publication remain outside this worker's completed scope. No hidden worker blocker or pending source proposal.
