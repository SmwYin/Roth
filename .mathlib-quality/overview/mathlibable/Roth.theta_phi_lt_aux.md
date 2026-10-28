# Roth.theta_phi_lt_aux — private-prefilter assessment (225/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.theta_phi_lt_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.theta_phi_lt_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:840–889`. For every allowed determinant rank, the sum of singleton and prefix extremal indices, plus its square root and sqrt δ, is strictly below half the next-dimensional target. The exact original kernel type is:

```lean
∀ {n : ℕ} {δ : ℝ},
  0 < δ →
    δ ≤ 1 / (↑n + 1 + 1) →
      δ < 1 →
        ∀ {r q : Fin (n + 2) → ℕ},
          Antitone r →
            3 ≤ ↑(r (Fin.last (n + 1))) →
              (∀ (i : Fin (n + 1)), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
                (↑n + 1 + 1) * (2 * (↑n + 1 + 1) + 1) / δ ≤ Real.log ↑(q 0) →
                  (∀ (j : Fin (n + 2)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                    (∀ {δ : ℝ},
                        0 < δ →
                          δ ≤ 1 / (↑n + 1) →
                            ∀ {r q : Fin (n + 1) → ℕ},
                              3 ≤ ↑(r (Fin.last n)) →
                                (∀ (i : Fin n), ↑(r i.succ) ≤ δ * ↑(r i.castSucc)) →
                                  (↑n + 1) * (2 * (↑n + 1) + 1) / δ ≤ Real.log ↑(q 0) →
                                    (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                                      Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < 10 ^ (n + 1) * δ ^ (1 / 2) ^ (n + 1)) →
                      ∀ {l : ℕ},
                        l ∈ Finset.Icc 1 (r (Fin.last (n + 1)) + 1) →
                          have M := Roth.lem6M (n + 2) (r 0) (↑(q 0) ^ (δ * ↑(r 0))) l;
                          have Φ :=
                            (Roth.Θ M (fun (x : Unit) ↦ q (Fin.last (n + 1))) fun (x : Unit) ↦
                                l * r (Fin.last (n + 1))) +
                              Roth.Θ M (fun (j : Fin (n + 1)) ↦ q j.castSucc) fun (j : Fin (n + 1)) ↦ l * r j.castSucc;
                          Φ + √Φ + √δ < 10 ^ (n + 2) * δ ^ (1 / 2) ^ (n + 2) / 2
```

Small positive delta, antitone degree sequence, minimum last degree, ratios, denominator logarithm growth and the previous-dimensional induction hypothesis. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.theta_phi_lt_aux/native-type.json), [exact declaration](../evidence/Roth.theta_phi_lt_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.theta_phi_lt_aux/target-metadata.json), [whole declaring module](../evidence/Roth.theta_phi_lt_aux/source-module.lean.txt).

## Structural, API and duplication review

Derive all weights positive from antitonicity and the last-weight bound, and denominator positivity from theta_denominators_one_lt_aux. Set ε=δ(1+1/(n+2)); use one_le_lem6M and lem6M_lt for the height envelope, theta_scaled_unique_le_aux for the singleton term, and theta_prefix_lt_aux with theta_delta_succ_lt_aux for the induction term. Combine them through lem7_Φ_bound and lem7_numeric to reach the strict half-target. This is the per-rank quantitative stage used after Θ_option_le. Explicit project dependencies are `Roth.lem6M`, `Roth.lem6M_lt`, `Roth.lem7_numeric`, `Roth.lem7_Φ_bound`, `Roth.one_le_lem6M`, `Roth.theta_delta_succ_lt_aux`, `Roth.theta_denominators_one_lt_aux`, `Roth.theta_prefix_lt_aux`, `Roth.theta_scaled_unique_le_aux`, `Roth.Θ`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.theta_lt_succ_aux` | `Roth/Theta.lean:891` | Bounds every allowed rank after the caller applies Θ_option_le and Finset.sup'_lt_iff; full original successor proof replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.theta_phi_lt_aux/callers.json), [raw source search](../evidence/Roth.theta_phi_lt_aux/source-search.json), and [direct value consumers](../evidence/Roth.theta_phi_lt_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.theta_phi_lt_aux/canonical-snapshot.json), [entry](../evidence/Roth.theta_phi_lt_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate225`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate225.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.theta_phi_lt_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.theta_phi_lt_aux/native-receipt.json), [verification ledger](../evidence/Roth.theta_phi_lt_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.theta_phi_lt_aux/inputs.json), [baseline manifest](../evidence/Roth.theta_phi_lt_aux/input-manifest.json), [build record](../evidence/Roth.theta_phi_lt_aux/baseline-build.txt).

The complete native type is captured directly from kernel `ci.type` in a clean display-only command, preserving both internal M/Φ let-bindings and explicit function domains. This avoids treating an internal `:=` as the separator before the theorem proof. The original proof/audit receipt remains unchanged. [Full type capture](../evidence/Roth.theta_phi_lt_aux/full-type-receipt.json), [exact capture source](../evidence/Roth.theta_phi_lt_aux/full-type-executed.lean.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.theta_phi_lt_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.theta_phi_lt_aux/assessment.json), [overview entry](../evidence/Roth.theta_phi_lt_aux/overview-entry.json), [portable validator](../evidence/Roth.theta_phi_lt_aux/validate.py), [current manifest](../evidence/Roth.theta_phi_lt_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
