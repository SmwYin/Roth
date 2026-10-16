# Phase 6.6: `Roth.kroneckerExp_injOn`

Scope: proof body of this declaration only. Read-only preparation preceded the owner's explicit
GO after isolated pass2 completed. No Git operations, other-declaration edits, import changes,
new helpers, public signature changes, documentation changes, or shared-report edits.

Final source SHA256: `cc7b2786088d6c839d36a14d9b5b09a884eb1de1a0d521b3bc2b84c9772cbfcf`.
Source ownership is returned to the owner for full-project/separate checks and publication.

## Diagnosis

Read both installed skills, full installed `commands/buzz.md`, full `references/profiling.md`,
cleanup gates, relevant proof patterns, previous dedicated declaration audit, and actual pass2
trace. LSP goal inspection confirmed the precomposition intermediary, and positive local search
verified the function injectivity API before experiments.

Pass2 actual declaration cost: 1311.73 ms; proof 1238.880 ms. The 666.046 ms `refine` is the
**second** refine, containing `Nat.ofDigits_inj_of_len_eq`, rather than the first precomposition
refine. Its first digit-bound `simpa` costs 536.123 ms. The `hsum` terminal simp costs 515.887 ms.
The trace contains failed `Nonempty (Fin (Fintype.card σ))` instance searches of 384.902,
287.409, and 156.324 ms, under empty-universe/IsEmpty simp discharge. These nested times are
not additive. Root causes: broad simp triggering failing instance synthesis (taxonomy 1/2),
with a smaller expected-type improvement from splitting the first refine.

Fix: use `List.forall_mem_ofFn_iff.2` directly for digit bounds; constrain `hsum` to the actual
list-index, equivalence, and Fin identities. The terminal `simp only` is an explicitly measured
performance exception to the ordinary unsqueezed-terminal-simp rule. Split the first compound
refine into two `apply` calls to establish expected types early.

## Measured experiments

Each distinct fixture imports built `Roth.GenWronskian`, replays the complete proof under the
fresh name `Roth.perfKronecker`, and never calls the target theorem. Compiler runs were
sequential. Exact command for each fixture:

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FIXTURE
```

All fixture files/logs use `/private/tmp/roth-perf-kronecker-<row>.{lean,log}`. Totals include
anchored declaration command plus associated non-linter async work, never cumulative categories.

| Row | Change from original | Total ms | Result |
|---|---|---:|---|
| baseline | Exact original body | 754.506 | exit 0 |
| a1 | Split first refine into two applies | 713.342 | exit 0; insufficient source-level evidence alone |
| a2 | Restricted hsum simp; direct ofFn digit bounds | 171.546 | exit 1; missing list get/equivalence normalization |
| a3 | Add `List.get_ofFn`, length, Fin cast/equivalence identities | 172.675 | exit 1; dependent Fin casts remain |
| a4 | Direct getElem API instead of get_ofFn | 183.697 | exit 1; Fin cast value and eta remain |
| a5 | Add Fin cast value/eta normalization | 142.665 | exit 0; accepted mathematics |

Rejected a2–a4 times are failed elaboration measurements, not timings of valid proofs. Attempt
summary: `/private/tmp/roth-perf-kronecker-attempts.json`. A5 introduced deprecated
`Fin.coe_cast`; final source uses its verified replacement `Fin.val_cast`, with no warning.

Final actual source measurement, exit 0:

```text
lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/GenWronskian.lean
```

Complete 19-declaration trace: `/private/tmp/roth-perf-kronecker-final-source.log`, also archived
by owner as pass3. Target command 6.434 ms + proof async 154.692 ms + associated async 3.625 ms
= **164.751 ms**, roughly 8× faster than pass2. This is far below the 1000 ms budget; no target
borderline resweep is needed. Owner parsed all 19 declarations below budget after this change;
the owner retains the final resweep for the unrelated 842.94/917.18 ms borderline declarations.
No other declaration was edited to propagate a suspected issue without measurements.

## Gates

- `lake build Roth.GenWronskian`: actual exit 0, build completed successfully (1838 jobs).
  Log `/private/tmp/roth-perf-kronecker-module.log`.
- Final complete `lean_diagnostic_messages`: success true, partial false, timed_out false,
  zero errors, no failed dependencies. Exactly the five prior outside warnings remain:
  header, two warnings on the dependent-Wronskian theorem, DecidableEq on `det_sum_rows`,
  and Fintype on `exists_genWronskian_ne_zero`. No target or deprecation warning.
- `/private/tmp/roth-perf-kronecker-check.lean`, compiled by actual `lake env lean`, exit 0.
  It assigns the target to the exact original fully quantified public type, including `hk`;
  independently reproves the theorem from the original and final bodies under fresh names;
  and prints target/reproof axioms as exactly `[propext, Classical.choice, Quot.sound]`.
  The independent reproof does not reference the target theorem.
- Paired temporary `#count_heartbeats in` wrappers in that external fixture: original 6773,
  final 643 heartbeats (about 10.5× reduction). Log `/private/tmp/roth-perf-kronecker-check.log`.
- Automated source comparison against `/private/tmp/roth-perf-kronecker-start.lean` confirms
  byte-identical content outside this proof and byte-identical theorem statement.
- No new helper, axiom, sorry, native_decide, instance, limit raise, or profiling scaffolding.
- HAVE SCAN: only `hsum`, retained because it has proof content and is used for both digit sums;
  no single-use term-only have. Proof is 12 body lines, all at most 100 codepoints (maximum 99).
- Protected signature widths remain 49 and 64 codepoints; joining the full conclusion would
  exceed 100. No statement repacking is authorized or needed.

New external identifiers positively verified by compiled `#check` in the check fixture:
`List.get_eq_getElem`, `List.getElem_ofFn`, `List.length_ofFn`, `Equiv.apply_symm_apply`,
`Fin.val_cast`, `Fin.eta`, and `List.forall_mem_ofFn_iff`. LSP local search additionally verified
`List.forall_mem_ofFn_iff`, `List.get_eq_getElem`, and `Fin.val_cast` before final use.

No deferral or public-API proposal. Owner is responsible for the final cumulative resweep,
full-project build, separate build, and publication after revoking source ownership.
