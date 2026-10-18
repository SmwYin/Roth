# ORIGINAL23 cleanup — `Roth.one_le_lem6M`

Dedicated single-declaration worker; only this proof and this report changed. Release HEAD
`35074319a001f55c71c461606a46fe12804114bc`; immutable original
`2b64544bf9f77a8ff957bf1bcaf693ac72217ff6`. Target at Theta:274.

## Result

Body 8 → 6 lines. Removed four single-use intermediate bindings and replaced the linear
arithmetic proof of `1 ≤ (r₁ : ℝ) + 1` with `le_add_of_nonneg_left (Nat.cast_nonneg r₁)`.
Direct existing product/power lemmas assemble the four lower bounds. No new helpers, imports,
caller changes, declaration/signature/domain/name/visibility/doc changes or attributes.

## Baseline and preparation

Read lean4 and mathlib-quality SKILL.md, full cleanup.md, golfing-rules.md,
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md,
style-rules.md, naming-conventions.md and profiling.md; read current Theta fully and immutable
original target. No tools/writes before owner RELEASE. Baseline source SHA256
`ad8d2553390a9af55ecec731f216e8bab23702ec79229af1331cfe87e6f1079f`.
Owner supplied preceding full build (65.683s), separate LeanEval (26.314s), stable17 hashes,
and complete baseline diagnostics `/private/tmp/roth-theta-lem6Phi/final-lsp.json`:
success true, partial false, timed_out false, no failed dependencies, 0 errors/17 warnings.
This exact-hash evidence is inherited, not a fresh worker baseline. Cache fetch unnecessary.
Classic dialect. Header metadata remains protected under standing user preference.

## Full audit

| # | Item | Concrete finding/action |
|---|---|---|
| 1 | LINT | Baseline/final: no diagnostic in target; 17 existing file warnings outside target. |
| 2 | HAVE SCAN | h1 at277 has proof in nested linarith; h2 at279 has `by exact_mod_cast`; h3 at280 and h4 at281 have no proof block. Each is used once in final assembly. Inline all four; express first directly via ordered addition. |
| 3 | SET_OPTION | None in target; none added. |
| 4 | SIMP SQUEEZE | No simp calls. |
| 5 | NAMING | `one_le_lem6M` describes conclusion using retained object name; no forbidden regex, `_ge_`/`_gt_`, or forbidden abbreviation token. Exact paper API name protected, no rename recommended. |
| 6 | LINE PACKING | One signature line, 87 codepoints; table below. |
| 7 | BY PLACEMENT | `:= by` ends the signature line. |
| 8 | FORMAT | Two-space tactic indent, one tactic per line, no blank proof lines, no haveI/letI. |
| 9 | COMMENTS | No proof comments present; no narrative removed. |
| 10 | DOCSTRING | Existing one-sentence source doc preserved byte-for-byte. |
| 11 | VISIBILITY | Public auxiliary bound used by index_le_lem6 and Θ_lt; retained public contract. |
| 12 | STRUCTURE | Six body lines, no conjunction and two one-line leaf branches; no helper extraction needed. |
| 13 | MATHLIB | All five actual methods below; use existing lower-bound product/power API, retain paper-specific public wrapper. |
| 14 | JUNK DEF | n/a: theorem, not def. |
| 15 | EXISTS LEMMA | n/a: no existential conclusion/witness. |
| 16 | SHOW/CHANGE | Neither present or introduced. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every effective binder probed below. hB is necessary; domain/formula fixed. |
| 19 | INEQUALITY | Both hypotheses/conclusion use ≤; scan below. |
| 20 | NORMAL-FORM | `1 ≤ M` is canonical multiplicative lower-bound form used by library and callers. |
| 21 | SYNTAX-GEN | Existing hB explicit, B implicit, numerical inputs explicit match both callers; no restatement improves application. |
| 22 | IMPORT-FANOUT | n/a: no new imports. |
| 23 | CASTS | Seven explicit proof ascriptions disappear with the haves (including the old r₁ natural-to-real expression); Nat.cast_nonneg now infers ℝ from the expected inequality. Zero explicit proof ascriptions retained/introduced; the definition and its genuine cross-type coercions are unchanged. All verified by compiled candidate/module. |
| 24 | INSTANCE-NAME | n/a: no instance declaration or named instance added. |

## Line packing and inequalities

`#check @Roth.one_le_lem6M` at format.width100 (positive.log):
`∀ (p r₁ : ℕ) {B : ℝ}, 1 ≤ B → ∀ (l : ℕ), 1 ≤ Roth.lem6M p r₁ B l`.

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 274 (whole signature) | 87 | none; proof body next | n/a | ok |

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | hB | `1 ≤ B` | none | none |
| 2 | conclusion | `1 ≤ lem6M p r₁ B l` | none | none |
| — | entire signature | no ≥ or > | n/a | n/a |

## Five actual mathlib searches

Raw results `/private/tmp/roth-theta-one-le-m/search0.json` through `search4.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | product of real numbers at least one is at least one, natural factorial at least one | Nat.self_le_factorial, Nat.one_lt_factorial, Nat.factorial_le_pow, Stirling bound; partial factorial matches. |
| B Loogle | `1 ≤ ?a → 1 ≤ ?b → 1 ≤ ?a * ?b` | one_le_mul, Left.one_le_mul, one_le_mul_of_one_le_of_one_le. |
| C LeanSearch | If one is less than or equal to a and b then one is less than or equal to a times b | desired one_le_mul_of_one_le_of_one_le and strict/left/right variants. |
| D source rg | full names one_le_mul_of_one_le_of_one_le, one_le_pow₀, one_le_factorial, factorial_pos in order/factorial sources | GroupWithZero/Basic:441,484; Factorial/Basic:69. No exact paper-specific target expected. |
| E local names | one_le_mul; le_add_of_nonneg_left | Source-backed product hits. Symbol index explicitly unavailable; generated general le_add_of_nonneg_left not returned, independently #check and candidate compilation verified. |

Auxiliary variants considered: one_le_mul, Left/Right.one_le_mul, strict one_lt_mul variants,
Nat.self_le_factorial, Nat.one_lt_factorial, Nat.factorial_pos, one_le_pow₀. Unrestricted
one_le_mul requires MulLeftMono on the whole carrier, unavailable for ordinary real
multiplication, whereas the chosen PosMulMono lemma matches the situation. Common-equivalents
lookup has no relevant discrete/finite/separation/bornology bucket.

Conclusion: partial library matches implement the actual ordered-factor mathematics. No
claim of exhaustive absence from mathlib is made. The public theorem is a preserved project
API about the specific defined coefficient bound, not a new private convenience helper.
Clean isolated anonymous `exact?` failed and bounded `apply?` timed out with only generic
partial transformations. No search imported/used Roth.one_le_lem6M: automation.lean defines
only the immutable M formula under RothProbe23, then anonymous examples. Failed examples
have no reusable user names. Known stalled multi_attempt limitation from earlier leaves was
respected; ordinary isolated compiler trials were used instead.

## Generalisation and inversion

Actual effective type has exactly five binders, no σ/τ/universe/section instances; all five
are preserved exactly. Compiled `binder-negative.lean` with autoImplicit=false, exit1,
records each attempted deletion separately; this failure log is not used for soundness.
`positive.lean` exit0 provides independent concrete counterexamples and the immutable proof.

| Binder | Class/use | Compiled candidate | Result/reason |
|---|---|---|---|
| p : ℕ (explicit) | value, exponent | drop p retaining r₁ | Unknown p in conclusion. It is a free index of the fixed M formula; abstracting its domain requires redefining M, not a mechanical weakening. |
| r₁ : ℕ (explicit) | value, base and exponent | drop r₁ retaining p | Unknown r₁ in conclusion and base lower bound; natural nonnegativity used. No typeclass parents for concrete ℕ. |
| B : ℝ (implicit) | value, base | drop B | Unknown B in hB and conclusion. Generic ordered-semiring formulation would change lem6M itself; not within this proof cleanup. |
| hB : 1 ≤ B (explicit) | proposition, power base bound | drop; weaken 0 ≤ B | Missing hB; weakened proof type mismatch at one_le_pow₀ hB. Exit0 counterexample B=0,p=r₁=0,l=1 rules out both propositions. Even 0<B fails at B=1/2 with same indices (compiled). |
| l : ℕ (explicit) | value, factorial and exponent | drop l | Unknown l in conclusion/factorial bound; no abstract factorial domain supports unchanged formula. |

No pointwise/global predicates, universes, bundled hypotheses or typeclasses occur in this
actual telescope. hB already weak, so strict→weak catalogue does not apply. Converting explicit
indices to implicit would change application rather than mathematical generality and is not
recommended. There are no unused effective hypotheses.

Inversion: `lem6M` occurs only in unfolding, then proof is abstract multiplicative order.
The abstract restatement “product of four factors ≥1 is ≥1” is already supplied by iterated
one_le_mul_of_one_le_of_one_le; powers by one_le_pow₀. Use these directly. A new abstract helper
would duplicate mathlib and add a separately auditable declaration with no benefit. Original
M-specific public theorem remains for existing callers, per explicit API constraint.

## Public literature check

Actual WebSearch queries:
1. `product of real numbers each at least one at least one ordered monoid factorial`
2. `site:leanprover-community.github.io/mathlib4_docs one_le_mul_of_one_le_of_one_le one_le_pow₀`
3. `Formalizing Roth theorem Takloo Bighash Yin M factorial B Lemma 6`

Top results for (1): CMU Noll monoids notes, IISc factorial-monoid exercises, discrete mathematics
notes (broad terminology, no precise target match). For (2): official Ring.Defs, Order.Kleene,
GroupWithZero.Basic documentation; (3): Miller/Takloo-Bighash textbook chapter, Pythagorean
number theory book, author page (no exact public manuscript match). These broad results do
not justify changing the theorem. Relevant primary source is local clean.tex:704–729, Lemma6
and eq16, specifying the exact M formula; the official
[mathlib ordered group-with-zero API](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Order/GroupWithZero/Basic.html)
confirms the abstract power lower-bound principle. No new assumptions/generalisation found.
ChatGPT mathematical MCP unavailable: inspected session tool inventory, no math-opinion tool.
No external message sent. No reliance on search failure as absence evidence.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no terminal by-exact wrapper. |
| 1.2 by rfl | n/a: none. |
| 1.3 rw+exact→rwa | n/a: unfolding changes M to a product; next step assembles four factors rather than reusing same proposition. |
| 1.4 simp+exact | n/a: no simp. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructors | n/a: no conjunction/structure. |
| 1.7 apply+exact | applied composition principle: nested existing lemmas under refine with only two substantive leaves. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta | n/a: no lambdas. |
| 1.10 single-use have | applied: all four lower bounds inlined, no have remains. |
| 1.11 apply+intro | n/a: no function introduction. |
| 1.12 redundant show | n/a: none. |
| 1.13 projections | n/a: no conjunction projections. |
| 1.14 merge rw | n/a: exactly one rw. |
| 1.15 unsqueeze terminal simp | n/a: none. |
| 1.16 squeeze nonterminal simp | n/a: none. |
| 1.17 dot | n/a: chosen binary theorem has no useful object receiver. |
| 1.18 <| | n/a: nesting/product arity uses parentheses for distinct arguments; no trailing tactic argument. |
| 1.19 push Not | n/a: no negation normalization. |
| 1.20 existential helper | n/a: no existential. |
| 2.1 grind | tried whole proof `grind [lem6M]`, failed with unresolved power/factorial inequalities. |
| 2.2 tactics before grind | n/a: final proof has no grind; trial was entire body. |
| 2.3 simpa consolidation | tried `simp [lem6M]`, leaves product inequality; no simp/closing chain to consolidate. |
| 2.4 fun_prop | n/a: no analytic function-property predicate. |
| 2.5 positivity | tried after unfolding, fails “not a positivity goal”; goal is 1≤ not 0≤. |
| 2.6 gcongr | tried after unfolding, did not make progress from scalar1 to a product. |
| 2.7 lia/omega | lia after unfolding fails on non-linear real/power product; arithmetic subgoal replaced with direct ordered-add lemma instead. No omega needed. |
| 2.8 aesop | tried with safe unfold lem6M, exhaustive search leaves inequality. |
| 2.9 norm_num/norm_cast | norm_num [lem6M] alone leaves product inequality; retain norm_num only for 1≤2 and exact_mod_cast for factorial. |
| 2.10 decide | n/a: symbolic real inequality, not closed decidable computation. |
| 2.11 field_simp/ring | n/a: no denominator/algebraic equality. |
| 2.12 linear_combination | n/a: no ring/ring_nf ending or equality certificate. |
| 2.13 wlog | n/a: no symmetric cases. |
| 2.14 calc→term | n/a: no calc. |
| 2.15 <;> | n/a: two remaining leaves need different facts, not a common tactic. |
| 3.1 erw→rw | n/a: no erw. |
| 3.2 fun_prop | n/a: no continuity/measurability. |
| 3.3 omega→lia | satisfied 2.7; no omega in final. |
| 3.4 rfl substitution | n/a: no rcases. |
| 3.5 attributes | n/a: existing paper-specific public bound, no demonstrated automation need; none added. |
| 3.6 simp_all | n/a: no simp_all only. |
| 3.7 maxHeartbeats | none in production; scratch automation uses lower20000 limit only, never a raise. |

## Step back / simplify

Whole-proof grind, simp, aesop, positivity, gcongr, lia, norm_num, exact?, apply? were actually
tried in isolated automation.lean (expected exit1, raw automation.log). None produced a complete
one-tactic proof; apply? bounded out. No self-reference. The selected direct composition
eliminates linear arithmetic and intermediate names without a helper. Holistic simplify
review: PASS-THROUGH after selecting that proof; no duplication requiring extraction, and
no new API warranted. No callable built-in simplify tool in this host; manual review recorded
instead of pretending to invoke an absent tool.

## Verification and gates

All raw artifacts are under `/private/tmp/roth-theta-one-le-m/`.

| Gate | Result | Evidence |
|---|---|---|
| candidate | pass | exact-source-prefix candidate.lean exit0, candidate.log. |
| lake_build_file | pass | `/Users/ramin/.elan/bin/lake build Roth.Theta` exit0; module.log ends “Build completed successfully (2423 jobs).” |
| final live diagnostics | pass | fresh native complete unfiltered final-lsp.json: success=true, partial=false, timed_out=false, failed_dependencies=[], 0 errors17 warnings; none target. |
| independent original proof | pass | positive.lean imports built module but copies exact original M and original eight-line NONSELF proof into ImmutableOriginal23; original-minimal.txt was extracted from immutable2b64544. positive.log exit0 prints full old proof. |
| exact actual original type | pass | positive.lean compares actual built constant type with independent old type, replacing only private probe namespace on M; exact Expr AST equality preserves every binder name/order/type/BinderInfo. Old explicit adapter compiles. |
| retained metadata | pass | No source changes outside proof; original name, docs, theorem/public visibility and header unchanged. Exact type has no hidden section instances. |
| actual standard axioms | pass | positive.log exit0: current built Roth.one_le_lem6M and independent original both depend only on propext, Classical.choice, Quot.sound. |
| new identifiers | pass | le_add_of_nonneg_left local search attempted (index unavailable); actual generated source annotation and successful #check in positive.log + exact-prefix/module compilation verify identifier. Other referenced names were existing and #checked. |
| definition_protected | pass | no definition edit. |
| theorem_statement_protected | pass | byte-identical header and exact compiled type AST. |
| structure | pass | six body lines, two one-line branches, no ∧. |
| naming | pass | no forbidden pattern or rename recommendation. |
| line_packing | pass | full one-line measured table above. |
| inequality_orientation | pass | two ≤ occurrences, no ≥/>. |
| caller contracts | pass | only two callers in same Theta: index_le_lem6 and Θ_lt; no edits needed and module/fullLSP passes. No external target callers found. |
| no trust/limit/scaffolding change | pass | no sorry, axiom, native_decide, limit raise or profiling code in production diff. |
| owner full build+LeanEval | pending owner | intentionally not run by leaf; owner performs final sequential release gates after freeze. |

Focused diff saved as target-diff.patch; source outside target proof verified identical to
release snapshot. No Git mutations, shared logs or rename queue writes.

## Buzz / real profile

Outcome: FAST-BOARD; no heartbeat raises removed or added, no deferrals, no profiling scaffolding
in source. Both baseline and final profiles ran **after all ordinary requests had completed**,
sequentially, with owner explicitly confirming its CPU/compiler window remained drained.

Exact commands (each exit0, separate sequential invocation):

```
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-one-le-m/baseline-prefix.lean
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 /private/tmp/roth-theta-one-le-m/final-prefix.lean
```

| Quantity (ms) | Baseline | Final |
|---|---:|---:|
| Outermost target command | 8.641 | 5.942 |
| Associated async target proof | 260.774 | 116.851 |
| Associated target kernel task | 8.521 | 2.585 |
| Associated target async linter | 6.608 | 5.965 |
| Sum of those disjoint outer tasks | 284.544 | 131.343 |
| Conservative rounded total incl. tiny lazy lem6M.eq_1 generation/check tasks | <286 | <133 |

Raw UTF8 logs profile-baseline.log and profile-final.log; exact line anchors and nonnested
accounting in profile-anchors.txt and profile-summary.json. Kernel inner times8.486/2.551ms
are included in outer kernel task, not added twice. No separate target compiler task appears
(the theorem is proof data). Both measurements are fresh worker profiles, neither inherited.
Neither conservative total reaches750ms, so no borderline repeat is required; both are below
1000ms budget. The result removes linarith, shrinks term/kernel replay, and reduces measured
target cost by about54%. Timing noise still applies to these single accepted measurements.

**Prefix-only scope:** each file is the exact corresponding source prefix from imports through
this declaration at line274, followed only by `end Lemma6; end Roth` as separate commands.
Verified exact-source-prefix equality before profiling. Baseline prefix SHA256
`305180c4f8091ec595cb20934373c7eb59adbff741f83de316b3bd548f3a7c59`, final prefix
`57948f1d3888840428726c3d212af1601fbbf37dc1358bf9bfdfc00575363d1b`.
This does not claim a full-Theta profile pass. Known later index_le_lem6 profiling/default
heartbeat issue remains for owner final whole-module sweep after later cleanup.

## 11-step checklist

- [x] Step1: full required references read.
- [x] Step2: all24 substantive audit items reported.
- [x] Step2.5: five actual search methods, variants and limitations recorded.
- [x] Step2.6: all effective binders compiled-probed; public literature and inversion considered.
- [x] Step2.7: every signature line measured.
- [x] Step2.8: inequality scan table complete.
- [x] Step3: all42 golf rules assessed and relevant automation actually tried.
- [x] Step4: whole-proof/term-mode/abstract-factor alternatives reviewed.
- [x] Step5a: fresh complete unfiltered diagnostics clean of errors, warnings outside target recorded.
- [x] Step5b: actual module, original proof/type, built axioms, structural/protection/performance gates documented.
- [x] Step6a: no rename recommended; shared queue untouched as dispatched.

## Freeze

Source frozen; worker revokes further source edits. Final Theta SHA256 `5c4aa2d1347aba94a182fdbe58a06e78f19ada9568e8f0b33876469ce8781cea`.
Only target proof differs from release snapshot, saved target-diff.patch. Full file979→977
lines; body8→6. No helpers added, no separate-helper audits outstanding. Owner final full
build, separate Roth.LeanEval and checkpoint/push remain owner gates. No worker tool request
or compiler process remains running.


## Owner cumulative publication gates

After leaf source revocation and drained requests, owner ran full `lake build` (73.770 s),
then separate `lake build Roth.LeanEval` (26.327 s); both exit0. All 17 project/source/pin
hashes remained identical through both commands. Theta SHA256 `5c4aa2d1347aba94a182fdbe58a06e78f19ada9568e8f0b33876469ce8781cea`.
Raw logs: `/private/tmp/roth-theta-d23-full.log`, `/private/tmp/roth-theta-d23-leaneval.log`; machine record
`/private/tmp/roth-theta-d23-builds.json`. These completed gates supersede pending owner
entries above. Exact-path staging, commit and successful push publish this checkpoint before
the next original declaration edit. After publication: Theta 23/35, overall 204/264 original
declarations, 9/14 completed files. No new production helper; the prior helper remains separately audited.
