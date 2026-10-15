# `Roth.weight_zero` — declaration cleanup

Worker: fresh declaration worker `decl07`; baseline HEAD `c9979b7`.
Owned source: only `weight_zero` in `Roth/Box.lean`, originally lines 76–77;
final lines 77–78. Parent owns dependent builds, checkpoint, and publication.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full. I also read the complete
declaration-worker prompt, both Lean skills, and relevant style sections on line
width, formatting, comments, documentation, unused variables, declarations,
tactics, and visibility. Naming is checked against the explicit naming gate and
the skill's naming rules; no naming punch-list issue requires a rename.

## Step 2 — audit

The theorem states that summing the coordinate weights of the zero multi-index
gives zero. Each numerator is zero, hence every summand is zero, regardless of
the natural-number denominators. The proof is already one terminal simp call.

| # | Audit | Concrete finding/action |
|---|---|---|
| 1 | LINT | Baseline has unusedSectionVars and unusedDecidableInType warnings for `[DecidableEq σ]`. Remove this instance under the user's explicit approval; both target warnings disappear. |
| 2 | HAVE SCAN | No `have` bindings in the proof, so no single-use intermediary exists. |
| 3 | SET_OPTION | No declaration-local options; none introduced. |
| 4 | SIMP SQUEEZE | `simp [weight]` is terminal and unsqueezed. Bare `simp` fails live, so keep the explicit definition argument. |
| 5 | NAMING | `weight_zero` is snake_case and names the function followed by its zero-input argument. No forbidden abbreviation, scheme number, numeric auxiliary, single-letter name, or reversed inequality suffix. No rename. |
| 6 | LINE PACKING | One signature line, 54 codepoints, with all arguments/conclusion/`by` already on it. Full table below. |
| 7 | BY PLACEMENT | `by` ends the signature line. |
| 8 | FORMAT | One two-space-indented tactic; no interior blank line, semicolon, trailing whitespace, `haveI`, or `letI`. |
| 9 | COMMENTS | No inline proof comments before or after. |
| 10 | DOCSTRING | Existing one-sentence zero-input description is preserved byte-for-byte. No proof strategy to relocate. |
| 11 | VISIBILITY | Public simp API for the project-owned weight definition; retain public visibility and `@[simp]` as required. |
| 12 | STRUCTURE | One proof-body line, no conjunction, no branches; extraction would add unnecessary structure. |
| 13 | MATHLIB | Five-method status below. Generic sum-zero lemmas supply the proof, while `Roth.weight` remains the project API. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: no existential statement or witness. |
| 16 | SHOW vs CHANGE | Neither construct occurs. |
| 17 | PUSH_NEG | No negation-pushing tactic. |
| 18 | GENERALISE | Verified removal of unused DecidableEq; Fintype drop and replacement by Finite fail at the statement. Full parameter table below. |
| 19 | INEQUALITY | No inequality symbol in signature/hypotheses; table below. |
| 20 | NORMAL-FORM | `weight r 0 = 0` is the standard zero-evaluation simp direction, with simpler RHS. Preserve. |
| 21 | SYNTAX-GEN | OK: explicit `r` is convenient for rewriting and simp matching; no bundled condition is needed. |
| 22 | IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in the diff; the diff is only an omit command. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues found: one redundant assumption producing two diagnostics. Fixed: one.
Refactoring needed: none within the approved scope.

### Mathlib search status

| Method | Queries/evidence | Result |
|---|---|---|
| A — Lean-Finder | `sum of zero function is zero weighted sum zero` | Returned `finsum_zero`, `finsum_eq_zero_of_forall_eq_zero`, `Finsupp.sum_zero_index`. Different sum representations, relevant generic building blocks. |
| B — Loogle | `Finset.sum, (0 : _)` | Returned `Finset.sum_empty'`, `Finset.sum_empty`, `Finset.sum_of_isEmpty`; these concern empty sums, not the general index type here. |
| C — LeanSearch | Natural-language zero-weight/zero-sum route | Unavailable: inherited service HTTP 500 already established for this file; parent explicitly directed no repeated retries. This is not evidence of absence. Local source and native elaboration provide fallback. |
| D — source search | `weight_zero`, `sum_const_zero`, `sum_zero`; then `weight`, `zero`, generated additive variants in `Data/Finsupp/Weight.lean` and `Algebra/BigOperators/Group/Finset/Defs.lean` | Full-name initial textual search had no hit; expanded search exposed bundled `Finsupp.weight`, `weight_eq_sum`, `map_zero`, and generated additive sum infrastructure. No absence claim inferred from the first search. |
| E — local names | `Finset.sum_const_zero` | Returned `Finset.sum_const_zero` in `Group/Finset/Defs.lean`; index reported warming, so only this positive result is used. |

Auxiliary forms checked: `Finset.sum_eq_zero`, `Finset.sum_const_zero`,
`Finsupp.sum_zero_index`, `Finsupp.weight_eq_sum`, and bundled `map_zero`.
Native `#check` confirmed the first two sum lemmas. Live `exact?` did not close
the target. Live `apply?` offered partial real-equality/zero-characterization
routes, not a complete replacement; its temporary sorry warning belongs to the
rejected probe and was never written to source.

Common-equivalents lookup: no discrete/topological/bornological bucket applies.
Conclusion: partial generic matches already drive `simp [weight]`. Keep the
public project simp theorem under the user's explicit API-preservation scope.
Switching the definition to the bundled Finsupp representation would be a
separate representation migration, already outside the authorized changes.
There is no new wrapper, new generic lemma, or mathematical absence assertion.

### Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates / verification | Result |
|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | Domain of `r`, multi-indices, and finite sum | Already universe-polymorphic. Dropping σ cannot preserve the dependent types; no smaller universe restriction is present. | Keep. |
| 2 | `[Fintype σ]` | typeclass | Instance required to elaborate `Roth.weight` in the conclusion | Native drop probe fails `failed to synthesize Fintype σ`; native `[Finite σ]` replacement fails at the same statement. A selected Fintype construction would restate the API. | Keep. |
| 3 | `[DecidableEq σ]` | decidability | No role in statement or proof | Scoped `omit [DecidableEq σ] in` before unchanged docstring; full module/LSP and independent proof verify. | Removed under explicit user approval. |
| 4 | `(r : σ → ℕ)` | structure value | Denominator function in `weight r 0` | Appears in conclusion. Removing it would leave a free variable, or implicit insertion would change binder mode rather than weaken a hypothesis. No propositional/pointwise weakening applies. | Keep explicit. |

No propositional hypotheses, positivity assumptions, bundled equivalences, or
analytic typeclasses occur. Inversion check: unfolding `weight` leaves the
abstract fact that a finite sum of zero summands is zero, already supplied by
`Finset.sum_eq_zero`/`sum_const_zero`. No additional abstract theorem is needed.
An arbitrary scalar codomain or support sum would require changing `weight`
itself; it is not a theorem-only assumption weakening. No broader change queued.

### Public literature search

Query: `weighted sum zero vector linear map zero generalization`.
Top three search hits were [Vaia's zero mapping exercise](https://www.vaia.com/en-us/textbooks/math/linear-algebra-4-edition/chapter-5/problem-32-prove-a-the-zero-mapping-0-defined-by-mathbf0v0-i/),
[weighted zero-sum sequence research](https://arxiv.org/abs/2202.00461), and
[Zero element](https://en.wikipedia.org/wiki/Zero_element).
The first is a secondary exercise page; the second concerns combinatorial
zero-sum subsequences and is not this identity; the third gives general zero
terminology. None supports an additional project change.

The relevant primary teaching source returned by that query was inspected:
[Jakob Scholbach, Linear Maps, Remark 4.4](https://jakobscholbach.github.io/lectures/linear-algebra/maps/)
derives preservation of zero from linearity. This confirms the familiar general
zero-map principle; applying it here through a newly bundled map would require
changing the chosen representation. The current finite-sum proof already uses
the appropriate abstract algebraic ingredients. No new positivity requirement.
ChatGPT math MCP: unavailable; no matching tool is exposed. No second opinion
was fabricated. Literature-driven changes queued: none.

### Line packing

Native `#check` with `format.width 100`, after rebuilding:

```lean
@Roth.weight_zero : ∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ), Roth.weight r 0 = 0
```

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| Before 76 / after 77 | 54 | none; proof body follows | n/a: all signature tokens including conclusion and `:= by` fit on this line | ok |

The signature text is unchanged. The new scoped command is 23 codepoints and
is placed before the docstring, so it does not break documentation attachment.

### Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Entire signature and inherited hypotheses | n/a: no `≥` or `>`; conclusion is equality | none | none; name has neither `_ge_` nor `_gt_` |

## Step 3 — all 42 golfing rules

- [1.1] `by exact`: n/a, proof is a simp tactic, not a term wrapper.
- [1.2] `by rfl`: n/a, no such wrapper; live `rfl` fails because the finite sum is not definitionally zero.
- [1.3] `rw + exact`: n/a, no rewrite/exact pair.
- [1.4] `simp + exact`: n/a, simp already closes.
- [1.5] trailing `rfl`: n/a, no trailing tactic.
- [1.6] anonymous constructor: n/a, equality has no constructor proof block.
- [1.7] `apply + exact`: n/a, no apply/exact sequence.
- [1.8] `by_contra!`: n/a, no contradiction proof.
- [1.9] eta reduction: n/a, no lambda in proof.
- [1.10] inline have: n/a, zero have bindings.
- [1.11] refine/fun: n/a, no introductions.
- [1.12] redundant show: n/a, no show.
- [1.13] obtain projections: n/a, no have or projections.
- [1.14] merge rw: n/a, no rw.
- [1.15] terminal simp only: n/a, existing terminal simp is already unsqueezed.
- [1.16] nonterminal simp: n/a, sole simp is terminal.
- [1.17] dot notation: n/a, no direct proof-term application to shorten.
- [1.18] `<|`: n/a, no nested application parentheses.
- [1.19] push Not: n/a, no negation tactic.
- [1.20] existential helper: n/a, not an existential or helper declaration.
- [2.1] grind: live `grind` and `grind [weight]` both fail; retained simp.
- [2.2] tactics before grind: n/a, no grind in selected proof.
- [2.3] simpa consolidation: n/a, no trailing closing step to combine.
- [2.4] fun_prop: n/a, equality of numbers, not a function-property goal.
- [2.5] positivity: n/a, goal is equality to zero, not a sign/nonzero assertion.
- [2.6] gcongr: n/a, no inequality or monotonicity subgoal.
- [2.7] lia/omega: n/a, target is a real-valued finite-sum equality, not Nat/Int arithmetic.
- [2.8] aesop: live attempt fails with no progress.
- [2.9] norm_num/norm_cast: `norm_num [weight]` succeeds but is longer than `simp [weight]`; no cast-normalization chain exists.
- [2.10] decide: n/a, arbitrary real sum with arbitrary index type is not a closed decidable computation.
- [2.11] field_simp/ring: tested `unfold weight; field_simp; ring`; field_simp is not imported and the attempt fails. No new import justified for a longer route to zero summands.
- [2.12] linear_combination: n/a, no ring-ending proof or algebraic hypotheses to combine.
- [2.13] wlog: n/a, no symmetric cases.
- [2.14] calc composition: n/a, no calc.
- [2.15] `<;>`: n/a, a single goal closed by a single tactic.
- [3.1] erw to rw: n/a, no erw.
- [3.2] legacy function tactics: n/a, none present.
- [3.3] omega to lia: n/a, neither occurs; arithmetic route is inapplicable.
- [3.4] rcases/rfl substitution: n/a, no case elimination.
- [3.5] automation attributes: existing `@[simp]` is the correct zero-evaluation rule; preserved.
- [3.6] simp_all only: n/a, no simp_all and no local propositions to simplify.
- [3.7] heartbeat options: n/a, no options to remove.

## Step 4 — step back

The original proof already has one tactic. Bare simp and reflexivity fail, so
the definition-unfolding argument is necessary. `exact?` fails; `apply?` only
produces open side goals. Generic sum-zero term proofs need a per-coordinate
zero proof and are longer than the existing terminal simp. No have blocks,
redundant steps, duplicated branches, or missing API extraction signals exist.
Keep `simp [weight]` and make only the approved assumption cleanup.

## Step 5 — verification and gates

- Actual `/Users/ramin/.elan/bin/lake build Roth.Box` exited 0, session 26474;
  log `/private/tmp/roth-box-d07-module.log`, 1154 jobs.
- Full native `lean_diagnostic_messages`: `success: true`, `partial: false`,
  `timed_out: false`; no errors, no target warnings. The 16 remaining warnings
  concern later declarations and the known unchanged copyright header.
- Native independent snippet imports only mathlib, defines an isolated copy of
  the unchanged finite-sum definition, and proves the selected simp proof with
  `[Fintype σ]` and no DecidableEq. It succeeds without importing/calling this
  project theorem. Scratch formatting warnings do not concern the source file.
- Native post-build `#check` confirms the final type above; a direct application
  `Roth.weight_zero r` without DecidableEq elaborates. Deliberately rejected
  Fintype-drop and Finite-replacement probes fail as recorded above.
- Native `lean_verify`: standard trust, axioms `propext`, `Classical.choice`,
  `Quot.sound`; no nonstandard axioms or source-scan warnings.
- `git diff --check -- Roth/Box.lean` exited 0. Exact worker diff adds only
  `omit [DecidableEq σ] in` immediately before the existing docstring.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit 0, cited above. |
| definition_protected | pass | No definition or abbreviation changed. |
| theorem_statement_protected | pass | Textual theorem line/conclusion/explicit binder unchanged; only user-approved unused section instance removed, audited at item 18. |
| structure_gate | pass | One proof line, no conjunction or branches. |
| naming_gate | pass | Descriptive snake_case function/argument name, no forbidden patterns. |
| line_packing_gate | pass | Complete one-row width table, 54 codepoints, no dangling signature token. |
| inequality_orientation_gate | pass | Complete scan table; zero reversed inequalities. |
| documentation/comment preservation | pass | Docstring and simp attribute byte-identical; no inline comments existed. |
| trust | pass | Standard three axioms, no sorry or source warnings. |

Overall worker gates: pass. Full project and separate LeanEval checkpoints are
parent responsibilities after this frozen source; this report does not claim
their completion in advance.

## Step 6 — result

Before: 2 declaration lines. After: 2 declaration lines. Saved: 0 lines.
One scoped omission command adds one source line. Audit issues found/fixed: 1/1
(two associated diagnostics). No proof-golf churn applied. Renames queued: none.
Comments preserved: none present; existing docstring preserved. Refactoring: none.

- [x] Step 1 — required references read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — five-method search status and fallback limitations recorded.
- [x] Step 2.6 — every parameter audited, actual drop checks and public literature included.
- [x] Step 2.7 — complete measured signature-width table.
- [x] Step 2.8 — complete inequality scan table.
- [x] Step 3 — all 42 golfing rules have concrete statuses.
- [x] Step 4 — whole-proof and alternative-strategy reflection.
- [x] Step 5a — complete native diagnostics; no errors or target warnings.
- [x] Step 5b — actual module build, diff gates, type/isolated proof/trust checks.
- [x] Step 6a — no rename needed, so rename sidecar untouched.

Source ownership released after successful module/LSP checks; report ownership
released on worker completion.

Publication verification: full `lake build` session 79655 exited 0 (2586 jobs;
`/private/tmp/roth-box-d07-full.log`); separate `lake build Roth.LeanEval` session 57725
exited 0 (2585 jobs; `/private/tmp/roth-box-d07-leaneval.log`). All affected dependents pass.
