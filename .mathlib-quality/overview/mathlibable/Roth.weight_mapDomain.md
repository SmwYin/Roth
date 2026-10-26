---
decl: Roth.weight_mapDomain
file: Roth/Box.lean
line: 127
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the statement Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d is exactly mathlib's Finsupp.linearCombination_mapDomain, which needs no injectivity; the project's hf hypothesis is superfluous (verified in evidence).
action: Keep in Roth/Box.lean as the project-local API name but drop the superfluous hypothesis hf (proof via Finsupp.sum_mapDomain_index, evidence (4)) and update the 3 callers Index.lean:219, Theta.lean:391, Lattice.lean:155; no mathlib PR.
---

# Roth.weight_mapDomain

## Inventory entry

### `theorem Roth.weight_mapDomain`
- **Type**: `{σ : Type*} [Fintype σ] {τ : Type*} [Fintype τ] {f : σ → τ} (hf : Function.Injective f) (r : τ → ℕ) (d : σ →₀ ℕ) : Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d`
- **What**: Pushing a multi-index forward along an injective change of variables `f : σ → τ` and evaluating the weight with parameters `r` equals evaluating the weight of the original multi-index with the pulled-back parameters `r ∘ f`.
- **How**: `simpa [Finsupp.sum_fintype, weight]` applied to `Finsupp.sum_mapDomain_index_inj` with `h := fun j n ↦ (n : ℝ) / r j` (rewrites both `univ` sums as `Finsupp.sum` and transports along the injective `mapDomain`).
- **Hypotheses**: `hf : Function.Injective f` (superfluous, see below); section variable `[Fintype σ]`, plus `[Fintype τ]` (both needed for `Roth.weight` to typecheck).
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:219 (`exact weight_mapDomain hf r d`, inside `index_rename`); Roth/Theta.lean:391 (`rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1`); Roth/Lattice.lean:155 (`rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]`). Also named in the Box.lean module docstring (line 33).
- **Visibility**: public
- **Lines**: 123–130, proof length 2 lines
- **Notes**: docstring cites §4, Lemma 4-2. The injectivity hypothesis is not needed: the weight is additive, so it commutes with `mapDomain` for any `f` (evidence (3), (4), (6)).

## Junk check (Step 8)
- Used anywhere? Yes: 3 call sites in 3 files (Index, Theta, Lattice).
- Wrapper of 1–2 mathlib calls? Yes: one `simpa` around `Finsupp.sum_mapDomain_index_inj`; re-aimed, it is literally `Finsupp.linearCombination_mapDomain`.
- Does mathlib have it? For the re-aimed `Finsupp.weight`: yes, `Finsupp.linearCombination_mapDomain` (Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158), since `Finsupp.weight w` is by definition `(linearCombination R w).toAddMonoidHom`. Mathlib also has the polynomial-level consequence `MvPolynomial.weightedTotalDegree_rename_of_injective` (Mathlib/RingTheory/MvPolynomial/Homogeneous.lean:78).
- Too specific (inline)? No, while `Roth.weight` is unbundled; it is consumed inside `rw` chains at 2 sites.
- Well-chosen? Mostly, but it carries a superfluous hypothesis `hf`.
- Conclusion: `KEEP` — action: keep the name, drop `hf` (proof of evidence (4)), and drop the now-unneeded injectivity arguments at Index.lean:219, Theta.lean:391, Lattice.lean:155.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_mapDomain` not in mathlib (no `namespace Roth` in Mathlib, and no `weight_mapDomain` of any namespace). Not a pure glue lemma (a `simpa` with a mathlib lemma). Parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`; per the re-aim rule this run is re-aimed at `Finsupp.weight`: target `Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` compiles with `lake env lean` with no output)
- decl `Roth.weight_mapDomain`: resolved at Roth/Box.lean:127
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_mapDomain` is a theorem stating the following: let `f : σ → τ` be an injective map between finite variable sets, `r ∈ ℕ^τ` parameters and `d ∈ ℕ^(σ)` a multi-index. Let `f_* d ∈ ℕ^(τ)` be the pushed-forward multi-index, `(f_* d)_t = ∑_{f(s) = t} d_s`. Then `w_r(f_* d) = w_{r∘f}(d)`, i.e. `∑_t (f_* d)_t / r_t = ∑_s d_s / r_{f(s)}`. Re-aimed: for any weight vector `w : τ → M`, the weighted degree satisfies `⟨w, f_* d⟩ = ⟨f^* w, d⟩` — pushforward on exponents is adjoint to pullback on weights. This holds for every `f`, injective or not.

Variables / typeclasses involved (Lean side):
- `σ τ : Type*`, `[Fintype σ] [Fintype τ]` — finite variable sets (needed for `Roth.weight`).
- `f : σ → τ` — change of variables.
- `r : τ → ℕ` — parameters on the target.
- `d : σ →₀ ℕ` — the multi-index.

Hypotheses (Lean side):
- `hf : Function.Injective f` — used by the proof (via `sum_mapDomain_index_inj`) but not needed for the conclusion.

Conclusion (math): `w_r(f_* d) = w_{r∘f}(d)`.

Conclusion (Lean): `Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a naturality/functoriality lemma for a linear functional on the exponent monoid; a helper for `index_rename`.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | index of polynomial invariant under embedding into more variables Roth lemma weight i_j/r_j | partial | index = min of `∑ i_h / r_h`; invariance under embedding used implicitly, not stated as a lemma | arXiv 1305.0926, math/9708214, Evertse (Leiden) notes, Natarajan–Thangadurai chapter |
| 2 | WebSearch (general form) | weighted degree monomial change of variables pushforward exponent vector linear functional composition | partial | weighted degree `⟨w, α⟩`; monomial maps act linearly on exponent vectors | Magma docs, arXiv 0912.3879, Lin's monomial-maps paper (1007.0253); no explicit lemma |
| 3 | WebSearch (named-after / aliases) | weighted degree invariant under renaming of variables weighted homogeneous polynomial rename | yes | weighted degree is preserved by renaming when the weights are renamed along (`w ∘ e`) | mathlib WeightedHomogeneous docs mirrors; folklore |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `renam`, `embed`, `Lemma 4-2` | yes | l.621-623 (proof of Lemma 4-2: embedding `P` into more variables leaves its index unchanged); l.631-634 (Lean note: prove invariance under variable renaming as a separate lemma) | project paper §4 |
| 6 | nLab | graded ring / grading on polynomial ring | partial | a grading is a monoid hom from exponents; pulling back gradings along variable maps | definitional |
| 7 | nCatLab | — | n/a | — | not a categorical concept beyond adjunction of pushforward/pullback of finitely supported functions (linear algebra) |
| 8 | Stacks Project | graded rings, weighted polynomial rings | partial | morphisms of weighted polynomial rings preserving degree | nothing lemma-level |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | too immediate for discussion |
| 10 | recent arXiv (last 5 years) | (results of #2: arXiv 2604.26950 weighted linearization) | partial | coordinate changes respecting a weight filtration | same fact implicit |

### Literature summary (Phase 3)

Concept identified as: naturality of the weighted degree under change of variables — for `f : σ → τ`, `⟨w, f_* d⟩ = ⟨w ∘ f, d⟩` (pushforward of finitely supported functions is the transpose of precomposition).
Sources agree on the standard form: yes (immediate from linearity of `d ↦ ∑ d_i w_i`; never a named result).
Most general standard form: for any map `f` (no injectivity), any exponent semiring `R` and any `R`-module of weights `M`.
Generality dimensions where the literature varies:
  - injectivity: Roth's use is an embedding (injective), but the identity holds for all `f`.
  - weights: integer gradings vs `1/r_j` vs arbitrary module values.
Disagreement with the literature: the project carries an injectivity hypothesis the standard fact does not need.

### Generality analysis — `Roth.weight_mapDomain`

Literature-standard form (from Phase 3): `Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d` for any `f`, `R`, `M`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hf : Function.Injective f` | required | none | yes | additivity of the weight suffices; verified for the project form (evidence (3), (4)) and a non-injective instance (evidence (6)) |
| 2 | weight vector | `1/r j`, `r : τ → ℕ` | any `w : τ → M` | yes | realised by `Finsupp.linearCombination_mapDomain` (evidence (1)) |
| 3 | codomain `ℝ`, exponents `ℕ` | ℝ, ℕ | `Module R M`, any semiring `R` | yes | evidence (1) |
| 4 | `[Fintype σ] [Fintype τ]` | required | not needed | yes for the re-aimed form; no for the project form | `Roth.weight` needs both to typecheck; evidence (1) uses none |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — the general form is already in mathlib (`Finsupp.linearCombination_mapDomain`, which applies to `Finsupp.weight` by definition), false-positive class 4, routed to NO-mathlib-has-it.
Number of weakening opportunities found: 4; row 1 (drop `hf`) verified for the project lemma itself in the evidence file (`weight_mapDomain'`, compiles), rows 2–4 verified via evidence (1).
Proposed restatement: none to add to mathlib; locally `theorem weight_mapDomain (f : σ → τ) (r : τ → ℕ) (d : σ →₀ ℕ) : weight r (d.mapDomain f) = weight (r ∘ f) d`.
Cost of restatement: CHEAP (proof of evidence (4); three callers drop one argument).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | only hypothesis is injectivity, which is superfluous |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | yes | after bundling `Roth.weight r` as an `AddMonoidHom` (parent refactor), this is `(weight r).comp (mapDomain.addMonoidHom f) = weight (r ∘ f)`, i.e. `linearCombination_comp_lmapDomain` | `Finsupp.linearCombination_mapDomain`, `linearCombination_comp_lmapDomain` |
| 4 | bundled substructure? | yes | same as #3 | as #3 |
| 5 | field-specific to semiring? | yes | any semiring of exponents, any module of weights | covered by `linearCombination_mapDomain` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary `w : τ → M` | as #3 |
| 8 | concrete-via-abstract? | yes (mild) | the proof uses only additivity of `n ↦ n / r j`; that is exactly why injectivity is unnecessary | `Finsupp.sum_mapDomain_index` (non-injective version) |
| 9 | false-generalisation guard | no false generalisation | the generalised form specialises back to the project lemma with `hf` (evidence (5) still holds; (3) implies it) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.linearCombination_mapDomain` applied to `Finsupp.weight w` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: the `Finsupp.linearCombination` / `Finsupp.weight` API; `MvPolynomial.weightedTotalDegree_rename_of_injective` is the polynomial-level analogue already in mathlib.
  - Real mathematical improvement: the statement is naturality of a linear functional, which holds for every `f`; removing the injectivity hypothesis is a genuine weakening.

### Proof strategy — `Roth.weight_mapDomain`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after the parent refactor, `Finsupp.linearCombination_mapDomain` in one line | CHEAP (part of the parent refactor) |
| 5 | missing mathlib helpers | no | `Finsupp.sum_mapDomain_index` and `linearCombination_mapDomain` exist | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: use `Finsupp.sum_mapDomain_index` (additive `h`) instead of `Finsupp.sum_mapDomain_index_inj`, removing `hf`; after the parent refactor use `Finsupp.linearCombination_mapDomain`.
  - Cost: CHEAP
  - Missing mathlib API (if any): none.
  - Would refactoring make the proof strictly shorter / cleaner? yes for the bundled version (one term); same length for the unbundled version, but a strictly weaker hypothesis set.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_mapDomain`

[A] Lean-Finder       "weighted degree of a multi-index is unchanged by pushing it forward along a map of variables and pulling back the weights"   hits: `MvPolynomial.weightedTotalDegree_rename_of_injective`, `MvPolynomial.isWeightedHomogeneous_monomial`, `weightedTotalDegree'`
[B] Loogle            `Finsupp.linearCombination _ _ (Finsupp.mapDomain _ _)`   no hits (pattern too loose for the bundled coercion); name-based hit found via [C] and [D]
[C] LeanSearch        "Finsupp.weight of mapDomain f d equals weight of composition w ∘ f applied to d"   hits: `Finsupp.linearCombination_mapDomain` (top hit), `Finsupp.weight`, `Finsupp.mapDomain_comp`
[D] Grep mathlib src  `weight.*mapDomain`, `mapDomain.*weight`, `linearCombination_mapDomain`, `weightedTotalDegree_rename`, `namespace Roth`   hits: `Finsupp.linearCombination_mapDomain` (Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158, `@[simp]`), `linearCombination_comp_lmapDomain` (:147), `linearCombination_embDomain` (:153), `MvPolynomial.weightedTotalDegree_rename_of_injective` (Mathlib/RingTheory/MvPolynomial/Homogeneous.lean:78, whose proof is `unfold weight; simp`, i.e. this fact inline), `Finsupp.degree_mapDomain` (Mathlib/Data/Finsupp/Weight.lean:273, the `w = 1` case); no `Finsupp.weight_mapDomain`; no `Roth` namespace
[E] Name pattern      `lean_local_search weight_mapDomain`: n/a (tool error: ripgrep not on PATH); replaced by the grep in [D] and by compiling `Finsupp.linearCombination_mapDomain` in the evidence file

Searched for both the user's form (`weight r (d.mapDomain f) = weight (r ∘ f) d` with injective `f`) and the re-aimed form (`Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d`).

Concluded: found in mathlib as `Finsupp.linearCombination_mapDomain`; more general form (no injectivity, any `R`, `M`); applies to `Finsupp.weight` definitionally (evidence (1), and by `simp [Finsupp.weight]` in (1')).

### Normal-form check — `Roth.weight_mapDomain`

Equivalent formalisms: `weight r (d.mapDomain f) = weight (r ∘ f) d`; `Finsupp.weight w (mapDomain f d) = Finsupp.weight (w ∘ f) d`; `(linearCombination R v').comp (lmapDomain R R f) = linearCombination R (v' ∘ f)`; `∑ t, (mapDomain f d) t / r t = ∑ s, d s / r (f s)`.
Does mathlib already have a canonical form for this idea? yes: `Finsupp.linearCombination_mapDomain` (pushed-forward form on the LHS, pulled-back weights on the RHS).
Is our statement stated against the canonical form? yes, same orientation (mapDomain on the LHS, `r ∘ f` on the RHS).
RHS convention respected? yes.

### Syntactic generality — `Roth.weight_mapDomain`

Alternative restatements attempted:
- drop `hf` (compiles; evidence (3), (4))
- re-aimed `Finsupp.weight` form (compiles; evidence (1))
Chosen restatement: drop `hf`, keep the rest.
Justification: callers then no longer need to supply `Option.some_injective _`, `Fin.castSucc_injective n`, `hf`; the `rw` chains become `weight_mapDomain` with no argument.

### Superfluous-argument audit — `Roth.weight_mapDomain`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hf : Function.Injective f` | no | conclusion holds for every `f` (evidence (3), (4), (6)) |
| 2 | `[Fintype τ]`, `[Fintype σ]` | yes | needed for `Roth.weight` to typecheck |
| 3 | `r`, `d`, `f` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (drop `hf`)
Superfluous arguments: 1 to drop (`hf`)

Overall: RESTATE-BEFORE-SHIP (locally; nothing ships to mathlib)

### Call sites — `Roth.weight_mapDomain`

Internal use count: 3 (outside Roth/Box.lean)
External-to-file callers: 3 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:219 | `exact weight_mapDomain hf r d` (in `index_rename`, which still needs `hf` for `support_rename_of_injective`) |
| Roth/Theta.lean:391 | `rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1` |
| Roth/Lattice.lean:155 | `rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]` |

Inline-derivation grep:
  - (none) — `grep -rn mapDomain Roth/` shows no other re-derivation of the weight of a pushed-forward multi-index.

### Composition check (Phase 6)

Can `Roth.weight_mapDomain` be derived from mathlib in ≤3 chained calls?

Attempt 1 (re-aimed form): `Finsupp.linearCombination_mapDomain (R := R) (v' := w) f d`
  - Mathlib decls used: `Finsupp.linearCombination_mapDomain`
  - Result: succeeds (evidence (1)); also `simp [Finsupp.weight]` (evidence (1'))

Attempt 2 (project form, no `hf`): parent bridge `Roth.weight r d = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d`, then `rw [bridge, bridge]; exact Finsupp.linearCombination_mapDomain (R := ℕ) f d`
  - Result: succeeds (evidence (3))

Attempt 3 (project form, no `hf`, no bridge): `simpa [Finsupp.sum_fintype, Roth.weight, add_div] using Finsupp.sum_mapDomain_index (h := fun j n ↦ (n : ℝ) / r j) ..`
  - Result: succeeds (evidence (4))

Conclusion: COMPOSABLE (re-aimed form is literally an existing mathlib lemma; routed to NO-mathlib-has-it)

## Verdict: `Roth.weight_mapDomain`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): naturality `⟨w, f_* d⟩ = ⟨w ∘ f, d⟩` of the weighted degree; used implicitly in the paper's Lemma 4-2 (clean.tex l.621-623, 631-634) and in mathlib's `weightedTotalDegree_rename_of_injective`; never a named result.
- Generality analysis (Phase 4): STRICTLY NARROWER (superfluous `hf`, specialised weights), with the general form already in mathlib (class 4).
- Mathlib search (Phase 5): found in mathlib as `Finsupp.linearCombination_mapDomain`; more general form.
- Composition check (Phase 6): COMPOSABLE (one call after the parent bridge).

**Rationale:**

Re-aimed at `Finsupp.weight` (the parent `Roth.weight` equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`), the statement is `Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d`. Since `Finsupp.weight w` is by definition `(linearCombination R w).toAddMonoidHom`, this is exactly mathlib's `@[simp]` lemma `Finsupp.linearCombination_mapDomain`, stated for any map `f`, any semiring `R` and any `R`-module `M`. There is no `Finsupp.weight_mapDomain` alias, but adding one would be a one-line restatement of a `simp` lemma that already fires (`simp [Finsupp.weight]` closes it), not new content. The project lemma's injectivity hypothesis is an artefact of the proof using `sum_mapDomain_index_inj`; the evidence proves the project lemma without it.

WHY not: mathlib has the general fact as `Finsupp.linearCombination_mapDomain`. Belongs-elsewhere check: keep it project-local in Roth/Box.lean as the change-of-variables lemma of the unbundled `Roth.weight`, but without `hf`.

Existing mathlib decl:        `Finsupp.linearCombination_mapDomain`
Located at:                   `Mathlib/LinearAlgebra/Finsupp/LinearCombination.lean:158`
Our form follows in ≤1 line:
```lean
example (w : τ → M) (f : σ → τ) (d : σ →₀ R) :
    Finsupp.weight w (d.mapDomain f) = Finsupp.weight (w ∘ f) d :=
  Finsupp.linearCombination_mapDomain (R := R) (v' := w) f d
-- project form via the parent bridge, no injectivity:
example (f : σ → τ) (r : τ → ℕ) (d : σ →₀ ℕ) :
    Roth.weight r (d.mapDomain f) = Roth.weight (r ∘ f) d := by
  rw [bridge, bridge]; exact Finsupp.linearCombination_mapDomain (R := ℕ) f d
```
Call sites in our project (from Phase 6.0):  3
Refactor plan: while `Roth.weight` stays unbundled, restate as `theorem weight_mapDomain (f : σ → τ) (r : τ → ℕ) (d : σ →₀ ℕ)` (no `hf`) with the proof `simpa [Finsupp.sum_fintype, weight, add_div] using Finsupp.sum_mapDomain_index (s := d) (h := fun j n ↦ (n : ℝ) / r j) (fun _ ↦ by simp) (fun _ _ _ ↦ by push_cast; ring)`; then at Roth/Index.lean:219 write `exact weight_mapDomain f r d` (keeping `hf` in `index_rename`, which needs it for `support_rename_of_injective`), at Roth/Theta.lean:391 replace `weight_mapDomain (Option.some_injective _)` by `weight_mapDomain`, and at Roth/Lattice.lean:155 replace `weight_mapDomain (Fin.castSucc_injective n)` by `weight_mapDomain`; update the Box.lean module docstring line 33 ("an injective change of variables" to "a change of variables"). If the parent refactor (`Roth.weight r : (σ →₀ ℕ) →+ ℝ := Finsupp.weight _`) is carried out, the proof becomes `Finsupp.linearCombination_mapDomain _ f d` (or the lemma can be deleted and `Finsupp.linearCombination_mapDomain` used in those `rw` chains).
Next action: no mathlib PR; drop the superfluous `hf` locally (CHEAP).

---

## Next step

No mathlib action. Drop the superfluous injectivity hypothesis of `Roth.weight_mapDomain` (proof via `Finsupp.sum_mapDomain_index`) and update Index.lean:219, Theta.lean:391, Lattice.lean:155; under the parent refactor it becomes `Finsupp.linearCombination_mapDomain`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_mapDomain/weight_mapDomain_reaim.lean` (imports `Roth.Box`; `lake env lean` produces no output, i.e. compiles clean after one fix of named arguments): (1) re-aimed form for general `R`, `M` as `Finsupp.linearCombination_mapDomain`, (1') same by `simp [Finsupp.weight]`; (2) parent bridge; (3) `weight_mapDomain'` — project lemma without `hf` via bridge + `linearCombination_mapDomain`; (4) project lemma without `hf` via `Finsupp.sum_mapDomain_index`; (5) current injective proof still works; (6) non-injective instance `Fin 2 → Unit`.
- LeanSearch (top hit `Finsupp.linearCombination_mapDomain`), Lean-Finder (`MvPolynomial.weightedTotalDegree_rename_of_injective`), Loogle (no hit on a loose pattern); `lean_local_search` unavailable (ripgrep not on PATH).
- Mathlib greps: `weight.*mapDomain`, `linearCombination_mapDomain` (LinearCombination.lean:147, 153, 158), `weightedTotalDegree_rename_of_injective` (Homogeneous.lean:78), `degree_mapDomain` (Weight.lean:273), `namespace Roth` (none).
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.554, 615-634).
- Project grep `grep -rn weight_mapDomain Roth/` (3 call sites + declaration + docstring).
