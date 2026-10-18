# Independent initial audit: int_factorization_eq_aux

Written before any repository source edit. Scope: this added private helper and necessary exact call substitution only. Private literature exemption: no public theorem proposed or changed. Initial exact added-helper snapshot: /private/tmp/roth-separation-d29-first-freeze.lean.

Mathematics: the coefficient embedding ℤ → ℚ is injective; it respects multiplication, renaming, and polynomial evaluation, so a mapped factorization descends to integer equality.

1. LINT: initial live goal succeeds; complete diagnostics pending.
2. HAVE SCAN: none.
3. SET_OPTION: none.
4. SIMP SQUEEZE: none.
5. NAMING: descriptive snake_case private _aux, no forbidden pattern.
6. LINE PACKING: initial signature table below; removed helper has no final signature.
7. BY PLACEMENT: correct.
8. FORMAT: 2-space indentation, no internal blank lines.
9. COMMENTS: none inside helper; preserve all caller comments/docstrings.
10. DOCSTRING: private helper appropriately has none.
11. VISIBILITY: private, one use.
12. STRUCTURE: four physical tactic lines; caller eleven, inline candidate sixteen unless compressed.
13. MATHLIB: all five actual methods executed; constituent map/rename/injectivity/aeval lemmas found, exact? timed out.
14. JUNK DEF: n/a lemma.
15. EXISTS LEMMA: n/a equality.
16. SHOW vs CHANGE: none.
17. PUSH_NEG: none.
18. GENERALISE: binder table below.
19. INEQUALITY: no occurrences in helper signature/hypotheses/body; table below.
20. NORMAL-FORM: polynomial equality reflected through injective map is canonical.
21. SYNTAX-GEN: inline single-use transport; remove intermediate V-prime binder locally.
22. IMPORT-FANOUT: no added import.
23. CASTS: X-none ascriptions fix coefficient ring; Int.castRingHom target fixes ℚ; none redundant.
24. INSTANCE-NAME: n/a no instances.

## Initial signature widths

| Line | Width | Next token | width+1+token | Status |
|---|---:|---|---:|---|
| 1 | 100 | `{F` | 103 | ok |
| 2 | 76 | `(hF` | 80 | initial repack if retained |
| 3 | 79 | `Polynomial.aeval` | 96 | initial repack if retained |
| 4 | 65 | `F` | 67 | initial repack if retained |
| 5 | 85 | `` | n/a | ok |

## Effective binders / generalisation

| Binder | Probe and disposition |
|---|---|
| τ : Type* | Already universe polymorphic, unrestricted; finite/decidable instances explicitly omitted and absent in live goal. |
| U | Occurs in conclusion and factor hypothesis; deletion ill-formed, not compiler drop-tested. |
| V | Occurs in conclusion and map hypothesis; deletion ill-formed, not compiler drop-tested. |
| V-prime | Eliminable by substitution along hVmap; exact independent probe planned. |
| F | Occurs in hypothesis and conclusion; deletion ill-formed, not compiler drop-tested. |
| hVmap | Essential connection to V-prime; eliminate with V-prime substitution instead. |
| hF | Essential mathematical input; no weakening to inequality; no compiler negative test claimed. |
| ℤ/ℚ | Abstract injective coefficient hom is the general mathematical principle already in mathlib; avoid a new generalized wrapper. |

## Inequality occurrence table

| Scope | Occurrences | Action |
|---|---:|---|
| Entire helper | 0 | none |

## Actual search evidence

Local index warming but source hit Polynomial.map_aeval_eq_aeval_map. Loogle returned map_rename/map_comp_rename; LeanSearch returned map_injective/coeff_inj; LeanFinder returned map_eval/map_eval₂. Direct source and standard-file search and #checks to be logged. Native live goal confirms both omitted instances absent. Automation actual live trials: grind fails; simp_all no progress; aesop incomplete; exact? 200000-heartbeat timeout. Multiline candidate through multi_attempt had parser ambiguity with following tactics and is not claimed as a verified failure of the mathematics.


## Compiled decision

Full-module scratch proposal /private/tmp/roth-equality-inline-proposal.lean compiled with exit 0; log /private/tmp/roth-equality-inline-proposal.log. Main actual physical body is 15 lines, longest inserted branch 4 lines. Parent explicitly authorizes single-use wrapper removal. Applied only helper deletion plus its call substitution. No public type or documentation changed.

## All 42 golf rules

- [1.1] n/a no by-exact wrapper.
- [1.2] n/a no by-rfl.
- [1.3] n/a no rewrite followed by exact.
- [1.4] n/a no simp/exact.
- [1.5] n/a no trailing rfl.
- [1.6] n/a no constructor.
- [1.7] n/a injectivity application generates nontrivial rewrite goal.
- [1.8] n/a no contradiction.
- [1.9] n/a no eta lambdas in helper.
- [1.10] n/a no helper have.
- [1.11] n/a no intro.
- [1.12] n/a no show.
- [1.13] n/a no projections.
- [1.14] already single rw list.
- [1.15] n/a no simp only.
- [1.16] n/a no bare simp.
- [1.17] n/a map_injective explicit coefficient hom fixes inference.
- [1.18] n/a no trailing tactic parentheses.
- [1.19] n/a no push_neg.
- [1.20] n/a not existential; single-use equality wrapper inlined under parent authorization.
- [2.1] actual live grind failed.
- [2.2] n/a no grind prefix.
- [2.3] actual simp_all no progress; multiline simpa probe parsing inconclusive, direct rw transport retained.
- [2.4] n/a no analytic function property.
- [2.5] n/a no positivity goal.
- [2.6] n/a no inequalities.
- [2.7] n/a no linear arithmetic.
- [2.8] actual live aesop incomplete.
- [2.9] n/a symbolic map equality, no numeric computation; cast injectivity used directly.
- [2.10] n/a arbitrary polynomial equality is not closed computation.
- [2.11] n/a no division.
- [2.12] n/a no ring ending or polynomial algebraic hypothesis combination.
- [2.13] n/a no symmetric cases.
- [2.14] n/a no calc.
- [2.15] n/a one goal after injectivity.
- [3.1] n/a rw already.
- [3.2] n/a no legacy analytic tactics.
- [3.3] n/a no omega.
- [3.4] n/a no rcases rfl.
- [3.5] n/a removed one-use private transport; no global attributes warranted.
- [3.6] n/a no simp_all only.
- [3.7] n/a no limits.

## Step-back review

Exact? reached the default heartbeat bound; grind/simp_all/aesop did not replace the transport. Direct injectivity plus naturality is the mathematical proof; moving those four lines into their only use removes the unnecessary wrapper and avoids a new generic helper. No new helper added.

## Verification so far

Exact INITIAL helper signature independently proved as initial_type_independent, with no self/helper invocation: /private/tmp/roth-equality-independent.lean and .log, exit 0, only propext, Classical.choice, Quot.sound. Complete unfiltered native final diagnostics: /private/tmp/roth-equality-final-lsp.json, partial=false, success=true, 0 errors / 3 warnings / 0 infos. Warnings: preserved header plus both existing caller-30 instance warnings (DecidableEq and Fintype); caller-30 audit remains parent scope.

## Gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | lake build Roth.Separation exit 0, 1877 jobs; /private/tmp/roth-equality-build.log |
| definition_protected | pass | no definition changed, focused diff /private/tmp/roth-equality-worker.diff |
| theorem_statement_protected | pass | private-wrapper removal explicitly authorized; both public signatures byte-identical to start |
| structure_gate | pass | removed helper; retained main 15 physical body lines, equality branch 4 lines |
| naming_gate | pass | no renamed or added declaration, removed descriptive name |
| line_packing_gate | pass | initial full signature table above, final target signature absent; caller signature unchanged |
| inequality_orientation_gate | pass | zero occurrences for removed target/inserted transport branch |
| actual built axioms | pass | /private/tmp/roth-equality-built-axioms.log: both Roth.exists_int_factors and Roth.exists_det_eq_mul use only propext, Classical.choice, Quot.sound; exact suffix environment lookup found no removed helper constant |
| native LSP | pass | /private/tmp/roth-equality-final-lsp.json: complete, 0 errors / 3 warnings / 0 infos |

No new helpers; no rename queued; no concrete API proposal pending from this worker. Parent owns caller-30 instance decision and cumulative verification. Existing public conjunction signatures are preserved by explicit task instruction; no change to public result packaging is proposed.

## Eleven completion steps

- [x] Step 1: reference documents read (Lean and quality skills, full golfing/proof-pattern references, cleanup Phase 4/gates, generalisation/search/style/naming/profiling).
- [x] Step 2: all 24 audit items above, written before source edits.
- [x] Step 2.5: five actual search methods above; no unavailable remote method represented as absence.
- [x] Step 2.6: every effective binder reviewed; omitted finite/decidable assumptions confirmed absent in live goal. No unexecuted negative compiler claims.
- [x] Step 2.7: full initial signature width table; removed declaration has no final lines to repack.
- [x] Step 2.8: inequality occurrence table above.
- [x] Step 3: all 42 golf-rule statuses above.
- [x] Step 4: step-back review above; authorized single-use wrapper removal.
- [x] Step 5a: complete native diagnostics above.
- [x] Step 5b: actual module build, exact initial independent proof, actual built axiom checks and diff gates above; profile result below.
- [x] Step 6a: no renames required, no sidecar mutation.

Arithmetic: 555 → 548 physical source lines, net -7. Helper body 4 → absent; main body 11 → 15. Focused worker diff removes 12 lines and adds 5 (including changed refinement), yielding -7. Original public batch retained-count bookkeeping remains parent-owned.

Correction to initial estimate in audit item 12: measured compiled caller body is 15 physical lines (not the preliminary unmeasured sixteen-line estimate); no tactic compression was required. Initial search source inspection: Polynomial/AlgebraMap.lean:499, MvPolynomial/Eval.lean:396, MvPolynomial/Rename.lean:68; #check outputs included in independent-proof log.

## Isolated performance and freeze

All earlier Lean/MCP/compiler requests were drained before final actual-module profile launch. Command: lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean, exit 0; raw /private/tmp/roth-equality-drained-profile.log. Anchored totals count only outer command plus outer async proof, without nested double counting.

| Log | Target | Command ms | Proof ms | Total ms | Anchors |
|---|---|---:|---:|---:|---|
| roth-integral-drained-profile.log | Roth.exists_int_factors | 101.770 | 448.785 | 550.555 | 934637, 934718 |
| roth-integral-drained-profile.log | Roth.exists_det_eq_mul | 113.589 | 453.340 | 566.929 | 995953, 1017462 |
| roth-equality-drained-profile.log | Roth.exists_int_factors | 90.686 | 474.046 | 564.732 | 903663, 903747 |
| roth-equality-drained-profile.log | Roth.exists_det_eq_mul | 130.195 | 430.556 | 560.751 | 988420, 1009988 |

Removed helper has no final cost. Changed caller 29 and downstream caller 30 are each below 750 ms and 1000 ms, so neither requires a worker repeat. Parent explicitly retains responsibility for two cumulative sweeps because an earlier unrelated helper had a borderline baseline. No whole-file improvement claimed. Machine-readable anchors: /private/tmp/roth-equality-profile-anchors.json.

Every request is now completed/drained, including native automation/search/LSP, scratch proposal, exact INITIAL independent proof, actual module build, actual built axiom checks, and final profiler. No background process remains owned by this worker.

Freeze SHA256: `625a4b282d0e0e7ecb78a2e9f4eb3aec52ac14cc3cafae9eb1d21285d50977fc`. Frozen source has 548 physical lines. ALL source ownership is revoked: this worker is report-only and will make no further Lean source edits. Parent must perform cumulative original/public compatibility, all actual axioms, full LSP/profiles, full project and separate LeanEval verification before publication.
