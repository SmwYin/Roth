---
decl: Roth.index_C_mul
file: Roth/Index.lean
line: 195
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: CHEAP
junk: KEEP
rationale: ind(cP) = ind(P) for c ≠ 0 about the project-only def Roth.index is a one-line rewrite (map_mul, taylor_C, smul_eq_C_mul, MvPolynomial.support_smul_eq). hc is needed (compiled counterexample). The subject is not a mathlib notion, and the power-series analogue (weightedOrder of a • f) is a two-call composition of weightedOrder_mul and weightedOrder_monomial_of_ne_zero, so nothing goes upstream.
action: Keep in Roth/Index.lean as the named form of the source's scalar-invariance identity (one caller, Roth/Theta.lean:405). Do not upstream. Optional separate tiny mathlib PR is MvPowerSeries.weightedOrder_smul (equality for a ≠ 0 over a domain) in Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean, which is unrelated to this decl.
---

# Roth.index_C_mul

## Inventory entry

### `theorem Roth.index_C_mul`
- **Type**: `{σ : Type*} [Fintype σ] {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) : Roth.index (C c * P) α r = Roth.index P α r`
- **What**: Multiplying a real polynomial by a nonzero constant does not change its Roth index at `α` with weights `r`.
- **How**: Unfolds both indices (`sInf` of `weight r` over `(taylor α _).support`). `map_mul` and `MvPolynomial.taylor_C` turn `taylor α (C c * P)` into `C c * taylor α P`. `← MvPolynomial.smul_eq_C_mul` rewrites that as `c • taylor α P`, and `MvPolynomial.support_smul_eq hc` gives equal supports.
- **Hypotheses**: `hc : c ≠ 0`, which is necessary (evidence (1)). No positivity is needed on `r`, and no nonvanishing is needed on `P`.
- **Uses from project**: `Roth.index`, `MvPolynomial.taylor`, `MvPolynomial.taylor_C` (Roth/Taylor.lean:55)
- **Used by**: Roth/Theta.lean:405 (`sum_max_sub_le_index_det`, sign factor `Equiv.Perm.sign s` of a Leibniz-expansion term). It is used nowhere else; `grep -rn index_C_mul Roth/` returns only the declaration and that call.
- **Visibility**: public
- **Lines**: 194-197 (docstring 194, statement 195-196, proof 197), proof length 1 line
- **Notes**: Formalises the end of clean.tex §4: "For nonzero c ... ind(cP;α;r) = ind(P;α;r)" (clean.tex:636-640). The Lean note at clean.tex:627-634 also asks for "invariance under nonzero scalars" as its own lemma. `Roth.index_neg` is its `c = -1` case (see Roth.index_neg.md).

## Junk check (Step 8)
- Used anywhere? Yes, once: Roth/Theta.lean:405.
- Wrapper of 1-2 mathlib calls? Close to it. It is a 4-rewrite chain whose only real content is `MvPolynomial.support_smul_eq` plus the project's `taylor_C`.
- Does mathlib have it? Not for `Roth.index`, which is project-only. Mathlib has `MvPowerSeries.le_weightedOrder_smul` (an inequality only) and no equality form.
- Too specific (inline)? It could be inlined at its single caller. It is kept because it is a source-cited identity that the source's Lean note explicitly asks to be a separate lemma, and it states the invariance in the reusable `C c * P` normal form.
- Well-chosen? Yes. `hc` is necessary, and the statement has no superfluous hypotheses.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The declaration is public.
- The name does not end `_aux`.
- The docstring does not start internal/auxiliary.
- Step 8 said KEEP.
- `Roth.index_C_mul` is not in mathlib: `grep -rn "namespace Roth" .lake/packages/mathlib/Mathlib/` finds nothing.

The proof is a rewrite chain, not `rfl`/`Iff.rfl`, so this is not a glue lemma and gets a full run. The parent `Roth.index` is BORDERLINE-needs-human rather than NO-mathlib-has-it, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief, and the evidence file importing `Roth.Index` elaborates with no diagnostics)
- decl `Roth.index_C_mul`:   resolved at Roth/Index.lean:195
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the Roth index of a real multivariate polynomial at a point and its basic properties (§4 of the source)

### Statement (Phase 1)

`Roth.index_C_mul` is a theorem stating the following:

Let `P ∈ ℝ[X_j : j ∈ σ]` with σ finite, `α ∈ ℝ^σ`, `r_j ∈ ℕ`, and `c ∈ ℝ` with `c ≠ 0`. Define `ind(P) = min { ∑ d_j / r_j : the coefficient of X^d in P(X + α) is nonzero }`. Then `ind(cP) = ind(P)`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables.
- `c`: the scalar.
- `P`: the polynomial.
- `α`: the point.
- `r`: the weights.

Hypotheses (Lean side):
- `hc : c ≠ 0`. Without it `cP = 0`, and Lean's `index 0 = 0`.

Conclusion (math): the index is invariant under nonzero scalar multiplication.

Conclusion (Lean): `index (C c * P) α r = index P α r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a basic invariance property of a project definition (a one-line remark at the end of source §4). It is not a main result and is not named after anyone.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE (one-liner rule applies to defs only; noted that the proof is a single rewrite chain)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth lemma index of polynomial unchanged multiplying by nonzero constant ind(cP)=ind(P) | partial | Roth index = weighted multiplicity at a point with weights 1/r_j (arXiv math/9708214). The identity follows directly from the definition | no source states it as a lemma. It is treated as immediate (Natarajan–Thangadurai, *Pillars of Transcendental Number Theory* §6.1, and Bombieri–Gubler, cited but not opened) |
| 2 | WebSearch (general form) | valuation v(cf)=v(f) for nonzero constant unit order of vanishing scalar multiple invariance | partial | the order of vanishing is the lowest nonzero homogeneous term (Lebl, *Tasty Bits of SCV* 6.2). For a valuation, v(unit) = 0 and v(ab) = v(a) + v(b) (Stacks 02MB) | the general form is "a valuation is invariant under units", i.e. v(u) = 0 combined with multiplicativity |
| 3 | WebSearch (aliases: monomial valuation, support) | monomial valuation weighted order power series support of scalar multiple equals support | partial | weighted order = min over the support (arXiv 0811.0414, math/0212203). supp(c·f) = supp(f) for c ≠ 0 over a field | mathlib's MvPowerSeries.Order docs surfaced (`le_weightedOrder_smul` only) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for "ind(cP" | yes | clean.tex:636-640: "For nonzero c ... ind(cP;α;r) = ind(P;α;r)". The Lean note at clean.tex:627-634 says "Prove invariance under nonzero scalars ... as separate lemmas" | the Lean statement matches the source verbatim |
| 6 | nLab | valuation | no | abstract valuations only (v(units) = 0) | nothing at the polynomial or point level |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | order of vanishing (tag 02MB) | partial | ord_R is additive, and units have order 0 | not the weighted multi-index form |
| 9 | MathOverflow / Math.SE | covered by searches 2-3 | no | n/a | considered trivial, and no dedicated thread was found |
| 10 | recent arXiv | Roth index (1806.10737, 1305.0926) | partial | index as weighted multiplicity, with scalar invariance used implicitly | no standalone statement |

### Literature summary (Phase 3)

Concept identified as: invariance of a (weighted, monomial) order of vanishing at a point under multiplication by a unit, i.e. a valuation takes the value 0 on units.
Sources agree on the standard form: yes. `v(uf) = v(f)` for a unit `u`, which over a field means any nonzero constant.
Most general standard form: for any valuation-like order `v`, `v(uf) = v(u) + v(f) = v(f)` for units `u`. For a support-defined order over a module with no zero-smul-divisors, `supp(c • f) = supp(f)` for `c ≠ 0`.
Generality dimensions where the literature varies:
  - coefficients: any domain / torsion-free module vs `ℝ` (project).
  - weights: any nonnegative weights. The project's real weights `1/r_j` include junk `r_j = 0`, and the lemma holds there too.
  - zero convention: `v(0) = +∞` (literature) vs `0` (project). This is irrelevant here because both sides vanish together only when `c ≠ 0`.
Disagreement with the literature: none.

### Generality analysis — `Roth.index_C_mul`

Literature-standard form: `ord_{α,w}(cP) = ord_{α,w}(P)` for `c` a nonzero scalar (a unit) over a domain, any weights.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hc : c ≠ 0` | required | nonzero / unit | NO | evidence (1): with `c = 0`, `P = X true`, `α = 0`, `r = 1`, we get `0 ≠ 1` (compiled) |
| 2 | `r : σ → ℕ` | arbitrary, no positivity | any weights | already general | the proof never uses `r` |
| 3 | `P` | arbitrary, no `P ≠ 0` | arbitrary | already general | for `P = 0` both sides are `index 0` |
| 4 | ring `ℝ` | fixed | any domain | not for this statement | `Roth.index` is defined only over `ℝ`, and the proof's `support_smul_eq` already works in that generality |
| 5 | `C c * P` vs `c • P` | `C c * P` | either | equivalent | evidence (2) proves the `•` form in one line, and evidence (3) proves the `P * C c` form via `mul_comm` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. The only hypothesis, `hc`, is necessary (compiled counterexample), and `r`, `α`, `P` are unconstrained.
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | `c ≠ 0` is data-level | — |
| 2 | Sequences vs filters? | no | finite algebraic statement | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | yes in principle | `IsUnit c` / `[Module.IsTorsionFree]` over any ring | belongs to the parent-def question (`Roth.index` is ℝ-only and BORDERLINE) |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | partial | "the index is an `AddValuation`, so it vanishes on units" | parent-def redesign |
| 8 | Concrete-via-abstract? | yes (the diagnostic fires) | after `rw [index, index]` the proof never mentions `index` again. It is pure `MvPolynomial.support_smul_eq` applied to `taylor α P`. The abstract statement "nonzero scalar multiples have equal support" is already mathlib's `MvPolynomial.support_smul_eq` | nothing new to add |
| 9 | False-generalisation guard | no false generalisation | the `•` form (evidence (2)) is the same statement | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for this lemma)
  - Reason: the abstract content is mathlib's `MvPolynomial.support_smul_eq`, as Q8 shows. Any further modernisation is a redesign of the parent `Roth.index`, which is assessed separately as BORDERLINE.

### Proof strategy — `Roth.index_C_mul`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no (for this proof) | none. A side observation is that mathlib lacks the equality `MvPowerSeries.weightedOrder (a • f) = weightedOrder f` for `a ≠ 0` (it has only `le_weightedOrder_smul`). Evidence (5) shows it is a two-call composition. A route through `index_eq_weightedOrder_div` would need it, but the current support-level proof does not | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It is a single rewrite chain down to `MvPolynomial.support_smul_eq` and needs no `hr`. This is strictly better than going through the weighted-order bridge, which needs `0 < r j`.
  - Missing mathlib API: none for this lemma.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_C_mul`

[A] Lean-Finder       "weighted order of nonzero scalar multiple of multivariate power series equals weighted order"   hits: `MvPowerSeries.le_weightedOrder_smul` (inequality), `weightedOrder_monomial_of_ne_zero`, `weightedOrder_monomial`, `le_order_smul`, `weightedOrder_le`. There is no equality for `a • f`
[B] Loogle            `MvPowerSeries.weightedOrder, HSMul.hSMul`   hits: `le_weightedOrder_pow`, `le_weightedOrder_smul` only
[C] LeanSearch        "order of vanishing unchanged by multiplying polynomial by nonzero constant"   hits: `meromorphicOrderAt_smul_of_ne_zero`, `meromorphicOrderAt_mul_of_ne_zero`, `analyticOrderAt_smul` (analytic one-variable analogues, not polynomial or weighted)
[D] Grep mathlib src  `weightedOrder_smul`, `weightedOrder_C_mul`, `order_smul`, `rootMultiplicity_C_mul`, `support_smul_eq`. Hits: `MvPolynomial.support_smul_eq` (Mathlib/Algebra/MvPolynomial/Basic.lean:700), `MvPolynomial.smul_eq_C_mul` (Basic.lean:211), `MvPowerSeries.weightedOrder_neg` (Order.lean:358), `le_weightedOrder_smul` (Order.lean:313). No polynomial-level or at-a-point scalar invariance
[E] Name pattern      `Roth.index_C_mul`, `index_C_mul`   no mathlib decl in a matching namespace (no `namespace Roth` in mathlib). `lean_local_search` was unavailable (ripgrep is not on PATH), so this check used grep instead

Searched for both:
  - the user's current form (Roth index invariant under nonzero constants)
  - the literature-standard form (weighted order / valuation invariant under units)

Concluded: found building blocks (`MvPolynomial.support_smul_eq`, `MvPolynomial.smul_eq_C_mul`, `map_mul`, plus the project's `taylor_C`); composition gives our form.

### Normal-form check — `Roth.index_C_mul`

Equivalent formalisms:
- `index (C c * P) = index P` (this lemma)
- `index (c • P) = index P`
- `index (P * C c) = index P`

Does mathlib already have a canonical form? For supports, mathlib's simp normal form is `c • p` (`support_smul_eq` is `@[simp]`, and `smul_eq_C_mul` relates the two). Lemmas named `*_C_mul` with `C a * p` on the LHS are also standard in MvPolynomial (e.g. `totalDegree_C_mul`, `degreeOf_C_mul_le`).
Is our statement against a canonical form? Yes. The LHS `C c * P` follows the `_C_mul` naming, and the RHS is the simpler term.
RHS convention respected? yes

### Syntactic generality — `Roth.index_C_mul`

Alternative restatements attempted:
- `C c * P` (current)
- `c • P` (evidence (2), one line)
- `P * C c` (evidence (3))
- `IsUnit c` hypothesis (equivalent over ℝ, harder to supply)

Chosen restatement: current.
Justification: the single caller (Theta.lean:405) produces an integer cast, which `map_intCast` turns into the `C`-free cast form. `simpa only [map_intCast]` against `C c * P` fits that caller directly. An optional `smul` companion would be cheap but has no consumer.

### Superfluous-argument audit — `Roth.index_C_mul`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype σ]` | yes | needed by `Roth.weight` / `Roth.index` |
| 2 | `hc : c ≠ 0` | yes | evidence (1), compiled counterexample |
| 3 | `P`, `α`, `r` explicit | yes | unconstrained data, and all three are given explicitly at the caller |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not a mathlib candidate)

### Call sites — `Roth.index_C_mul`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:405 | `simpa only [map_intCast] using index_C_mul (Int.cast_ne_zero.2 (Units.ne_zero (Equiv.Perm.sign s))) (∏ i, Matrix.of E (s i) i) α r` |

Inline-derivation grep:
  - (none) — no other site rewrites `support_smul_eq` under `index`. `index_neg` (Index.lean:190) re-derives the `c = -1` case via `support_neg`, but it is unused (Roth.index_neg.md recommends deletion).

### Composition check (Phase 6)

Can `Roth.index_C_mul` be derived from mathlib in ≤3 chained calls?

Attempt 1: unfold `index`, push `taylor` through the product, and apply `support_smul_eq`.
  - Mathlib decls used: `map_mul`, `MvPolynomial.smul_eq_C_mul` (Mathlib/Algebra/MvPolynomial/Basic.lean:211), `MvPolynomial.support_smul_eq` (Mathlib/Algebra/MvPolynomial/Basic.lean:700), plus project `MvPolynomial.taylor_C` (Roth/Taylor.lean:55, itself `algHom_C`).
  - Result: succeeds. This is the current proof, reproduced in evidence (4).
  - Notes: one rewrite chain with no side goals.

Conclusion: COMPOSABLE

## Verdict: `Roth.index_C_mul`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): clean.tex:636-640 states it verbatim. In the literature it is the trivial "valuations vanish on units / nonzero scalars preserve the support" fact.
- Generality analysis (Phase 4): MAXIMALLY GENERAL. `hc` is necessary (compiled counterexample), and the statement has no other hypotheses.
- Mathlib search (Phase 5): building blocks `MvPolynomial.support_smul_eq` and `MvPolynomial.smul_eq_C_mul`. Mathlib has no equality version for weighted orders (only `le_weightedOrder_smul`).
- Composition check (Phase 6): COMPOSABLE (a single rewrite chain).

**Rationale:**

The lemma unfolds `Roth.index` and then reduces to mathlib's `MvPolynomial.support_smul_eq` applied to `taylor α P`. The project's `taylor_C` (via `map_mul`) and `smul_eq_C_mul` bridge `C c * _` to `c • _`. Once `index` is unfolded the proof never mentions it again (Q8 fires), and the abstract statement is already in mathlib. The subject `Roth.index` is a real-valued, project-specific normalisation of a weighted order at a point. Its own report rated it BORDERLINE, and any upstream version would be an `ℕ∞`-valued weighted order of `taylor α P`. For that version, invariance under a nonzero scalar is a composition of `MvPowerSeries.weightedOrder_mul` with `weightedOrder_monomial_of_ne_zero` (evidence (5)), so this lemma has no upstream counterpart to contribute.

The statement itself is optimal. `hc` is genuinely needed (evidence (1)), and the proof avoids the `0 < r j` hypothesis that the weighted-order route would require. A side observation, not part of this verdict: mathlib states only the inequality `le_weightedOrder_smul`. The equality `weightedOrder (a • f) = weightedOrder f` for `a ≠ 0` over a domain is missing, but it composes in two calls (evidence (5)), so it is at most a cosmetic mathlib addition.

WHY not: the lemma is a one-line rewrite chain ending in `MvPolynomial.support_smul_eq`, about a project definition. It adds no mathematics that mathlib lacks.
Belongs-elsewhere check: keep it project-local in Roth/Index.lean. It is the source's explicitly requested "invariance under nonzero scalars" lemma (clean.tex:627-640). It packages the `taylor`/`C`/`smul` bridging so that Theta.lean:405 does not have to.
Mathlib building blocks: `MvPolynomial.support_smul_eq` (Mathlib/Algebra/MvPolynomial/Basic.lean:700), `MvPolynomial.smul_eq_C_mul` (Mathlib/Algebra/MvPolynomial/Basic.lean:211), `map_mul`; project `MvPolynomial.taylor_C` (Roth/Taylor.lean:55).
Composition sketch (≤3 lines):
```lean
example {c : ℝ} (hc : c ≠ 0) (P : MvPolynomial σ ℝ) (α : σ → ℝ) (r : σ → ℕ) :
    index (C c * P) α r = index P α r := by
  rw [index, index, map_mul, taylor_C, ← smul_eq_C_mul, support_smul_eq hc]
```
Call sites in our project (from Phase 6.0): 1 (Roth/Theta.lean:405).
Refactor plan: do not delete. The verdict is "not for mathlib", not "inline". Inlining at Theta.lean:405 would mean unfolding `index` in a Leibniz-expansion step and repeating the chain above under `simpa only [map_intCast]`. That loses the named reference to the source identity and gains nothing. If `Roth.index_neg` is deleted as recommended, this lemma is the single place for scalar invariance. A future `index_neg` would follow from it with `c = -1` (compiled in evidence/Roth.index_neg/subsumed.lean).
Next action: keep locally; do not upstream.

## Next step

Keep `Roth.index_C_mul` in Roth/Index.lean unchanged and do not upstream it: its abstract content is `MvPolynomial.support_smul_eq`. Optionally, as an independent tiny mathlib PR, add `MvPowerSeries.weightedOrder_smul` (equality for `a ≠ 0` over a domain) next to `weightedOrder_mul` in Mathlib/RingTheory/MvPowerSeries/NoZeroDivisors.lean.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.index_C_mul/hyps.lean` (imports `Roth.Index`). `lean_diagnostic_messages` reports no diagnostics after one fix: the first draft of (5) omitted the explicit `w` argument of `weightedOrder_monomial_of_ne_zero`. The file contains:
  - (1) a counterexample showing `hc` is necessary: `c = 0`, `P = X true` (σ = Bool), `α = 0`, `r = 1` gives LHS `0` and RHS `1`.
  - (2) the `c • P` form in one line (`map_smul`, `support_smul_eq`).
  - (3) the `P * C c` form via `mul_comm`.
  - (4) the current proof reproduced as a composition.
  - (5) `MvPowerSeries.weightedOrder (a • f) = weightedOrder f` for `a ≠ 0`, composed from `MvPowerSeries.smul_eq_C_mul`, `weightedOrder_mul`, `monomial_zero_eq_C_apply`, and `weightedOrder_monomial_of_ne_zero`. This confirms the mathlib gap is only cosmetic.
- WebSearch ×3 (queries in the table).
- Local grep of `.mathlib-quality/references/clean.tex` (lines 627-640).
- Lean-Finder, Loogle, LeanSearch, and grep of `.lake/packages/mathlib/Mathlib/`, as recorded in Phase 5.
- `grep -rn index_C_mul Roth/`: the declaration plus Theta.lean:405.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session. `lean_local_search` n/a: ripgrep is not on PATH, so grep was used instead.
