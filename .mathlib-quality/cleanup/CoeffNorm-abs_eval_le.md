# Phase 4 — `Roth.abs_eval_le`

Dedicated single-declaration audit. Original source lines 212–240; final lines 223–239.
Before: 25 proof-body lines; after: 14 (15 including the `:= by` line); saved 11.
Public signature and complete existing docstring are byte-identical.
Whole-file SOURCE FROZEN SHA256:
`f3bf41ffebbac5dab7b9fd600a154957131ae7b259e6281c4bc48f879004a2ad`.
Source ownership was revoked at that checkpoint; subsequent work was report/probes/gates only.

## References and baseline

Read both full SKILL.md files and the full worker contract, substituting this declaration,
file and range. I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read the complete style-rules.md
and naming-conventions.md and the relevant review-stages sections.
The inherited full baseline build and separate `lake build Roth.LeanEval` (session 8381,
exit 0) were accepted as directed; neither was repeated by this worker.
Initial complete native LSP: success true, partial false, no errors; six outside warnings.

## Full 24-item audit

| # | Item | Finding and action |
|---|---|---|
| 1 | LINT | No target warning. Complete initial/final LSP each show six outside warnings: preserved header, four DecidableEq signatures and hC. No suppression added. |
| 2 | HAVE SCAN | Original hB0: no by, explicit helper use plus implicit positivity use, retained. Original hbox: no by, one use, inlined at the subset argument. Original heval: by proof, replaced entirely with direct Mathlib expansion. Final hB0 has explicit and implicit uses; no other have. |
| 3 | SET_OPTION | None in target or diff. |
| 4 | SIMP SQUEEZE | Original nonterminal simp only [abs_pow] merged with abs_mul/abs_prod rewrites into a precise nonterminal simp only list. Terminal box equality simp preserved in extracted helper. A live simp? probe at the already simplified closing step made no progress; no bare nonterminal simp remains. |
| 5 | NAMING | abs_eval_le describes the mathematical conclusion, snake_case, no forbidden abbreviation/pattern; no rename. |
| 6 | LINE PACKING | Every public signature line measured below, 97/65/75 codepoints, all breaks justified. |
| 7 | BY PLACEMENT | by stays at end of signature line; all local by proofs follow this convention. |
| 8 | FORMAT | Two-space body indent; calc continuations retained; no empty proof lines, trailing spaces, haveI, letI, or semicolon chains. Lambda arrows changed to ↦ in edited lines. |
| 9 | COMMENTS | No inline proof comments existed; complete source docstring preserved verbatim. |
| 10 | DOCSTRING | Existing value-bound docstring and source citation preserved exactly, per API preservation instruction. |
| 11 | VISIBILITY | Public headline remains public. Only new helper is private with descriptive _aux suffix and no docstring. |
| 12 | STRUCTURE | Main body reduced 25→14 lines; no conjunction; largest nested proof four lines. Meaningful finite geometric-product bound extracted above. |
| 13 | MATHLIB | Direct eval_map/eval₂_eq' replace manual as_sum/map_sum/monomial proof. Five methods and exact?/apply? probes below. |
| 14 | JUNK DEF | n/a: theorem, no definitions added or altered. |
| 15 | EXISTS LEMMA | n/a: no existential theorem or witness wrapper. |
| 16 | SHOW vs CHANGE | n/a: no show/change in final target. |
| 17 | PUSH_NEG | n/a: no push_neg. |
| 18 | GENERALISE | Every parameter mechanically examined and probed below; public API retained. |
| 19 | INEQUALITY | All signature inequalities are ≤; scan table below. |
| 20 | NORMAL-FORM | eval_map is the standard simp conversion to eval₂; eval₂_eq' gives canonical finite support sum. Public coefficient/degree form retained for callers. |
| 21 | SYNTAX-GEN | Current coordinate-degree and coefficient hypotheses apply directly in Roth's bound. Support-local coefficient hypotheses would require an additional nonnegative B condition at P=0; no silent restatement. |
| 22 | IMPORT-FANOUT | n/a: no imports added, removed, or changed. |
| 23 | CASTS | 0 redundant casts introduced. The remaining `(P.coeff k : ℝ)` bridges ℤ→ℝ. The public nested ascription is unchanged. Removed manual expansion contained one other genuine ℤ→ℝ cast, not an optimization of the type contract. |
| 24 | INSTANCE-NAME | n/a: no instance declaration added or touched. |

Issues fixed: long headline proof, manual evaluation expansion, single-use hbox,
and separated absolute-value rewrites. No target issue silently deferred.
Added helper needing its own **fresh dedicated audit**:
`sum_box_prod_pow_le_aux`, lines 208–218. This report does not claim that helper audited.

## Mathlib search-status

| Method | Actual query | Result |
|---|---|---|
| A Lean-Finder | Bound absolute value of multivariate polynomial evaluation by coefficient bound times product of powers of one plus absolute values | Returned Chevalley numBound/degBound and Dioph.abs_poly_dioph; no direct target match. |
| B Loogle | `MvPolynomial.eval₂, | _ | ≤ _`, then corrected `MvPolynomial.eval₂, _ ≤ _` | First query parser rejection; corrected query returned Polynomial.eval₂_homogenize_of_eq_one, unrelated. |
| C LeanSearch | multivariate polynomial norm evaluation coefficient bound | Returned norm_coeff_le_choose_mul_mahlerMeasure, coeff_le_of_roots_le, le_gaussNorm; none is the desired value estimate. |
| D Source rg | Full names abs_eval_le and sum_box_prod_pow_le_aux; norm_eval.*le, eval.*norm.*le; inspected MvPolynomial/Eval.lean | No equivalent target found. eval₂_eq' at line 76 and eval_map at line 432 directly replace expansion. Untruncated searches, no head/max-count filter. |
| E Local name | MvPolynomial.eval₂_eq | Found eval₂_eq, eval₂_eq', eval₂_eq_eval_map and variants (index warming, so not used as absence evidence). |

Auxiliary variants: eval₂_eq versus eval₂_eq', eval₂_eq_eval_map versus eval_map;
support-product versus full Fintype product. All used candidates verified by compiled #check.
Common-equivalents lookup: no bucket applies (not discreteness/finiteness/separation/bornology).
Actual live whole-proof grind failed; aesop exhausted with eval₂ bound remaining;
exact? failed to close; apply? offered only generic abs_le/ordered-arithmetic reductions.
No claim that source search alone proves absence. The compiled discovery probes establish
that the obvious generic routes did not solve this target.

Six strict rules: (1) this is a substantive box-bound estimate, not a one-to-three-call
wrapper; (2) all five methods plus actual exact? were used; (3) evaluation auxiliary
variants inspected; (4) no custom predicate introduced; (5) no equivalent full target
found to delete, partial evaluation API used directly; (6) direct Mathlib usage recorded
here, existing module/docstrings preserved under the stronger scope instruction.

## Generalisation status — every parameter

Actual isolated probes: `/private/tmp/d24-drops.lean`, CLI session 56315 exit 1 as expected;
`/private/tmp/d24-data-drops.lean`, session 60926 exit 1 as expected, autoImplicit false.
These deliberate failing scratch probes were never added to the project source.

| Parameter | Class and use | Mechanical candidates and actual evidence | Result |
|---|---|---|---|
| `{σ : Type*}` | type variable, all indices | Drop in scratch (renamed to unbound τ): unknown identifier τ at L6–7. Universe polymorphic already; no fixed universe to weaken. No concrete indexing type to abstract. | Retain. |
| `[Fintype σ]` | typeclass, ∏ and box | Drop: Fintype synthesis fails at L7/10/11/13/17. Parent `[Finite σ]`: same failures at L37/40/41/43/47, because statement uses actual Fintype products. | Retain; parent would require rewriting the statement or scoped construction. |
| `(P : MvPolynomial σ ℤ)` | structure value, evaluation/coefficients/degrees | Drop with autoImplicit false: unknown P/P.coeff at L10–12. Concrete ℤ→abstract coefficient ring is a public mathematical restatement, listed below; not a parameter deletion. | Retain. |
| `{r : σ → ℕ}` | structure value, all exponent bounds | Drop: unknown r at L14/16. Naturals are polynomial exponents, not merely an induction-order parameter. | Retain. |
| `hP` | proposition, support inclusion | Drop actual proof: unknown hP at scratch L71. No strict inequality to weaken. Point-localization cannot retain only one coordinate because product uses every coordinate; support-local monomial bounds are an equivalent API restatement rather than weaker degree data. | Retain; independent counterexample below confirms essential bound. |
| `{B : ℝ}` | structure value, coefficient/value threshold | Drop: unknown B at L19/20. Real ordered bound is part of target, abstract ordered codomain is a big restatement. | Retain. |
| `hB` | proposition, every coefficient and B nonnegative | Drop actual proof: unknown hB at L99. No strict→weak candidate. Restriction to support alone loses nonnegativity at P=0; actual counterexample below. | Retain. |
| `(x : σ → ℝ)` | structure value, evaluation point | Drop: unknown x at L24. No continuity, integrability or monotonicity premise to point-localize. General normed codomain is a big restatement. | Retain. |

Actual counterexamples compiled in `/private/tmp/d24-counterexamples.lean`, session 42054,
exit 0: X at x=2 with r=0 and B=1 violates the bound without degree control;
P=0, B=-1, r=0 violates it when a support-only coefficient condition is vacuous.
The first has an ordinary valid coefficient bound but invalid degree bound; the second
has a valid degree bound but lacks the original global coefficient hypothesis.
There is no DecidableEq parameter on the public target to delete. No algebraic,
analytic, bijective or strict hypothesis from the weakening catalogue occurs.
Inversion check: P is a variable, not a fixed named construction; no hidden concrete
witness to abstract after one rewrite. The extraction separates the finite-box estimate.

Big-change candidate for Phase 5 consideration: a separate normed commutative-ring or
real-coefficient evaluation variant, with norms and a coefficient ring homomorphism.
The algebraic expansion already supports commutative semirings; the current exact
public statement must remain available. This prospective variant is **unverified**;
it has not been applied or represented as a completed generalisation.

## Literature search

Web query 1: “multivariate polynomial evaluation bound coefficient height product
geometric sum generalization”. Top three results:

1. [Rack, Markov inequality generalization](https://www.sciencedirect.com/science/article/pii/0021904582901083).
2. [Amortized multivariate multipoint evaluation](https://www.sciencedirect.com/science/article/abs/pii/S0885064X22000589).
3. [Fast multivariate multipoint evaluation](https://doi.org/10.1145/3652025).

These concern different bounds/algorithmic complexity; they do not justify dropping
any current hypothesis.
Web query 2: “polynomial evaluation absolute value sum absolute coefficients triangle
inequality normed ring”. Top three results:

1. [Neukirch, Algebraic Number Theory, valuations](https://www.math.toronto.edu/~ila/Neukirch_Algebraic_number_theory.pdf).
2. [Elementary polynomial-root inequalities](https://www.pure.ed.ac.uk/ws/portalfiles/portal/8655499/ELEMENTARY_INEQUALITIES_INVOLVING_THE_ROOTS_OF_A_POLYNOMIAL_WITH_APPLICATIONS_IN_HARMONIC_ANALYSIS_AND_NUMBER_THEORY.pdf).
3. [MIT arithmetic geometry, absolute values](https://ocw.mit.edu/courses/18-782-introduction-to-arithmetic-geometry-fall-2013/6fa17c4b03bb6826fd2731ee2da74e2b_MIT18_782F13_lec5.pdf).

These support the absolute-value/triangle-inequality framework. The possible normed-ring
extension is an inference from that framework, not a claimed quotation or tested theorem.
ChatGPT math MCP: n/a, no tool matching chatgpt/math appeared in ALL_TOOLS discovery.
Local canonical source remains the existing §6 Lemma 9 reference preserved in the docstring.

## Width-100 reference and packing

Compiled `/private/tmp/d24-proof.lean` with `set_option format.width 100`:

```lean
@abs_eval_le : ∀ {σ : Type u_2} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      (∀ (d : σ →₀ ℕ), |↑(P.coeff d)| ≤ B) →
        ∀ (x : σ → ℝ), |(eval x) ((map (Int.castRingHom ℝ)) P)| ≤ B * ∏ j, (1 + |x j|) ^ r j
```

| Sig line | Chars | Next complete syntactic unit | Arithmetic | Action |
|---|---:|---|---|---|
| 223 | 97 | `{B : ℝ}` (7) | 97 + 1 + 7 = 105 > 100 | ok |
| 224 | 65 | conclusion including `:= by` (71, indent excluded) | 65 + 1 + 71 = 137 > 100 | ok |
| 225 | 75 | no next signature line | n/a | ok |

No touched Lean line exceeds 100 codepoints. Signature equality checked mechanically.

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | entire signature/hypotheses | n/a — zero ≥/> | none; hP/hB/conclusion use ≤ | none |

Final body also has zero ≥/> comparisons. Lambda arrows are ↦; → in types is not a comparison.

## All 42 golfing rules

| Rule | Status |
|---|---|
| 1.1 | n/a: no by-exact wrapper. |
| 1.2 | n/a: no by-rfl wrapper. |
| 1.3 | n/a: no final rw/exact pair with same closing expression. |
| 1.4 | Tried live simpa-only consolidation at coefficient bound: works but requires explicit product type and 100+-char wrapping, no improvement over current two lines. |
| 1.5 | Applied by deleting the manual heval proof, including trailing rfl, in favor of eval₂_eq'. |
| 1.6 | n/a: no constructor pair. |
| 1.7 | n/a: no apply/exact chain. |
| 1.8 | n/a: no contradiction/negation. |
| 1.9 | n/a: remaining lambdas supply dependent arguments, not eta wrappers. |
| 1.10 | Applied: hbox inlined; hB0 retained for explicit and implicit use. |
| 1.11 | n/a: no apply/intro chain. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no projected conjunction have. |
| 1.14 | Applied: evaluation expansion uses a single rw list; absolute-value rewrites merged into simp only. |
| 1.15 | n/a: terminal helper simp stays bare; target simp only is nonterminal. |
| 1.16 | n/a: no bare nonterminal simp. Actual simp? probe recorded above. |
| 1.17 | Retained .trans composition for triangle/sum comparisons and degree bounds. |
| 1.18 | n/a: remaining parentheses fix constructor/argument grouping; no avoidable trailing by parens. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no trivial existential helper. |
| 2.1 | Tried native whole-proof grind; failed with negated evaluation inequality, as recorded above. |
| 2.2 | n/a: no final grind. |
| 2.3 | Tried live simpa consolidation; retained clearer two-line coefficient estimate. |
| 2.4 | n/a: no function-property goal. |
| 2.5 | Applied/retained positivity for nonnegative product and omitted box terms. |
| 2.6 | Tried live gcongr on monomial comparison; leaves coefficient inequality, so current direct multiplication lemma retained. |
| 2.7 | n/a: no residual Nat/Int arithmetic goal; degree comparisons use transitivity. |
| 2.8 | Tried native whole-proof aesop; exhaustive search did not prove eval₂ bound. |
| 2.9 | n/a in target: no concrete numeric or cast-arithmetic goal. Counterexample simp probes compile separately. |
| 2.10 | n/a: arbitrary real variables make this unsuitable for finite decidable computation. |
| 2.11 | n/a: no denominators or ring identity. |
| 2.12 | n/a: no ring/ring_nf ending. |
| 2.13 | n/a: no symmetric case split. |
| 2.14 | Applied conceptually inside triangle and coefficient bounds with .trans; full three-stage calc preserves intermediate box estimate clearly. |
| 2.15 | n/a: no multiple similar generated goals to combine. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactics. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases-with-rfl. |
| 3.5 | No attribute added: this bound has user-supplied r/B and is not an unconditional rewrite normal form. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no heartbeat or recursion limit override. |

## Reflection

The proof's mathematical steps are triangle inequality, bounded coefficients,
enlarging support to a degree box, and a finite product of geometric sums.
Whole-goal automation and exact? did not replace these steps. eval₂_eq' eliminates the
fragile manual polynomial expansion. A fully term-style nested transitivity expression
would obscure the box estimate; the 14-line calc exposes it directly. The helper is
the weighted geometric-product estimate, independent of P, not a duplicate evaluation
wrapper. The earlier direct prod_univ_sum use is preserved exactly inside that helper.

## Actual verification and diff gates

Original-type assignment and independent nonself reproof:
`lake env lean /private/tmp/d24-proof.lean`, session 90708, exit 0.
The independent reproof is the complete original proof under a fresh name; it contains
no reference to abs_eval_le. A separate exact original-signature example assigns
`abs_eval_le P hP hB x`. Both target and independent_reproof print only
`[propext, Classical.choice, Quot.sound]`. The first probe invocation used unsupported
`pp.width`; corrected scratch option to `format.width` and reran successfully.

Final frozen-source module gate: `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`,
session 24551, exit 0, 1658 jobs replayed. Earlier changed-source module build session
55791 also exited 0, compiling CoeffNorm in 17 seconds.
Final native complete diagnostics: success true, partial false, timed_out false,
failed_dependencies empty; no errors/sorries/target warnings, six preserved outside warnings.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | frozen-source module build session 24551 exit 0 |
| definition_protected | ✓ pass | baseline comparison: no existing def/abbrev changed |
| theorem_statement_protected | ✓ pass | exact docstring+signature string equality true |
| structure_gate | ✓ pass | 14 body lines, 15 including := by; no ∧ or long branch |
| naming_gate | ✓ pass | descriptive conforming target name, no rename |
| line_packing_gate | ✓ pass | complete 3-row signature table, no repack |
| inequality_orientation_gate | ✓ pass | zero ≥/> in signature/hypotheses |
| scope | ✓ pass | outside target plus new helper, whole source prefix/suffix identical to worker baseline |
| trust | ✓ pass | independent original proof and exact-type assignment compile; standard axioms only |

Overall: pass for this dedicated declaration. Helper audit remains a separate task.
Renames queued: none. Comments preserved: complete docstring; no inline comments existed.
Refactoring needed: fresh dedicated audit of sum_box_prod_pow_le_aux; optional abstract
normed-coefficient variant for Phase 5 consideration, with original API preserved.

## Required phase checklist

- [✓] Step 1 — complete reference documents read.
- [✓] Step 2 — full 24-item audit recorded.
- [✓] Step 2.5 — five-method search and six strict rules recorded.
- [✓] Step 2.6 — every parameter examined, actual isolated probes and literature recorded.
- [✓] Step 2.7 — every public signature line measured and width-100 #check recorded.
- [✓] Step 2.8 — inequality scan table recorded.
- [✓] Step 3 — all 42 golfing rules have individual statuses.
- [✓] Step 4 — mathematical reflection completed.
- [✓] Step 5a — native complete file diagnostics clean of errors and target warnings.
- [✓] Step 5b — actual module build and full diff gates passed.
- [✓] Step 6a — no rename needed; no sidecar mutation.
