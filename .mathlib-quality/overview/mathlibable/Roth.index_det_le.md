---
decl: Roth.index_det_le
file: Roth/Theta.lean
line: 457
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Eq. (17) of the proof of Roth's Lemma 6 (ind F ≤ l Φ for the factored generalised-Wronskian determinant F = U(x_1..x_{p-1}) V(x_p)); a 3-step chain of project lemmas (abs_coeff_det_hasseDeriv_le, coeff_rename_mul_aeval, index_separated_mul_le_aux) about project-only notions (Roth.index, RSet, Θ, lem6Φ, lem6M), with no standalone literature standing, no mathlib counterpart and no ≤3-call mathlib composition, so neither YES nor NO fits; recommended resolution is to keep it in the project.
action: Keep in Roth/Theta.lean (single caller Roth.index_le_lem6 at Roth/Theta.lean:578); optionally make it private and drop the unused R ≠ 0 part of hR (compiled in evidence/Roth.index_det_le/weaken.lean); do not upstream.
---

# Roth.index_det_le

## Inventory entry

### `theorem Roth.index_det_le`
- **Type**: `{τ : Type*} [Fintype τ] {r : Option τ → ℕ} (hr0 : ∀ j, 0 < r j) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} {B : ℝ} {R : MvPolynomial (Option τ) ℤ} (hR : R ∈ RSet B r) {h : Option τ → ℤ} (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) {l : ℕ} (hl : 1 ≤ l) {D : Fin l → (τ →₀ ℕ)} {U : MvPolynomial τ ℤ} {V : Polynomial ℤ} (hU : U ≠ 0) (hV : V ≠ 0) (hUd : ∀ j, degreeOf j U ≤ l * r (some j)) (hVd : V.natDegree ≤ l * r none) (hF : (Matrix.of fun μ ν : Fin l ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) R).det = rename some U * Polynomial.aeval (X none) V) : index (map (Int.castRingHom ℝ) (Matrix.of …).det) (fun j ↦ (h j : ℝ) / q j) r ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l`
- **What**: Let `R ∈ ℛ_p(B; r)` with all `r_j ≤ r₁`, and suppose the generalised Wronskian `F = det(Δ_{D_μ} (1/ν!) ∂^ν_{x_p} R)_{μ,ν<l}` factors as `U(x_1, …, x_{p-1}) V(x_p)` with `U, V ≠ 0`, `deg_{x_j} U ≤ l r_j`, `deg V ≤ l r_p`. Then `ind(F; h/q; r) ≤ l Φ`, where `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q'; l r')` and `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`. Source: clean.tex §5, proof of Lemma 6, eq. (17) (l.734–777).
- **How**: Step 1: coefficients of `F` are bounded by `M` via `Roth.abs_coeff_det_hasseDeriv_le` (Lemma 3) after `simpa` with `lem6M`, `Finset.prod_const`, `Fintype.card_option`, `pow_mul`. Step 2: coefficients of `U` and `V` are bounded by `M`, using `Roth.coeff_rename_mul_aeval` (coefficient of `U·V` in separated variables is a product), `Int.one_le_abs` on the leading coefficient of `V` / a nonzero coefficient of `U` (`MvPolynomial.ne_zero_iff`), `le_mul_of_one_le_right/left`. Step 3: `rw [hF]` and apply the private `Roth.index_separated_mul_le_aux` (Lemma 4-2 + `index_le_Θ` + weight scaling).
- **Hypotheses**: `hr0` (for `index_mul` inside the aux lemma); `hr₁` (uniform degree bound for Lemma 3); `hR` (only the degree and coefficient clauses are used; `R ≠ 0` is superfluous, see evidence); `hh` (coprimality for `index_le_Θ`); `hl` (to clear `/ l`); `hU`, `hV`, `hUd`, `hVd`, `hF` (Lemma 2 output). `[DecidableEq τ]` omitted.
- **Uses from project**: `Roth.RSet`, `Roth.index`, `Roth.lem6Φ`, `Roth.lem6M`, `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), `Roth.abs_coeff_det_hasseDeriv_le` (Roth/CoeffNorm.lean:258), `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:123), `Roth.index_separated_mul_le_aux` (Roth/Theta.lean:414, private)
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:578, `have hupper := index_det_le hr0 hr₁ hR hh hl hU hV hUd hVd hF`). No other occurrence in `Roth/` or `Roth.lean`. Transitively feeds `Roth.Θ_option_le` (Lemma 6, l.593).
- **Visibility**: public
- **Lines**: 452–491 (docstring 452–455, statement 457–467, proof 468–491), proof length 24 lines
- **Notes**: `omit [DecidableEq τ] in` precedes it. Public but single-use and Lemma-6-internal. The `R ≠ 0` component of `hR` is unused (derivable from `hF`, `hU`, `hV`, `hl`).

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.index_le_lem6` (Theta.lean:578), on the main path to Lemma 6.
- Wrapper of 1–2 mathlib calls? No; it chains three project lemmas (Lemma 3 coefficient bound, separated-variables coefficient identity, the aux index bound) over 24 lines.
- Does mathlib have it? No: `Roth.index`, `RSet`, `Θ`, `lem6Φ`, `lem6M`, `MvPolynomial.hasseDeriv` are project definitions (searches in Phase 5).
- Too specific (inline?)? Specific to Lemma 6, but it is a displayed, labelled equation of the source (eq. (17)); inlining would bloat `index_le_lem6`. Keep as a named lemma.
- Well-chosen? Yes, mirrors the source; minor: `hR` could be the two bound clauses only.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `index_det_le`, `lem6Φ`, `lem6M`, `namespace Roth`: no hit. Not a glue lemma (24-line proof), so the full workflow follows. Parent defs `Roth.index` (BORDERLINE), `Roth.lem6Φ`, `Roth.lem6M`, `Roth.RSet` (NO-composable) are not NO-mathlib-has-it, so no re-aim.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` elaborates with only a style warning)
- decl `Roth.index_det_le`:  resolved at Roth/Theta.lean:457
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index across sets of polynomials `Θ_m(B; q; r)` and Lemmas 5, 6, 7 of the source

### Statement (Phase 1)

`Roth.index_det_le` is a theorem stating the following:

Let `R ∈ ℤ[x_1, …, x_p]` be nonzero with `deg_{x_j} R ≤ r_j ≤ r₁` and all coefficients `|·| ≤ B`. Let `l ≥ 1` and `D_0, …, D_{l-1}` multi-indices in `x_1, …, x_{p-1}`, and suppose the generalised Wronskian `F = det(Δ_{D_μ} (1/ν!) ∂^ν_{x_p} R)` equals `U(x_1, …, x_{p-1}) V(x_p)` with `U, V` nonzero, `deg_{x_j} U ≤ l r_j`, `deg V ≤ l r_p`. Then for any `h_j` coprime to `q_j`, `ind(F; h_1/q_1, …, h_p/q_p; r) ≤ l Φ` with `Φ = Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}) + Θ_1(M; q_p; l r_p)` and `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`.

Variables / typeclasses involved (Lean side):
- `τ` with `[Fintype τ]`: the first `p-1` variables; `Option τ`: all variables, `none = x_p`.
- `r`, `r₁`: weights / degree bounds and their maximum; `q`, `h`: denominators and numerators of the point; `B`: coefficient bound; `l`, `D`: Wronskian size and row orders; `U`, `V`: the factors.

Hypotheses (Lean side):
- `hr0`: positive weights. `hr₁`: `r_j ≤ r₁`. `hR`: `R ∈ ℛ(B; r)`. `hh`: `gcd(h_j, q_j) = 1`. `hl`: `l ≥ 1`.
- `hU`, `hV`, `hUd`, `hVd`, `hF`: the factorisation from Lemma 2 with its degree bounds.

Conclusion (math): `ind F ≤ l Φ`.

Conclusion (Lean): `index (map (Int.castRingHom ℝ) F) (fun j ↦ (h j : ℝ) / q j) r ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an intermediate displayed step (eq. (17)) inside the proof of Lemma 6, not a main result or a new structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 24 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma proof index of generalized Wronskian factorization U(x_1..x_{p-1})V(x_p) index bounded by l Theta | partial | Roth's lemma by induction on the number of variables; generalised Wronskian factorisation | arXiv 2502.00731 (Lemma 3.9), arXiv 1305.0926, Roth 1955; no standalone statement of `ind F ≤ lΦ` |
| 2 | WebSearch (general form) | index of product of polynomials in disjoint variables equals sum of indices Roth lemma | partial | index additivity for products / disjoint variables listed among basic index properties | arXiv math/0307203 (index definition), arXiv 2502.00731 (Lemmas 2.21–2.22) |
| 3 | WebSearch (aliases) | coefficients of product of polynomials in separate variables bounded height Gauss lemma Roth theorem proof Cassels Diophantine approximation Lemma 6 | partial | height of a product of polynomials in disjoint variables is the product of heights; Gauss lemma | arXiv 2502.00731 proves height inequalities for products; Cassels' numbering not confirmed |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | read clean.tex l.730–777 (proof of Lemma 6, eq. (17)) | yes | `abc(U), abc(V) < M`; `U ∈ ℛ_{p-1}(M; lr')`, `V ∈ ℛ_1(M; lr_p)`; Lemma 4-2 additivity; `ind F ≤ lΦ` | the Lean statement is exactly eq. (17) with the source's M and Φ |
| 6 | nLab | index of a polynomial; Wronskian | no | n/a | no entry on Roth's index or this estimate |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Diophantine estimate, not algebraic geometry; no index-of-polynomial entry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread on this step; routine inside Roth's lemma |
| 10 | recent arXiv | 2502.00731, 1305.0926, 1806.10737 | partial | as #1–#3 | the step is always proved inline within the Roth-lemma induction |

### Literature summary (Phase 3)

Concept identified as: the upper bound `ind F ≤ lΦ` in the induction step of Roth's lemma (Lemma 6 of the source), combining a height bound on the Wronskian (Lemma 3), height multiplicativity for products in disjoint variables, additivity of the index in disjoint variables (Lemma 4-2), and the definition of Θ as a supremum.
Sources agree on the standard form: yes, but only as an inline step of Roth's lemma.
Most general standard form: index additivity `ind(UV) = ind U + ind V` for polynomials in disjoint variables, plus `ind ≤ Θ` for polynomials of bounded height and degree; the specific constants `M`, `Φ` are paper-specific.
Generality dimensions where the literature varies:
  - height: max-coefficient (this source) vs Mahler measure / projective height (Bombieri–Gubler, Hindry–Silverman).
  - constants: paper-specific `M`.
Disagreement with the literature: none.

### Generality analysis — `Roth.index_det_le`

Literature-standard form: clean.tex eq. (17).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hR : R ∈ RSet B r` | nonzero + degree + coefficient bounds | `R ∈ ℛ_p(B; r)` | yes (cosmetic) | `R ≠ 0` follows from `hF`, `hU`, `hV`, `hl`; compiled in evidence (1) |
| 2 | `hr0` | `0 < r j` | positive weights | no | needed by `index_mul` in the aux lemma |
| 3 | `hr₁` | `r j ≤ r₁` | `r_1 > … > r_p` | already weaker than source | only the uniform bound is used |
| 4 | `hl` | `1 ≤ l` | `1 ≤ l ≤ r_p + 1` | no | needed to divide by `l`; upper bound already dropped |
| 5 | `hh` | coprime `h_j, q_j` | same | no | needed by `index_le_Θ` |
| 6 | `hU`, `hV` | nonzero | nonzero | no | needed for `Int.one_le_abs` and for `index_mul` |
| 7 | ring `ℤ`, Roth index over `ℝ` | fixed | fixed | no | the statement is about integer polynomials and Θ over ℤ |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (up to the cosmetic removal of `R ≠ 0` from `hR`, which is a hypothesis implied by the others, verified in evidence (1))
Number of weakening opportunities found: 1 (verified: evidence (1), `lean_diagnostic_messages` clean apart from a long-line style warning)
Proposed restatement: replace `hR` by `hRd : ∀ j, degreeOf j R ≤ r j` and `hRc : ∀ d, |(R.coeff d : ℝ)| ≤ B`.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | data-level bounds | — |
| 2 | Sequences vs filters? | no | finite algebraic inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | `RSet` is a set of polynomials with bounds; nothing to bundle | — |
| 5 | Field-specific vs typeclass-weakened? | no | integrality is essential (`Int.one_le_abs`) | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | the paper-specific constant `M` and Θ are fixed objects | — |
| 8 | Concrete-via-abstract? | partially | after Step 2 the proof is the generic aux lemma (index of `U·V` in disjoint variables ≤ sum of Θ bounds); the concrete Wronskian enters only through Lemma 3's coefficient bound | the abstract part is already split out (`index_separated_mul_le_aux`) |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: the statement is a paper-specific inequality with paper-specific constants about project definitions; its generic pieces (index additivity, height multiplicativity in disjoint variables) are already separate project lemmas.

### Proof strategy — `Roth.index_det_le`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | mild | a mathlib lemma "coefficient of `rename f p * rename g q` for disjoint `f`, `g` is a product of coefficients" (project's `coeff_rename_mul_aeval`) | CHEAP (separate follow-up) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (follows the source: coefficient bound, height multiplicativity, index additivity)
  - Missing mathlib API: a disjoint-variables coefficient-product lemma (already a project lemma in Roth/Separation.lean; assessed separately).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_det_le`

[A] Lean-Finder       "coefficient of product of two multivariate polynomials in disjoint variables is the product of coefficients"   hits: `MvPolynomial.coeff_mul`, `MvPolynomial.coeff_monomial_mul`, `MonomialOrder.coeff_mul_of_add_of_degree_le`, `Polynomial.coeff_prod_of_natDegree_le` (building blocks only)
[B] Loogle            `Matrix.det, MvPolynomial.rename`   no hits; `Matrix.det, MvPolynomial.rename, MvPolynomial.hasseDeriv` rejected (`MvPolynomial.hasseDeriv` is not a mathlib constant)
[C] LeanSearch        "order of vanishing of product of polynomials in disjoint sets of variables equals sum of orders"   hits: `analyticOrderAt_mul`, `analyticOrderNatAt_mul`, `meromorphicOrderAt_mul` (one-variable analytic orders; not applicable)
[D] Grep mathlib src  `index_det_le`, `lem6Φ`, `lem6M`, `namespace Roth`, `Roth` under NumberTheory   no relevant hits (only Liouville docs mention Roth)
[E] Name pattern      `Roth.index_det_le`   no mathlib decl in a matching namespace

Searched for both:
  - the user's current form (eq. (17) for the Roth Wronskian)
  - the literature-standard pieces (index additivity in disjoint variables; height multiplicativity)

Concluded: not in mathlib (all 5 methods exhausted); only building blocks (`MvPolynomial.coeff_mul`, `Matrix.det_apply`).

### Normal-form check — `Roth.index_det_le`

Equivalent formalisms: (a) `index F ≤ l * lem6Φ …`; (b) `index F / l ≤ lem6Φ …`.
Does mathlib already have a canonical form? no.
Proposed canonical form: current (upper bound with `index` on the LHS, matching `index_le_Θ` and the source).
RHS convention respected? yes

### Syntactic generality — `Roth.index_det_le`

Alternative restatements attempted:
- current (`hR : R ∈ RSet B r`)
- `hRd`, `hRc` without `R ≠ 0` (evidence (1), compiles via the original)
- `hF` stated for the mapped real polynomial: rejected, the integrality of `U`, `V` is essential

Chosen restatement: current.
Justification: the sole caller (Theta.lean:578) already has `hR : R ∈ RSet B r`, so the bundled hypothesis is easiest to supply.

### Superfluous-argument audit — `Roth.index_det_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype τ]` | yes | `Roth.index`, `Fintype.card τ` |
| 2 | `[DecidableEq τ]` | no | already omitted |
| 3 | `hR.1 : R ≠ 0` | no | implied by `hF`, `hU`, `hV`, `hl` (evidence (1)) |
| 4 | `hr0`, `hr₁`, `hh`, `hl`, `hU`, `hV`, `hUd`, `hVd`, `hF` | yes | each used in Steps 1–3 |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 component (`R ≠ 0` inside `hR`), harmless at the call site

Overall: SHIP-AS-STATED (locally)

### Call sites — `Roth.index_det_le`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:578 | `have hupper := index_det_le hr0 hr₁ hR hh hl hU hV hUd hVd hF` in `Roth.index_le_lem6` |

Inline-derivation grep:
  - (none) — no other site re-derives an upper index bound for the Wronskian.

### Composition check (Phase 6)

Can `Roth.index_det_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `abs_coeff_det_hasseDeriv_le` + `coeff_rename_mul_aeval` + `index_separated_mul_le_aux`.
  - Decls used: all project lemmas (none in mathlib).
  - Result: fails as a mathlib composition; it is a three-step chain of project lemmas plus coefficient bookkeeping (24 lines).

Attempt 2: mathlib-only via `MvPolynomial.coeff_mul`, `Matrix.det_apply`.
  - Result: fails; mathlib has no Roth index, Θ or Wronskian height bound.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.index_det_le`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the statement is eq. (17) of the source's proof of Lemma 6 (clean.tex l.734–777) and a routine inline step of Roth's lemma; no source states it standalone.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; one cosmetic redundancy (`R ≠ 0`) verified in evidence (1).
- Mathlib search (Phase 5): not in mathlib; only building blocks.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The theorem is a paper-specific inequality with paper-specific constants (`lem6M`, `lem6Φ`, both NO-composable) about the project's own `Roth.index`, `RSet` and `Θ`, with one caller. It fails the YES buckets (no standalone literature standing and no mathlib gap it fills by itself), and it fails the NO buckets (mathlib does not have it and it is not a ≤3-call mathlib composition). Like its siblings `Roth.sum_max_sub_le_index_det` and `Roth.min_le_sum_max`, it is therefore BORDERLINE with a clear recommendation to keep it project-local.

The only mathlib-relevant fragments are generic: the coefficient of a product of polynomials in disjoint variables (`Roth.coeff_rename_mul_aeval`) and Lemma 3's height bound (`Roth.abs_coeff_det_hasseDeriv_le`, BORDERLINE), which are assessed in their own reports.

Numbered questions:
1. Keep `Roth.index_det_le` project-local in Roth/Theta.lean (recommended: yes)?
2. Make it `private` (single caller `Roth.index_le_lem6`, Lemma-6-internal)? Yes or no.
3. Replace `hR` by the two bound clauses, dropping the redundant `R ≠ 0` (evidence (1))? Yes or no (the caller already has `hR`, so the default is no).

Next action: user answers the questions; default is to keep the lemma as is in Roth/Theta.lean.

### Next step

Keep `Roth.index_det_le` in Roth/Theta.lean (caller `Roth.index_le_lem6`, Theta.lean:578). Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_det_le/weaken.lean` (imports `Roth.Theta`; `lean_diagnostic_messages`: success, one long-line style warning only):
  - (1) an `example` proving the statement with `hR` replaced by `hRd`, `hRc` (no `R ≠ 0`), deriving `R ≠ 0` from `hF`, `hU`, `hV`, `hl` (zero matrix has zero determinant via `Matrix.det_eq_zero_of_column_eq_zero`) and then applying `Roth.index_det_le`.
- WebSearch ×3 (queries in the table); local read of `.mathlib-quality/references/clean.tex` l.730–777; Lean-Finder, Loogle ×2, LeanSearch and mathlib grep as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
- Sources: https://arxiv.org/pdf/2502.00731, https://arxiv.org/pdf/1305.0926, https://arxiv.org/pdf/math/0307203, https://arxiv.org/pdf/1806.10737, Roth 1955 (Mathematika, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational-approximations-to-algebraic-numbers.pdf).
