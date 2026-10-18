# Approved instance removal: degreeOf_coeffNone_le (R04)

Scope: only `Roth.degreeOf_coeffNone_le` and this report. Exact approval from parent:
remove BOTH `[Fintype τ]` and `[DecidableEq τ]`, with scoped `omit` before the
original docstring; minimal proof adjustment only. Original snapshot:
`/private/tmp/roth-separation-original.lean`. Other public contracts protected;
wrapper deletion and Domain widening were considered and declined. No helper or Git work.

## Initial audit — written before source edits

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read both skill instructions,
cleanup Phase 4, relevant style/naming/profiling references and the original D09 report.
Fresh native baseline LSP is complete: partial=false, timed_out=false, no failed
dependencies, 0 errors/25 warnings; three warnings concern this target.
Raw evidence uses prefix `/private/tmp/roth-separation-r04-`.
The inherited 576-line module is clean at dispatch HEAD df9cf57.

| # | Audit item | Concrete finding/action |
|---|---|---|
| 1 | Lint | Target unusedSectionVars plus unused Fintype/DecidableEq in type. Apply approved omit. |
| 2 | Have | No have declarations in the two-line proof. |
| 3 | Options | None; no limit changes or warning suppression. |
| 4 | Simp | One terminal unsqueezed simpa; retain. |
| 5 | Naming | degreeOf and coeffNone are the underlying API spellings; _le describes orientation. No forbidden pattern. |
| 6 | Packing | Two signature lines; complete conclusion cannot fit after explicit arguments. Width table below will give exact arithmetic. |
| 7 | By | At end of conclusion line. |
| 8 | Format | Two-space tactics and mathematical ↦; no empty proof lines. |
| 9 | Comments | No proof comments; preserve original docstring verbatim. |
| 10 | Docs | Explains extraction and individual degree bound, with source citation; preserve. |
| 11 | Visibility | Public API; user retained it explicitly. No visibility change. |
| 12 | Structure | Two-line proof, no conjunction or branches; no helper/extraction. |
| 13 | Mathlib | Fresh five searches executed; Fin-indexed partial analogue and Option support API found. Retain existing proof. |
| 14 | Junk def | n/a: theorem. |
| 15 | Exists helper | n/a: no existential statement/helper. |
| 16 | Show | No show expressions. |
| 17 | Push_neg | None. |
| 18 | Generalise | All eight effective binders listed below; approved omission only, no algebra/degree restatement. |
| 19 | Inequality | Single conclusion ≤, no > or ≥ in hypotheses. |
| 20 | Normal form | Natural individual degree inequality already canonical. |
| 21 | Syntax | Explicit polynomial/exponent/variable convenient for direct applications; retain. |
| 22 | Imports | n/a: no new import required. |
| 23 | Casts | 0 dropped / 0 cross-type / 0 load-bearing; no casts in diff. |
| 24 | Instance names | n/a: theorem, no declared instance. |

Issues to fix: exactly the approved extraneous instance binders. Refactoring needed:
none beyond that approval. No pending user input. The original support transport proof
already expresses the mathematics directly; no proof golf is necessary.

## Fresh searches and literature

A Lean-Finder: “multivariate polynomial coefficient degree in another variable bounded
by original degree”; returned monomial_le_degreeOf and degreeOf_le_totalDegree.
B Loogle: `MvPolynomial.degreeOf, Polynomial.coeff`; returned degreeOf_coeff_finSuccEquiv.
C LeanSearch: “degreeOf coefficient optionEquivLeft less than or equal degreeOf some”;
returned totalDegree_coeff_optionEquivLeft_le and natDegree_optionEquivLeft.
E native local name search `degreeOf_coeff` returned target and Fin analogue; index
warming, so no absence inferred. Raw native JSONs are finder/loogle/leansearch/local.json.
D source rg checked degreeOf_coeff, totalDegree_coeff_option, mem_support_coeff_option,
degreeOf_le_iff and degreeOf_eq_sup in Equiv.lean and Degrees.lean; found support transport
L549, Fin analogue L834, degree criterion L235 and finite-support supremum L223.
Auxiliary variants inspected include optionElim_apply_some, totalDegree_coeff_optionEquivLeft_add_le,
and the support theorem. Common-equivalents table: no relevant topology/finiteness entry.

Conclusion: partial Fin-indexed match; existing Option support API supports the retained
local theorem. No absence claim. All six replacement rules considered: no new wrapper;
all searches/generic probes; auxiliary variants; no custom predicate; retained public
theorem because user explicitly declined deletion; module documentation preserved under
the user's stronger instruction. No missing API or cast/typeclass plumbing signal.

Fresh web queries: (1) “multivariate polynomial coefficient degree individual variable
bound polynomial rings arbitrary variables”; (2) “site.homepages.math.uic.edu jan lec11
multivariate polynomials coefficients degree”.
Top relevant hits for (1): Verschelde Lecture 11, Magma Introduction, Magma Element
Operations. For (2): Lecture 11, Polynomialsfactor slides, lec29 interpolation notes.
Primary reference: [Verschelde Lecture 11](https://homepages.math.uic.edu/~jan/mcs320/mcs320notes/lec11.html)
explains collecting terms as a univariate polynomial with polynomial coefficients and
individual degrees. [Magma Element Operations](https://docs.magma-maths.org/BasicRings/MultivariatePolynomialRings/operation-element.html)
defines extraction in one variable with remaining polynomial coefficients.
Inference from finite support: the bound needs no finiteness of the ambient variable
type. Formal proof/probes validate arbitrary-index semiring generality directly.
Local clean.tex source already cited in preserved docstring.
ChatGPT math MCP: actual ALL_TOOLS inventory has no matching tool; unavailable.

## Effective binders and planned fresh compiler probes

| Binder | Use | Candidates / mathematical limit |
|---|---|---|
| {τ : Type*} | remaining variable type | Drop fails unknown τ; Sort does not fit MvPolynomial. Already universe polymorphic. |
| [Fintype τ] | unused | Drop separately, Finite replacement, and drop both; approved weakest form is absence. |
| [DecidableEq τ] | unused | Drop separately and both; approved weakest form absence. |
| {R : Type*} | coefficients | Drop fails unknown R; already universe polymorphic. |
| [CommSemiring R] | polynomial API | Drop and Semiring candidates; CommSemiring needed by MvPolynomial/option equivalence. |
| P | source polynomial | Drop leaves unknown P; structure/value has no independent weaker class. |
| ν : ℕ | coefficient exponent | Drop leaves unknown ν; Polynomial.coeff fixes Nat, no arbitrary-order generalization. |
| j : τ | measured variable | Drop leaves unknown j; arbitrary value already. |

Rows above are mathematical analysis and scheduled probes, NOT yet compiler-verified
negative tests. Fresh outcomes are appended below after probes. No proposition,
strict hypothesis, bundled property, global continuity assumption, concrete field,
or cross-universe equality occurs. Inversion check: the concrete coefficient definition
reduces to the standard Option coefficient API, already abstract over arbitrary τ/R;
another abstract extraction helper would duplicate support transport.

## Fresh probe outcomes

All 11 native lean_run_code requests completed; exact code and full raw diagnostics:
`/private/tmp/roth-separation-r04-probe-{dropBoth,dropFintype,dropDecEq,finite,dropTau,dropR,dropCommSemiring,semiring,dropP,dropNu,dropJ}.json`.
The first four succeed with no diagnostics. DropTau/dropR/dropP/dropNu/dropJ fail with
the named missing identifier under autoImplicit=false. The malformed dropP test also
reaches the default heartbeat cap; no limit was raised, and that secondary error is not
used as the mathematical reason. DropCommSemiring and Semiring both fail synthesizing
CommSemiring R at the polynomial binder. Every effective binder has a fresh actual
compiler test; universe/type and Nat-index limitations are mathematical API analysis.
The weakest index assumption is no assumption, now applied exactly as approved.

## Width and inequality artifacts

Signature text is byte-identical to baseline; measured with Python codepoint lengths.
Compiler reference uses `set_option format.width 100` in the independent probe log.

| Final line | Width | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 108 | 79 | Entire conclusion with := by, 54 codepoints | 79 + 1 + 54 = 134 > 100 | ok, keep break |
| 109 | 58 | none | end of signature | ok |

All explicit arguments already share L108. No partial conclusion identifier is split
off merely to fill the first line.

| Occurrence | Where | Form | Action |
|---|---|---|---|
| 1 | Conclusion L109 | degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P | canonical ≤; retain |
| none | All inherited/explicit binders | No inequality hypotheses; no ≥ or > | no rewrite |
| none | Proof local statements | No local typed inequality or reversed relation | no rewrite |

## All 42 golfing rules — fresh revisit

Fresh native live multi-attempt raw log:
`/private/tmp/roth-separation-r04-attempts.json`. It tests at the first proof line;
the live tool replaces a line and retains the following tactic. Thus extra residual
line errors are reported faithfully and are not treated as whole-proof success.
No one-tactic replacement succeeds.

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl proof. |
| 1.3 | n/a: no rw/exact chain. |
| 1.4 | Already terminal simpa using the monomial bound. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor or conjunction. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction/negation chain. |
| 1.9 | Lambda uses d and hd substantively; cannot eta-reduce to a named function. |
| 1.10 | n/a: no have. |
| 1.11 | Already refine plus mathematical fun ↦. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected have. |
| 1.14 | n/a: no rw. |
| 1.15 | Terminal simpa is already unsqueezed; retain. |
| 1.16 | n/a: no nonterminal simp. |
| 1.17 | .2 and .1 project iff directions directly; no verbose global projection. |
| 1.18 | Parentheses delimit the support iff before projection; not trailing tactic/lambda arguments. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: not a private existential helper. |
| 2.1 | Actual whole-goal grind fails on negated symbolic degree bound. |
| 2.2 | n/a: no retained grind or preparatory tactics before it. |
| 2.3 | Already direct simpa consolidation; actual simp [coeffNone] leaves bound open. |
| 2.4 | n/a: no analytic function property. |
| 2.5 | n/a: comparison of symbolic degrees rather than positivity/nonzero goal. |
| 2.6 | Actual gcongr makes no progress. |
| 2.7 | Actual lia fails; support relation is essential. |
| 2.8 | Actual aesop makes no progress. |
| 2.9 | n/a: no concrete numeric computation or casts. |
| 2.10 | n/a: arbitrary-polynomial bound is not finite computation. |
| 2.11 | n/a: no field division or denominator identity. |
| 2.12 | n/a: no ring-ending equality proof. |
| 2.13 | n/a: no symmetric case split. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: exactly one support goal; no parallel goals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | Already actual lia test at 2.7; no omega. |
| 3.4 | n/a: no rcases/substitution. |
| 3.5 | No new automation attribute: degree inequality is not a simplifier normal-form rewrite; registration changes public behavior outside approved scope. |
| 3.6 | n/a: no simp_all only/context saturation. |
| 3.7 | No maxHeartbeats existed or was introduced. |

Fresh exact? fails to close the initial goal. Fresh apply? finds the existing
degreeOf_le_iff route and many partial generic order routes, with no complete simpler
proof. Full suggestions retained in raw JSON; no absence inferred.
No new source identifier except the language command `omit`; all existing proof lemma
names already resolved in the actual module build and the width/type probe.

Step-back mathematical review: a supported coefficient monomial extends by its extracted
power to a supported original monomial. Evaluate its exponent at some j and compare to
the source degree. The existing two-line support proof states this directly. Term mode
would still need a simplification/transport proof; no helper or broader restatement is
justified. The approved instance omission is the complete change.

## Built module, exact types, independent proofs and actual axioms

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` completed exit 0,
“Build completed successfully (1876 jobs).” Full log:
`/private/tmp/roth-separation-r04-build.log`.

Actual `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-separation-r04-independent.lean`
completed exit 0. Exact source/log:
`/private/tmp/roth-separation-r04-independent.{lean,log}`.
It copies the original coefficient definition (unchanged mathematical value), proves the
exact NEW arbitrary-τ statement independently by finite-support suprema, and checks
`@independentNew = @Roth.degreeOf_coeffNone_le` by rfl only after that proof.
It separately proves the exact ORIGINAL inherited-binder statement by the same
independent finite-support argument, without invoking the target. The explicit
originalAdapter has original order τ, Fintype, DecidableEq, R, CommSemiring, P, ν, j;
it calls the generalized actual built theorem with its NEW explicit arguments.
The explicit ft/de/cs call and equality of the independent ORIGINAL proof and adapter
compile. The target appears only in adapter/checks/#print, never either independent proof.

Actual built target, both independent proofs, originalAdapter, and conservatively
checked public downstream chain exists_separated_representation,
det_hasseDeriv_separated and exists_det_eq_mul all use exactly
[propext, Classical.choice, Quot.sound]. No source helper was added, no private proof
changed. Fresh source search finds no direct target call remaining in Roth (earlier
cleanup inlined its sole old caller); no caller substitution is needed.

Complete unfiltered native module diagnostics:
`/private/tmp/roth-separation-r04-final-lsp.json`: partial=false, timed_out=false,
failed_dependencies=[], success=true, **0 errors/22 warnings**.
Fresh baseline was 0 errors/25 warnings. All three target warnings eliminated.
Other warnings and preserved header are outside this approved one-declaration scope.
No warning suppression.

## Simplify review and gates

Holistic simplify review performed directly (no built-in simplify tool exposed):
PASS-THROUGH. Existing support proof is already direct, no duplicate work, locals,
cast round trips, brittle normalization or helper needed. No decomposition flag.
No source proof changes beyond the instance omission.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual Roth.Separation build exit 0 |
| definition_protected | pass | No def/abbrev or values changed |
| theorem_statement_protected | pass, explicit approval | Only approved scoped omission; conclusion/explicit args/docstring/proof byte-identical; both exact-type probes compile |
| structure_gate | pass | Two physical proof lines, no conjunction/branches/helper |
| naming_gate | pass | API-derived degreeOf_coeffNone_le, no forbidden abbreviations/patterns |
| line_packing_gate | pass | Both signature lines measured above; 134 > 100 |
| inequality_orientation_gate | pass | Single ≤, zero ≥/> in Lean signature/hypotheses |
| no_unintended_breakage at target scope | pass | Actual module build, complete diagnostics, actual target and conservative downstream axioms |
| cumulative original/public/full project/LeanEval | parent-owned | Parent runs after freeze, sequential builds and exact-path commit/push before next edit; not asserted by worker |

`git diff --check` passes. Actual wc: **576 → 577 lines**, +1/-0.
Target keyword-to-proof-end declaration remains **4 → 4 lines**, proof **2 → 2 lines**;
one new scoped omit line outside the preserved docstring/declaration adds no proof line.
Docstring comparison against dispatch HEAD is byte-identical. All other source text
unchanged. Applied change fixes three warnings by removing two needless inherited
instances. No golf-rule rewrite, helper, rename, import, attribute or public deletion.
Renames queued: none. Comments preserved: none present in proof; docstring unchanged.
Refactoring deferred/pending proposal: none within scope.

## Final actual repository profile

After all native Lean/MCP attempts, independent compilers and module build were drained,
with owner compiler/MCP jobs idle, ran exactly:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Exit 0, full raw **112 MiB** log `/private/tmp/roth-separation-r04-profile.log`.
Parser `/private/tmp/roth-separation-r04-profile-table.py` is the supplied repository
anchor parser with errors='replace' when opening the raw log (baseline has three invalid
nested UTF8 bytes; ASCII declaration anchors are intact). Parsed full module table:
`/private/tmp/roth-separation-r04-profile.log.json`.

| Actual repository target | Outer command | Outer async proof | Conservative total | Anchors |
|---|---:|---:|---:|---|
| degreeOf_coeffNone_le | 3.629 ms | 29.701 ms | **33.330 ms** | 2 command / 1 proof |

The parser takes the maximum outer command anchor and maximum outer async proof, sums
them conservatively, and never sums nested nodes. Two command anchors are expected
through scoped omit. Supplied actual R03 baseline target: 8.027 + 21.528 = 29.555 ms.
Final 33.330 ms is comfortably below 750 ms resweep trigger and 1000 ms budget;
ordinary timing variation does not imply a regression/improvement. No whole-project
performance claim. No declaration in this final parsed table reaches 750 ms, so no repeat
required. Buzz outcome FAST-BOARD. No limits or profiler scaffolding in source.

## Completion checklist

- [✓] Step 1 — full golfing/proof-pattern/search/generalisation/gate references read; relevant style/naming/profiling read.
- [✓] Step 2 — all 24 initial audit items written before source edits.
- [✓] Step 2.5 — all five actual native/source search methods and auxiliary variants; literature evidence.
- [✓] Step 2.6 — every effective binder freshly probed; approved weakest index assumption applied.
- [✓] Step 2.7 — every signature line measured, final packing table.
- [✓] Step 2.8 — every inequality occurrence scanned.
- [✓] Step 3 — all 42 golf rules have concrete statuses and applicable live automation tested.
- [✓] Step 4 — mathematical step-back review; retained direct support proof.
- [✓] Step 5a — complete unfiltered native diagnostics, 0 errors/22 warnings.
- [✓] Step 5b — all diff gates; actual build, exact NEW/ORIGINAL independent proofs, explicit original adapter, built axioms, isolated repository profile.
- [✓] Step 6a — no renames needed/queued; no shared sidecar mutation.

## Freeze

Source SHA256: **3c5bbe4d1706e8c7f0c392ceabc1f23565e5e70f295d6dd5f65d5deee3637eac**.

All native Lean/MCP, compiler, build and profiler requests have completed and are drained.
**ALL source ownership is revoked**, including this theorem and every other source path.
I am **report-only**, with no source edits after this freeze. Parent owns cumulative
whole-original/public/all-retained checks, sequential full project and separate LeanEval
builds, exact-path commit and successful cleanup-branch push before the next edit.
No concrete pending proposal or required user input.

## Owner cumulative publication gates

Source FROZEN SHA256 `3c5bbe4d1706e8c7f0c392ceabc1f23565e5e70f295d6dd5f65d5deee3637eac`; leaf ownership revoked and requests drained before owner gates. Owner probe `12312` exit0,50.42s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r04-compatibility.{lean,log,json}`. Owner build session `24948` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,118.53s/31.91s; source hash stable. `/private/tmp/roth-separation-r04-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
