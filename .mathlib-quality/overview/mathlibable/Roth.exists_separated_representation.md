# Roth.exists_separated_representation

## Phase 0 — Baseline and provenance

Public canonical declaration168 is at Roth/Separation.lean:325. All17 source/pin SHA256 values freshly match the reusable successful baseline: lake build,2467 jobs, exit0, no errors or warnings. The whole declaring module and sole caller were read. [inputs.json](../evidence/Roth.exists_separated_representation/inputs.json), [baseline-build.txt](../evidence/Roth.exists_separated_representation/baseline-build.txt).

Original native full type, kernel body and standard axioms pass. The explicit function-binder printer preserves both φ/ψ types; the kernel body has no elision. Exact293 ordered unique canonical names have kernel values. Direct kernel-value consumers are audited separately from source references and transitive/simp dependency closure.

## Phase 1 — Mathematical content and full statement

For a field K and arbitrary variable type τ, a nonzero polynomial P of degree at most n in the distinguished variable has a separated sum with length1≤l≤n+1. Both univariate and remaining-variable families are linearly independent. The univariate degrees are at most n; every other-variable degree is bounded by the corresponding degree of P.

The proof takes a basis of the finite span of coefficient polynomials, forms coordinate polynomials in the distinguished variable, proves their independence, and reconstructs P. The three private helpers contain genuine mathematics and are not existing mathlib calls.

```lean
∀ {τ : Type u_1} {K : Type u_2} [inst : Field K] {P : MvPolynomial (Option τ) K},
  P ≠ 0 →
    ∀ {n : ℕ},
      MvPolynomial.degreeOf none P ≤ n →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ n + 1 ∧
              ∃ (φ : Fin l → Polynomial K) (ψ : Fin l → MvPolynomial τ K),
                LinearIndependent K φ ∧
                  LinearIndependent K ψ ∧
                    (∀ (ν : Fin l), (φ ν).natDegree ≤ n) ∧
                      (∀ (ν : Fin l) (j : τ), MvPolynomial.degreeOf j (ψ ν) ≤ MvPolynomial.degreeOf (some j) P) ∧
                        P =
                          ∑ ν : Fin l, (Polynomial.aeval (MvPolynomial.X none)) (φ ν) * (MvPolynomial.rename some) (ψ ν)
```

τ is arbitrary, K supplies scalars, P is the polynomial, hP is nonvanishing, n is the supplied upper bound and hn certifies it. Actual native type omits Fintype/DecidableEq τ. [native-type.json](../evidence/Roth.exists_separated_representation/native-type.json), [target-excerpt.lean.txt](../evidence/Roth.exists_separated_representation/target-excerpt.lean.txt).

## Phase 2 — Preliminary classification

BIG: listed among the module's main results. One-line definition test n/a: theorem with substantial finite-basis construction.

## Phase 3 — Exhaustive literature

| Channel | Artifact | Finding |
|---|---|---|
|General current|web-current.json|Separated-polynomial wording returns adjacent material, no exact bounded theorem located.|
|General standard|web-general.json|Two-factor tensor rank is linear-map/matrix rank.|
|General modern|web-modern.json|Full rank factorization gives the finite-matrix formulation.|
|ChatGPT math|literature-availability.json|Unavailable: no callable math-advice tool.|
|Local clean.tex|clean-excerpt.tex.txt|§2 proof of Lemma2, lines355–434: minimal separated representation has both LI families; implementation chooses coefficient-span basis.|
|nLab|nlab.json/primary-nlab.json|Actual mathematical query; direct XHTML fetch unsupported, not absence evidence.|
|nCatLab|ncatlab.json|Distinct /ncatlab namespace query returns /nlab material; no exact in-namespace hit claimed.|
|Stacks|stacks.json/primary-stacks.json|Tag00CV gives universal tensor-product construction, not bounded simultaneous-LI decomposition.|
|MathOverflow|mathoverflow.json|Rank-two matrix decomposition discussions are adjacent context.|
|Recent arXiv|arxiv.json/primary-arxiv.json|Actual five-year query; Yang2024 finite-field tensor decomposition is recent adjacent primary literature.|

Each web record preserves exact request, returned-response SHA256/bytes/status, titles/locators and concise original summary; no returned full bodies archived. [literature-individual.json](../evidence/Roth.exists_separated_representation/literature-individual.json).

Primary standard reference: [Draisma, Multilinear Algebra and Applications](https://math-unibe.ch/jdraisma/publications/mlappl.pdf), §5.4 definition5.4.51 and §6.2 definition6.2.55, PDF pp39/41: two-factor tensor rank equals the associated linear-map/coefficient-matrix rank. This explains the abstract decomposition but does not supply polynomial degree transports. [primary-draisma-locator.json](../evidence/Roth.exists_separated_representation/primary-draisma-locator.json).

The scalar generalization has independent primary support: [Stacks §15.22, Lemma15.22.11(3)](https://stacks.math.columbia.edu/tag/0549) proves finite torsion-free modules over a PID finite free. A finite coefficient span is torsion-free as a polynomial submodule. Its application to the full separated-polynomial theorem is an inference, not a claim that Stacks literally states our degree theorem. [primary-pid.json](../evidence/Roth.exists_separated_representation/primary-pid.json).

## Phase 4a — Parameter and mathematical audit

| Binder/property | Analysis |
|---|---|
|τ : Type*|Already arbitrary, including infinite or empty types; no finite-variable assumption needed.|
|K, Field K|Supplies ring structure and finite free coefficient span; generic finite-module/PID API is investigated.|
|P|Arbitrary finite-support polynomial.|
|hP : P≠0|Produces positive span rank. At n=0, zero cannot have a length≥1 separated sum with both LI families; actual guard preserves separated equality.|
|n : ℕ|Polynomial exponent/degree bound; actual degree specialization verified.|
|hn|Needed for length and φ-degree bounds; X_none has degree1 and fails the n=0 premise.|
|Both LI families|Must both survive generalization. Pointwise nonzero is insufficient.|
|Both degree families|Must survive tensor/matrix transport. A bare pure-tensor expansion loses these claims.|
|Fintype/DecidableEq τ|Already omitted, not a new weakening.|

## Phase 4b — Verified generality

Full project-context replay uses all three actual private constants via a term elaborator returning their existing kernel constants. No new axioms. A full arbitraryVariables corollary takes n=degreeOf none P. The CommRing representationOfBasis theorem preserves both LI families, both degree bounds and reconstruction given a bounded finite basis and length bounds; this conditional result is not called an unconditional scalar weakening.

The strongest independent evidence is the complete **mathlib-only unconditional PID theorem**. It imports the stable10 modules plus the genuine FreeModule.PID module, guards Roth.exists_separated_representation as unavailable, and replays all coefficient, basis, independence, degree and reconstruction mathematics in namespace Separated168PIDIsolated. Despite its historical helper name freeSpanRepresentation, the executed full theorem has no Module.Free premise: only CommRing+IsDomain+IsPrincipalIdealRing. Native diagnostics are complete and clean, with standard axioms. [separated-repr-isolated-pid-executed.lean.txt](../evidence/Roth.exists_separated_representation/separated-repr-isolated-pid-executed.lean.txt), [separated-repr-isolated-pid-receipt.json](../evidence/Roth.exists_separated_representation/separated-repr-isolated-pid-receipt.json).

The complete theorem is also verified in project context over CommRing K + IsDomain K + IsPrincipalIdealRing K, retaining arbitrary τ, P≠0, chosen n, hn, length bounds, both LI families, all degree bounds and reconstruction. The sole proof-infrastructure change is FiniteDimensional.span_of_finite to Module.Finite.span_of_finite; the actual generic PID instance supplies Module.Free for the torsion-free finite coefficient span. Native PID proof is complete, error/warning-free, partial=false, with standard axioms. An initial missing-import attempt failed at Module.Free K V and recovered sorryAx; it is rejected evidence only. Importing Mathlib.LinearAlgebra.FreeModule.PID resolved this without changing the mathematical proof.

This is a genuine scalar weakening, not merely an explicit-basis reformulation. It covers ℤ and every PID, while every field supplies the new instances. We do not claim PID is the weakest possible scalar condition. [separated-repr-pid-with-import-executed.lean.txt](../evidence/Roth.exists_separated_representation/separated-repr-pid-with-import-executed.lean.txt), [separated-repr-pid-with-import-receipt.json](../evidence/Roth.exists_separated_representation/separated-repr-pid-with-import-receipt.json).

## Phase 4c — Nine modern-idiom rows

| # | Check | Result |
|---|---|---|
|1|Typeclasses|Already uses Field; PID/free-span hypotheses expose scalar structure.|
|2|Filters/nets|No topology.|
|3|Universal property|Tensor-product universal property identifies separated multiplication; does not choose minimal independent factors.|
|4|Bundled substructures|Already Submodule.span, Module.Basis and support-box submodule.|
|5|Vector spaces to modules|Yes: finite torsion-free PID modules and ring-generic given-basis reconstruction. Full statements tested.|
|6|Higher categories|No applicable categorical law.|
|7|Concrete index|Fin l expresses finite rank and ℕ polynomial exponents. Arbitrary finite reindexing is equivalent, not a stronger theorem.|
|8|Concrete-via-abstract diagnostic|Yes algebraically: after coefficient expansion, only the finite coefficient family, spanning basis and support bounds remain; no arithmetic property of P. Abstract two-module decomposition could support additional consumers.|
|9|False-generalization guard|Retain two-factor decomposition, both LI families and all degree constraints. Higher-order tensor rank or an arbitrary finite sum changes the claim. Nonzero/cancellation/degree/zero guards are explicit.|

Genuine modern alternatives: polynomial Q over MvPolynomial coefficients via optionEquivLeft; tensor in bounded-degree univariate module tensor the multivariate support-box submodule; finite coefficient matrix and full rank factorization. Equivalence requires injective reconstruction and degree-preserving transports. Existing tensor finite-sum API lacks both LI claims. Existing square matrix rank normal form requires finite coefficient-support encoding, factor translation and bound recovery. No cosmetic category upgrade is proposed.

## Phase 4.5 — Infrastructure risk

n/a — declaration kind is theorem. Typeclass diamond, reducibility leak, noncanonical unfolding, instance priority collision, universe-polymorphism infrastructure and coercion ambiguity are all definition-only checks here. This theorem introduces no type, instances, operations, coercions, quotient or foundational definition. A proposed leaf module avoids strengthening foundational polynomial imports.

## Phase 4.6 — Five proof-strategy rows

| # | Check | Result |
|---|---|---|
|1|Topology ε–δ/filter|n/a finite algebra.|
|2|Element/submodule argument|Already span, support-box inclusion and basis; idiomatic.|
|3|Sequence/net|n/a no convergence.|
|4|Construction/universal property|Universal tensor property alone does not establish both LI families; minimal decomposition still requires linear algebra.|
|5|Missing helpers|Coordinate-polynomial independence and basis reconstruction are genuine finite-coordinate arguments; generic minimal two-factor decomposition is a possible abstract API, not an existing replacement.|

Basis strategy is MATHLIB-IDIOMATIC. Scalar infrastructure should use generic finite/free modules. No proof-refactor cost determines the verdict.

## Phase 5 — Actual five-method search

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
|Current full bounded polynomial|formal-finder-current.json|loogle-current.json|leansearch-current.json|rg-current.json|local-current.json|
|Literature two-factor tensor rank|finder-literature.json|loogle-literature.json|leansearch-literature.json|rg-literature.json|local-literature.json|
|Modern matrix rank factorization|finder-modern.json|loogle-modern.json|leansearch-modern.json|rg-modern.json|local-modern.json|

All15 cells executed. Five supplementary PID cells locate Module.free_of_finite_type_torsion_free'. Local fallback reports index unavailable even when results return; neither this nor unsuccessful external searches proves absence. Pin signatures are independently read/checked. [formal-search.json](../evidence/Roth.exists_separated_representation/formal-search.json), [rg-pid.json](../evidence/Roth.exists_separated_representation/rg-pid.json).

TensorProduct.exists_sum_tmul_eq/exists_finset give finite sums only. TensorProduct.eq_repr_basis_left/right reconstruct along a supplied basis, without opposite independence or polynomial degree bounds. Matrix.exists_rank_normal_form gives square-matrix normal form, not the target polynomial theorem. Module.finBasis, finrank_range_le_card, basis independence and polynomial sum-degree estimates are genuine building blocks, but the coordinate construction remains substantive. Full generic typeclass experiments are part of native evidence, not text-only guesses.

## Phase 5.5 — Three statement-shape checks

Normal forms compared: Option multivariate polynomial; polynomial over multivariate coefficients; bounded-module tensor; finite coefficient matrix. The current reconstruction equality is useful and both LI/degree outputs are substantive. No pairwise equivalence proliferation proposed.

Syntactic generality: caller-supplied n is useful; actual-degree specialization is checked. Given-basis and PID forms tested. Prefer the generalized scalar theorem with current bounded output, rather than deleting unused-by-one-caller bounds.

Superfluous arguments: no Fintype/DecidableEq survives; hP,hn and all remaining data are substantive; Field is the scalar weakening candidate. RESTATE-BEFORE-SHIP at the verified scalar floor while preserving the full mathematical API.

## Phase 6.0 — Full callers and inline audit

| Caller | Use |
|---|---|
|Roth/Separation.lean:522, private exists_rat_factors_det_hasseDeriv_aux|Destructures l, length bounds, φ,ψ, both LI proofs and equality; discards degree bounds. hψ supplies nonzero generalized Wronskian; hφ supplies nonzero ordinary Wronskian.|

One explicit use, zero outside declaring module. Three lexical occurrences include documentation31 and declaration325. Fresh enumeration of every canonical production module, rg --no-ignore and git grep agree. Exact293 kernel-value audit independently finds the same one private consumer. [callers.json](../evidence/Roth.exists_separated_representation/callers.json), [lexical-enumeration.json](../evidence/Roth.exists_separated_representation/lexical-enumeration.json).

No equivalent independent inline derivation found. Private helpers165–167 are real steps; their SKIP prefilters are not a NO verdict for this public theorem. Full caller replay retains all hypotheses and both Wronskian paths. A refactor can apply the generalized theorem at ℚ without changing the caller's mathematical requirements.

## Phase 6 — Actual composition experiments

Full replay retains coefficient expansion, bounded-basis existence, coordinate-polynomial independence, mapped-basis independence, univariate degree estimate, support-box degree control and reconstruction. Project helpers do not count as mathlib primitives. Conditional ring reconstruction isolates the finite-basis input; generic PID freeness does not erase the polynomial arguments.

No ≤3-existing-call target proof was produced. Tensor finite-sum API loses both LI conditions and bounds. Matrix rank normal form still needs polynomial support/factor transports. Neither NO-has-it nor NO-composable is justified. This is not a closing simp-with-definitions case. No exact?/apply? failure or timeout is claimed as absence evidence; an initial False-based preparation was discarded before execution because it would invalidate the diagnostic.

Native mathlib-only experiment proves the entire free-span version over CommRing+IsDomain with an explicit Module.Free coefficient-span instance; it replays the actual coordinate/reconstruction mathematics under exact10 imports, with Roth target unavailable. This is a conditional abstract hypothesis, while the PID theorem supplies it unconditionally. The complete rational caller also passes using pidRepresentation, preserving both Wronskian arguments. [separated-repr-pid-caller-executed.lean.txt](../evidence/Roth.exists_separated_representation/separated-repr-pid-caller-executed.lean.txt), [separated-repr-pid-caller-receipt.json](../evidence/Roth.exists_separated_representation/separated-repr-pid-caller-receipt.json), [separated-repr-isolated-free-span-receipt.json](../evidence/Roth.exists_separated_representation/separated-repr-isolated-free-span-receipt.json), [separated-repr-guards-receipt.json](../evidence/Roth.exists_separated_representation/separated-repr-guards-receipt.json). [verification.json](../evidence/Roth.exists_separated_representation/verification.json).

## Phase 7 — Verdict and upstream action

**YES-but-generalise-first**, reason LITERATURE-WEAKENING and MODERN-IDIOM: replace Field K by CommRing K + IsDomain K + IsPrincipalIdealRing K and use Module.Finite instead of Field-only finite-dimensional notation in the bounded-basis helper. Both independence families and all degree information survive in the complete native proof. The standard finite torsion-free PID theorem supports the weakening; this is not a hierarchy guess or an unresolved development project.

The missing API is the bounded separated-polynomial decomposition with simultaneous independence of both families, not finite tensor expansion or finite-basis existence. The generic PID instance is already mathlib infrastructure and must be reused. The scalar widening alone does not remove the coordinate independence and support/degree/reconstruction mathematics. Existing tensor/matrix hits do not establish a ≤3-call full theorem. Parent coeffNone was assessed as a composable coefficient alias, but this is not a glue law for that alias: independently re-aiming at optionEquivLeft coefficients leaves the full finite-free decomposition theorem to prove.

Proposed upstream home: **Mathlib/Algebra/MvPolynomial/Separation.lean** (new leaf importing Polynomial, support-degree and linear-algebra/PID infrastructure). Proposed PR title: **feat(Algebra/MvPolynomial): bounded separated representations over principal ideal domains**. Public namespace should be MvPolynomial, with a name indicating existence of independent separated factors. Keep the three construction steps private or promote a generic finite-coordinate/tensor lemma only when its complete independent API is designed.

Grouping: the accepted YES MvPolynomial.degreeOf_hasseDeriv_le and Roth.hasseDeriv_rename_mul_aeval are downstream derivative/separation consumers; the decomposition belongs in its own finite-linear-algebra leaf PR rather than being bundled into foundational Hasse definitions. Prior helper SKIP assessments are not upstream approvals. Current accepted-YES grouping is read from tracked progress. [accepted-yes-grouping.json](../evidence/Roth.exists_separated_representation/accepted-yes-grouping.json).

Checklist before PR:
1. Run /generalise Roth.exists_separated_representation using the exact verified PID full statement; preserve both LI and both degree families, and generalize the finite-basis helper with Module.Finite.
2. Run /cleanup Roth/Separation.lean Roth.exists_separated_representation; normalize coeffNone to the mathlib coefficient API and remove Roth-specific naming in the upstream leaf.
3. Run the mathlib build and the complete rational determinant caller against the generalized theorem; no project theorem may masquerade as an existing mathlib replacement.
4. Request algebra/PID review from **Yaël Dillies**, selected from relevant pinned PID history: commit290f644e69 migrated NoZeroSMulDivisors to Module.IsTorsionFree. **Kim Morrison** is another relevant recent PID-file contributor (commit02398f3984). These are proposed reviewers, not contacts already messaged. [reviewer-commits.json](../evidence/Roth.exists_separated_representation/reviewer-commits.json).

Keep the current theorem in Roth/Separation.lean until a separately authorized generalization/upstreaming change; the overview makes no production edits. The sole explicit caller can apply the generalized theorem at ℚ with the same tuple destructuring and both Wronskian consequences. No Archive destination is needed.

## Phase 8 — Evidence and validation

Exact executed sources/raw native receipts, source/pin hashes, exact canonical293 audit, formal-search receipts, literature-request metadata, caller searches and portable validator are retained. Accepted receipts require complete native success, no errors/warnings/sorryAx and only propext/Classical.choice/Quot.sound. Current copy manifest is authoritative. Root-owned acceptance records and historical manifests are excluded from recursive worker coverage.


Accepted native evidence: original full type/kernel/audit; full project replay; ring given-basis reconstruction; full original caller; full unconditional PID theorem; full PID caller; isolated unconditional PID theorem; isolated full conditional free-span theorem; four mathematical guards plus the narrow Field-inference diagnostic; pinned candidate signatures. All accepted proof receipts are complete and clean. The four mathematical guards test repeated nonzero-but-dependent factors, cancellation, actual degree premise and zero versus positive length with both LI families. FieldNotInferred only checks absence of automatic Field synthesis and proves no impossibility claim.

[verification.json](../evidence/Roth.exists_separated_representation/verification.json), [validate.py](../evidence/Roth.exists_separated_representation/validate.py), [copy-manifest.json](../evidence/Roth.exists_separated_representation/copy-manifest.json).
