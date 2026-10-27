# Roth.degreeOf_rename_mul_aeval

**Verdict: BORDERLINE-needs-human.** The separated partial-degree law is elementary and useful, but its existing spelling combines degree additivity, injective renaming, an independent-variable normalization, and a zero-factor convention. Mathlib has the algebraic core. The choice worth reviewing is which additional normalization API, if any, should be public upstream.

## Phase 0 — Baseline

Declaration 163 is a public theorem at `Roth/Separation.lean:197`, confirmed independently against both canonical manifests. All 17 current production-source/pin hashes match the shared successful baseline. The recorded full build completed successfully; no production edit or Git mutation was made for this assessment. The native original resolves, has a complete kernel body without printer elision, and uses only `propext`, `Classical.choice`, and `Quot.sound`.

Evidence: [fresh input hashes](../evidence/Roth.degreeOf_rename_mul_aeval/inputs.json), [baseline](../evidence/Roth.degreeOf_rename_mul_aeval/baseline-build.txt), [successful full build receipt](../evidence/Roth.degreeOf_rename_mul_aeval/index-file-completion-2026-10-27.json), [native original receipt](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-original-audit-receipt.json).

## Phase 1 — Comprehend

Let U be a polynomial in variables indexed by τ, and let V be a nonzero univariate polynomial over a domain. Embed U into the variables `some j` and V into the separate variable `none`. The degree of their product in `some j` equals the degree of U in j. U may be zero: Lean assigns zero polynomial partial degree zero, so this case is valid separately. The entire declaring module and its sole caller were read; the module constructs the separated determinant factorization used in Roth's Lemma 2.

Full native type:

```lean
@Roth.degreeOf_rename_mul_aeval : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommRing R] [IsDomain R]
  (U : MvPolynomial τ R) {V : Polynomial R},
  V ≠ 0 →
    ∀ (j : τ),
      MvPolynomial.degreeOf (some j) ((MvPolynomial.rename some) U * (Polynomial.aeval (MvPolynomial.X none)) V) =
        MvPolynomial.degreeOf j U
```

The original proof splits U=0, applies `MvPolynomial.degreeOf_mul_eq` in the other branch, identifies the renamed U degree, and proves the V contribution is zero by renaming a singleton-variable polynomial. Its one project proof dependency is `Roth.aeval_X_eq_rename`; the isolated proof replaces that dependency with the actual existing `Polynomial.toMvPolynomial_eq_rename_comp` term. All parameters are explicit above: arbitrary universe-polymorphic τ and R, coefficient ring/domain instances, U, implicit V, its nonzero proof, and j. No `Fintype τ` or `DecidableEq τ` survives elaboration.

Evidence: [native type](../evidence/Roth.degreeOf_rename_mul_aeval/native-type.json), [complete declaring module](../evidence/Roth.degreeOf_rename_mul_aeval/Roth-Separation.lean.txt), [exact isolated proof](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-isolated-executed.lean.txt).

## Phase 2 — Preliminary checks

SMALL: a partial-degree helper, neither a new structure, named theorem, nor listed main result. The one-line definition-only check and its three exceptions are n/a because the declaration is a theorem. Exhaustive literature width still applies.

## Phase 3 — Exhaustive literature

Each query below was actually executed separately. The evidence retains exact requests, response SHA256 and byte counts, returned title/URL locators, and concise original summaries; full returned article/search bodies were not persisted.

| Channel | Actual query / locator | Finding |
|---|---|---|
| General web, specific | `degree in each variable product polynomials disjoint variables integral domain` | Standard domain product-degree rule; disjoint-variable version is a specialization. |
| General web, general | `polynomial degree product leading coefficient nonzero zero divisors commutative semiring` | Nonannihilation of top coefficients is the decisive condition. |
| General web, alias | `partial degree multivariate polynomial product separate variables` | “Partial degree” is standard terminology; separation-algorithm results are broader background. |
| ChatGPT mathematics MCP | unavailable | n/a: no `ask_chatgpt_math` capability in current inventory. |
| Local source | `clean.tex`, §2 Lemma 2, lines347–435 | Final paragraph explicitly compares individual degrees of separated nonzero factors. |
| nLab | `site:ncatlab.org/nlab polynomial ring integral domain degree product` | Polynomial/degree/domain background. Direct degree-page open failed400 with unsupported XHTML content type. |
| nCatLab | `site:ncatlab.org/ncatlab polynomial ring degree product` | Actual distinct namespace query; returned /nlab and /schreiber material, no in-namespace exact hit. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring degree product domain` | Domain/factorization context; tag0BC1 is a UFD result, not the exact target. |
| MathOverflow | `site:mathoverflow.net degree product multivariate polynomials integral domain` | Related formal-polynomial/function and factorization discussions; no exact new formulation. |
| Recent arXiv | `site:arxiv.org/abs/ polynomial multiplication partial degree after:2021-10-27 before:2026-10-28` | 2024 reduction/multiplication paper plus recent algorithm papers; no change to the elementary law. |

The standard content is preservation of degree when multiplying by a nonzero expression independent of the selected variable. Textbook univariate degree additivity supplies the reason: top coefficients multiply without annihilating. Aspnes's [polynomial lecture notes, lines19–20](https://www.cs.yale.edu/homes/aspnes/pinewiki/Polynomials.html) state the field case. Extending to no-zero-divisor semirings is a locally verified Lean generalization, not a claim that these notes state that exact level. [Stacks tag0BC1](https://stacks.math.columbia.edu/tag/0BC1) supplies background on polynomial rings over UFDs. [Wang–Su–Wang–Zhang, submitted19March2024](https://arxiv.org/abs/2403.12716), concerns reversible reductions for polynomial multiplication and is contextual only. We found no distinct named theorem or historical reformulation that justifies preserving the Option-specific spelling upstream.

Evidence: [all eight search records](../evidence/Roth.degreeOf_rename_mul_aeval/literature-individual.json), [four actual primary accesses](../evidence/Roth.degreeOf_rename_mul_aeval/literature-primary-access.json), [availability and limitations](../evidence/Roth.degreeOf_rename_mul_aeval/literature-availability.json), [local source search](../evidence/Roth.degreeOf_rename_mul_aeval/local-literature-search.json), [local Lemma2 excerpt](../evidence/Roth.degreeOf_rename_mul_aeval/clean-excerpt.tex.txt).

## Phase 4a — Parameter and generality audit

| Parameter/hypothesis | Role and verdict |
|---|---|
| τ : Type* | Any variable set already; neither finite nor decidable needed. |
| R : Type* | Arbitrary coefficient universe already. |
| CommRing R | Stronger than needed: actual complete proof works over `CommSemiring R`. |
| IsDomain R | Replace with `NoZeroDivisors R`; no independent `Nontrivial R` instance is needed. A supplied V≠0 already excludes the degenerate case in every inhabited application. |
| U | Arbitrary, including zero. Adding U≠0 would narrow the original API, so the faithful original-form proof keeps the zero branch. |
| V and hV : V≠0 | Essential in this unconditional preservation statement. U=X, V=0 over ℤ is a compiled counterexample to dropping hV. |
| j : τ | Necessary selected coordinate; no distinguished concrete coordinate assumption. |
| some/none embedding | A convenient disjoint-variable representation; the proof uses injection plus absence of j from the other factor, not Option's particular names. |

Dropping all coefficient nonannihilation assumptions is false: over ℤ×ℤ, take U=(1,0)X and V=C(0,1). Both are nonzero, U has degree1, and the product vanishes. This counterexample was compiled, including its degree calculation. `NoZeroDivisors R` is a verified sufficient global hypothesis, not a claim of the weakest possible point-local coefficient condition. More targeted leading-coefficient or nonannihilation premises may suffice; those alternatives were not mechanically verified here and are not claimed generalizations. The proposed semiring weakening preserves the formal polynomial object and degree convention. Generalizing to arbitrary functions would change the object (and lose formal degree); that proposal is rejected.

## Phase 4b — Mechanically verified form

The isolated theorem `SeparatedDegree163.semiring` proves the unchanged conclusion over `[CommSemiring R] [NoZeroDivisors R]`, with arbitrary τ and no finiteness/decidability assumptions. It does not import Roth, and `#check_failure Roth.degreeOf_rename_mul_aeval` guards accidental project reuse. Its proof uses the pinned canonical aeval/rename equality with an explicit type annotation. `abstract_degree_zero` additionally proves the representation-independent principle: for arbitrary P and nonzero Q, `degreeOf j Q=0` implies `degreeOf j (P*Q)=degreeOf j P`, including P=0. This is new diagnostic proof, not an already-existing replacement theorem.

Evidence: [accepted isolated source](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-isolated-executed.lean.txt), [accepted clean native result](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-isolated-receipt.json). Earlier missing-import/type-inference and raw-rewrite-normalization attempts were rejected and are retained separately; none is accepted evidence.

## Phase 4c — Nine modern-idiom rows

| # | Diagnostic | Result / downstream consequence |
|---|---|---|
| 1 | Bundled hypotheses to instances | No new class needed; coefficients already use standard classes. |
| 2 | Filters/nets | No topology or limits. |
| 3 | Universal property | Existing polynomial algebra homs already encode evaluation; no new construction class. |
| 4 | Bundled substructure | No ad hoc closure predicate to replace. |
| 5 | Weaker algebraic hierarchy | Yes: semiring/no-zero-divisor proof compiled; serves ℕ and subtraction-free coefficient contexts. |
| 6 | Higher categories | No categorical content beyond ordinary algebra hom functoriality. |
| 7 | Concrete index generalization | Polynomial exponents must remain ℕ in this API; arbitrary τ already supported. Laurent degrees would be a different representation. |
| 8 | Concrete-via-abstract | Yes: after embedding normalization, only Q≠0 and degreeOf j Q=0 are used. The abstract principle serves independent-variable factors unrelated to Option/univariate evaluation. |
| 9 | False-generalization guard | Semiring and abstract independence restatements preserve the same polynomial/degree object. Compiled counterexamples reject dropping hV or all nonannihilation assumptions. Formal polynomials cannot be replaced by polynomial functions without further structure. |

Modern-idiom verdict: semiring weakening is verified; abstract independence is the organizational candidate. Its useful downstream interaction is with `degreeOf_mul_eq`, injective renaming, and zero-degree factors. This does not itself settle whether a public wrapper is warranted.

## Phase 4.5 — Infrastructure risk

All six definition-specific rows are n/a for this theorem: no typeclass diamond, reducibility declaration, noncanonical definition unfolding, instance priority, universe-forcing construction, or coercion is introduced. Universe-polymorphic theorem elaboration was verified. The representation bridge uses existing algebra homs rather than adding a competing representation.

## Phase 4.6 — Five proof-strategy rows

| # | Check | Assessment |
|---|---|---|
| 1 | ε–δ versus filters | n/a: algebraic finite polynomial statement. |
| 2 | Elements versus substructure inclusions | Current proof uses canonical polynomial-degree API; no ideal/submodule recast helps this equality. |
| 3 | Sequences versus nets | n/a: no limits. |
| 4 | Construction versus universal property | Existing hom equality supplies the aeval bridge directly; no custom construction. |
| 5 | Missing helper API | Potential useful target: degree zero outside the range of a variable renaming, or multiplication by a nonzero zero-degree factor. Exact contribution/naming remains a design question. |

The strategy is mathlib-idiomatic after replacing the project aeval wrapper with `Polynomial.toMvPolynomial_eq_rename_comp`. It is an ordinary new proof with a zero branch and normalization, not an existing one-call theorem. Cost is not used to decide the verdict.

## Phase 5 — Fifteen actual mathlib search cells

All five methods ran on current, literature-standard, and abstract forms. Finder returned `degreeOf_rename_of_injective`, `degreeOf_mul_eq`, and degree-zero/constant multiplication candidates. LeanSearch independently found the generic product-degree theorem. Loogle's current-form search returned no item; its abstract search found basic degree-zero facts. Local search reports index unavailable, while returning source-backed results; this limitation is not treated as absence. Scratch/project hits were excluded as replacement candidates. Exact requests and raw formal-search responses are preserved.

| Form | Finder | Loogle | LeanSearch | rg | local |
|---|---|---|---|---|---|
| Current rename/aeval product | ran | ran | ran | ran | ran |
| Standard partial-degree additivity | ran | ran | ran | ran | ran |
| Abstract independent/degree-zero factor | ran | ran | ran | ran | ran |

Pinned source inspection and native checks verify these positive candidates:

* `MvPolynomial.degreeOf_mul_eq`, `Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean:43`: nonzero p,q over a commutative semiring with no zero divisors; degreeOf n(p*q)=degreeOf n p+degreeOf n q.
* `MvPolynomial.degreeOf_rename_of_injective`, `Mathlib/Algebra/MvPolynomial/Degrees.lean:419`: injective renaming preserves the corresponding coordinate degree.
* `Polynomial.toMvPolynomial_eq_rename_comp`: actual algebra hom equality that bridges aeval at X i and singleton-variable renaming; not definitional in the attempted raw rewrite.
* `Polynomial.toMvPolynomial_injective`: evaluation at the formal variable is injective and preserves V≠0.
* `MvPolynomial.degreeOf_C_mul`: preserves degree under multiplication by an actual coefficient constant in nonZeroDivisors. The embedded V is not such an R-constant; moving to a larger coefficient ring needs its own representation normalization.

Other relevant building blocks are `rename_eq_zero_iff_of_injective`, `degrees_rename_of_injective`, `degreeOf_eq_natDegree`, `Polynomial.natDegree_mul_C`, and basic multiset count/replicate laws. They supply the mathematics without giving the whole old spelling as a direct call. Search results establish these presences; they do not prove global absence. Parent re-aim gate: the original uses no custom parent polynomial definition already replaced by D′; the project aeval bridge has an exact mathlib replacement, and that replacement is used explicitly. It does not itself supply the degree law.

Evidence: [all fifteen formal cells](../evidence/Roth.degreeOf_rename_mul_aeval/formal-search.json), [current rg](../evidence/Roth.degreeOf_rename_mul_aeval/rg-current.json), [standard rg](../evidence/Roth.degreeOf_rename_mul_aeval/rg-literature.json), [abstract rg](../evidence/Roth.degreeOf_rename_mul_aeval/rg-modern.json), [pinned degree source](../evidence/Roth.degreeOf_rename_mul_aeval/Mathlib-Algebra-MvPolynomial-NoZeroDivisors.lean.txt).

## Phase 5.5 — Three statement-shape checks

Normal form: the equality has the computed product degree on the left and the simpler U degree on the right, consistent with rewriting. Equivalent forms are the Option/aeval formula, an arbitrary degree-zero-factor formula, and univariate degree preservation after a coordinate equivalence. Mathlib's canonical algebraic core is product-degree additivity; representation changes require their own bridge. No orthogonal equivalence is proposed.

Syntactic generality: implicit V plus hV is convenient in the actual caller; U must remain arbitrary in the old form. The abstract alternative takes a general nonzero Q and an explicit degree-zero premise, making it reusable without forcing a univariate encoding. The full original caller supplies U≠0 independently; its inlined proof can use that stronger local fact without narrowing the exported original theorem.

Superfluous arguments: no dead j/U/V arguments; τ already arbitrary. `CommRing`/`IsDomain` can be replaced by `CommSemiring`/`NoZeroDivisors`. hV cannot be removed. Fintype/DecidableEq are absent from the actual API, so they are not claimed as new weakenings. Statement-shape verdict: RESTATE-BEFORE-SHIP if a contribution is selected; preserve the original local API while deciding the upstream abstraction.

## Phase 6.0 — Callers and inline audit

Fresh canonical-inventory lexical enumeration, `rg --no-ignore`, and tracked `git grep` agree: two textual occurrences, the declaration and one use. The sole explicit caller is `Roth.exists_det_eq_mul`, `Roth/Separation.lean:554`, rewriting its remaining-variable factor bound. There are zero external-to-file explicit uses. Source inspection found no equivalent inline rederivation elsewhere. The neighboring distinguished-variable theorem is analogous, not the same statement.

The fresh canonical runtime audit traverses exactly the tracked 293 names in their exact order, including private names, and finds one direct kernel-value consumer: `Roth.exists_det_eq_mul`. This is a direct consumer audit, not a claim about transitive simp/kernel closure or external projects.

Evidence: [lexical enumeration](../evidence/Roth.degreeOf_rename_mul_aeval/lexical-enumeration.json), [tracked grep](../evidence/Roth.degreeOf_rename_mul_aeval/caller-git-grep.json), [unignored grep](../evidence/Roth.degreeOf_rename_mul_aeval/caller-rg.json), [inline search](../evidence/Roth.degreeOf_rename_mul_aeval/rg-inline.json), [canonical audit source](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-audit-executed.lean.txt).

## Phase 6 — Actual composition and caller experiment

The isolated original-form proof succeeds using only mathlib. A direct `degreeOf_mul_eq` call fails even after both required factor nonzero proofs are supplied: its conclusion still has the extra degree of the independent factor, and its U degree is still in the renamed variables. The faithful proof supplies those normalizations and handles U=0. A second accepted isolated composition experiment supplies both genuine nonzero proofs, confirms that even `simpa only [degreeOf_rename_of_injective ...]` does not close the old statement from degree additivity, and then closes it using the actual independence normalization. The diagnostic abstract law has a short proof after the degree-zero premise is supplied; deriving that premise for the aeval expression is the substantive remaining API question. The final independence normalization closes with `simp [degreeOf, degrees_rename_of_injective, Multiset.mem_replicate]` after the preceding zero split, degree-additivity step, rename-degree step, and typed representation bridge. This tail simp is not a closing simp composition for the whole declaration and does not automatically trigger a verdict. BORDERLINE rests on the concrete upstream API choice, not the short final tactic.

The entire sole caller was actually replayed with the original `[Finite τ]` interface and all original hypotheses/conclusions. Its target use was replaced by an inline mathlib derivation, using its available U≠0. A term elaborator accesses the actual existing private factorization helper; it introduces no axiom and avoids reimplementing unrelated machinery. The assessed target name is absent from the new source region. Native checking completed cleanly with only standard axioms.

Evidence: [full caller executed source](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-callers-executed.lean.txt), [clean caller receipt](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-callers-receipt.json), [exact new caller region](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-callers-region.txt), [isolated source and branch guard](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-isolated-executed.lean.txt).

Supplemental evidence: [exact normalized-branch composition source](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-composition-executed.lean.txt), [clean composition receipt](../evidence/Roth.degreeOf_rename_mul_aeval/separated-degree-composition-receipt.json).

## Phase 7 — Verdict and concrete design questions

**BORDERLINE-needs-human.** The theorem is not dead code, the mathematics is standard, the coefficient hierarchy can be weakened mechanically, and mathlib already contains degree additivity plus the required embedding bridge. The remaining normalization is ordinary proof rather than an honest one-to-three-call specialization. A single source caller is a local-API signal, not a reason to overstate either novelty or redundancy. The general degree-zero-factor law and the renaming independence normalizer are plausible upstream directions; deciding which deserves a public name is mathematical API design, not missing verification.

1. Should mathlib expose degree preservation for multiplication by a nonzero factor of degree zero, allowing the other factor to be zero?
2. Should the primary reusable addition instead be a `degreeOf (rename f P)=0` theorem for variables outside the range of f, with the separated formula derived locally?
3. Should the Option/aeval specialization remain project-local after weakening to semirings, rather than adding another upstream spelling?

These are future design questions, not a request to stop this read-only assessment. No production change is proposed here. If the result remains local, its natural destination is the existing degree helper section of `Roth/Separation.lean`. If abstract helpers are accepted, a likely home for rename independence is `Mathlib/Algebra/MvPolynomial/Degrees.lean`; degree multiplication belongs in `Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean`. Import layering and names should be reviewed before a PR. A new helper proof is not counted as an existing mathlib replacement.

## Phase 8 — Delivery and verification

This package records the exact executed sources and complete raw receipts, all rejected native attempts separately, fresh source/pin hashes, the ordered canonical audit, all formal/literature searches, and a portable read-only validator. Original native output is scoped to its new target-specific region while full-file error/warning/sorry checks remain global. The successful isolated run required the genuine additional `Mathlib.Algebra.MvPolynomial.NoZeroDivisors` import; rejected missing-import runs are not API-absence evidence. Full source artifacts use `.lean.txt` to avoid indexing them as production modules. `assessment.json` and `verification.json` distinguish completed verification from the pending root acceptance and future design decisions.
