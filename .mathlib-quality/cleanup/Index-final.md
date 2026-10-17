# Index — completed file cleanup

Baseline `e557886`; final source SHA256
 `30e6f151ddd2d9c344b9537d1bef87124e3f5814d2e58f3cba499a7e1ea6c939`.
Original275→final245 lines (−30,−10.9%). All21 originals audited by distinct fresh
Sol Medium declaration workers;19 retained (one definition,17 public theorems,one private
support lemma),two trivial private wrappers deleted,no added helpers. Overall151/264
original declarations;8/14 files complete after successful publication.

## Phases 0–5: scope and applied work

Baseline actual full build28852 and complete native LSP passed. The header metadata
warning was explicitly user-preserved. Import-group separation added; nine imports and
all original block documentation are unchanged. Module remains in its original dialect.
Every declaration received all24 audit items,42 golf rules,five actual Mathlib searches,
mechanical binder probes,literature evidence for public declarations,signature packing,
inequality table and11 checked steps. Owner verified each checkpoint and published it
before the next source edit. Final programmatic inventory rechecked all21 reports.
Some actual remote Lean-Finder/Loogle/LeanSearch requests failed with DNS errors;
individual audits record bounded attempts and local-source/#check fallbacks. Such
unavailability was not treated as proof of absence. Math ChatGPT MCP was unavailable.

Routine proof improvements use existing finite-support,infimum,weighted-order,Taylor and
multiplicity API. Main improvements include derivative-bound arithmetic,weight conversion,
the weighted-order bridge,multiplication and the one-variable theorem (23→15 body lines).
No proof/branch decomposition remains outstanding and no new helper needs an audit.

All three public-hypothesis changes were separately scoped and explicitly approved:
remove σ-DecidableEq from17 theorems and τ-DecidableEq from index_rename; remove unused
index_le_card.hr; remove unused index_mul_left_weights.hl. Only four Theta call arguments
were deleted (two hr arguments and two scaling rewrite arguments). All other public
contracts,data,nonzero/Fintype/Unique hypotheses,definitions and documentation are preserved.
Final consolidation removes the now-unused ambient decidability variable and17 redundant
scoped omit commands; actual public types remain those validated at the declaration gates.
No broader zero-convention/generalized-coefficient API proposal was applied.

| Original declaration | Dedicated audit | Final disposition |
|---|---|---|
| `index` | [Audit](Index-index.md) | Retained; full audit complete |
| `mem_support_taylor_iff` | [Audit](Index-mem_support_taylor_iff.md) | Retained; full audit complete |
| `weightSet_finite` | [Audit](Index-weightSet_finite.md) | Deleted trivial private wrapper |
| `weightSet_nonempty` | [Audit](Index-weightSet_nonempty.md) | Deleted trivial private wrapper |
| `index_le_weight` | [Audit](Index-index_le_weight.md) | Retained; full audit complete |
| `exists_weight_eq_index` | [Audit](Index-exists_weight_eq_index.md) | Retained; full audit complete |
| `le_index_iff` | [Audit](Index-le_index_iff.md) | Retained; full audit complete |
| `index_nonneg` | [Audit](Index-index_nonneg.md) | Retained; full audit complete |
| `index_eq_zero_iff` | [Audit](Index-index_eq_zero_iff.md) | Retained; full audit complete |
| `index_hasseDeriv_ge` | [Audit](Index-index_hasseDeriv_ge.md) | Retained; full audit complete |
| `le_index_sum` | [Audit](Index-le_index_sum.md) | Retained; full audit complete |
| `weight_eq_finsuppWeight_div` | [Audit](Index-weight_eq_finsuppWeight_div.md) | Retained; full audit complete |
| `index_eq_weightedOrder_div` | [Audit](Index-index_eq_weightedOrder_div.md) | Retained; full audit complete |
| `index_mul` | [Audit](Index-index_mul.md) | Retained; full audit complete |
| `index_prod` | [Audit](Index-index_prod.md) | Retained; full audit complete |
| `index_neg` | [Audit](Index-index_neg.md) | Retained; full audit complete |
| `index_C_mul` | [Audit](Index-index_C_mul.md) | Retained; full audit complete |
| `index_mul_left_weights` | [Audit](Index-index_mul_left_weights.md) | Retained; full audit complete |
| `index_rename` | [Audit](Index-index_rename.md) | Retained; full audit complete |
| `index_le_card` | [Audit](Index-index_le_card.md) | Retained; full audit complete |
| `index_unique` | [Audit](Index-index_unique.md) | Retained; full audit complete |

Phase5b project-end rename policy: queue raw/deduped1,applied0,no conflict detected.
`index_hasseDeriv_ge → index_sub_weight_le_index_hasseDeriv` remains in the shared sidecar
for the parent to drain after all files. This explicitly scheduled project-level work
is not falsely reported as applied. No other Index rename or API decision is pending.

## Phase 6: cumulative gates

All leaf/reviewer source ownership was revoked and compiler requests drained before the
final source freeze. Index and Theta hashes stayed fixed across the final build sequence.
The whole original Index is independently re-proved in a separate namespace from its
original proofs,including the deleted private wrappers. No original proof is certified
merely by invoking its replacement. All18 original public type/value recoveries compile
with adapters for the approved arguments; actual index definition value recovers by rfl.

| Gate | Actual successful evidence |
|---|---|
| lake_build_file | `lake build Roth.Index`,session62865 exit0; `/private/tmp/roth-index-final-module.log`. Final full build also verifies the unchanged Theta source and its dependencies. |
| lake_build | Sequential owner35061: `lake build` exit0 in87.99s, then separate `lake build Roth.LeanEval` exit0 in40.00s. Root omits LeanEval. Logs `/private/tmp/roth-index-final-{full,leaneval}.log`; frozen hash JSON `...-builds.json`. |
| definition_protected | Entire original index defining declaration unchanged; original definition value equality rfl. No new data definitions. |
| theorem_statement_protected | Actual compiler3443 exit0, `/private/tmp/roth-index-final-compatibility.log`: all18 original public exact-type/value recoveries; all17 actual approved no-DecEq types additionally scanned with Expr.find?. |
| standard_axioms | Same actual-built probe checks every one of19 retained public/private constants: only propext,Classical.choice,Quot.sound. Original independent proofs also compile standard-only. |
| Theta contracts | Fresh compiler54584 exit0 after full build, `/private/tmp/roth-index-final-theta-all-compatibility.log`: independently re-proves ORIGINAL Index+FULL ORIGINAL Theta,all29 original Theta public type/value equalities rfl,all29 actual standard-axiom checks. All Theta positivity and instance contracts preserved. |
| cumulative_no_unintended_breakage | Fresh rg identifies mathematical callers Theta,MainLemma,Main; Separation matches are comments only. Complete unfiltered native LSP all success=true,partial=false,timed_out=false,0errors. Index1/Theta28/MainLemma3/Main4 warnings; root aggregator and separate LeanEval build. |
| docs/comments/structure/width | All original block comments/docstrings byte-identical; no removed inline proof narratives. Every source line≤100 codepoints; no overlong proof/branch flag; exact diff checked. |
| housekeeping/trust | No sorry,new axiom,native_decide,limit raise,debug option,TODO/FIXME,legacy lambda/dollar/push_neg or profiling scaffolding. |

Diagnostic JSON: `/private/tmp/roth-index-final-lsp-initial.json` (Index complete),
`...-lsp-repeat.json` (MainLemma complete),`...-lsp-afterbuild.json` (Theta/Main complete).
Earlier partial/time-limited responses are explicitly not successful gates. The complete
Theta warning set equals d20's by message+line. Of28 warnings,23 predate Index cleanup;
five newly exposed warnings intentionally remain for the later Theta owner: section
DecidableEq in sum_max_sub_le_index_det and private indexSet_comp_subset,section DecidableEq
and explicit hr in indexSet_bddAbove,and explicit hr in Θ_le_card. Contracts were kept and
no lint was suppressed. Main/MainLemma warnings remain their earlier4/3; Index's sole
warning is the explicitly user-preserved missing header metadata.

New external identifiers were first queried through native local search; it returned
positive source hits with index=error,so no absence was inferred. Actual source fallback
and compiler72331 exit0 `/private/tmp/roth-index-final-identifiers.log` verify:

| Added external reference | Verified |
|---|---|
| ENat.toNat_le_toNat | Actual #check + compiled use |
| Finsupp.weight_eq_sum | Actual #check + compiled use |
| Nat.cast_div_charZero | Actual #check + compiled use |
| Set.forall_mem_image.mpr | Actual #check + compiled use |
| sub_le_iff_le_add | Actual #check + compiled use |
| mul_div_cancel_right₀ | Actual #check + compiled use |
| div_right_comm | Actual #check + compiled use |
| mul_div_assoc | Actual #check + compiled use |
| Finset.finite_toSet / Set.Finite.image | Actual #checks + compiled dot-notation uses |

Overall cumulative gates: PASS. Initial full-Theta probe57758 could not start because its
compiled dependency was missing during rebuilding; it is not accepted evidence. Fresh
post-build54584 above is authoritative. No source modification was required.

## Phase 6.5: independent simplify

[Fresh independent full-file review](Index-simplify.md): PASS-THROUGH. Built-in Claude
/simplify is unavailable on this host; the report explicitly records the independent
holistic adaptation. All245 lines and full baseline diff reviewed. Concrete alternative
for index_mul compiled in a whole-file isolated namespace; rejected in light of earlier
measured regression and the clarity of the shared certificate. Import/reuse/helper/API/
automation/style checks produced no further recommended source edit. Reviewer requests
and scratch compilation were fully drained before final profiling; no orphan worker.

## Phase 6.6: actual per-declaration profiling

Budget1000ms,750ms borderline. Actual sequential final-source commands:
`lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`.
Sessions98346/75637 each exit0. No concurrent Lean probes/builds/native requests during
these samples. Traces `/private/tmp/roth-index-final{1,2}-profile-trace.log`; anchored parser
asserts all19 current declaration anchors. Totals add command and associated named async
proof/kernel/compiler roots without nested double counting; aggregate categories/imports/
linters are not substituted for declaration timings. Both complete final sweeps pass.

| Retained declaration | Source line | Sample1 total ms | Sample2 total ms |
|---|---:|---:|---:|
| index | 51 | 18.52 | 23.89 |
| mem_support_taylor_iff | 55 | 25.57 | 28.15 |
| index_le_weight | 62 | 30.93 | 21.97 |
| exists_weight_eq_index | 69 | 97.74 | 97.12 |
| le_index_iff | 78 | 91.74 | 79.80 |
| index_nonneg | 86 | 7.41 | 4.40 |
| index_eq_zero_iff | 91 | 103.71 | 107.88 |
| index_hasseDeriv_ge | 102 | 113.43 | 86.05 |
| le_index_sum | 110 | 190.05 | 195.49 |
| weight_eq_finsuppWeight_div | 122 | 152.56 | 137.55 |
| index_eq_weightedOrder_div | 135 | 291.85 | 282.89 |
| index_mul | 154 | 207.61 | 191.86 |
| index_prod | 167 | 219.39 | 210.96 |
| index_neg | 182 | 163.18 | 154.92 |
| index_C_mul | 187 | 75.59 | 73.21 |
| index_mul_left_weights | 192 | 160.66 | 148.56 |
| index_rename | 204 | 55.80 | 62.42 |
| index_le_card | 216 | 29.38 | 26.19 |
| index_unique | 226 | 374.66 | 341.66 |

Maximum374.66ms/341.66ms (index_unique); dominant terminal bound simplification steps
104.52ms/103.18ms. All19 FAST-BOARD,none borderline/over budget,zero deferrals,zero performance
patches or resource-limit changes. The shorter unique proof was slower than its original
leaf snapshot; clarity/structure improvement is claimed,not a speedup. A premature parser
attempt while sample1 was still running rejected incomplete anchors; only the complete
post-exit parse/table is accepted. No initial over-budget final sample was hidden.

## Phase 7: completion

All file phases complete with the explicitly scheduled parent project-end rename handoff.
All21 original reports,owner checkpoints,scoped approval ledger,independent review,actual
profile table and cumulative evidence are recorded. Header warning and preserved Theta
contract warnings are disclosed above; no other Index follow-up remains. No source edit
after the final freeze. Exact-path final commit and successful push on ramin-cleanup are
required before ownership release; the parent resumes with a fresh Separation owner.
