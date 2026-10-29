# Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux — private-prefilter assessment (258/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:515–548`. Bounds integer remainder coefficients of diagonal Hasse derivatives by the natural floor of B times beta cubed under common exponential bounds. The exact original kernel type is:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] {f : Polynomial ℤ} {P : MvPolynomial σ ℤ}
  {r : σ → ℕ} {A B β : ℝ} {s : ℕ},
  (∀ (i : ℕ), |↑(f.coeff i)| ≤ A) →
    (∀ (k : σ), degreeOf k P ≤ r k) →
      (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
        ∑ k : σ, r k ≤ s →
          2 ^ s ≤ β →
            (1 + A) ^ s ≤ β → ∀ (j : σ →₀ ℕ) (i : ℕ), |(Roth.diag ((hasseDeriv j) P) %ₘ f).coeff i| ≤ ↑⌊B * β ^ 3⌋₊
```

Finite variables; total degree bound, divisor/input coefficient bounds and common growth-factor bounds. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/native-type.json), [exact declaration](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/target-metadata.json), [whole declaring module](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/source-module.lean.txt).

## Structural, API and duplication review

Derive beta>=1 from the powers-of-two bound. Bound the box product by 2^(sum r), and invoke the precise preceding coefficient estimate, absorbing the box, Hasse and remainder-elimination factors into beta. Treat divisor natural degree zero separately: monic constant is1 and has zero remainder, while nonmonic modByMonic returns the input and the zero-divisor estimate applies. Finish with Int.natCast_floor_eq_floor and Int.le_floor. The sole rpow-bound existence caller compares this floor with floor(B^c) before pigeonholing; no monicity premise is needed by this bound itself. Explicit project dependencies are `MvPolynomial.hasseDeriv`, `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, `Roth.diag`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_mem_RSet_le_index_of_rpow_bound_aux` | `Roth/MainLemma.lean:581` | Bounds each selected remainder coefficient by floor(B*beta^3), then compares floors using the supplied power budget B*beta^3<=B^c. Full original body replayed. |

1 explicit source caller declarations, all in MainLemma.lean; 1 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/callers.json), [raw source search](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/source-search.json), and [direct value consumers](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/canonical-snapshot.json), [entry](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate258`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate258.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/native-receipt.json), [verification ledger](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/inputs.json), [baseline manifest](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/input-manifest.json), [build record](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/assessment.json), [overview entry](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/overview-entry.json), [portable validator](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/validate.py), [current manifest](../evidence/Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
