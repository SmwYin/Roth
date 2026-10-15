# Phase 4 — `Roth.sum_range_le_sum_of_injective`

Dedicated declaration worker; baseline `1c983b5`. Original project lines 121–126; dispatch lines 116–121; final lines 116–119. Source ownership was only this declaration. No imports, shared reports, Git state, other declarations, API, or documentation changed.

## Step 1 — References

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md in full. Also read both Lean 4/mathlib-quality skills and relevant formatting, comment-preservation, documentation, and naming reference sections. The supplied Phase-4 worker contract controls this report. Newer `lia`/lambda and comment-preservation rules supersede older illustrative examples.

## Step 2 — Full audit

1. **LINT:** No warning in target. Complete native LSP reports success, not partial, with only the existing header warning and downstream unused `hφ`/`hd` at final lines 127/128. No suppression.
2. **HAVE SCAN:** Dispatch L119 `have h := sum_range_card_le_sum (Finset.univ.image d)`: no `by`, used once by L120–121 `rwa ... at h`; inline into terminal `simpa ... using ...`.
3. **SET_OPTION:** None; no limit/debug options added.
4. **SIMP SQUEEZE:** Original had no simp. New `simpa` is terminal and deliberately unsqueezed; cardinality simplification removes explicit `card_univ`/`card_fin` entries.
5. **NAMING:** Descriptive snake_case names the sum lower bound and injectivity hypothesis. No forbidden abbreviation, numbered scheme, single-letter public name, `_ge_`, or `_gt_`. No rename required.
6. **LINE PACKING:** All signature lines measured below; no repacking necessary.
7. **BY PLACEMENT:** `:= by` at end of conclusion line.
8. **FORMAT:** Two-space proof indentation, no empty proof lines, no semicolon chains. Removed the explicit mathematical lambda entirely using `hd.injOn`. No `haveI`/`letI`.
9. **COMMENTS:** No inline comments existed; docstring preserved byte-for-byte.
10. **DOCSTRING:** Existing two-line description states the sharp bound and its role in the degree argument; preserved under existing-docstring contract.
11. **VISIBILITY:** Public API preserved as explicitly instructed. Source search currently finds only its declaration; lack of callers is not authorization to delete or privatize the existing public theorem.
12. **STRUCTURE:** Two proof lines, one terminal tactic; no conjunction or branches, no decomposition needed.
13. **MATHLIB:** Existing private helper duplicates an integer mathlib bound after specialization. Declaration 5 already compiled the specialization; this worker confirms target-specific search evidence. Its deletion/import/caller adaptation remains the concrete Phase-5a action. No new wrapper is created.
14. **JUNK DEF:** n/a: theorem, not definition.
15. **EXISTS LEMMA:** n/a: no existential statement.
16. **SHOW vs CHANGE:** Neither appears in source.
17. **PUSH_NEG:** None.
18. **GENERALISE:** Injectivity is necessary: removing it admits the constant-zero counterexample at l=2 (kernel-checked below). Size and function occur in the conclusion. No ambient field parameter survives elaboration. Broader finite-type/integer forms are available through mathlib, with no current caller need for new public API.
19. **INEQUALITY:** One Lean-code `≤`, already correctly oriented; no `≥`/`>` in signature or proof. Table below.
20. **NORMAL-FORM:** Finite sums over `Fin l` are the canonical form used by polynomial-degree sums. Closed triangular-number expressions add division/subtraction and give no application benefit here.
21. **SYNTAX-GEN:** Bundled `Function.Injective d` directly matches callers' intended degree-distinctness data. Replacing it with a retract is stronger, not a weakening; `InjOn univ` is equivalent, not more general.
22. **IMPORT-FANOUT:** No import changed. Phase-5a import `Mathlib.Algebra.Order.Group.Int.Sum` and dependent validation belong to the file coordinator, as recorded by declaration 5.
23. **CASTS:** 0 dropped / 0 new cross-type / 0 new load-bearing ascriptions in diff. Existing `(ν : ℕ)` in statement is the genuine `Fin` value coercion and unchanged.
24. **INSTANCE-NAME:** n/a: no instance declaration. The unnecessary local `classical` was removed; existing decidable equality instances suffice.

Issues found/fixed: single-use h, avoidable classical, and verbose injectivity lambda. All three fixed. One already-known cross-declaration refactor retained for Phase 5a; no API proposal awaiting approval.

## Step 2.5 — Mathlib search status

| Method | Actual query / evidence | Result |
|---|---|---|
| A Lean-Finder | `sum of injective function Fin n to natural numbers at least sum of indices` | Returned `Finset.sum_range_le_sum`, alongside infinite-sum injection and pigeonhole facts. |
| B Loogle | `Function.Injective, Finset.sum, LE.le` | Only `Finset.geomSum_injective`, not a replacement for the target. |
| C LeanSearch | Service status inherited from file coordinator's confirmed HTTP 500 | Unavailable, not evidence of absence; redundant retry avoided. |
| D Source | Untruncated `rg` for `sum_range_le_sum` and full target name in mathlib/project; read Int/Sum lower-bound source | Confirms `Finset.sum_range_le_sum` at Mathlib/Algebra/Order/Group/Int/Sum.lean:72; no exact target-name duplicate found. |
| E Name pattern | Native local search `sum_range_le_sum` | Source hits for mathlib candidate and target. Index unavailable; no absence inferred from index. |

Auxiliary variants: `sum_Ico_le_sum`, `sum_le_sum_range`, `sum_image`, `card_image_of_injective`, `Function.Injective.injOn`, and `Fin.sum_univ_eq_sum_range`. The first three were inspected in source/reference evidence; all newly used names were checked against elaboration. Common-equivalents table has no special bucket for this finite-sum bound.

Actual `exact?` failed to close the live goal. `apply?` offered partial sum-injection, sum-monotonicity, and arithmetic-order routes with unproved subgoals; no complete proof. No claim that the mathematical result is absent from mathlib: the integer version is known and will be specialized directly in Phase 5a, using the compiled proof in [declaration 5's report](Wronskian-sum_range_card_le_sum.md).

Six replacement rules: (1) no new wrappers; (2) five methods recorded, failure distinguished from absence; (3) auxiliary variants inspected; (4) standard Function.Injective retained; (5) private duplicate deletion already queued, while the public API is user-protected; (6) coordinator owns any module-documentation note accompanying the actual import/reuse change.

## Step 2.6 — Generalisation and literature

| Parameter / hypothesis | Kind | Mechanical candidates | Verification and disposition |
|---|---|---|---|
| `{l : ℕ}` | index parameter | Drop, arbitrary finite index type | Drop would leave Fin l unbound; arbitrary finite type needs cardinality-based restatement and offers no current caller benefit. Keep. |
| `(d : Fin l → ℕ)` | function value | Drop, Nat→Int/lower-bounded integers, abstract order | Drop leaves sum unbound. Integer/lower-bound form is already in mathlib. Dense ordered codomains do not support this bound from mere distinctness. Keep current API. |
| `(hd : Function.Injective d)` | proposition | Drop; localize to `InjOn univ`; replace with left inverse; strict→weak | Dropping is false: Fin 2 constant zero violates 1≤0, compiled `by decide`. InjOn univ is equivalent and a retract is stronger, not a weaker assumption. No strict comparison to weaken. Keep. |
| Ambient `{K : Type*} [Field K]` | surrounding, not actual parameters | Drop/class parents/universe | Automatically omitted by Lean; isolated type check confirms no K/Field. Nothing to weaken. |
| Local `classical` | decidability | Drop | Removed; complete LSP and module build pass using existing Nat/Fin instances. |

Inversion check: the argument already works through a finite image rather than properties of a distinguished concrete witness. The useful abstraction is the bounded-integer finite-set theorem already supplied by mathlib; it motivates direct reuse, not another public companion. No typeclass, topology, universe, pointwise-analysis, or strict-to-weak hypothesis remains to test. No new public generalisation is warranted by existing callers.

Literature queries actually run:

- `distinct nonnegative integers sum at least n(n-1)/2 generalization`: top three returned OEIS A076107, *Variations on the Erdős distinct-sums problem*, and *A generalization of the Erdős–Birch theorem*. These concern different additive-number-theory questions and supply no weakening of this statement.
- `"distinct" "sum" "n(n-1)/2" "nonnegative" minimum`: directly relevant search result was the elementary distinct-composition minimum; other hits concern sequence sums and numerical distance matrices. No new hypothesis relaxation identified.
- `site.leanprover-community.github.io/mathlib4_docs sum_range_le_sum`: generic index/repository/order-sum pages ranked first; opened the exact primary documentation page directly.

The [official Mathlib integer-sum documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/Group/Int/Sum.html) supplies the useful general form: distinct integers bounded below by c have sum at least the consecutive interval starting at c of the same cardinality. This supports the already-queued helper replacement. The local pinned source confirms that theorem is available here. ChatGPT math MCP: unavailable (no matching callable tool in the session). Literature-driven new API changes: none; the broader mathlib formulation is reused internally during Phase 5a.

## Step 2.7 — Line packing

At `format.width := 100`, the reference type is:

```lean
@Roth.sum_range_le_sum_of_injective :
  ∀ {l : ℕ} (d : Fin l → ℕ), Function.Injective d → ∑ ν, ↑ν ≤ ∑ ν, d ν
```

Both before and after (signature byte-identical):

| Signature line | Codepoints | Next syntax unit | Arithmetic | Action |
|---|---:|---|---|---|
| 116 | 83 | whole conclusion `∑ ν : Fin l, (ν : ℕ) ≤ ∑ ν, d ν := by` (37) | 83+1+37=121>100 | ok |
| 117 | 41 | none; proof next | n/a | ok |

The summation binder/body is a single conclusion syntax unit, not split mid-binder. Proof line widths are 72 and 82. No changed line exceeds 100 codepoints.

## Step 2.8 — Inequality scan

| Location | Occurrence | Orientation/action |
|---|---|---|
| L117 conclusion | `∑ ν : Fin l, (ν : ℕ) ≤ ∑ ν, d ν` | correct lower-bound orientation; retain |
| L116 hypotheses | none in `Function.Injective d` | n/a |
| L118–119 proof | no comparison tokens | n/a |
| Name | `_le_`, no `_ge_`/`_gt_` | correct; no rename |

The pre-existing docstring's `≥` is mathematical prose and intentionally preserved.

## Step 3 — Golfing rule pass (all 42)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no such wrapper. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw+exact→rwa | Original already used rwa; replaced entire fact/rewrite sequence by simpa. |
| 1.4 simp+exact→simpa | Applied analogous rewrite-and-use consolidation into terminal simpa. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor tuple | n/a: no conjunction/existence constructor. |
| 1.7 apply+exact | n/a: no such chain. |
| 1.8 by_contra! | n/a: no contradiction chain. |
| 1.9 eta-reduce | Explicit membership-ignoring injectivity lambda replaced by hd.injOn. |
| 1.10 inline single-use have | Applied to h. |
| 1.11 apply+intro | n/a: none. |
| 1.12 redundant show | n/a: none. |
| 1.13 have projections | n/a: h is an inequality, no projections. |
| 1.14 merge rw | n/a: original one rwa chain. |
| 1.15 unsqueeze terminal simp | New terminal simpa is unsqueezed. |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp. |
| 1.17 dot notation | Applied hd.injOn. |
| 1.18 `<|` | n/a: parenthesized image is a data argument, not a trailing lambda/tactic term. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential helper | n/a: no existential helper. |
| 2.1 grind | Actual live attempt failed: aggregate inequality not derivable by arithmetic alone. |
| 2.2 delete before grind | n/a: no retained grind. |
| 2.3 simpa consolidation | Applied; one terminal tactic replaces four original body lines. |
| 2.4 fun_prop | n/a: no analytic function-property goal. |
| 2.5 positivity | n/a: lower bound is a nonzero sum in general, not a zero-bound goal. |
| 2.6 gcongr | Actual attempt reduced to pointwise ν≤d ν, which injectivity does not imply; rejected. |
| 2.7 lia/omega | Actual lia failed on aggregate bound; no linear arithmetic data relates sums. |
| 2.8 aesop | Actual attempt failed, no progress. |
| 2.9 norm_num/norm_cast | n/a: target has symbolic finite sums, no numeric/cast-normalization proof step. |
| 2.10 decide | n/a for target: symbolic l,d prevent finite computation; used only for concrete counterexample in scratch. |
| 2.11 field_simp/ring | n/a: no fractions or algebraic equality. |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic hypotheses. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc composition | n/a: no calc chain. |
| 2.15 `<;>` | n/a: one goal and terminal tactic. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 legacy function tactics | n/a: none. |
| 3.3 omega→lia | n/a: no omega retained; lia tested at 2.7. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | n/a: arbitrary injective-function sum bound is not a canonical simplification rule; no new attributes needed. |
| 3.6 simp_all | n/a: no simp_all only; direct simpa already closes. |
| 3.7 remove limits | n/a: no maxHeartbeats/maxRecDepth. |

## Step 4 — Reflection and actual experiments

Whole-proof `grind`, `simp`, `aesop`, `lia` failed; `gcongr` produces an invalid pointwise requirement (a permutation need not dominate its index). `exact?` found no exact proof; `apply?` produced only incomplete suggestions. Direct `simpa` succeeds. Initial multiline `lean_multi_attempt` replacements also exposed suffix/parser errors because that tool replaces one tactic position while leaving the old following lines; these were not treated as final validation. The complete contextual source edit then passed full-file diagnostics and the module build. The final proof is one tactic, so a term expression would obscure the finite-image/cardinality normalization rather than simplify it.

## Step 5 — Verification

- Actual `/Users/ramin/.elan/bin/lake build Roth.Wronskian` exited 0, 1826 jobs; log `/private/tmp/roth-wronskian-sum_range_le_sum_of_injective-module.log`.
- Complete native `lean_diagnostic_messages` returned `success: true`, `partial: false`, `timed_out: false`, no failed dependencies/errors. Only three pre-existing out-of-target warnings listed above.
- Isolated native `lean_run_code` reported stale imports despite module rebuild; no success claimed for that probe. Fallback compiler verification is recorded below.
- Source frozen and coordinator notified before shared full-project/LeanEval validation; those builds/publication are coordinator-owned.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit0. |
| definition_protected | pass | No definition/abbreviation edit. |
| theorem_statement_protected | pass | Both signature lines byte-identical to baseline. |
| structure_gate | pass | Two body lines; no conjunction/branches. |
| naming_gate | pass | Descriptive snake_case, no forbidden patterns. |
| line_packing_gate | pass | Complete two-line codepoint arithmetic table above. |
| inequality_orientation_gate | pass | One correctly oriented ≤, no code ≥/>; table above. |

Overall: pass. No new axiom, sorry, admit, native_decide, limits, or debug scaffolding in source. Only target proof changed.

## Step 6 — Result

Before: 6 declaration lines. After: 4. Saved: 2. Proof body: 4→2 lines. Audit issues found/fixed: 3/3. Applied rules: 1.4, 1.9, 1.10, 1.17, 2.3, plus removal of unnecessary classical. Renames queued: none. Comments preserved: no inline comments existed; existing docstring byte-identical.

Refactoring needed: the already-queued Phase-5a deletion of `sum_range_card_le_sum`, its new mathlib import, and direct specialization in this caller. No additional refactor or generalisation proposal.

- [x] Step 1: reference docs read.
- [x] Step 2: all 24 audit items.
- [x] Step 2.5: five-method mathlib search status.
- [x] Step 2.6: every parameter/hypothesis, mechanical candidates, inversion/literature status.
- [x] Step 2.7: complete signature width table.
- [x] Step 2.8: every inequality occurrence.
- [x] Step 3: all 42 rules.
- [x] Step 4: bounded actual automation/alternative proofs.
- [x] Step 5a: complete native LSP clean of errors.
- [x] Step 5b: actual module build and seven diff gates.
- [x] Step 6a: no renames needed.

### Isolated verification completion

`lake env lean /private/tmp/roth-wronskian-decl07-check.lean` exited 0. It checked the exact public type by assigning `@Roth.sum_range_le_sum_of_injective` to an independently written quantified signature, kernel-checked the constant-zero Fin 2 counterexample with `decide`, and checked every named simplification component. `#print axioms` returned exactly `[propext, Classical.choice, Quot.sound]`. The source itself contains no newly introduced axiom; removing the local `classical` directive does not imply eliminating all inherited classical dependencies.

Exact width-100 `#check` output (one line):

```lean
@Roth.sum_range_le_sum_of_injective : ∀ {l : ℕ} (d : Fin l → ℕ), Function.Injective d → ∑ ν, ↑ν ≤ ∑ ν, d ν
```
