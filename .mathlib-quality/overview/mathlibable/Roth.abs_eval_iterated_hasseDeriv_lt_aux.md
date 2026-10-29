# Roth.abs_eval_iterated_hasseDeriv_lt_aux — private-prefilter assessment (255/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:459–475`. Bounds every evaluated iterated Hasse derivative of an integer polynomial by beta cubed times the original coefficient bound, from coordinate degrees and a common exponential bound. The exact original kernel type is:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {P : MvPolynomial σ ℤ} {r : σ → ℕ} {B α β : ℝ}
  {s : ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) →
    0 < B →
      ∑ j : σ, r j ≤ s →
        2 ^ s < β →
          (1 + |α|) ^ s ≤ β →
            (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
              ∀ (i k : σ →₀ ℕ),
                |(eval fun (x : σ) ↦ α) ((map (Int.castRingHom ℝ)) ((hasseDeriv i) ((hasseDeriv k) P)))| <
                  β * (β * B) * β
```

Finite variables, bounded degrees/coefficient size, positive coefficient bound and bounds for powers of two and one plus the point absolute value. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/native-type.json), [exact declaration](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/target-metadata.json), [whole declaring module](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/source-module.lean.txt).

## Structural, API and duplication review

Apply degreeOf_hasseDeriv_le twice, abs_coeff_hasseDeriv_le twice and abs_eval_le. Rewrite the product of identical evaluation factors with Finset.prod_pow_eq_pow_sum, replace the degree sum by s, and combine the two strict powers-of-two estimates with positive B and the non-strict evaluation-factor bound. The sole caller exists_auxiliary_polynomial_of_log_bound_aux chooses beta=B^delta, derives B>0 from a nonzero integer coefficient, and rewrites B*beta^3 as B^(1+3delta). This is an analytic height estimate, not the subsequent Hasse-derivative selection lemma. Explicit project dependencies are `MvPolynomial.degreeOf_hasseDeriv_le`, `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_hasseDeriv_le`, `Roth.abs_eval_le`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_auxiliary_polynomial_of_log_bound_aux` | `Roth/MainLemma.lean:643` | Controls evaluated double Hasse derivatives using beta=B^delta and the three-small-factors bounds, then rewrites the cubic product as B^(1+3delta). Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/callers.json), [raw source search](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/source-search.json), and [direct value consumers](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/canonical-snapshot.json), [entry](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate255`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate255.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/native-receipt.json), [verification ledger](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/inputs.json), [baseline manifest](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/input-manifest.json), [build record](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/assessment.json), [overview entry](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/overview-entry.json), [portable validator](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/validate.py), [current manifest](../evidence/Roth.abs_eval_iterated_hasseDeriv_lt_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
