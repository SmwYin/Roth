---
decl: Roth.hasseDeriv_rename_mul_aeval
file: Roth/Separation.lean
line: 146
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The factorwise rule Delta_(d,nu)(U(x_tau)V(x_none)) = (Delta_d U)(x_tau)(D^(nu) V)(x_none) for Hasse derivatives of a product in disjoint variables is absent from mathlib (which has no multivariate Hasse derivative); it should ship with the parent API in the literature-standard Sum form and at mathlib's a.optionElim index, both verified to compile.
action: Upstream with MvPolynomial.hasseDeriv into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean as hasseDeriv_rename_inl_mul_rename_inr (Sum form) plus the Option form at d.optionElim nu; locally restate at optionElim and update the single call site det_hasseDeriv_separated (Roth/Separation.lean:365, its matrix index at :353).
---

# Roth.hasseDeriv_rename_mul_aeval

## Inventory entry

### `theorem Roth.hasseDeriv_rename_mul_aeval`
- **Type**: `{τ R : Type*} [CommSemiring R] (d : τ →₀ ℕ) (ν : ℕ) (U : MvPolynomial τ R) (V : Polynomial R) : hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval (X none) V) = rename some (hasseDeriv d U) * Polynomial.aeval (X none) (Polynomial.hasseDeriv ν V)` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check`, evidence (0))
- **What**: The Hasse derivative `Δ_{d + ν e_none}` of a separated product `U(x_τ) V(x_none)` is `(Δ_d U)(x_τ) · (D^{(ν)} V)(x_none)`.
- **How**: Splits `Δ_{d+νe_none} = Δ_d ∘ Δ_{νe_none}` with `hasseDeriv_hasseDeriv_of_disjoint` (supports disjoint since `none ∉ range some`), pulls `rename some U` out of `Δ_{νe_none}` with `hasseDeriv_mul_of_degreeOf_eq_zero` (degree of `rename some U` in `none` is 0, via `degrees_rename_of_injective`), applies `hasseDeriv_single_aeval_X`, pulls `aeval (X none) (D^ν V)` out of `Δ_{d.mapDomain some}` by the same lemma (via `aeval_X_eq_rename`, `Multiset.mem_replicate`), and finishes with `hasseDeriv_rename (Option.some_injective τ)`.
- **Hypotheses**: `[CommSemiring R]` only.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.hasseDeriv_mul_of_degreeOf_eq_zero`, `MvPolynomial.hasseDeriv_single_aeval_X`, `MvPolynomial.hasseDeriv_rename`, `Roth.aeval_X_eq_rename`
- **Used by**: `Roth.det_hasseDeriv_separated` in Roth/Separation.lean:365 (`rw [mul_comm (...), hasseDeriv_rename_mul_aeval]`, entries of `A Bᵀ`). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 141–166, proof length 19 lines
- **Notes**: Same disjoint-variables / non-canonical-index pattern as `Roth.coeff_rename_mul_aeval` (index `d.mapDomain some + single none ν` instead of mathlib's `d.optionElim ν`).

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:365), in the key step of Lemma 2 (`F = GW · W`).
- Wrapper of 1–2 mathlib calls? No: five project Hasse lemmas chained plus two degree side conditions; mathlib has no multivariate Hasse derivative at all.
- Does mathlib have it? No (Phase 5).
- Too specific? Single use, but it is the natural statement "Hasse derivatives act factorwise on products in disjoint variables" and isolates a 19-line computation from the determinant proof; inlining would bloat `det_hasseDeriv_separated`.
- Well-chosen? Mostly; index spelling non-canonical (see verdict).
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; qualified name absent from mathlib (mathlib has no `MvPolynomial.hasseDeriv`). Not a glue lemma (19-line proof), so no inheritance; full workflow below.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` elaborates with no errors)
- decl `Roth.hasseDeriv_rename_mul_aeval`: resolved at Roth/Separation.lean:146
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.hasseDeriv_rename_mul_aeval` is a theorem stating the following: let `U ∈ R[x_τ]` and `V ∈ R[y]`, and view `U(x_τ) V(x_*)` in `R[x_τ, x_*]`. For a multi-index `d` on `τ` and `ν ∈ ℕ`, the Hasse derivative `Δ_{(d,ν)} = Δ_d ∘ (1/ν!) ∂^ν/∂x_*^ν` of the product equals `(Δ_d U)(x_τ) · (D^{(ν)} V)(x_*)`, where `D^{(ν)}` is the univariate Hasse derivative.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — non-distinguished variables; `R`, `[CommSemiring R]` — coefficients.
- `d : τ →₀ ℕ`, `ν : ℕ` — the two halves of the derivative multi-index.
- `U : MvPolynomial τ R`, `V : Polynomial R`.

Hypotheses (Lean side):
- none.

Conclusion (math): `Δ_{(d,ν)}(U(x_τ)V(x_*)) = (Δ_d U)(x_τ) · (D^{(ν)}V)(x_*)`.

Conclusion (Lean): `hasseDeriv (d.mapDomain some + Finsupp.single none ν) (rename some U * Polynomial.aeval (X none) V) = rename some (hasseDeriv d U) * Polynomial.aeval (X none) (Polynomial.hasseDeriv ν V)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: helper identity for the determinant step of Lemma 2; not a main result, no new structure.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 19
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative product of polynomials in disjoint variables factorwise D(f(x)g(y)) | partial | via Taylor-coefficient definition, `A(s+z) = f(s1+z1) g(s2+z2)` separates, so `D^{(a,b)}(f(x)g(y)) = D^{(a)}f · D^{(b)}g` | Wikipedia "Hasse derivative" gives multivariate definition via Taylor coefficients; nLab "Hasse-Schmidt derivative"; no source names the factorwise rule |
| 2 | WebSearch (general form) | multivariate Hasse derivative Leibniz rule product formula separated variables | yes | multi-index Leibniz `D_α(fg) = ∑_{β+γ=α} D_β f · D_γ g` (arXiv 1802.09894 Hasse–Schmidt derivations; arXiv 1406.0657 §4) | factorwise rule is the special case where `D_β f = 0` unless `β` lives on f's variables |
| 3 | WebSearch (named-after / context) | Roth theorem proof generalized Wronskian Hasse operator separate variables determinant | partial | Roth 1955 Mathematika; arXiv 2502.00731 survey; arXiv 2111.12409 | the separated-product step is used implicitly in Roth's lemma proofs (induction on number of variables) |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `Delta`, `phi_\rho` | yes | line 414: `GW = det(∑_ρ Δ_μ (1/ν!) ∂^ν/∂x_p^ν φ_ρ(x_p) ψ_ρ(x_1..x_{p-1}))`, lines 408–409 `A_{μρ} = Δ_μ ψ_ρ`, `B_{νρ} = Δ_ν φ_ρ` | exactly the factorwise identity, used without comment |
| 6 | nLab | Hasse-Schmidt derivative | yes | higher derivations `D_n` with `D_n(ab) = ∑_{i+j=n} D_i a D_j b`; several indeterminates handled separately, order irrelevant | no separated-product statement, consistent with Leibniz |
| 7 | nCatLab | Hasse-Schmidt derivative (same nLab/ncatlab page) | yes | same as #6 | not categorical beyond that |
| 8 | Stacks Project | n/a | n/a | — | Stacks treats differentials/derivations, not Hasse operators on polynomial rings; checked that "Hasse" does not appear in the relevant algebra chapters' scope |
| 9 | MathOverflow / Math.SE | (covered by #1/#2 searches; no thread surfaced) | no | — | too elementary to be discussed |
| 10 | recent arXiv | arXiv 2311.12752 (line-point low-degree test), arXiv 1003.3386 (monomial-like codes) surfaced by #1 | yes | multivariate Hasse derivatives via `A(x+z)` coefficients; product rule used freely | confirms the standard multi-index Leibniz framework |

### Literature summary (Phase 3)

Concept identified as: multivariate Hasse derivatives acting on products of polynomials in disjoint sets of variables; a special case of the multi-index Leibniz rule (equivalently, Taylor expansion `A(x+z)` factorising when `A = f(x)g(y)`).
Sources agree on the standard form: yes — `Δ_{(α,β)}(f(x)g(y)) = Δ_α f(x) · Δ_β g(y)` follows immediately from Leibniz / Taylor; it is used, never stated as a named result.
Most general standard form: for arbitrary variable sets `X`, `Y`, `f ∈ R[X]`, `g ∈ R[Y]`, multi-indices `α` on `X`, `β` on `Y`: `Δ_{α ⊔ β}(f g) = (Δ_α f)(Δ_β g)` in `R[X ⊔ Y]`.
Generality dimensions where the literature varies:
  - second block: one variable (project) up to arbitrary `Y` (most general).
  - coefficient ring: commutative semiring (already most general).
Disagreement with the literature: none mathematically; the project specialises to a one-variable second block and spells the index `d.mapDomain some + single none ν` rather than mathlib's `d.optionElim ν`.

### Generality analysis — `Roth.hasseDeriv_rename_mul_aeval`

Literature-standard form: `hasseDeriv (Finsupp.sumElim d e) (rename Sum.inl p * rename Sum.inr q) = rename Sum.inl (hasseDeriv d p) * rename Sum.inr (hasseDeriv e q)`; mathlib-idiomatic Option form at index `d.optionElim ν`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial`, `rename` require it |
| 2 | second block `{none}`, `V : Polynomial R` | one variable | arbitrary variable set (`Sum` form) | yes (restatement) | verified: `hasseDeriv_rename_inl_mul_rename_inr` compiles (evidence (2)) |
| 3 | index `d.mapDomain some + single none ν` | non-canonical | `d.optionElim ν` | yes (restatement) | verified: `hasseDeriv_rename_some_mul_aeval_X_none` compiles (evidence (1)) |
| 4 | `τ : Type*` | arbitrary | arbitrary | no | section `Fintype`/`DecidableEq` already omitted |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (one-variable second block; non-canonical index)
Number of weakening opportunities found: 2 (both restatements, both verified clean by `lean_diagnostic_messages`, evidence (1)–(2))
Proposed restatement:

```lean
theorem MvPolynomial.hasseDeriv_rename_inl_mul_rename_inr (d : σ →₀ ℕ) (e : τ →₀ ℕ)
    (p : MvPolynomial σ R) (q : MvPolynomial τ R) :
    hasseDeriv (Finsupp.sumElim d e) (rename Sum.inl p * rename Sum.inr q) =
      rename Sum.inl (hasseDeriv d p) * rename Sum.inr (hasseDeriv e q)

theorem MvPolynomial.hasseDeriv_rename_some_mul_aeval_X_none (d : τ →₀ ℕ) (ν : ℕ)
    (U : MvPolynomial τ R) (V : Polynomial R) :
    hasseDeriv (d.optionElim ν) (rename some U * Polynomial.aeval (X none) V) =
      rename some (hasseDeriv d U) * Polynomial.aeval (X none) (Polynomial.hasseDeriv ν V)
```

Cost of restatement: CHEAP — Sum form proved in ~20 lines by the same strategy (disjoint split + `hasseDeriv_mul_of_degreeOf_eq_zero` twice + `hasseDeriv_rename` twice); Option form is a 3-line index conversion.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | the identity is already stated structurally (via `rename`) | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general? | yes | second block `Option`/one variable to arbitrary `τ` (`Sum` form) | general disjoint-variables Hasse API, usable with `sumAlgEquiv`; Option form follows |
| 8 | Concrete-via-abstract? | partially | proof never uses that the second block is a single variable except through `hasseDeriv_single_aeval_X`; in the Sum form that step disappears (evidence (2) uses only `hasseDeriv_rename`) | the Option form becomes a corollary via `aeval_X_eq_rename` |
| 9 | False-generalisation guard | no | Option form is the same statement in canonical spelling; Sum form strictly contains it (`Option τ ≃ τ ⊕ Unit`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the Sum form plus the Option form at `d.optionElim ν` above.
  - Cost: CHEAP
  - Mathlib downstream this enables: matches `optionEquivLeft_coeff_coeff` / `mem_support_coeff_optionEquivLeft` index normal form and sits beside the sibling coefficient lemma `coeff_rename_some_mul_aeval_X_none` (Roth.coeff_rename_mul_aeval report); Sum form pairs with `sumAlgEquiv_comp_rename_inl/inr`.
  - Real mathematical improvement: the Sum form is the actual content (Hasse operators respect the tensor decomposition `R[X ⊔ Y] ≅ R[X] ⊗ R[Y]`), and consumers no longer need the `mapDomain some + single none` conversion.

### Proof strategy — `Roth.hasseDeriv_rename_mul_aeval`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | multivariate `hasseDeriv` API (parent, `hasseDeriv_rename`, `hasseDeriv_hasseDeriv_of_disjoint`, Leibniz `hasseDeriv_mul`) and a `degreeOf (inr j) (rename inl p) = 0` lemma (currently `simp [degreeOf, degrees_rename_of_injective]`) | CHEAP (ships with the parent PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: prove the Sum form (no `hasseDeriv_single_aeval_X` needed) and derive the Option form; alternatively, once the multivariate Leibniz `hasseDeriv_mul` exists (per the `hasseDeriv_mul_of_degreeOf_eq_zero` report), the Sum form is a `Finset.sum_eq_single` over the antidiagonal.
  - Cost: CHEAP
  - Missing mathlib API (if any): all of the multivariate Hasse derivative API (parent `MvPolynomial.hasseDeriv`)
  - Would refactoring make the proof strictly shorter / cleaner? yes (removes the one-variable special-case step)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.hasseDeriv_rename_mul_aeval`

[A] Lean-Finder       "Hasse derivative of product of polynomials in disjoint variables equals product of Hasse derivatives"   no hit: `Polynomial.hasseDeriv_mul` (univariate Leibniz), `MvPolynomial.pderiv_mul`, `Polynomial.derivative_prod`
[B] Loogle            `Polynomial.hasseDeriv, MvPolynomial.rename`   no results
[C] LeanSearch        "hasseDeriv of rename times polynomial in another variable"   no hit: `MvPolynomial.pderiv_rename`, `Polynomial.hasseDeriv`, `Polynomial.hasseDeriv_one`
[D] Grep mathlib src  `hasseDeriv` across Mathlib   only Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean; none in Algebra/MvPolynomial or RingTheory/MvPowerSeries
[E] Name pattern      `MvPolynomial.hasseDeriv`, `hasseDeriv_rename`   not in mathlib (project-only)

Searched for both:
  - the user's current form (Option / `aeval (X none)`): not in mathlib.
  - the literature-standard form (Sum / multi-index Leibniz): not in mathlib (no multivariate Hasse derivative exists).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); closest analogues `MvPolynomial.pderiv_rename`, `MvPolynomial.pderiv_mul`, `Polynomial.hasseDeriv_mul`.

### Normal-form check — `Roth.hasseDeriv_rename_mul_aeval`

Equivalent formalisms: index (a) `d.mapDomain some + single none ν` (project); (b) `d.optionElim ν` (mathlib); (c) Sum form with `Finsupp.sumElim d e`.
Does mathlib already have a canonical form? yes — (b) for Option indices (`optionEquivLeft_coeff_coeff`), `Finsupp.sumElim` for Sum.
Is our statement stated against the canonical form? NO → REFACTOR to (b), with (c) as the general lemma.
RHS convention respected? yes (RHS is the factored product).

### Syntactic generality — `Roth.hasseDeriv_rename_mul_aeval`

Alternative restatements attempted:
- `optionElim` index (evidence (1)): compiles.
- Sum form (evidence (2)): compiles.
- `toMvPolynomial none V` in place of `aeval (X none) V` (per `hasseDeriv_single_aeval_X` report): definitional, not separately compiled.

Chosen restatement: Sum form as the main lemma, Option form at `optionElim` as corollary.
Justification: the single caller (`det_hasseDeriv_separated`) builds the index itself in its matrix entry, so it can use `(D μ).optionElim ν` just as easily, and the result then matches the sibling coefficient lemma.

### Superfluous-argument audit — `Roth.hasseDeriv_rename_mul_aeval`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed by `MvPolynomial` |
| 2 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted (evidence (0)); `classical` used in the proof |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (index `d.optionElim ν`)
Syntactic generality: RESTATE (Sum form as main lemma)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.hasseDeriv_rename_mul_aeval`

Internal use count: 0 (outside the declaring file); 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:365 | `rw [mul_comm (Polynomial.aeval (X none ...) (φ ρ)), hasseDeriv_rename_mul_aeval]` in `det_hasseDeriv_separated` (matrix index `(D μ).mapDomain some + Finsupp.single none ν` at :353) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.hasseDeriv_rename_mul_aeval`?):
  - (none) — `grep -rn "hasseDeriv_hasseDeriv_of_disjoint\|hasseDeriv_single_aeval_X" Roth/` shows these are used together only here.

K = 1 would lean toward inlining, but the identity is the natural API statement for disjoint-variable products (the source states it as a step), and in mathlib it is the expected companion of `hasseDeriv_rename` / Leibniz; the single-use count reflects the project's narrow consumer, not the abstraction.

### Composition check (Phase 6)

Can `Roth.hasseDeriv_rename_mul_aeval` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone
  - Mathlib decls used: none applicable — mathlib has no multivariate Hasse derivative.
  - Result: fails.

Attempt 2: from the (to-be-upstreamed) project API
  - Decls used: `hasseDeriv_hasseDeriv_of_disjoint`, `hasseDeriv_mul_of_degreeOf_eq_zero` ×2, `hasseDeriv_single_aeval_X`, `hasseDeriv_rename`, plus two degree side conditions.
  - Result: a 6-rewrite chain with side goals — a proof, not a composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.hasseDeriv_rename_mul_aeval`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard consequence of the multi-index Leibniz rule / Taylor factorisation; used verbatim in the source (clean.tex:408–414).
- Generality analysis (Phase 4): STRICTLY NARROWER (one-variable second block; non-canonical index), both restatements verified to compile (evidence (1), (2)).
- Mathlib search (Phase 5): not in mathlib in either form; mathlib has no multivariate Hasse derivative.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**
The gap is the whole multivariate Hasse derivative API: mathlib has `Polynomial.hasseDeriv` (with Leibniz `hasseDeriv_mul`) and `MvPolynomial.pderiv` (with `pderiv_rename`, `pderiv_mul`), but no `MvPolynomial.hasseDeriv`. Within the planned `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` (see the `MvPolynomial.hasseDeriv` report), the statement that Hasse operators act factorwise on products in disjoint variables is the expected companion of `hasseDeriv_rename` and the Leibniz rule; it is what every Wronskian/Roth-lemma argument uses when separating a variable (source clean.tex:414), and the project's determinant step `det_hasseDeriv_separated` rests on it.

The project form should not ship as stated. The literature content is the Sum form (arbitrary second block), which evidence (2) proves directly by the same strategy without the one-variable bridge lemma; and the Option form should use mathlib's `d.optionElim ν` index, as decided for the sibling `Roth.coeff_rename_mul_aeval`.

Reason for the generalisation: both apply.
- LITERATURE-WEAKENING: second block generalises from one variable to arbitrary `τ` (Sum form).
- MODERN-IDIOM: index moves to the `optionElim` normal form, matching `optionEquivLeft_coeff_coeff` and the sibling coefficient lemma.

Proposed restatement:
```lean
theorem MvPolynomial.hasseDeriv_rename_inl_mul_rename_inr (d : σ →₀ ℕ) (e : τ →₀ ℕ)
    (p : MvPolynomial σ R) (q : MvPolynomial τ R) :
    hasseDeriv (Finsupp.sumElim d e) (rename Sum.inl p * rename Sum.inr q) =
      rename Sum.inl (hasseDeriv d p) * rename Sum.inr (hasseDeriv e q)
theorem MvPolynomial.hasseDeriv_rename_some_mul_aeval_X_none (d : τ →₀ ℕ) (ν : ℕ)
    (U : MvPolynomial τ R) (V : Polynomial R) :
    hasseDeriv (d.optionElim ν) (rename some U * Polynomial.aeval (X none) V) =
      rename some (hasseDeriv d U) * Polynomial.aeval (X none) (Polynomial.hasseDeriv ν V)
```
Both compile in evidence/Roth.hasseDeriv_rename_mul_aeval/restate.lean.
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- Hasse-operator counterpart of `pderiv_rename` for disjoint-variable products; pairs with `sumAlgEquiv_comp_rename_inl/inr`
- same index normal form as `optionEquivLeft_coeff_coeff` and the sibling `coeff_rename_some_mul_aeval_X_none`
- generalised Wronskian factorisations `GW(φ(x_*)ψ(x_τ)) = GW(ψ)·W(φ)` become a direct `Matrix.det_mul` argument

Proposed mathlib location: new `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean` (with the parent `MvPolynomial.hasseDeriv`).
Proposed PR title: "feat(Algebra/MvPolynomial/HasseDeriv): Hasse derivatives of products in disjoint variables"
PR grouping: ship with `MvPolynomial.hasseDeriv`, `hasseDeriv_rename`, `hasseDeriv_hasseDeriv_of_disjoint`, `hasseDeriv_mul_of_degreeOf_eq_zero` (Leibniz), `hasseDeriv_single_aeval_X`; coordinate the index spelling with the `Roth.coeff_rename_mul_aeval` PR.
Local refactor: restate at `d.optionElim ν`; change the matrix index in `det_hasseDeriv_separated` (Separation.lean:353) to `(D μ).optionElim ν` and check its downstream users of that index.
Next action: run `/generalise Roth.hasseDeriv_rename_mul_aeval` with the Sum / `optionElim` targets, then `/cleanup` and fold into the parent HasseDeriv PR.

---

## Next step

Restate at `d.optionElim ν` (with the Sum form as the general lemma), update the single call site `det_hasseDeriv_separated` (Roth/Separation.lean:365, index at :353), and upstream both forms with the multivariate Hasse derivative API to `Mathlib/Algebra/MvPolynomial/HasseDeriv.lean`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.hasseDeriv_rename_mul_aeval/restate.lean` (imports `Roth.Separation`), checked with `lean_diagnostic_messages`: no errors or warnings, only the `#check` info. (0) `#check @Roth.hasseDeriv_rename_mul_aeval` shows `[CommSemiring R]` only. (1) `hasseDeriv_rename_some_mul_aeval_X_none` (`optionElim` index) compiles via an index conversion and the project lemma. (2) Sum form `hasseDeriv_rename_inl_mul_rename_inr` compiles via `hasseDeriv_hasseDeriv_of_disjoint`, `hasseDeriv_mul_of_degreeOf_eq_zero` ×2, `hasseDeriv_rename` ×2, `degrees_rename_of_injective`.
- Searches: 3 WebSearch queries (recorded above); Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no results); mathlib grep for `hasseDeriv` (only univariate/Laurent files), `pderiv_rename`/`pderiv_mul` (PDeriv.lean:110, 143), `Finsupp.sumElim`/`optionElim` (Data/Finsupp/Basic.lean:1046, Option.lean:119); local reference grep of clean.tex (lines 408–414). ChatGPT MCP n/a (not configured in this session).
