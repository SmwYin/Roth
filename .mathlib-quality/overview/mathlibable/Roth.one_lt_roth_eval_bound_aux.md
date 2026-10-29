# Roth.one_lt_roth_eval_bound_aux — private-prefilter assessment (284/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.one_lt_roth_eval_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.one_lt_roth_eval_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Main.lean:453–478`. Combines the nonzero integer-value lower bound with the Taylor upper bound for the auxiliary polynomial, giving a strict scalar product bound greater than1. The exact original kernel type is:

```lean
∀ {α κ : ℝ} {f : Polynomial ℤ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      ∀ {A : ℝ},
        (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
          ∀ {m : ℕ} [inst : NeZero m] {δ : ℝ},
            0 ≤ δ →
              δ ≤ 1 / ↑m →
                ∀ {r : Fin m → ℕ},
                  (∀ (j : Fin m), 0 < r j) →
                    3 ≤ r (Fin.rev 0) →
                      (∀ (i j : Fin m), ↑i + 1 = ↑j → ↑(r j) / δ ≤ ↑(r i)) →
                        ∀ {q : Fin m → ℕ},
                          (∀ (j : Fin m), 0 < q j) →
                            0 ≤ κ →
                              ∀ {h : Fin m → ℤ},
                                (∀ (j : Fin m), |α - ↑(h j) / ↑(q j)| ≤ 1 / ↑(q j) ^ κ) →
                                  (∀ (j : Fin m), IsCoprime (h j) ↑(q j)) →
                                    2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤
                                        δ ^ 2 * Real.log ↑(q 0) →
                                      (∀ (j : Fin m), ↑(r 0) * Real.log ↑(q 0) ≤ ↑(r j) * Real.log ↑(q j)) →
                                        1 <
                                          (∏ j : Fin m, ↑(q j) ^ r j) *
                                            ((∏ j : Fin m, (↑(r j) + 1)) *
                                                ↑(Roth.mainCoeffBound δ (q 0) (r 0)) ^ (1 + 3 * δ) *
                                              ↑(q 0) ^ (-↑(r 0) * (Roth.gam δ f.natDegree m - Roth.eta δ m) * κ))
```

Monic integer equation, coefficient bounds, positive degrees/denominators, small delta, coprime approximants, nonnegative exponent and numerical parameter bounds. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.one_lt_roth_eval_bound_aux/native-type.json), [exact declaration](../evidence/Roth.one_lt_roth_eval_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.one_lt_roth_eval_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.one_lt_roth_eval_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Invoke main_lemma to get Q, coordinate degree bounds, strict index bound, rational-point nonvanishing and derivative bounds. Transfer coordinate degrees across the injective integer coefficient map via support_map_of_injective. Derive the real-power denominator comparison from the balanced-log hypothesis using Real.rpow_le_iff_le_log and positive degrees. Multiply abs_eval_lt_of_le_index by the positive denominator product and combine one_le_prod_pow_mul_abs_eval. Explicit project dependencies are `Roth.abs_eval_lt_of_le_index`, `Roth.eta`, `Roth.gam`, `Roth.mainCoeffBound`, `Roth.main_lemma`, `Roth.one_le_prod_pow_mul_abs_eval`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.roth_of_isIntegral` | `Roth/Main.lean:547` | Provides the strict greater-than1 premise of roth_log_bound_aux; the main lemma supplies its gamma-minus-eta decay exponent. Full original body replayed. |

1 explicit source caller declarations, all in Main.lean; 1 direct original value consumers. Exact separate lists retained. Entire Main module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.one_lt_roth_eval_bound_aux/callers.json), [raw source search](../evidence/Roth.one_lt_roth_eval_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.one_lt_roth_eval_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.one_lt_roth_eval_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.one_lt_roth_eval_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainPrivate284`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainPrivate284.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.one_lt_roth_eval_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.one_lt_roth_eval_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.one_lt_roth_eval_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.one_lt_roth_eval_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.one_lt_roth_eval_bound_aux/input-manifest.json), [build record](../evidence/Roth.one_lt_roth_eval_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.one_lt_roth_eval_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.one_lt_roth_eval_bound_aux/assessment.json), [overview entry](../evidence/Roth.one_lt_roth_eval_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.one_lt_roth_eval_bound_aux/validate.py), [current manifest](../evidence/Roth.one_lt_roth_eval_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
