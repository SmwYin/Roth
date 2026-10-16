# Phase 4: `Roth.genWronskian`

Scope: only declaration originally L27–29/current L28–30 and this report. Start snapshot:
`/private/tmp/roth-genWronskian-worker-start.lean`. Both skills and complete supplied Phase-4
contract read; golfing-rules, proof-patterns, mathlib-search, generalisation-patterns,
cleanup-gates read in full, naming-conventions and mathlib-review-stages read in full,
and relevant style-rules sections read. Existing documentation, visibility and value protected.

## Initial 24-item audit (before source edit)

1. LINT: zero target warnings; complete diagnostics gives five warnings elsewhere (see verification).
2. HAVE SCAN: n/a, no `have` in this direct data definition.
3. SET_OPTION: none in declaration.
4. SIMP SQUEEZE: n/a, no simp calls.
5. NAMING: `genWronskian` is lowerCamelCase, names the generalized Wronskian and matches its public
   API (`genWronskian_eq_zero_of_not_linearIndependent`, `exists_genWronskian_ne_zero`). No forbidden
   patterns or abbreviations; no rename justified.
6. LINE PACKING: L28 has86 codepoints, next return-type chunk `MvPolynomial σ K :=` has19;
   86+1+19=106>100. L29 has23 codepoints and ends signature. Three lines already justified.
7. BY PLACEMENT: n/a, term-mode data construction.
8. FORMAT: replace ordinary lambda `=>` with `↦`; remove redundant parentheses around arrow codomain
   `σ →₀ ℕ`. Keep two-space body/four-space signature continuation; no blank internal lines.
9. COMMENTS: no inline comments; preserve original two-line docstring unchanged.
10. DOCSTRING: public mathematical definition documented, formula and exact source location supplied.
11. VISIBILITY: public reusable object, used in Roth.Separation and two local theorem families.
12. STRUCTURE: one expression, three declaration lines, no conjunction or branches; no helper needed.
13. MATHLIB: perform all five searches; specialized two-polynomial univariate Wronskian differs.
14. JUNK DEF: KEEP, names source's mathematical object, nonvanishing/vanishing API and downstream
    Separation users; not a disposable one-proof wrapper.
15. EXISTS LEMMA: n/a, data definition.
16. SHOW vs CHANGE: n/a, no show.
17. PUSH_NEG: n/a, none.
18. GENERALISE: inspect every explicit/implicit parameter; separately compile CommRing candidate,
    preserve production Field signature pending fileowner review. Fintype σ does not occur in the
    elaborated definition's signature; Lean automatically omits it, so no drop edit required.
19. INEQUALITY: zero reversed inequalities in signature (table below).
20. NORMAL-FORM: determinant of Hasse derivative matrix is the standard construction; no equivalence
    lemma or alternative predicate required.
21. SYNTAX-GEN: existing D/φ function arguments directly serve downstream determinant rewriting.
    Arbitrary finite family or arbitrary linear operators would be a public restatement.
22. IMPORT-FANOUT: n/a, no new imports.
23. CASTS: zero dropped / zero cross-type / zero load-bearing ascriptions in diff; binder types
    are required declarations, not expression casts.
24. INSTANCE-NAME: n/a, no instance declaration.

Issues to fix: (1) ordinary lambda arrow; (2) redundant arrow-codomain parentheses.
Refactoring candidate requiring review: CommRing coefficient weakening, separate compiled proposal.

## Mathlib search-status: `genWronskian`

[A] Lean-Finder: `generalized Wronskian determinant multivariate Hasse derivatives`.
Top3: `Polynomial.wronskian`, `Polynomial.wronskianBilin`, `Polynomial.sylvesterDeriv`.
These concern univariate pairs or a resultant matrix, not arbitrary Hasse multi-indices.
[B] Loogle: `"wronskian"`. Top3: `Polynomial.wronskian`,
`Polynomial.wronskian_self_eq_zero`, `Polynomial.wronskian_neg_eq`.
Auxiliary shape query `Matrix.det, Matrix (Fin _) (Fin _) _ → _`: top3
`Matrix.det_fin_zero`, `Matrix.det_fin_one`, `Matrix.det_succ_column_zero`.
[C] LeanSearch: same natural-language query as A. Top3: `Polynomial.wronskian`,
`IsCoprime.wronskian_eq_zero_iff`, `Polynomial.wronskian_add_left`.
[D] Untruncated source rg: `generalized.?wronskian|genWronskian|wronskian|hasseDeriv` in
LinearAlgebra, RingTheory/Polynomial and Algebra/MvPolynomial; full-name search
`genWronskian|generalWronskian|generalizedWronskian` across Mathlib has no textual matches.
The existing Wronskian module explicitly lists n-tuple Wronskians as future work (L29).
[E] `lean_local_search`: `wronskian`, `genWronskian`, `wronskianBilin`; positive matches
include local generalized API and Mathlib univariate API. Index reported unavailable initially,
then warming on repeated requests; **empty indexed results are not used as absence evidence**.
Auxiliary variants: `_self_eq_zero`, `_neg_eq`, `_eq_zero_iff`, `_add_left`,
`wronskianBilin_apply`, `det_fin_zero`, `det_fin_one`, `det_succ_column_zero`.
Common-equivalents lookup: no matching topology/finite/bornology bucket.
Concluded: partial match `Matrix.det`; retain local named generalized-Wronskian object built on
that API. The two-polynomial `Polynomial.wronskian` has a different type. No claim of absolute
absence from generic/auto-generated APIs is needed for this existing data definition. No wrapper
lemma added, no custom predicate, no replacement/bridge, no extra imports/docs mutation.

## Generalisation status: `genWronskian`

| # | Parameter | Class | Used as | Candidates / verification | Result |
|---|---|---|---|---|---|
| 1 | `{K : Type*}` | type variable | coefficient type in φ/result | drop would unbind K; already universe polymorphic | retain; no narrower universe restriction |
| 2 | `[Field K]` | typeclass | supplies commutative ring for determinant/Hasse derivative | drop, DivisionRing rejected; CommRing compiles separately | optional CommRing extension closed under API preservation; Field retained |
| 3 | `{σ : Type*}` | type variable | multi-index and polynomial variables | drop would unbind σ; already universe polymorphic | retain |
| 4 | section `[Fintype σ]` | typeclass | unused by this definition | compiled candidate without it, `#check` actual type has none | already automatically omitted; no source/API change |
| 5 | `{l : ℕ}` | structure value | common finite row/column size | drop would unbind l; arbitrary finite index restates public API | retain; zero dimension already allowed |
| 6 | `D : Fin l → σ →₀ ℕ` | structure value | Hasse derivative orders | drop leaves D unbound; arbitrary linear operators would restate object/API | retain; no bounds to weaken |
| 7 | `φ : Fin l → MvPolynomial σ K` | structure value | columns of derivative matrix | drop leaves φ unbound; replacement modules would change object | retain |

No proposition, strict inequality, continuity/global pointwise condition, decidability parameter,
bijectivity or bundled conjunction to weaken. No extra universe equality exists. Inversion check:
n/a, direct data definition has no proof after an unfolding that could reveal an abstract theorem.
A CommRing construction and specialization by rfl compiled separately in
`/private/tmp/roth-genWronskian-candidate.lean` (session24008, exit0). The file owner reviewed the
proposal and explicitly closed it as optional under public-API preservation; no pending action.
LSP standalone snippet initially rejected an out-of-date import; after a module build, that
native snippet still reported stale imports, so the isolated proposal used `lake env lean`.
Production-file diagnostics work completely and are recorded below.

## Literature search status

[A] WebSearch query1: `generalized Wronskian Hasse derivatives commutative ring generalization`.
Top3 returned hits:
1. Cas Burton, *A basis theorem for rings with commuting operators in characteristic zero*,
   https://doi.org/10.1016/j.jalgebra.2025.10.039 — general Hasse–Schmidt operators; not a
   direct generalized-Wronskian definition replacement.
2. *Fast Multivariate Multipoint Evaluation over All Finite Fields*, §3.2,
   https://doi.org/10.1145/3652025 — primary source defines multivariate Hasse derivatives over
   commutative rings; supports coefficient-ring extension of the construction.
3. *The Wronskian and its derivatives*,
   https://www.researchgate.net/publication/290016771_The_Wronskian_and_its_derivatives —
   secondary hosting search hit; not used as authoritative evidence.
Query2: `Wronskian generalized multivariate derivatives definition`, restricted to
arxiv.org/ncatlab.org/en.wikipedia.org. Top3: [Wronskian](https://en.wikipedia.org/wiki/Wronskian),
[Wronskiano](https://it.wikipedia.org/wiki/Wronskiano),
[Abel's identity](https://en.wikipedia.org/wiki/Abel%27s_identity).
Canonical-form search locates the multivariate determinant with constant-coefficient differential
operators. The authoritative project source clean.tex §2 L206–210 defines the same determinant;
our definition picks Hasse operators and places order bounds in the existence theorem.
No extra characteristic-zero or positive-dimension assumptions are needed just to define it.
[B] ChatGPT math MCP: n/a, no matching callable tool in ALL_TOOLS metadata discovery.
Literature-driven candidate: CommRing extension, separately compiled and closed as optional by
fileowner; no production restatement. Arbitrary differential operators/family indexing are
broader API designs, not necessary to this cleanup.

## Line packing — final

Reference: `#check @Roth.genWronskian` at `format.width 100`:
```
@Roth.genWronskian : {K : Type u_1} →
  [inst : Field K] → {σ : Type u_2} → {l : ℕ} → (Fin l → σ →₀ ℕ) → (Fin l → MvPolynomial σ K) → MvPolynomial σ K
```
(The function-type pretty-printer's unbroken tail is not a source width waiver.)

| Sig line | Chars | Next signature token | Arithmetic | Action |
|---|---:|---|---|---|
| 28 | 84 | `MvPolynomial σ K :=` (19) | 84+1+19=104>100 | ok |
| 29 | 23 | none; body next | n/a | ok |

Widths are measured codepoints including indentation. Removing codomain parentheses saved2
characters, insufficient to fit the whole return type on L28. Body L30 has50 characters.

## Inequality scan

| # | Location | Original | Rewrite | Lemma rename? |
|---|---|---|---|---|
| — | complete signature/hypotheses | n/a, no ≥ or > | none | none; no _ge_/_gt_ in name |

## Golfing-rule pass (42/42)

- [1.1] n/a: direct term, no by exact.
- [1.2] n/a: no by rfl wrapper.
- [1.3] n/a: no rw/exact.
- [1.4] n/a: no simp/exact.
- [1.5] n/a: no simp/rfl.
- [1.6] n/a: no constructors.
- [1.7] n/a: no apply/exact.
- [1.8] n/a: no contradiction proof.
- [1.9] considered: ν occurs inside φ before hasseDeriv application; ordinary eta reduction
  does not remove it without introducing function composition. Current matrix expression clearer.
- [1.10] n/a: no have.
- [1.11] n/a: no apply/intro.
- [1.12] n/a: no show.
- [1.13] n/a: no projection destructuring.
- [1.14] n/a: no rw.
- [1.15] n/a: no simp only.
- [1.16] n/a: no simp.
- [1.17] already `.det`; keep explicit `Matrix.of` to express matrix construction.
- [1.18] n/a: parentheses delimit receiver before `.det`; `<|` cannot replace that grouping.
- [1.19] n/a: no push_neg.
- [1.20] n/a: not an existential lemma.
- [2.1] n/a: data construction, no proposition/proof for grind.
- [2.2] n/a: no grind tactics.
- [2.3] n/a: no simplification proof.
- [2.4] n/a: no function-property goal.
- [2.5] n/a: no positivity goal.
- [2.6] n/a: no inequalities.
- [2.7] n/a: no arithmetic goal.
- [2.8] n/a: data definition, no aesop proof goal.
- [2.9] n/a: no numerical/cast goal.
- [2.10] n/a: data construction, no decidable proposition.
- [2.11] n/a: no algebraic equality proof/denominators.
- [2.12] n/a: no ring-ending proof or hypotheses.
- [2.13] n/a: no symmetric case split.
- [2.14] n/a: no calc.
- [2.15] n/a: no subgoals.
- [3.1] n/a: no erw.
- [3.2] n/a: no continuity/measurability tactics.
- [3.3] n/a: no omega.
- [3.4] n/a: no rcases.
- [3.5] n/a: definition, no new theorem attributes needed; existing API retained.
- [3.6] n/a: no simp_all.
- [3.7] n/a: no heartbeat/recursion options.

Applied syntax normalization: ordinary lambda arrow to ↦; redundant codomain parentheses removed.
No applicable proof-automation attempt was omitted: this is a data term, not a tactic proof.

## Step-back reflection

Term-mode construction already expresses the mathematics directly. Proof tactics exact?/apply?
would have to synthesize a polynomial rather than prove the intended equality, so they are not
sound replacements for this data definition. The independent value test below supplies its own
Matrix.det construction and checks equality by kernel reduction. No have-blocks, extraction
signals or different proof strategy remain. Retain the named mathematical object and existing API.

## Verification and gates

Post-edit complete `lean_diagnostic_messages`: success=true, partial=false, timed_out=false,
failed_dependencies=[], zero errors, zero target warnings. Full raw result including all warnings:
`/private/tmp/roth-genWronskian-post-lsp.json`.

All five preserved file warnings:

1. L1: `* -/: Copyright too short!` (missing authoritative metadata).
2. L36: automatically included section variable `[Fintype σ]` unused in
   `Roth.genWronskian_eq_zero_of_not_linearIndependent`.
3. L32: same theorem does not use `[Fintype σ]` (#4) in its type.
4. L242: `det_sum_rows` does not use `[DecidableEq ι]` (#5) in its type.
5. L260: `exists_genWronskian_ne_zero` does not use `[Fintype σ]` (#4) in its type.

No metadata invented; no linter suppression added. These warnings lie outside the owned declaration.

Post-edit command `/Users/ramin/.elan/bin/lake build Roth.GenWronskian`, session74305, exit0,
1838 jobs, target compiled in24s. No full-project build run by this declaration worker.

`/private/tmp/roth-genWronskian-verify.lean`, command
`/Users/ramin/.elan/bin/lake env lean /private/tmp/roth-genWronskian-verify.lean`, session76861,
exit0: original function type checked with no Fintype σ; original expression equality by rfl;
independently constructed Matrix.det/function value agrees by rfl. Initial scratch attempt lacked
`noncomputable` on a data-valued example and was corrected only in scratch before final exit0.
Both production definition and independent equality depend on exactly
`[propext, Classical.choice, Quot.sound]`. Native `lean_verify` independently returns trust=standard,
non_standard_axioms=[], warnings=[]. No sorry, new axiom, native_decide, options/version changes.

Rejected isolated candidates: `/private/tmp/roth-genWronskian-rejected.lean`, session79109,
exit1 as expected. `[DivisionRing R]` and no coefficient class both fail `CommSemiring R`
instance synthesis on the polynomial binder. CommRing candidate succeeded separately (session24008).
These probes never modified the production declaration's assumptions.

Worker-only diff captured against start snapshot at
`/private/tmp/roth-genWronskian-worker.diff`: precisely two removed/two added lines in target;
no neighboring declarations/docstrings/comments touched, no new helper.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | module build session74305 exit0 |
| definition_protected | pass | authorized equivalent parentheses/arrow syntax only; original type and value rfl verified |
| theorem_statement_protected | pass | no theorem changed |
| structure_gate | pass | one-expression body, three declaration lines, no ∧ or branch |
| naming_gate | pass | meaningful lowerCamelCase public generalized-Wronskian name, no forbidden pattern |
| line_packing_gate | pass | two signature rows above; 84+1+19=104>100 |
| inequality_orientation_gate | pass | complete scan table; zero ≥/> |

Overall: pass. Full-project build, separate LeanEval and publication belong to fileowner.

## Result

Before:3 lines. After:3 lines. Saved:0 lines. Audit issues found:2; fixed:2.
Refactoring deferred:0. Optional CommRing extension reviewed and closed under API preservation.
Rules applied: syntax/format audit item8; dot notation rule1.17 already satisfied.
Renames queued:none. Comments preserved: original2-line docstring unchanged; no inline comments.
Refactoring needed:none. Source-freeze ready.

## Phase checklist

- [✓] Step1 — mandatory references read.
- [✓] Step2 — all24 audit items printed before edit.
- [✓] Step2.5 — five-method mathlib search status with actual hits/index caveat.
- [✓] Step2.6 — every parameter and public literature reviewed; candidate compiled/reviewed.
- [✓] Step2.7 — measured every signature line at width100.
- [✓] Step2.8 — complete inequality scan table.
- [✓] Step3 — all42 golfing rules have statuses/reasons.
- [✓] Step4 — step-back reflection completed for direct data construction.
- [✓] Step5a — complete successful production-file LSP diagnostics.
- [✓] Step5b — diff gate table, module/type/value/axiom evidence recorded.
- [✓] Step6a — no renames needed, no sidecar mutation.
