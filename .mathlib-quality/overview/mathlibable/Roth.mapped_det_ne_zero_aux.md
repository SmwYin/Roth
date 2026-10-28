# Roth.mapped_det_ne_zero_aux — private-prefilter assessment (211/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.mapped_det_ne_zero_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.mapped_det_ne_zero_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:511–529`. A Hasse-derivative determinant over the reals is nonzero when its integer precursor factors into nonzero complementary-variable and distinguished-variable integer factors. The exact original kernel type is:

```lean
∀ {τ : Type u_2} {R : MvPolynomial (Option τ) ℤ} {l : ℕ}
  {D : Fin l → τ →₀ ℕ} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ},
  U ≠ 0 →
    V ≠ 0 →
      (Matrix.of fun μ ν ↦ (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) R).det =
          (rename some) U * (Polynomial.aeval (X none)) V →
        (Matrix.of fun μ ν ↦
              (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) ((map (Int.castRingHom ℝ)) R)).det ≠
          0
```

Nonzero separated integer factors and a factorization identity. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.mapped_det_ne_zero_aux/native-type.json), [exact declaration](../evidence/Roth.mapped_det_ne_zero_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.mapped_det_ne_zero_aux/target-metadata.json), [whole declaring module](../evidence/Roth.mapped_det_ne_zero_aux/source-module.lean.txt).

## Structural, API and duplication review

Commute the integer-to-real coefficient map through the determinant using RingHom.map_det and through every Hasse derivative using hasseDeriv_map. Injectivity of the coefficient map reduces nonvanishing to the integer determinant. Substitute the separated factorization, split the nonzero product, and use injective complementary renaming and the aeval_X_eq_rename identification with uniqueAlgEquiv to transport nonvanishing of both factors. This supplies the nonzero determinant premise of sum_max_sub_le_index_det inside index_le_lem6, independently of the row-weight and scalar arithmetic helpers. Explicit project dependencies are `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `Roth.aeval_X_eq_rename`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.index_le_lem6` | `Roth/Theta.lean:556` | Supplies the mapped determinant nonzero premise to sum_max_sub_le_index_det from the separated nonzero integer factors; full original caller body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.mapped_det_ne_zero_aux/callers.json), [raw source search](../evidence/Roth.mapped_det_ne_zero_aux/source-search.json), and [direct value consumers](../evidence/Roth.mapped_det_ne_zero_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.mapped_det_ne_zero_aux/canonical-snapshot.json), [entry](../evidence/Roth.mapped_det_ne_zero_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate211`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate211.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.mapped_det_ne_zero_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.mapped_det_ne_zero_aux/native-receipt.json), [verification ledger](../evidence/Roth.mapped_det_ne_zero_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.mapped_det_ne_zero_aux/inputs.json), [baseline manifest](../evidence/Roth.mapped_det_ne_zero_aux/input-manifest.json), [build record](../evidence/Roth.mapped_det_ne_zero_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.mapped_det_ne_zero_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.mapped_det_ne_zero_aux/assessment.json), [overview entry](../evidence/Roth.mapped_det_ne_zero_aux/overview-entry.json), [portable validator](../evidence/Roth.mapped_det_ne_zero_aux/validate.py), [current manifest](../evidence/Roth.mapped_det_ne_zero_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
