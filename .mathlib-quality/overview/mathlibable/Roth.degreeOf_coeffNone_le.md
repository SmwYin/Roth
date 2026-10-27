# Roth.degreeOf_coeffNone_le — BORDERLINE-needs-human

Declaration157/293, `Roth/Separation.lean:114`. Complete read-only assessment; two future upstream API questions remain, with no unresolved verification or required user input. No production or Git changes.

## Phase 0 — Doctor

The full declaring module was read, including separated representation, its three private linear algebra auxiliaries, domain degree identities, integrality and the final determinant theorem. The module separates a distinguished variable before constructing Roth's determinant factors. Original declaration resolves and contains no placeholder. The successful full build (2467 jobs, exit0) is reused only after freshly matching all17 source/pin hashes against the shared manifest. The current full-build receipt also matches these fresh inputs. [Baseline](../evidence/Roth.degreeOf_coeffNone_le/baseline-build.txt), [fresh hashes](../evidence/Roth.degreeOf_coeffNone_le/inputs.json), [full build receipt](../evidence/Roth.degreeOf_coeffNone_le/index-file-completion-2026-10-27.json), [whole module](../evidence/Roth.degreeOf_coeffNone_le/Roth-Separation.lean.txt).

## Phase 1 — Comprehend

Collect a polynomial in powers of one distinguished variable. Each coefficient is a polynomial in the remaining variables. Its degree in any one remaining variable is at most the original polynomial's degree in that same variable. The statement covers zero polynomials and absent coefficients; it requires neither a degree restriction on the selected power nor nonzero/domain hypotheses.

Full native elaborated type:

```lean
@Roth.degreeOf_coeffNone_le : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (P : MvPolynomial (Option τ) R) (ν : ℕ) (j : τ),
  MvPolynomial.degreeOf j (Roth.coeffNone P ν) ≤ MvPolynomial.degreeOf (some j) P
```

`τ` is an arbitrary variable type; `R` a commutative semiring; `P` the polynomial; `ν` the distinguished exponent; `j` the remaining coordinate. There are no `Fintype τ` or `DecidableEq τ` arguments despite the ambient module section. The only project dependency is the coefficient alias in the statement. The proof's mathematical inputs are all mathlib support and degree facts.

The proof converts the degree conclusion to bounds on supported monomials. Coefficient support inserts exponent `ν` at `none`. The inserted monomial belongs to `P.support`, so its `some j` exponent is bounded by `degreeOf (some j) P`; evaluation of the inserted exponent at `some j` recovers the original exponent at `j`. The latter is actual rewriting, not a definitional representation bridge. [Native type](../evidence/Roth.degreeOf_coeffNone_le/native-type.json), [original and exact293 audit receipt](../evidence/Roth.degreeOf_coeffNone_le/coefficient-degree-original-audit-receipt.json). The complete native kernel print has no elision marker and uses only the three standard axioms.

## Phase 2 — Preliminary checks

SMALL: an individual degree bookkeeping lemma, not a new structure, named theorem or module main result. The definition-only one-line filter is n/a because this is a theorem. Its three source proof lines do not establish a three-call composition: they include support-wise introduction and a `simpa` normalization. Literature and all later phases still run in full.

## Phase 3 — Exhaustive literature

Each row records the actual request, status, response hash/bytes, returned titles and locators, and an original concise summary. Full returned web bodies are not archived. Credential-bearing URL queries are sanitized before freeze. The protocol's informal nine-channel label is not treated as a reason to invent an additional channel: all named channels and three general queries were executed.

| Channel | Actual query / locator | Result and limitation |
|---|---|---|
| Specific web | `multivariate polynomial coefficient polynomial degree in remaining variable bounded degree` | MathWorks `coeffs` and degree documentation; coefficient polynomials in remaining variables, ordinary individual degree. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-web-specific.json) |
| General web | `polynomial collecting powers one variable coefficient individual degree bound` | Polynomial presentations and extraction terminology; no additional assumptions suggested. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-web-general.json) |
| Alias web | `coefficient extraction partial degree multivariate polynomial support projection` | Support/partial-degree terminology and computational APIs. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-web-alias.json) |
| ChatGPT mathematical MCP | Standard form, generality, historical evolution | n/a: `ask_chatgpt_math` unavailable; not replaced with an invented consultation. |
| Local reference | `collecting\|psi\|degree at most\|r_j` in `clean.tex` | §2 proof of Lemma2, line374, explicitly bounds the coefficient polynomials' degrees in remaining variables. [Exact local search](../evidence/Roth.degreeOf_coeffNone_le/local-literature-search.json), [excerpt](../evidence/Roth.degreeOf_coeffNone_le/clean-separation-excerpt.tex.txt) |
| nLab | `site:ncatlab.org/nlab polynomial degree coefficient ring` | Polynomial context, no exact coordinate bound located; direct polynomial-page fetch failed400 unsupported XHTML content. [Search](../evidence/Roth.degreeOf_coeffNone_le/literature-nlab.json), [access](../evidence/Roth.degreeOf_coeffNone_le/literature-access.json) |
| nCatLab | `site:ncatlab.org/ncatlab polynomial coefficient degree` | Explicit distinct namespace queried; returned out-of-namespace pages are not evidence of an exact in-namespace law. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-ncatlab.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial coefficients degree variables` | General polynomial-ring coefficient context; no exact coordinate extraction law located. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-stacks.json) |
| MathOverflow | `site:mathoverflow.net multivariate polynomial coefficient degree bound` | Numeric coefficient magnitude bounds and other degree questions; distinguish these from degree of a coefficient polynomial. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-mo.json) |
| Recent arXiv | `site:arxiv.org multivariate polynomial partial degree coefficients 2021 2022 2023 2024 2025 2026` | Noisy results include older papers; not passed off as a five-year exact hit. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-arxiv.json) |
| Supplementary recent arXiv refinement | `site:arxiv.org/abs "individual degree" "2024" "polynomial"` | Chuyoon–Shpilka2026 and Bhargava et al.2024 give current individual-degree applications; contextual, not exact coefficient-law attribution. [Receipt](../evidence/Roth.degreeOf_coeffNone_le/literature-recent.json) |

Primary sources: [MathWorks coefficient examples](https://www.mathworks.com/help/symbolic/sym.coeffs.html), section “Coefficients of Multivariate Polynomial with Respect to Particular Variable”, lines69–81, explicitly show polynomial coefficients in the unselected variable. [Chuyoon–Shpilka](https://arxiv.org/abs/2603.07589), submitted8March2026, abstract lines16–22, studies bounded individual degree; this is modern context only. The direct access receipt preserves exact requests and outcomes.

Standard concept: collecting powers / coefficient extraction and partial or individual degree. The local mathematical reference states precisely the needed inequality over rational polynomials in finitely many variables. The support proof validates the stronger existing Lean hypotheses: arbitrary variable types and arbitrary commutative semirings. Historical polynomial-ring presentations and contemporary sparse-polynomial language agree on this meaning; no categorical or analytic reformulation is needed. This is routine algebra, not a claim of a novel mathematical theorem.

## Phase 4a — Parameter and hypothesis audit

| Parameter / axis | Current form | Standard form / checked conclusion |
|---|---|---|
| Variable type `τ` | Arbitrary `Type u_1` | Stronger than finite-variable literature; isolated theorem compiles with no finiteness assumptions. |
| Coefficients `R` | Arbitrary `Type u_2`, `CommSemiring R` | No field, additive inverses, domain, characteristic or nontriviality used. The existing `MvPolynomial`/`optionEquivLeft` interface fixes this class. Replacing it by `Semiring` does not preserve that interface. |
| Polynomial `P` | Arbitrary, including zero | No nonzero premise needed; degree uses natural zero convention. |
| Exponent `ν` | Any natural number | No `ν ≤ degreeOf none P` restriction; absent coefficients satisfy the bound. |
| Coordinate `j` | Any `τ` | Tracks `some j` correctly; cannot replace by distinguished coordinate. |
| Degree order | Natural coordinate degree, ≤ | Strict inequality or equality would change content; strict-loss example checked. |
| Decidability | None | Ambient `DecidableEq` omitted; no exported decidability needed. |
| Universes | Independent `u_1`, `u_2` | Preserved in native full type. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL for the fixed Option-polynomial coefficient interface; zero verified mechanical weakenings of the theorem itself. The isolated canonical statement is the original with its definitional alias expanded, not a new mathematical generalization.

An expanded-representation component was actually checked: for arbitrary finite supports `s,t`, a function `f` carrying `s` into `t`, and pointwise natural weights `a x ≤ b (f x)`, one has `s.sup a ≤ t.sup b`. Its proof compiles without any coefficient algebra or even `DecidableEq α/β`. This shows why no multiplicative reasoning is needed after support transport, but the transport and weight-identification hypotheses are new input data. It is not an existing complete replacement, nor evidence that `CommSemiring` can be dropped from the unchanged project statement. [Exact isolated execution](../evidence/Roth.degreeOf_coeffNone_le/coefficient-degree-isolated-executed.lean.txt), [clean receipt](../evidence/Roth.degreeOf_coeffNone_le/coefficient-degree-isolated-receipt.json).

## Phase 4c — Modern idiom, all nine rows

| # | Question | Answer / downstream consequence |
|---|---|---|
| 1 | Preambles to typeclasses | No change: `CommSemiring` already expresses coefficient structure; no bundled hypothesis to convert. |
| 2 | Sequences/metrics to filters | No: finite algebraic support, no convergence. |
| 3 | Construction to universal property | No new construction. `optionEquivLeft` already supplies the algebra equivalence. Restating the inequality categorically adds no usable degree API. |
| 4 | Closure predicates to bundled substructures | No change to this inequality. The private consumer already uses `Submodule.span` and `restrictSupport`; a checked bound feeds their membership API. |
| 5 | Fields to modules/(semi)rings | Already CommSemiring, substantially broader than the rational source; the field is only needed by the private basis consumer. |
| 6 | Higher categories | No meaningful higher-categorical degree improvement identified. |
| 7 | Concrete index to ordered structure | `ν : ℕ` is the actual monomial exponent. Abstract support supremum weights were checked, but changing the polynomial exponent type would rebuild the representation. |
| 8 | Concrete-via-abstract diagnostic | `coeffNone` appears zero times in the proof body; the proof immediately uses abstract degree/support APIs. Canonical restatement removes the project alias. The checked raw-support component exposes transport assumptions explicitly; it is not an existing full replacement. Downstream: degree bound can feed `restrictSupport` generator membership. |
| 9 | False-generalization guard | Reject equality: `P = X (some ())`, coefficient1 gives degree0 while original remaining-coordinate degree1. Reject arbitrary chosen supports without transport premises. The canonical alias-free inequality preserves the exact polynomial and coordinate. |

Modern idiom available: canonical mathlib spelling and a more abstract support component, but no verified mechanical hypothesis weakening or superior whole-result replacement. `strict_guard` is a kernel-checked strict-loss counterexample. The generic component is newly proved scratch evidence, not counted as an existing mathlib theorem. API choice is addressed in Phase7.

## Phase 4.5 — Infrastructure risk

n/a: theorem. All six definition-specific rows (typeclass diamonds, reducibility leaks, noncanonical unfolding, instance priority collisions, universe-polymorphism construction issues, coercion ambiguity) are inapplicable: this declaration adds only a proof, not a definition, class, instance, coercion or reducibility attribute. Full native type and independent canonical execution verify the theorem's universe and assumption surface.

## Phase 4.6 — Proof strategy, all five rows

| # | Question | Assessment |
|---|---|---|
| 1 | ε-δ versus filters | n/a; no topology. |
| 2 | Element proof versus substructure inclusions | Support-wise bounds are canonical for `degreeOf_le_iff`. The consumer's span inclusion composes with the degree inequality; complete auxiliary replay verifies this. |
| 3 | Sequences versus nets | n/a; no limits. |
| 4 | Construction versus universal property | Existing algebra equivalence is already used; no new object. |
| 5 | Missing helpers mathlib should have | Candidate Option analogue of `degreeOf_coeff_finSuccEquiv`; a generic support-degree transport API is an alternative. No additional proof helpers are required for the current short proof. |

MATHLIB-IDIOMATIC: support transport followed by degree supremum control is the direct proof. The potential contribution is the reusable statement, not an elaborate new proof strategy. No cost-based verdict downgrade.

## Phase 5 — Five actual search methods on three forms

All15 formal-method cells (12 API/name calls and3 source searches) have exact raw request/response receipts. Finder uses its documented default v4.28 snapshot; the pinned source is authoritative for positive candidates. Local search reports `index: unavailable` while still returning source-backed positive matches. This is not an absence certificate.

| Form | Finder | Loogle | LeanSearch | Source rg | Local name search |
|---|---|---|---|---|---|
| Current | Option coefficient coordinate degree; totalDegree Option lemmas returned | `MvPolynomial.degreeOf, MvPolynomial.optionEquivLeft`; natDegree equivalence hits | Option API and total-degree lemmas | `degreeOf.*coeff\|coeff.*degreeOf` | `degreeOf_coeff`: finite analogue plus project/scratch names |
| Literature | Collect powers and bound remaining degree; exact finite analogue returned | `MvPolynomial.degreeOf, Polynomial.coeff`; finite analogue | finite analogue and coordinate degree bounds | finite coefficient / total-degree Option names | `degreeOf_coeff_finSuccEquiv`: positive pinned source hit |
| Abstract | Support projection and coordinate supremum | `Finset.sup, _ ≤ _`; sup_le, le_sup, monotonicity | supDegree/support and `degreeOf_eq_sup` | supDegree/support projection forms | `mem_support_coeff_optionEquivLeft`: positive pinned source hit |

[Current Finder](../evidence/Roth.degreeOf_coeffNone_le/search-current-finder.json), [Loogle](../evidence/Roth.degreeOf_coeffNone_le/search-current-loogle.json), [LeanSearch](../evidence/Roth.degreeOf_coeffNone_le/search-current-leansearch.json), [local](../evidence/Roth.degreeOf_coeffNone_le/search-current-local.json), [rg](../evidence/Roth.degreeOf_coeffNone_le/rg-current.json).
[Literature Finder](../evidence/Roth.degreeOf_coeffNone_le/search-literature-finder.json), [Loogle](../evidence/Roth.degreeOf_coeffNone_le/search-literature-loogle.json), [LeanSearch](../evidence/Roth.degreeOf_coeffNone_le/search-literature-leansearch.json), [local](../evidence/Roth.degreeOf_coeffNone_le/search-literature-local.json), [rg](../evidence/Roth.degreeOf_coeffNone_le/rg-literature.json).
[Abstract Finder](../evidence/Roth.degreeOf_coeffNone_le/search-modern-finder.json), [Loogle](../evidence/Roth.degreeOf_coeffNone_le/search-modern-loogle.json), [LeanSearch](../evidence/Roth.degreeOf_coeffNone_le/search-modern-leansearch.json), [local](../evidence/Roth.degreeOf_coeffNone_le/search-modern-local.json), [rg](../evidence/Roth.degreeOf_coeffNone_le/rg-modern.json).

Pinned positive candidates, signatures checked natively:

- `MvPolynomial.degreeOf_coeff_finSuccEquiv`, `Mathlib/Algebra/MvPolynomial/Equiv.lean:834`: same degree inequality for `Fin (n+1)` variables. This does not directly instantiate arbitrary `τ`; adding a finite equivalence would impose an unjustified finiteness hypothesis.
- `MvPolynomial.mem_support_coeff_optionEquivLeft`, same file:549: exact support insertion iff for arbitrary Option variables.
- `MvPolynomial.degreeOf_le_iff`, `Mathlib/Algebra/MvPolynomial/Degrees.lean:235`: coordinate bound iff each supported exponent is bounded.
- `MvPolynomial.monomial_le_degreeOf`, same file:268: a supported monomial exponent is bounded by the coordinate degree.
- `MvPolynomial.optionEquivLeft_coeff_coeff`: coefficients after separation equal original coefficients at inserted exponents.
- Option total-degree bounds are different: bounding coefficient total degree by original total degree does not yield the sharper specified-coordinate bound.

Conclusion: positive building blocks and a finite-variable analogue, not an exact has-it claim. Empty searches, external snapshot mismatch or unavailable local index are not used to prove absence. No costly failed automation search is presented as absence evidence.

## Phase 5.5 — Three statement-shape checks

Normal form: compare (a) alias `degreeOf j (coeffNone P ν) ≤ ...`, (b) canonical `degreeOf j ((optionEquivLeft R τ P).coeff ν) ≤ ...`, and (c) support-wise exponent implication. Mathlib's canonical user-facing spelling is (b); (c) is an implementation view via `degreeOf_le_iff`. The inequality has the desired upper bound on its RHS, not an orthogonal equivalence.

Syntactic generality: (b) was actually compiled, as was the abstract support-supremum component and a complete consumer using the degree inequality. Choose (b) for any proposed upstream theorem; it avoids a project-specific definition and has the same mathematics. Renaming and expanding an alias are surface cleanup, not `YES-but-generalise-first`.

Superfluous arguments: `τ` and `R` index the polynomial representation; `CommSemiring R` is required by that interface; `P`, `ν`, `j` all select actual mathematical data. None can be dropped. Finiteness, decidable equality, nontriviality, a domain and a power bound are already absent. No new assumptions are imported by the isolated proof.

Overall: RESTATE-BEFORE-SHIP only for canonical namespace/name/alias removal; fixed mathematical hypotheses already correct. Suggested future name `MvPolynomial.degreeOf_coeff_optionEquivLeft_le` in `Mathlib/Algebra/MvPolynomial/Equiv.lean` beside the finite analogue.

## Phase 6.0 — Callers and inline audit

Explicit references: declaration line114 only; zero same-file callers and zero external-to-file callers. Both ignore-resistant source `rg` and tracked `git grep` agree. Fresh lexical enumeration covers the canonical source inventory, not scratch files. Exact ordered293 native kernel-value audit finds zero direct value consumers. These counts are separate: source names, direct kernel constants, implicit simp closure and semantic reuse are not interchangeable. This theorem is not tagged simp.

| Caller or inline location | Source relation | Checked refactor |
|---|---|---|
| No explicit caller | Zero calls to target | No existing target application needs substitution. |
| Private `Roth.exists_coeffNone_basis_aux`, Separation310–313 | Generator degree/support argument is independently re-derived inline with the same monomial support insertion. Its kernel does not reference this theorem. | Entire auxiliary replay replaces generator proof with `degreeOf_le_iff.1 (canonical P ν j) d hd`. All basis construction, finite dimension, positive rank and degree conclusions retained. |

[rg](../evidence/Roth.degreeOf_coeffNone_le/caller-rg.json), [git grep](../evidence/Roth.degreeOf_coeffNone_le/caller-git-grep.json), [lexical inventory](../evidence/Roth.degreeOf_coeffNone_le/lexical-enumeration.json), [inline search](../evidence/Roth.degreeOf_coeffNone_le/rg-inline.json), [canonical audit source](../evidence/Roth.degreeOf_coeffNone_le/coefficient-degree-audit-executed.lean.txt), [full inline auxiliary replay](../evidence/Roth.degreeOf_coeffNone_le/coefficient-degree-inline-caller-executed.lean.txt), [receipt](../evidence/Roth.degreeOf_coeffNone_le/coefficient-degree-inline-caller-receipt.json).

This is a concrete potential use, not proof that the original theorem was called. Zero lexical and kernel counts therefore support assessing API value; they do not automatically establish junk or composability.

## Phase 6 — Composition experiments

Attempt1, actual isolated canonical proof:

```lean
  refine degreeOf_le_iff.2 fun d hd ↦ ?_
  simpa using monomial_le_degreeOf (some j) ((mem_support_coeff_optionEquivLeft R).1 hd)
```

It compiles without Roth imports; `#check_failure Roth.degreeOf_coeffNone_le` guards against circular use. Three structural APIs are visible, but the final `simpa` normalizes `d.optionElim ν (some j)` to `d j`. `Finsupp.optionElim` is defined through an embedding and an update; evaluation is not a definitional bridge. The existing simplifier uses `Finsupp.optionElim_apply_eq_elim` and `Option.elim_some`. Thus both the canonical and old spellings need more than three named dependencies when normalization is counted honestly. Do not classify NO solely from three source lines.

Attempt2: use the finite analogue directly. Its exact checked type is restricted to `Fin (n+1)`; there is no supplied finite equivalence for arbitrary `τ`. This is a genuine partial match, not a specialization of a more general law. Transporting finite support through additional equivalences would be a new proof.

Attempt3: generic finite supremum component. Its two main order calls (`Finset.sup_le`, `Finset.le_sup`) plus transitivity prove the abstract component. Obtaining the full polynomial result still requires support insertion and coordinate compatibility. A newly proved helper is not an existing mathlib replacement.

Conclusion: no demonstrated strict ≤3-call composition of the whole target. The remaining projection normalization is small; deciding whether the Option statement deserves its own named API is precisely the Phase6b “trivial simp composition” boundary. This is a legitimate BORDERLINE judgment, not a verification failure or a claim of strict theorem absence.

## Phase 7 — Verdict and actionable next step

**BORDERLINE-needs-human.** Existing finite-index degree API and a complete private-auxiliary replay support usefulness of an arbitrary Option-variable law. Conversely, the complete proof is three support/degree calls plus elementary projection normalization, and the current public theorem has no direct callers. Neither a strict NO composition nor automatic YES follows from those facts. The decision concerns the desired upstream API, not cost, search timeout or proof difficulty.

1. Should mathlib expose `degreeOf_coeff_optionEquivLeft_le` directly beside `degreeOf_coeff_finSuccEquiv`, so arbitrary variable types get the same coordinate-degree interface?
2. Should the upstream contribution instead start from a general support/supDegree transport lemma, with this Option bound as an application, or is the existing support-wise proof the preferred client interface?

If the direct law is accepted: use the already checked canonical statement over arbitrary `τ` and `CommSemiring R`, place it in `Mathlib/Algebra/MvPolynomial/Equiv.lean`, and use it in the private basis auxiliary as replayed. The local `coeffNone` wrapper need not be shipped. If the API is declined: retain the support argument inside `Roth/Separation.lean` as the suitable project-local destination; removing the currently uncalled public wrapper would require no explicit caller edits. This is an assessment, not authorization to mutate production. No cost-based downgrade or inherited parent verdict is used. The parent coefficient alias was NO-composable; the re-aim special-case NO-has-it rule does not apply to it.

## Phase 8 — Evidence completion

All native checks succeeded on their first actual executions, complete and nonpartial, with no errors/warnings or nonstandard axioms. Accepted evidence: original full native type/kernel/axioms; exact ordered293 audit; mathlib-only canonical theorem, raw-support component and strict-loss guard; complete private auxiliary replay. Root made preparation-only indentation changes, removed unnecessary generic `DecidableEq` assumptions and moved the caller's `open` inside its namespace before first execution; exact accepted executed sources and complete raw receipts are archived. Preparation files are clearly distinguished from execution sources. No rejected native attempt or recovered `sorryAx` is accepted.

[Verification map](../evidence/Roth.degreeOf_coeffNone_le/verification.json), [phase metadata](../evidence/Roth.degreeOf_coeffNone_le/assessment.json), [overview entry](../evidence/Roth.degreeOf_coeffNone_le/overview-entry.json), [portable validator](../evidence/Roth.degreeOf_coeffNone_le/validate.py). The current copy manifest validates all artifact hashes/bytes, exact canonical order including private names, fresh17 inputs, complete raw/native success, standard axioms, full caller/inline evidence, all literature and formal-search channels, local links and the credential guard. Root independent acceptance remains pending.
