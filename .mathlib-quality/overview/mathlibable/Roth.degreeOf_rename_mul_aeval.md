---
decl: Roth.degreeOf_rename_mul_aeval
file: Roth/Separation.lean
line: 197
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The partial-degree identity deg_{x_j}(U(x_τ)V(x_*)) = deg_{x_j} U for V ≠ 0 is absent from mathlib, as are its two building blocks (degreeOf of a rename outside the range is 0; degreeOf (p*q) = degreeOf p when q ≠ 0 avoids the variable). The project form over-assumes CommRing + IsDomain (CommSemiring + NoZeroDivisors suffices, verified) and should ship as the Sum.inl/Sum.inr form plus the two API lemmas.
action: Upstream degreeOf_rename_eq_zero_of_notMem_range (Mathlib/Algebra/MvPolynomial/Degrees.lean, after degreeOf_rename_of_injective), degreeOf_mul_of_degreeOf_eq_zero_right and degreeOf_inl_rename_inl_mul_rename_inr (Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean, after degreeOf_mul_eq), all proved in evidence weaken.lean; locally weaken to CommSemiring + NoZeroDivisors with the 2-rewrite proof, keeping its single call site Separation.lean:554.
---

# Roth.degreeOf_rename_mul_aeval

## Inventory entry

### `theorem Roth.degreeOf_rename_mul_aeval`
- **Type**: `∀ {τ : Type*} {R : Type*} [CommRing R] [IsDomain R] (U : MvPolynomial τ R) {V : Polynomial R}, V ≠ 0 → ∀ (j : τ), degreeOf (some j) (rename some U * Polynomial.aeval (X none) V) = degreeOf j U` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check` in the evidence file)
- **What**: In `R[x_τ, x_*]` over a domain, for `V ≠ 0` the degree of the separated product `U(x_τ) V(x_*)` in a variable `x_j`, `j ∈ τ`, equals the degree of `U` in `x_j`.
- **How**: Case `U = 0` by `simp`. Otherwise `rw [degreeOf_mul_eq ...]` (nonzero factors from `rename_eq_zero_iff_of_injective` and `map_ne_zero_iff` with `Polynomial.toMvPolynomial_injective`), then `degreeOf_rename_of_injective (Option.some_injective τ)`; the remaining `degreeOf (some j) (aeval (X none) V) = 0` is closed by `simp [aeval_X_eq_rename, degreeOf, degrees_rename_of_injective ..., Multiset.mem_replicate]`.
- **Hypotheses**: `[CommRing R] [IsDomain R]` (section variables), `hV : V ≠ 0`.
- **Uses from project**: `Roth.aeval_X_eq_rename`
- **Used by**: `Roth.exists_det_eq_mul` in Roth/Separation.lean:554 (`rw [← degreeOf_rename_mul_aeval U hV j, ← hFUV]`, bounding `degreeOf j U` by the degree of the determinant `F`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 193–207, proof length 9 lines
- **Notes**: Twin of `Roth.degreeOf_none_rename_mul_aeval` (line 213), which handles the `none` variable. The `CommRing + IsDomain` section variables are stronger than needed: `CommSemiring + NoZeroDivisors` suffices (evidence (4), (5)).

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:554, in the proof of Lemma 2 `exists_det_eq_mul`).
- Wrapper of 1–2 mathlib calls? No as written: `degreeOf_mul_eq` + `degreeOf_rename_of_injective` + a 3-lemma `simp` to show `aeval (X none) V` does not involve `some j`. The last step is a missing mathlib lemma (degreeOf of a rename outside the range is 0).
- Does mathlib have it? No (Phase 5).
- Too specific? Borderline-specific (Option spelling, one call site), but it is the source's step "since the variables are disjoint and both factors are nonzero, the individual degrees of U, V equal the corresponding degrees of F" and has a twin lemma; inlining would duplicate the nonzero-ness bookkeeping.
- Well-chosen? Yes as a local lemma; typeclasses over-assumed (see Notes).
- Conclusion: `KEEP` (weaken to `CommSemiring + NoZeroDivisors`; re-prove from the API lemmas below).

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; qualified name `Roth.degreeOf_rename_mul_aeval` absent from mathlib (and `MvPolynomial.degreeOf_rename_mul_aeval` too). Not a glue lemma (9-line proof), so full workflow.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` elaborates with no errors)
- decl `Roth.degreeOf_rename_mul_aeval`: resolved at Roth/Separation.lean:197
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.degreeOf_rename_mul_aeval` is a theorem stating the following: let `R` be an integral domain, `U ∈ R[x_τ]` and `V ∈ R[y]` with `V ≠ 0`. View both inside `R[x_τ, x_*]`, `U` via the inclusion of variables and `V` via `y ↦ x_*`. Then for each `j ∈ τ`, `deg_{x_j}(U(x_τ) V(x_*)) = deg_{x_j} U`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the non-distinguished variables.
- `R : Type*`, `[CommRing R] [IsDomain R]` — coefficients.
- `U : MvPolynomial τ R`, `V : Polynomial R`, `j : τ`.

Hypotheses (Lean side):
- `hV : V ≠ 0` — needed: for `V = 0` the left side is `0` (evidence (6)).

Conclusion (math): `deg_{x_j}(U(x_τ)V(x_*)) = deg_{x_j} U`.

Conclusion (Lean): `degreeOf (some j) (rename some U * Polynomial.aeval (X none) V) = degreeOf j U`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a degree-bookkeeping helper for Lemma 2; no new structure, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 9
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | degree in x of product f(x)g(y) polynomials disjoint variables integral domain degree equals degree of f | partial | over a domain `deg_x(f(x)g(y)) = deg f` for `g ≠ 0` (view as polynomial in x over R[y]; leading coeff `a_n g(y) ≠ 0`) | sources (St Olaf, SFU worksheet 9, UCSD notes, UCI 120B) state only the one-variable `deg(fg) = deg f + deg g` over a domain; the two-block case is an immediate corollary, not stated as a named result |
| 2 | WebSearch (general form) | partial degree multivariate polynomial product integral domain deg_x(fg) = deg_x f + deg_x g | yes | `deg_{x_j}(fg) = deg_{x_j} f + deg_{x_j} g` for nonzero `f, g` over a domain | arXiv 2506.20985 states it explicitly; UTK "Polynomial Rings" notes; the project statement is this with `deg_{x_j} g = 0` |
| 3 | WebSearch (aliases / mathlib) | Mathlib MvPolynomial degreeOf rename mul lemma | no | — | surfaced `degreeOf_rename_of_injective`, `degreeOf_C_mul_le`, `degreeOf_mul_X_of_ne`, `vars_rename`; no product-with-disjoint-variables lemma and no degreeOf-outside-range lemma |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/*.tex` for "disjoint" / "individual degrees" | yes | clean.tex:435 "since the variables are disjoint and both factors are nonzero, the individual degrees of U,V equal the corresponding degrees of F" | exactly the project statement (and its `none` twin); used as obvious |
| 6 | nLab | polynomial ring / degree of a polynomial | no | — | nLab treats `A[X ⊔ Y] ≅ A[X] ⊗ A[Y]` (see sibling `Roth.coeff_rename_mul_aeval` report) but has no partial-degree statement |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept (elementary degree bookkeeping) |
| 8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry statement; Stacks uses degree additivity over domains only implicitly |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be posed as a question; Math.SE has many `deg(fg)=deg f+deg g` over domain threads, which is the general form |
| 10 | recent arXiv | arXiv 2506.20985 (surfaced by #2), arXiv 2402.14163 | yes | partial degree additivity over a domain | confirms the general form, no new variant |

### Literature summary (Phase 3)

Concept identified as: additivity of the partial degree `deg_{x_j}` under multiplication over a domain, specialised to a factor that does not involve `x_j` (disjoint variables).
Sources agree on the standard form: yes — `deg_{x_j}(fg) = deg_{x_j} f + deg_{x_j} g` for nonzero `f, g` over a domain; with disjoint variables the second summand is `0`.
Most general standard form: for `R` with no zero divisors, `f, g ∈ R[X]`, `g ≠ 0`, `x_j` not occurring in `g`: `deg_{x_j}(fg) = deg_{x_j} f`; in the two-block spelling `p ∈ R[X]`, `q ∈ R[Y]`, `q ≠ 0`, `j ∈ X`: `deg_{x_j}(p(x)q(y)) = deg_{x_j} p`.
Generality dimensions where the literature varies:
  - coefficients: integral domain (textbooks) vs no zero divisors (the proof only needs the leading coefficient product to be nonzero); the most general is a commutative semiring without zero divisors.
  - second block: one variable (project) vs arbitrary set `Y` (`Sum` form).
Disagreement with the literature: none mathematically; the project assumes `CommRing + IsDomain` and a one-variable second block.

### Generality analysis — `Roth.degreeOf_rename_mul_aeval`

Literature-standard form (from Phase 3): `[CommSemiring R] [NoZeroDivisors R]`, `q ≠ 0`: `degreeOf (Sum.inl j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j p`; underlying lemma `q ≠ 0 → degreeOf i q = 0 → degreeOf i (p * q) = degreeOf i p`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing R]` | commutative ring | commutative semiring | yes | no subtraction used; verified (evidence (4), (5)) |
| 2 | `[IsDomain R]` | integral domain | `NoZeroDivisors R` | yes | `degreeOf_mul_eq` needs only `NoZeroDivisors`; verified (evidence (4), (5)); cannot be dropped entirely (`2X · 2 = 0` over `ZMod 4`) |
| 3 | `hV : V ≠ 0` | required | required | no | for `V = 0` the LHS is `0` (evidence (6)) |
| 4 | second block `{none}`, `V : Polynomial R` | one variable | arbitrary `τ` (`Sum` form) | yes (restatement) | verified: `degreeOf_inl_rename_inl_mul_rename_inr` compiles (evidence (3)) |
| 5 | `τ : Type*` | arbitrary | arbitrary | no | `Fintype`/`DecidableEq` already omitted |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (typeclasses `CommRing → CommSemiring`, `IsDomain → NoZeroDivisors`, second block `Option → Sum`), all verified clean with `lean_diagnostic_messages` (evidence (3)–(5)).
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem MvPolynomial.degreeOf_rename_eq_zero_of_notMem_range {f : σ → τ} {i : τ}
    (hi : i ∉ Set.range f) (p : MvPolynomial σ R) : degreeOf i (rename f p) = 0

theorem MvPolynomial.degreeOf_mul_of_degreeOf_eq_zero_right [NoZeroDivisors R]
    {p q : MvPolynomial σ R} {i : σ} (hq : q ≠ 0) (hi : degreeOf i q = 0) :
    degreeOf i (p * q) = degreeOf i p

theorem MvPolynomial.degreeOf_inl_rename_inl_mul_rename_inr [NoZeroDivisors R]
    (p : MvPolynomial σ R) {q : MvPolynomial τ R} (hq : q ≠ 0) (j : σ) :
    degreeOf (Sum.inl j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j p
```

Cost of restatement: CHEAP — all three proved in 3–6 lines each in the evidence file; the project lemma then becomes a single `rw` with two of them.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | only `V ≠ 0`, a genuine hypothesis | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | statement about a concrete degree function | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | yes | `CommRing + IsDomain` → `CommSemiring + NoZeroDivisors` (matches `degreeOf_mul_eq`) | usable over `ℕ`, `ℝ≥0` and all semiring settings of `NoZeroDivisors.lean` |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general? | yes | second block `Option`/one variable → arbitrary `τ` (`Sum` form) | general disjoint-variables degree API, paired with the `Sum` coefficient lemma proposed in the `Roth.coeff_rename_mul_aeval` report |
| 8 | Concrete-via-abstract? | yes | after `degreeOf_mul_eq` the proof only uses that `aeval (X none) V` does not involve `some j` and is nonzero; the abstract content is `degreeOf_mul_of_degreeOf_eq_zero_right` + `degreeOf_rename_eq_zero_of_notMem_range` | the project lemma (and its twin `degreeOf_none_rename_mul_aeval`) become 1–2 line corollaries |
| 9 | False-generalisation guard | no | all proposals specialise back to the exact project statement (evidence (4) re-derives it) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the three lemmas in Phase 4b, with the Option statement as a corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: `degreeOf_rename_eq_zero_of_notMem_range` complements `degreeOf_rename_of_injective` and `vars_rename`; `degreeOf_mul_of_degreeOf_eq_zero_right` is the `degreeOf` counterpart of the project's `hasseDeriv_mul_of_degreeOf_eq_zero` pattern and of `degreeOf_mul_X_of_ne` (which handles only `q = X j`).
  - Real mathematical improvement: the degree claim is separated from the Option/aeval encoding, so it applies to any renaming into disjoint variables.

### Proof strategy — `Roth.degreeOf_rename_mul_aeval`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `degreeOf_rename_eq_zero_of_notMem_range`, `degreeOf_mul_of_degreeOf_eq_zero_right` (evidence (1), (2)); replaces the `by_cases hU` split and the `simp [degreeOf, degrees_rename_of_injective, Multiset.mem_replicate]` unfolding | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: `rw [degreeOf_mul_of_degreeOf_eq_zero_right hV' (aeval_X_eq_rename ▸ degreeOf_rename_eq_zero_of_notMem_range ..), degreeOf_rename_of_injective]` (evidence (4)).
  - Cost: CHEAP
  - Missing mathlib API (if any): the two helper lemmas above.
  - Would refactoring make the proof strictly shorter / cleaner? yes (no case split, no unfolding to multisets)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.degreeOf_rename_mul_aeval`

[A] Lean-Finder       "degree in variable i of product p * q equals degree of p when q is nonzero and does not involve variable i"   no hit for the statement: returned `degreeOf_mul_X_of_ne`, `degreeOf_mul_C_le`, `degreeOf_mul_eq`, `degreeOf_mul_X_eq_degreeOf_add_one_iff`, `degreeOf_C_mul` (building blocks only)
[B] Loogle            `MvPolynomial.degreeOf _ (MvPolynomial.rename _ _ * _)`   no hits
[C] LeanSearch        "degreeOf of rename f p is zero when variable is not in the range of f"   no hit: `rename`, `degreeOf_rename_of_injective`, `killCompl`, `pderiv_rename`
[D] Grep mathlib src  `degreeOf` across Algebra/MvPolynomial/{Degrees,Variables,NoZeroDivisors,Equiv}.lean and RingTheory/MvPolynomial; `degreeOf_rename_eq_zero`, `degreeOf_mul_of_degreeOf_eq_zero`, `degreeOf_inl`, `notMem_range`, `degreeOf_eq_zero_of`   only `degreeOf_rename_of_injective` (Degrees.lean:419), `degreeOf_mul_eq` (NoZeroDivisors.lean:43), `mem_vars_iff_degreeOf_ne_zero` (Variables.lean:148), `degreeOf_mul_X_of_ne` (Degrees.lean:323); no product-disjoint lemma, no outside-range lemma
[E] Name pattern      lean_local_search / grep for the three proposed names   free in mathlib

Searched for both:
  - the user's current form (Option / `aeval (X none)`): not in mathlib.
  - the literature-standard form (`Sum` form; general `q` not involving `i`): not in mathlib.

Concluded: found building blocks (`degreeOf_mul_eq`, `degreeOf_rename_of_injective`, `mem_vars_iff_degreeOf_ne_zero`, `vars_rename`, `rename_eq_zero_iff_of_injective`, `Polynomial.toMvPolynomial_injective`); no statement in either form.

### Normal-form check — `Roth.degreeOf_rename_mul_aeval`

Equivalent formalisms: (a) the project equation; (b) `degreeOf (some j) (rename some U * rename (fun _ ↦ none) ((uniqueAlgEquiv R Unit).symm V))`; (c) the `Sum` form; (d) via `optionEquivLeft`/`finSuccEquiv` coefficients.
Does mathlib already have a canonical form? no dedicated one; `degreeOf_rename_of_injective` uses `degreeOf (f i) (rename f p)`, which (a)/(c) follow.
Is our statement stated against the canonical form? yes — LHS `degreeOf (some j) (...)`, RHS the simpler `degreeOf j U`.
RHS convention respected? yes

### Syntactic generality — `Roth.degreeOf_rename_mul_aeval`

Alternative restatements attempted:
- `CommSemiring + NoZeroDivisors` version (evidence (4), (5)): compiles.
- `Sum` form (evidence (3)): compiles.
- general `degreeOf_mul_of_degreeOf_eq_zero_right` (evidence (2)): compiles.

Chosen restatement: for mathlib, the general product lemma + outside-range lemma + `Sum` corollary; for the project, the Option equation with weakened typeclasses (its call site `exists_det_eq_mul` already has `F = rename some U * aeval (X none) V`).
Justification: the general product lemma is applicable by `rw` at any site with a factor not involving the variable; the Option form is what the project's call site rewrites along.

### Superfluous-argument audit — `Roth.degreeOf_rename_mul_aeval`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing R]` | no (as ring) | `CommSemiring` suffices (evidence (4), (5)) |
| 2 | `[IsDomain R]` | partially | only `NoZeroDivisors` is needed (`Nontrivial` not used) |
| 3 | `hV : V ≠ 0` | yes | counterexample evidence (6) |
| 4 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (general product lemma + `Sum` form for mathlib)
Superfluous arguments: 2 to weaken (`CommRing → CommSemiring`, `IsDomain → NoZeroDivisors`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.degreeOf_rename_mul_aeval`

Internal use count: 0 outside the declaring file; 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:554 | `rw [← degreeOf_rename_mul_aeval U hV j, ← hFUV]` in `exists_det_eq_mul` (Lemma 2) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `degreeOf_rename_mul_aeval`?):
  - Roth/Separation.lean:213–228 `degreeOf_none_rename_mul_aeval` repeats the same nonzero-factor bookkeeping and an inline `degreeOf none (rename some U) = 0` (the outside-range lemma, evidence (1)).
  - Roth/Separation.lean:155–163 `hasseDeriv_rename_mul_aeval` proves `degreeOf` of `rename some _` / `aeval (X none) _` is `0` at a foreign variable twice by the same `simp [degreeOf, degrees_rename_of_injective, Multiset.mem_replicate]` unfolding — again the outside-range lemma.

### Composition check (Phase 6)

Can `Roth.degreeOf_rename_mul_aeval` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [degreeOf_mul_eq hU' hV', degreeOf_rename_of_injective (Option.some_injective τ), h0, add_zero]`
  - Mathlib decls used: `degreeOf_mul_eq`, `degreeOf_rename_of_injective`, `rename_eq_zero_iff_of_injective`, `map_ne_zero_iff`, `Polynomial.toMvPolynomial_injective`
  - Result: partial — needs a `by_cases U = 0` split and `h0 : degreeOf (some j) (aeval (X none) V) = 0`, which mathlib has no lemma for (the project uses a 4-lemma `simp` unfolding to multisets).
  - Notes: that is the current 9-line proof, not a composition.

Attempt 2: with the proposed helpers (evidence (4))
  - Decls used: `degreeOf_mul_of_degreeOf_eq_zero_right`, `degreeOf_rename_eq_zero_of_notMem_range`, `degreeOf_rename_of_injective`, `Roth.aeval_X_eq_rename`
  - Result: succeeds as a single `rw`, but only after adding the two missing helpers.

Conclusion: NOT-COMPOSABLE (from current mathlib)

## Verdict: `Roth.degreeOf_rename_mul_aeval`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): standard partial-degree additivity over a domain (arXiv 2506.20985; textbook one-variable case), specialised to a factor in disjoint variables; the source uses it at clean.tex:435.
- Generality analysis (Phase 4): STRICTLY NARROWER. `CommRing + IsDomain → CommSemiring + NoZeroDivisors` and the `Sum` form, all verified to compile (evidence (3)–(5)).
- Mathlib search (Phase 5): not in mathlib in either form; building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE from current mathlib (missing the outside-range lemma).

**Rationale:**
Mathlib has additivity `degreeOf_mul_eq` and the injective-rename lemma `degreeOf_rename_of_injective`. It has nothing that says a variable outside the range of a renaming has degree 0 (only `vars_rename`, which needs a `mem_vars_iff_degreeOf_ne_zero` detour), and nothing that says multiplying by a nonzero factor not involving `x_i` keeps `deg_{x_i}` (only the special case `degreeOf_mul_X_of_ne` for `q = X j`). The project feels both gaps: this lemma, its twin `degreeOf_none_rename_mul_aeval`, and `hasseDeriv_rename_mul_aeval` (Separation.lean:155–163, 213–228) each re-prove "this renamed factor has degree 0 in a foreign variable" by unfolding `degreeOf` to multisets with `degrees_rename_of_injective` and `Multiset.mem_replicate`.

The Option-specific lemma should not ship as stated: it assumes `CommRing + IsDomain` where `CommSemiring + NoZeroDivisors` (the hypotheses of `degreeOf_mul_eq`) suffices, and it fixes the second block to one variable. The mathlib contribution is the two general helpers plus the `Sum`-form disjoint-variables corollary; the project statement is then a one-`rw` corollary (evidence (4)). With only one project call site, the Option form itself stays local.

Reason for the generalisation: both apply.
- LITERATURE-WEAKENING: coefficients from integral domain to `NoZeroDivisors` semiring; second block from one variable to arbitrary `τ`.
- MODERN-IDIOM: concrete-via-abstract (Q8) — after `degreeOf_mul_eq` the proof uses only "nonzero and not involving `some j`", captured by the general product lemma.

Proposed restatement:
```lean
theorem MvPolynomial.degreeOf_rename_eq_zero_of_notMem_range {f : σ → τ} {i : τ}
    (hi : i ∉ Set.range f) (p : MvPolynomial σ R) : degreeOf i (rename f p) = 0
theorem MvPolynomial.degreeOf_mul_of_degreeOf_eq_zero_right [NoZeroDivisors R]
    {p q : MvPolynomial σ R} {i : σ} (hq : q ≠ 0) (hi : degreeOf i q = 0) :
    degreeOf i (p * q) = degreeOf i p
theorem MvPolynomial.degreeOf_inl_rename_inl_mul_rename_inr [NoZeroDivisors R]
    (p : MvPolynomial σ R) {q : MvPolynomial τ R} (hq : q ≠ 0) (j : σ) :
    degreeOf (Sum.inl j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j p
```
All three already compile in evidence/Roth.degreeOf_rename_mul_aeval/weaken.lean.
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- `degreeOf_rename_eq_zero_of_notMem_range` completes the `degreeOf`/`rename` API next to `degreeOf_rename_of_injective` (and gives the inr-variable analogue of the `Sum` corollary for free)
- `degreeOf_mul_of_degreeOf_eq_zero_right` generalises `degreeOf_mul_X_of_ne` from `X j` to any nonzero factor avoiding the variable (under `NoZeroDivisors`)
- the `Sum` corollary pairs with the `coeff_rename_inl_mul_rename_inr` lemma proposed in the `Roth.coeff_rename_mul_aeval` report as a disjoint-variables API

Proposed mathlib location: `Mathlib/Algebra/MvPolynomial/Degrees.lean` (outside-range lemma, after `degreeOf_rename_of_injective`); `Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean` (product lemma and `Sum` corollary, after `degreeOf_mul_eq`).
Proposed PR title: "feat(Algebra/MvPolynomial): degreeOf of products in disjoint variables"
PR grouping: ship with the disjoint-variables coefficient lemma from `Roth.coeff_rename_mul_aeval`; the twin `Roth.degreeOf_none_rename_mul_aeval` becomes a corollary of the same helpers plus `Roth.degreeOf_uniqueAlgEquiv_symm` (itself YES-add-as-is).
Local refactor: weaken the project lemma to `[CommSemiring R] [NoZeroDivisors R]` (move it out of `section Domain`) and use the evidence (4) proof; the single call site Separation.lean:554 is unchanged.
Next action: run `/generalise Roth.degreeOf_rename_mul_aeval` with the targets above, then `/cleanup` and open the PR.

---

## Next step

Add `degreeOf_rename_eq_zero_of_notMem_range` and `degreeOf_mul_of_degreeOf_eq_zero_right`, re-prove the project lemma from them under `CommSemiring + NoZeroDivisors` (call site Separation.lean:554 unchanged; reuse in `degreeOf_none_rename_mul_aeval` and `hasseDeriv_rename_mul_aeval`), then upstream the two helpers and the `Sum` corollary to `Mathlib/Algebra/MvPolynomial/{Degrees,NoZeroDivisors}.lean`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.degreeOf_rename_mul_aeval/weaken.lean` (imports `Roth.Separation`), checked with `lean_diagnostic_messages` after one round of fixes; final version: no errors, no warnings, only the `#check` info. Contents: (0) `#check @Roth.degreeOf_rename_mul_aeval` shows `[CommRing R] [IsDomain R]`. (1) `degreeOf_rename_eq_zero_of_notMem_range` compiles over `CommSemiring`. (2) `degreeOf_mul_of_degreeOf_eq_zero_right` compiles under `NoZeroDivisors`. (3) `Sum` form `degreeOf_inl_rename_inl_mul_rename_inr` compiles from (1), (2). (4) The project statement under `CommSemiring + NoZeroDivisors` compiles as one `rw` from (1), (2). (5) The original proof body, verbatim, compiles under `CommSemiring + NoZeroDivisors`. (6) `V = 0` makes the LHS `0` (so `hV` is needed).
- Searches: 3 WebSearch queries, Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no hits), mathlib greps for `degreeOf` lemmas and the proposed names (free), local references grep (clean.tex:424, 435). ChatGPT MCP n/a (not configured in this session).
