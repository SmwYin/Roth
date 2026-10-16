# GenWronskian unused-public-parameter proposal

Status: compiled proposal; not applied, awaiting a scoped user decision through the project orchestrator. Existing public signatures remain unchanged.

## Dependent-family vanishing theorem

Proposed edit: insert `omit [Fintype σ] in` immediately before the existing docstring of `Roth.genWronskian_eq_zero_of_not_linearIndependent`. Keep all explicit arguments, conclusion, proof and documentation unchanged. The resulting theorem works for arbitrary variable types and removes both inherited unused-section-variable and unused-Fintype warnings.

The fresh dedicated declaration worker compiled the complete candidate as `Roth.d02_omit` in `/private/tmp/roth-d02-omit.lean` using the actual project imports. It exits0, prints its elaborated signature without Fintype, and reports only standard axioms. The proof does not call the target theorem. Its matrix indices are `Fin l`, already finite independently of σ.

Source search across project Lean files finds no callers of this vanishing theorem. Ordinary future applications infer the same mathematical arguments; explicit `@` application loses the Fintype binder and shifts later argument positions. This is a public signature change, so scoped authorization is required before changing the source. Earlier Box/Wronskian approvals do not authorize it. Full downstream build gates remain mandatory if approved.

The broader optional coefficient-ring generalizations explored in declarations1–2 were closed under preservation of the current API and are not pending proposals.
