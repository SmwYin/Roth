# Roth.inv_add_inv_le — private-prefilter assessment (121/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.inv_add_inv_le/prefilter-rule.md), [rule provenance](../evidence/Roth.inv_add_inv_le/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Lattice.lean:40–45`. Bounds the sum of two complementary reciprocal terms by twice the endpoint harmonic factor. The exact original kernel type is:

```lean
∀ {lam x : ℝ},
  2 < lam → 0 ≤ x → x ≤ 2 → (lam - 1 + x)⁻¹ + (lam - 1 + (2 - x))⁻¹ ≤ 2 * lam / (lam ^ 2 - 1)
```

Real λ greater than two and x in the closed interval [0,2]. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.inv_add_inv_le/native-type.json), [exact declaration](../evidence/Roth.inv_add_inv_le/target-excerpt.lean.txt), [metadata](../evidence/Roth.inv_add_inv_le/target-metadata.json), [whole declaring module](../evidence/Roth.inv_add_inv_le/source-module.lean.txt).

## Structural, API and duplication review

The two reciprocal denominators are positive under the real interval bounds. Existing inv_add_inv and div_le_div_iff reduce the estimate to the nonnegative product x*(2-x). This paired endpoint bound feeds the reflected finite-sum argument, and is distinct from the square-root threshold and the full reciprocal-sum estimate. No new structure or instance is needed. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.sum_inv_le` | `Roth/Lattice.lean:47` | Uses this estimate in the next reciprocal-sum bound; full original body replayed. |

1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.inv_add_inv_le/callers.json), [raw source search](../evidence/Roth.inv_add_inv_le/source-search.json), and [direct value consumers](../evidence/Roth.inv_add_inv_le/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.inv_add_inv_le/canonical-snapshot.json), [entry](../evidence/Roth.inv_add_inv_le/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `LatticeInvAddInvAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later lattice-count proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `LatticeInvAddInvAssessment.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.inv_add_inv_le/executed.lean.txt), [complete raw receipt](../evidence/Roth.inv_add_inv_le/native-receipt.json), [verification ledger](../evidence/Roth.inv_add_inv_le/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.inv_add_inv_le/inputs.json), [baseline manifest](../evidence/Roth.inv_add_inv_le/input-manifest.json), [build record](../evidence/Roth.inv_add_inv_le/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.inv_add_inv_le/assessment.json), [overview entry](../evidence/Roth.inv_add_inv_le/overview-entry.json), [portable validator](../evidence/Roth.inv_add_inv_le/validate.py), [current manifest](../evidence/Roth.inv_add_inv_le/copy-manifest.json). Root acceptance is recorded separately after independent review.
