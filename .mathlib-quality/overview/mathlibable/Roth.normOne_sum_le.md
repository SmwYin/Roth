---
decl: Roth.normOne_sum_le
file: Roth/CoeffNorm.lean
line: 90
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Finite-sum triangle inequality for the l1 coefficient norm; a one-call Finset.le_sum_of_subadditive lemma but standard named-norm API exactly like mathlib's norm_sum_le / gauge_sum_le / eLpNorm_sum_le, with 4 project call sites; proof compiles verbatim for MvPolynomial.l1Norm over any SeminormedCommRing and for an AbsoluteValue-based l1 norm (evidence file clean).
action: Ship as MvPolynomial.l1Norm_sum_le over [SeminormedCommRing R] in the MvPolynomial.l1Norm PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean); keep the ℤ form for call sites Roth/CoeffNorm.lean:99,101,123,152 via Int.norm_eq_abs.
---

# Roth.normOne_sum_le

## Inventory entry

### `theorem Roth.normOne_sum_le`
- **Type**: `{σ : Type*} {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial σ ℤ) : Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)`
- **What**: Triangle inequality for the ℓ¹ coefficient norm over a finite sum: `‖∑ᵢ fᵢ‖₁ ≤ ∑ᵢ ‖fᵢ‖₁`.
- **How**: One term: `Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le s f` (mathlib's generic subadditive-to-finite-sum lemma fed with the project's `normOne_zero` and `normOne_add_le`).
- **Hypotheses**: none.
- **Uses from project**: `Roth.normOne`, `Roth.normOne_zero`, `Roth.normOne_add_le`
- **Used by**: Roth/CoeffNorm.lean:99 and :101 (`Roth.normOne_mul_le`, twice), Roth/CoeffNorm.lean:123 (`Roth.normOne_det_le`), Roth/CoeffNorm.lean:152 (`Roth.normOne_hasseDeriv_le`). No uses outside CoeffNorm.lean (`grep -rn normOne_sum_le Roth/`).
- **Visibility**: public
- **Lines**: 89–92, proof length 1 line
- **Notes**: Used by the source's determinant estimate (clean.tex:477–482, `‖det(…)‖₁ ≤ ∑_σ ‖∏_ν …‖₁`).

## Junk check (Step 8)
- Used anywhere? Yes, 4 call sites in 3 declarations (`normOne_mul_le`, `normOne_det_le`, `normOne_hasseDeriv_le`), the core of Lemma 3.
- Wrapper of 1–2 mathlib calls? Yes: one call to `Finset.le_sum_of_subadditive` with project inputs. But this is exactly mathlib's own convention for named norm-like functions (`norm_sum_le`, `enorm_sum_le` in Analysis/Normed/Group/Basic.lean:804–811, `gauge_sum_le` in Analysis/Convex/Gauge.lean:216, `eLpNorm_sum_le`, `abs_sum_le_sum_abs`), all one-line `le_sum_of_subadditive` lemmas kept as API; inlining at 4 sites would repeat a 3-argument term each time.
- Does mathlib have it? No (Phase 5): no ℓ¹ norm on (Mv)Polynomial / Finsupp.
- Too specific (inline)? No — generic API lemma for the norm.
- Well-chosen? Yes, modulo the parent's ℤ / `|·|` specialisation.
- Conclusion: `KEEP` — action: keep; re-aim at `MvPolynomial.l1Norm` with the parent def.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 KEEP; qualified name `Roth.normOne_sum_le` not in mathlib (no `namespace Roth` in `Mathlib/`). Not a glue lemma (it is a one-line proof by a mathlib combinator, not `rfl`/unfolding), so a full run in the generalised setting fixed by the parent verdict (`Roth.normOne`: YES-but-generalise-first to `MvPolynomial.l1Norm` over `[SeminormedCommRing R]`).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.CoeffNorm` has no diagnostics)
- decl `Roth.normOne_sum_le`: resolved at Roth/CoeffNorm.lean:90
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Coefficient norms (ℓ¹ and sup bounds) of integer polynomials and the estimates for Lemma 3 and Lemma 9 of Roth's theorem.

### Statement (Phase 1)

`Roth.normOne_sum_le` is a theorem stating the following: for a finite family of polynomials `f_i ∈ ℤ[X_σ]` (`i ∈ s`), the length (ℓ¹ coefficient norm) of their sum is at most the sum of their lengths: `L(∑_{i∈s} f_i) ≤ ∑_{i∈s} L(f_i)`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the variables.
- `ι : Type*`, `s : Finset ι` — the finite index set.
- `f : ι → MvPolynomial σ ℤ` — the family.

Hypotheses (Lean side):
- none.

Conclusion (math): `L(∑ f_i) ≤ ∑ L(f_i)`.

Conclusion (Lean): `Roth.normOne (∑ i ∈ s, f i) ≤ ∑ i ∈ s, Roth.normOne (f i)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API inequality (finite triangle inequality) of a helper definition; not a structure, not a main result, not named.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

Conclusion: check skipped (theorem). Note for Phase 7: the proof is a single `Finset.le_sum_of_subadditive` call; mathlib nonetheless ships the analogous `X_sum_le` for every named norm (`norm_sum_le`, `gauge_sum_le`, `eLpNorm_sum_le`), and this lemma has 4 consumers.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | length of polynomial L(P) sum of absolute values of coefficients L(P1+...+Pn) ≤ L(P1)+...+L(Pn) | partial | `L(P) = ∑ |a_i|` (Schinzel, Funct. Approx. 35, 37) | the finite-sum inequality is not stated explicitly; immediate from the norm axioms by induction |
| 2 | WebSearch (general form) | ℓ1 norm finite sum triangle inequality group algebra l1(G) | yes | `L¹(G)` / `ℓ¹(G)` is a Banach algebra (Wikipedia "Group algebra of a locally compact group") | finite triangle inequality for any norm, by induction |
| 3 | WebSearch (aliases / mathlib) | mathlib Finset.le_sum_of_subadditive norm_sum_le polynomial coefficient norm | yes | `Finset.le_sum_of_subadditive` (generic), `norm_sum_le` | the mathlib pattern for finite triangle inequalities; nothing for polynomial coefficient norms |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` lines 450, 477–482 | yes | "The triangle inequality gives …"; determinant bound `‖det(…)‖₁ ≤ ∑_σ ‖∏_ν …‖₁` | the source uses exactly the finite-sum form for the Leibniz expansion |
| 6 | nLab | normed vector space / Banach space | yes | triangle inequality axiom (finite version by induction); ℓ¹ as standard example | no polynomial-specific page |
| 7 | nCatLab | — | n/a | — | not a categorical statement (finite-sum inequality) |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry; no coefficient norms |
| 9 | MathOverflow / Math.SE | length of polynomials, norm properties (Mahler measure discussions) | yes | `L` is a norm on coefficient vectors | subadditivity/finite triangle used without comment |
| 10 | recent arXiv (last 5 years) | 1-norm of polynomials in a basis (arXiv 2404.04190); Paley inequality nonabelian groups (arXiv 2105.02989, from #2) | yes | same ℓ¹ norm; finite sums in group algebras | no competing form |

### Literature summary (Phase 3)

Concept identified as: finite triangle inequality for the length / ℓ¹ coefficient norm; special case of the finite triangle inequality in `ℓ¹(I, R)`.
Sources agree on the standard form: yes — consequence of the norm axioms.
Most general standard form: for any (semi)normed coefficient ring (or any absolute value on a semiring), `‖∑_{i∈s} p_i‖₁ ≤ ∑_{i∈s} ‖p_i‖₁`.
Generality dimensions where the literature varies:
  - coefficient ring: ℤ / ℝ / ℂ / seminormed ring / absolute value on a semiring; proof needs only `l1Norm 0 ≤ 0` and subadditivity.
  - index set of monomials: ℕ, ℕ^σ, any set.
Disagreement with the literature: only the inherited ℤ / `|·|` specialisation of the parent def.

### Generality analysis — `Roth.normOne_sum_le`

Literature-standard form (from Phase 3): `l1Norm (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1Norm (f i)` for `f : ι → MvPolynomial σ R`, `[SeminormedCommRing R]`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | coefficient ring | `ℤ` (via `normOne`) | `[SeminormedCommRing R]` | yes | proof only needs `l1Norm_zero` and `l1Norm_add_le`; verified (`Evidence83.l1Norm_sum_le`, verbatim proof) |
| 2 | norm structure | `|(· : ℝ)|` | `‖·‖` | yes | follows parent restatement; bridge `Evidence83.l1Norm_int_eq_normOne` via `Int.norm_eq_abs`; recovery `example` compiles |
| 3 | negation in `R` | `ℤ` ring | not needed | yes (option) | `Evidence83.l1NormAbv_sum_le` for `AbsoluteValue R ℝ` on `[CommSemiring R]`; a parent-def design choice, not primary target |
| 4 | `ι`, `s : Finset ι` | arbitrary | arbitrary | no | already maximal (a `Multiset` version is an optional companion, cf. `norm_multiset_sum_le`) |
| 5 | `σ : Type*` | arbitrary | arbitrary | no | already maximal |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (inherited from the parent def's ℤ-specialisation)
Number of weakening opportunities found: 1 primary (ℤ → `[SeminormedCommRing R]`), plus 1 optional (absolute-value ℓ¹ norm on a `CommSemiring`)
Verification: `.mathlib-quality/overview/evidence/Roth.normOne_sum_le/general_and_composition.lean` — general `l1Norm`, `l1Norm_zero`, `l1Norm_add_le`, `l1Norm_sum_le` (project proof verbatim), ℤ bridge, recovery `example` of the exact project statement, and `l1NormAbv_sum_le` over `[CommSemiring R] (v : AbsoluteValue R ℝ)`; `lean_diagnostic_messages`: no diagnostics.
Proposed restatement:

```lean
theorem MvPolynomial.l1Norm_sum_le {σ R ι : Type*} [SeminormedCommRing R]
    (s : Finset ι) (f : ι → MvPolynomial σ R) :
    (∑ i ∈ s, f i).l1Norm ≤ ∑ i ∈ s, (f i).l1Norm
```

Cost of restatement: CHEAP — proof is verbatim.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | Preambles → typeclasses? | no | no hypotheses | — |
| 2 | Sequences → filters? | no | finite inequality | — |
| 3 | Construction → universal property? | no | an inequality | — |
| 4 | Set predicate → bundled substructure? | no | — | — |
| 5 | Field/specific → typeclass hierarchy? | yes | ℤ → `[SeminormedCommRing R]` (with the parent) | `l1Norm_mul_le`, `l1Norm_det_le`-type bounds for all seminormed rings |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index → general monoid? | option | `AddMonoidAlgebra R M` ℓ¹ norm (parent's unverified option) | not needed by consumers |
| 8 | Concrete-via-abstract? | yes | proof uses only `f 0 ≤ 0` and subadditivity — the generic `Finset.le_sum_of_subadditive`; covered by row 5 | — |
| 9 | False-generalisation guard | no | for `R = ℤ` the general statement reduces to the project one (compiled `example`) | — |

Further option: if the parent `/generalise` packages `l1Norm` as an `AddGroupSeminorm`, this lemma becomes a specialisation of a generic seminorm finite-sum bound (mathlib has none named for `AddGroupSeminormClass` today; `Finset.le_sum_of_subadditive` would remain the proof), but mathlib still keeps the named `X_sum_le` form for each norm.

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `MvPolynomial.l1Norm_sum_le` over `[SeminormedCommRing R]` (above).
  - Cost: CHEAP
  - Mathlib downstream this enables: `l1Norm_mul_le` (submultiplicativity, whose proof calls this twice), determinant / Hasse-derivative norm bounds, univariate companion closing the ℓ¹ TODO in `Mathlib/Analysis/Polynomial/Norm.lean`.
  - Real mathematical improvement: one finite triangle inequality for all seminormed coefficient rings instead of a ℤ copy.

### Proof strategy — `Roth.normOne_sum_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | Topology ε-δ instead of filters? | no | — | — |
| 2 | Elementwise algebra instead of ideals? | no | — | — |
| 3 | Sequences instead of filters? | no | — | — |
| 4 | Construction instead of universal property? | no | — | — |
| 5 | Missing mathlib helpers? | no | uses `Finset.le_sum_of_subadditive` exactly as `norm_sum_le` / `gauge_sum_le` do | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC
(Identical pattern to mathlib's `norm_sum_le`, `gauge_sum_le`, `eLpNorm_sum_le`.)

### Diamond / defeq risk (Phase 4.5)

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.normOne_sum_le`

[A] Lean-Finder       "l1 norm of coefficients of a finite sum of multivariate polynomials is at most the sum of l1 norms"  no hits (only `degrees_sum_le`, `coeff_sum`, `totalDegree_finset_sum`, `mahlerMeasure_le_sum_norm_coeff`)
[B] Loogle            `Finsupp.sum (Finset.sum _ _) _ ≤ _`  no hits
[C] LeanSearch        "sum of norms of coefficients of a finite sum of polynomials is at most the sum over the polynomials"  no hits (generic `nnnorm_sum_le_of_le`, `norm_tsum_le_tsum_norm`, `Polynomial.finset_sum_coeff`)
[D] Grep mathlib src  `l1Norm`, `sum_norm_coeff_le`, `namespace Roth`, `le_sum_of_subadditive` users  no ℓ¹ polynomial norm; ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34-36; `le_sum_of_subadditive` users are `norm_sum_le`, `enorm_sum_le`, `norm_multiset_sum_le`, `gauge_sum_le`, `eLpNorm_sum_le`, `abs_sum_le_sum_abs` (the precedent pattern)
[E] Name pattern      `lean_local_search l1Norm_sum`  n/a: tool not loaded/ripgrep missing in this environment (as in the sibling reports); covered by grep [D]

Searched for both:
  - the user's current form (ℤ, `|·|`)
  - the literature-standard form (ℓ¹ finite triangle inequality over a seminormed ring / absolute value)

Concluded: not in mathlib (all 5 methods exhausted); building block `Finset.le_sum_of_subadditive` exists but the needed `l1Norm`, `l1Norm_zero`, `l1Norm_add_le` do not.

### Normal-form check — `Roth.normOne_sum_le`

Equivalent formalisms: `l1Norm (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1Norm (f i)`; `l1Norm (s.sum f) ≤ s.sum (l1Norm ∘ f)`; Multiset version.
Does mathlib already have a canonical form? Yes for norms: `norm_sum_le (s : Finset ι) (f : ι → E) : ‖∑ i ∈ s, f i‖ ≤ ∑ i ∈ s, ‖f i‖`. Our statement matches that shape and argument order exactly. RHS convention respected? yes (n/a for an inequality).

### Syntactic generality — `Roth.normOne_sum_le`

Alternative restatements attempted:
- `l1Norm (∑ i ∈ s, f i) ≤ ∑ i ∈ s, l1Norm (f i)` (explicit `s f`, as `norm_sum_le`)
- `(∀ i ∈ s, l1Norm (f i) ≤ n i) → l1Norm (∑ i ∈ s, f i) ≤ ∑ i ∈ s, n i` (`_of_le` variant, cf. `norm_sum_le_of_le`)
- Multiset form (cf. `norm_multiset_sum_le`)
Chosen restatement: the explicit `s f` form. Justification: matches `norm_sum_le` and is what all 4 call sites use via `(normOne_sum_le _ _).trans`.

### Superfluous-argument audit — `Roth.normOne_sum_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ : Type*` | yes | index type |
| 2 | `ι`, `s`, `f` | yes | — |
| 3 | ℤ coefficients (via `normOne`) | no | generalise with parent to `[SeminormedCommRing R]` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 1 to drop (ℤ specialisation, via parent def)

Overall: RESTATE-BEFORE-SHIP (state against `MvPolynomial.l1Norm` with `‖·‖`; name `l1Norm_sum_le`)

### Call sites — `Roth.normOne_sum_le`

Internal use count: 0 outside the declaring file; 4 inside Roth/CoeffNorm.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:99 | `refine (normOne_sum_le _ _).trans ?_` (`normOne_mul_le`) |
| Roth/CoeffNorm.lean:101 | `exact Finset.sum_le_sum fun a _ ↦ (normOne_sum_le _ _).trans_eq <|` (`normOne_mul_le`) |
| Roth/CoeffNorm.lean:123 | `calc _ ≤ ∑ τ …, normOne (_ * ∏ i, M (τ i) i) := normOne_sum_le _ _` (`normOne_det_le`) |
| Roth/CoeffNorm.lean:152 | `refine (normOne_sum_le _ _).trans ?_` (`normOne_hasseDeriv_le`) |

Inline-derivation grep (was the equivalent re-derived elsewhere without using `Roth.normOne_sum_le`?):
  - (none in the project; no other `le_sum_of_subadditive normOne` in `Roth/`).

### Composition check (Phase 6)

Can `Roth.normOne_sum_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Finset.le_sum_of_subadditive normOne normOne_zero.le normOne_add_le s f`
  - Mathlib decls used: `Finset.le_sum_of_subadditive`
  - Result: succeeds as a one-call composition — but only given the project's `normOne_zero` and `normOne_add_le`, which are not in mathlib (the latter is a genuine 7-line proof). From mathlib alone it is not composable.
  - Notes: in the generalised setting, the same one-call composition from `l1Norm_zero` and `l1Norm_add_le` is exactly how mathlib states `norm_sum_le` / `gauge_sum_le` / `eLpNorm_sum_le` as named API lemmas.

Attempt 2: via a mathlib ℓ¹ norm on `Finsupp` / `lp` / `PiLp 1` and `norm_sum_le`
  - Result: fails — no norm instance on `σ →₀ R` / `AddMonoidAlgebra`; `PiLp 1` needs a finite index; `lp` is the wrong carrier (parent Phase 6).

Conclusion: NOT-COMPOSABLE from mathlib alone (composable in one call from the companion API lemmas that would ship in the same PR).

## Verdict: `Roth.normOne_sum_le`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): finite triangle inequality for the length / ℓ¹ norm, a consequence of the norm axioms; used by the source for the determinant bound (clean.tex:477–482).
- Generality analysis (Phase 4): STRICTLY NARROWER (ℤ via parent def); general form compiled verbatim in the evidence file, plus an AbsoluteValue/CommSemiring variant.
- Mathlib search (Phase 5): not in mathlib (no ℓ¹ polynomial norm; Norm.lean ℓ¹ TODO).
- Composition check (Phase 6): NOT-COMPOSABLE from mathlib alone (one call given the companion lemmas).

**Rationale:**

Mathlib has no ℓ¹ coefficient norm on `Polynomial`/`MvPolynomial`/`Finsupp` (`Mathlib/Analysis/Polynomial/Norm.lean` lists the ℓ¹ "length" as a TODO), so this lemma cannot exist there yet; it belongs to the API of the parent's proposed `MvPolynomial.l1Norm`. Although the proof is a single `Finset.le_sum_of_subadditive` call, mathlib's convention is to ship exactly such a named `X_sum_le` lemma for every norm-like function (`norm_sum_le`, `enorm_sum_le`, `gauge_sum_le`, `eLpNorm_sum_le`, `abs_sum_le_sum_abs` are all this same one-liner), and here it has four consumers (`normOne_mul_le` twice, `normOne_det_le`, `normOne_hasseDeriv_le`) — it is the step that turns the triangle inequality into submultiplicativity and the Leibniz determinant bound. The one-liner is therefore justified as API surface, not as a wrapper to inline. The evidence file shows the proof goes through verbatim over `[SeminormedCommRing R]` and recovers the ℤ statement via `Int.norm_eq_abs`; it also works for an `AbsoluteValue`-based ℓ¹ norm on a commutative semiring.

Reason for the generalisation: LITERATURE-WEAKENING and MODERN-IDIOM (coefficient ring via the normed typeclass hierarchy), inherited from the parent.

Proposed restatement:
```lean
theorem MvPolynomial.l1Norm_sum_le {σ R ι : Type*} [SeminormedCommRing R]
    (s : Finset ι) (f : ι → MvPolynomial σ R) :
    (∑ i ∈ s, f i).l1Norm ≤ ∑ i ∈ s, (f i).l1Norm :=
  Finset.le_sum_of_subadditive l1Norm l1Norm_zero.le l1Norm_add_le s f
```

Estimated cost of regeneralisation: CHEAP.

Mathlib downstream this enables:
- `l1Norm_mul_le` (submultiplicativity) and `l1Norm_prod_le` for every seminormed coefficient ring;
- determinant-type bounds (`l1Norm_det_le`) via the Leibniz formula;
- a univariate `Polynomial.l1Norm_sum_le` companion closing the ℓ¹ TODO in Norm.lean.

PR grouping: ship with `MvPolynomial.l1Norm` and its API (`l1Norm_nonneg`, `l1Norm_eq_sum_of_support_subset`, `l1Norm_monomial`, `l1Norm_zero`, `norm_coeff_le_l1Norm`, `l1Norm_add_le`, `l1Norm_neg`, `l1Norm_mul_le`) as one PR.

Next action: run `/generalise Roth.normOne_sum_le` together with the parent `/generalise Roth.normOne`, restate as `MvPolynomial.l1Norm_sum_le`, and keep the ℤ form (via `Int.norm_eq_abs`) at its call sites Roth/CoeffNorm.lean:99, 101, 123, 152.

---

## Next step

Restate as `MvPolynomial.l1Norm_sum_le` over `[SeminormedCommRing R]` in the `MvPolynomial.l1Norm` PR (Mathlib/Analysis/Polynomial/Norm.lean or new Mathlib/Analysis/MvPolynomial/Norm.lean), with the project call sites (Roth/CoeffNorm.lean:99, 101, 123, 152) using the ℤ specialisation.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.normOne_sum_le/general_and_composition.lean` (imports `Roth.CoeffNorm`, `Mathlib.Analysis.Normed.Ring.Int`): general `l1Norm`, `l1Norm_zero`, `l1Norm_add_le`, `l1Norm_sum_le` (verbatim one-line proof), ℤ bridge `l1Norm_int_eq_normOne`, recovery `example` of the exact project statement, and `l1NormAbv_sum_le` for `AbsoluteValue R ℝ` on a `CommSemiring`; `lean_diagnostic_messages`: no diagnostics (first attempt).
- Mathlib greps: `l1Norm`, `sum_norm_coeff_le`, `namespace Roth` (no hits); `le_sum_of_subadditive` users (`norm_sum_le`, `enorm_sum_le`, `gauge_sum_le`, `eLpNorm_sum_le`, `abs_sum_le_sum_abs`); ℓ¹ TODO at Analysis/Polynomial/Norm.lean:34-36.
- LeanSearch / Lean-Finder / Loogle queries as in Phase 5 (no hit).
- WebSearch ×3 (length finite-sum inequality; ℓ¹(G) group algebra; mathlib le_sum_of_subadditive), local reference clean.tex lines 448–452, 477–482.
- ChatGPT MCP: n/a (not configured in this session).
