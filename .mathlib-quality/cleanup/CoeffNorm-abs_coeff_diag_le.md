# Phase 4: `Roth.abs_coeff_diag_le`

Dedicated single-declaration audit, 2026-10-16. Scope: `Roth/CoeffNorm.lean:169–176`
before, 169–174 after; C18 main/headline diagonal coefficient estimate.
Only this declaration's proof and this report were edited. No Git operations or shared logs.
Public signature and documentation are byte-identical. Declaration: 8 → 6 lines;
proof body: 6 → 4 lines. Two issues fixed: lambda arrow and repetitive terminal branches.

## References and mathematical understanding

Read both full skills (`mathlib-quality/SKILL.md`, `lean4/SKILL.md`), the full worker
contract `/private/tmp/roth-coeffnorm-worker-contract.md`, and full references
`golfing-rules.md`, `proof-patterns.md`, `mathlib-search.md`,
`generalisation-patterns.md`, `cleanup-gates.md`, `style-rules.md`,
`naming-conventions.md`, `mathlib-review-stages.md`, and `profiling.md`.

Diagonal substitution collects monomials of the same total degree. A resulting coefficient
is a sum of selected original coefficients. The triangle inequality bounds its absolute
value by the sum of absolute values, and the uniform bound gives `#support * B`.
In the nonmatching-degree branch the monomial coefficient is zero; `abs_nonneg` and `hB`
imply `0 ≤ B`. The final `grind` discharges these two elementary cases together.
The source at `.mathlib-quality/references/clean.tex:1449` explicitly gives this estimate
when replacing all variables by the same variable. Its exact source quotation was read.

Baseline inherited from file owner: full `lake build` and separate `lake build Roth.LeanEval`
session 39188 exit 0; complete baseline LSP no errors. These expensive baseline builds were
not repeated by this worker. Baseline/current six outside warnings are preserved: header,
four `DecidableEq` public arguments, and `hC`; no target warning.

## Full 24-item audit

| Item | Finding and action |
|---|---|
| 1 LINT | Complete live-file diagnostics before/after: target no warnings/errors; six inherited outside warnings only. |
| 2 HAVE SCAN | No `have` declarations, hence no single-use temporaries to inline. |
| 3 SET_OPTION | No per-declaration options or limits; none introduced. |
| 4 SIMP SQUEEZE | Original terminal `simpa` in zero branch was already unsqueezed; removed with branch consolidation. No remaining simp calls. |
| 5 NAMING | `abs_coeff_diag_le` is descriptive snake_case, uses established `coeff`/`diag` API names, and has no forbidden abbreviation or numeric pattern. No rename. |
| 6 LINE PACKING | Both signature lines measured below, width-100 `#check` performed. No repack required. |
| 7 BY PLACEMENT | `by` remains at the end of signature line 170. |
| 8 FORMAT | Two-space proof indent, one tactic per line, no blanks/internal instance syntax; changed `fun k _ =>` to `fun k _ ↦`. |
| 9 COMMENTS | No proof comments present; none removed. |
| 10 DOCSTRING | Existing public mathematical statement and §6 source quotation preserved exactly under the explicit documentation contract. |
| 11 VISIBILITY | Main public result listed in module documentation; visibility preserved. |
| 12 STRUCTURE | Four body lines, no conjunction, one-line shared case discharge; headline limit 15 and branch limit 10 both satisfied. |
| 13 MATHLIB | All five methods below; existing triangle/cardinality API used directly; no direct replacement established. |
| 14 JUNK DEF | n/a: theorem, no definition introduced. |
| 15 EXISTS LEMMA | n/a: no existential/helper declaration. |
| 16 SHOW/CHANGE | No `show` or `change`. |
| 17 PUSH_NEG | No `push_neg`. |
| 18 GENERALISE | Every parameter and actual probes recorded below; optional public variants closed under preservation policy. |
| 19 INEQUALITY | Both `≤` occurrences already correctly oriented; zero reverse symbols, scan below. |
| 20 NORMAL-FORM | Standard real absolute-value coefficient bound with smaller side left. `norm`/Gauss norm versions would require conversion without removing the diagonal specialization. |
| 21 SYNTAX-GEN | Current bound consumes the coefficientwise hypothesis directly. Support-local variant compiles but no concrete caller benefit requires an API change; closed. |
| 22 IMPORT-FANOUT | n/a: no imports added or removed. |
| 23 CASTS | Diff contains no casts: 0 dropped / 0 kept cross-type / 0 kept load-bearing in diff. Existing signature has two genuine ℤ→ℝ casts, two redundant ℤ annotations, and an implicit card ℕ→ℝ cast; signature preserved exactly. `Int.cast_sum` is the necessary sum/coercion bridge. |
| 24 INSTANCE-NAME | n/a: theorem introduces no instance. |

## Mathlib search status

| Method | Actual query and result |
|---|---|
| A Lean-Finder | Native query `absolute value of a sum bounded by cardinality times uniform bound polynomial coefficient diagonal substitution`; top hits `Dioph.abs_poly_dioph`, `ChevalleyThm.MvPolynomialC.numBound`, `Polynomial.cauchyBound`, all different subjects. |
| B Loogle | `Finset, |∑ _ ∈ _, _| ≤ _`; found exactly `Finset.abs_sum_le_sum_abs`, used directly. |
| C LeanSearch | `absolute value coefficient polynomial sum bounded by number of terms times bound`; returned `Polynomial.le_gaussNorm`, `Polynomial.coeff_bdd_of_roots_le`, `Polynomial.mahlerMeasure_le_sum_norm_coeff`; useful related norm bounds, none directly about this diagonal substitution. |
| D Source | Searched coefficient/sum/absolute-value bounds across Polynomial, MvPolynomial and ordered big operators; read `MvPolynomial/Polynomial.lean` and Finset triangle/card estimates. Untruncated full-name/selected-file search for `abs_coeff_diag_le`, `sum_le_card_nsmul`, `abs_sum_le_sum_abs`, coefficient `aeval`/`eval₂` confirmed constituent API, not a direct diagonal bound. |
| E Name pattern | Native `abs_sum_le_sum_abs`, `sum_le_card`, `coeff_diag`; returned Finset/Multiset/List sum API, this target, and unrelated matches. Index was `warming`; positive results verified by compiled `#check`, and empty/irrelevant results are not claimed as proof of absence. |

Auxiliary variants: `Polynomial.finsetSum_coeff`, `Polynomial.coeff_monomial`,
`Finset.sum_le_card_nsmul`, `Finset.abs_sum_le_sum_abs`, norm/coeff/root bounds and
`coeff` of `aeval`/`eval₂`. Common-equivalents lookup: no bucket for diagonal substitution;
generic bounded-sum pattern already has its canonical Finset API.

Conclusion: partial matches found; keep the protected public diagonal estimate and use the
existing mathlib sum lemmas directly. No new wrapper/helper or custom predicate introduced.
No unsupported exhaustive absence claim: compiled `exact?` and `apply?` both exhausted default
200,000 heartbeats. This is negative automation evidence, not a proof of library absence.
The six replacement rules were checked: direct constituent use, all five searches,
auxiliary searches, no disguised typeclass predicate, no found duplicate to delete, and
mathlib usage documented here without rewriting protected module documentation.

## Public literature search

Primary query: `polynomial diagonal substitution coefficient bound number terms height generalization`.
Top three returned hits:

1. [A sharper multivariate Christol theorem](https://www.researchgate.net/publication/371311480_A_sharper_multivariate_Christol%27s_theorem_with_applications_to_diagonals_and_Hadamard_products)
   — power-series coefficient diagonals, not substituting one variable for all variables.
2. [On the number of solutions of certain diagonal equations](https://www.sciencedirect.com/science/article/abs/pii/S0022314X21002705)
   — finite-field solution counting, not the coefficient estimate.
3. [No Free Degenerations](https://lucablanchi.it/presentation-theory/no-free-degenerations-presentation-cost-heights-normal-forms)
   — heights/presentations, not a direct formulation used here.

Additional query `"polynomial" "substitution" "length" "height" "triangle inequality"`
returned these top three (all irrelevant to the specific diagonal estimate):

1. [KAIST library catalogue](https://library.kaist.ac.kr/search/ctlgSearch/posesn/view.do?bibctrlno=1136397&se=b0&ty=B).
2. [Math 115A lecture notes mirror](https://studyres.com/doc/1918450/lecture-notes-for-math-115a--linear-algebra--fall-of-2002...?page=223).
3. [Problem Solving Tactics mirror](https://studylib.net/doc/27217550/problem-solving-tactics).

Additional query `"Formalizing Roth" Takloo Yin coefficients` returned these top three:

1. [CERN preprint-history article DOI](https://doi.org/10.1007/s11024-026-09639-w).
2. [Same unrelated article on Springer](https://link.springer.com/article/10.1007/s11024-026-09639-w).
3. [Unrelated Erdős formalization README](https://github.com/Shashi456/erdos-formalizations/blob/main/Erdos/P283/RSG/README.md).

No mathematical claim is inferred from these irrelevant hits. Separate-query reruns confirmed
the rankings after the original combined-query result interleaved their output.

Focused primary-source query:
`polynomial length coefficient sum absolute values substitution inequality site:arxiv.org`.
Top three hits:

1. [New Bounds on the Real Polynomial Roots](https://arxiv.org/abs/2008.11039)
   — root bounds from coefficient absolute sums, not this specialization.
2. [Fractional Pseudorandom Generators from Any Fourier Level](https://arxiv.org/pdf/2008.01316)
   — coefficient ℓ¹ masses and the triangle inequality (related generic principle).
3. [Parameterized algorithms for block-structured integer programming](https://arxiv.org/pdf/2311.01890)
   — unrelated integer-programming inequalities.

The local primary project source `clean.tex:1449` is the direct mathematical source; it supports
the exact current estimate. Abstract normed-coefficient and finite-fiber versions are mathematical
possibilities, not literature-established replacements from this search.
ChatGPT mathematics MCP: n/a, no such callable tool in `ALL_TOOLS` metadata.

## Mechanical generalisation: every parameter

| Parameter | Class / use | Candidates and actual probe | Result |
|---|---|---|---|
| `{σ : Type*}` | Universe-polymorphic variable, exponent domain | Already arbitrary universe (`#check` shows `u_1`); drop with autoImplicit false | CLI reports unknown `σ`; retain. No typeclass parent to weaken. |
| `(P : MvPolynomial σ ℤ)` | Structure value supplying both coefficient lists and support | Drop with autoImplicit false; concrete→abstract coefficients considered | CLI reports unknown `P`. ℤ→abstract ring/norm is public construction restatement, not mechanical binder weakening; closed under preservation absent concrete benefit. |
| `{B : ℝ}` | Scalar bound and RHS factor | Drop with autoImplicit false; abstract ordered scalar considered | CLI reports unknown `B`. Real→abstract norm/ordered ring changes public statement; closed under preservation. No strict/nonzero assumption present. |
| `(hB : ∀ d, |(P.coeff d : ℝ)| ≤ B)` | Proposition needed in both coefficient cases | Drop hypothesis; restrict to `∀ d ∈ P.support, ...` | Drop is false: compiled `P = C 1 : MvPolynomial Unit ℤ`, `B = 0`, `n = 0` counterexample. Support-local variant independently compiles with membership supplied; public argument change not applied under preservation policy. |
| `(n : ℕ)` | Requested univariate coefficient index | Drop with autoImplicit false; Nat→abstract index considered | CLI reports unknown `n`; Polynomial coefficient indices are definitionally ℕ, so arbitrary-index restatement changes the object. |

Actual probes: `/private/tmp/d18_drop_binders.lean`, CLI session 22637 exit 1 with expected
unknown identifiers `σ`, `P`, `B`, `n`; `/private/tmp/d18_generalise.lean`, session 55483
exit 0 for support-local weakening plus explicit counterexample to dropping `hB`.
Only inherited outside `hC` warning occurs in the prefix-based scratch file.
No inherited typeclass hypotheses: `#check @Roth.abs_coeff_diag_le` confirms precisely the
five binders above. Pointwise restrictions beyond support would need an additional nonnegativity
condition when no degree-n monomial exists, so they do not simply weaken this API.

Inversion check: `diag` disappears after `diag_eq_sum`, leaving the general finite-sum triangle
and cardinality estimate already supplied by mathlib. Thus there is no missing abstract theorem
to introduce. Optional abstract-coefficient/support-local API variants closed: no concrete
required downstream benefit, public contract preserved. No pending refactoring action.

## Line packing (width 100)

Fresh CLI `#check @Roth.abs_coeff_diag_le`, `set_option format.width 100`:

```lean
@Roth.abs_coeff_diag_le : ∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) {B : ℝ},
  (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) → ∀ (n : ℕ), |↑((Roth.diag P).coeff n)| ≤ ↑P.support.card * B
```

| Signature line | Codepoints | Next complete binder | Arithmetic | Action |
|---|---:|---|---|---|
| 169 | 96 | `(n : ℕ)` (7 chars) | 96 + 1 + 7 = 104 > 100 | ok |
| 170 | 71 | None, proof follows | n/a, complete conclusion and `:= by` already on line | ok |

Every final declaration line ≤100 codepoints; maximum 96. No signature edits.

## Inequality scan

| Occurrence | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | `hB`, line 169 | `|...| ≤ B` | Already oriented | none |
| 2 | Conclusion, line 170 | `|...| ≤ P.support.card * B` | Already oriented | none |
| — | Whole signature | No `≥` or `>` | n/a | No `_ge_`/`_gt_` name |

The tactic token `<;>` is not a reversed inequality and is excluded from the signature scan.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 by exact | n/a: no whole-proof wrapper. |
| 1.2 by rfl | n/a: no reflexivity proof. |
| 1.3 rw + exact | n/a: rewrite precedes two cases, not one exact term. |
| 1.4 simpa | Original zero branch already used terminal simpa; consolidated into grind. |
| 1.5 trailing rfl | n/a: none. |
| 1.6 constructor | n/a: no compound constructor goal. |
| 1.7 apply + exact | n/a: no such sequence. |
| 1.8 by_contra | n/a: no contradiction proof. |
| 1.9 eta lambda | Lambda must bind k and ignore membership; not eta-reducible. Changed arrow to ↦. |
| 1.10 have | n/a: no have. |
| 1.11 apply + intro | Existing refine + lambda already uses compact form. |
| 1.12 show | n/a: no show. |
| 1.13 obtain | n/a: no projections or destructuring. |
| 1.14 merge rw | Initial four rewrites already combined; coefficient rewrite requires the intervening sum-bound refinement. |
| 1.15 terminal simp only | n/a: no squeezed terminal simp. |
| 1.16 nonterminal simp | n/a: no bare nonterminal simp. |
| 1.17 dot notation | `.trans` already used directly. |
| 1.18 <\| | Parentheses around the second argument of `.trans` are needed to delimit the lambda/refinement; no removable terminal parentheses. |
| 1.19 push Not | n/a: no push_neg. |
| 1.20 existential | n/a: no existential helper. |
| 2.1 grind | Whole-proof grind fails (compiled fail_if_success). After monomial rewriting, `split_ifs <;> grind [abs_nonneg]` closes both cases; applied. |
| 2.2 preceding tactics | n/a: removing monomial expansion would hide the coefficient cases; no obsolete simp/rw before the final grind. |
| 2.3 simpa consolidation | `split_ifs <;> simpa using hB k` tested, leaves zero≤B; final grind handles it. |
| 2.4 fun_prop | n/a: no function-regularity goal. |
| 2.5 positivity | Actual native `split_ifs <;> positivity` reports not a positivity goal; does not solve either branch. |
| 2.6 gcongr | Actual native case probe reports no progress in both branches. |
| 2.7 lia/omega | n/a: ordered arithmetic is over ℝ; no Nat/Int arithmetic subgoal. Grind handles the real linear inequality. |
| 2.8 aesop | Whole proof fails in scratch; native case aesop leaves `0 ≤ B`. |
| 2.9 norm_num/norm_cast | Native case norm_num simplifies zero but leaves both inequalities; Int.cast_sum already crosses casts once. |
| 2.10 decide | n/a: not a closed finite decidable proposition. |
| 2.11 field_simp/ring | n/a: no denominators or equality identity. |
| 2.12 linear_combination | n/a: proof does not end in ring/ring_nf; the needed reasoning is an inequality. |
| 2.13 wlog | n/a: matching/nonmatching degree branches are not symmetric. |
| 2.14 calc | Already `.trans` term composition; no calc block. |
| 2.15 <;> | Applied shared discharge to both split_ifs goals. |
| 3.1 erw | n/a: only rw. |
| 3.2 regularity tactics | n/a: none. |
| 3.3 omega→lia | n/a: no omega or arithmetic migration. |
| 3.4 rcases rfl | n/a: none. |
| 3.5 automation attributes | No new global attribute: arbitrary-bound theorem is not a simplifying equality/normal form; local grind hint sufficient. |
| 3.6 simp_all | n/a: no simp_all only; ordinary whole-proof simp already tested and failed. |
| 3.7 maxHeartbeats | No limit present or introduced. |

## Reflection, simplify and performance

Whole-proof `grind`, `simp`, `aesop` were asserted to fail in independently compiled scratch
`d18_experiments.lean` (session 52964 exit 0). `exact?` hit the default deterministic limit
in earlier scratch session 29048; native `apply?` at line 171 also hit 200,000 heartbeats.
No one-tactic replacement established. Removing the first rewrites would obscure the finite
sum; a term-mode lambda/cases expression is longer. No `have` blocks or redundant steps remain.
The four-line proof follows the mathematics using existing APIs without helper extraction.

Initial native whole-proof multi-attempt/run-code calls stalled and were canceled; bounded
fallback multi-attempt session 28131 returned timeout at 65s and exited. A fallback session
startup 81909 exited cleanly. Fresh CLI then supplied isolated proof experiments; subsequent
native case attempts returned normally. Successful native consolidation probe returned goals=[];
its original-file trailing bullet diagnostics were expected from replacing only line 174 and
are absent from frozen production diagnostics.

Performance scratch `/private/tmp/d18_perf.lean`, corrected command syntax
`#count_heartbeats in`, CLI session 73914 exit 0:

| Version | Heartbeats | Per-declaration time |
|---|---:|---|
| Original | 627 | Below 100ms profiler threshold |
| Consolidated | 1542 | Below 100ms profiler threshold |

The short automated case closure costs 915 extra heartbeats but remains far below the 1s
budget and default limit; it removes duplicated case handling. No source profiling scaffolding.
The first profiling scratch used the stale reference's `count_heartbeats` spelling and failed;
it was corrected after reading the installed `#count_heartbeats` syntax, then recompiled.

## Actual verification and gates

SOURCE FROZEN SHA256 of whole `Roth/CoeffNorm.lean`:
`e8cec540e872c07592442cd4c2a9cf8bbaec03e0ee89ab0ebe9814295cb79d2c`.
Ownership explicitly revoked by file owner immediately after freezing. No later source edits.

`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session 37835, **exit 0**:
1658 jobs, target built in 17s. Complete native live diagnostics after freeze:
`success=true`, `partial=false`, `timed_out=false`, `failed_dependencies=[]`, zero errors,
six inherited outside warnings only, zero target warnings.

Fresh CLI `/Users/ramin/.elan/bin/lake env lean /private/tmp/d18_verify.lean`, session 38036,
**exit 0**: exact original-type assignment to the production theorem; separate
`independent_d18` reproof using the original explicit two branches and no call to the target;
both axiom sets exactly `[propext, Classical.choice, Quot.sound]`.
Width-100 `#check` output above came from this fresh verification.

| Gate | Result | Actual evidence |
|---|---|---|
| lake_build_file | ✓ pass | Session 37835 exit 0, module build 17s. |
| definition_protected | ✓ pass | Target-only unified diff contains no def/abbrev changes. |
| theorem_statement_protected | ✓ pass | Python byte comparison against `/private/tmp/d18_original_block.txt`: signature identical; exact-type CLI assignment compiles. |
| structure_gate | ✓ pass | Four proof lines ≤15; no conjunction; one-line branches. |
| naming_gate | ✓ pass | Descriptive name, no forbidden pattern, no rename. |
| line_packing_gate | ✓ pass | Both signature rows measured; 96+1+7=104, last row complete. |
| inequality_orientation_gate | ✓ pass | Actual signature scan: zero ≥/>; two correctly oriented ≤ occurrences. |
| trust/scaffolding | ✓ pass | Actual target scan no sorry/axiom/options/haveI/letI; independent standard-axiom reproof. |

The first mechanical scan naively counted `>` inside `<;>` and asserted; corrected scan
checks the signature as required and passes. This was a probe bug, not a source failure.
Final SHA recheck matches the frozen hash. Maximum declaration width 96 codepoints.
Overall: **pass**. Renames queued: none. Refactoring needed: none; optional public generality
variants are explicitly closed under the preservation policy. Comments preserved: existing
documentation unchanged; no inline proof comments existed.

## Required phase checklist

- [✓] Step 1 — full reference docs and both skills read.
- [✓] Step 2 — all 24 audit items recorded.
- [✓] Step 2.5 — all five mathlib search methods and six rules recorded.
- [✓] Step 2.6 — every parameter, mechanical probes and public literature search recorded.
- [✓] Step 2.7 — every signature line measured with width-100 #check reference.
- [✓] Step 2.8 — per-occurrence inequality scan recorded.
- [✓] Step 3 — all 42 golfing rules have individual status rows.
- [✓] Step 4 — reflection and actual alternative-proof tests complete.
- [✓] Step 5a — complete final native diagnostics, no errors/target warnings.
- [✓] Step 5b — actual module build, protected-signature, structure, naming, packing and orientation gates pass.
- [✓] Step 6a — no renames required; no shared sidecar edited.
