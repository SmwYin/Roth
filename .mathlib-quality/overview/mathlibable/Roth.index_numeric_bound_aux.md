# Roth.index_numeric_bound_aux — private-prefilter assessment (212/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.index_numeric_bound_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.index_numeric_bound_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Theta.lean:531–549`. A real index parameter satisfying the minimum of a linear and quadratic lower estimate against l(Φ+δ) is at most 2(Φ+sqrt Φ+sqrt δ) when Φ is nonnegative, δ≤1, the scale is at least three, and 0<l≤scale+1. The exact original kernel type is:

```lean
∀ {θ Φ δ rp l : ℝ},
  0 ≤ Φ →
    δ ≤ 1 → 3 ≤ rp → 0 < l → l ≤ rp + 1 → min (l * θ / 2) (rp * θ ^ 2 / 3) ≤ l * (Φ + δ) → θ ≤ 2 * (Φ + √Φ + √δ)
```

Nonnegative Phi, delta at most one, scale at least three and positive length at most scale plus one. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.index_numeric_bound_aux/native-type.json), [exact declaration](../evidence/Roth.index_numeric_bound_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.index_numeric_bound_aux/target-metadata.json), [whole declaring module](../evidence/Roth.index_numeric_bound_aux/source-module.lean.txt).

## Structural, API and duplication review

Split min_le_iff into a linear and quadratic branch. In the first divide by positive l and compare δ with sqrt δ via Real.le_sqrt_self_iff. In the second derive 3l≤4rp, hence θ²≤4(Φ+δ), use Real.sq_sqrt and the general square-root square identity together with nonnegative square roots to bound θ by 2(sqrt Φ+sqrt δ), and add the nonnegative Φ term. This closes the scalar real estimate in index_le_lem6 after combining determinant lower and upper bounds; it is distinct from nonvanishing and derivative-weight admissibility. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.index_le_lem6` | `Roth/Theta.lean:556` | Converts the combined determinant lower/upper estimates and min_le_sum_max into the final Lemma 6 index bound; full original caller body replayed. |

1 explicit source caller declarations, all in Theta.lean; 1 direct original value consumers. Exact separate lists retained. Entire Theta module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.index_numeric_bound_aux/callers.json), [raw source search](../evidence/Roth.index_numeric_bound_aux/source-search.json), and [direct value consumers](../evidence/Roth.index_numeric_bound_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.index_numeric_bound_aux/canonical-snapshot.json), [entry](../evidence/Roth.index_numeric_bound_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `ThetaPrivate212`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index estimates and Lemmas 5–7. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `ThetaPrivate212.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.index_numeric_bound_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.index_numeric_bound_aux/native-receipt.json), [verification ledger](../evidence/Roth.index_numeric_bound_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.index_numeric_bound_aux/inputs.json), [baseline manifest](../evidence/Roth.index_numeric_bound_aux/input-manifest.json), [build record](../evidence/Roth.index_numeric_bound_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.index_numeric_bound_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.index_numeric_bound_aux/assessment.json), [overview entry](../evidence/Roth.index_numeric_bound_aux/overview-entry.json), [portable validator](../evidence/Roth.index_numeric_bound_aux/validate.py), [current manifest](../evidence/Roth.index_numeric_bound_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
