# Roth.theta_lt_eta_of_sq_log_bound_aux — private-prefilter assessment (264/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:671–690`. Converts the square-logarithm and adjacent-degree hypotheses into the strict bound Theta<eta for the chosen real coefficient power. The exact original kernel type is:

```lean
∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
  0 ≤ δ →
    δ * ↑m ≤ 1 →
      ∀ {r q : Fin m → ℕ},
        3 ≤ r (Fin.rev 0) →
          (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) →
            2 * ↑m + 1 ≤ δ ^ 2 * Real.log ↑(q 0) →
              (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                Roth.Θ (↑(q 0) ^ (δ * ↑(r 0))) q r < Roth.eta δ m
```

Nonzero dimension, nonnegative delta with delta times dimension at most one, last degree at least three and ratio/balancing/logarithmic hypotheses. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/native-type.json), [exact declaration](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Write the nonzero dimension m as n+1. The positive square-log bound and delta>=0 imply delta>0; multiply through delta squared to derive the weaker logarithmic hypothesis needed by Theta_lt from delta*m<=1. Translate the last degree and adjacent ratio premises with Nat.cast_le and div_le_iff, invoke Theta_lt, and unfold eta. The sole index-gap caller first drops the nonnegative A/alpha logarithm terms. This is the numerical Theta-to-selected-eta specialization, distinct from constructing the auxiliary polynomial. Explicit project dependencies are `Roth.eta`, `Roth.Θ`, `Roth.Θ_lt`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | `Roth/MainLemma.lean:692` | Converts the ratio and square-log premises into Theta<eta, making the combined gamma-eta+Theta index inequality strict. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/callers.json), [raw source search](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate264`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate264.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/input-manifest.json), [build record](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/assessment.json), [overview entry](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/validate.py), [current manifest](../evidence/Roth.theta_lt_eta_of_sq_log_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
