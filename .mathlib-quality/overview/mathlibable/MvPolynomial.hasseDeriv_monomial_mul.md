# MvPolynomial.hasseDeriv_monomial_mul — completed private-helper overview triage

**Verdict: SKIP — private declaration (overview Step9a).** All applicable inventory, structural review, caller audit, proof verification and evidence checks are complete. The full public-declaration mathlibable workflow is explicitly inapplicable under the installed prefilter; this is not a public contribution verdict.

## Rule, inventory and mathematics

The [installed overview rule](../evidence/MvPolynomial.hasseDeriv_monomial_mul/prefilter-rule.md) lists the private modifier. The source at `Roth/HasseDeriv.lean:225` is a private lemma. [Exact source and metadata](../evidence/MvPolynomial.hasseDeriv_monomial_mul/corrected-target.json) freshly match production. Private source names have generated kernel names; this assessment verifies a scratch public replay rather than claiming resolution of the original private constant.

For arbitrary variable type σ and commutative semiring R, let d,a be natural finite-support indices with a j=0 for each j in d.support. Then for every c:R and multivariate polynomial g,

```lean
hasseDeriv d (monomial a c * g) = monomial a c * hasseDeriv d g
```

Thus a monomial involving none of the differentiated variables passes through the Hasse operator. The condition constrains exponents, not the coefficient or input g. No finite variable set, decidable equality, nonzero coefficient, degree bound on g, field, characteristic or factorial-invertibility premise is present. The actual polymorphic replay type confirms the CommSemiring parent interface.

The proof inducts on g by monomials and addition. For the monomial case, coordinatewise support separation proves a+b-d=a+(b-d) in truncated natural subtraction. The binomial factor hasseCoeff d(a+b) equals hasseCoeff d b, because a vanishes at every relevant coordinate. Monomial multiplication and commutative scalar arithmetic finish. The addition case uses linearity and distributivity. [Exact body](../evidence/MvPolynomial.hasseDeriv_monomial_mul/target-excerpt.lean.txt) is retained.

## Dependencies and callers

Project dependencies are the Hasse operator, scalar factor and monomial evaluation rule. Existing mathlib supplies MvPolynomial.induction_on', monomial_mul_monomial, Finsupp support membership, Finset.prod_congr, addition/truncated-subtraction simplification and semiring distributivity. It is a concrete support-separated operator proof, rather than an independent new generic finite-product construction.

There is exactly one explicit executable source invocation: public `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, declared at243, invokes this helper at `Roth/HasseDeriv.lean:246`. That caller expands its arbitrary undifferentiated factor f over monomials and derives each exponent-separation hypothesis from degreeOf j f=0. [Caller excerpt](../evidence/MvPolynomial.hasseDeriv_monomial_mul/caller-excerpts.lean.txt) and [untruncated searches](../evidence/MvPolynomial.hasseDeriv_monomial_mul/source-search.json) preserve the evidence. No explicit external production-file invocation of the private helper was found. This is source-level caller coverage, not opaque kernel/simp closure.

## Applicable structural review

**Mathlib API:** existing monomial multiplication, finite-product congruence and truncated-subtraction simplification support the proof. The project monomial Hasse computation is the operator-specific bridge. No separate missing generic finite-product or exponent infrastructure is needed. The public product theorem has its own subsequent full assessment; it inherits no SKIP verdict.

**Duplication:** this is the monomial step of one public factor-separation theorem, shared through a clear local helper. The same operator law is not re-proved independently elsewhere in the bounded source audit. The public theorem is a generalization to arbitrary factors rather than a duplicate at the same interface.

**Generality:** σ and g are unrestricted; the coefficient ring is already a commutative semiring. The support hypothesis is a sufficient coordinate-separation criterion with no unverified converse or claim of necessity. No unrelated noncommutative representation or abstract weighted family is proposed as a literal weakening.

**Missing API:** no generic helper deficiency blocks this induction. The public factor-separation Hasse interface is assessed next. Whether a future upstream module should use this exact private proof layout is left to its authorized cleanup, without fabricating an independent contribution verdict here.

**Junk/style/documentation:** keep the descriptive private helper. It isolates the monomial base case and coordinate subtraction from the public proof. A single explicit call is legitimate for a focused induction helper and does not itself establish junk. Its proof is below the cleanup size threshold; a public docstring/export is unnecessary for its private role. No production edit, rename, deletion or statement change is recommended by this triage.

## Verification and evidence

All17 source/pin hashes freshly match the successful full lake build baseline (2467jobs,exit0). Native Lean additionally replayed the entire original proof, with only its declaration name/namespace changed to `PrivateMonomialFactorAssessment.replay`. Its actual type and axiom report were queried. The whole scratch document completed with zero errors/warnings, no failed dependencies and only propext/Classical.choice/Quot.sound in every printed axiom set. No sorry, new axiom, unsafe/native_decide or resource-limit increase was introduced.

[Verification index](../evidence/MvPolynomial.hasseDeriv_monomial_mul/verification.json), [raw native receipt](../evidence/MvPolynomial.hasseDeriv_monomial_mul/native-replay.json), [exact executed source](../evidence/MvPolynomial.hasseDeriv_monomial_mul/executed.lean.txt), [baseline](../evidence/MvPolynomial.hasseDeriv_monomial_mul/baseline-build.txt) and [fresh input hashes](../evidence/MvPolynomial.hasseDeriv_monomial_mul/source-check.json) are preserved. Live scratch bytes matched the archived executed content before acceptance. Earlier scratch declarations are verified context, not extra completed public assessments. Archived .lean.txt content preserves proof evidence without introducing workspace Lean modules; the receipt retains the actual .lean execution path.

## Completion and next action

Applicable inventory, source/caller audit, API/duplication/generality/missing-API/junk review, private prefilter, native proof and evidence gates: complete. Full public mathlibable literature/search/modern-idiom/contribution phases: n/a under the explicit private rule. No unresolved item or user input remains.

[Assessment](../evidence/MvPolynomial.hasseDeriv_monomial_mul/assessment.json), [overview entry](../evidence/MvPolynomial.hasseDeriv_monomial_mul/overview-entry.json), [manifest](../evidence/MvPolynomial.hasseDeriv_monomial_mul/copy-manifest.json) and [portable validator](../evidence/MvPolynomial.hasseDeriv_monomial_mul/validate.py) supply the machine record. After independent acceptance and publication, continue with `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, the first unfinished canonical declaration.
