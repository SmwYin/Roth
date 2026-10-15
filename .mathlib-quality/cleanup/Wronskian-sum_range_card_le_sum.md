# Phase 4 — `Roth.sum_range_card_le_sum`

Dedicated declaration worker; baseline `a6ab470`; original dispatch lines 91–101 (11 lines), final lines 91–100 (10 lines). Only this declaration and this report were edited. Source frozen after module/LSP validation. Shared reports, imports, other declarations, and Git publication belong to the file worker.

## Step 1 — References

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full. Also read the Lean 4 skill and relevant style/naming sections. This report follows the supplied `/private/tmp/roth-wronskian-worker-contract.md` Phase-4 contract. The final-source rules take priority over stale illustrative examples (in particular, `lia`, lambda `↦`, and preservation of comments).

## Step 2 — Full audit

1. **LINT:** No diagnostic in the target. Complete file diagnostics have the known header warning and unused `hφ`/`hd` at final lines 130/131, outside ownership. No warning suppressed.
2. **HAVE SCAN:** Original L96 `has : a ∉ s := fun h => lt_irrefl a (ha a h)` has no `by`, but is used **twice**, in `card_insert_of_notMem has` and `sum_insert has`, both at original L100: retain. Original L97 `hcard : s.card ≤ a := by ...` has proof content, used by terminal `lia`: retain. No single-use proof-term `have` exists, contrary to the preliminary punch-list suspicion.
3. **SET_OPTION:** None in the declaration; no limit or diagnostic options added.
4. **SIMP SQUEEZE:** Empty branch `simp` is terminal; retain unsqueezed. The `simpa` proving `hcard` is terminal; retain unsqueezed. No nonterminal bare simp or squeezed terminal simp.
5. **NAMING:** `sum_range_card_le_sum` describes the two sides of the mathematical inequality and uses snake_case. No forbidden abbreviation, numeric scheme, `_ge_`, `_gt_`, or single-letter public name. This is a standard standalone finite-set property rather than an opaque technical step, so a descriptive standard-property name is appropriate. No rename queued; the potential mathlib replacement is a deletion, handled in Phase 5a.
6. **LINE PACKING:** Joined both signature lines into exactly 100 codepoints; arithmetic table below.
7. **BY PLACEMENT:** `:= by` remains at the signature line end.
8. **FORMAT:** Two-space proof indentation, match arrows retained, both mathematical lambdas changed to `↦`. No empty proof lines, semicolon chains, `haveI`, or `letI`. Replaced the subset term ascription by the explicit `(t := Finset.range a)` argument to `card_le_card`.
9. **COMMENTS:** None in this declaration; surrounding module and theorem documentation untouched.
10. **DOCSTRING:** n/a: private declaration, no docstring required or present.
11. **VISIBILITY:** Already private and used once in the same file, in `sum_range_le_sum_of_injective`; retained private pending the concrete mathlib deletion proposal.
12. **STRUCTURE:** Nine proof-body lines excluding the signature; longest induction branch six body lines. No conjunction in statement and no branch above ten lines. No decomposition needed.
13. **MATHLIB:** Found more general integer theorem `Finset.sum_range_le_sum`; a Nat specialization compiles. Queue deletion of this helper and use that specialization at its sole caller in Phase 5a. Do not retain a new wrapper around mathlib.
14. **JUNK DEF:** n/a: lemma, not definition.
15. **EXISTS LEMMA:** n/a: inequality, not existential witness helper.
16. **SHOW vs CHANGE:** No `show` or `change` in selected source. The isolated replacement uses a legitimate term-mode `show` to expose whole-sum Nat-to-Int casts.
17. **PUSH_NEG:** None.
18. **GENERALISE:** Only actual parameter is `S : Finset ℕ`; no explicit proposition/class hypotheses. The ambient field and size parameters are absent from the elaborated type. Generalisation table below. Mathlib already supplies the meaningful integer/lower-bound extension.
19. **INEQUALITY:** All comparisons have the smaller side on the left; table below. No reversed inequality names.
20. **NORMAL-FORM:** Standard finite sums and cardinality, already in canonical Nat lower-bound form. An arithmetic-progression closed form would introduce subtraction/division unnecessarily for the caller.
21. **SYNTAX-GEN:** Current argument shape is directly applicable to the finite image at its caller. Integer mathlib specialization is the concrete reuse action; no new API requested.
22. **IMPORT-FANOUT:** No imports changed in Phase 4. Proposed Phase-5a replacement requires `Mathlib.Algebra.Order.Group.Int.Sum`; direct project importers are `Roth/GenWronskian.lean` and `Roth.lean`. This is a small order/big-operator fact supporting the existing sum theorem; Phase 5a must validate downstream builds after adding it.
23. **CASTS:** 1 explicit subset type ascription dropped, 0 cross-type casts and 0 type ascriptions retained in the source diff; target finset is now supplied by a named argument. Candidate replacement casts are genuine Nat-to-Int casts and are not part of this edit.
24. **INSTANCE-NAME:** n/a: no instance declaration or local instance introduced.

Issues fixed: (1) underpacked signature, (2) two mathematical lambda arrows, (3) avoidable subset term ascription. `has` was not an issue after checking both uses. Refactoring needed: one concrete mathlib replacement, specified below.

## Step 2.5 — Mathlib search status

| Method | Query/evidence | Result |
|---|---|---|
| A Lean-Finder | “sum of the first card S natural numbers is at most sum of elements of finite set S” | `Finset.sum_range_le_sum`, `sum_le_sum_range`, and generic cardinality/sum bounds. |
| B Loogle | `Finset.sum, Finset.card, Finset.range, LE.le` | Found both integer range bounds, plus unrelated LYM/index facts. |
| C LeanSearch | Same finite-set sum lower-bound problem | Unavailable: file coordinator reports the already-confirmed LeanSearch HTTP 500; no redundant retry. This is not evidence of absence. |
| D Source | Untruncated searches for `sum_range.*(card|sum)`, `sum.*card.*sum`, and full candidate `sum_range_le_sum`; read `Mathlib/Algebra/Order/Group/Int/Sum.lean` in full | Exact integer lower bound at line 72 and interval variant `sum_Ico_le_sum`. |
| E Name pattern | Native local searches `sum_range` and `card_le` | Source hits confirmed the candidate. Index reported unavailable/warming, so empty index claims are not used. Native `#check` subsequently confirmed candidate types. |

Auxiliary variants examined: `sum_Ico_le_sum`, `sum_le_sum_Ioc`, `sum_le_sum_range`, `card_le_card`, `card_le_card_of_injOn`, generic sum subset/injection bounds from `apply?`, and cardinality-vs-maximum searches. Common-equivalents table has no matching bucket.

`exact?` on the current Nat goal did not close it. `apply?` offered partial sum-subset/injection and order facts, with unproved side conditions; it did not find a complete proof. No absence claim is made: the integer theorem is present and the specialization below is verified.

Native `#check` confirmed:

```lean
Finset.sum_range_le_sum {s : Finset ℤ} {c : ℤ} (hs : ∀ x ∈ s, c ≤ x) :
  ∑ n ∈ Finset.range s.card, (c + ↑n) ≤ ∑ x ∈ s, x
Nat.castEmbedding : ℕ ↪ R
Finset.card_map (f : α ↪ β) : (Finset.map f s).card = s.card
Finset.sum_map (s : Finset ι) (e : ι ↪ κ) (f : κ → M) :
  ∑ x ∈ Finset.map e s, f x = ∑ x ∈ s, f (e x)
```

**Concluded:** found a more general mathlib result. **Phase-5a action:** delete private `sum_range_card_le_sum`, add the appropriate import, and replace its sole call in `sum_range_le_sum_of_injective` with the following compiled Nat specialization. The private declaration is retained during this single-declaration pass because imports and the caller lie outside worker ownership.

```lean
import Mathlib.Algebra.Order.Group.Int.Sum
example (S : Finset ℕ) : ∑ k ∈ Finset.range S.card, k ≤ ∑ x ∈ S, x := by
  exact_mod_cast (show ((∑ k ∈ Finset.range S.card, k : ℕ) : ℤ) ≤
      ((∑ x ∈ S, x : ℕ) : ℤ) by
    simpa [Nat.cast_sum] using
      Finset.sum_range_le_sum (s := S.map Nat.castEmbedding) (c := 0) (by simp))
```

Native `lean_run_code` returned `success: true`, `timed_out: false`; no proof error. During the concurrent module build it emitted only “imports are out of date and should be rebuilt”; the subsequent module build completed successfully. A longer explicit `have h'`/`push_cast` version also compiled before the module rebuild.

The initial untyped `simpa`, `simpa [← Nat.cast_sum]`, and `exact_mod_cast` on a sum of individual casts failed to move from Int sums to Nat sums. The successful proof fixes the whole-sum cast type before simplifying. No failed experiment is present in source.

Six strict rules: no new wrapper created; five search methods recorded with unavailable service explicitly distinguished; auxiliary variants checked; no custom predicate/typeclass mismatch; deletion and caller specialization queued; file worker should mention direct mathlib use in its module-level summary if it applies the replacement.

## Step 2.6 — Generalisation

| Parameter | Class | Used as | Mechanical candidates | Verified/result |
|---|---|---|---|---|
| `(S : Finset ℕ)` | structure value | Both cardinality and sum in conclusion; induction subject | Drop is not a well-formed weakening: statement directly references S. Nat-to-abstract ordered type would need a different range/codomain statement, not a mechanical parameter weakening. Nat-to-Int with nonnegative lower bound is supplied by mathlib. | Kept; isolated compiled proof explicitly quantifies only S. Integer specialization compiled as above. |
| Ambient `{K : Type*} [Field K] {l : ℕ}` | surrounding section parameters, **not actual theorem parameters** | Unused and automatically omitted | No declaration-level arguments to drop or weaken | `#check` shows only `(S : Finset ℕ)`; isolated proof uses no surrounding variables. |

No proposition hypotheses to drop, localize, split, or weaken from strict to weak; no decidability hypothesis or universe parameter. Inversion check: the proof intrinsically uses `Finset.range`, Nat order, finset cardinality, and sums throughout; it is not a concrete witness hiding an abstract theorem. The meaningful broader lower-bound statement already exists in mathlib and is covered by the replacement action. No public API generalisation proposed.

Literature search: n/a, private declaration; literature search is not required. Math MCP: n/a for the same reason.

## Step 2.7 — Signature packing

Before:

| Signature line | Codepoints | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 91 | 52 | `∑ k ∈ Finset.range S.card, k ≤ ∑ x ∈ S, x := by` (47) | 52 + 1 + 47 = 100 ≤ 100 | Repack |
| 92 | 51 | No next signature line | n/a | End |

After:

| Signature line | Codepoints | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 91 | 100 | No next signature line, proof follows | n/a | ok |

Native isolated `#check @sum_range_card_le_sum_probe` at `format.width 100`:

```text
sum_range_card_le_sum_probe : ∀ (S : Finset ℕ), ∑ k ∈ Finset.range S.card, k ≤ ∑ x ∈ S, x
```

All ten source lines measured in Python codepoints; maximum 100, others 7–87.

## Step 2.8 — Inequality scan

| Occurrence/location | Expression | Orientation/action | Rename |
|---|---|---|---|
| Statement, final L91 | `∑ k ∈ Finset.range S.card, k ≤ ∑ x ∈ S, x` | Already `≤`; retain | None |
| Internal `hcard`, L96 | `s.card ≤ a` | Already `≤`; retain | None |
| Induction hypothesis `ha` (generated context) | `∀ x ∈ s, x < a` | Already `<`; retain | None |
| Reversed syntax scan | No `≥` or `>` inequality in signature or hypotheses | No rewrite needed; match `=>` is not an inequality | None |

## Step 3 — All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 `by exact` | n/a: no wrapper. |
| 1.2 `by rfl` | n/a: no wrapper. |
| 1.3 `rw` + exact → `rwa` | n/a: rewrite is followed by arithmetic using two inequalities, not an exact hypothesis. |
| 1.4 simp + exact → simpa | Already terminal `simpa` in hcard. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: no constructor proof. |
| 1.7 apply + exact | n/a: no such chain. |
| 1.8 by_contra! | n/a: no contradiction split. |
| 1.9 eta reduction | Both lambdas inspect their arguments, not eta expansions; normalized arrows to `↦`. |
| 1.10 single-use have | `has` has two uses; hcard has proof content. Both retained. |
| 1.11 refine + fun | n/a: no apply/intro chain. |
| 1.12 redundant show | n/a: none in source. |
| 1.13 have projections | n/a: no product/conjunction projections. |
| 1.14 merge rewrites | Already one ordered rewrite list. |
| 1.15 terminal simp only | n/a: no squeezed terminal simp. |
| 1.16 nonterminal bare simp | n/a: both simp/simpa calls terminal in their subproofs. |
| 1.17 dot notation | `Finset.mem_range.2` already used. `card_le_card` acts on a constructed function, so a named theorem call is clear. |
| 1.18 `<|` | Parenthesized lambda is a multiline argument to a `simpa using` expression; removing parentheses would not improve clarity or lines. Subset ascription removed through named target argument. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 trivial existential helper | n/a: conclusion is an inequality. |
| 2.1 whole-proof grind | Tried live: failed, cannot derive the set-sum bound without combinatorial reasoning. |
| 2.2 delete before grind | Terminal grind succeeds after rewrites, but is no shorter than existing lia. Whole proof grind already failed; no redundant preceding grind tactic retained. |
| 2.3 simpa consolidation | Existing hcard simpa retained; direct whole-proof simp failed. Mathlib-specialization simpa verified for Phase 5a. |
| 2.4 fun_prop | n/a: no function regularity proposition. |
| 2.5 positivity | n/a: comparison is between distinct sums/cardinality, not positivity. |
| 2.6 gcongr | Tried terminal arithmetic: leaves mismatched pairwise goals because RHS summands are reversed. Retain lia. |
| 2.7 lia/omega | Live terminal lia closes; existing preferred arithmetic tactic retained. |
| 2.8 aesop | Tried whole proof: failed without progress. |
| 2.9 norm_num/norm_cast | No literal numeric evaluation or source casts. In the concrete replacement, exact_mod_cast tested and succeeds after whole-sum cast annotation; naive sum-of-casts route failed. |
| 2.10 decide | n/a: arbitrary variable finite set, no closed computation to evaluate. |
| 2.11 field_simp; ring | n/a: no denominators or field identity. |
| 2.12 linear_combination | n/a: no terminal ring/ring_nf and target is a Nat inequality. |
| 2.13 wlog | n/a: empty and insert branches are structurally different. |
| 2.14 collapse calc | n/a: no calc. Direct add_le_add trial failed on RHS summand order; lia remains clearest. |
| 2.15 shared `<;>` | n/a: induction branches need different proofs; no duplicated closing goals. |
| 3.1 erw → rw | n/a: already rw. |
| 3.2 fun_prop migration | n/a: no continuity/measurability. |
| 3.3 omega → lia | Already satisfied by 2.7; no omega introduced. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attribute | n/a: private single-call bound, no global automation consumer; pending mathlib replacement. |
| 3.6 simp_all | No simp_all only; whole-proof simp/aesop/grind trials already fail for the structural reason recorded above. |
| 3.7 remove limits | n/a: no set_option maxHeartbeats/maxRecDepth. |

Actual live multi-attempt probes sometimes additionally reported trailing `|`/argument parse errors because a single tactic line replacement leaves the original continuation text in the temporary experiment. The reported initial-goal failures remain explicit; no success was inferred from those experiments. The selected complete proof was independently compiled as a self-contained snippet, then in the actual module.

## Step 4 — Reflection

The original argument is mathematically coherent: insert a maximum a, bound the smaller set's cardinality by a, and add the inductive sum bound. `has` genuinely supports two rewrites; inlining would duplicate reasoning. `lia` handles the harmless summand reversal better than `gcongr` or a direct `add_le_add`. The stronger improvement is reuse of the existing integer bound, verified and handed to the sequential file-level pass. The selected edit keeps the current proof intact apart from formatting and the removal of a term ascription.

## Step 5 — Verification and gates

- Complete native `lean_diagnostic_messages` on `Roth/Wronskian.lean`: `success: true`, `partial: false`, `timed_out: false`, no failed dependencies; only the three pre-existing out-of-scope warnings listed above.
- `/Users/ramin/.elan/bin/lake build Roth.Wronskian` completed with exit 0, 1826 jobs, module compilation 20 seconds. Log: `/private/tmp/roth-wronskian-sum-range-card-module.log` (session 64299).
- Isolated selected proof under the exact nine original mathlib imports compiled via native `lean_run_code`, `success: true`, `timed_out: false`.
- Exact original statement assigned to the isolated proof term successfully. `#check` has only the S parameter, confirming no accidental field/size assumptions.
- `#print axioms sum_range_card_le_sum_probe`: `[propext, Classical.choice, Quot.sound]` only.
- `git diff -- Roth/Wronskian.lean` inspected: only the owned declaration changed; signature is whitespace-identical; no surrounding docs/imports/call sites altered.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Wronskian`, exit 0. |
| definition_protected | pass | No def/abbrev edits. |
| theorem_statement_protected | pass | Signature token sequence unchanged, only joined lines; exact type assignment compiled. |
| structure_gate | pass | Nine proof lines, longest branch six, no ∧. |
| naming_gate | pass | Descriptive mathematical name, zero forbidden patterns; no rename applied. |
| line_packing_gate | pass | One 100-codepoint signature line with complete table. |
| inequality_orientation_gate | pass | Zero reversed inequalities; occurrence table above. |
| comments preserved | pass | No comments within target; surrounding comments untouched. |
| proof/type/axioms | pass | Isolated compilation, exact statement assignment, standard three axioms. |
| full project / LeanEval | coordinator-owned | Source frozen and module/LSP pass reported before parent dependent builds. |

Overall: Phase-4 pass with one explicit Phase-5a mathlib replacement action. No incomplete Phase-4 validation is claimed complete.

## Step 6 — Result and checklist

Before: 11 declaration lines. After: 10. Saved: 1 signature line; proof body stays nine lines. Three local audit issues fixed. No renames queued. No comments present or removed. No statement, mathematical definition, or public API changed.

Refactoring needed: delete this private helper and specialize `Finset.sum_range_le_sum` directly at its sole caller after adding `Mathlib.Algebra.Order.Group.Int.Sum`, using the verified code above; validate affected dependents. No additional generalisation/API request.

- [x] Step 1: required references read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: all five search methods and strict-rule disposition reported.
- [x] Step 2.6: all actual parameters, ambient omissions, inversion and literature disposition reported.
- [x] Step 2.7: before/after per-line codepoint width table.
- [x] Step 2.8: inequality occurrence table.
- [x] Step 3: every one of 42 rules has a concrete status.
- [x] Step 4: whole-proof, direct-term, and alternative strategy reflection.
- [x] Step 5a: complete clean target LSP diagnostics.
- [x] Step 5b: diff gates, module, isolated proof/type/axioms passed.
- [x] Step 6a: no rename needed; sidecar untouched.
