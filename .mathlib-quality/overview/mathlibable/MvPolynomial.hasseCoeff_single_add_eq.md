# MvPolynomial.hasseCoeff_single_add_eq — completed private-helper overview triage

**SKIP — private declaration under overview Step 9a.** All applicable inventory, structural review, caller audit and native proof/dependent verification are complete. Full public literature/search/contribution assessment is n/a under the [explicit private prefilter](../evidence/MvPolynomial.hasseCoeff_single_add_eq/prefilter-rule.md); no public NO or absence claim is inferred.

## Exact source and full type

Private lemma at `Roth/Taylor.lean:82–90`. [Canonical source](../evidence/MvPolynomial.hasseCoeff_single_add_eq/corrected-target.json), [exact excerpt](../evidence/MvPolynomial.hasseCoeff_single_add_eq/target-excerpt.lean.txt), [full declaring module](../evidence/MvPolynomial.hasseCoeff_single_add_eq/Taylor-module.lean.txt). Its fresh native replay type is:

```lean
∀ {σ : Type u_2} {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 → ∀ (d : σ →₀ ℕ), hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (Finsupp.erase i d) k'
```

A multivariate binomial coefficient at a monomial whose i-exponent is n factors into the ordinary binomial coefficient n.choose(d_i) and the binomial product for every other coordinate. The residual exponent vector k′ has zero i-coordinate, and erasing i from d removes that coordinate from the second factor. Everything lives in natural multi-indices and natural scalars.

σ is arbitrary; i and n are arbitrary; k′ and d are finitely supported natural functions; hi asserts k′_i=0. There is no coefficient ring, variable finiteness, external decidable equality, nonempty-variable, positive n, dominance or nonzero-binomial assumption in the actual type. The surrounding commutative-semiring section contributes no unused R instance. Local classical reasoning supplies the decidability needed for erasure and finite products.

## Mathematical proof and project dependencies

Unfold the project definition `MvPolynomial.hasseCoeff` and use existing `Finsupp.mul_prod_erase′` to separate the i-coordinate from the product indexed by d. The selected factor becomes n.choose(d_i), since hi and the single-coordinate addition identify its upper index with n. On the erased support, j≠i, so the one-coordinate summand vanishes and the remaining factors agree by `Finsupp.prod_congr`. This also handles d_i=0 and coordinates missing from support through the product identity factors.

The only direct project dependency is the definition **MvPolynomial.hasseCoeff**, both in the statement and its unfolded proof. There is no dependency on another project theorem. Existing library support includes Finsupp.mul_prod_erase′, Finsupp.prod_congr, Finsupp.support_erase and Finsupp.single_eq_of_ne, with ordinary choose/addition simplification. [Exact source searches](../evidence/MvPolynomial.hasseCoeff_single_add_eq/source-search.json) document those primitives. Their successful use is native verified; these observations are not an exhaustive public search establishing absence of another general factorization theorem.

## All explicit callers and duplication review

One explicit invocation, inside private `MvPolynomial.coeff_taylor_monomial_single_add_aux` (declared Taylor101), occurs at **Taylor117**. After coefficient separation and a univariate binomial-coefficient computation, this helper factors the multivariate Hasse coefficient into the same two terms as the induction step. [Caller excerpt](../evidence/MvPolynomial.hasseCoeff_single_add_eq/caller-excerpt.lean.txt) and the word-boundary grep distinguish the declaration from its use. No explicit outside-file caller was found. This is a source-level audit, not an opaque kernel or simp dependency closure.

The more general scalar cocycle and successor identities in HasseDeriv concern products of binomial coefficients at shifted derivative indices. This helper instead separates one coordinate of a single binomial product. They are related combinatorics but not duplicated statement/proof implementations. In this module one implementation supplies the induction caller; one use alone does not imply junk.

## Applicable overview assessment

**Mathlib API:** existing finite-product erasure and support-congruence primitives express the proof. The project hasseCoeff definition supplies the binomial-product representation. This private assessment does not inherit the parent's public verdict or assert a new public contribution.

**Generality:** arbitrary variable type and natural finitely supported indices already suffice. The actual native type confirms the ambient R instance is absent. hi is used to identify the selected upper binomial index; no weakening of it is claimed, and no new hypothesis or representation is introduced. Erasure preserves the meaning of the remaining factors, including zero cases.

**Missing API:** no missing primitive blocks the current short proof. Whether a generic product-factorization or public binomial API should replace this spelling would require its own public assessment, excluded here by the private rule.

**Naming, documentation and junk:** retain unchanged as a private helper. The name describes splitting hasseCoeff on a single-coordinate addition, and hi makes the precise role clear. It keeps the scalar identity out of the longer polynomial coefficient proof. Public export/docstring, renaming or inlining is unnecessary for the current role. No sorry, new axiom, resource-limit option, TODO or long proof is present.

## Native proof and direct-dependent checks

Native Lean accepted the exact original body renamed `MvPolynomial.PrivateSingleCoeffAssessment.replay`; only the declaration name changed, avoiding generated kernel names for private constants. [Complete receipt](../evidence/MvPolynomial.hasseCoeff_single_add_eq/native-replay.json) includes its full type and standard-axiom output. [Exact executed source](../evidence/MvPolynomial.hasseCoeff_single_add_eq/executed.lean.txt) preserves the actual request path and entire persistent document.

The complete actual caller was also replayed as `...caller`, replacing the scalar helper with this fresh replay. Its coefficient-extraction dependency uses the independently accepted private replay from canonical58, and its power-product dependency uses the unchanged accepted scratch helper from the earlier taylor_X check. These are private-name substitutions, not new mathematical premises or library building blocks. The remaining caller statement/proof is preserved. This is a full direct-caller experiment, not a claim that the production module was migrated.

Final diagnostics are complete, success=true, partial=false, no errors/warnings or failed dependencies. Both new target and caller use only propext, Classical.choice, Quot.sound. No sorry/admit, new axioms, unsafe/native_decide or raised limits are introduced. There are no rejected native attempts for this declaration.

All17 production sources/pins freshly match the clean full-build baseline: [baseline](../evidence/MvPolynomial.hasseCoeff_single_add_eq/baseline-build.txt), [baseline hashes](../evidence/MvPolynomial.hasseCoeff_single_add_eq/input-manifest.json), [fresh comparison](../evidence/MvPolynomial.hasseCoeff_single_add_eq/source-check.json). Production is unchanged, so the shared build validates existing dependents as well.

## Completion and next action

Keep the private helper. All required applicable checks are complete; nothing is deferred or blocked. Full public mathlibable phases are explicitly n/a, rather than marked completed without execution. This SKIP does not classify the future public coefficient theorem.

[Assessment](../evidence/MvPolynomial.hasseCoeff_single_add_eq/assessment.json), [verification](../evidence/MvPolynomial.hasseCoeff_single_add_eq/verification.json), [overview entry](../evidence/MvPolynomial.hasseCoeff_single_add_eq/overview-entry.json), [portable current-manifest validator](../evidence/MvPolynomial.hasseCoeff_single_add_eq/validate.py), [manifest](../evidence/MvPolynomial.hasseCoeff_single_add_eq/copy-manifest.json). Only after final acceptance will progress advance to private `MvPolynomial.prod_pow_single_add_tsub`.
