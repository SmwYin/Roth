---
decl: Roth.pigeonhole_count
file: Roth/MainLemma.lean
line: 334
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Ad-hoc counting inequality (2 natfloor(B^c)+1)^(nD) < (B+1)^N under B > 0, c at least 1, N > 0, c n D at most N/2 from the Lemma 9 pigeonhole (source §6); all four hypotheses necessary (compiled counterexamples) and already weaker than the source's B_1 > 1, c > 1; no literature standing, no mathlib counterpart (mathlib's own Siegel lemma keeps its analogous count card_S_lt_card_T private), not a 3-call composition; recommended resolution is keep project-local.
action: Keep Roth.pigeonhole_count in Roth/MainLemma.lean (single caller, private exists_mem_RSet_le_index_of_rpow_bound_aux at l.615); optionally make it private together with floor_rpow_count_lt_aux; no mathlib PR.
---

# Roth.pigeonhole_count

## Inventory entry

### `theorem Roth.pigeonhole_count`
- **Type**: `∀ {B : ℝ}, 0 < B → ∀ {c : ℝ}, 1 ≤ c → ∀ {n D N : ℕ}, 0 < N → c * ↑n * ↑D ≤ ↑N / 2 → ((2 * ⌊B ^ c⌋₊ + 1 : ℕ) : ℝ) ^ (n * D) < (B + 1) ^ N`
- **What**: For real `B > 0`, real `c ≥ 1`, naturals `n, D, N` with `N > 0` and `c n D ≤ N/2`, the number of remainder tuples `(2⌊B^c⌋ + 1)^{nD}` is strictly less than `(B + 1)^N` (the size of the box family when `B` is a natural number).
- **How**: Case `n * D = 0`: both sides reduce to `1 < (B+1)^N`, closed by `one_lt_pow₀`. Otherwise a three-step `calc`: `pow_lt_pow_left₀` applied to the private per-factor bound `floor_rpow_count_lt_aux` (`2⌊B^c⌋+1 < (B+1)^{2c}`), then `Real.rpow_mul_natCast` to merge exponents, then `Real.rpow_natCast` and `Real.rpow_le_rpow_of_exponent_le` with `linarith only [hD]` for `2c·nD ≤ N`.
- **Hypotheses**: `hB : 0 < B` (necessary, fails at `B = 0`); `hc : 1 ≤ c` (cannot be dropped, fails at `c = 1/2`; not sharp, any valid threshold exceeds `log 3 / log 4`); `hN : 0 < N` (necessary, fails at `n = D = N = 0`); `hD : c n D ≤ N / 2` (necessary). All checked in the evidence file.
- **Uses from project**: `Roth.floor_rpow_count_lt_aux` (private)
- **Used by**: Roth/MainLemma.lean:615 (private `exists_mem_RSet_le_index_of_rpow_bound_aux`, supplying the `hcount` argument of `exists_mem_RSet_le_index_aux`); listed in the module docstring l.43. No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 329–351 (docstring 329–333, statement 334–335, proof 336–351, proof length 16 lines)
- **Notes**: Source clean.tex §6 l.1480–1500 (`(1+2B_1^c)^{nD} < [2(1+B_1)]^{cnD} ≤ [2(1+B_1)]^{r/2} < (1+B_1)^r`). The Lean proof bypasses the source's intermediate `Y = 2(1+B)` by bounding each factor by `(B+1)^{2c}` directly (comment l.337–339). Lean hypotheses (`B > 0`, `c ≥ 1`) are weaker than the source's (`B_1 > 1`, `c > 1`).

## Junk check (Step 8)
- **Used anywhere?** Yes, once (l.615), in the Lemma 9 construction chain.
- **Wrapper of 1–2 mathlib calls?** No. It is a case split plus a 3-step calc over a private nonlinear helper.
- **Does mathlib have it?** No. LeanFinder returned only Behrend/Bertrand explicit inequalities; LeanSearch returned `Int.Matrix.exists_ne_zero_int_vec_norm_le` (Siegel's lemma) and double-counting lemmas; Loogle returned nothing. Mathlib's own Siegel lemma proof has the analogous count `card_S_lt_card_T` (Mathlib/NumberTheory/SiegelsLemma.lean:117) as a `private` lemma.
- **Too specific (inline?)?** It is proof-specific, but it isolates exactly the counting step of the pigeonhole; inlining into the 30-line caller would hurt readability. It could be `private`.
- **Well-chosen?** Yes. The statement takes real `B` so that natural coefficient bounds specialise by coercion, and uses minimal hypotheses.
- Conclusion: `KEEP`. Action: keep; optionally make private.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name has no `_aux`; docstring does not start internal/auxiliary; Step 8 KEEP; `grep -rn pigeonhole_count .lake/packages/mathlib/Mathlib` empty. It has a real 16-line proof, so it is not a glue lemma, and INHERITED does not apply. Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; the evidence file importing `Roth.MainLemma` compiles with no output)
- decl `Roth.pigeonhole_count`: ✓ resolved at Roth/MainLemma.lean:334
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's main lemma (Lemma 9 of the source): auxiliary polynomial construction via a pigeonhole/box argument with explicit coefficient bounds.

### Statement (Phase 1)

`Roth.pigeonhole_count` is a theorem stating the following. Let `B > 0` and `c ≥ 1` be real, and let `n, D, N` be natural numbers with `N ≥ 1` and `c n D ≤ N/2`. Then

  `(2⌊B^c⌋ + 1)^{nD} < (B + 1)^N`.

In the proof of Lemma 9, the left side counts the possible tuples of remainder coefficients (each in `[-⌊B^c⌋, ⌊B^c⌋]`, `nD` of them), and the right side is `|𝒲|`, the number of box polynomials; the inequality is what makes the pigeonhole principle apply.

Variables (Lean side):
- `B : ℝ` — coefficient bound of the box family.
- `c : ℝ` — exponent in the remainder coefficient bound `B^c`.
- `n D N : ℕ` — degree of `f`, number of selected Hasse derivatives, number of monomials.

Hypotheses (Lean side):
- `hB : 0 < B`
- `hc : 1 ≤ c`
- `hN : 0 < N`
- `hD : c * n * D ≤ N / 2`

Conclusion (math): `(2⌊B^c⌋+1)^{nD} < (B+1)^N`.

Conclusion (Lean): `((2 * ⌊B ^ c⌋₊ + 1 : ℕ) : ℝ) ^ (n * D) < (B + 1) ^ N`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an internal counting estimate in the proof of Lemma 9; not a structure, not a main result of the paper, not a named theorem (listed among the file's main results only as part of "the pigeonhole step").

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 16
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE

### Literature search table

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof auxiliary polynomial pigeonhole "1+2B^c" (1+B)^r number of remainders count Siegel lemma | partial | Roth-proof expositions (arXiv 2502.00731, math.uh.edu roth.pdf, Evertse Luminy notes) use a box-count pigeonhole step | no standalone statement of this inequality; constants are exposition-specific |
| 2 | WebSearch (general form) | Siegel's lemma pigeonhole principle box count (2H+1)^M < (B+1)^N condition N > 2M | yes | Siegel's lemma proof: `(B+1)^N` box points versus a smaller number of image values (Wikipedia "Siegel's lemma"; math.uh.edu roth.pdf) | the counting comparison is a proof step, never a stated lemma |
| 3 | WebSearch (aliases) | Dirichlet box principle counting inequality integer vectors bounded coefficients Thue-Siegel auxiliary polynomial | yes | Thue–Siegel lemma via Dirichlet's box principle (Waldschmidt arXiv 0908.4024; arXiv 2303.02037 Lemma 2.4 with `N > 2M`, count `(2NH+1)^N`) | same pattern: count inequality inside the proof |
| 4 | ChatGPT MCP | n/a | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `1+2B_1^c` | yes | l.1480–1500: `(1+2B_1^c)^{nD} < [2(1+B_1)]^{cnD} ≤ [2(1+B_1)]^{r/2} < (1+B_1)^r = |𝒲|` with `c = 1+3δ > 1`, `B_1 > 1` | source of the statement |
| 6 | nLab | pigeonhole principle / Siegel's lemma | no | — | nLab has no entry for proof-internal Diophantine counting estimates |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry statement |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | routine counting bookkeeping is not discussed as a result |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), arXiv 2303.02037 (2023) | partial | each uses its own counting inequality with its own constants | no common named form |

### Literature summary (Phase 3)

Concept identified as: the counting comparison in a Dirichlet box principle / Siegel's lemma argument ("fewer pigeonholes than pigeons"), here the specific estimate `(1+2B^c)^{nD} < (1+B)^r` of Roth's Lemma 9.
Sources agree on the standard form: no; it is never stated standalone. Every exposition proves its own count inline with its own constants.
Most general standard form: none. The underlying principle (pigeonhole, `Fintype.exists_ne_map_eq_of_card_lt`) is in mathlib; the arithmetic is case-specific.
Generality dimensions where the literature varies: the constants (`2B^c+1`, `c`, the factor `1/2`) only.
Disagreement with the literature: none. The Lean proof uses a direct per-factor bound `(B+1)^{2c}` instead of the source's `[2(1+B)]^c` and weaker hypotheses (`B > 0`, `c ≥ 1` instead of `B > 1`, `c > 1`); same conclusion.

### Generality analysis — `Roth.pigeonhole_count`

Literature-standard form (from Phase 3): none; the source states it for `B_1 > 1` integer, `c > 1`, `cnD ≤ r/2`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|------------------------|-------------------|--------------------------|---------------------|---------------------------------|
| 1 | `hB : 0 < B` | `B > 0`, real | `B_1 > 1`, integer | no (already weaker than source) | `B = 0`, `c = 1`, `n = D = 1`, `N = 2` gives `1 < 1` (compiled counterexample) |
| 2 | `hc : 1 ≤ c` | `c ≥ 1` | `c > 1` | no meaningful one | `B = 1`, `c = 1/2`, `n = D = N = 1` gives `3 < 2` (compiled); the exact threshold lies between `log 3/log 4 ≈ 0.79` and `1` and has no meaning |
| 3 | `hN : 0 < N` | `N > 0` | implicit (`r ≥ 1`) | no | `n = D = N = 0` gives `1 < 1` (compiled) |
| 4 | `hD : c n D ≤ N / 2` | `≤ N/2` | `≤ r/2` | no | `B = c = 1`, `n = D = N = 1` gives `3 < 2` (compiled) |
| 5 | `B : ℝ` | real | integer | no (already more general) | natural bounds specialise by coercion (as at the call site l.615) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. Every hypothesis is necessary (compiled counterexamples in evidence/Roth.pigeonhole_count/necessity.lean); `hB`, `hc` and the type of `B` are already weaker/more general than the source.
Number of weakening opportunities found: 0.
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|----------|----------|------------------------|----------------------------------|
| 1 | preambles to typeclasses? | no | only numeric hypotheses | — |
| 2 | sequences to filters? | no | finite inequality | — |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | `Real.rpow` and `Nat.floor` of a real power force ℝ | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | naturals index powers | — |
| 8 | concrete-via-abstract? | partly | the only concrete content is the per-factor bound; abstracting to "if `a < b^{2c}`, `a ≥ 0`, `b ≥ 1`, `2ckc ≤ N` then `a^k < b^N`" is just `pow_lt_pow_left₀` plus rpow monotonicity, too thin to be a mathlib lemma | none |
| 9 | false-generalisation guard | n/a | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: an explicit numeric counting inequality with exposition-specific constants; its abstract core is already a two-lemma mathlib composition.

### Proof strategy — `Roth.pigeonhole_count`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|------------------------|----------------|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | all ingredients present (`pow_lt_pow_left₀`, `Real.rpow_mul_natCast`, `Real.rpow_natCast`, `Real.rpow_le_rpow_of_exponent_le`, `one_lt_pow₀`, and in the helper `Real.add_rpow_le_rpow_add`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. A calc over standard rpow lemmas; shorter than the source's three-step chain via `Y = 2(1+B)`.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.pigeonhole_count`

- [A] Lean-Finder: "(2 * floor(B^c) + 1)^(n*D) < (B+1)^N when c*n*D ≤ N/2, B > 0, c ≥ 1" → `Behrend.le_N`, `Behrend.bound`, `bertrand_main_inequality`, `Behrend.three_le_nValue`, `Behrend.roth_lower_bound_explicit`; none matches.
- [B] Loogle: `(_ : ℝ) ^ (_ : ℕ) < (_ + 1) ^ (_ : ℕ), Nat.floor` → no hits.
- [C] LeanSearch: "counting inequality for Siegel lemma: (2 floor(B^c)+1)^k < (B+1)^N if 2 c k ≤ N" → `Int.Matrix.exists_ne_zero_int_vec_norm_le(')` (Siegel's lemma), `Finset.card_nsmul_lt_card_nsmul_of_*` (double counting); none matches.
- [D] Grep mathlib source: `pigeonhole_count`, `floor_rpow` → no hits. Inspected Mathlib/NumberTheory/SiegelsLemma.lean: its analogous count `card_S_lt_card_T` (l.117) is `private`.
- [E] Name pattern: `pigeonhole_count` is project-only (grep [D]).

Searched for both the exact form and the generic "box count in Siegel's lemma" form. Concluded: found building blocks (`pow_lt_pow_left₀`, `Real.rpow_mul_natCast`, `Real.rpow_le_rpow_of_exponent_le`, `Real.add_rpow_le_rpow_add`, `Nat.floor_le`); the statement is not in mathlib.

### Normal-form check — `Roth.pigeonhole_count`

Equivalent formalisms: (a) the current real form with `(… : ℕ) : ℝ` cast on the left; (b) a natural-number form with `B : ℕ` and `Nat` powers; (c) hypothesis `2 * c * n * D ≤ N` instead of `≤ N / 2`.
Mathlib has no canonical form (not a mathlib concept). Form (a) is what the caller needs: the `hcount` argument of `exists_ne_modByMonic_eq` is stated in ℝ.
RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.pigeonhole_count`

Alternative restatements attempted: (b) natural `B` (more specialised, would need a cast at the per-factor rpow step anyway); (c) `2cnD ≤ N` (equivalent).
Chosen restatement: current.
Justification: `hD` in the form `c * n * D ≤ N / 2` is produced verbatim by `mul_card_filter_weight_le_aux` at the call site (l.611–612), and real `B` covers natural `B` by coercion.

### Superfluous-argument audit — `Roth.pigeonhole_count`

| # | Argument | Essentially used? | Notes |
|---|----------|-------------------|-------|
| 1 | `hB` | yes | counterexample at `B = 0` compiled |
| 2 | `hc` | yes | counterexample at `c = 1/2` compiled |
| 3 | `hN` | yes | counterexample at `n = D = N = 0` compiled (only needed when `nD = 0`, but then it is needed) |
| 4 | `hD` | yes | counterexample at `B = c = n = D = N = 1` compiled |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.pigeonhole_count`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|------------------|----------------------------------|
| Roth/MainLemma.lean:615 (private `exists_mem_RSet_le_index_of_rpow_bound_aux`) | `(pigeonhole_count (Nat.cast_pos.2 hB) hc (Finset.prod_pos fun j _ ↦ Nat.succ_pos _) hD)` as the `hcount` argument of `exists_mem_RSet_le_index_aux` |

Inline-derivation grep: none (no other `⌊_ ^ _⌋₊` count comparisons in `Roth/`).

### Composition check (Phase 6)

Can `Roth.pigeonhole_count` be derived from mathlib in ≤3 chained calls?

Attempt 1: `pow_lt_pow_left₀ h₁ _ hk |>.trans_le (rpow monotonicity)` with `h₁ : 2⌊B^c⌋+1 < (B+1)^{2c}`.
- Mathlib decls used: `pow_lt_pow_left₀`, `Real.rpow_mul_natCast`, `Real.rpow_le_rpow_of_exponent_le`.
- Result: partial. `h₁` itself is not in mathlib; it needs `Real.add_rpow_le_rpow_add`, `Real.rpow_mul`, `Real.rpow_two`, `Nat.floor_le` and `nlinarith` (the private helper). The `nD = 0` case needs a separate `one_lt_pow₀`.

Attempt 2: `nlinarith`/`positivity` directly.
- Result: fails; rpow terms need explicit rewriting first.

Conclusion: NOT-COMPOSABLE (in the ≤3-call sense).

### Verdict: `Roth.pigeonhole_count`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the estimate appears only as an internal step of the proof of Lemma 9 (clean.tex l.1480–1500); Siegel-lemma and Thue-Siegel expositions all prove their own counting comparison inline with their own constants.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; all four hypotheses necessary (compiled counterexamples) and already weaker than the source.
- Mathlib search (Phase 5): building blocks only; mathlib's own Siegel lemma keeps its analogous count private.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

This is the "fewer pigeonholes than pigeons" arithmetic of the Lemma 9 box argument. The NO buckets do not fit: mathlib does not have the statement, and it needs a nonlinear per-factor bound (superadditivity of `t ↦ t^c`, a floor bound and `nlinarith`) plus a case split and rpow exponent manipulation, which is a real proof rather than a ≤3-call composition. The YES buckets do not fit either: its constants (`2⌊B^c⌋+1`, the factor `1/2`) are specific to this exposition, the literature never states it standalone, and mathlib's precedent for exactly this kind of step (`card_S_lt_card_T` in Mathlib/NumberTheory/SiegelsLemma.lean:117) is a `private` lemma next to the theorem it serves. Its abstract core (`a < b^{2c}` implies `a^k < b^N` when `2ck ≤ N`) is too thin to be worth a mathlib lemma.

BORDERLINE by elimination, consistent with the sibling numeric reports (`Roth.four_lt_rpow`, `Roth.lem7_numeric`, `Roth.sqrt_lt_floor`). The practical recommendation is clear: keep it in the project.

Numbered questions:
1. Keep `Roth.pigeonhole_count` project-local and never upstream it on its own? (Recommended: yes.)
2. Make it `private` (with its helper `floor_rpow_count_lt_aux`), given its only caller (l.615) is private? It is currently listed under "Main results" in the module docstring (l.43), so this is a project-API choice. (Recommended: optional.)

Next action: the user answers the questions. Default is no change: keep the theorem in Roth/MainLemma.lean with its single call site at l.615.

---

### Next step

Keep `Roth.pigeonhole_count` in Roth/MainLemma.lean; optionally make it private. Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.pigeonhole_count/necessity.lean` (imports `Roth.MainLemma`): `lake env lean` compiled it clean with no output in 41 s. It proves the conclusion fails, with the other hypotheses holding, at `B = 0` (hB), at `B = 1`, `c = 1/2` (hc), at `n = D = N = 0` (hN), and at `B = c = n = D = N = 1` without hD; plus a sanity instantiation of the original theorem at `B = 3`, `c = 1`, `n = 2`, `D = 1`, `N = 4`.
- Mathlib greps: `pigeonhole_count`, `floor_rpow` (no hits); SiegelsLemma.lean inspected (`card_S_lt_card_T` private, l.117).
- LeanFinder (1), LeanSearch (1), Loogle (1, no hits): see Phase 5.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local reference: clean.tex l.1480–1500.
- Project grep `grep -rn pigeonhole_count Roth/`: l.43 (docstring), l.334 (decl), l.615 (only use).
