---
decl: Roth.abs_coeff_det_hasseDeriv_le
file: Roth/CoeffNorm.lean
line: 258
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: CHEAP
junk: KEEP
rationale: Roth's Lemma 3 (paper-specific constant) is a 5-lemma chain through the project l1 norm API (abs_coeff_le_normOne, normOne_det_le, normOne_hasseDeriv_le, normOne_le_card_mul, card_le_card_box), each already slated for upstreaming as MvPolynomial.l1Norm lemmas; not composable from current mathlib (no l1 polynomial norm), but once that API lands it is a short corollary with a Roth-specific constant, so whether it merits its own mathlib lemma is a judgment call; hB0 is superfluous (follows from hB 0, compiled).
action: Recommended answer is keep local (do not upstream separately); drop hB0 (derive it from hB 0, evidence weaken.lean) and simplify the single caller Roth/Theta.lean:475, optionally expose the stronger normOne_det_hasseDeriv_le form the paper actually proves; ship only the underlying l1Norm lemmas in the MvPolynomial.l1Norm PR.
---

# Roth.abs_coeff_det_hasseDeriv_le

## Inventory entry

### `theorem Roth.abs_coeff_det_hasseDeriv_le`
- **Type**: `{σ : Type*} [Fintype σ] {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ)) (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ} (hB0 : 0 ≤ B) (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) (d : σ →₀ ℕ) : |(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤ (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)`
- **What**: Roth's Lemma 3: if `P ∈ ℤ[x_σ]` has partial degrees at most `r_j` and coefficients of absolute value at most `B`, every coefficient of the `l × l` determinant `det(Δ_{E μ ν} P)` of Hasse derivatives has absolute value at most `(∏ (r_j+1))^l · l! · B^l · 2^{(∑ r_j) l}`.
- **How**: `card_le_card_box` bounds `#supp P ≤ ∏ (r_j+1)`; then a calc: `abs_coeff_le_normOne` (coefficient at most ℓ¹ norm), `normOne_det_le` (Leibniz `l! C^l`) with entry bound `C = 2^{∑ r_j} ∏(r_j+1) B` from `normOne_hasseDeriv_le` and `normOne_le_card_mul`; `ring` rearranges.
- **Hypotheses**: `hP` (partial degree bounds), `hB0` (`0 ≤ B`, superfluous: follows from `hB 0`), `hB` (sup coefficient bound), `[Fintype σ]` (finite variable set, needed for `∏`/`∑`).
- **Uses from project**: `Roth.normOne`, `Roth.abs_coeff_le_normOne`, `Roth.normOne_det_le`, `Roth.normOne_hasseDeriv_le`, `Roth.normOne_le_card_mul`, `Roth.card_le_card_box`, `MvPolynomial.hasseDeriv`
- **Used by**: Roth/Theta.lean:475 (`hFcoef`, Step 1 of the Lemma 6 coefficient bound, passing `hB0` as `(abs_nonneg _).trans (hR.2.2 0)`). No other use.
- **Visibility**: public
- **Lines**: 258–275 (docstring 255–257), proof length 14 lines
- **Notes**: Source: clean.tex l.438 (Lemma `roth:lem3`); the paper's proof explicitly bounds the stronger quantity `‖F‖₁`.

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Theta.lean:475), and it is a numbered lemma of the source paper.
- Wrapper of 1–2 mathlib calls? No: a chain of five project lemmas plus arithmetic.
- Does mathlib have it? No (Phase 5); mathlib has no ℓ¹ polynomial norm and no MvPolynomial Hasse derivative.
- Too specific / inline? Specific (paper constant) but it names a paper lemma; inlining into the 1 caller would hurt readability.
- Well-chosen? Yes, apart from the superfluous `hB0` (evidence (2)).
- Conclusion: `KEEP`. Action: drop `hB0` and keep locally.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (`grep -rn "abs_coeff_det\|coeff_det_le" .lake/packages/mathlib/Mathlib/`: no hits). Not a glue lemma (14-line calc). Full workflow below.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates with no diagnostics)
- decl `Roth.abs_coeff_det_hasseDeriv_le`: resolved at Roth/CoeffNorm.lean:258
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.abs_coeff_det_hasseDeriv_le` is a theorem stating: let `P ∈ ℤ[x_1, …, x_p]` have degree at most `r_j` in `x_j` and all coefficients of absolute value at most `B`. For any `l` and any multi-indices `E(μ,ν)`, let `F = det(Δ_{E(μ,ν)} P)_{μ,ν<l}`. Then every coefficient of `F` has absolute value at most `((r_1+1)⋯(r_p+1))^l · l! · B^l · 2^{(r_1+⋯+r_p) l}`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]` — the variables; `l`, `E` — matrix size and derivative orders; `P` — the polynomial; `r` — degree bounds; `B` — coefficient bound; `d` — the monomial.

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j`; `hB0 : 0 ≤ B` (redundant); `hB : ∀ d, |coeff d P| ≤ B`.

Conclusion (math): `|[x^d] F| ≤ (∏(r_j+1))^l l! B^l 2^{(∑ r_j) l}`.

Conclusion (Lean): `|(((Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det.coeff d : ℤ) : ℝ)| ≤ (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)`.

### Size classification (Phase 2a)

Verdict: BIG
Reason: it is a numbered main step of the project (Lemma 3, listed under `## Main results` of Roth/CoeffNorm.lean); but mathematically it is a corollary of general ℓ¹-norm estimates.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 14
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof lemma coefficients of generalized Wronskian determinant bounded l! B^l 2^{(r_1+...+r_p) l} | partial | Roth 1955 (Mathematika) and expositions (arXiv 2502.00731, Bombieri–Gubler ch. 6) use such height bounds for derivative determinants; exact constant not located online | paper-specific constant |
| 2 | WebSearch (general form) | length of polynomial L(P) sum of absolute values of coefficients bound determinant of polynomial matrix Hadamard l! bound | yes | Goldstein–Graham / Lossers (SIAM Rev. 1974, Problem 73-17) Hadamard-type coefficient bound for determinants of polynomials; arXiv 2512.09823 Lemma 77: sup-norm of det ≤ p^{p/2} R₁^p with R₁ the max entry ℓ¹ norm | the general content is "ℓ¹ norm of det ≤ n! (max entry ℓ¹)^n" (or Hadamard-sharpened) |
| 3 | WebSearch (named-after / aliases) | "index" Roth lemma height of derivative determinant polynomial coefficient bound Schmidt Diophantine approximation Bombieri Gubler | partial | Bombieri–Gubler ch. 6 height lemmas for derivatives (`h(Δ P) ≤ h(P) + deg log 2`) and products | the estimate is assembled from standard height inequalities, never a named theorem |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` grep "roth:lem3" | yes | l.438: Lemma 3 with exactly this constant; proof bounds `‖F‖₁` via triangle inequality, submultiplicativity and the Hasse-derivative estimate | the paper proves the stronger ℓ¹ form |
| 6 | nLab | polynomial norm / height | no | — | nLab has no page on coefficient heights of polynomials |
| 7 | nCatLab | — | n/a | — | not a categorical statement (numerical estimate) |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no coefficient-size estimates |
| 9 | MathOverflow / Math.SE | (results of #2) | partial | Hadamard-type bounds for determinants of polynomial matrices appear as folklore answers | general bound only |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2502.00731 (2025), 2512.09823 (2025) | same ingredients used as tools |

### Literature summary (Phase 3)

Concept identified as: a coefficient (height) bound for a generalised Wronskian-type determinant in Roth's method; its content is the chain "coefficient ≤ ℓ¹ norm; ℓ¹ norm of a determinant ≤ n!·(entry ℓ¹ bound)^n; ℓ¹ norm of a Hasse derivative ≤ 2^{deg}·ℓ¹ norm; ℓ¹ norm ≤ #support · sup norm".
Sources agree on the standard form: yes for the ingredients; the combined constant is specific to the Roth exposition (clean.tex l.438).
Most general standard form: for any (semi)normed commutative ring and any finite matrix, `L(det M) ≤ n! (max L(M_ij))^n` and `L(Δ_d P) ≤ 2^{deg P} L(P)`; Lemma 3 is their instantiation.
Generality dimensions where the literature varies:
  - ring: ℤ (project) vs any seminormed ring (ingredients).
  - quantity bounded: one coefficient (project) vs ℓ¹ norm (paper's proof, stronger).
  - determinant constant: `n!` (Leibniz) vs `n^{n/2}` (Hadamard).
Disagreement with the literature: none; the project statement is weaker than what the paper proves (coefficient vs ℓ¹ norm).

### Generality analysis — `Roth.abs_coeff_det_hasseDeriv_le`

Literature-standard form (from Phase 3): the ingredients (`l1Norm_det_le`, `l1Norm_hasseDeriv_le`, `l1Norm_le_card_mul`, `norm_coeff_le_l1Norm`) over any seminormed commutative ring; Lemma 3 itself has no literature-standard general form beyond being their composition.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hB0 : 0 ≤ B` | explicit hypothesis | absent | yes | follows from `hB 0` and `abs_nonneg`; verified (evidence (1), (2)) |
| 2 | conclusion on one coefficient | `|coeff d F| ≤ …` | `L(F) ≤ …` (paper's proof) | yes (stronger conclusion) | verified (evidence (1)); the coefficient form is a one-line corollary (evidence (2)) |
| 3 | coefficients `ℤ` | `MvPolynomial σ ℤ` | `[SeminormedCommRing R] [NormOneClass R]` | yes in principle | requires the ingredient lemmas restated for `MvPolynomial.l1Norm` (sibling reports Roth.normOne, Roth.normOne_det_le, Roth.normOne_hasseDeriv_le compiled those); not re-done here: it is not a single mechanical edit of this lemma but a re-aim of the whole ℓ¹ API |
| 4 | `[Fintype σ]` | needed | needed | no | `∏ j` and `∑ j` in the constant (a `totalDegree` form would avoid it, see Roth.normOne_hasseDeriv_le) |
| 5 | Hasse-derivative entries | specific matrix | any matrix with entry ℓ¹ bounds | yes | that is exactly `normOne_det_le`, already assessed |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD only by the superfluous `hB0` and by bounding a coefficient instead of the ℓ¹ norm (both verified, evidence (1)–(3)); the remaining generality lives entirely in the ingredient lemmas, already assessed YES-but-generalise-first.
Number of weakening opportunities found: 2 (rows 1, 2), both compiled clean.
Proposed restatement:

```lean
theorem Roth.normOne_det_hasseDeriv_le [Fintype σ] {l : ℕ} (E : Fin l → Fin l → (σ →₀ ℕ))
    (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) {B : ℝ}
    (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) :
    normOne (Matrix.of fun μ ν : Fin l ↦ hasseDeriv (E μ ν) P).det ≤
      (∏ j, ((r j : ℝ) + 1)) ^ l * l.factorial * B ^ l * 2 ^ ((∑ j, r j) * l)
-- and abs_coeff_det_hasseDeriv_le without hB0 as its one-line corollary
```

Cost of restatement: CHEAP (compiled).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | hypotheses are numeric data |
| 2 | sequences to filters? | no | — | finite estimate |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | ℤ/abs to a seminormed ring with `l1Norm` | inherited from the ℓ¹ API re-aim (sibling reports); nothing specific to this lemma |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | `Fin l` is what the caller uses; `normOne_det_le`'s Fintype generalisation covers the abstract part | — |
| 8 | concrete-via-abstract? | yes | diagnostic: `hasseDeriv` occurs in the proof body only in the matrix being passed through; the substance is `normOne_det_le` applied to entries bounded by `normOne_hasseDeriv_le`. The abstract content is precisely those two (already assessed) lemmas | none beyond the ingredient lemmas |
| 9 | false-generalisation guard | no false generalisation | evidence (3) recovers the exact original statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma itself)
  - One-line reason: all abstraction (ring, matrix, norm) belongs to the ingredient lemmas; Lemma 3 is the Roth-specific instantiation and its only improvements are dropping `hB0` and exposing the ℓ¹ form.

### Proof strategy — `Roth.abs_coeff_det_hasseDeriv_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `MvPolynomial.l1Norm` with `norm_coeff_le_l1Norm`, `l1Norm_det_le`, `l1Norm_hasseDeriv_le`, `l1Norm_le_card_mul` (sibling reports) | MODERATE (separate PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a `calc` chain through the ℓ¹ norm, exactly the paper's proof)
  - Missing mathlib API: the ℓ¹ polynomial norm and its four estimates (sibling reports).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.abs_coeff_det_hasseDeriv_le`

[A] Lean-Finder       "bound on the absolute value of coefficients of the determinant of a matrix of integer polynomials in terms of a coefficient bound"   hits: `Matrix.det_le`, `Matrix.det_sum_le`, `Matrix.det_sum_smul_le` (AbsoluteValue-valued, `n! x^n`), `Polynomial.natDegree_det_X_add_C_le` — none bounds polynomial coefficients
[B] Loogle            `MvPolynomial.coeff, Matrix.det` (tool error: loogle rejected the identifier); `Matrix.det, Nat.factorial, abs`   no hits
[C] LeanSearch        "coefficient of determinant of matrix of polynomials bounded by factorial times power of bound"   hits: `Matrix.det_le`, `Matrix.det_sum_le`, `Matrix.det_matrixOfPolynomials`, `eval_det` — not applicable (the ℓ¹ norm is not an `AbsoluteValue`, see Roth.normOne_det_le report)
[D] Grep mathlib src  `abs_coeff_det`, `coeff_det_le`, `l1Norm`, `hasseDeriv.*det`   no hits
[E] Name pattern      `lean_local_search "abs_coeff_det"`: n/a (tool error: ripgrep not on PATH); replaced by the grep in [D]

Searched for both the user's form (coefficient bound for a Hasse-derivative determinant) and the general form (ℓ¹ / coefficient bound of a determinant of polynomials).

Concluded: not in mathlib (all methods exhausted); building blocks `Matrix.det_le` exist only for multiplicative absolute values, and no ℓ¹ polynomial norm exists.

### Normal-form check — `Roth.abs_coeff_det_hasseDeriv_le`

Equivalent formalisms: (a) per-coefficient bound (current); (b) ℓ¹ bound `normOne F ≤ …`; (c) sup-norm bound `∀ d, …`.
Does mathlib already have a canonical form? No.
Proposed canonical form: (b), with (a) as corollary (mirrors `Polynomial.le_supNorm` style: norm bound primary, coefficient bound derived).
RHS convention respected? yes.

### Syntactic generality — `Roth.abs_coeff_det_hasseDeriv_le`

Alternative restatements attempted:
- (a) current, with `hB0` (compiles, original)
- (b) ℓ¹ form without `hB0` (compiles; evidence (1))
- (c) coefficient form without `hB0` (compiles; evidence (2))
Chosen restatement: (b) as main lemma, (c) for the caller.
Justification: (c) removes the caller's manual `(abs_nonneg _).trans (hR.2.2 0)` at Roth/Theta.lean:475; (b) is what the paper proves.

### Superfluous-argument audit — `Roth.abs_coeff_det_hasseDeriv_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hB0` | no | derivable from `hB 0` (evidence (1)) |
| 2 | `hB` | yes | coefficient bound |
| 3 | `hP` | yes | degree bounds for the Hasse estimate and the support count |
| 4 | `[Fintype σ]` | yes | constant involves `∏ j`, `∑ j` |
| 5 | `d` | yes for (a); disappears in (b) | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (primary ℓ¹ form, coefficient form as corollary) — optional
Syntactic generality: RESTATE (drop `hB0`)
Superfluous arguments: 1 to drop (`hB0`)

Overall: RESTATE-BEFORE-SHIP (locally)

### Call sites — `Roth.abs_coeff_det_hasseDeriv_le`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:475 (`hFcoef`) | `abs_coeff_det_hasseDeriv_le _ R (r := fun _ ↦ r₁) (fun j ↦ (hR.2.1 j).trans (hr₁ j)) ((abs_nonneg ((R.coeff 0 : ℤ) : ℝ)).trans (hR.2.2 0)) hR.2.2 d` |

Inline-derivation grep (`normOne_det_le`, `normOne_hasseDeriv_le` over `Roth/`):
  - (none) — these are used only inside this lemma (Roth/CoeffNorm.lean:268–269). Note the caller re-derives `hB0` from `hB 0`, confirming its redundancy.

### Composition check (Phase 6)

Can `Roth.abs_coeff_det_hasseDeriv_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_le` with an absolute value on `MvPolynomial σ ℤ`
  - Mathlib decls used: `Matrix.det_le`
  - Result: fails — the ℓ¹ norm is submultiplicative but not multiplicative, so it is not an `AbsoluteValue`; mathlib has no other polynomial size function satisfying the hypotheses.
Attempt 2: from the proposed upstream ℓ¹ API: `(norm_coeff_le_l1Norm _ _).trans (l1Norm_det_le _ fun μ ν ↦ (l1Norm_hasseDeriv_le ..).trans (… l1Norm_le_card_mul …))` then `ring`
  - Decls used: not in mathlib (project lemmas, to be upstreamed)
  - Result: succeeds as a short chain (evidence (1), (2) with the project versions), but these are not current mathlib decls.
Conclusion: NOT-COMPOSABLE (from current mathlib); COMPOSABLE from the proposed ℓ¹ API once upstreamed.

### Verdict: `Roth.abs_coeff_det_hasseDeriv_le`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the ingredients (ℓ¹ norm of a determinant, of a Hasse derivative) are standard; the combined constant is specific to Roth's Lemma 3 (clean.tex l.438), never a named general result.
- Generality analysis (Phase 4): only `hB0` (superfluous) and the coefficient-vs-ℓ¹ conclusion can be improved, both compiled; all other generality sits in the ingredient lemmas (already YES-but-generalise-first).
- Mathlib search (Phase 5): not in mathlib; no ℓ¹ polynomial norm; `Matrix.det_le` needs a multiplicative absolute value.
- Composition check (Phase 6): NOT-COMPOSABLE from current mathlib, but a short corollary of the proposed upstream ℓ¹ API.

**Rationale:**

Two buckets fit partially. It is not `NO-composable-from-mathlib` today, because mathlib lacks the ℓ¹ norm. But once the sibling ℓ¹ lemmas land (`MvPolynomial.l1Norm`, `norm_coeff_le_l1Norm`, `l1Norm_det_le`, `l1Norm_hasseDeriv_le`, `l1Norm_le_card_mul`), Lemma 3 becomes a short `calc` of those with a constant tailored to Roth's argument. That is the profile of a project-local corollary, not of a mathlib lemma. It is also not a clean `YES-but-generalise-first`: the only verified improvements are local (drop `hB0`, state the ℓ¹ bound). All mathematically general content is already covered by the ingredient lemmas' own YES verdicts. Shipping it would add a numerical lemma with a single consumer.

Recommended answer: keep it in the project (or in a future Roth/Diophantine-approximation file in mathlib, if the whole Roth proof is ever upstreamed, which is the belongs-elsewhere destination). Refactor locally by dropping `hB0` and, optionally, adding the stronger ℓ¹ form.

Numbered questions (≤5):
1. Is a Roth-specific numerical lemma wanted in mathlib proper only if the full Roth theorem is upstreamed (Mathlib/NumberTheory/DiophantineApproximation/Roth*), and otherwise kept local? (recommended: yes)
2. Should the local lemma be restated without `hB0` (evidence (2)), simplifying Roth/Theta.lean:475? (recommended: yes)
3. Should the stronger ℓ¹ form `Roth.normOne_det_hasseDeriv_le` (evidence (1)), which is what the paper proves, become the primary statement, with the coefficient bound as its corollary? (recommended: yes, cheap)

Next action: the user answers the questions. With the recommended answers: restate locally without `hB0`, update the single call site Roth/Theta.lean:475 (drop the `((abs_nonneg _).trans (hR.2.2 0))` argument), and upstream only the ℓ¹ ingredient lemmas in the MvPolynomial.l1Norm PR.

---

### Next step

Keep `Roth.abs_coeff_det_hasseDeriv_le` local. Drop `hB0` (derive it from `hB 0`), optionally add `normOne_det_hasseDeriv_le` as the primary ℓ¹ form, and update Roth/Theta.lean:475. Do not open a separate mathlib PR. The general content ships with the `MvPolynomial.l1Norm` PR.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.abs_coeff_det_hasseDeriv_le/weaken.lean` (imports `Roth.CoeffNorm`). `lean_diagnostic_messages`: success, no diagnostics. It contains:
  - (1) `normOne_det_hasseDeriv_le`: the ℓ¹ bound without `hB0` (derived as `(abs_nonneg _).trans (hB 0)`).
  - (2) `abs_coeff_det_hasseDeriv_le'`: the coefficient bound without `hB0`, a one-line corollary of (1).
  - (3) The original statement (with `hB0`) recovered from (2) as an `example`.
- WebSearch: 3 queries (literature table rows 1–3). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.438.
- Lean-Finder (1), LeanSearch (1), Loogle (2; one tool error) queries, and mathlib greps as recorded in the search-status block. `lean_local_search` was unavailable (ripgrep missing).
- Project greps: `grep -rn abs_coeff_det_hasseDeriv_le Roth/` (1 call site, Roth/Theta.lean:475).
