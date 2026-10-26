# MvPolynomial.hasseCoeff_mul_succ — completed private-helper overview triage

**Verdict: SKIP — private declaration (overview Step 9a).** Applicable inventory, structural review, caller audit and proof verification are complete. The installed private prefilter excludes this helper from full public-declaration mathlibable assessment; no full literature/search phase is claimed complete.

## Scope and inventory

The [installed rule](../evidence/MvPolynomial.hasseCoeff_mul_succ/prefilter-rule.md) explicitly lists the private modifier. The source at `Roth/HasseDeriv.lean:191–195` is a private lemma. The [metadata and exact source](../evidence/MvPolynomial.hasseCoeff_mul_succ/corrected-target.json) have been freshly matched to the production file. Private logical source names receive generated kernel names; this assessment uses a scratch public replay rather than claiming a fresh lookup of the original private constant.

For arbitrary variable type σ, distinguished variable j and natural finitely supported indices d,e, the lemma proves:

```lean
hasseCoeff d (e + Finsupp.single j 1 + d) * (e j + 1) =
  (d j + 1) * hasseCoeff (d + Finsupp.single j 1) (e + Finsupp.single j 1 + d)
```

It is the single-coordinate successor case of the binomial cocycle. The actual replay type has only `{σ : Type*}`, j,d,e. There is no coefficient ring, variable finiteness, decidable equality, nonemptiness, dominance or positivity hypothesis. Its coordinate factors live in ℕ. Zero coordinates and zero indices are included.

The two tactic lines specialize `hasseCoeff_mul_hasseCoeff e (Finsupp.single j 1) d`, unfold the scalar product, and normalize addition/multiplication. This turns the one-coordinate choose factors into e j+1 and d j+1. The [exact source](../evidence/MvPolynomial.hasseCoeff_mul_succ/target-excerpt.lean.txt) and independent cocycle replay are retained.

## Dependencies and caller audit

Project dependencies are `MvPolynomial.hasseCoeff` and the private `MvPolynomial.hasseCoeff_mul_hasseCoeff`. Existing mathlib simplification supplies single-support products, natural choose normalization and commutative addition/multiplication. The broader cocycle uses `Nat.choose_mul`, `Finsupp.prod_of_support_subset` and finite-product congruence; it was assessed separately. This helper is not an independent new finite-product infrastructure proposal.

There is exactly one explicit executable source invocation: `MvPolynomial.pderiv_hasseDeriv`, declared at200, invokes this helper at `Roth/HasseDeriv.lean:205`. It reconciles the successor factor after coefficient comparison of ordinary partial differentiation with a Hasse derivative. [Caller excerpt](../evidence/MvPolynomial.hasseCoeff_mul_succ/caller-excerpts.lean.txt) and [untruncated searches](../evidence/MvPolynomial.hasseCoeff_mul_succ/source-search.json) show the declaration and single invocation. No explicit external production-file caller was found. This is a source audit, not a claim about opaque kernel/simp dependency closure.

## Applicable structural assessment

**Mathlib API:** the helper is a specialization of the already shared private cocycle. Existing `simpa` simplification and single-support finite-product API express the specialization; no extra generic mathlib API is required for this helper itself. The public partial/Hasse compatibility theorem requires its own full subsequent assessment.

**Duplication:** the shared general cocycle has two direct uses; this successor wrapper isolates its single-coordinate algebra for one coefficient proof. No duplicated independent successor proof was found by the source audit. A single use alone is not evidence that deletion improves the public theorem's proof.

**Generality:** the natural multi-index scalar identity is unrestricted in σ,j,d,e. The native replay verifies that no ambient CommSemiring binder was accidentally retained. An arbitrary cocycle formulation would assume the general scalar law rather than prove a stronger binomial fact. No unverified weakening is proposed.

**Missing API:** no missing generic support-product or simplification lemma blocks the two-line specialization. The public derivative law remains a separate assessment; this SKIP is not inherited as its verdict.

**Junk, naming and documentation:** retain the private helper in this read-only overview. Its name identifies the successor calculation and keeps scalar normalization out of the operator proof. A public docstring/export is unnecessary for its private role. Inlining could be revisited during a future authorized source refactor, but no deletion, rename or source modification is recommended here.

## Verification and evidence

All17 production-source/pin hashes freshly match the successful full `lake build` baseline (exit0,2467jobs). In addition, native Lean accepted `PrivateSuccessorAssessment.replay`, with the exact proof body apart from renaming the private dependency to its independently verified scratch replay. It reports the full type and only `propext`, `Classical.choice`, `Quot.sound`. The entire accepted scratch document has zero errors/warnings, complete elaboration and no failed dependencies. Earlier verification material in that document is context, not an extra claim of public assessment completion for this helper.

[Verification index](../evidence/MvPolynomial.hasseCoeff_mul_succ/verification.json), [raw native receipt](../evidence/MvPolynomial.hasseCoeff_mul_succ/native-replay.json), [exact executed source](../evidence/MvPolynomial.hasseCoeff_mul_succ/executed.lean.txt), [baseline](../evidence/MvPolynomial.hasseCoeff_mul_succ/baseline-build.txt), and [fresh hashes](../evidence/MvPolynomial.hasseCoeff_mul_succ/source-check.json) are preserved. Executed source bytes were matched to the live scratch file at assessment time. Archived `.lean.txt` files preserve exact content without adding workspace Lean modules; the native receipt records the original `.lean` execution path.

## Completion and action

Inventory, source/caller review, mathlib API/duplication/generality/missing-API/junk triage, private prefilter and proof/evidence checks are complete. Full public mathlibable literature, modern-idiom, five-method search and contribution verdict phases are n/a under the explicit rule. This SKIP does not assert that an equivalent public scalar identity could never be useful upstream.

[Assessment](../evidence/MvPolynomial.hasseCoeff_mul_succ/assessment.json), [overview entry](../evidence/MvPolynomial.hasseCoeff_mul_succ/overview-entry.json), [manifest](../evidence/MvPolynomial.hasseCoeff_mul_succ/copy-manifest.json) and [validator](../evidence/MvPolynomial.hasseCoeff_mul_succ/validate.py) supply the portable record. No assessment item or user input remains outstanding. After independent root acceptance and publication, continue with `MvPolynomial.pderiv_hasseDeriv` as the first unfinished canonical declaration.
