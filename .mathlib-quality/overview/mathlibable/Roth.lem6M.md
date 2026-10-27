---
decl: Roth.lem6M
file: Roth/Theta.lean
line: 270
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: lem6M is the ad hoc constant M = (r1+1)^(pl) l! B^l 2^(p l r1) from the proof of Lemma 6 (clean.tex eq. 16); it is a one-line real-arithmetic expression (ring-equal to l! * ((r1+1)^p B 2^(p r1))^l, compiled), with no literature or mathlib identity, so nothing to upstream.
action: Do not upstream; keep Roth.lem6M in Roth/Theta.lean as the shared name for the Lemma 6/7 constant (used by one_le_lem6M, lem6M_lt, index_det_le, index_le_lem6, Θ_option_le, theta_phi_lt_aux); no call-site changes.
---

# Roth.lem6M

## Inventory entry

### `def Roth.lem6M`
- **Type**: `(p r₁ : ℕ) (B : ℝ) (l : ℕ) : ℝ`
- **What**: The constant `M = (r₁ + 1)^{p l} · l! · B^l · 2^{p l r₁}` of Lemma 6. It bounds the coefficients of the generalised Wronskian determinant `F` built from `R ∈ RSet B r`.
- **How**: Direct closed-form expression `((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r₁)`, a product of mathlib primitives (`HPow`, `Nat.factorial`, casts). There is no proof.
- **Hypotheses**: none. It is declared in `section Lemma6`, but it uses none of the section variables (`τ`, `[Fintype τ]`, `[DecidableEq τ]`).
- **Uses from project**: `[]`
- **Used by**: Roth/Theta.lean only:
  - `one_le_lem6M` (279–280)
  - `index_det_le` (467, 472–473, 478, 483)
  - `index_le_lem6` (562–563)
  - `Θ_option_le` (574, 597–598, 602–603)
  - `lem6M_lt` (649, 651, 660, 662)
  - private `theta_phi_lt_aux` (853, 865–866, 871)
  - module docstring (29)
- **Visibility**: public
- **Lines**: 268–271 (docstring plus 2-line def). Proof length is 0 lines.
- **Notes**: Source is clean.tex §5, proof of Lemma 6, l.724 (`M= (r_1+1)^{pl} l! B^l 2^{plr_1}`). Lemma 7 (l.973) then specialises `B = q_1^{δ r_1}`; that specialisation is `lem6M_lt`.

## Junk check (Step 8)
- **Used anywhere?** Yes. About 20 references in Theta.lean across 6 declarations. It appears in the statements of `index_det_le`, `index_le_lem6`, `one_le_lem6M` and `lem6M_lt`.
- **Wrapper of 1–2 mathlib calls?** It is one arithmetic expression and wraps no lemma.
- **Does mathlib have it?** No. Mathlib's `Matrix.det_le` has the shape `n! • x^n`, and `lem6M` is ring-equal to that shape with `x = (r₁+1)^p B 2^{p r₁}` (evidence (3)). There is no named constant for it.
- **Too specific (inline?)?** Inlining would repeat a four-factor expression in 4 statements and 3 proofs. It would also break the interface between `index_det_le`, `index_le_lem6`, `lem6M_lt` and `theta_phi_lt_aux`, which all need to agree on the same `M`. The name mirrors the paper's `M`.
- **Well-chosen definition?** Yes for the project. One small cosmetic option exists: writing it as `l ! * ((r₁+1)^p * B * 2^(p r₁))^l` would match `Matrix.det_le` directly. That buys nothing, because `index_det_le` already gets there with `simpa [pow_mul, mul_right_comm]`.

Conclusion: **KEEP**. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter:
- The def is public and the name does not end in `_aux`.
- The docstring does not start with internal/auxiliary.
- Step 8 said KEEP.
- `grep -rn lem6M .lake/packages/mathlib/Mathlib` finds nothing.
- It is not a glue lemma.

None of these fire, so this is a full run.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief; the evidence file importing `Roth.Theta` compiles with no output)
- decl `Roth.lem6M`:         resolved at Roth/Theta.lean:270
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5, 6, 7 bounding it.

### Statement (Phase 1)

`Roth.lem6M` is a definition of a real number. For natural numbers `p`, `r₁`, `l` and a real `B`, it sets

  `M(p, r₁, B, l) = (r₁ + 1)^{p l} · l! · B^l · 2^{p l r₁}`.

In Lemma 6, `p` is the number of variables, `r₁` the largest degree bound, `B` the coefficient bound of `R` and `l` the size of the Wronskian. `M` bounds the coefficients of the determinant `det(Δ_{μ,ν} R)`. Each entry is a Hasse derivative with coefficients at most `2^{r₁ p} B`, there are at most `(r₁+1)^p` monomials per entry, and the Leibniz expansion has `l!` terms.

Variables / typeclasses involved (Lean side):
- `p : ℕ`: number of variables (call sites use `Fintype.card τ + 1` or `n + 2`).
- `r₁ : ℕ`: uniform degree bound.
- `B : ℝ`: coefficient bound.
- `l : ℕ`: Wronskian order.

Hypotheses (Lean side):
- none.

Conclusion (math): a positive real constant (when `B ≥ 1`, which is `one_le_lem6M`).

Conclusion (Lean): n/a, this is a definition.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is a proof-internal numeric constant of one lemma, not a structure, not a main result and not a named theorem.

(The literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | it unfolds by `rfl` (evidence (1)); proofs `rw [lem6M]` / `simpa only [lem6M, ...]` freely, and nothing relies on it being sealed |
| Avoid typeclass diamonds         | no       | it is a real number, not an instance |
| Mark semantic intent / API name  | yes (project-local) | it is the paper's `M`, shared between `index_det_le`, `index_le_lem6`, `lem6M_lt`, `one_le_lem6M` and `theta_phi_lt_aux`, which must all agree on the same constant |

Conclusion: ONE-LINER WITH-EXEMPTION. The exemption is a project-local API name only and does not argue for mathlib.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof Lemma 6 Wronskian generalized determinant coefficient bound (r_1+1)^{pl} l! B^l 2^{p l r_1} | no | — | finds Roth's generalised Wronskians (Roth 1955, Mathematika), Bombieri–van der Poorten quantitative Roth (Lemma 6 erratum), arXiv 2502.00731; none states this constant |
| 2 | WebSearch (general form) | bound on coefficients of generalized Wronskian determinant of derivatives of integer polynomial height l! factor Roth's lemma | partial | height bounds for derivatives of auxiliary polynomials (arXiv 2502.00731 Lemma 3.7) | the same kind of estimate, but each exposition has its own constant |
| 3 | WebSearch (named-after / aliases) | height of determinant of polynomial matrix Hadamard bound l! B^l binomial coefficients 2^r derivative Diophantine approximation | partial | Hadamard-type bounds on coefficients of a determinant of polynomials (Lossers, SIAM Rev. Problem 73-17; Dumas cs/0610136) | the general principle is "n! · (entry bound)^n" or Hadamard; no named constant |
| 4 | ChatGPT MCP | — | n/a | — | the `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` grep `M=` | yes | l.724 `M= (r_1+1)^{pl} l! B^l 2^{plr_1}`; l.736 derivation; l.973 Lemma 7 specialisation | matches the Lean def exactly |
| 6 | nLab | coefficient bound / height of determinant | no | — | there is no nLab entry for ad hoc numeric constants |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | partial | Hadamard / Leibniz-expansion bounds for determinants with polynomial entries | folklore technique, no canonical constant |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | arXiv 2502.00731 (2025) | uses its own differently-shaped constants |

### Literature summary (Phase 3)

Concept identified as: the proof-internal constant `M` in Lemma 6 of the (Ridout/Cassels/Yamada-style) quantitative Roth argument. It is a coefficient bound for a generalised Wronskian of a polynomial in `ℛ_p(B; r)`.

Sources agree on the standard form: no. Every exposition has its own constant, and the shape depends on how the derivative and monomial counts are bounded.

Most general standard form: the technique, not the constant. A determinant of an `l × l` matrix whose entries have height at most `x` has height at most `l! · N^{l-1} · x^l`, where `N` bounds the number of monomials (a Leibniz expansion). Mathlib's `Matrix.det_le` already gives the `n! · x^n` part for an absolute value.

Generality dimensions where the literature varies:
  - how the Hasse-derivative coefficient factor is bounded (`2^{r}` vs `binom(r, k)` products);
  - how the monomial count is bounded (`(r₁+1)^p` vs `∏(r_j+1)`).

Disagreement with the literature: none. It matches clean.tex l.724 verbatim.

### Generality analysis — `Roth.lem6M`

Literature-standard form (from Phase 3): there is none. It is a proof-specific numeric expression.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `p r₁ l : ℕ` | naturals | naturals | no | these are exponents and counts |
| 2 | `B : ℝ` | real | real (`≥ 1` in paper) | already weaker | no hypothesis is taken; `one_le_lem6M` adds `1 ≤ B` |
| 3 | codomain `ℝ` | `ℝ` | any ordered semiring | technically yes | false generalisation: all consumers compare with `|coeff|` in `ℝ` and with `Real.rpow` (`lem6M_lt`) |
| 4 | section instances `[Fintype τ] [DecidableEq τ]` | not taken | not needed | already absent | the def mentions no `τ` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for its role). There are no hypotheses or instances to drop.
Number of weakening opportunities found: 0
Proposed restatement: none. The closed form `l! * ((r₁+1)^p * B * 2^(p r₁))^l` (evidence (2)) is a reformulation, not a weakening.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | there are no hypotheses |
| 2 | sequences to filters? | no | — | it is a finite numeric expression |
| 3 | construction vs universal property? | no | — | it is a number |
| 4 | bundled substructure? | no | — | it is not a set |
| 5 | field-specific to semiring? | no | — | the codomain `ℝ` is forced by the consumers (row 3 above) |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | ℕ exponents are intrinsic |
| 8 | concrete-via-abstract? | no | — | there is no proof body |
| 9 | false-generalisation guard | yes | changing the codomain to a general ordered semiring would separate it from the `ℝ`-valued `RSet` / `Θ` API; rejected | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: it is a numeric constant. The only rephrasing is the `n! • x^n` shape of `Matrix.det_le` (evidence (3)), which is arithmetic, not an organisational improvement.

### Proof strategy — `Roth.lem6M`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no (for this def) | the reusable content (coefficient bound for det of Hasse derivatives) lives in `abs_coeff_det_hasseDeriv_le`, assessed separately | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It is a definition with no proof.

### Diamond / defeq risk — `Roth.lem6M`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | it defines no instances and uses only `ℝ` arithmetic |
| 2 | Reducibility leak | none | it is a plain semireducible noncomputable def; `rfl` unfolds it (evidence (1)), and proofs unfold it explicitly with `rw`/`simp only` |
| 3 | Non-canonical unfolding | low | the factor order `(r₁+1)^{pl} * l! * B^l * 2^{plr₁}` differs from the `n! • x^n` shape of `Matrix.det_le`; `index_det_le` bridges with `pow_mul, mul_right_comm` |
| 4 | Instance priority collision | none | it is not an instance |
| 5 | Universe-polymorphism issues | none | it takes no type arguments |
| 6 | Coercion ambiguity | none | it uses only the standard `ℕ → ℝ` casts |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.lem6M`

- [A] Lean-Finder, query "coefficient bound for determinant of a matrix whose entries are polynomials with bounded coefficients":
  - hits: `Matrix.det_le`, `Matrix.det_sum_le`, `Matrix.det_sum_smul_le` (Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean), plus irrelevant `Polynomial.natDegree_det_X_add_C_le`.
- [B] Loogle, query `(?a + 1) ^ (?p * ?l) * (Nat.factorial ?l) * ?B ^ ?l`:
  - no hits.
- [C] LeanSearch, query "bound on absolute value of coefficients of determinant of matrix of polynomials factorial times power of bound":
  - hits: `Matrix.det_le` (`abv A.det ≤ n! • x^n`), `Matrix.det_sum_le`, `Matrix.det_sum_smul_le`.
- [D] Grep mathlib src for `lem6M`:
  - none.
- [E] Name pattern, `lean_local_search`:
  - not needed beyond [D]. The qualified name is project-specific.

Searched for both the user's form (the exact four-factor constant) and the literature-standard form ("n! · x^n" determinant bound).

Concluded: found building blocks (`Matrix.det_le`'s `n! • x^n` shape, `Nat.factorial`, powers). No mathlib constant is this expression, and none should be.

### Normal-form check — `Roth.lem6M`

Equivalent formalisms:
- (a) `(r₁+1)^{pl} l! B^l 2^{plr₁}` (current, the paper's order);
- (b) `l! * ((r₁+1)^p B 2^{pr₁})^l`;
- (c) `l! • x^l` with `x = (r₁+1)^p B 2^{pr₁}`.

Does mathlib already have a canonical form for this idea? No. It is not an idea, it is a number.

Our statement follows the source's order (a). The equivalence to (b) and (c) is `ring` (evidence (2), (3)).

RHS convention respected? n/a. This is a def, not an equation lemma.

### Syntactic generality — `Roth.lem6M`

Alternative restatements attempted:
- (b) and (c) above (evidence (2)–(3)).

Chosen restatement: current (a).
Justification: it matches the source verbatim. `lem6M_lt` and `index_det_le` already normalise it with one `ring` / `simpa` step.

### Superfluous-argument audit — `Roth.lem6M`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `p` | yes | exponent |
| 2 | `r₁` | yes | base and exponent |
| 3 | `B` | yes | base |
| 4 | `l` | yes | exponent and factorial |
| 5 | section `τ`, `[Fintype τ]`, `[DecidableEq τ]` | not taken | the def does not mention `τ` |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project def)

### Call sites — `Roth.lem6M`

Internal use count: 0 outside the declaring file. There are about 20 lines in Theta.lean itself.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:279–280 | `theorem one_le_lem6M ... : 1 ≤ lem6M p r₁ B l := by rw [lem6M] ...` |
| Roth/Theta.lean:467 | `index_det_le ... ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l` |
| Roth/Theta.lean:472–473 | `hFcoef ... ≤ lem6M (Fintype.card τ + 1) r₁ B l := by simpa only [lem6M, ...] using abs_coeff_det_hasseDeriv_le ...` |
| Roth/Theta.lean:478, 483 | `hUc`, `hVc : ∀ a, |U.coeff a| ≤ lem6M (Fintype.card τ + 1) r₁ B l` |
| Roth/Theta.lean:562–563 | `index_le_lem6 ... 2 * (lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l + √(...) + √δ)` |
| Roth/Theta.lean:574, 597–603 | `Θ_option_le`: `let Φ := lem6Φ q r (lem6M ...) l`, `Finset.le_sup' (fun l ↦ lem6Φ q r (lem6M ...) l + ...)` |
| Roth/Theta.lean:649–662 | `theorem lem6M_lt ... : lem6M p r₁ ((q₁ : ℝ) ^ (δ * r₁)) l < (q₁ : ℝ) ^ (δ * (1 + 1 / p) * (l * r₁))` |
| Roth/Theta.lean:853, 865–871 | private `theta_phi_lt_aux`: `let M := lem6M (n + 2) (r 0) ((q 0 : ℝ) ^ (δ * r 0)) l`, `one_le_lem6M _ _ ...`, `lem6M_lt (p := n + 1 + 1) ...` |

Inline-derivation grep: (none). No site writes `(r₁+1)^(p*l) * l! * ...` without the name. `factorial_coefficient_le_two_pow_aux` (used in `lem6M_lt`) bounds the non-`B` factors, but it is a separate inequality, not a re-derivation of the constant.

### Composition check (Phase 6)

Can `Roth.lem6M` be derived from mathlib in ≤3 chained calls?

Attempt 1: the body itself, `((r₁ : ℝ) + 1) ^ (p * l) * l.factorial * B ^ l * 2 ^ (p * l * r₁)`.
- Mathlib decls used: `Nat.factorial`, `Monoid.npow`, `Nat.cast`.
- Result: succeeds trivially. It is a closed arithmetic term over mathlib primitives.

Attempt 2: `l.factorial • (((r₁ : ℝ) + 1) ^ p * B * 2 ^ (p * r₁)) ^ l`, the RHS shape of `Matrix.det_le`.
- Result: succeeds (evidence (3), `rw [lem6M, nsmul_eq_mul]; ring`).

Conclusion: COMPOSABLE. It is one arithmetic expression over mathlib primitives, with no new mathematics.

### Verdict: `Roth.lem6M`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): the constant appears only in the project's source, clean.tex l.724. The wider literature (Roth 1955; Bombieri–van der Poorten; arXiv 2502.00731; Hadamard-type determinant bounds) uses the technique with different constants. There is no standard object.
- Generality analysis (Phase 4): MAXIMALLY GENERAL for its role. There is nothing to drop, and changing the codomain is a false generalisation (Q9).
- Mathlib search (Phase 5): building blocks only. The nearest match is the `n! • x^n` shape of `Matrix.det_le`.
- Composition check (Phase 6): COMPOSABLE. It is a closed arithmetic term (evidence (1)–(3)).

**Rationale:**

`Roth.lem6M` names the number `(r₁+1)^{pl} l! B^l 2^{plr₁}` that the source writes as `M` in the proof of Lemma 6. It is a one-line arithmetic expression with no mathematical content beyond its role as a coefficient bound for one particular determinant. The reusable estimate behind it is the bound for coefficients of a determinant of Hasse derivatives. That estimate is the theorem `abs_coeff_det_hasseDeriv_le`, assessed separately, and its general skeleton is mathlib's `Matrix.det_le`. No source outside this proof uses this constant, and mathlib does not add named numeric constants of single proofs.

Belongs-elsewhere check: keep it project-locally. It is not junk:
- the name ties 4 statements (`index_det_le`, `index_le_lem6`, `one_le_lem6M`, `lem6M_lt`) and 2 proofs (`Θ_option_le`, `theta_phi_lt_aux`) to the same `M`;
- the Phase 2b API-name exemption applies locally.

The usual "inline at call sites" refactor for this bucket is not recommended. Inlining would duplicate the four-factor expression about 20 times and decouple the Lemma 6 and Lemma 7 halves, which must agree on `M`. The composition only explains why the def should not go to mathlib.

Mathlib building blocks:
- `Nat.factorial` (Mathlib/Data/Nat/Factorial/Basic.lean);
- `Matrix.det_le` (Mathlib/LinearAlgebra/Matrix/AbsoluteValue.lean) for the `n! • x^n` shape;
- the powers and casts.

Composition sketch (≤3 lines):
```lean
example (p r₁ : ℕ) (B : ℝ) (l : ℕ) :
    Roth.lem6M p r₁ B l = l.factorial • (((r₁ : ℝ) + 1) ^ p * B * 2 ^ (p * r₁)) ^ l := by
  rw [Roth.lem6M, nsmul_eq_mul]; ring
```

Call sites in our project (from Phase 6.0): about 20 lines in Roth/Theta.lean across 6 declarations, and 0 in other files.

Refactor plan: none required. Keep `Roth.lem6M` as the paper's `M`, and do not upstream it.

Next action: no upstreaming. Leave the def and its call sites as they are.

---

### Next step

No upstreaming. Keep `Roth.lem6M` in Roth/Theta.lean. Any reusable content (the determinant coefficient bound) is tracked under `Roth.abs_coeff_det_hasseDeriv_le`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.lem6M/lem6M_probes.lean` imports `Roth.Theta`. `lake env lean` compiled it with no output in 38 s. It checks three things:
  - (1) `lem6M` unfolds by `rfl`;
  - (2) `lem6M p r₁ B l = l! * ((r₁+1)^p * B * 2^(p*r₁))^l` by `ring`;
  - (3) the same as `l! • x^l`, the `Matrix.det_le` shape.
- Mathlib grep for `lem6M`: no hits.
- Project grep `grep -rn lem6M Roth/`: all hits are in Theta.lean (see the call-sites table).
- Lean-Finder (1), LeanSearch (1) and Loogle (1) queries, as in the search-status block.
- WebSearch: 3 queries (literature table).
- ChatGPT MCP: n/a (not configured).
- Local refs: clean.tex l.724, 736, 973.
