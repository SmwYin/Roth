---
decl: Roth.index_nonneg
file: Roth/Index.lean
line: 93
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Nonnegativity of the sInf-defined index is one call to Real.sInf_nonneg with the project weight_nonneg (compiled); its canonical counterpart for mathlib's ℕ∞-valued MvPowerSeries.weightedOrder is just zero_le, so nothing new for mathlib.
action: Keep locally as basic API of Roth.index (used at Roth/Index.lean:100 and Roth/Theta.lean:110, 395); do not upstream; if index is rebased on weightedOrder of taylor (Roth.index question 3), it becomes a positivity/div_nonneg one-liner.
---

# Roth.index_nonneg

## Inventory entry

### `theorem Roth.index_nonneg`
- **Type**: `(P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r` (with `[Fintype σ]`)
- **What**: The index of any real multivariate polynomial at any point, for any weights, is nonnegative.
- **How**: `Real.sInf_nonneg` applied to `weight r '' supp(taylor α P)`, with every member nonnegative by `Set.forall_mem_image` and the project's `weight_nonneg`.
- **Hypotheses**: none.
- **Uses from project**: `Roth.index`, `Roth.weight_nonneg` (Roth/Box.lean:75), implicitly `Roth.weight`, `MvPolynomial.taylor`
- **Used by**: Roth/Index.lean:100 (`index_eq_zero_iff`); Roth/Theta.lean:110 (`Θ_nonneg`), Roth/Theta.lean:395
- **Visibility**: public
- **Lines**: 92–94, proof length 1 line
- **Notes**: holds for all `r` (no positivity) and for `P = 0` (junk value `sInf ∅ = 0`).

## Junk check (Step 8)
- Used anywhere? Yes, 3 sites in 2 files.
- Wrapper of 1–2 mathlib calls? Yes (`Real.sInf_nonneg` + `Set.forall_mem_image`, plus project `weight_nonneg`), but it is a basic API lemma of the project def `Roth.index` and hides the `sInf`/image unfolding from callers; it is also the source's stated lemma ("We have ind(P) ≥ 0").
- Does mathlib have it? Not for `Roth.index` (project def). For mathlib's `MvPowerSeries.weightedOrder` (ℕ∞-valued) it is `zero_le`.
- Too specific (inline?)? No; inlining would expose the `sInf` definition at 3 sites, including in `Theta.lean`.
- Well-chosen? Yes; standard `foo_nonneg` name and shape, explicit arguments as used (`index_nonneg _ _ _`).
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, qualified name `Roth.index_nonneg` absent from mathlib (grep of `.lake/packages/mathlib/Mathlib` for `index_nonneg`: no hits). Not a glue lemma (proof is `Real.sInf_nonneg ...`, not `rfl`), so full run.

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.index_nonneg`:  ✓ resolved at Roth/Index.lean:93
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to integer weights (Roth §4)

### Statement (Phase 1)

`Roth.index_nonneg` is a theorem stating the following: for every `P ∈ ℝ[x_j : j ∈ σ]`, every `α ∈ ℝ^σ` and every `r ∈ ℕ^σ`, the index `ind_{α,r}(P) = min { ∑_j d_j / r_j : (Δ_d P)(α) ≠ 0 }` is `≥ 0` (with the Lean junk value `0` for `P = 0`).

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite set of variables (needed by `Roth.weight`)
- `P`, `α`, `r`: polynomial, point, weights

Hypotheses (Lean side):
- none

Conclusion (math): the index is nonnegative.

Conclusion (Lean): `0 ≤ index P α r`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma of the project def `Roth.index`; not a main result, not named.

### One-line check (Phase 2b)

Body line count: 1 (proof term)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | Roth's theorem index of a polynomial "ind" nonnegative weighted derivative lemma | yes | index = min of weighted derivative orders over nonvanishing derivatives (arXiv 2502.00731, math/0307203, 1305.0926, 1806.10737, Evertse notes) | nonnegativity is immediate (weights and orders nonnegative); 1305.0926 Prop. 6.21 uses `max{0, ...}` bounds implicitly relying on it |
| 2 | WebSearch (general form) | monomial valuation nonnegative on polynomial ring weighted order of vanishing nonnegative | yes | monomial valuation `v_{s,t}(f) = min{si + tj}` with nonnegative weights (arXiv 1707.00583, 1510.02295, 1712.08325) | nonnegativity on the polynomial ring follows from nonnegative weights and exponents; folklore |
| 3 | WebSearch (aliases / foundational) | infimum of a set of nonnegative reals is nonnegative sInf empty set zero | yes | inf of nonnegative set ≥ 0; mathlib convention `sInf ∅ = 0` (`Real.sInf_empty`, `Real.sInf_nonneg`) | the Lean proof is exactly this general fact |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "ind" | yes | clean.tex l.559: first lemma on the index, "We have ind(P) ≥ 0 and ind(P) = 0 iff ..."; l.545 sets ind(0) = +∞ | source states it as part of a lemma; Lean junk value 0 for P = 0 still satisfies it |
| 6 | nLab | valuation / order of vanishing | partial | valuation centred on a ring is nonnegative on it | no weighted multivariate at-a-point version |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing / valuation | partial | `ord` nonnegative on regular functions | same fact, different setting; nothing to add |
| 9 | MathOverflow / Math.SE | (covered by #2, #3) | no | — | folklore; no stand-alone statement |
| 10 | recent arXiv (last 5 years) | (#1: 2502.00731 (2025)) | yes | same definition | nonnegativity implicit |

### Literature summary (Phase 3)

Concept identified as: nonnegativity of the index / weighted order of vanishing / monomial valuation with nonnegative weights.
Sources agree on the standard form: yes; it is immediate from the definition (a min of nonnegative numbers) and is stated only in passing (clean.tex l.559).
Most general standard form: for a valuation-like `min` over the support with nonnegative weights, the value is `≥ 0`; abstractly, the infimum of a set of nonnegative reals is nonnegative (mathlib `Real.sInf_nonneg`).
Generality dimensions where the literature varies:
  - value of the zero polynomial: `+∞` (source, algebraic geometry) vs `0` (Lean junk via `sInf ∅`); nonnegativity holds in both
  - weights: ℕ / real `1/r_j`; nonnegative in all cases
Disagreement with the literature: none relevant (junk value differs but the inequality holds either way).

### Generality analysis — `Roth.index_nonneg`

Literature-standard form: `ind(P) ≥ 0` for all `P`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | hypotheses on `P` | none | none (or `P ≠ 0` with `ind 0 = ∞`) | already maximal | holds for all `P` incl. `P = 0` (evidence (3)) |
| 2 | positivity of `r` | not assumed | positive integers | already maximal | `weight_nonneg` needs no positivity (`d j / 0 = 0`) |
| 3 | coefficients `ℝ` | fixed by `Roth.index` | any ring | inherited | parent-level |
| 4 | `[Fintype σ]` | required | not needed | inherited | only through `Roth.weight` (parent) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent `Roth.index` (no hypotheses at all).
Number of weakening opportunities found: 0.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic minimum |
| 3 | construction vs universal property? | no | (parent: monomial valuation) | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | parent-level | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `0 ≤ f.weightedOrder w` | trivial in `ℕ∞`: `zero_le` (evidence (2)) |
| 8 | concrete-via-abstract? | yes, trivially | the proof only uses "inf of a nonnegative set is nonnegative" | that abstract fact is mathlib's `Real.sInf_nonneg` |
| 9 | false-generalisation guard | no | re-aim is the canonical analogue; not a drop-in replacement for the real-valued index | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no new content. The re-aimed statement is `zero_le` in `ℕ∞` and the abstract content is `Real.sInf_nonneg`; both already in mathlib.

### Proof strategy — `Roth.index_nonneg`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (single `Real.sInf_nonneg` application).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_nonneg`

[A] Lean-Finder       not run separately; [C] and [B] already return the exact building block (rate-limit economy)   n/a: redundant with [B]/[C]
[B] Loogle            `Real.sInf_nonneg`   hit: `Real.sInf_nonneg {s : Set ℝ} (hs : ∀ x ∈ s, 0 ≤ x) : 0 ≤ sInf s` (Mathlib.Algebra.Order.Archimedean.Real.Basic)
[C] LeanSearch        "infimum of a set of nonnegative real numbers is nonnegative"   hits: `Real.sInf_nonneg`, `Real.iInf_nonneg`, `Real.sInf_nonpos`, `Real.sSup_nonneg'`
[D] Grep mathlib src  `index_nonneg` (no hits); `weightedOrder` in Mathlib/RingTheory/MvPowerSeries/Order.lean (ℕ∞-valued, so nonnegativity is `zero_le`)
[E] Name pattern      `lean_local_search` not used (ripgrep unavailable in this environment per sibling reports); replaced by grep [D] and compiling the names in the evidence file

Searched for both the user's form (real-valued sInf index ≥ 0) and the literature-standard form (weighted order / monomial valuation ≥ 0).

Concluded: found building blocks (`Real.sInf_nonneg`, `Set.forall_mem_image`) giving the Roth form; the canonical analogue for `MvPowerSeries.weightedOrder` is `zero_le`. `Roth.index` itself is not in mathlib (parent BORDERLINE).

### Normal-form check — `Roth.index_nonneg`

Equivalent formalisms: `0 ≤ index P α r` (current); `index P α r ≥ 0`.
Mathlib canonical form: `0 ≤ _` (`foo_nonneg` convention). OK.
RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.index_nonneg`

Alternative restatements attempted:
- implicit arguments `{P α r}`
- `@[positivity]` extension instead of a lemma
Chosen restatement: current (explicit arguments).
Justification: call sites use `index_nonneg _ _ _` and `index_nonneg P α r` with explicit terms; a positivity extension would be overkill for 3 uses.

### Superfluous-argument audit — `Roth.index_nonneg`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `P`, `α`, `r` | yes | they determine the index; no hypotheses on them |
| 2 | `[Fintype σ]` | via `Roth.weight` only | parent-level |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as project API)

### Call sites — `Roth.index_nonneg`

Internal use count: 2 outside the declaring file (1 more inside Roth/Index.lean)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:100 | `refine ⟨fun h ↦ ?_, fun h ↦ (index_nonneg P α r).antisymm' ?_⟩` (`index_eq_zero_iff`) |
| Roth/Theta.lean:110 | `exact index_nonneg _ _ _` (`Θ_nonneg`) |
| Roth/Theta.lean:395 | `exact max_le (add_nonneg (index_nonneg _ _ _) ((weight_nonneg _ _).trans h2)) ...` |

Inline-derivation grep: (none); no other site applies `Real.sInf_nonneg` to the index set.

### Composition check (Phase 6)

Can `Roth.index_nonneg` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.sInf_nonneg (by rintro _ ⟨d, -, rfl⟩; exact weight_nonneg r d)`
  - Mathlib decls used: `Real.sInf_nonneg`; plus project `Roth.weight_nonneg`
  - Result: succeeds (evidence (1), compiled)

Attempt 2 (re-aim at the canonical object): `0 ≤ f.weightedOrder w` is `zero_le`
  - Result: succeeds (evidence (2), compiled)

Conclusion: COMPOSABLE.

## Verdict: `Roth.index_nonneg`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): nonnegativity is immediate from the definition as a min of nonnegative weights; stated only in passing (clean.tex l.559).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (no hypotheses).
- Mathlib search (Phase 5): building block `Real.sInf_nonneg`; canonical analogue `zero_le` for `ℕ∞`-valued `MvPowerSeries.weightedOrder`.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

The lemma is `Real.sInf_nonneg` applied to the set `weight r '' supp(P(X+α))`, all of whose members are nonnegative by the project's `weight_nonneg`. Mathematically there is nothing for mathlib: the abstract fact is already `Real.sInf_nonneg`, and for mathlib's canonical weighted order the statement is trivial (`zero_le` in `ℕ∞`). Its upstream fate is tied to the parent `Roth.index` (BORDERLINE); it would never be shipped on its own.

It should still not be inlined: it is basic API of a project definition, used in two files, and inlining would expose the `sInf` definition of the index in `Theta.lean`. Junk verdict KEEP.

Belongs-elsewhere check: keep in Roth/Index.lean as API of `Roth.index`.
Mathlib building blocks: `Real.sInf_nonneg` (Mathlib/Algebra/Order/Archimedean/Real/Basic.lean), `Set.forall_mem_image`; canonical analogue `zero_le` for `MvPowerSeries.weightedOrder` (Mathlib/RingTheory/MvPowerSeries/Order.lean).
Composition sketch:
```lean
example (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : 0 ≤ index P α r :=
  Real.sInf_nonneg (by rintro _ ⟨d, -, rfl⟩; exact weight_nonneg r d)
```
Call sites in our project: 3 (Roth/Index.lean:100; Roth/Theta.lean:110, 395).
Refactor plan: none. The 3 sites keep calling `index_nonneg`; inlining is not recommended because the lemma is the def's interface. If `Roth.index` is rebased on `weightedOrder (taylor α P)` (parent question 3), reprove it by `positivity`/`div_nonneg` on the scaled `ℕ∞ → ℝ` value; call sites unchanged.
Next action: no upstreaming; keep as is.

---

## Next step

No upstreaming; keep `Roth.index_nonneg` as local API of `Roth.index`.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_nonneg/compose.lean` (imports `Roth.Index`), compiled clean with `lake env lean` (rc 0, after fixing `zero_le _` to `zero_le` on the first attempt): (1) composition via `Real.sInf_nonneg` + `weight_nonneg`; (2) `0 ≤ f.weightedOrder w` by `zero_le`; (3) `index 0 α r = 0` by `simp [index]`, showing the junk case.
- WebSearch ×3 (queries in the literature table); Loogle `Real.sInf_nonneg`; LeanSearch query as recorded; grep of mathlib for `index_nonneg` (none) and `weightedOrder`; grep of clean.tex (l.545, 559).
- `ask_chatgpt_math` MCP not configured in this session; Lean-Finder skipped as redundant with Loogle/LeanSearch exact hits.
