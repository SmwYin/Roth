# Phase 4 — Roth.abs_coeff_hasseDeriv_le

Dedicated declaration worker, 2026-10-16. Scope: Roth/CoeffNorm.lean original L129–140,
current L129–138, and this report only. No Git mutations or shared-log mutations.
Original public signature and existing docstring are byte-identical.
SOURCE FROZEN SHA256: `e69bf642ea61b7df2ae8ea75e5b379a66aa58a3da95b0a9b8ea4c9bc21231b47`.
Ownership revoked by file owner after this hash; subsequent work is report/probes/build only.

I have read golfing-rules.md, proof-patterns.md, mathlib-search.md,
generalisation-patterns.md, and cleanup-gates.md. Also read the two full skill files,
the full worker contract, style-rules.md, naming-conventions.md and mathlib-review-stages.md.
Conflicting generic documentation/visibility advice yields to explicit preserved-API scope.

## Mathematics and baseline

The coefficient at e of Δ_d P is the coefficient at e+d of P multiplied by a
product of binomial coefficients. If e+d is supported, its coordinates are bounded
by degreeOf, hence by r, and that product is at most 2^(sum r). If it is unsupported,
the input coefficient is zero. The global coefficient hypothesis also supplies 0 ≤ B.
No summing over multiple source coefficients is required.

File-owner baseline: full build then separate `lake build Roth.LeanEval`, both exit 0,
session 12002, logs `/private/tmp/roth-coeffnorm-d13-full.log` and
`/private/tmp/roth-coeffnorm-d13-leaneval.log` (file-owner evidence).
This worker unnecessarily repeated the full build: session 74669, exit 0, 2587 jobs.
An incorrectly spelled `lake build LeanEval` returned unknown target (session 8839,
exit 1); this was a command spelling error, not a project failure. File owner clarified
that the publication builds are their responsibility. No further full builds by this worker.
Native baseline complete LSP: success true, partial false, no errors, no target warnings.
Six outside warnings preserved: header, four DecidableEq arguments, hC.

## Full audit

| # | Item | Concrete result |
|---|---|---|
| 1 | LINT | No target warnings before or after; six outside warnings unchanged. |
| 2 | HAVE SCAN | Only `hc`, original L136/current L134: has `by`, one use in mul_le_mul; retain proof-bearing bound. |
| 3 | SET_OPTION | None in target; no limit changes. |
| 4 | SIMP SQUEEZE | Only terminal `simpa using` in zero branch; no nonterminal bare simp. |
| 5 | NAMING | `abs_coeff_hasseDeriv_le` names subject and bound, no forbidden abbreviation/pattern or `_ge_`/`_gt_`. |
| 6 | LINE PACKING | All three signature lines measured below, no repack rows. |
| 7 | BY PLACEMENT | Both theorem and hc `by` end their preceding lines. |
| 8 | FORMAT | Two-space proof indent, branch indent, no blanks/trailing spaces; lambda `=>` changed to `↦`. Cast rewrite preparation merged. No haveI/letI. |
| 9 | COMMENTS | No inline proof comments present; existing four-line docstring preserved exactly. |
| 10 | DOCSTRING | Existing explanation and cited source retained under explicit doc preservation. |
| 11 | VISIBILITY | Public API preserved; downstream coefficient estimates use it. |
| 12 | STRUCTURE | Body 9→7 tactic lines (original L132–140/current L132–138); branches 3 and 2 lines, no conjunction; not a headline named in Main results. |
| 13 | MATHLIB | Five-method search below: partial univariate coefficient API; retained multivariate composition of local coefficient/binomial API and mathlib order API. |
| 14 | JUNK DEF | n/a: theorem, no data definition. |
| 15 | EXISTS LEMMA | n/a: no existential conclusion or single-use existential helper. |
| 16 | SHOW/CHANGE | n/a: no show in target. |
| 17 | PUSH_NEG | n/a: no negation-pushing tactic. |
| 18 | GENERALISE | Every parameter covered below; actual drop and point-local probes; no public restatement applied. |
| 19 | INEQUALITY | No ≥ or > in statement/hypotheses; scan below. |
| 20 | NORMAL-FORM | Absolute real coefficient bound in ≤ orientation is appropriate; coefficient formula uses canonical coeff API. |
| 21 | SYNTAX-GEN | Global hP/hB match polynomial-wide downstream bounds. Point-local alternatives compile but change argument dependency/order; no optional restatement added. |
| 22 | IMPORT-FANOUT | n/a: no imports added or changed. |
| 23 | CASTS | No cast syntax added/dropped in diff. hc's ℕ→ℝ cast is cross-type; zero-branch ℝ annotation load-bearing (omission actually fails positivity). Existing public ℤ/ℝ syntax protected. |
| 24 | INSTANCE-NAME | n/a: theorem introduces no instance declaration. |

Issues fixed: cast normalization made explicit in one rw; lambda arrow corrected.
No required refactoring. Optional point-local forms are discussed below, not queued changes.

## Mathlib search-status

[A] Lean-Finder: `multivariate Hasse derivative coefficient absolute value bound binomial two power`
returned Chevalley numBound_succ, Polynomial.hasseDeriv_coeff, Chebyshev coefficient bound.
The univariate coefficient identity is a partial match, not this multivariate estimate.
[B] Loogle: first `MvPolynomial.coeff, abs, _ ≤ _` rejected unknown identifier in remote
index; corrected `Polynomial.hasseDeriv, Polynomial.coeff` returned hasseDeriv_coeff
and taylor_coeff. Both are univariate.
[C] LeanSearch: `Hasse derivative coefficient norm bounded by two to degree` returned
Chebyshev coefficient bound and polynomial root bounds, none applicable to arbitrary P.
[D] Untruncated rg in Mathlib/Algebra/MvPolynomial and Polynomial/HasseDeriv.lean for
`abs_coeff_hasseDeriv_le|coeff_hasseDeriv|hasseCoeff_le_two_pow` had no hits (exit 1).
Broader source read found the local Roth/HasseDeriv coefficient formula and binomial bound.
A guessed RingTheory/Polynomial/HasseDeriv path did not exist; corrected standard path used.
[E] Native local search `hasseDeriv`, limit30, returned local multivariate API and
mathlib univariate/LaurentSeries APIs; index warming, so no absence claim from that index.

Auxiliary variants considered: coeff_hasseDeriv, hasseDeriv_coeff, degreeOf_hasseDeriv_le,
hasseCoeff_le_two_pow, coefficient root/Chebyshev bounds. Common-equivalents table: no match
(discrete/finiteness/bornology buckets do not describe coefficient derivative growth).
Compiled generic probes: exact? and apply? at the normalized coefficient goal hit default
200000 heartbeat limits; neither supplied a replacement. Whole-proof grind with the
coefficient identity/binomial bound failed; whole-proof aesop failed with no progress.
This is evidence against these routes, not a universal theorem of absence.

Six strict rules considered: no new wrapper; all five searches attempted; auxiliary
variants checked; no custom predicate replacing a class; no exact equivalent found to
delete/specialize; documentation additions barred by preserved-doc scope, with relied-on
API recorded here. No new public lemma/API extraction required by the short clean proof.

## Generalisation status

| Parameter | Class | Use | Mechanical candidates / actual result |
|---|---|---|---|
| `{σ : Type*}` | type-variable | Index of all polynomials/exponents/sums | Already universe polymorphic; drop would leave σ unbound. No parent class or point/strict weakening applies. |
| `[Fintype σ]` | typeclass | Finite sum in public conclusion, hasseCoeff bound | Actual removal probe fails Fintype synthesis already in conclusion. Finite cannot synthesize that conclusion's univ sum without choosing a Fintype; requires restatement, not a drop. |
| `d` | structure-value | Derivative order, e+d, binomial coefficient | Occurs in conclusion; removing it leaves d unbound, no value-hypothesis weakening. ℕ multi-index is inherent to coefficient order. |
| `P` | structure-value | coeff and degreeOf | Occurs in all hypotheses/conclusion; drop is ill-formed. ℤ→abstract normed ring would restate coefficient height; outside preserved API. |
| `{r}` | structure-value | degree bounds and exponent sum | Occurs in conclusion; drop ill-formed. ℕ is degree codomain, not an unused algebra assumption. |
| `hP` | proposition | support exponent ≤ degreeOf ≤ r | Actual removal probe gives unknown hP at coefficient-bound step. Point-local probe `∀ j, (e+d) j ≤ r j` compiles using hasseCoeff_le_two_pow directly, but moves e before hypothesis and excludes some zero-coefficient cases; useful alternate sufficient condition, not a global weakening of hP. No strict inequality to weaken. |
| `{B}` | structure-value | real coefficient bound | Occurs in conclusion; drop ill-formed. ℝ→ordered field requires changing coefficient cast/conclusion and public type, not mechanical safe work. |
| `hB` | proposition | coefficient bound plus 0≤B | Actual removal probe gives unknown hB at mul_le_mul and zero branch. Actual point-local `abs(coeff(e+d)) ≤ B`, with e moved earlier, compiles. No strict inequality; global→local changes public signature and is not applied. |
| `e` | structure-value | Output coefficient and shifted input | Appears in conclusion; drop ill-formed; no weaker structure/value assumption. |

Actual applicable probes used isolated lean_run_code examples, preserving live public API.
Original hP/hB drop probes elaborated with errors; point-local hP/hB probes both success true,
no diagnostics. No live public signature was changed for testing. No decidability argument
exists on this target. No continuity/measurability/bijective/strict/equality assumptions.
Inversion diagnostic: coefficient identity exposes the scalar multiplication estimate, but
its binomial coefficient and degree support relationship remain specific to Hasse derivatives;
there is already generic mul_le_mul for the abstract remainder. No missing abstract helper.

Literature-driven optional generality: Hasse derivatives are defined over commutative rings,
but absolute coefficient height requires an absolute value/norm. A normed coefficient-ring
version would be a separate scoped API decision; not needed or applied here.

## Public literature search

Query: `Hasse derivative coefficient binomial multivariate polynomial height bound generalization`.
Top three ranked results captured:
1. [ECCC report 2026/032](https://eccc.weizmann.ac.il/report/2026/032/download):
   multivariate Taylor coefficient definition, finite-field applications; does not remove
   the degree/height assumptions needed for an archimedean height estimate.
2. [Fast Multivariate Multipoint Evaluation over All Finite Fields](https://doi.org/10.1145/3652025),
   Definition3.4/Proposition3.5: commutative-ring Hasse derivative with monomial binomial formula.
3. [Joints of Varieties](https://link.springer.com/article/10.1007/s00039-022-00597-5):
   Hasse derivative/Taylor formalism and coefficient extraction over fields.
Inference: algebraic coefficient formula has broader coefficient scope, whereas this real
height estimate can be generalized only after specifying a suitable absolute value/norm.
No hit implies dropping hP or hB in the existing statement. ChatGPT math MCP not available
in ALL_TOOLS; no second-opinion result claimed.

## Line packing

Actual `set_option format.width 100 in #check @Roth.abs_coeff_hasseDeriv_le` succeeded:

```lean
@Roth.abs_coeff_hasseDeriv_le : ∀ {σ : Type u_2} [inst : Fintype σ] (d : σ →₀ ℕ) (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), degreeOf j P ≤ r j) →
    ∀ {B : ℝ},
      (∀ (e : σ →₀ ℕ), |↑(P.coeff e)| ≤ B) → ∀ (e : σ →₀ ℕ), |↑(((hasseDeriv d) P).coeff e)| ≤ (2 ^ ∑ j, r j) * B
```

Widths measured as Unicode codepoints (not bytes); binder/conclusion is the next syntactic unit.

| Signature line | Chars | Next unit | Arithmetic | Action |
|---|---:|---|---|---|
| 129 | 91 | `(hP : ∀ j, degreeOf j P ≤ r j)` (30) | 91+1+30=122 >100 | ok |
| 130 | 97 | conclusion through `:= by` (65) | 97+1+65=163 >100 | ok |
| 131 | 69 | proof next | n/a | ok |

## Inequality scan

| # | Location | Original | Rewrite | Rename |
|---|---|---|---|---|
| 1 | signature+hypotheses | No ≥ or > | n/a; hP,hB,conclusion already ≤ | none |

## Golfing rule pass — all 42 rules

| Rule | Status |
|---|---|
| 1.1 | n/a: theorem is not a by-exact wrapper; hc has cast proof content. |
| 1.2 | n/a: no by-rfl. |
| 1.3 | n/a: rewrites normalize expressions rather than making final exact definitional. |
| 1.4 | Already terminal simpa-using in zero branch. |
| 1.5 | n/a: no trailing rfl. |
| 1.6 | n/a: no conjunction/constructor. |
| 1.7 | n/a: no apply-exact sequence. |
| 1.8 | n/a: no by_contra. |
| 1.9 | Lambda depends on j inside degree bound, so cannot eta-reduce; arrow corrected to ↦. |
| 1.10 | hc has by/proof content; not a no-by single-use alias. |
| 1.11 | n/a: no apply-intro. |
| 1.12 | n/a: no show. |
| 1.13 | n/a: no pair projections. |
| 1.14 | Applied: coeff rewrite, cast normalization, absolute product normalization now one rw. |
| 1.15 | n/a: no terminal simp only. |
| 1.16 | n/a: no nonterminal bare simp. |
| 1.17 | Existing .trans on degree estimate retained. |
| 1.18 | n/a: no removable terminal function parentheses; parenthesized proof arguments are followed by further arguments. |
| 1.19 | n/a: no push_neg. |
| 1.20 | n/a: no existential helper. |
| 2.1 | Actual whole-proof grind [coeff_hasseDeriv, hasseCoeff_le_two_pow] failed. |
| 2.2 | n/a: no retained grind to subsume preceding steps. |
| 2.3 | Existing simpa using is already consolidated. |
| 2.4 | n/a: no analytic function-property goals. |
| 2.5 | Actual positivity substitutes abs_nonneg in mul_le_mul successfully; retain direct abs_nonneg as clearer and shorter. Existing power positivity retained. |
| 2.6 | Actual gcongr on product leaves coeff bound; explicit mul_le_mul closes immediately. |
| 2.7 | n/a: no isolated linear Nat/Int arithmetic goal; binomial coefficient needs hasseCoeff bound. |
| 2.8 | Whole-proof aesop actual failure, no progress. |
| 2.9 | exact_mod_cast retained for Nat→Real inequality; explicit cast rw replacement compiled. |
| 2.10 | n/a: arbitrary symbolic polynomial/real B bound is not a finite computation. |
| 2.11 | n/a: no denominators/algebra identity. |
| 2.12 | n/a: no ring/ring_nf terminal proof. |
| 2.13 | n/a: supported and zero branches are not symmetric. |
| 2.14 | n/a: no calc. |
| 2.15 | n/a: no repeated similar subgoals. |
| 3.1 | n/a: no erw. |
| 3.2 | n/a: no continuity/measurability tactics. |
| 3.3 | n/a: no omega. |
| 3.4 | n/a: no rcases rfl. |
| 3.5 | No attribute added: bound is not a simplification equality, and broad automatic registration is not required by downstream use. |
| 3.6 | n/a: no simp_all only. |
| 3.7 | n/a: no maxHeartbeats override. |

Additional real tests: nlinarith [hB (e+d)] failed on product goal. Omitting the
zero-branch explicit real type caused positivity to fail; annotation retained.
Some preliminary lean_multi_attempt snippets replaced only one line and collided with
remaining normalization steps or indentation; these were not accepted proofs. The final
candidate was independently tested as a complete standalone example, success true.

## Reflection and verification

A one-tactic proof was tested and did not succeed. The support split is mathematically
natural; generic mul_le_mul handles the product bound directly. Flattening hc into an
inline cast proof would obscure the scalar estimate. No helper extraction is justified:
branches are3/2 lines, and the target is not a module headline. The rewrite chain improves
predictability by replacing push_cast search with its two explicit arithmetic lemmas.

`/Users/ramin/.elan/bin/lake build Roth.CoeffNorm`, session31196, exit0:
Built Roth.CoeffNorm (23s), completed1658 jobs. Native final complete LSP after module
build: success true, partial false, timed_out false, no failed dependencies, zero errors,
zero target warnings, same six outside warnings. No suppression/new axioms/sorry added.

Independent verification scratch: `/private/tmp/roth-d14-check.lean`, explicit original
signature assignment to public theorem plus independent reproof from coeff_hasseDeriv,
hasseCoeff_le_two_pow and order API. A first named-theorem scratch attempt omitted hP/hB
from its type (section variables not auto-included), so it failed and was discarded.
A CLI attempt during module build lacked the in-progress olean, so rerun after build.
Final CLI result is recorded in the completion addendum below.

## Gate status

| Gate | Result | Evidence |
|---|---|---|
| lake_build_file | ✓ pass | Actual module build session31196 exit0. |
| definition_protected | ✓ pass | No def/abbrev/instance changed. |
| theorem_statement_protected | ✓ pass | Original signature/docstring unchanged; independent original-type assignment. |
| structure_gate | ✓ pass | Seven tactic body lines, branches3/2, no ∧; non-headline. |
| naming_gate | ✓ pass | No forbidden name pattern/abbreviation; no rename required. |
| line_packing_gate | ✓ pass | All three signature lines have measured ok rows above. |
| inequality_orientation_gate | ✓ pass | Scan table; zero ≥ or >. |

Overall: pass, subject to independent verification completion addendum.
Renames queued: none. Comments preserved: no inline proof comments; original docstring unchanged.
Refactoring needed: none required. No optional public restatement authorized/applied.

## Phase checklist

- [✓] Step1 — reference docs read.
- [✓] Step2 — full24-item audit printed.
- [✓] Step2.5 — five-method mathlib search printed.
- [✓] Step2.6 — every parameter mechanical analysis and applicable probes printed.
- [✓] Step2.7 — full signature width table and actual width100 #check printed.
- [✓] Step2.8 — inequality scan table printed.
- [✓] Step3 — every42 golfing rule has a status.
- [✓] Step4 — reflection and alternative strategy considered.
- [✓] Step5a — complete native diagnostics clean of errors and target warnings.
- [✓] Step5b — actual module build and diff-content gates printed.
- [✓] Step6a — rename sidecar unnecessary; no name issue.

## Completion addendum

Fresh CLI independent check: `/Users/ramin/.elan/bin/lake env lean
/private/tmp/roth-d14-check.lean`, session30662, exit0. The original-type assignment
and independent nonself reproof both compiled. Axiom output for each theorem is exactly
`[propext, Classical.choice, Quot.sound]`; no sorryAx. This resolves the earlier stale-import
native info and failed scratch attempts. Final SHA256 recheck matches the frozen hash.
Overall gates: pass. Before9 body lines; after7; saved2. Declaration including signature:
12→10 lines. Two issues fixed (cast preparation and lambda syntax), zero required refactors.

Final supplementary automation probes at zero-branch entry: simp_all simplified to
`0 ≤ B` without closing; positivity rejected the nonzero-left-side inequality; grind
failed. Line replacement also produced expected indentation collision with the unchanged
next line; no tested snippet was adopted and source hash remained unchanged.
