---
decl: Roth.exists_m
file: Roth/Main.lean
line: 196
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Eq. (47) parameter choice of Roth's proof (for kappa > 2 pick m > 16n^2 with 2m/(m - 4n sqrt m) < kappa); no literature standing outside this proof, no mathlib counterpart, hypothesis 2 < kappa necessary (compiled converse), a 20-line explicit-witness argument rather than a 3-call composition; its middle conjunct 4n sqrt m < m is redundant (compiled from 16n^2 < m) and discarded at the only call site; recommended resolution keep project-local.
action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_parameters_aux at Roth/Main.lean:419); do not upstream; optionally drop the redundant conjunct 4 * n * sqrt m < m from the statement (derivable from 16 * n ^ 2 < m, evidence (1)) and the `-` pattern at Main.lean:419.
---

# Roth.exists_m

## Inventory entry

### `theorem Roth.exists_m`
- **Type**: `{n : ℕ} {κ : ℝ} (hκ : 2 < κ) : ∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧ 2 * m / (m - 4 * n * √(m : ℝ)) < κ`
- **What**: the choice of the number of variables `m` in §7 of the source (eq. (47)): for `κ > 2` there is `m > 16 n²` with `4 n √m < m` and `2m / (m − 4n√m) < κ`.
- **How**: explicit witness `m = s²` with `s = ⌈4κn/(κ−2)⌉₊ + 4n + 1`; then `4n < s` (`lia`), `4κn < s(κ−2)` (`Nat.le_ceil`, `div_lt_iff₀`), first conjunct by `Nat.pow_lt_pow_left`, second by `Real.sqrt_sq` and `mul_lt_mul_of_pos_right`, third by `Real.sqrt_sq`, `div_lt_iff₀` and `nlinarith`.
- **Hypotheses**: `hκ : 2 < κ` (necessary: the conclusion forces it, compiled in evidence (2)).
- **Uses from project**: `[]`
- **Used by**: `Roth.exists_roth_parameters_aux` (private, Roth/Main.lean:419, which discards the middle conjunct with `-`); module docstring Roth/Main.lean:29; docstring of `Roth.exists_delta` (Main.lean:220).
- **Visibility**: public
- **Lines**: 191–218 (docstring 191–195, statement 196–197), proof length 21 lines
- **Notes**: the middle conjunct `4 n √m < m` is implied by `16 n² < m` (compiled, evidence (1)) and is unused at the only call site; kept only to mirror the source's wording ("`m > 4n m^{1/2}`").

## Junk check (Step 8)
- Used anywhere? Yes, once, by the private `Roth.exists_roth_parameters_aux` (Main.lean:419), the parameter-choice step of the final proof.
- Wrapper of 1–2 mathlib calls? No; explicit-witness real arithmetic over ~20 lines.
- Does mathlib have it? No (Phase 5); it is a proof-specific numeric choice.
- Too specific (inline?)? Single caller, but it is a named step of the source (eq. (47)) and inlining would lengthen an already long parameter lemma; keep as is.
- Well-chosen? Mostly; the middle conjunct is redundant (derivable from the first) and is discarded by the caller, so the statement could be slimmed.
- Conclusion: `KEEP` (optional tidy: drop the redundant middle conjunct).

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "For `κ > 2`"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Roth.exists_m` / `namespace Roth`: no hit. Not a glue lemma (real proof, no parent def), so a full run follows.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.exists_m`:      resolved at Roth/Main.lean:196
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §7 of the source: the proof of Roth's theorem (choice of parameters, approximants, and the final contradiction)

### Statement (Phase 1)

`Roth.exists_m` is a theorem stating the following:

Let `n ≥ 0` be an integer and `κ > 2` a real number. Then there exists a positive integer `m` with `m > 16 n²`, `m > 4 n √m`, and `2m / (m − 4n√m) < κ`. (Equivalently: since `2m/(m − 4n√m) = 2/(1 − 4n/√m) → 2` as `m → ∞`, all three hold for every sufficiently large `m`.)

Variables / typeclasses involved (Lean side):
- `n : ℕ`: the degree of the algebraic number (`f.natDegree` at the call site).
- `κ : ℝ`: the approximation exponent.

Hypotheses (Lean side):
- `hκ : 2 < κ`: the limit value of `2m/(m − 4n√m)` is 2, so the strict bound needs `κ > 2`.

Conclusion (math): a suitable number of variables `m` exists.

Conclusion (Lean): `∃ m : ℕ, 16 * n ^ 2 < m ∧ 4 * n * √(m : ℝ) < m ∧ 2 * m / (m - 4 * n * √(m : ℝ)) < κ`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a parameter-choice auxiliary of Roth's proof (source eq. (47)), not a theorem with independent standing.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 21 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof choose m large enough "2m/(m - 4n" kappa > 2 | no | n/a | hits arXiv math/0307203 (quantitative Roth–Ridout, own constraints on m, δ), Roth AP papers (unrelated); none states (47) |
| 2 | WebSearch (named-after / book) | Cassels Roth's theorem proof choice of number of variables m depending on kappa and degree n | no | n/a | Wikipedia Roth's theorem, arXiv 2502.00731, 1305.0926, 2410.09558 (notes a gap in Cassels); each proof makes its own m choice |
| 3 | WebSearch (general form) | limit m/(m - c sqrt m) = 1 as m tends to infinity eventually less than bound existence lemma | partial | `m/(m − c√m) = 1/(1 − c/√m) → 1`, hence eventually below any bound > 1 | elementary calculus; no named lemma |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | clean.tex eq. `roth:eq47` | yes | l.1588–1593: "We choose a positive integer m large enough that m > 4nm^{1/2} and 2m/(m − 4nm^{1/2}) < κ, which is possible as κ > 2"; `m > 16n²` from Lemma m-δ (l.1212, 1236) | exact match with the Lean statement |
| 6 | nLab | Roth's theorem / parameter choice | no | n/a | nLab has no entry on proofs of Roth's theorem |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real-number inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread about this parameter choice; only generic limit threads |
| 10 | recent arXiv | 2502.00731, 2410.09558, math/0307203 | no | n/a | each Roth-type proof makes its own ad hoc parameter choice |

### Literature summary (Phase 3)

Concept identified as: the choice of the number of variables `m` in the Cassels-style proof of Roth's theorem; no named concept.
Sources agree on the standard form: no — each proof uses its own constants; the only general content is "`2m/(m − 4n√m) → 2`, so it is eventually below any `κ > 2`".
Most general standard form: `∀ᶠ m in atTop, …` from a limit statement (built from mathlib's `Tendsto` API).
Generality dimensions where the literature varies:
  - constants (`16n²`, `4n`): proof-specific.
Disagreement with the literature: none; matches source eq. (47).

### Generality analysis — `Roth.exists_m`

Literature-standard form (from Phase 3): source eq. (47) plus `m > 16n²`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hκ : 2 < κ` | strict | `κ > 2` | NO | necessary: the conclusion forces `2 < κ` (compiled, evidence (2)) |
| 2 | `n : ℕ` | natural | degree | no | a count |
| 3 | conjunct `4 n √m < m` | stated | stated in source | n/a (conclusion) | redundant: follows from `16 n² < m` (compiled, evidence (1)); dropping it weakens nothing, only slims the statement |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (the only hypothesis is necessary, compiled converse)
Proposed restatement: none for generality; optional local slimming by deleting the redundant middle conjunct.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | concrete reals | — |
| 2 | Sequences/metric vs filters? | yes (cosmetic) | `∀ᶠ m : ℕ in atTop, 16 * n ^ 2 < m ∧ 2 * m / (m - 4 * n * √m) < κ` (via a limit `→ 2`) | none in mathlib; consumer only needs one `m` |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | sqrt needs ℝ | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `m, n` are counts | — |
| 8 | Concrete-via-abstract? | no | no named object; proof is explicit arithmetic | — |
| 9 | False-generalisation guard | no false generalisation | the eventually form implies the current one | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no (for mathlib)
  - One-line reason: the eventually-at-top restatement is a project-local cosmetic choice (the consumer needs a single `m`); it adds no mathlib API, since the statement is a proof-specific numeric bound.

### Proof strategy — `Roth.exists_m`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | partial | prove `Tendsto (fun m ↦ 2m/(m − 4n√m)) atTop (𝓝 2)` and take `(… ).eventually_lt_const` with `eventually_gt_atTop`; avoids the explicit ceiling witness | MODERATE (the explicit witness is already short) |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `Nat.le_ceil`, `Real.sqrt_sq`, `div_lt_iff₀`, `Real.lt_sqrt_of_sq_lt` all exist | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (explicit witness, short and fully elementary; the filter alternative would not be shorter)

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.exists_m`

[A] Lean-Finder       "m / (m - c * sqrt m) tends to 1 as m tends to infinity"   hits: `tendsto_natCast_div_add_atTop`, `Stirling.tendsto_self_div_two_mul_self_add_one`, `tendsto_nat_ceil_div_atTop` — building blocks only, no sqrt-ratio limit
[B] Loogle            `Filter.Tendsto (fun x : ℝ => √x / x) Filter.atTop (nhds 0)`   no hits
[C] LeanSearch        "there exists natural m such that c * sqrt m < m and 2 m / (m - c sqrt m) < κ for κ > 2"   hits: `Nat.sqrt_lt`, `exists_pow_btwn_of_lt_mul` — unrelated
[D] Grep mathlib src  `Roth.exists_m`, `namespace Roth`, `sqrt_div_self`   no Roth hit; `Real.sqrt_div_self'` (Analysis/Real/Sqrt.lean:391) is a building block for a limit proof
[E] Name pattern      lean_local_search not needed: the qualified name is project-only; covered by [D]

Searched for both:
  - the user's current form (eq. (47) with `16n²`)
  - the literature-standard / general form (eventually-at-top from a limit `→ 2`)

Concluded: found building blocks (`Nat.le_ceil`, `Real.sqrt_sq`, `Real.lt_sqrt_of_sq_lt`, `div_lt_iff₀`, `Real.sqrt_div_self'`); not in mathlib as a statement (project-specific).

### Normal-form check — `Roth.exists_m`

Equivalent formalisms: `∃ m, P m` (current); `∀ᶠ m in atTop, P m` (stronger, also true).
Does mathlib already have a canonical form for this idea? no (proof-specific numeric condition).
Proposed canonical form: current existential suffices for the single consumer.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_m`

Alternative restatements attempted:
- current three-conjunct form
- two-conjunct form `16 * n ^ 2 < m ∧ 2 * m / (m - 4 * n * √m) < κ` (middle conjunct derivable, evidence (1))
- `∀ᶠ m : ℕ in atTop, …`

Chosen restatement: two-conjunct form is marginally easier (the caller already discards the middle conjunct); current form kept for verbatim correspondence with the source.
Justification: the call site `obtain ⟨m, hm, -, h47'⟩` never uses `4 n √m < m`.

### Superfluous-argument audit — `Roth.exists_m`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hκ` | yes | necessary (compiled converse, evidence (2)) |
| 2 | `n` | yes | in the conclusion |
| 3 | conclusion conjunct `4 n √m < m` | no (redundant output) | implied by `16 n² < m`; unused by the caller |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: RESTATE (optional, local: drop the redundant middle conjunct)
Superfluous arguments: NONE (one redundant conclusion conjunct, see above)

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.exists_m`

Internal use count: 0 outside the declaring file (1 within Roth/Main.lean)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:419 | `obtain ⟨m, hm, -, h47'⟩ := exists_m (n := f.natDegree) hκ` (in private `Roth.exists_roth_parameters_aux`) |

Inline-derivation grep: `Roth.exists_delta_bound` (Roth/MainLemma.lean) re-derives `4n < √m` from `16n² < m` internally for its own gap bound; no other re-derivation of (47). (none for this statement.)

### Composition check (Phase 6)

Can `Roth.exists_m` be derived from mathlib in ≤3 chained calls?

Attempt 1: `((tendsto_… : Tendsto (fun m : ℕ ↦ 2 * m / (m - 4 * n * √m)) atTop (𝓝 2)).eventually_lt_const hκ).and (eventually_gt_atTop _) |>.exists`
  - Mathlib decls used: `Filter.Tendsto.eventually_lt_const`, `Filter.eventually_gt_atTop`, `Filter.Eventually.exists`
  - Result: partial — the limit `2m/(m − 4n√m) → 2` is not in mathlib and needs its own multi-step proof (`Real.sqrt_div_self'`, `tendsto_inv_atTop_zero`, sqrt tendsto, algebra)
  - Notes: plus the redundant middle conjunct

Attempt 2: explicit witness (current proof)
  - Result: a 21-line arithmetic proof, not a call chain.

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_m`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the source's eq. (47) (clean.tex l.1588–1593); every Roth-type proof makes its own parameter choice; the general content is an elementary limit.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (`hκ` necessary, compiled converse).
- Mathlib search (Phase 5): building blocks only; no counterpart.
- Composition check (Phase 6): NOT-COMPOSABLE (21-line explicit-witness argument; the limit route needs a missing limit lemma).

**Rationale:**

The statement is a bookkeeping step of one proof of Roth's theorem with proof-specific constants (`16n²`, `4n`). It has no standing outside that proof, so no YES bucket fits, and mathlib does not have it. But it is not a ≤3-call composition either: either one writes the explicit ceiling witness (current proof) or one first proves the limit `2m/(m − 4n√m) → 2`, which is itself a multi-step argument. So NO-composable does not apply by the gate, and the skill cannot pick a bucket alone. Same situation and same recommended resolution as the sibling parameter lemmas `Roth.exists_delta_bound` and `Roth.lem7_numeric` (BORDERLINE, keep project-local). A small local tidy is available: the middle conjunct `4 n √m < m` is implied by `16 n² < m` (compiled) and is discarded by the only caller.

Belongs-elsewhere check: belongs in the Roth project (it is eq. (47) of the source paper), in Roth/Main.lean next to `Roth.exists_delta`.

Numbered questions:
1. Do you agree to keep `Roth.exists_m` project-local and never upstream it (recommended: yes)?
2. Should the redundant middle conjunct `4 * n * √(m : ℝ) < m` be dropped from the statement (it follows from `16 * n ^ 2 < m`, evidence (1)), updating the pattern at Roth/Main.lean:419 from `⟨m, hm, -, h47'⟩` to `⟨m, hm, h47'⟩` (recommended: optional; keep if verbatim correspondence with eq. (47) is preferred)?
3. Given its single caller is private, should it stay public as the source's eq. (47) step (recommended: yes, for blueprint correspondence)?

Next action: user answers; default is keep as is in Roth/Main.lean.

### Next step

Keep `Roth.exists_m` project-local in Roth/Main.lean (single caller `Roth.exists_roth_parameters_aux`, Roth/Main.lean:419); do not upstream; optionally drop the redundant middle conjunct.

## Evidence
- WebSearch ×3 (queries in the literature table): no source beyond the project paper states this parameter choice.
- Local reference clean.tex l.1588–1593 (eq. (47)), l.1212 and l.1236 (`m > 16n²` from Lemma m-δ).
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5; grep of `.lake/packages/mathlib/Mathlib/` (no `Roth` hit; `Real.sqrt_div_self'` found).
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_m/experiments.lean` (imports Mathlib only; statement is pure real arithmetic), checked with `lean_diagnostic_messages`: clean, no errors or warnings. Contains (1) `16 * n ^ 2 < m → 4 * n * √m < m` (middle conjunct redundant); (2) the conclusion of `exists_m` implies `2 < κ` (necessity of `hκ`).
