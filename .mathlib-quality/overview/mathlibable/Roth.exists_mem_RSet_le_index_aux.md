# Roth.exists_mem_RSet_le_index_aux — private-prefilter assessment (259/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.exists_mem_RSet_le_index_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.exists_mem_RSet_le_index_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:550–567`. Uses a strict finite remainder count to construct a nonzero integer box polynomial whose index at the diagonal root is at least an arbitrary real cutoff. The exact original kernel type is:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {f : Polynomial ℤ} {α : ℝ},
  f.Monic →
    (Polynomial.aeval α) f = 0 →
      ∀ (r : σ → ℕ) (B C : ℕ) (J : Finset (σ →₀ ℕ)) {γ : ℝ},
        (∀ W ∈ Roth.boxFamily r B, ∀ j ∈ J, ∀ i < f.natDegree, |(Roth.diag ((hasseDeriv j) W) %ₘ f).coeff i| ≤ ↑C) →
          ↑(2 * C + 1) ^ (f.natDegree * J.card) < (↑B + 1) ^ ∏ k : σ, (r k + 1) →
            (∀ (d : σ →₀ ℕ), (∀ (k : σ), d k ≤ r k) → Roth.weight r d < γ → d ∈ J) →
              ∃ P ∈ Roth.RSet (↑B) r, γ ≤ Roth.index ((map (Int.castRingHom ℝ)) P) (fun (x : σ) ↦ α) r
```

Monic integer equation for the point, remainder coefficient/count bounds, and derivative set covering all low-weight box indices. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.exists_mem_RSet_le_index_aux/native-type.json), [exact declaration](../evidence/Roth.exists_mem_RSet_le_index_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.exists_mem_RSet_le_index_aux/target-metadata.json), [whole declaring module](../evidence/Roth.exists_mem_RSet_le_index_aux/source-module.lean.txt).

## Structural, API and duplication review

Apply exists_ne_modByMonic_eq to obtain two distinct box polynomials with matching selected remainders. Their difference belongs to RSet by sub_mem_RSet. Injectivity of the integer-to-real map preserves nonzeroness and coordinate degrees via degrees_map_of_injective; eval_hasseDeriv_sub_eq_zero and le_index_of_forall_eval_eq_zero turn remainder equality into the index lower bound. The sole rpow-bound caller supplies a filtered weight box J containing all indices strictly below the target cutoff. This is the algebraic pigeonhole-to-index step, separate from estimates proving its strict count premise. Explicit project dependencies are `MvPolynomial.hasseDeriv`, `Roth.RSet`, `Roth.boxFamily`, `Roth.diag`, `Roth.eval_hasseDeriv_sub_eq_zero`, `Roth.exists_ne_modByMonic_eq`, `Roth.index`, `Roth.le_index_of_forall_eval_eq_zero`, `Roth.sub_mem_RSet`, `Roth.weight`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | `Roth/MainLemma.lean:581` | Combines its filtered weight box, remainder coefficient bounds and strict cardinality estimate into the required high-index polynomial. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.exists_mem_RSet_le_index_aux/callers.json), [raw source search](../evidence/Roth.exists_mem_RSet_le_index_aux/source-search.json), and [direct value consumers](../evidence/Roth.exists_mem_RSet_le_index_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.exists_mem_RSet_le_index_aux/canonical-snapshot.json), [entry](../evidence/Roth.exists_mem_RSet_le_index_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate259`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate259.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.exists_mem_RSet_le_index_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.exists_mem_RSet_le_index_aux/native-receipt.json), [verification ledger](../evidence/Roth.exists_mem_RSet_le_index_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.exists_mem_RSet_le_index_aux/inputs.json), [baseline manifest](../evidence/Roth.exists_mem_RSet_le_index_aux/input-manifest.json), [build record](../evidence/Roth.exists_mem_RSet_le_index_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.exists_mem_RSet_le_index_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.exists_mem_RSet_le_index_aux/assessment.json), [overview entry](../evidence/Roth.exists_mem_RSet_le_index_aux/overview-entry.json), [portable validator](../evidence/Roth.exists_mem_RSet_le_index_aux/validate.py), [current manifest](../evidence/Roth.exists_mem_RSet_le_index_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
