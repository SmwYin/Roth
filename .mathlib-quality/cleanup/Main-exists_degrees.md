# `Roth.exists_degrees` — original 12

Status: FINAL for this scoped declaration. All required current gates pass; both final timing samples are below 1000 ms. Owner publication and independent whole-file review remain outside this worker scope.

## Frozen entry and mathematical scope

The genuine original and worker-entry targets were saved before any Lean experiment in
`/private/tmp/roth-main-degrees/{genuine-original,entry}.lean`. Exact comparison found them
identical, SHA256 `13dd177675ac5f56809f7bff74b8c13d566475e05df05c137713f68f3003be66`.
Genuine Main SHA256 `f651e4dd4b511c9aec15608b6d4ea9a2a4140ac513d486cee4c4ed7c30fa1069`;
entry Main SHA256 `8875868f966da50880091739b9a23369d133766180b27dd6972813090fd12228`.
The initial declaration has 65 nonblank lines (7 signature + 58 proof); the saved extraction
also includes one trailing blank line, producing the historical 66/59 counters.

The theorem chooses one vector of natural degrees. Its common product scale is larger
than `10 max_j log q_j / δ`; ceiling quotients give a lower product bound and an additive
rounding error. That error is small relative to the common scale. Multiplication by the
positive logarithm gives the lower degree bound directly. Canceling the preceding logarithm
from the adjacent product comparison gives strict adjacent separation. All five properties
remain about the same witness, and the complete mathematical conclusion is preserved.

## References and baseline

Read the installed Lean and mathlib-quality skills; full cleanup and cleanup-all workflows;
full golfing-rules, proof-patterns, mathlib-search, generalisation-patterns, cleanup-gates;
relevant style/naming sections; mathlib-review-stages, profiling and buzz workflow.
The owner's binding reuse instruction supplies the clean same-source baseline build/native/
complete LSP evidence, without rerunning an unchanged baseline. Existing header/hQ/hc warnings
are outside this declaration. No helper, import, definition, rename or shared progress edit.

## Full 24-item declaration audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | Initial baseline has no target-range warning; first complete edited Main LSP has no target warning and only the three existing warnings. |
| 2 | HAVE SCAN | Complete initial/final scan below. Remove artificial contradiction scaffolding; retain reusable estimates and proof-bearing blocks. |
| 3 | SET_OPTION | None in target; no resource limits raised. |
| 4 | SIMP SQUEEZE | Initial `simp only [hr]` was nonterminal and correctly scoped. New `simp [r, mul_div_assoc, ...]` closes `hr0`. Reciprocal normalization is nonterminal `simp only`. Terminal `simpa only [hr0]` deliberately rewrites exactly the witness identity without expanding the ceiling. |
| 5 | NAMING | `exists_degrees` is descriptive snake_case, with no scheme number, forbidden abbreviation, `_ge_`/`_gt_`, or numbered auxiliary suffix. No rename. |
| 6 | LINE PACKING | Every signature line measured in codepoints; required final table below. |
| 7 | BY PLACEMENT | All `by` tokens remain on their declaration/`have` line. |
| 8 | FORMAT | Two-space proof indentation, no internal blank lines, no tactic semicolon chains, and mapsto lambdas. |
| 9 | COMMENTS | No initial proof-body comments; no comment deleted. Source citation is preserved. |
| 10 | DOCSTRING | Existing public description and source citation preserved; it distinguishes the common product control and adjacent separation. |
| 11 | VISIBILITY | Public theorem is part of the documented mathematical API and its full conclusion is consumed downstream. No visibility change. |
| 12 | STRUCTURE | Initial 58 nonblank proof lines and 17-line adjacent branch require substantive shortening. Replaced with 30-line proof and branches at most 8 lines before final mandatory term inlining, and 7 lines finally. No conjunction splitting, unrelated fact tuple, helper wrapper or extraction. |
| 13 | MATHLIB | Five-method search below finds ceiling/order building blocks; no exact bundled Roth degree-selection theorem. |
| 14 | JUNK DEF | n/a: theorem, no definition. Local witness lets remain local. |
| 15 | EXISTS LEMMA | n/a: this is a substantive public existence theorem with inequality content, not a trivial private witness/rfl wrapper. |
| 16 | SHOW/CHANGE | No `show` or `change` in the rewritten target. |
| 17 | PUSH_NEG | None. Both initial `by_contra!` blocks are eliminated by direct positive-factor comparisons. |
| 18 | GENERALISE | Every binder audited below; supported bounded weakenings are `δ ≤ 1` and weak adjacent logarithm growth. Exact conclusion retained. |
| 19 | INEQUALITY | Zero reversed inequalities in signature or proof; required occurrence table below. |
| 20 | NORMAL-FORM | Natural-valued degrees, real cast products, and ordered inequalities are the canonical forms needed by consumers; no new equivalence API. |
| 21 | SYNTAX-GEN | Same witness and argument order; weakening removes unnecessary strictness at the call boundary. No optional ambient restatement. |
| 22 | IMPORT-FANOUT | n/a: no import added. |
| 23 | CASTS | Nat-to-real casts bridge arithmetic domains; explicit casts on `s`, `r j`, and `r i` fix the intended real expression. Numeric ascription in `div_pos` fixes ℝ. No new redundant same-type cast. |
| 24 | INSTANCE-NAME | The existing `NeZero m` binder stays anonymous; no instance added or named. |

### Complete initial HAVE scan

All initial `have` occurrences, including anonymous local facts, are accounted for in source order:

| Initial binding | Shape/use | Action |
|---|---|---|
| `hℓ` | term, reused throughout | retain |
| `hle` | term, reused for bounds | retain as pointwise binder |
| `hr₀R` | proof block | replace explicit ceil-plus-one scaling with `exists_nat_gt` |
| `hr₀'` | proof block | retain its mathematical scale bound as `hS` |
| `hr0` | proof block | simplify to terminal simp |
| `hlow` | pointwise proof block | direct `div_le_iff₀` application |
| `hup` | pointwise proof block | combine rounding error and relative bound |
| anonymous `Nat.ceil_lt_add_one` | single-use term in `hup` | inline into multiplication |
| `h2` in `hup` | term, rewritten then consumed | retain as the rewritten ceiling product `hceil` |
| `h53` | proof block | combine into `hup`, avoiding a second layer |
| anonymous `hup j` in `h53` | single-use term | inline as `linarith only` premise |
| anonymous `hle j` in `h53` | single-use term | inline as `linarith only` premise |
| `h31a` | proof block | direct positive-log cancellation as `hlarge` |
| `h1` in `h31a` | single-use term | inline `hlow j` |
| `h2` in `h31a` | single-use term | inline `hle j` |
| `h3` in `h31a` | nonnegative natural cast | removed with contradiction route |
| `h4` in `h31a` | single-use term | removed with contradiction route |
| `hℓm` in `h31a` | single-use term | removed with contradiction route |
| `h5` in `h31a` | single-use term | removed with contradiction route |
| `h6` in `h31a` | single-use term | replace by explicit monotonicity premise |
| anonymous `h31a j` in positivity | single-use term | inline |
| anonymous real positivity in positivity | single-use term | inline into `exact_mod_cast` |
| `A := h53 j` | single-use term | use direct product comparison |
| `B := hlow i` | single-use term | use direct product comparison |
| `C := h50 i j hij` | single-use term | inline into monotonicity |
| `hrj` | nonnegative natural cast | inline |
| `hri` | nonnegative natural cast | inline |
| `D` | proof block, explicit denominator identity | replace by associativity and positive-factor cancellation |
| anonymous identity inside `D` | proof block | eliminated; no `field_simp` needed |
| `E` | proof block, contradiction | replace by direct positive-factor cancellation |
| anonymous multiplication in `E` | single-use term | eliminated with contradiction route |

### Five-method mathlib search

| Method | Actual query | Result |
|---|---|---|
| Lean-Finder | common ceiling quotient degrees with logarithmic product control | Unrelated Behrend Roth bounds and Akra–Bazzi rounding; no exact local theorem. |
| Loogle | `Nat.ceil, _ < _ + 1` | `Nat.ceil_lt_add_one`, generalized negative-one variant. |
| LeanSearch | natural ceiling of nonnegative real is less than real plus one | `Nat.ceil_lt_add_one`, `Nat.abs_sub_ceil_le`, integer/extended variants. |
| Source search | `ceil_lt_add_one`, `ceil_lt_iff`, `ceil_le_iff`, `lt_ceil` in Floor sources | Verified floor definitions and Nat/Int alternatives; target uses Nat API directly. |
| Name-pattern | `ceil` via local search | Nat/Int/ENat ceiling families found in sources; symbol index unavailable, so no indexed absence claim. |

Auxiliary variants checked: `_of_gt_neg_one`, Nat/Int alternatives, `ceil_pos`, `ceil_le`,
`lt_ceil`, `div_le_iff₀`, and left/right positive multiplication cancellation.
Common-equivalents table: no matching discrete/finite/bounded predicate replacement.
Conclusion: partial matches supply the real API; keep the substantive bundled selection theorem.
No claim of exhaustive semantic absence or new API need is made from searches alone.

### Per-binder generalisation audit

| Binder | Class/use | Mechanical candidates and outcome |
|---|---|---|
| `{m : ℕ}` | finite index value | Drop changes all index types; no unused binder. Optional general finite index restatement excluded by scope. |
| `[NeZero m]` | typeclass | Required by the statement's `0 : Fin m` and nonempty supremum. No parent class or universe weakening applies. |
| `{δ : ℝ}` | scalar value | Appears in hypotheses and full conclusion. Logarithm/ceiling setting retained; no optional ambient field generalisation. |
| `hδ0 : 0 < δ` | proposition | Essential positivity for denominator and strict bounds; at δ=0 the same-j lower and strict upper product bounds contradict one another. Drop/weak form unsupported. |
| `hδ1 : δ < 1` | proposition | Bounded candidate `δ ≤ 1` compiles in the actual rewritten proof and independent old-style proof. Kept. No numeric range expansion experiment. |
| `{q : Fin m → ℕ}` | denominators | Used throughout statement/construction; dropping it changes the statement. |
| `hq : ∀ j, 1 < q j` | proposition | Gives each positive log. Weak `1 ≤ q j` admits q=1 and contradictory same-j product bounds. Cannot point-localise because each degree is controlled. |
| `h50` | proposition | Old proof uses `.le`; weak adjacent growth compiles in actual rewritten proof and independent proof. Kept. Dropping allows equal denominators and impossible strict separation when δ≤1. |

The bounded source tests are actual compiled tests, not assumed successful. Broader numerical,
ambient-type or conclusion restatements are outside the authorized experiment scope. Inversion
check: logarithms remain active throughout, so no unused concrete object was merely unfolded away.

### Literature search

Web query: “Roth theorem choose r_j ceiling r_1 log q_1 log q_j degrees rounding”.
The original [Roth paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational_approximations_to_algebraic_numbers.pdf)
uses the quotient/ceiling interval. Princeton's [Diophantine approximation notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf)
and Stanford's [transcendence notes](https://math.stanford.edu/~ksound/TransNotes.pdf)
confirm the common logarithmic-product role. Local `clean.tex` lines 1640–1642 explicitly
state the same rounding construction. No literature-driven broader API change proposed.
ChatGPT mathematical MCP: unavailable in this tool inventory; no invocation claimed.

### Inequality scan

| Occurrence | Original | Action |
|---|---|---|
| none | No `≥` or `>` in Lean signature/hypotheses | All inequalities already `<`/`≤`; no rename. |

## Historical performance diagnosis

Historical target row: 3452.761 ms, valid FAIL. Its actual source is Main689 after
MainLemma caller repairs, not the genuine project-original Main684. The target canonical
source matches; no speedup ratio across contexts is claimed.
Target-only indexed trace inspection identifies nlinarith tactic roots of 776.912,
566.334 and 531.181 ms; `field_simp` contributes about 182.190 ms in the adjacent block.
Nested nodes are not added to these parents. Root cause: class 4, broad-context nonlinear
arithmetic and extra contradiction/denominator normalization. The rewrite supplies small
`only` premise sets and cancels positive logarithms directly.

## All 42 golfing-rule slots

The binding bounded-mathematical-rewrite scope prevents speculative whole-proof tactic loops;
statuses below distinguish actual transformations from inapplicable tactics or unrun alternatives.

| Rule | Status |
|---|---|
| 1.1 by-exact wrapper | n/a: no root wrapper; real construction required. |
| 1.2 by-rfl | n/a: no by-rfl root or residual identity proof. |
| 1.3 rw + exact | Applied by replacing lower-bound rewrite/exact with direct iff application; final witness rewrites become simpa. |
| 1.4 simp + exact | Applied to final product conclusions via the witness identity. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor chain | Retained one existential/and tuple; no sequential constructor/exact boilerplate. |
| 1.7 apply + exact | Applied to lower bound through direct `div_le_iff₀` application. Remaining apply changes the positive-factor goal. |
| 1.8 contradiction compression | Both original by-contra blocks removed entirely by direct comparison. |
| 1.9 eta | Mapsto lambdas retained where q/log composition is substantive; no removable eta wrapper. |
| 1.10 single-use term haves | Initial aliases eliminated; final `hprod` and `hδ` inlined at native drain. No final one-use term-only have. |
| 1.11 apply + intro | n/a: no such pair. |
| 1.12 redundant show | n/a: none. |
| 1.13 have + projections | n/a: no projection-destructured have. Existential scale uses obtain. |
| 1.14 consecutive rw | n/a: no remaining consecutive rw calls. |
| 1.15 terminal simp | `hr0` closes with unsqueezed simp. Final simpa only [hr0] is the exact witness-identity conversion, avoiding unintended ceiling unfolding. |
| 1.16 nonterminal simp | Both algebra normalizations use explicit simp/rw lists; no bare nonterminal simp. |
| 1.17 dot notation | Used trans_lt/trans_le/mp-style chaining for comparisons. |
| 1.18 trailing parentheses | `<|` not needed in final production; parentheses delimit arithmetic premises and nested comparison arguments. |
| 1.19 push_neg | n/a: none. |
| 1.20 trivial existential | n/a: substantive public theorem. |
| 2.1 whole-proof grind | Not run: binding bounded constructive rounding rewrite; the existential natural scale and ceiling error are explicitly supplied. No claim of a successful grind attempt. |
| 2.2 pre-grind deletion | n/a: no grind. |
| 2.3 simpa consolidation | Applied to r0 and final product conclusions; also associativity cancellation. |
| 2.4 fun_prop | n/a: no continuity/differentiability/measurability goal. |
| 2.5 positivity | Used for nonnegative quotient and multiplicative factor. Natural degree positivity follows the actual strict lower bound. |
| 2.6 gcongr | Direct scalar multiplication APIs replace the original manual monotonicity scaffolding; no residual multistep calc monotonicity block to test. |
| 2.7 lia/omega | n/a: no residual Nat/Int linear arithmetic goal; comparison arithmetic is real and uses explicit positive logs. |
| 2.8 aesop | n/a: no residual logic/membership goal beyond the explicit tuple, no speculative whole-construction search. |
| 2.9 norm_num/cast | norm_num supplies positive 10; exact_mod_cast transfers q positivity and final natural degree positivity. |
| 2.10 decide | n/a: quantified real logarithmic inequalities are not finite decidable computation. |
| 2.11 field_simp/ring | Removed original field_simp identity; associativity and reciprocal normalization suffice, with actual compilation. |
| 2.12 linear_combination | n/a: no final ring/ring_nf block with contextual hypotheses; only arithmetic certificates remain. |
| 2.13 wlog | n/a: no symmetric case branches. |
| 2.14 collapse calc | n/a: no calc block; inequalities already composed as terms. |
| 2.15 multiple goals | Different tuple properties need distinct estimates; no duplicate terminal tactic sequence across goals. |
| 3.1 erw | n/a: no erw. |
| 3.2 legacy function tactics | n/a: no continuity/measurability tactic. |
| 3.3 omega→lia | n/a: neither occurs in target. |
| 3.4 rcases rfl | n/a: no substitution case split. |
| 3.5 automation attributes | n/a: no new reusable rewrite theorem or instance; no global attribute change. |
| 3.6 simp_all | n/a: no simp_all only or broad closure proof. |
| 3.7 limits | No limit option in target or new source. |

## Final mandatory HAVE review and holistic reflection

`hℓ`, `hle`, `hlow`, `hup`, and `hlarge` are reused; `hS`, `hr0`, `hlarge`, `hup`,
and the adjacent inequality `h` have tactic proof content. `hceil` is rewritten and then
used by linarith, so it has two genuine uses. The two one-use term aliases `hprod` and
`hδ` were inlined before the final gate cycle. The cast on the latter disappeared because
its real type is already fixed by `hδ1`; this is the one redundant cast dropped.

Manual holistic simplify review (built-in simplify unavailable, no invocation claimed):
the proof uses existing ceiling/order APIs directly, keeps a single degree witness,
eliminates both contradiction branches, has no duplicated new helper or wrapper, and
restricts nonlinear arithmetic to a few supplied facts. The independent proof deliberately
retains the distinct original ceil-plus-one scale. No production extraction is mathematically
necessary. No further speculative automation or optional generalisation was run.

Failed scratch probes are retained verbatim: v1 lacked the explicit supremum function;
v2 attempted the wrong scalar cancellation orientation; v3 needed reciprocal normalization.
Each is a real failed elaboration, not a successful validation. v4 compiled cleanly before
production application. The final mandatory inlining starts a new validation state and
is not credited with the earlier build/native results.

## Final signature packing (codepoints)

| Line | Width | Next semantic token | Token width | Arithmetic | Status |
|---|---:|---|---:|---|---|
| 278 | 93 | `(hq : ∀ j, 1 < q j)` | 19 | 93 + 1 + 19 = 113 > 100 | ok |
| 279 | 65 | `2 / δ * Real.log (q i) ≤ Real.log (q j)) :` | 42 | 65 + 1 + 42 = 108 > 100 | ok |
| 280 | 82 | `(∀ j, 10 / δ < r j)` | 19 | 82 + 1 + 19 = 102 > 100 | ok |
| 281 | 86 | `(∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j))` | 56 | 86 + 1 + 56 = 143 > 100 | ok |
| 282 | 69 | `(r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0)) := by` | 72 | 69 + 1 + 72 = 142 > 100 | ok |
| 283 | 78 | proof follows | — | n/a | ok |

All six lines are covered. No token fits its predecessor. The actual `set_option format.width 100 in #check @Roth.exists_degrees` reference is saved at `/private/tmp/roth-main-degrees/linear-repeat-profile/check-width100.txt`. Lean’s nested pretty output has one 105-codepoint line despite that option; the production signature itself remains at most 93 codepoints and satisfies the measured table.

## Verification qualifications before final measurements

First semantic attempt failed parsing raw repr names containing unquoted `._@` components;
only the scratch harness was repaired to quote the actual name component as `.«_@»`.
The next attempt passed the full recursive TYPE/raw-byte guards, including exactly the
actual second-binder hygienic substitutions, and completed actual VALUE inference/closedness/
standard-axiom checks for production root and independent root plus `_simp_1_1` through
`_simp_1_5`. The cumulative command then exhausted the unchanged 200000-heartbeat default
while checking `_simp_1_6`. This is a failed aggregate command, not a production theorem
performance result and not an excuse to pass the timing gate.

The successful completion tokens and unchanged source/independent-olean hashes are preserved
in `semantic-supplement-binding.json`. Only the outstanding `_simp_1_6`, recovery and caller
checks are supplemented, each in its own normal default-budget command; completed proofs
are not reinferred. Compact TYPE, universe, VALUE hash/length and acyclic dependency metadata
are collected afterwards. No full raw VALUE export or VALUE identity is claimed.

## Complete semantic closure

Actual complete TYPE/universe enumeration (72.625 s, exit 0) found exactly ten fresh rows:
production root (1), independent root plus seven generated simp declarations (8), recovery
root (1). Independent generated universes in suffix order 1–7 are `[u_2]`, `[u_2]`, `[u_2]`,
`[u_1]`, `[u_1]`, `[u_3]`, `[u_1]`; roots are monomorphic. No blanket empty-universe guard.
The second rejected aggregate had already emitted valid individual PASS rows for simp6,
recovery, and caller; it rejected the unanticipated simp7 rather than assuming a suffix count.
Those rows remain in `supplement-passed-rows.json` and were not reinferred.

Only outstanding simp7 was then checked (actual universe `[u_1]`, VALUE repr 3345 bytes).
Final compact metadata/graph command exited 0 in 93.178 s. Its ten TYPE/universe rows were
compared byte-for-byte against the prior full actual inventory. Production and independent
root VALUE representations are respectively 15,664,069 and 28,265,504 bytes; they were checked
in memory, not exported. The caller VALUE representation is 50,475,347 bytes, checked in its
separate default-budget command. Hash/length receipts are truthful; proof VALUE identity
across modules is neither required nor claimed.

Strict TYPE comparison recursively covers Names, Levels, BinderInfo, metadata, literals,
projections and every Expr constructor, with no ExprBEq short-circuit. Raw TYPEs differ at
one anonymous NeZero binder per independent/recovery pair: actual top-level path 1,
instImplicit, Main salt 2006318098 versus IndependentDegrees salts 1700487646 and 3650487712,
all hygiene suffix 5. The exact actual Names have macro scopes and equal erasures; only those
two literal pairs are substituted. The remaining complete raw TYPE bytes and recursive Expr
structure are exact. The caller TYPE exactly matches the indexed accepted old TYPE.

The indexed old read decoded only the required TYPE strings and metadata, with read caps
`2 * indexed_TYPE_bytes + 2000`; hashes match the index. No old VALUE row was decoded or
exported. Actual target/current/recovery/independent values are opaque theorems, closed,
inferred, and use only propext/Classical.choice/Quot.sound. The ten-row local graph is acyclic;
997 actual external-origin observations are strictly upstream of Main. Independent proof
rejects the target family and current/later Main; accepted earlier-library evidence is reused.
All checks use actual defaults 200000/20000/512. The two failed aggregate semantic commands
are retained as failures, with their successful guards reused explicitly rather than relabeled
as full passes.

## Performance rejection and targeted linear-arithmetic fix

The first isolated final-prefix sample was 892.375 ms. Because that is at least 750 ms,
one mandatory exact-same-freeze repeat was captured under a fresh owner HOLD, drained,
and parsed only after explicit owner RELEASE. It measured 1057.535 ms, a valid FAIL.
Both samples remain recorded; no noise dismissal, average, cherry-picked pass, or third
unchanged capture is used.

The repeat's target-only trace attributes 219.892 ms to the final nlinarith, 131.687 ms to
the scale nlinarith, and 89.304 ms to the lower-degree nlinarith. Their supplied premises
already include the necessary multiplicative inequalities. Replacing exactly those three
`nlinarith only` calls by `linarith only` removes unnecessary nonlinear-extra generation.

One scratch construction accidentally also substituted in an earlier prefix proof; it
failed on that unrelated `exists_m` proof, despite no target errors. No production edit
was credited from that run. The corrected scratch has byte-exact unchanged preceding
commands and only the three target substitutions; it exited 0 in 28.277 s. The production
edit then changed only those three tactic names. Inverting those three changes restores
the exact prior target; bytes before and after the target are identical. Signature, 30-line
body, seven-line largest branch, all HAVE uses, casts, naming, comment preservation and
all 42 rule statuses were rechecked before the new final gate cycle.

New production SHA256 is `8327e6baee2bf25b8f8b372edfbacab0e1b5f30f7a92a379ac02d934ff3b9853`.
The prior full/native/semantic results and the 892.375/1057.535 ms failed sample pair remain
historical for the preceding proof state. Fresh current FULL exited 0 in 35.968 s.

For the current semantic cycle, all eight independent TYPE/VALUE/universe/DAG results are
reused with exact unchanged independent source and olean hashes, and fresh actual complete
family TYPE/universe enumeration. Production VALUE is checked afresh; actual caller and
recovery actual VALUE hash/length receipts match the previous receipts, with current closedness,
standard axioms and TYPE checks. Previous inference is reused under unchanged source/TYPE/opaque
dependency contracts. Hash/length matching is not full raw or strict VALUE identity evidence;
no VALUE identity is claimed. Completed independent/caller proofs are not needlessly reinferred,
and no full raw VALUE is exported.


## Current final gates and performance

All results below bind to Main SHA256 `8327e6baee2bf25b8f8b372edfbacab0e1b5f30f7a92a379ac02d934ff3b9853`
(573 lines, 32670 bytes), with no subsequent production edit.

| Gate | Actual current result |
|---|---|
| Full `lake build` | PASS, terminal 0, 35.968 s |
| Separate `lake build Roth.LeanEval` | PASS, terminal 0, 5.063 s |
| Current semantics | PASS, terminal 0, 192.170 s; actual ten-row enumeration before guards; fresh target VALUE; qualified unchanged independent/caller/recovery evidence above |
| Native Main / Eval / root | PASS, terminal 0, 31.346 / 28.394 / 26.237 s |
| Fresh complete unfiltered diagnostics | Main 0 errors, three existing warnings at 1/357/358; Eval/root clean; all partial=false, fully drained |
| First exact final-prefix profile | PASS, 775.858 ms |
| Mandatory same-freeze repeat | PASS, 740.514 ms |

The first current sample consists of 42.060 ms outer command + 685.388 ms async proof +
18.962 ms kernel parent + 29.448 ms lint. The required repeat consists of 38.129 + 652.638 +
17.476 + 32.271 ms respectively. All disjoint roots are counted; nested kernel times are
not counted twice; no compiler or lazy prior DATA roots occurred for this target. Actual
fresh profile family is exactly `Roth.exists_degrees`, with empty universe list. Both captures
retain complete canonical target matching, actual TYPE checks and in-memory opaque VALUE
inference/closedness/standard-axiom checks. The repeat’s selected TYPE, actual literal hygiene
pair, family/universes, and VALUE hash/length receipts equal the first sample; this is not
a full raw VALUE identity claim. Its actual prefix/Main binder pair is path 1, instImplicit,
macro-scoped `_stdin` versus `Roth.Main`, salt 2006318098, hygiene suffix 5, both erasing to
`inst`; the remaining full raw TYPE bytes and recursive structure are exact.

Because 775.858 >= 750, precisely one repeat was required and performed. Both current
samples pass the strict 1000 ms budget. The earlier 892.375/1057.535 ms pair remains a valid
failed proof state, and historical 3452.761 ms remains a failed historical context; neither
is erased, noise-dismissed, averaged into the current pass, or used for a cross-context ratio.
No unchanged third capture was performed.

Each phase had fresh explicit owner HOLD before any preparation and explicit RELEASE after
actual raw-unparsed drain before parsing. Defaults before/after remained 200000/20000/512;
full parent/Lake environment byte equality was checked in memory, with only safe fields and
hash/length persisted. Source/import/tool/payload/model/map freezes passed. The repeat driver
exited 0; all four profile drivers and all 44 task-known launch groups are absent, with no
active queries. A local drain assertion initially expected a colon instead of the actual
`DEFAULTS=200000/20000/512`; the failed assertion was corrected against both actual outputs
without rerunning capture. The parser initially refused a missing local RELEASE receipt
before reading raw, although owner release had arrived; saving that receipt enabled the
successful parse. A later optional check that pretty output itself stays within 100 codepoints
failed at its actual 105-codepoint final line; the real width-100 option and production-line
packing are recorded separately above. These local receipt checks are not falsely labeled
successful first attempts and do not change the successful Lean/profile results.

## Phase closure

- [x] Genuine original and entry saved before experiments; exact comparison recorded.
- [x] All 24 audit items, all 42 rule slots, complete HAVE scan, five-method search, binder review,
  inequality scan, documentation, casts/instances and measured signature packing completed.
- [x] Substantive 58-to-30-line proof shortening; largest final branch 7; no new helper or wrapper.
- [x] Exactly two supported premise weakenings; same witness and full conclusion preserved;
  narrowly authorized sole caller repaired and checked.
- [x] Current full/Eval, semantic, native, complete diagnostics and required profile pair pass.
- [x] Historical and failed scratch/aggregate/receipt attempts qualified truthfully; no new limits,
  axioms, admits, imports, shared writes or Git operations.
- [x] Manual holistic scoped review completed; no unavailable simplify invocation claimed.
- [x] END: scoped declaration work complete; all source/report/compiler/native/semantic/LSP/profile
  leases released. Owner retains publication and independent whole-file final review.
