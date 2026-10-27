---
decl: Roth.boxFamily
file: Roth/MainLemma.lean
line: 275
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: boxFamily r B is MvPolynomial.restrictSupport ℤ {d with d j ≤ r j for all j} intersected with the coefficient box Icc 0 B (one-line ext proof in evidence; restrictDegree for constant r); mathlib already has the univariate analogue Polynomial.boxPoly with ncard_boxPoly in Mathlib/NumberTheory/MahlerMeasure.lean, so the def itself is a project-local name for a mathlib composition.
action: Keep boxFamily as a project-local abbreviation for the Lemma 9 family (used in Roth/MainLemma.lean:361-601), optionally restating its body via MvPolynomial.restrictSupport; do not upstream the def; re-aim any upstreaming of boxFamily_finite/ncard_boxFamily at a multivariate generalisation of Polynomial.boxPoly/ncard_boxPoly (support in a finite set S of monomials, coefficients in per-monomial intervals).
---

# Roth.boxFamily

## Inventory entry

### `def Roth.boxFamily`
- **Type**: `{σ : Type*} → (r : σ → ℕ) → (B : ℕ) → Set (MvPolynomial σ ℤ)`
- **What**: The set `𝒲` of integer polynomials `W` with `degreeOf j W ≤ r j` for every variable `j` and every coefficient in `[0, B]`.
- **How**: Set-builder `{W | (∀ j, degreeOf j W ≤ r j) ∧ ∀ d, 0 ≤ W.coeff d ∧ W.coeff d ≤ B}`.
- **Hypotheses**: none (no finiteness on `σ`; finiteness enters only in `boxFamily_finite`/`ncard_boxFamily` via `[Finite (Function.support r)]`).
- **Uses from project**: `[]` (only mathlib `MvPolynomial.degreeOf`, `MvPolynomial.coeff`)
- **Used by**: Roth/MainLemma.lean: private `boxFamily_eq_image_finsupp_aux` (l.281), `boxFamily_finite` (l.302), `ncard_boxFamily` (l.313), statements/proofs at l.361, 364, 367, 368, 373 (`pigeonhole_count`), l.389 (`exists_ne_modByMonic_eq`), l.552, l.601 (main Lemma 9 construction); module docstring l.35. No uses outside Roth/MainLemma.lean.
- **Visibility**: public
- **Lines**: 275–276, proof length 1 line (definition body)
- **Notes**: Source §6 proof of Lemma 9 (`.mathlib-quality/references/clean.tex` l.1405–1415, "`|𝒲| = (B_1+1)^r`"). The private aux lemma already rewrites the family as an image of `Finset.finsupp` over `Finset.Iic (Finsupp.ofSupportFinite r _)`.

## Junk check (Step 8)
- Used anywhere? Yes: 3 lemmas about it plus 4 statement-level uses in Lemma 9 machinery (all in Roth/MainLemma.lean).
- Wrapper of 1–2 mathlib calls? Essentially yes: it equals `{W | W ∈ MvPolynomial.restrictSupport ℤ {d | ∀ j, d j ≤ r j} ∧ ∀ d, W.coeff d ∈ Set.Icc 0 B}` (evidence), and for constant `r` the support part is `MvPolynomial.restrictDegree σ ℤ m`.
- Does mathlib have it? Not the multivariate set; the univariate analogue is `Polynomial.boxPoly n B₁ B₂` (Mathlib/NumberTheory/MahlerMeasure.lean:55) with `Polynomial.ncard_boxPoly` (l.57).
- Too specific / inline? Inlining the set-builder into the statements of `pigeonhole_count`, `exists_ne_modByMonic_eq` and the Lemma 9 statements would make them noisier; the name matches the paper's `𝒲`.
- Well-chosen definition? Reasonable as a local name; the `degreeOf` phrasing is fine, though `restrictSupport` phrasing would connect to mathlib's support API.
- Conclusion: `KEEP` — action: keep as a local abbreviation (optionally restate via `restrictSupport`); no deletion.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name has no `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.boxFamily` absent from mathlib (`grep -rn boxFamily .lake/packages/mathlib/Mathlib` empty). Not a glue lemma. Full workflow follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.MainLemma` elaborates with no diagnostics)
- decl `Roth.boxFamily`:     resolved at Roth/MainLemma.lean:275
- kind:                      def
- has sorry:                 no
- module docstring summary:  Roth's main lemma (Lemma 9 of the source): construction of an auxiliary polynomial via a pigeonhole/box argument with explicit coefficient bounds.

### Statement (Phase 1)

`Roth.boxFamily` is a definition of the following: for variables `σ`, a degree-bound vector `r ∈ ℕ^σ` and an integer `B ≥ 0`,
`𝒲(r, B) = { W ∈ ℤ[x_j : j ∈ σ] : deg_{x_j} W ≤ r_j for all j, and 0 ≤ c_d(W) ≤ B for every monomial d }`.
Equivalently, the polynomials supported on the box of monomials `{d : d ≤ r}` with coefficients in `{0, …, B}`; when only finitely many `r_j` are nonzero it has `(B+1)^{∏(r_j+1)}` elements.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables (arbitrary, possibly infinite).
- `r : σ → ℕ` — per-variable degree bounds.
- `B : ℕ` — coefficient upper bound.

Hypotheses (Lean side):
- none.

Conclusion (math): the finite family of "box" integer polynomials used in the Siegel/Dirichlet pigeonhole step.

Conclusion (Lean): n/a — definition (`Set (MvPolynomial σ ℤ)`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a project-local named set used for one counting step (Lemma 9); not a new structure, not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | no proof relies on blocking unfolding; proofs unfold it freely (`boxFamily_eq_image_finsupp_aux` uses `hW.1`, `hW.2`) |
| Avoid typeclass diamonds         | no       | it is a `Set`, no instances involved |
| Mark semantic intent / API name  | yes (project-local) | `pigeonhole_count` (l.361), `exists_ne_modByMonic_eq` (l.389), Lemma 9 statements (l.552, 601) name `𝒲` via it; but no mathlib consumer |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; no mathlib-level exemption)

### Literature search table

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form) | Siegel lemma box principle polynomials coefficients 0 ≤ bounded degree in each variable count (B+1)^N Roth theorem proof | yes | lattice points `0 ≤ x_i ≤ Z` number `(Z+1)^N`; auxiliary polynomial with `deg_{X_h} P ≤ r_h` (arXiv 2502.00731, uh.edu Roth notes, arXiv 0908.4024) | the family is the domain of the pigeonhole map; never named as a standalone concept |
|  2 | WebSearch (general form) | number of integer polynomials bounded height and degree finite set Northcott count (2H+1)^(n+1) | yes | polynomials of degree ≤ n and height ≤ H: `(2H+1)^{n+1}` (arXiv 1609.08720 etc.) | the general concept is "polynomials of bounded degree and bounded height", counted as a product of interval lengths |
|  3 | WebSearch (aliases) | Dirichlet box principle pigeonhole auxiliary polynomial multivariate multidegree coefficients bounded Roth lemma Thue Siegel | yes | Thue's "Schubfachprinzip" applied to integer coefficient vectors (Wikipedia Siegel's lemma; Croot notes) | confirms: a box of coefficient vectors, no special name |
|  4 | ChatGPT MCP | n/a | n/a | — | `ask_chatgpt_math` MCP not configured in this session |
|  5 | Local references | grep `.mathlib-quality/references/clean.tex` for "polynomials", "B_1+1" | yes | l.1405–1415: "Consider the set 𝒲 of all polynomials W = ∑ c(s) x^s … 0 ≤ c(s) ≤ B_1 … `|𝒲| = (B_1+1)^r`" | exact source of the def |
|  6 | nLab | box of integer points / polynomials with bounded coefficients | no | — | elementary combinatorial set; nLab has no entry |
|  7 | nCatLab | n/a | n/a | — | not a categorical concept |
|  8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry concept |
|  9 | MathOverflow / Math.SE | (covered via #1–#3 results) counting integer polynomials of bounded height | yes | product-of-intervals count | standard exercise-level fact |
| 10 | recent arXiv | arXiv 2502.00731 (Diophantine approximation and the subspace theorem), 1806.10737 (Roth over function fields) | yes | same pigeonhole on box of coefficients | no named general object |

### Literature summary (Phase 3)

Concept identified as: polynomials of bounded (multi)degree and bounded height / coefficients in a box — the domain of the Dirichlet box principle in Siegel's lemma.
Sources agree on the standard form: yes — "integer polynomials supported on a given finite set of monomials with coefficients in prescribed intervals", counted as a product of interval lengths.
Most general standard form: polynomials over ℤ (or any ring with locally finite order) supported in a finite set `S` of monomials with each coefficient in an interval `[a_d, b_d]`.
Generality dimensions where the literature varies:
  - support: box `d ≤ r`, total degree ≤ n, or arbitrary finite set — most general is an arbitrary finite set;
  - coefficient range: `[0, B]`, `[-H, H]`, per-coefficient `[B₁ i, B₂ i]` — most general is per-monomial intervals;
  - number of variables: 1 (Northcott counts) or many (Siegel/Roth).
Disagreement with the literature: none; the user's form is the box/`[0,B]` specialisation used in the paper.

### Generality analysis — `Roth.boxFamily`

Literature-standard form (from Phase 3): `{W | ↑W.support ⊆ S ∧ ∀ d, W.coeff d ∈ Icc (a d) (b d)}` for finite `S`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|------------------------|-------------------|--------------------------|---------------------|--------|
| 1 | coefficient ring | `ℤ` | any ordered ring with locally finite order | yes | evidence: the finiteness argument compiles for `[CommRing R] [PartialOrder R] [LocallyFiniteOrder R]` |
| 2 | support condition | `∀ j, degreeOf j W ≤ r j` (box) | `↑W.support ⊆ S`, `S` finite | yes | the box is `S = {d ∣ d ≤ r}`; evidence compiles finiteness for arbitrary finite `S` |
| 3 | coefficient range | `[0, B]`, `B : ℕ` | `[a, b]` (or per-monomial) | yes | evidence finiteness compiles for arbitrary `[a, b]` |
| 4 | `σ` | arbitrary | arbitrary | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (as a set); verified in evidence that the generalised family is finite by the same `Finset.finsupp` argument (`lean_diagnostic_messages` clean).
Number of weakening opportunities found: 3 (ring, support set, coefficient interval)
Proposed restatement (if STRICTLY NARROWER):

```lean
def MvPolynomial.boxPoly {R : Type*} [CommSemiring R] [Preorder R] (S : Set (σ →₀ ℕ))
    (a b : (σ →₀ ℕ) → R) : Set (MvPolynomial σ R) :=
  {W | W ∈ restrictSupport R S ∧ ∀ d, W.coeff d ∈ Set.Icc (a d) (b d)}
```

Cost of restatement: CHEAP for the def; MODERATE for re-proving `ncard` (needs `0 ∈ [a d, b d]` off `S`).
However, the generalised def would itself be a `restrictSupport ∩ coefficient-box` one-liner (see Phase 6): the generalisation does not create a non-composable object; the content worth upstreaming is the cardinality lemma, not the def.

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream |
|----|----------|----------|------------------------|--------------------|
|  1 | preambles → typeclasses | no | no structure preamble | — |
|  2 | sequences → filters | no | finite combinatorial set | — |
|  3 | construction → universal property | no | a set, not a construction | — |
|  4 | set-with-predicate → bundled substructure | partly | support part is the bundled `restrictSupport ℤ S` submodule; the coefficient box is not closed under addition, so the whole family cannot be bundled | `restrictSupport` membership API (`mem_restrictSupport_iff`, `restrictSupport_mono`) |
|  5 | field-specific → weaker typeclass | yes | ℤ → ordered ring with locally finite order | finiteness for other coefficient rings (e.g. ℕ, Gaussian-type orders) |
|  6 | higher-categorical | no | — | — |
|  7 | concrete index → general | yes | box `d ≤ r` → arbitrary finite support set `S` (e.g. `Finset.Iic r`) | interval API on `σ →₀ ℕ` (`Finset.Iic`, `Finsupp.card_Iic`) |
|  8 | concrete-via-abstract | no | the def has no proof body; `boxFamily_eq_image_finsupp_aux` uses only `S` finite and coefficient intervals finite (consistent with #5, #7) | — |
|  9 | false-generalisation guard | no false generalisation | the generalised set with `S = {d ≤ r}`, `R = ℤ`, `[0,B]` is literally the same set | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `{W | W ∈ MvPolynomial.restrictSupport ℤ (Finset.Iic r) ∧ ∀ d, W.coeff d ∈ Set.Icc 0 B}` (or the general `S`, `[a,b]` form above).
  - Cost: CHEAP
  - Mathlib downstream this enables: `MvPolynomial.mem_restrictSupport_iff`, `restrictSupport_mono`, `basisRestrictSupport`; `Finset.Iic`/`Finsupp.card_Iic` for the box (cf. Roth.box report).
  - Real mathematical improvement: connects the support condition to mathlib's existing support-restricted submodule instead of re-deriving the `degreeOf` ↔ support bridge (`monomial_le_degreeOf`/`degreeOf_le_iff`) in each proof.

### Proof strategy — `Roth.boxFamily`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|----------|----------|------------------------|------|
| 1 | topology ε-δ | no | — | — |
| 2 | elements vs. submodule inclusions | partly | support condition as `restrictSupport` membership | CHEAP |
| 3 | sequences vs. filters | no | — | — |
| 4 | universal property | no | — | — |
| 5 | missing mathlib helpers | yes | a multivariate `ncard`/finiteness lemma for "polynomials with support in finite `S` and coefficients in intervals" generalising `Polynomial.ncard_boxPoly` | follow-up (belongs to `ncard_boxFamily`'s assessment) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (definition body; no proof). Optional local refactor: phrase the support condition via `restrictSupport`. Missing mathlib API: multivariate analogue of `Polynomial.ncard_boxPoly`.

### Diamond / defeq risk — `Roth.boxFamily`

| # | Risk | Verdict | Evidence / rationale |
|---|------|---------|----------------------|
| 1 | Typeclass diamond | none | a plain `Set`; no instances defined or required |
| 2 | Reducibility leak | none | default (semireducible) def; proofs unfold via membership projections `hW.1`, `hW.2` |
| 3 | Non-canonical unfolding | low | `Set.mem_setOf` simp unfolds it to the conjunction; harmless, and evidence `ext; simp only [Roth.boxFamily, ...]` behaves as expected |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism | none | `σ : Type*` polymorphic; no annotations forced |
| 6 | Coercion ambiguity | none | `Set` coerces to type via standard `CoeSort` only (used as `boxFamily r B` subtype at l.367 without issue) |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: none

### Mathlib search-status: `Roth.boxFamily`

[A] Lean-Finder       "set of integer polynomials with degree at most n and coefficients between bounds, its cardinality" → hit `Polynomial.card_eq_of_natDegree_le_of_coeff_le` (index name; locally `Polynomial.ncard_boxPoly`), `Polynomial.card_mahlerMeasure_le_prod`
[B] Loogle            `Set.ncard, MvPolynomial.coeff` → query error (unknown identifier in loogle's index); n/a for this pattern
[C] LeanSearch        "finite set of multivariate polynomials with bounded degree in each variable and bounded integer coefficients" → `MvPolynomial.restrictDegree` finiteness instance (`Module.Finite`), `Polynomial.span_le_degreeLE_of_finite`; no multivariate box family
[D] Grep mathlib src  `boxFamily` (none), `boxPoly` (Mathlib/NumberTheory/MahlerMeasure.lean:55, 57), `restrictSupport`/`restrictDegree` (Mathlib/RingTheory/MvPolynomial/Basic.lean:93, 171), `bUnion_roots_finite` (Mathlib/Algebra/Polynomial/Roots.lean:622, inline finite-coefficient family)
[E] Name pattern      `lean_local_search` n/a: ripgrep not installed on this machine; replaced by grep [D]

Searched for both:
  - the user's current form (multivariate, box support, `[0,B]`) — not in mathlib;
  - the literature-standard form (finite support set, coefficient intervals) — univariate case present as `Polynomial.boxPoly` (degree ≤ n, real per-coefficient bounds) with `ncard_boxPoly`; multivariate absent.

Concluded: found building blocks (`MvPolynomial.restrictSupport`, `MvPolynomial.restrictDegree`, `Set.Icc`, `MvPolynomial.coeff`) composing to the form; univariate analogue `Polynomial.boxPoly` exists.

### Normal-form check — `Roth.boxFamily`

Equivalent formalisms: (a) `degreeOf`-bounded; (b) `↑W.support ⊆ {d ∣ d ≤ r}` / `restrictSupport`; (c) image of `Finset.finsupp` under `ofCoeff` (the private aux).
Does mathlib have a canonical form? Yes for the support part: `restrictSupport R S` (with `restrictDegree` for constant bounds).
Our statement uses (a), not the canonical (b); the evidence proves `(a) = (b) ∩ box` in one `ext` line, so a local restatement is cheap.
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.boxFamily`

Alternative restatements attempted:
- `{W | W ∈ restrictSupport ℤ {d | ∀ j, d j ≤ r j} ∧ ∀ d, W.coeff d ∈ Set.Icc 0 B}` (compiled)
- `{W | W ∈ restrictDegree σ ℤ m ∧ …}` for constant `r` (compiled)
- image of `Finset.finsupp (Iic r) (fun _ ↦ Icc 0 B)` under `AddMonoidAlgebra.ofCoeff` (project's private aux)

Chosen restatement: the current `degreeOf` form is easiest for the project's call sites (they produce `degreeOf` bounds, e.g. l.601); `restrictSupport` form is better for mathlib interop.
Justification: call sites in Lemma 9 reason per variable degree.

### Superfluous-argument audit — `Roth.boxFamily`

| # | Argument | Essentially used? | Notes |
|---|----------|-------------------|-------|
| 1 | `σ : Type*` | yes | no finiteness assumed (already minimal) |
| 2 | `r : σ → ℕ` | yes | support bound |
| 3 | `B : ℕ` | yes | could be `ℤ`-interval, but `ℕ` matches the source's `B_1 ≥ 0` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (optional) — support condition via `restrictSupport ℤ {d ∣ d ≤ r}`
Syntactic generality: OK for project use
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project-locally); for any mathlib version, RESTATE-BEFORE-SHIP in the general `S`, `[a,b]` form.

### Call sites — `Roth.boxFamily`

Internal use count: 8 uses in the declaring file (l.281, 302, 313, 361, 364, 367–373, 389, 552, 601); 0 outside the declaring file
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern |
|------------------|---------------|
| Roth/MainLemma.lean:281 | private `boxFamily_eq_image_finsupp_aux`: `boxFamily r B = AddMonoidAlgebra.ofCoeff '' …` |
| Roth/MainLemma.lean:302 | `boxFamily_finite : (boxFamily r B).Finite` |
| Roth/MainLemma.lean:313 | `ncard_boxFamily : (boxFamily r B).ncard = (B + 1) ^ ∏ᶠ j, (r j + 1)` |
| Roth/MainLemma.lean:361–373 | `pigeonhole_count`: hypothesis `∀ W ∈ boxFamily r B, …`, conclusion `∃ W' ∈ boxFamily r B, …`, `Fintype (boxFamily r B)` |
| Roth/MainLemma.lean:389 | `exists_ne_modByMonic_eq`: `(h' : W' ∈ boxFamily r B) (h'' : W'' ∈ boxFamily r B)` |
| Roth/MainLemma.lean:552 | Lemma 9 helper hypothesis `hC : ∀ W ∈ boxFamily r B, …` |
| Roth/MainLemma.lean:601 | Lemma 9 main proof `have hC : ∀ W ∈ boxFamily r B, …` |

Inline-derivation grep: (none) — no other site re-derives the family; mathlib's `Polynomial.bUnion_roots_finite` (Roots.lean:622) and `Polynomial.boxPoly` are the analogous univariate inline constructions.

### Composition check (Phase 6)

Can `Roth.boxFamily` be derived from mathlib in ≤3 chained calls?

Attempt 1: `{W | W ∈ MvPolynomial.restrictSupport ℤ {d | ∀ j, d j ≤ r j} ∧ ∀ d, W.coeff d ∈ Set.Icc 0 B}`
  - Mathlib decls used: `MvPolynomial.restrictSupport`, `Set.Icc`, `MvPolynomial.coeff` (equality proved via `mem_restrictSupport_iff`, `monomial_le_degreeOf`, `degreeOf_le_iff`)
  - Result: succeeds (evidence file, clean)
Attempt 2 (constant bound): `restrictDegree σ ℤ m` in place of `restrictSupport` — succeeds (evidence).

Conclusion: COMPOSABLE

## Verdict: `Roth.boxFamily`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the family is the unnamed "box of coefficient vectors" in Siegel/Dirichlet pigeonhole arguments (source clean.tex l.1405–1415); the standard general concept is polynomials with support in a finite monomial set and coefficients in intervals.
- Generality analysis (Phase 4): STRICTLY NARROWER as a set (ring, support, interval weakenings verified for finiteness), but the general form is itself a `restrictSupport ∩ coefficient box` composition.
- Mathlib search (Phase 5): building blocks `MvPolynomial.restrictSupport`/`restrictDegree`; univariate analogue `Polynomial.boxPoly` + `Polynomial.ncard_boxPoly`.
- Composition check (Phase 6): COMPOSABLE (one-line set-builder over mathlib primitives, equality compiled).

**Rationale:**

`Roth.boxFamily r B` is a one-line set-builder; the evidence proves it equals `{W | W ∈ MvPolynomial.restrictSupport ℤ {d | ∀ j, d j ≤ r j} ∧ ∀ d, W.coeff d ∈ Set.Icc 0 B}`, and for a constant bound the support part is `MvPolynomial.restrictDegree σ ℤ m`. There is nothing in the definition that mathlib could not express directly with its primitives, and even the most general literature form (finite support set `S`, coefficient intervals) remains such a composition. Mathlib's own precedent confirms this: the univariate analogue `Polynomial.boxPoly` is a section-local helper in the Northcott proof, not general API. The def is not worth upstreaming.

The only mathlib-worthy content is the counting statement (`ncard_boxFamily`/`boxFamily_finite`): a multivariate generalisation of `Polynomial.ncard_boxPoly` (support in a finite `S`, per-monomial bounds, count `∏_{d∈S} (⌊b_d⌋ - ⌈a_d⌉ + 1)`) is absent. That belongs to the assessment of `Roth.ncard_boxFamily` and should be re-aimed at that general form (and at `Polynomial.boxPoly`, which it would subsume via `Polynomial` ≃ one-variable `MvPolynomial`), not attached to this def.

WHY not: the def is a project-local name for `restrictSupport ∩ coefficient box`; mathlib has the building blocks and a univariate counterpart already.
Belongs-elsewhere check: keep in Roth/MainLemma.lean as the name for the paper's `𝒲`; its readability benefit in `pigeonhole_count`, `exists_ne_modByMonic_eq` and Lemma 9 statements justifies the local name.
Mathlib building blocks:      `MvPolynomial.restrictSupport` (Mathlib/RingTheory/MvPolynomial/Basic.lean:93), `MvPolynomial.restrictDegree` (l.171), `MvPolynomial.mem_restrictSupport_iff` (l.107), `MvPolynomial.monomial_le_degreeOf`, `MvPolynomial.degreeOf_le_iff`; analogue `Polynomial.boxPoly`/`Polynomial.ncard_boxPoly` (Mathlib/NumberTheory/MahlerMeasure.lean:55, 57)
Composition sketch (≤3 lines):
```lean
example (r : σ → ℕ) (B : ℕ) : Roth.boxFamily r B =
    {W | W ∈ restrictSupport ℤ {d : σ →₀ ℕ | ∀ j, d j ≤ r j} ∧ ∀ d, W.coeff d ∈ Set.Icc (0 : ℤ) B} := by
  ext W; simp only [Roth.boxFamily, Set.mem_ofPred_eq, mem_restrictSupport_iff, Set.mem_Icc]
  exact and_congr_left fun _ ↦ ⟨fun h d hd j ↦ (monomial_le_degreeOf j hd).trans (h j),
    fun h j ↦ degreeOf_le_iff.2 fun d hd ↦ h hd j⟩
```
Call sites in our project (from Phase 6.0):  8 uses, all in Roth/MainLemma.lean (l.281, 302, 313, 361–373, 389, 552, 601)
Refactor plan: no inlining recommended — inlining the set-builder into those 8 statements would hurt readability. Optionally change the body of `boxFamily` to the `restrictSupport` form above (and, together with the `Roth.box` refactor, use `Finset.Iic` for the support set), then simplify `boxFamily_eq_image_finsupp_aux` (l.281) since the support half becomes `mem_restrictSupport_iff`.
Next action: keep `Roth.boxFamily` project-local (no mathlib PR for the def); re-aim the `ncard_boxFamily`/`boxFamily_finite` assessments at a multivariate generalisation of `Polynomial.ncard_boxPoly`.

---

## Next step

Keep `Roth.boxFamily` as a local abbreviation (optionally restated via `MvPolynomial.restrictSupport`); do not upstream the def; any upstreaming effort goes to a multivariate `ncard` lemma generalising `Polynomial.ncard_boxPoly`, assessed under `Roth.ncard_boxFamily`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.boxFamily/boxFamily_compose.lean` (imports `Roth.MainLemma`, `Mathlib.RingTheory.MvPolynomial.Basic`; `lean_diagnostic_messages` clean, no warnings after replacing deprecated `Set.mem_setOf_eq` by `Set.mem_ofPred_eq`): (1) `boxFamily r B = restrictSupport ℤ {d ∣ ∀ j, d j ≤ r j} ∩ coefficient box`; (2) constant-bound case via `restrictDegree`; (3) generalised family (any `[CommRing R] [PartialOrder R] [LocallyFiniteOrder R]`, finite support set `S`, interval `[a,b]`) is finite.
- Mathlib greps: `boxFamily` (none); `boxPoly` (Mathlib/NumberTheory/MahlerMeasure.lean:55, 57, 81); `restrictSupport`/`restrictDegree` (Mathlib/RingTheory/MvPolynomial/Basic.lean:93, 166, 171, 181); `bUnion_roots_finite` (Mathlib/Algebra/Polynomial/Roots.lean:622).
- Lean-Finder (1 query): `Polynomial.card_eq_of_natDegree_le_of_coeff_le` (= local `ncard_boxPoly`), `card_mahlerMeasure_le_prod`. LeanSearch (1): `restrictDegree` finiteness instance, no multivariate box. Loogle (1): query error. `lean_local_search`: unavailable (ripgrep not installed).
- WebSearch: 3 queries (recorded in the literature table). ChatGPT MCP: n/a (not configured). Local reference: clean.tex l.1405–1415.
- Project grep `grep -rn boxFamily Roth/` for the call-sites table.
