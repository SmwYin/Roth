# Roth.floor_rpow_count_lt_aux — private-prefilter assessment (247/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.floor_rpow_count_lt_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.floor_rpow_count_lt_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:320–327`. For x>0 and c>=1 the integer coefficient count2 floor(x^c)+1 is strictly smaller than(x+1)^(2c). The exact original kernel type is:

```lean
∀ {x c : ℝ}, 0 < x → 1 ≤ c → ↑(2 * ⌊x ^ c⌋₊ + 1) < (x + 1) ^ (2 * c)
```

Positive base and real exponent at least one. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.floor_rpow_count_lt_aux/native-type.json), [exact declaration](../evidence/Roth.floor_rpow_count_lt_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.floor_rpow_count_lt_aux/target-metadata.json), [whole declaring module](../evidence/Roth.floor_rpow_count_lt_aux/source-module.lean.txt).

## Structural, API and duplication review

Real.add_rpow_le_rpow_add gives x^c+1<=(x+1)^c. Rewrite the doubled exponent as a square and use positivity of x^c, the natural-floor upper bound and the expanded square to obtain a strict gap. This is the positive scalar base estimate raised to a positive integer count in pigeonhole_count; its strictness is not the final exponent-budget comparison. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.pigeonhole_count` | `Roth/MainLemma.lean:334` | Supplies the strict one-coordinate count estimate; the caller raises it to the positive n*D power, with a separate zero-power branch. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.floor_rpow_count_lt_aux/callers.json), [raw source search](../evidence/Roth.floor_rpow_count_lt_aux/source-search.json), and [direct value consumers](../evidence/Roth.floor_rpow_count_lt_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.floor_rpow_count_lt_aux/canonical-snapshot.json), [entry](../evidence/Roth.floor_rpow_count_lt_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate247`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate247.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The original formatted proof body has an explicitly reported 31,525-character MCP elision; it is not claimed to be a complete kernel-body dump. The full written source is preserved and the whole module replay passed. There are 24 standard-axiom print results (23 public replay declarations including the fresh target, plus the imported original). Pre-execution exact-array and independent whole-module reconstruction checks are retained in [preparation checks](../evidence/Roth.floor_rpow_count_lt_aux/preparation-checks.json). Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.floor_rpow_count_lt_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.floor_rpow_count_lt_aux/native-receipt.json), [verification ledger](../evidence/Roth.floor_rpow_count_lt_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.floor_rpow_count_lt_aux/inputs.json), [baseline manifest](../evidence/Roth.floor_rpow_count_lt_aux/input-manifest.json), [build record](../evidence/Roth.floor_rpow_count_lt_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.floor_rpow_count_lt_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.floor_rpow_count_lt_aux/assessment.json), [overview entry](../evidence/Roth.floor_rpow_count_lt_aux/overview-entry.json), [portable validator](../evidence/Roth.floor_rpow_count_lt_aux/validate.py), [current manifest](../evidence/Roth.floor_rpow_count_lt_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
