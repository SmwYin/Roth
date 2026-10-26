---
decl: MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint
file: Roth/HasseDeriv.lean
line: 185
kind: theorem
visibility: public
verdict: YES-but-generalise-first
cost: CHEAP
junk: KEEP
rationale: Disjoint-support special case Delta_d Delta_e = Delta_(d+e) of the Hasse composition law (binomial factor is 1 exactly when supports are disjoint, verified sharp); absent from mathlib, not simp-composable, and should ship next to the parent's operator-form hasseDeriv_comp as hasseDeriv_comp_of_disjoint with this pointwise lemma as corollary.
action: Upstream with MvPolynomial.hasseDeriv_hasseDeriv into new Mathlib/Algebra/MvPolynomial/HasseDeriv.lean, adding operator form `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv (d + e)` (verified in evidence variants.lean) and an order-form `Disjoint d e` variant via Finsupp.disjoint_iff; locally keep as is (caller Roth/Separation.lean:156).
---

# MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint

## Inventory entry

### `theorem MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] {d e : σ →₀ ℕ}, Disjoint d.support e.support → ∀ (P : MvPolynomial σ R), hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P`
- **What**: If the multi-indices `d` and `e` involve disjoint sets of variables, then `Δ_d Δ_e = Δ_{d+e}` (the binomial factor of the composition law is `1`).
- **How**: `rw [hasseDeriv_hasseDeriv]`, then show `hasseCoeff d (d + e) = 1` by `Finset.prod_eq_one` over `d.support`, each factor being `(d i + 0).choose (d i) = 1` via `Finsupp.notMem_support_iff` and `Finset.disjoint_left`; finish with `Nat.cast_one`, `one_smul`.
- **Hypotheses**: `h : Disjoint d.support e.support`.
- **Uses from project**: `MvPolynomial.hasseDeriv`, `MvPolynomial.hasseDeriv_hasseDeriv`, `MvPolynomial.hasseCoeff`
- **Used by**: Roth/Separation.lean:156 (`hasseDeriv_rename_mul_aeval`, `rw [← hasseDeriv_hasseDeriv_of_disjoint hdisj, ...]`). No other use in `Roth/` (also referenced in the docstring of `hasseDeriv_hasseDeriv`, Roth/HasseDeriv.lean:172).
- **Visibility**: public
- **Lines**: 185–189, proof length 3 lines
- **Notes**: Mathlib has no multivariate Hasse derivative; univariate disjointness is trivial (one index is 0), so there is no univariate analogue.

## Junk check (Step 8)
- Used anywhere? Yes: Roth/Separation.lean:156 (separation of variables, paper §2 Lemma 2).
- Wrapper of 1–2 mathlib calls? No: it wraps the project lemma `hasseDeriv_hasseDeriv` plus a support argument; `simp [hasseDeriv_hasseDeriv, hasseCoeff]` does not close it (evidence item 5).
- Does mathlib have it? No (no `MvPolynomial.hasseDeriv` at all; loogle `"hasseDeriv", Disjoint` empty).
- Too specific / inline? No: it is the natural "derivatives in different variables compose" law and is used with `rw [← ...]`, which is much cleaner than inlining the coefficient computation.
- Well-chosen? Yes; hypothesis is sharp (evidence item 3).
- Conclusion: `KEEP` — keep; upstream with the parent.

## Mathlibable assessment (Step 9)

Real content (not `rfl` glue: it computes a binomial product), so the full workflow was run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.HasseDeriv` elaborates with no diagnostics)
- decl `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`: resolved at Roth/HasseDeriv.lean:185
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Multivariate Hasse derivatives `Δ_d` on `MvPolynomial σ R` and their basic calculus.

### Statement (Phase 1)

`MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` is a theorem stating the following:

Let `R` be a commutative semiring and `d, e ∈ ℕ^(σ)` multi-indices such that no variable occurs in both (`supp d ∩ supp e = ∅`). Then for every polynomial `P ∈ R[X_σ]`, `Δ_d(Δ_e P) = Δ_{d+e} P`. Equivalently, Hasse derivatives in disjoint sets of variables compose to the mixed Hasse derivative, with no binomial correction.

Variables / typeclasses involved (Lean side):
- `σ : Type*` — variables; `R : Type*`, `[CommSemiring R]` — coefficients.
- `d e : σ →₀ ℕ` — derivative orders; `P : MvPolynomial σ R`.

Hypotheses (Lean side):
- `h : Disjoint d.support e.support` — the two derivatives act on disjoint variable sets.

Conclusion (math): `Δ_d Δ_e P = Δ_{d+e} P`.

Conclusion (Lean): `hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: corollary of the composition law `hasseDeriv_hasseDeriv` (API lemma of the BIG parent `MvPolynomial.hasseDeriv`).

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3
One-liner verdict: n/a (kind is theorem, not def)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Hasse derivative multi-index disjoint support composition D_i D_j = D_{i+j} variables | partial | nLab "Hasse-Schmidt derivative": multivariate Hasse derivative indexed by a multiset of variables, order of variables irrelevant, monomial formula a product of per-variable binomials; composition `D_α D_β = binom(α+β, α) D_{α+β}`, factor 1 for disjoint supports | Wikipedia "Hasse derivative"; arXiv math/0510235 (Moosa–Scanlon: mixed derivatives `D_α` of commuting iterative HS derivations determined by iteration rule + commutation) |
| 2 | WebSearch (general form) | Hasse derivatives in different variables commute product D^(i) in x and D^(j) in y equals mixed Hasse derivative | partial | mixed Hasse derivative `D^γ` with multinomial `binom(α, γ)` (arXiv 0807.4332); `D_x^(i) D_y^(j) = D^(i,j)` follows by the monomial computation | arXiv 1303.0084, 2003.09694; no source isolates the disjoint case as a lemma — it is folklore / immediate from the general law |
| 3 | WebSearch (named-after / aliases) | iterative Hasse-Schmidt derivation binomial coefficient equals one Lucas theorem characteristic p composition | no | — | only background (Lucas' theorem, HS derivations in char p, arXiv 1807.10502, 2001.06869); the char-p "binomial ≡ 1" weakening is not a standard formulation |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for hasse / disjoint | yes | l.579–582 general composition identity `Δ_i Δ_k P = (∏_j binom(i_j+k_j, i_j)) Δ_{i+k} P`; l.632 ("the disjoint-variable formula ... as separate lemmas") explicitly asks for this lemma | §2 Lemma 2 separation argument (l.424–435) is the consumer |
| 6 | nLab | Hasse-Schmidt derivative | yes | multivariate Hasse derivative over a multiset of variables; per-variable binomial product ⇒ disjoint-variable composition is plain product | — |
| 7 | nCatLab | (same page) | partial | iterativity as coaction of the additive formal group; disjoint variables = product of independent coactions | no extra statement |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry statement; Stacks has no Hasse-derivative tag |
| 9 | MathOverflow / Math.SE | (results of #1–#2) | no | — | no dedicated thread; folklore |
| 10 | recent arXiv (last 5 years) | (results of #1, #3) | partial | arXiv 2504.04433 (2025, multivariable composition), 2305.04537 | general multi-index law only |

### Literature summary (Phase 3)

Concept identified as: Hasse derivatives in disjoint sets of variables commute and compose to the mixed derivative; special case of iterativity `D_α D_β = binom(α+β, α) D_{α+β}` where the multi-index binomial is 1.
Sources agree on the standard form: yes (stated as folklore / immediate corollary; the source paper requests it as a separate lemma, clean.tex l.632).
Most general standard form: for any commutative (semi)ring, any multi-indices with disjoint supports; as an operator identity.
Generality dimensions where the literature varies:
  - form: operator vs pointwise (as for the parent law).
  - hypothesis: disjoint supports (characteristic-free, sharp over ℤ) vs "binom(α+β, α) = 1 in R" (char-p, Lucas); the latter is not a standard formulation.
Disagreement with the literature: none.

### Generality analysis — `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

Literature-standard form (from Phase 3): `Δ_d ∘ Δ_e = Δ_{d+e}` for multi-indices with disjoint supports over a commutative semiring.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[CommSemiring R]` | commutative semiring | commutative semiring | no | forced by `MvPolynomial` (parent evidence `MvPolynomial.hasseDeriv/weaken_semiring_fails.lean`) |
| 2 | `h : Disjoint d.support e.support` | disjoint supports | disjoint supports | only char-dependently | over ℕ the hypothesis is equivalent to `hasseCoeff d (d + e) = 1` (evidence item 3, compiled); the weaker `(hasseCoeff d (d + e) : R) = 1` also works (item 4) but is just `hasseDeriv_hasseDeriv` + `one_smul`, not a standard form, and awkward at call sites |
| 3 | `h` spelling | `Disjoint d.support e.support` | — | equivalent | `Disjoint d e` (Finsupp lattice order) via `Finsupp.disjoint_iff` (evidence item 1) |
| 4 | statement level | pointwise in `P` | operator identity | yes (form) | `LinearMap.ext` of the current lemma (evidence item 2) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (in the characteristic-free sense; hypothesis verified sharp, item 3).
Number of weakening opportunities found: 0 standard hypothesis weakenings (the char-p weakening, item 4, compiles but is not literature-standard and not recommended); 1 verified restatement to the operator normal form (item 2).
Cost of restatement: CHEAP — mechanical (items 1–2 compile, no diagnostics).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | single Prop hypothesis |
| 2 | sequences to filters? | no | — | algebraic identity |
| 3 | construction vs universal property? | no | — | — |
| 4 | set-with-predicate to bundled substructure? | partial | hypothesis `Disjoint d e` in the lattice `σ →₀ ℕ` instead of on supports | `Finsupp.disjoint_iff`, lattice API (`inf`, `Disjoint.mono`); call site Separation.lean:156 builds support-disjointness directly, so keep both spellings or the support one |
| 5 | field-specific to semiring? | no | already `CommSemiring` | — |
| 6 | higher-categorical / operator? | yes | `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv (d + e)` in `Module.End` | consistent with the parent's proposed `hasseDeriv_comp` normal form (Polynomial.hasseDeriv_comp shape); gives commutation of the operators and composition of a finite family of single-variable Hasse derivatives into `Δ_d` |
| 7 | concrete index to general? | no | multi-indices already arbitrary `σ →₀ ℕ` | — |
| 8 | concrete-via-abstract? | no | proof is about the operator itself (one rewrite + binomial product) | — |
| 9 | false-generalisation guard | no false generalisation | operator and pointwise forms interderivable; `Disjoint d e ↔ Disjoint d.support e.support` is a mathlib iff | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes
  - Proposed mathlib-idiomatic restatement: `theorem hasseDeriv_comp_of_disjoint {d e : σ →₀ ℕ} (h : Disjoint d.support e.support) : (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e = hasseDeriv (d + e)`, with the pointwise lemma as corollary.
  - Cost: CHEAP
  - Mathlib downstream this enables: same normal form as the parent `hasseDeriv_comp` (and `Polynomial.hasseDeriv_comp`); `LinearMap`/`Module.End` rewriting, e.g. writing `Δ_d` as a composite `∏_j Δ_{d_j e_j}` of single-variable derivatives.
  - Real mathematical improvement: states the law as an identity of operators, matching the parent's normal form.

### Proof strategy — `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes (minor) | with the parent's `Finsupp.choose`, a lemma `Finsupp.choose_add_eq_one_of_disjoint` / `(d + e).choose d = 1 ↔ Disjoint d e` would make the proof a one-line `rw` (evidence item 3 proves the iff direction via `Nat.choose_eq_one_iff`) | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (specialise the general law, compute the factor).
  - Missing mathlib API: a multi-index `choose = 1 ↔ disjoint` lemma to ship with `Finsupp.choose`.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

[A] Lean-Finder       "Hasse derivatives with respect to disjoint sets of variables compose to the Hasse derivative of the sum of multi-indices"   `Polynomial.hasseDeriv_comp`, `LaurentSeries.hasseDeriv_comp(_coeff)`, `Polynomial.hasseDeriv_mul`, `MvPolynomial.pderiv_sumToIter`; nothing multivariate-Hasse
[B] Loogle            `"hasseDeriv", Disjoint`   no hits
[C] LeanSearch        "composition of Hasse derivatives equals Hasse derivative of sum when binomial coefficient is one"   `Polynomial.hasseDeriv_comp`, `LaurentSeries.hasseDeriv`, `LaurentSeries.hasseDeriv_comp`; nothing multivariate
[D] Grep mathlib src  `hasseDeriv` (only Algebra/Polynomial/HasseDeriv.lean, Algebra/Polynomial/Taylor.lean, RingTheory/LaurentSeries.lean); `hasseDeriv_hasseDeriv_of_disjoint`, `hasseDeriv_comp_of_disjoint`: no hits; building block `Finsupp.disjoint_iff` (Mathlib/Data/Finsupp/Order.lean:333), `Nat.choose_eq_one_iff`
[E] Name pattern      `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`, `MvPolynomial.hasseDeriv_comp_of_disjoint` (namespace-aware grep of `.lake/packages/mathlib/Mathlib`)   no hits

Searched for both the user's pointwise form and the operator / mixed-derivative form.

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form); the parent operator is absent from mathlib.

### Normal-form check — `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

Equivalent formalisms this statement could take: pointwise (current); operator `∘ₗ`; hypothesis on supports vs `Disjoint d e` in the lattice.
Does mathlib already have a canonical form for this idea? For the general law, yes: `Polynomial.hasseDeriv_comp` (operator form). No disjoint analogue.
Our statement is stated against the canonical form? partially (pointwise) → add operator form `hasseDeriv_comp_of_disjoint`, keep pointwise as corollary.
RHS convention respected? yes (composite on LHS, single derivative on RHS; the call site rewrites right-to-left with `←`, which is fine).

### Syntactic generality — `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

Alternative restatements attempted:
- `Disjoint d e` hypothesis (evidence item 1, compiles)
- operator form (item 2, compiles)
- `(hasseCoeff d (d + e) : R) = 1` hypothesis (item 4, compiles)
Chosen restatement: keep `Disjoint d.support e.support` (the only caller constructs it via `Finset.disjoint_left`) and add the operator form.
Justification: support disjointness is what call sites naturally prove; the order-form variant is one `Finsupp.disjoint_iff` away and can be offered as a second spelling.

### Superfluous-argument audit — `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[CommSemiring R]` | yes | required by `MvPolynomial σ R` |
| 2 | `h : Disjoint d.support e.support` | yes | sharp over ℕ (item 3); conclusion fails e.g. for `d = e = single j 1` over ℚ (factor 2) |
| 3 | `d`, `e`, `P` | yes | — |

### Statement-shape verdict (Phase 5.5)

Normal form: REFACTOR (add operator form `hasseDeriv_comp_of_disjoint`)
Syntactic generality: OK
Superfluous arguments: NONE

Overall: RESTATE-BEFORE-SHIP

### Call sites — `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Separation.lean:156 | `rw [← hasseDeriv_hasseDeriv_of_disjoint hdisj, hasseDeriv_mul_of_degreeOf_eq_zero ...]` (`hasseDeriv_rename_mul_aeval`) |

Inline-derivation grep: (none) — `grep -rn "hasseDeriv (.* + .*" Roth/` finds only the Separation/Theta statements `hasseDeriv ((D μ).mapDomain some + Finsupp.single none ν)` which go through `hasseDeriv_rename_mul_aeval`, not a re-derivation.

### Composition check (Phase 6)

Can `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` be derived from mathlib in ≤3 chained calls?

Attempt 1: from mathlib alone.
  - Mathlib decls used: none applicable (no multivariate Hasse derivative in mathlib).
  - Result: fails

Attempt 2: from the parent API by `simp [hasseDeriv_hasseDeriv, hasseCoeff]`.
  - Result: fails (evidence item 5, `fail_if_success`): the factor `∏_{i ∈ supp d} (d i + e i).choose (d i)` is not simplified to 1 without the disjointness argument.

Conclusion: NOT-COMPOSABLE (once the parent ships, it is a 3-line corollary, which is the usual grain of a mathlib API lemma).

## Verdict: `MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint`

**Category:** YES-but-generalise-first

**Evidence:**
- Literature search (Phase 3): disjoint-variable composition is the folklore special case of multi-index iterativity (nLab, Moosa–Scanlon math/0510235, arXiv 0807.4332); the source paper asks for it as a separate lemma (clean.tex l.632).
- Generality analysis (Phase 4): MAXIMALLY GENERAL in hypotheses (sharp, item 3); operator normal form verified (item 2).
- Mathlib search (Phase 5): not in mathlib.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

This lemma is what makes Hasse derivatives in separate variables behave like a product: `Δ_{d+e} = Δ_d Δ_e` when `d` and `e` touch disjoint variable sets. The project uses it to split a mixed derivative of a separated product `U(x_τ)V(x_none)` into factorwise derivatives (Roth/Separation.lean:156). It is the same kind of corollary that sits next to every composition law in mathlib, and with the parent's `MvPolynomial.hasseDeriv` (YES-but-generalise-first) and `hasseDeriv_hasseDeriv` (YES-but-generalise-first) it should ship in the same PR. The hypothesis is exactly right: over ℕ the binomial factor equals 1 iff the supports are disjoint (item 3). The only weaker variant is the char-p condition `(binom : R) = 1` (item 4), which is non-standard and is just `hasseDeriv_hasseDeriv` + `one_smul`.

The bucket is generalise-first for reason MODERN-IDIOM (normal form), matching the parent: add the operator form `hasseDeriv d ∘ₗ hasseDeriv e = hasseDeriv (d + e)` (`LinearMap.ext` of this lemma, item 2) beside the proposed `hasseDeriv_comp`, with this pointwise lemma as corollary, and optionally a `Disjoint d e` spelling (item 1).

Reason for the generalisation: MODERN-IDIOM (Bourbaki 2.0) — operator normal form consistent with `Polynomial.hasseDeriv_comp` and the parent's `hasseDeriv_comp`.
Proposed restatement:
```lean
theorem hasseDeriv_comp_of_disjoint {d e : σ →₀ ℕ} (h : Disjoint d.support e.support) :
    (hasseDeriv d : MvPolynomial σ R →ₗ[R] _) ∘ₗ hasseDeriv e = hasseDeriv (d + e) :=
  LinearMap.ext (hasseDeriv_hasseDeriv_of_disjoint h)  -- verified in evidence item 2

theorem hasseDeriv_hasseDeriv_of_disjoint {d e : σ →₀ ℕ} (h : Disjoint d.support e.support)
    (P : MvPolynomial σ R) : hasseDeriv d (hasseDeriv e P) = hasseDeriv (d + e) P := ...
```
Estimated cost of regeneralisation: CHEAP.
Mathlib downstream this enables:
  - `Module.End` rewriting in the same normal form as `hasseDeriv_comp`; commutation of Hasse derivatives in disjoint variables;
  - factorisation `Δ_d = ∏_j Δ_{d_j e_j}` of a mixed Hasse derivative into single-variable ones (combined with `hasseDeriv_single_aeval_X`/`uniqueAlgEquiv_hasseDeriv`), the standard way to reduce multivariate Hasse calculus to `Polynomial.hasseDeriv`.
WHY it belongs in mathlib (gap): `Mathlib/Algebra/MvPolynomial/` has no Hasse derivatives, so the disjoint-variable composition (used in Wronskian / separation-of-variables and multiplicity-method arguments) has no statement.
Proposed mathlib location: Mathlib/Algebra/MvPolynomial/HasseDeriv.lean (new file, with the parent).
PR grouping: ship with `Finsupp.choose` (+ `Finsupp.choose_mul`, and a `choose = 1 ↔ disjoint` lemma), `MvPolynomial.hasseDeriv`, `coeff_hasseDeriv`, `hasseDeriv_hasseDeriv`/`hasseDeriv_comp`.
Next action: run `/generalise MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint` (target: operator form above) when preparing the parent PR.

---

## Next step

Upstream together with `MvPolynomial.hasseDeriv_hasseDeriv`: add `hasseDeriv_comp_of_disjoint` in operator form and keep the pointwise lemma as a corollary. Locally no change is needed (caller Roth/Separation.lean:156).

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/MvPolynomial.hasseDeriv_hasseDeriv_of_disjoint/variants.lean` (`lean_diagnostic_messages`: success, no diagnostics): (1) `Disjoint d e` variant via `Finsupp.disjoint_iff`; (2) operator form via `LinearMap.ext`; (3) sharpness `hasseCoeff d (d + e) = 1 → Disjoint d.support e.support` via `Finset.prod_eq_one_iff_of_one_le` and `Nat.choose_eq_one_iff`; (4) char-p weakening `(hasseCoeff d (d + e) : R) = 1` suffices; (5) `fail_if_success (simp [hasseDeriv_hasseDeriv, hasseCoeff]; done)` shows simp alone does not close it. First check flagged a deprecated name and a nonexistent lemma in item 3; fixed in place and rechecked via the LSP (no `lake env lean` run).
- Loogle `"hasseDeriv", Disjoint` (none), `?n ≤ Nat.choose ?n ?k` (none); LeanSearch and Lean-Finder queries as in [A]/[C]; mathlib grep as in [D]–[E].
- WebSearch: 3 queries (table rows 1–3). ChatGPT MCP: n/a (not configured).
- Project greps: `grep -rn hasseDeriv_hasseDeriv_of_disjoint Roth/` (call sites), `grep -rn "hasseDeriv (.* + .*" Roth/` (no inline derivations), `.mathlib-quality/references/clean.tex` grep (l.579–582, l.632).
