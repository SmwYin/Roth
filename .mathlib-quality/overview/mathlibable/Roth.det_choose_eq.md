# Roth.det_choose_eq — full mathlibable assessment

Canonical declaration 43, `Roth/Wronskian.lean:79`. **Recommended verdict: YES-but-generalise-first**. This is an independent assessment; the Wronskian definitions' earlier BORDERLINE verdicts do not decide a scalar binomial determinant theorem.

## Phase 0 — baseline and exact declaration

The shared `lake build` completed successfully (2467 jobs). All 17 current production-source and pin hashes were freshly compared with the baseline manifest and match. The entire declaring module and its sole explicit caller were read. Source and pins remain unchanged. The native target replay resolves the theorem and compiles its exact proof with no warnings/errors, `partial=false`, and only `propext`, `Classical.choice`, `Quot.sound`.

Evidence: [baseline](../evidence/Roth.det_choose_eq/baseline-build.txt), [fresh hashes](../evidence/Roth.det_choose_eq/source-pin-hashes.json), [source](../evidence/Roth.det_choose_eq/source-wronskian.lean.txt), [native complete receipt](../evidence/Roth.det_choose_eq/native-target-success.json), [native selected type/signatures](../evidence/Roth.det_choose_eq/native-target-extract.json).

Full native elaborated type, with pretty-printer coercions preserved:

```lean
@Roth.det_choose_eq : ∀ {K : Type u_1} [inst : Field K] {l : ℕ} [CharZero K] (d : Fin l → ℕ),
  (Matrix.of fun μ ν ↦ ↑((d ν).choose ↑μ)).det =
    (∏ μ, (↑(↑μ).factorial)⁻¹) * ∏ i, ∏ j > i, (↑(d j) - ↑(d i))
```

## Phase 1 — mathematical content and proof

For any natural numbers `d₀,…,dₗ₋₁`, over a characteristic-zero field, the determinant of the matrix with entry `choose(dν,μ)` is the Vandermonde product of the `dν`, divided by `0!1!⋯(l−1)!`. Distinctness or increasing order of the `dν` is unnecessary; repeated values make both sides zero. The empty family is included.

`K` supplies commutative determinant arithmetic and inverses; `CharZero K` makes every natural factorial nonzero; `l` fixes the ordered finite square index; `d` supplies natural binomial tops. No project definition occurs in the type or proof.

The proof rewrites each binomial as the evaluation of the monic falling-factorial polynomial divided by its row factorial. It proves a matrix equality by extensionality, removes row factors from the determinant, transposes, applies mathlib's monic polynomial evaluation determinant theorem, and expands the Vandermonde determinant. Thus the core generic determinant law is already in mathlib; the binomial normalization remains a substantive representation bridge.

## Phase 2 — preliminary checks

**BIG**, because the theorem is explicitly listed under the module's main results. This is a narrative classification, not a literature-search shortcut. One-line definition test: **n/a, theorem**. Its proof has ten substantive source lines, including a matrix equality proof; definition-only defeq/diamond/API exemptions do not apply.

## Phase 3 — exhaustive literature protocol

Every named channel was executed or explicitly marked unavailable. Exact requests, returned response SHA256/byte counts, URLs and access statuses are in [web metadata](../evidence/Roth.det_choose_eq/webgeneral-metadata.json), [named channels 1](../evidence/Roth.det_choose_eq/named1-metadata.json), [named channels 2](../evidence/Roth.det_choose_eq/named2-metadata.json), [direct opens](../evidence/Roth.det_choose_eq/opens-metadata.json), [primary locators](../evidence/Roth.det_choose_eq/primary-metadata.json). Bodies of articles and search results were not archived. The [literature ledger](../evidence/Roth.det_choose_eq/literature.json) records original concise summaries and exact locators.

| Channel | Actual query/access | Finding |
|---|---|---|
| General web, specific | `determinant binomial coefficients Vandermonde product factorial polynomial` | Binomial/Vandermonde specialization; led to exact primary comment below. |
| General web, general | `determinant polynomial evaluation matrix product leading coefficients Vandermonde` | Standard graded-polynomial evaluation determinant. |
| General web, aliases | `Krattenthaler advanced determinant calculus binomial determinant falling factorial` | Located Krattenthaler's primary survey. |
| ChatGPT MCP | n/a: `ask_chatgpt_math` unavailable | No second-opinion response claimed. |
| Local `clean.tex` | `rg -n -i 'Vandermonde\|binom\|Wronskian\|factorial'` | §2 first lemma, lines184–194, exact formula and degree/leading-coefficient explanation. |
| nLab | `site:ncatlab.org/nlab Vandermonde determinant polynomial evaluation`; direct determinant/Vandermonde opens | Search exposes abstract determinant context. Direct opens fail400, unsupported XHTML; no unread page theorem claimed. |
| nCatLab | `site:ncatlab.org Vandermonde binomial determinant`; direct `/ncatlab/show/Vandermonde+determinant` | Search returns nLab material; direct path inaccessible. No separate categorical refinement found. |
| Stacks | `site:stacks.math.columbia.edu Vandermonde determinant`; direct search and tag0FJ9 | Search endpoint inaccessible. §15.120 was read: determinants of finite projective modules, no binomial formula. |
| MathOverflow | `site:mathoverflow.net determinant binomial coefficients Vandermonde factorial`; question198111 | Jason Starr's 2015-02-21 17:53 comment gives factorial product times binomial determinant equals Vandermonde; Newton basis explains the identity. |
| arXiv, last five years | `site:arxiv.org Vandermonde polynomial evaluation determinant after:2021-10-26 before:2026-10-27` | Jitman–Rungrottheera, submitted2026-01-24, arXiv2601.17626: related homogeneous bivariate evaluation determinants and finite-field bounds; no exact replacement. Older returned hits excluded. |

Primary mathematical anchor: [Krattenthaler, *Advanced Determinant Calculus*, Proposition1, equation(2.2), PDF page5](https://www.mat.univie.ac.at/~slc/wpapers/s42kratt.pdf) states the evaluation determinant for polynomials of successive degrees as product of leading coefficients times Vandermonde. [MathOverflow question198111, Starr comment](https://mathoverflow.net/questions/198111/invertibility-of-a-matrix-whose-entries-are-certain-binomial-coefficients) records the exact factorial-multiplied binomial form. The local reference independently supplies the precise quotient form used in Roth's proof. These are compatible forms, not competing identities. The ring formulation must use actual binomial values or valid integer-valued evaluation; it does not license arbitrary total division by zero.

## Phase 4a–b — parameters and verified generality

| Parameter or hypothesis | Essential role | Result of investigation |
|---|---|---|
| `K : Type u` | Scalar carrier | Already universe-polymorphic. |
| `[Field K]` | Commutative arithmetic, determinant, inverse factorials | Preserved in the same-RHS quotient weakening. Arbitrary commutative rings require multiplication by factorials instead of unlicensed cancellation. |
| `[CharZero K]` | Nonzero factorial casts | Stronger than necessary: native-verified replacement `hf : ∀ μ : Fin l, ((μ : ℕ).factorial : K) ≠ 0`. |
| `{l : ℕ}` | Square matrix size and row degrees | Arbitrary, including zero. Replacing `Fin l` by an unordered finite type requires an enumeration/sign convention and does not simply drop a hypothesis. |
| `d : Fin l → ℕ` | Natural binomial coefficients | No injectivity, monotonicity, positivity or degree bound required. Replacing natural tops with arbitrary field points means using falling-factorial polynomial evaluation; that generic law already exists. |

**STRICTLY NARROWER THAN STANDARD**, with a verified local weakening of the global characteristic-zero assumption. The exact original RHS and all other binders survive under local factorial nonvanishing. No Wronskian parent-interface change is needed. The extra helper `local_choose` is a new proof copied from the public conversion theorem with the weaker local premise; it is not misrepresented as an existing mathlib replacement. See [accepted isolated source](../evidence/Roth.det_choose_eq/native-factorial-executed.lean.txt) and [receipt](../evidence/Roth.det_choose_eq/native-factorial-success.json).

Proposed same-form public signature:

```lean
theorem Matrix.det_choose_of_factorial_ne_zero {K : Type*} [Field K] {l : ℕ}
     (d : Fin l → ℕ) (hf : ∀ μ : Fin l, ((μ : ℕ).factorial : K) ≠ 0) :
     (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det =
       (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) *
         ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i)
```

Cost: moderate, localized proof adjustment already demonstrated. Cost does not determine the verdict. A stronger cancellation-free statement over **every commutative ring**, including the zero ring, was also natively compiled:

```lean
theorem Matrix.factorial_mul_det_choose {R : Type*} [CommRing R] {l : ℕ}
    (d : Fin l → ℕ) :
    (∏ μ : Fin l, ((μ : ℕ).factorial : R)) *
      (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : R)).det =
        ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : R) - d i)
```

[Exact accepted ring/characteristic source](../evidence/Roth.det_choose_eq/native-ring-executed.lean.txt) and [complete success receipt](../evidence/Roth.det_choose_eq/native-ring-success.json) verify the formula, the `ZMod 2` size2 quotient specialization, and the size3 counterexample to dropping the factorial condition. At size3 with `d ν = ν.val`, the binomial matrix determinant is1 while the inverse-factorial RHS is0. This is a strict weakening, not a vacuous restatement. No general claim that `p ≥ l` automatically synthesizes the premise is made without a separately compiled characteristic-arithmetic lemma.

The cancellation-free identity is the preferred ring-level primary statement, and the local-factorial quotient formula remains its field corollary. They encode the same integral normalization; quotient recovery requires the explicitly stated nonzero premise. This expanded representation is distinguished from the identical-RHS hypothesis weakening above.

The first ring proof hit an unnecessarily strong pinned API assumption: `monic_descPochhammer` and `descPochhammer_natDegree` require `NoZeroDivisors R`. The accepted proof transfers monicity and degree from `ℤ` via `Int.castRingHom R`, `Monic.map`, `Monic.natDegree_map`, and `descPochhammer_map`, then applies the existing commutative-ring evaluation law. The zero-ring case is handled by `nontriviality R`. Thus no domain assumption is retained just to satisfy an overly narrow supporting lemma. Rejected native experiments are archived separately.

## Phase 4c — all modern-idiom questions

| # | Question | Answer, proposed form and concrete downstream effect |
|---|---|---|
| 1 | Typeclass preambles | Already uses standard `Field` and `CharZero`; local factorial nonvanishing is naturally a value hypothesis depending on `l`, not a new global class. |
| 2 | Filters/topology | No; finite algebraic determinant identity has no limiting argument. |
| 3 | Universal-property construction | No new object is constructed. Evaluation matrix and determinant already have their mathlib APIs. |
| 4 | Bundled substructures | No closure predicates or substructures occur. |
| 5 | Weaker algebraic hierarchy | Yes: local factorial nonvanishing admits suitable positive characteristic; multiplication-by-factorials form additionally removes division and field assumptions. This serves `ZMod` and commutative-ring evaluation arithmetic. |
| 6 | Higher categories | No; categorifying determinant lines would change the target use and supply no missing binomial conversion. |
| 7 | Concrete indices | `Fin l` is the canonical degree ordering. Arbitrary natural tops already allowed. General scalar evaluation nodes are handled by the existing monic polynomial law. |
| 8 | Concrete-via-abstract diagnostic | Fires after normalization: the `choose` identifier disappears from the final determinant-rewrite chain. The remaining content is precisely `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde` applied to `descPochhammer`, with degree and monicity witnesses. The abstract candidate was actually compiled by one existing call. Do not propose a new generic evaluation theorem. The entrywise and row-scaling bridge still needs proof. |
| 9 | False-generalization guard | Local nonzero factorials preserve the exact quotient identity; completely dropping their role is false in characteristic2 at size3. Multiplying through by factorials preserves a valid integral identity but loses recoverability of the quotient when the factor vanishes; clearly distinguish these representations. |

Modern-idiom verdict: use the existing generic polynomial-evaluation law, and improve the scalar hypotheses of the binomial specialization. The new contribution is public, characteristic-aware binomial normalization, not a duplicate abstraction.

## Phase 4.6 — all proof-strategy rows

| # | Strategy question | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a, no topology. |
| 2 | Elements versus substructures | No ideal/submodule inclusion can replace this scalar determinant calculation; matrix extensionality is appropriate for the representation bridge. |
| 3 | Sequences versus nets | n/a, finite algebra. |
| 4 | Construction versus universal property | n/a, no constructed categorical object. |
| 5 | Missing helpers mathlib should have | The adjacent private falling-factorial/binomial determinant bridge is the precise public API gap; local-nonzero conversion may be a useful supporting lemma. The arbitrary-ring proof also exposes unnecessarily strong `NoZeroDivisors` assumptions in the monicity/degree Pochhammer API; mapping from ℤ removes them in the accepted probe. The generic monic evaluation theorem already exists. |

Current strategy: **MATHLIB-IDIOMATIC**; recommended API change is the verified hypothesis weakening and a cancellation-free primary form. No monolithic new determinant proof is proposed.

## Phase 4.5 — infrastructure risk

n/a — theorem. Each of the six infrastructure rows (typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe issues, coercion ambiguity) is n/a because this declaration introduces neither data/definitional equality nor an instance/coercion path. Ordinary theorem statement coercions were checked in the native replay.

## Phase 5 — five actual methods on all three forms

Raw complete requests and responses: [current](../evidence/Roth.det_choose_eq/formal-current.json), [literature-standard](../evidence/Roth.det_choose_eq/formal-literature.json), [abstract](../evidence/Roth.det_choose_eq/formal-abstract.json). Pinned source searches: [current](../evidence/Roth.det_choose_eq/rg-current.json), [literature](../evidence/Roth.det_choose_eq/rg-literature.json), [abstract](../evidence/Roth.det_choose_eq/rg-abstract.json). External indices may use different mathlib revisions; all positive candidates were checked against pinned source and native signatures.

| Method | Current binomial determinant | Literature polynomial evaluation | Abstract monic evaluation |
|---|---|---|---|
| Finder | Semantic query returns Vandermonde, divisibility and monic evaluation candidates | Returns monic evaluation and evaluation-matrix factorization | Exact abstract theorem found |
| Loogle | `Matrix.det, Nat.choose`: empty | `Matrix.det, Polynomial.eval`: partial hits including exact monic theorem | `"det_eval_matrixOfPolynomials"`: exact theorem |
| LeanSearch | Binomial/Vandermonde query returns Vandermonde and divisibility, no direct public binomial formula | Polynomial-evaluation query returns generic blocks | Exact abstract theorem |
| `rg` | Full untruncated binomial/determinant source scan finds **private** integer bridge | Evaluation/factorization laws in Vandermonde and coefficient matrix in Block | Exact full-name source hit at Vandermonde280 |
| Local name index | `det_choose` finds project theorem; `index=unavailable` | `det_eval` source/index results recorded; `index=unavailable` | Exact candidate source result; `index=unavailable` |

Local-index unavailability does not prove absence. Search failures do not prove absence. The positive pinned public API consists of `Nat.cast_choose_eq_descPochhammer_div`, `Polynomial.descPochhammer_natDegree`, `Polynomial.monic_descPochhammer`, `Matrix.det_mul_column`, `Matrix.det_transpose`, `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`, `Matrix.det_vandermonde`. [Source hashes](../evidence/Roth.det_choose_eq/mathlib-source-hashes.json) and full [Vandermonde source](../evidence/Roth.det_choose_eq/source-mathlib-vandermonde.lean.txt)/[Pochhammer source](../evidence/Roth.det_choose_eq/source-mathlib-pochhammer.lean.txt) pin those observations.

`Matrix.of_eval_descPochhammer_eq_mul_of_choose` at Vandermonde301 is **private**, integer-valued, and oriented as evaluation rows. It cannot be cited as an accessible public theorem. The adjacent public `Matrix.superFactorial_dvd_vandermonde_det` gives divisibility, not the specified quotient. The generic monic law is fully reusable, but its conclusion is an evaluation determinant before binomial normalization. No claim is made that a failed search exhausts all possible proof terms.

## Phase 5.5 — statement shape

Normal forms considered: inverse-factorial product times difference product; quotient by factorial product; factorial product times binomial determinant equals Vandermonde; polynomial evaluation determinant equals Vandermonde. The explicit difference product on the RHS follows mathlib's `Matrix.det_vandermonde` orientation. This equality is not an orthogonal equivalence between two ad hoc predicates.

Syntactic-generality experiments: the exact quotient RHS with a local factorial-nonzero premise compiles; the arbitrary-monic evaluation law compiles by a single existing mathlib call. A multiplication-by-factorials form is the appropriate ring-level primary API. This avoids unnecessary global `CharZero` assumptions while preserving the existing caller's use as a rewrite after supplying factorial nonvanishing.

Superfluous-argument audit: the universe and size are genuine; commutativity is needed by determinant API; inverse structure is needed by the written RHS; global `CharZero` is stronger than the verified local premise. No unused explicit hypothesis or artificial positivity/injectivity restriction is present. **Overall: RESTATE-BEFORE-SHIP** — weaken characteristic assumptions, and consider the cancellation-free primary normal form.

## Phase 6.0 — callers and inline audit

Source-level direct references, excluding comments and the declaration itself:

| Caller | Pattern | Recommended future change |
|---|---|---|
| `Roth/Wronskian.lean:151`, `wronskian_ne_zero_of_natDegree_injective` | `simpa [h0, det_choose_eq, …] using coeff_wronskian_of_natDegree_injective` | Use the weakened formula at natural-degree vector, with `hf μ := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _)`; alternatively obtain the multiplication identity, prove the factorial product nonzero, and cancel. |

Within-file explicit use count1; outside-file use count0, files0. Under the command's convention excluding the declaring file, internal-use count `K=0`; total explicit proof callers1. Documentation lists the theorem but is not a proof caller. No inline independent rederivation appears elsewhere in the project. [Exact caller/inline scan](../evidence/Roth.det_choose_eq/rg-callers.json). This is source-level caller evidence, not the opaque kernel/simp dependency closure. The theorem has no `[simp]` attribute, and its explicit sole use supplies a real Wronskian nonvanishing step, so it is not junk.

## Phase 6 — actual composition experiments

1. **Existing abstract term succeeds:** the arbitrary commutative-ring monic evaluation statement is exactly `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde v p hdeg hmonic`. This confirms the abstraction exists; it does not solve the original binomial matrix goal without its bridge.
2. **Direct original-form `simpa only` from scaled abstract equality fails:** the normalization list includes the public choose conversion, determinant scaling, transpose and Vandermonde laws, but cannot synthesize the matrix equality needed to expose row scaling under the determinant. [Exact attempted source](../evidence/Roth.det_choose_eq/native-composition-executed.lean.txt), [rejected receipt](../evidence/Roth.det_choose_eq/native-composition-rejected.json). Any recovery `sorryAx` belongs only to rejected evidence and is not accepted proof evidence.
3. **Quotient recovery and real caller succeed:** [accepted recovery source](../evidence/Roth.det_choose_eq/native-corollary-executed.lean.txt)/[receipt](../evidence/Roth.det_choose_eq/native-corollary-success.json) derive the exact inverse formula from the newly proved ring identity using `Finset.prod_inv_distrib` and `eq_inv_mul_iff_mul_eq₀`, with nonzero factorial product, and recover the original CharZero formula. This is a bridge from a **new** theorem, not an existing ≤3-call mathlib replacement. [Accepted sole-caller replay](../evidence/Roth.det_choose_eq/native-caller-executed.lean.txt)/[receipt](../evidence/Roth.det_choose_eq/native-caller-success.json) copies the new ring theorem and recovery, and rebuilds `wronskian_ne_zero_of_natDegree_injective` using the recovered formula in its simp list. The old `Roth.det_choose_eq` is not invoked by that proof.
4. **Exact source proof succeeds:** entrywise matrix equality followed by at least four determinant transformations, plus degree/monicity witnesses. This is a real proof rather than a ≤3 existing-call term. The local-factorial generalization additionally proves the weaker entry-conversion helper.

**NOT-COMPOSABLE for the tested routes under the command's ≤3-call criterion.** This is an evidence-based composition assessment, not a proof that no possible three-call term exists. The abstract law alone is not an original-form replacement; new helper proofs are not existing mathlib building blocks. Were a closing `simp [defs,…]` found, Phase6b would classify it as borderline rather than automatic NO-composable. Here that attempted simple bridge did not close.

## Phase 7 — actionable verdict

**YES-but-generalise-first**, reason **LITERATURE-WEAKENING**, supported by the native verified replacement of `[CharZero K]` by local factorial nonvanishing. No parent-definition refactor is needed. The literature supplies both the exact binomial identity and the general polynomial explanation, and the pinned library contains the essential generic law plus a closely related private integer bridge. That private bridge, already used to prove superfactorial divisibility, is a concrete missing-public-API anchor. A public ring-level factorial-multiplied identity and its nonzero-factor quotient specialization would serve both integral divisibility and positive-characteristic users, alongside the existing Wronskian application.

This recommendation does **not** propose adding another generic monic polynomial evaluation theorem. It does not assert that an inaccessible private declaration is a public replacement. The original spelling needs an entrywise normalization proof, so the verified abstract hit cannot honestly support a ≤1-line original-form NO-mathlib-has-it verdict. This scalar theorem has no previously NO-mathlib-has-it parent definition to which ModeB's mandatory re-aim rule would apply.

Proposed location: `Mathlib/LinearAlgebra/Vandermonde.lean`, beside the private binomial bridge and `superFactorial_dvd_vandermonde_det`. Proposed PR title: **feat(LinearAlgebra/Vandermonde): expose binomial evaluation determinant formulas**. Group the cancellation-free identity, local-factorial quotient corollary and supporting local-nonzero Pochhammer conversion if useful; reuse the existing generic evaluation law. Current accepted YES declarations from `progress.json` are `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_map`, `hasseDeriv_rename`, `hasseDeriv_hasseDeriv`, `hasseDeriv_hasseDeriv_of_disjoint`, `pderiv_hasseDeriv`, `degreeOf_hasseDeriv_le`, `hasseDeriv_eq_zero_of_degreeOf_lt`, `hasseDeriv_mul_of_degreeOf_eq_zero`, and `factorial_smul_hasseDeriv_single` (all in namespace `MvPolynomial`). None is a natural same-PR dependency of this scalar determinant API; keep this a separate focused PR. Earlier Wronskian declarations are BORDERLINE and are not represented as accepted YES additions.

Pre-PR checklist:

- [ ] `/generalise Roth.det_choose_eq`: select ring-level primary statement and local-factorial quotient corollary; retain false-generalization guards.
- [ ] `/cleanup Roth/Wronskian.lean Roth.det_choose_eq`: style, naming, imports, direct-call audit and final proof cleanup.
- [ ] Ask Yaël Dillies or Yury Kudryashov to review, based on relevant Vandermonde mathematical/API history; no claim is made about their availability. Root supplied the complete executed history query and full stdout in [reviewer evidence](../evidence/Roth.det_choose_eq/reviewer-history.json). Relevant commits: `a00728860c` (Yaël Dillies, Vandermonde move to LinearAlgebra, #29095) and `32a0a63fe2` (Yury G. Kudryashov, Vandermonde golf, #23704). Toolchain/bot commits were excluded from reviewer selection.

All implementation changes are future recommendations. Production and overview records were not modified by this assessment.


## Phase 8 — completion and verification scope

All requested phases are complete. Five accepted native receipts cover the exact target replay, identical-RHS factorial-local weakening and existing abstract term, arbitrary-ring cancellation-free identity with positive-characteristic success/failure guards, inverse recovery from the new ring identity, and the actual sole-caller replay. Every accepted result reports success, no timeout/partial response, no warning/error, and only standard axioms. Rejected composition/guard/ring/recovery attempts are separated and excluded from accepted proof evidence. [Verification index](../evidence/Roth.det_choose_eq/verification.json), [assessment](../evidence/Roth.det_choose_eq/assessment.json), [portable read-only validator](../evidence/Roth.det_choose_eq/validate.py), [credential guard receipt](../evidence/Roth.det_choose_eq/secret-scan-receipt.json).

The report recommends an API change; no production migration was performed or built. The original baseline build is reusable because its 17 source/pin hashes freshly match. The isolated and persistent probe successes establish exactly the tested new statements and caller proof, without claiming a migrated production build. `unresolved=[]` records completion of this read-only assessment; normal upstream design review and the checklist remain future work. Root acceptance is pending independent review.
