# Roth.eq_mapDomain_some_add_single

**NO-composable-from-mathlib.** The additive reconstruction with `embDomain` is an explicit three-call composition. The project’s `mapDomain` spelling needs one additional representation theorem; it is not claimed to be a three-call term. Its sole caller can avoid the decomposition entirely using the existing polynomial coefficient correspondence. No production edits were made.

## Phase 0 — Doctor

Declaration153 resolves at Roth/Separation.lean:57. Baseline `lake build` succeeded; all17 production/pin hashes freshly match. The newer complete Index build also succeeded on exactly these inputs. Original native diagnostics are complete/nonpartial with no errors/warnings and standard axioms only. [Hashes](../evidence/Roth.eq_mapDomain_some_add_single/inputs.json), [build](../evidence/Roth.eq_mapDomain_some_add_single/index-file-completion-2026-10-27.json), [native](../evidence/Roth.eq_mapDomain_some_add_single/option-exponents-original-audit-receipt.json).

## Phase 1 — Comprehend

A finitely supported natural-valued function on a set with one extra distinguished point is its restriction extended by zero, plus the singleton carrying its value at that point. Evaluation at `none` gives `0 + d none`; at `some j` it gives `d (some j) + 0`. This is coordinate decomposition, independent of polynomial coefficients or the Roth theorem.

Full native type:

```lean
@Roth.eq_mapDomain_some_add_single : ∀ {τ : Type u_1} (d : Option τ →₀ ℕ),
  d = Finsupp.mapDomain some d.some + Finsupp.single none (d none)
```

Parameters: arbitrary universe-polymorphic τ and multi-index d. No hypotheses or instances, including no `Fintype τ`, `DecidableEq τ`, or `CommSemiring R`, survive elaboration. The source proof uses extensionality and the two Option constructors. [Complete module](../evidence/Roth.eq_mapDomain_some_add_single/Roth-Separation.lean.txt).

## Phase 2 — Preliminary checks

SMALL: elementary coordinate helper, no new structure, named theorem, or main-result status. One-line definition-only test and its three exemptions are n/a because this is a theorem. The proof is three substantive tactic lines; length alone does not decide inclusion.

## Phase 3 — Exhaustive literature

Every query below was actually executed; receipts retain exact requests, response hashes/bytes, primary locators and original concise summaries, without full web bodies. `ask_chatgpt_math` is unavailable, so the historical-formulation channel is explicitly n/a.

| Channel | Exact query / evidence | Finding |
|---|---|---|
| General web specific | `finitely supported functions Option restriction single distinguished coordinate decomposition` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-web-specific.json) | Mostly analytic-support material; no exact algebraic hit |
| General web broad | `finitely supported functions disjoint union direct sum decomposition` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-web-general.json) | Direct sums as finitely supported functions; nominal-set support is a different notion |
| General web alias | `free commutative monoid coproduct disjoint union finite support functions` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-web-alias.json) | Bourbaki Algebra I §7.7 supplies relevant free commutative monoid context |
| Local source | clean.tex Lemma2, lines347–435 [excerpt](../evidence/Roth.eq_mapDomain_some_add_single/clean-separation-excerpt.tex.txt) | Collect powers of the distinguished variable; multi-index splitting is implicit bookkeeping |
| nLab | `site:ncatlab.org/nlab free commutative monoid disjoint union` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-nlab.json) | Free commutative monoid and disjoint-union pages, related context |
| nCatLab | `site:ncatlab.org/ncatlab finitely supported functions coproduct` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-ncatlab.json) | Returned /nlab pages; no in-namespace exact hit |
| Stacks | `site:stacks.math.columbia.edu polynomial ring variables partition` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-stacks.json) | General algebra and blow-up material; no exact reconstruction theorem |
| MathOverflow | `site:mathoverflow.net finitely supported functions direct sum disjoint union` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-mo.json) | Related direct-sum/product discussions; no exact hit |
| Recent arXiv | `site:arxiv.org free commutative monoid disjoint union 2022 2023 2024 2025 2026` [receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-arxiv.json) | 2023 papers2311.03808,2311.06901,2308.15183 are within five years; no exact Option identity |

The [primary access receipt](../evidence/Roth.eq_mapDomain_some_add_single/literature-primary-access.json) records Bourbaki’s PDF rejected for excessive content length and nLab’s XHTML fetch failure. The accessible [mathlib Option documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Finsupp/Option.html) explicitly identifies restriction/reconstruction. Pinned local source and native signatures settle its actual generality. No inaccessible paper is claimed to have been read.

Literature synthesis: coordinate splitting across a disjoint union, equivalently the free commutative monoid/direct-sum decomposition. Natural numbers encode polynomial exponents, but reconstruction only needs a zero-valued target; additive spelling requires zero laws. No conflicting standard form was established. This conclusion is supported positively by formal API, not inferred from empty searches.

## Phase 4a — Generality

| Parameter / interface | Current | Verified wider form | Boundary |
|---|---|---|---|
| τ | Arbitrary Type u | Already arbitrary | No finiteness or equality decision needed |
| d | Option τ →₀ ℕ | Option τ →₀ M | Finite support built into Finsupp |
| coefficient algebra | ℕ | AddCommMonoid M | Fixed mapDomain interface requires finite sums |
| injection representation | mapDomain some | embDomain .some, AddZeroClass M | Injective extension itself needs no summation |
| reconstruction normal form | sum plus singleton | optionElim, Zero M | No addition at all |
| distinguished index | none | Any chosen point after an equivalence with Option | Changing public indexing representation is a restatement, not an omitted instance |
| ambient R | None in type | n/a | Section CommSemiring is not retained |

## Phase 4b — Verified weakening

STRICTLY NARROWER THAN STANDARD. All three meaningful coefficient floors compile: original syntax under AddCommMonoid; injection syntax under AddZeroClass; canonical optionElim under Zero. Independent pointwise generalized proof, exact canonical hit, and representation bridge are separately present in [isolated executed source](../evidence/Roth.eq_mapDomain_some_add_single/option-exponents-isolated-executed.lean.txt) and [successful raw receipt](../evidence/Roth.eq_mapDomain_some_add_single/option-exponents-isolated-receipt.json). The AddZeroClass claim changes mapDomain to embDomain; it is not a claim that mapDomain accepts AddZeroClass. No ring/group/order/nontriviality assumptions are needed. Cost CHEAP; no verdict is based on cost.

## Phase 4c — Modern idiom

| # | Question | Answer and concrete consequence |
|---|---|---|
| 1 | Bundled hypotheses to typeclasses | No hypotheses to bundle; wider coefficient structures use existing classes |
| 2 | Sequences versus filters | n/a purely algebraic |
| 3 | Construction versus universal property | Existing optionEquiv packages inverse reconstruction; no new universal-property class |
| 4 | Set predicates versus substructures | No such predicates |
| 5 | Vector-space/field hierarchy | No scalar field; arithmetic ℕ weakens to AddCommMonoid, or AddZeroClass with embeddings |
| 6 | Higher categorical | No benefit for coordinate equality; abstract coproduct context is explanatory |
| 7 | Concrete index/coefficients | Yes ℕ is the coefficient value type here, not τ; general M composes with arbitrary Finsupp data |
| 8 | Concrete-via-abstract diagnostic | Yes: proof never uses Nat induction/order/multiplication; only injection and zero/addition evaluations. Verified mapped proof retains identical tactic strategy for M |
| 9 | False-generalisation guard | No semantic mismatch in proved proposals: ℕ specializes exactly, embDomain_eq_mapDomain supplies actual bridge. Dropping distinguished singleton is false by compiled omission_guard |

Canonical form `d.some.optionElim (d none) = d` is already mathlib’s simp reconstruction law. It composes directly with optionEquiv and the MvPolynomial coefficient API. Embedding syntax removes unnecessary sum structure and serves AddZeroClass targets. No higher abstraction is proposed just for appearance.

## Phase 4.5 — Infrastructure risk

n/a: theorem introduces no data, definition or instance. Typeclass diamonds, reducibility leaks, unfolding conventions, priority collisions, universe-forcing definitions, and coercion ambiguity are all outside this declaration’s scope. Native wider proofs are universe-polymorphic.

## Phase 4.6 — Proof strategy

| # | Diagnostic | Finding |
|---|---|---|
| 1 | ε–δ versus filters | n/a |
| 2 | Elements versus substructures | Pointwise extensionality is idiomatic for Finsupp equality; existing inverse law avoids repeating it |
| 3 | Sequences versus nets | n/a |
| 4 | Construction versus universal property | Existing optionEquiv inverse supplies reconstruction; no new construction required |
| 5 | Missing helper API | No reconstruction gap; optional additive normal-form naming remains a design choice |

REFACTOR-RECOMMENDED, CHEAP: use existing inverse/update APIs, or eliminate the sole call through the canonical polynomial coefficient law. The latter is strictly cleaner and fully replayed. Cost does not determine the verdict.

## Phase 5 — All five mathlib methods

All methods ran on current, literature-standard and modern embedding/update forms. [Complete raw formal-search receipts index](../evidence/Roth.eq_mapDomain_some_add_single/formal-search.json).

| Method | Current | Literature | Modern |
|---|---|---|---|
| Lean-Finder | Option equivalence and optionElim candidates | sumFinsuppEquivProdFinsupp | optionEquiv inverse/update candidates |
| Loogle | mapDomain + some empty | optionElim_some exact canonical hit | Initial rate limit; [successful retry](../evidence/Roth.eq_mapDomain_some_add_single/search-modern-loogle-retry.json) returns update_eq_add_single |
| LeanSearch | sum_option_index, optionElim | optionElim_some, optionEquiv | update_eq_erase_add_single, update variants |
| rg | [current](../evidence/Roth.eq_mapDomain_some_add_single/rg-current.json) | [literature](../evidence/Roth.eq_mapDomain_some_add_single/rg-literature.json) | [modern](../evidence/Roth.eq_mapDomain_some_add_single/rg-modern.json) |
| Local name search | mapDomain_some empty | optionElim_some found | update_eq_add_single found |

Local index reports unavailable even when source fallback returns candidates; this is not absence evidence. External results can differ from the pin. Exact existing candidates were read in pinned sources and #checked/used natively: Finsupp.optionElim_some (Data/Finsupp/Option.lean:148), embDomain_some_none (:94), update_eq_add_single (Algebra/Group/Finsupp.lean:230), embDomain_eq_mapDomain (Data/Finsupp/Basic.lean:422). No exact old additive mapDomain spelling is asserted to have been found.

## Phase 5.5 — Statement shape

Normal forms considered: additive mapDomain split, additive embDomain split, optionElim reconstruction, optionEquiv inverse law. Existing canonical form is the inverse/reconstruction law with full d on RHS; project statement reverses that orientation and expands it for exponents. Normal-form REFACTOR for upstream use; preserve expanded exponents only where meaningful for derivative statements.

Syntactic alternatives actually compiled are the canonical, embedding, mapped, and bridge theorems in the isolated source. Chosen local caller restatement bypasses all these splits via `optionEquivLeft_coeff_some_coeff_none`. Superfluous argument audit: τ and d are essential; no instance to drop from original native type. ℕ is a verified specialization rather than a redundant hypothesis. Overall RESTATE-BEFORE-SHIP; there is no proposed upstream shipping action.

## Phase 6.0 — All callers and inline audit

[Ignore-proof rg](../evidence/Roth.eq_mapDomain_some_add_single/caller-rg.json), [tracked git grep](../evidence/Roth.eq_mapDomain_some_add_single/caller-git-grep.json), and [fresh canonical-source lexical inventory](../evidence/Roth.eq_mapDomain_some_add_single/lexical-enumeration.json) agree: one declaration and one use. Internal use count excluding declaring file0; same-file use1; external-to-file files0.

| Caller | Original use | Concrete refactor |
|---|---|---|
| Roth/Separation.lean:107, eq_sum_X_none_pow_mul_coeffNone | `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` | Replace with `rw [Roth.coeffNone, optionEquivLeft_coeff_some_coeff_none]` in the true branch |

The complete caller, including its private coefficient helper, was independently replayed with that replacement. [Exact source](../evidence/Roth.eq_mapDomain_some_add_single/option-exponents-caller-executed.lean.txt), [receipt](../evidence/Roth.eq_mapDomain_some_add_single/option-exponents-caller-receipt.json). Its private helper is referenced through the actual constant via a term elaborator; it does not depend on this theorem. No project lemma is counted as a mathlib building block.

Inline audit found the related coordinate normalization in coeff_coeffNone at86; it identifies inserted coordinates with optionElim, rather than re-proving full reconstruction of arbitrary d. Other mapDomain-plus-single occurrences in Separation and Theta are constructions of exponents, not hidden theorem consumers. [Search](../evidence/Roth.eq_mapDomain_some_add_single/rg-inline.json).

Fresh canonical kernel-value audit checks exact order293/293 unique/present/value-bearing, preserving private names; sole direct consumer is Roth.eq_sum_X_none_pow_mul_coeffNone. [Audit source](../evidence/Roth.eq_mapDomain_some_add_single/option-exponents-audit-executed.lean.txt). Source references and direct kernel consumers are separate audited quantities, not an opaque transitive/simp closure claim.

## Phase 6 — Actual composition experiments

The following is an explicit existing-call term, not automation unfolding definitions:

```lean
example [AddZeroClass M] (d : Option τ →₀ M) :
    d = d.some.embDomain .some + Finsupp.single none (d none) :=
  (Finsupp.optionElim_some d).symm.trans
    (Finsupp.update_eq_add_single (Finsupp.embDomain_some_none d.some) (d none))
```

Exactly three mathlib theorem calls: inverse reconstruction, zero at the excluded coordinate, update as addition. Definitional reduction of optionElim exposes its inverse update; no new normalization lemma is assumed. COMPOSABLE for the representation with maximal additive generality.

Separately, original mapDomain spelling was derived via embDomain_eq_mapDomain and congrArg. That proof uses four existing theorem dependencies including the zero-value premise. A compact displayed term using `by simp` for that premise does not erase the fourth dependency. The explicit bridge was compiled and is evidence, not an alleged pre-existing named theorem. The fully independent extensional proof was also compiled at AddCommMonoid M.

Canonical Zero reconstruction is the existing one-call `(Finsupp.optionElim_some d).symm`. It differs from the old additive spelling; the distinction is why the verdict here is NO-composable rather than claiming an exact old-form NO-mathlib-has-it hit. No closing `simp [defs...]` is used as the verdict evidence. In the actual project the sole consumer needs only the existing polynomial coefficient law, as the full caller replay establishes.

False-generalisation check: omission_guard proves single none1 cannot equal its lifted some restriction. In addition, the mapDomain typeclass requirement is preserved in the generalized old spelling; no AddZeroClass instance magic is assumed.

## Phase 7 — Verdict

**NO-composable-from-mathlib**, grounded in the explicit three-call embedding normal form, verified old-form bridge, and complete deletion/refactor of the sole caller through existing canonical polynomial API. The arithmetic specialization adds no new mathematical law. This is not verdict inheritance from coeffNone, which was a separate definition assessment.

Action: delete eq_mapDomain_some_add_single after changing Roth/Separation.lean:107 as shown. No other explicit caller needs updates. Generalized reconstruction belongs to existing Finsupp Option API, with the three-call term above; optional explanatory exponent identity belongs in the local Separation module documentation, not Archive or a new mathlib wrapper. An additive bridge name could be considered separately if broader consumers emerge, but it is not necessary for the present caller. No PR location/title/reviewer grouping is applicable to a NO verdict. All required checks complete; root acceptance remains pending.

## Phase 8 — Report and validation

[Assessment](../evidence/Roth.eq_mapDomain_some_add_single/assessment.json), [verification](../evidence/Roth.eq_mapDomain_some_add_single/verification.json), [overview entry](../evidence/Roth.eq_mapDomain_some_add_single/overview-entry.json), [portable validator](../evidence/Roth.eq_mapDomain_some_add_single/validate.py). All raw successful native evidence, exact executed sources, search receipts, input hashes and copy manifest are retained. Production/Git/progress remained untouched.
