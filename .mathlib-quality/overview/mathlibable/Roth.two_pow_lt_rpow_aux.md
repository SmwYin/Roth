# Roth.two_pow_lt_rpow_aux — private-prefilter assessment (216/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.two_pow_lt_rpow_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.two_pow_lt_rpow_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:621–644`. A logarithmic lower bound on a nonnegative real q makes its positive real power strictly exceed the explicit power-of-two combinatorial envelope. The exact original kernel type is:

```lean
∀ {p r₁ l : ℕ},
  0 < p →
    ∀ {δ q : ℝ},
      0 < δ →
        0 ≤ q →
          ↑p * (2 * ↑p + 1) / δ ≤ Real.log q → 0 < l * r₁ → 2 ^ ((2 * p + 1) * r₁ * l) < q ^ (δ / ↑p * (↑l * ↑r₁))
```

Positive dimension, delta and degree-size product; nonnegative base and the stated logarithmic lower bound. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.two_pow_lt_rpow_aux/native-type.json), [exact declaration](../evidence/Roth.two_pow_lt_rpow_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.two_pow_lt_rpow_aux/target-metadata.json), [whole declaring module](../evidence/Roth.two_pow_lt_rpow_aux/source-module.lean.txt).

## Structural, API and duplication review

Positivity of p and δ makes the logarithmic threshold positive, so Real.log_pos_iff yields q>1. Use Real.log_lt_sub_one_of_pos to obtain log 2<1 and rearrange the threshold into 2p+1≤log(q)δ/p. Multiply strictly by the positive natural product l*r₁, rewrite both powers via Real.rpow_def_of_pos and compare exponents using Real.exp_lt_exp. This supplies the strict exponential stage of lem6M_lt after the separate natural factorial envelope bound. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.lem6M_lt` | `Roth/Theta.lean:649` | Strictly bounds the power-of-two envelope by a q-power before multiplying back the positive height factor B^l; full original caller body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.two_pow_lt_rpow_aux/callers.json), [raw source search](../evidence/Roth.two_pow_lt_rpow_aux/source-search.json), and [direct value consumers](../evidence/Roth.two_pow_lt_rpow_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.two_pow_lt_rpow_aux/canonical-snapshot.json), [entry](../evidence/Roth.two_pow_lt_rpow_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate216`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate216.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.two_pow_lt_rpow_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.two_pow_lt_rpow_aux/native-receipt.json), [verification ledger](../evidence/Roth.two_pow_lt_rpow_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.two_pow_lt_rpow_aux/inputs.json), [baseline manifest](../evidence/Roth.two_pow_lt_rpow_aux/input-manifest.json), [build record](../evidence/Roth.two_pow_lt_rpow_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.two_pow_lt_rpow_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.two_pow_lt_rpow_aux/assessment.json), [overview entry](../evidence/Roth.two_pow_lt_rpow_aux/overview-entry.json), [portable validator](../evidence/Roth.two_pow_lt_rpow_aux/validate.py), [current manifest](../evidence/Roth.two_pow_lt_rpow_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
