---
decl: MvPolynomial.eval_eq_sum_box
file: Roth/Taylor.lean
line: 217
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Evaluated multivariate Taylor formula P(x) = sum (Δ_d P)(α) (x - α)^d is standard and absent from mathlib (no MvPolynomial.taylor, no univariate evaluated-sum form either), but the box form is a corollary of the verified CommSemiring hypothesis-free form eval (y + α) P = sum over supp(taylor α P) of (Δ_d P)(α) y^d plus a superset-s version, all compiled in evidence.
action: Ship in the MvPolynomial Taylor PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) as eval_add_eq_sum_of_subset (CommSemiring, arbitrary σ) with the ring x - α form and the Finset.Iic box form as corollaries (evidence items 2-4); locally keep (one caller Roth/Main.lean:390, unchanged except the box spelling when Roth.box is replaced).
---

# MvPolynomial.eval_eq_sum_box

## Inventory entry

### `theorem MvPolynomial.eval_eq_sum_box`
- **Type**: `{σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) : eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j`
- **What**: Taylor's theorem in evaluated form: if `deg_{X_j} P ≤ r_j` for all `j`, then for every point `x`, `P(x) = Σ_{d ≤ r} (Δ_d P)(α) ∏_j (x_j − α_j)^{d_j}`.
- **How**: one line, `simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)`: evaluates the polynomial identity `MvPolynomial.eq_sum_box_hasseDeriv` at `x`; `simp` pushes `eval` through `map_sum`, `map_mul`, `map_prod`, `map_pow`, `map_sub`, `eval_C`, `eval_X`.
- **Hypotheses**: `[CommRing A]` (subtraction `x j - α j`), `[Fintype σ]` (`∏ j`, `Roth.box`), `[DecidableEq σ]` (`Roth.box`), `hP` (degree box contains all nonzero Taylor coefficients).
- **Uses from project**: `MvPolynomial.eq_sum_box_hasseDeriv`, `MvPolynomial.hasseDeriv`, `Roth.box`
- **Used by**: Roth/Main.lean:390 (`abs_eval_lt_of_le_index`, `rw [eval_eq_sum_box (fun _ ↦ α) (fun j ↦ (h j : ℝ) / q j) r Q hd]`). Also named in the module docstring Roth/Taylor.lean:26. No other uses (`grep -rn eval_eq_sum_box Roth/`).
- **Visibility**: public
- **Lines**: 215–220 (docstring 215–216), proof length 1 line
- **Notes**: listed under `## Main results` of Roth/Taylor.lean; formalises the expansion used in the source paper §7 (clean.tex l.1658).

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/Main.lean:390), as a `rw` rule turning `eval x Q` into the Taylor sum which is then bounded termwise.
- Wrapper of 1–2 mathlib calls? It is `congrArg (eval x)` of a project lemma plus `simp`; not a mathlib wrapper (the parent is not in mathlib). As a named rewrite it saves the `simpa` at the caller.
- Does mathlib have it? No (Phase 5): there is no `MvPolynomial.taylor`, and even for one variable mathlib has only `Polynomial.taylor_eval` (`(taylor r f).eval s = f.eval (s + r)`) and `Polynomial.sum_taylor_eq`, not an evaluated Hasse-derivative sum.
- Too specific (inline?)? It could be inlined at its single caller, but it is the paper's named statement and a natural API companion of the polynomial form; keeping it is reasonable.
- Well-chosen? Stated against `Roth.box`, which its report says to REPLACE with `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`; evidence item 4 states it over `Finset.Iic`.

Conclusion: `KEEP`. Action: none locally beyond following the `Roth.box` REPLACE.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name does not end `_aux`; docstring does not start internal/auxiliary; Step 8 said KEEP; `grep -rn "eval_eq_sum_box" .lake/packages/mathlib/Mathlib/` has no hits. Not a glue lemma in the brief's sense (not `rfl` / `Iff.rfl` / pure unfolding: it applies `eval` and simplifies, and it is a separately named main result), so the full workflow was run, reusing the parent's literature and mathlib search where the concept is the same and adding evaluated-form searches.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.Taylor` elaborates, `success: true`)
- decl `MvPolynomial.eval_eq_sum_box`: ✓ resolved at Roth/Taylor.lean:217
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: the translation `P ↦ P(X + α)`, its coefficients as Hasse derivatives, and Taylor's expansion over a box.

### Statement (Phase 1)

`MvPolynomial.eval_eq_sum_box` is a theorem stating the following:

Let `A` be a commutative ring, `σ` a finite set of variables, `α, x ∈ A^σ` and `r ∈ ℕ^σ`. If `P ∈ A[X_σ]` has degree at most `r_j` in each `X_j`, then
`P(x) = Σ_{0 ≤ d ≤ r} (Δ_d P)(α) · ∏_j (x_j − α_j)^{d_j}`,
where `Δ_d` is the multi-index Hasse derivative. This is Taylor's formula evaluated at a point: the value of `P` at `x` is the finite Taylor sum about `α`.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]`, `[DecidableEq σ]` — finite variable set
- `A : Type*`, `[CommRing A]` — coefficient ring
- `α : σ → A` — expansion point; `x : σ → A` — evaluation point
- `r : σ → ℕ` — per-variable degree bound
- `P : MvPolynomial σ A`

Hypotheses (Lean side):
- `hP : ∀ j, degreeOf j P ≤ r j` — every nonzero Taylor coefficient lies in the box

Conclusion (math): `P(x) = Σ_{d ≤ r} (Δ_d P)(α) (x − α)^d`.

Conclusion (Lean): `eval x P = ∑ d ∈ Roth.box r, eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j`

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of Roth/Taylor.lean (evaluated form of the named Taylor theorem); mathematically a corollary of `eq_sum_box_hasseDeriv`.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 (theorem)
One-liner verdict: n/a (kind is theorem/lemma, not def)

Conclusion: MULTI-LINE (theorem; check skipped). Note: the proof is a one-line corollary of the parent; this is weighed in Phase 6/7.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | evaluate multivariate polynomial at point x equals sum Hasse derivatives at alpha times product (x_j - alpha_j)^{i_j} Taylor formula | yes | `P(x) = Σ_i D^i P(p) ∏ (x_j − p_j)^{i_j}`, sum over all multi-indices; `D^i F` = coefficient of `Z^i` in `F(X+Z)`; valid over any commutative ring `A` | arXiv 1310.6482, 1412.5012, 1402.0643, 1509.00279, 2111.07572, 2205.00342 |
| 2 | WebSearch (general form) | Hasse derivative multivariate polynomial f(a+b) = sum_i f^{(i)}(a) b^i commutative ring | yes | `f(a + b) = Σ_e (∂_e f)(a) b^e` (additive, no subtraction); univariate form stated as Prop. 2.2 of arXiv 2511.21241 over a commutative ring | arXiv 2205.00342 Def 3.4, 1303.0084, 1810.08075 (Hasse–Schmidt survey), 2511.21241 |
| 3 | WebSearch (named-after / aliases) | Roth's theorem proof Taylor expansion Q(h_1/q_1,...,h_m/q_m) index derivatives bound upper estimate | yes | the evaluated box form `Q(h/q) = Σ_{i ≤ r} Δ_i Q(α) ∏ (h_j/q_j − α)^{i_j}` used to bound `Q` at the rational point termwise | arXiv math/0307203 (quantitative Roth–Ridout), 2111.12409, 1806.10737, Siegel outline (ecroot.math.gatech.edu/siegel.pdf), Lang Ch. 7 §3 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Taylor / `h_1/q_1` | yes | l.1658: `Q(h_1/q_1,…,h_m/q_m) = Σ_{i_1=0}^{r_1}…Σ_{i_m=0}^{r_m} Δ_i Q(α,…,α) ∏ (h_j/q_j − α)^{i_j}`; l.502–507 the polynomial-form theorem | exactly the project statement, specialised at the call site to `α_j = α`, `x_j = h_j/q_j` |
| 6 | nLab | Hasse-Schmidt derivation / Taylor expansion | partial | Hasse–Schmidt derivations as coefficients of `f ↦ f(x+t)` | no entry for the evaluated polynomial identity; consistent with #2 |
| 7 | nCatLab | — | n/a | — | not a categorical concept (an evaluation identity in a commutative ring) |
| 8 | Stacks Project | — | n/a | — | elementary polynomial algebra; Stacks has principal parts but no tag for the concrete Taylor evaluation formula |
| 9 | MathOverflow / Math.SE | (via #1–#3) | partial | same `f(a + b) = Σ D^i f(a) b^i` | no dedicated thread surfaced; usage consistent with #1–#2 |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2205.00342 (2022), 2111.07572 (2021), 2111.12409 (2021), 2511.21241 (2025) | general form: sum over the support / all multi-indices, no box hypothesis; additive form `f(a+b)` over commutative rings |

### Literature summary (Phase 3)

Concept identified as: Taylor's formula for multivariate polynomials, evaluated at a point (Hasse-derivative form).
Sources agree on the standard form: yes. Coding-theory and Hasse–Schmidt sources write either `f(a + b) = Σ_e (∂_e f)(a) b^e` (additive) or `P(x) = Σ_i (D^i P)(a)(x − a)^i`, summing over all multi-indices (finitely many nonzero), over any commutative ring. Diophantine-approximation sources (Roth, Schmidt, Lang, the project paper l.1658) use the box `i ≤ r` form under a degree hypothesis.
Most general standard form: for `R` a commutative semiring, any variable set, `P(α + y) = Σ_e (Δ_e P)(α) y^e`, sum over the support of the translate (or any finite superset); with subtraction available, substituting `y = x − α` gives `P(x) = Σ (Δ_e P)(α)(x − α)^e`.
Generality dimensions where the literature varies:
  - index set: support (no hypothesis) vs. box with degree hypothesis; the box is a specialisation.
  - coefficient ring: commutative semiring (additive form) vs. commutative ring (`x − α` form); ours is `CommRing`.
  - number of variables: finite vs. arbitrary (`Finsupp.prod`).
Disagreement with the literature: none mathematically; the Lean form is the narrower box/ring specialisation.

### Generality analysis — `MvPolynomial.eval_eq_sum_box`

Literature-standard form (from Phase 3): `eval (α + y) P = Σ_{d ∈ s} (Δ_d P)(α) ∏ y_j^{d_j}` for any finite `s ⊇ supp(taylor α P)`, over a commutative semiring, any `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing A]` | commutative ring | commutative semiring (additive form `eval (y + α) P`) | yes (in the additive restatement) | evidence items 1–2 compile over `[CommSemiring R]`; the `x − α` spelling itself needs `Sub` (parent evidence item 1) |
| 2 | `[Fintype σ]` | finite variables | arbitrary `σ` | yes | items 1–3 use `d.prod fun j n ↦ …` and compile for arbitrary `σ` |
| 3 | `[DecidableEq σ]` | for `Roth.box` | not needed | yes | items 1–3 have no `DecidableEq σ` |
| 4 | `hP` | degree box | none (support) or `(taylor α P).support ⊆ s` | yes | item 1 has no hypothesis; items 2–3 take `hs`; item 7 shows `hP` is necessary in the box form (counterexample `P = X 0`, `r = 0`, `x = 1`, `α = 0`) |
| 5 | `Roth.box r` | project finset | `Finset.Iic (Finsupp.equivFunOnFinite.symm r)` | yes (re-aim) | Roth.box report: REPLACE; item 4 compiles over `Finset.Iic`, item 5 recovers the original |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 5 (CommRing to CommSemiring in additive form; drop `Fintype σ`; drop `DecidableEq σ`; replace `hP` by a support-containment hypothesis or nothing; `Roth.box` to `Finset.Iic`) — all verified by `lean_diagnostic_messages` on the evidence file (`success: true`, no errors).
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem MvPolynomial.eval_add_eq_sum_of_subset {σ R : Type*} [CommSemiring R] (α y : σ → R)
    (P : MvPolynomial σ R) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    eval (fun j ↦ y j + α j) P = ∑ d ∈ s, eval α (hasseDeriv d P) * d.prod fun j n ↦ y j ^ n
theorem MvPolynomial.eval_eq_sum_of_subset {σ A : Type*} [CommRing A] (α x : σ → A)
    (P : MvPolynomial σ A) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    eval x P = ∑ d ∈ s, eval α (hasseDeriv d P) * d.prod fun j n ↦ (x j - α j) ^ n
theorem MvPolynomial.eval_eq_sum_Iic [Fintype σ] [DecidableEq σ] (α x : σ → A) (r : σ → ℕ)
    (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r),
      eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j
```

Cost of restatement: CHEAP (each proved in 1–8 lines in the evidence file; the original follows in 3 lines).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|----------|----------|------------------------|----------------------------------|
|  1 | preambles to typeclasses? | no | — | `hP` is a data-dependent degree condition |
|  2 | sequences to filters? | no | — | purely algebraic |
|  3 | construction vs universal property? | no | — | evaluation identity |
|  4 | set-with-predicate to bundled substructure? | partial | box = order interval `Finset.Iic` in `σ →₀ ℕ` | `Finset.mem_Iic`, `Finsupp.card_Iic` (the caller bounds the number of terms by `∏ (r j + 1)`) |
|  5 | field-specific to semiring? | yes | additive form over `CommSemiring` (`eval (y + α) P`), matching mathlib's `Polynomial.taylor_eval` (`f.eval (s + r)`) | applies over `ℕ` and other semirings; same shape as `Polynomial.taylor_eval` |
|  6 | higher-categorical? | no | — | — |
|  7 | concrete index to general? | yes | `Fintype σ` + `∏ j` to arbitrary `σ` + `Finsupp.prod` | matches `MvPolynomial.eval_eq` conventions |
|  8 | concrete-via-abstract? | no | the box appears only to restrict the sum, which is the subset abstraction already counted in 4b | — |
|  9 | false-generalisation guard | no false generalisation | items 1–4 are the same identity (item 3 is item 2 at `y = x − α`); item 5 recovers the original verbatim | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: additive `eval_add_eq_sum_of_subset` over `CommSemiring` (shape of `Polynomial.taylor_eval` + `eval_eq`), with the `x − α` and `Finset.Iic` forms as corollaries (see 4b).
  - Cost: CHEAP
  - Mathlib downstream this enables: same normal form as the univariate `taylor_eval`/`sum_taylor_eq`; the box corollary uses mathlib's `LocallyFiniteOrder (σ →₀ ℕ)` API instead of `Roth.box`.
  - Real mathematical improvement: removes `Fintype`, `DecidableEq`, `hP` and the ring assumption from the core identity.

### Proof strategy — `MvPolynomial.eval_eq_sum_box`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|------------------------|----------------|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | helper lemmas mathlib SHOULD have | yes | `MvPolynomial.eval_taylor` (project, slated as `aeval_taylor`) + `eval_eq` + `coeff_taylor` give the support form in 2 lines (item 1) without going through the polynomial identity or `taylor_neg_taylor` | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove the semiring support form from `eval_taylor`, `eval_eq`, `coeff_taylor` (item 1), extend to supersets by `Finset.sum_subset` (item 2), specialise `y = x − α` (item 3), and get the box by `support ⊆ Iic r` from `hasseDeriv_eq_zero_of_degreeOf_lt` (item 4). This avoids needing a ring for the core and matches the univariate `taylor_eval` route.
  - Cost: CHEAP
  - Missing mathlib API (if any): none beyond the MvPolynomial Taylor/HasseDeriv PRs.
  - Would refactoring make the proof strictly shorter / cleaner? the current 1-line proof is already short; the refactor makes the *core* statement more general, not shorter.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.eval_eq_sum_box`

[A] Lean-Finder       "evaluation of multivariate polynomial at x equals sum over multi-indices of Hasse derivative evaluated at a times product of (x i - a i)^(d i)"   only univariate `Polynomial.hasseDeriv_apply`, `Polynomial.hasseDeriv`, `Polynomial.hasseDeriv_mul`, `Polynomial.taylor_coeff`, `Polynomial.aeval_sumIDeriv_eq_eval`; no evaluated Taylor sum
[B] Loogle            `MvPolynomial.eval _ _ = ∑ _ ∈ _, _ * ∏ _, (_ - _) ^ _`   no hits
[C] LeanSearch        "MvPolynomial eval x P equals sum of eval a (derivative) times product (x i - a i) ^ d i Taylor"   `MvPolynomial.eval₂_eq`, `eval_eq`, `eval_eq'` (expansion at 0 only), `Polynomial.derivative_eval`, `Polynomial.deriv_aeval`
[D] Grep mathlib src  `eval_eq_sum_box`, `hasseDeriv` together with `eval`, files mentioning both `MvPolynomial` and `taylor`/`hasseDeriv`   no `MvPolynomial` Taylor API; only univariate `Polynomial.taylor_coeff`, `taylor_eval`, `taylor_eval_sub`, `sum_taylor_eq` (Mathlib/Algebra/Polynomial/Taylor.lean:68,160,204,208)
[E] Name pattern      `MvPolynomial.eval_eq_sum_box`, `MvPolynomial.taylor`, `MvPolynomial.eval_add_eq_sum` (grep + parent reports `eq_sum_box_hasseDeriv`, `eval_taylor`, `taylor`)   no hits

Searched for both:
  - the user's current form (evaluated box sum with `(x j - α j)`)
  - the literature-standard form (additive semiring form `eval (y + α) P = Σ (Δ_d P)(α) y^d`, support sum)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); mathlib has only the univariate `Polynomial.taylor_eval` (evaluation of the translate) and `sum_taylor_eq` (polynomial form), and no evaluated Hasse-derivative sum even for one variable.

### Normal-form check — `MvPolynomial.eval_eq_sum_box`

Equivalent formalisms this statement could take: (i) current, `eval x P = Σ_box …`; (ii) `eval x` applied to the polynomial identity (`eq_sum_box_hasseDeriv`); (iii) additive `eval (y + α) P = Σ …y^d`; (iv) `eval y (taylor α P) = eval (y + α) P` (project `eval_taylor`) combined with `eval_eq`.
Does mathlib already have a canonical form for this idea? For one variable, the canonical pieces are `Polynomial.taylor_eval` (`(taylor r f).eval s = f.eval (s + r)`) and `taylor_coeff`; no evaluated-sum lemma.
Our statement is not stated against a mathlib canonical form (none exists); we propose (iii) as the core, keeping `eval x P = …` on the LHS so it works as a left-to-right `rw` rule like `MvPolynomial.eval_eq`.
RHS convention respected? yes (matches `MvPolynomial.eval_eq : eval X f = ∑ …`, which unfolds `eval` into a sum on the RHS).

### Syntactic generality — `MvPolynomial.eval_eq_sum_box`

Alternative restatements attempted:
- (a) support sum, semiring additive form (evidence item 1)
- (b) arbitrary superset `s`, semiring additive form (item 2)
- (c) arbitrary superset `s`, ring `x − α` form (item 3)
- (d) box over `Finset.Iic` with `hP` (item 4)
- (e) current, over `Roth.box`
Chosen restatement: (b) as the core, (c) and (d) as corollaries.
Justification: (b) applies with any convenient index finset and only needs a support containment; (d) is exactly what the caller at Roth/Main.lean:390 rewrites with.

### Superfluous-argument audit — `MvPolynomial.eval_eq_sum_box`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing A]` | only for the `x − α` spelling | additive form holds over `CommSemiring` (items 1–2) |
| 2 | `[Fintype σ]` | no (for the identity) | only for `∏ j`; `Finsupp.prod` works for any `σ` |
| 3 | `[DecidableEq σ]` | no (for the identity) | only for the box finset |
| 4 | `hP` | only in the box form | necessary there (item 7); absent from the core |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (LHS `eval x P`, like `MvPolynomial.eval_eq`); core should be the additive form (iii)
Syntactic generality: RESTATE (superset-`s` core; box over `Finset.Iic`)
Superfluous arguments: 3 to drop from the core (`Fintype σ`, `DecidableEq σ`, `hP`), and `CommRing` to `CommSemiring` in the additive form

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.eval_eq_sum_box`

Internal use count: 1 (not counting the declaring file; inside it only the module docstring mention at l.26)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:390 | `rw [eval_eq_sum_box (fun _ ↦ α) (fun j ↦ (h j : ℝ) / q j) r Q hd]` (in `abs_eval_lt_of_le_index`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `eval_eq_sum_box`?):
  - (none) — `grep -rn "congrArg (eval\|eq_sum_box_hasseDeriv" Roth/` finds only Roth/Taylor.lean:220.

### Composition check (Phase 6)

Can `MvPolynomial.eval_eq_sum_box` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib only
  - Mathlib decls used: `MvPolynomial.eval_eq`, `Polynomial.taylor_eval` (univariate)
  - Result: fails — mathlib has no `MvPolynomial.taylor` / multivariate `hasseDeriv`, so the coefficients `(Δ_d P)(α)` cannot even be named.

Attempt 2: from the parent `eq_sum_box_hasseDeriv` (project)
  - `simpa using congrArg (eval x) (eq_sum_box_hasseDeriv α r P hP)` (evidence item 6)
  - Result: succeeds in one line, but uses a project (non-mathlib) lemma; once the Taylor PR lands this is a one-line corollary there.

Conclusion: NOT-COMPOSABLE (from mathlib); a one-line corollary of the proposed Taylor-PR API.

## Verdict: `MvPolynomial.eval_eq_sum_box`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the evaluated Taylor formula `P(α + y) = Σ (Δ_d P)(α) y^d` / `P(x) = Σ (Δ_d P)(α)(x − α)^d` is standard over commutative rings (arXiv 1402.0643, 2205.00342, 2511.21241; Roth-method sources math/0307203, 2111.12409; project paper l.1658).
- Generality analysis (Phase 4): STRICTLY NARROWER — `Fintype`, `DecidableEq`, `hP`, `Roth.box` removable/replaceable and `CommRing` weakenable to `CommSemiring` in the additive form, all verified (evidence items 1–5 compile).
- Mathlib search (Phase 5): not in mathlib; not even the univariate evaluated-sum form.
- Composition check (Phase 6): NOT-COMPOSABLE from mathlib.

**Rationale:**

Mathlib has Taylor for one variable only: `Polynomial.taylor_eval` evaluates the translate, and `Polynomial.sum_taylor_eq` gives the polynomial expansion. It has nothing for `MvPolynomial`. The evaluated multivariate formula is how Taylor's theorem is actually used in Roth/Schmidt-type arguments, where `Q` at a rational point is bounded term by term (the only caller, Roth/Main.lean:390, does exactly this), and in multiplicity-code arguments. It belongs in the planned `MvPolynomial.taylor` PR, next to the polynomial form `eq_sum_box_hasseDeriv` (YES-but-generalise-first) and `eval_taylor` (YES-but-generalise-first).

As stated, it is the paper's box/ring specialisation. The content holds over any commutative semiring in the additive form `eval (y + α) P = Σ_{d ∈ s} (Δ_d P)(α) y^d`, for any `s` containing the support of the translate, with no finiteness, decidability or degree hypotheses. The evidence file proves that in 2 lines from `eval_taylor`, `eval_eq` and `coeff_taylor`. The ring `x − α` form and the `Finset.Iic` box form follow, and the original statement is recovered verbatim. The proof is only one line, since it is a corollary of the polynomial form. Even so, it deserves to ship as a named lemma: evaluated Taylor sums are what downstream users rewrite with, the semiring additive form is not a corollary of the ring-only polynomial identity, and the same split exists for one variable (`taylor_eval` alongside `sum_taylor_eq`).

Reason for the generalisation: LITERATURE-WEAKENING (support/superset sum with no hypotheses, arbitrary `σ`, additive form over `CommSemiring`) and MODERN-IDIOM (`Finset.Iic` instead of `Roth.box`; `Polynomial.taylor_eval`-style additive normal form).
Proposed restatement:
```lean
theorem MvPolynomial.eval_add_eq_sum_of_subset {σ R : Type*} [CommSemiring R] (α y : σ → R)
    (P : MvPolynomial σ R) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    eval (fun j ↦ y j + α j) P = ∑ d ∈ s, eval α (hasseDeriv d P) * d.prod fun j n ↦ y j ^ n := by
  sorry  -- proved in evidence item 2

theorem MvPolynomial.eval_eq_sum_of_subset {σ A : Type*} [CommRing A] (α x : σ → A)
    (P : MvPolynomial σ A) (s : Finset (σ →₀ ℕ)) (hs : (taylor α P).support ⊆ s) :
    eval x P = ∑ d ∈ s, eval α (hasseDeriv d P) * d.prod fun j n ↦ (x j - α j) ^ n := by
  sorry  -- proved in evidence item 3

theorem MvPolynomial.eval_eq_sum_Iic {σ A : Type*} [CommRing A] [Fintype σ] [DecidableEq σ]
    (α x : σ → A) (r : σ → ℕ) (P : MvPolynomial σ A) (hP : ∀ j, degreeOf j P ≤ r j) :
    eval x P = ∑ d ∈ Finset.Iic (Finsupp.equivFunOnFinite.symm r),
      eval α (hasseDeriv d P) * ∏ j, (x j - α j) ^ d j := by
  sorry  -- proved in evidence item 4
```
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- the multivariate counterpart of `Polynomial.taylor_eval` + `Polynomial.taylor_coeff` in a single rewrite rule, usable over semirings (e.g. `ℕ`);
- the box corollary uses `Finset.mem_Iic` / `Finsupp.card_Iic`, so callers bound the number of terms by `∏ (r j + 1)` with mathlib API instead of `Roth.card_box`;
- termwise estimates of `P(x)` in Diophantine approximation and the method of multiplicities without degree bookkeeping.
Proposed mathlib location: `Mathlib/Algebra/MvPolynomial/Taylor.lean` (new; with `MvPolynomial.taylor`, `coeff_taylor`, `aeval_taylor`/`eval_taylor`, `sum_taylor_eq`)
PR grouping: Taylor PR, together with `eq_sum_box_hasseDeriv` (as `sum_taylor_eq` / `eq_sum_hasseDeriv_of_subset`) and `eval_taylor`.
Next action: run `/generalise MvPolynomial.eval_eq_sum_box` to adopt the three-lemma layout above (and switch `Roth.box` to `Finset.Iic` per the Roth.box report), then `/cleanup Roth/Taylor.lean` before the PR.

## Next step

Restate as `eval_add_eq_sum_of_subset` (CommSemiring core) + `eval_eq_sum_of_subset` + `eval_eq_sum_Iic` (all compiled in evidence) and ship in the MvPolynomial Taylor PR. Locally keep the current lemma; its only caller (Roth/Main.lean:390) needs no change beyond the box spelling once `Roth.box` is replaced.

## Evidence
- WebSearch ×3 (queries in literature table rows 1–3); Lean-Finder, LeanSearch, Loogle (`MvPolynomial.eval _ _ = ∑ _ ∈ _, _ * ∏ _, (_ - _) ^ _`, no hits); grep over `.lake/packages/mathlib/Mathlib/` (no `eval_eq_sum_box`; `hasseDeriv`+`eval` only in univariate Polynomial/Taylor.lean; no MvPolynomial taylor/hasseDeriv) and `.mathlib-quality/references/clean.tex` (l.502–507, l.1658).
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.eval_eq_sum_box/variants.lean`, checked with `lean_diagnostic_messages`: `success: true`, no diagnostics (the first run failed on item 1 for want of `Finsupp.prod` in the `simp` set; fixed and rechecked):
  (1) `Evidence.eval_add_eq_sum_support`: `CommSemiring`, arbitrary `σ`, no hypotheses, support sum;
  (2) `Evidence.eval_add_eq_sum_of_subset`: any superset of the support;
  (3) `Evidence.eval_eq_sum_of_subset`: ring `x − α` form from (2);
  (4) `Evidence.eval_eq_sum_Iic`: box over `Finset.Iic (Finsupp.equivFunOnFinite.symm r)`;
  (5) original statement (over `Roth.box`) recovered from (4);
  (6) original as the one-line `congrArg (eval x)` corollary of `eq_sum_box_hasseDeriv`;
  (7) counterexample (`σ = Fin 1`, `A = ℤ`, `P = X 0`, `r = 0`, `x = 1`, `α = 0`): `hP` cannot be dropped from the box form.
- Parent reports consulted: `MvPolynomial.eq_sum_box_hasseDeriv.md`, `MvPolynomial.eval_taylor.md`, `Roth.box.md`.
