# Final independent holistic simplify review: Roth/Index.lean

### Simplify pass — Roth/Index.lean

Outcome: PASS-THROUGH (explicit host adaptation)

Issues identified by independent holistic review:
- None requiring or recommending another source change.

Fixes applied:
- None.

Files modified:
- `.mathlib-quality/cleanup/Index-simplify.md` only.

The built-in Claude Code `/simplify` skill and `Skill` invocation tool are unavailable in this host. This report records a fresh independent equivalent holistic review, not a claim that the unavailable built-in ran. Read the lean4 and mathlib-quality skills, cleanup Phase 6.5 in `/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`, quality principles, proof patterns, style rules, review stages, Lean proof simplification and review taxonomy. No subagents were used. The final full project gates and performance sweep belong to the file owner.

## Frozen review input and scope

Reviewed all 245 lines, all 19 retained declarations, and the full cumulative diff against `e557886`. Current published checkpoint supplied by owner: `6f12d04`; reviewed working source includes its subsequent section-instance consolidation.

- SHA256: `30e6f151ddd2d9c344b9537d1bef87124e3f5814d2e58f3cba499a7e1ea6c939`.
- Git blob: `437a0de12a5951b2223b0b5287f7cff12f2accd4`.
- All original block comments and docstrings compare byte-for-byte identical.
- The complete original `index` defining declaration compares identical.
- Maximum line width: 100 codepoints; `git diff --check` passed.
- Import list compares identical with the original; two private wrappers were removed, leaving one definition, one private support lemma and 17 public theorems.

The three approved public changes are deliberately recognized as changes: remove unused decidable-equality instances, remove `index_le_card.hr`, and remove `index_mul_left_weights.hl`. Retained hP/Fintype/Unique contracts and zero conventions are respected. No new API change or public rename proposed. The owner controls exact actual-type compatibility checks and the four minimal Theta caller argument deletions; this review did not mutate or revalidate Theta independently.

## Holistic assessment

| Area | Independent finding |
|---|---|
| Mathematical strategy and reuse | The file moves from finite Taylor support to its attained real minimum, proves the lower-bound characterization, then transfers multiplication to mathlib weighted power-series order. This gives a clear dependency spine. `Finsupp.weight_eq_sum`, conditional infimum lemmas, `weightedOrder_mul`, and polynomial root-multiplicity/trailing-degree machinery are used directly. No second parallel theory or wrapper API is introduced. |
| Duplication and helpers | Removed finite/nonempty support wrappers were trivial conversions. The remaining private `mem_support_taylor_iff` expresses the file's repeated Taylor-support/Hasse-derivative bridge and is used throughout. Repeated support/coefficient conversions are short and context-sensitive; another helper would enlarge the API without removing a substantial repeated argument. `index_mul.hfin` is a useful twice-used local fact, rather than a new exported wrapper. |
| Clarity and structure | No proof exceeds 30 lines. The two longer bridges (`index_eq_weightedOrder_div`, `index_unique`) retain useful named series/polynomial and coefficient facts. Their two inequality directions track the mathematics. No independent long branch needs extraction. Finite-product induction is justified because the law requires nonzero factors; manufacturing a bundled morphism would add machinery. |
| Automation | Final simplifications close with explicit library calls or terminal simp. No nonterminal bare simp, speculative automation chain, heartbeat increase, trace option, sorry, or custom axiom was introduced in the diff. Earlier general automation audits remain relevant context; this review did not rerun the per-declaration Phase 4 search suite. |
| Import hygiene | Nine explicit imports are unchanged. Their concepts cover real infima/scaling, polynomial Taylor/root multiplicity, cast division, finite minima, power-series multiplication, weights and the project Taylor bridge. `Roth.Box` is transitively reachable through `Roth.Taylor`, but is also the directly used weight API; retaining that explicit dependency is reasonable. No broad tactic umbrella or new heavy dependency was added. Exact globally minimal imports were not proved, and no uncompiled import deletion is recommended. |
| Generality and contracts | Removing the ambient unused sigma decidability instance consolidates the 17 previously scoped omissions. The private support lemma still omits Fintype explicitly. Broader hP-free zero-case statements or weakening Fintype/Unique would change protected public contracts and are outside this approved pass. |
| Naming and formatting | Existing theorem names are recognizable in their algebraic role. The historical `index_hasseDeriv_ge` name is unchanged; the actual inequality is smaller-side-first. No rename is proposed here. Ordinary lambdas use ↦, signatures are packed within 100 columns, declarations have consistent spacing, and original documentation is preserved. Header metadata remains user-preserved; no warning suppression or invented authorship. |

## Concrete alternative tested and rejected

A genuine candidate arose during independent reading: replace `index_mul`'s reusable universal finite-order certificate with direct proofs at its two uses:

```lean
  rw [ENat.toNat_add (by simpa using hP) (by simpa using hQ), Nat.cast_add]
```

Created `/private/tmp/IndexFinalSimplify.lean` as a clone of the entire current source, changed its namespace to `RothFinalSimplify`, opened `Roth` only for the already-built weight API, and replaced just those three body lines. It does not import `Roth.Index`; consequently its index theorem proofs check against the freshly cloned definition and preceding cloned declarations. `lake env lean /private/tmp/IndexFinalSimplify.lean` completed with exit 0; output log `/private/tmp/IndexFinalSimplify.log` is empty.

After that independent candidate was identified, the owner pointed out an existing experiment. Inspection of `Index-index_mul.md` confirms the same inlined conversion was already measured at 334.97 ms, versus 209.54 ms for the selected shared certificate on an isolated repeat; another selected run was 308.43 ms under concurrent verification. Those are prior measurements, not new profiling performed by this reviewer. The alternative saves two source lines but repeats a conversion whose shared statement is useful and was measured faster. I do not recommend adopting it. No performance conclusion is inferred from the unprofiled clone compile alone.

## Release and limitations

All Lean/compiler requests issued by this reviewer finished before source authority was released. The full-clone compiler session completed exit 0. A separate broad filesystem search for command documentation was explicitly terminated once the exact command path was found; it was not a Lean request. There are no outstanding tool sessions or queued native MCP requests from this reviewer. No full-project build or profiler was run here. Source authority was released to the owner with the frozen SHA above; subsequent activity is report writing only.

Final result: PASS-THROUGH for this independent adapted holistic review. The owner must still run its frozen final compatibility, build, diagnostics and performance gates; this report does not substitute for them.
