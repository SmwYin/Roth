# Roth.coeff_coeffNone — NO-mathlib-has-it

Mathlib already has the coefficient correspondence as `MvPolynomial.optionEquivLeft_coeff_coeff`, with the combined exponent written `d.optionElim ν`. The project theorem changes the coefficient extractor's name and expands that exponent into `d.mapDomain some + single none ν`. The canonical one-call theorem, the non-definitional representation bridge, and both complete caller refactors have actually compiled. This is an independent positive hit, not inheritance of parent152's NO-composable verdict.

## Phase 0 — Baseline and scope

Public theorem155/293 is at `Roth/Separation.lean:85`, branch `ramin-cleanup`. The entire561-line module was read, including both callers and its determinant/integrality context. The module separates one distinguished variable in preparation for Roth's Lemma2. Fresh hashes of all17 production sources/pins match the shared successful baseline. The newer complete build also succeeded:2467jobs, exit0. No production, Git, or progress changes were made.

Evidence: [fresh inputs](../evidence/Roth.coeff_coeffNone/inputs.json), [baseline](../evidence/Roth.coeff_coeffNone/baseline-build.txt), [complete build](../evidence/Roth.coeff_coeffNone/index-file-completion-2026-10-27.json), [entire module](../evidence/Roth.coeff_coeffNone/Roth-Separation.lean.txt). The actual native original, its full kernel printer and standard axiom check succeeded without partial results, errors or warnings. Historical persistent diagnostics were excluded from target-specific info assertions using line5354. The whole-file diagnostics still received error/warning/axiom screening.

## Phase 1 — Comprehend

Write a polynomial as a polynomial in the distinguished variable with coefficient polynomials in the remaining variables. The coefficient of a remaining-variable monomial in its ν-th coefficient polynomial is precisely the original polynomial's coefficient at the combined monomial. This is coefficient regrouping, with no finiteness, degree bound, nonzero assumption, or characteristic restriction.

Full native type:

```lean
@Roth.coeff_coeffNone : ∀ {τ : Type u_1} {R : Type u_2} [inst : CommSemiring R]
  (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ),
  (Roth.coeffNone P ν).coeff d =
    P.coeff (Finsupp.mapDomain some d + Finsupp.single none ν)
```

`τ` indexes the remaining variables; `R` supplies coefficients; `ν` and `d` specify the two exponent components. `CommSemiring R` supports the parent algebra equivalence. The project dependency is `Roth.coeffNone`; the exponent reconstruction theorem153 is not a dependency of this proof. The proof unfolds the parent, invokes the existing coefficient law, and checks exponent equality in the two Option cases.

Evidence: [native type](../evidence/Roth.coeff_coeffNone/native-type.json), [complete original native receipt](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-original-audit-receipt.json), [executed source](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-original-executed.lean.txt).

## Phase 2 — Preliminary checks

SMALL: coefficient bookkeeping, no new structure, not a named mathematical theorem or module main result. The definition-only one-line test is n/a because this is a theorem. Its useful local API role is real: two explicit callers; it is not dead code. Neither its size nor its dependency count settles the upstream verdict.

## Phase 3 — Exhaustive literature

Each row records an actual query; response bodies were not archived. Receipts contain exact requests, response SHA256/bytes, returned locators and original concise summaries. URL queries were removed from archived locators, with redactions documented. There is no invented ninth channel.

| Channel | Exact query / request | Outcome |
|---|---|---|
| Specific web | `polynomial coefficient collecting powers one variable coefficient monomial polynomial ring` | Standard monomial coefficients; primary Magma and Macaulay2 documentation supplies iterated coefficient-ring context. [receipt](../evidence/Roth.coeff_coeffNone/literature-web-specific.json) |
| General web | `iterated polynomial ring R x y isomorphism coefficients commutative semiring` | McKernan lecture15 states natural iterated polynomial-ring isomorphism. Direct PDF failed502; search excerpts retained only as summarized evidence. [receipt](../evidence/Roth.coeff_coeffNone/literature-web-general.json) |
| Aliases web | `polynomial ring in infinitely many variables finitely supported monomials coefficients` | Clemson monomial-algebra appendix describes finite monomial support and infinitely many variables. [receipt](../evidence/Roth.coeff_coeffNone/literature-web-alias.json) |
| ChatGPT math | Standard form, generality and historical evolution | n/a: `ask_chatgpt_math` unavailable. No substituted invented response. |
| Local source | `collecting\|roth:lem2\|coefficient` in `clean.tex` | Lemma2 proof, line374, explicitly collects powers of the last variable. [search](../evidence/Roth.coeff_coeffNone/local-literature-search.json), [excerpt](../evidence/Roth.coeff_coeffNone/clean-separation-excerpt.tex.txt) |
| nLab | `site:ncatlab.org/nlab polynomial ring multivariate coefficients` | Free commutative monoid/free module construction and free-algebra formulation; direct page parsing failed unsupported XHTML400. [receipt](../evidence/Roth.coeff_coeffNone/literature-nlab.json) |
| nCatLab | `site:ncatlab.org/ncatlab polynomial algebra coefficient variables` | Returned /nlab pages only; no in-namespace hit. This limitation is not absence evidence. [receipt](../evidence/Roth.coeff_coeffNone/literature-ncatlab.json) |
| Stacks | `site:stacks.math.columbia.edu polynomial ring variables coefficients` | Polynomial presentations and base change; inspected tag00SK, no direct regrouping law located. [receipt](../evidence/Roth.coeff_coeffNone/literature-stacks.json) |
| MathOverflow | `site:mathoverflow.net polynomial ring infinitely many variables coefficients` | Infinite-variable rings and coefficient-ring discussions; no exact new law. [receipt](../evidence/Roth.coeff_coeffNone/literature-mo.json) |
| Recent arXiv | `site:arxiv.org multivariate polynomial formalization Lean coefficients 2022 2023 2024 2025 2026` | 2602.12772 (2026) arbitrary/infinite-variable Gröbner formalization;2507.05327 (2025) divided powers and power series. Related context, not a novelty claim. [receipt](../evidence/Roth.coeff_coeffNone/literature-arxiv.json) |

Primary locators include [McKernan lecture15](https://mathweb.ucsd.edu/~jmckerna/Teaching/15-16/Spring/103B/l_15.pdf), [Clemson monomial appendix](https://ssather.people.clemson.edu/DOCS/monomial.pdf), [nLab polynomial](https://ncatlab.org/nlab/show/polynomial), [Stacks00SK](https://stacks.math.columbia.edu/tag/00SK), and [Guo–Shen–Liu–Zhi2026](https://arxiv.org/abs/2602.12772). Access results are [recorded separately](../evidence/Roth.coeff_coeffNone/literature-primary-access.json).

Literature-standard content is the elementary identity the coefficient of x^d in the t^ν coefficient equals the x^d t^ν coefficient. The project source works over rationals/integer coefficients for its application; the formal theorem already removes that specialization. Arbitrary remaining-variable sets are natural because every polynomial has finite support. Historically, classical collecting-terms notation becomes an algebra equivalence and coordinate pullback in mathlib; no claimed historical priority attaches to this bookkeeping identity.

## Phase 4a — Parameters and generality

| Parameter / hypothesis | Audit |
|---|---|
| `τ : Type u_1` | Already arbitrary and universe polymorphic; no finite or decidable index needed. Native type confirms omission of surrounding section instances. |
| `R : Type u_2` | Independent universe; not specialized to the literature's ℚ/ℤ. |
| `[CommSemiring R]` | Fixed `coeffNone`/`optionEquivLeft` interface requires this. No subtraction, domain, field or characteristic assumptions. No unverified Semiring weakening claimed. |
| `P` | Arbitrary polynomial, including zero; no support or degree hypothesis. |
| `ν : ℕ` | Ordinary polynomial exponent; replacing by negative integers changes the object to Laurent data. |
| `d : τ →₀ ℕ` | Arbitrary finitely supported exponent, already correct for arbitrary variable sets. |
| Coordinate representation | `optionElim`, `embDomain .some + single none`, and `mapDomain some + single none` have actually verified bridges. They do not impose new hypotheses on P. |
| Underlying coefficient representation | `[Zero A]` suffices for slicing `(Option τ →₀ ℕ) →₀ A` via `Finsupp.comapDomain`. Prior152's actual `slice_apply` and `direct_coeff` bridge are reused with fresh17-input hashes. This wider representation is distinct from mechanically weakening the fixed parent. |

## Phase 4b — Generality verdict

MAXIMALLY GENERAL for the fixed polynomial-parent interface; no mechanical weakening is proposed. The wider Zero-only layer is verified, not merely suggested:

```lean
slice P ν d = P (d.optionElim ν)
```

Here `slice` is comapDomain along the injective coordinate insertion. Its apply law is the existing `Finsupp.comapDomain_apply`; the prior152 helper construction and `direct_coeff` bridge are new scratch proofs, not existing mathlib replacements. This distinguishes a representation expansion from changing a typeclass on `Roth.coeffNone`. [Exact prior152 source](../evidence/Roth.coeff_coeffNone/coeff-none-pullback-guarded-executed.lean.txt), [actual native receipt](../evidence/Roth.coeff_coeffNone/coeff-none-pullback-guarded-receipt.json).

## Phase 4c — Modern idiom

| # | Question | Result and downstream consequence |
|---|---|---|
| 1 | Typeclass preambles | Already `CommSemiring`; no bundled ad hoc algebraic assumptions. |
| 2 | Filters/topology | No topology or limiting operation. |
| 3 | Universal property | Parent uses the existing algebra equivalence. Rebuilding a free algebra is unnecessary; `optionEquivLeft_coeff_coeff` already exposes its coordinate law. |
| 4 | Bundled substructures | No closure predicate or subobject to bundle. |
| 5 | Algebraic hierarchy | The polynomial surface is already semiring general; the verified Zero-only coefficient pullback allows non-ring coefficient data to use `Finsupp.comapDomain_apply`. It does not supply multiplicative polynomial structure. |
| 6 | Higher categories | No categorical coherence data or relevant higher-categorical restatement. |
| 7 | Concrete indices | ℕ is the free commutative monoid exponent for polynomials; arbitrary τ is already supported. Arbitrary exponents would change the parent object. |
| 8 | Concrete-via-abstract | Yes: after the existing coefficient law, the remaining proof is exponent bookkeeping. At coefficient-table level it is generic injective Finsupp pullback under `[Zero A]`; prior152 bridge proves agreement with the polynomial coefficients. This composes with generic comapDomain API and avoids duplicate polynomial wrapper laws. |
| 9 | False-generalization guard | Canonical/embedding/mapped spellings preserve every exponent. Omitting the distinguished contribution or mismatching ν is false; both concrete ℕ/Unit counterexamples compiled. The Zero-only table is correctly identified as underlying data, not falsely asserted to be an algebra equivalence. |

Modern idiom available: yes, already present in mathlib. Canonical exponent insertion and the coefficient law remove duplicated coordinate calculations; the first complete caller can also use `optionEquivLeft_coeff_some_coeff_none` directly. A new polynomial wrapper is not a modernization of an obsolete mathlib formulation. The exact isolated source verifies canonical, embedding and mapped forms plus both guards: [source](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-isolated-executed.lean.txt), [receipt](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-isolated-receipt.json).

## Phase 4.5 — Infrastructure risks

n/a: theorem, not a def/class/instance. It introduces no typeclass diamond, reducibility leak, noncanonical unfolding, priority collision, universe-coercion implementation, or CoeFun/CoeSort path. The non-definitional exponent bridge is tracked as statement shape, not dismissed as definitional equality.

## Phase 4.6 — Proof strategy

| # | Strategy diagnostic | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a: algebraic coordinate identity. |
| 2 | Elements versus subobjects | Extensionality is appropriate for exponent equality; no ideal/submodule inclusion is at issue. Canonical coordinates avoid that equality in consumers. |
| 3 | Sequences versus nets | n/a: no convergence. |
| 4 | Explicit construction versus universal property | Use the existing equivalence and its coefficient API, not another construction. |
| 5 | Missing helpers that should exist | No missing coefficient law. A named bridge between expanded Option coordinates and optionElim is optional normal-form API; the verified proof uses existing update/embedding ingredients. |

REFACTOR-RECOMMENDED: use canonical coordinates and existing coefficient lemmas at the two callers. This is supported by full caller replay, not an assumption that short proof syntax means composition. Cost does not determine the verdict.

## Phase 5 — All five actual mathlib methods

All methods ran on current, literature and modern forms, plus a supplementary Zero-only abstract form. Exact requests and complete unabridged formal-search responses are archived individually.

| Form | Finder | Loogle | LeanSearch | Source rg | Local search |
|---|---|---|---|---|---|
| Current coefficient identity | [receipt](../evidence/Roth.coeff_coeffNone/search-current-finder.json): exact canonical hit | [successful retry](../evidence/Roth.coeff_coeffNone/search-current-loogle-retry.json): quoted coeff, exact hit | [receipt](../evidence/Roth.coeff_coeffNone/search-current-leansearch.json) | [receipt](../evidence/Roth.coeff_coeffNone/rg-current.json) | [receipt](../evidence/Roth.coeff_coeffNone/search-current-local.json): declaration found in source; index unavailable |
| Collecting powers | [receipt](../evidence/Roth.coeff_coeffNone/search-literature-finder.json) | [receipt](../evidence/Roth.coeff_coeffNone/search-literature-loogle.json): exact and full-index variants | [receipt](../evidence/Roth.coeff_coeffNone/search-literature-leansearch.json) | [receipt](../evidence/Roth.coeff_coeffNone/rg-literature.json) | [receipt](../evidence/Roth.coeff_coeffNone/search-literature-local.json) |
| Algebra equivalence/optionElim | [receipt](../evidence/Roth.coeff_coeffNone/search-modern-finder.json) | [successful retry](../evidence/Roth.coeff_coeffNone/search-modern-loogle-retry.json): polynomial and power-series laws | [receipt](../evidence/Roth.coeff_coeffNone/search-modern-leansearch.json) | [receipt](../evidence/Roth.coeff_coeffNone/rg-modern.json) | [receipt](../evidence/Roth.coeff_coeffNone/search-modern-local.json) |
| Zero-only coefficient pullback | [receipt](../evidence/Roth.coeff_coeffNone/search-zero-finder.json): embedding/DFinsupp related hits | [receipt](../evidence/Roth.coeff_coeffNone/search-zero-loogle.json): comapDomain_apply | [receipt](../evidence/Roth.coeff_coeffNone/search-zero-leansearch.json): comapDomain_apply | [receipt](../evidence/Roth.coeff_coeffNone/rg-zero.json) | [receipt](../evidence/Roth.coeff_coeffNone/search-zero-local.json): source hit, index unavailable |

The first current/modern Loogle queries used `MvPolynomial.coeff`, unknown to that external revision; errors are preserved, and actual retries used the quoted name fragment. Failed queries and unavailable local indices prove no absence. External indices may differ from the pin; positive canonical candidate signature and proof were verified against the pinned mathlib in an isolated context. `MvPowerSeries.coeff_coeff_optionEquivLeft` at `Mathlib/RingTheory/MvPowerSeries/Equiv.lean:131` is related, not automatically a polynomial replacement.

Concluded: found in mathlib as `MvPolynomial.optionEquivLeft_coeff_coeff`, identical coefficient law in canonical coordinates, `Mathlib/Algebra/MvPolynomial/Equiv.lean:610`. Other exact ingredients: `Finsupp.update_eq_add_single` (`Mathlib/Algebra/Group/Finsupp.lean:230`), `Finsupp.embDomain_some_none` (`Mathlib/Data/Finsupp/Option.lean:92`), `Finsupp.embDomain_eq_mapDomain` (`Mathlib/Data/Finsupp/Basic.lean:422`), and abstract `Finsupp.comapDomain_apply` (`Basic.lean:517`). Source hashes are in [mathlib inputs](../evidence/Roth.coeff_coeffNone/mathlib-inputs.json).

## Phase 5.5 — Statement shape

Normal form: REFACTOR to `d.optionElim ν`, already the RHS of mathlib's coefficient law. The two equivalent expanded forms were actually tested, not assumed definitionally equal. Syntactic generality: use full-index `optionEquivLeft_coeff_some_coeff_none` for the expansion caller, and coordinate insertion for the product-coefficient caller. Both permit the actual supplied arguments. Superfluous arguments: NONE. `τ`, `R`, P, ν and d determine the types/coefficients; CommSemiring belongs to the fixed equivalence. Fintype/DecidableEq are already absent. Overall: RESTATE-BEFORE-SHIP if retaining a local statement; upstream should reuse the canonical theorem.

## Phase 6.0 — Callers and inline audit

Canonical source inventory, fresh lexical enumeration, `rg --no-ignore` and tracked `git grep` agree: one declaration plus two uses, both in the declaring module. Internal uses excluding the declaring file:0; same-file uses:2; external files:0. This distinction avoids describing zero external references as dead code.

| Caller | Source usage | Verified refactor |
|---|---|---|
| `Roth.eq_sum_X_none_pow_mul_coeffNone` | `Separation.lean:107`, rewrite target then reconstruct exponent | Replace the true branch with `rw [Roth.coeffNone, optionEquivLeft_coeff_some_coeff_none]`. No theorem153 or155 needed. |
| `Roth.coeff_rename_mul_aeval` | `Separation.lean:129`, reverse target to split coefficients | Prove the local optionElim-to-expanded-coordinate equality via update and embedding; rewrite through `optionEquivLeft_coeff_coeff`, then retain the coefficient-product calculation. |

Fresh canonical293 ordered runtime audit found exactly these two direct kernel-value consumers. Source references and kernel direct dependencies are separate measures; neither claims opaque transitive/simp closure. Inline audit found related private coefficient and support-degree API usage, not a duplicate full target. Evidence: [rg](../evidence/Roth.coeff_coeffNone/caller-rg.json), [git grep](../evidence/Roth.coeff_coeffNone/caller-git-grep.json), [lexical inventory](../evidence/Roth.coeff_coeffNone/lexical-enumeration.json), [inline search](../evidence/Roth.coeff_coeffNone/rg-inline.json), [canonical audit source](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-audit-executed.lean.txt).

Both complete caller bodies compiled with standard axioms, no warning/error, partial result or recovered placeholder: [exact executed source](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-callers-executed.lean.txt), [receipt](../evidence/Roth.coeff_coeffNone/coeff-coeffnone-callers-receipt.json). The private helper is accessed via the original constant using `Lean.mkPrivateNameCore`, not reaxiomatized or replaced by a new theorem.

## Phase 6 — Actual compositions and guards

Canonical statement: COMPOSABLE by one existing theorem call:

```lean
example (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    ((optionEquivLeft R τ P).coeff ν).coeff d = P.coeff (d.optionElim ν) :=
  optionEquivLeft_coeff_coeff R P ν d
```

The embedding statement adds `update_eq_add_single` with `embDomain_some_none`; the exact original mapDomain spelling additionally uses `embDomain_eq_mapDomain`. That is four named mathematical ingredients plus congruence/transitivity, not a claimed ≤3-call derivation. The isolated `mapped` proof checks the representation bridge, and full caller replays check applicability. No new scratch helper is counted as a library building block. A hypothetical closing `simp [defs...]` would remain Phase6b BORDERLINE evidence; it is not the basis for this verdict.

The omitted-distinguished-exponent and wrong-power guards are actual inequalities for P=`X none` over ℕ/Unit. An initial malformed guard parsed `.mapDomain` as a partial application and recovered a sorryAx; the entire initial source and receipt are preserved as rejected evidence. Root's parenthesized repair passed; no substantive replacement proof changed. Only the clean receipt is accepted.

## Phase 7 — Verdict and actionable plan

**NO-mathlib-has-it.** The normalized statement is already `MvPolynomial.optionEquivLeft_coeff_coeff`; its one-call proof is verified. This conclusion is scoped to the mathematical coefficient law and canonical representation, with the actual old-form normalization shown separately. It does not claim that the raw old syntax is definitional or a one-call replacement, and does not inherit parent152's verdict. The wider coefficient-table abstraction also has an existing generic application law; its new polynomial agreement bridge is explicitly identified.

At each of the two call sites, apply the exact full-body refactor in Phase6.0 before deleting the project theorem. The first removes both155 and153 dependencies; the second keeps an explicit local coordinate bridge. An optional explanatory wrapper belongs locally in `Roth/Separation.lean` near `coeffNone`, where it communicates the source paper's monomial convention. No new upstream coefficient theorem, PR title/grouping or reviewer selection is applicable to this NO verdict. An optional named exponent-normalization bridge is a separate API question, not a reason to duplicate the coefficient law or to change this verified hit into a cost-based BORDERLINE decision.

## Phase 8 — Evidence completion

All mandatory phases passed or carry the explicit theorem/optional-service n/a justification. Accepted proofs use only standard axioms `propext`, `Classical.choice`, `Quot.sound`; no limits were raised. The canonical audit preserves exact293 order and private names. Prior152 Zero-only evidence is clearly labeled prior evidence; all17 inputs were freshly matched. Rejected recovered-placeholder evidence is separate from accepted native success. No unresolved verification items remain.

[Assessment](../evidence/Roth.coeff_coeffNone/assessment.json), [verification](../evidence/Roth.coeff_coeffNone/verification.json), [overview entry](../evidence/Roth.coeff_coeffNone/overview-entry.json), [portable read-only validator](../evidence/Roth.coeff_coeffNone/validate.py), [current manifest](../evidence/Roth.coeff_coeffNone/copy-manifest.json). Root acceptance remains pending until independent review.
