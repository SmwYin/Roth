---
decl: Roth.index_rename
file: Roth/Index.lean
line: 212
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: ind(rename f P; α; r) = ind(P; α∘f; r∘f) for injective f, about the project-only def Roth.index, is a 5-rewrite chain (project taylor_rename, mathlib support_rename_of_injective, Finset.coe_image, Set.image_image, weight via Finsupp.sum_mapDomain_index_inj), the exact min-analogue of mathlib's weightedTotalDegree_rename_of_injective; hf is necessary (compiled counterexample), so nothing goes upstream.
action: Keep in Roth/Index.lean as the source-requested renaming-invariance lemma (callers Roth/Theta.lean:154 and Roth/Theta.lean:442 twice); do not upstream; if Roth.weight_mapDomain loses its superfluous hf, keep passing hf here since support_rename_of_injective needs it.
---

# Roth.index_rename

## Inventory entry

### `theorem Roth.index_rename`
- **Type**: `{σ : Type*} [Fintype σ] {τ : Type*} [Fintype τ] {f : σ → τ} (hf : Function.Injective f) (P : MvPolynomial σ ℝ) (α : τ → ℝ) (r : τ → ℕ) : Roth.index (rename f P) α r = Roth.index P (α ∘ f) (r ∘ f)`
- **What**: Embedding a real polynomial into a larger set of variables by an injective renaming does not change its Roth index, provided the point and the weights are pulled back along the renaming.
- **How**: Unfolds both indices (`sInf` of `weight r` over the support of the translate). `MvPolynomial.taylor_rename` (project) turns `taylor α (rename f P)` into `rename f (taylor (α ∘ f) P)`. Mathlib's `MvPolynomial.support_rename_of_injective hf` turns the support into `Finset.image (Finsupp.mapDomain f) _`, and `Finset.coe_image` with `Set.image_image` reduce the problem to a pointwise equality of weights. That equality is `Roth.weight_mapDomain hf r d` (project).
- **Hypotheses**: `hf : Function.Injective f`, which is necessary (evidence (1)). `[Fintype τ]` is needed because `index` is defined on `τ`. No positivity is needed on `r`, and no nonvanishing is needed on `P`.
- **Uses from project**: `Roth.index`, `Roth.weight` (via the unfolded `index`), `MvPolynomial.taylor`, `MvPolynomial.taylor_rename` (Roth/Taylor.lean:164), `Roth.weight_mapDomain` (Roth/Box.lean:127)
- **Used by**: Roth/Theta.lean:154 (`simp [map_rename, index_rename e.injective, Function.comp_def]`, an equivalence relabelling) and Roth/Theta.lean:442 (used twice, `index_rename (Option.some_injective _)` and `index_rename hinjV`, in the disjoint-variable product step). It is also mentioned in the module docstring at Roth/Index.lean:39. There are no other uses (`grep -rn index_rename Roth/`).
- **Visibility**: public
- **Lines**: 208-219 (docstring 208-211, statement 212-214, proof 215-219), proof length 5 lines
- **Notes**: Formalises the "embedded polynomial keeps its index" step in the proof of clean.tex Lemma 4-2 (clean.tex:614-624). The Lean note at clean.tex:627-634 asks for "invariance under nonzero scalars and variable renaming ... as separate lemmas". The pointwise helper `Roth.weight_mapDomain` carries a superfluous `hf` (see Roth.weight_mapDomain.md), but this lemma needs `hf` anyway for `support_rename_of_injective`.

## Junk check (Step 8)
- Used anywhere? Yes, 3 uses at 2 sites in Roth/Theta.lean (lines 154 and 442).
- Wrapper of 1-2 mathlib calls? No. It is a 5-step rewrite chain combining the project's `taylor_rename` and `weight_mapDomain` with mathlib's `support_rename_of_injective`.
- Does mathlib have it? Not for `Roth.index`, which is project-only. Mathlib has the max-analogue `MvPolynomial.weightedTotalDegree_rename_of_injective` (Mathlib/RingTheory/MvPolynomial/Homogeneous.lean:78), proved the same way. Mathlib has no weighted order for `MvPolynomial` and no `weightedOrder`/`rename` lemma for `MvPowerSeries`.
- Too specific (inline)? No. It has three uses, and it is a source-requested separate lemma.
- Well-chosen? Yes. `hf` is necessary, and the pull-back form `(α ∘ f) (r ∘ f)` matches the mathlib convention of `weightedTotalDegree_rename_of_injective`.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The declaration is public.
- The name does not end `_aux`.
- The docstring does not start internal/auxiliary.
- Step 8 said KEEP.
- `Roth.index_rename` is not in mathlib (there is no `namespace Roth` in `.lake/packages/mathlib/Mathlib/`).

The proof is a rewrite chain, not glue, so this lemma gets a full run. The parent `Roth.index` is BORDERLINE-needs-human rather than NO-mathlib-has-it, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief, and the evidence file importing `Roth.Index` elaborates with no errors)
- decl `Roth.index_rename`:  resolved at Roth/Index.lean:212
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_rename` is a theorem stating the following:

Let σ ⊆ τ be finite variable sets via an injective map `f : σ → τ`, let `P ∈ ℝ[x_j : j ∈ σ]`, `α ∈ ℝ^τ` and `r ∈ ℕ^τ`. View `P` as a polynomial in the τ-variables by `x_j ↦ x_{f(j)}`. Then the index of the embedded polynomial at `α` with weights `r` equals the index of `P` at the restricted point `(α_{f(j)})_j` with the restricted weights `(r_{f(j)})_j`.

Variables / typeclasses involved (Lean side):
- `σ`, `τ` with `[Fintype]`: the small and large variable sets.
- `f`: the renaming.
- `P`: the polynomial.
- `α`: the point.
- `r`: the weights on τ.

Hypotheses (Lean side):
- `hf : Function.Injective f`. A non-injective `f` can merge monomials and cancel them.

Conclusion (math): the index is invariant under injective variable renaming, with the point and weights pulled back.

Conclusion (Lean): `index (rename f P) α r = index P (α ∘ f) (r ∘ f)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic invariance property of a project definition, used as one step inside the proof of source Lemma 4-2. It is not a main result and is not named after anyone.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of polynomial invariant under change of variables embedding into more variables | no | none | the results were about invariant polynomials under group actions, which is unrelated. Roth-index texts treat the embedding step as immediate (e.g. the proof of the disjoint-variable product formula) |
| 2 | WebSearch (general form) | order of vanishing multivariate polynomial unchanged under injective renaming of variables weighted order monomial valuation | partial | weighted order = min over the support of the weight of the monomial (arXiv 2604.16698, weighted blow-ups). The order is preserved when the weights are transported along the renaming | this is the general form: a monomial valuation is natural in the variable set |
| 3 | WebSearch (aliases: weighted multiplicity, Bombieri–Gubler index) | weighted multiplicity polynomial at a point extension of scalars adjoining variables invariant Bombieri Gubler index | partial | multiplicity at a point = least degree of a nonzero Taylor term (arXiv 2609.01268) | no explicit renaming statement. The fact is regarded as definitional |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for "renam", "Lemma 4-2" | yes | clean.tex:620-622: when P is embedded into the larger ring, "its index is unchanged". clean.tex:632 asks to prove "invariance under nonzero scalars and variable renaming" separately | the Lean statement is the source's step, generalised from "add one variable" to any injective renaming |
| 6 | nLab | valuation / monomial valuation | no | abstract valuations only | nothing about changing the variable set |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (naturality in the variable set is the only categorical content, and it is trivial) |
| 8 | Stacks Project | order of vanishing, polynomial ring extension (tag 02MB area) | no | order of vanishing is compatible with flat extension of the ring | not the weighted multi-index form |
| 9 | MathOverflow / Math.SE | covered by searches 2-3 | no | n/a | too elementary for a dedicated thread |
| 10 | recent arXiv | Roth index / weighted order (results of 2-3) | partial | index as weighted multiplicity. Renaming invariance is used implicitly | no standalone statement |

### Literature summary (Phase 3)

Concept identified as: naturality of a weighted (monomial) order of vanishing at a point with respect to injective changes of the variable set, i.e. adjoining variables does not change the order when the weights are transported along.
Sources agree on the standard form: yes. They treat it as immediate from "order = min of the weight over the support" together with "an injective renaming maps the support bijectively".
Most general standard form: for any coefficient ring and any weights, `ord_{α,w}(rename f P) = ord_{α∘f, w∘f}(P)` for injective `f`. This is the min-counterpart of the weighted-degree statement `wdeg_w(rename f P) = wdeg_{w∘f}(P)`.
Generality dimensions where the literature varies:
  - coefficients: any commutative (semi)ring vs `ℝ` (project). Here it is fixed by the parent def `Roth.index`.
  - weights: ℕ, ℝ≥0 or real. The project uses `1/r_j` with junk `r_j = 0`, and the lemma holds for all `r`.
  - map: injective map vs equivalence. Injective is the most general form, and non-injective maps fail.
Disagreement with the literature: none.

### Generality analysis — `Roth.index_rename`

Literature-standard form: `ord_{α,w}(rename f P) = ord_{α∘f,w∘f}(P)` for injective `f`, any weights, any coefficients.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hf : Function.Injective f` | required | injective | NO | evidence (1): `f : Bool → Unit`, `P = X true - X false`, `α = 0`, `r = 1`. Then `rename f P = 0`, so the LHS is `index 0 = 0`, while the RHS is nonzero by `index_eq_zero_iff` (compiled) |
| 2 | `[Fintype τ]`, `[Fintype σ]` | required | finite variable sets | NO (for this def) | `Roth.index`/`Roth.weight` sum over `Fintype` |
| 3 | `r : τ → ℕ` | arbitrary | any weights | already general | the proof does not use positivity |
| 4 | `P` | arbitrary | arbitrary | already general | `P = 0` is fine (both sides are `index 0 = 0`) |
| 5 | ring `ℝ` | fixed | any ring | not for this statement | it is fixed by the parent def `Roth.index`, assessed separately |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (relative to the parent def). The only hypothesis, `hf`, is necessary (compiled counterexample).
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | `Function.Injective f` is standard (cf. `weightedTotalDegree_rename_of_injective`) | — |
| 2 | Sequences vs filters? | no | finite algebraic statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | yes in principle | any `CommSemiring` | this belongs to the parent-def question (`Roth.index` is ℝ-only and BORDERLINE) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | — | — |
| 8 | Concrete-via-abstract? | yes (the diagnostic fires) | after `rw [index, index, ...]`, `index` never reappears. The content is "`support_rename_of_injective` + `taylor_rename` + weights pulled back". The abstract form "a min over the support of a weight is natural under injective rename" is the min-twin of mathlib's `weightedTotalDegree_rename_of_injective` | it would require a new mathlib def (an `MvPolynomial` weighted order), which is the parent's BORDERLINE question |
| 9 | False-generalisation guard | no false generalisation | — | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the abstract content is mathlib's `support_rename_of_injective` plus pointwise weight transport. A cleaner "weighted order of `MvPolynomial` is natural under `rename`" lemma would only make sense after adding an upstream weighted-order def, which is the parent `Roth.index`'s BORDERLINE question and not this lemma's.

### Proof strategy — `Roth.index_rename`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the proof mirrors `weightedTotalDegree_rename_of_injective` (support image, then pointwise weight). Evidence (2) shows that the weight step can use mathlib's `Finsupp.sum_mapDomain_index_inj` directly | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It has the same shape as mathlib's `weightedTotalDegree_rename_of_injective`. It works on supports directly and needs no `0 < r j`, unlike a route through `index_eq_weightedOrder_div`.
  - Missing mathlib API: none for this lemma.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_rename`

[A] Lean-Finder       "weighted order of rename of polynomial by injective map equals weighted order with composed weights"   hits: `MvPolynomial.weightedTotalDegree_rename_of_injective` (the max-analogue), `degreeOf_rename_of_injective`, `degrees_rename_of_injective`, `MvPowerSeries.le_weightedOrder_subst_of_forall_ne_zero` (an inequality for substitution), `IsHomogeneous.rename_isHomogeneous_iff`
[B] Loogle            `MvPolynomial.rename, MvPolynomial.support, Function.Injective`   hits: `MvPolynomial.support_rename_of_injective` (the building block), `support_rename_killCompl_subset`
[C] LeanSearch        "order of vanishing of polynomial unchanged under injective renaming of variables"   hits: `degreeOf_rename_of_injective`, `pderiv_rename`, `degrees_rename_of_injective`, `rename_isHomogeneous_iff`. There is no order-of-vanishing version
[D] Grep mathlib src  `weightedOrder.*rename`, `rename.*weightedOrder`, `order_rename`, `weightedTotalDegree_rename`, `support_rename_of_injective`, `mapDomain_index_inj`. Hits: `support_rename_of_injective` (Mathlib/Algebra/MvPolynomial/Rename.lean:381), `weightedTotalDegree_rename_of_injective` (Mathlib/RingTheory/MvPolynomial/Homogeneous.lean:78), `Finsupp.prod_mapDomain_index_inj`/`sum_mapDomain_index_inj` (Mathlib/Data/Finsupp/Basic.lean:430). There is no weightedOrder-under-rename lemma (Mathlib/RingTheory/MvPowerSeries/Rename.lean defines `MvPowerSeries.rename` but has no order lemmas)
[E] Name pattern      `Roth.index_rename`, `index_rename`   no mathlib decl (no `namespace Roth` in mathlib)

Searched for both:
  - the user's current form (Roth index invariant under injective renaming)
  - the literature-standard form (weighted order of vanishing natural in injective renaming)

Concluded: found building blocks (`MvPolynomial.support_rename_of_injective`, `Finsupp.sum_mapDomain_index_inj`, `Finset.coe_image`, `Set.image_image`, plus the project's `taylor_rename`); composition gives our form. The closest mathlib analogue is `weightedTotalDegree_rename_of_injective` (sup instead of inf).

### Normal-form check — `Roth.index_rename`

Equivalent formalisms:
- `index (rename f P) α r = index P (α ∘ f) (r ∘ f)` (this lemma)
- `index (rename e P) α r = index P (α ∘ e) (r ∘ e)` for an `Equiv` `e` (a special case)
- `index (rename f P) α' r' = index P α r` given `α = α' ∘ f`, `r = r' ∘ f` (an unbundled variant)

Does mathlib already have a canonical form? Yes, for the analogous quantities: `weightedTotalDegree_rename_of_injective` and `degreeOf_rename_of_injective` put `rename` on the LHS and pull the weights back via `∘ e` on the RHS.
Is our statement against a canonical form? Yes. It matches the mathlib shape exactly.
RHS convention respected? yes

### Syntactic generality — `Roth.index_rename`

Alternative restatements attempted:
- the current pull-back form
- the `Equiv` form (weaker, and covered by `e.injective` at Theta.lean:154)
- the unbundled form with equations `α = α' ∘ f` (harder to supply, and the callers use `simp`/`rw` with `Function.comp_def`)

Chosen restatement: current.
Justification: it is usable both as a `simp` lemma (Theta.lean:154) and as a `rw` lemma (Theta.lean:442), and it matches the mathlib `_rename_of_injective` conventions.

### Superfluous-argument audit — `Roth.index_rename`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]`, `[Fintype τ]` | yes | needed by `Roth.index` on each side |
| 2 | `hf` | yes | evidence (1), compiled counterexample. It is used by `support_rename_of_injective` (the use in `weight_mapDomain` is superfluous there, but not here) |
| 3 | `P`, `α`, `r` explicit | yes | the callers pass them through `rw`/`simp` unification |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not a mathlib candidate)

### Call sites — `Roth.index_rename`

Internal use count: 3 (outside the declaring file)
External-to-file callers: 1 distinct file (Roth/Theta.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:154 | `· simp [map_rename, index_rename e.injective, Function.comp_def]` |
| Roth/Theta.lean:442 | `index_rename (Option.some_injective _), index_rename hinjV]` (two uses in one `rw`) |

Inline-derivation grep:
  - (none) — no other site rewrites `support_rename_of_injective` under `index` (`grep -rn support_rename_of_injective Roth/` hits only Index.lean:216 and unrelated non-index sites).

### Composition check (Phase 6)

Can `Roth.index_rename` be derived from mathlib in ≤3 chained calls?

Attempt 1: unfold `index`, push `taylor` through `rename`, transport the support, and compare weights pointwise.
  - Mathlib decls used: `MvPolynomial.support_rename_of_injective` (Mathlib/Algebra/MvPolynomial/Rename.lean:381), `Finset.coe_image`, `Set.image_image`, `Set.image_congr`, `Finsupp.sum_mapDomain_index_inj` (Mathlib/Data/Finsupp/Basic.lean:430, additive form), plus project `MvPolynomial.taylor_rename` (Roth/Taylor.lean:164).
  - Result: succeeds. This is evidence (2), which compiles without the project's `weight_mapDomain`.
  - Notes: it is one rewrite chain plus one pointwise `simpa`. This is the same shape as mathlib's own proof of `weightedTotalDegree_rename_of_injective`.

Conclusion: COMPOSABLE (as a short rewrite chain on mathlib building blocks; it is not a single call)

## Verdict: `Roth.index_rename`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): clean.tex:620-622 and 632 state the fact and request it as a separate lemma. In the literature it is the immediate naturality of a monomial-weighted order under adjoining variables.
- Generality analysis (Phase 4): MAXIMALLY GENERAL. `hf` is necessary (compiled counterexample).
- Mathlib search (Phase 5): building blocks are `support_rename_of_injective` and `Finsupp.sum_mapDomain_index_inj`. The analogue `weightedTotalDegree_rename_of_injective` exists for sup. There is no inf/order version because mathlib has no `MvPolynomial` weighted order.
- Composition check (Phase 6): COMPOSABLE (one rewrite chain, evidence (2)).

**Rationale:**

After unfolding `Roth.index`, the proof never mentions it again. It is `support_rename_of_injective` (supports transport by `mapDomain f`) plus pointwise weight transport (`Finsupp.sum_mapDomain_index_inj`), bridged by the project's `taylor_rename`. This is exactly the proof pattern of mathlib's `MvPolynomial.weightedTotalDegree_rename_of_injective`, with `sInf` in place of `Finset.sup`. The subject `Roth.index` is a real-valued, project-specific normalisation of a weighted order at a point (its own report is BORDERLINE), so this lemma has no mathlib home as stated. If an upstream `MvPolynomial` weighted order were ever added, its renaming lemma would be a new lemma about that def, written the same way. It would not be this one.

The statement is optimal. `hf` is genuinely needed (evidence (1)). The statement follows mathlib's `_rename_of_injective` conventions (rename on the LHS, `∘ f` pull-back on the RHS) and needs no positivity of `r`.

WHY not: it is a short rewrite chain on mathlib building blocks about a project definition. It adds no mathematics that mathlib lacks.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean. It is the source's explicitly requested "invariance under variable renaming" lemma (clean.tex:632) and packages the taylor/support/weight bridging for 3 uses in Theta.lean.
Mathlib building blocks: `MvPolynomial.support_rename_of_injective` (Mathlib/Algebra/MvPolynomial/Rename.lean:381), `Finsupp.sum_mapDomain_index_inj` (Mathlib/Data/Finsupp/Basic.lean:430), `Finset.coe_image`, `Set.image_image`; project `MvPolynomial.taylor_rename` (Roth/Taylor.lean:164).
Composition sketch (≤3 lines):
```lean
  rw [index, index, taylor_rename, support_rename_of_injective hf, Finset.coe_image, Set.image_image]
  refine congrArg sInf (Set.image_congr fun d _ ↦ ?_)
  simpa [Finsupp.sum_fintype, weight] using Finsupp.sum_mapDomain_index_inj (s := d) (h := fun j n ↦ (n : ℝ) / r j) hf
```
Call sites in our project (from Phase 6.0): 3 (Roth/Theta.lean:154; Roth/Theta.lean:442 twice).
Refactor plan: do not delete. The verdict is "not for mathlib", not "inline". Inlining would put the 3-line chain above inside a `simp` at Theta.lean:154 and inside a `rw` chain at Theta.lean:442 (twice), which hurts readability and gains nothing. The only local adjustment is tied to Roth.weight_mapDomain.md: if `weight_mapDomain` drops its superfluous `hf`, line 219 becomes `exact weight_mapDomain r d`, and `index_rename` still keeps `hf` for `support_rename_of_injective`.
Next action: keep locally; do not upstream.

## Next step

Keep `Roth.index_rename` in Roth/Index.lean unchanged and do not upstream it. Its abstract content is `MvPolynomial.support_rename_of_injective` plus weight transport, mirroring mathlib's `weightedTotalDegree_rename_of_injective`. When `Roth.weight_mapDomain` drops its unused `hf`, update the call at Roth/Index.lean:219 accordingly.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_rename/hyps.lean` (imports `Roth.Index`). `lean_diagnostic_messages` reports no errors (only the style-header linter warning about a missing module docstring). The file contains:
  - (1) a counterexample showing `hf` is necessary: `f : Bool → Unit`, `P = X true - X false`, `α = 0`, `r = 1`. Then `rename f P = 0`, so the LHS is `index 0 = 0`, while the RHS is `≠ 0` by `index_eq_zero_iff` since `eval 0 P = 0`.
  - (2) the full proof composed from mathlib's `support_rename_of_injective` and `Finsupp.sum_mapDomain_index_inj` plus the project's `taylor_rename`, without `Roth.weight_mapDomain`.
- WebSearch ×3 (queries in the table).
- Local grep of `.mathlib-quality/references/clean.tex` (lines 614-640).
- Lean-Finder, Loogle, LeanSearch, and grep of `.lake/packages/mathlib/Mathlib/`, as recorded in Phase 5.
- `grep -rn index_rename Roth/`: the declaration, the docstring mention at Index.lean:39, and Theta.lean:154 and 442.
- The ChatGPT channel is n/a: the `ask_chatgpt_math` MCP is not configured in this session.
