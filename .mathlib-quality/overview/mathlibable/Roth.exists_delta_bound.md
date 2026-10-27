---
decl: Roth.exists_delta_bound
file: Roth/MainLemma.lean
line: 77
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Lemma m-delta of the source (fixed m > 16n^2 gives delta0 > 0 with (29) delta < 1/m and (30) eta + 2(1+3delta)n sqrt m < m/2 for all 0 <= delta <= delta0); a parameter-choice step of Roth's proof about the project-only eta, hypothesis necessary (compiled converse), no literature standing outside Roth proofs, no mathlib counterpart, and a 12-line continuity argument rather than a 3-call composition; recommended resolution is keep project-local.
action: Keep in Roth/MainLemma.lean (single caller Roth.exists_delta at Roth/Main.lean:231); do not upstream; optional local restatement as an eventually-in-nhdsWithin-Ici-0 statement (compiled in evidence) if exists_delta is refactored to filters.
---

# Roth.exists_delta_bound

## Inventory entry

### `theorem Roth.exists_delta_bound`
- **Type**: `{n m : ℕ} (hm : 16 * n ^ 2 < m) : ∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 ≤ δ → δ ≤ δ₀ → δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2`
- **What**: Lemma `m-δ` of §6 of the source (clean.tex l.1211–1248), fixed-`m` form: for `m > 16 n²` there is `δ₀ > 0` such that every `δ ∈ [0, δ₀]` satisfies (29) `δ < 1/m` and (30) `10^m δ^{(1/2)^m} + 2(1+3δ) n √m < m/2`.
- **How**: from `hm`, `4n < √m` (`Real.lt_sqrt_of_sq_lt`), hence the gap `2n√m < m/2` (`nlinarith` with `Real.sq_sqrt`); the LHS of (30) is `ContinuousAt` 0 (`Real.continuousAt_rpow_const` plus `fun_prop`) and equals `2n√m` at `δ = 0` (`Real.zero_rpow`); `ContinuousAt.eventually_lt` and `Metric.eventually_nhds_iff` give a radius `ε`; take `δ₀ = min (1/m) ε / 2` (`half_lt_self`, `lt_min_iff`).
- **Hypotheses**: `hm : 16 * n ^ 2 < m` (necessary: the conclusion at `δ = 0` is equivalent to it, compiled in evidence).
- **Uses from project**: `Roth.eta`
- **Used by**: `Roth.exists_delta` (Roth/Main.lean:231); module docstring MainLemma.lean:40.
- **Visibility**: public
- **Lines**: 72–94 (docstring 72–76, statement 77–78), proof length 16 lines
- **Notes**: the source's proof gives an explicit `δ`; the Lean proof uses continuity instead (shorter, matches the source's "tends to 0" remark at l.1230).

## Junk check (Step 8)
- Used anywhere? Yes, by the public `Roth.exists_delta` (Main.lean:231), the parameter-choice step of the final proof.
- Wrapper of 1–2 mathlib calls? No; 16-line real-analysis argument (continuity + square-root arithmetic).
- Does mathlib have it? No (Phase 5); it is about the project-only `Roth.eta`.
- Too specific (inline?)? It has one caller, but it is a named lemma of the source (Lemma `m-δ`) and inlining would roughly double the already long `exists_delta` proof; keep as is.
- Well-chosen? Yes; matches the source's fixed-`m` Lean note verbatim.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "For fixed"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `exists_delta_bound`: no hit. Not a glue lemma (real proof), so a full run follows. Parent def `Roth.eta` is NO-composable-from-mathlib.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates)
- decl `Roth.exists_delta_bound`: resolved at Roth/MainLemma.lean:77
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma (Lemma 9), its parameters λ, γ, η, B_1, and the pigeonhole step

### Statement (Phase 1)

`Roth.exists_delta_bound` is a theorem stating the following:

Let `n, m` be natural numbers with `m > 16 n²`. Then there is `δ₀ > 0` such that every real `δ` with `0 ≤ δ ≤ δ₀` satisfies `δ < 1/m` and `10^m δ^{2^{-m}} + 2(1 + 3δ) n √m < m/2`. Equivalently: both inequalities hold for all sufficiently small `δ ≥ 0`.

Variables / typeclasses involved (Lean side):
- `n : ℕ`: degree of the algebraic number (`f.natDegree` at the call site).
- `m : ℕ`: number of variables.

Hypotheses (Lean side):
- `hm : 16 * n ^ 2 < m`: ensures the `δ = 0` value `2n√m` of the LHS of (30) is below `m/2`.

Conclusion (math): (29) and (30) hold on an interval `[0, δ₀]`.

Conclusion (Lean): `∃ δ₀ : ℝ, 0 < δ₀ ∧ ∀ δ : ℝ, 0 ≤ δ → δ ≤ δ₀ → δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: listed under `## Main results` of MainLemma.lean, but it is a parameter-choice auxiliary of Roth's proof, not a theorem with independent standing.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 16 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof choose m > 16 n^2 delta 10^m delta^(1/2)^m + 2(1+3delta) n sqrt m < m/2 | no | n/a | hits arXiv 2111.12409, minru roth.pdf, Evertse Luminy notes; none states this parameter choice |
| 2 | WebSearch (aliases / book) | Cassels Introduction to Diophantine Approximation chapter VI Roth's theorem choice of parameters m delta | no | n/a | Cassels Ch. VI text not indexed; arXiv 2502.00731, 1306.2976 use their own δ choices |
| 3 | WebSearch (general form) | existence of small parameter delta continuity at zero strict inequality eventually holds near 0 lemma | partial | the general principle "continuous at 0 with strict inequality at 0 gives the inequality near 0" | standard real analysis; in mathlib as `ContinuousAt.eventually_lt` |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | clean.tex `lem:m-delta` | yes | l.1211–1248: Lemma m-δ, eqs. (29)–(30), explicit `δ = ½ min{1/m, E/(12n√m), (E/(2·10^m))^{2^m}}`, `E = m/2 − 2n√m`; Lean note asks for the fixed-`m`, all-smaller-δ form | exact match with the Lean statement |
| 6 | nLab | Roth's theorem / parameter choice | no | n/a | nLab has no entry on proofs of Roth's theorem |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real-number inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread about this parameter choice |
| 10 | recent arXiv | 2502.00731, 2111.12409, 1306.2976 | no | n/a | each Roth-type proof makes its own ad hoc parameter choice |

### Literature summary (Phase 3)

Concept identified as: the parameter-choice step (choice of `m` and `δ`) in the Cassels-style proof of Roth's theorem; no named concept.
Sources agree on the standard form: no — each proof uses its own constants; the only general content is "a continuous function below a bound at 0 stays below it near 0".
Most general standard form: `ContinuousAt.eventually_lt` (already in mathlib).
Generality dimensions where the literature varies:
  - constants and shape of the inequalities: proof-specific.
Disagreement with the literature: none; matches source Lemma m-δ.

### Generality analysis — `Roth.exists_delta_bound`

Literature-standard form (from Phase 3): source Lemma m-δ; general principle is `ContinuousAt.eventually_lt`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hm : 16 * n ^ 2 < m` | strict bound | `m > 16n²` | NO | necessary: the conclusion at `δ = 0` implies it (compiled, evidence (1)) |
| 2 | `0 ≤ δ` in conclusion | closed lower end | `0 < δ` in source | no (already stronger) | `δ < 0` makes `δ^{(1/2)^m}` the rpow junk value; no meaningful extension |
| 3 | `n m : ℕ` | naturals | integers | no | counts |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (necessity of `hm` verified by a compiled converse)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | concrete reals | — |
| 2 | Sequences/metric vs filters? | yes (cosmetic) | `∀ᶠ δ : ℝ in 𝓝[≥] 0, δ < 1 / m ∧ …` (compiled from the current form, evidence (2)) | filter_upwards combination with the second eventual bound in `exists_delta` |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | rpow and sqrt need ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `m, n` are counts | — |
| 8 | Concrete-via-abstract? | no | proof uses `eta` explicitly (continuity and value at 0); abstract content is `ContinuousAt.eventually_lt`, already in mathlib | — |
| 9 | False-generalisation guard | no false generalisation | the filter form is equivalent | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: yes (project-local only)
  - Proposed restatement: `theorem exists_delta_bound {n m : ℕ} (hm : 16 * n ^ 2 < m) : ∀ᶠ δ : ℝ in 𝓝[≥] 0, δ < 1 / m ∧ eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2`
  - Cost: CHEAP (compiled as a corollary; the single consumer `exists_delta` would combine it with its own eventual bound via `filter_upwards` and `(… ).exists_gt`-style extraction)
  - Mathlib downstream this enables: none in mathlib (statement about project-only `eta`); local tidiness only.
  - Real mathematical improvement: no new mathematics; it removes the explicit `min`/`half` bookkeeping in both this proof and `exists_delta`.

### Proof strategy — `Roth.exists_delta_bound`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | uses `Metric.eventually_nhds_iff` to extract a radius; a filter statement would avoid it | CHEAP |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `ContinuousAt.eventually_lt`, `Real.continuousAt_rpow_const`, `Real.zero_rpow` all exist | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (continuity + eventually; the radius extraction is forced by the ∃δ₀ statement shape)

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.exists_delta_bound`

[A] Lean-Finder       "if a function is continuous at a point and f a < c then f x < c eventually near a"   hits: `ContinuousAt.eventually_lt`, `Filter.Tendsto.eventually_lt_const`, semicontinuity iff lemmas — building blocks only
[B] Loogle            `(∀ᶠ x in nhdsWithin ?a (Set.Ici ?a), ?p x) ↔ ∃ u, ?a < u ∧ _`   no hits (mathlib has `mem_nhdsGE_iff_exists_Ico_subset` style lemmas instead)
[C] LeanSearch        "there exists delta0 positive such that for all delta in [0, delta0] an inequality holds, from eventually in nhdsWithin Ici 0"   hits: `eventually_abs_sub_lt`, `Metric.eventually_prod_nhds_iff`, `UniformSpace.ofDist_aux` — generic
[D] Grep mathlib src  `namespace Roth`, `exists_delta_bound`, `Ico_mem_nhdsGE`   no Roth hit; `Ico_mem_nhdsGE` exists (Topology/Order/…, used at MonotoneContinuity.lean:52)
[E] Name pattern      lean_local_search not used (ripgrep not on PATH in earlier runs); covered by [D]

Searched for both:
  - the user's current form (Lemma m-δ with `eta`)
  - the literature-standard / general form (`ContinuousAt.eventually_lt`)

Concluded: found building blocks (`ContinuousAt.eventually_lt`, `Real.continuousAt_rpow_const`, `Real.zero_rpow`, `Real.lt_sqrt_of_sq_lt`, `Metric.eventually_nhds_iff`); not in mathlib as a statement (project-specific).

### Normal-form check — `Roth.exists_delta_bound`

Equivalent formalisms: `∃ δ₀ > 0, ∀ δ ∈ [0, δ₀], P δ` (current); `∀ᶠ δ in 𝓝[≥] 0, P δ`; `∃ δ₀ > 0, ∀ δ ∈ Set.Ico 0 δ₀, P δ`.
Does mathlib already have a canonical form for this idea? yes: eventual statements in `𝓝[≥] 0`.
Proposed canonical form: the filter form (local refactor only; not proposed for mathlib).
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_delta_bound`

Alternative restatements attempted:
- current ∃δ₀ form
- `∀ᶠ δ : ℝ in 𝓝[≥] 0, …` (compiled as a corollary)
- source's explicit `δ` (single-value existential)

Chosen restatement: current (kept; the filter form is an optional local tidy).
Justification: the single consumer `exists_delta` uses `δ₀` directly with `exists_between (lt_min hδ₀ hε)`; the all-smaller-δ form is what the source's Lean note requests.

### Superfluous-argument audit — `Roth.exists_delta_bound`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hm` | yes | necessary (compiled converse, evidence (1)) |
| 2 | `n`, `m` | yes | in the conclusion |

### Statement-shape verdict (Phase 5.5)

Normal form: OK (filter form optional locally)
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.exists_delta_bound`

Internal use count: 1 (outside the declaring file)
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:231 | `obtain ⟨δ₀, hδ₀, hδ₀'⟩ := exists_delta_bound hm` (in `Roth.exists_delta`) |

Inline-derivation grep: `exists_delta` (Main.lean:232–248) repeats the same continuity pattern (`Real.continuousAt_rpow_const` + `ContinuousAt.eventually_lt` + `Metric.eventually_nhds_iff`) for its own bound (48), but does not re-derive (29)/(30). (none for this statement.)

### Composition check (Phase 6)

Can `Roth.exists_delta_bound` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Metric.eventually_nhds_iff.mp (hc.eventually_lt continuousAt_const h0)` then pick `δ₀ = min (1/m) ε / 2`
  - Mathlib decls used: `ContinuousAt.eventually_lt`, `Metric.eventually_nhds_iff`, `Real.continuousAt_rpow_const`, `Real.zero_rpow`
  - Result: partial — still needs the gap `2n√m < m/2` from `hm` (sqrt arithmetic with `nlinarith`), the continuity proof, the evaluation at 0, and the `min`/`half` choice for (29)
  - Notes: a real proof, not a call chain

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_delta_bound`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the source's Lemma m-δ (clean.tex l.1211–1248); every Roth-type proof makes its own parameter choice; the general content is `ContinuousAt.eventually_lt`.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (`hm` necessary, compiled converse).
- Mathlib search (Phase 5): building blocks only; no counterpart.
- Composition check (Phase 6): NOT-COMPOSABLE (16-line argument).

**Rationale:**

The statement is a bookkeeping step of one proof of Roth's theorem, phrased in terms of the project-only constant `Roth.eta`. It has no standing outside that proof, so no YES bucket fits; the abstract principle behind it (`ContinuousAt.eventually_lt`) is already in mathlib. But it is not a ≤3-call composition either: the gap `2n√m < m/2` from `m > 16n²`, the continuity of `δ ↦ η + 2(1+3δ)n√m`, its value at 0, and the extra condition `δ < 1/m` take a genuine 16-line proof. So NO-composable does not apply by the gate, and the skill cannot pick a bucket alone. Same situation and same recommended resolution as the sibling numeric lemmas `Roth.lem7_numeric`, `Roth.lem7_Φ_bound`, `Roth.sum_inv_lt` (all BORDERLINE, keep project-local).

Belongs-elsewhere check: belongs in the Roth project (it is a named lemma of the source paper), next to `eta` in Roth/MainLemma.lean.

Numbered questions:
1. Do you agree to keep `Roth.exists_delta_bound` project-local and never upstream it (recommended: yes)?
2. Should it be restated as `∀ᶠ δ : ℝ in 𝓝[≥] 0, δ < 1 / m ∧ …` (compiled from the current form in evidence (2)), with `Roth.exists_delta` (Main.lean:227) refactored to combine eventual bounds via `filter_upwards` (recommended: optional, only if `exists_delta` is touched)?
3. Given its single caller, should it stay public as the source's Lemma m-δ (recommended: yes, for blueprint correspondence) rather than be made private?

Next action: user answers; default is keep as is in Roth/MainLemma.lean.

### Next step

Keep `Roth.exists_delta_bound` project-local in Roth/MainLemma.lean (single caller `Roth.exists_delta`, Roth/Main.lean:231); do not upstream.

## Evidence
- WebSearch ×3 (queries in the literature table): no source beyond the project paper states this parameter choice.
- Local reference clean.tex l.1211–1248 (Lemma m-δ, explicit δ, Lean note), l.1598 (use in §7).
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5; grep of `.lake/packages/mathlib/Mathlib/` (no `Roth` hit).
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_delta_bound/experiments.lean` (imports Roth.MainLemma), checked with `lean_diagnostic_messages`: clean, no errors or warnings. Contains (1) the converse: the conclusion forces `16 * n ^ 2 < m` (necessity of `hm`); (2) the filter-form restatement `∀ᶠ δ : ℝ in 𝓝[≥] 0, …` derived from `exists_delta_bound` via `Ico_mem_nhdsGE`.
