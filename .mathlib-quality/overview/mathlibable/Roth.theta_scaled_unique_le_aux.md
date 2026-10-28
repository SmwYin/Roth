# Roth.theta_scaled_unique_le_aux — private-prefilter assessment (220/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.theta_scaled_unique_le_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.theta_scaled_unique_le_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:742–765`. A one-variable extremal index at height M is at most δ after scaling its weight by l, when M lies below the first denominator power and weighted denominator logarithms are balanced. The exact original kernel type is:

```lean
∀ {δ M : ℝ} {q₁ q₂ r₁ r₂ l : ℕ},
  1 < q₁ →
    0 < r₁ →
      0 < l →
        ↑r₁ * Real.log ↑q₁ ≤ ↑r₂ * Real.log ↑q₂ →
          1 ≤ M → M ≤ ↑q₁ ^ (δ * (↑l * ↑r₁)) → (Roth.Θ M (fun x ↦ q₂) fun x ↦ l * r₂) ≤ δ
```

First denominator greater than one, positive first degree and scale, balanced degree-log products and coefficient bounds between one and the target power. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.theta_scaled_unique_le_aux/native-type.json), [exact declaration](../evidence/Roth.theta_scaled_unique_le_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.theta_scaled_unique_le_aux/target-metadata.json), [whole declaring module](../evidence/Roth.theta_scaled_unique_le_aux/source-module.lean.txt).

## Structural, API and duplication review

First derive δ≥0 from M≥1, M≤q₁^(δlr₁), q₁>1 and positive lr₁. The balanced logarithms force q₂>1 and r₂>0. Apply Θ_mono to enlarge M, then Θ_unique_le. Rewrite Real.log_rpow, clear the positive scaled-weight logarithm, and use the balanced-log inequality. This is the singleton-factor contribution to theta_phi_lt_aux, distinct from the complementary-prefix induction. Explicit project dependencies are `Roth.Θ`, `Roth.Θ_mono`, `Roth.Θ_unique_le`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.theta_phi_lt_aux` | `Roth/Theta.lean:840` | Bounds the singleton extremal-index summand of Φ by ε from the M envelope and balanced denominator logarithms; full original caller body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.theta_scaled_unique_le_aux/callers.json), [raw source search](../evidence/Roth.theta_scaled_unique_le_aux/source-search.json), and [direct value consumers](../evidence/Roth.theta_scaled_unique_le_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.theta_scaled_unique_le_aux/canonical-snapshot.json), [entry](../evidence/Roth.theta_scaled_unique_le_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate220`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate220.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.theta_scaled_unique_le_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.theta_scaled_unique_le_aux/native-receipt.json), [verification ledger](../evidence/Roth.theta_scaled_unique_le_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.theta_scaled_unique_le_aux/inputs.json), [baseline manifest](../evidence/Roth.theta_scaled_unique_le_aux/input-manifest.json), [build record](../evidence/Roth.theta_scaled_unique_le_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.theta_scaled_unique_le_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.theta_scaled_unique_le_aux/assessment.json), [overview entry](../evidence/Roth.theta_scaled_unique_le_aux/overview-entry.json), [portable validator](../evidence/Roth.theta_scaled_unique_le_aux/validate.py), [current manifest](../evidence/Roth.theta_scaled_unique_le_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
