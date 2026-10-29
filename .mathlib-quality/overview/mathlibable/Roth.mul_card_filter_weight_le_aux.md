# Roth.mul_card_filter_weight_le_aux — private-prefilter assessment (260/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.mul_card_filter_weight_le_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.mul_card_filter_weight_le_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:569–579`. For arbitrary real scale a, bounds a times the number of lattice indices below the corresponding centered cutoff by half the coordinate box cardinality. The exact original kernel type is:

```lean
∀ {m : ℕ},
  0 < m →
    ∀ (r : Fin m → ℕ),
      (∀ (j : Fin m), 0 < r j) →
        ∀ (a : ℝ), a * ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - 4 * a * √↑m) / 2}.card ≤ ↑(∏ j : Fin m, (r j + 1)) / 2
```

Positive dimension and positive degree vector; arbitrary real scale. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.mul_card_filter_weight_le_aux/native-type.json), [exact declaration](../evidence/Roth.mul_card_filter_weight_le_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.mul_card_filter_weight_le_aux/target-metadata.json), [whole declaring module](../evidence/Roth.mul_card_filter_weight_le_aux/source-module.lean.txt).

## Structural, API and duplication review

Split on a>0. In the positive branch use card_filter_weight_le with loss4*a*sqrt(m), multiply by a, and clear the nonzero factors using m>0 and Real.sqrt_pos before ring normalization. In the nonpositive branch the left side is nonpositive while the cardinality half is nonnegative. The sole rpow-bound existence caller chooses a=c*f.natDegree to supply the counting-budget premise of pigeonhole_count. This all-real-scale helper is stronger in scope than the positive-scale cancellation probe from the lambda assessment. Explicit project dependencies are `Roth.box`, `Roth.card_filter_weight_le`, `Roth.weight`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | `Roth/MainLemma.lean:581` | Chooses scale c*f.natDegree to establish the c*n*D half-box budget for pigeonhole_count. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.mul_card_filter_weight_le_aux/callers.json), [raw source search](../evidence/Roth.mul_card_filter_weight_le_aux/source-search.json), and [direct value consumers](../evidence/Roth.mul_card_filter_weight_le_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.mul_card_filter_weight_le_aux/canonical-snapshot.json), [entry](../evidence/Roth.mul_card_filter_weight_le_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate260`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate260.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.mul_card_filter_weight_le_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.mul_card_filter_weight_le_aux/native-receipt.json), [verification ledger](../evidence/Roth.mul_card_filter_weight_le_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.mul_card_filter_weight_le_aux/inputs.json), [baseline manifest](../evidence/Roth.mul_card_filter_weight_le_aux/input-manifest.json), [build record](../evidence/Roth.mul_card_filter_weight_le_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.mul_card_filter_weight_le_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.mul_card_filter_weight_le_aux/assessment.json), [overview entry](../evidence/Roth.mul_card_filter_weight_le_aux/overview-entry.json), [portable validator](../evidence/Roth.mul_card_filter_weight_le_aux/validate.py), [current manifest](../evidence/Roth.mul_card_filter_weight_le_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
