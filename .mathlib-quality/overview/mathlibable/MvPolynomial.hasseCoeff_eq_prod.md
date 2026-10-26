---
decl: MvPolynomial.hasseCoeff_eq_prod
file: Roth/HasseDeriv.lean
line: 106
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: The full-product formula binom(k,d) = prod over all j of binom(k_j,d_j) is the literature definition of the multi-index binomial and the bridge from the support-indexed Finsupp.prod to Finset.prod API; absent from mathlib, it should ship with the parent Finsupp.choose in the mathlib idiom choose_eq_prod_of_support_subset (any finset s containing d.support, mirroring Finsupp.multinomial_eq_of_support_subset) plus the Fintype corollary choose_eq_prod.
action: Upstream in the Finsupp.choose PR (parent MvPolynomial.hasseCoeff; Mathlib/Data/Nat/Choose/Multinomial.lean or new Mathlib/Data/Finsupp/Choose.lean) as Finsupp.choose_eq_prod_of_support_subset and Finsupp.choose_eq_prod; locally keep (single call site Roth/HasseDeriv.lean:278 in hasseCoeff_le_two_pow).
---

# MvPolynomial.hasseCoeff_eq_prod

## Inventory entry

### `theorem MvPolynomial.hasseCoeff_eq_prod`
- **Type**: `∀ {σ : Type*} [Fintype σ] (d k : σ →₀ ℕ), hasseCoeff d k = ∏ j, (k j).choose (d j)`
- **What**: Over a finite index type, the multi-index binomial `hasseCoeff d k` (defined as a product over `d.support`) equals the full product `∏_j binom(k_j, d_j)` over all variables.
- **How**: Term proof `d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _`: mathlib's `Finsupp.prod_fintype` applied with the side condition `binom(n, 0) = 1` (`Nat.choose_zero_right`).
- **Hypotheses**: `[Fintype σ]` (finite set of variables); the section `[CommSemiring R]` is not included.
- **Uses from project**: `MvPolynomial.hasseCoeff`
- **Used by**: Roth/HasseDeriv.lean: `hasseCoeff_le_two_pow` (l.278). No other use in `Roth/`.
- **Visibility**: public
- **Lines**: 106–107, proof length 1 line
- **Notes**: Not a glue lemma (needs `Finsupp.prod_fintype` plus `Nat.choose_zero_right`, not `rfl`), so the full workflow was run. `[Fintype σ]` is stronger than needed: any finset `s ⊇ d.support` suffices (evidence file).

## Junk check (Step 8)
- Used anywhere? Yes, once (`hasseCoeff_le_two_pow`, Roth/HasseDeriv.lean:278, to convert to a `Finset.prod` for `Finset.prod_le_prod` / `Finset.prod_pow_eq_pow_sum`).
- Wrapper of 1–2 mathlib calls? Yes: one call to `Finsupp.prod_fintype` with `Nat.choose_zero_right`. But it is the standard "unfold to product" API lemma of a named definition, the analogue of mathlib's `Finsupp.multinomial_eq` / `Nat.multinomial`-style bridge lemmas, and it hides the definition's `Finsupp.prod` implementation detail.
- Does mathlib have it? No (no multi-index binomial in mathlib; see Phase 5).
- Too specific / inline? Could be inlined at its one call site (`simp [hasseCoeff, Finsupp.prod_fintype]` works, evidence file), but that breaks the definition's abstraction; it is also the literature definition of the parent, so it belongs in the parent's API.
- Well-chosen? Yes, modulo the over-strong `[Fintype σ]` (a `support ⊆ s` form is the mathlib idiom).
- Conclusion: `KEEP` — action: keep locally; when upstreaming, add the `_of_support_subset` form and derive this as the `Fintype` corollary.

## Mathlibable assessment (Step 9)

Not a glue lemma, so the full `/mathlibable` workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.HasseDeriv` compiles)
- decl `MvPolynomial.hasseCoeff_eq_prod`: resolved at Roth/HasseDeriv.lean:106
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseCoeff_eq_prod` is a theorem stating the following:

Let `σ` be a finite set of variables and `d, k ∈ ℕ^σ` multi-indices. The multi-index binomial coefficient `binom(k, d)`, defined in the project as the product of `binom(k_j, d_j)` over the support of `d`, equals the product `∏_{j ∈ σ} binom(k_j, d_j)` over all variables (the extra factors are `binom(k_j, 0) = 1`).

Variables / typeclasses involved (Lean side):
- `σ : Type*` with `[Fintype σ]` — the finite set of variables.
- `d : σ →₀ ℕ` — lower multi-index.
- `k : σ →₀ ℕ` — upper multi-index.

Hypotheses (Lean side):
- `[Fintype σ]` only.

Conclusion (math): `binom(k, d) = ∏_j binom(k_j, d_j)`.

Conclusion (Lean): `hasseCoeff d k = ∏ j, (k j).choose (d j)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: basic API (unfolding-to-product) lemma for a helper definition; not a main result.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | multi-index binomial coefficient "alpha choose beta" product over i of alpha_i choose beta_i definition | yes | `binom(α,β) = ∏_{i=1}^n binom(α_i,β_i) = α!/(β!(α-β)!)` | Wikipedia "Multi-index notation"; ProofWiki "Definition:Binomial Coefficient/Multiindices" (notes the product is finite because only finitely many components are nonzero); arXiv 0708.0780, 0708.1711 |
| 2 | WebSearch (general form) | multinomial notation binomial coefficient vector componentwise product convention binom(0,0)=1 finitely supported multi-index | yes | componentwise product; factors with `β_i = 0` equal 1 | Encyclopedia of Math "Multi-index notation"; no source treats infinitely many variables explicitly, but the finite-support restriction is exactly what our `Finsupp.prod` form encodes |
| 3 | WebSearch (named-after / aliases) | multivariate Hasse derivative coefficient product of binomial coefficients over all variables finite number of variables | yes | `H(F,i) = Σ_{j ≥ i} f_j ∏_t binom(j_t,i_t) X^{j-i}` | arXiv 2403.19824, 1412.5012, 2111.07572, 2603.03841: product over all `n` variables is the definition used |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `choose` | yes | l.122-134: `Δ_i x^k = (∏_{j=1}^p binom(k_j,i_j)) x^{k-i}`; l.460: `∏_j binom(s(i)_j, d_j)` bound | the paper's definition is exactly this full-product form over `p` variables; l.460 is the call site's use |
| 6 | nLab | Hasse–Schmidt derivative / multi-index | partial | several-variable HS derivatives, no multi-index binomial product identity | elementary combinatorics below nLab's granularity |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | elementary combinatorics, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1–#2 on multi-index binomial product) | no | — | no dedicated thread; the product form is the definition everywhere |
| 10 | recent arXiv (last 5 years) | (results of #3) | yes | arXiv 2403.19824 (2024), 2111.07572 (2021), 2603.03841 (2026) | all define the multi-index binomial as the product over all coordinates |

### Literature summary (Phase 3)

Concept identified as: multi-index binomial coefficient `binom(α, β) = ∏_i binom(α_i, β_i)` (multi-index notation).
Sources agree on the standard form: yes — the full componentwise product over the (finite) index set is the definition everywhere.
Most general standard form: for multi-indices on any index set with finite support, `binom(α,β)` equals the product of `binom(α_i,β_i)` over any finite set of indices containing the support of `β` (the extra factors are `binom(α_i,0) = 1`).
Generality dimensions where the literature varies:
  - index set: finite `{1,…,n}` in the literature; finitely supported over an arbitrary type here.
  - product range: all coordinates (literature) versus support of `β` (project definition); both agree.
Disagreement with the literature: none; this lemma is precisely the reconciliation of the project definition with the literature definition.

### Generality analysis — `MvPolynomial.hasseCoeff_eq_prod`

Literature-standard form (from Phase 3): `binom(k,d) = ∏_{j ∈ s} binom(k_j,d_j)` for any finite `s ⊇ supp d`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype σ]` | finite variable type, product over `univ` | any finset `s` with `d.support ⊆ s` | yes (verified) | `hasseCoeff_eq_prod_of_support_subset (h : d.support ⊆ s)` compiles via `Finsupp.prod_of_support_subset`; the Fintype form is its corollary with `subset_univ` (evidence file) |
| 2 | `d k : σ →₀ ℕ` | finsupps | multi-indices | `k : σ → ℕ` possible (parent evidence) | not recommended: parent report keeps `k` a finsupp |
| 3 | section `[CommSemiring R]` | not included | none | — | — |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN STANDARD (in the mild, mathlib-idiom sense: `[Fintype σ]` replaced by `d.support ⊆ s`).
Number of weakening opportunities found: 1 (verified, evidence file compiles).
Proposed restatement:
```lean
theorem Finsupp.choose_eq_prod_of_support_subset {k d : σ →₀ ℕ} {s : Finset σ}
    (h : d.support ⊆ s) : k.choose d = ∏ j ∈ s, (k j).choose (d j) :=
  d.prod_of_support_subset h _ fun _ _ ↦ Nat.choose_zero_right _

theorem Finsupp.choose_eq_prod [Fintype σ] (k d : σ →₀ ℕ) :
    k.choose d = ∏ j, (k j).choose (d j) :=
  choose_eq_prod_of_support_subset (Finset.subset_univ _)
```
Cost of restatement: CHEAP — mechanical; both compile.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | only hypothesis is already a typeclass |
| 2 | sequences to filters? | no | — | finite combinatorial identity |
| 3 | construction vs universal property? | no | — | a number |
| 4 | set-with-predicate to bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | ℕ-valued |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | yes | `Finsupp.choose_eq_prod_of_support_subset` (any finset containing the support), matching mathlib's `Finsupp.multinomial_eq_of_support_subset` / `Finsupp.multinomial_of_support_subset` pattern | usable for infinite `σ` (e.g. `MvPolynomial ℕ R`) after restricting to a finset; composes with all `Finset.prod` API |
| 8 | concrete-via-abstract? | yes (inherited) | proof never mentions polynomials; belongs in `Finsupp` as `Finsupp.choose` API (parent report) | as #7 |
| 9 | false-generalisation guard | no false generalisation | `Finsupp.choose k d` is `rfl`-equal to `hasseCoeff d k` (evidence file); the Fintype form is recovered exactly | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `Finsupp.choose_eq_prod_of_support_subset {k d} {s} (h : d.support ⊆ s) : k.choose d = ∏ j ∈ s, (k j).choose (d j)` plus `Finsupp.choose_eq_prod [Fintype σ] (k d)`.
  - Cost: CHEAP (both compile, one-line proofs)
  - Mathlib downstream this enables: `Finset.prod_le_prod`, `Finset.prod_pow_eq_pow_sum`, `Finset.prod_congr` and the rest of the `Finset.prod` API on multi-index binomials (as at the call site); the multi-index binomial theorem / Vandermonde identity stated over `Finset.Iic k`; consistent with `Finsupp.multinomial_eq_of_support_subset`.
  - Real mathematical improvement: removes the needless finiteness of the variable set and places the lemma in the namespace and naming pattern mathlib already uses for the sibling `Finsupp.multinomial`.

### Proof strategy — `MvPolynomial.hasseCoeff_eq_prod`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `Finsupp.prod_fintype` / `Finsupp.prod_of_support_subset` with `Nat.choose_zero_right` suffice | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (single application of `Finsupp.prod_fintype`). For the generalised form use `Finsupp.prod_of_support_subset` and derive the Fintype form by `Finset.subset_univ`.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseCoeff_eq_prod`

[A] Lean-Finder       "multi-index binomial coefficient equals product over all coordinates of binomial coefficients k_j choose d_j"   no multi-index hit (returns `Ring.multichoose`, `Nat.multinomial`, `Finsupp.multinomial`, `Nat.binomial_eq_choose`: different quantities)
[B] Loogle            `Finsupp.prod, Nat.choose, Finset.univ`   no hits
[C] LeanSearch        "Finsupp.prod over finite type equals product over univ when g i 0 = 1"   building blocks only: `Finsupp.prod_fintype`, `Finsupp.prod_of_support_subset`, `Finsupp.onFinset_prod`, `DFinsupp.prod_eq_prod_fintype`
[D] Grep mathlib src  `choose_eq_prod`, `hasseCoeff`, `Finsupp.choose`, `def choose` across `.lake/packages/mathlib/Mathlib`   no multi-index binomial (only `Ring.choose`, tactic `choose`); closest analogue `Finsupp.multinomial_eq_of_support_subset` (Data/Nat/Choose/Multinomial.lean:208)
[E] Name pattern      `choose_eq_prod` (lean_local_search unavailable: ripgrep not on PATH; replaced by the grep in [D])   no hits

Searched for both the user's form (Fintype product) and the literature/mathlib-idiomatic form (support-subset product).

Concluded: found building blocks (`Finsupp.prod_fintype`, `Finsupp.prod_of_support_subset`, `Nat.choose_zero_right`); the parent concept is not in mathlib, so neither is this lemma.

### Normal-form check — `MvPolynomial.hasseCoeff_eq_prod`

Equivalent formalisms this statement could take: product over `univ`; product over any `s ⊇ d.support`; product over `d.support` (the definition, `rfl`); `α!/(β!(α-β)!)` when `d ≤ k`.
Does mathlib already have a canonical form for this idea? For the sibling `Finsupp.multinomial`, mathlib states `multinomial_eq` (support form) and `multinomial_eq_of_support_subset` (arbitrary finset).
Our statement is stated against the canonical form? yes (LHS the named def, RHS the explicit `Finset.prod`); it should add the `_of_support_subset` variant.
RHS convention respected? yes

### Syntactic generality — `MvPolynomial.hasseCoeff_eq_prod`

Alternative restatements attempted:
- `hasseCoeff_eq_prod_of_support_subset {d k} {s} (h : d.support ⊆ s)` (compiles)
- `Finsupp.choose_eq_prod_of_support_subset` and `Finsupp.choose_eq_prod` (compile)
Chosen restatement: both `Finsupp` forms; the Fintype form keeps explicit `(k d)` for `rw` at call sites like l.278.
Justification: the Fintype form is directly rewritable without side goals; the subset form serves infinite `σ`.

### Superfluous-argument audit — `MvPolynomial.hasseCoeff_eq_prod`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | only to form `∏ j` over `univ` | replaceable by `d.support ⊆ s` (verified) |
| 2 | `d`, `k` | yes | — |
| 3 | section `[CommSemiring R]` | not included | — |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (add `_of_support_subset` form, derive this from it; move to `Finsupp.choose`)
Superfluous arguments: NONE in the Fintype corollary itself (finiteness is what `∏ j` needs); generalised by the subset form

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseCoeff_eq_prod`

Internal use count: 0 outside the declaring file (1 total)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/HasseDeriv.lean:278 | `rw [hasseCoeff_eq_prod, ← Finset.prod_pow_eq_pow_sum]` (in `hasseCoeff_le_two_pow`) |

Inline-derivation grep: (none) — `grep -rn "prod_fintype" Roth/` finds only this lemma; Roth/HasseDeriv.lean:271 (`uniqueAlgEquiv_hasseDeriv`) and Roth/Taylor.lean:83 unfold `hasseCoeff` directly via `simp [hasseCoeff, …]`/`Finsupp.prod` lemmas on singletons, not the full-product form.

### Composition check (Phase 6)

Can `MvPolynomial.hasseCoeff_eq_prod` be derived from mathlib in ≤3 chained calls?

Attempt 1: `d.prod_fintype _ fun _ ↦ Nat.choose_zero_right _` (the current proof)
  - Mathlib decls used: `Finsupp.prod_fintype`, `Nat.choose_zero_right`
  - Result: succeeds (evidence file)
  - Notes: one call, but it requires unfolding the non-mathlib definition `hasseCoeff`.

Attempt 2: `simp [hasseCoeff, Finsupp.prod_fintype]` at the call site
  - Result: succeeds (evidence file)

Conclusion: COMPOSABLE as a proof, but as the definition-to-literature bridge of a new definition (which mathlib lacks) it is NOT-COMPOSABLE as a call-site replacement — inlining would re-expose the `Finsupp.prod` implementation of `hasseCoeff`. Recorded as "trivial composition; standard API lemma of the parent def".

## Verdict: `MvPolynomial.hasseCoeff_eq_prod`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): the multi-index binomial is defined everywhere as the full product `∏_i binom(α_i,β_i)` (Wikipedia, ProofWiki, Encyclopedia of Math, arXiv 2403.19824/1412.5012, project paper l.127).
- Generality analysis (Phase 4): STRICTLY NARROWER (mathlib idiom): `[Fintype σ]` replaced by `d.support ⊆ s`, verified to compile; Phase 4c MODERN-IDIOM: `Finsupp` namespace, mirroring `Finsupp.multinomial_eq_of_support_subset`.
- Mathlib search (Phase 5): not in mathlib; building blocks `Finsupp.prod_fintype`, `Finsupp.prod_of_support_subset`, `Nat.choose_zero_right`.
- Composition check (Phase 6): trivial composition, but it is the characterising product formula of a new definition, so not replaceable at call sites without exposing the definition.

**Rationale:**

The parent `MvPolynomial.hasseCoeff` was assessed YES-but-generalise-first (upstream as `Finsupp.choose k d`). The project defines it as a product over `d.support` (the only form that makes sense for arbitrary `σ`), while the literature definition is the product over all coordinates; this lemma is exactly the bridge, and it is what any user of `Finsupp.choose` needs to bring `Finset.prod` API to bear (as at the one call site, which uses `Finset.prod_pow_eq_pow_sum` and `Finset.prod_le_prod`). The concrete mathlib gap is the absence of a multi-index binomial and hence of its product formula; mathlib's sibling `Finsupp.multinomial` has precisely this pair of lemmas (`multinomial_eq`, `multinomial_eq_of_support_subset`), which fixes the expected shape.

The generalisation is a cheap mathlib-idiom move: state it for any finset `s ⊇ d.support` (works for infinite `σ`), derive the `Fintype` version by `Finset.subset_univ`, and place both in `Finsupp`. It should ship only bundled with the parent definition, not alone.

Reason for the generalisation: LITERATURE-WEAKENING (drop `[Fintype σ]` in favour of a support-subset hypothesis) and MODERN-IDIOM (namespace/naming matching `Finsupp.multinomial_eq_of_support_subset`); Phase 5.5 RESTATE-BEFORE-SHIP.
Proposed restatement:
```lean
namespace Finsupp
theorem choose_eq_prod_of_support_subset {k d : σ →₀ ℕ} {s : Finset σ} (h : d.support ⊆ s) :
    k.choose d = ∏ j ∈ s, (k j).choose (d j) :=
  d.prod_of_support_subset h _ fun _ _ ↦ Nat.choose_zero_right _
theorem choose_eq_prod [Fintype σ] (k d : σ →₀ ℕ) : k.choose d = ∏ j, (k j).choose (d j) :=
  choose_eq_prod_of_support_subset (Finset.subset_univ _)
end Finsupp
```
Estimated cost of regeneralisation: CHEAP (both compile; the single call site at Roth/HasseDeriv.lean:278 keeps working with `Finsupp.choose_eq_prod` if the parent rename is adopted).
Mathlib downstream this enables:
- the full `Finset.prod` API (`prod_le_prod`, `prod_pow_eq_pow_sum`, `prod_congr`, `prod_mul_distrib`) on multi-index binomials, e.g. bounds `binom(k,d) ≤ 2^{|r|}`;
- the multi-index binomial theorem and Vandermonde identity stated over a common finset, for infinite variable types via `_of_support_subset`;
- API parity with `Finsupp.multinomial_eq_of_support_subset`.
Next action: run `/generalise MvPolynomial.hasseCoeff_eq_prod` together with the parent; upstream in the same PR as `Finsupp.choose` (Mathlib/Data/Nat/Choose/Multinomial.lean or new Mathlib/Data/Finsupp/Choose.lean), PR title "feat(Data/Finsupp): multi-index binomial coefficient `Finsupp.choose`".

---

## Next step

Ship as `Finsupp.choose_eq_prod_of_support_subset` plus `Finsupp.choose_eq_prod` in the `Finsupp.choose` PR (parent `MvPolynomial.hasseCoeff`); locally optionally add `hasseCoeff_eq_prod_of_support_subset` and derive this lemma from it.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff_eq_prod/support_subset_and_finsupp_choose.lean` (compiles with `lake env lean`, no errors): `hasseCoeff_eq_prod_of_support_subset` and the Fintype corollary; composition checks (`Finsupp.prod_fintype` term and `simp [hasseCoeff, Finsupp.prod_fintype]`); `Finsupp.choose_eq_prod_of_support_subset`, `Finsupp.choose_eq_prod`, and `rfl` agreement of `Finsupp.choose` with `hasseCoeff`.
- Parent evidence `.mathlib-quality/overview/evidence/MvPolynomial.hasseCoeff/restate_finsupp_choose.lean`.
- Mathlib grep for `choose_eq_prod`, `hasseCoeff`, `Finsupp.choose`, `def choose`: no multi-index binomial; analogue `Finsupp.multinomial_eq_of_support_subset` (Mathlib/Data/Nat/Choose/Multinomial.lean:208).
- LeanSearch: `Finsupp.prod_fintype`, `Finsupp.prod_of_support_subset` (building blocks); Lean-Finder: only `Nat.multinomial`/`Finsupp.multinomial`/`Ring.multichoose`; Loogle `Finsupp.prod, Nat.choose, Finset.univ`: no hits. `lean_local_search` unavailable (ripgrep not on PATH).
- WebSearch: 3 queries (summarised in the literature table). ChatGPT MCP: n/a (not configured).
- Project grep `grep -rn hasseCoeff_eq_prod Roth/` and `grep -rn prod_fintype Roth/` for the call-sites table.
