---
decl: Roth.kroneckerExp_injOn
file: Roth/GenWronskian.lean
line: 69
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: REPLACE
rationale: Re-aimed at the parent's mathlib counterpart, the lemma is mathlib's Behrend.map_injOn composed (Set.InjOn.comp) with the injective reindexing d ↦ d ∘ equivFin.symm via a 2-line identity kroneckerExp k = Behrend.map k ∘ (· ∘ e.symm); verified in 3 proof lines, and the hypothesis 1 < k turns out to be superfluous.
action: In Roth/GenWronskian.lean replace the 12-line Nat.ofDigits proof of kroneckerExp_injOn (l.69-82) by the Behrend.map_injOn composition (import Mathlib.Combinatorics.Additive.AP.Three.Behrend), drop hk, and update the single caller coeff_kronecker (l.97); fold into the kroneckerExp → Finsupp.weight refactor; do not upstream.
---

# Roth.kroneckerExp_injOn

## Inventory entry

### `theorem Roth.kroneckerExp_injOn`
- **Type**: `{σ : Type*} [Fintype σ] {k : ℕ} (hk : 1 < k) : Set.InjOn (Roth.kroneckerExp (σ := σ) k) {d | ∀ j, d j < k}`
- **What**: The Kronecker exponent `d ↦ ∑ j, d j * k ^ (equivFin σ j)` is injective on exponent vectors all of whose entries are `< k` (uniqueness of base-`k` expansions).
- **How**: Rewrites `kroneckerExp k d` as `Nat.ofDigits k (List.ofFn (d ∘ e.symm))` (local `hsum`, via `Nat.ofDigits_eq_sum_mapIdx`, `List.mapIdx_eq_ofFn`, `Fin.sum_ofFn`, `Equiv.sum_comp`), then concludes with `Nat.ofDigits_inj_of_len_eq hk`, `List.ofFn_injective`, `Function.Surjective.injective_comp_right` and `DFunLike.coe_injective`.
- **Hypotheses**: `hk : 1 < k` (needed by `Nat.ofDigits_inj_of_len_eq`; mathematically superfluous, see below); `[Fintype σ]` (for `equivFin`).
- **Uses from project**: `Roth.kroneckerExp`
- **Used by**: `Roth.coeff_kronecker` (Roth/GenWronskian.lean:97). Nothing else in `Roth/`.
- **Visibility**: public
- **Lines**: 69-82, proof length 12 lines
- **Notes**: The `1 < k` hypothesis is not needed: for `k ≤ 1` the box `{d | ∀ j, d j < k}` is a subsingleton (`k = 1`: only `d = 0`; `k = 0`: empty unless `σ` is empty). The evidence proof via `Behrend.map_injOn` has no such hypothesis.

## Junk check (Step 8)
- Used anywhere? Yes, once (`coeff_kronecker`, l.97).
- Wrapper of 1-2 mathlib calls? Effectively yes: `Behrend.map_injOn` plus `Set.InjOn.comp` with an injective reindexing, after a 2-line identity `kroneckerExp k = Behrend.map k ∘ (· ∘ e.symm)` (verified).
- Does mathlib have it? For `σ = Fin n` exactly: `Behrend.map_injOn : Set.InjOn (Behrend.map d) {x : Fin n → ℕ | ∀ i, x i < d}` (Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean:162). Also the list form `Nat.injOn_ofDigits` / `Nat.ofDigits_inj_of_len_eq`, and a private `NoetherNormalization.sum_r_mul_ne`.
- Too specific? It is a specialisation to the project's noncanonical enumeration; the content is mathlib's.
- Well-chosen? The statement is fine for local use, but it carries a superfluous `1 < k` and reproves mathlib.
- Conclusion: `REPLACE`. Action: reprove from `Behrend.map_injOn` (3 lines), drop `hk`, keep as a local lemma (or restate against `Finsupp.weight` as part of the `kroneckerExp` refactor).

## Mathlibable assessment (Step 9)

Pre-filter: name does not end `_aux`; docstring does not start internal/auxiliary; Step 8 said REPLACE; the qualified name `Roth.kroneckerExp_injOn` is not in mathlib. Not a glue lemma (12-line proof). The parent `Roth.kroneckerExp` was assessed `NO-mathlib-has-it` because mathlib has `Finsupp.weight` / `Behrend.map`. Per the **re-aim rule**, the lemma is re-aimed at `Behrend.map` (the parent's identical mathlib counterpart): mathlib has the analogous lemma `Behrend.map_injOn`, so the re-aim is a hit. Because the transfer needs a reindexing step (not ≤1 line), the bucket is `NO-composable-from-mathlib` rather than `NO-mathlib-has-it`. Full run follows (independently verifying the parent report's 5-line claim, now shortened to 3 lines).

### Baseline (Phase 0)
- lake build:               ✓ clean (project built per brief; evidence file importing Roth.GenWronskian elaborates clean)
- decl `Roth.kroneckerExp_injOn`:  ✓ resolved at Roth/GenWronskian.lean:69
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Generalized Wronskians and Lemma 1 (linearly independent families have a nonvanishing generalized Wronskian), via Kronecker substitution.

### Statement (Phase 1)

`Roth.kroneckerExp_injOn` is a theorem stating the following:

Let σ be a finite set enumerated as `e : σ ≃ {0, …, p-1}` and `k > 1`. If `d, d' ∈ ℕ^σ` have all entries `< k` and `∑_j d_j k^{e(j)} = ∑_j d'_j k^{e(j)}`, then `d = d'`. This is the uniqueness of base-`k` expansions ("the representation of a natural number as `s_1 + k s_2 + ⋯ + k^{p-1} s_p` with `0 ≤ s_i < k` is unique").

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: variable index set.
- `k : ℕ`: the base.

Hypotheses (Lean side):
- `hk : 1 < k`: base at least 2 (superfluous, see Phase 5.5c).

Conclusion (math): the Kronecker exponent map is injective on the box `[0, k)^σ`.

Conclusion (Lean): `Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k}`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a helper lemma (uniqueness of base-`k` digits) used once inside the proof of Lemma 1.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 12 substantive lines
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped for theorems)

### Literature search table

| #  | Channel                          | Query | Hit? | Standard form found | Notes |
|----|----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)        | uniqueness of base k representation s_1 + k s_2 + ... + k^{p-1} s_p digits less than k Kronecker substitution injective monomials | yes | unique finite base-`k` representation with digits in `[0, k)` | Wikipedia "Kronecker substitution"; arXiv 2110.03746; Isabelle AFP `DigitsInBase` |
|  2 | WebSearch (general form)         | weighted degree map injective on box exponent vectors weight vector powers of D Kronecker substitution lemma | yes | Kronecker map `e ↦ Σ e_i D^{i-1}` is a bijection between the box `[0,D)^n` and `[0, D^n)` ("collision-free") | arXiv 2411.17330, 1807.08289 (Arnold–Roche), 1412.4088 |
|  3 | WebSearch (aliases)              | "base-b representation" uniqueness theorem mixed radix positional numeral system proof | yes | base-`b` uniqueness by the division algorithm / induction peeling off `a_0` | LibreTexts (Clark, Elementary Number Theory §1.25), cut-the-knot, Cornell CS2800 notes; mixed radix is the natural generalisation |
|  4 | ChatGPT MCP                      | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session (no such tool in the deferred-tool list) |
|  5 | Local references                 | grep `.mathlib-quality/references/clean.tex` for "unique" / Kronecker | yes | "FACT: Since each `s_i` is strictly smaller than `k`, the representation ... is unique" (l.245-250) and Lean note on restricted injectivity (l.264-270) | exactly the project statement |
|  6 | nLab                             | positional numeral uniqueness / Kronecker substitution | no | — | elementary number theory, no nLab page (parent run found no Kronecker page either) |
|  7 | nCatLab (if categorical)         | same as #6 | n/a | — | not a categorical concept |
|  8 | Stacks Project (if alg geom)     | n/a | n/a | — | elementary arithmetic, not algebraic geometry |
|  9 | MathOverflow / Math.SE           | covered by #1/#3 queries | no | — | standard textbook fact; no MO thread surfaced in the searches |
| 10 | recent arXiv (last 5 years)      | covered by #2 | yes | box injectivity of the Kronecker map used as a lemma | arXiv 2411.17330 (2024) |

### Literature summary

Concept identified as: uniqueness of base-`k` (positional) representation / collision-freeness of the Kronecker substitution on the box.
Sources agree on the standard form: yes — `Σ_{i<n} a_i k^i` determines `(a_i)` when all `0 ≤ a_i < k`.
Most general standard form: for `a : Fin n → ℕ` with entries `< k`, `a ↦ Σ a_i k^i` is injective (no condition on `k` needed for the injectivity statement itself); mixed-radix and arbitrary-index versions are routine generalisations.
Generality dimensions where the literature varies:
  - index set: `Fin n` (standard) to any finite set with an injective enumeration.
  - base: usually `k ≥ 2` assumed, but the injectivity on `[0,k)^n` holds for all `k`.
Disagreement with the literature: none; the project's extra `1 < k` is harmless but unnecessary.

### Generality analysis — `Roth.kroneckerExp_injOn`

Literature-standard form (from Phase 3): `Set.InjOn (Behrend.map k) {x : Fin n → ℕ | ∀ i, x i < k}` (any `k`).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|------------------------|-------------------|--------------------------|---------------------|---------------------------------|
| 1 | `hk : 1 < k` | assumed | none | yes | box is a subsingleton for `k ≤ 1`; verified: `Evidence.kroneckerExp_injOn'` has no `hk` and compiles |
| 2 | `[Fintype σ]`, enumeration `equivFin` | fixed equivalence | any injective `e : σ → Fin n` | yes (not verified, not needed) | only injectivity of the enumeration is used; this is a statement about `Finsupp.weight` that belongs to the parent's `weightedSubst` plan |
| 3 | function `kroneckerExp` | project def | `Finsupp.weight (k ^ e ·)` / `Behrend.map k` | yes | parent report: `kroneckerExp` is `Finsupp.weight`; the lemma is then a reindexed `Behrend.map_injOn` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD — but the standard form (`Behrend.map_injOn`) is already in mathlib.
Number of weakening opportunities found: 1 verified (drop `hk`), plus the re-aim of the function to `Finsupp.weight`.
Proposed restatement: `theorem kroneckerExp_injOn {k : ℕ} : Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k}` (verified, evidence item 2), proved from `Behrend.map_injOn`.
Cost of restatement: CHEAP — one caller (`coeff_kronecker`, l.97) just drops the `hk` argument.

### Modern-idiom check (Phase 4c)

| #  | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|----|----------|----------|------------------------|---------------------------------|
|  1 | typeclasses instead of bundled hypotheses | no | `hk` is a plain numeric hypothesis (and droppable) | — |
|  2 | sequences vs filters | no | finite arithmetic, no topology | — |
|  3 | construction vs universal property | no | an injectivity statement | — |
|  4 | set-with-predicate vs bundled substructure | no | the box `{d \| ∀ j, d j < k}` is the standard `Set.InjOn` domain (same shape as `Behrend.map_injOn`) | — |
|  5 | field-specific vs (semi)ring | no | ℕ-valued; no field involved | — |
|  6 | 1-categorical vs higher | no | not categorical | — |
|  7 | concrete index to general | yes | state against `Finsupp.weight (k ^ e ·)` rather than the project def | `map_add`, weighted-homogeneous API (via parent refactor) |
|  8 | concrete-via-abstract | yes | after `hsum`, the proof never mentions `kroneckerExp` again: it is base-`k` uniqueness for `Fin p → ℕ`, i.e. `Behrend.map_injOn` | the project proof becomes a corollary of the mathlib lemma |
|  9 | false-generalisation guard | no false generalisation | `kroneckerExp k = Behrend.map k ∘ (· ∘ e.symm)` is an equality of functions (verified), same object | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (locally)
  - Proposed mathlib-idiomatic restatement: none new for mathlib; locally derive from `Behrend.map_injOn` (and, after the parent refactor, state against `Finsupp.weight`).
  - Cost: CHEAP
  - Mathlib downstream this enables: reuses `Behrend.map_injOn` and `Set.InjOn.comp` instead of the `Nat.ofDigits`/`List.ofFn` detour.
  - Real mathematical improvement: removes a re-proof of a mathlib fact and an unnecessary hypothesis.

### Proof strategy — `Roth.kroneckerExp_injOn`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|----------|----------|-----------------------|----------------|
| 1 | Topology ε-δ vs filters | no | — | — |
| 2 | Algebra element-wise vs point-free | partly | point-free: `kroneckerExp k = Behrend.map k ∘ reindex`, then `Set.InjOn.comp` | CHEAP |
| 3 | Sequences vs nets | no | — | — |
| 4 | Construction vs universal property | no | — | — |
| 5 | Helper lemmas mathlib should have | optional | a `Finsupp.weight`-stated box injectivity (`Set.InjOn (Finsupp.weight (k ^ e ·)) {d \| ∀ j, d j < k}` for injective `e : σ → Fin n`) is missing; belongs to the parent `weightedSubst` upstreaming plan | follow-up |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: rewrite with the reindexing identity and apply `Behrend.map_injOn.comp` with the injective reindexing.
  - Cost: CHEAP
  - Missing mathlib API (if any): none needed locally (optional `Finsupp.weight` form, see row 5).
  - Would refactoring make the proof strictly shorter / cleaner? yes (12 lines with a 4-line `simp only` list → 3 lines + 2-line identity, no `hk`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.kroneckerExp_injOn`

[A] Lean-Finder       "uniqueness of base-b digit expansion: if all digits less than b, sum a_i b^i determines the digits"  hits: `Nat.digits_inj_iff`, `Nat.ofDigits_inj_of_len_eq`, `Nat.injOn_ofDigits`, `Nat.digits.injective`
[B] Loogle            `Set.InjOn ⇑(Finsupp.weight _)`  no hits (no `Finsupp.weight` box injectivity in mathlib)
[C] LeanSearch        "sum of d i times k to the power i is injective on vectors with entries less than k"  hits: `Behrend.map_injOn` (top hit, exact form for `Fin n → ℕ`), `Finset.geomSum_injective`, `Nat.injOn_ofDigits`
[D] Grep mathlib src  `ofDigits_inj`, `InjOn (weight`, `weight.*InjOn`: hits `Nat.ofDigits_inj_of_len_eq` (Data/Nat/Digits/Defs.lean:312), `Nat.injOn_ofDigits` (Data/Nat/Digits/Lemmas.lean:360), private `sum_r_mul_ne` (RingTheory/NoetherNormalization.lean:90); `map_injOn` in Combinatorics/Additive/AP/Three/Behrend.lean:162; no `Finsupp.weight` injectivity
[E] Name pattern      grep of mathlib for `kroneckerExp`: no hits (lean_local_search not used; parent run reported ripgrep missing for the tool)

Searched for both:
  - the user's current form (injectivity of `∑ j, d j * k ^ e j` on the box)
  - the literature-standard form (base-`k` uniqueness on `Fin n → ℕ`)

Concluded: found in mathlib as `Behrend.map_injOn`; identical content for `σ = Fin n` (we are a reindexed specialisation). Building blocks for our form: `Behrend.map_injOn`, `Behrend.map_apply`, `Equiv.sum_comp`, `Set.InjOn.comp`.

### Normal-form check — `Roth.kroneckerExp_injOn`

Equivalent formalisms this statement could take: `Set.InjOn (kroneckerExp k) box`; `Set.InjOn (Finsupp.weight (k ^ e ·)) box`; `Set.InjOn (Behrend.map k) box` on `Fin n → ℕ`; `Set.InjOn (Nat.ofDigits k) {L | L.length = n ∧ ∀ x ∈ L, x < k}`.
Does mathlib already have a canonical form for this idea? yes — `Behrend.map_injOn` (functions `Fin n → ℕ`) and `Nat.injOn_ofDigits` (lists).
If yes: is our statement stated against the canonical form? NO — REFACTOR: derive from `Behrend.map_injOn`.
RHS convention respected? n/a (`Set.InjOn` statement, not an equation).

### Syntactic generality — `Roth.kroneckerExp_injOn`

Alternative restatements attempted (list):
- `Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k}` without `hk` (verified)
- `Set.InjOn (Finsupp.weight fun j ↦ k ^ (equivFin σ j : ℕ)) {d | ∀ j, d j < k}` (verified in the parent's evidence file as `weight_pow_equivFin_injOn`)

Chosen restatement: drop `hk`; after the parent refactor, state against `Finsupp.weight`.
Justification: the caller `coeff_kronecker` no longer has to supply `hk` for this step, and the form matches mathlib's `Behrend.map_injOn` shape.

### Superfluous-argument audit — `Roth.kroneckerExp_injOn`

| # | Argument / typeclass | Essentially used? | Notes |
|---|----------------------|-------------------|-------|
| 1 | `hk : 1 < k` | no | only needed by the `Nat.ofDigits_inj_of_len_eq` route; `Behrend.map_injOn` has no base hypothesis (verified) |
| 2 | `[Fintype σ]` | yes | the definition of `kroneckerExp` and `equivFin` need it |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (derive from `Behrend.map_injOn`)
Syntactic generality: RESTATE (drop `hk`)
Superfluous arguments: 1 to drop (`hk`)

Overall: RESTATE-BEFORE-SHIP (locally)

### Call sites — `Roth.kroneckerExp_injOn`

Internal use count: 0 outside the declaring file (1 use inside Roth/GenWronskian.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|------------------|----------------------------------|
| Roth/GenWronskian.lean:97 | `exact ite_eq_right fun h ↦ hed (kroneckerExp_injOn hk (fun j ↦ …) hd h.symm)` (in `coeff_kronecker`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.kroneckerExp_injOn`?):
  - (none in the project). In mathlib the same fact appears as `Behrend.map_injOn`, `Nat.injOn_ofDigits`, and the private `NoetherNormalization.sum_r_mul_ne`.

### Composition check (Phase 6)

Can `Roth.kroneckerExp_injOn` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [kroneckerExp_eq_comp]; exact Behrend.map_injOn.comp reindex_injOn mapsTo`
  - Mathlib decls used: `Behrend.map_injOn`, `Set.InjOn.comp`, `Behrend.map_apply`, `Equiv.sum_comp` (for the identity)
  - Result: succeeds (evidence item 2, 3 proof lines; identity item 1, 2 lines `ext; simp [...]`)
  - Notes: the identity `kroneckerExp k = Behrend.map k ∘ fun d i ↦ d (e.symm i)` is the only glue; it disappears into `Finsupp.weight`-based API after the parent refactor.

Attempt 2: `Nat.injOn_ofDigits` via `List.ofFn` (the project's current route)
  - Result: succeeds but needs the 4-line `simp only` bridge and `hk`; strictly worse.

Conclusion: COMPOSABLE

## Verdict: `Roth.kroneckerExp_injOn`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): uniqueness of base-`k` expansion, a standard textbook fact; the source paper states it as a FACT (clean.tex l.245-250).
- Generality analysis (Phase 4): STRICTLY NARROWER (superfluous `1 < k`, fixed enumeration); the general form is in mathlib.
- Mathlib search (Phase 5): `Behrend.map_injOn` is the identical fact for `Fin n → ℕ`; no `Finsupp.weight`-stated version.
- Composition check (Phase 6): COMPOSABLE — `Behrend.map_injOn.comp` with the injective reindexing, after a 2-line identity.

**Rationale:**

Re-aiming at the parent's mathlib counterpart (`kroneckerExp` = `Finsupp.weight (k ^ e ·)` = `Behrend.map k ∘ (· ∘ e.symm)`), the lemma is exactly `Behrend.map_injOn` transported along the bijection `d ↦ d ∘ e.symm`. This was verified in Lean: the reindexing identity is `ext d; simp [Behrend.map_apply, kroneckerExp, ← e.symm.sum_comp _]`, and the injectivity is three lines using `Set.InjOn.comp`. This independently confirms the parent report's claim and shortens its 5-line transfer to 3 lines. The mathlib route also shows that `hk : 1 < k` is superfluous.

It is not `NO-mathlib-has-it` because our form is on `σ →₀ ℕ` with a noncanonical enumeration, so it does not follow in one line. It is not `YES`: the only missing piece in mathlib is a `Finsupp.weight`-stated box injectivity, and that belongs to the parent `Roth.kronecker` / `weightedSubst` upstreaming plan, not to this project-specific lemma.

WHY not (refactor-actionable):
- Mathlib has the building block `Behrend.map_injOn`, and the project lemma is a short composition with the reindexing `fun d i ↦ d ((Fintype.equivFin σ).symm i)`.

Belongs-elsewhere check: keep it as a local lemma in Roth/GenWronskian.lean, since it is the named "FACT" of the source proof and `coeff_kronecker` uses it. Re-prove it from mathlib, and if the parent refactor lands, state it against `Finsupp.weight`.

Mathlib building blocks:
- `Behrend.map_injOn` (Mathlib/Combinatorics/Additive/AP/Three/Behrend.lean:162)
- `Behrend.map_apply` (same file)
- `Set.InjOn.comp` (Mathlib/Data/Set/Function.lean)
- `Equiv.sum_comp` (Mathlib/Algebra/BigOperators/Group/Finset/Defs.lean area)

Composition sketch (≤3 lines; verified in the evidence file as two declarations, the inlined `show` form below is the same proof):
```lean
theorem kroneckerExp_injOn {k : ℕ} : Set.InjOn (kroneckerExp (σ := σ) k) {d | ∀ j, d j < k} := by
  rw [show kroneckerExp (σ := σ) k = Behrend.map k ∘ fun d i ↦ d ((Fintype.equivFin σ).symm i) by
    ext d; simp [Behrend.map_apply, kroneckerExp,
      ← (Fintype.equivFin σ).symm.sum_comp fun j ↦ d j * k ^ (Fintype.equivFin σ j : ℕ)]]
  refine Behrend.map_injOn.comp (fun d _ d' _ h ↦ ?_) fun d hd i ↦ hd _
  ext j; simpa using congrFun h (Fintype.equivFin σ j)
```

Call sites in our project (from Phase 6.0): 1

Refactor plan:
- Roth/GenWronskian.lean:69-82: replace the proof with the composition above, drop `hk`, and add `import Mathlib.Combinatorics.Additive.AP.Three.Behrend`. Optionally keep the name as the source's "FACT".
- Roth/GenWronskian.lean:97 (`coeff_kronecker`): `kroneckerExp_injOn hk (…) hd h.symm` becomes `kroneckerExp_injOn (…) hd h.symm`. `coeff_kronecker` uses its own `hk` only at this point (l.97), so it becomes unused there; a `/generalise` follow-up should drop it from `coeff_kronecker` and check `kronecker_eq_zero_iff` / `linearIndependent_kronecker`.

Next action: keep the lemma but rewrite its proof from `Behrend.map_injOn` and drop `hk`; do this together with the parent's `kroneckerExp` → `Finsupp.weight` refactor; do not upstream.

## Next step

Rewrite `Roth.kroneckerExp_injOn` (Roth/GenWronskian.lean:69-82) as the 3-line `Behrend.map_injOn.comp` composition without `hk`. Update its only caller `coeff_kronecker` (l.97), and then check whether `hk` can be dropped from `coeff_kronecker`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.kroneckerExp_injOn/compose.lean` (imports `Roth.GenWronskian` and `Mathlib.Combinatorics.Additive.AP.Three.Behrend`). `lean_diagnostic_messages` is clean (no errors, no warnings). It contains:
  1. `Evidence.kroneckerExp_eq_comp`: `kroneckerExp k = Behrend.map k ∘ fun d i ↦ d (e.symm i)`, a function equality.
  2. `Evidence.kroneckerExp_injOn'`: the project statement without `1 < k`, from `Behrend.map_injOn.comp` (3 lines).
- Also relied on: the parent's evidence file `.mathlib-quality/overview/evidence/Roth.kroneckerExp/weight.lean` (items `weight_pow_equivFin_injOn` and `kroneckerExp_injOn'`). It was read, not re-run.
- Searches:
  - WebSearch ×3 (recorded in the literature table).
  - Loogle `Set.InjOn ⇑(Finsupp.weight _)`: no hits.
  - LeanSearch: top hit `Behrend.map_injOn`.
  - Lean-Finder: hits `Nat.ofDigits_inj_of_len_eq`, `Nat.injOn_ofDigits`.
  - Grep of the mathlib source: Digits/Defs.lean, Digits/Lemmas.lean, NoetherNormalization.lean, Behrend.lean.
  - Grep of local refs `clean.tex`, l.240-270.
- ChatGPT channel: n/a, the `ask_chatgpt_math` MCP is not configured in this session.
