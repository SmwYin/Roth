# Roth.mul_sq_div_three_le_sum_max_aux — private-prefilter assessment (205/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:347–355`. For nonnegative real height θ and a natural truncation length l at least θr, the positive-part residual sum is at least rθ²/3, including nonpositive scales and the boundary θr=l. The exact original kernel type is:

```lean
∀ {θ r : ℝ},
  0 ≤ θ → ∀ {l : ℕ}, θ * r ≤ ↑l → r * θ ^ 2 / 3 ≤ ∑ ν ∈ Finset.range l, max 0 (θ - ↑ν / r)
```

Nonnegative height; height times scale no larger than truncation length. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/native-type.json), [exact declaration](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/target-metadata.json), [whole declaring module](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/source-module.lean.txt).

## Structural, API and duplication review

If r≤0 the desired lower bound is nonpositive while every summand is nonnegative. For r>0 split θr≤l into strict inequality, handled by mul_sq_div_three_le_sum_max_of_pos_aux, and equality. At equality, use mul_div_two_le_sum_max_aux for lθ/2 and the identity l=θr to compare rθ²/3 with rθ²/2. This closes sign and boundary cases missing from the positive strict-length helper and supplies the quadratic branch of min_le_sum_max. Explicit project dependencies are `Roth.mul_div_two_le_sum_max_aux`, `Roth.mul_sq_div_three_le_sum_max_of_pos_aux`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.min_le_sum_max` | `Roth/Theta.lean:362` | In the nonnegative-height long-truncation branch, apply this real-scale bound at the natural scale rp and compose with the minimum’s second-component bound; full original proof replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/callers.json), [raw source search](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/source-search.json), and [direct value consumers](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/canonical-snapshot.json), [entry](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate205`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate205.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/native-receipt.json), [verification ledger](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/inputs.json), [baseline manifest](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/input-manifest.json), [build record](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/assessment.json), [overview entry](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/overview-entry.json), [portable validator](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/validate.py), [current manifest](../evidence/Roth.mul_sq_div_three_le_sum_max_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
