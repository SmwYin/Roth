---
decl: Roth.sqrt_one_sub_inv_lt
file: Roth/Lattice.lean
line: 29
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: A one-off numeric inequality from the proof of Lemma 8 with no literature standing and no mathlib counterpart; mathlib has the key building block Real.sqrt_one_add_le, but the remaining arithmetic for the lambda side is a real (if short) proof rather than a 3-call composition, so no bucket fits cleanly; recommended resolution is to keep it project-local.
action: Keep in Roth/Lattice.lean as a project lemma (not for mathlib); optionally reprove via Real.sqrt_one_add_le and weaken 2 ≤ m to 1 ≤ m (both compiled in evidence/Roth.sqrt_one_sub_inv_lt/experiments.lean); single caller Roth.sum_inv_lt (Roth/Lattice.lean:87) needs no change.
---

# Roth.sqrt_one_sub_inv_lt

## Inventory entry

### `theorem Roth.sqrt_one_sub_inv_lt`
- **Type**: `∀ {m : ℕ}, 2 ≤ m → ∀ {lam : ℝ}, 2 * √(m : ℝ) < lam → √(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2`
- **What**: For an integer `m ≥ 2` and real `λ > 2√m`, `√(1 - 1/m) < 1 - λ⁻²`. This is the chain `1 - λ⁻² > 1 - 1/(4m) > √(1 - 1/m)` in clean.tex §6, proof of Lemma 8 (l.1115–1117).
- **How**: Derives `4m < λ²` by `nlinarith` with `Real.sq_sqrt` and `Real.sqrt_nonneg`, then `λ⁻² < 1/(4m)` via `inv_pow`, `div_div` and `one_div_lt_one_div_of_lt`; rewrites the goal with `Real.sqrt_lt'` (positivity of the RHS from `one_div_le_one_div_of_le`) and closes the squared inequality by `nlinarith [sq_nonneg (lam⁻¹ ^ 2)]`.
- **Hypotheses**: `hm : 2 ≤ m` (only `1 ≤ m` is needed, verified); `hlam : 2 * √m < lam` (essential).
- **Uses from project**: `[]`
- **Used by**: `Roth.sum_inv_lt` (Roth/Lattice.lean:87, inside a `gcongr` side goal). `grep -rn sqrt_one_sub_inv_lt Roth/` finds only l.29 and l.87.
- **Visibility**: public
- **Lines**: 26–37 (docstring 26–28, statement 29–30, proof 31–37), proof length 7 lines
- **Notes**: Stated over `m : ℕ` with a cast; the real version with `1 ≤ m` holds with the same proof.

## Junk check (Step 8)
- Used anywhere? Yes, once (`Roth.sum_inv_lt`, l.87).
- Wrapper of 1–2 mathlib calls? No. It is a 7-line `nlinarith` proof; the shortest alternative found (via `Real.sqrt_one_add_le`) is still about 5 lines.
- Does mathlib have it? No (Phase 5). The nearest is `Real.sqrt_one_add_le : -1 ≤ x → √(1 + x) ≤ 1 + x / 2`.
- Too specific (inline?)? It is specific, but inlining 7 lines into the `gcongr` side goal of `sum_inv_lt` would make that calc harder to read; the named step mirrors the source's displayed chain.
- Well-chosen statement? Yes for the project; `2 ≤ m` could be relaxed to `1 ≤ m` but the caller has `2 ≤ m` anyway.
- Conclusion: `KEEP` (project-local helper).

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring does not start with internal/auxiliary; Step 8 said KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `sqrt_one_sub_inv_lt` gives no hit. Not a glue lemma. Full workflow follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per the brief; the evidence file importing `Roth.Lattice` compiles)
- decl `Roth.sqrt_one_sub_inv_lt`: ✓ resolved at Roth/Lattice.lean:29
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the lattice count estimate (Lemma 8): few multi-indices with small weighted sum.

### Statement (Phase 1)

`Roth.sqrt_one_sub_inv_lt` is a theorem stating: if `m ≥ 2` is an integer and `λ` is real with `λ > 2√m`, then `√(1 - 1/m) < 1 - 1/λ²`. Mathematically it follows from `1/λ² < 1/(4m)` and `√(1 - 1/m) ≤ 1 - 1/(2m) < 1 - 1/(4m)` (tangent-line bound for the square root).

Variables / typeclasses involved (Lean side):
- `m : ℕ`: the number of variables in Lemma 8 (cast to ℝ)
- `lam : ℝ`: the parameter λ of Lemma 8

Hypotheses (Lean side):
- `hm : 2 ≤ m`: the source's standing hypothesis; only `1 ≤ m` is used
- `hlam : 2 * √m < lam`: gives `λ² > 4m`

Conclusion (math): `√(1 - 1/m) < 1 - λ⁻²`.

Conclusion (Lean): `√(1 - 1 / (m : ℝ)) < 1 - lam⁻¹ ^ 2`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a numeric helper inequality inside the proof of Lemma 8; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 7
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | `"sqrt(1-1/m)" "1-1/(4m)" inequality` | no | none | no source states this inequality; results unrelated (arXiv 2207.09410, PMC5686241, a Liouville note on (1-1/m)^m) |
| 2 | WebSearch (general form) | `inequality sqrt(1 - x) less than 1 - x/2 elementary bound square root` | partial | `√(1 - x) ≤ 1 - x/2` for `x ≤ 1` (tangent line to a concave function) | folklore; the general principle behind the lemma; appears only as exercise-level material |
| 3 | WebSearch (named-after / usage) | `Roth theorem lattice point count lemma "lambda > 2 sqrt m" index estimate proof` | no | none | Roth's lemma / index literature (Ferretti, math.uh.edu notes) does not isolate this numeric step |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (absent from available and deferred tool lists) |
| 5 | Local references | `grep -n "1/(4m)" .mathlib-quality/references/clean.tex` | yes | l.1115 "1-λ^{-2} > 1-1/(4m) > √(1-1/m) > 0"; l.1117 squaring argument | Lean statement is exactly the source chain with the middle term dropped |
| 6 | nLab | "square root inequality" | no | none | elementary real inequality outside nLab's scope |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | covered by WebSearch #2 (tangent-line bound for √) | no dedicated thread | n/a | exercise-level |
| 10 | recent arXiv | covered by WebSearch #1 and #3 | no | none | the inequality is only ever used inline |

Sources: [arXiv 2207.09410](https://arxiv.org/pdf/2207.09410), [PMC5686241](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5686241/), [AoPS IMO 1962 P2](https://artofproblemsolving.com/wiki/index.php/1962_IMO_Problems/Problem_2), [Roth notes, math.uh.edu](https://www.math.uh.edu/~minru/fields/roth.pdf), [arXiv math/9708214](https://arxiv.org/pdf/math/9708214).

### Literature summary (Phase 3)

Concept identified as: an ad hoc numeric inequality; the only standard ingredient is the tangent-line bound `√(1 + x) ≤ 1 + x/2`.
Sources agree on the standard form: there is no standard form for the lemma itself; the tangent-line bound is universal.
Most general standard form: `√(1 + x) ≤ 1 + x/2` for `x ≥ -1` (already in mathlib as `Real.sqrt_one_add_le`).
Generality dimensions where the literature varies:
  - `m`: integer `≥ 2` in the source; any real `m ≥ 1` suffices
Disagreement with the literature: none (matches the source).

### Generality analysis — `Roth.sqrt_one_sub_inv_lt`

Literature-standard form (from Phase 3): none for the lemma; the ingredient is `Real.sqrt_one_add_le`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `m : ℕ` (cast) | natural number | real `m` | yes | the proof only uses `(m : ℝ) ≥ 1`; real version compiled in evidence |
| 2 | `hm : 2 ≤ m` | `2 ≤ m` | `1 ≤ m` | yes | `m = 1` works (LHS = 0, RHS > 0 as λ > 2); compiled. Cannot drop entirely: `m = 1/100`, `λ = 1/2` is a compiled counterexample |
| 3 | `hlam : 2√m < λ` | strict | strict | no | needed for `λ⁻² < 1/(4m)`; with only `λ > √(2m)` style bounds the RHS can drop below |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (in a minor way: `m : ℕ, 2 ≤ m` versus `m : ℝ, 1 ≤ m`)
Number of weakening opportunities found: 2, both verified in `.mathlib-quality/overview/evidence/Roth.sqrt_one_sub_inv_lt/experiments.lean` (clean compile).
Proposed restatement (if it were to be shipped anywhere):

```lean
theorem sqrt_one_sub_inv_lt_real {m : ℝ} (hm : 1 ≤ m) {lam : ℝ} (hlam : 2 * √m < lam) :
    √(1 - 1 / m) < 1 - lam⁻¹ ^ 2
```

Cost of restatement: CHEAP (compiled). However the weakening does not change the mathlib verdict: the statement remains a one-off inequality.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | bundled preambles to typeclasses | no | no structures | n/a |
| 2 | sequences to filters | no | finite numeric inequality | n/a |
| 3 | construction to universal property | no | no construction | n/a |
| 4 | set predicate to bundled substructure | no | no sets | n/a |
| 5 | field-specific to weaker typeclass | no | `√` is `Real.sqrt`; ℝ is intrinsic | n/a |
| 6 | 1-categorical to higher | no | not categorical | n/a |
| 7 | concrete index generalisation | yes (minor) | `m : ℕ` to `m : ℝ` with `1 ≤ m` (verified) | none in mathlib |
| 8 | concrete-via-abstract | no | no named object | n/a |
| 9 | false-generalisation guard | no false generalisation | the real version specialises to the original by a cast | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only change is ℕ to ℝ for `m`, a cosmetic widening of a project-specific inequality; it enables no mathlib API.

### Proof strategy — `Roth.sqrt_one_sub_inv_lt`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | topology ε-δ | no | n/a | n/a |
| 2 | algebra element-wise vs ideals | no | n/a | n/a |
| 3 | sequences vs filters | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing helper lemmas | no | mathlib's `Real.sqrt_one_add_le` replaces the squaring step (`Real.sqrt_lt'` + final `nlinarith`) with a `calc` | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (squaring via `Real.sqrt_lt'`, as in the source). An equally short alternative uses `Real.sqrt_one_add_le` then `linarith` (compiled in the evidence file); not strictly shorter, so optional.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.sqrt_one_sub_inv_lt`

[A] Lean-Finder       "sqrt(1 - 1/m) < 1 - lambda^(-2) when lambda > 2 sqrt m" → `LiouvilleNumber.aux_calc`, `Stirling.sqrt_pi_le_stirlingSeq`, `Nat.lt_ratSqrt_add_inv_prec_sq`, π-bound lemmas: no match
[B] Loogle            `√(1 - ?x) ≤ _` → no hits
[C] LeanSearch        "square root of 1 minus x is less than 1 minus x over 2" → `Real.sqrt_one_add_le` (building block), `Real.sqrt_le_one`, `Real.sqrt_lt'`, `Real.le_sqrt_of_sq_le`, `Real.sqrt_le_iff`
[D] Grep mathlib src  `sqrt_one_sub|sqrt_one_add_le|sqrt_one_sub_inv` → only `Real.sqrt_one_add_le` (Mathlib/Analysis/Real/Sqrt.lean:440) and unrelated trig/complex `sqrt_one_sub` lemmas
[E] Name pattern      `sqrt_one_sub_inv_lt` in mathlib → no declaration

Searched for both the user's form and the tangent-line general form.

Concluded: found building blocks (`Real.sqrt_one_add_le`, `one_div_lt_one_div_of_lt`, `inv_pow`, `Real.sq_sqrt`); the exact form is not in mathlib.

### Normal-form check — `Roth.sqrt_one_sub_inv_lt`

Equivalent formalisms: `√(1 - 1/m) < 1 - λ⁻²` versus `1 - 1/m < (1 - λ⁻²)^2` (squared) versus `λ⁻¹ / (1 - λ⁻²) < λ⁻¹ / √(1 - 1/m)` (the reciprocal form used by the caller).
Does mathlib already have a canonical form? No canonical form for this inequality. It is an inequality, not an ↔.
RHS convention respected? n/a (inequality)

### Syntactic generality — `Roth.sqrt_one_sub_inv_lt`

Alternative restatements attempted:
- real `m` with `1 ≤ m`: compiles, but the caller has `m : ℕ` and would need a cast argument
- squared form: rejected; the caller's `gcongr` side goal is exactly the √ form
Chosen restatement: the current form.
Justification: it matches the `gcongr` side goal in `sum_inv_lt` verbatim.

### Superfluous-argument audit — `Roth.sqrt_one_sub_inv_lt`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hm : 2 ≤ m` | partly | only `1 ≤ m` needed (verified); the caller has `2 ≤ m` |
| 2 | `m : ℕ` | no | any real `m ≥ 1` works (verified) |
| 3 | `hlam` | yes | essential |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 optional (`2 ≤ m` to `1 ≤ m`)

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.sqrt_one_sub_inv_lt`

Internal use count: 1 (in the declaring file; 0 in other files)
External-to-file callers: 0

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Lattice.lean:87 | `exact sqrt_one_sub_inv_lt hm hlam` closing a `gcongr` side goal in `Roth.sum_inv_lt` |

Inline-derivation grep: `grep -rn "sqrt_lt'\|1 / (m : ℝ)" Roth/` shows no other re-derivation of this inequality (none).

### Composition check (Phase 6)

Can `Roth.sqrt_one_sub_inv_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(Real.sqrt_one_add_le h).trans_lt (by linarith [λ⁻² < 1/(4m)])`
  - Mathlib decls used: `Real.sqrt_one_add_le`, `inv_pow`, `one_div_lt_one_div_of_lt`, `Real.sq_sqrt`, `Real.sqrt_nonneg`
  - Result: partial. The square-root half is one mathlib call, but establishing `λ⁻² < 1/(4m)` from `2√m < λ` needs an `nlinarith` step plus a reciprocal comparison; the compiled version (evidence file) is a 5-line proof.
Attempt 2: `Real.sqrt_lt'` then `nlinarith` (the current proof): a real proof by the 6b heuristic.

Conclusion: NOT-COMPOSABLE (by the strict 6b heuristic; the gap is elementary arithmetic, not missing API)

### Verdict: `Roth.sqrt_one_sub_inv_lt`

Verdict: BORDERLINE-needs-human

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): no literature states this inequality; it is an inline step of clean.tex §6 (l.1115–1117); its only standard ingredient is the tangent-line bound for √.
- Generality analysis (Phase 4): STRICTLY NARROWER in a cosmetic way (`m : ℕ, 2 ≤ m` to `m : ℝ, 1 ≤ m`, verified), which does not create mathlib value.
- Mathlib search (Phase 5): not in mathlib; building block `Real.sqrt_one_add_le` exists.
- Composition check (Phase 6): NOT-COMPOSABLE under the strict ≤3-call rule (needs `nlinarith`/`linarith` arithmetic).

**Rationale:** The statement is a numeric inequality with specific constants (`2√m`, `λ⁻²`, `1/m`) tailored to Lemma 8 of the Roth formalisation. Mathlib would not accept it: it names no concept, has no literature standing, and the general principle behind it (`√(1 + x) ≤ 1 + x/2`) is already `Real.sqrt_one_add_le`. So neither YES bucket applies. At the same time the strict NO-composable gate requires a ≤3-call composition, and the remaining `λ`-side arithmetic needs a short `nlinarith`/`linarith` proof, so NO-composable does not fit cleanly either; NO-mathlib-has-it does not fit because mathlib has only the ingredient. That leaves a judgment call, which the recommendation below resolves as "keep project-local".

Numbered questions:
1. Do you agree this lemma should stay project-local (not proposed to mathlib), as the evidence suggests? (Recommended: yes.)
2. Should the hypothesis be relaxed from `2 ≤ m` to `1 ≤ m` (compiled; the caller is unaffected), or kept as `2 ≤ m` to mirror the source? (Recommended: keep, it matches clean.tex.)
3. Should the proof be rewritten through `Real.sqrt_one_add_le` (compiled in the evidence file, same length) to make the mathlib dependency explicit? (Optional.)

Next action: user answers the questions; with the recommended answers the lemma stays as is in Roth/Lattice.lean, used once by `Roth.sum_inv_lt` (l.87).

---

### Next step

Keep `Roth.sqrt_one_sub_inv_lt` in Roth/Lattice.lean as a project lemma; no mathlib PR. Optional tweaks (relax `2 ≤ m` to `1 ≤ m`, reprove via `Real.sqrt_one_add_le`) are compiled in the evidence file and need no change at the single caller `Roth.sum_inv_lt` (Roth/Lattice.lean:87).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.sqrt_one_sub_inv_lt/experiments.lean` (imports `Roth.Lattice`), compiled clean with `lake env lean`. Contents: the real-`m`, `1 ≤ m` version proved via `Real.sqrt_one_add_le`; the project statement as a one-line corollary; the ℕ version with `1 ≤ m`; a counterexample (`m = 1/100`, `λ = 1/2`) showing `1 ≤ m` cannot be dropped. The first compile failed only on the counterexample's `norm_num` (leftover `-3 ≤ √(-99)`), fixed with `Real.sqrt_nonneg`.
- Searches: WebSearch ×3, LeanSearch ×1, Loogle ×1, Lean-Finder ×1, mathlib grep ×1, local grep of clean.tex (all recorded above).
- `grep -rn sqrt_one_sub_inv_lt Roth/` gives l.29 and l.87 only.
