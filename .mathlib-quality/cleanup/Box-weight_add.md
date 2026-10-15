# `Roth.weight_add` — declaration cleanup

Fresh worker `decl08`, baseline HEAD `502a98c`. Owned only `weight_add` and this
report. Original declaration lines 82–83; final lines 83–84. Parent owns full
project and LeanEval checkpoint builds and Git publication.

## Step 1 — references

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md in full, the full declaration
worker prompt, both skills, and relevant style sections covering formatting,
width, documentation, comments, variables, tactic mode, and visibility. Naming
was checked against the explicit gate and skill naming rules.

## Step 2 — audit

The theorem distributes the weighted sum over addition of multi-indices:
pointwise addition commutes with casting to reals, division distributes over
addition, and the finite sum distributes over addition. No positivity of the
denominators is required.

| # | Audit | Finding and action |
|---|---|---|
| 1 | LINT | Baseline target had unusedSectionVars and unusedDecidableInType for DecidableEq. Add scoped omission under the user's explicit approval; both target warnings disappear. |
| 2 | HAVE SCAN | No have bindings, so no single-use intermediate to inline. |
| 3 | SET_OPTION | No local options; none added. |
| 4 | SIMP SQUEEZE | One terminal unsqueezed simp call. Removing any of its three arguments fails to close the goal; keep it. |
| 5 | NAMING | weight_add is snake_case, names the function then the additive input operation, and has no forbidden abbreviation, numeric scheme, or reversed inequality suffix. No rename. |
| 6 | LINE PACKING | All signature tokens fit on one 96-codepoint line; required table below. |
| 7 | BY PLACEMENT | by is at the end of the signature line. |
| 8 | FORMAT | One two-space-indented tactic, no internal blank line, semicolon, trailing whitespace, haveI, or letI. |
| 9 | COMMENTS | No inline proof comments before or after. |
| 10 | DOCSTRING | Existing description and source citation preserved byte-for-byte. It describes additivity and its mathematical source. |
| 11 | VISIBILITY | Public API is used in Lattice, Index, and Theta. Retain public visibility. |
| 12 | STRUCTURE | One body line, no conjunction, no branches. Extraction would add unnecessary structure. |
| 13 | MATHLIB | Five-method evidence below: sum_add_distrib and bundled Finsupp.weight map_add provide generic content. Retain the project API as directed; no definition migration authorized. |
| 14 | JUNK DEF | n/a: theorem, not a definition. |
| 15 | EXISTS LEMMA | n/a: no existential statement or witness. |
| 16 | SHOW vs CHANGE | Neither construct occurs. |
| 17 | PUSH_NEG | No negation-pushing tactic. |
| 18 | GENERALISE | Approved unused DecidableEq removal verified; Fintype drop and Finite replacement fail. Parameter table below. |
| 19 | INEQUALITY | No inequality in the signature or hypotheses; required table below. |
| 20 | NORMAL-FORM | Function applied to sum on LHS, sum of function values on RHS is the standard map_add form. |
| 21 | SYNTAX-GEN | OK: explicit r, d, e allow direct rewriting; callers already use rw [weight_add]. |
| 22 | IMPORT-FANOUT | n/a: no import changes. |
| 23 | CASTS | 0 dropped / 0 kept as cross-type / 0 kept as load-bearing in the source diff, which is only an omit command. |
| 24 | INSTANCE-NAME | n/a: theorem, no instance declaration. |

Issues: one redundant instance producing two diagnostics; fixed. No deferred
refactoring within the approved scope.

### Mathlib search status

| Method | Query/evidence | Result |
|---|---|---|
| A — Lean-Finder | sum of weighted natural finitely supported functions preserves addition | Returned Finsupp.sum_nsmul and Finsupp.sum_add_index': support-sum and additivity infrastructure. |
| B — Loogle | `Finset.sum, _ + _` | Returned Finset.sum_induction_nonempty, sum_induction, and sum_hom_rel; general infrastructure, not a shorter direct application to the project definition. |
| C — LeanSearch | Weighted-sum additivity route | Unavailable: inherited HTTP 500 established for this file; parent directed no repeated retries. Not evidence of absence. |
| D — source search | Untruncated weight_add, sum_add_distrib, weight_eq_sum, map_add searches in Finsupp/Weight and Finset/Defs; read Finsupp/Weight lines 70–107 | Finsupp.weight is an AddMonoidHom; weight_eq_sum identifies it with a finite sum. No dedicated weight_add text is needed because map_add is generic. |
| E — local names | sum_add_distrib | Positive result Finset.sum_add_distrib in Algebra/BigOperators/Group/Finset/Basic. Index warming; no absence inference. |

Auxiliary variants: Finsupp.sum_add_index', Finsupp.sum_nsmul,
Finsupp.weight_eq_sum, and generic map_add. The independent probe compiles the
generic bundled route using inverse real weights. This is a representation
alternative, not a missing mathlib theorem. Common-equivalents buckets for
discrete, finite subsets, separation, and boundedness do not apply.

Conclusion: partial match for the current project definition, with general
content already supplied by mathlib. Keep the existing project theorem and
definition under the explicit API-preservation scope; no new wrapper or API is
introduced. Its one-line simp proof uses the existing generic sum lemma.

### Generalisation status

| # | Parameter | Class | Use | Candidates and verification | Result |
|---|---|---|---|---|---|
| 1 | σ : Type* | type variable | Domain of parameters and multi-indices | Already universe-polymorphic; dropping σ would leave the domain unbound | Keep |
| 2 | Fintype σ | typeclass | Required by weight's full finite sum | Drop; replace by Finite σ; direct compiler probes both fail to synthesize Fintype at statement line | Keep |
| 3 | DecidableEq σ | decidability | No occurrence in type or proof | Drop using scoped omit; module and complete native diagnostics pass, final #check omits it | Removed with explicit user approval |
| 4 | r : σ → ℕ | structure value | Denominator vector in each term | Drop would unbind r; no strict/global hypothesis to weaken | Keep |
| 5 | d : σ →₀ ℕ | structure value | First additive input in conclusion | Drop would unbind d; changing coefficient type requires changing weight | Keep |
| 6 | e : σ →₀ ℕ | structure value | Second additive input in conclusion | Drop would unbind e; changing coefficient type requires changing weight | Keep |

No propositional hypotheses, strict inequalities, topology assumptions, or
bundled bijections exist. The inversion check identifies generic additivity
after unfolding weight; mathlib already captures this with Finsupp.weight as
an additive homomorphism. A field/module/support-sum reformulation would change
the protected definition and API. It is outside the user's approved removals,
so no broader generalisation is applied or added to the work queue.

### Literature search status

Web query: `weighted sum additivity generalization linear combination linear map`.
The first three returned hits were ordered weighted averaging (a different
construction), a digital-signal-processing linearity section, and pointwise
vector operations. A focused primary-source query, `weighted sums additivity
linear maps site:math.mit.edu`, returned these top three:

1. [MIT 15.1 Synopsis](https://math.mit.edu/~djk/18_022/chapter15/section01.html):
   linear transformations preserve weighted sums.
2. [MIT 18.700 Day 14](https://math.mit.edu/~sschiavo/18-700/Lectures/LessonPlan14.pdf):
   weighted inner products have additivity; positivity is for the inner-product
   axioms, not needed to distribute addition.
3. [MIT Functional Analysis Chapter 1](https://math.mit.edu/~rbm/18-102-S17/Chapter1.pdf):
   vector-space distributivity and linear maps give the abstract context.

Inference from these sources: the canonical broader description is additivity
of a weighted linear functional. This agrees with the existing bundled mathlib
construction; it does not motivate new assumptions or an API rewrite here.
ChatGPT math MCP: unavailable in the tool catalog. No second-opinion result is
claimed. Literature-driven changes within approved scope: none beyond removal
of the unused instance.

### Line packing — weight_add

Width-100 reference from final compiled #check:

```lean
@weight_add : ∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) (d e : σ →₀ ℕ), weight r (d + e) = weight r d + weight r e
```

| Signature line | Codepoints | Next signature token | current + 1 + next ≤ 100? | Action |
|---|---:|---|---|---|
| Original 82 / final 83 | 96 | None; proof body follows | n/a: every signature token is already on this line | ok |

The source declaration is 96 codepoints measured by Python len, not byte count;
no rewrapping is needed. The diagnostic renderer prints the full type on one
line even with format.width set to 100; the source itself meets the width gate.

### Inequality scan — weight_add

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 1 | Entire signature and all hypotheses | No ≥ or >, nor ≤ or < | n/a | n/a: weight_add has no inequality suffix |

## Step 3 — all golfing rules

- [1.1] by exact wrapper: n/a; proof is simp.
- [1.2] by rfl: n/a; no reflexivity proof wrapper.
- [1.3] rw + exact: n/a; neither tactic occurs.
- [1.4] simp + exact: n/a; simp already closes.
- [1.5] trailing rfl: n/a; none.
- [1.6] constructor pair: n/a; equality has no conjunctive witnesses.
- [1.7] apply + exact: n/a; no chain.
- [1.8] by_contra + push_neg: n/a; neither occurs.
- [1.9] eta-reduce: n/a; no lambda in the proof.
- [1.10] inline have: n/a; no bindings.
- [1.11] apply + intro: n/a; no chain.
- [1.12] redundant show: n/a; absent.
- [1.13] have + projections: n/a; absent.
- [1.14] consecutive rw: n/a; absent.
- [1.15] unsqueeze terminal simp only: n/a; already terminal simp.
- [1.16] squeeze nonterminal simp: n/a; no nonterminal simp.
- [1.17] dot notation: n/a; simp lemma names need no receiver syntax.
- [1.18] use <|: n/a; no parenthesized tactic argument.
- [1.19] push_neg: n/a; absent.
- [1.20] trivial existential lemma: n/a; equality theorem.
- [2.1] grind: live bare grind failed; enriched optional batch stalled and was terminated, so no result claimed for that trial.
- [2.2] delete before grind: n/a; no grind retained.
- [2.3] simpa consolidation: n/a; current proof already one closing simp call.
- [2.4] fun_prop: n/a; no function-property predicate.
- [2.5] positivity: n/a; equality, not a positivity goal.
- [2.6] gcongr: n/a; no order relation or monotonicity step.
- [2.7] lia/omega: n/a; goal is equality of real sums with division, not Nat/Int arithmetic.
- [2.8] aesop: live attempt failed, made no progress.
- [2.9] norm_num/norm_cast: cast normalization is already handled by simp; optional norm_cast trial was in the terminated batch and no success is claimed.
- [2.10] decide: n/a; unbounded symbolic real equality is not a finite computation.
- [2.11] field_simp; ring: attempted in the optional batch that stalled; no validated result. The existing one-line distributive simp proof remains verified and shorter than a two-step denominator-clearing proof.
- [2.12] linear_combination: n/a; no ring-ending proof with contextual algebraic equations.
- [2.13] wlog: n/a; no case split or duplicated symmetric branches.
- [2.14] collapse calc: n/a; no calc.
- [2.15] close multiple goals: n/a; original proof has one goal.
- [3.1] erw → rw: n/a; absent.
- [3.2] continuity/measurability: n/a; absent.
- [3.3] omega → lia: n/a; no arithmetic tactic retained.
- [3.4] rcases rfl: n/a; absent.
- [3.5] register automation: retain existing API attributes; adding a new global simp normal form is outside this cleanup's approved changes.
- [3.6] simp_all: no simp_all only to unsqueeze; optional simp_all trial produced no retained result after batch termination.
- [3.7] remove heartbeat option: n/a; no option.

## Step 4 — reflection and actual experiments

Live multi-attempt at the original proof line tested bare simp, simp [weight],
simp [weight, add_div], simp [weight, Finset.sum_add_distrib], grind, aesop,
exact?, and apply?. The first four fail respectively because weight is opaque,
division and sum distribution remain, sum distribution remains, or division
distribution remains. grind and aesop failed; exact? found no complete proof.
apply? offered partial real-equality/subtraction routes, including a partial
IsLinearMap route, and left a temporary sorry diagnostic in the probe only.
No probe code or sorry was inserted into the source.

An extra batched native trial stalled and was terminated without counting any
of its unreturned results. The required independent proof, type, axiom, and
drop tests were completed through direct local Lean compilation instead.

The independent proof uses the original one-line simp body without calling
weight_add and without any DecidableEq instance. A second successful example
uses generic map_add with Finsupp.weight of the inverse real parameters; this
is longer than the existing proof and needs representation conversion. Term
mode offers no shorter direct application for the current definition. No
helper, option, new import, or new public declaration is warranted.

## Step 5 — verification and gates

- `/Users/ramin/.elan/bin/lake build Roth.Box` exited 0, session 58332,
  1154 jobs; log `/private/tmp/roth-box-d08-module.log`.
- Complete native diagnostics: success true, partial false, timed_out false;
  zero errors, zero target warnings. The 14 warnings concern future declarations
  or the user-preserved header. They are not suppressed.
- Native lean_verify: standard trust; propext, Classical.choice, Quot.sound;
  no nonstandard axioms and no suspicious source patterns.
- Isolation/type/axiom/generic route source:
  `/private/tmp/roth-box-d08-isolation.lean`; compiler log with final type and
  standard axioms `/private/tmp/roth-box-d08-isolation.log`; direct compiler
  session 15678 exited 0.
- Fintype drop and Finite replacement negative probes:
  `/private/tmp/roth-box-d08-drop.lean`; log shows failed Fintype synthesis at
  both statements; direct compiler session 39419 exited 1 as expected. These
  intentional failures are confined to scratch files.
- `git diff --check` exits 0. The source diff contains exactly one added omit
  command; theorem text, body, docstring, imports, and definitions are unchanged.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | Actual module build exit 0, log above |
| definition_protected | pass | No def or abbrev changes |
| theorem_statement_protected | pass | Text unchanged; elaborated unused instance removed under explicit approval and audit item 18 |
| structure_gate | pass | One body line, no conjunction or branches |
| naming_gate | pass | Descriptive weight_add, no forbidden pattern |
| line_packing_gate | pass | Complete one-row table; 96 codepoints |
| inequality_orientation_gate | pass | Complete scan table; no reversed inequalities |

Overall: pass. Full project and separate LeanEval checkpoint gates belong to
the parent and are not claimed by this declaration worker.

## Step 6 — result and checklist

Before: 2 declaration lines. After: 2 declaration lines. Saved: 0; one scoped
omit line added. Audit issues: 1 fixed, 0 deferred. Applied change: approved
mechanical generalisation removing redundant decidability. Proof retained
after live alternatives failed or offered no improvement. Renames queued:
none. Comments preserved: none present; docstring unchanged. Refactoring needed:
none within authorized scope.

- [x] Step 1 — required references read.
- [x] Step 2 — all 24 audit items answered.
- [x] Step 2.5 — five-method search status and generic compiled probe.
- [x] Step 2.6 — every parameter audited; public literature search recorded.
- [x] Step 2.7 — complete signature width table.
- [x] Step 2.8 — complete inequality scan.
- [x] Step 3 — all 42 golfing rules have a status.
- [x] Step 4 — live alternatives and whole-proof reflection.
- [x] Step 5a — complete native diagnostics, no target warnings or errors.
- [x] Step 5b — module build, diff gates, type/axiom/isolation evidence.
- [x] Step 6a — no rename needed; queue untouched.

Publication verification: full `lake build` session 60506 exited 0 (2586 jobs;
`/private/tmp/roth-box-d08-full.log`); separate `lake build Roth.LeanEval` session 78621
exited 0 (2585 jobs; `/private/tmp/roth-box-d08-leaneval.log`). All affected dependents pass.
