# MvPolynomial.coeff_aeval_X_mul — completed private-helper overview triage

**SKIP — private declaration, overview Step 9a.** Inventory, mathematical/structural review, caller audit, and native proof/dependent verification are complete. The [installed prefilter](../evidence/MvPolynomial.coeff_aeval_X_mul/prefilter-rule.md) explicitly excludes private declarations from the full public contribution assessment. No exhaustive public mathlibable literature/search verdict is claimed.

## Statement and inventory

Source is `Roth/Taylor.lean:63–80`, a private lemma in the commutative-semiring section. [Exact canonical source](../evidence/MvPolynomial.coeff_aeval_X_mul/corrected-target.json), [source excerpt](../evidence/MvPolynomial.coeff_aeval_X_mul/target-excerpt.lean.txt), and [complete module](../evidence/MvPolynomial.coeff_aeval_X_mul/Taylor-module.lean.txt) preserve the original. The full fresh native replay type is:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (i : σ) (f : R[X]) (B : MvPolynomial σ R),
  (∀ e ∈ B.support, e i = 0) →
    ∀ (d : σ →₀ ℕ), ((Polynomial.aeval (X i)) f * B).coeff d = f.coeff (d i) * B.coeff (Finsupp.erase i d)
```

In plain terms, multiply a univariate polynomial in the selected variable X_i by a multivariate polynomial B independent of that variable. Its coefficient at multi-index d factors as the univariate coefficient at d_i times B's coefficient at d with coordinate i erased. This is a coefficient-separation calculation, rather than a Taylor or derivative theorem.

Every parameter has a role: σ is any variable type, R any commutative semiring, i the selected coordinate, f the univariate factor, B the remaining factor, hB its support-independence premise, and d the desired coefficient. No Fintype, externally supplied DecidableEq, nonempty-variable, nonzero-factor, field/domain or characteristic assumption remains. Classical decidability is local to the proof. The support premise is actively used to eliminate every nonmatching univariate exponent; no assumption removal or alternative representation is proposed without verification.

## Proof and project dependencies

Expand the univariate evaluation into its coefficient sum, distribute multiplication, and extract each multivariate monomial coefficient. Only exponent d_i can survive. If a different exponent lies below d, the remaining exponent has a positive i-coordinate, contrary to B's support premise; if it is not below d, the monomial coefficient is zero directly. For the selected exponent, erase/add-single reconstruction identifies the complementary multi-index. A missing f coefficient is handled by its support criterion.

There are **no direct project theorem or definition dependencies** in this helper. Existing library primitives include Polynomial.eval₂_eq_sum, Polynomial.sum_def, MvPolynomial.coeff_monomial_mul′, Finsupp.erase_add_single, Finset.sum_eq_single, and support/choose-free natural subtraction normalization. The [pinned coefficient excerpt](../evidence/MvPolynomial.coeff_aeval_X_mul/mathlib-coefficient-excerpt.lean.txt) and [source searches](../evidence/MvPolynomial.coeff_aeval_X_mul/source-search.json) document the actual API used. These are structural proof observations, not a full search establishing that mathlib lacks a public equivalent.

## Callers and duplication

Exactly one explicit invocation appears, `Roth/Taylor.lean:115`, inside private `coeff_taylor_monomial_single_add_aux` (declared at101). That proof applies the helper to the one-coordinate binomial polynomial and the translate of the complementary monomial. It establishes hB from the induction hypothesis and vanishing Hasse coefficient. [Caller excerpt](../evidence/MvPolynomial.coeff_aeval_X_mul/caller-excerpt.lean.txt) and exact word-boundary searches preserve declaration/use distinctions. No explicit outside-file caller was found; this is a source-level audit, not an opaque kernel/simp dependency closure.

No second implementation of this exact coefficient separation was found in the inspected module. Related Hasse coefficient and binomial identities serve distinct roles: they identify the surviving scalar after this helper has separated variables. One direct use does not make this helper junk; its statement isolates an understandable convolution reduction from the longer induction step.

## Applicable structural review

**Mathlib API and missing API:** existing evaluation, monomial multiplication and finite-sum primitives suffice for the current proof. No missing primitive blocks it. Whether a polished generic coefficient-separation theorem should be exported upstream is not decided by the private prefilter; this SKIP is not a public NO or absence result.

**Generality:** the coefficient identity already works over arbitrary commutative semirings and arbitrary variable types. No cancellation or nonzero premise is used. The support-independence hypothesis has a concrete proof role; neither its weakening nor noncommutative coefficients were claimed verified. The native replay confirms no ambient finiteness instance accidentally entered its type.

**Naming, documentation and junk:** retain the private helper unchanged. Its name identifies the coefficient, substituted variable and product. An explanatory inline comment could be optional in a future production-edit pass; no public docstring/export or API rename is needed for its present private role. There is no sorry, axiom, resource-limit raise, TODO or proof over30 lines in the declaration.

## Native proof and dependent verification

The complete original proof body is replayed as `MvPolynomial.PrivateCoeffAevalAssessment.replay`, with only its private declaration name changed. Private source names have generated kernel names, so this is an exact source replay rather than a guessed original-private #check. The [accepted complete receipt](../evidence/MvPolynomial.coeff_aeval_X_mul/native-replay.json) prints the full elaborated type and standard axioms. The [exact executed document](../evidence/MvPolynomial.coeff_aeval_X_mul/executed.lean.txt) preserves all code and the original request path.

The entire direct caller is also replayed as `...caller`, using this new replay in place of the private coefficient helper. Its two other private dependencies use their separately accepted scratch replays from the earlier taylor_X validation. Their proof bodies are unchanged; this naming adjustment avoids generated private kernel names. The caller's mathematical statement and remaining proof are retained. This verifies the actual dependent proof, not a claim to have migrated the whole production module.

Both target and caller have only propext, Classical.choice, Quot.sound. Final diagnostics are complete, no errors/warnings or failed dependencies, no sorry/admit/new axioms/unsafe/native_decide or raised limits. One preparatory caller line exceeded100 columns after qualification; only wrapping changed. Its [rejected receipt](../evidence/MvPolynomial.coeff_aeval_X_mul/native-rejected.json) is retained separately and is not accepted proof evidence.

All17 production source/pin hashes freshly match the clean full-build baseline: [baseline](../evidence/MvPolynomial.coeff_aeval_X_mul/baseline-build.txt), [manifest](../evidence/MvPolynomial.coeff_aeval_X_mul/input-manifest.json), [fresh comparison](../evidence/MvPolynomial.coeff_aeval_X_mul/source-check.json). Production remains unchanged, so the shared build continues to validate all existing dependents; no versions were changed.

## Completion and action

Keep the private helper unchanged. All applicable overview checks are complete; full public literature, formal five-method search, modern-idiom contribution routing and upstream planning are n/a under the explicit private rule. No item is deferred or blocked. The SKIP does not settle the next public coefficient theorem's contribution assessment.

[Assessment](../evidence/MvPolynomial.coeff_aeval_X_mul/assessment.json), [verification](../evidence/MvPolynomial.coeff_aeval_X_mul/verification.json), [overview entry](../evidence/MvPolynomial.coeff_aeval_X_mul/overview-entry.json), [portable current-manifest validator](../evidence/MvPolynomial.coeff_aeval_X_mul/validate.py), and [manifest](../evidence/MvPolynomial.coeff_aeval_X_mul/copy-manifest.json) preserve the completed record. Root acceptance and publication follow independent final checks. Next canonical declaration is the private `MvPolynomial.hasseCoeff_single_add_eq`.
