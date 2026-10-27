---
decl: Roth.eq_mapDomain_some_add_single
file: Roth/Separation.lean
line: 57
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: REPLACE
rationale: The identity d = d.some.mapDomain some + single none (d none) is mathlib's Finsupp.optionElim_some written in a non-canonical spelling, and its single call site is closed outright by MvPolynomial.optionEquivLeft_coeff_some_coeff_none, so no new lemma is needed.
action: At Roth/Separation.lean:107 (eq_sum_X_none_pow_mul_coeffNone) replace `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` with `exact (optionEquivLeft_coeff_some_coeff_none R τ e P).symm` (after unfolding coeffNone), then delete the lemma; optionally restate coeff_coeffNone with `d.optionElim ν` (= MvPolynomial.optionEquivLeft_coeff_coeff); no mathlib PR.
---

# Roth.eq_mapDomain_some_add_single

## Inventory entry

### `theorem Roth.eq_mapDomain_some_add_single`
- **Type**: `{τ : Type*} (d : Option τ →₀ ℕ) : d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none)`
- **What**: Every multi-index on the variable set `Option τ` splits as its restriction to `τ`, pushed back along `some`, plus its `none`-component placed at `none`.
- **How**: `ext o`, then `cases o` and `simp` with `Finsupp.mapDomain_of_notMem_range` (the `none` case), `Finsupp.mapDomain_apply_of_injective (Option.some_injective τ)` and `Finsupp.some_apply` (the `some` case).
- **Hypotheses**: none beyond the type `τ` (the section's `[Fintype τ] [DecidableEq τ]` are omitted).
- **Uses from project**: `[]`
- **Used by**: Roth/Separation.lean:107 (`rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` inside `eq_sum_X_none_pow_mul_coeffNone`). No other uses anywhere in `Roth/`.
- **Visibility**: public
- **Lines**: 55–61, proof length 3 lines
- **Notes**: Holds for any `AddCommMonoid M` in place of `ℕ` (evidence (4)). Mathlib's canonical spelling of the same decomposition is `Finsupp.optionElim_some : f.some.optionElim (f none) = f`.

## Junk check (Step 8)
- Used anywhere? Once, at Separation.lean:107.
- Wrapper of 1–2 mathlib calls? Yes: it is `(Finsupp.optionElim_some d).symm` after the (missing) normalisation `optionElim y f = f.mapDomain some + single none y` (evidence (2), (3)).
- Does mathlib have it? In canonical form yes (`Finsupp.optionElim_some`, Mathlib/Data/Finsupp/Option.lean); the literal `mapDomain + single` spelling no.
- Too specific (inline)? Yes. Its only consumer needs `P.coeff e = (coeffNone P (e none)).coeff e.some`, which is exactly `MvPolynomial.optionEquivLeft_coeff_some_coeff_none` after unfolding `coeffNone` (evidence (5)); the detour through `coeff_coeffNone` + this lemma is unnecessary.
- Well-chosen? No: it encodes mathlib's `optionElim` in an ad-hoc spelling.
- Conclusion: `REPLACE` — action: at Separation.lean:107 close the branch with `(optionEquivLeft_coeff_some_coeff_none R τ e P).symm` (unfolding `coeffNone`), delete this lemma.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said REPLACE (not REMOVE); qualified name `Roth.eq_mapDomain_some_add_single` absent from mathlib (no `namespace Roth`). Not a glue lemma (not `rfl`; no assessed parent def). Full workflow run.

### Baseline (Phase 0)
- lake build:               clean (per brief; evidence file importing `Roth.Separation` compiles with no output)
- decl `Roth.eq_mapDomain_some_add_single`: resolved at Roth/Separation.lean:57
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Separating one variable (`none`) from the rest (`τ`) in polynomials over `Option τ`, towards Lemma 2 of the source (`F = U(x_τ) V(x_none)`).

### Statement (Phase 1)

`Roth.eq_mapDomain_some_add_single` is a theorem stating the following: for a multi-index `d ∈ ℕ^(τ ⊔ {∗})` (finitely supported), write `d' = d|_τ` and `d_∗ = d(∗)`. Then `d = ι_*(d') + d_∗ e_∗`, where `ι : τ → τ ⊔ {∗}` is the inclusion and `e_∗` the basis vector at `∗`. Equivalently, the canonical isomorphism `ℕ^(τ ⊔ {∗}) ≅ ℕ^(τ) × ℕ` composed with its inverse is the identity; monomially, `x^d = x_τ^{d'} x_∗^{d_∗}`.

Variables / typeclasses involved (Lean side):
- `τ : Type*` — the non-distinguished variables.
- `d : Option τ →₀ ℕ` — a multi-index (exponent vector) on `Option τ`.

Hypotheses (Lean side):
- none.

Conclusion (math): `d = ι_*(d|_τ) + d(∗) · e_∗`.

Conclusion (Lean): `d = (Finsupp.some d).mapDomain some + Finsupp.single none (d none)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a bookkeeping identity on exponent vectors; helper for a coefficient computation.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index decomposition x^alpha = x'^alpha' x_n^alpha_n separating last variable polynomial | yes | `x^α = x'^{α'} x_n^{α_n}` (Wikipedia "Multi-index notation"; arXiv 2308.12232 "Last-decomposition") | treated as notation, never a named result |
| 2 | WebSearch (general form) | free commutative monoid on disjoint union coproduct N^(A ⊔ B) ≅ N^A × N^B | yes | `ℕ[A ⊔ B] ≅ ℕ[A] × ℕ[B]` (nLab "free commutative monoid", biproduct in CMon) | the most general form: free functor preserves coproducts; our lemma is the `B = {∗}` case read as `x = (inl ∘ fst) x + (inr ∘ snd) x` |
| 3 | WebSearch (aliases / mathlib) | Mathlib Finsupp.optionElim Finsupp.some Option finitely supported function decomposition | yes | `Finsupp.optionEquiv : (Option α →₀ M) ≃ M × (α →₀ M)`, `optionElim`, `some` (Mathlib.Data.Finsupp.Option docs) | the exact mathlib API for this split |
| 4 | ChatGPT MCP | n/a | n/a | — | n/a: `ask_chatgpt_math` MCP not configured in this session |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "powers of" | yes | line 374: "collecting the terms in terms of the powers of `x_p`" | the source uses the split implicitly; no statement of the identity |
| 6 | nLab | free commutative monoid | yes | `ℕ[S] ≃ ⊕_{s∈S} ℕ`, biproduct in CMon | general form as in #2 |
| 7 | nCatLab | biproduct in CMon | yes | same page as #6 | categorical content is only "coproduct = product in CMon" |
| 8 | Stacks Project | n/a | n/a | — | not an algebraic-geometry concept; exponent-vector bookkeeping |
| 9 | MathOverflow / Math.SE | (covered by #1/#2 results) | no | — | too elementary to be discussed as a result |
| 10 | recent arXiv | "Last-decomposition" multivariate resultant (arXiv 2308.12232, surfaced by #1) | yes | splits monomials by trailing exponents | uses the identity as notation |

### Literature summary (Phase 3)

Concept identified as: splitting an exponent vector along `Option τ = τ ⊔ {∗}`; the free commutative monoid functor preserves coproducts (`ℕ^(A ⊔ B) ≅ ℕ^(A) × ℕ^(B)`).
Sources agree on the standard form: yes — it is universally treated as notation (`x^α = x'^{α'} x_n^{α_n}`), not as a named lemma.
Most general standard form: for any commutative monoid `M`, `(A ⊔ B →₀ M) ≅ (A →₀ M) × (B →₀ M)`, with `f = inl_*(f ∘ inl) + inr_*(f ∘ inr)`.
Generality dimensions where the literature varies:
  - coefficient monoid: `ℕ` to any additive commutative monoid (most general).
  - shape of the split: one extra variable (`Option`) to arbitrary disjoint union (`Sum`).
Disagreement with the literature: none; the project fixes `M = ℕ`, which is narrower than needed.

### Generality analysis — `Roth.eq_mapDomain_some_add_single`

Literature-standard form (from Phase 3): `f = (f.some).mapDomain some + single none (f none)` for `f : Option α →₀ M`, `M` any `AddCommMonoid`; in mathlib's idiom `f = f.some.optionElim (f none)` for any `Zero M`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient type `ℕ` | `Option τ →₀ ℕ` | any `AddCommMonoid M` | yes | proof only uses `mapDomain`/`single` pointwise evaluation; verified (evidence (4)) |
| 2 | `τ : Type*` | arbitrary type | arbitrary type | no | already general |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 1 (`ℕ` to `[AddCommMonoid M]`, verified to compile, evidence (4)).
Proposed restatement (if STRICTLY NARROWER): `theorem Finsupp.eq_mapDomain_some_add_single {M} [AddCommMonoid M] (d : Option α →₀ M) : d = d.some.mapDomain some + single none (d none)` — but this is itself `optionElim_some` in a non-canonical spelling (see 4c / 5.5), so the weakening does not make it mathlib material.
Cost of restatement: CHEAP — mechanical.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles to typeclasses? | no | no bundled hypotheses | — |
| 2 | Sequences to filters? | no | no topology | — |
| 3 | Construction vs universal property? | yes | state via `Finsupp.optionEquiv` / `optionElim` (the universal pairing) instead of `mapDomain + single` | `optionElim_some`, `optionElim_add`, `optionEquivLeft_coeff_coeff`, `mem_support_coeff_optionEquivLeft` all use `optionElim` |
| 4 | Set-with-predicate to bundled? | no | — | — |
| 5 | Field-specific to (semi)ring? | yes | `ℕ` to `AddCommMonoid M` (evidence (4)) | — |
| 6 | 1-categorical to higher? | no | — | — |
| 7 | Concrete index to general monoid? | yes | same as row 5 | — |
| 8 | Concrete-via-abstract? | no | statement has no named concrete object beyond `ℕ` | — |
| 9 | False-generalisation guard | no | the `optionElim` restatement is the same object (evidence (3)) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `d = d.some.optionElim (d none)`, which is exactly `(Finsupp.optionElim_some d).symm`.
  - Cost: CHEAP
  - Mathlib downstream this enables: direct use of `MvPolynomial.optionEquivLeft_coeff_coeff` and `optionEquivLeft_coeff_some_coeff_none`, which are stated with `optionElim` / `n none`, `n.some`.
  - Real mathematical improvement: removes an ad-hoc spelling of a decomposition mathlib already names.

### Proof strategy — `Roth.eq_mapDomain_some_add_single`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | yes | `rw [← optionElim_eq_mapDomain_add_single, optionElim_some]` (evidence (3)) | CHEAP |
| 5 | missing mathlib helpers | yes (minor) | `Finsupp.optionElim y f = f.mapDomain some + single none y` (or the `embDomain` version) is absent from Mathlib/Data/Finsupp/Option.lean | CHEAP (could be a tiny mathlib PR, but nothing in this project needs it once the call site uses optionEquivLeft API directly) |

### Proof strategy verdict (Phase 4.6)

Current strategy: REFACTOR-RECOMMENDED
  - Proposed strategy: don't prove this at all; the consumer uses `optionEquivLeft_coeff_some_coeff_none` directly.
  - Cost: CHEAP
  - Missing mathlib API (if any): optionally `Finsupp.optionElim_eq_mapDomain_add_single` (evidence (2)); not needed by the project.
  - Would refactoring make the proof strictly shorter / cleaner? yes

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.eq_mapDomain_some_add_single`

[A] Lean-Finder       "decompose a finsupp on Option α into the part on α and the value at none"   hits: `Finsupp.optionElim_some`, `Finsupp.optionEquiv`, `Finsupp.optionElim`, `Finsupp.some`
[B] Loogle            `Finsupp.mapDomain Option.some _ + Finsupp.single none _`   no hits (the literal spelling is absent)
[C] LeanSearch        "finitely supported function on Option α equals mapDomain some of its restriction plus single none of its value at none"   hits: `Finsupp.optionEquiv`, `optionElim`, `some_single_some`, `optionElim_apply_some`
[D] Grep mathlib src  `optionElim`, `mapDomain some`, `single none`, `embDomain.*single none`, `optionEquivLeft_coeff`   hits: Mathlib/Data/Finsupp/Option.lean (`optionElim_some`, `optionElim_add`, `optionElim_zero`, `eq_option_embedding_update_none_iff`); Mathlib/Algebra/MvPolynomial/Equiv.lean:509 `optionEquivLeft_coeff_some_coeff_none`, :610 `optionEquivLeft_coeff_coeff`; no `mapDomain some + single none` lemma
[E] Name pattern      lean_local_search-style grep for `eq_mapDomain_some_add_single`, `optionElim_eq`, `mapDomain_some`   no hits

Searched for both:
  - the user's current form (`mapDomain some + single none`): absent.
  - the literature-standard form (Option split / `optionEquiv`): present as `Finsupp.optionElim_some`.

Concluded: found building blocks (`Finsupp.optionElim_some`, `Finsupp.optionElim_apply_eq_elim`, `Finsupp.mapDomain_apply_of_injective`, `Finsupp.mapDomain_of_notMem_range`; at the call site `MvPolynomial.optionEquivLeft_coeff_some_coeff_none`); composition would yield our form.

### Normal-form check — `Roth.eq_mapDomain_some_add_single`

Equivalent formalisms: (a) `d = d.some.mapDomain some + single none (d none)`; (b) `d = (d.some.embDomain .some).update none (d none)` (`optionEquiv.symm`); (c) `d = d.some.optionElim (d none)`.
Does mathlib already have a canonical form? yes — (c), `Finsupp.optionElim_some` (Mathlib/Data/Finsupp/Option.lean).
Our statement is stated against a non-canonical form (a) → REFACTOR: use (c).
RHS convention respected? no (the decomposed form is on the RHS of an `f = …` statement, whereas mathlib's simp-normal `optionElim_some` collapses to `f`).

### Syntactic generality — `Roth.eq_mapDomain_some_add_single`

Alternative restatements attempted:
- (c) `d = d.some.optionElim (d none)` — compiles as `(optionElim_some d).symm` (evidence (1)).
- `M`-general version — compiles (evidence (4)).
- Call-site-level `P.coeff e = (coeffNone P (e none)).coeff e.some` — compiles as `(optionEquivLeft_coeff_some_coeff_none R τ e P).symm` (evidence (5)).

Chosen restatement: the call-site-level one (no standalone lemma).
Justification: the only consumer needs a coefficient identity which mathlib already provides verbatim.

### Superfluous-argument audit — `Roth.eq_mapDomain_some_add_single`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `ℕ` as codomain | no | any `AddCommMonoid M` works (evidence (4)) |
| 2 | `[Fintype τ] [DecidableEq τ]` | no | already omitted via `omit` |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (target: `Finsupp.optionElim_some`)
Syntactic generality: RESTATE (eliminate in favour of `optionEquivLeft_coeff_some_coeff_none` at the call site)
Superfluous arguments: 1 to drop (`ℕ` specialisation)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.eq_mapDomain_some_add_single`

Internal use count: 0 (outside the declaring file); 1 inside Roth/Separation.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:107 | `· rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` (in `eq_sum_X_none_pow_mul_coeffNone`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using it?):
  - Roth/Separation.lean:84–88 (`coeff_coeffNone`) re-proves the same `mapDomain some + single none` vs `optionElim` matching by `ext o; cases o <;> simp [...]` after `optionEquivLeft_coeff_coeff`; i.e. the project converts mathlib's `optionElim` into its own spelling there and converts back here.

### Composition check (Phase 6)

Can `Roth.eq_mapDomain_some_add_single` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [← optionElim_eq_mapDomain_add_single, optionElim_some]` where the glue is `ext o; cases o <;> simp [mapDomain_of_notMem_range, mapDomain_apply_of_injective (Option.some_injective _)]`.
  - Mathlib decls used: `Finsupp.optionElim_some`, `Finsupp.optionElim_apply_eq_elim` (simp), `Finsupp.mapDomain_of_notMem_range`, `Finsupp.mapDomain_apply_of_injective`.
  - Result: succeeds (evidence (2), (3)); equivalently the current 3-line `ext`/`simp` proof.
  - Notes: trivial simp composition.

Attempt 2 (at the call site): `(optionEquivLeft_coeff_some_coeff_none R τ e P).symm` closes the goal the lemma was used for.
  - Mathlib decls used: `MvPolynomial.optionEquivLeft_coeff_some_coeff_none`.
  - Result: succeeds (evidence (5)); 1 call.

Conclusion: COMPOSABLE

## Verdict: `Roth.eq_mapDomain_some_add_single`

Verdict: NO-composable-from-mathlib

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the identity is notation-level (`x^α = x'^{α'} x_n^{α_n}`); general form is `ℕ^(A ⊔ B) ≅ ℕ^(A) × ℕ^(B)`, which mathlib has for `Option` as `Finsupp.optionEquiv`.
- Generality analysis (Phase 4): STRICTLY NARROWER (`ℕ` vs `AddCommMonoid`), but the general form is `optionElim_some` in disguise.
- Mathlib search (Phase 5): building blocks `Finsupp.optionElim_some`, `MvPolynomial.optionEquivLeft_coeff_some_coeff_none`.
- Composition check (Phase 6): COMPOSABLE (1 call at the call site).

**Rationale:**
Mathlib already owns this decomposition in its canonical form, `Finsupp.optionElim_some : f.some.optionElim (f none) = f` (Mathlib/Data/Finsupp/Option.lean), with `optionEquiv` packaging it as an equivalence. The project lemma is the same statement with `optionElim y f` unfolded to `f.mapDomain some + single none y`, a spelling mathlib does not use. A generalised `AddCommMonoid` version compiles but would only add a second, non-canonical name for `optionElim_some`, so it is not mathlib material. At most, a one-line `optionElim_eq_mapDomain_add_single` normalisation could go in Data/Finsupp/Option.lean, and nothing in this project needs it.

The only consumer (Separation.lean:107) uses the lemma to turn `(coeffNone P (e none)).coeff e.some` back into `P.coeff e`. That is exactly mathlib's `MvPolynomial.optionEquivLeft_coeff_some_coeff_none` once `coeffNone` is unfolded, so the round trip through `coeff_coeffNone` and this lemma can go. The root cause is that `coeff_coeffNone` is stated with `d.mapDomain some + single none ν` rather than mathlib's `d.optionElim ν`. Restated in mathlib's form it is literally `optionEquivLeft_coeff_coeff` (evidence (6)).

WHY not: mathlib has the building blocks; the form is a 1-call composition at the call site.
Belongs-elsewhere check: not worth keeping anywhere; delete.
Mathlib building blocks: `Finsupp.optionElim_some` (Mathlib/Data/Finsupp/Option.lean), `MvPolynomial.optionEquivLeft_coeff_some_coeff_none` (Mathlib/Algebra/MvPolynomial/Equiv.lean:509), `MvPolynomial.optionEquivLeft_coeff_coeff` (Mathlib/Algebra/MvPolynomial/Equiv.lean:610).
Composition sketch (≤3 lines):
```lean
example (d : Option τ →₀ ℕ) : d = d.some.optionElim (d none) := (Finsupp.optionElim_some d).symm
-- at the call site:
example (P : MvPolynomial (Option τ) R) (e : Option τ →₀ ℕ) :
    P.coeff e = (coeffNone P (e none)).coeff (Finsupp.some e) :=
  (optionEquivLeft_coeff_some_coeff_none R τ e P).symm
```
Call sites in our project (from Phase 6.0): 1
Refactor plan: at Roth/Separation.lean:107, in the first `split_ifs` branch of `eq_sum_X_none_pow_mul_coeffNone`, replace `rw [coeff_coeffNone, ← eq_mapDomain_some_add_single]` with `exact (optionEquivLeft_coeff_some_coeff_none R τ e P).symm` (check whether the goal sides need `.symm` and whether `coeffNone` needs a `rw [coeffNone]` first, since it is a plain def). Optionally restate `coeff_coeffNone` (Separation.lean:82) with `P.coeff (d.optionElim ν)` so it becomes `optionEquivLeft_coeff_coeff`; its other callers then need `optionElim`-based rewriting.
Next action: delete `Roth.eq_mapDomain_some_add_single` from the project and inline the composition at the single call site.

---

## Next step

At Roth/Separation.lean:107 use `MvPolynomial.optionEquivLeft_coeff_some_coeff_none` directly, then delete `Roth.eq_mapDomain_some_add_single`. No mathlib PR.

## Evidence
- Evidence file: `.mathlib-quality/overview/evidence/Roth.eq_mapDomain_some_add_single/compose.lean` (imports `Roth.Separation`); `lake env lean` on it gives no output (all six checks pass): (1) `d = d.some.optionElim (d none)` by `(optionElim_some d).symm`; (2) glue `optionElim_eq_mapDomain_add_single` for any `AddCommMonoid M`; (3) the project statement by `rw [← optionElim_eq_mapDomain_add_single, optionElim_some]`; (4) the project statement generalised to `AddCommMonoid M`; (5) the call-site goal by `(optionEquivLeft_coeff_some_coeff_none R τ e P).symm`; (6) `coeff_coeffNone` restated with `optionElim` equals `optionEquivLeft_coeff_coeff R P ν d`.
- Searches: 3 WebSearch queries, Lean-Finder, LeanSearch and Loogle queries, mathlib grep, all recorded in the tables above. ChatGPT MCP was n/a (not configured in this session).
