# Roth.eval_diag — canonical 94/293

Category: **NO-mathlib-has-it**, subject to independent root acceptance. Existing result: `MvPolynomial.comp_aeval_apply`, `Mathlib/Algebra/MvPolynomial/Eval.lean:612`; its ring-hom counterpart is `MvPolynomial.hom_eval₂` at line 198. These are actual arbitrary-hom evaluation composition laws, with independently checked representation bridges. No new assessment helper is counted as existing mathlib.

## Phase 0 — baseline and scope

The shared baseline `lake build` succeeded with 2467 jobs, no reported warnings/errors. All 17 production source/pin hashes were freshly compared with its manifest and match. See [baseline](../evidence/Roth.eval_diag/baseline-build.txt), [fresh hashes](../evidence/Roth.eval_diag/input-hash-check.json), [inputs](../evidence/Roth.eval_diag/inputs.json). The target resolves at `Roth/CoeffNorm.lean:193`, public theorem, no sorry. The whole declaring module was read: integer coefficient ℓ¹ bounds, Hasse derivatives, diagonal substitution and value estimates. No production, pin, overview, progress or Git changes were made.

Canonical name/order comes directly from tracked declaration-order.json, including private declarations: [snapshot](../evidence/Roth.eval_diag/canonical-snapshot.json), [entry](../evidence/Roth.eval_diag/canonical-entry.json). Parent `Roth.diag` was independently assessed NO-composable-from-mathlib, not NO-mathlib-has-it; no mandatory re-aim verdict gate applies. This assessment independently finds an existing composition law.

## Phase 1 — comprehension

For an integer polynomial P in any set of variables, first substitute the same indeterminate X for every variable, obtaining an integer univariate polynomial. Cast its coefficients to ℝ and evaluate at x. The result equals casting P's coefficients to ℝ and evaluating every variable at x. This is substitution associativity/naturality, not an analytic estimate.

Full native type (univariate names expanded to avoid `open Polynomial` ambiguity):

```lean
∀ {σ : Type u_1} (P : MvPolynomial σ ℤ) (x : ℝ),
  Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (Roth.diag P)) =
    MvPolynomial.eval (fun _ ↦ x) (MvPolynomial.map (Int.castRingHom ℝ) P)
```

Parameters: σ arbitrary universe-polymorphic variable type; P arbitrary finitely supported formal polynomial; x arbitrary real number. There are no hypotheses or Fintype assumption. ℤ/ℝ instances are fixed representations in this statement. The original proof inducts on P, checking constants, sums, multiplication by a variable through `simp_all [diag]`. Conceptually, both sides are ring homomorphisms agreeing on constants and generators. [Original native source](../evidence/Roth.eval_diag/native-original-executed.lean.txt), [receipt](../evidence/Roth.eval_diag/native-original-success.json).

## Phase 2 — preliminary checks

SMALL: helper evaluation identity, not a named/main theorem or new structure. One-line definition-only test: n/a, theorem. Its one-line induction proof is not a glue `rfl` theorem and receives the full workflow. A short theorem proof does not trigger the definition exemption gate.

## Phase 3 — exhaustive literature

Exact requests, returned UTF-8 response hashes/bytes/status, locator URLs and original concise summaries are archived; returned bodies are not archived. No signed/credential-bearing URLs are retained. Query parameters in returned URLs were omitted uniformly; requests remain exact. Sources below support the stated scope, not an invented name for this specialized identity.

| Channel | Actual request / locator | Finding |
|---|---|---|
| General web, specific | `multivariate polynomial diagonal specialization evaluation P t t` | Diagonal evaluation is an instance of substitution; no dedicated standard named theorem found. |
| General web, general | `polynomial substitution evaluation composition universal property commutative semiring` | Universal property/free commutative semiring formulation. |
| General web, alias | `polynomial ring evaluation homomorphism naturality coefficient map` | Evaluation homomorphism/coefficient transport terminology. |
| ChatGPT mathematical MCP | n/a: `ask_chatgpt_math` unavailable | Optional channel absent; remaining channels executed. |
| Local clean.tex | `diagonal`, `point evaluation`, `same variable`, vanishing | §6 Lemma9, lines1503–1522 and1562–1569, identifies diagonal vanishing and separates substitution/evaluation. |
| nLab | `site:ncatlab.org/nlab/show polynomial ring universal property evaluation`; direct `/nlab/show/polynomial` | Definitions and meanings: polynomial ring is free commutative R-algebra on variables. Direct XHTML fetch failed unsupported content type; search excerpt available. |
| nCatLab | `site:ncatlab.org "polynomial" "semiring"`, then `site:ncatlab.org/ncatlab "polynomial" "universal property"`; direct `/ncatlab/show/polynomial` | No dedicated nCatLab entry found; direct URL inaccessible. nLab results are not mislabeled as separate nCatLab sources. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring universal property substitution`; refined exact universal-property query | Lemma98.10.1, tag07XB proof uses arbitrary images of polynomial generators. Direct tag00F0 was checked but is about spectra, not evidence for this identity. |
| MathOverflow | `site:mathoverflow.net polynomial ring evaluation substitution universal property` | Question32133 answer32303 transfers universal polynomial identities by evaluation over any commutative ring. |
| Recent arXiv, five years | `site:arxiv.org polynomial substitution evaluation semiring 2022 2023 2024 2025 2026`; explicit `after:2021-10-27 before:2026-10-28` query | Manjunath arXiv2410.15426 (20Oct2024), equations over polyhedral semirings; Datalog semiring polynomial systems2403.12436. Related scope only, no direct novel diagonal law. |

[Web0](../evidence/Roth.eval_diag/web-0.json), [web1](../evidence/Roth.eval_diag/web-1.json), [web2](../evidence/Roth.eval_diag/web-2.json), [web3](../evidence/Roth.eval_diag/web-3.json), [web4](../evidence/Roth.eval_diag/web-4.json), [web5](../evidence/Roth.eval_diag/web-5.json), [local locator/hash](../evidence/Roth.eval_diag/local-literature-source.json), [local excerpt](../evidence/Roth.eval_diag/local-literature-excerpt.txt).

Primary locators: [Groningen Algebraic Structures, III.2.1](https://www.rug.nl/staff/steffen.muller/lecture_notes_algebraic_structures.pdf), [nLab polynomial, Definitions and meanings](https://ncatlab.org/nlab/show/polynomial), [Stacks07XB](https://stacks.math.columbia.edu/tag/07XB), [MO answer32303](https://mathoverflow.net/questions/32133/expressing-operatornameadja-as-a-polynomial-in-a/32303), [Manjunath2024 abstract](https://arxiv.org/abs/2410.15426).

Literature summary: evaluation/substitution homomorphisms and their universal-property compatibility. The standard ring formulation admits arbitrary coefficient and target rings, arbitrary variable sets and coefficient homomorphisms; free semiring formulations justify dropping subtraction. No historical evolution claim is inferred from search publication metadata. Semiring articles corroborate scope, not the exact identity. The project form is specialized in coefficients/target, and its proof uses neither order nor topology.

## Phase 4a — all parameters and generality

| Parameter / constraint | Current | Broader form | Verified / limitation |
|---|---|---|---|
| σ | Type*, no finiteness | Arbitrary σ | Already general, retained. |
| P | MvPolynomial σ ℤ | MvPolynomial σ R, CommSemiring R | Compiled raw generic proof. This expands the representation; fixed `Roth.diag` itself is ℤ-specific. |
| x | ℝ | S, CommSemiring S | Compiled generic proof; no norm, order, domain, completeness or characteristic assumption. |
| coefficient map | Int.castRingHom ℝ | arbitrary f:R→+*S | Compiled generic proof. No injectivity needed. |
| diagonal substitution | aeval constX | arbitrary g:σ→A followed by φ:A→ₐ[R]B | Already existing `comp_aeval_apply`; ring hom form `hom_eval₂` permits arbitrary coefficient map. |
| Algebra R S | implicit canonical ℤ→ℝ for aeval interpretation | Optional in arbitrary-f raw statement | Compiled raw map/eval version needs no Algebra instance. Algebra version intentionally uses canonical algebraMap. |
| commutativity | fixed commutative rings | commutative semirings | Verified floor for these MvPolynomial APIs; unrestricted noncommutative evaluation would require commuting images and a different interface, not claimed. |

## Phase 4b — generality verdict

STRICTLY NARROWER THAN STANDARD in expanded coefficient/target representation; mechanically replacing `ℝ` alone does not change the fixed ℤ-only `diag` definition. Positive native evidence verifies both arbitrary CommSemiring R,S and arbitrary f, plus Algebra R S form; no unverified weakening is claimed. No Fintype, Nontrivial, IsDomain, CharZero or injectivity assumptions were introduced. The broader law already exists, so this is not a proposal to upstream a new generalized helper.

Raw replacement signature and proof, mathlib-only, protected by `#check_failure Roth.eval_diag` and `#check_failure Roth.diag`:

```lean
variable {σ R S : Type*} [CommSemiring R] [CommSemiring S]
theorem generic (P : MvPolynomial σ R) (f : R →+* S) (x : S) :
    Polynomial.eval x (Polynomial.map f (aeval (fun _ ↦ Polynomial.X) P)) =
      eval (fun _ ↦ x) (map f P) := by
  rw [Polynomial.eval_map, aeval_def, ← eval₂_eq_eval_map]
  change (Polynomial.eval₂RingHom f x) (eval₂ Polynomial.C (fun _ ↦ Polynomial.X) P) = _
  rw [hom_eval₂, Polynomial.eval₂RingHom_comp_C]
  simp only [Polynomial.coe_eval₂RingHom, Polynomial.eval₂_X]
```

[Exact accepted raw code](../evidence/Roth.eval_diag/native-raw-executed.lean.txt), [complete native success](../evidence/Roth.eval_diag/native-raw-success.json). The two initially rejected raw batches are separately archived: missing explicit Polynomial R annotation in the algebraic statement led to unresolved Semiring metavariables. Generic proof already compiled there, but neither whole batch was accepted. No axiom recovery counts as success.

## Phase 4c — nine modern-idiom rows

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Typeclasses rather than preambles? | Yes in expanded form: CommSemiring R,S plus optional Algebra; works over ℕ, quotient rings, positive characteristic, not just integers/reals. |
| 2 | Filters/nets/topology? | No; finite polynomial algebra, no limit statement. |
| 3 | Universal property? | Yes: `comp_aeval_apply` packages uniqueness of evaluation; arbitrary algebra homomorphisms replace redoing polynomial induction. |
| 4 | Bundled substructures? | No set-with-closure predicate here. Bundled AlgHom/RingHom, rather than a new substructure, carries the relevant data. |
| 5 | Field to (semi)ring? | Yes; compiled CommSemiring R,S proof; eliminates irrelevant real-field structure. |
| 6 | Higher categories? | No missing higher-categorical consequence; ordinary hom composition suffices. |
| 7 | Concrete index? | σ already arbitrary; ℤ,ℝ are coefficient/target types rather than index types. Their widening is row5. |
| 8 | Concrete-via-abstract diagnostic? | Fires: source proof body has 0 occurrences of ℤ, ℝ or Int.castRingHom and just one `[diag]` unfolding. Induction only exploits homomorphism behavior. Existing comp_aeval_apply/hom_eval₂ is the abstraction. |
| 9 | False-generalisation guard? | No false generalization in accepted forms. Explicit arbitrary-f form retains f on both sides; Algebra form consistently uses algebraMap. CommSemiring targets preserve intended formal substitution; no claim formal polynomials equal polynomial functions, no arbitrary noncommuting targets. |

Modern idiom available, already in mathlib. The actual downstream example is MainLemma.eval_hasseDeriv_sub_eq_zero, whose proof already uses `comp_aeval_apply` at arbitrary CommRing target S. This is a concrete existing benefit, not speculative categorification.

## Phase 4.5 — infrastructure risks

n/a: theorem introduces no data, instances, reducibility or coercion paths. All six rows separately n/a: typeclass diamonds, reducibility leak, noncanonical unfolding, instance-priority collision, universe-polymorphism infrastructure, coercion ambiguity. Existing-polynomial construction risk is not a new theorem risk.

## Phase 4.6 — five proof-strategy rows

| # | Question | Answer |
|---|---|---|
| 1 | ε–δ vs filters? | No topology. |
| 2 | Element induction vs bundled algebra? | Yes: use existing AlgHom composition evaluation law instead of repeating induction. |
| 3 | Sequences vs nets? | No analysis. |
| 4 | Construction vs universal property? | Yes: hom-evaluation composition expresses the universal-property proof directly. |
| 5 | Missing helpers mathlib should have? | None required: comp_aeval_apply, hom_eval₂, eval/map transport, generator evaluation and ℤ algebra-map normalization already exist. |

REFACTOR-RECOMMENDED: use direct existing evaluation law and representation transport. Cost CHEAP, not a verdict reason. No new helper API justified by the current proof.

## Phase 5 — five ACTUAL mathlib methods

[Raw complete formal search](../evidence/Roth.eval_diag/formal-search.json) includes every exact query and response, including failures/retries. Rows are independently executed on current, standard and abstract forms. External index versions can differ; pinned source and native signatures decide correctness. Local index reports unavailable: returned source-name matches are useful, never proof of absence.

| Method | Current form | Literature form | Abstract form |
|---|---|---|---|
| Finder | diagonal P(X,…,X) eval; related equiv lemmas | hom evaluation naturality: map_eval₂Hom, eval₂_map | comp_aeval / comp_aeval_apply |
| Loogle | `MvPolynomial.eval, Polynomial.eval`: equiv/Fin decomposition related | malformed `_ (_ _)` failed, rate limit retry failed, corrected `MvPolynomial.eval₂, "hom_eval₂"` found exact existing law | `MvPolynomial.aeval, AlgHom.comp`: comp_aeval |
| LeanSearch | diagonal evaluation question: related representations | ring hom commutes with eval: hom_eval₂/map_aeval | composition question: comp_aeval_apply |
| rg pinned sources | eval/diag/eval_toMvPolynomial | hom_eval₂, eval₂_comp_left, eval₂RingHom_comp_C, eval_map | comp_aeval, map_aeval, aeval_def, aeval_X |
| local name | eval_diag returns project target only | hom_eval₂ query returns hom_eval names (index unavailable; not exact match evidence) | comp_aeval returns real source laws |

[Current rg](../evidence/Roth.eval_diag/rg-current.json), [standard rg](../evidence/Roth.eval_diag/rg-literature.json), [abstract rg](../evidence/Roth.eval_diag/rg-abstract.json), [qualified-name rg](../evidence/Roth.eval_diag/rg-full-name.json). Qualified project name not present in mathlib. Conclusion: **found in mathlib as `MvPolynomial.comp_aeval_apply`; more general form**. It allows arbitrary substitution g and arbitrary algebra hom φ, rather than only constant-X followed by evaluation. `hom_eval₂` is the arbitrary-ring-hom version, not an experimental new helper.

Pinned primary signatures:

```lean
MvPolynomial.comp_aeval_apply (g : σ → A) (φ : A →ₐ[R] B) (P : MvPolynomial σ R) :
  φ (MvPolynomial.aeval g P) = MvPolynomial.aeval (fun i ↦ φ (g i)) P
MvPolynomial.hom_eval₂ (P : MvPolynomial σ R) (f : R →+* A)
    (φ : A →+* B) (g : σ → A) :
  φ (MvPolynomial.eval₂ f g P) =
    MvPolynomial.eval₂ (φ.comp f) (fun i ↦ φ (g i)) P
```

All coefficient/intermediate/target types are CommSemiring in the pinned laws; Algebra R A and Algebra R B are needed for the first. [MvPolynomial source](../evidence/Roth.eval_diag/mathlib-source-0.lean.txt), [univariate eval source](../evidence/Roth.eval_diag/mathlib-source-1.lean.txt), [aeval source](../evidence/Roth.eval_diag/mathlib-source-2.lean.txt), [hashes](../evidence/Roth.eval_diag/mathlib-inputs.json).

## Phase 5.5 — three statement-shape checks

Normal forms: (1) old `eval (map f ...)`; (2) `eval₂ f ...`; (3) bundled `aeval` composed with AlgHom. Mathlib already has their equivalences and normalizes composed evaluation to one evaluation on the RHS. Original respects direction but uses a specialized `diag` spelling and explicit coefficient-map wrappers. Canonical theorem for reuse is comp_aeval_apply, with hom_eval₂ when f is arbitrary.

Syntactic-generality attempts: compiled arbitrary-f old map/eval statement and Algebra R S aeval statement. Prefer latter when an Algebra instance is available, former when caller owns arbitrary f. For original ℤ→ℝ case, cast/algebraMap transport is required, not definitional equality falsely asserted. No extensionality theorem is offered without its normalization premise.

Superfluous-argument audit: σ necessary for variable type, P necessary as evaluated input, x necessary for point. No explicit hypotheses/typeclasses to drop in original. Fixed ℤ and ℝ can be widened in expanded representations; arbitrary CommSemiring R,S required for the chosen APIs. Algebra is needed only by the aeval interface and intentionally absent from arbitrary-f version.

Verdict: normal form REFACTOR; syntactic generality RESTATE to existing law; superfluous arguments NONE; RESTATE-BEFORE-SHIP if considering upstream. No new statement needs shipping.

## Phase 6.0 — callers and inline audit

Internal explicit named use count **0**, external-to-file files **0**. The sole textual `eval_diag` occurrence is its declaration; no simp attribute exports it implicitly. Full canonical ordered audit requests293, unique293, present293, values293, and finds **0 direct proof consumers**. This is direct constant inspection only, not transitive kernel/simp closure. Exact canonical order, not merely count, is validated.

| Caller / inline site | Kind and plan |
|---|---|
| No named caller | No replacement at any explicit named call site is needed. Delete theorem locally in a later authorized refactor. |
| Roth/MainLemma.lean:409, `Roth.eval_hasseDeriv_sub_eq_zero` | Inline derivation of the same law after HasseDeriv transport, over arbitrary CommRing S. It already uses comp_aeval_apply and aeval_X. Keep that proof; no conversion to narrow eval_diag. Its full theorem replay verifies the broader existing route. |

[Named grep](../evidence/Roth.eval_diag/rg-callers.json), [inline grep](../evidence/Roth.eval_diag/rg-inline.json), [whole relevant inline source module](../evidence/Roth.eval_diag/source-inline.lean.txt), [caller metadata](../evidence/Roth.eval_diag/callers.json), [canonical native source](../evidence/Roth.eval_diag/native-consumers-executed.lean.txt), [canonical native success](../evidence/Roth.eval_diag/native-consumers-success.json).

This is unused named project API whose substantive compatibility law is actually used through the more general mathlib abstraction. Zero named references alone is not taken as proof of uselessness or mathematical absence.

## Phase 6 — actual composition experiments

Attempt1, original induction replaced by generic hom_eval₂: accepted raw proof above and original specialization compile. Named uses: Polynomial.eval_map, MvPolynomial.aeval_def, MvPolynomial.eval₂_eq_eval_map, MvPolynomial.hom_eval₂, Polynomial.eval₂RingHom_comp_C, Polynomial.coe_eval₂RingHom, Polynomial.eval₂_X. Seven distinct mathlib names plus unfolding Roth.diag in original; this is not claimed to be a ≤3-call old-form composition. The experimental generic helper is not existing mathlib.

Attempt2, actual stronger existing theorem: specialize `comp_aeval_apply` at A=Polynomial ℤ, B=ℝ, g=const X and φ=Polynomial.aeval x. Generator evaluation yields x; existing eval-map/aeval-def and algebraMap-int transport recover exactly the source statement. Accepted direct proof uses one existing substantive law with explicit representation normalizers; full source/receipt preserved. It neither performs fresh polynomial induction nor relies on eval_diag or a downstream helper. Logical one-command specialization (formatted for reading):

```lean
simpa only [Polynomial.eval_map, MvPolynomial.eval_map, ← algebraMap_int_eq,
  ← Polynomial.aeval_def, ← MvPolynomial.aeval_def, Roth.diag, Polynomial.aeval_X] using
  (MvPolynomial.comp_aeval_apply (fun _ ↦ (Polynomial.X : Polynomial ℤ))
    (Polynomial.aeval x : Polynomial ℤ →ₐ[ℤ] ℝ) P)
```

The exact accepted normalization above rewrites towards aeval, including the non-definitional cast/algebraMap bridge. Two rejected disk batches first normalized forward and left generator/cast mismatches, then added eval₂_X but still left the cast mismatch; neither is accepted evidence. There is no claim the seven normalizers are zero calls: they are representation/generator conversions around a stronger already-existing law. A bare `simp [defs...]` would be Phase6b **trivial simp composition**, BORDERLINE in isolation. Here `using comp_aeval_apply` identifies and verifies a genuine more-general mathematical law; this distinction supports NO-mathlib-has-it rather than NO-composable-from-mathlib. No artificial ≤3 count is assigned. There is no failed-search proof of absence.

## Phase 7 — verdict and actionable plan

**NO-mathlib-has-it.** The canonical composition-of-evaluation law already exists as `MvPolynomial.comp_aeval_apply` in `Mathlib/Algebra/MvPolynomial/Eval.lean:612`, with generic ring-hom law hom_eval₂:198. The old spelling follows by the verified direct specialization and existing notation bridges; the seven normalizers are recorded honestly. It adds no new general mathematical law or modernization: the abstraction is already present and used in MainLemma. No parent verdict is inherited, no cost-based downgrade used.

Refactor plan at every explicit named caller: there are **0**, so no named call edits. Remove `Roth.eval_diag` in a later implementation change; maintain existing MainLemma:409 proof which already targets arbitrary CommRing S via comp_aeval_apply. If a future caller wants the old ℤ/ℝ map/eval shape, use the exact direct specialization above; if it owns an arbitrary coefficient hom f, use hom_eval₂ with eval₂RingHom_comp_C and eval-map bridges. For local readability a theorem could remain in `Roth/CoeffNorm.lean` as a downstream convenience wrapper, but that does not establish an upstream gap. No Archive destination is necessary for a duplicate universal law.

NO verdict means upstream file/PR title/reviewer selection and YES grouping checklist are n/a; [accepted YES/parent snapshot](../evidence/Roth.eval_diag/accepted-yes-grouping.json) was freshly read, not inferred from names. Verification failures are preserved as rejected evidence and do not enter accepted proof checks.

## Phase 8 — handoff and verification

All mandatory phases completed with justified theorem n/a, no unresolved mathematical or verification items. [Assessment](../evidence/Roth.eval_diag/assessment.json), [verification index](../evidence/Roth.eval_diag/verification.json), [generality rows](../evidence/Roth.eval_diag/generality.json), [portable read-only validator](../evidence/Roth.eval_diag/validate.py). Current copy-manifest is authoritative in scratch and integrated layouts; historical worker-copy-manifest is never substituted. Root acceptance remains pending until independent review. Production files/pins/Git untouched.
