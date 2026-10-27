---
decl: Roth.Θ_option_le
file: Roth/Theta.lean
line: 593
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The named Lemma 6 of the Roth development (Θ_p(B; q; r) ≤ 2 max over 1 ≤ l ≤ r_p+1 of Φ + √Φ + √δ), a 4-line sup-taking wrapper of the project lemmas Θ_le_of_forall_index_le and index_le_lem6 about project-only notions (Θ, lem6Φ, lem6M); mathlib has none of this and the literature states only the final Roth lemma standalone, so it is project-local; two hypotheses (hq, hB) are superfluous (compiled).
action: Keep in Roth/Theta.lean (single caller Roth/Theta.lean:920 in Lemma 7); optionally drop hq (together with index_le_lem6's _hq) and hB per evidence/Roth.Θ_option_le/weaken_hq.lean and remove the two corresponding arguments at Theta.lean:920; do not upstream.
---

# Roth.Θ_option_le

## Inventory entry

### `theorem Roth.Θ_option_le`
- **Type**: `{τ : Type*} [Fintype τ] {δ : ℝ} (hδ0 : 0 ≤ δ) (hδ1 : δ ≤ 1) {r : Option τ → ℕ} (hrp : 3 ≤ (r none : ℝ)) (hratio : ∀ j, (r none : ℝ) ≤ δ * r (some j)) {r₁ : ℕ} (hr₁ : ∀ j, r j ≤ r₁) {q : Option τ → ℕ} (hq : ∀ j, 0 < q j) {B : ℝ} (hB : 1 ≤ B) : Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' _ (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l + √(lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l) + √δ)`
- **What**: Lemma 6 of the source (clean.tex §5, Lemma `roth:lem6`, l.704–725): `Θ_p(B; q; r) ≤ 2 max_{1 ≤ l ≤ r_p+1} (Φ + Φ^{1/2} + δ^{1/2})` with `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q'; l r')`, `M = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`; the last variable is `none : Option τ`.
- **How**: `Roth.Θ_le_of_forall_index_le` reduces to a per-polynomial bound; `Roth.index_le_lem6` gives an `l ∈ [1, r_p+1]` with the index bounded by `2 f(l)`; conclude with `mul_le_mul_of_nonneg_left` and `Finset.le_sup'`.
- **Hypotheses**: `hδ0`, `hδ1`, `hrp`, `hratio`, `hr₁` (passed to `index_le_lem6`); `hq` (passed to `index_le_lem6`'s unused `_hq`, hence superfluous); `hB` (only for `indexSet_nonempty` inside `Θ_le_of_forall_index_le`; superfluous, see evidence (4)).
- **Uses from project**: `Roth.Θ` (Theta.lean:68), `Roth.lem6Φ` (Theta.lean:275), `Roth.lem6M` (Theta.lean:270), `Roth.Θ_le_of_forall_index_le` (Theta.lean:124), `Roth.index_le_lem6` (Theta.lean:556)
- **Used by**: `Roth/Theta.lean:920` (inductive step of Lemma 7, `refine (Θ_option_le (τ := Fin (n + 1)) hδ0.le hδ1.le ...).trans_lt ?_`); also named in the module docstring (Theta.lean:36). No other occurrence in `Roth/` or `Roth.lean`.
- **Visibility**: public
- **Lines**: 589–601 (docstring 589–592, statement 593–597, proof 598–601), proof length 4 lines
- **Notes**: preceded by `omit [DecidableEq τ] in`. Named source lemma (Lemma 6), listed in the module docstring's main results.

## Junk check (Step 8)
- Used anywhere? Yes, once: the Lemma 7 inductive step (Theta.lean:920), on the main path to Roth's theorem.
- Wrapper of 1–2 mathlib calls? No: it is a wrapper of two *project* lemmas (`Θ_le_of_forall_index_le`, `index_le_lem6`) plus `Finset.le_sup'`.
- Does mathlib have it? No (Phase 5).
- Too specific (inline?)? It is the named source Lemma 6 with a source docstring; inlining into Lemma 7 would lose the correspondence to the paper. Keep.
- Well-chosen? Yes; minor: `hq` and `hB` are superfluous (compiled in evidence).
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "**Lemma 6**"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Θ_option_le`, `lem6Φ`, `namespace Roth`: no hit. Not a glue lemma (`rfl`/unfolding): it composes two lemmas and takes a `sup'`, so the full workflow follows. Parents (`Roth.Θ`, `Roth.lem6Φ`: NO-composable-from-mathlib; `Roth.index_le_lem6`: BORDERLINE) are not NO-mathlib-has-it, so no re-aim.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; evidence file importing `Roth.Theta` compiles, exit 0)
- decl `Roth.Θ_option_le`:   resolved at Roth/Theta.lean:593
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  the index across sets of polynomials `Θ_m(B; q; r)` and Lemmas 5, 6, 7 of the source

### Statement (Phase 1)

`Roth.Θ_option_le` is a theorem stating the following:

Let `0 ≤ δ ≤ 1` and let `r_1, …, r_p` be weights with `r_p ≥ 3`, `r_p ≤ δ r_j` for `j < p`, and `r_j ≤ r₁` for all `j`; let `q_1, …, q_p` be positive integers and `B ≥ 1`. Then `Θ_p(B; q; r) ≤ 2 max_{1 ≤ l ≤ r_p+1} (Φ_l + Φ_l^{1/2} + δ^{1/2})`, where `Φ_l = Θ_1(M_l; q_p; l r_p) + Θ_{p-1}(M_l; q_1..q_{p-1}; l r_1..l r_{p-1})` and `M_l = (r₁+1)^{pl} l! B^l 2^{p r₁ l}`. Here `Θ_m(B; q; r)` is the supremum of the weighted index `ind(R; h/q; r)` over nonzero integer polynomials `R` with `deg_{x_j} R ≤ r_j`, coefficients bounded by `B`, and `h_j` coprime to `q_j`.

Variables / typeclasses involved (Lean side):
- `τ` with `[Fintype τ]`: the first `p−1` variables; `Option τ` indexes all `p`, `none = x_p`.
- `δ`, `r`, `r₁`: small parameter, weights, uniform weight bound; `q`: denominators; `B`: coefficient bound.

Hypotheses (Lean side):
- `hδ0`, `hδ1`: `0 ≤ δ ≤ 1`. `hrp`: `r_p ≥ 3`. `hratio`: `r_p ≤ δ r_j`. `hr₁`: `r_j ≤ r₁`.
- `hq`: `q_j > 0` (superfluous). `hB`: `B ≥ 1` (superfluous).

Conclusion (math): `Θ_p(B; q; r) ≤ 2 max_{l ∈ [1, r_p+1]} (Φ_l + √Φ_l + √δ)`.

Conclusion (Lean): `Θ B q r ≤ 2 * (Finset.Icc 1 (r none + 1)).sup' _ (fun l ↦ lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l + √(lem6Φ …) + √δ)`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: an intermediate named lemma (Lemma 6) of the source's proof of Roth's theorem, stated in project-specific quantities; not a structure, not a person-named theorem, not the project's main result (it is listed among the file's results, but only as a step towards Lemma 7 and Roth's theorem).

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 4 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof Cassels "Lemma 6" Theta index polynomials maximum over l generalized Wronskian | partial | Roth's lemma proved via generalised Wronskians (Davenport–Roth 1955, Cassels Ch. VI) | lemma numbering / Θ-recursion not surfaced; arXiv 2502.00731, 1305.0926, 1611.00248 |
| 2 | WebSearch (general form) | supremum of index of polynomials bounded height rational point weights inductive bound Roth lemma Ridout | yes (for the definition of Θ) | Ridout/Yamada: Θ as the sup of the index over integer polynomials with coefficients ≤ B and degrees ≤ r_j at rational points; the inductive bound controls this sup | arXiv math/0307203 (Yamada, quantitative Roth–Ridout); exact recursive constants not standardised |
| 3 | WebSearch (aliases) | "Roth's lemma" induction step number of variables index bound statement | yes (final lemma only) | Roth's lemma `ind ≤ 2mη` (2502.00731 Lemma 3.9), proved by induction on m | the inductive step is proved inline in every source found; no standalone statement |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | read `.mathlib-quality/references/clean.tex` l.700–725 (Lemma `roth:lem6`) and l.969, l.1021 (its use in Lemma 7) | yes | eq. (13), (15), (16): exactly the Lean statement | Lean hypotheses are weaker: `r_p ≥ 3` vs `r_p > 10/δ`; `r_p ≤ δ r_j` vs `r_{j-1}/r_j > 1/δ`; closed `0 ≤ δ ≤ 1`; `p ≥ 1` allowed (τ may be empty) |
| 6 | nLab | index of a polynomial; Roth's theorem | no | n/a | no entry on Roth's index or Roth's lemma |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | Diophantine estimate, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread isolating the Θ-recursion |
| 10 | recent arXiv | 2502.00731, math/0307203, 1806.10737 | partial | as #2, #3 | inductive step of Roth's lemma proved inline |

### Literature summary (Phase 3)

Concept identified as: the inductive step of Roth's lemma in Cassels/Ridout form ("Lemma 6"), as a recursive bound on the supremum Θ of indices.
Sources agree on the standard form: only for the final Roth lemma (index of a small-height polynomial at a high-height point is small); the Θ-recursion with these constants is specific to the Cassels-style presentation followed by the source.
Most general standard form: Roth's lemma itself (`ind(P; ξ; r) ≤ 2mη` under rapidly decreasing weights), proved by induction through the generalised Wronskian.
Generality dimensions where the literature varies:
  - point: rational (here) vs algebraic (Bombieri–Gubler, 2502.00731).
  - height normalisation and constants: source-specific.
Disagreement with the literature: none; the Lean hypotheses are weaker than the source's.

### Generality analysis — `Roth.Θ_option_le`

Literature-standard form: clean.tex Lemma 6 (eq. (13)).

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hq : ∀ j, 0 < q j` | positive denominators | positive integers `q_j` | yes | only fed to `index_le_lem6`'s unused `_hq`; dropped and compiled in evidence (2) |
| 2 | `hB : 1 ≤ B` | `B ≥ 1` | implicit (Θ well defined) | yes | only used for nonemptiness in `Θ_le_of_forall_index_le`; with `Real.sSup_le` the RHS just has to be ≥ 0; compiled in evidence (4) |
| 3 | `hrp : 3 ≤ r none` | `r_p ≥ 3` | `r_p > 10/δ` | already weaker | needed by `index_numeric_bound_aux` |
| 4 | `hratio` | `r_p ≤ δ r_j` | `r_{j-1}/r_j > 1/δ` | already weaker | used for weight-≤-δ bound and positivity of weights |
| 5 | `hδ0`, `hδ1` | `0 ≤ δ ≤ 1` | `0 < δ < 1` | already weaker | needed (`√δ ≥ δ`, positivity) |
| 6 | `hr₁` | `r_j ≤ r₁` | `r_1 > … > r_p` (r₁ = max) | already weaker | uniform bound for Lemma 3 |
| 7 | rational points over ℤ | fixed | algebraic points | no (here) | Θ is defined over rational points; changing it redesigns the development |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (up to the cosmetic removal of two superfluous hypotheses, both verified in evidence)
Number of weakening opportunities found: 2 (verified: `lake env lean .mathlib-quality/overview/evidence/Roth.Θ_option_le/weaken_hq.lean` exits 0 with no messages)
Proposed restatement: drop `hq` (requires dropping `_hq` from `Roth.index_le_lem6` too) and `hB`; replace `Θ_le_of_forall_index_le hB` by `Real.sSup_le` plus a nonnegativity side goal (evidence (4)); update the call site Theta.lean:920 by removing the arguments `(fun j ↦ Nat.zero_lt_of_lt (hq _))` and `(Real.one_le_rpow …)`.
Cost of restatement: CHEAP.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | numeric hypotheses on data | — |
| 2 | Sequences vs filters? | no | finite real inequality | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled substructure? | no | `RSet` is a set of bounded polynomials | — |
| 5 | Field-specific vs typeclass-weakened? | no | integrality essential | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `Option τ` split (last variable vs rest) is the induction structure | — |
| 8 | Concrete-via-abstract? | no | proof body is `Θ_le_of_forall_index_le` + `index_le_lem6` + `le_sup'`; the general part (a sup bound from pointwise bounds) is already the separate lemma `Θ_le_of_forall_index_le` / mathlib `csSup_le` | — |
| 9 | False-generalisation guard | no false generalisation | no widening proposed beyond dropping unused hypotheses | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - Reason: a paper-specific inequality with paper-specific constants about project definitions; its reusable abstraction (sup bounded by pointwise bounds) is already factored out.

### Proof strategy — `Roth.Θ_option_le`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the sup-taking step uses mathlib's `Finset.le_sup'`, `csSup_le` (via the project wrapper) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (pointwise bound, then sup; if `hB` is dropped, `Real.sSup_le` replaces `Θ_le_of_forall_index_le`, evidence (4))

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_option_le`

[A] Lean-Finder       "upper bound for the supremum of the index of integer polynomials with bounded coefficients at rational points (Roth's lemma)"   hits: `ChevalleyThm.MvPolynomialC.numBound`, `ChevalleyThm.degBound`, `one_le_pow_mul_abs_eval_div` — unrelated
[B] Loogle            `"sSup", MvPolynomial, Finset.sup'`   no hits (query rejected `sSup` as identifier; suggestions combining `SupSet.sSup`, `MvPolynomial`, `Finset.sup'` give nothing relevant)
[C] LeanSearch        "Roth lemma: index of polynomial with small coefficients at rational point bounded by maximum over l"   hits: `one_le_pow_mul_abs_eval_div`, `MvPolynomial.schwartz_zippel_sup_sum`, `Behrend.roth_lower_bound` (unrelated Roth number) — no match
[D] Grep mathlib src  `Θ_option_le`, `lem6Φ`, `namespace Roth`   no hits
[E] Name pattern      `Roth.Θ_option_le`   only the project declaration

Searched for both:
  - the user's current form (Θ-recursion, Lemma 6)
  - the literature-standard form (Roth's lemma / index bound for small-height polynomials)

Concluded: not in mathlib (all 5 methods exhausted, plus the literature-standard form).

### Normal-form check — `Roth.Θ_option_le`

Equivalent formalisms: (a) `Θ ≤ 2 * Finset.sup' …` (current); (b) `∀ R ∈ RSet, ∀ h coprime, index ≤ 2 max_l …`; (c) `Θ ≤ 2 * ⨆ l ∈ Icc 1 (r_p+1), …`.
Does mathlib already have a canonical form? no.
Proposed canonical form: current (`Finset.sup'` over the finite range matches the source's `max_l`, and the caller consumes it with `Finset.sup'_lt_iff`).
RHS convention respected? yes (upper bound with `Θ` on the LHS).

### Syntactic generality — `Roth.Θ_option_le`

Alternative restatements attempted:
- current (with `hq`, `hB`)
- without `hq` (evidence (2), compiles; original recovered in one line, evidence (3))
- without `hq` and `hB` (evidence (4), compiles)
- `⨆`-form: rejected; `Finset.sup'` gives `Finset.sup'_lt_iff`, which the caller uses.

Chosen restatement: drop `hq` and `hB` (otherwise current).
Justification: the caller at Theta.lean:920 then supplies two fewer arguments, one of which (`Real.one_le_rpow …`) is a non-trivial side proof.

### Superfluous-argument audit — `Roth.Θ_option_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype τ]` | yes | `Θ`, `Fintype.card τ` |
| 2 | `[DecidableEq τ]` | no | already omitted |
| 3 | `hq` | no | evidence (2) |
| 4 | `hB` | no | evidence (4): for `B < 1`, `RSet B r = ∅` and `Θ = sSup ∅ = 0 ≤` RHS |
| 5 | `hδ0`, `hδ1`, `hrp`, `hratio`, `hr₁` | yes | needed by `index_le_lem6` |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: 2 to drop (`hq`, `hB`)

Overall: RESTATE-BEFORE-SHIP (locally: drop `hq`, `hB`)

### Call sites — `Roth.Θ_option_le`

Internal use count: 0 outside the declaring file; 1 inside it
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:920 | `refine (Θ_option_le (τ := Fin (n + 1)) hδ0.le hδ1.le (r := r ∘ e.symm) … (fun j ↦ Nat.zero_lt_of_lt (hq _)) (Real.one_le_rpow …)).trans_lt ?_` (inductive step of Lemma 7) |

Inline-derivation grep:
  - (none) — no other site re-derives the Lemma 6 bound on `Θ`.

### Composition check (Phase 6)

Can `Roth.Θ_option_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Θ_le_of_forall_index_le hB fun R hR h hh ↦ (index_le_lem6 …).elim … Finset.le_sup'`.
  - Decls used: `Roth.Θ_le_of_forall_index_le`, `Roth.index_le_lem6` (project), `Finset.le_sup'`, `mul_le_mul_of_nonneg_left` (mathlib).
  - Result: succeeds as a ≤3-call composition, but of *project* lemmas; the content lies in `index_le_lem6` (BORDERLINE, itself NOT-COMPOSABLE).
Attempt 2: mathlib-only.
  - Result: fails; mathlib has no Roth index, Θ, generalised Wronskian or Roth lemma.

Conclusion: NOT-COMPOSABLE (from mathlib)

### Verdict: `Roth.Θ_option_le`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): exactly Lemma 6 of the source (clean.tex l.704–725), the inductive step of Roth's lemma in Cassels/Ridout form; the literature states only the final Roth lemma standalone.
- Generality analysis (Phase 4): MAXIMALLY GENERAL up to two superfluous hypotheses (`hq`, `hB`), both verified in evidence.
- Mathlib search (Phase 5): not in mathlib.
- Composition check (Phase 6): NOT-COMPOSABLE from mathlib (a short composition of project lemmas only).

**Rationale:**

The theorem is the source's named Lemma 6, a paper-specific recursion with paper-specific constants (`lem6M`, `lem6Φ`) about the project's own `Θ`, obtained in four lines from `Θ_le_of_forall_index_le` and the per-point `index_le_lem6`. No YES bucket fits: it has no standalone literature standing outside this proof scheme and fills no mathlib gap on its own (mathlib would first need the Roth index, Θ, Hasse-derivative Wronskians and Lemma 2, all BORDERLINE or NO in their own reports). No NO bucket fits: mathlib does not have it, and it is not a mathlib composition. As with its siblings `Roth.index_le_lem6`, `Roth.index_det_le` and `Roth.exists_det_eq_mul`, the verdict is BORDERLINE with a clear recommendation to keep it project-local. Its value is as the named source lemma consumed by Lemma 7.

Locally, `hq` and `hB` can be dropped at no cost (evidence (2) and (4)); dropping `hq` requires dropping `index_le_lem6`'s `_hq` as well, which that report also proposes.

Numbered questions:
1. Keep `Roth.Θ_option_le` project-local in Roth/Theta.lean (recommended: yes)?
2. Drop the superfluous `hq` (together with `index_le_lem6`'s `_hq`) and remove the argument at Theta.lean:920? The source's "positive integers `q_j`" argues for keeping it; default no.
3. Drop the superfluous `hB`, switching the proof to `Real.sSup_le` (evidence (4)) and removing the `Real.one_le_rpow …` argument at Theta.lean:920? Yes or no.

Next action: user answers the questions; default is to keep the theorem as is in Roth/Theta.lean.

### Next step

Keep `Roth.Θ_option_le` in Roth/Theta.lean (caller: Lemma 7 inductive step, Theta.lean:920). Do not upstream. Optionally apply the two hypothesis drops from evidence/Roth.Θ_option_le/weaken_hq.lean.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.Θ_option_le/weaken_hq.lean` (imports `Roth.Theta` and `Batteries.Tactic.OpenPrivate`; `lake env lean` exit 0, no messages, ~42 s):
  - (1) `Roth.index_le_lem6_no_hq`: per-point Lemma 6 without `_hq` (proof copied from evidence/Roth.index_le_lem6).
  - (2) `Roth.Θ_option_le_no_hq`: the statement without `hq`, proof verbatim except calling (1); compiles.
  - (3) an `example` recovering the original statement (with `hq`) from (2) in one line.
  - (4) `Roth.Θ_option_le_no_hq_no_hB`: also without `hB`, via `Real.sSup_le` and nonnegativity of the RHS (`Θ_nonneg`, `Real.sqrt_nonneg`, `Finset.le_sup'` at `l = 1`); compiles.
- WebSearch ×3 (queries in the table); local read of `.mathlib-quality/references/clean.tex` l.700–725; Lean-Finder, Loogle, LeanSearch and mathlib grep as recorded in Phase 5.
- ChatGPT channel n/a: the `ask_chatgpt_math` MCP is not configured in this session.
- Sources: https://arxiv.org/pdf/2502.00731, https://arxiv.org/pdf/math/0307203, https://arxiv.org/pdf/1305.0926, https://arxiv.org/pdf/1611.00248, https://arxiv.org/pdf/1806.10737, https://www.cambridge.org/core/journals/mathematika/article/rational-approximations-to-algebraic-numbers/EFB89E2873019B246F004FAA06E05A7F.
