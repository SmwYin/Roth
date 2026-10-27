# /mathlibable — Roth.wronskian_update_sub_smul

**Canonical 48; BORDERLINE-needs-human.** The determinant column-operation law is already in mathlib. The polynomial-family spelling requires a genuine matrix-entry bridge; the three direct normalization attempts failed. Keep this useful local rewriting lemma pending the finite-family Hasse-Wronskian API decision. This is an independent assessment, not inheritance from the two BORDERLINE parent definitions.

## Phase 0 — baseline and scope

Branch `ramin-cleanup`. Read all 224 lines of `Roth/Wronskian.lean`, including the complete sole calling theorem. No production, Git, pins, or overview changes were made. The saved successful baseline is `lake build`, exit 0, 2467 jobs; all 17 source/pin SHA256 values freshly match its input manifest. These are read-only assessment probes, not an upstream submission.

Evidence: [baseline](../evidence/Roth.wronskian_update_sub_smul/baseline-build.txt), [fresh hashes](../evidence/Roth.wronskian_update_sub_smul/source-pin-hashes.json), [input manifest](../evidence/Roth.wronskian_update_sub_smul/input-manifest.json), [entire source](../evidence/Roth.wronskian_update_sub_smul/source-wronskian.lean.txt), [canonical metadata](../evidence/Roth.wronskian_update_sub_smul/canonical-metadata.json).

## Phase 1 — comprehension

For a finite family of polynomials, replace one member by itself minus a constant scalar multiple of a different member. Its Hasse-Wronskian determinant is unchanged. Hasse derivatives are coefficient-linear, so this replacement subtracts the same scalar multiple of the corresponding column; alternating multilinearity makes the extra determinant zero.

Full native type (from the actual target check):

```lean
∀ {K : Type u_1} [Field K] {l : ℕ} {φ : Fin l → K[X]} {ν ν' : Fin l},
  ν ≠ ν' → ∀ (c : K),
  Roth.wronskian (Function.update φ ν' (φ ν' - C c * φ ν)) = Roth.wronskian φ
```

`K` is the coefficient field, `l` the family length, `φ` the family, `ν` the source column and `ν'` the destination column, `h` their distinctness and `c` any constant. No characteristic-zero, nonzero-family, independence or degree assumption occurs. The native replay uses only standard axioms. The only project mathematical definitions used are `Roth.wronskian` and `Roth.wronskianMatrix`; there is no preceding project theorem dependency.

The proof first identifies matrices by extensionality and linearity of `hasseDeriv`, then uses `Matrix.det_updateCol_add_smul_self` with `h.symm` and scalar `-C c`. The direction of `h.symm` is necessary because mathlib names the destination column first.

## Phase 2 — preliminary checks

SMALL: this is a helper named in Implementation notes, not one of the module's Main results; it introduces no structure and is not a named mathematical theorem. One-line-definition test: n/a, theorem (six substantive proof lines). Literature width remains exhaustive.

## Phase 3 — exhaustive literature search

Each exact request, returned response SHA256/byte count and safe locator is archived; full result bodies are deliberately not persisted. See [channel table](../evidence/Roth.wronskian_update_sub_smul/literature.json) and the seven web metadata artifacts listed there.

| Channel | Actual query / check | Finding |
|---|---|---|
| General, specific | `Wronskian subtract constant multiple column invariant Hasse derivatives` | Constant column replacement is the relevant identity; no stronger Hasse-specific assumption surfaced. |
| General, generality | `determinant commutative ring elementary column operation scalar multiple` | Elementary transvection law over a commutative ring. |
| General, aliases | `Wronskian change of basis determinant transvection invariant` | Wronskian transforms by the determinant of a constant change of family. |
| ChatGPT math | n/a: `ask_chatgpt_math` unavailable | No invented second opinion or historical assertion. |
| Local references | actual `rg` and relevant `clean.tex` section reading | §2 lines 174–194 eliminates equal leading degrees using constant column operations. |
| nLab | `site:ncatlab.org/nlab Wronskian determinant alternating multilinear` | Wronskian page gives the derivative matrix; determinant page gives alternating multilinearity. Direct Wronskian open failed with unsupported XHTML; indexed result was available. |
| nCatLab | `site:ncatlab.org/ncatlab determinant column operation`, retried `site:ncatlab.org/ncatlab "determinant"` | Returned nLab material, no separate nCatLab law. No higher-categorical restatement warranted. |
| Stacks | `site:stacks.math.columbia.edu determinant elementary matrix commutative ring`, refined determinants query and tag 0FJ9 open | §15.120 gives determinant modules and multiplicativity for finite projective modules; related abstraction, not this polynomial update theorem. |
| MathOverflow | `site:mathoverflow.net Wronskian constant change basis`, refined constant linear transformations | Basis-change factor discussed in question 347353; context only, not a primary proof source. |
| arXiv within 2021-10-26–2026-10-26 | Hasse/2022–2026 query and separate 2024/2025 Wronskian queries | Hermoso–Alcázar 2410.18867 (24 Oct 2024), §1–2 studies polynomial and Laurent polynomial Wronskians and constant linear changes. Kiselev 2510.02145 (2 Oct 2025) studies Wronskians as brackets, a different extension. |

Primary support: [Georgia Tech, Interactive Linear Algebra §4.1](https://textbooks.math.gatech.edu/ila/1553/determinants-definitions-properties.html) gives determinant invariance under row replacement and the transpose/column consequences. [Hermoso–Alcázar, 2024, §1–2](https://arxiv.org/html/2410.18867v1) writes the transformation factor for a constant matrix and the polynomial Wronskian over a characteristic-zero field. The local Hasse formulation retains the same column argument without requiring characteristic zero. [Stacks §15.120](https://stacks.math.columbia.edu/tag/0FJ9) supports the exterior-power perspective, not a claimed exact hit.

Standard concept: determinant invariance under an elementary column transvection. The polynomial law is its specialization using linear Hasse operators. Ordinary derivatives and Hasse derivatives give different determinants in general; the column-invariance principle applies to both, but their values must not be identified. No source supports allowing arbitrary polynomial multipliers in place of constants.

## Phase 4a–4b — parameters and generality

| Parameter / hypothesis | Current | Literature / abstract alternative | Verdict and evidence |
|---|---|---|---|
| `K : Type*` | arbitrary universe | arbitrary coefficient ring | Universe already polymorphic. |
| `[Field K]` | fixed parent interface | `[CommRing R]` for raw Hasse determinant | Clean native expanded ring proof succeeds. Simply changing the theorem instance cannot use the existing Field-bound parents. |
| `l : ℕ`, `Fin l` | first `l` derivative orders | any finite index and chosen row orders `r : ι → ℕ` | The operation only uses linearity of each selected row operator. Native arbitrary-finite-order probe verifies this representation. |
| `φ` | all polynomial families | unchanged | No degree/independence constraints needed. |
| `ν,ν'`, `h : ν ≠ ν'` | distinct columns | distinct alternating-map arguments | Essential: the same-index `Fin 1`, constant-one guard changes determinant 1 to 0. |
| `c : K` | any constant | any coefficient-ring element | Essential constant restriction: `[1,X]` becomes `[1,0]` when multiplying the first member by polynomial `X`; its Wronskian changes from 1 to 0. |
| char/nonzero assumptions | absent | absent | No further drops. Empty/singleton index sizes need no added hypotheses; distinctness may then be impossible. |

The raw statement is STRICTLY NARROWER THAN STANDARD: the ring and arbitrary finite row-order versions have actual native proofs. This does not certify a one-edit weakening of the public interface: parents 40/41 are independently BORDERLINE, and remain Field-bound. Proposed raw form is the determinant of `fun μ ρ ↦ hasseDeriv (r μ) (φ ρ)` over `[CommRing R]`, with the same update equality. The modern matrix form already has its column law in mathlib. Cost is not used to decide the verdict.

### Phase 4c — all modern-idiom rows

| # | Question | Answer / reformulation / concrete consequence |
|---|---|---|
| 1 | Typeclasses | Already typeclass based. Use CommRing in expanded representation; no new class. |
| 2 | Filters / topology | No: finite algebraic equality. |
| 3 | Universal property | Alternating-map structure characterizes the proof; not an object-construction theorem needing a new universal-property class. |
| 4 | Bundled substructures | No closure predicate or substructure in the statement. A bundled AlternatingMap is the relevant functional interface. |
| 5 | Fields to rings/modules | Yes: matrix determinant over R[X], with coefficient-linear row operators; admits zero divisors and positive characteristic. |
| 6 | Higher categories | No: determinant functors are related but do not improve this finite column update consumer. |
| 7 | Concrete index | Yes: arbitrary finite column index and row orders, rather than consecutive Fin orders; useful for generalized Wronskians and selected Hasse orders. |
| 8 | Concrete-via-abstract diagnostic | Fires: `wronskian` has zero explicit occurrences in the proof body (its matrix has two). After matrix identification the only fact is generic column invariance. `hasseDeriv` is used only through linearity. The native abstract AlternatingMap proof verifies this diagnosis. |
| 9 | False-generalization guard | Ring/selected-order versions preserve the determinant when specialized back. Ordinary derivative Wronskians must not silently replace Hasse ones. Arbitrary polynomial scalars are rejected; distinctness is retained. |

Modern idiom available, with real organizational benefit: the verified generic AlternatingMap update result applies once an appropriate alternating map is supplied, while matrix `updateCol` plugs directly into existing determinant API. Constructing a coefficient-ring-linear Hasse alternating map would be future work; no existing scalar-restriction API for AlternatingMap is claimed. Constructing a new bundled finite-family Wronskian is an upstream API choice, not evidence that the abstract law is missing. No new proposed helper is counted as an existing mathlib replacement.

### Phase 4.5 — infrastructure risks

n/a — theorem introduces no instance, definition, reducibility boundary or coercion. The six definition-only risks (diamond, reducibility leak, noncanonical unfolding, priority collision, universe constraints, coercion ambiguity) are not introduced here. Parent definition design is discussed separately, not inherited as a theorem risk verdict.

### Phase 4.6 — all proof-strategy rows

| # | Diagnostic | Answer |
|---|---|---|
| 1 | ε–δ vs filters | n/a: no topology. |
| 2 | Elements vs substructures | No ideal/submodule inclusion is being proved. Matrix entry extensionality is exactly the necessary representation bridge. |
| 3 | Sequences vs nets | n/a: no analysis. |
| 4 | Construction vs universal property | No categorical construction; bundled alternating form would expose reusable algebraic laws. |
| 5 | Missing helper API | Potential finite-family matrix/update compatibility lemma, conditional on accepting that family API. Generic determinant and AlternatingMap primitives already exist. |

Current strategy MATHLIB-IDIOMATIC: generic column theorem plus explicit entry bridge. A future bundled finite-family interface would make the consumer shorter by exposing multilinearity, but no missing abstract determinant law is established.

## Phase 5 — five actual formal methods, three forms

[Current raw receipt](../evidence/Roth.wronskian_update_sub_smul/formal-current.json), [literature receipt](../evidence/Roth.wronskian_update_sub_smul/formal-literature.json), [abstract receipt](../evidence/Roth.wronskian_update_sub_smul/formal-abstract.json). Exact queries and complete responses are preserved. External index versions can differ from the pin. Local search returned source hits with `index: unavailable`; this is not a proof of absence.

| Method | Current Hasse-family form | Literature column law | Modern abstract form |
|---|---|---|---|
| Finder | Hasse polynomial Wronskian update query; two-polynomial Wronskian near hits | Elementary column query hits `Matrix.det_updateCol_add_smul_self` | Alternating transvection query hits update-self/update-update laws |
| Loogle | `Polynomial.hasseDeriv, Matrix.det`: empty | `Matrix.det, Matrix.updateCol`: column update candidates | `AlternatingMap, Function.update`: update-sub/add/smul/self primitives |
| LeanSearch | Polynomial Wronskian invariance query finds generic determinant law | Scalar multiple of different column query finds same | Alternating update-sub query finds MultilinearMap.map_update_sub and AlternatingMap.map_update_smul |
| rg pinned source | [wronskian/hasseDeriv](../evidence/Roth.wronskian_update_sub_smul/rg-current.json): existing two-polynomial API | [det_updateCol](../evidence/Roth.wronskian_update_sub_smul/rg-literature.json): Basic.lean:478 exact generic law | [update primitives](../evidence/Roth.wronskian_update_sub_smul/rg-abstract.json): alternating/sub/smul/self/linear composition |
| local name pattern | `wronskian` | `det_updateCol` | `map_update` |

Pinned source candidate:

```lean
Matrix.det_updateCol_add_smul_self (A : Matrix n n R)
    {i j : n} (hij : i ≠ j) (c : R) :
    (A.updateCol i (fun k ↦ A k i + c • A k j)).det = A.det
```

Located at `Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean:478`, over `[CommRing R]`, `[Fintype n]`, `[DecidableEq n]`. Native `#check` and actual application verify the pin. Existing `Polynomial.wronskian` is binary and ordinary-derivative based; it is not an exact replacement for this arbitrary-family Hasse determinant. Search establishes positive usable building blocks; no global absence claim follows from empty searches.

## Phase 5.5 — statement shape

Normal forms considered: family `Function.update`, matrix `updateCol`, and bundled alternating-map update. The matrix law is canonical in the determinant API; the family form is convenient for the actual induction caller. Both sides normalize toward the original determinant on the RHS. Normal form OK conditional on retaining the family API.

Syntactic generality attempts: direct matrix law with negative polynomial constant; raw CommRing determinant; arbitrary finite selected Hasse orders; abstract alternating-map law. The public family update is easiest at Wronskian.lean:212 because induction is on polynomial families. A new helper must not be mistaken for an existing mathlib primitive.

Superfluous argument audit: type universe is already general; Field is mathematically stronger than needed but fixed by both parent definitions; Fin/consecutive orders can be generalized in expanded form; φ and c determine the operation; ν and ν' determine the columns; distinctness is essential. No CharZero/nonzero argument exists to drop. Overall RESTATE-BEFORE-SHIP if upstreaming a new family API: settle parent generality and use rings/selected orders. The existing local theorem can remain unchanged during this read-only survey.

## Phase 6.0 — all callers and inline audit

Internal use count excluding declaring file: **0**. Total explicit executable references: **1**, in the declaring module; external-to-file caller files: **0**. The module documentation at line 38 is one prose reference, not an executable use. The declaration at line 158 is not a use. [Untruncated caller/inline search](../evidence/Roth.wronskian_update_sub_smul/rg-callers.json).

| Caller | Actual use and proposed treatment |
|---|---|
| `Roth.wronskian_ne_zero_of_linearIndependent`, Wronskian.lean:205–215 (use at 212) | `rw [← wronskian_update_sub_smul hne ((φ ν').leadingCoeff / (φ ν).leadingCoeff)]` replaces the family by a lower-degree independent family. Retain this local rewrite while parent API is unsettled. If inlining later, establish precisely the updated-matrix equality using linearity, pass it through `congrArg Matrix.det`, compose with `Matrix.det_updateCol_add_smul_self ... hne.symm (-C c)`, and rewrite with its symmetric direction. Actual caller replay verifies the bridge without invoking the target. |

Inline-derivation audit: no duplicate family-update determinant proof found elsewhere; `updateCol`/generic column theorem occur only in this theorem. This is explicit source-reference accounting, not an exhaustive kernel/simp dependency closure. The theorem is not tagged simp. Its one caller is real use, not dead code.

## Phase 6 — actual composition experiments

1. Original proof replay succeeds. Generic column theorem plus matrix equality is the mathematical proof, but extensionality, updates, linearity and sign normalization are substantive bridge work, not three existing calls.
2. Direct `simpa [Matrix.updateCol_apply, Function.update_apply, apply_ite, ← smul_eq_C_mul, sub_eq_add_neg] using Matrix.det_updateCol_add_smul_self ...` fails: an unapplied updated row-function remains under `Matrix.of` on one side, versus an explicit conditional on the other.
3. Replacing `Matrix.updateCol_apply` with `Matrix.updateCol`, and then also replacing `Function.update_apply` with `Function.update`, fails with the same remaining row-function/conditional distinction. All rejected sources/receipts are separate; failure proves no mathematical absence.
4. Native CommRing expanded determinant succeeds with the original explicit bridge. It does not invoke the target and its guard confirms the project theorem is unavailable in the isolated environment.
5. Abstract alternating-map proof uses `map_update_sub`, `map_update_smul`, `map_update_self` **plus** `smul_zero`, `sub_zero`, and `Function.update_eq_self` normalization. That is not a strict three-fact term. Specializing it to the project family would additionally require constructing/identifying its alternating map. No new helper is counted as already existing.
6. Native arbitrary finite selected-row-order proof and sole-caller replay test the full representation bridge and practical refactor, with no original-target shortcut.

Conclusion: **NOT-COMPOSABLE in the strict ≤3-existing-call sense established here.** The generic determinant form already exists, but the old family spelling is not definitionally that law. Phase 6b says that even a closing `simp [defs...]` composition would be BORDERLINE; the actual tested direct versions do not close. This is not an automatic YES: whether the thin family API deserves upstream surface remains the parent-design question.

## Phase 7 — verdict and action

**BORDERLINE-needs-human.** The generic law is exactly present, but the existing Field-bound finite-family definitions are themselves BORDERLINE, not NO-mathlib-has-it. Therefore the explicit parent re-aim NO gate does not apply. The old form requires an independently verified nondefinitional bridge and no strict ≤3-fact existing composition was established. Literature confirms a useful standard column law; it does not decide which finite-family interface mathlib should expose.

Numbered future upstream API questions (read-only assessment is complete; no user response is needed now):

1. Should mathlib expose a finite-family Hasse-Wronskian over CommRing, with arbitrary selected derivative orders, alongside the binary ordinary Wronskian?
2. If that API is accepted, should column-update invariance be a named family rewrite, or follow from a bundled alternating map with generic update laws?
3. Should the polynomial-family-to-matrix update compatibility be public API or remain a local bridge in the family theorem proof?

Alternative local destination: retain `Roth/Wronskian.lean:158`, where the hard independence induction needs exactly this rewrite. No deletion is authorized by this assessment. If the family API is accepted upstream, develop its ring/finite-index interface first, then assess this law in that interface; do not submit a duplicate raw determinant law. Accepted YES items 43 (`det_choose_eq`), 46 (coefficient formula), and 47 (distinct-degree nonvanishing) are potential later Wronskian-package companions, not evidence that this law is YES. They are listed from actual progress, not name-based inference.

## Phase 8 — completion and verification

Exact executed native sources and complete raw receipts are linked by [verification.json](../evidence/Roth.wronskian_update_sub_smul/verification.json). Accepted runs have clean success, no partial/warming result, no errors/warnings, and standard axioms only; rejected experiments are preserved separately. Original target/type/axioms, CommRing representation, abstract law/essential-distinctness guard, finite selected orders and actual sole-caller bridge have been checked by root's serial native workflow. No circular own-target proof is accepted.

All formal methods and literature channels, modern-idiom/strategy/shape checks, callers and composition experiments are complete. `unresolved: []` records verification completion, not resolution of future API-design questions. The package includes full source/pin and mathlib hashes, evidence link checks, credential-safe URL metadata, the [tracked secret-guard receipt](../evidence/Roth.wronskian_update_sub_smul/secret-scan-receipt.json), a [portable read-only validator](../evidence/Roth.wronskian_update_sub_smul/validate.py), and the [current copy manifest](../evidence/Roth.wronskian_update_sub_smul/copy-manifest.json). Root independent acceptance remains pending. All evidence files are listed in the current copy manifest; historical worker manifests do not override it.
