# MvPolynomial.prod_pow_single_add_tsub — completed private-helper overview triage

**SKIP — private declaration under overview Step 9a.** All applicable inventory, structural review, caller audit and native verification are complete, including a verified generalization to **CommMonoid**. The [explicit private prefilter](../evidence/MvPolynomial.prod_pow_single_add_tsub/prefilter-rule.md) makes the full public literature/search/contribution workflow n/a. No public upstream inclusion or absence verdict is inferred.

## Exact source, type and meaning

Private lemma at `Roth/Taylor.lean:92–99`. [Canonical source](../evidence/MvPolynomial.prod_pow_single_add_tsub/corrected-target.json), [exact excerpt](../evidence/MvPolynomial.prod_pow_single_add_tsub/target-excerpt.lean.txt), [entire declaring module](../evidence/MvPolynomial.prod_pow_single_add_tsub/Taylor-module.lean.txt). The fresh native original replay type is:

```lean
∀ {σ : Type u_3} {R : Type u_4} [inst : CommSemiring R] (α : σ → R) {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 →
    ∀ (d : σ →₀ ℕ),
      ((Finsupp.single i n + k' - d).prod fun j e ↦ α j ^ e) =
        α i ^ (n - d i) * (k' - Finsupp.erase i d).prod fun j e ↦ α j ^ e
```

Take a single-coordinate exponent n at i plus a residual exponent k′ that is zero at i. After subtracting a multi-index d with natural truncated subtraction, the power-product evaluation factors into α_i^(n-d_i) and the product on k′ minus d with coordinate i erased. The statement does not assume d lies below the starting exponent; truncated subtraction handles all cases.

σ is arbitrary; α supplies scalar values, i/n select the coordinate and exponent, k′ supplies the complementary support, hi gives k′_i=0, d selects the exponent subtraction. No finiteness instance, external decidable equality, nonzero coordinate/value, field, characteristic, order or dominance premise is needed. The original CommSemiring instance is broader than the proof requires, as tested below.

## Proof and direct project dependencies

First prove the equality of natural exponent vectors by coordinate extensionality. At i use hi and erasure; at j≠i the single-coordinate term vanishes and erase agrees with d. Rewrite by that equality, then use Finsupp.prod_add_index′ and pow_add to split a power product across the sum of exponent vectors. Empty factors and exponent zero contribute one.

There are **no direct project dependencies** in this scalar helper. It uses ordinary Finsupp finite products, erasure, single-coordinate support identities and the natural power-addition law. The source searches preserve the actual library primitives. These observations establish how this proof works; they do not stand in for a public exhaustive contribution search.

## Callers and duplication

Exactly one explicit source invocation, Taylor117, occurs inside private `coeff_taylor_monomial_single_add_aux` (declared Taylor101). It reconciles the scalar powers after separating the selected variable and using the induction hypothesis. [Word-boundary source searches](../evidence/MvPolynomial.prod_pow_single_add_tsub/source-search.json), [caller excerpt](../evidence/MvPolynomial.prod_pow_single_add_tsub/caller-excerpt.lean.txt). No explicit outside-file caller was found; this is a source audit, not an opaque kernel/simp dependency closure.

The neighboring hasseCoeff_single_add_eq splits the **binomial scalar**, while this helper splits the **evaluation power product** after truncated subtraction. They are distinct parts of the induction calculation. No second exact implementation was found in this module. Keeping this small boundary isolates exponent bookkeeping from polynomial coefficients; one caller does not make it junk.

## Applicable structural review and verified generality

Existing mathlib product/erase/power primitives suffice; no missing normalization helper blocks the proof. The theorem is private, so export design, full literature/formal search and a public mathlibable verdict are unassessed rather than silently marked complete.

The proof uses no addition, zero, distributivity or coefficient-semiring structure on α's values. Native Lean accepted its **same body** under only `[CommMonoid M]`. Full expanded type:

```lean
∀ {σ : Type u_1} {M : Type u_2} [inst : CommMonoid M] (α : σ → M) {i : σ} {n : ℕ} {k' : σ →₀ ℕ},
  k' i = 0 →
    ∀ (d : σ →₀ ℕ),
      ((Finsupp.single i n + k' - d).prod fun j e ↦ α j ^ e) =
        α i ^ (n - d i) * (k' - Finsupp.erase i d).prod fun j e ↦ α j ^ e
```

[Generalization source](../evidence/MvPolynomial.prod_pow_single_add_tsub/general-executed.lean.txt), [complete clean receipt](../evidence/MvPolynomial.prod_pow_single_add_tsub/general-native.json). This is an actual checked weakening, not a conjectured abstraction. The source semiring provides such a monoid, so the original is a specialization; no stronger mathematical premise was introduced. No weakening of hi, change of exponent object, arbitrary noncommutative unordered product or group/negative-exponent law is claimed.

Recommendation: retain the private helper and record the CommMonoid weakening as a future source-refactor opportunity. The current read-only overview keeps its production signature and proof unchanged. A full public generic power-product contribution assessment would be a separate task; this private SKIP does not assert that such an API is absent from mathlib.

Naming describes single-coordinate addition and truncated subtraction. No public docstring/export, rename or inlining is needed for the present role. The source contains no sorry, new axiom, limit raise, TODO or long proof. The helper remains useful even though its scalar assumptions can be improved.

## Native target and direct-dependent verification

The exact original proof is replayed as `MvPolynomial.PrivatePowerProdAssessment.replay`, changing only the private declaration name. [Native target/caller receipt](../evidence/MvPolynomial.prod_pow_single_add_tsub/native-replay.json), [exact executed document](../evidence/MvPolynomial.prod_pow_single_add_tsub/executed.lean.txt). Private source names have generated kernel names, so this is an exact source replay, not a guessed original-private lookup.

The full actual direct caller is also replayed with this fresh target, using the separately accepted coefficient-extraction and scalar-binomial private replays from canonical58/59 for its other dependencies. Only these private identifiers and line wrapping change; mathematical statement and remaining proof are preserved. This verifies the direct dependent proof, not a whole-module production migration and not a claim that the caller was rewritten to the generalized CommMonoid API.

Both target/caller and the additional generalized theorem elaborate completely, no errors/warnings or failed dependencies, only propext, Classical.choice, Quot.sound. No sorry/admit, new axioms, unsafe/native_decide, or resource raises are introduced. There are no rejected native attempts for this declaration. [Verification index](../evidence/MvPolynomial.prod_pow_single_add_tsub/verification.json) retains both native sources and hashes.

All17 source/pin hashes freshly match the successful 2467-job full build: [baseline](../evidence/MvPolynomial.prod_pow_single_add_tsub/baseline-build.txt), [manifest](../evidence/MvPolynomial.prod_pow_single_add_tsub/input-manifest.json), [fresh comparison](../evidence/MvPolynomial.prod_pow_single_add_tsub/source-check.json). Production is unchanged, so existing dependents remain covered by the shared build. No Lean/mathlib versions changed.

## Completion and next step

All applicable inventory, API, duplication, generality, missing-API, junk, caller, private-rule and proof/evidence checks are complete. Nothing is deferred or blocked; the verified monoid weakening is an overview finding, not an unfinished assessment. Full public mathlibable phases are explicitly n/a under the private rule.

[Assessment](../evidence/MvPolynomial.prod_pow_single_add_tsub/assessment.json), [overview entry](../evidence/MvPolynomial.prod_pow_single_add_tsub/overview-entry.json), [portable validator](../evidence/MvPolynomial.prod_pow_single_add_tsub/validate.py), [current manifest](../evidence/MvPolynomial.prod_pow_single_add_tsub/copy-manifest.json). After acceptance and publication, continue with private `MvPolynomial.coeff_taylor_monomial_single_add_aux`.
