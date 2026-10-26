---
decl: MvPolynomial.hasseCoeff
file: Roth/HasseDeriv.lean
line: 50
kind: def
visibility: public
verdict: YES-but-generalise-first
cost: MODERATE
junk: KEEP
rationale: The multi-index binomial coefficient binom(k,d) = prod_j binom(k_j,d_j) is standard (multi-index notation) and absent from mathlib; it should go upstream as a Finsupp-level `Finsupp.choose k d` alongside a multivariate Hasse derivative rather than as an MvPolynomial-namespaced helper.
action: Upstream together with MvPolynomial.hasseDeriv as `Finsupp.choose k d` (Nat.choose argument order) in Mathlib/Data/Finsupp/ or Mathlib/Data/Nat/Choose/Multinomial.lean, porting hasseCoeff_eq_zero_iff and hasseCoeff_eq_prod; locally keep as is (used in Roth/HasseDeriv.lean, Roth/CoeffNorm.lean, Roth/Taylor.lean).
---

# MvPolynomial.hasseCoeff

## Inventory entry

### `def MvPolynomial.hasseCoeff`
- **Type**: `{σ : Type*} → (d k : σ →₀ ℕ) → ℕ`
- **What**: The multi-index binomial coefficient `∏_{j ∈ supp d} (k j).choose (d j)`, i.e. `binom(k, d)`; the scalar by which the Hasse derivative `Δ_d` multiplies the monomial `X^k`.
- **How**: One-line definition `d.prod fun j ↦ (k j).choose` (`Finsupp.prod` over the support of `d`; `Nat.choose`).
- **Hypotheses**: none (no typeclasses; `R` from the section `variable` is not included).
- **Uses from project**: `[]`
- **Used by**: Roth/HasseDeriv.lean: `hasseDeriv`, `hasseDeriv_monomial`, `hasseDeriv_apply`, `hasseCoeff_eq_zero_iff`, `coeff_hasseDeriv`, `hasseCoeff_eq_prod`, `hasseDeriv_zero_apply`, `hasseDeriv_C`, `hasseDeriv_rename`, `hasseCoeff_mul_hasseCoeff` (private), `hasseDeriv_hasseDeriv`, `hasseDeriv_hasseDeriv_of_disjoint`, `hasseCoeff_mul_succ` (private), `pderiv_hasseDeriv`, `hasseDeriv_monomial_mul`, `hasseDeriv_single_aeval_X`, `uniqueAlgEquiv_hasseDeriv`, `hasseCoeff_le_two_pow`; Roth/CoeffNorm.lean: `abs_coeff_hasseDeriv_le` (l.139); Roth/Taylor.lean: `hasseCoeff_single_add_eq` (private, l.82-85), `coeff_taylor_monomial_single_add_aux` (private, l.113-117, via lemmas)
- **Visibility**: public
- **Lines**: 49–50, proof length 1 line (definition body)
- **Notes**: Docstring says "a product over the support of `d`"; `hasseCoeff_eq_prod` gives the `Fintype` full-product form. Argument order `(d k)` is the reverse of `Nat.choose`'s `(n k)` convention (top index second).

## Junk check (Step 8)
- Used anywhere? Yes: about 40 occurrences in Roth/HasseDeriv.lean plus Roth/CoeffNorm.lean and Roth/Taylor.lean; it is the coefficient in the definition of `hasseDeriv`.
- Wrapper of 1–2 mathlib calls? Syntactically yes (`Finsupp.prod` + `Nat.choose`), but it names a standard concept (multi-index binomial) and is the API anchor for all Hasse-derivative coefficient lemmas.
- Does mathlib have it? No (Phase 5 below): mathlib has `Finsupp.multinomial` (a different quantity) and univariate `Polynomial.hasseDeriv`, nothing for `∏ (k j).choose (d j)`.
- Too specific / inline? No: inlining would replace a named ℕ by a `Finsupp.prod` lambda in ~40 statements and break `simp [hasseCoeff]` unfold-control.
- Well-chosen definition? Yes mathematically; the name is tied to Hasse derivatives rather than to the general multi-index binomial concept (see Phase 4c).
- Conclusion: `KEEP` — action: keep as is in the project; for upstreaming, rename to a Finsupp-level `choose` (see verdict).

## Mathlibable assessment (Step 9)

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` compiles)
- decl `MvPolynomial.hasseCoeff`: resolved at Roth/HasseDeriv.lean:50
- kind:                      def
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseCoeff` is a definition of the following: for multi-indices `d, k ∈ ℕ^(σ)` (finitely supported), the multi-index binomial coefficient
`binom(k, d) = ∏_{j} binom(k_j, d_j)`, the product taken over the support of `d` (other factors are `binom(k_j, 0) = 1`). It vanishes iff `d ≰ k`.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — the index set of variables.
- `d : σ →₀ ℕ` — lower multi-index (order of the derivative).
- `k : σ →₀ ℕ` — upper multi-index (exponent of the monomial).

Hypotheses (Lean side):
- none.

Conclusion (math): the natural number `binom(k, d)`.

Conclusion (Lean): n/a — definition (`ℕ`-valued).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: helper definition of a standard combinatorial number; not a new structure or main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | yes      | proofs control unfolding explicitly (`simp only [hasseCoeff]` in `hasseCoeff_mul_hasseCoeff`, `rw [hasseCoeff, ...]` in Taylor `hasseCoeff_single_add_eq`); `coeff_hasseDeriv` is stated with the opaque name so `simp` does not expand a `Finsupp.prod` lambda |
| Avoid typeclass diamonds         | no       | ℕ-valued, no instances involved |
| Mark semantic intent / API name  | yes      | consumers `coeff_hasseDeriv`, `hasseDeriv_hasseDeriv` (composition rule `Δ_d Δ_e = binom(d+e,d) Δ_{d+e}`), `hasseCoeff_le_two_pow`, `abs_coeff_hasseDeriv_le` in CoeffNorm.lean |

Conclusion: ONE-LINER WITH-EXEMPTION

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index binomial coefficient product binom(k_j, d_j) multivariate Hasse derivative definition | yes | `binom(α,β) = ∏ binom(α_i,β_i)`, zero if some `α_i < β_i`; `∂_a f = Σ_e binom(e,a) [x^e]f x^{e-a}` | arXiv 2403.19824, 2111.07572, 2603.03841; matches our def exactly |
| 2 | WebSearch (general form) | multi-index notation binomial coefficient "alpha choose beta" product | yes | multi-index notation: `binom(α,β) = ∏ binom(α_i,β_i) = α!/(β!(α-β)!)` | Wikipedia "Multi-index notation", Encyclopedia of Math; general concept independent of Hasse derivatives |
| 3 | WebSearch (named-after / aliases) | Hasse-Schmidt derivative several variables coefficient formula monomial | partial | product of univariate binomials per variable | nLab "Hasse-Schmidt derivative", arXiv 2003.09694 (multivariate HS derivations) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for hasse/binom/choose | yes | l.122-134: `Δ_i X^k = (∏_j binom(k_j,i_j)) X^{k-i}`; l.150 coefficient form; l.579-582 composition with `∏ binom(i_j+k_j, i_j)` | project source paper §1 |
| 6 | nLab | Hasse-Schmidt derivative (surfaced by query #3) | partial | several-variable derivatives indexed by multisets of variables | no standalone multi-index binomial entry |
| 7 | nCatLab | — | n/a | — | not a categorical concept; nLab entry #6 covers the only related page |
| 8 | Stacks Project | — | n/a | — | combinatorial/polynomial concept, not algebraic geometry |
| 9 | MathOverflow / Math.SE | mathoverflow multi-index binomial coefficient Vandermonde identity binom(alpha,beta) product of binomials | partial | multi-index Chu–Vandermonde `Σ_{|β|=r} binom(v,β) = binom(|v|,r)` | no MO thread surfaced; arXiv 2309.17397 Lemma 7.1 uses the same product convention |
| 10 | recent arXiv (last 5 years) | (results of #1, #9) | yes | arXiv 2403.19824 (2024), 2111.07572 (2021), 2309.17397 (2023) | all use the componentwise product with `β ≤ α` convention |

### Literature summary (Phase 3)

Concept identified as: multi-index binomial coefficient `binom(α, β)` (multi-index notation), the coefficient in multivariate Hasse derivatives and multivariate binomial/Taylor expansions.
Sources agree on the standard form: yes.
Most general standard form: for multi-indices `α, β` (finitely supported `ℕ`-valued), `binom(α,β) = ∏_i binom(α_i, β_i)`, which is `0` unless `β ≤ α`.
Generality dimensions where the literature varies:
  - index set: finite `{1..n}` in most sources; arbitrary index set with finite support is the natural mathlib generality (ours).
  - upper index: always a multi-index; only finitely many factors matter (those in `supp β`), so the upper index could be any function.
Disagreement with the literature: none mathematically; notation order differs (literature writes `binom(k, d)`, Lean signature is `hasseCoeff d k`).

### Generality analysis — `MvPolynomial.hasseCoeff`

Literature-standard form (from Phase 3): `binom(α,β) = ∏ binom(α_i,β_i)` for finitely supported multi-indices.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `σ : Type*` | arbitrary index type | finite index set | no (already more general) | product over `d.support` |
| 2 | `d : σ →₀ ℕ` | finitely supported | multi-index | no | finiteness of the product needs finite support |
| 3 | `k : σ →₀ ℕ` | finitely supported | multi-index | yes (`σ → ℕ`) | only `k j` for `j ∈ supp d` is read; verified in evidence file, but the finsupp form is what all `≤`/`+` lemmas use |
| 4 | codomain `ℕ` | ℕ | ℕ / ℤ | no | cast at use sites; `Ring.choose` generalisation (binomial rings) is a different concept |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for the mathematically meaningful form; the only verified weakening, `k : σ → ℕ`, compiles but is not recommended because it breaks the `d ≤ k` symmetry of the API and mathlib's multi-index API is uniformly `σ →₀ ℕ`).
Number of weakening opportunities found: 1 (verified, not recommended)
Cost of restatement: CHEAP

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | no | — | finite combinatorial quantity |
| 3 | construction vs universal property? | no | — | a number |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | ℕ-valued, no ring |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes (namespace) | `Finsupp.choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose`, top index first like `Nat.choose`, living in `Finsupp` next to `Finsupp.multinomial` | `Finsupp.antidiagonal`-based multivariate binomial theorem / Vandermonde, `MvPowerSeries`/`MvPolynomial` Taylor expansions, reusable outside Hasse derivatives |
| 8 | concrete-via-abstract? | yes | the definition never mentions polynomials; it is a pure `Finsupp` combinatorial number placed in `MvPolynomial` | as #7 |
| 9 | false-generalisation guard | no false generalisation | `Finsupp.choose k d` is `rfl`-equal to `hasseCoeff d k` (evidence file) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `def Finsupp.choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose` with `Finsupp.choose_eq_zero_iff : k.choose d = 0 ↔ ¬d ≤ k` and `Finsupp.choose_eq_prod [Fintype σ]`.
  - Cost: MODERATE (definition itself CHEAP; project-wide rename of ~45 occurrences in 3 files plus argument swap)
  - Mathlib downstream this enables: multi-index binomial theorem `(X+Y)^k = Σ_{d ≤ k} binom(k,d) X^d Y^{k-d}` over `Finsupp.Iic`/antidiagonal, multivariate `MvPolynomial` Hasse derivative and Taylor coefficients, sits beside `Finsupp.multinomial`.
  - Real mathematical improvement: the concept is polynomial-independent; naming it in `Finsupp` with `Nat.choose` argument order matches the literature `binom(k,d)` and lets non-polynomial developments reuse it.

### Proof strategy — `MvPolynomial.hasseCoeff`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the whole multi-index binomial API (`choose_eq_zero_iff`, `choose_eq_prod`, `choose_mul_choose` composition identity, which the project proves as private `hasseCoeff_mul_hasseCoeff`) | follow-up PR |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (definition via `Finsupp.prod` is the canonical way to take a finite product over a multi-index).
  - Missing mathlib API: multi-index binomial lemmas, listed in row 5.

### Diamond / defeq risk — `MvPolynomial.hasseCoeff`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | ℕ-valued function of two finsupps; no instances defined or required |
| 2 | Reducibility leak | none | plain semireducible `def`, no `@[reducible]`; unfolded only by explicit `simp [hasseCoeff]`/`rw` |
| 3 | Non-canonical unfolding | low | `rfl` exposes `Finsupp.prod`, which depends on `d.support` (classical decidability); harmless, and `hasseCoeff_eq_prod` provides the `Fintype` form |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | `σ : Type*`, no universe constraint forced (evidence file elaborates with `Type*`) |
| 6 | Coercion ambiguity | none | no `CoeFun`/`CoeSort`; a `Finsupp.choose` name would not clash (no existing `Finsupp.choose` in mathlib; `Classical.choose`/`Exists.choose` live in other namespaces and dot-notation on `σ →₀ ℕ` resolves to `Finsupp.choose`) |

### Risk verdict (Phase 4.5)

Overall risk: LOW
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `MvPolynomial.hasseCoeff`

[A] Lean-Finder       "binomial coefficient of multi-indices: product over j of (k j).choose (d j) for finitely supported functions"   no hits (only `Finsupp.multinomial`, `Nat.multinomial`, `Ring.multichoose`: different quantities)
[B] Loogle            `Finsupp.prod, Nat.choose`; `(_ →₀ ℕ) → (_ →₀ ℕ) → ℕ`   no hits
[C] LeanSearch        "multi-index binomial coefficient product over finsupp of choose"   no hits (multinomial family only)
[D] Grep mathlib src  `hasseCoeff`, `MvPolynomial.*[Hh]asse`, `choose` in `Algebra/MvPolynomial`, `RingTheory/MvPowerSeries`, `RingTheory/MvPolynomial`, `Data/Finsupp`, regex for `(k j).choose (d j)` / `prod fun j ↦ (k j).choose`   no hits (only `Polynomial.hasseDeriv`, `LaurentSeries` hasseDeriv, 2-variable `coeff_add_pow` style with `Nat.choose`)
[E] Name pattern      grep `def hasseCoeff`, `Finsupp.choose`   no hits

Searched for both the user's form and the literature-standard multi-index binomial `binom(α,β)`.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form).

### Normal-form check — `MvPolynomial.hasseCoeff`

Equivalent formalisms: `d.prod fun j ↦ (k j).choose`; `∏ j ∈ d.support, (k j).choose (d j)`; `∏ j, (k j).choose (d j)` (Fintype); `k.factorial / (d.factorial * (k-d).factorial)` when `d ≤ k`.
Does mathlib already have a canonical form? no.
Proposed canonical form: `Finsupp.choose k d` (Finsupp.prod definition) with `_eq_prod` lemma towards the Fintype product on the RHS.
RHS convention respected? yes (`hasseCoeff_eq_prod` puts the expanded form on the RHS).

### Syntactic generality — `MvPolynomial.hasseCoeff`

Alternative restatements attempted:
- `(d : σ →₀ ℕ) (k : σ → ℕ)` (compiles, evidence file)
- `Finsupp.choose (k d : σ →₀ ℕ)` (compiles, `rfl`-equal)
Chosen restatement: `Finsupp.choose k d`.
Justification: Nat.choose argument order and dot notation `k.choose d` read as `binom(k,d)`; finsupp upper index matches `d ≤ k`, `k - d`, `e + d` at every call site.

### Superfluous-argument audit — `MvPolynomial.hasseCoeff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `σ` | yes | index type |
| 2 | `d : σ →₀ ℕ` | yes | finite support bounds the product |
| 3 | `k : σ →₀ ℕ` | yes (as data); finsupp-ness not essential | could be `σ → ℕ`, kept for API uniformity |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (`Finsupp.choose k d`, top-index-first)
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseCoeff`

Internal use count: 3 direct uses of the def outside the declaring file (plus many via lemmas `hasseCoeff_eq_zero_iff`, `hasseCoeff_le_two_pow`)
External-to-file callers: 2 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/CoeffNorm.lean:139 | `have hc : (hasseCoeff d (e + d) : ℝ) ≤ 2 ^ (∑ j, r j)` |
| Roth/CoeffNorm.lean:140 | `exact_mod_cast hasseCoeff_le_two_pow ...` (lemma about the def) |
| Roth/CoeffNorm.lean:157 | `exact_mod_cast hasseCoeff_le_two_pow ...` (lemma about the def) |
| Roth/Taylor.lean:83 | `hasseCoeff d (Finsupp.single i n + k') = n.choose (d i) * hasseCoeff (d.erase i) k'` |
| Roth/Taylor.lean:85 | `rw [hasseCoeff, ← Finsupp.mul_prod_erase' d i _ (by simp), hasseCoeff]` |
| Roth/Taylor.lean:113 | `simp [(hasseCoeff_eq_zero_iff e k).2 ...]` |
| Roth/Taylor.lean:117 | `..., hasseCoeff_single_add_eq hi, ...` |

Inline-derivation grep: (none) — no occurrence of `prod fun j ↦ (k j).choose` or `∏ j, (k j).choose (d j)` outside the def and `hasseCoeff_eq_prod`.

### Composition check (Phase 6)

Can `MvPolynomial.hasseCoeff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `d.prod fun j ↦ (k j).choose` — this is the definition itself (`Finsupp.prod` + `Nat.choose`).
  - Mathlib decls used: `Finsupp.prod`, `Nat.choose`
  - Result: succeeds as a term, but inlining it at ~45 sites would lose the named anchor that statements like `coeff_hasseDeriv` and `hasseDeriv_hasseDeriv` are phrased against, and the defeq/API exemption of Phase 2b.
  - Notes: trivial composition; record as "trivial composition; user decides if worth a definition".

Conclusion: NOT-COMPOSABLE as a replacement for a named API concept (the composition is the body, but the standard named concept with its lemmas is missing from mathlib).

## Verdict: `MvPolynomial.hasseCoeff`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): multi-index binomial `binom(α,β) = ∏ binom(α_i,β_i)` is standard (Wikipedia/EoM multi-index notation; arXiv 2403.19824, 2111.07572; project paper §1).
- Generality analysis (Phase 4): MAXIMALLY GENERAL mathematically; Phase 4c MODERN-IDIOM: belongs in `Finsupp` as `choose`, not in `MvPolynomial`.
- Mathlib search (Phase 5): not in mathlib (all 5 methods).
- Composition check (Phase 6): trivial body, but no named concept to compose with; NOT-COMPOSABLE as an API replacement.

**Rationale:**

Mathlib has univariate `Polynomial.hasseDeriv` (with `(n+k).choose k` coefficients) and `Finsupp.multinomial`, but no multi-index binomial coefficient and no multivariate Hasse derivative. The concept named by `hasseCoeff` is the standard `binom(k,d)` of multi-index notation; it is polynomial-independent (Q8: the body never mentions polynomials), so the right upstream form is `Finsupp.choose (k d : σ →₀ ℕ) : ℕ` with `Nat.choose`'s top-first argument order, verified `rfl`-equal to `hasseCoeff d k` in the evidence file. The one-liner is justified by the defeq-control and API-name exemptions (Phase 2b): every Hasse-derivative coefficient lemma, the composition rule `Δ_d Δ_e = binom(d+e,d) Δ_{d+e}`, and the coefficient bound `binom(k,d) ≤ 2^{Σ r}` are stated against it. Risk is LOW (no instances, no coercions).

The concrete gap: mathlib lacks the multi-index binomial and hence any `MvPolynomial`/`MvPowerSeries` Hasse derivative, multivariate Taylor coefficient formula, or multi-index binomial theorem stated with it. It should ship only as part of a PR that also adds `MvPolynomial.hasseDeriv` (or a multi-index binomial theorem); alone it would be an orphan one-liner.

Reason for the generalisation: MODERN-IDIOM (namespace and argument order; Q7/Q8).
Proposed restatement:
```lean
namespace Finsupp
/-- The multi-index binomial coefficient `binom(k, d) = ∏ j, (k j).choose (d j)`. -/
def choose (k d : σ →₀ ℕ) : ℕ := d.prod fun j ↦ (k j).choose
theorem choose_eq_zero_iff (k d : σ →₀ ℕ) : k.choose d = 0 ↔ ¬d ≤ k := by sorry
theorem choose_eq_prod [Fintype σ] (k d : σ →₀ ℕ) : k.choose d = ∏ j, (k j).choose (d j) := by sorry
end Finsupp
```
Estimated cost of regeneralisation: MODERATE (def CHEAP; rename and argument swap at ~45 occurrences across Roth/HasseDeriv.lean, Roth/CoeffNorm.lean, Roth/Taylor.lean if adopted locally).
Mathlib downstream this enables:
- `MvPolynomial.hasseDeriv` / multivariate Taylor coefficients stated with `k.choose d`;
- multi-index binomial theorem and Vandermonde over `Finsupp.antidiagonal`, next to `Finsupp.multinomial`;
- the composition identity `binom(f+d,d)·binom(f+d+e,e) = binom(d+e,d)·binom(f+d+e,d+e)` (project's private `hasseCoeff_mul_hasseCoeff`) as a reusable `Finsupp.choose_mul_choose`.
Next action: run `/generalise MvPolynomial.hasseCoeff`, then upstream as `Finsupp.choose` in `Mathlib/Data/Nat/Choose/Multinomial.lean` (or a new `Mathlib/Data/Finsupp/Choose.lean`) bundled with the `MvPolynomial.hasseDeriv` PR; PR title "feat(Data/Finsupp): multi-index binomial coefficient `Finsupp.choose`".

---

## Next step

Run `/generalise MvPolynomial.hasseCoeff`; upstream as `Finsupp.choose k d` together with `MvPolynomial.hasseDeriv`, porting `hasseCoeff_eq_zero_iff`, `hasseCoeff_eq_prod`, `hasseCoeff_mul_hasseCoeff`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/restate_finsupp_choose.lean` (compiles with `lake env lean`, no errors): `Finsupp.choose k d` is `rfl`-equal to `hasseCoeff d k` and `choose_eq_zero_iff` ports in one line; the weakening `k : σ → ℕ` compiles with `hasseCoeff'_eq_zero_iff : … ↔ ∃ j, k j < d j`.
- Mathlib greps (`hasseCoeff`, `[Hh]asse` in MvPolynomial/MvPowerSeries, `choose` in Finsupp/MvPolynomial dirs, product-of-choose regexes): no hits beyond `Polynomial.hasseDeriv`, `LaurentSeries` hasseDeriv, `Finsupp.multinomial`.
- LeanSearch / Lean-Finder: only multinomial family; Loogle: two queries, no hits.
- WebSearch: 4 queries (results summarised in the literature table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseCoeff Roth/` for the call-sites table.
