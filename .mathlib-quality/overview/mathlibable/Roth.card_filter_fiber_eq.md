# Roth.card_filter_fiber_eq — private-prefilter assessment (129/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.card_filter_fiber_eq/prefilter-rule.md), [rule provenance](../evidence/Roth.card_filter_fiber_eq/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Lattice.lean:147–156`. Rewrites the weighted last-coordinate fiber as a smaller box with lambda shifted by the last-coordinate contribution. The exact original kernel type is:

```lean
∀ {n : ℕ} (r : Fin (n + 1) → ℕ) (lam : ℝ) (i : ℕ),
  ↑{d ∈ Roth.box (r ∘ Fin.castSucc) |
          Roth.weight r (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last n) i) ≤
            (↑(n + 1) - lam) / 2}.card =
    ↑{d ∈ Roth.box (r ∘ Fin.castSucc) |
          Roth.weight (r ∘ Fin.castSucc) d ≤ (↑n - (lam - 1 + 2 * ↑i / ↑(r (Fin.last n)))) / 2}.card
```

Natural box bounds, real λ, and any chosen last coordinate. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.card_filter_fiber_eq/native-type.json), [exact declaration](../evidence/Roth.card_filter_fiber_eq/target-excerpt.lean.txt), [metadata](../evidence/Roth.card_filter_fiber_eq/target-metadata.json), [whole declaring module](../evidence/Roth.card_filter_fiber_eq/source-module.lean.txt).

## Structural, API and duplication review

Weight additivity, injective mapDomain transport and singleton evaluation split the extended vector weight into the smaller-vector contribution plus i/r_last. An affine rearrangement moves that last-coordinate contribution into the shifted lambda parameter. Finset.filter_congr identifies the predicates before cardinalities are cast to real numbers. No denominator positivity is required for this rearrangement; all box bounds and last coordinates may be zero. Explicit project dependencies are `Roth.weight_add`, `Roth.weight_mapDomain`, `Roth.weight_single`, `Roth.box`, `Roth.weight`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.card_filter_weight_le_succ_aux` | `Roth/Lattice.lean:166` | Uses this helper in the lattice proof; full original body replayed. |

1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.card_filter_fiber_eq/callers.json), [raw source search](../evidence/Roth.card_filter_fiber_eq/source-search.json), and [direct value consumers](../evidence/Roth.card_filter_fiber_eq/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.card_filter_fiber_eq/canonical-snapshot.json), [entry](../evidence/Roth.card_filter_fiber_eq/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `LatticeWeightFiberAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later lattice-count proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `LatticeWeightFiberAssessment.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.card_filter_fiber_eq/executed.lean.txt), [complete raw receipt](../evidence/Roth.card_filter_fiber_eq/native-receipt.json), [verification ledger](../evidence/Roth.card_filter_fiber_eq/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.card_filter_fiber_eq/inputs.json), [baseline manifest](../evidence/Roth.card_filter_fiber_eq/input-manifest.json), [build record](../evidence/Roth.card_filter_fiber_eq/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.card_filter_fiber_eq/assessment.json), [overview entry](../evidence/Roth.card_filter_fiber_eq/overview-entry.json), [portable validator](../evidence/Roth.card_filter_fiber_eq/validate.py), [current manifest](../evidence/Roth.card_filter_fiber_eq/copy-manifest.json). Root acceptance is recorded separately after independent review.
