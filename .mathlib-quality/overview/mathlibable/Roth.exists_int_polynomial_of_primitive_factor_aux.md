# Roth.exists_int_polynomial_of_primitive_factor_aux — private-prefilter assessment (175/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Separation.lean:466–478`. When an integer multivariate polynomial is a separated product of an integer factor with coefficient gcd one and a rational univariate factor, the univariate factor has integer coefficients. The exact original kernel type is:

```lean
∀ {τ : Type u_1} {U : MvPolynomial τ ℤ} {V' : Polynomial ℚ} {F : MvPolynomial (Option τ) ℤ},
  U.support.gcd ⇑U.coeff = 1 →
    (map (Int.castRingHom ℚ)) F = (rename some) ((map (Int.castRingHom ℚ)) U) * (Polynomial.aeval (X none)) V' →
      ∃ (V : Polynomial ℤ), Polynomial.map (Int.castRingHom ℚ) V = V'
```

Primitive integral ordinary-variable factor and integral separated product. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/native-type.json), [exact declaration](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/target-metadata.json), [whole declaring module](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/source-module.lean.txt).

## Structural, API and duplication review

For each univariate coefficient, coeff_rename_mul_aeval identifies its products with the primitive factor coefficients as integer coefficients of the given product. exists_int_eq_of_gcd_eq_one then gives an integer witness for each coefficient, and Polynomial.mem_map_range assembles the integer polynomial. This coefficient descent is distinct from scalar compensation and from choosing a primitive representative. Explicit project dependencies are `Roth.coeff_rename_mul_aeval`, `Roth.exists_int_eq_of_gcd_eq_one`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_int_factors` | `Roth/Separation.lean:485` | Uses this helper in the separated polynomial proof; full original body replayed. |

1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/callers.json), [raw source search](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/source-search.json), and [direct value consumers](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/canonical-snapshot.json), [entry](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `SeparationPrivate175`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later separation and integrality theorems. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `SeparationPrivate175.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/native-receipt.json), [verification ledger](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/inputs.json), [baseline manifest](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/input-manifest.json), [build record](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/assessment.json), [overview entry](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/overview-entry.json), [portable validator](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/validate.py), [current manifest](../evidence/Roth.exists_int_polynomial_of_primitive_factor_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
