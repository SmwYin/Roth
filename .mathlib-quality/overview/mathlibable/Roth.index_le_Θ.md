---
decl: Roth.index_le_Θ
file: Roth/Theta.lean
line: 99
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The le_csSup intro lemma for the project-local supremum Θ, proved as one call of mathlib's le_csSup with indexSet_bddAbove and a membership witness (compiled); it is about a Roth-proof-specific quantity, so there is nothing to upstream, but it is the named API that 3 call sites use.
action: Do not upstream; keep in Roth/Theta.lean as the basic Θ API lemma (callers index_separated_mul_le_aux at Theta.lean:443 and 445, main_lemma at MainLemma.lean:760); no call-site changes.
---

# Roth.index_le_Θ

## Inventory entry

### `theorem Roth.index_le_Θ`
- **Type**: `∀ {σ : Type*} [Fintype σ] {B : ℝ} {q r : σ → ℕ} {R : MvPolynomial σ ℤ}, R ∈ RSet B r → ∀ {h : σ → ℤ}, (∀ j, IsCoprime (h j) (q j : ℤ)) → index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r`
- **What**: Take any `R ∈ ℛ_m(B; r)` and any point `(h_j/q_j)_j` with each `h_j` coprime to `q_j`. The index of `R` at that point, relative to `r`, is at most `Θ_m(B; q; r)`. This is the "a member is at most the supremum" property of `Θ`.
- **How**: `le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩`. This is mathlib's `le_csSup`, given the project's `BddAbove` lemma and the anonymous-constructor witness of membership in `indexSet`.
- **Hypotheses**: `hR : R ∈ RSet B r` and `hh : ∀ j, IsCoprime (h j) (q j)`. Both are needed to build the membership witness. There is no `1 ≤ B` hypothesis, because `le_csSup` needs only `BddAbove`, not `Nonempty`. The section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.Θ`, `Roth.indexSet`, `Roth.RSet`, `Roth.index`, `Roth.indexSet_bddAbove`
- **Used by**: Roth/Theta.lean:443 and 445 (private `index_separated_mul_le_aux`, which feeds Lemma 6, as `hUΘ` and `hVΘ`); Roth/MainLemma.lean:760 (`main_lemma`, `linarith only [hgap, index_le_Θ hW hh]`). Found with `grep -rn index_le_Θ Roth/`.
- **Visibility**: public
- **Lines**: 95–102 (docstring 96–98, statement 99–101, proof 102), proof length 1 line
- **Notes**: Source: clean.tex §5 l.655–670 (definition of `Θ_m` as a supremum). The Lean note at l.700–702 asks for "lemmas for bounding an individual index", and this is that lemma.

## Junk check (Step 8)
- **Used anywhere?** Yes, 3 times in 2 files (Theta.lean twice, MainLemma.lean once).
- **Wrapper of 1–2 mathlib calls?** Yes. It is one `le_csSup` call plus the project's `indexSet_bddAbove`. Inlining it would make each of the 3 callers write `le_csSup (indexSet_bddAbove _ _) ⟨_, hR, _, hh, rfl⟩`, which exposes `indexSet`'s existential shape at the call sites. It is the standard named intro lemma for a `sSup`-defined quantity, like `le_ciSup` for `⨆`, so keeping it is better.
- **Does mathlib have it?** No. It concerns the project's `Θ`. The generic content is `le_csSup`.
- **Too specific (inline?)?** No. It is the basic API of `Θ`, and it keeps callers independent of how `indexSet` is defined.
- **Well-chosen?** Yes. It takes unbundled `hR`/`hh`, which is the easiest shape to supply at the call sites.
- **Conclusion:** `KEEP`. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The lemma is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- The qualified name is absent from mathlib: there is no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`.

This is not a glue lemma in the brief's sense. The body is `le_csSup …`, a real (if one-step) mathlib lemma application, not `rfl`, `Iff.rfl` or pure unfolding. A full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors)
- decl `Roth.index_le_Θ`:    resolved at Roth/Theta.lean:99
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.index_le_Θ` is a theorem stating the following.

Let `R ∈ ℤ[X_j : j ∈ σ]` be nonzero, with `deg_{X_j} R ≤ r_j` and every coefficient of absolute value at most `B`. Let `h ∈ ℤ^σ` with `gcd(h_j, q_j) = 1` for all `j`. Then the index `ind(R; (h_j/q_j)_j; r)` is at most `Θ_m(B; q; r)`, where `Θ_m` is defined as the supremum of exactly these indices.

Variables / typeclasses involved (Lean side):
- `σ` with `[Fintype σ]`: the variables.
- `B`: the coefficient bound.
- `q`: the denominators.
- `r`: the degree bounds and index weights.
- `R`: the polynomial.
- `h`: the numerators.

Hypotheses (Lean side):
- `hR : R ∈ RSet B r`: `R` is admissible (nonzero, degree box, height bound).
- `hh : ∀ j, IsCoprime (h j) (q j)`: each point coordinate has exact denominator `q_j`.

Conclusion (math): `ind(R; h/q; r) ≤ Θ_m(B; q; r)`.

Conclusion (Lean): `index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: the definitional upper-bound property of a supremum; an API lemma, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem); recorded that the proof is a single `le_csSup` term.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof index of polynomial at most Theta_m supremum ind(R; h/q; r) ≤ Θ_m(B; q; r) | yes | Yamada (arXiv math/0307203 §2) defines `Θ_m` as the supremum of the index over `ℛ_m(B; r)`. The inequality is immediate from that definition and is not stated as a separate lemma | tacit in the literature |
| 2 | WebSearch (general form) | element of a set bounded above is at most its supremum le_csSup conditionally complete lattice | yes | `a ∈ s`, `s` bounded above, gives `a ≤ sup s` (mathlib `le_csSup`) | the entire mathematical content |
| 3 | WebSearch (named-after / aliases) | Cassels Ridout lemma index of polynomial bounded height rational point Theta bound Roth's lemma induction | partial | Ridout's bound `Θ < 10^m δ^{(1/2)^m}` (math/0307203 Lemma 2.1); Evertse (arXiv 2502.00731) states Roth's lemma pointwise | no named statement for "index ≤ Θ" |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "supremum", "individual index" | yes | clean.tex l.660: `Θ_m` is "the supremum of the numbers ind(R; …)". l.700–702 is the Lean note asking for "lemmas for bounding an individual index" | this lemma is exactly that |
| 6 | nLab | supremum | partial | the generic order-theoretic supremum (least upper bound) | nothing Roth-specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an inequality between reals) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; Stacks has no index-of-a-polynomial-at-a-point notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary for a thread |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), from searches 1 and 3 | partial | pointwise Roth's lemma | no supremum, so no analogue of this lemma |

### Literature summary (Phase 3)

Concept identified as: the upper-bound property of the supremum `Θ_m(B; q; r)` from the Ridout/Cassels presentation of Roth's lemma.
Sources agree on the standard form: yes. The fact is tacit, true by the definition of the supremum.
Most general standard form: every member of a set that is bounded above is `≤` its supremum (`le_csSup`).
Generality dimensions where the literature varies: none relevant.
Disagreement with the literature: none.

### Generality analysis — `Roth.index_le_Θ`

Literature-standard form: `a ∈ s → BddAbove s → a ≤ sSup s`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hR : R ∈ RSet B r` | required | `R ∈ ℛ_m(B; r)` | NO | needed for membership in `indexSet`. For `R ∉ RSet` (for example a polynomial of too large height) the index can exceed `Θ` |
| 2 | `hh : ∀ j, IsCoprime …` | required | `gcd(h_j, q_j) = 1` | NO | needed for membership; points with a smaller exact denominator are not in the family |
| 3 | `1 ≤ B` | not taken | paper assumes `B ≥ 1` | already weaker | `le_csSup` needs only `BddAbove`; the hypothesis `hR` itself forces the family to be nonempty |
| 4 | `[DecidableEq σ]` | omitted | n/a | already absent | evidence (3) |
| 5 | unbundled vs set-membership | unbundled `R, hR, h, hh` | `x ∈ indexSet → x ≤ Θ` | equivalent | evidence (2): also a one-line `le_csSup`; the unbundled form suits the callers |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. Every hypothesis is used to build the membership witness, and there are no extra assumptions.
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | the hypotheses are data-specific | — |
| 2 | Sequences vs filters? | no | an order inequality | — |
| 3 | Construction vs universal property? | no | it already is the universal-property (upper bound) half of `sSup` | — |
| 4 | Bundled substructure? | no | `indexSet` is a plain set of reals | — |
| 5 | Field-specific vs typeclass-weakened? | no | ℝ-valued by the definition of `index` | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | arbitrary finite `σ` already | — |
| 8 | Concrete-via-abstract? | yes, trivially | after the membership witness, the proof is pure `le_csSup`; the abstract form already exists in mathlib | none (the abstraction is `le_csSup` itself) |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the abstract content is exactly mathlib's `le_csSup`; nothing remains to modernise.

### Proof strategy — `Roth.index_le_Θ`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | no | `le_csSup` covers it | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a single `le_csSup` term).

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.index_le_Θ`

[A] Lean-Finder       "an element of a nonempty set of reals bounded above is at most the supremum"   hits: `le_csSup`, `Real.isLUB_sSup`, `Real.sSup_le`, `ConditionallyCompleteLattice.le_csSup`, `le_csSup_of_le` (building blocks)
[B] Loogle            `BddAbove ?s → ?a ∈ ?s → ?a ≤ sSup ?s`   hits: `le_csSup`, `DirectedOn.le_csSup`
[C] LeanSearch        "index of a polynomial at a rational point is bounded by the supremum over polynomials with bounded coefficients"   hits: `one_le_pow_mul_abs_eval_div`, `Polynomial.cauchyBound`, `MvPolynomial.schwartz_zippel_sup_sum` (unrelated)
[D] Grep mathlib src  `namespace Roth` (no hits); `def Θ` (no hits)
[E] Name pattern      `le_csSup` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean); `index_le_Θ` (project only)

Searched for both:
  - the user's form (index ≤ Θ for admissible `R` and `h`)
  - the literature-standard form (member ≤ supremum): this is `le_csSup`

Concluded: found building blocks (`le_csSup`, plus the project's `indexSet_bddAbove`); composition gives our form.

### Normal-form check — `Roth.index_le_Θ`

Equivalent formalisms:
- unbundled (current)
- `x ∈ indexSet B q r → x ≤ Θ B q r` (evidence (2))
- `IsLUB`-based

Does mathlib already have a canonical form? Yes: `le_csSup`. Our statement is its instance.
RHS convention respected? n/a (not an iff).

### Syntactic generality — `Roth.index_le_Θ`

Alternative restatements attempted:
- unbundled (current)
- set-membership form (evidence (2))

Chosen restatement: unbundled (current).
Justification: all 3 callers have `hR`/`hh` in hand and never mention `indexSet`. The membership form would force them to build `⟨R, hR, h, hh, rfl⟩` themselves.

### Superfluous-argument audit — `Roth.index_le_Θ`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hR` | yes | membership |
| 2 | `hh` | yes | membership |
| 3 | `[Fintype σ]` | yes | needed by `index` and `Θ` |
| 4 | `[DecidableEq σ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.index_le_Θ`

Internal use count: 1 outside the declaring file (Roth/MainLemma.lean), plus 2 inside Roth/Theta.lean.
External-to-file callers: 1 distinct file

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:443 | `have hUΘ := index_le_Θ hU (h := h ∘ some)` (private `index_separated_mul_le_aux`) |
| Roth/Theta.lean:445 | `have hVΘ := index_le_Θ hVmem (q := fun _ : Unit ↦ q none) (h := fun _ ↦ h none) …` (same lemma) |
| Roth/MainLemma.lean:760 | `linarith only [hgap, index_le_Θ hW hh]` (`main_lemma`) |

Inline-derivation grep:
  - (none). The only other `le_csSup` use in `Roth/` is the lemma itself (`grep -rn le_csSup Roth/`). `Θ_mono` uses `csSup_le_csSup`, which is a different fact.

### Composition check (Phase 6)

Can `Roth.index_le_Θ` be derived from mathlib in ≤3 chained calls?

Attempt 1: `le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩`
  - Decls used: mathlib `le_csSup`; project `Roth.indexSet_bddAbove`; the anonymous constructor for `indexSet` membership.
  - Result: succeeds (this is the current proof; recompiled as evidence (1)).
  - Notes: one mathlib call.

Conclusion: COMPOSABLE

## Verdict: `Roth.index_le_Θ`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** the fact is tacit, true by the definition of `Θ_m` as a supremum (clean.tex l.660, Yamada math/0307203 §2). The general content is "member ≤ supremum".
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. Both hypotheses are needed for membership, and there is no `1 ≤ B` assumption (evidence (1)).
- **Mathlib search (Phase 5):** building block `le_csSup` (Loogle and Lean-Finder hits). There is no `Roth` namespace in mathlib.
- **Composition check (Phase 6):** COMPOSABLE as one `le_csSup` call (evidence (1)).

**Rationale:**

`Roth.index_le_Θ` is mathlib's `le_csSup`, specialised to the project-local carrier `Roth.indexSet` with its `BddAbove` lemma `Roth.indexSet_bddAbove`. Both of those, and `Roth.Θ` itself, are NO-composable-from-mathlib: they are bookkeeping objects of the Ridout/Cassels proof of Roth's lemma. The only general mathematics here is "an element of a set bounded above is at most its supremum", which mathlib already has. There is nothing to upstream.

WHY not: it is a single mathlib call (`le_csSup`) about a Roth-proof-specific supremum that will never be in mathlib.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean. It is the intro lemma of `Θ`'s API, as `le_ciSup` is for `⨆`, and the Lean note in clean.tex l.700–702 asks for it. The bucket's usual "inline at call sites" step is not recommended. Inlining would repeat `le_csSup (indexSet_bddAbove _ _) ⟨_, hR, _, hh, rfl⟩` at the 3 callers, tie them to the internal shape of `indexSet`, and lose the paper-facing name.

Mathlib building blocks:
- `le_csSup` (Mathlib/Order/ConditionallyCompleteLattice/Basic.lean)
- project `Roth.indexSet_bddAbove` (Roth/Theta.lean)

Composition sketch (≤3 lines):
```lean
example (hR : R ∈ RSet B r) (hh : ∀ j, IsCoprime (h j) (q j : ℤ)) :
    index (map (Int.castRingHom ℝ) R) (fun j ↦ (h j : ℝ) / q j) r ≤ Θ B q r :=
  le_csSup (indexSet_bddAbove B q) ⟨R, hR, h, hh, rfl⟩
```

Call sites in our project (from Phase 6.0): 3, at Roth/Theta.lean:443, Roth/Theta.lean:445 and Roth/MainLemma.lean:760.

Refactor plan: none. Keep the lemma; leave the 3 call sites unchanged. If the call sites were ever inlined, each would become `le_csSup (indexSet_bddAbove _ _) ⟨_, hR, _, hh, rfl⟩` with explicit `q`/`h` as at 445, but this is not recommended.

Next action: no upstreaming; keep the lemma as the basic `Θ` API.

## Next step

No upstreaming. Keep `Roth.index_le_Θ` in Roth/Theta.lean as the intro lemma of the `Θ` API. Any reusable content (a weighted order of vanishing at a point) is tracked under `Roth.index`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.index_le_Θ/composition.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports no errors, only a header-linter warning about a missing module docstring and the `#check` info. It contains:
  - (1) the statement proved by one `le_csSup` call;
  - (2) the set-membership form `x ∈ indexSet B q r → x ≤ Θ B q r` via `le_csSup`;
  - (3) `#check @index_le_Θ`, confirming the signature uses only `[Fintype σ]`.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, and mathlib doc mirrors for `le_csSup`.
- Lean-Finder, Loogle and LeanSearch queries as recorded in Phase 5. A grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth`.
- Local refs: clean.tex l.655–670 and l.700–702.
- `grep -rn index_le_Θ Roth/` and `grep -rn le_csSup Roth/` for the call-sites table.
- Parent reports Roth.Θ.md and Roth.indexSet_bddAbove.md were reused.
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
