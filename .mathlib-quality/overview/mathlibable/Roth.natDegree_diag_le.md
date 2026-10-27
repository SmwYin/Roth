# Roth.natDegree_diag_le — canonical 93/293

**Verdict: BORDERLINE-needs-human.** The existing `MvPolynomial.aeval_natDegree_le`
already controls arbitrary univariate substitutions by total degree. The verified
remaining bridge from separate coordinate bounds to a total-degree bound is small
but is a proof with a multiset-count normalization. No old-form replacement with
at most three existing mathematical calls was established. Whether to add that
bridge upstream, or retain the application-facing local lemma, is an API choice.
This is a completed read-only assessment; upstream design questions do not mean
verification remains pending. Production and pins remain unchanged.

## Phase 0 — baseline and resolution

The shared successful `lake build` completed 2467 jobs with no reported warnings
or errors. Fresh hashes of all 17 source/pin inputs match its manifest:
[hash check](../evidence/Roth.natDegree_diag_le/input-hash-check.json),
[inputs](../evidence/Roth.natDegree_diag_le/inputs.json),
[build](../evidence/Roth.natDegree_diag_le/baseline-build.txt).
The target resolves to `Roth/CoeffNorm.lean:183`, a public theorem without sorry.
The complete declaring module collects coefficient norm, diagonal substitution,
and evaluation estimates. The complete explicit caller module is also archived:
[source](../evidence/Roth.natDegree_diag_le/source-module.lean.txt),
[callers module](../evidence/Roth.natDegree_diag_le/source-callers.lean.txt).
Canonical metadata is generated directly from tracked JSON, including private
names: [canonical entry](../evidence/Roth.natDegree_diag_le/canonical-entry.json),
[ordered snapshot](../evidence/Roth.natDegree_diag_le/canonical-snapshot.json).

## Phase 1 — statement and proof

For an integer polynomial in a finite family of variables, replace every variable
by the same univariate indeterminate. If the degree in variable j is at most
r(j), the resulting polynomial has natural degree at most the sum of the r(j).
This includes the zero polynomial, empty variable type, and zero coordinate bounds.

Full native type:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ},
  (∀ (j : σ), MvPolynomial.degreeOf j P ≤ r j) →
    (Roth.diag P).natDegree ≤ ∑ j, r j
```

`σ` indexes variables; its universe is already arbitrary. `Fintype σ` supplies the
finite sum. `P` is the input, `r` the coordinate bounds, and `hP` certifies each
bound. The integer coefficient type comes from the fixed parent `Roth.diag`.
The proof expands the diagonal as a sum of univariate monomials, bounds each
monomial degree by its exponent sum, and sums `monomial_le_degreeOf` followed by
`hP`. There is no coefficient cancellation assumption: cancellation can lower the
degree, which is why the result is an inequality.

The native original type, full proof, and standard axioms are preserved in
[original source](../evidence/Roth.natDegree_diag_le/native-original-executed.lean.txt)
and [original receipt](../evidence/Roth.natDegree_diag_le/native-original-success.json).
The receipt is complete (`partial=false`); earlier warm-file diagnostics are
preserved intact and not misrepresented as new experiments.

## Phase 2 — preliminary checks

SMALL: an auxiliary degree estimate for Lemma 9; no new structure or named main
result. The one-line definition test is **n/a: theorem**, not a definition; the
proof has six substantive tactic lines. The exhaustive literature scope is
unaffected by this classification. No cheap prefilter applies.

## Phase 3 — exhaustive literature

Every named channel was actually searched; no artificial ninth channel was added.
The optional mathematical second-opinion server is unavailable. Web archives
contain exact requests, response hashes/bytes/status, returned source locators,
and original short summaries only. No full article/search bodies are stored.
Returned URL queries were conservatively removed and redactions documented.

| Channel | Actual request / access | Result and relevance |
|---|---|---|
| General web, specific | `polynomial diagonal substitution degree sum partial degrees` | Diagonal and line restrictions are the standard context; some unrelated diagonal-form senses excluded. |
| General web, general | `multivariate polynomial composition total degree bound commutative ring` | Composition/total-degree is the broader algebraic form. |
| General web, aliases | `polynomial restriction to line degree at most total degree` | Goldreich manuscript §3.3 discusses line restrictions of bounded total degree. |
| ChatGPT math | n/a: `ask_chatgpt_math` unavailable | No second-opinion result claimed. |
| Local clean.tex | Full local search; §6 Lemma 9, lines 1407,1449,1455,1468 | Explicit diagonal substitution and `s≤Σr_j≤mr_1` in the remainder estimate. |
| nLab | `site:ncatlab.org/nlab polynomial degree substitution` | Polynomial entry gives free commutative algebra and substitution; direct open failed unsupported XHTML. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial ring universal property` | Returned shared nLab material; no distinct categorical degree theorem. No higher-category replacement inferred. |
| Stacks | `site:stacks.math.columbia.edu polynomial total degree substitution diagonal`; then `site:stacks.math.columbia.edu "polynomial rings" "degree"` | Contextual polynomial-ring material and unrelated separation/geometry; no exact diagonal-degree law located. |
| MathOverflow | `site:mathoverflow.net polynomial restriction line total degree` | Finite-field and polynomial-map degree discussions; near matches, no replacement theorem established. |
| Recent arXiv | `site:arxiv.org polynomial line restriction total degree after:2021-10-27 before:2026-10-28` | 2026 total-degree diagonal line test is a current application; not a source of a new coefficient assumption. |

[General queries](../evidence/Roth.natDegree_diag_le/web-0.json),
[nLab/nCatLab](../evidence/Roth.natDegree_diag_le/web-1.json),
[Stacks/MO](../evidence/Roth.natDegree_diag_le/web-2.json),
[recent arXiv](../evidence/Roth.natDegree_diag_le/web-3.json),
[direct opens and Stacks retry](../evidence/Roth.natDegree_diag_le/web-4.json),
[local source hash](../evidence/Roth.natDegree_diag_le/local-literature-source.json),
[local excerpt](../evidence/Roth.natDegree_diag_le/local-literature-excerpt.txt).

Primary locators: [Goldreich manuscript §3.3](https://www.wisdom.weizmann.ac.il/~oded/PDF/pt-v3.pdf)
(search access only; direct fetch timed out),
[Chambert-Loir commutative algebra notes, polynomial degree discussion](https://webusers.imj-prg.fr/~antoine.chambert-loir/publications/teach/sv-commalg.pdf)
(search access only), [nLab polynomial](https://ncatlab.org/nlab/show/polynomial)
(search access only), and [Fu–Yu–Zhao, arXiv:2609.27129 abstract](https://arxiv.org/abs/2609.27129)
(successful direct open; submitted September 22, 2026 and revised October 19).
The recent paper discusses total-degree diagonal line tests; this is contextual
application evidence, not proof of the elementary commutative-semiring theorem.

Literature summary: this is degree control under polynomial substitution,
specialized to a line. Total degree controls line restriction; separate coordinate
degrees give the looser sum bound needed locally. Sources vary between fields
(for functions and low-degree testing) and commutative rings (formal polynomial
algebra). The semiring extension below is established by Lean, rather than
attributed to field-specific papers. Formal polynomial degree is essential:
polynomial functions over finite fields can have multiple presentations.

## Phase 4a — parameter and hypothesis audit

| Parameter | Current form | Assessment |
|---|---|---|
| `σ : Type*` | Arbitrary universe/type | Already general; no `Fin m` restriction needed. |
| `Fintype σ` | Finite whole variable family | Needed to spell the finite sum unchanged; stronger total-degree form removes it entirely, verified. |
| Integer coefficients | Fixed by `diag` parent | Expanded `aeval` statement works over arbitrary `CommSemiring R`, verified. This does not edit the fixed parent interface. |
| `P` | Arbitrary polynomial | Essential input, including zero; no nonzero premise required. |
| `r : σ → ℕ` | Natural coordinate bounds | Matches natural degree and zero-safe conclusion; no positivity required. |
| `hP` | All coordinate degree bounds | Essential to the sum bound. E.g. one variable `X`, r=0 disproves dropping it. Total-degree bound is an alternative input. |

## Phase 4b — verified generality

The expanded representation is strictly more general than the integer parent
interface. Both the coefficient weakening and stronger intermediate compile:

```lean
variable {σ R : Type*} [CommSemiring R]
-- No finiteness assumption:
(aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).natDegree ≤ P.totalDegree
-- With Fintype σ and coordinate bounds:
(aeval (fun _ ↦ (Polynomial.X : Polynomial R)) P).natDegree ≤ ∑ j, r j
```

[Raw executed proofs](../evidence/Roth.natDegree_diag_le/native-raw-executed.lean.txt)
and [raw receipt](../evidence/Roth.natDegree_diag_le/native-raw-success.json)
show the original support/monomial method over arbitrary commutative semirings.
The isolated document imports mathlib only and guards both project names absent.
The copied expansion helper is a newly proved experimental helper, **not** an
existing mathlib block. Root corrected the proposed total-degree proof before
execution: `Finsupp.degree_eq_sum` needs `Fintype`; definitional `change` followed
by `le_totalDegree` avoids that assumption. There was no failed native attempt.

More decisively, [existing-API source](../evidence/Roth.natDegree_diag_le/native-existing-executed.lean.txt)
and [receipt](../evidence/Roth.natDegree_diag_le/native-existing-success.json)
verify the same total-degree conclusion by specializing existing
`aeval_natDegree_le` with `m=P.totalDegree`, `n=1`. A separately proved
`total_bound` converts coordinate bounds through degrees multiset cardinality.
That helper is new and is never counted as already in mathlib. An integer
specialization and complete caller replay compile in the consumer set.

No stronger algebraic assumptions (`IsDomain`, characteristic zero, nontriviality,
negation, order on coefficients) are used. `CommSemiring` is the ambient API floor
for these `MvPolynomial`/`aeval` expressions; a noncommutative polynomial theory
would be a different representation, not a mechanical drop. No unjustified
further weakening is proposed. Cost does not determine the verdict.

## Phase 4c — all nine modern-idiom questions

| # | Diagnostic | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles | Already uses `Fintype`; expanded coefficient type uses `CommSemiring`, the existing hierarchy. No custom class needed. |
| 2 | Filters/nets instead of metric sequences | No: finite algebraic degree estimate has no topology or limits. |
| 3 | Universal property instead of construction | `aeval` is the appropriate algebra homomorphism; exposes existing `aeval_natDegree_le`, rather than a new construction. |
| 4 | Bundled substructure instead of closure predicate | No new bundled structure required. Degree-bounded submodules/filtrations could package families but would not remove the coordinate-to-total bridge. |
| 5 | Weaken fields/rings through hierarchy | Yes: integer expression expands to `CommSemiring R`; works for ℕ and rings with zero divisors, verified. |
| 6 | Higher-categorical generalization | No: substitution universal property is already expressed by `aeval`; no higher coherence enters this inequality. |
| 7 | Generalize concrete indices | `σ` is arbitrary already. ℕ degrees encode exponents and cannot simply become arbitrary ordered indices. |
| 8 | Concrete-via-abstract proof diagnostic | Yes: after `rw [diag_eq_sum]`, zero occurrences of `diag` or `ℤ` remain in the proof. The proof uses support and degree bounds only; generic and total forms compile. The strongest substitution law found is already in mathlib. |
| 9 | False-generalization guard | No semantic mismatch for semiring `aeval`, verified integer recovery. Reject equality with total degree: `X₁-X₂` can vanish on the diagonal. Do not confuse restriction to a line with extraction of diagonal coefficients in a power series. |

Modern idiom is available and already largely implemented: `aeval_natDegree_le`
controls all substitutions, not only the diagonal. This improves actual downstream
composition by separating the reusable substitution bound from the coordinate
bound conversion. The sole caller can supply the latter for a Hasse derivative.
No new category or class abstraction improves that concrete application.
Detailed machine-readable rows: [generality](../evidence/Roth.natDegree_diag_le/generality.json).

## Phase 4.5 — infrastructure risk

Theorem n/a. Six required risk checks are recorded explicitly:

| Risk | Result and rationale |
|---|---|
| Typeclass diamond | n/a: theorem adds no instance or class path. |
| Reducibility leak | n/a: proof in Prop introduces no new data definition/reducible alias. |
| Noncanonical unfolding | n/a: no new unfolding rule is added; existing parent `diag` is handled explicitly. |
| Instance priority collision | n/a: no instance or priority is declared. |
| Universe issues | n/a: no new type constructor; existing variable universes remain arbitrary. |
| Coercion ambiguity | n/a: no coercion is introduced. |

Overall n/a for the assessed theorem, not a claim about all possible future defs.

## Phase 4.6 — all five proof-strategy questions

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus substructures | Degree proof is naturally coefficient/support based; a filtration restatement is optional packaging, not needed at the caller. |
| 3 | Sequences versus nets | No convergence. |
| 4 | Construction versus universal property | Use existing `aeval` and its degree theorem, rather than reproving expansion each time. |
| 5 | Missing helper API | A named coordinate-to-total-degree bound (`totalDegree_le_sum_degreeOf` or bounded variant) would make the caller substantially cleaner; experimental proof verified, no existing exact name asserted. |

REFACTOR-RECOMMENDED: reuse `aeval_natDegree_le` after deriving the total-degree
bound; retain the support argument as valid independent proof evidence.
The possible missing API is the short conversion theorem, not a new substitution
or diagonal-degree engine. Whether to publish that conversion is the open API
choice; no claim of exhaustive mathematical absence is made.

## Phase 5 — actual five-method mathlib search

[All 12 formal requests and raw receipts](../evidence/Roth.natDegree_diag_le/formal-search.json)
contain three query forms per API method; receipts are archived individually as
`search-01.json` through `search-12.json`. These are actual searches, not a list
of suggested commands. The first exploratory searches were repeated for durable
receipts; no changed search conclusion resulted.

| Method | Current / standard / abstract forms | Result |
|---|---|---|
| Lean-Finder | diagonal degree ≤ sum partial degrees; substitution total-degree bound; commutative-semiring evaluation law | Finds `MvPolynomial.aeval_natDegree_le` and `totalDegree_le_degrees_card`. |
| Loogle | `Polynomial.natDegree, MvPolynomial.aeval`; `MvPolynomial.totalDegree, Multiset.card`; `MvPolynomial.aeval_natDegree_le` | Actual generalized evaluation theorem hit; multiset cardinality near match. |
| LeanSearch | diagonal specialization vs total degree; total versus coordinate degrees; evaluation hom degree m*n | Finds generalized evaluation law and related total/coordinate-degree API. |
| rg | Current diagonal/aeval names; literature degree/multiset forms; abstract degree transport; full-name check | Existing theorem is in **RingTheory/Polynomial/Basic.lean:898**, missed by an initial Algebra-only search. No exact old qualified target found. |
| local name patterns | `natDegree_diag`; `aeval_natDegree`; `totalDegree_le` | Returns project/nearby names but reports index unavailable. That limitation is not absence evidence. |

Source receipts:
[current](../evidence/Roth.natDegree_diag_le/rg-current.json),
[literature](../evidence/Roth.natDegree_diag_le/rg-literature.json),
[abstract](../evidence/Roth.natDegree_diag_le/rg-abstract.json),
[untruncated full name](../evidence/Roth.natDegree_diag_le/rg-full-name.json),
[pinned source hashes](../evidence/Roth.natDegree_diag_le/mathlib-inputs.json).
External indexes may differ from this pin; every positive candidate used in a
proof was checked natively against this project pin.

Pinned existing candidate:

```lean
MvPolynomial.aeval_natDegree_le
  (F : MvPolynomial σ R) (hF : F.totalDegree ≤ m)
  (f : σ → Polynomial R) (hf : ∀ i, (f i).natDegree ≤ n) :
  (MvPolynomial.aeval f F).natDegree ≤ m * n
```

Other pinned blocks actually used:
`MvPolynomial.totalDegree_le_degrees_card` (`Algebra/MvPolynomial/Degrees.lean:445`),
`MvPolynomial.degreeOf_def` (same file:220),
`Multiset.sum_count_eq_card` (`Algebra/BigOperators/Group/Finset/Basic.lean:1096`),
`Finset.sum_le_sum`, and `Polynomial.natDegree_X_le`.
`totalDegree_rename_le` and `degreeOf_eq_natDegree` are genuine near matches but
require transport and do not independently close the original coordinate-bound
statement. No generic instance magically supplies that inequality premise.

Conclusion: mathlib already has the broader **substitution/total-degree law**;
the exact coordinate-bound specialization needs the verified normalization bridge.
No absent-theorem claim is inferred from negative searches or unrun automation.
The optional `exact?` negative probe was deliberately not executed; this assessment
uses positive elaborated proofs and does not claim an exhaustive absence result.

## Phase 5.5 — statement shape

Normal form: `aeval` at constant `Polynomial.X` is canonical; the project spelling
is definitionally the same expression. Sum of coordinate bounds and total-degree
bound are related but are not interchangeable hypotheses by definitional equality.
No `↔` theorem is needed; RHS normal-form convention is n/a for an inequality.

Syntactic alternatives actually tried: arbitrary-coefficient diagonal sum bound,
stronger total-degree conclusion without `Fintype`, and existing generalized
substitution theorem specialized at n=1. The local sum-of-coordinate-bounds form
is convenient because `hdP` in MainLemma already supplies those bounds; the generic
mathlib form is more reusable because other substitutions fit immediately.

Superfluous-argument audit: arbitrary σ, P, and r are essential roles; hP cannot be
dropped; Fintype is needed for the unchanged sum expression but disappears from
the sharper total-degree version; integer specificity belongs to the fixed parent,
not the expanded proof; no hidden positivity/nontriviality hypothesis is needed.
Overall RESTATE-BEFORE-SHIP for any upstream contribution: prefer the generic
coordinate-to-total bridge and reuse existing evaluation API, rather than export
another integer `Roth.diag` wrapper.

## Phase 6.0 — callers and inline audit

Internal named-use count **1**, external-to-file count **1**, one distinct caller:

| Caller | Usage and refactor experiment |
|---|---|
| `Roth/MainLemma.lean:513`, private `Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux` | `(natDegree_diag_le _ hdP)` supplies a degree bound for the remainder coefficient estimate. Exact entire caller replay replaces this with experimental generic specialization; all other hypotheses and conclusion preserved. |

No duplicate inline derivation outside the target found by the degree/diagonal
patterns: [call grep](../evidence/Roth.natDegree_diag_le/rg-callers.json),
[inline grep](../evidence/Roth.natDegree_diag_le/rg-inline.json),
[caller table](../evidence/Roth.natDegree_diag_le/callers.json).

The runtime audit checks **293 entries, 293 unique Lean names, 293 present values**
in exact canonical order, preserving private names. It independently finds only
`_private.Roth.MainLemma.0.Roth.abs_coeff_diag_hasseDeriv_modByMonic_le_aux`
as a direct proof consumer. This is not transitive kernel/simp dependency closure.
The sole-use signal leans toward a local application wrapper, but is not sufficient
to prove it is a ≤3-call composition or dead code.

[Exact canonical array](../evidence/Roth.natDegree_diag_le/canonical-audit-array.lean.txt),
[consumer source](../evidence/Roth.natDegree_diag_le/native-consumers-executed.lean.txt),
[complete native receipt](../evidence/Roth.natDegree_diag_le/native-consumers-success.json).
The replay avoids the assessed target as an explicit proof call. The existing
experimental generic helper is included with its proof in the executed warm file;
it is never counted as an existing mathlib declaration.

## Phase 6 — actual composition experiments

1. **Support expansion.** The original proof and raw semiring version close by
   summing monomial degrees. Requires the expansion normalization, natural-degree
   sum bound, monomial bound, exponent-sum conversion, sum monotonicity, and
   coordinate degree bounds. This is a proof, not three existing calls. The copied
   `DiagSumRaw.generic` is new experimental evidence.
2. **Existing substitution theorem.** The total-degree conclusion follows from
   `aeval_natDegree_le P le_rfl (fun _ ↦ Polynomial.X)` and `natDegree_X_le`, followed
   by `mul_one` normalization. This is a genuine short existing-call specialization,
   but its RHS is `P.totalDegree`, not the original sum bound.
3. **Coordinate-to-total bridge and full recovery.** The executed `total_bound`
   uses `totalDegree_le_degrees_card`, `sum_count_eq_card`, `sum_le_sum`, and
   `degreeOf_def` normalization. Then the existing evaluation theorem and X bound
   recover the old statement. Counting only mathematical inequality/count facts
   gives five existing facts overall, plus normalization. Grouping the bridge
   under its new theorem name would falsely reduce the count. Exact integer
   specialization and the full sole caller compile.

No ≤3 existing-call old-form term established. This means **not established as
COMPOSABLE under the strict threshold**, not a theorem that no such term exists.
No closing `simp [defs...]` composition was found. If one were found, Phase 6b's
“trivial simp composition” rule would still require API judgment rather than an
automatic NO. The initial optional negative `exact?` preparation is archived as
unexecuted and contributes no verification evidence.

## Phase 7 — verdict and concrete next action

**BORDERLINE-needs-human**, independently assessed. The parent `Roth.diag` was
accepted as NO-composable-from-mathlib (canonical 76), not NO-mathlib-has-it:
[authoritative grouping/parent snapshot](../evidence/Roth.natDegree_diag_le/accepted-yes-grouping.json).
Thus no mandatory parent re-aim NO-has-it gate applies. The more general existing
`aeval` law is nevertheless an important independent positive hit. It does not
remove the need to derive its total-degree premise from the old hP interface.
The verdict is about the missing bridge API and wrapper placement, never proof
cost. No positive upstream proposal is justified merely by search failure.

1. Should mathlib add a generic `totalDegree ≤ ∑ j, degreeOf j P` theorem (and/or
   the coordinate-bound variant), so the existing `aeval_natDegree_le` directly
   serves this and other coordinate-bounded applications?
2. If that bridge is added, should the diagonal sum-bound wrapper remain only in
   `Roth/CoeffNorm.lean`, with the sole MainLemma caller using it for readability?
3. Should a generic constant-X corollary with RHS `P.totalDegree` be added for
   discoverability, despite its already verified short existing-call proof?

Next action: resolve these upstream API choices before proposing a PR. The
read-only assessment itself is complete, with unresolved verification `[]`.
Retain the current local theorem pending that design choice. If the bridge is
upstreamed, refactor the sole caller by deriving the Hasse derivative's total
bound and specializing `aeval_natDegree_le` at constant X and n=1; the current
consumer experiment gives a precise checked implementation template. Alternative
local destination: the current `Roth/CoeffNorm.lean`, where this application-facing
bound already belongs. No source deletion or caller edit was performed.

Conditional future bridge destination: `Mathlib/Algebra/MvPolynomial/Degrees.lean`;
any optional substitution corollary belongs near the existing law in
`Mathlib/RingTheory/Polynomial/Basic.lean`. These are design options, not a YES
verdict, reviewer assignment, or promised PR.

## Phase 8 — verification and handoff

Four complete accepted native sets: original, raw semiring/general form,
existing-API composition, exact integer specialization plus full caller and
canonical audit. Standard axioms only: `propext`, `Classical.choice`, `Quot.sound`.
No new axiom, sorry, unsafe, native_decide, raised limits, warnings, or errors in
accepted evidence. Root alone ran native Lean; all exact executed sources and raw
receipts are retained. No rejected native attempt occurred. Root's preexecution
proof correction and the declined optional negative probe are explicitly separated
from accepted evidence in [verification](../evidence/Roth.natDegree_diag_le/verification.json).

[Assessment](../evidence/Roth.natDegree_diag_le/assessment.json),
[overview entry](../evidence/Roth.natDegree_diag_le/overview-entry.json),
[current copy manifest](../evidence/Roth.natDegree_diag_le/copy-manifest.json),
[portable validator](../evidence/Roth.natDegree_diag_le/validate.py).
The validator checks current manifest hashes/bytes, report links, source/pin hashes,
complete native success, standard axioms, exact canonical order/private names,
phase rows, search/literature evidence, and the credential guard. Historical worker
manifests never replace the current manifest; integration-only root acceptance is
excluded from recursive worker coverage. Root independent acceptance is pending.
