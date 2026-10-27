---
decl: Roth.one_le_lem6M
file: Roth/Theta.lean
line: 279
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: The fact 1 <= M for the project-local Lemma 6 constant lem6M (given 1 <= B) is three applications of mathlib's one_le_mul_of_one_le_of_one_le to four one_le_pow0 or factorial facts (compiled); it concerns a Roth-proof-specific number, so there is nothing for mathlib.
action: Do not upstream; keep Roth.one_le_lem6M in Roth/Theta.lean as the API lemma for lem6M (sole caller private theta_phi_lt_aux at Theta.lean:866, which feeds hM1 to Θ_mono-based bounds); no call-site changes.
---

# Roth.one_le_lem6M

## Inventory entry

### `theorem Roth.one_le_lem6M`
- **Type**: `(p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) : 1 ≤ lem6M p r₁ B l`
- **What**: If `B ≥ 1`, then the Lemma 6 constant `M = (r₁+1)^{pl} · l! · B^l · 2^{plr₁}` is at least `1`.
- **How**: It unfolds `lem6M` with `rw` and splits the product with three nested `one_le_mul_of_one_le_of_one_le`. Each factor is then closed directly: `one_le_pow₀` handles the three powers (using `le_add_of_nonneg_left` with `Nat.cast_nonneg r₁` for `1 ≤ r₁ + 1`, `hB`, and `norm_num` for `1 ≤ 2`), and `Nat.factorial_pos` with `exact_mod_cast` handles `1 ≤ l!`.
- **Hypotheses**: `hB : 1 ≤ B`. This is necessary (evidence (2), (3)).
- **Uses from project**: `Roth.lem6M`
- **Used by**: `Roth.theta_phi_lt_aux` (private, Roth/Theta.lean:866). There it supplies `hM1`, which is passed on at lines 884 and 888 to the Lemma 7 helpers that call `Θ_mono hM1 hM`. It is not used in any other file.
- **Visibility**: public
- **Lines**: 278–284 (docstring 278, statement 279, proof 280–284, 5 lines)
- **Notes**: Section `Lemma6` variables (`τ`, `[Fintype τ]`, `[DecidableEq τ]`) are not used. The source (clean.tex §5) uses `M ≥ 1` implicitly. Θ is only monotone in its first argument for `1 ≤ M`.

## Junk check (Step 8)
- **Used anywhere?** Yes, once (Theta.lean:866). The caller needs `1 ≤ M` to apply `Θ_mono`.
- **Wrapper of 1–2 mathlib calls?** No. It takes three `one_le_mul_of_one_le_of_one_le` plus four factor facts, which is a small but real composition.
- **Does mathlib have it?** No. `lem6M` is project-local (see `Roth.lem6M.md`, NO-composable-from-mathlib).
- **Too specific (inline?)?** It could be inlined at its single call site. It is better kept as the positivity-style API lemma of the def `lem6M`, which keeps the private `theta_phi_lt_aux` (already long) from unfolding `lem6M`.
- **Well-chosen?** Yes. The hypothesis is minimal and the conclusion is the form `Θ_mono` consumes.

Conclusion: **KEEP**. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter:
- The theorem is public and the name does not end in `_aux`.
- The docstring does not start with internal/auxiliary.
- Step 8 said KEEP.
- A namespace-aware grep for `one_le_lem6M` in `.lake/packages/mathlib/Mathlib/` finds nothing.
- It is not a glue lemma, because it has a 5-line proof and is not `rfl`.

None of these fire, so this is a full run. Parent `Roth.lem6M` is NO-composable-from-mathlib.

### Baseline (Phase 0)
- lake build:               clean (project built per brief; the evidence file importing `Roth.Theta` compiles with no output)
- decl `Roth.one_le_lem6M`:  resolved at Roth/Theta.lean:279
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it.

### Statement (Phase 1)

`Roth.one_le_lem6M` is a theorem stating the following. For natural numbers `p`, `r₁`, `l` and a real `B ≥ 1`,

  `1 ≤ (r₁ + 1)^{p l} · l! · B^l · 2^{p l r₁}`.

Every factor is at least 1, so their product is too.

Variables / typeclasses involved (Lean side):
- `p r₁ l : ℕ`: exponents and counts of Lemma 6.
- `B : ℝ`: coefficient bound.

Hypotheses (Lean side):
- `hB : 1 ≤ B`.

Conclusion (math): `M ≥ 1`.

Conclusion (Lean): `1 ≤ lem6M p r₁ B l`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is an elementary inequality about a proof-internal constant.

(The literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

n/a. The kind is theorem, not def. The proof is 5 lines.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof Lemma 6 constant M = (r_1+1)^{pl} l! B^l 2^{plr_1} generalized Wronskian index bound | no | — | finds Roth 1955, the Bombieri–van der Poorten Lemma 6 corrigendum, arXiv 2502.00731 and arXiv 1305.0926; none states this constant or `M ≥ 1` |
| 2 | WebSearch (general form) | product of real numbers each at least one is at least one lemma | partial | `∏ x_i ≥ 1` if all `x_i ≥ 1` (folklore, by induction; ProofWiki has bounds for finite products) | the only mathematical content is this folklore fact |
| 3 | WebSearch (named-after / aliases) | Cassels Introduction to Diophantine Approximation Roth's theorem Theta_m(B; q; r) lemma coefficient bound M | no | — | finds Cassels 1957 and Pottmeyer lecture notes (Roth's lemma); no statement of this constant |
| 4 | ChatGPT MCP | — | n/a | — | `ask_chatgpt_math` MCP not configured in this session (no such tool available) |
| 5 | Local references | grep `.mathlib-quality/references/clean.tex` for `M=` | yes | l.724 (eq. 16) defines `M`; l.736 derivation | `M ≥ 1` is used implicitly in Lemma 6/7, where Θ is applied with first argument `M` |
| 6 | nLab | product of elements ≥ 1 | no | — | there is no nLab entry for elementary real inequalities |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (result of #2) | partial | folklore product inequality | nothing specific |
| 10 | recent arXiv (last 5 years) | (result of #1) | no | — | arXiv 2502.00731 uses different constants |

### Literature summary (Phase 3)

Concept identified as: the positivity fact `M ≥ 1` for the proof-internal constant `M` of Lemma 6 in the quantitative Roth argument.

Sources agree on the standard form: there is no standard form. The general content is the folklore "a product of factors ≥ 1 is ≥ 1".

Most general standard form: in an ordered (semi)ring, if `1 ≤ a` and `1 ≤ b` then `1 ≤ a b`. Mathlib has this as `one_le_mul_of_one_le_of_one_le`, and for finite products as `Finset.one_le_prod` and `List.one_le_prod`.

Generality dimensions where the literature varies: none.

Disagreement with the literature: none.

### Generality analysis — `Roth.one_le_lem6M`

Literature-standard form (from Phase 3): there is none specific. The building block is `one_le_mul_of_one_le_of_one_le`.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `hB : 1 ≤ B` | `1 ≤ B` | `B ≥ 1` (paper) | no | it fails for `B = 0, l = 1` (evidence (2)) and for `0 < B`, e.g. `B = 1/2` (evidence (3)); only for `l = 0` is it unneeded (evidence (4)), and that case is irrelevant since callers have `l ≥ 1` |
| 2 | `p r₁ l : ℕ` | naturals | naturals | no | they are intrinsic to `lem6M` |
| 3 | codomain `ℝ` | `ℝ` | ordered semiring | technically yes | that is a false generalisation, because `lem6M` is `ℝ`-valued (parent report) |
| 4 | section instances | not taken | — | already absent | the statement mentions no `τ` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0. The drop of `hB` was refuted in Lean (evidence (2), (3)).
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | the only hypothesis is a numeric bound |
| 2 | sequences to filters? | no | — | it is a finite inequality |
| 3 | construction vs universal property? | no | — | — |
| 4 | bundled substructure? | no | — | — |
| 5 | field-specific to semiring? | no | — | `lem6M` is `ℝ`-valued |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | ℕ exponents are intrinsic |
| 8 | concrete-via-abstract? | yes (trivially) | after `rw [lem6M]` the proof uses only "each factor ≥ 1", which is exactly `one_le_mul_of_one_le_of_one_le`; the abstract form is already in mathlib | none new |
| 9 | false-generalisation guard | n/a | no generalisation is proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: the abstract content (Q8) already exists in mathlib as `one_le_mul_of_one_le_of_one_le`, and the residue is specific to `lem6M`.

### Proof strategy — `Roth.one_le_lem6M`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no | every step is an existing mathlib lemma (`one_le_mul_of_one_le_of_one_le`, `one_le_pow₀`, `Nat.factorial_pos`, `le_add_of_nonneg_left`) | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC

### Risk verdict (Phase 4.5)

n/a. The declaration kind is theorem.

### Mathlib search-status: `Roth.one_le_lem6M`

- [A] Lean-Finder, query "product of real numbers each at least 1 is at least 1":
  - hits: `one_le_finprod`, `List.one_le_prod`, `one_le_finprod'`, `Finset.one_le_prod`, `Finset.one_le_prod'`.
- [B] Loogle, query `1 ≤ ?a → 1 ≤ ?b → 1 ≤ ?a * ?b`:
  - hits: `one_le_mul`, `Left.one_le_mul` (both need `MulLeftMono`, which `ℝ` lacks), and `one_le_mul_of_one_le_of_one_le` (Mathlib/Algebra/Order/GroupWithZero/Basic.lean), which is the one usable for `ℝ`.
- [C] LeanSearch, query "1 ≤ a → 1 ≤ b → 1 ≤ a * b":
  - hits: `Right.one_le_mul`, `one_le_mul`, `one_le_mul_of_one_le_of_one_le`, `Left.one_le_mul`.
- [D] Grep mathlib src for `one_le_lem6M` and `lem6M`:
  - no hits.
- [E] Name pattern, `lean_local_search`:
  - not needed beyond [D]. The qualified name is project-specific.

Searched for both the user's form and the general "product of factors ≥ 1" form.

Concluded: found building blocks (`one_le_mul_of_one_le_of_one_le`, `one_le_pow₀`, `Nat.factorial_pos`). Composition yields our form.

### Normal-form check — `Roth.one_le_lem6M`

Equivalent formalisms:
- `1 ≤ lem6M …` (current);
- `0 < lem6M …` (weaker);
- `1 ≤ l! * x^l` (via the parent's ring identity).

Canonical form: `1 ≤ M` is what `Θ_mono` consumes. The RHS convention is n/a, since this is an inequality.

### Syntactic generality — `Roth.one_le_lem6M`

Alternative restatements attempted:
- taking `(hB : 1 ≤ B ^ l)` instead of `1 ≤ B`. This is marginally weaker, but harder to supply at the call site, which has `1 ≤ q^(δ r)` from `Real.one_le_rpow`.

Chosen restatement: current.
Justification: it matches what the caller has.

### Superfluous-argument audit — `Roth.one_le_lem6M`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `hB : 1 ≤ B` | yes | refuted without it (evidence (2), (3)) |
| 2 | `p r₁ l` | yes | arguments of `lem6M` |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project lemma)

### Call sites — `Roth.one_le_lem6M`

Internal use count: 0 outside the declaring file. There is 1 use in Theta.lean.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:866 (private `theta_phi_lt_aux`) | `have hM1 : 1 ≤ M := one_le_lem6M _ _ (Real.one_le_rpow (by exact_mod_cast hq.le) (mul_nonneg hδ0.le (Nat.cast_nonneg _))) l` |

Inline-derivation grep: (none). Other `hM1 : 1 ≤ M` occurrences (Theta.lean:743, 782) are hypotheses of helpers, not re-derivations.

### Composition check (Phase 6)

Can `Roth.one_le_lem6M` be derived from mathlib in ≤3 chained calls?

Attempt 1: `one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le h1 h2) h3) h4`. Each `hᵢ` is a `one_le_pow₀` or factorial cast fact.
- Mathlib decls used: `one_le_mul_of_one_le_of_one_le`, `one_le_pow₀`, `Nat.factorial_ne_zero` / `Nat.factorial_pos`.
- Result: succeeds (evidence (1)). The current proof is literally this composition.
- Notes: the nesting is one lemma applied three times plus four leaf facts. That is a trivial composition, not a new proof.

Conclusion: COMPOSABLE

### Verdict: `Roth.one_le_lem6M`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): there is no literature statement. The content is the folklore "a product of factors ≥ 1 is ≥ 1", and `M` itself appears only in clean.tex eq. (16).
- Generality analysis (Phase 4): MAXIMALLY GENERAL. Dropping `hB` or weakening it to `0 < B` is refuted in Lean.
- Mathlib search (Phase 5): building blocks `one_le_mul_of_one_le_of_one_le`, `one_le_pow₀`, `Nat.factorial_pos`.
- Composition check (Phase 6): COMPOSABLE (evidence (1)).

**Rationale:**

This lemma says the Lemma 6 constant `M = (r₁+1)^{pl} l! B^l 2^{plr₁}` is at least 1 when `B ≥ 1`. Mathematically it is the triviality that each factor is ≥ 1, and in Lean it is precisely three applications of mathlib's `one_le_mul_of_one_le_of_one_le` to `one_le_pow₀` and factorial facts. The parent `lem6M` is a project-specific constant, already judged NO-composable-from-mathlib. A positivity lemma about it has no meaning outside this proof, so mathlib gains nothing.

Belongs-elsewhere check: keep it project-locally, as the standard "bound" API lemma accompanying `lem6M`. It spares the long private `theta_phi_lt_aux` from unfolding `lem6M`, and it mirrors the paper's implicit `M ≥ 1`. The template refactor for this bucket ("inline at call sites") is possible, since there is a single call site, but it is not recommended. It would put a 4-line unfolding proof inside a proof that is already long, and it would couple that proof to the body of `lem6M`.

Mathlib building blocks:
- `one_le_mul_of_one_le_of_one_le` (Mathlib/Algebra/Order/GroupWithZero/Basic.lean)
- `one_le_pow₀`
- `Nat.factorial_pos` (Mathlib/Data/Nat/Factorial/Basic.lean)

Composition sketch (≤3 lines):
```lean
example (p r₁ : ℕ) {B : ℝ} (hB : 1 ≤ B) (l : ℕ) : 1 ≤ Roth.lem6M p r₁ B l :=
  one_le_mul_of_one_le_of_one_le (one_le_mul_of_one_le_of_one_le
    (one_le_mul_of_one_le_of_one_le h1 h2) (one_le_pow₀ hB)) (one_le_pow₀ one_le_two)
```
Here `h1 : 1 ≤ (r₁+1)^(p*l)` and `h2 : 1 ≤ (l ! : ℝ)`.

Call sites in our project (from Phase 6.0): K = 1, at Roth/Theta.lean:866.

Refactor plan: none recommended. If the project ever wanted to inline it, replace `one_le_lem6M _ _ hB' l` at Theta.lean:866 with `by rw [lem6M]; exact <composition above>`.

Next action: no upstreaming. Leave the lemma and its call site as they are.

---

### Next step

No upstreaming. Keep `Roth.one_le_lem6M` in Roth/Theta.lean next to `Roth.lem6M`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.one_le_lem6M/probes.lean` imports `Roth.Theta`. The final version compiled with no output, about 38 s per run. It checks four things:
  - (1) the composition proof, via three `one_le_mul_of_one_le_of_one_le` calls;
  - (2) `¬ 1 ≤ lem6M 1 0 0 1`, so `hB` cannot be dropped;
  - (3) `¬ 1 ≤ lem6M 0 0 (1/2) 1`, so `hB` cannot be weakened to `0 < B`;
  - (4) `lem6M p r₁ B 0 = 1`.
- The first run failed: a `nlinarith` variant of (1) hit a `MulRightMono ℝ` instance error. That variant was replaced by the explicit composition.
- Searches:
  - WebSearch: 3 queries (literature table).
  - Lean-Finder, Loogle, LeanSearch: 1 query each (search-status block).
  - Mathlib grep for `lem6M` / `one_le_lem6M`: no hits.
  - Project grep: a single caller at Theta.lean:866.
- ChatGPT MCP: n/a (not configured).
- Local refs: clean.tex l.724, 736.
