# Approved instance revisit: `Roth.coeff_coeffNone` (r02)

Fresh dedicated audit, starting after c9d850b. Exact approval: remove both index instances
on this theorem only. No new helpers, no other source ownership, no Git mutations.
I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md; Lean/mathlib skills, cleanup Phase 4,
style/naming/profiling references were consulted. Original d07 report supplies historical
context only; the evidence below is fresh. Owner retains cumulative/full/LeanEval gates.

## Initial audit — recorded before source edit

Fresh native unfiltered LSP: complete success, 0 errors, 28 warnings, three target warnings
(unused section pair, unused Fintype, unused DecidableEq).
Raw `/private/tmp/roth-separation-r02-initial-lsp.json`.
Actual supplied baseline `/private/tmp/roth-separation-r01-profile.log{,.json}`:
command 7.821 ms + outer proof 94.700 ms = 102.521 ms, one anchor each.
Source 574 lines; target L78–84, two signature and five proof lines.

| # | Audit | Finding/action |
|---|---|---|
| 1 | Lint | Remove exactly the approved two unused index instances. |
| 2 | Have | None to inline or rename. |
| 3 | Options | None in target. |
| 4 | Simp | Both cases close with terminal unsqueezed simp. |
| 5 | Naming | coeff_coeffNone describes coefficients of the named coeffNone API; no forbidden pattern/abbreviation. |
| 6 | Packing | Signature widths 78 and 86; full table below. |
| 7 | by | Ends the conclusion line. |
| 8 | Format | Two-space proof indent, no blank lines/instance lets/semicolons. |
| 9 | Comments | No inline narrative; docstring retained verbatim. |
| 10 | Docs | Public one-sentence coefficient interpretation exists. |
| 11 | Visibility | Retain approved public coefficient API. |
| 12 | Structure | Five proof lines, two short cases, no conjunction; no helper. |
| 13 | Mathlib | Fresh five searches find iterated coefficient theorem; retain wrapper by scope. |
| 14 | Junk def | n/a theorem. |
| 15 | Existential | n/a equality theorem. |
| 16 | show | None. |
| 17 | push_neg | None. |
| 18 | Generality | Probe every effective binder; apply only approved pair omission. |
| 19 | Inequality | No order symbols in signature or inherited binders. |
| 20 | Normal form | RHS additive exponent matches local public API; mathlib uses optionElim. |
| 21 | Syntax | Direct coefficient equation supports rw; no restatement needed. |
| 22 | Import | None added, no fanout. |
| 23 | Casts | No changed ascriptions/coercions. |
| 24 | Instance naming | n/a theorem, no instance declaration. |

Action: scoped `omit [Fintype τ] [DecidableEq τ] in` before original docstring;
only minimal proof adjustment if needed. No broader refactoring is authorized here.

| Signature line | Codepoints | Next unit | Arithmetic/action |
|---|---:|---|---|
| theorem line | 78 | `(coeffNone P ν).coeff d` (23) | 78+1+23=102>100, retain |
| conclusion | 86 | proof | n/a last signature line |

| Inequality occurrence | Location | Action |
|---|---|---|
| none | Signature plus all inherited binders | No orientation change |

## Fresh searches and literature

Native complete schemas discovered through ALL_TOOLS before use. Raw remote responses:
`/private/tmp/roth-separation-r02-search.json`.

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | coefficient optionEquivLeft polynomial optionElim | optionEquivLeft_coeff_coeff and _some_coeff_none |
| B Loogle | MvPolynomial.optionEquivLeft, Polynomial.coeff | support/total-degree coefficient APIs |
| C LeanSearch | coefficient of polynomial in option variables optionEquivLeft | both coefficient theorems and support API |
| D source rg | optionEquivLeft_coeff_coeff, optionEquivLeft_coeff_some_coeff_none | Equiv.lean L509,610; signatures inspected |
| E native local name | coeff_coeff | target plus MvPowerSeries variants; index unavailable, not absence |

Auxiliary variants: _coeff_some_coeff_none, _coeff_coeff, optionElim, mapDomain.
Common-equivalents table has no applicable topology/finiteness bucket. Existing mathlib
theorem already supplies the abstract content; preserve public wrapper per explicit scope.
Inversion check: coeffNone disappears at first unfolding, revealing that same existing
mathlib theorem; no new abstract helper needed.

Actual fresh web search and primary source read:
[McKernan, Polynomial rings, Lemma 15.7](https://www.math.ucsd.edu/~jmckerna/Teaching/15-16/Spring/103B/l_15.pdf)
identifies R[x,y] with R[x][y]. The coefficient identity is the corresponding coefficient
comparison; local mathlib states it over CommSemiring and arbitrary variable types.
This supports the approved index-instance omission. No mathematical second-opinion
connector is exposed. Other wrapper deletions and two-theorem coefficient widening were
considered and declined by user; no pending decision is created by this report.

Additional fresh literature query: “polynomial ring iterated polynomial coefficient ring
generalization commutative semiring”; first three returned entries were Alphabeta
“Polynomial Rings, the Division Algorithm and Roots”, Wikipedia “Polynomial ring”, and
Alphabeta “A polynomial ring on a finite ordered family agrees canonically with the
iterated polynomial-ring construction”. These are discovery context only; the primary
UCSD notes above and local mathlib signatures substantiate the conclusion. Full raw
response `/private/tmp/roth-separation-r02-literature.json`.

## All 42 golfing rules

| Rule | Fresh concrete status |
|---|---|
| 1.1 by exact | No exact wrapper. |
| 1.2 by rfl | No rfl body. |
| 1.3 rw+exact | No closing exact after rw. |
| 1.4 simp+exact | No closing exact after simp. |
| 1.5 trailing rfl | No rfl tactic. |
| 1.6 constructor | No structure/conjunction construction. |
| 1.7 apply+exact | No apply chain. |
| 1.8 contradiction | No by_contra. |
| 1.9 eta | No lambdas. |
| 1.10 inline have | No have. |
| 1.11 apply+intro | Neither occurs. |
| 1.12 redundant show | No show. |
| 1.13 projections | No local have/projection pair. |
| 1.14 merge rw | One rw call already. |
| 1.15 terminal simp | Already unsqueezed. |
| 1.16 nonterminal simp | Both cases close with simp. |
| 1.17 dot notation | Rewrite theorem used in rw; no term call to convert. |
| 1.18 trailing parens | Parentheses fix Option.some_injective argument; no final lambda/proof argument. |
| 1.19 push Not | No negation pushing. |
| 1.20 exists helper | No existential helper. |
| 2.1 grind | Fresh native grind [coeffNone] fails. |
| 2.2 pre-grind | No grind retained, nothing to delete. |
| 2.3 simpa | Whole simp [coeffNone] leaves coefficient equality; no simp+closing chain. |
| 2.4 fun_prop | No function-property predicate. |
| 2.5 positivity | No nonnegativity/nonzero goal. |
| 2.6 gcongr | No order/monotonicity goal. |
| 2.7 lia | Exponents are Nat, but target is arbitrary coefficient identity, no arithmetic constraints. |
| 2.8 aesop | Fresh native attempt fails without progress. |
| 2.9 norm_num/cast | No numerical computation or cross-type cast. |
| 2.10 decide | Arbitrary coefficients, no finite computable decision problem. |
| 2.11 field_simp/ring | No denominators or ring identity. |
| 2.12 linear_combination | No ring terminal tactic or algebraic hypotheses. |
| 2.13 wlog | none/some are asymmetric constructors, not symmetric cases. |
| 2.14 calc | No calc chain. |
| 2.15 multiple goals | Existing cases <;> simp shares closing tactic. |
| 3.1 erw | No erw. |
| 3.2 legacy properties | No continuity/measurability. |
| 3.3 omega | No omega. |
| 3.4 rcases rfl | No rcases. |
| 3.5 attributes | No new automation attribute justified; would alter simplification behavior. |
| 3.6 simp_all | No hypotheses needing simp_all; no simp_all only. |
| 3.7 limits | No limit options; none introduced. |

Step-back: direct existing coefficient theorem followed by equality of exponent
representations is clear and short. Fresh native exact? fails; apply? yields graph-membership
side goals rather than a coefficient identity. Raw `/private/tmp/roth-separation-r02-attempt.json`.
These live attempts replace one tactic line: continuation diagnostics are not treated as
whole-replacement failures. In particular simp leaves the whole equation unresolved and
apply? continuation errors do not establish theorem absence. No new API is claimed missing.
The approved edit needs no proof change. Holistic simplify review finds no independent
statement/definition cleanup within scope; no helper or rename is introduced.

## Every effective binder and exact type checks

Fresh actual standalone probes have autoImplicit=false, full source and diagnostics in
`/private/tmp/roth-separation-r02-probes.json` and the named scratch Lean files therein.
All ten compiler requests completed; no negative result is inferred merely from lint.

| Effective binder | Role | Actual probe / outcome | Action |
|---|---|---|---|
| τ : Type u | exponent variable type | drop-0 fails unknown τ; arbitrary u succeeds in independent proof | Keep universe polymorphism |
| Fintype τ | inherited finite enumeration | drop-1 exits 0; joint exits 0 | Approved omission applied |
| DecidableEq τ | inherited equality decision | drop-2 exits 0; joint exits 0 | Approved omission applied |
| R : Type v | coefficient type | drop-3 fails unknown R; independent v succeeds | Keep independent universe |
| CommSemiring R | polynomial/equivalence structure | drop-4 and Semiring weakening fail required CommSemiring synthesis | Keep coefficient assumption |
| P | input polynomial | drop-5 fails unknown P | Keep |
| ν : ℕ | distinguished exponent | drop-6 fails unknown ν | Keep natural exponent codomain |
| d : τ →₀ ℕ | remaining exponents | drop-7 fails unknown d | Keep natural exponent codomain |

No proposition/strict inequality/bundled logical assumption/global analytic assumption
exists. Neither arbitrary exponent monoids nor changing polynomial definitions preserves
the fixed coefficient contract; those are outside the approved task.

`/private/tmp/roth-separation-r02-independent.lean` imports the actual built module,
reconstructs the original coeffNone definition, independently proves the same equation
without using the target (over arbitrary τ), checks proof/type definitional equality,
ascribes the exact NEW arbitrary-τ type, and explicitly adapts the ORIGINAL
Fintype/DecidableEq argument order with a lambda. Compiler exit 0, full log
`/private/tmp/roth-separation-r02-independent.log`. Actual built target and two direct
callers `eq_sum_X_none_pow_mul_coeffNone`, `coeff_rename_mul_aeval`, plus independent proof
each report exactly `[propext, Classical.choice, Quot.sound]`. No affected private caller.

Fresh width-100 reference (format.width, not pp.width):

```lean
@Roth.coeff_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ)
  (d : τ →₀ ℕ), (Roth.coeffNone P ν).coeff d = P.coeff (Finsupp.mapDomain some d + Finsupp.single none ν)
```

Final measured source signature widths: L79 78, L80 86; same arithmetic as initial table
(78+1+23=102>100; final line no next unit). Scoped omit L77 is 35 codepoints; original
docstring L78 is 99. Final inequality table still has zero occurrences. Five proof lines
and seven declaration lines remain; adding scoped omit makes eight lines including omit,
excluding docstring/blank line. Actual file wc 574→575; diff +1/-0, no proof-line saving.

## Validation and completion

Actual `lake build Roth.Separation` exits 0, 1876 jobs;
`/private/tmp/roth-separation-r02-module.log`.
Complete native unfiltered LSP `/private/tmp/roth-separation-r02-final-lsp.json`:
partial=false, timed_out=false, success=true, failed_dependencies=[], 0 errors, 27 warnings.
All three target warnings are gone. Two newly exposed unusedSectionVars warnings belong
to `eq_sum_X_none_pow_mul_coeffNone` and `coeff_rename_mul_aeval`; unchanged public
contracts retained for their own approved audits. Header warning is user-preserved.

| Gate | Result / concrete evidence |
|---|---|
| lake_build_file | Pass, actual module command/log above |
| complete LSP | Pass, 0 errors, complete 27 warnings; target 0 warnings |
| definition_protected | Pass, no definition line touched |
| theorem_statement_protected | Approved exact pair omitted; all other binders/conclusion/docs unchanged; NEW/ORIGINAL checks pass |
| structure | Pass, 5 tactic/continuation lines; no conjunction, branches ≤1 line plus continuation |
| naming | Pass, descriptive coefficient name, no banned patterns |
| packing | Pass, every signature line remeasured above |
| inequality | Pass, zero reversed inequalities in complete effective signature |
| casts | 0 dropped / 0 cross-type kept / 0 load-bearing added in diff |
| axiom gate | Pass, built target and direct callers all standard three |
| whitespace/scaffolding | git diff --check exits 0; one omission line only, no helper/import/options/attributes |
| full/project/LeanEval/cumulative/publication | Parent-owned sequential gates after freeze |

All eleven completion steps: (1) required references read; (2) 24-item initial audit before
edit; (2.5) five actual searches; (2.6) every effective binder plus public literature;
(2.7) measured width tables; (2.8) inequality table; (3) all 42 golf rules;
(4) step-back and fresh automation attempts; (5a) complete unfiltered native LSP;
(5b) actual module/type/independent/axiom/diff gates (profile below);
(6a) no rename needed, no shared queue modification. No new helper needing another audit.

## Actual repository profile and freeze

After module/probe/independent/native requests all drained and owner confirmed compiler
jobs idle, actual isolated command exited 0:

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Full raw `/private/tmp/roth-separation-r02-profile.log`; anchored parser table
`/private/tmp/roth-separation-r02-profile.log.json`. Target has two command appearances:
inner documented theorem 6.833 ms (L54442) and enclosing scoped omission 7.736 ms
(L55949). Charge outer 7.736 only, plus sole outer async proof 79.367 ms (L55975):
**87.103 ms**. No double counting inner command or nested proof children. Below both
750 ms resweep threshold and 1000 ms budget. Supplied actual baseline 102.521 ms;
15.418 ms lower in this sweep, ordinary wall-clock variation, no projectwide performance
claim. No performance edits or profiler scaffolding in source.

Final result: only approved Fintype/DecidableEq pair removal applied; unchanged proof,
documentation, all other public contracts/definitions/coefficient assumptions retained.
No pending proposal or required user input from this declaration.

All module, native Lean MCP, search, automation, independent proof, ten binder-probe,
and profile requests have completed and been drained. Source SHA256:
`e3da33d7e951239837ba563ea0e8d6bb8fa783ef9bf6c0781bdce51588dce029`.
I explicitly revoke **ALL source ownership**, including Roth/Separation.lean and every
other source file. I am **report-only**; no source edits after this freeze. Parent owns
whole-original/public/all-actual checks, sequential full and separate LeanEval builds,
exact-path commit and successful push before next source edit.

## Owner cumulative publication gates

Source FROZEN SHA256 `e3da33d7e951239837ba563ea0e8d6bb8fa783ef9bf6c0781bdce51588dce029`; leaf ownership revoked and requests drained before owner gates. Owner probe `25584` exit0,42.40s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL25 actual retained standardaxiom checks. `/private/tmp/roth-separation-r02-compatibility.{lean,log,json}`. Owner build session `72584` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,117.83s/27.79s; source hash stable. `/private/tmp/roth-separation-r02-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
