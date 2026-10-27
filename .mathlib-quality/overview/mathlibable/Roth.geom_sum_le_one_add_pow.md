---
decl: Roth.geom_sum_le_one_add_pow
file: Roth/CoeffNorm.lean
line: 205
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Elementary inequality sum over s in range (r+1) of t^s at most (1+t)^r for t nonneg, absent from mathlib (no hit across five methods), not a 3-call composition, and the identical proof compiles verbatim over any ordered (even non-commutative) semiring, so it should be upstreamed in that generality.
action: Restate over [Semiring R] [PartialOrder R] [IsOrderedRing R] (compiled in evidence/Roth.geom_sum_le_one_add_pow/weaken.lean) and PR it to Mathlib/Algebra/Order/Ring/GeomSum.lean next to geom_sum_alternating_of_le_neg_one; the single caller Roth.sum_box_prod_pow_le_aux (Roth/CoeffNorm.lean:218) then uses the mathlib lemma unchanged.
---

# Roth.geom_sum_le_one_add_pow

## Inventory entry

### `theorem Roth.geom_sum_le_one_add_pow`
- **Type**: `∀ {t : ℝ}, 0 ≤ t → ∀ (r : ℕ), ∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r`
- **What**: For real `t ≥ 0` and `r ∈ ℕ`, the truncated geometric sum `1 + t + ⋯ + t^r` is at most `(1 + t)^r`. This is the step in clean.tex §6, proof of Lemma 9 (l.1546, l.1567) that turns a monomial count into `(1 + |α|)^r`.
- **How**: Rewrites `(t + 1)^r` with the binomial theorem `add_pow`, compares term by term with `Finset.sum_le_sum`, and bounds each term using `le_mul_of_one_le_right`, `pow_nonneg` and `Nat.choose_pos` (with `Finset.mem_range_succ_iff`) cast to ℝ, i.e. `1 ≤ C(r, m)`.
- **Hypotheses**: `ht : 0 ≤ t`. This is needed: `t = -1/2`, `r = 2` gives `3/4 ≤ 1/4` (counterexample compiled in the evidence file).
- **Uses from project**: `[]`
- **Used by**: `Roth.sum_box_prod_pow_le_aux` (private, Roth/CoeffNorm.lean:218), which feeds `Roth.abs_eval_le`. `grep -rn geom_sum_le_one_add_pow Roth/` finds only l.205 (declaration) and l.218.
- **Visibility**: public
- **Lines**: 202–211 (docstring 202–204, statement 205–206, proof 207–211), proof length 5 lines
- **Notes**: Stated over ℝ only, though nothing in the proof is specific to ℝ.

## Junk check (Step 8)
- Used anywhere? Yes, once (`sum_box_prod_pow_le_aux`, l.218), applied inside a `Finset.prod_le_prod₀`, so it is used as a named term rather than inlined.
- Wrapper of 1–2 mathlib calls? No. It is a 5-line proof (binomial expansion plus a term-wise comparison).
- Does mathlib have it? No (see Phase 5). The closest relatives are `one_add_mul_le_pow` (Bernoulli) and `pow_add_pow_le`, neither of which gives this.
- Too specific (inline?)? Inlining would put a 5-line argument inside a `simpa` term; it is cleaner as a lemma.
- Well-chosen statement? Yes. It is clean and matches the source verbatim.
- Conclusion: `KEEP`. Better still, generalise and upstream it (see Step 9), then delete the project copy.

## Mathlibable assessment (Step 9)

Pre-filter: the declaration is public, its name does not end in `_aux`, and its docstring does not start with internal or auxiliary. Step 8 said KEEP. A namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `geom_sum_le_one_add_pow` found no hit. None of the pre-filters fire, so the full workflow follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (the project is built according to the brief; the evidence file importing `Roth.CoeffNorm` elaborates without errors)
- decl `Roth.geom_sum_le_one_add_pow`: ✓ resolved at Roth/CoeffNorm.lean:205
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  ℓ¹ coefficient norms and value bounds for integer polynomials (Lemmas 3 and 9 of the Roth proof).

### Statement (Phase 1)

`Roth.geom_sum_le_one_add_pow` is a theorem stating the following. For every real `t ≥ 0` and every integer `r ≥ 0`,
  `∑_{s=0}^{r} t^s ≤ (1 + t)^r`.
The reason is that `(1+t)^r = ∑_{s=0}^{r} C(r,s) t^s` and `C(r,s) ≥ 1` for `0 ≤ s ≤ r`.

Variables / typeclasses involved (Lean side):
- `t : ℝ`: the ratio of the geometric sum
- `r : ℕ`: the truncation degree and exponent

Hypotheses (Lean side):
- `ht : 0 ≤ t`: nonnegativity, so that each term `C(r,s) t^s` dominates `t^s`

Conclusion (math): the truncated geometric sum of degree `r` is dominated by `(1+t)^r`.

Conclusion (Lean): `∑ s ∈ Finset.range (r + 1), t ^ s ≤ (1 + t) ^ r`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper inequality for Lemma 9. It is not a new structure, not a main result and not a named theorem.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | `"\sum_{k=0}^n x^k \le (1+x)^n" inequality binomial coefficients at least one` | partial | no source states it as a named result. Results (proofwiki Bernoulli, IIT binomial problems, arXiv 1701.07778 "On Number of Rich Words") use the same binomial-expansion domination argument | folklore, a one-line consequence of the binomial theorem |
| 2 | WebSearch (general form) | `truncated geometric series bounded by (1+x)^n ordered semiring binomial expansion bound` | partial | arXiv 2508.01471 (hemiring-valued pseudonormed rings) proves Bernoulli-type inequalities in ordered semirings by the same method; LeanAide docs for `Mathlib.Algebra.Order.Ring.Pow` list mathlib's Bernoulli lemmas | confirms that the natural generality is an ordered semiring |
| 3 | WebSearch (named-after / usage) | `Roth theorem proof "(1+\|\alpha\|)^r" bound polynomial value height coefficients` | yes | arXiv math/0307203 (quantitative Roth–Ridout) bounds the value at `(ζ,…,ζ)` by height times `(1+\|ζ\|)^{∑ r_j}`, the same use as here | the standard height estimate `\|P(α)\| ≤ H (1+\|α\|)^{deg}` relies on this inequality implicitly |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP is not configured in this session (absent from the available and deferred tool lists) |
| 5 | Local references | `grep -n "geom\|1 + t\|(1+t)" .mathlib-quality/references/clean.tex` | yes | l.1546 "∑_{j=0}^r t^j ≤ (1+t)^r, since each binomial coefficient is at least 1"; l.1567 the same with `t ≥ 0` | the Lean statement matches the source exactly |
| 6 | nLab | "geometric series", "binomial theorem" | no | nLab has binomial-theorem pages but no inequality of this form | elementary inequality outside nLab's scope |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | "sum x^k le (1+x)^n" | no dedicated thread found by the WebSearch runs above | n/a | the statement is a textbook exercise-level fact |
| 10 | recent arXiv | covered by WebSearch #2 and #3 (arXiv 2508.01471, math/0307203) | partial | used inline, never stated as a lemma | |

Sources: [arXiv 1701.07778](https://arxiv.org/pdf/1701.07778), [ProofWiki Bernoulli](https://proofwiki.org/wiki/Bernoulli%27s_Inequality), [arXiv 2508.01471](https://arxiv.org/pdf/2508.01471), [LeanAide Order.Ring.Pow](https://math.iisc.ac.in/~gadgil/descs/Mathlib.Algebra.Order.Ring.Pow.html), [arXiv math/0307203](https://arxiv.org/pdf/math/0307203).

### Literature summary (Phase 3)

Concept identified as: the domination of a truncated geometric sum by a binomial power (a folklore corollary of the binomial theorem, used in height estimates for polynomial values).
Sources agree on the standard form: yes. It is always `∑_{k≤n} x^k ≤ (1+x)^n` for `x ≥ 0`.
Most general standard form: valid for any `x ≥ 0` in an ordered semiring. The proof uses only the binomial expansion of `(x+1)^n`, which holds without commutativity because `1` commutes with `x`, together with `1 ≤ (C(n,k) : R)`. A two-variable cousin is `∑_{k≤n} a^k b^{n-k} ≤ (a+b)^n` for `a, b ≥ 0` in a commutative ordered semiring.
Generality dimensions where the literature varies:
  - scalar ring: ℝ (here) up to any ordered semiring; the most general is an ordered semiring
Disagreement with the literature: none

### Generality analysis — `Roth.geom_sum_le_one_add_pow`

Literature-standard form (from Phase 3): `0 ≤ x` in an ordered semiring `R` implies `∑ i ∈ range (n+1), x^i ≤ (1+x)^n`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `t : ℝ` | real number | element of an ordered semiring | yes | the proof uses `add_pow`, `pow_nonneg`, `le_mul_of_one_le_right` and `1 ≤ ↑(choose)`, all available in `[Semiring R] [PartialOrder R] [IsOrderedRing R]` (non-commutative via `(Commute.one_right t).add_pow`). Verified, see the evidence file |
| 2 | `ht : 0 ≤ t` | nonnegative | nonnegative | no | needed: `t = -1/2`, `r = 2` is a counterexample (compiled) |
| 3 | `r : ℕ` | natural number | natural number | no | it is an exponent |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (ℝ → arbitrary ordered semiring)
Verified weakening: `geom_sum_le_one_add_pow''` in `.mathlib-quality/overview/evidence/Roth.geom_sum_le_one_add_pow/weaken.lean` (and the commutative variant `geom_sum_le_one_add_pow'`) gives a clean `lean_diagnostic_messages`. The only proof change is the cast step: `exact_mod_cast Nat.choose_pos …` becomes `simpa using Nat.mono_cast (α := R) (Nat.choose_pos …)`, because the ℝ cast needed `CharZero`. Over ℝ the generalised lemma reproduces the project statement as a one-line term (also in the evidence file).
Proposed restatement:

```lean
theorem geom_sum_le_one_add_pow {R : Type*} [Semiring R] [PartialOrder R] [IsOrderedRing R]
    {x : R} (hx : 0 ≤ x) (n : ℕ) :
    ∑ i ∈ Finset.range (n + 1), x ^ i ≤ (1 + x) ^ n
```

Cost of restatement: CHEAP (mechanical; the proof is unchanged except one cast line).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | bundled preambles to typeclasses | no | there are no bundled structures | n/a |
| 2 | sequences to filters | no | finite inequality, no limits | n/a |
| 3 | construction to universal property | no | no construction | n/a |
| 4 | set predicate to bundled substructure | no | no subsets | n/a |
| 5 | field-specific to weaker typeclass | yes | ℝ → `[Semiring R] [PartialOrder R] [IsOrderedRing R]` (verified) | applies to ℕ, ℚ, `NNReal`, `ENNReal`-like semirings, ordered polynomial semirings |
| 6 | 1-categorical to higher | no | not categorical | n/a |
| 7 | concrete index generalisation | no | `ℕ` exponent is intrinsic | n/a |
| 8 | concrete-via-abstract | no | the statement mentions no named object beyond ℝ, which is covered by row 5 | n/a |
| 9 | false-generalisation guard | no false generalisation | the generalised statement is literally the same inequality, specialising to the original over ℝ | n/a |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (row 5, the same weakening as Phase 4b; there is no separate modernisation)
  - Proposed mathlib-idiomatic restatement: as in Phase 4b
  - Cost: CHEAP
  - Mathlib downstream this enables: usable in ℕ / ℚ / `NNReal` estimates (e.g. height bounds), next to `one_add_mul_le_pow` and `pow_add_pow_le`
  - Real mathematical improvement: the lemma holds verbatim in every ordered semiring; stating it over ℝ only would force re-proofs in ℕ and `NNReal`.

### Proof strategy — `Roth.geom_sum_le_one_add_pow`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | topology ε-δ | no | n/a | n/a |
| 2 | algebra element-wise vs ideals | no | n/a | n/a |
| 3 | sequences vs filters | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing helper lemmas | no | `add_pow` plus a term-wise `Finset.sum_le_sum` is the canonical route | n/a |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (binomial theorem plus term-wise comparison, which is exactly the source's argument).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.geom_sum_le_one_add_pow`

[A] Lean-Finder       "sum_{i=0}^n x^i ≤ (1+x)^n for x ≥ 0, binomial coefficients are at least one" → `pow_add_mul_le_add_pow`, `one_add_le_pow_of_two_add_nonneg`, `one_add_mul_le_pow'`, `one_add_mul_le_pow`, `add_pow_le`: all Bernoulli-type or other inequalities, no match
[B] Loogle            `∑ i ∈ Finset.range (_ + 1), ?x ^ i ≤ (1 + ?x) ^ _` → no hits; `Finset.sum, Finset.range, HPow.hPow, Nat.choose, LE.le` → no hits
[C] LeanSearch        "geometric sum of t^i for i up to n is at most (1+t)^n for nonnegative t" → `sum_geometric_two_le`, `Nat.geomSum_lt`, `Nat.geom_sum_le`, `geom_sum_alternating_of_le_neg_one`, `geom_sum_Ico_le_of_lt_one`: no match
[D] Grep mathlib src  `(1 \+ [a-z]) \^ [a-z]` lines also mentioning sum/geom → none; `(theorem|lemma) …geom_sum…le` → only the five `geom_sum` order lemmas in Algebra/Order/{Ring,Field}/GeomSum.lean and Algebra/Ring/GeomSum.lean, none of this shape; `one_add_pow|sum_range_pow_le|add_pow_le|pow_le_add_pow` → only `pow_add_pow_le`, `add_pow_le` (Algebra/Order/Ring/Basic.lean) and unrelated `tendsto_one_add_pow_exp…`
[E] Name pattern      grep for `geom_sum_le_one_add_pow` / `one_add_pow` under mathlib → no declaration

Searched for both the user's ℝ form and the ordered-semiring form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Building blocks: `add_pow`/`Commute.add_pow`, `Finset.sum_le_sum`, `Nat.choose_pos`.

### Normal-form check — `Roth.geom_sum_le_one_add_pow`

Equivalent formalisms: `∑ i ∈ range (n+1), x^i` (geom_sum convention, shifted) versus `∑ i ∈ range n, x^i ≤ (1+x)^(n-1)` (truncated subtraction, worse).
Does mathlib already have a canonical form? Mathlib's `geom_sum` lemmas use `∑ i ∈ range n, x ^ i`. With `range (n+1)` and exponent `n` the statement avoids `n - 1`, which is preferable. It is an inequality, not an ↔, so the RHS convention does not apply.
RHS convention respected? n/a (inequality)

### Syntactic generality — `Roth.geom_sum_le_one_add_pow`

Alternative restatements attempted:
- `∑ i ∈ range n, x^i ≤ (1+x)^(n-1)`: rejected: truncated subtraction `n - 1` is awkward to apply and needs a separate `n = 0` case
- `(1 + x)` versus `(x + 1)`: `1 + x` matches the source and the caller `(1 + |x j|)`
Chosen restatement: the current shape over an ordered semiring.
Justification: the caller supplies `abs_nonneg _` and `r j` directly with no rewriting.

### Superfluous-argument audit — `Roth.geom_sum_le_one_add_pow`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | ambient ring ℝ | no | any ordered semiring works (verified) |
| 2 | `ht : 0 ≤ t` | yes | counterexample at `t = -1/2` |
| 3 | `r` | yes | exponent |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (the ℝ specialisation, replaced by an ordered semiring)

Overall: RESTATE-BEFORE-SHIP (generalise the scalar ring)

### Call sites — `Roth.geom_sum_le_one_add_pow`

Internal use count: 1 (in the declaring file; no other file uses it)
External-to-file callers: 0

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:218 | `fun j _ ↦ geom_sum_le_one_add_pow (abs_nonneg (x j)) (r j)` inside `Finset.prod_le_prod₀` in private `sum_box_prod_pow_le_aux` |

Inline-derivation grep: `grep -rn "add_pow\|choose_pos" Roth/` found no other re-derivation of this inequality (none).

### Composition check (Phase 6)

Can `Roth.geom_sum_le_one_add_pow` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(add_pow t 1 r) ▸ Finset.sum_le_sum (fun m hm ↦ …)`
  - Mathlib decls used: `add_pow`, `Finset.sum_le_sum`, `le_mul_of_one_le_right`, `pow_nonneg`, `Nat.choose_pos`, `Nat.mono_cast`
  - Result: partial. It needs a commutation rewrite, a term-wise argument with a cast, and `one_pow`/`mul_one` cleanup, which makes it a 5-line proof rather than a composition.
Attempt 2: a Bernoulli-type lemma (`one_add_mul_le_pow`) only gives the first two terms `1 + r t`, so it fails.

Conclusion: NOT-COMPOSABLE (per the 6b heuristics this is a real proof, not a call chain)

## Verdict: `Roth.geom_sum_le_one_add_pow`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): a folklore binomial-theorem corollary, stated verbatim in the source (clean.tex l.1546, l.1567) and used implicitly in Roth–Ridout height estimates (arXiv math/0307203). Its natural generality is an ordered semiring.
- Generality analysis (Phase 4): STRICTLY NARROWER. ℝ generalises to `[Semiring R] [PartialOrder R] [IsOrderedRing R]`, verified clean in the evidence file.
- Mathlib search (Phase 5): not in mathlib in either form.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:** Mathlib has a small family of elementary power inequalities in ordered semirings: Bernoulli (`one_add_mul_le_pow`, `one_add_le_pow_of_two_add_nonneg`), `pow_add_pow_le` and `add_pow_le` in Mathlib/Algebra/Order/Ring/{Pow,Basic}.lean, plus order lemmas about geometric sums in Mathlib/Algebra/Order/Ring/GeomSum.lean. None of them compares a geometric sum with a binomial power. This lemma is the standard ingredient of the estimate `|P(α)| ≤ H(P) ∏ (1+|α|)^{deg}` used throughout Diophantine approximation. Today anyone needing it must redo the `add_pow`/`Finset.sum_le_sum`/`Nat.choose_pos` argument. The project's ℝ-only statement is a specialisation. The identical proof, with one cast line adjusted, compiles over any ordered semiring, including non-commutative ones via `Commute.one_right`, so the mathlib version should be the general one.

The concrete gap is that mathlib has no "geometric sum ≤ binomial power" lemma next to its geometric-sum order lemmas. The only competing route is a 5-line ad-hoc proof at each use site. The lemma has one current consumer (the private `sum_box_prod_pow_le_aux`), which is weak local demand, but the result is a general-purpose inequality whose natural home is mathlib rather than this project.

Reason for the generalisation: LITERATURE-WEAKENING (the ℝ form is strictly narrower than the ordered-semiring form)
Proposed restatement:
```lean
theorem geom_sum_le_one_add_pow {R : Type*} [Semiring R] [PartialOrder R] [IsOrderedRing R]
    {x : R} (hx : 0 ≤ x) (n : ℕ) :
    ∑ i ∈ Finset.range (n + 1), x ^ i ≤ (1 + x) ^ n := by
  rw [add_comm (1 : R) x, (Commute.one_right x).add_pow]
  refine Finset.sum_le_sum fun m hm ↦ ?_
  rw [one_pow, mul_one]
  refine le_mul_of_one_le_right (pow_nonneg hx m) ?_
  simpa using Nat.mono_cast (α := R) (Nat.choose_pos (Finset.mem_range_succ_iff.1 hm))
```
Estimated cost of regeneralisation: CHEAP (already compiled).
Proposed mathlib location: Mathlib/Algebra/Order/Ring/GeomSum.lean (it already imports the big-operators and ordered-ring API; `add_pow` lives in Mathlib/Algebra/BigOperators/... and may need an import check).
Proposed PR title: "feat(Algebra/Order/Ring/GeomSum): geometric sum is at most `(1 + x) ^ n`"
PR grouping: standalone. The related `Roth.abs_eval_le`, which uses it, has its own assessment.
Next action: run `/generalise Roth.geom_sum_le_one_add_pow` to confirm the ordered-semiring signature, apply it in Roth/CoeffNorm.lean (the caller at l.218 needs no change, since ℝ is an instance), then open the mathlib PR. Once merged, delete the project copy.

---

## Next step

Restate over `[Semiring R] [PartialOrder R] [IsOrderedRing R]` (proof in the evidence file) and PR it to Mathlib/Algebra/Order/Ring/GeomSum.lean. The single caller `Roth.sum_box_prod_pow_le_aux` (Roth/CoeffNorm.lean:218) then switches to the mathlib lemma with no argument changes.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.geom_sum_le_one_add_pow/weaken.lean` (imports `Roth.CoeffNorm`). It contains the commutative and non-commutative ordered-semiring versions, the ℝ specialisation as a one-line term, and the `t = -1/2` counterexample by `norm_num`. `lean_diagnostic_messages` reports no errors. The first attempt with `exact_mod_cast Nat.choose_pos` failed over general `R` (no `CharZero`) and was fixed with `Nat.mono_cast`.
- Searches: Loogle ×2, LeanSearch ×1, Lean-Finder ×1, WebSearch ×3, mathlib grep ×3 (all recorded above); local reference grep of clean.tex.
- `grep -rn geom_sum_le_one_add_pow Roth/` gives l.205 and l.218 only.
