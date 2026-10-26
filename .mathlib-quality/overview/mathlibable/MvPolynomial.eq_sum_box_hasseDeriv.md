---
decl: MvPolynomial.eq_sum_box_hasseDeriv
file: Roth/Taylor.lean
line: 197
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multivariate Taylor expansion P = sum (Δ_d P)(α) (X - α)^d is standard and absent from mathlib (only univariate Polynomial.sum_taylor_eq), but the box form with Fintype, DecidableEq, a degree hypothesis and Roth.box is a corollary; the mathlib form is the hypothesis-free support-sum analogue of Polynomial.sum_taylor_eq plus an arbitrary-superset version, both compiled in evidence.
action: Upstream in the MvPolynomial.taylor PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) as sum_taylor_eq (arbitrary σ, Finsupp.prod) and eq_sum_hasseDeriv_of_subset, with the box statement over Finset.Iic (Finsupp.equivFunOnFinite.symm r) as corollary (evidence items 2-4); locally keep (only caller eval_eq_sum_box at Roth/Taylor.lean:220, used at Roth/Main.lean:390).
---

# MvPolynomial.eq_sum_box_hasseDeriv

## Inventory entry

### `theorem MvPolynomial.eq_sum_box_hasseDeriv`
- **Type**: `{σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) : P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j`
- **What**: Taylor's expansion of a multivariate polynomial about `α`: if `deg_{X_j} P ≤ r_j` for every `j`, then `P = Σ_{d ≤ r} (Δ_d P)(α) ∏_j (X_j − α_j)^{d_j}`.
- **How**: first shows `taylor α P = ∑ d ∈ box r, monomial d (eval α (hasseDeriv d P))` coefficientwise via `coeff_taylor`, `coeff_sum`, `coeff_monomial`, `Finset.sum_ite_eq'`, and (outside the box) `Roth.mem_box` plus `hasseDeriv_eq_zero_of_degreeOf_lt`; then writes `P = taylor (-α) (taylor α P)` (`taylor_neg_taylor`), pushes `taylor (-α)` through the sum (`map_sum`), and rewrites each term with `taylor_monomial` and `Finsupp.prod_fintype`.
- **Hypotheses**: `[CommRing A]` (subtraction in `X j - C (α j)`, and `taylor_neg_taylor`), `[Fintype σ]` (the product `∏ j` and `Roth.box`), `[DecidableEq σ]` (for `Roth.box`), `hP` (degree bound per variable, so that the box contains all nonzero Taylor coefficients).
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.coeff_taylor`, `MvPolynomial.taylor_neg_taylor`, `MvPolynomial.taylor_monomial`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt`, `Roth.box`, `Roth.mem_box`
- **Used by**: Roth/Taylor.lean:220 (`eval_eq_sum_box`, which is in turn used at Roth/Main.lean:390). No other project uses (`grep -rn eq_sum_box_hasseDeriv Roth/`).
- **Visibility**: public
- **Lines**: 195–212 (docstring 195–196), proof length 14 lines
- **Notes**: listed under `## Main results` of Roth/Taylor.lean; formalises the Theorem "Taylor's expansion for polynomials in several variables" of the source paper §4 (clean.tex l.502).

## Junk check (Step 8)
- Used anywhere? Yes, once directly (`eval_eq_sum_box`, Roth/Taylor.lean:220), and transitively in the main proof (Roth/Main.lean:390).
- Wrapper of 1–2 mathlib calls? No; it needs `coeff_taylor` (project theorem) plus a translation-inverse argument (14-line proof).
- Does mathlib have it? No. Only the univariate `Polynomial.sum_taylor_eq` (Mathlib/Algebra/Polynomial/Taylor.lean:208). No `MvPolynomial.taylor` exists in mathlib.
- Too specific (inline?)? The box/degree-bound shape is the paper's shape and is what `eval_eq_sum_box` needs; it is a reasonable named corollary. The general content is the hypothesis-free support-sum form (evidence item 2).
- Well-chosen definition? n/a (theorem). It is stated against `Roth.box`, whose report says REPLACE with `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`; evidence item 4 shows the statement over `Finset.Iic` compiles.

Conclusion: `KEEP`. Action: none locally beyond the parent `Roth.box` REPLACE (switch the sum to `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` when `box` is replaced).

## Mathlibable assessment (Step 9)

Pre-filter: not private; name does not end `_aux`; docstring does not start internal/auxiliary; Step 8 said KEEP; `eq_sum_box_hasseDeriv` / `eq_sum_hasseDeriv` / `MvPolynomial.sum_taylor_eq` do not occur in `.lake/packages/mathlib/Mathlib/` (grep, no hits). Not a glue lemma (14-line proof with real content), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.Taylor` elaborates)
- decl `MvPolynomial.eq_sum_box_hasseDeriv`: ✓ resolved at Roth/Taylor.lean:197
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: the translation `P ↦ P(X + α)`, its coefficients as Hasse derivatives, and Taylor's expansion over a box.

### Statement (Phase 1)

`MvPolynomial.eq_sum_box_hasseDeriv` is a theorem stating the following:

Let `A` be a commutative ring, `σ` a finite set of variables, `α ∈ A^σ`, and `r ∈ ℕ^σ`. If `P ∈ A[X_σ]` has degree at most `r_j` in each variable `X_j`, then
`P = Σ_{0 ≤ d ≤ r} (Δ_d P)(α) · ∏_j (X_j − α_j)^{d_j}`,
where `Δ_d` is the multi-index Hasse derivative. That is, `P` equals its (finite) Taylor expansion about `α`, the sum running over the box of multi-indices bounded by `r`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]`, `[DecidableEq σ]` — the finite variable set
- `A : Type*`, `[CommRing A]` — coefficient ring
- `α : σ → A` — expansion point
- `r : σ → ℕ` — per-variable degree bound (box size)
- `P : MvPolynomial σ A`

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — the box contains all multi-indices with possibly nonzero Taylor coefficient

Conclusion (math): `P = Σ_{d ≤ r} (Δ_d P)(α) (X − α)^d`.

Conclusion (Lean): `P = ∑ d ∈ Roth.box r, C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j`

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of Roth/Taylor.lean and is the named theorem "Taylor's expansion for polynomials in several variables" (source paper §4).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 14 (theorem)
One-liner verdict: n/a (kind is theorem/lemma, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Taylor expansion polynomial several variables P(x) = sum Hasse derivative at alpha times product (x_j - alpha_j)^{i_j} | yes | `F(X) = Σ_i (H(F,i))(p) (X − p)^i`, finite sum over all multi-indices; `H(F,i)` = coefficient of `Z^i` in `F(X+Z)` | arXiv 1402.0643, 1509.00279 (multiplicity codes), 2111.07572, 1310.6482 (polynomial-method survey), 1707.01354 |
| 2 | WebSearch (general form) | multivariate polynomial expansion around a point f(x) = sum_i D^(i) f(a) (x-a)^i Hasse derivatives commutative ring finite sum | yes | over any commutative ring: `D^e f` = coefficient of `z^e` in `f(x+z)`; expansion about `a` by substituting `z = x − a`; sum finite (over the support) | arXiv 2205.00342 Def 3.4, 1303.0084, Hasse–Schmidt surveys 1810.08075, 1802.09894 |
| 3 | WebSearch (named-after / aliases) | Roth's theorem index of polynomial Taylor expansion "index" Delta P(alpha) Schmidt Diophantine approximation | partial | Roth-type index defined via derivatives `Δ_i P(α)` (Schmidt LNM 785 Ch. II, IV); Taylor expansion in the box `i_j ≤ r_j` is the form used there | arXiv 2502.00731 (Goel–Lunia–Ray exposition of Roth/subspace), math/0307203, Evertse lecture notes |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Taylor / expansion | yes | l.502–507: Theorem "Taylor's expansion for polynomials in several variables": degree `≤ r_i` in `x_i`, any `d_i ≥ r_i`, `P = Σ_{i_1 ≤ d_1}…Σ_{i_p ≤ d_p} (Δ_i P)(α) ∏ (x_j − α_j)^{i_j}`; proof by linearity + one-variable binomial (l.509–528) | exactly the project statement (with `r` playing the role of `d`) |
| 6 | nLab | Hasse-Schmidt derivation / Taylor expansion | partial | Hasse–Schmidt derivations as coefficients of `f ↦ f(x+t)` | no entry for the polynomial Taylor identity itself; consistent with #2 |
| 7 | nCatLab | — | n/a | — | not a categorical concept (an identity in a polynomial ring) |
| 8 | Stacks Project | — | n/a | — | elementary polynomial algebra; Stacks covers principal parts/differential operators but has no tag for the concrete polynomial Taylor formula |
| 9 | MathOverflow / Math.SE | (via #1–#3) | partial | same `f(x) = Σ D^i f(a) (x−a)^i` | no dedicated thread surfaced; usage consistent |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2205.00342 (2022), 2111.07572 (2021), 2502.00731 (2025) | all state the expansion as a finite sum over the support / all multi-indices, no box hypothesis needed |

### Literature summary (Phase 3)

Concept identified as: Taylor's formula (expansion about a point) for multivariate polynomials with Hasse derivatives.
Sources agree on the standard form: yes. The coding-theory/polynomial-method literature writes `P(X) = Σ_d (Δ_d P)(α) (X − α)^d` with the sum over all multi-indices (finitely many nonzero terms), over any commutative ring. Diophantine-approximation sources (Schmidt, the project paper) restrict the sum to a box `d ≤ r` containing the degree profile of `P`.
Most general standard form: for `A` a commutative ring, any variable set, `P = Σ_d (Δ_d P)(α) (X − α)^d`, the sum over the (finite) set of `d` with `(Δ_d P)(α) ≠ 0`, or over any finite set containing it.
Generality dimensions where the literature varies:
  - index set of the sum: support of the translate (most general, no hypothesis) vs. a box `d ≤ r` with a degree hypothesis (Roth/Schmidt); the box form is a specialisation.
  - number of variables: finite `p` (all sources) vs. arbitrary `σ` (possible with `Finsupp.prod` instead of `∏ j`).
  - coefficient ring: reals (project paper) to any commutative ring; ours is `CommRing`, needed for `X − α`.
Disagreement with the literature: none mathematically; the Lean form is the narrower box specialisation.

### Generality analysis — `MvPolynomial.eq_sum_box_hasseDeriv`

Literature-standard form (from Phase 3): `P = Σ_{d ∈ supp(taylor α P)} (Δ_d P)(α) ∏ (X_j − α_j)^{d_j}` over any commutative ring and any variable set; equivalently, over any finite `s` containing that support. Exact multivariate analogue of mathlib's `Polynomial.sum_taylor_eq`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing A]` | commutative ring | commutative ring | no | `X j - C (α j)` needs `Sub`; evidence item 1: `#check_failure` of `X j - C (α j)` over `[CommSemiring R]` fails to synthesize `HSub` |
| 2 | `[Fintype σ]` | finite variables | arbitrary (sum over support, `Finsupp.prod`) | yes | evidence item 2 (`sum_taylor_eq`) and item 3 compile for arbitrary `σ` using `d.prod fun j n ↦ (X j - C (α j)) ^ n` |
| 3 | `[DecidableEq σ]` | required by `Roth.box` | not needed | yes | items 2, 3 have no `DecidableEq σ` (only `classical`-free proofs over the support); the box form over `Finset.Iic` still needs it for the `LocallyFiniteOrder (σ →₀ ℕ)` instance |
| 4 | `hP : ∀ j, degreeOf j P ≤ r j` | degree-box hypothesis | none (sum over support) or `(taylor α P).support ⊆ s` | yes | item 2 has no hypothesis; item 3 takes `hs : (taylor α P).support ⊆ s`; item 6 shows `hP` cannot simply be dropped from the box form itself (counterexample `P = X 0`, `r = 0`) |
| 5 | `Roth.box r` | project-local Finset | `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` | yes (re-aim) | parent report Roth.box: NO-mathlib-has-it / REPLACE; item 4 compiles over `Finset.Iic`, and item 5 recovers the original statement from it |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4 (drop `Fintype σ`, drop `DecidableEq σ`, drop/abstract `hP`, replace `Roth.box` by mathlib's `Finset.Iic`) — all verified by compiling evidence items 2–5 with `lean_diagnostic_messages` (no errors).
Proposed restatement (if STRICTLY NARROWER):

```lean
-- core, mirrors Polynomial.sum_taylor_eq
theorem MvPolynomial.sum_taylor_eq {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A) :
    ∑ d ∈ (taylor α P).support,
      C ((taylor α P).coeff d) * d.prod (fun j n ↦ (X j - C (α j)) ^ n) = P
-- any superset of the support, Hasse-derivative coefficients
theorem MvPolynomial.eq_sum_hasseDeriv_of_subset (α : σ → A) (P : MvPolynomial σ A)
    (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    P = ∑ d ∈ s, C (eval α (hasseDeriv d P)) * d.prod fun j n ↦ (X j - C (α j)) ^ n
-- the project's box form, as corollary
theorem MvPolynomial.eq_sum_Iic_hasseDeriv [Fintype σ] [DecidableEq σ] (α : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r),
      C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j
```

Cost of restatement: CHEAP (all three compiled with short proofs in the evidence file; the original follows in 3 lines, item 5).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|----------|----------|------------------------|----------------------------------|
|  1 | preambles to typeclasses? | no | — | hypothesis `hP` is a genuine data-dependent condition, not a structure |
|  2 | sequences to filters? | no | — | purely algebraic |
|  3 | construction vs universal property? | no | — | identity in a polynomial ring |
|  4 | set-with-predicate to bundled substructure? | partial | the box is "multi-indices bounded by r"; mathlib's bundled form is the order interval `Finset.Iic` in `σ →₀ ℕ` | `Finset.mem_Iic`, `Finsupp.card_Iic` (see Roth.box report) |
|  5 | field-specific to semiring? | no | already `CommRing`, which is needed for subtraction | — |
|  6 | higher-categorical? | no | — | — |
|  7 | concrete index to general? | yes | `Fintype σ` + `∏ j` to arbitrary `σ` + `Finsupp.prod` | matches `MvPolynomial` API conventions (`monomial_eq`, `eval_eq` uses `∏ i ∈ d.support`) |
|  8 | concrete-via-abstract? | no | the box `Roth.box r` appears in the proof only to discard out-of-box terms; that is exactly the subset abstraction of item 3 (already counted in 4b), not a hidden abstract witness | — |
|  9 | false-generalisation guard | no false generalisation | items 2–4 are the same identity; item 5 recovers the original statement verbatim | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the support-sum `sum_taylor_eq` (shape of `Polynomial.sum_taylor_eq`) with the box form stated over `Finset.Iic` as a corollary (see 4b).
  - Cost: CHEAP
  - Mathlib downstream this enables: same normal form as the univariate `Polynomial.sum_taylor_eq`; the box version uses mathlib's `LocallyFiniteOrder (σ →₀ ℕ)` API (`Finset.mem_Iic`, `Finsupp.card_Iic`) instead of a project-local finset.
  - Real mathematical improvement: removes three superfluous hypotheses (`Fintype`, `DecidableEq`, `hP`) from the core identity, which then applies to any polynomial without a degree bookkeeping step.

### Proof strategy — `MvPolynomial.eq_sum_box_hasseDeriv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|------------------------|----------------|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | helper lemmas mathlib SHOULD have | yes | `MvPolynomial.sum_taylor_eq` itself (the support form) should be the core lemma, and the box form a `Finset.sum_subset` corollary; also the `taylorEquiv` of the taylor_neg_taylor report | CHEAP (evidence items 2–4) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove the hypothesis-free `sum_taylor_eq` (3 lines: `taylor_neg_taylor`, `as_sum`, `map_sum`, `taylor_monomial`), then `eq_sum_hasseDeriv_of_subset` via `Finset.sum_subset` and `coeff_taylor`, then the box form by showing `support ⊆ Iic r` from `hasseDeriv_eq_zero_of_degreeOf_lt`. This is exactly the univariate mathlib route (`sum_taylor_eq` via `taylor_taylor`).
  - Cost: CHEAP
  - Missing mathlib API (if any): none beyond the MvPolynomial Taylor/HasseDeriv PRs.
  - Would refactoring make the proof strictly shorter / cleaner? yes (the coefficientwise `h1` with `split_ifs` disappears from the core lemma).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.eq_sum_box_hasseDeriv`

[A] Lean-Finder       "multivariate polynomial equals sum over multi-indices of Taylor coefficients at a point times product of (X_j - a_j)^{d_j}"   only univariate `Polynomial.sum_taylor_eq`, `Polynomial.taylor`, `taylorEquiv`, `taylorLinearEquiv`, `taylorWithin` (analysis)
[B] Loogle            `MvPolynomial.X _ - MvPolynomial.C _`   3 hits: `MonomialOrder.monic_X_sub_C`, `MonomialOrder.degree_X_sub_C`, `combinatorial_nullstellensatz_exists_linearCombination`; none an expansion identity
[C] LeanSearch        "Taylor's formula for MvPolynomial: P equals sum of C (coefficient) times product (X i - C (a i)) ^ d i"   `Polynomial.taylor_apply`, `Polynomial.sum_taylor_eq`, `MvPolynomial.eval_eq`, `eval_eq'`, `Polynomial.taylor_coeff`, `MvPowerSeries.aeval_eq_sum` (topological evaluation, unrelated)
[D] Grep mathlib src  `eq_sum_box`, `sum_box_hasseDeriv`, `eq_sum_hasseDeriv`, `MvPolynomial.sum_taylor`, `taylor` under Mathlib/Algebra/MvPolynomial and Mathlib/RingTheory/MvPolynomial   no hits
[E] Name pattern      `MvPolynomial.taylor`, `MvPolynomial.sum_taylor_eq`, `MvPolynomial.eq_sum_box_hasseDeriv` (grep + parent reports)   no hits

Searched for both:
  - the user's current form (box sum with Hasse coefficients and `∏ (X j - C (α j))^(d j)`)
  - the literature-standard form (support-sum Taylor formula, analogue of `Polynomial.sum_taylor_eq`)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); only the univariate `Polynomial.sum_taylor_eq`.

### Normal-form check — `MvPolynomial.eq_sum_box_hasseDeriv`

Equivalent formalisms this statement could take: (i) `P = ∑ d ∈ box, C(Δ_d P(α)) * ∏ (X−α)^d` (current); (ii) `(sum over support of taylor α P of C a * (X−α)^d) = P` (mathlib univariate shape); (iii) `taylor (-α) (taylor α P) = P` (already `taylor_neg_taylor`); (iv) evaluated form `eval x P = …` (project `eval_eq_sum_box`).
Does mathlib already have a canonical form for this idea? For one variable: `Polynomial.sum_taylor_eq` in shape (ii), with `P` on the RHS.
Our statement is not in the canonical shape: it has `P` on the LHS (fine for `rw` at the call site, but non-canonical) and a box instead of the support.
RHS convention respected? no (for the core lemma, mathlib puts `f` on the RHS: `… = f`); the box corollary may keep `P = …` since it is used by `congrArg (eval x)`.

### Syntactic generality — `MvPolynomial.eq_sum_box_hasseDeriv`

Alternative restatements attempted:
- (a) support sum, no hypotheses (evidence item 2)
- (b) arbitrary superset `s` of the support (evidence item 3)
- (c) box via `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` with `hP` (evidence item 4)
- (d) current, with `Roth.box`
Chosen restatement: (a) as the core, (b) as the workhorse, (c) as the paper-shaped corollary.
Justification: (b) is easiest to apply (any convenient index finset, only a support containment to check); (c) is what `eval_eq_sum_box` needs; (a) matches mathlib's univariate lemma.

### Superfluous-argument audit — `MvPolynomial.eq_sum_box_hasseDeriv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing A]` | yes | subtraction (evidence item 1) and inverse translation |
| 2 | `[Fintype σ]` | no (for the identity) | only for `∏ j`; replace by `Finsupp.prod` (items 2, 3) |
| 3 | `[DecidableEq σ]` | no (for the identity) | only for `Roth.box`/`Finset.Iic` |
| 4 | `hP` | only for the box form | the identity itself needs none (item 2); in the box form it is necessary (item 6) |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (core lemma in `Polynomial.sum_taylor_eq` shape, `… = P`)
Syntactic generality: RESTATE (add `eq_sum_hasseDeriv_of_subset`; box form over `Finset.Iic`)
Superfluous arguments: 3 to drop from the core (`Fintype σ`, `DecidableEq σ`, `hP`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.eq_sum_box_hasseDeriv`

Internal use count: 0 (outside the declaring file); 1 inside it
External-to-file callers: 0 distinct files directly (transitively Roth/Main.lean via `eval_eq_sum_box`)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:220 | `simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)` (`eval_eq_sum_box`) |
| Roth/Main.lean:390 (transitive, via `eval_eq_sum_box`) | `rw [eval_eq_sum_box (fun _ ↦ α) (fun j ↦ (h j : ℝ) / q j) r Q hd]` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `eq_sum_box_hasseDeriv`?):
  - (none) — `grep -rn "X j - C (α j)\|taylor_neg_taylor" Roth/` finds only Taylor.lean.

### Composition check (Phase 6)

Can `MvPolynomial.eq_sum_box_hasseDeriv` be derived from mathlib in ≤3 chained calls?

Attempt 1: transport `Polynomial.sum_taylor_eq` one variable at a time (`finSuccEquiv`)
  - Mathlib decls used: `Polynomial.sum_taylor_eq`, `MvPolynomial.finSuccEquiv`
  - Result: fails — needs induction on the number of variables and a multivariate Hasse derivative/taylor compatibility that mathlib lacks.

Attempt 2: from project API only: `taylor_neg_taylor` + `as_sum` + `map_sum` + `taylor_monomial` + `coeff_taylor` + `Finset.sum_subset`
  - Mathlib decls used: `MvPolynomial.as_sum`, `map_sum`, `Finset.sum_subset`, `Finsupp.prod_fintype`
  - Result: succeeds but as a multi-step proof using project (non-mathlib) lemmas (evidence items 2–4), not a ≤3-call mathlib composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.eq_sum_box_hasseDeriv`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the multivariate Taylor expansion `P = Σ (Δ_d P)(α)(X−α)^d` is standard over commutative rings (arXiv 1402.0643, 2205.00342, multiplicity codes; Schmidt LNM 785; project paper §4 l.502), stated over the support or over a box.
- Generality analysis (Phase 4): STRICTLY NARROWER — `Fintype σ`, `DecidableEq σ`, `hP` and `Roth.box` all removable/replaceable, verified by compiling evidence items 2–5; `CommRing` is necessary (item 1).
- Mathlib search (Phase 5): not in mathlib; only univariate `Polynomial.sum_taylor_eq`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib has Taylor's formula for one variable (`Polynomial.sum_taylor_eq`, Mathlib/Algebra/Polynomial/Taylor.lean:208) but nothing for `MvPolynomial`. There is no multivariate translation, no multivariate Hasse derivative, and no expansion of `P` in powers of `X − α`. This is the gap. The identity is the basic tool of the method of multiplicities and of index arguments in Diophantine approximation, so it belongs in the planned `MvPolynomial.taylor` PR.

As stated, though, the project lemma is the paper's box specialisation. It asks for a finite variable type, `DecidableEq`, a per-variable degree bound, and the project-local `Roth.box`. That box is itself slated for replacement by `Finset.Iic` (Roth.box report: NO-mathlib-has-it). The real content holds with no hypotheses at all, as the support-sum identity exactly parallel to `Polynomial.sum_taylor_eq`. The evidence file compiles it in 3 lines, then a superset-`s` version, then the box form over `Finset.Iic`. It also recovers the original statement in 3 lines and shows that `hP` is necessary in the box form. So the lemma should ship in the general form, with the box version as a corollary. Cost is CHEAP.

Reason for the generalisation: LITERATURE-WEAKENING (support-sum form with no hypotheses; arbitrary `σ`) and MODERN-IDIOM (mathlib `Finset.Iic` instead of `Roth.box`, `Polynomial.sum_taylor_eq` normal form).
Proposed restatement:
```lean
theorem MvPolynomial.sum_taylor_eq {σ A : Type*} [CommRing A] (α : σ → A) (P : MvPolynomial σ A) :
    ∑ d ∈ (taylor α P).support,
      C ((taylor α P).coeff d) * d.prod (fun j n ↦ (X j - C (α j)) ^ n) = P := by
  sorry  -- proved in evidence item 2

theorem MvPolynomial.eq_sum_hasseDeriv_of_subset {σ A : Type*} [CommRing A] (α : σ → A)
    (P : MvPolynomial σ A) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    P = ∑ d ∈ s, C (eval α (hasseDeriv d P)) * d.prod fun j n ↦ (X j - C (α j)) ^ n := by
  sorry  -- proved in evidence item 3

theorem MvPolynomial.eq_sum_Iic_hasseDeriv {σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ]
    (α : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    P = ∑ d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r),
      C (eval α (hasseDeriv d P)) * ∏ j, (X j - C (α j)) ^ d j := by
  sorry  -- proved in evidence item 4
```
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- the same normal form as `Polynomial.sum_taylor_eq`, so univariate/multivariate statements line up (`uniqueAlgEquiv` bridges in the taylor report);
- the box corollary uses `Finset.mem_Iic` / `Finsupp.card_Iic` from mathlib's `LocallyFiniteOrder (σ →₀ ℕ)` rather than project API;
- downstream users (method of multiplicities, Schwartz–Zippel with multiplicities) get the expansion with no degree bookkeeping.
Proposed mathlib location: `Mathlib/Algebra/MvPolynomial/Taylor.lean` (new; with `MvPolynomial.taylor`, `coeff_taylor`, `taylor_neg_taylor`/`taylorEquiv`)
PR grouping: Taylor PR, after the `MvPolynomial.hasseDeriv` + `Finsupp.choose` PR; `eval_eq_sum_box` (evaluated form) ships as its corollary.
Next action: run `/generalise MvPolynomial.eq_sum_box_hasseDeriv` to adopt the three-lemma layout above (and switch `Roth.box` to `Finset.Iic` per the parent report), then `/cleanup Roth/Taylor.lean` before the PR.

## Next step

Restate as `sum_taylor_eq` (core) + `eq_sum_hasseDeriv_of_subset` + the box corollary over `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` (all compiled in evidence), and ship in the MvPolynomial Taylor PR. Locally keep the current lemma until `Roth.box` is replaced; the only caller is `eval_eq_sum_box` (Roth/Taylor.lean:220), which needs no change beyond the box spelling.

## Evidence
- WebSearch ×3 (queries in literature table rows 1–3); Lean-Finder, LeanSearch, Loogle (`MvPolynomial.X _ - MvPolynomial.C _`); grep over `.lake/packages/mathlib/Mathlib/` (no `eq_sum_box`, `eq_sum_hasseDeriv`, `MvPolynomial.sum_taylor`, no `taylor` in MvPolynomial dirs) and `.mathlib-quality/references/clean.tex` (l.501–528).
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.eq_sum_box_hasseDeriv/variants.lean` (checked with `lean_diagnostic_messages`: no errors, `success: true`; only the expected `#check_failure` info messages):
  (1) `#check_failure` of `X j - C (α j)` over `[CommSemiring R]`: fails to synthesize `HSub`, so CommRing is needed;
  (2) `Evidence.sum_taylor_eq`: hypothesis-free support-sum form, arbitrary `σ`, compiles;
  (3) `Evidence.eq_sum_hasseDeriv_of_subset`: any superset of the support, compiles;
  (4) `Evidence.eq_sum_Iic_hasseDeriv`: box form over `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`, compiles;
  (5) original project statement (with `Roth.box`) recovered from (4) in 3 lines;
  (6) counterexample (`P = X 0`, `r = 0`, `σ = Fin 1`, `A = ℤ`): `hP` cannot be dropped from the box form.
- Parent reports consulted: `MvPolynomial.coeff_taylor.md`, `MvPolynomial.taylor.md`, `MvPolynomial.taylor_neg_taylor.md`, `MvPolynomial.hasseDeriv.md`, `MvPolynomial.hasseDeriv_eq_zero_of_degreeOf_lt.md`, `Roth.box.md`, `Roth.mem_box.md`.
