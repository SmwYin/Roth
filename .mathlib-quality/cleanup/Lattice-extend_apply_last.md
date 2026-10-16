# Phase 4 — `Roth.extend_apply_last`

Scope: only the private declaration in `Roth/Lattice.lean`, originally lines 90–95.
Baseline supplied by owner: full build and LeanEval exit 0, logs
`/private/tmp/roth-lattice-d05-{full,leaneval}.log`. Existing copyright-header warning is
explicitly preserved by the user's choice. No Git or shared progress mutations.

## References

Read both lean4 and mathlib-quality SKILL.md files, the complete Phase-4 worker prompt,
and all five required references: golfing-rules, proof-patterns, mathlib-search,
generalisation-patterns, cleanup-gates. Read declaration formatting and naming guidance.

## Full audit

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | No declaration warning; complete file diagnostics reports only existing header warning at line 1. |
| 2 | HAVE SCAN | Original anonymous `have` at L92 has `by` proof content (range contradiction), used once in final simp. Not a trivial term binding; remove only because whole-proof simp subsumes it. |
| 3 | SET_OPTION | None; no limits or suppressions added. |
| 4 | SIMP SQUEEZE | Original and final simp are terminal; preserve unsqueezed form. |
| 5 | NAMING | `extend_apply_last` describes the extension's evaluation at last; snake_case with no banned patterns/abbreviations. No rename. |
| 6 | LINE PACKING | Two signature lines measured below, both justified. |
| 7 | BY PLACEMENT | `by` ends conclusion line. |
| 8 | FORMAT | Two-space proof indentation, no empty proof lines, one tactic. |
| 9 | COMMENTS | No proof comments to preserve. |
| 10 | DOCSTRING | Private equation helper; none required or altered. |
| 11 | VISIBILITY | Private helper used by four rewrites in the fibre-count bijection; retain private. |
| 12 | STRUCTURE | One-line body; no conjunction or long branch. |
| 13 | MATHLIB | Partial existing API used directly, five searches below; no exact replacement discovered. |
| 14 | JUNK DEF | n/a: lemma, no data definition. |
| 15 | EXISTS LEMMA | n/a: conclusion is an equation. |
| 16 | SHOW/CHANGE | No `show`. |
| 17 | PUSH_NEG | No negation tactic. |
| 18 | GENERALISE | All three parameter drop probes performed with autoImplicit false; table below. |
| 19 | INEQUALITY | No reversed inequality; table below. |
| 20 | NORMAL-FORM | Evaluation equation reduces extension at last to appended coordinate, appropriate rewrite normal form. |
| 21 | SYNTAX-GEN | Existing equation applies directly at four callers; no alternative restatement improves them. |
| 22 | IMPORT-FANOUT | No imports added. |
| 23 | CASTS | 0 dropped / 0 cross-type / 0 load-bearing ascriptions added; removed range binder ascription with entire have. |
| 24 | INSTANCE-NAME | n/a: no instance declaration or local instance. |

Issues found: explicit non-range proof redundant after targeted whole-proof simp.
Fixed: that proof redundancy. Refactoring needed: none.

## Five actual searches

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | `Finsupp mapDomain Fin.castSucc add single Fin.last evaluated at last` | `Fin.snoc_last`, `Fin.snoc_castSucc`, `Finsupp.cons`; related function construction, no exact Finsupp expression replacement. |
| B Loogle | `Finsupp.mapDomain, Fin.last` | Empty items, no error. |
| C LeanSearch | `A finitely supported function mapped by Fin.castSucc is zero at Fin.last` | `Fin.castSucc_ne_last`, `Fin.succAbove_last`; useful range facts. |
| D source rg | `mapDomain_of_notMem_range\|castSucc_ne_last\|last_notMem_range\|range_castSucc\|mapDomain.*last` over mathlib and Roth | Generic zero-outside-range lemma in Data/Finsupp/Basic.lean:286; Fin range and non-equality lemmas in Data/Fin/SuccPred.lean. |
| E local name | `castSucc_ne_last`, `Finsupp.mapDomain_of_notMem_range` | Both actual declarations found; symbol index warming, so no absence inferred from index. |

Auxiliary variants: `range_castSucc`, `last_notMem_range`, `mapDomain.*last` included
in the untruncated source search; `Fin.range_castSucc` verified with `#check`.
Common-equivalents buckets do not match this coordinate computation.

Conclusion: partial match `Finsupp.mapDomain_of_notMem_range`; use it in terminal simp.
No exact equation replacement found. `exact?` failed on original goal; `apply?` offered
only partial graph/equality/arithmetic routes, no closing term. A live multi-attempt
replacement emitted stale nested-body parse diagnostics, so its success-looking
results were independently rechecked with standalone compiled code before editing.
An initial shell wildcard search failed before rg ran; corrected search actually ran.

The owner's explicit task exception retains this useful computational equation at its
four card-bijection rewrites. Deleting it would repeat the construction and simp hint
at those sites. No API extraction signal remains: the whole body is one clear tactic.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidate tried | Verified | Result |
|---|---|---|---|---|---|---|
| 1 | `{m : ℕ}` | index value | `Fin m`, `Fin.last m`, `Fin.castSucc` | Drop under `autoImplicit false` | yes, standalone LSP run-code | Rejected: unknown identifier `m` in dependent domain and last index. |
| 2 | `(d : Fin m →₀ ℕ)` | structure value | source Finsupp in conclusion | Drop under `autoImplicit false` | yes, standalone LSP run-code | Rejected: unknown `d.mapDomain`. |
| 3 | `(i : ℕ)` | coordinate value | singleton value and RHS | Drop under `autoImplicit false` | yes, standalone LSP run-code | Rejected: unknown identifier `i` twice. |

No proposition, typeclass, decidability, global pointwise hypothesis, strict hypothesis,
or universe variable occurs; those weakening catalogues do not apply. The dependent
`Fin` construction uses a natural size, so abstracting the size is a restatement.
General coefficient AddCommMonoid API is optional abstraction without benefit to the
four natural-coordinate callers and is closed by the owner's scope instruction.
Inversion check: construction-specific `Fin.castSucc`, `Fin.last`, and Finsupp mapping
remain the proof's mathematical content; no hidden theorem about a named concrete
witness appears after unfolding. No big-change candidate proposed.
Literature: n/a — private declaration, literature search not required.

## Line packing

Reference `#check @...` at `format.width 100` is verified in the imported-private probe
record below; original signature is byte-identical.

| Sig line | Chars | Next expression/token | Arithmetic | Action |
|---|---|---|---|---|
| 90 | 66 | `(d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i)` (58 chars) | 66 + 1 + 58 = 125 > 100 | ok |
| 91 | 85 | no next signature line | n/a | ok |

The conclusion participates in the width arithmetic. Final tactic line is 42 codepoints.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| — | signature and hypotheses | no `≥` or `>` | n/a | n/a; no `_ge_`/`_gt_` |

## All 42 golfing rules

| Rule | Status and concrete reason |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no rw/exact pair. |
| 1.4 | n/a: no simp/exact pair. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor pair. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction/push-neg chain. |
| 1.9 | n/a: no eta lambda. |
| 1.10 | Have has proof content, not term-only; removed via whole-proof simp, not blind inlining. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected have. |
| 1.14 | n/a: no sequential rw. |
| 1.15 | n/a: terminal simp already unsqueezed. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | n/a: no advantageous additional dot notation. |
| 1.18 | n/a: no avoidable trailing proof parentheses. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Tried bare grind on original goal: failed. Targeted terminal simp succeeds. |
| 2.2 | n/a: retained proof contains no grind. |
| 2.3 | Whole-proof simp removes preliminary have; no final hypothesis needs simpa. |
| 2.4 | n/a: no function-property goal. |
| 2.5 | n/a: no positivity goal. |
| 2.6 | n/a: no monotonicity inequality. |
| 2.7 | n/a: Finset mapping equality is not Nat linear arithmetic; no arithmetic tactic retained. |
| 2.8 | Tried aesop: left mapDomain zero equation unsolved. |
| 2.9 | n/a: no numeric computation/cast. |
| 2.10 | n/a: variable-dependent Finsupp equality, not finite closed computation. |
| 2.11 | n/a: no denominator or ring goal. |
| 2.12 | n/a: no ring terminal or hypothesis combination. |
| 2.13 | n/a: no symmetric case branches. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: one goal solved directly. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases substitution. |
| 3.5 | No global attribute needed: private equation used by explicit rewrites. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no maxHeartbeats option. |

## Step back

Bare simp reduces to mapDomain vanishing but cannot finish. Supplying the generic
zero-outside-range lemma lets simp also discharge the Fin range condition, so one
tactic is preferable to retaining or inlining the proof-bearing range have.
No term proof or different construction improves the existing four callers.

## Verification and gates

`/Users/ramin/.elan/bin/lake build Roth.Lattice` exited 0; module compilation 31 s,
2214 jobs. Log: `/private/tmp/roth-lattice-extend-last-build.log`.
Complete native LSP diagnostics: `partial=false`, `success=true`, `timed_out=false`,
no failed dependencies, only pre-existing copyright warning at line 1. Live goal
at final tactic has original equation before and `goals_after=[]`.

Independent standalone exact-original-type proof compiled through native run-code:
`independent_extend_last` uses only `simp [Finsupp.mapDomain_of_notMem_range]`, no
reference to target. Axioms: `[propext, Classical.choice, Quot.sound]`.
Imported-built-private check is recorded below after the final shell probe.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build above, exit 0. |
| definition_protected | pass | No def/abbrev edited. |
| theorem_statement_protected | pass | Both signature lines unchanged. |
| structure_gate | pass | One tactic; no conjunction/branch. |
| naming_gate | pass | Descriptive snake_case, no forbidden abbreviation/pattern; no rename. |
| line_packing_gate | pass | Both signature lines measured above. |
| inequality_orientation_gate | pass | Explicit zero-occurrence table above. |

Full project and LeanEval final gates belong to owner after explicit freeze.

## Result and 11 checks

Before: 6 nonblank declaration lines. After: 3. Saved: 3.
Rules applied: 2.3 (whole-proof simp); proof-content have subsumed rather than
blindly treated as a trivial term. One redundancy fixed; no deferred refactoring.
Renames-queued: none. Comments-preserved: none present.

- [x] Step 1 — reference docs read.
- [x] Step 2 — full 24-item audit.
- [x] Step 2.5 — five actual searches.
- [x] Step 2.6 — every parameter mechanically probed.
- [x] Step 2.7 — per-signature-line packing arithmetic.
- [x] Step 2.8 — explicit inequality scan table.
- [x] Step 3 — every one of 42 golfing rules given a status.
- [x] Step 4 — alternate whole-proof strategies considered and tested.
- [x] Step 5a — complete LSP success, known user-preserved header warning only.
- [x] Step 5b — actual build and all seven worker gates.
- [x] Step 6a — no rename needed, sidecar unchanged.

## Imported built-private evidence and freeze

Final standalone probe `/private/tmp/roth_extend_last_actual.lean` completed with
exit 0 (`lake env lean`); log `/private/tmp/roth-extend-last-actual.log`.
It enumerated the actual imported environment constant, used `Lean.collectAxioms`
on its actual Name, and elaborated `#check @...` through an identifier carrying
that Name, with `format.width 100`:

```text
Actual imported private: _private.Roth.Lattice.0.Roth.extend_apply_last
Type: ∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) (Fin.last m) = i
Axioms: [propext, Classical.choice, Quot.sound]
@Roth.extend_apply_last✝ : ∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ),
  (Finsupp.mapDomain Fin.castSucc d + Finsupp.single (Fin.last m) i) (Fin.last m) = i
```

An earlier probe's direct textual private-name syntax failed after successfully
printing the actual constant and axioms. The final generated-identifier probe
resolved that diagnostic and exited 0. Native run-code briefly rejected imports
as out of date after the build; live-file LSP remained complete, and the fresh
standalone imported probe supplies final evidence. No compiler probes remain running.

Owner revoked source edit ownership for final gates at full-source SHA256
`4e1844b749055743bc6aad96f85057664c5376d91e37e95ef53fa729a96de689`.
This worker's target-block-only SHA256 (no trailing newline) is
`e5ee5448ae156d43ab41bccfbafdac213fba62fb0f36f0bdc52e41f3e6b29401`.
These hashes identify different scopes. Source is frozen; subsequent edits were
report-only. Overall worker gates: pass.

Owner checkpoint: sequential full/separate LeanEval session51672 after explicit sourcefreeze, both exit0(96.32s/34.26s), hash unchanged. Logs `/private/tmp/roth-lattice-d06-{full,leaneval}.log`.
