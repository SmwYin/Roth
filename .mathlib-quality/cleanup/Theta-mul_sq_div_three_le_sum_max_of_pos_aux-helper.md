# Dedicated audit: `mul_sq_div_three_le_sum_max_of_pos_aux`

Scope: only the new private positive-radius, strict-cutoff helper in `Roth/Theta.lean`.
This counts as one dedicated new-helper audit and **zero original-26 declarations**.
No Git mutation, shared report, rename queue, public signature, or caller changes.

## References and baseline

Read the Lean/mathlib-quality skills, full cleanup worker workflow, full golfing-rules,
proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates, and relevant
style, naming, and profiling sections. Standing authority in
`/private/tmp/roth_theta_leaf_instructions.md` governs this leaf.

Baseline source SHA256: `1e01b2a8d662c434a0fe32c58544459dc4a9d5a24065329876eecc341003f685`.
The preceding leaf supplied complete unfiltered native diagnostics at this exact hash:
`/private/tmp/roth-theta-quadratic-helper/final-lsp.json` and its evidence manifest:
success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors, 17 warnings.
This is explicitly **inherited baseline evidence**, not a fresh diagnostic call.
The accepted uncontended inherited exact-prefix profile was linear 500.838ms,
positive core 568.967ms, quadratic wrapper 314.604ms, public min 189.315ms.
Raw inherited log: `/private/tmp/roth-theta-quadratic-helper/final-profile.log`.
Full-project and separate LeanEval builds belong to the owner and are pending there.

Independent first-introduction declaration (22 body lines):
`/private/tmp/roth-theta-quadratic-helper/new-helper-initial.lean`, SHA256
`bbfaa4824d09a1f10356cbeb795bfae23d296889f76a675a576bfaedcaa2225c`.
First complete introduction snapshot SHA256:
`7685f1536fd898cfe55e148154245193b37cb1c23bd642dd32bcea7429f265c5`.
This audit's artifacts are under `/private/tmp/roth-theta-positive-audit/`.

## Mathematical understanding and action

Set n=⌊θr⌋. The arithmetic progression through n has sum at least (θr)²/3,
using n≤θr<n+1 and the exact sum of the first n natural numbers. Divide by
positive r, replace each summand by its positive part, then extend the range to l.
The single-use named bound `hn` was inlined directly into the final range inclusion.
The helper still has 22 body lines; the line count is unchanged because the application
wraps at 100 characters. There are fewer local facts to track, with the same mathematics.
No new helper was introduced. All source outside this helper is byte-identical to baseline.

Private-role retention: this is a substantive floor estimate, not a 1–3-call mathlib
wrapper. Its sole caller isolates the nonpositive-radius and equality boundary cases.
Inlining the whole helper there would recreate a branch longer than 10 lines. Retain
the private helper, with no docstring, and retain the broader downstream wrapper.
No downstream wrapper was used to prove the assigned helper or its original proof.

## Full 24-item audit

| # | Item | Result/action |
|---|---|---|
| 1 | Lint | No warning in helper's range; inherited file warnings belong to other declarations. Final full diagnostics required below. |
| 2 | Have scan | `hn`: no `by`, one use → inline. `hnle`: generalised, then used twice in arithmetic certificate → keep. `hnlt`: generalised and used in certificate → keep. `hsum`: rewritten by push_cast and used in certificate → keep. `hbound`: substantive six-line `by` proof → keep. |
| 3 | Options | No production options or limits. Scratch automation uses a lower 5000-heartbeat budget only. |
| 4 | Simp | Only `simp only [Finset.sum_div, sub_div, mul_div_cancel_right₀ _ hr.ne']`; nonterminal, deliberately explicit. |
| 5 | Naming | Snake case; describes squared-product lower bound and positive branch; `_aux` private suffix; no forbidden numeric scheme/abbreviation. No rename. |
| 6 | Packing | Two signature lines; measured table below, no repacking needed. `{l : ℕ}` already fits on first line. |
| 7 | By | `by` on signature line and local proof line. |
| 8 | Format | 2-space proof indent, 4-space signature continuation; no blank proof lines or semicolon tactic chains, no haveI/letI. |
| 9 | Comments | None inside assigned helper initially; none removed. All other narratives byte-identical. |
| 10 | Docstring | Private auxiliary correctly has none. |
| 11 | Visibility | Retain private: solely used by same-file boundary wrapper. |
| 12 | Structure | 22≤30 body lines; no conjunction, no case branch >10, local arithmetic block six lines; no further extraction. |
| 13 | Mathlib | Five searches and clean anonymous automation probes below; no direct replacement established. |
| 14 | Junk def | n/a: theorem, no new definitions. |
| 15 | Exists helper | n/a: no existential conclusion. |
| 16 | Show/change | n/a: neither occurs. |
| 17 | Push-neg | n/a: none. |
| 18 | Generalise | Every effective binder tested; broader boundary variants compile independently but already belong to downstream wrapper. |
| 19 | Inequality | All inequalities oriented `<`/`≤`; table below. |
| 20 | Normal form | Standard real inequality over `Finset.range`, `max 0`, natural floor; no alternate object disguised as a custom definition. |
| 21 | Syntactic generality | Current implicit θ,r,l and explicit proofs align with one routine caller; no improvement recommended. |
| 22 | Import fanout | n/a: no import added. |
| 23 | Casts | No new cast; retained `(n : ℝ)`, `Nat.cast (R := ℝ)`, and the real nonnegativity ascription fix the natural-to-real bridge. No redundant same-type cast introduced. |
| 24 | Instance names | n/a: no instance declaration; actual effective telescope checked separately. |

## Packing and inequality artifacts

Widths count Unicode codepoints, with `:= by` included. Width-100 actual type output is
preserved in `actual-positive.log`.

| Signature line | Chars | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 317 | 96 | `(hl : θ * r < l)` (16) | 96+1+16=113>100 | keep |
| 318 | 84 | proof body follows | n/a | keep |

The independent introduction put `{l : ℕ}` on the second signature line; baseline already
packed it onto line 317. This leaf measures and retains that packing; it does not claim
that inherited formatting as its own source change.

| Occurrence | Location | Orientation | Change |
|---|---|---|---|
| 1 | hr | `0 < r` | none |
| 2 | hθ | `0 ≤ θ` | none |
| 3 | hl | `θ * r < l` | none |
| 4 | conclusion | `r * θ ^ 2 / 3 ≤ ∑ ...` | none |
| 5 | entire signature | zero `≥`/`>` | no reversed name or rename |

## Five-method mathlib search

| Method | Actual query/action | Result |
|---|---|---|
| A Lean-Finder | Lower bound quadratic area for sum of positive parts max 0 (a - n / r) over a finite range | FloorPow reciprocal bounds and unrelated sum-of-squares estimates; no replacement. `search-finder.json`. |
| B Loogle | `Finset.sum, max, _ ≤ _`, corrected to `Finset.sum, Max.max, _ ≤ _` | First query rejected unqualified max; corrected query succeeds. `Finset.max_sum_le` is a pointwise comparison, not the quadratic area bound. Both raw outputs retained. |
| C LeanSearch | quadratic lower bound sum maximum zero arithmetic progression floor real | Floor APIs and unrelated reciprocal bounds; no replacement. `search-search.json`. |
| D Source rg | Full target name, `sum_max.*sq`, `sq.*sum_max`, `sum_range_id_mul_two`, `sum_le_sum_of_subset_of_nonneg` across all mathlib source, untruncated log | Existing arithmetic-sum/subset building blocks verified; no full target-name match. `source-search.log`. |
| E Local name | `sum_range` via native lean_local_search | Source hits include `Finset.sum_range_id_mul_two`; index=unavailable, so this is not indexed absence evidence. `search-local.json`. |

Auxiliary variants inspected: sum-range arithmetic identity, max-sum comparison,
sum-of-subset monotonicity, floor inequalities. No common-equivalents bucket applies.
Clean pretarget automation uses the exact preceding source, ending BEFORE the helper,
with anonymous examples, no current Theta import, no failed named-target pollution.
`exact?` cannot close; `apply?` offers only incomplete generic transformations and reaches
the deliberately lower 5000-heartbeat bound. `grind`, `simp`, `aesop`, positivity,
gcongr, lia, norm_num, decide, field_simp/ring, and nlinarith also do not close.
`automation.log` exit1 is expected negative evidence, never axiom verification.
No global absence claim: bounded failed searches do not prove absence. No direct
replacement established; retain the substantive proof built on verified mathlib APIs.
Native multi_attempt was not retried: inherited session limitation is repeated stalls;
the bounded ordinary compiler batch drained successfully.

## Generalisation: every effective binder

`negative-binders.lean` tests every binder with autoImplicit=false; exit1 is expected.
`boundary.lean` separately compiles the unchanged independent initial proof, boundary
extensions, and counterexamples, with standard axiom output. It calls no downstream wrapper.

| Binder | Class/use | Compiled candidate | Finding/decision |
|---|---|---|---|
| θ : ℝ | Value in floor, square, and every summand | Drop θ | Unknown θ in statement; indispensable data parameter. |
| r : ℝ | Value in cutoff, division and conclusion | Drop r | Unknown r in statement; indispensable data parameter. |
| hr : 0<r | Proposition; positive division and cancellation | Drop; weaken to 0≤r; independent radius-unrestricted proof | Original body fails without hr and with nonstrict hr. Independent all-r proof succeeds by nonpositive case + unchanged initial core. This broader case already exists in next wrapper; retain positive core, avoid duplicated casework. |
| hθ : 0≤θ | Proposition; floor nonnegativity | Drop; counterexample θ=-1,r=1,l=0 | Body fails; proposition false without it (1/3≤0). Already weak nonnegativity, no pointwise/typeclass weakening. |
| l : ℕ | Value; finite range and cutoff | Drop l | Unknown l in statement; indispensable range parameter. |
| hl : θr<l | Proposition; floor range inclusion | Drop; weaken ≤; independent equality extension | Original body fails; θ=4,r=1,l=1 refutes unrestricted cutoff. Weak ≤ succeeds with equality branch using preceding linear helper; next wrapper already states exactly that boundary-inclusive result. Retain strict core. |

There are no effective typeclass, universe, σ, τ, Fintype, or DecidableEq binders in the
actual helper type; metaprogramming checks all BinderInfo entries, not just printed headers.
Abstract ordered-field/floor API restatement considered: no production recommendation
for this private real-only branch; it would change representation/typeclass scope without
simplifying any caller. No optional speculative restatement is a blocker.
Public literature search: n/a, private declaration. Inversion check: no Roth-specific
named object to unfold; the proof already addresses arbitrary θ,r and a finite range.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: none |
| 1.2 by rfl | n/a: none |
| 1.3 rw+exact→rwa | n/a: no matching closing rewrite |
| 1.4 simp+exact→simpa | Existing nonterminal simp changes a whole finite-sum goal, then sum_le_sum supplies termwise comparison; no existing single premise to simpa. |
| 1.5 trailing rfl | n/a: none |
| 1.6 constructors | n/a: no product/conjunction proof |
| 1.7 apply+exact | n/a: already direct applications |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 eta | Both lambdas ignore indices and return max inequalities; not eta expansions. |
| 1.10 single-use have | Applied: inline hn. Other facts retained per detailed have scan. |
| 1.11 refine+fun | n/a: no apply/intro pair |
| 1.12 redundant show | n/a: none |
| 1.13 obtain | n/a: no projected pair |
| 1.14 merge rw | n/a: no consecutive rewrite calls |
| 1.15 unsqueeze terminal simp | n/a: sole simp is nonterminal |
| 1.16 squeeze nonterminal simp | Already explicit list |
| 1.17 dot notation | Already .2, .ne', .le; no redundant namespace application |
| 1.18 use <\| | Parentheses group sum/index proofs; no trailing tactic/lambda parentheses to remove |
| 1.19 push Not | n/a: none |
| 1.20 trivial exists | n/a: not existential |
| 2.1 grind | Fresh anonymous whole-proof trial fails |
| 2.2 delete before grind | n/a: production has no grind; whole-proof trial already deletes all setup |
| 2.3 simpa consolidation | Assessed with 1.4; simp whole-proof trial makes no progress |
| 2.4 fun_prop | n/a: no regularity goal |
| 2.5 positivity | Whole-goal trial reports not a positivity goal; exact mul_nonneg already states floor premise directly |
| 2.6 gcongr | Whole-goal trial makes no progress; direct positive-division lemma is shorter than introducing another tactic block |
| 2.7 lia/omega | Fresh lia trial fails (real nonlinear finite-sum bound); no omega introduced |
| 2.8 aesop | Fresh trial fails to progress |
| 2.9 norm_num/norm_cast | Whole-goal norm_num leaves goal; push_cast already centralises cast normalisation |
| 2.10 decide | Fresh trial rejects free variables; symbolic real proposition, no finite decision computation |
| 2.11 field_simp/ring | Existing field_simp closes the algebraic scaling identity; whole-goal field_simp/ring fails on genuine inequality |
| 2.12 linear_combination | n/a: no production terminal ring/ring_nf with hypotheses; arithmetic estimate already uses linear certificate |
| 2.13 wlog | n/a: no symmetric branches |
| 2.14 collapse calc | Four distinct mathematical steps; not a two-step transitivity wrapper |
| 2.15 <;> | n/a: no repeated similar subgoals |
| 3.1 erw→rw | n/a: no erw |
| 3.2 legacy regularity | n/a: no continuity/measurability |
| 3.3 omega→lia | Already tested lia; no omega |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 attributes | Private one-use numeric bound; no global automation registration recommended |
| 3.6 simp_all | n/a: no simp_all only |
| 3.7 remove limits | None in production; no increases or masking |

## Step-back and simplify assessment

No one-tactic proof found in the clean bounded batch. Exact finite-sum arithmetic,
positive division, pointwise max comparison, and subset monotonicity are independent
steps. The existing local arithmetic block is compact; extracting it would add another
single-use helper and require another fresh audit without resolving any structure limit.
An integral-area route would add analysis machinery/import costs for the same elementary
inequality. Retain the elementary proof and the established core/boundary split.
Holistic simplify performed directly (no callable built-in simplify skill exists here):
ISSUES-FOUND-AND-FIXED, single-use hn inlined; no remaining cross-proof duplicate introduced.

## Final verification and buzz

Fresh final module gate: `/Users/ramin/.elan/bin/lake build Roth.Theta` exited **0**,
`Build completed successfully (2423 jobs).` Full UTF-8 output: `final-module-build.log`.

Fresh final native `lean_diagnostic_messages` called with only the complete file path,
no declaration, line, or severity filter: success=true, partial=false, timed_out=false,
failed_dependencies=[], **0 errors, 17 warnings**, none within the helper. Raw full
response is `final-lsp.json`; warnings retain the previously supplied public-hypothesis,
instance, and header issues outside this leaf's scope.

Fresh final successful ordinary compiler probes (`final-probe-status-final.jsonl`):

- `actual-positive.lean`: exit0, 34.341s; source SHA256
  `5ea86973250defb110800112420002d5f8287ca2e420964b3ee858bb747e2c95`.
  Independent initial source proof compiled in a separate namespace, without invoking
  the current theorem. It checks actual constant
  `_private.Roth.Theta.0.Roth.mul_sq_div_three_le_sum_max_of_pos_aux`, exact effective
  types, universe arity, every retained binder's name/type/BinderInfo, and exactdrops=[].
  Initial proof value hash 1082453831 and actual proof value hash 4135709249 both
  typechecked using `value! true` (opaque allowed). Initial, actual, and full-old recovery
  axiom sets all exactly `[propext, Classical.choice, Quot.sound]`. No PANIC/error/sorryAx.
- Byte-identical `/private/tmp/roth-theta-min-sum/actual-compatibility.lean`: exit0,
  55.562s; SHA256 `bcb7e0d315c6b7277d83279f0bc147d70ed7e3f608e5e3111deb4ef5f768cafe`.
  Its complete immutable original namespace includes the entire original index_le_lem6
  proof/type, not a shortened caller sketch. Full old min telescope recovered with
  exactly hrp,hθ removed; original index_le_lem6 has no removals, exact effective binder
  metadata retained; public actual/original/recovery axioms and built linear/quadratic
  wrapper suffix axioms checked. Output `immutable-public.log` has both PASS markers.
- Candidate prefix and independent boundary/counterexample files each exited0 earlier.
  Negative automation and binder batches intentionally exited1 and are never cited as
  positive verification. Scratch verifier first required two corrections: structure-field
  layout, then explicit `repr` for BinderInfo display. Error outputs are retained as
  `actual-positive-initial-syntax.log` and `actual-positive-binder-format.log`; only the
  final clean exit0 certifies the proof/value checks.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Theta` invocation above exited0 |
| definition_protected | pass | No def/abbrev edit |
| theorem_statement_protected | pass | Signature byte-identical to this leaf's baseline; actual first-introduction type recovered exactly |
| structure_gate | pass | 22≤30 body lines, no conjunction or long branch |
| naming_gate | pass | Descriptive snake case, private `_aux`, no forbidden abbreviation or scheme number |
| line_packing_gate | pass | Complete measured two-line table above |
| inequality_orientation_gate | pass | No ≥/> in signature or hypotheses |
| cumulative local compatibility | pass | All source outside assigned helper byte-identical; immutable min/index and all three private suffix checks pass |
| full lake build then separate LeanEval | owner pending | Neither gate run by this leaf |

New identifier verification: no identifier introduced; the same floor/subset APIs merely
moved to their use site. No profiling scaffolding, raised limits, new axioms, sorry,
TODO/FIXME, changed documentation, or altered imports in this leaf's diff.

Buzz outcome: **FAST-BOARD for the four scoped prefix targets**. After all ordinary
compilers and the fresh full native diagnostics completed, ran the uncontended real
Lean 4.34 command:

`/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-positive-audit/final-prefix.lean`

Fresh final exit0, 99.527s wall time (full detailed trace output). Preserve the complete
UTF-8 `final-profile.log`, `profile-status.jsonl`, and all four declaration anchor files.
Aggregates sum each outer Elab.command and its associated root Elab.async proof,
kernel/addDecl/compiler and asynchronous linter entries. Nested trace children are not
added again. These are measured totals, not only a tactic timer or an echo of a command.

| Declaration | Inherited baseline ms | Fresh final ms |
|---|---:|---:|
| mul_div_two_le_sum_max_aux | 500.838 | 460.921 |
| mul_sq_div_three_le_sum_max_of_pos_aux | 568.967 | 543.552 |
| mul_sq_div_three_le_sum_max_aux | 314.604 | 304.757 |
| min_le_sum_max | 189.315 | 165.806 |

All four are below 750ms, so the ≥750ms repeat trigger does not fire. All are below the
1000ms budget. Small wall-clock differences are normal; no major speedup is claimed.
Limits raised: 0; masking options: 0; production profiling scaffolding: 0. No new helper.
No compiler/LSP requests were started after this uncontended profile. All requests drained.

The exact source prefix ends immediately after public min_le_sum_max. The later
whole-file profiled index_le_lem6 failure at default 200000 heartbeats is reserved to
original29/owner; this leaf neither reran nor concealed that known issue. No whole-file
profile pass or final all29/project acceptance is asserted here.

## Eleven-step checklist

- [✓] Step 1: required references read.
- [✓] Step 2: full 24-item audit above.
- [✓] Step 2.5: all five actual searches and corrected-query limitation recorded.
- [✓] Step 2.6: all six effective binders, drop/weakening probes, independent boundary proofs and counterexamples.
- [✓] Step 2.7: all signature lines measured; inherited packing distinguished from this leaf's edit.
- [✓] Step 2.8: per-occurrence inequalities scanned.
- [✓] Step 3: all 42 golf rules assigned concrete statuses.
- [✓] Step 4: whole-proof alternatives and private-role retention assessed.
- [✓] Step 5a: fresh complete unfiltered native final LSP, no errors.
- [✓] Step 5b: actual module, protected types, independent original/value/axiom, local diff gates checked.
- [✓] Step 6a: no renames needed; shared queue and shared reports untouched.

Result: one dedicated helper audit, 22→22 body lines, one redundant local fact removed.
Original-26 progress increment: **0**. Comments-preserved: none present in helper, all
outside prose byte-identical. No new helper requires another audit. Full owner builds
and later original declarations remain pending. Final source/report freeze recorded below.

Final source SHA256:
`e6360c9acdc9d7be22356ba3a26006e24cc1b0b667b5992395759228e1087530`.
All source outside the assigned helper, including the public min and index_le_lem6 caller,
remains byte-identical to this leaf's initial snapshot. `worker.diff` contains only hn
inlining. Evidence manifest: `/private/tmp/roth-theta-positive-audit/evidence-manifest.json`.
Terminal handoff: source/report edits revoked; all requests drained. No pending leaf gate.
