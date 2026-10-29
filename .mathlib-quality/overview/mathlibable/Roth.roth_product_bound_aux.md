# Roth.roth_product_bound_aux — private-prefilter assessment (285/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.roth_product_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.roth_product_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Main.lean:481–502`. Bounds the natural-floor coefficient scale from above and away from zero, and bounds the product of degree factors strictly by its delta power. The exact original kernel type is:

```lean
∀ {m : ℕ} [inst : NeZero m] {α A δ : ℝ},
  0 ≤ δ →
    0 ≤ A →
      ∀ {q r : Fin m → ℕ},
        0 < r 0 →
          (∀ (j : Fin m), r j ≤ r 0) →
            2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑(q 0) →
              0 < ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ∧
                ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ≤ ↑(q 0) ^ (δ * ↑(r 0)) ∧
                  ∏ j : Fin m, (↑(r j) + 1) < ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ^ δ
```

Nonzero dimension, nonnegative delta/coefficient bound, positive maximal first degree and combined logarithmic bound. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.roth_product_bound_aux/native-type.json), [exact declaration](../evidence/Roth.roth_product_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.roth_product_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.roth_product_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Extract the square-log threshold at least3 from m>=1 and nonnegative logarithm contributions. Apply four_lt_rpow and sqrt_lt_floor to get positivity of B and B<=q0^(delta*r0). Bound each degree factor by 2^r0 via Nat.lt_two_pow_self and rj<=r0, then use Finset.prod_le_pow_card and the first three_small_factors bound. Explicit project dependencies are `Roth.four_lt_rpow`, `Roth.mainCoeffBound`, `Roth.sqrt_lt_floor`, `Roth.three_small_factors`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.roth_of_isIntegral` | `Roth/Main.lean:547` | Supplies positivity, the coefficient-scale upper bound and the degree-product estimate needed when taking logarithms. Full original body replayed. |

1 explicit source caller declarations, all in Main.lean; 1 direct original value consumers. Exact separate lists retained. Entire Main module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.roth_product_bound_aux/callers.json), [raw source search](../evidence/Roth.roth_product_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.roth_product_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.roth_product_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.roth_product_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainPrivate285`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainPrivate285.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.roth_product_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.roth_product_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.roth_product_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.roth_product_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.roth_product_bound_aux/input-manifest.json), [build record](../evidence/Roth.roth_product_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.roth_product_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.roth_product_bound_aux/assessment.json), [overview entry](../evidence/Roth.roth_product_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.roth_product_bound_aux/validate.py), [current manifest](../evidence/Roth.roth_product_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
