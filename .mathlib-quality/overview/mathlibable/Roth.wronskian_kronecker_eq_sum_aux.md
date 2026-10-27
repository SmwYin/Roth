# Roth.wronskian_kronecker_eq_sum_aux — private-prefilter assessment (118/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.wronskian_kronecker_eq_sum_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.wronskian_kronecker_eq_sum_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/GenWronskian.lean:238–245`. Expands the Wronskian after Kronecker substitution as a finite polynomial-coefficient sum of substituted generalized Wronskians, given the derivative-row expansions. The exact original kernel type is:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] {l : ℕ} (k : ℕ) (φ : Fin l → MvPolynomial σ K) (s : Fin l → Finset (σ →₀ ℕ))
  (c : Fin l → (σ →₀ ℕ) → Polynomial K),
  (∀ (μ ν : Fin l),
      (Polynomial.hasseDeriv ↑μ) ((Roth.kronecker k) (φ ν)) =
        ∑ d ∈ s μ, c μ d * (Roth.kronecker k) ((hasseDeriv d) (φ ν))) →
    (Roth.wronskian fun ν ↦ (Roth.kronecker k) (φ ν)) =
      ∑ f ∈ Fintype.piFinset s, (∏ μ, c μ (f μ)) * (Roth.kronecker k) (Roth.genWronskian f φ)
```

A field, finite variable enumeration, and supplied finite expansion formulas for each univariate derivative row. No characteristic-zero, positivity or derivative-size premise is captured. The natural matrix-size parameter l is captured, but has no positivity premise. The complete original private theorem and axioms are printed via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.wronskian_kronecker_eq_sum_aux/native-type.json), [exact declaration](../evidence/Roth.wronskian_kronecker_eq_sum_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.wronskian_kronecker_eq_sum_aux/target-metadata.json), [whole declaring module](../evidence/Roth.wronskian_kronecker_eq_sum_aux/source-module.lean.txt).

## Structural, API and duplication review

The supplied uniform derivative-row expansions substitute into the Wronskian matrix. The existing project det_sum_rows helper expands its determinant by row multilinearity, while AlgHom.map_det transports each chosen generalized Wronskian through Kronecker substitution. This is a live application bridge, distinct from the standalone determinant identity and the final nonvanishing theorem. It adds no structure or instance; its private status is appropriate to the project-specific transport. Explicit project dependencies are `MvPolynomial.hasseDeriv`, `Roth.det_sum_rows`, `Roth.genWronskian`, `Roth.kronecker`, `Roth.wronskian`, `Roth.wronskianMatrix`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_genWronskian_ne_zero` | `Roth/GenWronskian.lean:254` | Uses the determinant expansion in the contradiction proving a nonzero generalized Wronskian; full original body replayed. |

1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.wronskian_kronecker_eq_sum_aux/callers.json), [raw source search](../evidence/Roth.wronskian_kronecker_eq_sum_aux/source-search.json), and [direct value consumers](../evidence/Roth.wronskian_kronecker_eq_sum_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.wronskian_kronecker_eq_sum_aux/canonical-snapshot.json), [entry](../evidence/Roth.wronskian_kronecker_eq_sum_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `PrivateWronskianSumAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later nonvanishing proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `PrivateWronskianSumAssessment.replay`; their checks include the private dependency chains. The original actual private theorem, body and axioms were independently resolved and printed. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.wronskian_kronecker_eq_sum_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.wronskian_kronecker_eq_sum_aux/native-receipt.json), [verification ledger](../evidence/Roth.wronskian_kronecker_eq_sum_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.wronskian_kronecker_eq_sum_aux/inputs.json), [baseline manifest](../evidence/Roth.wronskian_kronecker_eq_sum_aux/input-manifest.json), [build record](../evidence/Roth.wronskian_kronecker_eq_sum_aux/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.wronskian_kronecker_eq_sum_aux/assessment.json), [overview entry](../evidence/Roth.wronskian_kronecker_eq_sum_aux/overview-entry.json), [portable validator](../evidence/Roth.wronskian_kronecker_eq_sum_aux/validate.py), [current manifest](../evidence/Roth.wronskian_kronecker_eq_sum_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
