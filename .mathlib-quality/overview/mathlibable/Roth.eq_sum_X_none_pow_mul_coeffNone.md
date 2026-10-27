# Roth.eq_sum_X_none_pow_mul_coeffNone — NO-mathlib-has-it

Mathlib already has finite coefficient expansion as `Polynomial.as_sum_range_C_mul_X_pow'`. Applying it to `optionEquivLeft R τ P` gives precisely the distinguished-variable expansion in canonical polynomial coordinates. The actual inverse-equivalence bridge and full sole caller refactor have been checked separately; the old spelling is not claimed to be a one-call or definitionally equal replacement. This is an independent positive assessment, not inheritance of declarations152 or155.

## Phase 0 — Baseline and scope

Public theorem156/293 is at `Roth/Separation.lean:98` on `ramin-cleanup`. The entire561-line declaring module and its separated-representation, determinant, and integrality context were read. Fresh hashes of all17 source/pin inputs match the successful baseline. The newer complete build also succeeded,2467jobs,exit0. No production, Git, or progress files changed.

Evidence: [fresh inputs](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/inputs.json), [baseline](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/baseline-build.txt), [complete build](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/index-file-completion-2026-10-27.json), [entire module](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/Roth-Separation.lean.txt). Original native type, complete kernel printer and axioms passed without errors/warnings/partial results; target-specific diagnostics start at5716 and the fresh canonical audit at5719. Whole-file error and axiom checks remain active.

## Phase 1 — Comprehend

Any multivariate polynomial can be collected in powers of one chosen variable. If the degree in that variable is at most n, retaining powers0 through n recovers the whole polynomial. The coefficient of each power is a polynomial in the other variables. Zero polynomials and empty/infinite remaining-variable types are included.

Full native type:

```lean
@Roth.eq_sum_X_none_pow_mul_coeffNone :
  ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
    (P : MvPolynomial (Option τ) R) {n : ℕ},
    MvPolynomial.degreeOf none P ≤ n →
      P = ∑ ν ∈ Finset.range (n + 1),
        MvPolynomial.X none ^ ν *
          (MvPolynomial.rename some) (Roth.coeffNone P ν)
```

`τ` indexes the remaining variables; `R` is the coefficient semiring; `P` and `n` determine the polynomial and cutoff. The bound prevents omitted nonzero coefficients. Surrounding Fintype/DecidableEq assumptions are already omitted. The source proof uses coefficient extensionality, the private product-coefficient helper, `coeff_coeffNone`, exponent reconstruction153, and the support bound `monomial_le_degreeOf` to prove the out-of-range branch zero. These project lemmas are not mathlib building blocks.

Evidence: [native type](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/native-type.json), [original receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-original-audit-receipt.json), [executed original](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-original-executed.lean.txt).

## Phase 2 — Preliminary checks

SMALL: an elementary coefficient reconstruction law rather than a new structure or main theorem. The definition-only one-line test is n/a: this is a theorem. Its sole caller is useful and mathematically substantial, so zero external-file references do not make it dead code. Size and call count do not decide the verdict.

## Phase 3 — Exhaustive literature

Every named channel was attempted, including three distinct general-web forms. Web receipts retain exact requests, response hashes/bytes, titles/locators and original summaries, not full bodies. Signed/credential query parameters are excluded from archived URLs if present. No artificial channel is added to reconcile the informal nine-channel label.

| Channel | Actual query | Result |
|---|---|---|
| Specific web | `multivariate polynomial collecting powers one variable coefficient expansion polynomial ring` | Magma primary documentation describes collecting coefficients with respect to a selected variable; Wolfram Collect supplies computational terminology. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-web-specific.json) |
| General web | `polynomial ring iterated polynomial ring R x y isomorphism R x y coefficients` | McKernan lecture15 Lemma15.7 gives the natural iterated ring isomorphism with an explicit example. Direct PDF fetch502; search extract is summarized honestly. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-web-general.json) |
| Alias web | `polynomial coefficient expansion degree bound sum coefficients powers indeterminate semiring` | Semiring coefficient-expansion chapter preview and coefficient-vector formulations; secondary hits do not establish technical claims. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-web-alias.json) |
| ChatGPT mathematics | Standard form/generality/historical evolution | n/a: `ask_chatgpt_math` unavailable. |
| Local source | `collecting\|roth:lem2\|coefficient` in clean.tex | Lemma2 proof line374 collects terms in powers of the last variable; exactly this use. [search](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/local-literature-search.json), [excerpt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/clean-separation-excerpt.tex.txt) |
| nLab | `site:ncatlab.org/nlab polynomial ring universal property coefficients` | Free commutative algebra/formal finite monomial sums; direct fetch400 unsupported XHTML. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-nlab.json) |
| nCatLab | `site:ncatlab.org/ncatlab polynomial ring coefficient` | Returned /nlab pages, no in-namespace hit. Not evidence of absence. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-ncatlab.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial ring coefficients variables` | Polynomial presentations/base change; supplementary tag00SK accessed; no new coefficient reconstruction law identified. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-stacks.json) |
| MathOverflow | `site:mathoverflow.net polynomial rings infinitely many variables coefficients` | Infinite-variable and noncommuting-coefficient contexts; no exact replacement theorem. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-mo.json) |
| Recent arXiv | `site:arxiv.org polynomial rings coefficient expansion multivariate 2022 2023 2024 2025 2026` |2504.21708 and2502.21058, both2025, concern representations in subrings and skew extensions; related context, no novelty/priority inference. [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-arxiv.json) |

Primary locators: [Magma coefficient operations](https://docs.magma-maths.org/BasicRings/MultivariatePolynomialRings/operation-element.html), [McKernan lecture15](https://mathweb.ucsd.edu/~jmckerna/Teaching/15-16/Spring/103B/l_15.pdf), [nLab polynomial](https://ncatlab.org/nlab/show/polynomial), [Stacks00SK](https://stacks.math.columbia.edu/tag/00SK), [Vu2025](https://arxiv.org/abs/2504.21708). Actual direct access outcomes are [recorded](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/literature-primary-access.json).

Concept: finite coefficient expansion/collecting powers of an indeterminate. Sources agree on the mathematical content. Most general standard form is a formal polynomial over a semiring, expressed as a finite sum of coefficient monomials, or after transport through an iterated polynomial-ring equivalence. The project paper uses finite-variable polynomials over ℚ/ℤ; this theorem already removes those restrictions. Classical collecting-terms notation and free-algebra universal-property notation are different presentations, not different identities. No historical priority claim is needed.

## Phase 4a — Generality

| Parameter / hypothesis | Current versus standard; weakening audit |
|---|---|
| `τ : Type u_1` | Arbitrary remaining-variable type; already covers infinite and empty types because polynomials have finite support. |
| `R : Type u_2` | Independent coefficient universe; not specialized to rationals/integers. |
| `CommSemiring R` | Needed for fixed MvPolynomial/optionEquivLeft interface. Generic Polynomial expansion actually compiles under Semiring A; that is a wider representation, not a mechanical weakening of this parent. |
| `P` | Arbitrary, including0; no domain/characteristic/nonzero hypothesis. |
| `n : ℕ` | Arbitrary inclusive cutoff; ℕ is essential for ordinary polynomial powers/range. |
| `hn : degreeOf none P ≤ n` | Ensures support lies in the retained exponents. Removing the bound loses P=X with cutoff0; actual counterexample checked. |
| Endpoint `n+1` | Includes exponent n. Replacing by range n fails even for P=1,n=0; actual counterexample checked. |
| Distinguished `none` | Canonical Option split; a selected variable of arbitrary σ can be moved into this form using existing `Equiv.optionSubtypeNe`/`degreeOf_eq_natDegree` representation. No new selected-variable theorem claimed compiled. |
| Finite sum representation | Support sum and strict-cutoff `natDegree p < m` are existing equivalent Polynomial APIs; range n+1 is convenient for the actual caller's Fin(n+1). |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL for the fixed `coeffNone`/Option-polynomial surface; no verified mechanical hypothesis weakening is proposed. The verified wider representation is the existing generic theorem under `[Semiring A]`:

```lean
p = ∑ ν ∈ Finset.range m, Polynomial.C (p.coeff ν) * Polynomial.X ^ ν
```

with `p.natDegree < m`. Thus the polynomial coefficient ring can be any semiring; choosing `A = MvPolynomial τ R` specializes it. Changing the project parent's typeclass to Semiring would not supply its existing commutative-algebra equivalence. There is no unsupported generalise-first ticket. [Actual generic proof and guards](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-guards-executed.lean.txt), [native receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-guards-receipt.json).

## Phase 4c — Modern idiom

| # | Diagnostic | Answer / concrete consequence |
|---|---|---|
|1|Typeclass preambles|No: algebraic assumptions are already classes; no ad hoc predicates.|
|2|Sequences/metrics versus filters|No: finite algebraic identity without topology.|
|3|Construction versus universal property|Yes at representation level: existing `optionEquivLeft` bundles the iterated polynomial-algebra isomorphism. Transport its coefficient expansion instead of redoing exponent arithmetic; composes with map_sum/map_mul/map_pow.|
|4|Set with closure versus bundled subobject|No closure predicate or subobject to bundle.|
|5|Field-specific versus module/semiring hierarchy|Generic Polynomial theorem already works over Semiring A; original is already CommSemiring rather than field. Enables noncommutative coefficient semirings for generic univariate expansion, without falsely weakening MvPolynomial's interface.|
|6|Higher categorical form|No relevant coherence/higher morphism content.|
|7|Concrete indices|Natural exponents are ordinary polynomial data; generalized monoids would replace Polynomial with monoid algebra, and finite range/degree would require different structure. Arbitrary remaining variables already supported.|
|8|Concrete-via-abstract diagnostic|Yes: source extensional proof only uses support/coefficient laws, never special arithmetic of R or a named concrete P. In canonical coordinates this is generic Polynomial finite expansion. Actual canonical and inverse bridge proofs show agreement, so existing coefficient-support APIs become directly reusable.|
|9|False-generalization guard|Pass for actual equivalence transport and generic polynomial coefficient ring. Removing degree cutoff or endpoint is rejected by compiled inequalities. Power series need infinite sums/completeness or finite support; arbitrary monoid exponents do not preserve the claimed range identity.|

Modern idiom available and already in mathlib: finite expansion plus algebra-equivalence transport. No claim of a new categorification or a missing abstract reconstruction principle.

## Phase 4.5 — Infrastructure risks

n/a: theorem, not def/class/instance. No new typeclass diamond, reducibility leak, noncanonical definitional unfolding, instance priority, universe implementation, or CoeFun/CoeSort path. The inverse constant-polynomial bridge is a propositional proof, not silently treated as definitional equality.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Finding |
|---|---|---|
|1|ε–δ versus filters|n/a: algebraic finite identity.|
|2|Elementwise versus subobjects|Coefficient extensionality is sound, but transporting known polynomial expansion avoids exponent/support reproofs; no ideal/submodule inclusion is needed.|
|3|Sequences versus nets|n/a: no limits.|
|4|Constructed object versus universal property|Use existing equivalence and its maps, rather than reconstructing a polynomial from coefficients manually.|
|5|Missing helper API|No missing reconstruction law. A named inverse-C/rename normalization lemma may improve convenience; actual proof is `aevalTower_C` through existing symm definition. It is not claimed an existing helper theorem.|

REFACTOR-RECOMMENDED: apply the existing polynomial expansion and transport through `optionEquivLeft.symm`. This removes dependencies on project coefficient/exponent helpers in the expansion proof. Full caller applicability was actually checked. Cost does not determine the verdict.

## Phase 5 — All five actual methods on all three forms

Complete formal-search responses and exact requests are archived. Each row has Finder, Loogle, LeanSearch, source-rg and local-name search.

| Form | Finder | Loogle | LeanSearch | rg | Local |
|---|---|---|---|---|---|
|Current Option expansion|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-current-finder.json): some irrelevant `expand` substitution hits, inverse-equivalence candidate useful|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-current-loogle.json): related coefficient laws|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-current-leansearch.json): finite sum theorem|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/rg-current.json)|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-current-local.json): source positives, index unavailable|
|Literature finite coefficient expansion|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-literature-finder.json): exact theorem|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-literature-loogle.json): exact theorem|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-literature-leansearch.json): monomial and C-times-power variants|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/rg-literature.json)|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-literature-local.json): source positives|
|Modern equivalence transport|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-modern-finder.json): degree/equivalence candidates|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-modern-loogle.json): exact degree bridge|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-modern-leansearch.json)|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/rg-modern.json)|[receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/search-modern-local.json): degree bridge source hit|

Local index unavailable is recorded, not used to infer absence. External indices may differ from the pin. Positive candidates were inspected in pinned source and actually applied in isolated native Lean with target absence guarded.

Concluded: found in mathlib as `Polynomial.as_sum_range_C_mul_X_pow'`, more general finite coefficient expansion, `Mathlib/Algebra/Polynomial/Degree/Support.lean:93`. Its `[Semiring A]` signature and actual proof application were checked. Necessary representation ingredients: `MvPolynomial.optionEquivLeft` (`Equiv.lean:467`), `MvPolynomial.natDegree_optionEquivLeft` (`Equiv.lean:578`), `optionEquivLeft_symm_X` (`Equiv.lean:504`), and `Polynomial.aevalTower_C` (`AlgebraMap.lean:566`), plus map_sum/map_mul/map_pow and multiplicative commutation. [Mathlib source hashes](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/mathlib-inputs.json).

## Phase 5.5 — Statement shape

Normal form: canonical `Polynomial` expansion, with coefficient-times-X-power on the RHS. Equivalent forms considered include monomial sums (source-inspected existing `as_sum_range'`); coefficient-times-power sums and the original renamed Option expression were actually native-tested with the bridge. The original orientation expands P on the RHS appropriately; the representation is application-specific rather than wrong.

Syntactic generality: strict cutoff m with natDegree<m works over Semiring A; inclusive n+1 matches the actual Fin(n+1) caller. Keep the caller's inclusive bound, converting with natDegree_optionEquivLeft and Nat.lt_succ_of_le. Superfluous arguments: NONE. Both universes, τ,R,P,n determine the polynomial and coefficients; CommSemiring belongs to the fixed parent; hn is essential as the guard shows. No hidden Fintype/DecidableEq remain. Overall RESTATE-BEFORE-SHIP if proposing an upstream wrapper: use existing canonical theorem instead. The project surface may remain locally useful exposition.

## Phase 6.0 — Complete caller and inline audit

Fresh canonical-source lexical enumeration, `rg --no-ignore` and tracked `git grep` agree: one declaration plus one use, both in Separation. Internal use count excluding declaring file:0; same-file uses:1; external files:0. Not dead code.

| Caller | Original use | Verified refactor |
|---|---|---|
|`Roth.exists_separated_representation`, `Separation.lean:335`|After `Fin.sum_univ_eq_sum_range`, apply target to construct hP'|Replace with existing polynomial expansion transported by the exact inverse bridge; `coeffNone` unfolds definitionally to Polynomial.coeff. Keep the actual private basis, linear-independence and reconstruction helper constants and the full remainder of the proof.|

Private `eq_sum_aeval_basis_coeffNone_aux` and `exists_coeffNone_basis_aux` consume an expansion equality as an explicit premise; neither directly calls the target. They are retained unchanged in the actual full caller replay. Inline searches find those premises and the public caller, not another derivation of the full bounded expansion. Source counts and direct kernel-value consumers are separate; a fresh exact ordered293 audit finds only `Roth.exists_separated_representation`. No opaque transitive or simp-closure claim is made.

Evidence: [rg](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/caller-rg.json), [git grep](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/caller-git-grep.json), [lexical enumeration](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/lexical-enumeration.json), [inline search](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/rg-inline.json), [canonical audit](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-audit-executed.lean.txt), [full caller source](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-caller-executed.lean.txt), [caller receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-caller-receipt.json).

## Phase 6 — Actual composition experiments

In canonical polynomial coordinates the proof uses the existing expansion theorem and degree identity:

```lean
Polynomial.as_sum_range_C_mul_X_pow' _
  (Nat.lt_succ_of_le ((natDegree_optionEquivLeft R P).trans_le hn))
```

That actual term is accepted. The entirely generic Semiring version is a single call `p.as_sum_range_C_mul_X_pow' hn`. The original Option syntax additionally requires transporting equality with the inverse equivalence and normalizing maps, inverse X, inverse C and factor order. The inverse-C fact was proved in scratch by changing to `aevalTower` and applying its C law. It is a real representation bridge, not an existing library theorem counted as one call. The full old-form normalization uses more than three named existing ingredients, and is NOT claimed a ≤3-call composition. A closing `simp [defs...]` alone would be Phase6b BORDERLINE evidence; that is not the argument for this positive existing-law hit.

The actual isolated `canonical`, `inverse_C`, `expanded` proofs verify the exact old form without importing Roth; `#check_failure` prevents circular target use. The complete sole caller replays all basis and independence steps using original private constants, replacing the target invocation with the verified expanded bridge.

An initial isolated attempt omitted explicit R in natDegree_optionEquivLeft, producing a type mismatch and recovered placeholders; it is preserved as rejected. The clean corrected execution alone is accepted. A speculative redundant #check was removed before execution, so no failed-API claim is made. Guard source proves that removing the bound and dropping the inclusive endpoint give false identities. No limits were raised.

[Clean isolated source](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-isolated-executed.lean.txt), [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-isolated-receipt.json), [guards source](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-guards-executed.lean.txt), [receipt](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/coefficient-expansion-guards-receipt.json).

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it.** The generic reconstruction law is exactly `Polynomial.as_sum_range_C_mul_X_pow'`; specializing its coefficient ring and transporting through the existing algebra equivalence proves the supplied theorem. The exact canonical call and genuine representation bridge are both verified. This verdict concerns an existing mathematical law under a canonical representation; it does not assert the old syntax is a one-call replacement, and does not inherit parent152's NO-composable verdict. Source-local usefulness does not create a second upstream reconstruction principle.

Refactor the sole caller `exists_separated_representation` at335: retain its Fin-to-range conversion, apply the existing polynomial expansion to `optionEquivLeft R τ P` with the degree identity, then transport by the inverse as in the full accepted replay. The private basis/independence/reconstruction helpers remain actual original constants; no axiom or target invocation is substituted. Only after this concrete caller change should the wrapper theorem be deleted. If source exposition warrants retaining the named statement, its alternative destination is project-local `Roth/Separation.lean`, alongside coeffNone and the paper's chosen convention. Optional inverse-C/rename convenience API is a separate question; it is not a missing reconstruction theorem. No upstream PR grouping/reviewer checklist applies to this NO verdict, and no cost-based downgrade is used.

## Phase 8 — Evidence completion

All mandatory phases passed or carry theorem/optional-service n/a justification. Accepted original, canonical, representation, guard, and full caller proofs have clean actual native receipts and standard axioms only. The rejected recovered-placeholder attempt remains separate. Fresh17input hashes, full build receipt, exact ordered canonical293 audit and credential guard are checked by the portable validator. No unresolved verification item remains; root acceptance is pending independent review.

[Assessment](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/assessment.json), [verification](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/verification.json), [overview entry](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/overview-entry.json), [portable validator](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/validate.py), [current manifest](../evidence/Roth.eq_sum_X_none_pow_mul_coeffNone/copy-manifest.json).
