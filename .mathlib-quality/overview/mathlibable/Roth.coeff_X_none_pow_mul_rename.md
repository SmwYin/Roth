# Roth.coeff_X_none_pow_mul_rename — private-prefilter assessment (154/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.coeff_X_none_pow_mul_rename/prefilter-rule.md), [rule provenance](../evidence/Roth.coeff_X_none_pow_mul_rename/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Separation.lean:64–76`. The coefficient of X none ^ ν times rename some Q at e is Q.coeff e.some when e none = ν, and zero otherwise. The exact original kernel type is:

```lean
∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (ν : ℕ) (Q : MvPolynomial τ R) (e : Option τ →₀ ℕ),
  (MvPolynomial.X none ^ ν * (MvPolynomial.rename some) Q).coeff e = if e none = ν then Q.coeff e.some else 0
```

Commutative semiring coefficients and arbitrary variables. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.coeff_X_none_pow_mul_rename/native-type.json), [exact declaration](../evidence/Roth.coeff_X_none_pow_mul_rename/target-excerpt.lean.txt), [metadata](../evidence/Roth.coeff_X_none_pow_mul_rename/target-metadata.json), [whole declaring module](../evidence/Roth.coeff_X_none_pow_mul_rename/source-module.lean.txt).

## Structural, API and duplication review

The product of a pure power of the distinguished variable and a polynomial in the remaining variables has coefficients selected by the distinguished exponent. The proof moves through optionEquivLeft, computes the univariate monomial coefficient, and returns to the original exponent coordinates. This is a private computational interface for the subsequent coefficient-family expansion; it is distinct from the full expansion and determinant theorems. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.eq_sum_X_none_pow_mul_coeffNone` | `Roth/Separation.lean:98` | Uses this helper in the separated polynomial proof; full original body replayed. |

1 explicit source caller declaration, all in Separation.lean; 1 direct original value consumer. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.coeff_X_none_pow_mul_rename/callers.json), [raw source search](../evidence/Roth.coeff_X_none_pow_mul_rename/source-search.json), and [direct value consumers](../evidence/Roth.coeff_X_none_pow_mul_rename/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.coeff_X_none_pow_mul_rename/canonical-snapshot.json), [entry](../evidence/Roth.coeff_X_none_pow_mul_rename/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `SeparationPrivate154`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later separation and integrality theorems. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `SeparationPrivate154.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The original private kernel printer is complete, with no MCP elision. The exact new execution region and the whole persistent document are both preserved. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact new execution region](../evidence/Roth.coeff_X_none_pow_mul_rename/executed.lean.txt), [whole executed document](../evidence/Roth.coeff_X_none_pow_mul_rename/whole-session-executed.lean.txt), [complete raw receipt](../evidence/Roth.coeff_X_none_pow_mul_rename/native-receipt.json), [verification ledger](../evidence/Roth.coeff_X_none_pow_mul_rename/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.coeff_X_none_pow_mul_rename/inputs.json), [baseline manifest](../evidence/Roth.coeff_X_none_pow_mul_rename/input-manifest.json), [build record](../evidence/Roth.coeff_X_none_pow_mul_rename/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.coeff_X_none_pow_mul_rename/assessment.json), [overview entry](../evidence/Roth.coeff_X_none_pow_mul_rename/overview-entry.json), [portable validator](../evidence/Roth.coeff_X_none_pow_mul_rename/validate.py), [current manifest](../evidence/Roth.coeff_X_none_pow_mul_rename/copy-manifest.json). Root acceptance is recorded separately after independent review.

The more recent [full build receipt](../evidence/Roth.coeff_X_none_pow_mul_rename/index-file-completion-2026-10-27.json) and [log](../evidence/Roth.coeff_X_none_pow_mul_rename/index-file-completion-2026-10-27.log) also pass on these same unchanged inputs.
