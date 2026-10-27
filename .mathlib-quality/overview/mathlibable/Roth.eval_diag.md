---
decl: Roth.eval_diag
file: Roth/CoeffNorm.lean
line: 193
kind: theorem
visibility: public
verdict: SKIP
cost: n/a
junk: REMOVE
rationale: Unused in the project (its only former call site, eval_hasseDeriv_sub_eq_zero, was rewritten in 96928fd to inline MvPolynomial.comp_aeval_apply + Polynomial.aeval_X), and re-aimed at diag = aeval (fun _ ↦ X) it is exactly comp_aeval_apply plus aeval_X over any CommSemiring (compiled); Step 8 REMOVE fires the Step 9a pre-filter.
action: Delete Roth.eval_diag from Roth/CoeffNorm.lean:190-195 (no call sites in Roth/ or Roth.lean); its content is already spelled inline at Roth/MainLemma.lean:409-410 via MvPolynomial.comp_aeval_apply and Polynomial.aeval_X; deletion needs user sign-off per the earlier keep-public-API instruction.
---

# Roth.eval_diag

## Inventory entry

### `theorem Roth.eval_diag`
- **Type**: `{σ : Type*} (P : MvPolynomial σ ℤ) (x : ℝ) : Polynomial.eval x (Polynomial.map (Int.castRingHom ℝ) (diag P)) = eval (fun _ ↦ x) (map (Int.castRingHom ℝ) P)`
- **What**: Evaluating the diagonal polynomial `P(x, …, x)` (pushed to `ℝ[x]`) at a real `x` equals evaluating `P` (pushed to real coefficients) at the diagonal point `(x, …, x)`.
- **How**: `induction P using MvPolynomial.induction_on <;> simp_all [diag]` (constants, sums, multiplication by `X_i`; all closed by simp).
- **Hypotheses**: none.
- **Uses from project**: `Roth.diag`
- **Used by**: unused in project. `grep -rn eval_diag Roth Roth.lean` finds only the declaration at Roth/CoeffNorm.lean:193. Its one former use (`rwa [hasseDeriv_map, ← eval_diag, ...]` in `eval_hasseDeriv_sub_eq_zero`, Roth/MainLemma.lean) was removed in commit `96928fd` ("Generalize Hasse subtraction evaluation to commutative rings"), which replaced it by `simpa [..., diag, MvPolynomial.comp_aeval_apply, Polynomial.aeval_X]` (Roth/MainLemma.lean:409-410) so that the evaluation could take values in any commutative ring.
- **Visibility**: public
- **Lines**: 190–195 (docstring 190–192, statement 193–195), proof length 1 line
- **Notes**: Source: §6 proof of Lemma 9 (clean.tex l.1511, "`Δ_j W^*(x_1, …, x_m)` are zero when `x_1 = ⋯ = x_m = α`"). Stated over `ℤ → ℝ` only; the general statement holds for any `CommSemiring R` and `R`-algebra `S`.

## Junk check (Step 8)
- Used anywhere? No. There are no call sites in `Roth/` or `Roth.lean`; the sole former caller now inlines the mathlib composition.
- Wrapper of 1–2 mathlib calls? Yes. Re-aimed at `diag = aeval (fun _ ↦ Polynomial.X)` (parent report `Roth.diag.md`), the general statement `Polynomial.aeval x (aeval (fun _ ↦ X) P) = aeval (fun _ ↦ x) P` is `simp [MvPolynomial.comp_aeval_apply, Polynomial.aeval_X]` or `rw [← AlgHom.comp_apply, MvPolynomial.comp_aeval]; simp`; the project's `eval ∘ map` form follows by `rw [Polynomial.eval_map, MvPolynomial.eval_map]` and then that lemma by defeq (evidence (1), (1b), (3)).
- Does mathlib have it? Yes, as `MvPolynomial.comp_aeval_apply` (Mathlib/Algebra/MvPolynomial/Eval.lean:612) at `φ := Polynomial.aeval x`, `f := fun _ ↦ X`, plus `Polynomial.aeval_X`.
- Too specific (inline?)? There is nothing to inline into (no callers); the single historical caller already inlines it.
- Well-chosen? The `ℤ`/`ℝ` specialisation is narrower than the caller now needs (any commutative ring), which is why it fell out of use.
- Conclusion: `REMOVE`. Delete Roth/CoeffNorm.lean:190-195. Note that the earlier cleanup pass kept public API by explicit user instruction, so deletion needs the user's sign-off; the minimal alternative is to keep it but restate it generally as the `comp_aeval_apply` one-liner.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: Step 8 said REMOVE (unused in the project, and its content is mathlib's `MvPolynomial.comp_aeval_apply` plus `Polynomial.aeval_X` after re-aiming `diag` at `aeval (fun _ ↦ X)`). This fires the Step 9a pre-filter. The other pre-filter checks were also run: not private; name does not end in `_aux`; docstring does not start with internal/auxiliary; the qualified name `Roth.eval_diag` is absent from mathlib (no `namespace Roth` in `.lake/packages/mathlib/Mathlib/`). It is not a glue lemma (the proof is an induction, not `rfl`/unfolding).

Re-aim check (requested by the orchestrator, per the mathlibable re-aim rule): the parent `Roth.diag` is `NO-composable-from-mathlib` (literally `MvPolynomial.aeval (fun _ ↦ Polynomial.X)`), not `NO-mathlib-has-it`, so the re-aim rule does not force a full run; it was applied anyway as a verification. Re-aimed at `aeval (fun _ ↦ X)`, mathlib already has the analogous lemma: `MvPolynomial.comp_aeval_apply (φ : S₁ →ₐ[R] B) p : φ (aeval f p) = aeval (fun i ↦ φ (f i)) p` with `φ = Polynomial.aeval x`, closed by `Polynomial.aeval_X`. This compiles over any `CommSemiring R` and `R`-algebra `S` (evidence (1), (1b)), and the exact project statement is recovered by two `eval_map` rewrites (evidence (3)). Had the pre-filter not fired, the verdict would be `NO-mathlib-has-it` (re-aim hit): nothing to upstream.

## Evidence
- Evidence file `.mathlib-quality/overview/evidence/Roth.eval_diag/eval_diag_compose.lean` (imports `Roth.CoeffNorm`). First check failed with `typeclass instance problem is stuck Semiring ?m` because `Polynomial.X` lacked a type ascription, and the first attempts at (3) via `simpa` did not close; after ascribing `(Polynomial.X : Polynomial R)` and closing (3) with `rw [Polynomial.eval_map, MvPolynomial.eval_map]; exact aeval_aeval_X (S := ℝ) P x` (found with `lean_multi_attempt`), `lean_diagnostic_messages`: success, no diagnostics. Contents: (1) `aeval_aeval_X` over `[CommSemiring R] [Algebra R S]` via `MvPolynomial.comp_aeval`; (1b) the same by `simp [comp_aeval_apply, Polynomial.aeval_X]`; (2) the same by the project's `induction_on <;> simp_all`; (3) the exact `Roth.eval_diag` statement recovered from (1).
- Project greps: `grep -rn eval_diag Roth Roth.lean` (only the declaration); `git log -S eval_diag -- Roth` (introduced `3cab03b`, last caller removed `96928fd`; `git show 96928fd` shows the removed line `rwa [hasseDeriv_map, ← eval_diag, ← algebraMap_int_eq, Polynomial.eval_map_algebraMap]`); Roth/MainLemma.lean:402-411 read (current inline `comp_aeval_apply` spelling).
- Mathlib grep: `comp_aeval` (Mathlib/Algebra/MvPolynomial/Eval.lean:607), `comp_aeval_apply` (l.612), `MvPolynomial.eval_map` (l.432), `Polynomial.eval_map` (Mathlib/Algebra/Polynomial/Eval/Defs.lean:577).
- Loogle `Polynomial.aeval _ (MvPolynomial.aeval _ _)`: no hits (stated via `AlgHom` composition in mathlib). LeanSearch (evaluation after substitution): `MvPolynomial.polynomial_eval_eval₂`, `MvPolynomial.eval_eval₂`, `MvPolynomial.aeval_bind₁`, `MvPolynomial.eval_assoc` (all the same substitution-then-evaluate principle). Lean-Finder: `MvPolynomial.aeval_toMvPolynomial`, `MvPolynomial.eval_toMvPolynomial` (related).
- WebSearch: 3 queries (diagonal substitution / evaluation homomorphism; universal property `P(f_1,…,f_n)(a) = P(f_1(a),…,f_n(a))` — ProofWiki "Evaluation Homomorphism", Wikipedia "Polynomial ring"; Roth's theorem auxiliary polynomial at `(α, …, α)` — arXiv 2502.00731, Evertse notes): folklore consequence of the universal property, never a named lemma. Local refs: clean.tex l.1449, l.1511. ChatGPT MCP: n/a (`ask_chatgpt_math` not configured in this session). Full nine-channel `/mathlibable` artifacts not produced because the Step 9a pre-filter fired (SKIP).
