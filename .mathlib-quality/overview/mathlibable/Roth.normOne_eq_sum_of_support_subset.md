---
decl: Roth.normOne_eq_sum_of_support_subset
file: Roth/CoeffNorm.lean
line: 54
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Standard support-enlargement API lemma for the l1 coefficient norm (analogue of Polynomial.sum_eq_of_subset and Finsupp.sum_of_support_subset); mathlib has no l1 polynomial norm, and the same proof compiles for MvPolynomial.l1Norm over any SeminormedCommRing (evidence file, diagnostics clean).
action: Ship as MvPolynomial.l1Norm_eq_sum_of_support_subset over [SeminormedCommRing R] in the same PR as MvPolynomial.l1Norm (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the R = ℤ form for the call sites Roth/CoeffNorm.lean:61, 79, 80, 81.
---

# Roth.normOne_eq_sum_of_support_subset

## Inventory entry

### `theorem Roth.normOne_eq_sum_of_support_subset`
- **Type**: `{σ : Type*} {P : MvPolynomial σ ℤ} {s : Finset (σ →₀ ℕ)} (hs : P.support ⊆ s) : Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)|`
- **What**: The ℓ¹ coefficient norm `‖P‖₁ = ∑_{d ∈ supp P} |a_d|` may be computed as a sum over any finite set of exponents `s` containing the support.
- **How**: Term proof `Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]` (the extra summands vanish because their coefficients are zero).
- **Hypotheses**: `hs : P.support ⊆ s`.
- **Uses from project**: `Roth.normOne`
- **Used by**: Roth/CoeffNorm.lean:61 (`normOne_monomial`, with `support_monomial_subset`), Roth/CoeffNorm.lean:79, 80, 81 (`normOne_add_le`, three rewrites to put `P + Q`, `P`, `Q` over `P.support ∪ Q.support`). No uses outside CoeffNorm.lean (`grep -rn normOne_eq_sum_of_support_subset Roth/`).
- **Visibility**: public
- **Lines**: 52–56, proof length 1 line
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, 4 rewrite call sites in CoeffNorm.lean (61, 79, 80, 81); three of them in one `rw` chain where a named rewrite lemma is clearly better than re-deriving `Finset.sum_subset` three times.
- Wrapper of 1–2 mathlib calls? Yes (`Finset.sum_subset` + `simp`), but it is the standard API companion of a named sum-over-support def; mathlib ships exactly this shape for `Polynomial.sum` (`Polynomial.sum_eq_of_subset`), `Finsupp.sum` (`Finsupp.sum_of_support_subset`) and `finsum` (`finsum_eq_sum_of_support_subset`).
- Does mathlib have it? No — mathlib has no ℓ¹ polynomial norm (parent `Roth.normOne`); only the generic `Finsupp.sum` analogue.
- Too specific (inline)? No; inlining would repeat the `Finset.sum_subset` side proof at each of the 4 call sites.
- Well-chosen? Yes, modulo the parent's ℤ-specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at the generalised `MvPolynomial.l1Norm` together with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_eq_sum_of_support_subset` not in mathlib (no `namespace Roth` in Mathlib). Not a glue lemma (body is `Finset.sum_subset` with a vanishing side-proof, not `rfl`/unfolding), so a full run, assessed in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to an ℓ¹ norm on `MvPolynomial σ R`, `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence files importing `Roth.CoeffNorm` elaborate with no errors per `lean_diagnostic_messages`)
- decl `Roth.normOne_eq_sum_of_support_subset`: resolved at Roth/CoeffNorm.lean:54
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_eq_sum_of_support_subset` is a theorem stating the following: let `P ∈ ℤ[X_σ]` and let `s` be a finite set of exponent vectors containing every exponent `d` with nonzero coefficient `a_d`. Then the length `‖P‖₁ = ∑_{d ∈ supp P} |a_d|` equals `∑_{d ∈ s} |a_d|`, since the additional terms are `|0| = 0`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `P : MvPolynomial σ ℤ` — the polynomial.
- `s : Finset (σ →₀ ℕ)` — a finite set of exponents.

Hypotheses (Lean side):
- `hs : P.support ⊆ s` — `s` contains the support.

Conclusion (math): `‖P‖₁ = ∑_{d ∈ s} |a_d|`.

Conclusion (Lean): `Roth.normOne P = ∑ d ∈ s, |((P.coeff d : ℤ) : ℝ)|`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic computational API lemma for a helper definition; not a structure, not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE-check skipped (theorem). Note for Phase 7: support-enlargement lemmas are standard one-line API in mathlib (`Polynomial.sum_eq_of_subset`).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of a polynomial sum of absolute values of coefficients over any finite set containing support | partial | `L(P) = ∑ |a_i|` (length); no named support-enlargement statement | Dobrowolski–Smyth (arXiv 1606.04376), arXiv 1410.0912; the identity is treated as trivial |
| 2 | WebSearch (general form) | l1 norm finitely supported function sum over finite set containing support extend by zero | yes | for `f ∈ c₀₀(X,V) ⊂ ℓ¹`, `‖f‖₁ = ∑_{supp f} ‖f(x)‖` = sum over any finite superset | arXiv 1009.1107 (c₀₀ inside ℓ¹); mathlib `lp` docs |
| 3 | WebSearch (aliases / mathlib) | mathlib Finsupp.sum_of_support_subset polynomial coefficient norm sum_over_range | yes | `Finsupp.sum_of_support_subset`, `Finsupp.prod_of_support_subset`, `Polynomial.supp_subset_range` | the generic Finsupp form; no norm-specific lemma |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` (via parent report) | yes | `‖f‖₁ = ∑_e |a_e|` | source uses support-union sums implicitly in the triangle inequality of Lemma 3 |
| 6 | nLab | ℓ¹ / group algebra (via parent) | yes | ℓ¹(G) normed algebra | no polynomial-specific statement; identity is part of finite-support sums |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum identity) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomial L(PQ) ≤ L(P)L(Q) (via parent) | yes | same `L(P)` | support enlargement used silently in the proofs |
| 10 | recent arXiv (last 5 years) | ℓ¹ coefficient norm height bounds (via #1) | yes | same | no competing form |

### Literature summary (Phase 3)

Concept identified as: the ℓ¹ (length) norm of a finitely supported coefficient function is the finite sum of coefficient norms over any finite superset of the support ("extension by zero").
Sources agree on the standard form: yes — trivial identity, used silently.
Most general standard form: for any finitely supported `f : M →₀ R` into a seminormed group, `∑_{supp f} ‖f m‖ = ∑_{m ∈ s} ‖f m‖` for `supp f ⊆ s`; specialised to `MvPolynomial σ R` over `[SeminormedCommRing R]`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℂ / any (semi)normed ring; most general is seminormed.
  - index set: ℕ, ℕ^σ, arbitrary monoid.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_eq_sum_of_support_subset`

Literature-standard form (from Phase 3): `l1Norm p = ∑ d ∈ s, ‖p.coeff d‖` for `p.support ⊆ s`, `p : MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof uses only `‖0‖ = 0` (`simp`); verified (Evidence2.l1Norm_eq_sum_of_support_subset) |
| 2 | `|((·:ℤ):ℝ)|` | absolute value of real cast | `‖·‖` | yes | follows the parent's restatement; bridge via `Int.norm_eq_abs` compiled |
| 3 | `hs : P.support ⊆ s` | subset | subset | no | necessary: a set missing a support point drops a positive term |
| 4 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited solely from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 (ℤ → `[SeminormedCommRing R]` via the parent def)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_eq_sum_of_support_subset/composition_and_general.lean` proves `Evidence2.l1Norm_eq_sum_of_support_subset` over `[SeminormedCommRing R]` with the verbatim proof, a composition variant `l1Norm_eq_sum_of_support_subset'`, and an `example` recovering the exact project statement for `R = ℤ`; `lean_diagnostic_messages`: no diagnostics. The parent evidence file `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` (lines 25–27) also contains the general lemma and was re-checked clean this session.
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_eq_sum_of_support_subset {σ R : Type*} [SeminormedCommRing R]
    {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)} (hs : p.support ⊆ s) :
    p.l1Norm = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | only a subset hypothesis | — |
| 2 | Sequences → filters? | no | finite sum identity | — |
| 3 | Construction → universal property? | no | an equation | — |
| 4 | Set predicate → bundled substructure? | no | `Finset` subset is the idiomatic form (cf. `Polynomial.sum_eq_of_subset`) | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | general triangle/monomial lemmas for `l1Norm` |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` version (parent's unverified option) | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only that absent coefficients are `0` and `‖0‖ = 0`; covered by row 5; if `l1Norm` is phrased as `Finsupp.sum`, it is literally `Finsupp.sum_of_support_subset` (compiled) | same proof for all coefficient rings |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_eq_sum_of_support_subset` over `[SeminormedCommRing R]` (above), mirroring `Polynomial.sum_eq_of_subset`.
  - Cost: CHEAP
  - Mathlib downstream this enables: the standard route to `l1Norm_add_le` (sum over `p.support ∪ q.support`), `l1Norm_monomial` (via `support_monomial_subset`), and degree-box bounds (`s = Finset.range`-type boxes) for any normed coefficient ring.
  - Real mathematical improvement: one support-enlargement lemma for every seminormed coefficient ring rather than a ℤ copy.

### Proof strategy — `Roth.normOne_eq_sum_of_support_subset`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ vs filters? | no | — | — |
| 2 | Element-wise vs point-free algebra? | no | — | — |
| 3 | Sequences vs filters? | no | — | — |
| 4 | Construction vs universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | `Finset.sum_subset` (or `Finsupp.sum_of_support_subset`) suffices | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_eq_sum_of_support_subset`

[A] Lean-Finder       "sum of norms of coefficients of a multivariate polynomial can be computed over any finset containing the support"   hits `Polynomial.sum_eq_of_subset` (generic `Polynomial.sum`), `MvPolynomial.sum_def`, `Polynomial.sum_def`; no norm-specific lemma
[B] Loogle            `Finsupp.sum, Finset.sum, "support_subset"`   single hit `Finsupp.sum_of_support_subset` (generic building block)
[C] LeanSearch        "sum over support of finsupp equals sum over any finset containing the support"   hits `Finsupp.onFinset_sum`, `finsum_eq_sum_of_support_subset`, `finsum_mem_eq_sum_of_subset`; no ℓ¹-norm lemma
[D] Grep mathlib src  `l1Norm`, `normOne_eq_sum`, `support_subset.*‖` in `Analysis/Polynomial/`; TODO block of `Analysis/Polynomial/Norm.lean`   no hits; Norm.lean lines 31–37 list the ℓ¹ norm ("length") as a TODO
[E] Name pattern      `l1Norm_eq_sum_of_support_subset`, `normOne_eq_sum_of_support_subset`   none in mathlib (only project/evidence decls)

Searched for both the ℤ form and the general `[SeminormedCommRing R]` form.

Concluded: found building blocks (`Finset.sum_subset`, `Finsupp.sum_of_support_subset`, `MvPolynomial.sum_def`, `MvPolynomial.notMem_support_iff`); the statement concerns a def (`l1Norm`) not in mathlib.

### Normal-form check — `Roth.normOne_eq_sum_of_support_subset`

Equivalent formalisms: `l1Norm p = ∑ d ∈ s, ‖p.coeff d‖` (given `hs`); `(coeff p).sum (fun _ a ↦ ‖a‖) = ∑ d ∈ s, ‖p.coeff d‖`.
Does mathlib already have a canonical form for this idea? yes — `Polynomial.sum_eq_of_subset` / `Finsupp.sum_of_support_subset`: `named_sum = ∑ x ∈ s, g x (f x)` with the subset hypothesis.
RHS convention respected? yes (defined quantity on the LHS, explicit finite sum on the RHS, matching the mathlib analogues).

### Syntactic generality — `Roth.normOne_eq_sum_of_support_subset`

Alternative restatements attempted:
- current form with implicit `P`, `s` and explicit `hs` (current)
- version taking `s` explicitly
- version with `∑ d ∈ s, ‖coeff d p‖` written via `Finsupp.sum`

Chosen restatement: implicit `p`, `s`, explicit `hs`, finite `Finset.sum` on the RHS.
Justification: call sites pass `hs` and occasionally `(s := …)` by name (lines 79–81), which works with implicit `s`; matches `Finsupp.sum_of_support_subset`'s style.

### Superfluous-argument audit — `Roth.normOne_eq_sum_of_support_subset`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | coefficients in `ℤ` | no | only `‖0‖ = 0` needed; generalise with the parent |
| 2 | `hs` | yes | conclusion fails otherwise |
| 3 | `P`, `s` | yes | data |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (ℤ → `[SeminormedCommRing R]`, following the parent)
Superfluous arguments: 1 to drop (the fixed coefficient ring ℤ)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_eq_sum_of_support_subset`

Internal use count: 0 (outside the declaring file); 4 inside CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:61 (same file) | `rw [normOne_eq_sum_of_support_subset support_monomial_subset]` |
| Roth/CoeffNorm.lean:79 (same file) | `rw [normOne_eq_sum_of_support_subset support_add,` |
| Roth/CoeffNorm.lean:80 (same file) | `normOne_eq_sum_of_support_subset (s := P.support ∪ Q.support) Finset.subset_union_left,` |
| Roth/CoeffNorm.lean:81 (same file) | `normOne_eq_sum_of_support_subset (s := P.support ∪ Q.support) Finset.subset_union_right,` |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_eq_sum_of_support_subset`?):
  - (none) — the only `Finset.sum_subset` in CoeffNorm.lean is the lemma's own proof (line 56).

### Composition check (Phase 6)

Can `Roth.normOne_eq_sum_of_support_subset` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]` (after unfolding).
  - Mathlib decls used: `Finset.sum_subset`, `MvPolynomial.notMem_support_iff`
  - Result: succeeds (it is the current proof)
  - Notes: requires unfolding the new def.

Attempt 2: `rw [l1Norm, ← MvPolynomial.sum_def]; exact Finsupp.sum_of_support_subset (AddMonoidAlgebra.coeff p) hs _ fun _ _ ↦ norm_zero`.
  - Mathlib decls used: `MvPolynomial.sum_def`, `Finsupp.sum_of_support_subset`, `norm_zero`
  - Result: succeeds (compiled as `Evidence2.l1Norm_eq_sum_of_support_subset'`)
  - Notes: again only after unfolding the def mathlib lacks.

Conclusion: NOT-COMPOSABLE (as a statement about `l1Norm`, which is new; the proof is a one-call composition, as expected of a basic API lemma — exactly how mathlib's own `Polynomial.sum_eq_of_subset` is a companion of `Polynomial.sum`)

## Verdict: `Roth.normOne_eq_sum_of_support_subset`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the ℓ¹/length norm of a finitely supported coefficient function is a finite sum over any superset of the support (c₀₀ ⊂ ℓ¹; length `L(P)`); standard at seminormed-coefficient generality.
- Generality analysis (Phase 4): STRICTLY NARROWER (via the parent's ℤ-specialisation); `Evidence2.l1Norm_eq_sum_of_support_subset` over `[SeminormedCommRing R]` compiles with diagnostics clean, plus a bridge `example` back to the project statement.
- Mathlib search (Phase 5): not in mathlib; generic analogues `Polynomial.sum_eq_of_subset`, `Finsupp.sum_of_support_subset`.
- Composition check (Phase 6): NOT-COMPOSABLE as a statement (the def is new); the proof is a one-call composition.

**Rationale:**

The parent verdict puts an ℓ¹ coefficient norm `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` into mathlib, filling the TODO in `Mathlib/Analysis/Polynomial/Norm.lean` (lines 31–37, the ℓ¹ norm as the polynomial's "length"). A support-enlargement lemma is the standard computational interface for any sum-over-support def: mathlib provides `Polynomial.sum_eq_of_subset` for `Polynomial.sum` and `Finsupp.sum_of_support_subset` for `Finsupp.sum`, and the project uses this lemma four times to derive the triangle inequality and the monomial formula, which are themselves part of the parent's core API. The ℤ restriction comes only from the parent def; the identical proof compiles for the general def.

The lemma is a one-line theorem (Phase 2b n/a). A one-line companion for a new def is normal mathlib API, not a wrapper that callers skip: it is used at all four call sites and nowhere re-derived inline. If the general def is phrased as `(coeff p).sum fun _ a ↦ ‖a‖` (like the inline sum in `Polynomial.mahlerMeasure_le_sum_norm_coeff`), the lemma becomes a two-call composition of `MvPolynomial.sum_def` and `Finsupp.sum_of_support_subset`. That composition compiles, but it still has to be written down once as a named lemma about `l1Norm`.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from `Roth.normOne`.

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_eq_sum_of_support_subset {σ R : Type*} [SeminormedCommRing R]
    {p : MvPolynomial σ R} {s : Finset (σ →₀ ℕ)} (hs : p.support ⊆ s) :
    p.l1Norm = ∑ d ∈ s, ‖p.coeff d‖ :=
  Finset.sum_subset hs fun d _ hd ↦ by simp [notMem_support_iff.1 hd]
```

Estimated cost of regeneralisation: CHEAP (done in the evidence file).

Mathlib downstream this enables:
- `l1Norm_add_le` (sum over `p.support ∪ q.support` with `support_add`), `l1Norm_monomial` (with `support_monomial_subset`), and degree-box bounds for any normed coefficient ring;
- parallels `Polynomial.sum_eq_of_subset` for the univariate companion next to `Polynomial.supNorm`.

PR grouping: ship in the same PR as `MvPolynomial.l1Norm` and its core API (`_nonneg`, `_zero`, `_monomial`, `norm_coeff_le_l1Norm`, `_add_le`, `_sum_le`, `_mul_le`).

Next action: run `/generalise Roth.normOne` (parent) and port this lemma as `MvPolynomial.l1Norm_eq_sum_of_support_subset`; keep the ℤ form (or the abbreviation's inherited lemma) at call sites Roth/CoeffNorm.lean:61, 79, 80, 81.

---

## Next step

Port as `MvPolynomial.l1Norm_eq_sum_of_support_subset` together with the parent def `MvPolynomial.l1Norm` over `[SeminormedCommRing R]` (proof verbatim), proposed location `Mathlib/Analysis/Polynomial/Norm.lean` or a new `Mathlib/Analysis/MvPolynomial/Norm.lean`.

## Evidence
- WebSearch ×3 (length of polynomial over a superset of the support; ℓ¹ norm of finitely supported functions / extension by zero; mathlib `Finsupp.sum_of_support_subset` and polynomial coefficient norms): standard form confirmed, no mathlib ℓ¹ norm. Sources: https://www.arxiv.org/pdf/1606.04376, https://ar5iv.arxiv.org/html/1410.0912, https://arxiv.org/pdf/1009.1107, https://math.iisc.ac.in/~gadgil/proofs-and-programs-2023/doc/Mathlib/Algebra/BigOperators/Finsupp.html
- Lean-Finder, Loogle, LeanSearch queries as in the Phase 5 block: only generic `Polynomial.sum_eq_of_subset`, `Finsupp.sum_of_support_subset`, `finsum_eq_sum_of_support_subset`.
- Mathlib grep: no `l1Norm`; ℓ¹ norm listed as TODO in `Mathlib/Analysis/Polynomial/Norm.lean`; `MvPolynomial.sum_def` at `Mathlib/Algebra/MvPolynomial/Basic.lean:519`.
- New evidence file `.mathlib-quality/overview/evidence/Roth.normOne_eq_sum_of_support_subset/composition_and_general.lean`: general lemma over `[SeminormedCommRing R]`, Finsupp-composition variant, and `R = ℤ` bridge `example`. `lean_diagnostic_messages` reports no diagnostics. Two earlier drafts of the composition variant failed because `MvPolynomial` is no longer defeq to a `Finsupp`; passing `AddMonoidAlgebra.coeff p` fixed it.
- Parent evidence `.mathlib-quality/overview/evidence/Roth.normOne/generalise_seminormedring.lean` re-checked: no errors.
- ChatGPT MCP: n/a (not configured in this session).
