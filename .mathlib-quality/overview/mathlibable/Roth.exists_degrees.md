---
decl: Roth.exists_degrees
file: Roth/Main.lean
line: 282
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Source eqs. (51)-(53) rounding lemma choosing degrees r_j = ceil(s log q_1 / log q_j) in Roth's proof; hdelta0 and hq necessary (compiled converse) and h50 not droppable (compiled counterexample), no literature standing outside this proof, no mathlib counterpart, and a 30-line rounding argument rather than a 3-call composition; recommended resolution keep project-local.
action: Keep in Roth/Main.lean (single caller private Roth.exists_roth_approximants_aux at Roth/Main.lean:440); do not upstream; optionally relax hδ1 to δ ≤ 10 (uncompiled observation) if a caller ever needs it.
---

# Roth.exists_degrees

## Inventory entry

### `theorem Roth.exists_degrees`
- **Type**: `{m : ℕ} [NeZero m] {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) {q : Fin m → ℕ} (hq : ∀ j, 1 < q j) (h50 : ∀ i j : Fin m, i.val + 1 = j.val → 2 / δ * Real.log (q i) ≤ Real.log (q j)) : ∃ r : Fin m → ℕ, (∀ j, 0 < r j) ∧ (∀ j, 10 / δ < r j) ∧ (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) ∧ (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧ ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))`
- **What**: the choice of degrees in §7 of the source (clean.tex l.1615–1642): given denominators `q_j > 1` whose logarithms grow by a factor `≥ 2/δ` from one index to the next, there are positive degrees `r_j` with `r_j > 10/δ` (31), `r_{j+1}/δ < r_j` (31), `r_1 log q_1 ≤ r_j log q_j` (33) and `r_j log q_j < (1 + δ/10) r_1 log q_1` (53).
- **How**: pick `s : ℕ` above `max_j 10 ℓ_j / (δ ℓ_0)` (`exists_nat_gt`, `Finset.le_sup'`), with `ℓ_j = log q_j > 0` (`Real.log_pos`); set `r_j = ⌈s ℓ_0 / ℓ_j⌉₊` so `r_0 = s` (`Nat.ceil_natCast`); lower bound from `Nat.le_ceil`, upper bound from `Nat.ceil_lt_add_one` plus the choice of `s`; (31) both parts by `div_lt_iff₀`, `mul_lt_mul_iff_left₀` and `hδ1` (`(1+δ/10)/2 < 1`).
- **Hypotheses**: `hδ0` (positivity of δ, necessary), `hδ1 : δ ≤ 1` (used only to bound `(1+δ/10)/2 ≤ 11/20`), `hq` (logs positive, necessary), `h50` (eq. (50) growth, needed for (31b)).
- **Uses from project**: `[]` (only mathlib)
- **Used by**: private `Roth.exists_roth_approximants_aux` (Roth/Main.lean:440); module docstring Main.lean:33.
- **Visibility**: public
- **Lines**: 276–315 (docstring 276–281, statement 282–286), proof length 29 lines
- **Notes**: none

## Junk check (Step 8)
- Used anywhere? Yes, by `Roth.exists_roth_approximants_aux` (Main.lean:440).
- Wrapper of 1–2 mathlib calls? No; a 29-line rounding argument.
- Does mathlib have it? No (Phase 5); nearest are `Nat.ceil_lt_add_one`, `Nat.le_ceil`, `LinearGrowth.Real.eventually_atTop_exists_nat_between` (building blocks only).
- Too specific (inline?)? Single caller, but it is the source's named "one rounding lemma" (Lean note at clean.tex l.1640–1642); inlining would bloat the private aux. Keep.
- Well-chosen? Yes; matches eqs. (51)–(53) exactly.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name does not end in `_aux`; docstring starts "Given"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `Roth.exists_degrees` / `exists_degrees` inside a `Roth` namespace: no hit. Not a glue lemma. Full run follows. Siblings `Roth.exists_approximants`, `Roth.exists_delta`, `Roth.exists_m` are BORDERLINE-needs-human.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule)
- decl `Roth.exists_degrees`: resolved at Roth/Main.lean:282
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §7 of the source: assembling Roth's theorem (choice of parameters m, δ, approximants, degrees, and the final contradiction)

### Statement (Phase 1)

`Roth.exists_degrees` is a theorem stating the following:

Let `0 < δ ≤ 1` and let `q_0, …, q_{m-1}` be integers `> 1` with `log q_{j+1} ≥ (2/δ) log q_j`. Then there are positive integers `r_0, …, r_{m-1}` with `r_j > 10/δ`, `r_{j+1} < δ r_j`, and `r_0 log q_0 ≤ r_j log q_j < (1 + δ/10) r_0 log q_0` for every `j`.

Variables / typeclasses involved (Lean side):
- `m : ℕ` with `[NeZero m]`: number of approximants (index 0 must exist).
- `δ : ℝ`: Roth's small parameter.
- `q : Fin m → ℕ`: denominators of the approximants.

Hypotheses (Lean side):
- `hδ0 : 0 < δ`, `hδ1 : δ ≤ 1`: size of δ.
- `hq : ∀ j, 1 < q j`: makes `log q_j > 0`.
- `h50`: eq. (50), rapid growth of `log q_j`.

Conclusion (math): degrees satisfying (31), (33), (53).

Conclusion (Lean): `∃ r : Fin m → ℕ, (∀ j, 0 < r j) ∧ (∀ j, 10 / δ < r j) ∧ (∀ i j : Fin m, i.val + 1 = j.val → (r j : ℝ) / δ < r i) ∧ (∀ j, (r 0 : ℝ) * Real.log (q 0) ≤ r j * Real.log (q j)) ∧ ∀ j, (r j : ℝ) * Real.log (q j) < (1 + δ / 10) * (r 0 * Real.log (q 0))`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: parameter-choice auxiliary of Roth's proof, no independent standing.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 29 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof choose degrees r_j = ceil(r_1 log q_1 / log q_j) r_j log q_j close to r_1 log q_1 | no | n/a | hits Wikipedia Roth, arXiv 2502.00731 (subspace survey), Evertse notes; balanced weights `r_j log q_j ≈ const` are the standard idea but no statement of this lemma |
| 2 | WebSearch (aliases / book) | Cassels Diophantine approximation Roth theorem choice of r_1..r_m "r_j log q_j" index polynomial degrees | partial | weights with small consecutive ratios and `r_j log q_j` roughly constant | Cassels Ch. VI not indexed; arXiv 2502.00731 describes the same weight choice informally |
| 3 | WebSearch (general form) | simultaneous rounding positive reals to integers ceiling ratio bounded relative error lemma | no | n/a | only unrelated rounding/discrepancy papers (math/9504228, 1501.00014); the content here is the elementary `⌈x⌉ < x + 1` |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | clean.tex roth:eq51–roth:eq53 | yes | l.1615–1642: (51) r_1 large, (52) `r_1 log q_1/log q_j ≤ r_j < 1 + r_1 log q_1/log q_j`, (53), and (31)/(33) derived; Lean note asks for "one rounding lemma" | exact match |
| 6 | nLab | Roth's theorem / degree choice | no | n/a | nLab has no entry on proofs of Roth's theorem |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | elementary real inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread on this degree choice |
| 10 | recent arXiv | 2502.00731, 1806.10737 | no | n/a | each Roth-type proof makes its own ad hoc weight choice |

### Literature summary (Phase 3)

Concept identified as: the choice of balanced degrees (weights) in the Roth/Cassels proof; no named concept.
Sources agree on the standard form: no — constants are proof-specific; the shared idea is `r_j log q_j ≈ r_1 log q_1`.
Most general standard form: none beyond the elementary rounding fact `⌈x⌉ < x + 1` (`Nat.ceil_lt_add_one`).
Generality dimensions where the literature varies:
  - constants (10/δ, 1 + δ/10, growth factor 2/δ): proof-specific.
Disagreement with the literature: none; matches source eqs. (50)–(53).

### Generality analysis — `Roth.exists_degrees`

Literature-standard form (from Phase 3): source §7 degree choice.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hδ0 : 0 < δ` | strict | `δ > 0` | NO | necessary: (33)+(53) imply `0 < δ` (compiled converse) |
| 2 | `hq : ∀ j, 1 < q j` | strict | `q_j > 1` | NO | necessary: (33)+(53) imply `1 < q j` for all `j` (compiled converse) |
| 3 | `h50` | eq. (50) | eq. (50) | NO (cannot drop) | without it the conclusion can fail: `m = 2`, `q = (2,2)`, `δ = 1` (compiled counterexample) |
| 4 | `hδ1 : δ ≤ 1` | `δ ≤ 1` | `δ` small | possibly (not verified) | the proof only uses `(1+δ/10)/2 ≤ 11/20 < 1`; `δ ≤ 10` (or any `δ` with a larger `s`) looks sufficient, but this was not compiled, so not claimed |
| 5 | `[NeZero m]` | index 0 exists | — | NO | `r 0`, `q 0` appear in the conclusion |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (no compiled weakening; `hδ0`, `hq` shown necessary, `h50` shown non-droppable)
Number of weakening opportunities found: 0 verified (one uncompiled observation on `hδ1`, irrelevant to the single caller which has `δ ≤ 1`)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | concrete reals | — |
| 2 | Sequences/metric vs filters? | no | finite family, no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | uses `Real.log` | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | partial | `Fin m` with `i.val + 1 = j.val` could be any finite linear order with successor; no gain | none |
| 8 | Concrete-via-abstract? | partial | the proof only uses `ℓ_j = log q_j > 0`; an abstract version over positive reals `ℓ_j` is the real content, but it remains a proof-specific inequality bundle | none |
| 9 | False-generalisation guard | no false generalisation | the `ℓ_j` abstraction is equivalent | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the statement is a bespoke bundle of proof-specific inequalities; abstracting `log q_j` to positive reals `ℓ_j` would be a local tidy, not a mathlib contribution.

### Proof strategy — `Roth.exists_degrees`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | explicit ceiling construction is the point | — |
| 5 | missing mathlib helpers | no | `Nat.le_ceil`, `Nat.ceil_lt_add_one`, `Nat.ceil_natCast`, `Finset.le_sup'`, `exists_nat_gt` all exist | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (direct construction exactly as in the source's Lean note)

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.exists_degrees`

[A] Lean-Finder       "for positive reals l_j there exist natural numbers r_j with r_0 l_0 ≤ r_j l_j < (1+ε) r_0 l_0"   hits: `LinearGrowth.Real.eventually_atTop_exists_nat_between` (one natural between `a x` and `b x`) — building block only
[B] Loogle            `(⌈?x⌉₊ : ?α) < ?x + 1`   no direct hit (pattern unification); found via [C]
[C] LeanSearch        "ceiling of x/y times y is less than x + y"   hits: `Nat.ceil_lt_add_one`, `Int.ceil_lt_add_one` — building blocks
[D] Grep mathlib src  `exists_degrees` / `Roth` under `.lake/packages/mathlib/Mathlib/`   no hit
[E] Name pattern      `exists_degrees` in namespace Roth; only the project decl

Searched for both:
  - the user's current form (degrees with (31), (33), (53))
  - the general form (simultaneous rounding with bounded relative error)

Concluded: found building blocks (`Nat.le_ceil`, `Nat.ceil_lt_add_one`, `Nat.ceil_natCast`, `exists_nat_gt`, `Finset.le_sup'`); not in mathlib (project-specific).

### Normal-form check — `Roth.exists_degrees`

Equivalent formalisms: current five-conjunct existential; existential over positive reals `ℓ_j` instead of `log q_j`; (31b) as `r j < δ * r i`.
Does mathlib already have a canonical form for this idea? no.
Proposed canonical form: current (matches the source and the caller).
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.exists_degrees`

Alternative restatements attempted:
- current form
- abstract `ℓ : Fin m → ℝ` with `0 < ℓ j` in place of `q`/`hq` (not compiled; optional)
- (31b) as `(r j : ℝ) < δ * r i`

Chosen restatement: current.
Justification: the caller destructures exactly these five facts and re-exports (33), (53) verbatim.

### Superfluous-argument audit — `Roth.exists_degrees`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hδ0` | yes | necessary (compiled converse) |
| 2 | `hδ1` | yes in proof | conclusion likely holds for larger δ (uncompiled); caller has `δ ≤ 1` |
| 3 | `hq` | yes | necessary (compiled converse) |
| 4 | `h50` | yes | not droppable (compiled counterexample) |
| 5 | `[NeZero m]` | yes | index 0 |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.exists_degrees`

Internal use count: 1 (in the declaring file; no other files)
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:440 | `obtain ⟨r, hr0, h31a, h31b, h33, h53⟩ := exists_degrees hδ0 hδ1 hq1` (in private `Roth.exists_roth_approximants_aux`) |

Inline-derivation grep: (none) — no other site re-derives the ceiling degrees.

### Composition check (Phase 6)

Can `Roth.exists_degrees` be derived from mathlib in ≤3 chained calls?

Attempt 1: `⟨fun j ↦ ⌈s * ℓ 0 / ℓ j⌉₊, …⟩` with `Nat.le_ceil` / `Nat.ceil_lt_add_one`
  - Mathlib decls used: `exists_nat_gt`, `Finset.le_sup'`, `Nat.le_ceil`, `Nat.ceil_lt_add_one`, `Nat.ceil_natCast`, `div_lt_iff₀`
  - Result: partial — still needs the choice of `s`, and the real-inequality algebra for (31a), (31b), (53) using `h50` and `hδ1`
  - Notes: a genuine 29-line proof, not a call chain

Conclusion: NOT-COMPOSABLE

### Verdict: `Roth.exists_degrees`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): only the source's §7 (clean.tex l.1615–1642); other Roth proofs use the same balanced-weight idea with their own constants.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (`hδ0`, `hq` necessary by compiled converse; `h50` non-droppable by compiled counterexample).
- Mathlib search (Phase 5): building blocks only; no counterpart.
- Composition check (Phase 6): NOT-COMPOSABLE (29-line argument).

**Rationale:**

The statement is a bookkeeping step of one proof of Roth's theorem: it bundles five proof-specific inequalities (eqs. (31), (33), (53)) about ceiling-defined degrees. It has no standing outside that proof, so no YES bucket fits; its only general ingredient, `⌈x⌉ < x + 1`, is already `Nat.ceil_lt_add_one`. But it is not a ≤3-call composition, since the choice of `s` and the inequality algebra are a real 29-line proof, so NO-composable does not apply by the gate. Same situation and same recommended resolution as its siblings `Roth.exists_approximants`, `Roth.exists_delta`, `Roth.exists_m` (all BORDERLINE, keep project-local).

Belongs-elsewhere check: belongs in the Roth project (Roth/Main.lean), as the source's "one rounding lemma" for eqs. (51)–(53).

Numbered questions:
1. Do you agree to keep `Roth.exists_degrees` project-local and never upstream it (recommended: yes)?
2. Should `hδ1 : δ ≤ 1` be relaxed (e.g. to `δ ≤ 10`), given the only caller has `δ ≤ 1` (recommended: no, not needed)?
3. Given its single caller (private `exists_roth_approximants_aux`), should it stay public for blueprint correspondence with eqs. (51)–(53) (recommended: yes)?

Next action: user answers; default is keep as is in Roth/Main.lean.

### Next step

Keep `Roth.exists_degrees` project-local in Roth/Main.lean (single caller `Roth.exists_roth_approximants_aux`, Roth/Main.lean:440); do not upstream.

## Evidence
- WebSearch ×3 (queries in the literature table): no source beyond the project paper states this degree choice.
- Local reference clean.tex l.1615–1642 (eqs. (51)–(53) and the Lean note).
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5; grep of `.lake/packages/mathlib/Mathlib/` (no hit).
- Evidence file `.mathlib-quality/overview/evidence/Roth.exists_degrees/experiments.lean` (imports Mathlib only; self-contained statement shapes), checked with `lean_diagnostic_messages`: clean, no errors or warnings. Contains `exists_degrees_converse` ((33) and (53) imply `0 < δ` and `∀ j, 1 < q j`) and `exists_degrees_needs_h50` (for `m = 2`, `q = (2,2)`, `δ = 1` no `r` satisfies (31b) and (33)).
