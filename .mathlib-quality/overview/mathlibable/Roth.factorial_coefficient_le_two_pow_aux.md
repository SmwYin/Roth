# Roth.factorial_coefficient_le_two_pow_aux — private-prefilter assessment (215/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.factorial_coefficient_le_two_pow_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.factorial_coefficient_le_two_pow_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:609–619`. The non-height factors of the Lemma 6 determinant envelope are bounded by one explicit power of two when l is at most 2 to the degree ceiling. The exact original kernel type is:

```lean
∀ (p r₁ l : ℕ),
  l ≤ 2 ^ r₁ → (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤ 2 ^ ((2 * p + 1) * r₁ * l)
```

Determinant size at most two to the maximum degree. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.factorial_coefficient_le_two_pow_aux/native-type.json), [exact declaration](../evidence/Roth.factorial_coefficient_le_two_pow_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.factorial_coefficient_le_two_pow_aux/target-metadata.json), [whole declaring module](../evidence/Roth.factorial_coefficient_le_two_pow_aux/source-module.lean.txt).

## Structural, API and duplication review

Use Nat.lt_two_pow_self to bound r₁+1 by 2^r₁. Bound l factorial by l^l using Nat.factorial_le_pow, then use l≤2^r₁ and Nat.pow_le_pow_left. Multiply the nonnegative natural bounds and combine the powers with pow_mul and pow_add; polynomial exponent arithmetic gives the final exponent (2p+1)r₁l. This is the combinatorial-envelope stage of lem6M_lt, separate from the strict logarithmic comparison with q. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.lem6M_lt` | `Roth/Theta.lean:649` | Bounds the factors other than B^l by one power of two before the strict q-power comparison; full original caller body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.factorial_coefficient_le_two_pow_aux/callers.json), [raw source search](../evidence/Roth.factorial_coefficient_le_two_pow_aux/source-search.json), and [direct value consumers](../evidence/Roth.factorial_coefficient_le_two_pow_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.factorial_coefficient_le_two_pow_aux/canonical-snapshot.json), [entry](../evidence/Roth.factorial_coefficient_le_two_pow_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate215`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate215.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.factorial_coefficient_le_two_pow_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.factorial_coefficient_le_two_pow_aux/native-receipt.json), [verification ledger](../evidence/Roth.factorial_coefficient_le_two_pow_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.factorial_coefficient_le_two_pow_aux/inputs.json), [baseline manifest](../evidence/Roth.factorial_coefficient_le_two_pow_aux/input-manifest.json), [build record](../evidence/Roth.factorial_coefficient_le_two_pow_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.factorial_coefficient_le_two_pow_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.factorial_coefficient_le_two_pow_aux/assessment.json), [overview entry](../evidence/Roth.factorial_coefficient_le_two_pow_aux/overview-entry.json), [portable validator](../evidence/Roth.factorial_coefficient_le_two_pow_aux/validate.py), [current manifest](../evidence/Roth.factorial_coefficient_le_two_pow_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
