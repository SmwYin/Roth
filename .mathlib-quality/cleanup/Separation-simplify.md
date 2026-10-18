# Final independent holistic simplify review: Roth/Separation.lean

### Simplify pass — Roth/Separation.lean

Outcome: ISSUES-FOUND-AND-FIXED (explicit independent host adaptation)

Issues identified by independent review:
- The scalar redistribution proof used `linear_combination` for an equality that follows directly from commutative multiplication and inverse cancellation. This was also the sole use of the explicit LinearCombination tactic import.

Fixes applied:
- Append `mul_mul_mul_comm, ← C_mul, mul_inv_cancel₀ hg, C_1, one_mul` to the existing rewrite chain in `rescale_separated_factor_aux`.
- Remove its local cancellation certificate, `linear_combination` invocation, and the explicit `Mathlib.Tactic.LinearCombination` import.

Files modified:
- `Roth/Separation.lean`.
- `.mathlib-quality/cleanup/Separation-simplify.md`.

The built-in Claude Code `/simplify` and its `Skill` invocation tool are unavailable on this host. This records a fresh independent equivalent review of reuse, quality, and efficiency; it does not claim the unavailable built-in ran. Read lean4 and mathlib-quality skills; cleanup Phase 6/6.5 at `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`; cleanup-gates, golfing-rules and proof-patterns references. No subagents were used. This review complements the completed per-declaration audits and leaves the owner's final cumulative gates and profiling to the owner.

## Review input and contract

Read every one of the initial 560 lines and the entire cumulative diff against `a39317e:Roth/Separation.lean`, including the complete separated-basis and integrality reorganizations. Original snapshot: `/private/tmp/roth-separation-original.lean`, 618 lines and 30 original declarations. Initial retained source: 27 declarations, supplied checkpoint `d007c3e`, SHA256 `2f1dd34c7e9556683e147c522310bb4e07f9a21a6145a2f58018f928fb4b67f1`.

The source defines coefficient extraction in one distinguished variable and proves four advertised results: an independent separated representation, determinant factorization into generalized/univariate Wronskians, integral rescaling, and the degree-controlled integral factorization of Lemma 2. The fixed dependency spine is appropriate to those results.

The public definition `coeffNone` compares byte-for-byte identical with the original. All Lean block comments, including module and declaration documentation, compare byte-for-byte identical. The only approved public changes remain the twelve τ-instance removals already applied by the owner (eleven pairs of Fintype/DecidableEq, final theorem DecidableEq only). Public domains, theorem contracts, names and documentation remain protected. The unused public Fintype instance and header metadata are deliberately retained. No previously declined API widening or wrapper deletion was reopened.

## Holistic assessment

| Area | Independent conclusion |
|---|---|
| Reuse and strategy | Coefficient extraction now uses `optionEquivLeft`; support restriction replaces the bespoke degree-bounded submodule. `Finset.gcd_eq_sum_mul` replaces the original Bézout induction; `Polynomial.mem_map_range` replaces manual reconstruction of the integral polynomial. These are substantive uses of existing APIs rather than parallel theories. The determinant proof uses mapped determinants and matrix multiplication directly. |
| Definitions | `coeffNone` provides the module's advertised coefficient interface and is used in both expansion and basis construction. Replacing it with notation would affect the public contract and reduce discoverability. No new definition, abbreviation, instance, or theory layer was introduced. |
| Helper necessity | The six retained added private helpers divide the long arguments into independent mathematical stages: coordinate-polynomial independence, basis reconstruction, basis size/degree control, scalar redistribution, coefficient integrality, and rational determinant factors. None has a body consisting of a trivial existential witness. Recombining them would obscure these stages and recreate overlong headline proofs. |
| Duplication | The two short `optionEquivLeft`/rename equalities share a three-line extensionality argument; another helper would add a declaration and signature overhead for little gain. Degree proofs share nonzero-factor transport but differ in their complementary variable and natural-degree conclusions; the direct library calls remain reasonable. The integral factors' nonzero facts and degree facts concern fixed common witnesses and are correctly recombined in one result. |
| Shared witnesses | The basis helper's existential length and basis carry their associated bounds together. The rational factor helper similarly carries a shared dimension, operator family, and factors. Splitting these into independent existential theorems would not preserve witness correlation. No such split is recommended. |
| Structure | All four headline tactic bodies stay within 15 lines: 14, 10, 15 and 11, respectively. The longest retained tactic body is 30 lines (`exists_primitive_smul_eq`); local branches are at most ten. The new scalar proof is two tactic lines. The field/integrality sections follow the mathematical dependency order. No extra decomposition is necessary. |
| Automation and efficiency | Existing targeted rewrite/simp chains generally expose the mathematical bridge without broad search. The one unnecessary ring-normalization invocation identified here was replaced by direct multiplication/cancellation lemmas. No timing claim is made from this unprofiled change. The owner must rerun the actual final per-declaration profiles on the new SHA. No heartbeat limit, trace scaffold, `sorry`, custom axiom, unsafe shortcut, or native decision procedure was introduced. |
| Imports | `Polynomial.Eval.Subring` supports the new coefficientwise map-range argument. GCD, multivariate polynomial, coefficient-norm and generalized-Wronskian dependencies correspond to used mathematics. Removing the sole explicit tactic dependency is validated by an actual module build. Exact globally minimal transitive imports were not claimed. |
| API and generality | Private reconstruction already works over CommSemiring; coordinate independence over CommRing/modules; redistribution over any field; the final rational stage over Finite τ. These private generalizations are coherent. Public coefficient-domain and Fintype contracts remain as authorized. The thin public wrappers have protected callers and were retained. |
| Naming, packing and comments | Mathematical snake_case theorem names and the private unnumbered `_aux` convention are appropriate. No rename request arose. Initial maximum width is 100 codepoints and the edit shortens the file. Proof organization retains all original source comments and documentation; no fabricated copyright/license data or linter suppression was added. |
| Trust | A fresh proof of exactly the scalar helper's mathematical signature uses only ordinary kernel-checked algebra. Actual helper and downstream public integrality/factorization axioms are checked below. This review does not substitute for the owner's final all-original/public/actual declaration compatibility and trust sweep. |

## Concrete candidate and rejected attempts

The successful candidate was first checked using native `lean_run_code` as a self-contained example with the exact scalar helper signature. It returned success true, timed_out false, and no diagnostics. The applied proof is:

```lean
  rw [hF, hUmap, map_mul, Polynomial.aeval_C, algebraMap_eq, smul_eq_C_mul, map_mul,
    rename_C, mul_mul_mul_comm, ← C_mul, mul_inv_cancel₀ hg, C_1, one_mul]
```

A preceding native `lean_multi_attempt` at the old local-cancellation line tested general AC simp and a calc rearrangement. The simp candidates left cancellation goals; the calc candidate oriented its first equality incorrectly. Replacing the line also left the old local-have continuation in that tool's temporary script, producing parser diagnostics. Consequently none of those temporary attempts was treated as a valid full-proof result or applied. The self-contained successful candidate and actual source build supersede them. A direct `lean_verify` of the internal private name was rejected by that tool's name validator, and an explicit numeric private name was not parsable in `#print axioms`; the final fresh compiler probe instead resolves that declaration through the environment and calls `Lean.collectAxioms`.

## Actual verification and release

- `lake build Roth.Separation` completed exit 0, including the proof simplification and import deletion.
- Complete native LSP diagnostics returned success true, partial false, timed_out false, failed_dependencies empty. The only two warnings are the deliberately preserved header metadata and public `exists_det_eq_mul` Fintype contract.
- `git diff --check -- Roth/Separation.lean` exited 0.
- Fresh standalone compiler probe: `/private/tmp/roth-separation-final-simplify.lean`; it independently states and proves the scalar helper signature and resolves actual helper/public downstream declarations through the environment for standard-axiom checking.

The fresh compiler probe completed exit 0. `separationRescaleReview`, actual `_private.Roth.Separation.0.Roth.rescale_separated_factor_aux`, `Roth.exists_int_factors`, and `Roth.exists_det_eq_mul` each depend only on `[propext, Classical.choice, Quot.sound]`.

Final source: 556 lines, 27 retained declarations, SHA256 `f3c7999541130206a760ab9a6e5a2e9446402faf18c878d9fcfd88ad7cda26d0`. No declarations, public types, or documentation changed during this review.

All native Lean requests and compiler processes issued by this reviewer have completed; no pending requests or tool sessions remain. All source ownership is revoked and returned to the file owner; further reviewer activity is report-only. The owner must run the final actual-source compatibility, caller diagnostics, builds, and performance sweeps on this SHA. No further source suggestion remains open from this review.

The supplied earlier all-27 Separation profile maximum 705.265 ms belongs to the input SHA and is historical evidence, not certification of the new SHA. The owner's Theta ordinary-build/full-LSP results are also prior owner evidence; this reviewer made no Theta edits or requests. Theta's interrupted/failed profiled compile is not a successful sample. Theta performance work remains the next file's work; no whole-project performance claim is made here.

## Owner final mechanical follow-through
After the independent review, the owner found three remaining ordinary lambda arrows in aeval_X_eq_rename and degreeOf_none_rename_mul_aeval. They were normalized from => to ↦; valid conv_lhs => syntax remains. This syntax-only adjustment preserves exact mathematical types/values and adds no declaration. All final diagnostics/contracts/axioms/builds/profiles are refreshed on this later source; pre-normalization profiles remain preserved as historical evidence rather than labeled final.
