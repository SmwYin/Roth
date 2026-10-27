# Roth.derivative_kronHasse_aux — private-prefilter assessment (113/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.derivative_kronHasse_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.derivative_kronHasse_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/GenWronskian.lean:153–160`. Differentiating a substituted Hasse operator is a polynomial-coefficient sum of next-order substituted Hasse operators. The exact original kernel type is:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2}
  [inst_1 : Fintype σ] (k : ℕ) (d : σ →₀ ℕ),
  (fun P ↦ Polynomial.derivative (Roth.kronHasse✝ k d P)) =
    ∑ j,
      (Polynomial.derivative (Polynomial.X ^ k ^ ↑((Fintype.equivFin σ) j)) * Polynomial.C ↑(d j + 1)) •
        Roth.kronHasse✝ k (d + Finsupp.single j 1)
```

A field, finite variable enumeration, and arbitrary base and derivative exponent. No characteristic-zero, positivity or derivative-size premise is captured. The original type has no matrix-size parameter and does not require characteristic zero. The complete original private theorem and axioms are printed via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.derivative_kronHasse_aux/native-type.json), [exact declaration](../evidence/Roth.derivative_kronHasse_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.derivative_kronHasse_aux/target-metadata.json), [whole declaring module](../evidence/Roth.derivative_kronHasse_aux/source-module.lean.txt).

## Structural, API and duplication review

This function-valued derivative identity follows pointwise from the project chain rule and the partial/Hasse commutation identity. It supplies the next-order generators in the bounded-span induction. Existing function extensionality and pointwise sums/scalars express the interface; there is no new definition, instance or coercion. It is a live internal recurrence, not a duplicate of the scalar chain rule. The public contribution verdicts of its ingredients remain separate. Explicit project dependencies are `Roth.derivative_aeval`, `MvPolynomial.pderiv_hasseDeriv`, `Roth.kronHasse`, `Roth.kronecker`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves an equality in an existing function/module type and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.derivative_mem_kronSpan` | `Roth/GenWronskian.lean:162` | Uses the derivative recurrence to prove closure of the bounded span under differentiation; full original body replayed. |

1 explicit source caller declarations, all in GenWronskian.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.derivative_kronHasse_aux/callers.json), [raw source search](../evidence/Roth.derivative_kronHasse_aux/source-search.json), and [direct value consumers](../evidence/Roth.derivative_kronHasse_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.derivative_kronHasse_aux/canonical-snapshot.json), [entry](../evidence/Roth.derivative_kronHasse_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `PrivateDerivativeAuxAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later nonvanishing proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `PrivateDerivativeAuxAssessment.replay`; their checks include the private dependency chains. The original actual private theorem, body and axioms were independently resolved and printed. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.derivative_kronHasse_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.derivative_kronHasse_aux/native-receipt.json), [verification ledger](../evidence/Roth.derivative_kronHasse_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.derivative_kronHasse_aux/inputs.json), [baseline manifest](../evidence/Roth.derivative_kronHasse_aux/input-manifest.json), [build record](../evidence/Roth.derivative_kronHasse_aux/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.derivative_kronHasse_aux/assessment.json), [overview entry](../evidence/Roth.derivative_kronHasse_aux/overview-entry.json), [portable validator](../evidence/Roth.derivative_kronHasse_aux/validate.py), [current manifest](../evidence/Roth.derivative_kronHasse_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
