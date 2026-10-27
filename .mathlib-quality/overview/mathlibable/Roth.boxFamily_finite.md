---
decl: Roth.boxFamily_finite
file: Roth/MainLemma.lean
line: 301
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Re-aimed per Roth.boxFamily at the general statement that polynomials with support in a finite monomial set S and coefficients in a finite set U form a finite set (any CommSemiring R); this is absent from mathlib, which re-derives the univariate case inline in Polynomial.bUnion_roots_finite and via ncard in the Northcott proof; the general lemma compiles and boxFamily_finite is a 3-line corollary (evidence).
action: Upstream MvPolynomial.finite_setOf_support_subset_coeff_mem (and the Polynomial natDegree analogue) to Mathlib/RingTheory/MvPolynomial/Basic.lean next to restrictSupport, refactoring Polynomial.bUnion_roots_finite (Mathlib/Algebra/Polynomial/Roots.lean:622) to use it; locally keep boxFamily_finite (one call site Roth/MainLemma.lean:367) and re-prove it from the general lemma once available.
---

# Roth.boxFamily_finite

## Inventory entry

### `theorem Roth.boxFamily_finite`
- **Type**: `∀ {σ : Type*} (r : σ → ℕ) [Finite (Function.support r)] (B : ℕ), (boxFamily r B).Finite`
- **What**: The family `𝒲` of integer polynomials with `degreeOf j W ≤ r j` for all `j` and all coefficients in `[0, B]` is finite, provided only finitely many degree bounds `r j` are nonzero (σ may be infinite).
- **How**: Rewrites with the private `boxFamily_eq_image_finsupp_aux` (the family is the image under `AddMonoidAlgebra.ofCoeff` of `Finset.finsupp (Finset.Iic (Finsupp.ofSupportFinite r _)) (fun _ ↦ Finset.Icc 0 B)`), then closes with `(Finset.finite_toSet _).image _`.
- **Hypotheses**: `[Finite (Function.support r)]` (needed: with infinitely many positive `r j` the family is infinite).
- **Uses from project**: `Roth.boxFamily`, `Roth.boxFamily_eq_image_finsupp_aux` (private)
- **Used by**: Roth/MainLemma.lean:367 (`exists_ne_modByMonic_eq`, to build `Fintype (boxFamily r B)`). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 299–305, proof length 3 lines
- **Notes**: Source §6, proof of Lemma 9 (`.mathlib-quality/references/clean.tex` l.1405–1415, where `|𝒲| = (B_1+1)^r` implicitly asserts finiteness). Sibling `ncard_boxFamily` (l.312) gives the exact count.

## Junk check (Step 8)
- Used anywhere? Yes, once (l.367, `exists_ne_modByMonic_eq`).
- Wrapper of 1–2 mathlib calls? It is a 2-line wrapper over the private aux lemma plus `Finset.finite_toSet`/`Set.Finite.image`; the real content lives in the aux.
- Does mathlib have it? No multivariate statement; univariate analogues are only inline (`Polynomial.bUnion_roots_finite` proof, Roots.lean:627–634; `h_finite` inside the private `card_mahlerMeasure`, MahlerMeasure.lean:100–104).
- Too specific / inline? Could be inlined at l.367 (`Set.finite_of_ncard_ne_zero` from `ncard_boxFamily` would also do), but a named finiteness lemma is the natural companion to `ncard_boxFamily` and to the `Fintype` construction.
- Well-chosen? Yes as a local lemma; the general form (finite support set, finite coefficient set) is the mathlib-shaped statement.
- Conclusion: `KEEP` — action: keep; once the general lemma exists, re-prove it as a one-line corollary.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name has no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.boxFamily_finite` absent from mathlib (grep of `.lake/packages/mathlib/Mathlib` for `boxFamily_finite` empty). Not a glue lemma (proof uses a rewrite plus a finiteness argument, not `rfl`). Parent `Roth.boxFamily` is `NO-composable-from-mathlib`, and its report explicitly directs re-aiming the finiteness/count lemmas at a multivariate generalisation of `Polynomial.ncard_boxPoly`; so a full run is done, re-aimed at the general finiteness statement.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` elaborates with no diagnostics)
- decl `Roth.boxFamily_finite`: resolved at Roth/MainLemma.lean:301
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's main lemma (Lemma 9 of the source): construction of an auxiliary polynomial via a pigeonhole/box argument with explicit coefficient bounds.

### Statement (Phase 1)

`Roth.boxFamily_finite` is a theorem stating the following: let `σ` be any set of variables and `r ∈ ℕ^σ` with only finitely many nonzero entries, and `B ≥ 0`. Then there are only finitely many polynomials `W ∈ ℤ[x_j : j ∈ σ]` with `deg_{x_j} W ≤ r_j` for every `j` and every coefficient in `{0, …, B}`. Indeed `W` is determined by its coefficient vector on the finite box `{d : d ≤ r}` of monomials, each entry taking one of `B+1` values.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables, arbitrary.
- `r : σ → ℕ` — per-variable degree bounds.
- `B : ℕ` — coefficient bound.

Hypotheses (Lean side):
- `[Finite (Function.support r)]` — only finitely many variables may occur, so the monomial box is finite.

Conclusion (math): `𝒲(r, B)` is finite.

Conclusion (Lean): `(boxFamily r B).Finite`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a finiteness helper for one pigeonhole step; not a structure, not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a (kind is theorem, not def). Proof body 3 lines.

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | finitely many integer polynomials bounded degree in each variable bounded coefficients finite set multivariate Siegel lemma pigeonhole | yes | multivariate Siegel lemma via pigeonhole over "all integer polynomials of the given degree and bounded magnitude" (arXiv 1310.6482, Tao; MIT 18.S997 lec. 26) | finiteness of the counted family is used without being named |
|  2 | WebSearch (general form) | polynomials with coefficients in a finite set and support in a finite set of monomials form a finite set | partial | no source states it as a lemma; the fact is the elementary bound `|U|^|S|` (monomial-basis framing, Wikipedia "Monomial basis") | general form: support in finite `S`, coefficients in finite `U` |
|  3 | WebSearch (named-after / aliases) | Northcott property finiteness polynomials of bounded height and degree | yes | Northcott: finitely many algebraic numbers of bounded height and degree; proof goes through finiteness of integer polynomials of bounded degree and height (projecteuclid FACM 39, arXiv 2401.03730) | the polynomial finiteness is the classical first step of Northcott's theorem |
|  4 | ChatGPT MCP | n/a | n/a | — | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for `B_1+1` | yes | l.1405–1415: the set `𝒲` with `|𝒲| = (B_1+1)^r` | source of the statement (finiteness implicit in the count) |
|  6 | nLab | finite set of polynomials with bounded coefficients | no | — | elementary combinatorics; no nLab entry |
|  7 | nCatLab | n/a | n/a | — | not a categorical concept |
|  8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry statement |
|  9 | MathOverflow / Math.SE | counting / finiteness of integer polynomials of bounded height (via #1–#3 hits) | yes | product of interval lengths; regarded as exercise-level | no named result |
| 10 | recent arXiv | arXiv 2401.03730 (Widmer's Northcott criteria), 1310.6482 | yes | same finiteness step inside Northcott / Siegel arguments | no general named object |

### Literature summary (Phase 3)

Concept identified as: finiteness of the set of polynomials of bounded support and bounded height (the domain of the Dirichlet box principle in Siegel's lemma; first step of Northcott's theorem).
Sources agree on the standard form: yes — polynomials whose monomials lie in a fixed finite set and whose coefficients lie in a fixed finite set form a finite set (at most `|U|^|S|` elements).
Most general standard form: for any coefficient ring `R`, finite set `S` of monomials and finite `U ⊆ R`, `{p : ↑p.support ⊆ S ∧ ∀ d, p.coeff d ∈ U}` is finite.
Generality dimensions where the literature varies:
  - support: box `d ≤ r`, total degree ≤ n, arbitrary finite set — most general: arbitrary finite `S`;
  - coefficients: `[0,B]`, `[-H,H]`, any finite set — most general: any finite `U` (no order needed);
  - ring: ℤ in applications; the finiteness needs no structure beyond `Zero`.
Disagreement with the literature: none; the user's form is the box/`[0,B]`/ℤ specialisation.

### Generality analysis — `Roth.boxFamily_finite`

Literature-standard form (from Phase 3): `{p : MvPolynomial σ R | ↑p.support ⊆ S ∧ ∀ d, p.coeff d ∈ U}.Finite` for finite `S`, `U`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|------------------------|-------------------|--------------------------|---------------------|--------|
| 1 | coefficient ring | `ℤ` | any `CommSemiring R` | yes | evidence lemma compiles for `[CommSemiring R]`, no order |
| 2 | coefficient condition | `0 ≤ c ∧ c ≤ B` | `c ∈ U`, `U` finite | yes | evidence: only finiteness of `U` used |
| 3 | support condition | `∀ j, degreeOf j W ≤ r j` | `↑W.support ⊆ S`, `S` finite | yes | box is the instance `S = Finset.Iic r` (evidence corollary) |
| 4 | `[Finite (Function.support r)]` | finite support of `r` | `S.Finite` | no (same role) | needed: becomes finiteness of `S` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — verified: `MvPolynomial.finite_setOf_support_subset_coeff_mem` compiles (`lean_diagnostic_messages` clean) and `Roth.boxFamily_finite` follows from it in 3 lines (same file).
Number of weakening opportunities found: 3 (ring, coefficient set, support set)
Proposed restatement:

```lean
theorem MvPolynomial.finite_setOf_support_subset_coeff_mem {σ R : Type*} [CommSemiring R]
    {S : Set (σ →₀ ℕ)} (hS : S.Finite) {U : Set R} (hU : U.Finite) :
    {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d, p.coeff d ∈ U}.Finite
```

Cost of restatement: CHEAP (proof already compiled, 7 lines).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream |
|----|----------|----------|------------------------|--------------------|
|  1 | preambles → typeclasses | no | no structure preamble | — |
|  2 | sequences → filters | no | finite combinatorial statement | — |
|  3 | construction → universal property | no | a finiteness statement | — |
|  4 | set-with-predicate → bundled substructure | partly | support part as `p ∈ restrictSupport R S` | `mem_restrictSupport_iff` |
|  5 | field-specific → weaker typeclass | yes | ℤ → `CommSemiring R` | applies to ℕ, ℤ, finite rings, number rings |
|  6 | higher-categorical | no | — | — |
|  7 | concrete index → general | yes | box `d ≤ r`, `[0,B]` → finite `S`, finite `U` | `Finset.Iic`, `Set.finite_Icc`, `Set.Finite.pi` users |
|  8 | concrete-via-abstract | yes | after `rw [boxFamily_eq_image_finsupp_aux]` the proof never mentions `boxFamily`/`ℤ`/order: only finiteness of the monomial set and coefficient set is used | the abstract lemma; `boxFamily_finite` becomes a corollary |
|  9 | false-generalisation guard | no false generalisation | instantiating `S = Iic r`, `U = Icc 0 B` recovers a superset containing `boxFamily r B`, so the original follows by `Set.Finite.subset` | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.finite_setOf_support_subset_coeff_mem` above (optionally phrased with `p ∈ restrictSupport R S`), plus the `Polynomial` analogue `{f : R[X] | f.natDegree ≤ n ∧ ∀ i, f.coeff i ∈ U}.Finite` (compiled in evidence).
  - Cost: CHEAP
  - Mathlib downstream this enables: replaces the inline finiteness argument in `Polynomial.bUnion_roots_finite` (Mathlib/Algebra/Polynomial/Roots.lean:627–634) and the `ncard`-based `h_finite` in `card_mahlerMeasure` (Mathlib/NumberTheory/MahlerMeasure.lean:100–104); gives a finiteness companion to `Polynomial.ncard_boxPoly`.
  - Real mathematical improvement: one general finiteness lemma replaces two ad-hoc inline derivations in mathlib and the project's ℤ/box-specific one.

### Proof strategy — `Roth.boxFamily_finite`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|----------|----------|------------------------|------|
| 1 | topology ε-δ | no | — | — |
| 2 | elements vs. submodule inclusions | no | — | — |
| 3 | sequences vs. filters | no | — | — |
| 4 | universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `MvPolynomial.finite_setOf_support_subset_coeff_mem` (and Polynomial analogue) | CHEAP (file follow-up PR) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (image of `Finset.finsupp` under `ofCoeff`); modulo the missing general lemma it would be a one-liner.
  - Missing mathlib API: the general finiteness lemma above.
  - Would refactoring make the proof strictly shorter? yes (3 lines from the general lemma, no private aux needed for finiteness).

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.boxFamily_finite`

[A] Lean-Finder       "finitely many finitely supported functions with support in a finite set and values in finite sets" → `Finset.finsupp`, `Finset.dfinsupp`, `Finsupp.pi`, `Finsupp.fintype`, `DFinsupp.fintype` (building blocks only)
[B] Loogle            `Set.Finite, Finset.finsupp` → no hits
[C] LeanSearch        "set of polynomials with bounded degree and coefficients in a finite set is finite" → `Polynomial.span_le_degreeLE_of_finite`, `restrictDegree`/`restrictTotalDegree` `Module.Finite` instances, `Polynomial.card_eq_of_natDegree_le_of_coeff_le` (= `ncard_boxPoly`); no finiteness lemma of the target shape
[D] Grep mathlib src  `boxFamily_finite` (none); regex for `(theorem|lemma|instance)` names containing finite+finsupp / `finite_coeff` / `finite_setOf_coeff` → only unrelated (`Module.Finite.finsupp`, `Presentation.finite_coeffs`); `bUnion_roots_finite` (Roots.lean:622, inline derivation of the univariate case); `finite_mahlerMeasure_le`/`card_mahlerMeasure` (MahlerMeasure.lean, finiteness via `Set.finite_of_ncard_ne_zero`)
[E] Name pattern      `lean_local_search` n/a: ripgrep not installed on this machine (per earlier reports); replaced by grep [D]

Searched for both:
  - the user's current form (multivariate, box, `[0,B]`, ℤ) — not in mathlib;
  - the literature-standard form (finite `S`, finite `U`, any ring) — not in mathlib, multivariate or univariate; only inline re-derivations.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks `Finset.finsupp`, `Finset.mem_finsupp_iff`, `AddMonoidAlgebra.ofCoeff`, `Set.Finite.image`/`subset`.

### Normal-form check — `Roth.boxFamily_finite`

Equivalent formalisms: `(boxFamily r B).Finite`; `Finite (boxFamily r B)`; `Set.ncard ≠ 0` (via `ncard_boxFamily`); support phrased via `restrictSupport`.
Does mathlib have a canonical form? `Set.Finite` is the standard predicate for such statements (cf. `finite_mahlerMeasure_le`).
Our statement uses `Set.Finite`: OK. RHS convention: n/a (not an equation).

### Syntactic generality — `Roth.boxFamily_finite`

Alternative restatements attempted:
- general `support ⊆ S ∧ coeff ∈ U` form (compiled);
- `p ∈ restrictSupport R S ∧ …` form (equivalent via `mem_restrictSupport_iff`);
- Polynomial `natDegree ≤ n ∧ coeff ∈ U` form (compiled).
Chosen restatement: the `↑p.support ⊆ S ∧ ∀ d, p.coeff d ∈ U` form.
Justification: hypotheses are plain `Set.Finite` facts, callers supply `S` (e.g. `Finset.Iic r`) and `U` (e.g. `Set.finite_Icc`) directly and conclude via `Set.Finite.subset`.

### Superfluous-argument audit — `Roth.boxFamily_finite`

| # | Argument / typeclass | Essentially used? | Notes |
|---|----------------------|-------------------|-------|
| 1 | `σ : Type*` | yes | arbitrary, no finiteness |
| 2 | `r : σ → ℕ` | yes | defines the box |
| 3 | `[Finite (Function.support r)]` | yes | without it the family is infinite |
| 4 | `B : ℕ` | yes | coefficient bound |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (for mathlib: general `S`, `U`, `R` form)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (ship the general lemma; keep the box form as a project corollary)

### Call sites — `Roth.boxFamily_finite`

Internal use count: 0 outside the declaring file (1 use inside it)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern |
|------------------|---------------|
| Roth/MainLemma.lean:367 | `let : Fintype (boxFamily r B) := (boxFamily_finite r B).fintype` in `exists_ne_modByMonic_eq` |

Inline-derivation grep:
  - Mathlib/Algebra/Polynomial/Roots.lean:627–634 (`Polynomial.bUnion_roots_finite`): inline proof that `{f | f.natDegree ≤ d ∧ ∀ i, f.coeff i ∈ U}` is finite via `Set.Finite.pi` + injectivity of coefficients.
  - Mathlib/NumberTheory/MahlerMeasure.lean:100–104 (private `card_mahlerMeasure`): finiteness of a coefficient box obtained from `ncard ≠ 0`.

### Composition check (Phase 6)

Can `Roth.boxFamily_finite` be derived from mathlib in ≤3 chained calls?

Attempt 1: `((Finset.finsupp S U).finite_toSet.image ofCoeff).subset ?_` — the subset goal needs a `rintro`, `Finset.mem_finsupp_iff` rewrite and the `degreeOf` → support bridge (`monomial_le_degreeOf`); this is a short proof (≈6 lines), not a call chain.
  - Mathlib decls used: `Finset.finsupp`, `Finset.finite_toSet`, `Set.Finite.image`, `Set.Finite.subset`, `Finset.mem_finsupp_iff`, `AddMonoidAlgebra.ofCoeff`, `MvPolynomial.monomial_le_degreeOf`
  - Result: partial (works, but is a real proof)
Attempt 2: `Set.finite_of_ncard_ne_zero` from `ncard_boxFamily` — requires the project's own count lemma, not mathlib.
  - Result: fails as a mathlib-only composition.

Conclusion: NOT-COMPOSABLE (mathlib lacks the general lemma; both mathlib and the project re-derive it inline).

## Verdict: `Roth.boxFamily_finite`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the finiteness of polynomials with bounded support and bounded coefficients is the classical first step of Siegel's lemma (pigeonhole) and Northcott's theorem; most general form uses a finite monomial set and a finite coefficient set.
- Generality analysis (Phase 4): STRICTLY NARROWER; general lemma compiled, original derived as a corollary (evidence file).
- Mathlib search (Phase 5): not in mathlib in any form; only inline re-derivations (`bUnion_roots_finite`, `card_mahlerMeasure`).
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

The project lemma, after the rewrite with the private aux lemma, uses nothing about ℤ, the order, the bound `B` or the box shape beyond "finitely many monomials, finitely many coefficient values". The general lemma `MvPolynomial.finite_setOf_support_subset_coeff_mem` (any `CommSemiring R`, finite `S`, finite `U`) compiles with the same `Finset.finsupp`/`ofCoeff` argument, and `boxFamily_finite` follows in three lines by `Set.Finite.subset` with `S = Finset.Iic (ofSupportFinite r _)`, `U = Set.Icc 0 B`.

The gap is concrete: mathlib re-derives the univariate instance inline in `Polynomial.bUnion_roots_finite` (Roots.lean:627–634) and obtains a box-finiteness via `ncard ≠ 0` inside `card_mahlerMeasure` (MahlerMeasure.lean:100–104); `Polynomial.ncard_boxPoly` has no finiteness companion. This is the re-aim target named in the `Roth.boxFamily` report (multivariate generalisation of `boxPoly`/`ncard_boxPoly`): for finiteness the right general form needs no order at all. The project-specific `boxFamily_finite` itself should stay local.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (Q8 concrete-via-abstract fired).
Proposed restatement:
```lean
theorem MvPolynomial.finite_setOf_support_subset_coeff_mem {σ R : Type*} [CommSemiring R]
    {S : Set (σ →₀ ℕ)} (hS : S.Finite) {U : Set R} (hU : U.Finite) :
    {p : MvPolynomial σ R | (p.support : Set (σ →₀ ℕ)) ⊆ S ∧ ∀ d, p.coeff d ∈ U}.Finite := by
  classical
  refine ((hS.toFinset.finsupp fun _ ↦ hU.toFinset).finite_toSet.image
    AddMonoidAlgebra.ofCoeff).subset ?_
  rintro p ⟨hp, hc⟩
  refine ⟨p.coeff, ?_, rfl⟩
  rw [Finset.mem_coe, Finset.mem_finsupp_iff]
  exact ⟨fun d hd ↦ hS.mem_toFinset.2 (hp hd), fun d _ ↦ hU.mem_toFinset.2 (hc d)⟩
```
plus the `Polynomial` analogue `{f : R[X] | f.natDegree ≤ n ∧ ∀ i, f.coeff i ∈ U}.Finite` (compiled in evidence, `[Semiring R]`).
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - `Polynomial.bUnion_roots_finite`: replace its inline `Set.Finite.pi` argument by the Polynomial analogue;
  - `card_mahlerMeasure`/`finite_mahlerMeasure_le`: finiteness without going through `ncard ≠ 0`;
  - a finiteness companion for `Polynomial.boxPoly`/`ncard_boxPoly`, and the multivariate counterpart for Siegel-lemma style arguments.
Proposed mathlib location: `Mathlib/RingTheory/MvPolynomial/Basic.lean` (next to `restrictSupport`) for the multivariate lemma; `Mathlib/Algebra/Polynomial/Degree/...` or `Roots.lean` for the univariate one.
Local refactor: once available, replace the body of `boxFamily_finite` (Roth/MainLemma.lean:301) by the 3-line corollary; the single call site l.367 is unaffected.
Next action: run `/generalise Roth.boxFamily_finite` against the general form above, then open a mathlib PR "feat(RingTheory/MvPolynomial): finiteness of polynomials with bounded support and coefficients", grouped with the multivariate count lemma re-aimed from `Roth.ncard_boxFamily`.

---

## Next step

Upstream `MvPolynomial.finite_setOf_support_subset_coeff_mem` (and the `Polynomial` natDegree analogue, refactoring `Polynomial.bUnion_roots_finite`); keep `Roth.boxFamily_finite` local and re-prove it as a corollary.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.boxFamily_finite/finite_general.lean` (imports `Roth.MainLemma`; `lean_diagnostic_messages` clean, no warnings): (1) `MvPolynomial.finite_setOf_support_subset_coeff_mem` for `[CommSemiring R]`, finite `S`, finite `U`; (2) `Roth.boxFamily_finite` re-derived from (1) in 3 lines; (3) Polynomial analogue `{f : R[X] | f.natDegree ≤ n ∧ ∀ i, f.coeff i ∈ U}.Finite` for `[Semiring R]`. Two LSP iterations fixed a missing `classical` and the `ofFinsupp` coercion; final check clean.
- Mathlib greps: `boxFamily_finite` (none); finite/finsupp/coeff name regex (only unrelated hits); `bUnion_roots_finite` (Roots.lean:622–634); `MahlerMeasure.lean` l.55–104 (`boxPoly`, `ncard_boxPoly`, `card_mahlerMeasure`).
- LeanSearch (1), Lean-Finder (1), Loogle (1, no hits): see Phase 5. `lean_local_search` not used (ripgrep unavailable per earlier reports).
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local reference: clean.tex l.1405–1415.
- Project grep `grep -rn boxFamily_finite Roth/`: l.301 (decl), l.367 (only use).
