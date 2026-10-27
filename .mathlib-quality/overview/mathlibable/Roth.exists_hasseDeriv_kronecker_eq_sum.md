---
decl: Roth.exists_hasseDeriv_kronecker_eq_sum
file: Roth/GenWronskian.lean
line: 214
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: MODERATE
junk: KEEP
rationale: Existential, Kronecker-specific shadow of the characteristic-free multivariate Hasse chain rule (D^(mu)(P(g)) as a K[t]-combination of (Delta_d P)(g) with total degree of d at most mu, for any g in R[t]^sigma over any commutative ring); mathlib has neither the multivariate Hasse derivative nor any algebraic Faa di Bruno, but the right mathlib form is that general chain rule, which needs a new Taylor-expansion proof (not a mechanical weakening), so shipping is a judgment call tied to the MvPolynomial.hasseDeriv PR.
action: Keep locally (single caller Roth/GenWronskian.lean:260 in exists_genWronskian_ne_zero); if the MvPolynomial.hasseDeriv / MvPolynomial.taylor PR goes ahead, add a general `Polynomial.hasseDeriv_aeval` chain rule (any CommRing R, any g : sigma to R[X], explicit or existential coefficients) to the new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean and derive this lemma from it, dropping [CharZero K] and the private kronHasse/kronSpan machinery.
---

# Roth.exists_hasseDeriv_kronecker_eq_sum

## Inventory entry

### `theorem Roth.exists_hasseDeriv_kronecker_eq_sum`
- **Type**: `{K : Type*} [Field K] {σ : Type*} [Fintype σ] [CharZero K] (k μ : ℕ) : ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → Polynomial K), (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ K, Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P)`
- **What**: The `μ`-th Hasse derivative of the Kronecker substitution `h(t) = P(t^{k^{e j}})` is, uniformly in `P`, a `K[t]`-linear combination of Kronecker substitutions of the multivariate Hasse derivatives `Δ_d P` with `|d| ≤ μ`.
- **How**: Uses the private membership lemma `hasseDeriv_kronecker_mem` (the operator `P ↦ D^(μ)(kronecker k P)` lies in the `K[t]`-span `kronSpan k μ` of the operators `kronHasse k d`, `|d| ≤ μ`), then unpacks span membership with `Finsupp.mem_span_image_iff_linearCombination` and reads off `s := c.support`; closes with `simpa [Finsupp.linearCombination_apply, Finsupp.sum, kronHasse]` applied pointwise (`congrFun`).
- **Hypotheses**: `[Field K]`, `[Fintype σ]` (section variables), `[CharZero K]` (needed by `hasseDeriv_kronecker_mem`, which divides by `μ + 1` to pass from `derivative ∘ D^(μ)` to `D^(μ+1)`).
- **Uses from project**: `Roth.kronecker`, `MvPolynomial.hasseDeriv` (Roth/HasseDeriv.lean), private `Roth.hasseDeriv_kronecker_mem`, private `Roth.kronHasse` (and transitively `kronSpan`, `derivative_mem_kronSpan`, `derivative_kronHasse_aux`, `derivative_aeval`, `pderiv_hasseDeriv`).
- **Used by**: `Roth.exists_genWronskian_ne_zero` (Roth/GenWronskian.lean:260, via `choose s c hs hc using fun μ : Fin l ↦ exists_hasseDeriv_kronecker_eq_sum k μ`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 214–220, proof length 5 lines
- **Notes**: The statement is the source's "there are `r(μ)`, `f^μ_i(t)`, `Δ^{(i)}_μ` of order `≤ μ` with `d^μ/dt^μ h_ν = ∑ f^μ_i (Δ^{(i)}_μ φ_ν)(γ(t))`", with Hasse derivatives on both sides.

## Junk check (Step 8)
- Used anywhere? Yes, once: the key step of Lemma 1 (`exists_genWronskian_ne_zero`, l.260).
- Wrapper of 1–2 mathlib calls? No; it packages the private span-induction development into an existential. The final step is one mathlib call (`Finsupp.mem_span_image_iff_linearCombination`) on a project lemma.
- Does mathlib have it? No. Mathlib has only univariate `Polynomial.hasseDeriv` (with `hasseDeriv_comp`, `taylor_coeff`), no multivariate Hasse derivative, no algebraic chain rule for Hasse derivatives (only the analytic `FaaDiBruno.lean`) and no Kronecker substitution.
- Too specific (inline?)? Mildly: one caller. But it is the cleanly-stated public interface to the private `kronHasse`/`kronSpan` machinery and matches a numbered claim of the source; inlining would push span bookkeeping into Lemma 1.
- Well-chosen? Reasonable locally. The mathematically natural statement is the general Hasse chain rule for arbitrary substitutions `g : σ → K[t]` over any commutative ring; the Kronecker point and `[CharZero K]` are artefacts of the proof route.
- Conclusion: `KEEP`. Action: keep as the public interface for Lemma 1; consider replacing the proof by the general chain rule if the Hasse-derivative API is upstreamed.

## Mathlibable assessment (Step 9)

Pre-filter: public, name not `_aux`, docstring not internal/auxiliary, Step 8 `KEEP`, no `Roth.exists_hasseDeriv_kronecker_eq_sum` or `Polynomial.hasseDeriv_aeval`-type decl in mathlib (grep of `.lake/packages/mathlib/Mathlib/` for `hasseDeriv` finds only `Algebra/Polynomial/HasseDeriv.lean`, `Algebra/Polynomial/Taylor.lean`, `RingTheory/LaurentSeries.lean`). Not a glue lemma (5-line proof via span unpacking), so not INHERITED. Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief)
- decl `Roth.exists_hasseDeriv_kronecker_eq_sum`: ✓ resolved at Roth/GenWronskian.lean:214
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians of multivariate polynomials and Lemma 1 (linearly independent family has a nonzero generalized Wronskian), via Kronecker substitution.

### Statement (Phase 1)

`Roth.exists_hasseDeriv_kronecker_eq_sum` is a theorem stating the following. Let `K` be a field of characteristic zero, `σ` a finite set of variables with a chosen enumeration `e`, `k, μ ∈ ℕ`, and `γ(t) = (t^{k^{e(j)}})_j`. There are finitely many multi-indices `d` with `|d| ≤ μ` and polynomials `c_d(t) ∈ K[t]` such that for every `P ∈ K[x_σ]`, `D^{(μ)}(P(γ(t))) = ∑_d c_d(t) · (Δ_d P)(γ(t))`, where `D^{(μ)}` is the univariate and `Δ_d` the multivariate Hasse derivative. The point is uniformity: `s` and `c` do not depend on `P`.

Variables / typeclasses involved (Lean side):
- `K`, `[Field K]`, `[CharZero K]`: coefficient field (characteristic zero used in the proof).
- `σ`, `[Fintype σ]`: variables (finiteness for `Fintype.equivFin` inside `kronecker` and for the finite sum in the chain rule).
- `k`: Kronecker base; `μ`: derivative order.

Hypotheses (Lean side):
- none beyond typeclasses.

Conclusion (math): `D^{(μ)} ∘ γ^*` lies in the `K[t]`-span of `{γ^* ∘ Δ_d : |d| ≤ μ}`.

Conclusion (Lean): `∃ s c, (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P, Polynomial.hasseDeriv μ (kronecker k P) = ∑ d ∈ s, c d * kronecker k (hasseDeriv d P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an intermediate step (a claim inside the proof of Lemma 1), not a main result or a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5 (theorem)
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma generalized Wronskian proof Kronecker substitution derivative of h(t)=phi(t,t^k,...) differential operators order at most mu | yes | Kronecker substitution `(t, t^d, …, t^{d^{m-1}})` and Wronskian criterion with operators of order `≤ i` | arXiv 2502.00731 (subspace theorem survey), Roth 1955 Mathematika Lemma 1, Bombieri–Gubler App. D; the derivative-of-`h` step is stated as a chain-rule consequence, not as a named lemma |
| 2 | WebSearch (general form) | Hasse derivative chain rule composition multivariate polynomial substitution formula | yes | chain rule for Hasse derivatives of `f(g_1,…,g_n)`, a Faà di Bruno variant, valid over any field | arXiv 1303.0084 (Forbes–Shpilka, explicit Noether normalisation, Lemma on Hasse chain rule); Wikipedia "Hasse derivative" mentions a chain-rule analogue |
| 3 | WebSearch (aliases) | Faà di Bruno formula Hasse-Schmidt derivations composition polynomial arbitrary characteristic | yes | Faà di Bruno only transfers to char p for orders `< p`; Hasse–Schmidt / iterative higher derivations give the char-free version | arXiv 1611.01940 (chain rule for higher derivations), 1810.08075 (Narváez Macarro), math/0206261 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `r(\mu)` / differential operators | yes | l.292–294: "there is a natural number `r(μ)` … polynomials `f^μ_i(t)` with rational coefficients, and differential operators `Δ^{(i)}_μ` of order `≤ μ` such that `d^μ/dt^μ h_ν = ∑ f^μ_i(t)(Δ^{(i)}_μ φ_ν)(γ(t))`" | exact source; stated with ordinary derivatives, `γ(t) = (t, t^k, …)`; proved by induction with the chain rule |
| 6 | nLab | Hasse derivative / chain rule (query #4 of WebSearch with site terms: "nlab OR mathoverflow Hasse derivative chain rule composition") | no | — | no nLab page on Hasse derivatives or their chain rule |
| 7 | nCatLab | — | n/a | — | not a categorical concept (nLab #6 found nothing) |
| 8 | Stacks Project | — | n/a | — | Stacks treats differentials/derivations, not Hasse chain rules for polynomial substitution; not an algebraic-geometry statement |
| 9 | MathOverflow / Math.SE | query in #6 | no | no thread surfaced | — |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | 2502.00731 (2025), 2509.00887 (2025, Hasse–Schmidt derivations in char p), 2205.00342 (2022, multivariate multipoint evaluation, uses Hasse derivatives of compositions) | same general chain-rule picture |

### Literature summary (Phase 3)

Concept identified as: the chain rule (Faà di Bruno formula) for Hasse derivatives, specialised to a univariate substitution `γ(t)`; in Roth-type arguments it is the step "derivatives of `φ(γ(t))` are combinations of `(Δφ)(γ(t))` with `Δ` of order `≤ μ`".
Sources agree on the standard form: yes. For `g : σ → R[t]` and `P ∈ R[x_σ]`, `P(g(t+h)) = ∑_d (Δ_d P)(g(t)) · (g(t+h) − g(t))^d`; since `h | g_j(t+h) − g_j(t)`, the coefficient of `h^μ` gives `D^{(μ)}(P∘g) = ∑_{|d| ≤ μ} c_{d,μ}(t) (Δ_d P)(g(t))` with `c_{d,μ}` the `h^μ`-coefficient of `(g(t+h) − g(t))^d`, independent of `P`.
Most general standard form: over any commutative (semi)ring `R`, any finite `σ`, any substitution `g : σ → R[t]` (and in fact into any `R`-algebra with a Hasse–Schmidt derivation), with explicit coefficients.
Generality dimensions where the literature varies:
  - characteristic: ordinary-derivative versions need char 0 or orders `< p`; Hasse versions are characteristic-free.
  - substitution: Roth uses monomials `t^{k^{j}}`; the chain rule holds for arbitrary `g`.
  - explicitness: existential (Roth) vs explicit coefficient (Faà di Bruno / Taylor coefficient).
Disagreement with the literature: none in substance; the Lean form is a specialisation (Kronecker point, field of char 0, existential coefficients).

### Generality analysis — `Roth.exists_hasseDeriv_kronecker_eq_sum`

Literature-standard form (from Phase 3): for `[CommRing R]`, `[Fintype σ]`, `g : σ → R[X]`, `μ : ℕ`: `Polynomial.hasseDeriv μ (aeval g P) = ∑ d with d.degree ≤ μ, c μ d * aeval g (hasseDeriv d P)` with `c μ d` the `μ`-th Taylor coefficient of `∏ j (taylor-increment of g j)^(d j)`, or existentially.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CharZero K]` | char 0 | none | yes (mathematically) | the conclusion is characteristic-free, but the current proof divides by `μ + 1` (`smul_mem_iff` with `Nat.cast_ne_zero`); dropping it requires the Taylor-expansion proof, not a mechanical edit |
| 2 | `[Field K]` | field | commutative (semi)ring | yes (mathematically) | the current proof uses `smul_mem_iff` over the field `K` (restrictScalars); with a new proof only commutativity is needed |
| 3 | substitution `kronecker k` | `x_j ↦ t^{k^{e j}}` | any `g : σ → R[t]` | yes (mathematically) | `derivative_kronHasse_aux` uses `derivative_aeval` at the Kronecker point, but the span-induction argument works for any `g` (the derivative of `g j` replaces `derivative (X ^ k ^ e j)`); still needs restating four private helpers |
| 4 | `[Fintype σ]` | finite | finite (or finitely supported sum) | no | the sum over `j` in the first-order chain rule needs finiteness; the Hasse form would use `Finset` sums over `s` anyway |
| 5 | existential `s`, `c` | existential | explicit coefficients | stronger form exists | explicit form is strictly more informative; existential is what the caller needs |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (mathematically), but no mechanical weakening verifies: every typeclass is used by the present proof (`[CharZero K]` and `[Field K]` through `smul_mem_iff` by `(μ+1 : K) ≠ 0`; `kronecker` through `derivative_kronHasse_aux`). Per the gate, this is false-positive class 5 ("real but not a single mechanical edit"), so the bucket cannot be YES-but-generalise-first.
Number of weakening opportunities found: 3 (all requiring a new proof)
Proposed restatement (target for a future PR):

```lean
theorem Polynomial.hasseDeriv_aeval {R : Type*} [CommRing R] {σ : Type*} [Fintype σ]
    (g : σ → R[X]) (μ : ℕ) : ∃ (s : Finset (σ →₀ ℕ)) (c : (σ →₀ ℕ) → R[X]),
      (∀ d ∈ s, d.degree ≤ μ) ∧ ∀ P : MvPolynomial σ R,
        hasseDeriv μ (aeval g P) = ∑ d ∈ s, c d * aeval g (MvPolynomial.hasseDeriv d P)
```

(with an explicit-coefficient version via `MvPolynomial.taylor` preferred for mathlib).

Cost of restatement: MODERATE — the proof via the project's `MvPolynomial.taylor` (P(X + Y) = ∑ Δ_d P · Y^d, `coeff_taylor`) plus `Polynomial.taylor_coeff` and divisibility `X ∣ taylor(g j) − g j` is standard, but new.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles → typeclasses? | no | no bundled-structure hypotheses | — |
| 2 | sequences → filters? | no | purely algebraic | — |
| 3 | construction → universal property? | no | — | — |
| 4 | set-with-predicate → bundled substructure? | partially | the private proof already uses `Submodule.span`; the public statement could say `(fun P ↦ hasseDeriv μ (aeval g P)) ∈ Submodule.span R[X] (range ...)` | composes with span API, but the explicit sum is easier at the call site (Lemma 1 needs `choose`) |
| 5 | field-specific → ring? | yes | `[CommRing R]` without `CharZero` | char-p applications (polynomial method, multiplicity codes, Stöhr–Voloch) use Hasse chain rules in char p |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index → general? | no | `ℕ` orders are intrinsic | — |
| 8 | concrete-via-abstract? | yes | diagnostic: after `hasseDeriv_kronecker_mem`, the Kronecker point enters only through `derivative_aeval` at `X ^ k ^ e j` in `derivative_kronHasse_aux`; nothing uses its monomial shape or injectivity. Abstract form: arbitrary `g : σ → K[X]`, with this lemma as `g := fun j ↦ X ^ k ^ e j` | reusable Hasse chain rule for any polynomial curve |
| 9 | false-generalisation guard | no false generalisation | the general statement specialises to exactly the current one at `g = Kronecker point` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Polynomial.hasseDeriv_aeval` above (any `g`, any `CommRing`), ideally explicit via `MvPolynomial.taylor`.
  - Cost: MODERATE
  - Mathlib downstream this enables: a Hasse chain rule complementing `Polynomial.derivative_aeval`-style lemmas, `Polynomial.taylor_coeff`, and the univariate `Polynomial.hasseDeriv_comp`; needed by any polynomial-method argument (multiplicity Schwartz–Zippel, Wronskian criteria) in arbitrary characteristic.
  - Real mathematical improvement: removes an artificial characteristic-zero hypothesis and the special substitution, giving the actual chain rule rather than a Roth-specific consequence.

### Proof strategy — `Roth.exists_hasseDeriv_kronecker_eq_sum`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elementwise vs submodule | no | already point-free (`Submodule.span_induction`, `mem_span_image_iff_linearCombination`) | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | multivariate Hasse derivative + multivariate Taylor (project files, assessed YES), and a Hasse chain rule; with these the proof is a Taylor-coefficient comparison, characteristic-free | MODERATE (follow-up PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: expand `aeval g P` at `t + h` with `MvPolynomial.taylor` (Hasse coefficients), use `X ∣ taylor (g j) − g j`, compare `h^μ`-coefficients via `Polynomial.taylor_coeff`.
  - Cost: MODERATE
  - Missing mathlib API: `MvPolynomial.hasseDeriv`, `MvPolynomial.taylor` (both project-local, both assessed for upstreaming), the chain rule itself.
  - Would refactoring make the proof strictly shorter / cleaner? yes (removes `kronHasse`, `kronSpan`, `derivative_kronHasse_aux`, `derivative_mem_kronSpan`, `hasseDeriv_kronecker_mem` and `[CharZero K]`).

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_hasseDeriv_kronecker_eq_sum`

[A] Lean-Finder       "higher derivative of polynomial evaluated at polynomial maps is linear combination of partial derivatives of order at most n (Faà di Bruno)"   no hits (closest: `Polynomial.derivative_eval₂_C`, `Polynomial.aeval_iterate_derivative_of_ge`, `Polynomial.hasseDeriv_apply`)
[B] Loogle            `Polynomial.hasseDeriv, MvPolynomial.aeval`; `Polynomial.hasseDeriv, Polynomial.comp`   no hits (both empty)
[C] LeanSearch        "Hasse derivative of a composition of polynomials chain rule"   no hits (only first-order `Polynomial.derivative_comp`, analytic `HasDerivAt.scomp`)
[D] Grep mathlib src  `hasseDeriv` (files: Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean); `hasseDeriv.*aeval`, `kronecker.*hasse`, `FaaDiBruno`   no algebraic chain rule; `FaaDiBruno` only in Analysis/Calculus/ContDiff/FaaDiBruno.lean (analytic, formal multilinear series)
[E] Name pattern      via grep: `hasseDeriv_comp` exists (univariate `(D k).comp (D l) = choose • D (k+l)`, not a chain rule for substitution); no `hasseDeriv_aeval` / `hasseDeriv_eval₂`

Searched for both:
  - the user's current form (Kronecker-specific)
  - the literature-standard form (Hasse chain rule for arbitrary substitution; mathlib lacks even the multivariate Hasse derivative)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Building blocks present: `Polynomial.hasseDeriv`, `Polynomial.taylor_coeff`, `Polynomial.hasseDeriv_comp`, `Finsupp.mem_span_image_iff_linearCombination`; the multivariate side is missing.

### Normal-form check — `Roth.exists_hasseDeriv_kronecker_eq_sum`

Equivalent formalisms this statement could take: (a) existential sum (current); (b) span membership `(fun P ↦ D^(μ) (kronecker k P)) ∈ Submodule.span K[X] (kronHasse k '' {d | d.degree ≤ μ})` (the private `hasseDeriv_kronecker_mem`); (c) explicit Faà di Bruno sum with named coefficients.
Does mathlib already have a canonical form for this idea? no.
If no: canonical form proposed: (c), an explicit equation `hasseDeriv μ (aeval g P) = ∑ d ∈ s, c μ d * aeval g (hasseDeriv d P)`; LHS-to-RHS expansion as a non-simp rewrite.
RHS convention respected? yes (the derivative of the composite on the LHS, the expansion on the RHS).

### Syntactic generality — `Roth.exists_hasseDeriv_kronecker_eq_sum`

Alternative restatements attempted (list):
- span-membership form (b)
- existential sum (a)
- explicit coefficients (c)

Chosen restatement: (a) for the local caller, (c) for mathlib.
Justification: the caller (`exists_genWronskian_ne_zero`) uses `choose s c hs hc`, which (a) feeds directly; (c) would also feed it and is more reusable.

### Superfluous-argument audit — `Roth.exists_hasseDeriv_kronecker_eq_sum`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CharZero K]` | no (conclusion), yes (proof) | conclusion holds in every characteristic; current proof needs it |
| 2 | `[Field K]` | no (conclusion), yes (proof) | commutative ring suffices mathematically |
| 3 | `[Fintype σ]` | yes | needed by `kronecker` (`Fintype.equivFin`) and the first-order chain rule |
| 4 | `k` | yes | defines the substitution; any `g` works mathematically |
| 5 | `μ` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK locally; REFACTOR for mathlib (explicit chain-rule equation for arbitrary `g`)
Syntactic generality: OK locally
Superfluous arguments: 2 in the conclusion (`[CharZero K]`, `[Field K]` → `[CommRing R]`), not droppable with the current proof

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.exists_hasseDeriv_kronecker_eq_sum`

Internal use count: 0 (outside the declaring file); 1 inside Roth/GenWronskian.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/GenWronskian.lean:260 | `choose s c hs hc using fun μ : Fin l ↦ exists_hasseDeriv_kronecker_eq_sum (K := K) (σ := σ) k μ` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.exists_hasseDeriv_kronecker_eq_sum`?):
  - (none) — grep of `Roth/` for `hasseDeriv μ (kronecker` / `kronSpan` finds only the private helpers it wraps (l.146–205).

### Composition check (Phase 6)

Can `Roth.exists_hasseDeriv_kronecker_eq_sum` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finsupp.mem_span_image_iff_linearCombination` applied to a span membership.
  - Mathlib decls used: `Finsupp.mem_span_image_iff_linearCombination`, `Finsupp.linearCombination_apply`
  - Result: partial
  - Notes: this is the final step of the actual proof; the membership itself (`hasseDeriv_kronecker_mem`) is a ~40-line project development (span induction with the first-order chain rule `derivative_aeval` and `pderiv_hasseDeriv`), with no mathlib counterpart.

Attempt 2: from `Polynomial.taylor_coeff` and a multivariate Taylor expansion.
  - Mathlib decls used: `Polynomial.taylor_coeff`, `Polynomial.taylor`
  - Result: fails
  - Notes: mathlib has no multivariate Taylor expansion or multivariate Hasse derivative.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_hasseDeriv_kronecker_eq_sum`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the statement is the Roth-specific instance of the characteristic-free Hasse chain rule / Faà di Bruno (Forbes–Shpilka arXiv 1303.0084; Wikipedia "Hasse derivative"; source clean.tex l.292–294).
- Generality analysis (Phase 4): STRICTLY NARROWER mathematically, but no mechanical weakening verifies (every typeclass used by the current proof); gate false-positive class 5.
- Mathlib search (Phase 5): not in mathlib; mathlib lacks the multivariate Hasse derivative and any algebraic Hasse chain rule.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The lemma as stated is too narrow for mathlib: it fixes the Kronecker substitution, needs characteristic zero, and only asserts existence of coefficients. Its genuine content, that `D^{(μ)}(P ∘ g)` is a `K[t]`-combination of `(Δ_d P) ∘ g` with `|d| ≤ μ`, uniformly in `P`, is the multivariate Hasse chain rule, which holds for every `g : σ → R[t]` over every commutative ring and is missing from mathlib together with the multivariate Hasse derivative itself (the project's `MvPolynomial.hasseDeriv`, assessed YES-but-generalise-first, and `MvPolynomial.taylor`, assessed YES-add-as-is). That general chain rule is a reasonable mathlib addition (the named gap: mathlib has `Polynomial.derivative_comp`/`derivative_eval₂_C` for first order and analytic Faà di Bruno, but no Hasse or higher-order algebraic chain rule), but reaching it requires a new Taylor-coefficient proof and retiring five private helpers, not a single mechanical edit, so YES-but-generalise-first is excluded by the gate.

Whether to invest in the general chain rule (and in which shape: explicit or existential), or to keep this lemma as a project-local step of Lemma 1, is a scope decision tied to how much of the Hasse-derivative API is upstreamed. Locally the lemma is well-shaped for its single caller.

Numbered questions (≤5):
1. Will the `MvPolynomial.hasseDeriv` / `MvPolynomial.taylor` API be upstreamed? (If no, keep this lemma local and close the question.)
2. If yes, should that PR include a Hasse chain rule `Polynomial.hasseDeriv_aeval` for arbitrary `g : σ → R[X]` over `[CommRing R]`?
3. Should the mathlib form give explicit coefficients (the `h^μ`-Taylor coefficient of `∏ j (g j (t+h) − g j t)^(d j)`) rather than an existential?
4. Once the general rule exists, should this lemma be reproved as its one-line specialisation (dropping `[CharZero K]` and the private `kronHasse`/`kronSpan`/`derivative_kronHasse_aux`/`derivative_mem_kronSpan`/`hasseDeriv_kronecker_mem`), or inlined at Roth/GenWronskian.lean:260?

Next action: user answers the questions; re-run `/mathlibable Roth.exists_hasseDeriv_kronecker_eq_sum` to resolve the verdict.

---

### Next step

Keep the lemma locally for its single caller (Roth/GenWronskian.lean:260). If the multivariate Hasse-derivative PR (new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean) proceeds, decide questions 1–4 and, if approved, add the characteristic-free chain rule there and reprove this lemma as its specialisation to `g = fun j ↦ X ^ k ^ e j`.

## Evidence
- WebSearch: 4 queries (Roth Lemma 1 Kronecker derivative; Hasse derivative chain rule multivariate substitution; Faà di Bruno for Hasse–Schmidt derivations in arbitrary characteristic; nLab/MathOverflow Hasse chain rule). Hits: arXiv 2502.00731, 1303.0084, 1611.01940, 1810.08075, math/0206261, 2509.00887, 2205.00342, Wikipedia "Hasse derivative"; no nLab/MathOverflow pages.
- ChatGPT MCP: n/a (`ask_chatgpt_math` not configured in this session).
- Local references: `.mathlib-quality/references/clean.tex` l.292–294, 321–336.
- Mathlib: Loogle (2 queries, empty), LeanSearch (1), Lean-Finder (1), grep of `.lake/packages/mathlib/Mathlib/` for `hasseDeriv`, `hasseDeriv.*aeval`, `kronecker.*hasse`, `FaaDiBruno`.
- Project: `grep -rn exists_hasseDeriv_kronecker_eq_sum Roth/` (one caller, l.260); parent reports read: Roth.kronecker, Roth.hasseDeriv_kronecker_mem, Roth.derivative_aeval, Roth.linearIndependent_kronecker, MvPolynomial.hasseDeriv, MvPolynomial.taylor, Roth.genWronskian.
- No Lean evidence file: no weakening is claimed as verified (all proposed generalisations need a new proof), so no Lean run was needed.
