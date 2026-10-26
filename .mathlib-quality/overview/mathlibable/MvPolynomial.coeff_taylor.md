---
decl: MvPolynomial.coeff_taylor
file: Roth/Taylor.lean
line: 134
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Multivariate Taylor theorem in coefficient form, coeff_d P(X + α) = (Δ_d P)(α), is the standard defining property of multi-index Hasse derivatives and is absent from mathlib (only univariate Polynomial.taylor_coeff); the statement is maximally general but must ship stated against the generalised MvPolynomial.hasseDeriv (Finsupp.choose coefficient), so it inherits the parent's restate-first requirement.
action: Upstream with MvPolynomial.taylor and MvPolynomial.hasseDeriv in a new Mathlib/Algebra/MvPolynomial/Taylor.lean (statement unchanged, proof re-run after hasseCoeff becomes Finsupp.choose), promoting private helper coeff_aeval_X_mul to a public lemma; locally keep as is (used in Roth/Index.lean:64,153,158 and Roth/Taylor.lean:173,202).
---

# MvPolynomial.coeff_taylor

## Inventory entry

### `theorem MvPolynomial.coeff_taylor`
- **Type**: `{σ R : Type*} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ) (P : MvPolynomial σ R) : (taylor α P).coeff d = eval α (hasseDeriv d P)`
- **What**: Taylor's theorem for multivariate polynomials, coefficient form: the coefficient of `X^d` in the translate `P(X + α)` is the value at `α` of the `d`-th Hasse derivative `Δ_d P`.
- **How**: `MvPolynomial.induction_on'`; the `add` case is `simp` with linearity; the `monomial` case is the private `coeff_taylor_monomial_aux`, which runs `Finsupp.induction` on the exponent and, in the `single_add` step (`coeff_taylor_monomial_single_add_aux`), splits `(X i + C (α i))^n` as `Polynomial.aeval (X i)` of a univariate binomial, using the private `coeff_aeval_X_mul`, mathlib's `Polynomial.coeff_X_add_C_pow`, `hasseDeriv_monomial`, the private `hasseCoeff_single_add_eq` and `prod_pow_single_add_tsub`.
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv`, private `coeff_taylor_monomial_aux` (which uses private `coeff_taylor_monomial_single_add_aux`, `coeff_aeval_X_mul`, `hasseCoeff_single_add_eq`, `prod_pow_single_add_tsub`, and public `taylor_X`, `hasseDeriv_monomial`, `hasseDeriv_C`, `hasseCoeff`, `hasseCoeff_eq_zero_iff`)
- **Used by**: Roth/Taylor.lean:173 (`degreeOf_taylor_le`), Roth/Taylor.lean:202 (`eq_sum_box_hasseDeriv`), Roth/Index.lean:64 (private `mem_support_taylor_iff`), Roth/Index.lean:153 and :158 (`index_eq_weightedOrder_div`)
- **Visibility**: public
- **Lines**: 131–138 (docstring 131–133), proof length 4 lines (plus ~60 lines of private helpers at 63–128 dedicated to it)
- **Notes**: listed under `## Main results` of Roth/Taylor.lean; the private helpers exist only for this theorem.

## Junk check (Step 8)
- Used anywhere? Yes: 5 call sites in 2 files (Taylor.lean, Index.lean), including the definition-level characterisation of the index (`mem_support_taylor_iff`).
- Wrapper of 1–2 mathlib calls? No. It is a genuine theorem (per-variable binomial expansion plus coefficient bookkeeping); evidence file probe (3) shows `simp` with the unfolding lemmas does not close it.
- Does mathlib have it? No: only the univariate `Polynomial.taylor_coeff` (Mathlib/Algebra/Polynomial/Taylor.lean:68); there is no `MvPolynomial.taylor` nor `MvPolynomial.hasseDeriv` in mathlib.
- Too specific (inline?)? No; it is the central theorem of the file.
- Well-chosen definition? n/a (theorem); the statement is the exact multivariate analogue of mathlib's `taylor_coeff`.

Conclusion: `KEEP`. Action: none locally; upstream with the Taylor/HasseDeriv API.

## Mathlibable assessment (Step 9)

Pre-filter: not private, name does not end `_aux`, docstring does not start internal/auxiliary, Step 8 said KEEP, `MvPolynomial.coeff_taylor` does not exist in `.lake/packages/mathlib/Mathlib/` (grep for `coeff_taylor` finds only `Polynomial.coeff_taylor_natDegree` usage in RingTheory/Polynomial/DegreeLT.lean and analysis lemmas). Not a glue lemma (real proof with ~60 lines of helper content), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.Taylor` elaborates)
- decl `MvPolynomial.coeff_taylor`: ✓ resolved at Roth/Taylor.lean:134
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: the translation `P ↦ P(X + α)`, its coefficients as Hasse derivatives, and Taylor's expansion over a box.

### Statement (Phase 1)

`MvPolynomial.coeff_taylor` is a theorem stating the following:

Let `R` be a commutative semiring, `σ` any index set, `P ∈ R[X_σ]` and `α ∈ R^σ`. For every multi-index `d`, the coefficient of `X^d` in `P(X + α)` equals `(Δ_d P)(α)`, where `Δ_d` is the multi-index Hasse derivative `Δ_d X^k = binom(k, d) X^(k−d)`. Equivalently `P(X + α) = Σ_d (Δ_d P)(α) X^d`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the set of variables
- `R : Type*`, `[CommSemiring R]` — the coefficient semiring
- `α : σ → R` — the translation point
- `d : σ →₀ ℕ` — the multi-index
- `P : MvPolynomial σ R` — the polynomial

Hypotheses (Lean side):
- none

Conclusion (math): `[X^d] P(X + α) = (Δ_d P)(α)`.

Conclusion (Lean): `(taylor α P).coeff d = eval α (hasseDeriv d P)`

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of Roth/Taylor.lean; it is Taylor's theorem for polynomials in several variables (named result, project paper §4 Theorem).

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4 (theorem)
One-liner verdict: n/a (kind is theorem/lemma, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Taylor formula polynomial several variables coefficient of P(X+a) equals Hasse derivative evaluated at a | partial | univariate `P(a+b) = Σ_j P^[j](a) b^j`; multivariate analogue `Σ_α D^α P(a) (X−a)^α` mentioned | Wikipedia "Hasse derivative", ProofWiki "Taylor Expansion for Polynomials", arXiv 2511.21241, mathlib `taylor_coeff` docs; no multivariate formal source |
| 2 | WebSearch (general form) | Hasse derivative multivariate polynomial P(x+y) = sum_i (D^i P)(x) y^i any commutative ring | yes | over any commutative ring `R`, `D^e f` := coefficient of `z^e` in `f(x+z)`, with explicit formula `Σ_a binom(a,e) f_a x^(a−e)` | arXiv 2205.00342 (Def 3.4 / Prop 3.5): exactly our `coeff_taylor` combined with `hasseDeriv_apply`; arXiv 1303.0084 Def 5.1 (directional variant); arXiv 1810.08075 Hasse–Schmidt surveys |
| 3 | WebSearch (named-after / aliases) | "Hasse-Schmidt" Taylor expansion polynomial ring multiplicity method Dvir Kopparty Saraf Sudan | yes | Hasse derivative = coefficient of `z^i` in `P(x+z)`; vanishing to order m = no Taylor terms below degree m | arXiv 1909.03180 Def 7, arXiv 1402.3018 §6, ECCC 2021/163 (multiplicity Schwartz–Zippel); the standard DKSS framework |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for Taylor / P_α / Δ_d | yes | l.501–502 "Taylor's expansion for polynomials in several variables"; l.547–548 Lean note "Let `P_α(X)=P(X+α)`, whose coefficient at `d` is `(Δ_dP)(α)`" | project source paper; exactly our statement |
| 6 | nLab | Hasse-Schmidt derivation / Taylor expansion of polynomials | partial | Hasse–Schmidt derivations as the coefficients of the Taylor map `f ↦ f(x+t)` | no separate entry for the polynomial Taylor formula; consistent with #2 (same pages as in the hasseDeriv report) |
| 7 | nCatLab | — | n/a | — | not a categorical concept (a coefficient identity in a polynomial ring) |
| 8 | Stacks Project | — | n/a | — | elementary polynomial algebra; Stacks has differential operators / principal parts but no tag for the concrete polynomial Taylor coefficient formula |
| 9 | MathOverflow / Math.SE | (via #1–#3: multiplicity-method and Hasse-derivative threads) | partial | same `P(x+z) = Σ_i (D^i P)(x) z^i` | no dedicated thread surfaced; usage consistent |
| 10 | recent arXiv (last 5 years) | (results of #1–#3) | yes | arXiv 2511.21241 (2025), 2205.00342 (2022), ECCC 2021/163 | all use the coefficient-of-`P(x+z)` characterisation over commutative rings |

### Literature summary (Phase 3)

Concept identified as: Taylor's formula for (multivariate) polynomials with Hasse (divided) derivatives; in the coding-theory / polynomial-method literature it is often taken as the *definition* of the Hasse derivative (`D^e f` = coefficient of `z^e` in `f(x+z)`).
Sources agree on the standard form: yes.
Most general standard form: for any commutative ring (the proof works over commutative semirings) and any set of variables, `f(x + a) = Σ_e (D^e f)(a) x^e`, i.e. `[x^e] f(x+a) = (D^e f)(a)`.
Generality dimensions where the literature varies:
  - coefficient ring: field / finite field (coding theory) to commutative ring; ours is commutative semiring, the most general available for `MvPolynomial`.
  - point: `a ∈ R^n` (ours, as `σ → R`) vs `a` in an `R`-algebra `S` / the generic point `f(x+z)` in `R[x][z]`; the generic-point version is the identity `f(x+z) = Σ (D^e f)(x) z^e` in `R[x,z]`, of which ours is the specialisation `x ↦ a` (and conversely ours over `S = R[x]` gives the generic version). In Lean this would need `taylor` for `α : σ → S` with `S` an `R`-algebra; ours already covers it by taking `R := S` after `map`.
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.coeff_taylor`

Literature-standard form (from Phase 3): `[X^d] P(X + α) = (Δ_d P)(α)` for `P ∈ R[X_σ]`, `R` commutative (semi)ring, `α ∈ R^σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative ring | no (already weaker) | `MvPolynomial σ R` requires `CommSemiring R`; evidence probe (1): `#check_failure (MvPolynomial ℕ R)` with `[Semiring R]` fails to synthesize `CommSemiring R` |
| 2 | `σ : Type*` | arbitrary, universe-polymorphic | finite set of n variables | no (already more general) | evidence probe (2): instantiates at `σ : Type 3` |
| 3 | `α : σ → R` | arbitrary function | point of `R^n` | no | matches `MvPolynomial.eval`; the `R`-algebra-point variant reduces to this via `map (algebraMap R S)` together with `taylor_map` and `hasseDeriv_map` |
| 4 | `d : σ →₀ ℕ` | any multi-index | any multi-index | no | — |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only weakening candidate, `CommSemiring → Semiring`, verified impossible in the evidence file)
Proposed restatement (if STRICTLY NARROWER): n/a. The *statement* is unchanged; the only required change is inherited from the parent `MvPolynomial.hasseDeriv` (YES-but-generalise-first): its coefficient `hasseCoeff d k` should become the multi-index binomial `k.choose d` (`Finsupp.choose`), which changes the private helper `hasseCoeff_single_add_eq` but not this theorem's statement.

Cost of restatement: CHEAP (statement untouched; the proof's `hasseCoeff` helpers are re-proved once `Finsupp.choose` exists)

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|----------|----------|------------------------|----------------------------------|
|  1 | preambles to typeclasses? | no | — | no hypotheses |
|  2 | sequences to filters? | no | — | purely algebraic |
|  3 | construction vs universal property? | no | the theorem is the characterising property; a uniqueness form ("`Δ_d` is the unique family with `P(X+α) = Σ (Δ_d P)(α) X^d`") is not used in mathlib's univariate file either | — |
|  4 | set-with-predicate to bundled substructure? | no | — | — |
|  5 | field-specific to semiring? | no | already `CommSemiring` | — |
|  6 | higher-categorical? | no | concrete coefficient identity | — |
|  7 | concrete index to general? | no | `σ` arbitrary | — |
|  8 | concrete-via-abstract? | no | the proof is about `taylor` and `hasseDeriv` throughout (both reappear in the monomial step after `induction_on'`); no concrete witness to abstract | — |
|  9 | false-generalisation guard | no false generalisation | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: the statement is already the exact multivariate analogue of mathlib's `Polynomial.taylor_coeff : (taylor r f).coeff n = (hasseDeriv n f).eval r`, with the same LHS/RHS orientation. An optional companion `taylor_eq_sum : taylor α P = ∑ d ∈ ..., monomial d (eval α (hasseDeriv d P))` (cf. project's `eq_sum_box_hasseDeriv`) is an addition, not a restatement.

### Proof strategy — `MvPolynomial.coeff_taylor`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|------------------------|----------------|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | helper lemmas mathlib SHOULD have | yes | (a) `coeff_aeval_X_mul`: coefficient of `Polynomial.aeval (X i) f * B` when no monomial of `B` involves `X i` — a general "separated variable" coefficient lemma, natural in Mathlib/Algebra/MvPolynomial (cf. `MvPolynomial.optionEquivLeft`); (b) multi-index binomial `Finsupp.choose` with `(single i n + k').choose d = n.choose (d i) * k'.choose (d.erase i)` (replaces `hasseCoeff_single_add_eq`); (c) `prod_pow_single_add_tsub` is a `Finsupp.prod` bookkeeping lemma | ship (a), (b) with the PR; (c) can stay private |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (linearity reduction to monomials, then induction over the support with the one-variable binomial `Polynomial.coeff_X_add_C_pow` — the same strategy as mathlib's univariate `taylor_coeff`, lifted one variable at a time).
  - Missing mathlib API: `Finsupp.choose` (from the hasseCoeff report) and a public form of `coeff_aeval_X_mul`; with them the private helpers shrink but the overall shape is unchanged.
  - Would refactoring make the proof strictly shorter / cleaner? Marginally (helpers become reusable API); no strategy change recommended. An alternative via `MvPolynomial.optionEquivLeft` / `finSuccEquiv` (induct on the number of variables and apply univariate `Polynomial.taylor_coeff`) only works for finite `σ` and is not shorter.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.coeff_taylor`

[A] Lean-Finder       "Taylor coefficient of a multivariate polynomial translated by a point is a divided (Hasse) derivative evaluated at that point"   only univariate `Polynomial.taylor_coeff`, `taylor_coeff_one`, `hasseDeriv_apply`, `taylor_eval`, `taylor_apply`, `taylor_monomial`, `taylor_taylor`
[B] Loogle            `MvPolynomial.coeff _ ((MvPolynomial.aeval _) _)`   query error (loogle's index rejects `MvPolynomial.coeff` as a constant in this form); compensated by [D] grep and the parent report's Loogle on `(_ → _) → MvPolynomial _ _ →ₐ[_] MvPolynomial _ _` (only `rename`, `killCompl`, `bind₁`)
[C] LeanSearch        "coefficient of multivariate polynomial P(X + a) equals evaluation at a of Hasse derivative, Taylor formula several variables"   `Polynomial.taylor_coeff`, `Polynomial.taylor_coeff_one`, `Polynomial.hasseDeriv(_apply)`, `MvPowerSeries.coeff_subst` (general substitution, CommRing, finsum formula, not Hasse), `PowerSeries.coeff_subst`, `MvPolynomial.mkDerivation`
[D] Grep mathlib src  `coeff_taylor`, `taylor_coeff` (only Polynomial/Taylor.lean, Analysis/Calculus/Taylor.lean, uses in Henselian/IsIntegral/DegreeLT); files mentioning `hasseDeriv` (only Polynomial/HasseDeriv.lean, Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean); `MvPolynomial.taylor` (none)   no multivariate result
[E] Name pattern      `MvPolynomial.coeff_taylor`, `MvPolynomial.taylor`, `MvPolynomial.hasseDeriv` (via grep and parent reports)   no hits

Searched for both:
  - the user's current form (`coeff (taylor α P) d = eval α (hasseDeriv d P)`)
  - the literature-standard form (Hasse derivative as coefficient of `P(X+Z)`; general substitution coefficient formula `MvPowerSeries.coeff_subst`, which is a different, non-Hasse statement)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); only the univariate analogue `Polynomial.taylor_coeff` exists.

### Normal-form check — `MvPolynomial.coeff_taylor`

Equivalent formalisms this statement could take: (i) `(taylor α P).coeff d = eval α (hasseDeriv d P)` (current); (ii) `taylor α P = ∑ d ∈ S, monomial d (eval α (hasseDeriv d P))` (sum form); (iii) `coeff d (aeval (X + C α) P) = ...` without the named `taylor`.
Does mathlib already have a canonical form for this idea? For one variable yes: `Polynomial.taylor_coeff` in shape (i).
Our statement is stated in the canonical (i) shape with the computable side `eval α (hasseDeriv d P)` on the RHS, exactly as mathlib.
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.coeff_taylor`

Alternative restatements attempted:
- (i) coefficient form (current)
- (ii) sum form over a support/box (project has it as `eq_sum_box_hasseDeriv`, derived from (i))
- (iii) `aeval`-spelled LHS (rejected: loses the named API; `taylor_apply` converts)
Chosen restatement: (i).
Justification: it rewrites directly in `mem_support_iff` / `MvPowerSeries.coeff` goals (all 5 call sites rewrite with it), matches mathlib's univariate lemma, and (ii) follows from it.

### Superfluous-argument audit — `MvPolynomial.coeff_taylor`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed for `MvPolynomial σ R` to exist (evidence probe 1) |
| 2 | `α`, `d`, `P` | yes | appear in the conclusion |
| 3 | (no `DecidableEq σ`, no `Fintype σ`) | n/a | `classical` is used internally only; no superfluous instance arguments |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (statement); the `hasseDeriv` it mentions must first be restated per the parent report.

### Call sites — `MvPolynomial.coeff_taylor`

Internal use count: 3 (outside the declaring file; plus 2 in Roth/Taylor.lean)
External-to-file callers: 1 distinct file (Roth/Index.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Index.lean:64 | `rw [mem_support_iff, coeff_taylor]` (private `mem_support_taylor_iff`) |
| Roth/Index.lean:153 | `index_le_weight (by simpa [F, MvPolynomial.coeff_coe, coeff_taylor] using hd)` (`index_eq_weightedOrder_div`) |
| Roth/Index.lean:158 | `(by simpa [F, MvPolynomial.coeff_coe, coeff_taylor] using he)` (`index_eq_weightedOrder_div`) |
| Roth/Taylor.lean:173 | `simp [mem_support_iff, coeff_taylor, hasseDeriv_eq_zero_of_degreeOf_lt h] at he` (`degreeOf_taylor_le`) |
| Roth/Taylor.lean:202 | `simp only [coeff_taylor, coeff_sum, coeff_monomial, Finset.sum_ite_eq']` (`eq_sum_box_hasseDeriv`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `coeff_taylor`?):
  - (none) — `grep -rn "aeval (fun j ↦ X j + C" Roth/` finds only `taylor`, `taylor_apply`, `taylor_X`, `taylor_monomial` (API lemmas, not re-derivations).

### Composition check (Phase 6)

Can `MvPolynomial.coeff_taylor` be derived from mathlib in ≤3 chained calls?

Attempt 1: `simp [taylor_apply, hasseDeriv_apply, coeff_sum, coeff_monomial, aeval_def, eval₂_eq, map_sum]`
  - Mathlib decls used: `MvPolynomial.aeval_def`, `eval₂_eq`, `coeff_sum`, `coeff_monomial`, `map_sum`
  - Result: fails (evidence probe 3: `fail_if_success (simp [...]; done)` succeeds — simp leaves a goal)
  - Notes: the missing content is the multinomial expansion of `∏_j (X_j + α_j)^{k_j}`.

Attempt 2: transport from univariate `Polynomial.taylor_coeff` via `finSuccEquiv` / `optionEquivLeft`
  - Mathlib decls used: `Polynomial.taylor_coeff`, `MvPolynomial.finSuccEquiv`
  - Result: fails as a composition — requires an induction on the number of variables (finite `σ` only) plus compatibility of `hasseDeriv` with `finSuccEquiv`, which itself is new API.

Conclusion: NOT-COMPOSABLE

## Verdict: `MvPolynomial.coeff_taylor`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard Taylor formula / Hasse-derivative characterisation `[x^e] f(x+a) = (D^e f)(a)` over commutative rings (arXiv 2205.00342 Def 3.4/Prop 3.5, 1909.03180 Def 7, 2511.21241 Prop 2.2; project paper §4 l.501, l.547).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (CommSemiring weakening verified impossible, evidence probe 1); Phase 4c: no modern idiom.
- Mathlib search (Phase 5): not in mathlib; only univariate `Polynomial.taylor_coeff`.
- Composition check (Phase 6): NOT-COMPOSABLE (evidence probe 3).

**Rationale:**

The theorem is the multivariate Taylor formula, the central fact of the multivariate polynomial method with multiplicities (DKSS), of index arguments in Diophantine approximation (Roth, Thue–Siegel–Dyson), and of multiplicity codes; in that literature it is frequently taken as the definition of the Hasse derivative. Mathlib has the univariate version (`Polynomial.taylor_coeff`) but no multivariate Taylor shift and no multivariate Hasse derivative, so anyone needing "`P` vanishes to order `m` at `α`" for `MvPolynomial` currently has to re-derive this identity by hand. The project's statement is in exactly mathlib's univariate shape, at maximal generality (`CommSemiring`, arbitrary `σ`), with 5 genuine call sites, and is not a composition of mathlib lemmas.

The bucket is generalise-first, not add-as-is, solely because its RHS mentions `MvPolynomial.hasseDeriv`, whose assessed verdict is YES-but-generalise-first (coefficient to be spelled with the multi-index binomial `Finsupp.choose` rather than the project-local `hasseCoeff`). This theorem's own statement needs no change (Phase 4b MAXIMALLY GENERAL, Phase 5.5 SHIP-AS-STATED), but it cannot ship before the parent is restated, and its proof's `hasseCoeff_single_add_eq` helper must be re-proved for `Finsupp.choose`. Cost is CHEAP and does not affect the bucket.

Reason for the generalisation: inherited from parent `MvPolynomial.hasseDeriv` (LITERATURE-WEAKENING / normal-form of the coefficient as `Finsupp.choose`); this decl's own Phase 4b found no further weakening.
Proposed restatement:
```lean
theorem MvPolynomial.coeff_taylor {σ R : Type*} [CommSemiring R] (α : σ → R) (d : σ →₀ ℕ)
    (P : MvPolynomial σ R) : (taylor α P).coeff d = eval α (hasseDeriv d P) := by
  sorry  -- unchanged statement; `hasseDeriv` now defined with `(k.choose d : R)`;
         -- proof re-run with `Finsupp.choose` version of `hasseCoeff_single_add_eq`
```
Estimated cost of regeneralisation: CHEAP
Proposed mathlib location: `Mathlib/Algebra/MvPolynomial/Taylor.lean` (new; imports the new `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`)
PR grouping: ship with `MvPolynomial.taylor`, `taylor_X`, `taylor_C`, `taylor_monomial`, `eval_taylor`, `taylor_taylor`, `taylor_zero`, `taylor_map`, `taylor_rename`, `degreeOf_taylor_le`, `taylor_injective` (Taylor PR), after the `MvPolynomial.hasseDeriv` + `Finsupp.choose` PR; promote private `coeff_aeval_X_mul` to a public lemma in `Mathlib/Algebra/MvPolynomial/Variables.lean` or the Taylor file.
Next action: run `/generalise MvPolynomial.hasseDeriv` (parent) first; then re-check `coeff_taylor` compiles against the restated `hasseDeriv`, and `/cleanup Roth/Taylor.lean MvPolynomial.coeff_taylor` before the PR.

## Next step

Restate `MvPolynomial.hasseDeriv` with the `Finsupp.choose` coefficient (parent report), re-prove `coeff_taylor`'s private helpers against it (statement unchanged), and upstream `coeff_taylor` in the Taylor PR (new `Mathlib/Algebra/MvPolynomial/Taylor.lean`) with a public version of `coeff_aeval_X_mul`. Locally keep as is.

## Evidence
- WebSearch ×3 (queries in the literature table rows 1–3); Lean-Finder, LeanSearch, Loogle (errored on the `MvPolynomial.coeff` pattern, recorded), grep over `.lake/packages/mathlib/Mathlib/` and `.mathlib-quality/references/clean.tex`.
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.coeff_taylor/probes.lean` (checked with `lean_diagnostic_messages`: no errors; info messages only): (1) `#check_failure (MvPolynomial ℕ R)` with `[Semiring R]` fails to synthesize `CommSemiring R` (Semiring weakening impossible); (2) statement instantiated at `σ : Type 3`; (3) `fail_if_success (simp [taylor_apply, hasseDeriv_apply, coeff_sum, coeff_monomial, aeval_def, eval₂_eq, map_sum]; done)` succeeds, i.e. simp-composition does not close the goal; (4) `#check @Polynomial.taylor_coeff` confirms the univariate analogue over `Semiring`.
- Parent reports consulted: `MvPolynomial.taylor.md` (YES-add-as-is), `MvPolynomial.hasseDeriv.md` (YES-but-generalise-first), `MvPolynomial.coeff_hasseDeriv.md`, `MvPolynomial.hasseDeriv_monomial.md`.
