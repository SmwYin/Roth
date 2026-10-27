---
decl: Roth.normOne_le_card_mul
file: Roth/CoeffNorm.lean
line: 113
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Comparison length L(P) at most #support times a uniform coefficient bound (l1 at most N times sup); a one-call Finset.sum_le_card_nsmul lemma but standard norm-comparison API (cf. norm_le_card_mul_iSup_norm_inner, mahlerMeasure_le_sqrt_natDegree_add_one_mul_supNorm) for the absent l1 norm; proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing (even any CommSemiring with Norm) and recovers the Z form.
action: Ship as MvPolynomial.l1Norm_le_card_mul over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), optionally with an l1Norm_le_card_support_mul_supNorm companion; keep the Z form for the single call site Roth/CoeffNorm.lean:270 via Int.norm_eq_abs.
---

# Roth.normOne_le_card_mul

## Inventory entry

### `theorem Roth.normOne_le_card_mul`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) {B : ℝ} (hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B) : Roth.normOne P ≤ P.support.card * B`
- **What**: If every coefficient of `P` has absolute value at most `B`, then the ℓ¹ coefficient norm is at most (number of monomials) · `B`.
- **How**: One term: `simpa [normOne] using P.support.sum_le_card_nsmul _ _ (fun d _ ↦ hB d)` (mathlib's `Finset.sum_le_card_nsmul`, after unfolding `normOne`; `simp` turns `nsmul` into `*`).
- **Hypotheses**: `hB` — uniform bound on all coefficients (only used on the support).
- **Uses from project**: `Roth.normOne`
- **Used by**: Roth/CoeffNorm.lean:270 (proof of `Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3). No other uses (`grep -rn normOne_le_card_mul Roth/`).
- **Visibility**: public
- **Lines**: 110–115, proof length 1 line
- **Notes**: Formalises the source step "Pad the monomial expansion of `R` … `R = ∑_{i=1}^N α_i`, `|u_i| ≤ B`" (clean.tex:454–456), giving `‖R‖₁ ≤ N B`.

## Junk check (Step 8)
- Used anywhere? Yes, once (Lemma 3, `abs_coeff_det_hasseDeriv_le`).
- Wrapper of 1–2 mathlib calls? Yes: one `Finset.sum_le_card_nsmul` after unfolding. But this is a norm-comparison API lemma of a named norm (ℓ¹ ≤ #support · ℓ^∞), of the kind mathlib keeps for every named norm (`norm_le_card_mul_iSup_norm_inner` in Analysis/InnerProductSpace/PiL2.lean:543, `Polynomial.mahlerMeasure_le_sqrt_natDegree_add_one_mul_supNorm`). Inlining it at the single site would require unfolding `normOne`, breaking the def's abstraction.
- Does mathlib have it? No (no ℓ¹ polynomial norm; Phase 5).
- Too specific (inline)? Borderline (K = 1), but it is the natural interface lemma between the ℓ¹ norm and coefficient bounds; keeping it is the cleaner choice.
- Well-chosen? Yes, modulo the parent's ℤ / `|·|` specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm` with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_le_card_mul` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (a proof by a mathlib inequality, not `rfl`/unfolding), so a full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.normOne_le_card_mul`: resolved at Roth/CoeffNorm.lean:113
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_le_card_mul` is a theorem stating the following: let `P = ∑_e a_e X^e ∈ ℤ[X_σ]` and suppose `|a_e| ≤ B` for all `e`. Then the length (ℓ¹ coefficient norm) satisfies `L(P) ≤ N · B`, where `N` is the number of monomials of `P` (the size of its support). Equivalently `L(P) ≤ #supp(P) · H(P)` with `H` the height (sup norm).

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `P : MvPolynomial σ ℤ` — the polynomial.
- `B : ℝ` — the coefficient bound.

Hypotheses (Lean side):
- `hB : ∀ d, |((P.coeff d : ℤ) : ℝ)| ≤ B` — uniform coefficient bound.

Conclusion (math): `L(P) ≤ #supp(P) · B`.

Conclusion (Lean): `Roth.normOne P ≤ P.support.card * B`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic comparison inequality of a helper definition; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem). Note for Phase 7: the proof is one `Finset.sum_le_card_nsmul` call after unfolding the def; justification as API is addressed in Phase 7.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of polynomial L(P) ≤ (number of nonzero coefficients) × height H(P) inequality | partial | `H(P) = max |a_i|`, `L(P) = ∑ |a_i|` (Dubickas–Jankauskas; Schinzel, Funct. Approx. 35; Kieffer arXiv 2105.07670) | `L ≤ k·H` for `k` monomials not stated as a named result; immediate from the definitions; the "k monomials" setting appears in Lawton-type results |
| 2 | WebSearch (general form) | l1 norm bounded by cardinality of support times sup norm ‖x‖₁ ≤ |supp x| ‖x‖_∞ sparse vector | partial | `‖x‖₁ ≤ |supp x| · ‖x‖_∞` (folklore; companion `‖x‖₁ ≤ √|supp x| ‖x‖₂` in sparse-recovery notes) | standard norm comparison on finitely supported vectors |
| 3 | WebSearch (aliases / mathlib) | mathlib Finset.sum_le_card_nsmul polynomial length height norm comparison | yes | `Finset.sum_le_card_nsmul` (generic) | no polynomial length/height comparison in mathlib |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 454–456 | yes | "Pad the monomial expansion of `R` by zero terms and write `R=∑_{i=1}^N α_i` … `|u_i| ≤ B`" | the source's exact use: `‖R‖₁ ≤ N B` with `N = ∏(r_j+1)` |
| 6 | nLab | normed vector space / ℓ^p comparison | partial | equivalence of norms on finite-dimensional spaces, with constants depending on dimension | the constant `#support` is the sharp one for ℓ¹ vs ℓ^∞ |
| 7 | nCatLab | — | n/a | — | not a categorical statement (an elementary inequality) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length vs height of polynomials (`H ≤ L ≤ (n+1) H`) | yes | `H(P) ≤ L(P) ≤ (deg P + 1) H(P)` in univariate form | the support-cardinality form is the sharp sparse version |
| 10 | recent arXiv (last 5 years) | heights of polynomials from values (arXiv 2105.07670); 1-norm of polynomials in a basis (arXiv 2404.04190) | yes | length/height comparisons used routinely | no competing form |

### Literature summary (Phase 3)

Concept identified as: comparison `L(P) ≤ #supp(P) · H(P)` between length (ℓ¹) and height (ℓ^∞) of a polynomial; special case of `‖x‖₁ ≤ |supp x| ‖x‖_∞` for finitely supported vectors.
Sources agree on the standard form: yes — elementary; univariate texts state the weaker `L ≤ (deg+1) H`.
Most general standard form: for coefficients in any (semi)normed ring (indeed any type with a norm), `‖p‖₁ ≤ #supp(p) · B` whenever `‖coeff_e p‖ ≤ B` for `e ∈ supp p`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / normed ring; the proof needs only a real-valued function of the coefficients.
  - bound hypothesis: on all `e` vs on `e ∈ supp p` vs `B = H(P)` (sup norm).
  - counting factor: `#supp` (sharp) vs `deg+1` / `∏(r_j+1)` (box size).
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_le_card_mul`

Literature-standard form (from Phase 3): `l1Norm p ≤ #p.support * B` given `∀ d, ‖p.coeff d‖ ≤ B`, for `p : MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof only unfolds the def and applies `Finset.sum_le_card_nsmul`; verified (`Evidence86.l1Norm_le_card_mul`, verbatim proof) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | follows parent restatement; bridge `Evidence86.l1Norm_int_eq_normOne` via `Int.norm_eq_abs`; recovery `example` compiles |
| 3 | norm axioms | ring norm | none needed | yes (option) | `Evidence86.l1Norm'_le_card_mul` compiles over `[CommSemiring R] [Norm R]`; but the parent def lives over `SeminormedCommRing`, so this is moot for the API |
| 4 | `hB` on all `d` | `∀ d` | `∀ d ∈ p.support` | yes (option) | `Evidence86.l1Norm_le_card_mul'` compiles; the `∀ d` form is easier to supply and matches the call site; the support form could be the primary with `∀ d` as corollary |
| 5 | `B` sign | arbitrary `B` | arbitrary | no | no `0 ≤ B` needed (empty support gives `0 ≤ 0`) — already maximal |
| 6 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 primary (ℤ → `[SeminormedCommRing R]`), plus 2 optional (support-restricted hypothesis; no norm axioms)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_le_card_mul/general_and_composition.lean` — general `l1Norm`, `l1Norm_le_card_mul` (project proof verbatim), `l1Norm_le_card_mul'` (hypothesis on support only), ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement, a term-mode composition `example` via `Finset.sum_le_card_nsmul`/`nsmul_eq_mul`, and `l1Norm'_le_card_mul` over `[CommSemiring R] [Norm R]`; `lean_diagnostic_messages`: no diagnostics (after fixing a misplaced docstring in the first draft).
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_le_card_mul {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) {B : ℝ} (hB : ∀ d ∈ p.support, ‖p.coeff d‖ ≤ B) :
    p.l1Norm ≤ #p.support * B
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | only a numeric bound hypothesis | — |
| 2 | Sequences → filters? | no | finite inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | coefficient-bound-to-ℓ¹ step for every seminormed coefficient ring |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` ℓ¹ norm (parent's unverified option) | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | the proof uses only "sum over a finset of terms each ≤ B" — the generic `Finset.sum_le_card_nsmul`; covered by row 5 (and row 3 of Phase 4a: no norm axioms needed) | — |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_le_card_mul` over `[SeminormedCommRing R]` (above), with an optional companion `l1Norm_le_card_support_mul_supNorm`-style lemma once a multivariate sup norm exists (univariate: `Polynomial.supNorm` already exists).
  - Cost: CHEAP
  - Mathlib downstream this enables: ℓ¹ vs height comparisons next to `Polynomial.supNorm` / `le_supNorm`; feeds `mahlerMeasure_le_sum_norm_coeff`-style bounds into height bounds.
  - Real mathematical improvement: one comparison lemma for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.normOne_le_card_mul`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | — | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | uses `Finset.sum_le_card_nsmul` directly | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_le_card_mul`

[A] Lean-Finder       "l1 norm of polynomial coefficients bounded by card of support times uniform coefficient bound"  no hits (only `Polynomial.cauchyBound`, `norm_coeff_le_choose_mul_mahlerMeasure`, `mahlerMeasure_le_sum_norm_coeff`, `gaussNorm`, `card_mahlerMeasure_le_prod`)
[B] Loogle            `Finset.sum (MvPolynomial.support _) _ ≤ _`  no hits
[C] LeanSearch        "sum of norms of coefficients of polynomial at most number of nonzero coefficients times bound"  no hits (`mahlerMeasure_le_sum_norm_coeff`, `ClassGroup.norm_le`, `coeff_bdd_of_roots_le` — unrelated)
[D] Grep mathlib src  `l1Norm`, `le_card_mul`, `_le_card_nsmul`, `supNorm` lemmas in Analysis/Polynomial/  no ℓ¹ polynomial norm; ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34-38; precedent comparison lemmas `norm_le_card_mul_iSup_norm_inner` (InnerProductSpace/PiL2.lean:543), `mahlerMeasure_le_sqrt_natDegree_add_one_mul_supNorm` (Polynomial/MahlerMeasure.lean:346)
[E] Name pattern      `lean_local_search l1Norm_le_card`  not run separately (tool returns index-dependent results; as in sibling reports); covered by grep [D]

Searched for both:
  - the user's current form (ℤ, `|·|`)
  - the literature-standard form (ℓ¹ ≤ #support · bound over a seminormed ring)

Concluded: not in mathlib (all methods exhausted); building block `Finset.sum_le_card_nsmul` exists but the needed `l1Norm` does not.

### Normal-form check — `Roth.normOne_le_card_mul`

Equivalent formalisms: `l1Norm p ≤ #p.support * B` (bound hypothesis); `l1Norm p ≤ #p.support * supNorm p` (sup-norm form, needs a multivariate sup norm); `l1Norm p ≤ #p.support • B`.
Does mathlib already have a canonical form? For comparisons, mathlib uses the `X ≤ card * Y` shape with `*` (e.g. `norm_le_card_mul_iSup_norm_inner`, `Finset.card_biUnion_le_card_mul`). Our statement matches. RHS convention: n/a (inequality).

### Syntactic generality — `Roth.normOne_le_card_mul`

Alternative restatements attempted:
- `(hB : ∀ d, ‖p.coeff d‖ ≤ B)` (current)
- `(hB : ∀ d ∈ p.support, ‖p.coeff d‖ ≤ B)` (weaker hypothesis, compiled)
- sup-norm form `l1Norm p ≤ #p.support * supNorm p` (no hypothesis)
Chosen restatement: the support-restricted hypothesis as the primary (strictly more applicable; `fun d _ ↦ hB d` recovers the current form). Justification: it is what `Finset.sum_le_card_nsmul` takes natively, and callers with a global bound pass `fun d _ ↦ hB d`; the sup-norm form becomes a corollary once a multivariate sup norm exists.

### Superfluous-argument audit — `Roth.normOne_le_card_mul`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ : Type*` | yes | index type |
| 2 | `P` | yes | — |
| 3 | `B`, `hB` | yes (only on the support) | weaken to `∀ d ∈ p.support` |
| 4 | ℤ coefficients (via `normOne`) | no | generalise with parent to `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (hypothesis on the support only)
Superfluous arguments: 1 to drop (ℤ specialisation, via parent def)

Overall: RESTATE-BEFORE-SHIP (state against `MvPolynomial.l1Norm` with `‖·‖`, hypothesis on support; name `l1Norm_le_card_mul`)

### Call sites — `Roth.normOne_le_card_mul`

Internal use count: 0 outside the declaring file; 1 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:270 | `((normOne_le_card_mul P hB).trans (mul_le_mul_of_nonneg_right hsupp hB0))` (`abs_coeff_det_hasseDeriv_le`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_le_card_mul`?):
  - (none; no other `sum_le_card_nsmul` on a `normOne` sum in `Roth/`).

### Composition check (Phase 6)

Can `Roth.normOne_le_card_mul` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(p.support.sum_le_card_nsmul _ _ fun d _ ↦ hB d).trans_eq (nsmul_eq_mul _ _)` (after unfolding the def)
  - Mathlib decls used: `Finset.sum_le_card_nsmul`, `nsmul_eq_mul`
  - Result: succeeds (compiled in the evidence file for `l1Norm`) — but only by unfolding the ℓ¹ norm definition, which itself is not in mathlib. From mathlib alone there is no ℓ¹ polynomial norm to state it about.
  - Notes: once `l1Norm` exists in mathlib, this is the kind of one-line comparison API lemma mathlib keeps (consumers should not unfold a named norm).

Attempt 2: via a mathlib ℓ¹ norm on `Finsupp` / `lp` / `PiLp 1` and a norm comparison
  - Result: fails — no norm instance on `σ →₀ R` / `AddMonoidAlgebra`; `PiLp 1` needs a finite index type (parent Phase 6).

Conclusion: NOT-COMPOSABLE from mathlib alone (composable in one call after unfolding the companion def that would ship in the same PR).

## Verdict: `Roth.normOne_le_card_mul`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): length ≤ #monomials · height, the sharp sparse form of `L ≤ (deg+1) H`; used verbatim by the source (clean.tex:454–456).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via parent def); general form compiled verbatim, plus support-restricted and norm-axiom-free variants.
- Mathlib search (Phase 5): not in mathlib (no ℓ¹ polynomial norm; Norm.lean ℓ¹ TODO).
- Composition check (Phase 6): NOT-COMPOSABLE from mathlib alone (one call given the companion def).

**Rationale:**

Mathlib has no ℓ¹ coefficient norm on `Polynomial`/`MvPolynomial`/`Finsupp` (`Mathlib/Analysis/Polynomial/Norm.lean` lists the ℓ¹ "length" as a TODO next to the existing `Polynomial.supNorm`), so this lemma cannot exist there yet; it belongs to the API of the parent's proposed `MvPolynomial.l1Norm`. The proof is a single `Finset.sum_le_card_nsmul` after unfolding, and it has one consumer (Lemma 3, `abs_coeff_det_hasseDeriv_le`). It is still worth shipping as API because it is the standard length-vs-height comparison (the ℓ¹ ≤ #support · ℓ^∞ inequality), mathlib keeps such comparison lemmas for its named norms (`norm_le_card_mul_iSup_norm_inner`, `mahlerMeasure_le_sqrt_natDegree_add_one_mul_supNorm`), and the alternative — unfolding `l1Norm` at use sites — breaks the abstraction of a named norm. The evidence file shows the proof goes through verbatim over `[SeminormedCommRing R]`, recovers the ℤ statement via `Int.norm_eq_abs`, and that the hypothesis is only needed on the support.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from the parent; plus the support-restricted hypothesis (Phase 5.5).

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_le_card_mul {σ R : Type*} [SeminormedCommRing R]
    (p : MvPolynomial σ R) {B : ℝ} (hB : ∀ d ∈ p.support, ‖p.coeff d‖ ≤ B) :
    p.l1Norm ≤ #p.support * B := by
  simpa [l1Norm] using p.support.sum_le_card_nsmul _ _ hB
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- the coefficient-bound → ℓ¹ step in any height/length estimate (Siegel-lemma and Roth/Thue-type size bounds) over any seminormed coefficient ring;
- with a univariate companion, `Polynomial.l1Norm_le_card_support_mul_supNorm` next to `Polynomial.le_supNorm`, closing part of the ℓ¹ TODO in Norm.lean.

PR grouping: ship with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_eq_sum_of_support_subset`, `l1Norm_monomial`, `l1Norm_zero`, `norm_coeff_le_l1Norm`, `l1Norm_add_le`, `l1Norm_neg`, `l1Norm_sum_le`, `l1Norm_mul_le`, `l1Norm_prod_le`) as one PR.

Next action: run `/generalise Roth.normOne_le_card_mul` together with the parent `/generalise Roth.normOne`, restate as `MvPolynomial.l1Norm_le_card_mul` (hypothesis on the support), and keep the ℤ form (via `Int.norm_eq_abs`, passing `fun d _ ↦ hB d`) at its call site Roth/CoeffNorm.lean:270.

---

## Next step

Restate as `MvPolynomial.l1Norm_le_card_mul` over `[SeminormedCommRing R]` in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), with the project call site Roth/CoeffNorm.lean:270 using the ℤ specialisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_le_card_mul/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): general `l1Norm`, `l1Norm_le_card_mul` (verbatim one-line proof), `l1Norm_le_card_mul'` (support-restricted hypothesis), ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement, term-mode composition `example`, and `l1Norm'_le_card_mul` over `[CommSemiring R] [Norm R]`; `lean_diagnostic_messages`: first draft had a parse error (docstring before `variable`), fixed to a comment; final check no diagnostics.
- Mathlib greps: `le_card_mul` / `_le_card_nsmul` theorem names (precedent `norm_le_card_mul_iSup_norm_inner`), `supNorm`/`sum_norm` lemmas in Analysis/Polynomial (no ℓ¹ norm), ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34-38.
- LeanSearch / Lean-Finder / Loogle queries as in Phase 5 (no hit).
- WebSearch ×3 (length vs #monomials·height; ℓ¹ ≤ |supp|·ℓ^∞; mathlib sum_le_card_nsmul polynomial norms); local reference clean.tex lines 454–456.
- ChatGPT MCP: n/a (not configured in this session).
