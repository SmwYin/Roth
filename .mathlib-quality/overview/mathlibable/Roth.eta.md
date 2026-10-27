---
decl: Roth.eta
file: Roth/MainLemma.lean
line: 66
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: eta is the Roth-proof parameter η = 10^m δ^((1/2)^m) of the source's eq. (36), a one-line real expression (pow times rpow) with no general mathematical content; nothing to upstream, kept locally as the paper's named η used in main_lemma and exists_delta.
action: Do not upstream; keep Roth.eta in Roth/MainLemma.lean (consumers MainLemma.lean:78/85/89/100-101/676/687/699/743/750/753, Main.lean:229-244/413-414/463); optional local tidy, move eta into Roth/Theta.lean and state Θ_lt (Theta.lean:966) and its helpers via eta.
---

# Roth.eta

## Inventory entry

### `def Roth.eta`
- **Type**: `(δ : ℝ) (m : ℕ) : ℝ`, defined as `10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)`
- **What**: the parameter `η = 10^m δ^{(1/2)^m}` of §6 of the source (clean.tex eq. (36), l.1346–1349); the upper bound from Lemma 7 (`Roth.Θ_lt`) on the index at `(h_j/q_j)_j`, and the loss in the index bound `γ - η` of Roth's Lemma 9.
- **How**: direct term; one line of real arithmetic: monoid power `10 ^ m` times real power `δ ^ ((1/2)^m)` (`Real.rpow`).
- **Hypotheses**: none (total function; meaningful for `δ ≥ 0`; for `δ < 0` `Real.rpow` gives the junk value of the complex-branch definition).
- **Uses from project**: `[]`
- **Used by**: `Roth.exists_delta_bound` (Roth/MainLemma.lean:78 statement, :85 continuity, :89 `simpa [eta, ...]`); `Roth.eta_lt_gam_iff` (MainLemma.lean:100–101); private `Roth.theta_lt_eta_of_sq_log_bound_aux` (MainLemma.lean:676 statement, :687 `simpa [eta] using Θ_lt ...`); private `Roth.exists_auxiliary_polynomial_with_index_gap_aux` (MainLemma.lean:699); `Roth.main_lemma` (MainLemma.lean:743, :750, :753); `Roth.exists_delta` (Roth/Main.lean:229, :230, :233, :244 `simpa [gam, lam, eta, ...]`); private `Roth.exists_roth_parameters_aux` (Main.lean:413, :414); private `Roth.one_lt_roth_eval_bound_aux` (Main.lean:463); module docstring MainLemma.lean:33.
- **Visibility**: public
- **Lines**: 65–66 (docstring 65, definition 66), proof length 0 lines (one-line body)
- **Notes**: Roth/Theta.lean (imported by MainLemma.lean, so it cannot see `eta`) spells the same expression inline in `Θ_lt` (Theta.lean:966) and its induction helpers (Theta.lean:787, 789, 820, 851, 856, 901, 902, 934, 949, plus `p - 1` / `p` variants at 679–711); `theta_lt_eta_of_sq_log_bound_aux` bridges with `simpa [eta]`.

## Junk check (Step 8)
- Used anywhere? Yes: statements of 7 declarations across 2 files, including the public `main_lemma`, `exists_delta`, `exists_delta_bound`, `eta_lt_gam_iff`.
- Wrapper of 1–2 mathlib calls? It is a one-line arithmetic expression (`HPow` on ℝ with ℕ and ℝ exponents), not a lemma wrapper.
- Does mathlib have it? No (Phase 5): a paper-specific constant.
- Too specific (inline?)? Inlining would bloat the statements of `main_lemma` / `exists_delta` and lose the eq. (36) correspondence. If anything the reverse: Theta.lean re-spells the expression ~10 times and could use the name if `eta` were moved upstream into Theta.lean.
- Well-chosen definition? Yes; matches the source exactly, total.
- Conclusion: `KEEP`. Optional local tidy: relocate `eta` to Roth/Theta.lean and state `Θ_lt` as `... < eta δ (n + 1)`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "The parameter"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `Roth.eta`: no hit (bare-name `def eta` hits are unrelated: `OrderType.eta`, `ProfiniteGrp...eta`, `ModularForm.eta` (Dedekind eta), category-theory `Cone.eta` etc. — MAYBE-COLLISION only, resolved in Phase 5). Not a glue lemma (it is a def; siblings `Roth.lam`, `Roth.gam` were assessed NO-composable-from-mathlib, but `eta` is an independent def), so a full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.eta`:           resolved at Roth/MainLemma.lean:66
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  §6 of the source: the main lemma (Roth's Lemma 9), its parameters λ, γ, η, B_1 and the pigeonhole step

### Statement (Phase 1)

`Roth.eta` is a definition of the following:

For a real `δ` and a natural number `m`, `η(δ, m) = 10^m · δ^{(1/2)^m}`. In the Cassels-style proof of Roth's theorem, Lemma 7 (`Roth.Θ_lt`) bounds the index of any admissible polynomial at the rational point `(h_1/q_1, …, h_m/q_m)` by `η`; the main lemma then differentiates the auxiliary polynomial `W*` to order `< η`, losing at most `η` of its index `γ` at `(α, …, α)`. `η → 0` as `δ → 0⁺` for fixed `m`, which is all the proof needs.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: the small parameter.
- `m : ℕ`: number of variables.

Hypotheses (Lean side): none.

Conclusion (math): n/a — definition.

Conclusion (Lean): n/a — definition.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under `## Main definitions`, but it is a numeric parameter, not a mathematical structure or concept.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                 | no       | consumers unfold explicitly (`simpa [eta, ...]` at MainLemma.lean:89, :687, Main.lean:244; `grind [gam, lam]` in `eta_lt_gam_iff` keeps `eta` opaque); continuity proofs at MainLemma.lean:85–86 and Main.lean:239 use defeq through the term-mode `ContinuousAt` proof; no barrier role |
| Avoid typeclass diamonds          | no       | a real number, no instance involved |
| Mark semantic intent / API name   | yes (project-local) | names the paper's η of eq. (36) in the statements of `main_lemma` (MainLemma.lean:743), `exists_delta` (Main.lean:229–230), `exists_delta_bound` (MainLemma.lean:78); benefit is paper correspondence inside the project only, no mathlib consumer |

Conclusion: ONE-LINER WITH-EXEMPTION (project-local naming only; no mathlib-level exemption)

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof eta = 10^m delta^(1/2)^m index Lemma 7 Cassels | no | n/a | no indexed text states η = 10^m δ^{(1/2)^m}; hits Cassels catalogue entry, minru roth.pdf, klazar rothovka.pdf, arXiv 2502.00731 |
| 2 | WebSearch (general form) | Roth's lemma index of polynomial at rational point bounded by 10^m delta^(2^-m) | partial | Ridout-style Θ_m bound with 10^m δ^{(1/2)^m} (as extracted); Roth's lemma `Ind ≤ 2mη` with η^{2^{m-1}} conditions (arXiv 2502.00731) | the general role (index bound tending to 0 with δ) is standard; the constant normalisation is presentation-specific |
| 3 | WebSearch (aliases) | Cassels Introduction to Diophantine Approximation Roth Lemma 9 parameters lambda gamma eta | no | n/a | book text not indexed; confirms η is local bookkeeping of Cassels Ch. VI-style proofs |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `10^m`, `\eta`, eq. (36) | yes | eq. (36) `η = 10^m δ^{(1/2)^m}` (l.1346–1349); Lemma 7 bound l.958; used at l.1220, 1358 (eq. (38) `η < γ`), 1396, 1526–1537, 1594 | exact match with the Lean body |
| 6 | nLab | Roth's theorem parameters | no | n/a | nLab has no entry on Roth's proof constants |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | numeric Diophantine parameter, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread about this constant |
| 10 | recent arXiv | 2502.00731, 1806.10737, math/0307203 | partial | as #2 | each proof uses its own constants (e.g. η^{2^{m-1}} vs δ^{2^{-m}}) |

### Literature summary (Phase 3)

Concept identified as: the index-loss parameter η of the main lemma in the Cassels/Ridout-style proof of Roth's theorem (source eq. (36)), equal to the Lemma 7 bound; not a named mathematical concept.
Sources agree on the standard form: no — each exposition chooses its own normalisation (Roth's lemma in Bombieri–Gubler / arXiv 2502.00731 uses `2mη` with η^{2^{m-1}}-type conditions).
Most general standard form: none; η is presentation-specific bookkeeping.
Generality dimensions where the literature varies:
  - base constant (10) and exponent shape (`δ^{2^{-m}}` vs `η^{2^{m-1}}`): proof-specific.
Disagreement with the literature: none; matches the source exactly.

### Generality analysis — `Roth.eta`

Literature-standard form (from Phase 3): source eq. (36), `η = 10^m δ^{(1/2)^m}`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `δ : ℝ` | real | positive real | no | already total over ℝ |
| 2 | `m : ℕ` | natural | positive integer | no | already total over ℕ |
| 3 | codomain | ℝ | ℝ | no | real power `δ^{(1/2)^m}` needs ℝ |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (a concrete numeric definition; no hypotheses or typeclasses to weaken)
Number of weakening opportunities found: 0 (nothing proposed, so nothing needed compiling)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | no hypotheses | — |
| 2 | Sequences vs filters? | no | a number; its use (`η → 0` as `δ → 0`) is already argued via `ContinuousAt` / `Metric.eventually_nhds_iff` in consumers | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | rpow needs ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `m : ℕ` is a count | — |
| 8 | Concrete-via-abstract? | no | no proof body | — |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific numeric constant; nothing to reorganise.

### Proof strategy — `Roth.eta`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | definition, no proof | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | — | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (n/a for a definition with no proof; the body is the source formula verbatim)

### Diamond / defeq risk — `Roth.eta`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | value in ℝ; `10 ^ m` uses `Monoid.npow` (ℕ exponent), `δ ^ (…)` uses `Real.rpow` (ℝ exponent) via the standard `HPow` instances; no instance introduced |
| 2 | Reducibility leak | none | plain semireducible def; consumers either unfold explicitly or rely on defeq in term-mode continuity proofs deliberately |
| 3 | Non-canonical unfolding | none | not `@[simp]`; unfolds only on request |
| 4 | Instance priority collision | none | not an instance |
| 5 | Universe-polymorphism issues | none | arguments in `Type` (ℝ, ℕ) |
| 6 | Coercion ambiguity | none | no coercion in the body (the `(1 / 2 : ℝ)` ascription fixes the rpow exponent type) |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: none

### Mathlib search-status: `Roth.eta`

[A] Lean-Finder       "real constant 10^m * δ^((1/2)^m) bound on index in Roth's lemma"   hits: `rothNumberNat_le`, `Behrend.roth_lower_bound(_explicit)`, `SzemerediRegularity.bound`, `SzemerediRegularity.initialBound` — unrelated
[B] Loogle            `ℝ → ℕ → ℝ, Real.rpow`   no hits
[C] LeanSearch        "ten to the power m times delta raised to one half to the power m"   hits: `Surreal.zsmul_pow_two_powHalf`, `LSeries.delta_*`, `Submonoid.pow` — unrelated
[D] Grep mathlib src  `namespace Roth`, `Roth.eta`, `def eta`   no `Roth` hit; bare `def eta` hits are unrelated (`OrderType.eta` Order/Types/Arithmetic.lean:138, ProfiniteGrp completion `eta`, `ModularForm` Dedekind `eta` NumberTheory/ModularForms/DedekindEta.lean:60, category-theory cone/cocone/structured-arrow `eta` isos)
[E] Name pattern      `Roth.eta` via lean_local_search   n/a: tool failed (ripgrep not on PATH); covered by [D] grep

Searched for both:
  - the user's current form (η = 10^m δ^{(1/2)^m})
  - the literature-standard form (Roth-proof index-loss parameter; none standard)

Concluded: found building blocks (`HPow ℝ ℕ ℝ` via `Monoid.npow`, `Real.rpow`, multiplication on ℝ); composition yields our form; not in mathlib as a named constant (all 5 methods).

### Normal-form check — `Roth.eta`

Equivalent formalisms this statement could take: `10 ^ m * δ ^ ((1 / 2 : ℝ) ^ m)` (current); `10 ^ m * δ ^ (2 : ℝ)⁻¹ ^ m`; `10 ^ m * δ ^ ((2 : ℝ) ^ m)⁻¹`; the m-fold iterated square root `10^m * (sqrt^[m] δ)`.
Does mathlib already have a canonical form for this idea? no (no such constant).
Proposed canonical form: current (verbatim eq. (36), matching `Θ_lt`'s statement).
RHS convention respected? n/a (definition).

### Syntactic generality — `Roth.eta`

Alternative restatements attempted:
- current
- `δ ^ ((2 : ℝ) ^ m)⁻¹` form
- iterated `Real.sqrt` form
- inlining into every statement

Chosen restatement: current.
Justification: mirrors eq. (36) and the literal statement of `Θ_lt`, so `simpa [eta] using Θ_lt …` bridges without rewriting; `Real.zero_rpow` with `(1/2)^m ≠ 0` gives `eta 0 m = 0` in one `simp` step as used at MainLemma.lean:89 and Main.lean:244.

### Superfluous-argument audit — `Roth.eta`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `δ` | yes | base of the real power |
| 2 | `m` | yes | in both exponents |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.eta`

Internal use count: 7 lines in Roth/Main.lean (3 declarations) outside the declaring file; 10 further lines (5 declarations) in Roth/MainLemma.lean
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/MainLemma.lean:78 | `δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2` (statement of `exists_delta_bound`) |
| Roth/MainLemma.lean:85 | `ContinuousAt (fun δ ↦ eta δ m + ...) 0` |
| Roth/MainLemma.lean:89 | `simpa [eta, Real.zero_rpow ...] using hgap` |
| Roth/MainLemma.lean:100 | `eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔` (statement of `eta_lt_gam_iff`) |
| Roth/MainLemma.lean:101 | `eta δ m < gam δ n m` |
| Roth/MainLemma.lean:676 | `Θ ((q 0 : ℝ) ^ (δ * r 0)) q r < eta δ m` (private `theta_lt_eta_of_sq_log_bound_aux`) |
| Roth/MainLemma.lean:687 | `simpa [eta] using Θ_lt n hδpos` |
| Roth/MainLemma.lean:699 | `gam δ f.natDegree m - eta δ m + Θ ...` (private `exists_auxiliary_polynomial_with_index_gap_aux`) |
| Roth/MainLemma.lean:743 | `gam δ f.natDegree m - eta δ m < index ...` (statement of `main_lemma`) |
| Roth/MainLemma.lean:750 | `(gam δ f.natDegree m - eta δ m) + Θ ...) / 2` (`main_lemma` proof) |
| Roth/MainLemma.lean:753 | `(γ := gam δ f.natDegree m - eta δ m + c)` (`main_lemma` proof) |
| Roth/Main.lean:229 | `eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧` (statement of `exists_delta`) |
| Roth/Main.lean:230 | `(m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ` |
| Roth/Main.lean:233 | same expression in the `ContinuousAt` goal |
| Roth/Main.lean:244 | `simpa [gam, lam, eta, Real.zero_rpow ...]` |
| Roth/Main.lean:413–414 | `eta δ m + ...` and `/ (gam δ f.natDegree m - eta δ m) < κ` (private `exists_roth_parameters_aux`) |
| Roth/Main.lean:463 | `(-(r 0 : ℝ) * (gam δ f.natDegree m - eta δ m) * κ)` (private `one_lt_roth_eval_bound_aux`) |

Inline-derivation grep (`grep -rnF "10 ^" Roth/`): the expression `10 ^ k * δ ^ ((1 / 2 : ℝ) ^ k)` is re-spelled inline in Roth/Theta.lean, which is upstream of MainLemma.lean in the import order and so cannot use `eta`:
  - Theta.lean:966 (`Θ_lt`, Lemma 7, public) `< 10 ^ (n + 1) * δ ^ ((1 / 2 : ℝ) ^ (n + 1))`
  - Theta.lean:787, 789, 820, 851, 856, 901, 902, 934, 949 (induction helpers, same shape at `n + 1`, `n + 2`, `1`)
  - Theta.lean:679–680, 710–711 (variants at `p - 1`, `p`, some with a factor 3 or a modified base `δ (1 + 1/p)`)
  These are a project-local naming opportunity (move `eta` into Theta.lean), not a mathlib signal.

### Composition check (Phase 6)

Can `Roth.eta` be derived from mathlib in ≤3 chained calls?

Attempt 1: `fun δ m ↦ (10 : ℝ) ^ m * Real.rpow δ ((1 / 2 : ℝ) ^ m)`
  - Mathlib decls used: `Monoid.npow` (via `HPow ℝ ℕ ℝ`), `Real.rpow`, `HMul` on ℝ
  - Result: succeeds (this is the body)
  - Notes: none

Conclusion: COMPOSABLE

## Verdict: `Roth.eta`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): η is the source's eq. (36) bookkeeping constant (the Lemma 7 bound); no exposition treats it as a concept, and other expositions use different normalisations.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (nothing to weaken).
- Mathlib search (Phase 5): not in mathlib; building blocks `Monoid.npow`, `Real.rpow`, multiplication on ℝ. Bare-name `eta` hits in mathlib are unrelated concepts.
- Composition check (Phase 6): COMPOSABLE (one mathlib-term expression).

**Rationale:**

`Roth.eta` is a one-line numeric constant specific to one presentation of Roth's theorem. It has no mathematical content beyond its formula, so mathlib would never want it; it is already "composed from mathlib" arithmetic. Same treatment as its siblings `Roth.lam` and `Roth.gam` (both NO-composable-from-mathlib, kept locally).

WHY not: mathlib's building blocks (`Real.rpow` in Mathlib/Analysis/SpecialFunctions/Pow/Real.lean, `Monoid.npow`, multiplication on ℝ) give the expression directly. Belongs-elsewhere check: it belongs in the Roth project as the paper's named η; it appears folded in the public statements of `main_lemma`, `exists_delta`, `exists_delta_bound` and `eta_lt_gam_iff`, so inlining would hurt readability. The only local improvement is the opposite of inlining: Roth/Theta.lean re-spells the formula about ten times, and moving `eta` there would let `Θ_lt` be stated as `Θ … < eta δ (n + 1)`.

Mathlib building blocks: `Real.rpow`, `Monoid.npow`, multiplication on `ℝ`.
Composition sketch:
```lean
example (δ : ℝ) (m : ℕ) : Roth.eta δ m = (10 : ℝ) ^ m * δ ^ ((1 / 2 : ℝ) ^ m) := rfl
```
Call sites in our project (from Phase 6.0): 18 lines in 8 declarations (MainLemma.lean:78, 85, 89, 100, 101, 676, 687, 699, 743, 750, 753; Main.lean:229, 230, 233, 244, 413, 414, 463).
Refactor plan: none recommended for these sites. (Mechanically possible: replace `eta δ m` by its body at each site; rejected because it bloats the `main_lemma` / `exists_delta` statements and loses the eq. (36) correspondence.) Optional local tidy: move `eta` to Roth/Theta.lean and restate `Θ_lt` (Theta.lean:966) and helpers via `eta`, making `simpa [eta] using Θ_lt …` at MainLemma.lean:687 a direct application.
Next action: do not upstream; keep `Roth.eta` in the project.

## Next step

Do not upstream; keep `Roth.eta` as the paper's η (optionally relocate to Roth/Theta.lean so `Θ_lt` can use the name).

## Evidence
- WebSearch ×3 (queries in the literature table): no source states this constant; arXiv 2502.00731, 1806.10737, math/0307203, Cassels catalogue, minru roth.pdf, klazar rothovka.pdf surfaced.
- Local reference clean.tex l.958 (Lemma 7 bound), l.1346–1349 (eq. (36)), 1220, 1358, 1396, 1526–1537, 1594.
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5 (no relevant hit); lean_local_search failed (ripgrep not on PATH), replaced by grep over `.lake/packages/mathlib/Mathlib/` (no `Roth` hit; unrelated bare `def eta` hits listed).
- `grep -rnw eta Roth/` for call sites; `grep -rnF "10 ^" Roth/` for inline re-derivations (Theta.lean). No Lean experiments were needed (no weakening proposed; the composition sketch is the definitional body); no evidence files written.
