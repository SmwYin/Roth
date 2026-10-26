# MvPolynomial.hasseDeriv_C — full independent mathlibable assessment

**Verdict: BORDERLINE-needs-human.** The result is a standard positive-order Hasse derivative constant law with one actual Taylor-expansion caller. The univariate law in mathlib is an analogue, not a replacement for arbitrary variables. The independent construction proof reduces the constant to a single coefficient and closes by simplification after proving its binomial factor vanishes. Under Phase 6b this is explicitly a trivial-simp-composition design question, not an automatic NO. No verified term of at most three existing mathlib calls establishes the concrete multivariate normalization. Project parent lemmas do not count as existing mathlib calls. This assessment is complete; future upstream API choices require no input to finish this read-only work.

## Phase 0 — doctor

The actual theorem starts at **Roth/HasseDeriv.lean:126**; line 127 is its first proof line. All 17 source/pin hashes were freshly checked against the shared baseline manifest. The reusable baseline is `lake build`, exit 0, 2467 jobs, no reported errors or warnings. Declaration kind: theorem; no sorry. The entire 294-line declaring module and entire 224-line caller module were read. The module develops multivariate Hasse operators as linear maps over commutative semirings, with binomial, coefficient, composition, degree and univariate comparison interfaces.

Evidence: [baseline](../evidence/MvPolynomial.hasseDeriv_C/baseline-build.txt), [fresh hashes](../evidence/MvPolynomial.hasseDeriv_C/source-check.json), [target source](../evidence/MvPolynomial.hasseDeriv_C/target-excerpt.lean), [canonical target row](../evidence/MvPolynomial.hasseDeriv_C/corrected-target.json). Exact native checks and raw receipts are indexed by [verification](../evidence/MvPolynomial.hasseDeriv_C/verification.json).

## Phase 1 — comprehension

For a polynomial algebra in an arbitrary set of variables over a commutative semiring, every Hasse derivative with nonzero finitely supported natural multi-index kills a constant polynomial. At least one differentiation order is positive, so the corresponding binomial coefficient of the zero-exponent monomial is zero. Linearity multiplies that zero factor by the constant coefficient.

The variable type `σ` is arbitrary and universe-polymorphic; the coefficient type `R` has `CommSemiring R`; `d : σ →₀ ℕ` is implicit; `hd : d ≠ 0` is explicit; `a : R` is arbitrary. There is no finite-variable, decidable-equality, characteristic, domain, nontriviality, field, or characteristic-zero hypothesis. The actual type is captured by the native target receipt:

```lean
theorem hasseDeriv_C {d : σ →₀ ℕ} (hd : d ≠ 0) (a : R) :
    hasseDeriv d (C a) = 0
```

The proof rewrites `C a` as `monomial 0 a`, applies project `hasseDeriv_monomial`, gets the zero factor from project `hasseCoeff_eq_zero_iff`, and simplifies the zero monomial. These project dependencies are mathematical interfaces, not established mathlib replacements.

## Phase 2 — preliminary checks

SMALL: a computational constant case, not a main result or a new structure. The word Hasse refers to the parent operator; this lemma is not an independent named classical theorem. Exhaustive search was nevertheless performed. One-line-definition test: **n/a, theorem**. Its short proof alone does not classify its upstream API value; no defeq/diamond exemption is needed for a theorem.

## Phase 3 — exhaustive literature

Exact requests, SHA256 and byte counts of exact returned representations, status/limitations, and concise original summaries are retained in [web metadata](../evidence/MvPolynomial.hasseDeriv_C/web-requests.json). Full web articles/search bodies are deliberately not persisted. The date window for recent arXiv is 2021-10-26 through 2026-10-26. The local source excerpt is [clean.tex §1](../evidence/MvPolynomial.hasseDeriv_C/local-reference-excerpt.tex).

| Channel | Actual query/access | Result and locator |
|---|---|---|
| Web specific | `multivariate Hasse derivative constant polynomial nonzero multi index` | Multivariate Taylor-coefficient definition located; constant case follows since translation fixes scalars. Primary Narváez source subsequently opened. |
| Web general | `Hasse Schmidt derivation over commutative rings constants base algebra` | Algebra-relative HS systems over commutative rings; no characteristic-zero division required. |
| Web aliases | `divided derivatives higher derivation constant positive characteristic` | Divided/higher derivatives identify the same context; positive characteristic matters and prevents substituting ordinary iterated derivatives without hypotheses. |
| ChatGPT mathematical MCP | unavailable | n/a: `ask_chatgpt_math` is not configured in available tools. No substitute opinion invented. |
| Local references | `rg Hasse|\\Delta|derivative .mathlib-quality/references/clean.tex` | Lines 122–153: multi-index binomial definition, zero when a coordinate order exceeds the exponent, linear extension. Constants are its exponent-zero specialization. |
| nLab | domain search, then direct `ncatlab.org/nlab/show/Hasse-Schmidt+derivative` | Indexed page states a commutative-rig formulation. Direct fetch fails with unsupported `application/xhtml+xml`; no full-page reading claimed. |
| nCatLab | domain search plus separate `/ncatlab/show/Hasse-Schmidt+derivative` | Separate path inaccessible. General categorical perspective found through HS literature, not claimed as a successful nCatLab page fetch. One initial `site.ncatlab.org` query typo is retained honestly, followed by correct `site:ncatlab.org/nlab`. |
| Stacks | domain search then [09CH](https://stacks.math.columbia.edu/tag/09CH) | Definition 10.133.1 and Example 10.133.5: generic finite-order differential operators include a multiplication part. This does **not** provide arbitrary-operator constant annihilation. |
| MathOverflow | `site:mathoverflow.net Hasse Schmidt derivation constants`, then [question 440759](https://mathoverflow.net/questions/440759/what-is-the-relationship-between-higher-order-derivations-in-the-sense-of-hasse) | February 13, 2023 question distinguishes HS systems and differential operators using algebra maps into truncated power series. Used as perspective, not as an answered theorem or replacement. |
| recent arXiv | broad multivariate date query; refined `site:arxiv.org/abs/ "Hasse-Schmidt" "2024"` and `"Hasse derivatives" "2023"` | [Bravo–Tirado Hernández 2409.19093](https://arxiv.org/abs/2409.19093), submitted September 27, 2024, concerns HS integrability over k-algebras. Also 2402.18717, submitted February 28, 2024, uses Hasse-Schmidt derivative terminology. Broad query's older/irrelevant hits were not treated as recent evidence. |

Primary formulation: [Narváez Macarro, A mini-course on Hasse-Schmidt derivations](https://personal.us.es/narvaez/course_HS_2018.pdf), September 2018, Definition 2.1.1 (printed pp.14–15), Proposition 2.1.4 (printed p.16). Multivariate HS components are linear and satisfy a higher Leibniz rule; they package as an algebra homomorphism into power series. Since an algebra homomorphism fixes the base scalars as constant power series, every nonzero coefficient kills those scalars. This last implication is our inference from the primary definition, not a direct quotation. The polynomial Taylor-coefficient family is a concrete instance. We do not rely on the PDF extraction of Proposition 2.1.5 as a zero-index claim.

Literature summary: standard names are multivariate Hasse derivative, divided derivative, higher/Hasse-Schmidt derivative. Sources vary between polynomial formulas over fields, commutative rings, and more abstract algebra-relative systems; the target already supports commutative semirings and arbitrary variable types, beyond the usual finite-variable field presentation. The abstract HS family is broader mathematics, but requires a new parent structure and identification, not dropping a hypothesis in this theorem. No conflicting normalization was found.

## Phase 4a–b — generality

| Parameter/hypothesis | Current form | Literature comparison / possible weakening | Checked conclusion |
|---|---|---|---|
| variable universe/type `σ` | arbitrary `Type*` | Literature often finite tuples | Already arbitrary; no `Fintype` to drop. |
| coefficient universe/type `R` | arbitrary `Type*` | Rings/fields common | Already universal in its interface. |
| coefficient structure | `CommSemiring R` | Binomial construction needs no subtraction | This is the literal floor of `MvPolynomial`, `C`, and `monomial` in Basic.lean:81,93,105. A raw Finsupp/AddMonoidAlgebra model with weaker assumptions would change the interface and is not a verified one-edit weakening. |
| multi-index `d` | finitely supported naturals | Finite tuples customary | Finite support is the natural arbitrary-variable polynomial order. Arbitrary signed/fractional orders change the object. |
| nonzero order `hd` | `d ≠ 0` | Standard positive total order | Essential for uniform arbitrary constants: at `d=0`, the result is `C a`, and `a=1` over ℕ disproves zero. Native isolated necessity check records this. Empty `σ` makes hd impossible, a legitimate vacuous boundary specialization rather than a flaw. |
| constant `a` | unrestricted element | Standard scalar constant | No nonzero requirement; `a=0` works even at zero order. Cannot delete parameter without changing statement. |

Verdict: **MAXIMALLY GENERAL for the fixed parent interface**, zero verified mechanical weakening opportunities. No strengthening to a ring, field, nontrivial or characteristic-zero assumption is needed. No claim that the algebraic construction has an absolute categorical floor is made.

## Phase 4c — all nine modern-idiom rows

| # | Question | Answer / proposal | Concrete downstream consequence |
|---|---|---|---|
| 1 | typeclasses versus explicit structure predicates | Already `CommSemiring` and bundled linear maps; hd is a proposition, not structure | Current instance API composes directly. |
| 2 | sequences/metrics versus filters | no: finite polynomial computation | No topology exists to improve. |
| 3 | construction versus universal property | `Finsupp.lsum` already expresses free linear extension; HS-system packaging is a separate possible parent API | Single-monomial computation comes from existing `lsum_single`; building a new HS system would unify product/composition laws but is not required here. |
| 4 | closure predicates versus bundled substructures | no predicate-shaped substructure in statement | A kernel/range formulation would add bundling work for the actual scalar evaluation caller. |
| 5 | field/vector-space versus module/semiring hierarchy | Already commutative semiring and linear map | Includes positive characteristic and zero divisors. No verified weakening of the fixed MvPolynomial statement. |
| 6 | higher-category upgrade | no: scalar constant normalization | No concrete higher-categorical consumer identified. |
| 7 | concrete number index versus arbitrary monoid | Natural exponents encode polynomial monomials | Arbitrary additive group would alter polynomial object/binomial order. Rejected. |
| 8 | concrete-via-abstract diagnostic | **fires**: after monomial and scalar-zero rewrites, the named Hasse operator disappears; final `simp` contains zero occurrences | Abstract statement: any linear extension whose component at exponent zero annihilates a kills C a. `C a` is definitionally the zero monomial, and `lsum_single` supplies the extension step. The essential factor-zero premise remains. See native abstract probe and diagnostic JSON. |
| 9 | false-generalization guard | Reject arbitrary linear-map/finite-order-differential-operator annihilation without normalization premise | Identity linear map at C 1 is a counterexample, now checked directly as `HasseCTargetProbe.false_arbitrary_linear_map` in the alternative receipt. Higher Hasse components are generally not ordinary derivations; `derivation_C` alone is inapplicable. |

Modern-idiom verdict: generic extension machinery is already present. The diagnostic identifies an abstraction **with a necessary normalization premise**, not a new unconditional Hasse theorem or an automatically publishable generic helper. Building an abstract HS-family package might be mathematically valuable for product, substitution and coefficient laws, but is not a mechanically verified generalise-first edit to this declaration. No cosmetic categorical upgrade is recommended.

## Phase 4.5 — infrastructure risk

n/a: declaration kind is theorem. It creates no typeclass instance, coercion, definitional equality, or reducibility path. Thus typeclass diamond, reducibility leak, noncanonical unfolding, instance-priority collision, universe infrastructure and coercion ambiguity rows are all theorem-inapplicable; no definition-risk claims are borrowed from the parent assessment. Its theorem universes are nevertheless read in the actual native signature.

## Phase 4.6 — proof strategy, all five rows

| # | Strategy question | Applies? | Result |
|---|---|---|---|
| 1 | epsilon/neighborhood versus filters | no | No topology. |
| 2 | element algebra versus submodule/ideal inclusions | considered; no improvement | Scalar normalization is precisely the needed application form; a range/kernel containment would specialize back to it. |
| 3 | sequences versus nets | no | No analysis. |
| 4 | object construction versus universal characterization | considered | Parent uses free linear extension already; its `lsum_single` law is the proper generic route. |
| 5 | missing helper mathlib should have | concrete parent API only | Multivariate Hasse monomial law and binomial factor support are project declarations. No additional generic linear-extension helper is missing. |

Current strategy **MATHLIB-IDIOMATIC**: reduce a constant to its zero-exponent monomial, then kill the scalar factor. A coefficient proof or abstract HS proof is possible but adds machinery for this local goal. The independent raw-definition proof (with explicit single-monomial reduction to avoid a C/monomial simp loop) verifies the existing strategy is not concealing a characteristic assumption. Cost is not a verdict factor.

## Phase 5 — five actual mathlib methods, all three forms

Raw complete requests/results: [current Finder](../evidence/MvPolynomial.hasseDeriv_C/finder-current.json), [current Loogle](../evidence/MvPolynomial.hasseDeriv_C/loogle-current.json), [current LeanSearch](../evidence/MvPolynomial.hasseDeriv_C/search-current.json), [current local](../evidence/MvPolynomial.hasseDeriv_C/local-current.json); corresponding `*-literature.json` and `*-abstract.json` are included in the manifest. [Source rg receipts](../evidence/MvPolynomial.hasseDeriv_C/grep-receipts.json) preserve commands, full output and statuses. The guessed nonexistent MonoidAlgebra/LinearAlgebra.lean path failure is retained and corrected by Module.lean; it is not an empty-result claim.

| Method | Current form | Literature-standard form | Abstract form |
|---|---|---|---|
| Finder | nonzero multivariate Hasse derivative kills constants | relative higher/HS system kills scalars | Finsupp linear extension of zero monomial |
| Loogle | `Polynomial.hasseDeriv, Polynomial.C` | `MvPolynomial.pderiv, MvPolynomial.C` | `Finsupp.lsum, Finsupp.single` |
| LeanSearch | Hasse constant law, nonzero order | higher derivation scalar law | lsum single component law |
| source rg | exact qualified target + hasseDeriv declarations over all mathlib | higher/HS/derivation names in MvPolynomial tree | `lsum_single`, coefficient equivalence, literal C and monomial source |
| local name patterns | `hasseDeriv_C` | `hasseDeriv` | `lsum` |

The local service explicitly reports `index: unavailable` and its fallback includes project evidence excerpts. Only `.lake/packages/mathlib/Mathlib/...` positives are mathlib candidates; evidence snippets and project symbols do not establish upstream presence. External indexes can differ from the pinned checkout. Positive candidates were checked against the pinned sources and actual native signatures.

* `Polynomial.hasseDeriv_C`, Algebra/Polynomial/HasseDeriv.lean:116, is for a single ℕ order on univariate polynomials, over `Semiring`. It is an exact moral analogue, not arbitrary-variable transport. Using project singleton/unique-variable compatibility theorems would add project API and/or restrict σ.
* `MvPolynomial.pderiv_C`, Algebra/MvPolynomial/PDeriv.lean:86, and `MvPolynomial.derivation_C`, Algebra/MvPolynomial/Derivation.lean:56, cover ordinary derivations. Higher Hasse derivatives need not satisfy the ordinary Leibniz rule; no generic Derivation instance can be assumed. Factorial rescaling would lose arbitrary-characteristic generality.
* `Finsupp.lsum_single`, LinearAlgebra/Finsupp/LSum.lean:123, computes extension on a singleton. `MvPolynomial.C_apply`, Basic.lean:138, is literally `C a = monomial 0 a`. These are genuine existing building blocks, but neither proves the concrete factor at zero vanishes.

Conclusion: partial matches and normalization building blocks found. Search failures do not prove absence. The isolated guarded concrete proof tests the normalization route directly; no generic duplicate term was identified. No exhausted `exact?` Hasse-delta search was repeated or limits raised.

## Phase 5.5 — statement shape

Normal form: application equals **0**, already canonical RHS. Equivalent forms include `hasseDeriv d ∘ₗ C.toLinearMap = 0` (with an appropriate bundled scalar embedding), scalar-image containment in the kernel, and a conditional `if d=0 then C a else 0` all-order formula. These are not existing equivalent theorem claims; they describe interface choices. The current application form matches both `Polynomial.hasseDeriv_C` and its actual rewrite consumer. Bundling would require a scalar-linear map rather than directly treating the ring hom C as a linear map.

Syntactic alternatives considered: explicit d first; `0 < d` in the pointwise order; total-order-zero/nonzero case split. `d ≠ 0` is readily available in the caller's `eq_or_ne d 0` branch and avoids an additional equivalence proof. The current statement therefore remains easiest to apply. The native probes test literal `C`/monomial interchange and the caller's nonzero branch. Actual additional native shape attempts are preserved in [alternative executed source](../evidence/MvPolynomial.hasseDeriv_C/alternatives-executed.lean) and [complete success receipt](../evidence/MvPolynomial.hasseDeriv_C/alternatives-lsp.json):

```lean
theorem explicit_order (d : σ →₀ ℕ) (a : R) (hd : d ≠ 0) :
    hasseDeriv d (C a) = 0 := original hd a

theorem all_orders (d : σ →₀ ℕ) (a : R) [Decidable (d = 0)] :
    hasseDeriv d (C a) = if d = 0 then C a else 0 := by
  classical
  by_cases hd : d = 0
  · subst d
    simp
  · simpa only [ite_eq_right hd] using original hd a
```

Both compile without errors or warnings. The explicit-order reshuffle works but offers no benefit to the current caller, which has `hd` directly and inferred d. The all-order conditional is a genuine checked alternative; its statement needs `[Decidable (d = 0)]` to elaborate the `if`. A `classical` tactic only inside the proof cannot retroactively supply statement elaboration. An initial attempt lacking that binder (and using deprecated `if_neg`) is retained as rejected evidence. This additional syntactic requirement is unnecessary for the target's implication form, so the current theorem is retained as the preferred application interface. These alternatives use `original`, an independently replayed project proof, and are statement-shape evidence rather than existing-mathlib replacement terms. No claimed alternative weakening is accepted without proof.

Superfluous audit: σ and R locate the algebra; `CommSemiring` is required by the fixed algebra/C/monomial interfaces; d selects the operator; hd excludes the verified zero-order counterexample; a is the scalar under differentiation. No superfluous parameter or typeclass was identified. **SHIP-AS-STATED** if the named lemma is selected for export; whether it receives `[simp]` is a future API question, not a current statement error.

## Phase 6.0 — actual callers and inline audit

Internal use count outside declaring file: **1**, in **1** source file. Same-file uses excluding the declaration: **0**.

| Caller | Exact use | Role / possible refactor |
|---|---|---|
| `Roth/Taylor.lean:127`, private `MvPolynomial.coeff_taylor_monomial_aux` starts at 120 | `simp [← C_apply, hasseDeriv_C hd, hd.symm]` | Nonzero derivative-order branch of exponent-zero induction case. Keep named theorem; if upstream later elects inlining, replace its use by local factor-zero fact and unfolded linear-extension simplification. The affected branch was replayed both ways with controlled `simp only` (the original source simp list left the coefficient goal `(C a).coeff d = 0` under this imported downstream environment; separate unfolded/inline attempts looped when C_apply was supplied to unrestricted simp); no proof through downstream public coeff_taylor is used. |

All 14 project Lean sources were included in the untruncated source rg audit and hashed. Broader searches for Hasse/C/zero-factor derivations found no separate inline rederivation of this constant law. Taylor.lean:113 proves vanishing of derivatives in an absent variable for a general monomial; it is a related stronger-support calculation, not an inline repetition of the constant theorem. MainLemma matches involving the letter C are bounds, not constant-polynomial derivatives.

This is an **explicit Lean-source-reference** audit. The target is **not** tagged `[simp]` in current source, and its actual caller supplies the theorem explicitly in a simp set. Imported lower-level simp dependencies and opaque kernel dependency closure are not enumerated. The caller does use simp implicitly for other identities; zero explicit matches elsewhere would not alone establish dead code. Here a real direct use is present.

## Phase 6 — composition experiments

1. Existing univariate/ordinary-derivation calls are near-misses for the arbitrary-variable higher operator; no replacement term follows solely from their types.
2. The original two-line proof uses project `hasseDeriv_monomial` and `hasseCoeff_eq_zero_iff`, so cannot support NO-composable-from-mathlib.
3. Independent mathlib-only raw delta: factor-zero is a finite-product/binomial/order argument; a typed `Finsupp.lsum_single` term first establishes the monomial interface; `rw [C_apply, delta_monomial, factor_zero hd]; simp` then closes the constant normalization. The helper is freshly proved, not an existing mathlib declaration. Exact successful code and receipt are retained. Abstract lsum normalization similarly requires its `b 0 = 0` premise.
4. The actual Taylor nonzero branch is checked with original theorem and with local factor-zero/unfolded proof. This verifies an actionable possible inlining plan at the only explicit call site, not deletion of the target or an independently rebuilt full private caller.

Conclusion: **no verified ≤3-existing-call term**, with a successful closing-simp construction route. Phase 6b explicitly calls such a route **borderline: trivial simp composition; user decides if worth a lemma**. A helper proof or a short tactic script is not counted as three existing theorem calls. Likewise `hL a` in the abstract C/zero-monomial diagnostic only packages the needed annihilation premise; it does not supply that premise for Hasse operators.

## Phase 7 — verdict and action

**BORDERLINE-needs-human**, independently reached from the standard law, actual single caller, pinned partial matches, and verified simplifying construction. It is not a cost downgrade or inherited parent verdict. The specific judgment is whether this named positive-order constant law is a useful exported normalization theorem alongside a future multivariate Hasse API, despite the short reduction to monomials and factor-zero. The theorem is not junk: it is mathematically standard and used by Taylor expansion. It can remain in `Roth/HasseDeriv.lean` while that API is designed.

Future upstream design questions, at most five:

1. Export the nonzero-order constant law as a named theorem alongside the multivariate monomial law, despite its closing-simp derivation?
2. Make the conditional theorem a `[simp]` rule, or keep callers explicitly supplying the nonzero-order hypothesis as here?
3. Prefer this `d ≠ 0` argument order, or align exactly with the univariate `(k) (a) (0 < k)` surface using an explicit multi-index?
4. Add an all-order conditional constant formula as the primary normalization interface, keeping this as a corollary?

No answer is needed to complete this read-only assessment. If later selected, the exact home is `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`, grouped with the accepted multivariate parent definition/coefficient API; run `/generalise MvPolynomial.hasseDeriv_C` and `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_C` before preparing a PR. If omitted upstream, retain it locally or inline the compiled affected branch; do not replace it with the univariate theorem without a justified transport.

## Phase 8 — evidence and limitations

The package contains exact executed sources, successful complete native receipts, all actual formal-search receipts, source commands/hashes, metadata-only web evidence, assessment and overview JSON, copy hashes/bytes, and a portable read-only validator. Root acceptance remains pending until independent review. Initial virtual and Taylor failures are retained separately as rejected receipts, including the C_apply/monomial simp loop and an unsuccessful coefficient/evaluation simplification. The accepted Taylor branch uses `simp only [← C_apply, taylor_C, hasseDeriv_C hd, map_zero, coeff_C_of_ne_zero hd]`; its inline version uses the scalar-zero fact and an explicitly proved zero derivative before the same controlled simplification. The later alternative receipt also verifies explicit argument order, the all-order conditional with an explicit decidability binder, and a direct arbitrary-linear-map counterexample. No failed or recovered placeholder result is accepted. Accepted proofs use only standard Lean axioms, with no placeholders, unsafe evaluation, new axioms, or raised limits.

Limitations: optional mathematical MCP unavailable; local index unavailable; direct nLab/nCatLab accesses failed as recorded; external search indexes may not match the pinned version; caller audit is source-only and branch execution is deliberately scoped. None of these is silently converted into proof of theorem absence or a requirement to stop.
