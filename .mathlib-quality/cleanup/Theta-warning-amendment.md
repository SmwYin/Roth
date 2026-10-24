# Approved Theta warning follow-up

Entry: clean published `7c49350`, following the completed 263-declaration cleanup.
The user explicitly approved removing `Θ_nonneg.hB/hr`, `Θ_le_card.hB`, and `Θ_mono.hr`;
`Θ_mono.hB` stays. The positive-denominator premise of `index_le_lem6` stays in the same
position, renamed `_hq` with a paper-setting comment. No other public assumption, Fintype
choice, metadata, toolchain or dependency pin is in scope.

Each theorem is checked and published before proceeding to the next. Actual compiler probes
bind old contracts to the complete pre-edit compiler TYPEs, recover them through adapters,
replay the new proofs independently without invoking the corresponding production theorem,
infer all actual opaque bodies, and check closedness and standard axioms. This is a scoped
amendment; the original exhaustive audits remain accepted and their count stays 263.

## Sequential checkpoints

1. **Θ_nonneg: PASS.** Removed only `hB/hr`; its original proof is unchanged and its docstring
   now states unconditional nonnegativity. The two internal uses drop the obsolete arguments.
   Their now-dead local `hB → hM1` chain is removed; its stale signpost is replaced by the
   accurate nonnegativity signpost at the remaining bound. Complete Theta diagnostics:
   zero errors, four remaining warnings. Build of Theta/MainLemma/Main/LeanEval: exit 0,
   114.129 s. Actual old-contract/new-independent/opaque-body check: exit 0, 41.056 s.
   The initial scratch checker rejected an unescaped generated `_@` Name; quoting was fixed
   without changing production code, and the complete checker was rerun successfully.

2. **Θ_le_card: PASS.** Removed only its unused `hB`; the proof and conclusion remain
   unchanged. Its private large-delta caller drops the now-dead `q > 1` derivation and the
   two premises used only to supply that discarded argument; both private-helper calls are
   updated. Public `Θ_lt` is unchanged. Complete Theta diagnostics: zero errors, three
   remaining warnings. Full downstream target build: exit 0, 117.753 s. Cumulative actual
   old-contract/new-independent/opaque-body checks: exit 0, 40.084 s.

3. **Θ_mono: PASS.** Removed only unused `hr`; the used `hB` and proof remain. Both
   internal calls drop the obsolete argument, and the prefix caller drops its now-dead
   local positivity proof. Complete Theta diagnostics: zero errors, two remaining warnings.
   Full downstream target build: exit 0, 114.300 s. Cumulative actual old-contract/
   new-independent/opaque-body checks: exit 0, 42.535 s.

Checkpoints 1–3 were published as `e2c4ef4`, `0d8f16f`, and `508f930`. The final
checkpoint records the fourth theorem and all completed file/project gates below.

4. **index_le_lem6: PASS.** The positivity premise stays in its original
   position as `_hq`; the proof comment records the paper's positive-denominator setting.
   Its positional caller remains valid, and there is no named `hq` call. Complete Theta
   diagnostics show zero errors and only the existing header warning. The full downstream
   target build passes (exit 0, 139.066 s). Cumulative actual old-contract/new-independent/
   opaque-body checks pass (exit 0, 78.333 s), including independent recovery of the old
   private large-delta helper. All 71 actual Theta constants use only standard axioms;
   default resource limits are unchanged.

Fresh independent Astra HIGH source review: **PASS**, no actionable finding. It independently
confirmed the exact authorized public changes, unchanged other public signatures (including
`Θ_lt`), retained conclusions/proof reasoning, complete callers and accurate documentation.
This is the available independent substitute for `/simplify`; no unavailable invocation is claimed.

## Evidence

Scratch: `/private/tmp/roth-theta-amendment/`. The exact entry source and seventeen source/pin
identities are saved under `before/` and `source-before.json`. `Before.lean` captured the
four complete original TYPE/VALUE records with actual inference and standard-axiom checks
(exit 0, 58.809 s). Each subsequent `AuditN.lean` and paired command receipt/raw streams
records the cumulative old/new/independent checks, with no resource-limit increase.

## Final file performance

Two serial actual whole-file profiles passed with exactly matching source, imported project
objects, pins and command: `lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 Roth/Theta.lean`. Sample A (214.072 s) required the same-source
repeat because two rows reached 750 ms; sample B (216.066 s) also passes every row strictly
below 1,000 ms. Maxima are 795.574 / 822.148 ms; no speedup or new repair is claimed.

All 50 written declaration payloads are bound to the actual trace and all 71 actual Theta
constants have kernel coverage. Timing sums disjoint outer command, asynchronous and
subsequent root costs; nested kernel children are included once through their parent.
Six pretty-printed payloads require parentheses normalization in addition to whitespace and
standalone-comment normalization; all remaining tokens agree. Repeated on-demand equation
checks are retained in their actual caller costs. No trace row is inferred from a source-only
name list. An attempted parse before stream completion stopped on an incomplete UTF-8 byte;
only the completed streams are used below.

| Declaration | Line | A (ms) | B (ms) | Dominant outer category, A |
|---|---:|---:|---:|---|
| `RSet` | 50 | 54.984 | 63.513 | `Elab.async` |
| `indexSet` | 56 | 32.418 | 32.110 | `Elab.command` |
| `Θ` | 62 | 6.091 | 7.342 | `Elab.command` |
| `one_mem_RSet` | 67 | 281.165 | 356.986 | `Elab.async` |
| `indexSet_nonempty` | 74 | 32.881 | 36.130 | `Elab.async` |
| `indexSet_bddAbove` | 81 | 310.294 | 315.111 | `Elab.async` |
| `index_le_Θ` | 93 | 38.426 | 47.317 | `Elab.async` |
| `Θ_nonneg` | 101 | 17.163 | 28.423 | `Elab.async` |
| `Θ_le_card` | 108 | 280.049 | 267.104 | `Elab.async` |
| `Θ_le_of_forall_index_le` | 118 | 39.988 | 36.864 | `Elab.async` |
| `Θ_mono` | 128 | 34.113 | 45.285 | `Elab.async` |
| `indexSet_comp_subset` | 135 | 234.528 | 261.880 | `Elab.async` |
| `Θ_equiv` | 153 | 53.396 | 78.344 | `Elab.async` |
| `isPrimitive_linear` | 161 | 220.261 | 251.662 | `Elab.async` |
| `isPrimitive_pow` | 169 | 50.411 | 59.699 | `Elab.async` |
| `exists_eq_pow_mul_of_rootMultiplicity` | 178 | 451.874 | 456.414 | `Elab.async` |
| `pow_rootMultiplicity_le` | 200 | 433.331 | 424.917 | `Elab.async` |
| `index_unique_le_log_div` | 217 | 634.017 | 582.374 | `Elab.async` |
| `Θ_unique_le` | 250 | 75.442 | 53.145 | `Elab.async` |
| `lem6M` | 264 | 60.116 | 27.008 | `Elab.command` |
| `lem6Φ` | 269 | 30.769 | 37.234 | `Elab.async` |
| `one_le_lem6M` | 273 | 140.191 | 157.320 | `Elab.async` |
| `floor_sq_div_two_le_sum` | 283 | 522.002 | 530.291 | `Elab.async` |
| `sq_div_three_lt_floor_sq_div_two` | 294 | 501.496 | 540.732 | `Elab.async` |
| `mul_div_two_le_sum_max_aux` | 298 | 516.785 | 474.883 | `Elab.async` |
| `mul_sq_div_three_le_sum_max_of_pos_aux` | 316 | 590.396 | 539.953 | `Elab.async` |
| `mul_sq_div_three_le_sum_max_aux` | 341 | 329.809 | 346.087 | `Elab.async` |
| `min_le_sum_max` | 356 | 168.455 | 171.427 | `Elab.async` |
| `sum_max_sub_le_index_det` | 370 | 705.104 | 709.948 | `Elab.async` |
| `index_separated_mul_le_aux` | 408 | 615.349 | 670.040 | `Elab.async` |
| `index_det_le` | 451 | 772.809 | 712.573 | `Elab.async` |
| `weight_le_delta_aux` | 488 | 398.915 | 377.727 | `Elab.async` |
| `mapped_det_ne_zero_aux` | 505 | 795.574 | 822.148 | `Elab.async` |
| `index_numeric_bound_aux` | 525 | 591.613 | 550.348 | `Elab.async` |
| `index_le_lem6` | 550 | 486.442 | 398.972 | `Elab.async` |
| `Θ_option_le` | 587 | 220.061 | 167.276 | `Elab.async` |
| `factorial_coefficient_le_two_pow_aux` | 603 | 272.716 | 251.185 | `Elab.async` |
| `two_pow_lt_rpow_aux` | 615 | 509.970 | 528.749 | `Elab.async` |
| `lem6M_lt` | 643 | 613.738 | 601.772 | `Elab.async` |
| `lem7_Φ_bound` | 672 | 662.769 | 692.566 | `Elab.async` |
| `lem7_numeric` | 703 | 682.494 | 624.269 | `Elab.async` |
| `theta_scaled_unique_le_aux` | 736 | 551.220 | 533.575 | `Elab.async` |
| `theta_delta_succ_lt_aux` | 761 | 651.512 | 653.420 | `Elab.async` |
| `theta_prefix_lt_aux` | 770 | 654.219 | 649.579 | `Elab.async` |
| `theta_lt_base_aux` | 812 | 543.230 | 506.288 | `Elab.async` |
| `theta_denominators_one_lt_aux` | 827 | 140.836 | 89.700 | `Elab.async` |
| `theta_phi_lt_aux` | 834 | 607.489 | 616.879 | `Elab.async` |
| `theta_lt_succ_aux` | 885 | 595.610 | 617.432 | `Elab.async` |
| `theta_lt_of_large_delta_aux` | 926 | 444.852 | 476.699 | `Elab.async` |
| `Θ_lt` | 956 | 351.762 | 338.945 | `Elab.async` |

## Final project gates

- Full `lake build`: exit 0, 26.202 s, 2,467 jobs. Subsequent separate
  `lake build Roth.LeanEval`: exit 0, 4.045 s.
- Complete native diagnostics for final Theta, MainLemma, Main, LeanEval and root: success,
  nonpartial, no timeout or failed dependency, zero errors. Theta/MainLemma/Main each have
  only their existing header warning; LeanEval and root are clean.
- Actual project warning inventory: **14**, reduced from 19. The remaining warnings are
  twelve missing-authoritative-metadata warnings and two retained public `Fintype`
  assumptions (`exists_genWronskian_ne_zero`, `exists_det_eq_mul`). All five targeted Theta
  binder warnings are resolved. No linter suppression or invented metadata was added.
- Only `Roth/Theta.lean` changed among the fourteen source files. All other thirteen sources
  and all three configuration/dependency pins match the clean entry exactly. Theta imports
  are unchanged; source has 979 lines, width ≤100, no trailing whitespace or trust/resource
  escape. All affected calls are internal and compile; there are no named `hq` calls.
- Existing accepted audits and unchanged-file performance/native evidence remain valid;
  no new 263-declaration audit or runtime speedup is claimed. Conclusions and old contracts
  are preserved through the checked adapters; the authorized statements accept fewer premises.

Evidence: completed `step4-{build,contracts}` and `final-{build,eval-build}` receipts/raw streams,
`Audit4.lean`, `theta-constants.json`, `checkpoint-diagnostics.json`, `final-diagnostics.json`,
`source-final.json`, `final-warning-inventory.json`, the two complete profile streams/receipts,
`profile-{a,b}-rows.json` and `profile-comparison.json`, all under the scratch directory above.
All required follow-up validation passes; no source change or validation gate remains.
