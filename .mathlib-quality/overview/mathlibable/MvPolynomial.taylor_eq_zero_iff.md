# MvPolynomial.taylor_eq_zero_iff — full mathlibable assessment

**YES-but-generalise-first**. Canonical declaration 72/293. Formal multivariate polynomial translation reflects zero. The ring proof is an existing generic injectivity corollary with a project-specific inverse-substitution premise; that premise cannot be counted as an existing mathlib fact. A new, fully verified maximal-support proof establishes the same statement over CommSemiring; all four measured simplifier consumers also pass with this stronger replacement. That stronger law is the proposed upstream target. This is a completed read-only assessment, with no production changes.

## Phase 0 — Doctor and source integrity

Accepted baseline: commit99f19fda4b3cbee38fc0d31af76075834f5cc265, full clean build2467jobs, Lean v4.34.0, mathlib5ed2965256430c3649e86755f9576b54eca72435. [Baseline](../evidence/MvPolynomial.taylor_eq_zero_iff/baseline-build.txt), [17 freshly matched source/pin hashes](../evidence/MvPolynomial.taylor_eq_zero_iff/inputs.json), [summary](../evidence/MvPolynomial.taylor_eq_zero_iff/input-hash-check.json). Target resolves at Roth/Taylor.lean192–193 and has @[simp], no sorry. [Canonical metadata](../evidence/MvPolynomial.taylor_eq_zero_iff/canonical-entry.json), [full declaring module](../evidence/MvPolynomial.taylor_eq_zero_iff/Taylor-module.lean.txt). The module constructs translation, proves its Hasse coefficient formula and bounded Taylor expansion. Fresh target, independent replay, raw composition and consumer probes were checked without treating partial responses as success.

## Phase 1 — Mathematical comprehension

A formal polynomial over any commutative ring is zero exactly when replacing every variable X_j by X_j+α_j gives the zero formal polynomial. One implication follows because substitution preserves zero. For the other, shift back by −α, or use the resulting injectivity of translation. Equality here is coefficientwise equality of formal polynomials, rather than vanishing of a polynomial function at coefficient-valued points.

Full native type:
```lean
∀ {σ : Type u_1} {A : Type u_2} [CommRing A] (α : σ → A)
  (P : MvPolynomial σ A), MvPolynomial.taylor α P = 0 ↔ P = 0
```
The variable set and coefficient type have independent universes. Neither finite variables, decidable equality, field, domain, characteristic zero, nontriviality nor a nonzero shift is assumed. The proof is `(taylor_injective α).eq_iff' (map_zero _)`, with the multivariate injectivity premise inherited mathematically from the inverse-shift law. The verdict is assessed independently of previous parent verdicts. [Original type, proof, fresh replay and axioms](../evidence/MvPolynomial.taylor_eq_zero_iff/native-target-success.json).

## Phase 2 — Preliminary checks

**SMALL:** elementary zero-reflection corollary, not a named main theorem or a new structure. Exhaustive literature breadth is unchanged. One-line definition check **n/a**: this is a theorem, so short body length is not a definition exemption or sufficient reason for automatic NO. Its simp attribute means a source grep alone cannot measure use.

## Phase 3 — Exhaustive literature protocol

All named channels were actually attempted. Exact requests, hashes and byte counts of original returned responses, safe primary locators and concise original summaries are archived; returned article/search bodies are deliberately omitted.

| Channel | Actual query or access | Finding and limitations |
|---|---|---|
| General web, current | `multivariate polynomial translation substitution nonzero polynomial zero iff` | Shift automorphism and nonzero-substitution contexts, not an exact independently named theorem at this generality. [Batch0](../evidence/MvPolynomial.taylor_eq_zero_iff/web-0.json). |
| General web, broad | `polynomial ring shift automorphism over commutative ring translation inverse` | Polynomial-ring automorphisms and lecturer shift example. Inverting translation implies zero reflection; implication is our inference, not a quotation of an arbitrary-variable theorem. [Batch0](../evidence/MvPolynomial.taylor_eq_zero_iff/web-0.json). |
| General web, aliases | `semiring polynomial Taylor translation leading coefficient zero reflection` | Semiring univariate Taylor API including leading coefficient; no primary general multivariate semiring theorem identified by search. Native generality checks control claims. [Batch0](../evidence/MvPolynomial.taylor_eq_zero_iff/web-0.json). |
| Optional ask_chatgpt_math | n/a | Unavailable tool, explicitly optional; other channels completed. |
| Local references | `Taylor`, `P_\\alpha` and coordinate shift forms in clean.tex | §4 Index lines500–548 uses real finite-coordinate Taylor translation and shifting back. It motivates the project need, not a mathematical restriction to ℝ/finitely many variables. [Search](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-local-literature.json), [excerpts](../evidence/MvPolynomial.taylor_eq_zero_iff/clean-excerpts.tex.txt), [source hash](../evidence/MvPolynomial.taylor_eq_zero_iff/local-literature.json). |
| nLab | `site:nlab.org polynomial algebra translation zero`; corrected actual platform `site:ncatlab.org/nlab polynomial free commutative algebra` | The polynomial page gives arbitrary-generator free commutative algebra and distinguishes formal polynomials from polynomial functions. Search accessible; direct fetch limitations documented separately. [Batch5](../evidence/MvPolynomial.taylor_eq_zero_iff/web-5.json), [direct accesses](../evidence/MvPolynomial.taylor_eq_zero_iff/web-3.json). |
| nCatLab/categorical | `site:ncatlab.org/nlab "automorphism" "isomorphism"` | Automorphism and isomorphism pages identify inverse morphisms as the abstract framework. Same nLab platform, separately checked categorical formulation, not an invented independent literature source. Direct automorphism fetch timed out; search content available. [Batch2](../evidence/MvPolynomial.taylor_eq_zero_iff/web-2.json), [batch4](../evidence/MvPolynomial.taylor_eq_zero_iff/web-4.json). |
| Stacks | `site:stacks.math.columbia.edu polynomial ring automorphism translation`; later universal-property query | General polynomial, divided-power and gluing contexts; direct00EP is an unrelated gluing lemma, not evidence for the exact zero-reflection statement. No precise exact hit asserted. [Batch1](../evidence/MvPolynomial.taylor_eq_zero_iff/web-1.json), [batch3](../evidence/MvPolynomial.taylor_eq_zero_iff/web-3.json), [batch4](../evidence/MvPolynomial.taylor_eq_zero_iff/web-4.json). |
| MathOverflow | `site:mathoverflow.net "polynomial" "translation" "automorphism"`; follow-up `"translation" "polynomial ring"` | Factoring by ring extension answer mentions shifting a polynomial to arrange an invertible constant coefficient; infinite-variable index translation is a different notion and excluded. Context only, not primary proof anchor. [Batch2](../evidence/MvPolynomial.taylor_eq_zero_iff/web-2.json), [batch4](../evidence/MvPolynomial.taylor_eq_zero_iff/web-4.json). |
| Recent arXiv, last5years | `site:arxiv.org "shift equivalence" "polynomials" "2022"`; direct2204.06968 | Chen–Du–Fang submitted14Apr2022, revised17Mar2025, within2021-10-27–2026-10-27. Original search title includes Shift Equivalence Testing; current abstract title is Symbolic Summation of Multivariate Rational Functions. Field-valued shift-equivalence computational context, not exact semiring proof. An initially mistyped2208.12288 is unrelated withdrawn microgrid research and expressly excluded. [Batch2](../evidence/MvPolynomial.taylor_eq_zero_iff/web-2.json), [corrected primary access](../evidence/MvPolynomial.taylor_eq_zero_iff/web-4.json), [date follow-up](../evidence/MvPolynomial.taylor_eq_zero_iff/web-5.json), [mistaken access](../evidence/MvPolynomial.taylor_eq_zero_iff/web-3.json). |

Primary mathematical anchor: [Klaus Sutner, Polynomials, Carnegie Mellon slides53–54](https://www.cs.cmu.edu/~cdm/resources/32-polynomials.pdf), the shift p(x)↦p(x+1) as an automorphism preserving coefficient ring, with proof. Our extension to several independent generators and arbitrary coefficient shifts uses the same universal-property inverse argument; no source is claimed to state our full Lean signature verbatim. [nLab polynomial](https://ncatlab.org/nlab/show/polynomial) supplies arbitrary-generator free commutative algebra, and [nLab automorphism](https://ncatlab.org/nlab/show/automorphism) gives the abstract inverse framework. [Recent primary abstract](https://arxiv.org/abs/2204.06968) establishes contemporary terminology and dates, not the generality proof.

Literature summary: translation/shift substitution preserves the zero polynomial and its nonzero complement; over rings it is an algebra automorphism. Standard ring presentations and generic inverse-map formulations agree, while semiring zero reflection need not entail injectivity. Formal polynomial equality must be distinguished from equality of induced functions over finite rings. No exact historical origin or universal semiring minimality is inferred from literature absence.

## Phase 4a–4b — Generality

| Parameter/hypothesis | Assessment |
|---|---|
| σ : Type u | Arbitrary set of variables already, including empty and infinite; no Fintype/DecidableEq to remove. |
| A : Type v | Independent universe; arbitrary commutative ring including positive characteristic, zero divisors and trivial ring. |
| CommRing A | Sufficient for current inverse/injective proof, with fixed parent CommSemiring interface. Univariate Polynomial.taylor_eq_zero is already Semiring; therefore ring necessity must be audited independently of taylor_injective. The WithTop ℕ injectivity counterexample from declaration71 does not refute zero reflection. The same conclusion over arbitrary CommSemiring is now actually verified by a new maximal-support/Hasse-coefficient proof; no inverse or injectivity assumption is used. |
| α : σ → A | Arbitrary coefficient shift, zero allowed. Essential value data. |
| P : MvPolynomial σ A | Arbitrary formal polynomial with inherent finite support. No explicit support/degree restriction. |
| Conclusion | Zero reflection, strictly weaker than equality reflection/injectivity over a semiring. Do not replace it with pointwise evaluation vanishing. |

**STRICTLY NARROWER: one verified class weakening CommRing→CommSemiring**, with the same parent taylor, parameters and conclusion. This is an actual theorem/proof replacement, **not an unchanged-body hypothesis deletion**. It needs no parent-definition, project-structure or foundational refactor. The successful native replacement proof is [exactly archived](../evidence/MvPolynomial.taylor_eq_zero_iff/native-semiring-executed.lean.txt) with [clean diagnostics and standard axioms](../evidence/MvPolynomial.taylor_eq_zero_iff/native-semiring-success.json), [generality record](../evidence/MvPolynomial.taylor_eq_zero_iff/generality.json). Phase4b explicitly permits proof adjustments/new ideas after a successful weakening; effort is not a verdict downgrade.

Proposed restatement:
```lean
theorem taylor_eq_zero_iff {σ R : Type*} [CommSemiring R]
    (α : σ → R) (P : MvPolynomial σ R) : taylor α P = 0 ↔ P = 0
```
The new proof chooses d maximal in nonempty support P. Any coefficient of the Hasse derivative at a nonzero exponent e would require e+d in support, contradicting maximality. Its constant coefficient is coeff d P, so hasseDeriv d P=C(coeff d P). The translated coefficient formula then gives a nonzero coefficient of the translated polynomial. This works over zero divisors, positive characteristic and noncancellative semirings; no additive inverse is used. Cost: MODERATE, a new28-line argument already compiled, rather than a one-token class edit. [Native source](../evidence/MvPolynomial.taylor_eq_zero_iff/native-semiring-executed.lean.txt).

## Phase 4c — Nine modern-idiom checks

| # | Question | Finding and downstream consequence |
|---|---|---|
| 1 | Typeclasses versus ad hoc hypotheses | Already CommRing; no hand-written algebraic predicate. |
| 2 | Sequences/metrics versus filters | No topology or convergence, n/a. |
| 3 | Construction versus universal property | Substitution uses free-algebra aeval; inverse identities reduce to generator equations. No coefficient induction needed for ring proof. |
| 4 | Bundled substructure | A newly proved translation AlgEquiv would make zero reflection a generic equivalence property and enable surjectivity/inverse transport. No existing multivariate translation equivalence was located; its inverse fields are new obligations. |
| 5 | Field versus weaker hierarchy | Already ring rather than field; semiring zero reflection differs materially from injectivity. The actual stronger CommSemiring theorem is verified, enabling zero reflection even where shift injectivity is false. |
| 6 | Higher-category version | Ordinary algebra homomorphisms/equivalences suffice. No higher coherence problem. |
| 7 | Concrete index | σ is arbitrary, no numerical index restriction. |
| 8 | Concrete-via-abstract diagnostic | Literal standalone taylor appears zero times in proof body; only taylor_injective α supplies its property. Abstract `(hf : Injective f) → f p = f 0 ↔ p=0` is already core Injective.eq_iff. For zero-preserving f this yields map_eq_zero_iff; actual generic conditional term verified. No new abstract theorem needed. |
| 9 | False-generalization guard | Zero reflection must not be conflated with semiring injectivity or equality of polynomial functions. An arbitrary aeval assignment need not reflect zero; inverse/injectivity premise or triangular structure is essential. |

[Proof-body diagnostic](../evidence/MvPolynomial.taylor_eq_zero_iff/proof-body-diagnostic.json). Modern idiom: existing generic zero-preserving injection/equivalence API, conditional on proving the mathematical substitution property. It enables support nonemptiness and weighted-order reasoning; it cannot conjure an inverse for every algebra homomorphism.

## Phase 4.5 — Six infrastructure risks

All **n/a: theorem**, rather than unsupported LOW claims. No new instances/data/coercions are introduced.

| Risk | Why n/a |
|---|---|
| Competing instances/diamonds | Theorem creates no instance. |
| Reducibility/defeq barrier | No new definition; unfolding the already present translation is separately tested. |
| Coercion paths | No new coercion; homomorphism coercions are existing. |
| Universe constraints | Polymorphic Prop only; source variables are independent universes. |
| Instance-search behavior | No new instance registration, simp theorem only. |
| Elaboration/import infrastructure | No production import or data change; exact native evidence records scratch-only checks. |

Overall infrastructure risk: n/a. Simp orientation/consumer behavior belongs to statement-shape and usage checks below.

## Phase 4.6 — All five proof-strategy checks

| # | Question | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | No topology. |
| 2 | Elements versus ideals/submodules | Current generic map equality corollary is already succinct. A kernel=⊥ formulation is equivalent under ring assumptions, but less convenient for actual simp consumers and not a new substitute for the inverse law. |
| 3 | Sequences versus nets | No analysis. |
| 4 | Explicit construction versus universal property | Inverse substitution is already naturally proved by aeval composition and generators; no category construction required in this one-line corollary. |
| 5 | Missing helper that should be in mathlib | Possible multivariate translation equivalence/core zero-reflection API. Generic Injective.eq_iff'/map_eq_zero_iff is already present. The new stronger argument uses a reusable maximal-supported-exponent Hasse-constant fact; package it as a helper if upstream review prefers, alongside the coefficient theorem. |

Ring strategy **MATHLIB-IDIOMATIC**, conditional on its inverse theorem. A semiring proof should use genuine triangular/leading-support structure rather than falsely import ring injectivity; no cost-based verdict downgrade.

## Phase 5 — Actual five-method search on three forms

[Raw formal-search responses](../evidence/MvPolynomial.taylor_eq_zero_iff/formal-search.json). Each of Finder, Loogle, LeanSearch and local name lookup was actually called for each of current, literature-standard and abstract forms; fifth method rg is archived separately. External index snapshots can differ from the pinned revision, so positive candidates are checked natively. Local symbol index status was unavailable despite source-backed hits, and empty local results do not prove absence.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Lean-Finder | Multivariate translation zero iff query: Polynomial.comp_X_add_C_eq_zero_iff, taylor_eq_zero, MvPolynomial.expand_eq_zero | Semiring shift nonzero query: univariate shift/expand and multivariate expand, which substitutes powers rather than constant shifts | Algebra-hom left-inverse zero reflection query: exterior/tensor algebra examples, no direct multivariate shift result |
| Loogle | `"taylor_eq_zero"`: Polynomial.taylor_eq_zero | `Polynomial.taylor, _ = 0 ↔ _ = 0`: same Semiring theorem | `Function.Injective ?f, ?f ?x = ?f ?y`: Injective.eq_iff and general injection facts |
| LeanSearch | Polynomial.comp_X_add_C_eq_zero_iff / ne_zero_iff and univariate AlgEquiv | Univariate shift and expand results; descriptions sometimes say semiring while returned formal types say CommRing: pinned native types control | ZeroHom.inverse and related zero-preserving hom API; generic map_eq_zero_iff also inspected directly |
| rg source | [Current](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-current.json), [untruncated full name](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-full-name.json) | [Literature](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-literature.json), [broader aeval/degree/support](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-independent.json) | [Abstract](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-abstract.json), [kernel/map equality](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-kernel.json) |
| Local names | `taylor_eq_zero`: Polynomial theorem and own target, distinguished | `leadingCoeff_taylor`: univariate theorem | `map_eq_zero_iff`: generic/specialized hits; unavailable index means no absence inference |

Pinned positives: `Polynomial.taylor_eq_zero` at Mathlib/Algebra/Polynomial/Taylor.lean104, `[Semiring R] (r:R)(f:Polynomial R)`, proof via leadingCoeff_taylor; `Polynomial.comp_X_add_C_eq_zero_iff` at AlgebraMap.lean518 is **Semiring** and univariate at the pinned revision; the external search index returned the older CommRing signature and is superseded by the native check; `Function.Injective.eq_iff'` lives in core Function; `map_eq_zero_iff` takes a zero-preserving map and an injectivity proof. Their exact pinned signatures and the univariate taylor application are archived in native raw evidence. [Polynomial module](../evidence/MvPolynomial.taylor_eq_zero_iff/Polynomial-Taylor-module.lean.txt), [core Function](../evidence/MvPolynomial.taylor_eq_zero_iff/Function-module.lean.txt). A univariate theorem does not definitionally become an arbitrary-variable theorem. MvPolynomial.expand changes exponents, not variables by constants, so is not a replacement.

Conclusion: verified partial matches and generic building blocks; no direct pinned arbitrary-variable shift zero-reflection theorem found. This bounded search result is not a theorem proving global absence.

## Phase 5.5 — Statement shape

1. **Normal form:** `taylor α P=0 ↔ P=0` simplifies a translated polynomial's zero-test to the original polynomial on the RHS. Alternatives are nonzero iff, a trivial kernel, injectivity over a ring, or a bundled equivalence's generic zero test. The existing simp orientation is appropriate and terminates by eliminating translation.
2. **Syntactic generality:** equality iff suits rewriting and simplifies negated zero tests automatically. Expanded `aeval (fun j↦X j+C(α j)) P` is definitionally the same translation; a theorem about arbitrary injective zero-preserving maps already exists but requires the shift premise. The nonzero form is the negation of this iff, not separate mathematics. Actual nonzero consumers are tested.
3. **Superfluous arguments:** α and P are used; σ/A are genuine type data; no Fintype, DecidableEq, field, domain, characteristic or nonzero assumption is present. CommRing is superfluous for the conclusion: actual replacement proof verifies CommSemiring. Restate this class before upstream shipping.

Overall normal form **OK**, and syntax **RESTATE-BEFORE-SHIP** solely to weaken CommRing to the verified CommSemiring class; keep the useful RHS simp normal form.

## Phase 6.0 — Callers and inline audit

[Explicit source search](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-callers.json) finds **zero named production references after excluding the declaration**, not dead code. Kernel-proof inspection using `value! (allowOpaque := true)` examines all public Taylor and Index declarations for both the target constant and generated names prefixed by it. Exact-name-only lookup misses simp-generated wrappers; the corrected prefix audit identifies four actual production consumers:

| Consumer | Source locator | Implicit use and refactor plan |
|---|---|---|
| Roth.exists_weight_eq_index | Roth/Index.lean76–81 (simp79–80) | `simpa using hP` proves translated support/image nonempty. If the concrete simp lemma is removed, supply the tested independent zero iff as a local simp rule, or an explicit inverse-based map_eq_zero proof. |
| Roth.le_index_iff | Roth/Index.lean85–90 (simp88) | `by simpa using hP` supplies nonempty support for le_csInf. Same replacement. |
| Roth.index_eq_weightedOrder_div | Roth/Index.lean143–158 (simp150) | `by simpa [F] using hP` supplies nonzero power series/finite weighted order. Same replacement, retaining coefficient embedding lemmas. |
| Roth.index_mul | Roth/Index.lean162–170 (simp169) | Local hfin's `by simp` converts translated/power-series nonvanishing for ENat.toNat_add. Same replacement; product identity statements unchanged. |

[Full caller module](../evidence/MvPolynomial.taylor_eq_zero_iff/Index-module.lean.txt), [corrected proof audit source](../evidence/MvPolynomial.taylor_eq_zero_iff/native-calleraudit-executed.lean.txt), [complete audit receipt](../evidence/MvPolynomial.taylor_eq_zero_iff/native-calleraudit-success.json), [caller summary](../evidence/MvPolynomial.taylor_eq_zero_iff/callers.json). This measured scan covers named public declarations in these modules; it is not an exhaustive transitive opaque-kernel closure of the entire repository. Transitive consumers such as index_prod are not mislabeled direct uses.

Inline derivation audit: [rg inline](../evidence/MvPolynomial.taylor_eq_zero_iff/rg-inline.json) finds univariate `Polynomial.taylor_eq_zero` at Index242 alongside coefficient-map injectivity. That handles the uniqueAlgEquiv univariate polynomial and is an actual counterpart, not an independent re-derivation of the same arbitrary-variable theorem. No source-level exact bypass was found. Four simp consumers demonstrate live API despite zero explicit tokens.

All four full caller proofs were replayed after disabling the original taylor_eq_zero_iff simp rule and registering only the **new semiring proof** as a local simp rule. The copied private support bridge is reconstructed explicitly, and dependent copied index proofs reference the fresh local le_index_iff/weighted-order result. The actual proof receipts are clean. [Exact consumer proofs](../evidence/MvPolynomial.taylor_eq_zero_iff/native-consumers-executed.lean.txt), [receipt](../evidence/MvPolynomial.taylor_eq_zero_iff/native-consumers-success.json). This validates those full proof fragments, not a production edit or whole rebuilt migrated module.

## Phase 6 — Composition experiments and verification

[Target source](../evidence/MvPolynomial.taylor_eq_zero_iff/native-target-executed.lean.txt), [target receipt](../evidence/MvPolynomial.taylor_eq_zero_iff/native-target-success.json), [raw source](../evidence/MvPolynomial.taylor_eq_zero_iff/native-raw-executed.lean.txt), [raw receipt](../evidence/MvPolynomial.taylor_eq_zero_iff/native-raw-success.json).

- Original one-line proof is reconstructed independently using prior fresh inverse/injectivity proofs, without this theorem. Used-constant audit confirms no circular target dependency.
- Generic map-zero iff from an injectivity premise compiles in the isolated mathlib-only experiment. It is a genuine existing short composition *conditional on that premise*, not unconditional multivariate zero reflection.
- Independently reconstructing the shift inverse uses aeval composition and generator normalization. The inverse witness is project mathematics/new scratch proof, not an existing mathlib building block. A closing simp inverse plus a generic injection term is Phase6b's borderline composition pattern, not automatically ≤3 existing calls for the whole target.
- Univariate `Polynomial.taylor_eq_zero` has the exact weaker Semiring signature and compiles directly. It is a comparison and generality signal, not an arbitrary-variable representation bridge.
- Expanded aeval is natively verified over CommSemiring, and the original arbitrary CommRing statement is recovered by specialization. [Shape/recovery source](../evidence/MvPolynomial.taylor_eq_zero_iff/native-extra-executed.lean.txt), [receipt](../evidence/MvPolynomial.taylor_eq_zero_iff/native-extra-success.json). Its used-constant audit confirms that the broader proof does not reference the original target, injectivity, negative shift or ring composition proof. Nonzero consumers retain mathematical meaning. The new semiring proof is a genuine finite-support/maximality argument with project coefficient and Hasse lemmas; it is not a ≤3 existing-mathlib-call normalization.

Accepted target, corrected caller audit, stronger semiring proof, four-consumer replay, expanded-form/recovery audit and isolated mathlib-only raw runs all report complete success, partial=false, no errors/warnings or failed dependencies, and only standard axioms propext/Classical.choice/Quot.sound where axioms are printed. Audit-only run has no new theorem axiom obligation. One initial semiring preparation attempt with two normalization goals/unused local is retained separately, not as an accepted proof: [rejected source](../evidence/MvPolynomial.taylor_eq_zero_iff/native-semiring-rejected-1.lean.txt), [receipt](../evidence/MvPolynomial.taylor_eq_zero_iff/native-semiring-rejected-1.json). Fixes unfold Finsupp.prod and use Ne.symm; no heartbeat/resource limits changed. No sorry/admit/new axiom/unsafe/native_decide appears in accepted experiment sources. Persistent-session prerequisite excerpts are archived and distinguished from isolated mathlib-only imports. [Verification inventory](../evidence/MvPolynomial.taylor_eq_zero_iff/verification.json).

## Phase 7 — Actionable verdict

**YES-but-generalise-first — LITERATURE-WEAKENING.** The existing ring statement is only a generic consequence of injectivity, but the correctly generalized statement is different mathematically: translation reflects zero over **every commutative semiring**, including semirings where the map is not injective. It requires the verified maximal-support/Hasse-coefficient argument, not the ring inverse witness. This supplies a specific missing multivariate semiring zero-reflection API analogous to the already Semiring univariate Polynomial.taylor_eq_zero, enabling support nonemptiness and finite weighted-order consumers without an unnecessary additive-group assumption. All four actual consumers pass with the stronger result. Thus a short original proof is not a reason to reject the stronger contribution.

The independent isolated composition experiment confirms that generic zero-map reflection requires an injectivity premise; no searched generic theorem supplies unconditional constant-shift zero reflection. Univariate translation is not a definitional arbitrary-variable replacement. A possible future ring AlgEquiv does not subsume the semiring statement. This is not NO-mathlib-has-it or a ≤3-existing-call composition, nor is it BORDERLINE merely because the successful weakening needed a new proof: the command expressly admits verified proof replacements/new ideas. No cost-based classification is used. No unchanged-body mechanical weakening is falsely claimed.

Proposed location: **Mathlib/Algebra/MvPolynomial/Taylor.lean**, with coefficient/Hasse infrastructure in the already proposed HasseDeriv module. Proposed PR title: **feat(Algebra/MvPolynomial): zero reflection of Taylor translation over commutative semirings**. Group with already accepted YES declarations **MvPolynomial.coeff_taylor** and **MvPolynomial.degreeOf_taylor_le**, using the accepted **MvPolynomial.hasseDeriv** and **MvPolynomial.coeff_hasseDeriv** foundation. Their actual current verdicts were checked in progress, not inferred from useful names: [group evidence](../evidence/MvPolynomial.taylor_eq_zero_iff/proposed-pr-group.json). The optional named taylor object had a prior BORDERLINE packaging verdict; if its name is declined, state this same semiring law directly against aeval(X+Cα), retaining substantive content. It needs no new generic injectivity or kernel theorem.

Before any upstream PR:

- Run `/generalise MvPolynomial.taylor_eq_zero_iff` on the CommSemiring replacement to confirm no further valid weakening; preserve the distinction from false semiring injectivity.
- Run `/cleanup Mathlib/Algebra/MvPolynomial/Taylor.lean MvPolynomial.taylor_eq_zero_iff`, including the full downstream/import checks and simplify/performance gates. This survey does not claim those future PR steps are already complete.
- Consider extracting the maximal-support Hasse-constant fact if useful to degree/leading-coefficient results, with the same exhaustive search bar before export.
- Select reviewers based on relevant recent source history: **Yaël Dillies** (MvPolynomial coefficient refactor631b214f7c) and **Aaron Liu** (Eval cleanup274ed6d67d) are evidence-based suggestions, not promises of availability. [Actual Git history](../evidence/MvPolynomial.taylor_eq_zero_iff/reviewer-history.json). No reviewer or PR has been contacted/created.

Retain production unchanged during this survey. Full declaration assessment and verification are complete, unresolved=[]; no further user input is needed. The complete stronger scratch proof and consumer migration evidence make the recommendation concrete and remotely reviewable after root acceptance.

## Phase 8 — Evidence and handoff

[Assessment](../evidence/MvPolynomial.taylor_eq_zero_iff/assessment.json), [overview entry](../evidence/MvPolynomial.taylor_eq_zero_iff/overview-entry.json), [verification index](../evidence/MvPolynomial.taylor_eq_zero_iff/verification.json), [current copy manifest](../evidence/MvPolynomial.taylor_eq_zero_iff/copy-manifest.json), [portable read-only validator](../evidence/MvPolynomial.taylor_eq_zero_iff/validate.py). Root independently reviews and accepts before updating overview/progress and performing one validated commit/push. No partial checkpoint is requested. All referenced evidence is intended for Git tracking remotely.
