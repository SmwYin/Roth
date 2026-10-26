---
decl: MvPolynomial.factorial_smul_hasseDeriv_single
file: Roth/HasseDeriv.lean
line: 286
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multivariate analogue of mathlib's Polynomial.factorial_smul_hasseDeriv (n! Delta_(n e_j) = d_j^n), absent from mathlib which has no multivariate Hasse derivative; a strictly more general form for an arbitrary base multi-index d (d_j^n Delta_d = n! C(d_j+n,n) Delta_(d+n e_j)) compiles and the lemma should also be offered in mathlib's operator (coe-of-smul = iterate) shape.
action: Upstream with the parent into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as `iterate_pderiv_hasseDeriv` (general d, evidence general.lean) plus `factorial_smul_hasseDeriv_single` in operator form as the d = 0 corollary; locally keep as is (no code callers, only the module docstring at Roth/HasseDeriv.lean:35).
---

# MvPolynomial.factorial_smul_hasseDeriv_single

## Inventory entry

### `theorem MvPolynomial.factorial_smul_hasseDeriv_single`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (j : σ) (n : ℕ) (P : MvPolynomial σ R), (n ! : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv j))^[n] P`
- **What**: `n! · Δ_{n e_j} P = ∂_j^n P`: the `n`-th iterate of the partial derivative in the variable `x_j` equals `n!` times the Hasse derivative of order `n e_j`. Over a `ℚ`-algebra this identifies `Δ_{n e_j}` with `(1/n!) ∂_j^n`.
- **How**: Induction on `n`; the zero case is `simp` (via `hasseDeriv_zero_apply`); the successor case rewrites with `Function.iterate_succ_apply'`, the induction hypothesis, `Derivation.map_smul`, the project lemma `pderiv_hasseDeriv` (`∂_j Δ_d = (d_j + 1) Δ_{d + e_j}`), `smul_smul`, `Finsupp.single_eq_same`, `Finsupp.single_add`, `Nat.factorial_succ`, `Nat.cast_mul`, `mul_comm`.
- **Hypotheses**: none beyond section variables `[CommSemiring R]`.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.pderiv_hasseDeriv`, `MvPolynomial.hasseDeriv_zero_apply` (via `simp` in the zero case)
- **Used by**: unused in project (no code callers; `grep -rn factorial_smul_hasseDeriv_single Roth/` finds only the declaration and the module docstring `Roth/HasseDeriv.lean:35`).
- **Visibility**: public
- **Lines**: 286–292, proof length 5 lines
- **Notes**: Listed under `## Main results` of the module docstring. It is the exact multivariate counterpart of mathlib's `Polynomial.factorial_smul_hasseDeriv` (Mathlib/Algebra/Polynomial/HasseDeriv.lean:133), whose proof has the same induction shape.

## Junk check (Step 8)
- Used anywhere? No code callers. It is documented API (module `## Main results`) and records the source's normalisation `Δ_i = (1/i!) ∂^i` (clean.tex §1).
- Wrapper of 1–2 mathlib calls? No: it needs the project's `hasseDeriv` and `pderiv_hasseDeriv`.
- Does mathlib have it? No (Phase 5): only the univariate `Polynomial.factorial_smul_hasseDeriv` and `LaurentSeries.derivative_iterate`.
- Too specific / inline? No: it is the standard comparison between Hasse and ordinary derivatives, the first fact any Hasse-derivative API states.
- Well-chosen? Yes; mathlib's univariate analogue is stated as an operator identity, which is the better upstream shape (see 4c).
- Conclusion: `KEEP`. Action: keep locally (cheap, documents the normalisation); upstream with the parent.

## Mathlibable assessment (Step 9)

Real content (5-line induction), not glue; full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; evidence file importing `Roth.HasseDeriv` elaborates without errors)
- decl `MvPolynomial.factorial_smul_hasseDeriv_single`: resolved at Roth/HasseDeriv.lean:286
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.factorial_smul_hasseDeriv_single` is a theorem stating the following:

Let `R` be a commutative semiring, `P ∈ R[x_σ]`, `j ∈ σ` and `n ∈ ℕ`. Then `n! · Δ_{n e_j} P = ∂_j^n P`, where `Δ_{n e_j}` is the Hasse derivative of multi-order `n e_j` and `∂_j` is the formal partial derivative in `x_j`. In characteristic zero this says `Δ_{n e_j} = ∂_j^n / n!`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`: variable index set.
- `R : Type*`, `[CommSemiring R]`: coefficients (needed by `MvPolynomial.pderiv`).
- `j : σ`: the variable.
- `n : ℕ`: the order.
- `P : MvPolynomial σ R`: the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `n! Δ_{n e_j} P = ∂_j^n P`.

Conclusion (Lean): `(n.factorial : R) • hasseDeriv (Finsupp.single j n) P = (⇑(pderiv j))^[n] P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic comparison lemma for the BIG parent `MvPolynomial.hasseDeriv`; listed in the module's `## Main results`, but it is a standard API lemma, not a main project theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a (kind is theorem, not def). Conclusion: MULTI-LINE.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | Hasse derivative multivariate "n!" partial derivative iterated equals factorial times Hasse derivative | yes | univariate `k! D^(k) = D^k`; multivariate Hasse derivative as coefficient of `Z^i` in `F(X+Z)` | arXiv 1707.01354, 1509.00279, mathlib docs; multivariate identity `i! Δ_i = ∂^i` implied by the binomial formula |
|  2 | WebSearch (general form) | Hasse-Schmidt derivation D^(n) n! D^(n) = D^n characteristic zero divided powers | yes | `δ^(n) = δ^n / n!` (exponential of a derivation) | Narváez Macarro, AIF 59 (2009), ar5iv 0903.0246; Hasse–Schmidt framework: `n! D_n = D_1^n` |
|  3 | WebSearch (aliases) | "Hasse derivative" multi-index "i_1! ⋯ i_n!" partial derivatives polynomial method multiplicities | yes | `Δ_i = (1/i!) ∂^i` in char 0; Hasse = ordinary derivative up to a nonzero constant | DKSS 0901.2529, 1707.01354, 2403.19824 |
|  4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "factorial", "frac{1}{i_1!" | yes | "Over a ℚ-algebra it agrees with Δ_i = (1/(i_1!⋯i_p!)) ∂_1^{i_1}⋯∂_p^{i_p}" (§1); "Convert ordinary iterated derivatives to Hasse derivatives by factorial scaling only over ℚ" (l.316) | the project lemma is the single-variable factor of this normalisation |
|  6 | nLab | nLab OR mathoverflow Hasse derivative divided power derivative (WebSearch, row 9 query) | no | no nLab page on Hasse derivatives surfaced | Wikipedia "Hasse derivative" gives `D^(r) = D^r / r!` in char 0 |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an identity between two explicit linear operators) |
|  8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry result; Stacks treats differential operators via principal parts, no Hasse-derivative identity of this form |
|  9 | MathOverflow / Math.SE | same query as row 6 | no | none surfaced | "The Digit Principle" (math/0002026) calls them divided-power derivatives and notes `D^(j) = D^j / j!` only for `j < p` in char p |
| 10 | recent arXiv | multivariate Hasse derivative factorial (rows 1, 3) | yes | 2511.04113, 2403.19824 define `Δ_β` via `f(x+y)`; identity used implicitly | standard background fact |

### Literature summary (Phase 3)

Concept identified as: comparison of Hasse (divided-power) derivatives with iterated ordinary derivatives, `i! Δ_i = ∂^i`.
Sources agree on the standard form: yes. The multi-index form is `(∏_j i_j!) Δ_i = ∏_j ∂_j^{i_j}`; the single-variable version `n! Δ_{n e_j} = ∂_j^n` is its one-coordinate factor, and the univariate one is mathlib's `Polynomial.factorial_smul_hasseDeriv`.
Most general standard form: (a) the full multi-index identity; (b) in operator-algebra form, the composition law `∂_j^n ∘ Δ_d = n! C(d_j + n, n) Δ_{d + n e_j}` (from `D^(k) D^(l) = C(k+l, k) D^(k+l)` with `D^(1) = ∂`); (c) abstractly, `n! D_n = D_1^n` for any iterative Hasse–Schmidt derivation.
Generality dimensions where the literature varies:
  - base multi-index: `0` (this lemma) up to arbitrary `d` (form (b)).
  - number of variables differentiated: one (`n e_j`) up to all (form (a)).
  - coefficient ring: literature states it over any commutative ring (identity is integral); this lemma is already over any commutative semiring.
Disagreement with the literature: none; the lemma is the special case `d = 0` of (b) and the one-coordinate case of (a).

### Generality analysis — `MvPolynomial.factorial_smul_hasseDeriv_single`

Literature-standard form (from Phase 3): `∂_j^n Δ_d = n! C(d_j + n, n) Δ_{d + n e_j}` for every multi-index `d` (and the full product form).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative ring | no | already weakest: `MvPolynomial.pderiv` requires `CommSemiring` |
| 2 | multi-index `Finsupp.single j n` acted on `P` directly | base index `0` | arbitrary base `d` | yes | verified: `iterate_pderiv_hasseDeriv` (evidence general.lean, item 2) compiles over `CommSemiring`, same induction with `pderiv_hasseDeriv` and `Nat.add_one_mul_choose_eq` |
| 3 | one variable `j` | `n e_j` | arbitrary `i` with `∏ i_j!` | partially | the full-product form needs a commuting product of iterated operators over `i.support`; it follows from (2) by induction on `i` but has no clean mathlib spelling (noncommutative-looking composition over a `Finset`); not proposed as the primary form |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (verified; row 2).
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem iterate_pderiv_hasseDeriv (j : σ) (n : ℕ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (⇑(pderiv (R := R) j))^[n] (hasseDeriv d P) =
      ((n ! * (d j + n).choose n : ℕ) : R) • hasseDeriv (d + Finsupp.single j n) P
```
with the project lemma recovered at `d = 0` (evidence item 2').

Cost of restatement: CHEAP — mechanical; the proof compiled on the second attempt.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | none; no bundled hypotheses | n/a |
| 2 | sequences to filters? | no | algebraic identity, no topology | n/a |
| 3 | construction to universal property? | no | identity between operators | n/a |
| 4 | set-with-predicate to bundled substructure? | no | none | n/a |
| 5 | field-specific to semiring? | no | already over `CommSemiring` | n/a |
| 6 | higher-categorical? | no | not categorical | n/a |
| 7 | concrete index to general monoid? | no | the index is `ℕ` because it counts iterations | n/a |
| 8 | concrete-via-abstract? | partially | the proof only uses `pderiv_hasseDeriv` (`∂_j Δ_d = (d_j+1) Δ_{d+e_j}`); it is the iterated form of that recurrence, i.e. the general-`d` statement above | gives `∂_j^n Δ_d` for every `d`, which is what downstream chain-rule expansions (source §5) iterate |
| 9 | false-generalisation guard | no false generalisation | the general-`d` form specialises exactly back to the lemma (item 2') | n/a |

Additional shape point: mathlib's univariate analogue is the operator identity `⇑(k ! • hasseDeriv k) = derivative^[k]`; the multivariate lemma should ship in the same shape (evidence item 1 shows it is a `funext` of the pointwise lemma).

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement:
    `theorem factorial_smul_hasseDeriv_single (j : σ) (n : ℕ) : ⇑((n ! : R) • hasseDeriv (Finsupp.single j n)) = (⇑(pderiv j))^[n]`
  - Cost: CHEAP (evidence item 1)
  - Mathlib downstream this enables: name and shape parallel to `Polynomial.factorial_smul_hasseDeriv` and `LaurentSeries.derivative_iterate`, so the univariate-to-multivariate transfer through `uniqueAlgEquiv_hasseDeriv` and `hasseDeriv_single_aeval_X` is lemma-for-lemma.
  - Real mathematical improvement: consistency with the existing univariate API (an organisational improvement, not new content); the substantive change is the general-`d` form from 4b.

### Proof strategy — `MvPolynomial.factorial_smul_hasseDeriv_single`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | n/a | n/a |
| 2 | elements vs point-free | no | the operator form is a `funext` away | CHEAP |
| 3 | sequences vs nets | no | n/a | n/a |
| 4 | construction vs universal property | no | n/a | n/a |
| 5 | missing mathlib helpers | yes | `hasseDeriv_single_one : hasseDeriv (single j 1) = (pderiv j).toLinearMap` and the composition law, as in the `pderiv_hasseDeriv` report; then the lemma is an induction exactly mirroring `Polynomial.factorial_smul_hasseDeriv` | shipped together with the parent |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Induction on `n` with the one-step recurrence is how mathlib proves the univariate analogue. Proving the general-`d` form first and deriving this one at `d = 0` is the recommended order, at no extra cost.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.factorial_smul_hasseDeriv_single`

[A] Lean-Finder       "n factorial times n-th Hasse derivative equals n-th iterate of the partial derivative in one variable of MvPolynomial"   hits: only univariate `Polynomial.factorial_smul_hasseDeriv`, `hasseDeriv_one'`, `hasseDeriv_comp`
[B] Loogle            `MvPolynomial.pderiv, Nat.factorial`   no hits
[C] LeanSearch        "iterated partial derivative of multivariate polynomial equals factorial times Hasse derivative"   hits: `Polynomial.factorial_smul_hasseDeriv`, `Polynomial.iterate_derivative_eq_factorial_smul_sum`, `LaurentSeries.derivative_iterate` (all univariate); no multivariate result
[D] Grep mathlib src  `hasseDeriv` (only Polynomial/HasseDeriv.lean, Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean); `pderiv.*\^\[` (no hits); `iterate` in MvPolynomial/PDeriv.lean (no hits)   no multivariate hit
[E] Name pattern      `lean_local_search factorial_smul_hasseDeriv`: n/a, tool error (ripgrep not installed); replaced by the namespace-aware grep in [D], which finds no `MvPolynomial.factorial_smul_hasseDeriv*`

Searched for both:
  - the user's current form
  - the literature-standard general-`d` form and the full multi-index form (no `MvPolynomial.hasseDeriv` exists, so neither can be in mathlib)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form).

### Normal-form check — `MvPolynomial.factorial_smul_hasseDeriv_single`

Equivalent formalisms: pointwise `n! • Δ P = ∂^[n] P`; operator `⇑(n! • Δ) = ∂^[n]`; `Δ = (n!)⁻¹ • ∂^n` over a `ℚ`-algebra.
Does mathlib already have a canonical form for this idea? yes, univariately: `Polynomial.factorial_smul_hasseDeriv` (operator form, iterate on the RHS).
Is our statement stated against it? Same orientation (Hasse side on LHS, iterate on RHS); shape differs (pointwise vs operator).
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.factorial_smul_hasseDeriv_single`

Alternative restatements attempted:
- operator form `⇑((n ! : R) • hasseDeriv (single j n)) = (⇑(pderiv j))^[n]` (evidence item 1)
- general base index `iterate_pderiv_hasseDeriv` (evidence item 2)

Chosen restatement: general-`d` form as the main lemma, operator form of the `d = 0` case named `factorial_smul_hasseDeriv_single` (pointwise version available by `congrFun`).
Justification: the general form is what iterated chain-rule computations need; the operator form matches the univariate API name and shape.

### Superfluous-argument audit — `MvPolynomial.factorial_smul_hasseDeriv_single`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `pderiv` |
| 2 | `j`, `n`, `P` | yes | the data of the statement |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (general-`d` main lemma, operator-form corollary)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.factorial_smul_hasseDeriv_single`

Internal use count: 0  (outside the declaring file; none inside it either)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/HasseDeriv.lean:35 | module docstring only: "`MvPolynomial.factorial_smul_hasseDeriv_single`: `n! • Δ_{n e_j} = ∂_j ^ n`" |

Inline-derivation grep (was the equivalent re-derived elsewhere?):
  - (none): `grep -rn "pderiv.*\^\[\|factorial" Roth/` shows no inline re-derivation of `n! Δ = ∂^n`; the project works with `hasseDeriv` and `pderiv_hasseDeriv` directly.

K = 0 with no inline re-derivation: the lemma is unused locally, but it is the standard comparison lemma a mathlib Hasse-derivative file must have (its univariate counterpart is a headline result of Mathlib/Algebra/Polynomial/HasseDeriv.lean even though no other mathlib file cites it; checked by grep), so the unused status reflects that the project only needs the one-step `pderiv_hasseDeriv`.

### Composition check (Phase 6)

Can the lemma be derived from mathlib in ≤3 chained calls?

Attempt 1: transport `Polynomial.factorial_smul_hasseDeriv` through `uniqueAlgEquiv`/`hasseDeriv_single_aeval_X`.
  - Mathlib decls used: `Polynomial.factorial_smul_hasseDeriv`; but also project `hasseDeriv`, `hasseDeriv_single_aeval_X`, and a missing bridge `pderiv j ∘ toMvPolynomial j = toMvPolynomial j ∘ derivative` (absent from mathlib, see the `hasseDeriv_single_aeval_X` report), and it would only cover polynomials in `x_j` alone.
  - Result: fails.
Attempt 2: induction using `pderiv_hasseDeriv` (current proof).
  - Uses non-mathlib API (`hasseDeriv`, `pderiv_hasseDeriv`).
  - Result: a real proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.factorial_smul_hasseDeriv_single`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): `i! Δ_i = ∂^i` is the standard comparison (Wikipedia "Hasse derivative", DKSS 0901.2529, 1707.01354, Narváez Macarro AIF 2009, source clean.tex §1).
- Generality analysis (Phase 4): STRICTLY NARROWER; the general-base-index form `iterate_pderiv_hasseDeriv` compiles (evidence item 2) and gives back the lemma at `d = 0` (item 2').
- Mathlib search (Phase 5): not in mathlib; only the univariate `Polynomial.factorial_smul_hasseDeriv` and `LaurentSeries.derivative_iterate`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` is YES-but-generalise-first because mathlib has only univariate Hasse derivatives. Any multivariate Hasse-derivative file needs the comparison with iterated partial derivatives. Mathlib's univariate file ships `Polynomial.factorial_smul_hasseDeriv` for exactly this reason, and the source (clean.tex §1) states the normalisation `Δ_i = ∂^i / i!` as the defining property over `ℚ`. This lemma is the one-variable factor of that identity, over any commutative semiring.

Its proof only iterates the one-step recurrence `pderiv_hasseDeriv`, so it extends at no extra cost to an arbitrary base index: `∂_j^n Δ_d = n! C(d_j + n, n) Δ_{d + n e_j}` (verified). That form is what iterated chain-rule expansions need (source §5 differentiates `Δ_d φ(γ(t))` repeatedly). The present lemma is its `d = 0` case. The corollary should be stated as an operator identity to match `Polynomial.factorial_smul_hasseDeriv`.

Reason for the generalisation: LITERATURE-WEAKENING (arbitrary base multi-index) and MODERN-IDIOM (operator shape matching the univariate mathlib lemma).
Proposed restatement:
```lean
theorem iterate_pderiv_hasseDeriv (j : σ) (n : ℕ) (d : σ →₀ ℕ) (P : MvPolynomial σ R) :
    (⇑(pderiv (R := R) j))^[n] (hasseDeriv d P) =
      ((n ! * (d j + n).choose n : ℕ) : R) • hasseDeriv (d + Finsupp.single j n) P := by
  sorry -- proof compiled in evidence general.lean

theorem factorial_smul_hasseDeriv_single (j : σ) (n : ℕ) :
    ⇑((n ! : R) • hasseDeriv (σ := σ) (R := R) (Finsupp.single j n)) =
      (⇑(pderiv (R := R) j))^[n] := by
  sorry -- d = 0 case of the above, compiled in evidence general.lean
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - lemma-for-lemma parallel with `Polynomial.factorial_smul_hasseDeriv` and `LaurentSeries.derivative_iterate`, so univariate results transfer through `uniqueAlgEquiv_hasseDeriv`;
  - over a `ℚ`-algebra, `hasseDeriv (single j n) = (n ! : R)⁻¹ • (pderiv j)^n`, connecting `MvPolynomial.pderiv` (Mathlib/Algebra/MvPolynomial/PDeriv.lean) to Hasse derivatives, which mathlib cannot currently state;
  - the general-`d` form computes `∂_j^n ∘ Δ_d`, needed for iterated chain rules and multiplicity arguments.
WHY it belongs in mathlib (gap): mathlib has no multivariate Hasse derivative and no lemma linking iterated `MvPolynomial.pderiv` to divided-power derivatives; the univariate file has `factorial_smul_hasseDeriv` as a headline result (Mathlib/Algebra/Polynomial/HasseDeriv.lean:30), and its multivariate counterpart is the missing piece.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new, with the parent).
PR grouping: ship with `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_hasseDeriv`, `pderiv_hasseDeriv`, `uniqueAlgEquiv_hasseDeriv`.
Next action: run `/generalise MvPolynomial.factorial_smul_hasseDeriv_single` (target: `iterate_pderiv_hasseDeriv` plus the operator-form corollary) before opening the PR.

---

## Next step

Upstream with the parent as `iterate_pderiv_hasseDeriv` (general `d`) and `factorial_smul_hasseDeriv_single` in operator form (the `d = 0` corollary). Locally, keep the lemma as is: it has no code callers and it documents the source's normalisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.factorial_smul_hasseDeriv_single/general.lean` (imports `Roth.HasseDeriv`), checked with `lean_diagnostic_messages`: success, no errors. Contents:
  - (1) Operator form `⇑((n ! : R) • hasseDeriv (single j n)) = (⇑(pderiv j))^[n]`, by `funext` and the project lemma.
  - (2) `iterate_pderiv_hasseDeriv`: general base multi-index form, by induction with `pderiv_hasseDeriv`, `Finsupp.single_add` and `Nat.add_one_mul_choose_eq`.
  - (2') The project lemma recovered from (2) at `d = 0`.
- Iterations: the first attempt failed (an `add_assoc` rewrite hit the wrong subterm and the name `Nat.succ_mul_choose_eq` does not exist); fixed with `add_assoc d` and `Nat.add_one_mul_choose_eq` plus a `calc`. No cold `lake env lean` run.
- Searches: Lean-Finder, Loogle, LeanSearch as in [A]–[C]; mathlib grep [D]; `lean_local_search` unavailable (ripgrep missing).
- WebSearch: 4 queries (table rows 1–3, 6/9). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn factorial_smul_hasseDeriv_single Roth/`; `.mathlib-quality/references/clean.tex` §1 (l.119–150) and l.316.
