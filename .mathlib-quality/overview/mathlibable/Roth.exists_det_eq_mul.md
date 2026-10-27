---
decl: Roth.exists_det_eq_mul
file: Roth/Separation.lean
line: 542
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: EXPENSIVE
junk: KEEP
rationale: Roth's Lemma 2 (the Hasse-derivative determinant of a nonzero integer polynomial factors as U(x_1..x_{p-1}) V(x_p) with degree bounds) is absent from mathlib and is a named step of Roth's theorem, but it is a highly specialised auxiliary of one proof that can only land after five unlanded API PRs (MvPolynomial.hasseDeriv, genWronskian and Lemma 1, tensor-rank decomposition, MvPolynomial Gauss lemma, det degree bound), and its natural generalisation (UFD or CharZero domain, no Finite) is not a single mechanical edit; whether mathlib wants Roth-proof internals is a policy call.
action: Keep in project (sole caller Roth.index_le_lem6, Roth/Theta.lean:571); decide whether a Roth-theorem development goes to Mathlib/NumberTheory/DiophantineApproximation/ (then upstream this as part of a final Roth PR series after its dependencies) or stays downstream; if upstreamed, restate over a UFD R with CharZero and drop [Finite τ].
---

# Roth.exists_det_eq_mul

## Inventory entry

### `theorem Roth.exists_det_eq_mul`
- **Type**: `∀ {τ : Type u_1} [Finite τ] {P : MvPolynomial (Option τ) ℤ}, P ≠ 0 → ∀ {r : Option τ → ℕ}, (∀ j, degreeOf j P ≤ r j) → ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ), (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ ℤ) (V : Polynomial ℤ), U ≠ 0 ∧ V ≠ 0 ∧ (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧ (Matrix.of fun μ ν ↦ hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν) P).det = rename some U * Polynomial.aeval (X none) V` (from `#check`, evidence (0)).
- **What**: Roth's Lemma 2: for a nonzero integer polynomial `P(x_τ, y)` with partial degrees `≤ r`, there are `1 ≤ l ≤ r_y + 1` and Hasse operators `Δ_{D μ}` in the `x_τ` variables of orders `≤ μ` such that `F = det(Δ_{D μ} Δ_y^{(ν)} P)_{μ,ν<l}` equals `U(x_τ) V(y)` with `U, V` nonzero integral, `deg_{x_j} U ≤ l r_j`, `deg V ≤ l r_y`.
- **How**: `exists_rat_factors_det_hasseDeriv_aux` (private; uses `exists_separated_representation`, `exists_genWronskian_ne_zero`, `det_hasseDeriv_separated`, `wronskian_ne_zero_of_linearIndependent`, `hasseDeriv_map`) gives the factorisation over ℚ; `exists_int_factors` (Gauss-lemma step) descends it to ℤ; the degree bounds come from `degreeOf_rename_mul_aeval`, `degreeOf_none_rename_mul_aeval` and `degreeOf_det_hasseDeriv_le`.
- **Hypotheses**: `[Finite τ]` (needed by the private helper; evidence (1)); `hP : P ≠ 0` (needed: for `P = 0` the determinant is 0 but `U, V ≠ 0`); `hr` (all components used: `hr none` for `l ≤ r none + 1`, all for the degree bounds).
- **Uses from project**: `Roth.exists_rat_factors_det_hasseDeriv_aux` (private), `Roth.exists_int_factors`, `Roth.degreeOf_rename_mul_aeval`, `Roth.degreeOf_none_rename_mul_aeval`, `Roth.degreeOf_det_hasseDeriv_le`, `MvPolynomial.hasseDeriv` (project def)
- **Used by**: `Roth.index_le_lem6` (Roth/Theta.lean:571, `obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1`); mentioned in module docstring Separation.lean:37. No other uses (`grep -rn exists_det_eq_mul Roth/`).
- **Visibility**: public
- **Lines**: 536–559 (statement 542–548), proof length 11 lines
- **Notes**: Docstring cites clean.tex §2, Lemma `roth:lem2` with a verbatim quote. The source's conclusion (1) "F has integral coefficients and is not identically zero" follows from (2) and is not stated separately (the caller re-derives nonvanishing via `mapped_det_ne_zero_aux`).

## Junk check (Step 8)
- Used anywhere? Yes, once (Theta.lean:571), as the key input to Lemma 6.
- Wrapper of 1–2 mathlib calls? No; assembles five project lemmas.
- Does mathlib have it? No (no multivariate Hasse derivative, no generalized Wronskian, nothing on Roth's theorem in Diophantine approximation; mathlib's "Roth" is the additive-combinatorics Roth theorem).
- Too specific? It is a named lemma of the source and the natural interface between the algebra files and Theta.lean; inlining would hurt readability.
- Well-chosen? Yes.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring starts "Lemma 2"; Step 8 KEEP; qualified name absent from mathlib (grep). Not a glue lemma (it is a theorem assembling several project results, not an unfolding). Full workflow follows.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` elaborates, only the intended error in probe (1))
- decl `Roth.exists_det_eq_mul`: resolved at Roth/Separation.lean:542
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable: the determinant `F = U(x_1, …, x_{p-1}) V(x_p)` (Lemma 2 of Roth's theorem).

### Statement (Phase 1)

`Roth.exists_det_eq_mul` is a theorem stating: let `P ∈ ℤ[x_s (s ∈ τ), y]` be nonzero with `deg_{x_s} P ≤ r_s` and `deg_y P ≤ r_y`. Then there exist an integer `l` with `1 ≤ l ≤ r_y + 1` and multi-indices `D_0, …, D_{l-1}` on `τ` with `|D_μ| ≤ μ` such that the determinant `F = det( Δ^{(D_μ)}_x Δ^{(ν)}_y P )_{0≤μ,ν<l}` of Hasse derivatives factors as `F = U(x) V(y)`, with `U ∈ ℤ[x]`, `V ∈ ℤ[y]` nonzero, `deg_{x_j} U ≤ l r_j`, `deg V ≤ l r_y`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` with `[Finite τ]`: the variables `x_1, …, x_{p-1}`; `Option τ` adjoins the distinguished `y = x_p` as `none`.
- `P : MvPolynomial (Option τ) ℤ`: the polynomial `R` of the source.
- `r : Option τ → ℕ`: partial-degree bounds.

Hypotheses (Lean side):
- `hP : P ≠ 0`.
- `hr : ∀ j, degreeOf j P ≤ r j`.

Conclusion (math): the Hasse-derivative "generalized Wronskian in y" of `P` with suitable `x`-operators of bounded order factors into separated, integral, nonzero factors of controlled degree.

Conclusion (Lean): as in the inventory Type above.

### Size classification (Phase 2a)

Verdict: BIG
Reason: listed under `## Main results` of the module docstring and is the named Lemma 2 of the source (Roth 1955, Lemma 2 in the project numbering). It is a main intermediate result of the Roth development, though not a final theorem.

### One-line check (Phase 2b)

Body line count: 11 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | "Roth lemma determinant generalized Wronskian factors U(x_1..x_{p-1}) V(x_p) integer polynomial Roth's theorem proof" | partial | Roth 1955 (Mathematika 2) uses generalized Wronskians of a polynomial in p variables; Lemma 1 = nonvanishing criterion; separation-of-last-variable induction | Roth's paper (cambridge.org), arXiv 2502.00731 (Goel–Lunia–Ray exposition), Bostan–Dumas arXiv 1301.6598; exact U·V statement not surfaced in snippets |
|  2 | WebSearch (general form) | "Roth's theorem proof generalized Wronskian lemma l ≤ r_p + 1 Schmidt Diophantine approximation index" | partial | same structure: auxiliary polynomial, index, Roth's lemma proved by induction on number of variables using a Wronskian determinant splitting off the last variable | arXiv 2502.00731 §3; Valcarce Dalmau thesis (UB 2023, Lang's version); the inequality itself is in Roth's paper |
|  3 | WebSearch (aliases / named) | "Roth's lemma multivariate polynomial index generalized Wronskian separation of variables determinant Bombieri Gubler" | partial | Bombieri–Gubler, Heights in Diophantine Geometry, Ch. 6 / App. D: Roth's lemma (index bound) proved via generalized Wronskians and this separation step | snippets only; standard textbook home is Bombieri–Gubler Ch. 6 and Schmidt LNM 785 Ch. V |
|  4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for `roth:lem2` | yes | clean.tex lines 347–365: exactly the project statement (integral R, p ≥ 2 variables, 1 ≤ l ≤ r_p + 1, operators of orders ≤ 0..l-1, F = U V, degree bounds l r_j, l r_p) | Lean statement matches; the source's "p ≥ 2" is not needed (τ may be empty) |
|  6 | nLab | Roth's theorem / Wronskian | no | n/a | nLab has no Diophantine-approximation content; Wronskian page is analytic, not this lemma |
|  7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
|  8 | Stacks Project | n/a | n/a | n/a | not commutative algebra/algebraic geometry in Stacks' sense; Diophantine approximation not covered |
|  9 | MathOverflow / Math.SE | covered by #1–#3 (expositions) | partial | same as #3 | standard references are Roth 1955, Schmidt LNM 785, Bombieri–Gubler |
| 10 | recent arXiv | covered by #1/#2: arXiv 2502.00731 (2025) | yes | modern exposition, same lemma structure | no reformulation changing the form |

### Literature summary (Phase 3)

Concept identified as: the "Wronskian splitting" step (Lemma 2 in Roth 1955 / Schmidt LNM 785 Ch. V Lemma 6A-type statements) in the proof of Roth's lemma on the index of polynomials.
Sources agree on the standard form: yes, up to presentation (Roth/Schmidt use ordinary derivatives divided by factorials, i.e. Hasse derivatives, over ℚ/ℤ).
Most general standard form: stated over ℤ (integral coefficients needed for the height estimates downstream); the purely algebraic part works over any domain of characteristic 0 (for Lemma 1) whose factorisations descend from the fraction field (UFD, Gauss lemma).
Generality dimensions where the literature varies:
  - base ring: ℤ (all number-theory sources) → number-field rings of integers (Lang's version) → UFD / char-0 domain (algebraic content only).
  - variables: p ≥ 2 explicit; in Lean, arbitrary finite τ (or any τ, since a polynomial uses finitely many variables).
Disagreement with the literature: none.

### Generality analysis — `Roth.exists_det_eq_mul`

Literature-standard form (from Phase 3): ℤ coefficients; the algebraic content extends to a char-0 UFD R.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | base ring ℤ (with ℚ inside the proof) | `ℤ`, `Int.castRingHom ℚ` | ℤ in the literature; algebraically a char-0 UFD with fraction field | yes in principle, not compiled | needs `exists_int_factors` in UFD form (compiled in its own evidence (6)), `exists_genWronskian_ne_zero` over `[IsDomain R] [CharZero R]` (compiled in its evidence), plus generalising the private rational helper, `exists_separated_representation` (field K, fine for Frac R) and the det degree bound; a multi-file restatement, not one edit |
| 2 | `[Finite τ]` | finite | any τ | yes in principle, not mechanical | probe (1): dropping it fails to synthesise `Finite τ` at the helper; would need the rename-to-finite-support reduction used for `exists_genWronskian_ne_zero` |
| 3 | `hP : P ≠ 0` | nonzero | nonzero | NO | for `P = 0` the determinant is 0 but `U, V ≠ 0` |
| 4 | `hr` | all partial degrees | all partial degrees | NO | `hr none` gives `l ≤ r none + 1`; all components give the U, V degree bounds |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as far as mechanically verified; no weakening compiled)
Number of weakening opportunities found: 0 verified; 2 literature-plausible (ℤ → char-0 UFD; drop `[Finite τ]`), each requiring restatements threaded through several declarations and files (false-positive class 5 of the verdict gate).
Proposed restatement: none verified. Candidate target (not compiled):
```lean
theorem MvPolynomial.exists_det_hasseDeriv_eq_rename_mul_aeval {τ R : Type*} [CommRing R]
    [IsDomain R] [CharZero R] [NormalizedGCDMonoid R] [UniqueFactorizationMonoid R]
    {P : MvPolynomial (Option τ) R} (hP : P ≠ 0) {r : Option τ → ℕ}
    (hr : ∀ j, degreeOf j P ≤ r j) : ∃ l, 1 ≤ l ∧ l ≤ r none + 1 ∧ ∃ D : Fin l → (τ →₀ ℕ),
      (∀ μ, (D μ).degree ≤ μ) ∧ ∃ (U : MvPolynomial τ R) (V : Polynomial R), U ≠ 0 ∧ V ≠ 0 ∧
        (∀ j, degreeOf j U ≤ l * r (some j)) ∧ V.natDegree ≤ l * r none ∧
        (Matrix.of fun μ ν : Fin l ↦
          hasseDeriv ((D μ).mapDomain some + Finsupp.single none (ν : ℕ)) P).det =
          rename some U * Polynomial.aeval (X none) V
```
Cost of restatement: EXPENSIVE (multi-file; depends on generalising the private helper and four public dependencies).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles → typeclasses | no | no bundled structure hypotheses | — |
| 2 | sequences → filters | no | purely algebraic | — |
| 3 | construction → universal property | no | existence statement | — |
| 4 | set+predicate → bundled substructure | no | none natural | — |
| 5 | field-specific → typeclass hierarchy | yes | ℤ → char-0 UFD (row 1 above) | other number rings with class number 1; function-field analogues fail (CharZero needed) |
| 6 | 1-categorical → higher | no | n/a | — |
| 7 | concrete index → abstract | partial | `Option τ` could be `σ ⊕ Unit` or a chosen variable `i : σ` with `rename`/`optionEquivLeft`; `Option` is the existing mathlib convention (`MvPolynomial.optionEquivLeft`) | — |
| 8 | concrete-via-abstract | no | the statement's ℤ enters essentially via the Gauss-lemma descent (`exists_int_factors`); ℚ via linear algebra over a field; the proof body is generic only after generalising those helpers (row 1) | — |
| 9 | false-generalisation guard | no false generalisation | the UFD/CharZero form specialises back to the ℤ statement; dropping CharZero would be false (Lemma 1 fails in char p) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (beyond the base-ring generalisation already recorded in Phase 4a)
  - One-line reason: the statement is a concrete step of a classical argument; the only reorganisation is the base-ring/typeclass widening, which is not mechanically reachable and not a change of idiom.

### Proof strategy — `Roth.exists_det_eq_mul`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elementwise vs ideals | no | proof is already an assembly of named lemmas | — |
| 3 | sequences vs filters | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | helpers mathlib should have | yes | `MvPolynomial.hasseDeriv` (YES-but-generalise-first), generalized Wronskian + Lemma 1 (`Roth.genWronskian`, `Roth.exists_genWronskian_ne_zero`, YES-but-generalise-first), tensor-rank decomposition (`Roth.exists_separated_representation`, BORDERLINE), MvPolynomial Gauss lemma (`Roth.exists_int_factors`, BORDERLINE), det degree bound (`Roth.degreeOf_det_hasseDeriv_le`, YES-but-generalise-first), separated degree lemmas (YES-but-generalise-first) | follow-up PRs, MODERATE each |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  - The 11-line proof is a clean assembly; the length lives in the helpers, each assessed separately. Given the helper API, this is the shortest path.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.exists_det_eq_mul`

[A] Lean-Finder       "Roth's lemma: nonzero integer polynomial, Wronskian-type determinant of derivatives splits as U(x_1,...,x_{p-1}) V(x_p) with degree bounds"   only 2-ary `Polynomial.wronskian` lemmas (Mathlib/RingTheory/Polynomial/Wronskian.lean); no hit
[B] Loogle            `Matrix.det, MvPolynomial.rename, Polynomial.aeval, MvPolynomial.X`   no hits
[C] LeanSearch        "determinant of Hasse derivatives of multivariate integer polynomial factors as product of polynomial in some variables times polynomial in the last variable"   only univariate `Polynomial.hasseDeriv*`; no hit
[D] Grep mathlib src  `exists_det_eq_mul`, `theorem roth`, "Roth's (theorem|lemma)"; `namespace MvPolynomial` files containing `hasseDeriv`/`wronskian`   only additive-combinatorics Roth (`rothNumberNat`, Behrend bounds); no MvPolynomial Hasse derivative or Wronskian files
[E] Name pattern      `lean_local_search exists_det_eq_mul`   n/a: tool error (ripgrep not installed); replaced by [D]

Searched for both the ℤ statement and the general char-0 UFD form (via [A]–[D] concept queries).
Concluded: not in mathlib (all available methods exhausted, plus the general form); even the prerequisite notions (multivariate Hasse derivative, generalized Wronskian) are absent.

### Normal-form check

Equivalent formalisms: (a) as stated, `F = rename some U * aeval (X none) V`; (b) via `MvPolynomial.optionEquivLeft`, `F ↦ Polynomial.C U * V.map C`-style in `(MvPolynomial τ ℤ)[X]`; (c) existence of a nonzero generalized Wronskian of the `y`-Hasse-derivative family that is a product of separated factors.
Canonical form in mathlib: none for this idea. Form (a) is the natural one for `MvPolynomial (Option τ)`. RHS convention: n/a (existential, not an equation lemma).

### Syntactic generality

Alternatives: (a) as stated; (b) also assert `F ≠ 0` (source conclusion (1)); the caller re-derives it from `U, V ≠ 0` via `mapped_det_ne_zero_aux`; (c) state the determinant with `(D μ).optionElim ν` instead of `mapDomain some + single none ν` (index choice flagged in the `Roth.det_hasseDeriv_separated` report).
Chosen: (a); (b) is a cheap convenience, (c) would align with the planned upstream generalized-Wronskian API.

### Superfluous-argument audit

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Finite τ]` | not for the conclusion | mathematically droppable (a polynomial involves finitely many variables) but the proof needs it (probe (1)) |
| 2 | `hP : P ≠ 0` | yes | conclusion false for `P = 0` |
| 3 | `hr` | yes | all components feed degree bounds |
| 4 | ℤ concreteness | partly | essential for the downstream height estimates; algebraically replaceable by char-0 UFD |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (optional: add `F ≠ 0`; align index with `optionElim` if upstreamed)
Superfluous arguments: 1 droppable in principle (`[Finite τ]`, not mechanical)
Overall: SHIP-AS-STATED for the project; RESTATE-BEFORE-SHIP if upstreamed (UFD/CharZero, no `Finite`)

### Call sites — `Roth.exists_det_eq_mul`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 file

| Caller file:line | Usage pattern |
|---|---|
| Roth/Theta.lean:571 | `obtain ⟨l, hl, hl', D, hD, U, V, hU, hV, hUd, hVd, hF⟩ := exists_det_eq_mul hR.1 hR.2.1` (in `Roth.index_le_lem6`) |

Inline-derivation grep: (none) — no other derivation of the U·V factorisation in `Roth/` (grep for `rename some U \*` outside Separation.lean/CoeffNorm.lean finds only consumers of `hF`).

### Composition check (Phase 6)

Attempt 1: from mathlib primitives only.
  - Mathlib decls used: none applicable (no `MvPolynomial.hasseDeriv`, no generalized Wronskian, no MvPolynomial Gauss lemma).
  - Result: fails.
Attempt 2: from the project helpers (`exists_rat_factors_det_hasseDeriv_aux`, `exists_int_factors`, degree lemmas).
  - Result: succeeds, but that is the current 11-line proof using five non-mathlib results.
Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_det_eq_mul`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): Roth 1955 Lemma 2 / Schmidt LNM 785 / Bombieri–Gubler Ch. 6; local clean.tex lines 347–365 match the Lean statement.
- Generality analysis (Phase 4): MAXIMALLY GENERAL as verified (no weakening compiled; dropping `[Finite τ]` fails, probe (1)); ℤ → char-0 UFD and dropping `Finite` are literature-plausible but multi-file restatements (class 5).
- Mathlib search (Phase 5): not in mathlib; prerequisites also absent.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:** The result is genuinely new to mathlib and is a named, literature-standard step of Roth's theorem on rational approximation; mathlib's Diophantine-approximation library (Mathlib/NumberTheory/DiophantineApproximation/, Liouville, Dirichlet) stops short of Thue–Siegel–Roth, so the gap is real. But the declaration is an auxiliary of one specific proof: its only consumer anywhere is Lemma 6 of the same development (Theta.lean:571), it is phrased with the project's index conventions (`mapDomain some + single none ν`, `Option τ`), and it can only be stated after the multivariate Hasse derivative, generalized Wronskian with Lemma 1, the tensor-rank decomposition, the MvPolynomial Gauss lemma and the det degree bound have landed. Its generalisation (char-0 UFD, no `Finite`) is plausible but not a single mechanical edit. Whether mathlib wants the internals of the Roth proof (as opposed to only the final theorem and its reusable algebraic API) is a policy question the evidence cannot settle; a YES verdict would only make sense as part of a full Roth-theorem upstreaming plan, where cost is EXPENSIVE.

Numbered questions:
1. Is the Roth-theorem development itself intended for mathlib (Mathlib/NumberTheory/DiophantineApproximation/Roth*.lean), or for a downstream library/Archive? (If downstream: this is NO for mathlib, keep locally.)
2. If upstreamed, should intermediate lemmas like this one be public mathlib API, or private/`protected` steps inside the Roth file (only the reusable algebra going to general MvPolynomial files)?
3. If public, should it be restated over a char-0 UFD with `[Finite τ]` dropped (candidate in Phase 4b), at the cost of generalising the private helper and four dependencies?
4. Should the determinant index be switched to `(D μ).optionElim ν` to match the proposed upstream generalized-Wronskian API?

Next action: user answers the questions; keep the decl in the project meanwhile.

---

### Next step

Answer questions 1–4. If the answer to 1 is "mathlib", sequence this as the last PR of the Separation series after `MvPolynomial.hasseDeriv`, `genWronskian`/Lemma 1, `exists_separated_representation` (tensor form), `exists_int_factors` (Gauss lemma) and `degreeOf_det_le` land, restated per question 3.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.exists_det_eq_mul/check.lean` (imports `Roth.Separation`). One `lake env lean` run (32 s):
  - (0) `#check @Roth.exists_det_eq_mul` — elaborated type recorded in the inventory.
  - (1) the same statement without `[Finite τ]`, proved by `Roth.exists_det_eq_mul hP hr` — fails with `failed to synthesize instance Finite τ` (intended: this failure is the evidence that `Finite` is not mechanically droppable).
- Searches: 3 WebSearch queries, Lean-Finder, Loogle, LeanSearch, mathlib grep (recorded above). ChatGPT MCP n/a (not configured). `lean_local_search` n/a (ripgrep not installed); replaced by grep.
- Web sources: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EFB89E2873019B246F004FAA06E05A7F/S0025579300000644a.pdf/rational-approximations-to-algebraic-numbers.pdf, https://arxiv.org/html/2502.00731v1, https://pdf.arxiv.org/pdf/1301.6598, https://arxiv.org/pdf/1611.00248, https://diposit.ub.edu/dspace/handle/2445/199221
