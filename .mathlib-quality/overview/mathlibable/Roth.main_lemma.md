---
decl: Roth.main_lemma
file: Roth/MainLemma.lean
line: 735
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Roth's main lemma (Lemma 9 of the source, Cassels/Ridout lineage) existence of an integer auxiliary polynomial with large index at (alpha,...,alpha), nonvanishing at (h_j/q_j) and bounded Hasse derivatives; a 16-line assembly of project helpers about the project-only index, Theta, RSet and Hasse derivatives with source-specific constants; mathlib has no Roth machinery, so it is a genuine gap but only upstreamable as part of a redesigned Roth development.
action: Keep in Roth/MainLemma.lean as the paper's Lemma 9 (single caller: private one_lt_roth_eval_bound_aux at Roth/Main.lean:466); do not upstream on its own; no call-site changes.
---

# Roth.main_lemma

## Inventory entry

### `theorem Roth.main_lemma`
- **Type**: `{α : ℝ} {f : Polynomial ℤ} (hf : f.Monic) (hfα : Polynomial.aeval α f = 0) {A : ℝ} (hA : ∀ i, |(f.coeff i : ℝ)| ≤ A) {m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 ≤ δ) (hδm : δ ≤ 1 / m) {r : Fin m → ℕ} (hrlast : 3 ≤ r (Fin.rev 0)) (h31b : ∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ ≤ r i) {q : Fin m → ℕ} (h32 : 2 * m + 1 + 2 * m * Real.log (1 + A) + 2 * m * Real.log (1 + |α|) ≤ δ ^ 2 * Real.log (q 0)) (h33 : ∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) {h : Fin m → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) : ∃ Q : MvPolynomial (Fin m) ℤ, Q ≠ 0 ∧ (∀ j, degreeOf j Q ≤ r j) ∧ gam δ f.natDegree m - eta δ m < index (map (Int.castRingHom ℝ) Q) (fun _ ↦ α) r ∧ eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0 ∧ ∀ i : Fin m →₀ ℕ, |eval (fun _ ↦ α) (hasseDeriv i (map (Int.castRingHom ℝ) Q))| < (mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ)`
- **What**: Roth's main lemma (clean.tex §6, Lemma `roth:lem9`, l.1392–1404): for a real root α of a monic integer polynomial f with coefficients bounded by A, m ≥ 1, 0 ≤ δ ≤ 1/m, degrees r_j with r_m ≥ 3 and r_{j+1}/δ ≤ r_j, denominators q_j with the logarithmic bounds (32), (33), and numerators h_j coprime to q_j, there is a nonzero Q ∈ ℤ[x_1..x_m] with deg_{x_j} Q ≤ r_j, index at (α,…,α) strictly greater than γ − η, Q(h_1/q_1,…,h_m/q_m) ≠ 0, and |Δ_i Q(α,…,α)| < B_1^{1+3δ} for all i, where B_1 = ⌊q_1^{δ r_1}⌋.
- **How**: (1) private `exists_auxiliary_polynomial_with_index_gap_aux` (pigeonhole auxiliary polynomial W ∈ RSet(q_1^{δ r_1}; r) plus Lemma 7) gives W with γ − η + Θ < index W and the double-Hasse-derivative bound; (2) set c := (index W − (γ − η) + Θ)/2; (3) private `exists_hasseDeriv_index_eval_bound_aux` with z = (h_j/q_j), side conditions closed by `linarith` using the gap and `Roth.index_le_Θ hW hh` (index of W at h/q is ≤ Θ); (4) `simpa only [add_sub_cancel_right]`. Mathlib lemma used: `add_sub_cancel_right`.
- **Hypotheses**: `hf`, `hfα`, `hA` (α algebraic integer with coefficient bound; used by the auxiliary-polynomial construction via Euclidean reduction mod f); `hδ0`, `hδm` (parameter range); `hrlast`, `h31b` (degree chain (31), weakened); `h32` (log bound (32), weakened to ≤); `h33` (balanced logs); `hh` (coprimality, used only by `index_le_Θ`). Every hypothesis is passed to a helper in the body.
- **Uses from project**: private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (Roth/MainLemma.lean:692), private `Roth.exists_hasseDeriv_index_eval_bound_aux` (Roth/MainLemma.lean:477), `Roth.index_le_Θ` (Roth/Theta.lean:99), `Roth.index` (Roth/Index.lean:58), `Roth.Θ` (Roth/Theta.lean:68), `Roth.RSet` (Roth/Theta.lean:56, via `hW`), `Roth.gam`, `Roth.eta`, `Roth.mainCoeffBound` (Roth/MainLemma.lean:63, 66, 69), `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean:57)
- **Used by**: Roth/Main.lean:466 (private `one_lt_roth_eval_bound_aux`, on the path to Roth's theorem); named in docstrings Roth/MainLemma.lean:21, :45 and Roth/Main.lean:34. No other occurrence in `Roth/` or `Roth.lean`.
- **Visibility**: public
- **Lines**: 726–762 (docstring 726–734, statement 735–746, proof 747–762), proof length 16 lines
- **Notes**: listed under `## Main results` of Roth/MainLemma.lean. Hypotheses weaker than the source: δ ≥ 0 and δ ≤ 1/m instead of 0 < δ < 1/m (29); no (30) (m > 16n² condition); r_m ≥ 3 instead of r_m > 10/δ; non-strict ratio and log bounds; A any coefficient bound (not max(1,|a_i|)); α need not be irrational; no positivity of q_j. Conclusion strict (`<` index) where the source has `≥`; the source's "γ − η > 0" part of item (1) is not asserted (it follows from (30), handled at the call site). Conjunct `Q ≠ 0` is implied by conjunct 4 (Q(h/q) ≠ 0) and is discarded (`-`) by the only caller; kept for fidelity to the source statement.

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Main.lean:466, the step of the final argument that produces Q.
- Wrapper of 1–2 mathlib calls? No; it assembles two substantial project helpers and `index_le_Θ`.
- Does mathlib have it? No (Phase 5: no Roth index, no Θ, no Roth lemma or main lemma).
- Too specific (inline?)? No: it is the source's named Lemma 9 and a listed main result; inlining into the private Main.lean helper would lose the paper correspondence.
- Well-chosen? Yes; already weaker hypotheses and a stronger (strict) conclusion than the source. Minor: the `Q ≠ 0` conjunct is redundant given `Q(h/q) ≠ 0`, harmless.
- Conclusion: `KEEP`. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "**Roth's main lemma**"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth`, `main_lemma`, `Roth's lemma`, `Roth's main lemma`, `rothLemma`: no hit. Not a glue lemma (16-line proof). Parents (`Roth.index`, `Roth.Θ`, `Roth.RSet`, `Roth.Θ_lt`) are BORDERLINE / NO-composable in their own reports, none NO-mathlib-has-it, so no re-aim. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.main_lemma`:    resolved at Roth/MainLemma.lean:735
- kind:                      theorem
- has sorry:                 no (`lean_verify`: axioms `propext`, `Classical.choice`, `Quot.sound` only)
- module docstring summary:  Roth's main lemma (Lemma 9): pigeonhole auxiliary polynomial, index gap, nonvanishing derivative

### Statement (Phase 1)

`Roth.main_lemma` is a theorem stating the following:

Let α ∈ ℝ be a root of a monic f ∈ ℤ[x] whose coefficients have absolute value ≤ A. Let m ≥ 1, 0 ≤ δ ≤ 1/m, let r_1 ≥ … ≥ r_m be natural numbers with r_m ≥ 3 and r_{j+1}/δ ≤ r_j, let q_1, …, q_m be natural numbers with δ² log q_1 ≥ 2m + 1 + 2m log(1+A) + 2m log(1+|α|) and r_j log q_j ≥ r_1 log q_1, and let h_j be integers coprime to q_j. Then there is a nonzero Q ∈ ℤ[x_1, …, x_m] with deg_{x_j} Q ≤ r_j such that the index of Q at (α, …, α) relative to r exceeds γ − η (γ = (m − 4(1+3δ)n√m)/2, η = 10^m δ^{(1/2)^m}, n = deg f), Q(h_1/q_1, …, h_m/q_m) ≠ 0, and every Hasse derivative satisfies |Δ_i Q(α, …, α)| < B_1^{1+3δ}, B_1 = ⌊q_1^{δ r_1}⌋.

Variables / typeclasses involved (Lean side):
- `α : ℝ`, `f : Polynomial ℤ`, `A : ℝ`: the algebraic integer, its equation, coefficient bound.
- `m : ℕ` with `[NeZero m]`: number of variables, indexed by `Fin m`.
- `δ : ℝ`; `r q : Fin m → ℕ`: degrees and denominators; `h : Fin m → ℤ`: numerators.

Hypotheses (Lean side):
- `hf`, `hfα`, `hA`: α is a root of a monic integer polynomial with coefficients bounded by A.
- `hδ0`, `hδm`: 0 ≤ δ ≤ 1/m. `hrlast`, `h31b`: chain (31). `h32`, `h33`: log bounds (32), (33). `hh`: gcd(h_j, q_j) = 1.

Conclusion (math): a nonzero integer polynomial with bounded degrees, index > γ − η at the diagonal algebraic point, nonvanishing at the rational point, and bounded Hasse derivatives at the diagonal point.

Conclusion (Lean): `∃ Q : MvPolynomial (Fin m) ℤ, Q ≠ 0 ∧ (∀ j, degreeOf j Q ≤ r j) ∧ gam δ f.natDegree m - eta δ m < index (map (Int.castRingHom ℝ) Q) (fun _ ↦ α) r ∧ eval (fun j ↦ (h j : ℝ) / q j) (map (Int.castRingHom ℝ) Q) ≠ 0 ∧ ∀ i, |eval (fun _ ↦ α) (hasseDeriv i (map (Int.castRingHom ℝ) Q))| < (mainCoeffBound δ (q 0) (r 0) : ℝ) ^ (1 + 3 * δ)`

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of Roth/MainLemma.lean, named after Roth ("Roth's main lemma", Lemma 9), the central step of the project's main theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 16 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof "main lemma" auxiliary polynomial index at (alpha,...,alpha) nonvanishing at rational point Cassels Lemma 9 | partial | Roth machinery: auxiliary polynomial with large index at (α,…,α) via Siegel's lemma, then Roth's lemma forces a low-order derivative nonvanishing at the rational point (Evertse Luminy slides; arXiv 2502.00731) | Cassels' numbering not surfaced; same structure |
| 2 | WebSearch (general form) | Roth theorem construction of auxiliary polynomial Siegel's lemma high index small height multivariate polynomial Bombieri Gubler | yes | Bombieri–Gubler Ch. 6 (as presented in arXiv 2502.00731): Siegel-lemma auxiliary polynomial with height ≲ ∑ d_h and index ≥ m(1/2 − ε)·... at (α,…,α) over a number field; non-vanishing via Roth's lemma | general form: algebraic α of any degree over a number field K, heights instead of integer coefficients |
| 3 | WebSearch (aliases / formalisations) | Thue-Siegel-Roth theorem formalization Lean Isabelle Roth's lemma auxiliary polynomial | yes | Lean eval page lists Thue–Siegel–Roth as open; mathlib has only Liouville, Dirichlet, `ae_not_liouvilleWith` | confirms no formal Roth machinery in mathlib or Isabelle AFP |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | read `.mathlib-quality/references/clean.tex` l.1195–1404 and l.1530–1561 (setup (28)–(33), Lemma `roth:lem9` and proof) | yes | Lemma 9: Q ≠ 0, deg ≤ r_j, ind ≥ γ − η > 0, Q(h/q) ≠ 0, |Δ_i Q(α..α)| < B_1^{1+3δ} under (29)–(33) | Lean hypotheses weaker (no (30), δ ≥ 0, r_m ≥ 3, ≤ in (31)/(32)); conclusion strict but omits "γ − η > 0" |
| 6 | nLab | Roth's theorem; index of a polynomial | no | n/a | no entry on Roth's theorem machinery |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Diophantine approximation estimate, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3; Roth proof expositions) | no | n/a | no thread isolating the main lemma as a standalone statement |
| 10 | recent arXiv | 2502.00731 (Roth and Schmidt via Bombieri–Gubler), 1806.10737 (function-field Roth), 0908.4024 (auxiliary functions survey) | partial | as #2 | each states its own version of the auxiliary-polynomial step with its own constants |

### Literature summary (Phase 3)

Concept identified as: the auxiliary-polynomial step ("main lemma") of Roth's theorem, in the Cassels/Ridout presentation (Lemma 9) combining Siegel's/pigeonhole construction, Roth's lemma (via Θ, Lemma 7) and passage to a nonvanishing derivative.
Sources agree on the standard form: only qualitatively. Every exposition (Roth 1955, Cassels Ch. VI, Schmidt LNM 785, Bombieri–Gubler Ch. 6, arXiv 2502.00731) has an auxiliary-polynomial step, but its packaging and constants are source-specific; it is never stated as a standalone library-level theorem.
Most general standard form: Bombieri–Gubler: for α algebraic over a number field K, m variables and degrees d_h, there is P with deg_{x_h} P ≤ d_h, controlled height, and index ≥ m(1/2 − ε) at (α,…,α); Roth's lemma then gives a low-order derivative nonvanishing at the rational/K-rational point.
Generality dimensions where the literature varies:
  - α: real algebraic integer (here) vs algebraic number over a number field (Bombieri–Gubler).
  - point: rational h_j/q_j (here) vs K-rational points with Weil heights.
  - size control: integer coefficients bounded by B_1 (here) vs heights.
  - constants γ, η, 1 + 3δ: source-specific.
Disagreement with the literature: none; the Lean hypotheses are weaker than the source's, the conclusion slightly stronger (strict) except for the separate "γ − η > 0".

### Generality analysis — `Roth.main_lemma`

Literature-standard form: clean.tex Lemma 9 under (28)–(33).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hf`, `hfα` | α root of monic integer f | algebraic integer α (source); any algebraic α (Bombieri–Gubler) | not mechanically | monicity drives the Euclidean reduction mod f in the pigeonhole step (`exists_ne_modByMonic_eq`, `norm_coeff_modByMonic_le`); non-monic would need a denominator-clearing redesign |
| 2 | `hA` | any upper bound A on coefficients | A = max(1, |a_i|) | already weaker | needed in (32)-derived bounds |
| 3 | `hδ0`, `hδm` | 0 ≤ δ ≤ 1/m | 0 < δ < 1/m | already weaker | δ > 0 is derived from (32) inside the helper |
| 4 | (30) | absent | 10^m δ^{(1/2)^m} + 2(1+3δ)n√m < m/2 | already weaker | only needed for γ − η > 0, which the call site handles |
| 5 | `hrlast`, `h31b` | r_m ≥ 3, r_{j+1}/δ ≤ r_j | r_m > 10/δ, r_{j-1}/r_j > 1/δ | already weaker | needed by Lemma 7 and the antitonicity of r |
| 6 | `h32`, `h33` | non-strict | strict (32), (33) | already weaker | load-bearing for B_1 estimates and Lemma 7 |
| 7 | `hh` | IsCoprime h_j q_j | gcd = 1 | no | needed for `index_le_Θ` (Θ is a sup over coprime numerators) |
| 8 | rational points / integer coefficients | fixed | K-rational points, heights | no (here) | changing it redesigns index, Θ, RSet and the whole development |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (relative to the project's index/Θ framework; hypotheses already strictly weaker than the source)
Number of weakening opportunities found: 0 (every hypothesis is passed to a helper and is mathematically load-bearing; no weakening proposed, so none needed compiling)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | numeric hypotheses on data; `IsIntegral ℤ α` could replace (hf, hfα) but A and n = deg f must stay explicit | — |
| 2 | Sequences vs filters? | no | finite existence statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | real logarithms, integer coefficients and rational points essential | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | the `Fin m` order is the content of the chain condition (31) | — |
| 8 | Concrete-via-abstract? | no | the body works with W, Θ and index throughout; no concrete object eliminated after an unfolding | — |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific existence statement with paper-specific constants about project definitions; a mathlib-idiomatic Roth would use heights (Bombieri–Gubler), which is a redesign rather than a restatement.

### Proof strategy — `Roth.main_lemma`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | assembly of project helpers; the generic gaps (multivariate Hasse derivative, Siegel's lemma) are assessed in their own reports | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (the source's argument: W from pigeonhole + Lemma 7, then a low-order derivative via the midpoint choice of c and `linarith`)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.main_lemma`

[A] Lean-Finder       "Roth's theorem: auxiliary integer polynomial with large index at algebraic point and nonvanishing at rational point"   hits: `one_le_pow_mul_abs_eval_div`, `Liouville.exists_pos_real_of_irrational_root`, `LindemannWeierstrass.exp_polynomial_approx`, `ChevalleyThm.MvPolynomialC.numBound`, `Polynomial.exists_approx_polynomial` — Liouville-level and unrelated; no Roth lemma
[B] Loogle            `"Roth"`   hits only `Algebra.GrothendieckGroup*` (substring match) — no Roth lemma
[C] LeanSearch        "Roth's theorem on rational approximation of algebraic numbers"   hits: `Liouville`, `Rat.finite_rat_abs_sub_lt_one_div_den_sq`, `Liouville.frequently_exists_num`, `Liouville.exists_pos_real_of_irrational_root`, `setOf_liouville_eq_irrational_inter_iInter_iUnion` — no Roth
[D] Grep mathlib src  `namespace Roth`, `main_lemma`, `Roth's lemma`, `Roth's main lemma`, `rothLemma`   no hits
[E] Name pattern      `Roth.main_lemma`   only the project declaration

Searched for both:
  - the user's current form (Cassels/Ridout Lemma 9)
  - the literature-standard form (Bombieri–Gubler auxiliary polynomial with heights; Siegel's lemma)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Mathlib's Diophantine approximation stops at Liouville and Dirichlet.

### Normal-form check — `Roth.main_lemma`

Equivalent formalisms: (a) current five-conjunct existence; (b) the same without the redundant `Q ≠ 0` (implied by `Q(h/q) ≠ 0`); (c) Bombieri–Gubler height form.
Does mathlib already have a canonical form? no.
Proposed canonical form: current (matches the source statement item by item).
RHS convention respected? n/a (existence statement).

### Syntactic generality — `Roth.main_lemma`

Alternative restatements attempted:
- current (`[NeZero m]`, `Fin m`, consecutive-index chain condition)
- dropping the `Q ≠ 0` conjunct (implied by the nonvanishing conjunct; the single caller already discards it)
- `IsIntegral ℤ α` in place of `hf, hfα` (loses the explicit `f`, needed for `A` and `n`)

Chosen restatement: current.
Justification: mirrors the source's Lemma 9 and is applied in one line at Roth/Main.lean:466; the redundant conjunct is harmless documentation.

### Superfluous-argument audit — `Roth.main_lemma`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hf`, `hfα`, `hA` | yes | pigeonhole step (reduction mod f) and B_1 estimates |
| 2 | `hδ0`, `hδm` | yes | Lemma 7 and r antitone |
| 3 | `hrlast`, `h31b` | yes | Lemma 7, degree bounds |
| 4 | `h32`, `h33` | yes | B_1 estimates, Lemma 7 |
| 5 | `hh` | yes | `index_le_Θ` |
| 6 | `[NeZero m]` | yes | `q 0`, `r 0`, `Fin.rev 0` must make sense |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (optional: drop redundant `Q ≠ 0` conjunct; not recommended, source fidelity)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED

### Call sites — `Roth.main_lemma`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:466 | `obtain ⟨Q, -, hQd, hidx_strict, hne, hC⟩ := main_lemma hf hfα hA hδ0 hδm hrlast h31b h32 h33 hcop` (in private `one_lt_roth_eval_bound_aux`) |

Inline-derivation grep:
  - (none) — no other site re-derives the Lemma 9 polynomial.

### Composition check (Phase 6)

Can `Roth.main_lemma` be derived from mathlib in ≤3 chained calls?

Attempt 1: `exists_auxiliary_polynomial_with_index_gap_aux` then `exists_hasseDeriv_index_eval_bound_aux` with `index_le_Θ`.
  - Decls used: project helpers only (plus `add_sub_cancel_right`).
  - Result: fails as a mathlib composition; the content lives in project helpers (pigeonhole over `boxFamily`, Lemma 7, Hasse derivatives, index).
Attempt 2: mathlib-only.
  - Result: fails; mathlib has no Roth index, Θ, multivariate Hasse derivative, Siegel's lemma for this setting, or Roth's lemma.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.main_lemma`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): exactly Lemma 9 of the source (clean.tex l.1392–1404), the auxiliary-polynomial step of Roth's theorem (Cassels/Ridout); the general literature form is the Bombieri–Gubler height formulation (arXiv 2502.00731), with different constants.
- Generality analysis (Phase 4): MAXIMALLY GENERAL relative to the project framework; hypotheses already weaker than the source, none superfluous.
- Mathlib search (Phase 5): not in mathlib.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

This is the central step of Roth's theorem, and mathlib has nothing like it: its Diophantine approximation stops at Liouville and Dirichlet, and no Roth machinery exists (the Lean eval page lists Thue–Siegel–Roth as open). So it fills a real gap in principle. But the statement belongs to the Cassels/Ridout presentation. Its constants are paper-specific (γ, η = 10^m δ^{(1/2)^m}, B_1^{1+3δ}). It is phrased in terms of the project's `index`, `Θ`, `RSet` and multivariate `hasseDeriv`, which are BORDERLINE or NO in their own reports. The proof is a 16-line assembly of private helpers. A mathlib Roth's theorem would more likely follow Bombieri–Gubler, with Weil heights and algebraic points over number fields. That would be a redesign of the development, not a restatement, which is class 5 of the false-positive routing. No YES bucket fits as is, and no NO bucket fits either. Verdict: BORDERLINE, recommending that it stay project-local. This matches `Roth.Θ_lt` (Lemma 7) and `Roth.Θ`.

Numbered questions:
1. Keep `Roth.main_lemma` project-local in Roth/MainLemma.lean (recommended: yes)?
2. If the project ever upstreams Roth's theorem as a whole, should the main lemma be restated in the Bombieri–Gubler height form rather than Cassels' Lemma 9 form? Default: out of scope.
3. Drop the redundant `Q ≠ 0` conjunct (implied by `Q(h/q) ≠ 0`; discarded by the only caller)? Default: no, keep for source fidelity.
4. Keep the "γ − η > 0" part of the source's item (1) out of this statement (it follows from (30) at the call site)? Default: yes; the docstring already flags the weaker hypotheses.

Next action: user answers the questions; default is to keep the theorem as is in Roth/MainLemma.lean.

### Next step

Keep `Roth.main_lemma` in Roth/MainLemma.lean (caller: private `one_lt_roth_eval_bound_aux`, Roth/Main.lean:466). Do not upstream on its own. No call-site changes.

## Evidence
- No evidence Lean file: no weakening was proposed (all hypotheses already weaker than the source and load-bearing), so no compilation experiment was needed; Lean start-up cost rule respected.
- `lean_verify Roth.main_lemma`: standard axioms only (`propext`, `Classical.choice`, `Quot.sound`).
- WebSearch ×3 (queries in the table); local read of `.mathlib-quality/references/clean.tex` l.1195–1404, l.1530–1561; Lean-Finder, Loogle, LeanSearch and mathlib grep as recorded in Phase 5; project-wide `grep -rn main_lemma Roth/ Roth.lean` (hits: MainLemma.lean:21, :45, :735; Main.lean:34, :466).
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
- Sources: https://arxiv.org/pdf/2502.00731, https://pub.math.leidenuniv.nl/~evertsejh/14-luminy-1.pdf, https://arxiv.org/pdf/1806.10737, https://arxiv.org/pdf/0908.4024, https://lean-lang.org/eval/problems/thue_siegel_roth/, https://en.wikipedia.org/wiki/Roth%27s_theorem.
