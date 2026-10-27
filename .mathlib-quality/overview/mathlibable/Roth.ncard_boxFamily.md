---
decl: Roth.ncard_boxFamily
file: Roth/MainLemma.lean
line: 311
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Re-aimed per Roth.boxFamily at the multivariate generalisation of Polynomial.ncard_boxPoly - the number of polynomials with support in a finite monomial set S and coeff d in a finite set U d is the product of the card of U d over S (any CommSemiring R), with the integer-interval form as corollary; absent from mathlib, compiles in evidence, and ncard_boxFamily follows from it.
action: Upstream MvPolynomial.ncard_setOf_support_subset_coeff_mem (plus the Icc corollary) to Mathlib/RingTheory/MvPolynomial/Basic.lean next to restrictSupport, grouped with the finiteness lemma from Roth.boxFamily_finite, and consider re-proving Polynomial.ncard_boxPoly (Mathlib/NumberTheory/MahlerMeasure.lean:57) from a univariate analogue; locally keep ncard_boxFamily (one call site Roth/MainLemma.lean:373) and re-derive it from the general lemma.
---

# Roth.ncard_boxFamily

## Inventory entry

### `theorem Roth.ncard_boxFamily`
- **Type**: `∀ {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ), (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1)`
- **What**: The family `𝒲` of integer polynomials with `degreeOf j W ≤ r j` and all coefficients in `[0, B]` has exactly `(B+1)^N` elements, `N = ∏ᶠ j, (r j + 1)` the number of monomials in the box `d ≤ r`.
- **How**: Rewrites with the private `boxFamily_eq_image_finsupp_aux` (image of `Finset.finsupp (Finset.Iic (ofSupportFinite r _)) (fun _ ↦ Icc 0 B)` under `AddMonoidAlgebra.ofCoeff`), then `Set.ncard_image_of_injective` with `AddMonoidAlgebra.ofCoeff_injective`, `Set.ncard_coe_finset`, `Finset.card_finsupp`; simplifies with `Int.card_Icc`, `Finsupp.card_Iic`, `Nat.card_Iic`, and converts the finset product to a `finprod` via `finprod_eq_prod_of_mulSupport_subset`.
- **Hypotheses**: `[Finite (Function.support r)]` (needed: otherwise the box of monomials is infinite and `ncard` is junk 0).
- **Uses from project**: `Roth.boxFamily`, `Roth.boxFamily_eq_image_finsupp_aux` (private)
- **Used by**: Roth/MainLemma.lean:373 (`exists_ne_modByMonic_eq`, in the `simpa` computing `Fintype.card` of the box family for the pigeonhole); mentioned in the module docstring l.43. No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 311–318, proof length 6 lines
- **Notes**: Source §6, proof of Lemma 9 (`.mathlib-quality/references/clean.tex` l.1415, `|𝒲| = (B_1+1)^r`). Sibling of `boxFamily_finite`.

## Junk check (Step 8)
- Used anywhere? Yes, once (l.373).
- Wrapper of 1–2 mathlib calls? No: a rewrite chain over a private bijection plus a finprod conversion.
- Does mathlib have it? Not multivariate. Univariate analogue `Polynomial.ncard_boxPoly` (Mathlib/NumberTheory/MahlerMeasure.lean:57, ℤ, `natDegree ≤ n`, real bounds via floor/ceil).
- Too specific? The box/`[0,B]` form is project-specific, but it is the natural count statement for the Lemma 9 pigeonhole; inlining would duplicate the bijection.
- Well-chosen? Yes locally; the general form (finite monomial set, per-monomial finite coefficient sets) is the mathlib-shaped statement.
- Conclusion: `KEEP` — action: keep; re-derive from the general lemma once available.

## Mathlibable assessment (Step 9)

Pre-filter: not private; no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; `grep -rn ncard_boxFamily .lake/packages/mathlib/Mathlib` empty. Not a glue lemma. Parent `Roth.boxFamily` is `NO-composable-from-mathlib` and explicitly directs re-aiming `ncard_boxFamily` at a multivariate generalisation of `Polynomial.ncard_boxPoly`; full run done, re-aimed accordingly.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` elaborates with no diagnostics)
- decl `Roth.ncard_boxFamily`: resolved at Roth/MainLemma.lean:311
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's main lemma (Lemma 9 of the source): auxiliary polynomial construction via a pigeonhole/box argument with explicit coefficient bounds.

### Statement (Phase 1)

`Roth.ncard_boxFamily` is a theorem stating the following: let `r ∈ ℕ^σ` have finite support and `B ≥ 0`. The set of polynomials `W ∈ ℤ[x_j : j ∈ σ]` with `deg_{x_j} W ≤ r_j` for all `j` and all coefficients in `{0,…,B}` has exactly `(B+1)^N` elements, where `N = ∏_j (r_j + 1)` is the number of monomials `x^d` with `d ≤ r`. Indeed such `W` correspond bijectively to coefficient vectors indexed by the monomial box, each entry free in `{0,…,B}`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables, arbitrary.
- `r : σ → ℕ` — degree bounds.
- `B : ℕ` — coefficient bound.

Hypotheses (Lean side):
- `[Finite (Function.support r)]` — finitely many variables occur, so the box is finite.

Conclusion (math): `|𝒲(r,B)| = (B+1)^{∏_j (r_j+1)}`.

Conclusion (Lean): `(boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a counting helper for one pigeonhole step; not a structure, not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a (kind is theorem, not def). Proof body 6 lines.

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | number of integer polynomials with coefficients in boxes product of interval lengths Siegel lemma counting multivariate | partial | Siegel-lemma / counting papers (arXiv 2110.13257, math/0409374, Schinzel Monatsh. 2002) use the product-of-interval-lengths count without naming it | count is used as an elementary step |
|  2 | WebSearch (general form) | cardinality of set of finitely supported functions with values in finite sets product formula polynomials coefficient vector bijection | yes | polynomials = finitely supported coefficient functions; for finite index the count is a product (`#(α →₀ β) = #β^#α`, Mathlib SetTheory/Cardinal/Finsupp docs) | general form: support in finite `S`, coefficient `d` in finite `U d`, count `∏ #(U d)` |
|  3 | WebSearch (named-after / aliases) | "Northcott" number of integer polynomials of degree at most n height at most H equals (2H+1)^(n+1) | yes | `(2H+1)^n` monic / `2H(2H+1)^n` exact-degree counts (Dubickas–Sha arXiv 1707.04965, 2409.08625) | box count of height-bounded polynomials, univariate |
|  4 | ChatGPT MCP | n/a | n/a | — | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for `B_1+1` | yes | l.1415: `|𝒲| = (B_1+1)^r` | source of the statement |
|  6 | nLab | counting polynomials with bounded coefficients | no | — | elementary combinatorics; no nLab entry |
|  7 | nCatLab | n/a | n/a | — | not a categorical concept |
|  8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry statement |
|  9 | MathOverflow / Math.SE | counting integer polynomials of bounded height (via #1, #3 hits) | yes | product of interval lengths; treated as exercise-level | no named result |
| 10 | recent arXiv | arXiv 2409.08625 (2024), 2110.13257 (2021) | yes | same elementary box count as a first step | no general named object |

### Literature summary (Phase 3)

Concept identified as: the box count of polynomials with prescribed support and bounded coefficients (domain size in the Dirichlet box principle of Siegel's lemma; counting step in Northcott-type arguments).
Sources agree on the standard form: yes — the number of polynomials with monomials in a finite set `S` and coefficient at `d` in a finite set `U_d` is `∏_{d∈S} |U_d|`; for integer intervals `[a_d,b_d]` this is `∏ (b_d - a_d + 1)`.
Most general standard form: any coefficient ring, finite monomial set `S`, per-monomial finite coefficient sets.
Generality dimensions where the literature varies:
  - support: box `d ≤ r`, total degree ≤ n, arbitrary finite set — most general: arbitrary finite `S`;
  - coefficients: `[0,B]`, `[-H,H]`, per-monomial intervals, arbitrary finite sets — most general: arbitrary finite `U_d`;
  - ring: ℤ in applications; the count needs no ring structure (only the coefficient bijection).
Disagreement with the literature: none; the user's form is the box/`[0,B]`/ℤ specialisation.

### Generality analysis — `Roth.ncard_boxFamily`

Literature-standard form: `{p : MvPolynomial σ R | ↑p.support ⊆ S ∧ ∀ d ∈ S, p.coeff d ∈ U d}.ncard = ∏ d ∈ S, #(U d)`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|------------------------|-------------------|--------------------------|---------------------|--------|
| 1 | coefficient ring | `ℤ` | any `CommSemiring R` | yes | evidence lemma compiles for `[CommSemiring R]` |
| 2 | coefficient condition | `0 ≤ c ≤ B`, same for all monomials | `c ∈ U d`, per-monomial finite set | yes | only `Finset.card_finsupp` used; evidence |
| 3 | support condition | `∀ j, degreeOf j W ≤ r j` | `↑W.support ⊆ S`, `S : Finset` | yes | box is `S = Finset.Iic r` (evidence corollary) |
| 4 | `[Finite (Function.support r)]` | finite support of `r` | `S` a `Finset` | no (same role) | needed for a finite count |
| 5 | RHS shape | `(B+1)^(∏ᶠ j, (r j+1))` | `∏ d ∈ S, #(U d)` | n/a | box shape gives the power via `prod_const`, `Finsupp.card_Iic` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — verified: `MvPolynomial.ncard_setOf_support_subset_coeff_mem` and its interval corollary `..._Icc` compile (`lean_diagnostic_messages` clean, no warnings), and `Roth.ncard_boxFamily` is re-derived from them in the same evidence file.
Number of weakening opportunities found: 3 (ring, coefficient sets, support set)
Proposed restatement:

```lean
theorem MvPolynomial.ncard_setOf_support_subset_coeff_mem {σ R : Type*} [CommSemiring R]
    (S : Finset (σ →₀ ℕ)) (U : (σ →₀ ℕ) → Finset R) :
    {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d ∈ S, p.coeff d ∈ U d}.ncard =
      ∏ d ∈ S, #(U d)

theorem MvPolynomial.ncard_setOf_support_subset_coeff_mem_Icc {σ : Type*}
    (S : Finset (σ →₀ ℕ)) (a b : (σ →₀ ℕ) → ℤ) :
    {p : MvPolynomial σ ℤ | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧
      ∀ d ∈ S, a d ≤ p.coeff d ∧ p.coeff d ≤ b d}.ncard = ∏ d ∈ S, (b d + 1 - a d).toNat
```

Cost of restatement: CHEAP (both proofs compiled: 9 lines and 1 line).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream |
|----|----------|----------|------------------------|--------------------|
|  1 | preambles → typeclasses | no | no structure preamble | — |
|  2 | sequences → filters | no | finite combinatorial identity | — |
|  3 | construction → universal property | no | a count | — |
|  4 | set-with-predicate → bundled substructure | partly | support condition as `p ∈ restrictSupport R S` | `mem_restrictSupport_iff` |
|  5 | field-specific → weaker typeclass | yes | ℤ → `CommSemiring R` | finite rings, ℕ, number rings |
|  6 | higher-categorical | no | — | — |
|  7 | concrete index → general | yes | box `d ≤ r`, uniform `[0,B]` → finite `S`, per-monomial `U d` | `Finset.finsupp`, `Finset.card_finsupp` users |
|  8 | concrete-via-abstract | yes | after `rw [boxFamily_eq_image_finsupp_aux]` the proof never mentions `boxFamily`; it uses only injectivity of `ofCoeff` and `Finset.card_finsupp`, with the box shape entering only in the final arithmetic | general lemma; `ncard_boxFamily` becomes a corollary |
|  9 | false-generalisation guard | no false generalisation | `S = Iic r`, `U d = Icc 0 B` describes exactly `boxFamily r B` (set equality proved in evidence) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.ncard_setOf_support_subset_coeff_mem` above, with the integer interval corollary as the multivariate `ncard_boxPoly`.
  - Cost: CHEAP
  - Mathlib downstream this enables: a multivariate counterpart of `Polynomial.ncard_boxPoly` (MahlerMeasure.lean:57) for Siegel-lemma style arguments; the univariate analogue (support ⊆ `range (n+1)`) would give a 2-line proof of `ncard_boxPoly` replacing its `toFn`/`ofFn` bijection; pairs with the finiteness lemma from `Roth.boxFamily_finite`.
  - Real mathematical improvement: one general counting lemma replaces the ad-hoc bijections in `ncard_boxPoly` and the project's box-specific proof.

### Proof strategy — `Roth.ncard_boxFamily`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|----------|----------|------------------------|------|
| 1 | topology ε-δ | no | — | — |
| 2 | elements vs. submodule inclusions | no | — | — |
| 3 | sequences vs. filters | no | — | — |
| 4 | universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `MvPolynomial.ncard_setOf_support_subset_coeff_mem` | CHEAP (follow-up PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (image of `Finset.finsupp` under `ofCoeff`, `Finset.card_finsupp`); modulo the missing general lemma it is a set-equality plus arithmetic.
  - Missing mathlib API: the general count lemma above.
  - Would refactoring make the proof strictly shorter? yes for the counting part (the private aux bijection becomes unnecessary); the box-to-support set equality remains.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.ncard_boxFamily`

[A] Lean-Finder       "cardinality of the set of polynomials with coefficients bounded in intervals is the product of the interval lengths" → `Polynomial.card_eq_of_natDegree_le_of_coeff_le` (= `ncard_boxPoly`, univariate ℤ), `Behrend.card_box`, `DFinsupp.card_uIcc`, `Polynomial.card_mahlerMeasure_le_prod`; no multivariate count
[B] Loogle            `Set.ncard, MvPolynomial.coeff` → query error (unknown identifier form); n/a beyond [C]/[D]
[C] LeanSearch        "number of multivariate polynomials with support in a finite set and coefficients in given finite sets equals product of cardinalities" → `MvPolynomial.coeffs`, `Finsupp.card_pi`, `MvPolynomial.cardinalMk_eq_max`, `FirstOrder.Ring.mvPolynomialSupportLEEquiv` (equiv of support-bounded polynomial families with coefficient functions; building block only)
[D] Grep mathlib src  `ncard_boxFamily` (none); `ncard_setOf_support`, `card_setOf_coeff`, `ncard.*coeff` → only MahlerMeasure.lean:57/78/81 (`ncard_boxPoly` and its use)
[E] Name pattern      `lean_local_search` not used (ripgrep unavailable per earlier reports); replaced by grep [D]

Searched for both:
  - the user's current form (multivariate, box, `[0,B]`, ℤ) — not in mathlib;
  - the literature-standard form (finite `S`, per-monomial finite `U d`, any ring) — not in mathlib; only univariate ℤ `ncard_boxPoly`.

Concluded: found a partial match (`Polynomial.ncard_boxPoly`, univariate); building blocks `Finset.card_finsupp`, `Finset.mem_finsupp_iff`, `AddMonoidAlgebra.ofCoeff_injective`, `Set.ncard_image_of_injective`, `Set.ncard_coe_finset`; multivariate general form not in mathlib.

### Normal-form check — `Roth.ncard_boxFamily`

Equivalent formalisms: `Set.ncard = …`; `Nat.card ↥s = …`; `Fintype.card`; `Finset.card` of a constructed finset.
Does mathlib have a canonical form? `Set.ncard` of a set-builder, as in `ncard_boxPoly`.
Our statement uses `Set.ncard`: OK. RHS convention: closed-form count on RHS — OK.

### Syntactic generality — `Roth.ncard_boxFamily`

Alternative restatements attempted:
- general `support ⊆ S ∧ ∀ d ∈ S, coeff d ∈ U d` with `∏ #(U d)` (compiled);
- integer intervals `a d ≤ coeff d ≤ b d` with `∏ (b d + 1 - a d).toNat` (compiled);
- the box form with `finprod` (original).
Chosen restatement: the general `U d` form, plus the `Icc` corollary.
Justification: callers supply a `Finset` of monomials and coefficient finsets directly; the `Icc` corollary matches `ncard_boxPoly`'s shape for integer bounds.

### Superfluous-argument audit — `Roth.ncard_boxFamily`

| # | Argument / typeclass | Essentially used? | Notes |
|---|----------------------|-------------------|-------|
| 1 | `σ : Type*` | yes | arbitrary |
| 2 | `r : σ → ℕ` | yes | defines the box |
| 3 | `[Finite (Function.support r)]` | yes | otherwise the count is infinite (`ncard` junk) |
| 4 | `B : ℕ` | yes | coefficient bound |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (for mathlib: general `S`, `U d`, `R` form)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (ship the general lemma; keep the box form as a project corollary)

### Call sites — `Roth.ncard_boxFamily`

Internal use count: 0 outside the declaring file (1 use inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern |
|------------------|---------------|
| Roth/MainLemma.lean:373 | `simpa only [..., Set.fintypeCard_eq_ncard, ncard_boxFamily, ...]` in `exists_ne_modByMonic_eq` |

Inline-derivation grep:
  - Mathlib/NumberTheory/MahlerMeasure.lean:57–69 (`Polynomial.ncard_boxPoly`): univariate instance via an explicit `toFn`/`ofFn` bijection and `Pi.card_Icc`.

### Composition check (Phase 6)

Can `Roth.ncard_boxFamily` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [set eq, Set.ncard_image_of_injective _ ofCoeff_injective, Set.ncard_coe_finset, Finset.card_finsupp]` — needs the set equality with `ofCoeff '' (Iic r).finsupp _` (a ~10-line proof, the project's private aux) and the finprod arithmetic.
  - Mathlib decls used: `AddMonoidAlgebra.ofCoeff_injective`, `Set.ncard_image_of_injective`, `Set.ncard_coe_finset`, `Finset.card_finsupp`, `Finsupp.card_Iic`, `finprod_eq_prod_of_mulSupport_subset`
  - Result: partial (works, but is a real proof)
Attempt 2: `FirstOrder.Ring.mvPolynomialSupportLEEquiv` + `Nat.card_congr` — the equiv is for families indexed by `ι` over a `CommRing` with unconstrained coefficients; adapting it to coefficient constraints is a real proof.
  - Result: fails as a short composition.

Conclusion: NOT-COMPOSABLE.

## Verdict: `Roth.ncard_boxFamily`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the product count of polynomials with prescribed support and bounded coefficients is the standard box count (Siegel's lemma, height counting); most general form uses a finite monomial set and per-monomial finite coefficient sets.
- Generality analysis (Phase 4): STRICTLY NARROWER; general lemma and `Icc` corollary compiled, original re-derived (evidence file).
- Mathlib search (Phase 5): only univariate `Polynomial.ncard_boxPoly`; no multivariate or general-coefficient-set count.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

After the rewrite with the private aux lemma, the proof uses only injectivity of `ofCoeff` and `Finset.card_finsupp`; ℤ, the order and the box shape enter only in the final arithmetic. The general lemma `MvPolynomial.ncard_setOf_support_subset_coeff_mem` (any `CommSemiring R`, `S : Finset (σ →₀ ℕ)`, `U : (σ →₀ ℕ) → Finset R`) is proved in 9 lines because its set-builder matches `Finset.mem_finsupp_iff` exactly (no `0 ∈ U d` side condition needed), and the integer interval form is a one-line `simpa`. `ncard_boxFamily` follows by a set equality with `S = Finset.Iic (ofSupportFinite r _)` and the same finprod arithmetic.

The concrete gap: mathlib has only the univariate, ℤ-specific `Polynomial.ncard_boxPoly` (MahlerMeasure.lean:57), proved via an ad-hoc `toFn`/`ofFn` bijection; there is no multivariate count, and no count for general coefficient sets. This is exactly the re-aim target named in the `Roth.boxFamily` report. The project-specific box statement stays local.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (Q8 concrete-via-abstract fired).
Proposed restatement:
```lean
theorem MvPolynomial.ncard_setOf_support_subset_coeff_mem {σ R : Type*} [CommSemiring R]
    (S : Finset (σ →₀ ℕ)) (U : (σ →₀ ℕ) → Finset R) :
    {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d ∈ S, p.coeff d ∈ U d}.ncard =
      ∏ d ∈ S, #(U d) := by
  classical
  have : {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d ∈ S, p.coeff d ∈ U d} =
      AddMonoidAlgebra.ofCoeff '' (S.finsupp U : Set ((σ →₀ ℕ) →₀ R)) := by
    ext p
    constructor
    · rintro ⟨hp, hc⟩
      exact ⟨p.coeff, Finset.mem_finsupp_iff.2 ⟨fun d hd ↦ hp hd, hc⟩, rfl⟩
    · rintro ⟨c, hc, rfl⟩
      exact Finset.mem_finsupp_iff.1 hc
  rw [this, Set.ncard_image_of_injective _ AddMonoidAlgebra.ofCoeff_injective,
    Set.ncard_coe_finset, Finset.card_finsupp]
```
plus `MvPolynomial.ncard_setOf_support_subset_coeff_mem_Icc` (integer bounds `a d ≤ coeff d ≤ b d`, count `∏ d ∈ S, (b d + 1 - a d).toNat`).
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - multivariate counterpart of `Polynomial.ncard_boxPoly` for Siegel-lemma / pigeonhole arguments;
  - with the univariate analogue (support ⊆ `Finset.range (n+1)`), a short re-proof of `ncard_boxPoly` replacing its `toFn`/`ofFn` bijection;
  - grouped with `MvPolynomial.finite_setOf_support_subset_coeff_mem` (from `Roth.boxFamily_finite`), a complete finiteness + count API for support/coefficient-bounded polynomials.
Proposed mathlib location: `Mathlib/RingTheory/MvPolynomial/Basic.lean` (next to `restrictSupport`) or `Mathlib/Algebra/MvPolynomial/Basic.lean`.
Local refactor: once available, replace the body of `ncard_boxFamily` (Roth/MainLemma.lean:311) by the corollary proof in evidence and drop the private aux if `boxFamily_finite` is also re-derived; call site l.373 unaffected.
Next action: run `/generalise Roth.ncard_boxFamily` against the general form above, then open one mathlib PR "feat(RingTheory/MvPolynomial): finiteness and cardinality of polynomials with bounded support and coefficients" together with the finiteness lemma.

---

## Next step

Upstream `MvPolynomial.ncard_setOf_support_subset_coeff_mem` (+ `Icc` corollary), grouped with the finiteness lemma from `Roth.boxFamily_finite`; keep `Roth.ncard_boxFamily` local and re-prove it as a corollary.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.ncard_boxFamily/ncard_general.lean` (imports `Roth.MainLemma`; `lean_diagnostic_messages` clean on first check, no warnings): (1) `MvPolynomial.ncard_setOf_support_subset_coeff_mem` for `[CommSemiring R]`; (2) `MvPolynomial.ncard_setOf_support_subset_coeff_mem_Icc` over ℤ; (3) `Roth.ncard_boxFamily` re-derived from (2).
- Mathlib greps: `ncard_boxFamily` (none); `ncard_setOf_support`/`card_setOf_coeff`/`ncard.*coeff` (only MahlerMeasure.lean `ncard_boxPoly` l.57 and its use l.78–81).
- LeanSearch (1), Lean-Finder (1), Loogle (1, query error): see Phase 5. `lean_local_search` not used.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local reference: clean.tex l.1415.
- Project grep `grep -rn ncard_boxFamily Roth/`: l.43 (docstring), l.311 (decl), l.373 (only use).
