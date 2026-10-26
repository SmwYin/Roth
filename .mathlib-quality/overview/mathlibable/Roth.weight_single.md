---
decl: Roth.weight_single
file: Roth/Box.lean
line: 96
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the analogue Finsupp.weight w (single s c) = c • w s is exactly mathlib's Finsupp.weight_single; the project form is a two-line simp unfolding used at 2 rewrite sites.
action: Keep in Roth/Box.lean while Roth.weight is unbundled; if Roth.weight is refactored onto Finsupp.weight (parent report), reprove it as Finsupp.weight_single plus nsmul_eq_mul and div_eq_mul_inv (keeping the name for Theta.lean:391 and Lattice.lean:155); no mathlib PR.
---

# Roth.weight_single

## Inventory entry

### `theorem Roth.weight_single`
- **Type**: `{σ : Type*} [Fintype σ] (r : σ → ℕ) (j : σ) (n : ℕ) : Roth.weight r (Finsupp.single j n) = n / r j`
- **What**: The single multi-index `n • e_j` has weight `n / r_j`.
- **How**: `classical; simp [weight, Finsupp.single_apply, ite_div]` (unfold to the `univ` sum, rewrite each coordinate with `Finsupp.single_apply`, push the `if` through the division with `ite_div`, collapse with `Finset.sum_ite_eq`).
- **Hypotheses**: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Theta.lean:391 (`rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1`); Roth/Lattice.lean:155 (`rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]`).
- **Visibility**: public
- **Lines**: 95–98, proof length 2 lines
- **Notes**: no source citation in the docstring; not `@[simp]`.

## Junk check (Step 8)
- Used anywhere? Yes: 2 call sites in 2 files (Theta, Lattice), both inside `rw` chains alongside `weight_add` and `weight_mapDomain`.
- Wrapper of 1–2 mathlib calls? Yes: a `simp` unfolding; re-aimed, it is `Finsupp.weight_single` + `nsmul_eq_mul` + `div_eq_mul_inv`.
- Does mathlib have it? For the re-aimed `Finsupp.weight`: yes, `Finsupp.weight_single` (Mathlib/Data/Finsupp/Weight.lean:96).
- Too specific (inline)? No: inlining the `simp` unfolding into two `rw` chains would be worse than the named lemma while `Roth.weight` is unbundled.
- Well-chosen? Yes as the single-index lemma for an unbundled function.
- Conclusion: `KEEP` — action: keep while `Roth.weight` is unbundled; under the parent `REPLACE` refactor, reprove it in one line from `Finsupp.weight_single`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_single` not in mathlib (no `namespace Roth` in Mathlib; only `Finsupp.weight_single`, a different namespace). Not a pure glue lemma (`simp` with two lemmas). Parent `Roth.weight` is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`; per the re-aim rule this run is re-aimed at `Finsupp.weight`: target `Finsupp.weight w (Finsupp.single s c) = c • w s`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` elaborates with only a header-linter warning)
- decl `Roth.weight_single`: resolved at Roth/Box.lean:96
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_single` is a theorem stating the following: for a finite index set `σ`, parameters `r ∈ ℕ^σ`, an index `j` and `n ∈ ℕ`, the multi-index `n e_j` (all coordinates zero except the `j`-th, equal to `n`) has weight `w_r(n e_j) = n / r_j`. Re-aimed: for any weight vector `w`, the weighted degree of `c e_s` is `c • w_s`, i.e. the weighted degree of the monomial `X_s^c` is `c` times the weight of `X_s`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (needed for `Roth.weight`).
- `r : σ → ℕ` — parameters `r_j`.
- `j : σ`, `n : ℕ` — the index and exponent.

Hypotheses (Lean side):
- none (with `r j = 0` both sides are `0` by `x / 0 = 0`).

Conclusion (math): `w_r(n e_j) = n / r_j`.

Conclusion (Lean): `Roth.weight r (Finsupp.single j n) = n / r j`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-step evaluation lemma for a linear functional on a basis vector.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index weight of single monomial x_j^n i_j/r_j polynomial index | partial | index = min of `∑ j_i / r_i`; the weight of `n e_j` being `n / r_j` is implicit, never stated | arXiv math/0307203, 1806.10737, 1305.0926, Evertse notes |
| 2 | WebSearch (general form) | weighted degree of a monomial x_i^n equals n times weight w_i | yes | W-degree `∑ w_i α_i`; for `x_i^n` it is `n w_i` | arXiv 2202.05742, 1412.7547, Magma docs |
| 3 | WebSearch (named-after / aliases) | weighted polynomial ring deg x_i = w_i grading variable weights monomial degree | yes | graded ring with `deg x_i = w_i`, so `deg x_i^n = n w_i` | arXiv 1412.7547, math/0506333, Magma docs |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `r_j`, `i_j` | yes | l.549-556 (index as min of `∑_j d_j / r_j`, natural weights `D / r_j`), l.565, 586 | single-index weight used implicitly in the Theta/Lattice steps |
| 6 | nLab | graded ring / grading on polynomial ring | partial | degree map of a grading sends `x_i` to `deg x_i`, multiplicative powers to multiples | definitional; no lemma-level content |
| 7 | nCatLab | — | n/a | — | not a categorical concept (evaluation of a linear map on a basis vector) |
| 8 | Stacks Project | weighted polynomial rings / graded rings | partial | `deg x_i^n = n deg x_i` built into the grading | nothing beyond the definition |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | immediate fact; no discussion |
| 10 | recent arXiv (last 5 years) | (results of #2: arXiv 2202.05742) | yes | matrix-weighted degree `W·α`, linear in `α` | same fact, implicit |

### Literature summary (Phase 3)

Concept identified as: evaluation of the weighted degree on a basis multi-index (weighted degree of a pure power `X_s^c`).
Sources agree on the standard form: yes (immediate from the definition `∑ w_i α_i`; never a named result).
Most general standard form: for any weight vector `w : σ → M` (module over the exponent semiring `R`), `weight w (c e_s) = c • w_s`.
Generality dimensions where the literature varies:
  - weight values: positive integers vs `1/r_j` vs arbitrary — covered by any `Module R M`.
  - finiteness of `σ`: not needed.
Disagreement with the literature: none.

### Generality analysis — `Roth.weight_single`

Literature-standard form (from Phase 3): `Finsupp.weight w (Finsupp.single s c) = c • w s`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector | `1/r j`, `r : σ → ℕ` | any `w : σ → M` | yes | realised by `Finsupp.weight_single` (evidence (1), compiles) |
| 2 | codomain `ℝ` | ℝ | any `AddCommMonoid M` with `Module R M` | yes | evidence (1) |
| 3 | `[Fintype σ]` | required | not needed | yes for the re-aimed form; no for the project form | `Roth.weight` needs it to typecheck; evidence (2) compiles without it |
| 4 | exponent `n : ℕ` | ℕ | any semiring `R` | yes | evidence (1) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is already in mathlib (`Finsupp.weight_single`), false-positive class 4, routed to NO-mathlib-has-it.
Number of weakening opportunities found: 4 (rows 1–4), all verified in the evidence file.
Proposed restatement: none to add; `Finsupp.weight_single w s c`.
Cost of restatement: CHEAP (nothing to write).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | yes | bundle `Roth.weight r` as an `AddMonoidHom` (parent refactor); then this lemma is `Finsupp.weight_single` | `Finsupp.weight_single`, `map_add`, `map_sum` |
| 4 | bundled substructure? | yes | same as #3 | as #3 |
| 5 | field-specific to semiring? | yes | any codomain module | covered by `Finsupp.weight_single` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary weight vector `w : σ → M` | as #3 |
| 8 | concrete-via-abstract? | no | proof is a one-step `simp`; nothing beyond the re-aimed form | — |
| 9 | false-generalisation guard | no false generalisation | re-aimed form specialises back to the project lemma (evidence (2), (4)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.weight_single w s c` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: the `Finsupp.weight` API (`weight_single`, `weight_eq_sum`, `map_add`).
  - Real mathematical improvement: the fact is the evaluation of a bundled linear functional on a basis vector, already provided.

### Proof strategy — `Roth.weight_single`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after bundling `Roth.weight`, `Finsupp.weight_single` + `nsmul_eq_mul` + `div_eq_mul_inv` | CHEAP (part of the parent refactor) |
| 5 | missing mathlib helpers | no | `Finsupp.weight_single` exists | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the current unbundled def; `simp [weight, Finsupp.single_apply, ite_div]` is the natural proof). After the parent refactor the proof becomes `rw [Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]`.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_single`

[A] Lean-Finder       "weighted degree of the single multi-index n e_j is n times the weight of j"   hits: `MvPolynomial.isWeightedHomogeneous_X`, `MvPolynomial.isWeightedHomogeneous_monomial`, `Finsupp.weight_single`, `MvPowerSeries.weightedOrder_monomial(_of_ne_zero)`
[B] Loogle            `Finsupp.weight _ (Finsupp.single _ _)`   hit: `Finsupp.weight_single` (only result)
[C] LeanSearch        "weight of Finsupp.single s r equals r • w s"   hits: `Finsupp.weight_single`, `Finsupp.weight_apply`, `Finsupp.weight_single_one_apply`, `Finsupp.weight`, `Finsupp.weight_single_index`
[D] Grep mathlib src  `weight_single`, `namespace Roth`   hits: `Finsupp.weight_single` (Mathlib/Data/Finsupp/Weight.lean:96), `weight_single_index` (:88), `weight_single_one_apply` (:92); no `Roth` namespace
[E] Name pattern      `Finsupp.weight_single`, `Finsupp.weight_eq_sum` (used in compiled evidence)   hits

Searched for both the user's form (`weight r (single j n) = n / r j`) and the re-aimed form (`Finsupp.weight w (single s c) = c • w s`).

Concluded: found in mathlib as `Finsupp.weight_single`; more general form (we are a specialisation via the parent bridge).

### Normal-form check — `Roth.weight_single`

Equivalent formalisms: `weight r (single j n) = n / r j`; `Finsupp.weight w (single s c) = c • w s`; `weight r (single j n) = n * (r j)⁻¹`.
Does mathlib already have a canonical form for this idea? yes: `Finsupp.weight_single` (`c • w s` on the RHS).
Is our statement stated against the canonical form? It is the specialisation with `w s = (r s)⁻¹` and `•` simplified to `/`; fine locally.
RHS convention respected? yes (evaluated form on the RHS).

### Syntactic generality — `Roth.weight_single`

Alternative restatements attempted:
- `Finsupp.weight_single` applied to `fun j ↦ ((r j : ℝ))⁻¹` (compiles; evidence (2))
- `@[simp]` tagging (would not help the two `rw` call sites)
Chosen restatement: as stated.
Justification: `n / r j` is the form consumed at Theta.lean:391 and Lattice.lean:155 (the latter follows with `mul_div_assoc`).

### Superfluous-argument audit — `Roth.weight_single`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed for `Roth.weight` to typecheck |
| 2 | `r` | yes | — |
| 3 | `j`, `n` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_single`

Internal use count: 2 (outside Roth/Box.lean)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:391 | `rw [weight_add, weight_mapDomain (Option.some_injective _), weight_single] at h1` |
| Roth/Lattice.lean:155 | `rw [weight_add, weight_mapDomain (Fin.castSucc_injective n), weight_single, mul_div_assoc]` |

Inline-derivation grep:
  - (none) — no re-derivation of the weight of a single multi-index elsewhere in Roth/.

### Composition check (Phase 6)

Can `Roth.weight_single` be derived from mathlib in ≤3 chained calls?

Attempt 1 (re-aimed form): `Finsupp.weight_single w s c`
  - Mathlib decls used: `Finsupp.weight_single`
  - Result: succeeds (evidence (1))

Attempt 2 (project form): parent bridge `Roth.weight r f = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) f`, then `rw [Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]`
  - Result: succeeds (evidence (3), (4)); the current proof also re-checked (evidence (5))

Conclusion: COMPOSABLE (re-aimed form is literally an existing mathlib lemma; routed to NO-mathlib-has-it)

## Verdict: `Roth.weight_single`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): the weighted degree of `X_s^c` is `c w_s`, immediate from the definition; used implicitly in the paper, never named.
- Generality analysis (Phase 4): STRICTLY NARROWER, general form already in mathlib (class 4).
- Mathlib search (Phase 5): found in mathlib as `Finsupp.weight_single`.
- Composition check (Phase 6): COMPOSABLE (one call, plus `nsmul_eq_mul`/`div_eq_mul_inv` for the project spelling).

**Rationale:**

Re-aimed at `Finsupp.weight` (the parent `Roth.weight` equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`), the statement is exactly mathlib's `Finsupp.weight_single : Finsupp.weight w (Finsupp.single s r) = r • w s`, stated for any semiring of exponents and any module of weights, with no `Fintype` assumption. The project lemma exists only because `Roth.weight` is an unbundled `univ` sum; its spelling `n / r j` is the `nsmul` form simplified.

WHY not: mathlib has the general fact as `Finsupp.weight_single`. Belongs-elsewhere check: keep it project-local in Roth/Box.lean as the single-index lemma of `Roth.weight` (its `n / r j` spelling is what the two `rw` chains consume).

Existing mathlib decl:        `Finsupp.weight_single`
Located at:                   `Mathlib/Data/Finsupp/Weight.lean:96`
Our form follows in ≤1 line:
```lean
example (w : σ → M) (s : σ) (c : R) :
    Finsupp.weight w (Finsupp.single s c) = c • w s := Finsupp.weight_single w s c
-- project form via the parent bridge:
example (r : σ → ℕ) (j : σ) (n : ℕ) : Roth.weight r (Finsupp.single j n) = n / r j := by
  rw [bridge, Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]
```
Call sites in our project (from Phase 6.0):  2
Refactor plan: while `Roth.weight` stays unbundled, keep the lemma with its current proof. If the parent refactor (`Roth.weight r : (σ →₀ ℕ) →+ ℝ := Finsupp.weight fun j ↦ ((r j : ℝ))⁻¹`) is carried out, reprove `Roth.weight_single` as `by rw [Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv]` and keep the name, so Roth/Theta.lean:391 and Roth/Lattice.lean:155 are unchanged (alternatively replace `weight_single` by `Finsupp.weight_single, nsmul_eq_mul, div_eq_mul_inv` in those two `rw` lists and delete the lemma).
Next action: no mathlib PR; reprove from `Finsupp.weight_single` only as part of the parent `Roth.weight` refactor.

---

## Next step

No mathlib action. Keep as the single-index lemma for `Roth.weight`; under the parent refactor its proof becomes `Finsupp.weight_single` + `nsmul_eq_mul` + `div_eq_mul_inv` (call sites Theta.lean:391, Lattice.lean:155 unchanged).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_single/weight_single_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no errors, one header-linter style warning only): (1) `Finsupp.weight_single` for general `R`, `M`; (2) the re-aimed form specialised to `w = fun j ↦ (r j : ℝ)⁻¹` without `[Fintype σ]`; (3) parent bridge `Roth.weight r d = Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d`; (4) project lemma via bridge + `Finsupp.weight_single`; (5) current proof `simp [Roth.weight, Finsupp.single_apply, ite_div]`.
- Loogle `Finsupp.weight _ (Finsupp.single _ _)` (hit: `Finsupp.weight_single`); LeanSearch and Lean-Finder queries as in the search-status block.
- Mathlib greps: `weight_single` (Weight.lean:88, 92, 96), `namespace Roth` (none).
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.549-556, 565, 586).
- Project grep `grep -rn weight_single Roth/` (2 call sites + declaration).
