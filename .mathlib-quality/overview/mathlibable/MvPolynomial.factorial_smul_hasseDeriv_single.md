# MvPolynomial.factorial_smul_hasseDeriv_single

Verdict: **YES-add-as-is**. This is the characteristic-free coordinate identity linking multivariate Hasse operators to iterated formal partial derivatives. The positive univariate analogue is not a replacement on arbitrary multivariate inputs. Assessment complete; root acceptance pending; production files unchanged.

## Phase 0 — baseline

The shared successful `lake build` completed2467 jobs with exit0. All17 production source/pin SHA256 values were freshly recomputed and matched the shared baseline before reuse. The theorem resolves at `Roth/HasseDeriv.lean:286`; full module read, including its definitions, computational API and downstream compatibility lemmas. Exact target type/axioms and independent replay succeeded in the native project document. Evidence: [baseline](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/baseline-build.txt), [input check](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/input-check.json), [exact native verification map](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/verification.json).

## Phases 1–2 — content and preliminary checks

For every polynomial P over a commutative semiring R, any variable j, and any natural number n, multiplying its Hasse derivative of multi-index ne_j by n! gives the n-fold iterate of formal differentiation in j. No division is used, so the statement includes positive characteristic. For example, second ordinary differentiation loses the coefficient of X² in characteristic2 while the second Hasse derivative still equals1.

Full elaborated type (universe names from the native receipt):

```lean
∀ {σ : Type u_3} {R : Type u_4} [CommSemiring R] (j : σ) (n : ℕ)
  (P : MvPolynomial σ R),
  ↑n.factorial • (hasseDeriv (Finsupp.single j n)) P = (⇑(pderiv j))^[n] P
```

σ is an arbitrary variable type; R the coefficient semiring; j the coordinate; n the order; P the input. The sole typeclass is CommSemiring R; there are no extra propositions, finiteness, characteristic, injectivity or nonzero assumptions. Mathematical proof: order0 is identity; differentiating the ordern equality, using R-linearity and ∂jΔd=(dj+1)Δ(d+e_j), gives the factorial successor. [Exact source excerpt](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/target-excerpt.lean.txt).

SMALL: a standard operator compatibility theorem, not a new structure or project's main Roth theorem. Phase2b one-line-definition check is n/a: kind theorem, independently of its short induction proof.

## Phase 3 — exhaustive literature

All nine channels were attempted; three distinct actual general-web queries cover coordinate, abstract iterative and alias formulations. Optional ChatGPT math unavailable. Explicit nCatLab-namespace access also failed with URL not accessible; no independent categorical corroboration is claimed. Local clean.tex§1 gives the monomial construction over commutative semirings and normalized mixed-partial formula over Q-algebras. Narváez Macarro's introduction, pp2980–2981, gives coordinate Hasse operators and binomial composition. Stacks tag07GK Lemma23.2.2 gives the analogous factorial identity for divided powers in commutative ideals. Recent arXiv2024/2025 results concern integrability and iterative operators; their abstracts give no stronger replacement for this coordinate identity. Direct nLab open failed400 unsupported XHTML, while the search result exposed its multivariate monomial formula; no full-page access is claimed.

See the complete per-channel queries, source URLs/locators, original summaries and access limitations in [literature](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/literature.md), exact requests and returned-payload hashes in [web requests](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/web-requests.json) and [direct access receipts](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/web-open.json). Full article/search bodies are not retained.

Standard form: n!Δ(ne_j)=∂j^n, and more abstractly factorial scaling for an **iterative** family. General Hasse–Schmidt Leibniz axioms alone do not imply iterativity. Dividing by factorial requires extra invertibility and would unnecessarily narrow this theorem.

## Phase 4a–b — parameters and generality

| Parameter / hypothesis | Assessment |
|---|---|
| σ : Type* | Arbitrary, including infinite types; finite support replaces global finiteness. No Fintype, Unique or DecidableEq argument to drop. |
| R : Type*, CommSemiring R | Fixed parent interfaces MvPolynomial/pderiv require CommSemiring. Actual mathlib-only `#check_failure` confirms pderiv cannot elaborate under just Semiring. No claimed weakening. A different noncommutative coefficient representation would be new machinery. |
| j : σ | Specifies the coordinate; no distinguished/default choice needed. Compiled distinct-coordinate check uses k≠j. |
| n : ℕ | Natural factorial and finite iteration are essential; n=0 covered. No restriction to positive orders or invertible factorials. |
| P | Arbitrary multivariate polynomial, including inputs involving coordinates other than j. A polynomial solely in Xj is a proper specialization. |
| Scalar cast | Equivalent ℕ-smul form compiled using Nat.cast_smul_eq_nsmul R. This changes presentation, not hypotheses or mathematical generality. |

MAXIMALLY GENERAL for the pinned multivariate polynomial and formal partial-derivation interface; zero verified literal weakenings. Generic recurrence below is a new theorem with new premises, not a drop of CommSemiring in the existing statement. Cost plays no role in the verdict.

## Phase 4c — all nine modern-idiom checks

| # | Question | Answer / consequence |
|---|---|---|
|1|Typeclasses rather than bundled hypotheses?|Already CommSemiring; no ad-hoc structure hypothesis.|
|2|Filters or nets?|No topology or convergence.|
|3|Universal-property characterization?|No object is constructed here. Derivation is already bundled.|
|4|Bundled substructure instead of closure predicate?|No subset/closure predicate. Endomorphism-power equality compiled as complementary shape.|
|5|Weaken field/vector assumptions?|Already semiring and arbitrary characteristic; fixed parent CommSemiring floor checked.|
|6|Higher category?|No categorical assertion or construction to replace.|
|7|Generalize concrete index?|n counts finite iterates and factorials, σ arbitrary; replacing ℕ by a general monoid loses these operations.|
|8|Concrete-via-abstract diagnostic?|Fires: after applying pderiv_hasseDeriv, the remaining work is scalar/factorial/iterate algebra. Generic additive recurrence and two actual consumers compiled; see below.|
|9|False-generalization guard?|Dropping factorial is false over ℕ; cancelling factorial or recovering Hasse operators from ordinary iterates is false in ZMod2. Replacing an iterative family by arbitrary Hasse–Schmidt operators is unjustified. Both explicit polynomial guards compiled.|

The compiled abstract extraction is:

```lean
{M : Type*} [AddCommMonoid M]
(D : M →+ M) (H : ℕ → M → M)
(hzero : ∀ x, H 0 x = x)
(hsucc : ∀ n x, D (H n x) = (n + 1) • H (n + 1) x)
(n : ℕ) (x : M) : n.factorial • H n x = (⇑D)^[n] x
```

This extracts the elementary induction and actually specializes both to our multivariate family and to Polynomial.hasseDeriv using its existing binomial composition law. It is meaningful **proof reuse**, not evidence that the coordinate theorem should be replaced: the consumers must still supply the substantive coordinate-specific recurrence, and the abstract statement says nothing about Hasse derivatives, partial derivations or polynomial coefficients. No preexisting mathematical consumer becomes expressible only through this helper; both already have exactly these polynomial interfaces. Thus Q8 fires but the honesty-bar conclusion is **no mandatory modern statement replacement**. Keep the standard named coordinate compatibility result; optionally share the recurrence induction in an upstream proof. This is not a YES-as-is justified by avoiding an expensive abstraction, nor a claimed mechanical weakening. [Q8 diagnostic](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/q8-diagnostic.json), [project consumer](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/consumer-executed.lean.txt), [mathlib-only generic/Polynomial consumer](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/raw-executed.lean.txt).

## Phase 4.5 — infrastructure risks

Theorem n/a for all six rows: typeclass diamonds (adds no instance); reducibility leak (adds no definition); noncanonical unfolding (no new definitional equality); instance priorities (no instance); universe restriction (arbitrary independent Type* parameters); coercion ambiguity (no new coercion). The bundled alternate statement required an explicit equality of the derivation and its linear-map coercions; a rejected attempt is retained separately and never counted as proof success.

## Phase 4.6 — proof strategy

| # | Question | Answer |
|---|---|---|
|1|Topology ε–δ vs filters?|n/a, algebraic finite iteration.|
|2|Element proof vs ideal/submodule inclusion?|No such inclusion. Pointwise operator equality is natural; equivalent bundled endomorphism-power form compiled.|
|3|Sequences vs nets?|n/a, finite natural-number iteration is not convergence.|
|4|Construction vs universal property?|n/a, existing operators are related.|
|5|Missing helper mathlib should have?|Canonical multivariate Hasse recurrence pderiv_hasseDeriv is a substantive prerequisite for upstreaming. Generic additive recurrence is an optional reusable induction helper; it is independently proved, not an existing replacement.|

MATHLIB-IDIOMATIC: natural induction via the canonical recurrence is the right argument. The independent mathlib-only experiment reconstructs delta, its coefficient formula, binomial cocycle, partial recurrence and finally this factorial theorem; no imported project theorem or own downstream simp result closes the raw proof.

## Phase 5 — five actual methods × three forms

| Method | Current coordinate form | Literature factorial form | Abstract divided-power/recurrence form |
|---|---|---|---|
|Lean-Finder|Polynomial.factorial_smul_hasseDeriv; pderiv-adjacent results|Polynomial analogue, LaurentSeries.derivative_iterate|DividedPowers.factorial_mul_dpow_eq_pow; Polynomial analogue|
|Loogle|Initial Function.iterate identifier query rejected; successful pderiv retry yields ordinary derivative API|Polynomial.hasseDeriv + Nat.factorial yields exact univariate analogue|Initial iterate query rejected, retry rate-limited; final successful DividedPowers query yields ideal-theoretic analogue|
|LeanSearch|Polynomial analogue plus pderiv/mkDerivation|Polynomial analogue and LaurentSeries result|DividedPowers ideal API and Polynomial analogue|
|rg pinned source|No multivariate Hasse/factorial theorem hit|Polynomial/HasseDeriv133 and LaurentSeries191|DividedPowers/Basic213; no higher-derivation/recurrence structure match|
|local name search|Project target only|Pinned Polynomial analogue and archived evidence false positives explicitly excluded|Generic iterate names, no matching recurrence; index reports unavailable|

[Exact request/receipt index](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/formal-search.json), [untruncated source searches](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/source-search.json). Unavailable local index and external revision drift do not prove absence. Positive candidates were read at the pinned revision; Polynomial theorem's full Semiring signature and actual use routes are native-checked. DividedPowers concerns elements of a commutative ideal and cannot simply be applied to the generally noncommutative algebra of all endomorphisms. LaurentSeries is a different coefficient-indexed representation. A commutative subalgebra of generated operators plus a divided-power structure would require new proofs, not a free specialization.

Mathlib-only missing-name guards succeed for MvPolynomial.hasseDeriv and the exact target; this establishes namespace availability only. We make no claim that a failed exact? establishes nonexistence. The raw constructive experiment identifies the concrete normalization premises needed beyond extensionality.

## Phase 5.5 — statement shape

Normal forms considered: original pointwise R-smul equality, pointwise ℕ-smul equality, equality of functions, and bundled linear-endomorphism equality `(n! : R) • Δ(ne_j) = pderiv(j).toLinearMap ^ n`. All alternatives compiled. Polynomial.factorial_smul_hasseDeriv uses a function equality with ℕ-smul, so a complementary function or endomorphism version would align with that API. Current RHS is already the ordinary iterate normal form; pointwise rewriting avoids coercion bookkeeping at use sites. SHIP-AS-STATED, with optional companion bundled theorem, rather than replacing this useful pointwise interface with a generic recurrence criterion.

Superfluous-argument audit: σ and R determine polynomial type; CommSemiring enables fixed interfaces; j specifies which derivative; n specifies factorial/iterate; P is input. None can be removed without changing the statement. There is no hidden Fintype, Nontrivial or characteristic assumption.

## Phase 6.0 — callers and inline audit

| Source reference | Role |
|---|---|
|Roth/HasseDeriv.lean:35|Module main-result documentation only.|
|Roth/HasseDeriv.lean:286|Declaration itself.|

Zero explicit proof invocations; zero external-to-file callers. Scope is repository source text, not opaque kernel/simp dependency closure; theorem is not a simp theorem. Search for related factorial/iterated-partial patterns found no equivalent inline derivation elsewhere. Its lack of current callers is recorded in junk audit, but a standard compatibility theorem can complete a reusable upstream API without an immediate Roth consumer. The raw and generic experiments are assessment consumers, not retroactively counted as project usage.

## Phase 6 — actual composition experiments

1. **Pinned Polynomial analogue:** it operates on Polynomial R, not MvPolynomial σ R. A change-of-representation route for arbitrary P would need a coordinate separation and compatibility for both Hasse and iterated partial derivation. Existing single-variable `aeval(Xj)` bridge covers only polynomials in Xj; Unique σ is stronger than the target. No ≤3 existing-call replacement established.
2. **Existing ordinary derivative/coefficient API:** independent raw delta and coefficient proofs use monomial/additive induction, vanishing/binomial support analysis, finite-product cocycle, the partial recurrence, and induction on n. This is an actual successful proof; it is substantive new reasoning, not three calls and not a closing `simp [defs]` composition.
3. **Abstract route:** generic recurrence proof is successful and its actual Polynomial/MvPolynomial consumers compile, but recurrence is newly proved evidence. The MvPolynomial consumer still requires the project pderiv_hasseDeriv theorem. New helpers and project parents do not count as existing mathlib building blocks. Extensionality alone does not normalize either side.

NOT-COMPOSABLE from existing pinned mathlib in ≤3 calls. The short original induction does not change that conclusion: it relies on the new multivariate Hasse recurrence. No successful terminal-simp composition was found or used to infer an automatic NO.

## Phases 7–8 — actionable verdict

**YES-add-as-is.** Add the coordinate factorial identity as part of the multivariate Hasse derivative API. It provides the missing bridge between characteristic-free Hasse coefficient computations and the existing formal Derivation/Function.iterate API. Over characteristic zero users can then invert factorials when their coefficient algebra allows it; over characteristic p the theorem precisely describes the loss of information in ordinary iteration, without falsely identifying the operators.

The concrete API gap is compatibility of a newly supplied multivariate Hasse family with the already bundled coordinate derivations. Neither the univariate theorem nor commutative-ideal divided powers gives this on arbitrary multivariate P. The raw independent proof and both false-generalization guards support this conclusion. Zero present project callers weakens evidence of local demand, not the mathematical standardness or the clear compatibility role. The generic recurrence experiment supports optional sharing of the induction proof and does not require discarding the canonical coordinate identity.

Proposed location: `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` (new module, with base Hasse API). PR title: **feat(Algebra/MvPolynomial/HasseDeriv): relate iterated partial and Hasse derivatives**. Group with already accepted YES declarations read from current progress: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv`, `MvPolynomial.hasseDeriv_map`, `MvPolynomial.hasseDeriv_rename`, `MvPolynomial.hasseDeriv_hasseDeriv`, and especially `MvPolynomial.pderiv_hasseDeriv`. The generic recurrence helper may be factored into a suitable iteration/additive-hom module after API review; it does not need its own invented higher-derivation structure here.

Pre-PR checklist:

- `/generalise MvPolynomial.factorial_smul_hasseDeriv_single` — reconfirm fixed parent-interface floor and shape choice.
- `/cleanup Roth/HasseDeriv.lean MvPolynomial.factorial_smul_hasseDeriv_single` — full style/proof/diff gates before transplant.
- Select reviewers from relevant recent commits: Yaël Dillies (631b214f7c, MvPolynomial refactor2026-09-02) or Moritz Firsching (334438dace, HasseDeriv_map2026-08-19). [Exact commit receipt](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/reviewer-source-search.json).

Verification complete, unresolved mathematical checks=[]: exact project target/replay, pointwise natural scalar, function and bundled forms, other-coordinate test, factorial necessity over ℕ, characteristic2 distinction, independent mathlib-only factorial proof, fixed-interface failure guard, generic recurrence and two actual consumers. Only standard axioms propext/Classical.choice/Quot.sound. Accepted sources and full receipts in [verification map](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/verification.json); rejected attempts isolated. Portable [validator](../evidence/MvPolynomial.factorial_smul_hasseDeriv_single/validate.py) checks current manifest, source/pin hashes, phase completion, exact native sources, diagnostics/axioms and report links.
