---
decl: Roth.lem6Φ
file: Roth/Theta.lean
line: 275
kind: def
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: lem6Φ is the proof-internal quantity Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1}) of Lemma 6 (clean.tex eq. 15); it is a one-line sum of two project Θ terms (rfl, compiled), and Θ itself is NO-composable, so there is nothing to upstream.
action: Do not upstream; keep Roth.lem6Φ in Roth/Theta.lean as the paper's Φ shared by index_separated_mul_le_aux, index_det_le, index_le_lem6, Θ_option_le and theta_lt_succ_aux; no call-site changes.
---

# Roth.lem6Φ

## Inventory entry

### `def Roth.lem6Φ`
- **Type**: `{τ : Type*} [Fintype τ] (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) : ℝ`
- **What**: The quantity `Φ` of Lemma 6. It is `Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1})`. The variables are indexed by `Option τ`, and the distinguished last variable `p` is `none`.
- **How**: Direct definition `Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) + Θ M (q ∘ some) fun j ↦ l * r (some j)`. It is a sum of two instances of the project's `Θ`, and there is no proof.
- **Hypotheses**: `[Fintype τ]`, which `Θ` requires. The section variable `[DecidableEq τ]` is not taken.
- **Uses from project**: `Roth.Θ`
- **Used by**: Roth/Theta.lean only:
  - private `index_separated_mul_le_aux` (statement 420; `rw [lem6Φ, ...]` at 449)
  - `index_det_le` (statement 467)
  - `index_le_lem6` (statement 562–563; `let Φ := lem6Φ ...` at 574)
  - `Θ_option_le` (597–598, 602–603)
  - private `theta_lt_succ_aux` (`simp only [lem6Φ, ...]` at 927)
  - module docstring (29)
- **Visibility**: public
- **Lines**: 273–276 (docstring plus 2-line def). Proof length is 0 lines.
- **Notes**: Source is clean.tex §5, Lemma 6, eq. (15) (l.720). It is paired with `Roth.lem6M` (eq. (16)), which is always the `M` argument at the call sites.

## Junk check (Step 8)
- **Used anywhere?** Yes. It is used in 5 declarations of Theta.lean, and it appears in the statements of `index_det_le`, `index_le_lem6` and the private `index_separated_mul_le_aux`.
- **Wrapper of 1–2 mathlib calls?** No. It wraps two calls of the project def `Θ`, not mathlib.
- **Does mathlib have it?** No. Mathlib has no index or `Θ` (see `Roth.Θ.md`). Lean-Finder, LeanSearch and Loogle return nothing relevant.
- **Too specific (inline?)?** Inlining would repeat a two-term `Θ` sum, with reindexing `q ∘ some` and `fun _ : Unit ↦ q none`, about 8 times. That includes inside `Finset.sup'` lambdas and under a square root. The name mirrors the paper's `Φ` and ties the Lemma 6 statement (`index_le_lem6`, `Θ_option_le`) to its use in Lemma 7 (`theta_lt_succ_aux`).
- **Well-chosen definition?** Yes. The `M` and `l` are left as parameters rather than hard-wiring `lem6M`, so the private `index_separated_mul_le_aux` can use it for an arbitrary `M`.

Conclusion: **KEEP**. No action needed.

## Mathlibable assessment (Step 9)

Pre-filter:
- The def is public and the name does not end in `_aux`.
- The docstring does not start with internal/auxiliary.
- Step 8 said KEEP.
- `grep -rn lem6Φ .lake/packages/mathlib/Mathlib` finds nothing.
- It is not a glue lemma; it is a def.

None of these fire, so this is a full run. The parent `Roth.Θ` is `NO-composable-from-mathlib`, so no re-aim is needed.

### Baseline (Phase 0)
- lake build:               clean (the project is built per the brief; the evidence file importing `Roth.Theta` compiles)
- decl `Roth.lem6Φ`:         resolved at Roth/Theta.lean:275
- kind:                      def (noncomputable)
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5, 6, 7 bounding it.

### Statement (Phase 1)

`Roth.lem6Φ` is a definition of a real number. Take a finite index type `τ`, which gives `p = |τ| + 1` variables indexed by `Option τ` with `none` as the last one. Take positive integers `q_j` and degree bounds `r_j`, a real `M` and a natural `l`. It sets

  `Φ = Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1, …, q_{p-1}; l r_1, …, l r_{p-1})`.

The first term is the supremum of indices of one-variable polynomials (height ≤ M, degree ≤ l r_p) at rationals with denominator `q_p`. The second term is the same in the other `p − 1` variables. Lemma 6 bounds `ind F ≤ l Φ` for the Wronskian determinant `F = U(x_1..x_{p-1}) V(x_p)`. This works because the index is additive on products in separated variables.

Variables / typeclasses involved (Lean side):
- `τ`, `[Fintype τ]`: indexes the first `p − 1` variables. `Fintype` is required by `Θ`.
- `q r : Option τ → ℕ`: the denominators and degree bounds.
- `M : ℝ`: the height bound (`lem6M ...` at every public call site).
- `l : ℕ`: the Wronskian order, which scales the degrees.

Hypotheses (Lean side):
- none.

Conclusion (math): a real number, nonnegative because `Θ ≥ 0`.

Conclusion (Lean): n/a, this is a definition.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: it is a proof-internal quantity of one lemma (eq. (15)), not a new structure, not a main result and not a named theorem.

(The literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 1 substantive line
One-liner verdict: ONE-LINER

| Exemption                         | Applies? | Evidence |
|-----------------------------------|----------|----------|
| Avoid defeq abuse                | no       | it unfolds by `rfl` (evidence (1)); consumers unfold it with `rw [lem6Φ]` / `simp only [lem6Φ, ...]`, and nothing relies on sealing |
| Avoid typeclass diamonds         | no       | it is a real number, not an instance |
| Mark semantic intent / API name  | yes (project-local) | it is the paper's `Φ`, shared between `index_det_le`, `index_le_lem6`, `Θ_option_le` and `theta_lt_succ_aux` |

Conclusion: ONE-LINER WITH-EXEMPTION. The exemption is project-local only and does not argue for mathlib.

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth theorem proof Lemma 6 Phi = Theta_1(M; q_p; l r_p) + Theta_{p-1} index bound induction | no | — | general Roth expositions (math.uh.edu roth.pdf, arXiv 2502.00731, Bombieri–van der Poorten corrigenda); none names this Φ |
| 2 | WebSearch (general form) | Roth's lemma index of polynomial at rational point supremum Theta_m(B; q; r) Cassels induction on number of variables | partial | Θ_m(B; h/q; r) and the inductive Roth lemma (Ridout-style, arXiv math/0307203; arXiv 2502.00731 Lemma 3.9) | the induction step bounds the index through the factorisation `U(x')V(x_p)`; the sum of the two Θ's appears only implicitly, not as a named object |
| 3 | WebSearch (named-after / aliases) | index of product of polynomials in separated variables additivity Roth lemma generalized Wronskian factorization Theta sum | partial | index of a product in separated variables (arXiv 1305.0926, GIT and Roth) | the technique (index additivity on separated products) is standard; there is no named constant |
| 4 | ChatGPT MCP | — | n/a | — | the `ask_chatgpt_math` MCP is not configured in this session (no such tool available) |
| 5 | Local references | `.mathlib-quality/references/clean.tex` grep `Phi` | yes | l.720 eq. (15) `\Phi = \Theta_1(M; q_p; lr_p) + \Theta_{p-1}(M; q_1..q_{p-1}; lr_1..lr_{p-1})`; l.772–776 `ind F ≤ lΦ`; l.1010 Lemma 7 estimate | matches the Lean def exactly (last variable = `none`) |
| 6 | nLab | index of polynomial / Roth's lemma | no | — | nLab has no entry for Diophantine-approximation proof constants |
| 7 | nCatLab | — | n/a | — | not a categorical concept |
| 8 | Stacks Project | — | n/a | — | not algebraic geometry |
| 9 | MathOverflow / Math.SE | (results of #2, #3) | partial | discussions of Roth's lemma induction | folklore technique; no canonical Φ |
| 10 | recent arXiv (last 5 years) | (results of #1, #2) | partial | arXiv 2502.00731 (2025) | it runs the induction with its own bookkeeping and no Φ |

### Literature summary (Phase 3)

Concept identified as: the proof-internal quantity `Φ` in the induction step (Lemma 6) of the Ridout/Cassels-style Roth lemma. It is the sum of the two `Θ` bounds for the separated factors `V(x_p)` and `U(x_1..x_{p-1})` of the Wronskian.

Sources agree on the standard form: no. Each exposition organises the induction differently, and none of the sources found names this sum.

Most general standard form: the underlying technique, `ind(U(x')V(x_p)) = ind U + ind V`. That is the project lemma `index_mul` together with `index_rename`. The sum of the two suprema is not a standard object.

Generality dimensions where the literature varies:
  - which variable is split off (first or last);
  - whether the degrees are scaled by `l` inside `Θ` or by renormalising the index.

Disagreement with the literature: none. It matches clean.tex eq. (15) verbatim.

### Generality analysis — `Roth.lem6Φ`

Literature-standard form (from Phase 3): there is none. It is a proof-specific quantity.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `[Fintype τ]` | finite index type | finitely many variables | no | `Θ` takes `[Fintype σ]`; dropping it fails to elaborate (evidence (2)) |
| 2 | `[DecidableEq τ]` (section variable) | not taken | not needed | already absent | `#check @lem6Φ` shows only `[Fintype τ]` |
| 3 | `Option τ` indexing | `none` = last variable | `p` variables, split last | no (equivalent) | `Fin (n+1)` / `Sum` indexing would be isomorphic; `Option` matches the `Θ_option_le` / `finSuccEquivLast` transport |
| 4 | `M : ℝ` | arbitrary real | `M` from eq. (16) | already weaker | not hard-wired to `lem6M`; `index_separated_mul_le_aux` uses it with a general `M` |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL (for its role). The only instance is required by `Θ`.
Number of weakening opportunities found: 0
Proposed restatement: none
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream this enables |
|---|---|---|---|---|
| 1 | preambles to typeclasses? | no | — | there are no hypotheses |
| 2 | sequences to filters? | no | — | it is a finite sum of two suprema |
| 3 | construction vs universal property? | no | — | it is a number |
| 4 | bundled substructure? | no | — | it is not a set |
| 5 | field-specific to semiring? | no | — | the codomain `ℝ` is that of `Θ` |
| 6 | higher-categorical? | no | — | — |
| 7 | concrete index to general? | no | — | the `Option τ` split is intrinsic to the induction step |
| 8 | concrete-via-abstract? | no | — | there is no proof body |
| 9 | false-generalisation guard | n/a | no generalisation proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
One-line reason: it is a named sum of two values of a project-local def. There is no organisational improvement to make.

### Proof strategy — `Roth.lem6Φ`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers | no (for this def) | the reusable content is index additivity (`index_mul`, `index_rename`), assessed separately | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It is a definition with no proof.

### Diamond / defeq risk — `Roth.lem6Φ`

| # | Risk | Verdict | Evidence / rationale |
|---|---|---|---|
| 1 | Typeclass diamond | none | it defines no instances; `Fintype Unit` and `Fintype τ` are canonical |
| 2 | Reducibility leak | none | it is a plain semireducible noncomputable def, unfolded by `rfl` (evidence (1)) and explicitly by `rw`/`simp only` |
| 3 | Non-canonical unfolding | low | `simp only [lem6Φ, Function.comp_def, ...]` in `theta_lt_succ_aux` must also normalise `q ∘ some` after the `finSuccEquivLast` transport; this works |
| 4 | Instance priority collision | none | it is not an instance |
| 5 | Universe-polymorphism issues | none | `τ : Type*` is universe-polymorphic, and `Unit` is used at `Type` for the first `Θ`, with no constraint forced |
| 6 | Coercion ambiguity | none | it uses only `ℕ → ℝ` casts inside `Θ` |

### Risk verdict (Phase 4.5)

Overall risk: NONE
Top risks: none
Recommended mitigations: n/a

### Mathlib search-status: `Roth.lem6Φ`

- [A] Lean-Finder, query "sum of supremum of indices of polynomials in one variable and in remaining variables, index of polynomial at a rational point":
  - hits: `ChevalleyThm.*Bound` and `MvPolynomial.schwartz_zippel_sum_degreeOf`, none relevant.
- [B] Loogle, query `(Option ?τ → ℕ) → ℝ → ℕ → ℝ`:
  - no hits.
- [C] LeanSearch, query "index of a multivariate polynomial at a point with respect to weights":
  - hits: only the `MvPolynomial.IsWeightedHomogeneous` / `weightedHomogeneousComponent` API, with no index.
- [D] Grep mathlib src for `lem6Φ`:
  - none. `Roth.Θ.md` records that mathlib has no `Θ` or index.
- [E] Name pattern, `lean_local_search`:
  - not needed beyond [D]. The qualified name is project-specific.

Searched for both the user's form (the Φ sum) and the literature-standard form (index additivity / Θ of separated variables).

Concluded: found building blocks only. Mathlib provides `sSup`, `+`, `Option` and `Function.comp`; `Θ` is project-local. Nothing in mathlib is this quantity.

### Normal-form check — `Roth.lem6Φ`

Equivalent formalisms:
- (a) `Θ_1(...) + Θ_{p-1}(...)` (current, the paper's order);
- (b) the swapped sum `Θ_{p-1} + Θ_1`. `index_separated_mul_le_aux` bridges to it with `add_comm`.

Does mathlib already have a canonical form for this idea? No.

The def follows the source order (a).

RHS convention respected? n/a. This is a def.

### Syntactic generality — `Roth.lem6Φ`

Alternative restatements attempted:
- hard-wire `M := lem6M (Fintype.card τ + 1) r₁ B l`. This was rejected because it loses the general-`M` use in `index_separated_mul_le_aux`.
- index by `Fin (n+1)`. This was rejected because `Option τ` is what `Θ_option_le` and the `Θ_equiv` / `finSuccEquivLast` transport use.

Chosen restatement: current.
Justification: it matches eq. (15), and the general `M` keeps the private helper reusable.

### Superfluous-argument audit — `Roth.lem6Φ`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `[Fintype τ]` | yes | required by `Θ` (evidence (2)) |
| 2 | `q`, `r` | yes | arguments of both `Θ` |
| 3 | `M` | yes | height bound of both `Θ` |
| 4 | `l` | yes | degree scaling |
| 5 | section `[DecidableEq τ]` | not taken | absent from the signature |

### Statement-shape verdict (Phase 5.5)

- Normal form: OK
- Syntactic generality: OK
- Superfluous arguments: NONE

Overall: SHIP-AS-STATED (as a project def)

### Call sites — `Roth.lem6Φ`

Internal use count: 0 outside the declaring file. There are about 10 lines in Theta.lean itself.
External-to-file callers: 0 distinct files.

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:420 | private `index_separated_mul_le_aux ... ≤ l * lem6Φ q r M l` |
| Roth/Theta.lean:449 | `rw [lem6Φ, mul_add, add_comm]` (proof of the same) |
| Roth/Theta.lean:467 | `index_det_le ... ≤ l * lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l` |
| Roth/Theta.lean:562–563 | `index_le_lem6 ... 2 * (lem6Φ q r (lem6M ...) l + √(lem6Φ q r (lem6M ...) l) + √δ)` |
| Roth/Theta.lean:574 | `let Φ := lem6Φ q r (lem6M (Fintype.card τ + 1) r₁ B l) l` (proof of `index_le_lem6`) |
| Roth/Theta.lean:597–603 | `Θ_option_le`: `Finset.le_sup' (fun l ↦ lem6Φ q r (lem6M ...) l + √(...) + √δ) ...` |
| Roth/Theta.lean:927 | private `theta_lt_succ_aux`: `simp only [lem6Φ, e, Function.comp_def, finSuccEquivLast_symm_none, ...]` |

Inline-derivation grep: none. The private `theta_phi_lt_aux` (840) works with the unfolded `Θ` sum after `theta_lt_succ_aux` unfolds `lem6Φ`. That is a consumer of the unfolding, not an independent re-derivation of the name.

### Composition check (Phase 6)

Can `Roth.lem6Φ` be derived from mathlib in ≤3 chained calls?

Attempt 1: the body, `Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) + Θ M (q ∘ some) fun j ↦ l * r (some j)`.
- Decls used: `Roth.Θ` (project, itself NO-composable: one `sSup` over the project's `indexSet`), `HAdd`, `Function.comp`, `Option.some`.
- Result: succeeds by `rfl` (evidence (1)).

Conclusion: COMPOSABLE. It is two applications of `Θ` and one `+`, with no new mathematics. The non-mathlib ingredient `Θ` is itself project-local and NO-composable (`Roth.Θ.md`).

### Verdict: `Roth.lem6Φ`

**Category:** NO-composable-from-mathlib

**Evidence:**
- Literature search (Phase 3): `Φ` appears only in the project source, clean.tex eq. (15). The wider literature (Ridout/Cassels-style Roth lemma, arXiv math/0307203, 2502.00731, 1305.0926) uses index additivity on separated products but names no such sum.
- Generality analysis (Phase 4): MAXIMALLY GENERAL. The only instance, `[Fintype τ]`, is forced by `Θ` (evidence (2)).
- Mathlib search (Phase 5): there are no hits, and mathlib has no index or `Θ` at all.
- Composition check (Phase 6): COMPOSABLE. The def is `Θ + Θ` by `rfl`.

**Rationale:**

`Roth.lem6Φ` names the sum `Θ_1(M; q_p; l r_p) + Θ_{p-1}(M; q_1..q_{p-1}; l r_1..l r_{p-1})` that the source calls `Φ` in Lemma 6. It is a one-line sum of two applications of the project's `Θ`. `Θ` itself was assessed `NO-composable-from-mathlib` as a Roth-proof-specific quantity. A named sum of two such quantities, particular to one induction step, has even less claim to mathlib. The reusable mathematics behind it is the additivity of the index on products in separated variables. That lives in `index_mul` / `index_rename`, which are assessed separately.

Belongs-elsewhere check: keep it project-locally. The Phase 2b API-name exemption applies locally:
- the name ties the statements of `index_det_le`, `index_le_lem6` and `Θ_option_le` to the Lemma 7 estimate in `theta_lt_succ_aux` / `theta_phi_lt_aux`;
- inlining would duplicate a reindexed two-term `Θ` sum about 8 times, including under `√` and inside `Finset.sup'` lambdas.

The usual "inline at call sites" refactor for this bucket is therefore not recommended. The composition only explains why the def should not go to mathlib.

Mathlib building blocks:
- `sSup` (through `Roth.Θ`);
- `HAdd.hAdd`, `Function.comp`, `Option.some` (core / Mathlib.Logic.Function.Basic).

Composition sketch (≤3 lines):
```lean
example {τ : Type*} [Fintype τ] (q r : Option τ → ℕ) (M : ℝ) (l : ℕ) :
    Roth.lem6Φ q r M l = Roth.Θ M (fun _ : Unit ↦ q none) (fun _ ↦ l * r none) +
      Roth.Θ M (q ∘ some) (fun j ↦ l * r (some j)) := rfl
```

Call sites in our project (from Phase 6.0): about 10 lines in Roth/Theta.lean across 5 declarations (`index_separated_mul_le_aux`, `index_det_le`, `index_le_lem6`, `Θ_option_le`, `theta_lt_succ_aux`), and 0 in other files.

Refactor plan: none required. Keep `Roth.lem6Φ` as the paper's `Φ`, and do not upstream it.

Next action: no upstreaming. Leave the def and its call sites as they are.

---

### Next step

No upstreaming. Keep `Roth.lem6Φ` in Roth/Theta.lean. The reusable content (index additivity on separated products) is tracked under `Roth.index_mul` / `Roth.index_rename`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.lem6Φ/lem6Phi_probes.lean` imports `Roth.Theta`, and `lake env lean` compiles it cleanly in 39 s. It contains:
  - (1) `lem6Φ q r M l = Θ ... + Θ ...` by `rfl`;
  - (3) `#check @lem6Φ`, which shows that only `[Fintype τ]` is taken.
- Probe (2), run once (42 s): the body without `[Fintype τ]` fails with `failed to synthesize Fintype τ`, so the instance is essential. That probe was then replaced by a comment so the file compiles.
- Mathlib grep for `lem6Φ`: no hits.
- Project grep `grep -rn lem6Φ Roth/`: all hits are in Theta.lean (see the call-sites table).
- Lean-Finder (1), LeanSearch (1) and Loogle (1) queries, as in the search-status block.
- WebSearch: 3 queries (literature table).
- ChatGPT MCP: n/a (not configured).
- Local refs: clean.tex l.720, 772–776, 1010.
