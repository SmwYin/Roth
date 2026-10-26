---
decl: MvPolynomial.taylor_taylor
file: Roth/Taylor.lean
line: 146
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: The additive composition law of translations, P(X + β)(X + α) = P(X + α + β), is the exact multivariate counterpart of mathlib's Polynomial.taylor_taylor (used in FieldTheory/Laurent.lean and Polynomial/Taylor.lean) and is core API of the YES-add-as-is MvPolynomial.taylor; it is already maximally general (CommSemiring forced by MvPolynomial) and only needs the cosmetic restatement taylor (α + β) on the RHS before shipping.
action: Upstream with MvPolynomial.taylor in new Mathlib/Algebra/MvPolynomial/Taylor.lean, stated as taylor α (taylor β P) = taylor (α + β) P (Pi addition, matching Polynomial.taylor_taylor; evidence item 4) plus the bundled companion taylor_comp_taylor (item 5); locally keep (one call site, Roth/Taylor.lean:184 taylor_neg_taylor).
---

# MvPolynomial.taylor_taylor

## Inventory entry

### `theorem MvPolynomial.taylor_taylor`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α β : σ → R) (P : MvPolynomial σ R), (taylor α) ((taylor β) P) = (taylor fun j ↦ α j + β j) P`
- **What**: Translating first by `β` and then by `α` is translating by `α + β`: `P(X + β)` evaluated at `X + α` is `P(X + α + β)`.
- **How**: one `simp` call: unfold `taylor` to `aeval (fun j ↦ X j + C (α j))`, push the outer `aeval` inside with mathlib's `MvPolynomial.comp_aeval_apply` (`φ (aeval f p) = aeval (fun i ↦ φ (f i)) p`), then `aeval_X`, `map_add`, `algHom_C`, `C_add` and `add_assoc` identify the substitutions.
- **Hypotheses**: `[CommSemiring R]` (section variable, forced by `MvPolynomial`); no propositional hypotheses.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: Roth/Taylor.lean:184 (`taylor_neg_taylor`, via `simp [taylor_taylor]`), which in turn feeds `taylor_injective` and `taylor_eq_zero_iff` (Roth/Taylor.lean) and through them Roth/Index.lean. No other direct uses (`grep -rn taylor_taylor Roth/`).
- **Visibility**: public
- **Lines**: 146–148 (docstring 145), proof length 1 line
- **Notes**: Name identical to mathlib's univariate `Polynomial.taylor_taylor`. RHS uses the lambda `fun j ↦ α j + β j` rather than Pi addition `α + β` (definitionally equal; evidence item 4 proves the Pi form by the term `taylor_taylor α β P`). Not `@[simp]`; neither is the univariate one.

## Junk check (Step 8)
- Used anywhere? Yes: `taylor_neg_taylor` (Roth/Taylor.lean:184), the key step of `taylor_injective`.
- Wrapper of 1–2 mathlib calls? Short: one `simp` with `comp_aeval_apply`; but plain `simp` fails (evidence item 2), so it is not a trivial simp consequence, and the statement needs the project operator `taylor`.
- Does mathlib have it? No multivariate version; the univariate `Polynomial.taylor_taylor` is the template (Mathlib/Algebra/Polynomial/Taylor.lean:157).
- Too specific / inline? No: it is the group law of the translation operator, core API (mathlib uses the univariate one in FieldTheory/Laurent.lean:44, 103 and in `taylor_eval_sub`-style inverse arguments at Polynomial/Taylor.lean:210).
- Well-chosen? Yes; RHS would be cleaner as `α + β`.
- Conclusion: `KEEP` — action: keep locally; upstream with `MvPolynomial.taylor`, RHS restated with Pi addition.

## Mathlibable assessment (Step 9)

Not a glue lemma (needs `comp_aeval_apply`; plain `simp` fails, evidence item 2), not private / `_aux` / internal; qualified name `MvPolynomial.taylor_taylor` absent from mathlib (namespace-aware grep: `taylor_taylor` occurs only as `Polynomial.taylor_taylor`). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Taylor` compiles with no errors or warnings)
- decl `MvPolynomial.taylor_taylor`: resolved at Roth/Taylor.lean:146
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Taylor expansion of multivariate polynomials: translation `P ↦ P(X + α)` and its coefficients as Hasse derivatives.

### Statement (Phase 1)

`MvPolynomial.taylor_taylor` is a theorem stating the following:

Let `R` be a commutative semiring, `σ` a set of variables, `α, β ∈ R^σ`, and let `τ_α : R[X_σ] → R[X_σ]`, `τ_α P = P(X + α)`, be translation. Then `τ_α ∘ τ_β = τ_{α+β}`: for every `P`, `(P(X + β))(X + α) = P(X + α + β)`. In other words `α ↦ τ_α` is an action of the additive monoid `(R^σ, +)` on `R[X_σ]` by `R`-algebra endomorphisms.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — index set of variables.
- `R : Type*`, `[CommSemiring R]` — coefficient ring.
- `α β : σ → R` — the two translation vectors.
- `P : MvPolynomial σ R` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `τ_α (τ_β P) = τ_{α+β} P`.

Conclusion (Lean): `taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API lemma (composition law) of the parent definition `MvPolynomial.taylor`; not a main result.

(Note: literature width is EXHAUSTIVE regardless. BIG/SMALL is recorded for framing only.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | composition of translations multivariate polynomial P(X+a+b) shift operators commute E^a E^b = E^(a+b) | partial | shift operator `T_a f(x) = f(x + a)`; translations compose additively, `T_a T_b = T_{a+b}` | Wikipedia "Shift operator"; no source isolates the polynomial identity, regarded as immediate |
| 2 | WebSearch (general form) | translation group action on polynomial ring additive group R^n acts by algebra automorphisms x_i maps to x_i + a_i | yes | translations `X + v = (X_1 + v_1, ..., X_n + v_n)`, `v ∈ R^n`, form a subgroup of polynomial automorphisms isomorphic to `(R^n, +)` via `v ↦ X + v` | arXiv 0707.3151 (tame automorphisms over rings), arXiv 2303.12324 (`Q(x)·α = Q(x + α)` as a faithful action of `(R, +)`), arXiv 1709.04510; most general form: action of the additive monoid `R^σ` |
| 3 | WebSearch (named-after / aliases) | "Taylor shift" composition property shift by a then b equals shift by a+b polynomial | partial | Taylor shift `P(x) ↦ P(x + a)` as `e^{aD}`, so `e^{aD} e^{bD} = e^{(a+b)D}` | Codeforces "OGFs, EGFs, differentiation and Taylor shifts", arXiv 2003.12468, arXiv 1811.11093 (Isabelle Budan–Fourier uses Taylor shifts); alias "Taylor shift" = mathlib's name |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for translat / `P_\alpha` / `X+\alpha` | partial | l.547 "Let `P_α(X)=P(X+α)`"; l.600–629 translated polynomials | the paper never composes translations explicitly; the project uses the law only to invert translation (`taylor_neg_taylor`) |
| 6 | nLab | translation / action of an additive group / polynomial monad | partial | `R[X_σ]` free commutative algebra; substitutions compose by Kleisli composition (polynomial monad); translations are the action of the additive group of `R^σ` | composition law = monad associativity specialised to `X ↦ X + α` (mathlib: `bind₁_comp_bind₁`, `comp_aeval`) |
| 7 | nCatLab | — | n/a | — | not a categorical statement beyond the monad remark in row 6 |
| 8 | Stacks Project | — | n/a | — | translations of affine space form the group scheme `G_a^n` acting on `A^n`; Stacks has no polynomial-ring translation lemma (elementary commutative algebra) |
| 9 | MathOverflow / Math.SE | (results of #1, #3) | no | — | no dedicated thread; treated as immediate |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | partial | arXiv 2303.12324 (2023), 2501.10520 (2025, j-translations `X_j ↦ X_j + c`) | same additive-action form; no new formulation |

### Literature summary (Phase 3)

Concept identified as: the group (monoid) law of translations / Taylor shifts, `τ_α ∘ τ_β = τ_{α+β}`; i.e. `α ↦ τ_α` is an action of `(R^σ, +)` on `R[X_σ]` by algebra endomorphisms (automorphisms over a ring).
Sources agree on the standard form: yes.
Most general standard form: for any commutative (semi)ring `R` and any variable set, `τ_α ∘ τ_β = τ_{α+β}` as `R`-algebra maps (equivalently pointwise on every `P`).
Generality dimensions where the literature varies:
  - coefficient ring: field to commutative ring; ours is commutative semiring, the most general for `MvPolynomial`.
  - packaging: pointwise identity (most sources, and mathlib's univariate `Polynomial.taylor_taylor`) vs. an action / homomorphism `R^σ → End(R[X_σ])` (automorphism-group papers).
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.taylor_taylor`

Literature-standard form (from Phase 3): `τ_α ∘ τ_β = τ_{α+β}` on `R[X_σ]`, `R` a commutative semiring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative (semi)ring | no | forced by `MvPolynomial σ R` (parent evidence `MvPolynomial.taylor`, hasseDeriv `weaken_semiring_fails.lean`) |
| 2 | `α β : σ → R` | arbitrary functions | vectors in `R^σ` | no | already the full additive monoid `σ → R` |
| 3 | `σ : Type*` | arbitrary | finite | no (already more general) | — |
| 4 | packaging | pointwise | pointwise or AlgHom composition | n/a | the AlgHom form `(taylor α).comp (taylor β) = taylor (α + β)` is an equivalent companion (evidence item 5), not a weakening |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (no hypotheses; the only typeclass is forced by `MvPolynomial`).
Proposed restatement: none for generality. (A cosmetic RHS change `fun j ↦ α j + β j` to `α + β` is recorded in Phase 5.5; it is definitionally the same statement, evidence item 4.)

Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | the proof already goes through the universal property (`comp_aeval_apply`) | — |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical / bundled? | partial | bundled forms: `(taylor α).comp (taylor β) = taylor (α + β)` (item 5), and the monoid hom `Multiplicative (σ → R) →* (MvPolynomial σ R →ₐ[R] MvPolynomial σ R)` (item 6, compiles) | the AlgHom-comp companion is useful for `AlgHom.ext`-style arguments; the monoid-hom packaging has no mathlib precedent even univariately (mathlib's `Polynomial.taylor` has only pointwise `taylor_taylor`), so it is not a required modernisation |
| 7 | concrete index to general? | no | index already general | — |
| 8 | concrete-via-abstract? | no | statement mentions only the project operator; proof is generic substitution associativity, which mathlib already has in general form (`comp_aeval`); nothing further to abstract | — |
| 9 | false-generalisation guard | no false generalisation | the bundled forms are the same mathematical statement (each derived from the pointwise one in one line) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is the pointwise group law in exactly the shape mathlib uses for the univariate operator; bundled forms are optional companions (one-liners from this lemma), not an organisational improvement that changes the primary statement.

### Proof strategy — `MvPolynomial.taylor_taylor`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | already uses `comp_aeval_apply` (universal property of `aeval`) | — |
| 5 | missing mathlib helpers | no | `comp_aeval_apply`, `aeval_X`, `algHom_C` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (one `simp` through `comp_aeval_apply`, mirroring `Polynomial.taylor_taylor`'s `simp only [taylor_apply, comp_assoc, ..., add_assoc]`; a mathlib version might prefer `simp only [taylor_apply, comp_aeval_apply, ...]` for robustness, a style point for the PR).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.taylor_taylor`

[A] Lean-Finder       "composition of two translations of a multivariate polynomial is translation by the sum"   `Polynomial.taylor_taylor` (univariate), `MvPolynomial.bind₁_comp_bind₁`, `MvPolynomial.rename_rename`; no multivariate translation lemma
[B] Loogle            `MvPolynomial.aeval _ (MvPolynomial.aeval _ _)`   only `MvPolynomial.aeval_sumElim` (unrelated); no translation composition
[C] LeanSearch        "multivariate polynomial substitute X + C a then X + C b equals substitute X + C (a + b)"   `MvPolynomial.eval₂_add`, `MvPolynomial.bind₁`, `Polynomial.algEquivAevalXAddC_apply` (univariate); no hit
[D] Grep mathlib src  `taylor_taylor`, `taylor` under `Mathlib/Algebra/MvPolynomial`   `taylor_taylor` only at Algebra/Polynomial/Taylor.lean:157 (univariate) and its consumers FieldTheory/Laurent.lean:44, 103 and Polynomial/Taylor.lean:210; nothing in `Algebra/MvPolynomial`; building blocks `MvPolynomial.comp_aeval` (Eval.lean:607), `comp_aeval_apply` (Eval.lean:612), `bind₁_comp_bind₁` (Monad.lean)
[E] Name pattern      `MvPolynomial.taylor_taylor` (namespace-aware grep; `lean_local_search` unavailable: ripgrep not installed)   no hits

Searched for both the user's form and the literature-standard forms (pointwise and AlgHom-composition, and the general-substitution form `comp_aeval` / `bind₁_comp_bind₁`, which mathlib has for arbitrary substitutions, not for the translation operator).

Concluded: found building blocks (`MvPolynomial.comp_aeval_apply`, `MvPolynomial.comp_aeval`, `MvPolynomial.bind₁_comp_bind₁`); the translation form is not in mathlib because the operator itself is not.

### Normal-form check — `MvPolynomial.taylor_taylor`

Equivalent formalisms this statement could take: `taylor α (taylor β P) = taylor (fun j ↦ α j + β j) P` (current); `taylor α (taylor β P) = taylor (α + β) P` (Pi addition); `(taylor α).comp (taylor β) = taylor (α + β)` (AlgHom).
Does mathlib already have a canonical form for this idea? yes: `Polynomial.taylor_taylor : taylor r (taylor s f) = taylor (r + s) f` — nested application on the LHS, single translation by the sum (outer shift first) on the RHS.
Our statement is stated against the canonical form? yes for orientation and argument order (`α` outer, sum `α + β`); the RHS spells the sum as a lambda instead of `α + β`.
RHS convention respected? yes (collapses two translations into one).

### Syntactic generality — `MvPolynomial.taylor_taylor`

Alternative restatements attempted:
- current lambda RHS
- Pi-addition RHS `taylor (α + β) P` (evidence item 4: compiles by the term `taylor_taylor α β P`, so definitionally identical)
- AlgHom composition `(taylor α).comp (taylor β) = taylor (α + β)` (item 5)
Chosen restatement: Pi-addition RHS as the primary lemma, plus the AlgHom companion `taylor_comp_taylor`.
Justification: `α + β` is how mathlib writes sums of functions (it rewrites with `Pi.add_apply`, matches `Polynomial.taylor_taylor`'s `r + s`, and lets `taylor_neg_taylor` be stated as `taylor (-α)` with `neg_add_cancel`, as in the univariate `taylor_eval_sub` proof at Polynomial/Taylor.lean:210); the lambda form forces users to eta-expand. The same change applies to `taylor_zero` (`taylor 0 P = P`) and `eval_taylor` (`x + α`) in the same PR.

### Superfluous-argument audit — `MvPolynomial.taylor_taylor`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `α`, `β`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (RHS `taylor (α + β) P`; add `taylor_comp_taylor`)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (cosmetic, definitionally equal)

### Call sites — `MvPolynomial.taylor_taylor`

Internal use count: 0  (outside the declaring file); 1 inside Roth/Taylor.lean
External-to-file callers: 0 distinct files (indirect consumers via `taylor_injective` / `taylor_eq_zero_iff`: Roth/Index.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Taylor.lean:184 | `simp [taylor_taylor]` (proof of `taylor_neg_taylor`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `MvPolynomial.taylor_taylor`?):
  - (none) — `grep -rn "comp_aeval" Roth/` finds only `taylor_taylor` and `taylor_rename` (Roth/Taylor.lean:147, 165), the latter a different statement (renaming).

### Composition check (Phase 6)

Can `MvPolynomial.taylor_taylor` be derived from mathlib in ≤3 chained calls?

Attempt 1: in mathlib-only spelling (unfolded `taylor`), `rw [comp_aeval_apply]; simp [add_assoc]` (evidence item 3).
  - Mathlib decls used: `MvPolynomial.comp_aeval_apply`, `aeval_X`, `algHom_C`, `C_add`, `add_assoc` (simp set).
  - Result: succeeds, but it is a `rw` + `simp` proof, not a call chain, and needs the operator `taylor` (absent from mathlib) to even state the lemma.
  - Notes: plain `simp` does not prove the project form (item 2).

Attempt 2: `bind₁_comp_bind₁` (taylor is `bind₁ (X + C α)` by rfl, parent evidence).
  - Result: partial — gives `bind₁ (fun i ↦ bind₁ g (X i + C (β i)))`, still requiring a simp step to reach `X i + C (α i + β i)`.

Conclusion: NOT-COMPOSABLE (the operator is new; with it, this is the operator's group law, exactly as `Polynomial.taylor_taylor` is for the univariate operator)

## Verdict: `MvPolynomial.taylor_taylor`

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): translations `X + v` form a subgroup of polynomial automorphisms isomorphic to `(R^n, +)` (arXiv 0707.3151, 2303.12324); shift operators compose additively (`T_a T_b = T_{a+b}`, Wikipedia "Shift operator", Taylor-shift literature).
- Generality analysis (Phase 4): MAXIMALLY GENERAL (no hypotheses; `CommSemiring` forced); Phase 4c: no modernisation required (bundled forms are optional companions).
- Mathlib search (Phase 5): not in mathlib; template `Polynomial.taylor_taylor`; building blocks `comp_aeval_apply`, `bind₁_comp_bind₁`.
- Composition check (Phase 6): NOT-COMPOSABLE (operator absent from mathlib; plain `simp` does not close it).

**Rationale:**

The parent `MvPolynomial.taylor` was assessed YES-add-as-is with `taylor_taylor` in its planned upstream file. The composition law is the basic structural fact about translations (they form an action of `(R^σ, +)`), and mathlib's univariate `Polynomial.taylor` carries the exact analogue, which mathlib itself consumes (FieldTheory/Laurent.lean:44 and 103 for Laurent-shift arithmetic, and Polynomial/Taylor.lean:210 to invert translation via `taylor (-r)`). The project uses it in precisely that last role: `taylor_neg_taylor` (translation by `-α` inverts translation by `α`) and thence `taylor_injective`, which the index API in Roth/Index.lean relies on. Without this lemma, any consumer of `MvPolynomial.taylor` would re-derive it through `comp_aeval_apply` plus a simp step.

The statement admits no weakening: it has no hypotheses and its only typeclass is forced by `MvPolynomial`. The only change before shipping is cosmetic: write the RHS as `taylor (α + β) P`, which is definitionally the current statement (evidence item 4), and matches `Polynomial.taylor_taylor`'s `r + s`. The AlgHom companion `taylor_comp_taylor` is worth adding alongside. Neither is a generalisation, so the bucket is YES-add-as-is rather than generalise-first.

WHY add it:
  - New content for mathlib: the group law of multivariate translations. Mathlib has the univariate `Polynomial.taylor_taylor` and general substitution composition (`comp_aeval`, `bind₁_comp_bind₁`), but no translation operator on `MvPolynomial` and hence no such law. The named gap is the missing multivariate counterpart of `Mathlib/Algebra/Polynomial/Taylor.lean`.
  - Composes with: `taylor_zero` to give invertibility over rings (the multivariate `taylorEquiv` analogue, `taylor_injective`), and with `comp_aeval_apply` / `AlgHom.ext` arguments through the bundled companion.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/Taylor.lean (new file, with the parent `MvPolynomial.taylor`).
Proposed PR title: "feat(Algebra/MvPolynomial): add multivariate Taylor shift MvPolynomial.taylor" (lemma included in the parent PR).
PR grouping: ship with `MvPolynomial.taylor`, `taylor_X`, `taylor_C`, `taylor_monomial`, `coeff_taylor`, `aeval_taylor`/`eval_taylor`, `taylor_zero`, `taylor_map`, `taylor_rename`, `degreeOf_taylor_le`, `taylor_neg_taylor`, `taylor_injective` as one PR.
Restatement to apply before the PR (from Phase 5.5):
```lean
theorem taylor_taylor (α β : σ → R) (P : MvPolynomial σ R) :
    taylor α (taylor β P) = taylor (α + β) P := by
  simp [taylor, comp_aeval_apply, add_assoc]

theorem taylor_comp_taylor (α β : σ → R) :
    (taylor α).comp (taylor β) = taylor (α + β) :=
  AlgHom.ext fun P ↦ taylor_taylor α β P
```
Pre-PR checklist before opening:
  - [ ] `/generalise MvPolynomial.taylor_taylor` — confirm no easy further weakening (none expected)
  - [ ] `/cleanup Roth/Taylor.lean MvPolynomial.taylor_taylor` — full audit; switch to Pi-addition RHS consistently across `taylor_zero`, `eval_taylor`, `taylor_neg_taylor`
  - [ ] Pick a mathlib reviewer from recent `Mathlib/Algebra/MvPolynomial/` and `Mathlib/Algebra/Polynomial/Taylor.lean` commits

---

## Next step

Include `taylor_taylor` in the `MvPolynomial.taylor` upstream PR (new Mathlib/Algebra/MvPolynomial/Taylor.lean) with RHS `taylor (α + β) P` and the companion `taylor_comp_taylor`; locally no change is required (the single call site Roth/Taylor.lean:184 works with either RHS spelling).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.taylor_taylor/variants.lean` (compiles with `lake env lean`, no errors or warnings): (1) project statement re-proved by the project proof; (2) `fail_if_success simp` confirms plain `simp` cannot prove it; (3) mathlib-only composition on the unfolded statement, `rw [comp_aeval_apply]; simp [add_assoc]`; (4) Pi-addition form `taylor (α + β) P` proved by the term `taylor_taylor α β P` (definitionally equal); (5) bundled `taylor_comp_taylor : (taylor α).comp (taylor β) = taylor (α + β)` via `AlgHom.ext`; (6) monoid-hom packaging `taylorHom : Multiplicative (σ → R) →* (MvPolynomial σ R →ₐ[R] MvPolynomial σ R)` compiles from (5) and `taylor_zero`.
- First compile of the evidence file failed in item (6) (`by simpa using taylor_zero P` collapsed the goal to `True`); replaced by the term `taylor_zero P`, final file compiles clean.
- Loogle `MvPolynomial.aeval _ (MvPolynomial.aeval _ _)`: only `aeval_sumElim`. LeanSearch / Lean-Finder: as recorded in [A]/[C]. Mathlib grep: `taylor_taylor` only univariate (Algebra/Polynomial/Taylor.lean:157) with consumers FieldTheory/Laurent.lean:44, 103 and Polynomial/Taylor.lean:210. `lean_local_search` unavailable (ripgrep not installed); replaced by grep.
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn taylor_taylor Roth/` (declaration and Roth/Taylor.lean:184); `grep -rn comp_aeval Roth/`; grep of `.mathlib-quality/references/clean.tex` for translation (l.547, 600–629).
