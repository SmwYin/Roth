---
decl: Roth.coeff_wronskian_of_natDegree_injective
file: Roth/Wronskian.lean
line: 122
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The classical leading-term formula for the n-ary Wronskian (coefficient of t^(sum d - l(l-1)/2) equals prod of leading coefficients times det (d_nu choose mu)) is absent from mathlib, which only has the 2-ary Polynomial.wronskian; the proof goes through verbatim over any CommRing (verified), and the name's _of_natDegree_injective suffix is misleading because the statement has no hypotheses.
action: Upstream with Roth.wronskian / Roth.wronskianMatrix to Mathlib/RingTheory/Polynomial/Wronskian.lean over [CommRing R] (verified in evidence) under a hypothesis-free name such as coeff_wronskian_sum_natDegree_sub, together with the per-index product-coefficient helper (Roth.coeff_prod_of_natDegree_le') in Mathlib/Algebra/Polynomial/BigOperators.lean; locally keep (sole use Roth/Wronskian.lean:152).
---

# Roth.coeff_wronskian_of_natDegree_injective

## Inventory entry

### `theorem Roth.coeff_wronskian_of_natDegree_injective`
- **Type**: `∀ {K : Type*} [Field K] {l : ℕ} {φ : Fin l → K[X]}, (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det`
- **What**: For any family `φ_0, …, φ_{l-1}` of polynomials with degrees `d_ν`, the coefficient of `t^D`, `D = ∑ d_ν − ∑ ν` (truncated subtraction), in the Hasse Wronskian `det (D^{(μ)} φ_ν)` is `(∏ lc(φ_ν)) · det (C(d_ν, μ))_{μ,ν}`.
- **How**: Expands both determinants with `Matrix.det_apply'` and `finsetSum_coeff` and compares permutation by permutation. For a permutation `σ` with `σ i ≤ d_i` for all `i`, it rewrites `D = ∑ (d_i − σ i)` (`Equiv.sum_comp`, `Finset.sum_tsub_distrib`), applies the private per-index top-coefficient lemma `coeff_prod_of_natDegree_le'` (via `natDegree_hasseDeriv_le`) and `hasseDeriv_coeff`. Otherwise some factor vanishes (`hasseDeriv_eq_zero_of_lt_natDegree`, `Nat.choose_eq_zero_of_lt`). Finishes with `simp [coeff_intCast_mul, Finset.prod_mul_distrib, ...]`.
- **Hypotheses**: `[Field K]` (section variable); none on `φ`.
- **Uses from project**: `Roth.wronskian`, `Roth.wronskianMatrix`, `Roth.coeff_prod_of_natDegree_le'` (private)
- **Used by**: Roth/Wronskian.lean:152 `wronskian_ne_zero_of_natDegree_injective` (in `simpa ... using`); also named in the module docstring at l.41.
- **Visibility**: public
- **Lines**: 122–143, proof length 19 lines
- **Notes**: The name suffix `_of_natDegree_injective` refers to a hypothesis the statement does not have (the docstring says so explicitly). The identity holds for every family; injectivity is only needed downstream to make the RHS nonzero.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Wronskian.lean:152, the distinct-degree nonvanishing lemma, which is the base case of the hard direction of `wronskian_eq_zero_iff`.
- Wrapper of 1–2 mathlib calls? No: a 19-line permutation-by-permutation coefficient computation.
- Does mathlib have it? No. Mathlib has only the 2-ary `Polynomial.wronskian` and its degree bound `Polynomial.natDegree_wronskian_lt_add`; no n-ary Wronskian and no coefficient formula.
- Too specific / inline? One call site, but it is the named step of the source proof ("The coefficient of t^D in the new Wronskian is ...") and inlining 19 lines into a `simpa` would be worse.
- Well-chosen statement? Mathematically yes (hypothesis-free, which is the right generality). The name is misleading and `[Field K]` is stronger than needed.
- Conclusion: `KEEP`. Action: keep; rename to a hypothesis-free name and generalise to `[CommRing R]` when upstreaming.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring does not start with internal/auxiliary; Step 8 said KEEP; the qualified name `Roth.coeff_wronskian_of_natDegree_injective` is absent from mathlib (grep for `coeff_wronskian` in `.lake/packages/mathlib/Mathlib/` has no hits). It is a 19-line theorem, not a glue lemma, so the full workflow runs. It reuses the parent assessments `Roth.wronskian` / `Roth.wronskianMatrix` (YES-but-generalise-first) and `Roth.det_choose_eq` (YES-but-generalise-first).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.coeff_wronskian_of_natDegree_injective`: resolved at Roth/Wronskian.lean:122
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (Hasse `l × l` determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.coeff_wronskian_of_natDegree_injective` is a theorem stating the following. Let `K` be a field and `φ_0, …, φ_{l−1} ∈ K[t]` with degrees `d_ν` and leading coefficients `a_ν`. Put `D = ∑ d_ν − (0 + 1 + ⋯ + (l−1))` (truncated at 0). Then the coefficient of `t^D` in the Wronskian `W = det (D^{(μ)} φ_ν)_{μ,ν}` (Hasse derivatives) equals `(∏ a_ν) · det (C(d_ν, μ))_{μ,ν}`. Each Hasse-derivative product `∏_ν D^{(σ ν)} φ_ν` has degree at most `D` and its `t^D` coefficient is `∏ C(d_ν, σ ν) a_ν`.

Variables / typeclasses involved (Lean side):
- `K : Type*` with `[Field K]`: coefficients.
- `l : ℕ`: number of polynomials.
- `φ : Fin l → K[X]`: the family.

Hypotheses (Lean side):
- none.

Conclusion (math): `[t^D] W(φ) = (∏ a_ν) det (C(d_ν, μ))`.

Conclusion (Lean): `(wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) = (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : K)).det`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a computational step (the top-coefficient formula) in the proof of the Wronskian criterion; not a main result and introduces no structure.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 19
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | leading coefficient of Wronskian of polynomials distinct degrees product of leading coefficients Vandermonde | yes | `W(p_1..p_n)` has degree `∑ d_i − C(n,2)` and leading coefficient `(∏ a_i) · ∏_{i<j}(d_j − d_i)` (classical Wronskian normalisation) | arXiv 1801.07980 (Wronskian Hermite polynomials, monic case); arXiv 1301.6598 "Wronskians and linear independence" (monomial computation via falling factorials); arXiv 2410.18867 (distinct degrees ⇒ nonzero) |
| 2 | WebSearch (general form) | degree of Wronskian of polynomials sum of degrees minus n(n-1)/2 leading coefficient formula | yes | same formula; the top term of the Wronskian is the Wronskian of the leading monomials, for arbitrary families (it may vanish) | arXiv 1909.03874; Durán–Pérez–Varona "Some conjectures on Wronskian and Casorati" |
| 3 | WebSearch (named-after / aliases) | Hasse derivative Wronskian polynomials positive characteristic degree bound leading term Garcia Voloch | partial | Hasse Wronskians (Garcia–Voloch, Wang 1998) in characteristic p; degree rule `deg D^{(k)} f ≤ deg f − k` | in char p the Hasse normalisation `det (C(d_ν, μ))` replaces the Vandermonde; arXiv 0807.4332, Wikipedia "Hasse derivative", arXiv 1805.01498 (degrees distinct mod q) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §2 l.182–194 | yes | "The coefficient of `t^D` in the new Wronskian is `(∏ a_ν) det (d_ν choose μ)`… All other contributions have lower total degree" | the exact source; the source states it only for distinct degrees, but the identity is hypothesis-free |
| 6 | nLab | via WebSearch #1 (returned nLab "Vandermonde determinant") | no | — | nLab has a Vandermonde page but nothing on Wronskian leading terms; not a categorical concept |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no Wronskian coefficient formula |
| 9 | MathOverflow / Math.SE | covered by WebSearch #1–#2 (no MO thread surfaced) | no | — | folklore; quoted in papers (Wronskian Hermite polynomials, exceptional orthogonal polynomials) |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2410.18867 (2024/25), 2602.20832 (2026) | confirm the degree/leading-coefficient formula is standard and used |

### Literature summary (Phase 3)

Concept identified as: the leading-term (degree and leading coefficient) formula for the Wronskian of polynomials.
Sources agree on the standard form: yes. For the classical Wronskian, the top coefficient in degree `∑ d_i − C(l,2)` is `(∏ a_i) · ∏_{i<j}(d_j − d_i)`; with Hasse derivatives the Vandermonde is replaced by `det (C(d_ν, μ)) = Δ(d)/∏ μ!` (the source's form).
Most general standard form: over any commutative ring, `[t^{∑ d − C(l,2)}] W(φ) = (∏ lc φ_ν) · det (C(d_ν, μ))`, for any family; and `deg W ≤ ∑ d − C(l,2)`.
Generality dimensions where the literature varies:
  - coefficients: ℚ / ℂ / char-0 fields up to arbitrary commutative rings (Hasse version is char-free).
  - normalisation: classical derivatives (Vandermonde) vs Hasse derivatives (binomial determinant).
  - hypotheses: often stated for distinct degrees (where the coefficient is nonzero), but the identity itself is unconditional.
Disagreement with the literature: none in content; the project's name suggests a distinct-degree hypothesis it does not have.

### Generality analysis — `Roth.coeff_wronskian_of_natDegree_injective`

Literature-standard form (from Phase 3): unconditional identity over any commutative ring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | `[CommRing R]` | yes | Verified: `Evidence.coeff_wronskian` over `[CommRing R]` compiles with the project proof verbatim (helper over `[CommSemiring]`); all mathlib lemmas used (`hasseDeriv_coeff`, `natDegree_hasseDeriv_le`, `hasseDeriv_eq_zero_of_lt_natDegree`, `coeff_mul_add_eq_of_natDegree_le`) are `[Semiring R]`. Needs `Roth.wronskian` itself restated over `CommRing` (parent report) |
| 2 | hypotheses on `φ` | none | none | no | already unconditional |
| 3 | `Fin l` index / `∑ ν` offset | `Fin l` | `Fin n` | no | the offset `∑ ν = C(l,2)` is tied to the row index `0..l−1` |
| 4 | Hasse normalisation | `det (C(d_ν, μ))` | same (char-free) | no | the classical-derivative Vandermonde form requires multiplying by `∏ μ!`; the Hasse form is the char-free one |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`[Field K]` → `[CommRing R]`), verified clean with `lean_diagnostic_messages` on the evidence file; the project statement is recovered as the field specialisation by a term-mode `coeff_wronskian φ` (verified).
Proposed restatement:

```lean
theorem coeff_wronskian_sum_natDegree_sub {R : Type*} [CommRing R] {l : ℕ} (φ : Fin l → R[X]) :
    (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      (∏ ν, (φ ν).leadingCoeff) * (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : R)).det
```
Cost of restatement: CHEAP (proof compiles unchanged in evidence).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no bundled hypotheses |
| 2 | sequences to filters? | no | — | finite algebraic identity |
| 3 | construction vs universal property? | no | — | coefficient computation |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R]` (row 1 above) | integral Wronskians over ℤ; base change via `map_wronskian` (parent evidence) |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `Fin l` is the natural row index for derivative orders |
| 8 | concrete-via-abstract? | no | — | the proof mentions `wronskian` only to unfold it; the content is the coefficient of a determinant of Hasse derivatives, which is exactly the Wronskian; no other witness |
| 9 | false-generalisation guard | no false generalisation | the `CommRing` version is the same identity; specialises definitionally to the project form (evidence (2)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only improvement is the typeclass weakening already recorded in Phase 4b (literature-weakening), plus a rename; no reformulation in a different idiom is called for.

### Proof strategy — `Roth.coeff_wronskian_of_natDegree_injective`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | per-index top coefficient of a product, `coeff (∏ f i) (∑ n i) = ∏ coeff (f i) (n i)` when `natDegree (f i) ≤ n i` (project's private `coeff_prod_of_natDegree_le'`; mathlib only has the uniform-bound `Polynomial.coeff_prod_of_natDegree_le`) | CHEAP (file with the Wronskian PR or separately to Mathlib/Algebra/Polynomial/BigOperators.lean) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (Leibniz expansion + top coefficient of each term, the standard argument and the source's).
  - Missing mathlib API: the per-index `coeff_prod_of_natDegree_le` generalisation (verified over `CommSemiring` in `.mathlib-quality/overview/evidence/Roth.coeff_prod_of_natDegree_le'/` and again here).
  - A natural companion `natDegree (wronskian φ) ≤ ∑ d_ν − ∑ ν` (the n-ary analogue of `Polynomial.natDegree_wronskian_lt_add`) would be the expected sibling lemma in mathlib; not verified here.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.coeff_wronskian_of_natDegree_injective`

[A] Lean-Finder       "top coefficient of determinant of matrix of Hasse derivatives of polynomials"   hits: `Polynomial.sylvesterDeriv`, `Matrix.det_matrixOfPolynomials`, `Polynomial.discr`, `Polynomial.wronskian`, `Polynomial.leadingCoeff_det_X_one_add_C`; none is a Wronskian coefficient formula
[B] Loogle            `Polynomial.coeff, Matrix.det, Polynomial.hasseDeriv`   no hits
[C] LeanSearch        "coefficient of Wronskian determinant of Hasse derivatives equals product of leading coefficients times determinant of binomial coefficients"   hits: `Polynomial.wronskian` (2-ary), `LaurentSeries.hasseDeriv_comp_coeff`, `Polynomial.wronskian_neg_left`, `wronskian_add_right`, `IsCoprime.wronskian_eq_zero_iff`; only 2-ary API
[D] Grep mathlib src  `coeff_wronskian`, `wronskian.*coeff`, `natDegree_wronskian`, `leadingCoeff_wronskian`, files containing both `hasseDeriv` and `det`   only `Polynomial.natDegree_wronskian_lt_add` (2-ary, RingTheory/Polynomial/Wronskian.lean:111) and its use in FLT/MasonStothers.lean; no file combines `hasseDeriv` with `Matrix.det`
[E] Name pattern      grep for qualified names `Roth.coeff_wronskian_of_natDegree_injective`, `Polynomial.coeff_wronskian`, `coeff_wronskian_sum_natDegree_sub`   absent

Searched for both the user's form (field, Hasse Wronskian) and the literature-standard form (commutative ring, degree/leading-coefficient formula for n polynomials).

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form). Mathlib has no n-ary Wronskian at all (`Mathlib/RingTheory/Polynomial/Wronskian.lean` TODO, see parent report `Roth.wronskian`).

### Normal-form check — `Roth.coeff_wronskian_of_natDegree_injective`

Equivalent formalisms:
- coefficient at `∑ d − ∑ ν` (current);
- coefficient at `∑ d − l(l−1)/2` (`Finset.sum_range_id_mul_two`);
- with RHS via `det_choose_eq` as `(∏ a)(∏ μ!)⁻¹ ∏ (d_j − d_i)` (char 0 only);
- `leadingCoeff W = ...` / `natDegree W = ...` under distinct-degree + nonzero hypotheses.

Does mathlib already have a canonical form? No (no n-ary Wronskian).
Proposed canonical form: the current hypothesis-free coefficient identity with the binomial determinant on the RHS (char-free); the Vandermonde form is a corollary via `Roth.det_choose_eq` (or its upstream multiplied form).
RHS convention respected? yes

### Syntactic generality — `Roth.coeff_wronskian_of_natDegree_injective`

Alternative restatements attempted:
- current coefficient identity over `[CommRing R]` (compiles, evidence (1));
- `l * (l - 1) / 2` in place of `∑ ν : Fin l, (ν : ℕ)` (rejected: the proof and call site naturally use the sum via `Equiv.sum_comp`; division form is harder to rewrite);
- `leadingCoeff`/`natDegree` statements under distinct degrees (rejected as the primary form: need nonvanishing of the RHS, which needs `CharZero` or a char-p condition; better as corollaries).

Chosen restatement: the coefficient identity over `[CommRing R]`, with a hypothesis-free name.
Justification: applies to every family with no side conditions; the call site (l.152) feeds it to `simpa` with `det_choose_eq` unchanged.

### Superfluous-argument audit — `Roth.coeff_wronskian_of_natDegree_injective`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R]` suffices (verified) |
| 2 | `l` | yes | size |
| 3 | `φ` | yes | the family |
| 4 | (name suffix `_of_natDegree_injective`) | n/a | refers to a non-existent hypothesis; rename |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`[CommRing R]`, hypothesis-free name)
Superfluous arguments: 1 to drop (`[Field K]` weakened to `[CommRing R]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.coeff_wronskian_of_natDegree_injective`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:152 | `Nat.factorial_ne_zero, hd.eq_iff] using coeff_wronskian_of_natDegree_injective (φ := φ)` (`wronskian_ne_zero_of_natDegree_injective`) |
| Roth/Wronskian.lean:41 | module docstring mention only |

Inline-derivation grep: `grep -rn "hasseDeriv_coeff\|det_apply'" Roth/` — the Leibniz-expansion coefficient computation appears only here (l.127–143); GenWronskian.lean and Separation.lean reach Wronskian nonvanishing through `wronskian_ne_zero_of_linearIndependent`, not by re-deriving the coefficient. (none)

### Composition check (Phase 6)

Can `Roth.coeff_wronskian_of_natDegree_injective` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_apply'` + `Polynomial.finsetSum_coeff` + `Polynomial.coeff_prod_of_natDegree_le`.
  - Mathlib decls used: `Matrix.det_apply'`, `Polynomial.finsetSum_coeff`, `Polynomial.coeff_prod_of_natDegree_le`, `Polynomial.hasseDeriv_coeff`, `Polynomial.natDegree_hasseDeriv_le`
  - Result: fails. Mathlib's product-coefficient lemma has a uniform degree bound; the per-permutation degree bookkeeping (`∑ (d_i − σ i) = ∑ d − ∑ ν`, case split on `σ i ≤ d_i`) is genuine reasoning.
  - Notes: 19-line proof with a `have key` and a case split.

Attempt 2: no mathlib n-ary Wronskian API exists to compose from.
  - Result: fails.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.coeff_wronskian_of_natDegree_injective`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the degree/leading-coefficient formula for Wronskians of polynomials is classical (arXiv 1801.07980, 1301.6598, 2410.18867, 1909.03874) and is the source's displayed step (clean.tex l.182–194); in the Hasse normalisation it is `(∏ a_ν) det (C(d_ν, μ))` in degree `∑ d − C(l,2)`.
- Generality analysis (Phase 4): STRICTLY NARROWER; `[Field K]` → `[CommRing R]` verified clean in evidence; the statement already has no hypotheses on `φ`.
- Mathlib search (Phase 5): not in mathlib; mathlib only has the 2-ary Wronskian and `natDegree_wronskian_lt_add`.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The gap is concrete: `Mathlib/RingTheory/Polynomial/Wronskian.lean` defines only the Wronskian of two polynomials and records the n-ary Wronskian as a TODO; its only degree fact is `natDegree_wronskian_lt_add`. The project lemma is the n-ary leading-term formula, the standard tool for showing that Wronskians of polynomials with distinct degrees do not vanish (the base case of the Wronskian criterion and of Roth-type and Mason–Stothers-type arguments). It is stated without hypotheses, which is the right generality, and its proof uses only `[Semiring]` Hasse-derivative lemmas, so it holds over every commutative ring: the evidence file proves it verbatim for `[CommRing R]` and recovers the project's field statement as a specialisation. It only makes sense in mathlib alongside the n-ary `wronskian` def (parent report `Roth.wronskian`, YES-but-generalise-first), so it should ship in the same PR.

Two restatement points: generalise to `[CommRing R]`, and rename. The suffix `_of_natDegree_injective` advertises a hypothesis the statement does not take (the docstring admits this), which violates mathlib naming conventions; a name like `coeff_wronskian_sum_natDegree_sub` (or `coeff_wronskian_top`) describes the conclusion. It also needs the per-index product-coefficient helper (`Roth.coeff_prod_of_natDegree_le'`, currently private), which mathlib lacks in that form and should be added next to `Polynomial.coeff_prod_of_natDegree_le`.

Reason for the generalisation: LITERATURE-WEAKENING (`Field` → `CommRing`), plus a rename.
Proposed restatement:
```lean
theorem Polynomial.coeff_wronskian_sum_natDegree_sub {R : Type*} [CommRing R] {l : ℕ}
    (φ : Fin l → R[X]) :
    (wronskian φ).coeff (∑ ν, (φ ν).natDegree - ∑ ν : Fin l, (ν : ℕ)) =
      (∏ ν, (φ ν).leadingCoeff) *
        (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : R)).det := by
  sorry -- proved verbatim in evidence (Evidence.coeff_wronskian)
```
Estimated cost of regeneralisation: CHEAP (proof compiles unchanged).
Mathlib downstream this enables:
- with the n-ary `wronskian`, the nonvanishing of Wronskians of distinct-degree families (char 0, or char p with `det (C(d_ν, μ)) ≠ 0`), hence the Wronskian linear-independence criterion;
- integral Wronskians over ℤ via base change (`map_wronskian`, parent evidence);
- a natural sibling `natDegree_wronskian_le` (n-ary analogue of `natDegree_wronskian_lt_add`).
PR grouping: ship in the n-ary Wronskian PR with `Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.wronskian_eq_zero_of_not_linearIndependent`, the per-index `coeff_prod_of_natDegree_le'`, and the `Roth.det_choose_eq` multiplied form (Vandermonde PR) as a dependency for the nonvanishing corollary.
Next action: run `/generalise Roth.coeff_wronskian_of_natDegree_injective` targeting `[CommRing R]` and rename to a hypothesis-free name (update the sole call site Roth/Wronskian.lean:152 and docstring l.41); then include it in the n-ary Wronskian PR to `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

---

## Next step

Generalise to `[CommRing R]` (verified), rename to a hypothesis-free name such as `coeff_wronskian_sum_natDegree_sub`, and upstream with the n-ary Wronskian (`Roth.wronskian`, `Roth.wronskianMatrix`) to `Mathlib/RingTheory/Polynomial/Wronskian.lean`, plus the per-index product-coefficient helper to `Mathlib/Algebra/Polynomial/BigOperators.lean`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.coeff_wronskian_of_natDegree_injective/weaken.lean` (imports `Roth.Wronskian`), checked with `lean_diagnostic_messages`: clean, no errors or warnings. It proves (1) `Evidence.coeff_wronskian` over `[CommRing R]` with the project proof verbatim (helper `coeff_prod_of_natDegree_le'` over `[CommSemiring S]`), (1') elaboration over `ℤ`, (2) the project statement as the `Field` specialisation by `coeff_wronskian φ`.
- Mathlib grep: `coeff_wronskian`, `wronskian.*coeff`, `natDegree_wronskian`, `leadingCoeff_wronskian` hit only the 2-ary `Polynomial.natDegree_wronskian_lt_add` (RingTheory/Polynomial/Wronskian.lean:111) and its use in NumberTheory/FLT/MasonStothers.lean:40; HasseDeriv.lean lemmas used are all in `[Semiring R]` (l.55 variable line).
- LeanSearch, Lean-Finder, Loogle results as in Phase 5 (Loogle: no hits).
- WebSearch: 3 queries (Phase 3 table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn coeff_wronskian_of_natDegree_injective Roth/`: l.41 (docstring), l.122 (decl), l.152 (sole use).
