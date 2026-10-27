# Roth.coeff_prod_of_natDegree_le' — completed private-helper overview triage

**Verdict: SKIP — private declaration (overview Step 9a).** Applicable inventory, structural review, caller audit, native verification and evidence are complete. Full public mathlibable literature/search and contribution phases are n/a under the explicit private rule; none is falsely marked completed.

## Rule and inventory

The [installed rule](../evidence/Roth.coeff_prod_of_natDegree_le'/prefilter-rule.md) lists the private modifier. [Exact source/metadata](../evidence/Roth.coeff_prod_of_natDegree_le'/corrected-target.json) freshly match Roth/Wronskian.lean:93–103. The complete [module](../evidence/Roth.coeff_prod_of_natDegree_le'/source-wronskian.lean.txt) was read. Private source names have generated kernel names; this review verifies a public scratch replay instead of claiming lookup of the original private constant.

Full source interface:

~~~lean
{K : Type*} [Field K] {ι : Type*} (s : Finset ι) (f : ι → K[X]) (n : ι → ℕ) (h : ∀ i ∈ s, (f i).natDegree ≤ n i) : (∏ i ∈ s, f i).coeff (∑ i ∈ s, n i) = ∏ i ∈ s, (f i).coeff (n i)
~~~

For a finite polynomial product with an individual natural degree bound for each factor, the coefficient at the sum of those bounds is the product of the boundary coefficients. Bounds need not be attained: lower-degree factors contribute zero boundary coefficient. Empty products, zero factors and arbitrary ambient index types are included. No degree distinctness, positivity, characteristic or finite-ambient hypothesis occurs.

The [exact proof](../evidence/Roth.coeff_prod_of_natDegree_le'/target-excerpt.lean.txt) inducts on the finite set. The empty case simplifies; insertion uses the two-factor boundary coefficient identity, the degree bound on the remaining product, and the induction hypothesis.

## Dependencies and callers

No project declaration is used in the proof. Mathlib supplies Polynomial.coeff_mul_add_eq_of_natDegree_le, Polynomial.natDegree_prod_le, Finset.sum_le_sum and insertion/product/sum normalization.

There is exactly one executable invocation: Roth/Wronskian.lean:131, inside coeff_wronskian_of_natDegree_injective (declared122). It extracts the boundary coefficient in each permutation product of Hasse derivatives. [Caller excerpt](../evidence/Roth.coeff_prod_of_natDegree_le'/caller-excerpts.lean.txt) and [full searches](../evidence/Roth.coeff_prod_of_natDegree_le'/source-search.json) show the reference. There are no explicit outside-file calls. This is a source audit, not opaque kernel/simp dependency coverage.

## Applicable structural review

**Mathlib API/duplication:** public Polynomial.coeff_prod_of_natDegree_le at Algebra/Polynomial/BigOperators.lean:230 uses one common bound n and coefficient index s.card*n. This helper uses individual bounds n i and index ∑ i∈s,n i. The public common-bound theorem is related, not identical. [Pinned comparison](../evidence/Roth.coeff_prod_of_natDegree_le'/mathlib-comparison.lean.txt), [source hash](../evidence/Roth.coeff_prod_of_natDegree_le'/mathlib-source-hashes.json) and native signature check verify that distinction. No independently repeated same-interface project proof appeared in the bounded audit.

**Generality:** the unchanged induction body compiles over CommSemiring rather than Field. [Exact native replay](../evidence/Roth.coeff_prod_of_natDegree_le'/executed.lean.txt) and [receipt](../evidence/Roth.coeff_prod_of_natDegree_le'/native-replay.json) verify removal of inverse, additive-inverse, nontriviality and domain assumptions without changing the formula. Commutativity supports the finite-product interface. No explicit DecidableEq or Fintype is required; classical finite-set reasoning is internal to the proof. No maximality claim beyond this representation is made.

**Missing API:** the varying-bound form is a plausible future generalization of the public common-bound coefficient API. Private triage records that opportunity without claiming a full public upstream literature/search assessment or automatically exporting the helper.

**Junk/style/documentation:** retain the focused private induction helper. One actual coefficient-proof use justifies its local role. Its prime distinguishes the public common-bound name; any future export needs deliberate naming. No deletion, rename, export, statement or production edit is applied. The main public Wronskian coefficient theorem will receive its own full assessment.

## Verification

All 17 source/pin hashes freshly match the successful full build baseline (2467 jobs, exit0). Native Lean accepts PrivateCoeffProductAssessment.replay with the original proof body, a scratch public name and the genuinely weaker CommSemiring class. Full elaborated type and axioms were printed; the entire document has no errors, warnings, failed dependencies or partial elaboration, and only propext, Classical.choice and Quot.sound. No sorry/new axiom, unsafe/native_decide or resource-limit increase is used.

[Verification index](../evidence/Roth.coeff_prod_of_natDegree_le'/verification.json), [baseline](../evidence/Roth.coeff_prod_of_natDegree_le'/baseline-build.txt) and [fresh input hashes](../evidence/Roth.coeff_prod_of_natDegree_le'/source-check.json) preserve the audit. Archived .lean.txt bytes matched the actual .lake execution file before acceptance. Prior scratch proofs are context, not additional completed assessments. Production sources/pins remain unchanged.

## Completion and next action

Applicable inventory, API/duplication/generality/missing-API/junk review, source/caller audit, private prefilter, proof and evidence checks are complete. Full public mathlibable phases are n/a. SKIP does not assert that the generalized identity is useless or supply a public contribution verdict.

[Assessment](../evidence/Roth.coeff_prod_of_natDegree_le'/assessment.json), [overview entry](../evidence/Roth.coeff_prod_of_natDegree_le'/overview-entry.json), [current manifest](../evidence/Roth.coeff_prod_of_natDegree_le'/copy-manifest.json) and [portable validator](../evidence/Roth.coeff_prod_of_natDegree_le'/validate.py) record completion. Continue after acceptance/publication with Roth.sum_range_le_sum_of_injective, the first unfinished canonical declaration.
