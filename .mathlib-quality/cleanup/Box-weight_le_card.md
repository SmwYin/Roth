# `Roth.weight_le_card` — declaration 11/14

Dedicated fresh worker `/root/cleanup_continuation/box_file/decl11`.
Baseline: `d196a3f`; original declaration lines 103–106; final lines 104–107.
Scope: this theorem and this report only. The parent owns the required Index caller update
and the full project / separate LeanEval build checkpoints.

## Result

Removed the unused positivity hypothesis `hr : ∀ j, 0 < r j` and the unused section
instance `[DecidableEq σ]`, as explicitly approved by the user (“Follow your recommendation”).
The conclusion, remaining binders, theorem name, visibility, and docstring are unchanged.
Normalized the proof lambda to `↦`. The existing sum comparison already handles zero
denominators through Lean's total division, so no extra case split is needed.

Before: 4 declaration lines. After: 4 declaration lines. Saved: 0 lines; the scoped
`omit` adds one surrounding command line. Three target warnings removed.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, and the relevant style sections.
The full worker prompt was read from `/private/tmp/roth-box-declaration-worker.md`.
The Lean 4 and mathlib-quality skills govern preservation and the audit below.

## Full audit (24 items)

1. **LINT:** baseline has unused `hr`, unused section `DecidableEq σ`, and unused
   decidability in theorem type. All three are gone in complete final diagnostics.
2. **HAVE SCAN:** none: the proof is a composed sum inequality and equality.
3. **SET_OPTION:** none in the declaration; no options added.
4. **SIMP SQUEEZE:** the sole `by simp` closes the constant-sum equality. Keep terminal
   simp unsqueezed; no nonterminal simp exists.
5. **NAMING:** `weight_le_card` describes its ordered conclusion in snake_case. `card`
   matches `Fintype.card`; no forbidden abbreviation, number scheme, `_ge_`, `_gt_`,
   single-letter public name, or numbered auxiliary suffix. No rename needed.
6. **LINE PACKING:** both signature lines measured below; their combined length is 102,
   exceeding 100, so the break is necessary.
7. **BY PLACEMENT:** outer proof is term mode; both short tactic proofs follow their `by`
   on the same line. No standalone `by`.
8. **FORMAT:** two-space proof indentation, four-space continuation, no blank proof lines,
   no semicolon chains, `haveI`, or `letI`. Replace ordinary lambda `=>` with `↦`.
9. **COMMENTS:** no inline proof comments existed; none removed.
10. **DOCSTRING:** existing public statement and source reference preserved byte-for-byte.
11. **VISIBILITY:** public theorem is used in `Roth/Index.lean:241`; retain public visibility.
12. **STRUCTURE:** two proof lines, no conjunction or case branches; no helper extraction.
13. **MATHLIB:** generic sum comparison and division bounds already provide the proof;
    five-method results below. No new helper or duplicate API introduced.
14. **JUNK DEF:** n/a: theorem, not a definition.
15. **EXISTS LEMMA:** n/a: neither private nor existential.
16. **SHOW vs CHANGE:** none.
17. **PUSH_NEG:** none.
18. **GENERALISE:** remove exactly the two approved unused assumptions; retain the
    mathematically necessary coordinate bound and finite indexing structure. Table below.
19. **INEQUALITY:** all statement/hypothesis inequalities use `<` or `≤`; occurrence table below.
20. **NORMAL-FORM:** `weight r d ≤ Fintype.card σ` is the advertised upper bound, with
    natural-to-real cardinality coercion inferred. No alternative normal form needed.
21. **SYNTAX-GEN:** approved removal makes application simpler. `hd` already accepts the
    coordinatewise proof supplied by the Index caller. Replacing it with function-order
    notation would not remove any caller obligation and is outside approved API changes.
22. **IMPORT-FANOUT:** n/a: no new imports or dependencies.
23. **CASTS:** 0 explicit casts dropped, 0 new explicit cross-type casts, 0 new load-bearing
    ascriptions. Existing `exact_mod_cast` transports the necessary ℕ inequality to ℝ.
24. **INSTANCE-NAME:** n/a: no instance declaration or named local instance.

Issues found: unused positivity, unused decidability, lambda syntax; all fixed.
Refactoring needed: parent must remove the one obsolete `hr` argument at the Index caller,
as already authorized and assigned. No Phase 5 rename or mathematical generalization queued.

## Mathlib search-status (five methods)

| Method | Query / evidence | Result |
|---|---|---|
| A: Lean-Finder | “finite sum of real numbers bounded by one is at most cardinality” | Found `Finset.sum_le_card_nsmul`, plus reverse and ENNReal bounds. |
| B: Loogle | `Finset.sum, _ ≤ _ * _` | Found `Finset.sum_card_le`, `sum_card_inter_le`, and square bounds; these have different conclusions. |
| C: LeanSearch | Inherited service diagnosis: HTTP 500 | Unavailable; not used as absence evidence or repeatedly retried. |
| D: local source | `sum_le_card`, `sum_le_sum`, `sum_const`, `div_le_one_of_le₀` | Confirmed sum bound in `Algebra/Order/BigOperators/Group/Finset.lean`; generated additive lemma at line 285; related division bound in `Algebra/Order/Field/Basic.lean`. |
| E: name-pattern search | Native `lean_local_search` query `sum_le_card` | Empty with `index: unavailable`; not absence evidence. Source and compiled checks supply fallback. |

Auxiliary variants inspected: `sum_le_card_nsmul`, `card_nsmul_le_sum`, `sum_le_sum`,
`sum_card_le`, and `div_le_one_of_le₀`. The common-equivalents table's topology/finite-set
intersection buckets do not apply; this is an ordered finite sum.

Compiled checks confirmed `Finset.sum_le_card_nsmul` and `div_le_one_of_le₀`.
A trial `Fintype.sum_le_sum` is unavailable in this checkout, so it was rejected in scratch.
Conclusion: partial generic matches; retain this public project-weight theorem and use the
existing mathlib proof. Removing public API is outside this worker's authorized scope.
No claim that mathlib lacks a generic equivalent is made. No API-extraction signal appears:
the original proof is already two direct lines with no wrapper plumbing.

## Generalisation status

| Parameter | Class / role | Candidates checked | Result |
|---|---|---|---|
| `{σ : Type*}` | type-variable, indexes both data and finite sum | Universe check; drop would leave `σ` unbound | Already universe polymorphic (`u_1` in `#check`); retain. |
| `[Fintype σ]` | typeclass, finite sum and cardinality | Drop compiled in scratch with `autoImplicit false`; finite-only would need a new cardinality formulation | Drop fails to synthesize `Fintype σ` in both `weight` and `Fintype.card`; retain. |
| `[DecidableEq σ]` | decidability, unused | Drop in independent proof and live scoped `omit` | Both compile; approved removal applied. |
| `{r : σ → ℕ}` | structure value, denominator vector | Drop is ill-scoped because conclusion contains `r`; changing ℕ needs redefining weight | Retain; no standalone weakening applicable. |
| `(hr : ∀ j, 0 < r j)` | proposition, unused | Drop before any strict-to-weak variant | Strongest weakening compiles; approved removal applied. A weak positivity premise would be redundant. |
| `{d : σ →₀ ℕ}` | structure value, numerator multi-index | Drop is ill-scoped because conclusion and `hd` contain `d`; arbitrary functions require API restatement | Retain existing weight domain. |
| `(hd : ∀ j, d j ≤ r j)` | proposition, supplies each ratio bound | Drop checked by certified counterexample; pointwise notation offers no weaker bound | Necessary: Unit, `r=1`, `d=single () 2` violates the conclusion; `simp [weight]` proves the negation. Retain. |

Inversion check: after expanding the definition, this is the abstract finite-sum bound.
That API already exists as `Finset.sum_le_sum` / `sum_le_card_nsmul`; no new abstraction
is warranted. A general ordered-field weight construction would change the definition
and many signatures; it is not part of the user's bounded approval. No such change queued.

## Public literature status

Web query: “finite sum bounded by cardinality monotonicity summation generalization”.
Top three returned entries: Pearson's finite-series study guide, the research article
“A fundamental inequality for the sum of sets of m-tuples”, and Papadimitrakis's measure
theory notes. The latter two are about different cardinality/summability questions; no
new premise removal is inferred from them.

Follow-up queries: `site.leanprover-community.github.io/mathlib4_docs "sum_le_card_nsmul"`
and `site.en.wikipedia.org Summation identities inequality monotonicity`.
The official-source search returned [mathlib's Chebyshev source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Order/Chebyshev.lean),
the [mathlib Behrend port record](https://leanprover-community.github.io/mathlib-port-status/file/combinatorics/additive/behrend),
and [the community finite-sum bounds discussion](https://leanprover-community.github.io/archive/stream/217875-Is-there-code-for-X%3F/topic/Finset.20sum.20bounds.html).
These identify uses of the generic cardinality bound; the checked local source is the
authority for this checkout. The encyclopedia query returned Summation, Chebyshev's sum
inequality, and List of mathematical identities; no broader project-specific claim drawn.
The local primary manuscript `clean.tex:666–667` states the coordinate bound and weight at
most the number of variables. The approved zero-denominator extension is established by
the Lean proof, not by an unsupported literature attribution.

ChatGPT math MCP: n/a, no callable math connector is installed (tool inventory checked).
Literature-driven additional API changes: none proposed within the approved scope.

## Line packing

Final `#check` at `format.width = 100`:

```lean
@weight_le_card : ∀ {σ : Type u_1} [inst : Fintype σ] {r : σ → ℕ} {d : σ →₀ ℕ},
  (∀ (j : σ), d j ≤ r j) → weight r d ≤ ↑(Fintype.card σ)
```

| Signature line | Codepoints | Next complete signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| Baseline 103 | 91 | `weight r d ≤ Fintype.card σ :=` (30) | 91 + 1 + 30 = 122 > 100 | ok |
| Baseline 104 | 34 | none; proof begins | n/a | ok |
| Final 104 | 71 | `weight r d ≤ Fintype.card σ :=` (30) | 71 + 1 + 30 = 102 > 100 | ok |
| Final 105 | 34 | none; proof begins | n/a | ok |

Final proof widths: 99 and 13; all lines are at most 100 codepoints.

## Inequality scan

| Occurrence | Location | Orientation / action | Rename? |
|---|---|---|---|
| `0 < r j` | baseline `hr` | Already correct; entire unused hypothesis removed with approval | no |
| `d j ≤ r j` | `hd` | Correct, retained | no |
| `weight r d ≤ Fintype.card σ` | conclusion | Correct, retained | no |
| reversed `≥` / `>` | entire final signature | None | no |

## Golfing rule pass (42 rules)

- [1.1] `by exact`: n/a; outer proof is already term mode.
- [1.2] `by rfl`: n/a; absent.
- [1.3] `rw + exact`: n/a; no rewrites.
- [1.4] `simp + exact`: n/a; terminal simp only.
- [1.5] trailing `rfl`: n/a; absent.
- [1.6] constructor combination: n/a; no constructors.
- [1.7] apply/exact combination: n/a; already direct lemma application.
- [1.8] contradiction: n/a; no contradiction argument.
- [1.9] eta reduction: lambda has an intentionally ignored membership argument and
  constructs a division bound; no eta-redex. Lambda arrow normalized.
- [1.10] single-use have: n/a; none.
- [1.11] apply/intro: n/a; none.
- [1.12] redundant show: n/a; none.
- [1.13] have/projections: n/a; none.
- [1.14] merge rw: n/a; no rewrites.
- [1.15] unsqueeze terminal simp: already unsqueezed.
- [1.16] squeeze nonterminal simp: n/a; no nonterminal simp.
- [1.17] dot notation: `.trans_eq` already used.
- [1.18] `<|`: existing parentheses are required around the expression before `.trans_eq`;
  the final `(by simp)` is only 9 characters and compiles unchanged.
- [1.19] push Not: n/a; no negation tactic.
- [1.20] inline existential lemma: n/a; not existential.
- [2.1] grind: tried live and independently as `grind [weight]`; fails to prove the bound.
- [2.2] delete before grind: n/a; selected proof contains no grind.
- [2.3] simpa consolidation: `simpa [weight] using Finset.sum_le_card_nsmul ...` compiles,
  but needs an explicit ratio function, bound, and membership lambda; longer than retained proof.
- [2.4] fun_prop: n/a; no analytic function-property goal.
- [2.5] positivity: existing denominator nonnegativity subproof compiled independently.
- [2.6] gcongr: independently closes the cast inequality from `hd`; same-length tactic
  replacement provides no benefit over the explicit cast transport, so retain `exact_mod_cast`.
- [2.7] lia/omega: n/a; main goal is a real sum/division inequality, not Nat/Int arithmetic;
  the only Nat inequality is exactly `hd j`.
- [2.8] aesop: tried live and independently; makes no progress.
- [2.9] norm_num/norm_cast: exact_mod_cast already solves the cast-only premise; no numeric
  constants or redundant casts in the main theorem to normalize.
- [2.10] decide: n/a; arbitrary real weighted inequality is not closed finite computation.
- [2.11] field_simp/ring: n/a; not an algebraic identity, and denominators may be zero.
- [2.12] linear_combination: n/a; no ring-ending block or polynomial equality.
- [2.13] wlog: n/a; no symmetric cases.
- [2.14] collapse calc: proof already composes the inequality and equality via `.trans_eq`.
- [2.15] common goal closure: n/a; no repeated tactic branches.
- [3.1] erw/rw: n/a; neither present.
- [3.2] continuity/measurability: n/a; neither present.
- [3.3] omega/lia: n/a; no arithmetic solver in selected proof.
- [3.4] rfl substitution: n/a; no rcases.
- [3.5] automation attributes: conditional upper bound is not a simplification equation;
  no new global automation registration justified by this cleanup.
- [3.6] simp_all: n/a; no simp_all only; a whole-goal simp attempt leaves the sum bound.
- [3.7] maxHeartbeats: n/a; no resource options to remove.

## Step back / actual experiments

The original two-line proof, with neither removed assumption present, compiled independently.
`grind [weight]`, `simp [weight]`, `aesop`, and `exact?` did not close the whole goal.
Live `apply?` offered partial order-theory routes, not a closed proof. That live multi-attempt
replacement also left the second term continuation and produced a parser error; it is not
counted as a successful compiled alternative. Independent scratch proofs supplied the clean
positive evidence and repeated the important failing whole-goal tactics.
The alternative `sum_le_card_nsmul` proof compiled but was longer. A guessed
`Fintype.sum_le_sum` was rejected as unknown in scratch. No guessed identifier entered source.
The retained proof directly expresses “each ratio is at most one, then sum”; no extraction
or alternative proof strategy improves it under the fixed definition.

## Verification and diff gates

`/Users/ramin/.elan/bin/lake build Roth.Box` exited **0** (session **28240**), reporting
1154 jobs. Log: `/private/tmp/roth-box-d11-module.log`.
Complete native diagnostics: `success=true`, `partial=false`, `timed_out=false`; no errors,
no target warnings. Remaining warnings concern later declarations and the preserved header.
Native `lean_verify`: standard axioms `propext`, `Classical.choice`, `Quot.sound`, no
nonstandard axioms, no suspicious source patterns. A separate `#print axioms` agrees.
The final independent proof does not reference `Roth.weight_le_card`; it compiles with
only `[Fintype σ]` and `hd`, proving isolation and both approved removals.
`git diff --check` passed. The diff changes only this theorem's scope/signature/lambda;
existing comments, definitions, and other declarations are untouched by this worker.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module invocation and exit 0 above |
| definition_protected | pass | No definition/abbreviation changes |
| theorem_statement_protected | pass, authorized exception | Exactly approved `hr`/DecidableEq removals; same conclusion and remaining binders |
| structure_gate | pass | 2 proof lines; no conjunction or large branches |
| naming_gate | pass | Descriptive inequality name; no forbidden pattern |
| line_packing_gate | pass | Both signature lines measured; joining is 102 codepoints |
| inequality_orientation_gate | pass | No reversed inequalities; occurrence table complete |

Overall: pass. Full project and separate LeanEval builds are parent-owned, not claimed here.

## Completion checklist

- [x] Step 1: reference docs read.
- [x] Step 2: all 24 audit items reported.
- [x] Step 2.5: five-method mathlib search with explicit service limitations.
- [x] Step 2.6: all parameters considered; approved weakening verified; literature recorded.
- [x] Step 2.7: every signature line measured.
- [x] Step 2.8: inequality scan recorded.
- [x] Step 3: all 42 golfing rules have a concrete status.
- [x] Step 4: whole-proof alternatives and independent positive proof checked.
- [x] Step 5a: complete clean elaboration, target warnings removed.
- [x] Step 5b: actual module build, type/axiom/isolation and diff gates passed.
- [x] Step 6a: no rename required; no rename sidecar mutation.
- [x] Step 6b: report complete; source ownership released to parent.

Comments preserved: unchanged docstring; no inline proof comments existed.
Refactoring deferred: no new mathematical work; the single authorized caller repair and
dependent builds remain with the parent checkpoint owner.

Parent compatibility verification: removed only the obsolete `hr` argument at
`Roth/Index.lean:241`. Complete native Index LSP success=true, partial=false, no errors.
Its own unchanged `index_le_card` signature now exposes an unused hr warning; that
separate declaration remains for the future Index worker, with no warning suppression.

Publication verification: full `lake build` session 7727 exited 0 (2586 jobs;
`/private/tmp/roth-box-d11-full.log`); separate `lake build Roth.LeanEval` session 44525
exited 0 (2585 jobs; `/private/tmp/roth-box-d11-leaneval.log`). All affected dependents pass.
