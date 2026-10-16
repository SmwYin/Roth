# Phase 4: `Roth.normOne_add_le`

Scope: only `Roth/CoeffNorm.lean` L72–78 and this report. Starting context supplied by file owner: branch `ramin-cleanup`, HEAD `bbe0216`; full baseline build and separate `LeanEval` succeeded (session 9002); complete baseline LSP had no errors. No Git operations or shared-log edits performed.

Read in full: mathlib-quality/SKILL.md, lean4/SKILL.md, `/private/tmp/roth-coeffnorm-worker-contract.md`, and mathlib-quality references golfing-rules.md, proof-patterns.md, mathlib-search.md, generalisation-patterns.md, cleanup-gates.md, style-rules.md, naming-conventions.md. Also read mathlib-review-stages.md and local mathematical source `clean.tex` L442–458. Native Lean MCP was discovered using ALL_TOOLS metadata and worked; fallback not required.

## Audit (all 24 items)

1. LINT: no warning in target. Complete baseline/final LSP has six outside warnings: preserved header, four unused DecidableEq hypotheses, unused `hC`; none suppressed or changed.
2. HAVE SCAN: no `have` in the proof.
3. SET_OPTION: none; no heartbeat/recursion limit introduced.
4. SIMP SQUEEZE: one terminal `simpa using`; no nonterminal bare simp or terminal simp-only.
5. NAMING: `normOne_add_le` describes the triangle inequality for `normOne`; no forbidden abbreviation or numeric pattern. No rename.
6. LINE PACKING: single 95-codepoint signature line; measured table below. All code lines ≤100.
7. BY PLACEMENT: `by` stays at end of theorem line.
8. FORMAT: two-space tactic indent, four-space rewrite continuation, no internal blank lines; fixed sole lambda `=>` to `↦`. No haveI/letI.
9. COMMENTS: no proof comments present; existing two-line public docstring preserved byte for byte.
10. DOCSTRING: already identifies triangle inequality and the local source; retained under the existing-docstring protection policy.
11. VISIBILITY: public norm API consumed by `normOne_sum_le`; retained.
12. STRUCTURE: 6 proof-body lines, no conjunction/case branches; no extraction needed.
13. MATHLIB: all five methods executed; partial matches only, detailed below.
14. JUNK DEF: n/a, theorem, no data definition.
15. EXISTS LEMMA: n/a, no existential/private witness lemma.
16. SHOW vs CHANGE: n/a, neither appears.
17. PUSH_NEG: n/a, no negation tactic.
18. GENERALISE: all parameters audited and drop-probed below; no signature change.
19. INEQUALITY: statement uses ≤; zero ≥/>; table below.
20. NORMAL-FORM: already standard subadditivity form `f (P + Q) ≤ f P + f Q`. Generic norm/absolute-value forms require changing the custom norm API, not a syntactic normalization.
21. SYNTAX-GEN: OK, direct explicit P/Q arguments are convenient for downstream `Finset.le_sum_of_subadditive`.
22. IMPORT-FANOUT: n/a, no import changes.
23. CASTS: 0 dropped / 1 kept as cross-type and load-bearing (`P.coeff d : ℝ`); actual deletion probe picks integer absolute values and fails against the real goal. Q's cast is inferred.
24. INSTANCE-NAME: n/a, theorem introduces no instance.

Issues found: one lambda arrow style issue; fixed. Refactoring needed for this declaration: none. A broad norm redesign is a possible future project, not an identified cleanup defect or approved signature change.

## Mathlib search status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | triangle inequality sum absolute values of finitely supported functions | `AbsoluteValue.sum_le`, `IsAbsoluteValue.abv_sum`, `nat_abs_sum_le` |
| B Loogle | `Finset.sum, \|?a + ?b\| ≤ _` | unrelated `Real.abs_log_sub_add_sum_range_le`; no usable direct match |
| C LeanSearch | sum of norms of sum finitely supported functions is at most sum of norms | `MeasureTheory.eLpNorm'_sum_le`, `MeasureTheory.eLpNorm_sum_le`, `norm_sum_le` |
| D source rg | `sum_add_index`, `sum_le_sum_index`, `sum.*add.*le`, `normOne_add_le`, `sum_norm_add`, `sum_abs_add` | Finsupp sum-index equalities and monotonicity; no direct target duplicate |
| E local name | `sum_add_le` | subadditive hom and unrelated algebra results; index warming, so not evidence of absence |

Auxiliary variants examined: `Finsupp.sum_le_sum`, `sum_le_sum_index`, `sum_of_support_subset`, `sum_add_index'`, `sum_nonneg`, support union variants, generic norm-add/sum inequalities. Read relevant Finsupp Order source and `Analysis/Normed/Lp/Finsupp.lean`: the latter supplies WithLp metric structures with support-union triangle proofs, not a direct theorem about the local `normOne`. Common-equivalents table: no discrete/finite/bounded bucket applies.

Conclusion: partial mathlib matches; retain the project's norm API and its existing support-union proof using `Finset.sum_le_sum` and `abs_add_le`. No claim of exhaustive mathematical absence. Six replacement rules checked: no new wrapper, custom predicate, duplicate definition, import, or module-doc edit; exact?/apply? generic probes were executed, and no replacement theorem closed the target. Deleting the public declaration would violate the owner's explicit API preservation instruction.

## Generalisation status

| # | Parameter | Class | Used as | Mechanical candidates tried | Verified? | Result |
|---|---|---|---|---|---|---|
| 1 | `{σ : Type*}` | type variable | polynomial variable type | drop σ binder with autoImplicit=false; universe widening | yes for drop | drop fails `Unknown identifier σ`; Type* is already universe polymorphic, no universe restriction remains |
| 2 | `(P : MvPolynomial σ ℤ)` | structure value | LHS and first RHS summand/support | drop P binder with autoImplicit=false | yes | fails `Unknown identifier P`; retain |
| 3 | `(Q : MvPolynomial σ ℤ)` | structure value | LHS and second RHS summand/support | drop Q binder with autoImplicit=false | yes | fails `Unknown identifier Q`; retain |

No typeclass, decidability, proposition, point-local continuity, strict inequality, or bundled property parameter exists: the corresponding weakening catalogues have no applicable entry. Drop probes were isolated native `lean_run_code` examples; no public signature edited. Coefficients ℤ and values ℝ are fixed inside the protected definition of normOne; changing them requires a different API and is not mechanical hypothesis weakening.

Inversion check: after rewriting normOne onto a common finite support, only coefficientwise absolute-value subadditivity remains. The abstract result is already `Finset.sum_le_sum` plus `abs_add_le`; no missing abstract helper is needed. Big-change candidates requiring action: none.

## Public literature search

Query 1: `l1 norm triangle inequality finitely supported functions generalization`. Top three returned hits:

1. [Georgia Tech exercise sheet](https://www2.isye.gatech.edu/~msingh94/CS599/hw2.pdf): explicitly asks for L1 triangle inequality on functions.
2. [Various issues around the L1-norm distance](https://arxiv.org/abs/2110.04787): normalized probabilistic distances; not a direct improvement of this result.
3. [Triangle inequality](https://en.wikipedia.org/wiki/Triangle_inequality): general norm terminology; supplementary only.

Query 2: `site.edu l1 norm triangle inequality lecture notes`. Top three returned hits:

1. [ETSU, Norms](https://faculty.etsu.edu/gardnerr/Func/notes/2-2.pdf): ℓ1 satisfies triangle inequality.
2. [Illinois lecture overview](https://publish.illinois.edu/safe-autonomy/files/2019/01/Lecture1_Overview.pdf): norm triangle axiom.
3. [UT Austin appendices](https://users.ece.utexas.edu/~baldick/classes/380N/Appendices.pdf): L1 norm and triangle inequality.

Primary teaching sources support the standard coefficientwise sum argument. The local reference `clean.tex` L450–452 states the stronger scaled form `‖f + kg‖₁ ≤ ‖f‖₁ + |k|‖g‖₁`; the current theorem is its k=1 component. Inference: arbitrary finite coefficient families and normed coefficient groups admit the same argument; a public generalized definition would require a separate API design. ChatGPT math MCP: n/a, no such tool exposed in ALL_TOOLS.

## Candidate experiments

Native `lean_multi_attempt` at L73 (before any proof steps): `grind` failed; `simp [normOne]` left sum inequalities; `aesop` made no progress; `exact?` could not close; `apply?` produced only partial generic order refinements, not a proof. Hence no one-tactic replacement found.

At L78 after support rewrites:

- `gcongr; exact abs_add_le _ _`: failed with stuck AddLeftMono metavariables.
- `exact Finset.sum_le_sum fun d _ ↦ by simpa using abs_add_le (P.coeff d : ℝ) (Q.coeff d)`: no goals, no diagnostics; kept.
- Remove `: ℝ`: failed, resulting integer inequality mismatches real inequality; reverted candidate.
- `grind [MvPolynomial.coeff_add, Int.cast_add, abs_add_le]`: failed; also warned that coeff_add alias is deprecated; rejected.

An initial L79 attempt targeted the blank line and produced a parser error; reran all final-step candidates at the correct L78. This was a probe-position correction, not evidence against the tactics.

## Golfing-rule pass (42/42)

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: whole body has necessary support rewrites |
| 1.2 by rfl | n/a: no reflexivity wrapper |
| 1.3 rw + exact → rwa | n/a: exact term is a sumwise proof, not transported unchanged; existing rewrite block expresses shared support |
| 1.4 simp + exact → simpa | already final coefficientwise `simpa using` |
| 1.5 trailing rfl | n/a: none |
| 1.6 anonymous constructor | n/a: no conjunction |
| 1.7 apply + exact | n/a: direct exact already |
| 1.8 by_contra! | n/a: no contradiction proof |
| 1.9 lambda eta reduction | lambda uses d inside two coefficients and ignores membership, not eta-reducible; arrow normalized |
| 1.10 inline have | n/a: none |
| 1.11 refine + fun | n/a: no apply/intro sequence |
| 1.12 redundant show | n/a: none |
| 1.13 obtain | n/a: no projection pair |
| 1.14 merge rw | already one rw block |
| 1.15 unsqueeze terminal simp-only | n/a: no simp-only |
| 1.16 squeeze nonterminal simp | n/a: no nonterminal simp |
| 1.17 dot notation | n/a: no hypothesis/object receiver makes the existing theorem applications shorter |
| 1.18 use <\| | n/a: no trailing proof/lambda parentheses |
| 1.19 push Not | n/a: no push_neg |
| 1.20 inline existential helper | n/a: no existential |
| 2.1 grind | whole and final-step probes failed |
| 2.2 delete before grind | whole-proof grind tried, insufficient |
| 2.3 simpa consolidation | already used at coefficientwise closing step |
| 2.4 fun_prop | n/a: no analytic function-property goal |
| 2.5 positivity | n/a: goal compares two norms, not positivity |
| 2.6 gcongr | actual final-step probe failed; explicit sum_le_sum retained |
| 2.7 lia/omega | n/a: real absolute-value/support sums, no Nat/Int arithmetic goal |
| 2.8 aesop | actual whole-proof probe failed |
| 2.9 norm_num/norm_cast | n/a: no concrete numeral computation or pure cast goal |
| 2.10 decide | n/a: symbolic arbitrary polynomial inequality, not finite computation |
| 2.11 field_simp/ring | n/a: no rational identity or denominator |
| 2.12 linear_combination | n/a: no ring-ending proof or algebraic equality hypotheses |
| 2.13 wlog | n/a: no symmetric case branches |
| 2.14 calc collapse | n/a: no calc |
| 2.15 <;> | n/a: single sumwise goal; no repeated goals |
| 3.1 erw → rw | n/a: only rw already |
| 3.2 fun_prop | n/a: no continuity/measurability tactic |
| 3.3 omega → lia | n/a: no omega |
| 3.4 rcases rfl | n/a: no rcases |
| 3.5 automation attributes | no change: a subadditivity inequality should not be a simp rewrite; global tactic registration unneeded |
| 3.6 simp_all | n/a: no simp_all-only |
| 3.7 maxHeartbeats | n/a: none |

## Line packing

Actual native `#check @Roth.normOne_add_le` under `set_option format.width 100`:

```lean
@Roth.normOne_add_le : ∀ {σ : Type u_1} (P Q : MvPolynomial σ ℤ),
  Roth.normOne (P + Q) ≤ Roth.normOne P + Roth.normOne Q
```

(The MCP rendered the message on one line; line break above is display-only.)

| Signature line | Codepoints | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| L72, whole statement through `:= by` | 95 | none; proof starts next | n/a, no next signature line | ok |

Before/after identical signature. Proof line widths: 11, 51, 91, 92, 29, 89 after arrow normalization. The multiline rw has one argument per continuation because the preceding argument plus the next argument exceeds 100; no signature underpacking remains.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | signature L72 | one `≤`; no `≥` or `>` | n/a: already oriented | none |

No proposition parameters or typed inequality hypotheses. Final scan found zero forbidden inequality symbols.

## Step-back reflection

The support union is needed because cancellation may shrink support of P+Q. Rewriting all three norms onto the same finite set makes the scalar triangle inequality lift directly. Removing the real cast changes the elaborated scalar domain. Generic Finsupp norm routes add conversions/imports without simplifying this protected definition. The current six-line proof is compact, explicit, and uses existing sum APIs; no useful new helper or public restatement was identified.

## Frozen source and actual gates

SOURCE FROZEN target block SHA256 (including docstring and trailing blank line):
`bf7d98e77726dd4a63bc81cf462384cf7a824cebb93329f64dd5bbfc37456b8a`.

SOURCE FROZEN whole-file SHA256:
`1c67627438e2ed4ecec1e2024e1d517b23c235fc3b3f44d409394477fc5a818c`.

All source edits finished before these hashes; source ownership then explicitly revoked. Subsequent work only builds, probes, diagnostics, and report.

Diff against `/private/tmp/d07-add-before.txt`: exactly `fun d _ =>` → `fun d _ ↦`. Python comparison checked exact protected statement/docstring prefix, only authorized arrow replacement, no def/abbrev additions, no sorry/axiom/options, widths and body count.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 10663 exit 0, Built Roth.CoeffNorm (20s), 1658 jobs |
| definition_protected | ✓ pass | no definition touched; parsed target contains no def/abbrev |
| theorem_statement_protected | ✓ pass | prefix through `:= by` exactly equal before/after; original-type check below |
| structure_gate | ✓ pass | 6 proof-body lines, no conjunction/branch |
| naming_gate | ✓ pass | descriptive norm/add/le name, no forbidden pattern |
| line_packing_gate | ✓ pass | measured sole signature line 95; all target lines ≤100 |
| inequality_orientation_gate | ✓ pass | signature scan has zero ≥/> |
| diagnostic gate | ✓ pass | complete native final LSP after build, success=true, partial=false, timed_out=false, failed_dependencies=[]; zero errors, six pre-existing outside warnings |
| comments/docs preservation | ✓ pass | exact original docstring preserved; no proof comments existed |

Native final independent example re-proved the original statement using support union and scalar abs_add_le without calling normOne_add_le; succeeded. A second example assigned `@normOne_add_le` to its original quantified type; succeeded. Axiom print: `[propext, Classical.choice, Quot.sound]` only. Native imported probe emitted cached-import information, so fresh CLI verification was also run as required; first CLI raced the active build and failed because the olean was temporarily absent, then it was rerun after the successful module build. Final CLI result is recorded below.

## Result

Before: 7 declaration lines / 6 body lines. After: 7 / 6. Saved: 0 lines, one codepoint; one style fix. No theorem signature, instance, definition value, documentation, import or trust-basis change. Renames queued: none. Refactoring needed: none for target. Six file-level warnings remain in the owner's separately tracked scope.

- [✓] Step 1 — required reference docs read in full
- [✓] Step 2 — all 24 audit items reported
- [✓] Step 2.5 — all five mathlib search methods reported
- [✓] Step 2.6 — every parameter audited with actual applicable drop probes
- [✓] Step 2.7 — every signature line measured and packing table emitted
- [✓] Step 2.8 — inequality scan table emitted
- [✓] Step 3 — all 42 golfing rules considered with explicit statuses
- [✓] Step 4 — proof-strategy reflection completed
- [✓] Step 5a — complete final LSP has no errors or target warnings
- [✓] Step 5b — actual module build and all diff gates pass
- [✓] Step 6a — no renames needed; no shared sidecar modified

Fresh final CLI: `/Users/ramin/.elan/bin/lake env lean /private/tmp/d07-add-final.lean`, session 36739, exit 0. No warnings/errors. Output verifies original quantified type and axioms `[propext, Classical.choice, Quot.sound]`. The scratch proof independently uses sum/absolute-value primitives, not the target theorem; original-type assignment is a separate example.
