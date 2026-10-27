---
decl: Roth.kronecker_monomial
file: Roth/GenWronskian.lean
line: 60
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The monomial-evaluation lemma is the basic simp/API lemma of the Kronecker (weighted) substitution and has no mathlib counterpart (aeval_monomial leaves a Finsupp.prod of powers); re-aimed at weightedSubst w over CommSemiring with exponent Finsupp.weight w d it compiles verbatim (no Field, no Fintype) and the project lemma is a one-line specialisation.
action: Ship as MvPolynomial.weightedSubst_monomial (simp) together with the def MvPolynomial.weightedSubst in Mathlib/Algebra/MvPolynomial/ (next to Expand.lean), in the same PR as the Roth.kronecker API; locally restate against Finsupp.weight and keep the single call site coeff_kronecker (Roth/GenWronskian.lean:93) rewriting with it.
---

# Roth.kronecker_monomial

## Inventory entry

### `theorem Roth.kronecker_monomial`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] (k : ℕ) (d : σ →₀ ℕ) (a : K) : kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d`
- **What**: The Kronecker substitution `x_j ↦ t^{k^{e j}}` sends the monomial `a x^d` to `a t^{∑_j d_j k^{e j}}`.
- **How**: One `simp` call unfolding `kronecker`, `kroneckerExp`, then `MvPolynomial.aeval_monomial`, `Finsupp.prod_fintype`, `← pow_mul`, `mul_comm`, `← Finset.prod_pow_eq_pow_sum`.
- **Hypotheses**: section variables `[Field K]`, `[Fintype σ]`; no hypotheses.
- **Uses from project**: `Roth.kronecker`, `Roth.kroneckerExp`
- **Used by**: `Roth.coeff_kronecker` (Roth/GenWronskian.lean:93, `simp_rw [kronecker_monomial, Polynomial.coeff_C_mul_X_pow]`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 59–62, proof length 2 lines
- **Notes**: Neither `Field` nor `Fintype` is used essentially. `kroneckerExp k d` equals `Finsupp.weight (fun j ↦ k ^ equivFin σ j) d` (see the `Roth.kroneckerExp` report).

## Junk check (Step 8)
- Used anywhere? Yes, once: `coeff_kronecker` (l.93).
- Wrapper of 1–2 mathlib calls? Close to it. The proof is one `simp` with `aeval_monomial` plus three algebraic folding lemmas (`pow_mul`, `Finset.prod_pow_eq_pow_sum`, `Finsupp.prod_fintype`). It is the natural `simp` normal form for the substitution.
- Does mathlib have it? No. Loogle, LeanSearch and Lean-Finder return only the generic `MvPolynomial.aeval_monomial`, `eval₂Hom_monomial`, `bind₁_monomial` and `expand_monomial`. There is no lemma folding `d.prod fun i k ↦ (X ^ w i) ^ k` into `X ^ weight w d`.
- Too specific (inline?)? No. It is the monomial lemma of a named map, the analogue of `MvPolynomial.expand_monomial` for `expand`.
- Well-chosen? Yes as an API lemma. It should be stated against `Finsupp.weight` rather than `kroneckerExp`.
- Conclusion: `KEEP`. Action: restate against `Finsupp.weight` when `kroneckerExp` is replaced.

## Mathlibable assessment (Step 9)

Pre-filter: not private, no `_aux`, docstring not internal/auxiliary, Step 8 KEEP. A namespace-aware grep finds no `kronecker_monomial`/`weightedSubst` in mathlib. This is not a glue lemma (its proof is a `simp` with real algebraic folding, not `rfl`). The parent `Roth.kronecker` is YES-but-generalise-first and `Roth.kroneckerExp` is NO-mathlib-has-it (because mathlib has `Finsupp.weight`). Under the re-aim rule this lemma is therefore assessed in full, stated against `weightedSubst w` with exponent `Finsupp.weight w d`.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing `Roth.GenWronskian` is diagnostic-clean)
- decl `Roth.kronecker_monomial`: ✓ resolved at Roth/GenWronskian.lean:60
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians of multivariate polynomials and Lemma 1, proved via Kronecker substitution `x_j ↦ t^{k^j}`.

### Statement (Phase 1)

`Roth.kronecker_monomial` is a theorem stating the following. Let `K` be a field, `σ` a finite set of variables with a fixed enumeration `e : σ ≃ {0,…,p-1}`, and `k ∈ ℕ`. Under the Kronecker substitution `x_j ↦ t^{k^{e(j)}}`, the monomial `a·x^d` maps to `a·t^{N}` with `N = ∑_j d_j k^{e(j)}`.

Variables / typeclasses involved (Lean side):
- `K`, `[Field K]`: coefficients.
- `σ`, `[Fintype σ]`: variables (finiteness only feeds `Fintype.equivFin`).
- `k : ℕ`: the base.
- `d : σ →₀ ℕ`: the exponent vector; `a : K`: the coefficient.

Hypotheses (Lean side):
- none.

Conclusion (math): `κ_k(a x^d) = a t^{∑ d_j k^{e j}}`.

Conclusion (Lean): `kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the basic evaluation lemma of a helper map inside the proof of Lemma 1.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: n/a
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Kronecker substitution monomial x^d maps to t^(d_1 + d_2 k + ...) exponent base k | yes | `x_i ↦ x^{D^{i-1}}` sends `x^d` to `x^{∑ d_i D^{i-1}}`; inverse by D-adic expansion | arXiv 1807.08289, 1709.08979, 2403.12716; SFU Monagan course notes |
| 2 | WebSearch (general form) | monomial substitution x_i -> t^{w_i} weighted degree image of monomial is t^{w·d} | yes | weighted degree of `x^d` is `∑ w_i d_i`; `f(t^{w_1}z_1, …) = t^n f(z)` for weighted-homogeneous `f` | MathWorld "Weighted Homogeneous Polynomial"; arXiv 1412.7547; the general form is the weighted substitution with exponent the weighted degree |
| 3 | WebSearch (aliases) | "Kronecker map" OR "Kronecker substitution" monomial image "weighted degree" polynomial | yes | same monomial formula (Kronecker map, `(δ+1)^{i-1}` weights) | arXiv 2411.17330, 1412.4088; no weighted-Kronecker naming found |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `t^{k`, `s_1 + k s_2` | yes | l.231 `h_ν(t) = φ_ν(t, t^k, …)`; l.243 each monomial `b(s) x^s` becomes `b(s) t^{s_1 + k s_2 + ⋯ + k^{p-1} s_p}` | this is exactly the lemma, used implicitly in the source |
| 6 | nLab | Kronecker substitution / monomial substitution | no | — | no nLab page (checked with the parent assessment); computational-algebra fact |
| 7 | nCatLab | — | n/a | — | not a categorical concept (nLab found nothing) |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks 00OW (Noether normalisation) uses the trick only inside a proof |
| 9 | MathOverflow / Math.SE | query #3 site terms | no | — | no thread surfaced |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | 2403.12716 (2024), 2411.17330 (2024) | same monomial formula, with general or iterated weights |

### Literature summary (Phase 3)

Concept identified as: the image of a monomial under Kronecker substitution, i.e. the weighted degree.
Sources agree on the standard form: yes. Under `x_i ↦ t^{w_i}` the monomial `a x^d` maps to `a t^{∑ w_i d_i}`. Kronecker's weight is `w_i = D^{i-1}`.
Most general standard form: weighted substitution with arbitrary weight `w`, over any commutative (semi)ring; the exponent is the weighted degree `∑ w_i d_i` (mathlib: `Finsupp.weight w d`).
Generality dimensions where the literature varies:
  - weights: `D^{i-1}` up to arbitrary `w`; the lemma holds for any `w`.
  - coefficients: integers or fields in practice; the lemma holds over any commutative semiring.
Disagreement with the literature: the Lean form fixes `w = k^{equivFin σ ·}`, assumes a field, and uses a custom exponent `kroneckerExp`.

### Generality analysis — `Roth.kronecker_monomial`

Literature-standard form (from Phase 3): `aeval (fun j ↦ X ^ w j) (monomial d a) = C a * X ^ Finsupp.weight w d` for `[CommSemiring R]`, any `σ`, any `w : σ → ℕ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | commutative semiring | yes | Verified: `Evidence.weightedSubst_monomial` over `[CommSemiring R]` compiles. The `R = ℤ` example also compiles |
| 2 | `[Fintype σ]` | finite variables | any `σ` | yes | Verified: the evidence lemma uses `Finsupp.prod`/`Finsupp.sum` with no `Fintype`. The example at `σ = ℕ` compiles |
| 3 | weight `k ^ equivFin σ j` | fixed, noncanonical | arbitrary `w : σ → ℕ` | yes | Verified: the general-weight lemma compiles, and the project lemma follows from it in one `change`+`simpa` (evidence example 3) |
| 4 | exponent `kroneckerExp k d` | custom def | `Finsupp.weight w d` | yes (mathlib) | Verified in the evidence file and in the `Roth.kroneckerExp` report |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 4 (Field to CommSemiring, drop Fintype, arbitrary weight, `Finsupp.weight` exponent). All four are verified clean via `lean_diagnostic_messages` on `.mathlib-quality/overview/evidence/Roth.kronecker_monomial/reaim.lean`.
Proposed restatement:

```lean
@[simp] theorem MvPolynomial.weightedSubst_monomial {R σ : Type*} [CommSemiring R]
    (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]
```

Cost of restatement: CHEAP. It is a mechanical rewrite and was verified. It depends on the parent def `weightedSubst` landing first, or in the same PR.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | no hypotheses | — |
| 2 | sequences to filters? | no | finite algebraic identity | — |
| 3 | construction vs universal property? | no | already about an `aeval` | — |
| 4 | set-with-predicate to bundled substructure? | no | no sets involved | — |
| 5 | field to (semi)ring? | yes | `[CommSemiring R]` | usable over `ℤ`, `ℕ` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | weight `k ^ equivFin σ j` becomes `w : σ → ℕ`; exponent becomes `Finsupp.weight w` | `Finsupp.weight` API (`map_add`, `weight_single`); `IsWeightedHomogeneous` (`isWeightedHomogeneous_monomial` uses the same `Finsupp.weight w d`) |
| 8 | concrete-via-abstract? | yes | after unfolding, the proof never uses that the weight is `k ^ e j`; it only folds `∏ (X^{w j})^{d j}` | the general lemma, with the Kronecker case as a corollary (evidence example 3) |
| 9 | false-generalisation guard | no false generalisation | `Roth.kronecker k = weightedSubst (k ^ equivFin σ ·)` by `rfl`, so it is the same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `weightedSubst w (monomial d a) = C a * X ^ Finsupp.weight w d` (simp).
  - Cost: CHEAP
  - Mathlib downstream this enables: simp normal form for `weightedSubst` (same role as `expand_monomial` for `expand`). It also links to `Finsupp.weight` and `IsWeightedHomogeneous`: a `w`-homogeneous `P` of weight `n` maps to `C c * X ^ n` via `sum` + this lemma. It is the first step in coefficient lemmas such as the port of `coeff_kronecker`.
  - Real mathematical improvement: it removes the noncanonical enumeration and the custom exponent, and states the fact at its natural generality.

### Proof strategy — `Roth.kronecker_monomial`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ? | no | — | — |
| 2 | Algebra elementwise vs point-free? | no | single `simp` | — |
| 3 | Analysis sequences? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no (weak) | a `Finsupp.prod_pow_pow`-style folding `d.prod (fun i k ↦ (x ^ w i) ^ k) = x ^ weight w d` would make it one `rw`; not needed | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (one `simp` from `aeval_monomial`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.kronecker_monomial`

[A] Lean-Finder       "substituting X_i := t^(w_i) into a multivariate monomial X^d a gives a * t^(sum d_i w_i)"  no hits (returned `bind₁_monomial`, `expand_monomial`, `rename_monomial`, `MvPowerSeries.subst_monomial`; all generic or different maps)
[B] Loogle            `MvPolynomial.aeval, MvPolynomial.monomial, Polynomial.X`; `MvPolynomial.aeval, Finsupp.weight`  no hits for either
[C] LeanSearch        "aeval of monomial when each variable maps to a power of X equals C a times X to the weighted degree"  no hit beyond `MvPolynomial.aeval_monomial`, `eval₂Hom_monomial`, `eval₂_monomial`, `isWeightedHomogeneous_monomial`
[D] Grep mathlib src  `weightedSubst`, `kroneckerSubst`, `kronecker_monomial`, `Polynomial.X ^ w`, `fun i ↦ Polynomial.X ^`  no hits
[E] Name pattern      `weightedSubst_monomial`, `kronecker_monomial`  no mathlib decl (the only `kronecker` names are matrix Kronecker products, per the parent report)

Searched for both:
  - the user's current form (`kronecker k (monomial d a) = C a * X ^ kroneckerExp k d`)
  - the literature-standard form (`aeval (X ^ w ·) (monomial d a) = C a * X ^ Finsupp.weight w d`)

Concluded: found building blocks (`MvPolynomial.aeval_monomial`, `Finsupp.weight_apply`, `pow_mul`, `Finset.prod_pow_eq_pow_sum`); not in mathlib in either form.

### Normal-form check — `Roth.kronecker_monomial`

Equivalent formalisms this statement could take: `C a * X ^ weight w d`; `monomial (weight w d) a` (Polynomial); `algebraMap R R[X] a * d.prod (fun i k ↦ (X ^ w i) ^ k)` (raw `aeval_monomial`).
Does mathlib already have a canonical form for this idea? Partly. `C a * X ^ n` is the standard simp RHS (cf. `Polynomial.C_mul_X_pow_eq_monomial`, which goes the other way, so `monomial n a` is also acceptable). `Finsupp.weight` is canonical for the exponent.
Our statement is in normal form apart from the custom `kroneckerExp` exponent. REFACTOR: use `Finsupp.weight w d`.
RHS convention respected? yes

### Syntactic generality — `Roth.kronecker_monomial`

Alternative restatements attempted (list):
- current (`kroneckerExp`, Field, Fintype)
- `weightedSubst w (monomial d a) = C a * X ^ weight w d` (verified)
- `weightedSubst w (monomial d a) = Polynomial.monomial (weight w d) a` (equivalent via `C_mul_X_pow_eq_monomial`)

Chosen restatement: the `C a * X ^ weight w d` form.
Justification: it matches the single call site (`Polynomial.coeff_C_mul_X_pow` at l.93) and mathlib's `expand`/`aeval` simp conventions.

### Superfluous-argument audit — `Roth.kronecker_monomial`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | CommSemiring suffices (verified) |
| 2 | `[Fintype σ]` | no | only via `equivFin`/`Finsupp.prod_fintype`; general proof avoids it (verified) |
| 3 | `k` | yes | becomes the weight `w` |
| 4 | `d`, `a` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (exponent `Finsupp.weight w d`)
Syntactic generality: RESTATE (`weightedSubst w`)
Superfluous arguments: 2 to drop (`[Field K]` to `[CommSemiring R]`, `[Fintype σ]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.kronecker_monomial`

Internal use count: 0 (outside the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:93 (declaring file) | `simp_rw [kronecker_monomial, Polynomial.coeff_C_mul_X_pow]` in `coeff_kronecker` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.kronecker_monomial`?):
  - Roth/GenWronskian.lean:155–159 (`derivative_kronHasse_aux`) unfolds `kronecker` to `aeval` for the chain rule. That is not a monomial re-derivation.
  - (none else)

### Composition check (Phase 6)

Can `Roth.kronecker_monomial` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [aeval_monomial]`
  - Mathlib decls used: `MvPolynomial.aeval_monomial`
  - Result: partial. It leaves `algebraMap R R[X] a * d.prod fun i k ↦ (X ^ w i) ^ k` (evidence example 4).
  - Notes: folding into `X ^ weight w d` needs `Finsupp.prod`, `pow_mul`, `Finset.prod_pow_eq_pow_sum` and `Finsupp.weight_apply`.

Attempt 2: `simp [aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum, ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]`
  - Result: succeeds as a trivial simp composition (borderline per 6b).

Conclusion: COMPOSABLE as a simp-set for a bare `aeval`. However, this is the defining simp lemma of a named map (`weightedSubst`, YES-but-generalise-first), exactly as `expand_monomial` is for `expand`. A named def cannot ship without its monomial lemma, so this lemma rides with the def and Phase 7 treats it as NOT-COMPOSABLE.

## Verdict: `Roth.kronecker_monomial`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard fact. Under `x_i ↦ t^{w_i}` a monomial maps to `t^{weighted degree}` (Kronecker substitution literature; weighted-homogeneity scaling, MathWorld). The source uses it at clean.tex l.243.
- Generality analysis (Phase 4): STRICTLY NARROWER. Four weakenings were verified clean in `evidence/Roth.kronecker_monomial/reaim.lean`.
- Mathlib search (Phase 5): not in mathlib in either form; only the building block `aeval_monomial` exists.
- Composition check (Phase 6): a simp composition for bare `aeval`, but it is the defining API lemma of the proposed named def.

**Rationale:**

The parent `Roth.kronecker` is YES-but-generalise-first with target `MvPolynomial.weightedSubst w := aeval (X ^ w ·)`, and `Roth.kroneckerExp` should be replaced by `Finsupp.weight`. Re-aimed at that setting, this lemma becomes `weightedSubst w (monomial d a) = C a * X ^ Finsupp.weight w d`. It holds over any commutative semiring, any variable type and any weight, and compiles with the project's own proof idea (one `simp`). The project statement follows by `change` + `simpa` (evidence example 3). Mathlib has no lemma that folds `aeval_monomial`'s `Finsupp.prod` of powers into a single power with `Finsupp.weight` exponent. The named gap is the missing `_monomial` simp lemma for the missing weighted-substitution def (cf. `MvPolynomial.expand_monomial` for `expand`). It is also the link between `aeval (X ^ w ·)` and the existing `Finsupp.weight`/`IsWeightedHomogeneous` API.

On its own, a two-line simp lemma would not be a contribution. Its value depends on the def shipping, and every named substitution in mathlib ships with its monomial lemma. So the verdict is generalise-first in lockstep with the parent, not a standalone PR.

Reason for the generalisation: LITERATURE-WEAKENING (any commutative semiring, any weight) and MODERN-IDIOM (`Finsupp.weight` exponent, no `Fintype.equivFin`).

Proposed restatement:
```lean
@[simp] theorem MvPolynomial.weightedSubst_monomial {R σ : Type*} [CommSemiring R]
    (w : σ → ℕ) (d : σ →₀ ℕ) (a : R) :
    weightedSubst w (monomial d a) = Polynomial.C a * Polynomial.X ^ Finsupp.weight w d := by
  simp [weightedSubst, aeval_monomial, Finsupp.prod, Finsupp.weight_apply, Finsupp.sum,
    ← pow_mul, mul_comm, Finset.prod_pow_eq_pow_sum]   -- verified
```
Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- `simp` evaluation of `weightedSubst` on `P.as_sum`, which gives the coefficient and injectivity lemmas (ports of `coeff_kronecker`, `kronecker_eq_zero_iff`).
- With `isWeightedHomogeneous_monomial` (same `Finsupp.weight w d`): weighted-homogeneous polynomials map to single terms `C c * X ^ n`.
- Could simplify degree computations in `Mathlib/RingTheory/NoetherNormalization.lean` if it adopts the public injectivity lemma (as noted in the parent report).

PR grouping: ship in one PR with `MvPolynomial.weightedSubst` (parent `Roth.kronecker`), the base-k injectivity of `Finsupp.weight (k ^ e ·)` (from `Roth.kroneckerExp_injOn`), and the coeff and eq_zero_iff ports.

Next action: run `/generalise Roth.kronecker` (which covers this lemma) to restate it against `weightedSubst w` and `Finsupp.weight w`. Update the single call site `coeff_kronecker` (Roth/GenWronskian.lean:93). Then include `weightedSubst_monomial` in the `Mathlib/Algebra/MvPolynomial/` PR for `weightedSubst`.

---

## Next step

Run `/generalise Roth.kronecker` with this lemma's target `MvPolynomial.weightedSubst_monomial` (CommSemiring R, any σ, exponent `Finsupp.weight w d`), and ship it in the same PR as the def.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.kronecker_monomial/reaim.lean` (imports `Roth.GenWronskian`); `lean_diagnostic_messages`: clean, no errors or warnings, after one fix iteration (first version: the numeric example needed `Finsupp.weight_single`, and the specialisation needed `change` to `weightedSubst`). It verifies: (1) `weightedSubst_monomial` over `[CommSemiring R]`, any `σ`, any weight; (2) a numeric instance at `R = ℤ`, `σ = ℕ`; (3) `Roth.kronecker_monomial`'s statement derived from (1); (4) `aeval_monomial` alone leaves the unfolded `Finsupp.prod` form.
- Reused evidence: `.mathlib-quality/overview/evidence/Roth.kronecker/generalise.lean` (`rfl` identification of `kronecker` with `weightedSubst`) and `.mathlib-quality/overview/evidence/Roth.kroneckerExp/weight.lean` (`kroneckerExp = Finsupp.weight`).
- WebSearch (3 queries), Loogle (2), LeanSearch (1), Lean-Finder (1), mathlib grep (2 patterns): results recorded above. ChatGPT MCP: n/a, not configured.
