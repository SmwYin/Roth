# MvPolynomial.coeff_taylor_monomial_single_add_aux — completed private-helper overview triage

**SKIP — private declaration under overview Step 9a.** Applicable inventory, mathematical/structural review, caller audit and native proof/dependent checks are complete. The [private prefilter](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/prefilter-rule.md) excludes the full public contribution workflow. No public mathlibable absence, redundancy or inclusion verdict is inferred.

## Source, full type and mathematical meaning

Private lemma at `Roth/Taylor.lean:101–118`. [Canonical source](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/corrected-target.json), [exact excerpt](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/target-excerpt.lean.txt), [entire module](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/Taylor-module.lean.txt). Fresh native type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (a : R) {i : σ} (n : ℕ) {k : σ →₀ ℕ},
  k i = 0 →
    (∀ (d : σ →₀ ℕ), ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))) →
      ∀ (d : σ →₀ ℕ),
        ((taylor α) ((monomial (Finsupp.single i n + k)) a)).coeff d =
          (eval α) ((hasseDeriv d) ((monomial (Finsupp.single i n + k)) a))
```

Assume the coefficient of the translate of a residual monomial equals the evaluated Hasse derivative, for every multi-index. If the residual monomial has exponent zero at coordinate i, the same identity holds after adjoining the factor X_i^n. This is the single-coordinate induction step of the coefficient Taylor theorem, not an arbitrary-substitution evaluation equation.

Parameters: arbitrary variable type σ and commutative semiring R; α translation values, a coefficient, i selected coordinate, n arbitrary natural exponent, k residual natural multi-index, hi its zero i-coordinate, ih the coefficient identity at every residual index, d the target index. No Fintype, external DecidableEq, nonempty-variable, positive n, nonzero coefficient, field/domain or characteristic hypothesis occurs. ih is used at arbitrary e for support control and at the complementary index for coefficient extraction. No weakening is inferred by invoking the later coefficient theorem, which would be circular as an assessment of this induction proof.

## Mathematical argument and direct dependencies

Identify (X_i+α_i)^n with evaluation of the univariate binomial polynomial at X_i. The induction hypothesis and vanishing Hasse coefficient show that the translated residual monomial still has no supported i-exponents. Split the target monomial into its selected-coordinate power times residual monomial, use translation's multiplicativity and variable law, and apply the private coefficient-separation lemma. The univariate binomial coefficient formula supplies n.choose(d_i). The other two private helpers split the multivariate binomial coefficient and residual evaluation power product into the same factors; commutative multiplication finishes.

Direct project dependencies (statement and body):

- MvPolynomial.taylor and MvPolynomial.hasseDeriv.
- MvPolynomial.taylor_X, MvPolynomial.hasseDeriv_monomial, MvPolynomial.hasseCoeff_eq_zero_iff.
- Private MvPolynomial.coeff_aeval_X_mul, MvPolynomial.hasseCoeff_single_add_eq, MvPolynomial.prod_pow_single_add_tsub.

These project helpers are not counted as existing mathlib building blocks. Existing library API includes Polynomial.coeff_X_add_C_pow, monomial_single_add, map_mul/map_pow, eval_monomial, support membership and finite-index normalization. [Source searches](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/source-search.json) preserve the actual univariate primitive. No exhaustive library-only composability claim is made.

## Caller and duplication audit

One explicit caller: private `MvPolynomial.coeff_taylor_monomial_aux`, declared Taylor120, invokes this step at **Taylor129** in its Finsupp single_add case. [Caller excerpt](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/caller-excerpt.lean.txt), exact word-boundary search in the source-search receipt. No explicit outside-file invocation found; source-level audit does not enumerate opaque kernel/simp dependency closure.

The leaf scalar helpers have separate roles, while this declaration assembles them with the polynomial induction hypothesis and support argument. Generic aeval_monomial computes an image as a product; it does not by itself identify each translated coefficient with a Hasse evaluation. The later public coeff_taylor adds linearity across arbitrary polynomials. These are distinct layers, so the short proofs of earlier translation aliases do not classify this induction step as redundant. No second exact step implementation appears in the module.

## Applicable structural assessment

**API and missing API:** existing univariate binomial and multivariate coefficient/support laws support the decomposition. The three private helpers isolate the required coefficient, binomial, and power-product calculations; there is no missing primitive preventing the current proof. Potential public Hasse/Taylor APIs require their own full assessment.

**Generality:** verified arbitrary variables and commutative-semiring coefficients, without characteristic or cancellation assumptions. The selected-coordinate condition and induction hypothesis have concrete roles in this proof. No additional mechanical weakening was proposed or claimed tested. The scalar helper's separately verified CommMonoid generalization does not weaken the polynomial/translation interface of this step.

**Naming/documentation/junk:** retain private helper. The name records its coefficient-Taylor, monomial and single-coordinate induction roles. Keeping the step separate makes the Finsupp induction caller short. No public docstring/export, rename, inlining, sorry, new axiom, resource raise, TODO or proof over30 lines is needed or present. One use is expected for an induction-case helper.

## Native target and dependent verification

The original proof is replayed as `MvPolynomial.PrivateTaylorStepAssessment.replay`, replacing only private identifiers with their independently accepted source-equivalent scratch proofs from canonical58–60 and wrapping long qualified lines. The actual statement and mathematical proof are preserved. [Complete accepted receipt](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/native-replay.json), [exact executed source](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/executed.lean.txt). Private declarations have generated kernel names; no guessed original-private lookup is claimed.

The complete direct caller, the Finsupp induction proving the coefficient theorem for arbitrary monomials, is also replayed as `...caller`, using this new step. Its base-case proofs and all remaining steps are retained. This is actual dependent-proof verification, not a claim of production migration or simplification of the public Taylor theorem. The proof does not use the later coeff_taylor to establish its own induction step.

Final diagnostics are complete success, partial=false, no errors/warnings or failed dependencies. Both target and caller use only propext, Classical.choice, Quot.sound. No sorry/admit, new axiom, unsafe/native_decide or raised limits are introduced; no rejected native attempts for this declaration. [Verification index](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/verification.json).

All17 source/pin hashes freshly match the clean full-build baseline (2467 jobs): [baseline](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/baseline-build.txt), [manifest](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/input-manifest.json), [fresh comparison](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/source-check.json). Production and versions remain unchanged, so the shared build continues to validate existing dependents.

## Completion and action

Keep unchanged. All applicable inventory/API/duplication/generality/missing-API/junk/caller/private-prefilter/native/evidence checks are complete. Full public contribution phases are n/a under the explicit rule, not claimed executed. No outstanding item or required user input remains.

[Assessment](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/assessment.json), [overview entry](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/overview-entry.json), [portable validator](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/validate.py), [current manifest](../evidence/MvPolynomial.coeff_taylor_monomial_single_add_aux/copy-manifest.json). After acceptance and publication, continue with private `MvPolynomial.coeff_taylor_monomial_aux`.
