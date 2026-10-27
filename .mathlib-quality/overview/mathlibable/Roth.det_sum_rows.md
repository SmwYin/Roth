# Full mathlibable assessment — `Roth.det_sum_rows`

Verdict: **BORDERLINE-needs-human**. This is a standard weighted multilinearity expansion. Mathlib has the two generic laws used by its proof, but their normalization into the entrywise determinant statement is real, observable proof work. Phase 6b classifies a closing simp composition as borderline; it does not authorize silently counting every simplification as one existing theorem call. There is no cost-based downgrade or inherited parent verdict.

## Phase 0 — baseline

The successful baseline build completed 2467 jobs at `99f19fda4b3cbee38fc0d31af76075834f5cc265`. All 17 current source/pin hashes were freshly compared with the shared baseline manifest and matched. Production Lean files and pins remain unchanged. `Roth.det_sum_rows` is a public theorem at `Roth/GenWronskian.lean:228`, without sorry. The entire 272-line declaring module and its sole explicit caller were read. The module reduces generalized Wronskians to univariate Wronskians via Kronecker substitution. Evidence: [baseline](../evidence/Roth.det_sum_rows/baseline-build.txt), [fresh inputs](../evidence/Roth.det_sum_rows/inputs.json), [full declaring module](../evidence/Roth.det_sum_rows/declaring-module.lean.txt), [verification](../evidence/Roth.det_sum_rows/verification.json).

## Phase 1 — mathematical statement and proof

For a finite square matrix over a commutative ring, suppose row μ is a finite sum of rows `N μ i` weighted by scalars `c μ i`. Its determinant is the sum over all choices of one summand in each row of the chosen determinant multiplied by the product of the chosen weights. Empty row supports and zero matrix size are included; no nonzero coefficients or positive size hypothesis occurs.

The full elaborated type is preserved in [native type](../evidence/Roth.det_sum_rows/original-type.txt):

```lean
Roth.det_sum_rows.{u_3, u_4} {l : ℕ} {A : Type u_3} [CommRing A] {ι : Type u_4}
    (s : Fin l → Finset ι) (c : Fin l → ι → A) (N : Fin l → ι → Fin l → A) :
    (Matrix.of fun μ ν ↦ ∑ i ∈ s μ, c μ i * N μ i ν).det =
      ∑ f ∈ Fintype.piFinset s,
        (∏ μ, c μ (f μ)) * (Matrix.of fun μ ν ↦ N μ (f μ) ν).det
```

`l` is the square matrix size; `A` the coefficient ring; `ι` the arbitrary summand type; `s` gives finite support per row; `c` gives weights; `N` supplies candidate row vectors. There are no inherited `K`, `Field`, `σ`, `Fintype σ`, `CharZero`, `k`, or degree-bound parameters in the actual type. The proof applies `MultilinearMap.map_sum_finset` to `Matrix.detRowAlternating.toMultilinearMap`, pulls out all weights with `map_smul_univ`, and converts function sums/scalar actions to matrix entries/multiplication. This is independent of Hasse derivatives and generalized Wronskians.

## Phase 2 — preliminary checks

**SMALL**: a standard linear algebra helper, neither a new structure nor a project main theorem or named theorem. One-line-definition test: **n/a — theorem**. The five-line original proof is not a definition and does not receive a definition-only exemption or rejection. Literature width remains exhaustive.

## Phase 3 — exhaustive literature

Exact requests, response hashes/bytes, credential-safe returned URLs and access status are in [web receipts](../evidence/Roth.det_sum_rows/web-receipts.json). No article/search-result bodies are archived. Summaries below are original concise descriptions. The protocol's nominal nine-channel wording actually lists three general searches plus the other named channels; each named channel was executed or explicitly marked unavailable.

| Channel | Exact query / access | Result and locator |
|---|---|---|
| General web, specific | `determinant multilinearity sum linear combinations rows formula commutative ring` | Standard determinant multilinearity; Chambert-Loir, *Commutative Algebra*, §3.8, Definition 3.8.11, page137, treats arbitrary commutative rings. |
| General web, general | `multilinear map finite sums product expansion determinant row choices` | Expansion is repeated separate linearity; arbitrary multilinear maps are the abstract object. |
| General web, aliases | `determinant alternating multilinear form commutative ring universal property` | Alternating multilinear form / determinant as universal volume form are the familiar aliases and representation. |
| ChatGPT mathematical MCP | Standard form, generality, historical evolution | n/a: `ask_chatgpt_math` unavailable in the tool inventory; no invented response. |
| Local source | `rg` of multilinearity and `mathcal S` in `clean.tex` | §2 proof of Lemma1, lines318–342, defines Cartesian choices, coefficient products and the exact row expansion. [Local excerpt](../evidence/Roth.det_sum_rows/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab determinant multilinear`; direct determinant URL | Indexed page supplies alternating multilinearity and explicitly discusses extension to arbitrary commutative rings. Direct fetch fails with unsupported XHTML content type; not recorded as direct access success. |
| nCatLab | `site:ncatlab.org/ncatlab determinant` | Returned nLab exterior-algebra/categorical discussion; no separate nCatLab article identified. The categorified determinant is broader context, not a required reformulation of this finite identity. |
| Stacks | `site:stacks.math.columbia.edu determinant multilinear`; direct tag0FJ9 | §15.120 *Determinants* accessed: determinant lines of finite projective modules. This explains coordinate-free scope, but is not an exact row-expansion replacement. |
| MathOverflow | `site:mathoverflow.net determinant multilinearity commutative ring` | *Definitions of determinant by unique features*, question425617, discusses normalized alternating multilinearity and universal integer polynomial. Other ring-factorization result500973 is not this identity. |
| Recent arXiv, five-year window | `site:arxiv.org determinant multilinearity 2022 2023 2024 2025 2026` | Returned 2609.23138 (2026), *Comparing different approaches to the concept of determinant*, and 2606.20586 (2026), vector determinant framework. They discuss multilinearity, but neither returned abstract supplies a stronger exact weighted finite-row law; no novelty inference from them. Older results also returned and were excluded from the recent window. |

Primary mathematical anchors: [Chambert-Loir §3.8](https://webusers.imj-prg.fr/~antoine.chambert-loir/publications/teach/sv-commalg.pdf), [Stacks §15.120](https://stacks.math.columbia.edu/tag/0FJ9). Supplementary exposition: [nLab determinant](https://ncatlab.org/nlab/show/determinant), [MathOverflow425617](https://mathoverflow.net/questions/425617/definitions-of-determinant-by-unique-features), [2026 determinant formulations](https://arxiv.org/abs/2609.23138).

Literature summary: this is finite expansion by multilinearity, with determinant as an alternating multilinear special case. Commutative rings already match the standard scalar setting. Finite index sets need not be `Fin l`, summand types may depend on the row, and the abstract weighted expansion makes sense for module-valued multilinear maps over commutative semirings. The project source is narrower in its rational-polynomial application than the actual helper statement.

## Phase 4a–b — generality and parameters

| Parameter / hypothesis | Used and possible weakening |
|---|---|
| `A : Type*` | Already universe polymorphic and arbitrary; no field, domain, characteristic or nontriviality assumption. |
| `[CommRing A]` | Fixed determinant API requires this class; arbitrary `[CommSemiring A]` or noncommutative `[Ring A]` does not elaborate the same `Matrix.det`. Abstract multilinear expansion over modules is a representation widening, not a claim that the determinant has this weaker interface. |
| `l : ℕ`, `Fin l` row/column index | Can replace by arbitrary `J` with `[Fintype J] [DecidableEq J]`; native mechanical proof checked. Positive size is unnecessary. |
| `ι : Type*` | Arbitrary, with no `Finite ι` or `DecidableEq ι` requirement. Can depend on row as `I : J → Type*`; checked separately. |
| `s` | Essential finite support data, may be empty or vary with row. No global finite summand universe is needed. |
| `c` | Arbitrary weights, including zero; can absorb into `N` for an unweighted intermediate law, but pulling their product outside each determinant is part of the stated result. |
| `N` | Essential row-vector data. No linear independence, regularity, or relation between rows is required. |
| ambient `K, σ` | Not parameters of this declaration, as native printing independently confirms. |

Generality verdict: **STRICTLY NARROWER THAN STANDARD** on finite index and dependent summand axes, with actual compiled widening in the accepted native evidence. Cost CHEAP, purely mechanical; cost is not a verdict factor. The exact proposed dependent statement is archived with the accepted native experiment; conceptually use `s : ∀ μ : J, Finset (I μ)`, `c : ∀ μ, I μ → A`, and `N : ∀ μ, I μ → J → A` in the displayed identity. No new public upstream theorem is silently assumed just because a scratch helper compiled.

## Phase 4c — modern idiom

| # | Question | Finding and concrete downstream consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No change: `CommRing` and finite index instances already express structure. |
| 2 | Sequences to filters | No: finite algebraic identity, no convergence. |
| 3 | Construction to universal property | No new construction; exterior powers explain determinant conceptually, but would add machinery without improving this caller. |
| 4 | Closure predicate to bundled substructure | No closure predicate. Already uses bundled alternating and multilinear maps in the proof. |
| 5 | Field/vector-space hierarchy | Abstract `MultilinearMap` permits `CommSemiring` and arbitrary modules; generic expansion and scalar extraction are existing mathlib laws. This serves every multilinear form, rather than only polynomial matrices. |
| 6 | Higher categories | No: determinant lines/functors do not simplify this finite coordinate expansion; not proposed. |
| 7 | Concrete index | Yes: `Fin l` to arbitrary finite `J`, with dependent `I μ`, avoids arbitrary enumerations and applies directly to finite bases. |
| 8 | Concrete-via-abstract | Yes: source body has one `Matrix.detRowAlternating` line and one `Matrix.det` normalization line; all mathematical transformations are the two generic multilinear laws. The determinant only selects a bundled multilinear witness. The exact abstract weighted formula was probed, with its normalization retained explicitly. |
| 9 | False-generalization guard | No semantic mismatch in finite/dependent widening: specializing `J := Fin l` and constant `I` restores the exact statement. Replacing determinant by arbitrary multilinear map is an abstract theorem whose determinant specialization must be bridged, not a definitional assertion or a ring-interface drop. Infinite determinants and noncommutative determinants are rejected as different objects. |

Modern-idiom verdict: **available**, but already largely embodied by mathlib's `MultilinearMap.map_sum_finset` and `map_smul_univ`. The useful unresolved API choice is whether their combined weighted expansion deserves a named generic helper or determinant convenience theorem. Existing bundled API supports scalar restriction, dependent modules and finite bases; no proposed new topology or category infrastructure is needed.

## Phase 4.5 — infrastructure risk

n/a: theorem. All six definition-only categories were considered: no new typeclass path (diamond), no new reducibility boundary, no new noncanonical definition unfolding, no instance-priority declaration, no structure universe computation, and no coercion instance. Existing multilinear-map coercions cause a normalization issue in an attempted proof; that is proof elaboration evidence, not a new typeclass diamond introduced by this theorem.

## Phase 4.6 — proof strategy

| # | Strategy question | Result |
|---|---|---|
| 1 | ε–δ versus filters | n/a: no topology. |
| 2 | Elements versus subobjects | No submodule inclusion to abstract; bundled multilinear evaluation is already the right algebraic strategy. |
| 3 | Sequences versus nets | n/a: no limiting process. |
| 4 | Explicit categorical construction versus universal property | n/a: no categorical object is built; exterior-power redevelopment would not help the sole caller. |
| 5 | Missing helper API | Possible weighted `MultilinearMap.map_sum_finset` convenience law, or determinant row expansion. Existing sum and scalar laws suffice mathematically; whether to name their simp combination is the upstream taste question. |

Verdict: **MATHLIB-IDIOMATIC** for the proof's mathematical strategy. Retain the generic sum/scalar approach rather than introducing permutation combinatorics. Any accepted convenience statement should broaden its indices first. No timing/cost criterion decides inclusion.

## Phase 5 — actual five-method search on three forms

All raw external formal-search responses are preserved in [formal receipts](../evidence/Roth.det_sum_rows/formal-search-raw.json); exact untruncated CLI/source queries in [source receipts](../evidence/Roth.det_sum_rows/source-search-raw.json). External Finder indices may differ from the project pin, so every selected positive candidate is source-checked and native-checked. The local index reports `unavailable`; its source-backed results establish presence only and do not establish absence.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Lean-Finder | Weighted determinant-row finite-choice expansion | Commutative-ring determinant multilinearity, arbitrary index | Multilinear finite dependent sums and all-coordinate scaling |
| Loogle | `Matrix.det, Finset.sum` | `Matrix.detRowAlternating, MultilinearMap.map_sum_finset` | `MultilinearMap.map_sum_finset` |
| LeanSearch | Same exact current natural-language query as Finder | Same standard-form natural-language query as Finder | Same abstract natural-language query as Finder |
| `rg` pinned source | `det_sum_rows`, determinant/sum variants | `detRowAlternating`, `det_updateRow_sum` | `map_sum_finset`, `map_smul_univ` |
| Local name-pattern | `det_sum` | `detRowAlternating` | `map_sum_finset` |

Current-form hits such as `Matrix.det_updateRow_sum` concern replacement of one row by a combination of the existing rows; they do not state simultaneous independent row choices. The standard Loogle conjunction returns no match; that is only a search outcome, not an absence theorem. Abstract searches positively locate:

- `MultilinearMap.map_sum_finset`, `Mathlib/LinearAlgebra/Multilinear/Basic.lean:620`: arbitrary finite index, dependent summand types, module-valued expansion.
- `MultilinearMap.map_smul_univ`, same file:1161: product of all scalar weights.
- `Matrix.detRowAlternating`, `Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:55`: bundled determinant, with `Matrix.det` defined by evaluation at line60.
- `Finset.sum_fn`, `Pi.smul_def`, `smul_eq_mul`: representation normalization.

Conclusion: **found existing generic building blocks**, with actual specialization/normalization experiments. No claim of global mathlib absence is made from an unavailable index or failed search. Native signatures and exact proof receipts distinguish an unweighted law, weighted law, and actual caller.

## Phase 5.5 — statement shape

Normal forms considered: entrywise `Matrix.of` sums, sums of row vectors followed by `detRowAlternating`, and arbitrary `MultilinearMap` evaluation. The bundled multilinear formulation is canonical for the abstract mathematical law; the entrywise determinant equality is convenient for rewriting the actual Wronskian matrix. RHS is the fully expanded finite-choice sum, so rewrite orientation respects the intended normal form.

Syntactic generality attempts: arbitrary finite square index, row-dependent summand types, unweighted row-vector expansion followed by scalar extraction, and fully abstract weighted multilinear formula. The first two are mechanical theorem widenings; the abstract route is existing API plus explicit normalization. Superfluous arguments: no unused original hypothesis; `l` is replaceable by `J`, while `A, ι, s, c, N` all carry necessary data. `CommRing` is an interface constraint for this determinant, not a droppable field-style artifact.

Statement-shape verdict: normal form **OK** for a determinant convenience theorem; syntactic generality **RESTATE** to arbitrary finite/dependent indices if accepted upstream; superfluous arguments **NONE**. Overall **RESTATE-BEFORE-SHIP**.

## Phase 6.0 — explicit callers and inline audit

| Caller | Actual use and plan |
|---|---|
| `Roth/GenWronskian.lean:245`, private `Roth.wronskian_kronecker_eq_sum_aux` | `det_sum_rows s c (fun μ d ν ↦ kronecker k (hasseDeriv d (φ ν)))` supplies the matrix expansion; `simpa` rewrites Wronskian definitions and algebra-hom determinant transport. A standalone replay of this entire caller uses generic multilinear expansion instead and was actually tested. |

External-to-declaring-file count: **0**. Same-file explicit use: **1**. Internal count under the command's strict excluding-declaring-file convention: **0**, which must not hide the one live same-file caller. The exact canonical audit independently scans all293 written declarations, preserving private names and exact order; the sole direct consumer agrees. This is direct source/kernel-expression evidence, not a claim about complete transitive simp dependency closure.

Inline-derivation audit: no other production derivation of the same simultaneous weighted row expansion was found. Scratch declarations under `.lake` are excluded from production callers. A single live caller is a weak signal for a public convenience API, but does not prove dead code. Its downstream use is the final nonvanishing generalized Wronskian theorem.

## Phase 6 — composition experiments

1. The original weighted proof uses `map_sum_finset`, then `map_smul_univ` under a finite sum, then function/matrix/scalar normalization. Mathematical laws: two; representation steps: explicit simplification and congruence. It is not an unverified direct application of one existing weighted determinant theorem.
2. The initial isolated source proved arbitrary finite `J` weighted expansion, but its direct unweighted `simpa only [Matrix.det, Finset.sum_fn] using …` failed with a coercion/`Matrix.of` type mismatch. The complete raw receipt, including recovery `sorryAx`, is retained only as **rejected evidence**. The clean accepted source is separate; no failed theorem is counted as proved.
3. The one-shot weighted determinant simp attempt **failed** with a normalization type mismatch, and is retained as rejected evidence. The explicit clean unweighted bridge and the arbitrary finite/dependent weighted bridge **passed**. Exact original `Fin l` recovery from the strongest dependent helper **passed** in mathlib-only isolation. The first direct caller rewrite failed; a separate clean caller replay **passed** after establishing the exact weighted matrix equality locally and applying the original caller normalization. All statuses and immutable receipts are in [verification](../evidence/Roth.det_sum_rows/verification.json).
4. Abstract weighted expansion through `F.map_sum_finset` and `map_smul_univ` is a closing simp composition. Phase6b explicitly classifies this pattern as **trivial simp composition; human decides if worth a lemma**. A native successful simp proof does not silently turn into a ≤3 existing-call term without normalization.

Conclusion: **BORDERLINE trivial simp composition**. There is no supported claim of a bare ≤1-call exact weighted determinant replacement, nor a claim of a substantive new determinant theorem. The generic laws already exist. Parent `Roth.genWronskian` was assessed YES-but-generalise-first, so the special ModeB NO-parent re-aim rule does not apply here; this helper is in any event a theorem directly about mathlib matrices rather than that parent definition.

## Phase 7 — verdict and actionable alternatives

**BORDERLINE-needs-human**. The named theorem packages textbook multilinearity in a useful matrix syntax; its exact proof content consists of two existing generic laws plus normalization, and it has one live caller. Phase6b leaves this precise convenience-lemma decision open. Finite/dependent index generalization is verified and should be used if an upstream wrapper is wanted; it does not by itself establish a missing mathematical API.

1. Should mathlib expose a determinant-specific simultaneous weighted row expansion, despite the existing bundled multilinear sum/scalar laws and a single current caller?
2. Would a generic weighted `MultilinearMap.map_sum_finset` corollary be the preferred named convenience API, leaving determinant specialization to local normalization?
3. If a determinant convenience theorem is accepted, should its public statement use arbitrary finite square index and row-dependent summand types as verified here?

Concrete next actions depend on that API choice. For a determinant theorem, propose `Matrix.det_sum_smul_rows` in `Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean`, using the verified dependent statement; for a generic weighted theorem use `Mathlib/LinearAlgebra/Multilinear/Basic.lean` next to `map_sum_finset`. For a local-only decision, keep the helper private beside its sole caller in `Roth/GenWronskian.lean`, or inline the exact accepted caller replay and delete the public helper. The replay supplies the complete refactor template; do not replace it with a bare `map_sum_finset` call that omits normalization. No production refactor or upstream PR is performed by this assessment.

All phases are complete, with the verification status recorded separately. These three upstream API questions are design choices, not pending native checks or user permission requests.
