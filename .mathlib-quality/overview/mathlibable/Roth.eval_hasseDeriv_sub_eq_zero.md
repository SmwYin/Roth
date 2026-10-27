---
decl: Roth.eval_hasseDeriv_sub_eq_zero
file: Roth/MainLemma.lean
line: 402
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Congruence of diagonalised Hasse derivatives mod f gives vanishing of the derivative of W' - W'' at (alpha, ..., alpha); the content is the mathlib triple dvd_modByMonic_iff_dvd + sub_modByMonic + aeval_eq_zero_of_dvd_aeval_eq_zero plus a simp unfolding of the project-local diag and hasseDeriv_map, single caller, Roth-specific shape, nothing to upstream.
action: Do not upstream; keep in Roth/MainLemma.lean as the named Lemma 9 step (sole caller exists_mem_RSet_le_index_aux at Roth/MainLemma.lean:567) or optionally inline its two-step proof there; no mathlib PR.
---

# Roth.eval_hasseDeriv_sub_eq_zero

## Inventory entry

### `theorem Roth.eval_hasseDeriv_sub_eq_zero`
- **Type**: `∀ {σ : Type*} {S : Type*} [CommRing S] {f : Polynomial ℤ} {α : S}, Polynomial.aeval α f = 0 → ∀ {W' W'' : MvPolynomial σ ℤ} {j : σ →₀ ℕ}, Roth.diag (hasseDeriv j W') %ₘ f = Roth.diag (hasseDeriv j W'') %ₘ f → MvPolynomial.eval (fun _ ↦ α) (hasseDeriv j (MvPolynomial.map (Int.castRingHom S) (W' - W''))) = 0`
- **What**: If `f(α) = 0` and the diagonal substitutions `Δ_j W'(x, …, x)` and `Δ_j W''(x, …, x)` have the same remainder modulo `f`, then the Hasse derivative `Δ_j (W' - W'')`, with coefficients pushed into `S`, vanishes at the diagonal point `(α, …, α)`.
- **How**: (i) `f ∣ diag (hasseDeriv j (W' - W''))` via `Polynomial.dvd_modByMonic_iff_dvd.mp` and `simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]`; (ii) `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero hdvd hfα`, transported to the goal by `simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def, diag, MvPolynomial.comp_aeval_apply, Polynomial.aeval_X]`.
- **Hypotheses**: `hfα : aeval α f = 0`; `h` congruence of remainders. No monicity of `f` (`%ₘ` is used, but `dvd_modByMonic_iff_dvd` holds for any `f`), no finiteness of `σ`.
- **Uses from project**: `Roth.diag`, `Roth.diag_sub`, `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_map`
- **Used by**: `Roth.exists_mem_RSet_le_index_aux` (private, Roth/MainLemma.lean:567). No other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 396–411 (docstring 396–401, statement 402–405), proof length 6 lines
- **Notes**: Paper step: §6, proof of Lemma 9 ("`Δ_j W^*(x_1,…,x_m)` are zero when `x_1 = ⋯ = x_m = α`").

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/MainLemma.lean:567 inside the private `exists_mem_RSet_le_index_aux`.
- Wrapper of 1–2 mathlib calls? Close: three mathlib lemmas (`Polynomial.dvd_modByMonic_iff_dvd`, `Polynomial.sub_modByMonic`, `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero`) plus a simp that unfolds project-local `diag` and commutes `hasseDeriv` with `map`.
- Does mathlib have it? No (involves project-local `diag`, `hasseDeriv`); the generic core (congruent mod `f` ⇒ equal at roots of `f`) is a mathlib composition, and for monic `f` is `Polynomial.aeval_modByMonic_eq_self_of_root`.
- Too specific (inline)? Specific to Lemma 9, but naming it isolates the coercion/simp bookkeeping from the main proof and matches a sentence of the paper; same treatment as the sibling `Roth.sub_mem_RSet` (KEEP).
- Well-chosen? Yes; already maximally general in `S` and avoids an unnecessary monicity hypothesis.
- Conclusion: `KEEP` — keep as the named Lemma 9 step; optional inlining at line 567 is cosmetic.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.eval_hasseDeriv_sub_eq_zero` absent from mathlib (grep count 0). Not a glue lemma (real 6-line proof), so a full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` elaborates clean)
- decl `Roth.eval_hasseDeriv_sub_eq_zero`: resolved at Roth/MainLemma.lean:402
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's Lemma 9 (the main lemma): existence of an auxiliary integer polynomial with large index at (α, …, α) and controlled coefficients.

### Statement (Phase 1)

`Roth.eval_hasseDeriv_sub_eq_zero` is a theorem stating the following:

Let `f ∈ ℤ[x]`, let `S` be a commutative ring and `α ∈ S` a root of `f`. Let `W', W'' ∈ ℤ[x_j : j ∈ σ]` and `j` a multi-index. If `Δ_j W'(x,…,x) ≡ Δ_j W''(x,…,x) (mod f)` in `ℤ[x]`, then `(Δ_j (W' − W''))(α,…,α) = 0` in `S`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variable index set.
- `S : Type*`, `[CommRing S]` — target ring of evaluation.
- `f : ℤ[X]`, `α : S` — the modulus and its root.
- `W' W'' : MvPolynomial σ ℤ`, `j : σ →₀ ℕ` — the polynomials and the derivative multi-index.

Hypotheses (Lean side):
- `hfα : aeval α f = 0` — `α` is a root of `f`.
- `h : diag (Δ_j W') %ₘ f = diag (Δ_j W'') %ₘ f` — congruence modulo `f`.

Conclusion (math): the Hasse derivative of the difference vanishes at the diagonal point.

Conclusion (Lean): `eval (fun _ ↦ α) (hasseDeriv j (map (Int.castRingHom S) (W' - W''))) = 0`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: one step inside the proof of Lemma 9; not a main result, not named, introduces no structure.

### One-line check (Phase 2b)

Body line count: 6 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table

| #  | Channel                           | Query | Hit? | Standard form found | Notes |
|----|-----------------------------------|-------|------|---------------------|-------|
|  1 | WebSearch (specific form)         | Roth's lemma 9 Hasse derivative diagonal substitution divisible by f(x) vanish at alpha | partial | none as a stated lemma | Background only (Hasse derivative Wikipedia, Evertse notes); the step is an inline sentence in Roth-type proofs |
|  2 | WebSearch (general form)          | polynomials congruent modulo f have equal values at roots of f | partial | `h ∣ g₁ − g₂`, `h(r)=0` ⇒ `g₁(r)=g₂(r)` | Folklore; stated in passing, never as a named theorem |
|  3 | WebSearch (named / aliases)       | "multivariate Hasse derivative" evaluation diagonal "index" Roth theorem Siegel lemma | yes | Roth proof: auxiliary polynomial has large index at (α,…,α) | Evertse Luminy slides, arXiv 2502.00731, Ru's Roth notes; step is inline |
|  4 | ChatGPT MCP                       | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
|  5 | Local references                  | grep `.mathlib-quality/references/clean.tex` for "W^*", "Lemma 9" | yes | lines 1505–1511: Hasse differentiation, diagonal substitution, evaluation at α | the project's source; exactly the sentence formalised |
|  6 | nLab                              | Hasse-Schmidt derivative / derivation (WebSearch restricted to ncatlab.org) | yes | definition and Leibniz rule only | nothing about evaluation at roots of a modulus |
|  7 | nCatLab (categorical)             | n/a | n/a | n/a | not a categorical concept (elementary polynomial congruence) |
|  8 | Stacks Project                    | n/a | n/a | n/a | not an algebraic-geometry concept |
|  9 | MathOverflow / Math.StackExchange | Hasse-Schmidt derivation evaluation at root polynomial divisible (restricted to math.stackexchange.com; mathoverflow.net blocked to the search agent) | no | none | no thread treats this step; it is considered trivial |
| 10 | recent arXiv (last 5 years)       | covered by #3 (arXiv 2502.00731 "Diophantine approximation and the subspace theorem") | yes | inline step of Roth's proof | no stand-alone lemma |

### Literature summary

Concept identified as: "a polynomial congruent to another mod f takes the same value at roots of f", composed with diagonal substitution and Hasse differentiation (step of Roth's Lemma 9).
Sources agree on the standard form: yes — folklore, always inline.
Most general standard form: for any commutative ring `R`, `R`-algebra `S`, `f, g, h ∈ R[x]` with `f ∣ g − h` and `f(α) = 0`, `g(α) = h(α)`.
Generality dimensions where the literature varies:
  - ring of evaluation: number field / ℂ / ℝ to any `R`-algebra; Lean already takes any `CommRing S`.
  - monicity of `f`: irrelevant to the statement (Lean does not assume it).
Disagreement with the literature: none.

### Generality analysis

Literature-standard form: above (generic core).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `[CommRing S]` | commutative ring | any `ℤ`-algebra that is a commutative ring | no | `Int.castRingHom S` needs `NonAssocRing S` and `MvPolynomial.eval` needs `CommSemiring S` (evidence #3); together that is `CommRing` |
| 2 | `f : Polynomial ℤ` | integer coefficients | coefficients in any `R` | not usefully | `diag`, `hasseDeriv` and the `W`'s are over `ℤ` throughout the project; generalising `R` means restating `diag` (already flagged in `Roth.diag` report), not a local edit |
| 3 | `h` via `%ₘ` | remainder equality | `f ∣ g − h` | equivalent | no monicity required; `%ₘ` matches the caller `exists_ne_modByMonic_eq` |
| 4 | `hfα` | `aeval α f = 0` | `f(α) = 0` | no | essential |

### Generality verdict

The current form is: MAXIMALLY GENERAL (within the project's ℤ-coefficient conventions)
Number of weakening opportunities found: 0 (verified: no monicity hypothesis present; CommRing S minimal per `#check @Int.castRingHom` in evidence)
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Downstream |
|---|---|---|---|---|
| 1 | preambles → typeclasses | no | single-use hypotheses | — |
| 2 | sequences → filters | no | no analysis | — |
| 3 | construction → universal property | no | — | — |
| 4 | set-with-predicate → bundled substructure | partly | congruence could be `AdjoinRoot.mk f g = AdjoinRoot.mk f h` or `Ideal.Quotient` | none here; the caller produces `%ₘ` equalities |
| 5 | field-specific → (semi)ring | no | already any `CommRing S` | — |
| 6 | higher-categorical | no | — | — |
| 7 | concrete index → general | no | ℤ is forced by the project | — |
| 8 | concrete-via-abstract | yes (diagnostic) | after `hdvd`, the proof only uses `aeval_eq_zero_of_dvd_aeval_eq_zero` — abstract core is the generic lemma (evidence #1), itself a 3-call mathlib composition | none: the abstract core is already composable |
| 9 | false-generalisation guard | no false generalisation | the generic core is the same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
One-line reason: the only abstraction (Q8) lands on a statement that mathlib already provides as a composition, so it yields no new lemma to add.

### Proof strategy (Phase 4.6)

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | divisibility is the natural tool | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the generic core is available as `dvd_modByMonic_iff_dvd` + `aeval_eq_zero_of_dvd_aeval_eq_zero` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Risk verdict
n/a — declaration kind is theorem.

### Mathlib search-status

[A] Lean-Finder: "two polynomials congruent modulo f take the same value at every root of f" → `AdjoinRoot.mk_eq_mk`, `Polynomial.aeval_modByMonic_eq_self_of_root` (monic), `Polynomial.eval₂_modByMonic_eq_self_of_root`, `IsAdjoinRootMonic.map_modByMonic`; no exact match.
[B] Loogle: `Polynomial.aeval _ (_ %ₘ _) = Polynomial.aeval _ _` → `Polynomial.aeval_modByMonic_eq_self_of_root`, `minpoly.aeval_modByMonic_minpoly`, `Matrix.aeval_eq_aeval_mod_charpoly`; building blocks only.
[C] LeanSearch: "if p mod q equals r mod q and q vanishes at x then p and r have the same value at x" → `Polynomial.eval₂_modByMonic_eq_self_of_root`, `Polynomial.modByMonic_eq_of_dvd_sub`, `SModEq.eval`; building blocks.
[D] Grep mathlib src: `eval_hasseDeriv_sub_eq_zero` (0 hits); `dvd_modByMonic_iff_dvd` (Mathlib/Algebra/Polynomial/Div.lean:269), `aeval_eq_zero_of_dvd_aeval_eq_zero` (Mathlib/Algebra/Polynomial/AlgebraMap.lean:511).
[E] Name pattern (lean_local_search / grep): no MvPolynomial Hasse derivative in mathlib (see `MvPolynomial.hasseDeriv` report), hence no Hasse-specific form.

Searched for both the user's form and the generic core.
Concluded: found building blocks (`Polynomial.dvd_modByMonic_iff_dvd`, `Polynomial.sub_modByMonic`, `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero`, `MvPolynomial.comp_aeval_apply`, `MvPolynomial.eval_map`); composition yields our form.

### Statement-shape verdict (Phase 5.5)

Normal-form check: equivalent formalisms are `%ₘ` equality, `f ∣ g − h`, `AdjoinRoot.mk f g = AdjoinRoot.mk f h`. Mathlib's canonical bridge is `Polynomial.modByMonic_eq_of_dvd_sub` / `dvd_modByMonic_iff_dvd`; the `%ₘ` form matches what the caller (`exists_ne_modByMonic_eq`) produces.
Syntactic generality: alternatives tried — hypothesis `f ∣ diag (hasseDeriv j (W' - W''))`; conclusion with `aeval` instead of `eval ∘ map`. Chosen: the current form, because it takes the caller's output verbatim and returns exactly the shape `le_index_of_forall_eval_eq_zero` consumes.
Superfluous-argument audit:

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommRing S]` | yes | minimal (evidence #3) |
| 2 | `hfα` | yes | root of `f` |
| 3 | `h` | yes | congruence |

Normal form: OK. Syntactic generality: OK. Superfluous arguments: NONE.
Overall: SHIP-AS-STATED (locally)

### Call sites

Internal use count: 1 (declaring file only); external-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern |
|---|---|
| Roth/MainLemma.lean:567 | `fun d hd hw ↦ eval_hasseDeriv_sub_eq_zero hfα (hWeq d (hJ d hd hw))` in `exists_mem_RSet_le_index_aux` |

Inline-derivation grep: (none) — no other site re-derives `aeval_eq_zero_of_dvd_aeval_eq_zero` for diagonalised Hasse derivatives.

### Composition check (Phase 6)

Attempt 1 (generic core): `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero (Polynomial.dvd_modByMonic_iff_dvd.mp (by simp [Polynomial.sub_modByMonic, hgh])) hfα` — succeeds (evidence #1).
Attempt 2 (our form): the generic core + `simpa [hasseDeriv_map, eval_map, ← algebraMap_int_eq, ← aeval_def, diag, MvPolynomial.comp_aeval_apply, Polynomial.aeval_X]` — succeeds (evidence #2), i.e. a trivial simp transport of a 3-call composition.

Conclusion: COMPOSABLE (generic content is a 3-lemma mathlib composition; the remainder is a simp transport through project-local `diag`/`hasseDeriv`).

## Verdict: `Roth.eval_hasseDeriv_sub_eq_zero`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): folklore "congruent mod f ⇒ equal at roots of f", inline in every Roth proof; never a named lemma.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (no monicity, `CommRing S` minimal).
- Mathlib search (Phase 5): building blocks `dvd_modByMonic_iff_dvd`, `sub_modByMonic`, `aeval_eq_zero_of_dvd_aeval_eq_zero`.
- Composition check (Phase 6): COMPOSABLE.

**Rationale:** The mathematical content is the one-line fact that `f ∣ g − h` and `f(α) = 0` give `g(α) = h(α)`, which mathlib supplies by composing `Polynomial.dvd_modByMonic_iff_dvd`, `Polynomial.sub_modByMonic` and `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero` (and, for monic `f`, `Polynomial.aeval_modByMonic_eq_self_of_root` directly). Everything else is bookkeeping through the project-local `Roth.diag` (itself NO-composable) and `MvPolynomial.hasseDeriv_map`. The shape (diagonal substitution of a Hasse derivative of a difference of integer polynomials) is specific to Roth's Lemma 9 and has one caller.

WHY not: mathlib has the building blocks; the statement is a 3-call composition plus a simp transport. Belongs-elsewhere: keep project-local in Roth/MainLemma.lean as the named Lemma 9 step (same as sibling `Roth.sub_mem_RSet`).
Mathlib building blocks: `Polynomial.dvd_modByMonic_iff_dvd` (Mathlib/Algebra/Polynomial/Div.lean:269), `Polynomial.sub_modByMonic` (Mathlib/Algebra/Polynomial/Div.lean), `Polynomial.aeval_eq_zero_of_dvd_aeval_eq_zero` (Mathlib/Algebra/Polynomial/AlgebraMap.lean:511), `MvPolynomial.comp_aeval_apply`, `MvPolynomial.eval_map`.
Composition sketch:
```lean
example (hfα : aeval α f = 0) (hgh : g %ₘ f = h %ₘ f) : aeval α (g - h) = 0 :=
  aeval_eq_zero_of_dvd_aeval_eq_zero
    (dvd_modByMonic_iff_dvd.mp (by simp [sub_modByMonic, hgh])) hfα
```
Call sites in our project: 1 (Roth/MainLemma.lean:567).
Refactor plan: optional — at Roth/MainLemma.lean:567 the two-step proof could be inlined, but keeping the named step matches the paper and isolates coercion bookkeeping; recommended to keep.

## Next step

Do not upstream; keep `Roth.eval_hasseDeriv_sub_eq_zero` in Roth/MainLemma.lean (sole caller Roth/MainLemma.lean:567). No mathlib PR.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.eval_hasseDeriv_sub_eq_zero/experiments.lean` (imports `Roth.CoeffNorm`), checked with `lean_diagnostic_messages`: clean (only the `#check` info). Contains (1) the generic core as a 3-lemma mathlib composition without monicity, (2) a re-proof of the declaration, (3) `#check @Int.castRingHom` showing `NonAssocRing` is required, so `CommRing S` is minimal.
- Searches: Loogle, LeanSearch, Lean-Finder, mathlib grep as recorded; 5 WebSearch queries (one rejected for a blocked domain, re-run restricted to ncatlab.org/math.stackexchange.com); local reference `clean.tex` lines 1505–1511. ChatGPT MCP n/a (not configured).
