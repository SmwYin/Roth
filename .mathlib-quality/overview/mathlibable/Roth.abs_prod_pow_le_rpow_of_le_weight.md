# Roth.abs_prod_pow_le_rpow_of_le_weight — private-prefilter assessment (280/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/prefilter-rule.md), [rule provenance](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Main.lean:347–371`. Converts coordinatewise rational-approximation errors and denominator growth into decay of a monomial controlled by its weighted degree. The exact original kernel type is:

```lean
∀ {m : ℕ} [inst : NeZero m] {r q : Fin m → ℕ},
  (∀ (j : Fin m), 0 < q j) →
    ∀ {κ : ℝ},
      0 ≤ κ →
        ∀ {x : Fin m → ℝ},
          (∀ (j : Fin m), |x j| ≤ 1 / ↑(q j) ^ κ) →
            (∀ (j : Fin m), ↑(q 0) ^ (↑(r 0) / ↑(r j)) ≤ ↑(q j)) →
              ∀ (d : Fin m →₀ ℕ) {c : ℝ}, c ≤ Roth.weight r d → |∏ j : Fin m, x j ^ d j| ≤ ↑(q 0) ^ (-↑(r 0) * c * κ)
```

Nonzero dimension, positive denominators, nonnegative approximation exponent and coordinate error/denominator-growth bounds. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/native-type.json), [exact declaration](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/target-excerpt.lean.txt), [metadata](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/target-metadata.json), [whole declaring module](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/source-module.lean.txt).

## Structural, API and duplication review

Use Finset.abs_prod and abs_pow for pointwise absolute-value estimates. Rewrite reciprocal powers as negative real powers; Real.rpow_le_rpow_of_nonpos and the denominator growth comparison replace all bases by powers of q0. Collapse the product with Real.rpow_sum_of_pos and the weight formula. Finally use q0>=1 and the nonpositive exponent multiplier to replace weight by its lower bound c. Zero coordinate degrees are allowed because real division is total; no positive r premise is silently added. Explicit project dependencies are `Roth.weight`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.abs_eval_lt_of_le_index` | `Roth/Main.lean:380` | Bounds each nonvanishing Taylor monomial after index_le_weight supplies its weight lower bound; vanishing terms are handled separately. Full original body replayed. |

1 explicit source caller declarations, all in Main.lean; 1 direct original value consumers. Exact separate lists retained. Entire Main module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/callers.json), [raw source search](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/source-search.json), and [direct value consumers](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/canonical-snapshot.json), [entry](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainPrivate280`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainPrivate280.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/executed.lean.txt), [complete raw receipt](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/native-receipt.json), [verification ledger](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/inputs.json), [baseline manifest](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/input-manifest.json), [build record](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/assessment.json), [overview entry](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/overview-entry.json), [portable validator](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/validate.py), [current manifest](../evidence/Roth.abs_prod_pow_le_rpow_of_le_weight/copy-manifest.json). Root acceptance is recorded separately after independent review.
