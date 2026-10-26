---
decl: Roth.normOne_nonneg
file: Roth/CoeffNorm.lean
line: 50
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Standard nonnegativity companion of the l1 coefficient norm (cf. Polynomial.supNorm_nonneg, gaussNorm_nonneg, mahlerMeasure_nonneg); mathlib has no l1 norm on polynomials, and the same one-line proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing (Evidence.l1Norm_nonneg).
action: Ship as MvPolynomial.l1Norm_nonneg (proof Finset.sum_nonneg fun _ _ => norm_nonneg _) in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep Roth.normOne_nonneg as the R = ℤ specialisation used by normOne_prod_le (line 107) and normOne_det_le (line 128).
---

# Roth.normOne_nonneg

## Inventory entry

### `theorem Roth.normOne_nonneg`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) : 0 ≤ Roth.normOne P`
- **What**: The ℓ¹ coefficient norm `‖P‖₁ = ∑ |a_e|` of an integer polynomial is nonnegative.
- **How**: Term proof `Finset.sum_nonneg fun _ _ ↦ abs_nonneg _` (each summand of the support sum is an absolute value).
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`
- **Used by**: Roth/CoeffNorm.lean:107 (`normOne_prod_le`, as the nonnegativity argument of `Finset.le_prod_of_submultiplicative_of_nonneg`), Roth/CoeffNorm.lean:128 (`normOne_det_le`, inside `Finset.prod_le_prod₀`). No uses outside CoeffNorm.lean (`grep -rn normOne_nonneg Roth/`).
- **Visibility**: public
- **Lines**: 49–51, proof length 1 line
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, 2 in-file call sites (lines 107, 128), both passing it as a function argument (`normOne_nonneg` / `fun _ _ ↦ normOne_nonneg _`), where a named lemma is genuinely more convenient than an inline term.
- Wrapper of 1–2 mathlib calls? Yes formally (`Finset.sum_nonneg` + `abs_nonneg`), but it is the standard API companion of a named def; mathlib ships exactly such lemmas for every real-valued norm-like def (`Polynomial.supNorm_nonneg`, `Polynomial.gaussNorm_nonneg`, `Polynomial.mahlerMeasure_nonneg`, `spectralValue_nonneg`).
- Does mathlib have it? No — mathlib has no ℓ¹ polynomial norm (parent report `Roth.normOne`).
- Too specific (inline)? No; inlining would require unfolding `normOne` at both call sites.
- Well-chosen? Yes, modulo the parent's ℤ-specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at the generalised `MvPolynomial.l1Norm` together with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_nonneg` not in mathlib (no `namespace Roth` in Mathlib; the only `normOne` hits in Mathlib are `NormOneClass` instances). Not a glue lemma (the body is a real, if short, proof via `Finset.sum_nonneg`, not `rfl`/unfolding), so a full run, assessed in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to an ℓ¹ norm on `MvPolynomial σ R`, `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the parent evidence file importing `Roth.CoeffNorm` has no errors per `lean_diagnostic_messages`)
- decl `Roth.normOne_nonneg`: resolved at Roth/CoeffNorm.lean:50
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_nonneg` is a theorem stating the following: for every polynomial `P ∈ ℤ[X_σ]`, its length (ℓ¹ coefficient norm) `‖P‖₁ = ∑_e |a_e|` is a nonnegative real number.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `P : MvPolynomial σ ℤ` — the polynomial.

Hypotheses (Lean side):
- none.

Conclusion (math): `0 ≤ ‖P‖₁`.

Conclusion (Lean): `0 ≤ Roth.normOne P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic API lemma (nonnegativity) of a helper definition; not a new structure, not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE-check skipped (theorem). Note for Phase 7: a one-line API lemma about a new def is the mathlib norm (cf. `Polynomial.supNorm_nonneg`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a polynomial L(P) sum of absolute values of coefficients nonnegative norm properties | yes | `‖P‖ = ∑ |c_α|`, a norm (nonneg, zero only at 0, triangle, submultiplicative) | arXiv 0808.2952 (multivariate, states the norm and multiplicativity); Schinzel's reduced-length papers; FriCAS `length` |
| 2 | WebSearch (general form) | l1 norm monoid algebra finitely supported function sum of norms seminorm nonnegativity | yes | ℓ¹(M) norm `∑ ‖f(m)‖`; finitely supported functions dense in ℓ¹ | nonnegativity is part of the norm axioms; mathlib `lp` docs (`p = 1`: summable norms) |
| 3 | WebSearch (named-after / aliases / mathlib) | mathlib Polynomial supNorm_nonneg l1 norm polynomial coefficients | partial | ℓ_r coefficient norms vs sup norm (Galicer–Mansilla–Muro); Magma `SumNorm` | No mathlib ℓ¹ hit; aliases: length, SumNorm, ℓ¹ norm |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` (via parent report, lines 445–452) | yes | `‖f‖₁ = ∑_e |a_e|` | Source uses the norm in Lemma 3; nonnegativity is implicit (used in products of bounds) |
| 6 | nLab | Banach algebra / group algebra ℓ¹ (via parent) | yes | ℓ¹(G) normed algebra | nonneg is an axiom of norms; no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | Not a categorical statement (an inequality for a concrete norm) |
| 8 | Stacks Project | — | n/a | — | Not algebraic geometry; no coefficient norms in Stacks |
| 9 | MathOverflow / Math.SE | length of polynomial L(PQ) ≤ L(P)L(Q) (via parent) | yes | same `L(P)` | nonneg taken as trivial everywhere |
| 10 | recent arXiv (last 5 years) | ℓ¹ coefficient norm in height bounds (via #1/#3) | yes | same | no competing form |

### Literature summary (Phase 3)

Concept identified as: nonnegativity of the length `L(P)` (ℓ¹ coefficient norm), i.e. the first norm axiom for `L`.
Sources agree on the standard form: yes — `0 ≤ ∑ ‖a_e‖`, trivially from nonnegativity of each term.
Most general standard form: for any seminormed coefficient ring `R` (indeed any seminormed additive group) and any index monoid, `0 ≤ ∑_m ‖f(m)‖`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℂ / any (semi)normed ring; most general is seminormed (for `MvPolynomial`, `SeminormedCommRing`).
  - index set: ℕ, ℕ^σ, arbitrary monoid.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_nonneg`

Literature-standard form (from Phase 3): `0 ≤ l1Norm p` for `p : MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only nonnegativity of each summand (`norm_nonneg`); verified (Evidence.l1Norm_nonneg) |
| 2 | `abs_nonneg` | absolute value of real cast | `norm_nonneg` | yes | follows the parent's `|·|` → `‖·‖` restatement |
| 3 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited solely from the parent def's ℤ-specialisation; the statement has no hypotheses of its own)
Number of weakening opportunities found: 1 (ℤ → `[SeminormedCommRing R]` via the parent def)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` lines 22–23 prove `Evidence.l1Norm_nonneg (p : MvPolynomial σ R) : 0 ≤ l1Norm p := Finset.sum_nonneg fun _ _ ↦ norm_nonneg _` over `[SeminormedCommRing R]`; re-checked this session with `lean_diagnostic_messages` (severity error): no errors. The same file has the bridge `l1Norm_int_eq_normOne`, so the project lemma is the `R = ℤ` instance.
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_nonneg {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) : 0 ≤ p.l1Norm :=
  Finset.sum_nonneg fun _ _ ↦ norm_nonneg _
```

Cost of restatement: CHEAP — proof is verbatim (`abs_nonneg` → `norm_nonneg`).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite sum inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | no sets | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `positivity` extension / `norm_nonneg`-style API for `l1Norm` |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` ℓ¹ norm (parent's unverified option) | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only nonnegativity of summands; covered by row 5 | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ`, `‖z‖ = |(z:ℝ)|` (compiled bridge) — same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_nonneg` over `[SeminormedCommRing R]` (above); optionally tagged for a `positivity` extension like other nonnegative norm-like defs.
  - Cost: CHEAP
  - Mathlib downstream this enables: required by any submultiplicativity-over-products lemma (`Finset.le_prod_of_submultiplicative_of_nonneg` needs it, exactly as in the project's `normOne_prod_le`) and by `Finset.prod_le_prod₀` bounds; parallels `Polynomial.supNorm_nonneg`.
  - Real mathematical improvement: one nonnegativity lemma for every normed coefficient ring rather than a ℤ copy.

### Proof strategy — `Roth.normOne_nonneg`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Element-wise vs point-free algebra? | no | — | — |
| 3 | Sequences vs filters? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | `Finset.sum_nonneg` + `norm_nonneg` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_nonneg`

[A] Lean-Finder       "nonnegativity of the l1 norm of the coefficients of a multivariate polynomial"   hits only `Polynomial.gaussNorm_nonneg`, `spectralValue(Terms)_nonneg`, `Polynomial.mahlerMeasure_nonneg`; no ℓ¹ norm
[B] Loogle            `|- 0 ≤ ∑ _ ∈ _, ‖_‖`   no hits (generic `Finset.sum_nonneg` is the building block)
[C] LeanSearch        "sum of norms of coefficients of a polynomial is nonnegative"   hits `Polynomial.mahlerMeasure_le_sum_norm_coeff` (inline `p.sum fun _ a ↦ ‖a‖`), `mahlerMeasure_nonneg`, `spectralValue_nonneg`; no ℓ¹ lemma
[D] Grep mathlib src  `normOne`, `l1Norm`, `supNorm_nonneg`, `gaussNorm_nonneg`   `normOne` only as `NormOneClass` instances; `Polynomial.supNorm_nonneg` (Analysis/Polynomial/Norm.lean:66) and `gaussNorm_nonneg` are the sup/Gauss analogues; no ℓ¹
[E] Name pattern      `l1Norm_nonneg`, `normOne_nonneg`   none in mathlib (only the project's own decl)

Searched for both the ℤ form and the general `[SeminormedCommRing R]` form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); building blocks `Finset.sum_nonneg`, `norm_nonneg` exist, but the def itself does not.

### Normal-form check — `Roth.normOne_nonneg`

Equivalent formalisms: `0 ≤ l1Norm p`; `0 ≤ ∑ d ∈ p.support, ‖p.coeff d‖`.
Does mathlib already have a canonical form for this idea? yes — `0 ≤ f x` named `f_nonneg` (e.g. `supNorm_nonneg`).
RHS convention respected? yes (`0 ≤ _`, mathlib's `_nonneg` shape).

### Syntactic generality — `Roth.normOne_nonneg`

Alternative restatements attempted:
- `0 ≤ normOne P` (current)
- `0 ≤ p.l1Norm` over `[SeminormedCommRing R]` (evidence)

Chosen restatement: the general form with explicit `p`.
Justification: the explicit argument lets it be passed as a function (`normOne_nonneg`) to `Finset.le_prod_of_submultiplicative_of_nonneg`, as at line 107.

### Superfluous-argument audit — `Roth.normOne_nonneg`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficients in `ℤ` | no | only `norm_nonneg` needed; generalise with the parent |
| 2 | `P` | yes | the polynomial |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (ℤ → `[SeminormedCommRing R]`, following the parent)
Superfluous arguments: 1 to drop (the fixed coefficient ring ℤ)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_nonneg`

Internal use count: 0 (outside the declaring file)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:107 (same file) | `Finset.le_prod_of_submultiplicative_of_nonneg normOne normOne_nonneg` |
| Roth/CoeffNorm.lean:128 (same file) | `Finset.prod_le_prod₀ (fun _ _ ↦ normOne_nonneg _) fun i _ ↦ hM _ _` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_nonneg`?):
  - (none) — no other `Finset.sum_nonneg … abs_nonneg` over `normOne` in Roth/.

### Composition check (Phase 6)

Can `Roth.normOne_nonneg` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.sum_nonneg fun _ _ ↦ norm_nonneg _` (after unfolding the def).
  - Mathlib decls used: `Finset.sum_nonneg`, `norm_nonneg` (`abs_nonneg` for ℤ)
  - Result: succeeds as a proof term
  - Notes: but the statement is about `l1Norm`, which is itself not in mathlib; the composition only works by unfolding the (new) def, so it cannot replace the lemma at call sites without exposing the def body. Mathlib's convention for norm-like defs is to ship the `_nonneg` lemma with the def (`Polynomial.supNorm_nonneg`, `gaussNorm_nonneg`, `mahlerMeasure_nonneg`).

Conclusion: NOT-COMPOSABLE (as a statement about a def mathlib lacks; the proof body is a one-call composition, which is expected of a basic API lemma)

## Verdict: `Roth.normOne_nonneg`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): nonnegativity is the first norm axiom of the length `L(P) = ∑ ‖a_e‖` (arXiv 0808.2952, Schinzel, ℓ¹ monoid-algebra norm); standard at seminormed-coefficient generality.
- Generality analysis (Phase 4): STRICTLY NARROWER (via the parent's ℤ-specialisation); `Evidence.l1Norm_nonneg` over `[SeminormedCommRing R]` compiles (diagnostics clean).
- Mathlib search (Phase 5): not in mathlib; analogues `Polynomial.supNorm_nonneg`, `Polynomial.gaussNorm_nonneg`.
- Composition check (Phase 6): NOT-COMPOSABLE as a statement (the def is new); the proof is the expected one-liner.

**Rationale:**

The parent verdict puts an ℓ¹ coefficient norm `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` into mathlib, filling the TODO in `Mathlib/Analysis/Polynomial/Norm.lean` ("the `l^1` norm is sometimes called the polynomial's _length_"). Any such def needs its nonnegativity lemma: mathlib ships one for every real-valued norm-like polynomial invariant (`supNorm_nonneg`, `gaussNorm_nonneg`, `mahlerMeasure_nonneg`, `spectralValue_nonneg`), and it is the hypothesis consumed by `Finset.le_prod_of_submultiplicative_of_nonneg` (exactly how the project uses it for `normOne_prod_le`). The current lemma is ℤ-only only because `normOne` is; the identical proof with `norm_nonneg` already compiles for the general def.

Although the lemma is a one-liner, it is a theorem (Phase 2b n/a) and a one-line `_nonneg` companion is standard mathlib API for a new def, not a wrapper consumers would bypass; its two call sites pass it as a function argument, where a named lemma is necessary.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from `Roth.normOne`.

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_nonneg {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) : 0 ≤ p.l1Norm :=
  Finset.sum_nonneg fun _ _ ↦ norm_nonneg _
```

Estimated cost of regeneralisation: CHEAP (done in the evidence file).

Mathlib downstream this enables:
- nonnegativity side conditions for `l1Norm_prod_le` (via `Finset.le_prod_of_submultiplicative_of_nonneg`) and for product bounds via `Finset.prod_le_prod₀`;
- a `positivity` extension for `l1Norm`, matching the sup/Gauss norm API.

PR grouping: ship in the same PR as `MvPolynomial.l1Norm` and its core API (`_zero`, `_monomial`, `norm_coeff_le_l1Norm`, `_add_le`, `_sum_le`, `_mul_le`).

Next action: run `/generalise Roth.normOne` (parent) and port this lemma as `MvPolynomial.l1Norm_nonneg`; keep `Roth.normOne_nonneg` (or the abbreviation's inherited lemma) at call sites Roth/CoeffNorm.lean:107 and :128.

---

## Next step

Port as `MvPolynomial.l1Norm_nonneg` together with the parent def `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (proof verbatim with `norm_nonneg`), proposed location `Mathlib/Analysis/Polynomial/Norm.lean` or a new `Mathlib/Analysis/MvPolynomial/Norm.lean`.

## Evidence
- WebSearch ×3 (length of polynomial nonneg/norm properties; ℓ¹ monoid-algebra norm; mathlib supNorm / ℓ¹ coefficient norm): standard form confirmed, no mathlib ℓ¹ norm.
- LeanSearch, Lean-Finder, Loogle queries as in the Phase 5 block: only sup/Gauss/Mahler/spectral analogues.
- Mathlib grep for `normOne`, `l1Norm`, `supNorm_nonneg`, `gaussNorm_nonneg`: `normOne` only as `NormOneClass`; `Polynomial.supNorm_nonneg` at Analysis/Polynomial/Norm.lean:66.
- Reused evidence file `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` (from the parent assessment): `Evidence.l1Norm_nonneg` at lines 22–23 over `[SeminormedCommRing R]` plus bridge `l1Norm_int_eq_normOne`; `lean_diagnostic_messages` (errors) re-run this session: none. No new evidence file written.
- ChatGPT MCP: n/a (not configured in this session).
