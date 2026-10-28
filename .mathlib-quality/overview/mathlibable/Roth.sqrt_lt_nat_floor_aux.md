# Roth.sqrt_lt_nat_floor_aux — private-prefilter assessment (236/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.sqrt_lt_nat_floor_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.sqrt_lt_nat_floor_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:104–106`. For a real X at least2, its square root is strictly below the natural floor. The exact original kernel type is:

```lean
∀ {X : ℝ}, 2 ≤ X → √X < ↑⌊X⌋₊
```

Real input at least two. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and the original body printer elides 14524 characters; it is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.sqrt_lt_nat_floor_aux/native-type.json), [exact declaration](../evidence/Roth.sqrt_lt_nat_floor_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.sqrt_lt_nat_floor_aux/target-metadata.json), [whole declaring module](../evidence/Roth.sqrt_lt_nat_floor_aux/source-module.lean.txt).

## Structural, API and duplication review

Nat.le_floor gives floorX>=2, while Nat.lt_floor_add_one bounds X<floorX+1. Together these force X<floorX squared. Apply Real.sqrt_lt' with positive floor. This is the strict lower-bound half of the public two-sided floor statement, distinct from Nat.floor_le. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.sqrt_lt_floor` | `Roth/MainLemma.lean:115` | Supplies the strict square-root lower bound; Nat.floor_le independently supplies the non-strict upper bound. Full original body replayed. |

One explicit source caller, all in MainLemma.lean; one direct original value consumer. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.sqrt_lt_nat_floor_aux/callers.json), [raw source search](../evidence/Roth.sqrt_lt_nat_floor_aux/source-search.json), and [direct value consumers](../evidence/Roth.sqrt_lt_nat_floor_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.sqrt_lt_nat_floor_aux/canonical-snapshot.json), [entry](../evidence/Roth.sqrt_lt_nat_floor_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate236`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate236.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved; the original body printer has the disclosed elision, while the direct native type and axiom checks are complete. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.sqrt_lt_nat_floor_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.sqrt_lt_nat_floor_aux/native-receipt.json), [verification ledger](../evidence/Roth.sqrt_lt_nat_floor_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.sqrt_lt_nat_floor_aux/inputs.json), [baseline manifest](../evidence/Roth.sqrt_lt_nat_floor_aux/input-manifest.json), [build record](../evidence/Roth.sqrt_lt_nat_floor_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.sqrt_lt_nat_floor_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.sqrt_lt_nat_floor_aux/assessment.json), [overview entry](../evidence/Roth.sqrt_lt_nat_floor_aux/overview-entry.json), [portable validator](../evidence/Roth.sqrt_lt_nat_floor_aux/validate.py), [current manifest](../evidence/Roth.sqrt_lt_nat_floor_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
