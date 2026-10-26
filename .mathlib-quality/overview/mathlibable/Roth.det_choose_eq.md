---
decl: Roth.det_choose_eq
file: Roth/Wronskian.lean
line: 79
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The binomial determinant det (d_nu choose mu) = Vandermonde / prod mu! exists in mathlib only as the private ℤ-lemma Matrix.of_eval_descPochhammer_eq_mul_of_choose; the char-free form (prod mu!) * det = prod (d_j - d_i) holds over any CommRing (and with Ring.choose over any binomial ring), verified in evidence, and the project's CharZero-field statement is a 2-line corollary.
action: Upstream to Mathlib/LinearAlgebra/Vandermonde.lean the CommRing lemmas det_eval_descPochhammer and prod_factorial_mul_det_choose (plus the BinomialRing Ring.choose version), replacing the private of_eval_descPochhammer_eq_mul_of_choose; keep det_choose_eq locally as the field corollary used at Roth/Wronskian.lean:151.
---

# Roth.det_choose_eq

## Inventory entry

### `theorem Roth.det_choose_eq`
- **Type**: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] (d : Fin l → ℕ), (Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det = (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) * ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i)`
- **What**: The binomial determinant `det (C(d_ν, μ))_{μ,ν}` equals the Vandermonde product `∏_{i<j} (d_j − d_i)` divided by `∏_{μ<l} μ!`.
- **How**: Rewrites each entry as `(μ!)⁻¹ · descPochhammer K μ` evaluated at `d ν` (`Nat.cast_choose_eq_descPochhammer_div`), so the matrix is a column-scaled transpose. It then pulls the scalars out with `Matrix.det_mul_column` and `Matrix.det_transpose`, and finishes with `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde` (using `descPochhammer_natDegree` and `monic_descPochhammer`) and `Matrix.det_vandermonde`.
- **Hypotheses**: `[Field K]` (section variable), `[CharZero K]`.
- **Uses from project**: `[]`
- **Used by**: Roth/Wronskian.lean:151 `wronskian_ne_zero_of_natDegree_injective` (in a `simpa` call). It is also named in the module docstring at l.28.
- **Visibility**: public
- **Lines**: 79–93, proof length 11 lines
- **Notes**: Mathlib proves the same identity, with the factorials multiplied in, over ℤ and with transposed indexing, as the private lemma `Matrix.of_eval_descPochhammer_eq_mul_of_choose` (Mathlib/LinearAlgebra/Vandermonde.lean:301). It uses it only to prove `superFactorial_dvd_vandermonde_det`.

## Junk check (Step 8)
- Used anywhere? Yes, once: at Roth/Wronskian.lean:151, where it identifies the top coefficient of the Wronskian for a family of distinct degrees as nonzero.
- Wrapper of 1–2 mathlib calls? No. It chains about 5 mathlib lemmas plus an entrywise rewriting step.
- Does mathlib have it? Only as a private ℤ-lemma whose factorials are multiplied in (`Matrix.of_eval_descPochhammer_eq_mul_of_choose`). That lemma cannot be used from outside its file, and it is stated over ℤ, not over a field.
- Too specific / inline? It has one call site, but it is a named classical identity (the source writes it out as a displayed formula), and the call site uses it inside `simpa`. Inlining it would bury an 11-line proof in that `simpa`.
- Well-chosen statement? The `⁻¹` form needs `CharZero` (evidence (4)). The natural statement multiplies the factorials in and holds over any `CommRing`.
- Conclusion: `KEEP`. Action: keep it locally as the field corollary, and upstream the char-free form.

## Mathlibable assessment (Step 9)

Pre-filter: not private, no `_aux` suffix, and the docstring does not start with internal or auxiliary. Step 8 said KEEP. The qualified name `Roth.det_choose_eq` is absent from mathlib (grep finds no `det_choose` in mathlib at all). It is not a glue lemma, so the full workflow runs below.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief, and the evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.det_choose_eq`: resolved at Roth/Wronskian.lean:79
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (the `l × l` Hasse determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.det_choose_eq` is a theorem stating the following. Let `K` be a field of characteristic zero and `d_0, …, d_{l−1}` natural numbers. Then
`det ( C(d_ν, μ) )_{0 ≤ μ, ν < l} = ∏_{0 ≤ i < j < l} (d_j − d_i) / ∏_{μ=0}^{l−1} μ!`.
Equivalently, `(∏ μ!) · det (C(d_ν, μ)) = Δ(d)`, the Vandermonde determinant of the nodes. The reason is that `C(X, μ)` is a polynomial of degree `μ` with leading coefficient `1/μ!`.

Variables / typeclasses involved (Lean side):
- `K : Type*` with `[Field K]` and `[CharZero K]`: the scalars. Characteristic zero makes the `μ!` invertible.
- `l : ℕ`: the matrix size.
- `d : Fin l → ℕ`: the nodes.

Hypotheses (Lean side):
- none beyond the typeclasses.

Conclusion (math): the binomial determinant equals the Vandermonde product times `∏ (μ!)⁻¹`.

Conclusion (Lean): `(Matrix.of fun μ ν : Fin l ↦ ((d ν).choose μ : K)).det = (∏ μ : Fin l, ((μ : ℕ).factorial : K)⁻¹) * ∏ i : Fin l, ∏ j ∈ Finset.Ioi i, ((d j : K) - d i)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a classical determinant identity used as a helper for the distinct-degree Wronskian lemma. It is not a main result of the project and introduces no structure. The module docstring does list it under Main results, but only as a tool.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 11
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | determinant binomial coefficients matrix det (binom{a_j}{i}) Vandermonde divided by product of factorials | yes | `det (C(a_j, i))_{i,j} = Δ(a_1..a_n) / ∏_{k<n} k!` | arXiv 2603.08106 states exactly this; Krattenthaler "Advanced Determinant Calculus" (math/9902004) lists such binomial determinants |
| 2 | WebSearch (general form) | superfactorial divides Vandermonde determinant integer-valued polynomials binomial basis | yes | over ℤ: `sf(n−1) ∣ Δ(a)`, because `Δ(a) = sf · det (C(a_j, i))`; Pólya: the `C(X, k)` form a ℤ-basis of `Int(ℤ)` | MathWorld "Vandermonde Determinant" (Chapman 1996); Chabert's survey; OEIS A000178; mathlib's `superFactorial_dvd_vandermonde_det` |
| 3 | WebSearch (named-after / aliases) | "binomial determinant" Gessel Viennot det binom(a_j, b_i) product formula | yes | Gessel–Viennot 1985: general binomial determinants `det C(a_i, b_j)` (minors of Pascal's matrix) count lattice paths. The case of consecutive `b_j = 0..n−1` has the Vandermonde product formula | González–Planas-Vilanova arXiv 2603.29431 give closed forms for consecutive rows/columns |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for choose/Vandermonde | yes | l.187–193: `det (C(d_ν, μ)) = ∏_{i<j}(d_j − d_i) / ∏ μ!`, "`binom X μ` has degree μ and leading coefficient 1/μ!" | the exact source of the lemma |
| 6 | nLab | (via WebSearch results #1–#3; nLab "Vandermonde determinant") | no | — | nLab has no page on binomial determinants. This is a classical algebraic and combinatorial identity, not a categorical concept |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept. The closest Stacks material, on integer-valued polynomials, does not state it |
| 9 | MathOverflow / Math.SE | (covered by the #2 search, which returned MathWorld/OEIS and no MO thread) | partial | the folklore "Vandermonde / superfactorial is an integer" with the binomial-matrix proof | standard folklore. The ℤ-divisibility corollary is the commonly quoted form |
| 10 | recent arXiv (last 5 years) | results of #1 and #3 | yes | arXiv 2603.08106 (2026), 2603.29431 (2026) | confirms that the form multiplied by `∏ k!` or divided by it is the standard statement |

### Literature summary (Phase 3)

Concept identified as: the binomial determinant with consecutive lower indices, `det (C(a_j, i))_{0 ≤ i < n}`. This is the Vandermonde determinant written in the binomial basis.
Sources agree on the standard form: yes. Every source gives `det (C(a_j, i)) = Δ(a) / ∏_{k<n} k!`, or equivalently `∏ k! · det = Δ(a)`. The ℤ-divisibility statement `sf ∣ Δ` is the commonly cited corollary.
Most general standard form: for nodes `a_j` in any ring where `C(a, k)` makes sense (ℤ, ℚ-algebras, and more generally binomial rings or λ-rings), `(∏_{k<n} k!) · det (C(a_j, i)) = ∏_{i<j}(a_j − a_i)`. The division form needs the `k!` to be invertible.
Generality dimensions where the literature varies:
  - nodes: natural numbers or integers, up to elements of a binomial ring or ℚ-algebra.
  - scalars: ℤ, ℚ, fields of characteristic 0. The multiplied form holds over any commutative ring.
  - normalisation: divided by `∏ k!` (needs `k!` invertible), or multiplied by `∏ k!` (char-free).
Disagreement with the literature: none. The project uses the division form, which forces `CharZero`.

### Generality analysis — `Roth.det_choose_eq`

Literature-standard form (from Phase 3): `(∏_{μ<l} μ!) · det (C(x_ν, μ)) = ∏_{i<j}(x_j − x_i)` over any commutative ring for natural-number nodes, and over any binomial ring for arbitrary nodes.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K] [CharZero K]` | char-0 field, division form | any commutative ring, multiplied form | yes | Verified: `Evidence.prod_factorial_mul_det_choose` over `[CommRing R]` compiles. In the `⁻¹` form `CharZero` cannot be dropped (verified counterexample in `ZMod 2`, `l = 3`, `d = ![0,1,2]`: LHS `1`, RHS `0`). So the weakening is a restatement into multiplied form, with the project statement as a 2-line corollary (verified) |
| 2 | `d : Fin l → ℕ` | natural nodes, `Nat.choose` | arbitrary nodes in a binomial ring, `Ring.choose` | yes | Verified: `Evidence.prod_factorial_mul_det_ringChoose` for `[CommRing R] [BinomialRing R]` and `x : Fin l → R` compiles. It covers ℤ, ℤ_p and ℚ-algebras |
| 3 | `Fin l` indexing | `Fin l` | `Fin n` | no | the row index runs over the lower binomial indices `0..l−1`, so `Fin l` is the natural index |
| 4 | row/column orientation `(μ, ν)` | lower index in rows | either | no | the transpose has the same determinant. Mathlib's private lemma uses the transposed orientation `(i, j) ↦ C(v i, j)`, and either orientation is fine |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2, both verified clean with `lean_diagnostic_messages` on the evidence file:
- (a) Char-free multiplied form over `[CommRing R]`.
- (b) `Ring.choose` with arbitrary nodes in a `[BinomialRing R]`.

Both use a new helper, `det_eval_descPochhammer`, which holds over any `CommRing`. Mathlib's `det_eval_matrixOfPolynomials_eq_det_vandermonde` needs exact degree and monicity, and the descPochhammer instances of those (`descPochhammer_natDegree`, `monic_descPochhammer`) are proved only for nontrivial rings without zero divisors. The helper avoids that by mapping from ℤ.
Proposed restatement:

```lean
namespace Matrix
variable {R : Type*} [CommRing R] {n : ℕ}
theorem det_eval_descPochhammer (v : Fin n → R) :
    (of fun i j : Fin n ↦ (descPochhammer R j).eval (v i)).det = (vandermonde v).det
theorem prod_factorial_mul_det_choose (v : Fin n → ℕ) :
    (∏ j : Fin n, ((j : ℕ).factorial : R)) * (of fun i j : Fin n ↦ ((v j).choose i : R)).det =
      ∏ i : Fin n, ∏ j ∈ Finset.Ioi i, ((v j : R) - v i)
theorem prod_factorial_mul_det_ringChoose [BinomialRing R] (v : Fin n → R) :
    (∏ j : Fin n, ((j : ℕ).factorial : R)) * (of fun i j : Fin n ↦ Ring.choose (v j) i).det =
      ∏ i : Fin n, ∏ j ∈ Finset.Ioi i, (v j - v i)
end Matrix
```
Cost of restatement: CHEAP. All three compile in evidence, with proofs of 4–12 lines.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | the only hypotheses are typeclasses |
| 2 | sequences to filters? | no | — | finite algebraic identity |
| 3 | construction vs universal property? | no | — | an identity of numbers |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R]` multiplied form (Phase 4a row 1) | replaces the private ℤ-lemma; `superFactorial_dvd_vandermonde_det` follows over ℤ |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | ℕ nodes to binomial-ring nodes with `Ring.choose` (row 2) | links `Mathlib/RingTheory/Binomial.lean` (`Ring.choose`, `Ring.descPochhammer_eq_factorial_smul_choose`) with the Vandermonde API, and gives Vandermonde divisibility in every binomial ring (for example ℤ_p) |
| 8 | concrete-via-abstract? | no | — | the proof only uses that `C(X, μ) · μ!` is monic of degree `μ` (the Vandermonde-in-another-basis argument). Mathlib already has that abstraction (`det_eval_matrixOfPolynomials_eq_det_vandermonde`), and the new helper is the descPochhammer instance of it without the domain hypothesis |
| 9 | false-generalisation guard | no false generalisation | the CommRing form specialises back to the project statement (evidence (3)). The `Ring.choose` form agrees with `Nat.choose` on ℕ-casts (`Ring.choose_natCast`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: the three `Matrix.*` lemmas in Phase 4b, placed in `Mathlib/LinearAlgebra/Vandermonde.lean`.
  - Cost: CHEAP
  - Mathlib downstream this enables:
    - makes the private `of_eval_descPochhammer_eq_mul_of_choose` public and general;
    - `superFactorial_dvd_vandermonde_det` becomes a corollary for natural-number or binomial-ring nodes;
    - a domain-free `det_eval_descPochhammer`;
    - a link from `Ring.choose` to `Matrix.vandermonde`.
  - Real mathematical improvement: the identity is char-free in multiplied form, and stating it that way removes the `CharZero`/field assumption, which only the division normalisation needed.

### Proof strategy — `Roth.det_choose_eq`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `Matrix.det_eval_descPochhammer` over any `CommRing`, without mathlib's domain-only `descPochhammer_natDegree`/`monic_descPochhammer` route, and the public multiplied-form choose lemma | CHEAP (ship with the restatement) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It is the standard "Vandermonde in the falling-factorial basis" argument, which is mathlib's own route in `superFactorial_dvd_vandermonde_det`.
  - Missing mathlib API: `det_eval_descPochhammer` over a general `CommRing`, and a public choose-determinant lemma.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.det_choose_eq`

[A] Lean-Finder       "det (Nat.choose (v i) j) times product of factorials equals Vandermonde determinant"   hits: `superFactorial_dvd_vandermonde_det`, `det_vandermonde_id_eq_superFactorial`, `det_vandermonde`, `det_projVandermonde`, `det_vandermonde_sub`. None is the choose determinant
[B] Loogle            `Matrix.det, Nat.choose`   no hits (the private mathlib lemma is not indexed)
[C] LeanSearch        "determinant of matrix of binomial coefficients choose equals Vandermonde divided by product of factorials"   hits: `det_vandermonde`, `superFactorial_dvd_vandermonde_det`, `det_projVandermonde`, `det_vandermonde_id_eq_superFactorial`, `det_eval_matrixOfPolynomials_eq_det_vandermonde`. These are building blocks only
[D] Grep mathlib src  `det_choose`, `choose_det`, `descPochhammer.*vandermonde`, files containing both `choose` and `det`   one hit, the private `Matrix.of_eval_descPochhammer_eq_mul_of_choose` (Mathlib/LinearAlgebra/Vandermonde.lean:301), over ℤ with natural-number nodes; no `Ring.choose` determinant
[E] Name pattern      `lean_local_search` not used. Grep for the qualified names `Roth.det_choose_eq`, `Matrix.det_choose`, `prod_factorial_mul_det_choose` and `det_eval_descPochhammer` replaced it   absent from mathlib

Searched for both the user's form (char-0 field, division form) and the literature-standard form (multiplied form over a commutative ring, binomial-ring nodes).

Concluded: found a partial match, `Matrix.of_eval_descPochhammer_eq_mul_of_choose` (private, ℤ only, factorials multiplied in, transposed orientation). It is not usable from outside its file and does not cover fields or general rings. The general form is not in mathlib.

### Normal-form check — `Roth.det_choose_eq`

Equivalent formalisms:
- `det (C(d_ν, μ)) = (∏ μ!)⁻¹ · Δ` (current);
- `(∏ μ!) · det (C(d_ν, μ)) = Δ` (multiplied);
- `det (C(d_ν, μ)) = Δ / ∏ μ!`;
- the transposed matrix;
- `Δ` written as `(vandermonde d).det` or as `∏ ∏ (d j − d i)`.

Does mathlib already have a canonical form? The Vandermonde side is canonical as `∏ i, ∏ j ∈ Ioi i, (v j - v i)` (the RHS of `det_vandermonde`). There is no public choose-determinant lemma.
Proposed canonical form: the multiplied form with the Vandermonde product on the RHS, `(∏ μ!) * det (choose) = ∏ i, ∏ j ∈ Ioi i, (v j - v i)`. It keeps the canonical `det_vandermonde` RHS and has no division.
RHS convention respected? yes

### Syntactic generality — `Roth.det_choose_eq`

Alternative restatements attempted:
- multiplied form over `[CommRing R]` (compiles, evidence (1));
- `Ring.choose` form over `[BinomialRing R]` (compiles, evidence (2));
- division form over a char-0 field (current; recovered from (1), evidence (3));
- RHS as `(vandermonde (fun ν ↦ (d ν : R))).det` (rejected: the call site needs the explicit product, which it feeds to `Finset.prod_eq_zero_iff` and `sub_eq_zero`).

Chosen restatement: the multiplied form with the explicit product RHS, with the division form kept as the field corollary.
Justification: the multiplied form applies in every ring with no side conditions. The only call site (l.151) shows nonvanishing with `simpa [..., Nat.factorial_ne_zero, ...]`, which works with either form.

### Superfluous-argument audit — `Roth.det_choose_eq`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | only for `⁻¹` | `[CommRing R]` suffices for the multiplied form (verified) |
| 2 | `[CharZero K]` | yes for the stated form, no for the multiplied form | evidence (4): the `⁻¹` form is false in `ZMod 2` |
| 3 | `l` | yes | matrix size |
| 4 | `d` | yes | nodes; can be generalised to binomial-ring nodes |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR. Target the multiplied form `(∏ μ!) * det = ∏ ∏ (x j − x i)`.
Syntactic generality: RESTATE (`[CommRing R]` with natural-number nodes, plus the `[BinomialRing R]` version with `Ring.choose`).
Superfluous arguments: 2 to drop in the upstream form (`[Field K]` weakened to `[CommRing R]`, and `[CharZero K]`).

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.det_choose_eq`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:151 | `simpa [h0, det_choose_eq, eq_comm (a := 0), Finset.prod_eq_zero_iff, sub_eq_zero, hφ,` (`wronskian_ne_zero_of_natDegree_injective`) |
| Roth/Wronskian.lean:28 | module docstring mention only |

Inline-derivation grep: no other binomial-determinant or `descPochhammer`/Vandermonde computation in `Roth/` (`grep -rn "choose μ\|det_vandermonde\|descPochhammer" Roth/` hits only l.79–93). In mathlib, the same computation is re-derived privately in `of_eval_descPochhammer_eq_mul_of_choose`, which is evidence that the public lemma is a missing API piece.

### Composition check (Phase 6)

Can `Roth.det_choose_eq` be derived from mathlib in ≤3 chained calls?

Attempt 1: `det_vandermonde` together with `det_eval_matrixOfPolynomials_eq_det_vandermonde` (p = descPochhammer) and `det_mul_column`.
  - Mathlib decls used: `Matrix.det_vandermonde`, `Matrix.det_eval_matrixOfPolynomials_eq_det_vandermonde`, `Matrix.det_mul_column`, `Matrix.det_transpose`, `descPochhammer_natDegree`, `monic_descPochhammer`, `Nat.cast_choose_eq_descPochhammer_div`
  - Result: partial. It works only after a matrix-rewriting `have` with `ext; simp`, which makes it an 11-line proof and not a composition.
  - Notes: this is a proof with intermediate reasoning, not a ≤3-call composition.

Attempt 2: the private `Matrix.of_eval_descPochhammer_eq_mul_of_choose`.
  - Result: fails. It is private and over ℤ only.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.det_choose_eq`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the binomial determinant with consecutive lower indices equals `Δ / ∏ k!`. This is classical (Krattenthaler's survey, Gessel–Viennot, Chapman 1996 via MathWorld, arXiv 2603.08106) and is the source's displayed identity (§2, clean.tex l.187–193).
- Generality analysis (Phase 4): STRICTLY NARROWER. The multiplied form over `[CommRing R]` and the `Ring.choose` form over `[BinomialRing R]` both compile in evidence. The current form is a 2-line corollary, and `CharZero` is necessary only for the `⁻¹` normalisation (counterexample compiled).
- Mathlib search (Phase 5): a partial match only, the private ℤ-lemma `Matrix.of_eval_descPochhammer_eq_mul_of_choose`. There is no public or general form.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The gap in mathlib is concrete. `Mathlib/LinearAlgebra/Vandermonde.lean` proves the binomial determinant identity only as the private lemma `of_eval_descPochhammer_eq_mul_of_choose`, over ℤ, and only to derive `superFactorial_dvd_vandermonde_det`. No public lemma states `det (C(v_j, i))` in terms of the Vandermonde product, and none exists over a general ring or for `Ring.choose`. The project lemma is this identity in its char-0 division form. The evidence file shows that the right statement multiplies the factorials in: `(∏ μ!) · det (C(x_ν, μ)) = ∏_{i<j}(x_j − x_i)`. That form holds over every commutative ring for natural-number nodes, and over every binomial ring with `Ring.choose` for arbitrary nodes. The project's statement follows from it in two lines (cancel `∏ μ!`, using `CharZero`).

A small infrastructure gap appears along the way. Mathlib's `det_eval_matrixOfPolynomials_eq_det_vandermonde` needs exact degree and monicity, which mathlib proves for `descPochhammer R` only when `R` is nontrivial without zero divisors. The helper `det_eval_descPochhammer` removes that restriction by mapping from ℤ (verified). The `CharZero` hypothesis cannot simply be dropped from the current form: in `ZMod 2` with `l = 3` and `d = ![0, 1, 2]` the LHS is `1` and the RHS is `0` (verified by `decide`). So the generalisation is a restatement, not a hypothesis deletion, and the project keeps its form as a corollary.

Reason for the generalisation: LITERATURE-WEAKENING (from a char-0 field to any commutative ring in multiplied form, and from natural-number nodes to binomial-ring nodes) plus MODERN-IDIOM (`Ring.choose`/`BinomialRing`).
Proposed restatement:
```lean
namespace Matrix
variable {R : Type*} [CommRing R] {n : ℕ}
theorem det_eval_descPochhammer (v : Fin n → R) :
    (of fun i j : Fin n ↦ (descPochhammer R j).eval (v i)).det = (vandermonde v).det := by
  sorry -- proved in evidence via descPochhammer_map from ℤ and RingHom.map_det
theorem prod_factorial_mul_det_choose (v : Fin n → ℕ) :
    (∏ j : Fin n, ((j : ℕ).factorial : R)) * (of fun i j : Fin n ↦ ((v j).choose i : R)).det =
      ∏ i : Fin n, ∏ j ∈ Finset.Ioi i, ((v j : R) - v i) := by
  sorry -- proved in evidence
theorem prod_factorial_mul_det_ringChoose [BinomialRing R] (v : Fin n → R) :
    (∏ j : Fin n, ((j : ℕ).factorial : R)) * (of fun i j : Fin n ↦ Ring.choose (v j) i).det =
      ∏ i : Fin n, ∏ j ∈ Finset.Ioi i, (v j - v i) := by
  sorry -- proved in evidence via Ring.descPochhammer_eq_factorial_smul_choose
end Matrix
```
Estimated cost of regeneralisation: CHEAP (all proofs are in the evidence file).
Mathlib downstream this enables:
- replaces the private `Matrix.of_eval_descPochhammer_eq_mul_of_choose`; `superFactorial_dvd_vandermonde_det` can be reproved through the public lemma;
- Vandermonde divisibility by the superfactorial in any binomial ring;
- `det_eval_descPochhammer` without the `NoZeroDivisors`/`Nontrivial` detour;
- a bridge between `Mathlib/RingTheory/Binomial.lean` and `Mathlib/LinearAlgebra/Vandermonde.lean`.
PR grouping: one small PR to `Mathlib/LinearAlgebra/Vandermonde.lean` (it must import `Mathlib.RingTheory.Binomial`, or the `Ring.choose` lemma goes in a downstream file). It is independent of the Wronskian PR (`Roth.wronskianMatrix`, `Roth.wronskian`), which would then use the field corollary.
Next action: run `/generalise Roth.det_choose_eq` with the multiplied `[CommRing R]` and `[BinomialRing R]` targets. Then open a PR titled "feat(LinearAlgebra/Vandermonde): binomial determinant `det (choose (v j) i)`" that replaces the private lemma. Locally, keep `det_choose_eq` as the corollary used at Roth/Wronskian.lean:151.

---

## Next step

Upstream `Matrix.det_eval_descPochhammer`, `Matrix.prod_factorial_mul_det_choose` and `Matrix.prod_factorial_mul_det_ringChoose` (all over `[CommRing R]`) to `Mathlib/LinearAlgebra/Vandermonde.lean`, replacing the private `of_eval_descPochhammer_eq_mul_of_choose`. Keep `Roth.det_choose_eq` as the char-0 field corollary.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.det_choose_eq/weaken.lean` (imports `Roth.Wronskian` and `Mathlib.RingTheory.Binomial`), checked with `lean_diagnostic_messages`: clean, no errors or warnings.
  - Earlier iterations failed: `descPochhammer_natDegree` and `monic_descPochhammer` need `NoZeroDivisors`/`Nontrivial`, and `simp` looped on `← descPochhammer_map`. Both were fixed by mapping from ℤ.
  - The file verifies: (H) `det_eval_descPochhammer` over any `CommRing`; (1) `prod_factorial_mul_det_choose` over `[CommRing R]`; (2) `prod_factorial_mul_det_ringChoose` over `[CommRing R] [BinomialRing R]`; (3) the project statement derived from (1) in a char-0 field; (4) a counterexample showing `CharZero` is needed for the `⁻¹` form (`ZMod 2`, `l = 3`, by `decide`).
- Mathlib greps:
  - `det_choose`, `choose_det`, `descPochhammer.*vandermonde`: none.
  - Vandermonde.lean l.287–322: the private `of_eval_descPochhammer_eq_mul_of_choose` and `superFactorial_dvd_vandermonde_det`.
  - Pochhammer.lean l.281/336: domain hypotheses on `monic_descPochhammer` and `descPochhammer_natDegree`.
  - Binomial.lean l.390: `Ring.descPochhammer_eq_factorial_smul_choose`.
- LeanSearch, Lean-Finder and Loogle results are in Phase 5. Loogle `Matrix.det, Nat.choose` returned no hits.
- WebSearch: 3 queries (Phase 3 table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn det_choose_eq Roth/`: l.28 (docstring), l.79 (decl), l.151 (sole use).
