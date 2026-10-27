---
decl: Roth.extend_apply_castSucc
file: Roth/Lattice.lean
line: 92
kind: theorem
visibility: private
verdict: SKIP
cost: n/a
junk: KEEP
rationale: Private one-line simp lemma evaluating the last-coordinate extension d.mapDomain Fin.castSucc + single (Fin.last m) i at j.castSucc; mathlib has Finsupp.cons/tail (front insertion) and Fin.snoc_castSucc for plain functions, but no Finsupp.snoc, so nothing covers this exact Finsupp form.
action: Keep as private helper for its three uses in card_filter_box_fiber_aux (Roth/Lattice.lean:112, 115, 122) next to extend_apply_last; if a Finsupp.snoc/init API is ever added to Mathlib/Data/Finsupp/Fin.lean, replace the extension by Finsupp.snoc and this lemma by the corresponding snoc_castSucc.
---

# Roth.extend_apply_castSucc

## Inventory entry

### `theorem Roth.extend_apply_castSucc`
- **Type**: `∀ {m : ℕ} (d : Fin m →₀ ℕ) (i : ℕ) (j : Fin m), (d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i) j.castSucc = d j` (declared `private lemma`).
- **What**: Extending a finitely supported exponent vector `d : Fin m →₀ ℕ` to `Fin (m + 1)` by pushing it forward along `Fin.castSucc` and putting `i` in the last slot does not change the old coordinates: the extended vector evaluated at `j.castSucc` is `d j`. This is the Finsupp analogue of `Fin.snoc_castSucc`.
- **How**: One `simp` call using mathlib's `Finsupp.mapDomain_apply_of_injective` instantiated at `Fin.castSucc_injective m`; the remaining `Finsupp.single (Fin.last m) i (j.castSucc) = 0` is closed by simp via `Finsupp.single_apply` / `Fin.castSucc_ne_last` (simp lemmas), and `add_zero`.
- **Hypotheses**: none beyond the data `m, d, i, j`; all are used. The codomain `ℕ` could be any `AddZeroClass`/`AddCommMonoid` (`mapDomain` needs `AddCommMonoid`), but the lemma is private and only used at `ℕ`.
- **Uses from project**: `[]` (only mathlib: `Finsupp.mapDomain`, `Finsupp.single`, `Fin.castSucc`, `Fin.last`, `Finsupp.mapDomain_apply_of_injective`, `Fin.castSucc_injective`).
- **Used by**: Roth/Lattice.lean `Roth.card_filter_box_fiber_aux` only (private), at l.112 (bounding coordinates in the box, `Fin.lastCases` castSucc branch), l.115 (injectivity of the extension map in `Finset.card_bij`), l.122 (surjectivity, `hext` ext step). `grep -rn extend_apply_castSucc Roth/` returns only the definition and these three uses. Transitively feeds the public `Roth.card_filter_box_last` (l.130).
- **Visibility**: private
- **Lines**: 92–94, proof length 1 line
- **Notes**: Companion of `Roth.extend_apply_last` (l.96). The extension expression `d.mapDomain Fin.castSucc + Finsupp.single (Fin.last m) i` recurs in `card_filter_box_fiber_aux`, `card_filter_box_last` and `card_filter_fiber_eq`; it is a hand-rolled "Finsupp.snoc".

## Junk check (Step 8)
- Used anywhere? Yes, three times inside `card_filter_box_fiber_aux` (l.112, l.115, l.122), always as a simp lemma alongside `extend_apply_last`.
- Wrapper of 1–2 mathlib calls? Yes: it is `simp [Finsupp.mapDomain_apply_of_injective (Fin.castSucc_injective m)]`. Each use site could instead pass that term to simp directly. But naming it gives a clean simp-normal-form rule for the recurring extension at three sites, matching the paired `extend_apply_last`; this is a reasonable local API, not junk.
- Does mathlib have it? Not in this form. Checked: `Mathlib/Data/Finsupp/Fin.lean` provides only `Finsupp.tail`/`Finsupp.cons` (insertion at index `0` via `Fin.succ`), with `cons_zero`, `cons_succ`, `tail_cons`, etc.; `grep -rn "Finsupp.snoc\|Finsupp.init\|snoc"` over `Mathlib/Data/Finsupp/` finds nothing, so there is no Finsupp snoc/init API and no `castSucc` lemma there. `Fin.snoc_castSucc` (Mathlib/Data/Fin/Tuple/Basic.lean:527) and `Fin.Embedding.snoc_castSucc` (Mathlib/Data/Fin/Tuple/Embedding.lean:74) are the same statement for plain functions and embeddings, not for `→₀`. So mathlib's `Fin.snoc_castSucc` / `Fin.cons` API does not cover it directly. A REPLACE would require either (a) rephrasing the extension via `Finsupp.equivFunOnFinite.symm (Fin.snoc d i)` and then using `Fin.snoc_castSucc` (more coercion noise at every site, not simpler), or (b) reindexing the induction to peel off coordinate `0` and using `Finsupp.cons`/`cons_succ` (a refactor of `card_filter_box_last` and its downstream `Fin.castSucc`-based induction, out of proportion for a 1-line private helper).
- Too specific / inline? Inlining the simp argument at three sites is possible but would duplicate the injectivity term; keeping the named pair is clearer.
- Well-chosen? Yes, given the project's choice of a castSucc/last decomposition; the statement is exactly the rewrite needed.
- Conclusion: `KEEP`. Action: none now; if mathlib gains `Finsupp.snoc` (natural home `Mathlib/Data/Finsupp/Fin.lean`, mirroring `Finsupp.cons`), switch the extension to it and replace this lemma by `Finsupp.snoc_castSucc`.

## Mathlibable assessment (Step 9)

Verdict: SKIP

Skip reason: private (declared `private lemma` at Roth/Lattice.lean:92).

Side note: the only upstreamable idea here is a `Finsupp.snoc`/`Finsupp.init` API mirroring `Finsupp.cons`/`Finsupp.tail` in `Mathlib/Data/Finsupp/Fin.lean`, of which this lemma would be the `snoc_castSucc` member. That is a separate, generic contribution, not this declaration.

## Evidence
- `grep -rn extend_apply_castSucc Roth/`: definition l.92; uses l.112, l.115, l.122 (all in `card_filter_box_fiber_aux`).
- `grep -n` of declarations in `.lake/packages/mathlib/Mathlib/Data/Finsupp/Fin.lean`: only `tail`, `cons` and their lemmas (`cons_zero`, `cons_succ`, `tail_cons`, `cons_tail`, ...).
- `grep -rn "snoc\|def init\|castSucc" .lake/packages/mathlib/Mathlib/Data/Finsupp/`: no hits. `grep -rn "Finsupp.snoc\|Finsupp.init" Mathlib/`: no hits.
- `grep -rn "theorem snoc_castSucc"` in mathlib: `Fin.snoc_castSucc` (Data/Fin/Tuple/Basic.lean:527, functions) and `snoc_castSucc` in Data/Fin/Tuple/Embedding.lean:74 (embeddings); neither applies to `→₀`.
- `Finsupp.mapDomain_apply_of_injective` confirmed at Mathlib/Data/Finsupp/Basic.lean:273 (`@[simp]`, needs injectivity argument).
- No Lean runs and no evidence Lean files: a private SKIP needs no weakening or proof experiments, and the project builds clean, so the lemma compiles as stated.
