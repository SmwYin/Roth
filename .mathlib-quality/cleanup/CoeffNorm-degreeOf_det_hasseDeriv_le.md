# Phase 4 — Roth.degreeOf_det_hasseDeriv_le

Dedicated declaration 25 audit. Original source: `/private/tmp/roth-coeffnorm-original.lean`
L281–294; worker-start snapshot: `/private/tmp/roth-d25-start.lean` L241–254;
final source: `Roth/CoeffNorm.lean` L241–249.
Before: 14 declaration lines / 11 proof lines. After: 9 / 6. Saved: 5 lines.

SOURCE FROZEN: `dbbbeba0c96895502c9830ac2bca3fe8fb952028582f53e76e49964d6f9cc63a`.
The fileowner explicitly revoked source ownership at this hash. No later source writes;
the same whole-file hash was rechecked after the probes. Only this declaration's proof
and ordinary-lambda arrow spelling changed. All parameters, order, explicitness,
mathematics, documentation, imports, header, pinned versions and other declarations remain
unchanged. No helpers, instances, renames, Git operations, full build, or LeanEval by this worker.

## Step 1 — references and mathematical context

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read the mathlib-quality and lean4
skills, cleanup-all instructions, relevant cleanup command instructions, the complete
Phase-4 contract, naming conventions, relevant style rules and mathlib-review-stages.
The initial large combined reads were truncated, so the contract and search guide were
subsequently read in segments. These are the workflow sources, not prior reports.

The result bounds the degree in a fixed variable of a determinant of Hasse derivatives.
Expand the determinant over permutations; a sum has degree at most the largest summand
degree; constant multiplication does not increase degree; a product has degree at most
the sum of its factor degrees; each Hasse derivative has degree at most that of P.
There are l factors, each bounded by r j. This matches the last sentence of the proof
before Lemma 3 in `.mathlib-quality/references/clean.tex` L435: F is a determinant with
entry degree at most r_j, so its individual degree is at most l r_j.

Fresh native baseline diagnostics were complete: `partial=false`, `success=true`, zero
errors and six warnings elsewhere in the file. No target-range warnings. Header metadata
and pending hC/DecidableEq API decisions belong to the owner and were left untouched.

## Step 2 — full audit, all 24 items

1. LINT: none on this declaration. Six inherited file warnings remain: header, four
   unused-in-type DecidableEq warnings, and unused hC in normOne_det_le.
2. HAVE SCAN: original `hsign` has `by`, one use in the following rewrite. Its proof
   content was not blindly inlined: the entire multiplication/sign argument was replaced
   by `degreeOf_C_mul_le`. No have remains.
3. SET_OPTION: n/a — no per-declaration option or elaboration limit in original/final source.
4. SIMP SQUEEZE: original sign-case `simp [h, degreeOf_neg]` and final `by simp` were
   terminal. Both disappeared with the old steps. Final `simpa using` is terminal and
   deliberately unsqueezed. No nonterminal bare simp.
5. NAMING: `degreeOf_det_hasseDeriv_le` names the degree bound for the Hasse-derivative
   determinant, using the existing mixed-case operation names. No forbidden abbreviation,
   scheme number, single-letter theorem, `_ge_`, `_gt_`, or numbered auxiliary suffix.
   No rename needed or queued.
6. LINE PACKING: all three signature lines measured below; every break is justified.
   Body maximum 69 codepoints. No width/packing change needed in signature.
7. BY PLACEMENT: `:= by` remains at the end of the conclusion line.
8. FORMAT: two-space tactic indentation, four-space signature continuation, no internal
   blank line/trailing space, one tactic per line, no haveI/letI or tactic-semicolon chain.
   Ordinary `fun` arrows changed to `↦` in the statement and proof.
9. COMMENTS: no proof comments existed; none deleted. Existing docstring byte-preserved.
10. DOCSTRING: public result already documents the bound and local source; preserved
    under the explicit documentation lock.
11. VISIBILITY: public API preserved. This is a classic import/namespace file, not a
    leading-`module` file. No visibility changes authorized or necessary.
12. STRUCTURE: six proof lines, no conjunction and no case branches. Below even the
    15-line headline threshold. No extraction or decomposition flag needed.
13. MATHLIB: five actual methods below. The constant-multiplication API replaces the
    bespoke sign proof; determinant/sum/product degree APIs provide the remaining steps.
14. JUNK DEF: n/a — theorem, no definition value introduced or changed.
15. EXISTS LEMMA: n/a — no existential statement/helper.
16. SHOW vs CHANGE: none in this worker-start version. A term-mode show alternative was
    tested in native multi-attempt, but the direct API application was accepted without it.
17. PUSH_NEG: n/a — no negative-proposition normalization.
18. GENERALISE: every parameter drop-tested, pointwise and abstract variants compiled
    below. Public restatements were not applied. Optional redesigns closed without action.
19. INEQUALITY: scan table below. Both inequalities already use ≤; no reversed notation/name.
20. NORMAL-FORM: standard Matrix.det, MvPolynomial.degreeOf, finite sums/products and
    ≤ bound are appropriate normal forms; no equivalence/conversion layer needed.
21. SYNTAX-GEN: pointwise degree hypothesis works, but existing global hP is convenient
    for callers that already have all individual-degree bounds. Preserve existing API.
22. IMPORT-FANOUT: n/a — no imports changed or added.
23. CASTS: removed the standalone polynomial cast/type ascription with hsign; retained
    `(Equiv.Perm.sign τ : ℤ)` as a genuine unit-to-integer coercion, and `(i : Fin l)`
    as load-bearing index annotation for the independent sum proof. Removing the sign
    coercion was tested and fails with `CommSemiring ℤˣ`. Counts: 1 polynomial
    ascription removed / 1 cross-type coercion kept / 1 index annotation kept.
24. INSTANCE-NAME: n/a — no instance declarations or names.

Issues fixed: bespoke sign-degree case split, explicit sum-cardinality calc, ordinary
lambda arrows. Refactoring needed: none within authorized scope.

## Step 2.5 — five-method mathlib search

| Method | Actual query/search | Result |
|---|---|---|
| A Lean-Finder | `MvPolynomial degreeOf integer constant cast is zero` | degreeOf_one, degreeOf_C, degrees_C, totalDegree_C, degrees_one |
| A follow-up | matrix of multivariate polynomials, entry degrees bounded by r, determinant degree at most matrix size times r | Matrix.toMvPolynomial_totalDegree_le, Polynomial.natDegree_det_X_add_C_le, Matrix.det_matrixOfPolynomials, Matrix.det_mvPolynomialX_ne_zero, Matrix.det_le; none states the present general entry-bound result |
| B Loogle | `MvPolynomial.degreeOf, Int.cast` | no hits |
| B follow-up | `MvPolynomial.degreeOf, MvPolynomial.C, _ * _` | degreeOf_C_mul_le, degreeOf_mul_C_le, degreeOf_C_mul |
| C LeanSearch | degree in one variable of determinant of multivariate polynomial matrix bounded by sum of entry degree bounds | degreeOf, degreeOf_mul_le, Matrix.det_le, det_sum_le, det_matrixOfPolynomials |
| D source rg | degreeOf integer/C/det/prod/mul patterns in MvPolynomial and Matrix/Determinant | Degrees.lean degreeOf_C, degreeOf_mul_le, degreeOf_prod_le, degreeOf_C_mul_le, degreeOf_mul_C_le; no exact determinant/Hasse name |
| E local names | degreeOf_det; degreeOf_C_mul_le | local target plus unrelated degree lemmas; then exact positive hit degreeOf_C_mul_le |

Auxiliary variants: C_mul/mul_C and their ≤/equality variants; det_apply'; sum/prod
degree bounds; Finset.sum_le_sum and sum_le_card_nsmul. Native `#check` confirmed
degreeOf_C_mul_le and all reused APIs. The guessed `C_intCast` and `Int.cast_sign`
names were actually checked and rejected as unknown, then discarded.
Common-equivalents lookup: no matching discrete/finite/bornology bucket.

Concluded: partial match `MvPolynomial.degreeOf_C_mul_le`; keep the public theorem and
build directly on it. No claim of exhaustive mathematical absence is made. Untruncated
full-name source searches and prerequisite-only `exact?`/`apply?` probes found no direct
replacement. `exact?` could not close; bounded `apply?` produced only generic Nat/degree
reductions and exhausted 10000 heartbeats. Target theorem was excluded from those imports,
so this is not self-reproof through the existing name.

Six strict-rule disposition: (1) no new wrapper; proof composes determinant expansion,
sum supremum, constant multiplication, product degree, derivative degree and sum bounds,
not merely 1–3 calls; (2) all five methods plus nonself compiled probes; (3) auxiliary
variants inspected; (4) no custom class predicate; (5) no exact equivalent found for
deletion, and public API is explicitly preserved; (6) dependencies recorded here while
existing module documentation remains locked. No extraction signals remain: no repeated
cast juggling, definitional-equality rewrite, or manual typeclass plumbing.

## Step 2.6 — generalisation, every parameter

Native isolated examples used only the original prerequisite imports. Drop probes used
`set_option autoImplicit false` so Lean could not silently reintroduce deleted parameters.
These were scratch probes, with no public-source mutations.

| Parameter | Class/use | Mechanical candidates tried | Verified result |
|---|---|---|---|
| `{σ : Type*}` | universe/type variable in polynomials, indices, degrees | drop; universe catalogue | drop fails unknown σ; already universe-polymorphic |
| `{l : ℕ}` | structure value, Fin size and multiplier | drop; arbitrary finite index restatement | drop fails unknown l; arbitrary ι with Fintype/DecidableEq compiles |
| `E` | structure value, derivative multi-indices | drop; abstract matrix restatement | drop fails unknown E; generic matrix/entry-degree version compiles |
| `P` | structure value, polynomial and degree hypothesis | drop; ℤ→CommRing R | drop fails unknown P (also reaches normal heartbeat limit downstream); CommRing R version compiles |
| `{r : σ → ℕ}` | structure value, degree bounds/RHS | drop; point-local scalar bound | drop fails unknown r; pointwise hP version compiles |
| `hP` | proposition, factorwise degree comparison | drop; point-local degreeOf j P ≤ r j; strict→weak | drop fails unknown hP at factor step; pointwise version compiles; already weak ≤ |
| `j` | structure value, target variable | drop | drop fails unknown j in target and proof; no weaker value-type catalogue entry |

No typeclass/decidability binder occurs on this declaration. Algebraic typeclass parents,
topological point-localisation, structure unbundling, strict→weak, and dropping completeness
are otherwise inapplicable: this theorem starts with concrete integer coefficients and
dependent data parameters, not those stronger assumptions.

Additional verified scratch statements: arbitrary `[CommRing R]` coefficient ring;
arbitrary finite matrix index type; arbitrary matrix with entry degree bounds. The last
one confirms the inversion diagnostic: after expansion the proof uses only entry bounds,
and the Hasse-specific input is degreeOf_hasseDeriv_le. These are mathematically valid
broader formulations, but no necessary caller benefit or defect in the present API was
found. They would add/restyle public API. Closed as optional redesigns under the owner's
explicit public-API preservation instruction; no pending question or required refactor.

### Public literature status

An initial combined exploratory request queried `polynomial matrix determinant degree
bound Hasse derivatives generalization commutative ring` and `Hasse derivative degree
polynomial arbitrary characteristic determinant degree bound`. The response merged both
rankings; its first three displayed hits were [Goresky's algebra notes](https://www.math.ias.edu/~goresky/pdf/algebraic0.pdf),
[ROABP hierarchy paper](https://anamay.bitbucket.io/assets/docs/papers/ROABP-Hierarchy.pdf),
and [Hilbert functions and finite-degree Zariski closure](https://doi.org/10.1016/j.jcta.2015.03.011).
For auditable per-query top-three results, the questions were then searched separately:

Query 1: `polynomial matrix determinant degree bound generalization commutative ring`.
Top three returned hits:

1. [Northwestern, Chapter XII](https://sites.math.northwestern.edu/~len/d70/chap12.pdf):
   determinant over a commutative ring is homogeneous of matrix-entry degree r; supports
   the generic matrix argument used in the scratch probe.
2. [UNL Math 818 contents](https://www.math.unl.edu/~jkettinger2/818toc): determinant
   permutation formula and degree n in entries over a commutative ring; corroborates
   the same framework, not a direct Hasse determinant bound.
3. [Conrad, generalized Cayley–Hamilton](https://math.stanford.edu/~conrad/210BPage/handouts/cayleyhamilton.pdf):
   characteristic-polynomial determinant over A[x] with A commutative; related generic
   determinant setting, not an exact replacement theorem.

Query 2: `Hasse derivative degree polynomial generalization arbitrary characteristic`
(repeated separately after the long combined output was truncated). Top three returned:

1. [Joints of Varieties, author manuscript](https://par.nsf.gov/servlets/purl/10337079):
   uses Hasse derivatives over arbitrary fields, including positive characteristic.
2. [Algebraic independence over finite fields: higher derivation based](https://citeseerx.ist.psu.edu/document?doi=2cc8db4c436d9e5f06085d50e5b3df38c5efe642&repid=rep1&type=pdf):
   works with fields of arbitrary characteristic and higher derivations.
3. [Hasse derivative](https://en.wikipedia.org/wiki/Hasse_derivative): canonical
   overview surfaced by search, not used as a technical authority.

The same search also surfaced [nLab's Hasse–Schmidt derivative page](https://ncatlab.org/nlab/show/Hasse-Schmidt%2Bderivative),
whose result describes derivatives for P in R[X]. Technical conclusions here rely on
the primary-source determinant/Hasse descriptions and the compiled Lean probes, not
on claims that those pages contain this exact theorem. Inference: integer coefficients
are not mathematically essential for this degree estimate; the generalized proof was
independently compiled above. ChatGPT math MCP: n/a — no such capability in ALL_TOOLS.

## Step 2.7 — signature packing

Native `#check @Roth.degreeOf_det_hasseDeriv_le` with `format.width := 100`:

```text
@Roth.degreeOf_det_hasseDeriv_le : ∀ {σ : Type u_1} {l : ℕ} (E : Fin l → Fin l → σ →₀ ℕ) (P : MvPolynomial σ ℤ)
  {r : σ → ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) → ∀ (j : σ), degreeOf j (Matrix.of fun μ ν ↦ (hasseDeriv (E μ ν)) P).det ≤ l * r j
```

The renderer did not obey a hard 100-column wrap on its generated message; source
widths below were measured directly as Unicode codepoints. Complete next binders and
complete conclusion fragments are the packing units, not single lexical words.

| Signature line | Chars | Next fragment | Arithmetic | Action |
|---|---:|---|---|---|
| 241 | 96 | `{r : σ → ℕ}` (11) | 96 + 1 + 11 = 108 > 100 | ok |
| 242 | 56 | conclusion through `:= by` (81) | 56 + 1 + 81 = 138 > 100 | ok |
| 243 | 85 | none — proof follows | n/a | ok |

## Step 2.8 — inequality scan

| Occurrence/location | Original/final | Rewrite | Rename |
|---|---|---|---|
| hP, L242 | degreeOf j P ≤ r j | none; already ≤ | none |
| conclusion, L243 | degreeOf j (...) ≤ l * r j | none; already ≤ | none |
| reversed-symbol scan | zero ≥ and zero > in signature (ordinary arrows are ↦) | n/a | name has no _ge_/_gt_ |

## Step 3 — all 42 golfing rules

| Rule | Status/evidence |
|---|---|
| 1.1 by exact wrapper | n/a — no wrapper in proof |
| 1.2 by rfl | n/a — no reflexivity proof |
| 1.3 rw + exact → rwa | n/a — determinant rewrite is followed by degree-bound refinements |
| 1.4 simp + exact → simpa | applied in spirit to final arithmetic/sum bound: terminal simpa using sum_le_sum |
| 1.5 trailing rfl | n/a — none |
| 1.6 anonymous constructor | n/a — no conjunction/constructor |
| 1.7 apply + exact | n/a — no such pair; API transitivity uses refine |
| 1.8 by_contra! | n/a — no contradiction proof |
| 1.9 eta reduction | n/a — permutation and sum lambdas bind genuinely used indices |
| 1.10 single-use have | hsign has by; replaced entire argument with constant-multiplication API, no have left |
| 1.11 refine + fun | already used with Finset.sup_le; no apply/intro pair |
| 1.12 redundant show | direct degreeOf_C_mul_le succeeds; no show introduced |
| 1.13 obtain pair | n/a — no projected pair |
| 1.14 merge rw | n/a — only determinant rewrite remains |
| 1.15 terminal simp unsqueeze | final simpa is unsqueezed; no terminal simp only |
| 1.16 nonterminal simp squeeze | n/a — no nonterminal bare simp |
| 1.17 dot notation | existing .trans retained on degree inequalities |
| 1.18 <| | no shorter useful application; final sum lambda needs parentheses for simpa using |
| 1.19 push Not | n/a — no push_neg |
| 1.20 trivial exists | n/a — no existential wrapper |
| 2.1 whole grind | actual prerequisite-only probe fails with determinant-degree inequality unproved |
| 2.2 delete before grind | n/a — no grind retained |
| 2.3 simpa consolidation | applied: four-line calc becomes two-line terminal simpa using sum_le_sum |
| 2.4 fun_prop | n/a — algebraic degree bound, no analytic predicate |
| 2.5 positivity | n/a — goal is upper bound, no isolated positivity premise |
| 2.6 gcongr | actual live sum-goal attempt reports no progress |
| 2.7 lia / omega | actual live sum-goal lia fails; finite-sum degree premise requires explicit API, so no omega fallback needed |
| 2.8 aesop | actual prerequisite-only probe fails, made no progress |
| 2.9 norm_num / norm_cast | obsolete sign cast subproof removed with API; no numerical cast equality remains |
| 2.10 decide | n/a — symbolic theorem with arbitrary polynomial, no closed finite decision |
| 2.11 field_simp/ring | n/a — no division or ring identity |
| 2.12 linear_combination | n/a — no ring/ring_nf ending or polynomial equality |
| 2.13 wlog | n/a — sign branches removed entirely, no symmetric case split remains |
| 2.14 collapse calc | applied by terminal simpa; alternative sum_le_card_nsmul also compiled but needs three lines |
| 2.15 <;> sharing | n/a — old two sign cases disappeared with constant-multiplication API |
| 3.1 erw → rw | n/a — no erw |
| 3.2 legacy fun tactics | n/a — no continuity/measurability tactic |
| 3.3 omega → lia | no omega retained; lia was tried at 2.7 |
| 3.4 rcases rfl | sign rcases removed entirely; no remaining equality substitution |
| 3.5 automation attributes | n/a — no attribute needed for this specialized upper bound, no new global automation scope |
| 3.6 simp_all | n/a — no simp_all only or terminal context simplification needed |
| 3.7 remove maxHeartbeats | no limit in source; 10000-heartbeat cap was only bounded search scaffolding |

Native multi-attempt replaces a line, not a complete calc block. The first sum experiment
therefore also reported trailing-parser errors; those were not treated as mathematical
failures of the final proposal. The successful candidate was retested in a complete
isolated example, then installed and verified in the live file. Initial whole-proof
multi-attempt stalled and was cancelled; later individual bounded prerequisite-only
probes above supplied actual results instead of treating the cancelled call as evidence.

## Step 4 — reflection and alternatives

The core improvement is mathematical API selection: degreeOf_C_mul_le already forgets
the sign coefficient without evaluating its two unit values. The remaining proof follows
the determinant expansion directly. A fully nested term would still need the determinant
rewrite and terminal simplification and would obscure the finite-sum argument.
The final sum_le_sum proof compiles in two lines; sum_le_card_nsmul independently compiles
but takes three lines here, so it was not installed. Whole simp made no progress, grind
and aesop failed, exact? failed, and apply? only suggested generic reductions under its
bounded search. No necessary helper, new API declaration, or alternative strategy remains.

## Step 5 — verification and diff gates

1. Full live native diagnostics after edits and again after the module build:
   `partial=false`, `success=true`, `timed_out=false`, no failed dependencies, zero errors,
   exactly the six inherited warnings listed above. One intermediate final call returned
   partial while imports re-elaborated; the next complete call succeeded. No partial result
   was counted as a pass.
2. `/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`: exit 0, `Built Roth.CoeffNorm (16s)`,
   `Build completed successfully (1658 jobs)`. Existing header/unused-API warnings only.
   Full build and separate Roth.LeanEval remain the fileowner's job.
   Owner subsequently reported full and separate Roth.LeanEval builds both exit 0 in
   session 24977, hash unchanged; logs `/private/tmp/roth-coeffnorm-d25-full.log` and
   `/private/tmp/roth-coeffnorm-d25-leaneval.log`. This is owner-supplied evidence.
3. Native isolated assignment of the result to the exact original universally quantified
   type passed, with original binder order and implicit r. Source comparison also confirms
   signature byte identity after only `=>`→`↦` normalization.
4. Native independent proof under only the original prerequisite imports passed with
   `success=true`, no diagnostics. No import of Roth.CoeffNorm and no target-name reference.
5. Native `#print axioms Roth.degreeOf_det_hasseDeriv_le` reports only
   `[propext, Classical.choice, Quot.sound]`.
6. Snapshot diff is restricted to this declaration; docs/imports/other code byte-preserved.
   Whole-file frozen SHA256 checked again after probes and source revocation.
7. Profiling: native lean_profile_proof was bounded to 20 seconds and returned its timeout.
   Isolated trace.profiler elaboration succeeds but MCP exposes only `(trace)`, not timing.
   No per-declaration timing claim is made. File-level Phase 6.6 belongs to the owner;
   no source heartbeat/profiling options added, no unresolved proof decomposition needed.

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | pass | module build exit 0, 1658 jobs |
| definition_protected | pass | no def/abbrev values or declarations touched |
| theorem_statement_protected | pass | exact original-type assignment; only lambda glyph changed |
| structure_gate | pass | 6 body lines, no conjunction or branch |
| naming_gate | pass | descriptive operation-based bound name, no forbidden patterns |
| line_packing_gate | pass | three measured signature rows, no repack rows |
| inequality_orientation_gate | pass | zero reversed comparison symbols, no rename required |

Overall: Phase-4 gates pass. No new performance certification is claimed; file-level buzz
is separate from this declaration's proof/audit gates.

## Step 6 — result and all 11 checklist entries

Before 14 / after 9 / saved 5 declaration lines; body 11→6.
Rules applied: constant-multiplication API replacement, ordinary-lambda arrows,
1.4/2.3/2.14 terminal sum consolidation. Renames queued: none. Comments preserved:
no proof comments present, original declaration docstring unchanged. Refactoring needed:
none. Optional generalization ideas closed under public-API preservation, no user question.

- [✓] Step 1: reference documents read.
- [✓] Step 2: all 24 audit answers above.
- [✓] Step 2.5: five actual search methods and auxiliary variants recorded.
- [✓] Step 2.6: every parameter/drop test, compiled broader candidates and public literature recorded.
- [✓] Step 2.7: every signature line measured with arithmetic.
- [✓] Step 2.8: occurrence-based inequality scan recorded.
- [✓] Step 3: all 42 golfing rules have an applicable result or concrete n/a reason.
- [✓] Step 4: alternatives tested and strategy reconsidered.
- [✓] Step 5a: complete final native diagnostics clean in target, existing file warnings recorded.
- [✓] Step 5b: snapshot diff and all required Phase-4 gates checked.
- [✓] Step 6a: no rename necessary, so no queue entry or caller edits.
