---
decl: Roth.Θ
file: Roth/Theta.lean
line: 68
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Θ is Ridout/Cassels' Θ_m(B; q; r), the sSup of the project's indexSet (itself a Set.image of Roth.index over RSet B r and h coprime to q); it is one mathlib sSup over that image (compiled), a Roth-proof-specific quantity with nothing general to upstream.
action: Do not upstream; keep Roth.Θ in Roth/Theta.lean as the paper's Θ_m (consumers Θ_unique_le, Θ_option_le, Θ_lt, lem6Φ in Theta.lean and theta_lt_eta_of_sq_log_bound_aux, exists_auxiliary_polynomial_with_index_gap_aux, main_lemma in MainLemma.lean); optionally document the junk value Θ = 0 for B < 1 in the docstring; no call-site changes.
---

# Roth.Θ

## Inventory entry

### `def Roth.Θ`
- **Type**: `{σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : ℝ` (noncomputable)
- **What**: `Θ_m(B; q_1, …, q_m; r_1, …, r_m)`, the supremum of the indices `ind(R; (h_j/q_j)_j; r)` over nonzero integer polynomials `R` with `deg_{X_j} R ≤ r_j` and coefficients bounded by `B`, and over `h : σ → ℤ` with each `h_j` coprime to `q_j`.
- **How**: `sSup (indexSet B q r)` in the conditionally complete lattice `ℝ`. The `csSup` side conditions come from the companion lemmas `indexSet_nonempty` (needs `1 ≤ B`) and `indexSet_bddAbove` (bound `Fintype.card σ` via `index_le_card`).
- **Hypotheses**: none. Only `[Fintype σ]` is used; the section `[DecidableEq σ]` is not included (evidence (1)).
- **Uses from project**: `Roth.indexSet` (and through it `Roth.RSet`, `Roth.index`)
- **Used by**: Roth/Theta.lean: `index_le_Θ` (101), `Θ_nonneg` (107), `Θ_le_card` (114), `Θ_le_of_forall_index_le` (126), `Θ_mono` (135), `Θ_equiv` (160), private `index_unique_le_log_div` (253–258), `Θ_unique_le` (256–257, Lemma 5), `lem6M` (273), `lem6Φ` (276), private `index_separated_mul_le_aux` (443–450), `index_le_lem6` (583–591), `Θ_option_le` (593–599, Lemma 6), `lem7_Φ_bound` (707), private `theta_scaled_unique_le_aux` (744–759), private `theta_prefix_lt_aux` (787–790), the `Θ_lt` base case at 820–822, private `theta_phi_lt_aux` (851–855), private `theta_lt_succ_aux` (901–920), private `theta_lt_of_large_delta_aux` (934–959), `Θ_lt` (962–966, Lemma 7). Roth/MainLemma.lean: private `theta_lt_eta_of_sq_log_bound_aux` (676, 687), private `exists_auxiliary_polynomial_with_index_gap_aux` (699), `main_lemma` (750, 760, including `index_le_Θ hW hh`).
- **Visibility**: public
- **Lines**: 68, proof length 0 lines (one-line def body)
- **Notes**: Source: clean.tex §5 l.655–670. The paper assumes `q_j ≥ 1`, `r_j ≥ 1`, `B ≥ 1`; the Lean def takes none of these. For `B < 1` the defining family is empty, so `Θ B q r = sSup ∅ = 0` (junk value, compiled as evidence (3)); all consumers that need `Θ` as a true supremum assume `1 ≤ B`.

## Junk check (Step 8)
- Used anywhere? Yes, heavily: it is the central quantity of Lemmas 5, 6, 7 (`Θ_unique_le`, `Θ_option_le`, `Θ_lt`) and enters `main_lemma` in MainLemma.lean.
- Wrapper of 1–2 mathlib calls? Yes in form: `sSup` of the project set `indexSet`. Inlining it would replace a named paper quantity by `sSup (indexSet …)` at about 40 lines; no gain.
- Does mathlib have it? No. It is built from the project's `index` and `RSet`; Lean-Finder/LeanSearch find nothing similar (only unrelated Chevalley bounds and `Polynomial.finite_mahlerMeasure_le`).
- Too specific (inline?)? No; it is the paper's named notation and its API (`index_le_Θ`, `Θ_le_of_forall_index_le`, `Θ_mono`, `Θ_equiv`, `Θ_nonneg`, `Θ_le_card`) is used throughout.
- Well-chosen definition? Yes. `sSup` on `ℝ` with explicit nonempty/bddAbove lemmas is the standard mathlib pattern; the junk value `0` for `B < 1` is harmless (the paper never uses `B < 1`).

Conclusion: KEEP. No action needed (optionally mention the `B < 1` junk value in the docstring).

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring is not internal/auxiliary; Step 8 said KEEP; mathlib has no `namespace Roth` and no `def Θ` (grep of `.lake/packages/mathlib/Mathlib/`). Not a glue lemma (it is a def, the parent of the `Θ_*` lemmas). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` has no diagnostics)
- decl `Roth.Θ`:             resolved at Roth/Theta.lean:68
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5, 6, 7 bounding it.

### Statement (Phase 1)

`Roth.Θ` is a definition. For a finite variable set `σ`, a real `B` and `q, r : σ → ℕ`,

  `Θ(B; q; r) = sup { ind(R; (h_j/q_j)_j; r) : R ∈ ℛ(B; r), h ∈ ℤ^σ, gcd(h_j, q_j) = 1 }`,

the supremum (in `ℝ`, conditionally complete) of the Roth index of bounded-height integer polynomials at rational points with exact denominators `q_j`. For `1 ≤ B` the set is nonempty and bounded by `|σ|`, so `0 ≤ Θ ≤ |σ|`; for `B < 1` it is empty and `Θ = 0` by the `Real.sSup_empty` convention.

Variables / typeclasses involved (Lean side):
- `σ : Type*`, `[Fintype σ]`: the variables (needed by `index`).
- `B : ℝ`: coefficient bound.
- `q : σ → ℕ`: denominators.
- `r : σ → ℕ`: degree bounds and index weights.

Hypotheses (Lean side):
- none.

Conclusion (math): a real number.

Conclusion (Lean): n/a — definition (`noncomputable def Θ (B : ℝ) (q r : σ → ℕ) : ℝ := sSup (indexSet B q r)`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is a main definition of Theta.lean and the subject of Lemmas 5–7, but it introduces no new mathematical structure; it is the supremum of a project-specific family of reals, a proof-internal quantity of Roth/Ridout's argument.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | consumers go through `index_le_Θ` / `Θ_le_of_forall_index_le` / `csSup` lemmas; `Θ_equiv` unfolds it by `simp only [Θ]`-style rewriting; nothing relies on sealing |
| Avoid typeclass diamonds         | no       | no instances |
| Mark semantic intent / API name  | yes      | it is the paper's named quantity `Θ_m`, appearing in the statements of `Θ_unique_le`, `Θ_option_le`, `Θ_lt`, `lem6Φ` and `main_lemma` |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; the exemption does not argue for mathlib)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof Theta_m(B; q_1,...,q_m; r_1,...,r_m) supremum of index Ridout lemma | yes | Yamada (arXiv math/0307203 §2): `Θ_m(B; h/q; r)` is the supremum of the index over `ℛ_m(B; r)` at the rational point; Ridout's lemma bounds it by about `10^m δ^{(1/2)^m}` | same object as the Lean def (Lean also takes sup over the numerators `h`); v3 notes an unrelated gap in the mixed p-adic case |
| 2 | WebSearch (general form) | supremum of index of polynomials with bounded height at rational points Roth's lemma induction on number of variables | yes | Evertse (arXiv 2502.00731, Lemma 3.9): Roth's lemma bounds the index of a single polynomial pointwise (index ≤ 2mη), proved by induction on m | the general literature works pointwise; the supremum is a Ridout/Cassels bookkeeping device |
| 3 | WebSearch (named-after / aliases) | Cassels Introduction to Diophantine Approximation Theta_m index lemma Roth index supremum Mahler | partial | Cassels (1957, Ch. VI) is the classical source of the Roth-chapter index; Pottmeyer's lecture notes follow it | no alternative name for `Θ_m`; the notation traces to Cassels/Ridout |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §5 l.655–702 | yes | "the supremum of the numbers ind(R; h_1/q_1, …; r) over all R ∈ ℛ_m(B; r) and integers h_i with gcd(h_i, q_i)=1"; `0 ≤ Θ_m ≤ m`, monotone in `B` | matches the Lean def exactly; the Lean note (l.700–702) asks for exactly the nonempty/bddAbove/monotonicity API the file provides |
| 6 | nLab | index of a polynomial / Roth's lemma | no | — | nLab has no Diophantine-approximation entry for this |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no index-of-polynomial notion there |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | Roth's-lemma discussions use the index pointwise; no `Θ_m` threads surfaced |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | arXiv 2502.00731 (2025) | pointwise Roth's lemma; no supremum object |

### Literature summary (Phase 3)

Concept identified as: Ridout's / Cassels' `Θ_m(B; q; r)` in the proof of Roth's (Ridout's) theorem.
Sources agree on the standard form: yes. The supremum of the index over `ℛ_m(B; r)` and rational points of exact denominators `q_j` (clean.tex; Yamada fixes the point `h/q`, the project also sups over `h`, as clean.tex does).
Most general standard form: `sup { ind(P; α; r) : P ∈ 𝒫, α ∈ A }` for an admissible polynomial family and point set; modern treatments (Bombieri–Gubler, Evertse) avoid the supremum and state Roth's lemma pointwise.
Generality dimensions where the literature varies:
  - points: fixed `h/q` (Yamada) vs all `h` coprime to `q` (clean.tex, Lean) vs algebraic points of bounded height.
  - polynomial class: naive height ≤ B vs projective/Weil height.
Disagreement with the literature: none on content. Lean drops `q_j, r_j, B ≥ 1` and returns the junk value `0` for `B < 1`.

### Generality analysis — `Roth.Θ`

Literature-standard form (from Phase 3): `sup { ind(P; α; r) : P ∈ 𝒫, α ∈ A }`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | required | finitely many variables | NO | required by `index` (finite weighted sum) and for `Θ ≤ |σ|` |
| 2 | `[DecidableEq σ]` | not taken | not needed | already absent | evidence (1) |
| 3 | `B, q, r` side conditions | none | paper: `B ≥ 1`, `q_j, r_j ≥ 1` | already weaker than the paper | junk value for `B < 1` (evidence (3)); lemmas add `1 ≤ B`, `1 < q` as needed |
| 4 | point set / polynomial family | fixed via `indexSet` | any family | yes, but changes the object | as for `indexSet`: integrality, exact denominators and the height bound are used in Lemmas 5–7 |
| 5 | `ℝ`-valued `sSup` | conditionally complete `ℝ` | real supremum | n/a | could be `EReal`/`ℝ≥0∞`-valued `⨆`, but `Θ` is always in `[0, |σ|]` and the bounds are real arithmetic |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for what the project needs). No hypotheses, no unused instances (evidence (1)). Rows 4–5 are reformulations or false generalisations, not weakenings.
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | a supremum, no limits |
| 3 | construction vs universal property? | no | — | it is already defined by a universal property (least upper bound) via `sSup` |
| 4 | bundled substructure? | partial | `sSup (index-map '' (RSet B r ×ˢ {h coprime}))` (evidence (2)) or `⨆ p : admissible, index …` | `ciSup` lemmas; would not shorten the `rintro`-style proofs in Theta.lean |
| 5 | field-specific to semiring? | no | — | real-valued by design |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | arbitrary finite `σ` already; `Θ_equiv` transports along `σ ≃ τ` |
| 8 | concrete-via-abstract? | no | — | no proof body |
| 9 | false-generalisation guard | yes (row 4 of 4a) | widening the family changes `Θ` and breaks Lemma 5's Gauss-lemma bound; switching to `EReal` changes the arithmetic API used by Lemmas 6–7 | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only rephrasings (`sSup` of a `Set.image`, an indexed `iSup`, or an extended-real `⨆`) are the same number and would not shorten any consumer.

### Proof strategy — `Roth.Θ`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | `sSup` is already the universal-property form | — |
| 5 | missing mathlib helpers | no | the generic `csSup` API (`le_csSup`, `csSup_le`, `csSup_le_csSup`, `Real.sSup_nonneg`, `Real.sSup_le`, `Real.sSup_empty`) covers everything | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a definition with no proof; named `sSup` plus `Nonempty`/`BddAbove` lemmas is the standard pattern).

### Diamond / defeq risk — `Roth.Θ`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; `sSup` on `ℝ` comes from the unique `ConditionallyCompleteLinearOrder ℝ` instance |
| 2 | Reducibility leak | none | plain semireducible noncomputable def; consumers rewrite with the API lemmas |
| 3 | Non-canonical unfolding | low | junk value: `Θ B q r = 0` for `B < 1` (evidence (3)), since the family is empty and `Real.sSup_empty`; harmless because every bound on `Θ` used downstream assumes `1 ≤ B` (or applies at `B = q₁^{δ r₁} ≥ 1`), but undocumented in the docstring |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`; `Θ_equiv` relates `σ`, `τ` in independent universes |
| 6 | Coercion ambiguity | none | no coercions defined; the Greek identifier `Θ` is fine in a namespace but would not meet mathlib naming conventions |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none HIGH (row 3 low: `B < 1` junk value)
Recommended mitigations: n/a (optionally state the junk value in the docstring)

### Mathlib search-status: `Roth.Θ`

[A] Lean-Finder       "supremum of the order of vanishing of integer polynomials with bounded coefficients at rational points"   hits: `ChevalleyThm.MvPolynomialC.numBound/degBound`, `one_le_pow_mul_abs_eval_div`, `Polynomial.finite_mahlerMeasure_le` (none is this object)
[B] Loogle            `Real.sSup_empty` (found: `sSup ∅ = 0`, used in evidence (3)); `Roth.Θ` unknown to Loogle (expected: project decl)
[C] LeanSearch        "supremum of a set of real numbers that is nonempty and bounded above, le_csSup"   hits: `le_csSup`, `Real.isLUB_sSup`, `le_csSup_of_le`, `csSup_le` (building blocks)
[D] Grep mathlib src  `^namespace Roth` (none), `def Θ` (none); no index-of-polynomial notion (closest, `MvPowerSeries.weightedOrder`, is analysed in the `Roth.index` report)
[E] Name pattern      `Set.image`, `Set.mem_image`, `Set.mem_prod`, `Prod.exists`, `Real.sSup_empty` (all used in compiled evidence)

Searched for both the user's form (sup of indices over `RSet` and exact-denominator points) and the literature-standard form (sup of a weighted order of vanishing over an admissible family).

Concluded: found building blocks (`sSup` on `ℝ`, `Set.image`, `×ˢ`, `IsCoprime`, `MvPolynomial.map`). Nothing in mathlib matches `Θ`.

### Normal-form check — `Roth.Θ`

Equivalent formalisms: (a) `sSup (indexSet B q r)` (current); (b) `sSup` of a `Set.image` over `RSet B r ×ˢ {h | …}` (evidence (2)); (c) `⨆ p : {p // p.1 ∈ RSet B r ∧ …}, index …`.
Does mathlib already have a canonical form for this idea? No; project-specific quantity.
Is our statement stated against the canonical form? n/a. Form (a) keeps the carrier set named so `indexSet_nonempty`/`indexSet_bddAbove` feed `csSup` lemmas directly.
RHS convention respected? yes (evidence (2) has the composed form on the RHS).

### Syntactic generality — `Roth.Θ`

Alternative restatements attempted:
- `sSup` of a `Set.image` (evidence (2))
- indexed `⨆` over the admissible subtype
Chosen restatement: current (a)
Justification: `index_le_Θ` and `Θ_le_of_forall_index_le` are stated with unbundled `R, hR, h, hh`, which is the easiest shape to supply at the ~20 consumers; the `iSup` form would force subtype packaging.

### Superfluous-argument audit — `Roth.Θ`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `B` | yes | coefficient bound |
| 2 | `q` | yes | denominators |
| 3 | `r` | yes | degree bounds and weights |
| 4 | `[Fintype σ]` | yes | required by `index` |
| 5 | `[DecidableEq σ]` | not taken | evidence (1) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project def)

### Call sites — `Roth.Θ`

Internal use count: 5 lines outside the declaring file (in 3 declarations of Roth/MainLemma.lean); about 40 lines inside Roth/Theta.lean
External-to-file callers: 1 distinct file (Roth/MainLemma.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:676 | private `theta_lt_eta_of_sq_log_bound_aux`: `Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < eta δ m := by` |
| Roth/MainLemma.lean:687 | same lemma: `simpa [eta] using Θ_lt n hδpos` |
| Roth/MainLemma.lean:699 | private `exists_auxiliary_polynomial_with_index_gap_aux`: `gam δ f.natDegree m - eta δ m + Θ ((q 0 : ℝ) ^ (δ * r 0)) q r <` |
| Roth/MainLemma.lean:750 | `main_lemma`: `(gam δ f.natDegree m - eta δ m) + Θ ((q 0 : ℝ) ^ (δ * r 0)) q r) / 2` |
| Roth/MainLemma.lean:760 | `main_lemma`: `linarith only [hgap, index_le_Θ hW hh])` |
| Roth/Theta.lean:101–166 | API: `index_le_Θ`, `Θ_nonneg`, `Θ_le_card`, `Θ_le_of_forall_index_le`, `Θ_mono`, `Θ_equiv` |
| Roth/Theta.lean:253–258 | `index_unique_le_log_div` / `Θ_unique_le` (Lemma 5): `Θ B q r ≤ Real.log B / (r default * Real.log (q default))` |
| Roth/Theta.lean:273, 276 | `lem6M`, `lem6Φ`: `lem6Φ q r M l := Θ M (q ∘ some) … + Θ M (fun _ ↦ q none) …` |
| Roth/Theta.lean:443–450, 583–599 | `index_separated_mul_le_aux`, `index_le_lem6`, `Θ_option_le` (Lemma 6) |
| Roth/Theta.lean:707–966 | `lem7_Φ_bound`, `theta_scaled_unique_le_aux`, `theta_prefix_lt_aux`, `theta_phi_lt_aux`, `theta_lt_succ_aux`, `theta_lt_of_large_delta_aux`, `Θ_lt` (Lemma 7): `Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))` |

Inline-derivation grep:
  - (none). No file writes `sSup (indexSet …)` or the existential set directly; all consumers go through `Θ`.

### Composition check (Phase 6)

Can `Roth.Θ` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Θ B q r = sSup ((fun p ↦ index (map (Int.castRingHom ℝ) p.1) (fun j ↦ (p.2 j : ℝ) / q j) r) '' (RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)}))`
  - Mathlib decls used: `sSup` (`ConditionallyCompleteLattice ℝ`), `Set.image`, `Set.prod` (`×ˢ`), `IsCoprime`, `MvPolynomial.map`, `Int.castRingHom`; project: `Roth.RSet`, `Roth.index`
  - Result: succeeds (evidence (2), `congr 1; ext` plus `simp only` and a two-line `rintro`)
  - Notes: the only non-mathlib ingredients are the project defs `RSet` and `index`.

Conclusion: COMPOSABLE. `Θ` is one `sSup` of one `Set.image` of the project's `index` over a product set. No new mathematics.

### Verdict: `Roth.Θ`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): `Θ_m` is Ridout/Cassels' supremum (clean.tex §5; Yamada arXiv math/0307203 §2); modern treatments (Evertse arXiv 2502.00731) state Roth's lemma pointwise and do not use the supremum.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for the project; no hypotheses, `[DecidableEq σ]` already absent (evidence (1)); widenings are false generalisations (Q9).
- Mathlib search (Phase 5): building blocks only (`sSup`, `Set.image`, `×ˢ`, `IsCoprime`, `MvPolynomial.map`, `Real.sSup_empty`).
- Composition check (Phase 6): COMPOSABLE as `sSup` of one `Set.image` (evidence (2)).

**Rationale:**

`Roth.Θ` is exactly the paper's `Θ_m(B; q; r)`: the real supremum of `Roth.indexSet`, which is itself the image of the project's `Roth.index` over `Roth.RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j)}`. As a mathlib object it would add only `sSup` on top of two project defs that are themselves not mathlib material (`Roth.RSet`, `Roth.indexSet`: NO-composable-from-mathlib; `Roth.index`: BORDERLINE, with any upstreaming aimed at a general weighted order at a point). The quantity is a bookkeeping device of the Ridout/Cassels presentation of Roth's lemma; current literature avoids it, and mathlib would not want a Roth-specific supremum (nor a Greek-letter def name).

Belongs-elsewhere check: keep it project-locally in Roth/Theta.lean. It is not junk: it is the named quantity in Lemmas 5–7 and in `main_lemma`, and its `csSup` API keeps ~20 consumers short. The usual "inline at call sites" refactor for this bucket is not recommended: replacing `Θ B q r` by the composed `sSup (… '' …)` at every call site would make every statement of Lemmas 5–7 and `main_lemma` unreadable. The composition only explains why the def should not go to mathlib.

Mathlib building blocks: `sSup` / `ConditionallyCompleteLattice` (Mathlib/Order/ConditionallyCompleteLattice/Defs.lean), `Real.sSup_empty` (Mathlib/Algebra/Order/Archimedean/Real/Basic.lean), `Set.image` (Mathlib/Data/Set/Defs.lean), `Set.prod` / `×ˢ`, `IsCoprime` (Mathlib/RingTheory/Coprime/Basic.lean), `MvPolynomial.map`, `Int.castRingHom`.
Composition sketch (≤3 lines):
```lean
example {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : Roth.Θ B q r = sSup
    ((fun p : MvPolynomial σ ℤ × (σ → ℤ) ↦ index (map (Int.castRingHom ℝ) p.1)
      (fun j ↦ (p.2 j : ℝ) / q j) r) '' (Roth.RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)}))
```
Call sites in our project (from Phase 6.0): 3 declarations in Roth/MainLemma.lean (`theta_lt_eta_of_sq_log_bound_aux`, `exists_auxiliary_polynomial_with_index_gap_aux`, `main_lemma`), plus ~20 declarations in Roth/Theta.lean.
Refactor plan: none required. Keep `Roth.Θ` and its API; optionally add "for `B < 1` the family is empty and `Θ = 0`" to the docstring.
Next action: no upstreaming. Leave the def and its call sites as is.

---

### Next step

No upstreaming. Keep `Roth.Θ` in Roth/Theta.lean. Any reusable content (a weighted order of vanishing at a point) is tracked under `Roth.index`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ/Theta_vs_mathlib.lean` (imports `Roth.Theta`; `lean_diagnostic_messages` reports no diagnostics):
  (1) `Θ B q r` elaborates with only `[Fintype σ]` (no `DecidableEq`);
  (2) `Θ_eq_sSup_image`: `Θ B q r` is `sSup` of the `Set.image` of the index map over `RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)}`;
  (3) `Θ_of_lt_one`: for `B < 1`, `Θ B q r = 0` (empty family, `Real.sSup_empty`).
  The first draft failed only because the evidence `example` (1) was not marked `noncomputable`; fixed, file now clean.
- Mathlib grep: `^namespace Roth` (none), `def Θ` (none).
- Lean-Finder (1), LeanSearch (1), Loogle (1) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex §5 l.655–702.
- Project grep `grep -rn Θ Roth/` for the call-sites table.
