# det_hasseDeriv_separated cleanup

## Initial audit before source edits

Read lean4/SKILL.md, mathlib-quality/SKILL.md, full golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, relevant style/naming/profiling and installed cleanup Phase 4. Scope is only this original declaration and this report. No subdelegation. Baseline HEAD dd24a21 supplied clean.

1. LINT: initial clean repository supplied by parent; native full diagnostics queued before source edits.
2. HAVE SCAN: hA and hB each prove transport of a determinant; eliminate both using AlgHom.map_det directly.
3. SET_OPTION: none.
4. SIMP SQUEEZE: no simp calls in original.
5. NAMING: det_hasseDeriv_separated names determinant, operator and separated form; no forbidden abbreviation/pattern; no rename warranted.
6. LINE PACKING: signature table below; repack first two lines and expression boundaries within 100 codepoints.
7. BY PLACEMENT: original by at signature end.
8. FORMAT: replace mathematical lambdas => by ↦; retain one tactic per line.
9. COMMENTS: no inline proof comments; preserve original docstring verbatim.
10. DOCSTRING: public theorem documented with source and matrix product explanation; user-protected.
11. VISIBILITY: public named module main result; retain.
12. STRUCTURE: original body 19 physical tactic lines after := by, 20 including := by; headline needs at most 15 including := by. Prefer direct determinant map/mul/transpose API, no helper anticipated.
13. MATHLIB: actual Finder returns two-polynomial Wronskians, distinct from project finite-family Hasse definition; Loogle finds det_mul; LeanSearch finds RingHom.map_det; source finds AlgHom.map_det; local name search returns map_det source hits with index unavailable (not absence).
14. JUNK DEF: n/a theorem.
15. EXISTS LEMMA: n/a no existential.
16. SHOW vs CHANGE: no show.
17. PUSH_NEG: none.
18. GENERALISE: approved drop both Fintype τ and DecidableEq τ using scoped omit; inspect every binder below. Field weakening obstructed by Field-bound Wronskian definitions; compile probe pending.
19. INEQUALITY: no inequality occurrences in statement, hypotheses or proof.
20. NORMAL-FORM: matrix-product determinant with transpose is canonical; keep separated-sum application form.
21. SYNTAX-GEN: OK existing form rewrites caller directly; arbitrary matrix abstraction already det_mul.
22. IMPORT-FANOUT: no import change required.
23. CASTS: ν : ℕ genuine Fin→Nat bridge; X none ascription pins polynomial variable/coefficient ring. Inspect proof ascriptions after rewrite.
24. INSTANCE-NAME: n/a no instance declarations.

## Initial binder audit

| Binder | Assessment / concrete probe |
|---|---|
| τ : Type* | already arbitrary universe; retain variable type |
| Fintype τ | approved omit, compile arbitrary-τ proof |
| DecidableEq τ | approved omit, classical only if required |
| K : Type* | already arbitrary universe |
| Field K | genWronskian/wronskian require Field; CommRing probe pending, do not silently widen dependencies |
| l : ℕ | finite square derivative order; no positivity required (l=0 allowed) |
| D | arbitrary multi-index family; cannot drop data appearing in conclusion |
| φ | arbitrary polynomial family, no independence imposed |
| ψ | arbitrary multivariate family, no independence imposed |

## Initial signature width table

| Line | Codepoints | Next line fragment | Combined | Action |
|---|---:|---|---:|---|
| 344 | 90 | `(ψ` | 93 | inspect natural expression/binder unit |
| 345 | 36 | `(Matrix.of` | 47 | inspect natural expression/binder unit |
| 346 | 97 | `(∑` | 100 | inspect natural expression/binder unit |
| 347 | 75 | `rename` | 82 | inspect natural expression/binder unit |
| 348 | 35 | `rename` | 42 | inspect natural expression/binder unit |
| 349 | 38 | `Polynomial.aeval` | 55 | inspect natural expression/binder unit |
| 350 | 76 | `:= by` | 82 | inspect natural expression/binder unit |

Inequality table: zero occurrences (`≤`, `<`, `≥`, `>`); arrows are function syntax.

Literature: actual web search "Takloo-Bighash Yin Formalizing Roth theorem determinant Lemma 2 separated Wronskian" performed; exact manuscript not indexed. Source .mathlib-quality/references/clean.tex is the controlling primary manuscript, to inspect. Search also found generalized-Wronskian separation discussion at https://mathoverflow.net/questions/436759/english-translation-of-a-multidimensional-generalization-of-the-wronskian ; used only as discovery, not primary theorem evidence.

Planned actions: remove hA/hB transport boilerplate using AlgHom.map_det, identify product with transpose entrywise, approved scoped omit, mathematical lambda style. No public meaning/doc changes.

## Search and mathematical review

All five actual methods were called natively: A Lean Finder (three distinct two-polynomial Wronskian results); B Loogle `Matrix.det (_ * _)` (det_mul and commutation variants); C LeanSearch “ring homomorphism maps matrix determinant” (RingHom.map_det); D untruncated source rg for map_det/det_mul/det_transpose in Determinant/Basic.lean (AlgHom.map_det at 326, det_mul at 138, det_transpose at 203); E local `map_det` (five source hits; index explicitly unavailable). Remote methods succeeded; local index unavailability is not absence. No new helper is asserted absent from mathlib. Native live-file exact? timed out at the default 200000 heartbeats, grind failed, simp left the product identity, aesop did not complete. The multi-attempt line replacement also produced residual original multiline-have parser diagnostics; those are not claimed to invalidate or validate a whole-declaration replacement. Independently compiled direct proof establishes the chosen route. Full mathematical identity remains specialized to project Hasse Wronskians; determinant functoriality uses Mathlib directly.

Primary local manuscript `.mathlib-quality/references/clean.tex:405–418` explicitly identifies A_(μρ)=Δ_μψ_ρ and B_(νρ)=Δ_νφ_ρ and proves the differentiated sum matrix is A Bᵀ. The proof follows exactly this argument: map the two determinants into the common polynomial ring, reverse determinant multiplicativity and transpose invariance, then compare entries using Hasse separation. Actual public literature web search was performed; the exact manuscript was not returned by the public index. No secondary search result is used as proof evidence.

Six replacement rules: (1) no new wrapper; (2) all methods actually attempted, no unsupported absence claim; (3) AlgHom.map_det found by auxiliary route; (4) existing typeclasses retained except approved unused τ removals; (5) hA/hB local boilerplate deleted rather than wrapped; (6) usage documented here because original module docstring is user-protected.

## Final generalisation review

The independent proof has arbitrary `τ : Type*`, arbitrary `K : Type* [Field K]`, arbitrary l including zero, and unrestricted D, φ, ψ. It invokes no target theorem. Both τ classes are absent and no classical tactic is required. All data binders occur in the proposition and cannot simply be dropped; changing finite derivative order l to an abstract index would require a new order map and changes the public statement rather than deleting an assumption. No independence, nonzero, characteristic, degree, positivity or finiteness hypothesis is introduced. The type universes remain arbitrary. There are no global-to-local or strict-to-weak hypotheses.

Actual CommRing coefficient probe `/private/tmp/roth-s22-commring.lean` fails at `wronskian φ` because that existing public definition is Field-bound; `/private/tmp/roth-s22-commring.log` records the precise elaboration error. This is an existing API dependency, not mathematical impossibility: the determinant identity itself extends to commutative rings. Widening upstream Wronskian definitions is outside this declaration's ownership and not approved. No new public proposal is silently applied. Inversion check: after unfolding, the remaining content is determinant multiplicativity, which is already the general Mathlib `Matrix.det_mul`; no fresh abstract helper or public restatement is warranted.

## All 42 golfing rules

- 1.1: n/a no by-exact wrapper.
- 1.2: n/a no by-rfl declaration.
- 1.3: n/a no rw followed by exact.
- 1.4: n/a no simp/exact chain.
- 1.5: n/a no simp/rfl chain.
- 1.6: n/a no constructor.
- 1.7: n/a no apply/exact pair.
- 1.8: n/a no contradiction.
- 1.9: n/a all mathematical lambda variables are used nontrivially.
- 1.10: applied remove both single-use hA/hB proof blocks via direct AlgHom.map_det.
- 1.11: applied refinements take Matrix.ext/Finset.sum_congr lambdas directly.
- 1.12: n/a no show.
- 1.13: n/a no projections.
- 1.14: applied determinant rewrites consolidated in one rw.
- 1.15: n/a no terminal simp-only.
- 1.16: n/a no nonterminal simp.
- 1.17: applied use AlgHom.mapMatrix to express transported B.
- 1.18: n/a no trailing proof parentheses.
- 1.19: n/a no push_neg.
- 1.20: n/a no existential helper.
- 2.1: tried live grind; fails product identity.
- 2.2: n/a final proof contains no grind.
- 2.3: tried live simp with determinant definitions; leaves nontrivial matrix identity.
- 2.4: n/a algebraic equality, no function property.
- 2.5: n/a no positivity goal.
- 2.6: n/a no inequality.
- 2.7: n/a no arithmetic proposition.
- 2.8: tried live aesop; does not close the identity.
- 2.9: n/a no numeric or cast normalization proposition.
- 2.10: n/a arbitrary polynomial identity, no finite closed computation.
- 2.11: n/a no denominators.
- 2.12: n/a no ring/ring_nf terminator or algebraic hypotheses.
- 2.13: n/a no symmetric branches.
- 2.14: n/a no calc chain.
- 2.15: n/a no multiple similar goals.
- 3.1: n/a no erw; direct rw succeeds.
- 3.2: n/a no continuity/measurability.
- 3.3: n/a no omega or integer arithmetic.
- 3.4: n/a no rcases.
- 3.5: no attribute: specialized determinant factorization is not a normalizing simp rule.
- 3.6: n/a no simp_all.
- 3.7: pass no limits or scaffolding introduced.

## Step-back review and simplify pass

The mathematical proof now reads directly as the determinant argument. Two coercion/transport local have blocks were unnecessary; direct AlgHom.map_det eliminates nine proof lines with fewer explicit large matrices. Final Matrix.ext deliberately avoids generic `ext` descending into polynomial coefficients (the isolated generic-ext experiment failed with a stuck AddCommMonoid metavariable). No mathematically meaningful helper is needed. The final rfl identifies mapped matrix entries definitionally after the Hasse separation rewrite. No unrelated source changes, header modifications, deleted comments, tests mirroring implementation, or new imports.

Casts: one surviving proof X-none target ascription is load-bearing to resolve the variable and coefficient rings; ν : ℕ is a genuine Fin→Nat coercion in the statement; the earlier transport matrix ascriptions disappeared with hA/hB. No additional classical choice is introduced in the proof script, though standard polynomial/determinant library proofs use choice.

## Signature and inequality artifacts

Widths use Unicode codepoints, not bytes; the next unit is a complete binder or mathematical application, avoiding splitting those units internally. Pretty-printer reference uses `set_option format.width 100 in #check @det_hasseDeriv_separated` in the independent probe (raw output saved).

| Final signature line | Width | Next complete binder/expression unit width | Combined | Result |
|---|---:|---:|---:|---|
| 345 | 90 | 32 | 123 | overflow; natural unit boundary |
| 346 | 36 | 92 | 129 | overflow; natural unit boundary |
| 347 | 96 | 67 | 164 | overflow; natural unit boundary |
| 348 | 75 | 58 | 134 | overflow; natural unit boundary |
| 349 | 68 | 73 | 142 | overflow; natural unit boundary |
| 350 | 79 | none | terminal | terminal |

| Inequality occurrence | Location | Orientation | Action |
|---|---|---|---|
| none | whole signature and proof | no inequality | pass |

## Validation and gates

Initial module native LSP was complete and showed four target unused-instance warnings plus pre-existing header/later-theorem warnings; the final complete unfiltered native result is `/private/tmp/roth-s22-native-lsp.json`: success true, partial false, timed_out false, no failed dependencies, 0 errors / 6 warnings / 0 infos / 0 hints. There are no target warnings. No warnings suppressed.

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, log `/private/tmp/roth-s22-build.log` (1876 jobs). Exact arbitrary-τ independent proof and original full-instance adapter live in `/private/tmp/roth-s22-independent.lean`, with output `/private/tmp/roth-s22-independent.log`; final result and timing are appended below. Actual built target and internal caller `exists_det_eq_mul` are checked for axioms in that file. `rg` across all repository Lean sources found no external direct caller of this declaration; its only use is inside exists_det_eq_mul in the same actually-built and fully-LSP-checked module. External importers Roth.lean and Roth/Theta.lean do not directly call this target; cumulative full-project verification belongs to parent.

No new helpers; no pending rename; no source definition edits; docstring byte-preserved. Statement formula preserved modulo approved omission and mathematical lambda notation. All desired protection, naming, structure, inequality, no-scaffolding, no-sorry gates pass. Shared-log/Git edits are reserved to parent.

## Final measured result and freeze

Independent compilation exit 0. Exact original adapter print confirms binder order `τ`, `Fintype τ`, `DecidableEq τ`, `K`, `Field K`, `l`, `D`, `φ`, `ψ`; an explicit full-instance Unit/ℚ application also checks. Original adapter warning is expected because the deliberately preserved original classes are unused. Independent proof, adapter, actual target, and actual internal caller all report exactly `[propext, Classical.choice, Quot.sound]`; none has sorryAx or a new axiom.

All earlier compiler/MCP requests drained before actual final profile. Final command `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean` exited 0; raw `/private/tmp/roth-s22-final-profile.log`, parsed `/private/tmp/roth-s22-final-profile.log.json`, parser `/private/tmp/roth-separation-profile-table.py`. Repository target anchors: command 56.067ms (two nested command anchors due scoped omit; max outer used), proof 382.136ms (one actual Roth.det_hasseDeriv_separated proof anchor), conservative sum 438.203ms. Supplied baseline actual target: 47.310 + 372.720 = 420.030ms. Difference is +18.173ms, within ordinary run noise; no performance improvement claimed. Internal caller final 132.609 + 377.792 = 510.401ms. Both below 750ms repeat threshold and 1000ms budget; no second sweep or slow-proof diagnosis required. Nested profiler children are not added. Profiling scaffolding remains outside source.

Source arithmetic: 597→588 file lines (−9); target declaration 26→16 physical lines (−10); target body including `:= by` 20→11 (−9); scoped omit adds one line. Actual Git numstat is +8/−17, net −9. No helper added. Original target docstring preserved verbatim. Only this target declaration and its omit are changed in source.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual Roth.Separation exit 0 |
| definition_protected | pass | no definition modified |
| theorem_statement_protected | pass | only approved τ class omissions and notation/line breaks |
| structure_gate | pass | headline body 11≤15, no conjunction or long branches |
| naming_gate | pass | mathematical det/operator/separated description; no forbidden pattern |
| line_packing_gate | pass | all signature natural binder/expression unit rows overflow; max 96 codepoints |
| inequality_orientation_gate | pass | zero inequalities |
| cumulative_no_unintended_breakage | pass for owned scope | internal caller actual module build/LSP/axioms; no external direct target caller |
| no_sorry/no_limits/no_scaffolding | pass | source diff contains only direct proof and approved omit |

All eleven completion steps:
1. Step 1 — references read.
2. Step 2 — all 24 initial audit items written before source edits.
3. Step 2.5 — all five actual search methods and strict replacement rules recorded.
4. Step 2.6 — every effective binder reviewed; approved omissions compiled; Field-bound CommRing failure recorded.
5. Step 2.7 — full signature codepoint width table plus format.width 100 probe recorded.
6. Step 2.8 — complete empty inequality occurrence table.
7. Step 3 — all 42 golf rules have concrete statuses.
8. Step 4 — holistic step-back/simplify reasoning recorded.
9. Step 5a — complete unfiltered native LSP clean of errors, 6 preserved unrelated warnings.
10. Step 5b — diff gates and actual build/compatibility/axioms/profile evidence recorded.
11. Step 6a — no renames warranted, no shared queue mutation.

No concrete pending public proposal: mathematically plausible coefficient-ring widening would require broader upstream public-definition changes, not authorized here. Parent handles cumulative original30/public20/allactual checks, sequential full project/separate LeanEval builds, commit/push before next original declaration.

Frozen source SHA256: `4784c8e32e2e6662d5283fed9aebd68d72b4ce7ba0054b65b11d7a210e595449`. All Lean/MCP/compiler/profile requests are complete. ALL source ownership is revoked; worker is report-only, with no source edits after this freeze.

## Owner cumulative publication gates

Source FROZEN SHA256 `4784c8e32e2e6662d5283fed9aebd68d72b4ce7ba0054b65b11d7a210e595449`; leaf ownership revoked and requests drained before owner gates. Owner probe `99849` exit0,40.15s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL26 actual retained standardaxiom checks. `/private/tmp/roth-separation-d22-compatibility.{lean,log,json}`. Owner build session `46326` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,121.58s/28.20s; source hash stable. `/private/tmp/roth-separation-d22-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
