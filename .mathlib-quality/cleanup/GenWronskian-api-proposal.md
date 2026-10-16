# GenWronskian unused-public-parameter proposal

Status: compiled proposal; not applied, awaiting a scoped user decision through the project orchestrator. Existing public signatures remain unchanged.

## Dependent-family vanishing theorem

Proposed edit: insert `omit [Fintype σ] in` immediately before the existing docstring of `Roth.genWronskian_eq_zero_of_not_linearIndependent`. Keep all explicit arguments, conclusion, proof and documentation unchanged. The resulting theorem works for arbitrary variable types and removes both inherited unused-section-variable and unused-Fintype warnings.

The fresh dedicated declaration worker compiled the complete candidate as `Roth.d02_omit` in `/private/tmp/roth-d02-omit.lean` using the actual project imports. It exits0, prints its elaborated signature without Fintype, and reports only standard axioms. The proof does not call the target theorem. Its matrix indices are `Fin l`, already finite independently of σ.

Source search across project Lean files finds no callers of this vanishing theorem. Ordinary future applications infer the same mathematical arguments; explicit `@` application loses the Fintype binder and shifts later argument positions. This is a public signature change, so scoped authorization is required before changing the source. Earlier Box/Wronskian approvals do not authorize it. Full downstream build gates remain mandatory if approved.

The broader optional coefficient-ring generalizations explored in declarations1–2 were closed under preservation of the current API and are not pending proposals.

## Finite row determinant expansion

Proposed edit: remove only `[DecidableEq ι]` from `Roth.det_sum_rows`; keep the complete finite-row determinant formula and all other binders unchanged. The worker compiled `/private/tmp/roth-d18-candidate.lean` using the project imports, exit0; `/private/tmp/roth-d18-candidate.log` prints the exact type without DecidableEq and standard axioms `[propext, Classical.choice, Quot.sound]`. Its independent proof directly uses multilinear finite-sum/scalar expansion and does not invoke the target theorem. No local Classical scope is needed.

Final project caller search finds only the same-file private `wronskian_kronecker_eq_sum_aux`, which applies `det_sum_rows s c (fun μ d ν ↦ kronecker k (hasseDeriv d (φ ν)))` with no explicit instance argument. The original direct headline call moved into this meaningful helper during decomposition; inferred data remain unchanged. No explicit `@det_sum_rows` calls or external project callers exist. Future explicit `@` calls lose the DecidableEq binder and shift later positions. The source retains the instance pending a scoped user decision; full downstream build gates remain mandatory if approved. This proposal is independent of the earlier vanishing theorem's Fintype omission.
