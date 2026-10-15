# Declaration cleanup: `Roth.weight_eq_zero_iff`

Dedicated fresh worker `decl09`; baseline `5c86638`; only this declaration and this report are owned by the worker. The parent owns full project builds and publication. Before: lines 89–91, three declaration lines. After: lines 90–92, three declaration lines plus one scoped `omit` command. Existing public docstring, conclusion, argument order, and proof are preserved.

## Step 1 — References

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, and cleanup-gates.md. Read the complete supplied declaration-worker prompt, both skill entry points, and the relevant formatting, documentation, hypothesis, inequality, and visibility sections of style-rules.md. No naming defect requires a rename workflow. User approval to remove verified unused DecidableEq assumptions overrides the default signature-preservation restriction for this specific instance only.

## Step 2 — Full audit

1. **LINT:** target had unusedSectionVars and unusedDecidableInType warnings for `[DecidableEq σ]`. Scoped omission removes both. Final full-file diagnostics have zero target warnings or errors.
2. **HAVE SCAN:** no `have` bindings; no single-use intermediate to inline.
3. **SET_OPTION:** no per-declaration option or raised heartbeat limit.
4. **SIMP SQUEEZE:** one terminal `simp [...]`; keep unsqueezed. Live deletion probes show the positivity/nonnegativity/extensionality arguments are substantive.
5. **NAMING:** `weight_eq_zero_iff` describes exactly the zero characterization, uses snake_case, and contains no numeric scheme, forbidden abbreviation, or reversed inequality name. No rename queued.
6. **LINE PACKING:** both signature lines measured below; whole conclusion plus `:= by` would make the first line 102 codepoints, so its break is justified.
7. **BY PLACEMENT:** `by` ends the conclusion line.
8. **FORMAT:** four-space signature continuation, two-space tactic indentation, one tactic, no blank interior lines, no `haveI`/`letI`, no trailing whitespace.
9. **COMMENTS:** zero inline proof comments before and after; no deletion or relocation. Existing docstring preserved byte-for-byte.
10. **DOCSTRING:** existing public statement and source citation explain the positive-parameter restriction and its index application. Preserved under Lean4 Rule A.
11. **VISIBILITY:** public headline result is used in `Roth/Index.lean:105`; keep public.
12. **STRUCTURE:** one tactic line; no conjunction in theorem conclusion and no branches; well below headline proof limit 15.
13. **MATHLIB:** five-method search below confirms the existing generic sum-zero building block. The Finsupp weight theorem needs a different weight representation and codomain structure; not a direct replacement for this public API.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: an iff theorem, not a private existential witness helper.
16. **SHOW vs CHANGE:** no `show` or `change` expression.
17. **PUSH_NEG:** no negation-pushing tactic.
18. **GENERALISE:** remove verified unused DecidableEq only; retain positivity, Fintype, and data parameters for the reasons in the table below.
19. **INEQUALITY:** strict hypothesis already has smaller side on left; full occurrence scan below.
20. **NORMAL-FORM:** `weight r d = 0 ↔ d = 0` is the canonical equality-to-zero characterization. Pointwise zero is an internal extensionality step, not a better public conclusion.
21. **SYNTAX-GEN:** OK: explicit `hr` and implicit `r,d` support the existing rewrite `weight_eq_zero_iff hr`; no callsite restatement needed.
22. **IMPORT-FANOUT:** n/a: no imports added or changed.
23. **CASTS:** 0 dropped / 0 added or kept in diff; existing definition handles the necessary ℕ→ℝ casts.
24. **INSTANCE-NAME:** n/a: theorem introduces no instance declaration.

Issues found: one unused typeclass dependency producing two lint warnings. Fixed: one. Refactoring needed: none within the approved scope.

## Step 2.5 — Mathlib search

| Method | Query and observed result |
|---|---|
| A Lean-Finder | `finite sum nonnegative terms equals zero iff every term zero`: found `Finset.sum_eq_zero_iff_of_nonneg`, `Fintype.sum_eq_zero_iff_of_nonneg`, and `List.all_zero_of_le_zero_le_of_sum_eq_zero`. |
| B Loogle | `"sum_eq_zero_iff_of_nonneg"`: found both Finset and Fintype versions with their general ordered-additive-monoid signatures. |
| C LeanSearch | Known session HTTP500 service failure, inherited from parent; recorded unavailable rather than treating outage as negative mathematical evidence. Local/Finder/Loogle alternatives used. |
| D source | Untruncated `rg` on `weight_eq_zero_iff`, `weight_eq_zero`, `sum_eq_zero_iff_of_nonneg` in Finsupp/Weight and ordered big operators located `Finsupp.weight_eq_zero_iff_eq_zero` and generic sum uses. Read Weight.lean 140–185. |
| E name pattern | Native `lean_local_search weight_eq_zero` returned this theorem, `Homogenization.weight_eq_zero_iff`, and `Finsupp.weight_eq_zero_iff_eq_zero`; semantic index reported unavailable, so empty absence claims would be invalid. |

Auxiliary variants inspected: Finset and Fintype sum-zero equivalences, `Finsupp.ext_iff`, Finsupp weight-zero characterization, `le_weight_of_ne_zero`, `le_weight_of_ne_zero'`. Common-equivalents lookup: no discrete/finiteness/bornology bucket applies.

Compiled `#check` confirms the imported signatures. Finsupp's result requires `[CanonicallyOrderedAdd M]` and `[NonTorsionWeight ℕ w]`; the present real-valued quotient sum is not its literal statement. Recasting in nonnegative reals would be a representation/API project outside this declaration's approved scope. Conclusion: **partial match; keep the established Roth API, already built directly on the appropriate Finset theorem**. No absence claim is made. Live `exact?` failed to close the actual target; `apply?` offered only partial logical decompositions or an injectivity premise, not a direct replacement.

## Step 2.6 — Generalisation

| Parameter | Class | Use | Candidates / verification | Result |
|---|---|---|---|---|
| `{σ : Type*}` | type variable | domain of all coordinates | Already universe polymorphic; removing it leaves every coordinate type unbound. | Keep. |
| `[Fintype σ]` | typeclass | finite full-domain sum in `weight` | Dropping changes whether the existing definition can be formed; `[Finite σ]` needs a chosen Fintype and a signature/definition restatement. | Keep existing representation; no broader rewrite proposed. |
| `[DecidableEq σ]` | decidability | unused | Drop via scoped `omit`; independent example without this instance, module build, and complete LSP pass. | Removed, explicitly user-approved. |
| `{r : σ → ℕ}` | data | denominators in weight and positivity assumption | Cannot drop referenced datum; abstract real/field weights would require changing `weight` itself. | Keep. |
| `(hr : ∀ j, 0 < r j)` | proposition | `(hr _).ne'` excludes zero denominators | Drop or strict→weak refuted by compiled Unit counterexample: `r=0`, `d=single () 1` has zero weight but is nonzero. Point-localisation to support would change explicit public API. `∀ j, r j ≠ 0` is equivalent for naturals, not a genuine weakening. | Keep load-bearing strict positivity. |
| `{d : σ →₀ ℕ}` | data | weighted multi-index and zero conclusion | Cannot drop referenced datum. Natural nonnegativity supplies the sum criterion; arbitrary signed coefficients allow cancellation. | Keep. |

Inversion check: unfolding `weight` exposes a general nonnegative finite-sum fact, which already exists as `Finset.sum_eq_zero_iff_of_nonneg`. The local result supplies the quotient nonzeroness and Finsupp extensionality needed by this project's named weight. Extracting another general sum theorem would duplicate mathlib. Big-change candidates applied: none. No speculative generalisation is queued.

Public literature query: `positive weighted sum nonnegative terms zero iff all zero generalized ordered monoid`. Top three displayed hits:

1. [Zerosumfree monoid](https://en.wikipedia.org/wiki/Zerosumfree_monoid): terminology for sums of nonzero elements not vanishing.
2. [When Is a Graded Free Complex Exact?](https://www.mdpi.com/2227-7390/10/18/3393): positive/reduced monoids provide an abstract setting.
3. [Mathlib ordered monoid documentation](https://cs.brown.edu/courses/cs1951x/docs/algebra/ordered_monoid.html): older library presentation of order/nonzero relationships; current local Lean signatures were used for implementation decisions.

The abstract ordered-monoid formulation is consistent with the existing generic Finset building block; it does not justify allowing zero denominators. ChatGPT math MCP: unavailable in discovered tools, no fabricated second opinion. Literature-driven API changes: none.

## Signature width and inequality artifacts

Native `#check` with `set_option format.width 100`:

```lean
@Roth.weight_eq_zero_iff : ∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ},
  (∀ (j : σ), 0 < r j) → ∀ {d : σ →₀ ℕ}, Roth.weight r d = 0 ↔ d = 0
```

| Signature line (final) | Codepoints | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 90 | 73 | `weight r d = 0 ↔ d = 0 := by` (28) | 73 + 1 + 28 = 102 > 100 | ok: conclusion break |
| 91 | 32 | none; proof follows | n/a: final signature line | ok |

The same widths hold before editing at lines 89–90. No repacking changes required.

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | `hr`, final line 90 | `0 < r j` | none: correct orientation | none |
| reversed scan | complete signature and hypotheses | zero `≥` / `>` occurrences | n/a | no `_ge_` / `_gt_` name |

## Step 3 — All 42 golfing rules

- [1.1] `by exact`: n/a; proof is simp.
- [1.2] `by rfl`: n/a; equivalence is not definitional.
- [1.3] `rw + exact`: n/a; no rewrites or exact chain.
- [1.4] `simp + exact`: n/a; simp already closes.
- [1.5] trailing rfl: n/a; no trailing tactic.
- [1.6] constructor compression: n/a; no constructor proof.
- [1.7] apply/exact: n/a; no such chain.
- [1.8] by_contra/push_neg: n/a; no contradiction block.
- [1.9] eta reduction: n/a; no lambda.
- [1.10] inline have: n/a; no have.
- [1.11] apply/intro: n/a; no such chain.
- [1.12] redundant show: n/a; no show.
- [1.13] have/projections: n/a; no projected intermediate.
- [1.14] merge rw: n/a; no rw.
- [1.15] terminal simp unsqueeze: already unsqueezed; bare simp failed live with no progress.
- [1.16] nonterminal simp squeeze: n/a; terminal only.
- [1.17] dot notation: `(hr _).ne'` already uses it.
- [1.18] `<|`: n/a; no trailing lambda/tactic argument parentheses.
- [1.19] push Not: n/a; no push_neg.
- [1.20] existential inline: n/a; no private existential helper.
- [2.1] grind: live attempt failed on weight-zero implying d-zero.
- [2.2] delete before grind: n/a; retained proof has no grind.
- [2.3] simpa consolidation: n/a; single closing simp already has no follow-up to combine.
- [2.4] fun_prop: n/a; no continuity/measurability/differentiability goal.
- [2.5] positivity: n/a as whole proof; goal is an iff, and sum nonnegativity is discharged by simp's `div_nonneg` argument.
- [2.6] gcongr: n/a; no monotonicity inequality goal.
- [2.7] lia/omega: n/a; theorem is a real quotient-sum equivalence over arbitrary Finsupp, not Presburger arithmetic.
- [2.8] aesop: live exhaustive attempt left the forward implication unsolved.
- [2.9] norm_num/norm_cast: n/a; no fixed numeric computation or standalone cast equality in the theorem.
- [2.10] decide/kernel: n/a; arbitrary real and function parameters, no finite closed proposition.
- [2.11] field_simp/ring: n/a; sum-zero iff all coordinates zero uses order, not a polynomial identity.
- [2.12] linear_combination: n/a; no ring/ring_nf ending or polynomial hypotheses.
- [2.13] wlog: n/a; no symmetric branches.
- [2.14] calc term mode: n/a; no calc.
- [2.15] `<;>`: n/a; one goal closed by one tactic.
- [3.1] erw→rw: n/a; no erw.
- [3.2] legacy property tactics: n/a; none.
- [3.3] omega→lia: n/a; no omega.
- [3.4] rcases rfl: n/a; no rcases.
- [3.5] automation attribute: no new attribute; explicit positive hypothesis and established rewrite API preserved.
- [3.6] simp_all: live expanded `simp_all` without explicit nonzeroness failed, retaining disjunctions `d i = 0 ∨ r i = 0`; existing focused simp is sufficient.
- [3.7] raised options: n/a; none present or added.

Additional live minimisation: removing `div_nonneg` leaves the sum unexpanded; removing `(hr _).ne'` leaves zero-denominator disjunctions; removing `Finsupp.ext_iff` leaves pointwise-zero iff Finsupp-zero; replacing Finset with Fintype sum-zero plus `funext_iff` fails to discharge the function nonnegativity premise. Original tactic passes with zero residual goals and no tactic diagnostics.

## Step 4 — Reflection

The entire proof is already one tactic. It unfolds the quotient sum, uses nonnegative summands to reduce zero sum to coordinatewise zero, excludes zero denominators using hr, and uses Finsupp extensionality. Bare automation and direct theorem search did not improve this. A term proof would explicitly package these same steps and be longer. Retain the focused proof; the substantive improvement is the verified removal of a spurious instance.

## Step 5 — Verification and gates

- Independent native `lean_run_code` example uses `[Fintype σ]` and no `[DecidableEq σ]`, reproduces the proof without calling `weight_eq_zero_iff`, success=true, timed_out=false.
- Same probe compiles `weight (fun _ : Unit ↦ 0) (Finsupp.single () 1) = 0 ∧ (Finsupp.single () 1 : Unit →₀ ℕ) ≠ 0`; this refutes both the hr drop and nonnegative-only weakening. The scratch counterexample's long-line style warning affects no repository source.
- `/Users/ramin/.elan/bin/lake build Roth.Box > /private/tmp/roth-box-d09-module.log 2>&1`: session 7673, actual exit 0, 1154 jobs.
- Complete native file diagnostics: success=true, partial=false, timed_out=false; zero errors, zero target warnings. Twelve remaining warnings concern header metadata or future declarations; no suppression added.
- Native `lean_verify`: standard trust, axioms `propext`, `Classical.choice`, `Quot.sound`; no nonstandard axioms or source-scan warnings.
- Native `#check` and `#print axioms` compile successfully and corroborate type and trust.
- `git diff --check` exits 0; source diff adds only the scoped `omit` before the preserved docstring. No Index change is required by this typeclass removal.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | module command above, actual exit 0 |
| definition_protected | pass | no def/abbrev touched |
| theorem_statement_protected | pass, authorized weakening | literal theorem signature/conclusion unchanged; only approved unused section instance removed from elaborated type |
| structure_gate | pass | one tactic line; no conjunction or branches |
| naming_gate | pass | descriptive weight/zero/iff name, no forbidden patterns |
| line_packing_gate | pass | two measured rows above; joined signature 102 codepoints |
| inequality_orientation_gate | pass | only `0 < r j`, no reversed comparison |
| docstrings/comments | pass | docstring byte-identical, zero proof comments before/after |
| full project and LeanEval | parent-owned checkpoint | source frozen for parent's separate builds; no premature success claim |

Overall worker gates: PASS. Parent must record its full-build and separate LeanEval evidence before publication.

## Step 6 — Result and checklist

Before 3 declaration lines; after 3; saved 0. One additional scoped-omit line. One issue fixed, two warnings removed. No proof-rule rewrite retained. Renames queued: none. Refactoring needed: none. Source ownership released once module and complete LSP gates passed; report ownership released at final handoff.

- [x] Step 1: reference documents read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: all five search methods accounted for.
- [x] Step 2.6: every parameter, strict/weak counterexample, inversion, and public literature covered.
- [x] Step 2.7: every signature line measured.
- [x] Step 2.8: inequality occurrence and reversed-operator scan reported.
- [x] Step 3: all 42 golfing rules have concrete statuses.
- [x] Step 4: independent strategy reflection completed.
- [x] Step 5a: complete diagnostics clean for target, known unrelated warnings explicit.
- [x] Step 5b: module build and all diff gates passed.
- [x] Step 6a: no rename needed or queued.
- [x] Step 6b: report complete; parent retains checkpoint builds and Git ownership.

Publication verification: full `lake build` session 2639 exited 0 (2586 jobs;
`/private/tmp/roth-box-d09-full.log`); separate `lake build Roth.LeanEval` session 25122
exited 0 (2585 jobs; `/private/tmp/roth-box-d09-leaneval.log`). All affected dependents pass.
