# Roth.sum_inv_le — private-prefilter assessment (122/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.sum_inv_le/prefilter-rule.md), [rule provenance](../evidence/Roth.sum_inv_le/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Lattice.lean:47–61`. Bounds the reciprocal arithmetic-grid sum by (r+1)*lambda/(lambda^2-1), using complementary-term pairing. The exact original kernel type is:

```lean
∀ {r : ℕ},
  1 ≤ r →
    ∀ {lam : ℝ}, 2 < lam → ∑ j ∈ Finset.range (r + 1), (lam - 1 + 2 * ↑j / ↑r)⁻¹ ≤ (↑r + 1) * (lam / (lam ^ 2 - 1))
```

Positive natural r and real λ greater than two. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.sum_inv_le/native-type.json), [exact declaration](../evidence/Roth.sum_inv_le/target-excerpt.lean.txt), [metadata](../evidence/Roth.sum_inv_le/target-metadata.json), [whole declaring module](../evidence/Roth.sum_inv_le/source-module.lean.txt).

## Structural, API and duplication review

The preceding private complementary-pair bound is summed over the finite grid. Finset.sum_range_reflect identifies the reflected grid sum with the original one, and ordinary finite-sum distribution and arithmetic divide the resulting estimate by two. This upgrades the pointwise pair estimate to the whole reciprocal grid sum, without duplicating the public strict square-root bound. Explicit project dependencies are `Roth.inv_add_inv_le`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.sum_inv_lt` | `Roth/Lattice.lean:68` | Uses this estimate in the next reciprocal-sum bound; full original body replayed. |

1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.sum_inv_le/callers.json), [raw source search](../evidence/Roth.sum_inv_le/source-search.json), and [direct value consumers](../evidence/Roth.sum_inv_le/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.sum_inv_le/canonical-snapshot.json), [entry](../evidence/Roth.sum_inv_le/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `LatticeSumInvAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later lattice-count proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `LatticeSumInvAssessment.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.sum_inv_le/executed.lean.txt), [complete raw receipt](../evidence/Roth.sum_inv_le/native-receipt.json), [verification ledger](../evidence/Roth.sum_inv_le/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.sum_inv_le/inputs.json), [baseline manifest](../evidence/Roth.sum_inv_le/input-manifest.json), [build record](../evidence/Roth.sum_inv_le/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.sum_inv_le/assessment.json), [overview entry](../evidence/Roth.sum_inv_le/overview-entry.json), [portable validator](../evidence/Roth.sum_inv_le/validate.py), [current manifest](../evidence/Roth.sum_inv_le/copy-manifest.json). Root acceptance is recorded separately after independent review.
