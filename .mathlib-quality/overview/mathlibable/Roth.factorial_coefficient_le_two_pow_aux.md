---
decl: Roth.factorial_coefficient_le_two_pow_aux
file: Roth/Theta.lean
line: 609
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private natural-number arithmetic step of Lemma 7 bounding the non-B factors of lem6M, (r1+1)^(pl) l! 2^(pl r1), by 2^((2p+1) r1 l) when l is at most 2^r1; a 2-step calc from Nat.lt_two_pow_self and Nat.factorial_le_pow with no mathlib counterpart in this shape.
action: Keep as private helper for its sole use in lem6M_lt (Roth/Theta.lean:658); no upstream action.
---

# Roth.factorial_coefficient_le_two_pow_aux

## Inventory entry

### `theorem Roth.factorial_coefficient_le_two_pow_aux`
- **Type**: `∀ (p r₁ l : ℕ), l ≤ 2 ^ r₁ → (r₁ + 1) ^ (p * l) * l.factorial * 2 ^ (p * l * r₁) ≤ 2 ^ ((2 * p + 1) * r₁ * l)` (declared `private lemma`, all in `ℕ`).
- **What**: If `l ≤ 2^{r₁}` then `(r₁+1)^{pl} · l! · 2^{p l r₁} ≤ 2^{(2p+1) r₁ l}`. These are exactly the factors of `lem6M p r₁ B l = (r₁+1)^{pl} l! B^l 2^{p l r₁}` other than `B^l`; the lemma is the "the remaining factors are at most `2^{(2p+1) r₁ l}`" step of the source's proof of Lemma 7 (§5).
- **How**: Two-step `calc`. Step 1: `gcongr` reduces to `r₁ + 1 ≤ 2^{r₁}` (closed by `Nat.lt_two_pow_self`) and `l! ≤ (2^{r₁})^l` (closed by `Nat.factorial_le_pow l` composed with `Nat.pow_le_pow_left hl`). Step 2: the identity `(2^{r₁})^{pl} (2^{r₁})^l 2^{p l r₁} = 2^{(2p+1) r₁ l}` by `rw [← pow_mul, ← pow_mul, ← pow_add, ← pow_add]` and `ring_nf`.
- **Hypotheses**: `hl : l ≤ 2 ^ r₁` (used only for the factorial bound `l! ≤ l^l ≤ (2^{r₁})^l`). Necessary in some form: without a bound on `l` relative to `r₁` the claim fails (e.g. `p = 0, r₁ = 0, l = 2`: `2! = 2 > 1 = 2^0`). Already the natural weak form (the call site has the stronger `l ≤ r₁` and weakens it).
- **Uses from project**: `[]` (only mathlib/core: `Nat.lt_two_pow_self`, `Nat.factorial_le_pow`, `Nat.pow_le_pow_left`, `pow_mul`, `pow_add`, `gcongr`, `ring_nf`).
- **Used by**: Roth/Theta.lean `Roth.lem6M_lt` only (l.658, `exact_mod_cast factorial_coefficient_le_two_pow_aux p r₁ l (hl'.trans Nat.lt_two_pow_self.le)`, to get the real-valued `hnatR`). `grep -rn factorial_coefficient_le_two_pow_aux Roth/` returns only the definition (l.609) and this use.
- **Visibility**: private
- **Lines**: 609–618, proof length 8 lines (611–618)
- **Notes**: Name ends in `_aux`; would also be caught by the Step 9a pre-filter. Stated in `ℕ` and cast to `ℝ` at the call site, which keeps the arithmetic in the easier semiring.

## Junk check (Step 8)
- Used anywhere? Yes, once: `Roth.lem6M_lt` (public, Lemma 7 support), l.658.
- Wrapper of 1–2 mathlib calls? Close to it but not literally: two mathlib inequalities (`Nat.lt_two_pow_self`, `Nat.factorial_le_pow`) plus `Nat.pow_le_pow_left` combined by `gcongr`, then an exponent-arithmetic identity. Its content is the specific exponent bookkeeping `pl r₁ + l r₁ + p l r₁ = (2p+1) r₁ l`.
- Does mathlib have it? No. Mathlib has the ingredients (`Nat.factorial_le_pow : n ! ≤ n ^ n` in Mathlib/Data/Nat/Factorial/Basic.lean:183; core `Nat.lt_two_pow_self`, `Nat.pow_le_pow_left`), but no lemma bounding this particular product; its shape is dictated by the project's `lem6M` (Roth/Theta.lean:270).
- Too specific / inline? It could be inlined into `lem6M_lt` as a `have`, but separating it keeps the ℕ arithmetic (proved in ℕ, then `exact_mod_cast`) out of the real-analytic calc in `lem6M_lt`, and its sibling `two_pow_lt_rpow_aux` follows the same pattern. Keeping it separate is reasonable.
- Well-chosen? Yes; the single hypothesis is the minimal natural one and is used.
- Conclusion: `KEEP`. Action: none.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Theta.lean:609); additionally the name ends in `_aux`.

Side note: the upstreamable content, if any, would be the generic ingredients, which mathlib already has (`Nat.factorial_le_pow`, `Nat.lt_two_pow_self`).

## Evidence
- `grep -rn factorial_coefficient_le_two_pow_aux Roth/`: definition l.609, sole use l.658 (`lem6M_lt`).
- Read Roth/Theta.lean l.595–665 (this lemma, `two_pow_lt_rpow_aux`, `lem6M_lt`) and the definition of `lem6M` (l.270–271) to confirm the "What" and the call site.
- `grep` of `.lake/packages/mathlib/Mathlib/` and the core toolchain: `Nat.factorial_le_pow` (Mathlib/Data/Nat/Factorial/Basic.lean:183), `Nat.pow_le_pow_left` (Init/Data/Nat/Basic.lean:804); no combined product bound of this shape.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening experiments, and the project builds clean, so the lemma compiles as stated. The counterexample showing `hl` is needed (`p = 0, r₁ = 0, l = 2`) is by hand arithmetic.
