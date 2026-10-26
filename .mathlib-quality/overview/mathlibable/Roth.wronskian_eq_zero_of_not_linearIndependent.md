---
decl: Roth.wronskian_eq_zero_of_not_linearIndependent
file: Roth/Wronskian.lean
line: 65
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The easy direction of the n-ary Wronskian criterion (dependent family has zero Wronskian) is absent from mathlib (n-ary Wronskian is a mathlib TODO); [Field K] weakens to [CommRing R] [IsDomain R] with the proof unchanged (verified), and IsDomain is necessary (ZMod 4 counterexample verified).
action: Upstream with Roth.wronskianMatrix/Roth.wronskian to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] [IsDomain R] (proof verbatim, evidence file); locally keep (call site Roth/Wronskian.lean:222 in wronskian_eq_zero_iff).
---

# Roth.wronskian_eq_zero_of_not_linearIndependent

## Inventory entry

### `theorem Roth.wronskian_eq_zero_of_not_linearIndependent`
- **Type**: `{K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]} (h : ¬ LinearIndependent K φ) : wronskian φ = 0`
- **What**: A `K`-linearly dependent family of `l` polynomials has vanishing (Hasse) Wronskian `det (D^{(μ)} φ_ν)`.
- **How**: From `Fintype.not_linearIndependent_iff` get a nontrivial relation `∑ g ν • φ ν = 0`; the constant vector `C ∘ g` is a nonzero kernel vector of the Wronskian matrix (apply the linear map `hasseDeriv μ` to the relation, `smul_eq_C_mul`), so `Matrix.exists_mulVec_eq_zero_iff` gives `det = 0`.
- **Hypotheses**: `[Field K]` (section variable); `h : ¬ LinearIndependent K φ`.
- **Uses from project**: `Roth.wronskian`, `Roth.wronskianMatrix`
- **Used by**: Roth/Wronskian.lean:222 (`wronskian_eq_zero_iff`, reverse direction). No other project use.
- **Visibility**: public
- **Lines**: 62–71, proof length 6 lines
- **Notes**: Roth/GenWronskian.lean:41 `genWronskian_eq_zero_of_not_linearIndependent` repeats the identical argument for the multivariate generalized Wronskian (same 5-line proof shape); both are instances of one abstract fact (det of `(L_μ (φ ν))` vanishes for linear maps `L_μ` and dependent `φ`).

## Junk check (Step 8)
- Used anywhere? Yes, once: it is the easy direction of `wronskian_eq_zero_iff` (Roth/Wronskian.lean:222), which is used downstream.
- Wrapper of 1–2 mathlib calls? No: 6-line proof combining `Fintype.not_linearIndependent_iff`, `Matrix.exists_mulVec_eq_zero_iff`, `hasseDeriv` linearity and `smul_eq_C_mul`.
- Does mathlib have it? No: only the 2-ary `Polynomial.wronskian` exists; the general `Matrix.det_eq_zero_of_not_linearIndependent_cols` needs dependence of the columns over `K[X]`, which still has to be derived.
- Too specific (inline?)? No: it is a named half of the main criterion of §2, and holds in any characteristic (unlike the converse), so separating it is the right granularity.
- Well-chosen? Yes; only `[Field K]` is stronger than needed.
- Conclusion: `KEEP` — action: keep; generalise to `[CommRing R] [IsDomain R]` when upstreaming.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring does not start internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `wronskian_eq_zero_of_not` over `.lake/packages/mathlib/Mathlib/`: no hit). Not a glue lemma (real 6-line proof), so the full workflow is run; the parent defs `Roth.wronskian` / `Roth.wronskianMatrix` are YES-but-generalise-first and their evidence is reused.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.wronskian_eq_zero_of_not_linearIndependent`: resolved at Roth/Wronskian.lean:65
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskian_eq_zero_of_not_linearIndependent` is a theorem stating: if polynomials `φ_0, …, φ_{l-1} ∈ K[t]` over a field `K` satisfy a nontrivial relation `c_0 φ_0 + ⋯ + c_{l-1} φ_{l-1} = 0` with constants `c_ν ∈ K`, then their Wronskian `det (D^{(μ)} φ_ν)` is the zero polynomial. No characteristic assumption.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K]` — constants / coefficient field.
- `l : ℕ` — number of polynomials.
- `φ : Fin l → K[X]` — the family.

Hypotheses (Lean side):
- `h : ¬ LinearIndependent K φ` — linear dependence over the constants.

Conclusion (math): `W(φ_0, …, φ_{l-1}) = 0`.

Conclusion (Lean): `Roth.wronskian φ = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the easy half of the file's main criterion `wronskian_eq_zero_iff`; a tool lemma, not itself listed as a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 6 substantive lines
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian vanishes linearly dependent polynomials any field converse fails characteristic p | yes | dependent implies zero Wronskian always (derivation is linear, columns become dependent); converse fails in char p (`1, x^p`) and for non-analytic functions (Peano) | Wikipedia "Wronskian"; Bostan–Dumas arXiv 1301.6598; arXiv 2602.20832 |
| 2 | WebSearch (general form) | linearly dependent functions Wronskian identically zero integral domain differential ring proof | yes | in any differential ring, a relation with constant coefficients gives dependent columns; no division needed | Bostan–Dumas 1301.6598 (constants ring, e.g. `K[[x^p]]`); forum and LibreTexts expositions |
| 3 | WebSearch (named-after / aliases) | Hasse derivative Wronskian "linearly dependent" vanishes Garcia Voloch | yes | Schmidt / Garcia–Voloch: `f_0..f_m` independent over `k` iff the Hasse Wronskian matrix `(D^{(i)} f_j)` has maximal rank (for suitable orders); dependent implies every such minor vanishes | arXiv 2107.09865, 1404.4506; J. Wang's notes on Wronskians in char p |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §2 first lemma, l.164–173 | yes | "Linear dependence gives a nontrivial constant linear relation between the columns, so the determinant vanishes" (over ℚ) | exact source; the second lemma (l.213–216) states the same for generalized Wronskians |
| 6 | nLab | Wronskian linear dependence | no | — | no nLab page on Wronskians (also checked for the parent `Roth.wronskian`) |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not a scheme-theoretic statement; Wronskians in curve theory surfaced via #3 |
| 9 | MathOverflow / Math.SE | (covered by #1/#2 searches) | partial | no dedicated MO thread; Math.SE/forum treatments of "dependent implies W = 0" are elementary exercises | the statement is textbook folklore |
| 10 | recent arXiv (last 5 years) | results of #1/#3 | yes | arXiv 2602.20832 (2026) Thm 2.11 states the full criterion for polynomials (char 0 or char > degree), with the easy direction char-free | confirms the char-free easy direction |

### Literature summary (Phase 3)

Concept identified as: the easy direction of the Wronskian criterion for linear independence ("dependent functions have vanishing Wronskian").
Sources agree on the standard form: yes — stated for functions over ℝ/ℂ, for elements of a differential ring/field (dependence over the constants), and for polynomials over any field with Hasse derivatives; always characteristic-free.
Most general standard form: if `f_1..f_n` in a commutative ring `A` (with derivation / Hasse–Schmidt derivation over a subring of constants `R`) satisfy a nontrivial `R`-linear relation, and `A` has no zero divisors over `R` (so a nonzero constant vector stays nonzero), the Wronskian is zero.
Generality dimensions where the literature varies:
  - coefficients: field to integral domain (needed: a nonzero constant vector must be a nonzero kernel vector over a domain).
  - derivative: ordinary vs Hasse (irrelevant to this direction; only linearity is used).
  - ambient object: polynomials, power series, analytic functions, differential rings.
Disagreement with the literature: none.

### Generality analysis — `Roth.wronskian_eq_zero_of_not_linearIndependent`

Literature-standard form (from Phase 3): for `φ : Fin l → R[X]` over an integral domain `R`, `¬ LinearIndependent R φ → wronskian φ = 0`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | integral domain | yes | proof uses only `Matrix.exists_mulVec_eq_zero_iff` (needs `[CommRing A] [IsDomain A]` for `A = R[X]`) and `C` injective; verified: proof compiles verbatim over `[CommRing R] [IsDomain R]` (evidence) |
| 2 | `[IsDomain R]` to plain `[CommRing R]` | — | — | NO | false: over `ZMod 4`, `![C 2]` is dependent (`2 • C 2 = 0`) but its Wronskian is `C 2 ≠ 0` (both facts verified in evidence) |
| 3 | `h : ¬ LinearIndependent K φ` | dependence over constants | dependence over constants | no | this is the hypothesis; dependence over `R[X]` would be the different (mathlib) column statement |
| 4 | `Fin l` index | `Fin l` | n-tuple | no | inherited from the def (square matrix indexed by derivative orders) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`[Field K]` to `[CommRing R] [IsDomain R]`; verified clean via `lean_diagnostic_messages`; `IsDomain` shown necessary by a verified counterexample)
Proposed restatement:

```lean
theorem Polynomial.wronskianDet_eq_zero_of_not_linearIndependent {R : Type*} [CommRing R]
    [IsDomain R] {l : ℕ} {φ : Fin l → R[X]} (h : ¬ LinearIndependent R φ) :
    wronskianDet φ = 0
```
(`wronskianDet` = placeholder n-ary name chosen when upstreaming the parent def.)

Cost of restatement: CHEAP — the proof is unchanged.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled preamble |
| 2 | sequences to filters? | no | — | algebraic, finite |
| 3 | construction vs universal property? | no | — | a vanishing statement |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R] [IsDomain R]` (Phase 4a row 1) | integral Wronskians (`ℤ[X]`), consistency with the `CommRing` parent def |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | inherited `Fin l` | — |
| 8 | concrete-via-abstract? | partial | proof body uses only that each `hasseDeriv μ` is `R`-linear; an abstract lemma "for linear maps `L_μ : M →ₗ[R] A` into a domain `A` with injective `algebraMap`, `det (L_μ (φ ν)) = 0` when `φ` is dependent" would cover this and Roth/GenWronskian.lean:41 at once | not proposed as the upstream form (not compiled; a design choice for the PR); recorded as an option |
| 9 | false-generalisation guard | no false generalisation | the `IsDomain` version is the same statement about the same object (project theorem is a direct specialisation, verified); dropping `IsDomain` would change truth (counterexample), so it is not proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the `[CommRing R] [IsDomain R]` form above, in `Mathlib/RingTheory/Polynomial/Wronskian.lean` beside the n-ary def.
  - Cost: CHEAP
  - Mathlib downstream this enables: n-ary analogue of `Polynomial.wronskian_self_eq_zero`-style vanishing; half of the char-0 iff; contrapositive "nonzero Wronskian implies linear independence" over any domain (e.g. `ℤ`).
  - Real mathematical improvement: the statement is true over every integral domain, and that is its exact range of validity (counterexample over `ZMod 4`).

### Proof strategy — `Roth.wronskian_eq_zero_of_not_linearIndependent`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | partial | could instead go through `Matrix.det_eq_zero_of_not_linearIndependent_cols` after showing the columns are `R[X]`-dependent; no shorter. The abstract linear-map lemma (4c row 8) would deduplicate with GenWronskian.lean:41 | CHEAP (optional) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (kernel vector + `Matrix.exists_mulVec_eq_zero_iff`, 6 lines).
  - Optional: factor the shared argument with `genWronskian_eq_zero_of_not_linearIndependent` into one abstract lemma.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.wronskian_eq_zero_of_not_linearIndependent`

[A] Lean-Finder       "if a family of polynomials is linearly dependent then the determinant of the matrix of their derivatives vanishes"   only 2-ary `Polynomial.wronskian_self_eq_zero`, `isAlt_wronskianBilin`, `Polynomial.wronskian`, unrelated `sylvesterDeriv`, `det_matrixOfPolynomials`
[B] Loogle            `Matrix.det, LinearIndependent, Polynomial.hasseDeriv`   no hits
[C] LeanSearch        "linearly dependent polynomials have zero Wronskian determinant"   2-ary family, `IsCoprime.wronskian_eq_zero_iff`, and building blocks `Matrix.det_eq_zero_of_not_linearIndependent_cols` / `_rows` (`[CommRing R] [IsDomain R]`, dependence of the matrix columns over the matrix ring)
[D] Grep mathlib src  `wronskian.*linearIndependent`, `linearIndependent.*wronsk`, `wronskian_eq_zero` (only `IsCoprime.wronskian_eq_zero_iff`, 2-ary, Wronskian.lean:125, and its use in FLT/MasonStothers.lean:91–92); `exists_mulVec_eq_zero_iff` (ToLinearEquiv.lean:163, `[IsDomain A]`)   no n-ary hit
[E] Name pattern      grep for `wronskian_eq_zero_of_not_linearIndependent` and `Roth.wronskian` in mathlib   absent

Searched for both the user's form (field) and the literature-standard form (integral domain; general differential-ring version).

Concluded: found building blocks (`Matrix.exists_mulVec_eq_zero_iff`, `Matrix.det_eq_zero_of_not_linearIndependent_cols`, `Fintype.not_linearIndependent_iff`); the statement itself is not in mathlib (no n-ary Wronskian exists).

### Normal-form check — `Roth.wronskian_eq_zero_of_not_linearIndependent`

Equivalent formalisms: `¬ LinearIndependent R φ → W φ = 0`; contrapositive `W φ ≠ 0 → LinearIndependent R φ`; relation form `∑ g ν • φ ν = 0 → g ≠ 0 → W φ = 0`.
Does mathlib already have a canonical form? For matrices, mathlib states both `det_eq_zero_of_not_linearIndependent_cols` and `linearIndependent_cols_of_det_ne_zero`; we follow that pair.
Proposed canonical form: keep the current implication, add the contrapositive `linearIndependent_of_wronskianDet_ne_zero` (mirrors `Matrix.linearIndependent_cols_of_det_ne_zero`).
RHS convention respected? yes (not an iff; the char-0 iff `wronskian_eq_zero_iff` puts `¬ LinearIndependent` on the RHS)

### Syntactic generality — `Roth.wronskian_eq_zero_of_not_linearIndependent`

Alternative restatements attempted:
- current: `¬ LinearIndependent R φ → wronskian φ = 0`
- contrapositive: `wronskian φ ≠ 0 → LinearIndependent R φ`
- explicit relation form with `g : Fin l → R`
Chosen restatement: current form (plus contrapositive as a companion).
Justification: the iff `wronskian_eq_zero_iff` consumes it directly as `.mpr`; the contrapositive is the form users apply to prove independence.

### Superfluous-argument audit — `Roth.wronskian_eq_zero_of_not_linearIndependent`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R] [IsDomain R]` suffices (verified) |
| 2 | `[IsDomain R]` (after weakening) | yes | counterexample over `ZMod 4` without it (verified) |
| 3 | `h` | yes | the hypothesis |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (add contrapositive companion when upstreaming)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[CommRing R] [IsDomain R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskian_eq_zero_of_not_linearIndependent`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:222 | `wronskian_eq_zero_of_not_linearIndependent⟩` (reverse direction of `wronskian_eq_zero_iff`) |

Inline-derivation grep: Roth/GenWronskian.lean:41–48 (`genWronskian_eq_zero_of_not_linearIndependent`) re-derives the same argument for the multivariate generalized Wronskian (`Fintype.not_linearIndependent_iff` + `Matrix.exists_mulVec_eq_zero_iff` + linearity of `hasseDeriv`); not a re-derivation of this exact statement but the same proof, a deduplication opportunity.

### Composition check (Phase 6)

Can the statement be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_eq_zero_of_not_linearIndependent_cols (A := wronskianMatrix φ) ?_`.
  - Mathlib decls used: `Matrix.det_eq_zero_of_not_linearIndependent_cols`
  - Result: partial — the remaining goal (columns of the Wronskian matrix are `K[X]`-dependent) needs the relation transfer via `Fintype.not_linearIndependent_iff`, `hasseDeriv` linearity and `smul_eq_C_mul`: a real 4-line proof.

Attempt 2: the current proof: `Fintype.not_linearIndependent_iff` then `Matrix.exists_mulVec_eq_zero_iff` then a `simpa` computation.
  - Result: works, but it is a proof with a nontrivial `simpa` step, not a call chain.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.wronskian_eq_zero_of_not_linearIndependent`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the standard char-free easy direction of the Wronskian criterion (Wikipedia, Bostan–Dumas arXiv 1301.6598, arXiv 2602.20832, Schmidt/Garcia–Voloch for Hasse Wronskians, project source §2).
- Generality analysis (Phase 4): STRICTLY NARROWER — `[Field K]` weakens to `[CommRing R] [IsDomain R]`, verified; `IsDomain` necessary, verified.
- Mathlib search (Phase 5): building blocks only; no n-ary Wronskian in mathlib (TODO at `Mathlib/RingTheory/Polynomial/Wronskian.lean` l.27–29).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's `Mathlib/RingTheory/Polynomial/Wronskian.lean` has only the 2-ary Wronskian and asks in its TODO for the n-ary one. Once the parent def `Roth.wronskian` (YES-but-generalise-first) is upstreamed, this lemma is the first basic fact about it. It is the standard, characteristic-free half of the linear-independence criterion, and its contrapositive (nonzero Wronskian implies independence) is how Wronskians are used in practice. Mathlib's `Matrix.det_eq_zero_of_not_linearIndependent_cols` does not give it directly. That lemma needs dependence of the matrix columns over `R[X]`, and getting there from a constant relation among the `φ ν` is the content of this lemma.

The statement is narrower than it should be. The proof never uses division: it needs only that `R[X]` is a domain (`Matrix.exists_mulVec_eq_zero_iff`) and that `C` is injective. The evidence file compiles the identical proof over `[CommRing R] [IsDomain R]`, and also shows the domain hypothesis cannot be dropped: over `ZMod 4`, `![C 2]` is dependent but its Wronskian is `C 2 ≠ 0`. So `[CommRing R] [IsDomain R]` is the exact generality.

Reason for the generalisation: LITERATURE-WEAKENING (field to integral domain).
Proposed restatement:
```lean
theorem Polynomial.wronskianDet_eq_zero_of_not_linearIndependent {R : Type*} [CommRing R]
    [IsDomain R] {l : ℕ} {φ : Fin l → R[X]} (h : ¬ LinearIndependent R φ) :
    wronskianDet φ = 0 := by
  sorry -- current proof verbatim (verified in evidence)
theorem Polynomial.linearIndependent_of_wronskianDet_ne_zero {R : Type*} [CommRing R]
    [IsDomain R] {l : ℕ} {φ : Fin l → R[X]} (h : wronskianDet φ ≠ 0) :
    LinearIndependent R φ := by
  sorry -- contrapositive
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- the n-ary analogue of the 2-ary vanishing lemmas (`wronskian_self_eq_zero`, `isAlt_wronskianBilin`): a family with a repeated or dependent member has zero Wronskian;
- proving linear independence over `ℤ` or any domain from a nonzero Wronskian;
- the easy half of the char-0 iff (`Roth.wronskian_eq_zero_iff`, follow-up PR).
PR grouping: same PR as `Roth.wronskianMatrix` and `Roth.wronskian` (n-ary Wronskian over `[CommRing R]`); optionally factor the shared kernel-vector argument with Roth/GenWronskian.lean:41 into one abstract linear-map lemma.
Next action: run `/generalise Roth.wronskian_eq_zero_of_not_linearIndependent` (target `[CommRing R] [IsDomain R]`), then ship it with the parent defs in `Mathlib/RingTheory/Polynomial/Wronskian.lean`, together with the contrapositive companion.

---

## Next step

Run `/generalise Roth.wronskian_eq_zero_of_not_linearIndependent`, targeting `[CommRing R] [IsDomain R]`. Then upstream it with the n-ary Wronskian PR, adding a `linearIndependent_of_..._ne_zero` companion.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskian_eq_zero_of_not_linearIndependent/weaken_domain.lean`, checked with `lean_diagnostic_messages`: clean, no errors or warnings, on the first check. It verifies: (1) the theorem over `[CommRing R] [IsDomain R]`, with the project proof verbatim; (2) the project theorem is a specialisation of it; (3) over `ZMod 4`, `![C 2]` is not linearly independent; (4) its Wronskian is nonzero, so `IsDomain` is necessary.
- WebSearch: 3 queries, summarised in the literature table. ChatGPT MCP: n/a (not configured).
- LeanSearch, Lean-Finder and Loogle queries and the mathlib greps are recorded in Phase 5.
- Project greps: `grep -rn wronskian_eq_zero_of_not_linearIndependent Roth/` returned 1 call site. `grep -rn "not_linearIndependent\|exists_mulVec_eq_zero_iff" Roth/` found the parallel proof at Roth/GenWronskian.lean:41.
