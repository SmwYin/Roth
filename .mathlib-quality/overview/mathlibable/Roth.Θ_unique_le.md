---
decl: Roth.Θ_unique_le
file: Roth/Theta.lean
line: 256
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Lemma 5 of the source (Θ_1(B; q; r) ≤ log B / (r log q)) is a two-call composition of the project's Θ_le_of_forall_index_le and private index_unique_le_log_div about the Roth-proof-specific supremum Θ; hypotheses are essential (1 ≤ B compiled necessary), and the reusable arithmetic core (q^t ≤ lc) lives in pow_rootMultiplicity_le, assessed separately.
action: Do not upstream; keep in Roth/Theta.lean as the paper's Lemma 5 (callers theta_scaled_unique_le_aux at Theta.lean:759 and theta_lt_base_aux at Theta.lean:822); no call-site changes.
---

# Roth.Θ_unique_le

## Inventory entry

### `theorem Roth.Θ_unique_le`
- **Type**: `∀ {σ : Type*} [Fintype σ] [Unique σ] {B : ℝ}, 1 ≤ B → ∀ {q : σ → ℕ}, 1 < q default → ∀ {r : σ → ℕ}, Θ B q r ≤ Real.log B / (↑(r default) * Real.log ↑(q default))`
- **What**: Lemma 5 of the source. In one variable, if `q > 1` and `B ≥ 1`, the supremum `Θ_1(B; q; r)` of indices of nonzero integer polynomials with degree at most `r` and coefficients bounded by `B`, taken at rational points `h/q` with `gcd(h, q) = 1`, is at most `log B / (r log q)`.
- **How**: A term-mode proof. `Θ_le_of_forall_index_le hB` reduces to a bound on each index. Each index is bounded by the private `index_unique_le_log_div`, whose leading-coefficient hypothesis comes from the `RSet` coefficient bound `hR.2.2` (rewritten with `Polynomial.leadingCoeff` and `coeff_uniqueAlgEquiv`). `index_unique_le_log_div` in turn uses `index_unique`, a `ℚ`-to-`ℝ` transfer of root multiplicity (`Polynomial.eq_rootMultiplicity_map`), `pow_rootMultiplicity_le` (Gauss's lemma and a leading-coefficient comparison), and `Real.log_le_log`.
- **Hypotheses**: `1 ≤ B` (needed for nonemptiness in `csSup_le`, and genuinely necessary, see Evidence (1)); `1 < q default` (needed so that `log q > 0`); `[Unique σ]` (the one-variable case); `[Fintype σ]` (needed by `Θ`). The section's `[DecidableEq σ]` is omitted. No positivity of `r` is assumed: when `r = 0` the RHS is `0` by Lean's `x / 0 = 0`, and the statement still holds.
- **Uses from project**: `Roth.Θ`, `Roth.Θ_le_of_forall_index_le`, `Roth.index_unique_le_log_div` (private), `Roth.RSet` (membership projection `hR.1`, `hR.2.2`), `Roth.coeff_uniqueAlgEquiv` (in `simpa only`), `Roth.uniqueAlgEquiv` (via the helper's statement), `Roth.index`.
- **Used by**: Roth/Theta.lean:759 (inside private `theta_scaled_unique_le_aux`, the one-variable term of Lemma 6/7's Φ bound); Roth/Theta.lean:822 (inside private `theta_lt_base_aux`, the `m = 1` base case of Lemma 7); module docstring Roth/Theta.lean:35. Found with `grep -rn Θ_unique_le Roth/`; no other file uses it.
- **Visibility**: public
- **Lines**: 253–260 (docstring 253–255, statement 256–257, proof 258–260), proof length 3 lines
- **Notes**: Source: clean.tex §5, Lemma `roth:lem5` (l.671–691). The paper also assumes `r_1 > 0` in the proof ("Since `log q_1 > 0` and `r_1 > 0`"); the Lean statement drops it thanks to the division-by-zero convention.

## Junk check (Step 8)
- **Used anywhere?** Yes, at Roth/Theta.lean:759 and :822.
- **Wrapper of 1–2 mathlib calls?** No. It wraps two *project* lemmas (`Θ_le_of_forall_index_le`, `index_unique_le_log_div`), and the mathematical content sits in the helper chain (`index_unique`, `pow_rootMultiplicity_le`).
- **Does mathlib have it?** No. It concerns the project-local `Θ`. The arithmetic core (the denominator power `q^t` divides the leading coefficient) is near mathlib's `den_dvd_of_is_root` and `Polynomial.pow_rootMultiplicity_dvd`, but mathlib has no multiplicity version. That core is assessed in Roth.pow_rootMultiplicity_le.md.
- **Too specific (inline?)?** No. It is a named lemma of the paper (Lemma 5), with two callers.
- **Well-chosen?** Yes. The statement has minimal hypotheses, stronger than the paper's (no `r > 0`).
- **Conclusion:** `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib: `grep -rln "namespace Roth\b" .lake/packages/mathlib/Mathlib/` has no hits.

This is not a glue lemma. It is a named paper lemma whose term-mode body composes two project lemmas plus a coefficient rewrite, not `rfl`/unfolding. A full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors)
- decl `Roth.Θ_unique_le`:   resolved at Roth/Theta.lean:256
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.Θ_unique_le` is a theorem stating the following.

Let `B ≥ 1`, let `q > 1` and `r` be natural numbers, and let `Θ_1(B; q; r)` be the supremum, over nonzero `R ∈ ℤ[x]` with `deg R ≤ r` and all coefficients of absolute value at most `B`, and over integers `h` coprime to `q`, of the index `ind(R; h/q; r) = (multiplicity of h/q as a root of R) / r`. Then `Θ_1(B; q; r) ≤ log B / (r log q)`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ] [Unique σ]`: a one-element variable type (the one-variable case).
- `B`: the coefficient bound.
- `q : σ → ℕ`: the denominator, evaluated at `default`.
- `r : σ → ℕ`: the degree bound and index weight, evaluated at `default`.

Hypotheses (Lean side):
- `hB : 1 ≤ B`: makes the defining family nonempty, and keeps `log B ≥ 0`.
- `hq : 1 < q default`: makes `log q > 0`.

Conclusion (math): `Θ_1(B; q; r) ≤ log B / (r log q)`.

Conclusion (Lean): `Θ B q r ≤ Real.log B / (↑(r default) * Real.log ↑(q default))`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a named lemma of the source paper (Lemma 5), but an intermediate bound on a project-local supremum inside the Roth argument. It is not a project main result (the main result is Roth's theorem) and is not named after a person.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines (a single term)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem). The body composes `Θ_le_of_forall_index_le` and `index_unique_le_log_div`.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma one variable index rational point "log B" "r log q" root multiplicity leading coefficient Gauss lemma | partial | A Georgia Tech note on Siegel/Roth (ecroot.math.gatech.edu/siegel.pdf) calls the one-variable case obvious: a rational root `p/q` of multiplicity `m` forces `q^m` to divide the leading coefficient | the arithmetic core, not the `Θ` packaging; Evertse's explicit Roth's lemma papers are multivariable |
| 2 | WebSearch (general form) | multiplicity of rational root h/q of integer polynomial q^t divides leading coefficient bound | partial | the rational root theorem (denominator divides the leading coefficient) plus factoring out `(qx - h)^t`; related multiplicity bounds (arXiv 1806.05222, math/0512239, Bonciocat–Bonciocat–Zaharescu) are of a different kind | general form = `q^t ∣ lc(R)`, hence `q^t ≤ |lc(R)| ≤ B` |
| 3 | WebSearch (named-after / aliases) | Cassels Ridout Roth theorem Theta_m(B;q;r) supremum index Lemma one variable bound log B | partial | Yamada (arXiv math/0307203, withdrawn for an error in Lemma 3.1) and arXiv 2603.10561 restate Ridout's method; the `Θ_m` supremum and its one-variable bound are standard in the Cassels/Ridout presentation | named only as a step of Roth's lemma |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | clean.tex, `roth:lem5` | yes | l.671–691: "Suppose additionally that `q_1 > 1`. Then `Θ_1(B; q_1; r_1) ≤ log B/(r_1 log q_1)`", proved via Gauss's lemma and a leading-coefficient comparison | this lemma verbatim |
| 6 | nLab | rational root theorem / index of a polynomial | no | nothing relevant | not a categorical or structural concept |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an inequality of reals about integer polynomials) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; no index-at-a-point notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–2 | no | n/a | too elementary; the core is the rational root theorem with multiplicity |
| 10 | recent arXiv (last 5 years) | arXiv 2603.10561 (p-adic Roth, 2026) and 2502.00731 (2025), from searches 1 and 3 | partial | Ridout-style height conditions and a pointwise Roth's lemma | no stand-alone one-variable `Θ_1` lemma |

### Literature summary (Phase 3)

Concept identified as: the one-variable case of Roth's lemma in the Cassels/Ridout `Θ_m` presentation. If `h/q` (in lowest terms) is a root of multiplicity `t` of `R ∈ ℤ[x]`, then `q^t ∣ lc(R)`, so `q^t ≤ B` and `t/r ≤ log B / (r log q)`.
Sources agree on the standard form: yes (clean.tex; the Georgia Tech note; Ridout-style expositions).
Most general standard form: `q^t ∣ lc(R)` for a root `h/q` of multiplicity `t` (a fraction-ring statement in the style of mathlib's `den_dvd_of_is_root`); the `Θ`/log bound follows directly from it.
Generality dimensions where the literature varies:
  - `r > 0`: assumed in the paper; not needed in Lean.
  - Base ring: `ℤ` in Roth's argument; the arithmetic core works over any UFD and its fraction field.
Disagreement with the literature: none. The Lean form is slightly stronger (no `r > 0`).

### Generality analysis — `Roth.Θ_unique_le`

Literature-standard form: `B ≥ 1, q > 1 ⇒ Θ_1(B; q; r) ≤ log B/(r log q)`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hB : 1 ≤ B` | required | `B ≥ 1` implicit | NO | Evidence (1) compiles a counterexample without it: at `B = 1/2`, `q = 2`, `r = 1`, the RHS is negative while `Θ ≥ 0` |
| 2 | `hq : 1 < q default` | required | `q_1 > 1` | NO | at `q = 1`, `log q = 0` makes the RHS `0`, but `R = x - h` (coefficients bounded by `B ≥ |h|`) has positive index, so the bound fails |
| 3 | `r > 0` | not taken | paper uses `r_1 > 0` | already weaker | the `x/0 = 0` convention gives RHS `0`, and the index with zero weights is `0` |
| 4 | `[Unique σ]` | required | one variable | NO | the multivariable analogue is Lemma 6/7 (`Θ_option_le`, `Θ_lt`), a different statement |
| 5 | `[DecidableEq σ]` | omitted | n/a | already absent | Evidence (2) signature check |
| 6 | base ring `ℤ` | fixed by `Θ` | `ℤ` | NO (for this decl) | `Θ` is defined over `ℤ`; ring-generalising belongs to the core `pow_rootMultiplicity_le` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. Each remaining hypothesis is necessary (Evidence (1) for `B`; the `q = 1` argument for `q`).
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | `[Unique σ]` already encodes one variable | — |
| 2 | Sequences vs filters? | no | a finite inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no for this decl | the core (`q^t ∣ lc`) could be stated over a UFD; that is `pow_rootMultiplicity_le`'s business | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | the `Unique σ` encoding is a project convention for one variable inside `MvPolynomial` | — |
| 8 | Concrete-via-abstract? | yes, but already done | the proof never manipulates `Θ` beyond `Θ_le_of_forall_index_le`; the abstract content is factored into `index_unique_le_log_div` and `pow_rootMultiplicity_le` | none new |
| 9 | False-generalisation guard | no widening proposed | — | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the lemma is a thin `Θ`-level packaging of an index bound, and the abstract content is already split into the helper lemmas.

### Proof strategy — `Roth.Θ_unique_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | possibly (in the helper chain, not here) | a fraction-ring statement "`den(r)^(rootMultiplicity r p) ∣ lc(p)`" generalising `den_dvd_of_is_root`; recorded under Roth.pow_rootMultiplicity_le.md | MODERATE (separate decl) |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. A `csSup_le`-style elimination plus a pointwise bound, which is exactly the paper's "Taking the supremum proves the claim".

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_unique_le`

[A] Lean-Finder       "q to the power of root multiplicity of h/q divides leading coefficient of integer polynomial"   hits: `Polynomial.pow_rootMultiplicity_dvd`, `den_dvd_of_is_root`, `Polynomial.pow_rootMultiplicity_not_dvd`, `num_dvd_of_is_root`, `Polynomial.exists_eq_pow_rootMultiplicity_mul_and_not_dvd` (building blocks of the core, none is the multiplicity version)
[B] Loogle            `Polynomial.rootMultiplicity, Polynomial.leadingCoeff, Real.log`   no hits
[C] LeanSearch        "root multiplicity of a rational root of an integer polynomial bounded by log of leading coefficient over log of denominator"   hits: `Polynomial.rootMultiplicity_eq_nat_find_of_nonzero`, `Polynomial.le_rootMultiplicity_iff`, `Polynomial.rootMultiplicity_le_iff`, `Polynomial.rootMultiplicity_X_sub_C_pow` (generic, not this bound)
[D] Grep mathlib src  `namespace Roth` (no hits); `den_dvd_of_is_root` at Mathlib/RingTheory/Polynomial/RationalRoot.lean:89
[E] Name pattern      `Θ_unique_le`, `index_unique_le_log_div`, `pow_rootMultiplicity_le` (project only)

Searched for both:
  - the user's form (`Θ B q r ≤ log B / (r log q)`)
  - the literature-standard core (`q^t ∣ lc(R)` / `t ≤ log B / log q`)

Concluded: found building blocks (`csSup_le` via the project's `Θ_le_of_forall_index_le`; `den_dvd_of_is_root`, `pow_rootMultiplicity_dvd`, Gauss's lemma for the core). The `Θ` form is not in mathlib and cannot be, since `Θ` is project-local.

### Normal-form check — `Roth.Θ_unique_le`

Equivalent formalisms:
- `Θ B q r ≤ log B / (r log q)` (current)
- `Θ B q r * (r log q) ≤ log B` (with `r > 0`)
- `q ^ (r Θ) ≤ B` (rpow form)

Does mathlib already have a canonical form? No (project-local quantity). The current form matches the paper and both callers, which rewrite the RHS directly.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.Θ_unique_le`

Alternative restatements attempted:
- division form (current)
- multiplied-out form (needs an extra `r > 0` hypothesis; strictly less general)

Chosen restatement: division form (current).
Justification: no `r > 0` side condition, and both callers (Theta.lean:759, :822) immediately rewrite `log` of an rpow and clear the denominator with `div_le_iff₀`/`field_simp`.

### Superfluous-argument audit — `Roth.Θ_unique_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hB : 1 ≤ B` | yes | necessary (Evidence (1)) |
| 2 | `hq : 1 < q default` | yes | necessary (`q = 1` counterexample) |
| 3 | `[Unique σ]` | yes | one-variable identification via `uniqueAlgEquiv` |
| 4 | `[Fintype σ]` | yes | required by `Θ` (implied by `Unique`, but `Θ` takes it as an instance argument) |
| 5 | `[DecidableEq σ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.Θ_unique_le`

Internal use count: 0 outside the declaring file; 2 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:759 | `((Θ_unique_le (q := fun _ : Unit ↦ q₂) (r := fun _ ↦ l * r₂) (hM1.trans hM) hq₂).trans ?_)` in `theta_scaled_unique_le_aux` |
| Roth/Theta.lean:822 | `refine (Θ_unique_le (q := q) (r := r) (Real.one_le_rpow ...) hq1).trans_eq ?_` in `theta_lt_base_aux` |
| Roth/Theta.lean:35 | module docstring mention only |

Inline-derivation grep: (none). `grep -rn "index_unique_le_log_div\|pow_rootMultiplicity_le" Roth/` shows the helper chain is used only through `Θ_unique_le`.

### Composition check (Phase 6)

Can `Roth.Θ_unique_le` be derived in ≤3 chained calls?

Attempt 1 (the current proof): `Θ_le_of_forall_index_le hB fun _ hR _ hh ↦ index_unique_le_log_div hq hR.1 (by simpa only [Polynomial.leadingCoeff, coeff_uniqueAlgEquiv] using hR.2.2 _) (hh default)`
  - Decls used: project `Θ_le_of_forall_index_le` (itself mathlib's `csSup_le` + `indexSet_nonempty`), project `index_unique_le_log_div`, project `coeff_uniqueAlgEquiv`; mathlib `Polynomial.leadingCoeff`.
  - Result: succeeds (this is the shipped proof; it elaborates in the project build).
  - Notes: at the `Θ` level the composition is two calls. The real content (Gauss's lemma, leading-coefficient comparison, the log step) lives in the helpers, which use mathlib's `Polynomial.eq_rootMultiplicity_map`, `Polynomial.leadingCoeff_mul`, `Real.log_le_log`, `Real.log_pow`.

Conclusion: COMPOSABLE (at the `Θ` level, from `csSup_le` plus project index bounds; not from mathlib alone, since `Θ` is project-local).

## Verdict: `Roth.Θ_unique_le`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** this is the paper's Lemma 5 (clean.tex l.671–691), the one-variable step of Roth's lemma in the Cassels/Ridout `Θ_m` presentation. Its general content is the rational root theorem with multiplicity (`q^t ∣ lc(R)`).
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. `1 ≤ B` is necessary (Evidence (1), compiled), `1 < q` is necessary, and `r > 0` is already dropped.
- **Mathlib search (Phase 5):** no `Roth` namespace and no `Θ` in mathlib. The building blocks are `csSup_le`, `den_dvd_of_is_root`, `Polynomial.pow_rootMultiplicity_dvd` and Gauss's lemma.
- **Composition check (Phase 6):** COMPOSABLE as `Θ_le_of_forall_index_le` (= `csSup_le`) applied to the pointwise bound `index_unique_le_log_div`.

**Rationale:**

`Roth.Θ_unique_le` bounds the Roth-proof-specific supremum `Θ_1(B; q; r)`. `Θ` is NO-composable-from-mathlib (Roth.Θ.md) and will never be a mathlib object, so no statement about it is upstreamable. The proof is the supremum-elimination lemma `Θ_le_of_forall_index_le` (mathlib's `csSup_le`) composed with the pointwise index bound. Whatever reusable mathematics exists is the rational-root-with-multiplicity fact `q^{rootMultiplicity (h/q) R} ≤ |lc R|`, which is `Roth.pow_rootMultiplicity_le` (assessed separately as YES-but-generalise-first) and its factorisation lemma `exists_eq_pow_mul_of_rootMultiplicity`. Any upstreaming effort should target those, not this `Θ`-level wrapper.

WHY not: it is a two-call composition about a project-local quantity. Its mathlib-worthy core is already carved out into a separately assessed lemma.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean as the paper's named Lemma 5. The bucket's usual "inline at call sites" step is not recommended. The lemma has two callers (Theta.lean:759, :822), carries the paper's numbering, and inlining would duplicate the coefficient-rewrite `simpa` and the helper call at each site.

Mathlib building blocks:
- `csSup_le` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean), via project `Roth.Θ_le_of_forall_index_le`
- `Polynomial.eq_rootMultiplicity_map`, `Polynomial.leadingCoeff_mul`, `Real.log_le_log`, `Real.log_pow` (in the helper chain)
- `den_dvd_of_is_root` (Mathlib/RingTheory/Polynomial/RationalRoot.lean:89), the nearest mathlib analogue of the core
- project `Roth.index_unique_le_log_div` (private), `Roth.pow_rootMultiplicity_le`, `Roth.index_unique`

Composition sketch (the current proof):
```lean
theorem Θ_unique_le [Unique σ] {B : ℝ} (hB : 1 ≤ B) {q : σ → ℕ} (hq : 1 < q default) {r : σ → ℕ} :
    Θ B q r ≤ Real.log B / (r default * Real.log (q default)) :=
  Θ_le_of_forall_index_le hB fun _ hR _ hh ↦ index_unique_le_log_div hq hR.1
    (by simpa only [Polynomial.leadingCoeff, coeff_uniqueAlgEquiv] using hR.2.2 _) (hh default)
```

Call sites in our project (from Phase 6.0): 2, at Roth/Theta.lean:759 and Roth/Theta.lean:822.

Refactor plan: none. Keep the lemma and leave both call sites unchanged.

Next action: no upstreaming. Pursue the core via Roth.pow_rootMultiplicity_le's YES-but-generalise-first plan.

## Next step

No upstreaming. Keep `Roth.Θ_unique_le` in Roth/Theta.lean as Lemma 5 (callers Theta.lean:759, :822). The mathlib-worthy core is `Roth.pow_rootMultiplicity_le` (the rational root theorem with multiplicity), tracked in its own report.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ_unique_le/necessity.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports success with no errors; the only messages are a header-linter warning and the `#check` info. It contains:
  - (1) a compiled proof that the statement fails without `1 ≤ B`: `¬ (Θ (1/2) (fun _ : Unit ↦ 2) (fun _ ↦ 1) ≤ log (1/2) / (1 * log 2))`, using `Θ_nonneg` and `Real.log_neg`;
  - (2) `#check @Θ_unique_le`, confirming the signature uses `[Fintype σ] [Unique σ]` only (no `DecidableEq`).
- The `1 < q` necessity is argued in Phase 4 (with `q = 1`, `R = x - h` has index `1/r > 0` while the RHS is `0`); it was not compiled.
- WebSearch ×3 (queries in the table). Sources: ecroot.math.gatech.edu/siegel.pdf, arXiv 1806.05222, arXiv math/0512239, arXiv math/0307203, arXiv 2603.10561, arXiv 2502.00731, Evertse's Leiden papers.
- Lean-Finder, Loogle and LeanSearch queries as recorded in Phase 5. Grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth`; `den_dvd_of_is_root` at Mathlib/RingTheory/Polynomial/RationalRoot.lean:89.
- Local refs: clean.tex l.668–700.
- `grep -rn "Θ_unique_le\|index_unique_le_log_div" Roth/` for the call-sites table.
- Parent/sibling reports reused: Roth.Θ.md, Roth.Θ_le_of_forall_index_le.md, Roth.index_unique_le_log_div.md, and the recent pow_rootMultiplicity_le assessment (YES-but-generalise-first, per commit 31fca12).
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
