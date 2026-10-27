# Roth.kronSpan — private-prefilter assessment (105/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.kronSpan/prefilter-rule.md), [rule provenance](../evidence/Roth.kronSpan/prefilter-provenance.json).

## Definition and mathematical role

Private noncomputable definition at `Roth/GenWronskian.lean:149–151`. The polynomial-module span of substituted Hasse operators with total order at most the natural bound. The exact original kernel type is:

```lean
{K : Type u_1} →
  [inst : Field K] →
    {σ : Type u_2} → [Fintype σ] → ℕ → ℕ → Submodule (Polynomial K) (MvPolynomial σ K → Polynomial K)
```

A field, finite variable enumeration, and natural base and order bound. No characteristic-zero, positivity or derivative-size premise is captured. The original type has no matrix-size parameter. The complete original private definition and axioms are printed via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.kronSpan/native-type.json), [exact declaration](../evidence/Roth.kronSpan/target-excerpt.lean.txt), [metadata](../evidence/Roth.kronSpan/target-metadata.json), [whole declaring module](../evidence/Roth.kronSpan/source-module.lean.txt).

## Structural, API and duplication review

Existing Submodule.span takes the image of the private substituted Hasse operators whose total order is at most the bound. It organizes the derivative-stability induction and finite span witness. The span and its individual operator generators have distinct roles; no duplicate definition or new instance is introduced. Explicit project dependencies are `Roth.kronHasse`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It defines a value in an existing function/module type and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.derivative_mem_kronSpan` | `Roth/GenWronskian.lean:162` | Uses the private span in the derivative expansion; full original body replayed. |
| `Roth.hasseDeriv_kronecker_mem` | `Roth/GenWronskian.lean:190` | Uses the private span in the derivative expansion; full original body replayed. |

2 explicit source caller declarations, all in GenWronskian.lean; 2 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.kronSpan/callers.json), [raw source search](../evidence/Roth.kronSpan/source-search.json), and [direct value consumers](../evidence/Roth.kronSpan/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.kronSpan/canonical-snapshot.json), [entry](../evidence/Roth.kronSpan/canonical-entry.json).

## Native definition and full dependent proof verification

The whole declaring module was replayed in namespace `PrivateKronSpanAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace; original proof bodies are retained. This includes every explicit caller and the later nonvanishing proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `PrivateKronSpanAssessment.replay`; their checks include the private dependency chains. The original actual private definition, body and axioms were independently resolved and printed. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.kronSpan/executed.lean.txt), [complete raw receipt](../evidence/Roth.kronSpan/native-receipt.json), [verification ledger](../evidence/Roth.kronSpan/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.kronSpan/inputs.json), [baseline manifest](../evidence/Roth.kronSpan/input-manifest.json), [build record](../evidence/Roth.kronSpan/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.kronSpan/assessment.json), [overview entry](../evidence/Roth.kronSpan/overview-entry.json), [portable validator](../evidence/Roth.kronSpan/validate.py), [current manifest](../evidence/Roth.kronSpan/copy-manifest.json). Root acceptance is recorded separately after independent review.
