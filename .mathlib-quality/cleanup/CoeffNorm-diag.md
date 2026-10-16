# Phase 4 declaration report: `Roth.diag`

Target: `Roth/CoeffNorm.lean`, L154–156 (two docstring lines, one definition line).
Dedicated owner: d16_diag. Scope: target definition and this report only.
Baseline supplied by parent: full `lake build` passed, then separate exact
`lake build Roth.LeanEval`, session 76914, exit 0; complete baseline LSP without errors.
This worker did not repeat either full-project or LeanEval build.

## Step 1 — references and mathematical meaning

Read both complete skills `/Users/ramin/.codex/skills/mathlib-quality/SKILL.md` and
`/Users/ramin/.codex/skills/lean4/SKILL.md`, and the complete 853-line worker contract
`/private/tmp/roth-coeffnorm-worker-contract.md`, substituting this target/file/range.
Read in full: `golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `style-rules.md`,
`naming-conventions.md`, `mathlib-review-stages.md`, and `mathlib-quality-principles.md`
under `/Users/ramin/.codex/skills/mathlib-quality/references/`.
Large reads were split into consecutive line ranges to avoid truncated output.
The specific initial combined skill read truncated; subsequent complete sequential reads
covered the missing content.

`diag` substitutes the same univariate indeterminate into every variable of an integer
multivariate polynomial. The algebra-homomorphism `MvPolynomial.aeval` supplies exactly
this construction. Its output is a polynomial, rather than a proposition to prove.
No tactic proof is involved. Source `.mathlib-quality/references/clean.tex` L1449
discusses this identification of variables in Lemma 9; L1476–1478 explains why the
coefficient estimates handle it separately (monomials may merge).

## Step 2 — full audit (24 items)

| Item | Finding / action |
|---|---|
| 1 LINT | Complete baseline/final native LSP: zero target errors or warnings. Six existing outside warnings listed below. |
| 2 HAVE SCAN | n/a: no `have` in this one-term data construction; exhaustive list empty. |
| 3 SET_OPTION | None in target or target diff. No limit raise or linter suppression. |
| 4 SIMP SQUEEZE | n/a: no `simp`, `simp only`, or tactic block. |
| 5 NAMING | `diag` describes diagonal substitution, is lowerCamelCase data naming, has four letters, and matches no forbidden numeric pattern or prohibited abbreviation. No rename needed. |
| 6 LINE PACKING | One complete declaration line, 94 codepoints after the arrow edit; signature through `:=` is 63. Full table below. |
| 7 BY PLACEMENT | n/a: direct term definition with no `by`. |
| 8 FORMAT | Replace ordinary lambda `fun _ =>` with `fun _ ↦`. No whitespace/indentation issue or internal blank line; no `haveI`/`letI`. |
| 9 COMMENTS | Two-line mathematical/source docstring preserved byte-for-byte; no inline proof comments. |
| 10 DOCSTRING | Describes the diagonal substitution and gives its source; already concise, useful mathematical context. Preserve under Lean skill Rule A and explicit dispatch. |
| 11 VISIBILITY | Public API, listed in module definitions and used externally in `Roth/MainLemma.lean`; public visibility justified. |
| 12 STRUCTURE | One term, no conjunction, no branch, no extraction/decomposition needed. |
| 13 MATHLIB | Five searches identify general `MvPolynomial.aeval`, already used directly; full evidence below. |
| 14 JUNK DEF | Retain: meaningful diagonal operation with `diag_eq_sum`, `abs_coeff_diag_le`, `natDegree_diag_le`, `eval_diag`, `diag_sub`, and substantial external use. Satisfies explicit keep-test despite one-line construction. |
| 15 EXISTS LEMMA | n/a: data definition, not a private existential lemma. |
| 16 SHOW vs CHANGE | n/a: no `show` or tactic goal conversion. |
| 17 PUSH_NEG | n/a: no negation tactic. |
| 18 GENERALISE | Every parameter and relevant catalogue family analyzed below. Actual isolated drop probes reject removing dependent binders; arbitrary coefficient-semiring extension compiles but is outside the locked public API. |
| 19 INEQUALITY | Zero `≥`/`>` inequalities in signature, hypotheses, or body. Scan table below. |
| 20 NORMAL-FORM | Already uses canonical algebra evaluation; tested definitional equality with `eval₂Hom`. No bridge theorem added. |
| 21 SYNTAX-GEN | OK: `diag P` is convenient at existing polynomial coefficient/degree/remainder call sites; a bundled-hom redesign would change public type. |
| 22 IMPORT-FANOUT | n/a: no new imports. |
| 23 CASTS | casts: 0 dropped / 0 kept as cross-type / 0 kept as load-bearing. No expression ascription or coercion in changed body. Signature type annotations are public parameter/result types. |
| 24 INSTANCE-NAME | n/a: no instance declaration. |

Issues to fix: one routine lambda-arrow style issue, fixed. Refactoring needed: none
within the authorized scope. Optional coefficient generality is discussed below without
changing this integer-polynomial API or creating a new public declaration.

Outside warning inventory, identical before/after: header L1; unused `[DecidableEq σ]`
on `normOne_mul_le` L89, `normOne_prod_le` L99, `normOne_det_le` L112,
`abs_coeff_det_hasseDeriv_le` L268; unused name `hC` L115. Header preservation is explicit
user policy; the other five are outside this worker's target and await scoped decisions.

## Step 2.5 — five-method mathlib search

All native searches were actually invoked; no service failure in these searches.

| Method | Query / result |
|---|---|
| A Lean-Finder | `multivariate polynomial diagonal substitution all variables to univariate polynomial X` → `MvPolynomial.aeval_X_left_apply`, `matPolyEquiv_diagonal_X`, `MvPolynomial.eval₂_eta`; first/third confirm general evaluation, matrix result is different. |
| B Loogle | `MvPolynomial.aeval, Polynomial.X` → `MvPolynomial.optionEquivRight_apply`, `MvPolynomial.optionEquivLeft_apply`, `AlgebraicIndependent.mvPolynomialOptionEquivPolynomialAdjoin_apply`, `Polynomial.aeval_homogenize_X_one`, `Polynomial.homogenize_eq_of_isHomogeneous`; useful evaluation infrastructure, none a reason to replace the established diagonal API. |
| C LeanSearch | `MvPolynomial evaluation all variables at Polynomial.X` → `MvPolynomial.eval_X`, `MvPolynomial.aeval_X`, `MvPolynomial.eval₂_X`. |
| D source rg | `def (aeval|eval₂Hom|rename)`, `aeval_eq_eval₂Hom`, `rename.*sum`, and `aeval.*fun.*Polynomial.X` in algebra/ring-theory MvPolynomial sources → `Eval.lean` L158/569/575, `Rename.lean` L54, `Equiv.lean` L468/623. Full untruncated search for `diag` in these two MvPolynomial trees returned no hits. `Polynomial.lean` has no `diag`/`aeval` match. |
| E local name search | `MvPolynomial.aeval` → definition plus `_C`, `_X`, `_def`, `_sum`, `Tower`, `_prod`, `_zero`, `_ofNat`, `_range`. Index `warming`; positive source hits usable, no absence inferred from this index status. |

Auxiliary variants checked: `_X`, `_C`, `_def`, `_eq_eval₂Hom`, `_sum`, `_prod`,
`eval₂Hom`, `rename`, `optionEquivLeft_apply` / `optionEquivRight_apply`.
Common-equivalents table: no discrete/finite/separation/bornology pattern; generic
evaluation rather than a hidden custom predicate is relevant here.

Concluded: found a partial/general construction match (`MvPolynomial.aeval`);
ACTION: retain the existing meaningful diagonal API and build on this mathlib construction,
which is already exactly the body. No claim of exhaustive mathematical absence, and no new
lemma or definition was invented. Isolated `rfl` probes verify both `aeval` and
`eval₂Hom` representations. Thus the generic compiled route was probed as well as searched.

Six strict rules: (1) no wrapper lemma created; (2) all five searches performed, no
unsupported absence claim; (3) auxiliary variants searched; (4) no custom predicate;
(5) no duplicate theorem found to delete, and the definition has established API/use;
(6) mathlib use documented here, with no out-of-scope module-docstring edit.

## Step 2.6 — generalisation status

`#check @Roth.diag` establishes that the *entire* actual parameter list is `{σ}` and `P`.
There are no hidden instance or propositional parameters in the elaborated type.

| # | Parameter | Class | Used as | Mechanical candidates / actual probes | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type u}` from `{σ : Type*}` | type-variable | Domain of `MvPolynomial σ ℤ` and of constant substitution | Drop binder with autoImplicit false → unknown identifier; universe already arbitrary `u`, successful scratch uses independent universes `u v`. No class parents, point-local or strict→weak predicate exists on this type variable. | yes | Retain; cannot remove dependent domain, no universe restriction to weaken. |
| 2 | `(P : MvPolynomial σ ℤ)` | structure-value | Argument to `aeval` | Drop binder with autoImplicit false → `Unknown identifier P`; change coefficient type ℤ to arbitrary `[CommSemiring R]` in isolated `candidate` construction and specialize back by `rfl`. No predicate to point-localize, strict inequality to weaken, bundled proposition to unbundle, or user-supplied typeclass to weaken/drop. | yes | Retain public parameter/type. General coefficient construction works, but applying it would change public type and downstream coefficient estimates, contrary to the dispatch. |

Every catalogue family: typeclass parents and decidability n/a (none in actual parameter
list); analysis/global-to-pointwise n/a (no continuity/measurability/integrability/order
assumption); strict→weak n/a (no inequalities); unbundling n/a (no Prop/Equiv hypothesis);
drop-tests actually run; universe extension already present; concrete ℤ → arbitrary
commutative semiring construction actually tested in scratch. This does not substitute a
semantically unrelated object: specialization at ℤ is definitionally equal to `diag`.

Inversion check: n/a as theorem-proof diagnostic: this is a direct polynomial construction,
not a proof about a named concrete witness after unfolding. Its only construction is
already the abstract evaluation map, specialized to the coefficient ring used throughout
this module.

Actual native `lean_run_code` removal probes gave `success=false`, `timed_out=false`:
drop P → L6 `Unknown identifier P`; drop σ → L3 `Unknown identifier σ` with autoImplicit
false. These are intentional failing scratch experiments, not source errors.
The generalized `candidate` with independent universe-polymorphic σ/R and
`[CommSemiring R]` compiled successfully; specialization `candidate P = Roth.diag P`
closed by `rfl`. No temporary declarations entered project source.

Big-change candidates: mathematically, diagonal substitution extends from ℤ to any
commutative semiring. This is already supplied by generic `MvPolynomial.aeval` and was
tested as a scratch construction. It is not proposed for this integer norm/bounds module:
public API/value preservation is explicit, and no downstream generic use was identified.
Refactoring needed: none for this task; a future independently requested generic API
could use `aeval` directly.

### Public literature search

Web query 1: `polynomial ring universal property evaluation substitution commutative
semiring diagonal generalization`. Top three returned hits captured:

1. [Polynomial ring, step-by-step](https://maths.free/abstract-algebra/polynomial-ring/).
2. [Polynomial ring mirror](https://wiki.chogus.org/content/wikipedia_en_all_maxi_2025-08/Polynomial_ring).
3. [Polynomial ring](https://en.wikipedia.org/wiki/Polynomial_ring).

These are search leads only; the conclusion is supported by the local primary mathlib
definition/probes and the project's source text, not an unsourced absence assertion.
The same result set included primary author notes
[Bergman, Rings §4.12](https://math.berkeley.edu/~gbergman/245/3.4.pdf) and
[Leinster, universal-property uses](https://www.math.mcgill.ca/darmon/courses/24-25/algebra4/leinster.pdf).

Web query 2: `polynomial ring universal property multivariable generalization`, restricted
to Stacks/nLab/mathlib-documentation domains. Top three returned hits captured:

1. [nLab universal construction](https://ncatlab.org/nlab/show/universal+construction).
2. [Stacks Lemma 23.5.1](https://stacks.math.columbia.edu/tag/07H5).
3. [Stacks divided power algebra PDF](https://stacks.math.columbia.edu/download/dpa.pdf).

The Stacks two hits concern *divided power* polynomial algebras, so are not a license
to replace this ordinary polynomial definition. Further relevant result:
[nLab polynomial](https://ncatlab.org/nlab/show/polynomial), identifying polynomial rings
as free commutative algebras. Primary implementation evidence is
`Mathlib/Algebra/MvPolynomial/Eval.lean` L569, whose generic `aeval` type has only
commutative-semiring/algebra assumptions, tested concretely in the isolated candidate.
The canonical perspective is evaluation of a freely generated algebra; the current
definition already uses it. No finite-variable or nonempty-variable hypothesis is needed.

ChatGPT math MCP: n/a — no `chatgpt-math` capability in `ALL_TOOLS`; no substitute
external conversation was invented. Literature-driven mandatory refactoring: none.

## Step 2.7 — line packing

Actual `set_option format.width 100; #check @Roth.diag` output:

```lean
@Roth.diag : {σ : Type u_1} → MvPolynomial σ ℤ → Polynomial ℤ
```

| Signature line | Chars | Next signature token | current + 1 + next ≤ 100? | Action |
|---|---:|---|---|---|
| L156, keyword through `:=` | 63 | none: body already begins on the same line | n/a: final/only signature line; full line including body is 94 ≤ 100 | ok |

Measured with Python `len` of Unicode strings, not bytes. Before full line was 95
codepoints; after replacing the two-character arrow with one codepoint it is 94.
No signature continuation exists to repack. No underpacked/overlong row remains.

## Step 2.8 — inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| 0 | complete signature / all parameters | n/a — zero `≥`/`>` inequalities | none | n/a — no `_ge_`/`_gt_` name |

The old `=>` was a lambda delimiter, not an inequality, and is now `↦` anyway.
Post-edit scan of the signature and complete target body has no reversed inequality.

## Step 3 — all 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: definition already direct term. |
| 1.2 by rfl | n/a: no tactic wrapper. |
| 1.3 rw + exact | n/a: no rewriting tactics. |
| 1.4 simp + exact | n/a: no simplifier/tactic chain. |
| 1.5 simp; rfl | n/a: no simp or rfl in target. |
| 1.6 constructor | n/a: no proof/product construction. |
| 1.7 apply + exact | n/a: no tactic mode. |
| 1.8 by_contra! | n/a: no contradiction proof. |
| 1.9 eta reduction | n/a: constant lambda ignores variable, so not `fun x ↦ f x`. `Function.const σ Polynomial.X` was tested by rfl but is longer and adds an explicit domain. Ordinary lambda arrow normalized under FORMAT. |
| 1.10 inline have | n/a: no have. |
| 1.11 refine + fun | n/a: no apply/intro pair. |
| 1.12 show | n/a: no show. |
| 1.13 obtain projections | n/a: no have or projections. |
| 1.14 merge rw | n/a: no rw. |
| 1.15 terminal simp only | n/a: no simp. |
| 1.16 nonterminal simp | n/a: no simp. |
| 1.17 dot notation | n/a: no receiver-based call improves the `aeval` construction. |
| 1.18 `<|` | n/a: `(fun _ ↦ Polynomial.X)` is a nonfinal argument followed by P; `<|` cannot replace these parentheses without reassociation. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 inline ∃ | n/a: definition returns polynomial data. |
| 2.1 grind whole proof | n/a: no proposition or multiline proof; data is already one term. |
| 2.2 delete before grind | n/a: no grind. |
| 2.3 simpa | n/a: no simplification/closing proof chain. |
| 2.4 fun_prop | n/a: no analytic predicate. |
| 2.5 positivity | n/a: no order proposition. |
| 2.6 gcongr | n/a: no inequality. |
| 2.7 lia/omega | n/a: no arithmetic proof. |
| 2.8 aesop | n/a: data construction, no logical goal. |
| 2.9 norm_num/norm_cast | n/a: no numeric/cast proof. |
| 2.10 decide | n/a: no decidable proposition. |
| 2.11 field_simp/ring | n/a: no denominator identity. |
| 2.12 linear_combination | n/a: no ring proof or hypotheses. |
| 2.13 wlog | n/a: no case branches. |
| 2.14 calc term | n/a: direct term already, no calc. |
| 2.15 `<;>` | n/a: no tactic subgoals. |
| 3.1 erw | n/a: no rewriting. |
| 3.2 fun_prop replacement | n/a: no legacy analytic tactic. |
| 3.3 omega→lia | n/a: no arithmetic tactic. |
| 3.4 rcases rfl | n/a: no case analysis. |
| 3.5 automation attributes | n/a: no new theorem to register; changing public normal forms is not required for this definition. |
| 3.6 simp_all | n/a: no proof block. |
| 3.7 maxHeartbeats | n/a: target has no limit override. |

## Step 4 — reflection and construction probes

The existing direct `aeval` term is shorter and clearer than manufacturing the data via
tactic automation. Thus `exact?`/`apply?` proof search is inapplicable: there is no theorem
goal and an arbitrary polynomial inhabitant would not preserve the defined diagonal map.
No have-block composition, redundant goal changes, repeated branches or alternative proof
strategy exists. Both a constant-function representation and an `eval₂Hom` representation
were independently tested by `rfl`; they introduce additional syntax without improving
call sites. Retain the original construction and change only the lambda arrow.

## Source freeze and actual diff

Read live target immediately before context-anchored `apply_patch`; captured full file
baseline in `/private/tmp/roth-diag-before.lean`. Only source edit:

```diff
-noncomputable def diag (P : MvPolynomial σ ℤ) : Polynomial ℤ := aeval (fun _ => Polynomial.X) P
+noncomputable def diag (P : MvPolynomial σ ℤ) : Polynomial ℤ := aeval (fun _ ↦ Polynomial.X) P
```

SOURCE FROZEN, communicated to parent and explicitly acknowledged with ownership revoked:
whole-file SHA256 `af400c5f5c9179a854279959ce8050ed9f68d7acb5888ae7b2e5b52b736588d8`.
No subsequent source edits. Signature prefix comparison returned true; full-file equality
after reversing exactly this lambda-arrow normalization returned true. This checks that no
other declaration/docstring changed in this worker. Naming-pattern and unsafe-token scans
returned false/empty; no `sorry`, `axiom`, `admit`, suppression or limit option introduced.

## Step 5 — actual verification and gates

Module invocation: `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 93460,
exit 0; `Built Roth.CoeffNorm (18s)` and `Build completed successfully (1658 jobs)`.
Only known outside target warnings and dependency header warnings appeared.

Native whole-file `lean_diagnostic_messages` before and after edit and after module build:
`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`;
zero errors; six listed existing outside warnings; zero target warnings. No unavailable
LSP result was counted as pass. Native scratch retained stale-import informational text,
so independent fresh CLI verification was run after the actual build.

Fresh CLI verification file `/private/tmp/roth-diag-check.lean` checks exact original
public type via typed term, equality of full function to original lambda by `rfl`,
pointwise equality to original body by `rfl`, `eval₂Hom` equivalence by `rfl`,
`Function.const` equivalence by `rfl`, arbitrary CommSemiring candidate and specialization
by `rfl`, width100 `#check`, and `#print axioms Roth.diag`.
The initial CLI attempt exposed that a data-valued type-checking `example` must itself be
`noncomputable`; that scratch annotation was corrected. No source change resulted.
Final fresh CLI outcome is recorded in the completion addendum below.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | exact Roth.CoeffNorm command above, session 93460 exit 0. |
| definition_protected | ✓ pass | Routine authorized lambda delimiter normalization only; public signature/value/docstring unchanged. Full-function original-value rfl check, not a redesign. |
| theorem_statement_protected | ✓ pass | No theorem or lemma edited. |
| structure_gate | ✓ pass | One term; no conjunction or branches. |
| naming_gate | ✓ pass | Descriptive multi-letter data name; forbidden-pattern scan false. |
| line_packing_gate | ✓ pass | Complete one-row width table, 63 signature/94 full-line codepoints. |
| inequality_orientation_gate | ✓ pass | Full occurrence table and post-edit scan; zero reversed inequalities. |
| scope/docstrings | ✓ pass | Baseline comparison differs in exactly one ordinary-lambda arrow. |
| no sorry / standard axioms | ✓ pass | Target unsafe scan empty; axioms `[propext, Classical.choice, Quot.sound]`. |

Definition gate note: literal grep of the changed definition line can flag it; that
heuristic is discharged by the explicitly authorized routine notation change and the
independent original-value equality checks. No blanket exception for definition redesign
was used. Overall: pass, with no rename/decomposition deferral.

## Result and required phase checklist

Before: 1 code line (+2 docstring lines). After: 1 code line (+same 2 docstring lines).
Saved: 0 lines, 1 codepoint. Audit issues found: 1; fixed: 1. Rule applied: FORMAT ordinary
lambda arrow; all 42 golf rules considered above. Renames queued: none.
Comments preserved: 2 of 2 docstring lines, no inline proof comments present.
Refactoring needed: none in authorized scope.

- [✓] Step 1 — full required references read.
- [✓] Step 2 — full 24-item audit printed.
- [✓] Step 2.5 — five-method search-status block printed.
- [✓] Step 2.6 — every parameter, catalogue candidates, probes and public literature recorded.
- [✓] Step 2.7 — full per-signature-line codepoint table and actual width100 #check.
- [✓] Step 2.8 — full inequality occurrence table and post-edit scan.
- [✓] Step 3 — all 42 golfing rules have individual status/reason.
- [✓] Step 4 — construction alternatives and step-back reflection done.
- [✓] Step 5a — complete final native file diagnostics, zero errors/target warnings.
- [✓] Step 5b — actual module build and all diff gates recorded.
- [✓] Step 6a — no renames needed; no shared sidecar changed.

## Completion addendum — fresh compiler and freeze recheck

`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-diag-check.lean`, corrected
session 56394, exited **0**. All six exact-type/original-value/construction checks and
the universe-polymorphic coefficient candidate passed; no errors or warnings.
Actual output included:

```text
@Roth.diag : {σ : Type u_1} → MvPolynomial σ ℤ → Polynomial ℤ
'Roth.diag' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Separate fresh CLI drop-probe session 84109 exited **1**, as intended, with exactly
`Unknown identifier P` and `Unknown identifier τ` (τ is the deliberately unbound
variable-domain placeholder in that second probe). This independently confirms both
native binder-drop failures without relying on stale native imports.
The successful session has no stale-import diagnostic.

Final whole-file SHA256 recheck:
`af400c5f5c9179a854279959ce8050ed9f68d7acb5888ae7b2e5b52b736588d8`.
Source freeze remains intact. Overall final gates: **pass**.
