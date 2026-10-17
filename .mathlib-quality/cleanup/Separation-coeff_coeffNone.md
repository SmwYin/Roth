# `Roth.coeff_coeffNone` — fresh original declaration d07

Scope: only the proof of this public theorem in `Roth/Separation.lean`. Original contract and
docstring preserved. Parent owns Git, cumulative compatibility, full-project/LeanEval gates,
publication and pending instance proposal. No helpers will be introduced.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md, plus lean4/mathlib-quality skills,
cleanup Phase 4, style, naming and profiling references.

## Initial audit (written before any source edit)

Baseline supplied by parent: module/full/separate LeanEval pass; complete LSP 0 errors,
31 warnings. Fresh unfiltered LSP confirms complete success, 31 warnings (raw
`/private/tmp/roth-separation-d07-initial-4.json`). Target has three retained warnings:
unused section variables Fintype/DecidableEq; unused DecidableEq in type; unused Fintype
in type. Header metadata is explicitly preserved. Target starts L77, signature L77–78,
proof tactics L79–84 (6 lines). Baseline actual-module cost: command 7.068 ms + outer
async proof 98.367 ms = 105.435 ms in `/private/tmp/roth-separation-d05-final-profile.log{,.json}`.

| # | Audit | Concrete finding / action |
|---|---|---|
| 1 | Lint | Three target warnings above; instance removal remains pending approval. |
| 2 | Have scan | No `have` occurs. |
| 3 | set_option | None. |
| 4 | Simp squeeze | Nested terminal `simp [Finsupp.mapDomain_of_notMem_range]`; preserve unsqueezed if retained. |
| 5 | Naming | `coeff_coeffNone` names coefficient API of `coeffNone`, follows mathlib mixed definition-name convention; no banned abbreviations/patterns. |
| 6 | Packing | Two measured signature lines; table below. |
| 7 | By placement | `by` ends signature L78. |
| 8 | Format | Two-space proof indentation; no blank lines, semicolons or instance lets. |
| 9 | Comments | No inline comments; existing docstring preserved verbatim. |
| 10 | Docstring | Public one-sentence statement already present. |
| 11 | Visibility | Public coefficient API used by subsequent expansion/degree theorems; retained. |
| 12 | Structure | Six tactic lines; no conjunction or branches >10 lines. No helper needed. |
| 13 | Mathlib | Actual five-method searches all find optionEquivLeft coefficient API; investigate direct use of optionEquivLeft_coeff_coeff. |
| 14 | Junk def | n/a: theorem. |
| 15 | Exists lemma | n/a: public equality. |
| 16 | Show/change | Term-mode `show` proves index evaluation, not a tactic goal change; candidate replacement eliminates it. |
| 17 | push_neg | None. |
| 18 | Generalise | Probe all effective binders separately; preserve original signature and pending public instance menu. |
| 19 | Inequality | No inequality occurrences; table below. |
| 20 | Normal form | RHS explicit multi-index matches public API; mathlib canonical optionElim equivalent; keep signature. |
| 21 | Syntax generality | Existing explicit coefficient equation supports rewriting directly; no restatement. |
| 22 | Import fanout | n/a: no new imports. |
| 23 | Casts | One load-bearing Finsupp type ascription inside term-mode show; candidate may eliminate entire subproof. No cross-type coercions. |
| 24 | Instance name | n/a: theorem, no instance declaration. |

Initial issues/action: replace manual some/none restriction rewrites with existing
`optionEquivLeft_coeff_coeff` plus direct conversion of its multi-index, if compiler-tested.
Refactoring proposal: public `[Fintype τ]`/`[DecidableEq τ]` omission is already pending in
`Separation-instance-proposal.md`; it will not be applied here. Deleting the public wrapper
would change the public contract and is outside authorization; keep this coefficient API.

## Search status

All five methods actually ran, raw results `/private/tmp/roth-separation-d07-initial-{0,1,2,3}.json`.

| Method | Query | Result |
|---|---|---|
| A Lean-Finder | coefficient optionEquivLeft polynomial optionElim | optionEquivLeft_coeff_coeff and _coeff_some_coeff_none found. |
| B Loogle | MvPolynomial.optionEquivLeft, Polynomial.coeff | Both coefficient theorems, support and degree variants found. |
| C LeanSearch | coefficient of polynomial in option variables optionEquivLeft | Both coefficient theorems and support variant found. |
| D Source rg | optionEquivLeft_coeff, some_add, some_single_none, optionElim, mapDomain | Equiv.lean L509,610 and Finsupp/Option.lean APIs inspected. |
| E Name pattern | optionEquivLeft_coeff via lean_local_search | Both source declarations found; index warming, not evidence of absence. |

Auxiliary variants: _coeff_some_coeff_none, _coeff_coeff, some_optionElim,
optionElim_some, optionElim_apply_none/some, embDomain_eq_mapDomain.
Common-equivalents table: no topology/custom-predicate bucket applies.
Conclusion: existing theorem supplies the mathematical content; retain the authorized
public API and build directly on mathlib, no new wrappers/helpers.

## Literature search

Actual WebSearch query: “polynomial ring R X Y isomorphism R X Y iterated polynomial ring
coefficients commutative semiring generalization”. Top three returned hits: UCSD notes
(two host aliases), then Androma. Only primary mathematical teaching sources relied on:
[McKernan, Polynomial rings](https://www.math.ucsd.edu/~jmckerna/Teaching/15-16/Spring/103B/l_15.pdf)
states the natural iterated polynomial-ring identification over a commutative ring;
[Chavan, Polynomial rings in several variables](https://home.iitk.ac.in/~chavan/alg3.pdf)
also describes the coefficient-ring identification. The local mathlib theorem already
works over CommSemiring and arbitrary index types; no field/domain hypothesis is needed.
No math ChatGPT MCP is available (tool inventory checked). Literature supports the
pending index-instance omission, with no further public restatement proposed.

## Initial packing and inequality tables

| Signature line | Codepoints | Next syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 77 | 78 | `(coeffNone P ν).coeff d` (23) | 78 + 1 + 23 = 102 > 100 | ok |
| 78 | 86 | none: proof body next | n/a | ok |

The next syntactic unit is the conclusion expression, not a whitespace-delimited fragment.
Final measured table and width-100 #check will be recorded below.

| Occurrence | Location | Original | Rewrite |
|---|---|---|---|
| none | Entire signature, all inherited binders | no `≥`/`>` | n/a |

## Golfing rules: all 42

| Rule | Concrete status |
|---|---|
| 1.1 by exact | n/a: no exact wrapper. |
| 1.2 by rfl | n/a: no standalone `by rfl`. |
| 1.3 rw + exact | n/a: no closing exact term after rewrite. |
| 1.4 simp + exact | n/a: no exact term after simp. |
| 1.5 trailing rfl | Removed old `rfl` by replacing the entire strategy; not directly after simp. |
| 1.6 constructor | n/a: no conjunction or structure construction. |
| 1.7 apply + exact | n/a: no apply. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: no lambdas. |
| 1.10 single-use have | n/a: none occurs. |
| 1.11 apply + intro | n/a: neither occurs. |
| 1.12 redundant show | Removed term-mode index `show` with strategy replacement; it was not redundant in the old proof. |
| 1.13 have projections | n/a: no have or projections. |
| 1.14 merge rw | n/a: one rewrite call after replacement. |
| 1.15 terminal simp only | n/a: final terminal simp is already unsqueezed. |
| 1.16 nonterminal simp | n/a: both `cases` branches close with simp. |
| 1.17 dot notation | n/a: mathlib coefficient theorem is a rewrite lemma; no dot-term application. |
| 1.18 `<|` | n/a: no parenthesized final term argument. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential helper | n/a: no existential/helper. |
| 2.1 grind | Actual live attempt failed at original equality with coeffNone unfolded. |
| 2.2 pre-grind steps | n/a: no grind retained. |
| 2.3 simpa | Actual isolated attempt unfolding optionElim/optionEquiv failed: update index not normalized to single + mapDomain. Retained direct extensionality. |
| 2.4 fun_prop | n/a: coefficient equality, no function property. |
| 2.5 positivity | n/a: no positivity or nonzero goal. |
| 2.6 gcongr | n/a: no inequality or monotonicity. |
| 2.7 lia/omega | n/a: no numeric constraint, arbitrary coefficient equality. |
| 2.8 aesop | Actual live attempt failed, no progress at coefficient equality. |
| 2.9 norm_num/norm_cast | n/a: no numerical computation or cross-type cast. |
| 2.10 decide | n/a: arbitrary semiring coefficients, no finite decidable computation. |
| 2.11 field_simp/ring | n/a: no division/rational expression. |
| 2.12 linear_combination | n/a: no ring closure or ring hypotheses. |
| 2.13 wlog | n/a: none/some cases have different constructors, no symmetric branches. |
| 2.14 calc | n/a: no calc chain. |
| 2.15 `<;>` | Applied to none/some branches: both close by the same terminal simp call. |
| 3.1 erw | n/a: no erw. |
| 3.2 legacy properties | n/a: no continuity/measurability. |
| 3.3 omega to lia | n/a: no omega. |
| 3.4 rcases rfl | n/a: no rcases. |
| 3.5 automation attributes | Retain existing attribute state; global simp registration would alter public simplification behavior without need. |
| 3.6 simp_all | n/a: no simp_all only and no hypotheses to simplify. |
| 3.7 heartbeat option | n/a: none exists, none introduced. |

Step-back review: the mathematics is exactly mathlib's iterated coefficient theorem;
only the representation of the exponent differs. Direct `rw`, `congr 1`, extensionality
and none/some simp make this explicit. Actual live `exact?` failed; `apply?` suggested
unhelpful Finsupp graph-membership goals. `grind`, `simp`, `aesop` did not close the entire
proof. Live goal inspection confirms rewriting reduces to equality of coefficients at
`d.optionElim ν` and `d.mapDomain some + single none ν`. An isolated shorter attempt
using `eq_mapDomain_some_add_single` without an explicit index failed because its
rewrite LHS is a metavariable; no speculative rewrite was applied. The final proof does
not depend on that local public theorem or any removed private wrapper. No missing API
is invented. Native multi-attempt replaces a single tactic line, so old continuation
syntax errors in the first attempt batch are not evidence that a whole replacement
fails; the accepted replacement was separately compiler-checked as an isolated example
and as the actual repository module.

Final proof uses five tactic/continuation lines, before six; declaration seven physical
lines, before eight, excluding its docstring and following blank line. Actual file
`wc -l`: 602 → 601. Diff contains exactly six removed and five added proof lines,
with no other source declaration touched. Actual diff saved as
`/private/tmp/roth-separation-d07.diff`; `git diff --check -- Roth/Separation.lean` exits 0.
No renames, helpers, definitions, imports, attributes, comments or docstrings changed.
Cast audit: one explicit Finsupp ascription dropped with its subproof, zero cross-type
coercions introduced, zero load-bearing ascriptions remain in this diff.

## Exact original recovery and built axiom evidence

`/private/tmp/roth-separation-d07-independent.lean` reconstructs the exact original
`coeffNone` definition and theorem statement from the immutable original snapshot in
`OriginalD07`. Its independent proof invokes only mathlib APIs and does not use the
target theorem. Separately, an example recovers the exact original quantified type with
`@Roth.coeff_coeffNone`; a second equality check verifies the types agree definitionally.
Compiler exits 0; complete log `/private/tmp/roth-separation-d07-independent.log`.
Actual built `Roth.coeff_coeffNone` and `OriginalD07.independent` both report exactly
`[propext, Classical.choice, Quot.sound]`. No changed private constants exist.

Width-100 `#check @Roth.coeff_coeffNone` from that real compiler run:

```lean
@Roth.coeff_coeffNone : ∀ {τ : Type u_3} [Fintype τ] [DecidableEq τ] {R : Type u_4} [inst : CommSemiring R]
  (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ),
  (Roth.coeffNone P ν).coeff d = P.coeff (Finsupp.mapDomain some d + Finsupp.single none ν)
```

Final signature is byte-for-byte unchanged; the final packing table is the same measured
two rows (78/86 codepoints) and the inequality table has zero occurrences as above.
## Generalisation probes

Every effective binder is included below. Actual standalone compiler probes use
`set_option autoImplicit false`; `/private/tmp/roth-separation-d07-probes.json` contains
the full raw results and scratch source paths. Early drop-0–drop-3 imports raced the
module rebuild and returned missing-olean errors; those are environmental failures,
not negative binder evidence, and were retried after the successful module build.

| Binder | Kind / role | Candidate | Compiler result / action |
|---|---|---|---|
| `{τ : Type*}` | index type | drop; independent universe `Type u` | Drop needs τ in Fintype and polynomial; explicit u compiled in independent proof/probes. Keep arbitrary universe. |
| `[Fintype τ]` | inherited index instance | drop individually and jointly | Joint omission compiles; individual retry recorded below. Original instance retained pending approval. |
| `[DecidableEq τ]` | inherited index instance | drop individually and jointly | Joint omission compiles; individual retry recorded below. Original instance retained pending approval. |
| `{R : Type*}` | coefficient type | drop; independent universe `Type v` | Drop needs R in CommSemiring and polynomial; independent v compiled. Keep arbitrary universe. |
| `[CommSemiring R]` | coefficient algebra | drop; weaken to Semiring | Both fail to synthesize CommSemiring R for the original statement/coeffNone API. Keep. |
| `(P : MvPolynomial (Option τ) R)` | polynomial | drop | Unknown P/P.coeff under autoImplicit false; statement refers to it on both sides. Keep. |
| `(ν : ℕ)` | distinguished exponent | drop | Unknown ν; fixes coeffNone index and single exponent. Keep. |
| `(d : τ →₀ ℕ)` | remaining exponent | drop | Unknown d/d.mapDomain; fixes both coefficient indices. Keep. |

No propositional hypotheses, strict inequalities, bundled logical assumptions, or
pointwise/global analytic assumptions exist; corresponding catalogue weakenings are
inapplicable. Universes already independent. Inversion check: named `coeffNone` unfolds
once; the abstract content is precisely existing `optionEquivLeft_coeff_coeff`, now used
directly. No new general theorem is needed. Big change remains only the already-compiled
pending public index-instance omission; no public binder changes applied.

## Profile and gates

Actual command (exit 0):

```text
/Users/ramin/.elan/bin/lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Separation.lean
```

Raw complete log `/private/tmp/roth-separation-d07-final-profile.log`, parsed anchored
table `/private/tmp/roth-separation-d07-final-profile.log.json`. Target has exactly one
outer-command anchor (9.753 ms) and one outer-async-proof anchor (105.724 ms), total
**115.477 ms**, below 750 ms resweep threshold and 1000 ms budget. Nested nodes are
not added again. Supplied unchanged-target baseline was 105.435 ms; this sweep is
10.042 ms higher (about 9.5%), within usual wall-clock noise. No performance improvement
is claimed; the change improves API use and removes manual rewrite machinery.

Original immutable snapshot used a 3-line proof invoking private wrappers removed by
earlier workers. This worker starts after those removals: its actual before/after is
6 → 5 proof lines, not 3 → 5 claimed as a shortening. No helper was reintroduced.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual `lake build Roth.Separation` exit 0; `/private/tmp/roth-separation-d07-module.log`, 1876 jobs. |
| complete LSP | pass | `/private/tmp/roth-separation-d07-final-lsp.json`: partial=false, timed_out=false, success=true; 0 errors, 31 warnings, no failed dependencies. |
| definition_protected | pass | Only target proof lines in worker diff; no definitions touched. |
| theorem_statement_protected | pass | Exact original signature and docs preserved; independent original recovery exit 0. |
| structure_gate | pass | Five proof lines, no conjunction, two one-line cases. |
| naming_gate | pass | Mathematical coefficient API name; no banned pattern. |
| line_packing_gate | pass | Every signature line measured 78/86, next LHS yields 102 >100; final signature unchanged. |
| inequality_orientation_gate | pass | Required occurrence table shows none. |
| standard axioms | pass | Actual built target and independent proof both only propext/Classical.choice/Quot.sound. |
| no scaffolding / diff check | pass | No added sorry, axiom, native_decide, limits, instance lets, debug options; diff check exit 0. |
| cumulative compatibility/full/LeanEval/publication | parent-owned | Parent runs these sequential gates after freeze; worker does not duplicate whole-original check. |

All eleven completion steps:

- [x] Step 1: required references read.
- [x] Step 2: full 24-item initial audit written before source edit.
- [x] Step 2.5: all five actual mathlib searches recorded.
- [x] Step 2.6: every effective binder/generalisation and public literature search recorded.
- [x] Step 2.7: complete signature codepoint table, final same table.
- [x] Step 2.8: inequality occurrence table.
- [x] Step 3: all 42 rules have concrete statuses.
- [x] Step 4: step-back review, actual exact?/apply?/automation attempts.
- [x] Step 5a: complete unfiltered successful LSP.
- [x] Step 5b: actual module/compatibility/axiom/profile and diff gates recorded.
- [x] Step 6a: no rename needed, no shared rename queue touched.

Final binder retry results (all requests drained): drop-0 fails with unknown τ;
drop-1 (Fintype alone) exits 0; drop-2 (DecidableEq alone) exits 0; drop-3 fails with
unknown R. Raw `/private/tmp/roth-separation-d07-probes.json` preserves both the earlier
environment failures and these valid retries. Remaining probes: drop CommSemiring,
P, ν, d and Semiring weakening all fail for the explicit reasons in the table;
joint index-instance omission exits 0. All three positive probe configurations
(individual Fintype, individual DecidableEq, joint) remain unapplied, involving two
removable binders.

Final result: one proof cleanup applied; one line saved against worker-start state,
one obsolete ascription removed, zero API/doc changes, zero helpers/renames.
Pending public proposal: omit Fintype/DecidableEq on this theorem in the existing
12-theorem menu, only after parent receives exact approval. No other proposed change.

Freeze: all native Lean/MCP calls and shell module/probe/independent/profile sessions
have completed and been drained. Source SHA256:
`a3a41139893974634024440f0897d72359502621f287671625d000e2bb3fc25b`.
I explicitly revoke **ALL source ownership**, including `Roth/Separation.lean` and
every other source file. I am now **report-only** and will make no source edits.

## Owner cumulative publication gates

Source FROZEN SHA256 `a3a41139893974634024440f0897d72359502621f287671625d000e2bb3fc25b`; leaf ownership revoked and requests drained before owner gates. Owner probe `48331` exit0,44.71s: independent ORIGINAL30 proof bodies,all20 original public type/value recoveries and ALL27 actual retained standardaxiom checks. `/private/tmp/roth-separation-d07-compatibility.{lean,log,json}`. Owner build session `87726` sequential `lake build` then separate `lake build Roth.LeanEval` both exit0,139.54s/33.53s; source hash stable. `/private/tmp/roth-separation-d07-{full,leaneval}.log`, `...-builds.json`. Owner original block docs byte-identical; exact diff/whitespace checked. Exact-path commit and successful cleanup-branch push precede next declaration.
