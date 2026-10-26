# Full mathlibable assessment: `MvPolynomial.hasseCoeff_eq_prod`

**Verdict: NO-composable-from-mathlib.** The support/full-product bridge is the existing generic `Finsupp.prod_fintype` supplied with `Nat.choose_zero_right`. Keep the finite-variable binomial formula available to readers, but a separate upstream theorem about the project scalar alias contributes no new product API. This is an independent full assessment, not inheritance from `hasseCoeff`: the proof is a two-call theorem application, outside the narrow `rfl`/unfold glue rule.

## Phase 0 — Doctor

The production declaration resolves at `Roth/HasseDeriv.lean:106`, body line 107. Kind: theorem. Source has no `sorry`; the native target inspection records its elaborated type and standard axioms. The file develops characteristic-free multivariate Hasse derivatives and their coefficient/operator identities.

Baseline `lake build` PASS (2467 targets) is reused only after all 17 source/pin SHA256 checks match the shared baseline. See [baseline receipt](../evidence/MvPolynomial.hasseCoeff_eq_prod/baseline-build.txt), [manifest](../evidence/MvPolynomial.hasseCoeff_eq_prod/input-manifest.json), [source check](../evidence/MvPolynomial.hasseCoeff_eq_prod/source-check.json), and [native verification](../evidence/MvPolynomial.hasseCoeff_eq_prod/verification.json). Production sources, pins, branch, and Git are owned by the root integration gate; this worker writes scratch evidence only.

## Phase 1 — Comprehend

For lower and upper natural multiindices `d,k` on finitely many variables, the product of `choose (k j) (d j)` over the support of `d` equals the product over every variable. At any coordinate omitted from the support, `d j = 0`, so its factor is one. This is an identity of natural numbers; no coefficient semiring occurs.

Elaborated signature:

```lean
theorem MvPolynomial.hasseCoeff_eq_prod {σ : Type*} [Fintype σ] (d k : σ →₀ ℕ) :
    MvPolynomial.hasseCoeff d k = ∏ j, (k j).choose (d j)
```

`σ` is the variable type; `Fintype σ` supplies the full finite enumeration. `d,k` encode finite natural exponent families. There are no order/dominance, nonzero, nonempty, characteristic, or coefficient-ring hypotheses. The surrounding `R` and `[CommSemiring R]` are absent from the actual type. [Target source](../evidence/MvPolynomial.hasseCoeff_eq_prod/target-excerpt.lean).

## Phase 2 — Preliminary checks

SMALL: representation bridge for a scalar factor, not a new structure or a module main theorem. The theorem proof occupies one substantive line. The one-line *definition* exemption test is n/a (theorem), rather than a manufactured API-name exemption. Its short proof is a substantive composability signal, not a reason to skip any channel.

## Phase 3 — Exhaustive literature search

The complete table and original source summaries are in [literature.md](../evidence/MvPolynomial.hasseCoeff_eq_prod/literature.md), with [exact requests, outcomes and response hashes](../evidence/MvPolynomial.hasseCoeff_eq_prod/web-requests.json). Three distinct general searches ran: the multiindex Hasse binomial formula; general identity-padded products in commutative monoids; Hasse–Schmidt/divided-power aliases. Local §1 Derivatives was actually read. nLab, nCatLab, Stacks, MathOverflow and recent arXiv were each actually checked. Optional `ask_chatgpt_math` is unavailable. Direct nLab derivation XHTML was unsupported and the nCatLab path inaccessible; indexed nLab derivative/monoid material was inspected, and neither failure is negative mathematical evidence.

Primary sources: the multiindex coefficient definition on p.362 in [Cherry–Toropu](https://www.impan.pl/shop/en/publication/transaction/download/product/83782); displayed notation in [Faster Algorithms for Multivariate Interpolation With Multiplicities and Simultaneous Polynomial Approximations](https://perso.ens-lyon.fr/gilles.villard/BIBLIOGRAPHIE/PDF/ieee-2015.pdf); and essentially finite products in §2.3 p.30 of [Algebra course notes](https://user.math.uni-kiel.de/~laue/vorlesungen/algebra.introduction/alg.int.pdf). They support coordinatewise binomial products and omission of identity factors. [Stacks §23.2](https://stacks.math.columbia.edu/tag/07GK) supplies divided-power context, not a new support bridge. Recent-window searches (2021-10-26 to 2026-10-26) found active Hasse applications, including [Yu 2026](https://arxiv.org/abs/2610.10649), [He–Pham–Xu 2022](https://arxiv.org/abs/2201.06156), and [Ghosh 2024](https://arxiv.org/abs/2402.18717); the abstracts establish activity, not a changed standard for this identity. Broad-query time-series false positives were excluded.

Concept: multiindex binomial coefficient, under the generic identity-padding principle for finite products. Finite-variable full products and support products agree; the upper family need not itself have finite support. The abstract standard needs a pointed input type, commutative monoid target and `g j 0 = 1`. Over arbitrary variables a finite superset of the support suffices instead of `univ`. No operator-level historical modernization is claimed from the optional unavailable second opinion.

## Phase 4a–b — Generality

| Parameter / hypothesis | Current form | Standard / broader form | Weakening assessment |
|---|---|---|---|
| variable type | arbitrary `Type*` | arbitrary universe-polymorphic index | Already general; no concrete finite cardinal fixed. |
| enumeration | `[Fintype σ]` | finite ambient set containing support, for arbitrary `σ` | Literal `∏ j` requires an enumeration. Finite-set alternative is verified using existing `prod_of_support_subset`; it changes RHS and adds a containment premise. |
| lower order `d` | `σ →₀ ℕ` | finite natural order | Essential to support product; abstract theorem permits any zero-bearing value type. |
| upper order `k` | `σ →₀ ℕ` | arbitrary function `σ → ℕ` | Expanded statement verifies with exactly the same proof; on finite `σ` this is representation generality, and it requires expanding/changing the parent alias signature. No new product construction is needed. |
| scalar codomain | `ℕ` | arbitrary commutative monoid for identity-padding principle | Verified abstract form is already `Finsupp.prod_fintype`; binomial counting itself remains natural. |
| surrounding `R`, semiring | not in actual signature | none | No weakening claimed for hypotheses that were never parameters. |

For the fixed `hasseCoeff` signature, all actual hypotheses are needed to form the written expression. Relative to the abstract standard, the expanded product is STRICTLY NARROWER in allowed input/factor types, with verified broader witnesses. These witnesses do not produce `YES-but-generalise-first`: the abstract form already exists in mathlib, and the upper-function variant is the same two-call specialization. The broader fixed finite-variable input representation is a harmless optional parent API decision, not an unresolved blocker or a claimed new theorem.

Verified restatements in [isolated probe code](../evidence/MvPolynomial.hasseCoeff_eq_prod/probes.lean):

```lean
example [Fintype σ] (d : σ →₀ ℕ) (k : σ → ℕ) :
    d.prod (fun j ↦ (k j).choose) = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _
```

The generic statement uses `[Zero M] [CommMonoid N]`, `d : σ →₀ M`, `g : σ → M → N` and `h : ∀ j, g j 0 = 1`. It is existing API; cost of specialization is CHEAP, with no cost-based verdict argument.

## Phase 4c — Modern mathlib idiom, all nine questions

| # | Question | Answer / proposed form | Downstream consequence |
|---|---|---|---|
| 1 | Hypotheses into typeclasses? | No additional change; enumeration already a class. | Existing `Fintype` / `Finset.univ` API. |
| 2 | Sequences / metric to filters? | No; finite combinatorial identity. | No topology. |
| 3 | Constructed object to universal property? | No new object constructed. | No missing universal-property API. |
| 4 | Closure predicate to bundled substructure? | No closure predicate; Finsupp already bundles finite support. | No lattice/quotient reformulation needed. |
| 5 | Field/vector-space to semiring/module? | No ring assumption in signature; abstract target is `CommMonoid`. | Existing product API already handles the weaker structure. |
| 6 | Higher categorical generalization? | No; categorical monoid sources inspected but this is a scalar product equality. | No concrete blocked downstream proof. |
| 7 | Concrete numeric index to abstract structure? | Yes for identity-padding mechanism: pointed `M`, commutative monoid `N`, factor `g`. | `Finsupp.prod_fintype` already supplies it, including power products used in Taylor/GenWronskian. Natural choose is preserved in specialization. |
| 8 | Concrete-via-abstract adversarial diagnostic? | Yes. Actual body contains zero occurrences of `hasseCoeff` and zero applied `Nat.choose` operations (the identifier `Nat.choose_zero_right` is a separate lemma); it uses only `prod_fintype` and `choose_zero_right`, one line each. | Abstract mechanism is already mathlib, so no new theorem is exposed by abstraction. See [exact body diagnostic](../evidence/MvPolynomial.hasseCoeff_eq_prod/concrete-via-abstract.json). |
| 9 | False-generalization guard? | No false generalization in retained proposals: specializing `g j n := (k j).choose n` preserves the exact object. Changing natural choose to an arbitrary operation without `g j 0 = 1`, or changing divided-power operators/categories, is rejected. | Verified specializations retain the precise scalar identity. |

Modern idiom available: yes, already implemented by `Finsupp.prod_fintype` and `prod_of_support_subset`. Real organizational improvement: use that existing uniform API at the sole caller instead of adding a second scalar-product bridge. This does not justify an upstream modernization PR; no missing abstract API remains.

## Phase 4.5 — Diamond / defeq risk

n/a — theorem, no new definition/class/instance, coercion or definitional computation introduced. Parent-definition policy is assessed independently in its completed report.

## Phase 4.6 — Proof strategy, all five questions

| # | Check | Applies? / evidence | Alternative / cost |
|---|---|---|---|
| 1 | Topological ε–δ versus filters | No topology. | n/a |
| 2 | Element algebra versus bundled inclusions | No ideals/submodules/subrings; generic finite product theorem used directly. | n/a |
| 3 | Sequences versus nets | No limits. | n/a |
| 4 | Explicit object versus universal property | No object construction. | n/a |
| 5 | Missing helper mathlib should contain | No: generic bridge and unit binomial fact already exist and compile. | Inline existing two calls, CHEAP. |

Strategy verdict: MATHLIB-IDIOMATIC. The existing proof is already the correct shortest route modulo desirable API. The issue is packaging as an extra public theorem; no new helper or automation is required.

## Phase 5 — All five actual mathlib search methods

Current/literature binomial forms and the abstract identity-padding form were searched independently. Native pinned checks validate candidates despite external service indexes using other mathlib revisions.

| Method | Current / literature queries | Abstract query and result | Receipt |
|---|---|---|---|
| A Lean-Finder | Finite multiindex binomial product over support equals all variables; returned multinomial-related distractors | Finsupp support product equals fintype product, `g i 0 = 1`; hit `Finsupp.prod_fintype`, support subset and DFinsupp variants | [current](../evidence/MvPolynomial.hasseCoeff_eq_prod/finder-current.json), [abstract](../evidence/MvPolynomial.hasseCoeff_eq_prod/finder-abstract.json) |
| B Loogle | `Nat.choose, Finsupp.prod`: empty search result | `Finsupp.prod, Finset.prod`: `prod_fintype`, `prod_of_support_subset`, power and indicator relatives | [current](../evidence/MvPolynomial.hasseCoeff_eq_prod/loogle-current.json), [abstract](../evidence/MvPolynomial.hasseCoeff_eq_prod/loogle-abstract.json) |
| C LeanSearch | Multiindex binomial support product: returned finprod/tprod/multinomial relatives | Finitely supported function product over finite type if zero maps to one: exact generic bridge | [current](../evidence/MvPolynomial.hasseCoeff_eq_prod/search-current.json), [abstract](../evidence/MvPolynomial.hasseCoeff_eq_prod/search-abstract.json) |
| D Source grep | Full qualified/short target, scalar alias and binomial-product patterns; no target theorem in pinned mathlib source | Actual `prod_fintype` at Basic.lean:63; `prod_of_support_subset`:57; `choose_zero_right` at Choose/Basic.lean:56 | [untruncated receipts](../evidence/MvPolynomial.hasseCoeff_eq_prod/grep-receipts.json) |
| E Local name search | `hasseCoeff_eq_prod`: project theorem source hit | `prod_fintype`: pinned mathlib source hit, plus old evidence excerpt excluded as a library source | [current](../evidence/MvPolynomial.hasseCoeff_eq_prod/local-current.json), [abstract](../evidence/MvPolynomial.hasseCoeff_eq_prod/local-abstract.json) |

Local symbol index status is `unavailable`: source hits establish candidates only; no negative inference from that index. The external type signatures and local texts were tested in the pinned Lean environment. `Finsupp.multinomial` is a factorial ratio counting all rearrangements, not the coordinatewise binomial product, so is not a replacement. Finprod, tprod and DFinsupp are related general infrastructures, unnecessary for the exact two-call route. There is no universal absence claim or reliance on failure of search automation. Conclusion: found building blocks, composition yields exact target.

## Phase 5.5 — Statement shape, all three checks

**Normal form.** Equivalent presentations: alias equals full product; expanded Finsupp support product equals full product; reversed equality; finite-superset product. `Finsupp.prod_fintype` already chooses support product on the LHS and full product on the RHS. Current orientation is appropriate for rewriting into `Finset.prod_*` estimates, as at the sole caller. Normal form: OK, not an orthogonal equivalence web.

**Syntactic generality.** Actually attempted: explicit unfolded product; upper ordinary-function version; generic factor version; finite ambient set; whole sole-caller proof with the wrapper replaced. For the current caller, a typed `show` equality or `change` to the expanded product is easier than introducing new bundle/argument ordering. Chosen local route: existing `d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _)`; finite-superset alternative is reserved for arbitrary index types.

**Superfluous argument audit.** `σ` needed as index; `Fintype σ` needed for literal full product; `d` supplies support and lower orders; `k` supplies upper values. Finite support of `k` is a representation restriction rather than a necessary mathematical hypothesis; its ordinary-function extension was verified. No `R` / semiring argument exists to drop, no decidable equality or nonempty assumption added. Overall fixed interface: SHIP-AS-STATED as a local rewrite interface, but no separate upstream shipment is recommended. Expanded ordinary-function representation is optional if the parent scalar API is redesigned; existing abstract API already covers it.

## Phase 6.0 — Complete caller and inline audit

| Caller | File / declaration / invocation | Usage |
|---|---|---|
| `MvPolynomial.hasseCoeff_le_two_pow` | `Roth/HasseDeriv.lean:276`, invocation at 278 | `rw [hasseCoeff_eq_prod, ← Finset.prod_pow_eq_pow_sum]` before coordinatewise choose bounds. |

One explicit invocation in one caller, same file. Internal use count under the command's *excluding declaring file* definition: 0; external-to-file caller files: 0. The same-file caller is nevertheless counted in the refactor plan. Fully qualified, unqualified and dot-notation patterns were searched across the 14 production sources and canonical inventory; declaration/doc occurrences were excluded. No external-library caller claim is made, and opaque tactic/kernel dependency closure is not asserted.

Inline re-derivation grep: no identical full-variable binomial bridge found elsewhere. Related routes are `hasseCoeff_mul_hasseCoeff` at lines 159–163 (finite support-superset product extension with unit binomial factors), `MvPolynomial.eq_sum_box_hasseDeriv` proof at Taylor:212 (generic full product of powers), and `kronecker_monomial` at GenWronskian:62 (generic power-product simplification). These are not additional target callers and are not refactor obligations. [Source/caller metadata](../evidence/MvPolynomial.hasseCoeff_eq_prod/source-evidence.json), [grep receipts](../evidence/MvPolynomial.hasseCoeff_eq_prod/grep-receipts.json).

## Phase 6 — Composition

Attempt 1 succeeds, two mathlib calls:

```lean
example [Fintype σ] (d k : σ →₀ ℕ) :
    d.prod (fun j ↦ (k j).choose) = ∏ j, (k j).choose (d j) :=
  d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _
```

`Finsupp.prod_fintype` is at `Mathlib/Algebra/BigOperators/Finsupp/Basic.lean:63`; `Nat.choose_zero_right` at `Mathlib/Data/Nat/Choose/Basic.lean:56`. [Pinned excerpts](../evidence/MvPolynomial.hasseCoeff_eq_prod/mathlib-prod-excerpt.lean), [choose excerpt](../evidence/MvPolynomial.hasseCoeff_eq_prod/mathlib-choose-excerpt.lean). Definitional elaboration unfolds the local scalar alias for the original target; it is not a new proof in disguise. No induction, branching, ring reasoning or tactic search is hidden in this composition.

The same exact statement and full caller rewrite were verified with project imports, and the expanded statement, broader witnesses and full caller inequality with mathlib-only imports. The isolated probes contain no `Roth` import or project target declaration. The first isolated run rejected the whole caller because the narrow imports omitted `Mathlib.Data.Nat.Choose.Bounds`; its raw receipt and source are retained as a rejected attempt, including its recovery `sorryAx`. The corrected final run adds that production import and succeeds for all five named witnesses with standard axioms. The persistent target/caller disk retains two earlier unrelated style warnings; it is not claimed warning-free. Actual successful native receipts and axiom observations are indexed in [verification.json](../evidence/MvPolynomial.hasseCoeff_eq_prod/verification.json). Conclusion: COMPOSABLE.

## Phase 7 — Verdict and refactor-actionable next action

**NO-composable-from-mathlib.** The theorem specializes a zero-to-one support-product bridge using an independent natural-binomial unit fact. The literal binomial bridge is not identified as a bare already-existing named theorem: using two named facts makes the composable bucket precise. If one regards the supplied unit proof as specialization bookkeeping, the practical conclusion is the same, but the selected verdict explicitly counts it. No unresolved mathematical taste or cost question is needed for this two-call route.

WHY not add: `Finsupp.prod_fintype` already handles all pointed inputs and commutative product targets, while `Nat.choose_zero_right` supplies exactly the omitted-coordinate condition. The verified upper-function and finite-superset forms also reduce directly to existing API; they reveal no missing theorem. Literature confirms the formula's meaning but does not justify duplicating the generic bridge under an alias already assessed as unsuitable for standalone upstream addition. This verdict does not inherit the parent's verdict or prejudge the independently accepted Hasse operator/coefficient identity.

Belongs elsewhere: the formula is useful exposition and may remain a **project-local semantic/package interface** in `Roth/HasseDeriv.lean` while the scalar alias is kept. Standalone upstream addition is unnecessary. It is not dead mathematical code: the bound theorem uses it once.

Refactor plan covers **every explicit caller (one)**. In `MvPolynomial.hasseCoeff_le_two_pow` (`Roth/HasseDeriv.lean:276–280`), replace the wrapper rewrite by:

```lean
  rw [show hasseCoeff d k = ∏ j, (k j).choose (d j) from
    d.prod_fintype _ (fun _ ↦ Nat.choose_zero_right _), ← Finset.prod_pow_eq_pow_sum]
```

The rest of the caller is unchanged. If the parent alias is also removed, use the expanded product as the theorem's LHS and the fully isolated caller proof in `probes.lean`; if it is retained, the typed equality above preserves its signature. Delete `hasseCoeff_eq_prod` only after that caller migration, then run the project build. Record the two generic product facts in module documentation when implementing the refactor. No other production caller requires adjustment. This assessment proposes the change; no production edits are made.

Phase 7 gate: all nine literature channels attempted; all five actual mathlib methods; all nine modern-idiom rows; risk n/a justified; all five strategy rows; all three shape checks; explicit caller table and inline audit; successful exact and isolated composition witnesses; full NO refactor/alternative destination; no unavailable-index absence inference. No `sorry`, new axiom, unsafe proof, native decision procedure or raised elaboration limit is used in successful witnesses.

## Phase 8 — Evidence and completion scope

[Assessment](../evidence/MvPolynomial.hasseCoeff_eq_prod/assessment.json), [overview entry](../evidence/MvPolynomial.hasseCoeff_eq_prod/overview-entry.json), [verification](../evidence/MvPolynomial.hasseCoeff_eq_prod/verification.json), [copy manifest](../evidence/MvPolynomial.hasseCoeff_eq_prod/copy-manifest.json), [portable validator](../evidence/MvPolynomial.hasseCoeff_eq_prod/validate.py). Reports are frozen only after actual native success, hash, link and validation gates. Root acceptance/integration is a separate gate. Optional unavailable ChatGPT, external index revision differences, nLab/nCatLab access failures, and explicit-only caller scope remain recorded limitations, not mathematical evidence of absence.
