# Full mathlibable assessment: `Roth.normOne`

Canonical declaration **75/293**, public definition at `Roth/CoeffNorm.lean:47`.
**Verdict: NO-composable-from-mathlib.** This verdict concerns upstream inclusion of the
integer-only definition. Retain its useful project-local name during this source-frozen survey;
no Lean source change, deletion, instance installation, or upstream submission is performed.

## Phase 0 — Baseline and resolution

The successful baseline `lake build` at `99f19fda4b3cbee38fc0d31af76075834f5cc265`
reported 2467 jobs, exit 0, no warnings or errors. Reuse is justified by a fresh match of
**all 17 production source and pin hashes**, not merely by the existence of compiled files.
See [baseline](../evidence/Roth.normOne/baseline-build.txt),
[inputs](../evidence/Roth.normOne/inputs.json), and
[hash gate](../evidence/Roth.normOne/input-hash-check.json).

The declaration uniquely resolves in production code. It contains no unproved placeholder,
new axiom, unsafe proof, or resource-limit setting. The entire declaring module was read:
it develops coefficient ℓ¹ bounds, Hasse derivative bounds, diagonal substitution, evaluation,
and determinant estimates. [Exact module](../evidence/Roth.normOne/source-module.lean.txt).

## Phase 1 — Mathematical comprehension and native type

For an integer polynomial in an arbitrary variable set, take the real sum of the absolute
values of its nonzero coefficients. The polynomial has finite support even if its variable
set is infinite, so this quantity is finite and the zero polynomial has value zero. This is
the coefficient ℓ¹ norm, also called the polynomial's length; it is not the maximum coefficient,
Mahler measure, or an integral norm of the polynomial's values.

Native full type, from `#print`:

```lean
Roth.normOne.{u_1} : {σ : Type u_1} → MvPolynomial σ ℤ → ℝ
```

Its exact body is:

```lean
fun {σ} P ↦ ∑ d ∈ P.support, |((P.coeff d : ℤ) : ℝ)|
```

`σ` is the universe-polymorphic variable type and `P` the polynomial. There are **no explicit
typeclass assumptions, finite-variable assumptions, decidable-equality parameters, nonzero
hypotheses, or degree bounds**. Integer commutative-ring and real absolute-value structures
are inferred internally. The result is real-valued data, so a theorem conclusion is n/a.
Native expansion by `rfl` and standard axiom output are retained in
[target source](../evidence/Roth.normOne/native-target-executed.lean.txt) and
[target receipt](../evidence/Roth.normOne/native-target-success.json).

## Phase 2 — Size and one-line definition gate

**BIG**: a named mathematical concept listed in the module's main definitions and used as the
central scalar quantity in its determinant estimate. This classification does not narrow the
literature protocol. The definition body has **one substantive line**.

| One-line exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | No demonstrated requirement | `rfl` exposes the body; ordinary unfolding is already used at CoeffNorm67,87,100,115,153. No sealed representation barrier was found. |
| Avoid typeclass diamonds | No | This is a scalar function, not a type, instance, or alternate structure on polynomials. It does not select between competing norm instances. |
| Semantic intent / API stability | **Yes** | Fourteen distinct local declaration consumers include `normOne_mul_le`, `normOne_det_le`, and `normOne_hasseDeriv_le`; the name makes their statements readable and can shelter later implementation changes. |

Conclusion: **ONE-LINER WITH-EXEMPTION**. This permits considering upstream inclusion; it does
not overrule an actual one-call existing-mathlib composition. Keeping a project-specific name
can be sound design without making its specialised definition a new upstream contribution.

## Phase 3 — Exhaustive literature protocol

Exact requests, response SHA256/UTF8 byte counts, access outcomes and concise original summaries
are saved in [web0](../evidence/Roth.normOne/web-0.json),
[web1](../evidence/Roth.normOne/web-1.json), [web2](../evidence/Roth.normOne/web-2.json),
[web3](../evidence/Roth.normOne/web-3.json), [web4](../evidence/Roth.normOne/web-4.json),
[web5](../evidence/Roth.normOne/web-5.json), and [web6](../evidence/Roth.normOne/web-6.json).
Full third-party response/article bodies and signed download URLs are not archived.

| Required channel | Actual query / action | Result and limitation |
|---|---|---|
| General web: specific | `polynomial length l1 norm sum absolute coefficients multivariate integer polynomial` | Evertse–Győry primary book manuscript gives the exact multivariate integer length and the coefficient/support/product bounds, §4.1, p67, (4.1.7)–(4.1.8). |
| General web: general | `Wiener algebra discrete semigroup l1 convolution norm submultiplicative` | Primary functional-analysis notes give finite-sequence convolution and its ℓ¹ norm; broader coefficient-indexed convolution is the relevant abstraction. This does not identify all Wiener algebras with polynomials. |
| General web: aliases | `polynomial coefficient norm length height sum absolute values` | Distinguishes length (sum) from height (maximum); pinned mathlib's own polynomial norm module records this terminology and its other-Lp TODO. |
| `ask_chatgpt_math` | Unavailable; optional tool explicitly allowed to be skipped | No mathematical second opinion was fabricated. |
| Local references | Exact `normOne`/ℓ¹/triangle/submultiplicativity searches in `clean.tex`; lines437–497 read | §3 Lemma3 proof defines the coefficient sum and requires triangle/product/determinant estimates. [Excerpt](../evidence/Roth.normOne/local-literature.txt), [hash](../evidence/Roth.normOne/local-literature-source.json). |
| nLab | `site:ncatlab.org/nlab "l1" "norm"`; later `site:ncatlab.org/ncatlab "ell" "norm"` returned nLab p-norm | Relevant indexed p-norm definition and Banach-algebra convolution examples. Direct opens of p-norm and Banach algebra returned HTTP400 unsupported XHTML; search text remains evidence, not a claimed successful page load. |
| nCatLab namespace | `site:ncatlab.org/ncatlab "norm" "convolution"` | No relevant namespace-specific result. Category algebra results describe convolution multiplication, not a canonical replacement norm. No categorical restatement is supported. |
| Stacks Project | `site:stacks.math.columbia.edu polynomial sum absolute coefficients norm`; two more absolute-value searches | No exact coefficient-ℓ¹ definition hit returned. Search absence does not establish mathematical absence from Stacks. |
| MathOverflow | `site:mathoverflow.net polynomial length sum absolute coefficients norm`; specific-form web also found question465899 | That 2024 question defines coefficient-vector ℓ¹ for integer polynomials, confirming current usage; it is supplementary, not the primary source for the definition. Distinguish question303091's unit-circle integral L1 norm, which is another object. |
| Recent arXiv, five-year window | Explicit `after:2021-10-27 before:2026-10-28` coefficient-L1/length searches; follow-up exact-title search | Initial broad queries yielded irrelevant optimisation/complexity papers, recorded as non-evidence. Positive follow-up: Houben–Streng, arXiv2207.08915 (2022), primary paper §3.2 and Lemma3.4: complex coefficient ℓ¹ sum and submultiplicative estimate. PDF opened; publisher §3.2 checked. |

Primary sources used:

- [Evertse–Győry, *Effective Results and Methods for Diophantine Equations over Finitely Generated Domains*](https://math.unideb.hu/sites/default/files/upload_documents/version-210614_0.pdf),
  June2021 manuscript, printed p67 (PDF page86 zero-based), §4.1, (4.1.7)–(4.1.8).
- [Feichtinger, Functional Analysis notes](https://www.univie.ac.at/NuHAG/FEICOURS/ws1314/FAws1314Fei.pdf),
  p34, finite sequences/polynomial Cauchy product and coefficient ℓ¹ submultiplicativity.
- [Houben–Streng, *Generalized class polynomials*](https://arxiv.org/abs/2207.08915), 2022,
  §3.2 and Lemma3.4; [published primary version](https://link.springer.com/article/10.1007/s40993-022-00400-2).

Synthesis: the exact integer multivariate concept is standard. Standard coefficient ℓ¹ sums
also exist over complex/normed coefficient spaces and arbitrary discrete supports. The finite
sum formula is elementary; the substantial reusable mathematics lies in its compatible norm,
convolution, functoriality, and bound API. The literature does not license replacing a sum
norm by a coefficient maximum or by a Banach completion.

## Phase 4a–4b — Generality, verified rather than guessed

| Parameter / structure | Current form | Verified broader formula / boundary |
|---|---|---|
| Variables `σ` | Arbitrary `Type u` | Already unlimited in cardinality and universe; no `Fintype` to remove. |
| Coefficients | `ℤ` | `CommSemiring R` plus `Norm R` suffices to *define* the coefficient norm sum. A `SeminormedCommRing R` version was also checked; it is stronger than necessary for the formula. |
| Coefficient-size operation | Cast to ℝ, then absolute value | Existing `Finsupp.sum` accepts an arbitrary `size : R → S` with only `Zero R` and `AddCommMonoid S`. The index may be any `ι`, not just polynomial exponents. |
| Codomain | `ℝ` | Arbitrary additive commutative monoid for the generic aggregation, or ℝ for a norm value. Generic aggregation alone is not a norm. |
| Exponents | `σ →₀ ℕ` through `MvPolynomial` | Arbitrary support index works for the coefficient aggregation; multiplication then needs its own monoid/convolution compatibility. Not a theorem weakening about unchanged polynomial multiplication. |
| Zero coefficients | Omitted by finite support | For the concrete size operation `size 0 = 0`. Arbitrary size functions still define a support sum, but require zero preservation for padding/support-change lemmas. |

The formula is **STRICTLY NARROWER THAN STANDARD** at the data-construction level, with native
verified recoveries, not an untested guess:

```lean
noncomputable def arbitraryNorm {σ R : Type*} [CommSemiring R] [Norm R]
    (P : MvPolynomial σ R) : ℝ := ∑ d ∈ P.support, ‖P.coeff d‖

noncomputable def finiteCoefficientSize {ι R S : Type*} [Zero R] [AddCommMonoid S]
    (size : R → S) (f : ι →₀ R) : S := f.sum fun _ c ↦ size c
```

The second is merely a scratch name for an **already-existing one-call construction**.
Native `recoverFromFinsupp` gives the original integer formula by `rfl`; `recoverFromNorm`
uses only unfolding and `Int.norm_eq_abs`. [Exact generality source](../evidence/Roth.normOne/native-generality-executed.lean.txt),
[receipt](../evidence/Roth.normOne/native-generality-success.json),
[generality record](../evidence/Roth.normOne/generality.json).

No weaker normed-ring axioms, full convolution norm structure, arbitrary weighted norm, or
complete downstream generalisation is claimed verified. Those are separate API developments.
The verdict is NO-composable rather than YES-generalise because the proposed formula itself
already composes from existing mathlib; implementation cost is not the reason.

## Phase 4c — All nine modern-idiom diagnostics

| # | Diagnostic | Finding / concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of bundled preambles | Yes for coefficient norm abstraction: existing `Norm R`/seminormed hierarchy replaces ℤ-specific absolute value; checked integer recovery. No new global norm instance is warranted by a scalar sum definition. |
| 2 | Filters/nets rather than metric sequences | No: a finite algebraic aggregation, no convergence premise or argument. |
| 3 | Universal-property characterization | No needed change: polynomials' free-algebra structure does not determine their coefficient L1 norm without additional size data. |
| 4 | Bundled substructures | Potential later `AddGroupSeminorm`/`RingSeminorm` or `WithLp` norm structure would expose triangle/product APIs, but such bundles are not constructed here. Existing metric-to-zero bridge is independently verified; do not pretend a scalar functional is already a bundled norm. |
| 5 | Module/(semi)ring hierarchy | Yes: formula needs only `CommSemiring R` and `Norm R`; the raw Finsupp formula needs still less. Specific norm properties need corresponding axioms. This enables integer/real/complex coefficient formulas without parallel ad hoc definitions. |
| 6 | Higher category | No relevant categorical content or downstream improvement identified. |
| 7 | Concrete indices/scalars | Yes: coefficient index can be arbitrary `ι`; existing Finsupp aggregation is not tied to natural exponents. This supports monoid-algebra coefficient norms but does not establish their multiplication bounds. |
| 8 | Concrete-via-abstract | Yes: the body never uses integer arithmetic beyond the coefficient-size map. `Finsupp.sum` is the abstract operation, and exact `rfl` recovery demonstrates the concrete specialization. Four native consumer replays check usable consequences, beyond renaming the expression. |
| 9 | False-generalisation guard | Pass for the exact recoveries. Arbitrary `Norm R` is only notation/data and does not imply positivity or triangle inequality. A maximum coefficient, integral value norm, Mahler measure, or completed Wiener algebra changes the object and is rejected as a replacement. |

Modern-idiom verdict: use the existing Finsupp coefficient aggregation for the construction;
consider a separately designed general L1 algebra API for substantive upstream bounds. Do not
create a competing global polynomial `Norm` instance merely to abbreviate this project function.

## Phase 4.5 — Six infrastructure risks for this definition

| # | Risk | Assessment and actual evidence |
|---|---|---|
| 1 | Typeclass diamond | **NONE** introduced: result is a scalar function; existing ℤ/ℝ structures and the existing wrapped Finsupp metric are synthesized in scratch, with no global new instance. A future direct polynomial norm instance would need a separate compatibility audit. |
| 2 | Reducibility leak | **LOW**: ordinary noncomputable `def`, no `@[reducible]`; original expansion and the Finsupp replacement both close by `rfl`. It is intentionally transparent when unfolded; naming does not provide opacity. |
| 3 | Non-canonical unfolding | **LOW**: the def is not a simp theorem; `simp [normOne]` explicitly unfolds to a finite sum. No hidden alternative polynomial evaluation/maximum is selected. Four native caller replays test the transparent replacement. |
| 4 | Instance priority collision | **NONE**: not an instance, no priority declaration or registration. The scratch metric Fact is local and witnesses `1 ≤ 1`, not a new permanent instance. |
| 5 | Universe polymorphism | **NONE** found: native full type has arbitrary `Type u`; concrete and lifted-index probes compile. Codomain ℝ is fixed intentionally and does not force the variable universe down to zero. |
| 6 | Coercion ambiguity | **LOW**: the explicit ℤ→ℝ cast and absolute value are unambiguous. No `CoeFun`/`CoeSort` is declared. `P.coeff` is the existing Finsupp projection; its `.sum` yields the same function by `rfl`. Norm spelling is reconciled by `Int.norm_eq_abs`. |

Overall **LOW**, no HIGH rows. This is a check of the actual scalar definition, not an unsupported
assertion that arbitrary future normed-algebra implementations would be diamond-free.

## Phase 4.6 — All five proof-strategy rows

This declaration constructs data, with no mathematical proof body. Its downstream proof strategy
is nonetheless assessed because that is the API design signal.

| # | Required strategy question | Result |
|---|---|---|
| 1 | ε–δ versus filters | No analytic limit proof. |
| 2 | Elements versus ideals/submodules | No ideal/submodule argument; coefficient Finsupp aggregation is already the appropriate data-level abstraction. |
| 3 | Sequences versus nets | No sequence or limit argument. |
| 4 | Construction versus universal property | A norm value is prescribed by coefficient data; a free-algebra universal property alone cannot recover it. |
| 5 | Missing helper API | No helper needed to construct the value: `Finsupp.sum` suffices. A generic convolution L1 ring-seminorm and its Hasse bounds may be valuable independent additions; no absence claim follows from this scalar definition alone. |

**REFACTOR-RECOMMENDED for an upstream proposal:** reuse `Finsupp.sum` and the existing metric
construction, rather than add an integer-only public definition. Cost: CHEAP for the value;
a bundled convolution norm API is separate work, not a reason to suppress a valid theorem.
Keep the local name for readability under the current production freeze.

## Phase 5 — Actual five-method mathlib searches

[Combined formal receipts](../evidence/Roth.normOne/formal-search.json) contain twelve actual
calls: three forms for each API method. All raw results are preserved, including near-misses.

| Method | Current / literature / abstract queries | Result |
|---|---|---|
| Finder | integer multivariate coefficient absolute sum / finitely-supported L1 norm / WithLp Finsupp distance sum | Current hit Gauss norm and Mahler measure are different; general hits `PiLp.norm_eq_of_L1`, `lp.norm_rpow_eq_tsum`; distance results mostly finite PiLp, not the needed arbitrary Finsupp index. |
| Loogle | `MvPolynomial, "norm"` / `Finsupp, "sum", "norm"` / `WithLp, "dist"` | No exact integer multivariate norm definition returned; hits include unrelated Noether normalization and inner-product formulas, plus WithLp distance API. These are not accepted as exact matches. |
| LeanSearch | exact coefficient-sum concept / L1 of finitely supported function / WithLp-one distance sum | Found coefficient primitives, Mahler-bound sum usage, `lp.norm_eq_tsum_rpow`, finite PiLp metric formulas. Native/source verification determines applicability. |
| `rg` pinned source | normOne/oneNorm/l1Norm / polynomial coefficient norm & length / Finsupp sum, distance and L1 normalization | Positive actual construction is generated `Finsupp.sum`; pinned Finsupp Lp file has a metric, not a normed-group instance. Polynomial norm TODO explicitly distinguishes ℓ¹ from implemented sup norm. [Current](../evidence/Roth.normOne/rg-current.json), [literature](../evidence/Roth.normOne/rg-literature.json), [abstract](../evidence/Roth.normOne/rg-abstract.json). |
| Local name search | normOne / Finsupp.dist_def / lp.norm_eq_tsum_rpow | Source fallback found the project and positive source names, but each result says **index unavailable**. This is not an indexed proof of absence; native checks and source archives supply the positive evidence. |

Positive pinned source locations, independently read:

- `Finsupp.sum`, generated by `@[to_additive]` from `Finsupp.prod`:
  `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:47–49`.
  [Exact module](../evidence/Roth.normOne/mathlib-finsupp-bigoperators.lean.txt).
- `MvPolynomial.support` at `Mathlib/Algebra/MvPolynomial/Basic.lean:462–463` is precisely
  `P.coeff.support`; `MvPolynomial.sum_def` at519–522 relates the same aggregation spelling.
  [Exact module](../evidence/Roth.normOne/mathlib-mvpolynomial-basic.lean.txt).
- `Finsupp.dist_def` at `Mathlib/Analysis/Normed/Lp/Finsupp.lean:83–86`, together with
  `Finsupp.sum_mapRange_index`, gives an independently checked metric-to-zero realization.
  [Exact module](../evidence/Roth.normOne/mathlib-finsupp-lp.lean.txt).
- `Polynomial.supNorm`, `Mathlib/Analysis/Polynomial/Norm.lean:53`, is a coefficient maximum
  for a **univariate** polynomial, not this sum. The module's TODO at35–39 asks for other Lp norms.
  [Exact module](../evidence/Roth.normOne/mathlib-polynomial-norm.lean.txt).

Conclusion: **building blocks found; exact value is one-call composable**. No claim that mathlib
already supplies a fully bundled arbitrary-variable polynomial ℓ¹ ring norm is made. External
indexes may precede the pinned checkout; the native pinned proofs control this verdict.

## Phase 5.5 — Three statement-shape checks

**Normal form.** Equivalent exact forms are the finite support sum, `P.coeff.sum` with coefficient
absolute value, and the same sum of integer coefficient norms. The metric-to-zero form is a further
verified representation after wrapping coefficients in `WithLp 1`. An equality bridge should
normalise toward one chosen public API; do not build quadratic pairwise equivalences. For this
local library the named function remains readable; for the data construction use Finsupp.sum.
This is a definition, so an iff-RHS convention is n/a; all actual recovery equalities are explicit.

**Syntactic generality.** Tried norm-valued generic coefficients, arbitrary coefficient-size
aggregation, and L1 metric to zero; original type and a literal Finsupp aggregation are easiest
for existing finite-support algebraic proofs. A type synonym is appropriate if a new normed
structure is later designed. Replacing the scalar expression by bare `‖P‖` without proving which
polynomial norm instance is selected is rejected.

**Superfluous arguments.** `σ` determines exponents and cannot disappear; `P` supplies the
coefficients. There are no explicit typeclasses/hypotheses to delete. ℤ and ℝ are specialised
data choices, not unused proof assumptions. They can be generalised at the formula level as
verified in Phase4, but a production migration is outside this read-only assessment.

Overall **RESTATE-BEFORE-SHIP** for a proposed upstream integer-only def; no upstream statement
should be shipped unchanged. This observation does not authorize changing current Lean code.

## Phase 6.0 — Complete explicit caller and inline audit

**K=14 distinct production declarations**, all in `Roth/CoeffNorm.lean`, with **zero direct
external-to-file named callers**. This is not an occurrence count or an exhaustive opaque
kernel dependency closure. Inferred consumers through the public bound theorems remain real.
No `@[simp]` attribute is attached to the definition itself. Its zero theorem is simp-tagged,
and is separately assessed later in canonical order.
[Exact grep](../evidence/Roth.normOne/rg-callers.json),
[full-name search](../evidence/Roth.normOne/rg-full-name.json),
[structured callers](../evidence/Roth.normOne/callers.json).

| Caller, production lines | Usage and mechanical replacement plan |
|---|---|
| `normOne_nonneg`,50–51 | Scalar in conclusion; replace by coefficient aggregation; `Finset.sum_nonneg` proof unchanged. |
| `normOne_eq_sum_of_support_subset`,54–56 | Named sum on left; replace functional, retain `Finset.sum_subset` support-padding argument. |
| `normOne_monomial`,59–62 | Monomial value; restate support-expansion helper consistently, then same singleton simplification. |
| `normOne_zero`,66–67 | Rewrite `simp [normOne]` to `simp [replacement]`; same zero support. |
| `abs_coeff_le_normOne`,71–73 | Direct generic `Finsupp.single_eval_le_sum`, no new norm theorem needed. |
| `normOne_add_le`,77–82 | Replace both summands and sum result; same padded-support triangle argument. |
| `normOne_neg`,86–87 | Explicit definition unfolding becomes replacement unfolding. |
| `normOne_sum_le`,90–92 | Generic subadditive finite-sum API receives replacement and the replayed zero/add bounds. |
| `normOne_mul_le`,96–102 | Replace scalar functional and unfold at100; same monomial-convolution and finite-sum estimate. |
| `normOne_prod_le`,105–108 | Generic submultiplicative finite-product API receives replacement and corresponding bounds. |
| `normOne_le_card_mul`,113–115 | Unfold Finsupp.sum and apply `sum_le_card_nsmul`. |
| `normOne_det_le`,119–129 | Replace matrix-entry and determinant scalar values; keep permutation expansion and sum/product/negation bounds. |
| `normOne_hasseDeriv_le`,147–158 | Replace values and explicit unfolding at153; retain monomial/binomial estimate. |
| `abs_coeff_det_hasseDeriv_le`,258–272 | Only intermediate scalar at265 is directly named; substitute replacement plus consistently restated bound lemmas. Final coefficient-bound conclusion does not change. |

Inlining every raw support sum would worsen local readability; the **recommended local destination
is still `Roth/CoeffNorm.lean`**. This is the belongs-elsewhere distinction: no reason to submit
the ℤ-only one-line construction upstream, good reason to keep a semantic downstream abbreviation.
If later replacing it, the table covers every named consumer rather than silently deleting the API.

[Inline audit](../evidence/Roth.normOne/rg-inline.json) found no separate full coefficient-ℓ¹
definition. Diagonal coefficient/evaluation proofs sum absolute values of different quantities;
they are related estimates, not a duplicate definition. Each bound theorem receives its own
later assessment; this verdict does not automatically classify all normOne laws as redundant.

## Phase 6 — Actual composition and native supporting experiments

The actual one-call replacement is:

```lean
noncomputable def replacement (P : MvPolynomial σ ℤ) : ℝ :=
  P.coeff.sum (fun _ z ↦ |(z : ℝ)|)
```

This uses **one mathematical aggregation operation**, existing `Finsupp.sum`, plus existing
coefficient projection/cast/absolute-value operations. `normOne` and replacement are definitionally
equal, verified by `rfl`. It is not a newly proved norm axiom and not a closing `simp [many defs]`
argument incorrectly called a ≤3-lemma theorem proof. The metric bridge is **not** counted as
one of these ≤3 calls; it requires genuine normalization through zipWith/mapRange and sum support.

Four actual independently executed mathlib-only caller replays check nonnegativity, zero,
the individual coefficient bound, and the support-cardinality bound with this replacement.
The isolated source has `#check_failure Roth.normOne`, so it cannot use the imported project's
own norm or bound theorems circularly. [Raw source](../evidence/Roth.normOne/native-raw-executed.lean.txt),
[raw receipt](../evidence/Roth.normOne/native-raw-success.json).
A separate native context theorem proves `Φ normOne ↔ Φ replacement` by `Iff.rfl` for
**every predicate** on the functional. This verifies definitional transport of all fourteen
caller statements. [Context source](../evidence/Roth.normOne/native-context-executed.lean.txt),
[receipt](../evidence/Roth.normOne/native-context-success.json).

The other ten caller refactor rows are transparent-substitution plans, **not falsely claimed
full proof replays**. Exact definitional equality makes them compatible at the value level;
future coordinated deletion should still validate the entire affected module and dependents.

Supporting abstract experiment: for an arbitrary integer Finsupp, `dist` between its `WithLp 1`
image and zero equals the sum of integer absolute values. The proof identifies the distance
zipWith with a mapRange, uses the existing `Finsupp.dist_def` at exponent one and
`Finsupp.sum_mapRange_index`, then `dist_zero_right` and `Int.norm_eq_abs`. Instantiating the
coefficient Finsupp yields exactly `normOne`. The exponent parameter is NNReal in the pinned
Finsupp file; a **local** `Fact (1 ≤ (1 : ℝ≥0))` is supplied. This is a metric equality, not a
claim that a normed-group or normed-ring structure has already been installed there.
[Metric source](../evidence/Roth.normOne/native-metric-executed.lean.txt),
[metric receipt](../evidence/Roth.normOne/native-metric-success.json).

Infrastructure checks additionally verify `normOne` at `Unit`, arbitrary-universe `ULift Unit`,
existing ℤ/ℝ norms, `SeminormedCommRing ℤ`, wrapped lifted-index Finsupp `MetricSpace`, and
arbitrary/lifted `rfl` bridges. [Infrastructure source](../evidence/Roth.normOne/native-infrastructure-executed.lean.txt),
[receipt](../evidence/Roth.normOne/native-infrastructure-success.json).

Rejected preparation accounting: one target attempt lacked `CommSemiring` for a purported
seminormed-additive coefficient type; its exact source and labelled diagnostic note are retained,
but its full raw response was not retained and is **not reconstructed**. Three metric attempts
failed on missing NNReal notation, missing local Fact, and an unused simp argument. Three raw
attempts failed on missing real structure, then a real-order elaboration mismatch (an extra
import did not fix that mismatch); final expected-type `using!` elaboration fixed it. All six
metric/raw rejection sources and raw receipts are preserved separately. The accepted target,
generality, metric, raw, infrastructure, and context sets each have full clean native receipts.

Accepted exact native sets, rejected preparations, standard-axiom checks, and proof/source
hashes are listed in [verification](../evidence/Roth.normOne/verification.json). Warming or
partial LSP responses are not accepted as proof completion. Native prep failures remain
separate evidence, not accepted proofs, and no default heartbeat/recursion limit was raised.

## Phase 7 — Verdict, why, and actionable destination

**NO-composable-from-mathlib.** The exact ℤ-specific scalar construction is an instance of
`Finsupp.sum`, with a literal one-call replacement and a native `rfl` bridge. Literature confirms
the meaning and standard wider setting; source/API searches distinguish the genuine coefficient
L1 quantity from maximum norms and Mahler measure. Native generic recoveries and four raw caller
replays establish applicability, independently of the existence of the original project API.

The semantic one-line exemption is real: fourteen consumers benefit from the stable local name.
That supports retaining the definition downstream; it does not create missing upstream
construction mathematics. The recommendation does **not** rest on generalisation being expensive,
and does not conclude that useful submultiplicativity/Hasse/determinant lemmas are already
available in the optimal general form. Those statements require their own canonical assessments.

**Existing building blocks:** `Finsupp.sum`, generated in
`Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:47–49`; `MvPolynomial.coeff` and
`MvPolynomial.support` in `Mathlib/Algebra/MvPolynomial/Basic.lean`; integer cast/real absolute
value. Norm spelling uses `Int.norm_eq_abs` only for the alternate norm-valued presentation.

**Refactor plan if deleting the local wrapper later:** replace its value by the exact composition
above in all fourteen tabled consumers, update the explicit unfolding names in zero/negation/
product/cardinality/Hasse proofs, and restate dependent bound lemmas consistently. Four representative
proofs are actually replayed; all consumers are inventoried; there is no argument-order reversal
or theorem weakening. Run module and dependent validation for that future migration.

**Recommended destination and present action:** keep the semantic function in
`Roth/CoeffNorm.lean` while finishing the survey. For future upstream work, develop the substantive
general coefficient L1/Finsupp convolution norm API against existing WithLp infrastructure,
rather than submit this integer-only definition. Production Lean sources remain unchanged.
No reviewer contact, PR creation, or upstream submission is authorized or performed here.

## Phase 8 — Completion and preserved evidence

All applicable phases are complete. Def-specific one-line and six infrastructure checks are
included; no theorem-only prefilter was used. Required optional-tool/access/index limitations
are explicit. Supporting native exact sources/receipts, all formal-search returns, CLI receipts,
source/pin hashes, caller inventory, and report are in the Git-copy manifest.
No incomplete assessment is marked complete, and no intermediate Git checkpoint is created.

[Machine assessment](../evidence/Roth.normOne/assessment.json),
[overview entry](../evidence/Roth.normOne/overview-entry.json),
[current manifest](../evidence/Roth.normOne/copy-manifest.json),
[portable read-only validator](../evidence/Roth.normOne/validate.py).
