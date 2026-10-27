---
decl: Roth.indexSet
file: Roth/Theta.lean
line: 62
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: indexSet is the paper's set of indices ind(R; h/q; r) over R in R_m(B; r) and h coprime to q, whose sSup is Θ_m; it is exactly the Set.image of the index map over RSet B r ×ˢ {h coprime to q} (compiled), a proof-internal object of the Roth/Ridout argument with nothing general to upstream.
action: Do not upstream; keep Roth.indexSet in Roth/Theta.lean as the carrier of Θ (used only in Theta.lean by Θ, indexSet_nonempty, indexSet_bddAbove, index_le_Θ, Θ_le_of_forall_index_le, Θ_mono, indexSet_comp_subset, Θ_equiv); no call-site changes.
---

# Roth.indexSet

## Inventory entry

### `def Roth.indexSet`
- **Type**: `{σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : Set ℝ`
- **What**: The set of real numbers `ind(R; (h_j / q_j)_j; r)` where `R` ranges over `RSet B r` (nonzero integer polynomials with degree in `X j` at most `r j` and coefficients bounded by `B`) and `h : σ → ℤ` over tuples with each `h j` coprime to `q j`. Its supremum is `Θ_m(B; q; r)`.
- **How**: Set-builder `{x | ∃ R ∈ RSet B r, ∃ h, (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r = x}`, using `MvPolynomial.map`, `Int.castRingHom` and `IsCoprime` from mathlib.
- **Hypotheses**: none. Only `[Fintype σ]` is needed (inherited from `Roth.index`); the section variable `[DecidableEq σ]` is not included (evidence (1)).
- **Uses from project**: `Roth.RSet`, `Roth.index`
- **Used by**: Roth/Theta.lean only: `Θ` (68, `sSup (indexSet B q r)`), `indexSet_nonempty` (80), `indexSet_bddAbove` (87), `index_le_Θ` (102, via `indexSet_bddAbove` and membership), `Θ_le_of_forall_index_le` (127), `Θ_mono` (136), private `indexSet_comp_subset` (141–142), `Θ_equiv` (162–163). `Θ_nonneg` and `Θ_le_card` destructure membership through `Θ`'s `sSup`. Module docstring at lines 26 and 28. No uses outside Theta.lean (`grep -rn indexSet Roth/`).
- **Visibility**: public
- **Lines**: 62–64, proof length 0 lines (3-line def body)
- **Notes**: Source: clean.tex §5 l.657–664 (definition of `Θ_m`). The paper takes `q_j ≥ 1`, `r_j ≥ 1`, `B ≥ 1`, and writes `gcd(h_i, q_i) = 1`; Lean imposes none of the side conditions and phrases coprimality as `IsCoprime` over `ℤ`.

## Junk check (Step 8)
- Used anywhere? Yes. It is the set whose `sSup` defines `Θ`. Its nonemptiness and boundedness lemmas (`indexSet_nonempty`, `indexSet_bddAbove`) are what the `csSup` API needs in `index_le_Θ`, `Θ_le_of_forall_index_le`, `Θ_mono` and `Θ_equiv`.
- Wrapper of 1–2 mathlib calls? Essentially yes. It equals `Set.image` of the index map over `RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j)}` (evidence (2)). The image form is less readable at destructuring sites (`rintro _ ⟨R, hR, h, hh, rfl⟩`).
- Does mathlib have it? No. It is built from the project's `Roth.index` and `Roth.RSet`. Lean-Finder and Loogle find nothing similar.
- Too specific (inline?)? Inlining it into `Θ` would force `indexSet_nonempty` and `indexSet_bddAbove` to be restated about an anonymous set. The name keeps the `csSup` side conditions readable.
- Well-chosen definition? Yes. It is the paper's "set of numbers ind(R; h/q; r)" and gives the `Θ` lemmas a named carrier.

Conclusion: KEEP. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter: the def is public, its name does not end in `_aux`, its docstring is not internal or auxiliary, and Step 8 said KEEP. Mathlib has no `namespace Roth` (grep of `.lake/packages/mathlib/Mathlib/`), so no `Roth.indexSet`. It is not a glue lemma (it is the parent def of `Θ`). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` has no diagnostics)
- decl `Roth.indexSet`:      resolved at Roth/Theta.lean:62
- kind:                      def
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5, 6, 7 bounding it.

### Statement (Phase 1)

`Roth.indexSet` is a definition. For finite `σ`, a real `B` and `q, r : σ → ℕ`, it is the subset of `ℝ`

  `I(B; q; r) = { ind(R; (h_j/q_j)_j; r) : R ∈ ℛ(B; r), h ∈ ℤ^σ, gcd(h_j, q_j) = 1 for all j }`,

i.e. the set of values of the Roth index of bounded-height integer polynomials at rational points whose `j`-th coordinate has exact denominator `q_j`. The number `Θ_m(B; q; r)` is `sup I(B; q; r)`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]`: the variables (finiteness is needed by `index`, a finite sum of weights).
- `B : ℝ`: coefficient bound (passed to `RSet`).
- `q : σ → ℕ`: denominators of the evaluation points.
- `r : σ → ℕ`: degree bounds and index weights.

Hypotheses (Lean side):
- none.

Conclusion (math): a subset of `ℝ`.

Conclusion (Lean): n/a — definition (`def indexSet (B : ℝ) (q r : σ → ℕ) : Set ℝ := {x | ∃ R ∈ RSet B r, ∃ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) ∧ index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r = x}`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is listed as a main definition of Theta.lean, but it is only the carrier set of `Θ`, an image of the project's `index` over an admissible family. It introduces no structure and is not a named theorem.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive set-builder (spread over 2 source lines)
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | membership is destructured directly (`rintro _ ⟨R, hR, h, hh, rfl⟩` in `Θ_le_of_forall_index_le`, `Θ_mono`, `indexSet_comp_subset`) and built by anonymous constructor (`index_le_Θ`, `indexSet_nonempty`); nothing relies on sealing |
| Avoid typeclass diamonds         | no       | no instances |
| Mark semantic intent / API name  | yes      | it names the paper's "set of numbers ind(R; h/q; r)" and carries the `csSup` side lemmas `indexSet_nonempty`, `indexSet_bddAbove` used by `index_le_Θ`, `Θ_le_of_forall_index_le`, `Θ_mono` |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local API name only; the exemption does not argue for mathlib)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof Theta_m(B; q_1,...,q_m; r_1,...,r_m) supremum of index of polynomials at rational points h_i/q_i gcd | partial | Roth's lemma bounds the index of a polynomial at a point of rational approximations (Evertse arXiv 2502.00731; Luminy notes) | no source in this query states the set of indices as a named object |
| 2 | WebSearch (general form) | set of indices of polynomials at rational points supremum index Roth lemma bounded height multidegree | yes | Yamada (arXiv math/0307203) defines `Θ_m(B; h/q; r)` as the supremum of the index over `ℛ_m(B; r)` and the points; Ferretti (arXiv math/9708214) multihomogeneous index | the supremum is defined directly; the set of indices is never named |
| 3 | WebSearch (named-after / aliases) | Roth's lemma index "Theta" Cassels Diophantine approximation Ridout index of polynomial at rational point supremum | partial | Ridout's form of Roth's lemma is quoted via `Θ_m` (Yamada); Cassels' tract (1957, Ch. VI) is the classical source | `Θ_m` notation traces to Ridout / Cassels; no separate name for the underlying set |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §5 l.657–670 | yes | "the supremum of the numbers ind(R; h_1/q_1, …; r) over all R ∈ ℛ_m(B; r) and integers h_i with gcd(h_i, q_i) = 1" | matches the Lean set exactly; Lean names the set and takes `sSup` |
| 6 | nLab | index of a polynomial / Roth's lemma | no | — | nLab has no Diophantine-approximation entry for this |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no index-of-polynomial notion there |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | no | — | discussions of Roth's lemma use the index pointwise; no named set of indices |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | partial | arXiv 2502.00731 (2025) proves Roth's lemma pointwise | same pointwise usage |

### Literature summary (Phase 3)

Concept identified as: the family of indices underlying Ridout's / Cassels' `Θ_m(B; q; r)` in Roth's lemma.
Sources agree on the standard form: yes. Every source defines `Θ_m` directly as a supremum over (polynomial, point) pairs. None names the set of values.
Most general standard form: `sup { ind(P; α; r) : P ∈ 𝒫, α ∈ A }` for an admissible polynomial family `𝒫` and point set `A`. Number-field versions (Ridout, Schmidt) replace rationals by algebraic points.
Generality dimensions where the literature varies:
  - points: rationals with fixed exact denominators (here) vs points of bounded height vs algebraic points.
  - polynomial class: naive height ≤ B (here) vs projective height.
Disagreement with the literature: none on content. Lean drops `q_j, r_j, B ≥ 1` (side lemmas add `1 ≤ B` where needed) and uses `IsCoprime` in `ℤ` for `gcd = 1`.

### Generality analysis — `Roth.indexSet`

Literature-standard form (from Phase 3): `{ ind(P; α; r) : P ∈ 𝒫, α ∈ A }` for an admissible family and point set.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | required | finitely many variables | NO | `index` sums `d j / r j` over `σ`; finiteness is essential |
| 2 | `[DecidableEq σ]` | not taken | not needed | already absent | evidence (1) |
| 3 | points `h_j / q_j` with `IsCoprime (h j) (q j)` | exact denominators | any admissible point set | yes, but changes the object | the exact-denominator condition is what Lemma 5 (Gauss's lemma on `q x - h`) uses; dropping it gives a different set |
| 4 | polynomial family `RSet B r` | fixed | any family | yes, but changes the object | as for RSet: integrality and the height bound are used in Lemmas 5–7 |
| 5 | `q, r, B` side conditions | none | paper: positive, `B ≥ 1` | already weaker than the paper | — |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for what the project needs). The def takes no hypotheses and no unused instances (evidence (1)). The two possible widenings (rows 3 and 4) are false generalisations (Q9): they define a different set.
Number of weakening opportunities found: 0
Proposed restatement: none. The image form (evidence (2)) is a reformulation, not a weakening.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | a set of reals, no limits |
| 3 | construction vs universal property? | no | — | a subset |
| 4 | bundled substructure? | partial | `Set.image (fun p ↦ index …) (RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j)})` (evidence (2)) | `Set.image` lemmas (`Set.Nonempty.image`, `bddAbove` via `Set.forall_mem_image`), or `Θ` as `⨆ p : admissible, index …`; neither shortens the current proofs, which destructure by `rintro` |
| 5 | field-specific to semiring? | no | — | the index is real-valued by design |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | arbitrary finite `σ` already |
| 8 | concrete-via-abstract? | no | — | no proof body |
| 9 | false-generalisation guard | yes (rows 3, 4 of Phase 4a) | widening the point set or the polynomial family changes the set and breaks Lemma 5's Gauss-lemma argument; the image form (row 4) is the same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only rephrasing is `Set.image` over a product set (evidence (2)), or an indexed `iSup` for `Θ`. It is the same object, and the existing `rintro`-style proofs would not get shorter.

### Proof strategy — `Roth.indexSet`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the generic `csSup` API (`le_csSup`, `csSup_le`, `csSup_le_csSup`, `Real.sSup_nonneg`, `Real.sSup_le`) is used directly; nothing is missing | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a definition with no proof. A named carrier set with `Nonempty` / `BddAbove` lemmas feeding the `csSup` API is the standard pattern.)

### Diamond / defeq risk — `Roth.indexSet`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; uses `MvPolynomial.map` and `Int.castRingHom ℝ` only |
| 2 | Reducibility leak | none | plain semireducible def; membership is unfolded by anonymous-constructor patterns, which is the intended use |
| 3 | Non-canonical unfolding | low | coprimality is `IsCoprime` in `ℤ` (not `Nat.gcd`/`Int.gcd = 1`) and the point is `(h j : ℝ) / q j` with real division, so `q j = 0` gives `h j / 0 = 0`; harmless because `IsCoprime h 0` forces `h = ±1` and the paper assumes `q_j ≥ 1` |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`; `Θ_equiv` transports across `σ ≃ τ` with independent universes |
| 6 | Coercion ambiguity | none | no coercions defined |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.indexSet`

[A] Lean-Finder       "supremum of the vanishing order (index) of integer polynomials with bounded coefficients at rational points"   hits: only `ChevalleyThm.MvPolynomialC.numBound/degBound` (unrelated)
[B] Loogle            `Roth.indexSet` (unknown to Loogle, expected: project decl); `Set ℝ, MvPolynomial, IsCoprime`   no hits
[C] LeanSearch        "image of a set under a function equals set of values attained by elements of the set"   hits: `Set.image`, `PFun.image_def`, `Set.mapsTo_image` (the building block used in evidence (2))
[D] Grep mathlib src  `namespace Roth` (none); no index-of-polynomial notion in mathlib (the closest notion, `MvPowerSeries.weightedOrder`, was analysed in the `Roth.index` report)
[E] Name pattern      `Set.image`, `Set.mem_image`, `Set.mem_prod`, `Prod.exists` (all used in compiled evidence)

Searched for both the user's form (indices of `RSet` polynomials at exact-denominator rational points) and the literature-standard form (sup of indices over an admissible family).

Concluded: found building blocks (`Set.image`, `Set.prod`, `IsCoprime`, `MvPolynomial.map`). The index itself is the project's `Roth.index` (BORDERLINE in its own report). Nothing in mathlib matches the set.

### Normal-form check — `Roth.indexSet`

Equivalent formalisms: (a) the current existential set-builder; (b) `Set.image` over `RSet B r ×ˢ {h | …}` (evidence (2)); (c) `Set.range` over the subtype of admissible pairs.
Does mathlib already have a canonical form for this idea? No; this is a project-specific set.
Is our statement stated against the canonical form? n/a. Form (a) is what every consumer destructures.
RHS convention respected? yes (in the evidence bridge, the image form is on the RHS).

### Syntactic generality — `Roth.indexSet`

Alternative restatements attempted:
- `Set.image` over a product set (evidence (2))
- `Set.range` over a subtype
Chosen restatement: current (a)
Justification: `rintro _ ⟨R, hR, h, hh, rfl⟩` and `⟨R, hR, h, hh, rfl⟩` are the shortest introduction and elimination forms at all eight consumers.

### Superfluous-argument audit — `Roth.indexSet`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `B` | yes | passed to `RSet` |
| 2 | `q` | yes | denominators and coprimality |
| 3 | `r` | yes | degree bounds and index weights |
| 4 | `[Fintype σ]` | yes | required by `index` |
| 5 | `[DecidableEq σ]` | not taken | evidence (1) |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project def)

### Call sites — `Roth.indexSet`

Internal use count: 0 outside the declaring file (11 lines inside Roth/Theta.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:68 | `noncomputable def Θ (B : ℝ) (q r : σ → ℕ) : ℝ := sSup (indexSet B q r)` |
| Roth/Theta.lean:80 | `theorem indexSet_nonempty ... : (indexSet B q r).Nonempty` |
| Roth/Theta.lean:87 | `theorem indexSet_bddAbove ... : BddAbove (indexSet B q r)` |
| Roth/Theta.lean:102 | `index_le_Θ`: `le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩` |
| Roth/Theta.lean:127 | `Θ_le_of_forall_index_le`: `csSup_le (indexSet_nonempty hB q r) ?_` |
| Roth/Theta.lean:136 | `Θ_mono`: `csSup_le_csSup (indexSet_bddAbove B' q) (indexSet_nonempty hB q r) ?_` |
| Roth/Theta.lean:141–142 | private `indexSet_comp_subset`: `indexSet B (q ∘ e) (r ∘ e) ⊆ indexSet B q r` |
| Roth/Theta.lean:162–163 | `Θ_equiv`: `subset_antisymm (indexSet_comp_subset e B q r) ...` |

Inline-derivation grep:
  - (none). Nothing in Roth/ restates the existential set without `indexSet`. Downstream files go through `Θ` and `index_le_Θ` / `Θ_le_of_forall_index_le`.

### Composition check (Phase 6)

Can `Roth.indexSet` be derived from mathlib in ≤3 chained calls?

Attempt 1: `indexSet B q r = (fun p ↦ index (map (Int.castRingHom ℝ) p.1) (fun j ↦ (p.2 j : ℝ) / q j) r) '' (RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)})`
  - Mathlib decls used: `Set.image`, `Set.prod` (`×ˢ`), `IsCoprime`, `MvPolynomial.map`, `Int.castRingHom`; project: `Roth.RSet`, `Roth.index`
  - Result: succeeds (evidence (2), `ext` plus `simp only` and a two-line `rintro`)
  - Notes: the only non-mathlib ingredients are the two project defs it is built from.

Conclusion: COMPOSABLE. It is a single `Set.image` of the project's `index` over a product of the project's `RSet` with a coprimality set. No new mathematics.

### Verdict: `Roth.indexSet`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the set is the family under Ridout / Cassels / Yamada's supremum `Θ_m` (clean.tex §5; arXiv math/0307203). Every source defines the supremum directly and never names the set.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for the project. There are no hypotheses, and `[DecidableEq σ]` is already absent (evidence (1)). Widening the points or the polynomial family is a false generalisation (Q9).
- Mathlib search (Phase 5): building blocks only (`Set.image`, `×ˢ`, `IsCoprime`, `MvPolynomial.map`).
- Composition check (Phase 6): COMPOSABLE as one `Set.image` (evidence (2)).

**Rationale:**

`Roth.indexSet` is the set of values `ind(R; h/q; r)` over `R ∈ ℛ_m(B; r)` and `h` coprime to `q`. Its `sSup` is `Θ_m(B; q; r)`, exactly as clean.tex §5 defines it. It contributes nothing beyond its two ingredients: it is the image of the project's `Roth.index` over `Roth.RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j)}` (compiled). Both ingredients have their own reports: `Roth.RSet` is NO-composable-from-mathlib, and `Roth.index` is BORDERLINE, with any upstreaming aimed at a weighted order at a point. A Roth-specific set of reals tied to bounded integer polynomials and exact-denominator rational points has no place in mathlib, and no source treats it as an object.

Belongs-elsewhere check: keep it project-locally as the carrier of `Θ`. It is not junk. The name lets `indexSet_nonempty` and `indexSet_bddAbove` discharge the `csSup` side conditions in `index_le_Θ`, `Θ_le_of_forall_index_le`, `Θ_mono` and `Θ_equiv`. The usual "inline at call sites" refactor for this bucket is not recommended. Inlining the image form into `Θ` and those eight sites would replace `rintro _ ⟨R, hR, h, hh, rfl⟩` with `Set.mem_image` / `Prod` plumbing and make every statement longer. The composition only explains why the def should not go to mathlib.

Mathlib building blocks: `Set.image` (Mathlib/Data/Set/Defs.lean), `Set.prod` / `×ˢ`, `IsCoprime` (Mathlib/RingTheory/Coprime/Basic.lean), `MvPolynomial.map`, `Int.castRingHom`.
Composition sketch (≤3 lines):
```lean
example {σ : Type*} [Fintype σ] (B : ℝ) (q r : σ → ℕ) : Roth.indexSet B q r =
    (fun p : MvPolynomial σ ℤ × (σ → ℤ) ↦ index (map (Int.castRingHom ℝ) p.1)
      (fun j ↦ (p.2 j : ℝ) / q j) r) '' (Roth.RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)})
```
Call sites in our project (from Phase 6.0): 0 outside Theta.lean; 8 consumers inside it (`Θ`, `indexSet_nonempty`, `indexSet_bddAbove`, `index_le_Θ`, `Θ_le_of_forall_index_le`, `Θ_mono`, `indexSet_comp_subset`, `Θ_equiv`).
Refactor plan: none required. Keep `Roth.indexSet` as the named carrier of `Θ` and do not upstream it.
Next action: no upstreaming. Leave the def and its call sites as is.

---

### Next step

No upstreaming. Keep `Roth.indexSet` in Roth/Theta.lean. Any reusable content (a weighted order at a point) is tracked under `Roth.index`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.indexSet/indexSet_vs_mathlib.lean` (imports `Roth.Theta`; `lean_diagnostic_messages` reports no diagnostics):
  (1) `indexSet B q r` elaborates with only `[Fintype σ]` (no `DecidableEq`);
  (2) `indexSet_eq_image`: `indexSet B q r` equals the `Set.image` of the index map over `RSet B r ×ˢ {h | ∀ j, IsCoprime (h j) (q j : ℤ)}`;
  (3) `Θ B q r = sSup (indexSet B q r)` by `rfl`.
  The first draft used the deprecated `Set.mem_setOf_eq` and lacked a module docstring. Both warnings were fixed, and the file is now clean.
- Mathlib grep: `namespace Roth` (none).
- Lean-Finder (1), LeanSearch (1), Loogle (2) queries as in the search-status block.
- WebSearch: 3 queries (literature table). ChatGPT MCP: n/a (not configured). Local refs: clean.tex §5 l.657–670.
- Project grep `grep -rn indexSet Roth/` for the call-sites table.
