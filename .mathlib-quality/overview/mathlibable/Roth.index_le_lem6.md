---
decl: Roth.index_le_lem6
file: Roth/Theta.lean
line: 556
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The pointwise form of Roth's Lemma 6 (ind(R; h/q; r) ≤ 2(Φ + √Φ + √δ) for some 1 ≤ l ≤ r_p+1, for R ∈ ℛ_p(B; r)); it assembles six project lemmas (exists_det_eq_mul, sum_max_sub_le_index_det, index_det_le, min_le_sum_max and two private aux lemmas) about project-only notions (Roth.index, RSet, Θ, lem6Φ, lem6M), so it has no mathlib counterpart and is not a ≤3-call mathlib composition, while as an internal step of Roth's lemma it has no standalone literature standing; recommended resolution is to keep it in the project.
action: Keep in Roth/Theta.lean (single caller Roth.Θ_option_le at Roth/Theta.lean:600); optionally drop the unused hypothesis _hq (compiled in evidence/Roth.index_le_lem6/weaken_hq.lean) and update that call site; optionally make it private; do not upstream.
---

# Roth.index_le_lem6

## Inventory entry

### `theorem Roth.index_le_lem6`
- **Type**: `{τ : Type*} [Fintype τ] {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (_hq : ∀ j, 0 < q j) {B : ℝ} {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ 2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l + √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ)`
- **What**: Lemma 6 of the source (clean.tex §5, Lemma `roth:lem6`, l.704–) for a single polynomial and point: if `R ∈ ℛ_p(B; r)`, `r_p ≥ 3`, `r_p ≤ δ r_j` for `j < p`, `r_j ≤ r₁`, and `gcd(h_j, q_j) = 1`, then for some `1 ≤ l ≤ r_p + 1`, `ind(R; h/q; r) ≤ 2(Φ + Φ^{1/2} + δ^{1/2})` with `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q'; l r')`, `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`.
- **How**: Obtain `l`, `D`, `U`, `V` with the generalised Wronskian `F = U(x') V(x_p)` from `Roth.exists_det_eq_mul` (Lemma 2); lower bound `∑_{ν<l} max(0, ind R − ν/r_p) − lδ ≤ ind F` from `Roth.sum_max_sub_le_index_det` (with private `mapped_det_ne_zero_aux`, `weight_le_delta_aux`); upper bound `ind F ≤ lΦ` from `Roth.index_det_le` (eq. (17)); combine with `Roth.min_le_sum_max` and conclude with the private numeric lemma `index_numeric_bound_aux` (case split on the `min`).
- **Hypotheses**: `hδ0`, `hδ1`, `hrp`, `hratio` (weight comparisons, used for `r j > 0` and the weight-≤-δ bound); `hr₁` (uniform degree bound for Lemma 3 via `index_det_le`); `hR` (Lemma 2 needs `R ≠ 0` and the degree bounds); `hh` (coprimality for `index_le_Θ`); `_hq` (positivity of the `q j`) is **unused** — see evidence.
- **Uses from project**: `Roth.RSet`, `Roth.index` (Roth/Index.lean:58), `Roth.Θ_nonneg`, `Roth.lem6Φ`, `Roth.lem6M`, `Roth.exists_det_eq_mul` (Roth/Separation.lean:542), `Roth.sum_max_sub_le_index_det` (Theta.lean:376), `Roth.mapped_det_ne_zero_aux` (Theta.lean:511, private), `Roth.weight_le_delta_aux` (Theta.lean:494, private), `Roth.index_det_le` (Theta.lean:457), `MvPolynomial.hasseDeriv_map` (Roth/HasseDeriv.lean:134), `Roth.index_numeric_bound_aux` (Theta.lean:531, private), `Roth.min_le_sum_max` (Theta.lean:362)
- **Used by**: `Roth.Θ_option_le` (Roth/Theta.lean:600, `obtain ⟨l, hl, hl', hle⟩ := index_le_lem6 hδ0 hδ1 hrp hratio hr₁ hq hR hh`). No other occurrence in `Roth/` or `Roth.lean`. Transitively feeds Lemma 7 via `Θ_option_le` (Theta.lean:920).
- **Visibility**: public
- **Lines**: 551–587 (docstring 551–554, statement 556–563, proof 564–587), proof length 24 lines
- **Notes**: `omit [DecidableEq τ] in` precedes it. `_hq` is unused (named with underscore; the comment "Retain the paper's positive-denominator setting" explains it is kept to mirror the source). Single caller.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.Θ_option_le` (Theta.lean:600), on the main path to Lemma 7 and Roth's theorem.
- Wrapper of 1–2 mathlib calls? No; it chains six project lemmas over 24 lines.
- Does mathlib have it? No (Phase 5): mathlib has no Roth index, `Θ`, `RSet` or generalised Wronskian.
- Too specific (inline?)? It is the per-point core of Lemma 6, exactly the sentence "We need to show that the index ... is bounded by the right hand side of (13)"; inlining into `Θ_option_le` is possible but would merge two clearly separated source steps. Keep as a named lemma.
- Well-chosen? Yes; minor: `_hq` is redundant.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring does not start with internal/auxiliary; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `index_le_lem6`, `lem6Φ`, `namespace Roth`: no hit. Not a glue lemma (24-line proof), so the full workflow follows. Parent defs `Roth.index`, `Roth.lem6Φ`, `Roth.lem6M`, `Roth.RSet` are not NO-mathlib-has-it, so no re-aim.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` compiles, exit 0)
- decl `Roth.index_le_lem6`: resolved at Roth/Theta.lean:556
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index across sets of polynomials `Θ_m(B; q; r)` and Lemmas 5, 6, 7 of the source

### Statement (Phase 1)

`Roth.index_le_lem6` is a theorem stating the following:

Let `0 ≤ δ ≤ 1`, and let `r_1, …, r_p` be positive weights with `r_p ≥ 3`, `r_p ≤ δ r_j` for `j < p`, and all `r_j ≤ r₁`. Let `R ∈ ℤ[x_1, …, x_p]` be nonzero with `deg_{x_j} R ≤ r_j` and coefficients bounded by `B`, and let `h_j/q_j` be rationals in lowest terms. Then there is an integer `1 ≤ l ≤ r_p + 1` with `ind(R; h_1/q_1, …, h_p/q_p; r) ≤ 2(Φ + Φ^{1/2} + δ^{1/2})`, where `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1})` and `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`.

Variables / typeclasses involved (Lean side):
- `τ` with `[Fintype τ]`: the first `p−1` variables; `Option τ`: all `p` variables, `none = x_p`.
- `δ`, `r`, `r₁`: the small parameter, the weights, their maximum; `q`, `h`: the point; `B`: coefficient bound; `R`: the polynomial.

Hypotheses (Lean side):
- `hδ0`, `hδ1`: `0 ≤ δ ≤ 1`. `hrp`: `r_p ≥ 3`. `hratio`: `r_p ≤ δ r_j`. `hr₁`: `r_j ≤ r₁`.
- `_hq`: `q_j > 0` (unused). `hR`: `R ∈ ℛ_p(B; r)`. `hh`: `gcd(h_j, q_j) = 1`.

Conclusion (math): `∃ l ∈ [1, r_p+1], ind(R; h/q; r) ≤ 2(Φ_l + √Φ_l + √δ)`.

Conclusion (Lean): `∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ 2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l + √(lem6Φ …) + √δ)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the per-polynomial form of an intermediate lemma (Lemma 6) of Roth's proof, not a main result or a new structure; the named result `Θ_option_le` is its one-line consequence.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 24 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma index of polynomial at rational point bounded Theta induction generalized Wronskian proof | partial | Roth's lemma proved by induction on the number of variables using the generalised Wronskian | arXiv 2502.00731 (Lemma 3.9, Lemma 2.24), arXiv 1305.0926, arXiv math/0307203 (Ridout's form of Roth's Lemma 7); the inductive step is always inline, never isolated as a lemma |
| 2 | WebSearch (general form) | index of a polynomial at a point weighted order of vanishing upper bound polynomial bounded height Diophantine approximation | partial | auxiliary-polynomial method: upper bounds on (weighted) orders of vanishing at a point for polynomials of bounded height | alg-geom/9608010, Bonn polynomial-methods handout; no general statement of this Θ-recursion |
| 3 | WebSearch (aliases) | "Roth's lemma" statement index small coefficients degrees rapidly decreasing | yes (for the final lemma) | Roth's lemma: `ind ≤ 2mη` (2502.00731 Lemma 3.9), `ind < mε` (Evertse slides, Roth 1955); constants vary by source | only the end statement (Lemma 7 analogue) is standard; the Lemma 6 recursion `Θ_p ≤ 2 max_l(Φ + Φ^{1/2} + δ^{1/2})` is Roth/Cassels-specific |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | read clean.tex l.700–790 (Lemma `roth:lem6` and proof) | yes | statement (13), (15), (16); proof begins "We need to show that the index ... is bounded by the right hand side of (13)" | the Lean statement is exactly this per-point claim, with `r_p > 10/δ`, `r_{j-1}/r_j > 1/δ` relaxed to `r_p ≥ 3`, `r_p ≤ δ r_j` |
| 6 | nLab | index of a polynomial; Roth's theorem | no | n/a | no entry on Roth's index or Roth's lemma |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Diophantine estimate, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread isolating this step |
| 10 | recent arXiv | 2502.00731, 1806.10737, math/0307203 | partial | as #1, #3 | inductive step of Roth's lemma proved inline |

### Literature summary (Phase 3)

Concept identified as: the inductive step of Roth's lemma (Lemma 6 of the source, after Cassels' exposition), stated for one polynomial and one point.
Sources agree on the standard form: only on the final Roth lemma (index small for polynomials of small height at points of large height); the Θ-recursion and its constants are presentation-specific.
Most general standard form: Roth's lemma itself (`ind(P; ξ; r) ≤ 2mη` under rapidly decreasing weights and large heights), proved by induction via the generalised Wronskian.
Generality dimensions where the literature varies:
  - point: rational (this source) vs algebraic (2502.00731, Bombieri–Gubler).
  - height: max-coefficient vs absolute logarithmic height.
  - constants: source-specific.
Disagreement with the literature: none; the Lean hypotheses are weaker than the source's (`r_p ≥ 3` instead of `r_p > 10/δ`; `δ ≤ 1` closed).

### Generality analysis — `Roth.index_le_lem6`

Literature-standard form: clean.tex Lemma 6, per point.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `_hq : ∀ j, 0 < q j` | positive denominators | positive integers `q_j` | yes | unused by the proof; dropped and compiled in evidence (1) |
| 2 | `hrp : 3 ≤ r none` | `r_p ≥ 3` | `r_p > 10/δ` | already weaker | needed by `index_numeric_bound_aux` (`3l ≤ 4 r_p` from `l ≤ r_p + 1`) |
| 3 | `hratio` | `r_p ≤ δ r_j` | `r_{j-1}/r_j > 1/δ` | already weaker | only the comparison with `r_p` is used (weight ≤ δ bound) |
| 4 | `hδ0`, `hδ1` | `0 ≤ δ ≤ 1` | `0 < δ < 1` | already weaker | `hδ1` for `δ ≤ √δ`; `hδ0` for positivity of weights |
| 5 | `hr₁` | `r_j ≤ r₁` | `r_1 > … > r_p` | already weaker | uniform bound for Lemma 3 |
| 6 | `hR` | `R ∈ ℛ_p(B; r)` | same | no | `R ≠ 0` needed by Lemma 2 (`exists_det_eq_mul`) |
| 7 | `hh` | coprime | same | no | needed by `index_le_Θ` inside `index_det_le` |
| 8 | rational point over ℤ | fixed | algebraic points in the general Roth lemma | no (here) | Θ is defined over rational points; changing it is a redesign of the development, not a mechanical edit |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (up to the cosmetic removal of the unused `_hq`, verified in evidence (1))
Number of weakening opportunities found: 1 (verified: `lake env lean` on evidence/Roth.index_le_lem6/weaken_hq.lean exits 0)
Proposed restatement: drop `_hq`; update the call site Theta.lean:600 (`index_le_lem6 hδ0 hδ1 hrp hratio hr₁ hR hh`).
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | numeric data-level hypotheses | — |
| 2 | Sequences vs filters? | no | finite algebraic/real inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | `RSet` is a set of bounded polynomials, nothing to bundle | — |
| 5 | Field-specific vs typeclass-weakened? | no | integrality is essential (Gauss lemma, `Int.one_le_abs`) | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | the `Option τ` split (last variable vs rest) is the induction structure | — |
| 8 | Concrete-via-abstract? | partially | the proof is "lower bound + upper bound + numeric lemma"; the concrete Wronskian enters through the two bound lemmas, which are already separate | already factored (`sum_max_sub_le_index_det`, `index_det_le`, `index_numeric_bound_aux`) |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific inequality with paper-specific constants about project definitions; its reusable pieces are already separate lemmas.

### Proof strategy — `Roth.index_le_lem6`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no (directly) | the needed API (multivariate Hasse derivatives, generalised Wronskian, Roth index) is project-level and assessed in its own reports | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (mirrors the source: Lemma 2 factorisation, lower bound, eq. (17), numeric conclusion; each step a named lemma)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_le_lem6`

[A] Lean-Finder       "index of a multivariate integer polynomial at a rational point is bounded (Roth's lemma)"   hits: `ChevalleyThm.MvPolynomialC.numBound`, `one_le_pow_mul_abs_eval_div` (Liouville-type lower bound); nothing on a Roth index
[B] Loogle            `MvPolynomial, Matrix.det, Real.sqrt`   no hits
[C] LeanSearch        "Roth lemma index of polynomial with small coefficients at rational point is small"   hits: `one_le_pow_mul_abs_eval_div`, `Behrend.roth_lower_bound`, `rothNumberNat` (unrelated Roth number)
[D] Grep mathlib src  `index_le_lem6`, `lem6Φ`, `namespace Roth`   no hits
[E] Name pattern      `Roth.index_le_lem6`   only the project declaration

Searched for both:
  - the user's current form (per-point Lemma 6)
  - the literature-standard form (Roth's lemma / index bound for small-height polynomials)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form).

### Normal-form check — `Roth.index_le_lem6`

Equivalent formalisms: (a) `∃ l ∈ [1, r_p+1], index ≤ 2(Φ_l + √Φ_l + √δ)`; (b) `index ≤ 2 max_l (…)` (this is what `Θ_option_le` does after taking the sup).
Does mathlib already have a canonical form? no.
Proposed canonical form: current (existential witness; the max form is derived in the caller).
RHS convention respected? yes (upper bound with `index` on the LHS, matching `index_le_Θ`)

### Syntactic generality — `Roth.index_le_lem6`

Alternative restatements attempted:
- current (with `_hq`)
- without `_hq` (evidence (1), compiles; original recovered in one line, evidence (2))
- `max`-over-`l` form: rejected, it is exactly `Θ_option_le`'s job

Chosen restatement: drop `_hq` (otherwise current).
Justification: one fewer argument to supply at the call site; nothing else changes.

### Superfluous-argument audit — `Roth.index_le_lem6`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype τ]` | yes | `Roth.index`, `Fintype.card τ` |
| 2 | `[DecidableEq τ]` | no | already omitted |
| 3 | `_hq` | no | unused (evidence (1)) |
| 4 | `hδ0`, `hδ1`, `hrp`, `hratio`, `hr₁`, `hR`, `hh` | yes | each used in the proof |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (`_hq`)

Overall: RESTATE-BEFORE-SHIP (locally: drop `_hq`)

### Call sites — `Roth.index_le_lem6`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:600 | `obtain ⟨l, hl, hl', hle⟩ := index_le_lem6 hδ0 hδ1 hrp hratio hr₁ hq hR hh` in `Roth.Θ_option_le` |

Inline-derivation grep:
  - (none) — no other site re-derives the per-point Lemma 6 bound.

### Composition check (Phase 6)

Can `Roth.index_le_lem6` be derived from mathlib in ≤3 chained calls?

Attempt 1: `exists_det_eq_mul` + `sum_max_sub_le_index_det` + `index_det_le` + `min_le_sum_max` + `index_numeric_bound_aux`.
  - Decls used: all project lemmas (none in mathlib).
  - Result: fails as a mathlib composition; five project lemmas plus two private helpers and `simp` bookkeeping.

Attempt 2: mathlib-only.
  - Result: fails; mathlib has no Roth index, Θ, Hasse-derivative Wronskian or Roth lemma.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.index_le_lem6`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the statement is the per-point content of Lemma 6 of the source (clean.tex l.704–) and the inductive step of Roth's lemma; the literature states only the final Roth lemma standalone.
- Generality analysis (Phase 4): MAXIMALLY GENERAL up to one unused hypothesis (`_hq`), verified in evidence (1).
- Mathlib search (Phase 5): not in mathlib.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The theorem is a paper-specific inequality with paper-specific constants (`lem6M`, `lem6Φ`) about the project's own `Roth.index`, `RSet` and `Θ`, with one caller (`Θ_option_le`). It does not fit a YES bucket: it has no standalone literature standing and fills no mathlib gap by itself (mathlib's Diophantine-approximation library would first need the Roth index, Hasse-derivative Wronskians and Lemma 2, all assessed as BORDERLINE in their own reports). It does not fit a NO bucket: mathlib does not have it and it is not a ≤3-call mathlib composition. Like its siblings `Roth.index_det_le`, `Roth.sum_max_sub_le_index_det`, `Roth.min_le_sum_max` and `Roth.exists_det_eq_mul`, it is BORDERLINE, with a clear recommendation to keep it project-local.

It would become relevant to mathlib only as part of a full Roth-theorem upstreaming plan (policy question, EXPENSIVE). Locally, the unused `_hq` can be dropped at no cost.

Numbered questions:
1. Keep `Roth.index_le_lem6` project-local in Roth/Theta.lean (recommended: yes)?
2. Drop the unused `_hq` and update the call site Theta.lean:600? The source-fidelity comment argues for keeping it; default no.
3. Make it `private` (single caller `Roth.Θ_option_le`)? Yes or no.

Next action: user answers the questions; default is to keep the lemma as is in Roth/Theta.lean.

### Next step

Keep `Roth.index_le_lem6` in Roth/Theta.lean (caller `Roth.Θ_option_le`, Theta.lean:600). Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_le_lem6/weaken_hq.lean` (imports `Roth.Theta` and `Batteries.Tactic.OpenPrivate`, opens the three private helpers; `lake env lean` exit 0, no messages):
  - (1) `Roth.index_le_lem6_no_hq`: the statement without `_hq`, with the original proof copied verbatim; compiles.
  - (2) an `example` recovering the original statement (with `_hq`) from (1) in one line.
- WebSearch ×3 (queries in the table); local read of `.mathlib-quality/references/clean.tex` l.700–790; Lean-Finder, Loogle, LeanSearch and mathlib grep as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
- Sources: https://arxiv.org/pdf/2502.00731, https://arxiv.org/pdf/1305.0926, https://arxiv.org/pdf/math/0307203, https://arxiv.org/pdf/1806.10737, https://arxiv.org/pdf/alg-geom/9608010, https://pub.math.leidenuniv.nl/~evertsejh/14-bonn.pdf.
