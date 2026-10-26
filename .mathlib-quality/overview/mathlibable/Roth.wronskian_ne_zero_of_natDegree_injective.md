---
decl: Roth.wronskian_ne_zero_of_natDegree_injective
file: Roth/Wronskian.lean
line: 148
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Nonvanishing of the n-ary (Hasse) Wronskian for nonzero polynomials of distinct degrees is classical (Bostan-Dumas Lemma 3) and absent from mathlib, which has only the 2-ary Wronskian; [Field K] weakens to [CommRing R] [IsDomain R] [CharZero R] and a char-free core with hypothesis det (C(d_nu, mu)) ne 0 holds over any domain (both verified), while CharZero and hφ are necessary (counterexamples verified).
action: Upstream with the n-ary Wronskian PR to Mathlib/RingTheory/Polynomial/Wronskian.lean as a char-free domain lemma (hypothesis det of binomial matrix ne 0) plus the CharZero distinct-degree corollary over [CommRing R] [IsDomain R] [CharZero R]; locally keep (sole call site Roth/Wronskian.lean:210 in wronskian_ne_zero_of_linearIndependent).
---

# Roth.wronskian_ne_zero_of_natDegree_injective

## Inventory entry

### `theorem Roth.wronskian_ne_zero_of_natDegree_injective`
- **Type**: `∀ {K : Type*} [Field K] {l : ℕ} [CharZero K] {φ : Fin l → K[X]}, (∀ ν, φ ν ≠ 0) → Function.Injective (fun ν ↦ (φ ν).natDegree) → wronskian φ ≠ 0`
- **What**: In characteristic zero, nonzero polynomials `φ_0, …, φ_{l-1}` of pairwise distinct degrees have nonzero (Hasse) Wronskian `det (D^{(μ)} φ_ν)`.
- **How**: Assumes `wronskian φ = 0` and `simpa`s the coefficient identity `coeff_wronskian_of_natDegree_injective` (coefficient of `t^{∑d − ∑ν}` is `(∏ lc φ_ν) · det (C(d_ν, μ))`), rewriting the binomial determinant with `det_choose_eq` (`(∏ μ!)⁻¹ ∏_{i<j}(d_j − d_i)`) and closing with `Finset.prod_eq_zero_iff`, `sub_eq_zero`, `Nat.factorial_ne_zero`, `hd.eq_iff`, `hφ`.
- **Hypotheses**: `[Field K]` (section variable), `[CharZero K]`, `hφ : ∀ ν, φ ν ≠ 0`, `hd : Function.Injective fun ν ↦ (φ ν).natDegree`.
- **Uses from project**: `Roth.wronskian`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.det_choose_eq`
- **Used by**: Roth/Wronskian.lean:210 (`wronskian_ne_zero_of_linearIndependent`, base case of the strong induction); module docstring l.30.
- **Visibility**: public
- **Lines**: 148–153, proof length 3 lines
- **Notes**: Short proof because the work is in the two helper lemmas; it is the "distinct degrees ⇒ nonzero" step of §2, first lemma.

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Wronskian.lean:210, base case of the hard direction of `wronskian_eq_zero_iff`.
- Wrapper of 1–2 mathlib calls? No: it combines two project lemmas (coefficient identity, binomial determinant) with a nonvanishing argument.
- Does mathlib have it? No: only the 2-ary `Polynomial.wronskian` exists (no n-ary Wronskian, no nonvanishing criterion beyond `IsCoprime.wronskian_eq_zero_iff`).
- Too specific (inline?)? No: a named, classical statement (distinct degrees ⇒ Wronskian ≠ 0), separately useful, and inlining would bloat the induction.
- Well-chosen? Yes; `[Field K]` is stronger than needed.
- Conclusion: `KEEP` — action: keep; generalise when upstreaming.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name absent from mathlib (grep `wronskian_ne_zero` over `.lake/packages/mathlib/Mathlib/`: no hits). Not a glue lemma (it proves a new fact from two lemmas), so the full workflow is run, reusing the parent assessments `Roth.wronskian` (YES-but-generalise-first), `Roth.coeff_wronskian_of_natDegree_injective` (YES-but-generalise-first) and `Roth.det_choose_eq` (YES-but-generalise-first).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Wronskian` elaborates clean in the LSP)
- decl `Roth.wronskian_ne_zero_of_natDegree_injective`: resolved at Roth/Wronskian.lean:148
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Wronskians of finitely many univariate polynomials (Hasse `l × l` determinant) and the linear-independence criterion in characteristic zero.

### Statement (Phase 1)

`Roth.wronskian_ne_zero_of_natDegree_injective` is a theorem stating: let `K` be a field of characteristic zero and `φ_0, …, φ_{l−1} ∈ K[t]` nonzero polynomials whose degrees are pairwise distinct. Then the Hasse Wronskian `W = det (D^{(μ)} φ_ν)_{μ,ν}` is not the zero polynomial.

Variables / typeclasses involved (Lean side):
- `K` with `[Field K] [CharZero K]`.
- `l : ℕ`, `φ : Fin l → K[X]`.

Hypotheses (Lean side):
- `hφ : ∀ ν, φ ν ≠ 0`
- `hd : Function.Injective fun ν ↦ (φ ν).natDegree`

Conclusion (math): `W(φ_0, …, φ_{l−1}) ≠ 0`.

Conclusion (Lean): `wronskian φ ≠ 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the base case of the Wronskian criterion; a short corollary of the coefficient formula.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (3 lines, single `simpa` after `intro`)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Wronskian of polynomials with distinct degrees is nonzero characteristic zero | yes | Bostan–Dumas, "Wronskians and linear independence" (arXiv 1301.6598) Lemma 3: over a char-0 field, nonzero power series of mutually distinct orders have nonzero Wronskian; arXiv 2602.20832 Thm 2.11 reduces the criterion to distinct degrees + leading term | polynomial/degree version is the same argument at the top end |
| 2 | WebSearch (general / char p) | Hasse Wronskian positive characteristic vanishes linearly independent polynomials x^p counterexample | yes | ordinary Wronskian of `1, x^p` vanishes in char p; Hasse Wronskians (Garcia–Voloch 1987, Wang 1999) restore a criterion with gap sequences | shows char-0 (or a condition on the degrees mod p) is needed for the fixed rows `0..l−1` |
| 3 | WebSearch (named-after / aliases) | generalized Wronskian n polynomials leading coefficient Vandermonde degrees nonvanishing lemma | yes | arXiv 1801.07980 (monic: leading coeff `Δ(n)`); arXiv 1805.01498 Lemma A.1: over `F_q`, degrees pairwise incongruent mod q ⇒ Hasse Wronskian nonsingular, via the binomial determinant | supports the char-free core "binomial determinant ≠ 0 ⇒ W ≠ 0" |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §2 l.157–202 | yes | "Thus the new Wronskian, and hence the original one, is nonzero" (l.194), for distinct degrees `d_0 < ⋯ < d_{l−1}` over ℚ | the exact source statement |
| 6 | nLab | — | n/a | — | not a categorical concept |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | no Wronskian criterion for polynomials there |
| 9 | MathOverflow / Math.SE | covered by WebSearch #1–#3 (no thread surfaced) | no | — | folklore; Wikipedia "Wronskian" gives the `1, x^p` counterexample |
| 10 | recent arXiv (last 5 years) | results of #1–#3 | yes | arXiv 2410.18867 (2024), 2602.20832 (2026) | confirm the statement is standard and in active use |

### Literature summary (Phase 3)

Concept identified as: nonvanishing of the Wronskian of polynomials (or power series) with distinct degrees (orders).
Sources agree on the standard form: yes — char-0 field, nonzero elements with pairwise distinct degrees ⇒ Wronskian ≠ 0, proved via the leading (Vandermonde) term.
Most general standard form: over a characteristic-zero integral domain (no division used); in the Hasse normalisation, over any integral domain provided the binomial determinant `det (C(d_ν, μ))` is nonzero (e.g. degrees pairwise incongruent mod p and `< p` in char p, arXiv 1805.01498).
Generality dimensions where the literature varies:
  - coefficients: ℚ / char-0 fields / domains; char p with conditions on degrees.
  - objects: polynomials (degree) vs power series (order).
Disagreement with the literature: none.

### Generality analysis — `Roth.wronskian_ne_zero_of_natDegree_injective`

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Field K]` | field | `[CommRing R] [IsDomain R]` | yes | Verified: `Evidence.wronskian_ne_zero_of_natDegree_injective` over `[CommRing R] [IsDomain R] [CharZero R]` (uses the CommRing coefficient identity and the char-free `prod_factorial_mul_det_choose` instead of `det_choose_eq`'s inverses). Domain needed for `∏ lc ≠ 0` |
| 2 | `[CharZero K]` + `hd` | char 0 and distinct degrees | `det (C(d_ν, μ)) ≠ 0` | yes (as a separate char-free core) | Verified: `Evidence.wronskian_ne_zero_of_det_choose_ne_zero` over any domain. `CharZero` cannot simply be dropped from the distinct-degree form: `1, X^2` over `ZMod 2` have Wronskian 0 (verified) |
| 3 | `hφ : ∀ ν, φ ν ≠ 0` | all nonzero | same | no | Verified counterexample: the one-element family `![0]` has Wronskian 0 |
| 4 | `hd` injective degrees | `Function.Injective` | same | no | needed (e.g. `φ_0 = φ_1` gives 0) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 2 (`Field` → `CommRing`+`IsDomain` for the CharZero form; char-free core with `det (C(d_ν, μ)) ≠ 0`), both verified clean with `lean_diagnostic_messages`; the project statement is recovered as the field specialisation (verified).
Proposed restatement:

```lean
theorem wronskian_ne_zero_of_det_choose_ne_zero {R : Type*} [CommRing R] [IsDomain R] {l : ℕ}
    {φ : Fin l → R[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hdet : (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : R)).det ≠ 0) :
    wronskian φ ≠ 0

theorem wronskian_ne_zero_of_natDegree_injective {R : Type*} [CommRing R] [IsDomain R]
    [CharZero R] {l : ℕ} {φ : Fin l → R[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν ↦ (φ ν).natDegree) : wronskian φ ≠ 0
```
Cost of restatement: CHEAP (both proofs are a few lines in evidence, given the CommRing versions of the parent lemmas).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | — |
| 2 | sequences to filters? | no | — | — |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to (semi)ring? | yes | `[CommRing R] [IsDomain R]` (row 1) | ℤ[X] families directly |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `Fin l` rows are derivative orders |
| 8 | concrete-via-abstract? | no | — | — |
| 9 | false-generalisation guard | checked | dropping `CharZero` is false (ZMod 2 counterexample); the char-free version carries the `det ≠ 0` hypothesis instead | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: only typeclass weakening and an extra char-free core, recorded in Phase 4b.

### Proof strategy — `Roth.wronskian_ne_zero_of_natDegree_injective`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | uses the n-ary Wronskian coefficient formula and the binomial-determinant/Vandermonde identity, both missing from mathlib (parent reports) | CHEAP, same PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (leading-coefficient argument, as in the literature and the source). Upstream it should go through the char-free `det ≠ 0` core and `prod_factorial_mul_det_choose` + `Nat.cast_inj` rather than the `⁻¹` form of `det_choose_eq`, avoiding division.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.wronskian_ne_zero_of_natDegree_injective`

[A] Lean-Finder       "determinant of matrix of Hasse derivatives of nonzero polynomials with pairwise distinct degrees is nonzero"   hits: `Matrix.det_mvPolynomialX_ne_zero`, `Matrix.det_matrixOfPolynomials`, `Polynomial.sylvesterDeriv`, `Polynomial.discr`, `Matrix.det_vandermonde_ne_zero_iff`; none is a Wronskian nonvanishing result
[B] Loogle            `Matrix.det, Polynomial.hasseDeriv`   no hits
[C] LeanSearch        "Wronskian of polynomials with distinct degrees is nonzero"   hits: 2-ary `Polynomial.wronskian`, `IsCoprime.wronskian_eq_zero_iff`, `degree_wronskian_lt_add`, `wronskian_self_eq_zero`, ...; only 2-ary API
[D] Grep mathlib src  `wronskian_ne_zero`, `wronskian.*natDegree`, files with both `hasseDeriv` and `det`   only `Polynomial.natDegree_wronskian_lt_add` (2-ary); no file combines `hasseDeriv` with a determinant
[E] Name pattern      `Roth.wronskian_ne_zero_of_natDegree_injective`, `Polynomial.wronskian_ne_zero*`   absent

Searched for both the user's form (char-0 field) and the literature-standard form (domain, distinct degrees / binomial determinant).

Concluded: not in mathlib (all 5 methods exhausted). Mathlib has no n-ary Wronskian (TODO in `Mathlib/RingTheory/Polynomial/Wronskian.lean`).

### Normal-form check — `Roth.wronskian_ne_zero_of_natDegree_injective`

Equivalent formalisms:
- `wronskian φ ≠ 0` (current);
- `natDegree (wronskian φ) = ∑ d − ∑ ν` and `leadingCoeff = (∏ lc) det (C(d, μ))` (stronger, needs the n-ary degree bound);
- distinct degrees as `Function.Injective (natDegree ∘ φ)` vs `Pairwise (· ≠ ·)` on degrees.

Does mathlib already have a canonical form? No.
Proposed canonical form: `≠ 0` with `Function.Injective fun ν ↦ (φ ν).natDegree` (as now); the leading-coefficient form is a natural later sibling.
RHS convention respected? yes

### Syntactic generality — `Roth.wronskian_ne_zero_of_natDegree_injective`

Alternative restatements attempted:
- over `[CommRing R] [IsDomain R] [CharZero R]` (compiles, evidence (2), also over ℤ);
- char-free core with `hdet` (compiles, evidence (1));
- dropping `CharZero` (refuted, evidence (4)); dropping `hφ` (refuted, evidence (5)).

Chosen restatement: both the char-free core and the CharZero corollary over a domain.
Justification: the call site (l.210) uses it over a char-0 field, recovered by specialisation (evidence (3)).

### Superfluous-argument audit — `Roth.wronskian_ne_zero_of_natDegree_injective`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Field K]` | no | `[CommRing R] [IsDomain R]` suffices (verified) |
| 2 | `[CharZero K]` | yes (for this form) | counterexample in `ZMod 2`; replaceable by `hdet` in the core |
| 3 | `hφ` | yes | counterexample `![0]` |
| 4 | `hd` | yes | equal members give 0 |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`[CommRing R] [IsDomain R] [CharZero R]`, plus char-free core)
Superfluous arguments: 0 to drop (1 to weaken: `[Field K]`)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.wronskian_ne_zero_of_natDegree_injective`

Internal use count: 1 inside the declaring file; 0 outside.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Wronskian.lean:210 | `· exact wronskian_ne_zero_of_natDegree_injective h.ne_zero hinj` (`wronskian_ne_zero_of_linearIndependent`) |
| Roth/Wronskian.lean:30 | module docstring mention only |

Inline-derivation grep: `grep -rn "det_choose_eq\|coeff_wronskian_of_natDegree_injective" Roth/` — used only here (l.151–152); GenWronskian.lean and Separation.lean go through `wronskian_ne_zero_of_linearIndependent` / `wronskian_eq_zero_iff`. (none)

### Composition check (Phase 6)

Can `Roth.wronskian_ne_zero_of_natDegree_injective` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_vandermonde_ne_zero_iff` + `Matrix.det_ne_zero_of_...` on the Hasse matrix.
  - Mathlib decls used: `Matrix.det_vandermonde_ne_zero_iff`
  - Result: fails. Mathlib has no n-ary Wronskian, no coefficient formula for it, and no binomial-determinant identity; the leading-term computation is genuine work (project lemmas, 19 + 8 lines).

Attempt 2: from the project helpers, it is 3 lines — but those helpers are themselves not in mathlib.
  - Result: fails as a mathlib-only composition.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.wronskian_ne_zero_of_natDegree_injective`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): classical (Bostan–Dumas Lemma 3, arXiv 1301.6598; arXiv 2602.20832 Thm 2.11; Hasse variant arXiv 1805.01498 Lemma A.1); the source's step at clean.tex l.194.
- Generality analysis (Phase 4): STRICTLY NARROWER; `Field` → `CommRing`+`IsDomain`+`CharZero` verified, char-free `det ≠ 0` core verified; `CharZero` and `hφ` shown necessary by verified counterexamples.
- Mathlib search (Phase 5): not in mathlib (only the 2-ary Wronskian).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's `Mathlib/RingTheory/Polynomial/Wronskian.lean` defines only the Wronskian of two polynomials, and lists the n-ary Wronskian as a TODO. This lemma, that nonzero polynomials with pairwise distinct degrees have nonzero Wronskian, is the standard base case of the Wronskian criterion for linear independence. It is a natural member of an n-ary Wronskian API, next to `Roth.wronskian`, `Roth.coeff_wronskian_of_natDegree_injective` and `Roth.wronskian_eq_zero_of_not_linearIndependent`, which are all assessed YES-but-generalise-first. Its proof uses no division once it goes through the char-free binomial-determinant identity (`prod_factorial_mul_det_choose`, parent `Roth.det_choose_eq` evidence). So it holds over any characteristic-zero domain. Separately, the char-free core "nonzero family with `det (C(d_ν, μ)) ≠ 0` ⇒ `W ≠ 0`" holds over any domain and covers the char-p statements in the literature. The evidence file also checks that neither `CharZero` nor `hφ` can be dropped.

Reason for the generalisation: LITERATURE-WEAKENING (`Field` → domain), plus a char-free core.
Proposed restatement:
```lean
theorem Polynomial.wronskian_ne_zero_of_det_choose_ne_zero {R : Type*} [CommRing R] [IsDomain R]
    {l : ℕ} {φ : Fin l → R[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hdet : (Matrix.of fun μ ν : Fin l ↦ ((φ ν).natDegree.choose μ : R)).det ≠ 0) :
    wronskian φ ≠ 0 := by
  sorry -- proved in evidence (Evidence.wronskian_ne_zero_of_det_choose_ne_zero)

theorem Polynomial.wronskian_ne_zero_of_natDegree_injective {R : Type*} [CommRing R] [IsDomain R]
    [CharZero R] {l : ℕ} {φ : Fin l → R[X]} (hφ : ∀ ν, φ ν ≠ 0)
    (hd : Function.Injective fun ν ↦ (φ ν).natDegree) : wronskian φ ≠ 0 := by
  sorry -- proved in evidence (Evidence.wronskian_ne_zero_of_natDegree_injective)
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
- the hard direction of the n-ary Wronskian criterion (linear independence ⇒ `W ≠ 0`) in char 0;
- char-p nonvanishing statements via the `det ≠ 0` core.
PR grouping: the n-ary Wronskian PR (with `Roth.wronskianMatrix`, `Roth.wronskian`, `Roth.coeff_wronskian_of_natDegree_injective`, `Roth.wronskian_eq_zero_of_not_linearIndependent`); depends on the Vandermonde PR for `prod_factorial_mul_det_choose` (parent `Roth.det_choose_eq`).
Next action: run `/generalise Roth.wronskian_ne_zero_of_natDegree_injective` targeting `[CommRing R] [IsDomain R] [CharZero R]` with the char-free core, then include it in the n-ary Wronskian PR to `Mathlib/RingTheory/Polynomial/Wronskian.lean`.

---

## Next step

Generalise to a characteristic-zero commutative domain and add the char-free `det (C(d_ν, μ)) ≠ 0` core (both verified), then upstream with the n-ary Wronskian to `Mathlib/RingTheory/Polynomial/Wronskian.lean`; locally keep (call site Roth/Wronskian.lean:210).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.wronskian_ne_zero_of_natDegree_injective/weaken.lean` (imports `Roth.Wronskian`, `Mathlib.Algebra.Field.ZMod`), checked with `lean_diagnostic_messages`: no errors. The only warnings are flexible-`simp` linter notes on the counterexample. It proves (1) `Evidence.wronskian_ne_zero_of_det_choose_ne_zero` over `[CommRing R] [IsDomain R]`; (2) `Evidence.wronskian_ne_zero_of_natDegree_injective` over `[CommRing R] [IsDomain R] [CharZero R]`, with (2') an instance over ℤ; (3) the project statement as the field specialisation; (4) `Roth.wronskian (K := ZMod 2) ![1, X ^ 2] = 0` (`CharZero` needed); (5) `Roth.wronskian ![(0 : ℚ[X])] = 0` (`hφ` needed). The CommRing coefficient identity and the char-free binomial determinant identity are copied from the sibling evidence files.
- Mathlib grep `wronskian_ne_zero`, `wronskian.*natDegree`: only 2-ary `natDegree_wronskian_lt_add`; no file combines `hasseDeriv` and a determinant.
- LeanSearch, Lean-Finder, Loogle as in Phase 5 (Loogle: no hits).
- WebSearch: 3 queries (Phase 3 table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn wronskian_ne_zero_of_natDegree_injective Roth/`: l.30 (docstring), l.148 (decl), l.210 (sole use).
