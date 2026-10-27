---
decl: Roth.lem6M_lt
file: Roth/Theta.lean
line: 649
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: The Lemma 7 estimate M < q1^(delta(1+1/p) l r1) for the project-local Lemma 6 constant lem6M with B = q1^(delta r1) (clean.tex l.973-981); a 4-step real-arithmetic chain through two private aux lemmas, with no literature standing and no mathlib counterpart, and not a 3-call mathlib composition; recommended resolution is to keep it project-local (a compiled weakening to real q1 and l at most 2^r1 exists but buys nothing at the single call site).
action: Keep in Roth/Theta.lean (single caller private theta_phi_lt_aux at Roth/Theta.lean:871); optionally make it private or adopt the weakened signature of evidence/Roth.lem6M_lt/weaken.lean; do not upstream.
---

# Roth.lem6M_lt

## Inventory entry

### `theorem Roth.lem6M_lt`
- **Type**: `{p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ q₁ : ℕ} (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁) {l : ℕ} (hl : 1 ≤ l) (hl' : l ≤ r₁) : lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁))`
- **What**: If `log q₁ ≥ p(2p+1)/δ` and `1 ≤ l ≤ r₁`, then the Lemma 6 constant `M = (r₁+1)^{pl} l! 2^{plr₁} B^l` with `B = q₁^{δ r₁}` satisfies `M < q₁^{δ₁ l r₁}` where `δ₁ = δ(1 + 1/p)`.
- **How**: Shows `q₁ > 0` from the log hypothesis (`Real.log_pos_iff`). Bounds the non-`B` factors by `2^{(2p+1) r₁ l}` using private `factorial_coefficient_le_two_pow_aux` (cast with `exact_mod_cast`, with `l ≤ 2^{r₁}` from `Nat.lt_two_pow_self`). Then uses private `two_pow_lt_rpow_aux` for `2^{(2p+1) r₁ l} < q₁^{(δ/p) l r₁}`, and merges exponents with `Real.rpow_mul_natCast` and `Real.rpow_add`. The chain is a 4-step `calc`.
- **Hypotheses**: `hp` (p > 0, divides by p); `hδ0`; `hq₁` (forces `q₁ > 1` and gives `2p+1 ≤ (δ/p) log q₁`); `hl` (needed for strictness, since at `l = 0` both sides equal 1); `hl'` (only used to get `l ≤ 2^{r₁}` and `r₁ > 0`).
- **Uses from project**: `Roth.lem6M`, `Roth.factorial_coefficient_le_two_pow_aux` (private), `Roth.two_pow_lt_rpow_aux` (private)
- **Used by**: `Roth.theta_phi_lt_aux` (private) at Roth/Theta.lean:871; no other uses in `Roth/`
- **Visibility**: public
- **Lines**: 646–667 (statement 649–651, proof 652–667, proof length 16 lines)
- **Notes**: Source is clean.tex §5, proof of Lemma 7, l.973–981. The docstring cites it correctly.

## Junk check (Step 8)
- **Used anywhere?** Yes. It has one caller, the private `theta_phi_lt_aux` (Theta.lean:871), which is the Lemma 7 induction step.
- **Wrapper of 1–2 mathlib calls?** No. It is a 4-step `calc` over two project helper lemmas plus rpow algebra.
- **Does mathlib have it?** No. It is about the project constant `lem6M`. LeanFinder, LeanSearch and Loogle return only unrelated hits (Behrend bounds and the generic `Real.lt_rpow_of_log_lt`).
- **Too specific (inline?)?** It is specific to the proof, but it isolates a clearly named estimate from the paper ("M < q₁^{δ₁ l r₁}"). Inlining it into the already long `theta_phi_lt_aux` would hurt readability.
- **Well-chosen?** Yes. It mirrors the paper. It could be `private`, since its only caller is private.

Conclusion: **KEEP**. Optionally make it `private`.

## Mathlibable assessment (Step 9)

Pre-filter: none of the filters fire.
- It is public.
- The name has no `_aux` suffix.
- The docstring does not start with internal/auxiliary.
- Step 8 said KEEP.
- `grep -rn lem6M .lake/packages/mathlib/Mathlib` finds nothing.
- It is not a glue lemma, because it has a real proof. INHERITED therefore does not apply.

Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built; the evidence file importing `Roth.Theta` compiles)
- decl `Roth.lem6M_lt`:      ✓ resolved at Roth/Theta.lean:649
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)` (supremum of indices of bounded integer polynomials at rational points) and Lemmas 5, 6, 7 bounding it

### Statement (Phase 1)

`Roth.lem6M_lt` is a theorem stating the following. Let `p ≥ 1`, `δ > 0`, and `q₁ ∈ ℕ` with `log q₁ ≥ p(2p+1)/δ`. Let `1 ≤ l ≤ r₁`. Then

  `(r₁+1)^{pl} · l! · 2^{plr₁} · (q₁^{δ r₁})^l < q₁^{δ(1+1/p) l r₁}`.

That is, the coefficient bound `M` of Lemma 6, specialised to `B = q₁^{δ r₁}`, is below `q₁^{δ₁ l r₁}` with `δ₁ = δ(1+p⁻¹)`.

Variables / typeclasses involved (Lean side):
- `p`: number of variables
- `δ`: Roth's small parameter
- `r₁`: first degree bound
- `q₁`: first denominator
- `l`: Wronskian order

Hypotheses (Lean side):
- `hp : 0 < p`
- `hδ0 : 0 < δ`
- `hq₁`: the size condition (eq. 21 of the source)
- `hl : 1 ≤ l`
- `hl' : l ≤ r₁`

Conclusion (math): `M < q₁^{δ₁ l r₁}`.

Conclusion (Lean): `lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁))`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is an internal numeric estimate in the proof of Lemma 7. It is not a structure, not a main result, and not a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 16
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof Lemma 7 "M < q_1^{delta_1 l r_1}" delta_1 = delta(1+1/p) estimate Wronskian constant | partial | Ridout-style version of Roth's Lemma 7 in a quantitative Roth–Ridout paper | that paper has the same hypothesis shape `log q_1 > δ^{-1} m(2m+1)`, but the M-estimate is not stated standalone; Roth 1955 (Mathematika) also turns up |
| 2 | WebSearch (general form) | Roth's lemma induction Theta_m(B;q;r) bound 10^{m-1} delta^{(1/2)^{m-1}} proof estimate of M and Phi | partial | Roth's lemma via induction on m (arXiv 2502.00731) | different constants and no standalone M-estimate |
| 3 | WebSearch (aliases / elementary form) | inequality (r+1)^{pl} l! 2^{plr} < 2^{(2p+1) r l} factorial bound l! ≤ l^l elementary estimate | no | — | only generic factorial and Stirling bounds (arXiv 1802.07046) and Cauchy-estimate arguments (arXiv 1009.4408) |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` grep `M <`, `delta_1 l r_1` | yes | l.973–981 `M < (2^{(2p+1)r_1} q_1^{δ r_1})^l < ... = q_1^{δ_1 l r_1}` | matches the Lean statement exactly (the Lean version goes through 2 directly, not e) |
| 6 | nLab | coefficient bound / Roth lemma | no | — | nLab has no entries for proof-internal numeric estimates in Diophantine approximation |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | no discussion of this specific estimate; it is routine bookkeeping |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | arXiv 2502.00731, arXiv 2111.12409 | each exposition has its own constants |

### Literature summary (Phase 3)

Concept identified as: the bookkeeping estimate `M < q₁^{δ₁ l r₁}` in the inductive proof of Roth's lemma (Lemma 7 in the Cassels/Ridout-style exposition that clean.tex follows).

Sources agree on the standard form: no. It is not a standalone result anywhere. Each exposition has its own constants: `e` vs `2`, and the choice of `δ₁`.

Most general standard form: none exists. The underlying technique is "absorb polynomial/factorial factors into `q₁^{εlr₁}` using `log q₁ ≫ 1/ε`".

Generality dimensions where the literature varies:
  - the base used to absorb the factors (`e` in the source, `2` in Lean);
  - whether `q₁` is an integer or any real `> 1` (only `log q₁` matters).

Disagreement with the literature: none.

### Generality analysis — `Roth.lem6M_lt`

Literature-standard form (from Phase 3): none. The source states it for integer `q₁ > 1` and `1 ≤ l ≤ r_p + 1 ≤ r₁`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `q₁ : ℕ` | natural, cast to ℝ | integer `q₁ > 1` | yes | only `log q₁` and `q₁ > 0` are used; a real `q₁ ≥ 0` works (compiled, evidence) |
| 2 | `hl' : l ≤ r₁` | `l ≤ r₁` | `l ≤ r_p + 1 < r₁ + 1` | yes | only `l ≤ 2^{r₁}` (plus `0 < l r₁`) is used (compiled, evidence) |
| 3 | `hl : 1 ≤ l` | `1 ≤ l` | `1 ≤ l` | no | at `l = 0` both sides equal 1 (compiled, evidence), so strictness needs `l ≥ 1` |
| 4 | `hp : 0 < p` | `0 < p` | `p ≥ 1` | no | `1/p` and the use of `δ/p` need it |
| 5 | `hq₁` | `p(2p+1)/δ ≤ log q₁` | `2p+1 < δ p⁻¹ log q₁` | no | it is the exact quantitative input; strictness of the conclusion comes from `log 2 < 1` |

### Generality verdict (Phase 4b)

The current form is: STRICTLY NARROWER THAN the maximal one, in two cosmetic directions (real `q₁`; `l ≤ 2^{r₁}`). Both are verified.
Number of weakening opportunities found: 2. Both compile in `.mathlib-quality/overview/evidence/Roth.lem6M_lt/weaken.lean` (`lake env lean`, no output). The original statement is re-derived from the weak form in one term.
Proposed restatement:

```lean
theorem lem6M_lt {p : ℕ} (hp : 0 < p) {δ : ℝ} (hδ0 : 0 < δ) {r₁ l : ℕ} {q₁ : ℝ}
    (hq0 : 0 ≤ q₁) (hq₁ : (p : ℝ) * (2 * p + 1) / δ ≤ Real.log q₁)
    (hlr : 0 < l * r₁) (hl' : l ≤ 2 ^ r₁) :
    lem6M p r₁ (q₁ ^ (δ * r₁)) l < q₁ ^ (δ * (1 + 1 / p) * (l * r₁))
```

Cost of restatement: CHEAP. It also needs `factorial_coefficient_le_two_pow_aux` to take `l ≤ 2^r₁`, which it already does. These weakenings have no consumer: the single call site supplies exactly `1 ≤ l ≤ r₁` with integer `q₁`.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | it has only numeric hypotheses |
| 2 | sequences to filters? | no | — | it is a finite inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | `Real.rpow` and `Real.log` force ℝ |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | partial | real `q₁` instead of ℕ (row 1 above) | none |
| 8 | concrete-via-abstract? | no | — | the proof uses the explicit shape of `lem6M` throughout (`rw [lem6M]; ring`); the named object is the content |
| 9 | false-generalisation guard | no false generalisation | the real-`q₁` form is the same inequality | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: it is an explicit numeric estimate about a proof-specific constant. There is no organisational reformulation.

### Proof strategy — `Roth.lem6M_lt`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | the private helper `two_pow_lt_rpow_aux` unfolds `Real.rpow_def_of_pos` by hand, and mathlib's `Real.lt_rpow_of_log_lt` (found by LeanSearch) could shorten it; that is a golf of the helper, not a missing API | CHEAP |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC (a `calc` chain of monotonicity plus rpow algebra). A minor golf is possible in the helper via `Real.lt_rpow_of_log_lt`.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.lem6M_lt`

- [A] Lean-Finder, query "(r+1)^(p*l) * l! * 2^(p*l*r) * B^l < q^(δ(1+1/p) l r) when log q ≥ p(2p+1)/δ": only unrelated hits (`Behrend.roth_lower_bound_explicit`, `Behrend.bound`, …).
- [B] Loogle, query `(2:ℝ) ^ ?n < ?q ^ ?x`: no hits.
- [C] LeanSearch, query "2^n < q^x when log q times x exceeds n, real rpow bound from logarithm hypothesis": building blocks only (`Real.lt_rpow_of_log_lt`, `Real.rpow_lt_iff_lt_log`, `Real.le_rpow_of_log_le`).
- [D] Grep mathlib source for `lem6M`: none. The building blocks `Nat.factorial_le_pow` (Mathlib/Data/Nat/Factorial/Basic.lean) and `Real.rpow_def_of_pos` (Mathlib/Analysis/SpecialFunctions/Pow/Real.lean:51) exist.
- [E] Name pattern (`lem6M`): project-only.

Searched for both the user's form and the generic "absorb factors via a log bound" form.

Concluded: found building blocks (`Nat.factorial_le_pow`, `Nat.lt_two_pow_self`, `Real.lt_rpow_of_log_lt`, `Real.rpow_add`, `Real.rpow_mul_natCast`). The statement itself is not in mathlib.

### Normal-form check — `Roth.lem6M_lt`

Equivalent formalisms:
- (a) `lem6M … < q₁^{δ(1+1/p) l r₁}` (current);
- (b) `lem6M … < (q₁^{δ₁ r₁})^l`;
- (c) the log form `log M < δ₁ l r₁ log q₁`.

Mathlib has no canonical form, since this is not a mathlib concept. The current form (a) matches the shape used at the call site, which compares with `q 0 ^ (ε * (l * r 0))`.

RHS convention respected? n/a (this is an inequality).

### Syntactic generality — `Roth.lem6M_lt`

Alternative restatements attempted:
- the weak form (real `q₁`, `l ≤ 2^{r₁}`, `0 < l r₁`), compiled;
- form (b) above.

Chosen restatement: current.
Justification: the single caller has `1 ≤ l ≤ r₁` directly, and the weak form would only move `Nat.lt_two_pow_self` to the call site.

### Superfluous-argument audit — `Roth.lem6M_lt`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hp` | yes | `1/p`, `δ/p` |
| 2 | `hδ0` | yes | division by δ, positivity |
| 3 | `hq₁` | yes | the main input |
| 4 | `hl` | yes | strictness (counterexample at `l = 0` compiled) |
| 5 | `hl'` | weakenable | only `l ≤ 2^{r₁}` and `r₁ > 0` are needed |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE (`hl'` is weakenable but not superfluous)

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.lem6M_lt`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:871 (private `theta_phi_lt_aux`) | `have hM : M < (q 0 : ℝ) ^ (ε * (l * r 0)) := by simpa only [ε, ...] using lem6M_lt (p := n + 1 + 1) (Nat.zero_lt_succ _) hδ0 ... hl1 (hl2.trans ...)` |

Inline-derivation grep: none. No other site re-derives a bound on `lem6M` against an rpow.

### Composition check (Phase 6)

Can `Roth.lem6M_lt` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.lt_rpow_of_log_lt` applied to `M`.
- Mathlib decls used: `Real.lt_rpow_of_log_lt`.
- Result: partial. The remaining goal `log M < δ₁ l r₁ log q₁` still needs the factorial/power estimate and the logarithm of a product, which is the whole content.

Attempt 2: the current calc with mathlib lemmas only (`Nat.factorial_le_pow`, `Nat.lt_two_pow_self`, `gcongr`, `Real.rpow_def_of_pos`, `Real.rpow_add`).
- Result: succeeds, but takes about 15 lines with `linarith`, `ring` and `gcongr`. That is a real proof, not a composition.

Conclusion: NOT-COMPOSABLE (in the ≤3-call sense).

### Verdict: `Roth.lem6M_lt`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the estimate appears only as an internal step in the proof of Lemma 7 (clean.tex l.973–981). Other Roth expositions use their own constants, and none states it standalone.
- Generality analysis (Phase 4): two cosmetic weakenings, both compiled (real `q₁ ≥ 0`; `l ≤ 2^{r₁}` with `0 < l r₁`). `hl` is necessary.
- Mathlib search (Phase 5): building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE. It is a genuine 15-line arithmetic proof.

**Rationale:**

The theorem is the paper's bookkeeping estimate `M < q₁^{δ₁ l r₁}`. It is stated about the project-local constant `lem6M`, which was assessed as NO-composable-from-mathlib (a proof-specific number). The NO buckets do not fit:
- mathlib does not have the statement;
- the statement is not a ≤3-call composition, since it needs a factorial/power estimate, a log-to-rpow conversion and exponent algebra.

The YES buckets do not fit either: the statement has no standing outside this proof and is about a constant mathlib would never define. That leaves BORDERLINE by elimination. The judgment is clear in practice: keep it in the project, as with the sibling `Roth.index_le_lem6` and `Roth.Θ_option_le` reports.

The weakenings compile but have no consumer. The single private caller supplies exactly `1 ≤ l ≤ r₁` with integer `q₁`, so adopting them is optional.

Numbered questions:
1. Keep `Roth.lem6M_lt` project-local and never upstream it? (Recommended: yes.)
2. Make it `private`, given that its only caller (`theta_phi_lt_aux`, Theta.lean:871) is private? (Recommended: optional; yes if the public API should list only paper lemmas.)
3. Adopt the weakened signature (real `q₁ ≥ 0`, `l ≤ 2^r₁`, `0 < l * r₁`) from evidence/Roth.lem6M_lt/weaken.lean? (Recommended: no, since no caller benefits.)
4. Golf private `two_pow_lt_rpow_aux` using `Real.lt_rpow_of_log_lt`? (Recommended: optional, cosmetic.)

Next action: the user answers the questions. The default is no change: keep the theorem in Roth/Theta.lean with its one call site at line 871.

---

### Next step

Keep `Roth.lem6M_lt` in Roth/Theta.lean. Optionally make it private. Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.lem6M_lt/weaken.lean` imports `Roth.Theta`. `lake env lean` compiled it clean, with no output, in 39 s. It proves three things:
  - `lem6M_lt_weak`, with real `q₁ ≥ 0`, `0 < l * r₁` and `l ≤ 2 ^ r₁`. The private helper proofs are inlined because they are inaccessible from another module.
  - The original statement, derived from the weak form in one term.
  - The fact that at `l = 0` both sides equal 1, so `hl` is necessary.
- Mathlib grep for `lem6M`: no hits. Project grep `grep -rn lem6M_lt Roth/`: the declaration and one use at Theta.lean:871.
- LeanFinder (1 query), LeanSearch (1 query) and Loogle (1 query), as in the search-status block.
- WebSearch: 3 queries (literature table).
- ChatGPT MCP: n/a (not configured).
- Local references: clean.tex l.973–981.
