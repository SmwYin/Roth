# GenWronskian — independent Phase 6.5 simplify review

Reviewed the entire 262-line `Roth/GenWronskian.lean` and cumulative
`git diff 21318b1..HEAD -- Roth/GenWronskian.lean`, independently of the dedicated
declaration audits. Reviewed source SHA-256:
`175ce6a3ece377484ccf54ad54479d3f79e425080364fbbcbe635484a9d482c9`.
The final source checksum remained identical after all probes.

This is the fresh-reviewer fallback for unavailable builtin `/simplify`. Read the installed
mathlib-quality and lean4 skills and relevant style-rules, golfing-rules, proof-patterns,
cleanup-gates, and proof-simplification references. Source, shared logs, Git, and build
artifacts were not changed. Only this report is owned by this reviewer.

## Compiled finding: two redundant Mathlib imports

Remove these two lines together:

```diff
 import Mathlib.Data.List.Indexes
-import Mathlib.Data.Nat.Digits.Defs
-import Mathlib.LinearAlgebra.Multilinear.Basic
```

The full private copy with this exact change compiled successfully. Required digits and
multilinear APIs are already available through the remaining imports. This is an import
minimality proposal, with no changes to declarations, proofs, definitions, or comments.
Retain `Mathlib.Data.List.Indexes`: removing all three explicit Mathlib imports failed at
`List.mapIdx_eq_ofFn`, so the fully reduced import set needs that module.

## Whole-file inspection

- Reuse: the determinant expansion uses `MultilinearMap.map_sum_finset` and
  `map_smul_univ`; digit uniqueness uses `Nat.ofDigits_inj_of_len_eq`; the operator
  representation uses the existing span/linearCombination API. A local source search
  for derivative/aeval chain rules in Mathlib's MvPolynomial directory found no existing
  replacement for `derivative_aeval`. No new helper is proposed.
- Structure: the derivative induction and finite operator-span representation form a
  coherent chain. `derivative_kronHasse_aux` isolates the generator identity, and
  `wronskian_kronecker_eq_sum_aux` isolates the determinant transport. The latter's
  explicit `hc` argument keeps the chosen representation local to the caller. Retain
  these helpers; neither is a trivial existential witness or a duplicated bridge.
- Definitions: retain `genWronskian`, `kronecker`, and `kroneckerExp` as mathematical API.
  The private operator and span definitions are used across multiple declarations and
  express the shared induction invariant. Their inlining would duplicate meaningful
  structure. The cumulative diff does not change the public definition values.
- Mechanical constructs: scanned every `have`, `let`, `set`, `obtain`, `convert`, and
  simplification block. The remaining `hsum` has a tactic proof and supplies both sides
  of the digit comparison. The `det_sum_rows` hypothesis is transformed before use;
  a direct terminal simplification was actually tested and failed (below). No remaining
  no-`by`, single-use `have` requires inlining. The main theorem's local `k` names the
  degree bound and is used repeatedly. Its already-inlined degree bound does not need
  another local fact or another helper.
- Efficiency: the cumulative rewrite replaces manual coefficient/support case splits,
  ring reasoning, and inverse manipulation with existing APIs and direct inequalities.
  There is no new broad search tactic, raised option, axiom, or native decision step.
  These are structural observations only; this reviewer made no per-declaration timing
  claim. The owner runs the separate profiling phase after this review.
- API and documentation: leave the known public assumption proposals (unused Fintype
  and det_sum_rows DecidableEq) pending user approval. They are not mandatory findings
  of this review. Preserve all existing docs/comments and the user-preserved header.
  Caller search found the expected GenWronskian uses in `Roth/Separation.lean`; no
  public rename or statement change is proposed.

## Actual compiler probes

All commands ran from `/Users/ramin/LEAN/Roth`; each path below is a full private copy
of the reviewed source with only the stated candidate change. Each command used
`/Users/ramin/.elan/bin/lake env lean <path>`; no shared module build was run.

| Private path | Candidate | Exit/result |
| --- | --- | --- |
| `/private/tmp/roth-genwronskian-final-simplify.lean` | Replace final `simp only … at h ⊢; exact h` in det_sum_rows with terminal `simpa […] using h` | 1; Matrix.of normalization/type mismatch |
| `/private/tmp/roth-genwronskian-final-simplify-direct.lean` | Direct terminal simpa using map_sum_finset, including map_smul_univ | 1; scalar extraction and Matrix.of normalization mismatch |
| `/private/tmp/roth-genwronskian-final-simplify-of.lean` | First candidate plus explicit Matrix.of simplification | 1; normalization leaves Equiv.refl application mismatch |
| `/private/tmp/roth-genwronskian-final-simplify-noimports.lean` | Remove all three Mathlib imports | 1; unknown List.mapIdx_eq_ofFn and corresponding unsolved digit-sum goal |
| `/private/tmp/roth-genwronskian-final-simplify-minimports.lean` | Retain List.Indexes; remove Digits.Defs and Multilinear.Basic | **0**; full file accepted |

The successful command was exactly:

```text
/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-genwronskian-final-simplify-minimports.lean
```

The successful compile emitted only the known unused `[Fintype σ]` section-variable
warning for `genWronskian_eq_zero_of_not_linearIndependent`. No warning suppression
was introduced. Rejected proof proposals were never applied to the source. All compiler
probes are complete; no orphan compiler session remains.

## Handoff

**Ready for owner implementation and re-gating:** remove the two compiled redundant
imports above. The remainder is checked PASS-THROUGH after specific holistic inspection
and bounded failed proof-simplification probes. This independent review does not replace
the owner's module/project builds, public-type checks, LSP checks, or profiling gates.
