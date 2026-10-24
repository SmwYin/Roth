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

The remaining three checkpoints and final file-wide profile/build gates are pending.

## Evidence

Scratch: `/private/tmp/roth-theta-amendment/`. The exact entry source and seventeen source/pin
identities are saved under `before/` and `source-before.json`. `Before.lean` captured the
four complete original TYPE/VALUE records with actual inference and standard-axiom checks
(exit 0, 58.809 s). Each subsequent `AuditN.lean` and paired command receipt/raw streams
records the cumulative old/new/independent checks, with no resource-limit increase.
