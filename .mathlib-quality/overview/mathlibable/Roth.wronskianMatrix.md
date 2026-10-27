# Roth.wronskianMatrix — full mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The Hasse Wronskian matrix has a meaningful literature name and real project consumers, and mathlib explicitly requests an n-tuple Wronskian in its pinned TODO. Its entire construction is also a verified two-building-block expression. The remaining decision is the upstream API's granularity and derivative normalization, not whether the construction works. All assessment phases are complete; verification unresolved: []. This is a read-only assessment, with no production changes or authorization to implement future recommendations.

## Phase 0 — baseline and scope

Resolved public noncomputable definition at `Roth/Wronskian.lean:56`, canonical declaration 40. No prefilter applies. [Baseline](../evidence/Roth.wronskianMatrix/baseline-build.txt) reports exit0 and a successful 2467-job build; [fresh source/pin hashes](../evidence/Roth.wronskianMatrix/source-pin-hashes.json) verify all17 inputs match the shared baseline. The complete declaring module and both caller modules were read and archived: [Wronskian](../evidence/Roth.wronskianMatrix/source-wronskian.lean.txt), [GenWronskian](../evidence/Roth.wronskianMatrix/caller-genwronskian.lean.txt), [Separation](../evidence/Roth.wronskianMatrix/caller-separation.lean.txt). No sorry occurs in the declaration. Root alone ran native Lean and Git.

## Phase 1 — comprehension

For a family φ of l univariate polynomials, this constructs the square matrix whose column ν is the first l Hasse derivatives of φν. Row μ uses derivative order μ, starting at zero. The entries remain polynomials; there is no evaluation point and no determinant in this definition. Hasse derivatives coincide with ordinary iterated derivatives after multiplication by μ!, without needing division to define them.

Full native type:
```lean
@Roth.wronskianMatrix : {K : Type u_1} → [inst : Field K] → {l : ℕ} →
  (Fin l → K[X]) → Matrix (Fin l) (Fin l) K[X]
```

The implicit universe-polymorphic coefficient type K carries a Field instance. The implicit natural l sets both row and column counts and bounds derivative orders. The explicit family φ supplies columns. No nonzero, independence, characteristic, positive-length or degree hypothesis is present. The empty matrix at l=0 is deliberately permitted. The implementation is exactly `Matrix.of fun μ ν ↦ Polynomial.hasseDeriv μ (φ ν)`; Field is stronger than either component requires. Native type/definition and standard axioms are in [focused output](../evidence/Roth.wronskianMatrix/native-target-focused.json) and the [complete target receipt](../evidence/Roth.wronskianMatrix/native-target-success.json).

## Phase 2 — size and one-line definition test

BIG: a named classical mathematical matrix, listed among the module's main definitions. Body line count1: ONE-LINER WITH-EXEMPTION.

| Exemption | Applies? | Concrete evidence |
|---|---|---|
| Avoid defeq abuse | no | Exact body and entry equalities close by rfl; no downstream proof was found that needs a sealed unfolding barrier. |
| Avoid typeclass diamonds | no | The definition supplies a value, not an instance; no competing target instances are selected through its name. |
| Semantic intent/API stability | yes | `Roth.wronskian`, the column-update proof and `det_hasseDeriv_separated` refer to this specific named matrix; the literature also distinguishes the matrix and determinant. This makes the anchor meaningful but does not by itself settle upstream inclusion. |

The exemption prevents automatically dismissing a useful named concept solely by body length. It does not erase the actual composition result below.

## Phase 3 — exhaustive literature

[Full channel table and synthesis](../evidence/Roth.wronskianMatrix/literature-summary.md); exact requests and hash/byte/status/locator metadata: [web1](../evidence/Roth.wronskianMatrix/web1-metadata.json), [web2](../evidence/Roth.wronskianMatrix/web2-metadata.json), [web3](../evidence/Roth.wronskianMatrix/web3-metadata.json), [web4](../evidence/Roth.wronskianMatrix/web4-metadata.json). The protocol's named channels all ran, with three distinct general-web forms; optional ask_chatgpt_math is unavailable. No full web bodies or signed URLs are archived.

Guruswami–Kopparty's *Explicit Subspace Designs*, §3 Definition9, explicitly uses this Hasse-derivative matrix. [Primary paper](https://www.math.toronto.edu/swastik/subspace-designs.pdf). Gatto–Scherbak's survey explains ordinary and generalized row orders, together with jet-bundle interpretations. [Primary survey](https://www.impan.pl/~pragacz/gatto2.pdf). The Stacks principal-parts universal property supports investigating jets, but is not a ready-made matrix definition. [Tag09CH](https://stacks.math.columbia.edu/tag/09CH). Recent generalized Wronskians continue to use selected jet coordinates. [Kiselev2025 abstract](https://arxiv.org/abs/2511.03848).

Standard form: consecutive Hasse derivative rows for polynomials, with generalized forms allowing chosen derivative orders and multivariate operators. Ordinary derivative Wronskians are a related normalization, not the identical object. Local clean.tex §2, lines157–163, uses factorial-normalized derivatives over rational coefficients; [local excerpt](../evidence/Roth.wronskianMatrix/local-literature.txt). Literature supporting linear independence criteria imposes additional characteristic assumptions; no such criterion is part of this definition.

## Phase 4a–b — parameter and generality audit

| Parameter | Current | Weaker/general form checked | Finding |
|---|---|---|---|
| K | Type u | Type u retained, explicit Type0/Type1 checked | Already universe polymorphic. |
| Field K | field | Semiring R | Verified same-body weakening in native target and isolated probes; no inverses, subtraction or commutativity needed to construct entries. The literature's commutative-rig divided derivatives fit this weaker API; noncommutative Semiring is additionally supported by pinned hasseDeriv. |
| l | implicit ℕ | l=0 permitted; no lower bound added | Essential for consecutive orders and square determinant use. |
| Fin l row index | consecutive derivative orders | arbitrary ι with `order : ι → ℕ` | Rectangular definition and exact specialization compile; this is an expanded representation, not a hypothesis drop needed for present callers. |
| Fin l column index | l columns | arbitrary κ | Rectangular bridge compiles, but square format serves the determinant. |
| φ | polynomial family | retained; arbitrary linear maps considered | Essential input. Arbitrary differential operators are a different larger interface; bundling the existing operator is a useful alternative, not an existing replacement. |
| noncomputable | Hasse derivative data | retained | Pinned hasseDeriv lives in a noncomputable section. Initial data examples without a surrounding noncomputable section failed; corrected accepted probes retain it. |

**STRICTLY NARROWER THAN STANDARD** on coefficient hypotheses: one verified mechanical weakening, Field→Semiring. The standalone replacement body compiles as:
```lean
noncomputable def hasseWronskianMatrix {R : Type*} [Semiring R] {l : ℕ}
    (φ : Fin l → R[X]) : Matrix (Fin l) (Fin l) R[X] :=
  Matrix.of fun μ ν ↦ Polynomial.hasseDeriv μ (φ ν)
```

This snippet is a proposed future spelling; the exact executed version is named `WronskianMatrixAssessment.matrix`. Cost CHEAP for this definition alone; downstream determinant and independence theorems retain the assumptions their proofs need. No blanket claim that the whole file generalizes is made. [Accepted isolated source](../evidence/Roth.wronskianMatrix/native-taylor-executed.lean.txt), [accepted receipt](../evidence/Roth.wronskianMatrix/native-taylor-success.json).

## Phase 4c — nine modern-idiom checks

| # | Question | Answer and concrete consequence |
|---|---|---|
|1| Typeclass preambles | no: Field is already a typeclass; weakening it is row5. |
|2| Filters/nets/topology | no: a finite algebraic matrix has no convergence structure. |
|3| Universal properties | possible future jet interpretation, not a present replacement: Taylor coefficients after evaluation match evaluated Hasse rows by verified `evaluated_taylor`; principal parts adds a substantially different interface. No universal-property construction is asserted present in mathlib. |
|4| Bundled substructures | no set-with-closure predicate occurs. A bundled linear operator is separately useful and tested, not a substructure lattice issue. |
|5| Module/semiring hierarchy | yes: Semiring construction accepts ℕ coefficients and specializes back to Fields definitionally; a bundled R-linear map yields `map_add` without new entrywise proof. |
|6| Higher categories | no: no categorical statement requires upgrading; no concrete downstream benefit identified. |
|7| Concrete indices | yes, optional: arbitrary row/column types plus order map yield a rectangular generalized matrix; the exact Fin specialization is rfl. Consecutive ℕ derivative orders cannot simply become an arbitrary group without an order-selection map. |
|8| Concrete-via-abstract diagnostic | no named concrete witness: K and φ are already variables. The one-line body contains hasseDeriv once and Matrix.of once; no proof unfolds a named witness then works only abstractly. The verified bundled map packages this same operator, without a novel abstract theorem. |
|9| False-generalization guard | Semiring and rectangular specialization preserve the original entries exactly. Replacing Hasse derivatives by ordinary iterated derivatives changes the matrix: the accepted ℕ[X] X² order2 guard compares coefficient0 values1 and2. Reject a silent ordinary-derivative substitution. |

Modern idiom available: yes, as coefficient weakening and optional bundled linear map; real gains are ℕ-coefficient use and generic LinearMap.map_add. Native `bundled_bridge` is rfl and `matrix_add` is a direct map_add call. `evaluated_taylor` shows only an evaluated jet identity, not a definitionally equal polynomial matrix replacement. These new scratch constructions do not count as preexisting mathlib declarations. Root's isolated import guard confirms Roth.wronskianMatrix is unavailable in this evidence environment.

## Phase 4.5 — six infrastructure checks

| Risk | Verdict | Evidence |
|---|---|---|
|Typeclass diamond|none|No instance or new carrier is declared. `#synth Semiring ℕ` chooses Nat.instSemiring, and `#synth CommRing (Polynomial ℤ)` uses the existing polynomial ring instance; the matrix anchor does not introduce an alternative scalar structure.|
|Reducibility leak|low|An ordinary semireducible def, not a reducible abbreviation. Exact body and entry equality succeed by rfl; intended finite lambda expansion is cheap.|
|Noncanonical unfolding|low|Unfolding reaches Matrix.of and standard Hasse derivatives. Existing proofs explicitly unfold for entry calculations; no simp attribute on the definition forces automatic expansion.|
|Instance priority collision|none|This is not an instance; there is no priority or overlapping instance head.|
|Universe polymorphism|none|Type u and explicit Type1 examples compile, alongside the Type0 ℕ coefficient example. No universe equation is introduced by Fin indices.|
|Coercion ambiguity|none|No new CoeFun/CoeSort instance exists. Standard Matrix/LinearMap coercions and direct entry applications compile; the bundled linear-map bridge also closes by rfl.|

Overall LOW, no HIGH rows. The useful semantic anchor is not a typeclass or defeq workaround.

## Phase 4.6 — five proof-strategy checks

| # | Check | Result |
|---|---|---|
|1| ε-δ vs filters | n/a, no topology/proof. |
|2| Elements vs submodule inclusions | no such proof; direct Matrix.of is idiomatic. Bundling the family-to-matrix operation provides existing linear-map laws. |
|3| Sequences vs nets | n/a, no limiting argument. |
|4| Construction vs universal property | the concrete matrix is intentionally constructed entrywise; a principal-parts interface may serve a future generalized API, not shorten this definition. |
|5| Missing helper lemmas | no helper is required to construct it. Missing named n-ary/normalized Wronskian API is the pinned TODO, not an obstacle solved by inventing helper proofs. |

Strategy MATHLIB-IDIOMATIC as a concrete matrix constructor. If upstream elects a linear-map-primary interface, the native bundled variant is a concrete future option.

## Phase 5 — actual five-method × three-form search

[Complete formal requests/responses](../evidence/Roth.wronskianMatrix/formal-search-raw.json), [untruncated source commands/results](../evidence/Roth.wronskianMatrix/source-search-raw.json), [pinned excerpts](../evidence/Roth.wronskianMatrix/mathlib-source-excerpts.lean.txt).

Forms: current = square Hasse derivative matrix of finite univariate families; standard = generalized divided-derivative Wronskian over semirings; abstract = linear-map evaluation matrix / Taylor jets.

| Method | Current executed query | Literature-standard executed query | Abstract executed query | Observed result |
|---|---|---|---|---|
|Lean-Finder|The square Hasse derivative Wronskian matrix of a finite family of univariate polynomials|Generalized Wronskian matrix divided derivatives over an arbitrary semiring|Matrix of a family of linear maps applied to a family of vectors, Taylor jet coefficient matrix|Binary Polynomial.wronskian, Sylvester and Jacobi candidates; no exact n-ary matrix candidate returned.|
|Loogle|`Polynomial.hasseDeriv, Matrix`|`"wronskian"`|`Matrix.of`|Current query empty; standard binary API; abstract Matrix.of constructor.|
|LeanSearch|same current natural-language form|same standard natural-language form|same abstract natural-language form|hasseDeriv and binary wronskian; abstract LinearMap.toMatrix/toMatrix' need a chosen basis/domain map.|
|rg pinned source|full qualified and bare wronskianMatrix, no truncation|all wronskian/Wronskian occurrences|hasseDeriv, taylor_coeff, Matrix.of, toMatrix' and jet definition patterns in candidate files|No named wronskianMatrix source hit; existing Hasse/Matrix building blocks and explicit n-tuple TODO.|
|local name pattern|wronskianMatrix|wronskian|toMatrix|Project target/binary API/general matrix declarations; index unavailable, so results are source-assisted and cannot establish absence.|

All tools were actually invoked on all three forms. Finder default external index v4.28 may differ from the pinned revision. No search-only absence theorem is claimed. Positive candidate signatures were checked natively: `hasseDeriv` needs Semiring; Matrix.of takes a curried function; binary wronskian takes two polynomials and returns a polynomial, not an l×l matrix. The pinned Wronskian module TODO explicitly asks to define an n-tuple Wronskian; it is a concrete gap anchor, not an exact already-existing generalized matrix.

`LinearMap.toMatrix` is a basis-coordinate constructor for a single linear map. An arbitrary polynomial family need not be a basis; its output here would require constructing additional maps/coordinates. `Polynomial.taylor_coeff` matches *evaluations* of entries; it does not already name their full polynomial matrix. No ≤1-line specialization of the binary Wronskian to arbitrary l was found or asserted.

## Phase 5.5 — statement shape

Normal forms considered: direct Hasse matrix; ordinary derivative matrix with factorial row scaling; evaluated Taylor coefficient matrix; bundled linear map. Direct Hasse entries are the correct normal form for this development. A native normalization counterexample excludes treating the ordinary form as an equality. Data definition: RHS normal-form convention for iff/equality theorems is inapplicable, but native bridge identities display the direct constructor on the RHS.

Syntactic generality: retain implicit l and explicit φ, weaken coefficients to Semiring if shipping the standalone definition. Rectangular order-map and bundled linear-map forms were actually compiled and specialize by rfl; they are optional upstream design choices. The bundled variant concretely gains generic linear-map laws.

Superfluous-argument audit: Field's inverse, division, subtraction and multiplicative commutativity are unnecessary for construction; replace Field with Semiring. K, its universe, l and φ are essential to the displayed types/entries. No characteristic/decidability hypothesis is needed or hidden in the declaration signature. Overall **RESTATE-BEFORE-SHIP** for the standalone coefficient class; no production change is made.

## Phase 6 — callers, inline audit and actual composition

Source-level external-to-declaring-file uses: K=2 occurrences in2 files. Across all source, there are7 executable occurrences in6 caller declarations (the update theorem uses the name twice). This is an explicit source audit, not the kernel dependency or simp closure.

| Caller and exact reference | Pattern | Future mechanical inline plan if anchor rejected |
|---|---|---|
|Roth/Wronskian.lean:60, Roth.wronskian|det of named matrix|Replace `wronskianMatrix φ` with `(Matrix.of fun μ ν : Fin l ↦ Polynomial.hasseDeriv μ (φ ν))`.|
|Roth/Wronskian.lean:71, wronskian_eq_zero_of_not_linearIndependent|simp unfolding for row relation|Drop `wronskianMatrix` from simp list after determinant definition is inlined; entries are Matrix.of applications.|
|Roth/Wronskian.lean:139, coeff_wronskian_of_natDegree_injective|rw unfolds determinant and matrix|Remove the matrix unfolding rewrite after changing determinant definition.|
|Roth/Wronskian.lean:161 and163, wronskian_update_sub_smul|matrix argument to det column-update lemma and entry simp|Insert same Matrix.of expression in the determinant lemma argument, remove obsolete unfolding name from simp.|
|Roth/GenWronskian.lean:244, wronskian_kronecker_eq_sum_aux (private)|simp unfolds for row-multilinearity calculation|Remove matrix name after determinant definition is inlined.|
|Roth/Separation.lean:358, det_hasseDeriv_separated|mapMatrix and transpose determinant|Supply exact Matrix.of expression to mapMatrix.|

The module-doc occurrence at Wronskian:23 and the definition itself are excluded. Inline audit searched Matrix.of and Hasse derivatives throughout Roth. `genWronskian` forms a *multivariate, user-selected operator* matrix, and Separation has mixed partial determinant matrices; these are related constructions, not univariate bypasses of the exact target. No exact univariate inline re-derivation outside the target's consumers was found.

Actual composition1 succeeds:
```lean
Matrix.of (fun μ ν : Fin l ↦ Polynomial.hasseDeriv μ (φ ν))
```
This uses Matrix.of and Polynomial.hasseDeriv, two named building blocks, plus lambda/application syntax. It constructs the exact data; the project's Field bridge and entries are rfl. **COMPOSABLE as raw data construction.** It is not a closing simp-only composition; the Phase6b simp-borderline heuristic is not invoked.

Composition2, binary Polynomial.wronskian, is a partial near-match only: wrong arity/result type and no arbitrary-size matrix. Composition3, a bundled operator, is constructed with LinearMap.pi twice, hasseDeriv.comp and proj; its exact bridge is rfl and map_add supplies additivity. It is new verified scratch infrastructure rather than an existing named upstream replacement. Composition4, evaluated Taylor jets, closes by function extensionality and `Polynomial.taylor_coeff`; it proves an evaluated identity, not equality of original polynomial matrices.

These experiments provide positive evidence for straightforward inlining, but the Phase2 semantic/API exemption and pinned n-ary TODO make a categorical deletion recommendation a taste decision. Neither a cost argument nor invented absence evidence is used.

## Phase 7 — actionable verdict

**BORDERLINE-needs-human**, with all verification complete. Two concrete future upstream questions:

1. Should the n-tuple Wronskian TODO expose a separately named Hasse matrix (over Semiring), or keep this matrix inline inside the determinant API?
2. If exposing it, should its primary public spelling be `Polynomial.hasseWronskianMatrix`, with ordinary-derivative Wronskians connected by factorial row scaling, and should the bundled linear-map form be primary or supplementary?

These are future maintainer/API design questions; this read-only assessment needs no further user input. Default local recommendation: retain the useful named anchor until a coherent n-ary API is chosen; separately record the verified Field→Semiring opportunity for this definition only. Alternative destination if not accepted upstream: `Roth/Wronskian.lean`, where the name organizes determinant, column-operation and separation proofs. If the upstream decision rejects the anchor, every explicit caller has a mechanical inlining plan above.

A possible future contribution would extend `Mathlib/RingTheory/Polynomial/Wronskian.lean`, with title “feat(Polynomial): add Hasse Wronskian matrices for finite families”. This is a conditional recommendation, not an accepted YES verdict. Since accepted progress entries include the multivariate Hasse derivative API but no Wronskian-matrix YES, do not claim a previously accepted n-ary grouping; the primary contribution would group the matrix with a coherently assessed n-ary determinant API, with multivariate operator compatibility as separate follow-up. Future checklist: `/generalise Roth.wronskianMatrix`; `/cleanup Roth/Wronskian.lean Roth.wronskianMatrix`; settle derivative normalization; choose a reviewer from relevant commits. Moritz Firsching's directly relevant hasseDeriv_map commit334438dace is a reasonable reviewer lead; [history note](../evidence/Roth.wronskianMatrix/reviewer-history.txt), with original Wronskian authors Jineon Baek/Seewoo Lee as subject-matter context. No reviewer contacted.

## Phase 8 — verification and handoff

Accepted evidence: [target snapshot](../evidence/Roth.wronskianMatrix/native-target-executed.lean.txt), [target receipt](../evidence/Roth.wronskianMatrix/native-target-success.json), [isolated strongest snapshot](../evidence/Roth.wronskianMatrix/native-taylor-executed.lean.txt), [isolated strongest receipt](../evidence/Roth.wronskianMatrix/native-taylor-success.json). Both terminal responses succeed, with no errors, no warnings and no partial elaboration. Axioms are confined to propext, Classical.choice and Quot.sound. Native code uses no new axioms, sorry, unsafe, native_decide or raised resource limits. Project imports are only used to inspect/bridge the target; generalized construction, bundling, Taylor identity and normalization guard were verified in mathlib-only code guarded by #check_failure.

The original isolated data examples failed because their enclosing context was computable; the exact rejected request/diagnostics remain [separate](../evidence/Roth.wronskianMatrix/native-raw-rejected.json). The accepted strongest snapshot includes noncomputable section. No failed candidate is counted as verification evidence. Supporting earlier accepted raw/bundled receipts preserve chronology.

[Verification map](../evidence/Roth.wronskianMatrix/verification.json) lists exact source/receipt pairs; [assessment](../evidence/Roth.wronskianMatrix/assessment.json), [copy manifest](../evidence/Roth.wronskianMatrix/copy-manifest.json), and [portable validator](../evidence/Roth.wronskianMatrix/validate.py) make the package auditable in scratch and integrated layouts. Root acceptance remains pending. No repository or pin changed.
