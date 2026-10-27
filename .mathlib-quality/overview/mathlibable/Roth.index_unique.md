---
decl: Roth.index_unique
file: Roth/Index.lean
line: 234
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: The one-variable identity ind(P; α; r) = rootMultiplicity_α(P) / r, about the project-only def Roth.index, is mathlib's Polynomial.rootMultiplicity_eq_natTrailingDegree (multiplicity = trailing degree of p(X+α)) plus the project's index API (index_le_weight, le_index_iff) and the uniqueAlgEquiv/hasseDeriv bridge; hP is superfluous (compiled), and nothing goes upstream.
action: Keep in Roth/Index.lean for its single caller Roth/Theta.lean:242 (index_unique_le_log_div); optionally drop the superfluous hP (proof in evidence/Roth.index_unique/hyps.lean), which removes the map_ne_zero_iff argument at Theta.lean:242; do not upstream.
---

# Roth.index_unique

## Inventory entry

### `theorem Roth.index_unique`
- **Type**: `{σ : Type*} [Fintype σ] [Unique σ] {P : MvPolynomial σ ℝ} (hP : P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : index P α r = (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default`
- **What**: In one variable, the index of a nonzero polynomial `P` at `α` with weight `r` equals the multiplicity of `α` as a root of `P`, divided by `r`.
- **How**: Sets `q = Polynomial.taylor (α default) (uniqueAlgEquiv ℝ σ P)`. A `key` step identifies `eval α (hasseDeriv d P)` with `q.coeff (d default)` via `Polynomial.taylor_coeff`, the project `MvPolynomial.uniqueAlgEquiv_hasseDeriv`, `Finsupp.unique_single` and `MvPolynomial.eval₂_uniqueAlgEquiv`. It rewrites with mathlib's `Polynomial.rootMultiplicity_eq_natTrailingDegree` and `Polynomial.taylor_apply`. It then proves `le_antisymm`: `≤` from `index_le_weight` at `single default q.natTrailingDegree` (using `Polynomial.trailingCoeff_nonzero_iff_nonzero`), and `≥` from `le_index_iff` together with `Polynomial.natTrailingDegree_le_of_ne_zero`.
- **Hypotheses**: `hP : P ≠ 0`. It is superfluous: both sides are `0` at `P = 0` (evidence (1)). No positivity of `r` is assumed.
- **Uses from project**: `Roth.index`, `Roth.index_le_weight`, `Roth.le_index_iff`, `Roth.weight` (via `simpa [weight]`), `MvPolynomial.hasseDeriv`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv` (Roth/HasseDeriv.lean:266).
- **Used by**: Roth/Theta.lean:242 (`index_unique_le_log_div`, private, which feeds `Θ_unique_le` = source Lemma 5). The reports for `index_le_card` and `index_sub_weight_le_index_hasseDeriv` also use it in their evidence counterexamples.
- **Visibility**: public
- **Lines**: 231–251, proof length 15 lines
- **Notes**: Listed in the module docstring's main results ("the index ... in one variable"). The source is clean.tex §5, proof of Lemma 5: "Taylor's theorem gives ind(R; h_1/q_1; r_1) = t/r_1".

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Theta.lean:242, on the path to Lemma 5 (`Θ_unique_le`).
- Wrapper of 1–2 mathlib calls? No. It is a 15-line bridge between a project def and mathlib's `rootMultiplicity`, and it goes through the multivariate–univariate equivalence `uniqueAlgEquiv`.
- Does mathlib have it? No. `Roth.index` is project-only. Mathlib has the univariate fact `rootMultiplicity_eq_natTrailingDegree` (multiplicity = trailing degree of `p(X + t)`), which is the content.
- Too specific (inline?)? Inlining at the single call site is possible, but it would put a 15-line multivariate/univariate bridge into the Theta Lemma 5 proof. As a named lemma it matches the source's "identify the one-variable index with t/r_1" step (clean.tex Lean note, l.695–697).
- Well-chosen? Yes. The `Unique σ` + `uniqueAlgEquiv` formulation matches how Theta.lean states Lemma 5.
- Conclusion: `KEEP`. Optional action: drop the superfluous `hP`.

## Mathlibable assessment (Step 9)

Pre-filter: the lemma is public, its name does not end in `_aux`, its docstring is not internal or auxiliary, and Step 8 said KEEP. It is not in mathlib: there is no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`, and `index_unique` has no hits there. It is not a glue lemma (the proof is a 15-line `le_antisymm` argument). The parent `Roth.index` is BORDERLINE-needs-human, not NO-mathlib-has-it, so the re-aim rule does not apply. The canonical analogue (root multiplicity as an order of vanishing) is still checked in Phases 4c and 6. Full run.

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; an evidence file importing `Roth.Index` compiles with no output)
- decl `Roth.index_unique`:  ✓ resolved at Roth/Index.lean:234
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to integer weights, and its API (Roth §4)

### Statement (Phase 1)

`Roth.index_unique` is a theorem stating the following. Let `P ∈ ℝ[x]` be a nonzero polynomial in one variable, `α ∈ ℝ` and `r ∈ ℕ`. Let `t` be the multiplicity of `α` as a root of `P`. Then the index of `P` at `α` relative to `r` is `t / r`. Equivalently: the least `k` with `(Δ_k P)(α) ≠ 0` is the root multiplicity, so the minimum over the support of `P(x + α)` of `k / r` is `t / r`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ] [Unique σ]`: a one-element variable set
- `P : MvPolynomial σ ℝ`: the polynomial, transported to `Polynomial ℝ` by `uniqueAlgEquiv ℝ σ`
- `α : σ → ℝ`, `r : σ → ℕ`: the point and the weight, read at `default`

Hypotheses (Lean side):
- `hP : P ≠ 0` (superfluous, evidence (1))

Conclusion (math): `ind(P; α; r) = mult_α(P) / r`.

Conclusion (Lean): `index P α r = (Polynomial.rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a bridge lemma that specialises the project def `Roth.index` to one variable. It is not a named theorem of the paper; it is one step inside the proof of Lemma 5.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 15 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | index of a polynomial one variable equals multiplicity of root divided by r Roth's theorem | partial | index = min of `∑ j_h/r_h` over nonvanishing derivatives (arXiv math/0307203, 2502.00731); Natarajan–Thangadurai, *Pillars of Transcendental Number Theory* ch. 6 | the one-variable case `t/r` is used tacitly (the base case of Roth's lemma), not stated as a lemma |
| 2 | WebSearch (general form) | multiplicity of root equals order of vanishing lowest degree term of Taylor expansion p(x+a) Hasse derivatives | yes | multiplicity at `p` = least `m` with a nonzero Hasse derivative of order `m` at `p` = lowest degree in `P(x+p)` (arXiv 1310.6482, 1402.0643) | the general fact is standard textbook material |
| 3 | WebSearch (aliases) | "order of vanishing" polynomial at a point "multiplicity" Hasse derivative vanish nlab OR stacks OR mathoverflow | yes (arXiv only) | the same criterion: `P` vanishes to order ≥ m iff Hasse derivatives of order < m vanish (arXiv 1310.6482, 1505.07547) | no nLab/Stacks/MO pages returned |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among the available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "multiplicity" | yes | clean.tex l.679–680 ("Let t be the multiplicity of h_1/q_1 as a root of R; Taylor's theorem gives ind(R; h_1/q_1; r_1) = t/r_1"); Lean note l.695–697 | the lemma is exactly this step |
| 6 | nLab | order of a zero / multiplicity of a root | partial | nLab treats multiplicity of roots only informally | nothing at this granularity |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing | partial | `ord_Z` along a prime divisor (valuation of the DVR) | for a point on the affine line, this is the root multiplicity; there is no index notion |
| 9 | MathOverflow / Math.SE | covered by query #3 | no | — | folklore; nothing stand-alone |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), from #1 | yes | the index definition and the one-variable base case of Roth's lemma | the identity is implicit |

### Literature summary (Phase 3)

Concept identified as: in one variable, the (weighted) order of vanishing at `α` is the root multiplicity at `α`, scaled by `1/r`. The general fact is "root multiplicity = order of the lowest nonzero term of the Taylor expansion at `α`".
Sources agree on the standard form: yes. Multiplicity = least order of a nonvanishing Hasse derivative = trailing degree of `P(x + α)`.
Most general standard form: for any commutative ring `R`, `p ∈ R[X]` and `t ∈ R`, `mult_t(p) = natTrailingDegree(p(X + t))`. This is in mathlib as `Polynomial.rootMultiplicity_eq_natTrailingDegree`.
Generality dimensions where the literature varies:
  - coefficient ring: ℝ (Roth) vs any commutative ring (mathlib)
  - normalisation: divided by `r` (Roth index) vs unscaled order (algebra)
Disagreement with the literature: none. The literature's index of `0` is `+∞`. The project's junk value is `0`, and that happens to agree with `rootMultiplicity t 0 = 0`, which is why `hP` can be dropped.

### Generality analysis — `Roth.index_unique`

Literature-standard form: `mult_t(p) = ord(p(X + t))`, unscaled, over any commutative ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hP : P ≠ 0` | nonzero | not needed | yes, verified | with `index 0 = 0` and `rootMultiplicity_zero`, both sides are `0` (evidence (1), compiled) |
| 2 | coefficients `ℝ` | fixed by `Roth.index` | any commutative ring | inherited | `Roth.index` is ℝ-only (parent report) |
| 3 | positivity of `r` | not assumed | — | already maximal | `r default = 0` makes both sides `0` (evidence (3), compiled) |
| 4 | `[Unique σ]` | one variable | — | essential | this is the content of the lemma |
| 5 | `[Fintype σ]` | required | implied by `Unique` | inherited | it comes from `Roth.index`/`weight`, which take `[Fintype σ]` as a section variable, not derived from `Unique` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent def, except for the superfluous `hP`, whose drop is verified (evidence (1)). Dropping it is a local cleanup about a project def, not a mathlib generalisation.
Number of weakening opportunities found: 1 (`hP`, verified by compilation).
Proposed restatement (local): `theorem index_unique [Unique σ] (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : index P α r = (rootMultiplicity (α default) (uniqueAlgEquiv ℝ σ P) : ℝ) / r default`
Cost of restatement: CHEAP (add `rcases eq_or_ne P 0 with rfl | hP; · simp [index]`, and remove the `map_ne_zero_iff` argument at Theta.lean:242).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | `[Unique σ]` is already a typeclass | — |
| 2 | sequences to filters? | no | finite algebraic identity | — |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | inherited | the multiplicity side is general in mathlib; the index side is ℝ-only | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | the canonical content is `rootMultiplicity t p = natTrailingDegree (taylor t p)` | already mathlib (`rootMultiplicity_eq_natTrailingDegree`; evidence (2)) |
| 8 | concrete-via-abstract? | yes, trivially | after `rw [rootMultiplicity_eq_natTrailingDegree]` the proof only uses "the index is the minimum of the support weights" | that abstract content is the project API (`index_le_weight`, `le_index_iff`) plus mathlib trailing-degree lemmas |
| 9 | false-generalisation guard | n/a | no generalisation is proposed beyond the local `hP` drop, which keeps the same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no. The canonical statement is already in mathlib (`Polynomial.rootMultiplicity_eq_natTrailingDegree`). This lemma only relates it to the project's index.

### Proof strategy — `Roth.index_unique`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partial | a project bridge `uniqueAlgEquiv (taylor α P) = Polynomial.taylor (α default) (uniqueAlgEquiv P)` (compiled as evidence in the `MvPolynomial.taylor` report) would replace the `key` step through Hasse derivatives | CHEAP (optional) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (two-sided bound via the index API plus `rootMultiplicity_eq_natTrailingDegree`). An optional golf would route the `key` step through a `uniqueAlgEquiv_taylor` bridge (see the `MvPolynomial.taylor` report). That is not required.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "multiplicity of a root of a polynomial is the least n such that the n-th Hasse derivative does not vanish at the root"   hits: `Polynomial.lt_rootMultiplicity_iff_isRoot_iterate_derivative` (char 0, iterated derivatives), `rootMultiplicity_eq_nat_find_of_nonzero`, `lt_rootMultiplicity_iff_isRoot_iterate_derivative_of_mem_nonZeroDivisors(')`
[B] Loogle            `Polynomial.rootMultiplicity, Polynomial.hasseDeriv`   no hits (mathlib has no Hasse-derivative characterisation of multiplicity)
[C] LeanSearch        "root multiplicity equals trailing degree of the polynomial composed with X + C t"   hits: `Polynomial.rootMultiplicity_eq_natTrailingDegree` (RingDivision.lean:133), `rootMultiplicity_eq_rootMultiplicity`, `rootMultiplicity_eq_natTrailingDegree'`, `eval_divByMonic_eq_trailingCoeff_comp`
[D] Grep mathlib src  `index_unique` (no hit); `namespace Roth` (no hit); `rootMultiplicity_eq_natTrailingDegree` (Algebra/Polynomial/RingDivision.lean:133); `rootMultiplicity_zero` (Algebra/Polynomial/Div.lean:524); `natTrailingDegree`/`trailingDegree` in RingTheory/PowerSeries (no bridge to `PowerSeries.order`)
[E] Name pattern      `lean_local_search` not used; grep [D] used instead, as in the sibling reports

Searched for both: the project form (index in one variable) and the literature-standard form (multiplicity = order of vanishing of the Taylor translate).

Concluded: building blocks found (`Polynomial.rootMultiplicity_eq_natTrailingDegree`, `Polynomial.taylor_apply`, `Polynomial.taylor_coeff`, `Polynomial.trailingCoeff_nonzero_iff_nonzero`, `Polynomial.natTrailingDegree_le_of_ne_zero`, `MvPolynomial.eval₂_uniqueAlgEquiv`). The literature-standard form is in mathlib as `Polynomial.rootMultiplicity_eq_natTrailingDegree`. `Roth.index` itself is not in mathlib.

### Normal-form check

Equivalent formalisms: `index P α r = mult / r`; `index P α r * r = mult` (needs `r ≠ 0`); `index P α r = natTrailingDegree (taylor …) / r`. The chosen form uses mathlib's canonical `rootMultiplicity` on the RHS, which is what the caller needs (Theta.lean:242 then rewrites `rootMultiplicity` across a field extension). RHS convention respected: yes, the canonical object is on the right.

### Syntactic generality

Alternatives: a `Polynomial`-input version (`index (uniqueAlgEquiv.symm p) α r = …`); the multiplication form; a trailing-degree RHS. Chosen: the current form. The caller holds an `MvPolynomial σ ℤ` mapped to ℝ, so the `MvPolynomial` input with `uniqueAlgEquiv` on the right is the easiest shape to apply.

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hP : P ≠ 0` | no | conclusion holds at `P = 0` (evidence (1)) |
| 2 | `[Unique σ]` | yes | the statement only makes sense in one variable |
| 3 | `[Fintype σ]` | yes (inherited) | required by `Roth.index` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (`hP`)
Overall: SHIP-AS-STATED locally, with an optional `hP` drop (no upstreaming)

### Call sites

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern |
|---|---|
| Roth/Theta.lean:242 | `rw [index_unique ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR), hmapeq, hmult]` (`index_unique_le_log_div`) |

Inline-derivation grep: none. `grep -rn rootMultiplicity Roth/` finds only this lemma and the Theta Lemma 5 helpers (`exists_eq_pow_mul_of_rootMultiplicity`, `pow_rootMultiplicity_le`, `index_unique_le_log_div`), and none of these re-derives the index identity.

### Composition check (Phase 6)

Can `Roth.index_unique` be derived from mathlib in ≤3 chained calls?

Attempt 1 (current proof): `rw [rootMultiplicity_eq_natTrailingDegree, ← taylor_apply]`, then `le_antisymm` of `index_le_weight` (at `single default natTrailingDegree`) and `le_index_iff` (with `natTrailingDegree_le_of_ne_zero`), after a `key` coefficient bridge.
  - Decls used: mathlib `Polynomial.rootMultiplicity_eq_natTrailingDegree`, `Polynomial.taylor_apply`, `Polynomial.taylor_coeff`, `Polynomial.trailingCoeff_nonzero_iff_nonzero`, `Polynomial.natTrailingDegree_le_of_ne_zero`, `MvPolynomial.eval₂_uniqueAlgEquiv`; project `index_le_weight`, `le_index_iff`, `uniqueAlgEquiv_hasseDeriv`
  - Result: succeeds (it is the current proof)
  - Notes: the mathematical content is one mathlib lemma (`rootMultiplicity_eq_natTrailingDegree`, evidence (2)) plus the index's two-sided characterisation (min of the support weights). The rest is transport across `uniqueAlgEquiv`.

Conclusion: COMPOSABLE. The new mathematical content is mathlib's `rootMultiplicity_eq_natTrailingDegree`; the remainder is the project's index API and the one-variable transport. This is the sense in which the sibling reports (`index_le_card`, `le_index_iff`) use the bucket.

## Verdict: `Roth.index_unique`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the identity is the source's "Taylor's theorem gives ind = t/r_1" (clean.tex l.679–680). The general fact (multiplicity = lowest order of the Taylor translate) is standard.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for the parent def, except that `hP` is superfluous (compiled, evidence (1)).
- Mathlib search (Phase 5): the canonical form is `Polynomial.rootMultiplicity_eq_natTrailingDegree`. There is no `Roth.index`.
- Composition check (Phase 6): COMPOSABLE (mathlib lemma + project index API + `uniqueAlgEquiv` transport).

**Rationale:**

The statement is about the project-only, ℝ-valued `Roth.index` (whose own report is BORDERLINE), so it has no mathlib home as stated. Its mathematical content is "root multiplicity = trailing degree of `p(X + α)`", which mathlib already has as `Polynomial.rootMultiplicity_eq_natTrailingDegree`. The index of a one-variable polynomial is by definition the minimal support weight of that translate, scaled by `1/r`. If an upstream `MvPolynomial` weighted order at a point were ever added (parent question), the natural mathlib lemma would be "in one variable it equals `rootMultiplicity`", stated against that new def, not this ℝ-valued scaled form.

Locally the lemma earns its name. It is the source's identification step for Lemma 5, and inlining it would put a 15-line multivariate/univariate transport into Theta's Lemma 5 helper. `hP` is superfluous because the junk value `index 0 = 0` agrees with `rootMultiplicity t 0 = 0` (evidence (1)).

WHY not: it adds no mathematics mathlib lacks. Its content is `rootMultiplicity_eq_natTrailingDegree` transported to a project def.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean, next to the rest of the index API that the Lemma 5 proof in Theta.lean relies on.
Mathlib building blocks: `Polynomial.rootMultiplicity_eq_natTrailingDegree` (Mathlib/Algebra/Polynomial/RingDivision.lean:133), `Polynomial.rootMultiplicity_zero` (Mathlib/Algebra/Polynomial/Div.lean:524), `Polynomial.taylor_apply`, `Polynomial.taylor_coeff`, `Polynomial.trailingCoeff_nonzero_iff_nonzero`, `Polynomial.natTrailingDegree_le_of_ne_zero`, `MvPolynomial.eval₂_uniqueAlgEquiv`. Project: `Roth.index_le_weight`, `Roth.le_index_iff`, `MvPolynomial.uniqueAlgEquiv_hasseDeriv`.
Composition sketch (≤3 lines, content only):
```lean
  rw [Polynomial.rootMultiplicity_eq_natTrailingDegree, ← Polynomial.taylor_apply]
  exact le_antisymm (index_le_weight (d := single default q.natTrailingDegree) …)
    ((le_index_iff hP).2 fun d hd ↦ … natTrailingDegree_le_of_ne_zero …)
```
Call sites in our project (from Phase 6.0): 1 (Roth/Theta.lean:242).
Refactor plan: do not delete or inline, since inlining would move the transport proof into `index_unique_le_log_div`. Optional local cleanup: drop `hP` by proving the `P = 0` case with `rcases eq_or_ne P 0 with rfl | hP; · simp [index]`. Then at Theta.lean:242 replace `index_unique ((map_ne_zero_iff _ (map_injective _ Int.cast_injective)).2 hR)` by `index_unique _` (or `index_unique (P := _)`). `hR` is still used at Theta.lean:246, so its binder stays.
Next action: keep locally; optionally drop `hP`; do not upstream.

## Next step

Keep `Roth.index_unique` in Roth/Index.lean and do not upstream it. Optionally drop the superfluous `hP` (proof in `.mathlib-quality/overview/evidence/Roth.index_unique/hyps.lean`) and simplify the argument at Roth/Theta.lean:242.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_unique/hyps.lean` (imports `Roth.Index`) compiled clean with `lake env lean` (no output, about 30 s). It contains:
  - (1) `index_unique_noHP`: the lemma without `hP`, with the `P = 0` case closed by `simp [index]`;
  - (2) the mathlib building block `rootMultiplicity t p = natTrailingDegree (Polynomial.taylor t p)` via `rootMultiplicity_eq_natTrailingDegree` + `taylor_apply`;
  - (3) `r = 0` needs no positivity: the index is `0` (via the `hP`-free lemma and `simp`).
- WebSearch ×3 (queries in the literature table). Sources: arXiv math/0307203, 2502.00731, 1310.6482, 1402.0643, 1505.07547, and the Natarajan–Thangadurai chapter (ideas.repec.org).
- LeanSearch, Loogle (`Polynomial.rootMultiplicity, Polynomial.hasseDeriv`: no hits) and Lean-Finder queries, as recorded in Phase 5.
- Greps: mathlib for `namespace Roth`, `index_unique`, `rootMultiplicity_eq_natTrailingDegree`, `rootMultiplicity_zero`, and trailing degree in PowerSeries; project for `index_unique` and `rootMultiplicity`; clean.tex for "multiplicity" (l.679, 696).
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
