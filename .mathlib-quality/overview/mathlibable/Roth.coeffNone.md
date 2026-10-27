# Roth.coeffNone — NO-composable-from-mathlib

Declaration 152/293, `Roth/Separation.lean:80`, noncomputable definition. Full read-only assessment; all phases completed. Root acceptance pending.

## Phase 0 — Doctor

All 17 source/pin hashes freshly match the shared baseline. The original build completed successfully (2467 jobs), and the fresh Index-completion full build also passed with the identical inputs. See [inputs](../evidence/Roth.coeffNone/inputs.json), [baseline](../evidence/Roth.coeffNone/baseline-build.txt), and [fresh full build](../evidence/Roth.coeffNone/index-file-completion-2026-10-27.json).

The complete declaring module was read, including every caller and the final determinant theorem. Its purpose is separation of one distinguished variable and integral factorization of a Hasse-derivative determinant. Native type, body and axioms succeed with no warnings, no errors, no placeholders and no printer elision. The exact native type is

```lean
Roth.coeffNone.{u_1, u_2} : {τ : Type u_1} →
  {R : Type u_2} → [CommSemiring R] →
  MvPolynomial (Option τ) R → ℕ → MvPolynomial τ R
```

There is **no Fintype or DecidableEq parameter**. Their presence in the surrounding source section does not put them into this declaration. Its axioms are exactly `propext`, `Classical.choice`, `Quot.sound`. [Native original and canonical audit](../evidence/Roth.coeffNone/coeff-none-original-audit-receipt.json).

## Phase 1 — Comprehend

Given a polynomial in a distinguished variable and any family of other variables, collect terms with distinguished-variable exponent ν. The resulting coefficient is itself a polynomial in the other variables. For example, the coefficient of x² in `a(y)x²+b(y)x+c(y)` is `a(y)`.

`τ` indexes the remaining variables; `R` supplies a commutative coefficient semiring; `P` is the original finite-support polynomial; `ν : ℕ` is the distinguished-variable exponent. There are no propositional hypotheses or bounds. The definition is exactly

```lean
Polynomial.coeff (MvPolynomial.optionEquivLeft R τ P) ν
```

The existing equivalence identifies `R[Option τ]` with `R[τ][X]`. This is coefficient extraction after reinterpreting the polynomial, rather than evaluation at zero or a derivative.

## Phase 2 — Preliminary checks

SMALL: coefficient-extraction helper, not the module's main separation or factorization theorem. One substantive body line, therefore ONE-LINER WITH-EXEMPTION:

| Exemption | Applies | Evidence |
|---|---|---|
| Avoid defeq abuse | No demonstrated necessity | Native target equality is `rfl`; the module replay succeeds after removing the anchor. Two explicit unfolding steps become `change` followed by the original mathlib rewrites. |
| Avoid typeclass diamonds | No | An ordinary function creates no instances, coercions or new carrier types. Canonical semiring and module syntheses succeed. |
| Semantic intent / stable API | Yes | Documented name used by seven declarations, including expansion, degree control and basis construction. It improves local readability. |

The semantic exemption is real. It establishes legitimate local use, but does not override the independently verified two-call mathlib composition when deciding upstream inclusion.

## Phase 3 — Exhaustive literature

Every named channel was attempted; the informal nine-channel label does not justify inventing an additional channel. Search artifacts retain exact requests, returned response SHA256/bytes/status, titles and sanitized URLs, with no full article or search-result bodies.

| Channel | Exact query / locator | Outcome |
|---|---|---|
| General web, specific | `polynomial coefficient one variable polynomial in remaining variables` | CGAL's Polynomial manual describes precisely the univariate view with polynomial coefficients. |
| General web, general | `polynomial rings in infinitely many variables iterated polynomial ring semiring` | Infinite-variable polynomial rings and finite-support descriptions; nothing imposing finite τ. |
| General web, aliases | `collecting terms polynomial recursive representation coefficient extraction` | Recursive versus distributed representation; primary Monagan–Pearce paper found. |
| ChatGPT math | Standard form, maximal generality and historical evolution would be requested | n/a: `ask_chatgpt_math` unavailable. Other channels were all executed. |
| Local reference | `collecting|coefficient polynomials|roth:lem2` in clean.tex | §2 Lemma 2 proof, line374; basis-span implementation note lines428–433. |
| nLab | `site:ncatlab.org/nlab polynomial ring free commutative algebra` | Polynomial/free-algebra context returned. Opening polynomial page fails unsupported XHTML; no claim of full-page inspection. |
| nCatLab, distinct namespace | `site:ncatlab.org/ncatlab polynomial ring coefficients` | Search returns `/nlab` and other pages, no exact `/ncatlab` hit. Recorded honestly as out-of-namespace results. |
| Stacks | `site:stacks.math.columbia.edu polynomial ring infinitely many variables` | Ordinary and divided-power polynomial contexts returned. Opened tag07H4; its divided-power multiplication is a different object, not a generalization of ordinary coefficients. |
| MathOverflow | `site:mathoverflow.net polynomial ring iterated polynomial coefficients` | Polynomial rings and coefficient-slice discussion; no direct new abstraction establishing an upstream name. |
| Recent arXiv | `site:arxiv.org 2022 2023 2024 2025 2026 polynomial coefficient extraction multivariate` | Opened 2312.17664, dated 2023-12-29, within 2021-10-27–2026-10-27. Sparse interpolation uses ordinary coefficient-times-monomial representation; older2019 and unrelated hits are not counted as recent evidence. |

Primary standard-form evidence: [CGAL §5.1–5.2](https://doc.cgal.org/Manual/3.4/doc_html/cgal_manual/Polynomial/Chapter_main.html), especially lines22–29 and36–42, interprets a multivariate polynomial as univariate over a polynomial coefficient ring. [Monagan–Pearce §1, pp1–2](https://www.cecm.sfu.ca/personal/monaganm/papers/PseudoHeap.pdf) explains the recursive representation. [Recent sparse interpolation paper](https://arxiv.org/abs/2312.17664) concerns algorithms, not a replacement mathematical definition. [Stacks23.5](https://stacks.math.columbia.edu/tag/07H4) supplies a useful false-generalization contrast only.

Standard concept: coefficient extraction in a chosen variable / recursive polynomial representation. The local rational and integer context imposes stronger assumptions than needed: this definition already works over arbitrary commutative semirings and arbitrary variable types. The sources do not establish a separate standard mathematical object requiring the name `coeffNone`. The older recursive representation and recent sparse representation are compatible viewpoints, not evidence of a historical change in coefficient meaning.

Evidence: [specific search](../evidence/Roth.coeffNone/literature-web-specific.json), [generality search](../evidence/Roth.coeffNone/literature-web-general.json), [alias search](../evidence/Roth.coeffNone/literature-web-alias.json), [nLab](../evidence/Roth.coeffNone/literature-nlab.json), [nCatLab](../evidence/Roth.coeffNone/literature-ncatlab.json), [Stacks](../evidence/Roth.coeffNone/literature-stacks.json), [MO](../evidence/Roth.coeffNone/literature-mo.json), [arXiv](../evidence/Roth.coeffNone/literature-arxiv.json), [access limitations](../evidence/Roth.coeffNone/literature-primary-access.json), [successful primary access](../evidence/Roth.coeffNone/literature-primary-supplement.json), [local excerpt](../evidence/Roth.coeffNone/clean-separation-excerpt.tex.txt).

## Phase 4a — Parameters and generality

| Parameter | Audit |
|---|---|
| `τ : Type u_1` | Arbitrary, possibly infinite or empty; native source uses no finite/equality assumption. Independent higher-universe `τ := Type` compiles. |
| `R : Type u_2`, `[CommSemiring R]` | Matches the existing algebra-equivalence interface; no field, characteristic, domain or nontriviality restriction. |
| `P` | Arbitrary polynomial, including zero; finite support is supplied by the carrier, no extra support assumption. |
| `ν : ℕ` | Arbitrary natural exponent, including zero and exponents above the degree; the latter produce zero. Integers would change to Laurent data, not weaken this interface. |
| Ambient `[Fintype τ]`, `[DecidableEq τ]` | Not actual parameters, so not weakening opportunities. |

## Phase 4b — Verified generality outcome

**STRICTLY NARROWER at the expanded coefficient representation**, with a mechanically verified hierarchy weakening from commutative-semiring polynomial coefficients to arbitrary finite-support data over `[Zero A]`. The fixed `MvPolynomial`/AlgEquiv surface is already general: this pin's MvPolynomial carrier itself requires CommSemiring, so changing that binder alone to Semiring is not a well-formed fixed-surface weakening.

The canonical expanded core is already present as `Finsupp.comapDomain`. Insert ν into an exponent vector using `d.optionElim ν`; this insertion is injective because evaluation at each `some j` recovers d j. The checked definition is

```lean
Finsupp.comapDomain (fun d => d.optionElim ν) P (coordinateInjective ν).injOn
```

It needs only `[Zero A]`. Native `slice_apply` checks that its coefficient is exactly `P (d.optionElim ν)`. Native `direct_coeff` proves that the original direct coefficient polynomial's underlying Finsupp is this slice of `P.coeff`, by coefficient extensionality and **the existing** `MvPolynomial.optionEquivLeft_coeff_coeff R P ν d`. Thus this is the same coefficient information, not a similar-looking different operation. This is a genuine representation bridge; it is not definitional equality of the polynomial and Finsupp carriers and is not counted as a one-call replacement of the old spelling.

The initial additive sum/filter slice remains exploratory and its separate equality was not proved; the sharper Zero-only pullback supplies the accepted canonical weakening. No new generalized definition is needed upstream because the more general core operation already exists. Consequently this finding strengthens reuse rather than creating a YES-but-generalise-first contribution. [Exact expanded proof](../evidence/Roth.coeffNone/coeff-none-pullback-guarded-executed.lean.txt), [native receipt](../evidence/Roth.coeffNone/coeff-none-pullback-guarded-receipt.json).

## Phase 4c — All nine modern-idiom rows

| # | Diagnostic | Result and downstream consequence |
|---|---|---|
| 1 | Typeclasses | Already uses CommSemiring; no unbundled structure hypothesis. |
| 2 | Filters/topology | No topology or limiting process. |
| 3 | Universal property | The parent optionEquivLeft already implements the polynomial algebra equivalence. Reuse it rather than a second universal-property construction. |
| 4 | Bundled substructures | No closure predicate to bundle. A coefficient operator can be bundled as a linear map instead. |
| 5 | Hierarchy | Already beyond the source's fields/integers. CommSemiring belongs to the fixed carrier/algebra interface. The underlying coefficient slice weakens to Zero via existing comapDomain and the native bridge. |
| 6 | Higher categories | No categorical coherence assertion; categorification adds no identified downstream use. |
| 7 | Index structures | ℕ indexes ordinary powers. General monoid exponents would change the polynomial carrier and require a proved bridge. |
| 8 | Concrete-via-abstract | Explicit body inspection: zero project-specific identifiers; only optionEquivLeft and coeff. Replace the new plain-function anchor by existing coordinate projection after equivalence. At the representation level, existing comapDomain pulls back arbitrary finite-support data over Zero; the direct_coeff theorem verifies the bridge. Bundled version is `(lcoeff _ ν).restrictScalars R |>.comp optionEquivLeft.toLinearMap`, enabling map_add and map_smul directly; both laws compile. |
| 9 | False-generalization guard | Projection is linear but generally not multiplicative. Native witness at ν=1, P=Q=X none gives coeff(X²)=0 versus coeff(X)²=1 over ℕ. No AlgHom proposal is valid. Laurent, divided-power and evaluation operations would change the content and are rejected. |

Modern organization: the existing bundled coefficient map and equivalence already supply the useful abstract interface. The bundled composition is a verified alternative, not an asserted preexisting named replacement for the whole composite. [Named independent native source](../evidence/Roth.coeffNone/coeff-none-isolated-named-executed.lean.txt), [receipt](../evidence/Roth.coeffNone/coeff-none-isolated-named-receipt.json).

## Phase 4.5 — Definition infrastructure risks

| Risk | Level | Checked evidence |
|---|---|---|
| Typeclass diamond | NONE | Ordinary function, no new instance; native canonical semiring/module syntheses succeed. |
| Reducibility leak | LOW | Semireducible def with no reducible attribute. Actual-context equality to exact mathlib RHS closes by rfl; caller replay validates controlled unfolding removal. |
| Noncanonical unfolding | LOW | Extra anchor has two explicit unfolding consumers. No simp attribute introduces a new normalization direction; direct RHS is canonical upstream spelling. |
| Instance priority collision | NONE | No instance declaration or priority. |
| Universe polymorphism | LOW | Full native type has independent universes; abstract u/v and `τ := Type`, `R := ℕ` elaborate. No forced finite universe. |
| Coercion ambiguity | NONE | No new CoeFun/CoeSort declaration; existing AlgEquiv and linear-map applications elaborate. |

Overall LOW. There is no specific colliding instance pair or competing coercion to synthesize; attributing an instance to this function would be a category mistake. The actual structure/coercion paths used by its body were tested.

## Phase 4.6 — All five proof-strategy rows

| # | Strategy question | Audit |
|---|---|---|
| 1 | ε–δ versus filters | n/a: algebraic definition. |
| 2 | Elements versus point-free algebra | Bundled linear-map composite is the useful alternative for add/smul laws; plain expression remains sufficient for current callers. |
| 3 | Sequences versus nets | n/a: no analysis. |
| 4 | Construction versus universal property | Parent equivalence already handles construction; no new universal-property helper needed. |
| 5 | Missing helper API | None needed to construct the target. The expanded representation bridge was proved using extensionality and existing optionEquivLeft_coeff_coeff. It is a new verification proof, not a preexisting named bridge or missing core operation. |

Current strategy MATHLIB-IDIOMATIC as a local function. Upstream recommendation is reuse the existing two-call composition; no cost-based downgrade.

## Phase 5 — Five actual formal methods, all three forms

| Form | Finder / LeanSearch request | Loogle | Local name search | Pinned rg |
|---|---|---|---|---|
| Current | `MvPolynomial option variable coefficient polynomial` | `MvPolynomial.optionEquivLeft` | `optionEquivLeft` | coeffNone, optionEquivLeft coefficients |
| Literature | `polynomial ring R[X,Y] as polynomial in X over R[Y] coefficient` | `Polynomial.coeff` | `coeff` | optionEquivLeft, optionEquivRight, sumAlgEquiv |
| Modern | `linear map polynomial coefficient composed algebra equivalence` | `Polynomial.lcoeff` | `lcoeff` | lcoeff, lcoeff_comp_mapAlgHom_eq, restrictScalars |

All twelve original remote/local tools returned; four supplementary pullback searches also returned and pinned rg inspected Finsupp Basic/Option. Their exact requests and complete receipts are `search-modern-comap-{finder,leansearch,loogle,local}.json` and `rg-modern-comap.json`. Finsupp.comapDomain needs only Zero; its application theorem is definitionally the pullback. All positive candidates used were native-checked. Exact complete request/response files `search-{current,literature,modern}-{finder,leansearch,loogle,local}.json` are preserved. Local tool reports `index: unavailable` while returning source fallback candidates; that is not an absence proof. External indices can differ from this pin; positive candidates were independently checked in native mathlib-only context.

Pinned building blocks:

* `MvPolynomial.optionEquivLeft`, Equiv.lean:467: arbitrary `CommSemiring R`, arbitrary `τ`, algebra equivalence to `Polynomial (MvPolynomial τ R)`.
* `Polynomial.coeff`, Basic.lean:562: coefficient finite-support function, `[Semiring A]`, applied to the resulting polynomial and ν.
* `Polynomial.lcoeff`, Coeff.lean:79: bundled coefficient linear map, `[Semiring A]`; restrict scalars and compose with the existing equivalence's linear map.
* `MvPolynomial.optionEquivLeft_coeff_coeff`, Equiv.lean:610: existing coefficient-coordinate theorem; associated support and degree results already use the direct coefficient spelling.

Conclusion: building blocks found; the whole new name is a two-call composite. No claim that `Polynomial.lcoeff` alone is the same whole operator. Native signatures and applications establish compatibility. [Source search current](../evidence/Roth.coeffNone/rg-current.json), [literature](../evidence/Roth.coeffNone/rg-literature.json), [modern](../evidence/Roth.coeffNone/rg-modern.json).

## Phase 5.5 — Three statement-shape checks

Normal form: REFACTOR for upstream use to `(optionEquivLeft R τ P).coeff ν`, matching existing coefficient/support/degree API. Syntactic generality: current P-first, ν-second application is readable; ν-first bundled form is useful specifically for map_add/map_smul, not a new mathematical generality. Superfluous arguments: NONE in the elaborated type. Noncomputable status reflects the canonical existing equivalence and does not add a hypothesis. SHIP-AS-STATED locally if the semantic name is retained; use existing direct form upstream.

## Phase 6.0 — Complete caller and inline audit

Canonical-inventory lexical enumeration, `rg --no-ignore` and tracked `git grep` agree: zero callers outside Separation.lean; seven consuming declarations inside it. Source spelling occurrences, consuming declarations and direct kernel-value references are separate quantities. Comments and the defining occurrence are excluded from consumer count.

| Caller | Source use | Concrete refactor validated |
|---|---|---|
| coeff_coeffNone,85–87 | Statement plus explicit unfold | Direct expression in statement; change to double-coefficient form then original optionEquivLeft_coeff_coeff rewrite. |
| eq_sum_X_none_pow_mul_coeffNone,98–107 | Expansion statement | Direct expression under rename; existing coefficient proof unchanged. |
| degreeOf_coeffNone_le,114–117 | Statement | Direct expression; same support membership proof. |
| coeff_rename_mul_aeval,123–132 | **Body-only** explicit unfolding | Same statement; change after coefficient rewrite to direct double-coefficient goal, then original map rewrites. |
| private eq_sum_aeval_basis_coeffNone_aux,265–286 | Hypothesis, basis carrier and proof | Substitute direct expression in coefficient family and all dependent basis coordinates. |
| private exists_coeffNone_basis_aux,291–316 | Hypothesis, span and proof | Substitute direct expression in span and local family; existing support-degree argument retained. |
| exists_separated_representation,322–345 | Local coefficient family / expansion | Substitute direct expression and use replayed expansion/basis lemmas. |

Exact canonical293 audit finds these same seven direct kernel consumers, including both private names, with 293 requested, 293 unique, 293 present and 293 values. This is direct value dependency, not transitive simp/kernel closure. [Canonical audit source](../evidence/Roth.coeffNone/coeff-none-audit-executed.lean.txt), [lexical inventory](../evidence/Roth.coeffNone/lexical-enumeration.json), [tracked grep](../evidence/Roth.coeffNone/caller-git-grep.json), [unignored rg](../evidence/Roth.coeffNone/caller-rg.json).

Inline audit: the private coeff_X_none_pow_mul_rename already computes coefficient behavior using direct optionEquivLeft. degreeOf_coeffNone_le and the private basis auxiliary likewise use mem_support_coeff_optionEquivLeft directly. No external independent definition of this operator was found. [Inline receipt](../evidence/Roth.coeffNone/rg-inline.json).

## Phase 6 — Actual compositions and full caller validation

Independent mathlib-only construction is the exact two-call term:

```lean
Polynomial.coeff (MvPolynomial.optionEquivLeft R τ P) ν
```

Count: one existing equivalence application and one existing coefficient projection. No normalization theorem, project lemma, search tactic or new helper proof is needed to construct this object. The actual target-to-term equality was separately checked by `rfl`; that check certifies agreement but is **not** the reason for NO. This is not a closing `simp [defs]` composition under Phase6b.

A second candidate, the bundled linear-map composition, also compiles; named application, add and smul laws plus the nonmultiplicativity guard have only standard axioms. The initial sum/filter finite-support candidate remains exploratory. The sharper comapDomain candidate compiles over Zero and its actual coefficient bridge is verified, proving the representation-level weakening. Neither is miscounted as a one-call polynomial-level equality.

All seven caller refactors were actually elaborated: **the entire Separation module** was replayed under a fresh namespace with the definition removed and every exact identifier application replaced by the direct expression. Existing theorem identifiers were preserved, two explicit unfold rewrites adapted using change, no replacement wrapper was added. Final exists_det_eq_mul also succeeds. Native complete/nonpartial receipt has zero errors and warnings, and printed axioms for all seven callers plus the final theorem are standard. Replayed source contains other project mathematics, so it is caller validation; only the isolated snippet is evidence for mathlib-only composition. [Exact caller execution](../evidence/Roth.coeffNone/coeff-none-callers-executed.lean.txt), [raw native receipt](../evidence/Roth.coeffNone/coeff-none-callers-receipt.json).

Conclusion COMPOSABLE, literally two existing calls. Native source and receipt hashes, exact execution paths and region boundaries are in [verification metadata](../evidence/Roth.coeffNone/verification.json). The first pullback attempt omitted the explicit R argument in optionEquivLeft_coeff_coeff and failed with a type mismatch and recovered sorryAx. Its source and receipt are archived as rejected; they supply no accepted proof evidence. The corrected guarded execution is clean. Other native probes succeeded on their first attempts. The unguarded corrected pullback success is preserved as supplemental evidence; the guarded success is the accepted isolated bridge.

## Phase 7 — Verdict and action

**NO-composable-from-mathlib.** The mathematical operation is standard and useful; the semantic-name exemption and all seven consumers were taken seriously. They support keeping a documented local abbreviation if desired. They do not supply mathematical content beyond the two existing operations already used verbatim throughout mathlib's option-variable API.

Existing building blocks are optionEquivLeft and Polynomial.coeff; lcoeff provides the optional bundled form. At the expanded coefficient-data level, Finsupp.comapDomain is the existing more general core over Zero, with a separately verified bridge. Every source caller has a validated direct-expression migration above. Alternative local destination: retain the documented `Roth.coeffNone` in `Roth/Separation.lean` for narrative readability, or replace it by a local `let` coefficient family in the basis proof. No production change is made by this assessment. No upstream PR or new helper API is required for this definition. This is not a cost downgrade, not a dead-code claim and not a verdict inferred from rfl alone.

YES PR title/reviewer/grouping requirements are n/a for this NO verdict. No unresolved verification or user decision is required to complete the read-only assessment.

## Phase 8 — Evidence and completion

All required phases PASS; the expanded generality claim is backed by the accepted Zero-only pullback bridge. Completed-only metadata, exact sources, complete native receipts, searches, fresh input hashes, canonical inventory, report links and current artifact manifest are checked by the [portable read-only validator](../evidence/Roth.coeffNone/validate.py). The validator checks actual native success, disk partial=false, standard axioms, canonical293 exact order and seven consumers, literal caller migration, all named search channels and the credential guard. Root performs independent acceptance before integration.
