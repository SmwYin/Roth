---
decl: Roth.Θ_lt
file: Roth/Theta.lean
line: 962
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The named Lemma 7 of the Roth development (Ridout/Cassels Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}), proved by induction on m from private helpers and Lemmas 5 and 6 about the project-only Θ; mathlib has no Roth index or Θ, the literature states it only inside Roth/Ridout proofs, and its hypotheses are already weaker than the source, so it stays project-local.
action: Keep in Roth/Theta.lean as the paper's Lemma 7 (single caller: private theta_lt_eta_of_sq_log_bound_aux at Roth/MainLemma.lean:687); do not upstream; no call-site changes.
---

# Roth.Θ_lt

## Inventory entry

### `theorem Roth.Θ_lt`
- **Type**: `(n : ℕ) {δ : ℝ} (hδ0 : 0 < δ) {r q : Fin (n + 1) → ℕ} (hrlast : 3 ≤ (r (Fin.last n) : ℝ)) (hratio : ∀ i : Fin n, (r i.succ : ℝ) ≤ δ * r i.castSucc) (hq1 : ((n : ℝ) + 1) * (2 * ((n : ℝ) + 1) + 1) / δ ≤ Real.log (q 0)) (hqr : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) : Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))`
- **What**: Lemma 7 of the source (clean.tex §5, Lemma `roth:lem7`, l.935–960): for `m = n + 1` variables, rapidly decreasing weights `r` and denominators `q` with `log q_1` large and balanced `r_j log q_j ≥ r_1 log q_1`, the supremum of indices `Θ_m(q_1^{δ r_1}; q; r)` is `< 10^m δ^{(1/2)^m}`.
- **How**: induction on `n` generalising `δ`. Base case `n = 0`: for `δ ≤ 1`, private `theta_lt_base_aux` (via Lemma 5 `Θ_unique_le`) with `1 < q 0` from private `theta_denominators_one_lt_aux`; for `δ > 1`, private `theta_lt_of_large_delta_aux` (trivial bound `Θ_le_card` and `(n+1)^2 < 4^(n+1)`). Step: for `δ ≤ 1/(n+2)`, private `theta_lt_succ_aux` (Lemma 6 `Θ_option_le` transported along `finSuccEquivLast`, closed by `theta_phi_lt_aux` with the induction hypothesis); otherwise again `theta_lt_of_large_delta_aux`. Mathlib: `not_le`, `Nat.cast_add`, `Nat.cast_one`.
- **Hypotheses**: `hδ0` (positivity of δ; with δ = 0 the RHS is 0 and the claim is false since Θ ≥ 0); `hrlast` (needed by Lemma 6 and positivity of `r 0` in the base case); `hratio` (weight decay, fed to Lemma 6 and the induction); `hq1` (large `log q 0`, gives `q_j > 1` and the Lemma 5 bounds); `hqr` (balanced logarithms). All named in the proof body.
- **Uses from project**: `Roth.Θ`, private `Roth.theta_lt_base_aux`, private `Roth.theta_denominators_one_lt_aux`, private `Roth.theta_lt_of_large_delta_aux`, private `Roth.theta_lt_succ_aux` (all in Roth/Theta.lean)
- **Used by**: Roth/MainLemma.lean:687 (private `theta_lt_eta_of_sq_log_bound_aux`, itself used at MainLemma.lean:724 on the path to `main_lemma`); named in the module docstring Roth/Theta.lean:39. No other occurrence in `Roth/` or `Roth.lean`.
- **Visibility**: public
- **Lines**: 956–981 (docstring 956–961, statement 962–966, proof 967–981), proof length 15 lines
- **Notes**: listed under `## Main results` of Roth/Theta.lean. Hypotheses are weaker than the source: no upper bound `δ < 1/m` (large δ handled by `theta_lt_of_large_delta_aux`), `r_m ≥ 3` instead of `r_m > 10/δ`, non-strict `r_{j} ≤ δ r_{j-1}` and `≤` in (21).

## Junk check (Step 8)
- Used anywhere? Yes: once, in MainLemma.lean:687, on the main path to Roth's theorem.
- Wrapper of 1–2 mathlib calls? No; an induction dispatching to four project helpers.
- Does mathlib have it? No (Phase 5: no Roth index, no Θ, no Roth lemma in mathlib).
- Too specific (inline?)? No: it is the source's named Lemma 7 and a listed main result of the file; inlining into the private MainLemma helper would lose the paper correspondence.
- Well-chosen? Yes; the statement is already more general than the source.
- Conclusion: `KEEP`. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "**Lemma 7**"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth`, `Θ_lt`, `roth_lemma`, `rothLemma`, "Roth's lemma": no hit. Not a glue lemma (a 15-line induction). Parents `Roth.Θ` (NO-composable-from-mathlib) and `Roth.Θ_option_le` (BORDERLINE) are not NO-mathlib-has-it, so no re-aim. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.Θ_lt`:          resolved at Roth/Theta.lean:962
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index across sets of polynomials `Θ_m(B; q; r)` and Lemmas 5, 6, 7 of the source

### Statement (Phase 1)

`Roth.Θ_lt` is a theorem stating the following:

Let `m ≥ 1`, `δ > 0`, let `r_1, …, r_m` be non-negative integers with `r_m ≥ 3` and `r_j ≤ δ r_{j-1}` (`2 ≤ j ≤ m`), and let `q_1, …, q_m` be natural numbers with `log q_1 ≥ m(2m+1)/δ` and `r_j log q_j ≥ r_1 log q_1` for all `j`. Then `Θ_m(q_1^{δ r_1}; q_1, …, q_m; r_1, …, r_m) < 10^m δ^{(1/2)^m}`, where `Θ_m(B; q; r)` is the supremum of the weighted index `ind(R; h/q; r)` over nonzero integer polynomials `R` with `deg_{x_j} R ≤ r_j`, coefficients bounded by `B`, and `h_j` coprime to `q_j`.

Variables / typeclasses involved (Lean side):
- `n : ℕ`: `m = n + 1`, variables indexed by `Fin (n + 1)`.
- `δ : ℝ`: small parameter. `r q : Fin (n + 1) → ℕ`: weights and denominators.

Hypotheses (Lean side):
- `hδ0`: `0 < δ`. `hrlast`: `r_m ≥ 3`. `hratio`: `r_{i+1} ≤ δ r_i`.
- `hq1`: `m(2m+1)/δ ≤ log q_1`. `hqr`: `r_1 log q_1 ≤ r_j log q_j`.

Conclusion (math): `Θ_m(q_1^{δ r_1}; q; r) < 10^m δ^{(1/2)^m}`.

Conclusion (Lean): `Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))`.

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of Roth/Theta.lean and the named Lemma 7 (Ridout's lemma) feeding `main_lemma`; not a structure, but a main result of the file.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 15 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof Cassels Lemma Theta_m(q_1^{delta r_1}) < 10^m delta^{(1/2)^m} index bound | partial | Roth's lemma `ind ≤ 2mη` (arXiv 2502.00731 Lemma 3.9), induction on m | exact constants `10^m δ^{(1/2)^m}` not surfaced directly |
| 2 | WebSearch (general form) | Roth's lemma index of polynomial at rational point small coefficients statement induction number of variables | yes | Ridout's version at rational points `h_i/q_i` with a `log q_1` condition (Yamada, arXiv math/0307203, Lemma 2.1); Bombieri–Gubler / 2502.00731 algebraic-point version | general form: index of small-height polynomial at high-height point is small |
| 3 | WebSearch (aliases) | "Roth's lemma" Ridout "index" upper bound rapidly decreasing degrees Bombieri Gubler | yes | Yamada states "Lemma 7 due to Ridout" with hypotheses `0 < δ < 1/m`, `r_m > 10/δ`, `r_{j-1}/r_j > 1/δ`, `log q_1` large: same statement as the source | confirms the lemma is Ridout's Lemma 7 |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | read `.mathlib-quality/references/clean.tex` l.935–1021 (Lemma `roth:lem7` and proof) | yes | eqs. (19)–(23): exactly the Lean conclusion | Lean hypotheses weaker: no `δ < 1/m`, `r_m ≥ 3` vs `r_m > 10/δ`, `≤` vs `<` in (20)–(21) |
| 6 | nLab | index of a polynomial; Roth's lemma | no | n/a | no entry on Roth's index or Roth's lemma |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Diophantine estimate, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread isolating Ridout's Lemma 7 |
| 10 | recent arXiv | 2502.00731, math/0307203, 1806.10737, 2601.11376, 1008.2268 | partial | as #2, #3 | Roth's lemma restated in each; Θ-formulation with these constants only in Ridout/Yamada lineage |

### Literature summary (Phase 3)

Concept identified as: Roth's lemma in Ridout's Θ formulation ("Lemma 7" of Ridout, as quoted by Yamada), the non-vanishing / small-index estimate for small-height polynomials at rational points with rapidly growing denominators.
Sources agree on the standard form: only qualitatively. Each source states Roth's lemma with its own constants and normalisation (Θ-sup with `10^m δ^{(1/2)^m}` in Ridout/Cassels; `ind ≤ 2mη` with height conditions in Bombieri–Gubler; Faltings-product-theorem refinements in Evertse/Ferretti).
Most general standard form: Roth's lemma for algebraic points (Bombieri–Gubler Ch. 6): index of `P ∈ ℤ[x_1..x_m]` with `deg_{x_h} ≤ r_h` at `β̄ ∈ Q̄^m` is `≤ 2mη` when `r_{j+1}/r_j ≤ η^{2^{m-1}}` and `h(β_h)` large relative to `h(P)`.
Generality dimensions where the literature varies:
  - point: rational (here, Ridout) vs algebraic (Bombieri–Gubler).
  - constants / height normalisation: source-specific.
Disagreement with the literature: none; the Lean hypotheses are weaker than the source's.

### Generality analysis — `Roth.Θ_lt`

Literature-standard form: clean.tex Lemma 7 / Ridout's Lemma 7 (eqs. (19)–(23)).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hδ0` | `0 < δ` | `0 < δ < 1/m` | already weaker | upper bound removed; `δ > 0` essential (δ = 0 makes RHS 0 while Θ ≥ 0) |
| 2 | `hrlast` | `r_m ≥ 3` | `r_m > 10/δ` | already weaker | needed by Lemma 6 (`Θ_option_le`) and for `0 < r 0` in the base case |
| 3 | `hratio` | `r_{i+1} ≤ δ r_i` | `r_{j-1}/r_j > 1/δ` | already weaker | drives Lemma 6 and the induction |
| 4 | `hq1` | `m(2m+1)/δ ≤ log q_1` | `log q_1 > m(2m+1)/δ` | already weaker | needed: gives `q_j > 1`; with `q ≡ 1` the claim fails (e.g. `m = 1`, `R = x^{r_1}` at `h = 0` has index 1) |
| 5 | `hqr` | `r_1 log q_1 ≤ r_j log q_j` | same, `j ≥ 2` | no | essential for Lemma 5 bounds in each variable |
| 6 | positivity of `r_j`, `q_j` | not assumed | positive integers | already weaker | derived inside the proof |
| 7 | rational points over ℤ | fixed | algebraic points | no (here) | Θ is defined over rational points; changing it redesigns the development |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (relative to the project's Θ; already strictly weaker hypotheses than the source)
Number of weakening opportunities found: 0 (every hypothesis is named in the proof and mathematically load-bearing as argued in the table; no weakening is proposed, so none needed compiling)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | numeric hypotheses on data | — |
| 2 | Sequences vs filters? | no | finite real inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | integrality and real logarithms essential | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `Fin (n + 1)` ordering of variables is the content of the decay condition; an arbitrary `Fintype` would need a linear order, no gain | — |
| 8 | Concrete-via-abstract? | no | the proof works throughout with `Θ` and the paper-specific helpers; no abstract witness to extract | — |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific quantitative estimate with paper-specific constants about project definitions; nothing reorganises it into contemporary mathlib API.

### Proof strategy — `Roth.Θ_lt`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the proof is a clean case split dispatching to helpers; no generic missing lemma | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (structural induction with case splits on δ; the source's strategy, extended to large δ by the trivial bound)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_lt`

[A] Lean-Finder       "Roth's lemma: the index of an integer polynomial with small coefficients at a rational point with large denominators is small"   hits: `one_le_pow_mul_abs_eval_div`, `Liouville.exists_pos_real_of_irrational_root`, `ChevalleyThm.MvPolynomialC.numBound`, `Real.exists_int_int_abs_mul_sub_le`, `Rat.finite_rat_abs_sub_lt_one_div_den_sq` — Liouville/Dirichlet-level only, no Roth lemma
[B] Loogle            `"Roth"`   hits only `Algebra.GrothendieckGroup*` (substring match) — no Roth lemma
[C] LeanSearch        "upper bound on supremum of index of multivariate integer polynomials at rational points, Roth lemma"   hits: `Behrend.roth_lower_bound`, `rothNumberNat_le`, `addRothNumber_le` (unrelated additive-combinatorics Roth number)
[D] Grep mathlib src  `namespace Roth`, `Θ_lt`, `roth_lemma`, `rothLemma`, `Roth's lemma`   no hits
[E] Name pattern      `Roth.Θ_lt`   only the project declaration

Searched for both:
  - the user's current form (Ridout Θ-bound, Lemma 7)
  - the literature-standard form (Roth's lemma, index bound for small-height polynomials at algebraic/rational points)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Mathlib's Diophantine approximation stops at Liouville and Dirichlet.

### Normal-form check — `Roth.Θ_lt`

Equivalent formalisms: (a) `Θ … < bound` (current); (b) `∀ R ∈ RSet, ∀ h coprime, index R (h/q) r < bound` (pointwise; strictly weaker than (a) since a sup can equal a non-attained bound); (c) Bombieri–Gubler `index ≤ 2mη` form.
Does mathlib already have a canonical form? no.
Proposed canonical form: current (matches the source; the caller consumes `Θ … < eta δ m` directly).
RHS convention respected? yes (upper bound with `Θ` on the LHS).

### Syntactic generality — `Roth.Θ_lt`

Alternative restatements attempted:
- current (`m = n + 1`, `Fin (n + 1)`, `hratio` over `Fin n` via `succ`/`castSucc`)
- `[NeZero m]` with `Fin m` and consecutive-index ratio as in the caller (MainLemma.lean:671–676)
- source-strict hypotheses (`<`, `δ < 1/m`, `r_m > 10/δ`)

Chosen restatement: current.
Justification: `n + 1` is the induction-friendly shape; the single caller adapts in four lines; strict source hypotheses would be strictly weaker as a theorem.

### Superfluous-argument audit — `Roth.Θ_lt`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hδ0` | yes | δ = 0 makes the claim false |
| 2 | `hrlast` | yes | Lemma 6 and `0 < r 0` |
| 3 | `hratio` | yes | Lemma 6 and induction |
| 4 | `hq1` | yes | `q_j > 1`; without it counterexample at `q ≡ 1` |
| 5 | `hqr` | yes | Lemma 5 bounds |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `Roth.Θ_lt`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:687 | `simpa [eta] using Θ_lt n hδpos (by simpa … using (Nat.cast_le (α := ℝ)).2 hrlast) (fun i ↦ …) (by simpa [M] using hq) hqr` (in private `theta_lt_eta_of_sq_log_bound_aux`) |

Inline-derivation grep:
  - (none) — no other site re-derives the Lemma 7 bound on `Θ`.

### Composition check (Phase 6)

Can `Roth.Θ_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Nat.rec` with `theta_lt_base_aux` / `theta_lt_succ_aux` / `theta_lt_of_large_delta_aux`.
  - Decls used: project helpers only (plus `not_le`, `Nat.cast_add`).
  - Result: fails as a mathlib composition; the content is in the project's Lemma 5, Lemma 6 and the private helpers.
Attempt 2: mathlib-only.
  - Result: fails; mathlib has no Roth index, Θ, generalised Wronskian or Roth lemma.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.Θ_lt`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): exactly Lemma 7 of the source (clean.tex l.935–960), which is Ridout's Lemma 7 as quoted by Yamada (arXiv math/0307203); the general literature form is Roth's lemma (Bombieri–Gubler Ch. 6, arXiv 2502.00731 Lemma 3.9) with different constants.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; hypotheses already weaker than the source, none superfluous.
- Mathlib search (Phase 5): not in mathlib.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Unlike Lemmas 5 and 6, Lemma 7 has standing in the literature: it is a quantitative form of Roth's lemma, the key non-vanishing estimate in Roth's theorem. Mathlib lacks Roth's lemma and Roth's theorem altogether (its Diophantine approximation stops at Liouville and Dirichlet), so in principle this fills a real gap. But it is stated for the project's `Θ`, which is built on the project's `index`, `RSet` and the Hasse-derivative/Wronskian infrastructure. Those are BORDERLINE or NO in their own reports, and the constants (`10^m δ^{(1/2)^m}`) belong to Ridout's presentation. A mathlib Roth's lemma would more likely be the Bombieri–Gubler form at algebraic points with mathlib's height machinery. That would be a redesign, not a mechanical restatement, which is class 5 of the false-positive routing. No YES bucket fits as is. No NO bucket fits either: mathlib does not have it and it is not a composition. So the verdict is BORDERLINE, recommending that it stay project-local, consistent with `Roth.Θ_option_le` and `Roth.Θ`.

Numbered questions:
1. Keep `Roth.Θ_lt` project-local in Roth/Theta.lean (recommended: yes)?
2. Should the project ever upstream Roth's theorem as a whole? If so, should Roth's lemma be restated in the Bombieri–Gubler form (algebraic points, Weil heights) instead of Ridout's Θ form? Default: no, out of scope.
3. Keep the hypotheses weaker than the source (no `δ < 1/m`, `r_m ≥ 3`), and note this in the docstring as is already done? Default: yes.

Next action: user answers the questions; default is to keep the theorem as is in Roth/Theta.lean.

### Next step

Keep `Roth.Θ_lt` in Roth/Theta.lean (caller: private `theta_lt_eta_of_sq_log_bound_aux`, Roth/MainLemma.lean:687). Do not upstream. No call-site changes.

## Evidence
- No evidence Lean file: no weakening was proposed (all hypotheses already weaker than the source and load-bearing), so no compilation experiment was needed; Lean start-up cost rule respected.
- WebSearch ×3 (queries in the table); local read of `.mathlib-quality/references/clean.tex` l.925–968; Lean-Finder, Loogle, LeanSearch and mathlib grep as recorded in Phase 5; project-wide `grep -rn "Θ_lt\b" Roth/` (hits: Theta.lean:39, :962; MainLemma.lean:687).
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
- Sources: https://arxiv.org/pdf/math/0307203, https://arxiv.org/pdf/2502.00731, https://arxiv.org/pdf/1806.10737, https://arxiv.org/html/2601.11376v1, https://arxiv.org/pdf/1008.2268, https://www.math.uh.edu/~minru/fields/roth.pdf.
