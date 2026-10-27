# Roth.mem_support_taylor_iff — private-prefilter assessment (134/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.mem_support_taylor_iff/prefilter-rule.md), [rule provenance](../evidence/Roth.mem_support_taylor_iff/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Index.lean:62–64`. Taylor support membership is equivalent to nonvanishing of the corresponding Hasse derivative at the center. The exact original kernel type is:

```lean
∀ {σ : Type u_1} {P : MvPolynomial σ ℝ} {α : σ → ℝ} {d : σ →₀ ℕ},
  d ∈ ((MvPolynomial.taylor α) P).support ↔ (MvPolynomial.eval α) ((MvPolynomial.hasseDeriv d) P) ≠ 0
```

A real polynomial and point; no finiteness of the variable type. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.mem_support_taylor_iff/native-type.json), [exact declaration](../evidence/Roth.mem_support_taylor_iff/target-excerpt.lean.txt), [metadata](../evidence/Roth.mem_support_taylor_iff/target-metadata.json), [whole declaring module](../evidence/Roth.mem_support_taylor_iff/source-module.lean.txt).

## Structural, API and duplication review

A multi-index lies in the Taylor support exactly when its Taylor coefficient is nonzero. mem_support_iff gives the coefficient criterion, and coeff_taylor identifies that coefficient with evaluation of the Hasse derivative. The private bridge is the common support-to-derivative interface for the index bound, attainment, lower-bound characterization and degree estimate. It is distinct from the quantitative inequalities it supports and requires no finite variable-type instance. Explicit project dependencies are `MvPolynomial.coeff_taylor`, `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.index_le_weight` | `Roth/Index.lean:69` | Uses this helper in the index proof; full original body replayed. |
| `Roth.exists_weight_eq_index` | `Roth/Index.lean:76` | Uses this helper in the index proof; full original body replayed. |
| `Roth.le_index_iff` | `Roth/Index.lean:85` | Uses this helper in the index proof; full original body replayed. |
| `Roth.index_le_card` | `Roth/Index.lean:224` | Uses this helper in the index proof; full original body replayed. |

4 explicit source caller declarations, all in Index.lean; 4 direct original value consumers. Exact separate lists retained. Entire Index module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.mem_support_taylor_iff/callers.json), [raw source search](../evidence/Roth.mem_support_taylor_iff/source-search.json), and [direct value consumers](../evidence/Roth.mem_support_taylor_iff/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.mem_support_taylor_iff/canonical-snapshot.json), [entry](../evidence/Roth.mem_support_taylor_iff/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `IndexSupportAssessment`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later index laws. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `IndexSupportAssessment.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.mem_support_taylor_iff/executed.lean.txt), [complete raw receipt](../evidence/Roth.mem_support_taylor_iff/native-receipt.json), [verification ledger](../evidence/Roth.mem_support_taylor_iff/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.mem_support_taylor_iff/inputs.json), [baseline manifest](../evidence/Roth.mem_support_taylor_iff/input-manifest.json), [build record](../evidence/Roth.mem_support_taylor_iff/baseline-build.txt).

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.mem_support_taylor_iff/assessment.json), [overview entry](../evidence/Roth.mem_support_taylor_iff/overview-entry.json), [portable validator](../evidence/Roth.mem_support_taylor_iff/validate.py), [current manifest](../evidence/Roth.mem_support_taylor_iff/copy-manifest.json). Root acceptance is recorded separately after independent review.
