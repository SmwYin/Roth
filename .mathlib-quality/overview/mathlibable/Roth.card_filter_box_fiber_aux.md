# Roth.card_filter_box_fiber_aux — private-prefilter assessment (126/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.card_filter_box_fiber_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.card_filter_box_fiber_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Lattice.lean:100–124`. A fixed last-coordinate fiber of a filtered rectangular box has the same cardinality as the smaller box filtered after extension by that coordinate. The exact original kernel type is:

```lean
∀ {m : ℕ} (r : Fin (m + 1) → ℕ) (p : (Fin (m + 1) →₀ ℕ) → Prop)
  [inst : DecidablePred p] {i : ℕ},
  i ≤ r (Fin.last m) →
    {d ∈ Roth.box (r ∘ Fin.castSucc) | p (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i)}.card =
      {d ∈ Finset.filter p (Roth.box r) | d (Fin.last m) = i}.card
```

A natural rectangular box, a decidable predicate, and a last coordinate within its bound. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.card_filter_box_fiber_aux/native-type.json), [exact declaration](../evidence/Roth.card_filter_box_fiber_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.card_filter_box_fiber_aux/target-metadata.json), [whole declaring module](../evidence/Roth.card_filter_box_fiber_aux/source-module.lean.txt).

## Structural, API and duplication review

Finset.card_bij compares the smaller filtered box with the fixed last-coordinate fiber. Extension preserves all old coordinates and sets the last to i; the bound hi ensures membership. Injectivity follows by restriction to castSucc coordinates. Surjectivity reconstructs the smaller vector with Finsupp.equivFunOnFinite and proves its extension equals the original by Fin.lastCases. This is the geometric fiber-identification step; the public cardinality theorem separately sums the fibers. Explicit project dependencies are `Roth.extend_apply_castSucc`, `Roth.extend_apply_last`, `Roth.mem_box`, `Roth.box`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.card_filter_box_last` | `Roth/Lattice.lean:131` | Uses this helper in the lattice proof; full original body replayed. |

1 explicit source caller declarations, all in Lattice.lean; 1 direct original value consumers. Exact separate lists retained. Entire module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.card_filter_box_fiber_aux/callers.json), [raw source search](../evidence/Roth.card_filter_box_fiber_aux/source-search.json), and [direct value consumers](../evidence/Roth.card_filter_box_fiber_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.card_filter_box_fiber_aux/canonical-snapshot.json), [entry](../evidence/Roth.card_filter_box_fiber_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `LatticeBoxFiberAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later lattice-count proof. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `LatticeBoxFiberAssessment.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.card_filter_box_fiber_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.card_filter_box_fiber_aux/native-receipt.json), [verification ledger](../evidence/Roth.card_filter_box_fiber_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.card_filter_box_fiber_aux/inputs.json), [baseline manifest](../evidence/Roth.card_filter_box_fiber_aux/input-manifest.json), [build record](../evidence/Roth.card_filter_box_fiber_aux/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.card_filter_box_fiber_aux/assessment.json), [overview entry](../evidence/Roth.card_filter_box_fiber_aux/overview-entry.json), [portable validator](../evidence/Roth.card_filter_box_fiber_aux/validate.py), [current manifest](../evidence/Roth.card_filter_box_fiber_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
