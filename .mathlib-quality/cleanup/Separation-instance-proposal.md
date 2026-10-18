# Separation: approved scoped unused-instance menu

Proposal: remove unused `[Fintype τ]` and `[DecidableEq τ]` from the eleven public theorems below; remove only `[DecidableEq τ]` from `exists_det_eq_mul`, retaining its `[Fintype τ]` because the existing generalized-Wronskian existence API uses it. All polynomial data, coefficient assumptions, nonzero/degree hypotheses and conclusions stay exactly the same. `coeffNone` and every other public declaration stay unchanged.

Implementation: scoped `omit` commands and local `classical` where required, plus omission of the same unused private instances on `coeff_X_none_pow_mul_rename`. No argument is passed explicitly for these instances in project callers; usual calls can synthesize fewer instances. All calls remain subject to complete module/caller LSP and full/separate LeanEval gates at each actual application. Later file consolidation may reduce redundant section-instance scaffolding only after actual type rechecks.

| Public theorem | Proposed removal |
|---|---|
| `eq_mapDomain_some_add_single` | `[Fintype τ]`, `[DecidableEq τ]` |
| `coeff_coeffNone` | `[Fintype τ]`, `[DecidableEq τ]` |
| `eq_sum_X_none_pow_mul_coeffNone` | `[Fintype τ]`, `[DecidableEq τ]` |
| `degreeOf_coeffNone_le` | `[Fintype τ]`, `[DecidableEq τ]` |
| `coeff_rename_mul_aeval` | `[Fintype τ]`, `[DecidableEq τ]` |
| `hasseDeriv_rename_mul_aeval` | `[Fintype τ]`, `[DecidableEq τ]` |
| `degreeOf_rename_mul_aeval` | `[Fintype τ]`, `[DecidableEq τ]` |
| `degreeOf_none_rename_mul_aeval` | `[Fintype τ]`, `[DecidableEq τ]` |
| `exists_separated_representation` | `[Fintype τ]`, `[DecidableEq τ]` |
| `det_hasseDeriv_separated` | `[Fintype τ]`, `[DecidableEq τ]` |
| `exists_int_factors` | `[Fintype τ]`, `[DecidableEq τ]` |
| `exists_det_eq_mul` | `[DecidableEq τ]` only |

## Exact compiled evidence

- Whole original file independently re-proved in `Roth.SeparationCandidate`, with exactly the scoped omissions and its required private supporting omission: actual `lake env lean /private/tmp/roth-separation-hypothesis-candidate.lean`, session5221 exit0 (proof candidate), then strengthened approval-evidence session79423 exit0.
- The final probe imports the actual built Separation module and independently compiles every original proof again. All12 original public contracts recover by `rfl` proof-irrelevance equalities with explicit adapters for the removed instance arguments.
- Actual expression traversal confirms no `DecidableEq` constant in all12 candidate types and no `Fintype` in the11 selected types. All12 candidate axiom sets consist only of `propext`, `Classical.choice`, `Quot.sound`.
- Final raw source/log: `/private/tmp/roth-separation-hypothesis-candidate.{lean,log}`. An intermediate import check ran during module rebuilding and failed because the olean was temporarily absent; this failed attempt is excluded from the successful evidence above.

This is a mathematical generality improvement: the eleven results concern finite polynomial support and need no finite ambient variable type. It does not claim that the final generalized-Wronskian construction is already available for an arbitrary infinite variable type. Baseline complete LSP already reports these unused-instance warnings. Each affected original declaration still receives its own fresh full audit/search/literature/verification pass before applying its approved scoped change. The user approved exactly these listed removals and necessary caller repairs; no other API generalization.

Status: USER APPROVED, relayed by the coordinator during original21 helper audits. The original21 frozen batch applied no public omission. The first six approved revisits now remove the pair from `eq_mapDomain_some_add_single`, `coeff_coeffNone`, `eq_sum_X_none_pow_mul_coeffNone`, `degreeOf_coeffNone_le`, `coeff_rename_mul_aeval`, and `hasseDeriv_rename_mul_aeval`, each with fresh audit, exact original adapters, caller checks and independent publication gates. The other three already-audited targets continue in dependency/source order; the three remaining originals apply their approved removals during their ordinary declaration audit. Original audit counts do not increase on revisits. The user has now considered and declined both public-wrapper deletions and Domain coefficient weakening; preserve those APIs and hypotheses. No decision remains pending for those alternatives. Nat codomain remains unchanged absent separate explicit approval.
