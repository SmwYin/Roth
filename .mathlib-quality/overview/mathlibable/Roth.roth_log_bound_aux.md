# Roth.roth_log_bound_aux — private-prefilter assessment (286/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.roth_log_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.roth_log_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Main.lean:505–541`. From the strict scalar evaluation product bound and balanced denominator logarithms, deduces G*kappa<m*(1+4delta). The exact original kernel type is:

```lean
∀ {m : ℕ} [inst : NeZero m],
  2 ≤ m →
    ∀ {δ G κ B : ℝ},
      δ ≤ 1 →
        ∀ {q r : Fin m → ℕ},
          (∀ (j : Fin m), 1 < q j) →
            (∀ (j : Fin m), ↑(r j) * Real.log ↑(q j) < (1 + δ / 10) * (↑(r 0) * Real.log ↑(q 0))) →
              0 < B →
                B ≤ ↑(q 0) ^ (δ * ↑(r 0)) →
                  ∏ j : Fin m, (↑(r j) + 1) < B ^ δ →
                    1 <
                        (∏ j : Fin m, ↑(q j) ^ r j) *
                          ((∏ j : Fin m, (↑(r j) + 1)) * B ^ (1 + 3 * δ) * ↑(q 0) ^ (-↑(r 0) * G * κ)) →
                      G * κ < ↑m * (1 + 4 * δ)
```

Dimension at least two, delta at most one, denominators above one, positive coefficient scale, balanced logarithmic bounds and explicit product expression above one. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.roth_log_bound_aux/native-type.json), [exact declaration](../evidence/Roth.roth_log_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.roth_log_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.roth_log_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Use the strict balance inequality at index0 to infer r0>0 and delta>=0. Expand the logarithm of the positive product with Real.log_mul, Real.log_rpow and Real.log_prod. Sum the strict balanced logarithmic bounds over the nonempty finite variable set, replace log of the degree product and log B using the supplied estimates, then divide by positive r0*log(q0). The final linear bound uses delta<=1 and m>=2. G is arbitrary real; its later specialization is gamma-minus-eta. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.roth_of_isIntegral` | `Roth/Main.lean:547` | Contradicts the independently chosen ratio m*(1+4delta)/(gamma-eta)<kappa after using eta_lt_gam_iff for denominator positivity. Full original body replayed. |

1 explicit source caller declarations, all in Main.lean; 1 direct original value consumers. Exact separate lists retained. Entire Main module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.roth_log_bound_aux/callers.json), [raw source search](../evidence/Roth.roth_log_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.roth_log_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.roth_log_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.roth_log_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainPrivate286`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainPrivate286.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.roth_log_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.roth_log_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.roth_log_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.roth_log_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.roth_log_bound_aux/input-manifest.json), [build record](../evidence/Roth.roth_log_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.roth_log_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.roth_log_bound_aux/assessment.json), [overview entry](../evidence/Roth.roth_log_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.roth_log_bound_aux/validate.py), [current manifest](../evidence/Roth.roth_log_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
