---
decl: MvPolynomial.hasseDeriv_map
file: Roth/HasseDeriv.lean
line: 134
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Delta_d commutes with coefficient change along any ring hom; it is the multivariate counterpart of mathlib's Polynomial.hasseDeriv_map and the Hasse analogue of MvPolynomial.pderiv_map, absent from mathlib (no MvPolynomial Hasse derivative), maximally general (RingHom of CommSemirings is exactly what MvPolynomial.map takes); should ship tagged simp like the univariate one.
action: Upstream with MvPolynomial.hasseDeriv to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, adding the simp attribute (safe, evidence file); locally keep (call sites Roth/MainLemma.lean:409,489,492,495, Roth/Theta.lean:524,580, Roth/Separation.lean:533).
---

# MvPolynomial.hasseDeriv_map

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_map`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {S : Type*} [CommSemiring S] (f : R →+* S) (d : σ →₀ ℕ) (P : MvPolynomial σ R), (hasseDeriv d) ((map f) P) = (map f) ((hasseDeriv d) P)`
- **What**: The multivariate Hasse derivative commutes with changing coefficients along a ring homomorphism: `Δ_d (f_* P) = f_* (Δ_d P)`; used to pass between `ℤ`, `ℚ` and `ℝ` coefficients.
- **How**: `ext e` then `simp [coeff_hasseDeriv, coeff_map]`: both coefficients equal `f (hasseCoeff d (e + d) * P.coeff (e + d))`, using that `f` fixes natural-number casts (`map_natCast`, `map_mul` via simp).
- **Hypotheses**: `f : R →+* S` between commutative semirings (forced by `MvPolynomial.map`); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.coeff_hasseDeriv` (and implicitly `MvPolynomial.hasseCoeff`)
- **Used by**: Roth/MainLemma.lean:409 (`eval_hasseDeriv_sub_eq_zero`), Roth/MainLemma.lean:489, 492, 495 (`exists_hasseDeriv_index_eval_bound_aux`), Roth/Theta.lean:524 (`mapped_det_ne_zero_aux`), Roth/Theta.lean:580 (`index_le_lem6`), Roth/Separation.lean:533 (`exists_rat_factors_det_hasseDeriv_aux`).
- **Visibility**: public
- **Lines**: 134–137 (docstring 130–133), proof length 2 lines
- **Notes**: Not tagged `@[simp]`, whereas mathlib's univariate `Polynomial.hasseDeriv_map` is `@[simp]`; every call site passes it to `simp`/`simpa`/`rw` explicitly. Mathlib's `MvPolynomial.pderiv_map` takes `φ`, `f`, `i` implicit; the project (like `Polynomial.hasseDeriv_map`) takes them explicit.

## Junk check (Step 8)
- Used anywhere? Yes: 7 uses in 3 files (MainLemma, Theta, Separation).
- Wrapper of 1–2 mathlib calls? No: it is about the project operator; the mathlib analogues (`Polynomial.hasseDeriv_map`, `MvPolynomial.pderiv_map`) are about different operators.
- Does mathlib have it? No (Loogle `"hasseDeriv_map"` returns only `Polynomial.hasseDeriv_map` and `LaurentSeries.hasseDeriv_map`).
- Too specific / inline? No: it is the standard base-change API lemma carried by every derivative-like operator in mathlib (`Polynomial.derivative_map`, `Polynomial.iterate_derivative_map`, `Polynomial.hasseDeriv_map`, `MvPolynomial.pderiv_map`, `LaurentSeries.hasseDeriv_map`).
- Well-chosen? Yes; one improvement: tag `@[simp]` (matches the univariate lemma; evidence shows no looping).
- Conclusion: `KEEP` — action: keep; add `@[simp]`; upstream with the parent definition.

## Mathlibable assessment (Step 9)

Not a glue lemma (needs `ext` plus the coefficient formula; plain `simp` fails, evidence item 2), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles with no errors or warnings)
- decl `MvPolynomial.hasseDeriv_map`: resolved at Roth/HasseDeriv.lean:134
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_map` is a theorem stating the following:

Let `f : R → S` be a homomorphism of commutative semirings and `f_* : R[X_σ] → S[X_σ]` the induced map on polynomial rings (apply `f` to every coefficient). For every multi-index `d ∈ ℕ^(σ)` and polynomial `P ∈ R[X_σ]`, the Hasse derivative commutes with `f_*`: `Δ_d (f_* P) = f_* (Δ_d P)`. This holds because `Δ_d` is defined by integer (binomial) coefficients, which every ring homomorphism fixes; in particular the Hasse derivative "is defined over ℤ".

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R S : Type*`, `[CommSemiring R] [CommSemiring S]` — source and target coefficient rings.
- `f : R →+* S` — the coefficient change.
- `d : σ →₀ ℕ` — the order of the derivative.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `Δ_d ∘ f_* = f_* ∘ Δ_d`.

Conclusion (Lean): `hasseDeriv d (map f P) = map f (hasseDeriv d P)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic naturality API lemma of the BIG parent definition `MvPolynomial.hasseDeriv`; not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative commutes with reduction of coefficients ring homomorphism polynomial "Hasse derivative" | partial | `D^(r) X^n = binom(n, r) X^(n-r)` has integer coefficients, so it is defined over `ℤ` and commutes with any coefficient map | Wikipedia "Hasse derivative"; arXiv 1501.07502; no source states it as a numbered lemma (folklore, immediate from the definition) |
| 2 | WebSearch (general form) | Hasse-Schmidt derivation base change functorial ring homomorphism compatible higher derivation polynomial ring | yes | base change of HS-derivations: `HS^m_{B/A} ⊗_B B' ≅ HS^m_{B'/A'}` for `B' = B ⊗_A A'` (Vojta, Jets via Hasse–Schmidt derivations, arXiv math/0407113, Lemma 5.5) | the polynomial case `B = A[X_σ]`, `B' = A'[X_σ]` is our statement at the operator level |
| 3 | WebSearch (named-after / aliases) | multivariate Hasse derivative integer coefficients reduce mod p "divided derivative" defined over Z | yes | multivariate `∂̄_a f = Σ_e binom(e, a) coeff_e(f) x^(e-a)`; the binomial formula makes it defined over `ℤ`, commuting with reduction mod `p` | arXiv 2111.07572, 2205.00342, 1310.6482, 1810.08075 |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for coefficients / Lean implementation notes | partial | the paper works over `ℚ`, `ℤ` and `ℝ` (l.166, 225, 374, 396, 430); the passage between coefficient rings is a Lean implementation matter (the lemma's docstring cites "§1, Lean implementation note"; l.147 note on `MvPolynomial`) | matches the call sites (`Int.castRingHom ℝ`, `Int.castRingHom S`) |
| 6 | nLab | Hasse-Schmidt derivative | yes | HS derivations as ring maps `A → A[[t]]`; base change is functorial | nLab "Hasse-Schmidt derivative" (no separate polynomial-ring lemma) |
| 7 | nCatLab | — | n/a | — | not a categorical concept beyond naturality of the operator |
| 8 | Stacks Project | — | n/a | — | Stacks treats differential operators and their base change abstractly (Tag 09CH region); no Hasse-derivative-specific lemma |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; treated as immediate from the definition |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | yes | arXiv 2205.00342 (2022), 2111.07572 (2021), 1905.01704 (2019, base change of integrable derivations) | all use the `ℤ`-defined binomial formula |

### Literature summary (Phase 3)

Concept identified as: naturality of Hasse derivatives in the coefficient ring (Hasse derivatives are defined over `ℤ`); abstractly, base change of Hasse–Schmidt derivations.
Sources agree on the standard form: yes.
Most general standard form: for any ring map `A → A'`, the Hasse derivatives on `A[X_σ]` and `A'[X_σ]` intertwine the induced map `A[X_σ] → A'[X_σ]`; equivalently `D^(β)` is the base change of `D^(β)` on `ℤ[X_σ]`.
Generality dimensions where the literature varies:
  - object: polynomials / power series / abstract HS derivations (operator choice belongs to the parent report).
  - map: ring homomorphism (standard) vs. tensor base change (abstract; for polynomial rings these coincide).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_map`

Literature-standard form (from Phase 3): `Δ_d ∘ f_* = f_* ∘ Δ_d` for any ring map `f`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `f : R →+* S` | ring hom | ring map | no | `MvPolynomial.map` requires `R →+* S`; an additive or `ℕ`-linear map would do mathematically (coefficient formula only needs `f (n * a) = n * f a`), but then the map on polynomials is `Finsupp.mapRange`, not `MvPolynomial.map`, and none of the 7 call sites need it |
| 2 | `[CommSemiring R] [CommSemiring S]` | commutative semirings | any rings | no (for `MvPolynomial`) | `MvPolynomial σ R` requires `CommSemiring R` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 3 | `d`, `P` | arbitrary | arbitrary | n/a | no constraint |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (no propositional hypotheses; typeclasses and the morphism type are forced by `MvPolynomial.map`).
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical? | no | a semilinear-map commutation `(hasseDeriv d).comp (map f) = ...` would need `R`-vs-`S` semilinearity bookkeeping; the pointwise form is what `simp` uses | — |
| 7 | concrete index to general? | no | index type already general | — |
| 8 | concrete-via-abstract? | no | proof uses only the coefficient formula; no named object | — |
| 9 | false-generalisation guard | no false generalisation | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is exactly the canonical naturality shape used by `Polynomial.hasseDeriv_map`, `Polynomial.derivative_map` and `MvPolynomial.pderiv_map`.

### Proof strategy — `MvPolynomial.hasseDeriv_map`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | proof is `ext; simp [coeff_hasseDeriv, coeff_map]`, identical in shape to mathlib's `Polynomial.hasseDeriv_map` (`ext; simp [hasseDeriv_coeff]`); an `induction_on'` proof also works (evidence item 3) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_map`

[A] Lean-Finder       "multivariate Hasse derivative commutes with base change of coefficients MvPolynomial.map"   `MvPolynomial.pderiv_map`, `Polynomial.derivativeFinsupp_map`, Weierstrass-curve base-change lemmas; no multivariate Hasse
[B] Loogle            `"hasseDeriv_map"`   `Polynomial.hasseDeriv_map` (univariate, `@[simp]`), `LaurentSeries.hasseDeriv_map`; nothing for `MvPolynomial`
[C] LeanSearch        "Hasse derivative of multivariate polynomial commutes with map of coefficients along ring hom"   `Polynomial.derivativeFinsupp_map`, `Polynomial.iterate_derivative_map`, `Polynomial.derivative_map`, `MvPolynomial.pderiv_map`, `Polynomial.sumIDeriv_map`; no multivariate Hasse
[D] Grep mathlib src  `hasseDeriv_map`, `map_hasseDeriv`, `pderiv_map`, `MvPolynomial.hasseDeriv` across `.lake/packages/mathlib/Mathlib`: only Algebra/Polynomial/HasseDeriv.lean:128, RingTheory/LaurentSeries.lean:171, Algebra/MvPolynomial/PDeriv.lean:136
[E] Name pattern      `MvPolynomial.hasseDeriv_map` (grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard general form (base change of HS derivations; univariate/partial-derivative analogues).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); `Polynomial.hasseDeriv_map` and `MvPolynomial.pderiv_map` are the templates, and the parent operator itself is absent.

### Normal-form check — `MvPolynomial.hasseDeriv_map`

Equivalent formalisms this statement could take: `hasseDeriv d (map f P) = map f (hasseDeriv d P)`; the reverse orientation `map f (hasseDeriv d P) = hasseDeriv d (map f P)`; operator form `(hasseDeriv d).toAddMonoidHom.comp (map f).toAddMonoidHom = ...`.
Does mathlib already have a canonical form for this idea? yes: `Polynomial.hasseDeriv_map`, `Polynomial.derivative_map`, `MvPolynomial.pderiv_map` all state `op (map f p) = map f (op p)`.
Our statement is stated against the canonical form? yes.
RHS convention respected? yes (pushes `map` outward, as mathlib's `@[simp]` univariate version does).

### Syntactic generality — `MvPolynomial.hasseDeriv_map`

Alternative restatements attempted:
- current (explicit `f d P`, mirrors `Polynomial.hasseDeriv_map`)
- implicit arguments (mirrors `MvPolynomial.pderiv_map`)
- reverse orientation
- `@[simp]` attribute added
Chosen restatement: current statement, plus `@[simp]`.
Justification: explicit arguments match the univariate mathlib lemma and allow `rw [← hasseDeriv_map]` (used at Roth/MainLemma.lean:492); `@[simp]` matches `Polynomial.hasseDeriv_map` and lets all 6 `simp`/`simpa` call sites drop the explicit argument (evidence items 4–5 show it closes call-site shapes and composite `map`s without looping).

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_map`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `[CommSemiring S]` | yes | required by `MvPolynomial σ S` |
| 3 | `f`, `d`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (add `@[simp]`, an attribute change only)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (with `@[simp]` attribute)

### Call sites — `MvPolynomial.hasseDeriv_map`

Internal use count: 7 (outside the declaring file)
External-to-file callers: 3 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:409 | `simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ...]` (`eval_hasseDeriv_sub_eq_zero`) |
| Roth/MainLemma.lean:489 | `simpa [hasseDeriv_map] using hkev` (`exists_hasseDeriv_index_eval_bound_aux`) |
| Roth/MainLemma.lean:492 | `rw [← hasseDeriv_map]` (same) |
| Roth/MainLemma.lean:495 | `simpa [hasseDeriv_map] using hbound i k` (same) |
| Roth/Theta.lean:524 | `Matrix.ext fun μ ν ↦ by simp [hasseDeriv_map]` (`mapped_det_ne_zero_aux`) |
| Roth/Theta.lean:580 | `simp only [hasseDeriv_map] at hlower` (`index_le_lem6`) |
| Roth/Separation.lean:533 | `rw [..., Matrix.of_apply, hasseDeriv_map]` (`exists_rat_factors_det_hasseDeriv_aux`) |

Inline-derivation grep: (none) — `grep -n "hasseDeriv .* (map"` over `Roth/` finds only statements consumed via `hasseDeriv_map`; no proof re-derives the commutation by `ext`/`coeff_hasseDeriv`.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_map` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable — `MvPolynomial.hasseDeriv` is not in mathlib (`Polynomial.hasseDeriv_map` is univariate and would need the `uniqueAlgEquiv` compatibility plus a `Fin 1`/`Unique` restriction).
  - Result: fails

Attempt 2: `ext e; simp [coeff_hasseDeriv, coeff_map]` from the parent's API.
  - Result: succeeds, but this is the lemma's own proof (ext + coefficient computation), exactly as mathlib proves `Polynomial.hasseDeriv_map`; plain `simp` without the lemma fails (evidence item 2).

Conclusion: NOT-COMPOSABLE (from mathlib; the operator is new)

## Verdict: `MvPolynomial.hasseDeriv_map`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): Hasse derivatives are defined over `ℤ` via binomial coefficients and so commute with every coefficient map (Wikipedia; arXiv 2111.07572, 2205.00342, 1310.6482); abstractly, base change of HS derivations (Vojta, arXiv math/0407113, Lemma 5.5).
- Generality analysis (Phase 4): MAXIMALLY GENERAL; Phase 4c: no modern-idiom move.
- Mathlib search (Phase 5): not in mathlib; templates `Polynomial.hasseDeriv_map`, `MvPolynomial.pderiv_map`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The parent `MvPolynomial.hasseDeriv` was assessed YES-but-generalise-first (multivariate Hasse derivative absent from mathlib; ship with `Finsupp.choose` coefficients). Every derivative-like operator in mathlib carries a naturality-in-coefficients lemma (`Polynomial.derivative_map`, `Polynomial.iterate_derivative_map`, `Polynomial.hasseDeriv_map`, `MvPolynomial.pderiv_map`, `LaurentSeries.hasseDeriv_map`); this is that lemma for the multivariate Hasse derivative, and it is the project's main tool for moving between `ℤ`, `ℚ` and `ℝ` coefficients (7 call sites in 3 files). The statement is maximally general (no hypotheses, morphism type forced by `MvPolynomial.map`) and in mathlib's canonical orientation; the parent's `Finsupp.choose` rename affects only the proof.

The only change is to add `@[simp]`, matching the univariate `Polynomial.hasseDeriv_map`; evidence shows it is loop-free and closes call-site shapes. This is an attribute, not a restatement, so the bucket is YES-add-as-is.

WHY add it: `Mathlib/Algebra/MvPolynomial/` has `pderiv_map` but no Hasse derivative, so there is no lemma letting `simp` push `MvPolynomial.map` through `Δ_d`. The fact that Hasse derivatives are "defined over `ℤ`" is the reason they exist in positive characteristic (polynomial method, DKSS multiplicities, mod-`p` reductions) and in Diophantine approximation (integer polynomials evaluated over `ℝ`, as in Roth's lemma); each such argument needs `Δ_d (f_* P) = f_* (Δ_d P)`. With it, `eval_map`, `eval₂_map`, `map_map` and the `RingHom.map_det` lemmas compose with Hasse derivatives, and it is the multivariate counterpart of `Polynomial.hasseDeriv_map`, which it specialises to through the `uniqueAlgEquiv` compatibility lemma.
Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent)
Proposed PR title:            "feat(Algebra/MvPolynomial): multivariate Hasse derivatives"
PR grouping (if applicable):  ship with `Finsupp.choose`, `MvPolynomial.hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`, `coeff_hasseDeriv`, `hasseDeriv_zero(_apply)`, `hasseDeriv_C`, `hasseDeriv_rename`, in one PR.
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.hasseDeriv_map` — confirm no easy further weakening (expected none)
  - [ ] `/cleanup Roth/HasseDeriv.lean MvPolynomial.hasseDeriv_map` — full audit + diff gates (add `@[simp]`)
  - [ ] Pick a mathlib reviewer based on `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/HasseDeriv.lean` recent commits

---

## Next step

Ship unchanged as `@[simp] MvPolynomial.hasseDeriv_map` in the parent's PR to new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean; locally keep it, optionally adding `@[simp]` and simplifying the `simp [hasseDeriv_map]` call sites (Roth/MainLemma.lean:409,489,495, Roth/Theta.lean:524,580).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_map/variants.lean` (compiles with `lake env lean`, no errors or warnings): (1) the statement re-proved by `ext; simp [coeff_hasseDeriv, coeff_map]`; (2) `fail_if_success simp` confirms plain `simp` cannot prove it without the lemma; (3) an alternative `induction_on'` proof via `map_monomial`; (4) with `attribute [local simp] hasseDeriv_map`, `simp [map_map]` closes `Δ_d (g_* (f_* P)) = (g ∘ f)_* (Δ_d P)` without looping; (5) with the simp attribute, plain `simp` closes the call-site shape `eval z (Δ_d (map (Int.castRingHom S) P)) = eval₂ (Int.castRingHom S) z (Δ_d P)` (cf. Roth/MainLemma.lean:489).
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv/weaken_semiring_fails.lean` (`CommSemiring` forced).
- Loogle `"hasseDeriv_map"`: `Polynomial.hasseDeriv_map`, `LaurentSeries.hasseDeriv_map` only; LeanSearch / Lean-Finder: univariate derivative maps and `MvPolynomial.pderiv_map` only; mathlib grep: as recorded in [D]. `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1-3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseDeriv_map Roth/` (Used-by, call sites) and `grep -n "hasseDeriv .* (map"` (inline derivations: none); grep of `.mathlib-quality/references/clean.tex` for coefficient rings and Lean notes.
