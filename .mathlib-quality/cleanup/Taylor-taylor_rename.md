# `MvPolynomial.taylor_rename` dedicated audit

Target: `Roth/Taylor.lean:158–160` (original task range 176–178).
Branch/baseline supplied by parent: `ramin-cleanup` / `7472875`.
Worker start source SHA: `d4a821b4ee428a5e8b052cb7a6cd0a62a9830b3fdb5a3d78557b86bd29d2dd74`.
Frozen source SHA: `4cd871acc4a0ad26ceba2c01bef9ee5c88e0f5117254a50d24a895b56af32f7a`.
Source ownership explicitly revoked after freeze; this report is the only subsequent edit.

Read lean4 and mathlib-quality SKILL.md, the full worker contract, golfing-rules.md,
proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md,
naming-conventions.md, mathlib-review-stages.md, and relevant style-rules.md sections
(line width, formatting, comments/docs, inequalities, syntax, declarations, tactics,
visibility, hypotheses, imports, normal forms, casts and simp attributes).

## Full audit (24 items)

1. LINT: native diagnostics report no target warning; pre-existing line-1 copyright/header
   warning remains and is outside ownership.
2. HAVE SCAN: no `have` in the original or final proof; no single-use intermediary to inline.
3. SET_OPTION: no declaration-local options or resource-limit increases.
4. SIMP SQUEEZE: original `simp_all` is terminal in each induction branch; final explicit
   `simp [...]` closes the entire goal and remains unsqueezed.
5. NAMING: `taylor_rename` describes the operations in the conclusion, is snake_case,
   and matches none of the forbidden abbreviations, numeric patterns or single-letter names.
6. LINE PACKING: measured both signature lines; complete table below, no repack needed.
7. BY PLACEMENT: `:= by` ends signature line 159.
8. FORMAT: two-space proof indentation, no internal blank lines or trailing whitespace;
   final proof is a single tactic, without local instances or chained semicolons.
9. COMMENTS: no inline proof comments were present; all three docstring lines preserved.
10. DOCSTRING: existing public description and source reference preserved verbatim under
    the explicit API/doc preservation requirement and lean4 Rule A.
11. VISIBILITY: public translation compatibility API preserved as expressly requested.
12. STRUCTURE: one proof-body line, no conjunction, no remaining branches; no extraction needed.
13. MATHLIB: all five search methods used; direct composition proof uses existing API below.
14. JUNK DEF: n/a, target is a theorem.
15. EXISTS LEMMA: n/a, no existential conclusion or private witness helper.
16. SHOW vs CHANGE: n/a, neither occurs.
17. PUSH_NEG: n/a, no negation tactic.
18. GENERALISE: all eight effective parameters tested/classified below; no accepted weakening.
19. INEQUALITY: zero reversed inequalities and no `_ge_`/`_gt_` name segment; table below.
20. NORMAL-FORM: equality pushes translation through renaming to the RHS; coherent with
    `aeval_rename` and composition on assignments. No equivalence family needed.
21. SYNTAX-GEN: OK, arbitrary renaming and translation assignments already accepted;
    no injectivity, surjectivity, finiteness or decidable-equality assumptions.
22. IMPORT-FANOUT: n/a, no imports added or changed.
23. CASTS: 0 dropped / 0 cross-type / 0 load-bearing ascriptions introduced in the diff.
24. INSTANCE-NAME: n/a, theorem introduces no instance declaration.

Issues fixed: proof strategy now expresses substitution composition directly, avoiding
polynomial induction. No statement, definition, attribute, visibility or documentation change.
Refactoring needed: none. No public-wrapper deletion is proposed; preserving this API is explicit.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | multivariate polynomial substitution commutes with renaming variables | `rename_bind₁`, `rename_comp_bind₁`, `bind₁_rename` |
| B Loogle | `MvPolynomial.rename, MvPolynomial.aeval` | `rename_eq_aeval`, `aeval_comp_rename`, `aeval_rename` (also deprecated `rename_eq`, not used) |
| C LeanSearch | Multivariate polynomial aeval renaming variables composition | `aeval_rename`, `aeval_comp_rename`, `map_comp_rename`, `eval_rename` |
| D source rg | `rename.*(aeval\|eval₂)\|aeval.*rename\|eval₂.*rename` in Algebra/MvPolynomial | Rename.lean:98,239–258; Monad.lean substitution variants; no absence claim |
| E local name | `aeval_rename`, project root supplied | found `MvPolynomial.aeval_rename`; index `unavailable`, so no negative index inference |

Auxiliary variants examined: `aeval_comp_rename`, `eval₂_rename`, `eval₂Hom_rename`,
`rename_eval₂`, `rename_eq_aeval`, `comp_aeval_apply`, `rename_bind₁`, `bind₁_rename`.
Common-equivalents table: no discrete/finiteness/separation/boundedness bucket matches.
Conclusion: partial match via general substitution composition. Keep the requested public
translation API and build directly on `rename_eq_aeval` and `comp_aeval_apply`.
Both names were independently checked in the pretarget-prefix compilation. No unsupported
claim of complete Mathlib absence is made; whole-goal `exact?`/`apply?` reached the default
200000 heartbeat limit, which was not raised.

## Generalisation status

Each drop experiment used native `lean_run_code`, imports excluding `Roth.Taylor`, an
identical independently named translation definition, `autoImplicit false`, and explicit
binders. All returned `success=false`, `timed_out=false`; failed probes never touched the
live declaration. The final live whole-file diagnostic is separately complete and clean.

| Parameter | Class / use | Mechanical candidates actually tested | Verified? / result |
|---|---|---|---|
| `{σ : Type*}` | type variable, source variable set | drop σ | yes: unknown σ at source assignment/polynomial; retained; already universe polymorphic |
| `{R : Type*}` | type variable, coefficients | drop R | yes: unknown R in class/assignment/polynomial; retained; already universe polymorphic |
| `[CommSemiring R]` | typeclass, translation and rename algebra API | drop; weaken to `[Semiring R]` | yes: both fail `CommSemiring R` synthesis in statement; retained |
| `{τ : Type*}` | type variable, renamed variable set | drop τ | yes: unknown τ in f/α; retained; already universe polymorphic |
| `(f : σ → τ)` | structure value, variable renaming | drop f | yes: unknown f at rename/composition; retained |
| `(α : τ → R)` | structure value, translation assignment | drop α | yes: unknown α at translation/composition; retained |
| `(P : MvPolynomial σ R)` | structure value, input polynomial | drop P | yes: unknown P in both sides; retained |
| universes of σ/R/τ | universe parameters | inspect compiled original-type output | yes: three independent levels; no fixed universe to weaken |

Catalogue exclusions: no proposition, strict inequality, global analytic property,
decidability hypothesis, concrete scalar field, bijection or bundled embedding exists to
weaken or localise. `Semiring` is the relevant immediate algebra parent; weaker parents
cannot supply the missing `CommSemiring` required even to state the existing API.
No binder can be removed while preserving the conclusion. Replacing dependent values with
new quantifiers would only rebind the same parameters. No small-safe result was available.
Inversion check: translation unfolds to general substitution; that abstract API already
exists (`comp_aeval_apply`, `rename_eq_aeval`), and the final proof uses it. No new helper needed.
Big-change candidates: none needed; no unsupported noncommutative restatement is proposed.

## Public literature search

WebSearch actual query: `multivariate polynomial substitution renaming variables universal
property generalization`. Top three displayed hits:

1. [Multivariate subresultants](https://www.sciencedirect.com/science/article/pii/002240499590926C)
   — unrelated subresultant generalisation; no hypothesis conclusion drawn.
2. [Mathlib Rename documentation](https://firsching.ch/FormalBook/docs/Mathlib/Algebra/MvPolynomial/Rename.html)
   — variable renaming and evaluation API.
3. [Mathlib Rename documentation mirror](https://teorth.github.io/analysis/docs/Mathlib/Algebra/MvPolynomial/Rename.html)
   — same API, not independent mathematical evidence.

Follow-up queries: `site.stacks.math.columbia.edu polynomial ring universal property` and
`site.leanprover-community.github.io/mathlib4_docs MvPolynomial aeval_algHom_apply`.
Top three displayed combined hits were official Mathlib Eval, Matrix.MvPolynomial and
Analytic.Polynomial documentation. The directly relevant primary reference is
[Mathlib Eval](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Eval.html),
whose `comp_aeval_apply` gives composition under arbitrary commutative semiring algebras.
The canonical universal-property formulation also appeared in
[Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring); it explains the algebra
homomorphism viewpoint, without supporting a stronger noncommutative claim.
Finding: the current result is naturally a substitution-composition specialisation; it
already permits arbitrary index sets and commutative semirings. No additional assumption
weakening was established. Math ChatGPT MCP: n/a, no such callable tool in ALL_TOOLS.
Literature-driven big-change candidates: none.

## Line packing

`#check` with `format.width 100` on the independently named original-type probe:

```lean
@taylor_rename_original_type_probe : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] {τ : Type u_5} (f : σ → τ)
  (α : τ → R) (P : MvPolynomial σ R), (taylor α) ((rename f) P) = (rename f) ((taylor (α ∘ f)) P)
```

The longer probe identifier is only a scratch name; source widths below use the real name.
The next logical token is the complete conclusion, rather than splitting an application.

| Sig line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 158 | 82 | `taylor α (rename f P) = rename f (taylor (α ∘ f) P) := by` (57 chars) | 82 + 1 + 57 = 140 > 100 | ok |
| 159 | 61 | no next signature line | n/a, body next | ok |

No signature changes; final proof line is 50 codepoints.

## Inequality scan

| # | Location | Original | Rewrite | Rename? |
|---|---|---|---|---|
| — | entire signature and inherited parameters | no `≥` or `>` inequalities | n/a | no `_ge_`/`_gt_` segment |

## Every golfing rule

| Rule | Status and evidence |
|---|---|
| 1.1 | n/a: no `by exact` wrapper |
| 1.2 | n/a: no `by rfl` |
| 1.3 | n/a: no rw/exact sequence |
| 1.4 | n/a: no simp/exact sequence |
| 1.5 | n/a: no trailing rfl |
| 1.6 | n/a: equality, no constructor pair |
| 1.7 | n/a: no apply/exact sequence |
| 1.8 | n/a: no contradiction/negation |
| 1.9 | n/a: no proof lambda to eta-reduce |
| 1.10 | n/a: no have |
| 1.11 | n/a: no apply/intro sequence |
| 1.12 | n/a: no show |
| 1.13 | n/a: no projections or have |
| 1.14 | n/a: no consecutive rw |
| 1.15 | n/a: no terminal simp only |
| 1.16 | n/a: all simplification terminal |
| 1.17 | n/a: simp lemma identifiers are not receiver applications |
| 1.18 | n/a: no nested term application with removable parentheses |
| 1.19 | n/a: no push_neg |
| 1.20 | n/a: no existential helper |
| 2.1 | tried live `grind`: failed with negated equality/False goal |
| 2.2 | n/a: final proof has no grind |
| 2.3 | applied direct terminal simp via substitution composition, replacing induction |
| 2.4 | n/a: no analytic function property |
| 2.5 | n/a: no positivity goal |
| 2.6 | n/a: no ordered congruence goal |
| 2.7 | n/a: no Nat/Int arithmetic goal |
| 2.8 | tried live `aesop`: failed, no progress |
| 2.9 | n/a: no numerical/cast goal |
| 2.10 | n/a: arbitrary polynomial equality, no finite decidable computation |
| 2.11 | n/a: no denominator identity |
| 2.12 | n/a: no ring/ring_nf ending or algebraic hypothesis |
| 2.13 | n/a: no symmetric case split |
| 2.14 | n/a: no calc |
| 2.15 | original already used `<;>`; eliminated branch creation entirely |
| 3.1 | n/a: no erw |
| 3.2 | n/a: no continuity/measurability tactic |
| 3.3 | n/a: no omega |
| 3.4 | n/a: no rcases/substitution |
| 3.5 | no new attributes: requested existing API preserved; proof works with explicit API lemmas |
| 3.6 | original terminal simp_all already unsqueezed; direct composition now closes whole goal |
| 3.7 | n/a: no maxHeartbeats option |

Step-back reflection: live bare `simp` made no progress, `grind` and `aesop` failed, and
`exact?`/`apply?` hit default heartbeats. Induction succeeds but is mathematically indirect.
Live direct `simp [taylor, rename_eq_aeval, comp_aeval_apply]` succeeded without warnings;
adding `Function.comp_def` was unnecessary, and adding `aeval_rename` caused an unused-arg
warning. A candidate with an unverified `aeval_algHom_apply` name failed and was discarded;
only independently checked names occur in final source. No live edits were made by these
experiments. An initial multi-attempt used the wrong line (170) and produced parser errors;
it was rerun at the located actual proof line 160, so those parser results were not counted.
Term mode would require exposing the same compositions with more plumbing; no helper or
new public abstraction is justified.

## Verification and diff gates

Actual commands:

* `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited 0; Taylor built in 17 seconds,
  1439 jobs completed. Only existing copyright warnings in Box, HasseDeriv and Taylor.
* `/Users/ramin/.elan/bin/lake env lean /private/tmp/decl14-original.lean` exited 0.
  This file contains the pretarget prefix, excludes the live target and all later source,
  and proves the unchanged original type with the final proof under an independent name.
  `#print axioms` returned exactly `[propext, Classical.choice, Quot.sound]`.
* Native final `lean_diagnostic_messages` on the entire live file returned
  `success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`;
  sole diagnostic is the unchanged line-1 header warning.

Worker diff against `/private/tmp/decl14-before.lean`:

```diff
-  induction P using MvPolynomial.induction_on <;> simp_all
+  simp [taylor, rename_eq_aeval, comp_aeval_apply]
```

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual module build exited 0 |
| definition_protected | pass | no definition lines changed |
| theorem_statement_protected | pass | both signature lines byte-for-byte unchanged |
| structure_gate | pass | one body line, no conjunction/branches |
| naming_gate | pass | descriptive name, no forbidden pattern |
| line_packing_gate | pass | both measured signature rows ok |
| inequality_orientation_gate | pass | complete scan, zero reversed inequalities |

Overall local gates: pass. Full project build and separate LeanEval belong to the parent
after source freeze; neither is claimed here.

## Result and all eleven phase checks

Before: 3 declaration lines. After: 3. Saved: 0 lines; the proof is shorter and all induction
branches eliminated. Audit issue fixed: direct proof strategy. No deferred refactoring,
renames, dropped comments or altered docstrings. Renames queued: none.

- [x] Step 1 — reference docs read.
- [x] Step 2 — complete 24-item audit printed.
- [x] Step 2.5 — all five search methods and auxiliary variants recorded.
- [x] Step 2.6 — per-parameter mechanical tests, inversion check and public literature recorded.
- [x] Step 2.7 — every signature line measured with arithmetic.
- [x] Step 2.8 — complete inequality scan table.
- [x] Step 3 — all 42 golfing rules have individual status.
- [x] Step 4 — whole-goal alternatives and direct/induction comparison recorded.
- [x] Step 5a — native complete live diagnostics clean apart from preserved header warning.
- [x] Step 5b — actual module build, isolated original-type/axiom check and diff gates pass.
- [x] Step 6a — no rename needed; no sidecar mutation required.
