---
decl: Roth.Θ_le_of_forall_index_le
file: Roth/Theta.lean
line: 124
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The csSup_le elimination lemma for the project-local supremum Θ, proved as one call of mathlib's csSup_le with indexSet_nonempty and destructuring of indexSet membership (compiled); it is about a Roth-proof-specific quantity, so there is nothing to upstream, but it is the named API that Lemmas 5 and 6 use.
action: Do not upstream; keep in Roth/Theta.lean as the basic upper-bound API lemma of Θ (callers Θ_unique_le at Theta.lean:258 and Θ_option_le at Theta.lean:599); no call-site changes.
---

# Roth.Θ_le_of_forall_index_le

## Inventory entry

### `theorem Roth.Θ_le_of_forall_index_le`
- **Type**: `∀ {σ : Type*} [Fintype σ] {B : ℝ}, 1 ≤ B → ∀ {q r : σ → ℕ} {c : ℝ}, (∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) → index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) → Θ B q r ≤ c`
- **What**: Suppose `B ≥ 1` and `c` bounds the index `ind(R; (h_j/q_j)_j; r)` for every `R ∈ ℛ_m(B; r)` and every `h` with each `h_j` coprime to `q_j`. Then `Θ_m(B; q; r) ≤ c`. This is the "the supremum is the least upper bound" property of `Θ`, the counterpart of `index_le_Θ`.
- **How**: `csSup_le (indexSet_nonempty hB q r)`, then `rintro _ ⟨R, hR, h, hh, rfl⟩; exact hc R hR h hh`. This is mathlib's `csSup_le`, with nonemptiness from the project's `indexSet_nonempty` and the bound obtained by destructuring membership in `indexSet`.
- **Hypotheses**: `hB : 1 ≤ B`, which makes `indexSet B q r` nonempty (it contains the index of the constant polynomial `1`). `hc` gives the pointwise bound. The section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet`, `Roth.index`, `Roth.indexSet_nonempty`
- **Used by**: Roth/Theta.lean:258 (`Θ_unique_le`, Lemma 5) and Roth/Theta.lean:599 (`Θ_option_le`, Lemma 6). Found with `grep -rn Θ_le_of_forall_index_le Roth/`. There are no uses outside Theta.lean.
- **Visibility**: public
- **Lines**: 121–129 (docstring 122–123, statement 124–126, proof 127–129), proof length 3 lines
- **Notes**: Source: clean.tex l.692 (proof of Lemma 5: "Taking the supremum proves the claim"). Lemma 6 makes the same move.

## Junk check (Step 8)
- **Used anywhere?** Yes, twice in Roth/Theta.lean (Lemmas 5 and 6).
- **Wrapper of 1–2 mathlib calls?** Yes. It is one `csSup_le` call plus the project's `indexSet_nonempty` and a destructuring of `indexSet` membership. Inlining it would make both callers write `csSup_le (indexSet_nonempty hB q r) fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ …`, which exposes the existential shape of `indexSet`. It is the standard named elimination lemma for a `sSup`-defined quantity, like `ciSup_le` for `⨆`, and it pairs with `index_le_Θ`. Keeping it is better.
- **Does mathlib have it?** No. It concerns the project's `Θ`. The generic content is `csSup_le`, or `Real.sSup_le`.
- **Too specific (inline?)?** No. Together with `index_le_Θ` it is the basic API of `Θ`, and it keeps callers independent of how `indexSet` is defined.
- **Well-chosen?** Yes. The quantified hypothesis `hc` is unbundled, so callers write `fun R hR h hh ↦ …` directly.
- **Conclusion:** `KEEP`. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib: there is no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`.

This is not a glue lemma in the brief's sense. The body applies a mathlib lemma (`csSup_le`) and destructures membership; it is not `rfl`, `Iff.rfl` or pure unfolding. A full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors or warnings)
- decl `Roth.Θ_le_of_forall_index_le`:    resolved at Roth/Theta.lean:124
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.Θ_le_of_forall_index_le` is a theorem stating the following.

Let `B ≥ 1` and `c ∈ ℝ`. Suppose that for every nonzero `R ∈ ℤ[X_j : j ∈ σ]` with `deg_{X_j} R ≤ r_j` and coefficients bounded by `B`, and for every `h ∈ ℤ^σ` with `gcd(h_j, q_j) = 1`, we have `ind(R; (h_j/q_j)_j; r) ≤ c`. Then `Θ_m(B; q; r) ≤ c`.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables.
- `B`: the coefficient bound.
- `q`: the denominators.
- `r`: the degree bounds and index weights.
- `c`: the candidate upper bound.

Hypotheses (Lean side):
- `hB : 1 ≤ B`: guarantees the family is nonempty.
- `hc`: the pointwise index bound over all admissible `R` and `h`.

Conclusion (math): `Θ_m(B; q; r) ≤ c`.

Conclusion (Lean): `Θ B q r ≤ c`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the least-upper-bound property of a supremum; an API lemma, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem); recorded that the proof is `csSup_le` plus destructuring.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem Ridout Theta_m(B; q; r) supremum of index bound every index "taking the supremum" | partial | Yamada (arXiv math/0307203) follows Ridout's index set-up, but the hit does not state the "bound every index, so bound Θ" step separately | tacit in the literature |
| 2 | WebSearch (general form) | csSup_le nonempty set every element at most c then supremum at most c conditionally complete lattice | yes | `s` nonempty and every `b ∈ s` satisfies `b ≤ a`, so `sup s ≤ a` (mathlib `csSup_le`) | the entire mathematical content; the docs note that nonemptiness is essential |
| 3 | WebSearch (named-after / aliases) | Cassels introduction to Diophantine approximation Roth lemma index of polynomial at rational point bounded height Theta | partial | Ridout's bound `Θ_m ≤ 10^m δ^{(1/2)^m}` (math/0307203); Evertse (arXiv 2502.00731) defines the index and states Roth's lemma | no named statement for this step |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "Taking the supremum" | yes | clean.tex l.692, end of the proof of Lemma 5: the paper bounds each index, then takes the supremum | this lemma is exactly that step |
| 6 | nLab | supremum (least upper bound) | partial | the generic order-theoretic definition: the supremum is below every upper bound | nothing Roth-specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an inequality between reals) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; Stacks has no index-of-a-polynomial notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary for a thread |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), from search 3 | partial | pointwise Roth's lemma | no supremum, so no analogue of this lemma |

### Literature summary (Phase 3)

Concept identified as: the least-upper-bound property of the supremum `Θ_m(B; q; r)` from the Ridout/Cassels presentation of Roth's lemma.
Sources agree on the standard form: yes. The fact is tacit ("taking the supremum").
Most general standard form: a nonempty set with upper bound `c` has supremum `≤ c` (`csSup_le`). In `ℝ` with the convention `sSup ∅ = 0`, the alternative is `0 ≤ c` (`Real.sSup_le`).
Generality dimensions where the literature varies: none relevant. The paper assumes `B ≥ 1` throughout §5.
Disagreement with the literature: none.

### Generality analysis — `Roth.Θ_le_of_forall_index_le`

Literature-standard form: `s.Nonempty → (∀ b ∈ s, b ≤ c) → sSup s ≤ c`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hB : 1 ≤ B` | required | paper's standing `B ≥ 1` | NO (only an incomparable alternative) | It cannot simply be dropped. For `B < 1`, `RSet B r = ∅`, so `Θ = 0` (evidence (3)), and the hypothesis-free statement would prove `0 ≤ -1`. The alternative `0 ≤ c` also works via `Real.sSup_le` (evidence (2)), but it is incomparable with `1 ≤ B`, not weaker. Both callers have `hB` in hand, so the current form fits them. |
| 2 | `hc` | required | `∀ b ∈ s, b ≤ c` | NO | this is the content of the lemma |
| 3 | `[DecidableEq σ]` | omitted | n/a | already absent | evidence (4) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. The only candidate change, `1 ≤ B` → `0 ≤ c`, compiles (evidence (2)) but is incomparable, not a weakening. A disjunction `1 ≤ B ∨ 0 ≤ c` would be strictly more general, but no caller needs it.
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | the hypotheses are data-specific | — |
| 2 | Sequences vs filters? | no | an order inequality | — |
| 3 | Construction vs universal property? | no | it already is the least-upper-bound half of `sSup` | — |
| 4 | Bundled substructure? | no | `indexSet` is a plain set of reals | — |
| 5 | Field-specific vs typeclass-weakened? | no | ℝ-valued by the definition of `index` | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | arbitrary finite `σ` already | — |
| 8 | Concrete-via-abstract? | yes, trivially | after destructuring, the proof is pure `csSup_le`; the abstract form already exists in mathlib | none (the abstraction is `csSup_le` itself) |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the abstract content is exactly mathlib's `csSup_le`; nothing remains to modernise.

### Proof strategy — `Roth.Θ_le_of_forall_index_le`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | no | `csSup_le` covers it | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (`csSup_le` plus `rintro` destructuring; it could also be written as a single term, evidence (1)).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_le_of_forall_index_le`

[A] Lean-Finder       "if every element of a nonempty set of reals is at most c then the supremum is at most c"   hits: `Real.sSup_le`, `Real.iSup_le`, `csSup_le`, `ciSup_le`, `csSup_le_iff` (building blocks)
[B] Loogle            `Set.Nonempty ?s → (∀ b ∈ ?s, b ≤ ?a) → sSup ?s ≤ ?a`   hits: `csSup_le`, `DirectedOn.csSup_le`
[C] LeanSearch        "supremum of indices of integer polynomials with bounded coefficients at rational points is at most a common bound"   hits: `iSup`, `Polynomial.cauchyBound_zero`, `Seminorm.finset_sup_apply_le` (unrelated)
[D] Grep mathlib src  `namespace Roth` (no hits); `theorem csSup_le ` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:201)
[E] Name pattern      `csSup_le`, `Real.sSup_le` (mathlib); `Θ_le_of_forall_index_le` (project only)

Searched for both:
  - the user's form (Θ ≤ c from pointwise index bounds)
  - the literature-standard form (nonempty set with upper bound c has sup ≤ c): this is `csSup_le`

Concluded: found building blocks (`csSup_le`, plus the project's `indexSet_nonempty`); composition gives our form.

### Normal-form check — `Roth.Θ_le_of_forall_index_le`

Equivalent formalisms:
- unbundled pointwise bound (current)
- `(∀ x ∈ indexSet B q r, x ≤ c) → Θ B q r ≤ c`
- `c ∈ upperBounds (indexSet B q r)`
- the iff form `Θ B q r ≤ c ↔ ∀ …` (via `csSup_le_iff` with `indexSet_bddAbove`)

Does mathlib already have a canonical form? Yes: `csSup_le`. Our statement is its instance.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.Θ_le_of_forall_index_le`

Alternative restatements attempted:
- unbundled (current)
- set-membership / `upperBounds` form
- iff form

Chosen restatement: unbundled (current).
Justification: both callers supply `fun R hR h hh ↦ …` directly and never mention `indexSet`. An iff form would be a nice-to-have, but no caller needs the reverse direction.

### Superfluous-argument audit — `Roth.Θ_le_of_forall_index_le`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hB` | yes | needed for nonemptiness; the conclusion fails without it (evidence (3)) |
| 2 | `hc` | yes | content |
| 3 | `[Fintype σ]` | yes | needed by `index` and `Θ` |
| 4 | `[DecidableEq σ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.Θ_le_of_forall_index_le`

Internal use count: 0 outside the declaring file, 2 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:258 | `Θ_le_of_forall_index_le hB fun _ hR _ hh ↦ index_unique_le_log_div hq hR.1 …` (`Θ_unique_le`, Lemma 5) |
| Roth/Theta.lean:599 | `refine Θ_le_of_forall_index_le hB fun R hR h hh ↦ ?_` (`Θ_option_le`, Lemma 6) |

Inline-derivation grep:
  - (none). `grep -rn "csSup_le\|Real.sSup_le" Roth/` finds only the lemma itself (Theta.lean:127), `Θ_le_card` (Theta.lean:115, `Real.sSup_le`, which bounds by `card σ ≥ 0` without needing `1 ≤ B`) and `Θ_mono` (Theta.lean:136, `csSup_le_csSup`). Each of these proves a different fact.

### Composition check (Phase 6)

Can `Roth.Θ_le_of_forall_index_le` be derived from mathlib in ≤3 chained calls?

Attempt 1: `csSup_le (indexSet_nonempty hB q r) fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ hc R hR h hh`
  - Decls used: mathlib `csSup_le`; project `Roth.indexSet_nonempty`; anonymous-constructor destructuring of `indexSet` membership.
  - Result: succeeds (evidence (1)).
  - Notes: one mathlib call.

Attempt 2: `Real.sSup_le (fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ hc R hR h hh) hc0`, with `0 ≤ c` in place of `1 ≤ B`.
  - Result: succeeds (evidence (2)). This is an alternative side condition.

Conclusion: COMPOSABLE

## Verdict: `Roth.Θ_le_of_forall_index_le`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** the fact is tacit: "Taking the supremum proves the claim" (clean.tex l.692). The general content is "a nonempty set with upper bound c has supremum ≤ c".
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. `1 ≤ B` is needed (evidence (3)); its only alternative, `0 ≤ c`, is incomparable (evidence (2)).
- **Mathlib search (Phase 5):** building blocks `csSup_le` and `Real.sSup_le` (Loogle and Lean-Finder hits). There is no `Roth` namespace in mathlib.
- **Composition check (Phase 6):** COMPOSABLE as one `csSup_le` call (evidence (1)).

**Rationale:**

`Roth.Θ_le_of_forall_index_le` is mathlib's `csSup_le`, specialised to the project-local carrier `Roth.indexSet` with its nonemptiness lemma `Roth.indexSet_nonempty`. Both of those, and `Roth.Θ` itself, are NO-composable-from-mathlib: they are bookkeeping objects of the Ridout/Cassels proof of Roth's lemma. The only general mathematics here is "a nonempty set with upper bound c has supremum ≤ c", which mathlib already has. There is nothing to upstream.

WHY not: it is a single mathlib call (`csSup_le`) about a Roth-proof-specific supremum that will never be in mathlib.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean. It is the elimination lemma of `Θ`'s API, paired with `index_le_Θ` as `ciSup_le` is paired with `le_ciSup`. The bucket's usual "inline at call sites" step is not recommended. Inlining would repeat `csSup_le (indexSet_nonempty hB q r) fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ …` at the 2 callers, tie them to the internal shape of `indexSet`, and lose the paper-facing name.

Mathlib building blocks:
- `csSup_le` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean:201)
- alternatively `Real.sSup_le` (Mathlib/Data/Real/Archimedean.lean)
- project `Roth.indexSet_nonempty` (Roth/Theta.lean)

Composition sketch (≤3 lines):
```lean
example (hB : 1 ≤ B) (hc : ∀ R ∈ RSet B r, ∀ h : σ → ℤ, (∀ j, IsCoprime (h j) (q j : ℤ)) →
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ c) : Θ B q r ≤ c :=
  csSup_le (indexSet_nonempty hB q r) fun _ ⟨R, hR, h, hh, hx⟩ ↦ hx ▸ hc R hR h hh
```

Call sites in our project (from Phase 6.0): 2, at Roth/Theta.lean:258 and Roth/Theta.lean:599.

Refactor plan: none. Keep the lemma; leave both call sites unchanged. If they were ever inlined, each would become the `csSup_le (indexSet_nonempty hB q r) …` term above, but this is not recommended.

Next action: no upstreaming; keep the lemma as the basic `Θ` API.

## Next step

No upstreaming. Keep `Roth.Θ_le_of_forall_index_le` in Roth/Theta.lean as the elimination lemma of the `Θ` API. An optional polish is to give the proof as the single term from evidence (1). Any reusable content (a weighted order of vanishing at a point) is tracked under `Roth.index`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ_le_of_forall_index_le/composition.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports success with no errors or warnings, only the `#check` info. It contains:
  - (1) the statement proved by a one-term `csSup_le` composition;
  - (2) the variant with `0 ≤ c` in place of `1 ≤ B`, via `Real.sSup_le`;
  - (3) `Θ (1/2) q r = 0`, showing that `RSet B r` is empty for `B < 1`, so `hB` cannot simply be dropped;
  - (4) `#check @Θ_le_of_forall_index_le`, confirming the signature uses only `[Fintype σ]`.
  An earlier draft of (3) failed (`simp` normalised `1/2` to `2⁻¹` before using the emptiness fact). It was fixed to `rw [Θ, this, Real.sSup_empty]`.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, and mathlib doc mirrors for `csSup_le`.
- Lean-Finder, Loogle and LeanSearch queries as recorded in Phase 5. A grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth`.
- Local refs: clean.tex l.684–693 (proof of Lemma 5).
- `grep -rn Θ_le_of_forall_index_le Roth/` and `grep -rn "csSup_le\|Real.sSup_le" Roth/` for the call-sites table.
- Parent reports Roth.Θ.md and Roth.index_le_Θ.md were reused.
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
