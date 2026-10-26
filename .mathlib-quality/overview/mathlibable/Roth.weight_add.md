---
decl: Roth.weight_add
file: Roth/Box.lean
line: 85
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the analogue Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e is mathlib's generic map_add (Finsupp.weight w is an AddMonoidHom); the project form is a one-line simp unfolding used at 3 rewrite sites.
action: Keep in Roth/Box.lean while Roth.weight is an unbundled function; if Roth.weight is refactored onto Finsupp.weight (parent report), delete it and replace weight_add by map_add at Index.lean:114, Theta.lean:391, Lattice.lean:155; no mathlib PR.
---

# Roth.weight_add

## Inventory entry

### `theorem Roth.weight_add`
- **Type**: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (d e : σ →₀ ℕ) : Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e`
- **What**: The weight `∑ j, d j / r j` is additive in the multi-index.
- **How**: `simp [weight, add_div, Finset.sum_add_distrib]` (unfold, `Finsupp.coe_add`, `Nat.cast_add`, split each quotient with `add_div`, split the sum with `Finset.sum_add_distrib`).
- **Hypotheses**: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:114 (`index_sub_weight_le_index_hasseDeriv`, `simpa [weight_add, hiw]`); Roth/Theta.lean:391 (`rw [weight_add, weight_mapDomain ..., weight_single] at h1`); Roth/Lattice.lean:155 (`rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]`).
- **Visibility**: public
- **Lines**: 83–86, proof length 1 line
- **Notes**: docstring cites §4, proof of Lemma `index-of-derivative` (clean.tex l.586-587: `∑ (i_j + k_j)/r_j = ind(Δ_k P) + ∑ k_j/r_j`). Not `@[simp]`.

## Junk check (Step 8)
- Used anywhere? Yes: 3 explicit call sites in 3 files (Index, Theta, Lattice).
- Wrapper of 1–2 mathlib calls? Yes: `simp [weight, add_div, Finset.sum_add_distrib]` (and, re-aimed, `map_add`).
- Does mathlib have it? For the re-aimed `Finsupp.weight`: yes, as the generic `map_add` (simp), since `Finsupp.weight w : (σ →₀ R) →+ M`. No dedicated `Finsupp.weight_add` (none needed).
- Too specific (inline)? Inlining the `simp` unfolding at 3 rewrite sites would be worse than the named lemma while `Roth.weight` is unbundled; the lemma is the natural API.
- Well-chosen? Yes, as the additivity lemma for an unbundled function; redundant only once `Roth.weight` is bundled.
- Conclusion: `KEEP` — action: keep while `Roth.weight` is an unbundled function; when the parent `REPLACE` refactor (`Roth.weight r := Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)`) lands, delete it and use `map_add` at the 3 sites.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_add` not in mathlib (no `namespace Roth` in Mathlib; only unrelated private `MvPolynomial.weight_add_weight_pairMap` in NewtonIdentities.lean:119). Not a pure glue lemma (`simp` with two algebraic lemmas), and its parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`. Per the re-aim rule, this run is re-aimed at `Finsupp.weight`: target statement `Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight_add`:    resolved at Roth/Box.lean:85
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_add` is a theorem stating the following: for a finite index set `σ`, parameters `r ∈ ℕ^σ` and multi-indices `d, e ∈ ℕ^σ`, the weight is additive, `w_r(d + e) = w_r(d) + w_r(e)`, where `w_r(d) = ∑_j d_j / r_j`. Re-aimed: for any weight vector `w : σ → M`, the weighted degree `⟨w, ·⟩` is additive on exponent vectors, i.e. it is an additive monoid homomorphism.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (needed for `Roth.weight`).
- `r : σ → ℕ` — parameters `r_j`.
- `d e : σ →₀ ℕ` — the two multi-indices.

Hypotheses (Lean side):
- none.

Conclusion (math): `w_r(d + e) = w_r(d) + w_r(e)`.

Conclusion (Lean): `Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line additivity lemma for a linear functional.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of derivative polynomial ind(Delta_k P) >= ind P - sum k_j/r_j weight additive | partial | index = min of `∑ i_h/r_h`; additivity of the weight used implicitly in the index-of-derivative lemma | arXiv math/0307203, 1305.0926, 1806.10737, Evertse Luminy notes; never stated as a separate lemma |
| 2 | WebSearch (general form) | weighted degree of product of monomials is sum of weighted degrees additive multi-index | yes | weighted degree is an additive monoid hom on exponents, so degree of a product of monomials is the sum | mathlib WeightedHomogeneous docs mirrors, Magma docs |
| 3 | WebSearch (named-after / aliases) | grading of polynomial ring by weight vector degree map monoid homomorphism exponents Z^n linear functional | yes | grading induced by a group/monoid hom from exponents to `G`, `x_i ↦ w_i` | arXiv 0901.3263, 2202.05742, 2607.20210 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `k_j/r_j`, `i_j+k_j` | yes | l.586-587: `ind(P) ≤ ∑_j (i_j + k_j)/r_j = ind(Δ_k P) + ∑_j k_j/r_j` | the exact use of additivity in the paper |
| 6 | nLab | graded ring / grading | partial | degree map of a grading is a monoid hom | no lemma-level content |
| 7 | nCatLab | — | n/a | — | not a categorical concept (additivity of a linear map) |
| 8 | Stacks Project | graded rings (weighted polynomial rings) | partial | `deg(x^a x^b) = deg x^a + deg x^b` built into the grading | nothing beyond the definition |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | immediate fact; no discussion |
| 10 | recent arXiv (last 5 years) | (results of #3: arXiv 2202.05742, 2607.20210) | yes | matrix-weighted degree `W·α`, linear in `α` | same fact, used implicitly |

### Literature summary (Phase 3)

Concept identified as: additivity of the weighted degree (a linear functional on exponent vectors).
Sources agree on the standard form: yes (immediate from linearity; never a named result).
Most general standard form: the weighted degree `d ↦ ∑ d_i • w_i` is an additive monoid hom `(σ →₀ R) →+ M`; additivity is `map_add`.
Generality dimensions where the literature varies:
  - weight values / codomain: integers, rationals `1/r_j`, reals, vectors (matrix weights) — all covered by any `Module R M`.
  - finiteness of `σ`: not needed.
Disagreement with the literature: none.

### Generality analysis — `Roth.weight_add`

Literature-standard form (from Phase 3): `Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e` for any `w : σ → M`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector | `1/r j`, `r : σ → ℕ` | any `w : σ → M` | yes | realised by `map_add` (evidence (1), compiles) |
| 2 | codomain `ℝ` | ℝ | any `AddCommMonoid M` with `Module R M` | yes | evidence (1) |
| 3 | `[Fintype σ]` | required | not needed | yes for the re-aimed form; no for the project form | `Roth.weight` needs it to typecheck; evidence (5) |
| 4 | exponents `ℕ` | ℕ | any semiring `R` | yes | evidence (1) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is already in mathlib (`map_add` for the bundled `Finsupp.weight`), false-positive class 4, routed to NO-mathlib-has-it.
Number of weakening opportunities found: 4 (rows 1–4), all verified in the evidence file.
Proposed restatement: none to add; `map_add (Finsupp.weight w)`.
Cost of restatement: CHEAP (nothing to write).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | yes | bundle `Roth.weight r` as an `AddMonoidHom` (parent refactor); then this lemma is `map_add` | `map_add` / `map_sum` / `map_nsmul` for free |
| 4 | bundled substructure? | yes | same as #3 | as #3 |
| 5 | field-specific to semiring? | yes | any codomain module | covered by `Finsupp.weight` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary weight vector `w : σ → M` | as #3 |
| 8 | concrete-via-abstract? | no | proof is a one-step `simp`; nothing beyond the re-aimed form | — |
| 9 | false-generalisation guard | no false generalisation | re-aimed form specialises back to the project lemma (evidence (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `map_add (Finsupp.weight w)` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: the `AddMonoidHom` API (`map_add`, `map_sum`, `map_nsmul`).
  - Real mathematical improvement: additivity is the defining property of the bundled hom, not a separate fact.

### Proof strategy — `Roth.weight_add`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after bundling `Roth.weight`, `map_add` | CHEAP (part of the parent refactor) |
| 5 | missing mathlib helpers | no | `map_add` exists | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the current unbundled def; `simp [weight, add_div, Finset.sum_add_distrib]` is the natural proof). After the parent refactor the lemma is redundant with `map_add`.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_add`

[A] Lean-Finder       "weighted degree of d + e equals weighted degree of d plus weighted degree of e"   hits: `MvPolynomial.IsWeightedHomogeneous.add`, `.mul`, `weightedTotalDegree`, `weightedTotalDegree'`, `IsWeightedHomogeneous`; no dedicated lemma (the fact is `map_add`)
[B] Loogle            `Finsupp.weight _ (_ + _)`   no hits (generic `map_add` is not indexed under that pattern)
[C] LeanSearch        "Finsupp.weight of a sum of multi-indices is the sum of weights"   hits: `Finsupp.weight_apply`, `Finsupp.degree_eq_weight_one`, `Finsupp.weight_single`, `MvPolynomial.IsWeightedHomogeneous.sum`
[D] Grep mathlib src  `weight_add`, `map_add` in Mathlib/Data/Finsupp/Weight.lean and WeightedHomogeneous.lean   no `Finsupp.weight_add` (only private `MvPolynomial.weight_add_weight_pairMap`, unrelated); `Finsupp.weight` defined with `map_add'` at Weight.lean:219; WeightedHomogeneous.lean:185 uses `map_add` for exactly this fact
[E] Name pattern      `map_add`, `Finsupp.weight` (used in compiled evidence)   hits

Searched for both the user's form (`weight r (d + e) = weight r d + weight r e`) and the re-aimed form (`Finsupp.weight w (d + e) = ...`).

Concluded: found in mathlib as `map_add` (applied to the `AddMonoidHom` `Finsupp.weight w`); more general form (we are a specialisation via the parent bridge).

### Normal-form check — `Roth.weight_add`

Equivalent formalisms: `weight r (d + e) = weight r d + weight r e`; `Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e`; `∑ j, ((d j + e j : ℕ) : ℝ) / r j = ∑ j, (d j : ℝ) / r j + ∑ j, (e j : ℝ) / r j`.
Does mathlib already have a canonical form for this idea? yes: `map_add` for bundled homs.
Is our statement stated against the canonical form? It is the `f (a + b) = f a + f b` shape, stated against the project def; fine locally.
RHS convention respected? yes (split form on RHS, as `map_add`).

### Syntactic generality — `Roth.weight_add`

Alternative restatements attempted:
- `map_add (Finsupp.weight w)` (compiles; evidence (1))
- `@[simp]` tagging (would let the `simpa` at Index.lean:114 drop the explicit argument; not needed at the `rw` sites)
Chosen restatement: as stated.
Justification: used as a left-to-right rewrite at all 3 sites; explicit `r d e` is harmless.

### Superfluous-argument audit — `Roth.weight_add`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed for `Roth.weight` to typecheck |
| 2 | `r` | yes | — |
| 3 | `d`, `e` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_add`

Internal use count: 3 (outside Roth/Box.lean)
External-to-file callers: 3 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:114 | `exact sub_le_iff_le_add.2 (by simpa [weight_add, hiw] using index_le_weight (r := r) hi.2)` |
| Roth/Theta.lean:391 | `rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1` |
| Roth/Lattice.lean:155 | `rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]` |

Inline-derivation grep:
  - (none) — no re-derivation of additivity of `Roth.weight` elsewhere in Roth/.
  - Mathlib's own analogue is inlined as `map_add` at Mathlib/RingTheory/MvPolynomial/WeightedHomogeneous.lean:185.

### Composition check (Phase 6)

Can `Roth.weight_add` be derived from mathlib in ≤3 chained calls?

Attempt 1 (re-aimed form): `map_add (Finsupp.weight w) d e`
  - Mathlib decls used: `map_add`, `Finsupp.weight`
  - Result: succeeds (evidence (1), (2), (5))

Attempt 2 (project form): via the parent bridge `Roth.weight r f = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) f` then `map_add`; or the current `simp [Roth.weight, add_div, Finset.sum_add_distrib]`
  - Result: succeeds (evidence (3), (4))

Conclusion: COMPOSABLE (re-aimed form is literally an existing mathlib lemma; routed to NO-mathlib-has-it)

## Verdict: `Roth.weight_add`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): additivity of the weighted degree is immediate from linearity; used implicitly in the paper (clean.tex l.586-587), never a named result.
- Generality analysis (Phase 4): STRICTLY NARROWER, general form already in mathlib (class 4).
- Mathlib search (Phase 5): found in mathlib as `map_add` for the `AddMonoidHom` `Finsupp.weight w`.
- Composition check (Phase 6): COMPOSABLE (one call).

**Rationale:**

Re-aimed at `Finsupp.weight` (the parent `Roth.weight` equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`), the statement `Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e` is mathlib's generic `map_add`, because `Finsupp.weight w : (σ →₀ R) →+ M` is bundled (its `map_add'` field is at Mathlib/Data/Finsupp/Weight.lean:219). The project lemma exists only because `Roth.weight` is an unbundled function.

WHY not: mathlib has the general fact as `map_add`. Belongs-elsewhere check: keep it project-local in Roth/Box.lean as the additivity lemma of the unbundled `Roth.weight`; it becomes deletable once the parent refactor bundles `Roth.weight`.

Existing mathlib decl:        `map_add` (applied to `Finsupp.weight w`)
Located at:                   `Mathlib/Algebra/Group/Hom/Defs.lean` (`map_add`, `AddHomClass`); `Finsupp.weight` at `Mathlib/Data/Finsupp/Weight.lean:82`
Our form follows in ≤1 line:
```lean
example (w : σ → M) (d e : σ →₀ R) :
    Finsupp.weight w (d + e) = Finsupp.weight w d + Finsupp.weight w e := map_add _ d e
-- project form via the parent bridge h : ∀ f, Roth.weight r f = Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹) f:
example (r : σ → ℕ) (d e : σ →₀ ℕ) : Roth.weight r (d + e) = Roth.weight r d + Roth.weight r e := by
  rw [h, h, h, map_add]
```
Call sites in our project (from Phase 6.0):  3
Refactor plan: while `Roth.weight` stays unbundled, keep the lemma. If the parent refactor (`Roth.weight r : (σ →₀ ℕ) →+ ℝ := Finsupp.weight fun j ↦ ((r j : ℝ))⁻¹`) is carried out, delete `Roth.weight_add` and replace `weight_add` by `map_add` at Roth/Index.lean:114 (inside `simpa [...]`; `map_add` is simp, so it can simply be dropped from the list), Roth/Theta.lean:391 and Roth/Lattice.lean:155 (in the `rw` lists). Alternatively keep `weight_add` as a one-line alias `map_add _ d e` to leave the 3 sites untouched.
Next action: no mathlib PR; delete only as part of the parent `Roth.weight` refactor.

---

## Next step

No mathlib action. Keep as the additivity lemma for the unbundled `Roth.weight`; remove it when `Roth.weight` is redefined via `Finsupp.weight` (then `map_add` covers it at Index.lean:114, Theta.lean:391, Lattice.lean:155).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_add/weight_add_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics): (1) `Finsupp.weight w (d + e) = ...` by `map_add` for general `R`, `M`; (2) the same by `simp`; (3) project lemma via the parent bridge + `map_add`; (4) current proof `simp [Roth.weight, add_div, Finset.sum_add_distrib]`; (5) the re-aimed form without `[Fintype σ]`.
- Loogle `Finsupp.weight _ (_ + _)` (no hits); LeanSearch and Lean-Finder queries as in the search-status block.
- Mathlib greps: `weight_add` over Mathlib (only private `MvPolynomial.weight_add_weight_pairMap`); `map_add` in Mathlib/Data/Finsupp/Weight.lean (:219) and WeightedHomogeneous.lean (:185).
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.586-587).
- Project grep `grep -rn weight_add Roth/` (3 call sites + declaration).
