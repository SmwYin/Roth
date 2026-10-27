# Roth.filter_weight_le_eq_empty — private-prefilter assessment (128/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.filter_weight_le_eq_empty/prefilter-rule.md), [rule provenance](../evidence/Roth.filter_weight_le_eq_empty/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Lattice.lean:143–145`. The weighted filtered box is empty when lambda is greater than the dimension. The exact original kernel type is:

```lean
∀ {m : ℕ} (r : Fin m → ℕ) {lam : ℝ},
  ↑m < lam → {d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2} = ∅
```

Natural rectangular bounds and λ greater than the dimension; no positivity of coordinate bounds. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.filter_weight_le_eq_empty/native-type.json), [exact declaration](../evidence/Roth.filter_weight_le_eq_empty/target-excerpt.lean.txt), [metadata](../evidence/Roth.filter_weight_le_eq_empty/target-metadata.json), [whole declaring module](../evidence/Roth.filter_weight_le_eq_empty/source-module.lean.txt).

## Structural, API and duplication review

The threshold (m-lambda)/2 is strictly negative when lambda exceeds the dimension. Every natural exponent vector has nonnegative weight, even if some coordinate bounds vanish. Finset.filter_eq_empty_iff and weight_nonneg reduce each hypothetical member to an arithmetic contradiction. This handles the empty tail regime in the main lattice estimate; it is distinct from its small-lambda cardinality bound and inductive step. Explicit project dependencies are `Roth.weight_nonneg`, `Roth.box`, `Roth.weight`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.card_filter_weight_le` | `Roth/Lattice.lean:202` | Uses this helper in the lattice proof; full original body replayed. |

1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.filter_weight_le_eq_empty/callers.json), [raw source search](../evidence/Roth.filter_weight_le_eq_empty/source-search.json), and [direct value consumers](../evidence/Roth.filter_weight_le_eq_empty/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.filter_weight_le_eq_empty/canonical-snapshot.json), [entry](../evidence/Roth.filter_weight_le_eq_empty/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `LatticeEmptyAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later lattice-count proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `LatticeEmptyAssessment.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.filter_weight_le_eq_empty/executed.lean.txt), [complete raw receipt](../evidence/Roth.filter_weight_le_eq_empty/native-receipt.json), [verification ledger](../evidence/Roth.filter_weight_le_eq_empty/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.filter_weight_le_eq_empty/inputs.json), [baseline manifest](../evidence/Roth.filter_weight_le_eq_empty/input-manifest.json), [build record](../evidence/Roth.filter_weight_le_eq_empty/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.filter_weight_le_eq_empty/assessment.json), [overview entry](../evidence/Roth.filter_weight_le_eq_empty/overview-entry.json), [portable validator](../evidence/Roth.filter_weight_le_eq_empty/validate.py), [current manifest](../evidence/Roth.filter_weight_le_eq_empty/copy-manifest.json). Root acceptance is recorded separately after independent review.
