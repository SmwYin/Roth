---
decl: Roth.index_sub_weight_le_index_hasseDeriv
file: Roth/Index.lean
line: 109
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Differentiating by Delta_k lowers the index by at most weight r k is a 3-line consequence of the attained minimum (exists_weight_eq_index), the Hasse composition rule hasseDeriv_hasseDeriv and index_le_weight (direct sInf proof compiled); the canonical re-aimed form weightedOrder(taylor P) le weightedOrder(taylor Delta_k P) + weight k composes from MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder and weightedOrder_le over any comm semiring with no hypothesis (compiled); hk necessary (compiled counterexample).
action: Keep locally as the source lemma lem:index-of-derivative (callers Roth/MainLemma.lean:494, Roth/Theta.lean:390); do not upstream on its own; if MvPolynomial.hasseDeriv and a weighted order at a point are upstreamed (see Roth.index and MvPolynomial.hasseDeriv_hasseDeriv reports), ship the ENat weightedOrder form of evidence (2) alongside them.
---

# Roth.index_sub_weight_le_index_hasseDeriv

## Inventory entry

### `theorem Roth.index_sub_weight_le_index_hasseDeriv`
- **Type**: `{σ : Type*} [Fintype σ] {P : MvPolynomial σ ℝ} {k : σ →₀ ℕ} (hk : hasseDeriv k P ≠ 0) (α : σ → ℝ) (r : σ → ℕ) : index P α r - weight r k ≤ index (hasseDeriv k P) α r`
- **What**: If `Δ_k P ≠ 0`, then `ind(Δ_k P; α; r) ≥ ind(P; α; r) − ∑_j k_j / r_j`: a Hasse derivative of order `k` lowers the index by at most the weight of `k`.
- **How**: Take `i` attaining the index of `Δ_k P` (`exists_weight_eq_index hk`). By `MvPolynomial.hasseDeriv_hasseDeriv`, `Δ_i Δ_k P = binom(i+k, i) · Δ_{i+k} P`, so (via `smul_eq_C_mul`, `eval_C`, `mul_ne_zero_iff`) `(Δ_{i+k} P)(α) ≠ 0`. Then `index_le_weight` gives `ind P ≤ weight r (i+k) = weight r i + weight r k` (`weight_add`), and `sub_le_iff_le_add` concludes.
- **Hypotheses**: `hk : hasseDeriv k P ≠ 0` (necessary: without it the junk value `index 0 = 0` breaks the inequality, evidence (3)); no positivity on `r` needed.
- **Uses from project**: `Roth.index`, `Roth.weight`, `Roth.exists_weight_eq_index`, `Roth.index_le_weight`, `Roth.weight_add` (Roth/Box.lean), `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv` (Roth/HasseDeriv.lean:175)
- **Used by**: Roth/MainLemma.lean:494 (index bound for the derivative `hasseDeriv k P` in the main-lemma construction); Roth/Theta.lean:390 (`hterm`, index of `E μ ν` in the Theta argument); listed in the module docstring of Roth/Index.lean:35.
- **Visibility**: public
- **Lines**: 107–114, proof length 3 lines
- **Notes**: Lean form of the source's Lemma `lem:index-of-derivative` (clean.tex l.571–588), with the same proof as the source ("choose a multi-index i attaining the index of Δ_k P; the Hasse composition identity …").

## Junk check (Step 8)
- Used anywhere? Yes, 2 call sites in 2 files (MainLemma.lean:494, Theta.lean:390).
- Wrapper of 1–2 mathlib calls? No; it chains two project index lemmas with the project Hasse composition rule (not in mathlib).
- Does mathlib have it? No. Mathlib has the univariate analogue `Polynomial.rootMultiplicity_sub_one_le_derivative_rootMultiplicity_of_ne_zero` (ordinary derivative, order 1, same nonvanishing hypothesis), and no Hasse-derivative or weighted-order version.
- Too specific (inline?)? No: a named lemma of the source paper with two consumers in different files.
- Well-chosen? Yes; the statement matches the source exactly, and `sub ≤` is the shape the callers consume (`sub_le_iff_le_add`, `sub_lt_sub_left … |>.trans_le`).
- Conclusion: `KEEP`. Action: none locally.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal or auxiliary, Step 8 KEEP. The qualified name is not in mathlib (no `namespace Roth` under `Mathlib/`; grep for `index_sub_weight`/`index_hasseDeriv` in Mathlib: no hits). Not a glue lemma (3-line argument using the composition rule), so a full run. Parent `Roth.index` is BORDERLINE-needs-human, so the re-aim rule does not force a re-aim; the canonical `weightedOrder` analogue is checked anyway (Phase 4c row 7, Phase 6 attempt 2).

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles clean)
- decl `Roth.index_sub_weight_le_index_hasseDeriv`: ✓ resolved at Roth/Index.lean:109
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights and its basic API (Roth §4)

### Statement (Phase 1)

`Roth.index_sub_weight_le_index_hasseDeriv` is a theorem stating the following. Let `P ∈ ℝ[x_j : j ∈ σ]`, `k ∈ ℕ^σ` with `Δ_k P ≠ 0` (Hasse derivative), `α ∈ ℝ^σ`, `r ∈ ℕ^σ`. Then

  `ind(Δ_k P; α; r) ≥ ind(P; α; r) − ∑_j k_j / r_j`.

Equivalently: the weighted order of vanishing at `α` drops by at most the weight of the differential operator `Δ_k`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: finite variable set (needed by `Roth.weight`)
- `P`, `k`, `α`, `r`: polynomial, derivative multi-index, point, weights

Hypotheses (Lean side):
- `hk : hasseDeriv k P ≠ 0`: excludes the junk value `index 0 = 0` on the right

Conclusion (math): differentiation by `Δ_k` lowers the index by at most `∑ k_j/r_j`.

Conclusion (Lean): `index P α r - weight r k ≤ index (hasseDeriv k P) α r`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under Main results of the file, but it is a basic property of the project def `Roth.index` (a 3-line lemma), not a result of independent weight.

### One-line check (Phase 2b)

Body line count: 3 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | Roth theorem index of polynomial derivative "index" decreases by at most i_1/r_1 + ... + i_m/r_m | yes | index of the derived polynomial is at least θ − ∑ k_i/r_i (arXiv math/0307203; index def in arXiv 2502.00731, Lemma 2.22 "properties of index under differentiation") | exactly our statement, standard basic property of the index |
| 2 | WebSearch (general form) | order of vanishing of derivative at a point drops by at most order of differential operator multiplicity | partial | an order-m operator lowers the vanishing order by at most m (arXiv 2503.11042; Binyamini–Novikov multiplicity operators arXiv 1309.1868) | unweighted general form; folklore |
| 3 | WebSearch (aliases) | Hasse derivative multiplicity of zero lemma mult(D^(i) f, a) >= mult(f,a) - abs(i) polynomial method | yes | `mult(P^(i), a) ≥ mult(P, a) − abs(i)` (Dvir–Kopparty–Saraf–Sudan method of multiplicities, arXiv 0901.2529, 1003.3736 Lemma 12, 2403.19824) | the unweighted Hasse-derivative form, standard in the polynomial method |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "index-of-derivative" | yes | clean.tex l.571–588: Lemma `lem:index-of-derivative`, hypothesis "Δ_k P not identically zero", proof via the Hasse composition identity | the Lean statement and proof match the source verbatim |
| 6 | nLab | order of vanishing / valuation of a derivative | no | — | no weighted multivariate order; derivative-of-order facts not treated |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing / differential operators | partial | principal parts / differential operators of order ≤ m map `m_x^{n}` into `m_x^{n−m}` | same fact in ideal language, unweighted |
| 9 | MathOverflow / Math.SE | (covered by #2, #3) | no | — | folklore; no stand-alone statement found |
| 10 | recent arXiv (last 5 years) | (#1 hit 2502.00731 (2025); #2 hit 2503.11042 (2025); #3 hit 2403.19824 (2024)) | yes | same forms as above | — |

### Literature summary (Phase 3)

Concept identified as: "differentiation lowers the (weighted) order of vanishing by at most the (weighted) order of the operator"; for Hasse derivatives, `mult(D^(i)P, a) ≥ mult(P, a) − |i|` (method of multiplicities), and in Roth's setting `ind(Δ_k P) ≥ ind(P) − ∑ k_j/r_j`.
Sources agree on the standard form: yes.
Most general standard form: for any commutative (semi)ring `R`, weights `w`, `ord_w(Δ_k f) ≥ ord_w(f) − w(k)` (with `ord 0 = ∞`, no nonvanishing hypothesis), equivalently `ord_w(f) ≤ ord_w(Δ_k f) + w(k)`.
Generality dimensions where the literature varies:
  - weights: unit weights (multiplicity) vs `1/r_j` (Roth index) vs `ℕ` weights
  - coefficients: ℝ (Roth) vs any field / semiring (polynomial method)
  - value at `0`: `+∞` (literature, mathlib) vs project junk `0`, which forces `hk`
Disagreement with the literature: none; `hk` is the source's own hypothesis and stems from the junk convention of the parent.

### Generality analysis — `Roth.index_sub_weight_le_index_hasseDeriv`

Literature-standard form: `ord_w(f) ≤ ord_w(Δ_k f) + w(k)`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hk : hasseDeriv k P ≠ 0` | nonzero derivative | not needed when `ord 0 = ∞` | no (for this def) | fails without it: `P = X 0`, `k = single 1 1`, `r = ![1,2]`, `α = 0` (evidence (3), compiled) |
| 2 | positivity of `r` | not assumed | — | already absent | proof never needs it |
| 3 | coefficients `ℝ` | fixed by `Roth.index` | any comm semiring | inherited | parent def; the re-aimed form holds over any `CommSemiring` (evidence (2)) |
| 4 | `[Fintype σ]` | required | not needed | inherited | via `Roth.weight` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL relative to the parent definition `Roth.index` (`hk` verified necessary, evidence (3)).
Number of weakening opportunities found: 0 at the lemma level.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no structural preamble |
| 2 | sequences to filters? | no | — | finite algebraic statement |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | inherited | only via the parent def; the re-aimed form is over `CommSemiring` | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `(↑(taylor α P)).weightedOrder w ≤ (↑(taylor α (hasseDeriv k P))).weightedOrder w + Finsupp.weight w k` | composes from `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_le` plus `hasseDeriv_hasseDeriv` (evidence (2)); no hypothesis needed |
| 8 | concrete-via-abstract? | no | the proof uses exactly "attained minimum" + "Hasse composition rule"; no hidden abstraction | — |
| 9 | false-generalisation guard | no false generalisation | the `weightedOrder` form is the canonical analogue but not a drop-in for the real-valued index (same caveat as parent) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no project-specific contribution. The re-aimed `ℕ∞` statement is a short composition of existing mathlib `weightedOrder` API with the (not yet upstream) Hasse composition rule; it would be worth shipping only together with an upstream `MvPolynomial.hasseDeriv` and `taylor`.

### Proof strategy — `Roth.index_sub_weight_le_index_hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (upstream-side) | `MvPolynomial.hasseDeriv_hasseDeriv` (assessed YES-but-generalise-first in its own report) | covered by that report |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (it is the source proof, reusing the attained-minimum API; a direct `sInf` proof also compiles, evidence (1)).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder       "weighted order of a multivariate power series after differentiation decreases by at most the weight of the derivative multi-index"   hits: `MvPowerSeries.weightedOrder_le`, `le_weightedOrder`, `nat_le_weightedOrder`, `weightedOrder_eq_nat` (building blocks); no derivative lemma
[B] Loogle            `Polynomial.rootMultiplicity _ (Polynomial.hasseDeriv _ _)` (no hits); `MvPowerSeries.weightedOrder _ _ ≤ MvPowerSeries.weightedOrder _ _ + _` (no hits)
[C] LeanSearch        "root multiplicity of derivative is at least root multiplicity minus one" → `Polynomial.rootMultiplicity_sub_one_le_derivative_rootMultiplicity_of_ne_zero`, `rootMultiplicity_sub_one_le_derivative_rootMultiplicity`, `derivative_rootMultiplicity_of_root` (univariate, order-1 analogues); "order of power series of derivative is at least order minus one" → no order lemma for `PowerSeries.derivative`
[D] Grep mathlib src  `index_sub_weight`, `index_hasseDeriv` (no hits); `rootMultiplicity` with `hasse`/`iterate_derivative` (only Polynomial/FieldDivision.lean: `isRoot_iterate_derivative_of_lt_rootMultiplicity`, `lt_rootMultiplicity_iff_isRoot_iterate_derivative_of_mem_nonZeroDivisors`); `weightedOrder` with derivatives in RingTheory/MvPowerSeries, PowerSeries (no hits)
[E] Name pattern      `lean_local_search` not run separately (grep [D] used, as in sibling reports)

Searched for both: the project form (index of a Hasse derivative) and the literature-standard form (weighted order / multiplicity of a derivative).

Concluded: found building blocks (`Set.Nonempty.csInf_mem`, `csInf_le`, `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_le`) plus the project's `hasseDeriv_hasseDeriv`; univariate partial analogue `Polynomial.rootMultiplicity_sub_one_le_derivative_rootMultiplicity_of_ne_zero` (Mathlib/Algebra/Polynomial/FieldDivision.lean). Not in mathlib in multivariate/Hasse/weighted form.

### Normal-form check

Equivalent formalisms: `index P - weight k ≤ index (Δ_k P)`; `index P ≤ index (Δ_k P) + weight k`. Mathlib's analogue `rootMultiplicity_sub_one_le_derivative_rootMultiplicity_of_ne_zero` uses the `sub ≤` shape, matching ours; for `ℕ∞` orders the `≤ … + …` shape would be canonical (truncated subtraction). RHS convention: n/a (inequality).

### Syntactic generality

Alternatives: the additive `index P α r ≤ index (hasseDeriv k P) α r + weight r k` form. Chosen: existing `sub ≤` form, since both callers consume it directly (MainLemma.lean:494 via `trans_le`; Theta.lean:390 rewrites with `sub_sub`, `sub_right_comm`).

### Superfluous-argument audit

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hk : hasseDeriv k P ≠ 0` | yes | evidence (3) |
| 2 | `[Fintype σ]` | yes (via `Roth.weight`) | inherited |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 2 (outside the declaring file)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern |
|---|---|
| Roth/MainLemma.lean:494 | `(index_sub_weight_le_index_hasseDeriv (fun h0 ↦ hkev (by rw [h0, map_zero])) α r)` closing a `trans_le` chain |
| Roth/Theta.lean:390 | `have h1 := index_sub_weight_le_index_hasseDeriv hE α r` then `rw [weight_add, weight_mapDomain …, weight_single] at h1` |

Inline-derivation grep: none found (no other site re-derives the bound from `exists_weight_eq_index` + `hasseDeriv_hasseDeriv`).

### Composition check (Phase 6)

Can `Roth.index_sub_weight_le_index_hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1 (current proof): `exists_weight_eq_index hk` → rewrite with `hasseDeriv_hasseDeriv`, `smul_eq_C_mul`, `map_mul`, `eval_C`, `mul_ne_zero_iff` → `index_le_weight` + `weight_add` + `sub_le_iff_le_add`.
  - Result: succeeds (3 lines, Roth/Index.lean:112–114).
Attempt 1' (direct, no sibling lemmas): `Set.Nonempty.csInf_mem` on the image for `Δ_k P`, `coeff_taylor`, `hasseDeriv_hasseDeriv`, then `csInf_le` for `P` at `i + k`, `weight_add`, `linarith`.
  - Result: succeeds (evidence (1), compiled).
Attempt 2 (re-aim at the canonical object): `weightedOrder w ↑(taylor α P) ≤ weightedOrder w ↑(taylor α (Δ_k P)) + weight w k` over any `CommSemiring`, no hypothesis, via `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_le`, `hasseDeriv_hasseDeriv`.
  - Result: succeeds (evidence (2), compiled).

Conclusion: COMPOSABLE. Attained minimum + Hasse composition rule + lower bound at `i + k`; the only non-mathlib ingredient is the project's `hasseDeriv_hasseDeriv`, whose upstream fate is decided in its own report.

## Verdict: `Roth.index_sub_weight_le_index_hasseDeriv`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): standard basic property of the index (clean.tex l.571–588; arXiv math/0307203; method-of-multiplicities lemma `mult(D^(i)P) ≥ mult(P) − |i|`).
- Generality analysis (Phase 4): MAXIMALLY GENERAL relative to the parent def; `hk` verified necessary (evidence (3)).
- Mathlib search (Phase 5): building blocks `Set.Nonempty.csInf_mem`, `csInf_le`, `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_le`; univariate analogue `Polynomial.rootMultiplicity_sub_one_le_derivative_rootMultiplicity_of_ne_zero`.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (2)).

**Rationale:**

Mathematically the lemma says: if `i` attains the index of `Δ_k P`, the composition rule `Δ_i Δ_k = binom(i+k,i) Δ_{i+k}` shows `(Δ_{i+k} P)(α) ≠ 0`, so the index of `P` is at most `w(i) + w(k)`. This is the standard "differentiation lowers the order of vanishing by at most the operator order" fact, and the proof is a three-step composition of the attained-minimum property, the Hasse composition rule and the defining lower bound. For mathlib's canonical object, the weighted order of the Taylor expansion, the same inequality composes from `exists_coeff_ne_zero_and_weightedOrder` and `weightedOrder_le` over any commutative semiring without the nonvanishing hypothesis (evidence (2)). Nothing here is a standalone mathlib contribution: its upstream value is entirely carried by `MvPolynomial.hasseDeriv_hasseDeriv` (YES-but-generalise-first) and the parent `Roth.index` (BORDERLINE).

Locally it should stay: it is a verbatim source lemma (`lem:index-of-derivative`) with 2 consumers in 2 files.

Belongs-elsewhere check: keep in Roth/Index.lean as basic API of `Roth.index`.
Mathlib building blocks: `Set.Nonempty.csInf_mem`, `csInf_le` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean), `Set.Finite.image`, `Set.Finite.bddBelow`, `MvPolynomial.mem_support_iff`; for the re-aim `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_le` (Mathlib/RingTheory/MvPowerSeries/Order.lean); project `MvPolynomial.hasseDeriv_hasseDeriv` (Roth/HasseDeriv.lean:175).
Composition sketch (the compiled proof at Roth/Index.lean:112–114):
```lean
  obtain ⟨i, hi, hiw⟩ := exists_weight_eq_index hk α r
  rw [hasseDeriv_hasseDeriv, smul_eq_C_mul, map_mul, eval_C, mul_ne_zero_iff] at hi
  exact sub_le_iff_le_add.2 (by simpa [weight_add, hiw] using index_le_weight (r := r) hi.2)
```
Call sites in our project: 2 (Roth/MainLemma.lean:494, Roth/Theta.lean:390).
Refactor plan: none required; both sites keep calling the lemma (inlining the 3-line composition at 2 sites in different files would duplicate the source lemma). If `Roth.index` is rebased on `weightedOrder (taylor α P)` (parent question), reprove via evidence (2) plus `index_eq_weightedOrder_div`; call sites unchanged.
Next action: no upstreaming; keep as is. If `MvPolynomial.hasseDeriv` is upstreamed, add the `ℕ∞` weighted-order form of evidence (2) next to `hasseDeriv_comp`.

---

## Next step

No upstreaming; keep `Roth.index_sub_weight_le_index_hasseDeriv` as the local source lemma. Optional follow-up tied to the `MvPolynomial.hasseDeriv` upstreaming: the hypothesis-free weighted-order inequality in evidence (2).

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_sub_weight_le_index_hasseDeriv/compose_reaim_necessity.lean` (imports `Roth.Index`) compiles clean with `lake env lean` (no output; four runs total, the first three fixing elaboration details: a missing `eval_smul` name, `Polynomial.C` ascription, the `x :=` argument name). It contains:
  - (1) direct composition via `Set.Nonempty.csInf_mem`, `csInf_le`, `coeff_taylor`, `hasseDeriv_hasseDeriv`, `weight_add` (no sibling attained-minimum lemmas);
  - (2) re-aim: `weightedOrder w ↑(taylor α P) ≤ weightedOrder w ↑(taylor α (hasseDeriv k P)) + Finsupp.weight w k` over any `CommSemiring`, no hypothesis, via `MvPowerSeries.exists_coeff_ne_zero_and_weightedOrder`, `MvPowerSeries.weightedOrder_le`;
  - (3) `hk` necessary: for `σ = Fin 2`, `P = X 0`, `k = single 1 1`, `r = ![1, 2]`, `α = 0`: `Δ_k P = 0`, `index P = 1` (via `index_rename`, `index_unique`, `rootMultiplicity_X_sub_C_self`), `weight r k = 1/2`, so `1 − 1/2 ≤ index 0 = 0` fails.
- WebSearch ×3 (queries in the literature table).
- Loogle ×2 (no hits), LeanSearch ×2, Lean-Finder ×1 as recorded.
- Greps: project for call sites; mathlib for `index_sub_weight`, `index_hasseDeriv`, rootMultiplicity/derivative lemmas, weightedOrder/derivative lemmas; clean.tex for `index-of-derivative`.
- `ask_chatgpt_math` MCP not configured in this session.
