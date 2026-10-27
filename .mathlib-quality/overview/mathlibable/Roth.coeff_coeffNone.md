---
decl: Roth.coeff_coeffNone
file: Roth/Separation.lean
line: 85
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: REPLACE
rationale: After unfolding coeffNone (rfl) this is MvPolynomial.optionEquivLeft_coeff_coeff with the multi-index spelled d.mapDomain some + single none ν instead of mathlib's canonical d.optionElim ν; both call sites are served directly by mathlib lemmas.
action: At Roth/Separation.lean:107 use `exact optionEquivLeft_coeff_some_coeff_none R τ e P` (after unfolding) and at :129 restate coeff_rename_mul_aeval with `a.optionElim b` and rewrite with `← optionEquivLeft_coeff_coeff`; then delete coeff_coeffNone (or keep it as the one-line `optionEquivLeft_coeff_coeff R P ν d` stated with optionElim); no mathlib PR.
---

# Roth.coeff_coeffNone

## Inventory entry

### `theorem Roth.coeff_coeffNone`
- **Type**: `{τ : Type*} {R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) : (coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν)` (section `[Fintype τ] [DecidableEq τ]` omitted via `omit ... in`; confirmed by `#check`, evidence (0))
- **What**: The coefficient of `x_τ^d` in the `x_none^ν`-coefficient of `P` is the coefficient of `x_τ^d x_none^ν` in `P`.
- **How**: `rw [coeffNone, optionEquivLeft_coeff_coeff]`, then `congr 1; ext o; cases o <;> simp [Finsupp.mapDomain_of_notMem_range, Finsupp.mapDomain_apply_of_injective (Option.some_injective τ)]` to identify `d.optionElim ν` with `d.mapDomain some + single none ν`.
- **Hypotheses**: `[CommSemiring R]` only.
- **Uses from project**: `Roth.coeffNone`
- **Used by**: `Roth.eq_sum_X_none_pow_mul_coeffNone` (Roth/Separation.lean:107, `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]`), `Roth.coeff_rename_mul_aeval` (Roth/Separation.lean:129, `rw [← coeff_coeffNone, coeffNone, ...]`). No uses outside Separation.lean (`grep -rn coeff_coeffNone Roth/`).
- **Visibility**: public
- **Lines**: 84–91, proof length 5 lines
- **Notes**: The only content beyond mathlib is the Finsupp identity `d.mapDomain some + single none ν = d.optionElim ν`, which mathlib does not state but which is not needed if the canonical `optionElim` spelling is used (evidence (2)).

## Junk check (Step 8)
- Used anywhere? Yes, 2 call sites (Separation.lean:107, 129).
- Wrapper of 1–2 mathlib calls? Yes: `optionEquivLeft_coeff_coeff` plus a spelling conversion of the multi-index.
- Does mathlib have it? Yes, `MvPolynomial.optionEquivLeft_coeff_coeff` (Mathlib/Algebra/MvPolynomial/Equiv.lean:610) is the same statement with `d.optionElim ν` (evidence (1), proof term is the mathlib lemma itself).
- Too specific? The non-canonical RHS forces the project to also carry `eq_mapDomain_some_add_single` (already assessed REPLACE) to reconnect with mathlib.
- Well-chosen? No: the RHS spelling is the non-canonical one.
- Conclusion: `REPLACE` — use `optionEquivLeft_coeff_some_coeff_none` at :107 (evidence (4)) and the `optionElim` spelling with `optionEquivLeft_coeff_coeff` at :129.

## Mathlibable assessment (Step 9)

Pre-filter: not private; not `_aux`; docstring not internal/auxiliary; Step 8 = REPLACE (not REMOVE); qualified name `Roth.coeff_coeffNone` absent from mathlib (no `coeffNone` anywhere in `.lake/packages/mathlib/Mathlib/`). Not a pure glue lemma (5-line proof, not `rfl`), so the parent `Roth.coeffNone` (NO-composable-from-mathlib) is not blanket-inherited. Per the orchestrator's instruction the re-aim rule is applied: `coeffNone P ν` is rfl-equal to `(optionEquivLeft R τ P).coeff ν`, and the re-aimed lemma about `optionEquivLeft` exists in mathlib. Full workflow run below, re-aimed at `optionEquivLeft`.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles)
- decl `Roth.coeff_coeffNone`: resolved at Roth/Separation.lean:85
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.coeff_coeffNone` is a theorem stating the following: let `P ∈ R[x_τ, x_∗]` and write `P = ∑_ν φ_ν(x_τ) x_∗^ν` via `R[x_τ, x_∗] ≅ R[x_τ][x_∗]`. Then for every multi-index `d` on `τ`, the coefficient of `x_τ^d` in `φ_ν` equals the coefficient of `x_τ^d x_∗^ν` in `P`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the non-distinguished variables.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `P : MvPolynomial (Option τ) R`, `ν : ℕ`, `d : τ →₀ ℕ`.

Hypotheses (Lean side):
- none.

Conclusion (math): `[x_τ^d] φ_ν = [x_τ^d x_∗^ν] P`.

Conclusion (Lean): `(coeffNone P ν).coeff d = P.coeff (d.mapDomain some + Finsupp.single none ν)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a coefficient-bookkeeping lemma for an unnamed mathlib idiom; not a new structure, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 5
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | coefficient of monomial x^a y^n in multivariate polynomial equals coefficient of x^a in coefficient of y^n R[x][y] | yes | `∑ a_ij x^i y^j ↦ ∑_j (∑_i a_ij x^i) y^j`, so `[x^a y^n] f = [x^a]([y^n] f)` | textbooks (Judson AATA §17.1, UTK IAAWA §5.1) treat it as immediate from the identification `R[x,y] = R[x][y]` |
| 2 | WebSearch (general form) | isomorphism R[X_1..X_n] ≅ R[X_1..X_{n-1}][X_n] coefficients correspondence monomials | yes | monomial basis indexed by `ℕ^n`; iterated construction `R[X_1..X_{n-1}][X_n]` (Encyclopedia of Mathematics "Polynomial ring"; Wikipedia "Monoid ring") | statement is a consequence of the isomorphism, never a named result |
| 3 | WebSearch (aliases / mathlib) | Mathlib MvPolynomial optionEquivLeft_coeff_coeff optionElim | partial | Mathlib.Algebra.MvPolynomial.Equiv docs pages | search index stale; the lemma itself confirmed by channels [A]/[C] in Phase 5 |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "powers of" | yes | line 374: "collecting the terms in terms of the powers of `x_p`" | source uses the coefficient correspondence implicitly |
| 6 | nLab | polynomial ring (from parent assessment `Roth.coeffNone`) | yes | `A[X ⊔ Y] ≅ A[X][Y]` (free commutative algebra preserves coproducts) | only the isomorphism; coefficient bookkeeping not discussed |
| 7 | nCatLab | free commutative algebra | yes | same as #6 | no further content |
| 8 | Stacks Project | n/a | n/a | — | elementary commutative algebra; Stacks has no coefficient-level statement to compare |
| 9 | MathOverflow / Math.SE | (covered by #1/#2; physicsforums "Is R[x,y] isomorphic to R[y,x]?" surfaced) | no | — | too elementary to be discussed as a result |
| 10 | recent arXiv | arXiv 2508.13165 (intro to rings and fields), surfaced by #1/#2 | yes | iterated polynomial ring identification | confirms standard treatment |

### Literature summary (Phase 3)

Concept identified as: coefficient correspondence under `R[x', x_n] ≅ R[x'][x_n]`.
Sources agree on the standard form: yes — `[x'^d x_n^k] P = [x'^d]([x_n^k] P)`, treated as immediate.
Most general standard form: for any variable set `σ`, commutative semiring `R`, `P ∈ R[σ ⊔ {∗}]`: `coeff_d(coeff_k(P)) = coeff_{(d,k)}(P)`.
Generality dimensions where the literature varies:
  - split block size: one variable (`Option`) or a block (`Sum`).
  - coefficient ring: commutative semiring is already most general.
Disagreement with the literature: none mathematically; the Lean spelling of the multi-index `(d,k)` (`mapDomain some + single none`) differs from mathlib's canonical `optionElim`.

### Generality analysis — `Roth.coeff_coeffNone`

Literature-standard form (from Phase 3): `coeff_d((optionEquivLeft R σ P).coeff k) = P.coeff (d.optionElim k)` for `[CommSemiring R]`, arbitrary `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial`, `optionEquivLeft` need it |
| 2 | `τ : Type*` | arbitrary | arbitrary | no | section `Fintype`/`DecidableEq` already omitted (evidence (0)) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement (if STRICTLY NARROWER): n/a
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | already via `optionEquivLeft` | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | no | `ℕ` intrinsic to `Polynomial.coeff` | — |
| 8 | Concrete-via-abstract? | no | proof unfolds `coeffNone` immediately and then is mathlib's lemma; no witness to abstract | — |
| 9 | False-generalisation guard | no | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the mathlib-idiomatic form (`optionElim` multi-index, `optionEquivLeft` coefficient) already exists as `optionEquivLeft_coeff_coeff`.

### Proof strategy — `Roth.coeff_coeffNone`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the conversion `d.mapDomain some + single none ν = d.optionElim ν` (evidence (2)) is only needed because of the non-canonical spelling; with `optionElim` the proof is the mathlib term | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: state with `d.optionElim ν`; proof becomes `optionEquivLeft_coeff_coeff R P ν d` (or drop the lemma).
  - Cost: CHEAP
  - Missing mathlib API (if any): none
  - Would refactoring make the proof strictly shorter / cleaner? yes

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.coeff_coeffNone`

[A] Lean-Finder       "coefficient of x^d y^m in a polynomial over Option σ equals the d coefficient of the y^m coefficient after identifying R[σ ⊔ *] with R[σ][X]"   hit: `MvPolynomial.optionEquivLeft_coeff_coeff` (top), `optionEquivLeft_coeff_some_coeff_none`, `optionEquivLeft_monomial`
[B] Loogle            `Polynomial.coeff (MvPolynomial.optionEquivLeft _ _ _) _, MvPolynomial.coeff`   n/a: query error (identifier `MvPolynomial.coeff` not resolved by loogle's parser); covered by [A], [C], [D]
[C] LeanSearch        "coefficient of d in the m-th coefficient of optionEquivLeft p equals coefficient of p at d extended by m at none"   hit: `MvPolynomial.optionEquivLeft_coeff_coeff` (top), `optionEquivLeft_coeff_some_coeff_none`, `mem_support_coeff_optionEquivLeft`
[D] Grep mathlib src  `optionEquivLeft_coeff`, `optionElim.*mapDomain`, `mapDomain some`   `optionEquivLeft_coeff_coeff` at Mathlib/Algebra/MvPolynomial/Equiv.lean:610, `optionEquivLeft_coeff_some_coeff_none` at :509; no lemma relating `mapDomain some + single none` to `optionElim` (mathlib uses `embDomain .some + .single .none` only inline at :593/:606)
[E] Name pattern      `optionEquivLeft_coeff`, `coeffNone`   n/a for `lean_local_search` (ripgrep not installed in this session); grep [D] covers the name pattern: only the two theorems above

Searched for both:
  - the user's current form (`mapDomain some + single none ν` spelling): no mathlib statement in this spelling.
  - the literature-standard / re-aimed form (`optionElim` spelling on `optionEquivLeft`): present as `MvPolynomial.optionEquivLeft_coeff_coeff`.

Concluded: found in mathlib as `MvPolynomial.optionEquivLeft_coeff_coeff`; identical content, different (canonical) multi-index spelling.

### Normal-form check — `Roth.coeff_coeffNone`

Equivalent formalisms: RHS multi-index as (a) `d.mapDomain some + single none ν`; (b) `d.optionElim ν` (mathlib); (c) `d.embDomain .some + .single .none ν`.
Does mathlib already have a canonical form? yes — (b), in `optionEquivLeft_coeff_coeff` and `mem_support_coeff_optionEquivLeft`.
Is our statement stated against the canonical form? NO → REFACTOR to (b), at which point it is the mathlib lemma.
RHS convention respected? no (non-canonical RHS).

### Syntactic generality — `Roth.coeff_coeffNone`

Alternative restatements attempted:
- `optionElim` spelling: closes by `optionEquivLeft_coeff_coeff R P ν d` (evidence (1)).
- `e : Option τ →₀ ℕ` form `(coeffNone P (e none)).coeff e.some = P.coeff e`: closes by `optionEquivLeft_coeff_some_coeff_none R τ e P` (evidence (4)); this is what call site :107 actually needs.

Chosen restatement: the mathlib lemmas themselves.
Justification: :107 needs the `e`-form, :129 can be phrased with `optionElim`; neither needs the `mapDomain` spelling.

### Superfluous-argument audit — `Roth.coeff_coeffNone`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | needed by `MvPolynomial` |
| 2 | section `[Fintype τ] [DecidableEq τ]` | no | already omitted via `omit ... in` (evidence (0)) |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (target `P.coeff (d.optionElim ν)`)
Syntactic generality: RESTATE (use `optionEquivLeft_coeff_some_coeff_none` at :107)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (the restated form is already in mathlib)

### Call sites — `Roth.coeff_coeffNone`

Internal use count: 0 outside the declaring file; 2 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:107 | `eq_sum_X_none_pow_mul_coeffNone`: `· rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` |
| Roth/Separation.lean:129 | `coeff_rename_mul_aeval`: `rw [← coeff_coeffNone, coeffNone, map_mul, ...]` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `coeff_coeffNone`?):
  - Roth/Separation.lean:57–61 `eq_mapDomain_some_add_single` re-derives the same `mapDomain some + single none` decomposition (the inverse direction of the conversion), only to undo this lemma's spelling at :107.
  - Roth/Separation.lean:64–75 private `coeff_X_none_pow_mul_rename` uses `optionEquivLeft_coeff_some_coeff_none` directly.

### Composition check (Phase 6)

Can `Roth.coeff_coeffNone` be derived from mathlib in ≤3 chained calls?

Attempt 1: `optionEquivLeft_coeff_coeff R P ν d` for the `optionElim`-stated version
  - Mathlib decls used: `MvPolynomial.optionEquivLeft_coeff_coeff`
  - Result: succeeds (evidence (1)), 1 call, no proof.
  - Notes: exact statement needs one Finsupp conversion.

Attempt 2: exact project statement: `by rw [mapDomain_some_add_single_none]; exact optionEquivLeft_coeff_coeff R P ν d`
  - Mathlib decls used: `optionEquivLeft_coeff_coeff`, plus the 3-line Finsupp identity (evidence (2)–(3))
  - Result: succeeds.
  - Notes: the identity is avoidable by changing the spelling.

Conclusion: COMPOSABLE (in fact identical to a mathlib lemma in canonical spelling)

## Verdict: `Roth.coeff_coeffNone`

Verdict: NO-mathlib-has-it

**Category:** NO-mathlib-has-it

**Evidence:**
- Literature search (Phase 3): standard, immediate coefficient correspondence under `R[x', x_n] ≅ R[x'][x_n]`.
- Generality analysis (Phase 4): MAXIMALLY GENERAL.
- Mathlib search (Phase 5): found as `MvPolynomial.optionEquivLeft_coeff_coeff` (Equiv.lean:610), canonical `optionElim` spelling.
- Composition check (Phase 6): COMPOSABLE; re-aimed form is the mathlib term (evidence (1)).

**Rationale:**
Since `coeffNone P ν` is by definition `(optionEquivLeft R τ P).coeff ν`, this lemma says `((optionEquivLeft R τ P).coeff ν).coeff d = P.coeff (d.mapDomain some + single none ν)`. Mathlib's `optionEquivLeft_coeff_coeff` states exactly this with `d.optionElim ν` as the multi-index. The only extra content in the project version is a Finsupp spelling conversion. The conversion is not in mathlib (evidence (2)), but mathlib does not need it, because it uses `optionElim` throughout. This is a re-aim hit: the parent def has no mathlib name, but the lemma about its definitional body already exists.

The non-canonical spelling costs the project a second lemma. `eq_mapDomain_some_add_single` exists only to undo it at :107, where `optionEquivLeft_coeff_some_coeff_none` closes the goal directly (evidence (4)).

WHY not: mathlib already has the statement, as `MvPolynomial.optionEquivLeft_coeff_coeff`, in its canonical spelling.
Belongs-elsewhere check: nowhere. At most keep a project-local alias in the `optionElim` spelling if readability needs `coeffNone`.
Existing mathlib decl:        `MvPolynomial.optionEquivLeft_coeff_coeff`
Located at:                   `Mathlib/Algebra/MvPolynomial/Equiv.lean:610`
Our form follows in ≤1 line:
```lean
example (P : MvPolynomial (Option τ) R) (ν : ℕ) (d : τ →₀ ℕ) :
    (Roth.coeffNone P ν).coeff d = P.coeff (d.optionElim ν) :=
  optionEquivLeft_coeff_coeff R P ν d
```
Call sites in our project (from Phase 6.0): 2
Refactor plan:
- Roth/Separation.lean:107 (`eq_sum_X_none_pow_mul_coeffNone`): replace `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` with `exact optionEquivLeft_coeff_some_coeff_none R τ e P` (the goal is `(coeffNone P (e none)).coeff e.some = P.coeff e`, and `coeffNone` unfolds by rfl; evidence (4)). This also frees `eq_mapDomain_some_add_single` for deletion.
- Roth/Separation.lean:129 (`coeff_rename_mul_aeval`): restate the coefficient index as `a.optionElim b` and start the proof with `rw [← optionEquivLeft_coeff_coeff, map_mul, ...]`. Alternatively, keep the `mapDomain` statement and first rewrite with the conversion from evidence (2). Check this lemma's downstream users before changing its spelling.
Next action: delete `Roth.coeff_coeffNone` after updating the 2 call sites. If keeping it, restate it with `d.optionElim ν` and prove it by `optionEquivLeft_coeff_coeff R P ν d`. No mathlib PR.

---

## Next step

No mathlib PR. Replace the 2 uses (Separation.lean:107 via `optionEquivLeft_coeff_some_coeff_none`, :129 via `optionEquivLeft_coeff_coeff` in the `optionElim` spelling), then delete `coeff_coeffNone` together with `eq_mapDomain_some_add_single`.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.coeff_coeffNone/reaim.lean` (imports `Roth.Separation`). One `lake env lean` run (about 26 s) printed only the `#check` output, with no errors. (0) `#check @Roth.coeff_coeffNone` gives the signature with `[CommSemiring R]` only. (1) The `optionElim`-spelled statement is the term `optionEquivLeft_coeff_coeff R P ν d`. (2) `d.mapDomain some + single none ν = d.optionElim ν` is proved by `ext o; cases o <;> simp [...]` and is absent from mathlib. (3) The exact project statement follows from (2) plus `optionEquivLeft_coeff_coeff`. (4) The :107 goal `(coeffNone P (e none)).coeff e.some = P.coeff e` is the term `optionEquivLeft_coeff_some_coeff_none R τ e P`.
- Searches: 3 WebSearch queries, recorded above. Lean-Finder and LeanSearch both returned `optionEquivLeft_coeff_coeff` as the top hit. The Loogle query hit a parse error. `lean_local_search` was unavailable because ripgrep is missing. A mathlib grep for `optionEquivLeft_coeff`, `optionElim` with `mapDomain`/`embDomain`, and `mapDomain some` found the lemma and no spelling-conversion lemma. ChatGPT MCP was n/a (not configured in this session).
