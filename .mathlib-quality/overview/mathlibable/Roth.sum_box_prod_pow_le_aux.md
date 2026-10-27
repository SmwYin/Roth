# Roth.sum_box_prod_pow_le_aux — completed private-helper assessment (97/293)

**SKIP under the explicit B1 private-declaration prefilter.** All applicable inventory, mathematical/structural review, caller audit and native verification are complete. Full public literature/search/contribution phases are not applicable and were not executed. This does not decide the next public theorem's upstream worth. [Exact rule](../evidence/Roth.sum_box_prod_pow_le_aux/prefilter-rule.md), [provenance](../evidence/Roth.sum_box_prod_pow_le_aux/prefilter-provenance.json).

## Statement and mathematical role

Private theorem at `Roth/CoeffNorm.lean:214–218`, also ending in `_aux`. The finite sum of B times products of absolute coordinate powers over a rectangular exponent box is at most B times the corresponding product of binomial powers. The exact original private kernel type is printed in the native receipt:

```lean
∀ {σ : Type u_1} [inst : Fintype σ] (r : σ → ℕ) {B : ℝ},
  0 ≤ B → ∀ (x : σ → ℝ), ∑ k ∈ box r, B * ∏ j, |x j| ^ k j ≤ B * ∏ j, (1 + |x j|) ^ r j
```

The variable type is arbitrary with a Fintype enumeration. The bounds r are natural numbers, B is a nonnegative real common factor, and x is any real-valued coordinate tuple. The type has no external DecidableEq, nonzero-polynomial, finite-support-independent or characteristic premise. No weakening is claimed. Nonnegativity of B permits the final scalar multiplication; each |x j| supplies the scalar geometric bound's nonnegativity hypothesis. Empty coordinate families and zero bounds remain included.

[Canonical entry](../evidence/Roth.sum_box_prod_pow_le_aux/canonical-entry.json), [exact target and metadata](../evidence/Roth.sum_box_prod_pow_le_aux/target-metadata.json), [target excerpt](../evidence/Roth.sum_box_prod_pow_le_aux/target-excerpt.lean.txt), [complete declaring module](../evidence/Roth.sum_box_prod_pow_le_aux/source-module.lean.txt), [native type](../evidence/Roth.sum_box_prod_pow_le_aux/native-type.json).

## Proof, API and dependencies

Factor the Cartesian-box sum as a product of finite coordinate sums using `Finset.prod_univ_sum`, pull out B, apply `geom_sum_le_one_add_pow` in each coordinate, and use `Finset.prod_le_prod₀` plus multiplication by nonnegative B. Explicit project dependencies are `Roth.box` and `Roth.geom_sum_le_one_add_pow`; the latter's independent complete assessment is canonical96. Standard finite-sum/product and order primitives supply the remaining proof. No new primitive or instance is needed for this private decomposition.

This is distinct from the one-dimensional geometric inequality and from the public polynomial evaluation theorem: it handles the intervening rectangular product calculation. It is an appropriate four-line implementation boundary, with no duplicate full derivation found in the inspected module. Retain the private name and proof. There is no sorry, new axiom, unsafe/native decision, TODO or resource-limit increase. Full public naming/generalisation/contribution/literature searches are not silently claimed complete; they are n/a by the documented prefilter.

## Full caller and canonical dependency audit

There is exactly one explicit source caller: `Roth.abs_eval_le`, defined at CoeffNorm223 and using the helper at239. It enlarges polynomial support to the box and then applies this estimate. [Source search](../evidence/Roth.sum_box_prod_pow_le_aux/source-search.json), [whole caller source and metadata](../evidence/Roth.sum_box_prod_pow_le_aux/caller-metadata.json), [caller excerpt](../evidence/Roth.sum_box_prod_pow_le_aux/caller-excerpt.lean.txt).

The fresh runtime audit enumerates exactly293 canonical names in tracked order, all293 unique, present and with values; private names use Lean.mkPrivateNameCore. Its sole direct proof consumer is Roth.abs_eval_le. This is direct expression-constant inspection, not transitive kernel/simp closure. [Exact ordered snapshot](../evidence/Roth.sum_box_prod_pow_le_aux/canonical-snapshot.json), [generated array](../evidence/Roth.sum_box_prod_pow_le_aux/canonical-array.lean.txt).

## Native target and entire dependent verification

The exact target source is replayed as `MvPolynomial.PrivateBoxAssessment.replay`, changing only declaration privacy/name; no mathematical proof step is replaced. The entire public abs_eval_le proof is replayed as `...caller`, changing its declaration name and replacing the private call by the fresh replay. The new proof does not invoke the imported original private theorem or the later public abs_eval_le. No private kernel name was guessed: Lean.mkPrivateNameCore resolves the actual original for its kernel type and dependency audit.

[Exact executed snippet](../evidence/Roth.sum_box_prod_pow_le_aux/executed.lean.txt), [full raw native receipt](../evidence/Roth.sum_box_prod_pow_le_aux/native-receipt.json), [verification ledger](../evidence/Roth.sum_box_prod_pow_le_aux/verification.json). The original private and fresh replay types agree up to universe-parameter naming. The target replay and full caller have only propext, Classical.choice and Quot.sound. Diagnostics are complete success, partial=false, no error/warning, failed dependency, recovered sorryAx or interpreter panic. No rejected native attempt was accepted; a line-length preflight was corrected before execution.

All17 source/pin hashes freshly match the shared clean2467-job build: [fresh checks](../evidence/Roth.sum_box_prod_pow_le_aux/inputs.json), [baseline manifest](../evidence/Roth.sum_box_prod_pow_le_aux/input-manifest.json), [build receipt](../evidence/Roth.sum_box_prod_pow_le_aux/baseline-build.txt). Production Lean and versions remain unchanged, so the build baseline remains applicable.

## Completion and next declaration

Keep the helper unchanged. All applicable private assessment, structural review, exact type/proof/caller verification, provenance and evidence checks are complete; public mathlibable phases are explicitly n/a. No verification item is blocked or deferred. After acceptance and publication, continue with **Roth.abs_eval_le** (canonical98).

[Assessment](../evidence/Roth.sum_box_prod_pow_le_aux/assessment.json), [overview entry](../evidence/Roth.sum_box_prod_pow_le_aux/overview-entry.json), [portable validator](../evidence/Roth.sum_box_prod_pow_le_aux/validate.py), [current copy manifest](../evidence/Roth.sum_box_prod_pow_le_aux/copy-manifest.json). Root acceptance is recorded separately after final review.
