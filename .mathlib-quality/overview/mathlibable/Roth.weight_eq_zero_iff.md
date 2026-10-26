---
decl: Roth.weight_eq_zero_iff
file: Roth/Box.lean
line: 91
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Re-aimed at Finsupp.weight, mathlib's Finsupp.weight_eq_zero_iff_eq_zero needs CanonicallyOrderedAdd M (excludes ℝ), while the form with strictly positive weights in any ordered additive monoid is missing, strictly generalises it (verified), and is a short proof, not a 1-3 call composition.
action: Upstream Finsupp.weight_eq_zero_iff_of_pos (hw : ∀ i, 0 < w i) to Mathlib/Data/Finsupp/Weight.lean next to weight_eq_zero_iff_eq_zero (deriving the canonical one from it); keep Roth.weight_eq_zero_iff for its single call site Index.lean:102, reproved through it if Roth.weight is refactored onto Finsupp.weight.
---

# Roth.weight_eq_zero_iff

## Inventory entry

### `theorem Roth.weight_eq_zero_iff`
- **Type**: `{σ : Type*} [Fintype σ] {r : σ → ℕ} (hr : ∀ j, 0 < r j) {d : σ →₀ ℕ} : Roth.weight r d = 0 ↔ d = 0`
- **What**: For strictly positive parameters `r`, the weight `∑ j, d j / r j` of a multi-index vanishes exactly when the multi-index is zero.
- **How**: One `simp` call unfolding `weight` and using `Finset.sum_eq_zero_iff_of_nonneg` (each summand is nonnegative by `div_nonneg`), `(hr _).ne'` to cancel the division, and `Finsupp.ext_iff`.
- **Hypotheses**: `hr : ∀ j, 0 < r j` (essential: with `r j = 0`, `d j / 0 = 0` and any `d` supported at `j` has weight 0; evidence (5)); section variable `[Fintype σ]`.
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:102 (`index_eq_zero_iff`: `rw [h, weight_eq_zero_iff hr] at hdw`); mentioned in the Roth/Box.lean:31 module docstring.
- **Visibility**: public
- **Lines**: 88–93, proof length 1 line
- **Notes**: Source docstring cites clean.tex §4 l.565–566 ("Since each `r_j>0`, such a weight is zero exactly when every `i_j=0`").

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Index.lean:102).
- Wrapper of 1–2 mathlib calls? Effectively one `simp` call with 5 lemmas (a "trivial simp composition").
- Does mathlib have it? Not for `Roth.weight`. For the re-aimed `Finsupp.weight`, mathlib has `Finsupp.weight_eq_zero_iff_eq_zero` and `MvPolynomial.weightedDegree_eq_zero_iff`, but both require `[CanonicallyOrderedAdd M]`, so they do not apply to real weights `(r j)⁻¹`.
- Too specific (inline)? One call site; inlining the `simp` at Index.lean:102 is possible but the named iff reads better in the `rw ... at hdw` and mirrors the paper's sentence.
- Well-chosen? Yes; standard `_eq_zero_iff` API companion of `weight`.
- Conclusion: `KEEP` — action: keep in Roth/Box.lean; if `Roth.weight` is redefined via `Finsupp.weight`, reprove it from the upstreamed `Finsupp.weight_eq_zero_iff_of_pos`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_eq_zero_iff` not in mathlib (no `namespace Roth` there). Not a glue lemma (a `simp` proof, not rfl/unfolding). Parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`, so per the re-aim rule the run is re-aimed at `Finsupp.weight`. Mathlib does have an analogue (`Finsupp.weight_eq_zero_iff_eq_zero`), but only for canonically ordered codomains; it does not cover `ℝ`, so the re-aim is not a hit and a full run follows with target `Finsupp.weight w f = 0 ↔ f = 0` for `∀ i, 0 < w i` in an ordered additive monoid.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight_eq_zero_iff`: resolved at Roth/Box.lean:91
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_eq_zero_iff` is a theorem stating the following: let `σ` be finite and `r ∈ ℕ^σ` with every `r_j > 0`. For a multi-index `d ∈ ℕ^σ`, the weight `∑_j d_j / r_j` is zero if and only if `d = 0`. Re-aimed: for a weight vector `w : σ → M` in an ordered additive commutative monoid with all `w_i > 0`, the weighted degree `∑_i d_i w_i` of `d ∈ ℕ^(σ)` vanishes iff `d = 0`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (needed by `Roth.weight`).
- `r : σ → ℕ` — parameters.
- `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- `hr : ∀ j, 0 < r j` — positivity of the parameters; makes every weight `1/r_j` strictly positive.

Conclusion (math): the weight is zero exactly for the zero multi-index.

Conclusion (Lean): `Roth.weight r d = 0 ↔ d = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an elementary positivity iff about a bookkeeping def; not a structure or main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index zero iff polynomial does not vanish weight sum i_j/r_j positive r_j | partial | index = min of `∑ i_h/r_h` over nonvanishing derivatives; index 0 iff `P(α) ≠ 0` follows since only `I = 0` has weight 0 | arXiv math/0307203, arXiv 1305.0926, Evertse notes (math.leidenuniv.nl/~evertsejh/95-product.pdf); never stated as a separate lemma |
| 2 | WebSearch (general form) | weighted degree zero only for constant monomial positive weights grading degree zero part | yes | with positive weights only the constant monomial has weighted degree 0; fails for zero/negative weights | arXiv 1301.5612, arXiv 2202.05742 (matrix weights: no nontrivial monomial of degree 0 iff finitely many monomials per degree), Magma docs, mathlib WeightedHomogeneous docs |
| 3 | WebSearch (named-after / aliases) | "positively graded" polynomial ring weights degree zero component is the base field | partial | "positively graded" / "connected graded" (`A_0 = K`) | arXiv 2406.09593, arXiv 1510.04381, GSU commutative algebra lecture 20; the degree-zero-monomial fact is folklore |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `r_j>0` | yes | l.565–566: "Since each `r_j>0`, such a weight is zero exactly when every `i_j=0`" | project paper §4, proof of the `index = 0 ↔ P(α) ≠ 0` lemma; one-sentence remark |
| 6 | nLab | graded ring / connected graded algebra | partial | connected ℕ-graded algebra: positive-degree generators, degree-0 part the ground ring | a structural analogue, no lemma-level content |
| 7 | nCatLab | — | n/a | — | not a categorical concept (elementary inequality about finite sums) |
| 8 | Stacks Project | graded rings, weighted polynomial rings | partial | ℕ-gradings with positive weights; degree-0 part is the coefficient ring | consistent with #2, nothing to cite beyond it |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | immediate fact; no discussion found |
| 10 | recent arXiv (last 5 years) | (results of #2, #3: arXiv 2202.05742, 2406.09593, 2607.18948) | partial | positive (matrix) weights, pointed/connected gradings | uses the fact implicitly or as the defining condition |

### Literature summary (Phase 3)

Concept identified as: the weighted degree `⟨w, d⟩ = ∑ w_i d_i` of an exponent vector is zero only for `d = 0` when every weight is positive (equivalently: a positive weighting makes the grading connected / the monoid of exponents pointed).
Sources agree on the standard form: yes; always stated for positive weights, often as a one-line remark.
Most general standard form: for `w : σ → M` in an ordered additive monoid with every `w_i > 0`, `∑ d_i w_i = 0 ⇔ d = 0` (the converse direction is trivial); in the canonically ordered case, `w_i ≠ 0` suffices.
Generality dimensions where the literature varies:
  - weight values: positive integers (gradings), reals `1/r_j` (Roth), elements of an ordered monoid/group, matrix weights; the most general here is an ordered additive monoid with positive weights.
  - finiteness of `σ`: not needed.
  - the positivity hypothesis: necessary (zero or negative weights give nonzero `d` of degree 0; arXiv 2202.05742 makes this point).
Disagreement with the literature: none; the project form is the special weight vector `(1/r_j)`.

### Generality analysis — `Roth.weight_eq_zero_iff`

Literature-standard form (from Phase 3): `Finsupp.weight w f = 0 ↔ f = 0` for `∀ i, 0 < w i`, `[IsOrderedAddMonoid M]`, no finiteness.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector | `1/r j`, `r : σ → ℕ` | any `w` with `0 < w i` | yes | realised by evidence `finsupp_weight_eq_zero_iff_of_pos` (compiles) |
| 2 | codomain `ℝ` | ℝ | any ordered additive comm. monoid (non-canonical allowed) | yes | same evidence; needs only `IsOrderedAddMonoid` |
| 3 | `[Fintype σ]` | required | not needed | yes for the re-aimed form; no for the project form | `Roth.weight` itself requires it |
| 4 | `hr : ∀ j, 0 < r j` | positivity | positivity | no | necessary; counterexample `r = 0`, `d = single () 1` (evidence (5)) |
| 5 | `d : σ →₀ ℕ` | ℕ exponents | ℕ exponents | no | case of interest; matches mathlib's `weight_eq_zero_iff_eq_zero` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (rows 1–3), verified for the re-aimed `Finsupp.weight` statement in the evidence file (no diagnostics).
Proposed restatement:

```lean
theorem Finsupp.weight_eq_zero_iff_of_pos {σ M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {w : σ → M} (hw : ∀ i, 0 < w i) {f : σ →₀ ℕ} :
    weight w f = 0 ↔ f = 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ h ▸ map_zero _⟩
  by_contra hf
  obtain ⟨s, hs⟩ := Finsupp.ne_iff.1 hf
  exact (hw s).not_ge (h ▸ le_weight_of_ne_zero (fun i ↦ (hw i).le) hs)
```

It strictly generalises mathlib's `Finsupp.weight_eq_zero_iff_eq_zero` (which then becomes the one-liner `weight_eq_zero_iff_of_pos fun s ↦ pos_iff_ne_zero.2 (NonTorsionWeight.ne_zero ℕ w s)`, evidence (2)), and specialises back to the project lemma (evidence (3)).

Cost of restatement: CHEAP — verified 4-line proof.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | positivity of individual weights is data, not a class (mathlib's `NonTorsionWeight` class is the canonical-order analogue) |
| 2 | sequences to filters? | no | — | finite sums, no limits |
| 3 | construction vs universal property? | no | — | an iff, not a construction |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | ordered additive monoid codomain | covers `ℝ`, `ℚ`, `ℤ`-valued weights excluded by `CanonicallyOrderedAdd` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `ℝ`, `1/r j` to arbitrary positive `w : σ → M` | as #5 |
| 8 | concrete-via-abstract? | no | the proof uses only termwise nonnegativity and positivity; after the re-aim nothing concrete remains | — |
| 9 | false-generalisation guard | no false generalisation | the general form specialises back to the project lemma and to mathlib's canonical lemma (evidence (2), (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.weight_eq_zero_iff_of_pos` as in Phase 4b.
  - Cost: CHEAP
  - Mathlib downstream this enables: `weight_eq_zero_iff_eq_zero` and `MvPolynomial.weightedDegree_eq_zero_iff` (WeightedHomogeneous.lean:599) become corollaries; weighted-homogeneous results stated with positive real/rational/integer weights gain the degree-zero characterisation.
  - Real mathematical improvement: removes the canonical-order restriction, the only obstacle to using mathlib's lemma for real weights such as `1/r_j`.

### Proof strategy — `Roth.weight_eq_zero_iff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `Finsupp.weight_eq_zero_iff_of_pos` (the proposed lemma) | CHEAP (file follow-up PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(The single `simp` with `Finset.sum_eq_zero_iff_of_nonneg` is the natural proof for the `Fintype`/`ℝ` form. After a `Roth.weight` → `Finsupp.weight` refactor it would become one application of the proposed mathlib lemma.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_eq_zero_iff`

[A] Lean-Finder       "Finsupp.weight w f = 0 ↔ f = 0 for strictly positive weights in an ordered additive monoid"   hits: `Finsupp.weight_eq_zero_iff_eq_zero`, `MvPolynomial.weightedDegree_eq_zero_iff` (both `[CanonicallyOrderedAdd M]`), `NonTorsionWeight.ne_zero`, `nonTorsionWeight_of`, `le_weight_of_ne_zero`
[B] Loogle            `Finsupp.weight _ _ = 0`   2 hits: `Finsupp.weight_eq_zero_iff_eq_zero`, `MvPolynomial.weightedDegree_eq_zero_iff` — both canonical-order only
[C] LeanSearch        "weight of finsupp with positive weights is zero iff finsupp is zero"   same two plus `Finsupp.le_weight_of_ne_zero'`, `Finsupp.coe_eq_zero`, `Finsupp.support_eq_empty`
[D] Grep mathlib src  `weight_pos`, `weight_eq_zero_iff`, `weight_ne_zero` over Mathlib/   only `Finsupp.weight_eq_zero_iff_eq_zero` (Data/Finsupp/Weight.lean:173), `MvPolynomial.weightedDegree_eq_zero_iff` (RingTheory/MvPolynomial/WeightedHomogeneous.lean:599) and the unrelated `Quiver.Path.weight_pos`
[E] Name pattern      `Finsupp.weight_eq_zero_iff_of_pos`, `Finsupp.weight_pos`   absent

Searched for both the user's form (`∑ d j / r j = 0 ↔ d = 0`) and the re-aimed form (`Finsupp.weight w f = 0 ↔ f = 0` with positive weights).

Concluded: found a partial match (`Finsupp.weight_eq_zero_iff_eq_zero`); covers only canonically ordered codomains, not `ℝ`.

### Normal-form check — `Roth.weight_eq_zero_iff`

Equivalent formalisms: `weight r d = 0 ↔ d = 0`; `0 < weight r d ↔ d ≠ 0`; `weight r d = 0 ↔ ∀ j, d j = 0` (mathlib's `weightedDegree_eq_zero_iff` shape).
Does mathlib already have a canonical form for this idea? yes: `Finsupp.weight_eq_zero_iff_eq_zero` uses `weight w f = 0 ↔ f = 0`.
Is our statement stated against the canonical form? yes, same shape (`_ = 0 ↔ _ = 0`), with the canonical `f = 0` on the RHS.
RHS convention respected? yes

### Syntactic generality — `Roth.weight_eq_zero_iff`

Alternative restatements attempted:
- `0 < weight r d ↔ d ≠ 0` (less convenient for the `rw ... at hdw` at Index.lean:102)
- explicit `r`, `d` (call site passes only `hr`; implicit is easier)
- re-aimed `Finsupp.weight` form (compiles; evidence)
Chosen restatement: as stated (implicit `r`, `d`, explicit `hr`).
Justification: the only caller rewrites with `weight_eq_zero_iff hr`; `r` is inferred from `hr`.

### Superfluous-argument audit — `Roth.weight_eq_zero_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed for `Roth.weight` to typecheck |
| 2 | `hr : ∀ j, 0 < r j` | yes | necessary; counterexample without it (evidence (5)) |
| 3 | `r`, `d` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally); the mathlib contribution is the re-aimed `Finsupp.weight` form.

### Call sites — `Roth.weight_eq_zero_iff`

Internal use count: 1 (outside Roth/Box.lean)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:102 | `rw [h, weight_eq_zero_iff hr] at hdw` (in `index_eq_zero_iff`) |

Inline-derivation grep:
  - (none) — `grep -rn sum_eq_zero_iff_of_nonneg Roth/` finds only the lemma's own proof (Box.lean:93).

### Composition check (Phase 6)

Can `Roth.weight_eq_zero_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1 (project form): `simp [weight, Finset.sum_eq_zero_iff_of_nonneg, div_nonneg, (hr _).ne', Finsupp.ext_iff]`
  - Mathlib decls used: `Finset.sum_eq_zero_iff_of_nonneg`, `div_nonneg`, `Finsupp.ext_iff`
  - Result: succeeds (current proof; evidence (4)), but it is a 5-lemma `simp` composition ("trivial simp composition; user decides").

Attempt 2 (via mathlib's `Finsupp.weight_eq_zero_iff_eq_zero`):
  - Result: fails; `ℝ` is not `CanonicallyOrderedAdd`. Routing through `ℝ≥0` (cast weights to `NNReal`, `nonTorsionWeight_of`, push the cast through `Finsupp.weight`) needs more than 3 calls plus a cast lemma for `weight`.

Attempt 3 (re-aimed general form): needs `by_contra`, `Finsupp.ne_iff`, `le_weight_of_ne_zero`, `lt_irrefl`-style closing (evidence (1)): a short proof, not a call chain.

Conclusion: NOT-COMPOSABLE for the re-aimed `Finsupp.weight` form (the mathlib-level statement); the project's `Fintype`/`ℝ` form is a single `simp` composition.

## Verdict: `Roth.weight_eq_zero_iff`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): with positive weights only the zero exponent has weighted degree 0 (arXiv 2202.05742, 1301.5612; clean.tex l.565–566); positivity is necessary.
- Generality analysis (Phase 4): STRICTLY NARROWER; the general form for positive weights in any ordered additive monoid compiles (evidence (1)).
- Mathlib search (Phase 5): partial match `Finsupp.weight_eq_zero_iff_eq_zero` restricted to `[CanonicallyOrderedAdd M]`; no positive-weight version.
- Composition check (Phase 6): NOT-COMPOSABLE for the general form.

**Rationale:**

Per the re-aim rule, the parent `Roth.weight` is `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`, so the question is whether mathlib has `weight_eq_zero_iff` for `Finsupp.weight`. It does, but only as `Finsupp.weight_eq_zero_iff_eq_zero` (Mathlib/Data/Finsupp/Weight.lean:173), and its sibling `MvPolynomial.weightedDegree_eq_zero_iff` (WeightedHomogeneous.lean:599), both requiring `[CanonicallyOrderedAdd M]` and `NonTorsionWeight ℕ w`. That excludes real, rational and integer weights, which is exactly the Roth use. The literature-standard hypothesis is "all weights positive", and under it the iff holds in any ordered additive monoid with a 4-line proof from the existing `Finsupp.le_weight_of_ne_zero`. This is a real gap rather than a redundancy, and the general lemma implies mathlib's canonical-order one in one line (evidence (2)). So the right home for the content is a generalisation inside mathlib, not the project's `Fintype`/`ℝ` form.

The contribution is small, so it fits a one-lemma PR to `Mathlib/Data/Finsupp/Weight.lean` (optionally with `weight_eq_zero_iff_eq_zero` reproved from it), or a ride-along with a `Finsupp.weight_nonneg` companion (see the Roth.weight_nonneg report). The project lemma itself stays local with its one call site.

Reason for the generalisation: LITERATURE-WEAKENING (positive weights in an ordered monoid, rather than the canonical-order hypothesis of mathlib's version or the special real weights `1/r_j`) and MODERN-IDIOM (stated against `Finsupp.weight`).
Proposed restatement:
```lean
theorem Finsupp.weight_eq_zero_iff_of_pos {σ M : Type*} [AddCommMonoid M] [PartialOrder M]
    [IsOrderedAddMonoid M] {w : σ → M} (hw : ∀ i, 0 < w i) {f : σ →₀ ℕ} :
    weight w f = 0 ↔ f = 0 := by
  refine ⟨fun h ↦ ?_, fun h ↦ h ▸ map_zero _⟩
  by_contra hf
  obtain ⟨s, hs⟩ := Finsupp.ne_iff.1 hf
  exact (hw s).not_ge (h ▸ le_weight_of_ne_zero (fun i ↦ (hw i).le) hs)
```
Estimated cost of regeneralisation: CHEAP (already compiles in the evidence file).
Mathlib downstream this enables:
  - `Finsupp.weight_eq_zero_iff_eq_zero` becomes `weight_eq_zero_iff_of_pos fun s ↦ pos_iff_ne_zero.2 (NonTorsionWeight.ne_zero ℕ w s)`.
  - Weighted-degree zero characterisation for `ℝ`/`ℚ`/`ℤ`-valued positive weights (blocked today by `CanonicallyOrderedAdd`), e.g. `MvPolynomial.weightedDegree_eq_zero_iff` for such weights.
Project side: keep `Roth.weight_eq_zero_iff` for Index.lean:102. If the parent refactor (`Roth.weight := Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`) lands, reprove it as `weight_eq_zero_iff_of_pos fun j ↦ by have := hr j; positivity` (evidence (3)); the call site is unchanged.
Next action: run `/generalise Roth.weight_eq_zero_iff` with target `Finsupp.weight_eq_zero_iff_of_pos`, then open a small PR to Mathlib/Data/Finsupp/Weight.lean placing it in the `OrderedAddCommMonoid` section next to `le_weight_of_ne_zero`.

---

## Next step

Upstream `Finsupp.weight_eq_zero_iff_of_pos` (positive weights, ordered additive monoid) to Mathlib/Data/Finsupp/Weight.lean, deriving `weight_eq_zero_iff_eq_zero` from it; keep the project lemma locally for Index.lean:102.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_eq_zero_iff/weight_eq_zero_iff_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics, after one long-line fix): (1) `finsupp_weight_eq_zero_iff_of_pos`, the general form via `Finsupp.ne_iff` + `Finsupp.le_weight_of_ne_zero`; (2) mathlib's canonical-order `weight_eq_zero_iff_eq_zero` recovered from (1); (3) the project lemma recovered from (1) through the parent bridge; (4) the current one-`simp` proof; (5) the counterexample showing `hr` is necessary (`r = 0`, `d = single () 1`).
- Loogle `Finsupp.weight _ _ = 0` (2 hits, both canonical-order); LeanSearch and Lean-Finder queries as in the search-status block.
- Mathlib greps: `weight_pos`, `weight_eq_zero_iff`, `weight_ne_zero`.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.565–566.
- Project greps: `weight_eq_zero_iff` and `sum_eq_zero_iff_of_nonneg` over Roth/ for the call-sites table.
