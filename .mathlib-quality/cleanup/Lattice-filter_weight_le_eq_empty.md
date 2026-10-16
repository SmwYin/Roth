# Phase 4 — `Roth.filter_weight_le_eq_empty`

Scope: only the private declaration at `Roth/Lattice.lean:137–139`.
Source frozen at SHA256 `ff720f72959dc95143cec984113dd0fe3fef768e5757b8854a2eedbc90602dc7`.
The owner revoked source ownership after readiness; this worker makes no further source edits.

## Result

Changed the two ordinary lambda arrows from `=>` to `↦`. Mathematical statement,
parameters, name, visibility, proof strategy, public API, documentation, imports and header
are preserved. Before: 3 lines; after: 3 lines; saved: 0 lines.
No new identifiers, axioms, options, attributes, limits, suppressions or helpers.
Issues: two lambda-style occurrences fixed. Refactoring needed: none. Renames queued: none.
Comments preserved: none present in the target; all surrounding documentation untouched.

## Preparation and baseline

Read the lean4 and mathlib-quality skills, the complete Phase-4 worker instructions in
`/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`, golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns and cleanup-gates; consulted the
relevant declaration/lambda/visibility/formatting and naming sections of style-rules and
naming-conventions. Confirmed reference reading in commentary before editing.
Read the source immediately before a contextual three-line patch; no whole-file write.
Owner supplied baseline: full build and separate LeanEval, both exit 0, session 46779;
84.53s and 29.47s, logs `/private/tmp/roth-lattice-helper-fiber-{full,leaneval}.log`.
Native LSP baseline elaboration completed successfully; only the known file-header warning.

## Full audit (24 items)

| # | Item | Concrete disposition |
|---|---|---|
| 1 | LINT | No declaration diagnostics. Complete file LSP has only the existing L1 copyright-header warning, preserved by user instruction. |
| 2 | HAVE SCAN | No `have` declarations. |
| 3 | SET_OPTION | None in target or file; no limits introduced. |
| 4 | SIMP SQUEEZE | No simp invocation in target. |
| 5 | NAMING | `filter_weight_le_eq_empty` describes a filtered weight sublevel set equal to the empty set; snake_case; no forbidden abbreviation, numeric scheme, or `_ge_`/`_gt_`. No rename necessary. |
| 6 | LINE PACKING | Both signature lines measured below; first is 98 codepoints and cannot absorb the 64-codepoint conclusion. |
| 7 | BY PLACEMENT | Inline `by linarith` follows the lambda arrow on the same line. |
| 8 | FORMAT | Two lambda arrows corrected to `↦`; 4-space signature and 2-space term-proof indentation; no blank proof lines or semicolons. |
| 9 | COMMENTS | No inline target comments; surrounding comments and docstrings preserved. |
| 10 | DOCSTRING | Private standard property: a new docstring is unnecessary. |
| 11 | VISIBILITY | Correctly private, with two calls in `card_filter_weight_le`; no external callers. |
| 12 | STRUCTURE | One-line term proof containing one arithmetic tactic; no conjunction, long branch, or extraction need. |
| 13 | MATHLIB | Five actual routes below; existing `Finset.filter_eq_empty_iff` already supplies the generic step. |
| 14 | JUNK DEF | Not a definition. |
| 15 | EXISTS LEMMA | Not existential or single-use; two callers. |
| 16 | SHOW/CHANGE | Neither occurs. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every parameter drop tested; strict-to-weak tested and refuted below. |
| 19 | INEQUALITY | No reversed inequalities; occurrence table below. |
| 20 | NORMAL-FORM | Equality to `∅` is the form required by both rewriting call sites; underlying generic criterion is `Finset.filter_eq_empty_iff`. |
| 21 | SYNTAX-GEN | Existing explicit `r` and implicit dimension/threshold support the two `rw` calls directly; no useful caller-facing restatement. |
| 22 | IMPORT-FANOUT | No import changes. |
| 23 | CASTS | Zero redundant casts dropped; both `(m : ℝ)` occurrences are genuine natural-to-real casts (one in assumption, one in conclusion). No new casts. |
| 24 | INSTANCE-NAME | No instance declaration. |

## Mathlib search status

All five methods were actually invoked in this worker session.

| Method | Query | Observed outcome |
|---|---|---|
| A Lean-Finder | “A finite set filtered by a predicate is empty if the predicate is false for every element” | Native tool read timeout; recorded as unavailable evidence, not absence. |
| B Loogle | `Finset.filter _ _ = ∅` | `Finset.filter_false`, `filter_empty`, `filter_false_of_mem`, `filter_eq_empty_iff`. |
| C LeanSearch | “A finset filtered by an impossible predicate is empty” | `Finset.filter_false_of_mem`, `filter_False`, `filter_false`. |
| D Source | Untruncated `rg` for `filter_eq_empty`, `filter_weight_le_eq_empty`, `weight_nonneg` in Finset filter and project sources | Generic iff at Filter.lean:159; `filter_false_of_mem` at 169; project-specific weight nonnegativity at Box.lean:69; exactly two target calls. |
| E Name pattern | `lean_local_search` query `filter_eq_empty` | Finset source hit (tool reports its name with repeated Finset namespace); index unavailable, so no absence inferred. |

Auxiliary variants inspected: `filter_false_of_mem`, `filter_false`, `filter_empty`.
Both relevant generic types were independently compiler-checked with `#check`.
Common-equivalents table: no disguised topology, boundedness or finiteness concept.
Conclusion: partial generic match already used. The remaining content is the project-specific
nonnegative weight contradiction at a negative threshold, with two current callers.
This is not a duplicate of a generic mathlib theorem: it packages a domain fact about `Roth.weight`.
The no-wrapper rule does not justify deleting this repeated domain reasoning; replacing it
would duplicate the arithmetic argument in two branches. No new optional abstract API has
current-caller benefit. No public extraction or mathlib absence claim is made.
Compiled discovery probes: `exact?` could not close the arithmetic contradiction; `apply?`
produced only unrelated partial refinements and incomplete/sorry diagnostics, never a completed
replacement. These experiments did not mutate the source.

## Generalisation status

Native `lean_run_code` executed all five mechanical probes with `autoImplicit false` and
`import Roth.Lattice`; each expected failure was returned with `timed_out = false`.

| Parameter | Class / use | Candidate actually tested | Result |
|---|---|---|---|
| `{m : ℕ}` | Dimension; domain of `r`; cast in threshold and bound | Drop binder | Rejected: unknown `m` in dependent type and threshold. No universe or class weakening applies to a concrete natural number. |
| `(r : Fin m → ℕ)` | Structure value; box and weight parameter | Drop binder | Rejected: unknown `r` in conclusion and weight nonnegativity. No global predicate or class to localise. |
| `{lam : ℝ}` | Scalar threshold; occurs in conclusion and assumption | Drop binder | Rejected: unknown `lam` in assumption and conclusion. Changing the scalar structure needs a new weight API, not a binder weakening. |
| `(hlam : (m : ℝ) < lam)` | Proposition; ensures strictly negative threshold | Drop; weaken `<` to `≤` | Both rejected by `linarith failed to find a contradiction`. |

The strict weakening is mathematically false: an independent compiled example proves the
filtered box is nonempty for `m = 0`, `r = fun _ : Fin 0 ↦ 0`, `lam = 0`:

```lean
example : ¬ ((box (fun _ : Fin 0 ↦ 0)).filter
    (fun d ↦ weight (fun _ : Fin 0 ↦ 0) d ≤ ((0 : ℝ) - 0) / 2) = ∅) := by
  simp [box, weight]
```

Inversion diagnostic: the argument uses nonnegativity of weight; an abstract finite-set
lemma for a nonnegative function is possible, but `Finset.filter_eq_empty_iff` already
provides the reusable logical API. Adding another abstraction would not improve either
current caller, and is closed as optional scope. No assumption change retained.
Literature search: n/a — private declaration, literature search not required by Phase 4.

## Line packing

Actual native `lean_run_code`, `format.width := 100`, independent exact-type clone:

```text
@emptyClone : ∀ {m : ℕ} (r : Fin m → ℕ) {lam : ℝ}, ↑m < lam → {d ∈ box r | weight r d ≤ (↑m - lam) / 2} = ∅
```

The reference output uses binder/filter notation; the source binder line includes the
private declaration name and named hypothesis, which account for the different wrapping.

| Signature line | Codepoints | Next complete signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 137 | 98 | Entire conclusion through `:=`, 64 codepoints after indentation removed | 98 + 1 + 64 = 163 > 100 | ok |
| 138 | 68 | None; proof body follows | n/a | ok |

The first syntactic fragment `(box r).filter` alone is 14 codepoints:
98 + 1 + 14 = 113 > 100, independently justifying the break even without treating
the whole conclusion as a token. Proof line 139 is 74 codepoints. No repacking required.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | Whole signature | No `≥` or `>` occurrence | None | None |

The assumption uses `<`, and the filtered predicate uses `≤`, both smaller-side-first.

## Golfing rule pass (42 rules)

| Rule | Status |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | n/a: no `rw` followed by `exact`. |
| 1.4 | n/a: no simp/exact chain. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor proof. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction setup or push_neg chain. |
| 1.9 | n/a: neither lambda is an eta expansion; predicate uses subtraction/division and proof lambda discharges hypotheses. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: already term application followed by lambda, no apply/intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no have/projection pair. |
| 1.14 | n/a: no rw. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | Existing iff projection `.2` is concise; no improvement. |
| 1.18 | Already a trailing lambda without parentheses; no `<|` opportunity. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not an existential helper. |
| 2.1 | `by grind [weight_nonneg]` at the arithmetic term completed without diagnostics. Retained existing one-tactic linarith: same structure and size, direct linear arithmetic, no demonstrated improvement. |
| 2.2 | n/a: no preceding tactics before grind, and no grind retained. |
| 2.3 | n/a: no simp plus closing tactic; tested `by simp_all` failed to make progress. |
| 2.4 | n/a: no function-property goal. |
| 2.5 | n/a: goal is False from an upper bound and strict threshold, not positivity. |
| 2.6 | n/a: no monotone calc chain; arithmetic contradiction. |
| 2.7 | n/a: real linear arithmetic, not natural/integer Presburger arithmetic. |
| 2.8 | Tested `by aesop`: failed, made no progress. |
| 2.9 | n/a: symbolic real bound, no numeric/cast computation to normalize. |
| 2.10 | n/a: arbitrary real inequality, not decidable finite computation. |
| 2.11 | n/a: no algebraic identity; division is by constant 2 and linarith handles it. |
| 2.12 | n/a: proof does not end in ring/ring_nf. |
| 2.13 | n/a: no symmetric cases. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: no multiple generated goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega; symbolic real arithmetic. |
| 3.4 | n/a: no rcases or substitution. |
| 3.5 | No attribute added: private threshold helper is used explicitly in two rw calls; no automation registration benefit. |
| 3.6 | n/a: no simp_all only; tested simp_all did not close. |
| 3.7 | n/a: no maxHeartbeats option. |

Native live attempts first targeted the wrong term column and returned unknown-identifier
errors for unwrapped tactics; corrected immediately to column 43 and `by ...` term snippets.
Only the corrected outcomes above are used as proof evidence. Initial scratch probes importing
only Roth.Box lacked the linarith tactic; reran all parameter probes with Roth.Lattice.
An initial exact-clone run during the module rebuild reported outdated imports; rerun after
the successful build completed cleanly. These were scratch/tool-position issues, never
source proof failures.

## Step back and independent verification

The proof is already a one-line term plus one arithmetic tactic, and both lambda arrows are
now idiomatic. Changing to grind gives no shorter proof and adds no clarity. The two uses
justify retaining the domain helper. No extraction, additional lemma or API restatement.

Native `lean_run_code` compiled an independent theorem `emptyClone` with the original exact
type and the same non-self proof (`Finset.filter_eq_empty_iff.2` plus weight_nonneg/linarith).
It did not call the target. Width-100 #check and #print axioms succeeded; its axioms were
`propext`, `Classical.choice`, `Quot.sound`. The zero-threshold counterexample compiled too.
Native `lean_verify` of actual private `Roth.filter_weight_le_eq_empty`, with source scan,
returned `trust = standard`, those same three axioms, no nonstandard axioms and no warnings.

## Gates

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Lattice`, exit 0, Built Roth.Lattice (35s), 2214 jobs. Only known header warnings in Box and Lattice. |
| definition_protected | pass | No definition or abbreviation changes. |
| theorem_statement_protected | pass | Only equivalent lambda-arrow syntax; original exact-type clone independently compiled. All parameters and mathematical expressions identical. |
| structure_gate | pass | One-line term proof, one inner tactic, no conjunction/branches. |
| naming_gate | pass | Descriptive snake_case with no forbidden patterns or abbreviations. |
| line_packing_gate | pass | Both signature rows measured above; max 98. |
| inequality_orientation_gate | pass | Zero reversed inequalities. |
| diagnostics | pass | Complete native LSP: partial false, success true, timed_out false; sole known L1 header warning. |
| standard_axioms | pass | Actual private theorem native verification and independent clone both standard-only. |
| comments / identifiers | pass | No comments removed, no new identifiers; no source sorry/axiom/limits/TODO/FIXME matches. |
| cumulative callers | owner gate | Both private calls belong to successfully built Roth.Lattice; owner owns final full project and separate LeanEval gates. |

Overall declaration gates: pass. Final project-wide certification remains the owner's
post-freeze full build, separate LeanEval run and actual performance sweep.

## Phase checklist

- [x] Step 1 — reference docs read.
- [x] Step 2 — all 24 audit items recorded.
- [x] Step 2.5 — all five actual search routes recorded, including Finder timeout.
- [x] Step 2.6 — every parameter mechanically probed; strict weakening refuted.
- [x] Step 2.7 — width-100 #check and per-line packing arithmetic.
- [x] Step 2.8 — inequality scan table.
- [x] Step 3 — all 42 golf rules recorded.
- [x] Step 4 — holistic reconsideration and independent non-self proof.
- [x] Step 5a — complete LSP verification, only preserved header warning.
- [x] Step 5b — explicit gate block and actual module build.
- [x] Step 6a — no rename; no shared sidecar edits.

## Simplify and performance handoff

Manual holistic simplify review: PASS-THROUGH; no duplication worth another abstraction,
no quality or efficiency issue in the target. No built-in simplify callable is exposed.
No optional profile was run, per owner instruction to avoid delaying final gates.
Buzz performance status is deliberately not invented: owner performs the mandatory actual
final sweep after source freeze. No heartbeat limits were raised or removed.

Owner checkpoint: explicit source edit revocation before sequential full/separate LeanEval session67566; both exit0 (109.71s/40.64s), frozen hash stable. Logs `/private/tmp/roth-lattice-d08-{full,leaneval}.log`.
