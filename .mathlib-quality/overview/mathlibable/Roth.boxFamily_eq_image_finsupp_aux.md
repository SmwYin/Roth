# Roth.boxFamily_eq_image_finsupp_aux — private-prefilter assessment (244/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.boxFamily_eq_image_finsupp_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.boxFamily_eq_image_finsupp_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:280–297`. With finitely supported degree bounds, the integer polynomial box family is exactly the image of the finite Finsupp family with monomials in Iic(r) and coefficients in the integer interval[0,B]. The exact original kernel type is:

```lean
∀ {σ : Type u_1} (r : σ → ℕ) [inst : Finite ↑(Function.support r)] (B : ℕ),
  Roth.boxFamily r B =
    AddMonoidAlgebra.ofCoeff '' ↑((Finset.Iic (Finsupp.ofSupportFinite r ⋯)).finsupp fun (x : σ →₀ ℕ) ↦ Finset.Icc 0 ↑B)
```

Only finitely many variables have positive degree bounds. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and the original body printer contains no character-elision marker. The type printer suppresses an implicit finite-support proof with ⋯; the exact written statement is retained. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.boxFamily_eq_image_finsupp_aux/native-type.json), [exact declaration](../evidence/Roth.boxFamily_eq_image_finsupp_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.boxFamily_eq_image_finsupp_aux/target-metadata.json), [whole declaring module](../evidence/Roth.boxFamily_eq_image_finsupp_aux/source-module.lean.txt).

## Structural, API and duplication review

Map coefficient functions through AddMonoidAlgebra.ofCoeff. In the forward direction monomial_le_degreeOf places each support exponent in Iic of the finite-support degree function. Conversely the support bound implies every coordinate degree bound, and Finset.mem_finsupp_iff gives interval bounds on box monomials; off-box coefficients vanish. This representation is shared by finiteness and exact cardinality, which then use different existing finite-set laws. Explicit project dependencies are `Roth.boxFamily`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.boxFamily_finite` | `Roth/MainLemma.lean:301` | Transfers finiteness from the explicit finite coefficient family through AddMonoidAlgebra.ofCoeff. Full original body replayed. |
| `Roth.ncard_boxFamily` | `Roth/MainLemma.lean:311` | Computes the image cardinal using injectivity, Finset.card_finsupp and the finite box product formula. Full original body replayed. |

2 explicit source caller declarations, all in MainLemma.lean; 2 direct original value consumers. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.boxFamily_eq_image_finsupp_aux/callers.json), [raw source search](../evidence/Roth.boxFamily_eq_image_finsupp_aux/source-search.json), and [direct value consumers](../evidence/Roth.boxFamily_eq_image_finsupp_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.boxFamily_eq_image_finsupp_aux/canonical-snapshot.json), [entry](../evidence/Roth.boxFamily_eq_image_finsupp_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate244`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate244.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The original body printer contains no character-elision marker. All 24 axiom prints (23 public replay declarations and the original private theorem) use only standard axioms. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.boxFamily_eq_image_finsupp_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.boxFamily_eq_image_finsupp_aux/native-receipt.json), [verification ledger](../evidence/Roth.boxFamily_eq_image_finsupp_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.boxFamily_eq_image_finsupp_aux/inputs.json), [baseline manifest](../evidence/Roth.boxFamily_eq_image_finsupp_aux/input-manifest.json), [build record](../evidence/Roth.boxFamily_eq_image_finsupp_aux/baseline-build.txt).

The pre-execution exact293 and independently reconstructed whole-module checks are retained in [preparation checks](../evidence/Roth.boxFamily_eq_image_finsupp_aux/preparation-checks.json).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.boxFamily_eq_image_finsupp_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.boxFamily_eq_image_finsupp_aux/assessment.json), [overview entry](../evidence/Roth.boxFamily_eq_image_finsupp_aux/overview-entry.json), [portable validator](../evidence/Roth.boxFamily_eq_image_finsupp_aux/validate.py), [current manifest](../evidence/Roth.boxFamily_eq_image_finsupp_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
