---
decl: Roth.Θ_equiv
file: Roth/Theta.lean
line: 159
kind: theorem
visibility: public
verdict: NO-composable-from-mathlib
cost: n/a
junk: KEEP
rationale: Renaming invariance of the project-local supremum Θ, proved as congrArg sSup of a set equality built from two applications of the private indexSet_comp_subset (rename e, index_rename); the only general content is reindexing a supremum along an equivalence (mathlib Equiv.iSup_congr / renameEquiv), so nothing goes upstream.
action: Do not upstream; keep in Roth/Theta.lean as the paper-requested renaming lemma for Θ (single caller Theta.lean:919 in the Lemma 7 transport to Option (Fin (n+1))); no call-site changes.
---

# Roth.Θ_equiv

## Inventory entry

### `theorem Roth.Θ_equiv`
- **Type**: `∀ {σ : Type*} [Fintype σ] {τ : Type*} [Fintype τ] (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ), Θ B (q ∘ e) (r ∘ e) = Θ B q r`
- **What**: `Θ_m(B; q; r)` does not change when the variables are relabelled by a bijection `e : σ ≃ τ`, with the denominators `q` and weights `r` relabelled along with them.
- **How**: `congrArg sSup` reduces the goal to the set equality `indexSet B (q ∘ e) (r ∘ e) = indexSet B q r`. That equality is `subset_antisymm` of two instances of the private helper `indexSet_comp_subset`, applied to `e` and to `e.symm`. The second instance is massaged by `simpa [Function.comp_def]`, using `e.symm ∘ e = id`. The helper sends a witness `R` to `rename e R`, using `rename_eq_zero_iff_of_injective`, `degreeOf_rename_of_injective`, `coeff_rename_mapDomain`, `map_rename` and the project's `index_rename`.
- **Hypotheses**: `e : σ ≃ τ` is a genuine bijection, needed for an equality and not just one inequality. `B` is arbitrary, with no `1 ≤ B`. Only `[Fintype σ]` and `[Fintype τ]` are needed; the section's `[DecidableEq σ]` is omitted.
- **Uses from project**: `Roth.Θ`, `Roth.indexSet`, `Roth.indexSet_comp_subset` (private, Theta.lean:141). The helper in turn uses `Roth.RSet`, `Roth.index` and `Roth.index_rename`.
- **Used by**: Roth/Theta.lean:919. That is the Lemma 7 proof, which transports from `Fin (n + 2)` to `Option (Fin (n + 1))` via `finSuccEquivLast`, with the rewrite `rw [← Θ_equiv e.symm ...]`. Theta.lean:34 is a module-docstring mention. Nothing outside Theta.lean uses it (`grep -rn Θ_equiv Roth/`).
- **Visibility**: public
- **Lines**: 156–163 (docstring 157–158, statement 159–160, proof 161–163), proof length 3 lines
- **Notes**: Source: clean.tex l.630–634 ("Prove invariance under nonzero scalars and variable renaming ... as separate lemmas, so later proofs do not repeat the conversions"). The name `Θ_equiv` is slightly unusual. Mathlib would say `Θ_comp_equiv` or `Θ_rename`. This is a cosmetic point only.

## Junk check (Step 8)
- **Used anywhere?** Yes, once, at Theta.lean:919 (Lemma 7). There it is essential for reducing `Fin (n+2)` to the `Option` form that `Θ_option_le` expects.
- **Wrapper of 1–2 mathlib calls?** No. It is `congrArg sSup` plus `subset_antisymm` over a project helper that carries a 10-line renaming argument.
- **Does mathlib have it?** No. It is about the project-local `Θ`. The analogous generic fact is `Equiv.iSup_congr`.
- **Too specific (inline?)?** No. The source explicitly asks for a separate renaming lemma, and inlining it would expose `indexSet` at the Lemma 7 call site.
- **Well-chosen?** Yes. It has no superfluous hypotheses (`B` is arbitrary, and only `Fintype` is required), and the bijection is needed for equality.
- **Conclusion:** `KEEP`. No action. An optional rename to `Θ_comp_equiv` is cosmetic.

## Mathlibable assessment (Step 9)

Pre-filter checks:
- The theorem is public.
- The name does not end in `_aux`.
- The docstring is not internal/auxiliary.
- Step 8 said KEEP.
- No `namespace Roth` exists under `.lake/packages/mathlib/Mathlib/`.

This is not a glue lemma, because the body is a genuine set-equality argument. The full run follows. The parent `Roth.Θ` is NO-composable-from-mathlib, so no re-aim applies.

### Baseline (Phase 0)
- lake build:               clean (project built per the brief; the evidence file importing `Roth.Theta` elaborates with no errors or warnings)
- decl `Roth.Θ_equiv`:       resolved at Roth/Theta.lean:159
- kind:                      theorem
- has sorry:                 no
- module docstring summary:  `Θ_m(B; q; r)`, the supremum of indices of bounded integer polynomials at rational points, and Lemmas 5–7 bounding it

### Statement (Phase 1)

`Roth.Θ_equiv` is a theorem stating the following.

Let `e : σ → τ` be a bijection between finite index sets. For every `B ∈ ℝ` and every `q, r : τ → ℕ`, we have `Θ_σ(B; q∘e; r∘e) = Θ_τ(B; q; r)`. Here `Θ(B; q; r)` is the supremum of `ind(R; (h_j/q_j)_j; r)` over nonzero `R ∈ ℤ[X_j]` with `deg_{X_j} R ≤ r_j` and `|coeff| ≤ B`, and over `h` with `gcd(h_j, q_j) = 1`. In words, `Θ` is symmetric under relabelling the variables.

Variables / typeclasses involved (Lean side):
- `σ`, `τ` with `[Fintype]`: the two variable sets.
- `e`: the relabelling.
- `B`: the coefficient bound.
- `q`: the denominators.
- `r`: the degree bounds and weights.

Hypotheses (Lean side): none beyond `e` being an `Equiv`.

Conclusion (math): `Θ` is invariant under variable renaming.

Conclusion (Lean): `Θ B (q ∘ e) (r ∘ e) = Θ B q r`.

### Size classification (Phase 2a)

Verdict: SMALL
Reason: a transport/symmetry API lemma for a project-local supremum, not a main result.

(Note: literature width is EXHAUSTIVE regardless.)

### One-line check (Phase 2b)

Body line count: 3 substantive lines
One-liner verdict: n/a (kind is theorem)
Conclusion: MULTI-LINE check skipped (theorem).

### Literature search table — EXHAUSTIVE protocol

| # | Channel | Query | Hit? | Standard form found | Notes |
|---|---------|-------|------|---------------------|-------|
| 1 | WebSearch (specific form) | Roth's theorem index of polynomial invariance under permutation of variables Theta_m supremum Cassels | partial | Yamada arXiv math/0307203 defines the index and Θ_m (sup over bounded-height polynomials) | symmetry under permuting variables is tacit, never stated |
| 2 | WebSearch (general form) | supremum of image set invariant under bijection reparametrization sSup image equiv | yes | reindexing a supremum along a bijection leaves it unchanged (mathlib `Equiv.iSup_comp` / `Equiv.iSup_congr` docs surfaced) | the entire abstract content |
| 3 | WebSearch (named-after / aliases) | Ridout theorem Roth lemma index rational point symmetric in variables relabeling polynomials bounded height | partial | Yamada math/0307203, arXiv 2502.00731, arXiv 1305.0926 | no relabelling lemma stated; papers silently reorder variables |
| 4 | ChatGPT MCP | n/a | n/a | n/a | the `ask_chatgpt_math` MCP is not configured in this session (absent from the tool list) |
| 5 | Local references | grep clean.tex for "renam" | yes | clean.tex l.630–634: the Lean note asks to "Prove invariance under nonzero scalars and variable renaming" as separate lemmas | it is requested as bookkeeping, not as a theorem of the paper |
| 6 | nLab | supremum / join under reindexing | partial | the colimit (join) of a diagram is invariant under an isomorphism of index categories | generic, nothing Roth-specific |
| 7 | nCatLab | n/a | n/a | n/a | not a categorical concept (an equality of reals) |
| 8 | Stacks Project | n/a | n/a | n/a | not algebraic geometry; no index-of-a-polynomial notion |
| 9 | MathOverflow / Math.SE | covered by searches 1–3 | no | n/a | too elementary to have a thread |
| 10 | recent arXiv (last 5 years) | arXiv 2502.00731 (2025), from searches 1 and 3 | partial | Roth's lemma in m and m−1 variables | the variables are reordered without comment |

### Literature summary (Phase 3)

Concept identified as: symmetry of Ridout/Cassels' `Θ_m(B; q; r)` under permuting the variables (with `q` and `r` permuted along).
Sources agree on the standard form: yes. It is tacit, and every source treats the variables as unordered.
Most general standard form: a supremum over a family indexed by a set is unchanged under reindexing by a bijection (`Equiv.iSup_congr`). Here the bijection is `R ↦ rename e R`, `h ↦ h ∘ e.symm` on the parameter space, and it preserves the index by `index_rename`.
Generality dimensions where the literature varies: none.
Disagreement with the literature: none.

### Generality analysis — `Roth.Θ_equiv`

Literature-standard form: `Θ` is invariant under any bijective relabelling of the variables.

| # | Parameter / hypothesis | Current Lean form | Literature-standard form | Weaker form exists? | Reason it can/can't be weakened |
|---|---|---|---|---|---|
| 1 | `e : σ ≃ τ` | equivalence | bijection | NO (for equality) | An injection gives only one inclusion (one inequality), and the conclusion is an equality between Θ over different variable sets. Any inequality for embeddings would be a different statement; it is not claimed or compiled here. |
| 2 | `B : ℝ` | arbitrary | arbitrary | already general | no `1 ≤ B` (signature check, evidence (1)) |
| 3 | `[Fintype σ]`, `[Fintype τ]` | required | finite variable set | NO | `Θ`/`index` are defined only under `Fintype` |
| 4 | `[DecidableEq σ]` | omitted | n/a | already absent | evidence (1) |

### Generality verdict (Phase 4b)

The current form is: MAXIMALLY GENERAL
Number of weakening opportunities found: 0
Proposed restatement: none.
Cost of restatement: n/a

### Modern-idiom check (Phase 4c)

| # | Question | Applies? | Proposed reformulation | Mathlib downstream |
|---|---|---|---|---|
| 1 | Typeclasses instead of preambles? | no | no preamble hypotheses | — |
| 2 | Sequences vs filters? | no | an equality of suprema | — |
| 3 | Construction vs universal property? | no | — | — |
| 4 | Bundled substructure? | no | `indexSet` is a plain set of reals | — |
| 5 | Field-specific vs typeclass-weakened? | no | ℝ-valued by the definition of `index` | — |
| 6 | Higher-categorical? | no | — | — |
| 7 | Concrete index generalised? | no | arbitrary finite types already | — |
| 8 | Concrete-via-abstract? | yes, trivially | After unfolding, the proof is reindexing a supremum along the bijection `rename e`. The abstract form already exists in mathlib (`Equiv.iSup_congr`). It would apply literally only if `Θ` were written as an `iSup` over a sigma type. | none |
| 9 | False-generalisation guard | no false generalisation | no widening proposed | — |

### Modern-idiom verdict (Phase 4c)

Modern idiom available: no.
  - Reason: the abstract content is already mathlib's `Equiv.iSup_congr` with `MvPolynomial.renameEquiv`. Rewriting `Θ` as an `iSup` would be a project-local refactor, not a mathlib contribution.

### Proof strategy — `Roth.Θ_equiv`

| # | Question | Applies? | Idiomatic alternative | Cost of switch |
|---|---|---|---|---|
| 1 | ε-δ vs filters | no | — | — |
| 2 | elements vs ideals | no | — | — |
| 3 | sequences vs nets | no | — | — |
| 4 | construction vs universal property | no | — | — |
| 5 | missing mathlib helpers? | no | all renaming facts used (`degreeOf_rename_of_injective`, `coeff_rename_mapDomain`, `rename_eq_zero_iff_of_injective`, `map_rename`) are already in mathlib | — |

### Proof strategy verdict (Phase 4.6)

Current strategy: MATHLIB-IDIOMATIC. It proves one inclusion for a general equivalence and applies it to `e` and `e.symm` via `subset_antisymm`. This is the standard "prove ≤ once, use the inverse" pattern.

### Diamond / defeq risk

n/a — declaration kind is theorem.

### Mathlib search-status: `Roth.Θ_equiv`

[A] Lean-Finder       "supremum over a family reindexed by an equivalence is unchanged"   hits: `Equiv.iSup_comp`, `Equiv.iSup_congr`, `Equiv.biSup_comp`, `Set.BijOn.iSup_congr`, `Set.BijOn.iSup_comp` (building blocks)
[B] Loogle            `sSup (Set.range (?f ∘ ⇑?e)) = sSup (Set.range ?f)`   n/a: query error ("cannot coerce to function ?e"); covered by [A] and [D]
[C] LeanSearch        "supremum of index of multivariate polynomials invariant under renaming variables by an equivalence"   hits: `Equiv.iSup_comp`, `MvPolynomial.totalDegree_renameEquiv`, `MvPolynomial.rename_hsymm`, `MvPolynomial.totalDegree_rename_le` (analogues for other invariants; nothing about an index supremum)
[D] Grep mathlib src  `namespace Roth` (no hits); `Equiv.iSup_comp` (Mathlib/Order/CompleteLattice/Basic.lean:185); `Equiv.iSup_congr` (Basic.lean:195); `def renameEquiv` (Mathlib/Algebra/MvPolynomial/Rename.lean:213)
[E] Name pattern      `Equiv.iSup_congr`, `renameEquiv` (mathlib); `index_rename`, `Θ_equiv` (project only)

Searched for both:
  - the user's form (Θ renaming invariance): not in mathlib (no Θ)
  - the literature-standard form (a supremum is invariant under reindexing by a bijection): `Equiv.iSup_congr`

Concluded: found building blocks (`Equiv.iSup_congr` / `Equiv.iSup_comp`, `MvPolynomial.renameEquiv`, the mathlib renaming lemmas, and the project's `index_rename`); composition gives our form.

### Normal-form check — `Roth.Θ_equiv`

Equivalent formalisms:
- `Θ B (q ∘ e) (r ∘ e) = Θ B q r` (current)
- `Θ B q r = Θ B (q ∘ e.symm) (r ∘ e.symm)` (a one-line corollary, evidence (2))

Does mathlib already have a canonical form? The mathlib convention for invariants under renaming is `f (rename e p) = f p` or `f (g ∘ e) = f g`, with the "simpler" side on the RHS, for example `totalDegree_renameEquiv` and `Equiv.iSup_comp`. Our statement follows it.
RHS convention respected? yes

### Syntactic generality — `Roth.Θ_equiv`

Alternative restatements attempted:
- the current form, with `q r : τ → ℕ` composed with `e`
- the form with `q r : σ → ℕ` and `e.symm` (evidence (2))

Chosen restatement: current.
Justification: the only caller rewrites right-to-left with `e.symm` and then applies `Θ_option_le` to `q ∘ e.symm`. That fits the current form directly.

### Superfluous-argument audit — `Roth.Θ_equiv`

| # | Argument / typeclass | Essentially used? | Notes |
|---|---|---|---|
| 1 | `e : σ ≃ τ` | yes | both directions are needed for equality |
| 2 | `[Fintype σ]`, `[Fintype τ]` | yes | required for `Θ` to be defined |
| 3 | `B`, `q`, `r` | yes | data |
| 4 | `[DecidableEq σ]` | no | already omitted |

### Statement-shape verdict (Phase 5.5)

Normal form: OK
Syntactic generality: OK
Superfluous arguments: NONE

Overall: SHIP-AS-STATED (project-locally; nothing ships upstream)

### Call sites — `Roth.Θ_equiv`

Internal use count: 0 outside the declaring file, 1 inside Roth/Theta.lean.
External-to-file callers: 0 distinct files

| Caller file:line | Usage pattern (one-line excerpt) |
|---|---|
| Roth/Theta.lean:919 | `rw [← Θ_equiv e.symm ((q 0 : ℝ) ^ (δ * r 0)) q r]` (Lemma 7: transport from `Fin (n+2)` to `Option (Fin (n+1))` via `finSuccEquivLast`) |

Inline-derivation grep:
  - (none). `grep -rn "rename e\|Θ_equiv\|indexSet_comp_subset" Roth/` finds only the helper (Theta.lean:141–154) and this caller.

### Composition check (Phase 6)

Can `Roth.Θ_equiv` be derived from mathlib in ≤3 chained calls?

Attempt 1: `congrArg sSup (subset_antisymm (indexSet_comp_subset e B q r) (by simpa [Function.comp_def] using indexSet_comp_subset e.symm B (q ∘ e) (r ∘ e)))`. This is the current proof.
  - Mathlib decls used: `congrArg`, `subset_antisymm`; the project's private `indexSet_comp_subset`.
  - Result: succeeds (it is the shipped proof).
  - Notes: the content sits in the helper. The helper is the bijection on witnesses, `R ↦ rename e R`, `h ↦ h ∘ e.symm`, and each of its fields is one mathlib renaming lemma plus `index_rename`.

Attempt 2 (abstract form): if `Θ` were written as `⨆ (R, h), index ...`, the statement would be one call to `Equiv.iSup_congr` along `(renameEquiv ℤ e).toEquiv.prodCongr (Equiv.arrowCongr e (Equiv.refl ℤ))`, restricted to the constrained subtype, with `index_rename` supplying the pointwise equality.
  - Result: partial (a sketch). The constrained subtype makes it more than a one-liner, and it is not compiled. It only identifies the abstract mathlib content.

Conclusion: COMPOSABLE. The theorem is a short composition of mathlib's renaming lemmas and the generic fact that suprema are invariant under reindexing, applied to the project-local `Θ`.

## Verdict: `Roth.Θ_equiv`

**Category:** NO-composable-from-mathlib

**Evidence:**
- **Literature search (Phase 3):** symmetry of `Θ_m` under relabelling the variables is tacit in Ridout/Cassels/Yamada. The local source requests it only as a bookkeeping lemma (clean.tex l.630–634).
- **Generality analysis (Phase 4):** MAXIMALLY GENERAL. `B` is arbitrary, only `Fintype` is required, and the `Equiv` is needed for equality.
- **Mathlib search (Phase 5):** building blocks `Equiv.iSup_congr`, `Equiv.iSup_comp`, `MvPolynomial.renameEquiv`, and the mathlib `rename` lemmas. There is no Θ in mathlib.
- **Composition check (Phase 6):** COMPOSABLE, as `congrArg sSup` plus `subset_antisymm` over the renaming bijection of witnesses.

**Rationale:**

`Roth.Θ_equiv` says the project-local supremum `Θ` (Ridout/Cassels' `Θ_m`) is unchanged when the variables are relabelled along a bijection. Mathematically, a supremum is invariant under reindexing by a bijection of the index family (mathlib's `Equiv.iSup_congr`). Here that bijection sends `R ↦ rename e R` and `h ↦ h ∘ e.symm`, and the project's `index_rename` preserves the index. Every polynomial fact used is already a mathlib `rename` lemma. `Θ`, `indexSet` and `RSet` are bookkeeping objects of the Roth proof, all NO-composable-from-mathlib, and will not enter mathlib, so there is nothing to upstream.

WHY not: the general content (reindexing a supremum along an equivalence; renaming lemmas for `MvPolynomial`) is already in mathlib. The rest is about a Roth-specific quantity.

Belongs-elsewhere check: keep it project-local in Roth/Theta.lean. The source explicitly asks for a separate renaming lemma so that later proofs do not repeat the conversion. The bucket's default "inline at call sites" step is not recommended. Inlining at Theta.lean:919 would require the `indexSet` set-equality argument there and would make the private helper's job public.

Mathlib building blocks:
- `Equiv.iSup_congr`, `Equiv.iSup_comp` (Mathlib/Order/CompleteLattice/Basic.lean:195, 185)
- `MvPolynomial.renameEquiv` (Mathlib/Algebra/MvPolynomial/Rename.lean:213)
- `MvPolynomial.rename_eq_zero_iff_of_injective`, `MvPolynomial.degreeOf_rename_of_injective`, `MvPolynomial.coeff_rename_mapDomain`, `MvPolynomial.map_rename`
- project `Roth.index_rename` (Roth/Index.lean:212) and the private `Roth.indexSet_comp_subset` (Roth/Theta.lean:141)

Composition sketch (≤3 lines):
```lean
theorem Θ_equiv (e : σ ≃ τ) (B : ℝ) (q r : τ → ℕ) : Θ B (q ∘ e) (r ∘ e) = Θ B q r :=
  congrArg sSup <| subset_antisymm (indexSet_comp_subset e B q r) <| by
    simpa [Function.comp_def] using indexSet_comp_subset e.symm B (q ∘ e) (r ∘ e)
```

Call sites in our project (from Phase 6.0): 1, at Roth/Theta.lean:919.

Refactor plan: none. Keep the lemma and its one caller unchanged. An optional cosmetic rename to `Θ_comp_equiv`, matching mathlib's `_comp_equiv` naming, would touch only Theta.lean:919 and the docstring mention at Theta.lean:34.

Next action: no upstreaming.

## Next step

No upstreaming. Keep `Roth.Θ_equiv` in Roth/Theta.lean as the renaming-invariance API of `Θ` that the source requests (clean.tex l.630–634). Its sole caller is Theta.lean:919.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.Θ_equiv/composition.lean` (imports `Roth.Theta`). `lean_diagnostic_messages` reports success with no errors and only `#check` info. It contains:
  - (1) `#check @Θ_equiv`, confirming that only `[Fintype σ]` and `[Fintype τ]` are needed and that `B` is arbitrary;
  - (2) the inverse-direction corollary via `Θ_equiv e.symm`;
  - (3) the call-site pattern with `finSuccEquivLast`;
  - (4) `#check` of the building blocks `Equiv.iSup_comp`, `Equiv.iSup_congr`, `MvPolynomial.renameEquiv` and `Roth.index_rename`.
  The first check gave one long-line linter warning, which was fixed and re-checked clean.
- WebSearch ×3 (queries in the table). Sources: arXiv math/0307203, arXiv 2502.00731, arXiv 1305.0926, arXiv 1806.10737, and mathlib doc mirrors (Order/Bounds/Image, ConditionallyCompleteLattice).
- Lean-Finder and LeanSearch queries as recorded in Phase 5. The Loogle query errored on its pattern syntax. A grep of `.lake/packages/mathlib/Mathlib/` found no `namespace Roth` and located `Equiv.iSup_comp`, `Equiv.iSup_congr` and `renameEquiv`.
- Local refs: clean.tex l.625–640.
- `grep -rn Θ_equiv Roth/` for the call-sites table.
- Sibling reports reused: Roth.Θ.md (parent verdict), Roth.indexSet_comp_subset.md (helper, SKIP private), Roth.index_rename.md, Roth.Θ_mono.md (format).
- ChatGPT channel: n/a (the `ask_chatgpt_math` MCP is not configured in this session).
