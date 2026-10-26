---
decl: Roth.weight_zero
file: Roth/Box.lean
line: 80
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: KEEP
rationale: Re-aimed at Finsupp.weight (parent Roth.weight is NO-mathlib-has-it), the analogue Finsupp.weight w 0 = 0 is mathlib's generic simp lemma map_zero (Finsupp.weight w is an AddMonoidHom); the project form is a one-line simp unfolding with no explicit call sites (only a @[simp] lemma).
action: Keep as the @[simp] companion of Roth.weight in Roth/Box.lean while Roth.weight is an unbundled function; if Roth.weight is refactored onto Finsupp.weight (parent report), delete it since map_zero (simp) covers it; no mathlib PR.
---

# Roth.weight_zero

## Inventory entry

### `theorem Roth.weight_zero`
- **Type**: `{σ : Type*} [Fintype σ] (r : σ → ℕ) : Roth.weight r 0 = 0`
- **What**: The zero multi-index has weight `0`.
- **How**: `simp [weight]` (unfold to `∑ j, ((0 : σ →₀ ℕ) j : ℝ) / r j`; `Finsupp.coe_zero`, `Nat.cast_zero`, `zero_div`, `Finset.sum_const_zero`).
- **Hypotheses**: none beyond the section variable `[Fintype σ]` (needed by `Roth.weight`).
- **Uses from project**: `Roth.weight`
- **Used by**: no explicit reference anywhere in Roth/ (`grep -rn weight_zero Roth/` returns only the declaration); it is tagged `@[simp]`, so it may fire implicitly inside the ~18 `simp` calls in Roth/ that mention `weight`.
- **Visibility**: public
- **Lines**: 78–81, proof length 1 line
- **Notes**: `@[simp]` attribute; no source citation in the docstring (a trivial fact, not stated in clean.tex).

## Junk check (Step 8)
- Used anywhere? No explicit call site; potentially used implicitly as a `@[simp]` lemma.
- Wrapper of 1–2 mathlib calls? Yes: `simp [weight]` (and, re-aimed, `map_zero`).
- Does mathlib have it? For the re-aimed `Finsupp.weight`: yes, as the generic `map_zero` (simp), since `Finsupp.weight w : (σ →₀ R) →+ M`. No dedicated `Finsupp.weight_zero` (none needed).
- Too specific (inline)? It cannot be inlined usefully: its value is as a simp lemma for the unbundled `Roth.weight`, which `simp` cannot otherwise rewrite without unfolding.
- Well-chosen? Yes, as the standard `_zero` simp companion of an unbundled function; it becomes redundant only if `Roth.weight` is bundled.
- Conclusion: `KEEP` — action: keep while `Roth.weight` is an unbundled function; remove when the parent `REPLACE` refactor (`Roth.weight r := Finsupp.weight (fun j ↦ ((r j : ℝ))⁻¹)`) lands, since `map_zero` then fires under `simp`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said KEEP; qualified name `Roth.weight_zero` not in mathlib (no `namespace Roth` in Mathlib; only unrelated `ModularForm.eq_const_of_weight_zero`). Glue-ish (pure unfolding + `simp`) lemma about parent `Roth.weight`, whose verdict is `NO-mathlib-has-it` because it equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`. Per the re-aim rule, this run is re-aimed at `Finsupp.weight`: target statement `Finsupp.weight w 0 = 0`.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Box` has no diagnostics)
- decl `Roth.weight_zero`:   resolved at Roth/Box.lean:80
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Boxes of multi-indices bounded by `r` and the real weight `∑ d j / r j` used in Roth's theorem.

### Statement (Phase 1)

`Roth.weight_zero` is a theorem stating the following: for a finite index set `σ` and parameters `r ∈ ℕ^σ`, the weight `w_r(0) = ∑_j 0 / r_j` of the zero multi-index is `0`. Re-aimed: for any weight vector `w : σ → M`, the weighted degree `⟨w, 0⟩` of the zero exponent vector is `0`; i.e. the weighted degree, being additive, maps `0` to `0`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]` — finite variable set (needed for `Roth.weight` to typecheck).
- `r : σ → ℕ` — parameters (irrelevant to the conclusion).

Hypotheses (Lean side):
- none.

Conclusion (math): `w_r(0) = 0`.

Conclusion (Lean): `Roth.weight r 0 = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line simp lemma (value of an additive functional at `0`).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of polynomial weight sum i_j/r_j zero exponent P(alpha) nonzero index zero | yes | index = min of `∑ i_h/r_h` over nonvanishing derivatives; the zero exponent has weight 0, so `P(α) ≠ 0` gives index 0 | arXiv math/0307203, arXiv 1305.0926, arXiv math/9708214, Evertse notes; weight-of-zero used implicitly, never stated |
| 2 | WebSearch (general form) | weighted degree of zero multi-index is zero additive homomorphism weight function monomials | yes | weighted degree is an additive monoid hom `(σ →₀ ℕ) →+ M`, so `0 ↦ 0` | mathlib WeightedHomogeneous docs (several mirrors), Magma docs |
| 3 | WebSearch (named-after / aliases) | graded ring grading degree of constant monomial 1 is zero weight vector linear functional exponent lattice | yes | monomial weight `∑ m_i w_i` is linear in exponents; the constant monomial has degree 0 | arXiv 1611.07030 (positive gradings, `R_0 = K`), arXiv 0708.4402, Magma docs; folklore |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `weight` | partial | l.565-566: weight `∑ i_j/r_j` is zero exactly when every `i_j = 0` (uses the `⇐` direction implicitly) | project paper §4 |
| 6 | nLab | graded ring / grading | partial | degree map of a grading is a monoid hom, so the unit has degree 0 | no lemma-level content |
| 7 | nCatLab | — | n/a | — | not a categorical concept (value of an additive map at 0) |
| 8 | Stacks Project | graded rings (weighted polynomial rings) | partial | constants live in degree 0 | nothing to cite beyond the definition |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | immediate fact; no discussion |
| 10 | recent arXiv (last 5 years) | (results of #3: arXiv 2202.05742, 2607.20210) | partial | weight vectors / gradings with `deg 1 = 0` | used implicitly |

### Literature summary (Phase 3)

Concept identified as: the weighted degree (an additive functional on exponent vectors) vanishes at the zero exponent vector.
Sources agree on the standard form: yes (immediate from linearity; never a named result).
Most general standard form: any additive map `(σ →₀ R) →+ M` sends `0` to `0`; for weighted degree this is `Finsupp.weight w 0 = 0` for arbitrary `w : σ → M`, `R` a semiring.
Generality dimensions where the literature varies:
  - weight values / codomain: integers, rationals `1/r_j`, any additive monoid — all covered by the general form.
  - finiteness of `σ`: not needed.
Disagreement with the literature: none.

### Generality analysis — `Roth.weight_zero`

Literature-standard form (from Phase 3): `Finsupp.weight w (0 : σ →₀ R) = 0` for any `w : σ → M`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | weight vector | `1/r j`, `r : σ → ℕ` | any `w : σ → M` | yes | realised by `map_zero` (evidence (1), compiles) |
| 2 | codomain `ℝ` | ℝ | any `AddCommMonoid M` with `Module R M` | yes | evidence (1) |
| 3 | `[Fintype σ]` | required | not needed | yes for the re-aimed form; no for the project form | `Roth.weight` needs it to typecheck; evidence (5) shows `Finsupp.weight` form without `Fintype` |
| 4 | exponents `ℕ` | ℕ | any semiring `R` | yes | evidence (1) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the general form is already in mathlib (`map_zero` for the bundled `Finsupp.weight`), false-positive class 4, routed to NO-mathlib-has-it.
Number of weakening opportunities found: 4 (rows 1–4), all verified in the evidence file.
Proposed restatement: none to add; `map_zero (Finsupp.weight w)`.
Cost of restatement: CHEAP (nothing to write).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | yes | bundle `Roth.weight r` as an `AddMonoidHom` (parent refactor); then this lemma is `map_zero` | `map_zero` / `map_add` / `map_sum` for free |
| 4 | bundled substructure? | yes | same as #3 (bundled hom) | as #3 |
| 5 | field-specific to semiring? | yes | any codomain module | covered by `Finsupp.weight` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | arbitrary weight vector `w : σ → M` | as #3 |
| 8 | concrete-via-abstract? | no | proof is a one-step `simp` unfolding; nothing to extract beyond the re-aimed form | — |
| 9 | false-generalisation guard | no false generalisation | re-aimed form specialises back to the project lemma (evidence (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `map_zero (Finsupp.weight w)` (already in mathlib; nothing to add).
  - Cost: CHEAP
  - Mathlib downstream this enables: the whole `AddMonoidHom` API (`map_zero`, `map_add`, `map_sum`, `map_nsmul`).
  - Real mathematical improvement: the zero law is a consequence of additivity, not a separate fact.

### Proof strategy — `Roth.weight_zero`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | after bundling `Roth.weight`, `map_zero` | CHEAP (part of the parent refactor) |
| 5 | missing mathlib helpers | no | `map_zero` exists | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (for the current unbundled def; `simp [weight]` is the natural proof). After the parent refactor the lemma is redundant with `map_zero`.

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_zero`

[A] Lean-Finder       "weighted degree of the zero multi-index equals zero"   hits: `MvPolynomial.weightedTotalDegree'_zero`, `MvPolynomial.weightedTotalDegree_zero` (zero polynomial, different statement), `MvPolynomial.weightedDegree_eq_zero_iff`, `MvPolynomial.isWeightedHomogeneous_zero`; no dedicated lemma (the fact is `map_zero`)
[B] Loogle            `Finsupp.weight _ 0 = 0`   no hits (generic `map_zero` is not indexed under that pattern)
[C] LeanSearch        "Finsupp.weight of zero is zero"   hits: `Finsupp.weight_eq_zero_iff_eq_zero` (whose `←` direction is the fact), `MvPolynomial.weightedDegree_eq_zero_iff`, `Finsupp.single_zero`
[D] Grep mathlib src  `weight_zero` over Mathlib; `map_zero` in Mathlib/Data/Finsupp/Weight.lean   no `Finsupp.weight_zero` (only unrelated `ModularForm.eq_const_of_weight_zero`); Weight.lean:185 uses `rw [h, map_zero]` for exactly this fact
[E] Name pattern      `map_zero`, `Finsupp.weight` (used in compiled evidence)   hits

Searched for both the user's form (`weight r 0 = 0`) and the re-aimed form (`Finsupp.weight w 0 = 0`).

Concluded: found in mathlib as `map_zero` (applied to the `AddMonoidHom` `Finsupp.weight w`); more general form (we are a specialisation via the parent bridge).

### Normal-form check — `Roth.weight_zero`

Equivalent formalisms: `weight r 0 = 0`; `Finsupp.weight w 0 = 0`; `∑ j, (0 : ℝ) / r j = 0`.
Does mathlib already have a canonical form for this idea? yes: `map_zero` for bundled homs.
Is our statement stated against the canonical form? It is the `f 0 = 0` simp-normal shape, stated against the project def; fine locally.
RHS convention respected? yes (`= 0`).

### Syntactic generality — `Roth.weight_zero`

Alternative restatements attempted:
- `map_zero (Finsupp.weight w)` (compiles; evidence (1))
- implicit `r` (would make `simp` usage identical; explicit `r` is harmless for a simp lemma)
Chosen restatement: as stated.
Justification: used only as a simp lemma; argument explicitness is irrelevant there.

### Superfluous-argument audit — `Roth.weight_zero`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed for `Roth.weight` to typecheck |
| 2 | `r` | yes (in the statement) | conclusion independent of `r`, but `r` is part of the term |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_zero`

Internal use count: 0 explicit (outside and inside Roth/Box.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none explicit) | `@[simp]` lemma; may fire implicitly in the ~18 `simp` calls in Roth/ mentioning `weight` (e.g. Index.lean:114 `simpa [weight_add, hiw]`, Index.lean:245, 249 `simpa [weight, ...]`) |

Inline-derivation grep:
  - (none) — no re-derivation of `weight r 0 = 0` elsewhere in Roth/.
  - Mathlib's own analogue is inlined as `rw [h, map_zero]` at Mathlib/Data/Finsupp/Weight.lean:185.

### Composition check (Phase 6)

Can `Roth.weight_zero` be derived from mathlib in ≤3 chained calls?

Attempt 1 (re-aimed form): `map_zero (Finsupp.weight w)`
  - Mathlib decls used: `map_zero`, `Finsupp.weight`
  - Result: succeeds (evidence (1), (2), (5))

Attempt 2 (project form): `simp [Roth.weight]`, or via the parent bridge `weight_eq_finsupp_weight` then `map_zero`
  - Result: succeeds (evidence (3), (4))

Conclusion: COMPOSABLE (re-aimed form is literally an existing mathlib lemma; routed to NO-mathlib-has-it)

## Verdict: `Roth.weight_zero`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): vanishing of the weighted degree at the zero exponent is immediate from additivity; never a named result.
- Generality analysis (Phase 4): STRICTLY NARROWER, general form already in mathlib (class 4).
- Mathlib search (Phase 5): found in mathlib as `map_zero` for the `AddMonoidHom` `Finsupp.weight w`.
- Composition check (Phase 6): COMPOSABLE (one call).

**Rationale:**

Re-aimed at `Finsupp.weight` (the parent `Roth.weight` equals `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`), the statement `Finsupp.weight w 0 = 0` is mathlib's generic `map_zero`, a simp lemma, because `Finsupp.weight w : (σ →₀ R) →+ M` is bundled. Nothing about weights is missing from mathlib here. The project lemma exists only because `Roth.weight` is an unbundled function that `simp` cannot see through without unfolding.

WHY not: mathlib has the general fact as `map_zero`. Belongs-elsewhere check: keep it project-local in Roth/Box.lean as the `@[simp]` companion of the unbundled `Roth.weight`; it becomes deletable once the parent refactor bundles `Roth.weight`.

Existing mathlib decl:        `map_zero` (applied to `Finsupp.weight w`)
Located at:                   `Mathlib/Algebra/Group/Hom/Defs.lean` (`map_zero`, `ZeroHomClass`); `Finsupp.weight` at `Mathlib/Data/Finsupp/Weight.lean:82`
Our form follows in ≤1 line:
```lean
example (w : σ → M) : Finsupp.weight w (0 : σ →₀ R) = 0 := map_zero _
-- project form via the parent bridge:
example (r : σ → ℕ) : Roth.weight r 0 = 0 := by
  rw [weight_eq_finsupp_weight, map_zero]
```
Call sites in our project (from Phase 6.0):  0 explicit (implicit `simp` uses only)
Refactor plan: no explicit call sites to repoint. While `Roth.weight` stays unbundled, keep the lemma (it is the simp lemma that the implicit `simp` calls in Index.lean / Theta.lean / Lattice.lean may rely on). If the parent `Roth.weight` refactor onto `Finsupp.weight` is carried out, delete `Roth.weight_zero`; `map_zero` is `@[simp]` and takes over in every `simp` call, so no call site changes.
Next action: no mathlib PR; delete only as part of the parent `Roth.weight` refactor.

---

## Next step

No mathlib action. Keep as the `@[simp]` lemma for the unbundled `Roth.weight`; remove it when `Roth.weight` is redefined via `Finsupp.weight` (then `map_zero` covers it).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.weight_zero/weight_zero_reaim.lean` (imports `Roth.Box`; `lean_diagnostic_messages`: no diagnostics after adding `(R := ℕ)` to one elaboration): (1) `Finsupp.weight w 0 = 0` by `map_zero` for general `R`, `M`; (2) the same by `simp`; (3) project lemma via the parent bridge + `map_zero`; (4) current proof `simp [Roth.weight]`; (5) the re-aimed form without `[Fintype σ]`.
- Loogle `Finsupp.weight _ 0 = 0` (no hits); LeanSearch and Lean-Finder queries as in the search-status block.
- Mathlib greps: `weight_zero` over Mathlib; Mathlib/Data/Finsupp/Weight.lean (`map_zero` use at :185); `namespace Roth` (none).
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: grep of clean.tex (l.565-566).
- Project grep `grep -rn weight_zero Roth/` (declaration only).
