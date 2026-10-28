# Roth.theta_denominators_one_lt_aux — private-prefilter assessment (224/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.theta_denominators_one_lt_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.theta_denominators_one_lt_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:833–838`. If the first natural weight and first denominator logarithm are positive, balancing their product below every other weighted logarithm forces every natural denominator to exceed one. The exact original kernel type is:

```lean
∀ {n : ℕ} {r q : Fin (n + 1) → ℕ},
  0 < r 0 →
    0 < Real.log ↑(q 0) →
      (∀ (j : Fin (n + 1)), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) → ∀ (j : Fin (n + 1)), 1 < q j
```

Positive first degree and first denominator logarithm; balanced degree-log products. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.theta_denominators_one_lt_aux/native-type.json), [exact declaration](../evidence/Roth.theta_denominators_one_lt_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.theta_denominators_one_lt_aux/target-metadata.json), [whole declaring module](../evidence/Roth.theta_denominators_one_lt_aux/source-module.lean.txt).

## Structural, API and duplication review

The first weighted logarithm is positive. Its lower bound on r_j log(q_j), together with nonnegative natural r_j, forces log(q_j)>0 via pos_of_mul_pos_right. Apply Real.log_pos_iff for the nonnegative natural base and cast back to 1<q_j. This supplies denominator positivity in the singleton, successor and final index estimates. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.theta_phi_lt_aux` | `Roth/Theta.lean:840` | At j=0 supplies q0>1 for the coefficient-height lower bound and singleton-index estimate; whole actual caller replayed. |
| `Roth.theta_lt_succ_aux` | `Roth/Theta.lean:891` | Supplies every qj>1, hence positivity for Θ_option_le and the first-denominator height bound; whole actual caller replayed. |
| `Roth.Θ_lt` | `Roth/Theta.lean:962` | At n=0 supplies q0>1 to theta_lt_base_aux from the positive log threshold; whole actual caller replayed. |

3 explicit source caller declarations, all in Theta.lean; 3 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.theta_denominators_one_lt_aux/callers.json), [raw source search](../evidence/Roth.theta_denominators_one_lt_aux/source-search.json), and [direct value consumers](../evidence/Roth.theta_denominators_one_lt_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.theta_denominators_one_lt_aux/canonical-snapshot.json), [entry](../evidence/Roth.theta_denominators_one_lt_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate224`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate224.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.theta_denominators_one_lt_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.theta_denominators_one_lt_aux/native-receipt.json), [verification ledger](../evidence/Roth.theta_denominators_one_lt_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.theta_denominators_one_lt_aux/inputs.json), [baseline manifest](../evidence/Roth.theta_denominators_one_lt_aux/input-manifest.json), [build record](../evidence/Roth.theta_denominators_one_lt_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.theta_denominators_one_lt_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.theta_denominators_one_lt_aux/assessment.json), [overview entry](../evidence/Roth.theta_denominators_one_lt_aux/overview-entry.json), [portable validator](../evidence/Roth.theta_denominators_one_lt_aux/validate.py), [current manifest](../evidence/Roth.theta_denominators_one_lt_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
