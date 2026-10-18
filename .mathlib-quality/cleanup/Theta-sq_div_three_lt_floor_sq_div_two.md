# Cleanup: `Roth.sq_div_three_lt_floor_sq_div_two`

Dedicated original-25 leaf. Scope: this declaration only in `Roth/Theta.lean`; no caller edits,
helpers, imports, API changes, Git mutations, or shared-log changes. Fresh worker as dispatched.

## Result and mathematical content

The proof body shrank from five lines to one:

```lean
theorem sq_div_three_lt_floor_sq_div_two {a : ℝ} (ha : 10 < a) :
    a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2 := by
  nlinarith [Nat.lt_floor_add_one a]
```

The floor estimate `a < ⌊a⌋₊ + 1` together with `10 < a` supplies all the arithmetic needed.
The named floor alias, the separately named upper bound, and the lower-floor-bound subproof
are unnecessary. The declaration, hypothesis, conclusion, name, visibility, and docstring
remain unchanged. The sole caller is `min_le_sum_max` in the same file, unchanged.

## Baseline and provenance

- Immutable original: `2b64544bf9f77a8ff957bf1bcaf693ac72217ff6:Roth/Theta.lean`.
- Released checkpoint: `ae371a359885019f26d23b5885e926e7ea25e2bc` (owner reports published origin).
- Release source SHA256: `3522af0920e133d0f34f3da6c162e288d3987a0fb948ded6d3a89ef87ee1d62f`.
- Final source SHA256: `c24f9782e08680eaaebf16b134c8b86cbe13e05c9778d1606119f28f392cc7b9`.
- Owner-supplied release full build: exit 0, 83.621 s; separate `Roth.LeanEval`: exit 0, 29.992 s.
  These are inherited baseline evidence, not this worker's final full-project gates.
- Reused identical-source baseline LSP: `/private/tmp/roth-theta-floor-sum/final-lsp.json`:
  success true, partial false, timed_out false, failed_dependencies empty, zero errors,
  17 warnings, none in the target. No redundant baseline diagnostics request was made.
- No cache fetch or separate runLinter executable was needed; authoritative LSP warnings
  were retained. File dialect is classic imports, not the new module dialect.
- Read-only preparation made no writes or Lean/search/profile requests. All subsequent work
  occurred after explicit RELEASE, with the owner compiler window drained.

## References read

Read both `/Users/ramin/.codex/skills/lean4/SKILL.md` and
`/Users/ramin/.codex/skills/mathlib-quality/SKILL.md`, the complete cleanup command at
`/Users/ramin/.local/share/roth-mathlib-quality/commands/cleanup.md`, and the full
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`, `generalisation-patterns.md`,
and `cleanup-gates.md` under that installation's `skills/mathlib-quality/references`.
Also read relevant formatting, documentation, inequality, visibility, normal-form,
generality and cast sections of `style-rules.md`, relevant naming sections, all of
`profiling.md`, and the normal-form/syntactic-generality review criteria.

## Full substantive audit (24 items)

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target warning initially or finally. All 17 complete-file warnings have identical messages before/after; later locations move by four lines. |
| 2 | HAVE SCAN | Original `hlt` has no `by`, used by terminal arithmetic: inline `Nat.lt_floor_add_one a` as a tactic hint. Original `h10` has `by` and feeds arithmetic; whole-proof experiment proves it unnecessary, so remove its entire subproof. Final proof has no `have`. |
| 3 | SET_OPTION | None in this declaration; no production options introduced. |
| 4 | SIMP SQUEEZE | No simp call in the target; n/a. |
| 5 | NAMING | Snake-case name describes left/right square bounds and `<`; no forbidden abbreviation, scheme numbering, `_gt_`, `_ge_`, or numeric `_aux` pattern. No rename warranted. |
| 6 | LINE PACKING | Both signature lines measured below; moving the whole conclusion to line one would be 101 characters. |
| 7 | BY PLACEMENT | `by` remains at the end of the conclusion line. |
| 8 | FORMAT | Two-space proof indentation, one tactic, no empty proof lines. Original nested `norm_num; linarith` disappears with its unnecessary subproof. |
| 9 | COMMENTS | Original body contains zero narrative comments; none removed. Original source-bearing docstring preserved byte-for-byte. |
| 10 | DOCSTRING | Existing public docstring identifies the exact second FACT and its paper source; preserved. |
| 11 | VISIBILITY | Public wrapper retained under owner decision and no-unnecessary-API-churn preference. Sole current caller is internal, but changing visibility would add API churn without proof benefit. |
| 12 | STRUCTURE | Five body lines become one; zero conjunctions or branches. Not a headline theorem in module Main results; comfortably below both applicable limits. |
| 13 | MATHLIB | All five actual search methods attempted; partial floor bounds found, no direct replacement found. Clean anonymous `exact?` fails; bounded `apply?` yields only partial generic order/division suggestions. Details below. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: no existential output. |
| 16 | SHOW vs CHANGE | No production `show` or `change`. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Both effective binders probed; strict-to-weak, threshold, and field alternatives compiled, but none recommended for this source-specific public wrapper. Owner agreed to retain exact API. |
| 19 | INEQUALITY | All Lean-code inequalities have smaller side on left; measured occurrence table below. |
| 20 | NORMAL-FORM | Existing powers/divisions and natural floor with explicit real cast are the source's canonical comparison; no competing equivalent API found. |
| 21 | SYNTAX-GEN | Sole caller directly supplies `10 < θ * rp` and consumes `.le`; current syntax applies without adapters. No easier call-site restatement justified. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | Final statement retains the genuine ℕ→ℝ floor cast. Removed local `: ℝ`/`: ℕ` type annotations together with unused local bound; final proof has no explicit cast/ascription. |
| 24 | INSTANCE-NAME | n/a: no instances declared; actual type verification confirms no effective section instances. |

## Line packing and inequality artifacts

Compiled `#check @Roth.sq_div_three_lt_floor_sq_div_two` at `format.width 100`:

```text
@Roth.sq_div_three_lt_floor_sq_div_two : ∀ {a : ℝ}, 10 < a → a ^ 2 / 3 < ↑⌊a⌋₊ ^ 2 / 2
```

| Signature line | Codepoints | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 295 | 64 | Complete conclusion plus `:= by`, 36 characters excluding continuation indent | 64 + 1 + 36 = 101 > 100 | ok |
| 296 | 40 | None; proof body follows | n/a | ok |

| Occurrence | Location | Expression | Rewrite | Name action |
|---|---|---|---|---|
| 1 | Hypothesis `ha` | `10 < a` | none, canonical `<` | none |
| 2 | Conclusion | `a ^ 2 / 3 < (⌊a⌋₊ : ℝ) ^ 2 / 2` | none, canonical `<` | none |
| 0 reversed | Whole signature/body | No `≥` or `>` in Lean code | n/a | no `_ge_`/`_gt_` rename |

## Actual five-method mathlib search

Raw native results: `/private/tmp/roth-theta-sq-floor/search-{finder,loogle,leansearch,local}.json`.
Full-name and caller grep evidence: `/private/tmp/roth-theta-sq-floor/grep-evidence.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Real `a > 10`, square divided by 3 below half the natural-floor square | Returned `Behrend.div_lt_floor`, `mul_pow_le_nat_floor_pow`, and other distant bounds; no exact comparison. |
| B Loogle | `Nat.floor, _ ^ 2 / _ < _`; then `Nat.floor, LT.lt` | First empty; second returned `Nat.lt_succ_floor`, floor positivity/zero/lt facts, not this comparison. |
| C LeanSearch | Real at least ten, square/3 below half natural-floor square | Returned `Nat.div_two_lt_floor`, `Nat.abs_floor_sub_le`, and related partial facts. |
| D Source rg | Untruncated exact-name search across all Mathlib; floor/sq/pow/div variants in Algebra/Order/Floor, FloorPow, and Behrend | Exact name absent as text. Read `Nat.le_floor`, `Nat.lt_floor_add_one`, and partial variants. Text absence alone is not treated as a theorem-absence proof. |
| E Native local names | `floor` (50 results), then `Nat.le_floor` (15 results) | Found ordinary floor API. Index initially unavailable then warming; therefore no index-based absence claim is made. Names were additionally checked against source and compiled `#check`. |

Auxiliary variants include floor lower/upper bounds, `floor_lt`, `floor_le_iff`,
`lt_succ_floor`, `div_two_lt_floor`, and floor-power comparisons. The common-equivalents table
has no matching topology/finite/bornology concept here. The partial `div_two_lt_floor` has
insufficient coefficient strength for the desired square bound; direct square-floor API was
not found. The selected proof uses `Nat.lt_floor_add_one` directly and proves the remaining
numerical estimate by `nlinarith`. No new private wrapper or helper was introduced.

Clean search hygiene: the automation file imports only the original six pre-Theta imports;
it cannot import `Roth.Theta` since Theta itself imports those dependencies. Every tactic trial
is an anonymous `example`. No audited target or named failed trial can contaminate `exact?`.
The file exits 1 as expected; it does not certify successful positive declarations or axioms.
`exact?` reports it cannot close the goal. `apply?` returns partial order/division suggestions
and exhausts a deliberately lowered 20,000-heartbeat exploration budget. This is bounded
inconclusive search, not proof of mathematical absence. The known full-Theta native
multi_attempt stall was not repeated; live `lean_goal` and native isolated `lean_run_code`
were actually used, then ordinary isolated compiler trials supplied bounded exploration.

## Generalisation: every effective binder

`positive-final.log` is an exit-0 positive/axiom run. `drop-binders.log` is a separate expected
exit-1 negative run. `independent-original.log` verifies the complete actual effective type.

| Effective binder | Role | Actual compiled probes | Result/decision |
|---|---|---|---|
| `{a : ℝ}` | Value used by hypothesis, floor, and powers | Literal drop with `autoImplicit false`; generalise to `{K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] [FloorSemiring K] {a : K}` | Drop fails with unknown `a`, as dependence requires. Field formulation compiles with standard axioms. Retain real domain: sole real caller and paper-specific wrapper need no four-class API. Universe weakening is n/a for concrete ℝ; general-field probe is universe polymorphic. |
| `(ha : 10 < a)` | Lower bound essential to global validity | Drop; replace by `10 ≤ a`; replace by `5 ≤ a`; nonnegativity and lower threshold counterexamples | Drop proof fails; `a=0` certified counterexample. Both weak10 and weak5 proofs compile. `a=1.9` refutes nonnegative replacement and `a=4.99` refutes a bound of 4. Preserve source bound 10 and strict relation; no downstream application needs the broadened variants. |

There are exactly two effective binders. Section variables `σ`, `τ`, `Fintype`, and
`DecidableEq` do not occur in this theorem's actual telescope; no artificial binder probes
or instance scaffolding were added. Point-localisation and predicate unbundling do not apply
to a scalar lower-bound hypothesis. The successful broader candidates were communicated to
the owner before final API selection; the owner explicitly agreed that exact API preservation
was appropriate. These are assessed, unrecommended extensions, not unfinished required edits.

### Public literature and inversion

Actual WebSearch queries were `floor function squared inequality floor x squared x squared
3 2 generalization` and `"Formalizing Roth" "10" floor`. Returned hits included
[Polynomials involving the floor function](https://arxiv.org/abs/math/9504229),
[floor-function lecture material](https://www.cs.uleth.ca/~benkoczi/1820/hwk/soln3-2.pdf), and
an unrelated Roth-on-progressions formalisation. No returned source supplied this exact
comparison or a useful new canonical public formulation; unrelated generalisations were not
used as evidence. The decisive project reference is `.mathlib-quality/references/clean.tex`,
lines 879–889: its second FACT is explicitly for α > 10 and estimates α < n+1 ≤ (11/10)n.
The compiled weak5/weak10 and field examples are our concrete generalisation evidence.
ChatGPT math MCP is unavailable: actual tool inventory found no matching capability.

The inversion check finds an abstract arithmetic core after applying the single floor bound:
`10 < a → a < n + 1 → a²/3 < n²/2`. This exact real-valued candidate is compiled independently
at the end of `independent-original.lean`, proved by `nlinarith`. Extracting it would name one
arithmetic tactic, add a new helper and fresh-helper audit obligation, and improve neither
the one-line final proof nor the sole caller. Thus the abstraction is assessed concretely but
no new API/helper is recommended. The natural-floor concept itself already uses mathlib's
`FloorSemiring` API, as the compiled field probe demonstrates.

## Full golfing pass (42 rules)

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: original outer proof is not a term wrapper. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw + exact | n/a: no rewrite chain. |
| 1.4 simp + exact | n/a: no simp chain. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 anonymous constructor | n/a: scalar inequality, no conjunction. |
| 1.7 apply + exact | n/a: no such chain. |
| 1.8 by_contra! | n/a: no contradiction/negation setup. |
| 1.9 eta reduction | n/a: no lambdas. |
| 1.10 single-use have | Applied: inline `hlt` as the floor-bound hint; final whole-proof test also eliminates `h10`. |
| 1.11 refine + fun | n/a: no intro/application block. |
| 1.12 redundant show | n/a: none. |
| 1.13 obtain | n/a: no paired outputs/projections. |
| 1.14 merge rw | n/a: none. |
| 1.15 terminal simp only | n/a: no simp. |
| 1.16 squeeze nonterminal simp | n/a: no simp. |
| 1.17 dot notation | n/a: final proof applies only one floor lemma, no useful method receiver. |
| 1.18 `<|` | n/a: final proof has no parenthesised terminal subproof. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 inline existential | n/a: not existential. |
| 2.1 whole-proof grind | Tried plain and with `Nat.lt_floor_add_one`, `Nat.le_floor`; both fail with open arithmetic contradiction goals. |
| 2.2 delete before grind | Whole-proof experiments remove all original setup; hinted grind still fails. |
| 2.3 simpa consolidation | n/a: no simp/closing-chain structure; whole `simp_all` also makes no progress. |
| 2.4 fun_prop | n/a: no regularity property. |
| 2.5 positivity | Tried on whole goal: reports not a positivity goal. |
| 2.6 gcongr | Tried: leaves `a < ↑⌊a⌋₊` and denominator conditions; cannot supply the needed floor-relative bound. |
| 2.7 lia | Tried: fails on the nonlinear real square inequality. No omega fallback appropriate here. |
| 2.8 aesop | Tried: makes no progress. |
| 2.9 norm_num/norm_cast | Whole norm_num leaves goal open. Selected arithmetic proof eliminates the original cast-normalisation subproof entirely. |
| 2.10 decide/kernel | n/a: arbitrary real inequalities are not finite computable decision goals. |
| 2.11 field_simp/ring | n/a: strict inequality, not an algebraic identity. |
| 2.12 linear_combination | n/a: original does not end in ring/ring_nf; arithmetic inequalities need nlinarith. |
| 2.13 wlog | n/a: no symmetric branches. |
| 2.14 term calc | n/a: no calc/transitivity chain. |
| 2.15 `<;>` | n/a: one final goal. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop migration | n/a: no continuity/measurability tactic. |
| 3.3 omega→lia | n/a: no omega; lia was tried in 2.7. |
| 3.4 rcases rfl | n/a: no cases. |
| 3.5 automation attributes | No attribute added: conditional numerical estimate is not a simplifier rewrite and has one existing caller. |
| 3.6 simp_all | Whole simp_all tested and fails; no existing simp_all only to unsqueeze. |
| 3.7 maxHeartbeats | None in production before/after. Lower exploration limits were scratch-only. |

### Step back and simplify

Whole-goal `nlinarith` alone fails because floor bounds are not automatically known.
Adding exactly `Nat.lt_floor_add_one a` closes the entire goal in the clean `one-line.lean`
probe (exit 0), and the actual module build confirms it in context. This supersedes the
intermediate two-line candidate using a casted `Nat.le_floor` bound. The final one-line
proof expresses the only nonalgebraic fact explicitly, contains no duplicate structure or
new identifiers, and warrants no helper. Scoped holistic simplify review: PASS-THROUGH.
This host has no callable built-in `/simplify` Skill dispatcher; the review was performed
directly, not falsely reported as a separate tool invocation.

## Verification and diff gates

All evidence files below are under `/private/tmp/roth-theta-sq-floor/`.

| Gate | Result | Actual evidence |
|---|---|---|
| Module build | pass | `/Users/ramin/.elan/bin/lake build Roth.Theta` exited 0; `module-build.log`, 2423 jobs. |
| Independent immutable-original proof | pass | `lake env lean independent-original.lean` exited 0; original declaration copied from immutable Git source into `ImmutableOriginal`, with its full old proof. It never invokes the current theorem to prove the original. |
| Exact actual public telescope | pass | Same exit-0 run checks definitional type equality, walks both full telescopes, verifies ordinary binder names, BinderInfo, types and conclusion, and checks exactly two binders: implicit `a : ℝ`, explicit `ha : 10 < a`. No hidden section instances. |
| Actual built standard axioms | pass | `#print axioms Roth.sq_div_three_lt_floor_sq_div_two` after module build prints only `propext`, `Classical.choice`, `Quot.sound`; independent old proof has exactly that same standard list. |
| Complete unfiltered final LSP | pass | Native `lean_diagnostic_messages` on full absolute Theta path, no severity/declaration/line filters; `final-lsp.json`: success true, partial false, timed_out false, failed_dependencies [], 0 errors, 17 baseline warnings, no target diagnostics. |
| definition_protected | pass | `leaf.diff` contains no def/abbrev edits. |
| theorem_statement_protected | pass | Signature, name, visibility and documentation byte-identical to release and immutable target. Actual effective type also independently verified. |
| structure_gate | pass | One body line, no conjunction, zero branches. |
| naming_gate | pass | Mathematical snake-case name, no forbidden pattern. |
| line_packing_gate | pass | All signature rows measured above; 101-character combined line justifies break. |
| inequality_orientation_gate | pass | No reversed inequalities in Lean code. |
| Caller preservation | pass | Sole caller in the successfully built/diagnosed module; unchanged. No external use found in project source. |
| Comment/scaffolding protection | pass | All docstrings/comments unchanged; no sorry, new axioms, native_decide, limit raise, trace/debug option, or profiling scaffolding added. |
| New identifier validation | pass | Final diff introduces no identifier absent from original proof: `nlinarith`, `Nat.lt_floor_add_one`, and `a` were all already present. Floor lemma also read in mathlib source and compiled via native #check. |

Expected-failure exploration is deliberately separate: `automation.log`, `drop-binders.log`,
and the initial `positive.log` are not success/axiom certificates. The initial positive file
needed explicit `Nat.floor_eq_iff` rewrites for decimal counterexamples, since `norm_num`
alone did not evaluate those floors. The corrected `positive-final.log` exits 0 and certifies
all positive weakening/domain probes and the concrete counterexamples. The native #check
probe used a deprecated scratch-only Real.Basic import; production imports are unchanged.

Full project build and the separate `Roth.LeanEval` gate on this final source remain the
owner's sequential responsibility. This worker does not claim those pending owner gates.
No requests remain orphaned; all exploration/compiler sessions were drained before profiling.

## Buzz / actual profiling

Actual Lean 4.34 command for each profile:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 FILE
```

Both files preserve exact imports and every preceding production declaration and context,
ending immediately after this target with section/namespace closing commands. They are
explicitly **prefix-only** profiles, not whole-Theta success claims. The owner must still
perform the final whole-module sweep after later slow declarations are cleaned. No limit
raises were used. Imports and preceding declarations are excluded from target timing.

Baseline `baseline-prefix.lean` / `baseline-profile.log` exits 0. Target anchors:

- line 470933 outer `Elab.command`: 31.456 ms;
- line 473941 disjoint async target proof: 328.092 ms;
- line 512006 following async target linters: 6.253 ms.
- line 512004 disjoint async `addDeclCore`: 10.978 ms, containing `Kernel` at line 512005
  (10.948 ms). Count the parent once. The earlier `addDecl` at line 511519 (1.400 ms) is
  nested within the already-counted async proof, so not counted again.
- Accepted baseline aggregate: **376.779 ms**. An initial summary omitted the separate
  async kernel parent; inspecting root indentation corrected that accounting before freeze.
  Below 750 ms, so no borderline repeat needed.

Final `final-prefix.lean` / `final-profile.log` exits 0. All ordinary compiler and native
LSP requests were finished before launch. Target anchors:

- line 471562 outer `Elab.command`: 32.205 ms;
- line 474563 disjoint async target proof: 302.485 ms;
- line 503804 disjoint async `addDeclCore`: 10.898 ms, including its child kernel
  at line 503805 (10.868 ms), not counted separately;
- line 503806 disjoint async target linters: 4.194 ms;
- nested `addDecl` at line 503458 (1.406 ms) belongs to the proof task and is not recounted.

Accepted final aggregate: **349.782 ms**, below the 1,000 ms budget and 750 ms repeat
threshold. No repeat needed. `profile-anchors.txt` records the exact outer root tasks and
the immediately following `end Lemma6` boundary, which excludes its separate linter tasks.
Baseline/final show a small timing reduction; the substantive improvement is four removed
proof lines. Buzz outcome: **FAST-BOARD**, no over-budget declaration within this target.

No performance fix beyond proof simplification, no private helper, and no raised options.

## Phase artifacts and completion checklist

File-level fixes: n/a for this single-declaration leaf. Non-rename refactoring: none.
Rename queue: no rename proposed or queued; no shared sidecar touched. No structure deferral.
Comments preserved: none present in body; original source docstring intact. Total line delta:
5 → 1 body lines, saving four; file 972 → 968 lines relative to release.

- [✓] Step 1: required references read.
- [✓] Step 2: all 24 substantive audit answers recorded.
- [✓] Step 2.5: five actual search methods and limitations recorded.
- [✓] Step 2.6: all effective binder probes, public literature and inversion recorded.
- [✓] Step 2.7: every signature line measured.
- [✓] Step 2.8: inequality occurrence table recorded.
- [✓] Step 3: all 42 golfing rules assessed with actual applicable trials.
- [✓] Step 4: whole-proof reflection and scoped simplify review complete.
- [✓] Step 5a: complete final unfiltered LSP, zero errors.
- [✓] Step 5b: module build, independent original type/proof/metadata, actual axioms and diff gates.
- [✓] Step 6a: no rename necessary; no queue mutation authorized or performed.

Freeze status: source and this report frozen; source/report edit authority revoked on handoff.
No pending worker requests. Final owner full build, separate LeanEval build, and later
whole-module profiling remain explicitly owned by the parent.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (89.100 s),
then separate `lake build Roth.LeanEval` (28.568 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `c24f9782e08680eaaebf16b134c8b86cbe13e05c9778d1606119f28f392cc7b9`.
Raw logs: `/private/tmp/roth-theta-d25-full.log`, `/private/tmp/roth-theta-d25-leaneval.log`; machine record
`/private/tmp/roth-theta-d25-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 25/35, overall 206/264 original
declarations, 9/14 completed files. No new production helper; the prior helper remains separately audited.
