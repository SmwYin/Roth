# Phase 4 — `Roth.card_filter_weight_le`

Worker scope: only this headline public declaration, its two newly extracted private proof helpers,
and this report. No Git operations or shared progress-file edits. Historical source checkpoint: `786d2720d050576b7a978e822d076ace9cfd7d4c223113c9b2bc17057de919e7`.
Owner applied the reported signature packing correction and refroze at
`97697192cf943554cec6fbc3735d556e63eb441571c2f30b39ff2f7b6e73883e`.
Source ownership remains revoked; this worker is report/probes-only. Historical build evidence
is distinguished below from the owner's pending corrected-hash renewal.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both SKILL.md files, the full Phase-4
worker prompt, and relevant statement, formatting, documentation, and naming references.

## Mathematical decomposition and result

The proof counts fibres of the last coordinate. When `lam ≤ 2 √m`, the full box already gives the
bound. Otherwise the one-dimensional case is empty; in higher dimension, the prefix-box induction
hypothesis applies with positive parameter `lam - 1 + 2i/r_last`. Sum those estimates, apply
`sum_inv_lt`, and cancel the nonzero square-root factors.

Extracted two private lemmas with meaningful mathematical statements:

* `card_filter_weight_le_of_le_sqrt_aux`: the full-box bound in the easy parameter range; no
  positivity hypothesis on `r` is needed. Eight declaration lines, four body lines.
* `card_filter_weight_le_succ_aux`: the fibre induction step for positive predecessor dimension;
  the induction hypothesis is specialized to the actual prefix box. Thirty-three declaration
  lines, twenty-five body lines, no long case branch. This contains the substantive summation
  argument, not a forwarding wrapper.

The public declaration is 47 → 17 lines, saving 30; its proof is 44 → 15 lines counting the
`:= by` line (43 → 14 body lines). Its largest successor branch has nine lines including its
branch header. Whole file: 205 → 218 lines (+13), accounting for the extracted helpers.
Public docstring, mathematical statement, explicit/implicit parameter order, imports, header,
and versions are preserved. Only statement whitespace and `=>` → `↦` notation changed.
No adjacent existing declaration changed. The owner will dispatch a separate fresh complete
worker for each new private lemma; these helpers are not counted as separately cleaned here.

## Full 24-item audit

1. LINT: complete native LSP returned `partial:false`, `success:true`; the sole warning is the
   inherited line-1 copyright/header warning, explicitly preserved by the user. No warning on
   the owned declaration or new helpers. The initial extraction compile exposed one missing
   coercion in the easy `calc`; fixed explicitly. An intermediate nonterminal `simp` was removed.
2. HAVE SCAN: original `hR : 1 ≤ R := hr _` has no `by` and one use: inline `hr _`.
   Original `hsq1 := Real.one_le_sqrt.2 ...` has no `by` and one use: inline into `linarith`.
   Original `hlami := fun i _ ↦ by ...` has proof content and was used once: move the proof
   directly to the positivity premise in the successor helper. Original `hs := sum_inv_lt ...`
   is transformed by `push_cast` and then used in the sum estimate: keep this local in the
   successor helper. Public proof now has no `have`.
3. SET_OPTION: no limit, trace, or suppression options existed or were added.
4. SIMP SQUEEZE: public zero case's `simp` is terminal and remains unsqueezed. The intermediate
   `simp; positivity` attempt generated an actual squeeze suggestion; replaced the pair with
   explicit `rw [..., card_empty, Nat.cast_zero]` followed by `positivity`.
5. NAMING: `card_filter_weight_le` states the filtered-cardinality bound in snake_case;
   no forbidden abbreviation, numerical scheme, `_ge_`, or `_gt_`. Both new helper names
   describe their hypotheses or successor step, are private, and use nonnumbered `_aux`.
6. LINE PACKING: measured all signature lines in codepoints, with explicit arithmetic below.
   A final first-line defect was found and reported under source freeze; owner corrected it.
   Corrected-hash table below now has only `ok` rows.
7. BY PLACEMENT: every `by` ends the preceding expression line, including nested proofs.
8. FORMAT: two-space proof indentation, no blank lines inside declarations, ordinary lambdas
   use `↦`; public nested arithmetic tactics are on separate lines. The easy helper's inherited
   `rw; push_cast; rfl` line is explicitly left for its dedicated fresh helper audit.
9. COMMENTS: no inline proof comments were present; none deleted. Module and public docstring
   preserved verbatim.
10. DOCSTRING: existing public mathematical statement and source citation preserved verbatim.
    No docstrings on the private helpers. No permission-dependent documentation rewrite attempted.
11. VISIBILITY: headline stays public; both extracted internal estimates are private. No API expansion.
12. STRUCTURE: headline body fourteen lines (fifteen counting `:= by`), no conjunction in the
    statement, no branch over ten lines. Extraction resolves the original forty-three-line proof.
13. MATHLIB: all five actual searches below; use `Finset.card_filter_le` directly for the generic
    filtered-cardinality step. Specialized Roth estimate retained; no exact equivalent established.
14. JUNK DEF: n/a, this declaration is a theorem; no definitions added or changed.
15. EXISTS LEMMA: n/a, neither public theorem nor new helper returns an existential witness.
16. SHOW vs CHANGE: no tactic-mode `show`. The successor helper's `show 0 ≤ ... by positivity`
    is a term providing a `linarith` premise and is retained in term position.
17. PUSH_NEG: no `push_neg` remains or was introduced. Public proof uses `lt_of_not_ge h` directly
    instead of mutating `h` with `push Not`.
18. GENERALISE: every public parameter mechanically tested below. No public API change retained.
19. INEQUALITY: all signature inequalities have the smaller expression on the left; occurrence
    table below. No `≥`/`>` or reversed-order name introduced.
20. NORMAL-FORM: cardinality cast to `ℝ`, additive normalized weight, and the bound's product
    agree with the existing callers and source lemma. No competing normal-form API added.
21. SYNTAX-GEN: existing explicit dimension/radius inputs and implicit real parameter are usable
    by callers. The specialized private induction hypothesis is smaller than the original global
    hypothesis. No alternative public restatement with current caller benefit found.
22. IMPORT-FANOUT: n/a, no import added or modified.
23. CASTS: public signature has four cross-type coercions/ascriptions (dimension twice,
    cardinality, radius); the branch condition has the dimension cast once. These five are
    `ℕ` → `ℝ`. The inner `(n + 1 : ℕ)` fixes the successor dimension before casting and is
    load-bearing grouping. No same-type cast added. Private-helper casts receive separate audits.
24. INSTANCE-NAME: n/a, no instance declarations, `haveI`, or `letI` in this work.

## Mathlib search-status

| Method | Actual query | Results and action |
|---|---|---|
| A Lean-Finder | `Number of points in box with sum of normalized coordinates less than half minus lambda lattice count` | `ZLattice.tsumNormRPowBound`, `BoxIntegral.unitPartition.admissibleIndex`, `Behrend.card_box`; different lattice/box estimates |
| B Loogle | `Finset.card (Finset.filter _ _) ≤ _` | `Finset.card_filter_le`, `Finset.card_filter_le_iff`, `Finset.sum_card_le`; first used directly |
| C LeanSearch | `Cardinality of lattice points in a box with small sum of normalized coordinates` | `Behrend.card_box`, two `ZLattice.covolume.tendsto_card_div_pow` variants; none gives this weighted threshold |
| D source search | `rg -n 'card_filter_weight_le|card_filter_le|lattice.*count'` in Finset/Card, Behrend and local source; full untruncated candidate-name scan of Mathlib | Generic card-filter bound found; no full-name hit for public theorem or either new helper |
| E name-pattern | `lean_local_search(query="card_filter", limit=10)` | Existing project statements, `Finset.card_filter_le` and `_iff`; index reported `unavailable`, so absence is NOT inferred from this tool |

Auxiliary variants checked: `card_filter_le`, `card_filter_le_iff`, `sum_card_le`,
`card_box`, `tsumNormRPowBound`, and lattice covolume counting limits. Common-equivalents lookup:
no discrete/compactness/metric bucket applies. Conclusion: partial Mathlib match, used directly;
keep the substantive specialized theorem. No claim that failed text search proves absence.
The native generic-route probes `exact?` and `apply?` both reached the default 200000-heartbeat
limit; `grind`, `simp`, and `aesop` did not solve it. No search failure was called a proof.

New external names are `Finset.card_filter_le` (Loogle/local/source plus successful compilation)
and `Nat.succ_le_succ` (successful compiled application replacing `omega`). New local helper names
are actual declarations in the owned diff. No unknown identifiers in production diagnostics.

## Generalisation status — every public parameter

The compiled scratch batch is `/private/tmp/lattice-main-batch.lean`; diagnostics are
`/private/tmp/lattice-main-batch.log`. `autoImplicit false` is set only in this scratch batch,
to prevent a removed value binder from being silently reintroduced as an implicit argument.
A preliminary drop-`m` probe without this setting compiled precisely because Lean inferred an
implicit `m`; this is an explicit-to-implicit API change, not elimination or a generalization.

| Parameter | Class/use | Mechanical candidates actually tested | Result |
|---|---|---|---|
| `(m : ℕ)` | dimension; controls `Fin m`, threshold and bound | drop | unknown `m` in dependent type, threshold, sqrt, induction; preserve |
| `(r : Fin m → ℕ)` | radius function; box, weight and product | drop | unknown `r` in positivity hypothesis and conclusion; preserve |
| `(hr : ∀ j, 0 < r j)` | positivity of every radius | drop; strict→weak `∀ j, 0 ≤ r j` | drop leaves unknown `hr`; weak form fails positive-radius premise of successor estimate; preserve |
| `{lam : ℝ}` | real threshold and denominator | drop | unknown `lam` in positivity and conclusion; preserve |
| `(hlam : 0 < lam)` | positive real parameter | drop; strict→weak `0 ≤ lam` | drop leaves unknown `hlam`; weak form fails zero-dimensional empty-filter premise and easy-bound positivity premise; preserve |

No typeclass parameters, universe variables, bundled structures, continuity hypotheses,
decidability parameters, or local-point variants exist here. Radius positivity is required at
every coordinate by the current induction, so localizing to a single coordinate would not
supply the prefix induction hypotheses. Arbitrary finite index sets or a probabilistic
reformulation change public types and are not mechanical weakenings. No such API proposed:
no current caller benefit, as directed by owner/user scope. Inversion check: the proof uses
specific box cardinality, fibre decomposition, normalized weights, and positive radii throughout
its extracted argument; it does not merely unfold a named concrete witness then forget it.

## Public literature search

Actual web queries: `Roth lemma lattice count estimate 2 sqrt m lambda multi indices
 generalization`; `"Takloo-Bighash" "Yin" "Formalizing" Roth`; `"Roth" "lattice count" lemma 8`;
`"Roth" "lattice" "Takloo-Bighash"`; `"Roth" "lattice points" "lambda" estimate integers`;
`site.wikipedia.org Hoeffding inequality bounded independent variables`.

The first general query's top three returned topics were Diophantine approximation/subspace
 theorem, quantitative subspace theorem, and a 1996 Acta Math paper; none established a
weakening of this lemma. Exact-title searches did not locate an indexed version of the supplied
local paper. The third query cluster returned concentration literature: Hoeffding inequality,
Hoeffding lemma, and concentration inequalities, followed by the primary paper
[On Hoeffding's inequalities](https://arxiv.org/abs/math/0410159).
That paper concerns bounded independent summands, providing a broader concentration context;
this does not establish an immediately applicable Mathlib replacement or a needed API change.
The exact primary source supplied by the project, `.mathlib-quality/references/clean.tex`
1050–1136, requires positive integer radii and positive lambda and proves precisely the
same full-box/effective-fibre split. The Lean statement already covers dimension zero too.
No public hypothesis weakening or caller-improving restatement was established by the search.
ChatGPT mathematical MCP: n/a, no such callable tool in the available tool inventory.
No additional literature-driven scope is proposed.

## Line packing — actual codepoint arithmetic

Actual reference from `set_option format.width 100; #check @Roth.card_filter_weight_le` in the
successfully compiled original-proof probe:

```lean
Roth.card_filter_weight_le : ∀ (m : ℕ) (r : Fin m → ℕ),
  (∀ (j : Fin m), 0 < r j) →
    ∀ {lam : ℝ}, 0 < lam → ↑{d ∈ Roth.box r | Roth.weight r d ≤ (↑m - lam) / 2}.card ≤ 2 * √↑m / lam * ∏ j, (↑(r j) + 1)
```

The pretty printer keeps its final proposition together beyond the requested width; source
line packing below is nevertheless measured independently at 100 codepoints.

| Original sig line | Chars | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 157 | 83 | `(hlam : 0 < lam)` (16) | 83 + 1 + 16 = 100 | repack binder |
| 158 | 22 | full LHS through `≤` (71; old `=>`) | 22 + 1 + 71 = 94 | repack |
| 159 | 75 | RHS with `:= by` (47) | 75 + 1 + 47 = 123 | ok |
| 160 | 53 | none | n/a | ok |

After the first repack (`=>` becomes `↦`):

| Frozen sig line | Chars | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 200 | 83 | `(hlam : 0 < lam)` (16) | 83 + 1 + 16 = 100 | owner correction pending |
| 201 | 93 | RHS with `:= by` (47) | 93 + 1 + 47 = 141 | ok |
| 202 | 53 | none | n/a | ok |

Owner applied the final correction and the worker remeasured actual source (SHA-256 above):

| Corrected sig line | Chars | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 200 | 100 | colon (1) | 100 + 1 + 1 = 102 | ok |
| 201 | 76 | RHS with `:= by` (47) | 76 + 1 + 47 = 124 | ok |
| 202 | 53 | none | n/a | ok |

The last line is 53 codepoints; byte-width counting would yield a different result because of
Unicode symbols. The owner is renewing module, complete-LSP, original-proof/type/axiom and
full/separate gates against corrected hash.

## Inequality occurrence scan

| Occurrence | Location | Expression | Action |
|---|---|---|---|
| 1 | `hr` | `0 < r j` | already correct |
| 2 | `hlam` | `0 < lam` | already correct |
| 3 | filter predicate | `weight r d ≤ ((m : ℝ) - lam) / 2` | already correct |
| 4 | outer conclusion | cardinality `≤` explicit bound | already correct |
| 5 | proof branch condition | `lam ≤ 2 * √...` | already correct |

Zero `≥`/`>` in signature/hypotheses; no `_ge_`/`_gt_` in theorem name. Lambda `=>` in the
old statement is syntax, not an order relation, and was independently changed to `↦`.

## All 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 by exact | n/a: no standalone `:= by exact` wrapper in headline |
| 1.2 by rfl | n/a: no standalone reflexive proof |
| 1.3 rw+exact | easy-bound division premise becomes `(one_le_div hlam).2 h` in extraction |
| 1.4 simp+exact | n/a: no such pair; existing `simpa using hlam` already terminal |
| 1.5 trailing rfl after simp | n/a: no such pair in headline |
| 1.6 constructors | n/a: no conjunction/constructor |
| 1.7 apply+exact | n/a: no such pair |
| 1.8 contradiction+push | n/a: no by_contra |
| 1.9 eta reduction | n/a: remaining `fun j ↦ hr _` changes the finite-index input |
| 1.10 single-use have | applied: inline original `hR`, `hsq1`, and proof-local positive parameter |
| 1.11 apply+intro | n/a: no such pair |
| 1.12 redundant show | n/a in headline; helper's `show` is a term premise |
| 1.13 have projections | n/a: no tuple projections |
| 1.14 consecutive rw | no sequential pair in headline; explicit empty-card rewrites grouped |
| 1.15 terminal simp only | n/a: terminal zero-case `simp` already bare |
| 1.16 nonterminal simp | intermediate flexible-simp attempt fixed by explicit empty-card rewrite |
| 1.17 dot notation | n/a: no changed call with useful receiver notation |
| 1.18 `<|` | n/a: helper argument occupies a comma-delimited rewrite list; final helper has later arguments |
| 1.19 push_neg | n/a: no deprecated tactic; avoid mutating negation with direct `lt_of_not_ge` |
| 1.20 existential helper | n/a: neither theorem nor helper supplies an existential witness |
| 2.1 grind whole | actual native multi_attempt failed on `False` after cardinality negation |
| 2.2 delete before grind | n/a: retained public proof contains no grind |
| 2.3 simpa consolidation | existing zero-case parameter proof retained as `by simpa using hlam` |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal |
| 2.5 positivity | actual production `positivity` closes the empty one-dimensional case |
| 2.6 gcongr | n/a for final headline: no monotonicity calc remains; substantive sum helper separately audited |
| 2.7 lia/omega | removed original `omega`; exact `Nat.succ_le_succ hn` supplies dimension inequality |
| 2.8 aesop | actual native whole-proof attempt made no progress |
| 2.9 norm_num/cast | production `norm_num at h ⊢` reduces dimension-one empty-filter premise |
| 2.10 decide | n/a: free real/radius parameters prevent closed finite evaluation |
| 2.11 field_simp/ring | n/a in headline; substantive algebra moved to successor helper for fresh audit |
| 2.12 linear_combination | n/a in headline: no ring-ending subproof after extraction |
| 2.13 wlog | n/a: small/large lambda and zero/positive predecessor are not symmetric cases |
| 2.14 collapse calc | n/a in final headline: multi-step counting estimate extracted |
| 2.15 `<;>` | n/a: no set of analogous remaining goals |
| 3.1 erw | n/a: no erw |
| 3.2 fun_prop migration | n/a: no legacy continuity/measurability |
| 3.3 omega→lia | stronger direct Nat lemma replaces the only omega; no arithmetic search remains |
| 3.4 rcases rfl | applied: zero predecessor substituted directly by `rfl` pattern |
| 3.5 attributes | n/a: one-use private estimates do not justify global automation attributes |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 heartbeat options | n/a: none present or introduced; probe timeouts did not trigger limit raises |

## Step back / independent verification

Whole native proof probes at line 203: `grind` failed; `simp` and `aesop` made no progress;
`exact?` and `apply?` hit the unchanged default heartbeat limit. The mathematical induction
cannot be discharged by a generic card-filter lemma alone. The final headline is a short
case outline of named mathematical estimates.

`/private/tmp/lattice-main-original.lean` imports the built production module, independently
re-elaborates the entire ORIGINAL file's declarations/proofs in `RothOriginal` (using its own
original helpers, not `Roth.card_filter_weight_le`), and kernel-checks
`example : @RothOriginal.card_filter_weight_le = @Roth.card_filter_weight_le := rfl`.
This ensures the original proof is still valid and both functions have exactly the original
type. Its CLI compile exited 0. `/private/tmp/lattice-main-original.log` records the actual
public `#check` and both axiom outputs.

`/private/tmp/lattice-main-axioms.lean` is a full current-source copy with actual `#print axioms`
commands for both new PRIVATE helper declarations while their short names are in scope.
Its CLI compile exited 0. Output: each new helper, the public theorem, and the independently
reconstructed original theorem depend exactly on `[propext, Classical.choice, Quot.sound]`.
No `sorryAx`, custom axiom, or source trust shortcut.

Historical source checks on frozen hash: `/Users/ramin/.elan/bin/lake build Roth.Lattice`
exited 0, final invocation 43s (`/private/tmp/lattice-main-build.log`). Complete native
`lean_diagnostic_messages` after formatting returned `partial:false`, `success:true`, only
inherited header warning. No failed imports, unproved declarations, or target warnings.

## Gate status — packing corrected, owner final verification renewal pending

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass on frozen hash | actual `lake build Roth.Lattice` exit 0, 43s |
| definition_protected | pass | no definition/abbreviation changed |
| theorem_statement_protected | pass | compiled original proof-function equality, only layout/lambda notation changed |
| structure_gate | pass | 14 body lines; longest branch nine including header; no conjunction |
| naming_gate | pass | descriptive snake_case public name and private nonnumbered helpers |
| line_packing_gate | pass on corrected hash | actual measured widths100/76/53, all arithmetic rows `ok` |
| inequality_orientation_gate | pass | occurrence table; zero reversed inequalities |
| standard_axioms | pass | actual public, both helpers, independent original axioms printed |
| complete_LSP | pass on frozen hash | partial:false, success:true, inherited header warning only |

No overall final pass claimed before the owner confirms corrected-hash final gates.
Whole-project build, separate LeanEval, publication and final performance sweep belong to owner.

Renames queued: none. Refactoring needed: separately audit each of the two new helpers.
The signature packing correction has been applied by owner; final verification renewal is ongoing. No public-API
restatement, extra abstraction, module split, or header change proposed.

## Eleven required worker checks

* [✓] Step 1: all required references read.
* [✓] Step 2: all 24 audit entries above.
* [✓] Step 2.5: five actual search methods, partial match used.
* [✓] Step 2.6: all five parameters, drop and applicable weak-form probes, public literature.
* [✓] Step 2.7: every signature line measured; first-line defect discovered and reported.
* [✓] Step 2.8: inequality occurrence table.
* [✓] Step 3: all 42 rules accounted for.
* [✓] Step 4: whole-proof native tactics tried; mathematical reflection above.
* [✓] Step 5a: complete native diagnostics; only user-preserved header warning.
* [✓] Step 5b: diff gates including actual corrected-hash packing table emitted; owner renewing
  compilation evidence after the semantic-neutral signature repack before publication.
* [✓] Step 6a: no renames required; no sidecar mutation.

## Owner corrected-hash renewal — complete

The pending renewal above is now resolved at final source SHA256
`97697192cf943554cec6fbc3735d556e63eb441571c2f30b39ff2f7b6e73883e`.
All source ownership explicitly revoked before gates. Actual module73103 exit0(30s),
complete native LSP cell98 partial=false/success=true/zero errors, sole preserved header
warning. Owner independent ORIGINAL entire-file reproof and all4 original public exact
proof-function equalities29613 exit0; actual imported environment all13 public/private
standard-axiom scan68502 exit0. Logs `/private/tmp/roth-lattice-d10-packed-{module,compatibility,axioms}.log`.
Sequential full `lake build` then separate `lake build Roth.LeanEval`, session16889,
both exit0(6.37s/3.15s), frozen hash unchanged; logs
`/private/tmp/roth-lattice-d10-packed-{full,leaneval}.log`. Overall declaration gates PASS
on corrected hash; earlier786d2720 checks remain historical. Both new helpers require
their own fresh dedicated audit next; no additional original-declaration count.
