---
decl: Roth.approxSet
file: Roth/Main.lean
line: 55
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: approxSet is a one-line set-builder for the paper's eq. (1) over mathlib primitives; the mathlib notion carrying the same content is LiouvilleWith (whose docstring already names Thue-Siegel-Roth as the p > 2 statement), and a compiled bridge shows that, for irrational α, Roth.roth is equivalent to the statement that no α satisfies LiouvilleWith p α for p > 2, so the set itself has nothing to upstream.
action: Do not upstream approxSet; keep it in Roth/Main.lean as the paper's eq. (1) (call sites in Main.lean and LeanEval.lean); the mathlib-facing form of Roth's theorem is roth_not_liouvilleWith (two bridges, compiled in evidence/Roth.approxSet/liouvilleWith_bridge.lean), to be added next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean if Roth is ever upstreamed.
---

# Roth.approxSet

## Inventory entry

### `def Roth.approxSet`
- **Type**: `(α κ : ℝ) : Set (ℤ × ℕ)`
- **What**: The set of pairs `(h, q)` with `q > 0` and `|α - h/q| < 1/q^κ` (real power `κ`): the approximations of `α` of quality `κ`. Pairs need not be reduced.
- **How**: Set-builder `{hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}`, using `Real.rpow` and `abs`.
- **Hypotheses**: none.
- **Uses from project**: `[]`
- **Used by**: Roth/Main.lean: `approxSet_den_le_finite` (73), `reduction` (119–124), `approxSet_num_den_mem_aux` (149–150, private), `exists_reduced_approx` (165–182), `exists_approximants` (257–264), `exists_degrees` (430–431), `roth_of_isIntegral` (548), `roth` (574), `roth_rat` (indirectly through `roth`); Roth/LeanEval.lean: `exists_pos_div_rpow_lt_aux` (21, 35, private), `isDiophantine_iff` (43, 49).
- **Visibility**: public
- **Lines**: 55–56, proof length 0 lines (2-line def body)
- **Notes**: Source: clean.tex §6 eq. (1) (`roth:eq1`, l.1141–1143) and the Theorem (Roth) that follows it. The set includes non-reduced pairs. Only `.Infinite` and membership are ever used.

## Junk check (Step 8)
- Used anywhere? Yes. It appears in the statements of the main theorems (`roth`, `roth_of_isIntegral`), of the reduction and approximant-selection lemmas in Main.lean, and of the LeanEval bridge `isDiophantine_iff`.
- Wrapper of 1–2 mathlib calls? It is a one-line `setOf` over mathlib primitives (`abs`, `Real.rpow`, casts). It is not a wrapper of a mathlib lemma.
- Does mathlib have it? Not as a set. The closest mathlib notions are `LiouvilleWith p x` (∃ C, frequently in n, ∃ m, x ≠ m/n ∧ |x - m/n| < C/n^p), `Liouville`, and the `ℚ`-indexed set `{q : ℚ | |ξ - q| < 1 / q.den ^ 2}` in `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`. The evidence file shows that "`approxSet α κ` infinite" and `LiouvilleWith` can be converted into each other, up to an arbitrarily small loss in the exponent in one direction.
- Too specific (inline?)? Inlining the conjunction at about 10 statement sites would make the Main.lean statements harder to read. The name is the paper's eq. (1).
- Well-chosen definition? Yes for the project. It is phrased with pairs `(h, q)` exactly as in the paper, and `approxSet_den_le_finite` works naturally with `ℤ × ℕ`.

Conclusion: KEEP. No local action.

## Mathlibable assessment (Step 9)

Pre-filter: the def is public, its name does not end in `_aux`, its docstring is not internal or auxiliary, and Step 8 said KEEP. Mathlib has no `namespace Roth` and no `approxSet` (grep over `.lake/packages/mathlib/Mathlib/`). It is not a glue lemma. Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.approxSet`:     resolved at Roth/Main.lean:55
- kind:                      def
- has sorry:                 no
- module docstring summary:  Roth's theorem (`Roth.roth`): an irrational real algebraic number has only finitely many approximations of quality `κ > 2`, stated with `Roth.approxSet`.

### Statement (Phase 1)

`Roth.approxSet` is a definition. For real `α` and `κ` it is the set

  `A(α, κ) = { (h, q) ∈ ℤ × ℕ : q > 0, |α − h/q| < q^{−κ} }`,

the integer pairs giving rational approximations of `α` of quality (exponent) `κ`. Roth's theorem says that if `α` is irrational and algebraic and `A(α, κ)` is infinite, then `κ ≤ 2`.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the number being approximated.
- `κ : ℝ`: the approximation exponent (real power, `Real.rpow`).

Hypotheses (Lean side):
- none.

Conclusion (math): a subset of `ℤ × ℕ`.

Conclusion (Lean): n/a — definition (`def approxSet (α κ : ℝ) : Set (ℤ × ℕ) := {hq | 0 < hq.2 ∧ |α - (hq.1 : ℝ) / hq.2| < 1 / (hq.2 : ℝ) ^ κ}`).

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is the set used to state the project's main result, but it is notation for the paper's eq. (1). It introduces no new structure, and the concept it expresses (exponent-`κ` approximability) already exists in mathlib as `LiouvilleWith`.

(Literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | membership is unfolded freely (`⟨hq0, happ⟩` destructuring in `approxSet_den_le_finite`, `exists_pos_div_rpow_lt_aux`); nothing relies on sealing |
| Avoid typeclass diamonds         | no       | no instances |
| Mark semantic intent / API name  | yes (project only) | it appears in the statements of `roth`, `roth_of_isIntegral`, `reduction`, `exists_approximants`, `exists_degrees`, and `LeanEval.isDiophantine_iff`. In mathlib the stable name for this idea is already `LiouvilleWith` |

Conclusion: ONE-LINER WITH-EXEMPTION (the exemption covers the project only and does not argue for mathlib)

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem infinitely many rationals h/q with abs(alpha - h/q) < q^-kappa statement set of approximations | yes | "for κ > 2, `|α − h/q| < q^{−κ}` has only finitely many solutions" | Wikipedia "Roth's theorem"; Roth 1955 (Mathematika). The statement uses an inequality and its solution set, never a named set |
| 2 | WebSearch (general form) | irrationality exponent definition supremum mu such that 0 < abs(x - p/q) < 1/q^mu has infinitely many solutions | yes | irrationality exponent `μ(ξ) = sup{μ : |ξ − p/q| < q^{−μ} for infinitely many p/q}`; Roth ⇔ `μ(α) = 2` | Wikipedia "Irrationality measure"; Bugeaud (arXiv 2510.02059, Def. 1.1). Variants: coprime vs arbitrary pairs, `<` vs `≤` |
| 3 | WebSearch (named-after / aliases) | Liouville-Roth irrationality measure approximation exponent psi-approximable numbers definition | yes | "ψ-well approximable": `|ξ − p/q| < ψ(q)` has infinitely many solutions. Exponent version: `q^{−μ}`-approximable. Liouville numbers have `μ = ∞` | Waldschmidt notes (HCMUNS10); arXiv 2210.16553 (geometry of Diophantine exponents) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` §6 l.1141–1192 and l.1639–1644 | yes | eq. (1): `|α − h/q| < 1/q^κ` for infinitely many integer pairs `h, q` with `q > 0` | matches the Lean def exactly (pairs not required coprime). The paper's Lean note cites mathlib's DiophantineApproximation module as the reference formulation |
| 6 | nLab | irrationality measure / Diophantine approximation | no | — | nLab has no page on approximation exponents (it covers number theory only sparsely) |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | partial | irrationality measure, coprime-vs-not discussions | folklore. Answers there also state results as "the inequality has infinitely many solutions" |
| 10 | recent arXiv (last 5 years) | (results of #2, #3) | yes | arXiv 2510.02059 (2025), 2411.10733 (2024), 2210.16553 (2022) | all define the exponent through the inequality and never name the solution set |

### Literature summary (Phase 3)

Concept identified as: approximations of `α` of exponent `κ`. These are the solutions of the Dirichlet/Roth inequality `|α − p/q| < q^{−κ}`. Their infinitude defines "`q^{−κ}`-well approximable", and the supremum over `κ` is the irrationality exponent (Liouville–Roth irrationality measure).
Sources agree on the standard form: yes, up to coprimality (immaterial for the exponent) and `<` vs `≤`.
Most general standard form: for a function `ψ`, the `ψ`-approximations `{p/q : |ξ − p/q| < ψ(q)}`. The literature's object of interest is the predicate "infinitely many solutions" (or the exponent `μ(ξ)`), not the set itself.
Generality dimensions where the literature varies:
  - approximation function: `q^{−κ}` (Roth) vs `C q^{−κ}` (Liouville-with-exponent, as in mathlib) vs general `ψ(q)` (metric Diophantine approximation).
  - indexing: integer pairs (here, the paper) vs reduced fractions / `ℚ` (mathlib's `{q : ℚ | |ξ − q| < 1/q.den^2}`).
Disagreement with the literature: none. No source treats the solution set as a standalone object.

### Generality analysis — `Roth.approxSet`

Literature-standard form (from Phase 3): `ψ`-approximations `{(p, q) : q > 0, |ξ − p/q| < ψ(q)}`. What gets used is their infinitude, i.e. `LiouvilleWith`-type predicates.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | approximation function `q^{−κ}` | `1 / q ^ κ` | `ψ(q)` | yes, but no gain | Roth's theorem is about the exponent. A `ψ`-version (`{hq | 0 < hq.2 ∧ |α - hq.1/hq.2| < ψ hq.2}`) would just be a different setOf with no project or mathlib consumer |
| 2 | constant `1` in the numerator | `1 / q^κ` | `C / q^κ` (mathlib `LiouvilleWith`) | equivalent for the exponent question | evidence: `liouvilleWith_of_approxSet_infinite` and `approxSet_infinite_of_liouvilleWith` (exponent loss ε in one direction) |
| 3 | index type `ℤ × ℕ` | integer pairs | `ℚ` / reduced fractions | equivalent | `roth_rat` already converts the `ℚ` form into `approxSet` in 4 lines |
| 4 | `α κ : ℝ` | real | real | no | the setting is real Diophantine approximation |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (as notation; the def has no hypotheses to drop)
Number of weakening opportunities found: 0. Rows 1–3 are reformulations, not weakenings of hypotheses.
Proposed restatement: none for the set. The mathlib-facing restatement of what the set is used for is the `LiouvilleWith` form (Phase 4c).
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | no hypotheses |
| 2 | sequences to filters? | yes | "`approxSet α κ` infinite" becomes `∃ᶠ n in atTop, ∃ m, α ≠ m/n ∧ |α - m/n| < C/n^p`, i.e. `LiouvilleWith p α` | the whole `LiouvilleWith` API (`mono`, `frequently_lt_rpow_neg`, `mul_rat`, `add_rat`, `irrational`, `ne_cast_int`, `forall_liouvilleWith_iff`). For instance, the project's reduction `α ↦ Mα` is `LiouvilleWith.mul_nat` |
| 3 | construction vs universal property? | no | — | a subset |
| 4 | bundled substructure? | no | — | not closed under any operation |
| 5 | field-specific to semiring? | no | — | real setting |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | `ℤ × ℕ` pairs are standard |
| 8 | concrete-via-abstract? | no | — | no proof body |
| 9 | false-generalisation guard | no false generalisation | the `LiouvilleWith` form keeps the content of the exponent question: evidence `roth_iff_not_liouvilleWith` (for irrational `α`, Roth's `∀ κ, approxSet infinite → κ ≤ 2` ⇔ `∀ p > 2, ¬ LiouvilleWith p α`) compiles | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but it applies to the *statement of Roth's theorem*, not to `approxSet`.
  - Proposed mathlib-idiomatic restatement: `theorem roth_not_liouvilleWith {α : ℝ} (hα : Irrational α) (halg : IsAlgebraic ℚ α) {p : ℝ} (hp : 2 < p) : ¬ LiouvilleWith p α` (compiled as a one-line corollary of `Roth.roth` in the evidence file).
  - Cost: CHEAP (the two bridges total about 25 lines, compiled).
  - Mathlib downstream this enables: it fills the gap that the `LiouvilleWith.lean` module docstring states in prose ("If `p > 2` ... Thue–Siegel–Roth theorem states that such numbers must be transcendental") and plugs into the `LiouvilleWith` API.
  - Real mathematical improvement: the theorem is stated against mathlib's existing approximability predicate, so no new set or predicate is needed. `approxSet` then stays a local proof device.

### Proof strategy — `Roth.approxSet`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | `Set.Infinite` of pairs vs `∃ᶠ n in atTop` (`LiouvilleWith`); the project's set form suits the pigeonhole and finiteness steps (`approxSet_den_le_finite`, `exists_reduced_approx`) | MODERATE to rewrite Main.lean internally; not recommended, since bridging only at the final statement is CHEAP |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | the bridge `Irrational α → (Set.Infinite of approximations) → LiouvilleWith κ α`, and its converse with exponent loss. Mathlib has neither (it only has `LiouvilleWith.frequently_lt_rpow_neg`) | follow-up together with Roth, if upstreamed |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a definition with no proof; a set-builder for the paper's inequality is the natural shape for the project's internal use)

### Diamond / defeq risk — `Roth.approxSet`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | defines no instances; it uses only `ℝ` abs, `Real.rpow` and casts |
| 2 | Reducibility leak | none | plain semireducible def. Membership unfolds by `Iff.rfl` (evidence, first `example`) and by anonymous-constructor patterns, which is the intended use |
| 3 | Non-canonical unfolding | low | `1 / q ^ κ` with real `rpow` instead of `q ^ (-κ)` (the form `LiouvilleWith.frequently_lt_rpow_neg` uses). The evidence bridges need one `Real.rpow_neg` + `one_div` rewrite |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | monomorphic (`ℤ × ℕ`, `ℝ`) |
| 6 | Coercion ambiguity | none | it uses the standard `ℤ → ℝ` and `ℕ → ℝ` casts and defines no coercions |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.approxSet`

[A] Lean-Finder       "set of rational approximations p/q with |x - p/q| < 1/q^κ, infinitely many, irrationality exponent"   hits: `LiouvilleWith`, `LiouvilleWith.exists_pos`, `LiouvilleWith.frequently_lt_rpow_neg`, `Liouville`, `Liouville.frequently_exists_num`, `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, `..._iff_irrational`, `setOf_liouville_eq_irrational_inter_iInter_iUnion`
[B] Loogle            `Set.Infinite, |_ - _|, Rat.den`   hits: `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, `Real.infinite_rat_abs_sub_lt_one_div_den_sq_iff_irrational` (exponent 2 only, `ℚ`-indexed)
[C] LeanSearch        "LiouvilleWith p x: infinitely many rationals with |x - m/n| < n^(-p)"   hits: `LiouvilleWith`, `Liouville`, `liouvilleWith_one`, `LiouvilleWith.frequently_lt_rpow_neg`, `Liouville.liouvilleWith`, `forall_liouvilleWith_iff`
[D] Grep mathlib src  `irrationalityExponent`, `irrationalityMeasure`, `approxSet`, `namespace Roth`: no hits. `def LiouvilleWith` (NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:51; its module docstring l.26–28 cites Thue–Siegel–Roth for `p > 2`, unformalised). `exists_rat_abs_sub_lt_and_lt_of_irrational` (DiophantineApproximation/Basic.lean:176), `infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` (:197), `exists_int_int_abs_mul_sub_le` (:95, Dirichlet). No Thue–Siegel–Roth formalisation
[E] Name pattern      `LiouvilleWith.frequently_lt_rpow_neg`, `Nat.frequently_atTop_iff_infinite`, `Irrational.ne_rational`, `Real.rpow_neg` (all used in compiled evidence)

Searched for both the user's form (pairs with `|α − h/q| < q^{−κ}`) and the literature-standard form (exponent-`κ` approximability / irrationality exponent).

Concluded: found building blocks, with `LiouvilleWith` as the mathlib predicate for the literature-standard notion. No mathlib set of approximation pairs and no irrationality-exponent def.

### Normal-form check — `Roth.approxSet`

Equivalent formalisms: (a) "`approxSet α κ` infinite" (current, pairs); (b) `{x : ℚ | |α - x| < 1 / x.den ^ κ}.Infinite` (the mathlib Dirichlet style, used in `roth_rat`); (c) `LiouvilleWith κ α` (filter form with a constant; equivalent up to ε in the exponent); (d) the irrationality exponent `μ(α) ≥ κ` (no mathlib def).
Does mathlib already have a canonical form for this idea? yes: `LiouvilleWith` (`Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:51`).
Is our statement stated against the canonical form? No. For the project this is fine, since the set suits the internal pigeonhole and finiteness arguments. For mathlib, Roth should be stated against `LiouvilleWith`: evidence `roth_iff_not_liouvilleWith` has the form `our_form ↔ canonical_form` with the canonical form on the RHS.
RHS convention respected? yes (in the bridge).

### Syntactic generality — `Roth.approxSet`

Alternative restatements attempted:
- pairs `ℤ × ℕ` (current)
- `ℚ`-indexed set (`roth_rat` input form)
- `LiouvilleWith` predicate (evidence)
Chosen restatement: current, for the project. `approxSet_den_le_finite`, `exists_reduced_approx` and `exists_approximants` all manipulate pairs and denominators directly.
Justification: easiest to supply and consume in Main.lean. The `LiouvilleWith` form is the right one only at the mathlib boundary.

### Superfluous-argument audit — `Roth.approxSet`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `α` | yes | number approximated |
| 2 | `κ` | yes | exponent |

### Statement-shape verdict (Phase 5.5)

Normal form: OK for the project. For mathlib, the canonical form is `LiouvilleWith` (bridge compiled).
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project def)

### Call sites — `Roth.approxSet`

Internal use count: 4 lines outside the declaring file (Roth/LeanEval.lean), plus about 25 lines in the declaring file Main.lean
External-to-file callers: 1 distinct file (LeanEval.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/LeanEval.lean:21 | `(hs : (Roth.approxSet x κ).Finite)` in private `exists_pos_div_rpow_lt_aux` |
| Roth/LeanEval.lean:35 | `by_cases hmem : (p, q) ∈ Roth.approxSet x κ` |
| Roth/LeanEval.lean:43 | `IsDiophantine x ↔ ∀ {κ : ℝ}, (Roth.approxSet x κ).Infinite → κ ≤ 2` |
| Roth/LeanEval.lean:49 | `(hinf.sdiff (Roth.approxSet_den_le_finite x κ Q)).nonempty` |
| Roth/Main.lean:73 | `approxSet_den_le_finite ... {hq ∈ approxSet α κ | hq.2 ≤ Q₀}.Finite` |
| Roth/Main.lean:119–124 | `reduction ... (hinf : (approxSet α κ).Infinite) ... (approxSet α' κ').Infinite` |
| Roth/Main.lean:149–150 | private `approxSet_num_den_mem_aux` (reduced pair stays in the set) |
| Roth/Main.lean:165–182 | `exists_reduced_approx ... ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ ...` |
| Roth/Main.lean:257–264 | `exists_approximants ... (∀ j, (h j, q j) ∈ approxSet α κ)` |
| Roth/Main.lean:430–431 | `exists_degrees ... (∀ j, (h j, q j) ∈ approxSet α κ)` |
| Roth/Main.lean:548 | `roth_of_isIntegral ... (hinf : (approxSet α κ).Infinite) : κ ≤ 2` |
| Roth/Main.lean:574 | `roth ... (hinf : (approxSet α κ).Infinite) : κ ≤ 2` |

Inline-derivation grep:
  - Roth/Main.lean:581–586 `roth_rat` restates the condition over `ℚ` (`{x : ℚ | |α - x| < 1 / x.den ^ κ}`) and maps it into `approxSet`. This is a consumer, not a bypass.
  - Roth/LeanEval.lean:16–17 `IsDiophantine` restates the complementary bound `C / q^(2+ε) < |x - p/q|`. It is the external problem statement and is linked to `approxSet` by `isDiophantine_iff`.

### Composition check (Phase 6)

Can `Roth.approxSet` be derived from mathlib in ≤3 chained calls?

Attempt 1: inline the definition, `{hq : ℤ × ℕ | 0 < hq.2 ∧ |α - hq.1 / hq.2| < 1 / (hq.2 : ℝ) ^ κ}`
  - Mathlib decls used: `setOf`, `abs`, `Real.rpow`, `Int.cast`, `Nat.cast`
  - Result: succeeds. The def is a single set-builder over mathlib primitives (membership is `Iff.rfl`, evidence first `example`).
  - Notes: the only real use is `.Infinite`. For the mathlib-facing statement, that is replaced by `LiouvilleWith` (Attempt 2).

Attempt 2: replace "`(approxSet α κ).Infinite`" by `LiouvilleWith κ α`
  - Mathlib decls used: `LiouvilleWith`, `LiouvilleWith.frequently_lt_rpow_neg`, `Nat.frequently_atTop_iff_infinite`, `Irrational.ne_rational`
  - Result: partial. The two bridges are about 10 lines each (compiled), not ≤3 calls, and the converse loses ε in the exponent. Together they give `roth_iff_not_liouvilleWith`, and Roth in mathlib form follows in one line.
  - Notes: this moves the theorem's statement to mathlib's vocabulary. It does not replace the set inside the project's proof.

Conclusion: COMPOSABLE (the def itself is a one-line composition of mathlib primitives. The mathlib concept it serves is `LiouvilleWith`.)

## Verdict: `Roth.approxSet`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the literature uses the inequality `|α − p/q| < q^{−κ}` and its "infinitely many solutions" predicate (well-approximability / irrationality exponent). It never uses a named solution set. Source eq. (1) matches the def exactly.
- Generality analysis (Phase 4): MAXIMALLY GENERAL as notation (no hypotheses). Modern idiom: state Roth via `LiouvilleWith`, compiled.
- Mathlib search (Phase 5): building blocks plus `LiouvilleWith`. Mathlib has no set of approximation pairs and no irrationality exponent. The `LiouvilleWith.lean` docstring names Thue–Siegel–Roth as the unformalised `p > 2` statement.
- Composition check (Phase 6): COMPOSABLE (single set-builder over mathlib primitives).

**Rationale:**

`approxSet` is a one-line set-builder over `abs`, `Real.rpow` and casts. It names the solution set of the paper's eq. (1). The literature never treats that set as an object: the content is the predicate "infinitely many solutions", and mathlib already formalises that predicate as `LiouvilleWith p x` (with a constant `C`, in filter form). The evidence file compiles both bridges. With irrationality, infinitely many approximations of quality `κ` give `LiouvilleWith κ α`. Conversely, `LiouvilleWith p α` gives an infinite `approxSet α κ` for every `κ < p`. Hence `roth_iff_not_liouvilleWith`: for irrational `α`, the project's form of Roth is equivalent to `∀ p > 2, ¬ LiouvilleWith p α`. That is exactly the statement the `LiouvilleWith` module docstring attributes to Thue–Siegel–Roth.

So `approxSet` has nothing to upstream. If Roth's theorem is ever contributed, its mathlib statement should be `roth_not_liouvilleWith` (compiled as a one-line corollary of `Roth.roth`), with `approxSet` kept as a local proof device or inlined there. Inside the project the set is good API: it is the paper's notation, it suits the finiteness and pigeonhole lemmas (`approxSet_den_le_finite`, `exists_reduced_approx`), and the LeanEval bridge uses it. So no local change is needed.

WHY not (refactor-actionable): mathlib's building blocks (`setOf`, `abs`, `Real.rpow`, casts) give the set in one line, and mathlib's `LiouvilleWith` already carries its meaning. A mathlib PR adding `approxSet` would add a second name for an existing notion. The correct mathlib target is the theorem `¬ LiouvilleWith p α` for `p > 2`, not the set.

Belongs-elsewhere check: keep `Roth.approxSet` project-local in Roth/Main.lean, as the paper's eq. (1) and the hypothesis shape of `Roth.roth`.

Mathlib building blocks:      `setOf`, `abs`, `Real.rpow` (Mathlib/Analysis/SpecialFunctions/Pow/Real.lean), `LiouvilleWith` (Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean:51), `LiouvilleWith.frequently_lt_rpow_neg` (same file:97), `Nat.frequently_atTop_iff_infinite`, `Irrational.ne_rational`
Composition sketch (≤3 lines):
```lean
example (α κ : ℝ) (h : ℤ) (q : ℕ) :
    (h, q) ∈ Roth.approxSet α κ ↔ 0 < q ∧ |α - h / q| < 1 / (q : ℝ) ^ κ := Iff.rfl
-- mathlib-facing form of the theorem the set serves (compiled in the evidence file):
-- theorem roth_not_liouvilleWith (hα : Irrational α) (halg : IsAlgebraic ℚ α) (hp : 2 < p) :
--     ¬ LiouvilleWith p α := (roth_iff_not_liouvilleWith hα).1 (Roth.roth hα halg) p hp
```
Call sites in our project (from Phase 6.0):  4 outside Main.lean (LeanEval.lean:21, 35, 43, 49), about 25 inside Main.lean
Refactor plan: no inlining at the call sites. The set is the paper's notation, and inlining it into the statements of `roth`, `roth_of_isIntegral`, `reduction`, `exists_reduced_approx`, `exists_approximants`, `exists_degrees` and `LeanEval.isDiophantine_iff` would only hurt readability. Optionally add `approxSet_infinite_of_liouvilleWith`, `liouvilleWith_of_approxSet_infinite` and `roth_not_liouvilleWith` from the evidence file to Roth/Main.lean (after `roth_rat`) as the mathlib-vocabulary corollary.
Next action: keep `Roth.approxSet` in the project and do not upstream it. If Roth is upstreamed, state it as `roth_not_liouvilleWith` next to Mathlib/NumberTheory/Transcendental/Liouville/LiouvilleWith.lean, with the bridges from the evidence file.

---

## Next step

Keep `Roth.approxSet` project-local. Optionally add the compiled `LiouvilleWith` bridges and `roth_not_liouvilleWith` after `Roth.roth_rat` in Roth/Main.lean as the mathlib-facing statement of Roth's theorem.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.approxSet/liouvilleWith_bridge.lean` (imports `Roth.Main` and `Mathlib.NumberTheory.Transcendental.Liouville.LiouvilleWith`): it proves membership by `Iff.rfl`, `approxSet_infinite_of_liouvilleWith`, `liouvilleWith_of_approxSet_infinite`, `roth_iff_not_liouvilleWith` and `roth_not_liouvilleWith`. `lean_diagnostic_messages` reports no diagnostics (clean). The first `lake env lean` run failed only because the `LiouvilleWith` import was missing. It was fixed in place and re-checked with the LSP.
- Searches: 3 WebSearch queries, Lean-Finder, LeanSearch, Loogle, grep over mathlib (`irrationalityExponent`, `irrationalityMeasure`, `approxSet`, `namespace Roth`, `LiouvilleWith`, the DiophantineApproximation/Basic.lean theorems), and grep of the project (`approxSet`) and of clean.tex (eq. (1), §6). These are recorded in the tables above.
