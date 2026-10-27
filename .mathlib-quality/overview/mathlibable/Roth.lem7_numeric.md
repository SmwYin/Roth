---
decl: Roth.lem7_numeric
file: Roth/Theta.lean
line: 709
kind: theorem
visibility: public
verdict: BORDERLINE-needs-human
cost: n/a
junk: KEEP
rationale: Final numeric absorption step 2(Phi + sqrt Phi + sqrt delta) < 10^p delta^((1/2)^p) of the proof of Lemma 7 (clean.tex l.1023-1035); all hypotheses necessary (compiled counterexamples), ad hoc constants with no literature standing, no mathlib counterpart, not a 3-call composition; recommended resolution is keep project-local.
action: Keep in Roth/Theta.lean (single caller private theta_phi_lt_aux at Roth/Theta.lean:879); optionally make it private alongside lem7_Φ_bound; do not upstream.
---

# Roth.lem7_numeric

## Inventory entry

### `theorem Roth.lem7_numeric`
- **Type**: `{p : ℕ} (hp : 2 ≤ p) {δ : ℝ} (hδ0 : 0 < δ) (hδ1 : δ ≤ 1) {Φ : ℝ} (hΦ : Φ ≤ 3 * 10 ^ (p - 1) * δ ^ ((1 / 2 : ℝ) ^ (p - 1))) : 2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ ((1 / 2 : ℝ) ^ p)`
- **What**: For `p ≥ 2`, `0 < δ ≤ 1` and any real `Φ ≤ 3·10^{p-1} δ^{(1/2)^{p-1}}`, the inequality `2(Φ + √Φ + √δ) < 10^p δ^{(1/2)^p}` holds.
- **How**: Writes `p = k + 1` and sets `a = δ^{(1/2)^{k+1}}`, `T = 10^k`. It proves:
  - `a² = δ^{(1/2)^k}` (`Real.rpow_mul_natCast`);
  - `√δ ≤ a` (`Real.sqrt_eq_rpow`, `Real.rpow_le_rpow_of_exponent_ge`);
  - `10 ≤ T` (`le_self_pow₀`);
  - `√Φ < T a` (`Real.sqrt_lt'`);
  - `a² ≤ a` (`Real.rpow_le_one`).
  It then closes with one `linear_combination`.
- **Hypotheses**:
  - `hp`: needed. It fails at `p = 1`.
  - `hδ0`: needed for strictness. It fails at `δ = 0`.
  - `hδ1`: needed for `a² ≤ a` and `√δ ≤ a`. It fails for large `δ`.
  - `hΦ`: the input bound. `Φ` may be negative, and equality is allowed.
- **Uses from project**: `[]`
- **Used by**: `Roth.theta_phi_lt_aux` (private, the Lemma 7 induction step) at Roth/Theta.lean:879. It has no other uses in `Roth/`.
- **Visibility**: public
- **Lines**: 704–740 (docstring 704–708, statement 709–711, proof 712–740, proof length 29 lines)
- **Notes**: The source is clean.tex §5, proof of Lemma 7, l.1023–1035 ("Set a = δ^{2^{-p}} …"). The Lean proof bounds term by term (`3T a² ≤ 3T a`, `√Φ < T a`, `√δ ≤ 10 T a`) instead of the paper's explicit coefficient `2(3/10 + √3/10^{3/2} + 1/100) < 1`. The two give the same conclusion. It is the companion of `Roth.lem7_Φ_bound` (assessed BORDERLINE-needs-human, recommendation keep local).

## Junk check (Step 8)
- **Used anywhere?** Yes, once, by private `theta_phi_lt_aux` (Theta.lean:879).
- **Wrapper of 1–2 mathlib calls?** No. It is a 29-line real/rpow/sqrt arithmetic proof.
- **Does mathlib have it?** No. LeanFinder returns only unrelated explicit bounds (Szemerédi, Behrend, Bertrand, Liouville). LeanSearch and Loogle return only the building blocks (`Real.sqrt_lt'`, `Real.sqrt_eq_rpow`).
- **Too specific (inline?)?** It is proof-specific, but it isolates a named step of the paper's chain. Inlining it into the already long `theta_phi_lt_aux` would hurt readability.
- **Well-chosen?** Yes. It mirrors the paper, and the docstring notes the slightly weaker hypotheses (negative `Φ`, non-strict bounds). It could be `private`.

Conclusion: **KEEP**. Optionally make it `private`.

## Mathlibable assessment (Step 9)

Pre-filter: none of the filters fire.
- It is public.
- The name has no `_aux` suffix.
- The docstring does not start with internal/auxiliary.
- Step 8 said KEEP.
- `grep -rn lem7 .lake/packages/mathlib/Mathlib/` finds nothing.
- It is not a glue lemma, since it has a real 29-line proof. INHERITED therefore does not apply.

Full run follows.

### Baseline (Phase 0)
- lake build:               ✓ clean (project built; the evidence file importing `Roth.Theta` compiles)
- decl `Roth.lem7_numeric`:  ✓ resolved at Roth/Theta.lean:709
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)` (supremum of indices of bounded integer polynomials at rational points) and Lemmas 5, 6, 7 bounding it

### Statement (Phase 1)

`Roth.lem7_numeric` is a theorem stating the following. Let `p ≥ 2` be an integer, let `0 < δ ≤ 1`, and let `Φ` be a real number with `Φ ≤ 3·10^{p-1} δ^{2^{-(p-1)}}`. Then

  `2(Φ + √Φ + √δ) < 10^p δ^{2^{-p}}`.

In the proof of Roth's lemma, `Φ` bounds the `(p-1)`-variable contribution. The left side bounds `Θ_p`, and the conclusion is the induction claim `Θ_p < 10^p δ^{2^{-p}}`.

Variables (Lean side):
- `p`: the induction level (number of variables)
- `δ`: Roth's small parameter
- `Φ`: the bound coming from the previous step

Hypotheses (Lean side):
- `hp : 2 ≤ p`
- `hδ0 : 0 < δ`
- `hδ1 : δ ≤ 1`
- `hΦ : Φ ≤ 3·10^{p-1} δ^{(1/2)^{p-1}}`

Conclusion (math): `2(Φ + √Φ + √δ) < 10^p δ^{(1/2)^p}`.

Conclusion (Lean): `2 * (Φ + √Φ + √δ) < 10 ^ p * δ ^ ((1 / 2 : ℝ) ^ p)`

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is an internal numeric estimate in the proof of Lemma 7. It is not a structure, not a main result, and not a named theorem.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 29
One-liner verdict: n/a (kind is theorem)

Conclusion: MULTI-LINE

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's lemma proof "10^p" delta^{2^{-p}} Theta_p induction numerical bound sqrt 3 | no | — | only additive-combinatorics Roth papers (arXiv 2206.10037, 2208.14354, 2601.11376); none has this estimate |
| 2 | WebSearch (general form) | Cassels Introduction to Diophantine Approximation Roth's theorem Lemma index Theta_m(B;q;r) < 10^m delta^{(1/2)^m} | partial | Roth's lemma by induction on the number of variables (arXiv 2502.00731; Cassels Ch. VI; Pottmeyer DioApp notes) | the setting matches, but no standalone numeric estimate; constants are exposition-specific |
| 3 | WebSearch (aliases / elementary form) | elementary inequality x + sqrt(x) bound a^2 ≤ a for 0 < a ≤ 1, sqrt delta ≤ delta^(2^-p) | partial | the elementary ingredients `a² ≤ a` for `a ∈ (0,1]` and `δ^{1/2} ≤ δ^{e}` for `e ≤ 1/2` | textbook facts only |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex`, grep for `Set $a=`, `\sqrt3` | yes | l.1023–1035: `Θ_p < 2(3·10^{p-1}a² + √3·10^{(p-1)/2} a + δ^{1/2}) ≤ … < 10^p a` with `a = δ^{2^{-p}}` | matches the Lean statement (with `Φ` abstracted as the bound on the first term) |
| 6 | nLab | Roth's theorem / numeric estimate | no | — | nLab has no entries for proof-internal Diophantine numeric estimates |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #1–#3) | no | — | this routine bookkeeping is not discussed |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | arXiv 2502.00731, arXiv 2601.11376 | each exposition has its own constants |

### Literature summary (Phase 3)

Concept identified as: the final constant-absorption step `Θ_p < 10^p δ^{2^{-p}}` in the inductive proof of Roth's lemma (Lemma 7 of the Cassels-style exposition followed by clean.tex).

Sources agree on the standard form: no. It is not a standalone result anywhere. Constants such as `10^p`, `3` and `2^{-p}` are specific to this exposition.

Most general standard form: none. The ingredients (`a² ≤ a` on `(0,1]`, rpow monotonicity in the exponent for bases ≤ 1, `√x < y ↔ x < y²`) are textbook facts that mathlib already has.

Generality dimensions where the literature varies: the constants only.

Disagreement with the literature: none. The Lean proof uses a cruder term-by-term absorption instead of the paper's explicit numerical coefficient, and reaches the same conclusion.

### Generality analysis — `Roth.lem7_numeric`

Literature-standard form (from Phase 3): none. The source states it for integers `p ≥ 2`, `0 < δ < 1`, and `Φ` equal to the specific bound.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hp : 2 ≤ p` | `2 ≤ p` | `p ≥ 2` | no | at `p = 1`, `δ = 1`, `Φ = 3` the left side is `8 + 2√3 > 10` (compiled counterexample) |
| 2 | `hδ0 : 0 < δ` | `0 < δ` | `0 < δ` | no | at `δ = 0`, `Φ = 0` both sides are `0` (compiled counterexample) |
| 3 | `hδ1 : δ ≤ 1` | `δ ≤ 1` | `δ < 1` | no (Lean is already weaker than the source) | at `p = 2`, `δ = 16`, `Φ = 120` the left side is `> 240` and the right side is `200` (compiled counterexample) |
| 4 | `hΦ` | `Φ ≤ …`, any real `Φ` | `Φ < …`, `Φ ≥ 0` | no (already weaker) | it is the input bound itself |
| 5 | `p : ℕ` | natural | integer | no meaningful one | the exponents `10^p` and `(1/2)^p` are natural powers |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL. Every hypothesis is necessary, verified by the compiled counterexamples in evidence/Roth.lem7_numeric/necessity.lean, and `hΦ` / `hδ1` are already weaker than the paper's strict forms.
Number of weakening opportunities found: 0.
Proposed restatement: none.
Cost of restatement: n/a.

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | it has only numeric hypotheses |
| 2 | sequences to filters? | no | — | it is a finite inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | `Real.rpow` and `Real.sqrt` force ℝ |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | the natural `p` indexes powers |
| 8 | concrete-via-abstract? | no | — | there is no named object; the statement is pure arithmetic |
| 9 | false-generalisation guard | n/a | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: it is an explicit numeric inequality with fixed constants. There is no organisational reformulation.

### Proof strategy — `Roth.lem7_numeric`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | every ingredient is in mathlib (`Real.sqrt_lt'`, `Real.rpow_mul_natCast`, `Real.rpow_le_rpow_of_exponent_ge`, `Real.rpow_le_one`, `le_self_pow₀`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. Facts are combined by a `linear_combination`, with no missing API.

### Risk verdict (Phase 4.5)

n/a — declaration kind is theorem

### Mathlib search-status: `Roth.lem7_numeric`

- [A] Lean-Finder, query "if Φ ≤ 3·10^(p-1)·δ^((1/2)^(p-1)) with 0<δ≤1 and p≥2 then 2(Φ + √Φ + √δ) < 10^p δ^((1/2)^p)": no hits. It returns only unrelated explicit bounds (`SzemerediRegularity.hundred_lt_pow_initialBound_mul`, `Behrend.roth_lower_bound_explicit`, `Behrend.bound`, `Bertrand.real_main_inequality`, `LiouvilleNumber.aux_calc`).
- [B] Loogle, query `√?x < ?y ↔ ?x < ?y ^ 2`: building blocks `Real.sqrt_lt'`, `Real.sqrt_lt`.
- [C] LeanSearch, query "square root of x is at most x to the power of a for 0 < x ≤ 1 and a ≤ 1/2": building blocks `Real.sqrt_eq_rpow`, `Real.sqrt_lt'`, `Real.sqrt_le_iff`.
- [D] Grep mathlib source: `lem7` has no hits.
- [E] Name pattern (`lem7_numeric`): project-only.

Searched for both the exact form and the generic ingredient forms. Concluded: found building blocks. The statement itself is not in mathlib.

### Normal-form check — `Roth.lem7_numeric`

Equivalent formalisms:
- (a) the current form, with an abstract `Φ` and a hypothesis `hΦ`;
- (b) a form with `Φ` replaced by its bound `3·10^{p-1} δ^{(1/2)^{p-1}}` (closed form);
- (c) a form stated in terms of `a = δ^{2^{-p}}`.

Mathlib has no canonical form, since this is not a mathlib concept. Form (a) is easiest at the call site, where it is applied with `apply` and the `Φ`-bound is supplied by `lem7_Φ_bound`.

RHS convention respected? n/a (this is an inequality).

### Syntactic generality — `Roth.lem7_numeric`

Alternative restatements attempted:
- form (b), the closed form;
- form (c), in terms of `a`.

Chosen restatement: current.
Justification: the abstract `Φ` with a `≤` hypothesis is applied directly by `apply lem7_numeric hp hδ0 hδ1.le` in the caller.

### Superfluous-argument audit — `Roth.lem7_numeric`

| # | Argument | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hp` | yes | counterexample at `p = 1` compiled |
| 2 | `hδ0` | yes | counterexample at `δ = 0` compiled |
| 3 | `hδ1` | yes | counterexample at `δ = 16` compiled |
| 4 | `hΦ` | yes | it is the input bound; without it `Φ` is unbounded |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.lem7_numeric`

Internal use count: 0 outside the declaring file; 1 inside it.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:879 (private `theta_phi_lt_aux`) | `apply lem7_numeric hp hδ0 hδ1.le` after `lt_div_iff₀'`, with the `Φ`-bound then closed from `lem7_Φ_bound` and Lemma 6 |

Inline-derivation grep: none. `lem7_Φ_bound` (Theta.lean:678) is the preceding step of the same chain, not a re-derivation.

### Composition check (Phase 6)

Can `Roth.lem7_numeric` be derived from mathlib in ≤3 chained calls?

Attempt 1: `Real.sqrt_lt'` together with `Real.rpow_le_one`.
- Result: partial. These give `√Φ < T a` and `a² ≤ a`. Still needed: `a² = δ^{(1/2)^k}` (`Real.rpow_mul_natCast`), `√δ ≤ a`, `10 ≤ 10^k`, and a linear combination.

Attempt 2: `nlinarith` / `positivity` closing directly.
- Result: not attempted as a one-liner. The rpow and sqrt terms need explicit rewriting first, so this would be a proof, not a composition.

Conclusion: NOT-COMPOSABLE (in the ≤3-call sense).

### Verdict: `Roth.lem7_numeric`

**Category:** BORDERLINE-needs-human

**Evidence:**
- Literature search (Phase 3): the estimate appears only as an internal step of the proof of Lemma 7 (clean.tex l.1023–1035). Other Roth expositions use their own constants.
- Generality analysis (Phase 4): MAXIMALLY GENERAL. All hypotheses are necessary (compiled counterexamples).
- Mathlib search (Phase 5): building blocks only.
- Composition check (Phase 6): NOT-COMPOSABLE. It is a genuine 29-line arithmetic proof.

**Rationale:**

This is the paper's last constant-absorption inequality for the induction step of Roth's lemma. The NO buckets do not fit:
- mathlib does not have the statement;
- it needs five separate facts and a linear combination, so it is not a ≤3-call composition.

The YES buckets do not fit either. Its constants (`3`, `10^p`, `2^{-p}`) are arbitrary choices of this exposition, with no meaning outside the proof. Mathlib keeps such ad hoc inequalities (`Bertrand.real_main_inequality`, `LiouvilleNumber.aux_calc`) next to the theorem they serve.

That leaves BORDERLINE by elimination, consistent with the sibling reports `Roth.lem7_Φ_bound` and `Roth.lem6M_lt`. The practical recommendation is clear: keep it in the project. It would travel with Roth's theorem, as a private helper, only if that whole development were ever upstreamed.

Numbered questions:
1. Keep `Roth.lem7_numeric` project-local and never upstream it on its own? (Recommended: yes.)
2. Make it `private`, together with `Roth.lem7_Φ_bound`, given that its only caller (`theta_phi_lt_aux`, Theta.lean:879) is private? (Recommended: optional.)

Next action: the user answers the questions. The default is no change: keep the theorem in Roth/Theta.lean with its one call site at line 879.

---

### Next step

Keep `Roth.lem7_numeric` in Roth/Theta.lean. Optionally make it private. Do not upstream.

## Evidence
- `.mathlib-quality/overview/evidence/Roth.lem7_numeric/necessity.lean` imports `Roth.Theta`. `lake env lean` compiled it clean, with no output, in 39 s. It proves:
  - the conclusion fails at `p = 1`, `δ = 1`, `Φ = 3`, where `hΦ` holds, so `hp` is necessary;
  - it fails at `δ = 0`, `Φ = 0`, so `hδ0` is necessary;
  - it fails at `p = 2`, `δ = 16`, `Φ = 120`, where `hΦ` holds, so `hδ1` cannot be dropped;
  - a sanity instantiation of the original statement at `p = 2`.
- Mathlib grep for `lem7`: no hits.
- Project grep `grep -rn lem7_numeric Roth/`: the declaration (Theta.lean:709) and one use (Theta.lean:879).
- LeanFinder (1 query), LeanSearch (1 query) and Loogle (1 query), as in the search-status block.
- WebSearch: 3 queries (literature table).
- ChatGPT MCP: n/a (not configured).
- Local references: clean.tex l.1015–1035.
