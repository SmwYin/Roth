# Assessment — `Roth.derivative_aeval`

**Verdict: YES-but-generalise-first.** The algebraic multivariable chain rule fills the gap between `MvPolynomial.pderiv` and the existing univariate `Derivation.map_aeval`. At minimum replace `Field K` by `CommSemiring R`; the original induction proof works at that floor. A module-valued derivation formulation also verifies and exposes the reusable mathematical content. This is a read-only assessment; production code is unchanged.

## Phases 0–2: baseline, content and size

The shared build completed successfully (2467 jobs). All 17 production source/pin hashes freshly match the baseline [input check](../evidence/Roth.derivative_aeval/inputs.json), [build](../evidence/Roth.derivative_aeval/baseline-build.txt). The corrected canonical entry is declaration 112 at `Roth/GenWronskian.lean:133`, rather than the initially supplied line136. The full declaring module was read, including the private consumer and its downstream generalized Wronskian argument [source](../evidence/Roth.derivative_aeval/declaring-module.lean.txt).

Full elaborated type (native original receipt supplies universes and instance names):

```lean
@Roth.derivative_aeval : ∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] (γ : σ → Polynomial K)
  (P : MvPolynomial σ K),
  Polynomial.derivative ((MvPolynomial.aeval γ) P) =
    ∑ j, Polynomial.derivative (γ j) * (MvPolynomial.aeval γ) ((MvPolynomial.pderiv j) P)
```

For a polynomial P and polynomial coordinate functions γj(t), differentiating the substitution P(γ(t)) gives the sum of the evaluated partial derivative with respect to each variable times γj′(t). K supplies the coefficients; σ indexes the finitely many variables; γ and P are arbitrary. There is no characteristic-zero assumption, no nonempty-variable assumption, and no l parameter in the actual theorem. Constants, sums, and multiplication by one variable give a complete polynomial induction proof.

Classification: **SMALL**, a standard supporting identity, not the module’s main Wronskian theorem or a new structure. The definition-only one-line test is **n/a: theorem**; its proof contains a genuine induction with three cases, not an existing-call wrapper.

## Phase 3: exhaustive literature

All exact requests, response SHA256/byte counts and sanitized returned locators are in [web receipts](../evidence/Roth.derivative_aeval/web-receipts.json). Full returned article/search bodies are not retained. A returned signed preview URL had its whole query removed. The local source excerpt is [clean.tex](../evidence/Roth.derivative_aeval/local-literature.txt).

| Channel | Actual request / locator | Outcome and relevance |
|---|---|---|
| General web: specific | `algebraic chain rule multivariate polynomial formal derivatives commutative ring` | Armstrong’s university notes describe the Jacobian chain rule for formal polynomial substitution over a ring. |
| General web: general | `derivation polynomial ring evaluation sum partial derivatives chain rule` | Elkies, *Derivatives and Derivations*, paragraphs4–5: module-valued derivations and polynomial partials. |
| General web: aliases | `polynomial ring universal derivation differential dx_i arbitrary characteristic chain rule` | Universal differential and derivation formulations; no analytic differentiability is required. |
| Optional mathematical second opinion | `ask_chatgpt_math` | n/a: this tool is unavailable. No reduced search width. |
| Local references | `.mathlib-quality/references/clean.tex:285–315` | The FACT in §2 explicitly identifies this substitution identity and recommends polynomial induction. Source uses rational coefficients for its wider argument, not because this identity needs division. |
| nLab | `site:ncatlab.org/nlab/show derivation polynomial ring differential`; open `chain+rule` | Indexed chain-rule page describes formal power series over a general commutative ring. Direct fetch fails with unsupported XHTML content type; indexed content is not treated as complete page access. |
| nCatLab | `site:ncatlab.org/ncatlab/show polynomial differential chain rule`; direct `.../ncatlab/show/derivation` | Direct URL inaccessible. Search mainly returns nLab entries; no separate categorical result is asserted. |
| Stacks | `site:stacks.math.columbia.edu polynomial algebra module differentials derivation free basis`; open tag00RM | §10.131 Definition10.131.1 and Lemma10.131.3 provide ring/module-valued derivations and universal differentials. The direct section view/find did not itself locate the polynomial-basis lemma; no invented tag is cited. |
| MathOverflow | `site:mathoverflow.net algebraic chain rule polynomial derivation characteristic`; retry `site:mathoverflow.net "chain rule" "derivation" polynomial` | Question23083 and Ekedahl’s answer give a dual-number substitution proof of the formal chain rule. Supplementary motivation only; primary algebra sources anchor generality. |
| Recent arXiv, last five years | `site:arxiv.org derivations polynomial ring chain rule differential after:2021-10-27`; open2311.04866 | Efimov–Petravchuk–Sydorov (2023), *Centralizers of Jacobian derivations*: modern use of partial/Jacobian derivations; its characteristic-zero field hypotheses serve a different centralizer theorem. It does not restrict this chain rule. |

Primary locators: [Elkies](https://people.math.harvard.edu/~elkies/M250.04/deriv.html), [Stacks §10.131](https://stacks.math.columbia.edu/tag/00RM), [Armstrong notes, p32 onward](https://www.math.miami.edu/~armstrong/785fa20/785fa20notes.pdf). Supplementary [MO23083](https://mathoverflow.net/questions/23083/derivative-in-the-ring-ke-e%C2%B2-chain-rule), [arXiv2311.04866](https://arxiv.org/abs/2311.04866).

Concept: formal algebraic chain rule / polynomial derivations. The standard ring form allows arbitrary coefficient rings, target algebras and target modules; a fixed polynomial uses finitely many variables even if the whole variable type is infinite. The semiring version is justified independently by Lean’s `CommSemiring` derivation API and the verified proof, rather than attributed to a source that only says ring. Analytic derivative theorems require topological hypotheses absent here and do not replace this algebraic law.

## Phases 4a–4b: parameters and verified generality

| Parameter | Current role | Weakening or constraint |
|---|---|---|
| K / `Field K` | Coefficients | **Verified `CommSemiring R`** with the original proof. Division, additive inverses, nonzero denominators and characteristic zero are unused. `CommRing` follows as an intermediate specialization. |
| σ | Arbitrary universe-polymorphic index type | No concrete `Fin n` representation is needed. |
| `Fintype σ` | Makes the displayed total sum finite | Keep for the exact total-sum spelling. Finite support (`P.vars`) permits an arbitrary variable type; the native support experiment verifies this with no `Fintype σ` binder. |
| γ | Arbitrary coordinates into `Polynomial K` | Replace target by any commutative R-algebra A and polynomial derivative by D : Derivation R A M; this is the reusable module-valued chain rule. |
| P | Arbitrary formal multivariable polynomial | No degree bound or restricted support assumption needed in the finite-variable form. |
| Ambient l, `CharZero K` | Not in actual signature | Already absent; do not list them as hypotheses newly removed. |

The current statement is **STRICTLY NARROWER THAN STANDARD**. The mechanically verified minimum restatement is:

```lean
theorem derivative_aeval {R σ : Type*} [CommSemiring R] [Fintype σ]
    (γ : σ → Polynomial R) (P : MvPolynomial σ R) :
    Polynomial.derivative (aeval γ P) =
      ∑ j, Polynomial.derivative (γ j) * aeval γ (pderiv j P)
```

The strongest verified module-valued restatement has this full signature (with no global finiteness or scalar-tower assumption):

```lean
theorem map_mv_aeval {R A M σ : Type*} [CommSemiring R] [CommSemiring A]
    [Algebra R A] [AddCommMonoid M] [Module R M] [Module A M]
    (D : Derivation R A M) (γ : σ → A) (P : MvPolynomial σ R) :
    D (aeval γ P) = ∑ j ∈ P.vars, aeval γ (pderiv j P) • D (γ j)
```

The mechanical minimum is one hypothesis/interface edit; the enclosing project’s Field context is incidental. No foundational project definition has to be rewritten to make that theorem general. The broader native experiment is a **new proof**, not a claim that existing mathlib already has the law:

```lean
D (aeval γ P) = ∑ j, aeval γ (pderiv j P) • D (γ j)
```

with commutative semirings R,A, an R-algebra structure on A, and a module-valued R-derivation D. A separate native test verifies these formulas without `IsScalarTower R A M`. For arbitrary σ the accepted formula is `D (aeval γ P) = ∑ j ∈ P.vars, aeval γ (pderiv j P) • D (γ j)`; the proof restricts P to the subtype P.vars, applies the finite law, and transports using `pderiv_rename`, `aeval_rename` and `Finset.sum_coe_sort`. The exact accepted sources and any further removed tower assumptions are authoritative in [verification](../evidence/Roth.derivative_aeval/verification.json).

## Phase 4c: modern idiom, all nine questions

| # | Question | Answer and downstream consequence |
|---|---|---|
| 1 | Typeclasses instead of preambles? | Already uses typeclasses; preserve `CommSemiring`, `Algebra`, `Module`, `Derivation`. No new ad hoc predicate. |
| 2 | Filters instead of metric/sequence data? | No: purely algebraic finite identity. |
| 3 | Universal-property class? | Derivation extensibility / `mkDerivationEquiv` and Kähler differentials explain the law. A new class is unnecessary; bundled derivations already supply linearity and Leibniz. |
| 4 | Bundled substructures? | No set-with-closure predicate to replace. A module-valued target is the relevant abstraction. |
| 5 | Field to semiring/module? | Yes: accepted semiring proof and arbitrary module-valued derivation experiment. Enables zero-divisor/positive-characteristic algebras and non-ring target modules. |
| 6 | Higher categorical widening? | No concrete need; Kähler functoriality is sufficient. |
| 7 | Concrete index widening? | σ is already arbitrary. The `P.vars` form removes global finiteness, not a special numeric index. |
| 8 | Concrete-via-abstract diagnostic? | Yes: proof body mentions `Polynomial.derivative` zero times; after simplification it uses only additivity, constant annihilation and the Leibniz law. Native arbitrary-D proof confirms this is more than identifier counting. Reuses `Polynomial.derivative'`, `Derivation.compAlgebraMap`, and module-valued derivation APIs. |
| 9 | False generalization? | No: D=`Polynomial.derivative'` and A=M=Polynomial R recover the original after `smul_eq_mul` and commuting multiplication. Preserve formal polynomials: equality as functions over finite rings would be a different object and is not proposed. |

Modern idiom available: **yes**. The finite-variable derivation law is the reusable primary theorem; the polynomial-derivative spelling is a useful specialization. The representation change has concrete mathematical benefit for Kähler differential modules and arbitrary algebra derivations; it does not justify pretending those general laws already exist as an evaluated-sum theorem.

## Phase 4.5: infrastructure risk

All six definition/class/instance rows (definitional equality, instance diamonds, instance priority, reducibility, coercions and API migration) are **n/a: theorem**. No instance is installed. A future proof using pulled-back scalar actions should keep them local; current direct induction avoids any persistent diamond.

## Phase 4.6: proof strategy, all five rows

| # | Diagnostic | Assessment |
|---|---|---|
| 1 | Epsilon-delta instead of filters | n/a: no topology. |
| 2 | Element argument instead of submodule/ideal inclusion | Polynomial induction is idiomatic here; no inclusion proposition is being proved. A derivation-ext proof additionally needs an evaluated pullback derivation/module normalization. |
| 3 | Sequences instead of nets | n/a: no limits. |
| 4 | Construction instead of universal property | Universal derivations and `MvPolynomial.derivation_ext` are genuine alternative strategies. Existing coordinates do not immediately produce the displayed evaluated sum. |
| 5 | Missing helpers that should exist | The multivariable evaluated partial-sum law itself is the missing helper, paralleling univariate `Derivation.map_aeval`. The concrete derivative corollary should use it once added. |

Strategy: **MATHLIB-IDIOMATIC** for the new primary law, with direct polynomial induction. Refactor the concrete corollary through the general law before shipping that package; avoid rebuilding a whole Kähler proof solely for this small semiring result.

## Phase 5: all five mathlib methods on all three forms

[Complete formal responses](../evidence/Roth.derivative_aeval/formal-search-raw.json) and [exact source commands/results](../evidence/Roth.derivative_aeval/source-search-raw.json) retain the actual requests. Finder uses its v4.28 default index, which may differ from this project’s pin; source and native signatures settle candidates. The local index reported **unavailable**, although source fallback yielded names. This is not evidence of absence.

| Method | Current derivative-aeval form | Literature chain-rule form | Abstract derivation form |
|---|---|---|---|
| Finder | `aeval_sumElim_pderiv_inl`, univariate `derivative_eval₂_C` | `pderiv_mul`, `derivative_eval₂_C` | `mkDerivation`, `comp_aeval_eq`, coefficient-derivation laws |
| Loogle | `Polynomial.derivative, MvPolynomial.aeval`: no result | `MvPolynomial.pderiv, MvPolynomial.aeval`: specialized constant evaluations / cotangent coordinates | `Derivation, MvPolynomial.aeval`: specialized evaluation / cotangent entries |
| LeanSearch | specialized pderiv evaluation, analytic polynomial derivative | univariate chain rule and polynomial derivation constructor | `mkDerivation`, `comp_aeval_eq` |
| rg | whole MvPolynomial tree + univariate derivative file | chain/pderiv/aeval tree search | Derivation and Kähler tree search |
| Local name search | `derivative_aeval`: project/scratch matches | `pderiv`: candidate source matches | `compAlgebraMap`: existing constructor; index unavailable |

Candidate adjudication, pinned source reads plus native signatures:

- `Derivation.map_aeval` (`RingTheory/Derivation/Basic.lean:151`) and `Derivation.comp_aeval_eq` (`Algebra/Polynomial/Derivation.lean`) take **univariate** P : Polynomial R and one a : A. They do not evaluate a multivariable P or supply a sum over σ.
- `MvPolynomial.aeval_sumElim_pderiv_inl` (`Algebra/MvPolynomial/PDeriv.lean:155`) evaluates only the disjoint τ variables into **constants** and differentiates one untouched σ variable. Arbitrary γj(t) creates additional chain-rule terms, so it is not the same statement.
- `MvPolynomial.mkDerivationEquiv`, `derivation_ext`, `derivation_eq_of_forall_mem_vars` classify derivations by generator values. Applying them here requires constructing the evaluation pullback module/derivation and identifying evaluated partial coefficients; those are actual proof obligations.
- `KaehlerDifferential.mvPolynomialBasis_repr_apply` (`RingTheory/Kaehler/Polynomial.lean:81`) identifies each coordinate of the universal derivative with pderiv. A basis reconstruction and pullback along aeval are still needed; it assumes rings while the direct proof works over semirings. No unverified ≤3-call replacement is claimed.
- Analytic `fderiv_aeval` adds norm/topological hypotheses and addresses a different derivative notion.

The isolated generic-route `exact?` probe imported PDeriv, Polynomial.Derivation, and Kaehler.Polynomial, guarded both the project target and new support helper as absent, and returned “could not close the goal.” It neither timed out nor exhausted a raised/default heartbeat limit. This unsuccessful search is recorded separately, not as a proof of absence.

The negative search conclusion is bounded: no existing evaluated multivariable chain-rule law was found after checking these generic routes. A failed or resource-limited `exact?` probe does not prove global absence.

## Phase 5.5: statement shape

**Normal form:** expand a derivative of an evaluation on the left into the evaluated partial-sum on the right, matching univariate `Derivation.map_aeval`. Equivalent forms are dot-product/Jacobian notation, an equality of bundled derivations, and the module-valued smul formula. The smul formula is the natural primary law; multiplication is its polynomial specialization. This is an equality, not an artificial pairwise iff between noncanonical definitions.

**Syntactic generality:** tried the identical polynomial statement over `CommSemiring`, a finite-variable module-valued derivation sum, and arbitrary-variable support sum. Use γ and P explicitly so the theorem rewrites directly. The finite total sum is convenient at the actual caller; finite support should complement it rather than force callers to prove a global variable enumeration.

**Superfluous arguments:** Field is too strong (drop to CommSemiring); Fintype is needed only for the exact univ-sum spelling; γ and P are essential; universes are already general; no l or CharZero is retained. The separate native drop-test removes `IsScalarTower R A M` from both generic derivation proofs; no such hypothesis is required. Overall **RESTATE-BEFORE-SHIP**.

## Phases 6.0–6: callers, inline audit and composition

External-to-file use count: **0**. Same-file explicit source use count: **1**.

| Caller | Exact use | Action |
|---|---|---|
| private `Roth.derivative_kronHasse_aux`, `Roth/GenWronskian.lean:159` | `simp [kronHasse, kronecker, derivative_aeval, pderiv_hasseDeriv, ...]` | Replace by the generalized chain rule with γj=`X ^ k ^ e j`, P=`hasseDeriv d P`. The native replay uses actual existing private constants through `mkPrivateNameCore`; it does not introduce duplicate public definitions. |

The source search found no separate inline re-derivation; apparent hits are the declaration and this caller. Canonical audit checks exact order of all293 names (including private names), uniqueness, presence and direct proof-constant use. It independently identifies the same private consumer. This is direct source/kernel use analysis, not a claim that downstream simp dependency closure has only one node. The caller feeds the Hasse-derivative span recurrence and generalized Wronskian existence proof, so this is live code.

Composition attempts:

1. Existing `Derivation.map_aeval`: fails to match the multivariable polynomial domain; no bijection between arbitrary σ-variable polynomials and one univariate polynomial preserves this statement without additional algebra setup.
2. Existing `MvPolynomial.derivation_ext`/`mkDerivationEquiv`: generator uniqueness is available, but creating the evaluation pullback and the partial-sum derivation is a **new proof**, not three existing theorem applications.
3. Kähler coordinate theorem + basis reconstruction: gives a conceptual ring-valued route with additional pullback/module normalization. It does not provide a verified three-call semiring proof.
4. Native polynomial induction and generalized caller replay: succeed with **new assessment helper theorem(s)**. This establishes generality and applicability; it is not evidence for NO-composable. The original proof’s closing simp occurs inside an induction, not a single closing simp composition of the original goal.

Conclusion: **NOT-COMPOSABLE** from the verified existing API in ≤3 calls. The single local use is a weak reuse signal, outweighed by the independent standard chain-rule API gap; no cost-based verdict is used.

## Native evidence and rejected attempts

The [portable verification record](../evidence/Roth.derivative_aeval/verification.json) preserves exact execution requests, original paths, source hashes, native regions and expected axiom declarations. All accepted proofs are free of sorry, axioms, unsafe evaluation and raised limits; the only dependencies are `propext`, `Classical.choice`, and `Quot.sound`.

| Check | Exact executed source | Raw receipt |
|---|---|---|
| Original statement/proof/axioms, fresh region5365 | [original](../evidence/Roth.derivative_aeval/derivative-aeval-original-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-original-receipt.json) |
| Ordered293 canonical/direct-caller audit, fresh region5369 | [audit](../evidence/Roth.derivative_aeval/derivative-aeval-audit-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-audit-receipt.json) |
| Semiring and finite-variable arbitrary derivation | [isolated proof](../evidence/Roth.derivative_aeval/derivative-aeval-raw-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-raw-receipt.json) |
| Arbitrary variables, sum over P.vars | [support proof](../evidence/Roth.derivative_aeval/derivative-aeval-finite-support-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-finite-support-receipt.json) |
| Remove scalar-tower hypothesis | [no-tower proof](../evidence/Roth.derivative_aeval/derivative-aeval-no-tower-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-no-tower-receipt.json) |
| Strongest support law specializes to the exact original formula | [specialization](../evidence/Roth.derivative_aeval/derivative-aeval-specialization-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-specialization-receipt.json) |
| Positive Kähler candidate signature/axioms | [signature](../evidence/Roth.derivative_aeval/derivative-aeval-kaehler-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-kaehler-receipt.json) |
| Actual private operator caller, fresh region5689 | [caller replay](../evidence/Roth.derivative_aeval/derivative-aeval-consumer-executed.lean.txt) | [receipt](../evidence/Roth.derivative_aeval/derivative-aeval-consumer-receipt.json) |

The accepted support-to-original specialization uses `Polynomial.derivative'`, `Polynomial.derivative'_apply`, `smul_eq_mul`, multiplication commutativity, `Finset.sum_subset`, and `pderiv_eq_zero_of_notMem_vars`. It therefore proves the stronger formulation really covers this exact original statement. The private caller replay goes through that specialization, not the old project chain-rule lemma.

The isolated failed [generic exact? source](../evidence/Roth.derivative_aeval/derivative-aeval-absence-executed.lean.txt) and [raw search receipt](../evidence/Roth.derivative_aeval/derivative-aeval-absence-receipt.json) are separate from accepted proof evidence.

Rejected attempts are retained separately in verification: an initial generic-D simp orientation reached the recursion limit; reversing `mul_smul` and removing `smul_comm` fixed it, then an unused `add_comm` simp entry was removed. Two support proofs failed subtype-sum normalization; the accepted proof uses explicit `Finset.sum_coe_sort`. An initial caller attempt needed the global MvPolynomial opening and an explicit definitional expansion of the real private operator. A header-import reload returned partial elaboration and is not accepted; the later complete disk response is clean. Original/audit receipts predate that header insertion and retain their own truthful historical regions. No rejected attempt was rescued with raised limits or an unproved assumption.

## Phases 7–8: verdict and action

**YES-but-generalise-first**, reasons **LITERATURE-WEAKENING** and **MODERN-IDIOM**. The minimum concrete change is Field→CommSemiring, which preserves the entire proof and meets the mechanical-weakening gate. The polynomial family γ and the polynomial P are arbitrary; the result is not specific to Kronecker substitutions. The missing API is precisely the **multivariable counterpart of `Derivation.map_aeval`**, expressed through `MvPolynomial.pderiv`. The generic Derivation target makes polynomial derivative a specialization and serves module-valued algebra differentials without stronger field or characteristic assumptions.

Proposed upstream home: `Mathlib/Algebra/MvPolynomial/PDeriv.lean` for the module-valued partial-sum law (and finite-support version), since pderiv depends on Derivation. Put the polynomial-target specialization in a new leaf `Mathlib/Algebra/MvPolynomial/ChainRule.lean` importing PDeriv and Polynomial.Derivation if importing the latter into foundational PDeriv is undesirable. This layering is explicit and does not assume a new dependency is free.

Proposed PR title: **`feat(Algebra/MvPolynomial): chain rule for algebraic evaluation`**. Ship as a focused chain-rule API PR. The accepted YES results `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.pderiv_hasseDeriv` and the generalized Wronskian proposal are related clients, but do not bundle unrelated higher-order machinery into this first-order change. Exact accepted YES names were checked against current progress, not inferred from names.

Pre-PR actions:

- [ ] `/generalise Roth.derivative_aeval`: use the accepted semiring/module/support signatures; retain only genuinely needed scalar compatibility assumptions.
- [ ] `/cleanup Roth/GenWronskian.lean Roth.derivative_aeval`: prepare the upstream theorem(s), documentation and import boundary; update the one private caller using the verified replay pattern.
- [ ] Request review from Yaël Dillies or Marcelo Lynch, whose recent commits touch the relevant MvPolynomial files; recent source history is retained in the exact source-search receipt.

Until upstreaming, the generalized helper belongs in `Roth/GenWronskian.lean` (or a project MvPolynomial chain-rule module if other clients arise). No production refactor, deletion, Git change or publication is part of this assessment. Verification has no unresolved proof obligation; future PR design is ordinary follow-up work.
