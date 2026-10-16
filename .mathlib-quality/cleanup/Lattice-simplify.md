# Lattice: independent holistic simplify review

Verdict: **ISSUES-FOUND**, resolved by owner (one concrete import-hygiene finding).

Reviewed source SHA-256:
`be707274cdc77d8e31a73497e8392e8a556f8d13af1e3c190e32ad9c9496a2b3`.
Review date: 2026-10-16. Base diff: `45cdf4f -- Roth/Lattice.lean`.
Production source was read-only throughout this review.

This is an explicit adaptation of the unavailable built-in Claude `/simplify` hand-off,
performed in a fresh independent review context. It is not a claim that that command ran.
Read both mathlib-quality and lean4 skills, the complete current module and base diff,
quality principles, proof patterns, style rules, PR feedback examples, Lean proof
simplification and review taxonomy references. Existing declaration audits were available
as context; this review did not repeat their exhaustive searches or certify their gates.

## Finding S1: unnecessarily heavy imports

At lines 1–2 the module imports real/complex powers and smoothness of the square root,
although the proof uses elementary square-root inequalities and finite products.
The required square-root lemmas are defined in `Mathlib.Analysis.Real.Sqrt`; the finite
product decomposition is in `Mathlib.Algebra.BigOperators.Fin`.

Exact proposed source edit (no other changes):

```diff
-import Mathlib.Analysis.SpecialFunctions.Pow.Real
-import Mathlib.Analysis.SpecialFunctions.Sqrt
+import Mathlib.Algebra.BigOperators.Fin
+import Mathlib.Analysis.Real.Sqrt
```

The Mathlib/project import-group separator and all subsequent source remain unchanged.
The original Pow.Real module publicly imports Pow.Complex; SpecialFunctions.Sqrt imports
calculus smoothness and derivative modules. Neither layer is required to elaborate this file.
No performance number is inferred from this structural dependency reduction.

Compiled evidence:

- `/private/tmp/roth-lattice-simplify-imports.lean` is a complete clone of the reviewed
  file with exactly the proposed imports and an additional nested namespace
  `Roth.LatticeSimplifyProbe`, so all 13 declarations elaborate independently.
- `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-lattice-simplify-imports.lean`
  completed with exit 0 and an empty diagnostic log at
  `/private/tmp/roth-lattice-simplify-imports.log`.
- The initial narrower experiment with only `Analysis.Real.Sqrt` and `Roth.Box` failed
  specifically at `Fin.prod_univ_castSucc`. Adding its defining BigOperators.Fin import
  resolved the failure. This is why the proposal explicitly includes that import.

Owner action: apply the two-line import substitution, then renew actual module and
downstream compilation/LSP/axiom gates. Removing transitive imports may expose an
implicit dependency in a consumer; the isolated clone alone does not certify consumers.

Owner subsequently confirmed the exact substitution was applied, yielding source hash
`a363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8`.
Renewed actual module, cumulative/downstream gates, and final profiling are owner work
and were pending at this review hand-off. No additional compiler or profiler call was
made after the owner froze that source.

## Remaining holistic assessment

- **Reuse and proof structure:** the reciprocal pairing uses the existing reflected-sum
  API; the fiber count uses mathlib's fiberwise cardinality and `card_bij`. There is no
  remaining duplicated substantial proof skeleton. The formerly duplicated extension
  identity in the bijection proof is now established once as `hext` and reused.
- **Helpers:** the three extracted auxiliaries separate the fiber bijection, trivial
  square-root regime, and induction step. Each has a distinct mathematical role and
  the headline theorem is a readable induction outline. Further splitting would mostly
  move the same arithmetic or casting scaffolding between one-use declarations.
- **Efficiency:** no new unbounded search, global simp attributes, resource-limit changes,
  or computed data definitions appear. Existing `grind` closes the linear cast-normalized
  fiber comparison. Algebraic normalization and arithmetic automation occur at the
  appropriate local boundaries. No profiling was performed in this review.
- **Instances:** only existing decidability arguments and local `classical` scopes are
  used; no global instance or instance diamond is introduced.
- **Generality/API:** the fiber auxiliary already abstracts the predicate. The small-λ
  auxiliary needs no positivity assumption on coordinates. The successor auxiliary
  takes positivity of only the last coordinate and a numerical induction estimate.
  No current call site requires a broader abstract algebra API. The previously closed
  `m ≥ 1` proposal was read and not reopened. All four public theorem types and existing
  documentation are retained by the import-only proposal.
- **Naming/style:** public names remain stable; new private names describe their roles
  and use `_aux`. Existing mixed-case suffixes track established Fin API names. No
  further concrete naming, formatting, scope, comment-preservation, or module-placement
  correction is required by this holistic review. The user-selected header policy stays
  unchanged.

No further substantive finding emerged. All scratch compilations finished before this
report was handed back; no background probe remains active. The owner must renew gates
against the applied source hash before final completion and profiling.

## Owner verification after application

Renewed all gates PASS at sourcea363c5532a161603683d3d9de0af3b5adbb7914a6df8dae8aba79216fd343df8.
Actual module5997 exit0; complete module/caller nativeLSP132 zero errors,1/3 inherited
warnings. Original whole-source independent reconstruction/all4 public exact-type equalities,
all4 external identifiers and all13 actual built axioms46950 exit0. Sequential full/separate
93589 exit0/exit0(82.60s/23.98s), stable hash. Logs
`/private/tmp/roth-lattice-simplify-{module,compatibility,identifiers,axioms,full,leaneval}.log`.
Final outcome: ISSUES-FOUND-AND-FIXED. No follow-up suggestion remains; actual profiling is
the following owner phase and was not performed by the reviewer.
