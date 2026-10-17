# `Roth.index_prod` cleanup

Single-declaration worker; starting checkpoint `7debd94`, original reference `e557886`.
Applied the explicitly approved σ-decidability omission before the unchanged docstring,
and changed two mathematical lambda arrows to `↦`. The statement text, data arguments,
`hf`, `hr`, definition of index, and all comments are preserved. This **does change the
public type**: `[DecidableEq σ]` is absent. No other API change, helper, import, or rename.
The theorem remains 13 lines (10 proof lines); file 262 → 263 lines, including the directive.

Source authority released and revoked at SHA256
`568dc824159ae7476977806bf4eff276e9d175d5317c5381aee0c57a72d2e232`.
All worker Lean/compiler requests finished before release; subsequent work was report-only.
Full project, separate LeanEval, callers, file-final simplify and profile sweeps belong to
the owner. This report claims the scoped checks below, not a full-project pass.

## Audit: all 24 items

| # | Item | Finding/action |
|---|---|---|
| 1 | LINT | Two original target warnings concerned σ-decidability; approved omission removes both. Complete final native response has zero target warnings/errors; other warnings documented below. |
| 2 | HAVE SCAN | No `have` in the production proof; no single-use binding to inline. |
| 3 | SET_OPTION | None in target; no limit raises or suppression added. |
| 4 | SIMP SQUEEZE | Only `(by simp)` closes evaluation of 1 in the empty branch. Terminal, left unsqueezed. |
| 5 | NAMING | `index_prod` describes index of a finite product, matches `index_mul` and `weightedOrder_prod`; snake_case, no forbidden abbreviation or numeric/scheme pattern. No rename needed. |
| 6 | LINE PACKING | All three signature lines measured below; each break exceeds 100 when the next complete binder/conclusion is appended. |
| 7 | BY PLACEMENT | `:= by` ends the conclusion line. |
| 8 | FORMAT | Correct indentation and branch arrows, no internal blank lines, no tactic chains; normalized two lambda arrows. No `haveI`/`letI`. |
| 9 | COMMENTS | No target inline comments. All file block comments, including the target docstring, compare byte-for-byte equal to the worker snapshot. |
| 10 | DOCSTRING | Existing three-line statement/source citation retained verbatim; identifies the finite-product version of the adjacent binary result. |
| 11 | VISIBILITY | Public result used by `Roth/Theta.lean:399`, also named in module main results; retain public. |
| 12 | STRUCTURE | Ten proof lines; empty branch two tactics, insert branch one rewrite chain; neither branch exceeds 10 lines, no conclusion conjunction. Below headline limit 15. No helper/decomposition needed. |
| 13 | MATHLIB | Five actual methods below. Verified partial match `MvPowerSeries.weightedOrder_prod`; its codomain is ENat, while local index is a scaled real infimum with a distinct zero convention. Retain domain API; no new wrapper helper. |
| 14 | JUNK DEF | n/a: theorem, not a data definition. |
| 15 | EXISTS LEMMA | n/a: public equality, no existential wrapper. |
| 16 | SHOW vs CHANGE | No `show`/`change` in production proof. |
| 17 | PUSH_NEG | None. |
| 18 | GENERALISE | Every binder tested/classified below; only approved omission applied. Failed proof modifications do not establish mathematical necessity. |
| 19 | INEQUALITY | Table below; positivity already smaller-left; no reverse inequality in Lean signature or name. |
| 20 | NORMAL-FORM | Index of product on left, sum of indices on right: finite-product additivity normal form, matching binary theorem. No competing equivalence API. |
| 21 | SYNTAX-GEN | Finset plus membership-local nonzero premise suits existing caller. A product-nonzero premise is interconvertible through `Finset.prod_ne_zero_iff`; no demonstrated caller benefit from restatement. |
| 22 | IMPORT-FANOUT | No production import changes. ENat big-operator import is scratch-only for independent proof. |
| 23 | CASTS | Diff: 0 dropped / 0 cross-type / 0 load-bearing casts. Signature annotations identify binder types, not redundant coercions. |
| 24 | INSTANCE-NAME | No instance declaration/name introduced. Proof-local `classical` supplies finite-set equality decisions. |

## Search and literature

I read `lean4/SKILL.md`, `mathlib-quality/SKILL.md`, the cleanup worker contract,
cleanup-all orchestration/verification contract, golfing rules, proof patterns, search,
generalisation, style, naming, cleanup gates, review stages, profiling, and buzz guidance.
The five search methods were actual calls/searches, not inferred availability.

| Method | Query/evidence | Result |
|---|---|---|
| A LeanFinder | `weighted order of a finite product is the sum of weighted orders`; `...-prod-finder.json` | Bounded direct native request returned DNS error; unavailable, not “no hits”. |
| B Loogle | `MvPowerSeries.weightedOrder, Finset.prod`; `...-prod-loogle.json` | Bounded request returned DNS error; unavailable. |
| C LeanSearch | `weighted order of a product of formal multivariate power series`; `...-prod-search.json` | Bounded request returned DNS error; unavailable. |
| D source search | Full untruncated `rg` for `index_prod`, `weightedOrder_(prod\|mul)` and big-operator routes in mathlib/project | Finds weightedOrder product/multiplication, order product, lower-bound variants; actual source inspected at NoZeroDivisors:176–181. |
| E local name search | Native `weightedOrder_prod`, project root explicit; `...-prod-local.json` | Positive source-backed hit `MvPowerSeries.weightedOrder_prod`; index reported unavailable, so no absence inference. Actual built `#check` verifies it. |

Auxiliary variants checked: `weightedOrder_mul`, `le_weightedOrder_prod`, `order_prod`,
generic `map_prod`, and polynomial-to-power-series ring hom. Common-equivalents table:
no discrete/compact/bornological disguise. Conclusion: partial match used in independent
verification; no claim that exhaustive absence has been established. Native `exact?` and
`apply?` attempts hit the default 200000-heartbeat limit; no limit was raised.
No production identifiers were introduced: identifier-verification table has zero rows.

Actual public literature queries follow. An initial combined search returned an unpartitioned
result list; each query was repeated individually to capture the first three displayed leads
reliably. Rankings below are those individual repeated calls, not reconstructed rankings.

| Query (individual repeat) | Rank | Displayed lead |
|---|---:|---|
| `Roth polynomial index product additivity index lemma generalization weighted order` | 1 | [Heights in Diophantine Geometry, Scribd mirror](https://www.scribd.com/document/480772625/Heights-in-Diophantine-Geometry-E-Bombieri-W-Gubler-Cambridge-2006-WW-pdf) |
| same | 2 | [Baker–Wüstholz, Logarithmic Forms and Diophantine Geometry, PDF mirror](https://nzdr.ru/data/media/biblio/kolxoz/M/MT/Baker%20A.%2C%20Wuestholz%20G.%20Logarithmic%20Forms%20and%20Diophantine%20Geometry%20%28CUP%2C%202008%29%28ISBN%200521882680%29%28210s%29_MT_.pdf) |
| same | 3 | [AMS, Chapter 4: Rational](https://www.ams.org/bookstore/pspdf/mbk-48-prev.pdf) |
| `site.stacks.math.columbia.edu order vanishing product valuation` | 1 | [Stacks book PDF, Orders of vanishing p.724](https://stacks.math.columbia.edu/download/book.pdf) |
| same | 2 | [Stacks §10.121, Orders of vanishing](https://stacks.math.columbia.edu/tag/02MB) |
| same | 3 | [Stacks Definition 31.27.3](https://stacks.math.columbia.edu/tag/02RJ) |

Primary evidence actually read: local `clean.tex:530–550,589–614` states the index with
positive real weights and proves binary additivity via nonvanishing lowest-weight components.
[Stacks Lemma 10.121.1](https://stacks.math.columbia.edu/tag/02MB) supplies the related
nonzerodivisor order-additivity paradigm (not an identification with this multivariate index).
AMS open returned an internal error; mirror leads were not used as authoritative evidence.
No ChatGPT math MCP tool was available in discovered metadata. Literature suggests exploring
positive real weights and domain-valued coefficients, but those change the definition/API;
no such proposal was applied. The concrete-to-abstract inversion identifies valuation-like
finite-product additivity; the existing weightedOrder API already provides that abstraction.

## Every binder: mechanical generalisation

Probes use `autoImplicit false`; sources/logs in `/private/tmp/roth-index-prod-probes/`,
summary `/private/tmp/roth-index-prod-binders.json`. Data-drop failures below establish
that deletion does not preserve a well-formed existing statement; they are not theorem
counterexamples. Universe binders already use `Type*` independently for σ and ι.

| Binder | Class/use | Actual candidate and result |
|---|---|---|
| `{σ : Type*}` | type variable, polynomial variables | Delete → unknown σ in Fintype/polynomial types. Already universe-polymorphic. |
| `[Fintype σ]` | typeclass, `index`/weight enumeration | Delete and replace by `[Finite σ]` separately → failure to synthesize Fintype σ in statement. No weaker parent supplies chosen enumeration directly. |
| `[DecidableEq σ]` | decidability, unused | Drop via approved scoped omit → actual module/LSP/recovery pass, built `#check` confirms absent. |
| `{ι : Type*}` | type variable for product | Delete → unknown ι. No finiteness/decidability class required; universe already general. |
| `(s : Finset ι)` | structure value, product/sum domain | Delete → unknown s in hf and conclusion. Replacing finite set by arbitrary set restates both operators, not a mechanical weakening. |
| `{f : ι → MvPolynomial σ ℝ}` | structure value, factors | Delete → unknown f in hf/conclusion. Coefficient abstraction requires a different definition/public API. |
| `(hf : ∀ i ∈ s, f i ≠ 0)` | proposition, insert factor and remaining product | Delete → unknown hf at both insert proofs. Already point-local to s; outside-s assumptions not required. Product-nonzero equivalent noted above. |
| `(α : σ → ℝ)` | structure value, translation point | Delete → unknown α in conclusion. No proposition to weaken; arbitrary point retained. |
| `{r : σ → ℕ}` | structure value, weights | Delete → unknown r in hr/conclusion. Arbitrary function retained; real weights would be a new definition/API. |
| `(hr : ∀ j, 0 < r j)` | proposition, zero-index iff and index_mul | Delete → unknown hr; strict→weak `0 ≤ r j` → mismatch at zero-index iff. Restrict positivity to variables occurring in factors → mismatch with global positivity required by same proof. Retain; failed proof does not rule out a different proof of a wider statement. |

One hr probe initially collided with rebuilding `Index.olean`; that environment failure was
discarded and the same probe rerun after the module build. Final failure is the expected
unknown `hr`, not a missing import. All other data/type/proposition probes produced concrete
elaborator failures. No unapproved weakening was applied or claimed mathematically impossible.

## Signature packing and inequalities

Final actual built `#check @Roth.index_prod`, with `set_option format.width 100`:

```lean
@index_prod : ∀ {σ : Type u_2} [inst : Fintype σ] {ι : Type u_3} (s : Finset ι) {f : ι → MvPolynomial σ ℝ},
  (∀ i ∈ s, f i ≠ 0) →
    ∀ (α : σ → ℝ) {r : σ → ℕ}, (∀ (j : σ), 0 < r j) → index (∏ i ∈ s, f i) α r = ∑ i ∈ s, index (f i) α r
```

Codepoint arithmetic includes indentation, excludes newline. Complete binder/conclusion is
the syntactic packing unit; the final conclusion contains 57 codepoints without indentation.

| Source signature line | Width | Next complete token | Arithmetic | Action |
|---|---:|---|---|---|
| 178 theorem through hf | 96 | `(α : σ → ℝ)` = 11 | 96 + 1 + 11 = 108 > 100 | Keep break |
| 179 α/r/hr through colon | 49 | Conclusion through `:= by` = 57 | 49 + 1 + 57 = 107 > 100 | Keep break |
| 180 conclusion | 61 | No next signature token | n/a | Keep |

| # | Inequality location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | hr | `0 < r j` | Already smaller-left | None |
| 2 | All signature/hypotheses | No `≥` or `>` occurrence | n/a | No `_ge_`/`_gt_` name |

## All 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 | n/a: no `by exact` wrapper. |
| 1.2 | n/a: no `by rfl`. |
| 1.3 | Checked empty branch `rw; exact`: following proof is a constructed iff application, not a hypothesis made exact by rewriting. Explicit two-step proof retained. |
| 1.4 | n/a: no simp followed by exact/assumption. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no constructor pair. |
| 1.7 | n/a: no apply/exact pair. |
| 1.8 | n/a: no contradiction proof. |
| 1.9 | Membership-transforming lambdas cannot η-reduce to hf; normalized their arrows only. |
| 1.10 | n/a: no have. |
| 1.11 | n/a: no apply/intro pair. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no destructured have. |
| 1.14 | Already one rewrite chain per branch; none consecutive to merge. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Existing `.2`/nonzero-iff projections already direct; no verbose dot-notation opportunity. |
| 1.18 | Checked `<|` alternative for `(by simp)`; no clarity or line saving, retained ordinary application under minimum-value rule. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no private existential wrapper. |
| 2.1 | Native grind attempt fails on whole index equality; default limits retained. |
| 2.2 | n/a: no production grind prefix to delete. |
| 2.3 | Compiled alternative replaces the two-tactic base with `simp [index]`; 922 vs 900 heartbeats, rejected for marginal compression/performance regression. |
| 2.4 | n/a: no analytic function-property goal. |
| 2.5 | n/a: no positivity subgoal in proof; factor nonzero is supplied by hf, not sign/order structure on polynomials. |
| 2.6 | n/a: additive equality, no monotonicity inequality. |
| 2.7 | n/a: no Nat/Int arithmetic goal. |
| 2.8 | Native aesop fails exhaustive search; replacement of classical also leaves DecidableEq ι obligation, so not a valid replacement. |
| 2.9 | n/a: no concrete numeric or cast calculation. |
| 2.10 | n/a: equality of arbitrary index values is not finite decidable computation. |
| 2.11 | n/a: no denominator algebra in production proof. |
| 2.12 | n/a: no ring/ring_nf ending. |
| 2.13 | n/a: empty/insert cases have different roles, no symmetric duplicate. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: no similar parallel refinement goals; branch proofs differ. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactic. |
| 3.3 | n/a: no omega or arithmetic tactic. |
| 3.4 | n/a: no rcases-rfl substitution. |
| 3.5 | No attribute added: this conditional project index identity has no newly demonstrated global automation need; no API change authorized. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no maxHeartbeats override. |

Step-back review: one-tactic grind/simp/aesop attempts do not solve the goal; exact?/apply?
time out. The current induction states the mathematics directly. A genuinely different
weightedOrder finite-product route was proved independently, but needs a scaled-order
bridge and ENat sum transport; it is longer than the production induction. No additional
production helper is warranted. Scope-local simplify review: PASS-THROUGH after the approved
omission/lambda cleanup; no remaining reuse/structure issue. Owner performs independent
file-level simplify, rather than this worker claiming to be a second reviewer.

## Verification, failures, performance, and gates

Artifact prefix below is `/private/tmp/roth-index-`.

| Check | Actual evidence/result |
|---|---|
| Module build | `/Users/ramin/.elan/bin/lake build Roth.Index` exit 0; `prod-module.log`, Built Roth.Index 7.3s / 1501 jobs. |
| Native diagnostics | Bounded direct native `lean_diagnostic_messages` on **entire** Index, no severity/range filtering; `prod-after-lsp.json`: success=true, partial=false, timed_out=false, failed_dependencies=[]; 0 errors, 0 target warnings. |
| Remaining native warnings | 14 total: preserved header at line1; section/unused-decidable warnings for neg, C_mul, scaling, rename, card, unique; unused card.hr. They belong to other checkpoints; no suppression added. Baseline had16 including two target warnings. |
| Independent original proof | `prod-independent.lean/.log`, CLI exit0. Imports only original lower dependencies plus ENat.BigOperators, **not Roth.Index**. Recreates index definition literally; reproduces the lower weight/weighted-order bridge from the prior mul-independent scratch (attribution), then proves the finite-product claim freshly via `weightedOrder_prod`, `ENat.toNat_sum`, and generic ring-hom product transport. No Index theorem/private support shortcut used. |
| Original independent signature | Actual `#check` includes original `[DecidableEq σ]`, Fintype, both universes, all data, hf and hr. Unused-decidable warning is intentional for the original contract. |
| Exact original-type recovery | `prod-recovery.lean/.log`, exit0 after actual module build: original snapshot's full target statement under original section binders is proved by actual `Roth.index_prod s hf α hr`. This is separate from independent proof and axiom checks. |
| Actual axioms | Actual built target, original recovery, and independent original proof each print exactly `[propext, Classical.choice, Quot.sound]`. No sorryAx/native-decide/custom axiom. |
| Profile before | `lake env lean --profile -Dtrace.profiler=true -Dtrace.profiler.threshold=0 Roth/Index.lean`, exit0; `prod-before-profile-trace.log`, parser `prod-before-profile-table.json`: target command46.34ms, proof379.07ms, total429.52ms. |
| Profile final | Same actual command, exit0; `prod-after-profile-trace.log`, parser `prod-after-profile-table.json`: command38.17ms, proof385.00ms, total433.14ms. All19 source declarations anchored by parser assertion. Dominant target step: induction379.179ms. |
| Measured alternative | `prod-candidate.lean` exit0; corrected `prod-comparison.lean/.log` exit0: original900 vs `simp [index]` base922 heartbeats. Retain readable original; no claimed speedup from noise-sized wall-time difference. |
| Native attempts | `prod-attempts.json` retains actual failure diagnostics for grind/simp/aesop/exact?/apply?. No incomplete automation proof adopted. |

Scratch failures corrected before acceptance: initial nonexistent `MvPolynomial.coe_prod`;
generic ringHom rewrite did not match the coercion; a scratch induction had an overdependent
IH; `ENat.toNat_sum` initially needed its import. Final independent proof uses verified
`map_prod` with `coeToMvPowerSeries.ringHom_apply`. Initial heartbeat command omitted `#`;
corrected and recompiled. An early profile parse ran while the trace was incomplete and
failed its anchoring assertion; discarded, then rerun only after compiler exit0. Those
failed/partial outputs are not used as gate evidence. A final polling call for an already
closed baseline session returned unknown process; no compiler remained running.

Buzz outcome: **FAST-BOARD**, target433.14ms <750ms borderline threshold and1000ms budget.
No performance fix, no added/removed limit raises, no production profiler scaffolding;
no deferrals or same-issue propagation work in this single target. Final full-file resweep
is the owner's gate. No aggregate profiler category is presented as a target timing.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ | Actual module command above exit0. |
| definition_protected | ✓ | No definition/abbrev/source-import change. |
| theorem_statement_protected | ✓ approved exception | Item18: only explicitly approved omission; literal statement unchanged, original type recoverable. |
| structure_gate | ✓ | Body10 ≤15, no conjunction, no long branch. |
| naming_gate | ✓ | Mathematical snake_case, no forbidden pattern; no rename needed. |
| line_packing_gate | ✓ | All signature lines and complete-token arithmetic above. |
| inequality_orientation_gate | ✓ | Zero reversed occurrences in signature/hypotheses. |
| comments / identifiers | ✓ | All block comments unchanged; no inline target comments or new production identifiers. |
| no limits / scaffolding / trust change | ✓ | No such source additions; standard actual axioms above. |
| downstream / full build / LeanEval | Owner | Theta caller identified; owner checks after source release. Not claimed here. |

Renames queued: none; existing queue untouched. Refactoring required for this checkpoint:
none. Broader literature possibilities are research observations, not compiled API proposals.

## Eleven checked worker steps

- [x] Step1: reference documents read.
- [x] Step2: all24 audit items recorded.
- [x] Step2.5: all five actual mathlib methods, failures and verified partial match recorded.
- [x] Step2.6: every binder, mechanical probes, literature and limitations recorded.
- [x] Step2.7: every signature line, codepoint arithmetic and actual width100 #check recorded.
- [x] Step2.8: inequality scan table recorded.
- [x] Step3: all42 numbered golfing rules recorded.
- [x] Step4: alternative strategies/automation and measured comparison reviewed.
- [x] Step5a: complete unfiltered native diagnostics received, target clean.
- [x] Step5b: scoped gates, actual module/independent/recovery/axiom/profile evidence recorded.
- [x] Step6a: no target rename required; shared queue untouched.


## Owner checkpoint d15

Frozen SHA256 `568dc824159ae7476977806bf4eff276e9d175d5317c5381aee0c57a72d2e232`. Fresh whole ORIGINAL nonself reproof, all18 original public
type/value recoveries and all19 actual retained standard-axiom checks: compiler
session51247 exit0, `/private/tmp/roth-index-d15-compatibility.log`.
Approved no-DecEq types are additionally checked by Expr.find?; actual signatures printed.
Sequential owner full then separate LeanEval1153 both exit0(86.70s/23.18s),
Index+Theta hashes stable; `/private/tmp/roth-index-d15-{full,leaneval}.log`.
Worker COMPLETE unfiltered native Index diagnostics success=true partial=false timed_out=false, no faileddependencies, 0target diagnostics/14other warnings; /private/tmp/roth-index-prod-after-lsp.json. External Theta COMPLETE native LSP0errors/23inheritedwarnings/noinfos, caller399 accepted; raw /private/tmp/roth-index-d15-theta-lsp.json.
All original block docs byte-identical, source widths≤100, diff checked before staging.
Exact-path publication precedes the next edit.
