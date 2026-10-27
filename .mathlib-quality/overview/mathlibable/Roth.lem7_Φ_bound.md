---
decl: Roth.lem7_Φ_bound
file: Roth/Theta.lean
line: 678
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Pure numeric bookkeeping inequality delta1 + 10^(p-1) delta1^e < 3 10^(p-1) delta^e (e = (1/2)^(p-1), delta1 = delta(1+1/p)) from the proof of Lemma 7 (clean.tex l.1008-1019); every hypothesis is necessary (compiled counterexamples), no literature standing, no mathlib counterpart, not a 3-call composition; recommended resolution is to keep it project-local.
action: Keep in Roth/Theta.lean (single caller private theta_phi_lt_aux at Roth/Theta.lean:876); optionally make it private and golf hδe with Real.self_le_rpow_of_le_one; do not upstream.
---

# Roth.lem7_Φ_bound

## Inventory entry

### `theorem Roth.lem7_Φ_bound`
- **Type**: `{p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) : δ * (1 + 1 / p) + 10 ^ (p - 1) * (δ * (1 + 1 / p)) ^ ((1 / 2 : ℝ) ^ (p - 1)) < 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))`
- **What**: For `p ≥ 2` and `0 < δ ≤ 1`, with `δ₁ = δ(1 + 1/p)` and `e = (1/2)^{p-1}`, the inequality `δ₁ + 10^{p-1} δ₁^e < 3 · 10^{p-1} δ^e` holds.
- **How**: Sets `e`. Gets `e ≤ 1` (`pow_le_one₀`) and `1 ≤ 1 + 1/p ≤ 3/2` (`one_div_le_one_div_of_le`). Gets `δ ≤ δ^e` (`Real.rpow_le_rpow_of_exponent_ge`). Bounds `(δ(1+1/p))^e ≤ δ^e · 3/2` (`Real.mul_rpow`, `Real.rpow_le_rpow_of_exponent_le`). Then closes with one `linear_combination` of these facts, `le_self_pow₀` (`1 ≤ 10^{p-1}`) and `δ^e > 0` (`Real.rpow_pos_of_pos`).
- **Hypotheses**:
  - `hp`: needed for `1 + 1/p ≤ 3/2` and `10^{p-1} ≥ 10`. It fails at `p = 1`.
  - `hδ0`: needed for strictness. Both sides are 0 at `δ = 0`.
  - `hδ1`: needed for `δ ≤ δ^e`. It fails for large `δ`.
- **Uses from project**: `[]`
- **Used by**: `Roth.theta_phi_lt_aux` (private) at Roth/Theta.lean:876. It has no other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 674–702 (statement 678–680, proof 681–702, proof length 22 lines)
- **Notes**: The source is clean.tex §5, proof of Lemma 7, l.1008–1019. The Lean proof goes through `3/2` where the paper uses `δ₁ < 2δ` and `(1+p⁻¹)^e < 2`. Both give the same final bound.

## Junk check (Step 8)
- **Used anywhere?** Yes, once. The caller is the private `theta_phi_lt_aux` (Theta.lean:876), the Lemma 7 induction step.
- **Wrapper of 1–2 mathlib calls?** No. It is a 22-line real-arithmetic proof with rpow monotonicity and a `linear_combination`.
- **Does mathlib have it?** No. LeanFinder, LeanSearch and Loogle return only unrelated numeric bounds (Szemerédi, Liouville, Bertrand, Behrend) or building blocks.
- **Too specific (inline?)?** It is specific to the proof, but it isolates a named step of the paper ("Φ < … < 3·10^{p-1} δ^{(1/2)^{p-1}}"). Inlining it into the long `theta_phi_lt_aux` would hurt readability.
- **Well-chosen?** Yes. It mirrors the paper. It could be `private`, since its only caller is private.

Conclusion: **KEEP**. Optionally make it `private`.

## Mathlibable assessment (Step 9)

Pre-filter: none of the filters fire.
- It is public.
- The name has no `_aux` suffix.
- The docstring does not start with internal/auxiliary.
- Step 8 said KEEP.
- `grep -rln lem7 .lake/packages/mathlib/Mathlib/` finds nothing.
- It is not a glue lemma, because it has a real proof. INHERITED therefore does not apply.

Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built; the evidence file importing `Roth.Theta` compiles)
- decl `Roth.lem7_Φ_bound`:  ✓ resolved at Roth/Theta.lean:678
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)` (supremum of indices of bounded integer polynomials at rational points) and Lemmas 5, 6, 7 bounding it

### Statement (Phase 1)

`Roth.lem7_Φ_bound` is a theorem stating the following. Let `p ≥ 2` be an integer, let `0 < δ ≤ 1`, and put `δ₁ = δ(1 + 1/p)` and `e = 2^{-(p-1)}`. Then

  `δ₁ + 10^{p-1} δ₁^e < 3 · 10^{p-1} δ^e`.

This absorbs the bound `Φ < δ₁ + 10^{p-1} δ₁^e`, coming from Lemma 6 and the induction hypothesis, into the shape needed for the next induction step.

Variables (Lean side):
- `p`: number of variables (the induction level)
- `δ`: Roth's small parameter

Hypotheses (Lean side):
- `hp : 2 ≤ p`
- `hδ0 : 0 < δ`
- `hδ1 : δ ≤ 1`

Conclusion (math): `δ₁ + 10^{p-1} δ₁^e < 3·10^{p-1} δ^e`.

Conclusion (Lean): `δ * (1 + 1 / p) + 10 ^ (p - 1) * (δ * (1 + 1 / p)) ^ ((1 / 2 : ℝ) ^ (p - 1)) < 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is an internal numeric estimate in the proof of Lemma 7. It is not a structure, not a main result, and not a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 22
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma proof "Phi < delta_1 + 10^{p-1}" delta^{(1/2)^{p-1}} Theta_p bound induction | no | — | only additive-combinatorics Roth papers (arXiv 1409.3595, 2007.03528, 2111.12409); none has this estimate |
| 2 | WebSearch (general form) | Roth theorem Cassels Lemma 7 Theta_m(B;q;r) < 10^m delta^{(1/2)^m} induction proof | partial | Roth's lemma by induction on m (arXiv 2502.00731; Cassels, An Introduction to Diophantine Approximation, Ch. VI) | the setting matches, but no standalone numeric estimate; each exposition has its own constants |
| 3 | WebSearch (aliases / elementary form) | inequality x ≤ x^a for 0 < x ≤ 1 and 0 < a ≤ 1, (1+1/p)^{2^{-(p-1)}} bound elementary | partial | Bernoulli-type `(1+x)^a ≤ 1+ax` for `0<a<1`; `x ≤ x^a` | only the elementary ingredients, which are textbook facts |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` grep `Phi <`, `10^{p-1}` | yes | l.1008–1019: `Φ < δ₁ + 10^{p-1}δ₁^{(1/2)^{p-1}} … < 2δ + 2·10^{p-1}δ^{(1/2)^{p-1}} < 3·10^{p-1}δ^{(1/2)^{p-1}}` | matches the Lean statement exactly (the first and last terms of the chain) |
| 6 | nLab | Roth's theorem / numeric estimate | no | — | nLab has no entries for proof-internal numeric estimates in Diophantine approximation |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | this specific estimate is routine bookkeeping and is not discussed |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | arXiv 2502.00731, arXiv 2111.12409 | each exposition has its own constants |

### Literature summary (Phase 3)

Concept identified as: the constant-absorption step `Φ < 3·10^{p-1} δ^{(1/2)^{p-1}}` in the inductive proof of Roth's lemma (Lemma 7 of the Cassels-style exposition that clean.tex follows).

Sources agree on the standard form: no. It is not a standalone result anywhere. Constants such as `10`, `3` and `(1/2)^{p-1}` are specific to this exposition.

Most general standard form: none exists. The ingredients (`x ≤ x^a` for `x ≤ 1`, `a ≤ 1`; `c^a ≤ c` for `c ≥ 1`, `a ≤ 1`) are textbook facts that mathlib already has.

Generality dimensions where the literature varies: the constants only. There is no structural generality.

Disagreement with the literature: none. The Lean proof uses `1 + 1/p ≤ 3/2` instead of the paper's `< 2`, which gives the same conclusion.

### Generality analysis — `Roth.lem7_Φ_bound`

Literature-standard form (from Phase 3): none. The source states it for integers `p ≥ 2` and `0 < δ < 1`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hp : 2 ≤ p` | `2 ≤ p` | `p ≥ 2` | no | at `p = 1`, `δ = 1` the inequality reads `4 < 3` (compiled counterexample) |
| 2 | `hδ0 : 0 < δ` | `0 < δ` | `0 < δ` | no | at `δ = 0` both sides are `0` (compiled counterexample) |
| 3 | `hδ1 : δ ≤ 1` | `δ ≤ 1` | `δ < 1` | no (Lean is already weaker than the source) | at `p = 2`, `δ = 10^6` the left side exceeds the right side (compiled counterexample); some bound `δ ≤ C(p)` is needed, and `1` is the natural choice |
| 4 | `p : ℕ` | natural | integer | no meaningful one | `10^{p-1}` and `(1/2)^{p-1}` are natural powers; a real `p` would change the statement |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (every hypothesis is necessary, verified by the compiled counterexamples in evidence/Roth.lem7_Φ_bound/necessity.lean).
Number of weakening opportunities found: 0.
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | it has only numeric hypotheses |
| 2 | sequences to filters? | no | — | it is a finite inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | `Real.rpow` forces ℝ |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | the natural `p` indexes powers |
| 8 | concrete-via-abstract? | no | — | there is no named object; the statement is pure arithmetic with explicit constants |
| 9 | false-generalisation guard | n/a | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: it is an explicit numeric inequality with fixed constants. There is no organisational reformulation.

### Proof strategy — `Roth.lem7_Φ_bound`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `hδe` is proved via `simpa using Real.rpow_le_rpow_of_exponent_ge`; mathlib has exactly `Real.self_le_rpow_of_le_one` (Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:737), so this is a one-line golf, not a gap | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (monotonicity facts combined by `linear_combination`). A minor golf is available: `hδe := Real.self_le_rpow_of_le_one hδ0.le hδ1 he1`.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.lem7_Φ_bound`

- [A] Lean-Finder, query "δ(1+1/p) + 10^(p-1) (δ(1+1/p))^((1/2)^(p-1)) < 3·10^(p-1) δ^((1/2)^(p-1)) for 0<δ≤1, p≥2": only unrelated explicit bounds (`SzemerediRegularity.hundred_lt_pow_initialBound_mul`, `LiouvilleNumber.aux_calc`, `Bertrand.real_main_inequality`, `Behrend.bound`, `Behrend.roth_lower_bound_explicit`).
- [B] Loogle, query `?x ≤ ?x ^ ?e`: only natural-power versions (`le_self_pow₀`, `Nat.le_self_pow`, …).
- [C] LeanSearch, query "for 0 < x ≤ 1 and exponent e ≤ 1, x ≤ x ^ e real rpow": building blocks `Real.self_le_rpow_of_le_one`, `Real.rpow_le_rpow_of_exponent_ge`, `Real.rpow_le_self_of_le_one`.
- [D] Grep mathlib source: `lem7` has no hits. `self_le_rpow_of_le_one` is found at Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:737.
- [E] Name pattern (`lem7_Φ_bound`): project-only.

Searched for both the exact form and the generic ingredient forms.

Concluded: found building blocks (`Real.self_le_rpow_of_le_one`, `Real.mul_rpow`, `Real.rpow_le_rpow_of_exponent_le`, `le_self_pow₀`, `Real.rpow_pos_of_pos`). The statement itself is not in mathlib.

### Normal-form check — `Roth.lem7_Φ_bound`

Equivalent formalisms:
- (a) the current form, with `δ * (1 + 1/p)` spelled out;
- (b) a form with `δ₁` as a parameter and the hypothesis `δ₁ = δ(1+1/p)`;
- (c) a form with `e` abstracted as any `0 < e ≤ 1`.

Mathlib has no canonical form, since this is not a mathlib concept. The current form (a) matches the call site, where `ε := δ * (1 + 1 / ((n:ℝ)+1+1))` is unfolded by `simp only`.

RHS convention respected? n/a (this is an inequality).

### Syntactic generality — `Roth.lem7_Φ_bound`

Alternative restatements attempted:
- form (c), with arbitrary `e ∈ (0,1]` and `C = 10^{p-1} ≥ 10` (the proof only uses these);
- form (b).

Chosen restatement: current.
Justification: the single caller has exactly these quantities. Abstracting `e` and `C` would move bookkeeping to the call site with no other consumer.

### Superfluous-argument audit — `Roth.lem7_Φ_bound`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hp` | yes | counterexample at `p = 1` compiled |
| 2 | `hδ0` | yes | counterexample at `δ = 0` compiled |
| 3 | `hδ1` | yes | counterexample at `δ = 10^6`, `p = 2` compiled |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.lem7_Φ_bound`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:876 (private `theta_phi_lt_aux`) | `have hb := lem7_Φ_bound (p := n + 1 + 1) hp hδ0 hδ1.le` then `simp only [Nat.add_sub_cancel, ...] at hb` and used as `hb.le` in the final combination |

Inline-derivation grep: none. `lem7_numeric` (Theta.lean:710) is the next step of the chain, not a re-derivation.

### Composition check (Phase 6)

Can `Roth.lem7_Φ_bound` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.self_le_rpow_of_le_one` together with `Real.mul_rpow`.
- Result: partial. These give `δ ≤ δ^e` and split `(δ c)^e = δ^e c^e`. The bounds `c ≤ 3/2`, `c^e ≤ c`, `10^{p-1} ≥ 1` and a linear combination are still needed.

Attempt 2: the current proof with mathlib lemmas only.
- Result: succeeds, but takes about 20 lines with `linear_combination`. That is a real proof, not a composition.

Conclusion: NOT-COMPOSABLE (in the ≤3-call sense).

### Verdict: `Roth.lem7_Φ_bound`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the estimate appears only as an internal step of the proof of Lemma 7 (clean.tex l.1008–1019). Other Roth expositions use their own constants, and none states it standalone.
- Generality analysis (Phase 4): MAXIMALLY GENERAL. All three hypotheses are necessary (compiled counterexamples).
- Mathlib search (Phase 5): building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE. It is a genuine 20-line arithmetic proof.

**Rationale:**

The theorem is the paper's constant-absorption inequality for the induction step of Roth's lemma. The NO buckets do not fit:
- mathlib does not have the statement;
- it is not a ≤3-call composition, since it needs several monotonicity facts and a linear combination.

The YES buckets do not fit either. It is a statement with arbitrary explicit constants (`3`, `10`, `(1/2)^{p-1}`) that has no meaning outside this particular proof. Mathlib does not collect such ad hoc numeric inequalities: the closest analogues, such as `Bertrand.real_main_inequality` and `LiouvilleNumber.aux_calc`, live inside the files of the theorems they serve. That leaves BORDERLINE by elimination, consistent with the sibling `Roth.lem6M_lt` report. The practical judgment is clear: keep it in the project. If Roth's theorem were ever upstreamed, it would travel with that development as a private helper.

Numbered questions:
1. Keep `Roth.lem7_Φ_bound` project-local and never upstream it on its own? (Recommended: yes.)
2. Make it `private`, given that its only caller (`theta_phi_lt_aux`, Theta.lean:876) is private? (Recommended: optional; yes if the public API should list only paper lemmas.)
3. Golf `hδe` to `Real.self_le_rpow_of_le_one hδ0.le hδ1 he1`? (Recommended: yes, cosmetic.)

Next action: the user answers the questions. The default is no change: keep the theorem in Roth/Theta.lean with its one call site at line 876.

---

### Next step

Keep `Roth.lem7_Φ_bound` in Roth/Theta.lean. Optionally make it private and apply the one-line golf. Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.lem7_Φ_bound/necessity.lean` imports `Roth.Theta`. `lake env lean` compiled it clean, with no output, in 41 s. It proves:
  - the inequality fails at `p = 1`, `δ = 1`, so `hp` is necessary;
  - it fails at `δ = 0`, so `hδ0` is necessary;
  - it fails at `p = 2`, `δ = 10^6`, so `hδ1` cannot be dropped;
  - a sanity instantiation of the original statement at `p = 2`.
- Mathlib grep for `lem7`: no hits. `self_le_rpow_of_le_one` is found at Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:737.
- Project grep `grep -rn lem7_Φ_bound Roth/`: the declaration and one use at Theta.lean:876.
- LeanFinder (1 query), LeanSearch (1 query) and Loogle (1 query), as in the search-status block.
- WebSearch: 3 queries (literature table).
- ChatGPT MCP: n/a (not configured).
- Local references: clean.tex l.1008–1019.
