# Roth.exists_auxiliary_polynomial_of_log_bound_aux — private-prefilter assessment (263/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:643–669`. Produces an auxiliary polynomial with high diagonal-root index, a real-power coefficient bound, and uniform evaluated double-Hasse-derivative height bounds. The exact original kernel type is:

```lean
∀ {f : Polynomial ℤ} {α A : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
        ∀ {m q₁ r₁ : ℕ},
          0 < m →
            ∀ (r : Fin m → ℕ),
              (∀ (j : Fin m), 0 < r j) →
                ∑ j : Fin m, r j ≤ m * r₁ →
                  ∀ {δ : ℝ},
                    0 ≤ δ →
                      2 * ↑m + 1 + 2 * ↑m * Real.log (1 + A) + 2 * ↑m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log ↑q₁ →
                        ∃ P ∈ Roth.RSet (↑q₁ ^ (δ * ↑r₁)) r,
                          Roth.gam δ f.natDegree m ≤ Roth.index ((map (Int.castRingHom ℝ)) P) (fun (x : Fin m) ↦ α) r ∧
                            ∀ (i k : Fin m →₀ ℕ),
                              |(eval fun (x : Fin m) ↦ α)
                                    ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| <
                                ↑(Roth.mainCoeffBound δ q₁ r₁) ^ (1 + 3 * δ)
```

Monic integer equation, bounded coefficients, positive degree vector, total degree bound and combined logarithmic condition. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/native-type.json), [exact declaration](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Obtain P and its index from the log-budget helper after dropping the nonnegative alpha logarithm term. Use three_small_factors for powers of2 and 1+abs(alpha), deduce positivity of B from a nonzero coefficient of P, and identify B*(B^delta)^3 with B^(1+3delta). Use Nat.floor_le to enlarge RSet and abs_eval_iterated_hasseDeriv_lt_aux for the uniform evaluation estimate, then linear_combination closes the power identity. The sole index-gap caller additionally bounds Theta by eta; it is not part of this helper. Explicit project dependencies are `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.abs_eval_iterated_hasseDeriv_lt_aux`, `Roth.exists_mem_RSet_le_index_of_log_bound_aux`, `Roth.gam`, `Roth.index`, `Roth.mainCoeffBound`, `Roth.three_small_factors`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_auxiliary_polynomial_with_index_gap_aux` | `Roth/MainLemma.lean:692` | Supplies W, its high diagonal-root index, coefficient control and uniform double-derivative bounds before combining with Theta<eta. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/callers.json), [raw source search](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate263`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate263.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/input-manifest.json), [build record](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/assessment.json), [overview entry](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/validate.py), [current manifest](../evidence/Roth.exists_auxiliary_polynomial_of_log_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
