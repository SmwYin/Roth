# Roth.kronecker_eq_zero_iff

**BORDERLINE-needs-human.** The reusable mathematics is support-local injectivity of monomial substitution. Mathlib already has that injectivity for `Finsupp.mapDomain`; the substitution-to-coefficient-map bridge is newly proved evidence, not an existing mathlib replacement. The design question is whether to upstream that bridge alone, a restricted `aeval` injectivity API, or also this zero-test corollary. All assessment phases and native checks are complete; these are upstream API questions, not verification blockers.

## Phase 0 — Baseline and identity

Canonical declaration **110**, public theorem at `Roth/GenWronskian.lean:106`, confirmed against the complete tracked ordering, including private names. Fresh hashes match all **17** source/pin entries of the shared successful **2467-job** build. No production, pin, Git or progress changes were made. The entire 272-line declaring module and its sole actual caller were read. The module proves existence of nonzero generalized Wronskians by Kronecker substitution and the univariate Wronskian criterion.

Evidence: [fresh hashes](../evidence/Roth.kronecker_eq_zero_iff/inputs.json), [baseline](../evidence/Roth.kronecker_eq_zero_iff/baseline-build.txt), [canonical entry](../evidence/Roth.kronecker_eq_zero_iff/canonical-entry.json), [module](../evidence/Roth.kronecker_eq_zero_iff/source-0.lean.txt), [native original](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-original-receipt.json).

## Phase 1 — Mathematical content and exact type

Enumerate finitely many variables by `e : σ ≃ Fin (card σ)`. If every individual degree of `P` is less than `k`, substituting `X_j = t^(k^(e j))` detects whether `P` is zero. Distinct exponent vectors in the degree box have distinct base-`k` encodings, so their coefficients cannot cancel after substitution. The reverse implication is preservation of zero by an algebra homomorphism.

The native full elaborated type is:

```lean
∀ {K : Type u_1} [inst : Field K] {σ : Type u_2} [inst_1 : Fintype σ] {k : ℕ},
  1 < k → ∀ {P : MvPolynomial σ K},
    (∀ (j : σ), MvPolynomial.degreeOf j P < k) →
      ((Roth.kronecker k) P = 0 ↔ P = 0)
```

`K` supplies coefficients; `σ` indexes variables; its `Fintype` chooses the enumeration; `k` is the radix; `hk : 1 < k` enables the current digit-injectivity lemma; `P` is arbitrary within the coordinate-degree box `hP`. There is no `l`, characteristic, ordering or nonzero-polynomial premise. The proof empties the support by recovering each coefficient with project theorem `coeff_kronecker`; every supported exponent satisfies `hP` by `monomial_le_degreeOf`. This is a real use of a project coefficient theorem, not an existing-mathlib composition.

Evidence: [full native type](../evidence/Roth.kronecker_eq_zero_iff/full-type.txt), [original exact commands](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-original-executed.lean.txt).

## Phase 2 — Preliminary checks

**SMALL:** a zero-detection helper for the named substitution, not a new structure or the module's main Wronskian result. The name contains Kronecker because it describes the substitution; this helper does not assert a standalone named Kronecker theorem. One-line definition test: **n/a — theorem**. The substantive source proof has four tactic lines; no definition exemption is applicable. Smallness does not reduce the literature or search work.

## Phase 3 — Exhaustive literature

Every named channel was attempted. Search responses are represented by exact requests, SHA256, byte count, access status, locators, and original concise summaries; complete web bodies were not persisted.

| Channel | Exact query or access | Finding |
|---|---|---|
| General web, specific | `Kronecker substitution injective bounded individual degrees nonzero polynomial` | Ferrand's primary article gives exactly bounded partial-degree injectivity over a commutative ring. |
| General web, general | `Kronecker substitution monomial weights injective support commutative ring` | Confirms monomial exponent encoding; mixed-radix formulations also appear. |
| General web, aliases/application | `Kronecker map polynomial identity testing base degree encoding` | Identity testing and reversible multivariate-to-univariate reduction are applications. |
| Optional ChatGPT mathematics | n/a: `ask_chatgpt_math` unavailable | No external mathematical opinion claimed. |
| Local source | `clean.tex`, Wronskians proof lines225–275 | Rational coefficients, digit uniqueness, coefficient comparison, and explicit restricted injectivity implementation note. |
| nLab | `site:ncatlab.org/nlab Kronecker substitution polynomial`; direct monoid-algebra page | No precise target theorem established; direct URL inaccessible via web tool. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial monoid algebra injective substitution`; direct HomePage | No target law established; direct URL inaccessible. |
| Stacks Project | `site:stacks.math.columbia.edu polynomial monoid algebra injective`; tag00AQ | General commutative-ring convention accessible; Kronecker-delta matches are unrelated. No claimed substitution theorem. |
| MathOverflow | `site:mathoverflow.net Kronecker substitution injectivity polynomial` | Mostly point-injectivity/cyclotomic matches, which do not prove bounded polynomial-substitution injectivity. |
| Recent arXiv | `site:arxiv.org Kronecker substitution polynomial identity testing after:2021-10-27 before:2026-10-28` | arXiv:2403.12716 (19March2024), reversible and iterative Kronecker reductions; direct abstract checked. |

[Ferrand, *Monogenous Algebras. Back to Kronecker*](https://perso.imj-prg.fr/daniel-ferrand/wp-content/uploads/ferrand-pub/simple.9.pdf), August2019, proof of Proposition2.5.1, PDF p7, lines386–406, proves injectivity on the partial-degree box over any commutative unital ring. Its coefficient encoding argument requires no field division. This is a distinct application to polynomial laws and norms, establishing interest outside Roth's theorem. [Wang–Su–Wang–Zhang, arXiv:2403.12716](https://arxiv.org/abs/2403.12716), abstract lines16–20, studies reversible reductions with alternative exponents; it supports the usefulness of allowing weights beyond uniform powers. The latter source is not being cited as proving the precise support-local semiring theorem.

**Literature summary:** standard names are Kronecker substitution, base/radix encoding, and reversible reduction. A standard finite-variable form is injection on a coordinate-degree box over a commutative ring. Mixed-radix versions vary the coordinate bounds. The modern support-local semiring formulation below is verified algebraic abstraction of this argument, not attributed verbatim to the literature. The current Field restriction is stronger than Ferrand's statement.

Evidence: [general queries](../evidence/Roth.kronecker_eq_zero_iff/literature-0.json), [nLab/nCatLab/Stacks queries](../evidence/Roth.kronecker_eq_zero_iff/literature-3.json), [MathOverflow and recent arXiv](../evidence/Roth.kronecker_eq_zero_iff/literature-6.json), [direct accesses](../evidence/Roth.kronecker_eq_zero_iff/literature-direct.json), [exact primary locator](../evidence/Roth.kronecker_eq_zero_iff/literature-find.json), [local searches](../evidence/Roth.kronecker_eq_zero_iff/rg-local-literature.json).

## Phase 4a–4b — Parameters and verified generality

| Parameter/hypothesis | Essential mathematical content | Verified change and interface distinction |
|---|---|---|
| `K : Type*` | Arbitrary coefficients | Already universe polymorphic; expanded law keeps arbitrary coefficient type. |
| `[Field K]` | Addition and multiplication suffice | **CommSemiring R** compiled. The literal `Roth.kronecker` parent is Field-indexed; weakening only this theorem's binder is ill-typed. Expanded `aeval` representation is required. |
| `σ : Type*` | Variable index | Expanded support-local law works for arbitrary `σ`, including infinite types. |
| `[Fintype σ]` | Chosen positional weights | Remove from abstract weights law; positional law instead takes explicit `e : σ ≃ Fin n`, avoiding hidden enumeration choice. This is a changed representation, not dropping finite data while retaining `equivFin`. |
| `k : ℕ` | Positional radix | Any natural radix compiled in positional zero law. Arbitrary `w : σ → ℕ` compiled in abstract law. |
| `hk : 1 < k` | Needed by current proof's chosen helper | **Dropped** in compiled positional law and old-parent `zero_replay`. For `k≤1`, bounded vectors all vanish; at `k=0` and nonempty `σ`, `hP` is impossible. Empty `σ` is permitted and gives constants. No hidden positivity needed for this zero law. |
| `P` | Polynomial tested | Unrestricted apart from exponent separation/support hypothesis. |
| `hP : ∀ j, degreeOf j P < k` | Prevents collisions | Replace by `Set.InjOn (Finsupp.weight w) P.coeff.support`; this only separates actual supported exponents. The degree bound supplies this premise using the new108 positional separation helper. |

**STRICTLY NARROWER THAN STANDARD / verified expanded generality.** Three clear axes are coefficient semiring, explicit enumeration/no radix lower bound, and arbitrary support-local weights. The accepted exact native proofs establish these, with only standard axioms. Field/Fintype weakening cannot be described as a single edit to this existing theorem: its fixed parent and project helper interfaces must be restated. Dropping `hk` alone is true in the fixed interface, but obtaining it currently requires the strengthened separation API. These interface facts matter to verdict routing; no cost-based downgrade is made.

The verified abstract restatement is:

```lean
theorem abstract_zero {R σ : Type*} [CommSemiring R] (w : σ → ℕ)
    (P : MvPolynomial σ R)
    (hi : Set.InjOn (Finsupp.weight (R := ℕ) w)
      (↑P.coeff.support : Set (σ →₀ ℕ))) :
    aeval (fun j ↦ (Polynomial.X : Polynomial R) ^ w j) P = 0 ↔ P = 0
```

The compiled positional form takes `e : σ ≃ Fin n`, `{k : ℕ}`, `[CommSemiring R]`, and `hP`, with no `[Fintype σ]` binder and no `hk`. The explicit equivalence still implies finiteness; it is not a claim that infinitely many variables admit the same positional finite encoding.

Evidence: [abstract and positional exact source](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-abstract-executed.lean.txt), [disk diagnostics](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-abstract-receipt.json), [independent mathlib-only full source](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-isolated-executed.lean.txt), [isolated receipt](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-isolated-receipt.json).

## Phase 4c — Modern idiom, all nine checks

| # | Check | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclass preambles | Already typeclasses. Use existing `CommSemiring`, no new custom class; polynomial evaluation API then applies over `ℕ`, rings with zero divisors, and trivial semirings. |
| 2 | Filters/topology | No: finite algebraic coefficient identity; no topology present. |
| 3 | Universal property | Yes for the bridge: `MvPolynomial.algHom_ext` identifies the `aeval` homomorphism with `AddMonoidAlgebra.mapDomainAlgHom` after `Polynomial.toFinsuppIsoAlg`. Its bridge proof was newly developed in109; it is not an existing analogous injectivity law. |
| 4 | Bundled substructures | A bounded-degree submodule is possible, but not a subalgebra (products escape the box). For arbitrary support-set `S`, restricted `Set.InjOn` avoids introducing a redundant bundle and composes directly with `Finsupp.mapDomain_injOn`. |
| 5 | Field versus semiring | Yes: verified `[CommSemiring R]`; no subtraction, division, domain or nontriviality premise. Enables zero testing over semiring coefficients with unchanged proof. |
| 6 | Higher categories | No: no categorical data or law whose categorification would improve this API. |
| 7 | Concrete index | Natural exponents are part of ordinary polynomial semantics. Arbitrary `σ` and arbitrary weights are verified; replacing `ℕ` exponents by an arbitrary monoid would change the polynomial target to a monoid algebra and must be identified as an expanded representation. Its core injection theorem already exists. |
| 8 | Concrete-via-abstract diagnostic | **Fires.** In the four source proof lines, `kronecker` occurs zero times, `kroneckerExp` zero times; all specific arithmetic is hidden in `coeff_kronecker` (one occurrence). The proof needs coefficient recovery only. The stronger support-local mapDomain route bypasses project coefficient recovery entirely once the bridge is supplied. |
| 9 | False-generalisation guard | No false widening in accepted statements: explicit `hi` prevents collisions and positional degree bounds imply it. Reject global injectivity of one fixed substitution without a degree/support restriction: e.g. two variables with weights1 and`k` identify `X₁^k` and `X₂`. No domain assumption can prevent that collision. |

**Modern idiom available, real improvement:** use the weight homomorphism and support restriction, so `Finsupp.mapDomain_injOn` and `mapDomain_support_of_injOn` apply without reproving coefficient uniqueness. Arbitrary collision-free sparse supports and mixed weights are usable without a full rectangular degree bound. A restricted `aeval` injection theorem is an API option; finite-degree zero detection is its specialization. This is not a new categorical structure or new injectivity mathematics.

## Phase 4.5 — Infrastructure risks

**n/a: theorem.** No typeclass diamond, reducibility declaration, noncanonical data unfolding, instance priority, universe data construction or new coercion is introduced. The six definition/instance risk rows do not apply to a proof of a proposition. Restating parent definitions would require their separate infrastructure assessment and is not an action taken here.

## Phase 4.6 — Proof strategy, all five checks

| # | Check | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Element algebra versus substructure | Current coefficient/support proof is appropriate locally, but a restricted-injection law on coefficient supports is cleaner reusable API; `mapDomain_injOn` already expresses this abstractly. |
| 3 | Sequences versus limits | No analysis or infinite sums. |
| 4 | Construction versus universal property | The representation bridge can use algebra-hom extensionality; current zero proof itself constructs no object. |
| 5 | Missing helper API | Yes: a native `aeval`-to-weighted-mapDomain bridge; then choose whether an `aeval` support-injectivity/zero lemma merits public packaging. Those are actual newly proved helpers, not invented existing names. |

**REFACTOR-RECOMMENDED:** bridge once, invoke existing support-local injection, and derive zero detection. The accepted abstract proof gives this route. A second exact route uses image-of-support preservation. The question is API placement and packaging, not proof feasibility or development cost.

## Phase 5 — Five actual mathlib search methods

All methods ran on **current**, **literature-standard**, and **abstract** forms. Exact requests and complete formal responses are in [formal search](../evidence/Roth.kronecker_eq_zero_iff/formal-search.json); pinned source receipts are [current](../evidence/Roth.kronecker_eq_zero_iff/rg-current.json), [standard](../evidence/Roth.kronecker_eq_zero_iff/rg-standard.json), and [abstract](../evidence/Roth.kronecker_eq_zero_iff/rg-abstract.json).

| Method | Current form | Standard `aeval` form | Abstract support form |
|---|---|---|---|
| Finder | DegreeLT equivalence, finite-field evaluation kernel and coefficient-map candidates; different maps | Expansion and variable-injection candidates; different maps | Exact `Finsupp.mapDomain_injOn`, also apply' and global injection |
| Loogle | `aeval_algebraMap_eq_zero_iff` variants preserve an already evaluated value through scalar extension, not the original polynomial | `MvPolynomial.aeval, Set.InjOn`: empty | Exact injOn and support-image laws |
| LeanSearch | Monad substitution, power-series and rename candidates; no exact target | `MvPolynomial.map_injective` changes coefficients; `expand_injective` keeps independent variables | Exact mapDomain_injOn and mapDomain_apply' |
| `rg` pinned source | Full target/current-law pattern searched without truncation: only unrelated Kronecker results | `aeval_eq_zero`, IsEmpty evaluation injection, expand injection | Basic.lean:375 apply',389 support image,434 global injection,482 support restriction |
| Local name search | Project/scratch Kronecker entries and matrix products are not upstream hits | IsEmpty-only evaluation injection | Confirms Finsupp names; index reports unavailable |

Local results are a fallback name scan with unavailable index and include scratch/evidence noise. Those are not evidence of upstream presence or absence; pinned source and native signatures establish positive candidates. External indexes can differ from the pin. `MvPolynomial.aeval_eq_zero` is only the forward consequence when all coefficients vanish, not injectivity. `MvPolynomial.expand_injective` changes every variable to its own power and never collapses the variable index; coefficient-map and scalar-tower laws likewise do not model this substitution. The global `mapDomain_injective` premise cannot be supplied for a fixed radix on all exponent vectors.

**Conclusion:** found the exact abstract injection law as `Finsupp.mapDomain_injOn`, but only a partial representation match for the current/literature `aeval` statement. The exact bridge is non-definitional. Native mathlib-only `exact?` on the support-local `aeval` zero law fails to close, without timeout. That is a recorded failed generic route, not a universal proof of absence. No lemma is declared absent merely because a search failed.

Evidence: [absence source](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-absence-executed.lean.txt), [honest failed exact? receipt](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-absence-receipt.json), [positive pinned signatures and successful application](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-isolated-receipt.json).

## Phase 5.5 — Statement shape

**Normal forms checked:** (i) substitution zero iff source zero, (ii) support-local restricted injectivity of `aeval`, (iii) restricted `Finsupp.mapDomain` injection under the coefficient representation. Mathlib has (iii). The accepted bridge identifies (ii) with (iii) non-definitionally. A standalone zero test correctly puts `P = 0` on the RHS and can rewrite an evaluation-zero hypothesis; there is no reason to reverse it.

**Syntactic generality attempted:** the one-polynomial support-local zero law and the explicit-enumeration no-`hk` degree law both compile; the restricted-injection form also makes the abstraction explicit. The old caller supplies a bound for a linear combination, making a degree-bound zero corollary convenient. The generic support-law form accepts sparse support data directly. Neither convenience alone settles which should be public.

**Superfluous argument audit:** `K,σ,P` essential parameters; Field stronger than necessary only after expanding the parent; Fintype needed by literal `equivFin` parent but replaced by weights or explicit equivalence; `k` essential only to positional specialization; `hk` mathematically removable and removed in accepted old-parent replay; `hP` essential in positional form but replaceable by support injectivity. No characteristic or family-size assumption is accidentally retained. **RESTATE-BEFORE-SHIP:** use semiring coefficients, explicit weights/support separation, and optional positional corollary without `hk`.

## Phase 6.0 — Actual callers and inline audit

| Caller | Source reference | Use and replay |
|---|---|---|
| `Roth.linearIndependent_kronecker` | `Roth/GenWronskian.lean:123` | Converts vanishing of a substituted linear combination back to zero. Full proof replay compiled using `zero_replay`, which uses the new positional helper rather than the assessed theorem. |

Named reference count **1**, in the declaring file; internal use count excluding that file **0**, external-to-file callers **0**. The canonical kernel dependency audit freshly checks **293 requested,293 unique,293 present,293 values**, exact tracked order/private-name spellings, and identifies the same sole direct consumer. This is direct dependency evidence, not an opaque transitive or simp closure. The target is not marked simp. Inline derivation scan found no duplicate zero-test proof elsewhere; source matches are this theorem and its coefficient predecessor, not independent consumers. Its single-use status is an API signal but does not prove composability or dead code.

The replay retains `hk` in `linearIndependent_replay` because the original sum-degree proof uses positivity in `Finset.sup_lt_iff`. It removes `hk` from the zero criterion itself. This distinction prevents falsely claiming the caller's own lower bound has disappeared.

Evidence: [caller inventory](../evidence/Roth.kronecker_eq_zero_iff/callers.json), [source grep](../evidence/Roth.kronecker_eq_zero_iff/rg-callers.json), [inline grep](../evidence/Roth.kronecker_eq_zero_iff/rg-inline.json), [fresh canonical audit](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-audit-receipt.json), [full caller replay](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-consumer-executed.lean.txt), [clean caller diagnostics](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-consumer-receipt.json).

## Phase 6 — Actual composition experiments

1. **Existing abstract law:** `Finsupp.mapDomain_injOn S hi` directly supplies injection on coefficient functions supported in `S`, with `[AddCommMonoid M]`. For `S = P.coeff.support`, compare `P.coeff` and zero. This is an existing mathlib result, verified at the pin.
2. **Normalize actual substitution:** newly proved `CoeffKroneckerProbe.bridge` states `(aeval (fun j ↦ X ^ w j) P).toFinsupp.coeff = P.coeff.mapDomain (Finsupp.weight w)`. Its monomial/add induction is included verbatim in the independent isolated execution. This is the missing normalization, not `rfl`, not inherited NO evidence, and not supplied by a generic `LinearMap.ext` assertion.
3. **Zero law after normalization:** `abstract_zero` rewrites through that bridge, applies `mapDomain_injOn` to `P.coeff`/zero, and uses `AddMonoidAlgebra.coeff_injective`. This is successful, but contains a new helper and rewriting; it is not a ≤3 existing-call proof of the original statement.
4. **Positional law and actual consumer:** the newly proved108 no-base separation lemma plus degree-support containment gives `positional`; `zero_replay` specializes via `Fintype.equivFin`; the complete actual linear-independence proof then compiles. The no-base theorem is a new upstream candidate, not an existing mathlib call.
5. **Alternate normalizations:** the restricted-injection proof reuses `mapDomain_injOn` for both supports, while `support_zero` uses existing `mapDomain_support_of_injOn` plus `Finset.image_eq_empty` and coefficient injection. Both require the same new bridge; [exact restricted/support proofs](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-restriction-executed.lean.txt) and [clean receipt](../evidence/Roth.kronecker_eq_zero_iff/kronecker-zero-iff-restriction-receipt.json) are supplied. These routes test that coefficient recovery is not the only way to express the result.

**NOT-COMPOSABLE from existing mathlib alone in the tested forms.** The core law already exists in the coefficient representation, while a public `aeval` bridge/law remains a distinct API decision. No successful `simp [defs...]` proof is promoted to an automatic NO; the closing `simpa only [Roth.kronecker]` in the old-parent replay uses a newly proved positional theorem. If the bridge becomes upstream API, this zero-test may then be a convenient thin corollary or an inlined consequence. Current downstream project helpers cannot be counted as existing mathlib building blocks.

## Phase 7 — Verdict and action

**BORDERLINE-needs-human.** Generality and correctness are verified. The narrow spelling should not be shipped as-is. The core support-local injectivity already lives in `Finsupp.mapDomain_injOn`, but the `aeval`-to-mapDomain bridge and positional separation law used to recover the current statement are newly proved. Consequently neither a ≤1 existing-call specialization nor a ≤3 existing-call composition has been established for the current `aeval` form. Conversely, immediately choosing YES for the zero corollary would decide how much convenience API to package around a bridge without resolving that design choice.

**Automatic NO parent gate checked independently:** parent `Roth.kronecker` was NO because `MvPolynomial.aeval` already exists. Re-aimed searches and native generic probing did not establish an analogous bounded-support zero/injection law about `aeval`. `Finsupp.mapDomain_injOn` is an exact analogue in a further representation, reached through the new bridge; this is not an already-present law about the parent's replacement. Therefore no blanket inheritance is applied. Had such an `aeval` law been found and verified, normalization of the old spelling would not justify downgrading its NO verdict.

Concrete upstream API questions:

1. Should the contribution stop at the weighted `aeval`/`mapDomainAlgHom` bridge, with zero detection derived directly from existing `Finsupp.mapDomain_injOn`?
2. If a public consequence is wanted, should restricted `Set.InjOn` on arbitrary coefficient-support sets be primary, with a single-support zero iff lemma as a named rewriting corollary?
3. Should the positional degree-box zero test be included alongside the accepted108 explicit-enumeration separation API, or remain project-local in `Roth/GenWronskian.lean`?

These questions do not request user input or interrupt the overview. A provisional upstream home is a monomial-evaluation bridge file such as `Mathlib/Algebra/MvPolynomial/MonomialEval.lean`, or `Mathlib/Algebra/MvPolynomial/Eval.lean` if its import layer supports `Polynomial.toFinsuppIsoAlg`. Check that layering before choosing a home; the positional separation law belongs with the accepted108 Digits/Finsupp API, not in a new Kronecker-only hierarchy. Until that choice is made, retain the local zero-test or replace its sole call with the verified generalized local route. A complete future refactor at `linearIndependent_kronecker:123` substitutes `zero_replay`/the chosen support-law specialization and preserves the degree-of-sum obligations; the exact replay is supplied. Do not add another abstract Finsupp injectivity theorem, since the existing theorem already serves that role. No upstream PR or production refactor was performed.

## Phase 8 — Completion and verification

All phases PASS, with theorem-specific infrastructure n/a, and `unresolved: []`. Accepted original, canonical audit, abstract/positional, independent mathlib-only, sole-consumer, and restricted-injection/support-image-zero native runs are clean, complete and free of warnings, errors, `sorryAx`, new axioms or raised limits. Accepted proof axioms are a subset of `propext`, `Classical.choice`, `Quot.sound`. Historical disk diagnostics are retained in full but fresh target information is scoped to each recorded new-region start line. Earlier rejected binder/elaboration/style attempts and failed exact? searches are segregated from accepted proofs. The current copy manifest, portable read-only validator, source/pin hashes, all evidence links, formal-search receipts and credential scan are part of the handoff. Root records independent acceptance during integration; the worker metadata initially records it as pending.

Evidence: [verification index](../evidence/Roth.kronecker_eq_zero_iff/verification.json), [assessment](../evidence/Roth.kronecker_eq_zero_iff/assessment.json), [portable validator](../evidence/Roth.kronecker_eq_zero_iff/validate.py), [current manifest](../evidence/Roth.kronecker_eq_zero_iff/copy-manifest.json).
