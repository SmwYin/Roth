---
decl: Roth.natDegree_diag_le
file: Roth/CoeffNorm.lean
line: 183
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: Re-aimed at diag = aeval (fun _ ↦ X), the bound is one call to MvPolynomial.aeval_natDegree_le (n = 1) fed by totalDegree ≤ ∑ degreeOf, itself a one-line simpa from totalDegree_le_degrees_card, degreeOf_def and Multiset.sum_count_eq_card; compiled over any CommSemiring, nothing new for mathlib.
action: Do not upstream; optionally reprove Roth.natDegree_diag_le as the aeval_natDegree_le composition (needs import Mathlib.RingTheory.Polynomial.Basic in Roth/CoeffNorm.lean), keeping the name for its single call site Roth/MainLemma.lean:513.
---

# Roth.natDegree_diag_le

## Inventory entry

### `theorem Roth.natDegree_diag_le`
- **Type**: `{σ : Type*} [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) : (diag P).natDegree ≤ ∑ j, r j`
- **What**: If `P` has degree at most `r_j` in each variable `x_j`, the diagonal specialisation `P(x, …, x)` has degree at most `∑ r_j`.
- **How**: Rewrites with `diag_eq_sum`, applies `Polynomial.natDegree_sum_le_of_forall_le` with `Polynomial.natDegree_monomial_le`, then `Finsupp.degree_eq_sum` and `Finset.sum_le_sum` with `MvPolynomial.monomial_le_degreeOf` and `hP`.
- **Hypotheses**: `[Fintype σ]` (for `∑ j, r j`); `hP` (partial degree bounds).
- **Uses from project**: `Roth.diag`, `Roth.diag_eq_sum`
- **Used by**: Roth/MainLemma.lean:513 (private `abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, supplies the degree hypothesis of `norm_coeff_modByMonic_le`).
- **Visibility**: public
- **Lines**: 181–189 (docstring 181–182, statement 183–184), proof length 5 lines
- **Notes**: Source: §6 proof of Lemma 9 (clean.tex l.1468, "using `s ≤ ∑_j r_j ≤ m r_1`"). Statement is over `ℤ` only because `diag` is.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:513.
- Wrapper of 1–2 mathlib calls? Effectively yes after re-aiming: `MvPolynomial.aeval_natDegree_le` plus a one-line `totalDegree ≤ ∑ degreeOf` bound (evidence (1), (2)).
- Does mathlib have it? Not verbatim; the sharper `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P` is `aeval_natDegree_le` with `n = 1` (evidence (4)).
- Too specific (inline)? Single call site; inlining the composition is possible but would need the extra import `Mathlib.RingTheory.Polynomial.Basic` and would clutter a Lemma 9 helper. The name matches the paper step.
- Well-chosen? Yes as a project-local lemma about the project-local `diag`.
- Conclusion: `KEEP` — action: keep the name; optionally reprove it via `aeval_natDegree_le` (evidence (2)).

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.natDegree_diag_le` not in mathlib (no `namespace Roth` there). Not a glue lemma (5-line proof). Parent `Roth.diag` is `NO-composable-from-mathlib` (it is literally `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`); as instructed the lemma is re-aimed at the mathlib term, i.e. assessed as `natDegree (aeval (fun _ ↦ X) P) ≤ ∑ r_j`. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.natDegree_diag_le`: resolved at Roth/CoeffNorm.lean:183
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms of integer polynomials and the estimates (Hasse derivatives, diagonal substitution, evaluation) for Lemmas 3 and 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.natDegree_diag_le` is a theorem stating the following: let `P(x_1, …, x_m)` be a polynomial with integer coefficients of degree at most `r_j` in `x_j` for every `j`. Then the one-variable polynomial `P(x, …, x)` has degree at most `r_1 + ⋯ + r_m`. (Each monomial `x^k` becomes `x^{|k|}` and `|k| = ∑ k_j ≤ ∑ r_j`.)

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]` — finite variable index set (needed to form `∑ j, r j`).
- `P : MvPolynomial σ ℤ` — the polynomial.
- `r : σ → ℕ` — partial degree bounds.

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — degree in `x_j` at most `r_j`.

Conclusion (math): `deg P(x, …, x) ≤ ∑_j r_j`.

Conclusion (Lean): `(diag P).natDegree ≤ ∑ j, r j`; re-aimed: `(aeval (fun _ ↦ Polynomial.X) P).natDegree ≤ ∑ j, r j`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper degree estimate for a specialisation map; one step of the Lemma 9 argument.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | degree of P(x,x,...,x) at most total degree multivariate polynomial substitution same variable | partial | folklore: `deg P(x,…,x) ≤ totalDeg P` (strict possible, e.g. `x_1 − x_2`) | no textbook statement; PIT / Schwartz–Zippel "univariate restriction" material uses it silently |
| 2 | WebSearch (general form) | total degree bounded by sum of partial degrees multivariate polynomial deg_{x_i} | partial | `totalDeg P ≤ ∑_i deg_{x_i} P` (folklore); mathlib doc pages for `degreeOf` / `totalDegree` surfaced | no named source; trivially from the definitions |
| 3 | WebSearch (named-after / aliases) | Roth's theorem auxiliary polynomial degree r_1 + ... + r_m after setting x_1 = ... = x_m | partial | Roth-proof expositions (arXiv math/0307203 Bugeaud–Evertse-style, arXiv 2502.00731, Evertse notes) specialise to the diagonal and use the degree bound implicitly | never a named lemma |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "same variable", "r_1 + \dots + r_m" | yes | l.1449 (diagonal substitution), l.1468 "using `s ≤ ∑_j r_j ≤ m r_1`" | exactly the project statement |
| 6 | nLab | polynomial ring / graded ring | partial | `x_j ↦ x` is a graded map for the total-degree grading, so degree is at most total degree | supports routing through `totalDegree` |
| 7 | nCatLab | — | n/a | — | not a categorical statement (an elementary degree inequality) |
| 8 | Stacks Project | — | n/a | — | Stacks treats graded rings but has no statement about partial-degree sums; not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1, #2) | partial | folklore one-line argument | stated in passing only |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | partial | sumcheck formalisation (arXiv 2402.06093) proves related total-degree vs single-variable-degree facts | ad hoc, no general statement |

### Literature summary (Phase 3)

Concept identified as: degree bound for the specialisation `x_j ↦ x` (more generally for substitution `x_j ↦ f_j`): `deg P(f_1, …, f_m) ≤ totalDeg P · max deg f_j`, and `totalDeg P ≤ ∑_j deg_{x_j} P`.
Sources agree on the standard form: yes (folklore).
Most general standard form: over any commutative semiring, `deg P(f) ≤ totalDeg(P) · n` when all `deg f_j ≤ n` (this is mathlib's `MvPolynomial.aeval_natDegree_le`); the project form is its `f_j = x`, `n = 1` case composed with `totalDeg ≤ ∑ partial degrees`.
Generality dimensions where the literature varies:
  - coefficient ring: `ℤ` to any commutative semiring.
  - substitution: `x_j ↦ x` to `x_j ↦ f_j` with `deg f_j ≤ n`.
  - degree measure: `∑ deg_{x_j}` (crude, project) vs total degree (sharp, no finiteness of `σ`).
Disagreement with the literature: none.

### Generality analysis — `Roth.natDegree_diag_le`

Literature-standard form (from Phase 3): `MvPolynomial.aeval_natDegree_le` over `[CommSemiring R]`; sharp special case `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficients `ℤ` | `MvPolynomial σ ℤ` | `[CommSemiring R]` | yes | verified (evidence (2)) |
| 2 | `diag` (project name) | `Roth.diag P` | `aeval (fun _ ↦ X) P` | yes (re-aim) | `rfl`; evidence (3) recovers the original |
| 3 | `[Fintype σ]` + `hP` | partial-degree bounds | `totalDegree P ≤ m` | yes (sharper, Fintype-free) | evidence (4) |
| 4 | substitution `x_j ↦ x` | constant `X` | `f_j` with `natDegree f_j ≤ n` | yes | that is `aeval_natDegree_le` itself, already in mathlib |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4, all compiled clean (evidence file, `lean_diagnostic_messages`: success, no diagnostics) — but the general form (row 4, and row 3 as its `n = 1` case) is already mathlib's `MvPolynomial.aeval_natDegree_le`, so the weakening routes to a NO bucket (false-positive class 4: general form already in mathlib), not to generalise-first.
Proposed restatement: none for mathlib; locally, the general-`R` composition in evidence (2).

Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single degree hypothesis |
| 2 | sequences to filters? | no | — | finite algebraic inequality |
| 3 | construction vs universal property? | yes (mild) | state about `aeval (fun _ ↦ X)` (universal-property map) instead of `diag` | lands on `aeval_natDegree_le` directly |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | yes | `ℤ` to `[CommSemiring R]` | already mathlib's generality |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `ℕ`-valued degrees are the mathlib convention |
| 8 | concrete-via-abstract? | yes | after `rw [diag_eq_sum]` the proof never mentions `diag`; content is about `aeval` | the re-aim |
| 9 | false-generalisation guard | no false generalisation | evidence (3) recovers the exact `ℤ` statement from the general form | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `(aeval (fun _ ↦ X) P).natDegree ≤ P.totalDegree` — which is `aeval_natDegree_le` with `n = 1`, already in mathlib.
  - Cost: CHEAP
  - Mathlib downstream this enables: nothing new (the idiomatic form exists).
  - Real mathematical improvement: none beyond routing the project proof through the existing mathlib lemma.

### Proof strategy — `Roth.natDegree_diag_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes (mild) | use `aeval_natDegree_le` instead of expanding via `diag_eq_sum` | CHEAP |
| 5 | missing mathlib helpers | marginal | `MvPolynomial.totalDegree_le_sum_degreeOf [Fintype σ]` is absent but is a one-line `simpa [degreeOf_def] using totalDegree_le_degrees_card` | not worth a PR on its own |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (optional, local)
  - Proposed strategy: `aeval_natDegree_le` with `m := ∑ r_j`, `n := 1`, feeding `totalDegree ≤ ∑ degreeOf ≤ ∑ r_j`.
  - Cost: CHEAP (compiled, evidence (2))
  - Missing mathlib API (if any): none essential.
  - Would refactoring make the proof strictly shorter / cleaner? marginally (3 lines vs 5; removes dependence on `diag_eq_sum`), at the cost of an extra import.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.natDegree_diag_le`

[A] Lean-Finder       "degree of P(x,x,...,x) is at most the sum of the partial degrees of the multivariate polynomial P"   hits: `MvPolynomial.aeval_natDegree_le`, `degreeOf_le_totalDegree`, `totalDegree_le_degrees_card`, `le_totalDegree`
[B] Loogle            `MvPolynomial.totalDegree _ ≤ ∑ _, MvPolynomial.degreeOf _ _`   no hits
[C] LeanSearch        "total degree of multivariate polynomial at most sum of degrees in each variable"   hits: `totalDegree_le_degrees_card`, `le_totalDegree`, `monomial_le_degreeOf` (building blocks)
[D] Grep mathlib src  `aeval_natDegree_le` (Mathlib/RingTheory/Polynomial/Basic.lean:898), `totalDegree.*degreeOf`, `sum.*degreeOf`, `sum_count_eq_card` (Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:1096), `degreeOf_def` (Mathlib/Algebra/MvPolynomial/Degrees.lean:220)   hits (building blocks); no `natDegree_diag`-style or `totalDegree_le_sum_degreeOf` lemma
[E] Name pattern      `aeval_natDegree_le`, `totalDegree_le_degrees_card`, `degreeOf_def`, `Multiset.sum_count_eq_card`, `Polynomial.natDegree_X_le` (all used in compiled evidence)   hits

Searched for both the user's form (`natDegree (diag P) ≤ ∑ r_j`) and the literature-standard forms (`natDegree (aeval f P) ≤ totalDegree P * n`; `totalDegree ≤ ∑ degreeOf`).

Concluded: found building blocks (`MvPolynomial.aeval_natDegree_le`, `MvPolynomial.totalDegree_le_degrees_card`, `MvPolynomial.degreeOf_def`, `Multiset.sum_count_eq_card`); composition yields our form. The literature-general form is `aeval_natDegree_le` itself.

### Normal-form check — `Roth.natDegree_diag_le`

Equivalent formalisms: (a) `natDegree (diag P) ≤ ∑ r_j` from partial-degree bounds (project); (b) `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P`; (c) `aeval_natDegree_le` with hypothesis `totalDegree ≤ m`.
Does mathlib already have a canonical form for this idea? Yes: `MvPolynomial.aeval_natDegree_le` (hypothesis-style `totalDegree ≤ m`, `natDegree f_i ≤ n`).
Is our statement stated against the canonical form? No — it bypasses `totalDegree`; it is a corollary of the canonical form.
RHS convention respected? yes (inequality with bound on RHS).

### Syntactic generality — `Roth.natDegree_diag_le`

Alternative restatements attempted:
- (b) sharp `≤ totalDegree P` (compiles, evidence (4))
- general-`R` partial-degree form (compiles, evidence (2))
Chosen restatement: keep the partial-degree form locally (it is what the call site has: `hdP : ∀ k, degreeOf k P ≤ r k`).
Justification: the call site supplies partial-degree bounds directly; for mathlib, (b)/(c) already exist.

### Superfluous-argument audit — `Roth.natDegree_diag_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficient ring `ℤ` | no | any `CommSemiring R` (evidence (2)) |
| 2 | `[Fintype σ]` | only to form `∑ j, r j` | the sharp `totalDegree` form needs none (evidence (4)) |
| 3 | `hP` | yes | the degree bound |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (canonical form is `aeval_natDegree_le`; ours is a corollary)
Syntactic generality: OK locally
Superfluous arguments: 1 (`ℤ` specialisation, inherited from `diag`)

Overall: RESTATE-BEFORE-SHIP (moot: not shipping)

### Call sites — `Roth.natDegree_diag_le`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:513 (`abs_coeff_diag_hasseDeriv_modByMonic_le_aux`, private) | `norm_coeff_modByMonic_le (...) _ (...) (natDegree_diag_le _ hdP) i` |

Inline-derivation grep (`natDegree_sum_le_of_forall_le`, `aeval_natDegree_le`, `natDegree_monomial_le` over `Roth/`):
  - (none re-deriving this bound; other `natDegree_*` uses concern different polynomials)

### Composition check (Phase 6)

Can `natDegree (aeval (fun _ ↦ X) P) ≤ ∑ r_j` be derived from mathlib in ≤3 chained calls?

Attempt 1: `aeval_natDegree_le P (h.trans (Finset.sum_le_sum fun j _ ↦ hP j)) _ fun _ ↦ Polynomial.natDegree_X_le` with `h : totalDegree P ≤ ∑ j, degreeOf j P := by simpa [degreeOf_def] using P.totalDegree_le_degrees_card`, closed by `simpa` (`* 1`).
  - Mathlib decls used: `MvPolynomial.aeval_natDegree_le`, `MvPolynomial.totalDegree_le_degrees_card`, `MvPolynomial.degreeOf_def`, `Multiset.sum_count_eq_card` (simp), `Finset.sum_le_sum`, `Polynomial.natDegree_X_le`
  - Result: succeeds (evidence (1)–(3), compiled)
  - Notes: one main call (`aeval_natDegree_le`) plus a one-line `simpa` for the `totalDegree` bound — within the 1–3 call budget.
Conclusion: COMPOSABLE

## Verdict: `Roth.natDegree_diag_le`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): folklore; paper l.1468 uses `s ≤ ∑ r_j`; general form is "degree of a substitution ≤ total degree × max degree of substituted polynomials".
- Generality analysis (Phase 4): STRICTLY NARROWER, but the general form is mathlib's `MvPolynomial.aeval_natDegree_le` (false-positive class 4).
- Mathlib search (Phase 5): building blocks `aeval_natDegree_le`, `totalDegree_le_degrees_card`, `degreeOf_def`, `Multiset.sum_count_eq_card`.
- Composition check (Phase 6): COMPOSABLE (compiled).

**Rationale:**

Re-aimed at the mathlib term behind `diag` (`aeval (fun _ ↦ X)`, per the parent `Roth.diag` assessment), the statement is mathlib's `MvPolynomial.aeval_natDegree_le` at `n = 1`, with the hypothesis `totalDegree P ≤ ∑ r_j` supplied by `totalDegree ≤ ∑ degreeOf`, which is `simpa [degreeOf_def] using totalDegree_le_degrees_card` (the simp set closes it with `Multiset.sum_count_eq_card`). All of this compiles over any `CommSemiring R`, and the original `ℤ`/`diag` statement follows by definitional unfolding (evidence). The parent report's suggestion is confirmed. Nothing new for mathlib: the sharp, general form already exists, and `totalDegree_le_sum_degreeOf` is too thin to be a PR on its own (at most a drive-by `simp`-free convenience lemma next to `totalDegree_le_degrees_card`).

WHY not: a 1-call composition (plus a one-line bound) of mathlib lemmas. Belongs-elsewhere check: keep it in Roth/CoeffNorm.lean as a named project lemma about the project-local `diag`, since `diag` itself stays local (parent verdict) and the call site reads better with the name.

Mathlib building blocks:      `MvPolynomial.aeval_natDegree_le` (Mathlib/RingTheory/Polynomial/Basic.lean:898), `MvPolynomial.totalDegree_le_degrees_card` (Mathlib/Algebra/MvPolynomial/Degrees.lean:445), `MvPolynomial.degreeOf_def` (Mathlib/Algebra/MvPolynomial/Degrees.lean:220), `Multiset.sum_count_eq_card` (Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean:1096), `Polynomial.natDegree_X_le`
Composition sketch (≤3 lines):
```lean
example [Fintype σ] (P : MvPolynomial σ ℤ) {r : σ → ℕ} (hP : ∀ j, degreeOf j P ≤ r j) :
    (Roth.diag P).natDegree ≤ ∑ j, r j := by
  classical
  simpa using aeval_natDegree_le P (((by simpa [degreeOf_def] using P.totalDegree_le_degrees_card :
    P.totalDegree ≤ ∑ j, P.degreeOf j)).trans (Finset.sum_le_sum fun j _ ↦ hP j)) _
    fun _ ↦ Polynomial.natDegree_X_le
```
Call sites in our project (from Phase 6.0):  1 (Roth/MainLemma.lean:513)
Refactor plan: do not delete (single call site; the name documents the paper step). Optionally replace the 5-line proof at Roth/CoeffNorm.lean:183 by the composition above (add `import Mathlib.RingTheory.Polynomial.Basic` to Roth/CoeffNorm.lean); Roth/MainLemma.lean:513 is unchanged. If `diag` is generalised to `CommSemiring R` per the parent report, this lemma generalises verbatim (evidence (2)).
Next action: no mathlib action; optional local reproof via `aeval_natDegree_le`.

---

## Next step

No mathlib action for `Roth.natDegree_diag_le`. Optionally reprove it as `aeval_natDegree_le` (`n = 1`) composed with `totalDegree ≤ ∑ degreeOf`, keeping the name for Roth/MainLemma.lean:513.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.natDegree_diag_le/natDegree_diag_compose.lean` (imports `Mathlib.RingTheory.Polynomial.Basic`, `Roth.CoeffNorm`; first check failed with `Unknown identifier aeval_natDegree_le` because the import was missing, after adding it `lean_diagnostic_messages`: success, no diagnostics). Contents: (1) `totalDegree_le_sum_degreeOf` over `[CommSemiring R]` by one `simpa`; (2) `natDegree_aeval_X_le` (project statement re-aimed, general `R`) via `aeval_natDegree_le`; (3) exact `Roth.natDegree_diag_le` statement recovered from (2); (4) sharp `natDegree (aeval (fun _ ↦ X) P) ≤ totalDegree P` via `aeval_natDegree_le`.
- Loogle (1), LeanSearch (1), Lean-Finder (1) queries and mathlib greps as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex l.1449, l.1468.
- Project greps: `grep -rn natDegree_diag_le Roth/` (call site MainLemma.lean:513); parent report `.mathlib-quality/overview/mathlibable/Roth.diag.md`.
