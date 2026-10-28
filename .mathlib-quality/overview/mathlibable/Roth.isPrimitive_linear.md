# Roth.isPrimitive_linear — private-prefilter assessment (194/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.isPrimitive_linear/prefilter-rule.md), [rule provenance](../evidence/Roth.isPrimitive_linear/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:167–173`. If an integer numerator h and natural denominator q are coprime, the polynomial qX-h is primitive over the integers. The exact original kernel type is:

```lean
∀ {h : ℤ} {q : ℕ},
  IsCoprime h ↑q → (Polynomial.C ↑q * Polynomial.X - Polynomial.C h).IsPrimitive
```

Coprime integer numerator and natural denominator. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.isPrimitive_linear/native-type.json), [exact declaration](../evidence/Roth.isPrimitive_linear/target-excerpt.lean.txt), [metadata](../evidence/Roth.isPrimitive_linear/target-metadata.json), [whole declaring module](../evidence/Roth.isPrimitive_linear/source-module.lean.txt).

## Structural, API and duplication review

A scalar dividing every polynomial coefficient divides both the constant coefficient -h and the linear coefficient q. Coprimality forces this scalar to be a unit. This primitive linear-factor fact feeds Gauss descent in exists_eq_pow_mul_of_rootMultiplicity; it is distinct from closure of primitive polynomials under powers. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_eq_pow_mul_of_rootMultiplicity` | `Roth/Theta.lean:184` | Uses this helper in the polynomial-index transport and bounding proofs; full original body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.isPrimitive_linear/callers.json), [raw source search](../evidence/Roth.isPrimitive_linear/source-search.json), and [direct value consumers](../evidence/Roth.isPrimitive_linear/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.isPrimitive_linear/canonical-snapshot.json), [entry](../evidence/Roth.isPrimitive_linear/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate194`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate194.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.isPrimitive_linear/executed.lean.txt), [complete raw receipt](../evidence/Roth.isPrimitive_linear/native-receipt.json), [verification ledger](../evidence/Roth.isPrimitive_linear/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.isPrimitive_linear/inputs.json), [baseline manifest](../evidence/Roth.isPrimitive_linear/input-manifest.json), [build record](../evidence/Roth.isPrimitive_linear/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.isPrimitive_linear/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.isPrimitive_linear/assessment.json), [overview entry](../evidence/Roth.isPrimitive_linear/overview-entry.json), [portable validator](../evidence/Roth.isPrimitive_linear/validate.py), [current manifest](../evidence/Roth.isPrimitive_linear/copy-manifest.json). Root acceptance is recorded separately after independent review.
