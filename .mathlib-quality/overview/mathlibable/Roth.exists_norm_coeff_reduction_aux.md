# Roth.exists_norm_coeff_reduction_aux — private-prefilter assessment (242/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.exists_norm_coeff_reduction_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.exists_norm_coeff_reduction_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/MainLemma.lean:212–243`. Whenever P %ₘ f differs from P and f≠1, one leading-term elimination lowers the degree ceiling by one, multiplies the coefficient bound by at most1+A, and preserves the remainder. Monicity is derived from the changed-remainder premise rather than assumed. The exact original kernel type is:

```lean
∀ {R : Type u_1} [inst : SeminormedRing R] {f P : Polynomial R} {A C : ℝ},
  (∀ (i : ℕ), ‖f.coeff i‖ ≤ A) →
    (∀ (i : ℕ), ‖P.coeff i‖ ≤ C) →
      ∀ {s : ℕ},
        P.natDegree ≤ s →
          f ≠ 1 →
            P %ₘ f ≠ P →
              0 < f.natDegree ∧
                f.natDegree ≤ s ∧
                  ∃ (Q : Polynomial R), Q.natDegree ≤ s - 1 ∧ (∀ (i : ℕ), ‖Q.coeff i‖ ≤ (1 + A) * C) ∧ P %ₘ f = Q %ₘ f
```

Seminormed ring, coefficient bounds, bounded input degree, divisor not one and remainder different from input. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the written source proof is retained in full, and the actual original-body printer elides999 characters and is not a complete kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.exists_norm_coeff_reduction_aux/native-type.json), [exact declaration](../evidence/Roth.exists_norm_coeff_reduction_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.exists_norm_coeff_reduction_aux/target-metadata.json), [whole declaring module](../evidence/Roth.exists_norm_coeff_reduction_aux/source-module.lean.txt).

## Structural, API and duplication review

Nontriviality follows from the changed remainder. Nonmonic divisors leave P unchanged, so the divisor is monic; the same changed-remainder condition gives P nonzero and divisor degree<=P degree. Define Q by subtracting the leading monomial multiple of f. The division recursion identifies the same remainder, its well-founded degree lemma yields the strict degree drop, and coefficient formulas plus norm_sub_le/norm_mul_le give the new bound. The public coefficient-remainder theorem iterates this step by strong induction; this helper is not itself the full iterated estimate. The coefficient bounds imply A,C≥0 using coefficient0; no extra sign or commutativity hypothesis is inserted. The one-step statement differs from its public caller, which iterates the estimate and accounts for the saturated natural exponent. Explicit project dependencies are none. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing mathematical types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.norm_coeff_modByMonic_le` | `Roth/MainLemma.lean:252` | Performs one degree-lowering elimination step in the strong induction, preserving the remainder and multiplying the coefficient budget by1+A. Full original body replayed. |

One explicit source caller declaration in MainLemma.lean and one direct original value consumer. Exact separate lists retained. Entire MainLemma module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.exists_norm_coeff_reduction_aux/callers.json), [raw source search](../evidence/Roth.exists_norm_coeff_reduction_aux/source-search.json), and [direct value consumers](../evidence/Roth.exists_norm_coeff_reduction_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. Actual preparation/check receipts are in [preparation checks](../evidence/Roth.exists_norm_coeff_reduction_aux/preparation-checks.json). [Canonical snapshot](../evidence/Roth.exists_norm_coeff_reduction_aux/canonical-snapshot.json), [entry](../evidence/Roth.exists_norm_coeff_reduction_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `MainLemmaPrivate242`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (private lemma/theorem to public theorem); original proof bodies are retained. This includes every explicit caller and downstream proofs in this module. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `MainLemmaPrivate242.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved; the original elaborated proof has an explicit999-character printer elision, rather than complete kernel-body output. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. No native attempt failed or was accepted partially.

[Exact executed source](../evidence/Roth.exists_norm_coeff_reduction_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.exists_norm_coeff_reduction_aux/native-receipt.json), [verification ledger](../evidence/Roth.exists_norm_coeff_reduction_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.exists_norm_coeff_reduction_aux/inputs.json), [baseline manifest](../evidence/Roth.exists_norm_coeff_reduction_aux/input-manifest.json), [build record](../evidence/Roth.exists_norm_coeff_reduction_aux/baseline-build.txt).

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.exists_norm_coeff_reduction_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.exists_norm_coeff_reduction_aux/assessment.json), [overview entry](../evidence/Roth.exists_norm_coeff_reduction_aux/overview-entry.json), [portable validator](../evidence/Roth.exists_norm_coeff_reduction_aux/validate.py), [current manifest](../evidence/Roth.exists_norm_coeff_reduction_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
