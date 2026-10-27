---
decl: Roth.degreeOf_coeffNone_le
file: Roth/Separation.lean
line: 114
kind: theorem
visibility: public
verdict: YES-add-as-is
cost: CHEAP
junk: REPLACE
rationale: Re-aimed at optionEquivLeft it is the missing mathlib lemma degreeOf_coeff_optionEquivLeft (degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p), the absent twin of the existing degreeOf_coeff_finSuccEquiv and of totalDegree_coeff_optionEquivLeft_le; verified absent (namespace clash test) and proved in 2 lines over any CommSemiring.
action: Upstream `MvPolynomial.degreeOf_coeff_optionEquivLeft (p) (j) (i)` to Mathlib/Algebra/MvPolynomial/Equiv.lean right after totalDegree_coeff_optionEquivLeft_le (section optionEquivLeft); locally the project lemma has no callers, so delete it (or make it `degreeOf_coeff_optionEquivLeft P j ν` until the PR lands).
---

# Roth.degreeOf_coeffNone_le

## Inventory entry

### `theorem Roth.degreeOf_coeffNone_le`
- **Type**: `∀ {τ R : Type*} [CommSemiring R] (P : MvPolynomial (Option τ) R) (ν : ℕ) (j : τ), degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P` (section `[Fintype τ] [DecidableEq τ]` omitted via `omit ... in`)
- **What**: Taking the coefficient of `x_none^ν` (as a polynomial in the remaining variables `τ`) does not increase the degree in any remaining variable `x_j`.
- **How**: `degreeOf_le_iff` reduces to monomials `d` in the support of `coeffNone P ν`; `mem_support_coeff_optionEquivLeft` turns `d` into `d.optionElim ν ∈ P.support`; `monomial_le_degreeOf (some j)` plus `simpa` (`Finsupp.optionElim` at `some j` is `d j`) closes it. Relies on `coeffNone` unfolding definitionally to `(optionEquivLeft R τ P).coeff ν`.
- **Hypotheses**: none beyond `[CommSemiring R]`.
- **Uses from project**: `Roth.coeffNone`
- **Used by**: unused in project (grep of `Roth/` and `Roth.lean` finds only the declaration at Roth/Separation.lean:114)
- **Visibility**: public
- **Lines**: 111–116, proof length 2 lines
- **Notes**: Source-cited (§2, Lemma 2, "the ψ_ν's of degree at most r_j in x_j") but the formal proof of `exists_separated_representation` never needs it. It is exactly mathlib's spelling after unfolding `coeffNone` (evidence (2),(3)).

## Junk check (Step 8)
- Used anywhere? No. Zero call sites in the project.
- Wrapper of 1–2 mathlib calls? Short proof (`degreeOf_le_iff` + `mem_support_coeff_optionEquivLeft` + `monomial_le_degreeOf`), but the statement itself is not in mathlib.
- Does mathlib have it? No. Mathlib has the `finSuccEquiv` twin `degreeOf_coeff_finSuccEquiv` (Equiv.lean:834) and the `totalDegree` twin `totalDegree_coeff_optionEquivLeft_le` (Equiv.lean:597), but no `degreeOf` bound for `optionEquivLeft` coefficients (Phase 5).
- Too specific (inline)? Locally it is dead code. As a mathlib lemma about `optionEquivLeft` it is the natural basic API.
- Well-chosen? Statement is right, but it is spelled with the project abbreviation `coeffNone` rather than mathlib's `(optionEquivLeft R σ p).coeff i`.
- Conclusion: `REPLACE` — upstream as `MvPolynomial.degreeOf_coeff_optionEquivLeft`; the project copy (no callers) can then be deleted.

## Mathlibable assessment (Step 9)

Pre-filter: not private; not `_aux`; docstring not internal/auxiliary; Step 8 = REPLACE (not REMOVE); qualified name `Roth.degreeOf_coeffNone_le` absent from mathlib. Not a glue lemma (real support argument). Parent `Roth.coeffNone` is `NO-composable-from-mathlib` (it is rfl to `(optionEquivLeft R τ P).coeff ν`), and its report directs the re-aim: this lemma is assessed in the re-aimed form `degreeOf_coeff_optionEquivLeft`. Full workflow run on that form.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles with no errors)
- decl `Roth.degreeOf_coeffNone_le`: resolved at Roth/Separation.lean:114
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.degreeOf_coeffNone_le` is a theorem stating the following:

Let `R` be a commutative semiring and `P ∈ R[x_τ, x_∗]`. Write `P = ∑_ν φ_ν(x_τ) x_∗^ν` via `R[x_τ, x_∗] ≅ R[x_τ][x_∗]`. Then for every `j ∈ τ` and every `ν`, `deg_{x_j} φ_ν ≤ deg_{x_j} P`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the remaining variables; `none` is the distinguished one.
- `R : Type*`, `[CommSemiring R]` — coefficients.
- `P : MvPolynomial (Option τ) R`, `ν : ℕ` (power of `x_∗`), `j : τ` (variable whose degree is measured).

Hypotheses (Lean side):
- none.

Conclusion (math): the coefficients of `P` in `x_∗` have `x_j`-degree at most that of `P`.

Conclusion (Lean): `degreeOf j (coeffNone P ν) ≤ degreeOf (some j) P`, i.e. by rfl `degreeOf j ((optionEquivLeft R τ P).coeff ν) ≤ degreeOf (some j) P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic degree-bound API lemma for an existing mathlib equivalence; not a structure or main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 2
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (theorem; check skipped)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | degree in x_j of coefficient of x_n^k multivariate polynomial bounded by degree in x_j | partial | the bound is used inline in arguments (e.g. arXiv 2109.14052 degree counting), definitions of j-degree (Authorea lecture notes) | treated as immediate from the monomial definition; no named theorem |
| 2 | WebSearch (general form) | R[x_1..x_n] = R[x_1..x_{n-1}][x_n] partial degree of coefficients degree in each variable | partial | iterated ring `R[x_1..x_n] = R[x_1..x_{n-1}][x_n]` (Encyclopedia of Mathematics "Ring of polynomials", hackmd notes, arXiv 2508.13165) | partial degree = max exponent over monomials; coefficient bound is folklore |
| 3 | WebSearch (aliases / mathlib) | Mathlib degreeOf_coeff_finSuccEquiv optionEquivLeft degreeOf coeff | yes | mathlib commit adding `finSuccEquiv` API "degree_of of coefficients"; `finSuccEquiv_coeff_coeff`, `totalDegree_coeff_finSuccEquiv_add_le` | the `finSuccEquiv` version exists; no `optionEquivLeft` version found |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "degree at most r_j" | yes | line 374: "the ψ_ν's of degree at most r_j in x_j" | source uses the bound implicitly in Lemma 2 |
| 6 | nLab | polynomial ring | no | grading/multidegree only | no per-variable coefficient-degree statement |
| 7 | nCatLab | n/a | n/a | — | not a categorical concept (an elementwise degree inequality) |
| 8 | Stacks Project | n/a | n/a | — | basic commutative algebra; Stacks has no per-variable degree API to compare |
| 9 | MathOverflow / Math.SE | (covered by #1/#2) | no | — | too elementary to be discussed as a result |
| 10 | recent arXiv | covered by #1 (2109.14052) and #2 (2508.13165) | partial | inline use only | confirms folklore status |

### Literature summary (Phase 3)

Concept identified as: partial (per-variable) degree of the coefficients of a polynomial viewed in `R[x'][x_n]`.
Sources agree on the standard form: yes. It is folklore, immediate from "each monomial of `φ_ν` comes from a monomial of `P` with the same `x_j` exponent".
Most general standard form: any commutative (semi)ring `R`, any variable set, any split-off variable: `deg_{x_j} coeff_ν(P) ≤ deg_{x_j} P`.
Generality dimensions where the literature varies:
  - split-off block: one variable (`Option`, `Fin (n+1)`) or a block (`Sum`); one variable is the case with an existing mathlib sibling.
  - coefficient ring: commutative semiring is already most general for `MvPolynomial`.
Disagreement with the literature: none.

### Generality analysis — `Roth.degreeOf_coeffNone_le`

Literature-standard form (from Phase 3): `degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p` for `[CommSemiring R]`, arbitrary `σ`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | `MvPolynomial`, `degreeOf`, `optionEquivLeft` all require it |
| 2 | `τ : Type*` | arbitrary | arbitrary | no | section `Fintype`/`DecidableEq` already omitted |
| 3 | spelling `coeffNone P ν` | project abbreviation | `(optionEquivLeft R σ p).coeff i` | n/a (same statement) | re-aim to mathlib's spelling, verified by rfl (evidence (2),(3)) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement (if STRICTLY NARROWER): n/a (only the re-aimed spelling, which is the same statement; compiled in evidence (1))
Cost of restatement: CHEAP — mechanical

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no bundled hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | no | already about the iso `optionEquivLeft` | — |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | no | already `CommSemiring` | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | no | `ℕ` exponent intrinsic to `Polynomial.coeff` | — |
| 8 | Concrete-via-abstract? | no | the proof is about `optionEquivLeft` support only; the named `coeffNone` disappears by rfl, which is precisely the re-aim | — |
| 9 | False-generalisation guard | no | the re-aimed form is the same mathematical object (rfl) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the only change is spelling `coeffNone` as mathlib's `(optionEquivLeft R σ p).coeff i`, the same statement; no reformulation beyond that.

### Proof strategy — `Roth.degreeOf_coeffNone_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (it IS the missing helper) | the lemma itself is the gap; its proof uses only existing `degreeOf_le_iff`, `mem_support_coeff_optionEquivLeft`, `monomial_le_degreeOf` | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
  - The 2-line support proof is shorter than mathlib's own `degreeOf_coeff_finSuccEquiv` proof (which goes through `degreeOf_eq_sup`/`Finset.sup_le_iff`/`Finsupp.cons_succ`).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.degreeOf_coeffNone_le`

[A] Lean-Finder       "degree in a variable of a coefficient of a multivariate polynomial viewed as a polynomial in one distinguished variable is at most the degree of the original polynomial in that variable"   hits: `monomial_le_degreeOf`, `degreeOf_le_iff`, `degreeOf_le_totalDegree`, `totalDegree_coeff_finSuccEquiv_add_le`; no optionEquivLeft degreeOf bound
[B] Loogle            `MvPolynomial.degreeOf, MvPolynomial.optionEquivLeft`   hits: only `natDegree_optionEquivLeft`, `degree_optionEquivLeft`, `degreeOf_eq_natDegree` (all about `degreeOf none`, not about coefficients)
[C] LeanSearch        "degreeOf j of coeff of optionEquivLeft p is at most degreeOf (some j) p"   hits: `totalDegree_coeff_optionEquivLeft_le` (totalDegree twin), `optionEquivLeft_coeff_coeff`, `natDegree_optionEquivLeft`, `degreeOf_eq_natDegree`; no degreeOf twin
[D] Grep mathlib src  `degreeOf_coeff`, `optionEquivLeft` with `degreeOf`   only `degreeOf_coeff_finSuccEquiv` (Algebra/MvPolynomial/Equiv.lean:834, used at RingTheory/Spectrum/Prime/ChevalleyComplexity.lean:732); no optionEquivLeft analogue
[E] Name pattern      `lean_local_search` unavailable (ripgrep not installed); replaced by declaring `MvPolynomial.degreeOf_coeff_optionEquivLeft` inside `namespace MvPolynomial` in the evidence file: elaborates with no clash, so the name is free (evidence (1))

Searched for both:
  - the user's current form (`degreeOf j (coeffNone P ν)`): absent (project def).
  - the literature-standard / re-aimed form (`degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p`): absent; siblings present for `finSuccEquiv` (degreeOf) and for `optionEquivLeft` (totalDegree).

Concluded: not in mathlib (all 5 methods exhausted, plus the re-aimed form); building blocks exist but the statement is a genuine API gap.

### Normal-form check — `Roth.degreeOf_coeffNone_le`

Equivalent formalisms: (a) `degreeOf j (coeffNone P ν)`; (b) `degreeOf j ((optionEquivLeft R σ p).coeff i)` (mathlib spelling); (c) `∀ m ∈ ((optionEquivLeft R σ p).coeff i).support, m j ≤ degreeOf (some j) p` (via `degreeOf_le_iff`).
Does mathlib already have a canonical form for this idea? yes for the spelling: mathlib's `optionEquivLeft` API (`totalDegree_coeff_optionEquivLeft_le`, `mem_support_coeff_optionEquivLeft`) uses (b); and `degreeOf_coeff_finSuccEquiv` fixes the shape `degreeOf j (coeff ...) ≤ degreeOf (embed j) p`.
Is our statement stated against the canonical form? Not syntactically (uses `coeffNone`); REFACTOR to (b).
RHS convention respected? n/a (inequality).

### Syntactic generality — `Roth.degreeOf_coeffNone_le`

Alternative restatements attempted:
- (b) with argument order `(p j i)` matching `degreeOf_coeff_finSuccEquiv (p) (j) (i)`: compiles (evidence (1)).
- a sup-equality `degreeOf (some j) p = (optionEquivLeft R σ p).support.sup fun i ↦ degreeOf j (coeff i)`: stronger, but not needed and not the shape of the existing sibling; left as an optional follow-up.

Chosen restatement: `theorem degreeOf_coeff_optionEquivLeft (p : MvPolynomial (Option σ) R) (j : σ) (i : ℕ) : degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p`.
Justification: matches the `finSuccEquiv` twin's name, argument order and shape, and is used with `.trans` exactly as `degreeOf_coeff_finSuccEquiv` is at ChevalleyComplexity.lean:732.

### Superfluous-argument audit — `Roth.degreeOf_coeffNone_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial` / `optionEquivLeft` |
| 2 | `[Fintype τ] [DecidableEq τ]` | no | already omitted (`omit ... in`) |
| 3 | `P`, `ν`, `j` | yes | all appear in the conclusion |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (state against `(optionEquivLeft R σ p).coeff i`, not `coeffNone`)
Syntactic generality: RESTATE (`degreeOf_coeff_optionEquivLeft (p) (j) (i)`, finSuccEquiv-twin order)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP (spelling only; same statement by rfl)

### Call sites — `Roth.degreeOf_coeffNone_le`

Internal use count: 0 (also 0 inside the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| (none) | grep of `Roth/` and `Roth.lean` finds only the declaration Roth/Separation.lean:114 |

Inline-derivation grep (was the equivalent re-derived elsewhere without using it?):
  - (none) — no other project proof bounds `degreeOf` of `coeffNone`/`optionEquivLeft` coefficients. In mathlib, the analogous inline need is served by `degreeOf_coeff_finSuccEquiv` (ChevalleyComplexity.lean:732), showing downstream demand for this lemma shape.

### Composition check (Phase 6)

Can `Roth.degreeOf_coeffNone_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `degreeOf_le_iff.2 fun d hd ↦ by simpa using monomial_le_degreeOf (some j) ((mem_support_coeff_optionEquivLeft R).1 hd)`
  - Mathlib decls used: `MvPolynomial.degreeOf_le_iff`, `MvPolynomial.mem_support_coeff_optionEquivLeft`, `MvPolynomial.monomial_le_degreeOf`, plus a `simpa` step (`Finsupp.optionElim` at `some j`).
  - Result: partial — it works, but it is a small proof (intro of a support element + a simp normalisation), not a `.trans`/application chain. Per the heuristics, a `simpa`-closed binder argument is a proof, not a composition.
  - Notes: the same shape as mathlib's stand-alone `degreeOf_coeff_finSuccEquiv` and `totalDegree_coeff_optionEquivLeft_le`, which mathlib ships as named lemmas.

Attempt 2: transport from `degreeOf_coeff_finSuccEquiv` — fails: `finSuccEquiv` needs `Fin (n+1)` variables; for arbitrary `σ` there is no chain.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.degreeOf_coeffNone_le`

Verdict: YES-add-as-is (in the re-aimed spelling)

**Category:** YES-add-as-is

**Evidence:**
- Literature search (Phase 3): folklore per-variable degree bound for coefficients in `R[x'][x_n]`; standard over any commutative semiring.
- Generality analysis (Phase 4): MAXIMALLY GENERAL; re-aimed spelling compiles (evidence (1)).
- Mathlib search (Phase 5): not in mathlib; siblings `degreeOf_coeff_finSuccEquiv` and `totalDegree_coeff_optionEquivLeft_le` exist; name `MvPolynomial.degreeOf_coeff_optionEquivLeft` free.
- Composition check (Phase 6): NOT-COMPOSABLE (a short proof, as with its mathlib siblings).

**Rationale:**
Mathlib's `optionEquivLeft` section in Mathlib/Algebra/MvPolynomial/Equiv.lean has coefficient, support, `natDegree`, `degree` and `totalDegree` API for the coefficients `(optionEquivLeft R σ p).coeff i`. It has no per-variable `degreeOf` bound. The `finSuccEquiv` section does have one (`degreeOf_coeff_finSuccEquiv`, Equiv.lean:834), and mathlib uses it downstream (ChevalleyComplexity.lean:732). The `optionEquivLeft` version is the more general one, because it works for an arbitrary variable type `σ` and not just `Fin n`. So the gap is concrete: a twin of an existing lemma is missing from a parallel API, and the `totalDegree` row of that same parallel API is already filled by `totalDegree_coeff_optionEquivLeft_le`.

The project statement is the same statement, written with the project abbreviation `coeffNone` (rfl, evidence (2),(3)). The mathlib form is `degreeOf_coeff_optionEquivLeft (p) (j) (i)`. It compiles with a 2-line proof over any `CommSemiring`, using only existing lemmas (evidence (1)). Locally the lemma has zero callers, so after upstreaming, the project copy can simply be deleted.

WHY add it:
- New content: the per-variable degree bound `deg_{x_j} coeff_i(p) ≤ deg_{x_j} p` for `optionEquivLeft`. Users currently re-derive it by a support argument each time.
- Specific gap: it is the missing `optionEquivLeft` twin of `degreeOf_coeff_finSuccEquiv`, and the missing `degreeOf` companion of `totalDegree_coeff_optionEquivLeft_le`.
- Composition: it composes with `natDegree_optionEquivLeft` / `degreeOf_eq_natDegree` (degree bookkeeping when splitting off one variable). A follow-up could also golf `degreeOf_coeff_finSuccEquiv` through it, since `finSuccEquiv` factors through `optionEquivLeft`. That golf is not verified here.

Proposed mathlib location:    Mathlib/Algebra/MvPolynomial/Equiv.lean, section `optionEquivLeft`, after `totalDegree_coeff_optionEquivLeft_le`
Proposed PR title:            "feat(Algebra/MvPolynomial/Equiv): add `degreeOf_coeff_optionEquivLeft`"
PR grouping (if applicable):  standalone (no other project decl with a related YES verdict in this file; `coeffNone`, `coeff_coeffNone` and `eq_sum_X_none_pow_mul_coeffNone` are NO verdicts)
Proposed statement:
```lean
theorem degreeOf_coeff_optionEquivLeft (p : MvPolynomial (Option σ) R) (j : σ) (i : ℕ) :
    degreeOf j ((optionEquivLeft R σ p).coeff i) ≤ degreeOf (some j) p := by
  refine degreeOf_le_iff.2 fun d hd ↦ ?_
  simpa using monomial_le_degreeOf (some j) ((mem_support_coeff_optionEquivLeft R).1 hd)
```
Pre-PR checklist before opening:
  - [ ] `/generalise` — none expected (already CommSemiring, arbitrary σ)
  - [ ] `/cleanup` the snippet against mathlib style (docstring, variable naming `p`, `j`, `i`)
  - [ ] Pick a reviewer from recent commits to Mathlib/Algebra/MvPolynomial/Equiv.lean
Next action: open the mathlib PR with the statement above; in the project, delete `Roth.degreeOf_coeffNone_le` (Roth/Separation.lean:111–116; no call sites), or keep it as `degreeOf_coeff_optionEquivLeft P j ν` until the PR lands.

---

## Next step

Upstream `MvPolynomial.degreeOf_coeff_optionEquivLeft` (statement and 2-line proof above) to Mathlib/Algebra/MvPolynomial/Equiv.lean next to `totalDegree_coeff_optionEquivLeft_le`; delete the unused project lemma at Roth/Separation.lean:114.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.degreeOf_coeffNone_le/reaim.lean` (imports `Roth.Separation`). One `lake env lean` run (~38 s) produced no errors, only the two `#check` outputs. Checks: (1) `MvPolynomial.degreeOf_coeff_optionEquivLeft` declared inside `namespace MvPolynomial` elaborates with no name clash, and its 2-line proof compiles over `[CommSemiring R]` with arbitrary `σ`; (2) the project statement follows as `degreeOf_coeff_optionEquivLeft P j ν`; (3) the re-aimed statement follows as `Roth.degreeOf_coeffNone_le p i j`, so the two forms are the same statement; (4) `#check` of the siblings `totalDegree_coeff_optionEquivLeft_le` and `degreeOf_coeff_finSuccEquiv`.
- Searches: 3 WebSearch queries; LeanSearch, Loogle and Lean-Finder queries; and a mathlib grep for `degreeOf_coeff` and for `optionEquivLeft` with `degreeOf`, all recorded above. `lean_local_search` was unavailable because ripgrep is not installed, so the namespace-clash compile check replaced it. ChatGPT MCP was n/a (not configured in this session).
- Project-wide grep for `degreeOf_coeffNone_le` in `Roth/`: the declaration only, with no callers.
