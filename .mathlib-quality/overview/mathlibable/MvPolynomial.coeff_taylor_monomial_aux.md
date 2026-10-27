# MvPolynomial.coeff_taylor_monomial_aux — completed private-helper overview triage

**SKIP — private declaration under overview Step 9a.** Applicable inventory, mathematical/structural review, caller audit, direct proof-dependency inspection and native target/dependent verification are complete. Full public literature/search/contribution phases are n/a under the [explicit private prefilter](../evidence/MvPolynomial.coeff_taylor_monomial_aux/prefilter-rule.md). This does not classify the next public coefficient theorem.

## Exact statement and mathematical role

Private lemma at `Roth/Taylor.lean:120–129`. [Canonical source](../evidence/MvPolynomial.coeff_taylor_monomial_aux/corrected-target.json), [exact excerpt](../evidence/MvPolynomial.coeff_taylor_monomial_aux/target-excerpt.lean.txt), [entire declaring module](../evidence/MvPolynomial.coeff_taylor_monomial_aux/Taylor-module.lean.txt). Fresh native replay type:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) (d k : σ →₀ ℕ) (a : R),
  ((taylor α) ((monomial k) a)).coeff d = (eval α) ((hasseDeriv d) ((monomial k) a))
```

The coefficient at d of a translated monomial aX^k equals its d-th Hasse derivative evaluated at α. This proves the monomial case of coefficient-form Taylor expansion. It is stronger than merely writing the translated monomial as a product of shifted variables, because it identifies each coefficient with the appropriate evaluated derivative.

σ is any variable type; R any commutative semiring; α any translation; d and k any natural finitely supported multi-indices; a any coefficient. No Fintype, external decidable equality, degree bound, support independence, nonzero coefficient, field/domain or characteristic assumption occurs. Unlike the preceding induction-step helper, its final statement has no induction hypothesis or selected-coordinate premise. No weakening is proposed by invoking the later public theorem; that would obscure this helper's independent inductive proof.

## Argument and project dependencies

Induct on the finite support/exponents of k using Finsupp.induction, generalizing the target coefficient d. For k=0 the monomial is constant. Split d=0 from d≠0; generic algebra-hom scalar preservation and Hasse derivative rules give the required constant or zero. For a new coordinate power, the induction supplies the residual identity and the support condition needed by the separately checked single_add induction step.

Explicit project references are taylor and hasseDeriv in the statement, hasseDeriv_C in the base proof, and private coeff_taylor_monomial_single_add_aux in the induction case. Direct **elaborated proof-expression** inspection additionally identifies MvPolynomial.hasseDeriv_zero, used by simplification. The complete direct project dependency list is:

- MvPolynomial.taylor, MvPolynomial.hasseDeriv.
- MvPolynomial.hasseDeriv_zero, MvPolynomial.hasseDeriv_C.
- Private MvPolynomial.coeff_taylor_monomial_single_add_aux (mapped from its accepted scratch replay).

The constant cases actually use existing **MvPolynomial.algHom_C**, not the local taylor_C alias, as confirmed by the proof-expression constants. Existing library support includes Finsupp.induction, support-not-membership conversion, constant coefficient/evaluation formulas, equality cases and zero preservation. [Direct dependency audit](../evidence/MvPolynomial.coeff_taylor_monomial_aux/kernel-direct-project-dependencies.json), [source searches](../evidence/MvPolynomial.coeff_taylor_monomial_aux/source-search.json). The audit enumerates direct proof-expression constants including their type infrastructure; it does not claim transitive opaque/kernel closure. No public mathematical absence verdict follows from this inspection.

## Caller and duplication assessment

Exactly one explicit source invocation: public `MvPolynomial.coeff_taylor`, declared Taylor134, uses the monomial lemma at **Taylor138** in its monomial case. [Caller excerpt](../evidence/MvPolynomial.coeff_taylor_monomial_aux/caller-excerpt.lean.txt) and exact word-boundary source search. No explicit outside-file invocation found; source references are distinct from implicit simplifier or opaque dependencies.

This helper establishes the coefficient identity for one monomial; the public caller extends it by additivity to every polynomial. The previous single_add helper proves an induction case with an induction hypothesis. Generic aeval_monomial gives an image-product expression rather than the coefficient/derivative identity. These are different proof layers, not duplicate full implementations. One direct caller is appropriate for a private monomial-case boundary.

## Applicable structural review

**API and missing API:** existing Finsupp induction and constant normalization combine with the separately verified project induction step. No missing generic primitive blocks this decomposition. A public multivariate Hasse/Taylor API is assessed separately at coeff_taylor; private SKIP does not decide its worth.

**Generality:** the native full type confirms arbitrary variables and commutative-semiring coefficients with no support/degree/characteristic/nonzero restrictions or accidentally retained finiteness instances. No stronger generalization or assumption drop was claimed. Exponent induction removes the selected-coordinate hypothesis from the final result.

**Naming/documentation/junk:** keep unchanged as a private auxiliary theorem. Its monomial scope cleanly separates exponent induction from the public linearity proof. Public docstring/export, rename or inlining is unnecessary here. There is no sorry, new axiom, resource-limit raise, TODO or proof over30 lines in the declaration.

## Native target and full public-caller verification

The exact source body is replayed as `MvPolynomial.PrivateTaylorMonomialAssessment.replay`, replacing only the private induction-step identifier with its independently verified canonical61 scratch proof. [Complete accepted receipt](../evidence/MvPolynomial.coeff_taylor_monomial_aux/native-replay.json), [exact executed document](../evidence/MvPolynomial.coeff_taylor_monomial_aux/executed.lean.txt). Private kernel names were not guessed.

The complete public coeff_taylor proof is replayed as `...caller`: polynomial additivity in the add case, and this new monomial replay in the monomial case. This verifies the actual direct dependent proof while keeping the production module unchanged. Direct expression inspection confirms the new monomial proof contains no reference to the later public coeff_taylor, so its verification does not derive the special case circularly from the imported general theorem.

Final diagnostics are complete success, partial=false, no errors/warnings, interpreter panic, dummy result or failed dependencies. Target and public caller have only propext, Classical.choice, Quot.sound. No sorry/admit, new axioms, unsafe/native_decide, or raised limits are introduced. An optional dependency-inspection attempt initially omitted allowOpaque=true when reading a theorem value, causing an interpreter panic and dummy inspection result despite a success flag. That [rejected receipt](../evidence/MvPolynomial.coeff_taylor_monomial_aux/meta-rejected.json) is separately preserved and not accepted evidence. The corrected inspection explicitly allows opaque theorem values and returns the actual constants in the accepted receipt; the mathematical proofs themselves did not change.

All17 production source/pin hashes freshly match the clean 2467-job full build: [baseline](../evidence/MvPolynomial.coeff_taylor_monomial_aux/baseline-build.txt), [manifest](../evidence/MvPolynomial.coeff_taylor_monomial_aux/input-manifest.json), [fresh comparison](../evidence/MvPolynomial.coeff_taylor_monomial_aux/source-check.json). Production and versions remain unchanged, so existing dependents remain covered by the shared build. [Verification index](../evidence/MvPolynomial.coeff_taylor_monomial_aux/verification.json).

## Completion and next declaration

Keep the private monomial theorem unchanged. All applicable inventory/API/duplication/generality/missing-API/junk/caller/private-rule/native/evidence checks are complete. Public contribution phases are explicitly n/a; none was marked complete without execution. No item is blocked or deferred.

[Assessment](../evidence/MvPolynomial.coeff_taylor_monomial_aux/assessment.json), [overview entry](../evidence/MvPolynomial.coeff_taylor_monomial_aux/overview-entry.json), [portable current-manifest validator](../evidence/MvPolynomial.coeff_taylor_monomial_aux/validate.py), [manifest](../evidence/MvPolynomial.coeff_taylor_monomial_aux/copy-manifest.json). After acceptance and publication, continue with full public assessment of **MvPolynomial.coeff_taylor**.
