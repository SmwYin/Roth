---
decl: Roth.weight_eq_finsuppWeight_div
file: Roth/Index.lean
line: 130
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Clearing denominators in the rational weight (sum d_j/r_j = (sum d_j (D/r_j))/D with D = prod r_j) is a per-term field identity from Finsupp.weight_eq_sum, Nat.cast_sum/Nat.cast_div_charZero and field_simp (compiled); the re-aimed Finsupp.weight form adds nothing mathlib lacks beyond trivial cast/scaling algebra; hr is necessary (compiled) and D can be any nonzero common multiple (compiled).
action: Keep locally as the bridge used twice by index_eq_weightedOrder_div (Roth/Index.lean:152,155); optionally generalise to weight_eq_finsuppWeight_div_of_dvd (any nonzero common multiple D) and restate via Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) once Roth.weight is redefined; do not upstream.
---

# Roth.weight_eq_finsuppWeight_div

## Inventory entry

### `theorem Roth.weight_eq_finsuppWeight_div`
- **Type**: `{σ : Type*} [Fintype σ] {r : σ → ℕ} (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) : weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i`
- **What**: For positive integers `r_j` and `D = ∏ r_j`, the rational weight `∑ d_j / r_j` of a multi-index equals the natural-number weight `∑ d_j · (D / r_j)` (with the natural weights `w_j = D / r_j`) divided by `D`.
- **How**: `hD : 0 < ∏ (r i : ℝ)` by `Finset.prod_pos`; unfold `weight`, rewrite with `Finsupp.weight_eq_sum`, `Nat.cast_sum`, `Finset.sum_div`, `Nat.cast_prod`; per term (`Finset.sum_congr`) use `Nat.cast_mul`, `Nat.cast_div_charZero` with `Finset.dvd_prod_of_mem`, then `mul_div_assoc`, `div_right_comm`, `mul_div_cancel_right₀`.
- **Hypotheses**: `hr` (all `r j` positive; necessary, evidence (3); only nonvanishing is used).
- **Uses from project**: `Roth.weight`
- **Used by**: Roth/Index.lean:152 and Roth/Index.lean:155 (both inside `Roth.index_eq_weightedOrder_div`); no other file.
- **Visibility**: public
- **Lines**: 127–137, proof length 7 lines
- **Notes**: implements the source's Lean note ("set `D = ∏ r_j` and use the natural weights `w_j = D / r_j`", clean.tex l.549–556).

## Junk check (Step 8)
- Used anywhere? Yes, twice, both in `index_eq_weightedOrder_div` (Index.lean:152,155).
- Wrapper of 1–2 mathlib calls? No: a 7-line rewrite chain (cast of a natural division, sum manipulation, cancellation).
- Does mathlib have it? No. Mathlib's `Finsupp.weight` API (Mathlib/Data/Finsupp/Weight.lean) has `weight_apply`, `weight_eq_sum`, `weight_single`, but no lemma for casting weights or scaling the weight vector.
- Too specific (inline?)? Two uses in one proof, in opposite rewrite directions; inlining would duplicate the computation. Keep.
- Well-chosen? Yes; optionally the product `∏ r_i` could be any nonzero common multiple (evidence (2)), but the only consumer uses the product.
- Conclusion: `KEEP`. Action: none (optional local generalisation, see Next step).

## Mathlibable assessment (Step 9)

Pre-filter: public, not `_aux`, docstring not internal/auxiliary, Step 8 KEEP, qualified name `Roth.weight_eq_finsuppWeight_div` absent from `.lake/packages/mathlib/Mathlib/` (grep for `finsuppWeight` returns nothing). Not a glue lemma (real computation), so full run. Parent `Roth.weight` is `NO-mathlib-has-it` because mathlib has the more general `Finsupp.weight`; per the re-aim rule the statement is re-aimed at `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)` (evidence (4)) and the re-aimed form is assessed below.

### Baseline (Phase 0)
- lake build:               ✓ clean (per brief; evidence file importing `Roth.Index` compiles)
- decl `Roth.weight_eq_finsuppWeight_div`: ✓ resolved at Roth/Index.lean:130
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index of a real multivariate polynomial at a point relative to positive integer weights (Roth §4)

### Statement (Phase 1)

`Roth.weight_eq_finsuppWeight_div` is a theorem stating the following. Let `r_j` (`j ∈ σ`, `σ` finite) be positive integers and `D = ∏_j r_j`. For every multi-index `d ∈ ℕ^σ`,
`∑_j d_j / r_j = (∑_j d_j · (D / r_j)) / D`,
where `D / r_j ∈ ℕ` (exact division). That is, the rational weight vector `(1/r_j)` is `1/D` times the integral weight vector `(D/r_j)`, so weighted degrees scale accordingly.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: variables; `r : σ → ℕ`: weight parameters; `d : σ →₀ ℕ`: multi-index

Hypotheses (Lean side):
- `hr : ∀ j, 0 < r j`: positivity (so that `D ≠ 0` and `r_j ∣ D` gives an exact quotient)

Conclusion (math): rational weight = integral weight / `D`.

Conclusion (Lean): `weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a clearing-denominators bridge between the project's rational weight and mathlib's natural-number `Finsupp.weight`; not a main result, no new structure.

### One-line check (Phase 2b)

Body line count: 7 (tactic proof)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---|---|---|---|---|
| 1 | WebSearch (specific form) | Roth's theorem index polynomial "sum d_j / r_j" weights Lean formalization | partial | index = min of `∑ j_i / r_i` over nonzero Taylor coefficients (arXiv math/0307203, 2502.00731) | rational weights used directly; no clearing-denominators lemma stated |
| 2 | WebSearch (general form) | weighted degree rational weights clear denominators multiply by common denominator integer weights | yes | scaling all weights by a common positive integer (lcm / common denominator) scales every weighted degree by it (MathWorld "Weighted Homogeneous Polynomial": normalized weights `a_i/d`; arXiv 1103.0868, 1812.03195) | standard folklore: rational weights ↔ integral weights up to scaling |
| 3 | WebSearch (aliases) | "weighted degree" "rational weights" equivalent integer weights scaling grading | no | — | results off-topic (educational grading); confirms no named theorem |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not among available tools) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "natural weights", "D=" | yes | clean.tex l.549–556: "set `D=∏_j r_j` and use the natural weights `w_j=D/r_j` in `MvPowerSeries.weightedOrder` ... then divide the finite value by `D`" | our lemma is exactly this conversion |
| 6 | nLab | weighted projective space / grading | partial | weights are positive integers; rational weights normalised by a common factor | only the scaling convention, no lemma |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | graded rings, Veronese / rescaling gradings | partial | rescaling a ℤ-grading by `d` (Veronese) | same scaling idea; no rational-weight statement |
| 9 | MathOverflow / Math.SE | (covered by #2, #3) | no | — | folklore; nothing stated as a result |
| 10 | recent arXiv (last 5 years) | (#1, #2 results: 2502.00731 (2025), 2512.00681 (2025)) | yes | primitive integral weight obtained by clearing denominators / dividing by gcd | same folklore |

### Literature summary (Phase 3)

Concept identified as: clearing denominators of a rational weight vector (rescaling of a grading / weighted degree by a common multiple).
Sources agree on the standard form: yes. For weights `w ∈ ℚ^σ` and a positive common denominator `N`, `deg_w(d) = deg_{N w}(d) / N`.
Most general standard form: linearity of the weighted degree in the weight vector: `deg_{c·w}(d) = c · deg_w(d)`, plus compatibility of the integral weighted degree with the cast `ℕ → ℝ`; `N` any common multiple of the denominators (lcm being canonical), not necessarily the product.
Generality dimensions where the literature varies:
  - choice of `N`: product (project, source) vs lcm / any common multiple (most general); evidence (2) compiles the common-multiple form
  - weight values: rationals `1/r_j` here; in general any weight vector in a module
Disagreement with the literature: none.

### Generality analysis — `Roth.weight_eq_finsuppWeight_div`

Literature-standard form (from Phase 3): `deg_{w}(d) = deg_{N w}(d) / N` for any `N ≠ 0` with `N w` integral; abstractly `Finsupp.weight (c • w) = c • Finsupp.weight w` and `Nat.cast (weight w d) = weight (Nat.cast ∘ w) d`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `D = ∏ r_i` | product | any nonzero common multiple `D` of the `r_j` | yes | evidence (2): `weight_eq_finsuppWeight_div_of_dvd (hD : D ≠ 0) (hr : ∀ j, r j ∣ D)` compiles, and the project statement is its special case |
| 2 | `hr : ∀ j, 0 < r j` | positivity | `r j ≠ 0` | equivalent over `ℕ` | necessary: `r = (0,1)`, `d = single 1 1` gives `1 = 0` (evidence (3)) |
| 3 | `ℝ` codomain | real | any field of characteristic zero (or division semiring with the casts) | yes, inherited | fixed by `Roth.weight : … → ℝ`; not worth changing locally |
| 4 | `[Fintype σ]` | finite variables | needed for `∏ r_i` | no (for the product form) | the common-multiple form only needs finiteness via `Roth.weight` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (the product can be replaced by any nonzero common multiple), verified by evidence (2).
Number of weakening opportunities found: 1 (`D` arbitrary common multiple), compiled.
Proposed restatement (local only):

```lean
theorem weight_eq_finsuppWeight_div_of_dvd {r : σ → ℕ} {D : ℕ} (hD : D ≠ 0) (hr : ∀ j, r j ∣ D)
    (d : σ →₀ ℕ) : weight r d = (Finsupp.weight (fun j ↦ D / r j) d : ℝ) / D
```

Cost of restatement: CHEAP (compiled in evidence (2), 7 lines). This weakening is local polish; it does not create mathlib content (see Phase 6).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | marginal | could be stated in any char-0 field | none; `Roth.weight` is ℝ-valued |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (re-aim) | `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d = (Finsupp.weight (fun j ↦ D / r j) d : ℝ) / D` (evidence (4)); abstractly linearity of `Finsupp.weight` in `w` and cast compatibility | would need `Finsupp.weight_smul`-type and `Nat.cast_weight`-type lemmas, both one-liners from `Finsupp.weight_eq_sum` / linearity of `Finsupp.linearCombination` |
| 8 | concrete-via-abstract? | yes, trivially | proof uses only `r_j ∣ D` and `D ≠ 0`; the product is incidental (evidence (2)) | local generalisation only |
| 9 | false-generalisation guard | no false generalisation | the common-multiple form specialises back to the product form (evidence (2), last `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no mathlib contribution. The re-aimed statement is the parent's `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)` rewritten by a per-term field identity; generic `Finsupp.weight` scaling/cast lemmas would be one-line consequences of `weight_eq_sum` and are not what this declaration is.

### Proof strategy — `Roth.weight_eq_finsuppWeight_div`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | marginal | a `Nat.cast` lemma for `Finsupp.weight` would save `Nat.cast_sum`/`Nat.cast_mul`; `field_simp` replaces the manual cancellation chain (evidence (1)) | CHEAP, cosmetic |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a `simp only` + `field_simp` variant also compiles, evidence (1); neither is materially shorter).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.weight_eq_finsuppWeight_div`

[A] Lean-Finder       "weighted degree of a multi-index with rational weights 1/r_j equals the integer weighted degree with weights D/r_j divided by D"   hits: only `MvPolynomial.weightedTotalDegree*`, `isWeightedHomogeneous_monomial` (unrelated)
[B] Loogle            `Finsupp.weight`   30 hits, all of `weight_apply`, `weight_eq_sum`, `weight_single*`, `le_weight*`, `finite_of_nat_weight_*`, weighted-homogeneous API; no scaling or cast lemma
[C] LeanSearch        "Finsupp.weight cast natural weights to field, weight of scaled weights equals scalar times weight"   hits: `Finsupp.weight_single`, `Finsupp.weight_apply` (no scaling lemma)
[D] Grep mathlib src  `finsuppWeight`, `weight_smul`, `weight_nsmul`, `cast_weight`, `weight_cast`, `map_weight` in Mathlib/: no relevant hits; full theorem list of Mathlib/Data/Finsupp/Weight.lean reviewed
[E] Name pattern      covered by [B]/[D] (Loogle on the constant enumerates every `Finsupp.weight` lemma)

Searched for both: the project form (rational weight = integral weight / D) and the literature-standard form (linearity of the weighted degree in the weight vector, cast compatibility).

Concluded: found building blocks (`Finsupp.weight_eq_sum`, `Nat.cast_sum`, `Nat.cast_mul`, `Nat.cast_div_charZero`, `Finset.dvd_prod_of_mem`, `Finset.sum_div`, `field_simp`); no packaged statement in mathlib.

### Normal-form check — `Roth.weight_eq_finsuppWeight_div`

Equivalent formalisms: (a) `weight r d = (natWeight : ℝ) / D` (chosen); (b) `D * weight r d = natWeight`; (c) after the parent refactor, `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d = …`. Mathlib has no canonical form for this idea. The consumer rewrites in both directions with `weightedOrder(...).toNat / D`, so (a), with the project's `weight` on the LHS, is the right shape. RHS convention: n/a (bridge lemma, not a simp lemma).

### Syntactic generality — `Roth.weight_eq_finsuppWeight_div`

Alternative restatements attempted:
- product `D = ∏ r_i` (current)
- arbitrary nonzero common multiple `D` with `∀ j, r j ∣ D` (evidence (2))
- multiplied-out form `(∏ r_i) * weight r d = natWeight`

Chosen restatement: current (product) for the only consumer; the common-multiple version is easier to reuse but needs two side conditions at the call site.
Justification: `index_eq_weightedOrder_div` is stated with `∏ r_i`, so the product form rewrites directly.

### Superfluous-argument audit — `Roth.weight_eq_finsuppWeight_div`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hr` | yes | counterexample with `r = (0,1)` (evidence (3)) |
| 2 | `[Fintype σ]` | yes | needed for `∏ r_i` and for `Roth.weight` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (optional RESTATE to the common-multiple form, evidence (2))
Superfluous arguments: NONE
Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.weight_eq_finsuppWeight_div`

Internal use count: 0 outside the declaring file (2 inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:152 | `rw [← hdw, ENat.toNat_natCast, ← weight_eq_finsuppWeight_div hr]` (in `index_eq_weightedOrder_div`, upper bound) |
| Roth/Index.lean:155 | `rw [weight_eq_finsuppWeight_div hr]` (in `index_eq_weightedOrder_div`, lower bound) |

Inline-derivation grep (`Nat.cast_div_charZero`, `Finset.dvd_prod_of_mem`, `∏ i, r i) / r j` over Roth/): (none) — no other site re-derives the identity.

### Composition check (Phase 6)

Can `Roth.weight_eq_finsuppWeight_div` be derived from mathlib in ≤3 chained calls?

Attempt 1: `simp only [weight, Finsupp.weight_eq_sum, smul_eq_mul, Nat.cast_sum, Nat.cast_mul, Finset.sum_div, Nat.cast_prod]`, then `Finset.sum_congr` with `Nat.cast_div_charZero (Finset.dvd_prod_of_mem _ _)` and `field_simp`
  - Mathlib decls used: `Finsupp.weight_eq_sum`, `Nat.cast_sum`, `Nat.cast_mul`, `Nat.cast_div_charZero`, `Finset.dvd_prod_of_mem`, `Finset.sum_div`, `Finset.sum_congr`, `field_simp`
  - Result: succeeds (evidence (1), compiled)
  - Notes: a simp-normalisation plus one per-term cast lemma plus `field_simp`: per the 6b heuristics, a "trivial simp composition"; no idea beyond `r_j ∣ D`.

Attempt 2 (re-aim at the parent's mathlib form): `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹) d = (Finsupp.weight (fun j ↦ D / r j) d : ℝ) / D`
  - Result: succeeds (evidence (4)); same algebra, nothing specific to `Roth`.

Conclusion: COMPOSABLE (trivial simp + field_simp composition of mathlib building blocks; no new mathematical content).

## Verdict: `Roth.weight_eq_finsuppWeight_div`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): clearing denominators of rational weights is folklore (scaling a weight vector scales weighted degrees); the source's Lean note (clean.tex l.549–556) prescribes exactly this conversion.
- Generality analysis (Phase 4): STRICTLY NARROWER only in the choice `D = ∏ r_i` (any nonzero common multiple works, evidence (2)); local polish, no mathlib content.
- Mathlib search (Phase 5): building blocks `Finsupp.weight_eq_sum`, `Nat.cast_div_charZero`, `Finset.dvd_prod_of_mem`, `Finset.sum_div`; no packaged statement.
- Composition check (Phase 6): COMPOSABLE (evidence (1), (4)).

**Rationale (1–2 paragraphs):**

The lemma is the per-term identity `d_j / r_j = d_j · (D / r_j) / D` summed over `j`, valid because `r_j ∣ D` and `D ≠ 0`. Everything it needs is already in mathlib (`Finsupp.weight_eq_sum` to expose the sum, `Nat.cast_div_charZero` for the exact natural division, `field_simp` for the cancellation), and the proof is a short simp/field_simp composition (evidence (1)). Re-aimed at the parent's mathlib replacement `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)` (evidence (4)), the statement is "rescaling the weight vector by `D` rescales `Finsupp.weight` by `D`, compatibly with the cast `ℕ → ℝ`": generic one-liners from `weight_eq_sum` / linearity of `Finsupp.linearCombination`, not a meaningful mathlib addition. The specific `D = ∏ r_j` form exists only to feed `MvPowerSeries.weightedOrder`, which needs natural weights, in `index_eq_weightedOrder_div`.

It is a well-placed bridge lemma used twice, in opposite rewrite directions, in a single proof, so it should stay rather than be inlined. Junk verdict KEEP. A cheap local generalisation to an arbitrary nonzero common multiple `D` compiles (evidence (2)) but has no consumer.

WHY not: mathlib has the building blocks; the form is a trivial composition with no new content (see Composition sketch).
Belongs-elsewhere check: keep in Roth/Index.lean next to `index_eq_weightedOrder_div`; after the parent refactor (`Roth.weight := Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`) the proof starts from the parent's bridge `weight_eq_sum` instead of unfolding `weight`.
Mathlib building blocks: `Finsupp.weight_eq_sum` (Mathlib/Data/Finsupp/Weight.lean:100), `Nat.cast_div_charZero` (Mathlib/Data/Nat/Cast/Field.lean), `Finset.dvd_prod_of_mem` (Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean), `Finset.sum_div`, `Nat.cast_sum`, `Nat.cast_mul`, `field_simp`.
Composition sketch (≤3 lines):
```lean
example (hr : ∀ j, 0 < r j) (d : σ →₀ ℕ) :
    weight r d = (Finsupp.weight (fun j ↦ (∏ i, r i) / r j) d : ℝ) / ∏ i, r i := by
  simp only [weight, Finsupp.weight_eq_sum, smul_eq_mul, Nat.cast_sum, Nat.cast_mul, Finset.sum_div, Nat.cast_prod]
  refine Finset.sum_congr rfl fun j _ ↦ ?_
  rw [Nat.cast_div_charZero (Finset.dvd_prod_of_mem _ (Finset.mem_univ j)), Nat.cast_prod]; field_simp
```
(the `field_simp` call needs the nonvanishing facts `∏ (r i : ℝ) ≠ 0` and `(r j : ℝ) ≠ 0` from `hr` in context, as in evidence (1))
Call sites in our project (from Phase 6.0): 2 (Roth/Index.lean:152, Roth/Index.lean:155).
Refactor plan: none required. Inlining at the two sites would duplicate the computation; keep the lemma. Optionally replace it by `weight_eq_finsuppWeight_div_of_dvd` (evidence (2)) and recover the product form at Index.lean:152,155 with `(Finset.prod_ne_zero_iff.2 fun i _ ↦ (hr i).ne')` and `fun j ↦ Finset.dvd_prod_of_mem _ (Finset.mem_univ j)`.
Next action: no upstreaming; keep as is.

---

## Next step

No upstreaming; keep `Roth.weight_eq_finsuppWeight_div` as the clearing-denominators bridge for `index_eq_weightedOrder_div` (Roth/Index.lean:152,155). When `Roth.weight` is redefined as `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)` (parent action), reprove it from the parent's bridge lemma; optionally generalise to any nonzero common multiple `D` (evidence (2)).

## Evidence
- `.mathlib-quality/overview/evidence/Roth.weight_eq_finsuppWeight_div/compose_generalise_necessity.lean` (imports `Roth.Index`) compiled clean with `lake env lean` (about 21 s; first attempt failed on a `▸` elaboration detail, fixed by a type ascription). It contains:
  - (1) composition via `simp only [weight, Finsupp.weight_eq_sum, …]`, `Nat.cast_div_charZero`, `field_simp`;
  - (2) generalisation `weight_eq_finsuppWeight_div_of_dvd` (any nonzero common multiple `D`), and the project statement recovered from it;
  - (3) `hr` is necessary: `r = ![0, 1]`, `d = single 1 1` falsifies the identity (`simp [weight_single]`);
  - (4) re-aimed form against `Finsupp.weight (fun j ↦ (r j : ℝ)⁻¹)`.
- WebSearch ×3 (queries in the literature table).
- Loogle `Finsupp.weight` (30 hits, no scaling/cast lemma); LeanSearch and Lean-Finder queries as recorded.
- Greps: mathlib for `finsuppWeight`, `weight_smul`, `weight_nsmul`, `cast_weight`, `weight_cast`, `map_weight` (none relevant); theorem list of Mathlib/Data/Finsupp/Weight.lean; project for call sites; clean.tex for "natural weights".
- `ask_chatgpt_math` MCP not configured in this session.
