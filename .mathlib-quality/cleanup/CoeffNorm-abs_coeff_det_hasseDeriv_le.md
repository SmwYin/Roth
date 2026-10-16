# Phase 4 — Roth.abs_coeff_det_hasseDeriv_le

Current amendment: the user explicitly approved the unused public-binder removals on
2026-10-16. See [approved amendment audit](CoeffNorm-api-amendment.md) for the current
source, types, warning count and verification. The original audit below records its
historical checkpoint and remains unchanged.

Dedicated declaration 26 audit. Baseline: `/private/tmp/roth-coeffnorm-original.lean`
L299–318; worker-start snapshot `/private/tmp/roth-d26-start.lean` L254–273;
final source `Roth/CoeffNorm.lean` L254–268.
Before: 20 declaration lines, **14 proof lines after `:= by`**, 15 including that boundary.
After: 15 declaration lines, **10 proof lines after `:= by`**, 11 including that boundary.
Saved: 5 declaration lines / 4 proof lines. The earlier estimate of 13 proof lines was
incorrect; these counts were measured from the actual source.

SOURCE FROZEN whole-file SHA256:
`6bd90da3a6a467e166523e006f4911384e2d3ffd7c277b40d8a660c39d9aa738`.
After the first freeze, the fileowner briefly restored source ownership solely to
correct the measured signature packing. The fileowner explicitly revoked ownership again
at the final hash above. Subsequent work is report/probes only. Public types, parameter order/explicitness, decidability parameters,
mathematics, documentation, comments, imports, header and pinned versions are preserved.
No new helper, instance, rename, Git operation, full-project build or LeanEval by this worker.

## Step 1 — references and proof

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also consulted both mandatory skills,
the relevant cleanup and cleanup-all instructions, the full Phase-4 worker contract,
relevant style/naming rules and mathlib-review-stages normal forms, syntactic generality
and documentation guidance. Combined reads which truncated were followed by segmented
reads of the pertinent contract/reference material.

The support of P lies in the degree box, whose cardinality is at most the product of
r_j+1. Thus normOne(P) is at most that product times B. Every Hasse derivative has norm
at most 2^(sum r_j) times this bound. Bound a determinant by l! times the l-th power of
the entry bound, then bound each coefficient by normOne. This is the source Lemma 3
argument in `.mathlib-quality/references/clean.tex` L438 onward. The existing theorem
already allows arbitrary multi-indices E, beyond the source's special derivative matrix.

Fresh native baseline and final LSP both fully elaborated the file: `partial=false`,
`success=true`, `timed_out=false`, no failed dependencies, zero errors, six inherited
warnings. The target warning is unused-in-type `[DecidableEq σ]`; its removal is part
of the unapproved API proposal, so the binder remains. The other warnings are the
user-preserved header, three other DecidableEq binders and normOne_det_le's hC.

## Step 2 — all 24 audit items

1. LINT: only the protected DecidableEq warning on this theorem. One transient long-line
   warning caused by inlining was fixed by wrapping the expression; no new final warning.
2. HAVE SCAN: original hN0 has `by positivity`, one use in hC0; original hsupp has a
   nontrivial `by exact_mod_cast`, one use in hentry; original hC0 has no by, one use in
   normOne_det_le; original hentry is a proof term, no by, one use in normOne_det_le.
   Inline hC0 by positivity and hentry at its call site, making hN0 unnecessary. Keep
   hsupp's meaningful cardinality cast proof. Final sole have is hsupp, used once.
3. SET_OPTION: n/a — no per-declaration options or raised elaboration limits.
4. SIMP SQUEEZE: n/a — no simp in accepted proof; terminal algebraic identity uses ring.
5. NAMING: abs_coeff_det_hasseDeriv_le describes exactly the coefficient absolute-value
   upper bound and preserves standard operation spelling. No forbidden abbreviation,
   numbered scheme, single-letter name, `_ge_`, `_gt_` or numbered auxiliary suffix.
6. LINE PACKING: measured every signature line below. Repacked hP onto the preceding parameter line and d onto the B/hB line, using
   exact codepoint arithmetic. All final lines at most 100 codepoints.
7. BY PLACEMENT: `:= by` ends the signature's last line; final `by ring` is term syntax.
8. FORMAT: two-space proof indentation, four-space signature continuation, no blank
   proof lines/trailing space/haveI/letI. Ordinary lambda arrows changed to ↦. Removed
   the semicolon tactic pair `rw [pow_mul]; ring` because ring alone closes.
9. COMMENTS: no proof comments existed; none removed. Docstring byte-preserved.
10. DOCSTRING: existing source-specific Lemma 3 documentation retained under the user's
    explicit documentation preservation instruction; it explains the arbitrary-index scope.
11. VISIBILITY: headline public API retained. No new private implementation declaration.
12. STRUCTURE: 10 proof lines after boundary (11 including it), no conjunction/case split,
    no branch over 10 lines. Below the strict headline target of 15. No helper required.
13. MATHLIB: all five actual methods recorded below; only partial determinant/Hasse
    matches. Existing local normOne/box API supplies the missing coefficient estimates.
14. JUNK DEF: n/a — theorem, no data definition introduced/changed.
15. EXISTS LEMMA: n/a — no existential statement or witness helper.
16. SHOW vs CHANGE: n/a — no show/change command in the accepted proof.
17. PUSH_NEG: n/a — no negation-normalisation tactic.
18. GENERALISE: every parameter considered below; public parameters remain exactly as
    before. Removing DecidableEq is already an unapproved proposal. Further optional
    redesigns are analysis only, closed without source action under API preservation.
19. INEQUALITY: all occurrences use ≤, with no reversed inequality or name; table below.
20. NORMAL-FORM: standard Matrix.det, MvPolynomial.coeff, Hasse derivatives, finite
    products/sums, real absolute value and ≤; no competing equivalence wrapper needed.
21. SYNTAX-GEN: arbitrary E and global degree/coefficient bounds are directly reusable
    by Roth callers. Bundling a coefficient norm hypothesis changes the API without an
    identified caller benefit; no restatement applied.
22. IMPORT-FANOUT: n/a — no imports added or changed.
23. CASTS: no cast removed by this diff. Real casts in hsupp and the product bound are
    genuine Nat→Real coercions (three textual occurrences in added/replaced lines).
    Coefficient integer ascriptions and the Fin l matrix-index annotation are preserved
    inside the moved conclusion, not newly introduced casts. No new redundant coercion.
24. INSTANCE-NAME: n/a — no instance declaration.

Issues fixed: single-use hC0/hentry, now-redundant hN0, redundant pow rewrite,
underpacked parameter/conclusion lines, ordinary lambda spelling. Refactoring needed: none
within approved scope; existing API proposal remains pending and untouched.

## Step 2.5 — five actual mathlib searches

| Method | Query | Actual result |
|---|---|---|
| A Lean-Finder | coefficient bound determinant matrix Hasse derivatives multivariate polynomial | Matrix.det_matrixOfPolynomials, Polynomial.coeff_det_X_add_C_card, Matrix.det_sum_smul_le; only partial matches |
| B Loogle | `MvPolynomial.hasseDeriv, _ ≤ _` | unknown identifier in remote index; retried with quoted name |
| B retry | `"hasseDeriv", _ ≤ _` | Polynomial.natDegree_hasseDeriv_le; degree bound, no coefficient/determinant estimate |
| C LeanSearch | bound coefficients determinant matrix Hasse derivatives polynomial | Polynomial.coeff_det_X_add_C_card, Matrix.det_le, Polynomial.hasseDeriv; partial matches |
| D source rg | full target name, normOne/det and coefficient/det inequality variants throughout Mathlib | no full-name match; only unrelated polynomial determinant coefficient API and norm/characteristic-polynomial uses |
| E local names | hasseDeriv; normOne_det_le | project's multivariate Hasse derivative API and Roth.normOne_det_le; univariate/Laurent mathlib APIs. Index reported warming, so empty-search absence is not asserted |

Auxiliary variants considered: determinant entry bound `Matrix.det_le` and
`Matrix.det_sum_smul_le`, univariate coefficient determinant identity, Hasse derivative
degree bound, normOne coefficient/product/determinant estimates. Common-equivalents
lookup: no discrete/finiteness/bornology concept in disguise. The generic determinant
absolute-value theorem is partial: coefficient extraction is not multiplicative and
normOne is submultiplicative, so a multiplicative AbsoluteValue is not a direct replacement.
The local headline composes several project-specific bounds and the finite support box;
it is not a duplicate of 1–3 mathlib calls. No wrapper deletion or new API extraction.
The live native `exact?` attempt failed; `apply?` offered only generic absolute-value
splittings/monotonicity and exhausted its search budget. No absence conclusion relies
solely on grep. No claim of exhaustive global nonexistence is made.

## Step 2.6 — every parameter and generalisation catalogue

All direct drop probes are isolated scratch files, not edits to the production theorem.
Dropping a data parameter still used in the conclusion can cause autoImplicit to recreate
it; such a result does not certify a weaker statement. No public change is kept.

| Parameter | Class / use | Mechanical candidates considered | Verification / result |
|---|---|---|---|
| σ : Type* | type variable in all polynomial/index types | drop; universe generalisation | already universe-polymorphic; drop cannot remove a type used by every datum |
| [Fintype σ] | typeclass for sum/product/box | drop; Finite σ plus locally chosen Fintype | drop probe; finite replacement needs restating the sums/products around a chosen enumeration, so public restatement rejected |
| [DecidableEq σ] | decidability needed by normOne_det_le call's API | drop plus classical | isolated reproof compiles; pending public API proposal, not applied |
| {l : ℕ} | size/index and exponent | drop; abstract finite matrix index | drop is not meaningful with Fin l in type; abstract index would restate factorial/power via cardinality, not routine weakening |
| E | arbitrary multi-index matrix | drop; restrict/point-localise | actual E used in target determinant; already arbitrary, no property to weaken |
| P | polynomial | drop; abstract coefficient ring | P appears in target and both bounds; general coefficient ring requires an absolute-value/norm API and changes public signature |
| {r} | degree bounds, product and sum | drop; localise to support | r occurs in conclusion; support-local forms require changing bounds/statement |
| hP | proposition bounding each variable degree | drop; point-localise | required by support box and normOne_hasseDeriv_le; all variables used in product/sum, no single-variable localisation preserves bound |
| {B : ℝ} | real bound and target factor | drop; ordered field | B occurs in conclusion; abstract field changes normOne API and statement |
| hB0 | weak nonnegativity proposition | drop; strict→weak | already weak; direct drop fails on referenced hB0, but derivable from hB at 0, independently compiled below; API preserved |
| hB | global coefficient bound | drop; support-local bound | direct drop fails; support-local bound needs a separate derivation to global bound; optional restatement closed without caller benefit |
| d | arbitrary coefficient index | drop; point-localise | d is the target coefficient, already pointwise; no assumption to weaken |

No algebra/analysis typeclass-parent candidate applies to a concrete integer/real theorem
without an actual abstract-ring restatement. No strict hypothesis to weaken, bundled
conjunction, continuity/measurability/locality hypothesis, or cross-universe restriction.
Inversion check: the proof uses genuine Hasse derivative estimates and finite degree-box
counting; generic matrix norm control is already factored as normOne_det_le. A second
abstraction layer would duplicate that local API and offers no needed caller benefit.

### Public literature search

Query 1: `Hasse derivatives polynomial height determinant coefficient bound Roth lemma`.
Top relevant results: ECCC TR2026-032 (general Hasse coefficient extraction), Bombieri–
Gubler *Heights in Diophantine Geometry* (secondary hosted scan), JACM *Fast Multivariate
Multipoint Evaluation over All Finite Fields*. No result was taken as evidence that this
specific real coefficient bound works over arbitrary rings.

Query 2: `Hasse derivative polynomial height determinant coefficient bound generalization Roth lemma 3`.
Top three returned hits, retained for audit:

1. [ECCC TR22-063](https://eccc.weizmann.ac.il/report/2022/063/), Bhargava–Ghosh–Guo–Kumar–Umans,
   *Fast Multivariate Multipoint Evaluation Over All Finite Fields*. Search excerpt gives
   Hasse coefficient extraction over general rings; opened primary abstract confirms the
   finite-field evaluation context. No ordered absolute-value coefficient bound there.
2. [Compositio Mathematica PDF](https://numdam.org/item/CM_1996__101_3_225_0.pdf), search
   excerpt on a generalisation of Roth's lemma. HTML opening timed out; no uninspected
   theorem/generalisation is claimed from it.
3. [JACM article](https://doi.org/10.1145/3652025), search excerpt defines multivariate
   Hasse derivatives by shifted coefficient extraction. DOI opening returned 403; same
   research topic has the accessible ECCC primary abstract above.

The canonical definition is algebraic and more general than integer coefficients, but
this theorem is an archimedean height estimate; abstract-ring generalisation needs a
norm/absolute-value hypothesis and is not inferred from the algebraic definition alone.
The source's exact degree/height bound is in local clean.tex, already represented by the
current stronger arbitrary-E formulation. ChatGPT math MCP: n/a, no matching callable
math connector discovered. No literature-driven mandatory change within approved scope.

## Step 2.7 — signature packing, codepoint widths

`#check @Roth.abs_coeff_det_hasseDeriv_le` was run under `set_option format.width 100` in
the compiled integrity probe; it confirms all original binders including both instances.
The pretty-printer lays out the dependent ∀/implication type rather than source binders.

| Sig line | Chars | Next complete syntactic token | Arithmetic | Action |
|---|---:|---|---|---|
| 254 | 71 | `(E : Fin l → Fin l → (σ →₀ ℕ))`, 30 | 71 + 1 + 30 = 102 > 100 | ok |
| 255 | 100 | `{B : ℝ}`, 7 | 100 + 1 + 7 = 108 > 100 | ok |
| 256 | 80 | complete absolute-value conclusion through ≤, 78 | 80 + 1 + 78 = 159 > 100 | ok |
| 257 | 82 | `(∏ j, ((r j : ℝ) + 1))`, 22 | 82 + 1 + 22 = 105 > 100 | ok |
| 258 | 83 | no next signature token; includes `:= by` | n/a | ok |

Initial signature line 2 had width 69 and next hP binder width 30, so 69+1+30=100:
that binder was moved up. The following B/hB/d line now has width 80. The first freeze
had incorrectly left this exact-fit case unpacked; the fileowner explicitly restored
ownership for the packing correction, then refroze the corrected source. All rows above
were remeasured; no repack or wide-hyp exception remains. Declaration remains five
signature lines and ten proof lines. All body lines also stay within 100 codepoints.

## Step 2.8 — inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | hP | degreeOf j P ≤ r j | none | none |
| 2 | hB0 | 0 ≤ B | none | none |
| 3 | hB | absolute coefficient ≤ B | none | none |
| 4 | conclusion | absolute determinant coefficient ≤ explicit bound | none | none |
| n/a | entire signature/hypotheses | zero ≥ and zero > | none | no _ge_/_gt_ name |

The final hsupp and calc body bounds also use ≤ exclusively.

## Step 3 — all 42 golfing rules

- [1.1] by exact wrapper: n/a — none.
- [1.2] by rfl: n/a — none.
- [1.3] rw + exact: n/a — no such chain.
- [1.4] simp + exact: n/a — none.
- [1.5] trailing rfl after simp: n/a — none.
- [1.6] constructor/exact pairs: n/a — no conjunction/structure construction.
- [1.7] apply + exact: n/a — direct lemma applications already used.
- [1.8] by_contra + push_neg: n/a — no contradiction branch.
- [1.9] eta reduction: n/a — lambdas depend nontrivially on indices, not `fun x ↦ f x`.
- [1.10] single-use haves: applied hC0 and hentry; hN0 becomes unnecessary; hsupp kept
  because it has a nontrivial proof block.
- [1.11] apply + intro: n/a — direct lambda already used.
- [1.12] redundant show: n/a — none.
- [1.13] have + projections: n/a — no product-valued intermediate.
- [1.14] consecutive rw: n/a — only a single original rw; removed it entirely.
- [1.15] terminal simp only: n/a — none.
- [1.16] nonterminal bare simp: n/a — none.
- [1.17] dot notation: already uses `.trans` and `.coeff` naturally.
- [1.18] `<|`: nested bound is the first argument of mul_le_mul_of_nonneg_left and has
  a following positivity argument, so removing its parentheses would change parsing.
- [1.19] push Not: n/a — no push_neg.
- [1.20] trivial existential helper: n/a — none.
- [2.1] whole-proof grind: actually tried in native multi_attempt; failed after abs cases.
- [2.2] delete before grind: n/a — no grind kept.
- [2.3] simpa consolidation: no simp/closing pair; explicit algebraic normalisation is ring.
- [2.4] fun_prop: n/a — no function-property goal.
- [2.5] positivity: applied directly at determinant's nonnegativity argument; subsumes
  both standalone hN0 and hC0 and keeps hB0 in its context.
- [2.6] gcongr: isolated complete alternate reproof compiled (exit 0) on entry-bound
  transport; it uses one more line than direct mul_le_mul_of_nonneg_left, so not kept.
- [2.7] lia/omega: n/a — no integer linear arithmetic goal; hsupp is a cast of a genuine
  combinatorial cardinal inequality, already discharged by exact_mod_cast.
- [2.8] whole-proof aesop: actually tried; failed, made no progress.
- [2.9] norm_num/norm_cast: exact_mod_cast already handles the necessary Nat/Real
  cardinal bound; no concrete numeric expression to evaluate.
- [2.10] decide/kernel: n/a — symbolic arbitrary polynomials/real B, not finite computation.
- [2.11] field_simp/ring: no denominators; ring alone actually tested and accepted on
  final equality, eliminating `rw [pow_mul]`.
- [2.12] linear_combination: actually tried at final equality; tactic unavailable under
  current imports. No import added for an identity ring already closes.
- [2.13] wlog: n/a — no symmetric branches.
- [2.14] collapse calc: three mathematical stages (coefficient, determinant bound,
  algebraic equality), so a two-step transitivity term would obscure the final rewrite.
- [2.15] `<;>` shared closing: n/a — no parallel subgoals with the same proof.
- [3.1] erw→rw: n/a — no erw.
- [3.2] legacy function-property tactics: n/a — none.
- [3.3] omega→lia: n/a — no omega introduced/present.
- [3.4] rcases/rfl substitution: n/a — no rcases.
- [3.5] automation attributes: no attribute required; headline inequality is not a simp
  rewrite or recurring automation normal form. Public attributes preserved.
- [3.6] simp_all: n/a — no simp_all only, and no closing local simplification chain.
- [3.7] remove maxHeartbeats: n/a — no raised limit before/after.

Additional actual whole-proof `simp` failed with no progress. `exact?` failed; `apply?`
only found partial absolute-value rewrites. Correct-column final-equality native tests:
ring succeeded; simp with pow_mul/mul_pow/commutativity left a power-commutation goal;
linear_combination was unavailable. Two earlier multi_attempt calls used a declaration
line/incorrect column and returned syntax errors; those are tooling positioning errors,
not counted as proof failures or successful proof evidence.

## Step 4 — reflection

The mathematical outline is already compact: count support, transport the coefficient
bound through Hasse derivatives, apply determinant norm control, normalize the bound.
Whole-proof generic automation cannot invent those project-specific estimates. Inlining
single-use proof terms avoids a second named entry-bound statement; hsupp remains the
single useful mathematical intermediate. No new helper or public API is necessary.

## Step 5 — verification and gates

Native full LSP: complete, zero errors, six inherited warnings, no new final warning.
`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm` exited 0 after the final source edits.
Build output reported Built Roth.CoeffNorm (20s); this is module wall time, **not** a
per-declaration profile. Final performance profiling is owned by the fileowner.

`/private/tmp/roth-d26-integrity.lean` imports the built module and contains:
(1) a fresh declaration with the **exact original signature**, assigned directly from
`@Roth.abs_coeff_det_hasseDeriv_le σ _ _ l E P r hP B hB0 hB d`; and (2) a second theorem
with that exact original signature and the new proof body, which never invokes the
original target. Both compiled with `lake env lean`, exit 0. `#print axioms` for the target,
exact-type assignment and nonself reproof each returned exactly
`[propext, Classical.choice, Quot.sound]`. No sorry/custom axiom or strengthened hypothesis.

| Gate | Status | Evidence |
|---|---|---|
| lake_build_file | pass | final `lake build Roth.CoeffNorm`, exit 0 |
| definition_protected | pass | diff contains no def/abbrev changes |
| theorem_statement_protected | pass | only packing/lambda spelling in signature; exact original type assignment compiled |
| structure_gate | pass | 10 proof lines, 11 including boundary; no conjunction or long branch |
| naming_gate | pass | descriptive name, no forbidden pattern, no rename |
| line_packing_gate | pass | all five final measured rows above are ok |
| inequality_orientation_gate | pass | zero reversed inequalities |

## Step 6 — result and checklist

Before 20→after 15 declaration lines; proof 14→10 (or boundary-inclusive 15→11).
Comments-preserved: no inline comments existed; docstring preserved byte-for-byte.
Renames-queued: none. Refactoring needed: none in approved scope. Existing public API
proposal is neither approved nor applied. Full project, separate LeanEval, commit/push,
and per-declaration performance profile belong to the fileowner.

- [✓] Step 1 reference documents consulted.
- [✓] Step 2 all 24 audit items.
- [✓] Step 2.5 five actual search methods with truthful service/index limitations.
- [✓] Step 2.6 all parameter/catalogue rows; actual isolated probes in addendum.
- [✓] Step 2.7 final width arithmetic, all five rows pass.
- [✓] Step 2.8 inequality scan table.
- [✓] Step 3 all 42 rule statuses.
- [✓] Step 4 mathematical reflection.
- [✓] Step 5a full native diagnostics, complete and no errors.
- [✓] Step 5b final diff gates pass; final packed-source module completion below.
- [✓] Step 6a no rename required.

## Isolated probe results and final-source confirmation

`/private/tmp/roth-d26-drops.json` records all direct drop experiments (each completed
without a timeout) against the unchanged proof, with classical added only for the
DecidableEq test:

| Removed textual binder | Exit | Interpretation |
|---|---:|---|
| Fintype | 1 | instance synthesis fails in sums/products |
| DecidableEq | 0 | classical supplies proof-local equality; existing API proposal only |
| l | 0 | autoImplicit recreates l from Fin l/exponents, not a mathematical parameter removal |
| E | 1 | unknown E / cannot infer its function type |
| P | 0 | autoImplicit recreates polynomial P from its uses; no real weakening |
| r | 1 | unknown r / cannot infer its function type |
| hP | 1 | unknown hP in support and derivative bounds |
| B | 0 | autoImplicit recreates real B; no real weakening |
| hB0 | 1 | unknown hB0 and positivity failure |
| hB | 1 | unknown hB in normOne_le_card_mul |
| d | 0 | autoImplicit recreates the coefficient index d; no real weakening |

`/private/tmp/roth-d26-without-hB0.lean` separately compiles the genuinely stronger
statement without hB0, proving `have hB0 : 0 ≤ B := (abs_nonneg _).trans (hB 0)` before
the accepted proof. Exit 0. This records that hB0 is mathematically redundant; it is
**not removed** because all public arguments are explicitly protected. No new action or
approval question is requested. `/private/tmp/roth-d26-gcongr.lean` also exits 0, but the
alternative is longer and adds no clarity over the direct monotonicity lemma.

The final source-only diff against the worker-start snapshot is confined to this
signature's packing/ordinary lambda spelling and this theorem's proof. It adds no
helpers, custom axioms, options, imports, docs or comments. Final whole-file hash is
rechecked after verification. Overall gates: pass, with protected inherited warnings
explicitly retained and optional public restatements closed without action.

Final packed-source verification completed: native full LSP again returned
`partial=false`, `timed_out=false`, `success=true`, no failed dependencies, zero errors
and exactly the six inherited protected warnings. Fresh module build session 70334
exited 0 (`Built Roth.CoeffNorm (20s)`). Fresh integrity probe session 3207 exited 0,
again confirming the exact original type assignment, nonself reproof, and standard
axioms for all three declarations. The signature packing did not affect either probe.
A final source comparison confirmed every byte outside this declaration unchanged
from the worker snapshot, no target sorry/admit/axiom, all target lines at most 100
codepoints, and unchanged SHA256
`6bd90da3a6a467e166523e006f4911384e2d3ffd7c277b40d8a660c39d9aa738`.
All 11 checklist entries and all seven declaration gates pass. No test/probe process
from this worker remains running. Per-declaration profiling remains the fileowner's
separate task; no invented theorem timing is reported here.
