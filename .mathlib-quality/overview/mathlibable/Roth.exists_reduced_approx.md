---
decl: Roth.exists_reduced_approx
file: Roth/Main.lean
line: 164
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: CHEAP
junk: KEEP
rationale: Stated over the project-local approxSet (NO-composable) so it cannot go upstream as is; its content, that for irrational x infinitely many unreduced approximations of quality κ > 0 give infinitely many rationals x with abs(x - r) below r.den^(-κ), is missing from mathlib (no bridge between the unreduced LiouvilleWith-style form and the den-form of Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational), so whether that generic equivalence is worth upstreaming is a judgment call.
action: Keep in Roth/Main.lean (single caller exists_approximants at line 261); if the human approves, upstream the compiled equivalence approxSet_infinite_iff_rat (evidence/Roth.exists_reduced_approx/rat_form.lean), restated with LiouvilleWith-style unreduced fractions, to Mathlib/NumberTheory/DiophantineApproximation/Basic.lean.
---

# Roth.exists_reduced_approx

## Inventory entry

### `theorem Roth.exists_reduced_approx`
- **Type**: `{α : ℝ} (hα : Irrational α) {κ : ℝ} (hκ : 0 < κ) (hinf : (approxSet α κ).Infinite) (Q₀ : ℕ) : ∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ)`
- **What**: If α is irrational, κ > 0 and α has infinitely many (possibly unreduced) approximations h/q of quality κ, then for every bound Q₀ there is a reduced approximation h/q (gcd 1) of quality κ with q > Q₀.
- **How**: By contradiction. Let ρ(h, q) = h/q ∈ ℚ. (1) The image ρ(approxSet α κ) is finite: each value's reduced form (num, den) is again in `approxSet` (`approxSet_num_den_mem_aux`, needs κ ≥ 0) and is coprime (`Rat.reduced`, `Int.isCoprime_iff_gcd_eq_one`), so by the contradiction hypothesis den ≤ Q₀; the image therefore lies in the image of the finite set `approxSet_den_le_finite α κ Q₀` (`Rat.num_div_den`). (2) Each fibre {hq | ρ hq = x} is finite: since α is irrational, |α − x| > 0 (`Irrational.ne_rat`), and `eventually_div_rpow_lt` with M = 1/|α − x| bounds q by some N, so the fibre sits in `approxSet_den_le_finite α κ N`. (3) `Set.Finite.of_finite_fibers` then makes `approxSet α κ` finite, contradicting `hinf`.
- **Hypotheses**: `hα` irrational (needed: for rational α = a/b and κ > 1 there are infinitely many unreduced solutions (ka, kb) but no reduced ones with large denominator); `hκ : 0 < κ` (used for reduction monotonicity and for the fibre bound; see Phase 5.5 for whether the conclusion needs it); `hinf` infinite approximation set.
- **Uses from project**: `Roth.approxSet`, `Roth.approxSet_den_le_finite`, `Roth.approxSet_num_den_mem_aux`, `Roth.eventually_div_rpow_lt`
- **Used by**: Roth/Main.lean:261 `Roth.exists_approximants` (only; `grep -rn exists_reduced_approx Roth/`).
- **Visibility**: public
- **Lines**: 164–186, proof length 21 lines
- **Notes**: Source: clean.tex §7 l.1578–1587 ("We first justify choosing reduced solutions of arbitrarily large denominator ... the reduced denominators are unbounded as well").

## Junk check (Step 8)
- Used anywhere? Yes, once: `exists_approximants` (Main.lean:261) `choose`s a reduced approximant above every bound to build the rapidly growing sequence q_1 < q_2 < ... .
- Wrapper of 1–2 mathlib calls? No: a 21-line fibre argument (`Set.Finite.of_finite_fibers` plus two project finiteness lemmas).
- Does mathlib have it? No. The nearest are `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` (κ = 2, already in den-form, no unreduced hypothesis) and the unreduced `LiouvilleWith` API; nothing converts between the unreduced and reduced forms.
- Too specific (inline?)? One caller, but inlining a 21-line argument into the already long `exists_approximants` would hurt readability, and it matches a self-contained paragraph of the paper.
- Well-chosen? Yes: it is exactly what `exists_approximants` consumes.

Conclusion: KEEP. No action.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring is not internal/auxiliary; Step 8 said KEEP; mathlib has no `Roth` namespace (grep of `Mathlib/` for `exists_reduced_approx`: only unrelated `exists_reduced_factors`, `exists_reduced_word`). Not a glue lemma (21-line proof). Full run.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Main` elaborates with no diagnostics)
- decl `Roth.exists_reduced_approx`: resolved at Roth/Main.lean:164
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  Roth's theorem for real algebraic numbers, stated with `Roth.approxSet` and reduced via §6 to algebraic integers.

### Statement (Phase 1)

`Roth.exists_reduced_approx` is a theorem stating the following:

Let α be irrational and κ > 0. Suppose there are infinitely many pairs (h, q) ∈ ℤ × ℕ with q > 0 and |α − h/q| < q^{−κ}. Then for every Q₀ there is such a pair with q > Q₀ and gcd(h, q) = 1. Equivalently: the rationals r with |α − r| < den(r)^{−κ} have unbounded denominators, i.e. there are infinitely many of them.

Variables / typeclasses involved (Lean side):
- `α : ℝ`: the number being approximated.
- `κ : ℝ`: the approximation exponent.
- `Q₀ : ℕ`: the denominator threshold.

Hypotheses (Lean side):
- `hα : Irrational α`: makes |α − r| > 0 for every rational r, so each rational is represented by only finitely many solution pairs.
- `hκ : 0 < κ`: the bound q^{−κ} decreases in q (reducing a fraction keeps it a solution; large q violate a fixed positive error).
- `hinf : (approxSet α κ).Infinite`: infinitely many unreduced solutions.

Conclusion (math): there is a reduced solution with denominator larger than Q₀.

Conclusion (Lean): `∃ hq ∈ approxSet α κ, Q₀ < hq.2 ∧ IsCoprime hq.1 (hq.2 : ℤ)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a technical step of §7 (choosing reduced approximants), used once; not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a: kind is theorem. MULTI-LINE (21-line proof); check skipped.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | infinitely many solutions abs(α - p/q) < q^{-κ} may assume gcd(p,q)=1 reduced fractions without loss of generality irrational | yes (folklore) | reduce P/Q to lowest terms p/q; the bound only improves; one must still show infinitely many distinct reduced fractions | AoPS wiki "Rational approximation" (Dirichlet argument), Dummit lecture notes, arXiv 2109.11003 (Duffin–Schaeffer reduced setting) |
| 2 | WebSearch (general form) | irrationality exponent definition coprime p q equivalent unreduced fractions infinitely many rationals | yes | irrationality exponent μ(α) = sup of μ with infinitely many rationals p/q (or coprime pairs) satisfying abs(α - p/q) < q^{-μ}; sources switch freely between "rationals" and "coprime pairs" | Wikipedia "Irrationality measure", arXiv 2210.16553, 2001.00297, 2202.10738; the equivalence of the two conventions is used silently |
| 3 | WebSearch (named / aliases) | Roth theorem proof choose reduced solutions arbitrarily large denominator approximants h_j/q_j gcd 1 | partial | Roth's theorem stated for coprime p, q (Wikipedia); the selection step is never isolated | Croot's Siegel notes, arXiv 1806.10737 (function-field Roth) |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for "reduced" | yes | l.1578–1587: reducing preserves the inequality since b ≤ q and κ > 0; irrationality bounds the denominators representing a fixed rational; hence infinitely many distinct reduced solutions with unbounded denominators | matches the Lean proof step for step |
| 6 | nLab | "Diophantine approximation", "irrationality measure" | no | no page for the reduced/unreduced equivalence | nLab has no Diophantine approximation content at this level |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | not an algebraic-geometry concept |
| 9 | MathOverflow / Math.SE | (results of #1, #2) reduced fractions in definition of irrationality measure | yes (folklore) | "counting unreduced pairs would let (kp, kq) repeat a solution; restricting to coprime pairs or to rationals is the same for irrational α" | exercise level |
| 10 | recent arXiv | (results of #2) irrationality exponent coprime | partial | arXiv 2210.16553, 2202.10738 define exponents with coprime pairs or rationals interchangeably | no source states the equivalence as a lemma |

### Literature summary (Phase 3)

Concept identified as: for irrational α, the approximation property "infinitely many solutions of |α − p/q| < q^{−κ}" is the same whether one counts unreduced pairs, coprime pairs, or rationals (with their reduced denominators), provided κ > 0. Used silently in every definition of the irrationality exponent and in Roth's proof.
Sources agree on the standard form: yes (folklore; never named).
Most general standard form: for irrational α and κ > 0, {(p, q) : q > 0, |α − p/q| < q^{−κ}} is infinite iff {r ∈ ℚ : |α − r| < den(r)^{−κ}} is infinite (iff the reduced denominators are unbounded).
Generality dimensions where the literature varies:
  - bound: q^{−κ} (here), C q^{−κ}, ψ(q) with ψ non-increasing (the reduction step needs ψ non-increasing; the fibre step needs ψ → 0).
  - phrasing: unbounded denominators (here) vs infinitely many rationals vs `∃ᶠ n in atTop` (mathlib's `LiouvilleWith`).
Disagreement with the literature: none; the Lean form is the "unbounded reduced denominators" phrasing tailored to the caller.

### Generality analysis — `Roth.exists_reduced_approx`

Literature-standard form: approxSet α κ infinite iff the den-form rational set is infinite (irrational α, κ > 0).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason |
|---|---|---|---|---|---|
| 1 | `hα : Irrational α` | irrational | irrational (or α not equal to any solution value) | NO | for rational α = a/b and κ > 1 the conclusion fails (all large-q solutions are (ka, kb)) |
| 2 | `hκ : 0 < κ` | positive | κ > 0 (or ψ non-increasing, tending to 0) | not mechanically | the proof uses κ > 0 twice; the conclusion likely holds for κ ≤ 0 too (Dirichlet-type existence of reduced h/q with abs(α - h/q) < 1/(2q)), but that is a different proof, not a weakening; the only caller has κ > 2 |
| 3 | `q^{-κ}` bound | specific | any non-increasing ψ → 0 | yes (in principle) | not compiled; would require restating `approxSet` itself (class 5) |
| 4 | statement about `approxSet` | project def | generic set / `LiouvilleWith` | n/a | `approxSet` is NO-composable (parent report); an upstreamed statement must drop it |
| 5 | conclusion "∀ Q₀ ∃ reduced q > Q₀" | unbounded denominators | infinite set of rationals | equivalent | compiled: `rat_set_infinite_of_approxSet` derives the ℚ-form from this lemma; the converse is the den-bounded finiteness argument |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL for the project statement (no hypothesis can be dropped by a mechanical edit: `hα` is necessary, `hκ` is used essentially by the proof). A different, generic statement (dropping `approxSet`) is the mathlib-facing content; per false-positive class 5 that is a new lemma, not a weakening.
Number of weakening opportunities found: 0 mechanical; 1 restatement (compiled):
```lean
theorem approxSet_infinite_iff_rat {α κ : ℝ} (hα : Irrational α) (hκ : 0 < κ) :
    (approxSet α κ).Infinite ↔ {x : ℚ | |α - x| < 1 / (x.den : ℝ) ^ κ}.Infinite
```
(mathlib version would replace `approxSet` by the unreduced `∃ᶠ n in atTop, ∃ m, |α - m/n| < n^(-κ)` of `LiouvilleWith`).
Cost of restatement: CHEAP (compiled in the evidence file, about 25 lines incl. both directions).

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | hypotheses are propositions about one real number | — |
| 2 | sequences to filters? | yes | "∀ Q₀ ∃ q > Q₀" is `∃ᶠ q in atTop`; mathlib's `LiouvilleWith p x` is `∃ᶠ n : ℕ in atTop, ∃ m : ℤ, x ≠ m / n ∧ abs(x - m/n) < n^(-p)` | composes with `LiouvilleWith.frequently_lt_rpow_neg`, `Filter.Frequently` API |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to weaker typeclasses? | no | real setting intended | — |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | ℤ × ℕ pairs are the standard indexing | — |
| 8 | concrete-via-abstract? | yes (mild) | `approxSet` appears only to unfold membership; the content is the generic reduced/unreduced equivalence, compiled as `approxSet_infinite_iff_rat` | den-form lemmas such as `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` |
| 9 | false-generalisation guard | no false generalisation | the ℚ-form implies the project statement back (via finiteness of bounded-den rationals near α) and is implied by it (compiled forward direction) | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes, but as a different (generic) lemma.
  - Proposed mathlib-idiomatic restatement: for irrational x and p > 0, `(∃ᶠ n : ℕ in atTop, ∃ m : ℤ, abs(x - m/n) < n^(-p)) ↔ {r : ℚ | abs(x - r) < r.den^(-p)}.Infinite`.
  - Cost: CHEAP
  - Mathlib downstream this enables: it bridges `LiouvilleWith` (unreduced, filter form) and the den-form statements in DiophantineApproximation/Basic.lean (`Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`), and lets a future Thue–Siegel–Roth statement be phrased either way.
  - Real mathematical improvement: it names an equivalence every source uses silently; small but genuine.

### Proof strategy — `Roth.exists_reduced_approx`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | the fibre bound via `eventually_div_rpow_lt` could be phrased with `tendsto_rpow_neg_atTop`; no real gain | CHEAP |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | yes | `((h : ℚ) / q).den ≤ q` (see `approxSet_num_den_mem_aux` report) and a bounded-denominator finiteness lemma (see `approxSet_den_le_finite` report) | follow-up PRs, if approved |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (the `Set.Finite.of_finite_fibers` fibre argument is the natural proof; it mirrors the paper exactly).
  - Would refactoring make the proof strictly shorter / cleaner? no, beyond the helper lemmas already flagged in the sibling reports.

### Diamond / defeq risk

n/a: declaration kind is theorem.

### Mathlib search-status: `Roth.exists_reduced_approx`

[A] Lean-Finder       "irrational x, infinitely many fractions m/n with abs(x - m/n) < n^(-p) then infinitely many rationals q with abs(x - q) < q.den^(-p)"   hits: `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`, `..._iff_irrational`, `LiouvilleWith.frequently_lt_rpow_neg`, `Liouville.frequently_exists_num`, `LiouvilleWith.exists_pos`, `Liouville.liouvilleWith`; none converts unreduced to reduced
[B] Loogle            `Set.Infinite, Rat.den, abs(_ - _)`   hits: only the two κ = 2 Dirichlet lemmas in DiophantineApproximation/Basic.lean
[C] LeanSearch        "LiouvilleWith iff infinitely many rationals with denominator bound"   hits: `LiouvilleWith`, `Liouville`, `forall_liouvilleWith_iff`, `Liouville.frequently_exists_num`, `setOf_liouville_eq_iInter_iUnion`, `liouvilleWith_one`; no bridge
[D] Grep mathlib src  `exists_reduced`, `reduced_approx`, `namespace Roth`, `IsCoprime`/`Nat.Coprime`/`.reduced` in DiophantineApproximation/ and Transcendental/Liouville/, `Infinite.*den`   hits: only unrelated `exists_reduced_factors` (UFD), `exists_reduced_word` (Coxeter); building block `Set.Finite.of_finite_fibers` (Data/Set/Finite/Lattice.lean:234); `Rat.den_div_eq_of_coprime` (Data/Rat/Lemmas.lean:240)
[E] Name pattern      `exists_reduced_approx`, `approxSet_infinite_iff`, `liouvilleWith_iff_rat` (grep in place of `lean_local_search`): no hits

Searched for both:
  - the user's current form (reduced approximants with unbounded denominators)
  - the literature-standard form (unreduced-infinite iff rational-infinite)

Concluded: found building blocks (`Set.Finite.of_finite_fibers`, `Irrational.ne_rat`, `Rat.num_div_den`, `Rat.reduced`, `Rat.den_div_eq_of_coprime`); not in mathlib in either form.

### Normal-form check — `Roth.exists_reduced_approx`

Equivalent formalisms: (a) ∀ Q₀ ∃ reduced solution with q > Q₀ (current); (b) `{x : ℚ | abs(α - x) < 1/x.den^κ}.Infinite`; (c) `∃ᶠ q in atTop, ∃ h, IsCoprime h q ∧ ...`.
Does mathlib already have a canonical form for this idea? Partially: den-form (b) is the shape of `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`; unreduced filter form is `LiouvilleWith`.
If upstreamed, propose `unreduced ↔ (b)` with (b) on the RHS.
RHS convention respected? n/a for the project statement (not an iff).

### Syntactic generality — `Roth.exists_reduced_approx`

Alternative restatements attempted:
- current ∀ Q₀ ∃ form
- ℚ-set infinite (compiled, `rat_set_infinite_of_approxSet`)
- iff form (compiled, `approxSet_infinite_iff_rat`)
Chosen restatement: the current one for the project, since `exists_approximants` directly `choose`s a witness above each bound.
Justification: the caller needs witnesses above arbitrary thresholds, which (b) would only supply after an extra finiteness step.

### Superfluous-argument audit — `Roth.exists_reduced_approx`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hα` | yes | necessary (rational counterexample) |
| 2 | `hκ` | yes in the proof; possibly not for the conclusion | dropping it needs a Dirichlet-type proof, not compiled; irrelevant for the only caller (κ > 2) |
| 3 | `hinf` | yes | without it the conclusion fails for κ > 2 at non-Liouville points |
| 4 | `Q₀` | yes | threshold |

### Statement-shape verdict (Phase 5.5)

Normal form: OK for the project; for mathlib, REFACTOR into `unreduced ↔ den-form`
Syntactic generality: OK for the project
Superfluous arguments: NONE (to drop mechanically)

Overall: SHIP-AS-STATED (project); RESTATE-BEFORE-SHIP if anything goes upstream

### Call sites — `Roth.exists_reduced_approx`

Internal use count: 0 outside the declaring file; 1 in Main.lean
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:261 (`exists_approximants`) | `choose g hgmem hglt hgcop using fun Q₀ : ℕ ↦ exists_reduced_approx hα hκ hinf Q₀` |

Inline-derivation grep: (none). `Roth.roth_rat` (Main.lean:581) proves the easy converse direction (ℚ-set infinite ⇒ approxSet infinite) inline.

### Composition check (Phase 6)

Can `Roth.exists_reduced_approx` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Set.Finite.of_finite_fibers (fun hq => (hq.1 : ℚ) / hq.2) hV hfib` with `hV`, `hfib` supplied by mathlib.
  - Mathlib decls used: `Set.Finite.of_finite_fibers`
  - Result: partial; `hV` needs the reduction step and bounded-denominator finiteness, `hfib` needs irrationality plus the q^{-κ} → 0 bound. Neither is a mathlib lemma.
Attempt 2: route through a den-form infinite set (as `Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational` does for κ = 2).
  - Mathlib decls used: none applicable for general κ
  - Result: fails; mathlib has the den-form only for κ = 2 and only as a conclusion of Dirichlet, not as a conversion.

Conclusion: NOT-COMPOSABLE (21-line genuine argument)

### Verdict: `Roth.exists_reduced_approx`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): folklore equivalence of unreduced pairs, coprime pairs and rationals for irrational α, κ > 0; used silently in every definition of the irrationality exponent; clean.tex l.1578–1587 matches the proof.
- Generality analysis (Phase 4): MAXIMALLY GENERAL as a project statement (no mechanical weakening); the mathlib-facing content is a different generic lemma (compiled).
- Mathlib search (Phase 5): building blocks only; neither form exists.
- Composition check (Phase 6): NOT-COMPOSABLE.

**Rationale:**

As stated, the theorem cannot go to mathlib: it is phrased with `Roth.approxSet`, which the parent report classed NO-composable-from-mathlib (mathlib's notion is `LiouvilleWith`), and it is tailored to its single caller `exists_approximants`. Its real content is the folklore fact that, for irrational α and κ > 0, infinitely many unreduced approximations of quality κ yield infinitely many rationals r with |α − r| < den(r)^{−κ}. Mathlib states den-form results (`Real.infinite_rat_abs_sub_lt_one_div_den_sq_of_irrational`) and unreduced filter-form results (`LiouvilleWith`) but has no lemma converting between them; the compiled `approxSet_infinite_iff_rat` (evidence) is that conversion.

Whether such a bridge clears mathlib's bar is a judgment call: it is elementary, has no current in-mathlib consumer, and would mainly matter if Roth's theorem (or irrationality-exponent API) were upstreamed. Locally the lemma is well-shaped and should stay.

Numbered questions:
1. Should a generic bridge `(∃ᶠ n in atTop, ∃ m : ℤ, |x - m/n| < n^(-p)) ↔ {r : ℚ | |x - r| < r.den^(-p)}.Infinite` (irrational x, p > 0) be proposed for Mathlib/NumberTheory/DiophantineApproximation/Basic.lean (or next to LiouvilleWith)?
2. If yes, should it be bundled with the sibling helpers flagged in `Roth.approxSet_den_le_finite` (bounded-denominator finiteness) and `Roth.approxSet_num_den_mem_aux` (den of h/q is at most q) as one PR?
3. Is it worth dropping `hκ` (the conclusion plausibly holds for all κ via a Dirichlet-type argument), given that the only caller has κ > 2? Default: no.

Belongs-elsewhere check: the stated `approxSet` form stays project-local in Roth/Main.lean (paper §7, l.1578).
Call sites in our project (from Phase 6.0): 1 (Main.lean:261). No change needed in either outcome.
Next action: user answers Q1–Q3; default is KEEP as is.

---

## Next step

Keep `Roth.exists_reduced_approx` in Roth/Main.lean. If Q1 is yes, restate `approxSet_infinite_iff_rat` from `.mathlib-quality/overview/evidence/Roth.exists_reduced_approx/rat_form.lean` with LiouvilleWith-style unreduced fractions and open a mathlib PR to Mathlib/NumberTheory/DiophantineApproximation/Basic.lean.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.exists_reduced_approx/rat_form.lean` (imports `Roth.Main`): `rat_set_infinite_of_approxSet` (forward direction from `exists_reduced_approx`, using `Rat.den_div_eq_of_coprime`), `approxSet_infinite_of_rat_set` (converse, argument of `roth_rat`), and `approxSet_infinite_iff_rat`. Checked with `lean_diagnostic_messages`: no diagnostics.
- Searches: 3 WebSearch queries, Lean-Finder, LeanSearch, Loogle, grep over mathlib (`exists_reduced`, `reduced_approx`, `namespace Roth`, coprimality in DiophantineApproximation/ and Liouville/, `of_finite_fibers`, `den_div_eq_of_coprime`), project grep for call sites, grep of clean.tex (l.1578–1587). ChatGPT MCP was unavailable in this session.
