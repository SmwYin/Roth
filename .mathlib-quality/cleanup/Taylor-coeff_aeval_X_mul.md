# Phase 4: `MvPolynomial.coeff_aeval_X_mul`

Baseline: `0d5433c`, `Roth/Taylor.lean:57–80` (original inventory lines 59–82).
Result: 24 → 18 declaration lines; 20 → 14 proof-body lines; six lines saved.
The signature, visibility, imports, definitions, and all other declarations are unchanged.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also consulted both skills,
the full worker contract, relevant formatting/documentation/tactic sections of
style-rules.md, and naming-conventions.md. No comments or docstrings occur in this helper.

## Full audit

1. **LINT:** no target diagnostics. Complete file LSP has only the existing, user-preserved
   missing copyright-header warning at line 1.
2. **HAVE SCAN:** original `hA` (lines 62–65) has a genuine `by` proof, used once at line 69;
   replaced the expansion proof by direct `Polynomial.aeval_def`, `eval₂_eq_sum`, and
   `sum_def` rewrites. Original `herase` (66–68) has a genuine `by` proof, used once at 72;
   replaced by `tsub_eq_of_eq_add (Finsupp.erase_add_single i d).symm` at the use site.
   Original `hlt` (75) has no `by`, used once at 76; inlined its expression.
   No `have` remains.
3. **SET_OPTION:** none in original or result; no production options introduced.
4. **SIMP SQUEEZE:** original terminal `simp` calls for expansion, erasure, main summand,
   and absent-support summand were unsqueezed; retained terminal calls remain unsqueezed.
   The terminal `simpa` for the contradiction stays unsqueezed. Nonterminal `simp_rw`
   has explicit rewrite lemmas. No bare nonterminal `simp`, terminal `simp only`, or
   malformed simp list remains.
5. **NAMING:** `coeff_aeval_X_mul` describes the coefficient of the evaluated-polynomial
   product. It follows the `coeff_*` convention and uses the actual `aeval` and `X`
   API names. No forbidden abbreviations or numbered/scheme patterns occur.
   This is a standard mathematical coefficient identity, so the descriptive name is
   preferable to an opaque `_aux` suffix; no rename warranted or queued.
6. **LINE PACKING:** all four signature lines measured below; preserved exactly.
7. **BY PLACEMENT:** `:= by` remains at the end of the conclusion line. The nested
   contradiction lambda ends in `by`, never a separate bare `by` line.
8. **FORMAT:** two-space tactic indentation, properly focused branches, no empty proof
   lines, no semicolon chains, no `haveI`/`letI`. Ordinary lambda changed to `↦`.
   The evaluation rewrite list is packed within 100 codepoints.
9. **COMMENTS:** none present; no comment removed or relocated.
10. **DOCSTRING:** n/a: private helper has no docstring and does not need one.
11. **VISIBILITY:** private remains private; this internal convolution identity supports
    the file's monomial Taylor proof.
12. **STRUCTURE:** final body 14 lines; no conjunction in the conclusion; the largest
    branch is six lines. No extraction threshold remains. The argument expands the
    univariate factor, selects exponent `d i`, and proves other terms vanish using `hB`.
13. **MATHLIB:** five-method search below found useful building blocks, not a direct
    replacement of the full independent-variable product identity. Used the building
    blocks directly and removed the local expansion/erasure proofs.
14. **JUNK DEF:** n/a: theorem, no definition.
15. **EXISTS LEMMA:** n/a: equality theorem, no existential witness wrapper.
16. **SHOW vs CHANGE:** neither occurs.
17. **PUSH_NEG:** none.
18. **GENERALISE:** all parameters audited below; no statement changes. The commutative
    semiring hypothesis is already the structure required by the stated polynomial API.
19. **INEQUALITY:** no reversed inequality occurs in the signature. Original `hlt`
    uses `<` in the correct direction; final proof uses the same strict comparison
    through `.lt_of_ne`. See scan table below.
20. **NORMAL-FORM:** canonical coefficient identity, with evaluation/product on the left
    and product of coefficients on the right. No alternate normal form warranted.
21. **SYNTAX-GEN:** OK: the support condition directly expresses independence of variable
    `i` and matches the current caller. Replacing the polynomial construction or
    restating its independence hypothesis would change the contract without a current need.
22. **IMPORT-FANOUT:** n/a: no new imports.
23. **CASTS:** one redundant type annotation removed with `hA`; zero cross-type casts
    added. The original signature's `(X i : MvPolynomial σ R)` is preserved and fixes
    the evaluation target. No coercion juggling remains in the proof diff.
24. **INSTANCE-NAME:** n/a: this declaration is not an instance and introduces none.

Issues fixed: direct evaluation-sum reuse, direct erasure/cancellation reuse, inline
single-use `hlt`, and normalize its lambda arrow. Refactoring needed: none.

## Mathlib search status

| Method | Actual query / inspection | Result |
|---|---|---|
| A: Lean-Finder | multivariate polynomial coefficient product polynomial evaluated at X i independent of variable i | `MvPolynomial.coeff_X_mul'`, `coeff_mul_X'`, `coeff_X_mul`, `coeff_mul_X`, `eval₂_mul_monomial`; partial matches only |
| B: Loogle | `MvPolynomial.coeff, Polynomial.aeval`, then `"coeff", "aeval"` | First query rejected the identifier; corrected query returned `Polynomial.coeff_zero_eq_aeval_zero`, its primed version, and `MvPolynomial.aeval_eq_constantCoeff_of_vars`; none proves this product identity |
| C: LeanSearch | service availability inherited from parent: repeated HTTP 500 already established | Unavailable, not evidence of absence; per parent instruction no repeated retry |
| D: source search | `coeff_aeval_X_mul`, `coeff.*aeval`, `aeval.*coeff`, `single.*sub`, `sub.*single`, `erase.*sub`, `eval₂_eq_sum`, `sum_def` | No exact-name mathlib hit (untruncated full-name search); source exposes evaluation-sum and cancellation building blocks |
| E: name search | native `lean_local_search` for `coeff_aeval` | Returned only local helper; index `unavailable`, so no absence claim based on index |

Auxiliary variants checked: `coeff_X_mul`, `coeff_mul_X`, their primed versions,
`coeff_monomial_mul'`, `single_add_erase`, `erase_add_single`, and both operand orders
of subtraction cancellation. `#check` confirmed `Polynomial.aeval_def`,
`Polynomial.eval₂_eq_sum`, `Polynomial.sum_def`, `Finsupp.erase_add_single`,
`tsub_eq_of_eq_add`, and `MvPolynomial.coeff_monomial_mul'` with the actual imports.
Common-equivalents lookup: no listed topology/finiteness/separation/boundedness bucket applies.

Live pre-target `exact?` could not close the original goal. `apply?` offered only generic
graph-membership/inverse reformulations with unresolved obligations, not a proof.
Concluded: partial matches; retain this nontrivial coefficient convolution helper,
build directly on the verified mathlib expansion and cancellation API. No global
absence claim is made from unavailable search services. No new API extraction is
needed: the two local structural manipulations now use existing API directly.

## Generalisation status

| Parameter | Class | Role | Mechanical candidates / check | Result |
|---|---|---|---|---|
| `σ : Type*` | type variable | variable indices and finitely supported exponents | Already universe polymorphic; dropping loses the domain of `i`, `B`, and `d` | Keep; no smaller meaningful type parameter |
| `R : Type*` | type variable | coefficient type | Already universe polymorphic; dropping loses the coefficient parameter and instance target | Keep |
| `[CommSemiring R]` | typeclass | `MvPolynomial`, `Polynomial.aeval`, multiplication | Actually compiled `[Semiring R]` and no-instance probes | Both fail to synthesize `CommSemiring R`; no weakening applied |
| `i : σ` | structure value | evaluated variable and erased coordinate | Actual drop probe with `autoImplicit false` | Unknown `i` in statement; keep |
| `f : Polynomial R` | structure value | arbitrary univariate factor | Actual drop probe with `autoImplicit false` | Unknown `f` / `f.coeff`; keep |
| `B : MvPolynomial σ R` | structure value | factor independent of `i` | Actual drop probe with `autoImplicit false` | Unknown `B` / support / coefficient; keep |
| `hB : ∀ e ∈ B.support, e i = 0` | proposition | vanishing of nonsurviving summands | Actual drop probe | Proof fails at unknown `hB`; without independence the claimed identity is false (take both factors to be `X i`) |
| `d : σ →₀ ℕ` | structure value | coefficient index | Actual drop probe with `autoImplicit false` | Unknown `d` / `d.erase`; keep |

No decidability parameter exists; `classical` stays local to the proof. No topology,
analytic, strict positivity, bijectivity, or bundled-structure hypothesis exists to
weaken. Point-localisation is not a matching catalogue pattern for this algebraic
support condition; no speculative replacement condition added. The natural-number
exponents are part of the polynomial construction, not an arbitrary numeric parameter.
Inversion check: not applicable to a concrete named witness; `f`, `B`, and `d` are
arbitrary throughout, and variable independence is used in the central vanishing step.
Big-change candidates: none warranted. Literature: n/a, private declaration.

## Line packing

Reference, actual `#check @coeff_aeval_X_mul` with `format.width := 100`:

```lean
@coeff_aeval_X_mul : ∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (i : σ) (f : Polynomial R)
  (B : MvPolynomial σ R),
  (∀ e ∈ B.support, e i = 0) →
    ∀ (d : σ →₀ ℕ), ((Polynomial.aeval (X i)) f * B).coeff d = f.coeff (d i) * B.coeff (Finsupp.erase i d)
```

Before and after signature tables coincide; no repacking edit is needed. Continuation
units below are complete binders or equation sides including the proof introducer,
so the break preserves the readable equation rather than splitting an application.

| Sig line | Codepoints | Next signature unit | Arithmetic | Action |
|---|---:|---|---|---|
| 57 | 81 | `(hB : ∀ e ∈ B.support, e i = 0)` (31) | 81 + 1 + 31 = 113 > 100 | ok |
| 58 | 50 | left side through `=` (59) | 50 + 1 + 59 = 110 > 100 | ok |
| 59 | 63 | right side through `:= by` (41) | 63 + 1 + 41 = 105 > 100 | ok |
| 60 | 47 | proof body next | n/a | ok |

All final target lines are at most 100 Unicode codepoints.

## Inequality scan

| Occurrence | Location | Original | Action | Rename |
|---|---|---|---|---|
| none | all four signature lines / `hB` | no `≥` or `>` | none needed | no `_ge_` or `_gt_` in name |
| original local `hlt` | original line 75 | `m < d i` | correctly oriented; expression inlined | n/a |

No reversed inequalities in final signature, hypotheses, or proof.

## Golfing rule pass

| Rule | Status |
|---|---|
| 1.1 by exact wrapper | n/a: no whole-proof wrapper |
| 1.2 by rfl | n/a: no whole-proof `by rfl`; branch `rfl` is useful |
| 1.3 rw + exact | n/a: no consecutive rewrite/exact pair |
| 1.4 simp + exact | n/a: no such pair |
| 1.5 trailing rfl | n/a: no `rfl` following a closing simp |
| 1.6 anonymous constructor | n/a: equality, no constructor proof |
| 1.7 apply + exact | n/a: none |
| 1.8 by_contra + push_neg | n/a: neither tactic occurs |
| 1.9 eta reduction | n/a: contradiction lambda uses its argument nontrivially; normalized arrow to `↦` |
| 1.10 single-use have | applied: inlined `hlt`; removed `hA` and `herase` through direct API reuse |
| 1.11 apply + intro | n/a: no `apply` followed by `intro` |
| 1.12 redundant show | n/a: no `show` |
| 1.13 have + projections | n/a: no conjunction-valued intermediate fact |
| 1.14 merge rw | n/a: remaining `rw` calls separated by essential `simp_rw`; new first rewrite chain already merged |
| 1.15 terminal simp only | n/a: terminal simplifications already unsqueezed |
| 1.16 nonterminal simp | n/a: all `simp` calls close their goals; explicit `simp_rw` remains |
| 1.17 dot notation | used directly for `.symm`, `.lt_of_ne`, `.not_ge`; no further applicable replacement |
| 1.18 trailing parens | n/a: inner parentheses delimit method receivers/arguments; lambda already passed without parentheses |
| 1.19 push_neg | n/a: none |
| 1.20 trivial existential helper | n/a: not existential |
| 2.1 grind | tried live on whole proof; failed with unproved coefficient equality |
| 2.2 delete before grind | n/a: final proof contains no grind |
| 2.3 simpa consolidation | terminal contradiction already `simpa`; expansion and erasure blocks replaced by API |
| 2.4 fun_prop | n/a: no analytic/function regularity proposition |
| 2.5 positivity | n/a: no structural positivity goal; strict exponent comparison comes from two hypotheses |
| 2.6 gcongr | n/a: no monotonicity inequality goal |
| 2.7 lia / omega | tried an arithmetic contradiction variant in live multi-attempt; it did not produce a verified replacement because its preceding simp failed; retained short exact strict-order term |
| 2.8 aesop | tried live whole proof; exhaustive search failed, and its changed hypothesis normal form broke the remaining original tail |
| 2.9 norm_num / norm_cast | n/a: no concrete arithmetic or cast goal |
| 2.10 decide | n/a: arbitrary polynomials/semiring, not a closed decidable computation |
| 2.11 field_simp; ring | n/a: no division, field, or denominator |
| 2.12 linear_combination | n/a: no ring/ring_nf terminal block or linear-combination identity |
| 2.13 wlog | n/a: the vanishing and surviving cases are mathematically different |
| 2.14 calc collapse | n/a: no calc |
| 2.15 shared closing tactic | n/a: remaining sum obligations need different arguments; original shared extensionality closure was removed via API |
| 3.1 erw to rw | n/a: no erw |
| 3.2 continuity/measurability | n/a: none |
| 3.3 omega to lia | n/a: no omega retained or introduced |
| 3.4 rcases rfl | original equality split already substituted; entire erasure block eliminated |
| 3.5 automation attributes | n/a: private support-dependent identity; no stable global simp normal form added |
| 3.6 simp_all only | n/a: none |
| 3.7 remove limits | n/a: no heartbeat or recursion limit |

## Experiments and step-back review

Whole-proof `grind`, `simp`, `aesop`, and `exact?` did not close the target;
`apply?` supplied only unresolved generic transformations. Direct `simp` also did not
prove the erasure identity. `tsub_eq_of_eq_add` with `single_add_erase` had the wrong
addition order; `erase_add_single` gives exactly the needed equation.
An early live erasure probe targeted the enclosing `have` line rather than its body;
those failures were context errors, not evidence against the candidate. Retried at
the correct body line, then independently compiled the final full proof.
Live replacement tests leave an existing tail, so later `No goals to be solved`
messages were treated as provisional success only; final isolated and module builds
confirm the actual replacement without that tail.

The new proof expands evaluation directly, distributes multiplication and coefficient
extraction across the support sum, and retains the necessary single-summand argument.
This removes intermediate algebraic plumbing without inventing a new helper. A term-only
proof would still need the distinct sum obligations and would obscure this structure.
No redundant step remains in the verified argument, and no extra declaration is needed.

## Verification and diff gates

Final isolated compile: `lean_run_code` with original imports and only the pre-target
source prefix, followed by the entire replacement declaration, `#check` at width 100,
and `#print axioms`. Result `success: true`, `timed_out: false`; only informational
type/axiom output. Thus neither the compiled target nor any later declaration can
serve as a circular proof dependency. Axioms: `propext`, `Classical.choice`, `Quot.sound`.

Final live `lean_diagnostic_messages`: `success: true`, `partial: false`,
`timed_out: false`, `failed_dependencies: []`; only existing header warning.
Actual `/Users/ramin/.elan/bin/lake build Roth.Taylor` exited 0 (session 89624).
Log: `/private/tmp/roth-taylor-coeff_aeval_X_mul-build.log`.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | actual `lake build Roth.Taylor`, exit 0 |
| definition_protected | pass | no definitions/abbreviations touched |
| theorem_statement_protected | pass | signature compared byte-for-byte against worker snapshot; identical |
| structure_gate | pass | 14-line body, no conjunction, largest branch six lines |
| naming_gate | pass | mathematical snake_case/API name, no forbidden pattern; no rename |
| line_packing_gate | pass | complete four-row measured table; no overlong target line |
| inequality_orientation_gate | pass | complete scan; zero reversed code inequalities |
| comments/docstrings protected | pass | none in target; outside-source bytes unchanged |
| isolated/type/axiom gate | pass | pre-target compilation, exact signature and standard axioms |

Overall: pass. Parent owns the required full-project and separate `Roth.LeanEval`
dependent-build gates and the commit/push checkpoint.

Source frozen and ownership returned to parent at SHA256
`f4a686acc2e188a3bea162eb6bff0afd5079cd162d2297afbe1ce2b0d830529a`.
No further source edit after freeze; report-only completion.

## Required phase checklist

- [x] Step 1: references and worker contract read.
- [x] Step 2: all 24 audit items recorded.
- [x] Step 2.5: all five search methods have explicit status.
- [x] Step 2.6: every parameter audited; actual weakening/drop probes recorded.
- [x] Step 2.7: all signature lines have measured width rows.
- [x] Step 2.8: inequality scan table recorded.
- [x] Step 3: all 42 rules have status.
- [x] Step 4: strategy/term-mode/automation review completed.
- [x] Step 5a: complete live diagnostics clean apart from pre-existing header warning.
- [x] Step 5b: all diff gates passed.
- [x] Step 6a: no rename warranted, none queued.
- [x] Step 6b: result/report complete; no deferred refactoring.
