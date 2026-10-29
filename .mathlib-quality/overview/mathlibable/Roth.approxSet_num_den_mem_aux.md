# Roth.approxSet_num_den_mem_aux — private-prefilter assessment (273/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.approxSet_num_den_mem_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.approxSet_num_den_mem_aux/prefilter-provenance.json).

## Statement and mathematical role

Private theorem at `Roth/Main.lean:149–156`. Reducing a rational approximation to its canonical numerator and denominator preserves membership in approxSet for nonnegative approximation exponent. The exact original kernel type is:

```lean
∀ {α κ : ℝ},
  0 ≤ κ → ∀ {h : ℤ} {q : ℕ}, (h, q) ∈ Roth.approxSet α κ → ((↑h / ↑q).num, (↑h / ↑q).den) ∈ Roth.approxSet α κ
```

Nonnegative exponent and an approximation pair with positive denominator. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.approxSet_num_den_mem_aux/native-type.json), [exact declaration](../evidence/Roth.approxSet_num_den_mem_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.approxSet_num_den_mem_aux/target-metadata.json), [whole declaring module](../evidence/Roth.approxSet_num_den_mem_aux/source-module.lean.txt).

## Structural, API and duplication review

Rat.den_dvd gives the reduced positive denominator at most the original q. Rat.cast_def rewrites the value without changing it, and nonnegative-exponent monotonicity makes the reciprocal error tolerance no smaller at the reduced denominator. The sole exists_reduced_approx caller uses the result to force bounded reduced representatives under its contradiction hypothesis; finite fibers then handle arbitrary unreduced pairs. Explicit project dependencies are `Roth.approxSet`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_reduced_approx` | `Roth/Main.lean:164` | Moves an arbitrary approximation to a coprime canonical numerator/denominator pair before bounding the finite rational image. Full original body replayed. |

1 explicit source caller declarations, all in Main.lean; 1 direct original value consumers. Exact separate lists retained. Entire Main module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.approxSet_num_den_mem_aux/callers.json), [raw source search](../evidence/Roth.approxSet_num_den_mem_aux/source-search.json), and [direct value consumers](../evidence/Roth.approxSet_num_den_mem_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.approxSet_num_den_mem_aux/canonical-snapshot.json), [entry](../evidence/Roth.approxSet_num_den_mem_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainPrivate273`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainPrivate273.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.approxSet_num_den_mem_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.approxSet_num_den_mem_aux/native-receipt.json), [verification ledger](../evidence/Roth.approxSet_num_den_mem_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.approxSet_num_den_mem_aux/inputs.json), [baseline manifest](../evidence/Roth.approxSet_num_den_mem_aux/input-manifest.json), [build record](../evidence/Roth.approxSet_num_den_mem_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.approxSet_num_den_mem_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.approxSet_num_den_mem_aux/assessment.json), [overview entry](../evidence/Roth.approxSet_num_den_mem_aux/overview-entry.json), [portable validator](../evidence/Roth.approxSet_num_den_mem_aux/validate.py), [current manifest](../evidence/Roth.approxSet_num_den_mem_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
