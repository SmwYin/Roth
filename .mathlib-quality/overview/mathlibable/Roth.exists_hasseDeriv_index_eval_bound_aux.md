# Roth.exists_hasseDeriv_index_eval_bound_aux — private-prefilter assessment (256/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:477–495`. Selects one nonzero integer Hasse derivative that is nonvanishing at a second point, loses less than a specified cutoff in its index at the first point, and retains all derivative evaluation bounds. The exact original kernel type is:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {α z : σ → ℝ}
  {C γ c : ℝ},
  P ≠ 0 →
    (∀ (j : σ), degreeOf j P ≤ r j) →
      (∀ (i k : σ →₀ ℕ), |(eval α) ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| < C) →
        γ ≤ Roth.index ((map (Int.castRingHom ℝ)) P) α r →
          Roth.index ((map (Int.castRingHom ℝ)) P) z r < c →
            ∃ (Q : MvPolynomial σ ℤ),
              Q ≠ 0 ∧
                (∀ (j : σ), degreeOf j Q ≤ r j) ∧
                  γ - c < Roth.index ((map (Int.castRingHom ℝ)) Q) α r ∧
                    (eval z) ((map (Int.castRingHom ℝ)) Q) ≠ 0 ∧
                      ∀ (i : σ →₀ ℕ), |(eval α) ((hasseDeriv i) ((map (Int.castRingHom ℝ)) Q))| < C
```

Nonzero integral polynomial with degree bounds, high first index, low second index and uniform iterated derivative bound. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/native-type.json), [exact declaration](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Use exists_hasseDeriv_eval_ne_zero after injectively mapping integer coefficients into the reals. Set Q=hasseDeriv k P; nonvanishing of its evaluation ensures Q is nonzero, degreeOf_hasseDeriv_le preserves coordinate degrees, and index_sub_weight_le_index_hasseDeriv controls index loss. Commute coefficient maps with Hasse derivatives to transfer the supplied double-derivative height bound. The sole main_lemma caller chooses a midpoint cutoff c between the second-point index upper bound Theta and the available first-point gap. This is a selection/transport result, distinct from the numerical estimate supplying the height bound. Explicit project dependencies are `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.exists_hasseDeriv_eval_ne_zero`, `Roth.index`, `Roth.index_sub_weight_le_index_hasseDeriv`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.main_lemma` | `Roth/MainLemma.lean:735` | Selects the final derivative using the midpoint cutoff between the available first-point index gap and the rational-point Theta bound. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/callers.json), [raw source search](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate256`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate256.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/input-manifest.json), [build record](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/assessment.json), [overview entry](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/validate.py), [current manifest](../evidence/Roth.exists_hasseDeriv_index_eval_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
