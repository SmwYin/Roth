# Roth.exists_coeffNone_basis_aux — private-prefilter assessment (167/293)

**SKIP under the explicit B1 private/local rule.** All applicable inventory, structural review, caller audit and native verification are complete. The full public mathlibable literature/search/contribution phases, including its per-definition infrastructure table, are n/a under this prefilter and were not run. No Agent was dispatched. [Exact rule](../evidence/Roth.exists_coeffNone_basis_aux/prefilter-rule.md), [rule provenance](../evidence/Roth.exists_coeffNone_basis_aux/prefilter-provenance.json).

## Statement and mathematical role

Private lemma at `Roth/Separation.lean:291–316`. The coefficient-polynomial span of a nonzero separated expansion has a finite basis of positive size at most n+1, whose members satisfy the original individual degree bounds. The exact original kernel type is:

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {P : MvPolynomial (Option τ) K},
  P ≠ 0 →
    ∀ {n : ℕ},
      P = ∑ ν : Fin (n + 1), MvPolynomial.X none ^ ↑ν * (MvPolynomial.rename some) (Roth.coeffNone P ↑ν) →
        ∃ (l : ℕ) (b :
          Module.Basis (Fin l) K ↥(Submodule.span K (Set.range fun (ν : Fin (n + 1)) ↦ Roth.coeffNone P ↑ν))),
          1 ≤ l ∧ l ≤ n + 1 ∧ ∀ (ρ : Fin l) (j : τ), MvPolynomial.degreeOf j ↑(b ρ) ≤ MvPolynomial.degreeOf (some j) P
```

Field coefficients, nonzero polynomial, finite distinguished-variable expansion. All captured bounds are displayed in the native type and exact source; no production weakening is proposed under the private prefilter.  The original private type and axioms are printed; the short source proof is retained in full, and any MCP pretty-printer body elision is not a full kernel-body dump. Names are resolved via `Lean.mkPrivateNameCore`, avoiding guessed numeric private names. [Native type](../evidence/Roth.exists_coeffNone_basis_aux/native-type.json), [exact declaration](../evidence/Roth.exists_coeffNone_basis_aux/target-excerpt.lean.txt), [metadata](../evidence/Roth.exists_coeffNone_basis_aux/target-metadata.json), [whole declaring module](../evidence/Roth.exists_coeffNone_basis_aux/source-module.lean.txt).

## Structural, API and duplication review

The finitely many coefficient polynomials span a finite-dimensional space. Nonzero input forces at least one nonzero coefficient and thus positive finrank; finrank_range_le_card gives the upper bound. The span lies in a support-restriction submodule by coefficient-support transport, so every basis vector inherits the individual degree bounds. This basis-selection helper is distinct from reconstruction and coordinate-family independence. Explicit project dependencies are `Roth.coeffNone`. No production generalization is proposed. A public contribution decision for its ingredients is separate from this private prefilter; their earlier assessments do not automatically transfer a verdict here.

The helper is used and is not junk. Preserve this internal proof boundary. Source review finds no sorry, unsafe/native decision, added axiom, TODO or raised resource limit. It proves a proposition about existing function/module types and registers no new instance or coercion. These are structural observations, not a fabricated full public infrastructure assessment.

## Complete caller and canonical audit

| Explicit source caller | Location | Role and validation |
|---|---|---|
| `Roth.exists_separated_representation` | `Roth/Separation.lean:325` | Uses this helper in the separated polynomial proof; full original body replayed. |

1 explicit source caller declarations, all in Separation.lean; 1 direct original value consumers. Exact separate lists retained. Entire Separation module proof bodies replay successfully with fresh target name. Source and kernel memberships are explicitly distinct: source uses include unfolding names that may disappear after elaboration, while elaborated implicit terms may retain direct references without a literal source token. The exact caller list and full source bodies are in [caller metadata](../evidence/Roth.exists_coeffNone_basis_aux/callers.json), [raw source search](../evidence/Roth.exists_coeffNone_basis_aux/source-search.json), and [direct value consumers](../evidence/Roth.exists_coeffNone_basis_aux/canonical-consumers.json). No transitive dependency or simp closure is claimed.

The native audit enumerates the exact tracked 293-name order with correct private modules; all 293 are unique, present and have values. Independent pre-execution source validation and the portable validator compare the complete array against the tracked order. [Canonical snapshot](../evidence/Roth.exists_coeffNone_basis_aux/canonical-snapshot.json), [entry](../evidence/Roth.exists_coeffNone_basis_aux/canonical-entry.json).

## Native theorem and full dependent proof verification

The whole declaring module was replayed in namespace `SeparationPrivate167`, replacing only this target's exact identifier by `replay`, changing its privacy/name and the outer namespace (lemma to public theorem); original proof bodies are retained. This includes every explicit caller and the later separation and integrality theorems. The scratch replay does not invoke the imported original private target. Root printed axioms for all public replay declarations, including `SeparationPrivate167.replay`; their checks include the private dependency chains. The original actual private theorem and axioms were independently resolved and checked. The full written source is preserved even if the MCP pretty-printer elides the large elaborated arithmetic proof body. Only standard axioms `propext`, `Classical.choice`, `Quot.sound` occur. The native receipt is complete success, partial=false, no warning/error, failed dependency or recovered sorryAx. The original proof and full module replay passed on their first execution. Two auxiliary display-only probes were rejected: explicit printing caused a style warning and output elision; withOptions initially lacked the command-monad instance. Their exact sources/receipts are retained separately. The final full-type capture runs in liftTermElabM with locally scoped pp.funBinderTypes and is complete and clean. No partial result or rejected probe is accepted proof evidence.

[Exact executed source](../evidence/Roth.exists_coeffNone_basis_aux/executed.lean.txt), [complete raw receipt](../evidence/Roth.exists_coeffNone_basis_aux/native-receipt.json), [verification ledger](../evidence/Roth.exists_coeffNone_basis_aux/verification.json). All 17 source/pin hashes freshly match the clean 2467-job baseline, so unchanged production inputs retain that build baseline. [Fresh hashes](../evidence/Roth.exists_coeffNone_basis_aux/inputs.json), [baseline manifest](../evidence/Roth.exists_coeffNone_basis_aux/input-manifest.json), [build record](../evidence/Roth.exists_coeffNone_basis_aux/baseline-build.txt).

The full existential basis-witness type and finite summation domains are explicitly captured in [full native type receipt](../evidence/Roth.exists_coeffNone_basis_aux/full-type-receipt.json) and its [exact executed source](../evidence/Roth.exists_coeffNone_basis_aux/full-type-executed.lean.txt); the default pretty-printer had hidden those inferable binder types.

The complete actual persistent execution document is also retained as [whole executed source](../evidence/Roth.exists_coeffNone_basis_aux/whole-executed.lean.txt); the validator checks that the new executed chunk is its exact suffix at the recorded native region.

## Completed disposition

Keep the private helper unchanged. All applicable work and evidence are complete; full public phases are explicitly n/a by the actual private rule. No verification item or user decision is pending. After acceptance, continue with the next declaration named by the tracked progress record. [Assessment](../evidence/Roth.exists_coeffNone_basis_aux/assessment.json), [overview entry](../evidence/Roth.exists_coeffNone_basis_aux/overview-entry.json), [portable validator](../evidence/Roth.exists_coeffNone_basis_aux/validate.py), [current manifest](../evidence/Roth.exists_coeffNone_basis_aux/copy-manifest.json). Root acceptance is recorded separately after independent review.
