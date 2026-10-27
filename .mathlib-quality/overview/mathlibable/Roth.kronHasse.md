# Roth.kronHasse — private-prefilter assessment (104/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.kronHasse/prefilter-rule.md), [rule provenance](../evidence/Roth.kronHasse/prefilter-provenance.json).

## Definition and mathematical role

Private noncomputable definition at `Roth/GenWronskian.lean:145–146`. Composes a multivariate Hasse derivative with Kronecker substitution, as a polynomial-valued function. The exact original kernel type is:

```lean
{K : Type u_1} →
  [inst : Field K] → {σ : Type u_2} → [Fintype σ] → ℕ → (σ →₀ ℕ) → MvPolynomial σ K → Polynomial K
```

A field, a finite variable enumeration, a base, and a derivative multi-index. No characteristic-zero, positivity or derivative-size premise is captured. The original type has no matrix-size parameter. The complete original private definition and axioms are printed via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.kronHasse/native-type.json), [exact declaration](../evidence/Roth.kronHasse/target-excerpt.lean.txt), [metadata](../evidence/Roth.kronHasse/target-metadata.json), [whole declaring module](../evidence/Roth.kronHasse/source-module.lean.txt).

## Structural, API and duplication review

A pointwise composition: take one project multivariate Hasse derivative, then project Kronecker substitution. It provides generators for the polynomial-module span. Existing function composition is sufficient for the interface; this prefilter does not assign a separate public contribution verdict. The named private operator and the span have distinct roles. Explicit project dependencies are `MvPolynomial.hasseDeriv`, `Roth.kronecker`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It defines a value in an existing function/module type and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.kronSpan` | `Roth/GenWronskian.lean:149` | Uses the private operator in the derivative expansion; full original body replayed. |
| `Roth.derivative_kronHasse_aux` | `Roth/GenWronskian.lean:153` | Uses the private operator in the derivative expansion; full original body replayed. |
| `Roth.hasseDeriv_kronecker_mem` | `Roth/GenWronskian.lean:190` | Uses the private operator in the derivative expansion; full original body replayed. |
| `Roth.exists_hasseDeriv_kronecker_eq_sum` | `Roth/GenWronskian.lean:214` | Uses the private operator in the derivative expansion; full original body replayed. |

4 explicit source caller declarations, all in GenWronskian.lean; 5 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.kronHasse/callers.json), [raw source search](../evidence/Roth.kronHasse/source-search.json), and [direct value consumers](../evidence/Roth.kronHasse/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.kronHasse/canonical-snapshot.json), [entry](../evidence/Roth.kronHasse/canonical-entry.json).

## Native definition and full dependent proof verification

The whole declaring module was replayed in namespace `PrivateKronHasseAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace; original proof bodies are retained. This includes every explicit caller and the later nonvanishing proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `PrivateKronHasseAssessment.replay`; their checks include the private dependency chains. The original actual private definition, body and axioms were independently resolved and printed. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.kronHasse/executed.lean.txt), [complete raw receipt](../evidence/Roth.kronHasse/native-receipt.json), [verification ledger](../evidence/Roth.kronHasse/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.kronHasse/inputs.json), [baseline manifest](../evidence/Roth.kronHasse/input-manifest.json), [build record](../evidence/Roth.kronHasse/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.kronHasse/assessment.json), [overview entry](../evidence/Roth.kronHasse/overview-entry.json), [portable validator](../evidence/Roth.kronHasse/validate.py), [current manifest](../evidence/Roth.kronHasse/copy-manifest.json). Root acceptance is recorded separately after independent review.
