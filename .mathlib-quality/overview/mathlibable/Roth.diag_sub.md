---
decl: Roth.diag_sub
file: Roth/CoeffNorm.lean
line: 199
kind: theorem
visibility: public
verdict: NO-mathlib-has-it
cost: n/a
junk: REPLACE
rationale: Re-aimed at diag = MvPolynomial.aeval (fun _ ↦ X) (an AlgHom), the statement is literally mathlib's map_sub (also MvPolynomial.eval₂_sub), which is already its one-term proof; used at a single simp call site that compiles without it.
action: Optionally delete Roth.diag_sub (Roth/CoeffNorm.lean:197-200) and at its only call site Roth/MainLemma.lean:408 replace `diag_sub` by unfolding `diag` (`simp only [diag] at h ⊢` then `simp [map_sub, Polynomial.sub_modByMonic, h]`, compiled); or keep as a convenience simp lemma while diag is unbundled; no mathlib PR.
---

# Roth.diag_sub

## Inventory entry

### `theorem Roth.diag_sub`
- **Type**: `{σ : Type*} (P Q : MvPolynomial σ ℤ) : diag (P - Q) = diag P - diag Q`
- **What**: The diagonal substitution `P ↦ P(x, …, x)` commutes with subtraction.
- **How**: Term proof `map_sub _ _ _`: `diag P` unfolds by defeq to `MvPolynomial.aeval (fun _ ↦ Polynomial.X) P`, an `AlgHom` application, so the generic `map_sub` (additive form of `map_div`, Mathlib/Algebra/Group/Hom/Defs.lean:461) applies.
- **Hypotheses**: none.
- **Uses from project**: `Roth.diag`
- **Used by**: Roth/MainLemma.lean:408 (`simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]` inside `eval_hasseDeriv_sub_eq_zero`). No other uses (`grep -rn diag_sub Roth/`).
- **Visibility**: public
- **Lines**: 197–200 (docstring 197, statement 198–199, proof 200), proof length 1 line
- **Notes**: Stated over `ℤ` only; the same identity holds over any `CommRing R` (evidence (1)). Docstring has no source citation (it is pure API).

## Junk check (Step 8)
- Used anywhere? Yes, once (Roth/MainLemma.lean:408, as a simp lemma).
- Wrapper of 1–2 mathlib calls? Yes: exactly one, `map_sub`, applied through the defeq `diag P = aeval (fun _ ↦ X) P`.
- Does mathlib have it? Yes: `map_sub` for the `AlgHom` `aeval (fun _ ↦ X)`; also `MvPolynomial.eval₂_sub` (Mathlib/Algebra/MvPolynomial/CommRing.lean:160) since `aeval` is `eval₂ (algebraMap _ _)`.
- Too specific (inline?)? Yes; the one call site already passes `map_sub` to the same simp call, and works with `diag` unfolded instead (evidence (3)).
- Well-chosen? It exists only because `diag` is an unbundled `def`; if `diag` were bundled as an `AlgHom` (parent report recommendation) it would be redundant.
- Conclusion: `REPLACE` by `map_sub` (unfold `diag` at Roth/MainLemma.lean:408). Keeping it is harmless if the earlier keep-public-API instruction stands.

## Mathlibable assessment (Step 9)

Pre-filter: not private; name not `_aux`; docstring not internal/auxiliary; Step 8 said REPLACE (not REMOVE); qualified name `Roth.diag_sub` not in mathlib (no `namespace Roth` under `.lake/packages/mathlib/Mathlib/`). Not a pure `rfl` glue lemma (it applies `map_sub`), so a full run is done. Parent `Roth.diag` is `NO-composable-from-mathlib` (it is literally `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`); the re-aim rule does not force a re-aim for that bucket, but it is applied here at the orchestrator's request: re-aimed target `aeval (fun _ ↦ X) (P - Q) = aeval (fun _ ↦ X) P - aeval (fun _ ↦ X) Q`.

### Baseline (Phase 0)
- lake build: clean (project built per brief; evidence file importing `Roth.MainLemma` compiles with no output)
- decl `Roth.diag_sub`: resolved at Roth/CoeffNorm.lean:199
- kind: theorem
- has sorry: no
- module docstring summary: coefficient norms and diagonal substitution bounds for integer multivariate polynomials (Roth §6, Lemma 9).

### Statement (Phase 1)
- Lean: `theorem diag_sub (P Q : MvPolynomial σ ℤ) : diag (P - Q) = diag P - diag Q`
- Math: for `P, Q ∈ ℤ[x_1, …, x_m]`, `(P − Q)(x, …, x) = P(x, …, x) − Q(x, …, x)`.
- Re-aimed: for any commutative ring `R`, `aeval (fun _ ↦ X) : MvPolynomial σ R →ₐ[R] R[X]` preserves subtraction.

### Size classification
SMALL (one-line statement, one-term proof). Exhaustive literature sweep not triggered; three WebSearch queries run anyway per the brief.

### One-line check
A ring homomorphism preserves subtraction; `diag` is the evaluation (substitution) homomorphism `X_j ↦ x`. Instance of `map_sub`.

### Literature search table
| # | Channel | Query | Result |
|---|---|---|---|
| 1 | WebSearch | polynomial substitution homomorphism preserves subtraction P(x,…,x) diagonal | ProofWiki "Polynomial Evaluation Homomorphism"/"Substitution Homomorphism"; arXiv 1206.6769 (substitution is a ring hom); no named diagonal lemma |
| 2 | WebSearch | evaluation homomorphism multivariate polynomial ring universal property | ProofWiki "Universal Property of Polynomial Ring"; arXiv 1605.04832 (unique hom extending ρ with X_i ↦ b_i) |
| 3 | WebSearch | Lean mathlib map_sub MvPolynomial aeval AlgHom | mathlib docs: `MvPolynomial.eval_sub`, `aeval` as `AlgHom`, `rename = aeval (X ∘ f)` |
| 4 | Local refs | `.mathlib-quality/references/clean.tex` | l.1449 ("replace x_1,…,x_m by the same variable x"); subtraction used implicitly, never stated |
| 5 | LeanSearch | aeval of a difference of multivariate polynomials | `MvPolynomial.eval_sub`, `MvPolynomial.eval₂_sub`, `Polynomial.aeval_sub`, `Polynomial.eval_sub` |
| 6 | Loogle | `MvPolynomial.aeval _ (_ - _) = _` | no hits (mathlib states this via generic `map_sub`) |
| 7 | Mathlib grep | `eval₂_sub`, `map_div` | Mathlib/Algebra/MvPolynomial/CommRing.lean:160; Mathlib/Algebra/Group/Hom/Defs.lean:461 (`map_sub` via to_additive) |
| 8 | ChatGPT MCP | n/a | `ask_chatgpt_math` MCP not configured in this session |
| 9 | nLab / Stacks / MathOverflow | n/a | not needed for a SMALL decl; the fact is the definition of ring homomorphism |

### Literature summary
Folklore: substitution/evaluation maps out of a polynomial ring are ring homomorphisms (universal property), hence additive. No source names the subtraction identity for the diagonal substitution; it is never a standalone result.

### Generality verdict
Literature-standard form: any ring hom preserves subtraction. Project form is the special case `R = ℤ`, `f = aeval (fun _ ↦ X)`. Over any `CommRing R` it compiles by `map_sub` (evidence (1)). Maximally general form is mathlib's `map_sub` itself.

### Modern-idiom verdict
The modern idiom is to bundle `diag` as an `AlgHom` and use `map_sub` directly; a dedicated `_sub` lemma is the pre-bundling idiom.

### Proof strategy verdict
Already optimal: `map_sub _ _ _`.

### Mathlib search-status
Found: `map_sub` (generic, applies to `aeval`), `MvPolynomial.eval₂_sub`. Five methods: lean_local_search/grep (`eval₂_sub`, `map_div`), LeanSearch (5 hits listed), Loogle (no specific hit; generic lemma covers it), Lean-Finder not needed (exact hit found), namespace grep (`Roth` absent).

### Statement-shape verdict
Not mathlib shape: mathlib would not add a `_sub` lemma for an `AlgHom` application; `map_sub` is the canonical form.

### Call sites
| Site | Use | Replacement |
|---|---|---|
| Roth/MainLemma.lean:408 | `simp [map_sub, diag_sub, Polynomial.sub_modByMonic, h]` | `simp only [diag] at h ⊢; simp [map_sub, Polynomial.sub_modByMonic, h]` (compiled, evidence (3)) |

### Composition check
Composable from mathlib in one step: `map_sub (aeval fun _ ↦ X) P Q` (and the project statement by defeq, evidence (2)). Re-aim hit: mathlib has the analogous lemma for the re-aimed target.

Verdict: NO-mathlib-has-it

Next step: none for mathlib. Locally, optionally delete `Roth.diag_sub` and use the replacement at Roth/MainLemma.lean:408, or keep it as a convenience lemma until `diag` is bundled as an `AlgHom`.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.diag_sub/diag_sub_reaim.lean` (imports `Roth.MainLemma`), compiled with `lake env lean` (43 s, no output, success). Contents: (1) re-aimed general form over `[CommRing R]` by `map_sub _ _ _`; (2) exact project statement by `map_sub _ _ _`; (3) the full `eval_hasseDeriv_sub_eq_zero` proof with `diag_sub` removed (unfold `diag` then `simp [map_sub, Polynomial.sub_modByMonic, h]`).
- Greps: `grep -rn diag_sub Roth/` (declaration + MainLemma.lean:408); mathlib `eval₂_sub` (CommRing.lean:160), `map_div` (Hom/Defs.lean:461); `namespace Roth` absent from mathlib.
- Searches as recorded in the literature table (3 WebSearch, LeanSearch, Loogle). Parent report `Roth.diag.md` read (it already notes "diag_sub is map_sub").
