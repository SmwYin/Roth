# Full /mathlibable assessment — `Roth.genWronskian`

**YES-but-generalise-first.** The named generalized Hasse Wronskian deserves a stable mathematical API, but its coefficient hypothesis should be `CommRing`, and its square family index can be any finite type. These changes compile and specialize definitionally to the original. This conclusion is independently assessed: the accepted YES for multivariate Hasse derivatives is a prerequisite, not a verdict inherited by this determinant wrapper.

Canonical declaration101, `Roth/GenWronskian.lean:32`, assessed2026-10-27 on assigned branch `ramin-cleanup`; production sources and pins unchanged. Root acceptance is pending. No worker Git operation or production edit. All local evidence links target the intended integrated layout.

## Phase 0 — Doctor

Clean baseline: **2467 jobs**, exit0. All **17/17 source/pin hashes** freshly match the shared successful baseline; the root also supplied the fresh100-declaration milestone build. [Baseline](../evidence/Roth.genWronskian/baseline-build.txt), [fresh hash comparison](../evidence/Roth.genWronskian/inputs.json), [canonical entry](../evidence/Roth.genWronskian/canonical-entry.json). The whole declaring module and all five relevant source caller declarations were read; their entire module snapshots are preserved. [Declaring module](../evidence/Roth.genWronskian/source-0.lean.txt), [Separation](../evidence/Roth.genWronskian/source-1.lean.txt), [source hashes](../evidence/Roth.genWronskian/source-inputs.json).

Public noncomputable definition, no placeholder. Module defines generalized Wronskians and proves nonvanishing via Kronecker substitution. Actual native type:

```lean
Roth.genWronskian.{u_1, u_2} : {K : Type u_1} →
  [Field K] → {σ : Type u_2} → {l : ℕ} →
  (Fin l → σ →₀ ℕ) → (Fin l → MvPolynomial σ K) → MvPolynomial σ K
```

**There is no `[Fintype σ]` parameter in the elaborated type.** The surrounding section instance was already omitted automatically. Native `#print` and axioms resolve the exact target. Accepted checks have no errors/warnings and use only `propext`, `Classical.choice`, `Quot.sound`; no limit raises or trust bypasses. [Executed original/generalized checks](../evidence/Roth.genWronskian/gen-wronskian-generic-executed.lean.txt), [raw native receipt](../evidence/Roth.genWronskian/gen-wronskian-generic-receipt.json). The earlier original-only receipt had a missing scratch module docstring warning; it is retained as rejected evidence, never counted as clean success. [Rejected receipt](../evidence/Roth.genWronskian/gen-wronskian-original-receipt.json).

## Phase 1 — Comprehend

Given polynomials `φν` and finitely supported multiorders `Dμ`, form the square matrix whose `(μ,ν)` entry is the Hasse derivative `Δ(Dμ)(φν)`. Its determinant is another multivariate polynomial, the generalized Hasse Wronskian. The definition accepts arbitrary orders; the condition `degree(Dμ) ≤ μ` belongs to the later existence theorem. It accepts the empty family, whose determinant is1.

| Parameter | Meaning / actual need |
|---|---|
| `{K : Type u}` | coefficient carrier; field structure is stronger than the construction needs |
| `[Field K]` | supplies commutative-ring operations; division never appears |
| `{σ : Type v}` | arbitrary variable set; each input and each derivative multiorder has finite support |
| `{l : ℕ}` | square matrix cardinality, with no positivity assumption |
| `D : Fin l → σ →₀ ℕ` | one Hasse differential multiorder per row |
| `φ : Fin l → MvPolynomial σ K` | one polynomial per column |

Conclusion: a polynomial, not a proposition. The Hasse normalization matters: ordinary iterated partial derivatives multiply rows by factorials, and these factors can vanish in positive characteristic. The definition imposes no characteristic-zero hypothesis.

## Phase 2 — Preliminary checks

**BIG:** introduces the named mathematical concept supporting the module's main nonvanishing theorem. Body count: **one substantive line**, `Matrix.det (Matrix.of ...)`.

| One-line exemption | Applies? | Evidence |
|---|---|---|
| Avoid defeq abuse | No | Ordinary semireducible def, explicitly unfolded by the sum and separated-product callers; `rfl` exposes the RHS without special attributes. |
| Avoid typeclass diamonds | No | Returns an existing polynomial type; creates no typeclass or instance. |
| Semantic intent / stable API | **Yes** | The nonvanishing theorem, linear-dependence theorem, Kronecker determinant expansion, and separated-factorization proofs all refer to this same named invariant. A derivative-normalization or representation change can be isolated behind the name. |

**ONE-LINER WITH-EXEMPTION.** The name and docstring mark a standard object with five explicit source consumers. Its brevity does not establish a mathlib-only replacement: its inner multivariate Hasse operator is project code.

## Phase 3 — Exhaustive literature

Exact requests, returned response hashes/byte counts, titles/URLs, locators and original summaries are archived; article/search bodies are not. [General queries](../evidence/Roth.genWronskian/web-0.json), [nLab/nCatLab/Stacks queries](../evidence/Roth.genWronskian/web-3.json), [MO/recent queries](../evidence/Roth.genWronskian/web-6.json), [direct access](../evidence/Roth.genWronskian/web-direct.json), [bounded recent/primary follow-up](../evidence/Roth.genWronskian/web-follow.json), [local manuscript excerpt](../evidence/Roth.genWronskian/local-literature.txt).

| Channel | Exact query / read | Outcome and scope |
|---|---|---|
| General web, specific | `generalized Wronskian multivariate polynomials Hasse derivatives determinant` | Multivariate derivative determinants, primary Bostan–Dumas and Hasse references. |
| General web, general | `generalized Wronskians differential operators commutative rings characteristic positive` | Differential-operator generality and characteristic issues; not a proof of a matching API. |
| General web, aliases | `multivariate Wronskian Hasse Schmidt determinant divided derivatives` | Divided/Hasse normalization distinguished from ordinary derivatives. |
| Optional mathematical ChatGPT | Capability inventory | n/a: `ask_chatgpt_math` unavailable; no consultation claimed. |
| Local reference | `clean.tex`, lines206–210, subsequent lemmas | Explicit determinant definition with row-order bounds in prose; Hasse version formalized without baking bounds into the object. |
| nLab | `site:ncatlab.org/nlab Wronskian`; direct Wronskian page | Indexed Wronskian context; direct opening failed400 unsupported XHTML. No unread direct content claimed. |
| nCatLab | `site:ncatlab.org/ncatlab generalized Wronskian differential operators` | Related differential-operator material; no categorical replacement established. |
| Stacks | `site:stacks.math.columbia.edu Wronskian differential operators`; exact `"Wronskian"` follow-up; tag09CH | General finite-order operators over ring maps, not this polynomial determinant. The combined search response does not establish per-query absence. |
| MathOverflow | `site:mathoverflow.net generalized Wronskian multivariate polynomials` | Questions436759 and487552; Roth induction motivation and references, secondary context only. |
| Recent arXiv | `site:arxiv.org generalized Wronskians 2022 2023 2024 2025 2026`; date-bounded follow-up | Opened2511.03848 and2605.27305, both inside2021-10-27 through2026-10-27; multidimensional derivative determinants, with complete/incomplete variants. The returned2108.02993 is outside this interval and is not counted as recent. |

Primary anchor: Bostan–Dumas, *Wronskians and Linear Independence* (2010), pp.725–726, “Generalized Wronskians,” defines the selected partial-derivative determinant and bounds the order in row`s` by`s`. [Author-hosted paper](https://mathexp.eu/bostan/publications/BoDu10.pdf). Its formal-power-series and characteristic-zero nonvanishing theorem exceeds the present polynomial object, but does not require replacing this object with formal power series merely to define its determinant.

The local manuscript defines exactly the corresponding invariant. Recent primary records confirm continuing multivariate use: [Kiselev2025](https://arxiv.org/abs/2511.03848), abstract; [Ķēniņš–Kiselev2026](https://arxiv.org/abs/2605.27305), abstract. They use ordinary derivatives and selected or complete jet multiindices. They support the concept's relevance, not the claim that ordinary and Hasse determinants are identical in all characteristics. [Stacks09CH](https://stacks.math.columbia.edu/tag/09CH), Definition10.133.1, gives the surrounding linear-operator abstraction; it does not supply this invariant.

**Literature synthesis:** the stable idea is a determinant of a selected family of differential operators applied to a finite family. Functions/power series, allowed orders, normalization and coefficient assumptions vary with applications. Extending this polynomial Hasse determinant from fields to commutative rings preserves the same finite algebraic expression; this last generality claim is an algebraic inference verified natively, not attributed verbatim to the classical characteristic-zero paper.

## Phase 4 — Generality

| Parameter / hypothesis | Audit | Verified action |
|---|---|---|
| Coefficient carrier / universes | Already independent universe parameters | Preserve; independent `ULift` coefficient/variable/index probes pass. |
| `[Field K]` | Unnecessary inversion/nontriviality | Replace by `[CommRing R]`; actual definition compiles over `ℤ`. |
| `[CommSemiring R]` proposal | Rejected at the determinant interface | `Matrix.det` requires `CommRing`; `CommRing ℕ` fails. Dropping negatives changes signed determinant semantics. |
| Variables `σ` | Already arbitrary | No finite-variable weakening to claim. Infinite `ℕ` and empty variables compile. |
| `l` / `Fin l` | Only square finite indexing used | Arbitrary `ι`, `[Fintype ι] [DecidableEq ι]` compiles. Retain `Fin l` where later ordered row bounds use it. |
| `D` | Arbitrary finitely supported multiindices | Keep all entries; do not add order bounds to the definition. |
| `φ` | Arbitrary family | Keep all entries; no independence or degree condition needed. |
| Empty family | Meaningful determinant1 | Empty index probe compiles. |

Proposed definition (verified, CHEAP single-definition edit):

```lean
noncomputable def genWronskian {R σ ι : Type*} [CommRing R] [Fintype ι]
    [DecidableEq ι] (D : ι → σ →₀ ℕ) (φ : ι → MvPolynomial σ R) :
    MvPolynomial σ R :=
  (Matrix.of fun μ ν ↦ MvPolynomial.hasseDeriv (D μ) (φ ν)).det
```

Native `original_eq` is `rfl`; all five caller proofs replay in full with the generalized definition. This is mechanical weakening, not merely a desired API redesign. The abstract `ofOperators (δ : ι → M → A) φ := det(δi(φj))` also compiles and specializes by `rfl`, but is a diagnostic expression, not an existing mathlib primitive or a proposed additional wrapper to ship. [Executed generic source](../evidence/Roth.genWronskian/gen-wronskian-generic-executed.lean.txt), [caller replay](../evidence/Roth.genWronskian/gen-wronskian-consumers-executed.lean.txt), [bridge/infrastructure](../evidence/Roth.genWronskian/gen-wronskian-bridge-executed.lean.txt).

### Phase 4c — Nine modern-idiom questions

| # | Question | Result / downstream consequence |
|---|---|---|
| 1 | Bundled hypotheses to typeclasses? | No: coefficients already use typeclasses; `D` and `φ` are data. |
| 2 | Sequences/metric to filters? | No topology or limiting process. |
| 3 | Construction to universal property? | No: the value is the concrete determinant. Determinant multilinearity is existing API, not a new class characterizing derivatives. |
| 4 | Closure predicate to bundled substructure? | No closure predicate; parent derivatives are already linear maps. |
| 5 | Field to module/(semi)ring? | **Yes, CommRing**; integral coefficients and positive characteristic become available, and `RingHom.map_det` composes. General modules alone do not carry a determinant-valued multiplication. |
| 6 | Higher categorical version? | No categorical structures in the input/output. |
| 7 | Concrete index to abstract index? | **Yes, finite square index**; uses `Matrix.det` without choosing `equivFin`; later bounds may specialize. |
| 8 | Concrete-via-abstract diagnostic? | Body inspection: one occurrence of `hasseDeriv`, otherwise only `Matrix.of` and `.det`. Replacing the operator by arbitrary functions gives `ofOperators`; this identifies the existing determinant abstraction. It does not eliminate the chosen Hasse family, whose meaning and nonvanishing API justify the name. |
| 9 | False-generalization guard? | CommRing and arbitrary finite index preserve the exact Hasse entries and determinant; `rfl` specialization confirms this. Replacing Hasse by ordinary derivative or using a permanent over semirings would change the object and is rejected. |

Modern idiom available: **yes**, coefficient/index generality. Real consequence: characteristic-free construction over integral rings and direct use of determinant transport/multilinearity APIs. No category-theoretic rewrite is proposed.

### Phase 4.5 — Six infrastructure risks

| Risk | Verdict | Checked evidence |
|---|---|---|
| Typeclass diamond | NONE | No new instance/type; native synthesizes existing `CommRing (MvPolynomial ℕ ℤ)`, `Module ℤ ...`, `DecidableEq (Fin2)`. |
| Reducibility leak | LOW | Ordinary semireducible def, no reducibility attribute; `direct_eq := rfl` demonstrates intended access to determinant body. No new typeclass computation exposed. |
| Noncanonical unfolding | LOW | Three callers unfold/defeq-reduce the determinant intentionally; preserve explicit unfolding and a documented name. No competing simp expansion installed. |
| Priority collision | NONE | Definition is not an instance and introduces no priority. All instances are inherited from polynomial/matrix types. |
| Universe issues | NONE | Independent coefficient, variable and finite-index `ULift` probes compile; empty variables and empty index accepted. |
| Coercion ambiguity | NONE | Returns existing `MvPolynomial`; introduces no `CoeFun`/`CoeSort`. Parent `LinearMap` application and polynomial coefficient access use their existing canonical coercions. |

Overall risk **LOW**, no HIGH row. Mitigation: retain an ordinary named def; avoid a new instance or global unfolding simp rule. [Infrastructure/native bridge source and receipt](../evidence/Roth.genWronskian/gen-wronskian-bridge-receipt.json).

### Phase 4.6 — Five proof-strategy questions

| # | Question | Result |
|---|---|---|
| 1 | Topology ε–δ instead of filters? | No: finite algebraic construction. |
| 2 | Elementwise algebra instead of substructures? | No membership proof. Parent operators already bundled linear maps; determinant supplies multilinear structure. |
| 3 | Sequences instead of nets? | No limits. |
| 4 | Explicit category construction instead of universal property? | No categorical construction. |
| 5 | Missing helpers required? | Parent multivariate Hasse definition/API must be upstreamed; no helper is needed to define this determinant once it exists. Reindexing/map/alternation laws can reuse determinant API. |

**MATHLIB-IDIOMATIC construction**; generalize its signature. Full caller replays are migration checks, not new proofs that those callers themselves merit upstreaming.

## Phase 5 — All five mathlib search methods

Each service actually queried current, literature-standard and abstract forms. [12 exact formal requests and receipt index](../evidence/Roth.genWronskian/formal-search.json). Complete original service responses are separate referenced JSON files listed there; external indices may differ from the project pin.

| Method | Three forms | Result |
|---|---|---|
| Finder | multivariate Hasse determinant; general differential-operator Wronskian; determinant of linear-map evaluations | Pair `Polynomial.wronskian`/bilinear API and determinant candidates; no matching generalized multivariate object identified. |
| Loogle | `"wronskian"`; `"hasseDeriv"`; `Matrix.det` | Pairwise univariate Wronskian, univariate Hasse derivatives, finite commutative-ring determinant. |
| LeanSearch | generalized multivariate Hasse Wronskian; partial derivative determinant over rings; alternating multilinear determinant | Same partial candidates plus `Matrix.detRowAlternating`. |
| Source `rg` | exact target; Wronskian/Hasse in MvPolynomial and known primary files; determinant/alternating abstractions | Pinned Wronskian TODO explicitly requests an n-tuple definition; no multivariate Hasse definition in mathlib's MvPolynomial directory. Exact receipts preserved. |
| Local | `genWronskian`; `wronskian`; `Matrix.det` | Project target/callers and mathlib candidates. `index: unavailable`: source contributions are useful positive hits, never completeness evidence. |

[Exact current rg](../evidence/Roth.genWronskian/rg-current.json), [standard rg](../evidence/Roth.genWronskian/rg-standard.json), [abstract rg](../evidence/Roth.genWronskian/rg-abstract.json).

Pinned candidate source/type checks, actually executed mathlib-only with guards `#check_failure Roth.genWronskian` and `#check_failure MvPolynomial.hasseDeriv`:

- `Polynomial.wronskian`, `Mathlib/RingTheory/Polynomial/Wronskian.lean:43`: two univariate polynomials, ordinary first derivatives. Not arbitrary row multiorders or arbitrary finite families. The file's n-tuple TODO is a concrete gap anchor, not a claim that this multivariate API alone resolves every univariate design question.
- `Polynomial.hasseDeriv`, `Mathlib/Algebra/Polynomial/HasseDeriv.lean`: univariate operator; does not accept `σ →₀ ℕ`.
- `Matrix.det`, `Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:60`: arbitrary finite square matrix over `CommRing`; exact outer operation only.
- `Matrix.detRowAlternating`, same file:55: already bundles alternation in rows; no chosen family of multivariate Hasse derivatives.

Additional abstract Finder hits were read in pinned source: `exteriorPower.alternatingMapToDual_apply_ιMulti` pairs scalar-valued linear functionals with module vectors. Hasse endomorphisms here are K-linear with polynomial-valued output, not K-valued dual vectors; regarding the polynomial ring as the scalar ring would falsely require polynomial-linearity of Hasse differentiation. `LinearMap.det_toMatrix'` merely changes the representation of a supplied finite free endomorphism. `Algebra.PreSubmersivePresentation.jacobian_eq_det_aevalDifferential` requires a presentation and its first-order evaluation differential, not arbitrary higher Hasse rows. None supplies the missing multivariate operator family. Their source signatures are recorded as rejected nonmatching search candidates, not accepted replacement proofs. [Pinned candidate source audit](../evidence/Roth.genWronskian/rg-extra-candidates.json).

[Executed isolated source](../evidence/Roth.genWronskian/gen-wronskian-raw-executed.lean.txt), [raw exact receipt](../evidence/Roth.genWronskian/gen-wronskian-raw-receipt.json). Candidate names/signatures are positive native evidence; search failures/empty results are not proofs of absence.

### Phase 5.5 — Three statement-shape checks

1. **Normal form:** determinant of an evaluation matrix versus row alternating-map evaluation versus a support/coefficient sum. Existing `Matrix.det` is the canonical outer operation. Proposed named Hasse invariant retains that RHS; no orthogonal pairwise equivalence API or global unfolding rule. Hasse and ordinary derivative determinants are different normalizations.
2. **Syntactic generality:** arbitrary finite index was compiled, avoiding forced enumeration; `Fin l` remains a specialization suited to row-order bounds. Abstract operator input also compiled but would discard the Hasse-specific semantic interface if used as the only public name.
3. **Superfluous arguments:** field inverses are unused and removed; `Fintype σ` was never present; all `D`/`φ` values are needed. `Fintype ι` and `DecidableEq ι` are imposed by the exact determinant interface; no explicit order bound or linear-independence proof should be added to the def.

Overall **RESTATE-BEFORE-SHIP** with the displayed CommRing/finite-index signature.

## Phase 6 — Callers, inline audit and composition

**Five explicit source caller declarations**, three internal and two external. Counts distinguish declarations from seven textual occurrences; target declaration and prose are excluded. [Full caller inventory](../evidence/Roth.genWronskian/callers.json), [exact source grep](../evidence/Roth.genWronskian/rg-callers.json), [inline grep](../evidence/Roth.genWronskian/rg-inline.json).

| Caller | Locations | Migration and native result |
|---|---|---|
| `genWronskian_eq_zero_of_not_linearIndependent` | GenWronskian:41–49 | Re-aim polynomial value; identical determinant-kernel proof replay PASS. |
| private `wronskian_kronecker_eq_sum_aux` | GenWronskian:238–245 | Replace name in statement and explicit simp unfolding; entire proof replay PASS. |
| `exists_genWronskian_ne_zero` | GenWronskian:254–270 | Replace name in conclusion and re-aim private expansion; entire Kronecker proof replay PASS. |
| `det_hasseDeriv_separated` | Separation:351–366 | Replace name in statement and `rw` list; entire determinant-product proof replay PASS. |
| private `exists_rat_factors_det_hasseDeriv_aux` | Separation:510–534 | Replace local factor in `hFmap`, use replayed nonvanishing/product results; entire proof replay PASS. |

[Exact executed full-body replay](../evidence/Roth.genWronskian/gen-wronskian-consumers-executed.lean.txt), [native receipt](../evidence/Roth.genWronskian/gen-wronskian-consumers-receipt.json). They intentionally reuse project lemmas on derivatives/Kronecker/separation; this does not make them mathlib-only composition proofs. No scratch proof calls the original same theorem being replayed.

Inline audit: the univariate `wronskianMatrix` uses `Polynomial.hasseDeriv`. CoeffNorm, Separation and Theta raw determinant formulas use orders depending on both row and column applied to a single polynomial. They are related mathematics, but are not literal copies of the exact row-order/family-column RHS. The canonical293-name native audit inspects stored declaration values with `allowOpaque := true` and finds the same five direct proof consumers. It does not traverse transitive dependency or simp closure. This kernel constant-reference check is independent of the five-source-caller inventory. Exact293 unique/order snapshot and native array are independently validated.

**Composition experiments:**

- `original_eq`, `direct_eq`, `abstract_eq` close by `rfl`; they establish signature compatibility and the generic determinant pattern, not a missing mathlib Hasse primitive.
- Mathlib-only `raw` compiles by expanding the chosen Hasse operator as a finite sum of binomial-weighted monomials, then taking the determinant. It is a new scratch construction, not an existing generalized Wronskian declaration.
- Actual project bridge `raw_eq` identifies that raw expression with `generalized`; `expanded_eq` uses project `MvPolynomial.hasseDeriv_apply`, and the binomial `hasseCoeff` unfolds. The normalization argument is explicitly retained. [Executed bridge](../evidence/Roth.genWronskian/gen-wronskian-bridge-executed.lean.txt).
- This expanded route uses support sums, coefficient extraction, monomial construction, finite products/binomial coefficients and determinant. It is not a verified ≤3-existing-mathlib-call replacement. A future parent upstreaming would make the wrapper short, but the semantic one-line exemption still needs independent consideration; it is satisfied by the named invariant and its API here.

Composition verdict **NOT-COMPOSABLE under the strict existing-mathlib-only ≤3-call test**. This means no such replacement was established by the completed searches/experiments; it is not a universal impossibility theorem. The positive bridge is not a Phase6b automatic NO: it explicitly passes through project Hasse API and a new construction. Parent re-aim gate does not fire because the actual Hasse parent is accepted YES-add-as-is, not NO-mathlib-has-it.

## Phase 7 — Verdict and actionable next step

**YES-but-generalise-first — LITERATURE-WEAKENING / MODERN-IDIOM.** The concrete missing API is a named finite-family multivariate Hasse Wronskian with coefficient-ring generality and the subsequent vanishing/nonvanishing interface. Standard sources identify the invariant, the existing pairwise polynomial Wronskian TODO provides an upstream anchor, and all five project consumers demonstrate a coherent API. The verified mechanical CommRing/finite-index change is a strict improvement. Infrastructure risk is LOW; the semantic exemption explicitly justifies keeping this one-line named object.

Proposed upstream file: **`Mathlib/RingTheory/MvPolynomial/Wronskian.lean`**, new file importing the upstream multivariate Hasse API and matrix determinants. This path is a proposal for the multivariate layer, distinct from the existing pairwise `Polynomial` file.

Proposed PR title: **`feat(MvPolynomial): generalized Hasse Wronskians over commutative rings`**.

Group with already accepted YES declarations `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename` as a prerequisite/nearby API series. Their accepted verdicts were freshly read from progress, not inferred from names. The current definition's YES does not assign automatic YES to its later laws. [Accepted YES snapshot](../evidence/Roth.genWronskian/accepted-yes-snapshot.json).

Concrete follow-up checklist:

- `/generalise Roth.genWronskian`: replace Field by CommRing and use an arbitrary finite square index; keep `Fin l` specialization for row-order conditions.
- `/cleanup Roth/GenWronskian.lean Roth.genWronskian`: namespace/docstring/import/API review; select an upstream `MvPolynomial` name and retain explicit Hasse normalization.
- Upstream the multivariate Hasse prerequisite, then add this named definition and separately assess vanishing, coefficient-map/reindexing and nonvanishing laws. Existing determinant APIs should discharge generic structural laws.
- Refactor the five listed callers exactly as the clean replay; run project checks before a production change. This assessment itself changes none.
- Request review from **Rao Xiaojia**, whose recent matrix-API commit `3b3cdbb692` (2026-07-30) touches the relevant determinant infrastructure; **Yaël Dillies**, determinant simplification commit `bbd5fcf3ae` (2026-06-22), is an alternate. Selection is based on actual scoped recent commit metadata, not presumed availability. [Reviewer receipt](../evidence/Roth.genWronskian/reviewer-git.json).

No user approval or design answer is pending for this read-only assessment. If maintainers decline a named multivariate invariant, retain it in project-local `Roth/GenWronskian.lean`; that contingent alternative does not negate the present evidence-based YES.

## Phase 8 — Verification package

[Assessment](../evidence/Roth.genWronskian/assessment.json), [native/source verification](../evidence/Roth.genWronskian/verification.json), [overview entry](../evidence/Roth.genWronskian/overview-entry.json), [portable validator](../evidence/Roth.genWronskian/validate.py), [current manifest](../evidence/Roth.genWronskian/copy-manifest.json). All phases complete only when the portable validator passes; root independently reviews acceptance and normalizes the current integration manifest. Exact executed `.lean.txt` sources preserve actual execution paths in raw receipts. Rejected native preparation is separate from accepted proofs. Web metadata receives the tracked credential guard. No unfinished assessment is authorized for integration.
