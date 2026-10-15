# Phase 4 — `Roth.coeff_prod_of_natDegree_le'`

Dedicated single-declaration worker, baseline `c30f58c`. Original file inventory lines 106–117; dispatch lines 102–113, 12 lines. Only the target and this report are owned. Shared logs and Git belong to the file coordinator.

## Step 1 — References

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full, plus the naming guide and applicable style sections. Lean 4 and mathlib-quality skills apply. The authoritative worker contract is `/private/tmp/roth-wronskian-worker-contract.md`.

## Step 2 — Full audit (before editing)

1. **LINT:** No reported diagnostic in target; known header warning and downstream unused `hφ`/`hd` are outside ownership.
2. **HAVE SCAN:** No `have` declarations.
3. **SET_OPTION:** None; no changes to limits or diagnostics planned.
4. **SIMP SQUEEZE:** Empty branch uses terminal unsqueezed `simp`. Proposed insert-hypothesis simplification is nonterminal and uses explicit `simp only [Finset.forall_mem_insert]`.
5. **NAMING:** Snake_case mathematical coefficient/product conclusion with natural-degree upper-bound hypothesis; `natDegree` preserves the underlying API component spelling. Prime distinguishes variable bounds from mathlib's common-bound theorem. No forbidden abbreviation, number scheme, `_ge_`, or `_gt_`. A standard standalone polynomial property, not an opaque proof stage; no rename needed.
6. **LINE PACKING:** Three signature lines are measured below; no repack needed.
7. **BY PLACEMENT:** `:= by` at signature line end.
8. **FORMAT:** Two ordinary lambda arrows in the original insert case are removed by splitting its bound hypothesis. Match arrows stay `=>`; indentation remains two spaces and no blank proof lines or semicolon chains are introduced.
9. **COMMENTS:** No proof comments present; surrounding documentation untouched.
10. **DOCSTRING:** n/a: private lemma; no docstring present or required.
11. **VISIBILITY:** Private; sole current caller is the coefficient-of-Wronskian proof in this file. Preserve visibility.
12. **STRUCTURE:** Nine original tactic/body lines, longest branch five body lines; no conjunction in the statement. Proposed proof has eight body lines and a four-line insert body. No extraction required.
13. **MATHLIB:** Partial match `Polynomial.coeff_prod_of_natDegree_le` uses one shared bound; this result permits a separate `n i`. Keep the induction and reuse the verified binary coefficient identity and product degree bound. Full search below.
14. **JUNK DEF:** n/a: lemma, not definition.
15. **EXISTS LEMMA:** n/a: coefficient equality, not existential.
16. **SHOW vs CHANGE:** No `show` or `change`.
17. **PUSH_NEG:** None.
18. **GENERALISE:** Scratch-only `CommSemiring` weakening compiles. Keep the user's current API and do not broaden this private field lemma solely for hypothetical reuse; details below. Every parameter is audited.
19. **INEQUALITY:** One `≤` hypothesis, no `≥` or `>`; table below.
20. **NORMAL-FORM:** Polynomial coefficient of product at sum of degree bounds, equal to product of coefficients. Matches binary coefficient API and finite-product notation; already canonical.
21. **SYNTAX-GEN:** OK: membership-localized degree bound is exactly what the sole caller has. A global bound or bundled abstraction would make application less direct.
22. **IMPORT-FANOUT:** n/a: no new import needed.
23. **CASTS:** 0 dropped / 0 cross-type / 0 load-bearing term casts; none exist in target.
24. **INSTANCE-NAME:** n/a: no instance declaration. Local `classical` enables finite-set induction without an exported decidability assumption.

Issues to fix: simplify repeated insertion-membership plumbing by decomposing `h` once; this also eliminates both legacy lambda arrows. Refactoring needed: none. The partial match is already reused through its binary building block; no exact wrapper replacement was found.

## Step 2.5 — Five-method mathlib search

| Method | Actual query/evidence | Result |
|---|---|---|
| A Lean-Finder | “coefficient of product of polynomials at sum of bounds on their natural degrees equals product of coefficients” | Found the binary bound theorem, common-bound finite/list products, and natural-degree coefficient multiplication. |
| B Loogle | `Polynomial.coeff, Finset.prod` | Found `Polynomial.coeff_prod_of_natDegree_le`, `coeff_zero_prod`, ideal coefficient bounds, and specialized Vieta/characteristic-polynomial facts. |
| C LeanSearch | Variable-degree product coefficient problem | Unavailable: inherited confirmed HTTP 500 from coordinator. No redundant retry; this is not absence evidence. |
| D Source | Untruncated `coeff_prod`, `coeff_mul_add_eq_of_natDegree_le`, `natDegree_prod_le`, and full-name `coeff_prod_of_natDegree_le` searches; read `Algebra/Polynomial/BigOperators.lean` in full | Common-bound finite theorem at line 230; binary identity in `Degree/Operations.lean`; existing product-degree bound. No exact variable-bound replacement found. |
| E Local name pattern | Native `lean_local_search` for `coeff_prod` | Source hits confirmed common-bound theorem, power-series products, multivariate leading coefficients, and this target. Index reported unavailable; source positives are valid, no index absence claim made. |

Auxiliary variants examined: `coeff_list_prod_of_natDegree_le`, `coeff_multiset_prod_of_natDegree_le`, `coeff_zero_prod`, `natDegree_prod_le`, `natDegree_prod`, `leadingCoeff_prod`, `natDegree_add_coeff_mul`, and `coeff_mul_add_eq_of_natDegree_le`. Common-equivalents table has no matching bucket. Finset insertion predicate lemma `forall_mem_insert` was found in source before use and checked by Lean.

Actual `#check` results at `format.width := 100`:

```lean
@coeff_prod_of_natDegree_le : ∀ {R : Type u_1} {ι : Type u_2} (s : Finset ι) [inst : CommSemiring R] (f : ι → R[X])
  (n : ℕ), (∀ p ∈ s, (f p).natDegree ≤ n) → (∏ i ∈ s, f i).coeff (s.card * n) = ∏ i ∈ s, (f i).coeff n
@coeff_mul_add_eq_of_natDegree_le : ∀ {R : Type u_1} [inst : Semiring R] {df dg : ℕ} {f g : R[X]},
  f.natDegree ≤ df → g.natDegree ≤ dg → (f * g).coeff (df + dg) = f.coeff df * g.coeff dg
@natDegree_prod_le : ∀ {R : Type u_1} {ι : Type u_2} (s : Finset ι) [inst : CommSemiring R] (f : ι → R[X]),
  (∏ i ∈ s, f i).natDegree ≤ ∑ i ∈ s, (f i).natDegree
@Finset.forall_mem_insert : ∀ {α : Type u_1} [inst : DecidableEq α] (a : α) (s : Finset α) (p : α → Prop),
  (∀ x ∈ insert a s, p x) ↔ p a ∧ ∀ x ∈ s, p x
```

Native live `exact?` did not close the original goal; `apply?` offered the generic `Finsupp.apply_eq_of_mem_graph` with the entire coefficient equality still to establish as a graph-membership subgoal. It did not supply a proof. Together with the source and other searches this supports keeping the finite induction; it does not prove global absence from all of mathlib.

**Concluded:** partial match, retain target and directly use the binary coefficient identity and finite-product degree bound. The local theorem includes the induction necessary to pass from two factors to nonuniform finite bounds; it is not a 1–3-call wrapper. No additional API extraction is warranted. Six strict rules checked: no wrapper added, all five methods recorded, auxiliary variants inspected, no custom typeclass predicate, no exact equivalent requiring deletion found, and no new direct dependency requiring module-documentation change.

## Step 2.6 — Mechanical generalisation

| Parameter | Class | Use | Candidate/drop test | Verified? | Disposition |
|---|---|---|---|---|---|
| `{K : Type*}` | type variable | Coefficient type in `K[X]` and both sides | Drop invalidates all polynomial types; already universe polymorphic | Direct dependency inspection | Retain; no smaller hypothesis to remove. |
| `[Field K]` | typeclass | Polynomial semiring structure and commutative finite products | Drop; `DivisionRing`; `Semiring`; `CommSemiring`; stronger `CommRing` is subsumed by successful semiring case | Actual native scratch elaboration: first three fail; full `CommSemiring` proof compiles | Dropped class fails `Semiring K`; `DivisionRing`/`Semiring` fail `CommMonoid K[X]`. `CommSemiring` works but is left scratch-only under the current-API instruction. |
| `{ι : Type*}` | type variable | Index type of `s`, `f`, and `n` | Drop invalidates their types; universe already arbitrary | Direct dependency inspection | Retain. No constraint tying its universe to `K`. |
| `(s : Finset ι)` | structure value | Product/sum domain, induction subject, domain of bound | Drop removes the domain of every finite operator; replacing by global Fintype is a distinct interface | Direct dependency inspection | Retain arbitrary finite subset. |
| `(f : ι → K[X])` | structure value | Polynomials on both sides and in bound | Drop leaves the mathematical object unbound | Direct dependency inspection | Retain; no special family assumed. |
| `(n : ι → ℕ)` | structure value | Per-factor coefficient index and total index | Drop leaves coefficient indices unbound; a constant replaces variable bounds by a specialization | Direct dependency inspection | Retain arbitrary per-factor bounds. |
| `(h : ∀ i ∈ s, (f i).natDegree ≤ n i)` | proposition | Bound for inserted factor and remaining product | Remove with `clear h` and replay induction; point localization/strict-to-weak | Native scratch fails `Unknown identifier h` at insert simplification | Retain; already weak `≤` and restricted exactly to `s`. No unused conjunct. |
| Local `classical` | decidability | Finset insertion induction and membership simp | No exported `DecidableEq` binder to drop | Signature check | Retain local classical scope rather than add an interface assumption. |

The complete eight-line proof was checked over `[CommSemiring K]` through `lean_run_code` (`success: true`, not timed out) and `lake env lean /private/tmp/roth-wr-coeff-test.lean` (exit 0). This is a verified optional widening, not an applied change. The sole caller is over a field and gains nothing from widening; the user chose to keep the current API. It is closed as an optional no-caller-need change, not a pending refactoring task. No change to argument order, explicitness, visibility, normal-form attributes, or universes.

Inversion check: not applicable to a special named witness; the statement already has an arbitrary polynomial family and arbitrary finite set, and the proof continues to use polynomial degree/coefficient facts. Restatement over a generic graded algebra would change the object/interface and is not warranted by this caller.

Literature search: n/a, private declaration; the contract explicitly excludes private/auxiliary lemmas from public literature search. No ChatGPT math MCP query required.

## Step 2.7 — Required signature width table

Original and final signature are byte-for-byte identical. Actual original-type `#check` from the final isolated source, with `format.width := 100`:

```lean
@coeff_prod_of_natDegree_le' : ∀ {K : Type u_2} [inst : Field K] {ι : Type u_3} (s : Finset ι) (f : ι → K[X])
  (n : ι → ℕ), (∀ i ∈ s, (f i).natDegree ≤ n i) → (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)
```

Both initial and final measurements (Unicode codepoints, not bytes):

| Signature line | Chars | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 102 | 95 | `(h : ∀ i ∈ s, (f i).natDegree ≤ n i)` (36) | 95 + 1 + 36 = 132 > 100 | ok |
| 103 | 42 | Complete conclusion and `:= by` (70) | 42 + 1 + 70 = 113 > 100 | ok |
| 104 | 74 | No next signature line | n/a, proof next | ok |

No repack rows. Maximum final proof line is 99 codepoints (line 111).

## Step 2.8 — Required inequality occurrence scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | L103 hypothesis `h` | `(f i).natDegree ≤ n i` | None: correct smaller-side-left orientation | None |
| — | Entire signature and typed hypotheses | No `≥` or `>` | n/a | No `_ge_`/`_gt_` in name |

Post-edit scan agrees; no inequality orientation change was needed.

## Step 3 — All 42 golfing rules

Phase 1, instant wins:

- [1.1] `by exact`: n/a, original proof contains finite induction.
- [1.2] `by rfl`: n/a, no reflexivity wrapper.
- [1.3] `rw + exact`: n/a, terminal rewrite already closes insert case.
- [1.4] `simp + exact`: n/a, no such adjacent pair.
- [1.5] Trailing `rfl`: n/a, none.
- [1.6] Constructor terms: n/a, target is an equality, no constructor tactic.
- [1.7] `apply + exact`: n/a, none.
- [1.8] Contradiction plus negation pushing: n/a, none.
- [1.9] Eta lambdas: original membership lambdas are not eta reductions; the final proof eliminates both through `h.2`.
- [1.10] Single-use `have`: n/a, none.
- [1.11] `apply + intro`: n/a, none.
- [1.12] Redundant `show`: n/a, none.
- [1.13] `have` projections: n/a, no `have`; projections `h.1` and `h.2` now reuse the decomposed existing hypothesis.
- [1.14] Consecutive rewrites: already one merged terminal `rw` list.
- [1.15] Unsqueeze terminal simp: empty case already bare `simp`; retain.
- [1.16] Squeeze nonterminal simp: applied to new insert simplification as explicit `simp only [Finset.forall_mem_insert] at h`.
- [1.17] Dot notation: retained `(natDegree_prod_le _ _).trans`; no remaining verbose eligible function application.
- [1.18] `<|` over parentheses: n/a, inner `.trans (...)` argument is followed by surrounding list syntax; `<|` adds no clarity/saving. No `$`.
- [1.19] `push_neg`: n/a, none.
- [1.20] Single-use existential: n/a, not an existential lemma.

Phase 2, automation:

- [2.1] Whole-proof `grind`: tried on the live original proof position; failed with negated coefficient equality and no contradiction.
- [2.2] Delete before grind: n/a, no successful grind step.
- [2.3] Simpa consolidation: whole-proof `simp` was tried and made no progress; there is no simp/exact chain to merge. The successful new simplification only decomposes the insertion hypothesis.
- [2.4] `fun_prop`: n/a, no continuity/differentiability/measurability property.
- [2.5] `positivity`: n/a, target is a coefficient equality; no positivity/nonzero subgoal.
- [2.6] `gcongr`: actually compiled a separate sum-bound proof `gcongr with i hi; exact h i hi` (on separate tactic lines). It works but replaces the existing direct term `Finset.sum_le_sum h.2` by a longer tactic block; retain the direct term.
- [2.7] `lia`/`omega`: n/a, no bare arithmetic subgoal; the only inequality composition is already a direct library application.
- [2.8] Whole-proof `aesop`: tried live, failed and made no progress.
- [2.9] `norm_num`/`norm_cast`: n/a, no concrete computation or cross-type casts.
- [2.10] `decide`: n/a, universal equality over arbitrary field/polynomial data, not closed finite computation.
- [2.11] `field_simp; ring`: n/a, no denominators or ring-normalization goal.
- [2.12] `linear_combination`: n/a, proof does not end in `ring`/`ring_nf` and has no polynomial identity hypotheses to combine.
- [2.13] `wlog`: n/a, empty/insert branches are structurally different, not symmetric cases.
- [2.14] Collapse `calc`: n/a, no calc; inequality chain already uses `.trans`.
- [2.15] `<;>`: n/a, empty and insertion cases need distinct proofs; no repeated sibling closing tactic.

Phase 3, cleanup:

- [3.1] `erw` to `rw`: n/a, only `rw` present.
- [3.2] Legacy function tactics: n/a, none.
- [3.3] `omega` to `lia`: n/a, no arithmetic tactic in final proof.
- [3.4] `rcases ... rfl`: n/a, none.
- [3.5] Automation attributes: no new attribute; this private conditional coefficient lemma is not an unconditional simp rule and no repeated automation caller needs it.
- [3.6] `simp_all`: n/a, no `simp_all only`; whole-proof simp failed and induction still supplies the mathematical step.
- [3.7] Limits: no `maxHeartbeats`, recursion, or other per-declaration option.

## Step 4 — Step back and actual experiments

The mathematical content is induction over a finite product: empty product is immediate, then the coefficient at the sum of upper degree bounds multiplies by the inserted factor's coefficient. The remaining product is bounded using `natDegree_prod_le` and `Finset.sum_le_sum`. No alternative leading-coefficient strategy is shorter when some bounds can strictly exceed actual degrees.

Actual comparisons: native live `grind`, `simp`, `aesop`, `exact?`, `apply?`; all failed to prove the entire statement. `apply?` merely proposed a graph-membership restatement. The decomposed-hypothesis induction was compiled over CommSemiring, then applied at the unchanged Field signature. The isolated `gcongr` sum estimate compiles but is longer than the direct term. Term-mode Finset induction would still carry the same degree estimate and membership split and provides no simplification. No opaque arithmetic automation, new helper, or wrapper was introduced.

The initial native multi-attempt call returned slowly; one bounded helper fallback had already started before the native result arrived. Its result added no candidate and no further duplicate automation was run. The helper's cleanup warning about a closed Python event loop was after a successful `lean_run_code` result and was not a Lean error. The first scratch snippet had a long signature/leading-space style warning; the final exact-source isolated run below has only informational `#check`/axiom output. No scratch warnings, failed tests, or instrumentation are in the repository source.

## Step 5 — Verification and diff gates

- `/Users/ramin/.elan/bin/lake build Roth.Wronskian`: exit 0, 1826 jobs; module build 8.7 seconds. Log `/private/tmp/roth-wr-coeff-build.log`.
- Complete native `lean_diagnostic_messages`, timeout 30 seconds: `success: true`, `partial: false`, `timed_out: false`, failed dependencies empty. Only existing header warning (L1) and downstream unused `hφ`/`hd` (L129/130). No target warning or error.
- Exact final target copied from source into native `lean_run_code` with only `Mathlib.Algebra.Polynomial.BigOperators`, original Field context, `#check`, `#print axioms`, and an `example` demanding the original type: `success: true`, `timed_out: false`, only informational output.
- Axioms: `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`, custom axioms, or unchecked proof route.
- Mechanical comparison against saved pre-worker target `/private/tmp/roth-wr-coeff-before.txt`: signature byte-identical; only target insert proof changed; 12→11 declaration lines and 9→8 proof-body lines. No definition/import/documentation/other-declaration edits.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual `lake build Roth.Wronskian`, exit 0. |
| definition_protected | ✓ pass | No def/abbrev/import changes. |
| theorem_statement_protected | ✓ pass | Entire signature byte-identical. |
| structure_gate | ✓ pass | Eight proof-body lines, four-line insertion body, no statement conjunction. |
| naming_gate | ✓ pass | Descriptive standard-property name; no forbidden pattern/abbreviation; no rename. |
| line_packing_gate | ✓ pass | Three measured rows, all `ok`; maximum proof width 99. |
| inequality_orientation_gate | ✓ pass | Per-occurrence table; zero reversed inequalities. |
| isolated proof/type/axioms | ✓ pass | Exact final source elaborated at original type; standard axioms only. |

Overall: pass. Dependent full-project and `Roth.LeanEval` builds belong to coordinator and are not claimed by this worker.

## Step 6 — Result

Before: 12 declaration lines / 9 proof-body lines. After: 11 / 8. Saved: 1 line; eliminated two repeated membership lambdas and their legacy arrows. Two related audit issues fixed by the same change (membership plumbing and lambda style). Rules applied: 1.16, retained 1.14/1.17; direct hypothesis decomposition is the substantive golf. Refactoring needed: none. Renames queued: none. Comments preserved: none present in target; surrounding docs unchanged.

Phase checklist:

- [✓] Step 1 — Required reference documents read.
- [✓] Step 2 — All 24 audit items answered.
- [✓] Step 2.5 — Five search methods, limitations, auxiliary searches, and compiled probes recorded.
- [✓] Step 2.6 — Every hypothesis audited; actual class/drop experiments; private literature exemption; optional widening closed under current-API instruction.
- [✓] Step 2.7 — Complete initial/final signature width table.
- [✓] Step 2.8 — Inequality occurrence table and final scan.
- [✓] Step 3 — All 42 rules given applicable result or concrete n/a reason.
- [✓] Step 4 — Whole-proof search, alternative strategy, and direct-term comparison complete.
- [✓] Step 5a — Complete LSP diagnostics clean of errors; known outside-target warnings recorded.
- [✓] Step 5b — Actual module build, diff gates, isolated original-type proof, and axioms pass.
- [✓] Step 6a — No rename to append; source/report released to coordinator.
