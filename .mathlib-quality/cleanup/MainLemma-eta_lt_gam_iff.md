# Cleanup: `Roth.eta_lt_gam_iff`

Dedicated fresh Phase-4 worker, original 6/27 in `Roth/MainLemma.lean`.
Scope: this declaration and its documentation only; no helpers, imports, callers,
Git operations, shared progress edits, or renames. Entry lines 88–91; final 90–92.
Evidence directory: `/private/tmp/roth-mainlemma-eta-iff/`.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both installed skill
files, the installed cleanup/cleanup-all/buzz commands, style rules, naming
conventions, review stages, and profiling reference. Reference paths resolve under
`/Users/ramin/.local/share/roth-mathlib-quality/skills/mathlib-quality/`.

## Baseline and scope

The owner supplied a clean full build and separate Eval baseline at immutable
HEAD `67e9c5a2e39da43ed87986a26a8d9ce40b7be64f` before dispatch.
Cache fetching: skipped, existing compiled imports available. Worker obtained fresh
complete unfiltered native diagnostics (`diagbefore.json`): success=true,
partial=false, timed_out=false, failed_dependencies=[], zero errors.
Warnings were the user-retained header and the two unused binders in `log_B₁_gt`,
outside this declaration. No warning applies to this target. File dialect: classic.

## Auditing: `eta_lt_gam_iff` (entry lines 88–91, 4 lines)

1. **LINT:** none in target. Full native warnings retained above.
2. **HAVE SCAN:** n/a: neither proof contains a `have`.
3. **SET_OPTION:** n/a: no declaration options, limit raises, or profiling scaffolding.
4. **SIMP SQUEEZE:** n/a: neither selected proof contains simp. The failed terminal
   simp experiment is retained in `attempts.json`; it was never installed.
5. **NAMING:** `eta_lt_gam_iff` is snake_case, expresses the RHS inequality and
   equivalence, and refers to the actual parameter definitions `eta` and `gam`.
   No forbidden abbreviation/pattern, scheme number, reversed orientation, or
   single-letter name; no rename needed. Existing two queued project renames untouched.
6. **LINE PACKING:** repacked both signature lines; complete tables below.
7. **BY PLACEMENT:** `by` terminates the last signature line.
8. **FORMAT:** two-space body, four-space signature continuation, no internal blank
   line, no haveI/letI, one tactic, no semicolon. Original repeated-direction
   automation becomes one explicit `grind [gam, lam]` invocation.
9. **COMMENTS:** no inline proof comments existed; none deleted. Historical source
   quotation preserved verbatim. No proof sketch was hidden in the docstring.
10. **DOCSTRING:** retained equation-(38) explanation and quotation; added the
    concrete `.mp` then `sub_pos.mpr` application tip. Unlike the preceding
    existence theorem, this theorem converts an already supplied (30) to a positive
    denominator gap without any parameter-selection hypotheses.
11. **VISIBILITY:** public is required: `Roth/Main.lean:316,569` uses the theorem.
12. **STRUCTURE:** original body two lines, final one; no conjunction in statement,
    no long branch, not listed as a headline result. No helper extraction warranted.
13. **MATHLIB:** five-method block below. Existing abstract addition/subtraction API
    is a partial match; none identifies the project-specific scaled gamma expression.
    No missing-API extraction signal in this one-tactic normalization proof.
14. **JUNK DEF:** n/a: theorem, not definition.
15. **EXISTS LEMMA:** n/a: not existential or private.
16. **SHOW vs CHANGE:** n/a: no show/change.
17. **PUSH_NEG:** n/a: no push_neg.
18. **GENERALISE:** all three explicit effective binders audited below; no proposition,
    typeclass, universe, implicit, section, or inner statement binders exist.
19. **INEQUALITY:** both inequalities use `<`; no ≥/>. Scan below.
20. **NORMAL-FORM:** RHS `eta δ m < gam δ n m` is the useful project normal form,
    giving `0 < gam δ n m - eta δ m` directly. Equivalence points toward that form;
    no simp attribute or network of pairwise equivalences added.
21. **SYNTAX-GEN:** OK: `.mp` accepts exactly (30), with no assumptions to construct.
    Reversing the iff would make both existing callers less direct.
22. **IMPORT-FANOUT:** n/a: no new imports or changes to re-exports.
23. **CASTS:** 0 dropped / 1 kept cross-type / 0 newly introduced load-bearing.
    `(m : ℝ)` underneath sqrt converts ℕ to ℝ and was only moved with its signature.
24. **INSTANCE-NAME:** n/a: no instance declaration or local instance.

Issues to fix: (1) underpacked signature; (2) duplicated arithmetic directions;
(3) add concrete documentation application guidance. All three addressed.
Refactoring needed: none.

## Line packing — `eta_lt_gam_iff`

Reference, `#check @eta_lt_gam_iff` at format.width=100 (`independent-final.log`):

```lean
eta_lt_gam_iff : ∀ (δ : ℝ) (n m : ℕ), eta δ m + 2 * (1 + 3 * δ) * ↑n * √↑m < ↑m / 2 ↔ eta δ m < gam δ n m
```

The CLI emits this `#check` as one physical line; source packing uses codepoint
measurements and complete term/application units rather than splitting `eta δ m`.

Before:

| Sig line | Chars | Next signature term | Arithmetic | Action |
|---|---:|---|---|---|
| 88 | 42 | `eta δ m` (7) | 42 + 1 + 7 = 50 ≤ 100 | repack |
| 89 | 80 | none, proof follows | n/a | ok |

After:

| Sig line | Chars | Next signature term | Arithmetic | Action |
|---|---:|---|---|---|
| 90 | 93 | `eta δ m` (7) | 93 + 1 + 7 = 101 > 100 | ok |
| 91 | 29 | none, proof follows | n/a | ok |

## Inequality scan — `eta_lt_gam_iff`

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | whole signature and all binders | n/a — no ≥/> in signature | none | none |

The two `<` occurrences remain smaller-side-left. No inner binder occurs.

## Mathlib search-status: `eta_lt_gam_iff`

All native calls were serialized with compiler/profiler work. Raw responses in
`searches.json`; source search was untruncated.

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | `a + b < c iff a < c - b` | `lt_sub_iff_add_lt`, primed variant, `lt_sub_right_of_add_lt` |
| B Loogle | `?a + ?b < ?c ↔ ?a < ?c - ?b` | `Nat.add_lt_iff_lt_sub_right`; Nat-specific, not this real statement |
| C LeanSearch | real addition strict inequality equivalent subtraction | `lt_sub_iff_add_lt`, `sub_lt_iff_lt_add`, `lt_of_sub_pos` |
| D Grep source | `eta_lt_gam_iff`, `add_lt_iff_lt_sub_left/right`, `lt_sub_iff_add_lt` | Generic to_additive API and aliases in Algebra/Order/Group/Unbundled/Basic; no project-named theorem |
| E lean_local_search | `lt_sub_iff_add_lt` | index=error; only Nat/EReal textual results. Not evidence of absence; fallback untruncated source inspection and compiled `#check @lt_sub_iff_add_lt` succeeds |

Auxiliary variants tried: primed, left/right, subtraction-to-addition aliases;
compiled `exact?` and `apply?` in the true pretarget context. exact? failed;
apply? produced only unsolved generic iff transformations. No self-use was possible.
Common-equivalents lookup matched: no; none of the topology/finiteness/bornology buckets.
Concluded: partial match `lt_sub_iff_add_lt`; retain the project-specific conversion.
The reusable abstract subtraction principle already exists and is not redeclared.
The whole RHS still needs the gamma/lambda normalization and rational coefficient
normalization, which the explicit grind hints perform. No new wrapper/helper/API.

## Generalisation status: `eta_lt_gam_iff`

| # | Binder | Class | Used as | Mechanical candidates tried | Verification | Result |
|---|---|---|---|---|---|---|
| 1 | `(δ : ℝ)` | structure value | argument of eta/gam, coefficient 1+3δ | drop; concrete→abstract considered | drop file `drop-δ.lean` | required: deletion leaves unknown δ in statement; no positivity assumption exists to weaken |
| 2 | `(n : ℕ)` | structure value | lambda/gamma index and real coefficient | drop; Nat→abstract considered | `drop-n.lean` | required: deletion leaves unknown n in statement; type constrained by existing gam |
| 3 | `(m : ℕ)` | structure value | eta/gam index, sqrt cast and RHS m/2 | drop; Nat→abstract considered | `drop-m.lean` | required: deletion leaves unknown m; eta’s exponent uses this Nat |

Drop probes disable autoImplicit so accidental automatic generalization cannot mask
the missing binder. No parameter is a proposition, typeclass, decidability argument,
type variable, or universe; strict→weak, class-parent, point-localization and universe
catalogue substitutions consequently have no applicable target. No bundled hypothesis.

2.6b: rejected drop candidates are never installed. Exact type metadata independently
confirms all explicit binders, their names/order/default BinderInfo, no universes.
2.6c: no useful big-change candidate remains. Replacing ℝ/ℕ in this public theorem
would require redefining the three already audited parameter functions, including
real rpow/sqrt and a natural iteration exponent; this is a different definition
development with no demonstrated caller benefit, not an assumption weakening.
Inversion check fires after unfolding gam/lam: abstract arithmetic remains; its
general principle is already mathlib’s `lt_sub_iff_add_lt`. Do not add another helper.
2.6e: no small-safe weakening was available; all original effective binders retained.

### Literature search status

WebSearch queries and full results saved in `literature.json`, `literature2.json`.
Queries: `Roth main lemma eta gamma inequality 30 generalization`;
`ordered group addition subtraction inequality equivalence generalization`;
`"Formalizing Roth" "main lemma"`; and
`site.ncatlab.org ordered group translation invariant order`.
Search results included these relevant routes (other, irrelevant Roth arithmetic
progression results were not used to justify this Diophantine statement):

* [nLab ordered group](https://ncatlab.org/nlab/show/ordered%2Bgroup): translation
  compatibility is the abstract arithmetic idea, already covered by mathlib.
* [Inequality](https://en.wikipedia.org/wiki/Inequality_%28mathematics%29): broad
  addition/subtraction compatibility; no stronger project parameter theorem found.
* [Linearly ordered group](https://en.wikipedia.org/wiki/Linearly_ordered_group):
  order and translation compatibility, likewise no new project assumption removal.
* [Ordered-group textbook preview](https://www.ams.org/bookstore/pspdf/gsm-176-prev.pdf)
  and [IsarMathLib ordered groups](https://isarmathlib.org/OrderedGroup_ZF.html):
  supporting formal general context, without a statement using eta/gam.
* [Quantitative Roth results](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DEAA9636BD8906FA38315A64B014A183/S1446788700030159a.pdf/some_quantitative_results_related_to_roths_theorem.pdf):
  a related theorem search hit, not evidence for changing this elementary equivalence.

An additional focused query `Roth main lemma eta gamma inequality generalization`
returned, in order, the [Princeton Diophantine notes](https://web.math.princeton.edu/mathlab/jr02/diophantine.pdf),
*An Invitation to Modern Number Theory*, and a van der Corput inequality paper.
The third hit is unrelated and was discarded; the notes explicitly identify the
equivalence with η<γ in their parameter setup. The primary PDF was opened and
searched, supporting the same formulation rather than any additional assumptions.
The ordered-group query’s first three hits (ScienceDirect overview, Wikipedia
inequality, and its archived mirror) were captured in the original raw response;
nLab was then queried explicitly for the canonical translation formulation.

The exact authoritative local source is `clean.tex:1355–1358`, equation (38):
“Inequality \eqref{roth:eq30} is equivalent to” followed by `η < γ`.
That quotation and project interpretation are preserved.
ChatGPT math MCP: n/a, no callable mathematical second-opinion tool available.
Literature-driven big-change candidates: none; general arithmetic already exists.

## Golfing rule pass

### Phase 1: instant wins

* [1.1] by exact wrapper — n/a: absent.
* [1.2] by rfl — n/a: absent.
* [1.3] rw + exact — n/a: closing tactic was linarith.
* [1.4] simp + exact — n/a: no simp/exact pair.
* [1.5] trailing rfl — n/a: absent.
* [1.6] constructor/exact pair — replaced both original directions with one grind;
  no ready constructor terms existed.
* [1.7] apply + exact — n/a: absent.
* [1.8] by_contra + push_neg — n/a: absent.
* [1.9] eta-reduce lambdas — n/a: no lambdas.
* [1.10] inline single-use have — n/a: no have.
* [1.11] apply + intro — n/a: no apply.
* [1.12] redundant show — n/a: absent.
* [1.13] have + projections — n/a: absent.
* [1.14] merge rw — n/a: already one rw list; ultimately absorbed by grind hints.
* [1.15] unsqueeze terminal simp only — n/a: absent.
* [1.16] squeeze nonterminal simp — n/a: absent in selected proof.
* [1.17] dot notation — n/a: no explicit lemma application in proof.
* [1.18] use <| — n/a: no nested term arguments needing parentheses.
* [1.19] push_neg → push Not — n/a: absent.
* [1.20] inline trivial ∃ — n/a: no existential helper.

### Phase 2: automation upgrades

* [2.1] grind whole proof — tried actual pretarget, closes with [gam,lam]; applied.
* [2.2] delete tactics before grind — applied: unfolding rw and constructor/intros
  removed, retaining explicit unfold hints.
* [2.3] simpa consolidation — tried simp with gam/lam/lt_sub_iff_add_lt;
  residual iff, unused subtraction lemma; rejected.
* [2.4] fun_prop — n/a: no function property goal.
* [2.5] positivity — n/a: iff between two unrestricted strict inequalities.
* [2.6] gcongr — n/a: equivalent rearrangement, not monotonicity or calc.
* [2.7] lia/omega — n/a: arithmetic is over ℝ with sqrt/rpow atoms, not Nat/Int.
* [2.8] aesop — actual pretarget attempt fails with two implication branches.
* [2.9] norm_num/norm_cast — n/a: symbolic real iff, not numeric/cast equality.
* [2.10] decide/kernel — n/a: open real parameters, no finite computation.
* [2.11] field_simp/ring — n/a: not an equality; grind handles rational scaling.
* [2.12] linear_combination — n/a: no ring/ring_nf exit or equality certificate.
* [2.13] wlog — n/a: no symmetric case split.
* [2.14] collapse calc — n/a: no calc.
* [2.15] multiple goals <;> — original already shares linarith across both sides;
  whole-goal grind removes the need for multiple goals.

### Phase 3: cleanup

* [3.1] erw → rw — n/a: no erw.
* [3.2] continuity/measurability → fun_prop — n/a: neither tactic or property.
* [3.3] omega → lia — n/a: neither appears, real arithmetic.
* [3.4] rcases with rfl — n/a: no rcases.
* [3.5] register automation lemma — n/a: existing project conversion has no need
  for a global simp/grind attribute; explicit hints make the proof self-contained.
* [3.6] simp_all — n/a: no simp_all.
* [3.7] remove maxHeartbeats — n/a: no limit override existed or was added.

## Step 4: step back / holistic review

The whole proof is now one tactic. Real pretarget `exact?` failed, and `apply?`
offered unsolved generic iff transformations rather than a matching theorem.
The native multi-attempt response includes “No goals to be solved” on the following
old tactic after successful replacement; this is not mistaken for a whole-file pass.
Actual edited source subsequently passed complete native diagnostics and compilation.
Term mode would still need gamma normalization and coefficient arithmetic, making
the mathematical intent less clear. No haves to fold, redundant steps, missing
helper, or duplicated skeleton worth extracting. Independent holistic simplify
review of this small diff found no further change; built-in simplify skill is not
available in this runtime, and the owner retains file-wide final simplify work.

## Verification and independent original audit

`independent.lean` uses the actual source prefix before the target, then the **entire
original proof** copied from immutable `project-original.lean` under a fresh name,
then the actual revised declaration. It imports no Roth.MainLemma and neither old
proof nor searches can use the current theorem. Exact original text is retained
in `original-target.txt`, revised text in `current-target.txt`.

The compiler checks exact type AST equality, universe parameter equality, the
entire effective telescope (δ,n,m; all default BinderInfo), and infers/checks the
actual opaque values of both proofs (`value! true`). It collects and restricts
axioms to propext/Classical.choice/Quot.sound, then prints both axiom sets.
`independent-final.json`: exit 0; raw metadata in `independent-final.log`.
The first metadata harness used `ConstantInfo.value!` without allowOpaque=true;
that harness failed and is retained as `independent-failed-value-default.*`.
Correcting the harness did not change project source or either proof.

## Buzz pass — scoped to `eta_lt_gam_iff`

Outcome: FAST-BOARD. Both original and revised versions are under 1000ms.
The revised one-tactic proof is also faster in this comparison.

| Version | Command root | Proof/other async | Compiler/kernel roots | Lint root | Total |
|---|---:|---:|---:|---:|---:|
| Original | 7.512ms | 258.833ms | 7.909ms | 6.921ms | 281.175ms |
| Revised | 8.567ms | 145.086ms | 51.091ms | 3.485ms | 208.229ms |

Command: `/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true
-Dtrace.profiler.threshold=0 <exact-prefix.lean>`. Prefix through actual target plus
`end Roth`, final doc included; no tracing scaffolding added to project source.
External 420-second bound; both exit 0, strict UTF-8 decode and complete process
drain recorded. Actual command-boundary marker: `/-- Inequality (30)` through the
next column-zero Elab.command, with `Roth.eta_lt_gam_iff` in the anchored span.
`before-timing.json` and `after-timing.json` enumerate **every** disjoint column-zero
Elab.command/Elab.async root with raw line anchor. The owner canonical parser excludes
all nested children, standalone Meta.whnf internal events, and end-Roth command/lint.
Both measured totals <750ms; no repeat or slow-sample repair is required.

Before raw SHA256: `af8e49c6f1357e138b60fda9e6fa031fd98139c8b9419005e9a1d75d7296ad99`.
After raw SHA256: `f5030250f0205a11a527112fbdcfa1631aef708c400e162b8feff2bba6f8c1b8`.
Source hashes and full commands/status/timing/drain metadata are retained alongside.
Corrected independent heartbeat check: original 1588, revised 1055 heartbeats,
both below the default 200000; `heartbeats-final.log/.json`, compiler exit 0.
maxHeartbeats raises removed 0; added 0. Deferrals: none. No consumer source change
or import change; the owner’s pre-existing Main performance queue is unaffected.

## Final gates and completion

`lake build Roth.MainLemma Roth.Main` completed successfully (2465 jobs), exit 0,
74.835s; complete log and metadata in `affected-build.log/.json`. Only pre-existing
warnings occur; zero target warnings or compile errors. No call-site edits required.
All three rejected drop probes have their expected unknown-identifier errors and
exit 1 saved under `drop-delta`, `drop-n`, `drop-m`; none was installed in source.
The first heartbeat harness lacked `#`/the heartbeat utility import, failed syntax,
and is retained. Corrected scratch harness imports the existing compiled utility;
no project import changes were made.

### Gate status — `eta_lt_gam_iff` (Phase 4)

| Gate | Result | Details |
|---|---|---|
| lake_build_file | ✓ pass | actual `/Users/ramin/.elan/bin/lake build Roth.MainLemma Roth.Main`, exit 0, 74.835s |
| definition_protected | ✓ pass | worker diff has no def/abbrev edit |
| theorem_statement_protected | ✓ pass | lexical wrapping only; exact effective type AST/universes/binder metadata identical |
| structure_gate | ✓ pass | one body line ≤30, no ∧ or >10-line branch |
| naming_gate | ✓ pass | descriptive snake_case; no forbidden pattern/abbreviation; no rename |
| line_packing_gate | ✓ pass | complete 93/29-codepoint final table, next application would be 101 |
| inequality_orientation_gate | ✓ pass | scan emitted; no ≥/> in code signature or hypotheses |
| cumulative_no_unintended_breakage | ✓ pass | both caller modules build; public API unchanged |
| no-limit-raise / no-scaffolding | ✓ pass | zero additions in actual worker diff |

Overall: pass.

Fresh final **unfiltered** native diagnostics are saved in `native-final.json`
and `native-caller-final.json`. Both return success=true, partial=false,
timed_out=false, failed_dependencies=[], zero errors. MainLemma retains only
the header and two `log_B₁_gt` warnings; Main retains only its known header and
unused-variable warnings. No warning belongs to the cleaned target.

After the affected build, `actual-module.lean` imports **rebuilt Roth.MainLemma**
and replays the entire immutable original proof under a fresh name, without using
the revised theorem in that proof. Its `getConstInfo ``Roth.eta_lt_gam_iff` inspects
the authoritative imported constant; `value! true` obtains the **actual compiled
opaque body**, whose inferred type checks against its actual constant type.
Exact old/current type AST, universe, telescope names/order/default BinderInfo and
standard-axiom checks all pass. Compiler exit 0, 36.097s, full output and metadata
in `actual-module.log/.json`. Both this and the import-free prefix replay produced
the same audit output hash `f477bfa07f15748466dd82031d1a2cf5fee080559b289bb3359b663504eb7857`.

New-identifier verification: `grind` was tested natively and compiled; `gam` and
`lam` are unchanged local definitions; `sub_pos.mpr` is documentation guidance.
No new external theorem reference is introduced by the proof.

### Result: `eta_lt_gam_iff`

Before: 4 declaration lines. After: 3. Saved: 1; body 2→1.
Documentation adds two lines; whole file 694→695.
Audit issues found: 3. Fixed: 3. Refactoring deferred: 0.
Rules applied: 2.1, 2.2; signature packing and documentation improvement.
Gates: pass. Renames queued: none. Comments preserved: none present in proof;
historical source quotation preserved verbatim. Refactoring needed: none.

Phase checklist:

- [✓] Step 1 — reference docs read.
- [✓] Step 2 — full 24-item audit printed above.
- [✓] Step 2.5 — five-method mathlib search and index-error fallback recorded.
- [✓] Step 2.6 — all effective binders, catalogue candidates, inversion/literature audited.
- [✓] Step 2.7 — complete before/after codepoint signature tables emitted.
- [✓] Step 2.8 — inequality occurrence scan emitted.
- [✓] Step 3 — all 42 golfing rules have explicit status.
- [✓] Step 4 — whole-tactic, exact?/apply?, term and alternative strategy reflection complete.
- [✓] Step 5a — fresh complete unfiltered native target and caller diagnostics pass.
- [✓] Step 5b — diff gates and actual affected module build pass.
- [✓] Step 6a — no rename required; existing queue untouched.

Final source SHA256: `770a6ff1cb79679adfd37cdf765f475e33e1300497537ccd2fb3ae1508f6c26d`.
Main SHA256 remains `77379716d68354eef40ba1ae8c10c89f91dcffcc5ec4cfcee33655319e15a137`.
Final profile prefix was compared byte-for-byte with actual current source through
the target plus `end Roth`; matching hashes are in `source-manifest.json`.
All worker-owned compiler sessions and native calls have completed and drained.
No project source edit followed the final frozen profile or affected build.
The owner retains independent final review, full build/separate Eval, publication,
shared progress and later file-wide phases; none is claimed as worker Git work.
