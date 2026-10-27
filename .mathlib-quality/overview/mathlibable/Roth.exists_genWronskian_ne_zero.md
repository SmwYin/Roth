---
decl: Roth.exists_genWronskian_ne_zero
file: Roth/GenWronskian.lean
line: 254
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: MODERATE
junk: KEEP
rationale: Roth's Lemma 1 (linearly independent multivariate polynomials have a generalized Wronskian with orders at most mu that is nonzero; Ostrowski, Roth 1955, Bostan-Dumas Thm 3) is absent from mathlib, which has only the 2-ary univariate Wronskian; [Finite sigma] drops via rename and [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] via the fraction field (both verified), CharZero is necessary.
action: Upstream as MvPolynomial.exists_genWronskian_ne_zero (placeholder) over [CommRing R] [IsDomain R] [CharZero R] with no finiteness on sigma, in the new Mathlib/RingTheory/MvPolynomial/Wronskian.lean as a follow-up PR after MvPolynomial.hasseDeriv, the n-ary Polynomial Wronskian criterion, MvPolynomial.genWronskian and the weightedSubst (Kronecker) PR; locally keep (single caller Roth/Separation.lean:524 in private exists_rat_factors_det_hasseDeriv_aux).
---

# Roth.exists_genWronskian_ne_zero

## Inventory entry

### `theorem Roth.exists_genWronskian_ne_zero`
- **Type**: `{K : Type*} [Field K] {σ : Type*} {l : ℕ} [Finite σ] [CharZero K] {φ : Fin l → MvPolynomial σ K} (h : LinearIndependent K φ) : ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0`
- **What**: Lemma 1 of the source (Roth's lemma): a linearly independent family of `l` multivariate polynomials over a characteristic-zero field has a generalized Wronskian `det (Δ_{D μ} φ_ν)`, with Hasse operators of total order `|D μ| ≤ μ`, that is not identically zero.
- **How**: Kronecker substitution. Take `k = 2 + Σ_ν Σ_j degreeOf j (φ ν)`, which exceeds every partial degree. For each `μ`, `exists_hasseDeriv_kronecker_eq_sum` writes `Polynomial.hasseDeriv μ (kronecker k P)` as `Σ_{d ∈ s μ} c μ d * kronecker k (hasseDeriv d P)` with `|d| ≤ μ`. If every admissible generalized Wronskian vanished, the private `wronskian_kronecker_eq_sum_aux` (multilinear expansion via `det_sum_rows`) would make the univariate Wronskian of `kronecker k ∘ φ` zero. But that family is linearly independent (`linearIndependent_kronecker`), contradicting `wronskian_ne_zero_of_linearIndependent`.
- **Hypotheses**: `[Field K]`, `[CharZero K]` (needed for the univariate criterion), `[Finite σ]` (needed for the Kronecker substitution `kronecker`, which uses `Fintype.equivFin`), and `h : LinearIndependent K φ`.
- **Uses from project**: `Roth.genWronskian`, `Roth.exists_hasseDeriv_kronecker_eq_sum`, `Roth.wronskian_ne_zero_of_linearIndependent`, `Roth.linearIndependent_kronecker`, `Roth.wronskian_kronecker_eq_sum_aux` (private), `Roth.kronecker`, `MvPolynomial.hasseDeriv` (via `genWronskian`)
- **Used by**: Roth/Separation.lean:524 (`exists_rat_factors_det_hasseDeriv_aux`, private, the proof of Lemma 2)
- **Visibility**: public
- **Lines**: 254–270, proof length 14 lines
- **Notes**: This is a main result of §2 of the source (`roth:lem1`, clean.tex l.224–225). The source states it over `ℚ`. The project already generalises it to any characteristic-zero field, and to any finite variable type.

## Junk check (Step 8)
- Used anywhere? Yes. It is the key input to Lemma 2 (Roth/Separation.lean:524).
- Wrapper of 1–2 mathlib calls? No. It is a 14-line proof that combines four project lemmas.
- Does mathlib have it? No. `lean_leansearch` and `lean_leanfinder` return only the 2-ary `Polynomial.wronskian` API. Grep finds `wronsk` in 3 mathlib files (Polynomial/Wronskian, Radical, MasonStothers), none multivariate.
- Too specific (inline?)? No. It is a named lemma of the source and a standard theorem.
- Well-chosen definition? n/a (theorem). The statement shape is the standard one: there exist admissible orders such that the Wronskian is nonzero.
- Conclusion: `KEEP`. Action: keep locally; it is an upstream candidate in generalised form (below).

## Mathlibable assessment (Step 9)

Pre-filter: not private, no `_aux` suffix, docstring not internal/auxiliary, Step 8 KEEP. A namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds no `exists_genWronskian_ne_zero` and no `genWronskian`. Not a glue lemma (14-line proof). Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; the evidence file importing `Roth.GenWronskian` elaborates with no diagnostics)
- decl `Roth.exists_genWronskian_ne_zero`:  ✓ resolved at Roth/GenWronskian.lean:254
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians `det (Δ_{D μ} φ_ν)` of multivariate polynomials, and Lemma 1: a linearly independent family has a nonvanishing generalized Wronskian, proved by Kronecker substitution.

### Statement (Phase 1)

`Roth.exists_genWronskian_ne_zero` is a theorem stating the following.

Let `K` be a field of characteristic zero and `σ` a finite set of variables. If `φ_0, …, φ_{l-1} ∈ K[x_j : j ∈ σ]` are linearly independent over `K`, then there are multi-indices `D_0, …, D_{l-1}` with `|D_μ| ≤ μ` such that the generalized Wronskian `det (Δ_{D_μ} φ_ν)_{μ,ν}` is a nonzero polynomial. Here `Δ_d` is the multivariate Hasse derivative `∏_j (1/d_j!) ∂_j^{d_j}`.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K] [CharZero K]`: the coefficient field.
- `σ` with `[Finite σ]`: the variable index set.
- `l : ℕ`: the number of polynomials.

Hypotheses (Lean side):
- `h : LinearIndependent K φ`: the family is linearly independent over `K`.

Conclusion (math): some admissible generalized Wronskian of `φ` is not identically zero.

Conclusion (Lean): `∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0`

### Size classification (Phase 2a)

Verdict: BIG
Reason: A main result of the project (Lemma 1, `roth:lem1`, named in the module docstring as "the main result"). It is the classical generalized-Wronskian criterion of Ostrowski and Roth.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for
the report's framing and for the worker's mental model — it does not gate
which channels Phase 3 runs.)

### One-line check (Phase 2b)

Body line count: 14 substantive lines
One-liner verdict: n/a (kind is theorem/lemma, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma generalized Wronskian linearly independent polynomials several variables not identically zero | yes | Roth 1955 Lemma 1 (Mathematika, rational coefficients). arXiv 2502.00731 Lemma 2.25 states the iff over a field K with multi-indices `|μ_i| ≤ i−1`, proved by Kronecker substitution to one variable | exactly our statement (0-indexed orders `≤ μ`) and our proof strategy |
| 2 | WebSearch (general form) | generalized Wronskians linear dependence multivariate formal power series characteristic zero Bostan Dumas | yes | Bostan–Dumas (arXiv 1301.6598) Thm 3: over a char-0 field, linearly independent formal power series in `K[[x_1..x_m]]` have a nonzero generalized Wronskian. Ball–Parks–Pong (arXiv 1611.00248) give a different proof and extend it to quotients of analytic germs | most general standard form: power series, char-0 field. Char 0 is necessary (`1, x^p` over `𝔽_p`) |
| 3 | WebSearch (named-after / aliases) | Ostrowski generalized Wronskian theorem Kronecker substitution proof partial derivatives order at most i | yes | Ostrowski introduced generalized Wronskians; Dyson and Roth used them. Classical proofs go either by substitution with reduction to one variable, or by induction (Bostan–Dumas survey). Admissible tuples have i-th order `≤ i−1` | the aliases are "generalized Wronskian criterion", "Roth's lemma", "Ostrowski's theorem" |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` l.210–225 | yes | "If φ_0(x_1..x_p), …, φ_{l-1} are l linearly independent polynomials in p variables with rational coefficients, then at least one of their generalized Wronskians is not identically zero" (`roth:lem1`); the definition at l.210 uses operators of order `≤ μ` | the exact source statement, over ℚ |
| 6 | nLab | generalized Wronskian / Wronskian | n/a | — | nLab has no entry on the generalized Wronskian criterion, which is not a categorical concept |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | Stacks does not treat Wronskians; this is not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | covered by WebSearch #1–#3 (no thread surfaced) | no | — | a folklore textbook fact (Schmidt LNM 785, Ch. V; Bombieri–Gubler Lemma 6.4.6, cited by Bostan–Dumas) |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2502.00731 (2025, subspace theorem notes, Lemma 2.25), 2108.02993 (2021, geometric generalized Wronskians) | still in active use in Diophantine approximation |

### Literature summary (Phase 3)

Concept identified as: the generalized Wronskian criterion for linear independence of multivariate polynomials (Roth's Lemma 1, due to Ostrowski, used by Dyson and Roth).
Sources agree on the standard form: yes. If `f_1, …, f_n` are linearly independent over a char-0 field `K`, then some generalized Wronskian `det (D_i f_j)` is nonzero, where each `D_i` is a derivative of order `≤ i−1`. Roth states it for polynomials over ℚ. Bostan–Dumas and Ball–Parks–Pong extend it to formal power series.
Most general standard form: formal power series in finitely or infinitely many variables over a characteristic-zero field. Clearing denominators gives the same statement over any characteristic-zero integral domain.
Generality dimensions where the literature varies:
  - coefficients: ℚ (Roth), char-0 field (Bostan–Dumas), char-0 domain (by fraction field). Char 0 is necessary.
  - objects: polynomials (Roth, source) up to formal power series (Bostan–Dumas, Ball–Parks–Pong).
  - variables: finitely many in all sources. For polynomials, any variable set reduces to the finite case.
  - operators: arbitrary constant-coefficient operators of order `≤ i−1` (Roth) versus monomial derivatives (Bostan–Dumas). Multilinearity makes these equivalent, and the monomial form is stronger as an existence statement.
Disagreement with the literature: none in substance. The project uses Hasse derivatives, which differ from ordinary derivatives by a nonzero constant in char 0 and are the characteristic-free normalisation.

### Generality analysis — `Roth.exists_genWronskian_ne_zero`

Literature-standard form (from Phase 3): over a char-0 field (equivalently a char-0 domain), linearly independent polynomials or power series in any number of variables have a nonzero generalized Wronskian with admissible orders.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | char-0 integral domain (via fraction field) | yes | verified: `[CommRing R] [IsDomain R] [CharZero R]` by transfer to `FractionRing R` (`LinearIndependent.iff_fractionRing`, `map_genWronskian`, `MvPolynomial.map_injective`) |
| 2 | `[CharZero K]` | char 0 | char 0 | NO | necessary: `1, x^2` over `ZMod 2` with one variable (admissible orders `0, ≤1`; `Δ_1 x^2 = 2x = 0`). This is the univariate counterexample already compiled in the `Roth.wronskian_ne_zero_of_linearIndependent` evidence file |
| 3 | `[Finite σ]` | finite variable type | any (polynomials involve finitely many variables) | yes | verified: rename into the finite set `⋃ vars (φ ν)` (`exists_rename_eq_of_vars_subset_range`), then apply the lemma there. Push forward with `hasseDeriv_rename`, `AlgHom.map_det`, `Finsupp.degree_mapDomain`, and the injectivity of `rename` |
| 4 | `φ : Fin l → MvPolynomial σ K` | polynomials | formal power series | yes in the literature | needs `MvPowerSeries` Hasse derivatives and a different proof (Bostan–Dumas monomial reduction), which is not a mechanical weakening. Not proposed here; see the BORDERLINE-style note in Phase 7 |
| 5 | `Fin l` indexing | `Fin l` with orders `≤ μ` | finite family with ordered orders | NO | the admissibility `|D μ| ≤ μ` needs an ordering, and `Fin l` is the natural choice |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (verified), plus 1 literature-only (power series, not mechanical)
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem MvPolynomial.exists_genWronskian_ne_zero {R σ : Type*} [CommRing R] [IsDomain R]
    [CharZero R] {l : ℕ} {φ : Fin l → MvPolynomial σ R} (h : LinearIndependent R φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0
```

Both weakenings are compiled in `.mathlib-quality/overview/evidence/Roth.exists_genWronskian_ne_zero/weaken.lean` (clean, no diagnostics): `exists_genWronskian_ne_zero_of_infinite` (field, no `Finite σ`) and `exists_genWronskian_ne_zero` (domain, no `Finite σ`), with an `ℤ`, `σ = ℕ` instance and the project statement recovered as a specialisation.

Cost of restatement: MODERATE. The transfers are about 20 lines each on top of the existing proof, and the domain version depends on `map_genWronskian`.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | the hypotheses are already typeclasses plus one `LinearIndependent` | — |
| 2 | Sequences → filters? | no | purely algebraic | — |
| 3 | Construction → universal property? | no | an existence theorem | — |
| 4 | Set-with-predicate → bundled substructure? | no | `LinearIndependent` is the idiomatic predicate | — |
| 5 | Field-specific → (semi)ring? | yes | `[CommRing R] [IsDomain R] [CharZero R]` (verified) | applies over `ℤ` directly. The Separation caller currently passes `ℤ → ℚ` by hand (Roth/Separation.lean:515–523) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general? | yes | `σ` arbitrary rather than `Finite` (verified) | composes with `MvPolynomial ℕ R` and with `rename` without supplying finiteness |
| 8 | Concrete-via-abstract? | no | the statement is already abstract in `σ`, `K`, `φ`. The proof's concrete witness (`kronecker k`) is internal | — |
| 9 | False-generalisation guard | no | the domain and infinite-σ forms state the same theorem: the generalized Wronskian over `R` is the same object, and its non-vanishing is the same predicate | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the domain / arbitrary-σ form in Phase 4b, in namespace `MvPolynomial` next to `genWronskian`.
  - Cost: MODERATE
  - Mathlib downstream this enables: it applies to `MvPolynomial σ ℤ` (integral polynomials, as in Roth's Lemma 2) and to infinite variable types. It sits beside the n-ary univariate criterion as its multivariate analogue.
  - Real mathematical improvement (not just "looks cooler"): it removes the ℤ→ℚ round trip at the call site and removes a finiteness hypothesis that the theorem does not need.

### Proof strategy — `Roth.exists_genWronskian_ne_zero`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Elements vs submodule inclusions? | no | linear independence is already point-free | — |
| 3 | Sequences vs nets? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing helper lemmas mathlib should have? | yes | (a) `MvPolynomial.hasseDeriv`; (b) the n-ary univariate Wronskian criterion; (c) a weighted / Kronecker substitution `weightedSubst` with base-k injectivity; (d) a multivariate Hasse chain rule for `Polynomial.hasseDeriv (aeval g P)` (see the `Roth.exists_hasseDeriv_kronecker_eq_sum` report) | file follow-up PRs; each has its own report |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
The Kronecker-substitution reduction to the univariate criterion is one of the two classical proofs (Roth; Bostan–Dumas survey). Given (a)–(d), the proof body is already short (14 lines). It would get shorter only if the helper `exists_hasseDeriv_kronecker_eq_sum` were derived from a general chain rule, and that change lives in the helper, not here. The alternative is Bostan–Dumas's monomial-reduction proof, which covers power series. It would be the route to the power-series generalisation, not a cleanup of this proof.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_genWronskian_ne_zero`

[A] Lean-Finder       "generalized Wronskian of linearly independent polynomials in several variables is nonzero in characteristic zero"   no hits (returned `Polynomial.wronskian` API and `Matrix.det_mvPolynomialX_ne_zero`)
[B] Loogle            `LinearIndependent, Matrix.det, MvPolynomial`   no hits
[C] LeanSearch        "linearly independent multivariate polynomials have a nonzero generalized Wronskian"   no hits (only 2-ary `Polynomial.wronskian` lemmas)
[D] Grep mathlib src  `wronsk` (case-insensitive), `genWronskian`, `generalized Wronskian`, `Roth's lemma`   only Polynomial/Wronskian.lean, Polynomial/Radical.lean and FLT/MasonStothers.lean, all for the 2-ary univariate Wronskian; no multivariate hit. No `MvPolynomial.hasseDeriv` either (per the parent reports)
[E] Name pattern      lean_local_search / grep `exists_genWronskian`, `genWronskian`   project only

Searched for both:
  - the user's current form
  - the literature-standard form from Phase 3 (power-series / domain / multivariate Wronskian criterion)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Mathlib does not even have the univariate n-ary criterion. `Mathlib/RingTheory/Polynomial/Wronskian.lean` has a TODO for the n-tuple Wronskian.

### Normal-form check — `Roth.exists_genWronskian_ne_zero`

Equivalent formalisms this statement could take: (i) `LinearIndependent R φ → ∃ D admissible, genWronskian D φ ≠ 0` (current); (ii) contrapositive `(∀ D admissible, genWronskian D φ = 0) → ¬ LinearIndependent R φ`; (iii) iff with `genWronskian_eq_zero_of_not_linearIndependent`: `LinearIndependent R φ ↔ ∃ D admissible, genWronskian D φ ≠ 0`.
Does mathlib already have a canonical form for this idea? no (no Wronskian criterion at all). The 2-ary analogue `IsCoprime.wronskian_eq_zero_iff` uses iff form.
If no: name the canonical form we'd propose. Ship (i) as the main lemma and add the iff (iii) as `linearIndependent_iff_exists_genWronskian_ne_zero`, with the Wronskian condition on the RHS (the testable normal form), mirroring the project's univariate `wronskian_eq_zero_iff`.
RHS convention respected? yes (for the proposed iff)

### Syntactic generality — `Roth.exists_genWronskian_ne_zero`

Alternative restatements attempted (list):
- current existential with `(D μ).degree ≤ μ`
- `D μ ∈ {d | d.degree ≤ μ}` / a bundled `Finset` of admissible tuples
- the iff form (iii)

Chosen restatement: the current existential, plus the iff as a companion.
Justification: the caller (Roth/Separation.lean:524) destructures `⟨D, hD, hG⟩` and needs both the bound `hD` and the witness. The iff form needs a domain hypothesis for its reverse direction, which the existential does not.

### Superfluous-argument audit — `Roth.exists_genWronskian_ne_zero`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no (a domain suffices) | weakens to `[CommRing R] [IsDomain R]` via the fraction field (verified) |
| 2 | `[CharZero K]` | yes | fails in char p (`1, x^2` over `ZMod 2`) |
| 3 | `[Finite σ]` | no (for the conclusion) | used only by the Kronecker proof; drops via `rename` (verified) |
| 4 | `h : LinearIndependent K φ` | yes | the content of the theorem |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (add the iff companion when upstreaming)
Syntactic generality: OK
Superfluous arguments: 2 to drop (`[Finite σ]`; `[Field K]` → `[CommRing R] [IsDomain R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.exists_genWronskian_ne_zero`

Internal use count: 1  (within the same project, NOT counting the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:524 | `obtain ⟨D, hD, hG⟩ := exists_genWronskian_ne_zero hψ` (inside private `exists_rat_factors_det_hasseDeriv_aux`, the proof of Lemma 2) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.exists_genWronskian_ne_zero`?):
  - (none). `grep -rn "wronskian_kronecker_eq_sum_aux\|linearIndependent_kronecker" Roth/` hits only GenWronskian.lean.

K = 1, but this is a named main lemma whose single caller is the next main lemma. The low count reflects a linear proof chain, not a wrong abstraction.

### Composition check (Phase 6)

Can `Roth.exists_genWronskian_ne_zero` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable. Mathlib has neither the multivariate Hasse derivative, the n-ary univariate Wronskian criterion, nor a Kronecker substitution.
  - Result: fails
  - Notes: even with all project prerequisites upstreamed, the proof combines four lemmas with a contradiction argument and an expansion by multilinearity (14 lines). That is a real proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.exists_genWronskian_ne_zero`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): a standard named theorem (Ostrowski; Roth 1955 Lemma 1; Bostan–Dumas Thm 3; arXiv 2502.00731 Lemma 2.25) over char-0 fields, also stated for power series.
- Generality analysis (Phase 4): STRICTLY NARROWER. `[Finite σ]` drops and `[Field K]` weakens to a char-0 domain, both compiled clean in the evidence file.
- Mathlib search (Phase 5): not in mathlib; mathlib only has the 2-ary univariate Wronskian, with an n-ary TODO.
- Composition check (Phase 6): NOT-COMPOSABLE

**Rationale (1–2 paragraphs):**

The concrete gap is that mathlib's Wronskian API stops at `Polynomial.wronskian a b`, and `Mathlib/RingTheory/Polynomial/Wronskian.lean` carries a TODO for the n-tuple case. No multivariate Wronskian criterion exists. The generalized Wronskian criterion is the standard linear-independence test for several-variable polynomials and power series. It is the first lemma of every exposition of Roth's theorem and of Schmidt's subspace theorem, and Bostan–Dumas and Ball–Parks–Pong treat it as a theorem in its own right. `Roth.exists_genWronskian_ne_zero` is its polynomial case, already proved characteristic-free in the Hasse normalisation, so it is the natural capstone of the planned `MvPolynomial.genWronskian` PR series.

It should not ship as stated. Two hypotheses are stronger than needed, and the evidence file verifies both weakenings. `[Finite σ]` is an artefact of the Kronecker proof: renaming into the finitely many variables used gives the statement for any `σ`. `[Field K]` weakens to `[CommRing R] [IsDomain R] [CharZero R]` by passing to `FractionRing R`, because the generalized Wronskian commutes with `map`. `[CharZero]` is necessary. The power-series generalisation (Bostan–Dumas) is literature-standard but needs `MvPowerSeries` Hasse derivatives and a different proof. It is a later extension, not a precondition for this PR. Sequencing: this lemma depends on four upstream prerequisites, each with its own report: `MvPolynomial.hasseDeriv`, the n-ary Wronskian criterion `Roth.wronskian_ne_zero_of_linearIndependent` (YES-but-generalise-first), `MvPolynomial.genWronskian` (YES-but-generalise-first), and the Kronecker / `weightedSubst` API (`Roth.kronecker`, YES-but-generalise-first). The helper `Roth.exists_hasseDeriv_kronecker_eq_sum` is BORDERLINE: it should ideally come from a general Hasse chain rule.

Reason for the generalisation: LITERATURE-WEAKENING (char-0 domain and arbitrary variable set) plus MODERN-IDIOM (`MvPolynomial` namespace beside `genWronskian`, with an iff companion).
Proposed restatement:
```lean
namespace MvPolynomial
variable {R σ : Type*} [CommRing R] [IsDomain R] [CharZero R] {l : ℕ}

theorem exists_genWronskian_ne_zero {φ : Fin l → MvPolynomial σ R}
    (h : LinearIndependent R φ) :
    ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ genWronskian D φ ≠ 0 := by
  sorry -- field + finite σ: current Kronecker proof; general case: evidence file transfers

theorem linearIndependent_iff_exists_genWronskian_ne_zero {φ : Fin l → MvPolynomial σ R} :
    LinearIndependent R φ ↔ ∃ D : Fin l → (σ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧
      genWronskian D φ ≠ 0 := by
  sorry -- with genWronskian_eq_zero_of_not_linearIndependent
end MvPolynomial
```
Estimated cost of regeneralisation: MODERATE. The core proof is unchanged, and two short transfer arguments are already written in the evidence.
Mathlib downstream this enables:
- the multivariate Wronskian criterion over `ℤ` and other char-0 domains, with no `ℤ → ℚ` round trip (the local caller Roth/Separation.lean:515–523 does that round trip by hand today);
- linear-independence tests for `MvPolynomial σ R` with infinite `σ` (e.g. `MvPolynomial ℕ R`) without restricting variables first;
- the iff `linearIndependent_iff_exists_genWronskian_ne_zero`, the multivariate counterpart of the n-ary univariate criterion that the mathlib TODO asks for.
PR grouping: after the PRs for `MvPolynomial.hasseDeriv`, the n-ary Polynomial Wronskian (with its criterion), `MvPolynomial.genWronskian` (with `map_genWronskian` and the dependent-vanishing lemma), and `MvPolynomial.weightedSubst`, ship one PR "feat(RingTheory/MvPolynomial/Wronskian): generalized Wronskian criterion". It should contain the Kronecker Hasse-expansion helper (ideally via a general chain rule), `det_sum_rows`-style multilinear expansion (if not already in mathlib as `MultilinearMap.map_sum_finset`), this lemma in generalised form, and the iff.
Next action: run `/generalise Roth.exists_genWronskian_ne_zero` (targets: drop `[Finite σ]`, weaken to `[CommRing R] [IsDomain R] [CharZero R]`; the evidence file has both proofs), then upstream once the prerequisites land.

---

## Next step

Run `/generalise Roth.exists_genWronskian_ne_zero`, which drops `[Finite σ]` and weakens `[Field K]` to `[CommRing R] [IsDomain R] [CharZero R]` (proofs in the evidence file). Then upstream it as `MvPolynomial.exists_genWronskian_ne_zero`, plus the iff, to `Mathlib/RingTheory/MvPolynomial/Wronskian.lean` after its prerequisites. The single local caller, Roth/Separation.lean:524, stays as it is.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_genWronskian_ne_zero/weaken.lean` (imports `Roth.GenWronskian` plus the localization / CharP modules), checked with `lean_diagnostic_messages`: clean, no errors or warnings, first attempt. It verifies: (1) `exists_genWronskian_ne_zero_of_infinite`: the project statement without `[Finite σ]`, via `exists_rename_eq_of_vars_subset_range`, `LinearIndependent.of_comp`, `hasseDeriv_rename`, `AlgHom.map_det`, `Finsupp.degree_mapDomain` and `rename_injective`; (2) `exists_genWronskian_ne_zero` over `[CommRing R] [IsDomain R] [CharZero R]` with arbitrary `σ`, via `LinearIndependent.iff_fractionRing`, `mapAlgHom`, `map_injective` and `map_genWronskian` (copied from the `Roth.genWronskian` evidence); (2') an instance over `MvPolynomial ℕ ℤ`; (3) the project statement as a specialisation.
- The char-p counterexample showing `[CharZero]` is necessary (`1, X^2` over `ZMod 2`) is compiled in `.mathlib-quality/overview/evidence/Roth.wronskian_ne_zero_of_linearIndependent/weaken_domain.lean`. It is the one-variable case of this lemma: with one variable, the admissible `D` are `D 0 = 0` and `D 1 ∈ {0, e}`.
- WebSearch ×3 (queries in the literature table); lean_leansearch ×1, lean_leanfinder ×1, lean_loogle ×1 (no relevant hits); grep of mathlib for `wronsk`, `genWronskian`, `generalized Wronskian`, `Roth's lemma`; grep of `Roth/` for callers (one: Separation.lean:524); `.mathlib-quality/references/clean.tex` l.210–225.
