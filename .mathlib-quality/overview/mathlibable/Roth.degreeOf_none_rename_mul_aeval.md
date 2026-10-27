---
decl: Roth.degreeOf_none_rename_mul_aeval
file: Roth/Separation.lean
line: 213
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The identity deg_{x_*}(U(x_τ)V(x_*)) = natDegree V for U ≠ 0 is absent from mathlib, as are its building blocks (degreeOf of a rename outside the range is 0; degreeOf (p*q) = degreeOf q when p ≠ 0 avoids the variable; degreeOf i (p.toMvPolynomial i) = natDegree p); the project form over-assumes CommRing + IsDomain (CommSemiring + NoZeroDivisors suffices, verified) and should ship as those API lemmas plus a Sum.inr corollary.
action: Upstream Polynomial.degreeOf_toMvPolynomial_self (Mathlib/Algebra/MvPolynomial/Equiv.lean, section toMvPolynomial, after degreeOf_uniqueAlgEquiv_symm lands) together with the twin's degreeOf_rename_eq_zero_of_notMem_range, a left-factor degreeOf_mul_of_degreeOf_eq_zero_left and degreeOf_inr_rename_inl_mul_rename_inr (Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean), all proved in evidence weaken.lean; locally weaken to CommSemiring + NoZeroDivisors with the 2-step proof, keeping its single call site Separation.lean:557.
---

# Roth.degreeOf_none_rename_mul_aeval

## Inventory entry

### `theorem Roth.degreeOf_none_rename_mul_aeval`
- **Type**: `∀ {τ : Type*} {R : Type*} [CommRing R] [IsDomain R] {U : MvPolynomial τ R}, U ≠ 0 → ∀ (V : Polynomial R), degreeOf none (rename some U * Polynomial.aeval (X none) V) = V.natDegree` (section `[Fintype τ] [DecidableEq τ]` omitted; confirmed by `#check` in the evidence file)
- **What**: In `R[x_τ, x_*]` over a domain, for `U ≠ 0` the degree of the separated product `U(x_τ) V(x_*)` in the distinguished variable `x_*` equals `natDegree V`.
- **How**: Case `V = 0` by `simp`. Otherwise `rw [degreeOf_mul_eq ...]` (nonzero factors from `rename_eq_zero_iff_of_injective` and `map_ne_zero_iff` with `Polynomial.toMvPolynomial_injective`), an inline `show degreeOf none (rename some U) = 0` closed by `simp [degreeOf, degrees_rename_of_injective (Option.some_injective τ)]`, `zero_add`, `Roth.aeval_X_eq_rename`; finally `degreeOf_rename_of_injective` (renaming `Unit → Option τ`, `_ ↦ none`) chained with `Roth.degreeOf_uniqueAlgEquiv_symm`.
- **Hypotheses**: `[CommRing R] [IsDomain R]` (section variables), `hU : U ≠ 0`.
- **Uses from project**: `Roth.aeval_X_eq_rename`, `Roth.degreeOf_uniqueAlgEquiv_symm`
- **Used by**: `Roth.exists_det_eq_mul` in Roth/Separation.lean:557 (`rw [← degreeOf_none_rename_mul_aeval hU V, ← hFUV]`, bounding `natDegree V` by the `x_none`-degree of the determinant `F`). No other uses in `Roth/` (grep over `Roth/` for the bare name, which covers in-namespace calls).
- **Visibility**: public
- **Lines**: 210–226, proof length 13 lines
- **Notes**: Twin of `Roth.degreeOf_rename_mul_aeval` (line 197, assessed YES-but-generalise-first). `CommSemiring + NoZeroDivisors` suffices (evidence (5), (6)). `hV` is not needed (`V = 0` gives `0 = 0`), `hU` is (evidence (7)).

## Junk check (Step 8)
- Used anywhere? Yes, once (Separation.lean:557, Lemma 2 `exists_det_eq_mul`).
- Wrapper of 1–2 mathlib calls? No: `degreeOf_mul_eq` + a multiset unfolding for the outside-range fact + `degreeOf_rename_of_injective` + the project's `degreeOf_uniqueAlgEquiv_symm`. Two of these steps are missing mathlib lemmas.
- Does mathlib have it? No (Phase 5).
- Too specific? Option spelling with one call site, but it is literally the source step clean.tex:435 and pairs with its twin; inlining would duplicate the nonzero bookkeeping inside an already long proof.
- Well-chosen? Yes as a local lemma; typeclasses over-assumed.
- Conclusion: `KEEP` (weaken to `CommSemiring + NoZeroDivisors`, re-prove from the API lemmas).

## Mathlibable assessment (Step 9)

Pre-filter: not private; not `_aux`; docstring not internal/auxiliary; Step 8 = KEEP; `Roth.degreeOf_none_rename_mul_aeval` and `MvPolynomial.degreeOf_none_rename_mul_aeval` absent from mathlib (grep). 13-line proof, not a glue lemma, so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (per brief; the evidence file importing `Roth.Separation` elaborates with no errors)
- decl `Roth.degreeOf_none_rename_mul_aeval`: resolved at Roth/Separation.lean:213
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.degreeOf_none_rename_mul_aeval` is a theorem stating the following: let `R` be an integral domain, `U ∈ R[x_τ]` nonzero and `V ∈ R[y]` arbitrary. View both in `R[x_τ, x_*]`, `U` via the inclusion of variables and `V` via `y ↦ x_*`. Then `deg_{x_*}(U(x_τ) V(x_*)) = deg V`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — non-distinguished variables.
- `R : Type*`, `[CommRing R] [IsDomain R]` — coefficients.
- `U : MvPolynomial τ R`, `V : Polynomial R`.

Hypotheses (Lean side):
- `hU : U ≠ 0` — needed (evidence (7): `U = 0`, `V = X` gives `0 ≠ 1`).

Conclusion (math): `deg_{x_*}(U(x_τ)V(x_*)) = deg V` (with `deg 0 = 0`).

Conclusion (Lean): `degreeOf none (rename some U * Polynomial.aeval (X none) V) = V.natDegree`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: degree-bookkeeping helper for Lemma 2; no new structure, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 13
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | degree in y of product f(x) g(y) equals degree of g polynomial ring two variables integral domain | partial | view `k[x,y] = R[y]` with `R = k[x]`; `deg_y(fg) = deg_y f + deg_y g` over a domain | UCSD 103B notes, Judson AATA 17.1, UTK, SFU worksheet 9; only the one-variable rule is stated, the disjoint-variable case is the immediate corollary |
| 2 | WebSearch (general form) | univariate polynomial embedded in multivariate polynomial ring degree in the variable equals degree | partial | partial degree of `p(x_i)` in `x_i` equals `deg p` | Mathlib `degreeOf` docs, Isabelle AFP Cring_Multivariable_Poly (multivariate as univariate over smaller ring); stated as obvious, never as a named result |
| 3 | WebSearch (aliases / mathlib) | Mathlib Polynomial.toMvPolynomial degreeOf natDegree | no | — | no degree lemma for `toMvPolynomial` surfaced; confirms the API gap |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "disjoint" / "individual degrees" | yes | clean.tex:435 "since the variables are disjoint and both factors are nonzero, the individual degrees of U,V equal the corresponding degrees of F" | exactly this statement (the `V` half) and its twin (the `U` half) |
| 6 | nLab | polynomial ring / degree of a polynomial | no | — | nLab has `A[X ⊔ Y] ≅ A[X] ⊗ A[Y]` but no partial-degree statement (same finding as the twin report) |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept (elementary degree bookkeeping) |
| 8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry statement; degree additivity over domains is used implicitly only |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be posed; the general form `deg(fg)=deg f+deg g` over a domain is the standard Math.SE thread |
| 10 | recent arXiv | arXiv 2506.20985 (partial-degree additivity, found by the twin's search) | yes | `deg_{x_j}(fg) = deg_{x_j} f + deg_{x_j} g` over a domain | no new variant |

### Literature summary (Phase 3)

Concept identified as: additivity of the partial degree `deg_{x_i}` under multiplication over a domain, with a factor not involving `x_i`, plus the trivial identification `deg_{x_i} p(x_i) = deg p`.
Sources agree on the standard form: yes — `deg_{x_i}(fg) = deg_{x_i} f + deg_{x_i} g` for nonzero `f, g` over a domain.
Most general standard form: for `R` with no zero divisors, `p ≠ 0` not involving `x_i`: `deg_{x_i}(pq) = deg_{x_i} q`; two-block spelling `p ∈ R[X] \ 0`, `q ∈ R[Y]`, `j ∈ Y`: `deg_{y_j}(p(x)q(y)) = deg_{y_j} q`; and `deg_{x_i}(p(x_i)) = deg p` over any commutative semiring.
Generality dimensions where the literature varies:
  - coefficients: integral domain vs no zero divisors; most general is a commutative semiring without zero divisors.
  - second block: one variable (project, `Polynomial R`) vs an arbitrary set `Y` (`Sum` form).
Disagreement with the literature: none mathematically; the project over-assumes `CommRing + IsDomain`.

### Generality analysis — `Roth.degreeOf_none_rename_mul_aeval`

Literature-standard form (from Phase 3): `[CommSemiring R] [NoZeroDivisors R]`, `p ≠ 0`: `degreeOf (Sum.inr j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j q`; underlying `p ≠ 0 → degreeOf i p = 0 → degreeOf i (p * q) = degreeOf i q` and `degreeOf i (q.toMvPolynomial i) = q.natDegree`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommRing R]` | commutative ring | commutative semiring | yes | no subtraction used; verified (evidence (5), (6)) |
| 2 | `[IsDomain R]` | integral domain | `NoZeroDivisors R` | yes | `degreeOf_mul_eq` needs only `NoZeroDivisors`; verified (evidence (5), (6)); cannot be dropped (`2X` times `2` over `ZMod 4`) |
| 3 | `hU : U ≠ 0` | required | required | no | evidence (7) |
| 4 | second block `{none}`, `V : Polynomial R` | one variable | arbitrary `τ` (`Sum` form) | yes (restatement) | verified: `degreeOf_inr_rename_inl_mul_rename_inr` compiles (evidence (4)) |
| 5 | `τ : Type*` | arbitrary | arbitrary | no | `Fintype`/`DecidableEq` already omitted |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (`CommRing → CommSemiring`, `IsDomain → NoZeroDivisors`, second block `Option → Sum`), all verified clean with `lean_diagnostic_messages` (evidence (4)–(6)).
Proposed restatement (if STRICTLY NARROWER):

```lean
theorem Polynomial.degreeOf_toMvPolynomial_self (i : σ) (p : R[X]) :
    MvPolynomial.degreeOf i (p.toMvPolynomial i) = p.natDegree

theorem MvPolynomial.degreeOf_mul_of_degreeOf_eq_zero_left [NoZeroDivisors R]
    {p q : MvPolynomial σ R} {i : σ} (hp : p ≠ 0) (hi : degreeOf i p = 0) :
    degreeOf i (p * q) = degreeOf i q

theorem MvPolynomial.degreeOf_inr_rename_inl_mul_rename_inr [NoZeroDivisors R]
    {p : MvPolynomial σ R} (hp : p ≠ 0) (q : MvPolynomial τ R) (j : τ) :
    degreeOf (Sum.inr j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j q
```
(plus the twin's `degreeOf_rename_eq_zero_of_notMem_range`.)

Cost of restatement: CHEAP — each proved in 3–5 lines in the evidence file; the project lemma becomes `rw` + `exact` (evidence (5)).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | only `U ≠ 0`, a genuine hypothesis | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | statement about a concrete degree function | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | yes | `CommRing + IsDomain` → `CommSemiring + NoZeroDivisors` | matches `degreeOf_mul_eq`'s hypotheses; usable over `ℕ` etc. |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general? | yes | second block one variable → arbitrary `τ` (`Sum` form) | disjoint-variables degree API with the twin's `Sum.inl` corollary |
| 8 | Concrete-via-abstract? | yes | after `degreeOf_mul_eq` the proof uses only "`rename some U` is nonzero and avoids `none`" and "`aeval (X none) V = V.toMvPolynomial none` has `none`-degree `natDegree V`"; these are the abstract lemmas (2), (1), (3) | the project lemma and its twin become 2-line corollaries |
| 9 | False-generalisation guard | no | every proposal specialises back to the exact project statement (evidence (5) re-derives it; `aeval (X none) V` is defeq to `V.toMvPolynomial none`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the lemmas in Phase 4b, the Option statement as a corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: `Polynomial.degreeOf_toMvPolynomial_self` gives the missing degree API for `Polynomial.toMvPolynomial` (which today has only `C`/`X`/injectivity/eval/rename lemmas); the product lemma generalises `degreeOf_mul_X_of_ne`-style special cases.
  - Real mathematical improvement: separates the degree claim from the Option/aeval encoding and supplies the one-variable degree identity mathlib lacks for `toMvPolynomial`.

### Proof strategy — `Roth.degreeOf_none_rename_mul_aeval`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `degreeOf_rename_eq_zero_of_notMem_range`, `degreeOf_mul_of_degreeOf_eq_zero_left`, `Polynomial.degreeOf_toMvPolynomial_self` (evidence (1)–(3)); removes the `by_cases hV` split, the inline `show ... by simp [degreeOf, degrees_rename_of_injective]`, and the `Unit`-rename chain | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: `rw [degreeOf_mul_of_degreeOf_eq_zero_left hU' (degreeOf_rename_eq_zero_of_notMem_range (by simp) U)]; exact degreeOf_toMvPolynomial_self none V` (evidence (5)).
  - Cost: CHEAP
  - Missing mathlib API (if any): the three helpers above (and `degreeOf_uniqueAlgEquiv_symm`, already proposed YES-add-as-is, which proves (3)).
  - Would refactoring make the proof strictly shorter / cleaner? yes (13 lines to 4, no case split, no multiset unfolding)

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.degreeOf_none_rename_mul_aeval`

[A] Lean-Finder       "degree of univariate polynomial p embedded as p(X i) in multivariate polynomials, degreeOf i equals natDegree p"   no hit: `degreeOf_eq_natDegree` (via `optionEquivLeft`), `degree_finSuccEquiv`, `natDegree_finSuccEquiv`, `degreeOf_def` — reverse-direction equivalence lemmas only
[B] Loogle            `MvPolynomial.degreeOf _ (Polynomial.toMvPolynomial _ _)`   no hits (twin's `MvPolynomial.degreeOf _ (MvPolynomial.rename _ _ * _)` also no hits)
[C] LeanSearch        "degreeOf i (Polynomial.aeval (X i) p) = p.natDegree"   no hit (`natDegree`, `degree_eq_natDegree`, `natDegree_X`)
[D] Grep mathlib src  all `toMvPolynomial` lemmas in Algebra/MvPolynomial/Equiv.lean:875–939 (C, X, eq_rename_comp, injective, inj, eval, aeval, rename) — no degree lemma; `degreeOf_toMvPolynomial`, `degreeOf_mul_of_degreeOf_eq_zero`, `degreeOf_rename_eq_zero`, `degreeOf_inr`, `degreeOf_none`, `degreeOf_aeval_X`   none present; only `degreeOf_rename_of_injective` (Degrees.lean:419), `degreeOf_mul_eq` (NoZeroDivisors.lean:43)
[E] Name pattern      grep for the proposed names (`lean_local_search` unavailable: ripgrep not installed)   free in mathlib

Searched for both:
  - the user's current form (Option / `aeval (X none)`): not in mathlib.
  - the literature-standard form (`Sum.inr` form; general product lemma; `toMvPolynomial` degree): not in mathlib.

Concluded: found building blocks (`degreeOf_mul_eq`, `degreeOf_rename_of_injective`, `Polynomial.toMvPolynomial_eq_rename_comp`, `Polynomial.toMvPolynomial_injective`, `vars_rename`, `mem_vars_iff_degreeOf_ne_zero`); no statement in either form.

### Normal-form check — `Roth.degreeOf_none_rename_mul_aeval`

Equivalent formalisms: (a) project equation with `Polynomial.aeval (X none) V`; (b) with `V.toMvPolynomial none` (defeq); (c) with `rename (fun _ ↦ none) ((uniqueAlgEquiv R Unit).symm V)`; (d) `Sum` form.
Does mathlib already have a canonical form? mathlib's named embedding is `Polynomial.toMvPolynomial i`; there is no degree lemma for it.
Is our statement stated against the canonical form? acceptable — (a) is defeq to (b), but for mathlib the `toMvPolynomial` spelling (b) is the canonical one.
RHS convention respected? yes (`natDegree V` on the RHS)

### Syntactic generality — `Roth.degreeOf_none_rename_mul_aeval`

Alternative restatements attempted:
- `CommSemiring + NoZeroDivisors` version (evidence (5), (6)): compiles.
- `Sum.inr` form (evidence (4)): compiles.
- general left-factor product lemma (evidence (2)) and `toMvPolynomial` degree lemma (evidence (3)): compile.

Chosen restatement: for mathlib, the general lemmas + `Sum.inr` corollary; for the project, the Option equation with weakened typeclasses (the call site already has `F = rename some U * aeval (X none) V`).
Justification: the general lemmas apply by `rw` anywhere; the Option form is what Separation.lean:557 rewrites along.

### Superfluous-argument audit — `Roth.degreeOf_none_rename_mul_aeval`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing R]` | no (as ring) | `CommSemiring` suffices (evidence (5), (6)) |
| 2 | `[IsDomain R]` | partially | only `NoZeroDivisors` is needed |
| 3 | `hU : U ≠ 0` | yes | evidence (7) |
| 4 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (prefer `toMvPolynomial` spelling in mathlib)
Syntactic generality: RESTATE (general product lemma + `toMvPolynomial` degree + `Sum.inr` form for mathlib)
Superfluous arguments: 2 to weaken (`CommRing → CommSemiring`, `IsDomain → NoZeroDivisors`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.degreeOf_none_rename_mul_aeval`

Internal use count: 0 outside the declaring file; 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:557 | `rw [← degreeOf_none_rename_mul_aeval hU V, ← hFUV]` in `exists_det_eq_mul` (Lemma 2) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `degreeOf_none_rename_mul_aeval`?):
  - Roth/Separation.lean:197–207 `degreeOf_rename_mul_aeval` (twin) repeats the nonzero-factor bookkeeping and the outside-range fact.
  - Roth/Separation.lean:155–163 `hasseDeriv_rename_mul_aeval` re-proves the outside-range fact twice by the same `simp [degreeOf, degrees_rename_of_injective, ...]` unfolding.
  - Roth/Theta.lean:426 uses `degreeOf_uniqueAlgEquiv_symm` directly for a one-variable `V'` (the `toMvPolynomial`-free half of evidence (3)).

### Composition check (Phase 6)

Can `Roth.degreeOf_none_rename_mul_aeval` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [degreeOf_mul_eq hU' hV', h0, zero_add, toMvPolynomial_eq_rename_comp, degreeOf_rename_of_injective ...]` then a coefficient argument for `degreeOf default ((uniqueAlgEquiv R Unit).symm V) = natDegree V`
  - Mathlib decls used: `degreeOf_mul_eq`, `rename_eq_zero_iff_of_injective`, `map_ne_zero_iff`, `Polynomial.toMvPolynomial_injective`, `degreeOf_rename_of_injective`
  - Result: partial — needs a `by_cases V = 0` split, `h0 : degreeOf none (rename some U) = 0` (no mathlib lemma; multiset unfolding) and the `uniqueAlgEquiv` degree identity (no mathlib lemma; 10-line proof in the project).
  - Notes: that is the current 13-line proof plus its 10-line dependency.

Attempt 2: with the proposed helpers (evidence (5))
  - Decls used: `degreeOf_mul_of_degreeOf_eq_zero_left`, `degreeOf_rename_eq_zero_of_notMem_range`, `Polynomial.degreeOf_toMvPolynomial_self`
  - Result: succeeds as `rw` + `exact`, only after adding the missing helpers.

Conclusion: NOT-COMPOSABLE (from current mathlib)

## Verdict: `Roth.degreeOf_none_rename_mul_aeval`

Verdict: YES-but-generalise-first

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): partial-degree additivity over a domain, specialised to a factor in disjoint variables, plus `deg_{x_i} p(x_i) = deg p`; the source uses it at clean.tex:435.
- Generality analysis (Phase 4): STRICTLY NARROWER. `CommRing + IsDomain → CommSemiring + NoZeroDivisors` and the `Sum.inr` form, all verified (evidence (4)–(6)).
- Mathlib search (Phase 5): not in mathlib in either form; building blocks only; `Polynomial.toMvPolynomial` has no degree lemma at all.
- Composition check (Phase 6): NOT-COMPOSABLE from current mathlib.

**Rationale:**
Mathlib has `degreeOf_mul_eq` and `degreeOf_rename_of_injective`, but three pieces are missing: a variable outside the range of a renaming has degree 0; multiplying by a nonzero factor avoiding `x_i` preserves `deg_{x_i}`; and `degreeOf i (p.toMvPolynomial i) = p.natDegree`. The last is a concrete gap in the `toMvPolynomial` section of Mathlib/Algebra/MvPolynomial/Equiv.lean (lines 875–939), which has `C`, `X`, injectivity, eval and rename lemmas but no degree lemma, while its siblings `finSuccEquiv` and `optionEquivLeft` do have `natDegree`/`degreeOf` lemmas. The project re-proves these facts by multiset unfolding here, in the twin and in `hasseDeriv_rename_mul_aeval`.

The Option form should not ship as stated: it assumes `CommRing + IsDomain` where `CommSemiring + NoZeroDivisors` suffices, and fixes the second block to one variable. The mathlib contribution is the helper lemmas plus the `Sum.inr` corollary, shipped together with the twin's `Sum.inl` corollary; the project statement then becomes a 2-step corollary (evidence (5)). With one call site the Option form stays local.

Reason for the generalisation: both apply.
- LITERATURE-WEAKENING: coefficients from integral domain to a `NoZeroDivisors` semiring; second block from one variable to arbitrary `τ`.
- MODERN-IDIOM: concrete-via-abstract (Q8) — after `degreeOf_mul_eq` the proof uses only "nonzero and avoiding `none`" and the `toMvPolynomial` degree identity.

Proposed restatement:
```lean
theorem Polynomial.degreeOf_toMvPolynomial_self (i : σ) (p : R[X]) :
    MvPolynomial.degreeOf i (p.toMvPolynomial i) = p.natDegree
theorem MvPolynomial.degreeOf_mul_of_degreeOf_eq_zero_left [NoZeroDivisors R]
    {p q : MvPolynomial σ R} {i : σ} (hp : p ≠ 0) (hi : degreeOf i p = 0) :
    degreeOf i (p * q) = degreeOf i q
theorem MvPolynomial.degreeOf_inr_rename_inl_mul_rename_inr [NoZeroDivisors R]
    {p : MvPolynomial σ R} (hp : p ≠ 0) (q : MvPolynomial τ R) (j : τ) :
    degreeOf (Sum.inr j) (rename Sum.inl p * rename Sum.inr q) = degreeOf j q
```
All compile in evidence/Roth.degreeOf_none_rename_mul_aeval/weaken.lean.
Estimated cost of regeneralisation: CHEAP
Mathlib downstream this enables:
- `Polynomial.degreeOf_toMvPolynomial_self` gives the first degree lemma for `Polynomial.toMvPolynomial` (it needs `degreeOf_uniqueAlgEquiv_symm`, already assessed YES-add-as-is).
- `degreeOf_mul_of_degreeOf_eq_zero_left/right` cover any nonzero factor avoiding the variable, beyond `degreeOf_mul_X_of_ne` (only `X j`).
- The `Sum.inl`/`Sum.inr` pair, with the coefficient lemma proposed in the `Roth.coeff_rename_mul_aeval` report, forms a disjoint-variables API.

Proposed mathlib location: `Mathlib/Algebra/MvPolynomial/Equiv.lean` (section `toMvPolynomial`, `degreeOf_toMvPolynomial_self`); `Mathlib/Algebra/MvPolynomial/NoZeroDivisors.lean` (product lemmas and `Sum` corollaries, after `degreeOf_mul_eq`); `Mathlib/Algebra/MvPolynomial/Degrees.lean` (outside-range lemma, after `degreeOf_rename_of_injective`).
Proposed PR title: "feat(Algebra/MvPolynomial): degreeOf of products in disjoint variables"
PR grouping: one PR with the twin `Roth.degreeOf_rename_mul_aeval` helpers; `degreeOf_toMvPolynomial_self` can join the `uniqueAlgEquiv` degree PR from `Roth.degreeOf_uniqueAlgEquiv_symm`.
Local refactor: move the project lemma out of `section Domain` with `[CommSemiring R] [NoZeroDivisors R]` and the evidence (5) proof; call site Separation.lean:557 unchanged.
Next action: run `/generalise Roth.degreeOf_none_rename_mul_aeval` with the targets above, then `/cleanup` and open the PR.

---

## Next step

Add `degreeOf_rename_eq_zero_of_notMem_range`, `degreeOf_mul_of_degreeOf_eq_zero_left` and `degreeOf_toMvPolynomial_self`, re-prove the project lemma from them under `CommSemiring + NoZeroDivisors` (call site Separation.lean:557 unchanged), then upstream them with the `Sum.inr` corollary alongside the twin's PR.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.degreeOf_none_rename_mul_aeval/weaken.lean` (imports `Roth.Separation`), checked with `lean_diagnostic_messages` after one fix (a type annotation in (7)); final version: no errors, no warnings, only the `#check` info. Contents: (0) `#check` shows `[CommRing R] [IsDomain R]`. (1) `degreeOf_rename_eq_zero_of_notMem_range` over `CommSemiring`. (2) `degreeOf_mul_of_degreeOf_eq_zero_left` under `NoZeroDivisors`. (3) `degreeOf_toMvPolynomial_self` over `CommSemiring` (from `toMvPolynomial_eq_rename_comp`, `degreeOf_rename_of_injective`, `Roth.degreeOf_uniqueAlgEquiv_symm`). (4) `Sum.inr` form from (1), (2). (5) Project statement under `CommSemiring + NoZeroDivisors` by `rw` + `exact` from (1)–(3). (6) Original proof body verbatim under `CommSemiring + NoZeroDivisors`. (7) `U = 0`, `V = X` over `ℤ`: LHS `0`, `natDegree X = 1` (so `hU` is needed).
- Searches: 3 WebSearch queries, Lean-Finder ×1, LeanSearch ×1, Loogle ×1 (no hits), mathlib greps of the `toMvPolynomial` section and the proposed names (free), local references grep (clean.tex:424, 435, 742). ChatGPT MCP n/a (not configured). `lean_local_search` n/a (ripgrep not installed); grep used instead.
