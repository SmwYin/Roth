# Roth.exists_det_eq_mul — full assessment (canonical 178)

Verdict: **YES-but-generalise-first**, reason MODERN-IDIOM, with a fully proved stronger theorem. Replace the integer coefficient specialization by a characteristic-zero normalized GCD domain and remove `Finite τ`. Preserve the distinguished variable, individual Hasse operators, every witness bound, both nonzero factors, both degree conclusions and the exact determinant identity.

## Phase 0 — Doctor

The shared successful `lake build` completed 2467 jobs without warnings. All 17 production-source/pin hashes freshly match that baseline; see [baseline receipt](../evidence/Roth.exists_det_eq_mul/baseline-build.txt), [manifest](../evidence/Roth.exists_det_eq_mul/input-manifest.json) and [fresh hashes](../evidence/Roth.exists_det_eq_mul/source-hashes.json). The target resolves at Roth/Separation.lean:542, with no sorry or nonstandard axiom. Entire declaring module and complete sole source caller were read. The required full completed-module `lake build` also passed now: exit0,2467jobs,5.592seconds; all17inputs unchanged. [Completion build](../evidence/Roth.exists_det_eq_mul/separation-file-completion-2026-10-27.json), [exact build log](../evidence/Roth.exists_det_eq_mul/separation-file-completion-2026-10-27.log).

## Phase 1 — Comprehend

For a nonzero integer polynomial in a distinguished variable and a family of other variables, choose an integer `1 ≤ l ≤ r none + 1` and individual Hasse operators on the other variables of orders bounded by their row indices. Their mixed-derivative determinant factors into nonzero integer polynomials in the two disjoint groups of variables. Each factor has individual degree at most `l` times the corresponding bound for the original polynomial.

Full native type (all actual binders; no inherited Fintype or DecidableEq):

```lean
∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ},
  P ≠ 0 →
    ∀ {r : Option τ → ℕ},
      (∀ (j : Option τ), degreeOf j P ≤ r j) →
        ∃ (l : ℕ),
          1 ≤ l ∧
            l ≤ r none + 1 ∧
              ∃ (D : Fin l → τ →₀ ℕ),
                (∀ (μ : Fin l), Finsupp.degree (D μ) ≤ ↑μ) ∧
                  ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ),
                    U ≠ 0 ∧
                      V ≠ 0 ∧
                        (∀ (j : τ), degreeOf j U ≤ l * r (some j)) ∧
                          V.natDegree ≤ l * r none ∧
                            (Matrix.of fun (μ ν : Fin l) ↦
                                  (hasseDeriv (Finsupp.mapDomain some (D μ) + Finsupp.single none ↑ν)) P).det =
                              (rename some) U * (Polynomial.aeval (X none)) V
```

`τ` indexes the other variables, `[Finite τ]` supports the old generalized Wronskian selection proof, `P` is the input and `hP` its nonvanishing. `r` is a natural individual-degree bound and `hr` supplies every component. `l`, `D`, `U`, and `V` are existential outputs, not inputs. [Full module](../evidence/Roth.exists_det_eq_mul/declaring-module.lean.txt), [full caller](../evidence/Roth.exists_det_eq_mul/full-source-caller.lean.txt), [native type](../evidence/Roth.exists_det_eq_mul/native-type.json).

Proof: `exists_rat_factors_det_hasseDeriv_aux` maps to ℚ, applies `exists_separated_representation`, then `exists_genWronskian_ne_zero` and `wronskian_ne_zero_of_linearIndependent`. `det_hasseDeriv_separated` identifies the determinant with their product. `exists_int_factors` descends the factors to ℤ. `degreeOf_rename_mul_aeval` and `degreeOf_none_rename_mul_aeval`, followed by `degreeOf_det_hasseDeriv_le`, supply both bounds. This is substantive Wronskian selection and arithmetic descent, although the final public proof has only 14 substantive lines.

## Phase 2 — Preliminary checks

BIG: a named main result in the module docstring and Lemma2 of the source. One-line definition/exemption test: n/a, declaration is a theorem. A short final assembly from new project lemmas is not a composition of existing mathlib calls.

## Phase 3 — Exhaustive literature

Exact requests, response SHA256/byte counts/status, primary locators and original concise summaries are retained; full web bodies are not archived. [Web1](../evidence/Roth.exists_det_eq_mul/web-1.json), [web2](../evidence/Roth.exists_det_eq_mul/web-2.json), [web3](../evidence/Roth.exists_det_eq_mul/web-3.json), [web4](../evidence/Roth.exists_det_eq_mul/web-4.json), [web5](../evidence/Roth.exists_det_eq_mul/web-5.json).

| Channel | Actual query or locator | Finding |
|---|---|---|
| General web, specific | Roth theorem lemma generalized Wronskian polynomial determinant U V integral factors | Soundararajan–Petrow §17 constructs exactly this separated nonzero derivative determinant. |
| General web, general | generalized Wronskian separation of variables polynomial determinant characteristic zero field | Polynomial independence and characteristic-zero Wronskians; no claim of explicit GCD-domain version in those notes. |
| General web, aliases | Roth auxiliary polynomial separation lemma differential operators disjoint variables | Classical Roth auxiliary polynomial/index proof, distinct from arbitrary matrix factorization. |
| ask_chatgpt_math | standard form, generality, historical evolution | n/a: optional mathematical second-opinion tool unavailable; no fabricated request. |
| Local reference | clean.tex §2 Lemma `roth:lem2`, proof and implementation note | Exact integral statement, separated basis, Wronskian nonvanishing, primitive rescaling. [Excerpt](../evidence/Roth.exists_det_eq_mul/local-literature.txt). |
| nLab | site:ncatlab.org/nlab Wronskian determinant polynomial separation | Standard determinant definition. Direct page open failed unsupported XHTML; search response supplies definition. |
| nCatLab | site:ncatlab.org/ncatlab generalized Wronskian polynomial determinant; retry site:ncatlab.org/ncatlab Wronskian | Returned nLab and other out-of-namespace results. No exact nCatLab mathematical hit; not treated as evidence of absence. |
| Stacks | site:stacks.math.columbia.edu Gauss lemma primitive polynomial fraction field | Tag00H7 lies in Going down for integral over normal and states that an integral element over a normal domain has its minimal polynomial coefficients in the domain. Contextual near miss only; it does not supply primitive separated-product descent or bounded derivative selection. |
| MathOverflow | site:mathoverflow.net generalized Wronskian characteristic zero polynomials | “The total Wronskian,” 342982, concerns a prescribed all-jets matrix and analytic powers, not this admissible row-selection/factorization statement. |
| Recent arXiv | generalized Wronskian polynomial Roth after:2021-10-27 before:2026-10-28; Hasse derivative polynomial determinant with same bounds | 2511.03848 (2025), 2607.26039 and2605.27305 (2026) concern generalized Wronskians, Jacobi identities and degree growth. No exact separation theorem in inspected abstracts. Historical1310.4683 and March2021 paper are not counted as within five years. |

The Stanford primary course notes successfully open; UCL mirror returns404. §17, pp.62–63 supplies the classical minimal separated expansion, multiplication of ordinary/generalized Wronskians and rational-to-integral factor control. Stacks00H7 was inspected as a contextual near miss and is not cited as support for the separated-product Gauss step. Standard literature here states integer/rational versions for Diophantine applications. The characteristic-zero field argument and GCD-domain descent are a proved algebraic abstraction of that construction, not an assertion that every source states that abstraction. Primary sources: [Soundararajan–Petrow](https://math.stanford.edu/~ksound/TransNotes.pdf), [Stacks00H7](https://stacks.math.columbia.edu/tag/00H7), [Kiselev2025](https://arxiv.org/abs/2511.03848).

## Phase 4a — Parameter/generality audit

| Parameter/hypothesis | Role and result |
|---|---|
| `τ : Type*` | Arbitrary universes retained. No nonempty or ≥2-variables assumption is needed; stronger than the source's finite `p ≥ 2` presentation. |
| `[Finite τ]` | Removed by the complete finite-family support/rename proof `DetFactors178Support.arbitrary_variables`; each polynomial uses only finitely many variables. The old literal proof does need this instance. |
| `ℤ` coefficients | Replace by `[CommRing R] [IsDomain R] [NormalizedGCDMonoid R] [CharZero R]`. Use `FractionRing R` internally. Complete proof preserves both factor bounds and exact identity. No unproved arbitrary-domain descent claim. |
| `P ≠ 0` | Essential: with `l ≥ 1` the zero derivative matrix has zero determinant and cannot be a product of nonzero separated factors in a domain. Native semantic guard verifies this: [exact executed source](../evidence/Roth.exists_det_eq_mul/det-factors178-semantic-executed.lean.txt), [complete receipt](../evidence/Roth.exists_det_eq_mul/det-factors178-semantic-receipt.json). |
| `r : Option τ → ℕ` | Natural nonnegative exponents/degrees are appropriate; arbitrary additive-group indices lose polynomial/order content. |
| `hr : ∀ j, degreeOf j P ≤ r j` | Every component enters its corresponding bound. Setting `r j := degreeOf j P` gives a sharp-input corollary, but explicit upper bounds compose directly with RSet. |
| Distinguished `none`/`some` split | Preserves disjoint variable groups. An equivalence can transport arbitrary chosen coordinates; allowing overlapping groups is a different and generally false factorwise differentiation claim. |
| CharZero and GCD/domain structure | CharZero supports field Wronskian nonvanishing; domain supports fraction field/injective mapping and degree equalities; normalized gcd supports primitive factor descent. No stronger PID/UFD assumption is required. No claim these are a necessary characterization of all coefficient rings. |

## Phase 4b — Verified restatement

STRICTLY NARROWER than the verified modern algebraic form: literal integer coefficients and Finite τ can be removed. Both the arbitrary-variable proof over an abstract fraction field and the canonical `FractionRing R` theorem compile completely. The latter signature is:

```lean
variable {τ R : Type*} [CommRing R] [IsDomain R] [NormalizedGCDMonoid R] [CharZero R]
theorem exists_det_eq_mul_gcd_domain {P : MvPolynomial (Option τ) R} (hP : P ≠ 0) {r : Option τ → ℕ}
    (hr : ∀ j, degreeOf j P ≤ r j) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ),
      (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
        (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧
        (Matrix.of fun μ ν : Fin l ↦
            hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det = rename some U *
          Polynomial.aeval (X none : MvPolynomial (Option τ) R) V
```

The isolated proof contains full copied foundational developments and the generalized factor-descent proof, with `#check_failure Roth.exists_det_eq_mul` and a guard that the project's multivariate Hasse definition was initially absent. It imports only mathlib. The project proof uses existing foundational definitions at their valid types: `MvPolynomial.hasseDeriv` over R and Wronskian APIs over the field `FractionRing R`. It does not try to interpret the Field-hardwired `Roth.genWronskian` over R. Consequently no foundational definition must be replaced to state this theorem; the same mathematical objects appear in the ℤ specialization. This avoids the “generalise-first by guessing a multi-file foundational rewrite” false positive.

The supporting degree determinant helper weakens ℤ to CommRing R with the same eight-line proof. The complete GCD scalar, primitive representative and separated factor descent proofs are new candidate API, not existing mathlib calls. The full support bridge similarly is new proof. These previously assessed dependencies retain their independent verdicts; this verdict is not inherited. All exact accepted sources and native receipts are listed in [verification](../evidence/Roth.exists_det_eq_mul/verification.json).

## Phase 4c — Nine modern-idiom checks

| # | Question | Answer and concrete downstream consequence |
|---|---|---|
|1| Typeclasses instead of preambles | Yes: abstract characteristic-zero normalized GCD domain, using existing Algebra/IsFractionRing infrastructure. Specializes to ℤ and other arithmetic polynomial coefficient rings. |
|2| Filters/nets instead of sequences | No topology or convergence appears. |
|3| Universal property instead of construction | FractionRing and IsFractionRing express the coefficient localization; external-K generic theorem works for any witness, canonical corollary hides that choice. |
|4| Bundled substructure instead of closure set | Existing `Submodule.span` and `Module.Basis` already organize the finite coefficient space. No custom structure needed. |
|5| Hierarchy weakening | Yes: ℤ-specific arithmetic replaced by GCD-domain descent; field remains only for independence and Wronskians. `IsLocalization.exists_integer_multiple`, `surj_of_gcd_domain` compose. |
|6| Higher categories | No categorical content or downstream gain. |
|7| Concrete index abstraction | Fin l fixes simultaneous row/order bounds; keep ℕ degree and row order. Removing Finite τ is valuable, replacing ℕ by arbitrary groups is not. |
|8| Concrete-via-abstract diagnostic | Yes. The original main proof contains zero ℤ or ℚ tokens after its signature: it invokes abstract-purpose factor descent and degree lemmas. Full dependency expansion confirms only characteristic-zero fraction-field and GCD-domain properties; native proof verifies the abstraction. |
|9| False-generalisation guard | Pass for proposed R/arbitraryτ version: preserves every conjunct and ℤ specializes directly. Reject blanket arbitrary characteristic: the first Hasse derivative of X² over ZMod2 vanishes; no complete positive-characteristic existence claim is made. Reject overlapping variable groups. |

Modern idiom available: yes; mathematical gain is exact arithmetic descent over normalized GCD domains plus arbitrary ambient variables, using localization and finite support. Proof adjustment cost MODERATE; cost does not determine the verdict.

## Phase 4.5 — Infrastructure risks

n/a: theorem, no new definition, class, instance or coercion. The six definition-only checks (diamond, reducibility leak, noncanonical unfolding, instance priority, universe constraints, coercion ambiguity) introduce no new paths. Proof-local finite-support and scalar-extension instances are scoped; canonical FractionRing removes a superfluous public K parameter.

## Phase 4.6 — Five proof-strategy checks

| # | Check | Finding |
|---|---|---|
|1| Topology ε–δ/filter | n/a algebraic finite determinant. |
|2| Elements vs submodules | Existing separated-representation proof uses a basis of the coefficient submodule; factor integrality uses primitive coefficients, not ad hoc real analysis. |
|3| Sequences vs nets | n/a no limits. |
|4| Construction vs universal property | Algebra/IsFractionRing plus canonical FractionRing already give the appropriate coefficient-extension interface. |
|5| Missing helper API | Yes: finite-family Hasse Wronskian criterion, arbitrary-variable support bridge, normalized-GCD separated factor descent, generic degree bound for determinant of Hasse derivatives. |

MATHLIB-IDIOMATIC assembly, with REFACTOR-RECOMMENDED upstream layering: first establish those reusable helpers in their algebraic modules, then this synthesis as a leaf. The isolated long source is verification scaffolding copying dependencies, not a proposed single1300-line theorem proof. No numerical approximation, analytic differentiation or ad hoc integer denominator product is needed in the generic proof.

## Phase 5 — Actual five-method search on three forms

| Form | Finder | Loogle | LeanSearch | rg pinned tree | local names |
|---|---|---|---|---|---|
| Current ℤ determinant/factors/bounds | Full sentence in search-current-finder | `MvPolynomial, Matrix.det` | Same full sentence | Full qualified/short name and det_hasseDeriv | exists_det_eq_mul |
| Literature Roth separation/ Wronskians | Full sentence in search-standard-finder | `Polynomial.hasseDeriv, Matrix.det` | Same full sentence | wronskian/Wronskian/separated_representation | wronskian |
| Abstract GCD/fraction-field form | Full sentence in search-abstract-finder | `IsFractionRing, MvPolynomial` | Same full sentence | localization/injectivity/degree/determinant variants | exists_int_factors |

All15 cells executed:12 external/name API calls plus3 complete source searches. [Current Finder](../evidence/Roth.exists_det_eq_mul/search-current-finder.json), [standard Loogle](../evidence/Roth.exists_det_eq_mul/search-standard-loogle.json), [abstract LeanSearch](../evidence/Roth.exists_det_eq_mul/search-abstract-leansearch.json), [current rg](../evidence/Roth.exists_det_eq_mul/rg-current.json), [standard rg](../evidence/Roth.exists_det_eq_mul/rg-standard.json), [abstract rg](../evidence/Roth.exists_det_eq_mul/rg-abstract.json). Other exact query/complete response receipts are in the copy manifest. Local name search explicitly reports index unavailable, returning lexical source matches including scratch/project names. These are not mathlib hits; index unavailability is not absence evidence. External indices may differ from the pin.

Inspected positive matches:

- `Polynomial.hasseDeriv`, `.hasseDeriv_mul` supply univariate operators, not multivariate bounded row selection.
- `Polynomial.wronskian` and `IsCoprime.wronskian_eq_zero_iff` treat two univariate polynomials; the pinned file TODO explicitly requests n-tuples. This is a concrete missing API anchor for the selection prerequisites.
- `Matrix.det_mvPolynomialX_ne_zero` concerns independent matrix indeterminates; evaluating them at derivatives can kill the determinant. It cannot select the D μ.
- `Matrix.det_mul`, `Matrix.det_transpose`, `AlgHom.map_det` prove multiplicative determinant transport once a matrix product and independent families are supplied. They do not supply the representation, order-bounded nonvanishing or integral factors.
- `IsLocalization.exists_integer_multiple`, `surj_of_gcd_domain`, `IsFractionRing.injective`, `degrees_map_of_injective`, and `Polynomial.natDegree_map_eq_of_injective` are genuine coefficient extension/descent building blocks. Constructing the two nonzero separated factors, all witness bounds and degree control still requires the full proof.
- Jacobian and universal-factorization search hits concern presentations with derivative independence or resultants, not derivative-row existence for one input polynomial. They were rejected by inspected statement shape, not silently equated with the target.

Pinned source archives and hashes: [mathlib inputs](../evidence/Roth.exists_det_eq_mul/mathlib-inputs.json). Native signatures and direct-call experiments appear in verification. Conclusion: positive partial matches/building blocks; **no verified ≤3 existing-call replacement**. This is not a theorem of global library absence.

## Phase 5.5 — Statement shape

Normal forms compared: an explicit separated product in `MvPolynomial (Option τ) R`; a univariate polynomial over `MvPolynomial τ R` via `optionEquivLeft`; and a tensor/pure-rank-one description. Keep the explicit product normal form for the determinant theorem: the caller needs factors and separate degree bounds, and the degree/evaluation API already applies. The result is existence rather than an equivalence; RHS remains the canonical separated product.

Syntactic alternatives attempted: chosen external fraction field K versus canonical FractionRing R; finiteτ versus arbitraryτ; degree inputs `r` versus actual degrees. Native canonical/arbitraryτ theorem is chosen to avoid unnecessary K and Finite arguments while preserving `hr` for direct RSet application. All conjuncts are used downstream. Superfluous old assumption: Finite τ only; Fintype/DecidableEq were already omitted in the original. Integer specialization becomes a one-call application of the new theorem. `hP` and every component of `hr` remain. Overall RESTATE-BEFORE-SHIP as the exact generic signature above.

## Phase 6.0 — Complete callers and inline audit

Internal external-to-file use count **1**, in **1** file:

| Caller | Source use | Refactor |
|---|---|---|
| Roth.index_le_lem6, Roth/Theta.lean:556 (call571) | obtain l, all D/U/V/nonzero/degree/identity conjuncts from exists_det_eq_mul hR.1 hR.2.1 | Apply the generalized theorem with R=ℤ; no caller hypotheses or proof structure change. Full caller replay compiled. |

Fresh scoped `rg --no-ignore` and independent tracked-source `git grep` agree. [rg](../evidence/Roth.exists_det_eq_mul/callers.json), [git grep](../evidence/Roth.exists_det_eq_mul/git-callers.json), [inline audit](../evidence/Roth.exists_det_eq_mul/inline-audit.json). No independent inline rederivation was found; the private rational helper omits integral factors and degree conclusions and is an upstream construction prerequisite, not a competing full theorem. Module docstrings and declaration occurrences are not calls. Exact293-order kernel-value audit separately identifies the same direct consumer; source and kernel consumer meanings remain distinct. The imported full caller never supplies the generic proof, and the isolated generic proof imports neither target nor caller.

## Phase 6 — Composition experiments

Attempt1: `Matrix.det_mul`/`det_transpose` after a hypothetical matrix product. Native negative exact-call guards reject them on the complete current-form existential statement. Missing premises: separated basis, nonzero Wronskians, bounded D and arithmetic descent.

Attempt2: `IsLocalization.exists_integer_multiple` on P. Native direct-call guard rejects it; its conclusion is a single coefficient-extension scalar relation. It supplies none of l/D/U/V with their conjunction of bounds.

Attempt3: compose `exists_separated_representation`, `exists_genWronskian_ne_zero` and `exists_int_factors`. These are project/new lemmas, and additional determinant transport, nonvanishing, degree comparisons and finite-support proof are required; they are not three existing mathlib calls. Full generic proof and complete caller provide the positive composition experiment, explicitly labeled as a new proof.

Conclusion: **no verified ≤3 existing-call replacement** in the assessed sense (NOT-COMPOSABLE as a workflow label only). Failed search/negative probes do not prove mathematical impossibility; no claimed closing simp composition was found.

## Phase 7 — Actionable verdict

**YES-but-generalise-first**, MODERN-IDIOM. The concrete missing theorem is bounded-order Hasse determinant separation with **nonzero factors over the original normalized GCD domain and controlled individual degrees**. The n-tuple Wronskian TODO and existing localization APIs anchor the missing prerequisites. The literature supplies a substantive Roth construction, and the full native proof supplies the precise wider coefficient/ambient-variable form. A single consumer is weak evidence by count, but it uses every output and connects determinant nonvanishing, coefficient bounds, separated index estimates and induction; it is not dispensable glue.

Proposed upstream leaf: **Mathlib/RingTheory/MvPolynomial/Separation.lean**, importing the proposed Algebra/MvPolynomial/Separation decomposition leaf, RingTheory/MvPolynomial/Wronskian selection leaf and RingTheory/MvPolynomial/GaussLemma descent leaf. Keep this higher-import arithmetic determinant synthesis out of foundational MvPolynomial/Eval and out of the lower-level algebraic decomposition file. Proposed title: **feat(MvPolynomial): bounded Hasse determinants with separated factors**.

Grouping/sequencing: accepted YES `Roth.exists_separated_representation`, `Roth.exists_genWronskian_ne_zero`, `Roth.genWronskian`, `Roth.exists_primitive_smul_eq`, and `Roth.exists_int_factors` are prerequisites for focused upstream PRs, followed by this leaf theorem. They are read from current tracked progress, [accepted grouping](../evidence/Roth.exists_det_eq_mul/accepted-grouping.json). The separately borderline determinant convenience identity is not silently promoted to accepted YES; integrate its necessary identity using the existing determinant API and the separately assessed factorwise Hasse rule.

Pre-PR actions:

- `/generalise Roth.exists_det_eq_mul`: adopt the exact fully proved arbitraryτ normalized-GCD/CharZero statement; canonical FractionRing hides the auxiliary K. No pending mathematical proof or user question remains.
- `/cleanup Mathlib/RingTheory/MvPolynomial/Separation.lean MvPolynomial.exists_det_eq_mul`: choose final descriptive name, public namespace and imports; keep generic degree bound separate and construction helpers private where appropriate.
- `/pre-submit` after the layered upstream implementation is cleaned and verified.
- Reviewers from actual relevant recent commits: **Justus Springer** (e4c37418a1 primitive mem_lifts; f10bf357d0 localization normalization) and **Junyan Xu** (2f35248703 normalized-gcd hierarchy weakening); see [focused history](../evidence/Roth.exists_det_eq_mul/reviewers-focused.json). These are candidates, not assignments or availability claims.

Alternative local destination pending upstreaming: retain Roth/Separation.lean as the arithmetic leaf used by Roth.index_le_lem6. Do not delete/invent inline mathlib calls at the sole caller; once upstreamed replace its call by the generic theorem at R=ℤ. No production, pins, Git state, overview or progress files were edited by this worker.

## Phase 8 — Verification and handoff

[Verification index](../evidence/Roth.exists_det_eq_mul/verification.json) preserves exact executed sources and complete raw native/formal-search receipts, including separately rejected attempts. Accepted native checks require complete success, no partial/warming response, no errors/warnings/recovered sorry, and only propext/Classical.choice/Quot.sound. Original native #print is not elided; the full type and ordered293 kernel audit are retained. [Portable validator](../evidence/Roth.exists_det_eq_mul/validate.py) checks current manifest bytes/hashes, baseline/pinned sources, required keys/phases, exact canonical order, native diagnostics and links, then invokes the credential guard. The full project completion build has passed; root independently accepts before publishing completion178.
