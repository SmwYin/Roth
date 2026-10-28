# Roth.index_unique_le_log_div — private-prefilter assessment (198/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.index_unique_le_log_div/prefilter-rule.md), [rule provenance](../evidence/Roth.index_unique_le_log_div/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:223–250`. For a nonzero one-variable integer polynomial and a reduced rational evaluation point with denominator greater than one, its weighted index is at most log B divided by the weighted logarithm of that denominator, provided its absolute leading coefficient is bounded by B. The exact original kernel type is:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] [inst_1 : Unique σ] {B : ℝ}
  {q r : σ → ℕ},
  1 < q default →
    ∀ {R : MvPolynomial σ ℤ},
      R ≠ 0 →
        |↑((uniqueAlgEquiv ℤ σ) R).leadingCoeff| ≤ B →
          ∀ {h : σ → ℤ},
            IsCoprime (h default) ↑(q default) →
              Roth.index ((map (Int.castRingHom ℝ)) R) (fun j ↦ ↑(h j) / ↑(q j)) r ≤
                Real.log B / (↑(r default) * Real.log ↑(q default))
```

Singleton finite variable type; denominator greater than one; nonzero polynomial with bounded leading coefficient and coprime numerator. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.index_unique_le_log_div/native-type.json), [exact declaration](../evidence/Roth.index_unique_le_log_div/target-excerpt.lean.txt), [metadata](../evidence/Roth.index_unique_le_log_div/target-metadata.json), [whole declaring module](../evidence/Roth.index_unique_le_log_div/source-module.lean.txt).

## Structural, API and duplication review

Identify the one-variable polynomial after injective integer-to-real mapping, transport root multiplicity from rational to real coefficients, and rewrite the unique-variable index as multiplicity divided by its natural weight. Apply pow_rootMultiplicity_le, take logarithms using positivity of the denominator power, then normalize log_pow and divide by positive log q and nonnegative weight. This is the live private logarithmic bridge between the denominator-power coefficient bound and the public one-variable Theta bound; it is distinct from both the algebraic factor theorem and the supremum wrapper. Explicit project dependencies are `Roth.index`, `Roth.index_unique`, `Roth.pow_rootMultiplicity_le`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.Θ_unique_le` | `Roth/Theta.lean:256` | Uses this helper in the polynomial-index transport and bounding proofs; full original body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.index_unique_le_log_div/callers.json), [raw source search](../evidence/Roth.index_unique_le_log_div/source-search.json), and [direct value consumers](../evidence/Roth.index_unique_le_log_div/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.index_unique_le_log_div/canonical-snapshot.json), [entry](../evidence/Roth.index_unique_le_log_div/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate198`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate198.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.index_unique_le_log_div/executed.lean.txt), [complete raw receipt](../evidence/Roth.index_unique_le_log_div/native-receipt.json), [verification ledger](../evidence/Roth.index_unique_le_log_div/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.index_unique_le_log_div/inputs.json), [baseline manifest](../evidence/Roth.index_unique_le_log_div/input-manifest.json), [build record](../evidence/Roth.index_unique_le_log_div/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.index_unique_le_log_div/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.index_unique_le_log_div/assessment.json), [overview entry](../evidence/Roth.index_unique_le_log_div/overview-entry.json), [portable validator](../evidence/Roth.index_unique_le_log_div/validate.py), [current manifest](../evidence/Roth.index_unique_le_log_div/copy-manifest.json). Root acceptance is recorded separately after independent review.
