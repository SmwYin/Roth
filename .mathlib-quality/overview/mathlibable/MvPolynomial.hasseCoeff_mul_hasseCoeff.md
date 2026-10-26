# MvPolynomial.hasseCoeff_mul_hasseCoeff — completed private-helper overview triage

**Verdict: SKIP — private declaration (overview Step 9a).** The applicable inventory, structural review, caller audit and proof verification are complete. The full public-declaration mathlibable literature/search workflow is not applicable under the installed rule. This is not a negative verdict about whether an equivalent public mathematical identity could ever be useful upstream.

## Rule and completion scope

The installed [overview prefilter](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/prefilter-rule.md) explicitly lists “`private` or `local` modifier”. The source has that modifier at `Roth/HasseDeriv.lean:153`. This report completes its applicable overview entry and records the exact first unfinished successor in the project progress record after acceptance. No full-mathlibable phase is claimed complete for this helper, and no public theorem inherits this SKIP.

## Inventory and mathematical content

Kind: private lemma. Source lines153–168,14 proof lines. The source logical name is `MvPolynomial.hasseCoeff_mul_hasseCoeff`; Lean gives private declarations generated internal names, which this assessment does not claim to resolve by the displayed name. [Exact source and metadata](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/corrected-target.json).

For arbitrary natural multi-indices f,d,e on any variable type, it proves

```lean
hasseCoeff d (f + d) * hasseCoeff e (f + d + e) =
  hasseCoeff d (d + e) * hasseCoeff (d + e) (f + (d + e))
```

This is the binomial cocycle identity needed to compare two successive Hasse derivatives with the combined derivative. Every expression is a natural number. There is no coefficient semiring parameter, no variable finiteness or decidable-equality hypothesis, and no dominance assumption: the arguments have been written with additions to ensure the necessary orders.

The proof enlarges four finite-support products to the union of the supports of d and e, using that a choose-factor with lower order zero is one. It combines pairs of products coordinatewise, then applies `Nat.choose_mul` and `Nat.choose_symm_add` at each coordinate. The exact body is retained as [source](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/target-excerpt.lean.txt).

## Dependencies and callers

The only direct project declaration in the statement/body is `MvPolynomial.hasseCoeff`. Existing mathlib ingredients include `Finsupp.prod_of_support_subset`, support-union inclusions, `Finsupp.support_add`, `Finset.prod_mul_distrib`, `Finset.prod_congr`, `Nat.choose_zero_right`, `Nat.choose_mul`, `Nat.choose_symm_add`, and elementary natural addition/order laws. These are already used successfully; no new generic finite-product API is needed to express this proof.

| Explicit caller | Invocation | Role |
|---|---|---|
| `MvPolynomial.hasseDeriv_hasseDeriv`, starts175 | HasseDeriv.lean:179 | Reconciles the two coefficient factors in operator composition. |
| `MvPolynomial.hasseCoeff_mul_succ`, starts191 | HasseDeriv.lean:195 | Specializes the cocycle to a one-coordinate successor identity. |

Both callers are in the declaring module; no explicit external source use was found across all14 production Lean files. [Untruncated searches](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/source-search.json) and [caller excerpts](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/caller-excerpts.lean.txt) support these counts. This is an explicit source-reference audit, not an opaque kernel/simp closure claim.

## Applicable structural review

**Mathlib API:** the coordinate identity is existing `Nat.choose_mul`, lifted through finite products with existing support-extension tools. The surrounding scalar alias was assessed separately; this private helper is not independently advertised as a new public mathlib declaration. A later public Hasse composition assessment must examine its own full mathematical/API scope.

**Duplication:** the fresh source search finds this one use of `Nat.choose_mul` and the two helper invocations. The proof packages a shared scalar calculation; it is not two duplicated downstream proofs. This bounded audit does not claim a global literature or library absence theorem.

**Generality:** variable types and natural multi-indices are already unrestricted in this source interface. The native replay's type has no R or semiring instance. Replacing natural choose factors with an abstract cocycle would require an explicit cocycle assumption, which would package the conclusion rather than prove it. No unverified generalization is proposed.

**Missing API:** no generic support-product lemma is missing for this proof. The identity helps the public composition and successor APIs, whose mathlibable assessments remain separate. No verdict is assigned here to those unfinished declarations.

**Junk/style/documentation:** keep this shared helper private: it has two real uses, a descriptive mathematical name and a14-line proof below the cleanup size threshold. A public docstring or public export is unnecessary for its current role. No source edit, rename, deletion or theorem change is recommended by this triage.

## Verification and evidence

The successful full `lake build` baseline is reused only after all17 production-source/pin hashes match. Additionally, the entire exact proof was replayed in scratch as `PrivateScalarAssessment.replay`, with only the private name/namespace changed. Native Lean reports its full type, zero errors/warnings, completed elaboration and only `propext`, `Classical.choice`, `Quot.sound`. The executed source bytes were matched against the live scratch file before acceptance.

[Verification index](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/verification.json), [raw native receipt](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/native-replay.json), [exact executed content](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/executed.lean.txt), [baseline](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/baseline-build.txt), and [all17 hashes](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/source-check.json) are preserved. The replay validates the exact proof but is not misrepresented as a fresh axiom query on Lean's generated private name. Production files and pins remain unchanged.

The archived Lean content uses `.lean.txt` filenames to preserve exact proof evidence without presenting those copies as additional workspace Lean modules. The native request retains the actual executed `.lean` path.

## Workflow gates and next action

Inventory, source/caller review, API/duplication/generality/missing-API/junk review, prefilter application, proof verification and evidence checks: complete. Full public mathlibable literature/five-method/modern-idiom/contribution verdict phases: n/a under the explicit private prefilter. There is no unresolved assessment item or user question. Root acceptance is required before the overview/progress update, commit and push.

[Assessment](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/assessment.json), [overview entry](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/overview-entry.json), [copy manifest](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/copy-manifest.json), and [portable validator](../evidence/MvPolynomial.hasseCoeff_mul_hasseCoeff/validate.py) supply the machine-readable record. After publication, continue with the next canonical declaration rather than treating this private triage as a public contribution decision.
