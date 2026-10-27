---
decl: Roth.normOne_det_le
file: Roth/CoeffNorm.lean
line: 119
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Leibniz bound n! C^n for the l1 coefficient norm of a determinant is absent from mathlib (Matrix.det_le needs a multiplicative AbsoluteValue, which the l1 norm is not; no l1 polynomial norm exists); the project proof compiles verbatim for MvPolynomial over any SeminormedCommRing with NormOneClass and any Fintype index, and its abstract companion norm_det_le for any SeminormedCommRing with NormOneClass also compiles (evidence clean).
action: Ship Matrix.norm_det_le [SeminormedCommRing R] [NormOneClass R] (Fintype n) in Mathlib/Analysis/Matrix/Normed.lean (or beside Matrix.det_le in LinearAlgebra/Matrix/AbsoluteValue.lean with an Analysis import) and MvPolynomial.l1Norm_det_le in the MvPolynomial.l1Norm PR; keep the Z/Fin l form for the call site Roth/CoeffNorm.lean:268 (abs_coeff_det_hasseDeriv_le).
---

# Roth.normOne_det_le

## Inventory entry

### `theorem Roth.normOne_det_le`
- **Type**: `{σ : Type*} {l : ℕ} (M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)) {C : ℝ} (hM : ∀ μ ν, Roth.normOne (M μ ν) ≤ C) : Roth.normOne M.det ≤ l.factorial * C ^ l`
- **What**: If every entry of an `l × l` matrix of integer multivariate polynomials has ℓ¹ coefficient norm at most `C`, then its determinant has ℓ¹ norm at most `l! C^l`.
- **How**: Expands `Matrix.det_apply'` (Leibniz formula with `ε σ = ((sign σ : ℤ) : R)`), bounds the sum by `Roth.normOne_sum_le`, each term by case-splitting `Int.units_eq_one_or (sign τ)` and using `Roth.normOne_neg`, `Roth.normOne_prod_le` and `Finset.prod_le_prod₀` with `hM`; finally `Fintype.card_perm` counts the `l!` permutations.
- **Hypotheses**: `hM` — uniform entrywise ℓ¹ bound `C` (no sign condition needed on `C`).
- **Uses from project**: `Roth.normOne`, `Roth.normOne_sum_le`, `Roth.normOne_neg`, `Roth.normOne_prod_le`, `Roth.normOne_nonneg`
- **Used by**: Roth/CoeffNorm.lean:268 (`Roth.abs_coeff_det_hasseDeriv_le`, Lemma 3); mentioned in the module docstring (CoeffNorm.lean:27). No other uses (`grep -rn normOne_det_le Roth/`).
- **Visibility**: public
- **Lines**: 117–128, proof length 9 lines
- **Notes**: Listed under `## Main results` of the module docstring. Stated for `Fin l` only; the proof works for any `Fintype n`.

## Junk check (Step 8)
- Used anywhere? Yes: Lemma 3 (`abs_coeff_det_hasseDeriv_le`, CoeffNorm.lean:268).
- Wrapper of 1–2 mathlib calls? No — a genuine 9-line Leibniz estimate; mathlib's analogue `Matrix.det_le` (Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean:42) does not apply because it requires an `AbsoluteValue` (multiplicative), while `normOne` is only submultiplicative.
- Does mathlib have it? No (leansearch / Lean-Finder return only `Matrix.det_le`, `det_sum_le`, `det_sum_smul_le`; loogle `‖Matrix.det _‖ ≤ _` returns nothing).
- Too specific (inline)? No; it is the natural determinant estimate of the source (clean.tex:483) and a main result of the file.
- Well-chosen? Yes, modulo the parent's ℤ specialisation and the `Fin l` index.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm_det_le` plus the abstract `Matrix.norm_det_le`.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_det_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma. Full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`) and siblings `normOne_sum_le`, `normOne_neg`, `normOne_mul_le`, `normOne_prod_le` (all YES-but-generalise-first).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` compiles with no output)
- decl `Roth.normOne_det_le`: resolved at Roth/CoeffNorm.lean:119
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_det_le` is a theorem stating the following: let `M = (P_{μν})` be an `l × l` matrix with entries in `ℤ[X_σ]` and suppose each entry has length `L(P_{μν}) = ∑ |coeff|` at most `C`. Then `L(det M) ≤ l! · C^l`. It is the Leibniz-formula estimate (each of the `l!` signed products has length at most `C^l` by submultiplicativity) for the ℓ¹ norm on the monoid algebra `ℤ[ℕ^(σ)]`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables of the polynomial ring.
- `l : ℕ` — matrix size (index type `Fin l`).
- `M : Matrix (Fin l) (Fin l) (MvPolynomial σ ℤ)` — the matrix.
- `C : ℝ` — entry bound.

Hypotheses (Lean side):
- `hM : ∀ μ ν, normOne (M μ ν) ≤ C` — entrywise ℓ¹ bound.

Conclusion (math): `L(det M) ≤ l! C^l`.

Conclusion (Lean): `Roth.normOne M.det ≤ l.factorial * C ^ l`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a standard estimate for a helper norm; listed among the file's main results but not a main result of the project, not a new structure, not a named theorem.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 9
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: MULTI-LINE (check skipped, theorem).

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | determinant bound n! B^n polynomial entries length sum of absolute values of coefficients Leibniz formula | partial | `|det A| ≤ n! B^n` from Leibniz (EPFL discrete-optimisation notes 04); no source states the polynomial-length version | the polynomial case is the same counting with a submultiplicative norm |
| 2 | WebSearch (general form) | determinant inequality submultiplicative norm Banach algebra `|det A| ≤ n! max |a_ij|^n` | partial | n! M^n holds term-by-term for any submultiplicative norm (commutative setting); Hadamard bounds need inner products and do not transfer | confirms the abstract form is "norm on a seminormed commutative ring" |
| 3 | WebSearch (named-after / aliases) | Hadamard bound determinant polynomial matrix coefficient size Roth's lemma Wronskian height bound | yes | Hadamard `|det| ≤ B^n n^{n/2}` (sharper, Euclidean only); used with coefficient vectors for Wronskian heights (arXiv 2510.00892); Roth's lemma survey arXiv 2502.00731 | Hadamard is a different (Euclidean, archimedean) bound; Leibniz n! C^n is the one valid for arbitrary seminorms |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 441, 483, 487 | yes | `‖det(...)‖₁ ≤ ∑_σ ‖∏ ...‖₁ ≤ l!(B 2^S)^l` | exactly this lemma; uses the entrywise ℓ¹ bound |
| 6 | nLab | determinant | partial | Leibniz formula as signed sum over permutations; no norm estimates | — |
| 7 | nCatLab | — | n/a | — | not a categorical statement |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | Leibniz determinant bound n! max entry, vs Hadamard | yes | folklore `|det| ≤ n! M^n`, superseded by Hadamard in Euclidean settings | same as #1/#2 |
| 10 | recent arXiv (last 5 years) | arXiv 2301.06586 (determinant formulas), 2510.00892 (Hadamard on polynomial-coefficient determinants) | partial | Leibniz/Hadamard bounds as tools | no competing form for seminormed rings |

### Literature summary (Phase 3)

Concept identified as: the Leibniz (trivial) determinant bound `‖det A‖ ≤ n! (max ‖a_ij‖)^n`, specialised to the length / ℓ¹ coefficient norm of polynomials.
Sources agree on the standard form: yes.
Most general standard form: for any commutative ring with a submultiplicative seminorm `‖·‖` satisfying `‖1‖ ≤ 1` (so `‖±x‖ = ‖x‖` and the empty product is fine), an `n × n` matrix with `‖a_ij‖ ≤ C` has `‖det A‖ ≤ n! C^n`. Hadamard's sharper `n^{n/2}` bound needs a Euclidean structure and is a separate result.
Generality dimensions where the literature varies:
  - norm: absolute value (multiplicative; mathlib `Matrix.det_le`) / submultiplicative seminorm (our case) / Euclidean (Hadamard).
  - coefficient ring: ℤ / ℝ / ℂ / any seminormed commutative ring.
  - index type: `{1,…,n}` / any finite type.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation and the `Fin l` index.

### Generality analysis — `Roth.normOne_det_le`

Literature-standard form (from Phase 3): `l1Norm M.det ≤ (card n)! * C ^ card n` for `M : Matrix n n (MvPolynomial σ R)`, `[Fintype n] [DecidableEq n] [SeminormedCommRing R] [NormOneClass R]`; and abstractly `‖M.det‖ ≤ (card n)! * C ^ card n` for `M : Matrix n n R`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | project proof verbatim with `l1Norm_*`; verified (`Evidence87.l1Norm_det_le`) |
| 2 | norm of `1` | automatic for ℤ | `[NormOneClass R]` | needed | used through `l1Norm_prod_le` (empty-product / `l = 0` case: `det` of the empty matrix is `1`, `l1Norm 1 = ‖1‖`) |
| 3 | index type | `Fin l` | `[Fintype n] [DecidableEq n]` | yes | proof never uses `Fin`; verified with `Fintype.card n` (`Evidence87.l1Norm_det_le`), matching `Matrix.det_le` |
| 4 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | bridge `Evidence87.l1Norm_int_eq_normOne`; recovery `example` compiles |
| 5 | the polynomial norm itself | ℓ¹ on `MvPolynomial` | any submultiplicative seminorm on a commutative ring | yes (abstraction) | proof uses only subadditivity, `‖-x‖ = ‖x‖`, finite-product submultiplicativity; verified abstractly as `Evidence87.norm_det_le` over `[SeminormedCommRing R] [NormOneClass R]` |
| 6 | sign of `C` | arbitrary | arbitrary | no | already maximal (for `n` nonempty, `hM` forces `C ≥ 0`; for `n` empty both sides are `1`) |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD
Number of weakening opportunities found: 3 (ℤ → `[SeminormedCommRing R] [NormOneClass R]`; `Fin l` → `Fintype n`; plus the abstract companion `Matrix.norm_det_le`)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_det_le/general_det.lean` — `lake env lean` produced no output (no errors, no warnings) after one fix: `Evidence87.l1Norm_det_le`, `Evidence87.norm_det_le`, ℤ bridge, recovery `example` of the exact project statement.
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_det_le {σ R n : Type*} [SeminormedCommRing R] [NormOneClass R]
    [Fintype n] [DecidableEq n] (M : Matrix n n (MvPolynomial σ R)) {C : ℝ}
    (hM : ∀ i j, (M i j).l1Norm ≤ C) :
    M.det.l1Norm ≤ (Fintype.card n).factorial * C ^ Fintype.card n

theorem Matrix.norm_det_le {R n : Type*} [SeminormedCommRing R] [NormOneClass R]
    [Fintype n] [DecidableEq n] (M : Matrix n n R) {C : ℝ} (hM : ∀ i j, ‖M i j‖ ≤ C) :
    ‖M.det‖ ≤ (Fintype.card n).factorial * C ^ Fintype.card n
```

Cost of restatement: CHEAP — the project proof unchanged (names swapped); the abstract version replaces `l1Norm_prod_le` by `Finset.le_prod_of_submultiplicative_of_nonneg (‖·‖) … norm_mul_le` (mathlib's `Finset.norm_prod_le` needs `NormedCommRing`, a minor gap noticed in passing).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | yes | norm-one via `[NormOneClass R]` | standard mathlib idiom |
| 2 | Sequences → filters? | no | finite algebraic inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` | determinant bounds over ℝ, ℂ, ℚ_p, polynomial rings |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general? | yes | `Fin l` → `[Fintype n]` (as in `Matrix.det_le`) | applies to matrices indexed by any finite type (e.g. boxes, `Fin p × Fin q`) |
| 8 | Concrete-via-abstract? | yes | proof body never uses polynomial structure beyond `normOne_sum_le`, `normOne_neg`, `normOne_prod_le` (diagnostic: after `rw [Matrix.det_apply']` no polynomial-specific identifier appears) — so the real content is `Matrix.norm_det_le` for any seminormed commutative ring; the ℓ¹ version is a corollary once `l1Norm` is packaged as a seminormed-ring structure (type synonym), or a direct copy otherwise | a submultiplicative companion to `Matrix.det_le`, usable for operator norms, ℓ¹ norms, Gauss norms (`Polynomial.gaussNorm`), etc. |
| 9 | False-generalisation guard | no | for `R = ℤ`, `n = Fin l` the general statement is literally the project one (compiled `example`) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Matrix.norm_det_le` over `[SeminormedCommRing R] [NormOneClass R]` with `[Fintype n]`, and `MvPolynomial.l1Norm_det_le` (as corollary via an ℓ¹ seminormed-ring synonym, or as a direct proof).
  - Cost: CHEAP
  - Mathlib downstream this enables: submultiplicative counterpart of `Matrix.det_le` / `det_sum_le` (which require `AbsoluteValue`); determinant estimates for any normed commutative algebra; Wronskian / auxiliary-polynomial height bounds in Diophantine approximation (Roth, Siegel's lemma users in `Mathlib/NumberTheory/SiegelsLemma.lean`).
  - Real mathematical improvement: one Leibniz bound for every submultiplicative seminorm instead of only for absolute values.

### Proof strategy — `Roth.normOne_det_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | — | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | yes | `Matrix.norm_det_le` (abstract), `l1Norm_sum_le`/`l1Norm_neg`/`l1Norm_prod_le` siblings; `Finset.norm_prod_le` over `SeminormedCommRing` | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Same calc shape as mathlib's `Matrix.det_le`. The case split on `Int.units_eq_one_or` could instead use a `‖(u : ℤ) • x‖ = ‖x‖` lemma via `Matrix.det_apply`; cosmetic.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_det_le`

[A] Lean-Finder       "if all entries of a square matrix over a normed commutative ring have norm at most C then the norm of the determinant is at most n! C^n"  hits only `Matrix.det_le`, `Matrix.det_sum_le`, `Matrix.det_sum_smul_le` (AbsoluteValue), Gershgorin, `Matrix.norm_le_iff` — no seminorm version
[B] Loogle            `‖Matrix.det _‖ ≤ _`  no hits
[C] LeanSearch        "norm of determinant bounded by n factorial times bound on entries to the n, seminormed ring"  same `Matrix.det_le` family; `linftyOpSemiNormedRing`; no seminorm det bound
[D] Grep mathlib src  `det_le`, `norm_det`, `‖.*det.*‖ ≤`, `l1Norm`, `Hadamard` (LinearAlgebra/Matrix, Analysis)  only `Matrix.det_le`/`det_sum_le`/`det_sum_smul_le` (LinearAlgebra/Matrix/AbsoluteValue.lean:42–75); `Hadamard.lean` is the entrywise product, not Hadamard's inequality; no ℓ¹ polynomial norm (TODO at Analysis/Polynomial/Norm.lean:34–38)
[E] Name pattern      `Matrix.norm_det_le`, `l1Norm_det_le`, `normOne_det_le` (grep + leansearch name hits)  no hits

Searched for both:
  - the user's current form (ℤ, `|·|`, `Fin l`)
  - the literature-standard form (seminormed commutative ring, any `Fintype`)

Concluded: found a partial match (`Matrix.det_le`, AbsoluteValue only — not applicable to a submultiplicative norm); the seminorm / ℓ¹ form is not in mathlib.

### Normal-form check — `Roth.normOne_det_le`

Equivalent formalisms: `‖det M‖ ≤ (card n)! * C^card n`; nsmul form `(card n)! • C^card n` (as in `Matrix.det_le`); `Fin l` vs `Fintype n`.
Does mathlib already have a canonical form? Yes for absolute values: `Matrix.det_le` with `(Fintype.card n)! • x ^ Fintype.card n`. Our statement should match its shape (`Fintype n`, implicit bound, entrywise hypothesis); in ℝ, `*` with a `Nat.cast` is the more usable spelling, but `•` would match the sibling exactly — reviewer's choice. RHS convention: n/a (inequality).

### Syntactic generality — `Roth.normOne_det_le`

Alternative restatements attempted:
- `Fintype n` with `(card n)! * C ^ card n` (compiled)
- abstract `‖M.det‖` over a seminormed commutative ring (compiled)
Chosen restatement: the `Fintype n` versions. Justification: matches `Matrix.det_le`; the `Fin l` call site specialises by `Fintype.card_fin` through `simp`.

### Superfluous-argument audit — `Roth.normOne_det_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ` | yes | polynomial variables |
| 2 | `l` / `Fin l` | no (as `Fin`) | generalise to `[Fintype n] [DecidableEq n]` |
| 3 | ℤ coefficients | no | generalise with parent to `[SeminormedCommRing R]` |
| 4 | (new) `[NormOneClass R]` | yes for empty `n` | needed via `l1Norm_prod_le` |
| 5 | `hM` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (align with `Matrix.det_le`)
Syntactic generality: RESTATE (`Fintype n`)
Superfluous arguments: 2 to drop (ℤ specialisation via parent; `Fin l` index)

Overall: RESTATE-BEFORE-SHIP

### Call sites — `Roth.normOne_det_le`

Internal use count: 0 outside the declaring file; 1 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:268 | `normOne_det_le _ fun μ ν ↦ (normOne_hasseDeriv_le _ P hP).trans ...` (`abs_coeff_det_hasseDeriv_le`, Lemma 3) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_det_le`?):
  - (none; `grep -rn "det_apply" Roth/` shows other Leibniz expansions only in Wronskian identities, not norm bounds).

Note: K = 1, but the statement is the named estimate of the source (clean.tex:483) and the submultiplicative analogue of an existing mathlib API lemma, so it is not a wrong abstraction.

### Composition check (Phase 6)

Can `Roth.normOne_det_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Matrix.det_le` with `abv := normOne`
  - Mathlib decls used: `Matrix.det_le`
  - Result: fails — `normOne` is not an `AbsoluteValue` (only submultiplicative: `L(PQ) < L(P)L(Q)` in general, e.g. cancellation in `(1+X)(1-X)`), and mathlib has no ℓ¹ norm on `MvPolynomial`.
Attempt 2: a seminorm version of `Matrix.det_le` applied to an ℓ¹ normed-ring instance
  - Result: fails — neither the seminorm determinant bound nor the ℓ¹ instance exists in mathlib.

Conclusion: NOT-COMPOSABLE

## Verdict: `Roth.normOne_det_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): Leibniz bound `‖det A‖ ≤ n! C^n`, standard for any submultiplicative norm (Hadamard is the sharper Euclidean variant); used verbatim by the source (clean.tex:483).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via the parent; `Fin l`); general ℓ¹ form and abstract seminormed-ring form both compiled.
- Mathlib search (Phase 5): only `Matrix.det_le` (AbsoluteValue), inapplicable; no seminorm or ℓ¹ form.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

Mathlib's determinant estimates `Matrix.det_le`, `det_sum_le`, `det_sum_smul_le` (Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean) are stated only for an `AbsoluteValue`, i.e. a multiplicative function; there is no counterpart for a submultiplicative seminorm, and mathlib has no ℓ¹ coefficient norm on polynomials at all (explicit TODO in Mathlib/Analysis/Polynomial/Norm.lean). The project lemma is exactly that missing counterpart for the ℓ¹ norm, and the Phase 4c Q8 diagnostic shows its proof uses only subadditivity, negation-invariance and finite-product submultiplicativity — so the real content is a `Matrix.norm_det_le` for any `[SeminormedCommRing R] [NormOneClass R]`, which compiled in the evidence file with the same calc proof.

The recommended shipping is therefore two-layered: the abstract `Matrix.norm_det_le` (gap: submultiplicative analogue of `Matrix.det_le`), and `MvPolynomial.l1Norm_det_le` in the `l1Norm` PR — either as a direct copy of the project proof (compiled) or as a one-line corollary if the parent is packaged as a seminormed-ring type synonym. Both generalise the index from `Fin l` to any `Fintype n`, matching `Matrix.det_le`. `NormOneClass` is needed only for the empty matrix.

Reason for the generalisation: LITERATURE-WEAKENING (coefficient ring, index type) and MODERN-IDIOM (concrete-via-abstract: seminormed-ring determinant bound).

Proposed restatement:
```lean
theorem Matrix.norm_det_le {R n : Type*} [SeminormedCommRing R] [NormOneClass R]
    [Fintype n] [DecidableEq n] (M : Matrix n n R) {C : ℝ} (hM : ∀ i j, ‖M i j‖ ≤ C) :
    ‖M.det‖ ≤ (Fintype.card n).factorial * C ^ Fintype.card n := by
  sorry  -- proof in evidence file

theorem MvPolynomial.l1Norm_det_le {σ R n : Type*} [SeminormedCommRing R] [NormOneClass R]
    [Fintype n] [DecidableEq n] (M : Matrix n n (MvPolynomial σ R)) {C : ℝ}
    (hM : ∀ i j, (M i j).l1Norm ≤ C) :
    M.det.l1Norm ≤ (Fintype.card n).factorial * C ^ Fintype.card n := by
  sorry  -- proof in evidence file (project proof verbatim)
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- determinant bounds for any normed commutative algebra (ℓ¹, operator norms, Gauss norm), complementing `Matrix.det_le`;
- Wronskian / auxiliary-polynomial height estimates for Diophantine approximation (Roth's Lemma 3) on top of `MvPolynomial.l1Norm`;
- closes part of the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`.

PR grouping: `Matrix.norm_det_le` as its own small PR (Mathlib/Analysis/Matrix/Normed.lean, or next to `Matrix.det_le`); `l1Norm_det_le` with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_neg`, `l1Norm_sum_le`, `l1Norm_mul_le`, `l1Norm_prod_le`).

Next action: run `/generalise Roth.normOne_det_le` with the parent `/generalise Roth.normOne`; restate as `MvPolynomial.l1Norm_det_le` over `[SeminormedCommRing R] [NormOneClass R]` and `[Fintype n]`, add `Matrix.norm_det_le`, and keep the ℤ / `Fin l` form for the call site Roth/CoeffNorm.lean:268.

---

## Next step

Ship `Matrix.norm_det_le` ([SeminormedCommRing R] [NormOneClass R], `Fintype n`) and `MvPolynomial.l1Norm_det_le` (in the `MvPolynomial.l1Norm` PR), keeping the project's ℤ / `Fin l` specialisation at Roth/CoeffNorm.lean:268.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_det_le/general_det.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`; reproduces the sibling `l1Norm` API): `l1Norm_det_le` (`Fintype n`, `[SeminormedCommRing R] [NormOneClass R]`), abstract `norm_det_le`, ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement. First `lake env lean` run failed only because `Finset.norm_prod_le` requires `NormedCommRing` (replaced by `Finset.le_prod_of_submultiplicative_of_nonneg`); second run (~29 s): no output — no errors, no warnings.
- Mathlib greps: `det_le`, `norm_det`, `‖.*det.*‖ ≤`, `Hadamard`, `l1Norm` — only `Matrix.det_le` family (AbsoluteValue) at LinearAlgebra/Matrix/AbsoluteValue.lean:42–75; `Finset.norm_prod_le` at Analysis/Normed/Ring/Basic.lean:383 requires `NormedCommRing`.
- LeanSearch / Lean-Finder / Loogle as in Phase 5.
- WebSearch ×3 (Leibniz bound with polynomial entries; submultiplicative / Banach-algebra version; Hadamard and Roth/Wronskian height bounds); local reference clean.tex lines 441, 483, 487.
- ChatGPT MCP: n/a (not configured in this session).
