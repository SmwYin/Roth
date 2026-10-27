# `Roth.exists_int_eq_of_gcd_eq_one` — YES-but-generalise-first

Canonical declaration173, `Roth/Separation.lean:443`. Full read-only overview/mathlibable assessment; production sources and pins unchanged. Root acceptance pending.

## Phase 0 — Doctor

All seventeen freshly computed source/pin hashes match the shared successful `lake build` baseline (exit0,2467 jobs). [Fresh hashes](../evidence/Roth.exists_int_eq_of_gcd_eq_one/baseline-hashes.json), [baseline](../evidence/Roth.exists_int_eq_of_gcd_eq_one/baseline-build.txt), [inputs](../evidence/Roth.exists_int_eq_of_gcd_eq_one/input-manifest.json). The whole declaring module, including the complete sole explicit caller, was read. [Module](../evidence/Roth.exists_int_eq_of_gcd_eq_one/source-context.lean.txt). No prefilter or verdict inheritance applies.

## Phase 1 — Comprehend

A finite integer family of gcd1 detects whether a rational number is an integer: if each family member multiplied by the rational is an integer, the rational itself is an integer. The existential witnesses and equality orientation are part of the interface.

```lean
∀ {ι : Type u_2} {s : Finset ι} {u : ι → ℤ},
  s.gcd u = 1 → ∀ {v : ℚ},
    (∀ a ∈ s, ∃ (z : ℤ), ↑(u a) * v = ↑z) → ∃ (z : ℤ), v = ↑z
```

[Full native type](../evidence/Roth.exists_int_eq_of_gcd_eq_one/native-type.json), [original receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/integral-original-audit-receipt.json), [exact executed source](../evidence/Roth.exists_int_eq_of_gcd_eq_one/integral-original-executed.lean.txt). The proof obtains finite Bézout coefficients, chooses integer product witnesses, and returns their integer weighted sum. Casting the Bézout relation to ℚ and multiplying by `v` proves the witness equation. The project dependency `exists_sum_mul_eq_gcd` supplies only Bézout, not integrality descent.

The original body is fully printed (1946 characters, no MCP elision). The canonical kernel audit checks exact ordered293 names including private names,293 unique/present constants and293 values. Its sole direct kernel-value consumer is `_private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux`. These are kernel-value consumers, distinguished from lexical source callers. Standard axioms only: `propext`, `Classical.choice`, `Quot.sound`.

## Phase 2 — Preliminary

SMALL: elementary Bézout descent used inside integral factor descent. The proof contains a real finite linear-combination calculation; smallness alone does not decide composability. The one-line definition-only test is n/a for this theorem. One internal use is an abstraction signal, not evidence that a mathematical proof can be replaced by ≤3 existing calls.

## Phase 3 — Exhaustive literature

Exact requests, returned response hashes/bytes/status, titles/locators and original summaries are in [general searches](../evidence/Roth.exists_int_eq_of_gcd_eq_one/literature-0.json), [named channels](../evidence/Roth.exists_int_eq_of_gcd_eq_one/literature-1.json), [MO/arXiv](../evidence/Roth.exists_int_eq_of_gcd_eq_one/literature-2.json), [primary access](../evidence/Roth.exists_int_eq_of_gcd_eq_one/literature-3.json), [retries](../evidence/Roth.exists_int_eq_of_gcd_eq_one/literature-4.json). No article/search-result bodies are retained. Returned locator query parameters are removed; exact requests and returned-response digests remain.

| Channel | Actual request / primary locator | Finding |
|---|---|---|
| General specific | `rational number integer coprime coefficients Bezout lemma Gauss primitive polynomial` | Classical Bézout scalar-integrality argument related to primitive polynomial descent. |
| General abstract | `unit ideal generators scalar multiples submodule membership lemma` | Unit-ideal generation is the abstract membership mechanism. |
| General finite/history | `finite family integers gcd one rational multiples integer Bezout identity` | Finite-family extension of Bézout, rather than pairwise coprimality. |
| ChatGPT math | Tool inventory | n/a: `ask_chatgpt_math` unavailable. |
| Local clean.tex | §2 lines420–431 | Explicitly gives `∑ z_a u_a=1`, hence `v_b=∑ z_a(u_a v_b)` integral. [Search](../evidence/Roth.exists_int_eq_of_gcd_eq_one/local-literature-search.json), [excerpt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/local-literature.txt). |
| nLab | `site:ncatlab.org/nlab Bezout identity ideal relatively prime`; Bézout ring, Definition | Bézout rings have finite generated ideals principal and gcd as a linear combination. Direct page access returned HTTP400 unsupported `application/xhtml+xml`; search content returned. |
| nCatLab | `site:ncatlab.org/ncatlab unit ideal generators module`; retry `site:ncatlab.org/ncatlab "Bezout"` | Returned nLab pages outside the requested namespace; no exact nCatLab result. No absence inference. |
| Stacks | `site:stacks.math.columbia.edu primitive polynomial Gauss lemma`; retry Gauss lemma | Tag00EZ Example10.27.2 uses Gauss descent and denominator clearing. Tag00FC was opened and rejected as unrelated; it is not a target citation. |
| MathOverflow | `site:mathoverflow.net primitive polynomial rational integer coefficients Gauss lemma` | Question314251, Lemma2, studies rational composition becoming integral and a denominator argument using primitive coefficients; supplementary context. Question512096 distinguishes primitivity forms. |
| Recent arXiv, five years | `site:arxiv.org "primitive" "content" "polynomial" after:2021-10-27 before:2026-10-28` | arXiv2610.30208, submitted2026-10-21, discusses polynomial content and primitivity; an application, not the exact abstract theorem. Initial Gauss-periods hit2212.06115 was rejected as unrelated. |

Primary [Southampton MATH1001 §3.3](https://www.southampton.ac.uk/~wright/1001/bezouts-identity.html), Theorem3.16 and the finite-set extension, explains Bézout and ideal generation. [nLab Bézout ring](https://ncatlab.org/nlab/show/B%C3%A9zout%2Bring), Definition, gives the ring-level formulation. [Stacks00EZ](https://stacks.math.columbia.edu/tag/00EZ) supplies related Gauss-descent context. [Recent arXiv abstract](https://arxiv.org/abs/2610.30208) is dated application context. [MathOverflow314251](https://mathoverflow.net/questions/314251/f-g-in-mathbbzx-y-satisfying-operatornamejacf-g-0-and-f-g-noti) is supplementary discussion, not the foundational justification.

Synthesis: the proof uses only finite Bézout linear combinations and closure under addition/scalar multiplication. The integer image in ℚ is a ℤ-submodule. Thus the same proof applies to any submodule over a commutative Bézout ring, with gcd normalization. The stronger useful conclusion is that the gcd times the element lies in the submodule, without requiring gcd1; unit gcd then gives membership. This is a module/Bézout formulation, not a claim that arbitrary GCD rings satisfy Bézout. A fraction-field formulation over GCD domains may also hold by reduced denominators; that different route is not claimed as a verified mechanical weakening here.

## Phase 4a — All parameters

| Parameter / hypothesis | Role and audit |
|---|---|
| `ι : Type*` | Arbitrary universe; no finiteness or decidable equality hypothesis. Already unrestricted. |
| `s : Finset ι` | Only the selected finite family matters; no nonempty assumption is needed, since empty gcd0 cannot equal1 in ℤ. |
| `u : ι → ℤ` | Need collective gcd1, not pairwise coprimality. Zero entries are permitted. Generic form uses `R` with `[CommRing R] [IsBezout R] [NormalizedGCDMonoid R]`. |
| `hu : s.gcd u=1` | Essential for the unscaled conclusion; singleton2 and `v=1/2` violate the conclusion without it. Generic scaled-membership theorem drops `hu`; `IsUnit (s.gcd u)` suffices for unscaled membership. |
| `v : ℚ` | No nonzero/positivity assumption. Rational field arithmetic is unused except for viewing integer coefficients/products in ℚ. Generic form allows any module. |
| `hv` | All selected products must lie in the integer image. Retained exactly as membership in a submodule; not weakened to existence for some generator. |
| Conclusion | Preserves an actual integer witness for the original via linear-map range membership. No confusion with algebraic integrality. |
| Outer module parameters | `τ`, `Fintype τ`, `DecidableEq τ` do not occur in the full native type; nothing to remove. |

## Phase 4b — Generality verdict

STRICTLY NARROWER THAN THE VERIFIED MODULE FORM. This is a genuine change of representation, justified by a transferred proof, not a claim that replacing the concrete types is definitionally trivial. The proposed primary API has no `hu`:

```lean
theorem Submodule.gcd_smul_mem {R M ι : Type*} [CommRing R] [IsBezout R]
    [NormalizedGCDMonoid R] [AddCommMonoid M] [Module R M]
    (N : Submodule R M) (s : Finset ι) (u : ι → R) (v : M)
    (hv : ∀ i ∈ s, u i • v ∈ N) : s.gcd u • v ∈ N
```

The unit-gcd consequence uses existing `Submodule.smul_mem_iff_of_isUnit`. The original is recovered by taking `R=ℤ`, `M=ℚ`, `N=LinearMap.range (Algebra.linearMap ℤ ℚ)` and `hu`; range membership returns the same integer witness after symmetry. The proof and actual caller experiment are linked in verification below. No domain, field, fraction-ring, characteristic, finite-dimensionality, or cancellation assumption is needed by this module theorem. `CommRing`, Bézout and normalized gcd are inherited from the existing finite Bézout theorem; no unsupported semiring weakening is asserted.

## Phase 4c — Modern-idiom check

| # | Question | Answer / mathematical consequence |
|---|---|---|
| 1 | Typeclasses | Yes: generic `IsBezout`, normalized gcd and module structures replace concrete ℤ/ℚ arithmetic; no global instances are added. |
| 2 | Filters / nets | No: no topology or limits. |
| 3 | Universal-property construction | No new construction needed; existing linear-map range expresses the integer image. |
| 4 | Bundled substructure | Yes: replace ad hoc existential integer-image membership by `Submodule`; immediately supports ranges, kernels, quotients, intersections and scalar restriction. |
| 5 | Weaker hierarchy | Yes: any module over a commutative Bézout ring; no field or fraction-ring assumption in the proved module form. |
| 6 | Higher categories | No: no categorical coherence issue. |
| 7 | Concrete index | No: `ι` is already arbitrary. ℤ and ℚ are coefficient/ambient objects, handled by rows4–5. |
| 8 | Concrete-via-abstract | Yes by transferred proof: after Bézout, only finite sums, casts/scalars and closure remain. The literal zero/one-occurrence shortcut does not fire: ℤ/ℚ type annotations each appear on two calc lines; no `Rat.`/`Int.` operation appears. The native generic proof demonstrates the abstract mechanism, and the original is recovered through range membership. |
| 9 | False-generalization guard | Pass for the verified Bézout-module proposal. Reject replacing Bézout by an arbitrary gcd ring while equating gcd1 with unit-ideal generation: `(2,X)` in ℤ[X] has gcd1 but is a proper ideal. This guard concerns arbitrary modules, and does not assert that fraction-field integrality fails over gcd domains. |

[Actual concrete/abstract lexical diagnostic](../evidence/Roth.exists_int_eq_of_gcd_eq_one/concrete-abstract-diagnostic.json). Modern-idiom verdict: MODERN-IDIOM AVAILABLE with concrete downstream use in submodule membership and integral coefficient descent. The generalization preserves the source's finite-family mechanism and all original witnesses via specialization.

## Phase 4.5 — Infrastructure risks

Theorem n/a for all six definition/instance risks: typeclass diamonds (no instance declared), reducibility leak (no definition), noncanonical unfolding (no reducible alias), instance-priority collision (no instance), universe issues (universe-polymorphic theorem checked), coercion ambiguity (no new coercion). The generic theorem consumes existing structures; it does not install them.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Answer / alternative |
|---|---|---|
| 1 | Topology / epsilon-delta | No topology. |
| 2 | Elements vs substructures | Yes: use submodule closure after finite Bézout, replacing chosen integer witnesses and cast sums. |
| 3 | Analysis / sequences | No analysis. |
| 4 | Category / universal property | No new object; linear-map range suffices. |
| 5 | Missing helpers | Finite-gcd scalar membership is the precise candidate gap; existing unit-ideal membership is already available. |

REFACTOR-RECOMMENDED: transfer the Bézout proof to `Submodule.gcd_smul_mem`, then recover the concrete integer-image specialization. CHEAP proof transfer, actually checked; cost does not determine the verdict. The abstract theorem `Submodule.mem_of_span_top_of_smul_mem` gives the mathematical mechanism in an existing alternative interface, but connecting a finite gcd premise to unit-ideal generation requires a real bridge.

## Phase 5 — Actual five-method search on all three forms

Every cell below is an actual request/receipt, rather than a suggested search. External indices can differ from this pinned checkout. Local-search receipts explicitly report an unavailable index; returned fallback hits are useful but absence is not established by them.

| Form | Finder | Loogle | LeanSearch | rg | Local name search |
|---|---|---|---|---|---|
| Current integer/rational gcd1 | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/current-leanfinder.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/current-loogle.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/current-leansearch.json) | [full receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/current-rg.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/current-local_search.json) |
| Literature finite Bézout | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/standard-leanfinder.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/standard-loogle.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/standard-leansearch.json) | [full receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/standard-rg.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/standard-local_search.json) |
| Abstract module/unit ideal | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/abstract-leanfinder.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/abstract-loogle.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/abstract-leansearch.json) | [full receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/abstract-rg.json) | [receipt](../evidence/Roth.exists_int_eq_of_gcd_eq_one/abstract-local_search.json) |

Positive pinned candidates:

- `Finset.gcd_eq_sum_mul`, `Mathlib/RingTheory/PrincipalIdealDomain.lean:233`: arbitrary finite Bézout coefficients. Supplies the linear combination, but not module membership or integral descent.
- `Submodule.mem_of_span_top_of_smul_mem`, `Mathlib/RingTheory/Ideal/Operations.lean:93`: the existing unit-ideal/module membership law. Actual Finder and LeanSearch returned this exact hit. A direct exact-call example checks its full interface.
- `Submodule.smul_mem_iff_of_isUnit`, `Mathlib/Algebra/Module/Submodule/Defs.lean:233`: cancels a unit scalar in submodule membership. Supplies the unit-gcd corollary after the new scaled-gcd membership proof.
- `IsLocalization.IsInteger` and `isInteger_smul`, `Mathlib/RingTheory/Localization/Integer.lean:45,62`: image membership and scalar closure, without finite gcd descent.

[Exact pinned source archives and hashes](../evidence/Roth.exists_int_eq_of_gcd_eq_one/mathlib-inputs.json), [untruncated candidate full-name/semantic source search](../evidence/Roth.exists_int_eq_of_gcd_eq_one/candidate-fullname-rg.json). The mathlib-only execution guards the absent project target and positively probes the actual generic unit-ideal, Bézout, submodule-closure and integer-image routes. A draft blind `exact?` negative was removed before execution and supplies no evidence. Search failures alone are not an absence proof; no absolute absence assertion rests on them. The accepted generic proof constructs the finite linear-combination membership bridge; it is not claimed to be an already existing mathlib call.

## Phase 5.5 — Statement shape

1. Normal form: original witnesses have `u_i*v = ↑z`, conclusion `v=↑z`; `IsLocalization.IsInteger`/linear-map range uses reverse orientation. The specialization explicitly performs symmetry; this is not ignored as definitional equality.
2. Syntactic generality: arbitrary `ι` and a finite subset are already right. Generic arbitrary-module proof and `AddCommMonoid` rather than `AddCommGroup` were attempted with the same finite Bézout argument. Stronger scaled conclusion and unit-gcd corollary were separately checked.
3. Superfluous arguments: no unused native parameter or instance. Do not remove `hu` from the unchanged conclusion. The proposed generic scaled conclusion changes the statement in an explicit, verified way.

RESTATE-BEFORE-SHIP: use the generic submodule theorem as primary API; the original concrete witness spelling can remain project-local during migration. No implicit generality claim is based only on a name or on syntax.

## Phase 6.0 — Call sites and inline audit

| Explicit caller | Location | Role / complete experiment |
|---|---|---|
| `_private.Roth.Separation.0.Roth.exists_int_polynomial_of_primitive_factor_aux` | `Roth/Separation.lean:473` | For each univariate coefficient `b`, apply gcd1 to the coefficients of primitive `U`; the product witness is the appropriate coefficient of integer `F`. Replay the entire helper with the generic-specialized replacement. |

Internal use count1. [Unignored source search](../evidence/Roth.exists_int_eq_of_gcd_eq_one/callers-rg.json), [tracked source cross-check](../evidence/Roth.exists_int_eq_of_gcd_eq_one/callers-git-grep.json), [canonical-inventory lexical enumeration](../evidence/Roth.exists_int_eq_of_gcd_eq_one/lexical-enumeration.json), [caller audit](../evidence/Roth.exists_int_eq_of_gcd_eq_one/caller-audit.json), [inline search](../evidence/Roth.exists_int_eq_of_gcd_eq_one/inline-rg.json). Inspection found no independent inline rederivation of this statement. The adjacent Bézout wrapper is a different statement. Neither the one lexical caller nor the one direct kernel consumer is asserted to describe transitive simp/kernel closure.

## Phase 6 — Composition experiments

The original proof can replace its project Bézout wrapper with `Finset.gcd_eq_sum_mul`; it still chooses product witnesses and proves the weighted sum identity using casting, distributivity and associativity. This is a new proof, not a ≤3-call composition.

The unit-ideal abstract law is already one existing call:

```lean
N.mem_of_span_top_of_smul_mem s hs v hv
```

Its premise `Ideal.span s=⊤` is not the given finite gcd1 premise. The verified generic gcd-membership proof obtains Bézout coefficients, rewrites scalar multiplication of the finite sum, and proves termwise submodule closure. The concrete specialization constructs range witnesses and reverses equality. These bridges are real proofs; none is hidden inside a claimed one-line existing specialization. No verified ≤3-existing-call full-statement replacement was found for the original or finite-gcd module proposal. This is a search-and-experiment conclusion, not an impossibility proof. No closing `simp [defs...]` probe is misclassified as automatic NO; simple normalization steps inside the complete new proof do not turn the whole argument into a composition.

The mathlib-only batch passed its first actual execution; the strongest-generic proof, concrete specialization, nonunit/empty semantic guards and entire sole caller also passed their first actual execution, with complete diagnostics, no warnings/errors and standard axioms only. The nonunit guard proves `2*(1/2)` is integral while `1/2` is not; the empty-family guard checks that empty gcd cannot satisfy the original premise. The native evidence and exact executed sources, including the full sole caller, are enumerated in [verification](../evidence/Roth.exists_int_eq_of_gcd_eq_one/verification.json). Preparation-only snippets remain labelled as such; only accepted native receipts support verification.

## Phase 7 — Verdict

**YES-but-generalise-first, reason MODERN-IDIOM.** The concrete integer/rational theorem hides a finite-gcd scalar-membership lemma for arbitrary submodules over Bézout rings. The gap is precisely the finite-gcd membership bridge adjacent to existing `Finset.gcd_eq_sum_mul`; the more abstract unit-ideal law is already present. A generic proof and exact original specialization demonstrate a real generalization, while direct composition does not eliminate the finite linear-combination argument. This verdict is independent of declaration170/172, and does not treat their outcomes as proof.

Proposed upstream file: `Mathlib/RingTheory/PrincipalIdealDomain.lean`, after `Finset.gcd_eq_sum_mul`, where Bézout, finite gcd and submodule closure are already available through existing imports. Proposed PR title: **“feat(RingTheory): finite gcd scalar membership in submodules over Bézout rings”**. Proposed primary name: `Submodule.gcd_smul_mem`; optional unit-gcd corollary through existing `smul_mem_iff_of_isUnit`. Suggested reviewer Xavier Roblot (`bf0ef6d9e8`, generalized ideal-span divisibility), with Noah Walker (`c6d40f2169`, duplicate ideal API cleanup; `5edf93c0f3`, ideal multiplication conventions) as an alternative. These are candidates, not contacted reviewers. Reviewer selection is grounded in relevant recent path commits; see [reviewer evidence](../evidence/Roth.exists_int_eq_of_gcd_eq_one/reviewers.json).

Grouping: coordinate the concrete application with already accepted YES `Roth.exists_primitive_smul_eq` (172), whose primitive-factor descent uses the present helper indirectly. [Fresh accepted grouping](../evidence/Roth.exists_int_eq_of_gcd_eq_one/accepted-grouping.json). That declaration proposes a polynomial content module, so keep the foundational membership addition in the ring-theory file and use separate focused PRs if import layering calls for it. No unassessed declaration is claimed as accepted YES.

Before contribution: `/generalise Roth.exists_int_eq_of_gcd_eq_one`; restate primary API as the verified generic gcd-scaled submodule lemma; `/cleanup Mathlib/RingTheory/PrincipalIdealDomain.lean Submodule.gcd_smul_mem`; inspect the unit-gcd corollary for redundancy; add a mathematical docstring; run the appropriate build/checks and `/pre-submit`; choose reviewers from recent relevant commits. For the sole project caller, replace `exists_int_eq_of_gcd_eq_one hgcd` by the checked range-specialization of the generic lemma, preserving the integer witness and all coefficient equalities. Until that upstream API is adopted, `Roth/Separation.lean` is the appropriate local destination. There is no cost-based downgrade or unsupported deletion recommendation.

## Phase 8 — Overview and handoff

No junk/dead-code finding: this helper is used once explicitly and once directly in the canonical kernel audit, in a central integral-factor descent. Moral duplication is mathematical (Bézout and unit-ideal membership), with a missing finite-gcd/module bridge. The full assessment, exact sources and raw receipts are retained with hashes, a current copy manifest, and a portable read-only validator. Root acceptance remains pending until independent integration review.
