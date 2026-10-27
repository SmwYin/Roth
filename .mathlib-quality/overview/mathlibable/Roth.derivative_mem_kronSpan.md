# Roth.derivative_mem_kronSpan — private-prefilter assessment (114/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.derivative_mem_kronSpan/prefilter-rule.md), [rule provenance](../evidence/Roth.derivative_mem_kronSpan/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/GenWronskian.lean:162–188`. Ordinary differentiation sends every operator in the order-mu substituted Hasse span into the order-(mu+1) span. The exact original kernel type is:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] (k μ : ℕ) {F : MvPolynomial σ K → Polynomial K},
  F ∈ Roth.kronSpan✝ k μ → (fun P ↦ Polynomial.derivative (F P)) ∈ Roth.kronSpan✝ k (μ + 1)
```

A field and finite variable enumeration; the operator lies in kronSpan k μ. No characteristic-zero, positivity or derivative-size premise is captured. The original type has no matrix-size parameter. The complete original private theorem and axioms are printed via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.derivative_mem_kronSpan/native-type.json), [exact declaration](../evidence/Roth.derivative_mem_kronSpan/target-excerpt.lean.txt), [metadata](../evidence/Roth.derivative_mem_kronSpan/target-metadata.json), [whole declaring module](../evidence/Roth.derivative_mem_kronSpan/source-module.lean.txt).

## Structural, API and duplication review

Submodule.span_induction is the existing organizing API. The generator case uses the preceding private derivative recurrence and the bound on total Hasse order; the scalar case uses the polynomial Leibniz rule and inclusion of the old bounded span in the next one. This lifts a generator identity to closure of the whole polynomial-coefficient span. It is distinct from both the generator recurrence and the subsequent Hasse-iteration result. No new definition, class or instance is needed. Explicit project dependencies are `Roth.derivative_kronHasse_aux`, `Roth.kronSpan`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves membership in an existing submodule and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.hasseDeriv_kronecker_mem` | `Roth/GenWronskian.lean:190` | Uses this private lemma in the next stage of the Hasse-span expansion; full original body replayed. |

1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.derivative_mem_kronSpan/callers.json), [raw source search](../evidence/Roth.derivative_mem_kronSpan/source-search.json), and [direct value consumers](../evidence/Roth.derivative_mem_kronSpan/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.derivative_mem_kronSpan/canonical-snapshot.json), [entry](../evidence/Roth.derivative_mem_kronSpan/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `PrivateDerivativeSpanAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later nonvanishing proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `PrivateDerivativeSpanAssessment.replay`; their checks include the private dependency chains. The original actual private theorem, body and axioms were independently resolved and printed. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.derivative_mem_kronSpan/executed.lean.txt), [complete raw receipt](../evidence/Roth.derivative_mem_kronSpan/native-receipt.json), [verification ledger](../evidence/Roth.derivative_mem_kronSpan/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.derivative_mem_kronSpan/inputs.json), [baseline manifest](../evidence/Roth.derivative_mem_kronSpan/input-manifest.json), [build record](../evidence/Roth.derivative_mem_kronSpan/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.derivative_mem_kronSpan/assessment.json), [overview entry](../evidence/Roth.derivative_mem_kronSpan/overview-entry.json), [portable validator](../evidence/Roth.derivative_mem_kronSpan/validate.py), [current manifest](../evidence/Roth.derivative_mem_kronSpan/copy-manifest.json). Root acceptance is recorded separately after independent review.
