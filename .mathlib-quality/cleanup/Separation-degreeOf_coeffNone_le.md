# Declaration 9: `Roth.degreeOf_coeffNone_le`

Scope: only this public theorem and this report. Public index-instance omission is pending;
preserve the exact original public contract. No new helper is planned. Parent owns Git,
cumulative compatibility, full project and LeanEval builds.

## Initial audit — written before any source edit

HEAD `9f2312d`; source 599 lines. Native full unfiltered baseline is
`/private/tmp/roth-separation-d09-initial-lsp.json`: complete, 0 errors/31 warnings.
Target has unused Fintype/DecidableEq warnings; preservation is intentional pending approval.
Valid actual-module baseline supplied by parent:
`/private/tmp/roth-separation-d08-final-profile.log`, target command 3.743 ms + outer async
proof 62.772 ms = 66.515 ms, below the 1000 ms budget.

Read Lean and mathlib-quality skills, cleanup Phase 4, golfing-rules and proof-patterns,
mathlib-search, generalisation-patterns, cleanup-gates, style, naming and profiling references.

| # | Audit | Finding / planned action |
|---|---|---|
| 1 | Lint | Two index-instance warnings; preserve public signature pending approval. |
| 2 | Have scan | No have/let declarations. |
| 3 | set_option | None. |
| 4 | Simp | Terminal simpa is unsqueezed; nonterminal rw explicit. Test support API. |
| 5 | Naming | degreeOf and coeffNone retain referenced API spelling; `_le` describes bound; no banned names. |
| 6 | Packing | Two signature lines; measure next complete conclusion before retaining. |
| 7 | By | End of second signature line. |
| 8 | Format | Two-space tactics; change tactic lambda `=>` to mathematical `↦` when editing. |
| 9 | Comments | Zero inline proof comments; preserve docstring verbatim. |
| 10 | Docs | Explains coefficient extraction and source degree bound; sufficient. |
| 11 | Visibility | Public API used by exists_separated_representation; retain. |
| 12 | Structure | Four physical tactic lines; no branches or conjunction; no helper needed. |
| 13 | Mathlib | Five searches executed; partial Fin-indexed analogue and general Option support API found. |
| 14 | Junk def | n/a: theorem. |
| 15 | Exists | n/a: no existential helper. |
| 16 | Show | None. |
| 17 | push_neg | None. |
| 18 | Generalise | Probe all effective binders; index omissions remain pending. Check algebra prerequisites. |
| 19 | Inequality | Single conclusion ≤; no reverse inequalities. |
| 20 | Normal form | Natural degree inequality is canonical. |
| 21 | Syntax | Explicit P, coefficient index, and variable are convenient for direct bounds; no restatement. |
| 22 | Import fanout | No new imports planned. |
| 23 | Casts | No casts or redundant ascriptions in target proof. |
| 24 | Instance names | n/a: theorem, no named instance. |

Initial action: test direct support transport through `mem_support_coeff_optionEquivLeft`,
which can remove coefficient/nonzero rewriting and explicit mapDomain simplification.
No public theorem removal or signature change will be applied.

## Five actual searches and literature

All five native searches completed, raw outputs under `/private/tmp/roth-separation-d09-`:

| Method | Query | Result / raw suffix |
|---|---|---|
| A Lean-Finder | taking a coefficient in one variable of a multivariate polynomial does not increase degree in another variable | `degreeOf_coeff_finSuccEquiv`, `monomial_le_degreeOf`; `finder.json`. |
| B Loogle | `MvPolynomial.degreeOf, Polynomial.coeff` | `degreeOf_coeff_finSuccEquiv`; `loogle.json`. |
| C LeanSearch | degreeOf coefficient optionEquivLeft less than or equal degreeOf some | `totalDegree_coeff_optionEquivLeft_le`, `natDegree_optionEquivLeft`; `leansearch.json`. |
| D Source rg | `degreeOf_coeff`, `totalDegree_coeff_option`, `coeff_optionEquiv`, `degreeOf_le_iff` | Equiv.lean L549 support transport, L834 Fin-indexed degree analogue; Degrees.lean L235 degree criterion. |
| E Name pattern | `degreeOf_coeff` | Fin-indexed analogue and target; `local.json`, index unavailable, so source hits establish presence only. |

Auxiliary variants inspected: `mem_support_coeff_optionEquivLeft`,
`optionEquivLeft_coeff_some_coeff_none`, `totalDegree_coeff_optionEquivLeft_add_le`,
`totalDegree_coeff_optionEquivLeft_le`, `degreeOf_coeff_finSuccEquiv`,
`mem_support_coeff_finSuccEquiv`, `degreeOf_eq_sup`, and `Finsupp.optionElim_apply_some`.
The common-equivalents table has no applicable topology/finiteness/bornology entry.
Actual native `exact?` failed; `apply?` suggested only partial generic order routes and
`degreeOf_le_iff`, no complete proof. The unfiltered response is retained, including the
many unhelpful generic order suggestions. No unsupported claim of absence is made.

Conclusion: mathlib supplies a closely related Fin-indexed degree result and exactly the
general Option support transport needed by this project's coefficient API. Retain the
existing public theorem and build on that API. Its public removal is not authorized.
The proof does not exhibit repeated casts, typeclass plumbing, or wrapper round trips;
no missing auxiliary API or new helper is needed. All six replacement rules considered:
no newly introduced wrapper; actual searches/generic probes; auxiliary variants inspected;
no custom predicate; no exact equivalent proposed for deletion; existing documentation
preserved under the user's contract rather than expanded.

Actual web queries:
1. `multivariate polynomial coefficient polynomial degree in each variable bound polynomial rings`
2. `site.math.ucsd.edu polynomial rings several variables degree coefficients polynomial`

The second query's top three results were McKernan *Polynomial rings*, Yixuan Zhou's
thesis preliminaries, and Rogalski's *Math 200 lecture notes*. The general-query results
also exposed the primary teaching source inspected in full: [Verschelde, Lecture 11:
Univariate and Multivariate Polynomials](https://homepages.math.uic.edu/~jan/mcs320/mcs320notes/lec11.html).
It explains individual variable degrees and collecting terms to regard a multivariate
polynomial as univariate with polynomial coefficients (L129–157). This supports the
coefficient-ring interpretation, while the formal support proof establishes the precise
bound. The project's `.mathlib-quality/references/clean.tex` L374 explicitly states the
individual-degree bounds on coefficient polynomials. None of these mathematical
descriptions needs finiteness of the entire variable index type; finite polynomial support
is enough. Arbitrary-index semiring generality is already supplied by the local API.
Math ChatGPT MCP: unavailable; actual tool inventory search returned no matching tool.

## Signature packing and inequalities

Initial and final signatures are byte-identical; Python codepoint widths:

| Line | Width | Next complete syntactic unit | Packing arithmetic | Result |
|---|---:|---|---|---|
| 104 | 79 | conclusion plus `:= by` (54 characters stripped) | 79 + 1 + 54 = 134 > 100 | retain break |
| 105 | 58 | none | n/a | packed |

All explicit parameters are already on the first line. The conclusion is one expression;
moving only its initial identifier is not a useful signature packing operation.
The width-100 compiler reference is saved in the independent proof log.

| Occurrence | Location | Form | Action |
|---|---|---|---|
| 1 | conclusion L105 | `degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P` | canonical ≤ orientation |
| none | inherited/explicit binders | no inequality hypotheses and no ≥ or > | no rewrite/rename |

## Every-binder mechanical generalisation probes

Actual native `lean_run_code` calls, each self-contained with `autoImplicit false`,
are saved as `/private/tmp/roth-separation-d09-probe-NAME.json`; each contains exact code
and unfiltered result. These are isolated public proposals, not applied source changes.

| Binder | Class / use | Candidates actually tested | Compiler result / disposition |
|---|---|---|---|
| `{τ : Type*}` | type variable indexing all variables | dropTau | Unknown identifier τ; retain. Already universe-polymorphic; Sort would not fit MvPolynomial. |
| `[Fintype τ]` | inherited class, unused in new proof | dropFintype, finite, dropBoth | All compile; absence is weakest. Pending public omission proposal; not applied. |
| `[DecidableEq τ]` | inherited decidability, unused | dropDecEq, dropBoth | Both compile; pending public omission, not applied. |
| `{R : Type*}` | coefficient type | dropR | Unknown identifier R; retain. Already universe-polymorphic. |
| `[CommSemiring R]` | MvPolynomial/optionEquivLeft API requirement | dropCommSemiring, semiring | Both fail to synthesize CommSemiring R at polynomial binder. Retain; nonassociative/NonUnital changes would require different API, not a safe weakening. |
| `(P : MvPolynomial (Option τ) R)` | polynomial whose degrees are compared | dropP | Unknown P, followed by secondary heartbeat failure on malformed term; failure is the missing identifier. Retain. |
| `(ν : ℕ)` | exponent of ordinary polynomial coefficient | dropNu | Unknown ν; retain. Arbitrary ordered index cannot index Polynomial.coeff. |
| `(j : τ)` | remaining variable whose degree is bounded | dropJ | Unknown j; retain. |

No proposition hypotheses, bundled properties, global pointwise conditions, strict
bounds, fixed concrete coefficient fields, or cross-universe equalities occur, so their
catalogue weakenings do not apply. No finite computation is used. Inversion check:
`coeffNone` unfolds once to a coefficient of the standard option equivalence; its support
transport is exactly the generic API already found. A new abstract extraction lemma would
duplicate that API; no additional restatement is proposed.

Concrete pending proposal: drop `[Fintype τ] [DecidableEq τ]` together from this public
theorem, as recorded in the parent's instance proposal menu. The native `dropBoth` proof
compiles without either instance. Parent notification sent; not applied.

## All 42 golfing rules

| Rule | Concrete status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl proof. |
| 1.3 | Removed the nonterminal coefficient rewrite; no rw/exact pair remains. |
| 1.4 | Applied terminal `simpa using` directly to the support-derived monomial degree bound. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no conjunction constructor. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction or negation-pushing proof. |
| 1.9 | Lambda uses both monomial and membership evidence, not eta-reducible. |
| 1.10 | n/a: no have declaration in original or final target. |
| 1.11 | Already refine with fun; mathematical lambda spelling improved to ↦. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected have. |
| 1.14 | n/a: no consecutive rw; original single rw removed by support API. |
| 1.15 | Terminal simpa remains unsqueezed; no terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | `.1 hd` projects an iff after explicit R; no awkward full-name projection. |
| 1.18 | Parentheses delimit iff application and projection; no trailing tactic/lambda argument removable. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no private existential helper. |
| 2.1 | Native live whole-proof grind failed with negated degree inequality. |
| 2.2 | n/a: no retained grind or preparatory grind steps. |
| 2.3 | Support API gives direct simpa; broad simp [coeffNone] leaves degree bound open. |
| 2.4 | n/a: no analytic function-property goal. |
| 2.5 | n/a: comparison of unrelated symbolic degrees, no positivity subgoal. |
| 2.6 | Native gcongr failed to make progress. |
| 2.7 | Native lia failed; support relation is required rather than arithmetic. |
| 2.8 | Native aesop failed, no progress. |
| 2.9 | n/a: no concrete numeric computation or casts. |
| 2.10 | n/a: arbitrary polynomial bound is not finite decidable computation. |
| 2.11 | n/a: no denominator/field expression. |
| 2.12 | n/a: no ring-ending equality proof. |
| 2.13 | n/a: no symmetric case split. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: exactly one support subgoal. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no legacy continuity/measurability tactics. |
| 3.3 | n/a: no omega; lia already attempted under 2.7. |
| 3.4 | n/a: no rcases/rfl. |
| 3.5 | No new attribute: this degree inequality is not a simplifier normal-form rewrite. |
| 3.6 | n/a: no simp_all only or context saturation needed. |
| 3.7 | No heartbeat limits existed or were added. |

Step back: the mathematical proof is that every coefficient monomial extends to a
supported original monomial, so its exponent is bounded by the original degree.
The existing support API says exactly that and avoids reconstructing exponent vectors
manually. The two-line proof makes this route visible and adds no helper.
Native live attempt logs are `attempts.json` and `attempts2.json` under the same prefix.
The successful multi-attempt snippet reported “No goals to be solved” on an old remaining
source tactic, because live replacement substitutes a line rather than deleting the
remainder. The actual edited module build and complete diagnostics validate the final
two-line proof; this is not counted as a successful whole-file diagnostic from that probe.

Comments-preserved: zero inline comments before and after; docstring unchanged verbatim.
Casts: 0 dropped / 0 kept cross-type / 0 kept load-bearing. Only the explicit coefficient
type R argument is required by the support lemma; it is not a cast.

## Independent original type and actual built axioms

`/private/tmp/roth-separation-d09-independent.lean` copies the ORIGINAL coefficient
definition and exact inherited binder order from `/private/tmp/roth-separation-original.lean`.
It proves the original bound independently by rewriting both degrees as finite support
suprema and applying `Finset.le_sup`, without using the target theorem or its current
`degreeOf_le_iff` proof. `example : @independent = @Roth.degreeOf_coeffNone_le := rfl`
then checks the exact original quantified type using definitional equality of coefficient
definitions and proof irrelevance. The target is referenced only in this compatibility
check, #check, and #print axioms, never in the independent proof.

Actual invocation `/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-separation-d09-independent.lean`
exited 0. Full log `/private/tmp/roth-separation-d09-independent.log`. It includes
`format.width 100` signature output and #checks of the support lemma, degree criterion,
monomial degree bound and optionElim evaluation rule.
Both actual built `Roth.degreeOf_coeffNone_le` and `OriginalD09.independent` use exactly
`[propext, Classical.choice, Quot.sound]`. No private declaration changed or was added.

| New identifier in source diff | Verification | Result |
|---|---|---|
| `MvPolynomial.mem_support_coeff_optionEquivLeft` | source Equiv.lean L549, actual #check and module compilation | pass |

All other identifiers in the two added source lines were already present. `↦` is syntax.

## Simplify and buzz passes

Holistic simplify review performed directly; no built-in simplify tool is exposed.
Outcome PASS-THROUGH after the support-API change. There is no remaining duplication,
unnecessary local state, brittle conversion, or arithmetic automation to factor out.
No new helper was introduced and no decompose-proof flag is needed.

Actual repository module profile:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Exit 0, full raw `/private/tmp/roth-separation-d09-final-profile.log` (110 MiB).
Parser `/private/tmp/roth-separation-profile-table.py`, final anchored table
`/private/tmp/roth-separation-d09-final-profile.log.json`.
Target command 4.112 ms + outer async proof 36.412 ms = **40.524 ms**, one actual anchor
of each kind. Nested nodes are not double-counted. Supplied actual-module baseline
66.515 ms → final 40.524 ms. This observation concerns only this declaration;
no whole-project speed claim is made. Target is below both the 750 ms resweep trigger
and 1000 ms budget. Buzz outcome FAST-BOARD. No heartbeat-limit increases or profiling
scaffolding in source; no performance deferral.

## Verification gates and result

Actual `/Users/ramin/.elan/bin/lake build Roth.Separation` exited 0, “Build completed
successfully (1876 jobs).” Complete build log `/private/tmp/roth-separation-d09-build.log`.
Native unfiltered final `/private/tmp/roth-separation-d09-final-lsp.json` is complete
(`partial=false`, `timed_out=false`, no failed dependencies): **0 errors/32 warnings**.
Baseline was 31 warnings. The new warning is unusedSectionVars for the target, since
the new proof no longer indirectly consumes Fintype/DecidableEq via coeff_coeffNone.
The two existing public-instance-in-type warnings remain. No warning was suppressed;
all three await the same pending public instance-omission decision. Header warning
remains under explicit user preservation, and other warnings belong to other declarations.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build above, exit 0 |
| definition_protected | pass | no definition/abbrev changed |
| theorem_statement_protected | pass | exact signature byte-identical; independent original-type check compiled |
| structure_gate | pass | four → two proof lines; no conjunction or branches |
| naming_gate | pass | degreeOf/coeffNone API names plus `_le`; no banned pattern |
| line_packing_gate | pass | both signature lines measured above; next full expression exceeds 100 |
| inequality_orientation_gate | pass | single ≤ occurrence; no reverse symbol |
| no_unintended_breakage at target scope | pass | sole use is same module L306; actual module build and full LSP pass |
| cumulative compatibility/full project/LeanEval | parent-owned | parent performs these sequentially after freeze; not asserted by worker |

`git diff --check` passes. Actual source arithmetic: 599 → 597 lines, 4 removed / 2 added;
target declaration excluding documentation 6 → 4 lines; proof body 4 → 2 physical lines.
27 retained declarations unchanged. No imports, attributes, documentation, definitions,
theorem statements, instance assumptions, or other source declarations changed.

Result: support API replaces coefficient/multidegree rewriting, saving two lines.
Audit issues fixed: proof simplification and mathematical lambda style. Refactoring
deferred: the existing public instance omission proposal only. Renames queued: none.

Phase checklist:
- [✓] Step 1 — references read.
- [✓] Step 2 — all 24 audit items recorded before edits.
- [✓] Step 2.5 — all five actual searches and auxiliary variants recorded.
- [✓] Step 2.6 — every effective binder probed; literature and pending proposal recorded.
- [✓] Step 2.7 — all signature lines measured.
- [✓] Step 2.8 — all inequality occurrences scanned.
- [✓] Step 3 — all 42 golf rules given concrete statuses.
- [✓] Step 4 — mathematical step-back review performed.
- [✓] Step 5a — complete native diagnostics, 0 errors; 32 warnings documented above.
- [✓] Step 5b — diff gates, actual module build, independent proof, axioms and actual profile complete.
- [✓] Step 6a — rename queue action none; no shared sidecar edits needed.

## Freeze

Source SHA256: `72f715a6efc3664bfad5d760b598939f131a32393988c886da69206e67e1dc12`.
All native Lean/MCP, compiler, build and profiler requests have completed and are drained.
**All source ownership is revoked, including the target theorem and every other source
path. I am report-only and will make no source edits after this freeze.** Parent owns
the remaining cumulative verification, Git and push actions.

## Owner cumulative publication gates

Source FROZEN SHA256 `72f715a6efc3664bfad5d760b598939f131a32393988c886da69206e67e1dc12`; leaf ownership revoked and requests drained before owner gates. Owner probe `68300` exit0,54.14s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d09-compatibility.{lean,log,json}`. Owner build session `50653` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,158.46s/38.75s; source hash stable. `/private/tmp/roth-separation-d09-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
