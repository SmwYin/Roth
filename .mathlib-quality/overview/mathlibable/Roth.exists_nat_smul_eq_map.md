# `Roth.exists_nat_smul_eq_map` — BORDERLINE-needs-human

Canonical declaration 171, `Roth/Separation.lean:380`. Full read-only overview and mathlibable assessment. Production sources and pins remain unchanged. Root acceptance is pending.

## Phase 0 — Doctor

All 17 freshly computed source/pin SHA256 values match the shared successful baseline (`lake build`, exit 0, 2467 jobs). [Fresh hash checks](../evidence/Roth.exists_nat_smul_eq_map/baseline-hashes.json), [manifest](../evidence/Roth.exists_nat_smul_eq_map/input-manifest.json), [baseline receipt](../evidence/Roth.exists_nat_smul_eq_map/baseline-build.txt). The entire declaring module and full sole source caller were read; the module separates polynomial variables and descends rational factors to integer factors. [Complete source](../evidence/Roth.exists_nat_smul_eq_map/source-context.lean.txt).

## Phase 1 — Exact mathematical content

For any multivariate rational polynomial, including zero and polynomials with infinitely many *available* variables, there is a positive natural number whose scalar multiple has integer coefficients. A polynomial itself has finite monomial support; no finiteness assumption on the variable type is required.

```lean
∀ {σ : Type u_2} (G : MvPolynomial σ ℚ),
  ∃ (N : ℕ) (U : MvPolynomial σ ℤ),
    0 < N ∧ (map (Int.castRingHom ℚ)) U = ↑N • G
```

This is the [full native type](../evidence/Roth.exists_nat_smul_eq_map/native-type.json), explicitly preserving both existential witness types and positivity. Surrounding `τ`, `Fintype τ`, and `DecidableEq τ` do not occur. The proof takes the product of reduced positive coefficient denominators over the support, obtains integer scaled coefficients by denominator divisibility, reconstructs the integral polynomial by a monomial sum, and checks every coefficient, including those outside support. It uses no project lemma. [Native type, full kernel print, axioms and canonical audit](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-original-audit-receipt.json). The target print is complete, 4639 characters, without printer elision; standard axioms are `propext`, `Classical.choice`, `Quot.sound`.

## Phase 2 — Preliminary checks

SMALL: a denominator-clearing helper, not a named theorem, new structure or listed main result. This does not reduce literature width. Phase2b is n/a: theorem rather than definition; proof length does not invoke the one-line-definition filter. No inherited verdict or prefilter shortcut was used.

## Phase 3 — Exhaustive literature

Exact requests, returned response hashes/bytes, access status and original summaries are recorded in [general web metadata](../evidence/Roth.exists_nat_smul_eq_map/web-1-metadata.json), [named-channel metadata](../evidence/Roth.exists_nat_smul_eq_map/web-2-metadata.json), [retries and recent arXiv](../evidence/Roth.exists_nat_smul_eq_map/web-3-metadata.json), and [primary-source access](../evidence/Roth.exists_nat_smul_eq_map/web-4-metadata.json). Full returned articles/search-result bodies are deliberately not archived. Returned locator query strings were stripped; exact requests and full unchanged response digests remain. No credential values are retained.

| Channel | Actual request | Result |
|---|---|---|
| General web, specific | `rational multivariate polynomial clearing denominators positive integer coefficients` | Standard finite denominator clearing; rational polynomial context. |
| General web, general | `localization polynomial ring common denominator finite coefficients` | Localization is the relevant abstract form. |
| General web, aliases | `Gauss lemma rational polynomial scalar multiple primitive integral polynomial` | Primitive rescaling is the adjacent stronger normalization step. |
| ChatGPT math MCP | Available tool inventory | n/a: `ask_chatgpt_math` unavailable; other channels not reduced. |
| Local references | `rg -n -i 'clearing denominator\|clear.*denominator\|primitive polynomial\|gcd of.*coeff' .mathlib-quality/references/clean.tex` | §2 lines420–422 explicitly clears denominators before dividing coefficient gcd. [Excerpt](../evidence/Roth.exists_nat_smul_eq_map/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab localization commutative ring polynomial ring` | Localization via universal property, fractions, commutative rings and modules. |
| nCatLab | `site:ncatlab.org/ncatlab localization polynomial denominators` | Returned out-of-namespace `/nlab` material, no distinct exact hit. Direct `/ncatlab/show/localization` access failed. Not evidence of absence. |
| Stacks | `site:stacks.math.columbia.edu polynomial localization denominators finite`; retry `site:stacks.math.columbia.edu "common denominator"` | Downloads returned; direct tag00CM accessed and supplies exact primary localization definitions. |
| MathOverflow | `site:mathoverflow.net polynomial clearing denominators localization`; retry `site:mathoverflow.net "clearing denominators" "polynomial"` | Concrete polynomial use in question396413 and general localization discussions. Supplementary context, not stronger primary theorem evidence. |
| Recent arXiv, five years | `site:arxiv.org "clearing denominators" "polynomial" after:2021-10-27 before:2026-10-28` | arXiv2610.13463,2026-10-09, rational certificates and a Lean formalization;2610.13463 concerns application rather than abstract generality. Old hits in the first general search were not counted as recent. |

Primary locators: [Stacks00CM](https://stacks.math.columbia.edu/tag/00CM), Definition10.9.1–2 and Proposition10.9.3; [Conrad, *The Gauss norm and Gauss’s lemma*](https://kconrad.math.uconn.edu/blurbs/ringtheory/gaussnormlemma.pdf), p.3 Lemma10 and p.1 Example6; [nLab localization](https://ncatlab.org/nlab/show/localization%20of%20a%20commutative%20ring), Definition and universal property; [recent arXiv abstract](https://arxiv.org/abs/2610.13463). Conrad's primitive normalization is adjacent mathematical context, not an assertion that the multiplier clearing all rational coefficients must be primitive or integral in that stronger statement.

Literature summary: the concept is clearing denominators; common denominators exist for finite collections of localized elements, and polynomial finite support makes this applicable without finitely many variables. Over a commutative ring localized at a multiplicative subset, a denominator from that subset clears any finite family; positivity is specific to the integer/rational presentation. The classical scalar-multiple/primitive-polynomial language and localization universal property organize the same denominator mechanism. No source supports replacing rational coefficients by arbitrary field elements without a localization relation, or requiring primitivity with an arbitrary positive integer multiplier.

## Phase 4a — Parameter and generality audit

| Parameter / feature | Current form | Broader or alternative form | Assessment |
|---|---|---|---|
| Variable type | `σ : Type*` | Arbitrary universe-polymorphic index | Already unrestricted; neither finite nor decidable equality class occurs. |
| Input | `MvPolynomial σ ℚ` | Polynomial over a localization `S` of `R` | Expanded representation through existing `IsLocalization`; not an unused-hypothesis deletion. |
| Output coefficients | `MvPolynomial σ ℤ` | `MvPolynomial σ R` | Same localization numerator interpretation. |
| Multiplier | Positive `N : ℕ` | Denominator in `M`, or image `M.map C` | Positivity is preserved by taking `M = Submonoid.pos ℤ`; signed nonzero denominators alone require an additional sign conversion. |
| Scalar action | `(N : ℚ) • G` | Constant-polynomial scalar action / multiplication | Algebra bridge must actually normalize; it is not silently treated as definitionally identical. |
| Conclusion | Equality with mapped integer polynomial | `IsLocalization.IsInteger` of a denominator multiple | Existing predicate is membership in the localization-map image. |
| Zero input | Included | Included | Empty denominator product is1; no nonzero hypothesis should be added. |
| Parent interface | Standard `MvPolynomial` and coefficient map | Existing localization interface | No project parent-definition migration or inherited verdict. |

## Phase 4b — Verified generality

The concrete statement has no typeclass assumptions to mechanically drop. Abstract ring localization and finite coefficient-family localization are expanded representations, not a claim that arbitrary rational scalar data can be replaced by an unrelated field. The generic targets are already supplied by `MvPolynomial.isLocalization` and `IsLocalization.exists_integer_multiple`, with the coefficient route `IsLocalization.exist_integer_multiples` over commutative semirings. Both expansions actually compile as `Clear171Generic.clear` (arbitrary commutative rings) and `Clear171Generic.finiteFamily` (commutative semirings) in the [accepted combined execution](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-combined-executed.lean.txt), [clean raw native receipt](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-combined-receipt.json). Thus the concrete coefficient representation is STRICTLY NARROWER THAN STANDARD under a verified localization expansion. No removable assumption was discovered within the fixed rational/integer statement. Since the expanded laws already exist, this is not a YES-generalise contribution.

## Phase 4c — All nine modern-idiom rows

| # | Question | Answer / formulation | Concrete downstream consequence |
|---|---|---|---|
| 1 | Typeclass preambles | Yes in expanded localization form: `[Algebra R S] [IsLocalization M S]`. | Generic clearing works for any instantiated localization. |
| 2 | Filters / topology | No: finite algebraic denominator clearing has no convergence. | None. |
| 3 | Universal property | Yes: use the existing localization characterization of the polynomial ring. | `IsLocalization.exists_integer_multiple` supplies the numerator without reconstructing coefficients. |
| 4 | Bundled substructures | Yes: `M : Submonoid R` and existing image/range predicate. | Submonoid maps and localization APIs encode denominator constraints. |
| 5 | Hierarchy | Yes: abstract commutative rings for polynomial localization; commutative semirings for finite coefficient-family clearing. | Other localizations use the same theorem; no field/domain instance required for the generic law. |
| 6 | Higher categories | No higher-categorical content needed for this elementwise existence law. | No proposed expansion. |
| 7 | Concrete index | `σ` already arbitrary. `ℕ` is a constrained multiplier witness, not a variable index. | Preserve positive-natural output in the original specialization. |
| 8 | Concrete-via-abstract diagnostic | Original proof uses `Rat.den` repeatedly and `Rat.num`, `Rat.den_mul_eq_num`, `Rat.den_pos`; the simple “concrete name disappears after unfolding” diagnostic does not fire. Independently, localization abstraction gives another proof. | Do not pretend the original proof is already abstract or infer weakening from identifier absence. |
| 9 | False-generalization guard | Require an actual localization relation. Dropping positivity makes `N=0,U=0` work for every input and destroys the intended clearing result. Infinite available variables remain valid because support is finite. | Preserve positivity, full mapped equality and arbitrary `σ`; do not confuse rational functions or infinite series with finitely supported polynomials. |

The modern formulation is already established in mathlib. `MvPolynomial.algebraMvPolynomial` is deliberately scoped locally: Eval.lean documents a diamond if made global. No new global algebra instance is proposed.

## Phase 4.5 — Infrastructure risks

n/a: theorem, not definition/class/instance. All six definition-only risks are n/a: typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe-polymorphism construction risk, coercion ambiguity. The existing local algebra instance's documented diamond is noted in Phase4c; this does not add that instance globally.

## Phase 4.6 — All five proof-strategy rows

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ vs filters | n/a, no topology. |
| 2 | Element proof vs abstract algebra | REFACTOR-RECOMMENDED: polynomial localization supplies numerator existence directly, avoiding support coefficient reconstruction. |
| 3 | Sequences vs nets | n/a, no limits. |
| 4 | Construction vs universal property | Existing polynomial localization is the structural route. |
| 5 | Missing helpers mathlib should have | Generic denominator-clearing laws already exist. Whether a positive-natural polynomial specialization is useful upstream is a separate API design question, not an absence claim about localization. |

The proposed strategy is to extract an existing localized numerator and normalize the constant scalar. Cost is cheap to moderate and does not determine the verdict.

## Phase 5 — All five actual methods on three forms

[Complete raw API search receipts](../evidence/Roth.exists_nat_smul_eq_map/formal-search-receipts.json) contain 12 actual requests: Finder, Loogle, LeanSearch, local each on current, standard finite common-denominator, and abstract polynomial-localization forms. [Exact CLI receipts](../evidence/Roth.exists_nat_smul_eq_map/source-search-receipts.json) contain all three source searches plus tracked and no-ignore caller checks, completing 15 formal-search cells.

| Method | Current rational polynomial | Literature finite family | Abstract polynomial localization |
|---|---|---|---|
| Finder | Nearby univariate normalization and scalar lemmas; no exact positive-natural theorem. | `IsLocalization.exist_integer_multiples`, `commonDenom`, finite variants. | `MvPolynomial.isLocalization`. |
| Loogle | `MvPolynomial.map, ℚ, ℤ` returns Witt-vector map lemmas, not this theorem. | `IsLocalization.IsInteger, _ • _` returns exact generic denominator law and finite variants. | `IsLocalization, MvPolynomial` returns polynomial localization instance and constant `mk'` compatibility. |
| LeanSearch | Coefficient/natural scalar facts rather than exact theorem. | Finite-family common denominator API. | `MvPolynomial.isLocalization`, `isLocalization_C_mk'`. |
| rg | Exact project target name absent in mathlib; exit1. | Integer.lean contains common denominator, finite clearing and mapped integer-multiple laws. | Localization.lean contains the exact image-of-constants localization instance. |
| Local | Project theorem and historical scratch names; not mathlib replacement candidates. | Finite denominator declarations present. | `MvPolynomial.isLocalization` present. |

All local calls report `index: unavailable`; returned lexical hits are useful, but empty results would not prove absence. External search indices can differ from the pin; the pinned source and successful native checks take precedence. Historical scratch occurrences were excluded from production caller counts.

Pinned positive candidates: `IsLocalization.exists_integer_multiple`, Integer.lean:82; `exist_integer_multiples`, Integer.lean:87; `MvPolynomial.isLocalization`, MvPolynomial/Localization.lean:44; positive-integer localization of `ℚ`, FractionRing.lean:82. [Pinned source hashes](../evidence/Roth.exists_nat_smul_eq_map/mathlib-inputs.json) and full archived source modules retain exact signatures. These provide genuine generic numerator existence, while the original natural witness and scalar equality require the independently tested bridge.

## Phase 5.5 — Statement shape

Normal forms: (1) mapped numerator equality with positive natural multiplier; (2) `IsInteger` for a denominator scalar multiple; (3) localization fraction representation. Mathlib's generic normal form is the second, with a denominator in a submonoid. The original equality is convenient for its actual consumer's coefficient rewrite. This is an existence theorem, not an iff whose normal form belongs on the RHS.

Syntactic alternatives attempted: generic `IsInteger` extraction, image-of-constants localization, and finite coefficient-family clearing. The exact original statement keeps positivity and uses natural-to-rational scalar action; the abstract denominator representation composes directly with localization. There are no superfluous hypotheses: `σ` names variables and `G` is the input. No `Finite`, `Fintype`, `DecidableEq`, nonzero, or domain instance should be added. Restatement is relevant only for upstream API selection, not a silent weakening of the actual theorem.

## Phase 6.0 — Full source callers and inline audit

| Caller | Use |
|---|---|
| `Roth/Separation.lean:410`, `Roth.exists_primitive_smul_eq` | `obtain ⟨N, U0, hN, hU0⟩ := exists_nat_smul_eq_map G`; positivity proves the mapped integral polynomial is nonzero and later proves the rescaling scalar is nonzero. |

One explicit body use, in the declaring file; zero external-to-file uses and zero statement uses. The command's file-excluding internal-use count is0; total project explicit-use count is1. Fresh canonical-inventory lexical enumeration, tracked `git grep`, and `rg --no-ignore` scoped to all production sources agree. [Lexical audit](../evidence/Roth.exists_nat_smul_eq_map/lexical-enumeration.json), [CLI audit](../evidence/Roth.exists_nat_smul_eq_map/source-search-receipts.json). The independent kernel-value audit examines all 293 canonical declarations, preserves private names and exact order, and finds the sole direct consumer `Roth.exists_primitive_smul_eq`. This count is not a transitive/simp dependency closure. No duplicate inline support-product denominator proof occurs elsewhere in production.

## Phase 6 — Actual composition experiments

Attempt1: specialize the existing polynomial-localization law. `Clear171Generic.clear` is exactly `IsLocalization.exists_integer_multiple (M.map (C (σ := σ))) G`, with mathlib's existing local algebra instance. This succeeds natively with no project imports or target constant. It proves the generic `IsInteger` form, not the exact positive-natural output spelling.

Attempt2: use `IsLocalization.exist_integer_multiples` on finite coefficient support. The generic finite-family theorem compiles as `Clear171Generic.finiteFamily`; reconstructing an integer polynomial and checking its mapped coefficients would still be a genuine proof. The original support-product proof likewise exceeds three existing calls.

Attempt3: recover the exact original form from localization at positive integer constants. The accepted `ClearDenoms171.originalProbe171` extracts a positive integer `n`, sets `N = n.natAbs`, proves the integer and rational cast equalities explicitly, and normalizes polynomial algebra maps and scalar multiplication. It requires `Int.natAbs_of_nonneg`, `congrArg`, `Int.cast_natCast`, `Int.natAbs_pos`, algebra-map and constant-polynomial normalization, and final `smul_eq_C_mul`; this is a real proof, not a three-call term. [Exact first accepted original-form execution](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-probe-executed.lean.txt), [receipt](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-probe-receipt.json). Four rejected drafts are preserved separately in verification metadata: wrong explicit arguments, an unknown integer alias, failed `mod_cast` natural-absolute-value conversion, and an unknown `Int.eq_intCast` spelling. These failures are not evidence of absence and none is accepted proof evidence.

The [combined mathlib-only execution](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-combined-executed.lean.txt) and [complete clean receipt](../evidence/Roth.exists_nat_smul_eq_map/clear-denoms-combined-receipt.json) use exactly14 imports and guard the absent project target with `#check_failure`. They verify the exact original positive-natural statement, both generic forms, the entire sole caller proof with only its invocation replaced by the accepted helper, and both semantic guards. All six named declarations have standard axioms and no warnings, errors, timeouts, unsafe proof mechanism or recovered `sorryAx`. The caller uses positivity to obtain nonzero rescaling; the remaining original source proof is unchanged. Zero input allows `N=1,U=0`; deleting positivity permits the vacuous `N=0,U=0` construction.

Conclusion: No verified ≤3-existing-call exact-original-form replacement found. Its generic mathematical content is established existing API. The cast/scalar bridge has actual proof content, so this assessment does not issue NO-mathlib-has-it on semantic overlap, or NO-composable by counting closing `simp` as one call. Phase6b explicitly treats trivial `simp [defs...]` bridges as BORDERLINE; this verified bridge is at least that substantial.

## Phase 7 — Verdict gate

**BORDERLINE-needs-human.** The general denominator-clearing result is already in mathlib, and the exact positive-natural specialization is useful at the sole caller. The accepted replacement isolates the remaining API question: whether this concrete output packaging and its natural/cast/scalar normalization deserve an upstream theorem, a broader numerator bridge, or only a project-local helper. Neither a new generic mathematical gap nor a strict short existing-call replacement has been demonstrated. This is an API-design judgment supported by completed verification, not unresolved correctness, failed searches, cost, or a blanket parent re-aim rule.

1. Should mathlib expose a positive-natural integral-multiple theorem for rational `MvPolynomial`s, preserving `N : ℕ`, integer coefficients and arbitrary variables, in a rational-specialization module?
2. Would maintainers instead prefer a generic coefficient-scalar numerator theorem over `[IsLocalization M S]`, bridging constant-polynomial denominators to `map (algebraMap R S) U = s • G`, near `Mathlib/RingTheory/MvPolynomial/Localization.lean`?
3. If neither API spelling is wanted upstream, should the accepted localization proof remain a local integrality helper in `Roth/Separation.lean` or be inlined at `exists_primitive_smul_eq:410`?

These are concrete future upstream/API questions; no user response is needed to complete this read-only assessment. Production is unchanged. Keep the helper pending an API choice. If choosing local inlining, replace the sole `obtain` with the accepted localized numerator extraction, retain its positivity and exact map equality, then leave the caller's remaining proof intact; the full caller experiment verifies this route. There are no other explicit callers to update. The natural scalar normalization is not claimed definitionally equal, and no new global polynomial-algebra instance should be installed.

## Phase 8 — Completed handoff

All required phases pass; definition-only phases are explicitly n/a. Unresolved verification obligations: none. [Verification index](../evidence/Roth.exists_nat_smul_eq_map/verification.json), [assessment metadata](../evidence/Roth.exists_nat_smul_eq_map/assessment.json), [overview entry](../evidence/Roth.exists_nat_smul_eq_map/overview-entry.json), [portable validator](../evidence/Roth.exists_nat_smul_eq_map/validate.py). The current copy manifest covers exact executed sources and complete receipts, search evidence, source/pin hashes and the exact293 canonical-name audit. Root independently reviews and integrates the frozen package; this worker does not change production, Git or progress records.
