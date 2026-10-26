---
decl: MvPolynomial.taylor_apply
file: Roth/Taylor.lean
line: 46
kind: theorem
visibility: public
verdict: INHERITED-YES-add-as-is
cost: CHEAP
junk: KEEP
rationale: Pure rfl unfolding lemma of MvPolynomial.taylor (taylor α P = aeval (X + C α) P); multivariate analogue of mathlib's Polynomial.taylor_apply, ships with the parent.
action: Upstream with MvPolynomial.taylor in a new Mathlib/Algebra/MvPolynomial/Taylor.lean; locally keep as the named unfolding lemma (currently no project call site; Roth/Index.lean:243 uses the univariate Polynomial.taylor_apply).
---

# MvPolynomial.taylor_apply

## Inventory entry

### `theorem MvPolynomial.taylor_apply`
- **Type**: `∀ {σ R : Type*} [CommSemiring R] (α : σ → R) (P : MvPolynomial σ R), taylor α P = aeval (fun j ↦ X j + C (α j)) P`
- **What**: The translate `P(X + α)` is the evaluation of `P` at the point `X + α` (substitution `X j ↦ X j + α j`).
- **How**: `rfl` (the definition of `taylor` is `aeval fun j ↦ X j + C (α j)`).
- **Hypotheses**: `[CommSemiring R]` (section variable); none else.
- **Uses from project**: `MvPolynomial.taylor`
- **Used by**: unused in project (`grep -rn taylor_apply Roth/` finds only the declaration and Roth/Index.lean:243, which is mathlib's univariate `Polynomial.taylor_apply`; not `@[simp]`, so no implicit uses).
- **Visibility**: public
- **Lines**: 45–47, proof length 1 line (`rfl`)
- **Notes**: Name and role mirror mathlib's `Polynomial.taylor_apply : taylor r f = f.comp (X + C r)` (Mathlib/Algebra/Polynomial/Taylor.lean:43), which mathlib uses heavily as the unfolding lemma.

## Junk check (Step 8)
- Used anywhere? Not by name in the project; other project lemmas unfold `taylor` directly (`simp [taylor, ...]`).
- Wrapper of 1–2 mathlib calls? It is the `rfl` unfolding lemma of a project def, the standard `_apply` API lemma mathlib provides for the univariate operator; it lets downstream users avoid unfolding the def.
- Does mathlib have it? No: namespace-aware grep of `.lake/packages/mathlib/Mathlib/` finds only `Polynomial.taylor_apply`.
- Too specific? No.
- Well-chosen? Yes; matches univariate naming.
- Conclusion: `KEEP`. Action: keep; upstream with the parent (a mathlib reviewer would expect it; it could also replace the local `simp [taylor, ...]` unfoldings).

## Mathlibable assessment (Step 9)
Inherited from: MvPolynomial.taylor

Pre-filter: not private, no `_aux` / internal docstring, Step 8 KEEP, qualified name `MvPolynomial.taylor_apply` absent from mathlib (only `Polynomial.taylor_apply`), so no SKIP. The proof is literally `:= rfl` (Roth/Taylor.lean:47), so this is a genuine glue lemma about the already-assessed parent `MvPolynomial.taylor`, whose verdict is `YES-add-as-is` (not `NO-mathlib-has-it`), so the re-aim rule does not apply. Verdict `INHERITED-YES-add-as-is`, cost CHEAP. Next step: include in the parent's upstream PR (Mathlib/Algebra/MvPolynomial/Taylor.lean), mirroring `Polynomial.taylor_apply`.

## Evidence
- Source read: Roth/Taylor.lean:44-47, proof `rfl` (compiles as part of the clean project build; no separate evidence file needed).
- `grep -rn taylor_apply Roth/`: declaration plus Roth/Index.lean:243 (univariate `Polynomial.taylor_apply`).
- `grep -rn taylor_apply .lake/packages/mathlib/Mathlib/`: only Mathlib/Algebra/Polynomial/Taylor.lean (univariate, l.43, and its uses).
- Parent report: .mathlib-quality/overview/mathlibable/MvPolynomial.taylor.md (YES-add-as-is; its evidence probes.lean confirms `taylor α = aeval ...` by `rfl`).
