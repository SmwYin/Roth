# Roth.two_lt_rpow_aux — private-prefilter assessment (240/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.two_lt_rpow_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.two_lt_rpow_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:156–170`. A nonnegative delta and a positive natural degree turn log2<delta squared times logq into2<q to the delta-degree power. The exact original kernel type is:

```lean
∀ {δ : ℝ},
  0 ≤ δ → ∀ {q₁ r₁ : ℕ}, 0 < r₁ → Real.log 2 < δ ^ 2 * Real.log ↑q₁ → 2 < ↑q₁ ^ (δ * ↑r₁)
```

Nonnegative delta, positive degree and squared-delta log bound greater than log2. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and the actual original-body printer elides42458 characters and is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.two_lt_rpow_aux/native-type.json), [exact declaration](../evidence/Roth.two_lt_rpow_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.two_lt_rpow_aux/target-metadata.json), [whole declaring module](../evidence/Roth.two_lt_rpow_aux/source-module.lean.txt).

## Structural, API and duplication review

The threshold forces logq>0 and the natural denominator q>=2. If delta*logq<=log2, squaring this nonnegative inequality and combining logq>=log2 contradicts the delta-squared threshold. Then multiply by the degree>=1 and apply Real.lt_rpow_of_log_lt. This establishes the positive floor-power threshold used in three_small_factors; it differs from the public four-power estimate and from comparing all three small factors. The public `Roth.four_lt_rpow` shares the square-comparison method but uses a sufficient3 bound to obtain4; this helper instead uses a strict log2 threshold to obtain2. These different numerical interfaces are not identified, and no public contribution verdict is inherited. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.three_small_factors` | `Roth/MainLemma.lean:180` | Uses the derived logarithmic threshold to establish the floor-power lower bound needed for logarithms and the three exponential comparisons. Full original body replayed. |

One explicit source caller declaration in MainLemma.lean and one direct original value consumer. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.two_lt_rpow_aux/callers.json), [raw source search](../evidence/Roth.two_lt_rpow_aux/source-search.json), and [direct value consumers](../evidence/Roth.two_lt_rpow_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. The actual preparation and pre-execution check are recorded in [preparation checks](../evidence/Roth.two_lt_rpow_aux/preparation-checks.json). [Canonical snapshot](../evidence/Roth.two_lt_rpow_aux/canonical-snapshot.json), [entry](../evidence/Roth.two_lt_rpow_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate240`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate240.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved; the original elaborated arithmetic body has an explicit42458-character printer elision, which is disclosed rather than presented as complete kernel-body output. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.two_lt_rpow_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.two_lt_rpow_aux/native-receipt.json), [verification ledger](../evidence/Roth.two_lt_rpow_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.two_lt_rpow_aux/inputs.json), [baseline manifest](../evidence/Roth.two_lt_rpow_aux/input-manifest.json), [build record](../evidence/Roth.two_lt_rpow_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.two_lt_rpow_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.two_lt_rpow_aux/assessment.json), [overview entry](../evidence/Roth.two_lt_rpow_aux/overview-entry.json), [portable validator](../evidence/Roth.two_lt_rpow_aux/validate.py), [current manifest](../evidence/Roth.two_lt_rpow_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
