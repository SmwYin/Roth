---
decl: Roth.exists_delta
file: Roth/Main.lean
line: 227
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Eqs. (29), (30), (48)/(49) choice of delta in Roth's proof (given m > 16n^2 and the eq. (47) bound, pick 0 < delta < 1/m with (30) and m(1+4delta)/(gam - eta) < kappa); both hypotheses necessary (compiled converse), about project-only eta/gam, no literature standing outside this proof, no mathlib counterpart, and a 24-line continuity argument rather than a 3-call composition; recommended resolution keep project-local.
action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_parameters_aux at Roth/Main.lean:420); do not upstream; optionally restate together with Roth.exists_delta_bound as eventually-in-nhdsWithin-Ioi-0 bounds combined by filter_upwards and Filter.Eventually.exists_gt.
---

# Roth.exists_delta

## Inventory entry

### `theorem Roth.exists_delta`
- **Type**: `{n m : ℕ} (hm : 16 * n ^ 2 < m) {κ : ℝ} (h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ) : ∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧ (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ`
- **What**: the choice of `δ` in §7 of the source (clean.tex l.1588–1607): given `m > 16n²` and the eq. (47) bound `2m/(m − 4n√m) < κ`, there is `δ ∈ (0, 1/m)` satisfying (30) `η + 2(1+3δ)n√m < m/2` and (49) `m(1+4δ)/(γ − η) < κ`.
- **How**: `exists_delta_bound hm` gives `δ₀` handling (29)/(30) on `[0, δ₀]`; the map `δ ↦ m(1+4δ)/(γ(δ) − η(δ))` is `ContinuousAt` 0 (`ContinuousAt.div`, `Real.continuousAt_rpow_const`, denominator nonzero via `eta_lt_gam_iff` and `sub_pos`), its value at 0 equals `2m/(m − 4n√m)` (`simp` with `Real.zero_rpow`), so `ContinuousAt.eventually_lt` + `Metric.eventually_nhds_iff` give a radius `ε`; `exists_between (lt_min hδ₀ hε)` picks `δ`.
- **Hypotheses**: `hm : 16 * n ^ 2 < m` (eq. (47) side condition, feeds `exists_delta_bound`); `h47' : 2 * m / (m - 4 * n * √m) < κ` (eq. (47)). Both necessary (compiled converse).
- **Uses from project**: `Roth.exists_delta_bound`, `Roth.eta`, `Roth.gam`, `Roth.lam`, `Roth.eta_lt_gam_iff`
- **Used by**: private `Roth.exists_roth_parameters_aux` (Roth/Main.lean:420); module docstring Main.lean:29.
- **Visibility**: public
- **Lines**: 220–254 (docstring 220–226, statement 227–230), proof length 24 lines
- **Notes**: the explicit continuity proof (lines 232–241) could likely be shortened with `fun_prop`/`ContinuousAt.div` with a `by positivity`-style side goal; not pursued (not part of the assessment).

## Junk check (Step 8)
- Used anywhere? Yes, by `Roth.exists_roth_parameters_aux` (Main.lean:420), the parameter-choice step of the final proof.
- Wrapper of 1–2 mathlib calls? No; 24-line continuity argument stacked on `exists_delta_bound`.
- Does mathlib have it? No (Phase 5); it is about the project-only `eta`/`gam`.
- Too specific (inline?)? Single caller, but it is a named step of the source (eqs. (48)/(49)) and inlining would bloat the already long `exists_roth_parameters_aux`; keep.
- Well-chosen? Yes; mirrors the source's "decreasing δ further if necessary" step, and pairs with `Roth.exists_m`.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "Given"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Roth` + `exists_delta`: no hit. Not a glue lemma (real proof), so a full run follows. Parents: `Roth.eta`, `Roth.gam` (project defs, not NO-mathlib-has-it), sibling `Roth.exists_delta_bound` and `Roth.exists_m` are BORDERLINE-needs-human.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates clean)
- decl `Roth.exists_delta`: resolved at Roth/Main.lean:227
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §7 of the source: assembling Roth's theorem (choice of parameters m, δ, approximants, degrees, and the final contradiction)

### Statement (Phase 1)

`Roth.exists_delta` is a theorem stating the following:

Let `n, m` be natural numbers with `m > 16 n²` and let `κ` be real with `2m/(m − 4n√m) < κ`. Put `λ = 4(1+3δ)n√m`, `γ = (m − λ)/2`, `η = 10^m δ^{2^{-m}}`. Then there is `δ` with `0 < δ < 1/m`, `η + 2(1+3δ)n√m < m/2` (equivalently `η < γ`), and `m(1+4δ)/(γ − η) < κ`.

Variables / typeclasses involved (Lean side):
- `n : ℕ`: degree of the algebraic number.
- `m : ℕ`: number of variables.
- `κ : ℝ`: approximation exponent.

Hypotheses (Lean side):
- `hm : 16 * n ^ 2 < m`: makes `γ(0) − η(0) = (m − 4n√m)/2 > 0` and gives (29)/(30) via `exists_delta_bound`.
- `h47' : 2 * m / (m - 4 * n * √(m : ℝ)) < κ`: the value at `δ = 0` of the (49) LHS is below `κ`.

Conclusion (math): a single `δ` satisfying (29), (30) and (49).

Conclusion (Lean): `∃ δ : ℝ, 0 < δ ∧ δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ∧ (m : ℝ) * (1 + 4 * δ) / (gam δ n m - eta δ m) < κ`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: parameter-choice auxiliary of Roth's proof, not a theorem with independent standing.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 24 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem proof choose delta small 2m(1+4delta)/(m - 4(1+3delta) n sqrt m - 2 eta) < kappa | no | n/a | hits arXiv math/0307203 (quantitative Roth-Ridout, own δ choice), Evertse Luminy notes, minru roth.pdf; none states this inequality |
| 2 | WebSearch (aliases / book) | Cassels Diophantine approximation Roth theorem parameters m delta gamma - eta choice of epsilon | no | n/a | Cassels Ch. VI not indexed; arXiv 1306.2976, 2005.06531, 2601.11376 use their own parameters |
| 3 | WebSearch (general form) | continuous function strict inequality at zero holds for all small positive parameter existence lemma real analysis | partial | local sign preservation of continuous functions | textbook real analysis; in mathlib as `ContinuousAt.eventually_lt` |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | clean.tex eqs. roth:eq47–roth:eq49 | yes | l.1588–1607: choose `m` with (47), then δ small with (30), (29) via fixed-m Lemma m-δ, then "Decreasing δ further if necessary" (48), equivalent to (49) | exact match with the Lean statement |
| 6 | nLab | Roth's theorem / parameter choice | no | n/a | nLab has no entry on proofs of Roth's theorem |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real-number inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread on this parameter choice |
| 10 | recent arXiv | math/0307203, 2005.06531, 2601.11376 | no | n/a | each Roth-type proof makes its own ad hoc δ choice |

### Literature summary (Phase 3)

Concept identified as: the choice of `δ` in the Cassels-style proof of Roth's theorem; no named concept.
Sources agree on the standard form: no — constants are proof-specific; the only general content is local sign preservation of continuous functions.
Most general standard form: `ContinuousAt.eventually_lt` (already in mathlib), combined with `Filter.Eventually.and`.
Generality dimensions where the literature varies:
  - constants and shape of the inequalities: proof-specific.
Disagreement with the literature: none; matches source eqs. (29), (30), (48), (49).

### Generality analysis — `Roth.exists_delta`

Literature-standard form (from Phase 3): source §7 δ-choice; general principle `ContinuousAt.eventually_lt`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hm : 16 * n ^ 2 < m` | strict bound | `m > 4n m^{1/2}` | NO | necessary: the conclusion implies it (compiled, evidence) |
| 2 | `h47'` | eq. (47) | eq. (47) | NO | necessary: the conclusion implies it, since `m(1+4δ)/(γ−η) ≥ 2m/(m − 4n√m)` (compiled, evidence) |
| 3 | `n m : ℕ` | naturals | integers | no | counts |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (necessity of both hypotheses verified by a compiled converse)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | concrete reals | — |
| 2 | Sequences/metric vs filters? | yes (cosmetic, local) | prove `∀ᶠ δ in 𝓝[>] 0, …` for the four conjuncts and extract `δ` with `Filter.Eventually.exists_gt`-style lemmas | none in mathlib |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | rpow and sqrt need ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `m, n` are counts | — |
| 8 | Concrete-via-abstract? | no | proof uses `eta`/`gam` explicitly (continuity, value at 0); abstract content is `ContinuousAt.eventually_lt`, already in mathlib | — |
| 9 | False-generalisation guard | no false generalisation | the filter form is equivalent | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for mathlib)
  - One-line reason: the statement is about project-only `eta`/`gam`; the filter rephrasing is a local tidy (removes `Metric.eventually_nhds_iff` and the `min` bookkeeping), not a mathlib contribution.

### Proof strategy — `Roth.exists_delta`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | radius extraction via `Metric.eventually_nhds_iff` + `exists_between (lt_min …)`; could be `filter_upwards` on `𝓝[>] 0` | CHEAP |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `ContinuousAt.eventually_lt`, `Real.continuousAt_rpow_const`, `Real.zero_rpow` all exist; continuity block may be shortened by `fun_prop` | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (continuity + eventually; the radius extraction is forced by the ∃δ statement and the ∃δ₀ shape of `exists_delta_bound`)

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.exists_delta`

[A] Lean-Finder       "if f is continuous at 0 and f 0 < c then there exists positive delta with f δ < c for small δ"   hits: `ContinuousAt.eventually_lt`, `Metric.continuousAt_iff` — building blocks only
[B] Loogle            `(∀ᶠ x in nhdsWithin ?a (Set.Ioi ?a), ?p x) → ∃ x, ?a < x ∧ ?p x`   no hits for this exact shape
[C] LeanSearch        "exists positive x arbitrarily small satisfying an eventually property in nhdsWithin Ioi 0"   hits: `eventually_nhdsWithin_iff`, `Filter.Eventually.exists_lt` (Mathlib.Topology.Order.LeftRight) — generic building blocks
[D] Grep mathlib src  `Roth` + `exists_delta` under `.lake/packages/mathlib/Mathlib/`   no hit
[E] Name pattern      `exists_delta` in namespace Roth; only the project decl (lean_local_search not needed beyond [D])

Searched for both:
  - the user's current form (δ-choice with `eta`, `gam`)
  - the literature-standard / general form (`ContinuousAt.eventually_lt`)

Concluded: found building blocks (`ContinuousAt.eventually_lt`, `ContinuousAt.div`, `Real.continuousAt_rpow_const`, `Real.zero_rpow`, `Metric.eventually_nhds_iff`, `exists_between`); not in mathlib as a statement (project-specific).

### Normal-form check — `Roth.exists_delta`

Equivalent formalisms: `∃ δ, 0 < δ ∧ …` (current); `∀ᶠ δ in 𝓝[>] 0, …` (stronger, implies current); (30) stated as `eta < gam` via `eta_lt_gam_iff`.
Does mathlib already have a canonical form for this idea? yes: eventual statements in `𝓝[>] 0`.
Proposed canonical form: local only; current form is what the single caller consumes.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_delta`

Alternative restatements attempted:
- current single-δ existential
- `∀ᶠ δ : ℝ in 𝓝[>] 0, …` (not compiled; optional local refactor)
- (30) as `eta δ m < gam δ n m` (equivalent by `eta_lt_gam_iff`)

Chosen restatement: current.
Justification: the caller `exists_roth_parameters_aux` destructures exactly these four facts and re-exports them in the same shape.

### Superfluous-argument audit — `Roth.exists_delta`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hm` | yes | necessary (compiled converse) |
| 2 | `h47'` | yes | necessary (compiled converse) |
| 3 | `n`, `m`, `κ` | yes | in the conclusion |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.exists_delta`

Internal use count: 1 (in the declaring file; no other files)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:420 | `obtain ⟨δ, hδ0, hδm, h30, h49⟩ := exists_delta hm h47'` (in private `Roth.exists_roth_parameters_aux`) |

Inline-derivation grep: (none) — no other site re-derives (48)/(49).

### Composition check (Phase 6)

Can `Roth.exists_delta` be derived from mathlib in ≤3 chained calls?

Attempt 1: `(hc.eventually_lt continuousAt_const h0).and (exists_delta_bound …)` then extract a positive point
  - Mathlib decls used: `ContinuousAt.eventually_lt`, `Metric.eventually_nhds_iff`, `exists_between`, `Real.continuousAt_rpow_const`, `Real.zero_rpow`
  - Result: partial — still needs the continuity proof of `δ ↦ m(1+4δ)/(γ−η)`, the nonvanishing denominator at 0 (via `eta_lt_gam_iff`), the evaluation at 0 matching `h47'`, and `exists_delta_bound` for (29)/(30)
  - Notes: a real proof, not a call chain

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_delta`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the source's §7 (clean.tex l.1588–1607); every Roth-type proof makes its own parameter choice; general content is `ContinuousAt.eventually_lt`.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (both hypotheses necessary, compiled converse).
- Mathlib search (Phase 5): building blocks only; no counterpart.
- Composition check (Phase 6): NOT-COMPOSABLE (24-line argument).

**Rationale:**

The statement is a bookkeeping step of one proof of Roth's theorem, phrased in terms of the project-only `Roth.eta` and `Roth.gam`. It has no standing outside that proof, so no YES bucket fits; its abstract content (a function continuous at 0 and below `κ` there stays below `κ` nearby) is already `ContinuousAt.eventually_lt`. But it is not a ≤3-call composition: continuity of the (49) LHS, its value at 0, nonvanishing of the denominator, and combination with `exists_delta_bound` take a genuine 24-line proof. So NO-composable does not apply by the gate. Same situation and same recommended resolution as its siblings `Roth.exists_m` and `Roth.exists_delta_bound` (both BORDERLINE, keep project-local).

Belongs-elsewhere check: belongs in the Roth project (Roth/Main.lean, next to `exists_m`), as the source's eqs. (48)/(49) step.

Numbered questions:
1. Do you agree to keep `Roth.exists_delta` project-local and never upstream it (recommended: yes)?
2. Should it and `Roth.exists_delta_bound` be refactored to eventual statements in `𝓝[>] 0` combined by `filter_upwards`, dropping the `min`/radius bookkeeping (recommended: optional, local tidy only)?
3. Given its single caller (private `exists_roth_parameters_aux`), should it stay public for blueprint correspondence with eqs. (48)/(49) (recommended: yes)?

Next action: user answers; default is keep as is in Roth/Main.lean.

### Next step

Keep `Roth.exists_delta` project-local in Roth/Main.lean (single caller `Roth.exists_roth_parameters_aux`, Roth/Main.lean:420); do not upstream.

## Evidence
- WebSearch ×3 (queries in the literature table): no source beyond the project paper states this parameter choice.
- Local reference clean.tex l.1588–1607 (eqs. (47)–(49) and the "Decreasing δ further" sentence).
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5; grep of `.lake/packages/mathlib/Mathlib/` (no `Roth` hit).
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_delta/experiments.lean` (imports Roth.MainLemma), checked with `lean_diagnostic_messages`: clean, no errors or warnings. Contains `Roth.exists_delta_converse`: the conclusion of `exists_delta` implies both `16 * n ^ 2 < m` and `2 * m / (m - 4 * n * √m) < κ` (necessity of both hypotheses).
