# Full mathlibable assessment: `Roth.diag`

Canonical declaration **76/293**, public noncomputable definition at `Roth/CoeffNorm.lean:161`.
**Verdict: NO-composable-from-mathlib.** The integer-only function is one application of existing
`MvPolynomial.aeval`. Its useful project-local semantic name does not establish a missing upstream
construction. This source-frozen survey changes no production definition, theorem, instance or pin.

## Phase 0 — Baseline and resolution

The baseline `lake build` at `99f19fda4b3cbee38fc0d31af76075834f5cc265` completed successfully
with 2467 jobs, no warnings/errors. All **17 production source/pin hashes freshly match** that
baseline: [build](../evidence/Roth.diag/baseline-build.txt),
[inputs](../evidence/Roth.diag/inputs.json), [hash check](../evidence/Roth.diag/input-hash-check.json).
The unique production definition resolves and has no unproved placeholder. The entire declaring
module was read, together with actual MainLemma consumers. It develops coefficient norms, Hasse
bounds, diagonal specialization and evaluation bounds for the Roth main lemma.
[Module](../evidence/Roth.diag/source-module.lean.txt),
[caller module](../evidence/Roth.diag/source-callers.lean.txt).

## Phase 1 — Mathematical comprehension and full native type

For an integer polynomial in an arbitrary set of variables, replace every variable by a single
indeterminate t. Thus a monomial with coefficient a and multi-exponent d becomes a times t to
the sum of the exponents. Different monomials can collide and their coefficients add, so this
operation can lose information and can lower degree through cancellation.

Native full type and body:

```lean
Roth.diag.{u_1} : {σ : Type u_1} → MvPolynomial σ ℤ → Polynomial ℤ
fun {σ} P ↦ (MvPolynomial.aeval fun _ ↦ Polynomial.X) P
```

The parameters are the universe-polymorphic variable type σ and polynomial P; there are **no
explicit assumptions**, finite-variable restriction, nonzero condition, degree bound or
DecidableEq binder. Integer ring and polynomial algebra instances are inferred. This returns
polynomial data, not a proposition. Native resolution, `#print`, `#print axioms`, original
recovery and arbitrary predicate-context transport are retained in
[target source](../evidence/Roth.diag/native-target-executed.lean.txt) and
[target receipt](../evidence/Roth.diag/native-target-success.json).

## Phase 2 — Size and one-line definition gate

**BIG**: a named operation listed among the module's main definitions, representing restriction
to a diagonal; exhaustive literature is mandatory regardless of this classification. Its body
has **one substantive line**.

| Exemption | Applies? | Actual evidence |
|---|---|---|
| Avoid defeq abuse | No demonstrated need | The original body and generalized replacement are definitionally equal at ℤ (`rfl`). Existing proofs explicitly unfold `diag` in the expansion, evaluation and vanishing arguments; there is no sealed representation barrier. |
| Avoid typeclass diamonds | No | This creates a function, not a typeclass, instance, new type or competing polynomial algebra structure. |
| Semantic intent / API stability | **Yes** | Five CoeffNorm declaration consumers and six MainLemma consumers use the diagonal operation; `abs_coeff_diag_le` and `exists_ne_modByMonic_eq` benefit from the readable name. |

Conclusion: **ONE-LINER WITH-EXEMPTION**. That exemption establishes legitimate local API value,
but does not make a one-call specialization of an existing universal operation new mathematics.

## Phase 3 — Exhaustive literature protocol

Exact requests, original response SHA256/UTF8 byte counts, URLs, concise original summaries and
access limitations are retained in [web0](../evidence/Roth.diag/web-0.json),
[web1](../evidence/Roth.diag/web-1.json), [web2](../evidence/Roth.diag/web-2.json),
[web3](../evidence/Roth.diag/web-3.json), [web4](../evidence/Roth.diag/web-4.json), and
[web5](../evidence/Roth.diag/web-5.json). Full third-party response/article bodies are not archived;
returned URL queries/fragments are omitted to avoid retaining signed download credentials.

| Required channel | Actual query/action | Finding and limits |
|---|---|---|
| General web: specific | `multivariate polynomial diagonal specialization P(t t) all variables same variable ring homomorphism` | Primary polynomial-ring notes and the free-algebra construction give generator assignment as the relevant mechanism. |
| General web: general | `polynomial ring universal property arbitrary commutative ring evaluate variables algebra homomorphism` | Primary Altman–Kleiman text §1.3 gives the universal property with an arbitrary variable index set and ring map on coefficients. |
| General web: aliases | `diagonal specialization polynomial total degree sum exponents restriction diagonal` | Restriction/substitution language; no separate structure forced. Distinguish coefficient diagonal extraction, which is a different operation. |
| `ask_chatgpt_math` | Unavailable, optional channel permitted to be skipped | No second opinion fabricated. |
| Local references | `same variable`, `diagonal substitution`, `resulting polynomial` searches in `clean.tex` | §6 proof of Lemma9, lines1449 and1505–1511, explicitly substitutes all variables by x, then uses linearity and vanishing at α. [Excerpt](../evidence/Roth.diag/local-literature.txt), [hash](../evidence/Roth.diag/local-literature-source.json). |
| nLab | `site:ncatlab.org/nlab polynomial algebra universal property` | Indexed polynomial entry defines free commutative R-algebra on any set and substitution via generator assignment. Direct page open failed HTTP400 unsupported XHTML; search-index content was available. |
| nCatLab namespace | `site:ncatlab.org/ncatlab polynomial ring free commutative algebra`; follow-up polynomial/substitution | Returned nLab and other namespaces, no relevant nCatLab-namespace target. No higher-categorical replacement justified. |
| Stacks | Polynomial-ring universal/mapping-property searches, followed by exclusion of divided-power results | Returned divided-power analogues, not this ordinary-polynomial operation. A direct tag00DX inspection was Cayley–Hamilton and is explicitly excluded as irrelevant. No exact Stacks generality source claimed. |
| MathOverflow | `site:mathoverflow.net polynomial "diagonal" "specialization"`, then reordered query | Related symmetric-polynomial specialization and Wronskian restriction discussions; no exact canonical diagonal-map API or generality source. These are supplementary, not the primary mathematical basis. |
| Recent arXiv, five-year window | Both `"diagonal specialization"` and `"diagonal substitution"` with `after:2021-10-27 before:2026-10-28` | Primary Jiang2026 arXiv2609.10609 §1 explicitly sets u=v=x, and §3 Proposition3.1 uses the same substitution. Other subrank/discrepancy hits are not evidence for this exact operation. |

Primary sources:

- [Altman–Kleiman, *A Term of Commutative Algebra*](https://stuff.mit.edu/afs/athena/course/18/18.705/www/13Ed.pdf),
  §1.3, printedp2/PDFp9: arbitrary-index-variable polynomial universal property. The PDF states
  version September2013; search freshness is not treated as its publication date.
- [*The universal properties of polynomial rings and group rings*](https://fenix.tecnico.ulisboa.pt/downloadFile/845043405563825/ring_algebras2.pdf),
  Proposition2.1/Note2.2, PDFp3: univariate algebra evaluation and the free-algebra property.
- [Jiang, *Real stability of layer-refined antichain polynomials for three-chain products with a two-element factor*](https://arxiv.org/html/2609.10609v1),
  September2026, §1 lines55–63 and §3 Proposition3.1: diagonal specialization u=v=x.

Synthesis: **diagonal specialization / restriction to the diagonal** is standard. The structural
form is the algebra homomorphism sending every generator to one common element, here the target
polynomial indeterminate. Ring-text sources use arbitrary commutative rings and arbitrary
variable sets; mathlib's verified semiring implementation gives the exact weaker algebraic
requirements. The recent real-coefficient application is not evidence for semiring generality.
This is **not coefficient-diagonal extraction** of a multivariate generating series.

## Phase 4a–4b — Generality and actual verification

| Parameter | Current | Verified broader form / boundary |
|---|---|---|
| Variable type σ | Arbitrary `Type u` | Already arbitrary, including empty and lifted-universe types. No Fintype/Finite/DecidableEq to drop. |
| Coefficients | ℤ | Any `[CommSemiring R]` supports the same body, checked natively; original recovery is `rfl`. |
| Destination | `Polynomial ℤ` | `Polynomial R` for the same diagonal polynomial. Evaluation afterwards may target any commutative R-algebra S, verified by the generic composition law. |
| Common image of generators | `Polynomial.X` | General `MvPolynomial.aeval` already accepts every assignment into any commutative R-algebra. Arbitrary assignments are a broader operation, not another definition of this particular diagonal map. |
| Degree/nonzero | None | No assumptions to remove. Collapse is not injective for Bool variables over ℤ; no general degree-equality claim. |

**STRICTLY NARROWER THAN STANDARD** as a data-construction interface; the verified broader body is:

```lean
noncomputable def generalized {σ R : Type*} [CommSemiring R]
    (P : MvPolynomial σ R) : Polynomial R :=
  MvPolynomial.aeval (fun _ ↦ Polynomial.X) P
```

This is CHEAP same-body generality, not a guess based on unused syntax. Arbitrary independently
universe-polymorphic types, ℕ coefficients, empty/lifted variables, exact ℤ recovery, and
arbitrary algebra-target evaluation all compile without extra limits. No noncommutative
coefficient generality is claimed. [Generality](../evidence/Roth.diag/generality.json),
[naturality source](../evidence/Roth.diag/native-naturality-executed.lean.txt),
[receipt](../evidence/Roth.diag/native-naturality-success.json).
The final bucket is NO-composable because existing aeval already supplies that whole construction,
not because generalization costs time or because changing downstream files would be inconvenient.

## Phase 4c — All nine modern-idiom diagnostics

| # | Diagnostic | Finding / concrete downstream consequence |
|---|---|---|
| 1 | Typeclasses for preambles | Yes: CommSemiring R expresses coefficient structure; no explicit bespoke predicate or new instance required. |
| 2 | Filters/nets instead of metric notions | No topology or limits occur. |
| 3 | Universal property instead of construction | Already available: `MvPolynomial.aeval` is the universal generator assignment. Retaining the bundled AlgHom exposes map_add/map_mul/map_sub. No new universal-property class needed. |
| 4 | Bundled substructures | No closure-predicate subset is involved. The useful bundle is an AlgHom, already returned by aeval before applying P. |
| 5 | Field/vector-specific to semiring/module | Yes: ℤ specialization broadens to CommSemiring R with the identical body and rfl recovery. |
| 6 | Higher categorical formulation | No demonstrated benefit for this finite-support algebra operation; existing AlgHom composition suffices. |
| 7 | Concrete index to abstract structure | σ is already arbitrary. Natural polynomial exponents are the intended free commutative monoid; generalized monoid algebras are another representation, not necessary to repair this formula. |
| 8 | Concrete-via-abstract diagnostic | Yes: the body contains no `diag` self-reference and no integer arithmetic, only aeval and X. The ℤ token occurs in the signature; arbitrary CommSemiring R was actually verified. |
| 9 | False-generalization guard | Passed for coefficient broadening: still sends every variable to the same polynomial X, exact recovery. Reject replacing diagonal by coefficient extraction, an equivalence, or an injective variable rename. Native Bool counterexample verifies loss of injectivity. |

Modern idiom is useful but **already implemented**, not a new contribution: keep aeval bundled
when proving algebraic laws, use `comp_aeval_apply` for subsequent evaluation, and use the
semiring-parametric interface when coefficient bounds do not force ℤ.

## Phase 4.5 — Six infrastructure-risk rows

| Risk | Verdict | Actual check |
|---|---|---|
| Typeclass diamond | None | Function data introduce no instances. Existing canonical `Algebra ℕ (Polynomial ℕ)` synthesis and typed aeval application succeeded. |
| Reducibility leak | Low | Ordinary noncomputable def, no reducible attribute or custom reducibility. Original/body and eval₂Hom representations are rfl; consumers already unfold deliberately. |
| Noncanonical unfolding | Low | Substitution into generic predicate contexts is `Iff.rfl`; no conflicting simp definition installed. A second named wrapper could duplicate API, so prefer existing aeval upstream. |
| Instance-priority collision | None | No instance declaration or priority introduced; synthesis uses existing polynomial algebra structure. |
| Universe polymorphism | None observed | Native Type0/PEmpty and arbitrary `ULift.{u} Unit` variable applications, with independently polymorphic coefficients, succeed. |
| Coercion ambiguity | Low | aeval already has canonical AlgHom-to-function coercion; explicit typed function, eval₂Hom and bundle-composition forms compile. No new CoeFun/CoeSort instance installed. |

Overall **LOW**, no HIGH rows. Actual
[infrastructure source](../evidence/Roth.diag/native-infrastructure-executed.lean.txt) and
[receipt](../evidence/Roth.diag/native-infrastructure-success.json) also prove the Bool
noninjectivity boundary. This is checked behavior, not a claim that all import permutations
or all hypothetical future typeclass instances were tested.

## Phase 4.6 — All five proof-strategy rows

| # | Question | Finding / cost |
|---|---|---|
| 1 | Topology ε–δ versus filters | n/a: no topology. |
| 2 | Element algebra versus structural maps | Already uses universal AlgHom; retain bundle for map laws. CHEAP interface presentation improvement. |
| 3 | Sequences versus nets | n/a: no sequences/limits. |
| 4 | Construction versus universal property | Already idiomatic aeval; no manual coefficient-based construction to replace. |
| 5 | Helpers mathlib should supply | No missing helper required to define operation or evaluate its result. Coefficient and degree bounds are distinct subsequent declaration assessments. |

Strategy **MATHLIB-IDIOMATIC**. The declaration is a definition rather than a proof, but all
applicable construction-strategy questions were checked. No API gap is invented to justify it.

## Phase 5 — All five formal methods, all three forms

Full requests/results are in [formal search](../evidence/Roth.diag/formal-search.json).

| Method | Current / literature / abstract queries | Actual results and limitations |
|---|---|---|
| Lean-Finder | diagonal substitution; arbitrary-semiring specialization; universal generator assignment | Returned eval₂_eta, rename/unique-variable infrastructure, and unrelated matrix/Witt diagonal APIs. None of those unrelated hits is counted as replacement. |
| Loogle | `MvPolynomial.aeval, Polynomial.X`; `MvPolynomial.pUnitAlgEquiv`; `MvPolynomial.aeval, AlgHom.comp` | Current query finds option/homogenization operations; standard identifier failed in external index, retained honestly. Retry `"uniqueAlgEquiv"` found current unique-variable API and application equation. Abstract finds comp_aeval and aeval_comp_rename. [Retry](../evidence/Roth.diag/loogle-standard-retry.json). |
| LeanSearch | all variables to X; collapse rename/one-variable identification; homomorphism by generator assignment | Finds aeval, comp_aeval_apply, rename and pUnitAlgEquiv in older external index. |
| Source rg | Current diag/diagonal substitution; uniqueAlgEquiv/rename; generic aeval/composition | Pinned Eval569 gives exact constructor; Equiv67 and Rename54 give alternate variable-collapse route. Full untruncated relevant-tree name grep retained. [Current](../evidence/Roth.diag/rg-current.json), [literature](../evidence/Roth.diag/rg-literature.json), [abstract](../evidence/Roth.diag/rg-abstract.json), [full name](../evidence/Roth.diag/rg-full-name.json). |
| Local name-pattern | diag; pUnitAlgEquiv; comp_aeval | Finds project target, unrelated diag names, and actual pinned generic APIs. Symbol index reports unavailable; source-backed positive results usable, empty results would not establish absence. |

Pinned source matters: **`pUnitAlgEquiv` is deprecated since2026-04-15** in favor of
`MvPolynomial.uniqueAlgEquiv R PUnit`. No deprecated API is used in accepted Lean probes.
[Eval source](../evidence/Roth.diag/mathlib-eval.lean.txt),
[Equiv source](../evidence/Roth.diag/mathlib-equiv.lean.txt),
[Rename source](../evidence/Roth.diag/mathlib-rename.lean.txt).
No claim of formal absence relies on search failure: the exact positive constructor itself is
compiled independently with no project import.

## Phase 5.5 — All statement-shape checks

**Normal form:** aeval at constant X is the direct universal-property normal form. Equivalent
forms are eval₂Hom Polynomial.C constant X (`rfl`), and rename-to-PUnit followed by uniqueAlgEquiv
(proved equality of bundles, not defeq). Orient any useful bridge towards aeval; avoid a web of
pairwise wrapper equivalences. This is data rather than an iff, so RHS convention is reflected
by the alternate-representation equality having aeval on the RHS.

**Syntactic generality:** compare pointwise polynomial function, bundled AlgHom, explicit
RingHom evaluation, and rename/equivalence composition. Keep bundled aeval for algebra laws,
apply it to P at arithmetic coefficient call sites. The pointwise current interface is readable
but ℤ-specific. **RESTATE-BEFORE-SHIP** if preparing a reusable API; no source change here.

**Superfluous arguments:** σ determines variable type and P is essential input. There is no
explicit typeclass or hypothesis to delete. ℤ is a fixed coefficient specialization, not an
unused binder; broader coefficient data are verified separately. No Fintype/DecidableEq
assumption is introduced by using a finite support expansion.

## Phase 6.0 — Actual callers, inline audit and refactor plan

There are **11 distinct named declaration consumers**: five in CoeffNorm and six in MainLemma
(**one external file**, K=6 distinct external-to-declaring-file consumers). This is neither a
raw occurrence count nor an assertion about opaque kernel or simp-dependency closure.
[Exact grep](../evidence/Roth.diag/rg-callers.json),
[per-caller plan](../evidence/Roth.diag/callers.json),
[inline audit](../evidence/Roth.diag/rg-inline.json).
The retained function-context theorem proves definitional substitutability for any proposition
about the functional, but it does not claim every caller was separately recompiled.

| Caller | Occurrence pattern / concrete replacement plan |
|---|---|
| CoeffNorm164–168 `diag_eq_sum` | Expansion conclusion and `rw [diag]`: replace by aeval-to-X, retain eval₂_eq and monomial collection. Full arbitrary-semiring expansion replayed in mathlib-only probe. |
| CoeffNorm174–179 `abs_coeff_diag_le` | Coefficient of diag in conclusion: replace by same aeval expression and use rewritten expansion; finite absolute-sum estimate unchanged. |
| CoeffNorm183–189 `natDegree_diag_le` | Degree of diag: substitute aeval expression and rewritten expansion; keep ≤ degree estimate. |
| CoeffNorm193–196 `eval_diag` | Polynomial map/eval of diag: substitute then use generic algebra composition/naturality; avoids induction. |
| CoeffNorm199–200 `diag_sub` | Three occurrences: `map_sub _ _ _` already proves substituted statement. Full scratch replay accepted. |
| MainLemma359–379 `exists_ne_modByMonic_eq` | Remainder hypotheses, output equality and finite encoding F: replace every diag with aeval-to-X, same polynomial values; pigeonhole/remainder reconstruction unchanged. |
| MainLemma402–411 `eval_hasseDeriv_sub_eq_zero` | Both congruence inputs and divisibility intermediate: generic subtraction, comp_aeval_apply and aeval_X. **Full actual proof replayed** with fresh replacement, not original diag. |
| MainLemma497–513 `abs_coeff_diag_hasseDeriv_modByMonic_le_aux` (private) | Conclusion and hcD bound: use rewritten coefficient/degree bounds, same remainder-bound arithmetic. |
| MainLemma515–548 `abs_coeff_diag_hasseDeriv_modByMonic_le_floor_aux` (private) | Conclusion, local bound, hreal: use rewritten previous auxiliary, same monic/nonmonic/degree-zero cases and floors. |
| MainLemma550–567 `exists_mem_RSet_le_index_aux` (private) | Hypothesis hC: invoke rewritten pigeonhole and vanishing statements; index conclusion unchanged. |
| MainLemma581–616 `exists_mem_RSet_le_index_of_rpow_bound_aux` (private) | Local hC remainder bound: rewritten floor estimate supplies unchanged numerical result and final index bound. |

No second arbitrary-variable aeval-to-X definition was found. HasseDeriv's unique-variable
transport concerns univariate Hasse calculus; it is not another implementation of arbitrary
variable collapse. Counts are useful API signals, not a veto over the actual one-call composition.

## Phase 6 — Native composition and verification

The exact construction from existing mathlib is one call:

```lean
MvPolynomial.aeval (fun _ : σ ↦ (Polynomial.X : Polynomial ℤ)) P
```

The original definition and this expression are definitionally equal. Its generic coefficient
version is also exactly aeval; no new lemma or instance is needed. This is **not** the separate
rename bridge or a closing `simp [several defs]` theorem being mislabeled as a ≤3-call proof.
Mathlib building block: `Mathlib/Algebra/MvPolynomial/Eval.lean:569`, `MvPolynomial.aeval`.
`Polynomial.X` supplies the existing target generator.

Additional verified supporting experiments, not counted as one-call composition:

- `eval₂Hom Polynomial.C` representation is `rfl`.
- Existing `comp_aeval_apply` (Eval612) plus `Polynomial.aeval_X` evaluates the diagonal polynomial
  in any commutative R-algebra; exact source/receipt above.
- Mathlib-only finite monomial expansion repeats the original proof over **CommSemiring R**.
- Rename all variables to PUnit, then `uniqueAlgEquiv R PUnit`: equality to aeval proved by
  `algHom_ext`, typed change and generator equations. This composite is a homomorphism, **not an
  equivalence** for arbitrary σ; variable collisions are real.
- A native Bool/ℤ counterexample proves noninjectivity by distinguishing X true and X false
  after their diagonal images agree. No degree equality or cancellation-free claim follows.
- Actual subtraction and full MainLemma vanishing proof are replayed using fresh generalized
  replacement; generic predicate-context transport also checks exact original substitution.

[Raw exact source](../evidence/Roth.diag/native-raw-executed.lean.txt),
[raw receipt](../evidence/Roth.diag/native-raw-success.json),
[consumer exact source](../evidence/Roth.diag/native-consumer-executed.lean.txt),
[consumer receipt](../evidence/Roth.diag/native-consumer-success.json).
The raw source imports only Mathlib and has `#check_failure Roth.diag`, preventing circular use
of imported project diagonal laws. Root executed heavy native tools serially; full success,
no partial/warming response, no warnings/errors, no sorryAx, no new axioms or raised limits.

Rejected preparations are preserved separately: one consumer attempt had unqualified-name
ambiguity from the persistent session's `open Polynomial`, fixed by full MvPolynomial qualifiers;
one raw attempt's simp unfolding left an AlgEquiv projection goal, fixed by typed change.
Two infrastructure preparations failed on unqualified eval ambiguity and then an unnecessary
simpa style warning, corrected with qualified evaluation and simp at the hypothesis.
Neither is counted as accepted verification.

## Phase 7 — Verdict and actionable recommendation

**NO-composable-from-mathlib.** Literature establishes a standard operation, while native evidence
establishes that existing `MvPolynomial.aeval` already implements both the integer version and
its semiring-parametric generalization. The one-call exact replacement outweighs the API-use
signal for upstream inclusion of an integer-only wrapper; it does not invalidate the local name.
The verdict is independent of implementation cost. A new bundled universal-property interface is
not missing: aeval already returns that AlgHom.

Alternative local destination: **retain `Roth.diag` in `Roth/CoeffNorm.lean`** while surveying;
its source-specific name documents the operation used in the main-lemma remainder estimates.
If later deleting the wrapper, inline the exact aeval expression at all eleven caller locations
using the table above, update the expansion/subtraction/evaluation laws to the existing generic
API, and validate every affected dependent and a full build before pushing. No such deletion is
performed by this assessment. The degree/coefficient bounds are separate declarations and their
upstream verdicts are not inherited from this construction's NO verdict.

## Phase 8 — Evidence completion and handoff

All required assessment phases and applicable definition-specific gates are complete. Five
accepted native sets cover target/generality/context, naturality/representation, actual consumer,
isolated mathlib composition/expansion, and infrastructure/counterexample. Exact executed snippets
and full native receipts, all four rejected preparations, fresh source/pin hashes, source/caller
archives, searches and this report are enumerated in
[verification](../evidence/Roth.diag/verification.json) and
[current manifest](../evidence/Roth.diag/copy-manifest.json).
[Portable read-only validator](../evidence/Roth.diag/validate.py) checks all of these and the
credential guard. Verification unresolved items: **none**. Root acceptance remains pending until
independent review; only then may overview/progress be advanced and the declaration committed.
