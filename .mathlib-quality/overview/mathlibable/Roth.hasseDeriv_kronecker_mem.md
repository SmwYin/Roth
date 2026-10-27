# Roth.hasseDeriv_kronecker_mem — private-prefilter assessment (115/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.hasseDeriv_kronecker_mem/prefilter-rule.md), [rule provenance](../evidence/Roth.hasseDeriv_kronecker_mem/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/GenWronskian.lean:190–205`. Every univariate Hasse derivative of the Kronecker substitution operator lies in the corresponding bounded substituted-Hasse span. The exact original kernel type is:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] [CharZero K] (k μ : ℕ),
  (fun P ↦ (Polynomial.hasseDeriv μ) ((Roth.kronecker k) P)) ∈ Roth.kronSpan✝ k μ
```

Characteristic zero field and a finite variable enumeration. Characteristic zero is captured and used to invert the nonzero successor scalar in the induction. No positivity or derivative-size premise is captured. The original type has no matrix-size parameter. The complete original private theorem and axioms are printed via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.hasseDeriv_kronecker_mem/native-type.json), [exact declaration](../evidence/Roth.hasseDeriv_kronecker_mem/target-excerpt.lean.txt), [metadata](../evidence/Roth.hasseDeriv_kronecker_mem/target-metadata.json), [whole declaring module](../evidence/Roth.hasseDeriv_kronecker_mem/source-module.lean.txt).

## Structural, API and duplication review

Induction on the univariate Hasse order uses the order-zero span generator and the preceding derivative-span closure. Polynomial.hasseDeriv_comp relates the next Hasse derivative to differentiation, and characteristic zero makes the natural successor scalar invertible in the field. This is a live bridge from ordinary derivative closure to Hasse derivative span membership, not a duplicate of either preceding lemma. Existing span and scalar-restriction APIs supply the interface; no new class or instance is installed. Explicit project dependencies are `Roth.derivative_mem_kronSpan`, `Roth.kronSpan`, `Roth.kronHasse`, `Roth.kronecker`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_hasseDeriv_kronecker_eq_sum` | `Roth/GenWronskian.lean:214` | Uses this private lemma in the next stage of the Hasse-span expansion; full original body replayed. |

1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.hasseDeriv_kronecker_mem/callers.json), [raw source search](../evidence/Roth.hasseDeriv_kronecker_mem/source-search.json), and [direct value consumers](../evidence/Roth.hasseDeriv_kronecker_mem/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.hasseDeriv_kronecker_mem/canonical-snapshot.json), [entry](../evidence/Roth.hasseDeriv_kronecker_mem/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `PrivateHasseSpanAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later nonvanishing proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `PrivateHasseSpanAssessment.replay`; their checks include the private dependency chains. The original actual private theorem, body and axioms were independently resolved and printed. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.hasseDeriv_kronecker_mem/executed.lean.txt), [complete raw receipt](../evidence/Roth.hasseDeriv_kronecker_mem/native-receipt.json), [verification ledger](../evidence/Roth.hasseDeriv_kronecker_mem/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.hasseDeriv_kronecker_mem/inputs.json), [baseline manifest](../evidence/Roth.hasseDeriv_kronecker_mem/input-manifest.json), [build record](../evidence/Roth.hasseDeriv_kronecker_mem/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.hasseDeriv_kronecker_mem/assessment.json), [overview entry](../evidence/Roth.hasseDeriv_kronecker_mem/overview-entry.json), [portable validator](../evidence/Roth.hasseDeriv_kronecker_mem/validate.py), [current manifest](../evidence/Roth.hasseDeriv_kronecker_mem/copy-manifest.json). Root acceptance is recorded separately after independent review.
