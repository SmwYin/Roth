---
decl: Roth.extend_apply_last
file: Roth/Lattice.lean
line: 96
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-line simp lemma evaluating the last-coordinate extension d.mapDomain Fin.castSucc + single (Fin.last m) i at Fin.last m to i; mathlib has Fin.snoc_last for functions and Finsupp.cons/tail (front insertion) but no Finsupp.snoc, so nothing covers this exact Finsupp form.
action: Keep as private helper for its three uses in card_filter_box_fiber_aux (Roth/Lattice.lean:110, 111, 122) next to extend_apply_castSucc; if a Finsupp.snoc/init API is ever added to Mathlib/Data/Finsupp/Fin.lean, replace the extension by Finsupp.snoc and this lemma by the corresponding snoc_last.
---

# Roth.extend_apply_last

## Inventory entry

### `theorem Roth.extend_apply_last`
- **Type**: `∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ), (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) (Fin.last m) = i` (declared `private lemma`).
- **What**: Extending a finitely supported exponent vector `d : Fin m →₀ ℕ` to `Fin (m + 1)` by pushing it forward along `Fin.castSucc` and putting `i` in the last slot gives a vector whose last coordinate is `i`. This is the Finsupp analogue of `Fin.snoc_last`.
- **How**: One `simp` call with mathlib's `Finsupp.mapDomain_of_notMem_range` (Mathlib/Data/Finsupp/Basic.lean:286): `mapDomain Fin.castSucc d (Fin.last m) = 0` because `Fin.last m ∉ Set.range Fin.castSucc` (discharged by simp, via the simp lemma `Fin.range_castSucc`, Mathlib/Data/Fin/SuccPred.lean:241, reducing to `¬ (m < m)`); then `Finsupp.single_eq_same` and `zero_add`.
- **Hypotheses**: none beyond the data `m, d, i`; all are used. The codomain `ℕ` could be any `AddCommMonoid` (needed by `mapDomain`), but the lemma is private and only used at `ℕ`.
- **Uses from project**: `[]` (only mathlib: `Finsupp.mapDomain`, `Finsupp.single`, `Fin.castSucc`, `Fin.last`, `Finsupp.mapDomain_of_notMem_range`).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_box_fiber_aux` only (private), at l.110 (the extended vector lies in the fibre `d (Fin.last m) = i`, used as a term), l.111 (bounding the last coordinate in the box, `Fin.lastCases` last branch, as simp lemma), l.122 (surjectivity, `hext` ext step, as simp lemma). `grep -rn extend_apply_last Roth/` returns only the definition and these three uses. Transitively feeds the public `Roth.card_filter_box_last` (l.130).
- **Visibility**: private
- **Lines**: 96–98, proof length 1 line
- **Notes**: Companion of `Roth.extend_apply_castSucc` (l.92). The extension expression `d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i` recurs in `card_filter_box_fiber_aux`, `card_filter_box_last` and `card_filter_fiber_eq`; it is a hand-rolled "Finsupp.snoc".

## Junk check (Step 8)
- Used anywhere? Yes, three times inside `card_filter_box_fiber_aux` (l.110 directly as a proof term, l.111 and l.122 as a simp lemma alongside `extend_apply_castSucc`).
- Wrapper of 1–2 mathlib calls? Yes: it is `simp [Finsupp.mapDomain_of_notMem_range]`. The simp-argument use sites could pass that lemma directly, but the l.110 use is as a term (the fibre membership goal), where a named lemma is genuinely convenient; and the pair with `extend_apply_castSucc` gives a clean evaluation API for the recurring extension. Reasonable local API, not junk.
- Does mathlib have it? Not in this form. `Mathlib/Data/Finsupp/Fin.lean` provides only `Finsupp.tail`/`Finsupp.cons` (insertion at index `0`); `grep -rln snoc .lake/packages/mathlib/Mathlib/Data/Finsupp/` finds nothing, so there is no Finsupp snoc/init API and no `last`-evaluation lemma. `Fin.snoc_last` (Mathlib/Data/Fin/Tuple/Basic.lean:540) and `Fin.Embedding.snoc_last` (Mathlib/Data/Fin/Tuple/Embedding.lean:78) are the same statement for plain functions and embeddings, not for `→₀`. Replacing would require rephrasing the extension via `Finsupp.equivFunOnFinite.symm (Fin.snoc d i)` (more coercion noise at every site) or reindexing the induction to peel off coordinate `0` and using `Finsupp.cons_zero` (refactor of `card_filter_box_last` and downstream), out of proportion for a 1-line private helper.
- Too specific / inline? Inlining is possible at the simp sites, but the term use at l.110 and the symmetry with `extend_apply_castSucc` favour keeping it.
- Well-chosen? Yes, given the project's castSucc/last decomposition; the statement is exactly the rewrite needed.
- Conclusion: `KEEP`. Action: none now; if mathlib gains `Finsupp.snoc` (natural home `Mathlib/Data/Finsupp/Fin.lean`, mirroring `Finsupp.cons`), switch the extension to it and replace this lemma by `Finsupp.snoc_last`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:96).

Side note: as for `Roth.extend_apply_castSucc`, the only upstreamable idea is a `Finsupp.snoc`/`Finsupp.init` API mirroring `Finsupp.cons`/`Finsupp.tail` in `Mathlib/Data/Finsupp/Fin.lean`, of which this lemma would be the `snoc_last` member. That is a separate, generic contribution, not this declaration.

## Evidence
- `grep -rn extend_apply_last Roth/`: definition l.96; uses l.110, l.111, l.122 (all in `card_filter_box_fiber_aux`).
- `Finsupp.mapDomain_of_notMem_range` confirmed at Mathlib/Data/Finsupp/Basic.lean:286 (needs `a ∉ Set.range f`); `Fin.range_castSucc` is `@[simp]` at Mathlib/Data/Fin/SuccPred.lean:241, which lets simp discharge the side condition.
- `grep -rln snoc .lake/packages/mathlib/Mathlib/Data/Finsupp/`: no hits (no Finsupp snoc API).
- `grep -rn "theorem snoc_last"` in mathlib: `Fin.snoc_last` (Data/Fin/Tuple/Basic.lean:540, functions) and `snoc_last` in Data/Fin/Tuple/Embedding.lean:78 (embeddings); neither applies to `→₀`.
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
