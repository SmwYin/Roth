---
decl: Roth.kroneckerExp
file: Roth/GenWronskian.lean
line: 57
kind: def
visibility: public
verdict: NO-mathlib-has-it
cost: CHEAP
junk: REPLACE
rationale: kroneckerExp k is exactly the coercion of mathlib's AddMonoidHom Finsupp.weight (fun j ↦ k ^ equivFin σ j) (verified as a function equality), and after reindexing along equivFin it is mathlib's Behrend.map k, whose Behrend.map_injOn already gives the base-k injectivity the project reproves in kroneckerExp_injOn.
action: Replace kroneckerExp by Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) in Roth/GenWronskian.lean (kronecker_monomial l.60-62, kroneckerExp_injOn l.69-82, coeff_kronecker l.88-97); reprove kroneckerExp_injOn from Behrend.map_injOn via the reindexing (verified, 5 lines); do not upstream kroneckerExp itself.
---

# Roth.kroneckerExp

## Inventory entry

### `def Roth.kroneckerExp`
- **Type**: `{σ : Type*} → [Fintype σ] → (k : ℕ) → (σ →₀ ℕ) → ℕ`
- **What**: The exponent of the image of the monomial `X^d` under the Kronecker substitution `x_j ↦ t^{k^{e j}}`: `kroneckerExp k d = ∑ j, d j * k ^ (e j)`, with `e = Fintype.equivFin σ`.
- **How**: One-line definition as a `Finset.univ` sum; no proof.
- **Hypotheses**: `[Fintype σ]` (for the `Finset.univ` sum and for `Fintype.equivFin`). The section's `[Field K]` is not a parameter (unused by this def).
- **Uses from project**: `[]`
- **Used by**: `Roth.kronecker_monomial` (Roth/GenWronskian.lean:61-62), `Roth.kroneckerExp_injOn` (Roth/GenWronskian.lean:69-74), `Roth.coeff_kronecker` (Roth/GenWronskian.lean:89, 97). Indirectly via `coeff_kronecker`: `Roth.kronecker_eq_zero_iff` (l.111). No use outside Roth/GenWronskian.lean.
- **Visibility**: public
- **Lines**: 56-57, proof length 0 lines (one-line body)
- **Notes**: Plain (unbundled) function; mathlib's `Finsupp.weight` would give additivity (`map_add`, `map_zero`) and `weight_single` for free. Depends on the noncanonical `Fintype.equivFin`.

## Junk check (Step 8)
- Used anywhere? Yes, 3 lemmas in the same file (kronecker_monomial, kroneckerExp_injOn, coeff_kronecker).
- Wrapper of 1-2 mathlib calls? Yes: it is `⇑(Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`, verified by `ext d; simp [kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]` and also by `simp [Finsupp.weight_eq_sum, kroneckerExp]`.
- Does mathlib have it? Yes, twice: `Finsupp.weight` (Mathlib/Data/Finsupp/Weight.lean:82) and, for `σ = Fin n`, `Behrend.map` (Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean:133, `a ↦ ∑ i, a i * d ^ i` as an AddMonoidHom) with `Behrend.map_injOn` (l.162).
- Too specific? The specific weight `k ^ equivFin σ j` is Kronecker-specific; the right local object is the weight function, not a new exponent def.
- Well-chosen definition? No: it duplicates mathlib's `Finsupp.weight` without its AddMonoidHom structure.
- Conclusion: `REPLACE`. Action: use `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))` (optionally a local `abbrev` for the weight function `fun j ↦ k ^ e j`) at the three call sites; reprove `kroneckerExp_injOn` from `Behrend.map_injOn`.

## Mathlibable assessment (Step 9)

Pre-filter: name does not end `_aux`; docstring does not start internal/auxiliary; Step 8 said REPLACE (not REMOVE); the qualified name `Roth.kroneckerExp` does not exist in mathlib. Not a glue lemma. Parent `Roth.kronecker` was assessed `YES-but-generalise-first` and its report claims `kroneckerExp k d = Finsupp.weight (fun j ↦ k ^ equivFin σ j) d`; verified independently below, and per the re-aim rule the assessment is aimed at `Finsupp.weight` (and at `Behrend.map`, found in this run). Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing Roth.GenWronskian elaborates)
- decl `Roth.kroneckerExp`:  ✓ resolved at Roth/GenWronskian.lean:57
- kind:                      def
- has sorry:                 no
- module docstring summary:  Generalized Wronskians and Lemma 1 (linearly independent families have a nonvanishing generalized Wronskian), via Kronecker substitution.

### Statement (Phase 1)

`Roth.kroneckerExp` is a definition of the following:

For a finite variable set σ enumerated as `e : σ ≃ {0, …, p-1}` and a base `k`, the Kronecker exponent of an exponent vector `d ∈ ℕ^σ` is `∑_j d_j k^{e(j)}`, i.e. the integer whose base-`k` digits are `d_{e⁻¹(0)}, d_{e⁻¹(1)}, …` (when all `d_j < k`). It is the weighted degree of `X^d` for the weight `w_j = k^{e(j)}`, and the exponent of `t` in the image of `X^d` under `x_j ↦ t^{k^{e(j)}}`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variable index set (finite, enumerated by `Fintype.equivFin`).
- `k : ℕ`: the base.
- `d : σ →₀ ℕ`: the exponent vector.

Hypotheses (Lean side):
- none beyond `[Fintype σ]`.

Conclusion (math): the natural number `∑_j d_j k^{e(j)}`.

Conclusion (Lean): n/a — definition (value `∑ j, d j * k ^ (Fintype.equivFin σ j : ℕ) : ℕ`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-line helper exponent function for the Kronecker substitution, not a new structure or a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                 | no       | no downstream proof depends on the def being sealed; all three callers immediately `simp`/unfold it or rewrite through `Nat.ofDigits` |
| Avoid typeclass diamonds          | no       | a plain ℕ-valued function; no instances involved |
| Mark semantic intent / API name   | no       | the stable name already exists in mathlib (`Finsupp.weight`), with more API (AddMonoidHom) |

Conclusion: ONE-LINER WITHOUT-EXEMPTION

### Literature search table

| #  | Channel                          | Query | Hit? | Standard form found | Notes |
|----|----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)        | Kronecker substitution exponent "s_1 + k s_2" multivariate to univariate polynomial monomial map | yes | `x^e ↦ y^{Σ e_i D^{i-1}}`, injective on monomials with all `e_i < D` | arXiv 1401.6694 (Arnold–Roche), 1807.08289, 2411.17330 |
|  2 | WebSearch (general form)         | weighted degree of a monomial with respect to weight vector linear form exponent vector | yes | weighted degree `⟨w, α⟩ = Σ w_i α_i` | arXiv 2202.05742; Singular/Magma manuals; the Kronecker exponent is the case `w_i = k^{i}` |
|  3 | WebSearch (aliases)              | "Kronecker map" OR "Kronecker's trick" exponent base k digits injective polynomial substitution x_i = t^{d^i} | yes | same; base-`D` decoding; variants reduce exponents mod p or randomise weights | arXiv 1102.2789, 1710.01301, 2302.08891 |
|  4 | ChatGPT MCP                      | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session (no such tool in the deferred-tool list) |
|  5 | Local references                 | grep `.mathlib-quality/references/clean.tex` for kronecker / `s_1 + k s_2` | yes | `t^{s_1 + k s_2 + ⋯ + k^{p-1} s_p}` (l.243-248); Lean note at l.266 asks for the Kronecker substitution as an algebra hom | source uses exactly the base-`k` exponent with variables enumerated `1..p` |
|  6 | nLab                             | ncatlab.org search "Kronecker substitution" | no | — | "No pages contain Kronecker substitution"; not a categorical concept |
|  7 | nCatLab (if categorical)         | same as #6 | no | — | not categorical; nLab/nCatLab same site |
|  8 | Stacks Project (if alg geom)     | n/a | n/a | — | n/a: an elementary computer-algebra/combinatorial exponent map, not an algebraic-geometry notion |
|  9 | MathOverflow / Math.SE           | mathoverflow Kronecker substitution injective base k exponents polynomial identity | no | — | no MO/MSE thread surfaced; only arXiv hits (2302.08891, 2404.00332) |
| 10 | recent arXiv (last 5 years)      | covered by #1/#3/#9 | yes | weighted / randomized / iterative Kronecker substitution with arbitrary weight vector | arXiv 2411.17330 (2024), 2404.00332 (2024), 2403.12716 (2024) |

### Literature summary

Concept identified as: Kronecker exponent map / weighted degree of a monomial (base-`k` encoding of exponent vectors).
Sources agree on the standard form: yes — `d ↦ Σ_i d_i D^{i}` with variables enumerated, injective on `{d : all d_i < D}`; the general notion is the weighted degree `Σ_i w_i d_i` for an arbitrary weight vector.
Most general standard form: the linear form (weight) `d ↦ Σ_i w_i d_i` for an arbitrary weight `w : σ → M` into an additive monoid; the Kronecker case is `w_i = k^{e(i)}`.
Generality dimensions where the literature varies:
  - weight vector: `D^{i}` (classical) to arbitrary or random weights (Arnold–Roche); most general is arbitrary `w`.
  - indexing: `Fin n` to arbitrary finite / finitely supported index sets.
Disagreement with the literature: none on content; the project fixes the weight `k ^ equivFin σ j` instead of exposing a weight vector.

### Generality analysis — `Roth.kroneckerExp`

Literature-standard form (from Phase 3): `Finsupp.weight w : (σ →₀ ℕ) →+ M`, specialised to `w j = k ^ e j`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|------------------------|-------------------|--------------------------|---------------------|---------------------------------|
| 1 | `[Fintype σ]` | finite index, `Finset.univ` sum | finitely supported `d`, any `σ` | yes | `Finsupp.weight` sums over `d.support`; no finiteness needed |
| 2 | weight `k ^ equivFin σ j` | fixed, noncanonical enumeration | arbitrary `w : σ → ℕ` (or into any `AddCommMonoid`) | yes | the definition never uses the shape of the weight |
| 3 | unbundled function | `(σ →₀ ℕ) → ℕ` | AddMonoidHom | yes | `Finsupp.weight` is already `→+` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the standard form is already in mathlib.
Number of weakening opportunities found: 3 (all realised by mathlib's existing `Finsupp.weight`)
Verified: `Evidence.kroneckerExp_eq_weight : Roth.kroneckerExp (σ := σ) k = ⇑(Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))` compiles (evidence file, `lean_diagnostic_messages` clean). Additivity then follows by `map_add` (verified).
Proposed restatement: none new — use `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`.
Cost of restatement: CHEAP — three call sites in one file; the monomial lemma rewrites in one line (verified, item 4 of the evidence file).

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|----------|----------|------------------------|---------------------------------|
|  1 | typeclasses instead of bundled hypotheses | no | plain function, no preambles | — |
|  2 | sequences vs filters | no | finite combinatorial sum; no topology | — |
|  3 | construction vs universal property | no | an explicit linear form | — |
|  4 | set-with-predicate vs bundled substructure | no | no substructure involved | — |
|  5 | field-specific vs (semi)ring | no | ℕ-valued; `[Field K]` is not a parameter of this def | — |
|  6 | 1-categorical vs higher | no | not categorical | — |
|  7 | concrete index to general | yes | weight `k ^ e j` to arbitrary `w`; unbundled sum to the AddMonoidHom `Finsupp.weight w` | `map_add`, `map_zero`, `Finsupp.weight_single`, `le_weight`, `MvPolynomial.isWeightedHomogeneous_monomial`, `weightedTotalDegree` |
|  8 | concrete-via-abstract | no | the body is the one-line sum; no proof to inspect | — |
|  9 | false-generalisation guard | no false generalisation | `⇑(Finsupp.weight (k ^ e ·)) = kroneckerExp k` as functions (verified), same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))` (already in mathlib).
  - Cost: CHEAP
  - Mathlib downstream this enables: AddMonoidHom API (`map_add`, `map_sum`), `Finsupp.weight_single`, the weighted-homogeneous API (`IsWeightedHomogeneous`, `weightedTotalDegree`).
  - Real mathematical improvement: it removes a duplicate of an existing mathlib definition and makes the exponent additive by construction.

### Proof strategy — `Roth.kroneckerExp`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|-----------------------|----------------|
| 1 | Topology ε-δ vs filters | no | — (definition, no proof) | — |
| 2 | Algebra element-wise vs point-free | no | — | — |
| 3 | Sequences vs nets | no | — | — |
| 4 | Construction vs universal property | no | — | — |
| 5 | Helper lemmas mathlib should have | partly | a `Finsupp.weight`-stated base-`k` injectivity on the box `{d : ∀ j, d j < k}`; mathlib has it for `Fin n → ℕ` as `Behrend.map_injOn`, and privately in `NoetherNormalization.sum_r_mul_ne` | follow-up (belongs to the parent `Roth.kronecker` upstreaming plan) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED (for the dependent lemma, not the def)
  - Proposed strategy: define nothing; use `Finsupp.weight`; derive `kroneckerExp_injOn` from `Behrend.map_injOn` by reindexing along `equivFin` (verified, `Evidence.kroneckerExp_injOn'`, which also drops the `1 < k` hypothesis).
  - Cost: CHEAP
  - Missing mathlib API (if any): a `Finsupp.weight (k ^ e ·)` injectivity lemma for injective `e : σ → Fin n` (optional; `Behrend.map_injOn` suffices locally).
  - Would refactoring make the proof strictly shorter / cleaner? yes (12-line `Nat.ofDigits` proof becomes a 5-line transfer).

### Diamond / defeq risk — `Roth.kroneckerExp`

| # | Risk | Verdict | Evidence / rationale |
|---|------|---------|----------------------|
| 1 | Typeclass diamond | none | ℕ-valued function; no instance declared or consumed besides `Fintype σ` |
| 2 | Reducibility leak | none | plain semireducible `def`; callers unfold it explicitly with `simp [kroneckerExp]` |
| 3 | Non-canonical unfolding | low | value depends on the `Fintype σ` instance through `Fintype.equivFin`; two instances give different (but propositionally related) exponents |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*` polymorphic, value in ℕ |
| 6 | Coercion ambiguity | none | no `CoeFun`; replacing it by `⇑(Finsupp.weight _)` uses mathlib's standard AddMonoidHom coercion |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none HIGH (row 3 low: dependence on `Fintype.equivFin`).
Recommended mitigations: n/a.

### Mathlib search-status: `Roth.kroneckerExp`

[A] Lean-Finder       "weighted sum of exponents of a monomial: sum_i d_i * w_i for finitely supported d"  hits: `Finsupp.weight`, `Finsupp.weight_apply`, `MvPolynomial.isWeightedHomogeneous_monomial`, `MvPolynomial.weightedTotalDegree`
[B] Loogle            `Finsupp.weight`  hits: `Finsupp.weight`, `weight_single`, `le_weight`, `degree_eq_weight_one`, `finite_of_nat_weight_le`, …
[C] LeanSearch        "sum over i of d i times k to the power i, base k representation of exponent vector"  hits: `Nat.ofDigits_eq_sum_mapIdx`, `Behrend.map : ℕ → (Fin n → ℕ) →+ ℕ`
[D] Grep mathlib src  `def weight` in Data/Finsupp/Weight.lean (l.82, plus `weight_eq_sum` for `[Fintype σ]`); `def map`/`map_injOn` in Combinatorics/Additive/AP/Three/Behrend.lean (l.133, l.162); `ofDigits` in RingTheory/NoetherNormalization.lean (private `sum_r_mul_ne`, l.89)
[E] Name pattern      lean_local_search `kroneckerExp`: n/a (ripgrep not installed for the tool); grep of mathlib for `kroneckerExp`: no hits

Searched for both:
  - the user's current form (`∑ j, d j * k ^ e j`)
  - the literature-standard form (weighted degree `Finsupp.weight w`)

Concluded: found in mathlib as `Finsupp.weight`; more general form (we are the specialisation `w = (k ^ equivFin σ ·)`). Also found `Behrend.map` (identical form on `Fin n → ℕ`) with `Behrend.map_injOn`.

### Normal-form check — `Roth.kroneckerExp`

Equivalent formalisms this statement could take: `∑ j, d j * k ^ e j` (project); `Finsupp.weight (k ^ e ·) d`; `Behrend.map k (d ∘ e.symm)`; `Nat.ofDigits k (List.ofFn (d ∘ e.symm))`.
Does mathlib already have a canonical form for this idea? yes — `Finsupp.weight` (Mathlib/Data/Finsupp/Weight.lean).
If yes: is our statement stated against the canonical form? NO — REFACTOR: use `Finsupp.weight`, with `Finsupp.weight_eq_sum` as the bridge to the explicit sum.
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.kroneckerExp`

Alternative restatements attempted (list):
- `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))` (verified equal)
- `Behrend.map k fun i ↦ d ((Fintype.equivFin σ).symm i)` (verified equal)

Chosen restatement: `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`
Justification: it lives on `σ →₀ ℕ` like the call sites (no reindexing), and `MvPolynomial` monomial/weighted-homogeneous lemmas are stated with it; `Behrend.map` is used only inside the injectivity proof.

### Superfluous-argument audit — `Roth.kroneckerExp`

| # | Argument / typeclass | Essentially used? | Notes |
|---|----------------------|-------------------|-------|
| 1 | `[Fintype σ]` | only for `equivFin` | `Finsupp.weight` itself needs no finiteness; the Kronecker weight needs some injective enumeration |
| 2 | `k : ℕ` | yes | the base |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (use `Finsupp.weight`)
Syntactic generality: OK once replaced
Superfluous arguments: 1 to drop in the general form (`[Fintype σ]`), already absent from `Finsupp.weight`

Overall: RESTATE-BEFORE-SHIP (locally: replace by `Finsupp.weight`)

### Call sites — `Roth.kroneckerExp`

Internal use count: 0 outside the declaring file (5 occurrences inside Roth/GenWronskian.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|------------------|----------------------------------|
| Roth/GenWronskian.lean:61 | `kronecker k (monomial d a) = Polynomial.C a * Polynomial.X ^ kroneckerExp k d` |
| Roth/GenWronskian.lean:62 | `simp [kronecker, kroneckerExp, aeval_monomial, …]` |
| Roth/GenWronskian.lean:70 | `Set.InjOn (kroneckerExp (σ := σ) k) {d \| ∀ j, d j < k}` |
| Roth/GenWronskian.lean:73-74 | `Nat.ofDigits k (List.ofFn …) = kroneckerExp k d` (unfolded via simp) |
| Roth/GenWronskian.lean:89 | `(kronecker k P).coeff (kroneckerExp k d) = P.coeff d` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.kroneckerExp`?):
  - (none in the project). In mathlib the same sum is re-derived as `Behrend.map` and inside the private `NoetherNormalization.sum_r_mul_ne`.

### Composition check (Phase 6)

Can `Roth.kroneckerExp` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⇑(Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`
  - Mathlib decls used: `Finsupp.weight`, `Finsupp.weight_apply`/`Finsupp.weight_eq_sum`, `Fintype.equivFin`
  - Result: succeeds (equality of functions by `ext d; simp [kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]`)
  - Notes: none

Attempt 2: `Behrend.map k (d ∘ (Fintype.equivFin σ).symm)`
  - Mathlib decls used: `Behrend.map`, `Behrend.map_apply`, `Equiv.sum_comp`
  - Result: succeeds (2-line proof); additionally `Behrend.map_injOn` yields `kroneckerExp_injOn` in 5 lines

Conclusion: COMPOSABLE (in fact identical to an existing mathlib def)

## Verdict: `Roth.kroneckerExp`

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): the Kronecker exponent is the weighted degree `Σ w_i d_i` at `w_i = k^{e(i)}`; standard and well known.
- Generality analysis (Phase 4): STRICTLY NARROWER than the standard weighted degree, which mathlib already has.
- Mathlib search (Phase 5): found in mathlib as `Finsupp.weight` (more general) and as `Behrend.map` (identical on `Fin n → ℕ`).
- Composition check (Phase 6): COMPOSABLE, verified as a function equality.

**Rationale:**

`kroneckerExp k` is, as a function on `σ →₀ ℕ`, exactly the coercion of `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`. This confirms the claim in the parent `Roth.kronecker` report, and it is proved here as a function equality, not only pointwise. Mathlib's version is an `AddMonoidHom` and connects to the weighted-homogeneous `MvPolynomial` API, so the project def is a strictly weaker duplicate. The one-liner has no Phase 2b exemption and no caller outside its file.

The re-aim rule applies to the dependent lemma `Roth.kroneckerExp_injOn`. Mathlib already has the base-`k` injectivity as `Behrend.map_injOn` for `Behrend.map k : (Fin n → ℕ) →+ ℕ`. After reindexing along `equivFin`, `kroneckerExp k d = Behrend.map k (d ∘ e.symm)`, and the project's 12-line `Nat.ofDigits` proof becomes a 5-line transfer. That transfer was verified and also drops `1 < k`. A `Finsupp.weight`-stated box injectivity is still missing from mathlib. It belongs to the parent's `weightedSubst` upstreaming plan, not to `kroneckerExp`.

WHY not (refactor-actionable):
- Mathlib already has the general form. Our form is the specialisation `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`, and the equality is a one-line `ext; simp`.

Belongs-elsewhere check: nothing worth keeping beyond, at most, a local `abbrev` for the weight function `fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)` in Roth/GenWronskian.lean.

Existing mathlib decl:        `Finsupp.weight` (also `Behrend.map`, `Behrend.map_injOn`)
Located at:                   `Mathlib/Data/Finsupp/Weight.lean:82` (and `Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean:133,162`)
Our form follows in ≤1 line:
```lean
example (k : ℕ) : Roth.kroneckerExp (σ := σ) k =
    ⇑(Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) := by
  ext d; simp [Roth.kroneckerExp, Finsupp.weight_apply, Finsupp.sum_fintype]
```
Call sites in our project (from Phase 6.0): 5 occurrences in 3 lemmas, all in Roth/GenWronskian.lean
Refactor plan:
- l.61-62 `kronecker_monomial`: state with `Polynomial.X ^ Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) d`; the proof uses `Finsupp.weight_eq_sum` (or `weight_apply`) instead of unfolding `kroneckerExp`.
- l.69-82 `kroneckerExp_injOn`: restate as `Set.InjOn (Finsupp.weight fun j ↦ k ^ (Fintype.equivFin σ j : ℕ)) {d | ∀ j, d j < k}`. Prove it from `Behrend.map_injOn` via the reindexing identity (evidence items 5-6), which drops `hk`.
- l.88-97 `coeff_kronecker`: replace `kroneckerExp k d` by the weight. The proof is unchanged apart from the renamed injectivity lemma.

Next action: delete `Roth.kroneckerExp` and update those 3 lemmas in Roth/GenWronskian.lean. This fits naturally with the parent `Roth.kronecker` refactor to `aeval (X ^ w ·)`.

## Next step

Delete `Roth.kroneckerExp`. Switch `kronecker_monomial`, `kroneckerExp_injOn` and `coeff_kronecker` (Roth/GenWronskian.lean:60-97) to `Finsupp.weight (fun j ↦ k ^ (Fintype.equivFin σ j : ℕ))`, and reprove the injectivity from `Behrend.map_injOn`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.kroneckerExp/weight.lean` (imports `Roth.GenWronskian` and `Mathlib.Combinatorics.Additive.AP.Three.Behrend`). `lean_diagnostic_messages` is clean (no errors, no warnings). It contains:
  1. `kroneckerExp_eq_weight`: a function equality with `⇑(Finsupp.weight fun j ↦ k ^ e j)`.
  2. A pointwise equality via `Finsupp.weight_eq_sum`.
  3. Additivity via `map_add`.
  4. `weight_pow_equivFin_injOn`: injectivity transferred to `Finsupp.weight`.
  5. `kronecker_monomial` restated with `Finsupp.weight` (one-line `rw`).
  6. `kroneckerExp_eq_behrendMap`: equality with `Behrend.map k (d ∘ e.symm)`.
  7. `kroneckerExp_injOn'`: injectivity from `Behrend.map_injOn`, with no `1 < k` hypothesis.
- Searches:
  - WebSearch ×4 (recorded in the literature table).
  - nLab search fetch: no page.
  - Loogle `Finsupp.weight`.
  - LeanSearch (found `Behrend.map`).
  - Lean-Finder (found `Finsupp.weight`).
  - Grep of the mathlib source: Weight.lean, Behrend.lean, NoetherNormalization.lean.
  - Grep of local refs `clean.tex`, l.243-266.
  - `lean_local_search` was unavailable because ripgrep is not installed.
- ChatGPT channel: n/a, the `ask_chatgpt_math` MCP is not configured in this session.
