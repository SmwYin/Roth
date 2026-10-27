---
decl: Roth.norm_coeff_modByMonic_le
file: Roth/MainLemma.lean
line: 252
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Coefficient-norm bound for the monic remainder over any seminormed ring, ht(P mod f) at most (1+ht f)^(deg P+1-deg f) ht P; standard (arXiv 1401.7696 Lemma 4.5, Roth-Ridout math/0307203), absent from mathlib (only the algebraic analogue coeff_modByMonic_mem_pow_natDegree_mul in CoeffMem), not composable; mathlib form should be stated with Polynomial.supNorm (compiled corollary).
action: Upstream to Mathlib/Analysis/Polynomial/Norm.lean as Polynomial.supNorm_modByMonic_le (supNorm form, compiled in evidence/checks.lean) plus the coefficientwise form with explicit bounds A C s; keep project lemma (single caller MainLemma l.512) or rewrite that caller via the supNorm form after upstreaming.
---

# Roth.norm_coeff_modByMonic_le

## Inventory entry

### `theorem Roth.norm_coeff_modByMonic_le`
- **Type**: `∀ {R : Type*} [SeminormedRing R] {f : R[X]} {A : ℝ}, (∀ i, ‖f.coeff i‖ ≤ A) → ∀ (P : R[X]) {C : ℝ}, (∀ i, ‖P.coeff i‖ ≤ C) → ∀ {s : ℕ}, P.natDegree ≤ s → ∀ (i : ℕ), ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C`
- **What**: If every coefficient of f has norm at most A, every coefficient of P has norm at most C, and deg P ≤ s, then every coefficient of the remainder P mod f (mathlib's `modByMonic`) has norm at most (1 + A)^(s + 1 − deg f) · C. No monicity is assumed (for nonmonic f, `modByMonic` returns P and the bound is trivial).
- **How**: Derives `1 ≤ 1 + A` from `hfA 0`; disposes of `f = 1` by `simpa` (remainder 0); then strong induction on `s` (`Nat.strong_induction_on`). If `P %ₘ f = P` the bound follows from `hP` and `one_le_pow₀`; otherwise the private helper `exists_norm_coeff_reduction_aux` supplies Q of degree ≤ s − 1, coefficient bound (1 + A)·C and `P %ₘ f = Q %ₘ f`, and the induction hypothesis plus `pow_succ`/`lia` closes it.
- **Hypotheses**: `[SeminormedRing R]` (no commutativity, no monicity); `hfA` coefficient bound for f; `hP` coefficient bound for P; `hs : P.natDegree ≤ s`. Nonnegativity of A, C is derived.
- **Uses from project**: `Roth.exists_norm_coeff_reduction_aux` (private)
- **Used by**: Roth/MainLemma.lean:512 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, private, `norm_coeff_modByMonic_le (by simpa [Int.norm_eq_abs] using hA) _ ... i`); also listed in the module docstring (MainLemma l.41). `grep -rn norm_coeff_modByMonic_le Roth/` finds no other use.
- **Visibility**: public
- **Lines**: 245–272 (docstring 245–251, statement 252–254), proof length 18 lines
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, once (MainLemma l.512), and it is the named content of the source's "division by f" step in Lemma 9.
- Wrapper of 1–2 mathlib calls? No: strong induction with a 31-line private step lemma.
- Does mathlib have it? No. Loogle `‖Polynomial.coeff (_ %ₘ _) _‖`: no hits; LeanSearch/Lean-Finder return only algebraic results (`Polynomial.coeff_modByMonic_mem_pow_natDegree_mul`, `coeff_divModByMonicAux_mem_span_pow_mul_span` in Mathlib/Algebra/Polynomial/CoeffMem.lean); grep of mathlib for norm + modByMonic: nothing; `Mathlib/Analysis/Polynomial/Norm.lean` (`Polynomial.supNorm`) has no division lemmas.
- Too specific (inline?)? No; general seminormed-ring statement, reusable.
- Well-chosen? Yes; general and hypothesis-light. The `s` parameter is a convenience over `P.natDegree`.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "For polynomials"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `norm_coeff_modByMonic` / `namespace Roth`: no hit. Not a glue lemma; full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run per the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates cleanly via lean-lsp)
- decl `Roth.norm_coeff_modByMonic_le`: resolved at Roth/MainLemma.lean:252
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma (Lemma 9) via pigeonhole over box polynomials and remainders modulo f

### Statement (Phase 1)

`Roth.norm_coeff_modByMonic_le` is a theorem stating the following:

Let R be a seminormed ring, f, P ∈ R[X]. Suppose all coefficients of f have norm ≤ A, all coefficients of P have norm ≤ C, and deg P ≤ s. Then every coefficient of the remainder of P upon division by f (when f is monic; P itself otherwise) has norm ≤ (1 + A)^(s + 1 − deg f) · C. In height notation: H(P mod f) ≤ (1 + H(f))^(deg P + 1 − deg f) H(P).

Variables / typeclasses involved (Lean side):
- `R` with `[SeminormedRing R]`: coefficient ring with submultiplicative seminorm.
- `f`: the divisor; `P`: the dividend; `i`: coefficient index.

Hypotheses (Lean side):
- `hfA`: height of f ≤ A.
- `hP`: height of P ≤ C.
- `hs`: deg P ≤ s (degree budget).

Conclusion (math): height of P mod f ≤ (1 + A)^(s + 1 − deg f) C.

Conclusion (Lean): `‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a supporting estimate (polynomial-division height bound) inside the proof of Roth's lemma; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 18 substantive lines
One-liner verdict: n/a (kind is theorem, not def)
Conclusion: check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | coefficient bound remainder polynomial division monic divisor (1+A)^(m-n+1) height | partial | ht of quotient and remainder ≤ (d+1)(h + 2 log(d+1)) | arXiv 2503.20071 Prop. 3.5 (Cramer-rule bound, logarithmic height, different shape) |
| 2 | WebSearch (general form) | height of remainder and quotient of polynomial division by monic polynomial bound Mignotte | yes | ht(r) ≤ M₁ (1 + M₂)^(deg a − deg b + 1) | arXiv 1401.7696 Lemma 4.5: exactly our form (M₁ = ht a, M₂ = ht b), proved by tracking the division steps; Mignotte bounds (arXiv 2308.03885) concern exact divisors, not remainders |
| 3 | WebSearch (aliases / source context) | Roth theorem proof Lemma 9 leading-term elimination division by f coefficients bounded (1+A) | yes | each elimination multiplies height by ≤ (A+1); iterate to (A+1)^(s−n+1) | arXiv math/0307203 (quantitative Roth–Ridout) states the same step inline |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `1+A`, `elimination` | yes | l.1458–1466 `abc(T) ≤ (1+A)^{max(0,s−n+1)} B_1^{1+2δ}`; l.1469–1475 Lean note "each leading-term elimination multiplies the bound by at most 1+A" | exact match; `max(0, s−n+1)` is ℕ-subtraction `s + 1 − n` |
| 6 | nLab | polynomial division / height | no | n/a | nLab has no coefficient-size estimates |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Stacks has division algorithm only algebraically (no norms); not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–2) | no | n/a | no named result; folklore of computer algebra |
| 10 | recent arXiv | (searches 1–2 hit arXiv 2503.20071, 1401.7696) | yes | as rows 1–2 | used in computer algebra / primality-testing complexity analyses |

### Literature summary (Phase 3)

Concept identified as: height (sup-norm) bound for the remainder of division by a monic polynomial; folklore in computer algebra and Diophantine approximation.
Sources agree on the standard form: yes for the multiplicative form ht(r) ≤ ht(a)(1 + ht(b))^(deg a − deg b + 1) (arXiv 1401.7696 Lemma 4.5, math/0307203, project source); arXiv 2503.20071 gives an alternative additive-log Cramer bound.
Most general standard form: for a monic b over a (semi)normed ring, H(a mod b) ≤ (1 + H(b))^(deg a − deg b + 1) H(a).
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℂ in the literature; any seminormed ring here (more general).
  - height used: sup norm (here), occasionally ℓ¹ or log-height.
Disagreement with the literature: none; the Lean form is at least as general (no monicity, arbitrary seminormed ring, degree budget s).

### Generality analysis — `Roth.norm_coeff_modByMonic_le`

Literature-standard form (from Phase 3): H(P mod f) ≤ (1 + H(f))^(deg P + 1 − deg f) H(P) over ℤ or ℂ, f monic.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[SeminormedRing R]` | seminormed ring | ℤ or ℂ | no | already more general; `norm_mul_le` and `norm_sub_le` are used, and `Polynomial.supNorm` itself is defined for `SeminormedRing` |
| 2 | monicity of f | not assumed | f monic | already weaker | `modByMonic` returns P for nonmonic f |
| 3 | `hfA`, `hP` | explicit bounds A, C | heights H(f), H(P) | equivalent | taking A := f.supNorm, C := P.supNorm gives the supNorm form (evidence check 1) |
| 4 | `hs : P.natDegree ≤ s` | degree budget | exponent deg P + 1 − deg f | equivalent | s := P.natDegree recovers the literature exponent |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (no hypothesis to drop; all weakenings are already present)
Number of weakening opportunities found: 0
Proposed restatement: none from 4b (see 4c for the idiomatic supNorm form).
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | already typeclass-parametric | — |
| 2 | Sequences/metric vs filters? | no | no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | yes (mild) | the bound-hypotheses `∀ i, ‖p.coeff i‖ ≤ A` are the unbundled form of `p.supNorm ≤ A`; mathlib has `Polynomial.supNorm` (Mathlib/Analysis/Polynomial/Norm.lean) | `Polynomial.le_supNorm`, `exists_eq_supNorm`, `supNorm_eq_iSup`, `supNorm_C`/`supNorm_X`, Mahler-measure bounds (`mahlerMeasure_le_sqrt_sum_sq_norm_coeff`) |
| 5 | Field-specific vs typeclass-weakened? | no | already seminormed ring | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | ℕ degrees intrinsic | — |
| 8 | Concrete-via-abstract? | no | statement mentions no concrete object | — |
| 9 | False-generalisation guard | no false generalisation | the supNorm form is the same inequality with A, C, s instantiated canonically | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement (compiled, evidence check 1):
    `theorem Polynomial.supNorm_modByMonic_le {R : Type*} [SeminormedRing R] (P f : R[X]) : (P %ₘ f).supNorm ≤ (1 + f.supNorm) ^ (P.natDegree + 1 - f.natDegree) * P.supNorm`
  - Cost: CHEAP (four-line corollary of the current lemma via `exists_eq_supNorm`, `le_supNorm`)
  - Mathlib downstream this enables: plugs remainder bounds into the existing `Polynomial.supNorm` API (`le_supNorm`, `supNorm_eq_iSup`, and the Mahler-measure / Landau inequalities in Mathlib/Analysis/Polynomial/MahlerMeasure.lean that are stated against `supNorm`/coefficient norms); provides the analytic counterpart of the algebraic `Polynomial.coeff_modByMonic_mem_pow_natDegree_mul`.
  - Real mathematical improvement: the bound is about the height of a polynomial, which mathlib already names `supNorm`; stating it there makes it chain with other height estimates without unpacking coefficientwise bounds.

### Proof strategy — `Roth.norm_coeff_modByMonic_le`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (minor) | the step lemma's `hmod` unfolds the internal `Polynomial.divModByMonicAux`; for mathlib, prove it with `Polynomial.modByMonic_eq_of_dvd_sub` (P − Q is a multiple of f), or follow the induction pattern of `coeff_divModByMonicAux_mem_span_pow_mul_span` in Mathlib/Algebra/Polynomial/CoeffMem.lean | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (minor)
  - Proposed strategy: same strong induction, but avoid unfolding `divModByMonicAux` in the private step (use `modByMonic_eq_of_dvd_sub`), mirroring CoeffMem's structure.
  - Cost: CHEAP
  - Missing mathlib API: none beyond the lemma itself (a matching quotient bound for `/ₘ` would be a natural companion).
  - Would refactoring make the proof strictly shorter / cleaner? cleaner (robust against mathlib internals), similar length.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.norm_coeff_modByMonic_le`

[A] Lean-Finder       "coefficients of p modByMonic q are bounded by (1 + bound on coefficients of q) to the power degree times bound on coefficients of p"   only algebraic: `Polynomial.coeff_divModByMonicAux_mem_span_pow_mul_span`, `coeff_modByMonic_mem_pow_natDegree_mul`, `coeff_divByMonic_mem_pow_natDegree_mul`
[B] Loogle            `‖Polynomial.coeff (_ %ₘ _) _‖`   no hits
[C] LeanSearch        "bound on the norm of coefficients of the remainder of polynomial division by a monic polynomial"   `coeff_modByMonic_mem_pow_natDegree_mul`, `natDegree_modByMonic_le`, `modByMonic_eq_sub_mul_div`; no norm bound
[D] Grep mathlib src  `norm.*modByMonic`, `‖.*%ₘ`, `coeff_modByMonic`, `supNorm` (files: Analysis/Polynomial/Norm.lean, MahlerMeasure.lean)   no division bound; supNorm API has only basic lemmas (l.56–105)
[E] Name pattern      `norm_coeff_modByMonic`, `supNorm_modByMonic`   no mathlib decl

Searched for both:
  - the user's current form (coefficientwise bounds A, C, s)
  - the literature/idiomatic form (`supNorm` of the remainder)

Concluded: found a partial match (`Polynomial.coeff_modByMonic_mem_pow_natDegree_mul`, Mathlib/Algebra/Polynomial/CoeffMem.lean:86, the algebraic submodule analogue); not in mathlib as a norm bound.

### Normal-form check — `Roth.norm_coeff_modByMonic_le`

Equivalent formalisms: coefficientwise `∀ i, ‖(P %ₘ f).coeff i‖ ≤ ...` with free bounds A, C; `(P %ₘ f).supNorm ≤ (1 + f.supNorm)^... * P.supNorm`.
Does mathlib already have a canonical form? Yes for the height: `Polynomial.supNorm`. Our statement is not stated against it → mathlib version should be the supNorm form (normal form), with the coefficientwise flexible-bound form as a companion (it is the one call sites over ℤ consume). RHS convention: n/a (not an iff).

### Syntactic generality — `Roth.norm_coeff_modByMonic_le`

Alternative restatements attempted:
- supNorm form (compiled, check 1).
- coefficientwise with explicit A, C, s (current).
- exponent `P.natDegree + 1 - f.natDegree` without `s`.

Chosen restatement: ship both: supNorm form as the headline, current flexible form as the workhorse (the caller at MainLemma l.512 supplies bounds A, C and degree budget s that are not the exact sup norm / degree).
Justification: the flexible form avoids computing supNorm and natDegree exactly at call sites.

### Superfluous-argument audit — `Roth.norm_coeff_modByMonic_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[SeminormedRing R]` | yes | `norm_mul_le`, `norm_sub_le` |
| 2 | `hfA` | yes | bounds the eliminated multiple of f |
| 3 | `hP` | yes | base bound |
| 4 | `hs` | yes | controls the exponent |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (add the `Polynomial.supNorm` form as the normal form)
Syntactic generality: OK (keep the flexible form as companion)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (add the supNorm form).

### Call sites — `Roth.norm_coeff_modByMonic_le`

Internal use count: 0 outside the declaring file; 1 in the declaring file
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:512 | `norm_coeff_modByMonic_le (by simpa [Int.norm_eq_abs] using hA) _ (by simpa [Int.norm_eq_abs] using hcD) (natDegree_diag_le _ hdP) i` (in private `abs_coeff_diag_hasseDeriv_modByMonic_le_aux`) |

Inline-derivation grep (`%ₘ` with norm/abs bounds across Roth/): (none besides this declaration and its private step `exists_norm_coeff_reduction_aux`).

### Composition check (Phase 6)

Can `Roth.norm_coeff_modByMonic_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: via `Polynomial.coeff_modByMonic_mem_pow_natDegree_mul` with Mp, Mq the ℤ-spans of coefficients.
  - Mathlib decls used: `coeff_modByMonic_mem_pow_natDegree_mul`
  - Result: fails — membership in Mq^deg · Mp gives a sum of products with an uncontrolled number of terms and ℤ-coefficients, so no norm bound of the shape (1 + A)^(s+1−n) C follows.
Attempt 2: via `modByMonic_eq_sub_mul_div` and a quotient bound.
  - Result: fails — mathlib has no norm bound on `P /ₘ f` either.

Conclusion: NOT-COMPOSABLE (needs the induction on degree; 18-line proof plus 31-line step lemma)

### Verdict: `Roth.norm_coeff_modByMonic_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard multiplicative height bound (arXiv 1401.7696 Lemma 4.5; math/0307203; clean.tex l.1458–1475).
- Generality analysis (Phase 4): MAXIMALLY GENERAL in hypotheses (seminormed ring, no monicity); 4c modern idiom: restate via `Polynomial.supNorm` (compiled).
- Mathlib search (Phase 5): only the algebraic analogue `Polynomial.coeff_modByMonic_mem_pow_natDegree_mul`; no norm bound.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The lemma is the standard height estimate for division by a monic polynomial: each leading-term elimination multiplies the height by at most 1 + H(f), and there are at most deg P + 1 − deg f eliminations. It appears as Lemma 4.5 of arXiv 1401.7696 and inline in Roth-type proofs (math/0307203), and the Lean form is more general than the literature (any seminormed ring, monicity not required, degree budget s). Mathlib has the polynomial height (`Polynomial.supNorm`, Mathlib/Analysis/Polynomial/Norm.lean) and the algebraic version of exactly this division-step induction (`coeff_modByMonic_mem_pow_natDegree_mul`, Mathlib/Algebra/Polynomial/CoeffMem.lean), but no norm bound for `%ₘ` or `/ₘ`; the gap is concrete: the supNorm API stops at basic lemmas and has nothing about division.

The "generalise first" part is the MODERN-IDIOM restatement: mathlib should get `Polynomial.supNorm_modByMonic_le` stated against `supNorm` (compiled as a corollary in the evidence file), with the present flexible-bound version as a companion lemma, and the private step lemma's unfolding of `divModByMonicAux` replaced by `modByMonic_eq_of_dvd_sub`. No hypothesis needs dropping.

Reason for the generalisation: MODERN-IDIOM (Bourbaki 2.0) — state against `Polynomial.supNorm`.
Proposed restatement:
```lean
theorem Polynomial.supNorm_modByMonic_le {R : Type*} [SeminormedRing R] (P f : R[X]) :
    (P %ₘ f).supNorm ≤ (1 + f.supNorm) ^ (P.natDegree + 1 - f.natDegree) * P.supNorm
-- companion (current form):
theorem Polynomial.norm_coeff_modByMonic_le {R : Type*} [SeminormedRing R] {f : R[X]} {A : ℝ}
    (hfA : ∀ i, ‖f.coeff i‖ ≤ A) (P : R[X]) {C : ℝ} (hP : ∀ i, ‖P.coeff i‖ ≤ C) {s : ℕ}
    (hs : P.natDegree ≤ s) (i : ℕ) :
    ‖(P %ₘ f).coeff i‖ ≤ (1 + A) ^ (s + 1 - f.natDegree) * C
```
Estimated cost of regeneralisation: CHEAP (supNorm form already compiles from the current lemma).
Mathlib downstream this enables:
  - composes with `Polynomial.le_supNorm`, `exists_eq_supNorm`, `supNorm_eq_iSup` and height/Mahler-measure estimates in Mathlib/Analysis/Polynomial/MahlerMeasure.lean;
  - gives the analytic counterpart of `coeff_modByMonic_mem_pow_natDegree_mul` (useful for effective Diophantine and computer-algebra bounds over ℤ);
  - a natural companion quotient bound `supNorm_divByMonic_le` could follow by the same induction.
Proposed mathlib location: Mathlib/Analysis/Polynomial/Norm.lean (needs `Mathlib.Algebra.Polynomial.Div`).
PR grouping: alone, or with a `divByMonic` companion; the project's `Roth.exists_norm_coeff_reduction_aux` travels as a private helper.
Next action: run `/generalise Roth.norm_coeff_modByMonic_le` to settle the supNorm headline form and the `modByMonic_eq_of_dvd_sub` cleanup of the step lemma, then `/cleanup` and open the PR.

---

### Next step

Add `Polynomial.supNorm_modByMonic_le` (supNorm form) plus the coefficientwise form to Mathlib/Analysis/Polynomial/Norm.lean; in the project keep the lemma for its single caller (MainLemma l.512) until the upstream version lands, then point that caller at the mathlib name.

## Evidence
- `grep -rn norm_coeff_modByMonic_le Roth/`: docstring mention l.41, definition l.252, single use l.512.
- lean_loogle `‖Polynomial.coeff (_ %ₘ _) _‖`: no hits; lean_leansearch and lean_leanfinder: only algebraic CoeffMem results and basic `modByMonic` API (Phase 5).
- grep of `.lake/packages/mathlib/Mathlib/`: no `namespace Roth`, no `norm_coeff_modByMonic`, no norm bound mentioning `%ₘ`/`modByMonic`; `Polynomial.supNorm` in Analysis/Polynomial/Norm.lean (l.53) with lemmas l.56–105 only; `coeff_modByMonic_mem_pow_natDegree_mul` at Algebra/Polynomial/CoeffMem.lean:86.
- WebSearch x3 (Phase 3 rows 1–3): arXiv 1401.7696 Lemma 4.5 (same form), arXiv math/0307203 (same step inline), arXiv 2503.20071 Prop. 3.5 (different Cramer-type bound).
- clean.tex l.1453–1475: source statement and Lean note.
- Evidence file `.mathlib-quality/overview/evidence/Roth.norm_coeff_modByMonic_le/checks.lean` (lean_diagnostic_messages: no errors or warnings): (1) `supNorm_modByMonic_le` compiled as a corollary of the project lemma via `exists_eq_supNorm`/`le_supNorm`; (2) `#check` of mathlib's algebraic analogue `Polynomial.coeff_modByMonic_mem_pow_natDegree_mul`; (3) `#check` of the declaration.
