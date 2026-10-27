---
decl: Roth.eta_lt_gam_iff
file: Roth/MainLemma.lean
line: 100
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: eta_lt_gam_iff is the source's eq. (38), the rearrangement "(30) iff eta < gamma" of the project-only parameters gam/lam/eta; after unfolding gam = m/2 - 2(1+3delta)n sqrt m it is exactly mathlib's lt_sub_iff_add_lt (compiled two-step composition), so nothing to upstream; kept locally as the paper's named step with two callers.
action: Do not upstream; keep Roth.eta_lt_gam_iff in Roth/MainLemma.lean next to gam (callers Roth/Main.lean:241 and Roth/Main.lean:560, both via sub_pos); optional local tidy, restate as the gap form 0 < gam - eta (compiled in evidence) to drop the sub_pos at both call sites.
---

# Roth.eta_lt_gam_iff

## Inventory entry

### `theorem Roth.eta_lt_gam_iff`
- **Type**: `(δ : ℝ) (n m : ℕ) : eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ eta δ m < gam δ n m`
- **What**: inequality (30) of the source, `η + 2(1+3δ) n √m < m/2`, is equivalent to (38) `η < γ`, where `γ = (m - λ)/2` and `λ = 4(1+3δ) n √m`.
- **How**: `grind [gam, lam]`: unfold `gam` and `lam`, then linear arithmetic over ℝ.
- **Hypotheses**: none (holds for all real `δ` and natural `n, m`).
- **Uses from project**: `Roth.eta`, `Roth.gam`, `Roth.lam`
- **Used by**: `Roth.exists_delta` (Roth/Main.lean:241, `sub_pos.mpr ((eta_lt_gam_iff 0 n m).mp …)`); a theorem at Roth/Main.lean:560 (`sub_pos.2 ((eta_lt_gam_iff _ _ _).1 h30)`).
- **Visibility**: public
- **Lines**: 95–102 (docstring 95–99, statement 100–101), proof length 1 line
- **Notes**: docstring cites source eq. (38) (clean.tex l.1355–1359).

## Junk check (Step 8)
- Used anywhere? Yes, 2 call sites in Roth/Main.lean (241, 560).
- Wrapper of 1–2 mathlib calls? Essentially yes after unfolding: `gam = m/2 - 2(1+3δ)n√m` (ring) plus `lt_sub_iff_add_lt`. But it is about project defs, so mathlib cannot host it.
- Does mathlib have it? No (project-only `gam`/`eta`); the abstract content is `lt_sub_iff_add_lt`.
- Too specific (inline?)? Inlining at 2 sites would repeat the unfold-and-rearrange; it is a named equation (38) of the source and documents the link between (30) and `γ`. Keep.
- Well-chosen? Yes; optionally the RHS could be the gap form `0 < gam δ n m - eta δ m`, since both callers immediately apply `sub_pos`.
- Conclusion: `KEEP`.

## Mathlibable assessment (Step 9)

Pre-filter: public; name not `_aux`; docstring starts "Inequality (30)"; Step 8 KEEP; namespace-aware grep of `.lake/packages/mathlib/Mathlib/` for `namespace Roth` / `eta_lt_gam_iff`: no hit. Not a glue lemma in the strict sense (needs `grind`, not `rfl`/`Iff.rfl`), so a full run follows. Parent defs `Roth.gam`, `Roth.eta`, `Roth.lam` are all NO-composable-from-mathlib (no re-aim needed).

### Baseline (Phase 0)
- lake build:               clean (project built per brief; not re-run to respect the Lean start-up cost rule; evidence file importing Roth.MainLemma elaborates)
- decl `Roth.eta_lt_gam_iff`: resolved at Roth/MainLemma.lean:100
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  §6 of the source: Roth's main lemma (Lemma 9), its parameters λ, γ, η, B_1, and the pigeonhole step

### Statement (Phase 1)

`Roth.eta_lt_gam_iff` is a theorem stating the following:

For real `δ` and natural `n, m`, put `λ = 4(1+3δ) n √m`, `γ = (m - λ)/2` and `η = 10^m δ^{2^{-m}}`. Then `η + 2(1+3δ) n √m < m/2` if and only if `η < γ`. This is immediate since `γ = m/2 - 2(1+3δ) n √m`.

Variables / typeclasses involved (Lean side):
- `δ : ℝ`: Roth's small parameter.
- `n : ℕ`: degree of the algebraic number.
- `m : ℕ`: number of variables.

Hypotheses (Lean side):
- none.

Conclusion (math): inequality (30) is equivalent to (38) `η < γ`.

Conclusion (Lean): `eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔ eta δ m < gam δ n m`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a one-step algebraic rearrangement relating two forms of a parameter inequality in Roth's proof; not a main result, not named.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line (`grind [gam, lam]`)
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem); note the proof is a single tactic.

### Literature search table — EXHAUSTIVE protocol

| #  | Channel | Query | Hit? | Standard form found | Notes |
|----|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof parameters gamma = (m - lambda)/2 eta < gamma lambda = 4(1+3delta) n sqrt m | no | n/a | hits arXiv 2607.05124, 1302.2299, 2111.12409, Gasarch roth.pdf: all other Roth-type settings or other constants |
| 2 | WebSearch (aliases / book) | Cassels Diophantine approximation Roth's lemma index of polynomial at least (m - lambda)/2 parameter eta | no | n/a | arXiv 2502.00731 (Lemma 3.9, own η), 2004.03331, minru roth.pdf, Evertse Luminy notes; no statement of this rearrangement |
| 3 | WebSearch (general form) | linear inequality rearrangement a + b < c iff a < c - b lemma sub_pos lt_sub_iff_add_lt | yes | `a + b < c ↔ a < c - b` | elementary ordered-group fact; in mathlib as `lt_sub_iff_add_lt` |
| 4 | ChatGPT MCP | n/a | n/a | n/a | `ask_chatgpt_math` MCP not configured in this session (not in the tool list) |
| 5 | Local references | grep clean.tex for "equivalent to", "\eta < \gamma" | yes | l.1355–1359: "Inequality (30) is equivalent to (38) η < γ" | exact match with the Lean statement |
| 6 | nLab | Roth's theorem / parameter inequality | no | n/a | nLab has no entry on proofs of Roth's theorem; the general fact is elementary order algebra, not nLab material |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept |
| 8 | Stacks Project | n/a | n/a | n/a | real-number inequality, not algebraic geometry |
| 9 | MathOverflow / Math.SE | (covered by searches 1–3) | no | n/a | no thread; the general form is a textbook identity |
| 10 | recent arXiv | 2502.00731, 2607.05124, 2111.12409 | no | n/a | each Roth-type proof uses its own parameters |

### Literature summary (Phase 3)

Concept identified as: eq. (38) of the project source; no named concept. General content: `a + b < c ↔ a < c - b` in an ordered additive group.
Sources agree on the standard form: n/a (only the project source states it).
Most general standard form: `lt_sub_iff_add_lt` (ordered additive groups), already in mathlib.
Generality dimensions where the literature varies:
  - constants and shape of λ, γ, η: proof-specific.
Disagreement with the literature: none; matches source eq. (38).

### Generality analysis — `Roth.eta_lt_gam_iff`

Literature-standard form (from Phase 3): source eq. (38); general principle `lt_sub_iff_add_lt`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `δ : ℝ` | any real | `0 < δ` in source | no (already stronger) | no hypothesis on δ at all |
| 2 | `n m : ℕ` | naturals | naturals | no | arguments of the project defs `gam`, `eta` |
| 3 | hypotheses | none | none | no | nothing to drop |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0 (there are no hypotheses)
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of bundled hypotheses? | no | concrete reals | — |
| 2 | Sequences/metric vs filters? | no | no limits | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Set-with-predicate vs bundled? | no | — | — |
| 5 | Field-specific vs typeclass-weakened? | no | `gam`, `eta` are ℝ-valued (sqrt, rpow) | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | `n, m` are counts | — |
| 8 | Concrete-via-abstract? | yes (trivially) | proof unfolds `gam`, `lam` and uses only `a + b < c ↔ a < c - b`; abstract form is `lt_sub_iff_add_lt`, already in mathlib | none new |
| 9 | False-generalisation guard | no false generalisation | no generalisation proposed for mathlib | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no
  - One-line reason: the abstract content is already `lt_sub_iff_add_lt`; the statement is about project-only parameters. (Local-only cosmetic option: RHS `0 < gam δ n m - eta δ m`, see Phase 5.5.)

### Proof strategy — `Roth.eta_lt_gam_iff`

| # | Question | Applies? | Idiomatic alternative | Cost |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | `lt_sub_iff_add_lt` exists | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (single `grind [gam, lam]`; an explicit `rw [gam_eq]; exact lt_sub_iff_add_lt.symm` also compiles, evidence (1))

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.eta_lt_gam_iff`

[A] Lean-Finder       "a + b < c / 2 iff a < (c - 2 b) / 2 for real numbers"   hits: `add_div_two_lt_right`, `left_lt_add_div_two`, `half_lt_self_iff` — averaging lemmas, not this shape
[B] Loogle            `?a + ?b < ?c ↔ ?a < ?c - ?b`   hit: `Nat.add_lt_iff_lt_sub_right` (ℕ only); the ordered-group version is stated in the reversed direction
[C] LeanSearch        "a + b < c iff a < c - b"   hits: `lt_sub_iff_add_lt` (`a < c - b ↔ a + b < c`, AddGroup), `lt_sub_iff_add_lt'`, `tsub_lt_iff_left`
[D] Grep mathlib src  `namespace Roth`, `eta_lt_gam_iff`   no hits
[E] Name pattern      covered by [D] and [C] (`lt_sub_iff_add_lt` resolves in the evidence file)

Searched for both:
  - the user's current form (statement about `gam`/`eta`)
  - the general form (`a + b < c ↔ a < c - b`)

Concluded: found building blocks (`lt_sub_iff_add_lt`); composition with the unfolding identity `gam δ n m = m/2 - 2(1+3δ)n√m` yields our form; the statement itself is project-specific.

### Normal-form check — `Roth.eta_lt_gam_iff`

Equivalent formalisms: `η + 2(1+3δ)n√m < m/2` (30); `η < γ` (38, current RHS); `0 < γ - η` (gap form, used by both callers via `sub_pos`).
Does mathlib already have a canonical form for this idea? no (project defs).
Proposed canonical form: current RHS `η < γ` (the source's (38)); the gap form is an equally cheap local option (compiled, evidence (2)).
RHS convention respected? yes (the named-parameter form is on the RHS).

### Syntactic generality — `Roth.eta_lt_gam_iff`

Alternative restatements attempted:
- current iff with RHS `eta δ m < gam δ n m`
- iff with RHS `0 < gam δ n m - eta δ m` (compiled, evidence (2))
- an equation `gam δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √m` (compiled, evidence (1)), from which both forms follow by `lt_sub_iff_add_lt`

Chosen restatement: current (kept).
Justification: matches source eq. (38) verbatim; the gap form would save one `sub_pos` at each of 2 call sites, cosmetic only.

### Superfluous-argument audit — `Roth.eta_lt_gam_iff`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `δ` | yes | in both sides |
| 2 | `n`, `m` | yes | in both sides |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK (gap form optional locally)
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (locally; not proposed for mathlib)

### Call sites — `Roth.eta_lt_gam_iff`

Internal use count: 2 (outside the declaring file)
External-to-file callers: 1 distinct file (Roth/Main.lean)

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Main.lean:241 | `(sub_pos.mpr ((eta_lt_gam_iff 0 n m).mp (hδ₀' 0 le_rfl hδ₀.le).2)).ne'` (in `Roth.exists_delta`) |
| Roth/Main.lean:560 | `exact ((div_lt_iff₀' (sub_pos.2 ((eta_lt_gam_iff _ _ _).1 h30))).1 h49).not_gt` |

Inline-derivation grep: Roth/Main.lean:244 unfolds `gam, lam, eta` in a `simpa` to evaluate at `δ = 0`, a related but different computation (not a re-derivation of this iff). (none for this statement.)

### Composition check (Phase 6)

Can `Roth.eta_lt_gam_iff` be derived from mathlib in ≤3 chained calls?

Attempt 1: `rw [show gam δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √(m : ℝ) by unfold gam lam; ring]; exact lt_sub_iff_add_lt.symm`
  - Mathlib decls used: `lt_sub_iff_add_lt` (Mathlib/Algebra/Order/Group/Unbundled/Basic.lean), `ring`
  - Result: succeeds (compiled, evidence (1))
  - Notes: the only non-mathlib step is unfolding the project defs; the current proof is the single tactic `grind [gam, lam]`

Conclusion: COMPOSABLE

### Verdict: `Roth.eta_lt_gam_iff`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): only the source's eq. (38) (clean.tex l.1355–1359); general content `a + b < c ↔ a < c - b`.
- Generality analysis (Phase 4): MAXIMALLY GENERAL (no hypotheses).
- Mathlib search (Phase 5): building block `lt_sub_iff_add_lt`; nothing about `gam`/`eta` (project-only defs).
- Composition check (Phase 6): COMPOSABLE (unfold identity plus `lt_sub_iff_add_lt.symm`, compiled).

**Rationale:**

The statement is a rearrangement of a linear inequality, phrased in terms of the project-only parameters `Roth.gam`, `Roth.lam`, `Roth.eta` (all NO-composable-from-mathlib). Once `gam` is unfolded to `m/2 - 2(1+3δ)n√m`, the iff is literally mathlib's `lt_sub_iff_add_lt`; the project proof is one `grind`. There is no mathematical content for mathlib, and mathlib cannot host a statement about Roth's parameters.

WHY not (refactor-actionable): mathlib's `lt_sub_iff_add_lt` is the building block; the project lemma only packages the unfolding of `gam`/`lam`. Belongs-elsewhere check: it belongs in the Roth project, next to `gam` in Roth/MainLemma.lean, as the source's named eq. (38). Deleting it and inlining is possible but not recommended: it would replace one named call at each of the 2 sites with an unfold-and-rearrange.
Mathlib building blocks: `lt_sub_iff_add_lt` (Mathlib/Algebra/Order/Group/Unbundled/Basic.lean), `sub_pos`.
Composition sketch (≤3 lines):
```lean
example (δ : ℝ) (n m : ℕ) : eta δ m + 2 * (1 + 3 * δ) * n * √(m : ℝ) < m / 2 ↔
    eta δ m < gam δ n m := by
  rw [show gam δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √(m : ℝ) by unfold gam lam; ring]
  exact lt_sub_iff_add_lt.symm
```
Call sites in our project (from Phase 6.0): 2 (Roth/Main.lean:241, Roth/Main.lean:560).
Refactor plan: none required. Optional local tidy: restate the RHS as `0 < gam δ n m - eta δ m` (compiled, evidence (2)) and drop the `sub_pos.mpr` / `sub_pos.2` wrapper at Roth/Main.lean:241 and Roth/Main.lean:560.
Next action: keep in Roth/MainLemma.lean; do not upstream.

### Next step

Keep `Roth.eta_lt_gam_iff` project-local in Roth/MainLemma.lean (callers Roth/Main.lean:241, Roth/Main.lean:560); do not upstream. Optionally switch the RHS to the gap form `0 < gam δ n m - eta δ m`.

## Evidence
- WebSearch ×3 (queries in the literature table): no source beyond the project paper states this rearrangement; general fact is `lt_sub_iff_add_lt`.
- Local reference clean.tex l.1355–1359 (eq. (38)).
- lean_leanfinder, lean_leansearch, lean_loogle queries as recorded in Phase 5; grep of `.lake/packages/mathlib/Mathlib/` (no `Roth` hit).
- Evidence file `.mathlib-quality/overview/evidence/Roth.eta_lt_gam_iff/experiments.lean` (imports Roth.MainLemma), checked with `lean_diagnostic_messages`: no errors (one header-linter style warning only). Contains (1) the unfolding identity `gam δ n m = m / 2 - 2 * (1 + 3 * δ) * n * √m` and the composition `rw [gam_eq_evid]; exact lt_sub_iff_add_lt.symm`; (2) the gap-form restatement `… ↔ 0 < gam δ n m - eta δ m` from `eta_lt_gam_iff` and `sub_pos`.
